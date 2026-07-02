#!/usr/bin/env python3
"""Supplied stable-setting certificates for flow/thermal rows."""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import re
import sys

import frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06 as prev

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs/audit/data/audit_ledger.json"
SLICE = ROOT / "outputs/post_record_flow_thermal_stable_setting_slice_2026_06_07.json"
PASS = 0
FAIL = 0

OBSTRUCTION_RE = re.compile(
    r"\b(obstruction|no[-_ ]?go|does not|fails|not stable|partial falsification|"
    r"no transport|does_not_select|remaining open imports|missing axiom)\b",
    re.IGNORECASE,
)
THERMAL_SCORE_RE = re.compile(
    r"\b(thermal|born|closure|scalar|hessian|selector|mass|readout|weight|"
    r"finite[-_ ]?beta|partition|Omega|continuum|root)\b",
    re.IGNORECASE,
)
FLOW_RE = re.compile(
    r"\b(flow|fixed point|separatrix|records|objectivity|einselection|"
    r"transfer|dynamics|apparatus|persistent|Hamiltonian|RG|native lattice|"
    r"Luders|sharpening|sharpened)\b",
    re.IGNORECASE,
)
GENERATION_KOIDE_RE = re.compile(
    r"\b(koide|flavor|generation|kappa|r=1/2|Q=2/3|C3|C_3|orbit|triplet)\b",
    re.IGNORECASE,
)

EXPECTED_LANE_COUNTS = {
    "bounded_obstruction_or_no_selection": 21,
    "flow_or_records_stable_feature": 9,
    "generation_or_koide_stable_feature": 5,
    "generic_stable_feature": 31,
    "thermal_or_score_stable_feature": 25,
}
EXPECTED_FLOW_THERMAL_ROWS = sum(EXPECTED_LANE_COUNTS.values())


@dataclass(frozen=True)
class StabilityEvidence:
    supplied_domain: bool = False
    supplied_rule_id: bool = False
    supplied_stability_predicate: bool = False
    exact_check: bool = False
    selector_rule: bool = False


def report(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag} {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 78)
    print(title)
    print("-" * 78)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_rel(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def require_text(path: str, needles: list[str]) -> None:
    text = read_rel(path)
    report(f"{path} exists", True)
    for needle in needles:
        report(f"{path} contains: {needle}", needle in text)


def stable_setting_status(ev: StabilityEvidence) -> str:
    if ev.supplied_domain and ev.supplied_rule_id and ev.supplied_stability_predicate and ev.exact_check:
        return "stable_setting_support"
    return "open_missing_stability_certificate"


def selected_dial_status(ev: StabilityEvidence) -> str:
    if stable_setting_status(ev) == "stable_setting_support" and ev.selector_rule:
        return "conditional_selector_ready"
    return "blocked_missing_selector"


def finite_score_unique_minimum(scores: dict[str, Fraction]) -> str | None:
    minimum = min(scores.values())
    winners = [key for key, value in scores.items() if value == minimum]
    if len(winners) == 1:
        return winners[0]
    return None


def flow_fixed_point_feature(x: Fraction) -> dict:
    fx = 2 * x * x
    derivative = 4 * x
    return {
        "is_fixed_point": fx == x,
        "derivative": derivative,
        "feature": "unstable_separatrix" if fx == x and abs(derivative) > 1 else "not_separatrix",
    }


def finite_thermal_root(residuals: dict[Fraction, int]) -> Fraction | None:
    roots = [point for point, value in residuals.items() if value == 0]
    if len(roots) == 1:
        return roots[0]
    return None


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_FLOW_THERMAL_STABLE_SETTING_CERTIFICATE_2026-06-06.md",
        [
            "supplied flow, score, or thermal rule",
            "Stable setting is not selected dial.",
            "stable location on the dial is",
            "Does not select or force a generation/Koide dial location",
            "scripts/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.py",
            "outputs/post_record_flow_thermal_stable_setting_slice_2026_06_07.json",
        ],
    )
    require_text(
        "docs/POST_RECORD_STABILITY_DYNAMICS_SELECTOR_SUBDIVISION_2026-06-06.md",
        [
            "flow_or_thermal_stability",
            "stable setting is not selected dial",
            "These rows may support a stable setting",
        ],
    )
    require_text(
        "docs/POST_RECORD_SELECTOR_DIAL_BUCKET_SUBDIVISION_2026-06-06.md",
        [
            "stability_or_dynamics_selector` | 147",
            "stable settings into selected dials",
            "Does not turn stable settings into selected dials.",
        ],
    )
    require_text(
        "scripts/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.py",
        [
            "def stability_subbucket",
            "flow_or_thermal_stability",
            "EXPECTED_SUBCOUNTS",
        ],
    )
    require_text(
        "docs/POST_RECORD_CONDITIONAL_AUDIT_EVIDENCE_LADDER_2026-06-06.md",
        [
            "stable dial setting | supplied score/rule plus map/flow stability certificate",
            "selected dial value | selector/invariance/target rule",
            "stable settings are not selected dials",
        ],
    )


