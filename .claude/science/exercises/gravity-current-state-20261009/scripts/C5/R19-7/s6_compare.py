"""R19-7 s6: pre-stated NO-LINEAR / LINEAR tests across clusters (parsed from the s2 text outputs).
Per (bU, v): T2 (TT2 along z) main pole at every axis k (k=0 included); flatness = max/min over axis k;
V1 and S1 main poles at the smallest nonzero axis k (S1 '-' = no weight there); global gap;
size rule (METHOD): T2(k=0) on tilt4 (V=8) / tilt3 (V=6), same family; a shrink beyond 30% (ratio < 0.7) => OPEN there.
Linearity rule (METHOD): needs >= 3 nonzero k on one line; on tilt4 we additionally test the weaker 3-point pattern
k = 0, pi/2, pi: linear requires w(0) < 0.5 w(pi/2) and w(pi/2)/w(pi) in [0.4, 0.85] (sin(k/2)-type)."""
import sys, glob
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from parse_out import parse
C = {"cube2": parse(["s2_scan_cube2.out"]), "tilt3": parse(["s2_scan_tilt3.out"]),
     "tilt4": parse(["s2_scan_tilt4_partA.out"] + sorted(glob.glob("s2_scan_tilt4_b*.out")))}
mx = {"cube2": 1, "tilt3": 1, "tilt4": 2}
def fmt(x): return "-" if x is None else ("%.3g" % x)
print("%-4s %-5s | %-52s | %-52s | %-60s | %-9s | %s" % ("bU", "v", "cube2 T2(k=0,pi) flat | V,S@pi | gap", "tilt3 T2(k=0,2pi/3) flat | V,S@2pi/3 | gap",
      "tilt4 T2(k=0,pi/2,pi) flat | V,S@pi/2 | gap", "t4/t3 k0", "linear-3pt(tilt4)"))
keys = sorted(set().union(*[set(d.keys()) for d in C.values()]))
nviol = 0
for (bU, v) in keys:
    cells = []; k0 = {}; lin = "n/a"
    for tag in ["cube2", "tilt3", "tilt4"]:
        d = C[tag].get((bU, v))
        if d is None: cells.append("(not run)"); k0[tag] = None; continue
        t2 = [d.get(("axis", m, "TT2"), (0, None))[1] for m in range(0, mx[tag] + 1)]
        tv = [x for x in t2 if x is not None and x > 0]
        flat = max(tv)/min(tv) if tv else float('nan')
        vv = d.get(("axis", 1, "V1"), (0, None))[1]; ss = d.get(("axis", 1, "S1"), (0, None))[1]
        cells.append("%s flat=%.2f | V=%s S=%s | g=%.3g" % ("/".join(fmt(x) for x in t2), flat, fmt(vv), fmt(ss), d["gap"]))
        k0[tag] = t2[0]
        if tag == "tilt4" and all(x is not None for x in t2):
            w0, w1, w2 = t2; ok = (w0 < 0.5*w1) and (0.4 <= w1/w2 <= 0.85)
            lin = "LINEAR-pattern" if ok else "not linear (w0/w(pi/2)=%.2f, w(pi/2)/w(pi)=%.2f)" % (w0/w1, w1/w2)
    rat = (k0["tilt4"]/k0["tilt3"]) if (k0.get("tilt4") and k0.get("tilt3")) else float('nan')
    flag = " <-- shrink>30%" if rat == rat and rat < 0.7 else ""
    print("%-4.1f %-5.2f | %-52s | %-52s | %-60s | %-9s | %s%s" % (bU, v, cells[0], cells[1], cells[2], "%.3f" % rat, lin, flag))
