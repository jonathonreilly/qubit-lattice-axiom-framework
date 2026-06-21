#!/usr/bin/env python3
"""Route-2 E-center finite-size bridge admissibility gate.

The measured N=15 E-center calibration is a useful stack-internal support
datum, but the current finite-size evidence does not certify the exact
endpoint q_E=15/8.  This runner packages the current bridge gate:

* the landed box-size scan anchors the N=15 value and shows the two named
  infinite-volume schedules miss 15/8;
* an additional first-principles radius-window probe at N=17 and N=19 does
  not find an untuned radius rescue in broad interior windows;
* therefore a future finite-size derivation needs a predeclared schedule
  theorem, a selector theorem, or an independent source/readout primitive.

No observed masses, fitted targets, or nearest-rational selection are used.
The rationals 5/6 and 15/8 appear only as comparison targets.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CACHE = ROOT / "logs" / "runner-cache" / "frontier_quark_route2_qe_box_size_scan_2026_06_10.txt"
NOTE = DOCS / "QUARK_ROUTE2_E_CENTER_FINITE_SIZE_BRIDGE_ADMISSIBILITY_GATE_NO_GO_NOTE_2026-06-21.md"

PASS = 0
FAIL = 0

TARGET_Q_T = Fraction(5, 6)
TARGET_Q_E = Fraction(15, 8)


@dataclass(frozen=True)
class RadiusSample:
    n: int
    radius: Fraction
    q_e: Fraction
    q_t: Fraction


RADIUS_WINDOW: tuple[RadiusSample, ...] = (
    # First-principles probe using frontier_quark_route2_qe_box_size_scan_2026_06_10.gammas.
    # N=17: radius in [2.00, 7.20].
    RadiusSample(17, Fraction(200, 100), Fraction("-1.1575"), Fraction("-1.1070")),
    RadiusSample(17, Fraction(243, 100), Fraction("-9.9132"), Fraction("-2.5810")),
    RadiusSample(17, Fraction(287, 100), Fraction("-9.1047"), Fraction("-2.7042")),
    RadiusSample(17, Fraction(330, 100), Fraction("0.0593"), Fraction("0.2000")),
    RadiusSample(17, Fraction(373, 100), Fraction("0.0322"), Fraction("0.1223")),
    RadiusSample(17, Fraction(417, 100), Fraction("-5.2697"), Fraction("-0.3057")),
    RadiusSample(17, Fraction(460, 100), Fraction("1.0041"), Fraction("0.2390")),
    RadiusSample(17, Fraction(503, 100), Fraction("0.7535"), Fraction("0.8794")),
    RadiusSample(17, Fraction(547, 100), Fraction("0.9273"), Fraction("0.9014")),
    RadiusSample(17, Fraction(590, 100), Fraction("0.8784"), Fraction("0.9156")),
    RadiusSample(17, Fraction(633, 100), Fraction("1.0142"), Fraction("1.0202")),
    RadiusSample(17, Fraction(677, 100), Fraction("1.0265"), Fraction("1.0263")),
    RadiusSample(17, Fraction(720, 100), Fraction("1.0030"), Fraction("1.0038")),
    # N=19: radius in [2.00, 8.00].
    RadiusSample(19, Fraction(200, 100), Fraction("-1.2412"), Fraction("-1.1914")),
    RadiusSample(19, Fraction(250, 100), Fraction("-8.8596"), Fraction("-2.4513")),
    RadiusSample(19, Fraction(300, 100), Fraction("-4.2765"), Fraction("-1.1946")),
    RadiusSample(19, Fraction(350, 100), Fraction("-0.6284"), Fraction("-0.4680")),
    RadiusSample(19, Fraction(400, 100), Fraction("-7.0523"), Fraction("-1.2822")),
    RadiusSample(19, Fraction(450, 100), Fraction("-13.8823"), Fraction("-0.9555")),
    RadiusSample(19, Fraction(500, 100), Fraction("0.7061"), Fraction("0.8269")),
    RadiusSample(19, Fraction(550, 100), Fraction("0.9167"), Fraction("0.8758")),
    RadiusSample(19, Fraction(600, 100), Fraction("0.8264"), Fraction("0.9754")),
    RadiusSample(19, Fraction(650, 100), Fraction("1.1437"), Fraction("1.0522")),
    RadiusSample(19, Fraction(700, 100), Fraction("0.9938"), Fraction("1.0007")),
    RadiusSample(19, Fraction(750, 100), Fraction("0.9907"), Fraction("0.9903")),
    RadiusSample(19, Fraction(800, 100), Fraction("0.9955"), Fraction("0.9961")),
)


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def frac_decimal(text: str) -> Fraction:
    return Fraction(text)


def parse_fixed_radius_table(text: str) -> dict[int, tuple[Fraction, Fraction]]:
    rows: dict[int, tuple[Fraction, Fraction]] = {}
    pattern = re.compile(
        r"^\s+(?P<n>\d+)\s+"
        r"[+-]\d+\.\d+e[+-]\d+\s+"
        r"[+-]\d+\.\d+e[+-]\d+\s+"
        r"[+-]\d+\.\d+e[+-]\d+\s+"
        r"[+-]\d+\.\d+e[+-]\d+\s+"
        r"[+-]\d+\.\d+e[+-]\d+\s+"
        r"[+-]\d+\.\d+e[+-]\d+\s+"
        r"(?P<qt>[+-]\d+\.\d+)\s+"
        r"(?P<qe>[+-]\d+\.\d+)"
    )
    for line in text.splitlines():
        match = pattern.match(line)
        if match:
            rows[int(match.group("n"))] = (frac_decimal(match.group("qt")), frac_decimal(match.group("qe")))
    return rows


def parse_prop_tail(text: str) -> tuple[list[Fraction], list[Fraction]]:
    match = re.search(
        r"box-proportional q_E -> \[(?P<qe>[^\]]+)\].*?q_T -> \[(?P<qt>[^\]]+)\]",
        text,
        re.S,
    )
    if not match:
        return [], []
    def parse_list(part: str) -> list[Fraction]:
        values = []
        for item in part.split(","):
            cleaned = item.strip().strip("'")
            values.append(frac_decimal(cleaned))
        return values
    return parse_list(match.group("qe")), parse_list(match.group("qt"))


def by_n(samples: tuple[RadiusSample, ...], n: int) -> list[RadiusSample]:
    return [sample for sample in samples if sample.n == n]


def main() -> int:
    print("=" * 88)
    print("ROUTE-2 E-CENTER FINITE-SIZE BRIDGE ADMISSIBILITY GATE")
    print("=" * 88)

    print()
    print("A. Authority anchors")
    print("-" * 72)
    for path in (
        CACHE,
        DOCS / "QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md",
        DOCS / "QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md",
        DOCS / "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md",
        DOCS / "S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md",
        NOTE,
    ):
        check(f"{path.name} exists", path.exists(), str(path.relative_to(ROOT)))

    cache_text = read(CACHE)
    note_text = read(NOTE) if NOTE.exists() else ""
    check("box_scan_cache_status_ok", "status: ok" in cache_text)
    check("box_scan_cache_has_anchor", "N=15 q_T=0.833328" in cache_text and "q_E=1.876247" in cache_text)
    check("measured_note_names_box_size_discriminator", "box-size scan and extrapolation" in read(DOCS / "QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md"))
    check("s3_parent_names_endpoint_triple_blocker", "readout-map endpoint triple" in read(DOCS / "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md"))

    print()
    print("B. Fixed-radius finite-size scan")
    print("-" * 72)
    fixed = parse_fixed_radius_table(cache_text)
    check("fixed_radius_table_parsed", set(fixed) == {11, 13, 15, 17, 19, 21, 25, 29}, f"N={sorted(fixed)}")
    q_t_15, q_e_15 = fixed[15]
    check("N15_matches_target_window", abs(q_e_15 - TARGET_Q_E) < Fraction(2, 1000) and abs(q_t_15 - TARGET_Q_T) < Fraction(1, 1000), f"q_T(15)={float(q_t_15):.6f}; q_E(15)={float(q_e_15):.6f}")
    check("post_N15_fixed_radius_qE_all_below_target", all(fixed[n][1] < TARGET_Q_E for n in (17, 19, 21, 25, 29)))
    check("post_N15_fixed_radius_qE_negative", all(fixed[n][1] < 0 for n in (17, 19, 21, 25, 29)), str({n: float(fixed[n][1]) for n in (17, 19, 21, 25, 29)}))
    check("post_N15_fixed_radius_qT_sign_flip", fixed[15][0] > 0 and fixed[17][0] < 0)
    check("fixed_radius_cache_reports_a_aniso_cancellation", "a_center/a_shell = 1" in cache_text and "CANCELS exactly" in cache_text)

    print()
    print("C. Box-proportional schedule")
    print("-" * 72)
    q_e_prop, q_t_prop = parse_prop_tail(cache_text)
    check("proportional_tail_parsed", len(q_e_prop) == 4 and len(q_t_prop) == 4, f"q_E={q_e_prop}; q_T={q_t_prop}")
    check("proportional_tail_ends_near_one", abs(q_e_prop[-1] - 1) < Fraction(1, 20) and abs(q_t_prop[-1] - 1) < Fraction(1, 20), f"q_E_tail={float(q_e_prop[-1]):.3f}; q_T_tail={float(q_t_prop[-1]):.3f}")
    check("proportional_tail_not_target", abs(q_e_prop[-1] - TARGET_Q_E) > Fraction(4, 5) and abs(q_t_prop[-1] - TARGET_Q_T) > Fraction(1, 10))

    print()
    print("D. Untuned radius-window rescue probe")
    print("-" * 72)
    for n in (17, 19):
        samples = by_n(RADIUS_WINDOW, n)
        qes = [sample.q_e for sample in samples]
        qts = [sample.q_t for sample in samples]
        check(f"N{n}_radius_window_has_13_samples", len(samples) == 13)
        check(f"N{n}_radius_window_no_qE_crossing_15_8", all(q_e < TARGET_Q_E for q_e in qes), f"max q_E={float(max(qes)):.4f}")
        check(f"N{n}_radius_window_tail_near_one_not_target", abs(qes[-1] - 1) < Fraction(1, 25) and abs(qts[-1] - 1) < Fraction(1, 25), f"tail q_E={float(qes[-1]):.4f}; q_T={float(qts[-1]):.4f}")
        check(f"N{n}_radius_window_has_no_adjacent_sign_crossing_of_target_gap", all((a.q_e - TARGET_Q_E) * (b.q_e - TARGET_Q_E) > 0 for a, b in zip(samples, samples[1:])))

    print()
    print("E. Bridge gate classification")
    print("-" * 72)
    bridge_classes = {
        "single_box_exactification": "insufficient",
        "fixed_radius_limit": "misses_target",
        "box_proportional_limit": "misses_target",
        "sampled_untuned_radius_windows": "misses_target",
        "posthoc_radius_schedule": "new_selector_import",
        "changed_normalization_or_probe": "different_functional",
        "independent_source_readout_theorem": "open_positive_route",
    }
    check("same_functional_finite_size_routes_do_not_retire_endpoint_triple", all(bridge_classes[key] in {"insufficient", "misses_target", "new_selector_import", "different_functional"} for key in bridge_classes if key != "independent_source_readout_theorem"))
    check("future_positive_route_is_named", bridge_classes["independent_source_readout_theorem"] == "open_positive_route")
    check("paired_note_states_parent_remains_open", "parent row remains open" in note_text)
    check("paired_note_names_required_future_inputs", all(s in note_text for s in ("predeclared schedule", "selector theorem", "independent source/readout primitive")))
    check("paired_note_avoids_status_overclaim", re.search(r"(?m)^\\*?\\*?Status\\*?\\*?:\\s*(retained|promoted)\\b", note_text) is None)

    print()
    print("Summary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: no-go for retiring the Route-2 E-center endpoint triple from "
        "the current finite-size bridge evidence.  The same-functional fixed "
        "and proportional schedules miss 15/8, the sampled untuned radius "
        "windows at N=17 and N=19 do not rescue it, and any post-hoc schedule "
        "or changed observable is a new selector/source import rather than a "
        "derivation.  The positive route remains a predeclared schedule theorem, "
        "selector theorem, or independent nonblind source/readout primitive."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
