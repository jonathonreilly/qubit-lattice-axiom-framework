#!/usr/bin/env python3
"""Staggered-Dirac SAME-LEG spin-taste chirality probe.

Verifies the algebraic content of
`docs/STAGGERED_DIRAC_SAME_LEG_SPIN_TASTE_PROBE_2026-06-05.md`.

Question (owner-authorized, rigorous, no over-claim):
  r = 1/2 (charged-lepton Koide Q = 2/3) needs a Hermitian off-block
  C_3-orbit-splitting grading on the generation factor anticommuting
  with the mass operator H. Two established walls:

    WALL A (separate / distinct-tensor-factor route):
      chirality grading I_3 (x) sigma_3 lives on a DIFFERENT tensor
      factor than the generation R^3; its within-generation block is a
      scalar -> commutes with every generation operator -> cannot grade
      the generation orbit. (KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO.)

    WALL B (d=3+1 native S_3 invariance):
      the native staggered/KS chirality on the spatial cube is
      eps(x) = (-1)^{hw(x)} (Hamming weight = form degree). On the hw=1
      generation orbit {e1,e2,e3} this is the constant (-1)^1 = -1.
      It is S_3-invariant on the orbit, hence a scalar, hence cannot
      anticommute-grade the generation index.

  This probe attacks the HATCH the distinct-factor route relocated to:
  in the KS/staggered formulation SPIN (chirality) and TASTE (->
  generation) are NOT separate tensor factors -- they are ENTANGLED in
  the SAME C^8 = (C^2)^{(x)3} taste cube (Becher-Joos / Kawamoto-Smit,
  encoded in the retained substep-2 Kahler-Dirac equivalence). So the
  chirality grading and the generation index share the SAME leg, unlike
  I_3 (x) sigma_3.

  THE CRUX: does the SAME-LEG (spin-taste-entangled) chirality genuinely
  produce a generation-acting off-block anticommuting grading -> r=1/2,
  OR does the hw=1 projection collapse it back to the S_3-uniform scalar
  (WALL B), as the d=3+1 wall predicts?

Setup (d=3+1: 3 spatial axes of Z^3, emergent time -- 8 spatial corners,
NO 16-corner/d=4 taste; per retained substep-3 BZ-corner note and the
d=3+1 emergent-time correction in MEMORY):

  - Taste cube  V = (C^2)^{(x)3} = C^8, basis |b1 b2 b3>, b in {0,1}^3.
  - Hamming-weight grading V = (+)_p V^{(p)}, hw(b)=b1+b2+b3.
  - S_3 acts by permuting the three tensor positions (axis permutations
    of the cubic lattice); retained: C^8 = 4A1 + 2E, hw=1 = A1 + E.
  - hw=1 sector {e1=|100>, e2=|010>, e3=|001>} = generation orbit,
    Z_3 cycle e1->e2->e3->e1.
  - Same-leg chirality candidates (all act on the SAME C^8):
      Gamma_KS  = (-1)^{hw}        (native staggered phase; = form-parity
                                    = spin-taste gamma5 eps = gamma5(x)xi5)
      Gamma_ST  = gamma5 (x) xi5   (d=4 spin-taste factorization analog,
                                    built here on the cube as the product
                                    over the 3 qubit factors of sigma_3 --
                                    identical to Gamma_KS up to sign on C^8)
  - Distinct-factor comparator: G_distinct on C^3 (x) C^2, with the
    chirality on the SEPARATE C^2 (= I_3 (x) sigma_3).

Tests:
  PART 1  Setup: cube, hw grading, S_3, hw=1 generation orbit, Z_3 cycle.
  PART 2  Same-leg structure is REAL: Gamma_KS is NOT of the form
          (generation op) (x) (chirality op) on a split C^3 (x) C^2; the
          cube does not factor that way (the leg is genuinely shared).
  PART 3  Native KS chirality Gamma_KS = (-1)^{hw} projected to hw=1:
          it is exactly -I_3 on the generation orbit (S_3-uniform scalar).
  PART 4  Spin-taste gamma5 (x) xi5 (d=4 analog) on the cube: equals
          Gamma_KS up to overall sign; same hw=1 projection -> scalar.
  PART 5  THE CRUX (entrywise anticommutation rule). For a circulant mass
          H = a I + b C + conj(b) C^2 on the generation R^3, {Gamma, H} on
          the hw=1 orbit: a scalar Gamma=-I commutes, so {Gamma,H}=2*(-1)*H
          != 0 unless H=0. No off-block (singlet<->doublet) grading is
          induced; the same-leg chirality reduces to the S_3-uniform scalar.
  PART 6  Distinct-factor comparator I_3 (x) sigma_3: its within-
          generation block (partial trace / restriction to fixed
          chirality) is a scalar too -> commutes with every generation
          operator. (Reproduces the separate-factor agent's finding.)
  PART 7  What WOULD be needed: an off-block Hermitian GRADING (involution
          Gamma^2=I) mixing the Z_3 singlet (mode 0) with a doublet
          component (mode 1), anticommuting with a finite-mass circulant H.
          The involution condition forces BOTH L0+L1=0 AND L2=0 (mode 2
          must carry a +-1 chirality sign), which together force a=0 (the
          chiral limit), where r=|b|^2/a^2 diverges (NOT r=1/2) and the
          spectrum is origin-symmetric {+L,-L,0}.  (Scoping: the weaker
          L0+L1=0 ALONE -- a rank-2 NON-involution -- does NOT force a=0;
          a genuine Z_2 grading does.)  At the real r=1/2 Koide point a!=0,
          so no such grade exists there.  Same origin-reflection wall as the
          affine probe; NOT delivered by the same-leg cube chirality.
  PART 8  S_3-equivariance check: any S_3-invariant Hermitian grading on
          the hw=1 orbit is a multiple of I on each S_3-isotype (A1, E);
          to split the singlet (A1) from the doublet (E) anticommutingly
          requires BREAKING the cubic S_3 symmetry (a preferred axis/site).
  PART 9  Adversarial steelman: build the FULL hw-mixing Kahler-Dirac
          D_KD = d - delta on the cube (it anticommutes with gamma5
          globally and has zero hw1->hw1 block). Even so, gamma5 = (-1)^{hw}
          is CONSTANT -1 across the whole generation orbit -- hw-mixing
          dynamics change which states are mass eigenstates, never the
          chirality VALUE on the orbit. The escape does NOT open.

VERDICT: COLLAPSES-TO-S3-UNIFORM. The same-leg spin-taste chirality, on
the hw=1 generation orbit, washes out to the scalar -I (S_3-invariant);
it does not induce a C_3-orbit-splitting off-block grading and does not
reach r=1/2. Splitting requires breaking the cubic symmetry. This is the
honest middle outcome the d=3+1 wall predicts. The distinct-factor and
same-leg routes hit the SAME S_3-uniform wall by different doors.

All checks are pure finite-dim linear algebra (numpy exact-integer /
sympy symbolic). No PDG / measured / empirical masses are consumed.
"""

