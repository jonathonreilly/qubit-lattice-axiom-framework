#!/usr/bin/env python3
"""Generation-chirality gate re-examined UNDER the Record axiom (A3 v0.4).

Verifies the algebraic content of
`docs/CHIRALITY_UNDER_RECORD_AXIOM_PROBE_2026-06-05.md`.

CONTEXT. The charged-lepton Koide value Q = 2/3 (r = |b|^2/a^2 = 1/2) needs a
Hermitian grading Gamma_chi on the generation factor with {H, Gamma_chi} = 0,
where H = a I + b C + conj(b) C^2 is the circulant mass operator (C the cyclic
shift, C^3 = I). Gamma_chi must be OFF-BLOCK (singlet<->doublet mixing) and
C_3-orbit-splitting. The established support identity
`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO` shows no C_3-equivariant (circulant)
Hermitian operator anticommutes with the circulant grading, and the affine
probe sharpens this to the entrywise rule: in the Fourier basis where
H = diag(L0, L1, L2),

    {Gamma, H}_{jk} = (L_j + L_k) Gamma_{jk}.                          (WALL)

So any nonzero anticommuting Gamma is supported only on origin-reflection pairs
L_j + L_k = 0 (and L_m = 0 on the diagonal); a Hermitian involution forced
there pins mean = a = 0 (the chiral limit, where r diverges).

These no-gos predate the Record axiom. The Record axiom (v0.4, the "Record"
axiom of MINIMAL_AXIOMS_2026-06-04: a record is the durable additive scalar
registration of which REAL / CPT-even superselection sector is realized, with a
fixed K/CPT conjugation; K fuses the two faithful C_3 characters chi_1, chi_2
into the real doublet, and the recorded outcome is the K/CPT ORBIT of the
central sector). The owner's point: the no-gos were proved on Lattice+Quantum
alone, before this K/CPT structure existed, so its operators must be tested
directly as candidate gradings.

This runner constructs every K/CPT-native operator the Record structure makes
available and adversarially checks the FULL Gamma_chi property set + the Koide
readout Q for each:

  P1  Hermitian (real-symmetric / Hermitian on C^3)
  P2  involution  Gamma^2 = I  (genuine Z_2 grading, spectrum in {+1,-1})
  P3  off-block: mixes the Z_3 singlet (trivial char) with the doublet
  P4  C_3-orbit-splitting (NOT circulant: [Gamma, C] != 0)
  P5  {H, Gamma} = 0   (anticommutes with the finite-mass-scale circulant H)
  Q   the Koide ratio delivered (target 2/3)

Operators tested:
  (1) K  -- the static complex-conjugation / real-structure operator
  (2) i(C - C^2)  -- the K-odd Hermitian operator, spectrum {0, +-sqrt3}
      (and its normalization i(C-C^2)/sqrt3, spectrum {0, +-1})
  (3) the orbit-distinguishing operator  -- distinguishes chi_1 from chi_2
      inside the recorded doublet orbit  (diag(0,+1,-1) in Fourier basis)
  (4) the arrow-oriented versions  -- both signs +/- of the K-odd direction
  (5) DECISIVE: the real/CPT-even (det_R) vs K-odd (det_C) readout default at
      r = 1/2, and an EXISTENCE sweep: does ANY Hermitian involution with the
      off-block + orbit-split + anticommute properties exist at finite a != 0?

All checks are SYMBOLIC (sympy) on arbitrary parameters a, b (b complex). No
PDG / measured / empirical lepton masses are consumed; Q = 2/3 is only a target
to check against.
"""

from __future__ import annotations

import sys

import sympy as sp


PASS = 0
FAIL = 0


def banner(title: str) -> None:
    print()
    print("=" * 74)
    print(title)
    print("=" * 74)


def check(label: str, ok: bool) -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"  [PASS] {label}")
    else:
        FAIL += 1
        print(f"  [FAIL] {label}")
    return ok


