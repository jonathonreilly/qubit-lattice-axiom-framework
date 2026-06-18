#!/usr/bin/env python3
"""Finite prototype verifier for the universal-GR frame-bundle attempt.

This runner deliberately does not read the route-level upstream notes as proof
inputs. It checks the auditable source claim of the attempt row: on the finite
prototype Hessian, two valid polarization frames give the same scalar-channel
sector but different complement-channel localization coefficients. The route
context remains open unless downstream rows cite and audit the upstream
scalar/3+1/tensor/quotient authorities directly.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

ATTEMPT_NOTE = DOCS / "UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_ATTEMPT.md"

SOURCE_BOUNDARY_REQUIRED_PHRASES = [
    "Audit-scope note (2026-06-18)",
    "finite prototype frame-dependence diagnostic",
    "not one-hop proof authorities imported by this row",
    "without reading those upstream notes as proof inputs",
    "Downstream source-boundary firewall",
    "cite the finite prototype frame-dependence diagnostic",
    "citing those upstream sources directly if they are load-bearing",
    "`3+1` lift on `PL S^3 x R`",
    "unique symmetric",
    "rank-2 scalar-channel projector",
    "complement-channel localization coefficients",
    "canonical full polarization-frame bundle",
    "canonical full projector bundle",
    "curvature-localization operator `Pi_curv`",
    "Einstein/Regge dynamics law",
    "framework-level GR derivation",
    "exhaustive no-go",
    "distinguished covariant frame/projector bundle with connection",
    "This packet's auditable source claim is",
]


@dataclass
class Check:
    name: str
    ok: bool
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def has(text: str, needle: str) -> bool:
    return " ".join(needle.lower().split()) in " ".join(text.lower().split())


def bilinear(
    a: Sequence[Sequence[float]],
    b: Sequence[Sequence[float]],
    d: Sequence[float],
) -> float:
    """Exact Hessian prototype: -Tr(D^-1 a D^-1 b) for diagonal D."""

    total = 0.0
    n = len(d)
    for i in range(n):
        for j in range(n):
            total += a[i][j] * b[j][i] / (d[i] * d[j])
    return -total


def sym_basis(n: int) -> list[list[list[float]]]:
    basis: list[list[list[float]]] = []
    for i in range(n):
        m = [[0.0 for _ in range(n)] for _ in range(n)]
        m[i][i] = 1.0
        basis.append(m)
    for i in range(n):
        for j in range(i + 1, n):
            m = [[0.0 for _ in range(n)] for _ in range(n)]
            scale = 2.0 ** 0.5
            m[i][j] = 1.0 / scale
            m[j][i] = 1.0 / scale
            basis.append(m)
    return basis


def gram_matrix(
    basis: Sequence[Sequence[Sequence[float]]],
    d: Sequence[float],
) -> list[list[float]]:
    return [[bilinear(a, b, d) for b in basis] for a in basis]


def rank(matrix: Sequence[Sequence[float]], tol: float = 1e-12) -> int:
    rows = [list(row) for row in matrix]
    m = len(rows)
    n = len(rows[0]) if rows else 0
    r = 0
    c = 0
    while r < m and c < n:
        pivot = max(range(r, m), key=lambda i: abs(rows[i][c]))
        if abs(rows[pivot][c]) <= tol:
            c += 1
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        piv = rows[r][c]
        for j in range(c, n):
            rows[r][j] /= piv
        for i in range(m):
            if i == r:
                continue
            factor = rows[i][c]
            if abs(factor) <= tol:
                continue
            for j in range(c, n):
                rows[i][j] -= factor * rows[r][j]
        r += 1
        c += 1
    return r


def max_symmetry_error(matrix: Sequence[Sequence[float]]) -> float:
    err = 0.0
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            err = max(err, abs(val - matrix[j][i]))
    return err


def matmul(a: Sequence[Sequence[float]], b: Sequence[Sequence[float]]) -> list[list[float]]:
    n = len(a)
    m = len(b[0]) if b else 0
    out = [[0.0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for k in range(len(b)):
            aik = a[i][k]
            if abs(aik) <= 1e-15:
                continue
            for j in range(m):
                out[i][j] += aik * b[k][j]
    return out


def transpose(a: Sequence[Sequence[float]]) -> list[list[float]]:
    return [list(row) for row in zip(*a)]


def conj(rot: Sequence[Sequence[float]], m: Sequence[Sequence[float]]) -> list[list[float]]:
    return matmul(matmul(transpose(rot), m), rot)


def sym(i: int, j: int, n: int = 4) -> list[list[float]]:
    m = [[0.0 for _ in range(n)] for _ in range(n)]
    if i == j:
        m[i][j] = 1.0
    else:
        scale = 2.0 ** 0.5
        m[i][j] = 1.0 / scale
        m[j][i] = 1.0 / scale
    return m


def diag(vals: Sequence[float]) -> list[list[float]]:
    n = len(vals)
    m = [[0.0 for _ in range(n)] for _ in range(n)]
    for i, v in enumerate(vals):
        m[i][i] = float(v)
    return m


def canonical_polarization_frame() -> list[list[list[float]]]:
    """A fixed lapse/shift/trace/shear basis on the symmetric `3+1` sector."""

    sqrt2 = 2.0 ** 0.5
    sqrt3 = 3.0 ** 0.5
    sqrt6 = 6.0 ** 0.5
    return [
        sym(0, 0),
        sym(0, 1),
        sym(0, 2),
        sym(0, 3),
        diag((0.0, 1.0 / sqrt3, 1.0 / sqrt3, 1.0 / sqrt3)),
        diag((0.0, 1.0 / sqrt2, -1.0 / sqrt2, 0.0)),
        diag((0.0, 1.0 / sqrt6, 1.0 / sqrt6, -2.0 / sqrt6)),
        sym(1, 2),
        sym(1, 3),
        sym(2, 3),
    ]


def rotated_polarization_frame(theta: float) -> list[list[list[float]]]:
    """Rotate the spatial `1-2` plane of the canonical polarization frame."""

    c = math.cos(theta)
    s = math.sin(theta)
    rot = [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, c, -s, 0.0],
        [0.0, s, c, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]
    return [conj(rot, basis) for basis in canonical_polarization_frame()]


def response_vector(
    h: Sequence[Sequence[float]],
    frame: Sequence[Sequence[Sequence[float]]],
    d: Sequence[float],
) -> list[float]:
    return [bilinear(h, basis, d) for basis in frame]


def max_abs_delta(a: Sequence[float], b: Sequence[float]) -> float:
    return max(abs(x - y) for x, y in zip(a, b))


def main() -> int:
    attempt = read(ATTEMPT_NOTE)

    d = (2.0, 3.0, 5.0, 7.0)
    basis = sym_basis(4)
    gram = gram_matrix(basis, d)

    I = [[0.0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        I[i][i] = 1.0

    scalar_direct = bilinear(I, I, d)
    scalar_expected = -sum(1.0 / (x * x) for x in d)

    h_test = (
        (1.0, 0.35, -0.22, 0.18),
        (0.35, -0.75, 0.14, 0.07),
        (-0.22, 0.14, 0.41, -0.19),
        (0.18, 0.07, -0.19, -0.28),
    )
    frame_a = canonical_polarization_frame()
    frame_b = rotated_polarization_frame(math.pi / 6.0)
    resp_a = response_vector(h_test, frame_a, d)
    resp_b = response_vector(h_test, frame_b, d)
    frame_delta = max_abs_delta(resp_a, resp_b)
    scalar_channel_delta = max(abs(resp_a[i] - resp_b[i]) for i in (0, 4))
    complement_delta = max(abs(resp_a[i] - resp_b[i]) for i in (1, 2, 3, 5, 6, 7, 8, 9))

    checks = [
        Check(
            "prototype Gram matrix is symmetric",
            max_symmetry_error(gram) < 1e-15,
            f"max symmetry error = {max_symmetry_error(gram):.3e}",
        ),
        Check(
            "prototype symmetric quotient basis is nondegenerate",
            rank(gram) == len(gram),
            f"rank = {rank(gram)} / {len(gram)}",
        ),
        Check(
            "scalar-line restriction matches the same Hessian",
            abs(scalar_direct - scalar_expected) < 1e-15,
            f"direct = {scalar_direct:.6e}, expected = {scalar_expected:.6e}",
        ),
        Check(
            "canonical and rotated frames have ten symmetric-sector channels",
            len(frame_a) == len(frame_b) == 10,
            f"len(frame_a)={len(frame_a)}, len(frame_b)={len(frame_b)}",
        ),
        Check(
            "rank-2 scalar channel is invariant under the tested spatial rotation",
            scalar_channel_delta < 1e-12,
            f"max scalar-channel delta = {scalar_channel_delta:.3e}",
        ),
        Check(
            "complement channels depend on frame choice",
            complement_delta > 1e-6 and abs(complement_delta - frame_delta) < 1e-15,
            f"max complement delta = {complement_delta:.3e}",
        ),
        Check(
            "localized full-channel coefficients depend on frame choice",
            frame_delta > 1e-6,
            f"max channel delta across two valid polarization frames = {frame_delta:.3e}",
        ),
        Check(
            "source-boundary firewall names allowed and forbidden downstream uses",
            all(has(attempt, phrase) for phrase in SOURCE_BOUNDARY_REQUIRED_PHRASES),
            "attempt note preserves open-gate/source-boundary guardrails",
        ),
        Check(
            "source-boundary firewall forbids full GR/curvature-localization reuse",
            has(attempt, "do not cite it as a curvature-localization operator `Pi_curv`")
            and has(attempt, "do not cite it as an Einstein/Regge dynamics law")
            and has(attempt, "do not cite it as a framework-level GR derivation"),
            "runner pass remains blocker/support only, not GR closure",
        ),
        Check(
            "runner boundary avoids hidden route-level imports",
            has(attempt, "not one-hop proof authorities imported by this row")
            and has(attempt, "Any downstream current-stack or route-level closure must cite and audit the upstream sources directly"),
            "attempt note keeps upstream route handles out of this runner's proof inputs",
        ),
    ]

    print("UNIVERSAL GR POLARIZATION-FRAME BUNDLE FINITE DIAGNOSTIC")
    print("=" * 78)
    for c in checks:
        tag = "PASS" if c.ok else "FAIL"
        print(f"[{tag}] {c.name}")
        print(f"    {c.detail}")

    print("\n" + "=" * 78)
    print("PROTOTYPE RESULTS")
    print("=" * 78)
    print(f"scalar_direct   = {scalar_direct:.12e}")
    print(f"scalar_expected = {scalar_expected:.12e}")
    print(f"gram_rank       = {rank(gram)}")
    print(f"gram_size       = {len(gram)}")
    print(f"symmetry_error  = {max_symmetry_error(gram):.12e}")
    print(f"scalar_delta    = {scalar_channel_delta:.12e}")
    print(f"complement_delta= {complement_delta:.12e}")
    print(f"frame_delta     = {frame_delta:.12e}")
    print(f"resp_a[0:4]     = {[f'{x:.6e}' for x in resp_a[:4]]}")
    print(f"resp_b[0:4]     = {[f'{x:.6e}' for x in resp_b[:4]]}")

    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    n_pass = sum(c.ok for c in checks)
    n_fail = len(checks) - n_pass
    print(f"PASS={n_pass} FAIL={n_fail} TOTAL={len(checks)}")
    if n_fail == 0:
        print(
            "Finite diagnostic: the displayed prototype has a canonical rank-2 "
            "scalar channel, while complement-channel localization remains "
            "frame-dependent. Route-level upstream closure is not claimed by "
            "this runner."
        )
        return 0

    print("One or more candidate checks failed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