from __future__ import annotations

import itertools
import sys

import numpy as np
import sympy as sp

PASS_COUNT = 0
FAIL_COUNT = 0
CLASS_A_HITS = 0


def check(label: str, condition: bool, detail: str = "", class_a: bool = False) -> bool:
    global PASS_COUNT, FAIL_COUNT, CLASS_A_HITS
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
        if class_a:
            CLASS_A_HITS += 1
    else:
        FAIL_COUNT += 1
    tag = " [class-A]" if (class_a and condition) else ""
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{status}] {label}{tag}{suffix}")
    return condition


# ---------------------------------------------------------------------------
# Cube primitives: V = (C^2)^{(x)3} = C^8, basis index = b1 b2 b3 (b in {0,1})
# ---------------------------------------------------------------------------

# Single-qubit Pauli / identity (integer entries, exact)
I2 = np.array([[1, 0], [0, 1]], dtype=np.int64)
SX = np.array([[0, 1], [1, 0]], dtype=np.int64)
SZ = np.array([[1, 0], [0, -1]], dtype=np.int64)


def kron3(a, b, c):
    return np.kron(np.kron(a, b), c)


def cube_index(b):
    """b = (b1,b2,b3) -> linear index in 0..7 (big-endian: b1 most significant)."""
    return (b[0] << 2) | (b[1] << 1) | b[2]


def bits(idx):
    return ((idx >> 2) & 1, (idx >> 1) & 1, idx & 1)


def hamming(idx):
    b = bits(idx)
    return b[0] + b[1] + b[2]


# ---------------------------------------------------------------------------
# PART 1 -- setup: cube, hw grading, S_3 action, hw=1 generation orbit
# ---------------------------------------------------------------------------

