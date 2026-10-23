package com.grokbot.joetopia.game

import kotlin.js.JsExport
import kotlin.random.Random

/** Saves into the browser's localStorage. */
class WebSaveStore(private val key: String = "joetopia-save") : SaveStore {
    private val getF: dynamic = js("(function(k){try{return globalThis.localStorage ? globalThis.localStorage.getItem(k) : null}catch(e){return null}})")
    private val setF: dynamic = js("(function(k,v){try{if(globalThis.localStorage) globalThis.localStorage.setItem(k,v)}catch(e){}})")
    private val delF: dynamic = js("(function(k){try{if(globalThis.localStorage) globalThis.localStorage.removeItem(k)}catch(e){}})")
    override fun save(data: String) { setF(key, data) }
    override fun load(): String? { val v: dynamic = getF(key); return if (v == null) null else v.unsafeCast<String>() }
    override fun clear() { delF(key) }
}

private fun q(s: String?): String {
    if (s == null) return "null"
    val sb = StringBuilder("\"")
    for (c in s) when (c) {
        '"' -> sb.append("\\\""); '\\' -> sb.append("\\\\"); '\n' -> sb.append("\\n"); '\r' -> {}; '\t' -> sb.append("\\t")
        else -> if (c.code < 0x20) sb.append(" ") else sb.append(c)
    }
    return sb.append('"').toString()
}
private fun obj(vararg kv: Pair<String, Any?>) = kv.joinToString(",", "{", "}") { (k, v) -> q(k) + ":" + jv(v) }
private fun jv(v: Any?): String = when (v) {
    null -> "null"
    is Raw -> v.s
    is String -> q(v)
    is Boolean, is Int, is Long -> v.toString()
    is Double -> if (v.isNaN()) "0" else v.toString()
    is List<*> -> v.joinToString(",", "[", "]") { jv(it) }
    else -> q(v.toString())
}
private class Raw(val s: String)

/** The web front end drives the exact Android engine through this facade. */
@JsExport
object JoetopiaApi {
    private var e = GameEngine(WebSaveStore())

    fun reset(seed: Int) { e = if (seed >= 0) GameEngine(WebSaveStore(), Random(seed)) else GameEngine(WebSaveStore()) }
    fun hasSave(): Boolean = e.hasSave
    fun mode(): String = e.mode.name
    fun node(): String = e.node

    fun scene(): String {
        val s = e.scene()
        return obj("title" to s.title, "text" to s.text, "mode" to e.mode.name, "node" to e.node,
            "choices" to s.choices.map { Raw(obj("label" to it.label, "enabled" to it.enabled, "watch" to it.watch)) })
    }

    fun choose(i: Int, name: String): Boolean { if (e.mode == Mode.CREATE_NAME) e.pendingName = name; return e.choose(i) }

    /** The messages produced by the last action (also part of scene text). */
    fun lastLog(): String = e.log.joinToString("\n\n")

    fun status(): String {
        val p = e.player
        val c = e.combat
        val en = e.encounter
        return obj(
            "name" to p.name, "level" to p.level, "cls" to e.pclass.title, "clsId" to e.pclass.name, "credits" to p.kandi,
            "hp" to p.hp, "maxHp" to p.maxHp, "mp" to p.mp, "maxMp" to p.mpMax, "atk" to e.atk(), "def" to e.def(),
            "cha" to e.statValue(Stat.CHARM), "cun" to e.statValue(Stat.CUNNING), "spi" to e.statValue(Stat.SPIRIT),
            "xp" to p.xp, "xpNext" to p.xpToNext(), "points" to p.statPoints,
            "region" to e.regionName(), "regionKind" to e.regionKind(), "tier" to e.tierOf(e.node), "node" to e.node, "place" to e.placeName(e.node),
            "views" to e.views, "viewsTier" to e.viewsTier(), "streaming" to e.streaming, "canStream" to e.canStream(), "signal" to (e.signal() * 100).toInt(),
            "mode" to e.mode.name, "menus" to e.menusAvailable(), "canSave" to e.canSave(), "hasSave" to e.hasSave, "toga" to e.togaColor(),
            "effects" to p.effects.map { Raw(obj("id" to it.id, "name" to it.name, "left" to it.remaining, "poison" to it.poison, "regen" to it.regen)) },
            "combat" to (c?.let { Raw(obj("enemy" to it.enemy.type.name, "enemyId" to it.enemy.type.id, "hp" to it.enemy.hp, "maxHp" to it.enemy.maxHp,
                "turn" to it.turn, "stunned" to it.stunned, "dazzled" to it.dazzled, "blinded" to it.blinded, "defDown" to it.defDown,
                "ramirez" to it.ramirez, "guards" to it.guards, "spar" to it.spar, "defending" to it.defending, "enraged" to it.enraged)) }),
            "encounter" to (en?.let { Raw(obj("enemy" to it.type.name, "enemyId" to it.type.id, "npc" to it.npcName)) }),
            "talk" to e.talkNpc,
            "street" to e.streetId, "worn" to p.equipped.keys.joinToString(",") { it.name },
            // reality-show episode id + its art id (e.g. "reality_fletcher") so the pop-up shows that host's picture
            "showEpisode" to (if (e.streetId == "reality_show") e.showEpisode else null),
            "streetArt" to (if (e.streetId == "reality_show") Street.episode(e.showEpisode).art else e.streetId),
        )
    }

