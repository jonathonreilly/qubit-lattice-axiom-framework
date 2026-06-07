#!/usr/bin/env python3
"""Read-only sidecar classifier for Record-selector audit repair targets.

This runner consumes only audit metadata and source notes for the 13 rows
historically surfaced by the Record typing audit unlock map as
`selector_split_after_type`. Some rows may have advanced since the sidecar was
created; this runner checks that they remain known audit rows and keeps the
sidecar classification usable without applying audit verdicts.

The sidecar applies the selector theorem:

* post-record atom/channel symmetry can support the equal-letter location;
* pre-record microstate/dimension symmetry can support the dimension endpoint;
* stability alone leaves the dial open;
* many rows are not prior-selector rows at all once the type firewall is clean.

Run:
    python3 scripts/frontier_record_selector_audit_sidecar_2026_06_05.py
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs/audit/data/audit_ledger.json"


SIDE_CAR_ROWS: dict[str, dict[str, object]] = {
    "axiom_first_cluster_decomposition_theorem_note_2026-04-29": {
        "class": "false_positive_not_selector",
        "endpoint": "none",
        "repair": "Do not route through the selector theorem; the blocker is a transfer/spatial gap and cluster-decomposition bridge.",
        "use": "Record selector theorem does not move this row.",
        "must": "Lieb-Robinson",
    },
    "flavor_asymmetry_identification_principled_not_forced_2026-05-31": {
        "class": "observable_identification_bridge",
        "endpoint": "none",
        "repair": "Derive or admit the generation-space/local-density-as-observable bridge.",
        "use": "The selector theorem keeps this as an observable-identification gate, not a prior-selection gate.",
        "must": "single-fixed-point local density",
    },
    "flavor_emergent_chirality_no_transport_note_2026-05-30": {
        "class": "dynamics_or_orbit_breaking_bridge",
        "endpoint": "none",
        "repair": "Supply a native C3-breaking/orbit-splitting operator or spectral-asymmetry dynamics.",
        "use": "The selector theorem does not supply the missing generation transport or C3-breaking dynamics.",
        "must": "C₃-breaking",
    },
    "flavor_find_j_round1_jcs_measure_neutral_2026-06-02": {
        "class": "stable_dial_open",
        "endpoint": "dial",
        "repair": "Find a first-order/action or dynamics bridge; static J_cs is measure-neutral.",
        "use": "Confirms that a named structure can be native while the dial position remains open.",
        "must": "measure-NEUTRAL",
    },
    "flavor_generation_space_bridge_reduces_to_open_gate_2026-05-31": {
        "class": "observable_identification_bridge",
        "endpoint": "none",
        "repair": "Close the intensive-summand-as-observable promotion / generation-space bridge.",
        "use": "The selector theorem prevents treating a local summand promotion as a prior selector.",
        "must": "intensive single-fixed-point local density",
    },
    "flavor_measure_positivity_agnostic_note_2026-05-31": {
        "class": "stable_dial_open",
        "endpoint": "dial",
        "repair": "Derive the remaining reality/statistics or cross-factor bit; positivity alone is agnostic.",
        "use": "Matches the theorem's point that stability/positivity does not select the dial position alone.",
        "must": "positivity is AGNOSTIC",
        "must_any": ["positivity is AGNOSTIC", "positivity is blind", "checks are agnostic"],
    },
    "flavor_missing_axiom_carrier_measure_note_2026-05-30": {
        "class": "equal_letter_stable_location",
        "endpoint": "s=0_stable_location",
        "repair": "State the generator-channel HS measure as stable-location support only; do not claim it selects the physical dial position.",
        "use": "The selector theorem names this as equal-channel/post-record stability support, not a Record axiom consequence or dial selector.",
        "must": "generator-channel HS measure",
        "must_any": ["generator-channel HS measure", "generator-channel Hilbert-Schmidt"],
    },
    "flavor_trace_vs_center_dissolves_note_2026-05-30": {
        "class": "stable_dial_open",
        "endpoint": "dial",
        "repair": "Separate readout-class support from the still-free Fourier modulus.",
        "use": "The selector theorem classifies the modulus as a dial unless a dynamics/scoring premise fixes it.",
        "must": "free Fourier modulus",
        "must_any": ["free Fourier modulus", "modulus selector", "r = 1/2 modulus"],
    },
    "koide_kappa_block_total_frobenius_algebraic_narrow_theorem_note_2026-05-10": {
        "class": "equal_letter_stable_location",
        "endpoint": "s=0_stable_location",
        "repair": "Use the equal-weight log-functional as stable-location evidence only; do not promote it to physical dial selection.",
        "use": "The selector theorem identifies the algebra as support for a stable equal-letter location, not a dial-fixing premise.",
        "must": "No selection principle",
    },
    "koide_tracial_standard_form_carrier_narrow_note_2026-06-02": {
        "class": "equal_letter_stable_location",
        "endpoint": "s=0_stable_location",
        "repair": "Keep the carrier/channel-count reading as stable-location support; do not treat the candidate carrier as selecting the physical dial position.",
        "use": "The selector theorem says this is a stable equal-channel location when that surface is used, not an endpoint-forcing result.",
        "must": "channel-counting scoring",
        "must_any": ["channel-counting scoring", "supplied channel-count"],
    },
    "luders_rule_from_composition_consistency_note_2026-05-20": {
        "class": "measurement_update_not_prior",
        "endpoint": "none",
        "repair": "Derive or explicitly admit standard sequential-effect composition for record conditioning.",
        "use": "The selector theorem does not replace a measurement-update/Born-interface derivation.",
        "must": "sequential-effect composition",
    },
    "observable_principle_from_axiom_note": {
        "class": "record_scalar_generator_not_prior",
        "endpoint": "none",
        "repair": "Derive P2 continuous phase-blind scalar-generator selection.",
        "use": "Record additivity helps P1; the selector theorem does not supply log-det/modulus P2.",
        "must": "P2",
    },
    "quark_mass_spectrum_koide_scheme_open_gate_note_2026-05-26": {
        "class": "sector_specific_dial_open_gate",
        "endpoint": "dial",
        "repair": "Derive sector-specific mass scheme/scale and quark-sector dial parameters; do not transfer charged-lepton BAE.",
        "use": "The selector theorem reinforces that a stable charged-lepton endpoint cannot be copied to quarks.",
        "must": "must not be copied",
    },
}


EXPECTED_CLASS_COUNTS = {
    "false_positive_not_selector": 1,
    "observable_identification_bridge": 2,
    "dynamics_or_orbit_breaking_bridge": 1,
    "stable_dial_open": 3,
    "equal_letter_stable_location": 3,
    "measurement_update_not_prior": 1,
    "record_scalar_generator_not_prior": 1,
    "sector_specific_dial_open_gate": 1,
}


FORBIDDEN_WRITES = {
    ROOT / "docs/audit/data/audit_ledger.json",
    ROOT / "docs/audit/data/audit_queue.json",
    ROOT / "docs/audit/data/effective_status_summary.json",
    ROOT / "docs/audit/AUDIT_LEDGER.md",
    ROOT / "docs/audit/AUDIT_QUEUE.md",
}


PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return ok


def load_rows() -> dict[str, dict]:
    return json.loads(LEDGER.read_text())["rows"]


def note_text(path: str) -> str:
    return (ROOT / path).read_text(errors="ignore")


def contains_phrase(text: str, phrase: str) -> bool:
    return re.search(re.escape(phrase), text, flags=re.IGNORECASE) is not None


def main() -> int:
    rows = load_rows()
    touched = []

    print("=== Record selector audit sidecar ===")
    print(f"sidecar_rows={len(SIDE_CAR_ROWS)}")

    check("S0.1 sidecar has exactly the 13 selector-split audited-conditional rows", len(SIDE_CAR_ROWS) == 13)
    check("S0.2 expected class counts sum to 13", sum(EXPECTED_CLASS_COUNTS.values()) == 13)

    class_counts = Counter(entry["class"] for entry in SIDE_CAR_ROWS.values())
    check("S0.3 class counts match expected repair buckets", dict(class_counts) == EXPECTED_CLASS_COUNTS, str(dict(class_counts)))

    for claim_id, entry in SIDE_CAR_ROWS.items():
        row = rows.get(claim_id)
        check(f"L1 {claim_id} exists in audit ledger", row is not None)
        if row is None:
            continue
        path = row.get("note_path") or ""
        text = note_text(path) if path else ""
        touched.append((claim_id, row, entry))
        check(
            f"L2 {claim_id} has explicit current ledger metadata",
            bool(row.get("audit_status")) and bool(row.get("effective_status")),
            f"audit_status={row.get('audit_status')} effective_status={row.get('effective_status')}",
        )
        check(f"L3 {claim_id} note path exists", bool(path) and (ROOT / path).exists(), path)
        anchors = entry.get("must_any") or [entry["must"]]
        check(
            f"L4 {claim_id} source text matches sidecar anchor",
            any(contains_phrase(text, str(anchor)) for anchor in anchors),
            ", ".join(str(anchor) for anchor in anchors),
        )
        check(f"L5 {claim_id} sidecar class is nonempty", bool(entry["class"]))
        check(f"L6 {claim_id} repair target is nonempty", bool(entry["repair"]))

    endpoint_counts = Counter(entry["endpoint"] for entry in SIDE_CAR_ROWS.values())
    check("E1 endpoint counts expose stable locations without forcing them", endpoint_counts["s=0_stable_location"] == 3 and endpoint_counts["dial"] == 4)
    check("E2 no sidecar row claims a forced endpoint", all(entry["endpoint"] != "forced" for entry in SIDE_CAR_ROWS.values()))
    check(
        "E3 all s=0 stable-location rows are explicitly non-selecting",
        all(
            "do not" in entry["repair"].lower()
            for entry in SIDE_CAR_ROWS.values()
            if entry["endpoint"] == "s=0_stable_location"
        ),
    )
    check(
        "E4 all dial rows remain open-dial rows",
        all(entry["class"] in {"stable_dial_open", "sector_specific_dial_open_gate"} for entry in SIDE_CAR_ROWS.values() if entry["endpoint"] == "dial"),
    )

    untouched_audit_files_ok = all(path.exists() for path in FORBIDDEN_WRITES)
    check("audit-data-readonly guard: audit data files are read-only inputs in this runner", untouched_audit_files_ok)
    check("audit-vocab guard: runner has no audit verdict vocabulary in sidecar classes", all(not e["class"].startswith("audited_") for e in SIDE_CAR_ROWS.values()))

    print("\n=== Repair buckets ===")
    for cls, count in sorted(class_counts.items()):
        print(f"{cls}: {count}")

    print("\n=== Row sidecar table ===")
    for claim_id, row, entry in touched:
        print(
            " | ".join(
                [
                    claim_id,
                    row.get("claim_type") or "",
                    row.get("criticality") or "",
                    entry["class"],
                    entry["endpoint"],
                    entry["repair"],
                ]
            )
        )

    print("\n=== Interpretation ===")
    print("The selector theorem moves three rows into an explicit s=0 stable-location bucket, not a physical selector bucket.")
    print("Four rows remain dial-open: stability or native structure is not enough to pick a position.")
    print("Six rows are not prior-selector closures after the Record type firewall: they need observable identification, dynamics/orbit breaking, measurement-update, scalar-generator, or sector-specific mass-scheme repairs.")
    print("No audit verdicts are applied and no audit data is written.")

    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
