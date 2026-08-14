#!/usr/bin/env python3
"""Exact checks for formation-weight energy-dictionary underdetermination."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "FORMATION_WEIGHT_ENERGY_DICTIONARY_UNDERDETERMINATION_BOUNDED_THEOREM_NOTE_2026-08-13.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
JULY12_PATH = ROOT / "docs" / "KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md"
FORMATION_PATH = ROOT / "docs" / "ADMISSIBILITY_SUPPORT_CONSTRAINS_CONTENT_NOT_FORMATION_SITE_BOUNDED_THEOREM_NOTE_2026-08-13.md"

AUDIT_INPUT_PATHS = (
    "docs/FORMATION_WEIGHT_ENERGY_DICTIONARY_UNDERDETERMINATION_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md",
    "docs/ADMISSIBILITY_SUPPORT_CONSTRAINS_CONTENT_NOT_FORMATION_SITE_BOUNDED_THEOREM_NOTE_2026-08-13.md",
)

EnergyPair = tuple[Fraction, Fraction]


def normalize(text: str) -> str:
    return " ".join(text.split())


def declared_shares(w: Fraction, e_tot: Fraction) -> EnergyPair:
    return (w * e_tot, (1 - w) * e_tot)


def inverse_shares(w: Fraction, e_tot: Fraction) -> EnergyPair:
    return ((1 - w) * e_tot, w * e_tot)


def equal_shares(_w: Fraction, e_tot: Fraction) -> EnergyPair:
    return (e_tot / 2, e_tot / 2)


def dimension_shares(_w: Fraction, e_tot: Fraction) -> EnergyPair:
    return (e_tot / 3, 2 * e_tot / 3)


def affine_weight(t: Fraction, w: Fraction) -> Fraction:
    if not 0 <= t <= 1:
        raise ValueError("t must lie in [0,1]")
    if not 0 < w < 1:
        raise ValueError("w must lie in (0,1)")
    return t * w + (1 - t) * (1 - w)


def affine_shares(t: Fraction, w: Fraction, e_tot: Fraction) -> EnergyPair:
    if e_tot <= 0:
        raise ValueError("E_tot must be positive")
    g = affine_weight(t, w)
    return (g * e_tot, (1 - g) * e_tot)


def normalized_positive(pair: EnergyPair, e_tot: Fraction) -> bool:
    return pair[0] > 0 and pair[1] > 0 and pair[0] + pair[1] == e_tot


def channel_coordinates(pair: EnergyPair) -> EnergyPair:
    e_s, e_d = pair
    return (e_s / 3, e_d / 6)


def r_image(pair: EnergyPair) -> Fraction:
    e_s, e_d = pair
    if e_s <= 0:
        raise ZeroDivisionError("E_s must be positive")
    return e_d / (2 * e_s)


def declared_r(w: Fraction) -> Fraction:
    return (1 - w) / (2 * w)


def affine_r_formula(t: Fraction, w: Fraction) -> Fraction:
    g = affine_weight(t, w)
    return (1 - g) / (2 * g)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool, residual: object | None = None) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} {statement}")
        if not ok and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    july12 = JULY12_PATH.read_text(encoding="utf-8")
    formation = FORMATION_PATH.read_text(encoding="utf-8")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    normalized_july12 = normalize(july12)
    normalized_formation = normalize(formation)

    print("external_scientific_inputs: current Record boundary, July 12 declared dictionary, and August 13 formation-site residual are source-bound; no observation or fit")
    print("integrity_reads: this runner, its note, the current axiom memo, and two declared parent notes; no other scientific inputs")
    print("construction: conditional D_* solve plus an exact normalized affine family D_t joining inverse, equal, and declared shares")
    print("negative_scope: positivity and total-energy normalization do not uniquely select D_*; dynamics, symmetry, calibration, and content-to-energy maps remain live")

    checks.check("audit-inputs", "all four declared inputs exist", len(AUDIT_INPUT_PATHS) == 4 and AUDIT_TIMEOUT_SEC == 120 and all((ROOT / p).is_file() for p in AUDIT_INPUT_PATHS))

    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_content = "A readout value is determined by record content alone."
    record_absence = "A site with no record cannot be read."
    retired_boundary = "removed the named scalar functional `I`, finite additivity over disjoint record collections, and `I(empty)=0` from Record"
    declared_phrase = "this note's own declared modeling element"
    not_record_phrase = "It is not supplied by the Record axiom"
    formation_residual = "It supplies no site selector, formation probability, process, time, or physical rate."

    checks.check(
        "source-record-current",
        "lock, content-only readout, unreadable absence, and scalar retirement are pinned",
        all(p in normalized_axiom for p in (record_lock, record_content, record_absence, retired_boundary))
        and all(p in normalized_note for p in (record_lock, record_content, record_absence)),
    )
    checks.check(
        "source-record-no-energy-map",
        "current Record names neither the submitted dictionaries nor the channel energies",
        all(p not in axiom for p in ("D_*", "D_eq", "D_dim", "D_inv", "E_s", "E_d", "E_tot"))
        and "content-to-energy" in note,
    )
    checks.check(
        "source-july12-declaration",
        "July 12 calls the energy bridge a declared modeling element not supplied by Record",
        declared_phrase in normalized_july12
        and not_record_phrase in normalized_july12
        and "E_s = w E_tot" in july12
        and "E_d = (1-w) E_tot" in july12
        and "3 a^2" in july12
        and "6 |b|^2" in july12,
    )
    checks.check(
        "source-formation-residual",
        "current August 13 parent keeps formation selection and rate open",
        formation_residual in normalized_formation and "formation site" in normalized_note,
    )

    one = Fraction(1)
    w_third = Fraction(1, 3)
    w_half = Fraction(1, 2)

    for w in (w_third, w_half):
        pair = declared_shares(w, one)
        a2, b2 = channel_coordinates(pair)
        checks.check("declared-normalization", "D_* is positive and normalized at each comparison weight", normalized_positive(pair, one), residual=(w, pair))
        checks.check("declared-channel", "channel coordinates recover E_s=3a^2 and E_d=6|b|^2", 3 * a2 == pair[0] and 6 * b2 == pair[1], residual=(w, a2, b2))
        checks.check("declared-r", "conditional r equals (1-w)/(2w) and |b|^2/a^2", r_image(pair) == declared_r(w) == b2 / a2, residual=(w, r_image(pair), declared_r(w)))
        checks.check("declared-inverse", "w=1/(1+2r) inverts the declared image", 1 / (1 + 2 * r_image(pair)) == w)

    checks.check("declared-points", "D_* maps w=1/3 to r=1 and w=1/2 to r=1/2", r_image(declared_shares(w_third, one)) == 1 and r_image(declared_shares(w_half, one)) == w_half)

    t_grid = tuple(Fraction(k, 12) for k in range(13))
    w_grid = tuple(Fraction(k, 12) for k in range(1, 12))
    e_grid = (Fraction(1, 2), one, Fraction(7, 3))
    family_ok = all(
        normalized_positive(affine_shares(t, w, e_tot), e_tot)
        for t in t_grid
        for w in w_grid
        for e_tot in e_grid
    )
    checks.check("family-positive-normalized", "D_t is positive and normalized on the exact 13x11x3 rational grid", family_ok)
    checks.check("family-endpoints", "D_0=D_inv, D_1/2=D_eq, and D_1=D_* on the exact grid", all(affine_shares(0, w, e) == inverse_shares(w, e) and affine_shares(Fraction(1, 2), w, e) == equal_shares(w, e) and affine_shares(1, w, e) == declared_shares(w, e) for w in w_grid for e in e_grid))
    checks.check("dimension-comparator", "D_dim is positive and normalized but differs from D_* at w=1/2", normalized_positive(dimension_shares(w_half, one), one) and dimension_shares(w_half, one) != declared_shares(w_half, one))

    checks.check(
        "family-image-formula",
        "direct energy ratios equal the analytic affine image formula",
        all(r_image(affine_shares(t, w, one)) == affine_r_formula(t, w) for t in t_grid for w in w_grid),
    )
    checks.check(
        "third-image-formula",
        "at w=1/3, r_t=(1+t)/(2(2-t))",
        all(affine_r_formula(t, w_third) == (1 + t) / (2 * (2 - t)) for t in t_grid),
    )
    checks.check(
        "third-table",
        "inverse, equal, and declared shares give 1/4, 1/2, and 1 at w=1/3",
        r_image(affine_shares(0, w_third, one)) == Fraction(1, 4)
        and r_image(affine_shares(Fraction(1, 2), w_third, one)) == Fraction(1, 2)
        and r_image(affine_shares(1, w_third, one)) == 1,
    )
    checks.check(
        "half-coalescence",
        "all exact t-grid dictionaries coalesce at shares (1/2,1/2) and r=1/2 when w=1/2",
        all(affine_shares(t, w_half, one) == (w_half, w_half) and r_image(affine_shares(t, w_half, one)) == w_half for t in t_grid),
    )
    checks.check(
        "counterfamily-distinct",
        "distinct t-grid parameters give distinct shares at w=1/3",
        len({affine_shares(t, w_third, one) for t in t_grid}) == len(t_grid),
    )
    checks.check(
        "normalization-does-not-select",
        "D_0 and D_1 satisfy the same explicit normalization constraints but differ at w=1/3",
        normalized_positive(affine_shares(0, w_third, one), one)
        and normalized_positive(affine_shares(1, w_third, one), one)
        and affine_shares(0, w_third, one) != affine_shares(1, w_third, one),
    )

    checks.check("mutation-no-normalize", "using (wE_tot,wE_tot) fails total normalization away from w=1/2", sum((w_third, w_third), Fraction(0)) != one and normalized_positive(declared_shares(w_third, one), one))
    checks.check("mutation-constant-half", "replacing r_image by constant 1/2 fails declared w=1/3", r_image(declared_shares(w_third, one)) == 1 and Fraction(1, 2) != 1)
    checks.check("mutation-declared-only", "assuming t=1 erases exact live endpoint t=0", affine_shares(1, w_third, one) != affine_shares(0, w_third, one))

    allowed_retained = ("audit_required_before_effective_retained: true", "bare_retained_allowed: false")
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    required = (
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        "trace_class: negative_route_pruning",
        "target_claim_id: koide_energy_dictionary_r_from_w",
        "reachability_to_target: prunes",
        'hypothetical_axiom_status: "no edit"',
        "normalized affine counterfamily",
        "r_t(1/3)=(1+t)/(2(2-t))",
        "half-weight point is not a discriminator",
        "authors no audit verdict",
        "FAIL / DO NOT SHIP",
    )
    forbidden = (
        "For any finite collection of pairwise-disjoint records",
        "scalar readout `I` is additive",
        "I({s,d})",
        "I(empty)=0",
        "current Record additivity",
    )
    checks.check(
        "note-contract",
        "machine fields, current semantics, N1-N8, and retired-scalar hygiene hold",
        all(p in normalized_note for p in required)
        and all(line in note for line in allowed_retained)
        and all(f"### N{i}" in note for i in range(1, 9))
        and not any(p in note for p in forbidden)
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "new axiom" not in note.lower()
        and "Block 13" not in note
        and "toe-lphys" not in note,
    )

    print("per_element: the two channel energies, exact comparison weights, and affine-family parameters are evaluated rationally")
    print("per_site: one declared two-channel formation coordinate is analyzed; no physical site-selection theorem is claimed")
    print("per_mode: channel multiplicities three and six are used algebraically; no spectral-mode exhaustion is claimed")
    print("per_block: conditional inversion, normalized counterfamily, image formula, and half-weight coalescence are executed")
    print("lattice_wide: checked and not executed — no global formation law, energy readout, or dictionary no-go is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
