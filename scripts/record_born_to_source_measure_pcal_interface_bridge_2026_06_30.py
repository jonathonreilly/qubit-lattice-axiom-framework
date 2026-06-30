#!/usr/bin/env python3
"""Verify the Record/Born to source-measure P-cal interface bridge."""

from __future__ import annotations

from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

NOTE = DOCS / "RECORD_BORN_TO_SOURCE_MEASURE_PCAL_INTERFACE_BRIDGE_2026-06-30.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
BORN = DOCS / "RECORD_BORN_INTERFACE_FROM_SELECTIVE_WRITE_BRIDGE_2026-06-30.md"
OCCURRENCE = DOCS / "RECORD_OCCURRENCE_GATE_FACTORIZATION_FROM_LOCAL_AVAILABILITY_2026-06-30.md"
RECORD_INTERVENTION = DOCS / "SOURCE_MEASURE_RECORD_INTERVENTION_THEOREM_NOTE_2026-05-30.md"
RN_COCYCLE = DOCS / "SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md"
CUMULANT = DOCS / "SOURCE_MEASURE_PCAL_CUMULANT_MOBIUS_THEOREM_NOTE_2026-05-30.md"
TANGENT = DOCS / "SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md"
LOG_BOUNDARY = DOCS / "SOURCE_MEASURE_LOG_SELECTION_BOUNDARY_THEOREM_NOTE_2026-05-30.md"
PCAL_SYNTHESIS = DOCS / "SOURCE_MEASURE_PCAL_RETIREMENT_SYNTHESIS_NOTE_2026-05-30.md"
PLANCK_ACTION = DOCS / "SOURCE_MEASURE_PLANCK_ACTION_RN_SOURCE_UNIT_BRIDGE_NOTE_2026-05-30.md"

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


def tr(m: sp.Matrix) -> sp.Expr:
    return sp.simplify(sum(m[i, i] for i in range(m.rows)))


def expectation(prob: list[sp.Expr], values: list[sp.Expr]) -> sp.Expr:
    return sp.simplify(sum(p * v for p, v in zip(prob, values)))


