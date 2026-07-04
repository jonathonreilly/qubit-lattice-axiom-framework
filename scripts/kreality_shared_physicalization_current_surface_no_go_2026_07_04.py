#!/usr/bin/env python3
"""Verifier for the shared K-reality physicalization current-surface no-go."""

from __future__ import annotations

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "KREALITY_SHARED_PHYSICALIZATION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
REALIZED = DOCS / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
SPECIES = DOCS / "ACPHILAMBDA_SPECIES_BRIDGE_C3_GRADE_OWNER_RATIFICATION_RETIREMENT_NOTE_2026-07-04.md"
OLD_K = DOCS / "KREALITY_PREDICATE_ONE_SHARED_ATOM_ONE_CONSUMER_BOUNDED_NOTE_2026-06-12.md"
THETA_READY = DOCS / "THETA_MASS_DETERMINANT_BRIDGE_RETIREMENT_READINESS_NO_GO_NOTE_2026-07-04.md"

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


def same(a: sp.Matrix, b: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in (a - b))


def matrix_zero(a: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in a)


def section(title: str) -> None:
    print("\n" + "-" * 78)
    print(title)
    print("-" * 78)


def main() -> int:
    print("Shared K-reality physicalization current-surface no-go")
    print("=" * 78)

    note = NOTE.read_text(encoding="utf-8")
    axioms = AXIOMS.read_text(encoding="utf-8")
    realized = REALIZED.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")
    species = SPECIES.read_text(encoding="utf-8")
    old_k = OLD_K.read_text(encoding="utf-8")
    theta_ready = THETA_READY.read_text(encoding="utf-8")

    note_flat = flat(note)
    axioms_flat = flat(axioms)
    realized_flat = flat(realized)
    registry_flat = flat(registry)
    species_flat = flat(species)
    old_k_flat = flat(old_k)
    theta_flat = flat(theta_ready)

    section("A - source and governance firewalls")

    check("note declares no-go claim type", "**Claim type:** no_go" in note)
    check(
        "note has audit boundary and no registry edit",
        "independent audit lane only" in note_flat
        and "does not" in note_flat
        and "registry" in note_flat,
    )
    check("note refuses row retirement", "No row is retired" in note and "No Tier-A registry or machine registry is edited" in note)
    check("note keeps future routes open", "future dynamics, determinant-channel" in note_flat and "owner-governance routes are impossible" in note_flat)
    check("runner path is wired in note", Path(__file__).name in note)

    section("B - current hygiene does not supply physical K-real selection")

    check(
        "minimal axioms say laws privilege no states",
        "A law privileges no states" in axioms and "gives exactly one answer" in axioms,
    )
    check(
        "minimal axioms exclude K/CPT and readout-context selection from generic axiom content",
        "readout-context selection" in axioms_flat
        and "K`/CPT structure" in axioms_flat
        and "downstream readout-context content" in axioms_flat,
    )
    check(
        "minimal axioms exclude source/action and physical-observable identification",
        "source/action and physical-observable identification" in axioms,
    )
    check(
        "realized-state primitive is pointwise evaluation, not selection",
        "pointwise evaluation, not a state-selection rule" in realized_flat
        and "no state, averaging over alternatives" in realized_flat
        and "measure, weighting, probability rule" in realized_flat,
    )
    check(
        "realized-state primitive places r-like values in registration, not derivation output",
        "Per-sector registered weight patterns" in realized
        and "registered data, not derivation output" in realized,
    )
    check(
        "species bridge ratification is C3-grade naming only and leaves AC live",
        "C3-structural grade only" in species
        and "naming-class content" in species
        and "AC_phi_lambda itself does **not** retire" in species,
    )
    check(
        "registry carries exactly the surviving shared surfaces this note targets",
        "measure-side doublet occupancy realization binary" in registry_flat
        and "K-real structure" in registry_flat
        and "AC_φλ(i)" in registry_flat
        and "only after the determinant-readout/exhaustion bridge is closed" in registry_flat,
    )
    check(
        "old K-reality note explicitly did not derive or register the predicate",
        "not derived here" in old_k_flat
        and "not adopted here as a new axiom or primitive" in old_k_flat
        and "not registered here" in old_k_flat,
    )
    check(
        "block22 theta readiness no-go already separates shared K-real context from theta retirement",
        "shared C3 K-real structure" in theta_flat
        and "context, not automatic retirement" in theta_flat,
    )

    section("C - finite C3 monitor exhibit")

    I = sp.I
    sqrt3 = sp.sqrt(3)
    eye = sp.eye(3)
    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    C2 = C**2
    S = C + C2
    J = sp.simplify(I * (C - C2))
    a, x, y = sp.symbols("a x y", real=True)
    M_k = sp.simplify(a * eye + x * S)
    M_b = sp.simplify(a * eye + x * S + y * J)

    check("C is real order-three shift with C^T=C^2", same(C**3, eye) and same(C.T, C2) and same(sp.conjugate(C), C))
    check("S is real symmetric and C3-invariant", same(sp.conjugate(S), S) and same(S.T, S) and same(S * C, C * S))
    check("J is Hermitian, C3-invariant, and K-odd", same(J.conjugate().T, J) and same(J * C, C * J) and same(sp.conjugate(J), -J))
    check("K-real family M_K is real, Hermitian, C3-invariant", same(sp.conjugate(M_k), M_k) and same(M_k.conjugate().T, M_k) and same(M_k * C, C * M_k))
    check("K-broken family M_B remains Hermitian and C3-invariant", same(M_b.conjugate().T, M_b) and same(M_b * C, C * M_b))
    check("K-broken family is not K-real when y is nonzero", not matrix_zero(sp.simplify(sp.conjugate(M_b) - M_b)))

    omega = sp.Rational(-1, 2) + I * sqrt3 / 2
    P0 = sp.simplify((eye + C + C2) / 3)
    Pp = sp.simplify((eye + omega**2 * C + omega * C2) / 3)
    Pm = sp.simplify((eye + omega * C + omega**2 * C2) / 3)
    lam0 = sp.simplify((M_b * P0).trace() / P0.trace())
    lamp = sp.simplify((M_b * Pp).trace() / Pp.trace())
    lamm = sp.simplify((M_b * Pm).trace() / Pm.trace())
    check("K-real family leaves faithful pair degenerate", same(M_k * Pp, (a - x) * Pp) and same(M_k * Pm, (a - x) * Pm))
    check("K-broken family splits faithful characters", sp.simplify(lamp - lamm) != 0, f"lambda+={lamp}; lambda-={lamm}")
    check("singlet eigenvalue remains C3-classified", sp.simplify(lam0 - (a + 2 * x)) == 0)
    check("Hermitian K-broken determinant can be real, so determinant phase alone cannot select K-real", sp.im(sp.simplify(M_b.det())) == 0)

    witness = {a: sp.Rational(5, 3), x: sp.Rational(1, 7), y: sp.Rational(2, 11)}
    mk_num = M_k.subs(witness)
    mb_num = M_b.subs(witness)
    check("numeric K-real witness has two-sector faithful degeneracy", mk_num.eigenvals() == {sp.Rational(41, 21): 1, sp.Rational(32, 21): 2}, str(mk_num.eigenvals()))
    check("numeric K-broken witness has three distinct character eigenvalues", len(mb_num.eigenvals()) == 3, str(mb_num.eigenvals()))
    check("both finite monitor families are algebraically coherent", same(mk_num.conjugate().T, mk_num) and same(mb_num.conjugate().T, mb_num))

    section("D - no-go assembly")

    check(
        "note states the invalid implication explicitly",
        "therefore the physical C3 mass/readout monitor is K-real" in note,
    )
    check(
        "note names the missing K-real physicalization theorem",
        "physical mass/readout dynamics selects the K-real C3 monitor" in note,
    )
    check(
        "note names the K/CPT-site-basis bridge separately",
        "physical K/CPT predicate is exactly this site-basis" in note,
    )
    check(
        "note leaves AC(i), theta(b), R-eta, and gauge theta unmoved",
        "AC(i) measure-side realization binary" in note
        and "Theta(b) K-real mass reading" in note
        and "No R-eta readout identification is moved" in note
        and "No gauge-side theta winding account is moved" in note,
    )
    check(
        "no-go discipline is present",
        all(tag in note for tag in ("N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8")),
    )
    banned = ["fully closes", "solves theta", "derives K-reality", "retire AC_phi_lambda", "retire theta"]
    found = [phrase for phrase in banned if phrase in note]
    check("banned overclaim phrases are absent", not found, str(found))

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
