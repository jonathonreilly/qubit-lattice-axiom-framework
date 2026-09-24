#!/usr/bin/env python3
"""Scratch-copy mutation checks for the current exact-side runner."""
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RUNNER = ROOT / "scripts/postmark_electric_exact_side_fixed_index_kernel_2026_09_24.py"
CORE = ROOT / "scripts/core_derivation.py"
OUT = Path(__file__).resolve().parent / "exact_kernel"
OUT.mkdir(parents=True, exist_ok=True)

MUTATIONS = (
    ("label_reflection",
     "if NEG_LEFT[r] != -POS_LEFT[r] - 1:",
     "if NEG_LEFT[r] == -POS_LEFT[r] - 1:"),
    ("diagonal_coefficient",
     "diagonal[i] = weight(left) + weight(previous_right)",
     "diagonal[i] = weight(left) - weight(previous_right)"),
    ("staggered_link_sign",
     "return lo, hi, diagonal, -positive_links, positive_links",
     "return lo, hi, diagonal, positive_links, positive_links"),
    ("generator_phase_sign",
     "np.exp(-1j * time * (eigenvalues**2 - casimir * eigenvalues))",
     "np.exp(+1j * time * (eigenvalues**2 - casimir * eigenvalues))"),
    ("kernel_phase_order",
     "before_character = evolve(eigenvalues, eigenvectors, basis_b, plus)",
     "before_character = evolve(eigenvalues, eigenvectors, basis_b, minus)"),
    ("character_sign",
     "omega = np.exp(2j * np.pi * np.remainder(nodes, 3) / 3)",
     "omega = np.exp(-2j * np.pi * np.remainder(nodes, 3) / 3)"),
    ("projector_formula",
     "observable = (1.0 + omega + np.conjugate(omega)) / 3.0",
     "observable = (1.0 + omega + np.conjugate(omega)) / 2.0"),
    ("bessel_character_prefactor",
     "formula = (np.exp(1j * b * phi) * (1j ** m)",
     "formula = (np.exp(-1j * b * phi) * (1j ** m)"),
    ("arcsine_low_mass_formula",
     "np.arccos(1.0 - epsilon / 2.0) / np.pi",
     "np.arccos(1.0 - epsilon) / np.pi"),
)


def main() -> int:
    results = []
    for name, before, after in MUTATIONS:
        with tempfile.TemporaryDirectory(prefix=f"mutation_{name}_") as temp:
            scratch = Path(temp)
            scripts = scratch / "scripts"
            scripts.mkdir()
            runner = scripts / RUNNER.name
            shutil.copy2(RUNNER, runner)
            shutil.copy2(CORE, scripts / CORE.name)
            source = runner.read_text()
            if source.count(before) != 1:
                raise RuntimeError((name, "expected mutation anchor once", source.count(before)))
            runner.write_text(source.replace(before, after, 1))
            completed = subprocess.run(
                [sys.executable, str(runner)],
                cwd=scratch,
                capture_output=True,
                text=True,
                timeout=300,
            )
        stdout_path = OUT / f"{name}.stdout"
        stderr_path = OUT / f"{name}.stderr"
        stdout_path.write_text(completed.stdout)
        stderr_path.write_text(completed.stderr)
        detected = completed.returncode != 0
        failure = next(
            (line.strip() for line in reversed(completed.stderr.splitlines())
             if line.strip()),
            "",
        )
        results.append({
            "mutation": name,
            "before": before,
            "after": after,
            "exit_code": completed.returncode,
            "detected": detected,
            "failure": failure,
            "stdout_path": str(stdout_path),
            "stderr_path": str(stderr_path),
        })
    report = {
        "runner_sha256": hashlib.sha256(RUNNER.read_bytes()).hexdigest(),
        "mutations": results,
        "all_detected": all(row["detected"] for row in results),
    }
    target = OUT / "MUTATION_CHECKS.json"
    target.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"runner_sha256": report["runner_sha256"],
                      "all_detected": report["all_detected"],
                      "mutations": len(results),
                      "failed_to_detect": [
                          row["mutation"] for row in results
                          if not row["detected"]]}, indent=2))
    return 0 if report["all_detected"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
