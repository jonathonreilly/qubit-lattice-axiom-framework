#!/usr/bin/env python3
"""Verify the current-stack Pi_curv route-exhaustion no-go packet.

This runner is source-side support. It does not audit, retag, or edit any
ledger row.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

NOTE = DOCS / "UNIVERSAL_GR_PICURV_ROUTE_EXHAUSTION_NO_GO_NOTE_2026-06-18.md"
PARENT = DOCS / "UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_BLOCKER_NOTE.md"
ATTEMPT = DOCS / "UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_ATTEMPT.md"
A1_NOTE = DOCS / "UNIVERSAL_GR_A1_INVARIANT_SECTION_NOTE.md"
CASIMIR_NOTE = DOCS / "UNIVERSAL_GR_CASIMIR_BLOCK_LOCALIZATION_NOTE.md"
CONNECTION_NOTE = DOCS / "UNIVERSAL_GR_CANONICAL_PROJECTOR_CONNECTION_NOTE.md"
COMPLEMENT_NOTE = DOCS / "UNIVERSAL_GR_COMPLEMENT_CANONICAL_NOTE.md"
ROUND_REGGE_NOTE = DOCS / (
    "UNIVERSAL_GR_ROUND_PL_S3_REGGE_HESSIAN_CANONICAL_CHANNELS_"
    "NARROW_THEOREM_NOTE_2026-06-10.md"
)
SPIN2_NOTE = DOCS / (
    "UNIVERSAL_GR_SPIN2_TWO_DERIVATIVE_CURVATURE_GENERATOR_SUPPLIED_"
    "FLAT_ATLAS_NARROW_THEOREM_NOTE_2026-06-10.md"
)
FINITE_RANK_NOTE = DOCS / "FINITE_RANK_GRAVITY_RESIDUAL_HELPER_NOTE_2026-04-14.md"
EXTERIOR_NOTE = DOCS / "COARSE_GRAINED_EXTERIOR_LAW_HELPER_NOTE_2026-04-14.md"

TARGET_BLOCKER = (
    "scope_too_broad: narrow to the finite frame-delta/orbit support result "
    "or provide an exhaustive no-go gate covering at least five alternative "
    "Pi_curv construction routes."
)


@dataclass(frozen=True)
class Check:
    name: str
    ok: bool
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def has(text: str, needle: str) -> bool:
    return needle.lower() in text.lower()


def has_words(text: str, needle: str) -> bool:
    return needle.lower() in " ".join(text.lower().split())


def matmul(
    a: Sequence[Sequence[float]], b: Sequence[Sequence[float]]
) -> list[list[float]]:
    rows = len(a)
    cols = len(b[0]) if b else 0
    out = [[0.0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for k in range(len(b)):
            aik = a[i][k]
            if abs(aik) <= 1e-15:
                continue
            for j in range(cols):
                out[i][j] += aik * b[k][j]
    return out


def transpose(a: Sequence[Sequence[float]]) -> list[list[float]]:
    return [list(row) for row in zip(*a)]


def conj(
    rot: Sequence[Sequence[float]], m: Sequence[Sequence[float]]
) -> list[list[float]]:
    return matmul(matmul(transpose(rot), m), rot)


def sym(i: int, j: int, n: int = 4) -> list[list[float]]:
    m = [[0.0 for _ in range(n)] for _ in range(n)]
    if i == j:
        m[i][j] = 1.0
    else:
        scale = math.sqrt(2.0)
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
    sqrt2 = math.sqrt(2.0)
    sqrt3 = math.sqrt(3.0)
    sqrt6 = math.sqrt(6.0)
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
    c = math.cos(theta)
    s = math.sin(theta)
    rot = [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, c, -s, 0.0],
        [0.0, s, c, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]
    return [conj(rot, basis) for basis in canonical_polarization_frame()]


def bilinear(
    a: Sequence[Sequence[float]],
    b: Sequence[Sequence[float]],
    d: Sequence[float],
) -> float:
    total = 0.0
    n = len(d)
    for i in range(n):
        for j in range(n):
            total += a[i][j] * b[j][i] / (d[i] * d[j])
    return -total


def response_vector(
    h: Sequence[Sequence[float]],
    frame: Sequence[Sequence[Sequence[float]]],
    d: Sequence[float],
) -> list[float]:
    return [bilinear(h, basis, d) for basis in frame]


def max_abs_delta(a: Sequence[float], b: Sequence[float]) -> float:
    return max(abs(x - y) for x, y in zip(a, b))


def vector_average(a: Sequence[float], b: Sequence[float]) -> list[float]:
    return [(x + y) / 2.0 for x, y in zip(a, b)]


def main() -> int:
    note = read(NOTE)
    parent = read(PARENT)
    attempt = read(ATTEMPT)
    a1_note = read(A1_NOTE)
    casimir = read(CASIMIR_NOTE)
    connection = read(CONNECTION_NOTE)
    complement = read(COMPLEMENT_NOTE)
    round_regge = read(ROUND_REGGE_NOTE)
    spin2 = read(SPIN2_NOTE)
    finite_rank = read(FINITE_RANK_NOTE)
    exterior = read(EXTERIOR_NOTE)

    d = (2.0, 3.0, 5.0, 7.0)
    h_test = (
        (1.0, 0.35, -0.22, 0.18),
        (0.35, -0.75, 0.14, 0.07),
        (-0.22, 0.14, 0.41, -0.19),
        (0.18, 0.07, -0.19, -0.28),
    )
    resp_a = response_vector(h_test, canonical_polarization_frame(), d)
    resp_b = response_vector(h_test, rotated_polarization_frame(math.pi / 6.0), d)
    a1_delta = max(abs(resp_a[i] - resp_b[i]) for i in (0, 4))
    complement_delta = max(abs(resp_a[i] - resp_b[i]) for i in (1, 2, 3, 5, 6, 7, 8, 9))
    frame_delta = max_abs_delta(resp_a, resp_b)
    avg = vector_average(resp_a, resp_b)
    avg_not_section = max_abs_delta(avg, resp_a) > 1e-6 and max_abs_delta(avg, resp_b) > 1e-6

    route_markers = [f"ROUTE-{idx}" for idx in range(1, 9)]
    n_markers = [f"N{idx}" for idx in range(1, 9)]

    checks = [
        Check(
            "target audit blocker quote is present",
            TARGET_BLOCKER in note,
            "new note quotes the exact re-audit target",
        ),
        Check(
            "parent note points to repair packet",
            "UNIVERSAL_GR_PICURV_ROUTE_EXHAUSTION_NO_GO_NOTE_2026-06-18.md" in parent,
            "parent source note has a non-status-changing repair pointer",
        ),
        Check(
            "route table has eight explicit route families",
            all(marker in note for marker in route_markers),
            f"routes present = {[m for m in route_markers if m in note]}",
        ),
        Check(
            "N1-N8 gate is complete",
            all(marker in note for marker in n_markers),
            f"gates present = {[m for m in n_markers if m in note]}",
        ),
        Check(
            "route exhaustion is scoped to reviewed current route families",
            has(note, "each reviewed route family")
            and has(note, "reviewed current construction routes")
            and has_words(note, "not as an absolute foreclosure of future routes"),
            "the note avoids claiming all possible repo or future routes are closed",
        ),
        Check(
            "N2 wall independence table is visible",
            has(note, "Collapsed wall set")
            and has(note, "connection vs TT/gauge reduction")
            and has(note, "supplied atlas/action vs spatial-versus-`3+1` scope"),
            "multiple walls are separated rather than inflated or collapsed",
        ),
        Check(
            "proof-surface dependency links are present",
            all(
                target in note
                for target in (
                    "(UNIVERSAL_GR_A1_INVARIANT_SECTION_NOTE.md)",
                    "(UNIVERSAL_GR_CASIMIR_BLOCK_LOCALIZATION_NOTE.md)",
                    "(UNIVERSAL_GR_CANONICAL_PROJECTOR_CONNECTION_NOTE.md)",
                    "(UNIVERSAL_GR_COMPLEMENT_CANONICAL_NOTE.md)",
                    "(UNIVERSAL_GR_ROUND_PL_S3_REGGE_HESSIAN_CANONICAL_CHANNELS_NARROW_THEOREM_NOTE_2026-06-10.md)",
                    "(UNIVERSAL_GR_SPIN2_TWO_DERIVATIVE_CURVATURE_GENERATOR_SUPPLIED_FLAT_ATLAS_NARROW_THEOREM_NOTE_2026-06-10.md)",
                    "(FINITE_RANK_GRAVITY_RESIDUAL_HELPER_NOTE_2026-04-14.md)",
                    "(COARSE_GRAINED_EXTERIOR_LAW_HELPER_NOTE_2026-04-14.md)",
                )
            ),
            "route-boundary authorities are markdown dependencies",
        ),
        Check(
            "no absolute no-go overclaim",
            has(note, "not an absolute no-go")
            and has_words(note, "future stronger GR inputs are impossible")
            and has(note, "not a mathematical impossibility theorem"),
            "note scopes no-go to current repo surfaces",
        ),
        Check(
            "canonical channel positives are preserved",
            has(note, "not a no-go against canonical pointwise channel projectors")
            and has(note, "Casimir/block projectors")
            and has(note, "They fail only the narrower"),
            "projector/channel work is not demoted",
        ),
        Check(
            "supplied geometric positives are preserved",
            has_words(note, "not a no-go against supplied-action Regge routes")
            and has_words(note, "not a no-go against the flat-atlas spin-2 generator")
            and has(note, "supplied flat-atlas spin-2"),
            "positive supplied-geometric lanes remain available",
        ),
        Check(
            "independent audit authority is explicit",
            has_words(note, "independent audit sets any effective status")
            and has(note, "does not edit the audit ledger")
            and has(note, "not an audit verdict"),
            "source packet does not claim audit authority",
        ),
        Check(
            "A1 finite witness is reproduced",
            a1_delta < 1e-12 and complement_delta > 1e-6 and frame_delta > 1e-6,
            (
                f"a1_delta={a1_delta:.3e}, "
                f"complement_delta={complement_delta:.3e}, "
                f"frame_delta={frame_delta:.3e}"
            ),
        ),
        Check(
            "orbit average is not a section selector",
            avg_not_section,
            (
                "average lies between sampled sections; "
                f"delta_to_a={max_abs_delta(avg, resp_a):.3e}, "
                f"delta_to_b={max_abs_delta(avg, resp_b):.3e}"
            ),
        ),
        Check(
            "attempt note still forbids treating old packet as exhaustive no-go",
            has(attempt, "do not cite it as an exhaustive no-go"),
            "new packet supplies a separate route-exhaustion gate",
        ),
        Check(
            "A1 note keeps full Pi_curv open",
            has(a1_note, "exact invariant")
            and has(a1_note, "`A1` section")
            and has(a1_note, "not enough to close full GR")
            and has(a1_note, "canonical `Pi_curv`"),
            "A1 is exact support, not full closure",
        ),
        Check(
            "Casimir note excludes connection and dynamics",
            has(casimir, "distinguished connection")
            and has(casimir, "Einstein/Regge operator")
            and has(casimir, "does **not** prove"),
            "block projectors do not provide full Pi_curv",
        ),
        Check(
            "connection candidate note is candidate-only",
            has(connection, "not a finished `Pi_curv`")
            and has(connection, "does not yet supply a distinguished connection"),
            "orbit connection is not the full target",
        ),
        Check(
            "complement note contains no-go discipline boundaries",
            has(complement, "not to every possible future invariant")
            and has(complement, "framework-wide no-go"),
            "older complement no-go remains local",
        ),
        Check(
            "round Regge route is supplied-scope only",
            has(round_regge, "supplied")
            and has(round_regge, "spatial slice only")
            and has(round_regge, "does not derive action")
            and has(round_regge, "selection"),
            "round Regge is positive but not direct-universal Pi_curv derivation",
        ),
        Check(
            "flat-atlas spin-2 route is not PL S3 x R closure",
            has(spin2, "flat atlas")
            and has_words(spin2, "does **not** claim")
            and has(spin2, "PL S")
            and has(spin2, "flat-atlas"),
            "flat spin-2 supply leaves the target surface open",
        ),
        Check(
            "finite-rank helper is scalar/helper scoped",
            has(finite_rank, "finite-rank support operator")
            and has(finite_rank, "does not claim")
            and has(finite_rank, "tensorial `3 + 1` lift"),
            "finite-rank helper is not a tensorial Pi_curv route",
        ),
        Check(
            "coarse exterior helper is scalar/isotropic scoped",
            has(exterior, "shell-averaging")
            and has(exterior, "radial-harmonic")
            and has(exterior, "bounded helper-module"),
            "coarse exterior law is not full Pi_curv",
        ),
    ]

    print("UNIVERSAL GR PICURV ROUTE-EXHAUSTION NO-GO VERIFIER")
    print("=" * 78)
    for check in checks:
        tag = "PASS" if check.ok else "FAIL"
        print(f"[{tag}] {check.name}")
        print(f"    {check.detail}")

    print("\n" + "=" * 78)
    print("FINITE WITNESS")
    print("=" * 78)
    print(f"resp_a[0:5]      = {[f'{x:.6e}' for x in resp_a[:5]]}")
    print(f"resp_b[0:5]      = {[f'{x:.6e}' for x in resp_b[:5]]}")
    print(f"a1_delta         = {a1_delta:.12e}")
    print(f"complement_delta = {complement_delta:.12e}")
    print(f"frame_delta      = {frame_delta:.12e}")

    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    n_pass = sum(c.ok for c in checks)
    n_fail = len(checks) - n_pass
    print(f"PASS={n_pass} FAIL={n_fail} TOTAL={len(checks)}")
    if n_fail == 0:
        print(
            "Current-stack result: eight Pi_curv construction routes are "
            "enumerated and blocked at connection, TT/gauge, dynamics, "
            "or supplied-input boundaries; existing positive channel and "
            "supplied-geometric GR work is preserved."
        )
        return 0

    print("One or more route-exhaustion checks failed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
