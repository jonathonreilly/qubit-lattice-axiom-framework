# Handoff

This branch fixes the source inconsistency in `g_2_v`: the admitted interval
`[0.96,0.98]` does not contain the weak-coupling comparator `0.988`.

The runner now proves the comparator sits above the admitted upper endpoint and
maps to a `g_2` value below the certified interval. This repairs the source
contradiction but does not retire the remaining SU(2) `u_0` import.
