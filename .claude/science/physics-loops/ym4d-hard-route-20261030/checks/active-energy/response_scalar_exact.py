#!/usr/bin/env python3
"""Registered exact scalar quadratic check; not an SU(2) simulation."""

from fractions import Fraction as F
import os
import resource
import sys

LIMIT = 2 * 1024**3


def rss_bytes():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else value * 1024)


def memory_check():
    if rss_bytes() >= LIMIT:
        raise MemoryError("2 GiB RSS limit reached; stopping")


def set_limits():
    for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
                 "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
        if os.environ.get(name) != "1":
            raise RuntimeError(f"{name} must be 1 before starting")
    for name in ("RLIMIT_AS", "RLIMIT_DATA"):
        kind = getattr(resource, name, None)
        if kind is None:
            print(f"{name}: unavailable; RSS self-check active")
            continue
        try:
            soft, hard = resource.getrlimit(kind)
            cap = LIMIT if hard == resource.RLIM_INFINITY else min(LIMIT, hard)
            if soft != resource.RLIM_INFINITY:
                cap = min(cap, soft)
            resource.setrlimit(kind, (cap, hard))
            print(f"{name}: soft limit {cap} bytes")
        except (OSError, ValueError) as error:
            print(f"{name}: {error}; RSS self-check active")
    memory_check()


def solve(matrix, rhs):
    """Dense exact Gauss-Jordan; bounded dimension, RSS checked each pivot."""
    size = len(rhs)
    assert 0 < size <= 128
    memory_check()
    rows = [[F(v) for v in row] + [F(rhs[i])]
            for i, row in enumerate(matrix)]
    for col in range(size):
        memory_check()
        pivot = next(row for row in range(col, size) if rows[row][col])
        rows[col], rows[pivot] = rows[pivot], rows[col]
        divisor = rows[col][col]
        rows[col] = [v / divisor for v in rows[col]]
        for row in range(size):
            if row == col or not rows[row][col]:
                continue
            factor = rows[row][col]
            rows[row] = [v - factor * w
                         for v, w in zip(rows[row], rows[col])]
    result = [row[-1] for row in rows]
    assert all(sum(F(v) * x for v, x in zip(row, result)) == F(y)
               for row, y in zip(matrix, rhs))
    memory_check()
    return result


def fine_kkt(length, means):
    blocks = len(means)
    sites = length * blocks
    size = sites + blocks
    matrix = [[0] * size for _ in range(size)]
    for n in range(sites):
        matrix[n][n] = 2
        matrix[n][(n - 1) % sites] -= 1
        matrix[n][(n + 1) % sites] -= 1
        j = n // length
        matrix[n][sites + j] = 1
        matrix[sites + j][n] = 1
    rhs = [0] * sites + [length * mu for mu in means]
    h = solve(matrix, rhs)[:sites]
    for j, mu in enumerate(means):
        assert sum(h[j * length:(j + 1) * length]) == length * mu
    return h


def reduced_slopes(length, means):
    blocks = len(means)
    b = F(length**2 - 1, 6 * length)
    a = length - 2 * b
    assert a > 2 * b > 0
    matrix = [[F(0)] * blocks for _ in range(blocks)]
    for j in range(blocks):
        matrix[j][j] = a
        matrix[j][(j - 1) % blocks] = b
        matrix[j][(j + 1) % blocks] = b
    rhs = [means[j] - means[(j - 1) % blocks] for j in range(blocks)]
    return solve(matrix, rhs)


def check_case(length, blocks, control=None):
    if control is None:
        means = [int(j == blocks // 2) for j in range(blocks)]
    else:
        means = [control] * blocks
    h = fine_kkt(length, means)
    p = reduced_slopes(length, means)
    slopes = [h[(n + 1) % len(h)] - h[n] for n in range(len(h))]
    interpolated = []
    for j in range(blocks):
        assert p[j] == h[j * length] - h[(j * length - 1) % len(h)]
        for r in range(length):
            weight = F(r + 1, length)
            interpolated.append((1 - weight) * p[j] + weight * p[(j + 1) % blocks])
    assert slopes == interpolated
    energy = sum(v * v for v in slopes) / 2
    assert energy == sum(v * v for v in interpolated) / 2
    if control is None:
        assert all(means[j % blocks] == 0 for j in range(-2, 3))
        assert p[0] != 0 and all(v != 0 for v in p)
        print(f"L={length} M={blocks}: exact equations/means/slopes/energy agree; "
              f"p[0]={p[0]}; E={energy}; local zero-mean patch has zero minimizer")
    else:
        assert all(v == control for v in h)
        assert all(v == 0 for v in p) and energy == 0
        print(f"control mu={control}, L={length} M={blocks}: "
              "constant h, zero slopes and zero energy")
    memory_check()


def main():
    set_limits()
    print("source: 25a86977f538eb6bb104f097c435b44fd42138b7")
    print("arithmetic: exact fractions; two separately assembled systems")
    for length, blocks in ((3, 12), (5, 12), (7, 12), (5, 16)):
        check_case(length, blocks)
    for value in (0, 1):
        check_case(3, 12, value)
    print("All registered exact scalar checks passed.")
    print("per_element: fine differences match the interface interpolation exactly.")
    print("per_site: the cyclic fine-site KKT equations and every constraint were checked.")
    print("per_mode: no Fourier-mode exhaustion or nonlinear SU(2) calculation was run.")
    print("per_block: all block means and every nonzero interface slope were checked.")
    print("lattice_wide: four finite scalar rings only; arbitrary size is an analytic claim.")
    print(f"peak RSS: {rss_bytes()} bytes; limit: {LIMIT} bytes")


if __name__ == "__main__":
    main()
