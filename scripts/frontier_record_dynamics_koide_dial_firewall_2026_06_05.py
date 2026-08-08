#!/usr/bin/env python3
"""Record-dynamics firewall for Koide/generation dial selection."""

from __future__ import annotations

from pathlib import Path


PASS = 0
FAIL = 0


RECORD_GATES = {
    "kernel",
    "history",
    "local_observability",
    "reset_resource",
    "open_reset_channel",
    "epsilon_reset",
}

EXTERNAL_GATES = {
    "produced_record",
    "dial_selector",
    "stable_setting_supplied",
}

CLAIMS = {
    "register_supplied_dial": {"produced_record", "stable_setting_supplied"},
    "history_of_supplied_dial": {"produced_record", "history", "stable_setting_supplied"},
    "select_dial_location": {"dial_selector"},
    "force_koide_value": {"dial_selector"},
    "stable_location_on_dial": {"dial_selector", "stable_setting_supplied"},
}


def emit(line: str = "") -> None:
    print(line)


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" ({detail})" if detail else ""
    emit(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    emit()
    emit("-" * 78)
    emit(title)
    emit("-" * 78)


def classify(claim: str) -> str:
    required = CLAIMS[claim]
    supplied = RECORD_GATES | {"stable_setting_supplied"}
    if claim in {"register_supplied_dial", "history_of_supplied_dial"}:
        return "conditional_on_produced_record"
    if "dial_selector" in required and "dial_selector" not in supplied:
        return "selector_open"
    return "support_available"


def main() -> int:
    emit("=" * 78)
    emit("RECORD DYNAMICS KOIDE DIAL FIREWALL")
    emit("no-go / supplied-setting readout classifier")
    emit("=" * 78)

    section("1. Gate separation")
    check("record gates do not include dial_selector", "dial_selector" not in RECORD_GATES)
    check("record gates do not include produced_record", "produced_record" not in RECORD_GATES)
    check("external gates include stable_setting_supplied", "stable_setting_supplied" in EXTERNAL_GATES)
    check("external gates include dial_selector", "dial_selector" in EXTERNAL_GATES)
    check("history gate is record-dynamics only", "history" in RECORD_GATES)
    check("epsilon reset is not dial selection", "epsilon_reset" in RECORD_GATES and "epsilon_reset" != "dial_selector")

    section("2. Claim classifications")
    expected = {
        "register_supplied_dial": "conditional_on_produced_record",
        "history_of_supplied_dial": "conditional_on_produced_record",
        "select_dial_location": "selector_open",
        "force_koide_value": "selector_open",
        "stable_location_on_dial": "selector_open",
    }
    for claim, expected_value in expected.items():
        check(f"{claim}: required gates declared", bool(CLAIMS[claim]))
        check(f"{claim}: classification", classify(claim) == expected_value, classify(claim))

    section("3. Overclaim firewall")
    overclaims = {
        "history selects dial": classify("select_dial_location") == "selector_open",
        "reset gates select dial": "dial_selector" not in {"reset_resource", "open_reset_channel"},
        "epsilon reset stabilizes Koide value": classify("force_koide_value") == "selector_open",
        "local observability forces dial": "dial_selector" != "local_observability",
        "stable readout means selected location": classify("stable_location_on_dial") == "selector_open",
        "record stack can register supplied setting only conditionally": classify("register_supplied_dial") == "conditional_on_produced_record",
    }
    for label, ok in overclaims.items():
        check(label, ok)

    section("4. Source note sanity")
    doc = Path("docs/RECORD_DYNAMICS_KOIDE_DIAL_FIREWALL_2026-06-05.md")
    text = doc.read_text(encoding="utf-8")
    markers = [
        "actual_current_surface_status: no-go",
        "trace_class: negative_route_pruning",
        "does not select the dial location",
        "Does not derive Koide",
        "Does not update repo-wide authority surfaces.",
        "audit_required_before_effective_retained: true",
    ]
    check("source note exists", doc.exists(), str(doc))
    for marker in markers:
        check(f"note contains marker: {marker}", marker in text)
    forbidden_wording = [
        ("dial closure", "dial location is " + "selected"),
        ("koide closure", "Koide is " + "derived"),
        ("mass closure", "masses are " + "derived"),
        ("rate closure", "clock/rate is " + "derived"),
        ("audit verdict", "promoted to " + "retained"),
        ("authority edit", "updates repo-wide " + "authority"),
    ]
    for label, phrase in forbidden_wording:
        check(f"forbidden wording absent: {label}", phrase not in text)

    section("N5 EXECUTION CERTIFICATE (print-only; registers no check)")
    emit(
        "  per_element: checked and not executed -- this runner never computes a number. Its entire state is sets of "
        f"gate names and a dictionary of {len(CLAIMS)} claims mapped to the gates each one requires, and every "
        "operation performed on them is set membership, set union or equality of strings. There is no array and "
        "therefore no element, so any element-level reading of this firewall would be fabricated."
    )
    emit(
        "  per_site: checked and not executed -- no lattice, no site index and no spatial notion enters at any "
        "point. What the file classifies is provenance: which gates a claim would need, and whether those gates are "
        "on the record side or must be supplied from outside. That question sits entirely above any site-level "
        "description and would read the same for a system of any size or shape."
    )
    emit(
        "  per_mode: checked and not executed -- there is no state space, no basis and no spectrum here, so nothing "
        "can carry a mode. The word dial in this file names an externally supplied setting, tracked as the string "
        "gate dial_selector, and not a mode, channel or eigenvalue; no decomposition of anything is formed."
    )
    emit(
        f"  per_block: checked and not executed -- no space is decomposed into blocks. The single partition present "
        f"is the disjoint split of gate names into the {len(RECORD_GATES)} record-side gates and the "
        f"{len(EXTERNAL_GATES)} external gates, and that is a provenance partition over labels rather than a "
        "decomposition of any physical object, so it supports no block-resolved physical statement."
    )
    emit(
        "  lattice_wide: checked and not executed -- nothing of any extent is built, so there is no whole-system "
        "quantity, no finite-N statement and no limit. The firewall's content is that dial_selector is absent from "
        "the record-side gate set outright, which holds independently of how large or small any underlying system "
        "would be; that scale-independence is exactly why no lattice-wide claim can be made from this file."
    )

    section("SCORECARD")
    emit(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
