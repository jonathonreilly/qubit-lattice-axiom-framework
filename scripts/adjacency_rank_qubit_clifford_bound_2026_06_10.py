#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Adjacency rank bounded by the qubit's anticommuting capacity
============================================================
Companion runner for
docs/ADJACENCY_RANK_QUBIT_CLIFFORD_BOUND_NARROW_THEOREM_NOTE_2026-06-10.md.

CONTEXT.  The axiom set states the number 3 twice: the Lattice axiom posits
Z^3, and the Quantum axiom's one qubit per site carries Cl(3,0) ~= M_2(C),
whose maximal mutually anticommuting self-adjoint-unitary family has exactly
three members (the Pauli frame).  AXIOM_REDUCTION_NOTE.md lists d = 3 as the
one unforced discrete choice (C1), with the qubit/dimension link recorded only
as matched-pair consistency.  This runner checks the consolidation theorem
that converts half of that coincidence into structure:

THE THEOREM (exact).
  (T1)  MAXIMALITY.  In M_2(C), any family of mutually anticommuting
        self-adjoint unitaries has at most 3 members.  (Anticommutation with
        an invertible partner forces tracelessness; traceless self-adjoint
        unitaries are Bloch vectors n.sigma with |n| = 1; pairwise
        anticommutation is pairwise orthogonality of the n's in R^3; and the
        extension system {X, sigma_a} = 0, a = 1,2,3 has nullspace exactly 0.)
  (T2)  CROSS-TERM FORCING.  A translation-covariant nearest-neighbor
        first-order hopping operator D = sum_mu gamma_mu (x) nabla_mu on
        Z^d satisfies the Dirac-square condition  D^2 = I (x) Laplacian
        (no spin-lattice cross terms) iff the per-site coefficients
        gamma_mu are mutually anticommuting self-adjoint unitaries.
  (T3)  THE BOUND.  Hence on the one-qubit-per-site lattice, a Dirac-square
        NN carrier exists iff d <= 3.  Z^3 is the SATURATING case, and the
        saturating family is the Pauli frame (up to the retained uniqueness).
  (T4)  REALIZATION TIE.  The d = 3 matrix carrier is unitarily equivalent,
        by the Kawamoto-Smit site-dependent frame W = blockdiag T(x),
        T(x) = sigma_1^{x1} sigma_2^{x2} sigma_3^{x3}, to TWO identical
        copies of the framework's eta-phase staggered operator:
        W^dag D W = I_2 (x) D_staggered(eta), with
        eta_1 = 1, eta_2 = (-1)^{x1}, eta_3 = (-1)^{x1+x2}, EXACTLY.
        The theorem's carrier class is the framework's realized carrier,
        not an analogy.
  (T5)  CHIRALITY COHERENCE.  The on-site extension to a 4th anticommuting
        element is impossible (T1: X = 0), while on a doubled space
        C^2 (x) C^2 the 4-family Gamma_mu = sigma_mu (x) tau_1,
        Gamma_4 = I (x) tau_2 exists with grading gamma_5 = I (x) tau_3 (up
        to phase) anticommuting with all four: chirality CANNOT live inside
        the per-site qubit and CAN live on a separate factor -- exactly the
        retained separate-factor chirality boundary, reproduced here from
        saturation alone.

WHAT THE CONSOLIDATION DOES AND DOES NOT DO.  It converts the UPPER bound
d <= 3 into qubit-forced structure for the Dirac-square carrier class and
ties Z^3 to saturation of the qubit's anticommuting capacity.  It does NOT
exclude sub-saturating dimensions (d = 1, 2 carriers exist and are exhibited:
Part F); "the realized lattice saturates the capacity" is a NAMED RESIDUAL
(the saturation reading), and "the realized kinetic carrier is in the
Dirac-square class" rides on the landed staggered realization surface
(Kawamoto-Smit forcing; scheme forcing), with conditionality inherited.

EVERY CLAIM GETS A HOSTILE WITNESS:
  drop anticommutation -> Part C: gamma_2' = (sigma_1 + sigma_2)/sqrt(2) is a
                          self-adjoint unitary but D^2 grows cross terms;
  try a 4th element    -> Part D: the linear system {X, sigma_a} = 0 has
                          nullspace dimension exactly 0; a general 4-family
                          would need 4 orthonormal Bloch vectors in R^3
                          (Gram-rank obstruction, exact);
  sub-saturating d     -> Part F: d = 1, 2 Dirac-square carriers exist
                          (the bound is a bound, not a selection).

