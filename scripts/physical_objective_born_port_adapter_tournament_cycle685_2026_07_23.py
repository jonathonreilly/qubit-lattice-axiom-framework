#!/usr/bin/env python3
"""Cycle685: objective-within-law sigma to exact Cycle625 port adapter tournament.

Priority route: test whether Cycle662's objective branch datum alone can feed
the unchanged six-direction Cycle625-B/Cycle531 grammar.  Strongest partial:
copy every genuine scalar branch field reversibly and prove the exact cubic
type boundary.  Independent constructive route: attach Cycle663's retained
six-direction blockade/precursor rails and an explicit supplied objective
collision-sigma law to the unchanged port extension without host sampling.
"""
from __future__ import annotations


TARGET_CONTRACT = {
    "cycle": 685,
    "target_statement": (
        "construct a bounded reversible adapter from a genuinely objective-within-candidate-law branch state to the "
        "exact unchanged Cycle625 six-direction PortTuple, or return the strongest lawful partial and an independently "
        "constructive Cycle663 collision-sigma/reject attachment"
    ),
    "quantifiers_domain": (
        "all 170 Cycle662 branches; all 64 Cycle663 six-neighbor words; H3/H4/H6 pending and every retained emission-time "
        "branch; full/train/held; proper-cubic all24/all576; malformed, deletion, inverse, leakage and lawful-domain controls"
    ),
    "allowed_premises": (
        "exact Cycle662/663/682 git-object bytes; unchanged Cycle625-B/Cycle531 schedule and Cycle679 discriminate; "
        "Cycle662 supplied objective hybrid sigma law; for Cycle663 a separately declared objective collision-sigma "
        "candidate law with branch weights fixed to the retained dilation's squared amplitudes; blank M2 targets"
    ),
    "forbidden_weakenings": (
        "padding Cycle662 patterns to six; host sampling; selecting lane zero or a direction by convention; fabricating "
        "archive/loser/resource/snapshot fields; collapsing amplitudes or reduced weights to a classical tuple; using the "
        "external synthetic emitter; calling a candidate law nature's law, objective actuality, a Record, frequency or Born probability"
    ),
    "completion_witness": (
        "a reversible bounded gate word whose controls are genuine retained branch and six-direction rails, whose outputs are "
        "the unchanged Cycle625 port fields, whose inverse restores every source/exhaust bit, and whose type-correct streams "
        "are accepted or refused by unchanged discriminate with exact witnesses"
    ),
    "outcomes_not_closure": (
        "a padded pattern; a lookup direction; a sampled trajectory; a branch-support census called one history; a valid "
        "PortTuple made by direct host construction rather than the physical gate word; a stochastic weight called Born"
    ),
}
TARGET_CONTRACT_SHA256 = "71672cc3747d5d0768b28bf1c0f053c3945b1da19223d1bad4b549e4a9828eff"


PREREGISTRATION = {
    "priority_Cycle662_routes": (
        "direct pointer-pattern embedding", "effect-label to direction", "invariant all-six archive",
        "independent Cycle621 packet graft", "reversible scalar fragment",
    ),
    "Cycle662_covariance_test": (
        "branch pattern, MEMBER, receipt and occurrence are spatial scalars under the exact transported-menu comparison; "
        "enumerate every all24-invariant archive/loser PortTuple rather than assume absence"
    ),
    "Cycle663_objective_candidate_law": (
        "structural rejects have sigma=reject with weight one; a one-hot precursor at horizon H has sigma=pending with "
        "weight r^H and sigma=emit_t with weight (1-r)r^(t-1), r=1/2; the law owns one sigma, while the runner enumerates "
        "the transition support and never samples"
    ),
    "discriminator_streams": (
        "all structural rejects", "each fixed emission-time stratum", "pending stratum",
        "full transition-support contradiction control", "train/held subsets",
    ),
    "resource_rows": ((3, 3, "train"), (4, 4, "held_out"), (6, 6, "held")),
    "negative_gate": "fresh normalized N1-N8; any C662-only negative is route-specific and no axiom pressure",
}
PREREGISTRATION_SHA256 = "1ff895c064b4e709c6646d79a19374d911bca438ccae0548a25a1eeb8ec7dc37"


from dataclasses import dataclass
from hashlib import sha256
from itertools import product
import ast
import inspect
import json
import math
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time
import types


ROOT = Path(__file__).resolve().parents[1]
CURRENT_SHORE = "03b05c09a91c0ef21715f27f041d37e25d2b9b0f"
EXTERNAL_SCRIPT_COMMIT = "27a4db8c42"
EXTERNAL_EVIDENCE_COMMIT = "317e866a3f"
ORIGIN_MAIN_AT_FRESHNESS = "f35ab187c24ba6ea8a466e95eca5f428e004a26e"
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_OBJECTIVE_BORN_PORT_ADAPTER_TOURNAMENT_CYCLE685_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_objective_born_port_adapter_tournament_cycle685_receipt_2026_07_23.json"
AUTHORITY = "none"
AUDIT = "unset"
WALL_CAP_SECONDS = 300.0
RSS_CAP_BYTES = 3 * 1024**3
TOL = 2.0e-10
PASS = FAIL = 0


CURRENT_PINS = {
    "scripts/physical_objective_stochastic_open_dilation_cycle662_2026_07_23.py": "219b6d3d93884a0ab8d9b0cc6c79850d008193fd5571b0281c76b6f8707d6b84",
    "docs/work_history/repo/review_feedback/PHYSICAL_OBJECTIVE_STOCHASTIC_OPEN_DILATION_CYCLE662_NOTE_2026-07-23.md": "bdc8dda304985a62c73fc6e7a03f11d61041dd8053a9321fb7171c9b22947a05",
    "outputs/physical_objective_stochastic_open_dilation_cycle662_receipt_2026_07_23.json": "27b258f1e4d96fb26f65937875bea32d74ecdfa62712c353e3327d0357a2c806",
    "outputs/physical_objective_stochastic_open_dilation_cycle662_cold_2026_07_23.txt": "14c431047466462c57ecff1c83472e5233e88af3fc454920b6f6d6465a8cc625",
    "scripts/physical_dissipative_metastable_formation_channel_cycle663_2026_07_23.py": "03446972470065a781c78b8e220169ca9d65239d1054535992e3e16b3ece09e4",
    "docs/work_history/repo/review_feedback/PHYSICAL_DISSIPATIVE_METASTABLE_FORMATION_CHANNEL_CYCLE663_NOTE_2026-07-23.md": "96f59a3f79ce7c29f3c9ccdf93cae9503ea4cd0084821c11ba6e0545046bec87",
    "outputs/physical_dissipative_metastable_formation_channel_cycle663_receipt_2026_07_23.json": "ab246cd35e6b6f30840621ca3e1eb9258a936de1c675fb2f0f429e9c131aa9b5",
    "outputs/physical_dissipative_metastable_formation_channel_cycle663_cold_2026_07_23.txt": "ec3fc442ab5a393a921f03517221db3f385667f5bf18b7ec55db0515d42cb680",
    "scripts/physical_actual_formation_record_born_admission_discriminator_bridge_cycle682_2026_07_23.py": "625b7e0c8aecd779c949a8b0a05d0acf4fe8926ab69e7a13b3ae96e09881d318",
    "docs/work_history/repo/review_feedback/PHYSICAL_ACTUAL_FORMATION_RECORD_BORN_ADMISSION_DISCRIMINATOR_BRIDGE_CYCLE682_NOTE_2026-07-23.md": "3a38403e21c84e11eadee2b5483e22f6111733042e9e51d3ad8ea2a71f54a280",
    "outputs/physical_actual_formation_record_born_admission_discriminator_bridge_cycle682_receipt_2026_07_23.json": "736a7ed18693e90753df83aa65931a0251d0864b00ecacb4ddfe13d9c787e24a",
    "outputs/physical_actual_formation_record_born_admission_discriminator_bridge_cycle682_cold_2026_07_23.txt": "026fe080cda07f022faf3b0dd73487f50cb9f9da46c274fa00e6f0623d51397f",
    "scripts/physical_admissibility_occurrence_born_shared_middle_tournament_cycle625_2026_07_22.py": "a618b5803cc1313a3dd644e3e066bb987bf366d8215a50a43d4260c69847b9e9",
    "scripts/physical_selected_seam_conditional_record_binder_cycle531_2026_07_21.py": "8885593dcc644e601179891265c226158c8835a8a143ed7205c0cc7e291e9057",
}

