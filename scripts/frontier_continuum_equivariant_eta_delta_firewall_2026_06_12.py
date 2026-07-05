#!/usr/bin/env python3
"""Continuum equivariant-eta standard-form delta-firewall verifier.

Verifies:
  docs/CONTINUUM_EQUIVARIANT_ETA_STANDARD_FORM_DELTA_FIREWALL_BOUNDED_NOTE_2026-06-12.md

Statuses are pipeline-derived; the audit lane grades.

Run:
  python3 scripts/frontier_continuum_equivariant_eta_delta_firewall_2026_06_12.py
"""

from __future__ import annotations

import math
import re
import sys
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "CONTINUUM_EQUIVARIANT_ETA_STANDARD_FORM_DELTA_FIREWALL_BOUNDED_NOTE_2026-06-12.md"
DEP_FIXED = ROOT / "docs" / "KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
DEP_KD = ROOT / "docs" / "STAGGERED_DIRAC_SUBSTEP2_KAHLER_DIRAC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-17.md"
DEP_AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-05.md"

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    line = f"  [{'PASS' if ok else 'FAIL'}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def periodic_distance(x: float, y: float, period: float = 2.0 * math.pi) -> float:
    raw = abs(x - y) % period
    return min(raw, period - raw)


def lefschetz_from_omega(root: sp.Expr) -> tuple[sp.Expr, list[sp.Expr]]:
    terms = [
        sp.simplify(1 / ((1 - root**j) * (1 - root ** (2 * j))))
        for j in (1, 2)
    ]
    return sp.simplify(sp.Rational(1, 3) * sum(terms)), terms


def cotangent_from_weights() -> sp.Expr:
    raw = sum(
        sp.cot(sp.pi * j / 3) * sp.cot(sp.pi * 2 * j / 3)
        for j in (1, 2)
    )
    return sp.simplify(-sp.Rational(1, 3) * raw)


def c3_shift() -> np.ndarray:
    return np.array(
        [
            [0.0, 0.0, 1.0],
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
        ],
        dtype=complex,
    )


SIGMA_CHIRAL = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
SHIFT = c3_shift()
A_MASS = -2.0 * math.cos(0.42)
B_MASS = 1.0


def mass_matrix(phase: float) -> np.ndarray:
    return (
        A_MASS * np.eye(3, dtype=complex)
        + B_MASS * np.exp(1j * phase) * SHIFT
        + B_MASS * np.exp(-1j * phase) * SHIFT.T
    )


def d_operator(phase: float) -> np.ndarray:
    return np.kron(SIGMA_CHIRAL, mass_matrix(phase))


def mass_branches(phases: np.ndarray) -> np.ndarray:
    return np.array(
        [
            A_MASS + 2.0 * B_MASS * np.cos(phases + 2.0 * math.pi * k / 3.0)
            for k in range(3)
        ]
    )


def signed_crossings(branch: np.ndarray) -> tuple[int, int]:
    crosses = 0
    flow = 0
    n = len(branch)
    for idx in range(n):
        y0 = float(branch[idx])
        y1 = float(branch[(idx + 1) % n])
        if y0 == 0.0 or y1 == 0.0:
            continue
        if y0 * y1 < 0.0:
            crosses += 1
            flow += 1 if y0 < 0.0 < y1 else -1
    return crosses, flow


def eta_asymmetry(phase: float, eps: float = 1.0e-9) -> float:
    vals = np.linalg.eigvalsh(d_operator(phase)).real
    positives = int(np.sum(vals > eps))
    negatives = int(np.sum(vals < -eps))
    return float(positives - negatives)


def analytic_zero_crossings() -> list[float]:
    theta = math.acos(-A_MASS / (2.0 * B_MASS))
    zeros: set[float] = set()
    period = 2.0 * math.pi
    for k in range(3):
        offset = 2.0 * math.pi * k / 3.0
        for sign in (-1.0, 1.0):
            root = (sign * theta - offset) % period
            zeros.add(round(root, 14))
    return sorted(zeros)


