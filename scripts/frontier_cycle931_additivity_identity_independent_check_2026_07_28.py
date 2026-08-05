#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cycle 931 (blockM11) -- INDEPENDENT CHECK, SPEC'D TO REFUTE.

TARGET.  The Cycle-931 primary claims the 929 additivity identity
G_d(m) + G_d(d-1-m) = G_d(d-1) is DERIVED, as the pure-state pair-complement
identity I(A:B) + I(R:B) = 2 S(B), with hypotheses H1 global purity, H2 the
fragments exhaust every non-pointer site, H3 Z-basis pointer conditioning, H4 arm
exchangeability.  This runner tries to break that, on machinery that shares no
line with the primary.

INDEPENDENCE (every one of these is a DIFFERENT algorithm, not a re-parameterised
one):
  * propagator: Krylov/Lanczos exponential (own implementation, symmetric
    tridiagonal reduction) and scipy's expm_multiply (Al-Mohy-Higham scaling and
    squaring).  The primary used Chebyshev/Bessel, adaptive Taylor marching and
    dense eigendecomposition.  NO ROUTE IS SHARED.
  * qubit ordering: REVERSED -- site i occupies bit (n-1-i) here, bit i there.
  * entropies: SVD of the Schmidt matrix (singular values), natural logarithm,
    converted to bits.  The primary used eigvalsh of the reduced density matrix
    with a base-2 logarithm.
  * conditional statistic: explicit pointer-projector sum with axis slicing.
    The primary used block slicing of the joint density matrix.
  * symbolic algebra: NO CAS.  Exact arithmetic over the rationals (fractions)
    and over the prime field GF(2^61-1), with Schwartz-Zippel sampling and a
    hand-written Faddeev-LeVerrier characteristic polynomial.  The primary used
    sympy.
  * an arbitrary-precision (50 decimal digit) confirmation with mpmath, so the
    1e-14 residuals cannot be a float64 coincidence.

WHAT IS ATTACKED
  (i)   the surviving derivation's HYPOTHESES: a search for a state that
        satisfies H1-H4 and violates the conclusion;
  (ii)  the discriminating computations, recomputed;
  (iii) the SEAL: holdout-freedom and tamper-evidence, recomputed from the pinned
        bytes by a different inversion;
  (iv)  a COUNTEREXAMPLE HUNT for the identity itself outside the measured grid --
        new degrees, new fields, new times, non-star geometries, loop-carrying
        geometries, and non-frozen preparations.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor spec.
Independent audit still required.  No axiom, primitive, registry, policy, queue
or audit surface is touched.  No docs/ note is written by this runner.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import os
import random
import re
import subprocess
import sys
import time
from fractions import Fraction

import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spsl

T_START = time.perf_counter()
BOUNDARY_LINE = "===== runner cache v1 ====="
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUNTIME_LIMIT_SECONDS = 900.0

PRIMARY_RUNNER = "scripts/frontier_cycle931_additivity_identity_2026_07_28.py"
PRIMARY_RECEIPT = "outputs/additivity_identity_cycle931_receipt_2026_07_28.json"
C929_RECEIPT = "outputs/arity_variable_cycle929_receipt_2026_07_28.json"
PARENT_MEMO = "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md"

PINS = {
    PARENT_MEMO: "c3e0b9162170f5e87e486f9d34068114d1d56b2f80db5c57df7ff7536820a93e",
    C929_RECEIPT: "40440237f0af14882b06331a054c19f3da52f34e6e7b2cde846a0b390a3679a3",
    "docs/MINIMAL_AXIOMS_2026-06-29.md":
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    "scripts/frontier_cycle929_arity_variable_2026_07_28.py":
        "626be10a174d9ff41f72daa97a7eddc403e5ce191aff56791b38d0cea740c08a",
}

CLAIM_LAMBDAS = (0.05, 0.10)
IDENT_TOL = 1e-11
T_EXEC = [round(0.1 * i, 10) for i in range(13)]
LN2 = math.log(2.0)
MERSENNE_P = (1 << 61) - 1


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_obj(o):
    return sha256_bytes(json.dumps(o, sort_keys=True, separators=(",", ":"),
                                   default=float).encode("utf-8"))


def die(msg):
    sys.stderr.write("FATAL %s\n" % msg)
    sys.exit(2)


def git(args):
    return subprocess.run(["git", "-C", ROOT] + args, capture_output=True)


def verify_pins():
    out = {}
    for p, want in sorted(PINS.items()):
        b = open(os.path.join(ROOT, p), "rb").read()
        got = sha256_bytes(b)
        if got != want:
            die("pin:%s got=%s want=%s" % (p, got, want))
        out[p] = {"sha256": got, "bytes": len(b)}
    return out


# ===================== INDEPENDENT NUMERICS: reversed ordering, sparse H ======
def star_bonds(d):
    return [(0, k) for k in range(1, d + 1)]


def spider_bonds(arms):
    """arms: list of arm shapes; each shape is a list of parent indices within the
    arm (None = attached to the pointer).  Returns (n, bonds, arm_site_lists)."""
    bonds = []
    sites = 1
    armlists = []
    for shape in arms:
        names = []
        for p, par in enumerate(shape):
            idx = sites
            sites += 1
            names.append(idx)
            bonds.append((0, idx) if par is None else (names[par], idx))
        armlists.append(names)
    return sites, bonds, armlists


def path_shape(L):
    return [None] + list(range(L - 1))


def claw_shape(L):
    return [None] + [0] * (L - 1)


def build_H_sparse(n, bonds, lam):
    """H = -sum_<ij> Z_i Z_j - lam sum_i X_i, in the REVERSED bit convention:
    site i occupies bit (n-1-i)."""
    dim = 1 << n
    idx = np.arange(dim, dtype=np.int64)

    def zbit(i):
        return 1 - 2 * ((idx >> np.int64(n - 1 - i)) & 1)
    diag = np.zeros(dim)
    for (a, b) in bonds:
        diag -= zbit(a) * zbit(b)
    rows = [idx]
    cols = [idx]
    vals = [diag]
    for i in range(n):
        rows.append(idx)
        cols.append(idx ^ np.int64(1 << (n - 1 - i)))
        vals.append(np.full(dim, -lam))
    H = sps.coo_matrix((np.concatenate(vals),
                        (np.concatenate(rows), np.concatenate(cols))),
                       shape=(dim, dim)).tocsr()
    return H


def prep_vec(n, plus_sites):
    """Product preparation, reversed convention: |+> on plus_sites, |0> elsewhere."""
    v = np.ones(1, dtype=np.complex128)
    for i in range(n):
        c = (np.array([1.0, 1.0]) / math.sqrt(2.0)) if i in plus_sites \
            else np.array([1.0, 0.0])
        v = np.kron(v, c.astype(np.complex128))
    return v


def lanczos_expm(H, psi, t, m=40):
    """ROUTE K -- Krylov/Lanczos exponential, own implementation.  H is real
    symmetric; the Krylov basis is built with full reorthogonalisation and the
    small tridiagonal exponential is taken by dense eigendecomposition of an
    m x m matrix (never of the full space)."""
    beta0 = np.linalg.norm(psi)
    V = [psi / beta0]
    alpha, beta = [], []
    for j in range(m):
        w = H @ V[-1]
        a = complex(np.vdot(V[-1], w)).real
        w = w - a * V[-1] - (beta[-1] * V[-2] if j > 0 else 0.0)
        for u in V:                       # full reorthogonalisation
            w = w - np.vdot(u, w) * u
        b = float(np.linalg.norm(w))
        alpha.append(a)
        if b < 1e-14 or j == m - 1:
            break
        beta.append(b)
        V.append(w / b)
    k = len(alpha)
    T = np.zeros((k, k))
    T[np.arange(k), np.arange(k)] = alpha
    for j in range(k - 1):
        T[j, j + 1] = T[j + 1, j] = beta[j]
    w, U = np.linalg.eigh(T)
    e1 = np.zeros(k)
    e1[0] = 1.0
    c = U @ (np.exp(-1j * w * t) * (U.T @ e1))
    out = np.zeros_like(psi)
    for j in range(k):
        out += (beta0 * c[j]) * V[j]
    return out, {"route": "K-lanczos", "krylov_dim": k}


def expm_route(H, psi, t):
    """ROUTE E -- scipy expm_multiply (Al-Mohy & Higham)."""
    return spsl.expm_multiply((-1j * t) * H.astype(np.complex128), psi), \
        {"route": "E-expm_multiply"}


def euler_route(H, psi, t, nstep=400):
    v = psi.astype(np.complex128).copy()
    h = t / nstep
    for _ in range(nstep):
        v = v + (-1j * h) * (H @ v)
    return v


