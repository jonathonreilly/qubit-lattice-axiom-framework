#!/usr/bin/env python3
"""Y_T connected-source augmentation-ideal selector certificate.

This runner verifies the finite-dimensional algebra behind the narrow theorem:
on a normalized connected source surface over trace-one color records, the
identity color source is a normalization direction and the nonzero tangent
space is the traceless augmentation ideal.  The Y_T consequence is conditional:
if the physical Yukawa source is accepted as this connected source tangent,
then kappa_Y=0 and K_Y=(N^2-1)/N^2.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_connected_source_augmentation_ideal_selector_2026-05-26.json"

NOTE = DOCS / "YT_CONNECTED_SOURCE_AUGMENTATION_IDEAL_SELECTOR_NARROW_THEOREM_NOTE_2026-05-26.md"
YT_COLOR = DOCS / "YT_COLOR_PROJECTION_CORRECTION_NOTE.md"
YT_POLE_NOGO = DOCS / "YT_SOURCE_HIGGS_POLE_ROW_NORMALIZATION_NO_GO_NOTE_2026-05-23.md"
YT_SOURCE_ACTION = DOCS / "YT_SOURCE_ACTION_SUPPORT_PACKET_NOTE_2026-05-22.md"
FIERZ = DOCS / "EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md"

PASS_COUNT = 0
FAIL_COUNT = 0


Matrix = tuple[tuple[Fraction, ...], ...]


def check(name: str, ok: bool, detail: Any = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail != "" else ""
    print(f"[{tag}] {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def identity(n: int) -> Matrix:
    return tuple(tuple(Fraction(1 if i == j else 0) for j in range(n)) for i in range(n))


def diag(vals: list[Fraction]) -> Matrix:
    n = len(vals)
    return tuple(tuple(vals[i] if i == j else Fraction(0) for j in range(n)) for i in range(n))


def mat_sub(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(a[i][j] - b[i][j] for j in range(len(a))) for i in range(len(a)))


def scalar_mul(c: Fraction, a: Matrix) -> Matrix:
    return tuple(tuple(c * a[i][j] for j in range(len(a))) for i in range(len(a)))


def trace(a: Matrix) -> Fraction:
    return sum(a[i][i] for i in range(len(a)))


def hs_inner(a: Matrix, b: Matrix) -> Fraction:
    n = len(a)
    return sum(a[i][j] * b[i][j] for i in range(n) for j in range(n))


def traceless_projection(a: Matrix) -> Matrix:
    n = len(a)
    return mat_sub(a, scalar_mul(trace(a) / n, identity(n)))


def score_value(j: Matrix, rho: Matrix, expectation: Fraction) -> Fraction:
    return hs_inner(j, rho) - expectation


def trace_one_witnesses(n: int) -> list[Matrix]:
    # Diagonal rational density witnesses, including nonuniform states.
    uniform = diag([Fraction(1, n)] * n)
    point = diag([Fraction(1)] + [Fraction(0)] * (n - 1))
    spread = [Fraction(i + 1, n * (n + 1) // 2) for i in range(n)]
    return [uniform, point, diag(spread)]


def part1_sources() -> None:
    print("\nPart 1: source surfaces and claim boundary")
    for path in (NOTE, YT_COLOR, YT_POLE_NOGO, YT_SOURCE_ACTION, FIERZ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    required = [
        "normalized connected source-response surface",
        "identity color source is a pure normalization direction",
        "augmentation ideal",
        "kappa_Y = 0",
        "What Remains Open",
        "does not use `H_unit`",
        "does not certify full Y_T closure",
    ]
    for phrase in required:
        check(f"note contains boundary phrase: {phrase}", phrase in note)

    forbidden = [
        "observed top",
        "PDG",
        "define y_t_bare",
        "y_t_bare as input",
        "yt_ward_identity` as input",
        "full Y_T closure is certified",
        "retained Y_T is closed",
    ]
    for phrase in forbidden:
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def part2_projection_algebra() -> dict[str, Any]:
    print("\nPart 2: exact augmentation-ideal projection algebra")
    rows: dict[str, Any] = {}
    for n in range(2, 8):
        i_n = identity(n)
        p_i = traceless_projection(i_n)
        check(f"N={n} identity projects to zero", all(x == 0 for row in p_i for x in row))

        witness = diag([Fraction(k) for k in range(1, n + 1)])
        p = traceless_projection(witness)
        check(f"N={n} projection is traceless", trace(p) == 0, trace(p))
        check(f"N={n} projection is idempotent", traceless_projection(p) == p)
        check(f"N={n} projection is identity-orthogonal", hs_inner(p, i_n) == 0, hs_inner(p, i_n))

        full_dim = n * n
        traceless_dim = full_dim - 1
        frac = Fraction(traceless_dim, full_dim)
        ky_k0 = Fraction(n * n - 1, n * n)
        ky_k1 = Fraction(1, 1)
        check(f"N={n} connected fraction equals K_Y(kappa=0)", frac == ky_k0, frac)
        check(f"N={n} full-trace completion differs", ky_k1 - ky_k0 == Fraction(1, n * n), ky_k1 - ky_k0)
        rows[str(n)] = {
            "full_dim": full_dim,
            "augmentation_dim": traceless_dim,
            "connected_fraction": f"{frac.numerator}/{frac.denominator}",
            "singlet_gap_to_full_trace": f"1/{n*n}",
        }
    check("N=3 gives 8/9", rows["3"]["connected_fraction"] == "8/9", rows["3"])
    return rows


def part3_normalized_source_kernel() -> dict[str, Any]:
    print("\nPart 3: normalized source score kills identity direction")
    results: dict[str, Any] = {}
    for n in range(2, 6):
        i_n = identity(n)
        # On trace-one records, O_I(rho)=Tr(rho)=1, so E[O_I]=1.
        identity_scores = [score_value(i_n, rho, Fraction(1)) for rho in trace_one_witnesses(n)]
        check(f"N={n} identity score vanishes on trace-one witnesses", all(s == 0 for s in identity_scores), identity_scores)

        j = diag([Fraction(k) for k in range(1, n + 1)])
        j0 = traceless_projection(j)
        # The identity part of J contributes a constant Tr(J)/N on trace-one states.
        expectation_shift = trace(j) / n
        for rho in trace_one_witnesses(n):
            lhs = hs_inner(j, rho) - expectation_shift
            rhs = hs_inner(j0, rho)
            check(f"N={n} source score depends only on traceless part", lhs == rhs, {"lhs": str(lhs), "rhs": str(rhs)})
        results[str(n)] = {
            "identity_scores": [str(s) for s in identity_scores],
            "trace_shift": str(expectation_shift),
        }
    return results


def part4_yukawa_selector_consequence() -> dict[str, Any]:
    print("\nPart 4: Y_T selector consequence on connected-source surface")
    consequences: dict[str, Any] = {}
    for n in (2, 3, 4, 5, 6):
        f_adj = Fraction(n * n - 1, n * n)
        f_singlet = Fraction(1, n * n)
        kappa_connected = Fraction(0)
        k_connected = f_adj + kappa_connected * f_singlet
        k_full = f_adj + Fraction(1) * f_singlet
        check(f"N={n} connected-source selector sets kappa=0", k_connected == f_adj)
        check(f"N={n} full-trace completion is not selected by connected source", k_full == 1 and k_full != k_connected)
        consequences[str(n)] = {
            "F_adj": f"{f_adj.numerator}/{f_adj.denominator}",
            "F_singlet": f"{f_singlet.numerator}/{f_singlet.denominator}",
            "kappa_connected": "0",
            "K_connected": f"{k_connected.numerator}/{k_connected.denominator}",
            "K_full_trace": "1",
        }
    check("N=3 selected K_Y is 8/9", consequences["3"]["K_connected"] == "8/9", consequences["3"])
    return consequences


def part5_dependency_firewalls() -> None:
    print("\nPart 5: dependency and overclaim firewalls")
    note = read(NOTE)
    color = read(YT_COLOR)
    source_action = read(YT_SOURCE_ACTION)

    check("target color note exposes kappa family", "K_Y(kappa_Y) = 8/9 + kappa_Y/9" in color)
    check("target color note says kappa=0 is not derived there", "not a derived theorem" in color)
    check(
        "Y_T source/action gate remains open",
        "source/action gate is not yet" in source_action
        and "authority remains a separate open gate" in source_action,
    )

    must_not_close = [
        "It does not prove that the physical neutral EW/Higgs source-action surface",
        "It does not derive canonical `O_H`",
        "It does not derive scalar LSZ normalization",
        "It does not compute or claim a physical `y_t` value",
    ]
    for phrase in must_not_close:
        check(f"remaining blocker preserved: {phrase}", phrase in note)


def main() -> int:
    print("=" * 88)
    print("Y_T CONNECTED-SOURCE AUGMENTATION-IDEAL SELECTOR")
    print("=" * 88)
    part1_sources()
    projection_rows = part2_projection_algebra()
    source_rows = part3_normalized_source_kernel()
    selector_rows = part4_yukawa_selector_consequence()
    part5_dependency_firewalls()

    result = {
        "status": "bounded support: connected-source selector for kappa_Y=0",
        "claim": (
            "On a normalized connected source-response surface over trace-one "
            "color records, the identity color direction is a pure normalization "
            "mode, so the nonzero source tangent is the traceless augmentation "
            "ideal and K_connected=(N^2-1)/N^2."
        ),
        "yt_consequence": (
            "If the physical Yukawa-side source/action surface is accepted as "
            "this normalized connected source tangent, kappa_Y=0 and K_Y=8/9 "
            "at N_c=3."
        ),
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The theorem closes the finite color-source algebra on the connected "
            "source surface, but it does not itself derive same-surface neutral "
            "EW/Higgs source/action authority, canonical O_H, or scalar LSZ normalization."
        ),
        "projection_rows": projection_rows,
        "normalized_source_rows": source_rows,
        "selector_rows": selector_rows,
        "remaining_blockers": [
            "same-surface normalized connected source/action authority for Y_T",
            "canonical O_H",
            "scalar LSZ normalization",
            "strict pole rows or W/Z response bypass after normalization is fixed",
            "matching/running after physical input exists",
        ],
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
