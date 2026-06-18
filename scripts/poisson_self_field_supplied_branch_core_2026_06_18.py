#!/usr/bin/env python3
"""Supplied-branch core certificate for POISSON_SELF_FIELD_NOTE.

This runner does not derive a gravity law. It verifies that, once the 2D
Poisson branch and longitudinal factor are supplied, the finite computation
reported by the parent note is internally consistent and source-boundaried.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1800

import importlib.util
import inspect
import math
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PARENT_RUNNER = REPO_ROOT / "scripts" / "poisson_self_field.py"
PARENT_NOTE = REPO_ROOT / "docs" / "POISSON_SELF_FIELD_NOTE.md"
CORE_NOTE = (
    REPO_ROOT
    / "docs"
    / "POISSON_SELF_FIELD_SUPPLIED_BRANCH_CORE_BOUNDED_NOTE_2026-06-18.md"
)


def load_parent():
    spec = importlib.util.spec_from_file_location("poisson_self_field", PARENT_RUNNER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {PARENT_RUNNER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Score:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, ok: bool, detail: str = "") -> None:
        if ok:
            self.passed += 1
            status = "PASS"
        else:
            self.failed += 1
            status = "FAIL"
        suffix = f" -- {detail}" if detail else ""
        print(f"{status}: {label}{suffix}")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def finite_poisson_residual(psf) -> tuple[float, float]:
    hw = int(psf.PW / psf.H)
    nw = 2 * hw + 1
    gl = psf.NL // 3
    iz_src = round(psf.MASS_Z / psf.H)
    x_src = gl * psf.H
    fields = psf._make_poisson_field({}, psf.S, psf.MASS_Z)
    max_residual = 0.0
    max_boundary = 0.0

    for layer, values in enumerate(fields):
        dx = abs(layer * psf.H - x_src)
        eff_s = psf.S / (dx + 0.1) * psf.H * psf.H

        def val(iy: int, iz: int) -> float:
            return values[(iy + hw) * nw + (iz + hw)]

        for iy in range(-hw, hw + 1):
            for iz in range(-hw, hw + 1):
                on_boundary = iy in (-hw, hw) or iz in (-hw, hw)
                if on_boundary:
                    max_boundary = max(max_boundary, abs(val(iy, iz)))
                    continue
                lap = (
                    val(iy - 1, iz)
                    + val(iy + 1, iz)
                    + val(iy, iz - 1)
                    + val(iy, iz + 1)
                    - 4.0 * val(iy, iz)
                )
                source = eff_s if (iy == 0 and iz == iz_src) else 0.0
                max_residual = max(max_residual, abs(lap + source))
    return max_residual, max_boundary


def gravity_and_fm(psf) -> tuple[dict[str, float], dict[str, float]]:
    hw = int(psf.PW / psf.H)
    npl = (2 * hw + 1) ** 2
    fl_zero = [[0.0] * npl for _ in range(psf.NL)]
    strengths = [0.001, 0.002, 0.004, 0.008]
    gravity_delta: dict[str, float] = {}
    slopes: dict[str, float] = {}

    for label, drift, restore in psf.FAMILIES:
        pos, adj, nmap = psf.grow(0, drift, restore)
        free = psf._prop_beam(pos, adj, nmap, fl_zero, psf.K)
        z_free = psf._cz(free, pos)
        fl = psf._make_poisson_field(nmap, psf.S, psf.MASS_Z)
        g = psf._prop_beam(pos, adj, nmap, fl, psf.K)
        gravity_delta[label] = psf._cz(g, pos) - z_free

        deltas = []
        for s in strengths:
            fl = psf._make_poisson_field(nmap, s, psf.MASS_Z)
            g = psf._prop_beam(pos, adj, nmap, fl, psf.K)
            deltas.append(abs(psf._cz(g, pos) - z_free))
        lx = [math.log(x) for x in strengths]
        ly = [math.log(y) for y in deltas if y > 1e-15]
        mx = sum(lx[: len(ly)]) / len(ly)
        my = sum(ly) / len(ly)
        sxx = sum((x - mx) ** 2 for x in lx[: len(ly)])
        slopes[label] = sum(
            (x - mx) * (y - my) for x, y in zip(lx[: len(ly)], ly)
        ) / sxx

    return gravity_delta, slopes


def born_ratio(psf) -> float:
    pos, adj, nmap = psf.grow(0, 0.2, 0.7)
    fl_born = psf._make_poisson_field(nmap, psf.S, psf.MASS_Z)

    def pb(slits: list[int]) -> float:
        srcs = [
            (nmap.get((0, s, 0)) or nmap.get((1, s, 0)), 1.0 + 0j)
            for s in slits
        ]
        srcs = [(i, a) for i, a in srcs if i is not None]
        amps = psf._prop_beam(pos, adj, nmap, fl_born, psf.K, sources=srcs)
        return psf._dp(amps, pos)

    p123 = pb([-1, 0, 1])
    p12 = pb([-1, 0])
    p13 = pb([-1, 1])
    p23 = pb([0, 1])
    p1 = pb([-1])
    p2 = pb([0])
    p3 = pb([1])
    i3 = p123 - p12 - p13 - p23 + p1 + p2 + p3
    return abs(i3) / max(p123, 1e-300)


def null_delta(psf) -> float:
    hw = int(psf.PW / psf.H)
    npl = (2 * hw + 1) ** 2
    fl_zero = [[0.0] * npl for _ in range(psf.NL)]
    pos, adj, nmap = psf.grow(0, 0.2, 0.7)
    free = psf._prop_beam(pos, adj, nmap, fl_zero, psf.K)
    z_free = psf._cz(free, pos)
    fl0 = psf._make_poisson_field(nmap, 0.0, psf.MASS_Z)
    g0 = psf._prop_beam(pos, adj, nmap, fl0, psf.K)
    return psf._cz(g0, pos) - z_free


def main() -> int:
    print("=" * 72)
    print("POISSON SUPPLIED-BRANCH CORE CERTIFICATE")
    print("=" * 72)

    score = Score()
    psf = load_parent()
    parent_note = read_text(PARENT_NOTE)
    core_note = read_text(CORE_NOTE)
    parent_source = read_text(PARENT_RUNNER)
    make_poisson_field_source = inspect.getsource(psf._make_poisson_field)

    required_core_phrases = [
        "not a retained derivation of gravity",
        "PDE, source, boundary condition, normalization, physical gravity readout, and",
        "longitudinal falloff remain supplied or imposed",
        "This split adds no repo-wide axiom",
    ]
    for phrase in required_core_phrases:
        score.check(
            f"core note contains firewall phrase: {phrase[:54]}",
            phrase in core_note,
        )

    score.check(
        "parent note cites supplied-branch core split",
        "POISSON_SELF_FIELD_SUPPLIED_BRANCH_CORE_BOUNDED_NOTE_2026-06-18.md"
        in parent_note,
    )
    score.check(
        "parent note uses current Born cache value",
        "Born<1.5e-15" in parent_note
        and "1.32e-15" not in parent_note
        and "7.07e-16" not in parent_note,
    )
    score.check(
        "parent runner no longer advertises retained parent results",
        "Reproduces all retained results" not in parent_source,
    )
    score.check(
        "longitudinal denominator remains formula-level source",
        "s / (dx + 0.1) * H * H" in make_poisson_field_source,
    )

    max_residual, max_boundary = finite_poisson_residual(psf)
    score.check(
        "finite 2D Poisson residual within declared budget",
        max_residual <= 3.19e-5,
        f"max_residual={max_residual:.8e}",
    )
    score.check(
        "zero transverse Dirichlet boundary remains exact",
        max_boundary == 0.0,
        f"max_boundary={max_boundary:.1e}",
    )

    gravity_delta, slopes = gravity_and_fm(psf)
    for label in ("Fam1", "Fam2", "Fam3"):
        score.check(
            f"{label} centroid shift is TOWARD",
            gravity_delta[label] > 0.0,
            f"delta={gravity_delta[label]:+.6f}",
        )
        score.check(
            f"{label} F~M remains near linear",
            slopes[label] >= 0.9990,
            f"F~M={slopes[label]:.4f}",
        )

    born = born_ratio(psf)
    score.check(
        "Born cancellation is at machine precision on active Poisson branch",
        born <= 1.5e-15,
        f"Born |I3|/P={born:.2e}",
    )

    nd = null_delta(psf)
    score.check("s=0 null branch is exact", nd == 0.0, f"delta={nd:+.6e}")

    print("-" * 72)
    print(f"SUMMARY: PASS={score.passed} FAIL={score.failed}")
    if score.failed:
        print("VERDICT: FAIL -- supplied-branch core is not audit-ready")
        return 1
    print("VERDICT: PASS -- bounded supplied-branch core is audit-ready")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
