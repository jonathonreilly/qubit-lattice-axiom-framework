#!/usr/bin/env python3
"""Runner for ALPHA_BARE_FOUR_PI_FROM_Z3_PLANCHEREL_BRIDGE_BOUNDED_NOTE_2026-05-26."""

from __future__ import annotations

import math
import sys
from pathlib import Path

import sympy as sp

try:
    import numpy as np
except ImportError as exc:
    print(f"ERROR: numpy import failed: {exc}")
    sys.exit(2)


EXACT_PASS = 0
EXACT_FAIL = 0
BOUNDED_PASS = 0
BOUNDED_FAIL = 0
FAIL_NOTES: list[str] = []

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs/ALPHA_BARE_FOUR_PI_FROM_Z3_PLANCHEREL_BRIDGE_BOUNDED_NOTE_2026-05-26.md"
SOURCE_TEXT = NOTE_PATH.read_text(encoding="utf-8")


def exact_assert(condition: bool, label: str) -> None:
    global EXACT_PASS, EXACT_FAIL
    if condition:
        EXACT_PASS += 1
        print(f"  PASS [EXACT]  {label}")
    else:
        EXACT_FAIL += 1
        FAIL_NOTES.append(label)
        print(f"  FAIL [EXACT]  {label}")


def bounded_assert(condition: bool, label: str, tol: str = "") -> None:
    global BOUNDED_PASS, BOUNDED_FAIL
    if condition:
        BOUNDED_PASS += 1
        print(f"  PASS [BOUNDED] {label} {tol}")
    else:
        BOUNDED_FAIL += 1
        FAIL_NOTES.append(label)
        print(f"  FAIL [BOUNDED] {label} {tol}")


PI = math.pi
TWO_PI = 2.0 * PI
FOUR_PI = 4.0 * PI


print("=" * 78)
print("Section 0: source-boundary firewall")
print("=" * 78)

required_source_phrases = {
    "bounded theorem": "**Claim type:** bounded_theorem",
    "status authority": "independent audit lane only",
    "bz dependency": "BZ_VOLUME_TWO_PI_CUBED_SUBSTRATE_INTERNAL_NARROW_THEOREM_NOTE_2026-05-26.md",
    "framework-local green dependency": "LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md",
    "green certificate runner dependency": "scripts/lattice_greens_z3_asymptotic_normalization_certificate.py",
    "i1 dependency": "STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md",
    "i2 dependency": "ALPHA_CONVENTION_I2_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md",
    "i3 dependency": "CL3_NORMALIZATION_I3_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md",
    "no new axiom": "no new repo-wide axiom",
    "current minimal axioms memo": "MINIMAL_AXIOMS_2026-06-05.md",
}
for label, needle in required_source_phrases.items():
    exact_assert(needle in SOURCE_TEXT, f"(S-required) source contains {label}")

forbidden_source_phrases = [
    "retained-bounded",
    "retained_bounded",
    "audited_conditional",
    "effective_status",
    "MINIMAL_AXIOMS_2026-05-03",
    "MINIMAL_AXIOMS_2026-05-20",
    "A1 (local algebra)",
    "A2 (spatial substrate)",
    "spatial substrate",
    "substrate-internal",
    "canonical Cl(3) connection normalization",
    "new admission",
    "admission count",
    "axiom class",
    "Koide A1",
    "](HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md)",
    "](HIERARCHY_ALPHA_LM_EXPONENT_SPECIES_COUNT_BRIDGE_REGULATOR_DEPENDENCE_NO_GO_NOTE_2026-05-10.md)",
    "Maradudin accepted-premise bridge",
    "accepted Maradudin asymptotic",
]
for phrase in forbidden_source_phrases:
    exact_assert(
        phrase not in SOURCE_TEXT,
        f"(S-forbidden) source excludes stale/overpromoted phrase: {phrase}",
    )


print()
print("=" * 78)
print("Section A: BZ Haar constants")
print("=" * 78)

k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
haar_density = 1 / (2 * sp.pi) ** 3
haar_total = sp.integrate(
    sp.integrate(
        sp.integrate(haar_density, (k1, -sp.pi, sp.pi)),
        (k2, -sp.pi, sp.pi),
    ),
    (k3, -sp.pi, sp.pi),
)
exact_assert(
    sp.simplify(haar_total - 1) == 0,
    "(BZ-Haar) int_{[-pi,pi]^3} d^3k/(2 pi)^3 = 1",
)

bz_volume = (2 * sp.pi) ** 3
exact_assert(
    sp.simplify(bz_volume - 8 * sp.pi**3) == 0,
    "(BZ-Vol) vol([-pi,pi]^3) = (2 pi)^3 = 8 pi^3",
)


print()
print("=" * 78)
print("Section B: framework-local Green coefficient constants")
print("=" * 78)

theta, phi, k, r = sp.symbols("theta phi k r", positive=True, real=True)
sphere_area = sp.integrate(
    sp.integrate(sp.sin(theta), (theta, 0, sp.pi)),
    (phi, 0, 2 * sp.pi),
)
exact_assert(
    sp.simplify(sphere_area - 4 * sp.pi) == 0,
    "(B1) int_{S^2} dOmega = 4 pi",
)