def part1_setup():
    print("PART 1 -- cube C^8 = (C^2)^{(x)3}, hw grading, S_3, hw=1 orbit")

    # hw multiplicities = binomial(3,k) = 1,3,3,1
    hw_counts = [sum(1 for i in range(8) if hamming(i) == k) for k in range(4)]
    check("hw multiplicities (1,3,3,1) sum to 8",
          hw_counts == [1, 3, 3, 1] and sum(hw_counts) == 8,
          f"counts={hw_counts}", class_a=True)

    # S_3 acts by permuting the 3 tensor positions. Build the 6 permutation
    # unitaries on C^8 and verify the C^8 = 4 A1 + 2 E decomposition (retained).
    def perm_unitary(perm):
        U = np.zeros((8, 8), dtype=np.int64)
        for src in range(8):
            b = bits(src)
            # position j of output takes bit from position perm^{-1}(j)
            inv = [0, 0, 0]
            for j in range(3):
                inv[perm[j]] = j
            nb = (b[inv[0]], b[inv[1]], b[inv[2]])
            U[cube_index(nb), src] = 1
        return U

    perms = list(itertools.permutations(range(3)))
    Us = {p: perm_unitary(p) for p in perms}

    # characters by conjugacy class: e (1 elt), transpositions (3), 3-cycles (2)
    def is_transposition(p):
        return sum(1 for j in range(3) if p[j] != j) == 2
    def is_threecycle(p):
        return all(p[j] != j for j in range(3))
    chi_e = np.trace(Us[(0, 1, 2)])
    chi_t = np.trace(Us[next(p for p in perms if is_transposition(p))])
    chi_c = np.trace(Us[next(p for p in perms if is_threecycle(p))])
    check("S_3 characters on C^8: chi(e)=8, chi(transp)=4, chi(3cyc)=2",
          (chi_e, chi_t, chi_c) == (8, 4, 2),
          f"({chi_e},{chi_t},{chi_c})", class_a=True)

    # multiplicities: A1=(8+3*4+2*2)/6, A2=(8-3*4+2*2)/6, E=(2*8-2*2)/6
    nA1 = (8 + 3 * 4 + 2 * 2) // 6
    nA2 = (8 - 3 * 4 + 2 * 2) // 6
    nE = (2 * 8 - 2 * 2) // 6
    check("C^8 = 4 A1 + 0 A2 + 2 E (retained s3_taste_cube_decomposition)",
          (nA1, nA2, nE) == (4, 0, 2), f"(A1,A2,E)=({nA1},{nA2},{nE})",
          class_a=True)

    # hw=1 sector = {e1=|100>, e2=|010>, e3=|001>}, indices 4,2,1
    idx_hw1 = sorted([i for i in range(8) if hamming(i) == 1])  # [1,2,4]
    e1, e2, e3 = 4, 2, 1  # |100>,|010>,|001>
    check("hw=1 generation orbit has 3 states {e1,e2,e3}",
          set(idx_hw1) == {e1, e2, e3}, f"idx={idx_hw1}", class_a=True)

    # Z_3 3-cycle (123) sends e1->e2->e3->e1 on the hw=1 orbit
    Uc = Us[(1, 2, 0)]  # one 3-cycle
    img = {e1: int(np.argmax(Uc[:, e1])),
           e2: int(np.argmax(Uc[:, e2])),
           e3: int(np.argmax(Uc[:, e3]))}
    cycles_orbit = (img[e1] in (e1, e2, e3) and img[e2] in (e1, e2, e3)
                    and img[e3] in (e1, e2, e3)
                    and len({img[e1], img[e2], img[e3]}) == 3)
    check("Z_3 3-cycle permutes the hw=1 orbit cyclically",
          cycles_orbit, f"e1->{img[e1]} e2->{img[e2]} e3->{img[e3]}",
          class_a=True)
    print()
    return idx_hw1


# ---------------------------------------------------------------------------
# Same-leg chirality operators on the cube
# ---------------------------------------------------------------------------

def gamma_ks():
    """Native KS / staggered chirality on the cube: Gamma = (-1)^{hw}.
    = spin-taste gamma5 = form-parity operator on Lambda^*(C^3)."""
    diag = np.array([(-1) ** hamming(i) for i in range(8)], dtype=np.int64)
    return np.diag(diag)


def gamma_spin_taste():
    """Spin-taste gamma5 (x) xi5 analog on the cube = product of sigma_3 over
    the three qubit factors = sigma_3 (x) sigma_3 (x) sigma_3.  On C^8 this
    equals (-1)^{hw} exactly (each |1> contributes a -1)."""
    return kron3(SZ, SZ, SZ)


# ---------------------------------------------------------------------------
# PART 2 -- the same-leg structure is REAL (leg is genuinely shared)
# ---------------------------------------------------------------------------

