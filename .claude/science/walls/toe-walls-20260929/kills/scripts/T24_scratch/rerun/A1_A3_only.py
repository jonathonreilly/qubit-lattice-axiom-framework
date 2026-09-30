"""Kill-side rerun of the attacker's A1/A3 blocks only (verbatim logic from A_pin.run), skipping the slow A2 census."""
import itertools
import numpy as np
import A_pin as A
out = []
print("A1")
for gname in ["O", "D4", "D2", "C4z", "C2z", "trivial_group"]:
    grp = A.rot(gname)
    for r in [1, 2, 3]:
        mx_all = []; frac = 0
        for s in range(200):
            const, C = A.random_coeffs(r)
            cav, tab = A.average(const, C, grp, "full")
            d, _ = A.corner_d(cav, tab)
            mx_all.append(np.abs(d).max())
            if np.abs(d).max() > 1e-6: frac += 1
        print(f"  G={gname:13s} |G|={len(grp):2d} range {r}: max={max(mx_all):.2e} median={np.median(mx_all):.2e} unpinned frac={frac/200:.2f}", flush=True)
mx = []
for s in range(200):
    const, C = A.random_coeffs(2)
    cav, tab = A.average(const, C, A.rot("O"), "trivial")
    d, _ = A.corner_d(cav, tab); mx.append(np.abs(d).max())
print(f"  O trivial coin range 2: median max|d| = {np.median(mx):.2e}")
mxk = []
for s in range(200):
    const, C = A.random_coeffs(3)
    tab = {}
    for w, (cc, ss) in C.items():
        c2 = np.zeros(4); s2 = np.zeros(4); c2[0] = cc[0]; s2[1:] = ss[1:]
        tab[w] = [c2, s2]
    c0 = np.zeros(4); c0[0] = const[0]
    d, _ = A.corner_d(c0, tab); mxk.append(np.abs(d).max())
print(f"A3 Kramers-only range 3: max|d(TRIM)| = {max(mxk):.2e}")
