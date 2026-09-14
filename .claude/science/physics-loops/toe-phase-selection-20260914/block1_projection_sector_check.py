#!/usr/bin/env python3
"""Finite falsifiers for exact projection and charge-sector assertions.

Author checks only. No thermodynamic extrapolation or phase identification.
The cellular boundary is rebuilt here from oriented products of intervals.
The clock-move route and truncated-shift route are compared coefficientwise.
"""
from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations, product
import json
from pathlib import Path
import time

import numpy as np
from scipy import sparse
from scipy.sparse.csgraph import connected_components
from scipy.sparse.linalg import eigsh


def box_complex(lengths):
    """Oriented product cells; lengths count cubes, not vertices."""
    lengths = tuple(lengths)
    levels = []
    for k in range(4):
        level = []
        for axes in combinations(range(3), k):
            for origin in product(*(range(lengths[a] + (a not in axes))
                                    for a in range(3))):
                level.append((axes, origin))
        levels.append(level)
    boundaries = []
    for k in range(1, 4):
        lower = {cell: i for i, cell in enumerate(levels[k-1])}
        mat = np.zeros((len(lower), len(levels[k])), dtype=np.int64)
        for j, (axes, origin) in enumerate(levels[k]):
            for position, axis in enumerate(axes):
                rest = tuple(a for a in axes if a != axis)
                upper = list(origin)
                upper[axis] += 1
                sign = (-1)**position
                mat[lower[(rest, tuple(upper))], j] += sign
                mat[lower[(rest, origin)], j] -= sign
        boundaries.append(mat)
    b1, b2, b3 = boundaries
    assert not np.any(b1 @ b2)
    assert not np.any(b2 @ b3)
    return levels, b1, b2.T, b3.T