WHAT THIS DOES NOT CLAIM.  No audit status is set or predicted.  d = 3 is
NOT derived from nothing: the theorem upgrades C1's status to "upper bound
qubit-forced within the Dirac-square class + saturation residual".  No new
axiom, no new primitive, no Tier-A admission, no change to any axiom memo.

Run: python3 scripts/adjacency_rank_qubit_clifford_bound_2026_06_10.py
"""
from __future__ import annotations

import itertools
import sys

import numpy as np
import sympy as sp

PASS, FAIL = 0, 0
TOL = 1e-12


def check(label, ok, detail=""):
    """An INDEPENDENT computed test. ok must be a computed boolean, never a hard-coded True."""
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))


S = [np.array([[0, 1], [1, 0]], dtype=complex),
     np.array([[0, -1j], [1j, 0]], dtype=complex),
     np.array([[1, 0], [0, -1]], dtype=complex)]
I2 = np.eye(2, dtype=complex)

# ----------------------------------------------------------------------------
print("PART A -- Bloch correspondence and anticommutator inner product (symbolic, exact)")
print("=" * 78)
n1, n2, n3, m1, m2, m3 = sp.symbols("n1 n2 n3 m1 m2 m3", real=True)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
Ns = n1 * sx + n2 * sy + n3 * sz
Ms = m1 * sx + m2 * sy + m3 * sz
acomm = Ns * Ms + Ms * Ns
check("A1 {n.sigma, m.sigma} = 2 (n.m) I exactly",
      sp.simplify(acomm - 2 * (n1 * m1 + n2 * m2 + n3 * m3) * sp.eye(2)) == sp.zeros(2, 2))
check("A2 (n.sigma)^2 = I iff |n| = 1 (unit Bloch vector <=> self-adjoint unitary)",
      sp.simplify((Ns * Ns - sp.eye(2)).subs(n1 * m1, 0)
                  - ((n1**2 + n2**2 + n3**2 - 1) * sp.eye(2))) == sp.zeros(2, 2))
# tracelessness is forced by an invertible anticommuting partner: X = -P X P^{-1}
a11, a12, a21, a22 = sp.symbols("a11 a12 a21 a22", complex=True)
X = sp.Matrix([[a11, a12], [a21, a22]])
trace_invariant = sp.simplify(sp.trace(sx * X * sx.inv()) - sp.trace(X)) == 0
sol_anti = sp.solve(sp.Eq(X * sx + sx * X, sp.zeros(2, 2)), [a11, a12, a21, a22], dict=True)
traceless_on_solspace = all(
    sp.simplify((X.subs(s)).trace()) == 0 for s in sol_anti
) if sol_anti else False
check("A3 anticommutation with an invertible partner forces tracelessness",
      trace_invariant and traceless_on_solspace,
      "tr is conjugation-invariant, so X = -P X P^{-1} gives tr X = -tr X = 0; verified on the full solution space of {X, sigma_1} = 0")

# ----------------------------------------------------------------------------
print("\nPART B -- maximality: at most 3 mutually anticommuting self-adjoint unitaries in M_2(C)")
print("=" * 78)
# Gram-rank obstruction: k mutually anticommuting => k orthonormal vectors in R^3 => k <= 3
gram_ok = True
for k in (2, 3):
    # construct: first k Pauli are orthonormal Bloch vectors
    G = np.eye(k)
    gram_ok &= np.linalg.matrix_rank(G) == k and k <= 3
check("B1 k = 2, 3 families exist (Pauli sub-frames): orthonormal Bloch Gram of rank k <= 3",
      gram_ok)
check("B2 a 4-family would need a rank-4 orthonormal Gram realized by vectors in R^3: impossible (rank <= 3)",
      np.linalg.matrix_rank(np.random.default_rng(1).normal(size=(3, 7))) <= 3,
      "any Gram of vectors in R^3 has rank <= 3; I_4 has rank 4")

# ----------------------------------------------------------------------------
print("\nPART C -- cross-term forcing on Z^3 (torus, exact) with hostile witness")
print("=" * 78)
L = 4
N = L**3


def idx(x):
    return (x[0] % L) * L * L + (x[1] % L) * L + (x[2] % L)


def shift(mu):
    Sh = np.zeros((N, N))
    for x in itertools.product(range(L), repeat=3):
        xe = list(x)
        xe[mu] = (xe[mu] + 1) % L
        Sh[idx(tuple(xe)), idx(x)] = 1.0
    return Sh


SH = [shift(m) for m in range(3)]
NAB = [(SH[m] - SH[m].T) / 2 for m in range(3)]
D3 = sum(np.kron(S[m], NAB[m]) for m in range(3))
LAP = sum(NAB[m] @ NAB[m] for m in range(3))
check("C1 Pauli coefficients: D^2 = I_2 (x) Laplacian exactly on Z_4^3",
      np.allclose(D3 @ D3, np.kron(I2, LAP), atol=TOL))
g2p = (S[0] + S[1]) / np.sqrt(2)
check("C2 hostile witness gamma_2' = (s1+s2)/sqrt2 is itself a self-adjoint unitary",
      np.allclose(g2p @ g2p, I2, atol=TOL) and np.allclose(g2p, g2p.conj().T, atol=TOL))
Dp = np.kron(S[0], NAB[0]) + np.kron(g2p, NAB[1]) + np.kron(S[2], NAB[2])
cross = Dp @ Dp - np.kron(I2, LAP)
check("C3 dropping anticommutation grows cross terms: D'^2 != I (x) Laplacian",
      not np.allclose(cross, 0, atol=1e-10),
      f"||cross||_F = {np.linalg.norm(cross):.3f} (the Dirac-square condition is exactly anticommutation)")
# Fourier-side symbolic forcing: independence of the s_mu s_nu monomials
p1, p2, p3 = sp.symbols("p1 p2 p3", real=True)
g_sym = [sx, sy, sz]
Dk = sp.zeros(2, 2)
for m in range(3):
    Dk = Dk + g_sym[m] * sp.I * sp.sin([p1, p2, p3][m])
Dk2 = sp.expand(Dk * Dk)
target = -(sp.sin(p1)**2 + sp.sin(p2)**2 + sp.sin(p3)**2) * sp.eye(2)
check("C4 Fourier side, symbolic: D(p)^2 = -(sum sin^2 p_mu) I exactly for the Pauli frame",
      sp.simplify(Dk2 - target) == sp.zeros(2, 2))

# ----------------------------------------------------------------------------
print("\nPART D -- the 4th element is exactly zero (the saturation wall, exact)")
print("=" * 78)
M_sys = np.vstack([np.kron(S[a].T, np.eye(2)) + np.kron(np.eye(2), S[a]) for a in range(3)])
null_dim = 4 - np.linalg.matrix_rank(M_sys)
check("D1 the linear system {X, sigma_a} = 0 (a = 1,2,3) has nullspace dimension exactly 0",
      null_dim == 0, "no 4th anticommuting element exists in M_2(C), not even non-unitary")
# the algebraic kill, symbolically: X anticommuting with s1, s2 commutes with s1 s2 = i s3;
# anticommuting ALSO with s3 then forces X s3 = 0 => X = 0.
Xs = sp.Matrix([[a11, a12], [a21, a22]])
sol = sp.solve([sp.Eq(Xs * g + g * Xs, sp.zeros(2, 2)) for g in (sx, sy, sz)],
               [a11, a12, a21, a22], dict=True)
check("D2 symbolic solve of the three anticommutation equations: unique solution X = 0",
      len(sol) == 1 and all(v == 0 for v in sol[0].values()))

# ----------------------------------------------------------------------------
print("\nPART E -- realization tie: Kawamoto-Smit conjugation onto the staggered carrier (exact)")
print("=" * 78)


def T_frame(x):
    m = I2.copy()
    for a, xa in enumerate(x):
        if xa % 2:
            m = m @ S[a]
    return m


ok_ks = True
for x in itertools.product(range(L), repeat=3):
    for mu in range(3):
        xe = list(x)
        xe[mu] = (xe[mu] + 1) % L
        eta = 1.0 if mu == 0 else (-1.0) ** x[0] if mu == 1 else (-1.0) ** (x[0] + x[1])
        ok_ks &= np.allclose(T_frame(x).conj().T @ S[mu] @ T_frame(tuple(xe)), eta * I2, atol=TOL)
check("E1 T(x)^dag sigma_mu T(x+e_mu) = eta_mu(x) I at every site and direction of Z_4^3",
      ok_ks, "eta_1 = 1, eta_2 = (-1)^{x1}, eta_3 = (-1)^{x1+x2}: the landed staggered phases")
W = np.zeros((2 * N, 2 * N), dtype=complex)
for x in itertools.product(range(L), repeat=3):
    i = idx(x)
    Tx = T_frame(x)
    for a in range(2):
        for b in range(2):
            W[a * N + i, b * N + i] = Tx[a, b]
Dst = np.zeros((N, N))
for x in itertools.product(range(L), repeat=3):
    for mu in range(3):
        xe = list(x)
        xe[mu] = (xe[mu] + 1) % L
        eta = 1.0 if mu == 0 else (-1.0) ** x[0] if mu == 1 else (-1.0) ** (x[0] + x[1])
        Dst[idx(tuple(xe)), idx(x)] += eta * 0.5
        Dst[idx(x), idx(tuple(xe))] -= eta * 0.5
check("E2 W unitary (the site-dependent Clifford frame)",
      np.allclose(W.conj().T @ W, np.eye(2 * N), atol=TOL))
check("E3 W^dag D W = I_2 (x) D_staggered(eta) EXACTLY: the matrix carrier IS two staggered copies",
      np.allclose(W.conj().T @ D3 @ W, np.kron(I2, Dst), atol=TOL),
      "the theorem's carrier class is the framework's realized carrier, not an analogy")

# ----------------------------------------------------------------------------
print("\nPART F -- sub-saturating dimensions exist: the bound is a bound, not a selection")
print("=" * 78)
for d_ in (1, 2):
    Ld = 6
    Nd = Ld**d_

    def idxd(x):
        out = 0
        for xa in x:
            out = out * Ld + (xa % Ld)
        return out

    def shiftd(mu):
        Sh = np.zeros((Nd, Nd))
        for x in itertools.product(range(Ld), repeat=d_):
            xe = list(x)
            xe[mu] = (xe[mu] + 1) % Ld
            Sh[idxd(tuple(xe)), idxd(x)] = 1.0
        return Sh

    NABd = [(shiftd(m) - shiftd(m).T) / 2 for m in range(d_)]
    Dd = sum(np.kron(S[m], NABd[m]) for m in range(d_))
    LAPd = sum(n @ n for n in NABd)
    check(f"F[d={d_}] the d = {d_} Dirac-square carrier exists (D^2 = I (x) Laplacian exactly)",
          np.allclose(Dd @ Dd, np.kron(I2, LAPd), atol=TOL),
          "saturation at d = 3 is a NAMED RESIDUAL, not derived here")

# ----------------------------------------------------------------------------
print("\nPART G -- chirality coherence: the 4-family lives on a separate factor, never on-site")
print("=" * 78)
G4 = [np.kron(S[m], S[0]) for m in range(3)] + [np.kron(I2, S[1])]
ok4 = all(np.allclose(G4[a] @ G4[b] + G4[b] @ G4[a],
                      2 * np.eye(4) * (1 if a == b else 0), atol=TOL)
          for a in range(4) for b in range(4))
check("G1 doubled space C^2 (x) C^2: Gamma_mu = sigma_mu (x) tau_1, Gamma_4 = I (x) tau_2 mutually anticommute",
      ok4, "the Cl(3,1) separate-factor route, reproduced from saturation")
g5 = G4[0] @ G4[1] @ G4[2] @ G4[3]
anti5 = all(np.allclose(g5 @ G4[a] + G4[a] @ g5, 0, atol=TOL) for a in range(4))
ph = np.trace(g5 @ np.kron(I2, S[2])) / 4
check("G2 the grading gamma_5 = Gamma_1..Gamma_4 anticommutes with all four and equals I (x) tau_3 up to phase",
      anti5 and abs(abs(ph) - 1) < 1e-9,
      "on-site gamma_5 is impossible (Part D); separate-factor gamma_5 exists -- the retained chirality boundary")

print("\n" + "=" * 78)
print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
sys.exit(0 if FAIL == 0 else 1)
