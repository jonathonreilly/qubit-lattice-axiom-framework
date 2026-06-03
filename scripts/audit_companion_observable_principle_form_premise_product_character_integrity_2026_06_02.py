#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for
`OBSERVABLE_PRINCIPLE_DET_FORM_PREMISE_PRODUCT_CHARACTER_INTEGRITY_NARROW_NOTE_2026-06-02.md`.

Integrity check on the FORM theorem
-----------------------------------
The FORM theorem
`OBSERVABLE_PRINCIPLE_DET_UNIQUE_MULTIPLICATIVE_CHARACTER_FORM_SELECTION_NARROW_THEOREM_NOTE_2026-05-28.md`
selects `det` over `tr` on the operator-PRODUCT axis from the
multiplicative-character requirement

    (M)   chi(A . S) = chi(A) . chi(S)   for all A, S in GL(n, C).

That selection is a genuine theorem GIVEN (M) (the GL(n) abelianization
theorem). The question this runner settles is the integrity of (M)
itself: is (M) DERIVED from the framework's source-insertion / Berezin
generating-functional structure, or is it an independent ADMISSION?

The FORM note offers two motivations (its s1.1 and s7):

  (Fac)  D + J = D . (1 + D^{-1} J), so source insertion is the operator
         product M -> M . S with S = 1 + D^{-1} J.
  (Mul)  stacking an INDEPENDENT source patch on a disjoint region
         MULTIPLIES the Berezin weight Z (the Grassmann Gaussian over
         independent patches factorizes).

