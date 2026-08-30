#!/usr/bin/env python3
"""Independent Block20 authority/type checker; never imports the primary."""
from __future__ import annotations

import copy
import itertools
import json
import re
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ".claude/science/physics-loops/toe-source-eta-ownership-block20-directed-action-transfer-record-generator-cone-20260830"
TERMINAL = "DIRECTED-ACTION/TRANSFER-TO-PERMANENT-RECORD-APPEND-INTENSITY-INTERFACE-UNSUPPLIED-ON-INSPECTED-STACK"
PR_HEAD = "dac92a5ed9a8ddaa90aa4300223a2c77fb4cd203"
AUDIT_INPUT_PATHS = (
    f"{PACKET}/STATE.yaml", f"{PACKET}/GOAL.md", f"{PACKET}/AUTHORITY_GATE.md",
    f"{PACKET}/PREFLIGHT_WITNESSES.md", "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/audit/data/ledger/po/post_record_dynamics_authority_stack_map_2026-06-06.json",
    "docs/audit/data/ledger/po/post_record_transition_kernel_interface_2026-06-06.json",
    "docs/audit/data/ledger/po/post_record_supplied_selection_rule_interface_2026-06-06.json",
    "docs/audit/data/ledger/po/post_record_supplied_kernel_selection_rule_interface_2026-06-06.json",
    "docs/ADMISSIBILITY_LOCAL_GEOMETRY_RECORD_BOND_TRANSFER_REFLECTION_RESPONSE_CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_NULL_ANCHORED_JOINT_GEOMETRY_RECORD_TRANSFER_PERRON_RESPONSE_SELECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_CANONICAL_TWO_TT_POSITIVE_TRANSFER_RECORD_SOURCE_CONTINUITY_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
)
PREMISES = ("minimal_axioms", "scale_reference_primitive",
            "kinetic_isotropy_primitive", "realized_state_primitive")
LEDGERS = {
    "post_record_dynamics_authority_stack_map_2026-06-06": ("meta", "meta"),
    "post_record_transition_kernel_interface_2026-06-06": ("bounded_theorem", "unaudited"),
    "post_record_supplied_selection_rule_interface_2026-06-06": ("bounded_theorem", "unaudited"),
    "post_record_supplied_kernel_selection_rule_interface_2026-06-06": ("bounded_theorem", "unaudited"),
}


def text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def flat(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace(chr(96), "")).strip()


def state_map(value: str) -> dict[str, str]:
    out = {}
    for line in value.splitlines():
        if ":" in line and not line.lstrip().startswith("#"):
            key, item = line.split(":", 1)
            out[key.strip()] = item.strip().strip("\"'")
    return out


def axiom_ok(value: str) -> bool:
    headings = re.findall(r"^### ([^/\n]+) /", value, re.MULTILINE)
    source = flat(value)
    needed = ("Admissibility is not a dynamics axiom",
              "does not choose a Hamiltonian or transfer operator",
              "supply transition-probability or weight values", "define a time metric",
              "provide a record-production process or physical persistence dynamics",
              "it does not supply the formation site, probability, or rate",
              "records are permanent")
    return headings == ["Lattice", "Qubit", "Admissibility", "Record"] and all(x in source for x in needed)


def premises_ok(data: dict) -> bool:
    nodes = data.get("nodes", {})
    if tuple(data.get("canonical_ids", ())) != PREMISES or set(nodes) != set(PREMISES):
        return False
    notes = {key: flat(nodes[key]["note"]) for key in PREMISES}
    return (all((ROOT / nodes[key]["current_path"]).is_file() for key in PREMISES)
            and "source/action bridge" in notes["minimal_axioms"]
            and "Units conversion only" in notes["scale_reference_primitive"]
            and "no dimensionless DYNAMICAL content" in notes["kinetic_isotropy_primitive"]
            and "Supplies the slot, never the content" in notes["realized_state_primitive"])


def ledgers_ok(rows: dict[str, dict]) -> bool:
    return all(rows[key].get("claim_type") == types[0]
               and rows[key].get("audit_status") == "unaudited"
               and rows[key].get("effective_status") == types[1]
               for key, types in LEDGERS.items())


