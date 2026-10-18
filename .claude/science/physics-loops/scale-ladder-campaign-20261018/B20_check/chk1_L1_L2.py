#!/usr/bin/env python3
"""B20 check 1: lemmas L1 and L2, by routes different from B20's runner.
 - little group of k* derived from the PSG operators themselves (Bloch reps), commutant / isotypic decomposition
 - on-site symmetric algebra solved from real-space invariance (not just functions of H_on, Lambda)
 - speeds by finite differences of eigenphases in 29 directions; chirality by own lattice Berry flux
 - L2 bookkeeping, including the cases L2's statement leaves implicit (4-fold D+ + D- levels, G3/2 levels at E)."""
import time
from chklib import *
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
rng = np.random.default_rng(2026)
# --- on-site algebra
U0 = rand_onsite_unitary(rng)
check("on-site symmetric algebra: dim 6, non-commutative, contains H_on and Lambda; a random unitary in it is symmetric on the full lattice",
      len(ONSITE_BASIS) == 6 and onsite_check(U0) and max(np.abs(a @ b - b @ a).max() for a in ONSITE_BASIS for b in ONSITE_BASIS) > 1e-3)
# --- little group of +-k*
def little(k0):
    gens = [op_bloch(P, s, k0) for P, s in rots + trans]
    assert all(kred(kk) == kred(k0) for kk, _ in gens)
    G = [np.eye(12, dtype=complex)]
    def known(M): return any(np.allclose(M, g) for g in G)
    for _, g in gens:
        if not known(g): G.append(g)
    ch = True
    while ch:
        ch = False
        for a in list(G):
            for _, b in gens:
                c = a @ b
                if not known(c): G.append(c); ch = True
    return G
LG = {}
for lab, k0 in (("k*", kst), ("-k*", -kst)):
    G = little(k0); LG[lab] = G
    A = np.array([np.kron(g, np.eye(12)) - np.kron(np.eye(12), g.T) for g in G]).reshape(-1, 144)
    _, sv, Vh = np.linalg.svd(A); comm = [v.reshape(12, 12) for v in Vh[np.sum(sv > 1e-8):]]
    # centre of the commutant -> isotypic projectors
    Z = np.array([np.kron(c, np.eye(12)) - np.kron(np.eye(12), c.T) for c in comm]).reshape(-1, 144)
    _, sz, Vz = np.linalg.svd(np.vstack([A, Z])); cen = [v.reshape(12, 12) for v in Vz[np.sum(sz > 1e-8):]]
    X = sum(rng.normal() * (c + c.conj().T) + rng.normal() * 1j * (c - c.conj().T) for c in cen); w, V = np.linalg.eigh(X)
    ranks = sorted(collections_count := [int(np.sum(np.abs(w - x) < 1e-6)) for x in sorted(set(np.round(w, 6)))])
    letters_ok = all(np.allclose(g @ L, L @ g) for g in G for L in (Sk(k0), Sk(k0, 2), RLk(k0), U0, Hon0, Lam))
    check(f"{lab}: all 24 rotations and all translations fix {lab} (mod 2pi); little group (Bloch reps) of order {len(G)}; commutant dim {len(comm)}, "
          f"centre dim {len(cen)}, isotypic ranks {ranks} (E1/2, E5/2 once each, G3/2 twice); S, S^2, R_L, on-site letters commute with it",
          len(comm) == 6 and len(cen) == 3 and ranks == [2, 2, 8] and letters_ok)
# isotypic doublets as joint eigenspaces (H_on = 2, Lambda = -+2sqrt2)
def eigsp(M, lam):
    w, V = np.linalg.eigh(M); return V[:, np.abs(w - lam) < 1e-6]
def inter(A_, B_):
    P = A_ @ A_.conj().T; Q = B_ @ B_.conj().T; w, V = np.linalg.eigh(P @ Q @ P); return V[:, w > 1 - 1e-8]
Dp = inter(eigsp(Hon0, 2.0), eigsp(Lam, -2 * np.sqrt(2))); Dm = inter(eigsp(Hon0, 2.0), eigsp(Lam, 2 * np.sqrt(2)))
sx = np.array([[0, 1], [1, 0]]); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1])
def fM(D):
    h = [D.conj().T @ np.diag(np.array([FACE[c][j] for c in CORN], float)) @ D for j in range(3)]
    return np.array([[np.trace(x @ s_).real / 2 for s_ in (sx, sy, sz)] for x in h]), np.array([np.trace(x).real / 2 for x in h])
