#!/usr/bin/env python3
"""Exact checks for the reading-note derivation note (2026-07-02).

Toy availability model plus verbatim axiom-text guards. No floats, no repo
imports; stdlib only.
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

EM_DASH = "—"

checks = []


def check(condition, description):
    checks.append(bool(condition))
    status = "PASS" if condition else "FAIL"
    print(f"CHECK {len(checks):02d}: {status} {EM_DASH} {description}")


def normalize(text):
    return re.sub(r"\s+", " ", text)


axiom_text = normalize(AXIOM_PATH.read_text(encoding="utf-8"))

# Toy model: two-possibility domain, availability determined by a neighbor flag.
DOMAIN = frozenset({"up", "down"})


def available(neighbor_blocks_up):
    return frozenset({"down"}) if neighbor_blocks_up else DOMAIN


def is_record(assignment, neighbor_blocks_up):
    locked = assignment.get("locked")
    if not isinstance(locked, str):
        return False
    return locked in available(neighbor_blocks_up)


def is_configuration_of_records(assignments, neighbor_blocks_up):
    return all(is_record(a, neighbor_blocks_up) for a in assignments)


# T1: lock outside the available subset is not a record; statehood inherits.
check(
    "locks exactly one local possibility from the subset available" in axiom_text,
    "T1: Record sentence defines records via the available subset",
)
bad = {"locked": "up"}
good = {"locked": "down"}
check(
    not is_record(bad, True) and is_record(good, True),
    "T1: toy model rejects an unavailable lock as a record and accepts an available one",
)
check(
    not is_configuration_of_records([good, bad], True)
    and is_configuration_of_records([good], True)
    and "A state is a configuration of records." in axiom_text,
    "T1: a configuration containing the unavailable lock is not a configuration of records, hence not a state",
)

# T2: per-site uniqueness from option-carry syntax.
check(
    "A site need not carry a record." in axiom_text
    and "When present, a record locks exactly one local possibility" in axiom_text,
    "T2: option-carry syntax present (absent, or present locking exactly one)",
)
site_field_states = [None, {"locked": "down"}]
two_lock_attempt = {"locked": ("up", "down")}
check(
    all(s is None or is_record(s, False) for s in site_field_states)
    and not is_record(two_lock_attempt, False),
    "T2: the per-site field is none-or-one-record; a two-lock assignment is not an instance",
)

# T3: empty configuration is a state with zero readout.
check(
    is_configuration_of_records([], True) and is_configuration_of_records([], False),
    "T3: the empty configuration is vacuously a configuration of records under any conditions",
)
check(
    "`I(empty)=0`" in axiom_text,
    "T3: I(empty)=0 is verbatim Record text",
)

# T4: the "supplied" disambiguation is carried by the text.
check(
    "Its domain is a supplied condition" in axiom_text,
    "T4: the law sentence qualifies its condition as supplied",
)
check(
    "nearest-neighbor conditions" in axiom_text
    and "supplied nearest-neighbor conditions" not in axiom_text,
    "T4: Admissibility's conditions carry no 'supplied' qualifier; the texts disambiguate themselves",
)

pass_count = sum(1 for result in checks if result)
fail_count = len(checks) - pass_count
print(f"TOTAL: PASS={pass_count} FAIL={fail_count}")
sys.exit(1 if fail_count else 0)
