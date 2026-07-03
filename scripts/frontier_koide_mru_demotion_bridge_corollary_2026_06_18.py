#!/usr/bin/env python3
"""
Source-side runner for `KOIDE_MRU_DEMOTION_NOTE_2026-04-20`.

This runner verifies the repaired scope of the MRU demotion note:

1. the note demotes the SO(2)-quotient/MRU route instead of promoting it;
2. the only graph-visible retained authority is the spectrum-operator bridge;
3. the block-total Frobenius theorem is bounded context, not an independent
   unbounded closure route in this note;
4. the Path-A trace obstruction uses the correct tr(H^3) phase term; and
5. the bridge corollary `spectrum Q = 2/3 => operator kappa = 2` is exact on
   Herm_circ(3).

No audit verdict or ledger update is written here.
"""

from __future__ import annotations

import cmath
import math
import re
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "KOIDE_MRU_DEMOTION_NOTE_2026-04-20.md"
BLOCK_TOTAL_NOTE = (
    ROOT / "docs" / "KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md"
)

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] {label}")
    if detail:
        print(f"         {detail}")


def flattened(text: str) -> str:
    return " ".join(text.split())


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_source_boundaries() -> None:
    note = read(NOTE)
    flat = flattened(note)

    check(
        "note registers the dedicated demotion runner",
        "scripts/frontier_koide_mru_demotion_bridge_corollary_2026_06_18.py" in note,
    )
    check(
        "note states the bridge is the only graph-visible retained authority",
        "only graph-visible retained authority" in flat
        and "Graph-visible source authority (one hop)" in note,
    )
    check(
        "note explicitly rejects an independent block-total closure route",
        "It does not claim an independent block-total closure route." in flat
        and "not an independent retained closure route in this note" in flat,
    )
    check(
        "note preserves no-new-axiom / no-audit-verdict boundary",
        "No new axiom, Tier-A admission, audit verdict, or physical scalar-measure bridge" in flat
        and "independent audit lane only" in flat,
    )
    check(
        "note keeps MRU as supplementary conditional support",
        "MRU + weight-class obstruction" in note
        and "Supplementary / alternative framing" in note
        and "not load-bearing" in flat,
    )

    markdown_targets = re.findall(r"\[[^\]]+\]\(([^)]+)\)", note)
    bad_targets = [
        target
        for target in markdown_targets
        if "KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS" in target
        or "KOIDE_MOMENT_RATIO_UNIFORMITY" in target
        or "KOIDE_MRU_WEIGHT_CLASS_OBSTRUCTION" in target
    ]
    check(
        "block-total and MRU context pointers are not graph-visible markdown edges",
        not bad_targets,
        f"bad_targets={bad_targets}" if bad_targets else "",
    )

    retired_old_claims = [
        "Two independent retained theorems on this branch already give `kappa = 2`",
        "The `kappa = 2` gate is therefore carried by two retained independent routes",
        "The block-total Frobenius measure theorem is the independent second closure route.",
        "bridge + block-total Frobenius",
    ]
    present = [claim for claim in retired_old_claims if claim in note]
    check(
        "old overbroad two-route closure claims are absent",
        not present,
        f"present={present}" if present else "",
    )

    block_note = read(BLOCK_TOTAL_NOTE)
    block_flat = flattened(block_note)
    check(
        "block-total source authority itself declares bounded support",
        "**Claim type:** bounded_theorem" in block_note
        and "bounded support theorem" in block_flat,
    )
    check(
        "block-total source authority leaves canonical scalar-measure bridge open",
        "does not derive the scalar-lane `SO(2)` quotient" in block_flat
        and "canonical physical scalar measure" in block_flat,
    )


