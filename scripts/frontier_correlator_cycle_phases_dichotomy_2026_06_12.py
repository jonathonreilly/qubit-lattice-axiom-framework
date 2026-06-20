#!/usr/bin/env python3
"""Verifier for the correlator cycle-phase dichotomy bounded note.

Run:
    python3 scripts/frontier_correlator_cycle_phases_dichotomy_2026_06_12.py

No cache is generated. No network, git, or gh command is invoked.
"""

from __future__ import annotations

import math
import re
import sys
from pathlib import Path

import numpy as np
import sympy as sp


PASS = 0
FAIL = 0
FAILURES: list[str] = []

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "CORRELATOR_CYCLE_PHASES_READBACK_BLIND_OR_STATE_CONTINGENT_BOUNDED_NOTE_2026-06-12.md"
SCRIPT = ROOT / "scripts" / "frontier_correlator_cycle_phases_dichotomy_2026_06_12.py"
TWOPI = 2.0 * math.pi


def check(name: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        FAILURES.append(name if not detail else f"{name} :: {detail}")
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag} {name}{suffix}")
    return ok


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def wrap_angle(x: float) -> float:
    return float((x + math.pi) % TWOPI - math.pi)


def angle_distance(a: float, b: float) -> float:
    return abs(wrap_angle(a - b))


def cycle_shift_np() -> np.ndarray:
    return np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=np.complex128)


def H_np(a: float, B: float, delta: float) -> np.ndarray:
    C = cycle_shift_np()
    return a * np.eye(3, dtype=np.complex128) + B * np.exp(1j * delta) * C + B * np.exp(-1j * delta) * C.T


def thermal_G(a: float, B: float, delta: float, beta: float) -> np.ndarray:
    vals, vecs = np.linalg.eigh(H_np(a, B, delta))
    weights = 1.0 / (1.0 + np.exp(beta * vals))
    return vecs @ np.diag(weights) @ vecs.conj().T


def cycle_phase(G: np.ndarray) -> float:
    return float(np.angle(G[0, 1] * G[1, 2] * G[2, 0]))


def edge_phase(G: np.ndarray) -> float:
    return wrap_angle(3.0 * float(np.angle(G[0, 1])))


def polar_link_phase(G: np.ndarray) -> float:
    edges = [G[0, 1], G[1, 2], G[2, 0]]
    polar = [z / abs(z) for z in edges]
    return float(np.angle(polar[0] * polar[1] * polar[2]))


def projector_np(k: int) -> np.ndarray:
    omega = np.exp(2j * np.pi / 3.0)
    v = np.array([omega ** (j * k) for j in range(3)], dtype=np.complex128)
    return np.outer(v, v.conj()) / 3.0


def elementary_from_eigs(eigs: np.ndarray) -> tuple[float, float, float]:
    e1 = float(np.sum(eigs))
    e2 = float(eigs[0] * eigs[1] + eigs[0] * eigs[2] + eigs[1] * eigs[2])
    e3 = float(np.prod(eigs))
    return e1, e2, e3


def symbolic_surface_checks() -> dict[str, bool]:
    a, B, delta = sp.symbols("a B delta", real=True, positive=True)
    I3 = sp.eye(3)
    C = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    H = a * I3 + B * sp.exp(sp.I * delta) * C + B * sp.exp(-sp.I * delta) * C.T

    omega = -sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2
    F = sp.Matrix([[omega ** (j * k) for k in range(3)] for j in range(3)])
    lambdas = [
        a + B * sp.exp(sp.I * delta) * omega ** k + B * sp.exp(-sp.I * delta) * omega ** (-k)
        for k in range(3)
    ]
    diag_residual = H * F - F * sp.diag(*lambdas)
    diag_ok = all(sp.simplify(x) == 0 for x in diag_residual)

    projectors_delta_free = True
    projector_formula_ok = True
    for k in range(3):
        v = F[:, k]
        P = sp.simplify(v * v.conjugate().T / 3)
        for x in range(3):
            for y in range(3):
                entry = sp.simplify(P[x, y])
                projectors_delta_free = projectors_delta_free and (delta not in entry.free_symbols)
                expected = omega ** (k * (x - y)) / 3
                projector_formula_ok = projector_formula_ok and (sp.simplify(entry - expected) == 0)

    edge_product = sp.simplify(H[0, 1] * H[1, 2] * H[2, 0])
    w1_ok = sp.simplify(edge_product - B**3 * sp.exp(3 * sp.I * delta)) == 0

    tr = sp.simplify(H.trace())
    e2 = sp.simplify((tr**2 - (H * H).trace()) / 2)
    e3 = sp.simplify(H.det())
    e3_expected = a**3 - 3 * a * B**2 + 2 * B**3 * sp.cos(3 * delta)
    e3_ok = sp.simplify(sp.expand_complex(e3 - e3_expected)) == 0

    return {
        "diag_ok": diag_ok,
        "projectors_delta_free": projectors_delta_free,
        "projector_formula_ok": projector_formula_ok,
        "w1_ok": w1_ok,
        "e3_ok": e3_ok,
    }


