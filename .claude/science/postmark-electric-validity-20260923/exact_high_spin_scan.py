#!/usr/bin/env python3
"""Exact finite-spin fixed-time diagnostics beyond the S=384 campaign scan."""
from __future__ import annotations

import importlib.util
import argparse
import json
from pathlib import Path

AUDIT_TIMEOUT_SEC = 3600

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("spectral_probe", HERE / "spectral_fixed_time_probe.py")
spectral = importlib.util.module_from_spec(spec)
spec.loader.exec_module(spectral)


def run(spins):
    rows = []
    for spin in spins:
        exact = spectral.exact_spin(spin)
        rows.append({
            "S": spin,
            "C": exact["C"],
            "path_domain": exact["path_domain"],
            "dimension": exact["dimension"],
            "observable": [
                {
                    "time": x["time"],
                    "vacancy_B3": x["vacancy_B3"],
                    "path_class_probabilities_mod_3": x["path_class_probabilities_mod_3"],
                    "vacancy_character_mod_3": x["vacancy_character_mod_3"],
                    "norm_squared": x["norm_squared"],
                }
                for x in exact["observable"]
            ],
        })
        print(json.dumps(rows[-1], separators=(",", ":")), flush=True)
    return {
        "status": "double-precision exact finite-matrix diagnostics only; no fixed-time limit or discrepancy theorem",
        "source_revision": "b6eb31bedb3134dfacd8f4ab83cb7d96fc6dc953",
        "dependency_pr": 8831,
        "operator": "G_S=M_S^2-CM_S from supplied integer-spin one-vacancy Jacobi matrix",
        "times": [0.25, 0.5, 1.0],
        "results": rows,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--spins", nargs="+", type=int, default=[448, 512, 640, 768])
    parser.add_argument("--output", default="EXACT_HIGH_SPIN_SCAN.json")
    args = parser.parse_args()
    output_path = (HERE / args.output).resolve()
    if output_path.parent != HERE:
        raise SystemExit("--output must name a file inside the evidence directory")
    out = run(tuple(args.spins))
    payload = json.dumps(out, indent=2) + "\n"
    output_path.write_text(payload)
    print(payload, end="")