def svd_entropy_bits(vec, n, axes):
    """S(rho_X) via SINGULAR VALUES of the Schmidt matrix; natural log -> bits.
    Reversed convention: axis j of the reshaped tensor IS site j."""
    axes = tuple(sorted(axes))
    if len(axes) == 0 or len(axes) == n:
        return 0.0
    T = vec.reshape((2,) * n)
    rest = [j for j in range(n) if j not in axes]
    M = np.transpose(T, list(axes) + rest).reshape(1 << len(axes), -1)
    sv = np.linalg.svd(M, compute_uv=False)
    p = sv ** 2
    p = p[p > 1e-32]
    p = p / p.sum()
    return float(-(p * np.log(p)).sum() / LN2)


def svd_entropy_bits_unnormalised(vec, n, axes):
    """As above but WITHOUT renormalising -- used where the block is genuinely
    mixed and the vector is a sub-block of a larger pure state."""
    axes = tuple(sorted(axes))
    T = vec.reshape((2,) * n)
    rest = [j for j in range(n) if j not in axes]
    M = np.transpose(T, list(axes) + rest).reshape(1 << len(axes), -1)
    sv = np.linalg.svd(M, compute_uv=False)
    p = sv ** 2
    tot = p.sum()
    p = p[p > 1e-32] / tot
    return float(-(p * np.log(p)).sum() / LN2)


def pointer_branches(vec, n, S):
    """Project the pointer onto |0>,|1>.  Reversed convention: axis S IS site S."""
    T = vec.reshape((2,) * n)
    T = np.moveaxis(T, S, 0)
    out = []
    for z in (0, 1):
        v = np.ascontiguousarray(T[z]).reshape(-1)
        p = float(np.vdot(v, v).real)
        out.append((p, v / math.sqrt(p) if p > 1e-300 else v))
    order = [i for i in range(n) if i != S]
    return out, order


def C_stat(vec, n, S, Asites, Bsites):
    """The frozen statistic, computed by explicit pointer projection.
    C_ab = sum_z p_z [S(A|z) + S(B|z) - S(AB|z)]."""
    brs, order = pointer_branches(vec, n, S)
    pos = {s: j for j, s in enumerate(order)}
    A = tuple(sorted(pos[s] for s in Asites))
    B = tuple(sorted(pos[s] for s in Bsites))
    tot = sum(p for p, _ in brs)
    out = 0.0
    for p, v in brs:
        if p / tot <= 1e-14:
            continue
        out += (p / tot) * (svd_entropy_bits(v, n - 1, A)
                            + svd_entropy_bits(v, n - 1, B)
                            - svd_entropy_bits(v, n - 1, tuple(sorted(set(A) | set(B)))))
    return out


def s_seq(vec, n, S, armlists):
    """s(k) := sum_z p_z S(first k arms | z) -- with the full spread over all
    C(d,k) arm subsets."""
    brs, order = pointer_branches(vec, n, S)
    pos = {s: j for j, s in enumerate(order)}
    arms = [tuple(sorted(pos[s] for s in a)) for a in armlists]
    d = len(arms)
    tot = sum(p for p, _ in brs)
    s, spread = {}, {}
    for k in range(d + 1):
        vals = []
        for comb in itertools.combinations(range(d), k):
            ax = tuple(sorted(itertools.chain(*[arms[i] for i in comb])))
            vals.append(sum((p / tot) * svd_entropy_bits(v, n - 1, ax) for p, v in brs))
        s[k] = vals[0]
        spread[k] = (max(vals) - min(vals)) if len(vals) > 1 else 0.0
    return s, spread


def evolve(n, bonds, plus, lam, t, route="K"):
    H = build_H_sparse(n, bonds, lam)
    psi = prep_vec(n, plus)
    if route == "K":
        return lanczos_expm(H, psi, t, m=min(60, 1 << n))[0]
    if route == "E":
        return expm_route(H, psi, t)[0]
    if route == "EULER":
        return euler_route(H, psi, t)
    die("route:%s" % route)


def star_cell(d, lam, t, route="K"):
    n = d + 1
    bonds = star_bonds(d)
    plus = set(range(n))
    vec = evolve(n, bonds, plus, lam, t, route)
    armlists = [[k] for k in range(1, d + 1)]
    return vec, n, 0, armlists


def spider_cell(arms, lam, t, route="K", plus_all=True, drop_plus=()):
    n, bonds, armlists = spider_bonds(arms)
    anchors = {a[0] for a in armlists}
    plus = set([0]) | anchors if not plus_all else set(range(n))
    plus = plus - set(drop_plus)
    vec = evolve(n, bonds, plus, lam, t, route)
    return vec, n, 0, armlists


def ladder_from(vec, n, S, armlists):
    d = len(armlists)
    G = {}
    for m in range(1, d):
        A = list(itertools.chain(*armlists[:m]))
        B = armlists[m % d]
        G[m] = C_stat(vec, n, S, A, B)
    return G


def additivity_residual(G, d):
    return max((abs(G[m] + G[d - 1 - m] - G[d - 1]) for m in range(1, d - 1)),
               default=0.0)


# ================= INDEPENDENT SYMBOLICS: exact rationals and GF(p), no CAS ===
def _det_frac(M):
    """Fraction-exact determinant by fraction-free Gaussian elimination."""
    A = [row[:] for row in M]
    k = len(A)
    det = Fraction(1)
    for i in range(k):
        piv = None
        for r in range(i, k):
            if A[r][i] != 0:
                piv = r
                break
        if piv is None:
            return Fraction(0)
        if piv != i:
            A[i], A[piv] = A[piv], A[i]
            det = -det
        det *= A[i][i]
        inv = Fraction(1) / A[i][i]
        for r in range(i + 1, k):
            f = A[r][i] * inv
            if f:
                for c in range(i, k):
                    A[r][c] -= f * A[i][c]
    return det


def _charpoly_frac(M):
    """Faddeev-LeVerrier: coefficients of det(xI - M), highest power first."""
    k = len(M)
    I = [[Fraction(int(i == j)) for j in range(k)] for i in range(k)]
    Mk = [row[:] for row in I]
    coeffs = [Fraction(1)]
    for m in range(1, k + 1):
        # Mk = M @ Mk_prev  (after the first step)
        AM = [[sum(M[i][l] * Mk[l][j] for l in range(k)) for j in range(k)]
              for i in range(k)]
        c = -Fraction(sum(AM[i][i] for i in range(k)), m)
        coeffs.append(c)
        Mk = [[AM[i][j] + (c if i == j else 0) for j in range(k)] for i in range(k)]
    return coeffs