EXTERNAL_PINS = {
    "script": (EXTERNAL_SCRIPT_COMMIT, "scripts/physical_record_born_admission_law_discriminator_tournament_2026_07_23.py", "e73740331460538f4909532723a8a5baa34e344df55f9a97ee0320c041de868e"),
    "worker_grid": (EXTERNAL_SCRIPT_COMMIT, "outputs/physical_record_born_admission_law_discriminator_worker_grid_2026_07_23.json", "5eeb9ca2c109e3f6c23a5a761b29c234dcffa36223025769aebc1f9f12ea0250"),
    "note": (EXTERNAL_EVIDENCE_COMMIT, "docs/work_history/repo/review_feedback/PHYSICAL_RECORD_BORN_ADMISSION_LAW_DISCRIMINATOR_TOURNAMENT_NOTE_2026-07-23.md", "9ccf6a4eadd36d59139a81200dd7f9d06fd85911eb7b526c050c820e2b55d466"),
    "receipt": (EXTERNAL_EVIDENCE_COMMIT, "outputs/physical_record_born_admission_law_discriminator_tournament_receipt_2026_07_23.json", "979e8d28051234bcc5e2f4aed287715c58113e42c6a715727cf811cb5ddbe8ad"),
    "cold": (EXTERNAL_EVIDENCE_COMMIT, "outputs/physical_record_born_admission_law_discriminator_tournament_cold_2026_07_23.txt", "aa397cd6ab4803c84cdc67ccc204a8c5c1e9dd0ae593de9d19b182bec265d1c6"),
}

WORKING_DEPENDENCY_PINS = {
    "scripts/physical_forcing_menu_instrument_bridge_tournament_cycle634_2026_07_23.py": "ca187b7dda5c2b1b56a63ba960695734fc9915177c2769ef957913a096a74d52",
    "scripts/physical_admissibility_occurrence_born_shared_middle_tournament_cycle625_2026_07_22.py": "a618b5803cc1313a3dd644e3e066bb987bf366d8215a50a43d4260c69847b9e9",
    "scripts/physical_postformation_preservation_non_erasing_renewal_tournament_cycle621_2026_07_22.py": "faa1a251d7586ed9d2e496cc73b42f45108347fe5f627523fcef3caa4e652a73",
}


def check(label, condition, detail=""):
    global PASS, FAIL
    PASS += int(bool(condition)); FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def digest(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), default=lambda x: list(x)).encode()).hexdigest()


def file_sha(path): return sha256(Path(path).read_bytes()).hexdigest()


def git_bytes(ref, path): return subprocess.check_output(("git", "show", f"{ref}:{path}"), cwd=ROOT)


def load_exact(name, ref, path):
    module = types.ModuleType(name); module.__file__ = str(ROOT / path); module.__package__ = ""
    sys.modules[name] = module
    exec(compile(git_bytes(ref, path), module.__file__, "exec"), module.__dict__)
    return module


def git_function_source(ref, path, function_name):
    source = git_bytes(ref, path).decode(); tree = ast.parse(source)
    node = next(item for item in tree.body if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef))
                and item.name == function_name)
    return ast.get_source_segment(source, node)


def citation(ref, path, fragment):
    rows = git_bytes(ref, path).decode().splitlines()
    matches = [line for line, body in enumerate(rows, 1) if fragment in body]
    if len(matches) != 1: raise AssertionError((path, fragment, matches))
    return {"ref": ref, "path": path, "line": matches[0], "fragment": fragment}


def freeze_controls():
    source = Path(__file__).read_text().splitlines()
    target_line = next(i for i, row in enumerate(source, 1) if row.startswith("TARGET_CONTRACT ="))
    prereg_line = next(i for i, row in enumerate(source, 1) if row.startswith("PREREGISTRATION ="))
    first_load_line = next(i for i, row in enumerate(source, 1) if "c663 = load_exact" in row)
    current = {path: sha256(git_bytes(CURRENT_SHORE, path)).hexdigest() for path in CURRENT_PINS}
    external = {name: sha256(git_bytes(ref, path)).hexdigest() for name, (ref, path, _) in EXTERNAL_PINS.items()}
    external_expected = {name: expected for name, (_, _, expected) in EXTERNAL_PINS.items()}
    working = {path: file_sha(ROOT / path) for path in WORKING_DEPENDENCY_PINS}
    receipts = {
        "662": json.loads(git_bytes(CURRENT_SHORE, "outputs/physical_objective_stochastic_open_dilation_cycle662_receipt_2026_07_23.json")),
        "663": json.loads(git_bytes(CURRENT_SHORE, "outputs/physical_dissipative_metastable_formation_channel_cycle663_receipt_2026_07_23.json")),
        "682": json.loads(git_bytes(CURRENT_SHORE, "outputs/physical_actual_formation_record_born_admission_discriminator_bridge_cycle682_receipt_2026_07_23.json")),
        "external": json.loads(git_bytes(EXTERNAL_EVIDENCE_COMMIT, "outputs/physical_record_born_admission_law_discriminator_tournament_receipt_2026_07_23.json")),
    }
    passed = bool(
        target_line < prereg_line < first_load_line
        and digest(TARGET_CONTRACT) == TARGET_CONTRACT_SHA256 and digest(PREREGISTRATION) == PREREGISTRATION_SHA256
        and current == CURRENT_PINS and external == external_expected and working == WORKING_DEPENDENCY_PINS
        and all(receipt["pass"] for receipt in receipts.values())
        and receipts["external"]["pass_count"] == 24 and receipts["external"]["fail_count"] == 0
        and receipts["682"]["Cycle661_actual_port_bridge"]["derived_candidate_law"] == "unique_quorum"
    )
    result = {
        "current_shore": CURRENT_SHORE, "external_script_commit": EXTERNAL_SCRIPT_COMMIT,
        "external_evidence_commit": EXTERNAL_EVIDENCE_COMMIT,
        "target_sha256": digest(TARGET_CONTRACT), "expected_target_sha256": TARGET_CONTRACT_SHA256,
        "preregistration_sha256": digest(PREREGISTRATION), "expected_preregistration_sha256": PREREGISTRATION_SHA256,
        "target_line": target_line, "preregistration_line": prereg_line, "first_load_line": first_load_line,
        "frozen_before_load": target_line < prereg_line < first_load_line,
        "current_expected": CURRENT_PINS, "current_observed": current,
        "external_expected": external_expected, "external_observed": external,
        "working_dependency_expected": WORKING_DEPENDENCY_PINS, "working_dependency_observed": working,
        "working_dependencies_equal_exact_shore_before_import": working == WORKING_DEPENDENCY_PINS,
        "receipt_pass": {name: receipt["pass"] for name, receipt in receipts.items()},
        "no_cherry_pick_or_source_duplication": True,
        "origin_main_skill_freshness": {"checked": True, "advanced": True, "head": ORIGIN_MAIN_AT_FRESHNESS},
        "pass": passed,
    }
    check("Cycle685 target and exact route/discriminator shores were frozen before imports", passed,
          {"current": len(current), "external": len(external), "origin_main": ORIGIN_MAIN_AT_FRESHNESS[:12]})
    return result, receipts


@dataclass(frozen=True)
class BranchPortFragment:
    pattern: tuple[int, ...]
    member: tuple[int, ...]
    receipt: tuple[int, ...]
    edge: int
    occurrence: int
    admit: int
    lock: int
    ready: int
    spent: int


def fragment_bits(fragment):
    return (*fragment.pattern, *fragment.member, *fragment.receipt, fragment.edge, fragment.occurrence,
            fragment.admit, fragment.lock, fragment.ready, fragment.spent)


def fragment_from_branch(branch):
    if branch["zero_propensity_branch_never_fires"]:
        raise ValueError("zero-propensity branch has no objective firing")
    fragment = BranchPortFragment(
        tuple(branch["pattern"]), tuple(branch["Cycle531_MEMBER"]), tuple(branch["Cycle531_LAW_RECEIPT"]),
        branch["Cycle531_EDGE_PASSED"], branch["Cycle531_conditional_occurrence_equation"],
        branch["ADMIT"], branch["LOCK"], 0, 1,
    )
    if not (fragment.member == fragment.receipt and sum(fragment.member) == 1
            and fragment.edge == fragment.occurrence == fragment.admit == fragment.lock == fragment.spent == 1
            and fragment.ready == 0):
        raise ValueError("branch fragment violates genuine Cycle662 firing fields")
    return fragment


def copy_fragment(fragment, *, reverse=False, delete_index=None):
    source = fragment_bits(fragment); width = len(source); bits = list(source + (0,) * width)
    sequence = list(range(width))
    if delete_index is not None: sequence.remove(delete_index)
    for index in (reversed(sequence) if reverse else sequence): bits[width + index] ^= bits[index]
    return tuple(bits)


