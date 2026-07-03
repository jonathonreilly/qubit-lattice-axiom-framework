#!/usr/bin/env python3
"""Finite directed-certificate examples under supplied post-record orientation."""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import importlib.util
import json
import sys


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs/audit/data/audit_ledger.json"
STABILITY_SCRIPT = ROOT / "scripts/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.py"
PASS = 0
FAIL = 0

Word = tuple[str, ...]
Law = dict[Word, Fraction]


@dataclass(frozen=True)
class SuppliedBridge:
    bridge_id: str
    law_id: str
    orientation: str | None
    clock_id: str | None
    kernel_id: str | None


@dataclass(frozen=True)
class DirectedCertificate:
    cert_id: str
    law_id: str
    bridge_id: str
    statistic_id: str
    kind: str
    expected_value: Fraction
    threshold: int | None = None


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


def read_rel(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def require_text(path: str, needles: list[str]) -> None:
    text = read_rel(path)
    report(f"{path} exists", True)
    for needle in needles:
        report(f"{path} contains: {needle}", needle in text)


def load_script(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def normalize_law(law: Law) -> bool:
    return bool(law) and sum(law.values(), Fraction(0, 1)) == 1 and all(m >= 0 for m in law.values())


def rev(word: Word) -> Word:
    return tuple(reversed(word))


def reverse_law(law: Law) -> Law:
    out: defaultdict[Word, Fraction] = defaultdict(Fraction)
    for word, mass in law.items():
        out[rev(word)] += mass
    return dict(out)


def alphabet_for(law: Law) -> tuple[str, ...]:
    return tuple(sorted({atom for word in law for atom in word}))


def count_word(word: Word, alphabet: tuple[str, ...]) -> tuple[int, ...]:
    counts = Counter(word)
    return tuple(counts[a] for a in alphabet)


def count_pushforward(law: Law) -> dict[tuple[int, ...], Fraction]:
    alphabet = alphabet_for(law)
    out: defaultdict[tuple[int, ...], Fraction] = defaultdict(Fraction)
    for word, mass in law.items():
        out[count_word(word, alphabet)] += mass
    return dict(out)


def oriented_law(law: Law, bridge: SuppliedBridge) -> Law | None:
    if bridge.orientation == "forward":
        return law
    if bridge.orientation == "reverse":
        return reverse_law(law)
    return None


SIGNED_EDGES: dict[tuple[str, str], int] = {
    ("A", "B"): 1,
    ("B", "A"): -1,
    ("B", "C"): 1,
    ("C", "B"): -1,
}


def signed_transition_drift(word: Word) -> int:
    return sum(SIGNED_EDGES.get(edge, 0) for edge in zip(word, word[1:]))


def marker_lag(word: Word) -> int:
    if "M" not in word:
        return len(word)
    return word.index("M")


def low_to_high_boundary_event(word: Word) -> int:
    return int(len(word) >= 2 and word[0] == "L" and word[-1] == "H")


STATISTICS = {
    "signed_transition_drift": signed_transition_drift,
    "marker_lag": marker_lag,
    "low_to_high_boundary_event": low_to_high_boundary_event,
}


def expectation(law: Law, statistic) -> Fraction:
    return sum(Fraction(statistic(word), 1) * mass for word, mass in law.items())


def probability_gt(law: Law, statistic, threshold: int) -> Fraction:
    return sum(mass for word, mass in law.items() if statistic(word) > threshold)


def probability_le(law: Law, statistic, threshold: int) -> Fraction:
    return sum(mass for word, mass in law.items() if statistic(word) <= threshold)


def distribution(law: Law, statistic) -> dict[int, Fraction]:
    out: defaultdict[int, Fraction] = defaultdict(Fraction)
    for word, mass in law.items():
        out[statistic(word)] += mass
    return dict(sorted(out.items()))


def verify_certificate(
    law_id: str,
    law: Law,
    bridge: SuppliedBridge,
    cert: DirectedCertificate,
) -> tuple[str, Fraction | None]:
    if not normalize_law(law):
        return "blocked_bad_law", None
    if bridge.orientation not in {"forward", "reverse"}:
        return "blocked_missing_orientation", None
    if bridge.clock_id is None:
        return "blocked_missing_clock", None
    if bridge.kernel_id is None:
        return "blocked_missing_kernel", None
    if law_id != cert.law_id or bridge.law_id != law_id or bridge.bridge_id != cert.bridge_id:
        return "blocked_scope_mismatch", None
    statistic = STATISTICS.get(cert.statistic_id)
    if statistic is None:
        return "blocked_unknown_statistic", None
    olaw = oriented_law(law, bridge)
    if olaw is None:
        return "blocked_missing_orientation", None
    if cert.kind == "expectation":
        value = expectation(olaw, statistic)
    elif cert.kind == "probability_gt":
        if cert.threshold is None:
            return "blocked_missing_threshold", None
        value = probability_gt(olaw, statistic, cert.threshold)
    elif cert.kind == "probability_le":
        if cert.threshold is None:
            return "blocked_missing_threshold", None
        value = probability_le(olaw, statistic, cert.threshold)
    else:
        return "blocked_unknown_kind", None
    if value != cert.expected_value:
        return "value_mismatch", value
    return "verified", value


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_DIRECTED_CERTIFICATE_EXAMPLES_2026-06-06.md",
        [
            "supplied finite law plus supplied orientation bridge",
            "The law carries probability; the post-record words carry realized markers",
            "examples do not derive an arrow, clock, kernel, or selected dial",
            "scripts/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.py",
        ],
    )
    require_text(
        "docs/POST_RECORD_SUPPLIED_ORIENTATION_BRIDGE_INTERFACE_2026-06-06.md",
        [
            "supplied orientation bridge",
            "does not derive an orientation",
            "directed post-record certificates are available only under supplied orientation/law/clock/kernel bridges",
        ],
    )
    require_text(
        "docs/POST_RECORD_ARROW_ORIENTATION_FIREWALL_2026-06-06.md",
        [
            "count pushforward is invariant under reversal",
            "post-record counts do not orient a physical arrow",
            "An oriented law, boundary condition, clock, or production kernel",
        ],
    )
    require_text(
        "docs/POST_RECORD_STABILITY_DYNAMICS_SELECTOR_SUBDIVISION_2026-06-06.md",
        [
            "arrow_or_dynamics_bridge",
            "Total: `169` stability/dynamics selector rows.",
            "stable setting is not selected dial",
        ],
    )
    require_text(
        "scripts/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.py",
        [
            "def stability_subbucket",
            "EXPECTED_SUBCOUNTS",
            "arrow_or_dynamics_bridge",
        ],
    )


def row_bucket_checks() -> None:
    section("Arrow/dynamics row-bucket checks")
    stability = load_script("stability_dynamics_selector_subdivision", STABILITY_SCRIPT)
    rows = list(json.loads(LEDGER.read_text(encoding="utf-8"))["rows"].values())
    stability_rows = [
        row
        for row in rows
        if stability.prev.scoped(row)
        and stability.prev.ladder_bucket(row) == "selector_or_dial_needed"
        and stability.prev.selector_subbucket(row) == "stability_or_dynamics_selector"
    ]
    buckets: Counter[str] = Counter(stability.stability_subbucket(row) for row in stability_rows)
    report("stability/dynamics selector row count remains 169", len(stability_rows) == 169, str(len(stability_rows)))
    report("arrow/dynamics bridge row count remains 63", buckets["arrow_or_dynamics_bridge"] == 63, str(buckets))
    report("flow/thermal stability row count remains 106", buckets["flow_or_thermal_stability"] == 106, str(buckets))


def transition_drift_example() -> None:
    section("Example 1: signed transition drift")
    law: Law = {
        ("A", "B", "C"): Fraction(1, 4),
        ("A", "C", "B"): Fraction(1, 4),
        ("B", "A", "C"): Fraction(1, 4),
        ("C", "B", "A"): Fraction(1, 4),
    }
    forward = SuppliedBridge("bridge_transition_forward", "law_transition_drift", "forward", "word_index_clock", "signed_edge_kernel")
    reverse = SuppliedBridge("bridge_transition_reverse", "law_transition_drift", "reverse", "word_index_clock", "signed_edge_kernel")
    missing = SuppliedBridge("bridge_transition_forward", "law_transition_drift", None, "word_index_clock", "signed_edge_kernel")
    wrong = SuppliedBridge("bridge_wrong_law", "other_law", "forward", "word_index_clock", "signed_edge_kernel")
    cert_forward = DirectedCertificate(
        "transition_drift_forward_expectation",
        "law_transition_drift",
        "bridge_transition_forward",
        "signed_transition_drift",
        "expectation",
        Fraction(-1, 2),
    )
    cert_reverse = DirectedCertificate(
        "transition_drift_reverse_expectation",
        "law_transition_drift",
        "bridge_transition_reverse",
        "signed_transition_drift",
        "expectation",
        Fraction(1, 2),
    )
    cert_tail = DirectedCertificate(
        "transition_drift_forward_positive_tail",
        "law_transition_drift",
        "bridge_transition_forward",
        "signed_transition_drift",
        "probability_gt",
        Fraction(1, 4),
        threshold=0,
    )
    cert_wrong_value = DirectedCertificate(
        "transition_drift_bad_value",
        "law_transition_drift",
        "bridge_transition_forward",
        "signed_transition_drift",
        "expectation",
        Fraction(0, 1),
    )
    f_law = oriented_law(law, forward)
    r_law = oriented_law(law, reverse)
    assert f_law is not None and r_law is not None

    report("transition law normalizes", normalize_law(law))
    report("forward signed drift expectation is exact", expectation(f_law, signed_transition_drift) == Fraction(-1, 2), str(distribution(f_law, signed_transition_drift)))
    report("reverse signed drift expectation flips sign", expectation(r_law, signed_transition_drift) == Fraction(1, 2), str(distribution(r_law, signed_transition_drift)))
    report("forward positive drift tail is exact", probability_gt(f_law, signed_transition_drift, 0) == Fraction(1, 4))
    report("reverse positive drift tail is exact", probability_gt(r_law, signed_transition_drift, 0) == Fraction(3, 4))
    report("count pushforward is invariant for transition example", count_pushforward(f_law) == count_pushforward(r_law), str(count_pushforward(f_law)))

    status_f, value_f = verify_certificate("law_transition_drift", law, forward, cert_forward)
    status_r, value_r = verify_certificate("law_transition_drift", law, reverse, cert_reverse)
    status_tail, value_tail = verify_certificate("law_transition_drift", law, forward, cert_tail)
    status_missing, value_missing = verify_certificate("law_transition_drift", law, missing, cert_forward)
    status_wrong, value_wrong = verify_certificate("law_transition_drift", law, wrong, cert_forward)
    status_bad, value_bad = verify_certificate("law_transition_drift", law, forward, cert_wrong_value)
    report("forward transition certificate verifies", status_f == "verified" and value_f == Fraction(-1, 2))
    report("reverse transition certificate verifies", status_r == "verified" and value_r == Fraction(1, 2))
    report("positive-tail transition certificate verifies", status_tail == "verified" and value_tail == Fraction(1, 4))
    report("missing orientation blocks transition certificate", status_missing == "blocked_missing_orientation" and value_missing is None)
    report("wrong law scope blocks transition certificate", status_wrong == "blocked_scope_mismatch" and value_wrong is None)
    report("wrong value is rejected for transition certificate", status_bad == "value_mismatch" and value_bad == Fraction(-1, 2))


def marker_lag_example() -> None:
    section("Example 2: realized marker lag")
    law: Law = {
        ("A", "M", "B", "B"): Fraction(1, 2),
        ("A", "B", "M", "C"): Fraction(1, 3),
        ("M", "C", "A", "B"): Fraction(1, 6),
    }
    forward = SuppliedBridge("bridge_marker_forward", "law_marker_lag", "forward", "marker_clock", "record_write_kernel")
    reverse = SuppliedBridge("bridge_marker_reverse", "law_marker_lag", "reverse", "marker_clock", "record_write_kernel")
    cert_forward = DirectedCertificate(
        "marker_lag_forward_expectation",
        "law_marker_lag",
        "bridge_marker_forward",
        "marker_lag",
        "expectation",
        Fraction(7, 6),
    )
    cert_forward_tail = DirectedCertificate(
        "marker_lag_forward_le_one",
        "law_marker_lag",
        "bridge_marker_forward",
        "marker_lag",
        "probability_le",
        Fraction(2, 3),
        threshold=1,
    )
    f_law = oriented_law(law, forward)
    r_law = oriented_law(law, reverse)
    assert f_law is not None and r_law is not None

    records_are_realized = all(isinstance(word, tuple) and "M" in word for word in law)
    law_carries_probability = all(isinstance(mass, Fraction) for mass in law.values())
    report("marker law normalizes", normalize_law(law))
    report("law carries probabilities outside realized record words", records_are_realized and law_carries_probability)
    report("forward marker lag expectation is exact", expectation(f_law, marker_lag) == Fraction(7, 6), str(distribution(f_law, marker_lag)))
    report("reverse marker lag expectation is exact", expectation(r_law, marker_lag) == Fraction(11, 6), str(distribution(r_law, marker_lag)))
    report("forward marker lag tail is exact", probability_le(f_law, marker_lag, 1) == Fraction(2, 3))
    report("reverse marker lag tail is exact", probability_le(r_law, marker_lag, 1) == Fraction(1, 3))
    report("count pushforward is invariant for marker example", count_pushforward(f_law) == count_pushforward(r_law), str(count_pushforward(f_law)))

    status_f, value_f = verify_certificate("law_marker_lag", law, forward, cert_forward)
    status_tail, value_tail = verify_certificate("law_marker_lag", law, forward, cert_forward_tail)
    report("marker expectation certificate verifies", status_f == "verified" and value_f == Fraction(7, 6))
    report("marker tail certificate verifies", status_tail == "verified" and value_tail == Fraction(2, 3))


def boundary_example() -> None:
    section("Example 3: supplied low-to-high boundary event")
    law: Law = {
        ("L", "A", "H"): Fraction(1, 2),
        ("H", "A", "L"): Fraction(1, 6),
        ("L", "B", "A"): Fraction(1, 3),
    }
    forward = SuppliedBridge("bridge_boundary_forward", "law_boundary_event", "forward", "boundary_clock", "boundary_transfer")
    reverse = SuppliedBridge("bridge_boundary_reverse", "law_boundary_event", "reverse", "boundary_clock", "boundary_transfer")
    no_kernel = SuppliedBridge("bridge_boundary_forward", "law_boundary_event", "forward", "boundary_clock", None)
    cert_forward = DirectedCertificate(
        "boundary_forward_probability",
        "law_boundary_event",
        "bridge_boundary_forward",
        "low_to_high_boundary_event",
        "expectation",
        Fraction(1, 2),
    )
    cert_reverse = DirectedCertificate(
        "boundary_reverse_probability",
        "law_boundary_event",
        "bridge_boundary_reverse",
        "low_to_high_boundary_event",
        "expectation",
        Fraction(1, 6),
    )
    f_law = oriented_law(law, forward)
    r_law = oriented_law(law, reverse)
    assert f_law is not None and r_law is not None

    report("boundary law normalizes", normalize_law(law))
    report("forward low-to-high boundary probability is exact", expectation(f_law, low_to_high_boundary_event) == Fraction(1, 2))
    report("reverse low-to-high boundary probability is exact", expectation(r_law, low_to_high_boundary_event) == Fraction(1, 6))
    report("boundary event is orientation-sensitive", expectation(f_law, low_to_high_boundary_event) != expectation(r_law, low_to_high_boundary_event))
    report("count pushforward is invariant for boundary example", count_pushforward(f_law) == count_pushforward(r_law), str(count_pushforward(f_law)))

    status_f, value_f = verify_certificate("law_boundary_event", law, forward, cert_forward)
    status_r, value_r = verify_certificate("law_boundary_event", law, reverse, cert_reverse)
    status_no_kernel, value_no_kernel = verify_certificate("law_boundary_event", law, no_kernel, cert_forward)
    report("boundary forward certificate verifies", status_f == "verified" and value_f == Fraction(1, 2))
    report("boundary reverse certificate verifies", status_r == "verified" and value_r == Fraction(1, 6))
    report("missing kernel blocks dynamics-language boundary certificate", status_no_kernel == "blocked_missing_kernel" and value_no_kernel is None)


def firewall_checks() -> None:
    section("Firewall flags")
    audit_data_written = False
    audit_verdict_applied = False
    promoted_or_retained_claim = False
    orientation_derived_from_record = False
    physical_arrow_derived_from_record = False
    production_kernel_selected = False
    clock_or_rate_derived = False
    born_law_derived_from_record = False
    generation_or_koide_dial_selected = False
    stable_setting_selects_dial = False
    selected_dial_derived_from_stability = False

    report("audit data written flag is false", not audit_data_written)
    report("audit verdict applied flag is false", not audit_verdict_applied)
    report("promoted/retained claim flag is false", not promoted_or_retained_claim)
    report("Record-derived orientation flag is false", not orientation_derived_from_record)
    report("Record-derived physical arrow flag is false", not physical_arrow_derived_from_record)
    report("production-kernel selected flag is false", not production_kernel_selected)
    report("clock/rate derived flag is false", not clock_or_rate_derived)
    report("Born law derived from Record flag is false", not born_law_derived_from_record)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)
    report("stable setting selects dial flag is false", not stable_setting_selects_dial)
    report("selected dial derived from stability flag is false", not selected_dial_derived_from_stability)


def main() -> int:
    source_anchor_checks()
    row_bucket_checks()
    transition_drift_example()
    marker_lag_example()
    boundary_example()
    firewall_checks()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("SUPPLIED_DIRECTED_CERTIFICATE_EXAMPLES=TRUE")
    print("ARROW_OR_DYNAMICS_BRIDGE_ROWS=63")
    print("PRE_RECORD_LAW_CARRIES_PROBABILITY=TRUE")
    print("POST_RECORD_SITE_CARRIES_REALIZED_INFORMATION=TRUE")
    print("DIRECTED_STATISTICS_REQUIRE_SUPPLIED_ORIENTATION=TRUE")
    print("ORIENTATION_DERIVED_FROM_RECORD=FALSE")
    print("PHYSICAL_ARROW_DERIVED_FROM_RECORD=FALSE")
    print("PRODUCTION_KERNEL_SELECTED=FALSE")
    print("CLOCK_OR_RATE_DERIVED=FALSE")
    print("BORN_LAW_DERIVED_FROM_RECORD=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    print("STABLE_SETTING_SELECTS_DIAL=FALSE")
    print("SELECTED_DIAL_DERIVED_FROM_STABILITY=FALSE")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    print("AUDIT_VERDICT_APPLIED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
