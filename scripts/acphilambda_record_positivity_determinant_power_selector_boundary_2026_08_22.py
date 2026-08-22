#!/usr/bin/env python3
"""Exact checks for a positive-block/determinant-power typing boundary.

The runner separates three typings of a complex determinant z:

1. a phase-complete real-linear positive branch block (only the zero map);
2. a quantum amplitude z A (branch trace proportional to |z|^2);
3. a separately supplied positive first-power weight or square-root writer.

It also checks that supplied positive blocks add while their cardinality does
not fix their calibration.  The calculation is a bounded finite theorem.  It
does not derive a probability law, physical matter action, determinant typing,
charged-lepton event map, or an axiom update.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

import sympy as sp


AUDIT_INPUT_PATHS = (
    "docs/ACPHILAMBDA_RECORD_POSITIVITY_DETERMINANT_POWER_SELECTOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-22.md",
)


MUTATIONS = (
    "phase_domain",
    "positivity_certificate",
    "holomorphic_hermitian",
    "direct_weight",
    "kraus_power",
    "phase_invariance",
    "normalization",
    "positive_ray",
    "sqrt_escape",
    "coarse_additivity",
    "multiplicativity",
    "source_scope",
)

parser = argparse.ArgumentParser()
parser.add_argument("--mutation", choices=MUTATIONS)
args = parser.parse_args()
mutation = args.mutation


@dataclass
class Check:
    name: str
    passed: bool
    detail: str


checks: list[Check] = []


def check(name: str, passed: bool, detail: str) -> None:
    checks.append(Check(name=name, passed=bool(passed), detail=detail))


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and all(
        sp.simplify(value) == 0 for value in left - right
    )


def scalar_equal(left: sp.Expr, right: sp.Expr) -> bool:
    return sp.simplify(left - right) == 0


def branch(amplitude: sp.Matrix, state: sp.Matrix) -> sp.Matrix:
    return sp.simplify(amplitude * state * amplitude.H)


def weight(block: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(block))


def psd_2x2(block: sp.Matrix) -> bool:
    """Exact Sylvester check for a Hermitian 2x2 positive-semidefinite block."""
    return (
        block.shape == (2, 2)
        and matrix_equal(block, block.H)
        and sp.simplify(block[0, 0]).is_nonnegative is True
        and sp.simplify(block[1, 1]).is_nonnegative is True
        and sp.simplify(block.det()).is_nonnegative is True
    )


# A. The determinant of the 1x1 complex kernel [z] reaches every complex
# phase.  The four displayed points provide both additive inverses and a real
# basis for C.  Removing one inverse is the hostile phase-domain mutation.
phase_points = (1, -1, sp.I, -sp.I)
if mutation == "phase_domain":
    phase_points = (1, 1, sp.I, -sp.I)
det_values = tuple(sp.det(sp.Matrix([[z]])) for z in phase_points)
check(
    "phase-complete determinant witness",
    det_values == (1, -1, sp.I, -sp.I),
    f"det([z]) values={det_values}",
)


# B. Let B:C->Herm(2) be real-linear and suppose B(z), B(-z) are positive.
# Then every quadratic form q_v(B(z)) is both >=0 and <=0, hence zero.  Four
# polarization probes reconstruct all four real Hermitian coordinates.  Their
# coefficient matrix is invertible, certifying B(z)=0 for every z.  A repeated
# probe destroys the certificate under mutation.
probe_matrix = sp.Matrix(
    [
        [1, 0, 0, 0],       # q(e1) = a
        [0, 1, 0, 0],       # q(e2) = b
        [1, 1, 2, 0],       # q(e1+e2) = a+b+2c
        [1, 1, 0, -2],      # q(e1+i e2) = a+b-2d
    ]
)
if mutation == "positivity_certificate":
    probe_matrix[3, :] = probe_matrix[2, :]
check(
    "real-linear phase-complete positive map is zero",
    probe_matrix.rank() == 4 and probe_matrix.det() != 0,
    f"polarization rank={probe_matrix.rank()} det={probe_matrix.det()}",
)


# C. More generally, an entrywise-holomorphic F:Omega->M_d(C) on a connected
# open complex domain whose image is Hermitian is constant.  For each quadratic
# probe its scalar value is real-valued and holomorphic.  Writing that scalar as
# u+i v, v=0 together with the Cauchy-Riemann equations forces both derivatives
# of u to vanish.  The exact constraint matrix below has full rank.  The
# polarization probes then reconstruct a constant matrix; if 0 is in Omega and
# F(0)=0, it is the zero map.
cr_matrix = sp.Matrix(
    [
        [0, 0, 1, 0],   # v_x = 0
        [0, 0, 0, 1],   # v_y = 0
        [1, 0, 0, -1],  # u_x - v_y = 0
        [0, 1, 1, 0],   # u_y + v_x = 0
    ]
)
if mutation == "holomorphic_hermitian":
    cr_matrix[3, :] = cr_matrix[2, :]
check(
    "holomorphic Hermitian branch-block map is constant",
    cr_matrix.rank() == 4 and cr_matrix.det() != 0,
    f"Cauchy-Riemann rank={cr_matrix.rank()} det={cr_matrix.det()}",
)


# D. A raw complex determinant is not itself a positive branch weight on the
# phase-complete domain.  The i fixture is neither Hermitian nor real-valued.
rho = sp.Matrix([[sp.Rational(3, 5), sp.Rational(1, 5)],
                 [sp.Rational(1, 5), sp.Rational(2, 5)]])
raw_z = sp.Integer(1) if mutation == "direct_weight" else sp.I
raw_block = sp.simplify(raw_z * rho)
check(
    "raw holomorphic determinant is not a positive branch block",
    not matrix_equal(raw_block, raw_block.H) and not weight(raw_block).is_real,
    f"z={raw_z} hermitian={matrix_equal(raw_block, raw_block.H)} trace={weight(raw_block)}",
)


# E. Standard amplitude typing.  If A_z=c z A_0, complete positivity supplies
# sigma_z=A_z rho A_z^dag=|z|^2 sigma_1.  The exact c=1/9 fixture also makes
# A_z a trace-nonincreasing branch with a positive completion.  The mutation
# drops the adjoint phase from the expected power.
a0 = sp.Matrix([[1, 1], [0, 1]])
z = 3 + 4 * sp.I
instrument_scale = sp.Rational(1, 9)
sigma_1 = branch(instrument_scale * a0, rho)
az = instrument_scale * z * a0
sigma_z = branch(az, rho)
expected_power = z**2 if mutation == "kraus_power" else z * sp.conjugate(z)
single_completion_effect = sp.simplify(sp.eye(2) - az.H * az)
single_branch_probability = weight(sigma_z)
single_completion_probability = sp.simplify(sp.trace(rho * single_completion_effect))
check(
    "Kraus amplitude gives a squared-modulus branch-trace factor",
    matrix_equal(sigma_z, sp.simplify(expected_power * sigma_1))
    and scalar_equal(weight(sigma_z), 25 * weight(sigma_1))
    and psd_2x2(single_completion_effect)
    and scalar_equal(single_branch_probability, sp.Rational(5, 9))
    and scalar_equal(single_completion_probability, sp.Rational(4, 9))
    and scalar_equal(single_branch_probability + single_completion_probability, 1),
    f"trace ratio={sp.simplify(weight(sigma_z)/weight(sigma_1))} "
    f"branch_probability={single_branch_probability} "
    f"completion_probability={single_completion_probability}",
)


# F. The standard branch weight is phase blind, as positivity requires for a
# scalar rephasing of the same amplitude.
phase = 2 if mutation == "phase_invariance" else sp.I
sigma_phase = branch(instrument_scale * phase * z * a0, rho)
check(
    "scalar amplitude phase leaves its positive branch block invariant",
    matrix_equal(sigma_phase, sigma_z),
    f"phase={phase} invariant={matrix_equal(sigma_phase, sigma_z)}",
)


# G. Competing amplitude branches inherit |z_j|^2 trace ratios.  The exact
# instrument includes a completion outcome, so 1/5 and 4/5 are conditional on
# landing in the displayed determinant branches rather than unconditional.
menu = (sp.Integer(1), 2 * sp.I)
menu_weights = [sp.simplify(v * sp.conjugate(v)) for v in menu]
denominator = sum(menu_weights)
conditional_probabilities = [sp.simplify(v / denominator) for v in menu_weights]
expected_conditionals = [sp.Rational(1, 2), sp.Rational(1, 2)] if mutation == "normalization" else [sp.Rational(1, 5), sp.Rational(4, 5)]
menu_effect = sp.zeros(2)
menu_branch_probabilities = []
for menu_value in menu:
    menu_amplitude = instrument_scale * menu_value * a0
    menu_effect += sp.simplify(menu_amplitude.H * menu_amplitude)
    menu_branch_probabilities.append(weight(branch(menu_amplitude, rho)))
menu_completion_effect = sp.simplify(sp.eye(2) - menu_effect)
menu_completion_probability = sp.simplify(sp.trace(rho * menu_completion_effect))
check(
    "conditional determinant-branch menu uses squared-modulus ratios",
    conditional_probabilities == expected_conditionals
    and menu_branch_probabilities == [sp.Rational(1, 45), sp.Rational(4, 45)]
    and scalar_equal(sum(conditional_probabilities), 1)
    and psd_2x2(menu_completion_effect)
    and scalar_equal(menu_completion_probability, sp.Rational(8, 9))
    and scalar_equal(sum(menu_branch_probabilities) + menu_completion_probability, 1),
    f"branch_probabilities={menu_branch_probabilities} "
    f"conditional={conditional_probabilities} completion={menu_completion_probability}",
)


# H. A determinant may instead scale a positive block directly on an
# independently supplied positive ray.  Extending that typing to a negative
# point immediately violates positivity; the mutation falsely omits it.
positive_ray_points = (sp.Integer(0), sp.Integer(2), sp.Integer(5))
if mutation != "positive_ray":
    positive_ray_points += (-sp.Integer(1),)
direct_traces = tuple(weight(sp.simplify(v * rho)) for v in positive_ray_points)
positive_prefix = all(value >= 0 for value in direct_traces[:3])
negative_escape = direct_traces[-1] < 0 if len(direct_traces) == 4 else False
check(
    "first-power direct weight needs a supplied positive domain",
    positive_prefix and negative_escape,
    f"domain={positive_ray_points} traces={direct_traces}",
)


# I. A first-power modulus weight can be realized by a square-root Kraus
# amplitude sqrt(|z|) A_0.  It is positive and has exponent one, but is not
# complex-linear in z.  Mutation uses |z| and loses the first-power receipt.
sqrt_scale = instrument_scale * (
    sp.Abs(z) if mutation == "sqrt_escape" else sp.sqrt(sp.Abs(z))
)
sqrt_sigma = branch(sqrt_scale * a0, rho)
sqrt_ratio = sp.simplify(weight(sqrt_sigma) / weight(sigma_1))
not_complex_linear = not matrix_equal(
    instrument_scale * sp.sqrt(sp.Abs(sp.I)) * a0,
    sp.I * instrument_scale * a0,
)
check(
    "modulus-power-one square-root writer is a separate nonlinear bridge",
    scalar_equal(sqrt_ratio, sp.Abs(z)) and not_complex_linear,
    f"trace ratio={sqrt_ratio} complex_linear={not not_complex_linear}",
)


# J. Coarse positive blocks inherit the sum of their supplied fine positive
# blocks.  Two equal-weight-w blocks sum to 2w, while a calibrated split into
# two weight-w/2 blocks sums back to w.  Cardinality alone fixes no factor.
p0 = sp.diag(1, 0)
p1 = sp.diag(0, 1)
w = sp.Rational(3, 7)
fine_0 = w * p0
fine_1 = w * p1
coarse = (fine_0 + fine_1) / 2 if mutation == "coarse_additivity" else fine_0 + fine_1
split_0 = (w / 2) * p0
split_1 = (w / 2) * p1
split_coarse = split_0 + split_1
check(
    "coarse addition preserves supplied fine-block calibration",
    scalar_equal(weight(coarse), 2 * w)
    and scalar_equal(weight(fine_0), w)
    and scalar_equal(weight(fine_1), w)
    and scalar_equal(weight(split_coarse), w),
    f"equal_fine=({weight(fine_0)},{weight(fine_1)}) equal_coarse={weight(coarse)} calibrated_split={weight(split_coarse)}",
)


# K. Independent amplitude composition preserves the second-power law.
z1 = 2 + sp.I
z2 = 1 - 2 * sp.I
composite_weight = sp.simplify((z1 * z2) * sp.conjugate(z1 * z2))
factor_weight = sp.simplify(
    (z1 * sp.conjugate(z1)) * (z2 * sp.conjugate(z2))
)
if mutation == "multiplicativity":
    factor_weight += 1
check(
    "squared-modulus amplitude factors compose multiplicatively",
    scalar_equal(composite_weight, factor_weight),
    f"composite={composite_weight} factors={factor_weight}",
)


# L. Source guards keep the theorem at the physical-selector boundary.
root = Path(__file__).resolve().parents[1]
note = root / "docs" / "ACPHILAMBDA_RECORD_POSITIVITY_DETERMINANT_POWER_SELECTOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-22.md"
note_text = note.read_text(encoding="utf-8") if note.exists() else ""
needles = (
    "not a universal no-go",
    "does not derive the physical charged-lepton matter action",
    "no minimal-axiom edit",
    "routes that remain live",
    "physical event map",
    "standard amplitude typing",
    "W_P",
)
if mutation == "source_scope":
    needles += ("THIS_MARKER_MUST_NOT_EXIST",)
check(
    "source preserves action, event-map, escape, and axiom boundaries",
    all(needle in note_text for needle in needles),
    f"needles={len(needles)} present={sum(needle in note_text for needle in needles)}",
)


for result in checks:
    label = "PASS" if result.passed else "FAIL"
    print(f"[{label}] {result.name}: {result.detail}")

print("per_element: checked — phase-complete scalar determinant fixtures and their positive-weight typings are exercised exactly")
print("per_site: checked and not executed — no site-local matter action, site calibration, or site-to-event lift is claimed")
print("per_mode: checked and not executed — no fermion-mode carrier or K/CPT mode independence is selected by this theorem")
print("per_block: checked — Hermitian positivity, Kraus branch blocks, and a two-fine-event coarse sum are exercised exactly")
print("lattice_wide: checked and not executed — no lattice dynamics, continuum lift, or full charged-lepton action is claimed")

passed = sum(result.passed for result in checks)
failed = len(checks) - passed
print(f"TOTAL: PASS={passed} FAIL={failed}")
raise SystemExit(0 if failed == 0 else 1)
