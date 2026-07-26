#!/usr/bin/env python3
"""Audit harness for the bounded persistent-record side-bit comparison."""

from __future__ import annotations

import contextlib
import io
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.persistent_record_matched_compare import main as matched_compare_main

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "scripts/persistent_record_matched_compare.py",
    "scripts/persistent_record_overlap_kernel.py",
    "scripts/density_matrix_analysis.py",
    "scripts/entangling_env_decoherence.py",
    "scripts/generative_causal_dag_interference.py",
    "scripts/graph_memory_scar_decoherence.py",
)


def check(label: str, passed: bool, detail: str) -> bool:
    print(f"[C] {'PASS' if passed else 'FAIL'} {label}: {detail}")
    return passed


def main() -> int:
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        results = matched_compare_main([
            "--seeds", "2",
            "--gamma", "1.0",
            "--methods",
            "node,pr_trace,pr_soft,pr_side_trace,pr_side_soft",
        ])
    transcript = output.getvalue()
    print(transcript, end="")

    node = results.get("node") or []
    base_soft = results.get("pr_g1") or []
    side_soft = results.get("pr_side_g1") or []
    complete = len(node) == len(base_soft) == len(side_soft) == 3
    outcomes = [
        check(
            "side_bit_rows_complete",
            complete,
            f"node={node} base_soft={base_soft} side_soft={side_soft}",
        )
    ]
    if complete:
        outcomes.extend([
            check(
                "side_bit_modestly_improves_soft_overlap",
                all(side < base for side, base in zip(side_soft, base_soft)),
                f"base_soft={base_soft} side_soft={side_soft}",
            ),
            check(
                "side_bit_does_not_beat_node_label",
                all(side > baseline for side, baseline in zip(side_soft, node)),
                f"node={node} side_soft={side_soft}; lower purity is better",
            ),
        ])
    print(f"TOTAL: PASS={sum(outcomes)} FAIL={len(outcomes) - sum(outcomes)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
