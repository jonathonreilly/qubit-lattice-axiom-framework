#!/usr/bin/env python3
"""Source-resolved Green-pocket probe on a small exact lattice.

The load-bearing runner claim is now conditional on GREEN-KERNEL-PARAMS:
the kernel parameters, fixture, source strengths, and gain are supplied
premise values. Calibration replay and observable comparisons remain
motivation-tier evidence only.
"""

from __future__ import annotations

import math
import os
import re
import sys
import textwrap
import importlib.util
from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import scripts.minimal_source_driven_field_probe as m  # noqa: E402


# GREEN-KERNEL-PARAMS supplied premise values.
H = 0.5
NL_PHYS = 20
PW = 3
SOURCE_CLUSTER = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
SOURCE_STRENGTHS = tuple(m.SOURCE_STRENGTHS)
GREEN_EPS = 0.5
GREEN_MU = 0.08
DECLARED_GAIN = 2.131774

# Declared calibration target used by the computed-gain hard bar.
FIELD_TARGET_MAX = 0.02

# Frozen motivation reference for the calibration replay display.
MOTIVATION_REFERENCE_GAIN = 2.131774390045413

NOTE_PATH = os.path.join(ROOT, "docs", "SOURCE_RESOLVED_EXACT_GREEN_POCKET_NOTE.md")
EXPECTED_CLAIM_ID = "source_resolved_exact_green_pocket_note"
EXPECTED_CLAIM_TYPE = "bounded_theorem"
PRIMARY_RUNNER = "scripts/source_resolved_exact_green_pocket.py"
MOTIVATION_LABEL = (
    "Calibration replay comparisons are motivation-tier evidence only."
)
NOTE_NEEDLES = [
    "claim_id: source_resolved_exact_green_pocket_note",
    "**Type:** bounded_theorem",
    "**Claim type:** bounded_theorem",
    "**Primary runner:**",
    "## Artifact chain",
    "GREEN-KERNEL-PARAMS (named conditional premise): the Green-kernel",
    "Runner Readout and Motivation Exhibit",
    MOTIVATION_LABEL,
    "The named premises may not be cited as derived.",
]
FATAL_TIERS = ("LOAD-BEARING", "PREMISE", "PARSER", "TEXT")
ALL_TIERS = FATAL_TIERS + ("MOTIVATION",)


def _source_cluster_nodes(lat: m.Lattice3D) -> list[int]:
    gl = lat.nl // 3
    src_y = lat.hw
    src_z = lat.hw + round(m.SOURCE_Z / lat.h)
    nodes: list[int] = []
    for dy, dz in SOURCE_CLUSTER:
        y = src_y + dy
        z = src_z + dz
        if 0 <= y < lat.nw and 0 <= z < lat.nw:
            nodes.append(lat.nmap[(gl, y - lat.hw, z - lat.hw)])
    return nodes


def _source_resolved_green_field(
    lat: m.Lattice3D,
    source_strength: float,
    source_nodes: list[int],
) -> list[list[float]]:
    """Static source-resolved Green-like field on the exact lattice."""
    if not source_nodes:
        return [[0.0 for _ in range(lat.npl)] for _ in range(lat.nl)]

    source_pos = [lat.pos[i] for i in source_nodes]
    field = [[0.0 for _ in range(lat.npl)] for _ in range(lat.nl)]
    for layer in range(lat.nl):
        ls = lat.layer_start[layer]
        for i in range(lat.npl):
            x, y, z = lat.pos[ls + i]
            val = 0.0
            for mx, my, mz in source_pos:
                rho = math.sqrt((x - mx) ** 2 + (y - my) ** 2 + (z - mz) ** 2)
                rho_eps = rho + GREEN_EPS
                val += source_strength * math.exp(-GREEN_MU * rho_eps) / rho_eps
            field[layer][i] = val / len(source_pos)
    return field


def _field_abs_max(layers: list[list[float]]) -> float:
    return max(abs(v) for row in layers for v in row)


def _record(
    totals: dict[str, list[int]],
    tier: str,
    ok: bool,
    message: str,
) -> None:
    status = "[PASS]" if ok else "[FAIL]"
    prefix = f"  {status} "
    wrapped = textwrap.wrap(message, width=100 - len(prefix)) or [""]
    print(prefix + wrapped[0])
    for line in wrapped[1:]:
        print(" " * len(prefix) + line)
    bucket = totals.setdefault(tier, [0, 0])
    bucket[0 if ok else 1] += 1


def _print_totals(totals: dict[str, list[int]]) -> tuple[int, int]:
    print()
    print("TIER ACCOUNTING")
    fatal_pass = 0
    fatal_fail = 0
    motivation_pass = 0
    motivation_fail = 0
    for tier in ALL_TIERS:
        passed, failed = totals.get(tier, [0, 0])
        if tier in FATAL_TIERS:
            fatal_pass += passed
            fatal_fail += failed
        else:
            motivation_pass += passed
            motivation_fail += failed
        print(f"  {tier}: PASS={passed} FAIL={failed}")
    print(f"TOTAL: PASS={fatal_pass} FAIL={fatal_fail}")
    print(f"NONFATAL TOTAL: PASS={motivation_pass} FAIL={motivation_fail}")
    return fatal_pass, fatal_fail


