#!/usr/bin/env python3
"""Exercise two load-bearing Airy-runner checks on scratch source copies."""
from __future__ import annotations

from pathlib import Path
import tempfile


ROOT = Path(__file__).resolve().parents[3]
RUNNER = ROOT / "scripts" / "postmark_electric_simple_turning_point_airy_scale_transfer_2026_09_24.py"
SOURCE = RUNNER.read_text(encoding="utf-8")


def must_reject(label: str, needle: str, replacement: str) -> None:
    if SOURCE.count(needle) != 1:
        raise RuntimeError(f"{label}: expected one mutation site, found {SOURCE.count(needle)}")
    mutated = SOURCE.replace(needle, replacement)
    with tempfile.TemporaryDirectory(prefix="airy-runner-mutation-") as temp:
        scratch = Path(temp) / "mutated_runner.py"
        scratch.write_text(mutated, encoding="utf-8")
        namespace = {"__name__": "mutation_test", "__file__": str(scratch)}
        exec(compile(mutated, str(scratch), "exec"), namespace)
        try:
            namespace["symbolic_turning_checks"]()
        except ArithmeticError as exc:
            print(f"PASS {label}: rejected with {exc}")
            return
    raise AssertionError(f"{label}: load-bearing mutation escaped")


def main() -> None:
    must_reject(
        "factor-of-two Airy slope",
        "airy_coefficient = 800 * a / lam_at_a",
        "airy_coefficient = 400 * a / lam_at_a",
    )
    must_reject(
        "finite-spin edge-shift sign",
        "expected_shift = sp.simplify(\n        -lam_at_a * g1_edge.subs(u, a) / (80 * a)\n    )",
        "expected_shift = sp.simplify(\n        lam_at_a * g1_edge.subs(u, a) / (80 * a)\n    )",
    )


if __name__ == "__main__":
    main()