    fun openMenu(which: String): Boolean = when (which) {
        "gear" -> e.openGear(); "stats" -> e.openStats(); "myco" -> e.openMycopedia()
        "journal" -> if (e.openStats()) { e.openJournal(); true } else false
        else -> false
    }
    fun toggleStream(): Boolean = e.toggleStream()
    fun save(): Boolean = e.save()
    fun load(): Boolean = e.continueGame()
    fun toTitle() = e.toTitle()
    fun placeName(n: String): String = e.placeName(n)
    fun tierOf(n: String): Int = e.tierOf(n)

    /**
     * Works out what each explore choice does by replaying it on a throwaway copy of the game
     * (random hazards off), so the map can show exits, people and shops in the right places.
     */
    fun probe(): String {
        if (e.mode != Mode.EXPLORE) return "[]"
        val labels = e.scene().choices.map { it.label }
        val data = e.serialize()
        val out = mutableListOf<String>()
        for (i in labels.indices) {
            val s = GameEngine(MemorySaveStore(), Random(7 + i))
            var kind = "local"; var target: String? = null; var name: String? = null
            if (e.node != "intro" && s.deserialize(data)) {
                s.encounterRate = 0; s.streetRate = 0; s.indecencyFineChance = 0
                s.teleport(e.node)
                s.flags.clear(); s.flags.addAll(e.flags)
                val sl = s.scene().choices.map { it.label }
                if (sl.getOrNull(i) == labels[i]) {
                    s.choose(i)
                    when {
                        s.mode == Mode.EXPLORE && s.node != e.node -> { kind = "move"; target = s.node; name = s.placeName(s.node) }
                        s.mode == Mode.TALK -> { kind = "talk"; target = s.talkNpc; name = s.talkNpc?.let { s.npcById(it)?.name } }
                        s.mode == Mode.SHOP -> { kind = "shop"; target = s.shopId }
                        s.mode == Mode.MINGLE -> kind = "mingle"
                        s.mode == Mode.ENCOUNTER || s.mode == Mode.COMBAT -> { kind = "fight"; target = (s.encounter?.type ?: s.combat?.enemy?.type)?.id }
                        s.mode == Mode.STREET -> kind = "event"
                    }
                }
            } else if (e.node == "intro") { kind = "move"; target = "village"; name = e.placeName("village") }
            out += obj("i" to i, "label" to labels[i], "kind" to kind, "target" to target, "name" to name)
        }
        return out.joinToString(",", "[", "]")
    }

