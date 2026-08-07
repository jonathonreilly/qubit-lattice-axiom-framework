#!/usr/bin/env python3
"""Source/measure log-selection boundary runner.

This runner tests the missing premise left after the finite sharp-record
record-intervention theorem: can finite record probability calculus alone
select the unit logarithmic source generator?

The result is an exact negative boundary.  Product composition gives the
logarithmic Lie-algebra coordinate only up to a source scale.  Scaled RN
families remain valid probability interventions and change the Y_T source
coefficient by lambda.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT = ROOT / "outputs" / "source_measure_log_selection_boundary_2026-05-30.json"

NOTE = DOCS / "SOURCE_MEASURE_LOG_SELECTION_BOUNDARY_THEOREM_NOTE_2026-05-30.md"
RECORD = DOCS / "SOURCE_MEASURE_RECORD_INTERVENTION_THEOREM_NOTE_2026-05-30.md"
P1P2 = DOCS / "OBSERVABLE_PRINCIPLE_P1P2_TWO_STAGE_SYNTHESIS_NARROW_THEOREM_NOTE_2026-05-28.md"
YT_PREMISE_HISTORY = DOCS / "YT_TIER_A_SOURCE_ACTION_TOP_PREMISE_CLOSURE_NOTE_2026-05-29.md"
YT_NOGO = DOCS / "YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md"
SCALE_PRIMITIVE = DOCS / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, ok: bool, detail: Any = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail != "" else ""
    print(f"[{tag}] {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def part1_document_boundary() -> dict[str, Any]:
    print("\nPart 1: document boundary")
    for path in (NOTE, RECORD, P1P2, YT_PREMISE_HISTORY, YT_NOGO, SCALE_PRIMITIVE):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for phrase in (
        "Theorem",
        "Relation to the `F_p` wall",
        "Consequence for PR #2373",
        "Physical Lattice Assumption",
        "Approved Scale-Reference Primitive",
        "Consequence for Y_T",
        "Claim Boundary",
        "Non-Claims",
    ):
        check(f"note contains required phrase: {phrase}", phrase in note)

    check("note marks no-go claim type", "claim_type_author_hint: no_go" in note)
    check("note forbids closure from record algebra alone",
          "closure_claim_allowed_without_new_source_law: false" in note)
    check("note names remaining source-unit route", "physical source-unit/log-selection premise" in note)

    p1p2 = read(P1P2)
    check("parent P1/P2 synthesis records F_p wall", "F_p" in p1p2 and "Pattern-L wall" in p1p2)
    check("parent P1/P2 synthesis records P-cal residual", "P-cal" in p1p2 and "single residual premise" in p1p2)
    scale = read(SCALE_PRIMITIVE)
    check(
        "approved scale primitive records the Planck-mass anchor",
        "a^{-1} = M_Pl" in scale and "Planck mass scale" in scale,
    )

    return {
        "claim_type_author_hint": "no_go",
        "target": "finite record probability calculus alone selects unit log source",
    }


def part2_log_homomorphism_scale() -> dict[str, Any]:
    print("\nPart 2: product composition selects log only up to scale")
    x, y, c = sp.symbols("x y c", positive=True)
    phi = c * sp.log(x)
    check("c log is additive on products", zero(c * sp.log(x * y) - (c * sp.log(x) + c * sp.log(y))))

    # The multiplicative F_p family survives product composition for every p.
    p = sp.symbols("p", real=True)
    F_xy = (x * y) ** p
    F_sep = x**p * y**p
    check("F_p is multiplicative for every p", zero(F_xy - F_sep))
    check("log F_p is p log x", zero(sp.log(x**p) - p * sp.log(x)))

    # Additivity of F_p itself fails generically; this is the old wall.
    numeric_failures = []
    for p_val in (sp.Rational(1, 2), 1, 2, -1):
        lhs = (sp.Rational(2) * sp.Rational(3)) ** p_val
        rhs = sp.Rational(2) ** p_val + sp.Rational(3) ** p_val
        numeric_failures.append(lhs != rhs)
    check("F_p itself is not additive for p != 0 on test values", all(numeric_failures))

    return {
        "homomorphism_family": "c log x",
        "unfixed_parameter": "c",
        "counterfamily": "F_p=x^p is multiplicative for all p",
    }


def part3_rn_scaled_family() -> dict[str, Any]:
    print("\nPart 3: scaled RN families remain valid record interventions")
    h, lam = sp.symbols("h lambda", positive=True)
    weights = {1: sp.Rational(1, 2), -1: sp.Rational(1, 2)}
    Z = sum(weights[e] * sp.exp(lam * h * e) for e in (-1, 1))
    W = sp.log(Z)
    R = {e: sp.exp(lam * h * e - W) for e in (-1, 1)}
    norm = sp.simplify(sum(weights[e] * R[e] for e in (-1, 1)))
    check("scaled RN density normalizes for symbolic lambda", zero(norm - 1), norm)

    score = {e: sp.diff(sp.log(R[e]), h).subs(h, 0) for e in (-1, 1)}
    check("scaled score for + record is lambda", zero(score[1] - lam), score[1])
    check("scaled score for - record is -lambda", zero(score[-1] + lam), score[-1])

    fisher = sp.simplify(sum(weights[e] * score[e] ** 2 for e in (-1, 1)))
    check("scaled Fisher norm is lambda^2", zero(fisher - lam**2), fisher)

    # Independent histories: RN densities multiply and log densities add for every lambda.
    e1, e2 = sp.symbols("e1 e2")
    log_r_total = lam * h * e1 + lam * h * e2 - 2 * W
    log_r_sum = (lam * h * e1 - W) + (lam * h * e2 - W)
    check("scaled RN log-density adds over independent histories", zero(log_r_total - log_r_sum))

    # The same algebra admits every lambda.  Unit Fisher is an extra selector.
    check("lambda=1 is selected only after imposing Fisher unit", sp.solve(sp.Eq(fisher, 1), lam) == [1])
    check("lambda=2 is also a valid normalized RN intervention before unit selector", norm.subs(lam, 2) == 1)

    return {
        "scaled_rn_family": "exp(lambda h O - log E exp(lambda h O))",
        "score": "lambda O",
        "fisher_norm": "lambda^2",
    }


def part4_connected_response_equivalence() -> dict[str, Any]:
    print("\nPart 4: connected-response condition is log-selection in differential form")
    h_a, h_b, p = sp.symbols("h_a h_b p", positive=True)
    # Independent Bernoulli records on two blocks.
    Z_a = sp.cosh(h_a)
    Z_b = sp.cosh(h_b)
    Z = Z_a * Z_b
    W_log = sp.log(Z)
    W_power = Z**p

    mixed_log = sp.simplify(sp.diff(W_log, h_a, h_b))
    mixed_power = sp.simplify(sp.diff(W_power, h_a, h_b))
    check("log generator has zero mixed derivative for independent blocks", zero(mixed_log), mixed_log)

    value = sp.simplify(mixed_power.subs({h_a: sp.Rational(1, 3), h_b: sp.Rational(1, 5), p: 1}))
    check("power generator has nonzero mixed derivative on independent blocks", value != 0, value)

    # Normalized logarithmic derivative hides p, which proves normalization alone
    # does not select the log unit.
    Wp = p * sp.log(Z_a)
    normalized_grad = sp.simplify(sp.diff(Wp, h_a) / p)
    primitive_grad = sp.simplify(sp.diff(sp.log(Z_a), h_a))
    check("dividing by p recovers primitive gradient for every p", zero(normalized_grad - primitive_grad))

    return {
        "mixed_log": str(mixed_log),
        "mixed_power_sample": str(value),
        "lesson": "connected-response locality is equivalent to selecting the log coordinate",
    }


def part5_physical_lattice_boundary() -> dict[str, Any]:
    print("\nPart 5: physical lattice locality does not select lambda")
    h, lam = sp.symbols("h lambda", positive=True)
    site_values = [sp.symbols(f"o{i}") for i in range(3)]
    Z_site = [sp.Function(f"Z{i}")(h) for i in range(3)]
    # A local scaled RN log density on a finite physical lattice region.
    log_density_sites = [lam * h * site_values[i] - sp.log(Z_site[i]) for i in range(3)]
    log_density_region = lam * h * sum(site_values) - sp.log(sp.prod(Z_site))
    check(
        "physical-lattice product source log-density adds over sites for every lambda",
        zero(sp.expand_log(log_density_region, force=True) - sum(log_density_sites)),
    )

    # Locality alone cannot distinguish lambda=1 from lambda=2.
    local_score_lam1 = sp.diff(lam * h * site_values[0], h).subs(lam, 1)
    local_score_lam2 = sp.diff(lam * h * site_values[0], h).subs(lam, 2)
    check("lambda=1 local source is site-local", local_score_lam1 == site_values[0])
    check("lambda=2 local source is also site-local", local_score_lam2 == 2 * site_values[0])
    check("locality does not equate the two source scales", local_score_lam1 != local_score_lam2)

    return {
        "physical_lattice_assumption": "accepted",
        "result": "locality/product structure still admits all lambda source scales",
    }


def part6_planck_scale_boundary() -> dict[str, Any]:
    print("\nPart 6: Planck scale fixes dimensions, not lambda")
    a_inv, m_lat, lam = sp.symbols("a_inv m_lat lambda", positive=True)
    m_phys = m_lat * a_inv
    y33 = lam / sp.sqrt(6)
    check("Planck anchor enters dimensional mass conversion", zero(sp.diff(m_phys, a_inv) - m_lat), m_phys)
    check("dimensionless y33 has no dependence on lattice scale", zero(sp.diff(y33, a_inv)), y33)
    check("setting a^{-1}=M_Pl leaves lambda symbolic", "lambda" in str(y33), y33)
    check("Planck scale would need an extra source-coordinate bridge", y33.subs(lam, 2) != y33.subs(lam, 1))

    return {
        "scale_reference_primitive_anchor": "a^{-1}=M_Pl",
        "result": "dimensionful scale setting does not select dimensionless source lambda",
        "open_positive_route": "derive Planck/action unit = RN/Fisher source coordinate",
    }


def part7_yt_lambda_boundary() -> dict[str, Any]:
    print("\nPart 7: Y_T lambda boundary")
    lam = sp.symbols("lambda", positive=True)
    y33 = lam / sp.sqrt(6)
    check("lambda family leaves y33(lambda)=lambda/sqrt(6)", zero(y33 - lam / sp.sqrt(6)), y33)
    check("lambda=1 gives 1/sqrt(6)", zero(y33.subs(lam, 1) - 1 / sp.sqrt(6)))
    check("lambda=2 gives a different allowed source coefficient absent unit selector", y33.subs(lam, 2) != y33.subs(lam, 1))

    return {
        "yt_family": "y_33(lambda)=lambda/sqrt(6)",
        "remaining_selector": "physical source-unit/log-selection premise or strict same-source response evidence",
    }


def part8_firewall() -> None:
    print("\nPart 8: forbidden-import firewall")
    note = read(NOTE)
    forbidden_load_bearing = (
        "old Ward identity as input",
        "PDG target match",
        "alpha_LM input",
        "plaquette/u0 input",
        "selector fitted from data",
    )
    for phrase in forbidden_load_bearing:
        check(f"forbidden load-bearing phrase absent: {phrase}", phrase not in note)

    required_forbidden_names = (
        "H_unit",
        "yt_ward_identity",
        "y_t_bare",
        "PDG",
        "alpha_LM",
        "plaquette/u0",
        "fitted selectors",
    )
    for phrase in required_forbidden_names:
        check(f"note names forbidden route: {phrase}", phrase in note)


def part9_n5_execution_certificate() -> None:
    """Print-only record of what this runner resolves at each granularity.

    Adds no check, touches no counter, and contributes nothing to the JSON
    result payload.
    """
    print("\nPart 9: N5 execution certificate (print-only; adds no check and no counter)")
    print(
        "per_element: checked and not executed -- no matrix and no linear operator is constructed "
        "anywhere in this runner. Every object it forms is a scalar symbolic expression: logarithms, "
        "exponentials, partition functions, and their derivatives. With no matrix present there is no "
        "matrix element available to resolve, and nothing in this file should be read as resolving "
        "one."
    )
    print(
        "per_site: resolved symbolically across a three-site region -- Part 5 gives each site of a "
        "finite physical lattice region its own observable symbol o_i and its own partition function "
        "Z_i(h), assembles the region log-density as lambda*h*sum(o_i) - log(prod Z_i), and verifies "
        "by forced logarithmic expansion that it equals the sum of the three per-site log-densities "
        "for symbolic lambda. The site-local score is then read at that first site alone under "
        "lambda=1 and lambda=2, returning o_0 and 2*o_0, which is exactly how the file shows locality "
        "cannot separate the two source scales."
    )
    print(
        "per_mode: checked and not executed -- there is no operator in this runner, hence no "
        "spectrum, no eigenmode, and no Fourier decomposition available to resolve. The only "
        "two-valued structure present is the Bernoulli record outcome e in {-1, +1}, whose plus and "
        "minus scores Part 3 does compute separately; those are outcome labels on a probability "
        "space rather than modes of any operator, and this certificate declines to report them as "
        "mode resolution."
    )
    print(
        "per_block: resolved as an explicit two-block independence test -- Part 4 places independent "
        "Bernoulli records on blocks a and b, each with its own field and its own partition function, "
        "then separates the two candidate generators by their mixed second derivative taken across "
        "the block pair: the logarithmic generator has mixed derivative exactly zero while the power "
        "generator does not, evaluated at the exact rational point h_a=1/3, h_b=1/5 with p=1. That "
        "cross-block derivative is the entire content of the connected-response equivalence."
    )
    print(
        "lattice_wide: executed symbolically at one fixed region size and returning a negative, "
        "which is what the certificate reports -- whole-region additivity of the source log-density "
        "is formed and verified for the three-site product at arbitrary lambda, and the lattice "
        "spacing is carried separately through the approved Planck anchor in Part 6. No lattice is "
        "instantiated, no region size is varied, and no thermodynamic limit is taken. More to the "
        "point the outcome is a non-selection: locality and product structure together still admit "
        "every lambda, and the dimensionless coefficient lambda/sqrt(6) is shown to have no "
        "dependence on the lattice scale, so what is established is that no lattice-wide property "
        "selects the source unit, not any lattice-wide value."
    )
    print(
        "Scope, reported plainly: thirty-two of the fifty-seven checks are document tests -- twenty "
        "in Part 1 confirming that six notes exist and contain required phrases, and twelve in Part 8 "
        "confirming that forbidden phrases are absent and required route names present. Those resolve "
        "nothing quantitative. The twenty-five checks in Parts 2 through 7 carry every symbolic "
        "result certified above."
    )
    print(
        "Determinism: the computational parts run on sympy exact symbolic algebra with no "
        "floating-point tolerance anywhere -- equality is decided by simplification against zero, and "
        "the probe points are exact rationals, 1/2, 1, 2 and -1 for the multiplicativity leg and 1/3 "
        "and 1/5 for the mixed derivative. No RNG, optimizer, root-finding, grid scan, Monte Carlo, "
        "or flow integration is used, so no quantity in this certificate is interpolated from a "
        "sampled or converged value."
    )


def main() -> int:
    print("=" * 88)
    print("SOURCE/MEASURE LOG-SELECTION BOUNDARY")
    print("=" * 88)

    result = {
        "document_boundary": part1_document_boundary(),
        "log_homomorphism_scale": part2_log_homomorphism_scale(),
        "rn_scaled_family": part3_rn_scaled_family(),
        "connected_response_equivalence": part4_connected_response_equivalence(),
        "physical_lattice_boundary": part5_physical_lattice_boundary(),
        "planck_scale_boundary": part6_planck_scale_boundary(),
        "yt_lambda_boundary": part7_yt_lambda_boundary(),
    }
    part8_firewall()
    part9_n5_execution_certificate()

    result["summary"] = {
        "pass": PASS_COUNT,
        "fail": FAIL_COUNT,
        "claim_type_author_hint": "no_go",
        "trace_class": "negative_route_pruning",
        "target_blocker": "derive P-cal/log-selection from finite sharp-record source-measure alone",
        "closure_claim_allowed_without_new_source_law": False,
        "remaining_open_routes": [
            "derive physical source-unit law independent of P1",
            "strict same-source top/W response evidence",
            "explicit source-unit axiom/premise",
        ],
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(f"Wrote {OUT.relative_to(ROOT)}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
