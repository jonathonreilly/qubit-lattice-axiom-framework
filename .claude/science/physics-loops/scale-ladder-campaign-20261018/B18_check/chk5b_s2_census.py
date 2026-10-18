#!/usr/bin/env python3
"""B18 check 5b: clean node census of S2.H20.S2.L202 at both 2-fold k* quasi-energies (E = 0 and E = pi),
in ONE fundamental cell of its period lattice Lambda = <pi e_x, pi e_y, (pi/2)(1,1,1)> (1/16 of the BZ).
Chirality = sign det B (first-order PT on the near-degenerate pair at the refined node) and an own Fukui flux."""
import time, sys
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
exec(open('chk5_s2_b1.py').read().split("# ---------------- (A) S^2 family")[0])
from scipy.optimize import minimize
def fukui(Wd, k0, E, r=2e-3, n=16):
    th = np.linspace(0, np.pi, n + 1); phs = np.linspace(0, 2 * np.pi, 2 * n, endpoint=False); U = []
    for t in th:
        row = []
        for p in phs:
            e, V = np.linalg.eig(Wd(k0 + r * np.array([np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t)]))[0])
            a = wrap(np.angle(e) - E); a = np.where(a < 0, a, -9); i = int(np.argmax(a)); row.append(V[:, i] / np.linalg.norm(V[:, i]))
        U.append(row)
    tot = 0
    for i in range(n):
        for j in range(2 * n):
            a, b, c, d = U[i][j], U[i + 1][j], U[i + 1][(j + 1) % (2 * n)], U[i][(j + 1) % (2 * n)]
            tot += np.angle(np.vdot(a, b) * np.vdot(b, c) * np.vdot(c, d) * np.vdot(d, a))
    return tot / (2 * np.pi)
A_, B_ = (ARGS[0], ARGS[1]) if len(ARGS) >= 2 else ("H20", "L202")
WA = word(fS2, const(onsite(A_)), fS2, const(onsite(B_)))
print(f"word S2.{A_}.S2.{B_}")
Abas = np.array([[np.pi, 0, 0], [0, np.pi, 0], [np.pi / 2, np.pi / 2, np.pi / 2]]).T   # columns a1, a2, a3
Ainv = np.linalg.inv(Abas)
def frac(k): return np.mod(Ainv @ k, 1.0)
def tdist(u, v): d = np.mod(u - v + 0.5, 1.0) - 0.5; return np.linalg.norm(d)
def classify(k):
    u = frac(k)
    pts = {"O-fixed (k*-type)": [np.zeros(3)]}
    for nm, k0 in [("X (pi/2)e_x", np.pi / 2 * np.eye(3)[0]), ("X (pi/2)e_y", np.pi / 2 * np.eye(3)[1]), ("X (pi/2)e_z", np.pi / 2 * np.eye(3)[2])]:
        pts[nm] = [frac(k0)]
    for nm, p in pts.items():
        if any(tdist(u, q) < 1e-6 for q in p): return nm
    m = np.round(k / (np.pi / 4)).astype(int)
    if np.allclose(k, m * np.pi / 4, atol=1e-6): return "(pi/4)Z^3 point, parities " + "".join(str(abs(x) % 2) for x in sorted(np.abs(m) % 2))
    return "generic"
n = 20; g = (np.arange(n) + 0.5) / n
EL = [float(x) for x in ARGS[2:]] or [0.0, np.pi]
for E in EL:
    t0 = time.time()
    lv = [m for e, m, Q in levels_at(WA, kst) if abs(wrap(e - E)) < 1e-7]
    def gap(k): return np.min(np.abs(wrap(np.angle(np.linalg.eigvals(WA(k)[0])) - E)))
    cand = sorted(((gap(Abas @ np.array(t)), Abas @ np.array(t)) for t in itertools.product(g, repeat=3)), key=lambda x: x[0])
    nodes = []
    for v, k in cand[:350]:
        r = minimize(gap, k, method='Nelder-Mead', options=dict(xatol=1e-12, fatol=1e-15, maxiter=4000))
        if r.fun < 1e-9 and not any(tdist(frac(r.x), frac(q)) < 1e-5 for q in nodes): nodes.append(r.x)
    tot = 0; totf = 0; byc = {}
    for k in nodes:
        Wk, d = WA(k); e, V = np.linalg.eig(Wk); idx = np.argsort(np.abs(wrap(np.angle(e) - E)))[:2]
        deg = int(np.sum(np.abs(wrap(np.angle(e) - E)) < 1e-6))
        Q, _ = np.linalg.qr(V[:, idx]); a, B = pt(WA, k, Q); sv = np.linalg.svd(B, compute_uv=False); ch = int(np.sign(np.linalg.det(B)))
        fk = fukui(WA, k, E); tot += ch; totf += fk
        c = classify(k); byc.setdefault((c, tuple(np.round(sv, 4)), ch, round(fk)), []).append(deg)
    print(f"E = {E:+.6f}: k* level multiplicity {lv}; {len(nodes)} distinct E-touchings per Lambda-cell [{time.time()-t0:.0f}s]")
    for key, ds in sorted(byc.items()): print(f"   {key[0]:32s} speeds {key[1]}  sign det B {key[2]:+d}  Fukui {key[3]:+d}  count {len(ds)}  (multiplicity at E: {sorted(set(ds))})")
    print(f"   net chirality per cell: sign det {tot:+d}, Fukui {totf:+.3f}")
    check(f"census at E = {E:+.4f}: net chirality per Lambda-cell is zero (consistent with 3-winding 0)", tot == 0 and abs(totf) < 0.1)
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
