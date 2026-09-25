#!/usr/bin/env python3
"""Scratch-copy mutations against the current 15-cell and central runners."""
from __future__ import annotations

import ast
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent

MUTATIONS = (
    ("scripts/postmark_electric_moving_index_cell_symbol_2026_09_24.py",
     "cell_wrong_signed_residue",
     "POS_LEFT = (0, 1, 0, 1, 1, 1, 2, 1, 2, 2, 2, 3, 2, 3, 3)",
     "POS_LEFT = (0, 2, 0, 1, 1, 1, 2, 1, 2, 2, 2, 3, 2, 3, 3)"),
    ("scripts/postmark_electric_moving_index_cell_symbol_2026_09_24.py",
     "cell_wrong_principal_diagonal",
     "matrix[np.diag_indices(15)] = 2 * w",
     "matrix[np.diag_indices(15)] = 2.01 * w"),
    ("scripts/postmark_electric_moving_index_cell_symbol_2026_09_24.py",
     "cell_wrong_first_order_diagonal",
     "d1 = alpha(left[r], u) + alpha(previous_right[r], u)",
     "d1 = alpha(left[r], u) + alpha(previous_right[r], u) + 1"),
    ("scripts/postmark_electric_two_band_central_match_2026_09_24.py",
     "central_wrong_projected_derivative",
     "target = sp.diag(sigma*sp.sqrt(3)/15, -sigma*sp.sqrt(3)/15)",
     "target = sp.diag(sigma*sp.sqrt(3)/16, -sigma*sp.sqrt(3)/16)"),
    ("scripts/postmark_electric_two_band_central_match_2026_09_24.py",
     "central_wrong_outer_detuning",
     "sqrt3 * (1-u**2) / 15,\n         u * (3*u - 11)",
     "sqrt3 * (1-u**2) / 16,\n         u * (3*u - 11)"),
    ("scripts/postmark_electric_two_band_central_match_2026_09_24.py",
     "central_wrong_projection_coefficient",
     "-27*k**2 - 33*k - sp.Rational(62, 5)",
     "-27*k**2 - 32*k - sp.Rational(62, 5)"),
    ("scripts/postmark_electric_two_band_central_match_2026_09_24.py",
     "central_wrong_casimir_second_order",
     "outer_to_second_order = 1-u**2+h*alpha-h**2*(u-a)*(u-a-1)",
     "outer_to_second_order = 1-u**2+h*alpha-h**2*(u-a)*(u-a-1) + h**2"),
    ("scripts/postmark_electric_two_band_central_match_2026_09_24.py",
     "central_wrong_interface_identity",
     "if sp.simplify(f(-1)-f(0)) != 0:",
     "if sp.simplify(f(-1)-f(0)) == 0:"),
    ("scripts/postmark_electric_two_band_central_match_2026_09_24.py",
     "central_wrong_physical_hop_helper",
     "scripts/core_derivation.py::out[q2] -= amp1 * amp2",
     "scripts/core_derivation.py::out[q2] -= 2 * amp1 * amp2"),
)


def declared_inputs(text: str) -> tuple[str, ...]:
    tree = ast.parse(text)
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
                isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS"
                for target in node.targets):
            return tuple(ast.literal_eval(node.value))
    raise RuntimeError("runner has no literal AUDIT_INPUT_PATHS")


def main() -> int:
    results = []
    hashes = {}
    for runner_rel, name, before, after in MUTATIONS:
        runner = ROOT / runner_rel
        source = runner.read_text()
        hashes[runner_rel] = hashlib.sha256(runner.read_bytes()).hexdigest()
        with tempfile.TemporaryDirectory(prefix=f"mutation_{name}_") as temp:
            scratch = Path(temp)
            for rel in declared_inputs(source):
                target = scratch / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ROOT / rel, target)
            target_runner = scratch / runner_rel
            target_runner.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(runner, target_runner)
            if "core_derivation.py" in before:
                core = scratch / "scripts/core_derivation.py"
                core_text = core.read_text()
                old, new = before.split("::", 1)[1], after.split("::", 1)[1]
                if core_text.count(old) != 1:
                    raise RuntimeError((name, "core anchor count", core_text.count(old)))
                core.write_text(core_text.replace(old, new, 1))
            else:
                text = target_runner.read_text()
                if text.count(before) < 1:
                    raise RuntimeError((name, "runner anchor count", text.count(before)))
                target_runner.write_text(text.replace(before, after, 1))
            completed = subprocess.run([sys.executable, str(target_runner)], cwd=scratch,
                                       capture_output=True, text=True, timeout=300)
        log = OUT / f"{name}.log"
        log.write_text(completed.stdout + "\n--- stderr ---\n" + completed.stderr)
        failure = next((line.strip() for line in reversed(completed.stderr.splitlines())
                        if line.strip()), "")
        results.append({"runner": runner_rel, "mutation": name,
                        "exit_code": completed.returncode,
                        "expected_failure_observed": completed.returncode != 0,
                        "failure_signature": failure,
                        "log": str(log.relative_to(ROOT))})

    report = {"source_revision": "0e6ad8285096ed668816f18caaa6fbbfbd9c50e8",
              "runner_sha256": hashes, "mutations": results,
              "all_expected_failures_observed": all(x["expected_failure_observed"]
                                                     for x in results),
              "interpretation": "Scratch-copy checks only; not independent validation."}
    (OUT / "CELL_CENTRAL_MUTATION_CHECKS.json").write_text(
        json.dumps(report, indent=2) + "\n")
    print(json.dumps({"runner_sha256": hashes,
                      "mutations": len(results),
                      "all_expected_failures_observed": report["all_expected_failures_observed"]},
                     indent=2))
    return 0 if report["all_expected_failures_observed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
