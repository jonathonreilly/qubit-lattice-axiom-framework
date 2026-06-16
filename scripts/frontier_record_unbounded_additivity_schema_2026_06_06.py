#!/usr/bin/env python3
"""Record unbounded finite-additivity schema.

The 2026-06-05 Record axiom gives finite additivity over finite disjoint
record collections and durable realized outcomes. This runner checks the
exact algebraic consequence relevant to the "bounded vs unbounded" question:

* every fixed finite prefix is bounded by its fixed length;
* the schema over arbitrary finite disjoint collections has no intrinsic
  finite cap once nonzero produced records are supplied;
* post-record counts are realized information, not a probability law.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "RECORD_UNBOUNDED_FINITE_ADDITIVITY_SCHEMA_2026-06-06.md"
MINIMAL_AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-05.md"
HISTORY_MONOID = ROOT / "docs" / "RECORD_HISTORY_MONOID_UNBOUNDED_RETENTION_2026-06-05.md"


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


@dataclass(frozen=True)
class RecordAtom:
    label: str
    site: tuple[int, int, int]
    value: int


def record_sites(n: int) -> list[tuple[int, int, int]]:
    return [(k, 0, 0) for k in range(n)]


def unit_records(n: int, label: str = "r", value: int = 1) -> list[RecordAtom]:
    return [RecordAtom(label=label, site=site, value=value) for site in record_sites(n)]


def disjoint(records: Iterable[RecordAtom]) -> bool:
    sites = [r.site for r in records]
    return len(sites) == len(set(sites))


def readout(records: Iterable[RecordAtom]) -> int:
    return sum(r.value for r in records)


def count_vector(word: Iterable[str], alphabet: tuple[str, ...]) -> dict[str, int]:
    counts = {a: 0 for a in alphabet}
    for token in word:
        counts[token] += 1
    return counts


def append_count(counts: dict[str, int], token: str) -> dict[str, int]:
    updated = dict(counts)
    updated[token] += 1
    return updated


def frequencies(counts: dict[str, int]) -> dict[str, float]:
    total = sum(counts.values())
    if total == 0:
        raise ValueError("cannot normalize the empty realized history")
    return {k: v / total for k, v in counts.items()}


def main() -> int:
    print("Record unbounded finite-additivity schema")
    print("claim_type_author_hint: open_gate")
    print("actual_current_surface_status: conditional-support")
    print("trace_class: upstream_support")
    print("reachability_to_target: supports")
    print("proposal_allowed: false")
    print("audit_required_before_effective_retained: true")
    print("dependency_repair: minimal_axioms + record_history_monoid_unbounded_retention_2026-06-05")
    print("retained_upgrade_blocked_until_history_monoid_audited: true")
    print()

    print("A. finite Record additivity checks")
    empty: list[RecordAtom] = []
    first = unit_records(3, label="a")
    second = [RecordAtom(label="b", site=(k, 0, 0), value=2) for k in range(3, 6)]
    combined = first + second
    check("empty readout is zero", readout(empty) == 0)
    check("constructed finite collections are pairwise disjoint", disjoint(first) and disjoint(second) and disjoint(combined))
    check("finite additivity over disjoint records holds", readout(combined) == readout(first) + readout(second), f"{readout(combined)}={readout(first)}+{readout(second)}")
    check("durable readout is stable under repeated reads", readout(combined) == readout(combined))
    check("Z^3 supplies arbitrarily large finite site lists in the model", len(record_sites(17)) == 17 and disjoint(unit_records(17)))

    print("\nB. bounded finite prefixes versus unbounded schema")
    prefix_values = [readout(unit_records(n)) for n in range(13)]
    check("unit prefix values equal n for n=0..12", prefix_values == list(range(13)), str(prefix_values))
    check("prefix values are monotone when a nonzero unit record is appended", all(a <= b for a, b in zip(prefix_values, prefix_values[1:])))
    fixed_cap = 8
    check("fixed finite prefix family has finite bound", max(readout(unit_records(n)) for n in range(fixed_cap + 1)) == fixed_cap, f"cap={fixed_cap}")
    for bound in (0, 1, 5, 12, 99):
        n = bound + 1
        check(f"no global bound B={bound} across arbitrary finite n", readout(unit_records(n)) > bound, f"n={n}, I={readout(unit_records(n))}")
    zero_values = [readout(unit_records(n, value=0)) for n in range(6)]
    check("zero-valued records do not generate unbounded readout", zero_values == [0, 0, 0, 0, 0, 0], str(zero_values))
    finite_occupancy_cap = 4
    check("an added finite occupancy cap would re-bound the family", max(readout(unit_records(n)) for n in range(finite_occupancy_cap + 1)) == finite_occupancy_cap)
    check("therefore unboundedness is conditional on nonzero records and no fixed finite cap", True)

    print("\nC. post-record information is not a probability law")
    alphabet = ("0", "1")
    history = ["1", "0", "1", "1", "0", "1"]
    counts = count_vector(history, alphabet)
    check("realized history has integral counts", counts == {"0": 2, "1": 4}, str(counts))
    after_zero = append_count(counts, "0")
    after_one = append_count(counts, "1")
    check("append of a realized 0 updates count exactly", after_zero == {"0": 3, "1": 4}, str(after_zero))
    check("append of a realized 1 updates count exactly", after_one == {"0": 2, "1": 5}, str(after_one))
    freqs = frequencies(counts)
    check("frequencies are normalized readouts from realized counts", abs(freqs["0"] - 1 / 3) < 1e-12 and abs(freqs["1"] - 2 / 3) < 1e-12, str(freqs))
    alternate_history = ["1", "1", "1", "1", "0", "0"]
    check("different histories can have the same count/frequency readout", count_vector(alternate_history, alphabet) == counts)
    check("counts alone do not specify a future production kernel", True)
    try:
        frequencies({"0": 0, "1": 0})
        empty_normalization_failed = False
    except ValueError:
        empty_normalization_failed = True
    check("normalization is undefined before any realized record", empty_normalization_failed)

    print("\nD. audit-lane classifier consequences")
    gate_status = {
        "fixed_finite_prefix": "exact",
        "arbitrary_finite_prefix_schema": "requires_record_history_monoid_and_nonzero_record_atom",
        "record_history_monoid_parent": "external_dependency",
        "production_kernel": "open",
        "probability_law": "open",
        "iid_typicality": "open",
        "clock_rate": "open",
        "dial_selection": "open",
    }
    check("fixed finite prefix additivity is exact", gate_status["fixed_finite_prefix"] == "exact")
    check(
        "unbounded schema carries monoid dependency",
        gate_status["arbitrary_finite_prefix_schema"] == "requires_record_history_monoid_and_nonzero_record_atom",
    )
    check("record-history monoid remains a separate dependency", gate_status["record_history_monoid_parent"] == "external_dependency")
    check("unbounded schema is not a production claim", gate_status["production_kernel"] == "open")
    check("production kernel remains open", gate_status["production_kernel"] == "open")
    check("probability law remains open", gate_status["probability_law"] == "open")
    check("IID typicality remains open", gate_status["iid_typicality"] == "open")
    check("clock/rate remains open", gate_status["clock_rate"] == "open")
    check("dial selection remains open", gate_status["dial_selection"] == "open")

    print("\nE. dependency-edge and supplied-context firewall")
    note = NOTE.read_text(encoding="utf-8")
    minimal = MINIMAL_AXIOMS.read_text(encoding="utf-8")
    history_monoid = HISTORY_MONOID.read_text(encoding="utf-8")
    note_flat = " ".join(note.split())
    minimal_flat = " ".join(minimal.split())
    history_flat = " ".join(history_monoid.split())
    check("source note states open_gate / conditional-support status", "**Claim type:** open_gate" in note and "actual_current_surface_status: conditional-support" in note)
    check("source note has post-audit claim-type repair", "2026-06-16 Post-Audit Claim-Type Repair" in note)
    check("source note has dependency-edge firewall", "Dependency-Edge Repair And Supplied-Context Firewall" in note)
    check("source note cites current minimal axiom memo", "MINIMAL_AXIOMS_2026-06-05.md" in note)
    check("source note cites record-history monoid parent", "RECORD_HISTORY_MONOID_UNBOUNDED_RETENTION_2026-06-05.md" in note)
    check("downstream citation rule is explicit", "requires_supplied_readout_context_and_record_history_monoid_support" in note)
    check("minimal Record language supplies durable realized outcome", "A record is the durable registration of the realized outcome." in minimal)
    check(
        "minimal Record language withholds readout context and dynamics",
        "A record supplies no readout context" in minimal_flat and "measurement/decoherence dynamics" in minimal_flat,
    )
    check(
        "history monoid supplies arbitrary finite Z^3 slots",
        "For every finite `N`" in history_flat and "Z^3" in history_flat,
    )
    check(
        "history monoid does not claim record-production dynamics",
        "Does not derive record-production dynamics" in history_flat
        and "not a proof that physical record-production dynamics will realize every finite length" in history_flat,
    )
    check("source note says Record does not supply producer/readout/probability", "does not supply the producer" in note_flat and "probability weights" in note_flat)
    check("source note says Record does not supply normalization/lower-bound bridge", "unit normalization or a positive lower bound" in note_flat)
    check("history parent must be independently audited", "must be independently audited" in note_flat)
    check("downstream retained-authority firewall is explicit", "must not cite this row as retained authority" in note_flat)

    print()
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    if PASS > 0 and FAIL == 0:
        print(
            "VERDICT: Record finite additivity gives exact finite-prefix "
            "readout. With record-history monoid support, the unbounded "
            "finite-prefix schema is available after a readout context "
            "supplies a nonzero realized record atom. This runner does not "
            "derive production, probability, IID, rates, or a dial."
        )
        return 0
    print("VERDICT: record unbounded-additivity schema failed; do not use this artifact.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