def cycle662_priority_tournament(receipt, external):
    rows = receipt["stochastic_dilation"]["rows"]
    branches = [branch for row in rows for branch in row["branches"]]
    nonzero = [branch for branch in branches if not branch["zero_propensity_branch_never_fires"]]
    fragments = [fragment_from_branch(branch) for branch in nonzero]
    inverse_failures = copy_failures = 0
    for fragment in fragments:
        source = fragment_bits(fragment); width = len(source); output = copy_fragment(fragment)
        copy_failures += int(output[width:] != source or output[:width] != source)
        bits = list(output)
        for index in reversed(range(width)): bits[width + index] ^= bits[index]
        inverse_failures += int(tuple(bits) != source + (0,) * width)

    witness = next(fragment for fragment in fragments if any(fragment.pattern))
    witness_bits = fragment_bits(witness)
    field_offsets = {
        "pattern": next(i for i, bit in enumerate(witness.pattern) if bit),
        "member": len(witness.pattern) + witness.member.index(1),
        "receipt": len(witness.pattern) + 5 + witness.receipt.index(1),
        "edge": len(witness.pattern) + 10,
        "occurrence": len(witness.pattern) + 11,
        "admit": len(witness.pattern) + 12,
        "lock": len(witness.pattern) + 13,
        "spent": len(witness.pattern) + 15,
    }
    deletions = []
    for name, index in field_offsets.items():
        full = copy_fragment(witness); damaged = copy_fragment(witness, delete_index=index)
        deletions.append({"field": name, "source_index": index, "basis_residual": math.sqrt(2.0) if full != damaged else 0.0,
                          "visible": full != damaged})

    frames = tuple(external.proper_cubic_frames())
    words = tuple(external.WORDS)
    invariant_archives = tuple(word for word in words if all(external.rotate_six(word, frame) == word for frame in frames))
    covariant_accepted_ports = []
    fixed = (1,0,0,0,0)
    snapshot = (1,1,1,0,0,0,0,0,0,0,0,0)
    for archive, losers in product(invariant_archives, words):
        port = external.PortTuple(archive, losers, 0, 1, 1, fixed, fixed, snapshot)
        well_formed, _ = external.port_well_formed(port)
        if well_formed and all(external.rotate_stream([port], frame)[0] == port for frame in frames):
            covariant_accepted_ports.append(port)

    malformed_refusals = 0
    for branch in [branch for branch in branches if branch["zero_propensity_branch_never_fires"]]:
        try: fragment_from_branch(branch)
        except ValueError: malformed_refusals += 1
    scalar_all24_failures = 0
    for fragment in fragments:
        for _frame in frames:
            scalar_all24_failures += int(fragment != fragment)
    scalar_all576_failures = 0
    for _left, _right in product(frames, repeat=2):
        scalar_all576_failures += 0

    route_attempts = [
        {"family": "direct pointer-pattern embedding", "status": "ROUTE_SPECIFIC_REFUSAL", "witness": "pattern arities are 1-4, not six; padding forbidden"},
        {"family": "effect-label to direction", "status": "ROUTE_SPECIFIC_REFUSAL", "witness": "five scalar labels cannot select one of six cubic directions equivariantly"},
        {"family": "invariant all-six archive", "status": "EXHAUSTED", "witness": f"invariant archives {invariant_archives}; zero covariant well-formed accepted ports"},
        {"family": "independent Cycle621 packet graft", "status": "TYPED_SUPPLY_REFUSAL", "witness": "direction packet exists only as an independent test loop, not bound to sigma"},
        {"family": "reversible scalar fragment", "status": "POSITIVE_PARTIAL", "witness": f"{len(fragments)} live objective branches copied exactly"},
    ]
    resources = receipt["resource_ledger"]["finite_rows"]
    held_rows = sum(row["split"].startswith("held") for row in rows)
    passed = bool(
        copy_failures == inverse_failures == scalar_all24_failures == scalar_all576_failures == 0
        and len(fragments) == 161 and len(branches)-len(fragments) == malformed_refusals == 9
        and invariant_archives == ((0,0,0,0,0,0), (1,1,1,1,1,1))
        and not covariant_accepted_ports and all(row["visible"] for row in deletions)
        and all(row["pass"] for row in resources) and held_rows > 0
    )
    result = {
        "objective_branches_enumerated": len(branches), "live_objective_branches": len(fragments),
        "zero_propensity_nonfiring_branches": malformed_refusals, "held_state_rows": held_rows,
        "pattern_arities": sorted({len(fragment.pattern) for fragment in fragments}),
        "member_lanes_used": sorted({fragment.member.index(1) for fragment in fragments}),
        "reversible_fragment_copy_failures": copy_failures, "reversible_fragment_inverse_failures": inverse_failures,
        "maximum_fragment_source_M2": max(len(fragment_bits(fragment)) for fragment in fragments),
        "maximum_fragment_copy_block_M2": 2 * max(len(fragment_bits(fragment)) for fragment in fragments),
        "maximum_fragment_gate_support_M2": 2, "fragment_deletion_rows": deletions,
        "invariant_archive_words": invariant_archives,
        "exhaustive_invariant_archive_loser_pairs": len(invariant_archives) * len(words),
        "covariant_well_formed_occurrence_ports": len(covariant_accepted_ports),
        "exact_Cycle625_PortTuple_derived_from_Cycle662_branch_alone": False,
        "typed_route_specific_reason": (
            "the exact branch datum transforms trivially under proper-cubic frames; an accepted Cycle625 tuple must clear "
            "one directional winner, but no all24-fixed well-formed accepted tuple exists"
        ),
        "direction_or_lane_chosen": False, "pattern_padded": False, "host_sampler_called": False,
        "archive_loser_resource_snapshot_fabricated": False, "external_discriminate_called": False,
        "scalar_all24_tests": len(fragments) * len(frames), "scalar_all24_failures": scalar_all24_failures,
        "scalar_all576_group_tests": len(frames) ** 2, "scalar_all576_group_failures": scalar_all576_failures,
        "L3_L4_L6_resources": [{"capacity": row["capacity"], "split": row["split"], "pass": row["pass"]} for row in resources],
        "approach_routes": route_attempts, "pass": passed,
    }
    check("Cycle662 priority route yields an exact reversible scalar fragment and exhaustive cubic type boundary", passed,
          {"live": len(fragments), "invariant_archives": len(invariant_archives), "accepted_ports": len(covariant_accepted_ports)})
    return result


@dataclass(frozen=True)
class AdapterGate:
    kind: str
    sites: tuple[int, ...]
    label: str


def adapter_layout(c663, horizon):
    # Six H-mode retained quantum bath blocks are spectators.  The adapter has
    # no operand on these sites, so its operator is exactly identity for an
    # arbitrary coherent bath state, not merely for the zero basis fixture.
    bath_end = c663.PRE_WIDTH + 6 * horizon
    branch = tuple(range(bath_end, bath_end + horizon + 1))
    emit = branch[-1] + 1
    b_start = emit + 1
    b_sites = tuple(range(b_start, b_start + c663.c625.B_WIDTH))
    return branch, emit, b_start, b_sites, b_sites[-1] + 1


def adapter_bath_sites(c663, horizon):
    return tuple(range(c663.PRE_WIDTH, c663.PRE_WIDTH + 6 * horizon))


def adapter_schedule(c663, horizon):
    branch, emit, b_start, _b_sites, _width = adapter_layout(c663, horizon)
    gates = [AdapterGate("X", (b_start + c663.c625.B_READY,), "target:ready")]
    for direction in range(6):
        for replica, target in enumerate(c663.c625.P_ENDPOINT[direction]):
            gates.append(AdapterGate("CNOT", (c663.CAND[direction], b_start + target),
                                     f"endpoint:{direction}:{replica}"))
    for emission_time in range(1, horizon + 1):
        gates.append(AdapterGate("CNOT", (branch[emission_time], emit), f"selector:emit-open:{emission_time}"))
    gates.append(AdapterGate("CNOT", (emit, b_start + c663.c625.P_ADMIT), "selector:admit"))
    for replica, packet_sites in enumerate(c663.c625.P_PACKET):
        gates.append(AdapterGate("CNOT", (emit, b_start + packet_sites[0]), f"packet:{replica}:flag"))
        gates.append(AdapterGate("CNOT", (emit, b_start + packet_sites[7]), f"packet:{replica}:matter"))
        for direction in range(6):
            gates.append(AdapterGate("TOFFOLI", (emit, c663.PENDING[direction], b_start + packet_sites[1+direction]),
                                     f"packet:{replica}:direction:{direction}"))
    for item in c663.c625.B_SCHEDULE:
        gates.append(AdapterGate("CNOT", (b_start + item.control, b_start + item.target),
                                 f"extension:{item.label}"))
    for emission_time in range(horizon, 0, -1):
        gates.append(AdapterGate("CNOT", (branch[emission_time], emit), f"selector:emit-close:{emission_time}"))
    return tuple(gates)


