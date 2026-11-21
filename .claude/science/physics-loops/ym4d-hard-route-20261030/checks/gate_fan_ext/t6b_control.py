#!/usr/bin/env python3
import sys
import t6_edge_vs_fan as s
t = s.t
t.watchdog()
t.guard = lambda: None
if sys.argv[1] == "lit":
    lit = {L: t.run(L, "fan", literal=True) for L in (2, 4, 8)}
    print("literal", {k: round(v, 3) for k, v in lit.items()}, "ratios", round(lit[4] / lit[2], 3), round(lit[8] / lit[4], 3))
else:
    print("fan mode L =", sys.argv[2], {k: round(float(v), 3) for k, v in s.mode(int(sys.argv[2])).items()})