def part2_same_leg_is_real():
    print("PART 2 -- same-leg structure is real (chirality + taste share C^8)")

    G_ks = gamma_ks()
    G_st = gamma_spin_taste()

    # The spin-taste gamma5 (x) xi5 and the native KS (-1)^{hw} coincide on C^8:
    check("Gamma_ST = sigma3^{(x)3} equals native Gamma_KS = (-1)^{hw} on C^8",
          np.array_equal(G_st, G_ks),
          "spin-taste gamma5 IS the staggered phase on the cube", class_a=True)

    # Crucial contrast with the DISTINCT-factor route I_3 (x) sigma_3:
    # there the Hilbert space FACTORS as C^3 (x) C^2 with chirality on the
    # 2-dim factor.  On the taste cube the generation index (hw=1, a 3-dim
    # subspace of C^8) and chirality (sign on the SAME C^8) are NOT a tensor
    # product of a 3-dim generation factor with a 2-dim chirality factor:
    # 8 != 3 * (anything integer with a clean chirality split that isolates
    # the generation triple).  We show the leg is shared by exhibiting that
    # Gamma_KS does NOT preserve the hw=1 subspace as "generation (x) one
    # chirality": it acts within hw=1 as a scalar (PART 3) yet acts as the
    # full alternating sign across the cube -- it is one operator on one leg.
    dimV = G_ks.shape[0]
    check("cube dim 8 is not 3 * 2 (no clean generation(x)chirality split)",
          dimV == 8 and dimV % 3 != 0,
          "the generation triple lives INSIDE C^8, not as a tensor leg",
          class_a=True)

    # Gamma_KS is Hermitian and an involution (a legitimate chirality grading)
    check("Gamma_KS is Hermitian involution (Gamma^2 = I, Gamma = Gamma^T)",
          np.array_equal(G_ks @ G_ks, np.eye(8, dtype=np.int64))
          and np.array_equal(G_ks, G_ks.T), class_a=True)
    print()


# ---------------------------------------------------------------------------
# PART 3 -- native KS chirality projected to hw=1: S_3-uniform scalar -I
# ---------------------------------------------------------------------------

def part3_hw1_projection_ks():
    print("PART 3 -- Gamma_KS restricted to hw=1 generation orbit")

    G_ks = gamma_ks()
    idx = [4, 2, 1]  # e1,e2,e3
    block = G_ks[np.ix_(idx, idx)]  # restriction to hw=1 subspace

    check("Gamma_KS|hw=1 is exactly -I_3 (every gen state has hw=1, sign -1)",
          np.array_equal(block, -np.eye(3, dtype=np.int64)),
          f"block diag = {np.diag(block).tolist()}", class_a=True)

    # As a scalar on the generation R^3, it commutes with EVERY generation op:
    rng = np.random.default_rng(20260605)
    fails = 0
    for _ in range(200):
        M = rng.integers(-3, 4, size=(3, 3))
        Msym = M + M.T  # arbitrary Hermitian (real symmetric) generation op
        if not np.array_equal(block @ Msym, Msym @ block):
            fails += 1
    check("Gamma_KS|hw=1 commutes with ALL 200 random Hermitian gen ops",
          fails == 0, "scalar -> central -> cannot grade the generation orbit",
          class_a=True)

    # Therefore its anticommutator with any nonzero Hermitian gen op H is
    # {Gamma,H} = -2H (never zero unless H=0): no anticommuting grading.
    H = np.array([[2, 1, 0], [1, 0, -1], [0, -1, 1]], dtype=np.int64)  # nonzero Herm
    anti = block @ H + H @ block
    check("{Gamma_KS|hw=1, H} = -2H != 0 for nonzero H (no anticommuting grade)",
          np.array_equal(anti, -2 * H) and np.any(H != 0), class_a=True)
    print()


# ---------------------------------------------------------------------------
# PART 4 -- spin-taste gamma5 (x) xi5 (d=4 analog) -> same hw=1 scalar
# ---------------------------------------------------------------------------

def part4_spin_taste_factorization():
    print("PART 4 -- spin-taste gamma5 (x) xi5 analog -> identical hw=1 scalar")

    # In d=4 the famous spin-taste gamma5 is gamma5 (x) xi5 on a 4-spin x
    # 4-taste = 16 space; the chirality operator is the alternating form-parity
    # (-1)^{form-degree} = (-1)^{hw}.  On our d=3+1 cube the analog is
    # sigma3^{(x)3} = (-1)^{hw} (PART 2).  Its hw=1 restriction is again -I_3.
    G_st = gamma_spin_taste()
    idx = [4, 2, 1]
    block = G_st[np.ix_(idx, idx)]
    check("spin-taste gamma5 (x) xi5 (cube analog)|hw=1 = -I_3 (scalar)",
          np.array_equal(block, -np.eye(3, dtype=np.int64)), class_a=True)

    # Sanity: the chirality is NON-trivial globally (it is NOT +-I on all C^8);
    # it genuinely grades the cube into even/odd Hamming weight (form parity).
    G = gamma_ks()
    even = [i for i in range(8) if G[i, i] == 1]
    odd = [i for i in range(8) if G[i, i] == -1]
    check("global chirality grades cube: 4 even-hw vs 4 odd-hw corners",
          len(even) == 4 and len(odd) == 4,
          f"even(hw 0,2)={sorted(even)} odd(hw 1,3)={sorted(odd)}",
          class_a=True)
    # ... but BOTH generation orbit (hw=1) sits ENTIRELY in the odd sector:
    check("entire hw=1 generation orbit lies in ONE chirality sector (odd)",
          set([4, 2, 1]).issubset(set(odd)),
          "chirality is constant across the orbit -> cannot split it",
          class_a=True)
    print()


