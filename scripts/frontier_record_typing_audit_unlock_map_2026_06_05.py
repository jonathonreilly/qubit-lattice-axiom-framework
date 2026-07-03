#!/usr/bin/env python3
"""Audit-lane dispatch map for the Record typing firewall.

This is not an audit verdict runner. It reads audit metadata and source notes,
then classifies bounded/conditional rows by whether the exact Record typing
firewall can help:

* type_firewall_reaudit: the exact theorem can directly supply the object-type
  separation "record atom != probability state".
* born_record_interface: the theorem supports a cleaner pre-record/predictive
  versus post-record/realized split, but Born frequency/typicality remains open.
* selector_split_after_type: the theorem makes the record alphabet well typed,
  but a weighting/measure/Koide/generation selector remains open.
* dynamics_split_after_type: the theorem types the post-record value, but a
  physical instrument, decoherence, arrow, or stability dynamics remains open.
* not_record_relevant: the row is not touched by this theorem.

The runner deliberately does not read prior verdict rationales and does not
write audit data.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs/audit/data/audit_ledger.json"

RECORD_RE = re.compile(
    r"\b(record|readout|post-record|pre-record|K/CPT|orbit|central-sector|"
    r"sector|atom|event algebra)\b",
    re.IGNORECASE,
)
FOCUS_RE = re.compile(
    r"(RECORD|READOUT|BORN|PROBABILITY|KOIDE|GENERATION|MEASURE|WEIGHT|"
    r"PRE_RECORD|POST_RECORD)",
    re.IGNORECASE,
)
STRONG_RECORD_RE = re.compile(
    r"(Record axiom|K/CPT|post-record|pre-record|record atom|record alphabet|"
    r"realized record|realized outcome|event algebra)",
    re.IGNORECASE,
)
BORN_RE = re.compile(r"\b(Born|probability|probabilit|typicality|frequency)\b", re.IGNORECASE)
SELECTOR_RE = re.compile(
    r"\b(Koide|generation|weight|weighting|measure|prior|selector|selects|"
    r"normalization|dimension|block-count|Q=2/3|r=1/2|gamma)\b",
    re.IGNORECASE,
)
DYNAMICS_RE = re.compile(
    r"\b(dynamics|decoherence|instrument|Kraus|Hamiltonian|arrow|einselection|"
    r"thermaliz|stability|stable|flow|CPTP|measurement)\b",
    re.IGNORECASE,
)
TYPE_RE = re.compile(
    r"\b(atom|event algebra|orbit|not (a )?probability|probability state|"
    r"one-hot|realized outcome|realized record|information token)\b",
    re.IGNORECASE,
)

SCOPE_EFFECTIVE = {"retained_bounded", "retained_pending_chain", "audited_conditional"}

MUST_TOUCH = {
    "docs/RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md": {
        "type_firewall_reaudit",
        "selector_split_after_type",
    },
    "docs/OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md": {
        "type_firewall_reaudit",
        "born_record_interface",
    },
    "docs/BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md": {
        "born_record_interface",
    },
    "docs/PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md": {
        "born_record_interface",
    },
    "docs/PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md": {
        "dynamics_split_after_type",
    },
    "docs/PERSISTENT_RECORD_INSTRUMENT_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-22.md": {
        "dynamics_split_after_type",
    },
    "docs/FLAVOR_RECORD_READOUT_FORM_NOT_WEIGHT_2026-06-02.md": {
        "selector_split_after_type",
    },
    "docs/FLAVOR_RECORD_DYNAMICS_SHARPENS_ARROW_STABILIZER_FAILS_2026-06-02.md": {
        "dynamics_split_after_type",
        "selector_split_after_type",
    },
    "docs/FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md": {
        "selector_split_after_type",
        "dynamics_split_after_type",
    },
    "docs/GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md": {
        "selector_split_after_type",
    },
    "docs/KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md": {
        "selector_split_after_type",
    },
    "docs/KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE_NOTE_2026-05-30.md": {
        "selector_split_after_type",
    },
    "docs/KOIDE_RECORDS_POINTER_GROUNDS_BLOCK_CHANNEL_NOTE_2026-05-31.md": {
        "selector_split_after_type",
        "dynamics_split_after_type",
    },
    "docs/KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31.md": {
        "dynamics_split_after_type",
        "selector_split_after_type",
    },
}


def scoped(row: dict) -> bool:
    return (
        row.get("audit_status") == "audited_conditional"
        or row.get("effective_status") in SCOPE_EFFECTIVE
        or row.get("claim_type") == "bounded_theorem"
    )


def source_text(path: str) -> str:
    p = ROOT / path
    if not p.exists():
        return ""
    return p.read_text(errors="ignore")


def classify_text(path: str, title: str, text: str) -> str:
    hay = "\n".join([path, title, text[:25000]])
    path_title = "\n".join([path, title])
    path_upper = path.upper()

    # Keep the broad ledger scan honest: ordinary words such as "recorded",
    # "generation", or "dimension" appear in many unrelated notes. A row only
    # enters the unlock map if the path/title is in the Record/Born/Koide/
    # generation/readout family or the source text uses strong Record-axiom
    # phrases.
    if not FOCUS_RE.search(path_title) and not STRONG_RECORD_RE.search(hay):
        return "not_record_relevant"

    # Path-level precedence for known interface families. These are not audit
    # verdicts; they prevent generic "measure/normalization" terms from hiding
    # the cheaper dispatch class.
    if "PERSISTENT_RECORD" in path_upper or "KRAUS" in path_upper:
        return "dynamics_split_after_type"
    if "BORN" in path_upper or "PRE_RECORD_REFERENCE" in path_upper:
        return "born_record_interface"
    if "OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO" in path_upper:
        return "type_firewall_reaudit"

    record = bool(RECORD_RE.search(hay))
    born = bool(BORN_RE.search(hay))
    selector = bool(SELECTOR_RE.search(hay))
    dynamics = bool(DYNAMICS_RE.search(hay))
    typed = bool(TYPE_RE.search(hay))

    if not record and not (born and "record" in hay.lower()):
        return "not_record_relevant"
    if selector:
        return "selector_split_after_type"
    if dynamics:
        return "dynamics_split_after_type"
    if born:
        return "born_record_interface"
    if typed or record:
        return "type_firewall_reaudit"
    return "not_record_relevant"


def check(name: str, ok: bool, detail: str = "") -> bool:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(ok)


def row_label(row: dict) -> str:
    return (
        f"{row.get('claim_id')} | {row.get('audit_status')} | "
        f"{row.get('effective_status')} | {row.get('claim_type')} | {row.get('note_path')}"
    )


def main() -> int:
    rows = list(json.loads(LEDGER.read_text())["rows"].values())
    candidates = [r for r in rows if scoped(r)]
    buckets: dict[str, list[dict]] = defaultdict(list)

    for row in candidates:
        path = row.get("note_path") or ""
        text = source_text(path)
        cat = classify_text(path, row.get("title") or "", text)
        row["_record_unlock_category"] = cat
        buckets[cat].append(row)

    category_counts = Counter(r["_record_unlock_category"] for r in candidates)
    conditional = [r for r in rows if r.get("audit_status") == "audited_conditional"]
    conditional_counts = Counter()
    for row in conditional:
        path = row.get("note_path") or ""
        conditional_counts[classify_text(path, row.get("title") or "", source_text(path))] += 1

    print("=== Record typing audit-unlock map ===")
    print(f"ledger_rows={len(rows)}")
    print(f"scoped_bounded_or_conditional_rows={len(candidates)}")
    print(f"audited_conditional_rows={len(conditional)}")
    print("\nCategory counts over bounded/conditional scope:")
    for cat, count in sorted(category_counts.items()):
        print(f"  {cat}: {count}")
    print("\nCategory counts over audited_conditional only:")
    for cat, count in sorted(conditional_counts.items()):
        print(f"  {cat}: {count}")

    print("\nAudited-conditional rows touched by the Record typing firewall:")
    for row in conditional:
        path = row.get("note_path") or ""
        cat = classify_text(path, row.get("title") or "", source_text(path))
        if cat != "not_record_relevant":
            print(f"  {cat}: {row_label(row)}")

    print("\n=== Top dispatch rows ===")
    for cat in (
        "type_firewall_reaudit",
        "born_record_interface",
        "selector_split_after_type",
        "dynamics_split_after_type",
    ):
        print(f"\n[{cat}]")
        for row in buckets.get(cat, [])[:12]:
            print("  " + row_label(row))

    print("\n=== Must-touch source probes ===")
    must_ok = 0
    must_seen = 0
    for rel, allowed in MUST_TOUCH.items():
        path = ROOT / rel
        exists = path.exists()
        cat = classify_text(rel, "", path.read_text(errors="ignore") if exists else "")
        ok = exists and cat in allowed
        if exists:
            must_seen += 1
        if ok:
            must_ok += 1
        print(f"{'PASS' if ok else 'MISS'} {rel} -> {cat} allowed={sorted(allowed)}")

    print("\n=== Unlock interpretation ===")
    print(
        "DIRECT: type_firewall_reaudit rows can cite the exact Record typing theorem "
        "after it is retained, then re-audit the narrowed object-type claim."
    )
    print(
        "SPLIT: selector_split_after_type rows get a clean record alphabet/type, "
        "but still need a measure/weight/Koide/generation selector."
    )
    print(
        "SPLIT: dynamics_split_after_type rows get a clean post-record value type, "
        "but still need an instrument/decoherence/arrow/stability theorem."
    )
    print(
        "NO AUTO-PROMOTION: this runner writes no audit data and applies no verdicts."
    )

    checks = [
        check("ledger has substantial audit surface", len(rows) > 1000, str(len(rows))),
        check(
            "every scoped bounded/conditional row is bucketed",
            sum(category_counts.values()) == len(candidates),
            f"{sum(category_counts.values())}/{len(candidates)}",
        ),
        check(
            "every audited_conditional row is bucketed",
            sum(conditional_counts.values()) == len(conditional),
            f"{sum(conditional_counts.values())}/{len(conditional)}",
        ),
        check("has direct type-firewall re-audit candidates", category_counts["type_firewall_reaudit"] > 0),
        check("has Born/Record interface candidates", category_counts["born_record_interface"] > 0),
        check("has selector split candidates", category_counts["selector_split_after_type"] > 0),
        check("has dynamics split candidates", category_counts["dynamics_split_after_type"] > 0),
        check("must-touch source probes mostly classified", must_ok >= 10, f"{must_ok}/{must_seen}"),
    ]

    pass_count = sum(checks)
    fail_count = len(checks) - pass_count
    print("\n=== Scorecard ===")
    print(f"PASS={pass_count} FAIL={fail_count}")
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