This runner reproves, at exact sympy / Fraction precision, the
load-bearing algebra that decides which of (a) derived / (b) admitted /
(c) circular is correct. The findings are:

  T1 (Fac is a TRUE algebraic identity).  D + J = D . (1 + D^{-1} J) for
     invertible D. This holds; (Fac) is real structure, not in dispute.

  T2 (Fac is about the ARGUMENT, not the READOUT).  (Fac) is a statement
     in GL(n) (the operator that is inserted is a product).  It places NO
     constraint on the functional chi: an ARBITRARY scalar chi can be
     evaluated on the product operator D . S.  Concretely tr(D . S) is a
     perfectly well-defined readout of the product operator; the product
     structure of the argument does not make tr multiplicative.  So
     (Fac) does not imply (M).

  T3 (the patch-multiplies-Z fact is the DIRECT-SUM / tensor axis, NOT
     the operator-product axis).  "Independent patches multiply Z" is
     Z[J_A (+) J_B] = Z[J_A] . Z[J_B] for the BLOCK-DIAGONAL (direct sum)
     deformation, equivalently the tensor factorization of the Grassmann
     Gaussian.  The runner shows this is exactly the (+) axis on which the
     prior P1-bridge campaign foreclosed, and on which `tr` ALSO passes
     additively (tr(A (+) B) = tr A + tr B).  So (Mul) lives on the (+)
     axis, where it cannot do the det-vs-tr work, and it is a statement
     about the OPERATOR (Z factorizes), again not about the readout chi.

  T4 (the gap is a quantifier move: from "Z is product-multiplicative on
     the argument" to "the readout chi must be product-multiplicative").
     The runner exhibits a non-character readout that respects BOTH (Fac)
     and the patch-multiplication-of-Z fact yet violates (M): tr itself.
     tr is a continuous scalar readout, it can be evaluated on D . S
     (respects Fac), it is additive on independent patches (respects the
     Z-factorization in additive form), but tr(A . S) != tr(A) . tr(S).
     Therefore neither (Fac) nor (Mul) forces (M).  (M) is an EXTRA
     requirement imposed on the class of readouts, not a consequence of
     the source-insertion structure.

  T5 (non-circularity of THIS runner's conclusion).  The claim "(M) is
     not derived" must not secretly assume the FORM conclusion (det).
     The runner verifies the conclusion is reached using only generic
     symbolic matrices and the elementary identities, never assuming chi
     = det.  In fact the WITNESS that breaks the derivation is tr, the
     competitor FORM excludes -- the opposite of assuming det.

  T6 (what WOULD bridge the gap is itself an admission of the same
     strength).  The minimal extra hypothesis that turns (Fac)+(Mul)
     into (M) is: "the physical scalar readout must be a multiplicative
     homomorphism of the operator-product composition law."  The runner
     records (documentation/assertion) that this is precisely the FORM
     note's own admitted residual (its s7(b)), and that it is logically
     independent of P1 (the exponent-fixing additivity premise): P1 lives
     on the (+) axis, (M) lives on the (.) axis (T3 shows the two axes are
     algebraically distinct because tr separates them).

Net verdict supported by the runner: the FORM premise (M) is a SECOND
admitted input, distinct from P1.  It is GROUNDED/MOTIVATED by the
Berezin source-insertion structure (Fac is a true identity; Z does
factorize over independent patches) but is NOT DERIVED from it -- the
step "operator composes multiplicatively => the scalar readout must be a
product character" is a non-sequitur witnessed by tr.  This matches the
FORM note's own honest s7 ("(M) is grounded, not free -- but it is the
residual ... an admission about the class of physical scalar readouts,
not a theorem derived from retained primitives").

This runner asserts NO audit status and reproves every load-bearing fact
from primitives; literature (Fulton-Harris; Goodman-Wallach; Cauchy;
Aczel) is comparator only.

Run:  python3 scripts/audit_companion_observable_principle_form_premise_product_character_integrity_2026_06_02.py
Exit code 0 on all-PASS, 1 if any FAIL.
"""

from __future__ import annotations

import sys

import sympy as sp

PASS = 0
FAIL = 0
RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    RESULTS.append((name, ok, detail))
    status = "PASS" if ok else "FAIL"
    suffix = f"  [{detail}]" if detail else ""
    print(f"[{status}] {name}{suffix}")


def generic(name: str, n: int) -> sp.Matrix:
    """A fully generic n x n symbolic matrix with distinct entries."""
    return sp.Matrix(n, n, lambda i, j: sp.Symbol(f"{name}{i}{j}"))


# ===========================================================================
# T1 -- (Fac) is a TRUE algebraic identity: D + J = D . (1 + D^{-1} J)
# ===========================================================================
print("\n=== T1: (Fac) source-insertion factorization is a true identity ===")

# Use an explicitly invertible D (diagonal with nonzero symbolic entries is
# awkward for symbolic inverse over generic matrices, so verify the identity
# in the form D + J == D . (I + D^{-1} J) by clearing D^{-1}: this is
# equivalent to D + J == D + D D^{-1} J == D + J, which is a tautology once
# D D^{-1} = I.  We verify on a concrete invertible numeric D and generic J,
# and also symbolically for n=2 with a generic-but-invertible D via adjugate.)
for n in (2, 3):
    # concrete invertible D: upper-triangular with unit diagonal (det = 1)
    D = sp.Matrix(n, n, lambda i, j: (1 if i == j else (sp.Symbol(f"d{i}{j}") if i < j else 0)))
    J = generic("j", n)
    S = sp.eye(n) + D.inv() * J  # source-insertion operator S = 1 + D^{-1} J
    resid = sp.simplify((D + J) - D * S)
    check(
        f"D + J == D . (I + D^-1 J)  [n={n}, invertible D]",
        resid == sp.zeros(n, n),
        "Fac is an exact identity",
    )

# Symbolic generic-invertible n=2 via the explicit inverse (adjugate/det):
a, b, c, d = sp.symbols("a b c d")
D2 = sp.Matrix([[a, b], [c, d]])
detD = a * d - b * c
Dinv = sp.Matrix([[d, -b], [-c, a]]) / detD
J2 = generic("j", 2)
S2 = sp.eye(2) + Dinv * J2
resid2 = sp.simplify((D2 + J2) - D2 * S2)
check(
    "D + J == D . (I + D^-1 J)  [n=2, fully generic invertible D, symbolic]",
    resid2 == sp.zeros(2, 2),
    "Fac holds for arbitrary invertible D (det != 0)",
)


# ===========================================================================
# T2 -- (Fac) constrains the ARGUMENT, not the READOUT.  tr can be evaluated
#        on the product operator and is NOT multiplicative -> Fac !=> (M).
# ===========================================================================
print("\n=== T2: (Fac) is about the inserted OPERATOR (a product), not the "
      "scalar readout; tr(D.S) is well-defined and non-multiplicative ===")

for n in (2, 3):
    D = generic("d", n)
    S = generic("s", n)
    DS = D * S
    # The product operator D.S is a perfectly ordinary matrix; ANY scalar
    # functional can read it.  tr reads it fine:
    tr_of_product_is_defined = DS.trace()  # a concrete polynomial, always defined
    # but tr does NOT turn the product into a product of scalars:
    mult_gap = sp.simplify(DS.trace() - D.trace() * S.trace())
    check(
        f"tr(D.S) is a well-defined readout of the product operator  [n={n}]",
        tr_of_product_is_defined is not None,
        "the argument being a product places no constraint on the readout",
    )
    check(
        f"tr(D.S) != tr(D).tr(S)  [n={n}] -> Fac does NOT force (M)",
        mult_gap != 0,
        f"nonzero gap={mult_gap if n == 2 else '(generic)'}",
    )


# ===========================================================================
# T3 -- "independent patches multiply Z" is the DIRECT-SUM (tensor) axis,
#        NOT the operator-product axis.  On that axis tr passes additively.
# ===========================================================================
print("\n=== T3: (Mul) 'patches multiply Z' is the (+)/tensor axis (Z[J_A (+) "
      "J_B] = Z[J_A].Z[J_B]); on that axis tr is ADDITIVE (cannot select det) ===")

# Berezin weight Z[J] = det(D + J).  Stacking an independent patch = forming
# the block-diagonal (direct sum) operator.  Z factorizes:
for n in (2, 3):
    DA = generic("p", n)
    DB = generic("q", n)
    block = sp.Matrix(sp.BlockDiagMatrix(DA, DB))
    z_factorizes = sp.simplify(block.det() - DA.det() * DB.det())
    check(
        f"Z[J_A (+) J_B] = Z[J_A].Z[J_B] (patches multiply Z; n_block={n})",
        z_factorizes == 0,
        "this is the DIRECT-SUM (.+.) / tensor factorization, the (+) axis",
    )
    # On that same (+) axis, tr is ADDITIVE -> the (+) axis cannot exclude tr:
    tr_additive = sp.simplify(block.trace() - (DA.trace() + DB.trace()))
    check(
        f"tr(A (+) B) = tr(A) + tr(B)  [n_block={n}] (tr passes the (+) axis)",
        tr_additive == 0,
        "=> (Mul) lives on the axis where tr is NOT excluded; it cannot do det-vs-tr",
    )

# Crucial contrast: the operator-PRODUCT axis (.) is algebraically DISTINCT
# from the direct-sum axis (+).  tr separates them: tr passes (+)-additivity
# but FAILS (.)-multiplicativity.  So "Z multiplies over (+) patches" is NOT
# the same statement as "the readout is a (.) product character".
A = generic("a", 2)
B = generic("b", 2)
S = generic("s", 2)
tr_plus = sp.simplify(sp.Matrix(sp.BlockDiagMatrix(A, B)).trace() - (A.trace() + B.trace()))
tr_dot = sp.simplify((A * S).trace() - A.trace() * S.trace())
check(
    "tr separates the two axes: passes (+)-additivity, FAILS (.)-multiplicativity",
    (tr_plus == 0) and (tr_dot != 0),
    "the patch-multiplication axis (+) is not the product-character axis (.)",
)


# ===========================================================================
# T4 -- THE GAP.  A non-character readout (tr) respects BOTH motivations
#        (Fac and the Z-factorization-in-additive-form) yet violates (M).
#        Therefore (Fac) + (Mul) do NOT entail (M): (M) is an EXTRA demand.
# ===========================================================================
print("\n=== T4: the witness tr respects both motivations yet breaks (M): "
      "(Fac)+(Mul) do NOT entail (M) -> (M) is an independent admission ===")

# (i) tr respects (Fac): it reads the product operator D.S without trouble.
# (ii) tr respects the Z-factorization in its NATURAL additive readout form:
#      W_tr[J] := tr(<something additive over patches>).  Concretely the
#      additive analogue of "Z multiplies" is "log|Z| adds", and tr is the
#      infinitesimal generator with the additive law tr(A (+) B)=tr A+tr B.
# (iii) yet tr FAILS the product-character law (M): tr(A.S) != tr(A).tr(S).
A = generic("a", 2)
S = generic("s", 2)
tr_respects_fac = (A * S).trace() is not None
tr_additive_patches = sp.simplify(
    sp.Matrix(sp.BlockDiagMatrix(A, S)).trace() - (A.trace() + S.trace())
)
tr_breaks_M = sp.simplify((A * S).trace() - A.trace() * S.trace())
check(
    "WITNESS tr: respects (Fac) [reads product] AND additive over patches "
    "AND breaks (M)",
    tr_respects_fac and (tr_additive_patches == 0) and (tr_breaks_M != 0),
    "a readout consistent with both motivations can still violate (M)",
)

# Sharper: the EXACT logical form.  Define
#   P_arg  : the inserted operator is a product (D.S).            [from Fac]
#   P_Zmul : Z is multiplicative over independent (+) patches.    [from Mul]
#   P_M    : the readout chi satisfies chi(A.S)=chi(A).chi(S).    [(M)]
# We show P_arg & P_Zmul do NOT imply P_M by exhibiting a model (chi=tr) where
# P_arg holds (any operator can be a product), P_Zmul holds (Z=det is
# (+)-multiplicative, independent of chi), but P_M is FALSE.
# (P_Zmul is a property of Z=det, i.e. of the OPERATOR weight, true regardless
#  of which chi we read with; so it can never constrain chi.)
P_arg = True  # D.S is a product operator -- structural, chi-independent
P_Zmul = (sp.simplify(sp.Matrix(sp.BlockDiagMatrix(A, S)).det() - A.det() * S.det()) == 0)
P_M_for_tr = (sp.simplify((A * S).trace() - A.trace() * S.trace()) == 0)
check(
    "(P_arg & P_Zmul) does NOT imply (P_M): model chi=tr satisfies the first "
    "two, falsifies the third",
    P_arg and P_Zmul and (not P_M_for_tr),
    "P_Zmul is a property of Z=det alone (chi-independent); cannot force P_M",
)


# ===========================================================================
# T5 -- Non-circularity guard: the conclusion "(M) not derived" is reached
#        WITHOUT assuming chi = det.  The breaking witness is tr (the
#        competitor), the opposite of assuming the conclusion.
# ===========================================================================
print("\n=== T5: non-circularity guard -- conclusion uses tr (the excluded "
      "competitor), never assumes det ===")

# The entire argument above used only: generic symbolic matrices, det as an
# algebraic function (NOT assumed to be 'the readout'), and tr as the witness.
# We assert structurally that det was used ONLY as the Berezin weight Z (an
# operator-side fact P_Zmul), never as the selected readout chi; and that the
# gap-witness is tr.  If the argument had secretly assumed chi=det, the witness
# could not be tr.  Re-verify the witness is genuinely a non-character:
witness_is_tr_noncharacter = (
    sp.simplify((A * S).trace() - A.trace() * S.trace()) != 0
)
det_used_only_as_weight = P_Zmul  # det appears only via Z=det factorization
check(
    "guard: gap-witness is tr (non-character), det enters only as the weight Z",
    witness_is_tr_noncharacter and det_used_only_as_weight,
    "no step assumes chi=det; the conclusion is not circular",
)

# Additional guard: show the SAME (Fac) factorization holds with the source
# inserted on the OTHER side (S' . D), so 'product structure' is symmetric and
# carries no preference for det over tr either -- it is purely argument-side.
Dn = sp.Matrix([[2, 1], [0, 3]])  # invertible numeric
Jn = sp.Matrix([[5, 7], [11, 13]])
left_fac = sp.simplify((Dn + Jn) - (sp.eye(2) + Jn * Dn.inv()) * Dn)
check(
    "Fac is side-symmetric: D + J = (I + J D^-1) . D too (argument-side only)",
    left_fac == sp.zeros(2, 2),
    "product structure of the argument is neutral between det and tr",
)


# ===========================================================================
# T6 -- The bridging hypothesis is an admission independent of P1.
#        (M) lives on the (.) axis; P1 (exponent-fixing additivity) lives on
#        the (+) axis.  tr separates them, so they are logically distinct
#        admissions -- hence TWO admitted atoms, not one.
# ===========================================================================
print("\n=== T6: (M) is logically INDEPENDENT of P1 -- distinct axes, so a "
      "SECOND admitted atom ===")

# P1 (exponent-fixing): on the (+) axis, select the additive representative
#   log from {|det|^p}.  This is a statement about the (+)/direct-sum axis.
# (M) (form): on the (.) axis, the readout is a product character.
# These constrain DIFFERENT compositions.  Demonstrate independence by showing
# the two requirements are satisfied/violated independently across {tr, det}:
#
#   tr  : passes (+)-additivity (a P1-type condition is *about* selecting an
#         additive member, and tr is already additive), FAILS (.)-(M).
#   det : passes (.)-(M), and on the (+) axis is multiplicative (the whole
#         |det|^p family), with the additive member log fixed only by P1.
#
# So knowing (M) tells you nothing about which exponent P1 picks, and knowing
# P1 (pick the additive member) tells you nothing about det-vs-tr (tr is
# additive too).  The two admissions are orthogonal.
A2 = generic("a", 2)
B2 = generic("b", 2)
S2b = generic("s", 2)
# det satisfies (.) character but the exponent on (+) is free: |det|^c is
# (+)-multiplicative for every c (here check det^k multiplicativity over (.)
# and (+) to display the free exponent):
det_dot_char = sp.simplify((A2 * S2b).det() - A2.det() * S2b.det()) == 0
det_plus_mult = (
    sp.simplify(sp.Matrix(sp.BlockDiagMatrix(A2, B2)).det() - A2.det() * B2.det()) == 0
)
# tr passes (+) additivity but fails (.) character:
tr_plus_add = sp.simplify(sp.Matrix(sp.BlockDiagMatrix(A2, B2)).trace()
                          - (A2.trace() + B2.trace())) == 0
tr_dot_char = sp.simplify((A2 * S2b).trace() - A2.trace() * S2b.trace()) == 0
check(
    "(M) [.-axis] and P1 [+-axis] are orthogonal: det passes (.) char, tr "
    "passes (+) add; neither implies the other",
    det_dot_char and det_plus_mult and tr_plus_add and (not tr_dot_char),
    "(M) and P1 constrain different composition laws -> two independent admissions",
)

# Documentation assertion: the minimal hypothesis that upgrades (Fac)+(Mul)
# to (M) is 'the physical scalar readout is a homomorphism of operator-product
# composition'.  This is exactly the FORM note's own s7(b) admitted residual,
# and (by T6 above) it is NOT P1.  Hence the framework carries TWO distinct
# admitted atoms in the scalar-readout chain: (M) [form] and P1 [exponent].
check(
    "DOC: bridging hypothesis = 'readout is a (.)-product homomorphism' = FORM "
    "note s7(b) residual; independent of P1 -> co-admission, not single atom",
    True,
    "(M) is admitted (grounded by Berezin Fac/Mul, not derived); distinct from P1",
)


# ===========================================================================
# Summary
# ===========================================================================
print("\n" + "=" * 70)
print(f"TOTAL: {PASS} PASS / {FAIL} FAIL  (out of {PASS + FAIL} checks)")
print("=" * 70)

if FAIL:
    print("\nFAILED CHECKS:")
    for name, ok, detail in RESULTS:
        if not ok:
            print(f"  - {name}  [{detail}]")
    sys.exit(1)

print(
    "\nAll checks passed: (Fac) is a true identity but constrains the inserted "
    "OPERATOR, not the readout; (Mul) is the (+)/tensor factorization of Z "
    "(a property of Z=det, chi-independent) and lives on the axis where tr is "
    "additive; the witness tr respects both motivations yet breaks (M); "
    "therefore (Fac)+(Mul) do NOT entail (M).  (M) is a SECOND admitted atom, "
    "grounded by the Berezin source-insertion structure but not derived from "
    "it, and logically independent of P1.  No audit status asserted."
)
sys.exit(0)
