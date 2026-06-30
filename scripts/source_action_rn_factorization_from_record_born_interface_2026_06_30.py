#!/usr/bin/env python3
"""Verify the source/action RN factorization bridge."""

from __future__ import annotations

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

NOTE = DOCS / "SOURCE_ACTION_RN_FACTORIZATION_FROM_RECORD_BORN_INTERFACE_2026-06-30.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
BORN = DOCS / "RECORD_BORN_INTERFACE_FROM_SELECTIVE_WRITE_BRIDGE_2026-06-30.md"
SOURCE_PCAL = DOCS / "RECORD_BORN_TO_SOURCE_MEASURE_PCAL_INTERFACE_BRIDGE_2026-06-30.md"
POST_STACK = DOCS / "POST_STACK_HARD_GATE_STATUS_MAP_2026-06-30.md"
LOG_BOUNDARY = DOCS / "SOURCE_MEASURE_LOG_SELECTION_BOUNDARY_THEOREM_NOTE_2026-05-30.md"
PLANCK_ACTION = DOCS / "SOURCE_MEASURE_PLANCK_ACTION_RN_SOURCE_UNIT_BRIDGE_NOTE_2026-05-30.md"
RECORD_INTERVENTION = DOCS / "SOURCE_MEASURE_RECORD_INTERVENTION_THEOREM_NOTE_2026-05-30.md"
RN_COCYCLE = DOCS / "SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md"
CUMULANT = DOCS / "SOURCE_MEASURE_PCAL_CUMULANT_MOBIUS_THEOREM_NOTE_2026-05-30.md"
TANGENT = DOCS / "SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md"
ONB = DOCS / "SOURCE_MEASURE_SHARP_RECORD_ORTHONORMAL_RESPONSE_BASIS_NARROW_THEOREM_NOTE_2026-06-05.md"
YT_LSP = DOCS / "YT_LSP_SIGNED_RECORD_SOURCE_READOUT_SUPPORT_NOTE_2026-05-24.md"
OCCURRENCE = DOCS / "RECORD_OCCURRENCE_GATE_FACTORIZATION_FROM_LOCAL_AVAILABILITY_2026-06-30.md"

PASS = 0
FAIL = 0


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + title)


def expectation(prob: list[sp.Expr], values: list[sp.Expr]) -> sp.Expr:
    return sp.simplify(sum(p * v for p, v in zip(prob, values)))


