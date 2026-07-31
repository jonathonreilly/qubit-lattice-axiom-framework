#!/usr/bin/env python3
"""Exact checks for the coordinate-conditioned Z^3 dual-torus theorem.

The runner checks consequences of an explicit character coordinate
``chi_k(n) = exp(i k.n)``. It does not claim that bare Z^3 selects that
coordinate, and it does not apply an audit verdict.
"""

from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp


AUDIT_INPUT_PATHS = (
    "docs/BZ_VOLUME_TWO_PI_CUBED_SUBSTRATE_INTERNAL_NARROW_THEOREM_NOTE_2026-05-26.md",
)

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
SOURCE_TEXT = NOTE_PATH.read_text(encoding="utf-8")

PASS_COUNT = 0
FAIL_COUNT = 0
FAIL_NOTES: list[str] = []


def exact_check(condition: bool, label: str) -> None:
    """Record a deterministic exact check."""

    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        print(f"  PASS [EXACT] {label}")
    else:
        FAIL_COUNT += 1
        FAIL_NOTES.append(label)
        print(f"  FAIL [EXACT] {label}")


pi = sp.pi
two_pi = 2 * pi

print("SECTION source claim boundary")

required_source_phrases = {
    "explicit angular pairing": "χ_k(n) = exp(i k·n)",
    "coordinate-conditioned boundary": "coordinate-conditioned algebraic statement",
    "current lattice axiom": "MINIMAL_AXIOMS_2026-06-29.md",
    "unit-coordinate disclaimer": "absolute physical lattice spacing",
    "reparameterized density": "μ_Haar(dξ) = d³ξ",
    "full-rank condition": "det A ≠ 0",
    "independent audit authority": "independent audit lane alone",
}
for label, phrase in required_source_phrases.items():
    exact_check(phrase in SOURCE_TEXT, f"source states {label}")

forbidden_source_phrases = {
    "stale minimal-axiom memo": "MINIMAL_AXIOMS_2026-05-20.md",
    "bare substrate-internal promotion": "is therefore **substrate-internal**",
    "authored audit verdict": "audited_clean",
    "authored effective status": "effective_status =",
}
for label, phrase in forbidden_source_phrases.items():
    exact_check(phrase not in SOURCE_TEXT, f"source excludes {label}")

print("SECTION angular character period")

integer_samples = (
    ((1, 0, 0), (3, -2, 5)),
    ((2, -1, 4), (-7, 3, 2)),
    ((-3, 5, 1), (11, -4, 6)),
)
for index, (m_values, n_values) in enumerate(integer_samples, start=1):
    m_vec = sp.Matrix(m_values)
    n_vec = sp.Matrix(n_values)
    integer_pairing = (m_vec.dot(n_vec))
    phase = sp.exp(2 * sp.pi * sp.I * integer_pairing)
    exact_check(
        sp.simplify(phase) == 1,
        f"character period sample {index}",
    )

exact_check(
    sp.simplify(sp.exp(-2 * sp.pi * sp.I * sp.Integer(17))) == 1,
    "exponent-sign reversal preserves the period",
)
exact_check(
    sp.simplify(sp.exp(sp.I * pi * 7) - sp.exp(-sp.I * pi * 7)) == 0,
    "half-open cell endpoints represent the same character",
)

print("SECTION standard-coordinate covolume and Haar density")

axis_length = pi - (-pi)
standard_volume = axis_length**3
standard_density = sp.Integer(1) / standard_volume

exact_check(sp.simplify(axis_length - two_pi) == 0, "half-open axis length is 2 pi")
exact_check(
    sp.simplify(standard_volume - two_pi**3) == 0,
    "standard reciprocal-cell volume is (2 pi)^3",
)
exact_check(
    sp.simplify(standard_density - 1 / (8 * pi**3)) == 0,
    "Haar coordinate density is 1/(8 pi^3)",
)
exact_check(
    sp.simplify(standard_volume * standard_density) == 1,
    "standard Haar total mass is one",
)

