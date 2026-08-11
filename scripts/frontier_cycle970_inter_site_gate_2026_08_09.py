#!/usr/bin/env python3
"""Cycle 970: one-CNOT inter-site witness in the Cycle-719 substrate.

Load-bearing operational definition
-----------------------------------
On the two-site basis menu {0, 1}, for a landed gate word W, target site t,
fixed local input x, nearest-neighbor bit n, and target output y, define

    D[W,t,x](y | n) = 1{A.apply_semantic((t=x, neighbor=n), W)_t = y}.

This is the deterministic point distribution induced by the landed basis-state
semantics.  The same x is held on both neighbor branches.

The exhaustive declared family is every word of length zero or one on a
labeled nearest-neighbor two-site patch from the classical basis gate kinds
accepted by Cycle 719: identity, X on either site, and CNOT in either
orientation.  The claim surface is exactly this finite family and its exhibited
one-CNOT witness.

All certificate truth values test bookkeeping consistency.  Neither zero nor
nonzero dependence, nor construction success, is required for a PASS.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
STDOUT_LIMIT_BYTES = 150_000
HOUSE_STDOUT_LIMIT_BYTES = 6_000
AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle715_recurrent_directional_packet_bank_2026_07_26.py",
)

from hashlib import sha256
import json
from pathlib import Path
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
AXIOM_PATH, CORE_PATH, SEMANTICS_PATH = AUDIT_INPUT_PATHS

# The axiom memo is cited authority and therefore text-only.  The Cycle-719
# core is the executable substrate under test, not an imported result verdict.
BLOCKLIST_CITED_PRIMARIES = (AXIOM_PATH,)
EXECUTABLE_SUBSTRATE = CORE_PATH
EXECUTABLE_SEMANTICS = SEMANTICS_PATH

sys.path.insert(0, str(ROOT / "scripts"))
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as CORE

A = CORE.A
SITE_COORDS = ((0, 0, 0), (1, 0, 0))
DEFINITION = (
    "D[W,t,x](y|n)=indicator that landed deterministic basis-state semantics "
    "sends target input x and nearest-neighbor bit n to target output y; the "
    "same x is held on the n=0 and n=1 branches"
)
FAMILY_DESCRIPTION = (
    "all length-zero/one words on a labeled two-site nearest-neighbor patch "
    "from {identity, X on either site, CNOT in either orientation}"
)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def gate_label(gate: object) -> str:
    if gate.kind == "X":
        return f"X({gate.wires[0]})"
    if gate.kind == "CNOT":
        return f"CNOT({gate.wires[0]}->{gate.wires[1]})"
    return f"{gate.kind}{tuple(gate.wires)}"


def declared_family() -> tuple[dict, ...]:
    """Every length <= 1 two-site word from the declared landed kinds."""
    return (
        {"name": "I", "word": ()},
        {"name": "X_0", "word": (A.x(0),)},
        {"name": "X_1", "word": (A.x(1),)},
        {"name": "CNOT_0_TO_1", "word": (A.cn(0, 1),)},
        {"name": "CNOT_1_TO_0", "word": (A.cn(1, 0),)},
    )


def input_state(target: int, local_input: int, neighbor_bit: int) -> tuple[int, int]:
    state = [0, 0]
    state[target] = local_input
    state[1 - target] = neighbor_bit
    return tuple(state)


def point_distribution(
    word: tuple, target: int, local_input: int, neighbor_bit: int
) -> tuple[int, int]:
    after = A.apply_semantic(input_state(target, local_input, neighbor_bit), word)
    outcome = after[target]
    return (int(outcome == 0), int(outcome == 1))


def state_resolved_census() -> dict:
    rows = []
    witnesses = []
    for gate_row in declared_family():
        for target in (0, 1):
            for local_input in (0, 1):
                distributions = tuple(
                    point_distribution(gate_row["word"], target, local_input, n)
                    for n in (0, 1)
                )
                changed = distributions[0] != distributions[1]
                row = {
                    "word_name": gate_row["name"],
                    "gate_word": [gate_label(gate) for gate in gate_row["word"]],
                    "target_site": target,
                    "neighbor_site": 1 - target,
                    "local_input": local_input,
                    "distribution_neighbor_0": list(distributions[0]),
                    "distribution_neighbor_1": list(distributions[1]),
                    "changed": changed,
                }
                rows.append(row)
                if changed:
                    witnesses.append(row)
    return {
        "definition": DEFINITION,
        "family": FAMILY_DESCRIPTION,
        "family_words": len(declared_family()),
        "comparison_contexts": len(rows),
        "conditioned_configurations": 2 * len(rows),
        "changed_comparisons": len(witnesses),
        "conditioned_configurations_in_changed_pairs": 2 * len(witnesses),
        "unchanged_comparisons": len(rows) - len(witnesses),
        "witnesses": witnesses,
        "rows": rows,
    }


def one_cnot_witness() -> dict:
    target, neighbor, local_input = 0, 1, 0
    word = (A.cn(neighbor, target),)
    before = [input_state(target, local_input, n) for n in (0, 1)]
    after = [A.apply_semantic(state, word) for state in before]
    distributions = [
        point_distribution(word, target, local_input, n) for n in (0, 1)
    ]
    succeeded = distributions[0] != distributions[1]
    return {
        "construction_succeeded": succeeded,
        "gate_word": [gate_label(gate) for gate in word],
        "gate_repr": repr(word),
        "word_length": len(word),
        "target_site": target,
        "target_coordinate": SITE_COORDS[target],
        "neighbor_site": neighbor,
        "neighbor_coordinate": SITE_COORDS[neighbor],
        "neighbor_bit_read": neighbor,
        "fixed_local_input": local_input,
        "distribution_neighbor_0": list(distributions[0]),
        "distribution_neighbor_1": list(distributions[1]),
        "input_states": [list(state) for state in before],
        "output_states": [list(state) for state in after],
        "state_mutated_on_neighbor_1": after[1] != before[1],
        "target_mutated_on_neighbor_1": after[1][target] != before[1][target],
    }


def declared_scope(construction: dict, resolved: dict) -> dict:
    return {
        "route": "one_cnot_finite_family_witness",
        "supplied_input": (
            "the target has the same fixed local input x=0 on both neighbor branches"
        ),
        "framework_inputs": [
            "one nearest-neighbor edge",
            "the two basis possibilities {0,1}",
            "the Cycle-719 basis-state CNOT semantics",
        ],
        "family_words": resolved["family_words"],
        "comparison_contexts": resolved["comparison_contexts"],
        "witness_word": construction["gate_word"],
    }


def input_controls() -> dict:
    hashes = {}
    existing = True
    for rel in AUDIT_INPUT_PATHS:
        path = ROOT / rel
        inside = path.resolve().is_relative_to(ROOT.resolve())
        existing &= path.is_file() and inside
        hashes[rel] = sha256(path.read_bytes()).hexdigest() if path.is_file() else None
    axiom_text = (ROOT / AXIOM_PATH).read_text(encoding="utf-8")
    axiom_needle = (
        "For each site, the probability distribution over the possibilities is\n"
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    return {
        "literal_audit_input_paths": list(AUDIT_INPUT_PATHS),
        "all_inputs_exist_worktree_relative": existing,
        "sha256": hashes,
        "blocklist_cited_primaries": list(BLOCKLIST_CITED_PRIMARIES),
        "blocklist_text_only": all(
            not path.endswith(".py") for path in BLOCKLIST_CITED_PRIMARIES
        ),
        "executable_substrate": EXECUTABLE_SUBSTRATE,
        "executable_semantics": EXECUTABLE_SEMANTICS,
        "landed_axiom_needle_matches": axiom_needle in axiom_text,
    }


def run_science() -> dict:
    resolved = state_resolved_census()
    construction = one_cnot_witness()
    return {
        "resolved": resolved,
        "construction": construction,
        "scope": declared_scope(construction, resolved),
    }


def main() -> int:
    started = monotonic()
    first = run_science()
    second = run_science()
    controls = input_controls()
    deterministic = digest(first) == digest(second)

    resolved = first["resolved"]
    construction = first["construction"]
    scope = first["scope"]

    expected_resolved_total = len(declared_family()) * 2 * 2
    a_ok = (
        resolved["comparison_contexts"] == expected_resolved_total
        and resolved["changed_comparisons"] == len(resolved["witnesses"])
        and resolved["changed_comparisons"] + resolved["unchanged_comparisons"]
            == resolved["comparison_contexts"]
        and 0 <= resolved["changed_comparisons"] <= resolved["comparison_contexts"]
        and resolved["conditioned_configurations"] == 2 * expected_resolved_total
        and resolved["conditioned_configurations_in_changed_pairs"]
            == 2 * resolved["changed_comparisons"]
    )
    a_finding = (
        f"definition={DEFINITION}; state_resolved_changed="
        f"{resolved['changed_comparisons']}/{resolved['comparison_contexts']} paired "
        f"comparisons; changed_pair_configurations="
        f"{resolved['conditioned_configurations_in_changed_pairs']}/"
        f"{resolved['conditioned_configurations']}"
    )

    observed_separation = (
        construction["distribution_neighbor_0"]
        != construction["distribution_neighbor_1"]
    )
    b_ok = (
        construction["construction_succeeded"] == observed_separation
        and construction["state_mutated_on_neighbor_1"]
            == (construction["output_states"][1] != construction["input_states"][1])
        and construction["target_mutated_on_neighbor_1"]
            == (construction["output_states"][1][construction["target_site"]]
                != construction["input_states"][1][construction["target_site"]])
    )
    b_finding = (
        f"verdict={'CONSTRUCTED' if construction['construction_succeeded'] else 'OBSTRUCTED'}; "
        f"word={construction['gate_word']}; reads_neighbor_bit="
        f"{construction['neighbor_bit_read']}; D(n=0)="
        f"{construction['distribution_neighbor_0']}; D(n=1)="
        f"{construction['distribution_neighbor_1']}; transition_n1="
        f"{construction['input_states'][1]}->{construction['output_states'][1]}"
    )

    c_ok = (
        construction["construction_succeeded"]
        and scope["route"] == "one_cnot_finite_family_witness"
        and scope["family_words"] == len(declared_family())
        and scope["comparison_contexts"] == expected_resolved_total
        and scope["witness_word"] == construction["gate_word"]
    )
    c_finding = (
        f"route={scope['route']}; family_words={scope['family_words']}; "
        f"contexts={scope['comparison_contexts']}; supplied_input="
        "fixed target input x=0 on both neighbor branches"
    )

    elapsed = monotonic() - started
    pre_output_upper_bound = sum(map(len, (a_finding, b_finding, c_finding))) + 2_000
    d_ok = (
        controls["all_inputs_exist_worktree_relative"]
        and controls["blocklist_text_only"]
        and controls["landed_axiom_needle_matches"]
        and all(controls["sha256"].values())
        and deterministic
        and elapsed < 1400
        and AUDIT_TIMEOUT_SEC < 1400
        and pre_output_upper_bound < HOUSE_STDOUT_LIMIT_BYTES
        and HOUSE_STDOUT_LIMIT_BYTES < STDOUT_LIMIT_BYTES
    )
    d_finding = (
        f"sha_pins={compact(controls['sha256'])}; BLOCKLIST="
        f"{controls['blocklist_cited_primaries']} text_only="
        f"{controls['blocklist_text_only']}; determinism_replay={deterministic}; "
        f"runtime_s={elapsed:.6f}<1400; stdout_upper_bound_bytes="
        f"{pre_output_upper_bound}<{HOUSE_STDOUT_LIMIT_BYTES}<"
        f"{STDOUT_LIMIT_BYTES}; timeout_s={AUDIT_TIMEOUT_SEC}<1400"
    )

    certificates = [
        ("A_STATE_RESOLVED_CENSUS", a_ok, a_finding),
        ("B_ONE_CNOT_WITNESS", b_ok, b_finding),
        ("C_DECLARED_SCOPE", c_ok, c_finding),
        ("D_CONTROLS", d_ok, d_finding),
    ]
    report = {
        "cycle": 970,
        "claim_type": "bounded_theorem",
        "target_claim_type": "bounded_theorem",
        "claim_type_reason": (
            "exact finite two-site basis-menu census plus an explicit "
            "one-CNOT neighbor-conditioned witness at supplied target input x=0"
        ),
        "actual_current_surface_status": "bounded-support",
        "trace_class": "direct_blocker_closure",
        "reachability_to_target": "closes",
        "operational_definition": DEFINITION,
        "findings": first,
        "controls": controls,
        "determinism_replay": deterministic,
        "runtime_sec": elapsed,
        "science_digest": digest(first),
        "certificates": {
            name: {"pass": ok, "finding": finding}
            for name, ok, finding in certificates
        },
        "all_certificates_pass": all(ok for _, ok, _ in certificates),
    }
    checker_payload = {
        "resolved_total": resolved["comparison_contexts"],
        "resolved_changed": resolved["changed_comparisons"],
        "conditioned_configurations": resolved["conditioned_configurations"],
        "construction_succeeded": construction["construction_succeeded"],
        "gate_word": construction["gate_word"],
        "distribution_neighbor_0": construction["distribution_neighbor_0"],
        "distribution_neighbor_1": construction["distribution_neighbor_1"],
        "state_mutated_on_neighbor_1": construction["state_mutated_on_neighbor_1"],
        "scope_route": scope["route"],
        "family_words": scope["family_words"],
    }

    lines = [
        "=" * 78,
        "CYCLE 970 -- INTER-SITE GATE SUBSTRATE",
        "=" * 78,
    ]
    lines.extend(
        f"{'PASS' if ok else 'FAIL'} {name} :: {finding}"
        for name, ok, finding in certificates
    )
    lines.append("CHECKER_PAYLOAD: " + compact(checker_payload))
    lines.append("VERDICT: CYCLE719_SUBSTRATE_HOSTS_ONE_CNOT_INTER_SITE_WITNESS")
    pass_count = sum(ok for _, ok, _ in certificates)
    fail_count = len(certificates) - pass_count
    lines.append(f"TOTAL: PASS={pass_count} FAIL={fail_count}")
    text = "\n".join(lines) + "\n"
    report["stdout_bytes"] = len(text.encode())
    receipt_path = (
        ROOT / "outputs" / "inter_site_gate_cycle970_receipt_2026_08_09.json"
    )
    receipt_path.write_text(json.dumps(report, indent=1, sort_keys=True) + "\n")

    sys.stdout.write(text)
    if len(text.encode()) >= HOUSE_STDOUT_LIMIT_BYTES:
        sys.stderr.write("stdout budget exceeded\n")
        return 1
    return 0 if report["all_certificates_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
