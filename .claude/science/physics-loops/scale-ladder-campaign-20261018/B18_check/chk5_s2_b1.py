#!/usr/bin/env python3
"""B18 check 5: spot checks of (A) the S^2-word family and (B) the B1 doubler table.
Own route: exact degenerate perturbation theory (analytic derivatives) at symmetry points; own node
search with Newton-free refinement (Nelder-Mead on min |eigphase - E|), chirality from sign det B at the
refined node (first-order PT on the near-degenerate pair) and an own Fukui-link Berry flux."""
import time
from chk_model import *
from scipy.optimize import minimize
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
def dHk(bl, k, j):
    H = np.zeros((12, 12), complex)
    for sh, M in bl.items(): H += 1j * sh[j] * M * np.exp(1j * np.dot(k, sh))
    return H
PAU = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]])]
# factors as (value, derivative) closures
def fS(k): return SKc(k), [dHk(blS, k, j) for j in range(3)]
def fS2(k):
    s, d = fS(k); return s @ s, [dj @ s + s @ dj for dj in d]
def fRL(k): return RLk(k), [dHk(blL, k, j) for j in range(3)]
def const(U): return lambda k: (U, [np.zeros((12, 12))] * 3)
def word(*fs):
    def Wd(k):
        val = np.eye(12, dtype=complex); der = [np.zeros((12, 12), complex) for _ in range(3)]
        for f in fs:
            v, d = f(k); der = [der[j] @ v + val @ d[j] for j in range(3)]; val = val @ v
        return val, der
    return Wd
def levels_at(Wd, k, tol=1e-8):
    Wk = Wd(k)[0]; e, V = np.linalg.eig(Wk); ph = np.angle(e); out = []; used = np.zeros(12, bool)
    for i in np.argsort(ph):
        if used[i]: continue
        grp = [j for j in range(12) if not used[j] and abs(wrap(ph[j] - ph[i])) < tol]; used[grp] = True
        Q, _ = np.linalg.qr(V[:, grp]); out.append((ph[i], len(grp), Q))
    return out
def pt(Wd, k, Q):
    Wk, d = Wd(k); A = [-1j * Q.conj().T @ Wk.conj().T @ d[j] @ Q for j in range(3)]
    if Q.shape[1] != 2: return None
    a = np.array([np.trace(x).real / 2 for x in A]); B = np.array([[np.trace(A[j] @ PAU[b]).real / 2 for b in range(3)] for j in range(3)])
    return a, B
def weyl_at(Wd, k, E):
    for e, m, Q in levels_at(Wd, k):
        if m == 2 and abs(wrap(e - E)) < 1e-7:
            a, B = pt(Wd, k, Q); return np.linalg.svd(B, compute_uv=False), np.linalg.det(B), np.linalg.norm(a)
    return None
UHd = {f"H{a}{b}": UHc(a, b) for a, b in itertools.product(range(4), repeat=2)}
ULd = {f"L{a}{b}{c}": ULc(a, b, c) for a, b, c in itertools.product(range(4), repeat=3)}
ON = {**UHd, **ULd}
def onsite(lbl): # "L020*H02" = UL(020) @ UH(02)
    M = np.eye(12, dtype=complex)
    for p in lbl.split("*"): M = M @ ON[p]
    return M
v1 = np.sqrt(2) / 3
# ---------------- (A) S^2 family
WA = word(fS2, const(onsite("H20")), fS2, const(onsite("L202")))
ks2 = np.random.default_rng(1).uniform(-np.pi, np.pi, (3, 3))
per = all(np.allclose(WA(k)[0], WA(k + sh)[0]) for k in ks2 for sh in [np.pi * e for e in np.eye(3)] + [np.pi / 2 * np.ones(3)])
check("(A) S2.H20.S2.L202 is periodic under pi e_i and (pi/2)(1,1,1); S(k)^2 = diag(e^{2ik.f_c}) carries no gauge sign",
      per and np.allclose(fS2(ks2[0])[0], np.diag(np.exp(2j * np.array([np.dot(ks2[0], FACE[c]) for c in CORN])))) )
