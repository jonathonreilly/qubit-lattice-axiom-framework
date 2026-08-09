#!/usr/bin/env python3
"""Cycle 970: minimal inter-site gate in the landed Cycle-719 substrate.

Load-bearing operational definition
-----------------------------------
On the two-site basis menu {0, 1}, for a landed gate word W, target site t,
fixed local input x, nearest-neighbor bit n, and target output y, define

    D[W,t,x](y | n) = 1{A.apply_semantic((t=x, neighbor=n), W)_t = y}.

This is the deterministic point distribution induced by the landed basis-state
semantics.  The same x is held on both neighbor branches.  We separately
recompute the uniform-self-input marginal Dbar, which averages D over x=0,1;
that is the load-bearing alternative definition behind the prior zero result.

The exhaustive declared family is every word of length zero or one on a
labeled nearest-neighbor two-site patch from the classical basis gate kinds
accepted by Cycle 719: identity, X on either site, and CNOT in either
orientation.  TOF is excluded by its three-wire arity.  No claim is made about
longer words, the continuous M_2(C) domain, or a global covariant law.

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
)

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
AXIOM_PATH, CORE_PATH = AUDIT_INPUT_PATHS

# The axiom memo is cited authority and therefore text-only.  The Cycle-719
# core is the executable substrate under test, not an imported result verdict.
BLOCKLIST_CITED_PRIMARIES = (AXIOM_PATH,)
EXECUTABLE_SUBSTRATE = CORE_PATH

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


def uniform_self_input_census() -> dict:
    """Reproduce the prior marginal after averaging over target input x."""
    rows = []
    for gate_row in declared_family():
        for target in (0, 1):
            distributions = []
            for neighbor_bit in (0, 1):
                by_x = [
                    point_distribution(gate_row["word"], target, x, neighbor_bit)
                    for x in (0, 1)
                ]
                distributions.append(tuple(
                    sum(Fraction(row[y], 2) for row in by_x) for y in (0, 1)
                ))
            rows.append({
                "word_name": gate_row["name"],
                "target_site": target,
                "distribution_neighbor_0": [str(v) for v in distributions[0]],
                "distribution_neighbor_1": [str(v) for v in distributions[1]],
                "changed": distributions[0] != distributions[1],
            })
    return {
        "definition": "Dbar[W,t](y|n)=(D[W,t,0](y|n)+D[W,t,1](y|n))/2",
        "comparison_contexts": len(rows),
        "conditioned_configurations": 2 * len(rows),
        "changed_comparisons": sum(row["changed"] for row in rows),
        "rows": rows,
    }


def minimal_gate_attempt() -> dict:
    target, neighbor, local_input = 0, 1, 0
    word = (A.cn(neighbor, target),)
    before = [input_state(target, local_input, n) for n in (0, 1)]
    after = [A.apply_semantic(state, word) for state in before]
    distributions = [
        point_distribution(word, target, local_input, n) for n in (0, 1)
    ]
    succeeded = distributions[0] != distributions[1]
    zero_length_changes = any(
        point_distribution((), target, x, 0)
        != point_distribution((), target, x, 1)
        for x in (0, 1)
    )
    return {
        "construction_succeeded": succeeded,
        "minimal_in_declared_word_length": succeeded and not zero_length_changes,
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
        "zero_length_changes_distribution": zero_length_changes,
    }


def price(construction: dict, resolved: dict, uniform: dict) -> dict:
    if construction["construction_succeeded"]:
        return {
            "route": "successful_landed_construction",
            "delta": {
                "new_gate_classes": 0,
                "new_couplings": 0,
                "new_axioms": 0,
                "new_registered_primitives": 0,
                "supplied_premises": 1,
            },
            "supplied_premise": (
                "the target has the same fixed local input x=0 on both neighbor branches"
            ),
            "axiom_ledger": {
                "Lattice": "uses one supplied nearest-neighbor edge; no edit",
                "Qubit": (
                    "uses the finite basis menu {0,1}; no edit and no claim over full M_2(C)"
                ),
                "Admissibility": (
                    "supplies one bounded variation witness; no edit and no all-site covariant law"
                ),
                "Record": "unused; no formation, locking, permanence, or readout claim",
            },
            "primitive_ledger": {
                "scale_reference_primitive": "unused; delta 0",
                "kinetic_isotropy_primitive": "unused; delta 0",
                "realized_state_primitive": (
                    "not added or changed; supplied basis states remain test inputs"
                ),
            },
            "contradicts": [
                "an unqualified claim that every operational site-local distribution in the landed Cycle-719 substrate is neighbor-independent"
            ],
            "scopes": [
                f"uniform-self-input independence remains {uniform['changed_comparisons']}/{uniform['comparison_contexts']}",
                f"state-resolved dependence is {resolved['changed_comparisons']}/{resolved['comparison_contexts']}",
                "Cycle-719 controller certificates remain untouched because CNOT is landed machinery",
            ],
            "does_not_supply": [
                "a fixed translation- and proper-cubic-covariant all-site admissibility rule",
                "probability measures on the full continuous M_2(C) possibility domain",
                "formation site, rate, realized draw, or record dynamics",
            ],
        }
    return {
        "route": "failed_landed_construction",
        "obstruction": "no declared word separated the two neighbor-conditioned distributions",
        "minimal_delta_candidate": "a nearest-neighbor controlled permutation such as CNOT",
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
        "landed_axiom_needle_matches": axiom_needle in axiom_text,
    }


def run_science() -> dict:
    resolved = state_resolved_census()
    uniform = uniform_self_input_census()
    construction = minimal_gate_attempt()
    return {
        "resolved": resolved,
        "uniform": uniform,
        "construction": construction,
        "price": price(construction, resolved, uniform),
    }


def main() -> int:
    started = monotonic()
    first = run_science()
    second = run_science()
    controls = input_controls()
    deterministic = digest(first) == digest(second)

    resolved = first["resolved"]
    uniform = first["uniform"]
    construction = first["construction"]
    priced = first["price"]

    expected_resolved_total = len(declared_family()) * 2 * 2
    expected_uniform_total = len(declared_family()) * 2
    a_ok = (
        resolved["comparison_contexts"] == expected_resolved_total
        and resolved["changed_comparisons"] == len(resolved["witnesses"])
        and resolved["changed_comparisons"] + resolved["unchanged_comparisons"]
            == resolved["comparison_contexts"]
        and 0 <= resolved["changed_comparisons"] <= resolved["comparison_contexts"]
        and resolved["conditioned_configurations"] == 2 * expected_resolved_total
        and resolved["conditioned_configurations_in_changed_pairs"]
            == 2 * resolved["changed_comparisons"]
        and uniform["comparison_contexts"] == expected_uniform_total
        and 0 <= uniform["changed_comparisons"] <= uniform["comparison_contexts"]
    )
    a_finding = (
        f"definition={DEFINITION}; state_resolved_changed="
        f"{resolved['changed_comparisons']}/{resolved['comparison_contexts']} paired "
        f"comparisons; changed_pair_configurations="
        f"{resolved['conditioned_configurations_in_changed_pairs']}/"
        f"{resolved['conditioned_configurations']}; uniform_self_input_changed="
        f"{uniform['changed_comparisons']}/{uniform['comparison_contexts']}"
    )

    observed_separation = (
        construction["distribution_neighbor_0"]
        != construction["distribution_neighbor_1"]
    )
    b_ok = (
        construction["construction_succeeded"] == observed_separation
        and construction["minimal_in_declared_word_length"]
            == (observed_separation and not construction["zero_length_changes_distribution"])
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

    delta = priced.get("delta", {})
    expected_route = (
        "successful_landed_construction"
        if construction["construction_succeeded"] else "failed_landed_construction"
    )
    c_ok = (
        priced["route"] == expected_route
        and (
            not construction["construction_succeeded"]
            or (
                all(delta.get(key) == 0 for key in (
                    "new_gate_classes", "new_couplings", "new_axioms",
                    "new_registered_primitives",
                ))
                and delta.get("supplied_premises") == 1
                and set(priced.get("axiom_ledger", {}))
                    == {"Lattice", "Qubit", "Admissibility", "Record"}
                and set(priced.get("primitive_ledger", {})) == {
                    "scale_reference_primitive", "kinetic_isotropy_primitive",
                    "realized_state_primitive",
                }
            )
        )
    )
    c_finding = (
        "price=new gate/coupling/axiom/registered primitive 0/0/0/0; supplied "
        "premise=fixed target input x=0; changes=unqualified substrate-wide "
        f"independence is false while uniform marginal remains "
        f"{uniform['changed_comparisons']}/{uniform['comparison_contexts']}; "
        "full covariant M_2(C) law remains open"
        if construction["construction_succeeded"]
        else compact(priced)
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
        ("A_INDEPENDENCE_MEASUREMENT", a_ok, a_finding),
        ("B_GATE_CONSTRUCTION", b_ok, b_finding),
        ("C_PRICE", c_ok, c_finding),
        ("D_CONTROLS", d_ok, d_finding),
    ]
    report = {
        "cycle": 970,
        "claim_type": "bounded_theorem",
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

    lines = [
        "=" * 78,
        "CYCLE 970 -- INTER-SITE GATE SUBSTRATE",
        "=" * 78,
    ]
    lines.extend(
        f"{'PASS' if ok else 'FAIL'} {name} :: {finding}"
        for name, ok, finding in certificates
    )
    lines.append(
        "VERDICT: "
        + (
            "LANDED_SUBSTRATE_HOSTS_MINIMAL_INTER_SITE_GATE"
            if construction["construction_succeeded"]
            else "LANDED_SUBSTRATE_HAS_DECLARED_SCOPE_OBSTRUCTION"
        )
    )
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