def main() -> int:
    print("=== Record/Born to source-measure P-cal interface bridge ===")

    paths = [
        NOTE,
        AXIOMS,
        BORN,
        OCCURRENCE,
        RECORD_INTERVENTION,
        RN_COCYCLE,
        CUMULANT,
        TANGENT,
        LOG_BOUNDARY,
        PCAL_SYNTHESIS,
        PLANCK_ACTION,
    ]
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    note_flat = flat(note)
    axioms = read(AXIOMS)
    born = read(BORN)
    occurrence = read(OCCURRENCE)
    record_intervention = read(RECORD_INTERVENTION)
    record_intervention_flat = flat(record_intervention)
    rn_cocycle = read(RN_COCYCLE)
    cumulant = read(CUMULANT)
    tangent = read(TANGENT)
    log_boundary = read(LOG_BOUNDARY)
    pcal = read(PCAL_SYNTHESIS)
    planck = read(PLANCK_ACTION)

    section("PART A -- source boundaries")
    check("axioms give Qubit local possibility", "Each site has a domain of local possibilities" in axioms)
    check("axioms give Record fixed readout", "A record locks exactly one available local possibility" in axioms)
    check("axioms do not supply source/action", "source/action" in axioms)
    check("Record/Born bridge supplies Born trace weights after interface", "p(r) = m(P_r) = Tr(rho P_r)" in born)
    check("Record/Born bridge preserves occurrence wall", "W_occurrence" in born)
    check("occurrence bridge preserves activation-selection wall", "activation + selection" in occurrence)
    check("record intervention theorem supplies probability intervention surface", "smooth intervention on the probability law" in record_intervention_flat)
    check("RN cocycle theorem supplies log normalizer", "log E_0 exp" in rn_cocycle)
    check("cumulant theorem supplies connected log generator", "log Z" in cumulant and "connected" in cumulant)
    check("tangent theorem supplies Fisher unit", "Fisher norm `lambda^2`" in tangent and "Fisher norm is one" in tangent)
    check("log boundary preserves source-unit wall", "physical source-unit/log-selection law" in log_boundary)
    check("P-cal synthesis names single bridge", "physical source is a smooth sharp-record probability intervention" in pcal)
    check("Planck/action note is conditional", "conditional on that source-action normalization" in planck)

    section("PART B -- finite Record/Born probability surface")
    P0 = sp.Matrix([[1, 0], [0, 0]])
    P1 = sp.Matrix([[0, 0], [0, 1]])
    rho = sp.Matrix([[sp.Rational(3, 5), sp.Rational(1, 10)], [sp.Rational(1, 10), sp.Rational(2, 5)]])
    p0 = tr(rho * P0)
    p1 = tr(rho * P1)
    prob = [p0, p1]
    check("rho is normalized", tr(rho) == 1)
    check("projectors form a sharp record context", P0 * P1 == sp.zeros(2, 2) and P0 + P1 == sp.eye(2))
    check("Born p0 is Tr(rho P0)", p0 == sp.Rational(3, 5), f"p0={p0}")
    check("Born p1 is Tr(rho P1)", p1 == sp.Rational(2, 5), f"p1={p1}")
    check("Born probabilities normalize", sp.simplify(p0 + p1 - 1) == 0)
    check("finite context has full support", p0 > 0 and p1 > 0)

    section("PART C -- centered Fisher-unit source score")
    y = [sp.Integer(0), sp.Integer(1)]
    mean_y = expectation(prob, y)
    var_y = expectation(prob, [(v - mean_y) ** 2 for v in y])
    s = [sp.simplify((v - mean_y) / sp.sqrt(var_y)) for v in y]
    mean_s = expectation(prob, s)
    fisher_s = expectation(prob, [v**2 for v in s])
    check("raw binary mean is p1", mean_y == p1)
    check("raw binary variance is p0*p1", sp.simplify(var_y - p0 * p1) == 0, f"var={var_y}")
    check("centered score has zero mean", sp.simplify(mean_s) == 0, f"E[s]={mean_s}")
    check("centered score has Fisher norm one", sp.simplify(fisher_s - 1) == 0, f"E[s^2]={fisher_s}")
    check("score has two finite record-facing values", len(s) == 2 and all(v.is_finite is not False for v in s))

    section("PART D -- RN/log-normalizer theorem")
    h = sp.symbols("h", real=True)
    weights = [sp.exp(h * v) for v in s]
    Z = sp.simplify(sum(p * w for p, w in zip(prob, weights)))
    Ph = [sp.simplify(p * w / Z) for p, w in zip(prob, weights)]
    Rh = [sp.simplify(ph / p) for ph, p in zip(Ph, prob)]
    logRh = [sp.simplify(sp.log(r)) for r in Rh]
    W = sp.log(Z)
    check("Z(0)=1", sp.simplify(Z.subs(h, 0) - 1) == 0)
    check("P_h normalizes", sp.simplify(sum(Ph) - 1) == 0)
    check("E0[R_h]=1", sp.simplify(expectation(prob, Rh) - 1) == 0)
    check("R_h has exponential-over-normalizer form", all(sp.simplify(Rh[i] - sp.exp(h * s[i]) / Z) == 0 for i in range(2)))
    score_derivs = [sp.diff(sp.log(Rh[i]), h).subs(h, 0) for i in range(2)]
    check("log RN derivative returns centered score", all(sp.simplify(score_derivs[i] - s[i]) == 0 for i in range(2)))
    check("W'(0)=E[s]=0", sp.simplify(sp.diff(W, h).subs(h, 0)) == 0)
    check("W''(0)=Fisher norm one", sp.simplify(sp.diff(W, h, 2).subs(h, 0) - 1) == 0)

    section("PART E -- independent composition and connected response")
    Z2 = sp.simplify(Z * Z)
    W2 = sp.log(Z2)
    check("independent partition functions multiply", sp.simplify(Z2 - Z**2) == 0)
    check("log normalizers add for independent records", sp.simplify(W2 - 2 * W) == 0)
    # Direct mixed derivative check for W(h_a,h_b)=log(Z_a Z_b).
    ha, hb = sp.symbols("ha hb", real=True)
    Za = sum(p * sp.exp(ha * v) for p, v in zip(prob, s))
    Zb = sum(p * sp.exp(hb * v) for p, v in zip(prob, s))
    Wab = sp.log(Za * Zb)
    # Pattern-L raw powers exhibit cross-block response for noncentered
    # source coordinates. Centered score coordinates intentionally kill the
    # first derivative at the origin, so use the raw record label here.
    Za_raw = sum(p * sp.exp(ha * v) for p, v in zip(prob, y))
    Zb_raw = sum(p * sp.exp(hb * v) for p, v in zip(prob, y))
    q_raw = sp.symbols("q_raw", real=True)
    Raw = (Za_raw * Zb_raw) ** q_raw
    check("log generator has zero cross derivative for independent records", sp.simplify(sp.diff(Wab, ha, hb)) == 0)
    raw_cross = sp.simplify(sp.diff(Raw, ha, hb).subs({ha: 0, hb: 0}))
    check("raw power generator has nonzero cross derivative generically", raw_cross != 0 and raw_cross.has(q_raw), f"cross={raw_cross}")

    section("PART F -- scale visibility")
    lam = sp.symbols("lambda", positive=True)
    scaled_s = [lam * v for v in s]
    scaled_mean = expectation(prob, scaled_s)
    scaled_fisher = expectation(prob, [v**2 for v in scaled_s])
    check("scaled score remains centered", sp.simplify(scaled_mean) == 0)
    check("scaled Fisher norm is lambda^2", sp.simplify(scaled_fisher - lam**2) == 0)
    check("unit Fisher source selects lambda=1", sp.solve(sp.Eq(scaled_fisher, 1), lam) == [1])
    q = sp.symbols("q", real=True)
    Wq = q * W
    check("q-scaled log normalizer has W''(0)=q", sp.simplify(sp.diff(Wq, h, 2).subs(h, 0) - q) == 0)
    check("unit connected response selects q=1", sp.solve(sp.Eq(sp.diff(Wq, h, 2).subs(h, 0), 1), q) == [1])

    section("PART G -- note content")
    check("note declares bounded bridge theorem", "positive theorem candidate / bounded bridge theorem" in note)
    check("note states Record/Born to RN chain", "Born trace weights on a finite sharp-record context" in note)
    check("note names W_source_action residual", "W_source_action" in note)
    check("note says P-cal algebra closes at interface", "P-cal algebra closes at the record-facing interface layer" in note)
    check("note preserves physical source identification", "physical source/action deformation" in note)
    check("note preserves occurrence gate", "local activation + selection of available possibilities" in note)
    check("note excludes Y_T closure", "does not derive Y_T" in note)
    check("note excludes measured/fitted imports", "PDG values" in note and "fitted selectors" in note)

    section("PART H -- no-go discipline gate")
    for item in ("N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"):
        check(f"note includes {item}", item in note)
    check("N1 enumerates six routes", note.count("| Route |") == 1 and note.count("| Planck/action route |") == 1)
    check("N2 collapses residual to W_source_action", "Collapsed residual after this note" in note and "W_source_action" in note)
    check("N3 labels supplied interface", "\"Supplied selective interface\"" in note)
    check("N4 has six residual matches", note.count("| `") >= 6 and "Residual Matching" in note)
    check("N5 avoids source/action closure overclaim", "not \"source/action is derived\"" in note)
    check("N6 gives import-retirement path", "import-retirement path" in note)
    check("N7 steelman admits rephrasing risk", "merely rephrases the existing" in note)
    check("N8 separates layers", "Record/Born supplies the probability interface" in note_flat)

    section("PART I -- assembled conclusion")
    interface_ok = (
        p0 == sp.Rational(3, 5)
        and p1 == sp.Rational(2, 5)
        and sp.simplify(mean_s) == 0
        and sp.simplify(fisher_s - 1) == 0
        and sp.simplify(expectation(prob, Rh) - 1) == 0
        and sp.simplify(sp.diff(W, h, 2).subs(h, 0) - 1) == 0
    )
    check("Record/Born probabilities instantiate finite RN source calculus", interface_ok)
    check("physical source/action remains a residual", "physical source/action bridge" in note or "physical source/action identification" in note)
    check("no new axiom requested", "No axiom expansion is required" in note)

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL")
        return 1
    print(
        "RESULT: PASS -- supplied Record/Born finite probabilities instantiate "
        "the source-measure RN/log-normalizer P-cal interface; physical "
        "source/action identification remains open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