lv = levels_at(WA, kst); E2 = [e for e, m, Q in lv if m == 2]
print("S2.H20.S2.L202 levels at k*:", [(round(e, 5), m) for e, m, Q in lv])
EA = E2[0]
w_ks = weyl_at(WA, kst, EA); w_X = weyl_at(WA, np.pi / 2 * np.eye(3)[0], EA); w_0 = weyl_at(WA, np.zeros(3), EA)
print("k* :", w_ks, "\nX  :", w_X, "\n0  :", w_0)
check("(A) k* node of S2.H20.S2.L202 is isotropic at 4 sqrt2/3 (= sqrt2/3 per S application), and k = 0 is an identical copy",
      w_ks is not None and np.allclose(w_ks[0], 4 * v1, atol=1e-8) and w_0 is not None and np.allclose(w_0[0], 4 * v1, atol=1e-8),
      f"E = {EA:.6f}")
check("(A) the X-type point (pi/2)e_x carries a 2-fold level at the same E, isotropic at the same speed (B18: 'unexplained')",
      w_X is not None and np.allclose(w_X[0], 4 * v1, atol=1e-8), f"chirality signs k*: {np.sign(w_ks[1]):+.0f}, X: {np.sign(w_X[1]):+.0f}")
# own node search for S2.H20.S2.L202 at EA in one fundamental cell of the period lattice: cell = [0,pi)^3 halved by (pi/2)(1,1,1)
def gap(k, Wd=WA, E=EA): return np.min(np.abs(wrap(np.angle(np.linalg.eigvals(Wd(k)[0])) - E)))
n = 24; g = (np.arange(n) + 0.5) * np.pi / n
cand = []
for t in itertools.product(range(n), repeat=3):
    k = np.array([g[t[0]], g[t[1]], g[t[2]]]); cand.append((gap(k), k))
cand.sort(key=lambda x: x[0]); seeds = [k for v, k in cand[:400]]
nodes = []
for k in seeds:
    r = minimize(lambda x: gap(x), k, method='Nelder-Mead', options=dict(xatol=1e-12, fatol=1e-15, maxiter=4000))
    if r.fun < 1e-9:
        kk = np.mod(r.x, np.pi)   # reduce mod pi Z^3
        # reduce further by (pi/2)(1,1,1): canonical rep
        alt = np.mod(kk + np.pi / 2, np.pi)
        kk = min([kk, alt], key=lambda v: tuple(np.round(v, 6)))
        if not any(np.linalg.norm(wrap(2 * (kk - q))) < 1e-5 for q in nodes): nodes.append(kk)
print(f"(A) distinct E-touchings in one cell (mod pi Z^3 and (pi/2)(1,1,1)): {len(nodes)}")
def chir(Wd, k, E):
    Wk, d = Wd(k); e, V = np.linalg.eig(Wk); idx = np.argsort(np.abs(wrap(np.angle(e) - E)))[:2]
    Q, _ = np.linalg.qr(V[:, idx]); a, B = pt(Wd, k, Q); return np.linalg.svd(B, compute_uv=False), np.linalg.det(B)
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
tot_ch = 0; tot_fk = 0; rows = []
for kk in nodes:
    sv, dt = chir(WA, kk, EA); fk = fukui(WA, kk, EA)
    rows.append((np.round(kk / np.pi, 4), np.round(sv, 4), int(np.sign(dt)), round(fk, 3))); tot_ch += np.sign(dt); tot_fk += fk
for r_ in rows: print("   node k/pi", r_[0], "speeds", r_[1], "sign det B", r_[2], "Fukui flux (band just below E)", r_[3])
print(f"   net chirality per cell: sign-det sum {tot_ch:+.0f}, Fukui sum {tot_fk:+.3f}")
check("(A) own node census at E for S2.H20.S2.L202: the chiralities of all E-touchings in one cell sum to zero (3-winding of a product of "
      "a diagonal shift and constant unitaries is 0), so the B18 census line 'every sampled node class has Berry flux +1' is incomplete or mis-signed",
      abs(tot_ch) < 0.5 and abs(tot_fk) < 0.1, f"{len(nodes)} touchings; sign-det sum {tot_ch:+.0f}; Fukui sum {tot_fk:+.3f}")
# the (pi/4)(1,1,0) classes anisotropic?
anis = [r_ for r_ in rows if np.ptp(r_[1]) > 0.1]
check("(A) the census has anisotropic nodes (B18: (pi/4)(1,1,0)-type, speeds ~1.58-2.47), so not every species shares one cone",
      len(anis) > 0, f"{len(anis)} anisotropic node classes; speed ranges {[tuple(r_[1]) for r_ in anis][:4]}")