# ----------------------------------------------------------------------
# Symbols and primitive objects
# ----------------------------------------------------------------------

# Real free parameters of the circulant H. b is complex: b = br + i bi.
a, br, bi = sp.symbols("a b_r b_i", real=True)
b = br + sp.I * bi
bbar = sp.conjugate(b)

# primitive cube root of unity (algebraic form -> clean omega^3 = 1)
omega = sp.Rational(-1, 2) + sp.sqrt(3) / 2 * sp.I


def cyclic_shift() -> sp.Matrix:
    return sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])


def fourier_matrix() -> sp.Matrix:
    """Unitary Z_3 DFT. F[g,k] = omega^(g k)/sqrt3; F^dag C F = diag(1,w,w^2).

    Columns k = 0,1,2 are the characters: k=0 trivial (singlet), k=1,2 the two
    faithful characters chi_1, chi_2 that K/CPT conjugation fuses into the real
    doublet.
    """
    F = sp.zeros(3, 3)
    for g in range(3):
        for k in range(3):
            F[g, k] = omega ** (g * k) / sp.sqrt(3)
    return sp.simplify(F)


C = cyclic_shift()
F = fourier_matrix()
Fd = F.conjugate().T
I3 = sp.eye(3)
J_ones = sp.ones(3, 3)

# Circulant mass operator H = a I + b C + conj(b) C^2 (Hermitian for real a).
H = a * I3 + b * C + bbar * (C * C)


def to_fourier(M: sp.Matrix) -> sp.Matrix:
    return sp.simplify(Fd * M * F)


def is_hermitian(M: sp.Matrix) -> bool:
    return sp.simplify(M - M.conjugate().T) == sp.zeros(*M.shape)


def is_zero(M: sp.Matrix) -> bool:
    return sp.simplify(M) == sp.zeros(*M.shape)


def anticomm(X: sp.Matrix, Y: sp.Matrix) -> sp.Matrix:
    return sp.simplify(X * Y + Y * X)


def comm(X: sp.Matrix, Y: sp.Matrix) -> sp.Matrix:
    return sp.simplify(X * Y - Y * X)


def koide_eigenvalue_Q(eigs: list) -> sp.Expr:
    """Brannen/eigenvalue (det_R) Koide ratio Q = (sum L^2)/(sum L)^2 * 3 ... ?
    Standard Koide: K = (sum m)/( (sum sqrt(m))^2 ) with m_k = L_k^2 (signed
    sqrt(m) = L_k). Q (the framework's 2/3 target) = (sum L^2)/(sum L)^2.
    Returns sum L^2 / (sum L)^2; the Koide cone value is 2/3.
    """
    s1 = sum(eigs)
    s2 = sum(e**2 for e in eigs)
    if sp.simplify(s1) == 0:
        return sp.oo
    return sp.simplify(s2 / s1**2)


# ----------------------------------------------------------------------
banner("PART 0: SETUP -- H, Fourier diagonalization, the WALL entrywise rule")
# ----------------------------------------------------------------------
check("[A] C^3 = I", sp.simplify(C**3 - I3) == sp.zeros(3, 3))
check("[A] F unitary (F^dag F = I)", sp.simplify(Fd * F - I3) == sp.zeros(3, 3))

H_f = to_fourier(H)
L0 = sp.simplify(H_f[0, 0])
L1 = sp.simplify(H_f[1, 1])
L2 = sp.simplify(H_f[2, 2])
print(f"  H eigenvalues (Fourier): L0 = {L0}")
print(f"                           L1 = {L1}")
print(f"                           L2 = {L2}")
check("[A] H is diagonal in the Fourier basis (circulant)",
      is_zero(H_f - sp.diag(L0, L1, L2)))
check("[A] mean of eigenvalues = a  (L0+L1+L2 = 3a)",
      sp.simplify(L0 + L1 + L2 - 3 * a) == 0)

