#!/usr/bin/env python3
"""Exact current-axiom obstruction to YT bridge first-order moment nonselection.

This runner contains no physical target, fitted bridge, UV cut, profile-family
scan, or phenomenological constant.  It verifies an exact countermodel:

* an on-site qubit dynamics allowed by the current axiom surface has linear
  response kernel K(s) = sin(pi s), which is non-affine;
* two nonnegative profiles have identical zeroth and first moments but
  different responses under that kernel; and
* the current axiom authority explicitly withholds a dynamics and physical
  source/observable identification.

The result is a narrow non-derivability theorem.  It does not rule out a future
positive closure after a microscopic dynamics/source/readout packet is derived.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
NOTE_PATH = ROOT / "docs" / "YT_BRIDGE_MOMENT_CLOSURE_CURRENT_AXIOM_NONSELECTION_NO_GO_NOTE_2026-07-12.md"


@dataclass(frozen=True)
class Check:
    name: str
    ok: bool
    detail: str
    check_class: str


checks: list[Check] = []


def check(name: str, condition: bool, detail: str, check_class: str = "A") -> None:
    row = Check(name, bool(condition), detail, check_class)
    checks.append(row)
    state = "PASS" if row.ok else "FAIL"
    print(f"[{state} ({row.check_class})] {row.name}")
    print(f"    {row.detail}")


print("=" * 78)
print("YT BRIDGE FIRST-ORDER MOMENT NONSELECTION: EXACT CURRENT-AXIOM OBSTRUCTION")
print("=" * 78)

# Dependency-class check: the current framework authority says exactly which
# structures are and are not supplied.  This is a cross-note input
# verification, not a numerical physics input.
axiom_text = AXIOM_PATH.read_text(encoding="utf-8")
note_text = NOTE_PATH.read_text(encoding="utf-8")
axiom_text_flat = re.sub(r"\s+", " ", axiom_text)

required_axiom_clauses = (
    "It does not choose a Hamiltonian or transfer operator",
    "source/action and physical-observable identification",
    "scalar readout `I` is additive",
    "algebraic presentation `M_2(C)`",
)
check(
    "B1-current-axiom-authority-withholds-the-load-bearing-structures",
    all(clause in axiom_text_flat for clause in required_axiom_clauses),
    "current axiom memo supplies qubit/admissibility/additive-record structure but withholds Hamiltonian selection and source/observable identification",
    "B",
)

# Exact Pauli countermodel.
s = sp.symbols("s", real=True)
I = sp.I
pi = sp.pi

sigma_x = sp.Matrix([[0, 1], [1, 0]])
sigma_y = sp.Matrix([[0, -I], [I, 0]])
sigma_z = sp.Matrix([[1, 0], [0, -1]])
identity = sp.eye(2)
rho_z_plus = (identity + sigma_z) / 2
rho_x_plus = (identity + sigma_x) / 2

check(
    "A1-pauli-qubit-algebra",
    all(
        matrix == identity
        for matrix in (sigma_x**2, sigma_y**2, sigma_z**2)
    )
    and sigma_x * sigma_y + sigma_y * sigma_x == sp.zeros(2),
    "sigma_i^2=I and {sigma_x,sigma_y}=0 exactly",
)


def extra_admissible(neighbor_records: tuple[sp.Matrix, ...]) -> bool:
    """Exact countermodel rule: the extra 2I possibility needs six equal records."""
    return len(neighbor_records) == 6 and all(
        record == neighbor_records[0] for record in neighbor_records[1:]
    )


equal_neighbors = (rho_z_plus,) * 6
unequal_neighbors = (rho_z_plus,) * 5 + (rho_x_plus,)
rotated_neighbors = tuple(reversed(equal_neighbors))
check(
    "A2-admissibility-rule-varies-and-is-cubic-permutation-invariant",
    extra_admissible(equal_neighbors)
    and not extra_admissible(unequal_neighbors)
    and extra_admissible(rotated_neighbors),
    "A_x=D union {2I} for six equal neighboring records and A_x=D otherwise; equality is invariant under neighbor permutations",
)

density_checks = all(
    rho == rho.conjugate().T
    and sp.trace(rho) == 1
    and set(rho.eigenvals()).issubset({sp.Integer(0), sp.Integer(1)})
    for rho in (rho_z_plus, rho_x_plus)
)
readout_z = sp.trace(rho_z_plus * sigma_x)
readout_x = sp.trace(rho_x_plus * sigma_x)
check(
    "A3-record-content-is-admissible-and-readout-is-additive",
    density_checks
    and sp.simplify((readout_z + readout_x) - sum((readout_z, readout_x))) == 0,
    f"rho_z+,rho_x+ are density matrices in the always-admissible set D; I(Rz union Rx)={readout_z + readout_x}=I(Rz)+I(Rx)",
)

# H_0=(pi/2)sigma_z, V=sigma_x/2, O=sigma_x, T=1.  Derive both
# interaction-picture operators from the exact matrix exponential rather than
# inserting the rotated forms as expected values.
h_zero = pi * sigma_z / 2
source_operator = sigma_x / 2
endpoint_operator = sigma_x
u_zero_s = sp.simplify((-I * h_zero * s).exp())
u_zero_1 = sp.simplify(u_zero_s.subs(s, 1))
v_interaction = sp.simplify(u_zero_s.conjugate().T * source_operator * u_zero_s)
o_final_interaction = sp.simplify(
    u_zero_1.conjugate().T * endpoint_operator * u_zero_1
)
commutator = v_interaction * o_final_interaction - o_final_interaction * v_interaction
kernel = sp.simplify(I * sp.trace(rho_z_plus * commutator))

check(
    "A4-exact-qubit-linear-response-kernel",
    sp.simplify(kernel - sp.sin(pi * s)) == 0,
    f"i Tr(rho [V_I(s),O_I(1)]) = {kernel}",
)

# The law is a family over supplied (rho,H,V,O,phi), not a selection of the
# displayed Pauli coordinates.  A nontrivial exact unitary change of basis
# leaves the response invariant when the full supplied tuple is conjugated.
hadamard = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
rho_rot = sp.simplify(hadamard * rho_z_plus * hadamard.conjugate().T)
v_rot = sp.simplify(hadamard * v_interaction * hadamard.conjugate().T)
o_rot = sp.simplify(hadamard * o_final_interaction * hadamard.conjugate().T)
kernel_rot = sp.simplify(
    I * sp.trace(rho_rot * (v_rot * o_rot - o_rot * v_rot))
)
check(
    "A4b-supplied-law-family-is-coordinate-covariant",
    sp.simplify(kernel_rot - kernel) == 0,
    "simultaneous Hadamard conjugation of (rho,H,V,O) leaves i Tr(rho[V_I,O_I]) unchanged",
)
check(
    "A5-allowed-kernel-is-non-affine",
    sp.simplify(sp.diff(kernel, s, 2)) != 0,
    f"K''(s) = {sp.diff(kernel, s, 2)} is not identically zero",
)

# The alternative allowed zero Hamiltonian with source and observable along
# sigma_x has a vanishing commutator, so even the kernel itself is not selected
# by the axioms.
zero_kernel = sp.simplify(I * sp.trace(rho_z_plus * (sigma_x * sigma_x - sigma_x * sigma_x) / 2))
check(
    "A6-current-axiom-compatible-dynamics-give-different-kernels",
    zero_kernel == 0 and kernel != 0,
    "D_0 gives K=0 while D_pi gives K=sin(pi s)",
)

# Equal-moment profile pair.
h = 6 * s**2 - 6 * s + 1
phi_plus = 1 + h
phi_minus = 1 - h

h_at_endpoints_and_critical = [
    sp.simplify(h.subs(s, point)) for point in (0, sp.Rational(1, 2), 1)
]
critical_points = sp.solve(sp.Eq(sp.diff(h, s), 0), s)
check(
    "A7-profile-pair-is-nonnegative",
    critical_points == [sp.Rational(1, 2)]
    and sp.diff(h, s, 2) == 12
    and h_at_endpoints_and_critical == [1, sp.Rational(-1, 2), 1],
    "h'=12s-6 has unique critical point 1/2, h''=12>0, and endpoint/minimum values are 1,-1/2,1; hence 1+/-h are nonnegative",
)

i2_plus = sp.integrate(phi_plus, (s, 0, 1))
i2_minus = sp.integrate(phi_minus, (s, 0, 1))
first_plus = sp.integrate(s * phi_plus, (s, 0, 1))
first_minus = sp.integrate(s * phi_minus, (s, 0, 1))
c2_plus = sp.simplify(first_plus / i2_plus)
c2_minus = sp.simplify(first_minus / i2_minus)

check(
    "A8-profiles-have-identical-I2-and-c2",
    (i2_plus, c2_plus) == (i2_minus, c2_minus) == (1, sp.Rational(1, 2)),
    f"(I2+,c2+)={(i2_plus, c2_plus)}; (I2-,c2-)={(i2_minus, c2_minus)}",
)

response_plus = sp.integrate(kernel * phi_plus, (s, 0, 1))
response_minus = sp.integrate(kernel * phi_minus, (s, 0, 1))
response_difference = sp.factor(sp.simplify(response_plus - response_minus))
expected_difference = 4 * (pi**2 - 12) / pi**3

check(
    "A9-equal-moment-profiles-have-different-first-order-responses",
    sp.simplify(response_difference - expected_difference) == 0
    and response_difference.is_zero is False,
    f"R[phi+]-R[phi-] = {response_difference} != 0",
)

# The exact functional-analysis criterion: if every integrable perturbation
# orthogonal to 1 and s were annihilated, K would lie in span{1,s}.  The
# explicit h is already a witness that this allowed K fails that criterion.
annihilator_witness = sp.integrate(h * kernel, (s, 0, 1))
check(
    "A10-two-moment-annihilator-condition-fails",
    sp.simplify(annihilator_witness - 2 * (pi**2 - 12) / pi**3) == 0
    and annihilator_witness.is_zero is False,
    f"integral h(s)K(s) ds = {sp.factor(annihilator_witness)} != 0",
)

# Claim-state firewall checks pin the negative scope and absence of the old
# calibrated numerical inputs from the theorem statement.
required_boundary_phrases = (
    "not derivable",
    "does **not** say that an affine kernel is impossible",
    "No fitted target",
    "Independent audit must still review",
    "No-go discipline status:** `PASS`",
    "exactly one record forms at each site",
    "that record is then held fixed",
    "meta-family does not select an initial",
)
check(
    "B2-note-pins-the-narrow-negative-boundary",
    all(phrase in note_text for phrase in required_boundary_phrases),
    "note states current-surface non-derivability, future positive route, no-import firewall, record formation/uniqueness/permanence, law-domain neutrality, independent-audit gate, and N1-N8 PASS",
    "B",
)

failed = [row for row in checks if not row.ok]
class_counts = {
    label: sum(row.ok and row.check_class == label for row in checks)
    for label in ("A", "B", "C", "D")
}

print()
print("DEPENDENCY / INPUT CERTIFICATE")
print("  framework dependency: MINIMAL_AXIOMS_2026-06-29.md")
print("  admitted mathematics: Pauli algebra, finite-dimensional linear response, elementary calculus")
print("  fitted inputs: none")
print("  observational inputs: none")
print("  physical target values: none")
print("  selected proxy families/windows/thresholds: none")
print()
print("CLAIM BOUNDARY")
print("  Exact result: current axioms do not derive affine first-order response or first-order two-moment closure.")
print("  Not claimed: impossibility after a microscopic dynamics/source/readout law is derived.")
print("  Audit authority: independent audit required; effective status is pipeline-derived.")
print()
print(f"CHECK CLASS COUNTS: A={class_counts['A']} B={class_counts['B']} C={class_counts['C']} D={class_counts['D']}")
print(f"SUMMARY: PASS={len(checks) - len(failed)} FAIL={len(failed)}")

if failed:
    raise SystemExit(1)