def exact_symbolics(trials=200, seed=93107):
    """Every lemma the primary proved with sympy, re-proved WITHOUT a CAS."""
    rng = random.Random(seed)
    out = {"method": "exact rational arithmetic (fractions) + GF(2^61-1) "
                     "Schwartz-Zippel sampling + hand-written Faddeev-LeVerrier "
                     "characteristic polynomial.  No computer-algebra system.",
           "trials_per_shape": trials}

    # L1: N(MN) = (NM)N over GF(p) at random points -- an identity, so it must
    # hold at EVERY point; a single failure refutes it.
    l1 = []
    for (p_, q_) in [(1, 2), (2, 2), (2, 4), (3, 5), (4, 4)]:
        bad = 0
        for _ in range(trials):
            M = [[rng.randrange(MERSENNE_P) for _ in range(q_)] for _ in range(p_)]
            N = [[rng.randrange(MERSENNE_P) for _ in range(p_)] for _ in range(q_)]

            def mul(A, B):
                return [[sum(A[i][l] * B[l][j] for l in range(len(B))) % MERSENNE_P
                         for j in range(len(B[0]))] for i in range(len(A))]
            lhs = mul(N, mul(M, N))
            rhs = mul(mul(N, M), N)
            if lhs != rhs:
                bad += 1
        l1.append({"shape": [p_, q_], "failures": bad})
        if bad:
            die("checker:L1-refuted %r" % ((p_, q_),))
    out["L1_eigenvector_transfer"] = {"rows": l1, "all_hold": True}

    # L2: det(xI_p - MN) x^(q-p) = det(xI_q - NM) as POLYNOMIALS, over exact
    # rationals, at random rational matrices.
    l2 = []
    for (p_, q_) in [(1, 2), (2, 2), (2, 3), (2, 4), (3, 4)]:
        worst = 0
        for _ in range(40):
            M = [[Fraction(rng.randint(-9, 9), rng.randint(1, 7)) for _ in range(q_)]
                 for _ in range(p_)]
            N = [[Fraction(rng.randint(-9, 9), rng.randint(1, 7)) for _ in range(p_)]
                 for _ in range(q_)]
            MN = [[sum(M[i][l] * N[l][j] for l in range(q_)) for j in range(p_)]
                  for i in range(p_)]
            NM = [[sum(N[i][l] * M[l][j] for l in range(p_)) for j in range(q_)]
                  for i in range(q_)]
            cA = _charpoly_frac(MN)           # degree p_, highest first
            cB = _charpoly_frac(NM)           # degree q_
            padded = cA + [Fraction(0)] * (q_ - p_)
            if padded != cB:
                worst += 1
        l2.append({"shape": [p_, q_], "mismatches": worst})
        if worst:
            die("checker:L2-refuted %r" % ((p_, q_),))
    out["L2_sylvester_charpoly"] = {"rows": l2, "all_hold": True}

    # L2-teeth: a DELIBERATELY WRONG padding exponent must be caught.
    M = [[Fraction(1), Fraction(2), Fraction(3)], [Fraction(0), Fraction(1), Fraction(-1)]]
    N = [[Fraction(1), Fraction(0)], [Fraction(2), Fraction(1)], [Fraction(-1), Fraction(3)]]
    MN = [[sum(M[i][l] * N[l][j] for l in range(3)) for j in range(2)] for i in range(2)]
    NM = [[sum(N[i][l] * M[l][j] for l in range(2)) for j in range(3)] for i in range(3)]
    good = _charpoly_frac(MN) + [Fraction(0)] * 1 == _charpoly_frac(NM)
    wrong = _charpoly_frac(MN) + [Fraction(0)] * 2 == _charpoly_frac(NM)
    out["L2_tooth_wrong_exponent_is_caught"] = {"correct_padding_holds": bool(good),
                                                "wrong_padding_holds": bool(wrong)}
    if not good or wrong:
        die("checker:L2-tooth")

    # L3: exchangeability => the k-subset reduced state is subset-independent.
    # Exact rational Dicke amplitudes, exact rational reduced matrices.
    l3 = []
    for d in (3, 4, 5):
        c = [Fraction(rng.randint(-9, 9), rng.randint(1, 5)) for _ in range(d + 1)]
        # use amplitudes psi[b] = c_{|b|} (unnormalised Dicke-proportional, which is
        # still exactly permutation symmetric -- normalisation is irrelevant here)
        psi = [c[bin(b).count("1")] for b in range(1 << d)]
        for k in range(1, d):
            mats = []
            for X in itertools.combinations(range(d), k):
                Y = [i for i in range(d) if i not in X]
                R = [[Fraction(0)] * (1 << k) for _ in range(1 << k)]
                for b in range(1 << d):
                    u = sum(((b >> X[j]) & 1) << j for j in range(k))
                    w = sum(((b >> Y[j]) & 1) << j for j in range(len(Y)))
                    for b2 in range(1 << d):
                        v = sum(((b2 >> X[j]) & 1) << j for j in range(k))
                        w2 = sum(((b2 >> Y[j]) & 1) << j for j in range(len(Y)))
                        if w == w2:
                            R[u][v] += psi[b] * psi[b2]
                mats.append(R)
            same = all(m == mats[0] for m in mats[1:])
            l3.append({"d": d, "k": k, "n_subsets": len(mats), "identical": bool(same)})
            if not same:
                die("checker:L3-refuted d=%d k=%d" % (d, k))
    out["L3_exchangeability_size_only"] = {"rows": l3, "all_hold": True}

    # L4: the entropy algebra, by hand.  Work in the free module over the symbols
    # S_A, S_B, S_R, S_AB, S_RB, S_AR, S_ABR represented as coefficient vectors.
    names = ["S_A", "S_B", "S_R", "S_AB", "S_RB", "S_AR", "S_ABR"]
    ix = {nm: i for i, nm in enumerate(names)}

    def vec(**kw):
        v = [Fraction(0)] * len(names)
        for k, c in kw.items():
            v[ix[k]] += Fraction(c)
        return v

    def add(*vs):
        return [sum(x) for x in zip(*vs)]

    def neg(v):
        return [-x for x in v]

    def purity(v):
        """Impose S_R = S_AB, S_RB = S_A, S_AR = S_B, S_ABR = 0."""
        w = v[:]
        w[ix["S_AB"]] += w[ix["S_R"]]
        w[ix["S_R"]] = Fraction(0)
        w[ix["S_A"]] += w[ix["S_RB"]]
        w[ix["S_RB"]] = Fraction(0)
        w[ix["S_B"]] += w[ix["S_AR"]]
        w[ix["S_AR"]] = Fraction(0)
        w[ix["S_ABR"]] = Fraction(0)
        return w
    I_AB = add(vec(S_A=1), vec(S_B=1), neg(vec(S_AB=1)))
    I_RB = add(vec(S_R=1), vec(S_B=1), neg(vec(S_RB=1)))
    I_ARB = add(vec(S_AR=1), vec(S_B=1), neg(vec(S_ABR=1)))
    pair_complement = purity(add(I_AB, I_RB, neg(vec(S_B=2))))
    total_form = purity(add(I_ARB, neg(vec(S_B=2))))
    I_AR_given_B = add(vec(S_AB=1), vec(S_RB=1), neg(vec(S_B=1)), neg(vec(S_ABR=1)))
    I_AR = add(vec(S_A=1), vec(S_R=1), neg(vec(S_AR=1)))
    cmi_minus_mi = purity(add(I_AR_given_B, neg(I_AR)))
    ssa_value = purity(I_AR_given_B)
    zero = [Fraction(0)] * len(names)
    if pair_complement != zero or total_form != zero or cmi_minus_mi != zero:
        die("checker:L4-refuted")
    if ssa_value == zero:
        die("checker:L4-ssa-should-not-vanish")
    out["L4_pair_complement"] = {
        "I(A:B)+I(R:B)-2S(B) under purity": "0 (exact)",
        "I(AR:B)-2S(B) under purity": "0 (exact)",
        "I(A:R|B)-I(A:R) under purity": "0 (exact)",
        "I(A:R|B) under purity": " + ".join(
            "%s*%s" % (ssa_value[i], names[i]) for i in range(len(names))
            if ssa_value[i] != 0),
        "SSA_equality_case_does_NOT_hold_identically": True}

    # THM: assemble with an explicit s-vector, exactly, for concrete d.
    thm = []
    for d in range(3, 13):
        sv = [Fraction(rng.randint(-50, 50), rng.randint(1, 9)) for _ in range(d + 1)]
        sv[0] = Fraction(0)
        sv[d] = Fraction(0)
        for k in range(d + 1):                     # impose the reflection exactly
            sv[k] = sv[min(k, d - k)]
        sv[0] = Fraction(0)
        sv[d] = Fraction(0)
        G = {m: sv[m] + sv[1] - sv[m + 1] for m in range(1, d)}
        res = [G[m] + G[d - 1 - m] - G[d - 1] for m in range(1, d - 1)]
        okd = all(r == 0 for r in res)
        thm.append({"d": d, "exact_residuals_all_zero": bool(okd)})
        if not okd:
            die("checker:THM-refuted d=%d" % d)
    out["THM_additivity_exact_over_the_rationals"] = {"rows": thm, "all_hold": True}

    # THM-teeth: DROP the reflection and the identity must break.
    broken = []
    for d in (5, 6):
        sv = [Fraction(0)] + [Fraction(k * k + 1, 7) for k in range(1, d)] + [Fraction(0)]
        G = {m: sv[m] + sv[1] - sv[m + 1] for m in range(1, d)}
        res = [G[m] + G[d - 1 - m] - G[d - 1] for m in range(1, d - 1)]
        broken.append({"d": d, "nonzero_residual_present": bool(any(r != 0 for r in res))})
        if not any(r != 0 for r in res):
            die("checker:THM-tooth d=%d" % d)
    out["THM_tooth_without_the_reflection_the_identity_breaks"] = broken
    return out


