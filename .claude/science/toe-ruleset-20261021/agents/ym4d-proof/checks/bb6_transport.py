"""bb6: residual transport (Lemma RT) and transported sizes (Lemma TC) in the d = 4 abelian chain (lane B session 6).

Criteria: checks/bb6_criteria.md (written before this script).
Part A: k = 2, L = 3, coarse side T = 2; critical point of E_src with every source class; identities.
Part B: depth scaling m = 1..3 of the transported top term (Q_str^{(L^m)})^T rho; no solve.
"""
import itertools
import time

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

T0 = time.time()
rng = np.random.default_rng(20261028)
L, T, D4 = 3, 2, 4
ALPHA = 0.25
PLANES = [(a, b) for a in range(D4) for b in range(a + 1, D4)]


def coords(M):
    g = np.indices((M,) * D4).reshape(D4, -1).T  # (V, 4), row-major site order
    return g


def sidx(z, M):
    z = np.mod(z, M)
    return ((z[..., 0] * M + z[..., 1]) * M + z[..., 2]) * M + z[..., 3]


def d1(M):
    V = M ** D4
    z = coords(M)
    rows, cols, vals = [], [], []
    for mu in range(D4):
        e = np.zeros(D4, int); e[mu] = 1
        r = mu * V + np.arange(V)
        rows += [r, r]; cols += [sidx(z + e, M), np.arange(V)]; vals += [np.ones(V), -np.ones(V)]
    return sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(D4 * V, V))


def d2(M):
    V = M ** D4
    z = coords(M)
    rows, cols, vals = [], [], []
    for p, (a, b) in enumerate(PLANES):
        ea = np.zeros(D4, int); ea[a] = 1
        eb = np.zeros(D4, int); eb[b] = 1
        r = p * V + np.arange(V)
        # F_ab = x_b(z+e_a) - x_b(z) - x_a(z+e_b) + x_a(z)
        for (comp, shift, sgn) in ((b, ea, 1.0), (b, 0 * ea, -1.0), (a, eb, -1.0), (a, 0 * eb, 1.0)):
            rows.append(r); cols.append(comp * V + sidx(z + shift, M)); vals.append(sgn * np.ones(V))
    return sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(6 * V, D4 * V))


OFFS = np.array(list(itertools.product((-1, 0, 1), repeat=D4)))  # block offsets (L = 3)


def qstr(Mf):
    Mc = Mf // L
    Vf, Vc = Mf ** D4, Mc ** D4
    X = coords(Mc)
    rows, cols, vals = [], [], []
    for mu in range(D4):
        e = np.zeros(D4, int); e[mu] = 1
        r = mu * Vc + np.arange(Vc)
        for o in OFFS:
            for j in range(L):
                rows.append(r); cols.append(mu * Vf + sidx(L * X + o + j * e, Mf)); vals.append(np.full(Vc, L ** -4.0))
    return sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(D4 * Vc, D4 * Vf))


def hmap(Mf):
    Mc = Mf // L
    Vf, Vc = Mf ** D4, Mc ** D4
    X = coords(Mc)
    rows, cols, vals = [], [], []
    for o in OFFS:
        cur = L * X.copy()
        for a in range(D4):
            e = np.zeros(D4, int); e[a] = 1
            if o[a] == 1:
                rows.append(np.arange(Vc)); cols.append(a * Vf + sidx(cur, Mf)); vals.append(np.full(Vc, 1.0 / len(OFFS)))
                cur = cur + e
            elif o[a] == -1:
                cur = cur - e
                rows.append(np.arange(Vc)); cols.append(a * Vf + sidx(cur, Mf)); vals.append(np.full(Vc, -1.0 / len(OFFS)))
    return sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(Vc, D4 * Vf))


def evmap(Mf):
    Mc = Mf // L
    Vc = Mc ** D4
    X = coords(Mc)
    return sp.csr_matrix((np.ones(Vc), (np.arange(Vc), sidx(L * X, Mf))), shape=(Vc, Mf ** D4))


