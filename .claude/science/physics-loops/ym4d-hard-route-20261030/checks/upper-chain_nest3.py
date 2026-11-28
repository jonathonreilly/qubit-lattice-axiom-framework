#!/usr/bin/env python3
"""Nest coercivity, third registration: compounding with depth, and the role of clearance. Text 23.5 of parts/upper-chain.md.

Second registration (upper-chain_nest2.py): all PASS as registered, but two readings go beyond a PASS.
  N6, in 1D: L = 3, n = 5: c_1D = 5.90, 3.81, 2.75, 2.01, 2.02 at depth 1 to 5; L = 5, n = 4: 3.79, 2.97, 2.49, 2.49. It passed my thresholds, yet it falls with depth,
  by about 0.7 per level at L = 3, at clearance 1. So I cannot yet say it does not compound.
  N8: c_a = 8.57, 5.75, 4.49, 3.71 at L = 3, 5, 7, 9. It passed my threshold, yet L c_a = 25.7, 28.8, 31.4, 33.4: the slice loses a factor near L too. So the loss is NOT only a
  gauge artefact, as I had guessed when I registered N8. Reason, by hand: a coarse field with curvature at the next scale has the same normal component at the edge.

Here: normal-only fields only, so this reads the weight and the constraints, in any dimension, as an exact Rayleigh minimum, which is an upper bound for the constant
of the full problem. Sparse solver, so that many levels are in reach. c is with s, c~ with the repaired weight s~ := max(s_l, s_(l+1) 3.73^(-d / s_l)).

Configurations (L, r, t0, top width, n, X): r the clearance and t0 the thickness in parent cells.
  A (3, 1, 1, 1, 9, 4);  B (3, 2, 2, 2, 8, 6);  C (3, 3, 3, 3, 7, 8);  D (5, 1, 1, 1, 6, 4);  E (5, 2, 1, 1, 6, 4);  F (9, 3, 1, 1, 4, 4);  G (15, 5, 2, 1, 3, 4).

A first attempt at the sizes above produced no output in 8 minutes, at A with n = 9, since the Krylov space was too small, and I stopped it holding the lock, with no result seen. The run below
has ncv = 30, and n reduced: A n = 8, B n = 7, C n = 6, D n = 5, E n = 5; F, G and the added H, I, J as written. The criteria are unchanged.
A second attempt stopped at the guard on RSS, with no result, in the sparse LU of the full KKT system, because of the long constraint rows. The solver is now a shift by 1, a sparse LU of the
part without constraints, and the constraints by a dense Schur step, with at most about 100 rows. It is checked against the dense values of the second registration by V below.

V: at L = 5, n = 4, X = 4, depth 1 to 4 this reproduces c_1D, c~ of upper-chain_nest2.py, 3.7904, 2.9735, 2.4859, 2.4900, to within 1 percent (geometry of nested_layers there: clearance 1 if the parent has width at most 3, else 2).

Criteria, written before this run.
N9a: c~ >= 1 at every configuration and depth.
N9b: the repaired weight does not compound: at each configuration, min over depth of c~ >= (1/2) c~(depth 1).
N9c: with clearance r >= 2 the sharp weight does not compound beyond the first jump: at B, C, E, F, G, min over depth >= 2 of c >= (1/2) c(depth 2).
N9d, a report and not a claim: the fall of c per level at A and D, clearance 1.
A FAIL of N9a or N9b would mean the repaired statement is wrong; a FAIL of N9c would mean that even clearance does not stop the sharp weight from compounding.

Hand derivation of how clearance enters, written before this run. Between a level-l strip and the edge of its parent layer, f can solve the zero-cost recurrence f_(j-1) + 4 f_j + f_(j+1) = 0
in parent cells, and going outward from an inner edge it grows by 3.73 per cell. So a mode with amplitude A at the inner edge has amplitude B = 3.73^r A at the outer edge, and it costs
K_1 B^2 / (L l_2) at the next scale, against K_1 A^2 / l_2 if it stops at once. So if 3.73^(2 r) < L, the mode spans two jumps, and the sharp weight loses a further factor 3.73^(2 r) / L per level:
true compounding, unless r >= (log L) / (2 log 3.73). That is the scale of the clearance r_S that hard-core--mapped asks for another reason.
Added configurations: H (25, 1, 1, 1, 3, 2), I (41, 1, 1, 1, 3, 2), J (25, 3, 1, 1, 3, 2).
N9e: at clearance 1 and L >> 14 the sharp weight compounds: c(depth 2) / c(depth 1) at I is at most 0.6, and is below that at H.
N9f: at clearance 3 it does not: c(depth 2) / c(depth 1) at J is at least 0.7. Repaired weights at H, I, J fall under N9a, N9b.
Run with the Schur solver, as registered: V PASS. N10 PASS. N9c PASS. N9f PASS. N9a, N9b FAIL, only through c~ = -0.0000 at I, depth 3: the pseudo-inverse dropped a constraint, an artefact, and every other c~ is at least 5.6.
N9e FAIL, and it was not a test: my helper centres each layer in its parent, so the clearance is about L / 2 for every r at L >= 5, H and J gave the same numbers, and the case I meant was not run. Values at clearance 1, L = 3 (A): c = 5.90, 3.82, 2.84, 2.30, 1.96, 1.71, 1.47, 1.47; c~ = 10.46, 9.15, 7.97, 7.07, 6.43, 5.96, 5.61, 5.63. Clearance 2, L = 3 (B): c = 6.35, 5.42, 5.03, 4.82, 4.65, 4.40, 4.40; c~ = 10.12, 9.99, 9.91, 9.86, 9.83, 9.73, 9.82. Clearance 3, L = 3 (C): c = 6.52, 6.10, 5.92, 5.76, 5.36, 5.36; c~ = 10.04, 10.08, 10.10, 10.11, 9.43, 10.14.
Fourth registration, written before the fourth run. Layers placed at exactly r parent cells from the edge of the parent ("edge"), rows scaled before the inverse, and a spectral cut at 1e-13. Configurations, all edge, (L, r, t0, top, n, X): H' (25, 1, 1, 1, 3, 2); I' (41, 1, 1, 1, 3, 2); J' (25, 3, 1, 1, 3, 2); K (5, 1, 2, 1, 4, 4); M (9, 2, 4, 1, 4, 4); N (15, 3, 6, 1, 3, 4).
N11a: c~ >= 1 at every configuration and depth, A to J and the new ones, with no artefact. N11b: at each, min over depth of c~ >= (1/2) c~(depth 1).
N11e: the prediction: at clearance 1 and L >> 14 the sharp weight loses a further factor per level: c(2)/c(1) at I' is at most 0.6, and below that at H'. N11f: at clearance 3 it does not: c(2)/c(1) at J' is at least 0.7.
N11g: the shape asked by hard-core--mapped, w_0 >= 2 r_S (K, M, N): min over depth of c~ >= (1/2) c~(depth 1).
Fourth run: N11a, N11b, N11e, N11f, N11g all PASS. c(2)/c(1) = 0.174, 0.111 at H', I', and 0.884 at J'. c~ between 5.6 (A, L = 3, clearance 1, thickness 1) and 11.6, and near 9.9 at large L. A last run of the code below reproduces all of these, with V and N10.
N10: the repaired weight in the full operator, on the layers of the first run: d = 2, L = 3, n = 3, depth 1 to 3; d = 2, L = 5, n = 2, depth 1, 2; d = 3, L = 3, n = 2, depth 1, 2; phases as there.
    Claim: c~ >= 1 everywhere, and c~(deepest) >= (1/2) c~(depth 1) at each. Normal-only fields are not all the modes at nonzero phase, so this is not implied by N9.
"""
import importlib.util
import os
import resource
import sys
import time

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spl

