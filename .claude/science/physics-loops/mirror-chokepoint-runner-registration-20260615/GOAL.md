# Goal

Unblock `mirror_chokepoint_note` by making its already-cited load-bearing
primary runner parser-visible.

The note already lists the primary runner, primary cache, certificate runner,
and certificate cache at the top. The parser misses the primary runner because
the label is `Primary runner (load-bearing):`. This loop adds standard
`Runner:` and `Runner cache:` lines above the detailed artifact list.
