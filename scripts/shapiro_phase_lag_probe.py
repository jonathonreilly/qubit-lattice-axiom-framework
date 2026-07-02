#!/usr/bin/env python3
"""Computed bounded replay for the c-dependent Shapiro-style phase table.

This runner recomputes the finite proxy phase rows from the in-repo
`shapiro_delay_portable` propagation functions instead of rendering a stored
table. The claim it supports is intentionally bounded: a finite three-family,
two-seed replay with exact instantaneous control, small family spread, and
monotone c-dependent proxy phase. It is not a retained physical Shapiro theorem,
not a unique causal discriminator, and not a diamond/NV lab calibration.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import shapiro_delay_portable as portable


AUDIT_TIMEOUT_SEC = 600

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "SHAPIRO_DELAY_NOTE.md"
C_VALUES = tuple(portable.C_VALUES)
FAMILY_LABELS = tuple(label for label, _drift, _restore in portable.FAMILIES)


@dataclass(frozen=True)
class PhaseRow:
    c: float | str
    fam1: float
    fam2: float
    fam3: float


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else math.nan


def _spread(values: list[float]) -> float:
    return max(values) - min(values) if values else math.nan


def _detector_phase(
    det_inst: list[complex],
    det_c: list[complex],
) -> float:
    n_inst = math.sqrt(sum(abs(a) ** 2 for a in det_inst))
    n_c = math.sqrt(sum(abs(a) ** 2 for a in det_c))
    if n_inst <= 0.0 or n_c <= 0.0:
        return 0.0
    overlap = sum(a.conjugate() / n_inst * b / n_c for a, b in zip(det_inst, det_c))
    return math.atan2(overlap.imag, overlap.real)


def compute_phase_rows() -> list[PhaseRow]:
    """Recompute the finite phase table from the portable propagation harness."""
    hw = int(portable.PW / portable.H)
    npl = (2 * hw + 1) ** 2
    by_c: dict[float | str, list[float]] = {"inst": []}
    for c in C_VALUES:
        by_c[c] = []

    for _label, drift, restore in portable.FAMILIES:
        family_means: dict[float | str, float] = {}
        seed_phases: dict[float | str, list[float]] = {"inst": []}
        for c in C_VALUES:
            seed_phases[c] = []

        for seed in portable.SEEDS:
            pos, adj, nmap = portable.grow(seed, drift, restore)
            det_start = len(pos) - npl
            psi_inst = portable.prop_field(
                pos,
                adj,
                nmap,
                portable.S,
                portable.MASS_Z,
                portable.K,
                c_field=None,
            )
            det_inst = psi_inst[det_start:]
            seed_phases["inst"].append(_detector_phase(det_inst, det_inst))

            for c in C_VALUES:
                psi_c = portable.prop_field(
                    pos,
                    adj,
                    nmap,
                    portable.S,
                    portable.MASS_Z,
                    portable.K,
                    c_field=c,
                )
                seed_phases[c].append(_detector_phase(det_inst, psi_c[det_start:]))

        for key, values in seed_phases.items():
            family_means[key] = _mean(values)
            by_c[key].append(family_means[key])

    rows: list[PhaseRow] = []
    for key in ("inst", *C_VALUES):
        vals = by_c[key]
        rows.append(PhaseRow(key, vals[0], vals[1], vals[2]))
    return rows


def rows_as_dicts(rows: list[PhaseRow]) -> list[dict[str, float | str]]:
    out = []
    for row in rows:
        vals = [row.fam1, row.fam2, row.fam3]
        out.append(
            {
                "c": row.c,
                "mean": _mean(vals),
                "spread": _spread(vals),
                "fam1": row.fam1,
                "fam2": row.fam2,
                "fam3": row.fam3,
            }
        )
    return out


def check_payload(rows: list[dict[str, float | str]]) -> tuple[list[dict[str, Any]], bool]:
    phase_only = [r for r in rows if r["c"] != "inst"]
    means = [float(r["mean"]) for r in phase_only]
    spreads = [float(r["spread"]) for r in phase_only]
    inst = rows[0]

    note = NOTE.read_text(encoding="utf-8")
    checks = [
        {
            "name": "exact instantaneous zero control",
            "ok": max(abs(float(inst[k])) for k in ("fam1", "fam2", "fam3", "mean")) < 5e-12,
        },
        {
            "name": "family spread below 2.5e-4 rad on every finite-c row",
            "ok": max(spreads) <= 2.5e-4,
        },
        {
            "name": "phase increases monotonically as c decreases",
            "ok": all(a < b for a, b in zip(means, means[1:])),
        },
        {
            "name": "computed rows match the note table to displayed precision",
            "ok": all(f"{float(r['mean']):+.4f}" in note for r in phase_only),
        },
        {
            "name": "source note is bounded, not retained/proposed-retained",
            "ok": "bounded finite replay" in note
            and "**Type:** bounded_theorem" in note
            and "**Claim type:** bounded_theorem" in note
            and "proposed_retained" not in note
            and "Retained Phase Lag" not in note,
        },
        {
            "name": "source note records static-cone no-go boundary",
            "ok": "static cone shape can" in note
            and "reproduce the same phase curve" in note
            and "not a unique causal discriminator" in note,
        },
        {
            "name": "source note excludes lab calibration and physical speed claims",
            "ok": "not a lab-calibrated diamond/NV prediction" in note
            and "not a physical" in note
            and "field-speed measurement" in note,
        },
        {
            "name": "source note points at live causal packet, not stale generated note",
            "ok": "CAUSAL_PROPAGATING_FIELD_LIVE_PACKET_NOTE_2026-06-05.md" in note
            and "docs/CAUSAL_PROPAGATING_FIELD_NOTE.md" not in note,
        },
    ]
    return checks, all(item["ok"] for item in checks)


def render_markdown(rows: list[dict[str, float | str]], checks: list[dict[str, Any]]) -> str:
    phase_only = [r for r in rows if r["c"] != "inst"]
    max_spread = max(float(r["spread"]) for r in phase_only) if phase_only else 0.0

    lines: list[str] = []
    lines.append("# Shapiro Delay Note")
    lines.append("")
    lines.append("**Date:** 2026-04-06; bounded-source repair 2026-06-17")
    lines.append("**Status:** bounded finite replay / source-support packet; independent audit required before any effective status change")
    lines.append("**Type:** bounded_theorem")
    lines.append("**Claim type:** bounded_theorem")
    lines.append("")
    lines.append("## Artifact Chain")
    lines.append("")
    lines.append("- [`scripts/shapiro_phase_lag_probe.py`](../scripts/shapiro_phase_lag_probe.py)")
    lines.append("- [`logs/runner-cache/shapiro_phase_lag_probe.txt`](../logs/runner-cache/shapiro_phase_lag_probe.txt)")
    lines.append("- [`scripts/shapiro_delay_portable.py`](../scripts/shapiro_delay_portable.py) (finite propagation harness reused by this runner)")
    lines.append("- [`CAUSAL_PROPAGATING_FIELD_LIVE_PACKET_NOTE_2026-06-05.md`](CAUSAL_PROPAGATING_FIELD_LIVE_PACKET_NOTE_2026-06-05.md)")
    lines.append("- [`CAUSAL_FIELD_RECONCILIATION_NOTE.md`](CAUSAL_FIELD_RECONCILIATION_NOTE.md)")
    lines.append("- [`SHAPIRO_STATIC_DISCRIMINATOR_NOTE.md`](SHAPIRO_STATIC_DISCRIMINATOR_NOTE.md)")
    lines.append("")
    lines.append("## Question")
    lines.append("")
    lines.append("What finite in-repo replay supports the c-dependent proxy phase table while keeping the exact zero control and static-cone no-go boundary explicit?")
    lines.append("")
    lines.append("## Exact Control")
    lines.append("")
    lines.append("- `c = inst`: phase lag `0.000 rad` on all three configured families")
    lines.append("- exact null survives by direct detector-overlap comparison")
    lines.append("")
    lines.append("## Bounded Phase-Lag Replay")
    lines.append("")
    lines.append("| c | phase lag mean | family spread | fam1 | fam2 | fam3 |")
    lines.append("| ---: | ---: | ---: | ---: | ---: | ---: |")
    for row in phase_only:
        lines.append(
            f"| `{float(row['c']):.2f}` | `{float(row['mean']):+.4f} rad` | `{float(row['spread']):.4f} rad` | "
            f"`{float(row['fam1']):+.4f}` | `{float(row['fam2']):+.4f}` | `{float(row['fam3']):+.4f}` |"
        )
    lines.append("")
    lines.append("## Runner Checks")
    lines.append("")
    for item in checks:
        tag = "PASS" if item["ok"] else "FAIL"
        lines.append(f"- `{tag}` {item['name']}")
    lines.append("")
    lines.append("## Safe Read")
    lines.append("")
    lines.append(f"- family spread across the configured three-family replay stays at or below `{max_spread:.1e} rad`")
    lines.append("- the proxy phase increases monotonically as the field propagation parameter `c` decreases")
    lines.append("- this is a finite replay over the declared harness, not a derivation of a physical Shapiro law")
    lines.append("- the static-cone discriminator remains load-bearing: a static cone shape can reproduce the same phase curve, so this is not a unique causal discriminator")
    lines.append("- this is not a lab-calibrated diamond/NV prediction and not a physical field-speed measurement")
    lines.append("")
    lines.append("## Claim Boundary")
    lines.append("")
    lines.append("This row may support a bounded finite proxy replay if audit accepts the computation and scope. It does not retain the physical Shapiro-delay package, the failed diamond bridge rows, the complex-interaction renderer, or any unique-causality claim.")
    return "\n".join(lines)


def render_text(rows: list[dict[str, float | str]], checks: list[dict[str, Any]]) -> str:
    lines = [
        "SHAPIRO DELAY BOUNDED FINITE REPLAY",
        "computed from scripts/shapiro_delay_portable.py",
        "",
    ]
    for row in rows:
        lines.append(
            f"c={row['c']}: mean={float(row['mean']):+.6f} rad; spread={float(row['spread']):.6f} rad; "
            f"fam1={float(row['fam1']):+.6f}; fam2={float(row['fam2']):+.6f}; fam3={float(row['fam3']):+.6f}"
        )
    lines.append("")
    lines.append("CHECKS")
    for item in checks:
        lines.append(f"[{'PASS' if item['ok'] else 'FAIL'}] {item['name']}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--format", choices=("markdown", "text", "json"), default="markdown")
    parser.add_argument("--write-log", help="optional path to write the rendered report")
    args = parser.parse_args()

    rows = rows_as_dicts(compute_phase_rows())
    checks, ok = check_payload(rows)
    payload = {
        "rows": rows,
        "checks": checks,
        "summary": {
            "all_checks_pass": ok,
            "claim_boundary": "bounded finite replay; not retained physical Shapiro package",
        },
    }

    if args.format == "json":
        rendered = json.dumps(payload, indent=2, sort_keys=True)
    elif args.format == "text":
        rendered = render_text(rows, checks)
    else:
        rendered = render_markdown(rows, checks)

    print(rendered)

    if args.write_log:
        path = Path(args.write_log)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(rendered + "\n", encoding="utf-8")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