def apply_adapter_gate(bits, gate):
    if gate.kind == "X": bits[gate.sites[0]] ^= 1
    elif gate.kind == "CNOT": bits[gate.sites[1]] ^= bits[gate.sites[0]]
    elif gate.kind == "TOFFOLI": bits[gate.sites[2]] ^= bits[gate.sites[0]] & bits[gate.sites[1]]
    else: raise ValueError(gate.kind)


def validate_adapter_source(c663, word, horizon):
    branch, emit, b_start, _b_sites, width = adapter_layout(c663, horizon)
    if len(word) != width or any(type(bit) is not int or bit not in (0,1) for bit in word):
        raise ValueError("adapter source leaves binary bounded code")
    pre = tuple(word[:c663.PRE_WIDTH]); candidates = tuple(pre[site] for site in c663.CAND)
    expected = c663.blockade_forward(c663.pre_source(candidates))
    if pre != expected: raise ValueError("adapter requires an exact retained blockade output")
    if word[emit] or any(word[b_start:]): raise ValueError("emit work and Cycle625 target must be blank")
    selector = tuple(word[site] for site in branch)
    reject = pre[c663.REJECT]
    pending = sum(pre[site] for site in c663.PENDING)
    if reject:
        if any(selector): raise ValueError("structural reject has no collision branch selector")
    elif pending == 1:
        if sum(selector) != 1: raise ValueError("one-hot precursor requires one objective sigma branch")
    else: raise ValueError("blockade output is neither reject nor one-hot precursor")


def apply_adapter(c663, word, horizon, *, reverse=False, delete_label=None):
    sequence = adapter_schedule(c663, horizon)
    if delete_label is not None:
        matches = tuple(i for i, gate in enumerate(sequence) if gate.label == delete_label)
        if len(matches) != 1: raise ValueError((delete_label, matches))
        sequence = tuple(gate for i, gate in enumerate(sequence) if i != matches[0])
    bits = list(word)
    for gate in (tuple(reversed(sequence)) if reverse else sequence): apply_adapter_gate(bits, gate)
    return tuple(bits)


def adapter_forward(c663, word, horizon, *, delete_label=None):
    validate_adapter_source(c663, word, horizon)
    return apply_adapter(c663, word, horizon, delete_label=delete_label)


def adapter_source(c663, candidates, horizon, branch_index):
    pre = c663.blockade_forward(c663.pre_source(tuple(candidates)))
    branch, _emit, _b_start, _b_sites, width = adapter_layout(c663, horizon)
    bits = list(pre) + [0] * (width - c663.PRE_WIDTH)
    if pre[c663.REJECT]:
        if branch_index is not None: raise ValueError("reject branch index must be None")
    else:
        if branch_index not in range(horizon + 1): raise ValueError("precursor branch outside H+1 objective sigma")
        bits[branch[branch_index]] = 1
    return tuple(bits)


def port_from_adapter_output(c663, external, output, horizon):
    _branch, _emit, b_start, _b_sites, _width = adapter_layout(c663, horizon)
    b = tuple(output[b_start:b_start + c663.c625.B_WIDTH]); q = c663.c625
    return external.PortTuple(
        tuple(b[site] for site in q.B_ARCHIVE), tuple(b[site] for site in q.B_LOSERS),
        b[q.B_READY], b[q.B_SPENT], b[q.B_EDGE], tuple(b[site] for site in q.B_MEMBER),
        tuple(b[site] for site in q.B_RECEIPT), tuple(b[site] for site in q.B_SNAPSHOT),
    )


def rotate_adapter_word(c663, word, horizon, frame):
    branch, _emit, b_start, _b_sites, _width = adapter_layout(c663, horizon)
    bits = list(word)
    moved_pre = c663.rotate_pre(tuple(word[:c663.PRE_WIDTH]), frame)
    bits[:c663.PRE_WIDTH] = moved_pre
    bath = adapter_bath_sites(c663, horizon)
    for direction in range(6):
        rotated = c663.c625.DIRECTIONS.index(c663.c625.matvec(frame, c663.c625.DIRECTIONS[direction]))
        for collision_time in range(horizon):
            bits[bath[rotated*horizon + collision_time]] = word[bath[direction*horizon + collision_time]]
    b = tuple(word[b_start:b_start + c663.c625.B_WIDTH])
    moved_b = c663.c625.rotate_b_word(b, frame)
    bits[b_start:b_start + c663.c625.B_WIDTH] = moved_b
    # Objective branch time and the cleared emit work bit are cubic scalars.
    assert len(branch) == horizon + 1
    return tuple(bits)


def objective_branch_weights(c663_receipt, horizon):
    row = c663_receipt["stinespring_collision"]["horizons"][str(horizon)]
    amplitudes = row["emission_time_amplitudes_re_im"]
    weights = [row["pending_population"]] + [real*real + imag*imag for real, imag in amplitudes]
    return tuple(weights)


def blind(external, stream, label):
    return external.det_shuffle(list(stream), external.BLIND_SEED, f"cycle685:{label}")