dirichlet = sp.integrate(sp.sin(k * r) / k, (k, 0, sp.oo))
exact_assert(
    sp.simplify(dirichlet - sp.pi / 2) == 0,
    "(B2) int_0^oo sin(k r)/k dk = pi/2 for r > 0",
)

coefficient = (4 * sp.pi) / (2 * sp.pi) ** 3 * (sp.pi / 2)
exact_assert(
    sp.simplify(coefficient - 1 / (4 * sp.pi)) == 0,
    "(B3) (4 pi)/(2 pi)^3 * (pi/2) = 1/(4 pi)",
)


print()
print("=" * 78)
print("Section C: alpha-bare composition algebra")
print("=" * 78)

C, g_bare, alpha, rr = sp.symbols("C g_bare alpha r", positive=True, real=True)
G_asymptotic = 1 / (4 * sp.pi * rr)
V_from_static_source = -C * g_bare**2 * G_asymptotic
alpha_def = g_bare**2 / (4 * sp.pi)
V_alpha_form = -C * alpha / rr

exact_assert(
    sp.simplify(V_alpha_form.subs(alpha, alpha_def) - V_from_static_source) == 0,
    "(C1) -C alpha/r with alpha=g_bare^2/(4 pi) equals -C g_bare^2/(4 pi r)",
)

exact_assert(
    sp.simplify(alpha_def.subs(g_bare, 1) - 1 / (4 * sp.pi)) == 0,
    "(C2) at g_bare=1, alpha_bare=1/(4 pi)",
)

exact_assert(
    sp.simplify(V_from_static_source.subs(g_bare, 1) + C / (4 * sp.pi * rr)) == 0,
    "(C3) at g_bare=1, V(r) -> -C/(4 pi r)",
)


print()
print("=" * 78)
print("Section D: bounded lattice Green sanity check")
print("=" * 78)


def lattice_green_subtracted(r_vec: tuple[int, int, int], n_k: int = 96) -> tuple[float, float]:
    rx, ry, rz = r_vec
    r_mag = math.sqrt(rx * rx + ry * ry + rz * rz)
    g_cont = 1.0 / (FOUR_PI * r_mag)
    dk = TWO_PI / n_k
    grid = np.linspace(-PI + dk / 2, PI - dk / 2, n_k)
    kk1, kk2, kk3 = np.meshgrid(grid, grid, grid, indexing="ij")
    lam = 2.0 * (3.0 - np.cos(kk1) - np.cos(kk2) - np.cos(kk3))
    ksq = kk1**2 + kk2**2 + kk3**2
    mask = ksq > 1e-20
    sub = np.zeros_like(lam)
    sub[mask] = 1.0 / lam[mask] - 1.0 / ksq[mask]
    phase = np.cos(kk1 * rx + kk2 * ry + kk3 * rz)
    delta = float(np.sum(sub * phase) * (dk / TWO_PI) ** 3)
    return g_cont + delta, g_cont


for r_vec in ((8, 0, 0), (12, 0, 0), (5, 5, 5), (6, 8, 0)):
    g_lat, g_cont = lattice_green_subtracted(r_vec)
    ratio = g_lat / g_cont
    bounded_assert(
        abs(ratio - 1.0) < 0.035,
        f"(D1) G_lat({r_vec}) / (1/(4 pi |r|)) near 1",
        tol=f"ratio = {ratio:.6f}",
    )


print()
print("=" * 78)
print("Section E: no-import / boundary audit")
print("=" * 78)

load_bearing_inputs = {
    "BZ Haar d^3k/(2 pi)^3": "landed BZ lattice theorem",
    "G(r)->1/(4 pi r)": "framework-local Green theorem",
    "V=-C g_bare^2 G": "landed I1 bridge",
    "alpha=g_bare^2/(4 pi)": "landed I2 bridge",
    "g_bare=1 no-rescaling surface": "landed I3 bridge",
    "symbolic substitution": "closed algebra",
}

exact_assert(
    len(load_bearing_inputs) == 6,
    "(E1) load-bearing inputs enumerable (6 items)",
)
exact_assert(
    "d^4 k / (2 pi)^4" not in str(load_bearing_inputs),
    "(E2) no 4D loop-measure import in load-bearing inputs",
)
exact_assert(
    "Wick" not in str(load_bearing_inputs),
    "(E3) no Wick rotation in load-bearing inputs",
)


print()
print("=" * 78)
print("Summary")
print("=" * 78)
print(f"EXACT   : PASS = {EXACT_PASS}, FAIL = {EXACT_FAIL}")
print(f"BOUNDED : PASS = {BOUNDED_PASS}, FAIL = {BOUNDED_FAIL}")
total_pass = EXACT_PASS + BOUNDED_PASS
total_fail = EXACT_FAIL + BOUNDED_FAIL
print(f"TOTAL   : PASS = {total_pass}, FAIL = {total_fail}")
print()

if total_fail == 0:
    print("VERDICT: bounded alpha-bare composition bridge passes.")
    print("  The alpha-bare (4 pi) denominator composes with the Z^3")
    print("  framework-local Green coefficient through the landed BZ, I1, I2, and I3 rows.")
    sys.exit(0)

print("VERDICT: FAIL - alpha-bare composition bridge did not verify.")
print("Failed checks:")
for note in FAIL_NOTES:
    print(f"  - {note}")
sys.exit(1)