# (A') S2.L202.S2.L020 exact crossing at (pi/2)(-1,-1,0)
WA2 = word(fS2, const(onsite("L202")), fS2, const(onsite("L020")))
lv2 = levels_at(WA2, kst); E2b = [e for e, m, Q in lv2 if m == 2]
cross = [min(gap(np.array(p) * np.pi / 2, WA2, E)) if False else gap(np.array(p) * np.pi / 2, WA2, E) for E in E2b for p in [(-1, -1, 0)]]
print("S2.L202.S2.L020 2-fold levels at k*:", np.round(E2b, 6), "distance to E at (pi/2)(-1,-1,0):", np.round(cross, 14))
check("(A) S2.L202.S2.L020 reaches its k* node quasi-energy exactly at (pi/2)(-1,-1,0) (an X-type point): not clean",
      min(cross) < 1e-10, f"{min(cross):.1e}")
# ---------------- (B) B1 doubler table
WB = word(fS, fRL, const(onsite("L020*H02")))
lvB = levels_at(WB, kst); print("S.RL.L020*H02 levels at k*:", [(round(e, 5), m) for e, m, Q in lvB])
EB = [e for e, m, Q in lvB if m == 2 and abs(abs(e) - np.pi) < 1e-6]
res = []
for E in EB:
    res.append((E, weyl_at(WB, kst, E), weyl_at(WB, kst + np.pi * np.eye(3)[0], E), weyl_at(WB, -kst + np.pi * np.eye(3)[0], E)))
for r_ in res: print("   E", round(r_[0], 5), "k*", r_[1], "\n      D+x", r_[2], "\n      D-x", r_[3])
okB = any(r_[1] is not None and np.allclose(r_[1][0], v1, atol=1e-9) and r_[2] is not None and
          np.allclose(sorted(r_[2][0]), sorted([2 * np.sqrt(2) / 5, 3 * np.sqrt(2) / 10, 3 * np.sqrt(2) / 10]), atol=1e-9) for r_ in res)
check("(B) S.RL.L020*H02 at E = pi: k* isotropic sqrt2/3; doubler at k*+pi e_x uniaxial (2sqrt2/5 axial, 3sqrt2/10 transverse) exactly (PT)", okB)
sc = [max(abs(r_[2][0].max() - r_[2][0].min()), abs(r_[2][0] - v1).max()) for r_ in res if r_[2] is not None]
print("   score max(|va-vt|, |v-v*|):", np.round(sc, 6), " vs B18 0.1414 (= 2sqrt2/5 - 3sqrt2/10 =", round(2*np.sqrt(2)/5-3*np.sqrt(2)/10, 6), ")")
WC = word(fS, const(onsite("L131*H33")))
lvC = levels_at(WC, kst); EC = [e for e, m, Q in lvC if m == 2 and abs(e) < 1e-6]
rc = [(weyl_at(WC, kst, E), weyl_at(WC, kst + np.pi * np.eye(3)[0], E)) for E in EC]
print("S.L131*H33 levels at k*:", [(round(e, 5), m) for e, m, Q in lvC], rc)
okC = any(a is not None and b is not None and np.allclose(a[0], v1, atol=1e-9) and np.allclose(b[0], np.sqrt(2) / 5, atol=1e-9) for a, b in rc)
check("(B) S.L131*H33 at E = 0: the doubler at k*+pi e_x is isotropic at sqrt2/5 = (3/5) v* exactly at linear order (PT)", okC)
# is it clean? distance to E away from cube points on a coarse grid
grid = [np.array(t) * 2 * np.pi / 12 - np.pi + 0.07 for t in itertools.product(range(12), repeat=3)]
far = [q for q in grid if min(np.linalg.norm(wrap(q - c)) for c in CUBE) > 0.4]
dmin = min(gap(q, WC, EC[0]) for q in far) if EC else None
print("   S.L131*H33: min distance to E on a 12^3 grid away from the cube points:", dmin)
check("(B) S.L131*H33 is not clean at E (bands reach within 0.05 of E away from the cube points on a coarse grid)", dmin is not None and dmin < 0.05, f"{dmin:.3e}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time()-t0:.0f}s]")
