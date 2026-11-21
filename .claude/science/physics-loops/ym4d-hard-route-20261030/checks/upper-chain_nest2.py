#!/usr/bin/env python3
"""Nest coercivity, second registration. Text 23.5 of parts/upper-chain.md. Definitions as in upper-chain_nest.py.

First run of upper-chain_nest.py, as registered: N0 FAIL, N1 FAIL, N2 PASS, N3 PASS.
  N0(b): c = 12.44, 14.58 at n = 1, 2 against that file's 9.0, 9.78. Cause, by hand: its value is a mode of period 2 L, which my torus
  with an odd number of blocks does not hold. So N0(b) was mis-registered; N0' below tests this.
  N1: d = 2, L = 3, n = 3: c = 14.84, 6.08, 3.05, 3.10 at depth 0, 1, 2, 3. d = 2, L = 5, n = 2: 14.84, 3.18, 3.19. d = 3, L = 3, n = 2: 9.77, 5.66, 6.23.
  So the ratio falls to 0.205 against my 0.5, but it does not go on falling with depth.

Hand derivation, written before this run. Take H normal only, a function f(x) of the normal coordinate. Then d H = 0, and D^* H = f'. Inside a frozen
layer, at scale l = s_1, the constraints on normal bonds with both ends in the layer read f_(i-1) + 4 f_i + f_(i+1) = 0 at the block nodes, for f
piecewise linear with kinks at block boundaries, and then f' is constant on each block, so P_N D^* H = 0 there. This has the solution f_i = A r^i,
r = -2 + 3^(1/2) = -0.268, decaying inward from the edge of the layer. There is no constraint centred on the edge, since a bond with one end outside
is free. Outside, f varies at the next scale L l, at a cost K_1 A^2 / (L l). The weighted norm has (A^2 / l) sum |r|^... = 0.289 A^2 / l from inside the
layer, with weight 1 / l^2. So c <= (K_1 A^2 / (L l)) / (0.289 A^2 / l) = 3.5 K_1 / L. The same fields exist in every dimension. So if this is right, the
constant C of `library/fibre-propagator.md`, Nest coercivity, is of order L at one jump, and not absolute; and each jump has its own mode, so it need
not compound. The repair: near the edge of a layer the weight should still be the coarser one, s~ := max(s_l, s_(l+1) 3.73^(-d / s_l)), d the distance
to the edge of the shadow of the layer.

Criteria, written before this run.
N0': d = 2, L = 3, no layer, X = 4, Bloch phase pi: c within 1 percent of 9.0 at n = 1, within 2 percent of 9.78 at n = 2.
N0'': against that file's Check N: d = 2, L = 3, n = 2, X = 4, phase pi, with layers on a whole level-2 block and a whole level-1 block inside it, and the plain weight
    s = L^n everywhere, as that check has it: c >= 0.9 * 9.78. Its value is 9.78 with and without the layer. This says my code sees what that check saw.
N4: 1D, normal-only fields, exact Rayleigh minimum c_1D(L), n = 2, depth 1, L in {3, 5, 7, 9, 15, 25, 41}. Claim: L c_1D(L) stays within a factor 2 over
    L >= 5, and c_1D(41) <= c_1D(5) / 4. c_1D is an upper bound for c in every d, so this alone refutes an absolute constant.
N5: full operator, d = 2, Bloch phase 0, n = 2, depth 1, L in {3, 5, 7, 9}. Claim: c(L) <= c_1D(L) (1 + 1e-6), and L c(L) within a factor 2 over L >= 5.
N6: no compounding, 1D: L = 3, n = 5, depth 1 to 5; L = 5, n = 4, depth 1 to 4. Claim: c_1D at depth >= 2 is at least (1/3) c_1D(depth 1), and at the
    deepest depth at least (1/2) c_1D(depth 2).
N7: the repaired weight: c~ >= 1 on N4's L in 1D, on N6's depths in 1D, and on N5's L in the full operator. FAIL would mean the repair is wrong.
N8: the mode above is a pure gauge, H = D w, w' = f: zero curvature, seen only by the gauge term. By Lemma Inv of that file a gauge direction is null for the
    true Hessian. So the question that matters is the inequality on the gauge slice. Put a weight tau on the gauge term, so c(tau) := min ( ||d H||^2 + tau ||P_N D^* H||^2 )
    / || H / s ||^2, and c_a(L) := c(10^4), which is the slice up to 1 / tau. Claim: c_a(L) >= 1 at L in {3, 5, 7, 9}, and c_a(9) >= c_a(5) / 2. FAIL would mean the
    loss in L is not only a gauge artefact.
Run: all PASS as registered. But N8's threshold was too weak to decide what it was for: c_a = 8.57, 5.75, 4.49, 3.71, so L c_a = 25.7 to 33.4, and the loss is NOT only a gauge artefact. See upper-chain_nest3.py.
"""
import importlib.util
import math
import os
import resource
import sys
import time

