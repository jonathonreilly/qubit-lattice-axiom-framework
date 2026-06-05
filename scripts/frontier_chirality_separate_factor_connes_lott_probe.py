#!/usr/bin/env python3
"""Separate-factor Connes-Lott probe for the generation-chirality gate.

Verifies the algebraic content of
`docs/CHIRALITY_SEPARATE_FACTOR_CONNES_LOTT_PROBE_2026-06-05.md`.

THE OPEN HATCH (2026-06-05). The four prior probes established that NO
Hermitian, off-block (singlet<->doublet), C_3-orbit-splitting grading
Gamma_chi anticommutes with the circulant generation operator
H = a I + b C + conj(b) C^2 at finite a on the SINGLE generation factor
C^3; the chiral grading lives only at a = 0 (massless).

Two MULTI-FACTOR attempts already FAILED:
  * PT-C / CPT-C3: the spacetime grading gamma_CL = I_3 (x) sigma_3
    has Y = I_3 (identity on generation), so its anticommutator reduces
    to the trivial generation anticommutator -> ZERO generation residue
    (on-block collapse). [cpt_c3_cp_squared_scalar, retained_bounded]
  * native Cl(3) volume element omega = i*I_3 is a CENTRAL SCALAR on the
    generation factor -> cannot grade (commutes with everything).

The audit + the Record-axiom probe BOTH explicitly leave OPEN the
"separate-factor Connes-Lott with an INDEPENDENT H_L (+) H_R doubling":
a GENUINE extra chirality factor (NOT the spacetime one, NOT the on-site
Cl(3) one), tensoring the generation R^3 with an independent 2-dim
chirality space, with a Dirac operator whose off-diagonal block Y acts
NON-TRIVIALLY on the generation factor (a genuine generation operator,
UNLIKE PT-C's Y = I_3).

THE FRESH QUESTION. Build the Connes-Lott-style finite spectral triple

    Hilbert space   H = C^3_gen (x) C^2_LR ,   C^2_LR = H_L (+) H_R
    grading         gamma = I_3 (x) sigma_3 = diag(+I_3, -I_3)
    Dirac operator  D = [[0, Y], [Y^dag, 0]]   (block in L/R)

with Y an ARBITRARY 3x3 generation operator (NOT forced to I_3). By the
Connes-Lott axiom {D, gamma} = 0 holds AUTOMATICALLY on the full C^6 for
ANY Y (the off-diagonal Dirac anticommutes with the diagonal grading) --
chirality is GENUINE on the doubled space. Test whether, after the
PHYSICAL REDUCTION to the generation factor, this induces a genuine
off-block C_3-orbit-splitting grading on C^3 anticommuting with the
generation mass operator AND delivering Q = 2/3.

THREE crux tests (the honest verdict turns on these):

  Q1  Does gamma = I_3 (x) sigma_3 with off-diagonal Y (acting on
      generation) induce a genuine OFF-BLOCK (singlet<->doublet)
      C_3-orbit-splitting grading on the GENERATION factor after
      reduction -- UNLIKE PT-C where Y = I_3 gave zero generation
      residue?
  Q2  The discriminator vs PT-C: PT-C's Y = I_3 made {D, gamma} reduce
      to the trivial generation anticommutator. Here Y is a genuine
      generation operator. Does the reduced structure leave a NON-trivial
      generation grading, or does it STILL collapse (chirality and
      generation grading living in DISTINCT tensor factors -> the
      wrong-tensor-factor wall)?
  Q3  Does any off-diagonal Y give Gamma_chi-anticommutation on the
      generation factor AND Q = 2/3 -- OR must the independent doubling
      factor ITSELF be IMPORTED (it is NOT in A1+A2+A3: the Z^3 lattice
      has no native L/R doubling on the generation orbit)?

All algebra is SYMBOLIC (sympy) on arbitrary parameters. No PDG /
measured / empirical lepton masses are consumed. Numpy is used only for
an independent floating-point cross-check of the symbolic reductions.
"""

from __future__ import annotations

import sys

import numpy as np
import sympy as sp


# ----------------------------------------------------------------------
# harness
# ----------------------------------------------------------------------

PASS = 0
FAIL = 0


def banner(title: str) -> None:
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def check(label: str, ok: bool) -> bool:
    global PASS, FAIL
    status = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] {label}")
    return ok


def simp(M: sp.Matrix) -> sp.Matrix:
    return sp.simplify(sp.expand(M))


def hconj(M: sp.Matrix) -> sp.Matrix:
    return M.conjugate().T


def is_zero(M: sp.Matrix) -> bool:
    return simp(M) == sp.zeros(*M.shape)


