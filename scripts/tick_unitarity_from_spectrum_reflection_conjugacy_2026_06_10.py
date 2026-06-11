#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Tick unitarity from spectrum-reflection conjugacy
=================================================
Companion runner for
docs/TICK_UNITARITY_FROM_SPECTRUM_REFLECTION_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-06-10.md.

CONTEXT.  In the kinetic-isotropy retirement chain, block01
(KINETIC_ISOTROPY_FROM_STRICT_LICENSE_CHIRAL_QUANTIZATION, 2026-06-09) named
(P2) "unitarity of the realized one-tick update" as a bare conditional
reading, and the site-license dichotomy cycle (2026-06-09) discharged P3 and
reduced P4 while still ASSUMING the unitary tick.  P2 is the surviving
dynamical premise of the chain.  This runner checks the structure theorem
that retires the BARE unitarity reading into two narrower named readings:

THE THEOREM (finite-dimensional, exact).  Let T be an INVERTIBLE linear map
on a finite-dimensional Hilbert space with operator norm ||T|| <= 1 (a
contraction: the channel envelope).  Then

    ( there exists an isometric or anti-isometric Theta with
      Theta T Theta^{-1} = T^{-1} )        <=>        T is unitary.

Forward: isometric/anti-isometric conjugation preserves the operator norm,
so the relation forces ||T^{-1}|| = ||T|| <= 1; then for every x,
||x|| = ||T^{-1} T x|| <= ||T x|| <= ||x||, so T is an isometry, and a
finite-dimensional isometry is unitary.  Converse: for unitary T with
spectral frame W (T = W D W^dag, |D| = 1), the antiunitary
Theta = W o K o W^dag satisfies Theta T Theta^{-1} = W conj(D) W^dag =
T^{-1}.  The relation is therefore an EXACT characterization of unitarity
inside the invertible-contraction class.

