package com.grokbot.joetopia.game

import kotlin.js.JsExport

/**
 * Facade for the browser version of the TEXT game (joetopia-web/text/): drives the exact Android engine the way
 * MainActivity does (same scene, choices, status line, picture choice via Pictures.idFor). Saves under its own
 * localStorage key so it never touches the top-down World save on the same site.
 */
@JsExport
object JoetopiaText {
    private var e = GameEngine(WebSaveStore("joetopia-text-save"))
    private var available: Set<String> = emptySet()

    /** Art ids bundled with the page (same set the APK bundles: art/portraits + art/events). */
    fun setArt(csv: String) { available = csv.split(",").filter { it.isNotBlank() }.toSet() }
    fun mode(): String = e.mode.name

    fun scene(): String {
        val s = e.scene()
        val pic = Pictures.idFor(e, s.text) { it in available }
        val sb = StringBuilder("{")
        sb.append("\"title\":").append(js("JSON.stringify")(s.title) as String)
        sb.append(",\"text\":").append(js("JSON.stringify")(s.text) as String)
        sb.append(",\"mode\":\"").append(e.mode.name).append("\"")
        sb.append(",\"picture\":").append(if (pic == null) "null" else "\"$pic\"")
        sb.append(",\"choices\":[")
        s.choices.forEachIndexed { i, c ->
            if (i > 0) sb.append(",")
            sb.append("{\"label\":").append(js("JSON.stringify")(c.label) as String).append(",\"enabled\":").append(c.enabled).append(",\"watch\":").append(c.watch).append("}")
        }
        return sb.append("]}").toString()
    }

    /** The same three-line status text as the APK's status bar, plus bar values. */
    fun status(): String {
        val p = e.player
        val line = "${p.name} · Lv ${p.level} ${e.pclass.title}  Credits ${p.kandi}\n" +
            "HP ${p.hp}/${p.maxHp}  MP ${p.mp}/${p.mpMax}  ATK ${e.atk()} DEF ${e.def()}\n" +
            "CHA ${e.statValue(Stat.CHARM)} CUN ${e.statValue(Stat.CUNNING)} SPI ${e.statValue(Stat.SPIRIT)}  XP ${p.xp}/${p.xpToNext()}" +
            (if (p.statPoints > 0) "  ★${p.statPoints}" else "") + "  📍${e.regionName()}"
        val views = "📺 Views ${e.views} · ${e.viewsTier()}" + if (e.streaming) " · signal ${(e.signal() * 100).toInt()}%" else ""
        val q = { s: String -> js("JSON.stringify")(s) as String }
        return "{\"line\":${q(line)},\"views\":${q(views)},\"hp\":${p.hp},\"maxHp\":${p.maxHp},\"mp\":${p.mp},\"maxMp\":${maxOf(1, p.mpMax)}," +
            "\"v\":${e.views},\"vMax\":${maxOf(100, (e.views / 100 + 1) * 100)},\"streaming\":${e.streaming},\"canStream\":${e.canStream()}," +
            "\"menus\":${e.menusAvailable()},\"canSave\":${e.canSave()},\"inGame\":${e.mode != Mode.TITLE && e.mode != Mode.HELP && !e.mode.name.startsWith("CREATE")}}"
    }

    fun choose(i: Int, name: String): Boolean { if (e.mode == Mode.CREATE_NAME) e.pendingName = name; return e.choose(i) }
    fun gear(): Boolean = e.openGear()
    fun stats(): Boolean = e.openStats()
    fun myco(): Boolean = e.openMycopedia()
    fun save(): Boolean = e.save()
    fun canSave(): Boolean = e.canSave()
    fun toTitle() = e.toTitle()
    fun toggleStream(): Boolean = e.toggleStream()
    fun hasSave(): Boolean = e.hasSave

    /** Test hooks (?debug=1 and the headless test only). */
    fun debug(cmd: String, a: String, b: String): String {
        when (cmd) {
            "teleport" -> e.teleport(a)
            "bar" -> { if (!Dance.isBar(e.node)) e.teleport("bar_neon"); e.log.clear(); e.startStreet(a.ifEmpty { Dance.DRINKERS[0] }) }
            "fight" -> e.startFight(Enemies.byId(a) ?: Enemies.ASH_WOLF, e.node, b.ifEmpty { null })
            "rates" -> { e.encounterRate = a.toInt(); e.streetRate = b.toInt() }
        }
        return e.mode.name
    }
}