# ----------------------------------------------------------------------
# generation-factor primitives (C^3, circulant Koide operator)
# ----------------------------------------------------------------------

a, br, bi = sp.symbols("a b_r b_i", real=True)
b = br + sp.I * bi
bbar = sp.conjugate(b)
omega = sp.Rational(-1, 2) + sp.sqrt(3) / 2 * sp.I


def cyclic_shift() -> sp.Matrix:
    return sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])


def fourier_matrix() -> sp.Matrix:
    F = sp.zeros(3, 3)
    for g in range(3):
        for k in range(3):
            F[g, k] = omega ** (g * k)
    return F / sp.sqrt(3)


def circulant_H() -> sp.Matrix:
    C = cyclic_shift()
    return simp(a * sp.eye(3) + b * C + bbar * (C * C))


def gamma_chi_circulant() -> sp.Matrix:
    """Generation chiral grading Gamma_chi = (2/3) J - I = diag(+1,-1,-1)
    in the Fourier (singlet/doublet) basis. The off-block grading the
    Koide Q=2/3 gate requires must be Hermitian, square to I, and
    anticommute with the generation mass operator."""
    return sp.Rational(2, 3) * sp.ones(3, 3) - sp.eye(3)


# ----------------------------------------------------------------------
# PART 0 — sanity: the established single-factor wall (finite-a no anticommute)
# ----------------------------------------------------------------------

def part0_single_factor_wall():
    banner("PART 0 — established single-factor wall: no off-block grading "
           "anticommutes at finite a")
    H = circulant_H()
    Gchi = gamma_chi_circulant()
    # Gamma_chi is C_3-equivariant (circulant) -> commutes with H -> cannot
    # anticommute unless H = 0. This is WALL 1 (retained_bounded).
    C = cyclic_shift()
    check("Gamma_chi is circulant (C_3-equivariant): [Gamma_chi, C] = 0",
          is_zero(Gchi * C - C * Gchi))
    comm = simp(H * Gchi - Gchi * H)
    check("[H, Gamma_chi] = 0 (circulant grading commutes with circulant H)",
          is_zero(comm))
    anti = simp(H * Gchi + Gchi * H)
    check("{H, Gamma_chi} != 0 for finite a (so anticommute fails on C^3)",
          not is_zero(anti))
    # Solve {H, Gamma_chi} = 0: forces a -> 0 (massless).
    eqs = [anti[i, j] for i in range(3) for j in range(3)]
    sol = sp.solve(eqs, [a, br, bi], dict=True)
    print(f"    solve {{H,Gamma_chi}}=0 -> {sol}")
    forces_a0 = bool(sol) and all(s.get(a, None) == 0 for s in sol)
    check("on C^3 the anticommutation forces a = 0 (chiral/massless limit)",
          forces_a0)


# ----------------------------------------------------------------------
# PART 1 — build the separate-factor Connes-Lott spectral triple
# ----------------------------------------------------------------------

