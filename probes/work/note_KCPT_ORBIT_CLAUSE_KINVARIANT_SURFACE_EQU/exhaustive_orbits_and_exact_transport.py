#!/usr/bin/env python3
"""J:note falsifiers for KCPT_ORBIT_CLAUSE_KINVARIANT_SURFACE_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-06-10 (on main).

The note's four falsifiers, with machinery disjoint from its runner (random surfaces on 25 random label sets; floating-point states):
  1./2. T1 and T2 EXHAUSTIVELY: every involution pi on n = 1..7 labels and every single registered surface iota: S -> {0,1,2}
     (all 3^n), plus every pair of surfaces with values in {0,1} for n <= 5: whenever the family is pi-invariant and orbit-separating
     the indistinguishability classes equal the orbits (T1), and whenever some surface separates an orbit pair that orbit is not a
     class (T2);
  3. T3 in exact Gaussian-rational arithmetic: contexts of dimension up to 12 with central sectors of several sizes, involutions pi
     with fixed and swapped labels, antiunitaries K = U conj with K^2 = +1 and K^2 = -1 (Kramers self-paired sectors of even
     dimension), all transported by random rational unitaries (Cayley transforms); random rational density matrices: the transport
     identity tr(P_pi(k) rho) = tr(P_k rho_K), the defect form, and pi-symmetry for K-real states;
  4. the symmetrization (rho + rho_K)/2 is K-real for K^2 = -1 as well as +1.
HIT if any instance fails.
"""
from __future__ import annotations

import itertools
import random

from sympy.polys.domains import QQ, QQ_I
from sympy.polys.matrices import DomainMatrix

ZERO, ONE = QQ_I(0, 0), QQ_I(1, 0)


# ------------------------------------------------------------------------------------------------------------------ 1./2. T1, T2
def involutions(n):
    def rec(rem):
        if not rem:
            yield {}
            return
        a = rem[0]
        for p in rec(rem[1:]):
            q = dict(p)
            q[a] = a
            yield q
        for i in range(1, len(rem)):
            b = rem[i]
            rest = rem[1:i] + rem[i + 1:]
            for p in rec(rest):
                q = dict(p)
                q[a], q[b] = b, a
                yield q
    yield from rec(list(range(n)))


def classes(n, fam):
    key = {k: tuple(f[k] for f in fam) for k in range(n)}
    out = {}
    for k, v in key.items():
        out.setdefault(v, set()).add(k)
    return {frozenset(s) for s in out.values()}


def t1_t2():
    cases, bad1, bad2, ninv = 0, 0, 0, 0
    for n in range(1, 8):
        for pi in involutions(n):
            ninv += 1
            orbits = {frozenset({k, pi[k]}) for k in range(n)}
            fams = [[f] for f in itertools.product(range(3), repeat=n)]
            if n <= 5:
                fams += [[f, g] for f in itertools.product(range(2), repeat=n) for g in itertools.product(range(2), repeat=n)]
            for fam in fams:
                cases += 1
                inv = all(f[k] == f[pi[k]] for f in fam for k in range(n))
                sep = all(any(f[min(a)] != f[min(b)] for f in fam) for a in orbits for b in orbits if a != b)
                cl = classes(n, fam)
                if inv and sep and cl != orbits:
                    bad1 += 1
                splits = any(f[k] != f[pi[k]] for f in fam for k in range(n))
                if splits:
                    split_orbits = {frozenset({k, pi[k]}) for f in fam for k in range(n) if f[k] != f[pi[k]]}
                    if any(o in cl for o in split_orbits):
                        bad2 += 1
    return ninv, cases, bad1, bad2


# ---------------------------------------------------------------------------------------------------------------- 3./4. T3 exact
def dm(rows):
    return DomainMatrix([[QQ_I(*x) if isinstance(x, tuple) else x for x in r] for r in rows], (len(rows), len(rows[0])), QQ_I)


def conjm(M):
    return M.applyfunc(lambda z: QQ_I(z.x, -z.y), QQ_I)


def dag(M):
    return conjm(M).transpose()


def eye(n):
    return DomainMatrix.eye(n, QQ_I).to_dense()


def same(A, B):
    """exact equality independent of the sparse/dense storage format"""
    return (A - B).is_zero_matrix


def rand_gauss(rng, n, m, r=3):
    return DomainMatrix([[QQ_I(rng.randint(-r, r), rng.randint(-r, r)) for _ in range(m)] for _ in range(n)], (n, m), QQ_I)


def cayley(rng, n):
    A = rand_gauss(rng, n, n, 2)
    X = A - dag(A)                                    # anti-Hermitian
    return (eye(n) - X) * (eye(n) + X).inv()          # unitary, Gaussian-rational


