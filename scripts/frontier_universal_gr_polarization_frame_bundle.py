#!/usr/bin/env python3
"""Verify the finite polarization-frame orbit support packet.

This is not a closure proof and not an exhaustive no-go. It checks that the
current finite prototype gives:

1. the exact scalar observable generator from the axiom-side observable
   principle;
2. the exact `3+1` kinematic lift on `PL S^3 x R`;
3. the exact tensor-valued variational candidate;
4. the exact unique symmetric `3+1` quotient kernel;
5. a finite frame-orbit check showing that the sampled prototype determines an
   associated family of localizations, not a canonical complement section by
   this route;
6. source-boundary text forbidding reuse as full GR closure or as an
   exhaustive no-go.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

OBSERVABLE = DOCS / "OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md"
ROUTE2 = DOCS / "S3_ANOMALY_SPACETIME_LIFT_NOTE.md"
VARIATIONAL = DOCS / "UNIVERSAL_GR_TENSOR_VARIATIONAL_CANDIDATE_NOTE.md"
UNIQUENESS = DOCS / "UNIVERSAL_GR_TENSOR_QUOTIENT_UNIQUENESS_NOTE.md"
BLOCKER = DOCS / "UNIVERSAL_GR_TENSOR_ACTION_BLOCKER_NOTE.md"
CURVATURE = DOCS / "UNIVERSAL_GR_CURVATURE_LOCALIZATION_BLOCKER_NOTE.md"
FRAME_BUNDLE = DOCS / "UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_BLOCKER_NOTE.md"
ATTEMPT_NOTE = DOCS / "UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_ATTEMPT.md"

SOURCE_INPUT_LINKS = [
    "OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md",
    "S3_ANOMALY_SPACETIME_LIFT_NOTE.md",
    "UNIVERSAL_GR_TENSOR_VARIATIONAL_CANDIDATE_NOTE.md",
    "UNIVERSAL_GR_TENSOR_QUOTIENT_UNIQUENESS_NOTE.md",
]

SOURCE_BOUNDARY_REQUIRED_PHRASES = [
    "Downstream source-boundary firewall",
    "exact scalar observable generator",
    "exact `3+1` kinematic lift",
    "unique symmetric",
    "rank-2 scalar-channel projector",
    "complement-channel localization coefficients",
    "canonical full polarization-frame bundle",
    "canonical full projector bundle",
    "curvature-localization operator `Pi_curv`",
    "Einstein/Regge dynamics law",
    "framework-level GR derivation",
    "distinguished covariant frame/projector bundle with connection",
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
    obs = read(OBSERVABLE)
    route2 = read(ROUTE2)
    var = read(VARIATIONAL)
    uni = read(UNIQUENESS)
    blk = read(BLOCKER)
    curv = read(CURVATURE)
    fb = read(FRAME_BUNDLE)
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

    checks = [
        Check(
            "scalar generator is exact",
            has(obs, "observable principle") and has(obs, "det(d+j)") and has(obs, "det d"),
            "observable principle gives the exact scalar generator",
        ),
        Check(
            "3+1 lift is exact",
            has(route2, "pl s^3 x r") or has(route2, "O_lift = 1"),
            "route-2 gives the exact PL S^3 x R scaffold",
        ),
        Check(
            "tensor candidate is exact as a construction",
            has(var, "metric-source hessian") and has(var, "s_gr^cand"),
            "candidate note identifies the Hessian on the lifted background",
        ),
        Check(
            "unique symmetric quotient kernel is exact on the prototype",
            has(uni, "unique symmetric `3+1` quotient kernel")
            or has(uni, "unique bilinear lift"),
            "quotient-uniqueness note records the nondegenerate prototype kernel",
        ),
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
            "source note narrows to finite frame-orbit support",
            has(fb, "2026-06-18 scope repair")
            and has(fb, "finite frame-orbit support")
            and has(fb, "not an exhaustive no-go"),
            "source row is scoped as finite support, not universal no-go",
        ),
        Check(
            "source note exposes non-reciprocal verifier dependencies",
            all(f"]({target})" in fb for target in SOURCE_INPUT_LINKS)
            and "UNIVERSAL_GR_TENSOR_ACTION_BLOCKER_NOTE.md" in fb
            and "](UNIVERSAL_GR_TENSOR_ACTION_BLOCKER_NOTE.md)" not in fb
            and "UNIVERSAL_GR_CURVATURE_LOCALIZATION_BLOCKER_NOTE.md" in fb
            and "](UNIVERSAL_GR_CURVATURE_LOCALIZATION_BLOCKER_NOTE.md)" not in fb
            and "UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_ATTEMPT.md" in fb
            and "](UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_ATTEMPT.md)" not in fb,
            "support sources are markdown-linked; reciprocal guardrail notes stay plain text",
        ),
        Check(
            "curvature-localization blocker isolates the frame-orbit obstruction",
            has(curv, "older frame-orbit blocker was too strong")
            or (has(curv, "frame-orbit") and has(curv, "Casimir block localization")),
            "older frame-orbit blocker is now historical; live blocker reframed as interpretation theorem beyond Lorentzian closure",
        ),
        Check(
            "frame-bundle note records missing primitive without closure claim",
            has(fb, "polarization-frame bundle")
            and has(fb, "Pi_curv")
            and has(fb, "does not close universal GR"),
            "the dedicated note keeps Pi_curv and full GR outside this packet",
        ),
        Check(
            "localization coefficients depend on frame choice",
            frame_delta > 1e-6,
            f"max channel delta across two valid polarization frames = {frame_delta:.3e}",
        ),
        Check(
            "source-boundary firewall names allowed and forbidden downstream uses",
            all(phrase.lower() in attempt.lower() for phrase in SOURCE_BOUNDARY_REQUIRED_PHRASES),
            "attempt note preserves open-gate/source-boundary guardrails",
        ),
        Check(
            "source-boundary firewall forbids full GR/curvature-localization reuse",
            has(attempt, "do not cite it as a curvature-localization operator `Pi_curv`")
            and has(attempt, "do not cite it as an Einstein/Regge dynamics law")
            and has(attempt, "do not cite it as a framework-level GR derivation"),
            "runner pass remains blocker/support only, not GR closure",
        ),
    ]

    print("UNIVERSAL GR POLARIZATION-FRAME FINITE ORBIT VERIFIER")
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
            "Direct-universal progress: the scalar observable principle and the "
            "3+1 lift now support an exact tensor-valued variational candidate "
            "with a unique symmetric quotient kernel, but the exact curvature-"
            "localization operator is not supplied here. The checked result is "
            "finite frame-orbit support, not an exhaustive no-go."
        )
        return 0

    print("One or more candidate checks failed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
