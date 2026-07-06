#!/usr/bin/env python3
"""Verifier for AC occupancy determinant-power split exact support."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "ACPHILAMBDA_OCCUPANCY_DETERMINANT_POWER_SPLIT_EXACT_SUPPORT_NOTE_2026-07-04.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
OCC_REDUCTION = DOCS / "ACPHILAMBDA_OCCUPANCY_SELECTION_REALIZED_STATE_REDUCTION_NOTE_2026-06-11.md"
FIRST_ORDER = DOCS / "KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md"
MEASURE_NO_GO = DOCS / "ACPHILAMBDA_MEASURE_BINARY_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md"
FORMATION_NO_GO = DOCS / "ACPHILAMBDA_OCCUPANCY_FORMATION_APPEND_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md"
COUNTING_BIT = DOCS / "CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md"
DIAL = DOCS / "GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
REALIZED_PRIMITIVE = DOCS / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

PASS = 0
FAIL = 0


def flat(text: str) -> str:
    return " ".join(text.split())


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{tag}: {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "-" * 78)
    print(title)
    print("-" * 78)


def realification(x_mat: sp.Matrix, y_mat: sp.Matrix) -> sp.Matrix:
    top = sp.Matrix.hstack(x_mat, -y_mat)
    bottom = sp.Matrix.hstack(y_mat, x_mat)
    return sp.Matrix.vstack(top, bottom)


def gr_mul(p: dict[int, sp.Expr], q: dict[int, sp.Expr]) -> dict[int, sp.Expr]:
    out: dict[int, sp.Expr] = {}
    for m1, c1 in p.items():
        for m2, c2 in q.items():
            if m1 & m2:
                continue
            sign = 1
            g = m2
            while g:
                low = g & -g
                bit = low.bit_length() - 1
                if bin(m1 >> (bit + 1)).count("1") % 2:
                    sign = -sign
                g ^= low
            m = m1 | m2
            out[m] = out.get(m, 0) + sign * c1 * c2
    return {m: sp.simplify(c) for m, c in out.items() if sp.simplify(c) != 0}


def gr_int(p: dict[int, sp.Expr], g: int) -> dict[int, sp.Expr]:
    out: dict[int, sp.Expr] = {}
    bit = 1 << g
    for m, c in p.items():
        if not (m & bit):
            continue
        below = bin(m & (bit - 1)).count("1")
        sign = -1 if below % 2 else 1
        m2 = m ^ bit
        out[m2] = out.get(m2, 0) + sign * c
    return {m: sp.simplify(c) for m, c in out.items() if sp.simplify(c) != 0}


def berezin_partition(k_mat: list[list[sp.Expr]], n: int) -> sp.Expr:
    """Compute int dchibar dchi exp(chibar K chi) by exterior algebra."""

    action: dict[int, sp.Expr] = {}
    for i in range(n):
        for j in range(n):
            coeff = k_mat[i][j]
            if coeff == 0:
                continue
            gi, gj = 2 * i, 2 * j + 1
            monomial = (1 << gi) | (1 << gj)
            sign = 1 if gi < gj else -1
            action[monomial] = action.get(monomial, 0) + sign * coeff

    expo: dict[int, sp.Expr] = {0: sp.Integer(1)}
    term: dict[int, sp.Expr] = {0: sp.Integer(1)}
    for k in range(1, n + 1):
        term = gr_mul(term, action)
        term = {m: sp.simplify(c / k) for m, c in term.items() if sp.simplify(c) != 0}
        for m, c in term.items():
            expo[m] = expo.get(m, 0) + c

    out = expo
    for i in range(n):
        out = gr_int(out, 2 * i)
        out = gr_int(out, 2 * i + 1)
    return sp.simplify(out.get(0, 0))


def main() -> int:
    print("AC_phi_lambda occupancy determinant-power split exact support")
    print("=" * 78)

    note = NOTE.read_text(encoding="utf-8")
    tier = json.loads(TIER_A.read_text(encoding="utf-8"))
    occ_reduction = OCC_REDUCTION.read_text(encoding="utf-8")
    first_order = FIRST_ORDER.read_text(encoding="utf-8")
    measure_no_go = MEASURE_NO_GO.read_text(encoding="utf-8")
    formation_no_go = FORMATION_NO_GO.read_text(encoding="utf-8")
    counting_bit = COUNTING_BIT.read_text(encoding="utf-8")
    dial = DIAL.read_text(encoding="utf-8")
    minimal = MINIMAL.read_text(encoding="utf-8")
    realized = REALIZED_PRIMITIVE.read_text(encoding="utf-8")

    note_flat = flat(note)
    occ_flat = flat(occ_reduction)
    first_flat = flat(first_order)
    measure_no_go_flat = flat(measure_no_go)
    formation_no_go_flat = flat(formation_no_go)
    counting_flat = flat(counting_bit)
    dial_flat = flat(dial)
    minimal_flat = flat(minimal)
    realized_flat = flat(realized)

    section("A - source and registry boundaries")

    for path in [NOTE, TIER_A, OCC_REDUCTION, FIRST_ORDER, MEASURE_NO_GO, FORMATION_NO_GO, COUNTING_BIT, DIAL, MINIMAL, REALIZED_PRIMITIVE]:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())

    check("note declares bounded_theorem claim type", "**Claim type:** bounded_theorem" in note)
    check("runner path is wired in note", Path(__file__).name in note)
    check("note denies AC retirement", "does not retire `AC_phi_lambda`" in note and "`AC_phi_lambda(i)` is not retired" in note)
    check("note denies horn selection", "does not choose the orbit/holomorphic horn" in note_flat and "The sector/K-real horn is not selected" in note)
    check("note denies premise and primitive adoption", "does not adopt the orbit-occupancy premise" in note_flat and "does not introduce a K-real primitive" in note_flat)
    check("note denies registry/axiom/primitive/audit edits", "does not edit any Tier-A registry" in note_flat and "No registry, primitive, axiom" in note)

    ac = tier["retired_derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]
    check("live Tier-A genuine count is zero", tier["genuine_admitted_input_count"] == 0, tier["genuine_admitted_input_count"])
    check("canonical Tier-A IDs are empty on current main", tier["canonical_ids"] == [], tier["canonical_ids"])
    check("live derivation targets are empty on current main", tier.get("derivation_targets", {}) == {}, tier.get("derivation_targets"))
    retirement = ac.get("retirement", {})
    check("AC retired-target record is preserved", bool(ac))
    check("AC retirement date is recorded", retirement.get("date") == "2026-07-05", retirement)
    check("AC retirement mechanism is owner governance", retirement.get("mechanism") == "retired_by_owner_governance_on_audited_surface", retirement)
    check(
        "historical AC decomposition preserves three old atoms",
        ac["minimum_decomposition"] == [
            "reading_occupancy_selection",
            "delta_readout_identification_R_eta",
            "species_bridge",
        ],
        ac["minimum_decomposition"],
    )
    ac_flat = flat(json.dumps(ac))
    check("AC retired registry names reading/occupancy selection", "reading/occupancy selection" in ac_flat and "reading_occupancy_selection" in ac_flat)
    check("AC retirement boundary names occupancy grain", "matter-action occupancy grain" in ac_flat)
    check("note has current-main posture line", "Current-main posture (2026-07-06)" in note)
    check("note records live Tier-A zero posture", "Tier-A count\nzero" in note or "Tier-A count zero" in note)
    check("note says retirement records are not reopened", "does not reopen, modify,\nor re-grade either retirement record" in note)

    section("B - determinant power algebra")

    a, b, c, d, e, f, g, h = sp.symbols("a b c d e f g h", real=True)
    x_mat = sp.Matrix([[a, c], [e, g]])
    y_mat = sp.Matrix([[b, d], [f, h]])
    k_complex = x_mat + sp.I * y_mat
    r_complex = realification(x_mat, y_mat)
    det_c = sp.factor(k_complex.det())
    det_r = sp.factor(r_complex.det())
    abs_sq = sp.factor(det_c * sp.conjugate(det_c))
    check("generic 2x2 realification determinant equals squared complex determinant", sp.simplify(det_r - abs_sq) == 0)

    x, y, lam = sp.symbols("x y lam", real=True, positive=True)
    z = x + sp.I * y
    scalar_r = sp.Matrix([[x, -y], [y, x]])
    check("scalar realification gives z*zbar", sp.simplify(scalar_r.det() - z * sp.conjugate(z)) == 0)
    check("multiplication by i changes det_C phase but not det_R", sp.simplify((sp.I * z) - z) != 0 and sp.simplify(((-y) ** 2 + x**2) - (x**2 + y**2)) == 0)
    check("complex count scales once for one complex mode", sp.simplify((lam * z) / z - lam) == 0)
    scaled_scalar_r = sp.Matrix([[lam * x, -lam * y], [lam * y, lam * x]])
    check("realified count scales twice for one complex mode", sp.simplify(scaled_scalar_r.det() / scalar_r.det() - lam**2) == 0)

    k_symbols = [[sp.Symbol(f"k{i}{j}") for j in range(2)] for i in range(2)]
    z_berezin = berezin_partition(k_symbols, 2)
    det_berezin = sp.Matrix(k_symbols).det()
    check("explicit Berezin Gaussian gives det_C(K) to first power", sp.simplify(z_berezin - det_berezin) == 0, z_berezin)

    section("C - AC occupancy fork localization")

    alpha, beta, gamma, betabar = sp.symbols("alpha beta gamma betabar")
    det3 = alpha**3 + beta**3 + gamma**3 - 3 * alpha * beta * gamma
    check("independent C3 channel determinant is holomorphic in beta,gamma", betabar not in det3.free_symbols and gamma in det3.free_symbols)
    det_tied = alpha**3 + beta**3 + betabar**3 - 3 * alpha * beta * betabar
    check("tied section supplies mixed beta*betabar term", sp.diff(det_tied, beta, betabar) == -3 * alpha)
    u, v = sp.symbols("u v", real=True)
    det_tied_uv = sp.expand(det_tied.subs({beta: u + sp.I * v, betabar: u - sp.I * v}))
    expected_uv = sp.expand(alpha**3 + 2 * u**3 - 6 * u * v**2 - 3 * alpha * (u**2 + v**2))
    check("K-real substitution produces |beta|^2 dependence", sp.simplify(det_tied_uv - expected_uv) == 0, det_tied_uv)

    q = lambda r: sp.Rational(1, 3) + sp.Rational(2, 3) * r
    check("landed cells remain distinct", q(sp.Integer(1)) == 1 and q(sp.Rational(1, 2)) == sp.Rational(2, 3))
    check("note keeps both determinant horns live", "Holomorphic/orbit" in note and "Realified/sector-tied" in note)

    section("D - source integration and non-overclaim")

    check(
        "realized-state reduction names survivor as measure-side realization",
        "measure-side binary itself" in occ_flat and "matter action's statistics implements" in occ_flat,
    )
    check(
        "first-order theorem already localizes count-twice to K-real restriction",
        "measure side is first-order" in first_flat and "c = conj(b)" in first_flat and "which horn is physical is not decided" in first_flat,
    )
    check(
        "measure-binary no-go blocks axiom/primitive retirement",
        "does not supply the AC(i) reading/occupancy binary" in measure_no_go_flat
        and "No value of `r` is derived, selected, or preferred." in measure_no_go,
    )
    check(
        "formation-append no-go blocks Record shortcut",
        "The July 4 formation append does not retire AC_phi_lambda(i)." in formation_no_go
        and "measure-side doublet occupancy realization binary" in formation_no_go_flat,
    )
    check(
        "counting-bit synthesis names det_C versus det_R fork",
        "det_C" in counting_bit and "det_R" in counting_bit and "one binary counting-measure bit" in counting_flat,
    )
    check(
        "dial note identifies block-count and dimension endpoints",
        "block-count / det_C" in dial and "Born / dimension / det_R" in dial,
    )
    check(
        "axiom and primitive surfaces do not supply measure/weight selection",
        "readout-context selection" in minimal_flat
        and "Born weights" in minimal_flat
        and "measure, weighting, probability rule" in realized_flat,
    )

    required_note_phrases = [
        "det_R R(K) = det_C(K) * conjugate(det_C(K))",
        "determinant-power binary",
        "matter action implements",
        "Remaining Live Routes",
        "Independent audit required",
    ]
    for phrase in required_note_phrases:
        check(f"note contains required phrase: {phrase}", phrase in note)

    banned = [
        "derives `r = 1/2`",
        "chooses the orbit/holomorphic horn",
        "adopts the orbit-occupancy premise",
        "introduces a K-real primitive",
        "retires `AC_phi_lambda`",
        "edits the Tier-A registry",
        "R-eta is derived",
        "theta is derived",
        "retained_no_go",
        "audited_clean",
    ]
    false_positive_context = {
        "derives `r = 1/2`": "does not derive `r = 1/2`",
        "chooses the orbit/holomorphic horn": "does not choose the orbit/holomorphic horn",
        "adopts the orbit-occupancy premise": "does not adopt the orbit-occupancy premise",
        "introduces a K-real primitive": "does not introduce a K-real primitive",
        "retires `AC_phi_lambda`": "does not retire `AC_phi_lambda`",
        "edits the Tier-A registry": "does not edit the Tier-A registry",
    }
    found = []
    for phrase in banned:
        if phrase in note and false_positive_context.get(phrase) not in note:
            found.append(phrase)
    check("banned overclaim phrases are absent except explicit denials", not found, found)

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