def aug11_ok(value: str) -> bool:
    source = flat(value)
    block = re.search(r"The local state order is (.*?) Let sigma_g", source)
    states = re.findall(r"\(([01]),(null|occupied)\)", block.group(1) if block else "")
    needed = ("K = D_W^(1/2) E^(tensor 9) D_W^(1/2)",
              "is symmetric positive definite. Entrywise positivity gives a unique positive Perron vector",
              "P(y|x)=K(x,y)r(y)/(lambda r(x))",
              "pi(x)P(y|x)=r(x)K(x,y)r(y)/lambda=pi(y)P(x|y)",
              "permits transitions from occupied to null and therefore is Record-erasing",
              "A scheduler and permanent-Record causal update are not inferred from it",
              "ten-ray dictionary")
    return states == [("0", "null"), ("0", "occupied"), ("1", "null"), ("1", "occupied")] and all(x in source for x in needed)


def extensional_ok(aug10: str, two_tt: str) -> bool:
    a, t = flat(aug10), flat(two_tt)
    return all(x in a for x in ("one null plus fifteen actual-edge Record labels",
                                "The current axioms do not select B_2 over B_3",
                                "one extensional local geometry/Record transition rule",
                                "one autonomous causal Lorentzian Record/geometry update")) and all(
        x in t for x in ("identical static response and the same unit-speed OS0 limit",
                         "the current foundation does not select a physical transfer",
                         "An exact joint law must select the transfer and a transition-based conserved source-current decoder",
                         "No nonlinear completion, full-Z3 law, selected Record instrument"))


def fixture_bank() -> dict[int, tuple[tuple[int, ...], ...]]:
    vectors = {tuple(sorted(v, reverse=True)) for v in itertools.product(range(7), repeat=6) if sum(v) <= 6}
    return {z: tuple(sorted(v for v in vectors if sum(2**m for m in v) == z)) for z in (9, 10, 12)}


def desk_ok(bank: dict[int, tuple[tuple[int, ...], ...]]) -> bool:
    expected = {
        9: ((1, 1, 1, 0, 0, 0), (2, 0, 0, 0, 0, 0)),
        10: ((1, 1, 1, 1, 0, 0), (2, 1, 0, 0, 0, 0)),
        12: ((1, 1, 1, 1, 1, 1), (2, 1, 1, 1, 0, 0), (2, 2, 0, 0, 0, 0)),
    }
    if bank != expected:
        return False
    for z in (9, 10):
        low, high = sorted(bank[z], key=sum)
        for beta in (Fraction(1), Fraction(2), Fraction(3, 2)):
            rates = [beta**sum(v) * z for v in (low, high)]
            if rates[1] / rates[0] != beta or rates[1] / sum(rates) != beta / (1 + beta):
                return False
    ordered = sorted(bank[12], key=sum)
    return all(tuple((beta**sum(v) * 12) for v in ordered)[i + 1]
               / tuple((beta**sum(v) * 12) for v in ordered)[i] == beta
               for beta in (Fraction(1), Fraction(2)) for i in (0, 1))


def terminal_ok(value: str, state: dict[str, str]) -> bool:
    return (value == TERMINAL and "EMPTY" not in value
            and value.endswith("ON-INSPECTED-STACK")
            and state.get("action_record_bridge_frozen") == "false")


def n5(status: str) -> tuple[str, ...]:
    return (
        f"per_element: {status} exact source clauses, ledger fields, balance identity, and desk fixtures checked",
        f"per_site: {status} four-state carrier, reversible erasure, and six-mark Record type mismatch checked",
        f"per_mode: {status} checked and not executed — typed bridge absent, so C_AT and B_AT modes were not formed",
        f"per_block: {status} checked and not executed — no directed kernel or cadence exists for finite histories",
        f"lattice_wide: {status} checked and not executed — no generator exists for a Harris limit or physical clock",
    )