out = []
k = 2
M0, M1, M2 = T * L ** 2, T * L, T
V0, V1, V2 = M0 ** D4, M1 ** D4, M2 ** D4
D1_0, D1_1, D1_2 = d1(M0), d1(M1), d1(M2)
D2_0, D2_1 = d2(M0), d2(M1)
Qs0, Qs1 = qstr(M0), qstr(M1)
H0, H1 = hmap(M0), hmap(M1)
Q0 = (Qs0 - D1_1 @ H0).tocsr()
Q1 = (Qs1 - D1_2 @ H1).tocsr()
E0, E1 = evmap(M0), evmap(M1)
out.append(f"Part A: d = 4, L = 3, k = 2, T = 2; unknowns x0: {4 * V0}, x1: {4 * V1}; nnz Q0 = {Q0.nnz}, D2_0 = {D2_0.nnz}; "
           f"build {time.time() - T0:.1f} s")

# A0 root covariance
lam0 = rng.standard_normal(V0); lam1 = rng.standard_normal(V1)
a0 = max(np.abs(Q0 @ (D1_0 @ lam0) - D1_1 @ (E0 @ lam0)).max() / np.abs(lam0).max(),
         np.abs(Q1 @ (D1_1 @ lam1) - D1_2 @ (E1 @ lam1)).max() / np.abs(lam1).max())
A0 = a0 <= 1e-12
out.append(f"A0 root covariance max|Q d lam - d ev lam|/max|lam| = {a0:.2e}: {'PASS' if A0 else 'FAIL'}")

k0, k1 = 1.0, 0.7
G0 = rng.standard_normal(6 * V0); G1 = rng.standard_normal(6 * V1)
j0 = D2_0.T @ rng.standard_normal(6 * V0); j1 = D2_1.T @ rng.standard_normal(6 * V1)
s0 = rng.standard_normal(4 * V1); s1 = rng.standard_normal(4 * V2)
B = rng.standard_normal(4 * V2)
n0 = 4 * V0


def Hmv(v):
    x0, x1 = v[:n0], v[n0:]
    r0 = Q0 @ x0 - x1
    r1 = Q1 @ x1
    g0 = D2_0.T @ (D2_0 @ x0) + k0 * (Q0.T @ r0)
    g1 = -k0 * r0 + k1 * (Q1.T @ r1)
    return np.concatenate([g0, g1])


b0 = D2_0.T @ G0 + j0 + Q0.T @ s0
b1 = D2_1.T @ G1 + j1 - s0 + Q1.T @ s1 + k1 * (Q1.T @ B)
bvec = np.concatenate([b0, b1])
Hop = spla.LinearOperator((len(bvec), len(bvec)), matvec=Hmv, dtype=float)
it = [0]


def cb(_):
    it[0] += 1


ts = time.time()
xs, info = spla.cg(Hop, bvec, rtol=1e-13, maxiter=6000, callback=cb)
relres = np.linalg.norm(Hmv(xs) - bvec) / np.linalg.norm(bvec)
A1 = relres <= 1e-9
out.append(f"A1 CG: info {info}, iterations {it[0]}, {time.time() - ts:.1f} s, relative residual {relres:.2e}: "
           f"{'PASS' if A1 else 'FAIL'}")
x0, x1 = xs[:n0], xs[n0:]
r0 = Q0 @ x0 - x1
r1 = Q1 @ x1 - B
rho0 = k0 * r0 - s0
rho1 = k1 * r1 - s1
cc0 = np.abs(D1_1.T @ rho0).max() / np.abs(rho0).max()
cc1 = np.abs(D1_2.T @ rho1).max() / np.abs(rho1).max()
A2 = max(cc0, cc1) <= 1e-7
out.append(f"A2 co-closedness max|d*rho_0|/max|rho_0| = {cc0:.2e}, max|d*rho_1|/max|rho_1| = {cc1:.2e}: {'PASS' if A2 else 'FAIL'}")
fun = np.abs(Q1.T @ rho1 - Qs1.T @ rho1).max() / np.abs(rho1).max()
A3 = fun <= 1e-7
out.append(f"A3 funnel max|Q1^T rho1 - Qstr1^T rho1|/max|rho1| = {fun:.2e}: {'PASS' if A3 else 'FAIL'}")
pred = s0 + Qs1.T @ rho1 - D2_1.T @ G1 - j1
tr = np.abs(k0 * r0 - pred).max() / np.abs(k0 * r0).max()
A4 = tr <= 1e-7
out.append(f"A4 transport max|k0 r0 - [s0 + Qstr1^T rho1 - d*G1 - j1]|/max|k0 r0| = {tr:.2e}: {'PASS' if A4 else 'FAIL'}")
v = rng.standard_normal(4 * V2)
ctl = np.abs(Q1.T @ v - Qs1.T @ v).max() / np.abs(v).max()
A5 = ctl >= 1e-3
out.append(f"A5 control (non-co-closed v) max|Q1^T v - Qstr1^T v|/max|v| = {ctl:.3e} (must be >= 1e-3): {'PASS' if A5 else 'FAIL'}")
# A6: coarse units at level 1 (k - 1 = 1): r^c = L^{k-1-0} r = 3 r ; level 2 coarse = own
tsup = L * np.abs(Qs1.T @ rho1).max()
A6 = tsup <= L ** -2 * np.abs(rho1).max() * (1 + 1e-12)
out.append(f"A6 coarse sup of Qstr1^T rho1 = {tsup:.4e} vs L^-2 max|rho1| = {L ** -2 * np.abs(rho1).max():.4e} "
           f"(ratio {tsup / (L ** -2 * np.abs(rho1).max()):.3f}): {'PASS' if A6 else 'FAIL'}")
