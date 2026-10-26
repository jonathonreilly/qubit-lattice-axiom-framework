#!/usr/bin/env python3
"""Finite supplied three-entry PMNS bank and stipulated source-cubic filter.
The target, bank and I_src>0 condition are supplied. Numerical bisection
is a branch candidate, not a global threshold or physical selection proof.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ['docs/DM_PMNS_UPPER_OCTANT_SOURCE_CUBIC_SELECTOR_THEOREM_NOTE_2026-04-20.md', 'scripts/frontier_pmns_theta23_upper_octant_chamber_closure_prediction.py', 'scripts/frontier_sigma_hier_uniqueness_theorem.py']

import math

import numpy as np

from frontier_pmns_theta23_upper_octant_chamber_closure_prediction import boundary_distance
from frontier_sigma_hier_uniqueness_theorem import H_mat, jarlskog_sin_dcp, pmns_for_permutation

np.set_printoptions(precision=12, suppress=True, linewidth=140)

PASS_COUNT = 0
FAIL_COUNT = 0

SIGMA_210 = (2, 1, 0)
SIGMA_201 = (2, 0, 1)

CHAMBER_ROOTS = {
    "Basin 1": (0.6570613422097703, 0.9338063437590336, 0.7150423295873919),
    "Basin 2": (28.006188289564736, 20.721831213931072, 5.011599458304925),
    "Basin X": (21.128263668693783, 12.680028023619366, 2.08923480586059),
}


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def source_cubic(H: np.ndarray) -> float:
    return float(np.imag(H[0, 1] * H[1, 2] * H[2, 0]))


def pmns_data(point: tuple[float, float, float], perm: tuple[int, int, int]) -> dict[str, float]:
    H = H_mat(*point)
    evals, vecs = np.linalg.eigh(H)
    P = pmns_for_permutation(vecs, perm)
    s13sq = abs(P[0, 2]) ** 2
    c13sq = max(1.0 - s13sq, 1e-18)
    s12sq = abs(P[0, 1]) ** 2 / c13sq
    s23sq = abs(P[1, 2]) ** 2 / c13sq
    return {
        "s12sq": float(s12sq),
        "s13sq": float(s13sq),
        "s23sq": float(s23sq),
        "sin_dcp": float(jarlskog_sin_dcp(P)),
    }


def central_theta23_threshold() -> float:
    lo = 0.53
    hi = 0.55
    dlo, _, _ = boundary_distance(0.307, 0.0218, lo)
    dhi, _, _ = boundary_distance(0.307, 0.0218, hi)
    if dlo >= 0 or dhi <= 0:
        raise RuntimeError("threshold bracket failed")
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        dmid, _, _ = boundary_distance(0.307, 0.0218, mid)
        if dmid > 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def main() -> int:
    print("=" * 88)
    print("SUPPLIED THREE-BANK UPPER-OCTANT / SOURCE-CUBIC DIAGNOSTIC")
    print("=" * 88)

    print()
    print("Part 1: numerical threshold candidate on the supplied branch")
    threshold = central_theta23_threshold()
    print(f"   central threshold s23^2_min = {threshold:.12f}")
    check("The central theta_23 threshold lies above maximal mixing", threshold > 0.5, f"threshold={threshold:.12f}")
    check("The central theta_23 threshold matches 0.540970 to 6 digits", abs(threshold - 0.540970) < 5e-7)

    basin1_210 = pmns_data(CHAMBER_ROOTS["Basin 1"], SIGMA_210)
    basin1_201 = pmns_data(CHAMBER_ROOTS["Basin 1"], SIGMA_201)
    check(
        "At fixed H, the mu<->tau partner sends s23^2 to 1 - s23^2",
        abs(basin1_210["s23sq"] + basin1_201["s23sq"] - 1.0) < 1e-12,
        f"sum={basin1_210['s23sq'] + basin1_201['s23sq']:.12f}",
    )
    check(
        "At the supplied fixed H, swapping the mu/tau row labels flips the computed CP sign",
        basin1_210["sin_dcp"] * basin1_201["sin_dcp"] < 0.0,
        f"sin_dcp=({basin1_210['sin_dcp']:+.12f},{basin1_201['sin_dcp']:+.12f})",
    )
    check(
        "The lower-octant partner sits below the chamber threshold",
        basin1_201["s23sq"] < threshold < basin1_210["s23sq"],
        f"(lower,thr,upper)=({basin1_201['s23sq']:.12f},{threshold:.12f},{basin1_210['s23sq']:.12f})",
    )

    print()
    print("Part 2: upper-octant comparisons on the supplied three-entry bank")
    upper_octant_survivors: list[tuple[str, tuple[int, int, int], float, float]] = []
    for name, point in CHAMBER_ROOTS.items():
        for perm in (SIGMA_210, SIGMA_201):
            obs = pmns_data(point, perm)
            if obs["s23sq"] > 0.5:
                upper_octant_survivors.append((name, perm, obs["s23sq"], obs["sin_dcp"]))
                print(f"   {name}, sigma={perm}: s23^2={obs['s23sq']:.12f}, sin_dcp={obs['sin_dcp']:+.12f}")

    check(
        "The supplied three-entry bank has the listed three upper-octant labeled entries",
        upper_octant_survivors == [
            ("Basin 1", SIGMA_210, upper_octant_survivors[0][2], upper_octant_survivors[0][3]),
            ("Basin 2", SIGMA_210, upper_octant_survivors[1][2], upper_octant_survivors[1][3]),
            ("Basin X", SIGMA_201, upper_octant_survivors[2][2], upper_octant_survivors[2][3]),
        ],
        f"survivors={[(n, p) for n, p, _, _ in upper_octant_survivors]}",
    )
    check(
        "Every upper-octant survivor carries the same target s23^2 = 0.545",
        all(abs(s23 - 0.545) < 1e-12 for _, _, s23, _ in upper_octant_survivors),
    )

    print()
    print("Part 3: stipulated I_src>0 filters the supplied bank")
    source_signs = {}
    for name, point in CHAMBER_ROOTS.items():
        H = H_mat(*point)
        I_src = source_cubic(H)
        source_signs[name] = I_src
        print(f"   {name}: I_src={I_src:+.12f}")
    check("Basin 1 has positive source cubic orientation", source_signs["Basin 1"] > 0.0)
    check("Basin 2 has negative source cubic orientation", source_signs["Basin 2"] < 0.0)
    check("Basin X has negative source cubic orientation", source_signs["Basin X"] < 0.0)

    selected = [(name, perm) for name, perm, _, _ in upper_octant_survivors if source_signs[name] > 0.0]
    check(
        "Among the supplied upper-octant entries, stipulated I_src > 0 keeps Basin 1",
        selected == [("Basin 1", SIGMA_210)],
        f"selected={selected}",
    )

    print()
    print("Part 4: resulting supplied-table values, not physical selection")
    final_obs = pmns_data(CHAMBER_ROOTS["Basin 1"], SIGMA_210)
    check(
        "The stipulated finite filter returns the label (2,1,0)",
        selected == [("Basin 1", SIGMA_210)],
    )
    check(
        "The filtered supplied point has negative computed sin(delta_CP)",
        final_obs["sin_dcp"] < 0.0,
        f"sin_dcp={final_obs['sin_dcp']:+.12f}",
    )
    check(
        "The filtered supplied point reproduces the supplied PMNS target",
        abs(final_obs["s12sq"] - 0.307) < 1e-12
        and abs(final_obs["s13sq"] - 0.0218) < 1e-12
        and abs(final_obs["s23sq"] - 0.545) < 1e-12,
        f"(s12,s13,s23)=({final_obs['s12sq']:.12f},{final_obs['s13sq']:.12f},{final_obs['s23sq']:.12f})",
    )

    print()
    print("=" * 88)
    print("RESULT")
    print("=" * 88)
    print("  Finite supplied-bank/target comparisons with stipulated I_src(H)>0 only.")
    print("  No exhaustive chamber, physical row assignment, CP-sign selection or I12 closure.")
    print("  Numerical branch threshold and physical selector/target derivations remain open.")
    print()
    print(f"PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    raise SystemExit(main())