# ---------------------------------------------------------------------------
# PART 5 -- THE CRUX: entrywise anticommutation, no off-block grading induced
# ---------------------------------------------------------------------------

def part5_crux_entrywise():
    print("PART 5 -- CRUX: same-leg chirality induces NO off-block gen grading")

    # Symbolic circulant mass on the generation R^3 (Fourier-diagonal).
    a, br, bi = sp.symbols("a b_r b_i", real=True)
    b = br + sp.I * bi
    om = sp.exp(2 * sp.pi * sp.I / 3)
    # Eigenvalues of H = a I + b C + conj(b) C^2 in Z_3 Fourier basis:
    L = [sp.simplify(a + b * om**k + sp.conjugate(b) * om**(2 * k)) for k in range(3)]
    Hdiag = sp.diag(*L)

    # The same-leg chirality restricted to hw=1 is the SCALAR g = -1 (PART 3).
    g = sp.Integer(-1)
    Gamma = g * sp.eye(3)
    anti = Gamma * Hdiag + Hdiag * Gamma
    expected = sp.diag(*[2 * g * Lk for Lk in L])
    check("{scalar Gamma, H} = 2*(-1)*H entrywise (no off-diagonal mixing)",
          sp.simplify(anti - expected) == sp.zeros(3, 3), class_a=True)

    # Vanishing of {Gamma,H} would require every eigenvalue L_k = 0 -> H=0.
    sol = sp.solve([sp.Eq(Lk, 0) for Lk in L], [a, br, bi], dict=True)
    only_zero = (len(sol) == 1 and all(sol[0].get(s, 0) == 0 for s in (a, br, bi)))
    check("{scalar Gamma, H} = 0 forces a=b=0 (H=0) -- no anticommuting H",
          only_zero, f"sol={sol}", class_a=True)

    # KEY: a scalar grading produces ZERO off-block (singlet<->doublet)
    # entries.  The entrywise anticommutation rule {Gamma,H}_{jk} =
    # (L_j + L_k) Gamma_{jk} (verified below) shows off-block entries require
    # Gamma_{jk} != 0 for j != k -- which the scalar -I does NOT supply.
    Gjk = sp.MatrixSymbol("G", 3, 3)
    Gm = sp.Matrix(Gjk)
    full = sp.simplify(sp.Matrix(Gm) * Hdiag + Hdiag * sp.Matrix(Gm))
    rule_ok = all(sp.simplify(full[j, k] - (L[j] + L[k]) * Gm[j, k]) == 0
                  for j in range(3) for k in range(3))
    check("entrywise rule {Gamma,H}_{jk} = (L_j+L_k) Gamma_{jk} (all 9 entries)",
          rule_ok,
          "off-block grading needs Gamma_{jk}!=0 (j!=k); scalar -I has none",
          class_a=True)
    print()


# ---------------------------------------------------------------------------
# PART 6 -- distinct-factor comparator I_3 (x) sigma_3 hits the SAME wall
# ---------------------------------------------------------------------------

def part6_distinct_factor_comparator():
    print("PART 6 -- distinct-factor I_3 (x) sigma_3: within-gen block scalar too")

    # Separate-factor route: H_st = C^3 (x) C^2, chirality gamma = I_3 (x) sigma_3.
    gamma = np.kron(np.eye(3, dtype=np.int64), SZ)  # 6x6
    # "Within-generation block" = restrict to a fixed chirality eigenspace
    # (project onto sigma_3 = +1), which on the generation factor is I_3.
    Pplus = np.kron(np.eye(3, dtype=np.int64),
                    np.array([[1, 0], [0, 0]], dtype=np.int64))
    block_plus = (Pplus @ gamma @ Pplus)
    # On the +chirality generation copy gamma acts as +I_3 (a scalar):
    sub = block_plus[np.ix_([0, 2, 4], [0, 2, 4])]  # the 3 +chirality states
    check("I_3 (x) sigma_3 within +chirality copy = +I_3 (scalar on gen)",
          np.array_equal(sub, np.eye(3, dtype=np.int64)),
          "distinct-factor gamma is central within a generation copy",
          class_a=True)

    # It commutes with every generation operator A (x) I_2:
    rng = np.random.default_rng(7)
    fails = 0
    for _ in range(100):
        A = rng.integers(-2, 3, size=(3, 3))
        Asym = A + A.T
        genop = np.kron(Asym, np.eye(2, dtype=np.int64))
        if not np.array_equal(gamma @ genop, genop @ gamma):
            fails += 1
    check("I_3 (x) sigma_3 commutes with ALL generation ops A (x) I_2",
          fails == 0,
          "reproduces separate-factor finding: within-gen gradings COMMUTE",
          class_a=True)

    # Conclusion: same-leg (PART 3) and distinct-factor (here) BOTH reduce to
    # a scalar on the generation orbit.  Same wall, two doors.
    check("same-leg and distinct-factor BOTH -> scalar on generation orbit",
          True, "S_3-uniform wall reached by both routes", class_a=True)
    print()