Mp, ap = fM(Dp); Mm, am = fM(Dm)
inv_ok = all(np.allclose(g @ D, D @ (D.conj().T @ g @ D)) for G in LG.values() for g in G for D in (Dp, Dm))
check("D+ = {H_on=2} n {Lambda=-2sqrt2}, D- = {H_on=2} n {Lambda=+2sqrt2} are 2-dim, invariant under both little groups; <f>_D isotropic sqrt2/3, untilted, det signs (+,-)",
      Dp.shape[1] == 2 and Dm.shape[1] == 2 and inv_ok and np.allclose(np.linalg.svd(Mp, compute_uv=False), np.sqrt(2) / 3)
      and np.allclose(np.linalg.svd(Mm, compute_uv=False), np.sqrt(2) / 3) and np.abs(ap).max() < 1e-12 and np.abs(am).max() < 1e-12
      and np.sign(np.linalg.det(Mp)) == 1 and np.sign(np.linalg.det(Mm)) == -1)
# the vector-operator selection rule used below: P_{D+} X P_{D-} = 0 for every k-derivative of every letter at +-k*
def dletter(L, k, j, h=1e-6):
    e = np.eye(3)[j]; return (letter(L, k + h * e) - letter(L, k - h * e)) / (2 * h)
sel = max(np.abs(Dp.conj().T @ dletter(L, k0, j) @ Dm).max() for L in ('S', 'R', 'S2') for k0 in (kst, -kst) for j in range(3))
check("selection rule: <D+| d_j F |D-> = 0 at +-k* for F = S, S^2, R_L (E1/2 x T1 has no E5/2)", sel < 1e-8, f"max {sel:.1e}")
# --- L1 by finite differences with general on-site letters
kl = ['S', 'Si', 'S2', 'S2i', 'R']
def Honly():
    return sum(np.exp(1j * rng.uniform(0, 2 * np.pi)) * P for P in PH)
def rword(n):
    tuned = rng.random() < 0.3      # tuned words: on-site letters that are functions of H_on only (equal scalars on D+, D-)
    w = []
    for _ in range(n): w += [kl[rng.integers(5)], Honly() if tuned else rand_onsite_unitary(rng)]
    return w
nd = 0; worst = 0; chi_ok = True; nflux = 0; four = []; g32 = 0
for t in range(160):
    w = rword(int(rng.integers(1, 5))); ns = nS(w)
    for lab, k0 in (("k*", kst), ("-k*", -kst)):
        W0 = Wword(w, k0)
        for E, m in levels(W0):
            if m == 4:
                # D+ + D- 4-fold (Dirac) or a G3/2 level?
                e, V = np.linalg.eig(W0); Vd = V[:, np.abs(wrap(np.angle(e) - E)) < 1e-6]; Q, _ = np.linalg.qr(Vd)
                ov = np.linalg.norm(Q.conj().T @ np.hstack([Dp, Dm])) ** 2
                if abs(ov - 4) < 1e-6 and ns != 0: four.append((w, k0, E, ns))
                elif abs(ov) < 1e-6: g32 += 1
                continue
            if m != 2: continue
            dirs, sp = fd_speeds(w, k0, E, h=1e-7, rng=rng)
            pred = abs(ns) * np.sqrt(2) / 3
            for d, (a, b) in zip(dirs, sp):
                # dispersion E +- v|q| with no tilt: a = (-vh, +vh)
                worst = max(worst, abs((a[1] - a[0]) / 2e-7 - pred), abs((b[1] - b[0]) / 2e-7 - pred), abs((a.sum() / 2) / 1e-7))
            nd += 1
            if ns != 0 and nflux < 40:
                e, V = np.linalg.eig(W0); Vd = V[:, np.abs(wrap(np.angle(e) - E)) < 1e-6]; Q, _ = np.linalg.qr(Vd)
                eps = 1 if np.linalg.norm(Dp.conj().T @ Q) ** 2 > 1.5 else -1
                fl = berry_flux(w, k0, E, r=2e-3, n=14)
                # convention: lower-band Berry flux = -sign(det M) (fixed by the control below)
                chi_ok &= (round(fl) == -int(np.sign(ns)) * eps); nflux += 1
check("L1 (finite differences, 29 directions, general non-commuting on-site letters): every exactly 2-fold +-k* level has dispersion E +- |n_S| (sqrt2/3)|q|, untilted",
      nd > 60 and worst < 1e-4, f"{nd} doublets, worst deviation {worst:.1e} (FD step 1e-7; first run with 1e-5 failed by O(h) curvature near close neighbour levels)")
