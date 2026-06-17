#!/usr/bin/env python3
"""Implementation-fidelity verifier for the 3D inverse-square helper wrapper.

This verifies the audit-relevant interface surface of
`scripts/lattice_3d_inverse_square_kernel.py`: constants, helper function
presence, the inverse-square propagator expression, and the SHA-current cached
runner output. It does not derive an inverse-square tail theorem or promote any
downstream physics claim.
"""

from __future__ import annotations

import ast
import hashlib
import importlib.util
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = "docs/LATTICE_3D_INVERSE_SQUARE_KERNEL_HELPER_NOTE_2026-04-04.md"
RUNNER = "scripts/lattice_3d_inverse_square_kernel.py"
CACHE = "logs/runner-cache/lattice_3d_inverse_square_kernel.txt"

PASS = 0
FAIL = 0


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def sha256_file(rel: str) -> str:
    return hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def cache_meta(cache_text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in cache_text.splitlines():
        if ": " in line and not line.startswith("-----"):
            key, value = line.split(": ", 1)
            if key in {"runner", "runner_sha256", "exit_code", "status"}:
                out[key] = value.strip()
    return out


def load_runner_module():
    spec = importlib.util.spec_from_file_location(
        "lattice_3d_inverse_square_kernel_under_test",
        ROOT / RUNNER,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {RUNNER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def function_source(source: str, function_name: str) -> str:
    tree = ast.parse(source)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == function_name:
            return ast.get_source_segment(source, node) or ""
    return ""


def main() -> int:
    print("3D inverse-square helper implementation-fidelity verifier")
    print("=" * 72)

    note = read(NOTE)
    source = read(RUNNER)
    cache_text = read(CACHE)
    module = load_runner_module()

    note_flat = " ".join(note.split())
    check("note names implementation-fidelity packet",
          "2026-06-17 implementation-fidelity packet" in note)
    check("note preserves wrapper-only boundary",
          "may not be cited as a derivation of an inverse-square kernel" in note_flat
          and "implementation-fidelity certificate only" in note_flat)
    check("note links verifier runner",
          "lattice_3d_inverse_square_kernel_helper_fidelity_2026_06_17.py" in note)
    check("note links verifier cache",
          "lattice_3d_inverse_square_kernel_helper_fidelity_2026_06_17.txt" in note)

    required_functions = {
        "build_family",
        "barrier_metrics",
        "no_barrier_distance",
        "fit_power",
        "propagate_inverse_square",
        "make_field",
    }
    tree = ast.parse(source)
    actual_functions = {node.name for node in tree.body if isinstance(node, ast.FunctionDef)}
    for name in sorted(required_functions):
        check(f"{RUNNER} defines {name}", name in actual_functions)
        check(f"{RUNNER} exposes callable {name}", callable(getattr(module, name, None)))

    expected_constants = {
        "PHYS_L": 12.0,
        "PHYS_W": 6.0,
        "PHYS_CONNECTIVITY": 3.0,
        "STRENGTH": 5e-5,
        "MASS_Z_VALUES": [2.0, 3.0, 4.0, 5.0, 6.0, 7.0],
        "H_VALUES": [1.0, 0.5],
        "SLITS_PHYS": [(2.0, 0.0), (-2.0, 0.0), (0.0, 1.0)],
    }
    for name, expected in expected_constants.items():
        check(f"{RUNNER} constant {name}", getattr(module, name, None) == expected,
              f"live={getattr(module, name, None)!r}")

    propagate_src = " ".join(function_source(source, "propagate_inverse_square").split())
    check("propagator uses inverse-square free-kernel attenuation",
          "* w / (L * L)" in propagate_src)
    check("propagator preserves spent-delay action form",
          "ret = math.sqrt(max(dl * dl - L * L, 0.0))" in propagate_src
          and "act = dl - ret" in propagate_src)
    check("source helper uses declared finite field regularization",
          "field[i] = strength / (math.sqrt(" in source and "+ 0.1)" in source)

    pos, adj, nl, hw, nmap, det, barrier_layer, barrier, slit_indices, blocked, gl, span = module.build_family(1.0)
    check("build_family h=1.0 uses width-6 geometry",
          nl == 13 and hw == 6 and span == 3 and len(det) == 169,
          f"nl={nl}, hw={hw}, span={span}, det={len(det)}")
    check("build_family h=1.0 declares three slit indices",
          len(slit_indices) == 3 and len(set(slit_indices)) == 3)
    check("build_family h=1.0 blocks barrier except slits",
          len(blocked) == len(barrier) - len(slit_indices),
          f"blocked={len(blocked)}, barrier={len(barrier)}, slits={len(slit_indices)}")
    slope, r2 = module.fit_power([(2.0, 0.25), (4.0, 0.0625), (8.0, 0.015625)])
    check("fit_power recovers exact inverse-square exponent on synthetic data",
          abs(slope + 2.0) < 1e-12 and abs(r2 - 1.0) < 1e-12,
          f"slope={slope:.12f}, r2={r2:.12f}")

    meta = cache_meta(cache_text)
    check("main runner cache records runner path", meta.get("runner") == RUNNER,
          f"runner={meta.get('runner')}")
    check("main runner cache exits zero", meta.get("exit_code") == "0",
          f"exit_code={meta.get('exit_code')}")
    check("main runner cache status ok", meta.get("status") == "ok",
          f"status={meta.get('status')}")
    check("main runner cache sha matches source", meta.get("runner_sha256") == sha256_file(RUNNER),
          f"cache={meta.get('runner_sha256')}, live={sha256_file(RUNNER)}")
    for needle in [
        "3D INVERSE-SQUARE KERNEL BRANCH",
        "New propagator branch: same 3D ordered family, same spent-delay action, kernel w/L^2.",
        "h=1.0",
        "h=0.5",
        "fit=b^(0.25)",
        "keep it isolated",
    ]:
        check(f"main runner cache contains {needle!r}", needle in cache_text)

    print("=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        return 1
    print("Implementation-fidelity packet is complete; audit/review owns status movement.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