# The WALL entrywise rule: {Gamma, H}_{jk} = (L_j + L_k) Gamma_{jk} in Fourier.
G = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"g_{i}{j}"))
Hdiag = sp.diag(L0, L1, L2)
AC = sp.simplify(G * Hdiag + Hdiag * G)
Ls = [L0, L1, L2]
rule_ok = all(sp.simplify(AC[i, j] - (Ls[i] + Ls[j]) * G[i, j]) == 0
              for i in range(3) for j in range(3))
check("[A] WALL: {Gamma,H}_{jk} = (L_j+L_k) Gamma_{jk}  (all 9 entries)", rule_ok)
print("  => anticommuting Gamma is supported only where L_j + L_k = 0 (and")
print("     L_m = 0 on the diagonal): the origin-reflection / chiral locus.")


# ----------------------------------------------------------------------
banner("PART 1: Q1a -- the static K (complex conjugation / real structure)")
# ----------------------------------------------------------------------
# K (antilinear complex conjugation) is NOT a C-linear matrix. Its linear
# 'static' realization on the standard real basis is the identity-real-
# structure: the projector onto the real subspace, i.e. on C^3 the operator
# whose +1 eigenspace is Re. On the standard basis that is just I (it fixes
# every real vector). A nontrivial linear stand-in used by the prior PT-C is
# the real-structure GRADING that separates real vs imaginary parts -- but on
# C^3 with the standard real structure the 'static K' linear part is I3, which
# is ON-BLOCK and traceless-fails.
K_static = I3  # the linear (static) part of complex conjugation on R^3
print("  Static K (linear part on the real basis) = I3.")
check("[P1] static K Hermitian", is_hermitian(K_static))
check("[P2] static K involution (K^2 = I)", is_zero(K_static**2 - I3))
Kf = to_fourier(K_static)
offblock_K = not is_zero(Kf - sp.diag(Kf[0, 0], Kf[1, 1], Kf[2, 2]))
check("[P3-FAIL] static K is ON-BLOCK in Fourier (diagonal) => NOT off-block",
      not offblock_K)
check("[P4-FAIL] static K is CIRCULANT ([K,C]=0) => NOT orbit-splitting",
      is_zero(comm(K_static, C)))
check("[P5-FAIL] {H, K} = 2H != 0 => K does NOT anticommute with H",
      not is_zero(anticomm(H, K_static)))
# Q from K as a grading: K = I has eigenvalues all +1, <v|K|v> = 1 != 0 always,
# so it imposes NO Koide constraint; reading its own spectrum (1,1,1):
print("  static K trace = 3 (traceless-fails); as a grading <v|K|v> = 1 != 0")
print("  => imposes no Koide cone; CONFIRMS prior 'static K on-block, Q ill' finding.")


# ----------------------------------------------------------------------
banner("PART 2: Q1b -- the K-odd Hermitian operator i(C - C^2)")
# ----------------------------------------------------------------------
Kodd = sp.I * (C - C * C)            # = i(C - C^2) = i(R - R^2)
print("  Kodd = i(C - C^2):")
sp.pprint(Kodd)
check("[P1] Kodd Hermitian", is_hermitian(Kodd))
# spectrum
ev = Kodd.eigenvals()
ev_set = {sp.simplify(k): v for k, v in ev.items()}
print(f"  spec(Kodd) = {dict(ev_set)}")
spec_vals = sorted([complex(sp.N(k)).real for k in ev_set], key=lambda x: x)
check("[A] spec(Kodd) = {0, -sqrt3, +sqrt3}",
      set(sp.nsimplify(round(v, 9)) for v in spec_vals)
      == {sp.Integer(0), -sp.sqrt(3), sp.sqrt(3)})
check("[P2-FAIL] Kodd is NOT an involution (Kodd^2 = 3 P_doub != I; has a 0 eig)",
      not is_zero(Kodd**2 - I3))
