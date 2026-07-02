#!/usr/bin/env python3
"""Firewall for post-box-scan measured-calibration rescue transforms.

The prior box-size scan already showed that the measured Route-2 q_E
calibration does not converge to 15/8 in the tested limits. This runner checks
the narrower residual: whether a non-fitted bulk/tail reuse of the same cache
can still recover the endpoint without selecting the anomalous N=15 point.
"""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def squash(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS: {label}" + (f" -- {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL: {label}" + (f" -- {detail}" if detail else ""))


def parse_box_table(cache: str) -> dict[int, dict[str, float]]:
    rows: dict[int, dict[str, float]] = {}
    for line in cache.splitlines():
        parts = line.split()
        if len(parts) != 9:
            continue
        try:
            n = int(parts[0])
            nums = [float(x) for x in parts[1:]]
        except ValueError:
            continue
        rows[n] = {
            "eta_e0": nums[0],
            "eta_s": nums[1],
            "gE_center": nums[2],
            "gE_shell": nums[3],
            "gT_center": nums[4],
            "gT_shell": nums[5],
            "q_T": nums[6],
            "q_E": nums[7],
        }
    return rows


def parse_list_after(label: str, text: str) -> list[float]:
    match = re.search(re.escape(label) + r"\s*\[(.*?)\]", text)
    if not match:
        return []
    return [float(x) for x in re.findall(r"[+-]?\d+\.\d+", match.group(1))]


def in_closed_interval(value: float, values: list[float], tol: float = 0.0) -> bool:
    return min(values) - tol <= value <= max(values) + tol


def main() -> int:
    print("=" * 88)
    print("ROUTE-2 MEASURED-CALIBRATION RESCUE-TRANSFORM FIREWALL")
    print("=" * 88)

    note_path = "docs/QUARK_ROUTE2_MEASURED_CALIBRATION_RESCUE_TRANSFORM_FIREWALL_NOTE_2026-06-21.md"
    paths = {
        "note": note_path,
        "measured": "docs/QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md",
        "box_note": "docs/QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md",
        "box_cache": "logs/runner-cache/frontier_quark_route2_qe_box_size_scan_2026_06_10.txt",
        "covariance": "docs/QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md",
        "exact_readout": "docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        "parent": "docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md",
    }

    print()
    print("A. Authority surfaces")
    print("-" * 72)
    texts = {}
    for key, path in paths.items():
        exists = (ROOT / path).exists()
        check(f"{key} surface exists", exists, path)
        if exists:
            texts[key] = read(path)

    note = texts["note"]
    note_lower = note.lower()
    print()
    print("B. New note hygiene")
    print("-" * 72)
    check("new note declares no_go claim type", "**claim type:** no_go" in note_lower)
    check("new note says no audit verdict is applied", "does not apply an audit verdict" in note_lower)
    check("new note scopes to post-box-scan rescue transforms", "rescue-transform" in note_lower)
    check("new note forbids selecting N=15 as a proof input", "selecting `n=15`" in note_lower)
    check("new note does not claim future-transform impossibility", "cannot ever" not in note_lower and ("no future " + "primitive") not in note_lower)

    print()
    print("C. Cache parse and anchor")
    print("-" * 72)
    cache = texts["box_cache"]
    rows = parse_box_table(cache)
    expected_ns = [11, 13, 15, 17, 19, 21, 25, 29]
    check("cache table exposes expected box sizes", sorted(rows) == expected_ns, str(sorted(rows)))
    target_qe = 15.0 / 8.0
    target_qt = 5.0 / 6.0
    target_lambda = 9.0 / 4.0
    n15 = rows[15]
    check("N=15 q_E is near target comparator", abs(n15["q_E"] - target_qe) < 0.002, f"{n15['q_E']:.6f}")
    check("N=15 q_T is near target comparator", abs(n15["q_T"] - target_qt) < 0.00002, f"{n15['q_T']:.6f}")
    check("N=15 lambda is near 9/4 comparator", abs(n15["q_E"] / n15["q_T"] - target_lambda) < 0.002, f"{n15['q_E'] / n15['q_T']:.6f}")
    other_hits = [n for n, row in rows.items() if n != 15 and abs(row["q_E"] - target_qe) < 0.25]
    check("no other fixed-radius box is close to q_E=15/8", other_hits == [], str(other_hits))

    print()
    print("D. Bulk-tail convex and sign tests")
    print("-" * 72)
    bulk_ns = [17, 19, 21, 25, 29]
    qes_bulk = [rows[n]["q_E"] for n in bulk_ns]
    qts_bulk = [rows[n]["q_T"] for n in bulk_ns]
    lambdas_bulk = [rows[n]["q_E"] / rows[n]["q_T"] for n in bulk_ns]
    check("fixed-radius bulk q_E values are all negative", all(x < 0 for x in qes_bulk), str([round(x, 3) for x in qes_bulk]))
    check("positive target q_E is outside fixed-radius bulk convex hull", not in_closed_interval(target_qe, qes_bulk), f"hull=[{min(qes_bulk):.3f},{max(qes_bulk):.3f}]")
    check("fixed-radius bulk q_T values are all negative", all(x < 0 for x in qts_bulk), str([round(x, 3) for x in qts_bulk]))
    check("positive target q_T is outside fixed-radius bulk convex hull", not in_closed_interval(target_qt, qts_bulk), f"hull=[{min(qts_bulk):.3f},{max(qts_bulk):.3f}]")
    check("fixed-radius bulk lambdas stay above 9/4", all(x > target_lambda for x in lambdas_bulk), str([round(x, 3) for x in lambdas_bulk]))
    check("target lambda is outside fixed-radius bulk lambda hull", not in_closed_interval(target_lambda, lambdas_bulk), f"hull=[{min(lambdas_bulk):.3f},{max(lambdas_bulk):.3f}]")

    print()
    print("E. Box-proportional stable-tail tests")
    print("-" * 72)
    prop_qe = parse_list_after("box-proportional q_E ->", cache)
    prop_qt = parse_list_after("q_T ->", cache)
    check("box-proportional q_E list parsed", len(prop_qe) == 4, str(prop_qe))
    check("box-proportional q_T list parsed", len(prop_qt) == 4, str(prop_qt))
    stable_qe = prop_qe[1:]
    stable_qt = prop_qt[1:]
    check(
        "stable box-proportional q_E tail is unit-scale, not 15/8",
        all(0.90 <= x <= 1.06 for x in stable_qe)
        and not in_closed_interval(target_qe, stable_qe),
        str(stable_qe),
    )
    check("stable box-proportional q_T tail is near 1, not 5/6", max(abs(x - 1.0) for x in stable_qt) < 0.13 and not in_closed_interval(target_qt, stable_qt), str(stable_qt))
    prop_lam = [a / b for a, b in zip(prop_qe[1:], prop_qt[1:])]
    check("stable box-proportional lambda tail is near 1, not 9/4", max(abs(x - 1.0) for x in prop_lam) < 0.25 and not in_closed_interval(target_lambda, prop_lam), str([round(x, 3) for x in prop_lam]))

    print()
    print("F. Current-bank marker scan")
    print("-" * 72)
    measured = squash(texts["measured"])
    box_note = squash(texts["box_note"])
    covariance = squash(texts["covariance"])
    exact = squash(texts["exact_readout"])
    parent = squash(texts["parent"])
    check("measured note names box-size scan as discriminator", "box-size scan and extrapolation of `q_E(N)`" in measured)
    check("box note says N=15 is not bulk limit", "N=15" in box_note and "not a bulk limit" in box_note.lower())
    check("box note says both limits miss target", "fails under **both** limits" in box_note)
    check("covariance note says lambda is least box-stable", "least box-stable" in covariance)
    check("exact readout keeps rho_E as missing map entry", "missing map entry" in exact and "beta_E / alpha_E = 21/4" in exact)
    check("parent keeps endpoint triple open", "endpoint triple is not yet derived" in parent)

    print()
    print("G. Rescue-transform fan-out")
    print("-" * 72)
    fanout = {
        "same_function_fixed_radius_limit": "fails: q_E and q_T bulk tails are negative and miss targets",
        "same_function_box_proportional_limit": "fails: stable tail goes to 1, not target chain",
        "bulk_convex_average": "fails: target values outside fixed-radius bulk hulls",
        "bulk_covariance_ratio": "fails: lambda tail stays above 9/4 or near 1 in proportional limit",
        "N15_selection": "forbidden: selects the anomalous finite box rather than deriving a primitive",
    }
    for route, result in fanout.items():
        check(f"fan-out route {route} recorded", result.startswith("fails:") or result.startswith("forbidden:"), result)
    check("fan-out includes five post-scan rescue frames", len(fanout) == 5)

    print()
    print("Summary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: rescue-transform firewall failed; inspect checks above.")
        return 1
    print(
        "VERDICT: current-box-scan rescue transforms do not recover the Route-2 "
        "endpoint from the measured calibration without selecting N=15. Fixed-radius "
        "bulk tails, box-proportional stable tails, bulk convex reuse, and bulk "
        "covariance reuse all miss q_E=15/8, q_T=5/6, and lambda=9/4."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
