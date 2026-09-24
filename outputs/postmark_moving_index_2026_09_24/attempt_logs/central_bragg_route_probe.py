#!/usr/bin/env python3
"""Finite diagnostic for a symmetry-suppressed central Bragg crossing."""
from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
import postmark_electric_simple_bragg_crossing_transfer_2026_09_24 as transfer


def run() -> dict:
    rows = []
    for m in (1, 2, 3, 4):
        lam = 2.0*(1.0-math.cos(m*math.pi/5.0))
        transfer.LAMBDA = lam
        for S in (120, 240, 480, 960, 1920, 3840, 7680, 15360):
            lo, hi = -0.10, 0.10
            h0, h1 = math.ceil(S*lo), math.floor(S*hi)
            product = np.eye(2, dtype=np.complex128)
            inner = np.eye(2, dtype=np.complex128)
            rho = S**-0.5
            phase = 0.0
            hyperbolic = 0
            inner_cells = 0
            for h in range(h0, h1):
                u = h/S
                cell = transfer.exact_cell_transfer(S, h, lam)
                step = np.linalg.solve(
                    transfer.principal_frame((h+1)/S),
                    cell @ transfer.principal_frame(u),
                )
                product = step @ product
                if abs(float(np.trace(cell))) > 2.0:
                    hyperbolic += 1
                correction, _, _ = transfer.phase_correction(u)
                phase += 5.0*transfer.local_k(u) + correction/S
                if abs(u) <= rho:
                    inner = (((-1.0)**m)*step) @ inner
                    inner_cells += 1

            scalar_model = np.diag((np.exp(1j*phase), np.exp(-1j*phase)))
            error = float(np.linalg.norm(product-scalar_model, ord=np.inf))
            rows.append({
                "m": m,
                "lambda": lam,
                "S": S,
                "u_interval": [h0/S, h1/S],
                "hyperbolic_local_cells": hyperbolic,
                "product_error": error,
                "error_times_S_1_2": error*math.sqrt(S),
                "offdiagonal_mixing": max(abs(product[0, 1]), abs(product[1, 0])),
                "inner_width": rho,
                "inner_cells": inner_cells,
                "inner_scalar_error": float(np.linalg.norm(inner-np.eye(2), ord=np.inf)),
                "inner_error_times_S_1_2": float(np.linalg.norm(inner-np.eye(2), ord=np.inf))*math.sqrt(S),
            })

    source_paths = [
        "docs/POSTMARK_ELECTRIC_FIVE_SITE_TRANSFER_PHASE_EXPANSION_BOUNDED_THEOREM_NOTE_2026-09-24.md",
        "docs/POSTMARK_ELECTRIC_REGULAR_BULK_PHASE_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-09-24.md",
        "docs/POSTMARK_ELECTRIC_FIVE_SITE_INTER_FIBER_PHASE_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    ]
    return {
        "scope": "finite float64 exact-transfer diagnostics only; not a theorem",
        "u_interval": [-0.10, 0.10],
        "sample_m_values": [1, 2, 3, 4],
        "source_sha256": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in source_paths},
        "rows": rows,
    }


if __name__ == "__main__":
    result = run()
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
