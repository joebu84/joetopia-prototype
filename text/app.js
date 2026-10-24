// Browser shell for the Joetopia TEXT RPG. All game logic is the Android engine compiled to JS (JoetopiaText facade);
// this file only mirrors MainActivity's layout and behaviour.
(function () {
  'use strict';
  const T = JoetopiaKt.com.grokbot.joetopia.game.JoetopiaText;
  T.setArt(window.TEXT_ART || '');
  const has = new Set((window.TEXT_ART || '').split(','));
  const $ = (id) => document.getElementById(id);
  const story = $('story'), content = $('content'), picture = $('picture'), choicesEl = $('choices'), nameInput = $('nameInput');
  let pictureId = null, follow = true, toastTimer = 0;

  function toast(msg) {
    const t = $('toast'); t.textContent = msg; t.hidden = false;
    clearTimeout(toastTimer); toastTimer = setTimeout(() => { t.hidden = true; }, 2200);
  }
  const fire = (w) => (w >= 9 ? '  🔥🔥🔥' : w >= 5 ? '  🔥🔥' : w >= 2 ? '  🔥' : '');
  // Like the APK: prefer the wide event banner in the panel; tapping opens the full portrait.
  const src = (id, prefer) => {
    const order = prefer === 'portraits' ? ['portraits', 'events'] : ['events', 'portraits'];
    for (const f of order) if (has.has(id) && fileExists(f, id)) return 'art/' + f + '/' + id + '.webp';
    return null;
  };
  const folders = window.TEXT_ART_FOLDERS || null;
  function fileExists(folder, id) { return !folders || (folders[folder] && folders[folder].has(id)); }

  // StoryScroll: jump to the newest text, and keep following later layout changes (picture loading) until the user scrolls.
  function scrollBottom() { story.scrollTop = story.scrollHeight; }
  new ResizeObserver(() => { if (follow) scrollBottom(); }).observe(content);
  ['wheel', 'touchmove'].forEach((ev) => story.addEventListener(ev, () => { follow = false; }, { passive: true }));
  story.addEventListener('keydown', () => { follow = false; });

  function showPicture(id) {
    if (id === pictureId) return;
    pictureId = id;
    const s = id ? src(id, 'events') : null;
    // Hide the old picture at once and show the new one only when it has loaded, so a stale image never sits under a new scene.
    picture.hidden = true;
    if (s) { picture.onload = () => { if (pictureId === id) picture.hidden = false; }; picture.src = s; } else { picture.onload = null; picture.removeAttribute('src'); }
  }

  function render() {
    const st = JSON.parse(T.status());
    const sc = JSON.parse(T.scene());
    $('status').hidden = !st.inGame;
    $('stats').textContent = st.line;
    $('hpBar').style.width = Math.max(0, Math.min(100, 100 * st.hp / Math.max(1, st.maxHp))) + '%';
    $('mpBar').style.width = Math.max(0, Math.min(100, 100 * st.mp / st.maxMp)) + '%';
    $('viewsBar').style.width = Math.min(100, 100 * st.v / st.vMax) + '%';
    $('viewsText').textContent = st.views;
    const live = $('liveBtn');
    live.textContent = st.streaming ? '● LIVE' : '○ OFF';
    live.className = 'small ' + (st.streaming ? 'on' : 'off');
    live.disabled = !(st.canStream || st.streaming);
    document.querySelectorAll('.menu').forEach((b) => { b.disabled = !st.menus; });
    $('saveBtn').disabled = !st.canSave;

    const title = $('title');
    title.textContent = sc.title;
    title.className = sc.mode === 'TITLE' ? 'big' : '';
    $('body').textContent = sc.text;
    showPicture(sc.picture);
    const naming = sc.mode === 'CREATE_NAME';
    nameInput.hidden = !naming;
    if (!naming && document.activeElement === nameInput) nameInput.blur();

    follow = true;
    requestAnimationFrame(scrollBottom);

    choicesEl.textContent = '';
    sc.choices.forEach((c, i) => {
      const b = document.createElement('button');
      b.className = 'choice';
      b.textContent = c.label + (st.streaming ? fire(c.watch) : '');
      b.disabled = !c.enabled;
      b.addEventListener('click', () => {
        T.choose(i, T.mode() === 'CREATE_NAME' ? nameInput.value : '');
        render();
        choicesEl.scrollTop = 0;
      });
      choicesEl.appendChild(b);
    });
  }

  $('liveBtn').onclick = () => { if (T.toggleStream()) render(); else toast('You need a streaming device (phone, drone, camera, wand-cam or meta glasses).'); };
  $('gearBtn').onclick = () => { if (T.gear()) render(); else toast('Not during an encounter.'); };
  $('statsBtn').onclick = () => { if (T.stats()) render(); else toast('Not during an encounter.'); };
  $('mycoBtn').onclick = () => { if (T.myco()) render(); else toast('Not during an encounter.'); };
  $('saveBtn').onclick = () => { toast(T.save() ? 'Game saved.' : "You can't save right now."); render(); };
  $('menuBtn').onclick = () => { T.toTitle(); render(); };
  picture.onclick = () => {
    if (!pictureId) return;
    $('fullImg').src = src(pictureId, 'portraits'); $('full').hidden = false;
  };
  $('full').onclick = () => { $('full').hidden = true; };
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') { if (!$('full').hidden) $('full').hidden = true; }
  });
  // onPause: autosave whenever saving is allowed (like the APK when the app goes to the background).
  const autosave = () => { try { if (T.canSave()) T.save(); } catch (e) { /* ignore */ } };
  document.addEventListener('visibilitychange', () => { if (document.hidden) autosave(); });
  window.addEventListener('pagehide', autosave);

  window.JoetopiaTextUI = { T, render };
  render();
})();