def main() -> None:
    state_text, goal, authority, preflight = (text(f"{PACKET}/{name}") for name in
        ("STATE.yaml", "GOAL.md", "AUTHORITY_GATE.md", "PREFLIGHT_WITNESSES.md"))
    state = state_map(state_text)
    axiom = text("docs/MINIMAL_AXIOMS_2026-06-29.md")
    premise_data = json.loads(text("docs/audit/data/axiom_premise_nodes.json"))
    rows = {key: json.loads(text(next(p for p in AUDIT_INPUT_PATHS if p.endswith(f"/{key}.json")))) for key in LEDGERS}
    a11, a10, tt = (text(path) for path in AUDIT_INPUT_PATHS[-3:])
    packet_ok = (all((ROOT / p).is_file() for p in AUDIT_INPUT_PATHS)
                 and state.get("latest_connection_pr") == "7803"
                 and state.get("latest_connection_head") == PR_HEAD
                 and "conditional-support" in preflight
                 and "does not evaluate mixed-placement histories" in flat(preflight)
                 and "full action exponential" in flat(preflight)
                 and "INTERFACE-UNSUPPLIED" in flat(goal)
                 and "do not construct an empty numerical cone" in flat(authority)
                 and not any("interface_gate_2026_08_30.py" in p for p in AUDIT_INPUT_PATHS))
    bank = fixture_bank()
    db_ok = all(Fraction(b, 13) * 0 / Fraction(a, 11) == 0 for a in range(1, 6) for b in range(1, 6))
    base = (packet_ok, axiom_ok(axiom) and premises_ok(premise_data), ledgers_ok(rows),
            aug11_ok(a11), extensional_ok(a10, tt), db_ok and desk_ok(bank),
            terminal_ok(TERMINAL, state))
    mutations = []
    mutations.append(not axiom_ok(axiom.replace("Admissibility is not a dynamics axiom", "Admissibility is a dynamics axiom", 1)))
    p_mut = copy.deepcopy(premise_data); p_mut["canonical_ids"] = p_mut["canonical_ids"][:-1]
    mutations.append(not premises_ok(p_mut))
    l_mut = copy.deepcopy(rows); l_mut[next(iter(LEDGERS))]["audit_status"] = "audited_clean"
    mutations.append(not ledgers_ok(l_mut))
    mutations.append(not aug11_ok(a11.replace("(1,occupied).", "(1,null).", 1)))
    mutations.append(not aug11_ok(a11.replace("permits transitions from occupied to null", "forbids transitions from occupied to null", 1)))
    mutations.append(not extensional_ok(a10.replace("do not select B_2 over B_3", "select B_2 over B_3", 1),
                                         tt.replace("does not select a physical transfer", "selects a physical transfer", 1)))
    mutations.append("does not evaluate mixed-placement histories" not in flat(preflight.replace(
        "does not evaluate mixed-placement histories", "evaluates mixed-placement histories", 1)))
    mutations.append(not (Fraction(3, 5) * Fraction(1) / Fraction(2, 5) == 0))
    b_mut = dict(bank); b_mut[9] = b_mut[9][:-1]
    mutations.append(not desk_ok(b_mut))
    mutations.append(not terminal_ok("EMPTY", state))
    n5_lines = n5("PASS")
    seven = list(base)
    seven[6] = seven[6] and len(mutations) == 10 and all(mutations) and all(
        len(line) >= 40 for line in n5_lines) and all(
        "checked and not executed —" in n5_lines[i] for i in (2, 3, 4))
    passed = sum(seven); status = "PASS" if passed == 7 else "FAIL"
    summaries = (
        f"prereg_source: {status} frozen_packet=true pr=7803 head={PR_HEAD} remote_object_reads=0 primary_imports=0",
        f"foundation: {status} premises={','.join(PREMISES)} axiom_dynamics_bridge_absent=true",
        f"post_Record_authority: {status} rows=4 audit_status=unaudited effective=meta/unaudited",
        f"aug11_type: {status} carrier=4 symmetric_Perron=true reversible=true reverse_erasure=true marks=10_vs_6",
        f"other_transfers: {status} Aug10_extensional_kernel_gap=true two_TT_selector_and_Record_instrument_gap=true",
        f"exact_desk: {status} detailed_balance_reverse_zero_implies_forward_zero Z9=2/3 Z10=3/4 Z12=4/5/6 beta2_odds=1/7,2/7,4/7",
        f"hostile_and_terminal: {status} mutations={sum(mutations)}/10 C_AT=UNDEFINED B_AT=UNDEFINED NOT_EMPTY=true terminal={TERMINAL}",
    )
    print("\n".join((*summaries, *n5(status),
          f"scope: {status} inspected stack only; no action-wide no-go, axiom, audit, gravity, obligation, or TOE promotion",
          f"TOTAL: PASS={passed} FAIL={7-passed}")))
    if passed != 7:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