print("SECTION coordinate reparameterization")

jacobian_k_from_xi = two_pi**3
xi_density = sp.simplify(standard_density * jacobian_k_from_xi)
exact_check(xi_density == 1, "xi=k/(2 pi) removes the written denominator")
exact_check(
    sp.simplify(xi_density * sp.Integer(1)) == 1,
    "unit xi-cell has Haar mass one",
)
exact_check(
    xi_density != standard_density,
    "coordinate density changes while normalized measure does not",
)

print("SECTION variable spacing")

spacing = sp.Rational(3, 2)
spacing_volume = (two_pi / spacing) ** 3
spacing_density = spacing**3 / two_pi**3
exact_check(
    sp.simplify(spacing_volume - two_pi**3 / spacing**3) == 0,
    "spacing-dependent reciprocal volume",
)
exact_check(
    sp.simplify(spacing_density - 1 / spacing_volume) == 0,
    "spacing-dependent Haar density",
)
exact_check(
    sp.simplify(spacing_volume * spacing_density) == 1,
    "spacing-dependent Haar mass is one",
)
exact_check(
    sp.simplify(spacing_volume - standard_volume) != 0,
    "changing spacing changes coordinate covolume",
)

print("SECTION non-orthogonal full-rank lattice")

lattice_basis = sp.Matrix(
    [
        [2, 1, 0],
        [0, 3, 0],
        [0, 0, 1],
    ]
)
det_a = sp.simplify(lattice_basis.det())
reciprocal_basis = sp.simplify(two_pi * lattice_basis.inv().T)
reciprocal_volume = sp.simplify(reciprocal_basis.det())
general_density = sp.simplify(det_a / two_pi**3)

exact_check(det_a == 6, "non-orthogonal test basis has determinant six")
exact_check(
    sp.simplify(lattice_basis.T * reciprocal_basis - two_pi * sp.eye(3))
    == sp.zeros(3),
    "direct and reciprocal bases pair to 2 pi identity",
)
exact_check(
    sp.simplify(reciprocal_volume - two_pi**3 / det_a) == 0,
    "reciprocal covolume is (2 pi)^3/det(A)",
)
exact_check(
    sp.simplify(reciprocal_volume * general_density) == 1,
    "general full-rank Haar mass is one",
)

direct_integer = sp.Matrix([2, -1, 3])
reciprocal_integer = sp.Matrix([-4, 5, 1])
physical_point = lattice_basis * direct_integer
reciprocal_shift = reciprocal_basis * reciprocal_integer
pairing = sp.simplify(physical_point.dot(reciprocal_shift))
exact_check(
    sp.simplify(pairing - two_pi * direct_integer.dot(reciprocal_integer)) == 0,
    "non-orthogonal reciprocal shift has integral character phase",
)
exact_check(
    sp.simplify(sp.exp(sp.I * pairing)) == 1,
    "non-orthogonal character is periodic under reciprocal shifts",
)

print("SECTION rank and boundary guards")

rank_deficient_basis = sp.Matrix(
    [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
)
exact_check(rank_deficient_basis.det() == 0, "rank-deficient basis is detected")
exact_check(
    rank_deficient_basis.rank() < 3,
    "three-dimensional reciprocal-cell formula is excluded when rank is below three",
)

shift = sp.Rational(5, 7)
shifted_axis_length = (shift + pi) - (shift - pi)
exact_check(
    sp.simplify(shifted_axis_length**3 - standard_volume) == 0,
    "shifted half-open cells preserve covolume",
)

print("SUMMARY")
print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
if FAIL_COUNT:
    print("CHECK RESULT: coordinate-conditioned Haar algebra fails.")
    for note in FAIL_NOTES:
        print(f"  - {note}")
    sys.exit(1)

print("CHECK RESULT: coordinate-conditioned Haar algebra passes.")
sys.exit(0)