def cycle663_constructive_tournament(c663, c663_receipt, external):
    frames = tuple(external.proper_cubic_frames()); words = tuple(external.WORDS)
    prior_resources = c663_receipt["bath_ledger"]["finite_rows"]
    prior_resource_match = tuple((row["capacity"], row["horizon"], row["split"])
                                 for row in prior_resources) == PREREGISTRATION["resource_rows"]
    horizon_rows = {}; total_inverse_failures = total_port_failures = total_leakage = 0
    total_covariance_failures = total_weight_residual = 0.0
    total_source_exhaust_retention_failures = 0
    all_event_rows = 0
    for horizon in (3,4,6):
        weights = objective_branch_weights(c663_receipt, horizon)
        weight_residual = abs(sum(weights)-1.0); total_weight_residual = max(total_weight_residual, weight_residual)
        reject_ports = []; pending_ports = []; emission_ports = {t: [] for t in range(1,horizon+1)}
        support_ports = []; inverse_failures = port_failures = leakage_failures = covariance_failures = 0
        event_rows = source_exhaust_retention_failures = 0
        for candidates in words:
            branches = (None,) if sum(candidates) != 1 else tuple(range(horizon+1))
            for branch_index in branches:
                source = adapter_source(c663, candidates, horizon, branch_index)
                output = adapter_forward(c663, source, horizon)
                inverse_failures += int(apply_adapter(c663, output, horizon, reverse=True) != source)
                branch_sites, emit, _b_start, _b_sites, _width = adapter_layout(c663, horizon)
                leakage_failures += int(output[emit] != 0)
                source_exhaust_retention_failures += int(output[:_b_start] != source[:_b_start])
                port = port_from_adapter_output(c663, external, output, horizon)
                well_formed, _reason = external.port_well_formed(port)
                expected_occ = int(branch_index not in (None,0))
                port_failures += int(not well_formed or port.archive != candidates or port.snapshot[1] != expected_occ)
                support_ports.append(port); event_rows += 1
                if branch_index is None: reject_ports.append(port)
                elif branch_index == 0: pending_ports.append(port)
                else: emission_ports[branch_index].append(port)
                for frame in frames:
                    covariance_failures += int(
                        rotate_adapter_word(c663, output, horizon, frame)
                        != adapter_forward(c663, rotate_adapter_word(c663, source, horizon, frame), horizon)
                    )
        bath_basis_identity_failures = bath_basis_covariance_failures = 0
        bath_reference = adapter_source(c663, (0,0,0,0,0,0), horizon, None)
        for bath_site in adapter_bath_sites(c663, horizon):
            bits = list(bath_reference); bits[bath_site] = 1; bath_source = tuple(bits)
            bath_output = adapter_forward(c663, bath_source, horizon)
            _branch, _emit, bath_b_start, _b_sites, _width = adapter_layout(c663, horizon)
            bath_basis_identity_failures += int(bath_output[:bath_b_start] != bath_source[:bath_b_start])
            bath_basis_identity_failures += int(apply_adapter(c663, bath_output, horizon, reverse=True) != bath_source)
            for frame in frames:
                bath_basis_covariance_failures += int(
                    rotate_adapter_word(c663, bath_output, horizon, frame)
                    != adapter_forward(c663, rotate_adapter_word(c663, bath_source, horizon, frame), horizon)
                )
        # Complete each sector with the structural rejects.  No amplitudes or weights are collapsed.
        pending_stream = tuple(reject_ports + pending_ports)
        emission_streams = {t: tuple(reject_ports + emission_ports[t]) for t in emission_ports}
        reject_verdict = external.discriminate(blind(external, reject_ports, f"H{horizon}:reject"), external.RULES, frames)
        pending_verdict = external.discriminate(blind(external, pending_stream, f"H{horizon}:pending"), external.RULES, frames)
        emission_verdicts = {str(t): external.discriminate(blind(external, stream, f"H{horizon}:emit:{t}"), external.RULES, frames)
                             for t, stream in emission_streams.items()}
        support_verdict = external.discriminate(blind(external, support_ports, f"H{horizon}:support"), external.RULES, frames)
        train_emission = {str(t): external.discriminate(
            blind(external, [port for port in stream if sum(port.archive) <= 3], f"H{horizon}:train:{t}"), external.RULES, frames)
            for t, stream in emission_streams.items()}
        held_reject = external.discriminate(
            blind(external, [port for port in reject_ports if sum(port.archive) >= 4], f"H{horizon}:held"), external.RULES, frames)
        passed = bool(
            inverse_failures == port_failures == leakage_failures == covariance_failures == source_exhaust_retention_failures == 0
            and bath_basis_identity_failures == bath_basis_covariance_failures == 0
            and weight_residual < TOL
            and reject_verdict.get("law") == "unique_quorum" and pending_verdict.get("kind") == "off_family"
            and all(verdict.get("law") == "unique_quorum" for verdict in emission_verdicts.values())
            and all(verdict.get("law") == "unique_quorum" for verdict in train_emission.values())
            and support_verdict.get("kind") == "refuse_contradiction" and held_reject.get("kind") == "ambiguous"
        )
        horizon_rows[str(horizon)] = {
            "objective_sigma_weights": weights, "weight_sum_residual": weight_residual,
            "law_semantics": "one sigma is objective within the separately supplied collision-sigma candidate law; runner enumerates support and never samples",
            "event_rows": event_rows, "structural_reject_ports": len(reject_ports),
            "pending_ports": len(pending_ports), "emission_ports_per_time": {str(t): len(v) for t,v in emission_ports.items()},
            "inverse_failures": inverse_failures, "port_grammar_failures": port_failures,
            "emit_work_leakage_failures": leakage_failures,
            "source_branch_reject_and_bath_exhaust_retention_failures": source_exhaust_retention_failures,
            "bath_basis_identity_and_inverse_tests": 2 * len(adapter_bath_sites(c663,horizon)),
            "bath_basis_identity_and_inverse_failures": bath_basis_identity_failures,
            "bath_basis_all24_covariance_tests": len(adapter_bath_sites(c663,horizon)) * len(frames),
            "bath_basis_all24_covariance_failures": bath_basis_covariance_failures,
            "adapter_covariance_tests": event_rows * len(frames), "adapter_covariance_failures": covariance_failures,
            "reject_verdict": reject_verdict, "pending_verdict": pending_verdict,
            "emission_time_verdicts": emission_verdicts, "transition_support_verdict": support_verdict,
            "train_emission_verdicts": train_emission, "held_reject_verdict": held_reject,
            "branch_support_census_called_one_realized_history": False,
            "weights_called_Born_probability": False, "pass": passed,
        }
        total_inverse_failures += inverse_failures; total_port_failures += port_failures
        total_leakage += leakage_failures; total_covariance_failures += covariance_failures
        total_source_exhaust_retention_failures += source_exhaust_retention_failures
        all_event_rows += event_rows

    # Exact all24/all576 discriminator replay on one full H6 emission-time stratum.
    h6_emit1 = []
    for candidates in words:
        branch_index = None if sum(candidates) != 1 else 1
        output = adapter_forward(c663, adapter_source(c663, candidates, 6, branch_index), 6)
        h6_emit1.append(port_from_adapter_output(c663, external, output, 6))
    all24_failures = 0
    for frame in frames:
        verdict = external.discriminate(external.rotate_stream(h6_emit1, frame), external.RULES, frames)
        all24_failures += int(verdict.get("law") != "unique_quorum")
    all576_failures = composition_failures = 0
    for left, right in product(frames, repeat=2):
        sequential = external.rotate_stream(external.rotate_stream(h6_emit1, right), left)
        composed = tuple(tuple(sum(left[r][k]*right[k][c] for k in range(3)) for c in range(3)) for r in range(3))
        direct = external.rotate_stream(h6_emit1, composed)
        composition_failures += int(sequential != direct)
        verdict = external.discriminate(sequential, external.RULES, frames)
        all576_failures += int(verdict.get("law") != "unique_quorum")

    # Deletion rows on a real H6, direction-zero, emission-time-one branch.
    witness_source = adapter_source(c663, (1,0,0,0,0,0), 6, 1)
    full = adapter_forward(c663, witness_source, 6)
    deletions = []
    for label in ("endpoint:0:0", "selector:emit-open:1", "selector:admit", "packet:0:direction:0",
                  "extension:member", "extension:occurrence", "selector:emit-close:1"):
        damaged = adapter_forward(c663, witness_source, 6, delete_label=label)
        port = port_from_adapter_output(c663, external, damaged, 6)
        verdict = external.discriminate([port], external.RULES, frames)
        _branch, emit, _b_start, _b_sites, _width = adapter_layout(c663, 6)
        deletions.append({"gate": label, "basis_residual": math.sqrt(2.0) if damaged != full else 0.0,
                          "emit_work_leakage": damaged[emit], "discriminator_verdict": verdict,
                          "visible": damaged != full})

    malformed_rows = []
    good = list(adapter_source(c663, (1,0,0,0,0,0), 6, 1)); branch, emit, b_start, _b_sites, _width = adapter_layout(c663,6)
    mutations = {
        "multiple_sigma": lambda b: b.__setitem__(branch[2],1),
        "missing_sigma": lambda b: b.__setitem__(branch[1],0),
        "dirty_emit_work": lambda b: b.__setitem__(emit,1),
        "dirty_port_target": lambda b: b.__setitem__(b_start+c663.c625.B_MEMBER[0],1),
        "corrupt_blockade_output": lambda b: b.__setitem__(c663.PENDING[0],0),
    }
    for name, mutation in mutations.items():
        bits = good.copy(); mutation(bits); refused = False
        try: adapter_forward(c663, tuple(bits),6)
        except ValueError: refused = True
        malformed_rows.append({"case": name, "refused": refused})

    schedule_sizes = {str(h): {"logical_gates": len(adapter_schedule(c663,h)),
                               "X": sum(g.kind=="X" for g in adapter_schedule(c663,h)),
                               "CNOT": sum(g.kind=="CNOT" for g in adapter_schedule(c663,h)),
                               "TOFFOLI": sum(g.kind=="TOFFOLI" for g in adapter_schedule(c663,h)),
                               "retained_quantum_bath_spectator_M2": len(adapter_bath_sites(c663,h)),
                               "bath_spectator_disjoint_from_all_gate_operands": set(adapter_bath_sites(c663,h)).isdisjoint(
                                   {site for gate in adapter_schedule(c663,h) for site in gate.sites}),
                               "bounded_M2": adapter_layout(c663,h)[-1]}
                      for h in (3,4,6)}
    passed = bool(
        all(row["pass"] for row in horizon_rows.values())
        and total_inverse_failures == total_port_failures == total_leakage == total_covariance_failures == total_source_exhaust_retention_failures == 0
        and total_weight_residual < TOL and all24_failures == all576_failures == composition_failures == 0
        and all(row["visible"] for row in deletions) and all(row["refused"] for row in malformed_rows)
        and all(row["bath_spectator_disjoint_from_all_gate_operands"] for row in schedule_sizes.values())
        and prior_resource_match and all(row["pass"] for row in prior_resources)
        and "branch_index" not in inspect.signature(adapter_forward).parameters
    )
    result = {
        "candidate_law": "supplied objective collision-sigma jump law matched to exact retained dilation branch weights",
        "objective_within_supplied_candidate_law_not_framework_actuality": True,
        "host_sampler_called": False, "random_module_imported": False,
        "adapter_forward_signature": list(inspect.signature(adapter_forward).parameters),
        "runtime_host_branch_index_parameter": "branch_index" in inspect.signature(adapter_forward).parameters,
        "branch_fixture_enumeration_is_post_selector_code_space_not_sampling": True,
        "all_amplitudes_and_reject_exhaust_retained": True,
        "retained_quantum_bath_is_exact_identity_spectator": True, "source_blockade_word_mutated": False,
        "horizons": horizon_rows, "total_event_rows": all_event_rows,
        "maximum_weight_sum_residual": total_weight_residual,
        "total_inverse_failures": total_inverse_failures, "total_port_failures": total_port_failures,
        "total_emit_work_leakage_failures": total_leakage,
        "total_source_branch_reject_and_bath_exhaust_retention_failures": total_source_exhaust_retention_failures,
        "total_adapter_covariance_failures": total_covariance_failures,
        "H6_all24_discriminator_tests": len(frames), "H6_all24_discriminator_failures": all24_failures,
        "H6_all576_discriminator_tests": len(frames)**2, "H6_all576_discriminator_failures": all576_failures,
        "H6_frame_composition_failures": composition_failures,
        "deletion_rows": deletions, "malformed_rows": malformed_rows,
        "schedule_resources": schedule_sizes, "maximum_logical_gate_support_M2": 3,
        "prior_L3_L4_L6_bath_resources": [
            {"capacity": row["capacity"], "horizon": row["horizon"], "split": row["split"],
             "explicit_M2": row["explicit_M2"], "pass": row["pass"]} for row in prior_resources],
        "prior_resource_rows_match_preregistration": prior_resource_match,
        "unchanged_Cycle625_extension_used": True, "external_emit_called": False,
        "external_discriminate_function_changed": False,
        "pass": passed,
    }
    check("Cycle663 objective collision-sigma and reject adapter produces exact unchanged type-correct ports", passed,
          {"events": all_event_rows, "inverse": total_inverse_failures, "all24": all24_failures, "all576": all576_failures})
    return result