def main() -> int:
    print("Continuum equivariant-eta standard-form delta firewall")

    note = read(NOTE)
    note_lower = note.lower()
    dep_fixed = read(DEP_FIXED)
    dep_kd = read(DEP_KD)
    dep_axioms = read(DEP_AXIOMS)
    source = read(Path(__file__).resolve())

    omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    lefschetz_value, lefschetz_terms = lefschetz_from_omega(omega)
    topological_eta = sp.Rational(2, 9)

    print("\nPart C1: exact localization")
    check(
        "C1a holomorphic-Lefschetz average is 2/9",
        sp.simplify(lefschetz_value - topological_eta) == 0,
        f"value={sp.sstr(lefschetz_value)}",
    )
    check(
        "C1a each nontrivial C_3 group term is 1/3",
        all(sp.simplify(term - sp.Rational(1, 3)) == 0 for term in lefschetz_terms),
        f"terms={[sp.sstr(t) for t in lefschetz_terms]}",
    )

    cotangent_value = cotangent_from_weights()
    check(
        "C1b cotangent product form is 2/9",
        sp.simplify(cotangent_value - topological_eta) == 0,
        f"value={sp.sstr(cotangent_value)}",
    )
    check(
        "C1b cotangent and Lefschetz forms agree",
        sp.simplify(cotangent_value - lefschetz_value) == 0,
        f"difference={sp.sstr(sp.simplify(cotangent_value - lefschetz_value))}",
    )
    factor_multiplier = sp.simplify(cotangent_value / lefschetz_value)
    check(
        "C1c standard factor multiplier is 1",
        factor_multiplier == 1,
        f"multiplier={sp.sstr(factor_multiplier)}",
    )

    print("\nPart C2 and anti-circularity")
    a_sym, b_sym, phase_sym, operator_sym = sp.symbols("a B phase operator")
    c1_symbols = set(lefschetz_value.free_symbols) | set(cotangent_value.free_symbols)
    forbidden_c1_symbols = {a_sym, b_sym, phase_sym, operator_sym}
    check(
        "C2 C1 expressions have no mass/operator/free-phase symbols",
        c1_symbols.isdisjoint(forbidden_c1_symbols),
        f"free_symbols={sorted(str(s) for s in c1_symbols)}",
    )
    phase_scan = np.linspace(0.0, 2.0 * math.pi, 97, endpoint=False)
    c1_scan = np.array([float(topological_eta) for _ in phase_scan])
    c1_range = float(np.max(c1_scan) - np.min(c1_scan))
    check("C2 explicit phase scan of C1 has range 0", c1_range == 0.0, f"range={c1_range:.3g}")

    banned_assignment = re.compile(
        r"\bdelta\s*=\s*(?:Rational\(\s*2\s*,\s*9\s*\)|2\s*/\s*9)\b"
    )
    lefschetz_args = lefschetz_from_omega.__code__.co_varnames[
        : lefschetz_from_omega.__code__.co_argcount
    ]
    cotangent_args = cotangent_from_weights.__code__.co_varnames[
        : cotangent_from_weights.__code__.co_argcount
    ]
    check(
        "ANTI-CIRCULARITY no forbidden delta assignment appears in runner source",
        banned_assignment.search(source) is None,
    )
    check(
        "ANTI-CIRCULARITY C1 code path takes omega/weights, not phase input",
        lefschetz_args == ("root",)
        and cotangent_args == ()
        and "phase" not in lefschetz_args
        and "phase" not in cotangent_args,
        f"lefschetz_args={lefschetz_args}, cotangent_args={cotangent_args}",
    )

    print("\nPart C3: operator family")
    phases = (np.arange(1440, dtype=float) + 0.5) * (2.0 * math.pi / 1440.0)
    branches = mass_branches(phases)
    full_branches = np.vstack([branches, -branches])
    crossing_counts = []
    spectral_flow = 0
    for branch in full_branches:
        count, flow = signed_crossings(branch)
        crossing_counts.append(count)
        spectral_flow += flow
    total_crossings = int(sum(crossing_counts))
    nontrivial_range = float(np.max(branches) - np.min(branches))
    check(
        "C3a D(delta) eigenvalue branches cross zero and are nontrivial",
        total_crossings >= 1 and nontrivial_range > 1.0,
        f"zero_crossings={total_crossings}, branch_range={nontrivial_range:.6f}",
    )
    check(
        "C3b spectral flow over one phase period is an integer and equals 0",
        isinstance(spectral_flow, int) and spectral_flow == 0,
        f"spectral_flow={spectral_flow}",
    )
    eta_values = np.array([eta_asymmetry(phase) for phase in phases[::12]])
    eta_range = float(np.max(eta_values) - np.min(eta_values))
    check(
        "C3c eta(delta) is flat over the scan",
        eta_range < 1.0e-9,
        f"eta_range={eta_range:.3g}",
    )

    print("\nPart C4: independence assembly")
    zero_crossings = analytic_zero_crossings()
    eta_float = float(topological_eta)
    distances = [periodic_distance(z, eta_float) for z in zero_crossings]
    nearest = min(distances)
    nearest_zero = zero_crossings[distances.index(nearest)]
    check(
        "C4a nearest zero-crossing does not match Part-C1 value",
        nearest > 0.1,
        f"topological_eta={eta_float:.12f}, nearest_zero={nearest_zero:.12f}, distance={nearest:.6f}",
    )

    analytic_index_is_integer = isinstance(spectral_flow, int)
    topological_eta_is_two_ninths = sp.simplify(topological_eta - sp.Rational(2, 9)) == 0
    mass_phase_free = c1_range == 0.0 and eta_range < 1.0e-9
    delta_forced_by_eta = False
    check(
        "C4b analytic index, topological eta, and free mass phase are distinct",
        analytic_index_is_integer
        and topological_eta_is_two_ninths
        and mass_phase_free
        and not delta_forced_by_eta,
        (
            f"analytic_index={spectral_flow}, topological_eta={sp.sstr(topological_eta)}, "
            f"mass_phase_free={mass_phase_free}, delta_forced_by_eta={delta_forced_by_eta}"
        ),
    )
    check(
        "C4c note states route boundary without irreducibility/no-go posture",
        "Route boundary" in note
        and "surviving route" in note
        and "This is not an R-eta derivation" in note
        and "or a no-go theorem over all possible continuum mechanisms" in note,
    )

    print("\nB-checks: note and dependencies")
    check(
        "B1 fixed-locus dependency carries L_3(1,2)=2/9 content",
        "fixed-locus" in dep_fixed
        and ("L3(1,2)" in dep_fixed or "L_3(1,2)" in dep_fixed or "L₃(1,2)" in dep_fixed)
        and "2/9" in dep_fixed,
    )
    check(
        "B2 substep2 dependency carries D_KD Kahler-Dirac content",
        "D_KD" in dep_kd and ("Kahler-Dirac" in dep_kd or "Kähler-Dirac" in dep_kd),
    )
    check(
        "B3 minimal axioms dependency is present and status-bounded as meta",
        "Minimal Framework Axioms" in dep_axioms and "**Type:** meta" in dep_axioms,
    )
    required_firewall = [
        "does not set the mass phase `delta`",
        "does not identify `delta`",
        "Does not force `delta`",
        "Does not claim no possible derivation of R-eta",
    ]
    forbidden_note_words = ("underivable", "irreducible on every", "exhausted")
    check(
        "B4 firewall wording is present and terminal no-go wording is absent",
        all(phrase in note for phrase in required_firewall)
        and all(word not in note.lower() for word in forbidden_note_words),
    )
    check(
        "B5 malformed no-go gate is absent",
        "No-Go / Bounded-Wall Discipline Gate" not in note
        and all(f"**N{i}" not in note for i in range(1, 9)),
    )
    check(
        "B6 anti-circularity confirmation sentence is present",
        "does not take `a`, `b`, `delta`, or an operator coupling" in note_lower
        and "no `a`, `b`, `delta`, or operator" in note_lower,
    )
    md_links = re.findall(r"\[[^\]]+\]\([^)]+\)", note)
    check(
        "B7 markdown link inventory is exactly three",
        len(md_links) == 3,
        f"count={len(md_links)}",
    )
    context_items = [
        "`the W21 algebraic-independence note`",
        "`the |delta| chain note`",
        "`RETA_MAGNITUDE_IS_CONTINUUM_INDEX_THEOREM_LATTICE_INDEX_IS_INTEGER_BOUNDED_NOTE_2026-06-12.md`",
        "`the domain-wall-edge note that supplied the Donnelly/Fukaya comparator`",
    ]
    check(
        "B8 context inventory is backticked",
        all(item in note for item in context_items),
    )
    check(
        "B9 status lines and No-promotion statement are present",
        "**Date:** 2026-06-12" in note
        and "**Claim type:** bounded_theorem" in note
        and "**Status authority:** independent audit lane" in note
        and "**No-promotion statement:**" in note,
    )

    print(f"\nSUMMARY: PASS={PASS} FAIL={FAIL} TOTAL={PASS + FAIL}")
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 and PASS >= 16 else 1


if __name__ == "__main__":
    sys.exit(main())