    /** Test and debug hooks (used by the headless tests and the ?debug=1 console). */
    fun debug(cmd: String, a: String, b: String): String {
        when (cmd) {
            "create" -> { val cls = PlayerClass.byName(a.substringBefore(":")) ?: PlayerClass.BOUNCER; val body = BodyType.entries.firstOrNull { it.name == a.substringAfter(":", "") } ?: BodyType.FITNESS; e.newGame(); e.createCharacter(if (b.isEmpty()) "Tester" else b, cls, bodyType = body) }  // 'CLASS[:BODY]'
            "teleport" -> e.teleport(a)
            "fight" -> e.startFight(Enemies.byId(a) ?: Enemies.ASH_WOLF, e.node, b.ifEmpty { null })
            "encounter" -> e.startEncounter(Enemies.byId(a) ?: Enemies.ASH_WOLF, e.node)
            "street" -> e.startStreet(a)
            "travel" -> e.forceTravel(a, b)
            "hp" -> e.player.hp = a.toInt()
            "atk" -> e.player.baseAtk = a.toInt()
            "credits" -> e.player.kandi = a.toInt()
            "item" -> e.player.addItem(a, if (b.isEmpty()) 1 else b.toInt())
            "gear" -> GearList.byId(a)?.let { if (it !in e.player.ownedGear) e.player.ownedGear += it }
            "flag" -> e.flags += a
            "unflag" -> e.flags -= a
            "views" -> e.debugViews(a.toInt())
            "rates" -> { e.encounterRate = a.toInt(); e.streetRate = b.toInt() }
            // force the country "TEMPTRESS!" ban or the city club creep: nightlife <dance|flirt>
            "undercroft" -> { if (!e.inUndercroft()) e.teleport("d_under"); e.startUnder(a.ifEmpty { "pirates" }) }
            "underroll" -> { if (!e.inUndercroft()) e.teleport("d_under"); e.maybeUndercroft() }
            "scalegate" -> { if (!e.inScalegate()) e.teleport("d_scale"); e.startStreet(a.ifEmpty { "duel" }) }
            "lantern" -> { if (!e.inLantern()) e.teleport("d_lantern"); e.startStreet(a.ifEmpty { "starving_artist" }) }
            "chrome" -> { if (!e.inChrome()) e.teleport("d_chrome"); e.log.clear(); e.startStreet(a.ifEmpty { "courier" }) }
            "chromeroll" -> { val c = e.chromeChance; val r = e.encounterRate; e.chromeChance = b.toIntOrNull() ?: 100; e.encounterRate = maxOf(1, r); e.maybeChrome(); e.chromeChance = c; e.encounterRate = r }
            "spire" -> { if (!e.inSpire()) e.teleport("d_spire"); e.log.clear(); e.startStreet(a.ifEmpty { "runaway_chariot" }) }
            "spireroll" -> { if (!e.inSpire()) e.teleport("d_spire"); val c = e.spireChance; val r = e.encounterRate; e.spireChance = b.toIntOrNull() ?: 100; e.encounterRate = maxOf(1, r); e.maybeSpire(); e.spireChance = c; e.encounterRate = r }
            // set the per-move chances directly (e.g. 'spirechance 0' / 'creatorschance 100' before walking into the Creator Corner)
            "spirechance" -> e.spireChance = a.toInt()
            // Toadstool Forest: 'forest <troll|weirdo|unicorn|pixie|gnome>', 'forestroll [chance]', 'forestforce <unicorn angry|calm|gnome prank|merchant|weirdo 0-3|human 0-3|humangoblin red|blue|wear red|blue|none|clear>'
            "forest" -> { if (!e.inForest()) e.teleport("forest"); e.log.clear(); e.startStreet(a.ifEmpty { "troll" }) }
            "dance" -> { if (!e.onDanceTable()) e.teleport("rave"); e.log.clear(); e.startStreet(a.ifEmpty { Dance.WATER }) }
            "danceroll" -> { if (!e.onDanceTable()) e.teleport("rave"); val c = e.danceChance; val r = e.encounterRate; e.danceChance = 100; e.encounterRate = maxOf(1, r); e.danceForce = a.ifEmpty { null }; e.maybeDance(); e.danceForce = null; e.danceChance = c; e.encounterRate = r }
            "bar" -> { if (!Dance.isBar(e.node)) e.teleport("bar_neon"); e.log.clear(); e.barVariantForce = if (b == "noticed" || b == "missed") 4 else b.toIntOrNull()
                e.shadyNoticeForce = when (b) { "noticed" -> true; "missed" -> false; else -> null }; e.startStreet(a.ifEmpty { Dance.DRINKERS[0] }); e.barVariantForce = null; e.shadyNoticeForce = null }
            "dancechance" -> e.danceChance = a.toIntOrNull() ?: Dance.DANCE_CHANCE
            "drugforce" -> e.drugForce = when (a) { "1", "true" -> true; "0", "false" -> false; else -> null }
            "repair" -> { e.repairChance = 100; e.repairReadyAt = 0; e.teleport(a.ifEmpty { "village" }); e.debugLocals(List(3) { e.makeLocal() }); e.maybeRepairRequest(); e.repairChance = Repairs.REQUEST_CHANCE; e.log.clear(); e.mingleLocals().firstOrNull { n -> n.talks.any { it.label.contains("asks you to fix their") } }?.let { e.openTalk(it.id) } }
            "forestchance" -> { e.forestChance = a.toInt(); e.bigfootChance = b.toIntOrNull() ?: 0; e.forageEncounterScale = if (a.toInt() >= 100) 100 else GameEngine.FORAGE_ENCOUNTER_SCALE }
            "forestroll" -> { if (!e.inForest()) e.teleport("forest"); val c = e.forestChance; val r = e.encounterRate; e.forestChance = a.toIntOrNull() ?: 100; e.encounterRate = maxOf(1, r); e.maybeForest(); e.forestChance = c; e.encounterRate = r }
            "forestforce" -> when (a) {
                "unicorn" -> e.unicornAngryForce = b == "angry"
                "gnome" -> e.gnomePrankForce = b == "prank"
                "weirdo" -> e.weirdoForce = b.toIntOrNull()
                "human" -> e.humanForce = b.toIntOrNull()
                "humangoblin" -> e.humanGoblinBlueForce = if (b.isEmpty()) null else b == "blue"
                "wear" -> {  // 'forestforce wear red|blue|none' (goblin banger colours)
                    e.player.allWorn().toList().filter { it.colors.isNotEmpty() }.forEach { g -> e.player.equipped.entries.firstOrNull { it.value == g }?.key?.let { e.player.unequip(it) } }
                    val g = when (b) { "red" -> Forest.FLANNEL; "blue" -> Forest.WORK_JEANS; else -> null }
                    if (g != null) { e.player.addGear(g); e.player.equip(g) }
                }
                else -> { e.unicornAngryForce = null; e.gnomePrankForce = null; e.weirdoForce = null; e.humanForce = null; e.humanGoblinBlueForce = null }
            }
            "creatorschance" -> e.creatorsShowChance = a.toInt()
            // reality show: force the next episode ('episode fletcher'; 'episode' alone = random), the megarave 1% roll, a Robert joke
            "episode" -> e.showEpisodeForce = a.ifEmpty { null }
            "raveshowchance" -> e.megaraveShowChance = a.toDouble()
            "raveshowroll" -> { val c = e.megaraveShowChance; val r = e.encounterRate; e.megaraveShowChance = b.toDoubleOrNull() ?: 100.0; e.encounterRate = maxOf(1, r); e.maybeMegaraveShow(); e.megaraveShowChance = c; e.encounterRate = r }
            "joke" -> e.robertJoke()
            // wizard couriers / adrenochrome: item counts, use an item, open a buyer's sell list, talk to an NPC, base Spirit
            "count" -> return (e.player.inventory[a] ?: 0).toString()
            "use" -> { e.log.clear(); Items.byId(a)?.let { e.useItem(it) } }
            "sell" -> { e.log.clear(); e.openSellForTest(a) }
            "talk" -> { e.log.clear(); e.openTalk(a) }
            "basespi" -> return e.player.spirit.toString()
            "setspi" -> e.player.spirit = a.toInt()
            "cancelled" -> e.getCancelled()
            "toll" -> e.tollDue = (a.toIntOrNull() ?: 1).coerceIn(GameEngine.TOLL_MIN, GameEngine.TOLL_MAX)
            "courier" -> e.courierForce = a.ifEmpty { null }
            "lanternroll" -> { val c = e.lanternChance; val r = e.encounterRate; e.lanternChance = b.toIntOrNull() ?: 100; e.encounterRate = maxOf(1, r); e.maybeLantern(); e.lanternChance = c; e.encounterRate = r }
            "scaleroll" -> { if (!e.inScalegate()) e.teleport("d_scale"); val c = e.scaleChance; val r = e.encounterRate; e.scaleChance = b.toIntOrNull() ?: 100; e.encounterRate = maxOf(1, r); e.maybeScalegate(); e.scaleChance = c; e.encounterRate = r }
            "nightlife" -> { e.log.clear(); val r = e.encounterRate; val t = e.temptressChance; val c = e.creepChance
                e.encounterRate = maxOf(1, r); e.temptressChance = 100; e.creepChance = 100
                e.afterNightlife(a.ifEmpty { "dance" }); e.encounterRate = r; e.temptressChance = t; e.creepChance = c }
            "nodes" -> return listOf("intro","village","inn","elder","market","crossroads","forest","shrine","hermit","cave","lake","rave","dealer","vip","castle_gate","courtyard","throne",
                "neverland","alchemist","ziggurat","sanctum","alley","guild").joinToString(",")
            "streets" -> return Street.ALL.joinToString(",") { it.id }
            "flags" -> return e.flags.sorted().joinToString(",")
        }
        return e.mode.name
    }
}