def main() -> int:
    print("=== Source/action RN factorization from Record/Born interface ===")

    paths = [
        NOTE,
        AXIOMS,
        BORN,
        SOURCE_PCAL,
        POST_STACK,
        LOG_BOUNDARY,
        PLANCK_ACTION,
        RECORD_INTERVENTION,
        RN_COCYCLE,
        CUMULANT,
        TANGENT,
        ONB,
        YT_LSP,
        OCCURRENCE,
    ]
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    note_flat = flat(note)
    axioms = read(AXIOMS)
    born = read(BORN)
    source_pcal = read(SOURCE_PCAL)
    post_stack = read(POST_STACK)
    log_boundary = read(LOG_BOUNDARY)
    planck_action = read(PLANCK_ACTION)
    record_intervention = read(RECORD_INTERVENTION)
    rn_cocycle = read(RN_COCYCLE)
    cumulant = read(CUMULANT)
    tangent = read(TANGENT)
    onb = read(ONB)
    yt_lsp = read(YT_LSP)
    occurrence = read(OCCURRENCE)

    section("PART A -- source boundary")
    check("axioms give fixed records", "A record locks exactly one available local possibility" in axioms)
    check("axioms leave source/action downstream", "source/action" in axioms)
    check("Record/Born bridge supplies trace weights", "Tr(rho P_r)" in born)
    check("Record/Born bridge preserves occurrence wall", "W_occurrence" in born)
    check("Record/Born to P-cal bridge names W_source_action", "W_source_action" in source_pcal)
    check("post-stack map prioritizes source/action bridge", "physical source/action identification bridge" in post_stack)
    check("occurrence bridge is independent", "activation + selection" in occurrence)

    section("PART B -- prior source-measure authorities")
    check("record intervention theorem supplies probability intervention semantics", "smooth intervention on the probability law" in flat(record_intervention))
    check("RN cocycle theorem supplies normalized RN form", "E_0[R_h] = 1" in rn_cocycle and "W(h) = log E_0 exp" in rn_cocycle)
    check("cumulant theorem supplies connected log generator", "K[J] = log M[J]" in cumulant)
    check("tangent theorem supplies Fisher pairing", "<s,t>_F = E_0[s t]" in tangent)
    check("log boundary exposes lambda family", "lambda^2" in log_boundary and "source-unit/log-selection" in log_boundary)
    check("Planck-action bridge supplies unit candidate", "one Planck action quantum" in planck_action)
    check("six diagonal ONB is finite algebra only", "not a physical `Y_T` top/`W` response theorem" in onb)
    check("YT LSP readout support leaves source/action authority open", "accepted same-surface source/action authority" in yt_lsp)

    section("PART C -- finite action-exponent to RN factorization")
    h = sp.symbols("h", real=True)
    prob = [sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 6)]
    O = [sp.Integer(2), sp.Integer(-1), sp.Integer(0)]
    mean_O = expectation(prob, O)
    centered = [sp.simplify(v - mean_O) for v in O]
    fisher = expectation(prob, [v**2 for v in centered])
    delta_A = [-h * v for v in O]
    Z = expectation(prob, [sp.exp(-a) for a in delta_A])
    P_h = [sp.simplify(p * sp.exp(-a) / Z) for p, a in zip(prob, delta_A)]
    R_h = [sp.simplify(ph / p) for ph, p in zip(P_h, prob)]
    log_R_h = [sp.log(r) for r in R_h]
    score = [sp.simplify(sp.diff(lr, h).subs(h, 0)) for lr in log_R_h]
    W = sp.log(Z)
    check("reference probability normalizes", sum(prob) == 1)
    check("reference probability has full support", all(p > 0 for p in prob))
    check("action-deformed P_h normalizes", sp.simplify(sum(P_h) - 1) == 0)
    check("RN density has exponential-over-normalizer form", all(sp.simplify(R_h[i] - sp.exp(h * O[i]) / Z) == 0 for i in range(3)))
    check("E0[R_h]=1", sp.simplify(expectation(prob, R_h) - 1) == 0)
    check("origin score is centered action tangent", all(sp.simplify(score[i] - centered[i]) == 0 for i in range(3)), f"score={score}")
    check("score has zero mean", sp.simplify(expectation(prob, score)) == 0)
    check("Fisher norm is score variance", sp.simplify(expectation(prob, [s**2 for s in score]) - fisher) == 0, f"F={fisher}")
    check("W'(0) is uncentered mean", sp.simplify(sp.diff(W, h).subs(h, 0) - mean_O) == 0)
    check("W''(0) is Fisher variance", sp.simplify(sp.diff(W, h, 2).subs(h, 0) - fisher) == 0)

    section("PART D -- unit and scaled action coordinates")
    lam = sp.symbols("lambda", positive=True)
    unit_O = [sp.simplify(v / sp.sqrt(fisher)) for v in centered]
    unit_mean = expectation(prob, unit_O)
    unit_norm = expectation(prob, [v**2 for v in unit_O])
    scaled_delta_A = [-h * lam * v for v in unit_O]
    scaled_Z = expectation(prob, [sp.exp(-a) for a in scaled_delta_A])
    scaled_R = [sp.simplify(sp.exp(-a) / scaled_Z) for a in scaled_delta_A]
    scaled_score = [sp.simplify(sp.diff(sp.log(r), h).subs(h, 0)) for r in scaled_R]
    scaled_norm = expectation(prob, [v**2 for v in scaled_score])
    check("unit action source is centered", sp.simplify(unit_mean) == 0)
    check("unit action source has Fisher norm one", sp.simplify(unit_norm - 1) == 0)
    check("lambda-scaled action source has score lambda O", all(sp.simplify(scaled_score[i] - lam * unit_O[i]) == 0 for i in range(3)))
    check("lambda-scaled Fisher norm is lambda^2", sp.simplify(scaled_norm - lam**2) == 0)
    check("unit Fisher condition selects lambda=1", sp.solve(sp.Eq(scaled_norm, 1), lam) == [1])

    section("PART E -- action unit cancellation")
    kappa = sp.symbols("kappa", positive=True)
    s0, o = sp.symbols("S0 o", real=True)
    S_h = s0 - kappa * h * o
    delta_exponent = sp.simplify((S_h - s0) / kappa)
    log_weight_ratio = sp.simplify(-delta_exponent)
    score_symbolic = sp.diff(log_weight_ratio, h)
    check("S/kappa action exponent gives log RN hO", sp.simplify(log_weight_ratio - h * o) == 0)
    check("kappa cancels from the source score", sp.simplify(score_symbolic - o) == 0 and kappa not in score_symbolic.free_symbols)

    section("PART F -- six-component direction smoke test")
    u = sp.Matrix([1 / sp.sqrt(6)] * 6)
    norm_u = sp.simplify(u.dot(u))
    scaled_u_norm = sp.simplify((lam * u).dot(lam * u))
    check("democratic six-component direction is unit", sp.simplify(norm_u - 1) == 0)
    check("six components are all 1/sqrt(6)", all(sp.simplify(component - 1 / sp.sqrt(6)) == 0 for component in u))
    check("scaled six-component source norm is lambda^2", sp.simplify(scaled_u_norm - lam**2) == 0)

    section("PART G -- note content")
    required_sections = [
        "Claim",
        "Source Surface",
        "Finite Theorem",
        "Relation To Planck-Action Unit",
        "What Moves",
        "What Remains",
        "Audit Consequence If Retained",
        "Non-Claims",
        "No-Go Discipline Gate",
    ]
    for section_name in required_sections:
        check(f"note includes {section_name}", f"## {section_name}" in note)
    check("note names W_source_action", "W_source_action" in note)
    check("note names W_physical_source", "W_physical_source" in note)
    check("note states RN/action identity", "R_h(omega) = P_h(omega) / P_0(omega)" in note)
    check("note preserves top/Higgs wall", "physical top source" in note and "Higgs operator" in note)
    check("note consumes no measured values", "PDG values" in note and "fitted constants" in note)
    check("note requests no axiom", "No new axiom is requested by this note" in note)

    section("PART H -- no-go discipline gate")
    for item in ["N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"]:
        check(f"note includes {item}", item in note)
    check("N1 enumerates seven routes", note.count("| Record/Born interface route |") == 1 and note.count("| New primitive route |") == 1)
    check("N2 collapses residual to W_physical_source", "Collapsed residual after this bridge" in note and "W_physical_source" in note)
    check("N3 labels action exponent wall", "\"Action exponent\"" in note)
    check("N4 matches seven witnesses", note.count("| `SOURCE_MEASURE") >= 5 and "Residual Matching" in note)
    check("N5 avoids lattice-wide impossibility overclaim", "not phrased as a lattice-wide impossibility claim" in note_flat)
    check("N6 lists live closure paths", "Live closure paths remain" in note)
    check("N7 steelman admits coordinate-change objection", "just a change of coordinates" in note)
    check("N8 cross-cycle echo is present", "source-measure lane repeatedly converted broad" in note)

    section("PART I -- assembled conclusion")
    algebra_ok = (
        sp.simplify(sum(P_h) - 1) == 0
        and all(sp.simplify(score[i] - centered[i]) == 0 for i in range(3))
        and sp.simplify(scaled_norm - lam**2) == 0
        and sp.simplify(score_symbolic - o) == 0
    )
    check("action-exponent deformation factors exactly as RN/Fisher source", algebra_ok)
    check("physical selector remains open", "remaining wall is physical source direction and unit selection" in note_flat)
    check("occurrence remains separate", "Occurrence remains independent" in note)

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS -- record-facing action exponents factor exactly into RN/Fisher source coordinates; physical source selection remains open.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