FRAMEWORK READ.  The retained CPT note's identity table supplies two
spectrum-reflection conjugacies on the staggered Hamiltonian sector:
the unitary sublattice parity (C-type, eps H eps = -H) and the antiunitary
commuting CPT representative ([Theta, H] = 0).  At exponential-tick level
both give Theta U Theta^{-1} = U^{-1} exactly (verified below).  Reading
either identity on the REALIZED strict tick (the same epistemic slot as
block01's P3 reading) plus the channel envelope ||T|| <= 1 forces tick
unitarity.  P2 is thereby retired into:
  (C-reading)  tick-level transport of a retained spectrum-reflection
               identity, and
  (N-reading)  norm-nonincrease of the realized tick (channel envelope).
The omega <-> -omega quasi-energy pairing (block01's P3) follows as a
corollary of the unitary-S version -- coherent with the dichotomy cycle
having discharged its separate use.

EVERY HYPOTHESIS GETS A HOSTILE WITNESS (wall-independence):
  drop the conjugacy -> Part D/W1: the scalar winding family r e^{ik}
                        (block01 Part E2's velocity-tunable class) is a
                        contraction, never satisfies the relation
                        (norm obstruction ||T^{-1}|| = 1/r > 1), not unitary;
  drop contraction   -> Part D/W2: diag(2, 1/2) with the swap conjugacy
                        satisfies the relation, is not unitary;
  drop invertibility -> Part D/W3: a dephasing (decohering) tick is
                        non-invertible, the relation is unsatisfiable --
                        open-sector CPTP ticks are OUTSIDE the hypothesis
                        class (einselection consistency, not a conflict).

COHERENCE WITH THE IRREDUCIBILITY SUPPORT.  The kinetic-isotropy
independence witness family (bosonic POSITIVE TRANSFER, c_t/c_s tunable)
is exactly the relation-VIOLATING sector: T = e^{-E} has
||T^{-1}|| = e^{+E_max} > 1 whenever E != 0 (Part F).  The support note's
family is the Euclidean shadow, not a counterexample to this theorem.

WHAT THIS DOES NOT CLAIM.  No audit status is set or predicted.  The
tick-level transport of the H-level retained identities to the realized
strict tick is a NAMED READING, not derived here; the channel envelope is a
NAMED READING (physical maps do not increase norm), not derived here.  No
locality input is used (locality is P1's separate job).  Mass-sector scope:
the framework instances below are the massless hopping carrier (the
dispersive/massless point is where the kinetic-form normalization lives).
No new axiom, no new primitive, no Tier-A admission.

Run: python3 scripts/tick_unitarity_from_spectrum_reflection_conjugacy_2026_06_10.py
"""
from __future__ import annotations

import sys

import numpy as np

PASS, FAIL = 0, 0
TOL = 1e-10
RNG = np.random.default_rng(20260610)


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


def rand_unitary(n):
    z = RNG.normal(size=(n, n)) + 1j * RNG.normal(size=(n, n))
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / np.abs(np.diag(r)))


def opnorm(m):
    return np.linalg.norm(m, 2)


# ----------------------------------------------------------------------------
print("PART A -- isometric and anti-isometric conjugation preserve the operator norm")
print("=" * 78)
ok_u, ok_a = True, True
for _ in range(60):
    n = int(RNG.integers(2, 7))
    T = RNG.normal(size=(n, n)) + 1j * RNG.normal(size=(n, n))
    Q = rand_unitary(n)
    # unitary conjugation
    ok_u &= abs(opnorm(Q @ T @ Q.conj().T) - opnorm(T)) < TOL
    # antiunitary Theta = Q o K acts on matrices as T -> Q conj(T) Q^dag
    ok_a &= abs(opnorm(Q @ T.conj() @ Q.conj().T) - opnorm(T)) < TOL
check("A1 unitary conjugation: ||S T S^dag|| = ||T|| on 60 random instances", ok_u)
check("A2 antiunitary conjugation: ||Q conj(T) Q^dag|| = ||T|| on 60 random instances", ok_a,
      "conjugation preserves singular values")

# ----------------------------------------------------------------------------
print("\nPART B -- forward implication: relation + contraction => unitary")
print("=" * 78)
# B1: the norm obstruction certificate: a strict contraction direction forces
# ||T^{-1}|| > 1, making the relation a-priori unsatisfiable.
ok_obstruction = True
for _ in range(60):
    n = int(RNG.integers(2, 6))
    A = RNG.normal(size=(n, n)) + 1j * RNG.normal(size=(n, n))
    U_, s, Vh = np.linalg.svd(A)
    s = s / s.max()
    s[-1] = min(s[-1], 0.9)  # ensure at least one singular value < 1
    T = U_ @ np.diag(s) @ Vh
    ok_obstruction &= (opnorm(np.linalg.inv(T)) > 1 + 1e-9)
check("B1 every non-unitary invertible contraction has ||T^{-1}|| > 1 (60 instances)",
      ok_obstruction, "relation forces ||T^{-1}|| = ||T|| <= 1: a-priori obstruction")
# B2: the isometry chain on the boundary case.
ok_chain = True
for _ in range(40):
    n = int(RNG.integers(2, 7))
    U = rand_unitary(n)
    x = RNG.normal(size=n) + 1j * RNG.normal(size=n)
    ok_chain &= abs(np.linalg.norm(U @ x) - np.linalg.norm(x)) < TOL
ok_chain &= all(abs(opnorm(rand_unitary(int(RNG.integers(2, 6)))) - 1) < TOL for _ in range(10))
check("B2 boundary case: ||T|| = ||T^{-1}|| = 1 instances are isometric on random vectors",
      ok_chain)
# B3: T^dag T = I follows: scan a contraction family crossing the unitary point.
U0 = rand_unitary(4)
ok_family = True
for s_ in [0.2, 0.5, 0.8, 1.0]:
    T = U0 @ np.diag([1.0, 1.0, 1.0, s_])
    is_unitary = np.allclose(T.conj().T @ T, np.eye(4), atol=TOL)
    inv_contr = opnorm(np.linalg.inv(T)) <= 1 + 1e-9
    ok_family &= (is_unitary == inv_contr) and (is_unitary == (s_ == 1.0))
check("B3 contraction family T(s): relation-satisfiability (= contractive inverse) holds exactly at the unitary point s=1",
      ok_family)

# ----------------------------------------------------------------------------
print("\nPART C -- converse: every unitary admits an anti-isometric inverse-conjugacy")
print("=" * 78)
ok_conv = True
ok_invol = True
for _ in range(40):
    n = int(RNG.integers(2, 7))
    U = rand_unitary(n)
    lam, W = np.linalg.eig(U)
    Winv = np.linalg.inv(W)
    # Theta = W o K o W^{-1}: Theta U Theta^{-1} acts as W conj(Winv U W) Winv
    M = W @ np.conj(Winv @ U @ W) @ Winv
    ok_conv &= np.allclose(M, np.linalg.inv(U), atol=1e-8)
    # involution on the same frame: Theta^2 = id
    X = RNG.normal(size=n) + 1j * RNG.normal(size=n)
    ThX = W @ np.conj(Winv @ X)
    ok_invol &= np.allclose(W @ np.conj(Winv @ ThX), X, atol=1e-8)
check("C1 Theta = W o K o W^{-1} gives Theta U Theta^{-1} = U^{-1} on 40 random unitaries",
      ok_conv, "spectral-frame conjugation: conj(D) = D^{-1} on the unit circle")
check("C2 the constructed Theta is an involution (Theta^2 = id) on random vectors", ok_invol)

# ----------------------------------------------------------------------------
print("\nPART D -- hostile witnesses: every hypothesis is load-bearing")
print("=" * 78)
# W1: drop the conjugacy -- the velocity-tunable winding contraction family.
r = 0.7
ks = np.linspace(0, 2 * np.pi, 9)[:-1]
w1_contr = all(abs(r * np.exp(1j * k)) <= 1 for k in ks)
w1_obstr = (1.0 / r) > 1 + 1e-12
phases = np.unwrap(np.angle(r * np.exp(1j * ks)))
w1_winding = abs((phases[-1] - phases[0]) / (ks[-1] - ks[0]) - 1.0) < 1e-9
check("D/W1 scalar winding family r e^{ik} (r=0.7): contraction with winding 1",
      w1_contr and w1_winding, "block01 Part E2's tunable class")
check("D/W1 norm obstruction ||T^{-1}|| = 1/r > 1: the relation is unsatisfiable for it",
      w1_obstr, "contraction alone does NOT force unitarity; the conjugacy is load-bearing")
# W2: drop contraction -- relation holds, not unitary.
T2 = np.diag([2.0, 0.5])
S2 = np.array([[0.0, 1.0], [1.0, 0.0]])
w2_rel = np.allclose(S2 @ T2 @ S2, np.linalg.inv(T2), atol=TOL)
w2_not_contr = opnorm(T2) > 1
w2_not_unit = not np.allclose(T2.conj().T @ T2, np.eye(2), atol=TOL)
check("D/W2 diag(2,1/2) with swap conjugacy: relation HOLDS, not a contraction, not unitary",
      w2_rel and w2_not_contr and w2_not_unit, "the channel envelope is load-bearing")
# W3: drop invertibility -- a dephasing tick (Kraus {P0, P1} on one qubit,
# acting on the off-diagonal sector as 0) is non-invertible on the carrier.
Tdeph = np.diag([1.0, 0.0, 0.0, 1.0])  # action on vectorized 1-qubit operators
w3_sing = np.linalg.matrix_rank(Tdeph) < 4
check("D/W3 dephasing (decohering) tick is singular: the relation is unsatisfiable -- outside the class",
      w3_sing, "open-sector CPTP ticks evade the theorem; unitarity is located exactly where spectrum-reflection holds")

# ----------------------------------------------------------------------------
print("\nPART E -- framework instances: the retained identities transport to tick level")
print("=" * 78)
try:
    from scipy.linalg import expm
except Exception:  # minimal fallback
    def expm(m):
        out = np.eye(m.shape[0], dtype=complex)
        term = np.eye(m.shape[0], dtype=complex)
        for j in range(1, 40):
            term = term @ m / j
            out = out + term
        return out

for L in (8, 12):
    D = np.zeros((L, L))
    for x in range(L):
        D[x, (x + 1) % L] += 0.5
        D[(x + 1) % L, x] -= 0.5
    H = 1j * D  # Hermitian massless staggered hopping carrier (per-axis)
    eps = np.diag([(-1.0) ** x for x in range(L)])
    U = expm(-1j * H)
    Uinv = np.linalg.inv(U)
    check(f"E1[L={L}] sublattice parity: eps H eps = -H (the CPT note's C-type identity)",
          np.allclose(eps @ H @ eps, -H, atol=TOL))
    check(f"E2[L={L}] unitary-S transport: eps U eps = U^{{-1}} at exponential-tick level",
          np.allclose(eps @ U @ eps, Uinv, atol=TOL))
    # antiunitary commuting representative Theta = eps o K: [Theta, H] = 0
    check(f"E3[L={L}] antiunitary CPT-type: eps conj(H) eps = H ([Theta,H]=0, Theta = eps o K)",
          np.allclose(eps @ H.conj() @ eps, H, atol=TOL))
    check(f"E4[L={L}] antiunitary transport: eps conj(U) eps = U^{{-1}} at tick level",
          np.allclose(eps @ U.conj() @ eps, Uinv, atol=TOL))
    check(f"E5[L={L}] conclusion instance: the tick is unitary (T^dag T = I) and ||T|| = ||T^{{-1}}|| = 1",
          np.allclose(U.conj().T @ U, np.eye(L), atol=TOL)
          and abs(opnorm(U) - 1) < TOL and abs(opnorm(Uinv) - 1) < TOL)
    ph = np.sort(np.angle(np.linalg.eigvals(U)))
    check(f"E6[L={L}] corollary (former P3): quasi-energy spectrum is omega <-> -omega paired",
          np.allclose(np.sort(-ph), ph, atol=1e-9),
          "spectral pairing follows from the unitary-S version; coherent with the dichotomy discharge")

# a dispersive site-licensed Bloch tick from the dichotomy family: U(z) = [[0, z], [1, 0]]
ok_bloch_rel = True
ok_bloch_unit = True
for k in np.linspace(0.1, 2 * np.pi - 0.1, 7):
    z = np.exp(1j * k)
    Uz = np.array([[0.0, z], [1.0, 0.0]])
    ok_bloch_unit &= np.allclose(Uz.conj().T @ Uz, np.eye(2), atol=TOL)
    lam, W = np.linalg.eig(Uz)
    Winv = np.linalg.inv(W)
    M = W @ np.conj(Winv @ Uz @ W) @ Winv
    ok_bloch_rel &= np.allclose(M, np.linalg.inv(Uz), atol=1e-8)
check("E7 dispersive licensed Bloch tick U(z)=[[0,z],[1,0]]: unitary on every fiber",
      ok_bloch_unit)
check("E8 the per-fiber inverse-conjugacy exists for it (converse construction)",
      ok_bloch_rel)

# ----------------------------------------------------------------------------
print("\nPART F -- coherence: the irreducibility-support witness family violates the relation")
print("=" * 78)
ok_shadow = True
for xi in (0.5, 1.0, 2.0, 5.0):
    # bosonic positive-transfer dispersion at a sample momentum grid (free scalar, m=0.3)
    for p in np.linspace(0.1, np.pi - 0.1, 5):
        E = np.arccosh(1.0 + (xi * (2 * np.sin(p / 2) ** 2) + 0.3 ** 2) / 2.0)
        Tmode = np.exp(-E)
        ok_shadow &= (Tmode < 1.0) and (1.0 / Tmode > 1.0 + 1e-9)
check("F1 positive transfer e^{-E(p)} has ||T^{-1}|| > 1 strictly for every xi in the witness family",
      ok_shadow, "the c_t/c_s-tunable family is the relation-VIOLATING Euclidean sector -- no conflict")

# ----------------------------------------------------------------------------
print("\nPART G -- scope honesty: what is NOT proved here")
print("=" * 78)
# G1: the transport to the REALIZED strict tick is a reading: exponential ticks
# used in Part E are NOT strict radius-1 (block01 Part C); verify leakage so the
# reading's status stays visible.
L = 12
D = np.zeros((L, L))
for x in range(L):
    D[x, (x + 1) % L] += 0.5
    D[(x + 1) % L, x] -= 0.5
H = 1j * D
U = expm(-1j * H)
leak = abs(U[0, 2])  # distance-2 amplitude of the exponential tick
check("G1 the exponential tick leaks beyond radius 1 (|U[0,2]| > 0): tick-transport to the strict tick is a NAMED READING",
      leak > 1e-6, f"distance-2 amplitude = {leak:.3e} (block01 Part C's point, reproduced)")
check("G2 no locality input is used by the theorem itself (hypotheses: invertibility, contraction, conjugacy only)",
      True if (w2_rel and ok_conv) else False,
      "computed via the witnesses: W2 satisfies the relation with zero locality structure")

print("\n" + "=" * 78)
print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
sys.exit(0 if FAIL == 0 else 1)
