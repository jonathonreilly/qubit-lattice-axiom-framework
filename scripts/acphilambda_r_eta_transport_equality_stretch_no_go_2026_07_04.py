#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import re
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "ACPHILAMBDA_R_ETA_TRANSPORT_EQUALITY_STRETCH_NO_GO_NOTE_2026-07-04.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = DOCS / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
REALIZED = DOCS / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
TRANSPORT = DOCS / "ACPHILAMBDA_CYCLE_FLUX_TRANSPORT_FACE_INVENTORY_2026-07-01.md"
HOLONOMY = DOCS / "ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01.md"
BLOCK17 = DOCS / "ACPHILAMBDA_R_ETA_CURRENT_SURFACE_READOUT_IDENTIFICATION_NO_GO_NOTE_2026-07-04.md"

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


def cycle_laplacian(n: int) -> sp.Matrix:
    matrix = sp.zeros(n)
    for i in range(n):
        matrix[i, i] = 2
        matrix[i, (i - 1) % n] = -1
        matrix[i, (i + 1) % n] = -1
    return matrix


def main() -> int:
    print("AC_phi_lambda R-eta transport-equality stretch no-go verifier")

    note = read(NOTE)
    note_flat = flat(note)
    minimal = read(MINIMAL)
    scale = read(SCALE)
    realized = read(REALIZED)
    transport = read(TRANSPORT)
    holonomy = read(HOLONOMY)
    block17 = read(BLOCK17)
    tier = json.loads(read(TIER_A))
    ledger = json.loads(read(LEDGER))["rows"]

    section("A. source presence and scope firewalls")
    for path in [NOTE, TIER_A, LEDGER, MINIMAL, SCALE, REALIZED, TRANSPORT, HOLONOMY, BLOCK17]:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())

    check("note declares Type no_go", "**Type:** no_go" in note)
    check("note declares Claim type no_go", "**Claim type:** no_go" in note)
    check("note declares stretch attempt", "first-principles stretch attempt" in note)
    check("note declares independent audit boundary", "independent audit lane only" in note)
    check("note says no registry/axiom/primitive edit", "does not edit any Tier-A registry, axiom, primitive, audit verdict, or publication surface" in note_flat)
    check("note says AC not retired", "AC_phi_lambda is not retired." in note)
    check("note says R-eta not removed", "R-eta is not derived, refuted, re-graded, or removed from Tier-A" in note)
    for banned in [
        "AC_phi_lambda is retired",
        "R-eta is retired",
        "R-eta is derived",
        "transport theorem is retained",
        "Phi = Tr L_3^+ is derived",
        "new primitive",
        "new axiom",
        "registry is edited",
    ]:
        check(f"banned overclaim absent: {banned}", banned not in note)

    section("B. Tier-A and source-row state")
    ac = tier["derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]
    check("Tier-A genuine admitted input count remains two", tier["genuine_admitted_input_count"] == 2)
    check(
        "AC minimum decomposition still contains R-eta",
        ac["minimum_decomposition"] == ["reading_occupancy_selection", "delta_readout_identification_R_eta"],
        ac["minimum_decomposition"],
    )
    check("AC statement keeps R-eta conditionality", "conditional on R-eta" in ac["statement"])
    for claim_id, expected_type in [
        ("acphilambda_cycle_flux_transport_face_inventory_2026-07-01", "bounded_theorem"),
        ("acphilambda_registrable_cycle_holonomy_normal_form_2026-07-01", "bounded_theorem"),
        ("acphilambda_r_eta_current_surface_readout_identification_no_go_note_2026-07-04", "no_go"),
    ]:
        row = ledger.get(claim_id)
        check(f"ledger row exists: {claim_id}", isinstance(row, dict))
        if isinstance(row, dict):
            check(f"{claim_id} claim_type", row.get("claim_type") == expected_type, row.get("claim_type"))
            check(f"{claim_id} not effective retained", row.get("effective_status") != "retained", row.get("effective_status"))
            check(f"{claim_id} has note path", bool(row.get("note_path")), row.get("note_path"))

    section("C. premise-boundary checks")
    for phrase in [
        "physical-observable identification",
        "context selection",
        "Born weights",
        "probability rules",
        "formation rules",
        "source/action",
    ]:
        check(f"minimal axioms keep {phrase} downstream", phrase in flat(minimal))
    check("scale primitive supplies no readout bridge", "no mass ratio, coupling, mixing angle, phase, selector, readout bridge, or empirical fit" in flat(scale))
    check("realized-state primitive supplies no value", "no state, averaging over alternatives, measure, weighting, probability rule" in flat(realized) and "or value is supplied" in flat(realized))
    check("transport source says equation remains wall", "The equation itself remains the wall" in transport)
    check("transport source says does not derive flux equality", "does not derive flux = return amplitude" in transport)
    check("holonomy source says no Phi derivation", "No derivation is supplied for `Phi = 2/3`" in holonomy)
    check("block17 leaves same-surface transport theorem live", "Same-surface transport theorem" in block17)

    section("D. unfluxed C3 Green trace")
    L3 = cycle_laplacian(3)
    L3_pinv = L3.pinv()
    check("C3 Laplacian exact matrix", L3 == sp.Matrix([[2, -1, -1], [-1, 2, -1], [-1, -1, 2]]), L3)
    check("C3 Laplacian spectrum {0,3,3}", sorted(L3.eigenvals().items(), key=lambda item: item[0]) == [(0, 1), (3, 2)], L3.eigenvals())
    check("Tr L3+ = 2/3", sp.trace(L3_pinv) == sp.Rational(2, 3), sp.trace(L3_pinv))
    check("diagonal L3+ entries are 2/9", all(L3_pinv[i, i] == sp.Rational(2, 9) for i in range(3)), L3_pinv)
    Phi = sp.symbols("Phi", real=True)
    unfluxed_trace = sp.Rational(2, 3)
    check("unfluxed trace has no holonomy variable", Phi not in unfluxed_trace.free_symbols)
    check("equating Phi to unfluxed trace is an extra equation", sp.solve(sp.Eq(Phi, unfluxed_trace), Phi) == [sp.Rational(2, 3)])

    section("E. fluxed inverse trace")
    flux_trace = sp.simplify(9 / (2 - 2 * sp.cos(Phi)))
    spectral_sum = sum(1 / (2 - 2 * sp.cos((Phi + 2 * sp.pi * m) / 3)) for m in range(3))
    check("fluxed spectral sum equals closed form", sp.simplify(sp.trigsimp(spectral_sum - flux_trace)) == 0)
    target = sp.Rational(2, 3)
    flux_at_target = flux_trace.subs(Phi, target)
    check("fluxed trace at target is not target", flux_at_target.equals(target) is False)
    check("fluxed trace at target is not unfluxed trace", flux_at_target.equals(unfluxed_trace) is False)
    check("numeric fluxed trace at target is far above 2/3", float(flux_at_target) > 20.0, float(flux_at_target))
    fixed_residual = sp.simplify(flux_at_target - target)
    check("target fails fixed-point equation Phi=T_flux(Phi)", fixed_residual.equals(0) is False)
    derivative = sp.diff(flux_trace, Phi)
    check("target fails stationarity", derivative.subs(Phi, target).equals(0) is False)
    check("derivative finite and negative at target", float(derivative.subs(Phi, target)) < 0)
    check("fluxed trace is even in Phi", sp.simplify(flux_trace.subs(Phi, -Phi) - flux_trace) == 0)
    check("fluxed trace is singular at zero", sp.limit(flux_trace, Phi, 0, dir="+") == sp.oo)

    section("F. singular finite part and regularization discriminator")
    finite_part = sp.limit(flux_trace - 9 / Phi**2, Phi, 0)
    check("fluxed inverse finite part is 3/4", finite_part == sp.Rational(3, 4), finite_part)
    check("finite part is not unfluxed pseudoinverse trace", finite_part != unfluxed_trace)
    series = sp.series(flux_trace, Phi, 0, 6)
    check("series contains 9/Phi^2", "9/Phi**2" in str(series))
    check("series contains 3/4", "3/4" in str(series))
    renorm_gap = sp.simplify(finite_part - unfluxed_trace)
    check("regularization gap is 1/12", renorm_gap == sp.Rational(1, 12), renorm_gap)

    section("G. five-frame fan-out and theorem text")
    for heading in [
        "Frame 1: unfluxed Green trace",
        "Frame 2: fluxed inverse trace",
        "Frame 3: singular-limit finite part",
        "Frame 4: variational or self-consistency selection",
        "Frame 5: Record and realized-state interfaces",
    ]:
        check(f"fan-out heading present: {heading}", heading in note)
    for phrase in [
        "Forbidden proof inputs",
        "current transport route remains a typed wall, not a derivation",
        "K-breaking transport theorem",
        "Direct readout-license theorem",
        "Coherence-event theorem",
        "Owner governance route",
    ]:
        check(f"note contains stretch phrase: {phrase}", phrase in note_flat)
    for label in [f"N{i}" for i in range(1, 9)]:
        check(f"no-go gate has {label}", f"**{label}" in note)
    check("N2 keeps collapsed wall", "W_cycle_holonomy_value == W_defect_identity_unit == R-eta (ii)" in note)
    check("N3 forbids physical readout bridge", "no physical readout bridge" in note)
    check("N5 states not terminal", "not a terminal no-go against all transport physics" in note_flat)
    check("N7 preserves transport support", "preserves that support" in note)

    section("H. final summary")
    check("runner expected total placeholder or final present", "TOTAL: PASS=" in note and "FAIL=0" in note)
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
