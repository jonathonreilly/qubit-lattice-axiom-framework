"""C9 / 01: numerical certificates for the ingredients of the SU(2) rigidity theorem.

Theorem (proved in NOTE.md): every Z^d-translation-invariant QCA on one qubit per site that
commutes with global SU(2) is a lattice translation.  This script checks, on explicit matrices,
the finite-dimensional ingredients:

  A  Schur-Weyl: SU(2) commutant on n qubits = span of site permutations (dims 1,2,5,14,42).
  B  one-site-overlap lemma: SU(2)-invariant g on A, h on B, A cap B = {a}:
       [g,h] = 2i sum eps_{jkl} X_j Y_k sigma^l_a, X/Y = vector channels at a;
       vector channel of a nonzero invariant op spans all of C^3 (irreducibility);
       random pairs never commute; zero vector channel => commute.
  C  lex lemma: S cap (S+t) = {s1} for t = lexmax-lexmin, and [g, T_t g] != 0 for random g.
  D  2-qubit invariant algebra = span{1,P}; self-adjoint unitary with tau=1/2 => +P.
  E  geometric step: finite sets S whose ell-extremal difference is +-e1 for generic ell are
     exactly NN bonds (exhaustive in the 3x3x3 box, |S|<=4).
  F  commutation-pattern step: D+delta = D only for delta=0; NN swaps sharing a site do not commute.
  G  one-qubit vector operators = lambda*sigma; site-elimination step; NN transpositions generate
     S_8 on the unit cube graph.
"""
from __future__ import annotations

import itertools
import sys
import numpy as np

from c9_common import (Counter, PAULI, SX, SY, SZ, I2, op_on, perm_op, swap_op, all_perm_ops,
                       embed, random_su2_invariant, global_rot, random_su2, vector_channel,
                       min_support)

rng = np.random.default_rng(20261019)


def commutant_dim(n):
    """dim of {X : [X, S^j_tot] = 0, j=1..3} on n qubits, by nullspace."""
    dim = 2 ** n
    rows = []
    for s in PAULI:
        Stot = sum(op_on(n, {i: s}) for i in range(n))
        # vec([S,X]) = (I (x) S - S^T (x) I) vec X   (row-major vec)
        rows.append(np.kron(Stot, np.eye(dim)) - np.kron(np.eye(dim), Stot.T))
    M = np.vstack(rows)
    sv = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(sv < 1e-9))


def span_dim(ops):
    M = np.array([o.reshape(-1) for o in ops])
    sv = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(sv > 1e-9 * sv[0]))


def is_invariant(g, n, trials=3):
    for _ in range(trials):
        D = global_rot(n, random_su2(rng))
        if np.abs(D @ g @ D.conj().T - g).max() > 1e-9:
            return False
    return True