def flux_basis(F, D):
    p = F.shape[0]
    assert p <= 11, "This finite check deliberately caps the full carrier."
    powers = 3**np.arange(p, dtype=np.int64)
    codes = np.arange(3**p, dtype=np.int64)
    all_b = ((codes[:, None] // powers[None, :]) % 3 - 1).astype(np.int64)
    div = all_b @ D.T
    physical = np.all(div % 3 == 0, axis=1)
    b, div = all_b[physical], div[physical]
    ids = np.full(3**p, -1, dtype=np.int64)
    ids[codes[physical]] = np.arange(len(b))
    assert len(b) == 3**(p - D.shape[0])
    return b, div//3, powers, ids


def clock_coefficients(b, F, powers, ids):
    """A_mu = sum_k exp(-k mu) A[k], each A[k] an integer matrix."""
    triplets = {k: ([], []) for k in range(5)}
    for l in range(F.shape[1]):
        f = F[:, l]
        assert np.any(f)
        for sigma in (-1, 1):
            raw = b + sigma*f
            new = (raw + 1) % 3 - 1
            m = (new-raw)//3
            k = np.sum(m*m, axis=1)
            dest = ids[(new+1) @ powers]
            assert np.all(dest >= 0)
            for exponent in range(5):
                source = np.flatnonzero(k == exponent)
                triplets[exponent][0].append(dest[source])
                triplets[exponent][1].append(source)
    out = []
    for exponent in range(5):
        rows = np.concatenate(triplets[exponent][0])
        cols = np.concatenate(triplets[exponent][1])
        mat = sparse.coo_matrix((np.ones(len(rows), dtype=np.int64), (rows, cols)),
                               shape=(len(b), len(b))).tocsr()
        mat.sum_duplicates()
        assert (mat-mat.T).nnz == 0
        out.append(mat)
    return out


def shift_coefficients(b0, F):
    """Separate route: integer truncated shifts, never modular arithmetic."""
    index = {tuple(row): i for i, row in enumerate(b0)}
    rows, cols = {k: [] for k in range(5)}, {k: [] for k in range(5)}
    for l in range(F.shape[1]):
        f = F[:, l]
        r = np.count_nonzero(f)
        for jump in (-2, -1, 1, 2):
            new = b0 + jump*f
            allowed = np.flatnonzero(np.all(np.abs(new) <= 1, axis=1))
            exponent = 0 if abs(jump) == 1 else r
            for source in allowed:
                rows[exponent].append(index[tuple(new[source])])
                cols[exponent].append(source)
    out = []
    for exponent in range(5):
        out.append(sparse.coo_matrix(
            (np.ones(len(rows[exponent]), dtype=np.int64),
             (rows[exponent], cols[exponent])),
            shape=(len(b0), len(b0))).tocsr())
    return out


def local_star_check(lengths=(3, 3, 3)):
    levels, _, F, D = box_complex(lengths)
    census = Counter()
    closed_patterns = 0
    for l in range(F.shape[1]):
        support = np.flatnonzero(F[:, l])
        f = F[support, l]
        r = len(support)
        rank = np.linalg.matrix_rank(D[:, support].astype(float))
        assert rank == r-1
        census[r] += 1
        for wraps in product((0, 1), repeat=r):
            m = -f*np.asarray(wraps)
            closed = not np.any(D[:, support] @ m)
            all_or_none = len(set(wraps)) == 1
            assert closed == all_or_none
            closed_patterns += int(closed)
    return {"box": lengths, "star_sizes": dict(census),
            "closed_binary_wrap_patterns": closed_patterns,
            "edges": len(levels[1])}


def lowest(mat):
    n = mat.shape[0]
    if n <= 256:
        ev, vec = np.linalg.eigh(mat.toarray())
        val, v = ev[0], vec[:, 0]
    else:
        ev, vec = eigsh(mat.astype(float), k=1, which="SA", tol=2e-12,
                        v0=np.ones(n)/np.sqrt(n), maxiter=30000)
        val, v = ev[0], vec[:, 0]
    residual = float(np.linalg.norm(mat @ v-val*v))
    assert residual <= 1e-8*max(1, abs(val))
    return float(val), residual


def sector_check(lengths, stiffnesses=(0.0, 0.05, 0.2, 1.0, 5.0)):
    levels, _, F, D = box_complex(lengths)
    b, q, powers, ids = flux_basis(F, D)
    coeff = clock_coefficients(b, F, powers, ids)
    neutral = np.flatnonzero(np.all(q == 0, axis=1))
    shifts = shift_coefficients(b[neutral], F)
    projection = []
    for exponent in range(5):
        direct = coeff[exponent][neutral][:, neutral]
        diff = direct-shifts[exponent]
        diff.eliminate_zeros()
        assert diff.nnz == 0, (lengths, exponent)
        projection.append({"exponent": exponent, "nonzero_matrix_entries": direct.nnz,
                           "total_integer_multiplicity": int(direct.sum())})
    # Every hard move conserves integer charge, not just charge modulo three.
    row, col = coeff[0].nonzero()
    assert np.array_equal(q[row], q[col])
    sectors = {}
    for i, row in enumerate(q):
        sectors.setdefault(tuple(int(x) for x in row), []).append(i)
    electric = np.sum(b*b, axis=1)
    samples = []
    for stiffness in stiffnesses:
        values = []
        for charge, indexes in sorted(sectors.items()):
            idx = np.asarray(indexes)
            adjacency = coeff[0][idx][:, idx]
            count, _ = connected_components(adjacency, directed=False)
            h = -adjacency.astype(float) + sparse.diags(stiffness*electric[idx])
            energy, residual = lowest(h)
            values.append({"charge": charge, "size": len(idx), "components": count,
                           "energy_without_constant_or_charge_penalty": energy,
                           "residual": residual})
        zero = next(v["energy_without_constant_or_charge_penalty"] for v in values
                    if all(x == 0 for x in v["charge"]))
        charged = [v for v in values if any(x != 0 for x in v["charge"])]
        winner = min(charged, key=lambda v: v["energy_without_constant_or_charge_penalty"])
        threshold = max([0.0] + [
            (zero-v["energy_without_constant_or_charge_penalty"])
            /sum(x*x for x in v["charge"]) for v in charged])
        samples.append({"electric_stiffness_3K_over_2": stiffness,
                        "neutral_energy_without_constant": zero,
                        "lowest_charged": winner,
                        "charged_minus_neutral": winner["energy_without_constant_or_charge_penalty"]-zero,
                        "finite_box_lambda_threshold": threshold, "sectors": values})
        print(json.dumps({"box": lengths, "stiffness": stiffness,
                          "neutral": zero, "charged_difference": samples[-1]["charged_minus_neutral"],
                          "lambda_threshold": threshold}), flush=True)
    return {"box": lengths, "vertices_edges_faces_cubes": [len(v) for v in levels],
            "physical_dimension": len(b), "neutral_dimension": len(neutral),
            "charge_sectors": len(sectors), "projection_coefficients": projection,
            "samples": samples}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--cube-only", action="store_true")
    args = parser.parse_args()
    started = time.monotonic()
    result = {"status": "finite_author_check_only", "local_stars": local_star_check(),
              "boxes": [sector_check((1, 1, 1))]}
    if not args.cube_only:
        result["boxes"].append(sector_check((1, 1, 2)))
    result["elapsed_seconds"] = time.monotonic()-started
    if args.output:
        args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("Exact coefficientwise projection checks completed; finite sector comparisons recorded.")
    print("No infinite-volume sector ordering or phase inference.")


if __name__ == "__main__":
    main()
