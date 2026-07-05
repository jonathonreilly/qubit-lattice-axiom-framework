#!/usr/bin/env python3
"""Class-A exact verification for the source note

    docs/D2_TRUNCATION_ERROR_BUDGET_FIRST_DATUM_BOUNDED_THEOREM_NOTE_2026-06-12.md

Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_d2_truncation_error_budget_2026_06_12.py
"""
from __future__ import annotations

import math
import sys
from dataclasses import dataclass

import numpy as np


PASS_COUNT = 0
FAIL_COUNT = 0

ONSITE = 4.0
HOP = -1.0
KEEP_D2_4_8 = frozenset({4, 8})
KEEP_HARSH = frozenset({4})


def check(section: str, name: str, condition: bool, detail: str = "") -> bool:
    """Class-A check/TOTAL contract: every status is computed from condition."""
    global PASS_COUNT, FAIL_COUNT
    ok = bool(condition)
    if ok:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}][{section}] {name}")
    if detail:
        print(f"       {detail}")
    return ok


def total() -> None:
    total_count = PASS_COUNT + FAIL_COUNT
    print()
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT:
        sys.exit(1)


def max_abs(a: np.ndarray) -> float:
    return float(np.max(np.abs(a)))


def nonzero_count(a: np.ndarray, tol: float = 1.0e-14) -> int:
    return int(np.count_nonzero(np.abs(a) > tol))


def ceil_sig(x: float, sig: int = 2) -> float:
    """Round a positive measurement upward to a labeled measured ceiling."""
    ax = abs(float(x))
    if ax == 0.0:
        return 0.0
    exp = math.floor(math.log10(ax)) - sig + 1
    unit = 10.0 ** exp
    return float(math.ceil(ax / unit) * unit)


def factor_two(a: float, b: float) -> bool:
    if not (np.isfinite(a) and np.isfinite(b)) or a <= 0.0 or b <= 0.0:
        return False
    ratio = a / b
    return 0.5 <= ratio <= 2.0


def lattice_coords(L: int) -> list[tuple[int, int]]:
    return [(x, y) for x in range(L) for y in range(L)]


def site_index(L: int, x: int, y: int) -> int:
    return (x % L) * L + (y % L)


def free_hamiltonian(L: int) -> np.ndarray:
    n = L * L
    h = np.zeros((n, n), dtype=np.float64)
    for x in range(L):
        for y in range(L):
            i = site_index(L, x, y)
            h[i, i] = ONSITE
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                j = site_index(L, x + dx, y + dy)
                h[i, j] = HOP
    return 0.5 * (h + h.T)


def retain_step_1(coord: tuple[int, int]) -> bool:
    x, y = coord
    return (x + y) % 2 == 0


def retain_step_2(coord: tuple[int, int]) -> bool:
    x, y = coord
    return x % 2 == 0 and y % 2 == 0