def main(logname):
    fh = open(logname, "w")
    C = Counter(fh)
    C.log("C9/01 lemma certificates; seed 20261019")

    # ---------------- A: Schur-Weyl
    catalan = {1: 1, 2: 2, 3: 5, 4: 14, 5: 42}  # sum of squared multiplicities, independent formula
    for n in range(1, 6):
        cd = commutant_dim(n)
        sd = span_dim(all_perm_ops(n)) if n >= 1 else 1
        C.check(cd == sd == catalan[n],
                f"A Schur-Weyl n={n}: dim commutant={cd}, dim span(perms)={sd}, expected {catalan[n]}")

    # ---------------- B: one-site-overlap lemma
    # 5 qubits: order [a, b1, b2, c1, c2]; A = {a,b1,b2}, B = {a,c1,c2}
    n = 5
    eps = np.zeros((3, 3, 3))
    for (i, j, k), s in [((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1),
                         ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)]:
        eps[i, j, k] = s
    full = ['a', 'b1', 'b2', 'c1', 'c2']
    min_comm = np.inf
    max_formula_err = 0.0
    min_rank = 3
    for trial in range(20):
        g3 = random_su2_invariant(3, rng)
        h3 = random_su2_invariant(3, rng)
        g = embed(g3, ['a', 'b1', 'b2'], full)
        h = embed(h3, ['a', 'c1', 'c2'], full)
        comm = g @ h - h @ g
        min_comm = min(min_comm, np.linalg.norm(comm) / (np.linalg.norm(g) * np.linalg.norm(h)))
        # formula check using vector channels at a (qubit 0 of the 3-site ops)
        Xg = vector_channel(g3, 3, 0)  # ops on [b1,b2]
        Yh = vector_channel(h3, 3, 0)  # ops on [c1,c2]
        pred = np.zeros_like(comm)
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    if eps[j, k, l] != 0:
                        # X_j on b1b2, Y_k on c1c2, sigma^l on a; full order [a,b1,b2,c1,c2]
                        term = np.kron(PAULI[l], np.kron(Xg[j + 1], Yh[k + 1]))
                        pred += 2j * eps[j, k, l] * term
        max_formula_err = max(max_formula_err, np.abs(pred - comm).max())
        # irreducibility: span of (phi(X_1),phi(X_2),phi(X_3)) over functionals = rank of 3 x d^2
        M = np.array([Xg[j + 1].reshape(-1) for j in range(3)])
        min_rank = min(min_rank, np.linalg.matrix_rank(M, tol=1e-9))
    C.check(min_comm > 1e-3, f"B 20 random invariant pairs overlapping in one site never commute "
                             f"(min relative ||[g,h]|| = {min_comm:.3e})")
    C.check(max_formula_err < 1e-10, f"B commutator = 2i eps X_j Y_k sigma^l (max err {max_formula_err:.1e})")
    C.check(min_rank == 3, f"B vector channel of random invariant op spans C^3 (min rank {min_rank})")
    # zero vector channel at a => commute
    X0 = random_su2_invariant(2, rng)
    g = embed(np.kron(I2, X0), ['a', 'b1', 'b2'], full)
    h = embed(random_su2_invariant(3, rng), ['a', 'c1', 'c2'], full)
    C.check(np.abs(g @ h - h @ g).max() < 1e-10, "B zero vector channel at the shared site => commute")
    # vector channel transforms as a vector (rotation covariance), checked for one random g
    g3 = random_su2_invariant(3, rng)
    U = random_su2(rng)
    R = np.array([[0.5 * np.trace(PAULI[k] @ U @ PAULI[j] @ U.conj().T).real for j in range(3)]
                  for k in range(3)])  # Ad(U) sigma^j = sum_k R_kj sigma^k
    X = vector_channel(g3, 3, 0)
    D2 = global_rot(2, U)
    err = max(np.abs(D2 @ X[j + 1] @ D2.conj().T - sum(R[k, j] * X[k + 1] for k in range(3))).max()
              for j in range(3))
    # invariance: g = sum_j X_j (x) s^j = sum_j D X_j D^+ (x) U s^j U^+ ; this gives D X_j D^+ = sum_k R_jk X_k
    err2 = max(np.abs(D2 @ X[j + 1] @ D2.conj().T - sum(R[j, k] * X[k + 1] for k in range(3))).max()
               for j in range(3))
    C.check(min(err, err2) < 1e-10 and np.abs(D2 @ X[0] @ D2.conj().T - X[0]).max() < 1e-10,
            f"B vector channel is a vector operator, X_0 invariant (err {min(err, err2):.1e})")

    # ---------------- C: lex lemma on random supports in Z^3
    box = list(itertools.product(range(3), repeat=3))
    nC = 0
    okC = True
    worst = np.inf
    for size in (2, 3, 4):
        for trial in range(8):
            idx = rng.choice(len(box), size=size, replace=False)
            S = [box[i] for i in idx]
            ell = rng.normal(size=3)
            key = lambda p: float(np.dot(ell, p))
            s1 = max(S, key=key)
            s2 = min(S, key=key)
            t = tuple(np.subtract(s1, s2))
            St = [tuple(np.add(p, t)) for p in S]
            inter = set(S) & set(St)
            if inter != {s1}:
                okC = False
            union = list(dict.fromkeys(S + St))
            g = random_su2_invariant(size, rng)
            if sorted(min_support(g, size)) != list(range(size)):
                okC = False
            G1 = embed(g, S, union)
            G2 = embed(g, St, union)  # translate: same matrix on translated sites
            rel = np.linalg.norm(G1 @ G2 - G2 @ G1) / np.linalg.norm(G1) ** 2
            worst = min(worst, rel)
            nC += 1
    C.check(okC, f"C {nC} random supports (|S|=2,3,4), generic ell: S cap (S+t) = {{s1}} and random g has full support")
    C.check(worst > 1e-3, f"C [g, T_t g] != 0 in all {nC} cases (min relative norm {worst:.3e})")

    # ---------------- D: two qubits
    P = swap_op(2, 0, 1)
    C.check(commutant_dim(2) == 2 and span_dim([np.eye(4), P]) == 2, "D 2-qubit SU(2) commutant = span{1,P}")
    # a+bP self-adjoint unitary, non-scalar, normalized trace 1/2: eigen a+b (x3), a-b (x1)
    sols = []
    for ab in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        lt, ls = ab  # triplet eigenvalue, singlet eigenvalue
        if lt == ls:
            continue
        a, b = (lt + ls) / 2, (lt - ls) / 2
        tr = (3 * lt + ls) / 4
        if abs(tr - 0.5) < 1e-12:
            sols.append((a, b))
    C.check(sols == [(0.0, 1.0)], f"D self-adjoint unitary non-scalar a+bP with tau=1/2: {sols} (= +P only)")
    C.check(abs(np.trace(P).real / 4 - 0.5) < 1e-12, "D tau(P) = 1/2")

    # ---------------- E: geometric step, exhaustive in 3x3x3 box
    ells = [rng.normal(size=3) for _ in range(40)]
    e1 = np.array([1, 0, 0])
    found = {2: 0, 3: 0, 4: 0}
    bad = 0
    for size in (2, 3, 4):
        for S in itertools.combinations(box, size):
            okS = True
            for ell in ells:
                vals = [np.dot(ell, p) for p in S]
                d = np.subtract(S[int(np.argmax(vals))], S[int(np.argmin(vals))])
                if not (np.array_equal(d, e1) or np.array_equal(d, -e1)):
                    okS = False
                    break
            if okS:
                found[size] += 1
                if not (size == 2 and np.array_equal(np.abs(np.subtract(S[0], S[1])), e1)):
                    bad += 1
    C.check(found == {2: 18, 3: 0, 4: 0} and bad == 0,
            f"E sets S in 3^3 box (|S|<=4) with extremal difference +-e1 for 40 generic ell: {found} (expected 18 NN x-bonds only)")

    # ---------------- F: commutation pattern
    e = [np.array(v) for v in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]]
    okF = True
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        Dset = {tuple(v) for v in [0 * e[i], e[i], -e[j], e[i] - e[j]]}
        for delta in itertools.product(range(-3, 4), repeat=3):
            sh = {tuple(np.add(v, delta)) for v in Dset}
            if (sh == Dset) != (delta == (0, 0, 0)):
                okF = False
    C.check(okF, "F D_ij + delta = D_ij only for delta = 0 (all axis pairs, |delta|_inf <= 3)")
    S01 = swap_op(3, 0, 1)
    S12 = swap_op(3, 1, 2)
    C.check(np.abs(S01 @ S12 - S12 @ S01).max() > 0.5, "F swaps on bonds sharing one site do not commute")
    # direct check: shared-site pattern of shifted bond families equals original iff c1 = c2
    okF2 = True
    def share(b1, b2):
        return len(set(b1) & set(b2)) == 1
    for c1 in itertools.product(range(-1, 2), repeat=3):
        for c2 in itertools.product(range(-1, 2), repeat=3):
            same = True
            for y in itertools.product(range(-2, 3), repeat=3):
                orig = share([(0, 0, 0), (1, 0, 0)], [y, tuple(np.add(y, (0, 1, 0)))])
                b1 = [tuple(c1), tuple(np.add(c1, (1, 0, 0)))]
                b2 = [tuple(np.add(y, c2)), tuple(np.add(np.add(y, c2), (0, 1, 0)))]
                if share(b1, b2) != orig:
                    same = False
                    break
            if same != (c1 == c2):
                okF2 = False
    C.check(okF2, "F image bond families reproduce the x/y overlap pattern iff c_x = c_y (729 pairs)")

    # ---------------- G: final step
    # one-qubit vector operators: W^j = alpha'(sigma^j) must satisfy Ad(D) W^j = sum_k R_{kj} W^k,
    # because Ad(D) sigma^j = sum_k R_{kj} sigma^k and alpha' commutes with Ad(D^{(x)}).
    # solve linear system for M (3x4 complex) over a few random rotations
    basis = [I2, SX, SY, SZ]
    rows = []
    for _ in range(4):
        U = random_su2(rng)
        R = np.array([[0.5 * np.trace(PAULI[k] @ U @ PAULI[j] @ U.conj().T).real for j in range(3)]
                      for k in range(3)])
        # Ad(U) s^mu = sum_nu A_{nu mu} s^nu
        A = np.array([[0.5 * np.trace(basis[nu] @ U @ basis[mu] @ U.conj().T) for mu in range(4)]
                      for nu in range(4)])
        # condition: sum_mu M_{j mu} A_{nu mu} = sum_k R_{kj} M_{k nu}  for all j,nu
        # unknown vec(M) index (j,mu) -> 4j+mu
        for j in range(3):
            for nu in range(4):
                row = np.zeros(12, dtype=complex)
                for mu in range(4):
                    row[4 * j + mu] += A[nu, mu]
                for k in range(3):
                    row[4 * k + nu] -= R[k, j]
                rows.append(row)
    M = np.array(rows)
    sv = np.linalg.svd(M, compute_uv=False)
    null = int(np.sum(sv < 1e-9))
    _, _, vh = np.linalg.svd(M)
    v = vh[-1].reshape(3, 4)
    v = v / v[0, 1]
    target = np.array([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    C.check(null == 1 and np.abs(v - target).max() < 1e-9,
            f"G one-qubit vector operators form a 1-dim space spanned by sigma (nullity {null})")
    # site elimination: W vector op on [0,y] with genuine y-dependence fails [W, P_{yz}] = 0, z fresh
    worstG = np.inf
    for _ in range(10):
        c = rng.normal(size=3) + 1j * rng.normal(size=3)
        W = []
        for j in range(3):
            cross = sum(eps[j, k, l] * np.kron(PAULI[k], PAULI[l]) for k in range(3) for l in range(3))
            W.append(c[0] * np.kron(PAULI[j], I2) + c[1] * np.kron(I2, PAULI[j]) + c[2] * cross)
        Pyz = embed(swap_op(2, 0, 1), ['y', 'z'], ['0', 'y', 'z'])
        for j in range(3):
            Wj = embed(W[j], ['0', 'y'], ['0', 'y', 'z'])
            worstG = min(worstG, np.linalg.norm(Wj @ Pyz - Pyz @ Wj))
    C.check(worstG > 1e-3, f"G vector ops with y-dependence never commute with P_yz (z outside support), min {worstG:.2e}")
    # NN transpositions generate S_8 on the unit cube graph
    cube = list(itertools.product(range(2), repeat=3))
    edges = [(a, b) for a in range(8) for b in range(a + 1, 8)
             if sum(abs(x - y) for x, y in zip(cube[a], cube[b])) == 1]
    gens = []
    for a, b in edges:
        p = list(range(8))
        p[a], p[b] = b, a
        gens.append(tuple(p))
    seen = {tuple(range(8))}
    frontier = [tuple(range(8))]
    while frontier:
        nf = []
        for p in frontier:
            for gg in gens:
                q = tuple(gg[p[i]] for i in range(8))
                if q not in seen:
                    seen.add(q)
                    nf.append(q)
        frontier = nf
    C.check(len(seen) == 40320, f"G 12 NN transpositions of the unit cube generate |S_8| = {len(seen)}")

    C.total()
    fh.close()


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "../logs/c9_01_lemmas_run1.txt")