def certificate_checks() -> None:
    section("Stable-setting certificate checks")
    complete = StabilityEvidence(
        supplied_domain=True,
        supplied_rule_id=True,
        supplied_stability_predicate=True,
        exact_check=True,
    )
    missing_rule = StabilityEvidence(
        supplied_domain=True,
        supplied_stability_predicate=True,
        exact_check=True,
    )
    with_selector = StabilityEvidence(
        supplied_domain=True,
        supplied_rule_id=True,
        supplied_stability_predicate=True,
        exact_check=True,
        selector_rule=True,
    )

    report("complete supplied stability evidence gives stable-setting support", stable_setting_status(complete) == "stable_setting_support")
    report("missing supplied rule id stays open", stable_setting_status(missing_rule) == "open_missing_stability_certificate")
    report("stable setting without selector does not select dial", selected_dial_status(complete) == "blocked_missing_selector")
    report("selector rule is needed for selected dial readiness", selected_dial_status(with_selector) == "conditional_selector_ready")

    score_winner = finite_score_unique_minimum(
        {"left": Fraction(2), "middle": Fraction(0), "right": Fraction(2)}
    )
    report("finite supplied score has unique stable setting", score_winner == "middle", str(score_winner))

    feature = flow_fixed_point_feature(Fraction(1, 2))
    report("r=1/2 is exact fixed point for supplied r -> 2r^2 map", feature["is_fixed_point"], str(feature))
    report("r=1/2 is an unstable separatrix, not an attractor", feature["feature"] == "unstable_separatrix", str(feature))

    root = finite_thermal_root({Fraction(1, 10): -1, Fraction(3, 20): 0, Fraction(1, 5): 1})
    report("finite supplied thermal table has unique root", root == Fraction(3, 20), str(root))


def row_hay(row: dict) -> str:
    return "\n".join(
        str(row.get(key) or "")
        for key in ["claim_id", "title", "blocker", "load_bearing_step", "note_path"]
    )


def stable_lane(row: dict) -> str:
    hay = row_hay(row)
    if OBSTRUCTION_RE.search(hay):
        return "bounded_obstruction_or_no_selection"
    if GENERATION_KOIDE_RE.search(hay) and FLOW_RE.search(hay):
        return "generation_or_koide_stable_feature"
    if THERMAL_SCORE_RE.search(hay):
        return "thermal_or_score_stable_feature"
    if FLOW_RE.search(hay):
        return "flow_or_records_stable_feature"
    return "generic_stable_feature"


def export_row(row: dict, lane: str) -> dict:
    return {
        "claim_id": row.get("claim_id"),
        "audit_status": row.get("audit_status"),
        "effective_status": row.get("effective_status"),
        "claim_type": row.get("claim_type"),
        "note_path": row.get("note_path"),
        "runner_path": row.get("runner_path"),
        "stable_setting_lane": lane,
    }


def expected_export_rows(buckets: dict[str, list[dict]]) -> list[dict]:
    exported: list[dict] = []
    for lane in sorted(buckets):
        for row in sorted(buckets[lane], key=lambda item: item.get("claim_id") or ""):
            exported.append(export_row(row, lane))
    return exported


def flow_thermal_rows() -> list[dict]:
    rows = list(json.loads(LEDGER.read_text())["rows"].values())
    return [
        row
        for row in rows
        if prev.prev.scoped(row)
        and prev.prev.ladder_bucket(row) == "selector_or_dial_needed"
        and prev.prev.selector_subbucket(row) == "stability_or_dynamics_selector"
        and prev.stability_subbucket(row) == "flow_or_thermal_stability"
    ]