def check_trace_phase_obstruction() -> None:
    a, x, y = sp.symbols("a x y", real=True)
    b = x + sp.I * y
    bbar = x - sp.I * y

    C = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    H = a * sp.eye(3) + b * C + bbar * (C**2)
    tr_h3 = sp.expand(sp.trace(H**3))

    expected = sp.expand(3 * a**3 + 18 * a * (x**2 + y**2) + 3 * (b**3 + bbar**3))
    phase_term = sp.expand(tr_h3.subs(a, 0))
    wrong_a_scaled_phase = sp.expand(3 * a**3 + 18 * a * (x**2 + y**2) + 3 * a * (b**3 + bbar**3))

    check(
        "tr(H^3) exact formula has phase term 3(b^3+bbar^3), not a-scaled phase",
        sp.simplify(tr_h3 - expected) == 0,
        f"tr(H^3) = {sp.simplify(tr_h3)}",
    )
    check(
        "phase survives at a=0, so it cannot be proportional to a(b^3+bbar^3)",
        sp.simplify(phase_term - 3 * (b**3 + bbar**3)) == 0
        and sp.simplify(tr_h3 - wrong_a_scaled_phase) != 0,
        f"phase_at_a0={sp.simplify(phase_term)}",
    )

    def eigvals(a_val: float, b_val: complex) -> list[float]:
        omega = cmath.exp(2j * math.pi / 3)
        vals = [
            a_val + b_val * omega**k + b_val.conjugate() * omega ** (-k)
            for k in range(3)
        ]
        return [val.real for val in vals]

    a_val = 1.2
    radius = 0.7
    vals_0 = eigvals(a_val, radius)
    vals_rot = eigvals(a_val, radius * cmath.exp(1j * math.pi / 6))
    tr3_0 = sum(v**3 for v in vals_0)
    tr3_rot = sum(v**3 for v in vals_rot)
    det_0 = math.prod(vals_0)
    det_rot = math.prod(vals_rot)
    check(
        "generic SO(2) phase rotation changes scalar spectral observables",
        abs(tr3_0 - tr3_rot) > 1e-6 and abs(det_0 - det_rot) > 1e-6,
        f"tr3: {tr3_0:.6f} vs {tr3_rot:.6f}; det: {det_0:.6f} vs {det_rot:.6f}",
    )


def check_bridge_corollary() -> None:
    a, x, y = sp.symbols("a x y", real=True)
    b = x + sp.I * y
    bbar = x - sp.I * y
    omega = sp.exp(2 * sp.pi * sp.I / 3)

    lambdas = [
        sp.simplify(a + b * omega**k + bbar * sp.conjugate(omega**k))
        for k in range(3)
    ]
    lambdas_real = [sp.simplify(sp.re(val)) for val in lambdas]
    a0 = sp.simplify(sum(lambdas_real) / sp.sqrt(3))
    z = sp.simplify(
        (lambdas_real[0] + sp.conjugate(omega) * lambdas_real[1] + omega * lambdas_real[2])
        / sp.sqrt(3)
    )
    z_abs_sq = sp.simplify(sp.re(z) ** 2 + sp.im(z) ** 2)
    bridge_residual = sp.simplify((a0**2 - 2 * z_abs_sq) - 3 * (a**2 - 2 * (x**2 + y**2)))

    check("bridge gives a0 = sqrt(3) a exactly", sp.simplify(a0 - sp.sqrt(3) * a) == 0)
    check("bridge gives |z|^2 = 3 |b|^2 exactly", sp.simplify(z_abs_sq - 3 * (x**2 + y**2)) == 0)
    check(
        "spectrum residual equals three times operator residual exactly",
        bridge_residual == 0,
    )

    rng_points = [
        (math.sqrt(2) * 0.4, 0.4, 0.0),
        (math.sqrt(2) * math.hypot(-0.3, 0.5), -0.3, 0.5),
        (math.sqrt(2) * math.hypot(1.1, -0.2), 1.1, -0.2),
    ]
    max_spectrum_residual = 0.0
    for a_val, x_val, y_val in rng_points:
        residual = float(
            (a0**2 - 2 * z_abs_sq).subs({a: a_val, x: x_val, y: y_val}).evalf()
        )
        max_spectrum_residual = max(max_spectrum_residual, abs(residual))
    check(
        "operator kappa=2 sample points imply spectrum residual zero",
        max_spectrum_residual < 1e-12,
        f"max_spectrum_residual={max_spectrum_residual:.3e}",
    )


def main() -> None:
    print("Koide MRU demotion bridge-corollary source runner")
    print("=" * 78)
    check_source_boundaries()
    print("\nTrace/SO(2) obstruction checks")
    print("-" * 78)
    check_trace_phase_obstruction()
    print("\nSpectrum-operator bridge corollary checks")
    print("-" * 78)
    check_bridge_corollary()
    print(f"\nSUMMARY: KOIDE MRU DEMOTION BRIDGE-COROLLARY PASS={PASS} FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