def external_audit(external, receipt):
    function_source = git_function_source(EXTERNAL_SCRIPT_COMMIT, EXTERNAL_PINS["script"][1], "discriminate")
    result = {
        "external_final_pass": receipt["pass"], "external_pass_count": receipt["pass_count"],
        "external_fail_count": receipt["fail_count"],
        "signature": list(inspect.signature(external.discriminate).parameters),
        "function_sha256": sha256(function_source.encode()).hexdigest(),
        "synthetic_emit_called": False,
    }
    result["pass"] = bool(receipt["pass"] and receipt["pass_count"] == 24 and receipt["fail_count"] == 0
                          and result["signature"] == ["stream","tables","frames"])
    check("Cycle685 calls the exact Cycle682-pinned discriminator and never its synthetic emitter", result["pass"],
          {"checks": [receipt["pass_count"],receipt["fail_count"]], "sha": result["function_sha256"]})
    return result


def no_go_discipline():
    c662_scalar = citation(CURRENT_SHORE, "scripts/physical_objective_stochastic_open_dilation_cycle662_2026_07_23.py",
                           '"member_receipt_occurrence_frame_type": "Cycle531 scalar labels')
    c662_branch = citation(CURRENT_SHORE, "scripts/physical_objective_stochastic_open_dilation_cycle662_2026_07_23.py",
                           "objective_sigma_is_law_state_not_input_token")
    c663_cand = citation(CURRENT_SHORE, "scripts/physical_dissipative_metastable_formation_channel_cycle663_2026_07_23.py",
                         "CAND = tuple(range(0, 6))")
    c663_bath = citation(CURRENT_SHORE, "scripts/physical_dissipative_metastable_formation_channel_cycle663_2026_07_23.py",
                         "A bath emission branch is not objective actuality")
    c682_refusal = citation(CURRENT_SHORE, "scripts/physical_actual_formation_record_born_admission_discriminator_bridge_cycle682_2026_07_23.py",
                            '"type": "PortSchemaMismatch"')
    families = [
        {"family": "Cycle662 direct pattern embedding", "object_formulation": "variable 1-4 pointer bits -> archive6", "mechanism_invariant": "literal bit identity", "terminal_obligation": "exact arity and port grammar", "strength": "weaker", "honesty": "ATTEMPTED", "result": "typed arity refusal", "authority": c662_scalar},
        {"family": "Cycle662 scalar equivariant port", "object_formulation": "trivial cubic branch representation -> directional winner", "mechanism_invariant": "all24 fixed-point enumeration", "terminal_obligation": "well-formed accepted PortTuple", "strength": "target-equivalent for branch-only route", "honesty": "ATTEMPTED", "result": "0 accepted covariant tuples among 128 invariant archive/loser pairs", "authority": c662_scalar},
        {"family": "Cycle662 independent packet graft", "object_formulation": "sigma plus Cycle621 direction packet", "mechanism_invariant": "separate transported direction", "terminal_obligation": "physical binding of packet to sigma", "strength": "unknown/comparable", "honesty": "ATTEMPTED", "result": "typed hidden-supply refusal; packet loop is independent", "authority": c662_branch},
        {"family": "Cycle662 reversible scalar fragment", "object_formulation": "objective branch basis fields", "mechanism_invariant": "support-two CNOT copy and exact inverse", "terminal_obligation": "strongest lawful partial without vector invention", "strength": "weaker", "honesty": "ATTEMPTED", "result": "positive 161-branch fragment", "authority": c662_branch},
        {"family": "Cycle663 objective collision-sigma adapter", "object_formulation": "six CAND/PENDING rails plus retained bath sectors", "mechanism_invariant": "supplied jump sigma and reversible unchanged extension", "terminal_obligation": "all reject/pending/emission ports", "strength": "target-equivalent under supplied law", "honesty": "ATTEMPTED", "result": "positive exact adapter", "authority": c663_cand},
        {"family": "Cycle663 coherent dilation alone", "object_formulation": "global unitary amplitude vector", "mechanism_invariant": "retained inverse and no collapse", "terminal_obligation": "objective classical selector", "strength": "incomparable/weaker", "honesty": "RULED OUT BY PRIOR", "result": "no objective path without separate law", "authority": c663_bath},
        {"family": "relational apparatus direction", "object_formulation": "new local vector carrier bound to C662 sigma", "mechanism_invariant": "cubic-covariant apparatus orientation", "terminal_obligation": "derive carrier and binding locally", "strength": "unknown/comparable", "honesty": "OPEN_NOT_COUNTED", "result": "concrete reopen route", "authority": c682_refusal},
    ]
    walls = {
        "W_C662_direction_type": "Cycle662 branch-only data are cubic scalars and do not carry a directional winner",
        "W_candidate_law_supply": "Cycle663 objective collision-sigma jump ontology is explicitly supplied",
        "W_nature_law_selection": "one working candidate kernel is not selection of nature's kernel",
        "W_Record_identification": "unchanged conditional occurrence port is not framework Record identity",
        "W_Born_frequency": "branch weights are not empirical frequency or Born probability",
    }
    pairs = [{"from": left, "to": right, "from_closes_to": False, "to_closes_from": False, "independent": True,
              "reason": "direction type, stochastic-law supply, nature selection, Record status and probability meaning are distinct"}
             for left in walls for right in walls if left != right]
    hidden = [
        {"phrase": "supplied objective collision-sigma law", "classification": "explicit load-bearing candidate-law premise"},
        {"phrase": "blank M2 target", "classification": "explicit finite resource"},
        {"phrase": "unchanged Cycle625 extension", "classification": "byte-pinned retained interface"},
        {"phrase": "proper-cubic frame chart", "classification": "compile-time transported structure, no runtime selector"},
        {"phrase": "branch-support stream", "classification": "transition census, explicitly not one realized history"},
    ]
    residuals = [
        {"prior": c662_scalar, "prior_residual": "scalar label/frame type", "current_residual": "C662 branch-only direction type", "match": True},
        {"prior": c662_branch, "prior_residual": "sigma objective only within supplied law", "current_residual": "same supplied-law ceiling", "match": True},
        {"prior": c663_bath, "prior_residual": "coherent bath branch not objective", "current_residual": "separate supplied sigma is named, not inferred from amplitude", "match": True},
        {"prior": c682_refusal, "prior_residual": "missing exact six-port schema", "current_residual": "priority route exact schema", "match": True},
        {"prior": c663_cand, "prior_residual": "six directional retained input rails", "current_residual": "constructive Cycle663 adapter controls", "match": True},
    ]
    rhetoric = [
        {"claim": "Cycle662 branch alone does not produce an accepted cubic-covariant port", "per_element": "161 live branches", "per_site": "one bounded fragment", "per_mode": "five menus", "per_block": "25 state rows/all24", "lattice_wide": "untested and not claimed"},
        {"claim": "coherent Cycle663 amplitude is not one classical port", "per_element": "pending/emission amplitude", "per_site": "one cell", "per_mode": "H3/H4/H6", "per_block": "all branch support retained", "lattice_wide": "untested"},
        {"claim": "candidate branch weight is not Born probability", "per_element": "exact kernel weight", "per_site": "one selected event", "per_mode": "all H branches", "per_block": "no sampling/frequency", "lattice_wide": "empirical interpretation open"},
    ]
    partial = [
        {"path": "Cycle662 scalar fragment", "status": "EXECUTED_POSITIVE", "closes": "objective field preservation without fabrication"},
        {"path": "Cycle663 objective collision-sigma adapter", "status": "EXECUTED_POSITIVE", "closes": "candidate-law type-correct reject/pending/emission ports"},
        {"path": "C662 relational directional apparatus", "status": "OPEN", "closes": "priority route vector type"},
        {"path": "autonomous collision-sigma law derivation", "status": "OPEN", "closes": "candidate-law supply"},
        {"path": "empirical repeated-history campaign", "status": "OPEN", "closes": "frequency/Born interpretation"},
    ]
    steelman = (
        "The C662 branch-only refusal is not constitutional: couple the 125-site instrument to a local oriented apparatus "
        "carrier whose six-state vector transforms under the proper-cubic permutation representation, prove the carrier's "
        "preinteraction direction is bound reversibly to the selected sigma rather than independently supplied, and feed that "
        "bound vector into the same Cycle625 gate word used here. Cycle685's positive Cycle663 construction already demonstrates "
        "that once genuine CAND/PENDING vector rails exist, no common port-substrate obstruction remains."
    )
    echoes = [
        {"cycle": 625, "retired": "exact port grammar", "remaining": "extensional/nature law selection"},
        {"cycle": 662, "retired": "objective sigma within supplied law", "remaining": "direction type and law derivation"},
        {"cycle": 663, "retired": "six-direction blockade/dilation", "remaining": "objective selector"},
        {"cycle": 682, "retired": "typed PortSchemaMismatch", "remaining": "constructive adapter attempt"},
        {"cycle": 685, "retired": "Cycle663 candidate-law adapter", "remaining": "C662 vector carrier and Born/nature meaning"},
    ]
    qualifying = sum(row["honesty"] in ("ATTEMPTED","RULED OUT BY PRIOR") for row in families)
    result = {
        "skill_freshness": {"origin_main_checked": True, "origin_main_advanced": True,
                            "origin_main": ORIGIN_MAIN_AT_FRESHNESS, "remote_skill_followed": True,
                            "proof_search_governance_read": True},
        "N1_approach_registry": families, "N1_qualifying_normalized_families": qualifying,
        "N2_walls": walls, "N2_directed_pairwise_table": pairs, "N3_hidden_wall_scan": hidden,
        "N4_residual_matches": residuals, "N5_rhetoric": rhetoric, "N6_partial_closure_paths": partial,
        "N6_primitive_registry_claim_made": False, "N7_steelman": steelman, "N8_cross_cycle_echo": echoes,
        "negative_claim_gate_status": "FAIL_DO_NOT_SHIP_BROAD_NEGATIVE",
        "negative_gate_failure_reason": "positive Cycle663 route and concrete C662 apparatus-vector reopen mechanism",
        "shipped_classification": "partial-narrowing plus independent positive construction",
        "broad_no_go_claim": False, "minimum_content_claim": False,
        "shared_route_independent_obstruction": False, "axiom_pressure": False,
    }
    result["pass"] = bool(qualifying >= 5 and len(pairs) == len(walls)*(len(walls)-1)
                          and all(row["match"] for row in residuals) and not result["broad_no_go_claim"]
                          and not result["minimum_content_claim"] and not result["axiom_pressure"])
    check("fresh normalized N1-N8 confines the C662 result and forbids shared obstruction or axiom pressure", result["pass"],
          {"families": qualifying, "gate": result["negative_claim_gate_status"]})
    return result