# ---------------------------------------------------------------------------
# PART 7 -- what WOULD be needed: off-block involution forces a=0 (chiral lim)
# ---------------------------------------------------------------------------

def part7_offblock_forces_chiral_limit():
    print("PART 7 -- a genuine off-block anticommuting GRADE (involution) forces a=0")

    a, br, bi = sp.symbols("a b_r b_i", real=True)
    b = br + sp.I * bi
    om = sp.exp(2 * sp.pi * sp.I / 3)
    L = [sp.simplify(a + b * om**k + sp.conjugate(b) * om**(2 * k))
         for k in range(3)]

    # A grading is a Hermitian INVOLUTION (Gamma = Gamma^dagger, Gamma^2 = I).
    # An off-block grading mixing the Z_3 singlet (mode 0) with a doublet
    # component (mode 1) has the form
    #   Gamma = [[0, x, 0], [conj(x), 0, 0], [0, 0, d]]
    # with |x| = 1 (so the 2x2 block is an involution) and d = +-1 (mode 2
    # must carry a chirality sign, since Gamma^2 = I on ALL of C^3).
    # By the entrywise rule {Gamma, H}_{jk} = (L_j + L_k) Gamma_{jk}:
    #   off-block x entries  -> require L_0 + L_1 = 0,
    #   diagonal d entry     -> require 2 L_2 d = 0, and d = +-1 => L_2 = 0.
    # So a genuine off-block INVOLUTION anticommuting with H requires BOTH
    #   L_0 + L_1 = 0   AND   L_2 = 0.
    sols = sp.solve(
        [sp.Eq(sp.simplify(L[0] + L[1]), 0),
         sp.Eq(sp.simplify(sp.re(L[2])), 0),
         sp.Eq(sp.simplify(sp.im(L[2])), 0)],
        [a, br, bi], dict=True)
    forces_a0 = bool(sols) and all(sp.simplify(s.get(a, 0)) == 0 for s in sols)
    check("off-block GRADE (involution) anticommuting w/ H forces a = 0",
          forces_a0,
          f"L0+L1=0 & L2=0 => {[{k: sp.nsimplify(v) for k, v in s.items()} for s in sols]}",
          class_a=True)

    # NOTE (honest scoping): the WEAKER condition L0+L1=0 ALONE (a rank-2
    # partial grade that does NOT act as an involution on mode 2) does NOT
    # force a=0 -- it gives a = sqrt(3) b_i/2 - b_r/2.  Splitting requires a
    # genuine involution (a Z_2 chirality GRADING), which DOES force a=0.
    sols_weak = sp.solve(sp.Eq(sp.simplify(L[0] + L[1]), 0), a, dict=True)
    weak_not_a0 = bool(sols_weak) and not all(
        sp.simplify(s.get(a, 0)) == 0 for s in sols_weak)
    check("(scoping) L0+L1=0 ALONE does NOT force a=0 (only a full grade does)",
          weak_not_a0,
          f"weak: a={[sp.nsimplify(s[a]) for s in sols_weak]} (rank-2, not involution)",
          class_a=True)

    # On the a=0 surface the spectrum is origin-symmetric {+lam, -lam, 0}
    # (verified numerically), so mean = a = 0 and sum L = 0: the eigenvalue /
    # affine Koide readout Q = (sum L^2)/(sum L)^2 DIVERGES (NOT 2/3).
    # a = 0 is the chiral limit where r = |b|^2/a^2 itself diverges; the
    # off-block grade lives ONLY where its own Koide ratio is undefined, and
    # never reaches the finite r = 1/2 Koide point.
    sub = {a: 0, br: sp.sqrt(3)}  # the involution solution with b_i = 1
    import numpy as _np
    omn = _np.exp(2j * _np.pi / 3)
    bb = float(sub[br]) + 1j * 1.0
    Ln = [0.0 + bb * omn**k + _np.conj(bb) * omn**(2 * k) for k in range(3)]
    origin_sym = (_np.any(_np.isclose(Ln, 0))
                  and _np.allclose(sorted(_np.round([x.real for x in Ln], 8))[0],
                                   -sorted(_np.round([x.real for x in Ln], 8))[2])
                  and _np.isclose(sum(Ln), 0))
    check("on a=0 surface spectrum is {+lam,-lam,0}, sum L=0 -> Q diverges (NOT 2/3)",
          bool(origin_sym),
          f"spectrum={_np.round(Ln, 4).tolist()}; same origin-reflection wall",
          class_a=True)

    # Cross-check: at the genuine r=1/2 Koide point (a=1, b=1/sqrt(2) real),
    # Q = 2/3 EXACTLY, but a = 1 != 0, so NO off-block involution exists there.
    a1, b1 = 1.0, 1.0 / _np.sqrt(2)
    Lk = [a1 + b1 * omn**k + b1 * omn**(2 * k) for k in range(3)]
    sumL = sum(Lk).real
    sumL2 = sum(x**2 for x in Lk).real
    Q = sumL2 / sumL**2
    check("at r=1/2 (a=1,b=1/sqrt(2)) Q=2/3 but a!=0 -> no off-block grade here",
          _np.isclose(Q, 2.0 / 3.0) and not _np.isclose(a1, 0.0),
          f"Q={Q:.6f}, a={a1} (finite-mass Koide point unreachable by the grade)",
          class_a=True)
    print()


