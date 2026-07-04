#!/usr/bin/env python3
"""Verifier for AC_phi_lambda first-order determinant retirement readiness."""

from __future__ import annotations

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "ACPHILAMBDA_FIRST_ORDER_DETERMINANT_RETIREMENT_READINESS_NO_GO_NOTE_2026-07-04.md"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
REALIZED_REDUCTION = DOCS / "ACPHILAMBDA_OCCUPANCY_SELECTION_REALIZED_STATE_REDUCTION_NOTE_2026-06-11.md"
FIRST_ORDER = DOCS / "KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md"
ORBIT_OCC = DOCS / "KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md"
KREAL_NO_GO = DOCS / "KREALITY_SHARED_PHYSICALIZATION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
REALIZED_PRIMITIVE = DOCS / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

PASS = 0
FAIL = 0


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
    print(f"{tag}: {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "-" * 78)
    print(title)
    print("-" * 78)


def main() -> int:
    print("AC_phi_lambda first-order determinant retirement-readiness no-go")
    print("=" * 78)

    note = NOTE.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")
    realized_reduction = REALIZED_REDUCTION.read_text(encoding="utf-8")
    first_order = FIRST_ORDER.read_text(encoding="utf-8")
    orbit_occ = ORBIT_OCC.read_text(encoding="utf-8")
    kreal_no_go = KREAL_NO_GO.read_text(encoding="utf-8")
    axioms = AXIOMS.read_text(encoding="utf-8")
    realized_primitive = REALIZED_PRIMITIVE.read_text(encoding="utf-8")

    note_flat = flat(note)
    registry_flat = flat(registry)
    realized_reduction_flat = flat(realized_reduction)
    first_order_flat = flat(first_order)
    orbit_occ_flat = flat(orbit_occ)
    kreal_no_go_flat = flat(kreal_no_go)
    axioms_flat = flat(axioms)
    realized_primitive_flat = flat(realized_primitive)

    section("A - source and registry firewalls")

    check("note declares no-go claim type", "**Claim type:** no_go" in note)
    check("note denies AC retirement and registry edits", "does not retire `AC_phi_lambda`" in note_flat and "does not edit any Tier-A registry" in note_flat)
    check("note denies r derivation and orbit premise adoption", "does not derive `r = 1/2`" in note_flat and "does not choose the orbit-occupancy horn" in note_flat)
    check("note keeps future routes open", "future measure-side dynamics" in note_flat and "owner governance routes are impossible" in note_flat)
    check("runner path is wired in note", Path(__file__).name in note)

    section("B - existing sources still leave the measure-side horn live")

    check(
        "registry has current AC(i) residual",
        "measure-side doublet occupancy realization binary" in registry_flat
        and "registered realized-state data" in registry_flat
        and "not a Tier-A derivation target" in registry_flat,
    )
    check(
        "realized-state reduction names measure-side survivor",
        "measure-side binary itself" in realized_reduction_flat
        and "which grain" in realized_reduction_flat
        and "matter action's statistics implements" in realized_reduction_flat
        and "Both grain models satisfy every checked constraint" in realized_reduction,
    )
    check(
        "first-order theorem claims first-order measure but not r retirement",
        "measure side is first-order" in first_order_flat
        and "which horn is physical is not decided" in first_order_flat
        and "Not** a derivation of `r = 1/2`" in first_order,
    )
    check(
        "first-order theorem uses declared probe coupling",
        "declared probe coupling" in first_order_flat
        and "Not** a derivation of the generation Yukawa form" in first_order,
    )
    check(
        "orbit-occupancy note proposes but does not adopt premise",
        "proposal NOT adopted" in orbit_occ_flat
        and "Not claimed" in orbit_occ
        and "remains proposed, not adopted" in orbit_occ_flat,
    )
    check(
        "block23 K-real no-go blocks algebra-as-physical-selector shortcut",
        "K-real monitor" in kreal_no_go_flat
        and "not a retired tier-a residual" in kreal_no_go_flat.lower(),
    )
    check(
        "axiom/primitive hygiene supplies no measure or selection rule",
        "readout-context selection" in axioms_flat
        and "measure, weighting, probability rule" in realized_primitive_flat
        and "not a state-selection rule" in realized_primitive_flat,
    )

    section("C - finite determinant fork witness")

    a, b, c, bbar, x, y = sp.symbols("a b c bbar x y", real=True)
    det3 = a**3 + b**3 + c**3 - 3 * a * b * c
    check("det3 is holomorphic in independent b,c variables", bbar not in det3.free_symbols and c in det3.free_symbols)

    det_kreal = sp.expand(det3.subs({b: x + sp.I * y, c: x - sp.I * y}))
    expected_kreal = sp.expand(a**3 + 2 * x**3 - 6 * x * y**2 - 3 * a * (x**2 + y**2))
    check("K-real restriction c=conj(b) introduces |b|^2 count-twice term", sp.simplify(det_kreal - expected_kreal) == 0, str(det_kreal))
    check("K-real restricted determinant depends on x^2+y^2", sp.diff(det_kreal, y, 2) != 0 and sp.diff(det_kreal, x, 2) != 0)

    det_independent = det3.subs({a: sp.Integer(2), b: sp.Rational(1, 3), c: sp.Rational(5, 7)})
    det_kreal_num = det_kreal.subs({a: sp.Integer(2), x: sp.Rational(1, 3), y: sp.Rational(5, 7)})
    check("independent and K-real horns are distinct finite evaluations", sp.simplify(det_independent - det_kreal_num) != 0, f"ind={det_independent}; kreal={det_kreal_num}")

    # Treat b and bbar as independent Wirtinger variables on the K-real slice.
    det_wirtinger = a**3 + b**3 + bbar**3 - 3 * a * b * bbar
    check("Wirtinger mixed derivative localizes count-twice term", sp.diff(det_wirtinger, b, bbar) == -3 * a)

    r_sector = sp.Integer(1)
    r_orbit = sp.Rational(1, 2)
    q = lambda r: sp.Rational(1, 3) + sp.Rational(2, 3) * r
    check("sector and orbit horns map to distinct landed cells", q(r_sector) == 1 and q(r_orbit) == sp.Rational(2, 3))
    check("runner keeps both horn cells alive", "sector/K-real horn" in note and "orbit/holomorphic horn" in note)

    section("D - no-go assembly")

    check("note states invalid implication", "therefore AC_phi_lambda(i)'s measure-side realization binary is retired" in note)
    check("note names missing physical horn selection", "physical measure/readout theorem selecting the orbit/holomorphic horn" in note)
    check("note names declared-probe residual", "Physical coupling theorem" in note and "supplying the rotation-channel probe" in note)
    check("note leaves R-eta and theta untouched", "R-eta is untouched" in note and "Theta is untouched" in note)
    check("no-go discipline is complete", all(tag in note for tag in ("N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8")))
    banned = ["fully closes", "solves AC", "derives r = 1/2", "retires AC_phi_lambda", "adopts orbit-occupancy"]
    found = [phrase for phrase in banned if phrase in note]
    check("banned overclaim phrases are absent", not found, str(found))

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
