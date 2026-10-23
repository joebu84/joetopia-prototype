// UI TEXT RULES. How engine choices are sorted into dropdowns and icons.
// The choices themselves (and all stat checks) come from the Kotlin engine.
window.JOETOPIA_UI = {
  // Talk menus: first matching group wins. Order here = order on screen.
  talkGroups: [
    ['💬 Talk', /^(Small talk|Ask|Tell|Chat|Gossip|🗣|❓|Listen|Joke|Hug|🤗)/i],
    ['😊 Flirt & Charm', /(😊|💋|Flirt|Seduce|Compliment|Charm|Kiss|Dance with|date)/i],
    ['🙏 Pray, Preach & Debate', /(🙏|Pray|Preach|Debate|Bless|Convert|Sermon|Save|Witness|Gospel)/i],
    ['🍸 Drinks & Trade', /(🍸|Buy|drink|Trade|Sell|Bribe|Pay|Credits|Shop|Browse|Order)/i],
    ['🎓 Class & Skills', /\((Technomancer|Artificer|Dancer|Bouncer|Live-Streamer|TikTok Pastor|Shaman|Geneticist)\)|Scan|Hack|Stream|📺|Film|Train|Learn|Teach/i],
    ['📜 Quests & Favours', /(quest|favour|favor|deliver|shard|Morvane|Ramirez|tryout|Brute Squad|forge|shield|video game|game)/i],
    ['⚔ Fight & Tricks', /(⚔|Attack|Fight|Steal|🤏|Spar|Duel|Challenge|Slip past|Threaten|Intimidate)/i],
  ],
  otherGroup: '✨ Other',
  // Battle command buttons.
  battle: {
    attack: /^(Attack|Defend|⚔|Fight)/i,
    skill: /(\[\d+ MP\]|Call Ramirez|🔨|Quick-draw)/i,
    item: /^Use item/i,
    flee: /^(Flee|Run!?\b)/i,
  },
  // Which marker a "thing to do" gets on the map.
  spotIcons: [
    ['drink', /🍸|drink|Order|mead|cocktail/i], ['dance', /💃|🔥|dance|Freestyle|Perform/i],
    ['rest', /Rest|sleep|bed/i], ['pray', /pray|Kneel|offering|candle|oath|Sigil/i],
    ['forage', /Forage|mushroom|Dive|Drink from/i], ['explore', /Explore|Venture|Search|tunnels|paths|halls/i],
    ['books', /📚|Read|Research|Study|Tour|🏛|🖼|Analyse|archive/i], ['lab', /🧪|Brew|Stitch|Assemble|Synthesize|Culture|Craft|Identify|treated/i],
  ],
  // Toga colour names from the engine -> hex (for the placeholder player sprite).
  togaColors: { 'neon pink': '#ff4fd8', 'electric blue': '#2f7bff', lime: '#9dff3a', tangerine: '#ff9a3d', violet: '#9b5cff',
    gold: '#ffcc33', crimson: '#d81e3c', teal: '#1fc8b4', white: '#f4f4f4' },
};
