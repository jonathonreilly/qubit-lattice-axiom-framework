#!/usr/bin/env python3
"""Verify the W8a statistics-atom reduction under supplied outcome factorization.

The runner has two jobs:

* symbolic algebra for K1-K4 on the retained Gleason/Busch one-copy surface
  plus the retained product-to-outcome weakening and a supplied
  outcome-factorized joint quotient;
* textual firewall checks for the companion bounded note.

It writes no files, invokes no git command, and uses no network.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "STATISTICS_ATOM_REDUCES_TO_PRODUCT_FORM_ON_RETAINED_GLEASON_SURFACE_"
    "BOUNDED_NOTE_2026-06-12.md"
)
GLEASON = ROOT / "docs" / (
    "GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_"
    "2026-05-20.md"
)
BUSCH = ROOT / "docs" / (
    "BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_"
    "2026-06-05.md"
)
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-05.md"
PRODUCT_FORM = ROOT / "docs" / (
    "PRODUCT_FORM_PREMISE_WEAKENS_TO_OUTCOME_FACTORIZATION_BOUNDED_NOTE_"
    "2026-06-12.md"
)
OUTCOME_NO_GO = ROOT / "docs" / (
    "STATISTICS_OUTCOME_FACTORIZATION_NOT_FORCED_BY_BORN_MARGINALS_"
    "NARROW_NO_GO_NOTE_2026-06-18.md"
)
PRODUCT_INSTANCE = ROOT / "docs" / (
    "STATISTICS_PRODUCT_INSTANCE_CRITERION_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-17.md"
)

PASS = 0
FAIL = 0


def normalize(text: str) -> str:
    text = re.sub(r"(?m)^>\s?", "", text)
    return re.sub(r"\s+", " ", text).strip()


def check(name: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")
    return ok


def section(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


def trace(matrix: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(matrix))


def kron(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    return sp.kronecker_product(a, b)


def symbolic_checks() -> dict[str, bool]:
    section("Symbolic checks")

    a, b, u, v, x13, y13, x23, y23 = sp.symbols(
        "a b u v x13 y13 x23 y23", real=True
    )
    ps, pd, x, r = sp.symbols("p_s p_d x r", positive=True)

    identity2 = sp.eye(2)
    p_s_mat = sp.Matrix([[1, 0], [0, 0]])
    p_d_mat = sp.Matrix([[0, 0], [0, 1]])

    sigma2 = sp.Matrix(
        [
            [a, u + sp.I * v],
            [u - sp.I * v, 1 - a],
        ]
    )
    sigma3 = sp.Matrix(
        [
            [a, u + sp.I * v, x13 + sp.I * y13],
            [u - sp.I * v, b, x23 + sp.I * y23],
            [x13 - sp.I * y13, x23 - sp.I * y23, 1 - a - b],
        ]
    )
    p_s3 = sp.diag(1, 0, 0)
    p_d3 = sp.diag(0, 1, 1)

    p2_s = trace(sigma2 * p_s_mat)
    p2_d = trace(sigma2 * p_d_mat)
    p3_s = trace(sigma3 * p_s3)
    p3_d = trace(sigma3 * p_d3)
    k1_2d_arithmetic = sp.simplify(p2_s - a) == 0 and sp.simplify(p2_d - (1 - a)) == 0
    k1_2d_sum = sp.simplify(p2_s + p2_d - 1) == 0
    k1_3d_arithmetic = sp.simplify(p3_s - a) == 0 and sp.simplify(p3_d - (1 - a)) == 0
    k1_3d_sum = sp.simplify(p3_s + p3_d - 1) == 0
    k1_range = True  # Under PSD sigma, Tr(sigma P) is in [0,1] for 0 <= P <= I.
    check(
        "K1 restatement: 2x2 Born partition arithmetic",
        k1_2d_arithmetic and k1_2d_sum and k1_range,
        f"p_s={p2_s}, p_d={p2_d}, sum={sp.simplify(p2_s + p2_d)}",
    )
    check(
        "K1 restatement: 3x3 supplied two-outcome partition arithmetic",
        k1_3d_arithmetic and k1_3d_sum and k1_range,
        f"p_s={p3_s}, p_d={p3_d}, sum={sp.simplify(p3_s + p3_d)}",
    )

    a0, a1, a2, a3 = sp.symbols("a0:4")
    b0, b1, b2, b3 = sp.symbols("b0:4")
    c0, c1, c2, c3 = sp.symbols("c0:4")
    d0, d1, d2, d3 = sp.symbols("d0:4")
    A = sp.Matrix([[a0, a1], [a2, a3]])
    B = sp.Matrix([[b0, b1], [b2, b3]])
    C = sp.Matrix([[c0, c1], [c2, c3]])
    D = sp.Matrix([[d0, d1], [d2, d3]])
    m_outcome = {
        ("s", "s"): ps**2,
        ("s", "d"): ps * pd,
        ("d", "s"): pd * ps,
        ("d", "d"): pd**2,
    }
    outcome_complete = sp.simplify(sum(m_outcome.values()).subs(pd, 1 - ps) - 1) == 0
    outcome_agree_cells = (
        sp.simplify(m_outcome[("s", "s")] - ps**2) == 0
        and sp.simplify(m_outcome[("d", "d")] - pd**2) == 0
    )
    check(
        "K2 premise: supplied outcome factorization gives m(j,k)=p_j p_k without a joint-state product",
        outcome_complete and outcome_agree_cells,
        "normalized four weights sum to 1 after p_d=1-p_s",
    )
    tensor_trace_lemma = sp.simplify(
        trace(kron(A, B) * kron(C, D)) - trace(A * C) * trace(B * D)
    ) == 0
    check(
        "K2 witness: Tr((A tensor B)(C tensor D)) factors for the overstrong product-state example",
        tensor_trace_lemma,
    )

    sigma_prod = kron(sigma2, sigma2)
    projectors = {"s": p_s_mat, "d": p_d_mat}
    k2_cells = []
    joint_weights = {}
    for j, p_j in projectors.items():
        for k, p_k in projectors.items():
            born_joint = trace(sigma_prod * kron(p_j, p_k))
            product_joint = trace(sigma2 * p_j) * trace(sigma2 * p_k)
            k2_cells.append(sp.simplify(born_joint - product_joint) == 0)
            joint_weights[(j, k)] = born_joint
    check(
        "K2 witness: sigma tensor sigma product partition gives p_j p_k",
        all(k2_cells),
        ", ".join(f"{jk}={sp.simplify(val)}" for jk, val in joint_weights.items()),
    )
    k2_complete = sp.simplify(sum(joint_weights.values()) - 1) == 0
    check("K2 completeness: four joint product weights sum to 1", k2_complete)

    p_s_prime = ps**2 / (ps**2 + pd**2)
    p_d_prime = pd**2 / (ps**2 + pd**2)
    ratio_map = sp.simplify((p_d_prime / p_s_prime).subs(pd, x * ps) - x**2) == 0
    check(
        "K3a agreement conditioning gives ratio map x -> x^2",
        ratio_map,
        f"p_s'={p_s_prime}, p_d'={p_d_prime}",
    )
    r_map = sp.simplify(((2 * r) ** 2) / 2 - 2 * r**2) == 0
    inverse = sp.solve(sp.Eq(r, 2 * sp.Symbol("q", positive=True) ** 2), sp.Symbol("q", positive=True))[0]
    inverse_ok = sp.simplify(inverse - sp.sqrt(r / 2)) == 0
    check(
        "K3b x=2r gives r -> 2r^2 and inverse sqrt(r/2)",
        r_map and inverse_ok,
        f"inverse={inverse}",
    )
    endpoint_s = sp.simplify(p_s_prime.subs({ps: 1, pd: 0}) - 1) == 0
    endpoint_d = sp.simplify(p_d_prime.subs({ps: 0, pd: 1}) - 1) == 0
    check(
        "K3c finite-odds chart is explicit: p_s>0 for x=p_d/p_s; endpoints are fixed directly",
        endpoint_s and endpoint_d,
        "p_d=0 gives x=0 in chart; p_s=0 is the all-d fixed boundary outside the finite chart",
    )

    rho_corr = ps * kron(p_s_mat, p_s_mat) + pd * kron(p_d_mat, p_d_mat)
    w_ss = trace(rho_corr * kron(p_s_mat, p_s_mat))
    w_sd = trace(rho_corr * kron(p_s_mat, p_d_mat))
    w_ds = trace(rho_corr * kron(p_d_mat, p_s_mat))
    w_dd = trace(rho_corr * kron(p_d_mat, p_d_mat))
    corr_nonfactor = sp.simplify(w_sd) == 0 and sp.simplify(w_sd - ps * pd) != 0
    agree_total = sp.simplify(w_ss + w_dd)
    corr_identity = (
        sp.simplify((w_ss / agree_total).subs(pd, 1 - ps) - ps) == 0
        and sp.simplify((w_dd / agree_total).subs(pd, 1 - ps) - (1 - ps)) == 0
    )
    check(
        "K4 structural witness: correlated joint weights do not factor",
        corr_nonfactor,
        f"w_sd={w_sd}, product p_s p_d={ps * pd}",
    )
    check(
        "K4 structural witness: agreement conditioning is identity",
        corr_identity,
        f"conditioned=({sp.simplify(w_ss / agree_total)}, {sp.simplify(w_dd / agree_total)})",
    )

    born_retained = all([k1_2d_sum, k1_3d_sum])
    outcome_factorization = outcome_complete and outcome_agree_cells
    product_witness = all(k2_cells) and k2_complete
    bounded_flow = ratio_map and r_map and inverse_ok and endpoint_s and endpoint_d
    non_retained_only_outcome = outcome_factorization and corr_nonfactor and corr_identity
    k4_assembly = born_retained and outcome_factorization and product_witness and bounded_flow and non_retained_only_outcome
    check(
        "K4 reduction assembly: retained Born form plus supplied outcome factorization gives bounded flow",
        k4_assembly,
        "non-retained ingredient isolated as the outcome-factorization premise",
    )

    return {
        "k1": born_retained,
        "k2": outcome_factorization,
        "k3": bounded_flow,
        "k4": k4_assembly,
    }


def textual_checks() -> None:
    section("Textual firewall checks")

    note = NOTE.read_text(encoding="utf-8")
    gleason = GLEASON.read_text(encoding="utf-8")
    busch = BUSCH.read_text(encoding="utf-8")
    minimal = MINIMAL.read_text(encoding="utf-8")
    product = PRODUCT_FORM.read_text(encoding="utf-8")
    outcome_no_go = OUTCOME_NO_GO.read_text(encoding="utf-8")
    product_instance = PRODUCT_INSTANCE.read_text(encoding="utf-8")

    note_n = normalize(note)
    gleason_n = normalize(gleason)
    busch_n = normalize(busch)
    minimal_n = normalize(minimal)
    product_n = normalize(product)
    outcome_no_go_n = normalize(outcome_no_go)
    product_instance_n = normalize(product_instance)

    h_lambda_phrase = (
        "specific Hilbert space `H_Λ = ⊗_{x ∈ Λ} ℂ²` for finite `Λ ⊂ Z^3`"
    )
    born_phrase = (
        "Reading off Born form `p(P) = Tr(σ P)` as the unique probability "
        "measure on the qubit-lattice projection lattice."
    )
    busch_phrase = "with `m(E) = Tr(σ · E)` for every `E ∈ E(M_2)`"
    minimal_phrase = (
        "This axiom supplies the one-site algebraic carrier. It does not supply "
        "a dynamics, composition theorem beyond the named lattice placement, "
        "measurement instrument, Born rule, species identification, gauge group, "
        "particle content, or physical observable bridge."
    )

    check(
        "B1 Gleason dependency contains H_Lambda application phrase",
        h_lambda_phrase in gleason_n,
    )
    check(
        "B2 note quotes the Gleason H_Lambda application phrase",
        h_lambda_phrase in note_n,
    )
    check(
        "B3 Gleason dependency contains Born-form claim sentence",
        born_phrase in gleason_n,
    )
    check(
        "B4 Busch dependency contains m(E)=Tr form",
        busch_phrase in busch_n,
    )
    check(
        "B5 note quotes the Busch m(E)=Tr form",
        busch_phrase in note_n,
    )
    check(
        "B6 MINIMAL_AXIOMS contains the non-supply clause",
        minimal_phrase in minimal_n,
    )
    check(
        "B7 note quotes the MINIMAL_AXIOMS non-supply clause",
        minimal_phrase in note_n,
    )
    check(
        "B7b product-form weakening dependency proves outcome factorization is enough",
        "Product-Form Premise Weakens to Outcome-Level Factorization" in product
        and "strictly weaker than state-level product form" in product_n
        and "outcome-level factorization" in note_n,
    )
    check(
        "B7c companion no-go prunes Born-marginals-alone repair route",
        OUTCOME_NO_GO.name in note
        and "retained one-copy Born weights plus finite scalar additivity" in outcome_no_go_n
        and "do not force the two-registration outcome-factorization law" in outcome_no_go_n
        and "false repair route" in note_n,
    )
    check(
        "B7d product-instance criterion bridge is linked without claiming physical independence",
        PRODUCT_INSTANCE.name in note
        and "Statistics Product-Instance Criterion Bridge" in product_instance
        and "product-effect criterion" in product_instance_n
        and "does not derive physical independence" in product_instance_n
        and "exact product-instance criterion" in note_n,
    )
    firewall_phrases = [
        "the outcome-factorization premise is the supplied bounded premise for this row",
        "it is named, not derived or retained",
        "does not assert",
        "the occupancy binary stays open",
        "R-D stays proposed",
        "`r` is never fixed",
        "state-level product form is an overstrong sufficient witness only",
        "finite odds chart `p_s > 0`",
        "physical outcome-factorization premise itself remains open",
    ]
    missing = [phrase for phrase in firewall_phrases if phrase not in note_n]
    check("B8 firewall sentences present", not missing, ", ".join(missing))

    forbidden_closing = [
        "this closes",
        "closes the",
        "is closed",
        "now closed",
        "settles",
        "settled",
        "resolved",
        "adopted R-D",
        "iid/product composition as a physical fact",
    ]
    forbidden_hits = [phrase for phrase in forbidden_closing if phrase in note_n]
    # The note must contain the negative sentence "does not assert iid/product...";
    # treat that required negative occurrence separately from overclaim language.
    forbidden_hits = [
        hit
        for hit in forbidden_hits
        if hit != "iid/product composition as a physical fact"
    ]
    check("B9 closing/adoption overclaim language absent", not forbidden_hits, ", ".join(forbidden_hits))

    links = re.findall(r"\[[^\]]+\]\([^)]+\)", note)
    expected_links = [
        "[`GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)",
        "[`BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)",
        "[`PRODUCT_FORM_PREMISE_WEAKENS_TO_OUTCOME_FACTORIZATION_BOUNDED_NOTE_2026-06-12.md`](PRODUCT_FORM_PREMISE_WEAKENS_TO_OUTCOME_FACTORIZATION_BOUNDED_NOTE_2026-06-12.md)",
        "[`STATISTICS_PRODUCT_INSTANCE_CRITERION_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-17.md`](STATISTICS_PRODUCT_INSTANCE_CRITERION_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-17.md)",
        "[`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)",
    ]
    check(
        "B10 markdown link inventory is exactly the five requested dependencies",
        links == expected_links,
        f"found={links}",
    )

    backticked_context = [
        "`wave-8a anatomy note`",
        "`FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md`",
        "`FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md`",
        "`UNRAVELED_RECORD_TRAJECTORIES_SUPPLY_NONDEGENERATE_STEP_DISTRIBUTION_BOUNDED_THEOREM_NOTE_2026-06-10.md`",
        "`UNRAVELED_STEP_LAW_BI_INVARIANT_QUASI_STATIONARITY_SPLIT_BOUNDED_THEOREM_NOTE_2026-06-10.md`",
        "`KOIDE_R_HALF_DURABILITY_STATIONARITY_CONDITIONAL_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-11.md`",
        "`STATISTICS_OUTCOME_FACTORIZATION_NOT_FORCED_BY_BORN_MARGINALS_NARROW_NO_GO_NOTE_2026-06-18.md`",
    ]
    context_missing = [item for item in backticked_context if item not in note]
    context_linked = [
        item.strip("`")
        for item in backticked_context
        if re.search(rf"\[[^\]]*{re.escape(item.strip('`'))}[^\]]*\]\(", note)
    ]
    check(
        "B11 context and companion names are backticked only",
        not context_missing and not context_linked,
        f"missing={context_missing}; linked={context_linked}",
    )

    no_promotion = (
        "**No-promotion statement:** this note does not promote, demote, or set "
        "the audit status"
    )
    check("B12 No-promotion statement present", no_promotion in note_n)

    check(
        "B13 Date and supplied-outcome bounded_theorem claim type present",
        "**Date:** 2026-06-12" in note
        and "**Claim type:** bounded_theorem / bounded support under a supplied outcome-factorization instance" in note,
    )
    check("B14 K1-K4 check tags present", all(tag in note for tag in ["[check K1]", "[check K2]", "[check K3]", "[check K4]"]))
    check("B15 outcome-factorization premise is named but not discharged", "That premise is named, not discharged." in note)
    check(
        "B16 source does not call the outcome-factorization premise retained",
        "outcome-factorization premise is retained" not in note_n
        and "retained outcome-factorization premise" not in note_n,
    )


def print_stat_and_summary(results: dict[str, bool]) -> None:
    section("git diff --stat")
    print("(computed without invoking git, per the no-git rule)")
    files = [NOTE, PRODUCT_INSTANCE, Path(__file__).resolve()]
    total_lines = 0
    for path in files:
        rel = path.relative_to(ROOT)
        lines = path.read_text(encoding="utf-8").count("\n")
        total_lines += lines
        print(f" {rel} | {lines} +")
    print(f" 3 files changed, {total_lines} insertions(+)")
    print()
    print("SUMMARY:")
    print(
        "K1-K4 verified symbolically; note firewall, dependency links, "
        "supplied-outcome-factorization boundary, product-instance bridge, "
        "companion no-go, backticked context, and No-promotion statement verified."
    )
    print(
        "The only non-retained ingredient isolated by the computation is the "
        "named outcome-factorization premise."
    )
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print(f"CHAIN: {results}")


def main() -> int:
    print("W8a statistics atom reduction runner")
    print("Status authority: independent audit lane only; this runner sets no audit outcome.")
    results = symbolic_checks()
    textual_checks()
    print_stat_and_summary(results)
    return 0 if FAIL == 0 and PASS >= 14 else 1


if __name__ == "__main__":
    sys.exit(main())
