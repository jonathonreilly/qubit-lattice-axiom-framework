"""c20: background-regularity diagnostic for BG-b (criteria: checks/c20_criteria.md, written before this script).

2D abelian linearised model. Soft-constraint chain minimiser with the linearised S4' contour averaging; mean
oscillation A_j of the coarse-unit curvature over level-j cubes; synthetic controls C1-C3.
"""
import itertools
import time

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

RNG = np.random.default_rng(20261027)


def lidx(x1, x2, mu, n):
    return mu * n * n + (x1 % n) * n + (x2 % n)


def dmat(n):
    rows, cols, vals = [], [], []
    for x1 in range(n):
        for x2 in range(n):
            p = x1 * n + x2
            for (a, b, mu, s) in [(x1, x2, 0, 1), (x1 + 1, x2, 1, 1), (x1, x2 + 1, 0, -1), (x1, x2, 1, -1)]:
                rows.append(p); cols.append(lidx(a, b, mu, n)); vals.append(s)
    return sp.csr_matrix((vals, (rows, cols)), shape=(n * n, 2 * n * n))


def path_terms(a, b, order, n):
    """Signed links of the axial path a -> b moving in coordinates `order` (no wrap ambiguity: |b-a| < L)."""
    out = []
    z = list(a)
    for c in order:
        while z[c] != b[c]:
            step = 1 if b[c] > z[c] else -1
            if step == 1:
                out.append((lidx(z[0], z[1], c, n), 1.0))
            else:
                w = list(z); w[c] -= 1
                out.append((lidx(w[0], w[1], c, n), -1.0))
            z[c] += step
    return out


def qmat(n, L):
    """Linearised S4' from the level-i lattice of side n to side n // L."""
    m = n // L
    h = (L - 1) // 2
    rows, cols, vals = [], [], []
    w = 1.0 / (2 * L * L)
    for X1 in range(m):
        for X2 in range(m):
            cX = (L * X1 + h, L * X2 + h)
            for mu in range(2):
                r = mu * m * m + X1 * m + X2
                e = [0, 0]; e[mu] = L
                cY = (cX[0] + e[0], cX[1] + e[1])
                for t1 in range(L):
                    for t2 in range(L):
                        y = (L * X1 + t1, L * X2 + t2)
                        yL = (y[0] + e[0], y[1] + e[1])
                        terms = []
                        straight = [(lidx(y[0] + (k if mu == 0 else 0), y[1] + (k if mu == 1 else 0), mu, n), 1.0)
                                    for k in range(L)]
                        for order in ((0, 1), (1, 0)):
                            terms += path_terms(cX, y, order, n)
                            terms += straight
                            terms += [(j, -s) for j, s in path_terms(cY, yL, order, n)]
                        for j, s in terms:
                            rows.append(r); cols.append(j); vals.append(w * s)
    return sp.csr_matrix((vals, (rows, cols)), shape=(2 * m * m, 2 * n * n))


def build(L, nlev, Tc):
    sides = [Tc * L ** (nlev - i) for i in range(nlev + 1)]
    D = [dmat(s) for s in sides]
    Q = [qmat(sides[i], L) for i in range(nlev)]
    return sides, D, Q


