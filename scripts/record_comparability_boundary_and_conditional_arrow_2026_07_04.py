#!/usr/bin/env python3
"""Mechanical checks for the record-comparability no-go/certification packet."""

from __future__ import annotations

import json
import math
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PREMISE_NODES = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
DOC_AUTHORITY = ROOT / "docs" / "audit" / "data" / "doc_authority_registry.json"
NO_GO_NOTE = ROOT / "docs" / "RECORD_COMPARABILITY_NOT_DERIVED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-07-04.md"
CERT_NOTE = ROOT / "docs" / "RECORD_COMPARABILITY_CONDITIONAL_CHAIN_ARROW_CERTIFICATION_BOUNDED_NOTE_2026-07-04.md"
OWNER_PAGER = ROOT / "docs" / "RECORD_COMPARABILITY_OWNER_ONE_PAGER_2026-07-04.md"
TIER_A = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"

ONE_CONFIG_SENTENCE = "There is one configuration of records."
SITES = ("x", "y", "z")

PASS = 0
FAIL = 0


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict:
    return json.loads(read(path))


def record(label: str, passed: bool, detail: str = "") -> None:
    global PASS, FAIL
    if passed:
        PASS += 1
    else:
        FAIL += 1
    status = "PASS" if passed else "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{status}] {label}{suffix}")


def config(*sites: str) -> frozenset[str]:
    return frozenset(sites)


def is_state(c: frozenset[str]) -> bool:
    return c.issubset(set(SITES))


def comparable(a: frozenset[str], b: frozenset[str]) -> bool:
    return a.issubset(b) or b.issubset(a)


def strict_successor(a: frozenset[str], b: frozenset[str]) -> bool:
    return a.issubset(b) and a != b


def chain(configs: list[frozenset[str]]) -> bool:
    return all(comparable(a, b) for a, b in combinations(configs, 2))


def has_occurrence(history: list[frozenset[str]]) -> bool:
    return any(strict_successor(a, b) for a, b in zip(history, history[1:]))


def monotone(history: list[frozenset[str]]) -> bool:
    return all(a.issubset(b) for a, b in zip(history, history[1:]))


def strictly_growing_where_changed(history: list[frozenset[str]]) -> bool:
    return all((a == b) or strict_successor(a, b) for a, b in zip(history, history[1:]))


def terminal_incomparable_branch_family() -> tuple[list[frozenset[str]], list[frozenset[str]]]:
    empty = config()
    return [empty, config("x")], [empty, config("y")]


def all_one_step_chains() -> list[list[frozenset[str]]]:
    empty = config()
    return [[empty, config(site)] for site in SITES]


def text_checks() -> None:
    ax = read(AXIOMS)
    node_data = load_json(PREMISE_NODES)
    doc_auth = load_json(DOC_AUTHORITY)
    no_go = read(NO_GO_NOTE)
    cert = read(CERT_NOTE)
    owner = read(OWNER_PAGER)
    tier_a = load_json(TIER_A)

    minimal_note = node_data["nodes"]["minimal_axioms"]["note"]
    owner_rows = [row for row in doc_auth["rows"] if row["path"] == "docs/RECORD_COMPARABILITY_OWNER_ONE_PAGER_2026-07-04.md"]

    record("axiom has occurrence sentence", "Records form." in ax)
    record("axiom has state-as-configuration sentence", "A state is a configuration of records." in ax)
    record("axiom has permanence sentence", "records are permanent" in ax)
    record("axiom has one-record-per-site sentence", "site never carries more than one record" in ax)
    record("axiom requires further physical structure to be supplied separately", "Further physical\nstructure requires derivation" in ax)
    record("axiom excludes record-production process in prose", "record-production process" in ax)
    record("one-configuration sentence is not landed in axiom memo", ONE_CONFIG_SENTENCE not in ax)
    record("premise node mirrors occurrence", "records form" in minimal_note)
    record("premise node excludes state-selection", "state-selection rule" in minimal_note)
    record("premise node excludes record-production process", "record-production process" in minimal_note)
    record("premise node excludes formation rule", "formation rule" in minimal_note)
    record("owner pager names one-configuration sentence", ONE_CONFIG_SENTENCE in owner)
    record("owner pager declares no weight until acted on", "no weight until you act on it" in owner)
    record("doc authority registers owner pager as Class D", bool(owner_rows) and owner_rows[0]["class"] == "D")
    record("doc authority registers owner pager no-weight boundary", bool(owner_rows) and "No weight until decided" in owner_rows[0]["note"])
    record("no-go note states branching exhibit", "branch X: empty -> {x}" in no_go and "branch Y: empty -> {y}" in no_go)
    record("no-go note states not co-realized physical multiplicity", "not asserted as co-realized physical\n  multiplicity" in no_go)
    record("certification note states conditional-only boundary", "It is not derived here" in cert)
    record("certification note excludes clock/rate", "what clock, time metric, or simultaneity convention applies" in cert)
    record("certification note excludes formation selector", "which site receives a record" in cert)
    record("Tier-A registry still has two genuine admissions", tier_a.get("genuine_admitted_input_count") == 2)
    record(
        "Tier-A registry labels remain AC_phi_lambda and theta",
        sorted(v["label"] for v in tier_a["derivation_targets"].values()) == ["AC_phi_lambda", "theta"],
    )


def no_go_model_checks() -> None:
    hx, hy = terminal_incomparable_branch_family()
    tx, ty = hx[-1], hy[-1]

    record("branch X consists of valid states", all(is_state(c) for c in hx))
    record("branch Y consists of valid states", all(is_state(c) for c in hy))
    record("branch X has occurrence", has_occurrence(hx))
    record("branch Y has occurrence", has_occurrence(hy))
    record("branch X is monotone by permanence", monotone(hx))
    record("branch Y is monotone by permanence", monotone(hy))
    record("branch terminals are distinct", tx != ty)
    record("equal cardinality does not force identical record content", math.isclose(len(tx), len(ty)) and tx != ty)
    record("branch terminals are not comparable", not comparable(tx, ty), f"{sorted(tx)} vs {sorted(ty)}")
    record("combined alternative family is not a chain", not chain([tx, ty]))


def conditional_chain_checks() -> None:
    chain_history = [config(), config("x"), config("x", "y"), config("x", "y", "z")]
    simultaneous_jump = [config(), config("x", "y")]
    one_step_chains = all_one_step_chains()

    record("conditional history is pairwise comparable", chain(chain_history))
    record("conditional history is monotone", monotone(chain_history))
    record("conditional history strictly grows where changed", strictly_growing_where_changed(chain_history))
    record("conditional history has occurrence", has_occurrence(chain_history))
    record("simultaneous multi-record jump remains a chain", chain(simultaneous_jump) and strict_successor(*simultaneous_jump))
    record("one-step x and y chains both satisfy comparability", chain(one_step_chains[0]) and chain(one_step_chains[1]))
    record("different first-site choices remain valid", one_step_chains[0][-1] != one_step_chains[1][-1])
    record("comparability does not select the first site", len({hist[-1] for hist in one_step_chains}) == len(SITES))
    record("comparability adds no numeric rate field", all(len(hist) == 2 for hist in one_step_chains))


def main() -> int:
    print("Record comparability boundary and conditional arrow checks")
    print("=" * 68)
    text_checks()
    no_go_model_checks()
    conditional_chain_checks()
    print("=" * 68)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