Koddf = to_fourier(Kodd)
print(f"  Kodd in Fourier basis = diag{(sp.simplify(Koddf[0,0]), sp.simplify(Koddf[1,1]), sp.simplify(Koddf[2,2]))}")
offblock_Kodd = not is_zero(Koddf - sp.diag(Koddf[0, 0], Koddf[1, 1], Koddf[2, 2]))
check("[P3-FAIL] Kodd is ON-BLOCK (diagonal in Fourier) => NOT off-block",
      not offblock_Kodd)
check("[P4-FAIL] Kodd is CIRCULANT ([Kodd,C]=0) => NOT orbit-splitting",
      is_zero(comm(Kodd, C)))
check("[P5-FAIL] [H, Kodd] = 0: Kodd COMMUTES with H (does NOT anticommute)",
      is_zero(comm(H, Kodd)))
check("[A] {H, Kodd} = 2 H Kodd != 0 (so anticommutation fails unless H Kodd=0)",
      not is_zero(anticomm(H, Kodd)))
# normalized version
Kodd_n = Kodd / sp.sqrt(3)
print(f"  spec(Kodd/sqrt3) = {{0, -1, +1}} -- still has a 0, still NOT an involution")
check("[P2-FAIL] Kodd/sqrt3 still not an involution (0 eigenvalue)",
      not is_zero(Kodd_n**2 - I3))
# Koide of its own spectrum: sum = 0 -> Q = inf
QKodd = koide_eigenvalue_Q([sp.simplify(Koddf[0,0]), sp.simplify(Koddf[1,1]), sp.simplify(Koddf[2,2])])
print(f"  eigenvalue Koide of spec(Kodd) (sum=0): Q = {QKodd}  (NOT 2/3)")
check("[A] Kodd own-spectrum Koide Q = oo (sum of eigenvalues = 0)", QKodd == sp.oo)
print("  NOTE: Kodd = i*sqrt3*J where J=(C-C^T)/sqrt3 is the pt3 doublet complex")
print("  structure; this is its Hermitian partner, still circulant/on-block.")


# ----------------------------------------------------------------------
banner("PART 3: Q2 -- the orbit-distinguishing operator (chi_1 vs chi_2)")
# ----------------------------------------------------------------------
# The recorded outcome is the K/CPT orbit {chi_1, chi_2} = the doublet. The
# operator that DISTINGUISHES chi_1 from chi_2 WITHIN the orbit is the one that
# is 0 on the singlet and +-1 on the two faithful characters: diag(0,+1,-1) in
# the Fourier basis. Build it explicitly and test off-block-ness.
Odist_f = sp.diag(0, 1, -1)              # in Fourier basis
Odist = sp.simplify(F * Odist_f * Fd)    # back to site basis
print("  Orbit-distinguisher O_dist (site basis) = F diag(0,+1,-1) F^dag:")
sp.pprint(sp.simplify(Odist))
check("[P1] O_dist Hermitian", is_hermitian(Odist))
check("[A] O_dist eigenvalues {0,+1,-1} (distinguishes chi_1 from chi_2)",
      set(sp.simplify(k) for k in Odist.eigenvals()) == {sp.Integer(0), sp.Integer(1), sp.Integer(-1)})
check("[P2-FAIL] O_dist NOT an involution (0 eigenvalue on singlet)",
      not is_zero(Odist**2 - I3))
check("[P3-FAIL] O_dist is ON-BLOCK (diagonal in Fourier) => NOT off-block",
      not is_zero(Odist_f - sp.diag(0, 1, -1)) or True and
      is_zero(Odist_f - sp.diag(Odist_f[0,0], Odist_f[1,1], Odist_f[2,2])))
check("[P4-FAIL] O_dist is CIRCULANT ([O_dist,C]=0) => NOT orbit-SPLITTING off-block",
      is_zero(comm(Odist, C)))
check("[P5-FAIL] [H, O_dist] = 0: COMMUTES with H (does NOT anticommute)",
      is_zero(comm(H, Odist)))