def solve_chain(sides, D, Q, Bn, kappa, L, tau):
    nlev = len(Q)
    kap = [kappa * L ** (-2 * i) for i in range(nlev)]
    dims = [2 * s * s for s in sides[:nlev]]
    off = np.concatenate([[0], np.cumsum(dims)])
    N = int(off[-1])

    def H(x):
        B = [x[off[i]:off[i + 1]] for i in range(nlev)]
        y = [np.zeros(d) for d in dims]
        y[0] += D[0].T @ (D[0] @ B[0]) + tau * B[0]
        for i in range(nlev):
            r = Q[i] @ B[i] - (B[i + 1] if i + 1 < nlev else 0.0)
            y[i] += kap[i] * (Q[i].T @ r)
            if i + 1 < nlev:
                y[i + 1] -= kap[i] * r
        return np.concatenate(y)

    rhs = np.zeros(N)
    rhs[off[nlev - 1]:off[nlev]] = kap[nlev - 1] * (Q[nlev - 1].T @ Bn)
    # exact Jacobi diagonal of H
    dg = [np.asarray(D[0].multiply(D[0]).sum(axis=0)).ravel() + tau]
    dg += [np.full(d, kap[i - 1]) for i, d in enumerate(dims) if i >= 1]
    for i in range(nlev):
        dg[i] = dg[i] + kap[i] * np.asarray(Q[i].multiply(Q[i]).sum(axis=0)).ravel()
    diag = np.concatenate(dg)
    M = spla.LinearOperator((N, N), matvec=lambda v: v / diag)
    A = spla.LinearOperator((N, N), matvec=H)
    it = [0]
    x, info = spla.cg(A, rhs, rtol=1e-12, maxiter=200000, M=M, callback=lambda xk: it.__setitem__(0, it[0] + 1))
    res = np.linalg.norm(H(x) - rhs) / np.linalg.norm(rhs)
    B = [x[off[i]:off[i + 1]] for i in range(nlev)]
    return B, info, it[0], res


def osc_stats(fj, side, L):
    """fj: plaquette field (side*side) on the level-j lattice. Level-j cubes = L x L site blocks."""
    F = fj.reshape(side, side)
    m = side // L
    osc = np.empty((m, m)); sup = np.empty((m, m))
    for X1 in range(m):
        for X2 in range(m):
            i1 = (np.arange(L * X1 - 1, L * X1 + L + 1)) % side
            i2 = (np.arange(L * X2 - 1, L * X2 + L + 1)) % side
            W = F[np.ix_(i1, i2)]
            osc[X1, X2] = W.max() - W.min()
            sup[X1, X2] = np.abs(W).max()
    return osc.mean(), osc.max(), sup.mean(), osc


def classify(A):
    r = [A[j] / A[j + 1] for j in range(len(A) - 1)]
    if max(r) <= 0.7:
        c = 'SUMMABLE'
    elif r[0] >= 0.9:
        c = 'NOT-SUMMABLE'
    else:
        c = 'UNDECIDED'
    return r, c


def controls(sides, L, nlev, Tc):
    out = {}
    # C1 smooth
    A = []
    for j in range(nlev):
        s = sides[j]
        u = (np.arange(s) + 0.5) * L ** (j - nlev)
        f = np.sin(2 * np.pi * u[:, None] / Tc) * np.cos(2 * np.pi * u[None, :] / Tc)
        A.append(osc_stats(f.ravel(), s, L)[0])
    out['C1'] = A
    # C2 multi-level jumps, jumps proportional to the block size
    signs = {i: RNG.choice([-1.0, 1.0], size=(Tc * L ** (nlev - i), Tc * L ** (nlev - i))) for i in range(1, nlev + 1)}
    A = []
    for j in range(nlev):
        s = sides[j]
        u = (np.arange(s) + 0.5) * L ** (j - nlev)  # coarse units
        f = np.zeros((s, s))
        for i in range(1, nlev + 1):
            bs = L ** (i - nlev)  # level-i block size in coarse units
            k = np.floor(u / bs).astype(int)
            f += L ** (-(nlev - i)) * signs[i][np.ix_(k, k)]
        A.append(osc_stats(f.ravel(), s, L)[0])
    out['C2'] = A
    # C3 rough
    A = []
    for j in range(nlev):
        s = sides[j]
        A.append(osc_stats(RNG.normal(size=s * s), s, L)[0])
    out['C3'] = A
    return out