def _citation_graph_module():
    path = Path(ROOT) / "docs" / "audit" / "scripts" / "build_citation_graph.py"
    spec = importlib.util.spec_from_file_location("build_citation_graph", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import parser contract from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _frontmatter_claim_id(note: str) -> str | None:
    if not note.startswith("---\n"):
        return None
    end = note.find("\n---", 4)
    if end < 0:
        return None
    match = re.search(r"^claim_id:\s*(\S+)\s*$", note[4:end], re.MULTILINE)
    return match.group(1) if match else None


def _check_note_contract(totals: dict[str, list[int]]) -> None:
    with open(NOTE_PATH, "r", encoding="utf-8") as handle:
        note = handle.read()

    graph = _citation_graph_module()
    note_path = Path(NOTE_PATH)
    rel_path = note_path.relative_to(Path(ROOT) / "docs").as_posix()

    _record(
        totals,
        "PARSER",
        _frontmatter_claim_id(note) == EXPECTED_CLAIM_ID,
        f"frontmatter claim_id is {EXPECTED_CLAIM_ID}",
    )
    _record(
        totals,
        "PARSER",
        graph.claim_id_from_path(note_path) == EXPECTED_CLAIM_ID,
        f"parser path claim_id is {EXPECTED_CLAIM_ID}",
    )
    _raw_type, claim_type = graph.extract_claim_type_hint(note)
    _record(
        totals,
        "PARSER",
        claim_type == EXPECTED_CLAIM_TYPE,
        f"parser claim type is {EXPECTED_CLAIM_TYPE}",
    )
    _record(
        totals,
        "PARSER",
        graph.extract_runner(note, rel_path) == PRIMARY_RUNNER,
        f"parser primary runner is {PRIMARY_RUNNER}",
    )

    for needle in NOTE_NEEDLES:
        _record(totals, "TEXT", needle in note, f"note contains: {needle}")


def main() -> None:
    totals: dict[str, list[int]] = {}

    lat = m.Lattice3D.build(NL_PHYS, PW, H)
    source_nodes = _source_cluster_nodes(lat)
    zero_field = [[0.0 for _ in range(lat.npl)] for _ in range(lat.nl)]
    free = lat.propagate(zero_field, m.K)
    z_free = m._centroid_z(free, lat)

    print("=" * 84)
    print("SOURCE-RESOLVED EXACT GREEN POCKET")
    print("  conditional fixture theorem under GREEN-KERNEL-PARAMS")
    print("  motivation-tier replay is evidence only, not load-bearing")
    print("=" * 84)
    print(f"h={H}, W={PW}, L={NL_PHYS}, source_cluster={len(source_nodes)} nodes")
    print(
        "field kernel premise: exp(-mu rho_eps)/rho_eps, "
        f"rho_eps=rho+eps, mu={GREEN_MU}, eps={GREEN_EPS}"
    )
    print(f"source strengths premise: {SOURCE_STRENGTHS}")
    print(f"supplied gain premise: {DECLARED_GAIN:.6f}")
    print()

    print("PREMISE CONSISTENCY CHECKS")
    _record(totals, "PREMISE", H == 0.5, "lattice h premise is 0.5")
    _record(totals, "PREMISE", PW == 3, "lattice W premise is 3")
    _record(totals, "PREMISE", NL_PHYS == 20, "lattice L premise is 20")
    _record(totals, "PREMISE", len(source_nodes) == 4, "source cluster clips to 4 nodes")
    _record(
        totals,
        "PREMISE",
        SOURCE_STRENGTHS == (0.001, 0.002, 0.004, 0.008),
        "source-strength premise is {0.001, 0.002, 0.004, 0.008}",
    )
    _record(totals, "PREMISE", GREEN_MU == 0.08, "kernel mu premise is 0.08")
    _record(totals, "PREMISE", GREEN_EPS == 0.5, "kernel eps premise is 0.5")
    _record(totals, "PREMISE", DECLARED_GAIN == 2.131774, "gain premise is 2.131774")
    print()

    ref_raw = _source_resolved_green_field(lat, max(SOURCE_STRENGTHS), source_nodes)
    ref_max = _field_abs_max(ref_raw)
    replay_gain = FIELD_TARGET_MAX / ref_max if ref_max > 1e-30 else 1.0
    gain = DECLARED_GAIN

    print("MOTIVATION-TIER CALIBRATION REPLAY")
    print(f"  {MOTIVATION_LABEL}")
    print(f"  target max |f|: {FIELD_TARGET_MAX}")
    print(f"  replayed calibration gain: {replay_gain:.9e}")
    print(f"  supplied gain consumed by hard bars: {gain:.9e}")
    _record(
        totals,
        "MOTIVATION",
        abs(replay_gain - MOTIVATION_REFERENCE_GAIN) <= 5e-13,
        "replayed calibration gain matches the frozen motivation reference",
    )
    print()

    zero_dyn = _source_resolved_green_field(lat, 0.0, source_nodes)
    zero_amps = lat.propagate([[gain * v for v in row] for row in zero_dyn], m.K)
    zero_delta = m._centroid_z(zero_amps, lat) - z_free

    print("REDUCTION CHECK")
    print(f"  zero-source dynamic shift: {zero_delta:+.6e}")
    print()

    print("LOAD-BEARING REPLAY TABLE")
    print("  The Green readouts below feed hard-bar assertions.")
    print(f"{'s':>8s} {'inst':>12s} {'green':>12s} {'green/inst':>11s} {'max|f|':>12s}")
    print("-" * 70)

    inst_vals: list[float] = []
    green_vals: list[float] = []
    ratios: list[float] = []

    for s in SOURCE_STRENGTHS:
        inst_field = m._instantaneous_field_layers(lat, s, m.SOURCE_Z)
        raw_green = _source_resolved_green_field(lat, s, source_nodes)
        green_field = [[gain * v for v in row] for row in raw_green]

        inst_amps = lat.propagate(inst_field, m.K)
        green_amps = lat.propagate(green_field, m.K)

        inst_delta = m._centroid_z(inst_amps, lat) - z_free
        green_delta = m._centroid_z(green_amps, lat) - z_free
        ratio = green_delta / inst_delta if abs(inst_delta) > 1e-30 else float("nan")

        inst_vals.append(inst_delta)
        green_vals.append(green_delta)
        ratios.append(abs(ratio))

        print(
            f"{s:8.4f} {inst_delta:+12.6e} {green_delta:+12.6e} "
            f"{ratio:11.3f} {_field_abs_max(green_field):12.6e}"
        )

    inst_alpha = m._fit_power(list(SOURCE_STRENGTHS), inst_vals)
    green_alpha = m._fit_power(list(SOURCE_STRENGTHS), green_vals)
    toward = sum(1 for v in green_vals if v > 0)
    mean_ratio = sum(ratios) / len(ratios)

    print()
    print("LOAD-BEARING FIT READOUT")
    print("  green_alpha, TOWARD, and mean_ratio feed hard-bar assertions.")
    if inst_alpha is None:
        print("  instantaneous F~M exponent: n/a")
    else:
        print(f"  instantaneous F~M exponent: {inst_alpha:.2f}")
    if green_alpha is None:
        print("  green-kernel F~M exponent: n/a")
    else:
        print(f"  green-kernel F~M exponent: {green_alpha:.2f}")
    print(f"  TOWARD rows: {toward}/{len(green_vals)}")
    print(f"  mean |green/inst| ratio: {mean_ratio:.3f}")
    print()

    print("LOAD-BEARING HARD-BAR ASSERTIONS")
    print("  Conditional on GREEN-KERNEL-PARAMS; no parameter derivation claimed.")
    _record(
        totals,
        "LOAD-BEARING",
        abs(zero_delta) <= 1e-12,
        f"zero-source reduction |zero_delta|={abs(zero_delta):.3e} <= 1e-12",
    )

    expected_rows = len(green_vals)
    _record(
        totals,
        "LOAD-BEARING",
        toward == expected_rows,
        f"TOWARD sign {toward}/{expected_rows}",
    )

    green_ok = green_alpha is not None and 0.95 <= green_alpha <= 1.05
    green_msg = (
        f"green F~M exponent {green_alpha:.3f} in [0.95, 1.05]"
        if green_alpha is not None
        else "green F~M exponent None not in [0.95, 1.05]"
    )
    _record(totals, "LOAD-BEARING", green_ok, green_msg)

    _record(
        totals,
        "LOAD-BEARING",
        1.10 <= mean_ratio <= 1.40,
        f"mean |green/inst| ratio {mean_ratio:.3f} in [1.10, 1.40]",
    )
    gain_ok = 0.0 < replay_gain < 100.0 and abs(replay_gain - gain) <= 5e-7
    gain_msg = (
        f"computed gain is finite and matches DECLARED_GAIN within 5e-7 "
        f"({replay_gain:.9e})"
    )
    _record(totals, "LOAD-BEARING", gain_ok, gain_msg)
    print()

    print("PARSER AND TEXT CONTRACT CHECKS")
    _check_note_contract(totals)
    print()

    print("DETERMINISM STATEMENT")
    print("  uncounted: runner uses no random seed, no RNG branch, no network,")
    print("  and fixed loops over declared finite inputs.")

    _, fatal_fail = _print_totals(totals)
    print("DECLARATION: GREEN-KERNEL-PARAMS is supplied; kernel, gain, source")
    print("geometry, and hard-bar windows are not claimed as derived.")
    if fatal_fail > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
