#!/usr/bin/env python3
"""Narrow guard-reconciliation certificate for the N=100, q=0.03 pocket."""

from __future__ import annotations

import contextlib
import io
import os
import sys
from pathlib import Path


os.environ["DENSE_GUARD_LAYERS"] = "100"
os.environ["DENSE_GUARD_QS"] = "0.03"
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.dense_prune_channel_count_guard import main  # noqa: E402


def _extract_row(stdout: str, mode: str) -> dict[str, float]:
    for line in stdout.splitlines():
        parts = line.split()
        if len(parts) == 17 and parts[0] == "100" and parts[1] == mode and parts[2] == "0.03":
            return {
                "valid": float(parts[3]),
                "pur_b": float(parts[4]),
                "pur_p": float(parts[5]),
                "d_pur": float(parts[6]),
                "grav_b": float(parts[7]),
                "grav_p": float(parts[8]),
                "d_grav": float(parts[9]),
                "pur_se": float(parts[10]),
                "grav_se": float(parts[11]),
                "eff_b": float(parts[12]),
                "eff_p": float(parts[13]),
                "removed": float(parts[14]),
                "flip": float(parts[15]),
                "corr_eff": float(parts[16]),
            }
    raise AssertionError(f"missing N=100 q=0.03 {mode} row")


def _assert_certificate(stdout: str) -> None:
    plain = _extract_row(stdout, "plain")
    guarded = _extract_row(stdout, "guarded")

    assert plain["valid"] >= 4, plain
    assert guarded["valid"] >= 4, guarded
    assert plain["flip"] >= 1, plain
    assert guarded["flip"] == 0, guarded
    assert plain["d_grav"] < -1.0, plain
    assert abs(guarded["d_grav"]) < abs(plain["d_grav"]), (plain, guarded)
    assert guarded["d_pur"] > -0.01, guarded
    assert guarded["eff_p"] / guarded["eff_b"] >= 0.95, guarded
    assert plain["eff_p"] / plain["eff_b"] < 0.55, plain
    assert guarded["removed"] < plain["removed"], (plain, guarded)


def run_certificate() -> None:
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        main()
    stdout = buffer.getvalue()
    print(stdout, end="")
    _assert_certificate(stdout)
    print()
    print("CERTIFICATE PASS: N=100 q=0.03 aggregate guard check passed")
    print("BOUNDARY: gravity flips are removed at a small bounded purity cost")


if __name__ == "__main__":
    run_certificate()