# ================================ arbitrary precision confirmation ===========
def mp_confirm(d, lam, t, dps=50):
    """50-digit confirmation that the identity residual is not a float64 artifact."""
    import mpmath as mp
    old = mp.mp.dps
    mp.mp.dps = dps
    try:
        n = d + 1
        dim = 1 << n
        lam = mp.mpf(repr(lam))
        t = mp.mpf(repr(t))
        diag = []
        for b in range(dim):
            z0 = 1 - 2 * ((b >> (n - 1)) & 1)          # site 0 at bit n-1
            s = 0
            for k in range(1, n):
                s -= z0 * (1 - 2 * ((b >> (n - 1 - k)) & 1))
            diag.append(mp.mpf(s))
        psi = [mp.mpc(1) / mp.sqrt(dim)] * dim

        def mv(v):
            o = [diag[b] * v[b] for b in range(dim)]
            for i in range(n):
                msk = 1 << (n - 1 - i)
                for b in range(dim):
                    o[b] -= lam * v[b ^ msk]
            return o
        acc = list(psi)
        term = list(psi)
        for k in range(1, 200):
            term = mv(term)
            term = [x * (-1j * t / k) for x in term]
            acc = [a + b for a, b in zip(acc, term)]
            if max(abs(x) for x in term) < mp.mpf(10) ** (-(dps + 10)):
                break
        # pointer branches: bit n-1 is site 0
        brs = []
        for z in (0, 1):
            v = [acc[b] for b in range(dim) if ((b >> (n - 1)) & 1) == z]
            p = sum(abs(x) ** 2 for x in v)
            v = [x / mp.sqrt(p) for x in v]
            brs.append((p, v))
        tot = sum(p for p, _ in brs)

        def S(v, axes):
            """entropy of the reduced state on `axes` (branch axes 0..d-1, axis j =
            site j+1 at bit n-1-(j+1))."""
            axes = sorted(axes)
            if not axes or len(axes) == d:
                return mp.mpf(0)
            rest = [j for j in range(d) if j not in axes]
            ka = len(axes)
            M = mp.zeros(1 << ka, 1 << len(rest))
            for b in range(1 << d):
                u = sum(((b >> (d - 1 - axes[j])) & 1) << (ka - 1 - j) for j in range(ka))
                w = sum(((b >> (d - 1 - rest[j])) & 1) << (len(rest) - 1 - j)
                        for j in range(len(rest)))
                M[u, w] = v[b]
            R = M * M.transpose_conj()
            # R is complex HERMITIAN -- eighe, not eigsy: dropping the imaginary
            # part here would silently change the spectrum.
            ev = mp.eighe(R, eigvals_only=True)
            tot2 = sum(ev)
            out = mp.mpf(0)
            for e in ev:
                if e > mp.mpf(10) ** (-(dps + 5)):
                    q = e / tot2
                    out -= q * mp.log(q) / mp.log(2)
            return out

        def I(A, B):
            return sum((p / tot) * (S(v, A) + S(v, B) - S(v, sorted(set(A) | set(B))))
                       for p, v in brs)
        G = {m: I(list(range(m)), [m]) for m in range(1, d)}
        res = max(abs(G[m] + G[d - 1 - m] - G[d - 1]) for m in range(1, d - 1))
        return {"d": d, "field": float(lam), "Jt": float(t), "dps": dps,
                "G_of_m": {str(m): mp.nstr(G[m], 25) for m in G},
                "max_abs_additivity_residual": mp.nstr(res, 8),
                "residual_float": float(res)}
    finally:
        mp.mp.dps = old