RSS_LIMIT_GB = 2.0
RATE = 2 + 3**0.5


def rss_guard():
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9 > RSS_LIMIT_GB:
        raise SystemExit("RSS above limit")


def layers_for(L, n, depth, X, t_top, r, t0, edge=False):
    layers = {}
    if depth == 0:
        return layers
    I = X // 2
    a, b = I * L, (I + t_top) * L
    layers[n - 1] = (a, b)
    for l in range(n - 2, n - 1 - depth, -1):
        mid = (a + b) // 2
        na = a + r if edge else max(a + r, mid - t0 // 2)
        nb = na + t0
        assert nb <= b - r, (L, n, depth, l, a, b, r, t0)
        a, b = na * L, nb * L
        layers[l] = (a, b)
    return layers


def q_row(L, l, i, Lx):
    """Triangular weights of the normal line average of level-l bond i: from [i s, (i + 1) s) to one s further."""
    s = L**l
    x0 = i * s
    idx = (x0 + np.arange(2 * s - 1)) % Lx
    w = np.minimum(np.arange(1, 2 * s), np.arange(2 * s - 1, 0, -1)) / s
    return idx, w


def build_rows(L, n, X, layers):
    Lx = X * L**n
    rows = []

    def implied(m, i):
        # both level-m cells have all children in Sigma_(m-1)
        if m - 1 not in layers:
            return False
        a, b = layers[m - 1]
        return a <= i * L and (i + 2) * L <= b

    for i in range(X):
        if not implied(n, i):
            rows.append(q_row(L, n, i, Lx))
    for l, (a, b) in layers.items():
        for i in range(a, b - 1):
            if not implied(l, i):
                rows.append(q_row(L, l, i, Lx))
    r, c, v = [], [], []
    for k, (idx, w) in enumerate(rows):
        r.append(np.full(len(idx), k))
        c.append(idx)
        v.append(w)
    r, c, v = np.concatenate(r), np.concatenate(c), np.concatenate(v)
    return sp.csr_matrix((v, (r, c)), shape=(len(rows), Lx))


def weights(L, n, layers, Lx):
    x = np.arange(Lx)
    s = np.full(Lx, float(L**n))
    st = np.full(Lx, float(L**n))
    for l in sorted(layers, reverse=True):
        a, b = layers[l]
        sc = L**l
        lo, hi = a * sc, b * sc
        inside = (x >= lo) & (x < hi)
        if l >= 1:
            s[inside] = float(sc)
            d = np.minimum(x - lo, hi - 1 - x)[inside]
            st[inside] = np.maximum(float(sc), float(L ** (l + 1)) * RATE ** (-d / sc))
    return s, st


def solve(L, n, X, layers):
    """Smallest generalized eigenvalue on the constraints: shift by sigma, sparse LU for the unconstrained part, constraints by a dense Schur step."""
    Lx = X * L**n
    C = build_rows(L, n, X, layers)
    E = C.toarray()
    lev = np.full(Lx, n)
    x = np.arange(Lx)
    for l in sorted(layers, reverse=True):
        a, b = layers[l]
        sc = L**l
        lev[(x >= a * sc) & (x < b * sc)] = l
    ids = (lev.astype(np.int64) + 1) * 10**9 + x // (L ** lev.astype(np.int64))
    _, inv = np.unique(ids, return_inverse=True)
    cnt = np.bincount(inv)
    W = sp.csr_matrix((1.0 / np.sqrt(cnt[inv]), (x, inv)), shape=(Lx, len(cnt)))
    Df = sp.diags([np.ones(Lx), -np.ones(Lx - 1), [-1.0]], [0, -1, Lx - 1], format="csr")
    As = (Df.T @ Df).tocsc()
    G = (Df.T @ W).tocsc()
    s, st = weights(L, n, layers, Lx)
    sigma = 1.0
    out = []
    for arr in (s, st):
        w = 1.0 / arr**2
        M = sp.bmat([[As + sigma * sp.diags(w), G], [G.T, sp.identity(len(cnt))]], format="csc")
        lu = spl.splu(M, permc_spec="MMD_AT_PLUS_A")
        nM = M.shape[0]
        U = np.zeros((Lx, E.shape[0]))
        for k in range(E.shape[0]):
            rhs = np.zeros(nM)
            rhs[:Lx] = E[k]
            U[:, k] = lu.solve(rhs)[:Lx]
        Smat = E @ U
        dg = np.sqrt(np.maximum(np.diag(Smat), 1e-300))
        ev, vec = np.linalg.eigh((Smat / dg[:, None]) / dg[None, :])
        keep = ev > 1e-13 * ev.max()
        Sinv = ((vec[:, keep] / ev[keep]) @ vec[:, keep].T / dg[:, None]) / dg[None, :]
        rss_guard()

        def apply(y):
            rhs = np.zeros(nM)
            rhs[:Lx] = w * y
            z = lu.solve(rhs)[:Lx]
            return z - U @ (Sinv @ (E @ z))

        T = spl.LinearOperator((Lx, Lx), matvec=apply, dtype=float)
        vals = spl.eigs(T, k=2, which="LM", ncv=30, tol=1e-6, maxiter=3000, return_eigenvectors=False)
        out.append(float(1.0 / np.max(vals.real) - sigma))
    rss_guard()
    return out


CONFIGS = {
    "A": (3, 1, 1, 1, 8, 4),
    "B": (3, 2, 2, 2, 7, 6),
    "C": (3, 3, 3, 3, 6, 8),
    "D": (5, 1, 1, 1, 5, 4),
    "E": (5, 2, 1, 1, 5, 4),
    "F": (9, 3, 1, 1, 4, 4),
    "G": (15, 5, 2, 1, 3, 4),
    "H": (25, 1, 1, 1, 3, 2),
    "I": (41, 1, 1, 1, 3, 2),
    "J": (25, 3, 1, 1, 3, 2),
}

EDGE = {
    "H'": (25, 1, 1, 1, 3, 2),
    "I'": (41, 1, 1, 1, 3, 2),
    "J'": (25, 3, 1, 1, 3, 2),
    "K": (5, 1, 2, 1, 4, 4),
    "M": (9, 2, 4, 1, 4, 4),
    "N": (15, 3, 6, 1, 3, 4),
}


def main():
    t0_ = time.time()
    ref = [3.7904, 2.9735, 2.4859, 2.4900]
    ok_v = True
    for dep in range(1, 5):
        c, _ = solve(5, 4, 4, layers_for(5, 4, dep, 4, 1, 2, 1))
        print(f"V depth {dep}: c = {c:.4f}, dense {ref[dep - 1]}; elapsed {time.time() - t0_:.0f} s", flush=True)
        ok_v = ok_v and abs(c - ref[dep - 1]) <= 0.01 * ref[dep - 1]
    ok_a, ok_b = True, True
    results = {}
    for table, edge in ((CONFIGS, False), (EDGE, True)):
        for name, (L, r, t0, t_top, n, X) in table.items():
            cs, cts = [], []
            for dep in range(1, n + 1):
                c, ct = solve(L, n, X, layers_for(L, n, dep, X, t_top, r, t0, edge))
                cs.append(c)
                cts.append(ct)
            results[name] = (cs, cts)
            print(f"{name} L={L} r={r} t0={t0} n={n} {'edge' if edge else 'centred'}: c = {[round(x, 3) for x in cs]}; c~ = {[round(x, 3) for x in cts]}; elapsed {time.time() - t0_:.0f} s", flush=True)
            ok_a = ok_a and min(cts) >= 1
            ok_b = ok_b and min(cts) >= cts[0] / 2
    rH = results["H'"][0][1] / results["H'"][0][0]
    rI = results["I'"][0][1] / results["I'"][0][0]
    rJ = results["J'"][0][1] / results["J'"][0][0]
    print(f"N11e ratio c(2)/c(1): H' = {rH:.3f}, I' = {rI:.3f}; N11f: J' = {rJ:.3f}")
    ok_g = all(min(results[k][1]) >= results[k][1][0] / 2 for k in ("K", "M", "N"))
    here = os.path.dirname(os.path.abspath(__file__))
    spec = importlib.util.spec_from_file_location("nest1", os.path.join(here, "upper-chain_nest.py"))
    nest1 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nest1)

    def repaired(lat, layers):
        _, st = weights(lat.L, lat.n, layers, lat.shape[0])
        return 1.0 / np.repeat(st[lat.coords()[:, 0]], lat.d) ** 2

    nest1.weights = repaired
    ok10 = True
    cases = [
        ("d=2 L=3 n=3", 2, 3, 3, 3, [{2: (3, 6)}, {2: (3, 6), 1: (12, 15)}, {2: (3, 6), 1: (12, 15), 0: (39, 42)}], [(0.0,), (0.8,)]),
        ("d=2 L=5 n=2", 2, 5, 2, 3, [{1: (5, 10)}, {1: (5, 10), 0: (35, 40)}], [(0.0,), (0.8,)]),
        ("d=3 L=3 n=2", 3, 3, 2, 2, [{1: (3, 6)}, {1: (3, 6), 0: (12, 15)}], [(0.0, 0.0)]),
    ]
    for nm, d, L, n, X, depth_layers, phases in cases:
        vals = []
        for lay in depth_layers:
            v = min(nest1.coercivity(d, L, n, X, lay, k)[0] for k in phases)
            vals.append(v)
            print(f"N10 {nm} layers {sorted(lay)}: c~ = {v:.4f}; elapsed {time.time() - t0_:.0f} s", flush=True)
        ok10 = ok10 and min(vals) >= 1 and vals[-1] >= vals[0] / 2
    print("V", "PASS" if ok_v else "FAIL")
    print("N10", "PASS" if ok10 else "FAIL")
    print("N11a", "PASS" if ok_a else "FAIL")
    print("N11b", "PASS" if ok_b else "FAIL")
    print("N11e", "PASS" if rI <= 0.6 and rI < rH else "FAIL")
    print("N11f", "PASS" if rJ >= 0.7 else "FAIL")
    print("N11g", "PASS" if ok_g else "FAIL")


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
