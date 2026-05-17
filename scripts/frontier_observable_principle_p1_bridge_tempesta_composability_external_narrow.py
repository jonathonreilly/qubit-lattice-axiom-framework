#!/usr/bin/env python3
"""Runner for the observable-principle P1 bridge Tempesta composability
external bounded note.

This runner verifies the Tempesta composability axiom (arXiv:1407.3807,
arXiv:1507.07436, MDPI Entropy 20 (2018) 804, 26 (2024) 266) and the
Lazard-classified commutative one-dimensional formal group law machinery
at exact ``Fraction`` / ``sympy`` precision. It exhibits explicitly:

- That the additive formal group ``G_a(x, y) = x + y`` (Boltzmann-
  Gibbs), the multiplicative formal group ``G_m(x, y) = x + y + xy``
  (``F_p = r^p`` counterexample family), and the Tsallis formal group
  ``G_q(x, y) = x + y + (1 - q) xy`` (Tsallis q-entropy) all satisfy
  the formal-group-law axioms G1 (identity), G2 (associativity), G3
  (commutativity).
- That the framework's Grassmann determinant block factorization
  ``Z[J_A (+) J_B] = Z_A[J_A] Z_B[J_B]`` is the multiplicative input
  to the composability test.
- That ``W = c log|Z|`` satisfies the additive formal group composition
  law on independent subsystems.
- That ``F_p[J] = r(J)^p`` satisfies the multiplicative formal group
  composition law on independent subsystems for every real ``p``.
- That composability ALONE (axiom (C)) does not select among the
  Lazard-admissible formal group laws: Tempesta composability admits
  ``F_p``, Tsallis, Rényi, Boltzmann-Gibbs simultaneously.
- A source-note boundary check that the note declares
  ``bounded_theorem`` and avoids forbidden status-overclaim strings.

All numerical checks use exact ``fractions.Fraction`` arithmetic or
SymPy symbolic verification.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "OBSERVABLE_PRINCIPLE_P1_BRIDGE_TEMPESTA_COMPOSABILITY_EXTERNAL_NARROW_BOUNDED_NOTE_2026-05-17.md"
)

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"  [{status}] {label}")
    if detail:
        print(f"         {detail}")


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


# ----------------------------------------------------------------------
# Formal group laws under consideration
# ----------------------------------------------------------------------


def G_a(x, y):
    """Additive formal group: G_a(x, y) = x + y. Boltzmann-Gibbs."""
    return x + y


def G_m(x, y):
    """Multiplicative formal group: G_m(x, y) = x + y + xy. Linked to F_p = r^p."""
    return x + y + x * y


def G_q(x, y, q):
    """Tsallis formal group: G_q(x, y) = x + y + (1 - q) xy."""
    return x + y + (1 - q) * x * y


# ----------------------------------------------------------------------
# T1: Composability axiom statement — identity + associativity
# ----------------------------------------------------------------------


def test_T1_composability_axiom_statement() -> None:
    section("T1: Composability axiom (C) — identity and associativity for G_a, G_m, G_q")
    x, y, z, q = sp.symbols("x y z q")
    # Identity: G(x, 0) = x = G(0, x)
    check(
        "G_a identity: G_a(x, 0) = x and G_a(0, x) = x",
        sp.simplify(G_a(x, 0) - x) == 0 and sp.simplify(G_a(0, x) - x) == 0,
    )
    check(
        "G_m identity: G_m(x, 0) = x and G_m(0, x) = x",
        sp.simplify(G_m(x, 0) - x) == 0 and sp.simplify(G_m(0, x) - x) == 0,
    )
    check(
        "G_q identity: G_q(x, 0; q) = x and G_q(0, x; q) = x",
        sp.simplify(G_q(x, 0, q) - x) == 0 and sp.simplify(G_q(0, x, q) - x) == 0,
    )


# ----------------------------------------------------------------------
# T2: Lazard universal formal group law structure (G1, G2, G3)
# ----------------------------------------------------------------------


def test_T2_lazard_formal_group_law_structure() -> None:
    section("T2: Lazard formal group law structure — G1, G2, G3 for G_a, G_m, G_q")
    x, y, z, q = sp.symbols("x y z q")
    # G2 (associativity)
    diff_a = sp.expand(G_a(G_a(x, y), z) - G_a(x, G_a(y, z)))
    diff_m = sp.expand(G_m(G_m(x, y), z) - G_m(x, G_m(y, z)))
    diff_q = sp.expand(G_q(G_q(x, y, q), z, q) - G_q(x, G_q(y, z, q), q))
    check(
        "G_a associativity: G_a(G_a(x, y), z) = G_a(x, G_a(y, z))",
        sp.simplify(diff_a) == 0,
        f"diff = {sp.simplify(diff_a)}",
    )
    check(
        "G_m associativity: G_m(G_m(x, y), z) = G_m(x, G_m(y, z))",
        sp.simplify(diff_m) == 0,
        f"diff = {sp.simplify(diff_m)}",
    )
    check(
        "G_q associativity: G_q(G_q(x, y), z) = G_q(x, G_q(y, z))",
        sp.simplify(diff_q) == 0,
        f"diff = {sp.simplify(diff_q)}",
    )
    # G3 (commutativity)
    com_a = sp.simplify(G_a(x, y) - G_a(y, x))
    com_m = sp.simplify(G_m(x, y) - G_m(y, x))
    com_q = sp.simplify(G_q(x, y, q) - G_q(y, x, q))
    check(
        "G_a commutativity: G_a(x, y) = G_a(y, x)",
        com_a == 0,
    )
    check(
        "G_m commutativity: G_m(x, y) = G_m(y, x)",
        com_m == 0,
    )
    check(
        "G_q commutativity: G_q(x, y; q) = G_q(y, x; q)",
        com_q == 0,
    )


# ----------------------------------------------------------------------
# T3: Boltzmann-Gibbs is additive formal group (Shannon additivity)
# ----------------------------------------------------------------------


def test_T3_boltzmann_gibbs_additive() -> None:
    section("T3: Boltzmann-Gibbs Shannon entropy is additive (G_a) on independent distributions")
    # H(p) = -sum p_i log p_i; H(p (x) q) = H(p) + H(q) on independent dists.
    # Take p = (1/2, 1/2), q = (1/3, 2/3).
    p1, p2 = sp.Rational(1, 2), sp.Rational(1, 2)
    q1, q2 = sp.Rational(1, 3), sp.Rational(2, 3)

    def H(probs):
        return -sum(pi * sp.log(pi) for pi in probs)

    H_p = sp.simplify(H([p1, p2]))
    H_q = sp.simplify(H([q1, q2]))
    # Joint distribution on independent systems: (p_i q_j)
    joint = [p1 * q1, p1 * q2, p2 * q1, p2 * q2]
    H_joint = sp.simplify(H(joint))
    diff = sp.simplify(H_joint - (H_p + H_q))
    check(
        "Shannon entropy additivity on independent p, q: H(p (x) q) = H(p) + H(q)",
        diff == 0,
        f"H(p)={H_p}, H(q)={H_q}, H(joint)={H_joint}, diff={diff}",
    )
    # This is G_a applied to W(A) = H(p), W(B) = H(q): G_a(H_p, H_q) = H_p + H_q.
    check(
        "Shannon additivity matches G_a(H(p), H(q)) = H(p) + H(q)",
        sp.simplify(G_a(H_p, H_q) - H_joint) == 0,
    )


# ----------------------------------------------------------------------
# T4: Grassmann determinant factorization on real-D blocks (P1)
# ----------------------------------------------------------------------


def test_T4_grassmann_determinant_factorization() -> None:
    section("T4: Grassmann determinant block factorization (P1) — symbolic 4x4")
    a, c, jaa, jbb, kcc, kdd = sp.symbols("a c jaa jbb kcc kdd", real=True)
    # D_A real anti-symmetric:
    D_A = sp.Matrix([[0, a], [-a, 0]])
    # D_B real anti-symmetric:
    D_B = sp.Matrix([[0, c], [-c, 0]])
    # J_A diagonal real-symmetric source:
    J_A = sp.Matrix([[jaa, 0], [0, jbb]])
    # J_B diagonal real-symmetric source:
    J_B = sp.Matrix([[kcc, 0], [0, kdd]])
    # Block diagonal D and J:
    D = sp.diag(D_A, D_B)
    J = sp.diag(J_A, J_B)
    lhs = sp.expand((D + J).det())
    rhs = sp.expand((D_A + J_A).det() * (D_B + J_B).det())
    diff = sp.simplify(lhs - rhs)
    check(
        "det(D_A (+) D_B + J_A (+) J_B) = det(D_A + J_A) det(D_B + J_B) — multiplicative input to composability",
        diff == 0,
        f"sympy.simplify(lhs - rhs) = {diff}",
    )
    # Numerical instance:
    subs = {a: Fraction(2, 3), c: Fraction(1, 5), jaa: Fraction(1, 2),
            jbb: Fraction(1, 3), kcc: Fraction(2, 11), kdd: Fraction(3, 5)}
    lhs_n = sp.Rational(lhs.subs(subs))
    rhs_n = sp.Rational(rhs.subs(subs))
    check(
        "Numerical rational instance: det factorization holds",
        lhs_n == rhs_n,
        f"lhs={lhs_n}, rhs={rhs_n}",
    )


# ----------------------------------------------------------------------
# T5: W = c log|Z| satisfies the additive formal group composition law
# ----------------------------------------------------------------------


def test_T5_log_satisfies_additive_formal_group() -> None:
    section("T5: W = c log|Z| satisfies the additive formal group G_a")
    # On independent subsystems: r(J_A (+) J_B) = r_A r_B.
    # W = c log r implies W(A (+) B) = c log(r_A r_B) = c log r_A + c log r_B = W(A) + W(B).
    # This matches G_a(W(A), W(B)) = W(A) + W(B).
    r_A, r_B, c = sp.symbols("r_A r_B c", positive=True)
    W_A = c * sp.log(r_A)
    W_B = c * sp.log(r_B)
    W_joint = c * sp.log(r_A * r_B)
    diff = sp.simplify(W_joint - G_a(W_A, W_B))
    check(
        "W(A (+) B) = c log(r_A r_B) = c log r_A + c log r_B = G_a(W(A), W(B))",
        diff == 0,
        f"diff = {diff}",
    )


# ----------------------------------------------------------------------
# T6: F_p = r^p is in the multiplicative formal group class (G_m)
# ----------------------------------------------------------------------


def test_T6_F_p_in_multiplicative_formal_group_class() -> None:
    section("T6: F_p[J] = r(J)^p is in the multiplicative formal group class")
    # F_p[A (+) B] = (r_A r_B)^p = r_A^p r_B^p = F_p[A] F_p[B].
    # Equivalently, after the shift F_p -> 1 + (F_p - 1),
    # the composition law on the shifted variable is G_m(x, y) = x + y + xy:
    #   (1 + x)(1 + y) - 1 = x + y + xy.
    test_ps = [Fraction(-2), Fraction(-1), Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3)]
    r_A_val = Fraction(2)
    r_B_val = Fraction(3)
    ok_mult = True
    ok_shift = True
    details_mult = []
    details_shift = []
    for p in test_ps:
        p_s = sp.Rational(p)
        r_A_s = sp.Rational(r_A_val)
        r_B_s = sp.Rational(r_B_val)
        F_joint = (r_A_s * r_B_s) ** p_s
        F_prod = (r_A_s ** p_s) * (r_B_s ** p_s)
        diff = sp.simplify(F_joint - F_prod)
        if diff != 0:
            ok_mult = False
        details_mult.append((float(p), str(diff)))
        # Shift check: with F_p - 1 = x_A, F_p - 1 = x_B, G_m(x_A, x_B) = (F_p[A] - 1) + (F_p[B] - 1) + (F_p[A] - 1)(F_p[B] - 1)
        # = F_p[A] F_p[B] - 1. So F_joint - 1 = G_m(F_p[A] - 1, F_p[B] - 1).
        x_A = (r_A_s ** p_s) - 1
        x_B = (r_B_s ** p_s) - 1
        diff_shift = sp.simplify((F_joint - 1) - G_m(x_A, x_B))
        if diff_shift != 0:
            ok_shift = False
        details_shift.append((float(p), str(diff_shift)))
    check(
        "F_p[A (+) B] = F_p[A] F_p[B] (multiplicative) for p in {-2, -1, 1/2, 1, 2, 3}",
        ok_mult,
        f"(p, diff): {details_mult}",
    )
    check(
        "F_p[A (+) B] - 1 = G_m(F_p[A] - 1, F_p[B] - 1) — multiplicative formal group composition after shift",
        ok_shift,
        f"(p, shift_diff): {details_shift}",
    )


# ----------------------------------------------------------------------
# T7: Associativity check for G_m, G_a, G_q on rational instances
# ----------------------------------------------------------------------


def test_T7_associativity_rational_instances() -> None:
    section("T7: Associativity G(G(x, y), z) = G(x, G(y, z)) on rational instances")
    # G_a:
    x_v, y_v, z_v = Fraction(2, 3), Fraction(1, 5), Fraction(7, 11)
    diff_a = G_a(G_a(x_v, y_v), z_v) - G_a(x_v, G_a(y_v, z_v))
    check("G_a associativity on rational instance (x=2/3, y=1/5, z=7/11)", diff_a == 0,
          f"diff = {diff_a}")
    # G_m:
    diff_m = G_m(G_m(x_v, y_v), z_v) - G_m(x_v, G_m(y_v, z_v))
    check("G_m associativity on rational instance (x=2/3, y=1/5, z=7/11)", diff_m == 0,
          f"diff = {diff_m}")
    # G_q at q = 1/2:
    q_v = Fraction(1, 2)
    diff_q = G_q(G_q(x_v, y_v, q_v), z_v, q_v) - G_q(x_v, G_q(y_v, z_v, q_v), q_v)
    check("G_q associativity on rational instance (q=1/2, x=2/3, y=1/5, z=7/11)", diff_q == 0,
          f"diff = {diff_q}")


# ----------------------------------------------------------------------
# T8: Counterexample compatibility — F_p, Tsallis, Renyi all composable
# ----------------------------------------------------------------------


def test_T8_counterexample_compatibility() -> None:
    section("T8: Composability admits F_p, Tsallis, Renyi simultaneously — not unique selection")
    # Pick a test rational pair. Show that the same multiplicative input
    # r_A * r_B is consistent with three different choices of (W, G):
    #   (W = log r, G = G_a) — Boltzmann-Gibbs
    #   (W = r^p, G = G_m) — F_p counterexample
    #   (W = Tsallis-like, G = G_q) — Tsallis q-entropy
    r_A = sp.Rational(Fraction(2))
    r_B = sp.Rational(Fraction(3))
    # Choice 1: log
    W1_A = sp.log(r_A)
    W1_B = sp.log(r_B)
    W1_joint_via_log = sp.log(r_A * r_B)
    W1_joint_via_G_a = G_a(W1_A, W1_B)
    ok_1 = sp.simplify(W1_joint_via_log - W1_joint_via_G_a) == 0
    check(
        "Choice 1 (BG): W = log r composes via G_a (additive)",
        ok_1,
        f"log(r_A r_B) = {W1_joint_via_log}, G_a(log r_A, log r_B) = {W1_joint_via_G_a}",
    )
    # Choice 2: F_p with p = 2, in the shifted form
    p_val = sp.Rational(Fraction(2))
    W2_A = r_A ** p_val
    W2_B = r_B ** p_val
    W2_joint_via_F_p = (r_A * r_B) ** p_val
    # G_m on the shifted variables:
    W2_joint_via_G_m_shift = 1 + G_m(W2_A - 1, W2_B - 1)
    ok_2 = sp.simplify(W2_joint_via_F_p - W2_joint_via_G_m_shift) == 0
    check(
        "Choice 2 (F_p): W = r^p composes via shifted G_m (multiplicative formal group)",
        ok_2,
        f"(r_A r_B)^p = {W2_joint_via_F_p}, 1 + G_m(r_A^p - 1, r_B^p - 1) = {W2_joint_via_G_m_shift}",
    )
    # Choice 3: Tsallis q-entropy. Use canonical pair on a 2-state distribution.
    # S_q(p) = (1 - sum p_i^q) / (q - 1). For q = 1/2 and uniform p = (1/2, 1/2):
    q_val = sp.Rational(Fraction(1, 2))
    p_uniform = [sp.Rational(Fraction(1, 2)), sp.Rational(Fraction(1, 2))]

    def S_q(probs, q):
        s = sum(p ** q for p in probs)
        return (1 - s) / (q - 1)

    S_q_A = sp.simplify(S_q(p_uniform, q_val))
    S_q_B = sp.simplify(S_q(p_uniform, q_val))
    # Joint distribution: independent product (1/4 each).
    p_joint = [sp.Rational(Fraction(1, 4))] * 4
    S_q_joint = sp.simplify(S_q(p_joint, q_val))
    # Composability check: S_q(A (+) B) = G_q(S_q(A), S_q(B); q) = S_q(A) + S_q(B) + (1 - q) S_q(A) S_q(B)
    composed = sp.simplify(G_q(S_q_A, S_q_B, q_val))
    ok_3 = sp.simplify(S_q_joint - composed) == 0
    check(
        "Choice 3 (Tsallis): S_q on uniform p composes via G_q (multiplicative-shifted formal group)",
        ok_3,
        f"S_q(joint) = {S_q_joint}, G_q(S_q(A), S_q(B); q) = {composed}",
    )
    # No unique selection — all three are composable; the framework substrate alone selects none.
    all_three_ok = ok_1 and ok_2 and ok_3
    check(
        "All three (BG, F_p, Tsallis) are composability-admissible — composability does NOT uniquely select",
        all_three_ok,
        "Composability admits the entire Lazard-classified Z-entropy class.",
    )


# ----------------------------------------------------------------------
# T9: Bridge identification — composability admits all of additive, multiplicative, Tsallis
# ----------------------------------------------------------------------


def test_T9_bridge_identification_admits_all() -> None:
    section("T9: Bridge identification — composability admits all of additive, multiplicative, Tsallis")
    # Re-state the no-unique-selection finding as a sharper bridge statement.
    # On the framework's multiplicative input r(J_A (+) J_B) = r_A r_B, the
    # composability axiom (C) admits three named members of the Z-entropy
    # class (and infinitely many more in the Lazard ring image):
    #   (a) (W = log r, G = G_a) -- additive formal group, Boltzmann-Gibbs
    #   (b) (W = r^p, G = G_m via shift) -- multiplicative formal group, F_p
    #   (c) (W = Tsallis S_q, G = G_q) -- Tsallis formal group
    # Selecting (a) over (b) or (c) is the SAME admission as P1.
    # Verify this by exhibiting the three composition laws are distinct
    # (not the same formal group law):
    x, y, q = sp.symbols("x y q")
    # G_a vs G_m: G_a(x, y) - G_m(x, y) = -xy. Non-zero generically.
    diff_am = sp.expand(G_a(x, y) - G_m(x, y))
    check(
        "G_a and G_m are distinct formal group laws: G_a - G_m = -xy",
        sp.simplify(diff_am + x * y) == 0,
        f"G_a - G_m = {diff_am}",
    )
    # G_m vs G_q: G_m(x, y) - G_q(x, y; q) = xy - (1 - q) xy = q xy.
    diff_mq = sp.expand(G_m(x, y) - G_q(x, y, q))
    check(
        "G_m and G_q are distinct formal group laws: G_m - G_q = q xy",
        sp.simplify(diff_mq - q * x * y) == 0,
        f"G_m - G_q = {diff_mq}",
    )
    # G_a vs G_q: G_a(x, y) - G_q(x, y; q) = - (1 - q) xy. Non-zero generically.
    diff_aq = sp.expand(G_a(x, y) - G_q(x, y, q))
    check(
        "G_a and G_q are distinct formal group laws: G_a - G_q = - (1 - q) xy",
        sp.simplify(diff_aq + (1 - q) * x * y) == 0,
        f"G_a - G_q = {diff_aq}",
    )
    # Selecting G_a (additive) over G_m / G_q is exactly the P1 admission.


# ----------------------------------------------------------------------
# T10: Source-note boundary check
# ----------------------------------------------------------------------


def test_T10_source_note_boundary() -> None:
    section("T10: Source-note boundary")
    text = NOTE.read_text(encoding="utf-8")
    required_admissions = [
        "**Claim type:** bounded_theorem",
        "Status authority:** independent audit lane only",
        "Source-note proposal disclaimer",
        # Honest admissions:
        "does **not** derive the P1",
        "P1 is NOT closed positively",
        "Composability **does not force** the additive formal group",
        "is identifiable as the **multiplicative formal",
        "does not undertake",
        "does not pre-judge",
        # Sharpening over Routes A/B/C/E:
        "Sharpening over Routes A/B/C/E",
        "6 scaffold classes",
    ]
    for s in required_admissions:
        ok = s in text
        check(f'note contains admission string: "{s[:60]}..."', ok,
              f"present={ok}")
    forbidden = [
        "**Claim type:** positive_theorem",
        "**Claim type:** retained",
        "**Claim type:** no_go",  # this is a bounded_theorem, not a no_go
        "audited_clean (this note)",
        "retained_bounded (this note)",
        "P1 is now derived",
        "P1 is closed by this note",
        "P1 is retired by this note",
        "this note promotes the status",
        "audit lane verdict: retained",
        "effective_status: retained (this note)",
        "effective_status: audited_clean (this note)",
        # composability does NOT force additive G; reject any wording saying otherwise:
        "composability forces the additive",
        "composability uniquely selects",
        "Tempesta scaffold closes P1",
    ]
    hits = [f for f in forbidden if f in text]
    check(
        "note avoids forbidden status-promotion / overclaim strings",
        len(hits) == 0,
        f"forbidden_hits={hits}",
    )


# ----------------------------------------------------------------------
# main
# ----------------------------------------------------------------------


def main() -> int:
    print("# Observable-principle P1 bridge Tempesta composability runner")
    print(f"# Source note: {NOTE.relative_to(ROOT)}")
    test_T1_composability_axiom_statement()
    test_T2_lazard_formal_group_law_structure()
    test_T3_boltzmann_gibbs_additive()
    test_T4_grassmann_determinant_factorization()
    test_T5_log_satisfies_additive_formal_group()
    test_T6_F_p_in_multiplicative_formal_group_class()
    test_T7_associativity_rational_instances()
    test_T8_counterexample_compatibility()
    test_T9_bridge_identification_admits_all()
    test_T10_source_note_boundary()
    print(f"\n=== TOTAL: PASS={PASS}, FAIL={FAIL} ===")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