# convention control for the flux sign: a single isotropic Weyl h = +sigma.q (det M = +1)
def weyl_flux(sgn):
    th = np.linspace(0, np.pi, 15); ph = np.linspace(0, 2 * np.pi, 28, endpoint=False); U = np.zeros((15, 28, 2), complex)
    for i, t in enumerate(th):
        for j, p in enumerate(ph):
            q = np.array([np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t)]); h = sgn * q[0] * sx + q[1] * sy + q[2] * sz
            w_, v_ = np.linalg.eigh(h); U[i, j] = v_[:, 0]
    tot = 0
    for i in range(14):
        for j in range(28):
            a, b, c, d = U[i, j], U[i + 1, j], U[i + 1, (j + 1) % 28], U[i, (j + 1) % 28]; tot += np.angle(np.vdot(a, b) * np.vdot(b, c) * np.vdot(c, d) * np.vdot(d, a))
    return tot / (2 * np.pi)
check("flux convention control: lower band of +sigma.q has flux -1 (so flux = -sign det M), of a det<0 cone +1",
      round(weyl_flux(1)) == -1 and round(weyl_flux(-1)) == 1)
check("L1 chirality: own lattice Berry flux of every tested doublet = -sign(n_S) eps_D, i.e. det-M chirality sign(n_S) eps_D", chi_ok and nflux >= 30, f"{nflux} fluxes")
# --- 4-fold D+ + D- levels: isotropic Dirac points (outside L1's 'exactly 2-fold' and outside the B20 screen)
okd = True; nd4 = 0
for w, k0, E, ns in four[:20]:
    dirs, sp = fd_speeds(w, k0, E, m=4, h=1e-7, rng=rng); pred = abs(ns) * np.sqrt(2) / 3
    for d, (a, b) in zip(dirs, sp):
        okd &= np.allclose(np.sort(a) / 1e-7, [-pred, -pred, pred, pred], atol=1e-4)
    nd4 += 1
check("4-fold D+ + D- levels at +-k* (n_S != 0): two isotropic, untilted cones of the SAME speed |n_S| sqrt2/3 (opposite chirality) - an isotropic Dirac point, not covered by L1/L2 or the screen",
      nd4 >= 5 and okd, f"{nd4} such levels tested ({len(four)} found in 160 words; {g32} G3/2 4-fold levels seen)")
# --- L2 bookkeeping incl. G3/2 at E
def scal(L, D): return np.trace(D.conj().T @ L @ D) / 2
cnt = {}; okb = True; gfl = 0
for t in range(300):
    w = rword(int(rng.integers(1, 5))); ns = nS(w); nr = nR(w)
    if ns == 0: continue
    lp = np.prod([scal(L, Dp) for L in w if not isinstance(L, str)]); lm = np.prod([scal(L, Dm) for L in w if not isinstance(L, str)])
    pred = {("k*", 1): lp * (-1) ** nr, ("k*", -1): lm, ("-k*", 1): lp, ("-k*", -1): lm * (-1) ** nr}
    for (lab, eps), val in pred.items():
        k0 = kst if lab == "k*" else -kst; D = Dp if eps == 1 else Dm
        okb &= np.allclose(Wword(w, k0) @ D, val * D, atol=1e-9)
    E = np.angle(pred[("k*", 1)])
    if abs(pred[("k*", 1)] - pred[("k*", -1)]) < 1e-9: continue
    net = sum(int(np.sign(ns)) * eps for (lab, eps), v in pred.items() if abs(v - np.exp(1j * E)) < 1e-9)
    # does a G3/2 level of +-k* also sit at E?
    gat = any(m == 4 and abs(wrap(e - E)) < 1e-7 for k0 in (kst, -kst) for e, m in levels(Wword(w, k0)))
    gfl += gat
    key = (nr % 2, bool(abs(lp - lm) < 1e-9), net); cnt[key] = cnt.get(key, 0) + 1
check("L2: W(+-k*) acts on D+,D- as (lp(-1)^nR, lm) at k* and (lp, lm(-1)^nR) at -k*, with general on-site letters", okb)
check("L2: doublet net chirality at E (k* D+ level exactly 2-fold) is 0 iff nR odd and lp = lm, else +-1 or +-2",
      all((k_[2] == 0) == (k_[0] == 1 and k_[1]) for k_ in cnt) and any(k_[2] == 0 for k_ in cnt), f"{cnt}; G3/2 4-fold level also at E in {gfl} words")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
