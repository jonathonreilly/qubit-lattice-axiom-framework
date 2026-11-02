#!/usr/bin/env python3
"""f1: tree level of the soft step (S4' root map), linearised at the trivial background.
Criteria: checks/f1_criteria.md (written before this script)."""
import itertools, sys, time
import numpy as np

t0 = time.time()
OUT = []
def say(*a):
    s = " ".join(str(x) for x in a); OUT.append(s); print(s)

def root_map_coeffs(L):
    """c[mu] : dict (w tuple, nu) -> coefficient, w relative to the block root o."""
    o = (L - 1) // 2
    perms = list(itertools.permutations(range(4)))
    coeffs = []
    for mu in range(4):
        c = {}
        def add(z, nu, s):
            key = (tuple(int(v - o) for v in z), nu)
            c[key] = c.get(key, 0.0) + s
        for sig in perms:
            for y in itertools.product(range(L), repeat=4):
                # path o -> y in axis order sig
                path = []
                z = [o] * 4
                for ax in sig:
                    while z[ax] < y[ax]:
                        path.append((tuple(z), ax, +1)); z[ax] += 1
                    while z[ax] > y[ax]:
                        z[ax] -= 1; path.append((tuple(z), ax, -1))
                w = 1.0 / (len(perms) * L ** 4)
                for (zz, ax, s) in path:
                    add(zz, ax, s * w)                      # P^sigma(c_X -> y)
                    zs = list(zz); zs[mu] += L
                    add(zs, ax, -s * w)                     # reversed translate
                for j in range(L):
                    zz = list(y); zz[mu] += j
                    add(zz, mu, w)                          # straight leg
        coeffs.append(c)
    # pack into arrays, grouped by (mu, nu)
    packs = []
    for mu in range(4):
        row = []
        for nu in range(4):
            keys = [k for k in coeffs[mu] if k[1] == nu]
            W = np.array([k[0] for k in keys], dtype=float).reshape(-1, 4)
            CV = np.array([coeffs[mu][k] for k in keys])
            row.append((W, CV))
        packs.append(row)
    return packs

def Qhat(packs, q):
    """4x4 matrix Q[mu, nu](q) = sum_w c e^{i q.w}."""
    Q = np.zeros((4, 4), complex)
    for mu in range(4):
        for nu in range(4):
            W, CV = packs[mu][nu]
            if len(CV): Q[mu, nu] = np.exp(1j * (W @ q)) @ CV
    return Q

def shat(q): return np.exp(1j * np.asarray(q)) - 1.0

def Dhat(q):
    s = shat(q); return (np.vdot(s, s).real) * np.eye(4) - np.outer(s, s.conj())

def aliases(L):
    return [np.array(K, float) for K in itertools.product(range(L), repeat=4)]

def Qt_list(packs, L, p):
    o = (L - 1) / 2.0
    res = []
    for K in ALIAS[L]:
        q = (p + 2 * np.pi * K) / L
        res.append((q, np.exp(1j * o * q.sum()) * Qhat(packs, q)))
    return res

def transverse_basis(sc):
    n = sc / np.linalg.norm(sc)
    M = np.eye(4, dtype=complex) - np.outer(n, n.conj())
    w, v = np.linalg.eigh(M)
    return v[:, w > 0.5]          # 4x3 orthonormal, perpendicular to sc

def T_transverse(packs, L, p, kappa, QL=None):
    sc = shat(p)
    E = transverse_basis(sc)
    QL = QL if QL is not None else Qt_list(packs, L, p)
    S = np.zeros((4, 4), complex)
    for q, Qt in QL:
        s = shat(q); s2 = np.vdot(s, s).real
        PT = np.eye(4) - np.outer(s, s.conj()) / s2
        S += Qt @ PT @ Qt.conj().T / s2
    S /= L ** 4
    inv_k = 0.0 if np.isinf(kappa) else 1.0 / kappa
    A3 = E.conj().T @ (inv_k * np.eye(4) + S) @ E
    T3 = np.linalg.inv(A3)
    return E @ T3 @ E.conj().T, E, T3, QL

def T_direct(packs, L, p, kappa, QL=None):
    QL = QL if QL is not None else Qt_list(packs, L, p)
    nK = len(QL)
    Qt = np.hstack([Qt_ for _, Qt_ in QL])               # 4 x 4nK
    H = np.zeros((4 * nK, 4 * nK), complex)
    for i, (q, _) in enumerate(QL):
        H[4 * i:4 * i + 4, 4 * i:4 * i + 4] = L ** 4 * Dhat(q)
    H += kappa * Qt.conj().T @ Qt
    w, v = np.linalg.eigh(H)
    keep = w > 1e-10 * w.max()
    Hp = (v[:, keep] / w[keep]) @ v[:, keep].conj().T
    return kappa * np.eye(4) - kappa ** 2 * Qt @ Hp @ Qt.conj().T

