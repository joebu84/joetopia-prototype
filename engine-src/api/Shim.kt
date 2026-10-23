package com.grokbot.joetopia.game

/** Kotlin/JS has no String.format; this covers the specs the engine uses (%d %+d %s %.Nf %+.Nf %%). */
fun String.format(vararg args: Any?): String {
    val sb = StringBuilder(); var ai = 0; var i = 0
    while (i < length) {
        val c = this[i]
        if (c != '%') { sb.append(c); i++; continue }
        i++
        if (i < length && this[i] == '%') { sb.append('%'); i++; continue }
        var plus = false
        while (i < length && this[i] in "+- 0#") { if (this[i] == '+') plus = true; i++ }
        while (i < length && this[i].isDigit()) i++
        var prec = -1
        if (i < length && this[i] == '.') { i++; var p = 0; while (i < length && this[i].isDigit()) { p = p * 10 + (this[i] - '0'); i++ }; prec = p }
        val conv = this[i]; i++
        val a = args.getOrNull(ai++)
        val s = when (conv) {
            'd' -> { val n = (a as Number).toLong(); (if (plus && n >= 0) "+" else "") + n.toString() }
            'f' -> { val d = (a as Number).toDouble(); val t = d.asDynamic().toFixed(if (prec < 0) 6 else prec) as String; (if (plus && d >= 0) "+" else "") + t }
            else -> a.toString()
        }
        sb.append(s)
    }
    return sb.toString()
}

/** TreeMap stand-in: keeps keys sorted on every insert. */
class SortedMutableMap<K : Comparable<K>, V> : AbstractMutableMap<K, V>() {
    private val backing = LinkedHashMap<K, V>()
    private fun resort() { val e = backing.entries.sortedBy { it.key }.map { it.key to it.value }; backing.clear(); e.forEach { backing[it.first] = it.second } }
    override fun put(key: K, value: V): V? { val had = backing.containsKey(key); val old = backing.put(key, value); if (!had) resort(); return old }
    override val entries: MutableSet<MutableMap.MutableEntry<K, V>> get() = backing.entries
}
fun <K : Comparable<K>, V> sortedMapOf(vararg pairs: Pair<K, V>): MutableMap<K, V> = SortedMutableMap<K, V>().also { m -> pairs.forEach { m[it.first] = it.second } }