import numpy as np
import scipy.linalg as sl
import scipy.sparse as sp
import scipy.sparse.linalg as spl

RSS_LIMIT_GB = 2.0
RATE = 2 + 3**0.5


def rss_guard():
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9 > RSS_LIMIT_GB:
        raise SystemExit("RSS above limit")


here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("nest1", os.path.join(here, "upper-chain_nest.py"))
nest1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(nest1)


def nested_layers(L, n, depth, X, t_top=1, rs=None, t0=1):
    """Layers in the normal direction, as {l: (a_l, b_l)} in level-l units, centred, whole blocks, with clearance."""
    layers = {}
    if depth == 0:
        return layers
    I = X // 2
    # top layer: t_top level-n cells, in level-(n-1) units
    a, b = I * L, (I + t_top) * L
    layers[n - 1] = (a, b)
    for l in range(n - 2, n - 1 - depth, -1):
        # inside the shadow of Sigma_(l+1), which is [a, b) in level-(l+1) cells; whole level-(l+1) blocks of level-l cells
        r = rs if rs is not None else (1 if b - a <= 3 else 2)
        mid = (a + b) // 2
        na = max(a + r, mid - t0 // 2)
        nb = na + t0
        assert nb <= b - r, (L, n, depth, l, a, b, r)
        a, b = na * L, nb * L
        layers[l] = (a, b)
    return layers


def s_arrays(L, n, layers, Lx):
    """s and the repaired s~ on normal coordinates 0 .. Lx - 1."""
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


def one_d(L, n, X, layers):
    """Exact minimum of ||P_N f'||^2 / ||f / s||^2 over normal-only fields, for both weights."""
    Lx = X * L**n
    rows = []

    def q_row(l, i):
        sc = L**l
        v = np.zeros(Lx)
        for x0 in range(i * sc, (i + 1) * sc):
            for t in range(sc):
                v[(x0 + t) % Lx] += 1.0 / sc
        return v

    for i in range(X):
        rows.append(q_row(n, i))
    for l, (a, b) in layers.items():
        for i in range(a, b - 1):
            rows.append(q_row(l, i))
    C = np.array(rows)
    Z = sl.null_space(C, rcond=1e-10)
    # atoms: partition of normal coordinates
    atom = np.empty(Lx, dtype=np.int64)
    for x in range(Lx):
        lev = n
        for l in sorted(layers):
            a, b = layers[l]
            sc = L**l
            if a * sc <= x < b * sc:
                lev = l
                break
        atom[x] = (lev + 1) * 10**7 + x // L**lev
    # phi(x) = f(x) - f(x - 1) on sites
    Df = sp.diags([np.ones(Lx), -np.ones(Lx - 1), [-1.0]], [0, -1, Lx - 1], format="csr")
    Y = Df @ Z
    labels, inv = np.unique(atom, return_inverse=True)
    counts = np.bincount(inv)
    for j in range(Y.shape[1]):
        m = np.bincount(inv, weights=Y[:, j]) / counts
        Y[:, j] -= m[inv]
    A = Y.T @ Y
    s, st = s_arrays(L, n, layers, Lx)
    out = []
    for w in (s, st):
        B = Z.T @ (Z / w[:, None] ** 2)
        out.append(float(sl.eigh(A, B, eigvals_only=True, subset_by_index=[0, 0])[0]))
    rss_guard()
    return out


def full_sparse(L, X, tau=1.0):
    """d = 2, phase 0, n = 2, depth 1: smallest generalized eigenvalue on the constraints, for both weights."""
    n = 2
    layers = nested_layers(L, n, 1, X)
    (a, b) = layers[1]
    lat = nest1.Lat(2, L, n, X, (0.0,))
    D = lat.D().real.tocsr()
    C2 = lat.curl().real.tocsr()
    rows = []
    # top rows, dropping those implied by frozen level-1 bonds
    I0, I1 = a // L, b // L
    for y in lat.level_sites(n):
        i = y[0] // L**n
        for mu in range(2):
            if mu == 0 and I0 <= i and i + 1 < I1:
                continue
            if mu == 1 and I0 <= i < I1:
                continue
            rows.append(lat.q_row(y, mu, n))
    for y in lat.level_sites(1):
        i = y[0] // L
        if not a <= i < b:
            continue
        for mu in range(2):
            if mu == 0 and not i + 1 < b:
                continue
            rows.append(lat.q_row(y, mu, 1))
    C = nest1.stack(rows, lat.nb).real.tocsr()
    # atoms
    co = lat.coords()
    x0 = co[:, 0]
    inside = (x0 >= a * L) & (x0 < b * L)
    lev = np.where(inside, 1, n)
    ids = (lev + 1) * 10**10 + (co[:, 0] // L**lev) * 10**5 + co[:, 1] // L**lev
    _, inv = np.unique(ids, return_inverse=True)
    cnt = np.bincount(inv)
    W = sp.csr_matrix((1.0 / np.sqrt(cnt[inv]), (np.arange(lat.ns), inv)), shape=(lat.ns, len(cnt)))
    DW = (D @ W).tocsc() * tau**0.5
    As = (C2.T @ C2 + tau * (D @ D.T)).tocsc()
    na, nb, nc = len(cnt), lat.nb, C.shape[0]
    K = sp.bmat([[As, DW, C.T], [DW.T, sp.identity(na), None], [C, None, None]], format="csc")
    lu = spl.splu(K, permc_spec="COLAMD")
    rss_guard()
    s, st = s_arrays(L, n, layers, lat.shape[0])
    out = []
    for arr in (s, st):
        w = 1.0 / np.repeat(arr[x0], 2) ** 2

        def apply(y):
            rhs = np.zeros(nb + na + nc)
            rhs[:nb] = w * y
            return lu.solve(rhs)[:nb]

        T = spl.LinearOperator((nb, nb), matvec=apply, dtype=float)
        vals = spl.eigs(T, k=3, which="LM", tol=1e-7, maxiter=2000, return_eigenvectors=False)
        out.append(float(1.0 / np.max(vals.real)))
    rss_guard()
    return out


def main():
    t0 = time.time()
    c1, _ = nest1.coercivity(2, 3, 1, 4, {}, (math.pi,))
    c2, _ = nest1.coercivity(2, 3, 2, 4, {}, (math.pi,))
    print(f"N0' d=2 L=3 X=4 phase pi: n=1 c = {c1:.4f} (9.0), n=2 c = {c2:.4f} (9.78); elapsed {time.time() - t0:.0f} s", flush=True)
    ok0 = abs(c1 - 9.0) <= 0.09 and abs(c2 - 9.78) <= 0.2
    keep = nest1.weights
    nest1.weights = lambda lat, layers: np.full(lat.nb, 1.0 / float(lat.P) ** 2)
    c3, _ = nest1.coercivity(2, 3, 2, 4, {1: (6, 9), 0: (21, 24)}, (math.pi,))
    nest1.weights = keep
    print(f"N0'' plain weight, whole-block layers: c = {c3:.4f} (claim >= {0.9 * 9.78:.3f}); elapsed {time.time() - t0:.0f} s", flush=True)
    ok0b = c3 >= 0.9 * 9.78

    res = {}
    print("N4 1D, n = 2, depth 1:")
    for L in (3, 5, 7, 9, 15, 25, 41):
        c, ct = one_d(L, 2, 2 if L >= 25 else 4, nested_layers(L, 2, 1, 2 if L >= 25 else 4))
        res[L] = (c, ct)
        print(f"  L = {L}: c_1D = {c:.4f}, L c_1D = {L * c:.3f}; repaired c~ = {ct:.4f}; elapsed {time.time() - t0:.0f} s", flush=True)
    vals = [L * res[L][0] for L in res if L >= 5]
    ok4 = max(vals) / min(vals) <= 2 and res[41][0] <= res[5][0] / 4

    print("N5 full, d = 2, phase 0, n = 2, depth 1:")
    full = {}
    ok5 = True
    for L in (3, 5, 7, 9):
        c, ct = full_sparse(L, 2)
        full[L] = (c, ct)
        cu = one_d(L, 2, 2, nested_layers(L, 2, 1, 2))[0]
        ok5 = ok5 and c <= cu * (1 + 1e-6)
        print(f"  L = {L}: c = {c:.4f}, L c = {L * c:.3f}, c_1D at the same X = {cu:.4f}; repaired c~ = {ct:.4f}; elapsed {time.time() - t0:.0f} s", flush=True)
    v5 = [L * full[L][0] for L in full if L >= 5]
    ok5 = ok5 and max(v5) / min(v5) <= 2

    print("N6 1D, depth scan:")
    ok6 = True
    ct_all = [res[L][1] for L in res] + [full[L][1] for L in full]
    for L, n in ((3, 5), (5, 4)):
        cs = []
        for dep in range(1, n + 1):
            c, ct = one_d(L, n, 4, nested_layers(L, n, dep, 4))
            cs.append(c)
            ct_all.append(ct)
            print(f"  L = {L}, n = {n}, depth {dep}: c_1D = {c:.4f}, repaired c~ = {ct:.4f}; elapsed {time.time() - t0:.0f} s", flush=True)
        ok6 = ok6 and min(cs[1:]) >= cs[0] / 3 and cs[-1] >= cs[1] / 2
    ok7 = min(ct_all) >= 1.0
    print(f"N7 smallest repaired c~ = {min(ct_all):.4f} (claim >= 1)")
    print("N8 slice, full, d = 2, phase 0, n = 2, depth 1:")
    ca = {}
    for L in (3, 5, 7, 9):
        c100, _ = full_sparse(L, 2, tau=100.0)
        c1e4, _ = full_sparse(L, 2, tau=1e4)
        ca[L] = c1e4
        print(f"  L = {L}: c(tau = 1) = {full[L][0]:.4f}, c(100) = {c100:.4f}, c(10^4) = {c1e4:.4f}; elapsed {time.time() - t0:.0f} s", flush=True)
    ok8 = min(ca.values()) >= 1 and ca[9] >= ca[5] / 2
    print("N0'", "PASS" if ok0 else "FAIL")
    print("N0''", "PASS" if ok0b else "FAIL")
    print("N4", "PASS" if ok4 else "FAIL")
    print("N5", "PASS" if ok5 else "FAIL")
    print("N6", "PASS" if ok6 else "FAIL")
    print("N7", "PASS" if ok7 else "FAIL")
    print("N8", "PASS" if ok8 else "FAIL")


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
