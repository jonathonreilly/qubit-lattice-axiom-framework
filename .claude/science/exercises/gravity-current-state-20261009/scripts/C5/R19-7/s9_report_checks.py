"""R19-7 s9: recompute the ratios quoted in the report from the s2 text outputs (no rounding by hand)."""
import sys, glob, numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from parse_out import parse
C = {"cube2": parse(["s2_scan_cube2.out"]), "tilt3": parse(["s2_scan_tilt3.out"]),
     "tilt4": parse(["s2_scan_tilt4_partA.out"] + sorted(glob.glob("s2_scan_tilt4_b*.out")))}
kmin = {"cube2": 1, "tilt3": 1, "tilt4": 1}
for tag, D in C.items():
    rV = []; rS = []; sS = []; Vv = []
    for (bU, v), d in sorted(D.items()):
        t2 = d.get(("axis", kmin[tag], "TT2"), (0, None)); V1 = d.get(("axis", kmin[tag], "V1"), (0, None)); S1 = d.get(("axis", kmin[tag], "S1"), (0, None))
        t20 = d.get(("axis", 0, "TT2"), (0, None))
        if t2[1] and V1[1] is not None: rV.append((V1[1]/t2[1], bU, v)); Vv.append((V1[1], bU, v))
        if t2[1] and S1[1] is not None: rS.append((S1[1]/t2[1], bU, v))
        if t2[0] > 0 and t20[0] > 0: sS.append((t20[0]/t2[0], bU, v))
    print(tag, "points", len(D))
    print("   V/T2 main pole at kmin: min %s  max %s" % (min(rV), max(rV)))
    print("   V main pole at kmin: min %s max %s ; points with V/T2 < 1.3: %s" % (min(Vv), max(Vv), [x for x in rV if x[0] < 1.3]))
    if rS: print("   S/T2 at kmin: min %s max %s" % (min(rS), max(rS)))
    print("   S_TT2(k=0)/S_TT2(kmin): max %s  min %s" % (max(sS), min(sS)))