# informational: the pieces of r0 in level-1 coarse units
pieces = {"s0": s0, "Qstr^T rho1": Qs1.T @ rho1, "d*G1": D2_1.T @ G1, "j1": j1}
out.append("  informational coarse sups of the r0 pieces (level-1 units): " +
           ", ".join(f"{nm} {L * np.abs(pc).max():.3e}" for nm, pc in pieces.items()))
del D2_0, Q0, Qs0, H0, xs, x0

# Part B
out.append("Part B: H_m = coarse-unit (Q_str^{(L^m)})^T rho, random level-k rho on side T = 2")
rhoB = rng.standard_normal((D4, T, T, T, T))
rmax = np.abs(rhoB).max()
B1 = B2 = B3 = True
norm_list = []
for m in (1, 2, 3):
    s = L ** m
    Mf = T * s
    blk = np.mod((np.arange(Mf) + (s - 1) // 2) // s, T)  # block index of each fine coordinate
    S = Dg = P = 0.0
    for mu in range(D4):
        R = rhoB[mu][np.ix_(blk, blk, blk, blk)]
        # H(z) = s^-2 * avg_{j<s} R(z - j e_mu)  (periodic)
        H = np.zeros_like(R)
        for j in range(s):
            H += np.roll(R, j, axis=mu)
        H *= 1.0 / (s ** 3)
        del R
        S = max(S, np.abs(H).max())
        for nu in range(D4):
            G = s * (np.roll(H, -1, axis=nu) - H)
            Dg = max(Dg, np.abs(G).max())
            offs = sorted(set([2 ** q for q in range(0, 10) if 2 ** q <= s] + [s]))
            for a in range(D4):
                for dlt in offs:
                    P = max(P, np.abs(np.roll(G, -dlt, axis=a) - G).max() / (dlt / s) ** ALPHA)
            del G
        del H
    b1 = S <= L ** (-2 * m) * rmax * (1 + 1e-12)
    b2 = Dg <= 2 * L ** m * S * (1 + 1e-12)
    b3 = P <= 2 * L ** (ALPHA * m) * Dg * (1 + 1e-12)
    B1, B2, B3 = B1 and b1, B2 and b2, B3 and b3
    nrm = L ** ((1 - ALPHA) * m) * P / rmax
    norm_list.append(nrm)
    out.append(f"  m = {m}: S_m L^(2m)/max|rho| = {S * L ** (2 * m) / rmax:.4f} [B1 {'PASS' if b1 else 'FAIL'}]; "
               f"D_m/(2 L^m S_m) = {Dg / (2 * L ** m * S):.4f} [B2 {'PASS' if b2 else 'FAIL'}]; "
               f"P_m/(2 L^(am) D_m) = {P / (2 * L ** (ALPHA * m) * Dg):.4f} [B3 {'PASS' if b3 else 'FAIL'}]; "
               f"L^((1-a)m) P_m/max|rho| = {nrm:.4f}; D_m L^m/max|rho| = {Dg * L ** m / rmax:.4f}")
B4 = max(norm_list) / min(norm_list) <= 3
out.append(f"B4 [guess, informational] normalised Hoelder proxy varies by factor {max(norm_list) / min(norm_list):.3f} "
           f"(<= 3?): {'holds' if B4 else 'FAILED'}")
allp = A0 and A1 and A2 and A3 and A4 and A5 and A6 and B1 and B2 and B3
out.append(f"VERDICT: {'ALL PASS' if allp else 'NOT ALL PASS'} (A0-A6, B1-B3)")
out.append(f"[t = {time.time() - T0:.1f} s]")
print("\n".join(out))
