"""R19-1 s4: summary table + pre-registered equilibration criterion (METHOD (b)).
Reference E/edge (R18-1 s5b_pinch_table.out; focused ladder ptB where it exists): see REF."""
import numpy as np, glob, sys, os
sys.path.insert(0, '.')
from an_fs import table
REF = {(6, 0.0): 0.37522, (8, 0.0): 0.37496, (6, 0.5): 0.27241, (8, 0.5): 0.27223, (6, 1.0): 0.19225, (8, 1.0): 0.19205,
       (6, 2.0): 0.08411, (8, 2.0): 0.08452, (6, 3.0): 0.03151, (8, 3.0): 0.03263, (6, 3.5): 0.01729, (8, 3.5): 0.01971}
runs = {}
for p in sorted(glob.glob('../data/fs_L*_b*_s*.pkl')):
    res, rows = table(p); key = (res['L'], res['bU'])
    runs.setdefault(key, []).append((p, res, {(r[0], r[1], r[2]): r for r in rows}))
print("Equilibration criterion: (i) |E/edge - REF| <= 2%% per seed; (ii) seeds agree on f and S (axis, m=1, TT1/TT2/V1/S1) within 3 sigma.\n")
acc = {}
for key in sorted(runs):
    L, bU = key; lst = runs[key]; ok_i = []
    for p, res, rr in lst:
        E = res['Eb'].mean(); dev = (E - REF[key])/REF[key]; ok_i.append(abs(dev) <= 0.02)
        print("L=%d bU=%.1f %s: E/edge=%.5f (REF %.5f, dev %+.1f%%) neq=%d every=%d -> (i) %s" % (L, bU, os.path.basename(p), E, REF[key], 100*dev, res['neq'], res['every'], "PASS" if ok_i[-1] else "FAIL"))
    good = [x for x, o in zip(lst, ok_i) if o]
    ok_ii = None
    if len(good) >= 2:
        a, b = good[0][2], good[1][2]; ok_ii = True; worst = 0
        for ch in ["TT1", "TT2", "V1", "S1"]:
            ra, rb = a[("axis", 1, ch)], b[("axis", 1, ch)]
            for (va, ea, vb, eb) in [(ra[4], ra[5], rb[4], rb[5]), (ra[6], ra[7], rb[6], rb[7])]:
                z = abs(va - vb)/np.sqrt(ea**2 + eb**2 + 1e-30); worst = max(worst, z)
                if z > 3: ok_ii = False
        print("   (ii) seeds %s vs %s: worst |diff|/sigma = %.2f -> %s" % (os.path.basename(good[0][0]), os.path.basename(good[1][0]), worst, "PASS" if ok_ii else "FAIL"))
    allpass = all(ok_i)   # conservative reading (stated in the report): every seed run must pass (i); no seed selection
    acc[key] = (bool(ok_ii) and allpass, good if len(good) >= 2 else lst)
    print("   => %s\n" % ("ACCEPTED" if (ok_ii and allpass) else "NOT ACCEPTED (a seed fails (i), fewer than two seeds, or seed disagreement)"))
print("\nomega_SMA = f/S (units t) at the two smallest |k| per direction, ACCEPTED points, seed-averaged (first two passing seeds).")
print("TT1/TT2 = R18-1's two transverse-traceless polarizations; along axis z: TT1=(yy-xx)/sqrt2 (E), TT2=sqrt2 sym(y,-x) (T2).")
hdr = "%-3s %-4s %-4s %-2s %-4s %8s %9s %9s %10s" % ("L", "bU", "dir", "m", "ch", "q2", "S", "f", "f/S")
print(hdr)
for key in sorted(acc):
    ok, good = acc[key]
    if len(good) < 2: continue
    if not ok: print("-- NOT ACCEPTED point, informational only (first two seeds listed):", key)
    a, b = good[0][2], good[1][2]
    for d in ["axis", "face", "body"]:
        for m in [1, 2]:
            for ch in ["TT1", "TT2", "V1", "V2", "S1"]:
                if (d, m, ch) not in a: continue
                ra, rb = a[(d, m, ch)], b[(d, m, ch)]
                S = (ra[4] + rb[4])/2; f = (ra[6] + rb[6])/2; eS = np.hypot(ra[5], rb[5])/2; ef = np.hypot(ra[7], rb[7])/2
                w = f/S; ew = w*np.hypot(eS/S, ef/f)
                print("%-3d %-4.1f %-4s %-2d %-4s %8.4f %9.5f %9.5f %7.4f(%.4f)" % (key[0], key[1], d, m, ch, ra[3], S, f, w, ew))