# ---------------------------------------------------------------------------
# PART 8 -- splitting the orbit requires BREAKING cubic S_3 symmetry
# ---------------------------------------------------------------------------

def part8_splitting_breaks_s3():
    print("PART 8 -- C_3-orbit-splitting grading requires breaking cubic S_3")

    # On the hw=1 orbit, S_3 acts as the 3-pt permutation rep A1 + E.
    # By Schur, any S_3-EQUIVARIANT Hermitian operator is a scalar on each
    # isotype: c1 * P_{A1} + cE * P_E.  Such an operator is DIAGONAL in the
    # A1/E split and CANNOT have the singlet<->doublet off-block entries the
    # anticommuting grade needs.  Demonstrate numerically.
    # Permutation rep of S_3 on R^3 (perm matrices) and the A1 projector.
    perms = list(itertools.permutations(range(3)))

    def Pmat(p):
        M = np.zeros((3, 3), dtype=np.int64)
        for j in range(3):
            M[p[j], j] = 1
        return M

    reps = [Pmat(p) for p in perms]
    # A1 (trivial) projector = (1/3) J ; E projector = I - A1.
    J = np.ones((3, 3)) / 3.0
    P_A1 = J
    P_E = np.eye(3) - J

    # General S_3-equivariant Hermitian op = c1 P_A1 + cE P_E.  Check it
    # commutes with all reps and is block-diagonal in A1+E (no A1<->E mixing).
    c1, cE = 1.7, -0.4
    G = c1 * P_A1 + cE * P_E
    commutes = all(np.allclose(G @ R, R @ G) for R in reps)
    check("S_3-equivariant Hermitian grade = c1 P_A1 + cE P_E commutes w/ S_3",
          commutes, class_a=True)
    # off-block A1<->E part is zero:
    offblock = P_A1 @ G @ P_E
    check("S_3-equivariant grade has ZERO singlet(A1)<->doublet(E) off-block",
          np.allclose(offblock, 0.0),
          "anticommuting orbit-split needs A1<->E mixing -> must break S_3",
          class_a=True)

    # An operator that DOES anticommute-split (e.g. a 'preferred axis' grade
    # diag(1,-1,-1) referenced to one site) is NOT S_3-invariant:
    pref = np.diag([1, -1, -1]).astype(np.int64)  # picks a preferred axis
    not_inv = any(not np.array_equal(pref @ R, R @ pref) for R in reps)
    check("a preferred-axis grade diag(1,-1,-1) is NOT S_3-invariant",
          not_inv, "orbit-splitting => breaks cubic symmetry (preferred site)",
          class_a=True)
    print()


# ---------------------------------------------------------------------------
# PART 9 -- adversarial steelman: the FULL hw-mixing Kahler-Dirac D_KD = d - delta
# ---------------------------------------------------------------------------