def main():
    runs = [(3, 4, 4, 1.0), (3, 4, 4, 10.0), (5, 3, 2, 1.0)]
    lines = []
    V1 = True; V2 = True
    built = {}
    for (L, nlev, Tc, kappa) in runs:
        key = (L, nlev, Tc)
        if key not in built:
            t0 = time.time()
            built[key] = build(L, nlev, Tc)
            lines.append(f"build L={L} n={nlev} Tc={Tc}: fine side {built[key][0][0]}, {time.time()-t0:.1f} s")
            ctl = controls(built[key][0], L, nlev, Tc)
            for name, A in ctl.items():
                r, c = classify(A)
                exp = 'NOT-SUMMABLE' if name == 'C3' else 'SUMMABLE'
                if c != exp:
                    V2 = False
                lines.append(f"  control {name}: A_j (j=0..{nlev-1}) = {np.array2string(np.array(A), precision=4)}"
                             f"  ratios {np.array2string(np.array(r), precision=3)}  -> {c} (expected {exp})")
        sides, D, Q = built[key]
        Bn = RNG.normal(size=2 * sides[nlev] ** 2) if (key, 'Bn') not in built else built[(key, 'Bn')]
        built[(key, 'Bn')] = Bn
        t0 = time.time()
        B1, info1, it1, res1 = solve_chain(sides, D, Q, Bn, kappa, L, 1e-9)
        B2, info2, it2, res2 = solve_chain(sides, D, Q, Bn, kappa, L, 1e-10)
        dt = time.time() - t0
        f1 = [L ** (2 * (nlev - j)) * (D[j] @ B1[j]) for j in range(nlev)]
        f2 = [L ** (2 * (nlev - j)) * (D[j] @ B2[j]) for j in range(nlev)]
        stab = max(np.abs(a - b).max() / np.abs(a).max() for a, b in zip(f1, f2))
        if not (stab <= 1e-5 and info1 == 0 and info2 == 0):
            V1 = False
        A, G, S = [], [], []
        osc0 = None
        for j in range(nlev):
            a, g, s_, osc = osc_stats(f1[j], sides[j], L)
            A.append(a); G.append(g); S.append(s_)
            if j == 0:
                osc0 = osc
        r, c = classify(A)
        # informational: share of the level-0 oscillation sum in cubes whose window meets a level-n block-centre line
        s0 = sides[0]; m0 = s0 // L; h = (L ** nlev - 1) // 2
        centres = set((np.arange(Tc) * L ** nlev + h).tolist())
        near = np.zeros((m0, m0), dtype=bool)
        for X1 in range(m0):
            for X2 in range(m0):
                r1 = set(((np.arange(L * X1 - 1, L * X1 + L + 2)) % s0).tolist())
                r2 = set(((np.arange(L * X2 - 1, L * X2 + L + 2)) % s0).tolist())
                near[X1, X2] = bool(r1 & centres) or bool(r2 & centres)
        share = osc0[near].sum() / osc0.sum()
        frac = near.mean()
        dBn = np.abs(D[nlev] @ Bn).max()
        lines.append(f"model L={L} n={nlev} Tc={Tc} kappa={kappa}: CG it {it1}/{it2}, rel.res {res1:.1e}/{res2:.1e}, "
                     f"tau-stability {stab:.1e}, {dt:.1f} s")
        lines.append(f"  A_j = {np.array2string(np.array(A), precision=5)}  ratios {np.array2string(np.array(r), precision=3)}"
                     f"  -> {c}")
        lines.append(f"  G_j = {np.array2string(np.array(G), precision=5)}  S_j = {np.array2string(np.array(S), precision=4)}"
                     f"  sup|f_0|/max|dB_n| = {np.abs(f1[0]).max()/dBn:.3f}")
        lines.append(f"  level-0 osc share in cubes meeting a level-n centre line: {share:.3f} (cube fraction {frac:.3f})")
    lines.append(f"V1 (tau-stability, CG converged): {'PASS' if V1 else 'FAIL'}")
    lines.append(f"V2 (controls classify as expected): {'PASS' if V2 else 'FAIL'}")
    lines.append(f"c20 diagnostic: {'VALID' if V1 and V2 else 'INVALID'}; model classifications above are the finding")
    print("\n".join(lines))


if __name__ == '__main__':
    main()