ALIAS = {3: aliases(3), 5: aliases(5)}
rng = np.random.default_rng(20261027)
fails = []
def crit(name, ok, detail):
    say(f"[{name}] {'PASS' if ok else 'FAIL'} :: {detail}")
    if not ok: fails.append(name)

L = 3
packs = root_map_coeffs(L)
say(f"f1 start; L=3 root map built ({sum(len(c) for row in packs for (W, c) in row)} coefficients) t={time.time()-t0:.1f}s")

# (G) root covariance and normalisation
errG = 0.0
for _ in range(20):
    q = rng.uniform(-np.pi, np.pi, 4)
    errG = max(errG, np.abs(Qhat(packs, q) @ shat(q) - shat(L * q)).max())
errN = np.abs(Qhat(packs, np.zeros(4)) - L * np.eye(4)).max()
crit("G", errG <= 1e-12 and errN <= 1e-12, f"max|Q s - s_c(Lq)|={errG:.2e}, |Q(0)-L*1|={errN:.2e}")

kappas = [0.25, 1.0, 4.0, 16.0]
dirs = [np.array([1, 0, 0, 0.]), np.array([1, 1, 0, 0.]) / np.sqrt(2), np.array([1, 2, 3, 4.]) / np.sqrt(30)]
ngen = np.array([0.37, -0.81, 0.52, 0.13]); ngen /= np.linalg.norm(ngen)

# (A), (B)
okA = True; okB = True; worstA = [0, 0, 0]; worstB = 0
for kap in kappas:
    for p in [0.3 * dirs[2], 0.7 * dirs[1], 1.5 * ngen]:
        QL = Qt_list(packs, L, p)
        Td = T_direct(packs, L, p, kap, QL)
        Tt, E, T3, _ = T_transverse(packs, L, p, kap, QL)
        nT = np.linalg.norm(Td); sc = shat(p)
        h = np.linalg.norm(Td - Td.conj().T) / nT
        tr = np.linalg.norm(Td @ sc) / (nT * np.linalg.norm(sc))
        worstA[0] = max(worstA[0], h); worstA[1] = max(worstA[1], tr)
        okA &= (h <= 1e-12) and (tr <= 1e-9)
        b = np.linalg.norm(E.conj().T @ (Td - Tt) @ E) / np.linalg.norm(T3)
        worstB = max(worstB, b); okB &= b <= 1e-8
for _ in range(5):
    perm = rng.permutation(4); p = rng.uniform(-1.2, 1.2, 4); kap = 1.0
    Td = T_direct(packs, L, p, kap)
    # T(pi p)_{pi mu, pi nu} = T(p)_{mu nu}: with (pi p)_{pi(a)} = p_a
    pp = np.empty(4); pp[perm] = p
    Tpp = T_direct(packs, L, pp, kap)
    e = np.abs(Tpp[np.ix_(perm, perm)] - Td).max() / np.linalg.norm(Td)
    worstA[2] = max(worstA[2], e); okA &= e <= 1e-10
crit("A", okA, f"herm={worstA[0]:.1e}, |T s_c|={worstA[1]:.1e}, perm={worstA[2]:.1e}")
crit("B", okB, f"direct vs transverse (relative) max={worstB:.1e}")

# (C) marginal coefficient
def ratios(L_, packs_, t, n, kap):
    p = t * n
    Tt, E, T3, _ = T_transverse(packs_, L_, p, kap)
    sc = shat(p)
    return np.sort(np.linalg.eigvalsh(T3) / np.vdot(sc, sc).real)

okC = True; lines = []
for kap in kappas:
    for n in dirs:
        r1 = ratios(L, packs, 0.01, n, kap); r2 = ratios(L, packs, 0.02, n, kap)
        rich = (4 * r1 - r2) / 3
        ok = np.abs(r1 - 1).max() <= 1e-3 and np.abs(rich - 1).max() <= 1e-5
        okC &= ok
        lines.append(f"k={kap} n={np.round(n,3)}: |r(0.01)-1|={np.abs(r1-1).max():.2e}, |Rich-1|={np.abs(rich-1).max():.2e}")