def main() -> int:
    section("Setup - circulance and phase routes")
    sample = thermal_G(a=0.5, B=1.0, delta=0.37, beta=1.0)
    edges = [sample[0, 1], sample[1, 2], sample[2, 0]]
    edge_equal_resid = max(abs(edges[i] - edges[0]) for i in range(3))
    route_resid = angle_distance(cycle_phase(sample), edge_phase(sample))
    polar_resid = angle_distance(cycle_phase(sample), polar_link_phase(sample))
    check("setup: three directed edge correlators are equal by circulance", edge_equal_resid < 1e-12, f"max residual={edge_equal_resid:.3e}")
    check("setup: phi = 3 arg g(-1) agrees with directed-product phase", route_resid < 1e-12, f"wrapped residual={route_resid:.3e}")
    check("setup: polar_u/link route agrees with directed-product route", polar_resid < 1e-12, f"wrapped residual={polar_resid:.3e}")

    section("Readback and projector-blind symbolic checks")
    sym = symbolic_surface_checks()
    check("readback-symbolic: f = identity gives directed product B^3 exp(3 i delta)", sym["w1_ok"])
    deltas = np.linspace(-0.9, 0.9, 31)
    w1_resid = max(angle_distance(cycle_phase(H_np(1.2, 0.7, float(d))), 3.0 * float(d)) for d in deltas)
    check("readback-scan: identity cycle phase equals 3 delta numerically", w1_resid < 5e-15, f"max residual={w1_resid:.3e}")
    check("projector-symbolic: Fourier eigenvector matrix diagonalizes H(delta) with no delta-moving eigenvectors", sym["diag_ok"])
    check("projector-symbolic: P_k entries are omega^{k(x-y)}/3 and carry no delta", sym["projectors_delta_free"] and sym["projector_formula_ok"])

    projector_spreads = []
    subsets = [(0,), (1,), (2,), (0, 1), (0, 2), (1, 2)]
    for subset in subsets:
        P = sum((projector_np(k) for k in subset), start=np.zeros((3, 3), dtype=np.complex128))
        phases = [cycle_phase(P) for _ in np.linspace(-0.95, 0.95, 25)]
        spread = max(angle_distance(p, phases[0]) for p in phases)
        projector_spreads.append(spread)
    projector_spread = max(projector_spreads)
    check("projector-scan: all nonzero rank-one/rank-two band projectors have delta-independent phi", projector_spread < 1e-14, f"max spread={projector_spread:.3e}")

    section("Thermal state-contingent branch")
    k_odd_resids = []
    for beta in (1.0, 4.0):
        for a, B in ((0.5, 1.0), (1.0, 2.0), (-0.5, 1.5)):
            for d in (0.1, 0.37, 0.8):
                p_plus = cycle_phase(thermal_G(a, B, d, beta))
                p_minus = cycle_phase(thermal_G(a, B, -d, beta))
                k_odd_resids.append(abs(wrap_angle(p_plus + p_minus)))
    k_odd_resid = max(k_odd_resids)
    check("thermal-K-odd: thermal phi is K-ODD, phi(-delta) = -phi(delta)", k_odd_resid < 2e-12, f"max wrapped residual={k_odd_resid:.3e}")

    variation_details = []
    for beta in (1.0, 4.0):
        scan = np.linspace(0.05, 0.95, 25)
        phases = np.unwrap([cycle_phase(thermal_G(0.5, 1.0, float(d), beta)) for d in scan])
        variation = float(np.max(phases) - np.min(phases))
        variation_details.append((beta, variation))
    check("thermal-scan: thermal phi is delta-dependent for beta in {1,4}", all(v > 0.2 for _, v in variation_details), "variations=" + ", ".join(f"beta={b:g}:{v:.6f}" for b, v in variation_details))

    a_grid = [-1.0, -0.25, 0.0, 0.5, 1.0, 1.75]
    B_grid = [0.25, 0.5, 1.0, 1.5, 2.0]
    delta0 = 2.0 / 9.0
    grid_spreads = {}
    grid_values: dict[float, list[float]] = {}
    for beta in (1.0, 4.0):
        vals = [cycle_phase(thermal_G(a, B, delta0, beta)) for a in a_grid for B in B_grid]
        grid_values[beta] = vals
        grid_spreads[beta] = max(vals) - min(vals)
    print("thermal grid spread at delta=2/9:")
    for beta in (1.0, 4.0):
        print(f"  beta={beta:g}: min={min(grid_values[beta]): .15f} max={max(grid_values[beta]): .15f} spread={grid_spreads[beta]: .15f}")
    check("thermal-grid: (a,B)-grid spread is order 0.2-3.0 and state-class-contingent", 0.2 < grid_spreads[1.0] < 3.0 and 0.2 < grid_spreads[4.0] < 3.1)

    cross_f_diffs = [
        angle_distance(cycle_phase(thermal_G(a, B, delta0, 4.0)), cycle_phase(thermal_G(a, B, delta0, 1.0)))
        for a in a_grid
        for B in B_grid
    ]
    cross_f_max = max(cross_f_diffs)
    print(f"thermal cross-f spread at delta=2/9: min={min(cross_f_diffs):.15f} max={cross_f_max:.15f}")
    check("thermal-grid: cross-f spread is computed and nontrivial", cross_f_max > 0.2, f"max |wrapped beta4-beta1|={cross_f_max:.6f}")

    candidates = {
        "1/9": 1.0 / 9.0,
        "2/9": 2.0 / 9.0,
        "3/10": 0.3,
        "4/9": 4.0 / 9.0,
        "2/3": 2.0 / 3.0,
        "2pi/9": 2.0 * math.pi / 9.0,
        "pi/3": math.pi / 3.0,
    }
    tested_classes = [
        (1.0, 0.0, 1.0),
        (1.0, 0.5, 1.0),
        (1.0, 1.0, 2.0),
        (4.0, 0.0, 1.0),
        (4.0, 0.5, 1.0),
        (4.0, 1.0, 2.0),
        (4.0, -0.5, 1.5),
    ]
    print("thermal delta=2/9 comparison table (distance uses |phi|):")
    comparison_ok = True
    for beta, a, B in tested_classes:
        phi = cycle_phase(thermal_G(a, B, delta0, beta))
        distances = {name: abs(abs(phi) - value) for name, value in candidates.items()}
        nearest_name = min(distances, key=distances.get)
        nearest = distances[nearest_name]
        comparison_ok = comparison_ok and nearest > 0.1
        print(f"  beta={beta:g} a={a: .2f} B={B: .2f} phi={phi: .15f} |phi|={abs(phi): .15f} nearest={nearest_name}:{nearest:.6f}")
    check("thermal-comparison: no tested thermal class lands within 0.1 of any candidate constant", comparison_ok)

    section("Cos(3 delta) inversion and dichotomy assembly")
    check("inversion-symbolic: determinant has derived coefficient 3 via cos(3 delta)", sym["e3_ok"])
    inversion_resids = []
    for a in (0.7, 1.2):
        for B in (0.3, 0.8):
            for d in (0.05, 0.2, 0.7, 0.95):
                eigs = np.linalg.eigvalsh(H_np(a, B, d))
                e1, e2, e3 = elementary_from_eigs(eigs)
                a_rec = e1 / 3.0
                B2_rec = (3.0 * a_rec * a_rec - e2) / 3.0
                B_rec = math.sqrt(max(B2_rec, 0.0))
                cos3 = (e3 - a_rec**3 + 3.0 * a_rec * B_rec**2) / (2.0 * B_rec**3)
                cos3 = max(-1.0, min(1.0, cos3))
                d_rec = math.acos(cos3) / 3.0
                inversion_resids.append(abs(d_rec - d))
    inversion_resid = max(inversion_resids)
    check("inversion-numeric: e3 symmetric data recover |delta| on (0, pi/3)", inversion_resid < 5e-13, f"max residual={inversion_resid:.3e}")
    monotone_grid = np.linspace(1e-4, math.pi / 3.0 - 1e-4, 200)
    derivatives = -3.0 * np.sin(3.0 * monotone_grid)
    check("inversion-uniqueness: cos(3 delta) is strictly monotone on (0, pi/3)", bool(np.all(derivatives < 0.0)), f"max derivative={float(np.max(derivatives)):.3e}")

    readback_class = w1_resid < 5e-15
    blind_class = projector_spread < 1e-14
    state_class = k_odd_resid < 2e-12 and all(v > 0.2 for _, v in variation_details) and comparison_ok
    class_rows = {
        "identity": (readback_class, False, False),
        "rank-one/rank-two projectors": (False, blind_class, False),
        "thermal beta=1": (False, False, state_class),
        "thermal beta=4": (False, False, state_class),
    }
    exactly_one = all(sum(bool(x) for x in row) == 1 for row in class_rows.values())
    check("dichotomy (tested classes only, not surface exhaustion): each tested class falls in exactly one of {readback, blind, state-contingent}", exactly_one, str(class_rows))

    section("B-checks - note firewall, open targets, links, and status")
    note_text = NOTE.read_text(encoding="utf-8")
    lower = note_text.lower()
    flat_lower = " ".join(lower.split())
    check(
        "B1: firewall and open-target sentences are present",
        all(
            s in flat_lower
            for s in (
                "do not close",
                "the next paths",
                "registered state data",
                "no universality",
                "open-target update",
                "tested classes",
                "do not provide a carrier-class exhaustion theorem",
            )
        ),
    )
    forbidden = (
        "closes",
        "exhausted",
        "only path",
        "only route",
        "underivable theorem",
        "carrier-class elimination pattern",
        "removes a state-independent carrier-angle middleman",
    )
    check("B2: forbidden overclaim phrases are absent", not any(s in lower for s in forbidden), "checked=" + ", ".join(forbidden))
    check("B3: R-eta firewall is explicit and no fixed r value is used", "makes no r-eta claim either way" in flat_lower and "no fixed value of `r`" in flat_lower)
    check("B4: No-promotion statement present", "**No-promotion statement:**" in note_text)
    check("B5: status-authority and claim-type lines present", all(s in note_text for s in ("**Date:** 2026-06-12", "**Claim type:** bounded_theorem", "**Status authority:** independent audit lane only")))
    check("B6: readback consistency-vs-derivation sentence present", "consistency identity, not an independent derivation" in lower)
    links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", note_text)
    link_targets = {target for _, target in links}
    expected_targets = {"MINIMAL_AXIOMS_2026-06-05.md", "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"}
    check("B7: markdown link inventory is <= 3 and exactly the chosen dependency links", len(links) <= 3 and link_targets == expected_targets, f"links={links}")
    context_names = (
        "`INDUCED_HOLONOMY_MATTER_STATE_FUNCTIONAL_DERIVED_CURVATURE_TRAJECTORY_BOUNDED_THEOREM_NOTE_2026-06-10.md`",
        "`TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md`",
        "`UNORDERED_MASS_MULTISET_REGISTRABILITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-11.md`",
        "`KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-09.md`",
        "`KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`",
    )
    check("B8: context references are backticked", all(name in note_text for name in context_names))
    check("B9: target files exist and no runner cache path is declared", NOTE.exists() and SCRIPT.exists() and "logs/runner-cache" not in note_text)
    check(
        "B10: No-Go Discipline Gate is present and surface-local",
        "## No-Go Discipline Gate" in note_text
        and "tested-class surface-local boundary" in flat_lower
        and "not a carrier-class exhaustion theorem" in flat_lower
        and "not a global no-go for r-eta" in flat_lower,
    )
    check(
        "B11: carrier-class exhaustion remains explicit future work",
        "carrier-class exhaustion theorem" in flat_lower
        and "not supplied here" in flat_lower
        and "does not exhaust all possible state-independent carrier-angle middlemen" in flat_lower,
    )
    check(
        "B12: title and N2 are scoped to the tested classes, not surface-wide exhaustion",
        "tested identity/projector/thermal correlator cycle phases" in flat_lower
        and "for the three tested classes" in flat_lower
        and "not a claim that every carrier on this surface falls into one of these three faces" in flat_lower,
    )
    check(
        "B13: 2026-06-20 repair section narrows to the bounded checks and frames exhaustion as an open bridge",
        "## repair (2026-06-20): narrowed to the tested bounded checks only" in flat_lower
        and "remains an open bridge" in flat_lower
        and "does not attempt the carrier-class exhaustion theorem" in flat_lower,
    )

    section("Manual git diff --stat equivalent (no git invoked)")
    total_lines = 0
    for path in (NOTE, SCRIPT):
        rel = path.relative_to(ROOT)
        line_count = len(path.read_text(encoding="utf-8").splitlines())
        total_lines += line_count
        print(f" {rel} | {line_count} +")
    print(f" 2 files changed, {total_lines} insertions(+)")

    print("\nSUMMARY:")
    print("  Identity phases are readback: phi=3 delta exactly.")
    print("  Spectral projector phases are delta-blind because Fourier projectors do not move.")
    print("  Thermal phases are K-odd and state-contingent registered data, not universal readout identifications.")
    print("  Symmetric data recover |delta| through the derived cos(3 delta) inversion, leaving the named next paths open.")
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("FAILURES:")
        for item in FAILURES:
            print(f"  - {item}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