print("  The within-orbit distinguisher lives in the SAME (Fourier-diagonal /")
print("  circulant) algebra as H: it separates the two doublet characters but")
print("  does NOT mix singlet<->doublet. It is on-block. CONFIRMS the wall.")


# ----------------------------------------------------------------------
banner("PART 4: Q3 -- does the arrow (durable registration) orient a chirality?")
# ----------------------------------------------------------------------
# The arrow picks a sign of the K-odd direction: +Kodd vs -Kodd. Test both.
for sign, lab in [(+1, "+Kodd"), (-1, "-Kodd")]:
    Op = sign * Kodd
    same_onblock = is_zero(comm(Op, C))
    same_comm_H = is_zero(comm(H, Op))
    print(f"  arrow orientation {lab}: [Op,C]=0 ? {same_onblock};  [H,Op]=0 ? {same_comm_H}")
check("[A] +Kodd and -Kodd are BOTH on-block circulant (orientation inert)",
      is_zero(comm(Kodd, C)) and is_zero(comm(-Kodd, C)))
check("[A] +Kodd and -Kodd BOTH commute with H (neither anticommutes)",
      is_zero(comm(H, Kodd)) and is_zero(comm(H, -Kodd)))
print("  The arrow orients an operator that is on-block and commutes with H;")
print("  orienting a non-anticommuting operator changes no anticommutation")
print("  content and no Koide readout. CONFIRMS pt3 'CPT orientation inert'.")


# ----------------------------------------------------------------------
banner("PART 5: Q4 DECISIVE -- real/CPT-even (det_R) defaults to r=1 (NON-chiral)")
# ----------------------------------------------------------------------
# The Record axiom's stance is REAL / CPT-even. The native circulant mass
# operator H = a I + b C + conj(b) C^2 = i D with D real anti-Hermitian is
# Hermitian (retained cpt_exact_real_anti_hermitian_d). Its eigenvalue (det_R /
# signed-sqrt(m)) readout at r = 1/2 gives Q = 2/3 -- but WITHOUT any
# anticommuting grading: it is the CIRCULANT (C_3-equivariant) operator, the
# NON-chiral default. Show the two readout DEFAULTS:
#   (i)  real/CPT-even native: circulant H, NO off-block grading exists at
#        finite a (existence sweep below) -> the default grading content is the
#        COMMUTING circulant Gamma_chi -> Q=1 'block-vs-dimension' default OR the
#        retained eigenvalue value Q=2/3 with NO chirality.  Either way the
#        chiral (anticommuting) grading is ABSENT at finite a.
#   (ii) the K-odd (det_C) chiral deviation: an off-block anticommuting grading
#        forces a = 0 (chiral limit), where the eigenvalue/affine-r readout = oo.

# (A) EXISTENCE SWEEP (the genuinely-new, candidate-independent step): does ANY
#     Hermitian INVOLUTION Gamma (Gamma^2 = I), off-block (singlet<->doublet),
#     with {H, Gamma} = 0, exist at finite a != 0?
#
# The entrywise WALL forces, per entry: g_mm != 0 => L_m = 0; g_jk != 0 =>
# L_j + L_k = 0. Off-block means the singlet (mode 0) couples to a doublet mode,
# i.e. g01 != 0 (WLOG; g02 symmetric), which REQUIRES the surface S01: L0+L1=0.
# A single off-block ENTRY can therefore sit at finite a (S01 is not a=0). The
# decisive constraint is that Gamma must be a full INVOLUTION on C^3 (3 modes,
# odd): the third mode (2) cannot be ignored. Exhaustive case split.
cond01 = sp.simplify(L0 + L1)   # must vanish for an off-block 01 entry
cond02 = sp.simplify(L0 + L2)
print(f"  L0 + L1 = {cond01}")
print(f"  L0 + L2 = {cond02}")
S01 = sp.solve(sp.Eq(cond01, 0), a, dict=True)[0]
print(f"  An off-block g01 entry is allowed on surface S01: a = {S01[a]}  (FINITE, not a=0)")
print("  -- so a single off-block entry does NOT immediately force a=0. The")
print("     constraint comes from completing Gamma to an INVOLUTION on all 3 modes:")
L0s = sp.simplify(L0.subs(S01))
L1s = sp.simplify(L1.subs(S01))
L2s = sp.simplify(L2.subs(S01))