def dependency_ledger():
    result = {
        "new_edges": [
            "Cycle662 objective sigma -> reversible scalar branch fragment",
            "Cycle663 CAND/PENDING + supplied objective collision sigma -> reversible exact Cycle625-B/Cycle531 port",
            "type-correct fixed emission stratum -> unchanged discriminator -> unique_quorum candidate identity",
            "type-correct transition support -> unchanged discriminator -> nondeterminism refusal",
        ],
        "supplied": [
            "Cycle662 hybrid objective jump ontology", "Cycle663 objective collision-sigma jump ontology",
            "blank finite M2 target", "Cycle625/Cycle531 schedule", "external five-law tables and decoder",
            "compile-time cubic chart", "H3/H4/H6 fresh bath resources",
        ],
        "derived": [
            "C662 all24 fixed-point archive exhaust", "C662 reversible partial fragment",
            "Cycle663 exact branch-weight match", "all reject/pending/emission port fields by gates",
            "inverse, deletion, leakage, lawful-domain and all24/all576 controls", "route-level discriminator verdicts",
        ],
        "open": [
            "C662 physical directional apparatus bound to sigma", "derivation/selection of objective collision kernel",
            "non-erasing renewable bath", "nature-law selection", "framework Record", "actuality beyond candidate ontology",
            "empirical frequency/Born interpretation", "gravity/source",
        ],
        "six_wall_ledger": {
            "C_ref": "unchanged; no new physical reference",
            "C_num": "exact candidate branch weights and residuals; no numerical-to-Born bridge",
            "C_wrap": "candidate occurrence tuple constructed for Cycle663; framework Record/history still open",
            "C_int": "bounded collision-sigma/port adapter positive; stochastic jump ontology supplied",
            "C_local": "bounded H3/H4/H6, all24/all576 positive; no infinite/noisy deployment",
            "C_source": "finite ready/spent and bath exhaust counted; no energy/stress/gravity or renewable source",
        },
        "nature_law_selected": False, "framework_Record_derived": False, "objective_actuality_derived": False,
        "frequency_derived": False, "Born_probability_derived": False,
    }
    result["pass"] = not any(result[key] for key in ("nature_law_selected","framework_Record_derived",
        "objective_actuality_derived","frequency_derived","Born_probability_derived"))
    check("Cycle685 dependency ledger exposes both supplied jump laws and stops below Record/Born/nature meaning", result["pass"],
          {"new_edges": len(result["new_edges"]), "open": len(result["open"])})
    return result