packs5 = root_map_coeffs(5)
for n in dirs:
    r1 = ratios(5, packs5, 0.01, n, 1.0); r2 = ratios(5, packs5, 0.02, n, 1.0)
    rich = (4 * r1 - r2) / 3
    ok = np.abs(r1 - 1).max() <= 1e-3 and np.abs(rich - 1).max() <= 1e-5
    okC &= ok
    lines.append(f"L=5 k=1 n={np.round(n,3)}: |r(0.01)-1|={np.abs(r1-1).max():.2e}, |Rich-1|={np.abs(rich-1).max():.2e}")
for s in lines: say("   " + s)
crit("C", okC, "marginal coefficient of the coarse tree form = 1 (all kappa, n; and L=5)")

# (D) remainder O(p^4)
okD = True; rs = []
for kap in kappas:
    for n in dirs:
        r = []
        for t in (0.05, 0.1):
            p = t * n; Tt, E, T3, _ = T_transverse(packs, L, p, kap)
            sc = shat(p); Dc = np.vdot(sc, sc).real * (np.eye(4) - np.outer(sc, sc.conj()) / np.vdot(sc, sc).real)
            r.append(np.linalg.norm(Tt - Dc))
        ratio = r[1] / r[0]; rs.append(ratio)
        okD &= (14 <= ratio <= 18) and r[0] >= 1e-12
crit("D", okD, f"r(0.1)/r(0.05) in [{min(rs):.3f}, {max(rs):.3f}]")

# (E) tree background aliases
okE = True; es = []
for kap in kappas:
    for n in dirs:
        cs = []
        for t in (0.01, 0.02):
            p = t * n; QL = Qt_list(packs, L, p)
            Tt, E, T3, _ = T_transverse(packs, L, p, kap, QL)
            b = E[:, 0]
            cmax = 0.0
            for (q, Qt), K in zip(QL, ALIAS[L]):
                if not K.any(): continue
                s = shat(q); s2 = np.vdot(s, s).real
                PT = np.eye(4) - np.outer(s, s.conj()) / s2
                a = (PT / s2) @ Qt.conj().T @ Tt @ b / L ** 4
                curv = np.outer(s, a) - np.outer(a, s)
                cmax = max(cmax, np.linalg.norm(curv))
            cs.append(cmax)
        ratio = cs[1] / cs[0]; es.append(ratio); okE &= 7 <= ratio <= 9
crit("E", okE, f"alias curvature c(0.02)/c(0.01) in [{min(es):.3f}, {max(es):.3f}] (p^3 => 8)")

# (F) contraction constant
g = (np.arange(6) + 0.5) / 6 * 2 * np.pi - np.pi
lam = 0.0
for p in itertools.product(g, repeat=4):
    QL = Qt_list(packs, L, np.array(p))
    lam = max(lam, sum(np.linalg.norm(Qt, 2) ** 2 for _, Qt in QL) / L ** 4)
crit("F", lam < 0.5, f"lambda_Q = L^-4 max_p sum_K ||Q_K||_op^2 = {lam:.4f} (L^-2 = {L**-2:.4f})")
# POST-HOC (added 2026-10-27 23:13 UTC after the F FAIL; not a pre-registered criterion): the operator of Lemma
# F-depth is G -> L^-4 P_perp sum_K Q_K P_T G P_T Q_K^+ P_perp; for positive G <= g its norm is bounded by
# lam' := L^-4 max_p ||P_perp (sum_K Q_K Q_K^+) P_perp||_op. P_perp removes the d.h (coarse gradient) part of Q_root.
lamp = 0.0
for p in itertools.product(g, repeat=4):
    p = np.array(p); QL = Qt_list(packs, L, p); sc = shat(p)
    Pp = np.eye(4) - np.outer(sc, sc.conj()) / np.vdot(sc, sc).real
    Ssum = sum(Qt @ Qt.conj().T for _, Qt in QL)
    lamp = max(lamp, np.linalg.norm(Pp @ Ssum @ Pp, 2) / L ** 4)
say(f"[F' post-hoc, informational] lambda' = L^-4 max_p ||P_perp sum_K Q_K Q_K^+ P_perp||_op = {lamp:.5f} (proof bound L^-2 = {L**-2:.5f})")

say(f"f1 done: {'ALL PASS' if not fails else 'FAIL: ' + ','.join(fails)}; wall {time.time()-t0:.1f}s")
with open(sys.argv[1] if len(sys.argv) > 1 else "f1_out.txt", "w") as f:
    f.write("\n".join(OUT) + "\n")