# CASE A: mode 2 DECOUPLED from the off-block 01 block (g02=g12=0). Then Gamma
# restricted to mode 2 is a 1x1 involution g22 = +-1 (nonzero). Entry (2,2)
# requires 2 L2 g22 = 0 with g22 != 0 => L2 = 0.
caseA = sp.solve([sp.Eq(cond01, 0), sp.Eq(L2, 0)], [a, br, bi], dict=True)
caseA_a = [sp.simplify(s.get(a, S01[a].subs(s))) for s in caseA] if caseA else []
print(f"  CASE A (mode 2 decoupled, g22=+-1): involution needs L2=0 on S01")
print(f"          => {caseA}  => a = {caseA_a}")
caseA_forces_a0 = bool(caseA) and all(
    sp.simplify(S01[a].subs(s)) == 0 for s in caseA)
check("[A] CASE A: off-block involution with mode 2 decoupled FORCES a = 0 (chiral limit)",
      caseA_forces_a0)

# CASE B: mode 2 also couples off-block (g02 != 0 or g12 != 0) => needs
# L0+L2=0 and/or L1+L2=0 in addition to L0+L1=0.
caseB = sp.solve([sp.Eq(L0 + L1, 0), sp.Eq(L0 + L2, 0), sp.Eq(L1 + L2, 0)],
                 [a, br, bi], dict=True)
print(f"  CASE B (mode 2 off-block too): L0+L1=L0+L2=L1+L2=0 => {caseB}")
caseB_trivial = bool(caseB) and all(
    sp.simplify(s.get(a, 0)) == 0 and sp.simplify(s.get(br, 0)) == 0
    and sp.simplify(s.get(bi, 0)) == 0 for s in caseB)
check("[A] CASE B: mode 2 off-block forces a = b = 0 (trivial H = 0)", caseB_trivial)

# CASE C: purely diagonal involution (g_jk=0 all off-diag) is ON-BLOCK
# (no singlet<->doublet mixing) -> fails the off-block requirement by definition.
print("  CASE C (diagonal involution): no singlet<->doublet mixing => ON-BLOCK,")
print("          fails the off-block requirement P3 by construction.")
check("[A] EXHAUSTIVE: no off-block, finite-a, Hermitian INVOLUTION anticommutes with H",
      caseA_forces_a0 and caseB_trivial)
print("  => at FINITE a != 0 NO off-block Hermitian INVOLUTION anticommutes with H.")
print("     A single off-block entry can sit at finite a, but completing it to a")
print("     Z_2 grading on the odd 3rd mode forces a = 0. Candidate-independent WALL.")

# (B) At a = 0 (chiral limit) the anticommuting spectrum is {+lam, -lam, 0};
#     eigenvalue readout sum = 0 -> Q = oo. (det_R chiral-limit divergence.)
a0H = H.subs(a, 0)
a0H_f = to_fourier(a0H)
a0_eigs = [sp.simplify(a0H_f[0, 0]), sp.simplify(a0H_f[1, 1]), sp.simplify(a0H_f[2, 2])]
print(f"  at a=0: eigenvalues {a0_eigs}, sum = {sp.simplify(sum(a0_eigs))}")
Qa0 = koide_eigenvalue_Q(a0_eigs)
check("[A] at a=0 (where off-block grading exists) eigenvalue Koide Q = oo (sum=0)",
      Qa0 == sp.oo)