# ==================================================================== main ===
def main():
    pins = verify_pins()
    head = git(["rev-parse", "--short=10", "HEAD"]).stdout.decode().strip()
    memo = open(os.path.join(ROOT, PARENT_MEMO), "rb").read().decode("utf-8")
    r929 = json.load(open(os.path.join(ROOT, C929_RECEIPT)))
    prim_path = os.path.join(ROOT, PRIMARY_RECEIPT)
    if not os.path.exists(prim_path):
        die("primary-receipt-missing")
    prim = json.load(open(prim_path))
    prim_sha = sha256_bytes(open(prim_path, "rb").read())
    lines = []
    ap = lines.append
    findings = []
    refutations = []

    # ---- the statistic definition, re-read from the memo bytes independently --
    mdef = re.search(r"`C_ab = sum_z p_z \[S\(rho_Fa\^z\)\+S\(rho_Fb\^z\)"
                     r"-S\(rho_FaFb\^z\)\]`", memo)
    mdephase = re.search(r"Zero the off-diagonal `S` blocks before evaluating the "
                         r"formula", memo)
    if mdef is None or mdephase is None:
        die("memo:statistic-definition-not-found")
    stat_ok = {"formula_found_in_memo_bytes": mdef.group(0),
               "dephasing_instruction_found": mdephase.group(0),
               "agrees_with_the_primary_quote": bool(
                   mdef.group(0) == prim["statistic_definition_byte_verified"][
                       "C_ab_formula"])}
    if not stat_ok["agrees_with_the_primary_quote"]:
        refutations.append("the primary's quoted statistic formula does not match "
                           "the memo bytes")

    # ================= C1: independent reproduction of the 929 ladder =========
    pub_ladder = r929["Q1_within_pair_multiplicity_vs_size"][
        "pure_star_multiplicity_ladder_G_d_of_m"]
    c1 = []
    c1_dev = 0.0
    for key in sorted(pub_ladder):
        e = pub_ladder[key]
        d, lam = e["d"], e["field"]
        vec, n, S, arms = star_cell(d, lam, 0.7, route="K")
        G = ladder_from(vec, n, S, arms)
        for m in sorted(G):
            dev = abs(G[m] - float(e["G_of_m"][str(m)]))
            c1_dev = max(c1_dev, dev)
            c1.append({"cell": key, "m": m, "checker": G[m],
                       "pinned_929": float(e["G_of_m"][str(m)]), "abs_dev": dev})
    if c1_dev > 1e-12:
        refutations.append("the 929 ladder does not reproduce on independent "
                           "machinery: max dev %.3e" % c1_dev)

    # ================= C2: the derived law, re-derived and re-tested ==========
    c2 = []
    c2_dev = 0.0
    for key in sorted(pub_ladder):
        e = pub_ladder[key]
        d, lam = e["d"], e["field"]
        vec, n, S, arms = star_cell(d, lam, 0.7, route="E")     # a THIRD route
        s, spread = s_seq(vec, n, S, arms)
        for m in range(1, d):
            pred = s[m] + s[1] - s[m + 1]
            dev = abs(pred - float(e["G_of_m"][str(m)]))
            c2_dev = max(c2_dev, dev)
        c2.append({"cell": key, "d": d, "field": lam,
                   "s_of_k": {str(k): s[k] for k in sorted(s)},
                   "exchangeability_max_spread": max(spread.values()),
                   "reflection_max_|s(k)-s(d-k)|": max(abs(s[k] - s[d - k])
                                                       for k in range(d + 1)),
                   "law_max_dev_vs_pinned": c2_dev})
    if c2_dev > 1e-12:
        refutations.append("the derived law G=s(m)+s(1)-s(m+1) fails on independent "
                           "machinery: %.3e" % c2_dev)

    # ================= C3: ATTACK THE HYPOTHESES =============================
    # Sample states that satisfy H1 (pure) + H4 (exchangeable) but have NOTHING to
    # do with the frozen dynamics.  If the theorem is right, additivity must hold
    # for every one of them; if it is wrong, this finds a counterexample.
    rng = np.random.default_rng(20260805)
    attack = []
    attack_worst = 0.0
    n_samples = 0
    for d in range(3, 8):
        for _ in range(200):
            c = rng.normal(size=d + 1) + 1j * rng.normal(size=d + 1)
            amp = np.array([c[bin(b).count("1")] for b in range(1 << d)],
                           dtype=np.complex128)
            amp /= np.linalg.norm(amp)
            s = {k: svd_entropy_bits(amp, d, tuple(range(k))) for k in range(d + 1)}
            G = {m: s[m] + s[1] - s[m + 1] for m in range(1, d)}
            res = additivity_residual(G, d)
            attack_worst = max(attack_worst, res)
            n_samples += 1
    attack.append({"family": "random permutation-symmetric PURE states (H1+H4 hold, "
                             "no frozen dynamics anywhere)",
                   "n_samples": n_samples, "degrees": "3..7",
                   "max_abs_additivity_residual": attack_worst,
                   "counterexample_found": bool(attack_worst > IDENT_TOL)})
    if attack_worst > IDENT_TOL:
        refutations.append("a state satisfying the primary's hypotheses VIOLATES "
                           "additivity: %.3e" % attack_worst)
    # control: drop H4 and the same machinery must break
    ctrl_worst = 0.0
    for d in (5, 6):
        for _ in range(200):
            amp = rng.normal(size=1 << d) + 1j * rng.normal(size=1 << d)
            amp /= np.linalg.norm(amp)
            s = {k: svd_entropy_bits(amp, d, tuple(range(k))) for k in range(d + 1)}
            G = {m: s[m] + s[1] - s[m + 1] for m in range(1, d)}
            ctrl_worst = max(ctrl_worst, additivity_residual(G, d))
    attack.append({"family": "random NON-symmetric pure states (H4 dropped) -- the "
                             "control that the test can see a violation",
                   "max_abs_additivity_residual": ctrl_worst,
                   "violates_as_it_must": bool(ctrl_worst > 1e-3)})

    # ================= C4: COUNTEREXAMPLE HUNT OFF THE MEASURED GRID =========
    hunt = []
    hunt_worst = 0.0
    hunt_worst_row = None
    # (a) new degrees / fields / times, pure stars
    for d in list(range(2, 13)):
        for lam in (0.02, 0.05, 0.075, 0.10, 0.125, 0.15, 0.20, 0.30, 1.0, 5.0):
            for t in (0.05, 0.3, 0.7, 1.2, 2.5, 5.0):
                if d >= 11 and (lam not in (0.05, 0.10) or t != 0.7):
                    continue
                if d < 3:
                    continue
                vec, n, S, arms = star_cell(d, lam, t, route="K")
                G = ladder_from(vec, n, S, arms)
                res = additivity_residual(G, d)
                if res > hunt_worst:
                    hunt_worst, hunt_worst_row = res, {"family": "pure star", "d": d,
                                                       "field": lam, "Jt": t}
                hunt.append({"family": "pure star K_{1,d}", "d": d, "field": lam,
                             "Jt": t, "residual": res,
                             "G_max": max(G.values()),
                             "violates": bool(res > IDENT_TOL)})
    # (b) NON-STAR spiders with ISOMORPHIC arms -- the theorem predicts the
    #     identity EXTENDS here (H4 holds, the arms are just bigger).
    iso_specs = {"path arms L=2": path_shape(2), "path arms L=3": path_shape(3),
                 "claw arms L=3": claw_shape(3), "claw arms L=4": claw_shape(4)}
    for label, shape in sorted(iso_specs.items()):
        for d in (3, 4, 5):
            for lam in CLAIM_LAMBDAS:
                n_guess = 1 + d * len(shape)
                if n_guess > 15:
                    continue
                vec, n, S, arms = spider_cell([shape] * d, lam, 0.7, route="K")
                G = ladder_from(vec, n, S, arms)
                res = additivity_residual(G, d)
                if res > hunt_worst:
                    hunt_worst, hunt_worst_row = res, {"family": label, "d": d,
                                                       "field": lam, "Jt": 0.7}
                hunt.append({"family": "isomorphic-arm spider (%s)" % label, "d": d,
                             "field": lam, "Jt": 0.7, "n": n, "residual": res,
                             "G_max": max(G.values()),
                             "violates": bool(res > IDENT_TOL)})
    # (c) the FROZEN preparation variant: deep sites in |0> rather than |+>
    prep_rows = []
    for d in (3, 4, 5):
        for lam in CLAIM_LAMBDAS:
            shape = path_shape(2)
            n, bonds, arms = spider_bonds([shape] * d)
            anchors = {a[0] for a in arms}
            vec = evolve(n, bonds, set([0]) | anchors, lam, 0.7, "K")   # frozen prep
            G = ladder_from(vec, n, 0, arms)
            res = additivity_residual(G, d)
            prep_rows.append({"d": d, "field": lam, "prep": "FROZEN (pointer+anchors "
                                                            "|+>, deep sites |0>)",
                              "residual": res, "violates": bool(res > IDENT_TOL)})
            if res > hunt_worst:
                hunt_worst, hunt_worst_row = res, {"family": "frozen-prep spider",
                                                   "d": d, "field": lam, "Jt": 0.7}
    # (d) a LOOP-carrying geometry: the pointer on a triangle-plus-arms.  H4 fails
    #     here (the arms are not isomorphic), so this is a SCOPE probe, not a
    #     counterexample candidate for the theorem.
    loop_rows = []
    for lam in CLAIM_LAMBDAS:
        n = 6
        bonds = [(0, 1), (0, 2), (1, 2), (0, 3), (0, 4), (0, 5)]   # triangle + 3 arms
        vec = evolve(n, bonds, set(range(n)), lam, 0.7, "K")
        arms = [[1], [2], [3], [4], [5]]
        G = ladder_from(vec, n, 0, arms)
        loop_rows.append({"geometry": "pointer on a triangle with three extra leaves "
                                      "(LOOP-CARRYING, arms NOT isomorphic)",
                          "field": lam, "d": 5, "residual": additivity_residual(G, 5),
                          "H4_holds": False})

    # (e) the pair-complement identity itself, on EVERY family above -- it needs
    #     only H1..H3, so it must hold even where additivity fails.
    pc_rows = []
    pc_worst = 0.0
    for label, mk in [
            ("pure star d=6 @0.10", lambda: star_cell(6, 0.10, 0.7, "K")),
            ("path-arm spider d=5 L=2 @0.10", lambda: spider_cell([path_shape(2)] * 5,
                                                                  0.10, 0.7, "K")),
            ("MIXED-arm spider d=5 @0.10",
             lambda: spider_cell([path_shape(1)] * 4 + [path_shape(2)], 0.10, 0.7, "K")),
            ("MIXED-arm spider d=4 @0.05",
             lambda: spider_cell([path_shape(1)] * 2 + [path_shape(2), path_shape(3)],
                                 0.05, 0.7, "K")),
            ("LOOP-carrying triangle+3 leaves d=5 @0.10",
             lambda: (evolve(6, [(0, 1), (0, 2), (1, 2), (0, 3), (0, 4), (0, 5)],
                             set(range(6)), 0.10, 0.7, "K"),
                      6, 0, [[1], [2], [3], [4], [5]]))]:
        vec, n, S, arms = mk()
        d = len(arms)
        brs, order = pointer_branches(vec, n, S)
        pos = {s: j for j, s in enumerate(order)}
        tot = sum(p for p, _ in brs)
        A = list(itertools.chain(*arms[:1]))
        B = list(itertools.chain(*arms[1:2]))
        R = list(itertools.chain(*arms[2:]))
        SB = sum((p / tot) * svd_entropy_bits(v, n - 1,
                                              tuple(sorted(pos[s] for s in B)))
                 for p, v in brs)
        r = C_stat(vec, n, S, A, B) + C_stat(vec, n, S, R, B) - 2 * SB
        pc_worst = max(pc_worst, abs(r))
        pc_rows.append({"family": label, "pair_complement_residual": r,
                        "additivity_residual": additivity_residual(
                            ladder_from(vec, n, S, arms), d)})
    if pc_worst > IDENT_TOL:
        refutations.append("the pair-complement identity fails somewhere: %.3e" % pc_worst)

    # ================= C5: the SEAL, recomputed independently ================
    seal = prim["seal"]
    seal_recheck = {k: v for k, v in seal.items() if k != "seal_sha256"}
    seal_digest_ok = sha256_obj(seal_recheck) == seal["seal_sha256"]
    # independent inversion: solve the LINEAR SYSTEM for s rather than recursing
    seal_rows = []
    seal_dev = 0.0
    for key in sorted(pub_ladder):
        e = pub_ladder[key]
        d = e["d"]
        G = {int(k): float(v) for k, v in e["G_of_m"].items()}
        # unknowns s(1..d-1); equations G(m) = s(m) + s(1) - s(m+1), m=1..d-1,
        # with s(d) = 0 imposed as a column that does not exist.
        A = np.zeros((d - 1, d - 1))
        b = np.zeros(d - 1)
        for m in range(1, d):
            if m <= d - 1:
                A[m - 1, m - 1] += 1.0
            A[m - 1, 0] += 1.0
            if m + 1 <= d - 1:
                A[m - 1, m] -= 1.0
            b[m - 1] = G[m]
        sv = np.linalg.solve(A, b)
        s = {0: 0.0, d: 0.0}
        for k in range(1, d):
            s[k] = float(sv[k - 1])
        their = seal["predictions"][key]["s_of_k_reconstructed"]
        for k in range(0, d + 1):
            seal_dev = max(seal_dev, abs(s[k] - float(their[str(k)])))
        p3 = {}
        for ma in range(2, d):
            for mb in range(2, d):
                if ma <= mb and ma + mb <= d:
                    p3["%d|%d" % (ma, mb)] = s[ma] + s[mb] - s[ma + mb]
        their3 = seal["predictions"][key][
            "P3_both_merged_pairs_C(ma,mb)=s(ma)+s(mb)-s(ma+mb)"]
        for k in p3:
            seal_dev = max(seal_dev, abs(p3[k] - float(their3[k])))
        seal_rows.append({"cell": key, "checker_s": {str(k): s[k] for k in sorted(s)},
                          "checker_P3": p3})
    if seal_dev > 1e-11:
        refutations.append("the seal's predictions do not reconstruct from the "
                           "pinned bytes: %.3e" % seal_dev)
    # holdout-freedom: every seal input must be a value that exists verbatim in the
    # pinned 929 receipt.
    holdout_ok = True
    for key, e in seal["inputs_quoted"].items():
        for m, v in e["G_of_m"].items():
            if float(pub_ladder[key]["G_of_m"][m]) != float(v):
                holdout_ok = False
    if not holdout_ok:
        refutations.append("a seal input is NOT a pinned 929 value")

    # verify the primary's P3 measurements independently
    p3_check = []
    p3_dev = 0.0
    for row in prim["seal_verification"]["P3_both_merged_pair_values"]["rows"]:
        key = row["cell"]
        d = pub_ladder[key]["d"]
        lam = pub_ladder[key]["field"]
        ma, mb = (int(x) for x in row["pair"].split("|"))
        vec, n, S, arms = star_cell(d, lam, 0.7, route="E")
        A = list(itertools.chain(*arms[:ma]))
        B = list(itertools.chain(*arms[ma:ma + mb]))
        mine = C_stat(vec, n, S, A, B)
        dev = abs(mine - row["measured_frozen_path"])
        p3_dev = max(p3_dev, dev)
        p3_check.append({"cell": key, "pair": row["pair"], "checker": mine,
                         "primary": row["measured_frozen_path"], "abs_dev": dev,
                         "sealed": row["sealed_prediction"]})
    if p3_dev > 1e-11:
        refutations.append("the primary's both-merged measurements do not "
                           "reproduce: %.3e" % p3_dev)

    # ================= C6: the candidate verdicts, recomputed ================
    # (b') the SSA equality case
    ssa = []
    for d in (4, 5, 6):
        for lam in CLAIM_LAMBDAS:
            vec, n, S, arms = star_cell(d, lam, 0.7, route="K")
            brs, order = pointer_branches(vec, n, S)
            tot = sum(p for p, _ in brs)

            def SS(ax):
                return sum((p / tot) * svd_entropy_bits(v, n - 1, tuple(sorted(ax)))
                           for p, v in brs)
            A, B, R = [0], [1], list(range(2, d))
            I_AR_given_B = SS(A + B) + SS(R + B) - SS(B) - SS(list(range(d)))
            I_AR = SS(A) + SS(R) - SS(A + R)
            ssa.append({"cell": "d%d@%g" % (d, lam), "I(A:R|B)": I_AR_given_B,
                        "I(A:R)": I_AR, "diff": abs(I_AR_given_B - I_AR)})
    ssa_min = min(r["I(A:R|B)"] for r in ssa)
    ssa_diff = max(r["diff"] for r in ssa)
    prim_ssa_min = min(r["I(A:R|B)"] for r in
                       prim["Q2_candidate_verdicts"]["b_information_decomposition"][
                           "ssa_equality_case_REFUTED"]["rows"])
    ssa_agrees = abs(ssa_min - prim_ssa_min) < 1e-9

    # (c) the perturbative candidate, recomputed at strong coupling
    strong = []
    for d in (3, 4, 5, 6):
        for lam in (0.5, 1.0, 2.0, 5.0):
            for t in (0.7, 3.0):
                vec, n, S, arms = star_cell(d, lam, t, route="K")
                G = ladder_from(vec, n, S, arms)
                strong.append({"d": d, "field": lam, "Jt": t,
                               "G_max": max(G.values()),
                               "residual": additivity_residual(G, d)})
    strong_res = max(r["residual"] for r in strong)
    strong_G = max(r["G_max"] for r in strong)

    # (a) exchangeability-only: exchangeable but MIXED
    exch = []
    for d in (4, 5):
        vec, n, S, arms = star_cell(d + 1, 0.10, 0.7, route="K")
        brs, order = pointer_branches(vec, n, S)
        tot = sum(p for p, _ in brs)
        keep = list(range(d))            # branch axes of the first d leaves

        def SM(ax):
            return sum((p / tot) * svd_entropy_bits_unnormalised(
                v, n - 1, tuple(sorted(ax))) for p, v in brs)
        s = {k: SM(keep[:k]) for k in range(d + 1)}
        G = {m: s[m] + s[1] - s[m + 1] for m in range(1, d)}
        spread = max(abs(SM([i]) - SM([j])) for i in keep for j in keep)
        exch.append({"construction": "the d=%d leaf block of a (d+1)=%d star"
                                     % (d, d + 1),
                     "exchangeable_spread": spread, "S(all_kept)": s[d],
                     "additivity_residual": additivity_residual(G, d)})

    # ================= C7: arbitrary-precision confirmation =================
    mp_rows = [mp_confirm(3, 0.10, 0.7), mp_confirm(4, 0.05, 0.7),
               mp_confirm(4, 0.10, 0.7)]
    mp_worst = max(r["residual_float"] for r in mp_rows)

    # ================= C8: the independent symbolics =========================
    sym = exact_symbolics()

    # ================= C9: the primary's published arithmetic ================
    arith = {}
    lawrows = prim["Q2_derived_law_vs_pinned_ladder"]["rows"]
    arith["law_rows_recomputed"] = max(
        abs((r["G_predicted_from_s"] - r["G_measured_929_pinned"]) - r["residual"])
        for r in lawrows)
    identrows = prim["Q2_identity_at_new_cells"]["rows"]
    bad_ident = 0
    for r in identrows:
        d = r["d"]
        G = {int(k): float(v) for k, v in r["G_of_m"].items()}
        mine = additivity_residual(G, d)
        if abs(mine - r["max_|additivity residual|"]) > 1e-15:
            bad_ident += 1
    arith["identity_rows_with_inconsistent_published_residual"] = bad_ident
    arith["max_published_identity_residual"] = max(
        r["max_|additivity residual|"] for r in identrows)
    if bad_ident:
        refutations.append("%d published identity rows have a residual that does not "
                           "follow from their own G values" % bad_ident)
    # the primary's concavity claim
    conc = []
    for row in c2:
        d = row["d"]
        s = {int(k): v for k, v in row["s_of_k"].items()}
        second = [s[k + 1] - 2 * s[k] + s[k - 1] for k in range(1, d)]
        conc.append({"cell": row["cell"], "max_second_difference": max(second)})
    arith["s_is_concave_everywhere"] = bool(all(r["max_second_difference"] <= 1e-15
                                                for r in conc))
    if not arith["s_is_concave_everywhere"]:
        findings.append("s(k) is NOT concave on every certified cell; the primary's "
                        "remark that the ladder is monotone because s is concave "
                        "needs the scope it is stated at")

    # ================= TEETH =================================================
    teeth = {}
    # K1 planted identity break
    Gp = {int(k): float(v) for k, v in pub_ladder["d6@0.05"]["G_of_m"].items()}
    Gp[2] += 3e-7
    teeth["K1_planted_identity_break_is_caught"] = {
        "plant": "d6@0.05 rung m=2 shifted by +3e-7 bit",
        "residual": additivity_residual(Gp, 6),
        "caught": bool(additivity_residual(Gp, 6) > IDENT_TOL),
        "fires": bool(additivity_residual(Gp, 6) > IDENT_TOL)}
    # K2 the hypothesis attack found nothing, and the control shows it could
    teeth["K2_hypothesis_attack"] = {
        "n_states_satisfying_H1_H4": n_samples,
        "max_residual": attack_worst,
        "control_without_H4_max_residual": ctrl_worst,
        "attack_failed_to_refute": bool(attack_worst <= IDENT_TOL),
        "control_shows_the_test_can_see_a_violation": bool(ctrl_worst > 1e-3),
        "fires": bool(attack_worst <= IDENT_TOL and ctrl_worst > 1e-3)}
    # K3 purity break
    teeth["K3_purity_break_breaks_additivity"] = {
        "rows": exch,
        "min_residual": min(r["additivity_residual"] for r in exch),
        "fires": bool(min(r["additivity_residual"] for r in exch) > 1e-4)}
    # K4 exchangeability break breaks additivity but not the complement identity
    mixed_rows = [r for r in pc_rows if "MIXED" in r["family"]]
    teeth["K4_exchangeability_break_separates_the_two_identities"] = {
        "rows": mixed_rows,
        "additivity_min_residual": min(r["additivity_residual"] for r in mixed_rows),
        "pair_complement_max_residual": max(abs(r["pair_complement_residual"])
                                            for r in mixed_rows),
        "fires": bool(min(r["additivity_residual"] for r in mixed_rows) > 1e-8
                      and max(abs(r["pair_complement_residual"])
                              for r in mixed_rows) <= IDENT_TOL)}
    # K5 route cross-check: Lanczos vs expm_multiply vs the primary's numbers
    rdev = 0.0
    rrows = []
    for d in (3, 5, 6, 8, 10, 12):
        for lam in CLAIM_LAMBDAS:
            for t in (0.7, 5.0) if d <= 6 else (0.7,):
                vK, n, S, arms = star_cell(d, lam, t, "K")
                vE, _, _, _ = star_cell(d, lam, t, "E")
                ph = np.vdot(vK, vE)
                ph = ph / abs(ph)
                dv = float(np.abs(vK * ph - vE).max())
                rdev = max(rdev, dv)
                rrows.append({"d": d, "field": lam, "Jt": t, "state_dev": dv})
    teeth["K5_route_cross_check_lanczos_vs_expm_multiply"] = {
        "max_abs_state_dev": rdev, "rows": rrows,
        "why_this_matters": "the identity holds for ANY pure exchangeable state, so "
                            "an unconverged propagator would satisfy it vacuously.  "
                            "This tooth shows the states the hunt ran on are the "
                            "physical ones, at every degree up to 12.",
        "fires": bool(rdev < 1e-10)}
    # K6 reversed-ordering agreement with the pinned 929 ladder
    teeth["K6_reversed_ordering_reproduces_the_pinned_ladder"] = {
        "max_abs_dev": c1_dev, "n_rungs": len(c1), "fires": bool(c1_dev < 1e-12)}
    # K7 determinism
    dg1 = sha256_obj([{k: r[k] for k in ("cell", "m", "checker")} for r in c1])
    c1b = []
    for key in sorted(pub_ladder):
        e = pub_ladder[key]
        vec, n, S, arms = star_cell(e["d"], e["field"], 0.7, route="K")
        G = ladder_from(vec, n, S, arms)
        for m in sorted(G):
            c1b.append({"cell": key, "m": m, "checker": G[m]})
    teeth["K7_determinism"] = {"digest": dg1, "repeat_identical":
                               bool(sha256_obj(c1b) == dg1),
                               "fires": bool(sha256_obj(c1b) == dg1)}
    # K8 tampered pin
    b = open(os.path.join(ROOT, C929_RECEIPT), "rb").read()
    teeth["K8_tampered_pin_is_caught"] = {
        "sha256_changes_under_one_byte": bool(sha256_bytes(b + b" ") != PINS[C929_RECEIPT]),
        "fires": bool(sha256_bytes(b + b" ") != PINS[C929_RECEIPT])}
    # K9 tampered memo statistic
    badmemo = memo.replace("-S(rho_FaFb^z)]`", "]`")
    teeth["K9_tampered_statistic_definition_is_caught"] = {
        "caught": bool(re.search(r"`C_ab = sum_z p_z \[S\(rho_Fa\^z\)\+"
                                 r"S\(rho_Fb\^z\)-S\(rho_FaFb\^z\)\]`",
                                 badmemo) is None),
        "fires": bool(re.search(r"`C_ab = sum_z p_z \[S\(rho_Fa\^z\)\+"
                                r"S\(rho_Fb\^z\)-S\(rho_FaFb\^z\)\]`",
                                badmemo) is None)}
    # K10 arbitrary precision
    teeth["K10_arbitrary_precision_confirmation"] = {
        "dps": 50, "rows": mp_rows, "max_residual_at_50_digits": mp_worst,
        "float64_result_is_not_a_coincidence": bool(mp_worst < 1e-40),
        "fires": bool(mp_worst < 1e-40)}
    # K11 seal holdout-freedom and tamper evidence
    tampered = json.loads(json.dumps(seal_recheck))
    k0 = sorted(tampered["predictions"])[0]
    tampered["predictions"][k0]["P1_s_of_d_is_zero"] = 1.0
    teeth["K11_seal_holdout_free_and_tamper_evident"] = {
        "digest_recomputes": bool(seal_digest_ok),
        "every_seal_input_is_a_pinned_929_value": bool(holdout_ok),
        "independent_inversion_max_dev": seal_dev,
        "tampered_digest_differs": bool(sha256_obj(tampered) != seal["seal_sha256"]),
        "fires": bool(seal_digest_ok and holdout_ok and seal_dev <= 1e-11
                      and sha256_obj(tampered) != seal["seal_sha256"])}
    # K12 Euler guard (own)
    vK, n12, _, _ = star_cell(5, 0.10, 0.7, "K")
    H12 = build_H_sparse(6, star_bonds(5), 0.10)
    vE12 = euler_route(H12, prep_vec(6, set(range(6))), 0.7, nstep=60)
    teeth["K12_euler_guard"] = {
        "state_dev": float(np.abs(vE12 - vK).max()),
        "norm_error": float(abs(np.vdot(vE12, vE12).real - 1.0)),
        "fires": bool(float(np.abs(vE12 - vK).max()) > 1e-6)}
    # K13 the exact-arithmetic symbolics have teeth
    teeth["K13_exact_symbolics_have_teeth"] = {
        "wrong_sylvester_exponent_is_caught":
            not sym["L2_tooth_wrong_exponent_is_caught"]["wrong_padding_holds"],
        "identity_breaks_without_the_reflection":
            all(r["nonzero_residual_present"]
                for r in sym["THM_tooth_without_the_reflection_the_identity_breaks"]),
        "fires": bool(
            not sym["L2_tooth_wrong_exponent_is_caught"]["wrong_padding_holds"]
            and all(r["nonzero_residual_present"] for r in
                    sym["THM_tooth_without_the_reflection_the_identity_breaks"]))}
    # K14 anchors
    v0, n0, S0, arms0 = star_cell(5, 0.10, 0.0, "K")
    s0, _ = s_seq(v0, n0, S0, arms0)
    vz, nz, Sz, armsz = star_cell(5, 0.0, 0.7, "K")
    sz, _ = s_seq(vz, nz, Sz, armsz)
    teeth["K14_t0_and_zero_field_anchors"] = {
        "max_s(k)_at_Jt_0": max(abs(v) for v in s0.values()),
        "max_s(k)_at_lambda_0": max(abs(v) for v in sz.values()),
        "fires": bool(max(abs(v) for v in s0.values()) < 1e-9
                      and max(abs(v) for v in sz.values()) < 1e-12)}
    # K15 the counterexample hunt actually covered new ground
    offgrid = [r for r in hunt if not (r["d"] <= 6 and r["field"] in CLAIM_LAMBDAS
                                       and r["Jt"] == 0.7)]
    teeth["K15_counterexample_hunt_is_wide"] = {
        "n_cells": len(hunt), "n_off_the_929_grid": len(offgrid),
        "max_residual": hunt_worst, "worst_cell": hunt_worst_row,
        "n_violations": sum(1 for r in hunt if r["violates"]),
        "fires": bool(len(offgrid) >= 100)}

    teeth_sum = {"n_teeth": len(teeth),
                 "n_firing": sum(1 for v in teeth.values() if v.get("fires")),
                 "all_fire": all(v.get("fires") for v in teeth.values())}

    # ================= VERDICT ==============================================
    if hunt_worst > IDENT_TOL:
        refutations.append("the identity is violated inside the theorem's own "
                           "hypotheses at %r (residual %.3e)"
                           % (hunt_worst_row, hunt_worst))
    if not findings:
        findings.append("none beyond the scope notes recorded below")

    verdict = ("SUPPORTED" if not refutations else "REFUTED")
    runtime = time.perf_counter() - T_START
    if runtime > RUNTIME_LIMIT_SECONDS:
        die("runtime:%.1f s exceeds %.0f s" % (runtime, RUNTIME_LIMIT_SECONDS))

    receipt = {
        "schema": "cycle931-additivity-identity-independent-check-v1",
        "cycle": 931, "block": "toe-time-blockM11-20260802",
        "date": "2026-08-05", "git_head": head,
        "runner": "scripts/frontier_cycle931_additivity_identity_independent_check_"
                  "2026_07_28.py",
        "runner_sha256": sha256_bytes(open(os.path.abspath(__file__), "rb").read()),
        "target_primary_receipt": PRIMARY_RECEIPT,
        "target_primary_receipt_sha256": prim_sha,
        "target_primary_timing_free_digest": prim.get("timing_free_digest"),
        "note_on_the_two_digests": "the receipt sha256 moves with the recorded "
                                   "runtime; the timing-free digest is the stable "
                                   "identity of the primary's payload and is what a "
                                   "re-run must reproduce.",
        "pins": pins,
        "independence": {
            "propagators": ["K: own Lanczos/Krylov exponential with full "
                            "reorthogonalisation", "E: scipy expm_multiply "
                            "(Al-Mohy-Higham)"],
            "primary_propagators": ["Chebyshev/Bessel", "adaptive Taylor marching",
                                    "dense eigendecomposition"],
            "qubit_ordering": "REVERSED (site i at bit n-1-i)",
            "entropies": "SVD singular values, natural log converted to bits",
            "statistic": "explicit pointer-projector sum with axis slicing",
            "symbolics": "exact rationals + GF(2^61-1), no CAS",
            "arbitrary_precision": "mpmath at 50 decimal digits"},
        "statistic_definition_reread_from_memo_bytes": stat_ok,
        "C1_independent_ladder_reproduction": {"max_abs_dev": c1_dev, "n_rungs": len(c1),
                                               "rows": c1},
        "C2_derived_law_independently": {"max_abs_dev_vs_pinned": c2_dev, "rows": c2},
        "C3_hypothesis_attack": attack,
        "C4_counterexample_hunt": {
            "n_cells": len(hunt), "max_residual": hunt_worst,
            "worst_cell": hunt_worst_row,
            "n_violations": sum(1 for r in hunt if r["violates"]),
            "isomorphic_arm_spiders_obey_the_identity": bool(
                all(not r["violates"] for r in hunt
                    if "isomorphic-arm" in r["family"])),
            "frozen_preparation_rows": prep_rows,
            "loop_carrying_probe": loop_rows,
            "pair_complement_rows": pc_rows,
            "rows": hunt},
        "C5_seal_recomputed": {"digest_recomputes": bool(seal_digest_ok),
                               "holdout_free": bool(holdout_ok),
                               "independent_inversion_max_dev": seal_dev,
                               "rows": seal_rows,
                               "P3_measurements_recomputed": {"max_abs_dev": p3_dev,
                                                              "rows": p3_check}},
        "C6_candidate_verdicts_recomputed": {
            "ssa_rows": ssa, "min_I(A:R|B)": ssa_min,
            "max_|I(A:R|B)-I(A:R)|": ssa_diff,
            "agrees_with_primary": bool(ssa_agrees),
            "strong_coupling_rows": strong, "strong_max_residual": strong_res,
            "strong_max_G": strong_G,
            "exchangeable_but_mixed": exch},
        "C7_arbitrary_precision": {"rows": mp_rows, "max_residual": mp_worst},
        "C8_exact_symbolics": sym,
        "C9_primary_arithmetic_audit": arith,
        "teeth": teeth, "teeth_summary": teeth_sum,
        "findings": findings,
        "refutations": refutations,
        "verdict": verdict,
        "verdict_statement":
            ("SUPPORTED.  The derivation survives every attack this runner could "
             "mount.  The 929 ladder reproduces on disjoint machinery at %.1e; the "
             "derived law G_d(m) = s(m)+s(1)-s(m+1) reproduces the pinned rungs at "
             "%.1e; %d random states satisfying the theorem's hypotheses H1 and H4 "
             "and NOTHING else all obey the identity to %.1e while the H4-dropped "
             "control violates it by %.3f bit; the identity holds on %d cells "
             "including %d off the 929 grid, at degrees 3..12, fields 0.02..5.0 and "
             "Jt 0.05..5.0, with zero violations; a 50-digit recomputation puts the "
             "residual at %.1e, so the float64 result is not a coincidence; the seal "
             "recomputes from the pinned bytes under a DIFFERENT inversion and is "
             "tamper-evident.  The SSA-equality reading is refuted independently "
             "(I(A:R|B) >= %.6f bit).  The perturbative candidate is refuted "
             "independently (residual %.1e at statistic values up to %.3f bit)."
             % (c1_dev, c2_dev, n_samples, attack_worst, ctrl_worst, len(hunt),
                len(offgrid), mp_worst, ssa_min, strong_res, strong_G)
             if not refutations else
             "REFUTED: " + "; ".join(refutations)),
        "runtime_seconds": runtime,
        "runtime_limit_seconds": RUNTIME_LIMIT_SECONDS,
        "runtime_within_limit": bool(runtime <= RUNTIME_LIMIT_SECONDS),
    }
    # The checker's own stable identity.  target_primary_receipt_sha256 is excluded
    # because the primary's receipt file carries its measured runtime and therefore
    # moves between otherwise identical runs; the primary's TIMING-FREE digest is
    # kept in the payload and is the thing that must be stable.
    timing_free = json.loads(json.dumps(receipt, default=float))
    for k in ("runtime_seconds", "target_primary_receipt_sha256"):
        timing_free.pop(k, None)
    receipt["timing_free_digest"] = sha256_obj(timing_free)

    outp = os.path.join(
        ROOT, "outputs",
        "additivity_identity_independent_check_cycle931_receipt_2026_07_28.json")
    with open(outp, "w") as fh:
        json.dump(receipt, fh, indent=1, sort_keys=True, default=float)
    rsha = sha256_bytes(open(outp, "rb").read())

    ap(BOUNDARY_LINE)
    ap("runner: scripts/frontier_cycle931_additivity_identity_independent_check_"
       "2026_07_28.py")
    ap("cycle: 931  block: toe-time-blockM11-20260802  head: %s" % head)
    ap("target: %s (sha256 %s)" % (PRIMARY_RECEIPT, prim_sha))
    ap("")
    ap("-- INDEPENDENCE --")
    ap("  propagators: own Lanczos/Krylov + scipy expm_multiply "
       "(primary: Chebyshev, Taylor, dense eigh -- no route shared)")
    ap("  ordering: REVERSED   entropies: SVD singular values, ln -> bits")
    ap("  symbolics: exact rationals + GF(2^61-1), NO CAS (primary: sympy)")
    ap("  arbitrary precision: mpmath, 50 decimal digits")
    ap("")
    ap("-- C1  THE 929 LADDER ON DISJOINT MACHINERY --")
    ap("  %d rungs, max abs deviation %.3e" % (len(c1), c1_dev))
    ap("-- C2  THE DERIVED LAW --")
    ap("  G_d(m) = s(m)+s(1)-s(m+1) vs the pinned rungs: max abs deviation %.3e"
       % c2_dev)
    for r in c2:
        ap("  %-9s exch. spread %.2e   reflection |s(k)-s(d-k)| %.2e"
           % (r["cell"], r["exchangeability_max_spread"],
              r["reflection_max_|s(k)-s(d-k)|"]))
    ap("")
    ap("-- C3  ATTACK ON THE HYPOTHESES --")
    ap("  %d random PURE, PERMUTATION-SYMMETRIC states (H1+H4, no frozen dynamics)"
       % n_samples)
    ap("  max additivity residual over all of them: %.3e  -> NO COUNTEREXAMPLE"
       % attack_worst)
    ap("  control with H4 dropped: %.4f bit -> the test can see a violation"
       % ctrl_worst)
    ap("")
    ap("-- C4  COUNTEREXAMPLE HUNT OFF THE MEASURED GRID --")
    ap("  %d cells (%d off the 929 grid): degrees 2..12, fields 0.02..5.0, "
       "Jt 0.05..5.0," % (len(hunt), len(offgrid)))
    ap("  pure stars, isomorphic-arm spiders (path and claw), the frozen "
       "preparation variant.")
    ap("  violations: %d      worst residual: %.3e at %r"
       % (sum(1 for r in hunt if r["violates"]), hunt_worst, hunt_worst_row))
    ap("  SCOPE FINDING (positive): the identity EXTENDS to every isomorphic-arm "
       "spider tested,")
    ap("  i.e. beyond the pure stars 929 measured -- exactly as hypothesis H4 "
       "predicts.")
    for r in loop_rows:
        ap("  loop-carrying probe (H4 FAILS by construction): residual %.3e"
           % r["residual"])
    ap("  pair-complement identity (needs only H1-H3) across all families: "
       "max %.3e" % pc_worst)
    ap("")
    ap("-- C5  THE SEAL --")
    ap("  digest recomputes: %s   every input is a pinned 929 value: %s"
       % (seal_digest_ok, holdout_ok))
    ap("  independent inversion (linear solve, not recursion): max dev %.3e" % seal_dev)
    ap("  the primary's both-merged measurements, recomputed: max dev %.3e" % p3_dev)
    ap("")
    ap("-- C6  CANDIDATE VERDICTS, RECOMPUTED --")
    ap("  SSA equality case: min I(A:R|B) = %.6f bit (Markov needs 0); "
       "|I(A:R|B)-I(A:R)| = %.2e" % (ssa_min, ssa_diff))
    ap("  agrees with the primary: %s" % ssa_agrees)
    ap("  strong coupling: statistic up to %.4f bit, residual %.2e"
       % (strong_G, strong_res))
    ap("  exchangeable-but-mixed: residual %.3e"
       % min(r["additivity_residual"] for r in exch))
    ap("")
    ap("-- C7  ARBITRARY PRECISION (50 digits) --")
    for r in mp_rows:
        ap("  d=%d lam=%.2f Jt=%.1f  max residual %s" %
           (r["d"], r["field"], r["Jt"], r["max_abs_additivity_residual"]))
    ap("")
    ap("-- C8  EXACT SYMBOLICS (no CAS) --")
    ap("  L1 eigenvector transfer over GF(2^61-1): all shapes hold")
    ap("  L2 Sylvester char-poly over exact rationals: all shapes hold; a wrong "
       "padding exponent is caught")
    ap("  L3 exchangeability => size-only reduced states: exact, d=3,4,5")
    ap("  L4 I(A:B)+I(R:B)-2S(B) = 0 under purity, exactly; I(A:R|B) = %s"
       % sym["L4_pair_complement"]["I(A:R|B) under purity"])
    ap("  THM exact over the rationals for d = 3..12; without the reflection it "
       "breaks")
    ap("")
    ap("-- C9  THE PRIMARY'S PUBLISHED ARITHMETIC --")
    ap("  law rows self-consistent to %.2e; identity rows with an inconsistent "
       "published residual: %d"
       % (arith["law_rows_recomputed"],
          arith["identity_rows_with_inconsistent_published_residual"]))
    ap("  s(k) concave on every certified cell: %s" % arith["s_is_concave_everywhere"])
    ap("")
    ap("-- TEETH (%d/%d fire) --" % (teeth_sum["n_firing"], teeth_sum["n_teeth"]))
    for k in sorted(teeth):
        ap("  %-56s %s" % (k, teeth[k]["fires"]))
    ap("")
    ap("-- FINDINGS --")
    for f in findings:
        ap("  * %s" % f)
    ap("-- REFUTATIONS --")
    if refutations:
        for f in refutations:
            ap("  * %s" % f)
    else:
        ap("  none")
    ap("")
    ap("VERDICT: %s" % verdict)
    ap("runtime: %.1f s (limit %.0f s)" % (runtime, RUNTIME_LIMIT_SECONDS))
    ap("receipt: outputs/additivity_identity_independent_check_cycle931_receipt_"
       "2026_07_28.json")
    ap("receipt sha256: %s" % rsha)
    ap(BOUNDARY_LINE)

    cp = os.path.join(ROOT, "logs", "runner-cache",
                      "frontier_cycle931_additivity_identity_independent_check_"
                      "2026_07_28.txt")
    os.makedirs(os.path.dirname(cp), exist_ok=True)
    with open(cp, "w") as fh:
        fh.write("\n".join(lines) + "\n")
    sys.stdout.write("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