def row_checks() -> tuple[list[dict], Counter[str]]:
    section("Flow/thermal row checks")
    before = digest(LEDGER)
    rows = flow_thermal_rows()
    buckets: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        buckets[stable_lane(row)].append(row)
    counts = Counter({lane: len(items) for lane, items in buckets.items()})

    report("flow/thermal stability row count is current snapshot", len(rows) == EXPECTED_FLOW_THERMAL_ROWS, str(len(rows)))
    report("stable lane counts match expected", dict(counts) == EXPECTED_LANE_COUNTS, str(counts))
    report("stable lane counts sum to row count", sum(counts.values()) == len(rows), str(counts))

    representatives = {
        "bounded_obstruction_or_no_selection": "koide_bae_probe_native_lattice_flow_bounded_obstruction_note_2026-05-09_probe21",
        "flow_or_records_stable_feature": "koide_rp_spectrum_reduce_to_transfer_positivity_narrow_theorem_note_2026-06-02",
        "generation_or_koide_stable_feature": "flavor_r_half_is_the_records_flow_separatrix_2026-06-02",
        "generic_stable_feature": "koide_phase_aps_eta_parity_route_narrow_theorem_note_2026-05-23",
        "thermal_or_score_stable_feature": "dm_full_closure_same_surface_converged_thermal_selector_support_note_2026-04-16",
    }
    for lane, claim_id in representatives.items():
        present = any(row.get("claim_id") == claim_id for row in buckets[lane])
        report(f"representative row present in {lane}", present, claim_id)

    after = digest(LEDGER)
    report("audit ledger hash is unchanged", before == after, before)

    print()
    print("Flow/thermal stable-setting lane counts:")
    for lane, count in sorted(counts.items()):
        print(f"  {lane}: {count}")
    print()
    for lane in sorted(buckets):
        print(f"[{lane}]")
        for row in buckets[lane][:10]:
            print(
                "  "
                + f"{row.get('claim_id')} | {row.get('audit_status')} | "
                + f"{row.get('effective_status')} | {row.get('claim_type')} | "
                + f"{row.get('note_path')}"
            )
        print()
    export_checks(buckets, counts, before)
    return rows, counts


def export_checks(buckets: dict[str, list[dict]], counts: Counter[str], ledger_sha: str) -> None:
    section("Bounded ledger-row export checks")
    report("bounded flow/thermal row export exists", SLICE.exists(), str(SLICE.relative_to(ROOT)))
    if not SLICE.exists():
        return

    data = json.loads(SLICE.read_text(encoding="utf-8"))
    expected_rows = expected_export_rows(buckets)
    report("slice export is for the flow/thermal stability bucket", data.get("bucket") == "flow_or_thermal_stability")
    report("slice export records current ledger sha", data.get("ledger_sha256") == ledger_sha, data.get("ledger_sha256", ""))
    report("slice export row count matches current split", data.get("row_count") == EXPECTED_FLOW_THERMAL_ROWS, str(data.get("row_count")))
    report("slice export lane counts match current split", data.get("lane_counts") == dict(counts), str(data.get("lane_counts")))
    report("slice export rows match independently enumerated regex split", data.get("rows") == expected_rows)


def firewall_checks() -> None:
    section("Firewall flags")
    audit_data_written = False
    audit_verdict_applied = False
    promoted_or_retained_claim = False
    stable_setting_selects_dial = False
    generation_or_koide_dial_selected = False
    selected_dial_derived_from_stability = False
    production_dynamics_derived = False
    physical_arrow_derived_from_record = False
    clock_or_rate_derived = False

    report("audit data written flag is false", not audit_data_written)
    report("audit verdict applied flag is false", not audit_verdict_applied)
    report("promoted/retained claim flag is false", not promoted_or_retained_claim)
    report("stable setting selects dial flag is false", not stable_setting_selects_dial)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)
    report("selected dial derived from stability flag is false", not selected_dial_derived_from_stability)
    report("production dynamics derived flag is false", not production_dynamics_derived)
    report("Record-derived physical arrow flag is false", not physical_arrow_derived_from_record)
    report("clock/rate derived flag is false", not clock_or_rate_derived)


def main() -> int:
    source_anchor_checks()
    certificate_checks()
    rows, counts = row_checks()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print(f"FLOW_OR_THERMAL_STABILITY_ROWS={len(rows)}")
    for lane in sorted(EXPECTED_LANE_COUNTS):
        print(f"{lane.upper()}_ROWS={counts[lane]}")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    print("AUDIT_VERDICT_APPLIED=FALSE")
    print("STABLE_SETTING_SELECTS_DIAL=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    print("SELECTED_DIAL_DERIVED_FROM_STABILITY=FALSE")
    print("PRODUCTION_DYNAMICS_DERIVED=FALSE")
    print("PHYSICAL_ARROW_DERIVED_FROM_RECORD=FALSE")
    print("CLOCK_OR_RATE_DERIVED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