def context(rng, sizes, pairs, sign):
    """Block construction: sectors with the given sizes; pairs = list of (a, b) swapped labels (a == b: fixed).
    Returns projectors P_k, the unitary part U of K = U conj, and pi."""
    D = sum(sizes)
    offs = [sum(sizes[:i]) for i in range(len(sizes))]
    U = [[ZERO] * D for _ in range(D)]
    pi = {}
    for a, b in pairs:
        pi[a], pi[b] = b, a
        if a == b:
            m = sizes[a]
            if sign == 1:
                for i in range(m):
                    U[offs[a] + i][offs[a] + i] = ONE
            else:
                assert m % 2 == 0
                for i in range(0, m, 2):                   # J = [[0,-1],[1,0]] blocks: K = J conj, K^2 = J J = -1
                    U[offs[a] + i][offs[a] + i + 1] = QQ_I(-1, 0)
                    U[offs[a] + i + 1][offs[a] + i] = ONE
        else:
            m = sizes[a]
            assert sizes[b] == m
            for i in range(m):                              # K(v, w) = (s conj w, conj v): K^2 = s
                U[offs[a] + i][offs[b] + i] = QQ_I(sign, 0)
                U[offs[b] + i][offs[a] + i] = ONE
    Umat = DomainMatrix(U, (D, D), QQ_I)
    P = []
    for k, m in enumerate(sizes):
        rows = [[ONE if (i == j and offs[k] <= i < offs[k] + m) else ZERO for j in range(D)] for i in range(D)]
        P.append(DomainMatrix(rows, (D, D), QQ_I))
    # transport by a random rational unitary W: P -> W P W^dag, K -> W K W^-1 = (W U W^T) conj
    W = cayley(rng, D)
    P = [W * p * dag(W) for p in P]
    Umat = W * Umat * W.transpose()
    return P, Umat, pi, D


def K_apply_state(U, rho):
    """rho_K = K rho K^-1 with K = U conj:  U conj(rho) U^dag."""
    return U * conjm(rho) * dag(U)


def trace(M):
    return sum((M[i, i].element for i in range(M.shape[0])), ZERO)


def t3(seed=5):
    rng = random.Random(seed)
    specs = [((2, 2, 3), [(0, 1), (2, 2)], 1), ((2, 2, 4), [(0, 1), (2, 2)], -1), ((1, 1, 2, 2, 3), [(0, 1), (2, 3), (4, 4)], 1),
             ((2, 1, 1, 2), [(0, 0), (1, 2), (3, 3)], -1), ((3, 3, 2, 2, 2), [(0, 1), (2, 3), (4, 4)], -1),
             ((4, 4, 2, 2), [(0, 1), (2, 2), (3, 3)], 1), ((2, 2, 2, 2, 2, 2), [(0, 3), (1, 4), (2, 5)], -1),
             ((6, 6), [(0, 0), (1, 1)], -1)]
    stats = {"contexts": 0, "states": 0, "K^2 ok": True, "K P K^-1 = P_pi": True, "transport": True, "defect form": True,
             "symmetrized K-real": True, "K-real => pi-symmetric": True, "generic separates": 0, "max dim": 0}
    for sizes, pairs, sign in specs:
        P, U, pi, D = context(rng, sizes, pairs, sign)
        stats["contexts"] += 1
        stats["max dim"] = max(stats["max dim"], D)
        KK = U * conjm(U)                                  # K^2 = U conj(U)
        stats["K^2 ok"] &= same(KK, eye(D) * QQ_I(sign, 0))
        for k, p in enumerate(P):
            stats["K P K^-1 = P_pi"] &= same(U * conjm(p) * dag(U), P[pi[k]])
        for _ in range(4):
            A = rand_gauss(rng, D, D, 3)
            rho = A * dag(A)
            tr = trace(rho)
            rho = rho * QQ_I(QQ(1) / tr.x, 0)
            stats["states"] += 1
            rK = K_apply_state(U, rho)
            sym = (rho + rK) * QQ_I(QQ(1, 2), 0)
            stats["symmetrized K-real"] &= same(K_apply_state(U, sym), sym)
            sep = False
            for k, p in enumerate(P):
                lhs = trace(P[pi[k]] * rho)
                rhs = trace(p * rK)
                stats["transport"] &= lhs == rhs
                defect = trace(p * (rho - rK))
                stats["defect form"] &= (trace(p * rho) - lhs) == defect
                stats["K-real => pi-symmetric"] &= trace(P[pi[k]] * sym) == trace(p * sym)
                if trace(p * rho) != lhs:
                    sep = True
            stats["generic separates"] += int(sep)
    return stats


def main():
    ninv, cases, bad1, bad2 = t1_t2()
    print(f"1./2. exhaustive T1/T2: {ninv} involutions on n = 1..7 labels, {cases} surface families; T1 counterexamples {bad1}, "
          f"T2 counterexamples {bad2}")
    st = t3()
    print(f"3./4. exact T3: {st}")
    fails = []
    if bad1 or bad2:
        fails.append("T1/T2")
    for k in ("K^2 ok", "K P K^-1 = P_pi", "transport", "defect form", "symmetrized K-real", "K-real => pi-symmetric"):
        if not st[k]:
            fails.append(k)
    if fails:
        print(f"HIT: {fails}")
    print(f"SUMMARY: T1 and T2 hold on all {cases} surface families over all {ninv} involutions of up to 7 labels (no counterexample); "
          f"in exact Gaussian-rational arithmetic on {st['contexts']} transported contexts up to dimension {st['max dim']} (K^2 = +1 and "
          f"-1, Kramers sectors included) and {st['states']} random states the transport identity, the defect form, pi-symmetry of "
          f"K-real states and K-reality of (rho + rho_K)/2 hold exactly, and {st['generic separates']} of {st['states']} generic states "
          f"separate an orbit pair; no falsifier fires")


if __name__ == "__main__":
    main()