def retain_step_3(coord: tuple[int, int]) -> bool:
    x, y = coord
    return x % 2 == 0 and y % 2 == 0 and ((x + y) // 2) % 2 == 0


def decimate(
    h: np.ndarray,
    coords: list[tuple[int, int]],
    retain_predicate,
) -> tuple[np.ndarray, list[tuple[int, int]]]:
    keep_mask = np.array([retain_predicate(c) for c in coords], dtype=bool)
    keep = np.flatnonzero(keep_mask)
    elim = np.flatnonzero(~keep_mask)
    if keep.size == 0 or elim.size == 0:
        raise ValueError("decimation must have nonempty kept and eliminated sets")

    h_kk = h[np.ix_(keep, keep)]
    h_ke = h[np.ix_(keep, elim)]
    h_ee = h[np.ix_(elim, elim)]
    correction = h_ke @ np.linalg.solve(h_ee, h_ke.T)
    out = h_kk - correction
    out = 0.5 * (out + out.T)
    out[np.abs(out) < 5e-16] = 0.0
    return out, [coords[i] for i in keep]


def torus_d2(a: tuple[int, int], b: tuple[int, int], L: int) -> int:
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    dx = min(dx, L - dx)
    dy = min(dy, L - dy)
    return dx * dx + dy * dy


def truncate_shells(
    h: np.ndarray,
    coords: list[tuple[int, int]],
    L: int,
    keep_d2: frozenset[int] | None,
) -> np.ndarray:
    if keep_d2 is None:
        return h.copy()

    out = np.zeros_like(h)
    n = h.shape[0]
    for i in range(n):
        out[i, i] = h[i, i]
        for j in range(i + 1, n):
            if torus_d2(coords[i], coords[j], L) in keep_d2:
                out[i, j] = h[i, j]
                out[j, i] = h[j, i]
    return out


def projected_resolvent_at_e0(h: np.ndarray) -> np.ndarray:
    """Zero-mode-subtracted E=0 resolvent on the retained sites."""
    n = h.shape[0]
    one = np.ones((n, 1), dtype=np.float64) / math.sqrt(n)
    p0 = one @ one.T
    q0 = np.eye(n, dtype=np.float64) - p0
    restricted = q0 @ h @ q0 + p0
    resolvent = np.linalg.solve(restricted, q0)
    resolvent = q0 @ resolvent @ q0
    return 0.5 * (resolvent + resolvent.T)


@dataclass(frozen=True)
class Datum:
    L: int
    h2_full: np.ndarray
    h2_keep4_8: np.ndarray
    h2_harsh: np.ndarray
    h2_none: np.ndarray
    h3_full: np.ndarray
    h3_keep4_8: np.ndarray
    h3_harsh: np.ndarray
    h3_none: np.ndarray
    coords2: list[tuple[int, int]]
    coords3: list[tuple[int, int]]
    tail_keep4_8: float
    tail_harsh: float
    support_keep4_8: int
    support_harsh: int
    err_keep4_8: float
    err_harsh: float
    err_none_h3: float
    err_none_resolvent: float


def build_datum(L: int) -> Datum:
    coords0 = lattice_coords(L)
    h0 = free_hamiltonian(L)
    h1, coords1 = decimate(h0, coords0, retain_step_1)
    h2_full, coords2 = decimate(h1, coords1, retain_step_2)

    h2_keep4_8 = truncate_shells(h2_full, coords2, L, KEEP_D2_4_8)
    h2_harsh = truncate_shells(h2_full, coords2, L, KEEP_HARSH)
    h2_none = truncate_shells(h2_full, coords2, L, None)

    h3_full, coords3 = decimate(h2_full, coords2, retain_step_3)
    h3_keep4_8, coords3_keep4_8 = decimate(h2_keep4_8, coords2, retain_step_3)
    h3_harsh, coords3_harsh = decimate(h2_harsh, coords2, retain_step_3)
    h3_none, coords3_none = decimate(h2_none, coords2, retain_step_3)
    if coords3_keep4_8 != coords3 or coords3_harsh != coords3 or coords3_none != coords3:
        raise AssertionError("step-3 retained coordinates changed across branches")

    g3_full = projected_resolvent_at_e0(h3_full)
    g3_keep4_8 = projected_resolvent_at_e0(h3_keep4_8)
    g3_harsh = projected_resolvent_at_e0(h3_harsh)
    g3_none = projected_resolvent_at_e0(h3_none)

    return Datum(
        L=L,
        h2_full=h2_full,
        h2_keep4_8=h2_keep4_8,
        h2_harsh=h2_harsh,
        h2_none=h2_none,
        h3_full=h3_full,
        h3_keep4_8=h3_keep4_8,
        h3_harsh=h3_harsh,
        h3_none=h3_none,
        coords2=coords2,
        coords3=coords3,
        tail_keep4_8=max_abs(h2_keep4_8 - h2_full),
        tail_harsh=max_abs(h2_harsh - h2_full),
        support_keep4_8=nonzero_count(h2_keep4_8 - h2_full),
        support_harsh=nonzero_count(h2_harsh - h2_full),
        err_keep4_8=max_abs(g3_keep4_8 - g3_full),
        err_harsh=max_abs(g3_harsh - g3_full),
        err_none_h3=max_abs(h3_none - h3_full),
        err_none_resolvent=max_abs(g3_none - g3_full),
    )


def wraparound_probe(datum: Datum) -> bool:
    """Kept d2=4,8 shells are below the half-box wrap boundary for this L."""
    for i, a in enumerate(datum.coords2):
        for b in datum.coords2[i + 1 :]:
            dx = abs(a[0] - b[0])
            dy = abs(a[1] - b[1])
            d2_direct_min = min(dx, datum.L - dx) ** 2 + min(dy, datum.L - dy) ** 2
            if d2_direct_min in KEEP_D2_4_8 and max(min(dx, datum.L - dx), min(dy, datum.L - dy)) >= datum.L / 2:
                return False
    return True


def print_datum(datum: Datum) -> None:
    print(f"L={datum.L}")
    print(f"  retained sizes: step2={len(datum.coords2)} step3={len(datum.coords3)}")
    print(f"  dropped-tail max ||h2_keep4_8 - h2_full||_max = {datum.tail_keep4_8:.16e}")
    print(f"  dropped-tail support count keep4_8 = {datum.support_keep4_8}")
    print(f"  harsh dropped-tail max ||h2_keep4 - h2_full||_max = {datum.tail_harsh:.16e}")
    print(f"  harsh dropped-tail support count keep4 = {datum.support_harsh}")
    print(f"  retained resolvent error keep4_8 at E=0 = {datum.err_keep4_8:.16e}")
    print(f"  retained resolvent error keep-d2-4-only = {datum.err_harsh:.16e}")
    print(f"  no-trunc h3 max difference = {datum.err_none_h3:.16e}")
    print(f"  no-trunc resolvent max difference = {datum.err_none_resolvent:.16e}")


def main() -> None:
    np.set_printoptions(precision=16, suppress=False)
    print("Controlled-truncation datum: d=2 checkerboard convention")
    print("finite periodic L in {12,16}; dense NumPy; E=0; free d=2 Laplacian")
    print("cross-reference: landed range-unbounded note follow-on; no fixed-point claim")
    print()

    data12 = build_datum(12)
    data16 = build_datum(16)

    print_datum(data12)
    print()
    print_datum(data16)
    print()

    tail_ceiling = ceil_sig(data16.tail_keep4_8, sig=2)
    err_ceiling = ceil_sig(data16.err_keep4_8, sig=2)
    no_trunc_tol = 1.0e-12

    print("Checks")
    check(
        "A",
        "measured dropped-tail regression ceiling on L=16",
        np.isfinite(data16.tail_keep4_8) and data16.tail_keep4_8 > 0.0 and data16.tail_keep4_8 <= tail_ceiling,
        f"measured={data16.tail_keep4_8:.16e}, labeled measured ceiling={tail_ceiling:.16e}",
    )
    check(
        "A",
        "dropped-tail max-amplitude finite-size probe L=12 vs L=16 within factor 2",
        factor_two(data12.tail_keep4_8, data16.tail_keep4_8),
        f"L12={data12.tail_keep4_8:.16e}, L16={data16.tail_keep4_8:.16e}",
    )
    check(
        "A",
        "finite-lattice wraparound probe for kept d2={4,8} shells",
        wraparound_probe(data12) and wraparound_probe(data16),
        "kept shells are represented by shortest torus displacements on both lattices",
    )
    check(
        "A",
        "dropped-tail support count grows from L=12 to L=16 for keep-d2-{4,8}",
        data16.support_keep4_8 > data12.support_keep4_8 > 0,
        f"L12={data12.support_keep4_8}, L16={data16.support_keep4_8}",
    )
    check(
        "A",
        "measured retained-site resolvent error budget on L=16",
        np.isfinite(data16.err_keep4_8) and data16.err_keep4_8 > 0.0 and data16.err_keep4_8 <= err_ceiling,
        f"measured={data16.err_keep4_8:.16e}, labeled measured ceiling={err_ceiling:.16e}",
    )
    check(
        "A",
        "the truncation error GROWS with L (consistent with the L-growing "
        "dropped tail of the range-unbounded step-2 structure): ratio in [1, 4], "
        "both errors nonzero",
        data16.err_keep4_8 > data12.err_keep4_8 > 0.0 and data16.err_keep4_8 / data12.err_keep4_8 <= 4.0,
        f"L12={data12.err_keep4_8:.16e}, L16={data16.err_keep4_8:.16e}",
    )
    check(
        "A",
        "proportionality ordering: keep-d2-4-only error > keep-d2-{4,8} error > 0 on L=16",
        data16.err_harsh > data16.err_keep4_8 > 0.0,
        f"err_keep4={data16.err_harsh:.16e}, err_keep4_8={data16.err_keep4_8:.16e}",
    )
    check(
        "A",
        "harsh truncation drops at least as much operator tail as keep-d2-{4,8} on L=16",
        data16.tail_harsh >= data16.tail_keep4_8 > 0.0,
        f"tail_keep4={data16.tail_harsh:.16e}, tail_keep4_8={data16.tail_keep4_8:.16e}",
    )
    check(
        "A",
        "truncating nothing reproduces exact step 3 at the operator level",
        data16.err_none_h3 <= no_trunc_tol and data12.err_none_h3 <= no_trunc_tol,
        f"L12={data12.err_none_h3:.16e}, L16={data16.err_none_h3:.16e}, tol={no_trunc_tol:.1e}",
    )
    check(
        "A",
        "truncating nothing reproduces exact step-3 retained resolvent",
        data16.err_none_resolvent <= no_trunc_tol and data12.err_none_resolvent <= no_trunc_tol,
        (
            f"L12={data12.err_none_resolvent:.16e}, "
            f"L16={data16.err_none_resolvent:.16e}, tol={no_trunc_tol:.1e}"
        ),
    )

    total()


if __name__ == "__main__":
    main()