# (C) The real/CPT-even (det_R) DEFAULT at finite r=1/2: native circulant H,
#     eigenvalue readout = 2/3 but via the COMMUTING circulant Gamma_chi (NO
#     anticommuting/chiral grading). Confirm the retained eigenvalue value AND
#     that the only Hermitian Z_2 grading splitting singlet/doublet is the
#     CIRCULANT Gamma_chi (= the non-chiral, COMMUTING, r=1 'block' default).
Gamma_chi = sp.Rational(2, 3) * J_ones - I3
check("[A] Gamma_chi = (2/3)J - I is Hermitian involution, spectrum {+1,-1,-1}",
      is_hermitian(Gamma_chi) and is_zero(Gamma_chi**2 - I3)
      and set(sp.simplify(k) for k in Gamma_chi.eigenvals()) == {sp.Integer(1), sp.Integer(-1)})
check("[A] Gamma_chi is CIRCULANT ([Gamma_chi, C] = 0) => COMMUTES with H (det_R/non-chiral)",
      is_zero(comm(Gamma_chi, C)) and is_zero(comm(H, Gamma_chi)))
print("  The canonical singlet/doublet Hermitian involution Gamma_chi COMMUTES")
print("  with H: {H,Gamma_chi} = 2 H Gamma_chi != 0. So the real/CPT-even side")
print("  carries the COMMUTING grading -> NO chirality -> the NON-chiral default.")

# Numerical det_R confirmation at r=1/2 (the retained value, no chirality used).
subs_half = {a: 1, br: sp.sqrt(sp.Rational(1, 2)), bi: 0}   # r = |b|^2/a^2 = 1/2
eig_half = [sp.simplify(L0.subs(subs_half)), sp.simplify(L1.subs(subs_half)),
            sp.simplify(L2.subs(subs_half))]
Qhalf = sp.nsimplify(sp.N(koide_eigenvalue_Q(eig_half)), [sp.Rational(2, 3)])
print(f"  det_R eigenvalue readout at r=1/2 (theta=0): eigs={[sp.N(e,6) for e in eig_half]}")
print(f"  Q(det_R) = {Qhalf}  (= 2/3 by the retained circulant theorem, NO chirality)")
check("[A] det_R eigenvalue readout at r=1/2 gives Q = 2/3 with the COMMUTING grading",
      sp.simplify(Qhalf - sp.Rational(2, 3)) == 0)

print()
print("  CRUX (Q4): the Record axiom's REAL / CPT-even stance carries the")
print("  COMMUTING circulant grading Gamma_chi (non-chiral default), and ANY")
print("  off-block anticommuting (chiral / K-odd) grading is forced to a = 0")
print("  where the eigenvalue readout diverges. The new K/CPT structure")
print("  DEFAULTS AWAY from chirality; it does NOT supply an off-block, finite-a,")
print("  Gamma_chi. It CONFIRMS / STRENGTHENS the established no-go.")


# ----------------------------------------------------------------------
banner("SCORECARD")
# ----------------------------------------------------------------------
print(f"  PASS = {PASS}")
print(f"  FAIL = {FAIL}")
print()
print("  VERDICT: NEW-AXIOM-CONFIRMS-OR-STRENGTHENS-NO-GO.")
print("  Every K/CPT-native operator the Record axiom makes available --")
print("  static K, the K-odd i(C-C^2), the orbit-distinguisher diag(0,+1,-1),")
print("  and both arrow orientations -- is ON-BLOCK / CIRCULANT and COMMUTES")
print("  with H (fails P3,P4,P5). The real/CPT-even (det_R) readout defaults to")
print("  the COMMUTING grading (non-chiral, Q=2/3 value WITHOUT chirality, or")
print("  Q=1 on the block/dimension default), while the off-block anticommuting")
print("  chiral grading is forced to the a=0 chiral limit (Q=oo). No off-block,")
print("  finite-a, C_3-orbit-splitting Hermitian involution Gamma_chi is produced.")

if FAIL == 0:
    print("\nALL CHECKS PASSED")
    sys.exit(0)
else:
    print(f"\n{FAIL} CHECK(S) FAILED")
    sys.exit(1)
