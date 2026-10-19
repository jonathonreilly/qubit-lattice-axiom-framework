"""C9 / 03: independent numerical route (optimisation, no lexicographic argument) for the step
'alpha(P_{0,e}) must be a nearest-neighbour swap'.

For a TI SU(2)-symmetric QCA, g := alpha(P_{0,e1}) is a self-adjoint unitary, SU(2)-invariant,
normalised trace 1/2, and [g, T_t g] = 0 for every t with {0,e1} cap ({0,e1}+t) = empty.
We search, inside a finite window Wn, for ALL such g by least squares from many random starts
over the full SU(2)-invariant Hermitian algebra of the window, imposing commutation with every
translate T_t g whose support overlaps Wn (t not in {0, +-e1}).  Prediction (Theorem 1 steps
C-E): the only solutions are P on the e1-bonds inside the window.

Windows: 1D chain [0,1,2,3] (14-dim algebra); 2D square 2x2 (14-dim).
"""
from __future__ import annotations

import itertools
import sys
import numpy as np
from scipy.optimize import least_squares

from c9_common import Counter, all_perm_ops, embed, swap_op, perm_op


class Embedder:
    """Cached version of c9_common.embed (same formula, permutation matrix precomputed)."""
    def __init__(self, sub, full):
        n, k = len(full), len(sub)
        pos = [full.index(s) for s in sub]
        rest = [i for i in range(n) if i not in pos]
        self.Pm = perm_op(n, pos + rest)
        self.I = np.eye(2 ** (n - k), dtype=complex)

    def __call__(self, op):
        return self.Pm @ np.kron(op, self.I) @ self.Pm.T


def herm_basis(n):
    ops = all_perm_ops(n)
    cands = []
    for P in ops:
        cands.append(P + P.conj().T)
        cands.append(1j * (P - P.conj().T))
    # orthonormalise (Hilbert-Schmidt), keep independent
    basis = []
    for c in cands:
        v = c.copy()
        for b in basis:
            v = v - np.vdot(b, v) * b
        nv = np.linalg.norm(v)
        if nv > 1e-8:
            basis.append(v / nv)
    return basis


def run_window(C, name, W, e1, rng, starts):
    n = len(W)
    B = herm_basis(n)
    C.log(f"[{name}] window {W}; Hermitian SU(2)-invariant algebra dim = {len(B)}")
    F = [tuple([0] * len(e1)), tuple(e1)]
    Fm = {tuple(np.subtract(a, b)) for a in F for b in F}
    # translates t (t not in F-F) with W cap (W+t) nonempty
    ts = sorted({tuple(np.subtract(a, b)) for a in W for b in W} - Fm)
    C.log(f"[{name}] imposed commuting translates: {len(ts)}")
    setups = []
    for t in ts:
        Wt = [tuple(np.add(p, t)) for p in W]
        union = list(dict.fromkeys(W + Wt))
        setups.append((union, Wt, Embedder(W, union), Embedder(Wt, union)))
    dim = 2 ** n

    def build(c):
        return sum(ci * b for ci, b in zip(c, B))

    def resid(c):
        g = build(c)
        r = [(g @ g - np.eye(dim)).ravel(), np.array([np.trace(g) / dim - 0.5])]
        for union, Wt, E1, E2 in setups:
            G1 = E1(g)
            G2 = E2(g)
            r.append((G1 @ G2 - G2 @ G1).ravel() / np.sqrt(len(union)))
        r = np.concatenate(r)
        return np.concatenate([r.real, r.imag])

    # expected solutions: P on e1-bonds inside window
    expected = []
    for a in W:
        b = tuple(np.add(a, e1))
        if b in W:
            expected.append((a, b, embed(swap_op(2, 0, 1), [a, b], W)))
    C.log(f"[{name}] expected solutions: {[(a, b) for a, b, _ in expected]}")
    found = {}
    other = []
    nconv = 0
    for s in range(starts):
        c0 = rng.normal(size=len(B))
        sol = least_squares(resid, c0, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=4000)
        cost = np.linalg.norm(resid(sol.x))
        if cost > 1e-8:
            continue
        nconv += 1
        g = build(sol.x)
        match = None
        for a, b, Pab in expected:
            if np.abs(g - Pab).max() < 1e-6:
                match = (a, b)
        if match is None:
            other.append((cost, g))
        else:
            found[match] = found.get(match, 0) + 1
    C.log(f"[{name}] {starts} starts, {nconv} converged to residual < 1e-8; hits per expected bond: {found}")
    C.check(nconv > 0 and len(other) == 0,
            f"[{name}] every converged solution is a NN e1-bond swap ({len(other)} other solutions)")
    C.check(set(found) == {(a, b) for a, b, _ in expected},
            f"[{name}] each expected bond swap is found")
    # sanity: residual of the expected solutions is zero
    worst = 0.0
    for a, b, Pab in expected:
        c = np.array([np.vdot(bb, Pab).real for bb in B])
        worst = max(worst, np.linalg.norm(resid(c)))
    C.check(worst < 1e-10, f"[{name}] NN swaps satisfy all constraints (residual {worst:.1e})")
    # control: dropping commutation constraints admits other solutions (search is not trivially rigid)
    return other


def main(logname, starts=120):
    fh = open(logname, "w")
    C = Counter(fh)
    C.log("C9/03 optimisation search for alpha(P_{0,e1}) candidates; seed 11")
    rng = np.random.default_rng(11)
    run_window(C, "1D", [(0,), (1,), (2,), (3,)], (1,), rng, starts)
    run_window(C, "2D", [(0, 0), (1, 0), (0, 1), (1, 1)], (1, 0), rng, starts)
    # control: without commutation constraints, the self-adjoint-unitary + trace conditions alone
    # have many solutions (e.g. P_{02}, P_{03}); confirm P_{03} in 1D window violates commutation.
    W = [(0,), (1,), (2,), (3,)]
    P03 = embed(swap_op(2, 0, 1), [(0,), (3,)], W)
    Wt = [(3,), (4,), (5,), (6,)]
    union = list(dict.fromkeys(W + Wt))
    G1, G2 = embed(P03, W, union), embed(P03, Wt, union)
    C.check(np.abs(G1 @ G2 - G2 @ G1).max() > 0.5, "control: P_{03} fails [g, T_3 g] = 0 (constraints are active)")
    C.total()
    fh.close()


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "../logs/c9_03_search_run1.txt",
         int(sys.argv[2]) if len(sys.argv) > 2 else 120)