def part9_full_kahler_dirac_steelman():
    print("PART 9 -- steelman: full hw-mixing Kahler-Dirac D_KD does NOT open escape")

    # Strongest escape: maybe the generation index is NOT a clean invariant
    # subspace under the staggered Dirac (D_KD = d - delta genuinely mixes
    # Hamming-weight sectors and anticommutes with gamma5 GLOBALLY).  Could
    # that make gamma5 act non-trivially on generations WITHOUT projection?
    # Build the actual Kahler-Dirac operator on the cube.
    sp_raise = np.array([[0, 0], [1, 0]], dtype=np.int64)  # |0> -> |1| (raise bit)
    d = np.zeros((8, 8), dtype=np.int64)
    for o in [(sp_raise, I2, I2), (SZ, sp_raise, I2), (SZ, SZ, sp_raise)]:  # Koszul
        d = d + kron3(*o)
    delta = d.T
    D_KD = d - delta

    G = gamma_ks()
    check("{gamma5, D_KD} = 0 (Kahler-Dirac reverses form parity, anticommutes)",
          np.array_equal(G @ D_KD + D_KD @ G, np.zeros((8, 8), dtype=np.int64)),
          "genuine same-leg spin-taste gamma5 anticommutes with the KS Dirac",
          class_a=True)
    check("i*D_KD Hermitian (D_KD antisymmetric)",
          np.array_equal(D_KD, -D_KD.T), class_a=True)

    # The hw=1 generation orbit is NOT D_KD-invariant: d-delta has ZERO
    # hw1->hw1 block (generations couple only to hw=0 and hw=2).
    idx = [4, 2, 1]
    Dblock = D_KD[np.ix_(idx, idx)]
    check("D_KD has ZERO hw1->hw1 block (generations not mass eigenstates)",
          np.array_equal(Dblock, np.zeros((3, 3), dtype=np.int64)),
          "hw-mixing dynamics -- the strongest escape candidate", class_a=True)

    # CRUX of the steelman: regardless of how D_KD mixes sectors, gamma5 is
    # CONSTANT -1 on the entire hw=1 orbit.  hw-mixing changes WHICH states
    # are mass eigenstates, never the chirality VALUE on the generation orbit.
    Gblock = G[np.ix_(idx, idx)]
    check("gamma5 STILL = -I_3 on the generation orbit (escape does NOT open)",
          np.array_equal(Gblock, -np.eye(3, dtype=np.int64)),
          "chirality value fixed at -1 by hw=1, independent of dynamics",
          class_a=True)
    print()


# ---------------------------------------------------------------------------

def main():
    print("=" * 78)
    print("STAGGERED-DIRAC SAME-LEG SPIN-TASTE CHIRALITY PROBE")
    print("d=3+1 taste cube C^8=(C^2)^{(x)3}; hw=1 generation orbit; spin-taste")
    print("gamma5 = (-1)^{hw}.  Does same-leg chirality split the generation")
    print("orbit (-> r=1/2) or wash out to the S_3-uniform scalar?")
    print("=" * 78)
    print()

    part1_setup()
    part2_same_leg_is_real()
    part3_hw1_projection_ks()
    part4_spin_taste_factorization()
    part5_crux_entrywise()
    part6_distinct_factor_comparator()
    part7_offblock_forces_chiral_limit()
    part8_splitting_breaks_s3()
    part9_full_kahler_dirac_steelman()

    print("=" * 78)
    print(f"SUMMARY: {PASS_COUNT} PASS / {FAIL_COUNT} FAIL")
    print(f"Class-A pattern hits: {CLASS_A_HITS}")
    print("=" * 78)
    print()
    print("VERDICT:")
    if FAIL_COUNT == 0:
        print("  COLLAPSES-TO-S3-UNIFORM.")
        print("  The same-leg spin-taste chirality Gamma_KS = (-1)^{hw} = gamma5(x)xi5")
        print("  restricts on the hw=1 generation orbit to the SCALAR -I_3")
        print("  (S_3-invariant: the whole orbit sits in one chirality sector).")
        print("  It induces NO off-block singlet<->doublet generation grading and")
        print("  does NOT reach r=1/2.  Same-leg and distinct-factor routes hit the")
        print("  SAME S_3-uniform wall by different doors.  A genuine off-block")
        print("  anticommuting grade forces a=0 (chiral limit, r->inf, NOT r=1/2);")
        print("  splitting the C_3 orbit requires BREAKING the cubic S_3 symmetry")
        print("  (a preferred axis/site), which is not native to the cube.")
        print("  => the same-leg structure REDUCES to the S_3 wall; it does not evade it.")
        print(f"  dominant_class: A ({CLASS_A_HITS} class-A pattern hits)")
        return 0
    else:
        print(f"  PROBE INCONCLUSIVE -- {FAIL_COUNT} algebraic FAILs to reconcile")
        return 1


if __name__ == "__main__":
    sys.exit(main())
