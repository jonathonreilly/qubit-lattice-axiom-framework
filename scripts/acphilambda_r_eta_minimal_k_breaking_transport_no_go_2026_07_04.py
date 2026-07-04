#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "ACPHILAMBDA_R_ETA_MINIMAL_K_BREAKING_TRANSPORT_NO_GO_NOTE_2026-07-04.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = DOCS / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = DOCS / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = DOCS / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
TRANSPORT = DOCS / "ACPHILAMBDA_CYCLE_FLUX_TRANSPORT_FACE_INVENTORY_2026-07-01.md"
HOLONOMY = DOCS / "ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01.md"
REAL_LOCUS = DOCS / "ACPHILAMBDA_REAL_HOLONOMY_LOCUS_IDENTITY_2026-07-01.md"
DEFECT = DOCS / "ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01.md"
K_EVEN = DOCS / "ACPHILAMBDA_K_EVEN_REGISTRATION_CORRECTION_REGISTERED_PATTERN_2026-07-02.md"
BLOCK17 = DOCS / "ACPHILAMBDA_R_ETA_CURRENT_SURFACE_READOUT_IDENTIFICATION_NO_GO_NOTE_2026-07-04.md"
BLOCK18 = DOCS / "ACPHILAMBDA_R_ETA_TRANSPORT_EQUALITY_STRETCH_NO_GO_NOTE_2026-07-04.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"[PASS] {label}")
    else:
        FAIL += 1
        suffix = f" :: {detail}" if detail else ""
        print(f"[FAIL] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def weighted_triangle_laplacian(x: sp.Expr, y: sp.Expr, z: sp.Expr) -> sp.Matrix:
    """C3 ring conductances x=(0,1), y=(1,2), z=(2,0)."""
    return sp.Matrix(
        [
            [x + z, -x, -z],
            [-x, x + y, -y],
            [-z, -y, y + z],
        ]
    )


def main() -> int:
    print("AC_phi_lambda R-eta minimal K-breaking transport no-go verifier")

    note = read(NOTE)
    note_flat = flat(note)
    tier = json.loads(read(TIER_A))
    ledger = json.loads(read(LEDGER))["rows"]
    minimal = read(MINIMAL)
    scale = read(SCALE)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    transport = read(TRANSPORT)
    holonomy = read(HOLONOMY)
    real_locus = read(REAL_LOCUS)
    defect = read(DEFECT)
    k_even = read(K_EVEN)
    block17 = read(BLOCK17)
    block18 = read(BLOCK18)

    section("A. source presence and scope firewalls")
    for path in [
        NOTE,
        TIER_A,
        LEDGER,
        MINIMAL,
        SCALE,
        KINETIC,
        REALIZED,
        TRANSPORT,
        HOLONOMY,
        REAL_LOCUS,
        DEFECT,
        K_EVEN,
        BLOCK17,
        BLOCK18,
    ]:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())

    check("note declares Type no_go", "**Type:** no_go" in note)
    check("note declares Claim type no_go", "**Claim type:** no_go" in note)
    check("note declares K-breaking route scope", "minimal K-breaking / inhomogeneous transport route" in note_flat)
    check("note declares independent audit boundary", "independent audit lane only" in note)
    check(
        "note says no registry/axiom/primitive edit",
        "does not edit any Tier-A registry, axiom, primitive, audit verdict, or publication surface" in note_flat,
    )
    check("note says AC not retired", "AC_phi_lambda is not retired." in note)
    check("note says R-eta not removed", "R-eta is not derived, refuted, re-graded, or removed from Tier-A" in note)
    for banned in [
        "AC_phi_lambda is retired",
        "R-eta is retired",
        "R-eta is derived",
        "Phi = Tr L_3^+ is derived",
        "we remove R-eta",
        "registry is edited",
        "audit verdict is set",
    ]:
        check(f"banned overclaim absent: {banned}", banned not in note)

    section("B. Tier-A and current-source state")
    ac = tier["derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]
    check("Tier-A genuine admitted input count remains two", tier["genuine_admitted_input_count"] == 2)
    check(
        "AC minimum decomposition remains two atoms",
        ac["minimum_decomposition"] == ["reading_occupancy_selection", "delta_readout_identification_R_eta"],
        ac["minimum_decomposition"],
    )
    check("AC statement keeps R-eta", "R-eta" in ac["statement"])
    check("AC statement keeps conditional magnitude", "conditional on R-eta" in ac["statement"])
    for claim_id, expected_type in [
        ("acphilambda_cycle_flux_transport_face_inventory_2026-07-01", "bounded_theorem"),
        ("acphilambda_registrable_cycle_holonomy_normal_form_2026-07-01", "bounded_theorem"),
        ("acphilambda_real_holonomy_locus_identity_2026-07-01", "bounded_theorem"),
        ("acphilambda_defect_identity_unit_rescale_obstruction_2026-07-01", "bounded_theorem"),
        ("acphilambda_k_even_registration_correction_registered_pattern_2026-07-02", "bounded_theorem"),
        ("acphilambda_r_eta_current_surface_readout_identification_no_go_note_2026-07-04", "no_go"),
        ("acphilambda_r_eta_transport_equality_stretch_no_go_note_2026-07-04", "no_go"),
    ]:
        row = ledger.get(claim_id)
        check(f"ledger row exists: {claim_id}", isinstance(row, dict))
        if isinstance(row, dict):
            check(f"{claim_id} claim_type", row.get("claim_type") == expected_type, row.get("claim_type"))
            check(f"{claim_id} not effective retained", row.get("effective_status") != "retained", row.get("effective_status"))
            check(f"{claim_id} has note path", bool(row.get("note_path")), row.get("note_path"))

    section("C. premise-boundary checks")
    minimal_flat = flat(minimal)
    for phrase in [
        "formation rules",
        "with what weight",
        "or at what rate",
        "source/action",
        "physical-observable identification",
        "`K`/CPT structure",
    ]:
        check(f"minimal axioms keep {phrase} downstream", phrase in minimal_flat)
    check("scale primitive supplies no selector/readout bridge", "no mass ratio, coupling, mixing angle, phase, selector, readout bridge, or empirical fit" in flat(scale))
    check("kinetic primitive supplies no selector/readout bridge", "no mass ratio, coupling, mixing angle, phase, selector, readout bridge, or empirical fit" in flat(kinetic))
    check("realized-state primitive supplies no value/selection", "no state, averaging over alternatives, measure, weighting, probability rule" in flat(realized) and "or value is supplied" in flat(realized))
    check("transport source says equation remains wall", "The equation itself remains the wall" in transport)
    check("transport source says no flux equality derivation", "does not derive flux = return amplitude" in transport)
    check("holonomy source says no Phi derivation", "No derivation is supplied for `Phi = 2/3`" in holonomy)
    check("real locus says K-breaking registered content needed", "must supply K-reality-breaking registered content" in real_locus)
    check("defect source requires rescale-breaking clause", "rescale-breaking" in defect)
    check("K-even source keeps live licensed self-consistency map", "licensed registered self-consistency map" in k_even)
    check("block17 keeps R-eta live", "AC_phi_lambda sub-admission (ii) remains live" in block17)
    check("block18 says transport route remains typed wall", "typed wall, not a derivation" in block18)

    section("D. weighted C3 edge transport")
    x, y, z = sp.symbols("x y z", positive=True)
    L_xyz = weighted_triangle_laplacian(x, y, z)
    trace_L = sp.trace(L_xyz)
    principal_minor_sum = (
        L_xyz.extract([0, 1], [0, 1]).det()
        + L_xyz.extract([0, 2], [0, 2]).det()
        + L_xyz.extract([1, 2], [1, 2]).det()
    )
    check("weighted Laplacian row sums vanish", all(sp.simplify(sum(L_xyz[i, j] for j in range(3))) == 0 for i in range(3)))
    check("trace weighted Laplacian is 2(x+y+z)", sp.simplify(trace_L - 2 * (x + y + z)) == 0)
    check("principal minor sum is 3(xy+xz+yz)", sp.simplify(principal_minor_sum - 3 * (x * y + x * z + y * z)) == 0)
    T_edge = sp.simplify(2 * (x + y + z) / (3 * (x * y + x * z + y * z)))
    check("edge trace formula records exact return trace", sp.simplify(T_edge - 2 * (x + y + z) / (3 * (x * y + x * z + y * z))) == 0)
    check("homogeneous edge trace is 2/3", sp.simplify(T_edge.subs({x: 1, y: 1, z: 1}) - sp.Rational(2, 3)) == 0)
    check("inhomogeneous numeric sample misses target", sp.simplify(T_edge.subs({x: 2, y: 1, z: 1}) - sp.Rational(2, 3)) != 0)
    L_sample = weighted_triangle_laplacian(sp.Rational(2), sp.Rational(1), sp.Rational(1))
    check("sample pinv trace matches formula", sp.simplify(sp.trace(L_sample.pinv()) - T_edge.subs({x: 2, y: 1, z: 1})) == 0)
    X, Y = sp.symbols("X Y", real=True)
    Z = 3 - X - Y
    pair_sum_norm = sp.expand(X * Y + Y * Z + Z * X)
    square_gap = sp.expand(((X - Y) ** 2 + (Y - Z) ** 2 + (Z - X) ** 2) / 6)
    check("normalized edge gap identity", sp.simplify(3 - pair_sum_norm - square_gap) == 0)
    check("normalized target iff pair sum is 3", sp.solve(sp.Eq(2 / sp.Symbol("P"), sp.Rational(2, 3)), sp.Symbol("P")) == [3])
    check("normalized equality requires zero square gap", sp.solve(sp.Eq(square_gap, 0), X) != [])
    check("note states homogeneous-only edge hit", "occurs only at `x=y=z=1`" in note)

    section("E. one-edge defect family")
    s = sp.symbols("s", real=True)
    T_one_edge = sp.factor(T_edge.subs({x: 1 + s, y: 1, z: 1}))
    check("one-edge formula", sp.simplify(T_one_edge - 2 * (s + 3) / (3 * (2 * s + 3))) == 0, T_one_edge)
    check("one-edge target residual has factor s", sp.factor(T_one_edge - sp.Rational(2, 3)) == -2 * s / (3 * (2 * s + 3)) or sp.simplify(T_one_edge - sp.Rational(2, 3) + 2 * s / (3 * (2 * s + 3))) == 0)
    check("one-edge equation target gives zero defect", sp.solve(sp.Eq(T_one_edge, sp.Rational(2, 3)), s) == [0])
    check("one-edge derivative is negative for allowed positive side", sp.factor(sp.diff(T_one_edge, s)) == -2 / (2 * s + 3) ** 2)
    check("one-edge positive sample below target", T_one_edge.subs(s, 1) < sp.Rational(2, 3))
    check("one-edge note says s=0 only", "has only the non-defect solution `s=0`" in note)

    section("F. one-site source/mass defect")
    m = sp.symbols("m", positive=True)
    L3 = weighted_triangle_laplacian(1, 1, 1)
    P0 = sp.diag(1, 0, 0)
    Lm = L3 + m * P0
    trace_inverse = sp.factor(sp.trace(Lm.inv()))
    check("mass defect determinant is 3m", sp.factor(Lm.det()) == 3 * m, sp.factor(Lm.det()))
    check("mass defect inverse trace formula", trace_inverse == (4 * m + 9) / (3 * m), trace_inverse)
    check("mass defect inverse trace decomposes", sp.simplify(trace_inverse - (3 / m + sp.Rational(4, 3))) == 0)
    finite_part = sp.limit(trace_inverse - 3 / m, m, 0, dir="+")
    check("mass defect finite part is 4/3", finite_part == sp.Rational(4, 3), finite_part)
    check("finite part is not target", finite_part != sp.Rational(2, 3))
    check("positive full trace cannot hit target", sp.solve(sp.Eq(trace_inverse, sp.Rational(2, 3)), m) == [])
    check("positive sample full trace above 4/3", trace_inverse.subs(m, 9) > sp.Rational(4, 3))
    check("mass note states finite part miss", "finite part is `4/3`, not" in note)

    section("G. mixed selector and current-interface checks")
    alpha = sp.symbols("alpha", real=True)
    mixed = alpha * sp.Rational(2, 3) + (1 - alpha) * sp.Rational(4, 3)
    check("mixed homogeneous/source selector target requires alpha=1", sp.solve(sp.Eq(mixed, sp.Rational(2, 3)), alpha) == [1])
    check("mixed selector alpha=1 discards source contribution", sp.simplify(mixed.subs(alpha, 1) - sp.Rational(2, 3)) == 0)
    check("mixed selector alpha=0 is source finite part", mixed.subs(alpha, 0) == sp.Rational(4, 3))
    check("note says mixed route must derive coefficient", "must derive its coefficient" in note)
    check("note says Record additivity does not select surface", "after a readout surface is selected" in note)
    check("note says records form does not choose rate/weight", "with what weight, or at what rate" in note)

    section("H. fan-out, theorem, and no-go discipline")
    for heading in [
        "Frame 1: normalized positive edge inhomogeneity",
        "Frame 2: one-edge defect without conductance renormalization",
        "Frame 3: one-site source/mass defect",
        "Frame 4: affine or mixed transport selectors",
        "Frame 5: Record and realized-state interfaces",
    ]:
        check(f"fan-out heading present: {heading}", heading in note)
    for phrase in [
        "the implication",
        "is invalid",
        "minimal positive K-breaking transport does not retire R-eta",
        "successful theorem must either derive a non-minimal physical transport law",
        "Direct R-eta readout-license theorem",
        "Non-minimal transport theorem",
        "Theta residuals",
    ]:
        check(f"note contains theorem/queue phrase: {phrase}", phrase in note_flat)
    for label in [f"N{i}" for i in range(1, 9)]:
        check(f"no-go gate has {label}", f"**{label}" in note)
    check("N2 keeps collapsed wall", "W_cycle_holonomy_value == W_defect_identity_unit == R-eta (ii)" in note)
    check("N3 forbids source/action bridge", "no source/action bridge" in note)
    check("N5 says not terminal", "not a terminal no-go against all possible non-minimal transport physics" in note_flat)
    check("N7 steelmans richer operator", "richer operator" in note)
    check("expected total present", "TOTAL: PASS=133 FAIL=0" in note)

    section("I. final summary")
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