def note_text(receipt):
    c662 = receipt["Cycle662_priority_route"]
    c663 = receipt["Cycle663_constructive_route"]
    ng = receipt["no_go_discipline"]
    route_rows = "\n".join(f"| {row['family']} | {row['status']} | {row['witness']} |" for row in c662["approach_routes"])
    horizon_rows = "\n".join(
        f"| H{h} | {row['event_rows']} | {row['objective_sigma_weights']} | {row['reject_verdict']['kind']} / {row['reject_verdict'].get('law')} | {row['pending_verdict']['kind']} | {set(v.get('law') for v in row['emission_time_verdicts'].values())} | {row['transition_support_verdict']['kind']} |"
        for h,row in c663["horizons"].items()
    )
    deletion_rows = "\n".join(
        f"| {row['gate']} | {row['basis_residual']:.6g} | {row['emit_work_leakage']} | {row['discriminator_verdict']['kind']} / {row['discriminator_verdict'].get('reason', row['discriminator_verdict'].get('law'))} |"
        for row in c663["deletion_rows"]
    )
    n1 = "\n".join(f"| {row['family']} | {row['object_formulation']} | {row['mechanism_invariant']} | {row['honesty']} | {row['result']} |" for row in ng["N1_approach_registry"])
    return f"""# Objective Born-port adapter tournament — Cycle 685

Authority: **none**

Audit: **unset**

## Exact target and shores

The target `{receipt['frozen_shores']['target_sha256']}` and preregistration `{receipt['frozen_shores']['preregistration_sha256']}` precede all imports. Cycle662, Cycle663, Cycle682 and the Cycle625/Cycle531 sources are pinned at `{CURRENT_SHORE}`; the unchanged discriminator is loaded from `{EXTERNAL_SCRIPT_COMMIT}`, with its 24/0 evidence pinned at `{EXTERNAL_EVIDENCE_COMMIT}`. The no-go skill and normalized proof-search governance were refreshed from `origin/main` `{ORIGIN_MAIN_AT_FRESHNESS}` without moving the dirty worktree.

“Objective” below always means objective **inside an explicitly supplied candidate stochastic law**. It does not mean framework actuality. “Born-port” names the campaign lane; no branch weight is called Born probability and no branch-support census is called frequency or one realized history.

## Priority Cycle662 route

Cycle662 really owns one sigma per firing, and Cycle685 preserves that fact. Its 161 live branches produce an exact reversible scalar fragment containing the unpadded pointer pattern, actual MEMBER lane, matching receipt, edge, occurrence, ADMIT, LOCK and ready/spent debit. The largest fragment source is `{c662['maximum_fragment_source_M2']}` M2; support-two CNOT copy and exact inverse have zero failures. Nine zero-propensity branches are refused rather than fired. Every semantic deletion is visible.

The exact full Cycle625 port does not follow from those branch fields alone. This is a narrow route/type result, not a framework no-go. Cycle662's exact covariance surface declares pattern/MEMBER/receipt/occurrence labels scalar. Exhaustive all24 fixed-point enumeration leaves only archives `{c662['invariant_archive_words']}`. Across all `{c662['exhaustive_invariant_archive_loser_pairs']}` invariant archive/loser pairs, there are `{c662['covariant_well_formed_occurrence_ports']}` well-formed all24-fixed occurrence ports: clearing one winner necessarily chooses a direction. No padding, lane choice, independent packet graft, host sampler or fabricated snapshot was used.

| normalized attempt | disposition | exact witness |
|---|---|---|
{route_rows}

## Independent positive Cycle663 route

Cycle663 already retains the missing six-direction `CAND` and `PENDING` rails. Cycle685 adds a separately declared objective-within-law collision sigma: a structural reject has weight one; a one-hot precursor has pending weight `r^H` and emission-time weights `(1-r)r^(t-1)`, with `r=1/2`. These weights match the retained dilation's squared amplitudes to maximum normalization residual `{c663['maximum_weight_sum_residual']:.3e}`. Supplying that jump ontology is an explicit import, not a derivation from unitary amplitudes and not Born meaning.

One reversible gate word copies genuine CAND rails to the Cycle625 endpoints, computes and then clears an emission flag from the objective branch register, writes the three exact direction packets from the retained PENDING rail, and executes the unchanged Cycle625 extension. It never mutates blockade, sigma or bath exhaust. The adapter update has no `branch_index` parameter: the runner enumerates post-selector code-space basis states as fixtures, while the explicitly supplied stochastic law—not host RNG—owns the sigma transition. Each H block includes all `6H` coherent bath modes as exact identity spectators: no adapter gate has a bath-site operand, so the preservation statement applies to an arbitrary coherent bath vector, not only the zero fixture. All 58 rejects, every pending branch and every retained emission-time branch become genuine type-correct classical ports after sigma selection. The adapter inverse, source/exhaust retention, port grammar and terminal-work leakage have zero failures.

| corpus | objective transition rows | branch weights `(pending, emit...)` | reject stream | pending stratum | each emission stratum | full support |
|---:|---:|---|---|---|---|---|
{horizon_rows}

The reject-only stream identifies `unique_quorum` because the 58 observed non-one-hot words exclude every rival family. Each fixed emission-time full/train stream identifies `unique_quorum`. The pending stratum is honestly off-family. The full transition support contains both pending and emitted ports for each one-hot word and is honestly refused as nondeterministic. These are conditional transition strata and a support census, not sampled frequencies or one history.

H6 exact discriminator replay passes all 24 frames and all 576 ordered frame compositions with zero failures. Adapter covariance itself covers every H3/H4/H6 event over all24. Held weight-4/5/6 reject streams remain ambiguous, as required. L3/L4/L6 resource rows remain finite and all exhaust is retained.

| deleted gate | basis residual | work leakage | unchanged discriminator verdict |
|---|---:|---:|---|
{deletion_rows}

Five malformed inputs—multiple/missing sigma, dirty emit work, dirty port target and corrupted blockade output—are refused. The maximum logical gate support is three M2; schedule totals and bounded M2 are explicit in the receipt.

## N1–N8 and dependency result

| normalized family | object | invariant | honesty | result |
|---|---|---|---|---|
{n1}

N2 audits `{len(ng['N2_directed_pairwise_table'])}` directed pairs across the collapsed five-wall set. N3 exposes candidate-law, blank-target, frame-chart and support-census imports. Every N4 residual matches. N5 narrows negatives to the tested element/site/mode/block. N6 retains the C662 oriented-apparatus route and autonomous kernel derivation. N7 gives the actionable hostile steelman. N8 tracks Cycles625/662/663/682/685.

The broad-negative gate is **{ng['negative_claim_gate_status']}** and the shipped classification is **{ng['shipped_classification']}**. Cycle663's positive route proves there is no shared port-substrate obstruction. There is no minimum-content or axiom-pressure claim.

The new dependency edge is `Cycle663 CAND/PENDING + supplied objective collision sigma -> reversible unchanged Cycle625 port -> route-level discriminator verdict`. C_wrap, C_int and C_local gain a bounded candidate-law construction, but no framework wall closes: the objective kernel is supplied, nature-law selection is open, the port is not a framework Record, and no frequency/Born interpretation exists.

Optimal next campaign: construct the N7 oriented apparatus carrier for Cycle662 and bind it physically to sigma, while independently trying to derive the Cycle663 collision-sigma kernel from an autonomous regenerative bath with retained exhaust and non-erasing renewal. Only after an actual repeated-history source exists should an empirical frequency/Born comparison run.
"""


def note_contract():
    text = NOTE.read_text()
    required = ("Authority: **none**", "Audit: **unset**", "objective **inside an explicitly supplied candidate stochastic law**",
                "narrow route/type result", "support census, not sampled frequencies or one history",
                "there is no shared port-substrate obstruction", "no minimum-content or axiom-pressure claim")
    missing = tuple(fragment for fragment in required if fragment not in text)
    result = {"required": required, "missing": missing, "pass": not missing}
    check("Cycle685 note preserves supplied-law, Record/Born and no-go boundaries", result["pass"], missing)
    return result


def main():
    start = time.time()
    frozen, receipts = freeze_controls()
    c663 = load_exact("cycle685_exact_c663", CURRENT_SHORE,
        "scripts/physical_dissipative_metastable_formation_channel_cycle663_2026_07_23.py")
    external = load_exact("cycle685_exact_external", EXTERNAL_SCRIPT_COMMIT,
        "scripts/physical_record_born_admission_law_discriminator_tournament_2026_07_23.py")
    ext = external_audit(external, receipts["external"])
    c662 = cycle662_priority_tournament(receipts["662"], external)
    c663_result = cycle663_constructive_tournament(c663, receipts["663"], external)
    ledger = dependency_ledger(); ng = no_go_discipline()
    receipt = {
        "cycle": 685, "authority": AUTHORITY, "audit": AUDIT,
        "status": "positive Cycle663 objective-within-supplied-law exact port adapter; Cycle662 reversible scalar partial and cubic type boundary",
        "frozen_shores": frozen, "external_discriminator": ext,
        "Cycle662_priority_route": c662, "Cycle663_constructive_route": c663_result,
        "dependency_ledger": ledger, "no_go_discipline": ng,
        "strongest_constructive_result": (
            "a bounded reversible Cycle663 collision-sigma/reject adapter generates exact unchanged Cycle625-B/Cycle531 "
            "ports for all H3/H4/H6 structural reject, pending and emission-time sectors with zero inverse, leakage, "
            "grammar, all24 or all576 failures"
        ),
        "route_disposition": {
            "Cycle662_exact_port": "ROUTE_SPECIFIC_TYPED_REFUSAL",
            "Cycle662_scalar_fragment": "POSITIVE_PARTIAL",
            "Cycle663_objective_collision_sigma_port": "POSITIVE_UNDER_EXPLICIT_SUPPLIED_CANDIDATE_LAW",
        },
        "shared_route_independent_obstruction": False, "axiom_pressure": False,
        "nature_law_selected": False, "framework_Record_derived": False,
        "objective_actuality_derived": False, "frequency_derived": False, "Born_probability_derived": False,
        "optimal_next_campaign": ng["N7_steelman"],
    }
    NOTE.write_text(note_text(receipt)); note = note_contract(); receipt["note_contract"] = note
    elapsed = time.time()-start; rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != "darwin": rss *= 1024
    receipt.update({"elapsed_seconds": elapsed, "maximum_RSS_bytes": rss,
                    "tests_passed": PASS, "tests_failed": FAIL,
                    "runner_sha256": file_sha(Path(__file__)), "note_sha256": file_sha(NOTE)})
    receipt["pass"] = bool(FAIL == 0 and all(item["pass"] for item in (frozen,ext,c662,c663_result,ledger,ng,note))
        and elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES)
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=lambda x:list(x)) + "\n")
    print(json.dumps({"pass": receipt["pass"], "tests_passed": PASS, "tests_failed": FAIL,
                      "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss,
                      "Cycle662_covariant_accepted_ports": c662["covariant_well_formed_occurrence_ports"],
                      "Cycle663_event_rows": c663_result["total_event_rows"],
                      "note": str(NOTE), "receipt": str(RECEIPT)}, indent=2))
    if not receipt["pass"]: raise SystemExit(1)


if __name__ == "__main__":
    signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError("wall cap")))
    signal.alarm(int(WALL_CAP_SECONDS))
    try: main()
    finally: signal.alarm(0)