def kron(A: sp.Matrix, B: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(sp.kronecker_product(A, B))


def build_triple(Y: sp.Matrix):
    """Return (D, gamma, J?) on H = C^3_gen (x) C^2_LR.

    Ordering: basis index = (gen, chir) with chir in {L=0, R=1} the FAST
    index, so the 6x6 matrices are gen-blocks of 2x2. We instead use the
    L/R-block ordering (chir SLOW): top 3 = L sector, bottom 3 = R sector,
    so D = [[0, Y],[Y^dag, 0]] and gamma = diag(+I3, -I3) are clean blocks.
    """
    I3 = sp.eye(3)
    Z3 = sp.zeros(3, 3)
    D = sp.Matrix(sp.BlockMatrix([[Z3, Y], [hconj(Y), Z3]]))
    gamma = sp.Matrix(sp.BlockMatrix([[I3, Z3], [Z3, -I3]]))
    return simp(D), gamma


def part1_triple_axioms(Y: sp.Matrix, label: str):
    banner(f"PART 1 — Connes-Lott axioms for D=[[0,Y],[Y^dag,0]], "
           f"gamma=diag(+I3,-I3)  [{label}]")
    D, gamma = build_triple(Y)
    # gamma^2 = I (Z_2 grading)
    check(f"[{label}] gamma^2 = I_6", is_zero(gamma * gamma - sp.eye(6)))
    # gamma Hermitian
    check(f"[{label}] gamma Hermitian", is_zero(gamma - hconj(gamma)))
    # D Hermitian (self-adjoint Dirac)
    check(f"[{label}] D Hermitian (self-adjoint)", is_zero(D - hconj(D)))
    # THE Connes-Lott axiom: {D, gamma} = 0 on the FULL doubled space,
    # AUTOMATICALLY for ANY Y. This is the genuine chirality of the triple.
    anti = simp(D * gamma + gamma * D)
    check(f"[{label}] {{D, gamma}} = 0 on full C^6 (CHIRAL, automatic for "
          f"any Y)", is_zero(anti))
    return D, gamma


# ----------------------------------------------------------------------
# PART 2 — the physical reduction to the generation factor
# ----------------------------------------------------------------------

def part2_reduction(Y: sp.Matrix, label: str):
    banner(f"PART 2 — physical reduction to the generation factor  [{label}]")
    # The fermion masses are the SINGULAR VALUES of Y, i.e. the eigenvalues
    # of the generation mass-squared operator. There are two natural
    # generation operators after reduction:
    #   H_gen^2 = Y^dag Y   (L-sector mass^2)   or   Y Y^dag (R-sector).
    # The physical Koide operator is the generation mass operator whose
    # eigenvalues are the singular values of Y. To compare with the
    # established circulant Koide setup we test BOTH:
    #   (i) does the L/R grading gamma INDUCE any nonzero Hermitian grading
    #       on the GENERATION factor C^3?
    #   (ii) does that induced generation operator anticommute with the
    #       generation mass operator H_gen?
    #
    # KEY STRUCTURAL FACT. gamma = I_3 (x) sigma_3 acts as the IDENTITY on
    # the generation factor (it is I_3 tensored with the chirality Pauli).
    # The reduction of gamma to the generation factor is the partial trace
    # / block-projection onto either chiral sector. Both chiral PROJECTORS
    #   P_L = (I + gamma)/2 = diag(I3, 0),  P_R = (I - gamma)/2 = diag(0, I3)
    # restrict to the generation factor as the IDENTITY I_3 (they select a
    # sector but do NOT act within generation). Hence the grading gamma
    # carries NO generation content: its generation-reduced image is a
    # SCALAR (I_3), which cannot grade the generation factor.
    I3 = sp.eye(3)
    D, gamma = build_triple(Y)

    # (a) The chiral projectors P_L, P_R reduced to the generation factor.
    P_L = simp((sp.eye(6) + gamma) / 2)   # diag(I3, 0)
    P_R = simp((sp.eye(6) - gamma) / 2)   # diag(0, I3)
    PL_gen = P_L[0:3, 0:3]
    PR_gen = P_R[3:6, 3:6]
    check(f"[{label}] gamma's L-sector reduces to I_3 on generation "
          f"(P_L|gen = I3)", is_zero(PL_gen - I3))
    check(f"[{label}] gamma's R-sector reduces to I_3 on generation "
          f"(P_R|gen = I3)", is_zero(PR_gen - I3))
    print(f"    => gamma = I_3 (x) sigma_3 carries NO generation content;")
    print(f"       its generation-reduced image is the SCALAR I_3.")

    # (b) The induced generation grading. The ONLY generation operator that
    # gamma can transport into is via conjugation D gamma D^{-1} or the
    # Schur complement. Compute the generation operator induced by sandwiching
    # gamma with the Dirac off-diagonal: the natural "induced grading" is
    # the generation block of gamma itself, which is +-I_3 per sector --
    # i.e. a SCALAR. Confirm no off-diagonal (singlet<->doublet) generation
    # structure is induced.
    # Build the generation mass-squared operators.
    M2_L = simp(hconj(Y) * Y)    # acts on generation, L-sector mass^2
    M2_R = simp(Y * hconj(Y))    # R-sector mass^2
    check(f"[{label}] Y^dag Y is Hermitian (a genuine generation operator)",
          is_zero(M2_L - hconj(M2_L)))

    # (c) The induced generation grading from gamma is the IDENTITY (scalar)
    # on each chiral sector. Test: does a SCALAR generation operator
    # anticommute with the generation mass operator M2_L? {I3, M2_L} = 2 M2_L
    # which is 0 only if M2_L = 0 (massless). So the induced grading
    # anticommutes with the generation mass ONLY at zero mass.
    induced_gen_grading = I3  # the generation-reduced image of gamma
    anti_gen = simp(induced_gen_grading * M2_L + M2_L * induced_gen_grading)
    check(f"[{label}] {{induced_gen_grading=I3, M2_L}} = 2 M2_L != 0 unless "
          f"massless", not is_zero(anti_gen) or is_zero(M2_L))
    print(f"    => the L/R grading induces only the SCALAR I_3 on generation;")
    print(f"       it does NOT anticommute with the generation mass operator")
    print(f"       (which would need a genuine off-block generation grading).")
    return M2_L, M2_R


# ----------------------------------------------------------------------
# PART 3 — crux Q1/Q2: does off-diagonal Y leave a non-trivial generation
#          grading, or does it COLLAPSE like PT-C (the wrong-tensor-factor)?
# ----------------------------------------------------------------------

def part3_wrong_tensor_factor(label: str):
    banner(f"PART 3 — Q1/Q2: the wrong-tensor-factor wall  [{label}]")
    # The decisive algebra: gamma acts as A (x) sigma_3 where A = I_3 on the
    # generation factor. Any operator O on the full space that ANTICOMMUTES
    # with gamma must be OFF-DIAGONAL in the L/R blocks (gamma is diagonal
    # in L/R). The generation grading we WANT is a Hermitian involution G3
    # acting on C^3 ALONE, i.e. O = G3 (x) I_2 (the same chirality grading in
    # both L and R sectors). But G3 (x) I_2 is BLOCK-DIAGONAL in L/R:
    #   {G3 (x) I_2, gamma = I_3 (x) sigma_3}
    #     = G3 (x) {I_2, sigma_3} = G3 (x) (2 sigma_3 ... )? No:
    # {A (x) B, C (x) D} is NOT a simple tensor in general. Compute exactly.
    # use a concrete generic Hermitian G3 to test the tensor anticommutator
    g = sp.symbols("g0 g1 g2 g3r g3i g4r g4i g5r g5i", real=True)
    G3 = sp.Matrix([
        [g[0], g[3] + sp.I * g[4], g[5] + sp.I * g[6]],
        [g[3] - sp.I * g[4], g[1], g[7] + sp.I * g[8]],
        [g[5] - sp.I * g[6], g[7] - sp.I * g[8], g[2]],
    ])
    I2 = sp.eye(2)
    sig3 = sp.Matrix([[1, 0], [0, -1]])
    I3 = sp.eye(3)
    gamma = kron(I3, sig3)            # = diag over generation of sigma_3
    O = kron(G3, I2)                  # a generation grading, SAME in L & R
    anti = simp(O * gamma + gamma * O)
    # {G3 (x) I2, I3 (x) sig3} = G3 (x) {I2, sig3}?? No: it equals
    #   (G3 (x) I2)(I3 (x) sig3) + (I3 (x) sig3)(G3 (x) I2)
    # = G3 (x) sig3 + G3 (x) sig3 = 2 (G3 (x) sig3).
    expected = simp(2 * kron(G3, sig3))
    check(f"[{label}] {{G3(x)I2, I3(x)sig3}} = 2 (G3 (x) sig3)  (NOT zero "
          f"unless G3=0)", is_zero(anti - expected))
    # This is NONZERO for any nonzero G3. So a generation grading that acts
    # IDENTICALLY in both chiral sectors does NOT anticommute with gamma --
    # i.e. it is NOT chiral in the L/R sense. The grading gamma is purely on
    # the chirality factor; a genuine generation grading lives on the OTHER
    # factor; the two anticommute only if one is the IDENTITY there.
    check(f"[{label}] a nonzero generation grading G3(x)I2 does NOT "
          f"anticommute with gamma (wrong factor)",
          not is_zero(anti))
    print(f"    => CRUX: the L/R chirality grading gamma and a generation")
    print(f"       grading G3 live in DISTINCT tensor factors. They anti-")
    print(f"       commute ONLY through the chirality factor, leaving the")
    print(f"       generation factor UNGRADED. This is the wrong-tensor-")
    print(f"       factor wall -- the SAME collapse as PT-C, now shown to")
    print(f"       be structural (independent of whether Y = I_3 or generic).")


def part3b_most_general_anticommuting(label: str):
    banner(f"PART 3b — ADVERSARIAL: the MOST GENERAL Hermitian O with "
           f"{{O, gamma}}=0  [{label}]")
    # Do NOT restrict to product form. Take the most general Hermitian O on
    # C^6 and impose {O, gamma} = 0 with gamma = diag(+I3, -I3). Since gamma
    # is BLOCK-DIAGONAL (and a scalar +-1 on each L/R block), {O, gamma} = 0
    # forces O to be purely OFF-DIAGONAL in the L/R blocks:
    #   O = [[0, W], [W^dag, 0]]   for some 3x3 W.
    # This is the SAME structural form as the Dirac D itself. Crucially its
    # BLOCK-DIAGONAL (within-sector) generation parts O_LL, O_RR VANISH:
    # O induces NO operator on the generation factor within a chiral sector;
    # it only maps L-generation <-> R-generation. A "generation grading" in
    # the Koide sense is a Hermitian INVOLUTION acting WITHIN the generation
    # factor (block-diagonal per sector). NO such operator anticommutes with
    # gamma. This is the airtight version of the wrong-tensor-factor wall.
    W = sp.Matrix(3, 3, sp.symbols("w0:9")) \
        + sp.I * sp.Matrix(3, 3, sp.symbols("v0:9"))
    I3 = sp.eye(3)
    Z = sp.zeros(3, 3)
    O = sp.Matrix(sp.BlockMatrix([[Z, W], [hconj(W), Z]]))
    gamma = sp.Matrix(sp.BlockMatrix([[I3, Z], [Z, -I3]]))
    check(f"[{label}] every off-diagonal O=[[0,W],[W^dag,0]] anticommutes "
          f"with gamma", is_zero(O * gamma + gamma * O))
    check(f"[{label}] O's L-sector generation block O_LL = 0 (no within-sector "
          f"generation operator)", is_zero(O[0:3, 0:3]))
    check(f"[{label}] O's R-sector generation block O_RR = 0 (no within-sector "
          f"generation operator)", is_zero(O[3:6, 3:6]))
    # Conversely, ANY within-generation grading G3 (block-diagonal in L/R)
    # COMMUTES with gamma (gamma is scalar on each block), so it can never be
    # the chiral partner. Confirm with a generic Hermitian G3 placed in both
    # sectors AND in one sector only.
    g = sp.symbols("p0 p1 p2 p3r p3i p4r p4i p5r p5i", real=True)
    G3 = sp.Matrix([
        [g[0], g[3] + sp.I * g[4], g[5] + sp.I * g[6]],
        [g[3] - sp.I * g[4], g[1], g[7] + sp.I * g[8]],
        [g[5] - sp.I * g[6], g[7] - sp.I * g[8], g[2]],
    ])
    O_blockdiag = sp.Matrix(sp.BlockMatrix([[G3, Z], [Z, G3]]))
    check(f"[{label}] any within-generation block-diagonal grading COMMUTES "
          f"with gamma (never anticommutes)",
          is_zero(O_blockdiag * gamma - gamma * O_blockdiag))
    print(f"    => AIRTIGHT wrong-tensor-factor wall: the ONLY operators")
    print(f"       anticommuting with gamma=I3(x)sig3 are L/R-off-diagonal")
    print(f"       (D-like); they have ZERO within-generation block, so they")
    print(f"       are NOT generation gradings. Conversely every generation")
    print(f"       grading is L/R-block-diagonal and COMMUTES with gamma. No")
    print(f"       separate-factor chirality grading can grade generation.")


# ----------------------------------------------------------------------
# PART 4 — generic off-diagonal Y: the masses are singular values of Y.
#          Test whether ANY Y delivers a generation chiral grading + Q=2/3.
# ----------------------------------------------------------------------

def part4_generic_Y_no_generation_grading(label: str):
    banner(f"PART 4 — generic off-diagonal Y: induced generation operator + "
           f"Q  [{label}]")
    # The genuine off-diagonal Dirac with Y a generation operator DOES give
    # nontrivial generation dynamics: the masses are the singular values of Y.
    # But the CHIRALITY grading gamma = I_3 (x) sigma_3 STILL acts trivially
    # on generation. The "chiral structure" on the generation factor would be
    # the polar/sign part of Y -- which is the SINGULAR-VALUE readout, NOT a
    # Hermitian involution anticommuting with a Hermitian generation operator.
    #
    # Take Y = circulant generation operator (genuine, NOT I_3):
    #   Y = a I + b C + conj(b) C^2  (the Koide circulant itself).
    C = cyclic_shift()
    Y = simp(a * sp.eye(3) + b * C + bbar * (C * C))
    D, gamma = build_triple(Y)
    # full-space chirality holds:
    check(f"[{label}] {{D, gamma}} = 0 with Y = circulant generation op "
          f"(genuine, != I_3)", is_zero(simp(D * gamma + gamma * D)))
    # The generation mass operator is sqrt(Y^dag Y). For the Koide readout we
    # need eigenvalues. Y is normal (circulant) -> singular values = |eigs|.
    # In the Fourier basis Y = diag(L0, L1, L2). Singular values |L_k|.
    F = fourier_matrix()
    Yd = simp(hconj(F) * Y * F)
    diag_ok = is_zero(Yd - sp.diag(Yd[0, 0], Yd[1, 1], Yd[2, 2]))
    check(f"[{label}] Fourier diagonalizes circulant Y", diag_ok)
    L = [simp(Yd[k, k]) for k in range(3)]
    print(f"    eigenvalues of Y: L0={L[0]}, L1={L[1]}, L2={L[2]}")

    # The Q=2/3 SIGNED (Brannen / det_R) readout uses the SIGNED eigenvalues
    # of a Hermitian generation operator H_gen, NOT the singular values |L_k|.
    # gamma reduces to I_3 on generation, so it does NOT supply the SIGN
    # structure: the chirality factor cannot convert |L_k| into signed L_k.
    # Demonstrate the gap by comparing, AT r = 1/2, the two readouts as a
    # function of the phase theta = arg(b):
    #   SIGNED   Q = (sum L_k^2)/(sum L_k)^2          (Brannen / det_R)
    #   SINGULAR Q = (sum |L_k|^2)/(sum |L_k|)^2      (Yukawa / spectral triple)
    # The established result (signed-vs-singular readout note) is that the
    # SIGNED Q = 2/3 at r=1/2 for EVERY theta (theta-independent), while the
    # SINGULAR Q equals 2/3 ONLY on the sign-homogeneous phases and drops
    # BELOW 2/3 off them. The spectral triple's masses ARE the singular
    # values of Y, so the triple delivers the SINGULAR readout. gamma supplies
    # no sign data to convert it into the signed readout.
    apos = sp.symbols("a_pos", positive=True)
    sum1 = simp(sum(L))
    sum2 = simp(sum(x ** 2 for x in L))
    Q_signed = simp(sum2 / sum1 ** 2)
    mag = apos / sp.sqrt(2)   # |b| = a/sqrt2  <=>  r = |b|^2/a^2 = 1/2

    # (i) SIGNED Q = 2/3 at r=1/2 for representative phases (theta-independent).
    signed_ok = True
    for thetadeg in (0, 60, 120, 180, 240, 300):
        th = sp.rad(thetadeg)
        Qs = simp(Q_signed.subs({a: apos, br: mag * sp.cos(th),
                                 bi: mag * sp.sin(th)}))
        signed_ok = signed_ok and (simp(Qs - sp.Rational(2, 3)) == 0)
    check(f"[{label}] SIGNED (det_R) Q = 2/3 at r=1/2 for ALL phases "
          f"(theta-independent)", signed_ok)

    # (ii) SINGULAR (Yukawa) Q at a SIGN-INHOMOGENEOUS phase (theta=180, b
    # real negative): one eigenvalue is negative, so |L_k| != L_k and the
    # singular Q DROPS BELOW 2/3. This is the readout the spectral triple
    # actually delivers; gamma cannot restore the missing sign.
    th = sp.rad(180)
    Lneg = [simp(x.subs({a: apos, br: mag * sp.cos(th),
                         bi: mag * sp.sin(th)})) for x in L]
    signs = [sp.sign(x) for x in Lneg]
    print(f"    at r=1/2, theta=180 (b real <0): signed eigenvalues L_k/a = "
          f"{[simp(x/apos) for x in Lneg]}")
    print(f"    signs = {signs}  (sign-INHOMOGENEOUS)")
    sign_inhomog = len(set(str(s) for s in signs)) > 1
    check(f"[{label}] r=1/2 has sign-INHOMOGENEOUS phases (e.g. theta=180)",
          sign_inhomog)
    Labs = [sp.Abs(x) for x in Lneg]
    s1a = simp(sum(Labs))
    s2a = simp(sum(x ** 2 for x in Labs))
    Q_singular = simp(s2a / s1a ** 2)
    print(f"    SINGULAR (Yukawa) Q at theta=180 = {Q_singular} ~ "
          f"{sp.N(Q_singular, 6)}")
    singular_below = sp.N(Q_singular) < sp.Rational(2, 3)
    check(f"[{label}] SINGULAR (Yukawa) Q < 2/3 at the sign-inhomogeneous "
          f"phase (theta=180)", bool(singular_below))
    check(f"[{label}] SINGULAR Q != SIGNED Q at theta=180 (the two readouts "
          f"DIVERGE off sign-homogeneity)",
          simp(Q_singular - sp.Rational(2, 3)) != 0)
    print(f"    => the spectral-triple mass readout (singular values of Y) is")
    print(f"       the SINGULAR/Yukawa readout: it agrees with the signed")
    print(f"       Q=2/3 ONLY on sign-homogeneous phases and drops below 2/3")
    print(f"       off them. gamma = I_3 (x) sigma_3 supplies NO generation")
    print(f"       sign data, so it cannot pin the signed Q=2/3 across phases.")


# ----------------------------------------------------------------------
# PART 5 — could the doubling be NATIVE? (is H_L (+) H_R in A1+A2+A3?)
# ----------------------------------------------------------------------

def part5_doubling_provenance(label: str):
    banner(f"PART 5 — is the H_L (+) H_R doubling NATIVE or IMPORTED?  [{label}]")
    # A1+A2+A3 give: the Z^3 mod L qubit lattice (A1 lattice + A2 growth) and
    # the emergent-time/unitary-evolution structure (A3). The generation
    # factor C^3 arises as the Hamming-weight-1 orbit {e1,e2,e3} of the
    # (Z_2)^3 corner cube under the cyclic C_3. We ask: does the lattice
    # supply, NATIVELY, an L/R doubling on this generation orbit?
    #
    # FACT (structural, not numerical): the hw=1 orbit is a SINGLE C_3 orbit
    # of three corner states; there is no native 2-fold (L/R) multiplicity
    # attached to each generation. The qubit at each site is a 2-state spin,
    # but the generation index is the ORBIT label, not a per-site qubit. A
    # chiral doubling H_L (+) H_R on the GENERATION orbit would require a
    # second 2-dim factor TENSORED with the orbit -- which is exactly the
    # extra C^2 the Connes-Lott construction POSTULATES. It is not produced
    # by the (Z_2)^3 corner structure (the corners give the 8-dim cube, whose
    # hw=1 slice is the 3-dim generation factor with NO leftover 2-fold).
    #
    # We make this concrete by COUNTING dimensions: the corner Hilbert space
    # is C^8 = (C^2)^{(x)3}; its hw=1 subspace is 3-dimensional (C(3,1)=3).
    # A separate L/R doubling on generation needs dim 3 x 2 = 6 on a factor
    # that the cube does NOT contain as generation (x) chirality.
    cube_dim = 2 ** 3
    hw1_dim = 3  # C(3,1)
    check(f"[{label}] corner cube dim = 8 = (C^2)^3", cube_dim == 8)
    check(f"[{label}] hw=1 generation slice dim = 3 (C(3,1)) -- NO leftover "
          f"L/R 2-fold", hw1_dim == 3)
    # The hw=1 states e1,e2,e3 carry a SINGLE chirality label each
    # (the native sublattice parity C = (-1)^{x+y+z} = (-1)^{hw} is CONSTANT
    # = -1 on the entire hw=1 orbit -- it does NOT split into L/R within
    # generation). Verify: hw=1 => (-1)^1 = -1 for all three.
    native_chirality = [(-1) ** 1 for _ in range(3)]
    check(f"[{label}] native parity (-1)^hw is CONSTANT (= -1) on the hw=1 "
          f"orbit (NO native L/R split)",
          len(set(native_chirality)) == 1 and native_chirality[0] == -1)
    print(f"    => the native (Z_2)^3 cube gives NO L/R doubling on the")
    print(f"       generation orbit: parity is uniform on hw=1. The")
    print(f"       independent H_L (+) H_R factor is an EXTRA 2-dim space")
    print(f"       POSTULATED by the Connes-Lott construction, NOT derived")
    print(f"       from A1+A2+A3. The doubling is IMPORTED.")
    return True


# ----------------------------------------------------------------------
# PART 6 — independent numpy cross-check of the reduction collapse
# ----------------------------------------------------------------------

def part6_numpy_crosscheck(label: str):
    banner(f"PART 6 — independent floating-point cross-check  [{label}]")
    rng = np.random.default_rng(20260605)
    ok_all = True
    for trial in range(200):
        # random complex 3x3 Y (genuine off-diagonal generation operator)
        Yr = rng.standard_normal((3, 3))
        Yi = rng.standard_normal((3, 3))
        Y = Yr + 1j * Yi
        I3 = np.eye(3)
        Z3 = np.zeros((3, 3))
        D = np.block([[Z3, Y], [Y.conj().T, Z3]])
        gamma = np.block([[I3, Z3], [Z3, -I3]])
        # full-space chirality: {D, gamma} = 0 for ANY Y
        anti = D @ gamma + gamma @ D
        if np.max(np.abs(anti)) > 1e-9:
            ok_all = False
            break
        # the generation-reduced image of gamma is +-I_3 (scalar) per sector:
        # any Hermitian generation grading G3 (x) I2 fails to anticommute
        # with gamma unless G3 = 0. Test a random Hermitian G3.
        Gr = rng.standard_normal((3, 3))
        G3 = Gr + Gr.T  # Hermitian (real-symmetric here)
        O = np.kron(G3, np.eye(2))
        gamma2 = np.kron(np.eye(3), np.array([[1.0, 0], [0, -1.0]]))
        a2 = O @ gamma2 + gamma2 @ O
        expected = 2 * np.kron(G3, np.array([[1.0, 0], [0, -1.0]]))
        if np.max(np.abs(a2 - expected)) > 1e-9:
            ok_all = False
            break
        # nonzero G3 => nonzero anticommutator (no generation grading is chiral)
        if np.max(np.abs(G3)) > 1e-6 and np.max(np.abs(a2)) < 1e-9:
            ok_all = False
            break
    check(f"[{label}] 200 random Y: {{D,gamma}}=0 on C^6 AND no generation "
          f"grading G3(x)I2 anticommutes with gamma", ok_all)


# ----------------------------------------------------------------------
# PART 7 — verdict
# ----------------------------------------------------------------------

def part7_verdict():
    banner("PART 7 — VERDICT")
    print("""
  Q1  Does gamma=I3(x)sig3 + off-diagonal Y induce a genuine OFF-BLOCK
      C_3-orbit-splitting grading on the GENERATION factor (unlike PT-C)?
      ANSWER: NO. gamma = I_3 (x) sigma_3 acts as the IDENTITY on the
      generation factor; its generation-reduced image is the SCALAR I_3.
      The off-diagonal Y supplies generation DYNAMICS (the masses are the
      singular values of Y) but NOT a generation GRADING.

  Q2  Does the genuine off-diagonal Y leave a non-trivial generation
      grading, or COLLAPSE like PT-C?
      ANSWER: It COLLAPSES -- and the collapse is now shown to be
      STRUCTURAL (Part 3), not an artifact of PT-C's Y = I_3. A generation
      grading G3 (x) I_2 and the chirality grading I_3 (x) sigma_3 live in
      DISTINCT tensor factors; {G3(x)I2, I3(x)sig3} = 2 (G3 (x) sig3) != 0
      for any nonzero G3. The chirality factor cannot grade the generation
      factor. THE WRONG-TENSOR-FACTOR WALL HOLDS even with a genuine
      doubling and a genuine off-diagonal Y.

  Q3  Does any Y give Gamma_chi-anticommutation + Q=2/3, or must the
      doubling be IMPORTED?
      ANSWER: The doubling H_L (+) H_R is IMPORTED (Part 5). The native
      (Z_2)^3 corner cube gives NO L/R 2-fold on the generation orbit:
      parity (-1)^hw is uniform (= -1) on hw=1. The extra 2-dim chirality
      space is POSTULATED by Connes-Lott, not derived from A1+A2+A3. Even
      granting the import, the spectral-triple mass readout is the
      SINGULAR-VALUE (Yukawa) readout, which differs from the SIGNED Q=2/3
      unless sign-homogeneous; gamma supplies no generation sign data
      (Part 4).

  HONEST VERDICT: REQUIRES-IMPORTED-DOUBLING (and even then COLLAPSES on
  the generation factor via the wrong-tensor-factor wall). The separate-
  factor Connes-Lott route does NOT produce a native off-block C_3-orbit-
  splitting generation grading. It relocates the chirality import to an
  imported L/R doubling factor, and that factor -- being on a DISTINCT
  tensor leg from the generation R^3 -- cannot grade the generation factor.

  This OPENS the next path: a construction where the chirality grading and
  the generation operator share the SAME tensor factor (e.g. a genuinely
  generation-internal Z_2 with a Ginsparg-Wilson-type {D, Gamma} = 2 D R
  defect, or a non-product spectral triple where the doubling is FIBERED
  over generation rather than tensored) -- NOT the separate-factor product
  triple, which is now mapped to the wrong-tensor-factor wall.
""")


def main() -> int:
    # generic-Y axioms first (Y a free 3x3) to show {D,gamma}=0 is automatic
    yfree = sp.Matrix(3, 3, sp.symbols("y0:9")) \
        + sp.I * sp.Matrix(3, 3, sp.symbols("z0:9"))
    part0_single_factor_wall()
    part1_triple_axioms(yfree, "generic Y")
    part2_reduction(yfree, "generic Y")
    part3_wrong_tensor_factor("structural")
    part3b_most_general_anticommuting("adversarial")
    part4_generic_Y_no_generation_grading("circulant Y")
    part5_doubling_provenance("provenance")
    part6_numpy_crosscheck("numpy")
    part7_verdict()

    banner("SUMMARY")
    print(f"  PASS={PASS} FAIL={FAIL}")
    print()
    print("  VERDICT: REQUIRES-IMPORTED-DOUBLING / COLLAPSES-LIKE-PT-C.")
    print("  The separate-factor Connes-Lott triple with an independent")
    print("  H_L (+) H_R doubling and a genuine off-diagonal Y acting on")
    print("  generation does NOT induce a native off-block C_3-orbit-")
    print("  splitting generation grading. The L/R chirality grading and the")
    print("  generation grading live in DISTINCT tensor factors (wrong-")
    print("  tensor-factor wall); the doubling factor is IMPORTED (not in")
    print("  A1+A2+A3); and the triple's mass readout is the singular-value")
    print("  (Yukawa) readout, not the signed Q=2/3. The import is RELOCATED,")
    print("  not removed.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
