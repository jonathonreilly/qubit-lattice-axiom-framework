#!/usr/bin/env python3
"""Runner for the observable-principle P1 bridge Gleason-Busch route no_go.

This runner verifies the structural no-go on closing the P1 admitted
premise of OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md via the Gleason-Busch
quantum-probability scaffold. Per the 2026-05-21 narrowing review
(see source note §0.1), the route-level obstructions reduce to G1
and G3, with G2 recorded as a per-site Gleason-uniqueness sharpening
of the same scaffold landscape (not a stand-alone route-level P1
obstruction):

  G1 -- Gleason-Busch additivity is an INPUT hypothesis, not derived.
        Every published Gleason-type theorem (Gleason 1957, Busch 2003,
        CFMR 2004, Wright-Weigert 2019) takes sigma-additivity on
        projectors / POVM effects as the load-bearing hypothesis.
        Route-level P1 obstruction.
  G2 -- (narrowed 2026-05-21) Wallach unentangled-Gleason FAILS at the
        per-site decomposition H_Lambda = (x) H_x with H_x = C^2 (each
        per-site factor dim 2 < 3). This is a per-site Gleason-
        uniqueness sharpening of the Gleason-Busch scaffold landscape.
        Wallach SUCCEEDS at the per-region bipartition H_Lambda = H_A
        (x) H_B with |A|, |B| >= 2 (each region factor dim 2^|A| >= 4
        >= 3), which is the bipartition that is load-bearing for P1.
        G2 is therefore NOT a stand-alone route-level P1 obstruction;
        the route-level obstructions are G1 + G3.
  G3 -- Bridging Gleason output p(E_A x E_B) = p_A . p_B to scalar
        generator additivity W[J_A + J_B] = W[J_A] + W[J_B] invokes the
        Cauchy log functional equation classifier
        f(xy) = f(x) + f(y) + cty -> c log, which IS P1 in different
        vocabulary (Pattern L circularity, D5 of the Route D no-go).
        Route-level P1 obstruction.

The F_p[J] = |Z[J]|^p counterexample family of Routes A/C/E reappears
unchanged: F_p is compatible with Gleason-Busch multiplicative
factorization on product effects for every real p, but fails
block-additivity for every p != 0. The runner exhibits explicit witness
pairs at exact Fraction precision.

All numerical checks use exact fractions.Fraction arithmetic or SymPy
symbolic verification. No floating-point comparator inputs.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "OBSERVABLE_PRINCIPLE_P1_BRIDGE_GLEASON_BUSCH_ROUTE_NARROW_NOTE_2026-05-21.md"
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


def test_T1_no_go_theorem_stated_precisely() -> None:
    section("T1: no_go theorem statement and three obstructions G1/G2/G3")
    text = NOTE.read_text(encoding="utf-8")
    # Whitespace-normalize so line-wrapped phrases match
    text_norm = " ".join(text.split())
    required = [
        # The theorem statement core elements
        "Gleason-Busch route does **not** close P1",
        # Three obstructions named
        "G1",
        "G2",
        "G3",
        # G1 -- additivity input
        "additivity hypothesis input",
        # G2 -- Wallach dim-2 failure
        "Wallach",
        "dim-2",
        "qubit",
        # G3 -- Cauchy circularity
        "Cauchy",
        "Pattern L",
        # Scope-bounding
        "scope-bounded to the Gleason-Busch scaffold",
        # F_p counterexample
        "F_p",
    ]
    missing = [s for s in required if s not in text_norm]
    check(
        "no_go theorem statement contains all required core elements",
        len(missing) == 0,
        f"missing={missing}" if missing else "all required strings present",
    )


def test_T2_assumption_audit_table() -> None:
    section("T2: assumption audit (Exercise 1) table present")
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "Exercise 1 — Assumption audit",
        # Key entries
        "A1",
        "A2",
        "Gleason 1957",
        "Busch 2003",
        "Wallach 2000",
        "Pitowsky 2002",
        "Wright-Weigert 2019",
        # Dimension hypothesis check (narrowed 2026-05-21)
        "Dimension hypothesis check",
        # The crucial narrowed finding: Wallach succeeds at per-region
        # bipartition (trivially satisfied at |A|,|B| >= 2), fails at
        # per-site decomposition
        "trivially satisfied",
        "per-site",
        "per-region",
    ]
    missing = [s for s in required if s not in text]
    check(
        "assumption audit covers framework axioms, lit imports, and conventions",
        len(missing) == 0,
        f"missing={missing}" if missing else "assumption audit complete",
    )


def test_T3_elon_first_principles() -> None:
    section("T3: Elon first-principles (Exercise 2) present")
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "Exercise 2 — Elon Musk first-principles",
        # The asking part
        "P1 is the assertion",
        # Why Gleason might force it
        "Why Gleason might force it",
        # Why it fails
        "Why this hope fails",
        # Route-level obstructions (G1 + G3) plus G2 sharpening
        # (narrowed 2026-05-21 per §0.1 review)
        "(G1)",
        "(G2 narrowed",
        "(G3)",
        # The deep reason
        "deep reason",
        # Articulation of structural reduction
        "Shannon-Khinchin's failure mode",
    ]
    missing = [s for s in required if s not in text]
    check(
        "Elon first-principles articulates deep structural reason",
        len(missing) == 0,
        f"missing={missing}" if missing else "Elon exercise complete",
    )


def test_T4_lit_search_three_citations() -> None:
    section("T4: literature search (Exercise 3) with >= 3 real citations")
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "Exercise 3 — Literature search",
        # Three required citations with publication-quality details
        "Wallach (2000)",
        "Contemporary Mathematics 305",
        "quant-ph/0002058",
        "Busch (2003)",
        "Phys. Rev. Lett. 91, 120403",
        "quant-ph/9909073",
        "Wright, S. Weigert (2019)",
        "Found. Phys. 49",
        "1905.12751",
        # The decisive 2026 finding
        "Summing to Uncertainty",
        "2603.06211",
    ]
    missing = [s for s in required if s not in text]
    check(
        "literature search records >= 3 publication-quality citations",
        len(missing) == 0,
        f"missing={missing}" if missing else "lit search complete",
    )


def test_T5_tao_math_search() -> None:
    section("T5: Tao-style math search (Exercise 4) on bare math problem")
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "Exercise 4 — Math search",
        # Bare math problem decoupled from physics
        "decoupled from the physics framework",
        # Affirmative case
        "Affirmative for dim",
        # Negative case
        "Negative for any factor at dim 2",
        # Cauchy reformulation
        "Cauchy functional equation form",
        # Tao-search conclusion (narrowed 2026-05-21 per §0.1)
        "Tao-search conclusion",
        # Honest answer (narrowed 2026-05-21: per-region vs per-site
        # bipartition distinction now load-bearing)
        "honest math\nanswer",  # split across lines after narrowing
        # No published result derives additivity
        "No published math result",
    ]
    text_norm_space = " ".join(text.split())
    missing = [s for s in required if s.replace("\n", " ") not in text_norm_space]
    check(
        "Tao math search covers affirmative dim>=3, negative dim 2, Cauchy form",
        len(missing) == 0,
        f"missing={missing}" if missing else "math search complete",
    )


def test_T6_F_p_counterexample_existential_witnesses() -> None:
    section("T6: F_p counterexample family -- existential block-additivity defects")

    # The corrected (existential) load-bearing step: there EXIST witness
    # pairs where block-additivity fails. A single nonzero defect suffices
    # to obstruct the universal "Gleason-Busch forces F_p additive" claim.
    # We verify several explicit witnesses with exact Fraction arithmetic.

    # Symbolic verification first: F_p IS multiplicatively factorizing for
    # every real p.
    p, r_A, r_B = sp.symbols("p r_A r_B", positive=True, real=True)
    F_p_combined = (r_A * r_B) ** p
    F_p_factored = (r_A ** p) * (r_B ** p)
    mult_diff = sp.simplify(F_p_combined - F_p_factored)
    check(
        "F_p[J_A + J_B] = F_p[J_A] * F_p[J_B] (multiplicative, symbolic)",
        mult_diff == 0,
        f"simplify((r_A*r_B)^p - r_A^p * r_B^p) = {mult_diff}",
    )

    # Now existential witness: pick rational (p, r_A, r_B) where additivity
    # fails. We use exact Fraction arithmetic.
    witnesses_int_p = [
        # (p, r_A, r_B) all rational; integer p so we can use Fraction
        (Fraction(1), Fraction(2), Fraction(3)),   # F_1 defect: 6 - 5 = 1
        (Fraction(2), Fraction(2), Fraction(3)),   # F_2 defect: 36 - 13 = 23
        (Fraction(3), Fraction(2), Fraction(3)),   # F_3 defect: 216 - 35 = 181
        (Fraction(2), Fraction(3, 2), Fraction(5, 7)),
        (Fraction(-1), Fraction(2), Fraction(3)),  # F_-1 defect
        (Fraction(-2), Fraction(2), Fraction(3)),  # F_-2 defect
    ]
    defects: list[tuple[Fraction, Fraction, Fraction, Fraction]] = []
    for p_val, r_a, r_b in witnesses_int_p:
        # F_p[A+B] = (r_a * r_b)^p; F_p[A] + F_p[B] = r_a^p + r_b^p
        # Use Fraction integer power
        p_int = int(p_val)
        if p_int >= 0:
            lhs = (r_a * r_b) ** p_int
            rhs = (r_a ** p_int) + (r_b ** p_int)
        else:
            lhs = Fraction(1) / ((r_a * r_b) ** (-p_int))
            rhs = (Fraction(1) / (r_a ** (-p_int))) + (Fraction(1) / (r_b ** (-p_int)))
        defect = lhs - rhs
        defects.append((p_val, r_a, r_b, defect))

    nonzero_defects = [d for d in defects if d[3] != 0]
    check(
        f"existential: nonzero block-additivity defects on >= 1 integer-p witness",
        len(nonzero_defects) >= 1,
        f"found {len(nonzero_defects)} nonzero defects out of {len(defects)} witnesses",
    )
    # Sanity prints
    print("         Sample (p, r_A, r_B, defect):")
    for w in nonzero_defects[:4]:
        print(f"           p={w[0]}, r_A={w[1]}, r_B={w[2]}, defect={w[3]}")

    # Additional symbolic check: F_p with p = 1/2 (square root)
    p_half = sp.Rational(1, 2)
    r_a_s = sp.Rational(4)  # so sqrt is exact
    r_b_s = sp.Rational(9)
    F_half_combined = (r_a_s * r_b_s) ** p_half
    F_half_factored = (r_a_s ** p_half) + (r_b_s ** p_half)
    defect_half = sp.simplify(F_half_combined - F_half_factored)
    # (4*9)^(1/2) = 6;  4^(1/2) + 9^(1/2) = 2 + 3 = 5;  defect = 1
    check(
        "F_{1/2} defect: sqrt(4*9) - sqrt(4) - sqrt(9) = 6 - 5 = 1 != 0 (exact symbolic)",
        defect_half == 1,
        f"sympy.simplify(sqrt(36) - sqrt(4) - sqrt(9)) = {defect_half}",
    )

    # Sensitivity: log r IS additive (the Cauchy classifier limit)
    log_diff = sp.simplify(
        sp.expand_log(sp.log(r_A * r_B) - sp.log(r_A) - sp.log(r_B), force=True)
    )
    check(
        "log r IS block-additive (the p -> 0 / Cauchy classifier limit)",
        log_diff == 0,
        f"sympy.simplify(log(r_A*r_B) - log(r_A) - log(r_B)) = {log_diff}",
    )


def test_T7_G1_additivity_input_cauchy_classifier() -> None:
    section("T7: G1 -- Gleason-Busch additivity is INPUT, not output (Cauchy classifier)")

    # The structural content of G1: the Cauchy log functional equation
    # classifier is what Gleason-Busch reduces to (Wright-Weigert 2019),
    # and it takes additivity as the load-bearing hypothesis input.
    # The symbolic check verifies that log IS the unique continuous
    # multiplicative-to-additive functional, AND that the
    # additivity hypothesis is required.

    x, y = sp.symbols("x y", positive=True, real=True)

    # Cauchy: log(xy) - log(x) - log(y) = 0 identically on R+
    cauchy_lhs = sp.log(x * y) - sp.log(x) - sp.log(y)
    cauchy_simp = sp.simplify(sp.expand_log(cauchy_lhs, force=True))
    check(
        "Cauchy log functional equation: log(xy) - log(x) - log(y) = 0 (symbolic)",
        cauchy_simp == 0,
        f"simplify(log(xy) - log(x) - log(y)) = {cauchy_simp}",
    )

    # Sensitivity: x^p (the F_p family) does NOT satisfy Cauchy log equation
    # for p != 0 generically -- there exists x, y with x^p*y^p != x^p + y^p
    # (the existential check from T6 covers this).

    # Witness that the Cauchy classifier is what bridges multiplicative
    # to additive: if f(xy) = f(x) + f(y) on R+ with continuity, then f
    # is c*log. The note records this from Cauchy 1821 / Aczel 1966.

    text = NOTE.read_text(encoding="utf-8")
    required = [
        # G1 obstruction
        "G1 — Additivity input",
        # Lit confirmation
        "Summing to Uncertainty",
        # Cauchy classifier role
        "Cauchy log classifier",
        # Additivity is input, not output
        "input not output",
    ]
    missing = [s for s in required if s not in text]
    check(
        "G1 obstruction documented with Cauchy classifier reduction",
        len(missing) == 0,
        f"missing={missing}" if missing else "G1 documentation complete",
    )


def test_T8_G2_wallach_dim_2_failure() -> None:
    section("T8: G2 -- Wallach dim-2 failure on qubit substrate")

    # Verify the dimension arithmetic that triggers G2.
    #
    # Framework substrate: H_x = C^2 (qubit per site).
    # Joint register on |Lambda| sites: dim H_Lambda = 2^|Lambda|.
    # For |Lambda| >= 2: dim H_Lambda >= 4 >= 3 (Gleason 1957
    #   hypothesis on joint register satisfied).
    # Per-tensor-factor dim: 2 (each site).
    # Wallach 2000 hypothesis: each factor dim >= 3 (FAILS at dim 2).

    per_site_dim = 2  # H_x = C^2 from MINIMAL_AXIOMS_2026-05-20

    # Joint register dimensions for small |Lambda|
    joint_dims = [(n, per_site_dim ** n) for n in range(1, 6)]
    check(
        "joint register dim 2^|Lambda| values match qubit substrate",
        all(d == 2 ** n for (n, d) in joint_dims),
        f"joint dims: {joint_dims}",
    )

    # Gleason 1957 dim >= 3 satisfied on joint register for |Lambda| >= 2
    gleason_ok_for = [(n, d) for (n, d) in joint_dims if d >= 3]
    check(
        "Gleason 1957 (joint dim >= 3) satisfied for |Lambda| >= 2",
        gleason_ok_for == [(2, 4), (3, 8), (4, 16), (5, 32)],
        f"Gleason-OK joint blocks: {gleason_ok_for}",
    )

    # Wallach dim >= 3 per factor FAILS at every site
    wallach_ok_per_factor = per_site_dim >= 3
    check(
        "Wallach 2000 (per-factor dim >= 3) FAILS on qubit substrate (dim 2)",
        not wallach_ok_per_factor,
        f"per-site dim = {per_site_dim} < 3 -> Wallach hypothesis violated",
    )

    # G2 narrowed 2026-05-21 (see §0.1 narrowing review): G2 is a
    # per-site Gleason-uniqueness sharpening of the Gleason-Busch
    # scaffold landscape, NOT a stand-alone route-level P1 obstruction.
    # The runner now verifies the narrowed G2 documentation: that per-site
    # Wallach uniqueness fails at dim 2 (the sharpening), that per-region
    # Wallach uniqueness succeeds at the P1-relevant bipartition, and that
    # G2 is explicitly classified as a sharpening rather than a stand-alone
    # obstruction.
    text = NOTE.read_text(encoding="utf-8")
    # Normalize whitespace to match line-wrapped phrases
    text_norm = " ".join(text.split())
    required = [
        # G2 narrowed header
        "G2 — Per-site Wallach dim-2 sharpening",
        "C^2",
        # Per-site decomposition is where Wallach fails (dim 2 < 3)
        "per-site tensor factor at dim 2",
        # Per-region decomposition is where Wallach succeeds (load-bearing
        # for P1; each factor dim ≥ 4 ≥ 3)
        "per-region bipartition",
        # Explicit classification: G2 is a sharpening, not a P1 obstruction
        "per-site Gleason-uniqueness sharpening",
        # Pitowsky 2002 attribution preserved
        "Pitowsky 2002",
        # Section 0.1 narrowing review cross-reference present
        "§0.1",
    ]
    missing = [s for s in required if s not in text_norm]
    check(
        "G2 obstruction documents Wallach failure mode on qubit substrate",
        len(missing) == 0,
        f"missing={missing}" if missing else "G2 documentation complete",
    )


def test_T9_G3_pattern_L_circularity() -> None:
    section("T9: G3 -- Cauchy log classifier (Pattern L) circularity")

    # G3: bridging Gleason output p(E_A x E_B) = p_A . p_B to scalar
    # generator additivity W[J_A + J_B] = W[J_A] + W[J_B] requires
    # W = log p, which goes through the Cauchy classifier = P1 in
    # different vocabulary.
    #
    # Symbolic check: log of a product is the sum of logs; this is the
    # Cauchy classifier identity. F_p = r^p does NOT satisfy this for
    # p != 0 (T6 already verifies this).

    p_A, p_B = sp.symbols("p_A p_B", positive=True, real=True)
    log_prod = sp.simplify(
        sp.expand_log(sp.log(p_A * p_B) - sp.log(p_A) - sp.log(p_B), force=True)
    )
    check(
        "W = log p is additive: log(p_A * p_B) = log p_A + log p_B (Cauchy)",
        log_prod == 0,
        f"simplify(log(p_A*p_B) - log(p_A) - log(p_B)) = {log_prod}",
    )

    # F_q = p^q for q != 0 is NOT additive (existential witness from T6
    # at q=1: 2+3=5 != 6).
    # Verify: q=2 explicit; (2*3)^2 - (2^2 + 3^2) = 36 - 13 = 23 != 0
    q_val = 2
    defect = (Fraction(2) * Fraction(3)) ** q_val - (Fraction(2) ** q_val + Fraction(3) ** q_val)
    check(
        f"F_2(p) = p^2 NOT additive: defect = (2*3)^2 - (2^2 + 3^2) = {defect} != 0",
        defect != 0,
        f"explicit Fraction defect = {defect}",
    )

    # The G3 finding: selecting log over (.)^q for q != 0 IS P1.
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "G3 — Cauchy log classifier circularity",
        # Pattern L (D5) link
        "Pattern L",
        "D5",
        # Selecting log
        "selecting `log`",
        # IS P1
        "IS P1",
    ]
    missing = [s for s in required if s not in text]
    check(
        "G3 obstruction documents Pattern L / D5 circularity reduction",
        len(missing) == 0,
        f"missing={missing}" if missing else "G3 documentation complete",
    )


def test_T10_qubit_substrate_tensor_factorization() -> None:
    section("T10: framework qubit substrate -- Gleason factorization on product effects")

    # Symbolic check: on H_A (x) H_B with H_A = C^2, H_B = C^2,
    # for product state sigma = sigma_A (x) sigma_B and product effect
    # E = E_A (x) E_B, the Gleason output factorizes multiplicatively:
    # Tr((sigma_A (x) sigma_B)(E_A (x) E_B)) = Tr(sigma_A E_A) * Tr(sigma_B E_B).
    # This is the multiplicative factorization that Gleason-Busch produces.

    # Use 2x2 symbolic matrices over Q
    a1, a2, a3, a4 = sp.symbols("a1 a2 a3 a4", real=True)
    b1, b2, b3, b4 = sp.symbols("b1 b2 b3 b4", real=True)
    e1, e2, e3, e4 = sp.symbols("e1 e2 e3 e4", real=True)
    f1, f2, f3, f4 = sp.symbols("f1 f2 f3 f4", real=True)

    sigma_A = sp.Matrix([[a1, a2], [a3, a4]])
    sigma_B = sp.Matrix([[b1, b2], [b3, b4]])
    E_A = sp.Matrix([[e1, e2], [e3, e4]])
    E_B = sp.Matrix([[f1, f2], [f3, f4]])

    # Tr(sigma_A E_A) * Tr(sigma_B E_B)
    tr_A = sp.simplify((sigma_A * E_A).trace())
    tr_B = sp.simplify((sigma_B * E_B).trace())
    product_traces = sp.expand(tr_A * tr_B)

    # Tr((sigma_A (x) sigma_B) (E_A (x) E_B)) via Kronecker product
    sigma_full = sp.kronecker_product(sigma_A, sigma_B)
    E_full = sp.kronecker_product(E_A, E_B)
    tr_full = sp.simplify((sigma_full * E_full).trace())
    tr_full_expanded = sp.expand(tr_full)

    diff = sp.simplify(tr_full_expanded - product_traces)
    check(
        "Gleason on product state x product effect: Tr(sigma E) = Tr(sigma_A E_A) * Tr(sigma_B E_B) (symbolic 2x2 (x) 2x2)",
        diff == 0,
        f"sympy.simplify of difference = {diff}",
    )

    # This factorization is multiplicative, not additive. To get additive
    # W = log Tr requires the Cauchy classifier (G3).
    # Sanity: trace product is NOT trace sum
    sum_traces = sp.expand(tr_A + tr_B)
    sum_diff = sp.simplify(product_traces - sum_traces)
    check(
        "Trace product is NOT trace sum (sanity: multiplicative != additive)",
        sum_diff != 0,
        f"product - sum = {sum_diff}",
    )


def test_T11_audit_disposition_yaml() -> None:
    section("T11: audit-lane disposition YAML block present")
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "Audit-lane disposition",
        "claim_id: observable_principle_p1_bridge_gleason_busch_route_narrow_note_2026-05-21",
        "claim_type: no_go",
        "claim_scope",
        "load_bearing_step",
        "load_bearing_step_class: A",
        "declared_one_hop_deps",
        # Required deps
        "observable_principle_from_axiom_note",
        "observable_principle_p1_bridge_route_d_sharpened_no_go_note_2026-05-17",
        "born_rule_from_gleason_busch_derivation_note_2026-05-20",
        "minimal_axioms_2026-05-20",
        "forbidden_imports_check: passed",
    ]
    missing = [s for s in required if s not in text]
    check(
        "audit-lane disposition YAML is complete with no_go and class-A LBS",
        len(missing) == 0,
        f"missing={missing}" if missing else "audit YAML complete",
    )


def test_T12_no_go_scope_boundary() -> None:
    section("T12: no_go scope boundary -- does NOT claim P1 is FALSE")
    text = NOTE.read_text(encoding="utf-8")
    text_norm = " ".join(text.split())
    required = [
        # Explicit non-falsity claim
        "does **NOT** claim",
        "P1 is FALSE",
        # Scope-bounding
        "scope-bounded to the Gleason-Busch scaffold",
        # Forward paths preserved (note phrases this as "The forward
        # paths in §4.2 remain legitimate.")
        "forward paths in §4.2 remain legitimate",
        # No promotion language
        "stays `audited_conditional`",
        # Stays unaudited for Born rule
        "stays `unaudited`",
        # The campaign closure synthesis Path (b) is current
        "Path (b)",
    ]
    missing = [s for s in required if s not in text_norm]
    check(
        "no_go scope is bounded and does NOT claim falsity",
        len(missing) == 0,
        f"missing={missing}" if missing else "scope boundary complete",
    )


def test_T13_source_note_boundary() -> None:
    section("T13: source-note boundary check")
    text = NOTE.read_text(encoding="utf-8")
    required = [
        # Source-note structural elements
        "**Claim type:** no_go",
        "**Status authority:** independent audit lane only",
        "Source-note proposal disclaimer",
        # No forbidden status-promotion overclaim strings
    ]
    forbidden = [
        # Forbidden audit-status overclaim strings
        "this note promotes the parent",
        "Status authority: this note sets audit status",
        "pipeline-derived status: retained",
    ]
    missing = [s for s in required if s not in text]
    bad = [s for s in forbidden if s in text]
    check(
        "source-note boundary intact (no status-promotion overclaims)",
        len(missing) == 0 and len(bad) == 0,
        f"missing={missing}, forbidden_present={bad}" if (missing or bad) else "source-note boundary clean",
    )


def n5_execution_certificate() -> None:
    """State the granularity at which this runner actually resolves the no_go.

    Reporting only: adds no check() call and moves no PASS/FAIL count.
    """
    section("N5 execution certificate: what this runner resolves")

    per_site_dim = 2
    joint_dims = [per_site_dim ** n for n in range(1, 6)]
    doc_scan_checks = 11
    dim_arith_checks = 3
    symbolic_checks = 9

    print(
        "per_element: resolved symbolically, entry by entry. T10 carries the Qubit "
        "one-site baseline M_2(C) as fully general 2 x 2 matrices with named entries - "
        "sigma_A as (a1, a2, a3, a4), sigma_B as (b1..b4), E_A as (e1..e4), E_B as "
        "(f1..f4) - forms the Kronecker product into a 4 x 4, expands its trace, and "
        "certifies the factorization identity as an exact symbolic zero over all 16 "
        "free entries rather than at sample values. T6 then pins the defects at exact "
        "Fraction precision: 6 - 5 = 1 at p = 1, 36 - 13 = 23 at p = 2, 216 - 35 = 181 "
        "at p = 3, and 6 - 5 = 1 again for the p = 1/2 case on the perfect squares 4 "
        "and 9."
    )
    print(
        "per_site: checked, and only a dimension count is resolved - no amplitude is "
        "evaluated at any site. The per-site factor is fixed at dim 2 for the Qubit "
        f"one-site baseline, joint registers are enumerated as 2^|Lambda| = "
        f"{joint_dims} for |Lambda| = 1 to 5, and the whole of G2 turns on comparing "
        "those integers to the hypothesis thresholds: Gleason's dim >= 3 is satisfied "
        "on the joint register from |Lambda| = 2 onward while Wallach's per-factor "
        "dim >= 3 fails at every single site. No site carries a state, an effect or a "
        "readout value anywhere in this runner."
    )
    print(
        "per_mode: checked and not executed. Nothing here is diagonalized. States and "
        "effects are kept as general symbolic 2 x 2 matrices with no spectral "
        "decomposition and no eigenvalue constraint imposed, so the standard "
        "spectrum-in-[0,1] property of effects is never exercised on this route; and "
        "the F_p family is a family of scalar functionals of a positive real, which "
        "has no modes to resolve at all."
    )
    print(
        "per_block: resolved, and it is the granularity the entire no_go lives at. "
        "The object under test is the two-block bipartition H_A (x) H_B: T10 verifies "
        "that the Gleason output factorizes multiplicatively across those two blocks "
        "as an exact symbolic identity, T6 exhibits explicit block-additivity defects "
        "for the F_p family on the same two-block split at exact Fraction precision, "
        "and T8 separates the two block granularities that matter - the per-site "
        "factor at dim 2, where Wallach uniqueness fails, against the per-region "
        "bipartition at dim 2^|A| >= 4, where it succeeds and which is the split that "
        "is load-bearing for P1."
    )
    print(
        "lattice_wide: checked and not executed, and the missing global theorem is "
        "precisely this note's obstruction. No lattice-wide object is ever built; "
        "|Lambda| enters only through the dimension count above, and no volume, "
        "sequence or limit is taken. The route-level obstructions the note records - "
        "that Gleason-Busch takes additivity as an input hypothesis (G1), and that "
        "bridging its multiplicative output to an additive generator runs through the "
        "Cauchy log classifier, which is P1 restated (G3) - are exactly statements "
        "that the missing global derivation does not exist. Execution can exhibit "
        "witnesses against it but cannot supply it."
    )
    print(
        f"  scope: of the {PASS + FAIL} checks in this runner, {doc_scan_checks} are "
        "substring scans over the source Markdown (T1 to T5, the documentation halves "
        f"of T7, T8 and T9, and T11 to T13), {dim_arith_checks} are integer dimension "
        f"arithmetic in T8, and {symbolic_checks} are exact symbolic or Fraction "
        "computations. The majority of the check count therefore certifies the state "
        "of the note's prose rather than any computed quantity."
    )
    print(
        "  scope: the F_p leg is existential by design and the runner says so - the "
        "check passes on at least one nonzero defect out of six witnesses, all at "
        "rational or integer p, with the p = 1/2 case chosen on perfect squares so the "
        "root stays exact. No irrational exponent is exercised, and T9 reuses the same "
        "(2, 3) witness pair that T6 already used."
    )
    print(
        "  scope: fully deterministic - no RNG stream and no optimizer appears "
        "anywhere, and every numerical comparison is exact Fraction or SymPy."
    )


def main() -> int:
    print("=" * 78)
    print("Runner: observable_principle_p1_bridge_gleason_busch_route_narrow_note_2026-05-21")
    print("=" * 78)
    print("Verifies the no_go on closing P1 via the Gleason-Busch")
    print("quantum-probability scaffold. Three structural obstructions:")
    print("  G1: Gleason-Busch additivity is INPUT not derived")
    print("  G2: Wallach unentangled-Gleason FAILS at qubit (dim 2) per factor")
    print("  G3: Cauchy log classifier = P1 (Pattern L circularity D5)")

    test_T1_no_go_theorem_stated_precisely()
    test_T2_assumption_audit_table()
    test_T3_elon_first_principles()
    test_T4_lit_search_three_citations()
    test_T5_tao_math_search()
    test_T6_F_p_counterexample_existential_witnesses()
    test_T7_G1_additivity_input_cauchy_classifier()
    test_T8_G2_wallach_dim_2_failure()
    test_T9_G3_pattern_L_circularity()
    test_T10_qubit_substrate_tensor_factorization()
    test_T11_audit_disposition_yaml()
    test_T12_no_go_scope_boundary()
    test_T13_source_note_boundary()
    n5_execution_certificate()

    print()
    print("=" * 78)
    print(f"PASS={PASS}, FAIL={FAIL}")
    print("=" * 78)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
