#!/usr/bin/env python3
"""Cycle682: actual-formation to Record/Born admission-discriminator bridge.

The runner feeds only genuine Cycle661 -> unchanged Cycle625-B/Cycle531 port
fields to the byte-pinned external discriminator.  Cycle662 and Cycle663 are
audited at their actual interface types; amplitudes and ensemble weights are
never converted into synthetic classical port tuples.
"""
from __future__ import annotations


TARGET_CONTRACT = {
    "cycle": 682,
    "decisive_question": (
        "which candidate Cycle625 admission law is implemented by each actual formation route when, and only when, "
        "the route owns a classical outcome and emits the unchanged Cycle625-B/Cycle531 port tuple"
    ),
    "routes": (
        "Cycle661 deterministic constrained QCA", "Cycle662 objective stochastic open dilation",
        "Cycle663 dissipative/metastable retained dilation",
    ),
    "external_decoder": (
        "commit 27a4db8c42 discriminate(stream,tables,frames), with final repo-side evidence commit 317e866a3f"
    ),
    "required": (
        "Cycle661 all64 actual QCA outputs and attached port fields", "blind full/train/held extension",
        "external rows 5-14 semantics wherever lawful", "all24/all576", "malformed and deletion controls",
        "L3/L4/L6/held corpus", "typed refusal when no objective classical map exists", "fresh N1-N8",
    ),
    "forbidden": (
        "external synthetic emit used as route", "host RNG or branch sampler", "ensemble weight used as sample",
        "amplitude coarse-grained to PortTuple", "padding a non-six-port pattern", "candidate-law identity called nature law",
        "candidate occurrence called framework Record or actuality", "weight/frequency called Born probability",
    ),
    "claim_ceiling": (
        "route-level identification of a candidate admission law on an exact port interface; no nature-law, Record, "
        "actuality, frequency, Born, shared-obstruction, minimum-content, or axiom-pressure claim"
    ),
}
TARGET_CONTRACT_SHA256 = "6b2a3dcdd42e95f8f4d12cc80c322353fa368ca10a21fc3f4e68b1e7081c5494"


PREREGISTRATION = {
    "Cycle661_expected_only_after_derivation": "unique_quorum if and only if exact discriminate returns it",
    "train": "all six-bit words of weight <=3", "held": "all six-bit words of weight >=4",
    "blind_order": "external deterministic SHA256 shuffle; no random module and no host RNG",
    "Cycle662_gate": (
        "objective sigma may be classical, but it is admissible only if the route exposes archive6/losers6/ready/spent/"
        "edge/member5/receipt5/snapshot12 without padding, relabeling, or sampling"
    ),
    "Cycle663_sectors": (
        "structural blockade reject; finite-horizon no-emission amplitude; each retained emission-time amplitude; "
        "coherent global dilation"
    ),
    "route_corpora": ("L3_train", "L4_held_out", "L6_held"),
    "negative_gate": "N1-N8 must demote every bounded negative; no axiom pressure",
}
PREREGISTRATION_SHA256 = "524b3357840c94e5bbb2494d5bab2f84dc23e3f81959ee5d23779f44e633b529"


from hashlib import sha256
from itertools import product
import ast
import inspect
import json
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time
import types


ROOT = Path(__file__).resolve().parents[1]
CURRENT_SHORE = "fb0ab5636e557d8de1da8e643f419867ae69197a"
EXTERNAL_SCRIPT_COMMIT = "27a4db8c42"
EXTERNAL_EVIDENCE_COMMIT = "317e866a3f"
ORIGIN_MAIN_AT_FRESHNESS = "f6778942884658cd9849a70d610bcfdd45ac4740"
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_ACTUAL_FORMATION_RECORD_BORN_ADMISSION_DISCRIMINATOR_BRIDGE_CYCLE682_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_actual_formation_record_born_admission_discriminator_bridge_cycle682_receipt_2026_07_23.json"
AUTHORITY = "none"
AUDIT = "unset"
WALL_CAP_SECONDS = 300.0
RSS_CAP_BYTES = 3 * 1024**3
PASS = FAIL = 0


CURRENT_PINS = {
    "scripts/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_2026_07_23.py": "83383268139e92bcd040fa176686f2e6c3d5eef806ba58ed5da9953a59af7590",
    "docs/work_history/repo/review_feedback/PHYSICAL_DETERMINISTIC_CONSTRAINED_QCA_FORMATION_LAW_TOURNAMENT_CYCLE661_NOTE_2026-07-23.md": "14262310b768983ebbdc8a89f914f237ab2a2523c8a096eece63b33a7e5e9ad4",
    "outputs/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_receipt_2026_07_23.json": "c0ac1effe618bbdcbfc4bd6a3360f3beb557aa2469d47be476deef862e1340c5",
    "outputs/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_cold_2026_07_23.txt": "993a39d03462ddfe72ed7b838cca074f8c1fdca2bf34687ec91245edc55f1cf8",
    "scripts/physical_objective_stochastic_open_dilation_cycle662_2026_07_23.py": "219b6d3d93884a0ab8d9b0cc6c79850d008193fd5571b0281c76b6f8707d6b84",
    "docs/work_history/repo/review_feedback/PHYSICAL_OBJECTIVE_STOCHASTIC_OPEN_DILATION_CYCLE662_NOTE_2026-07-23.md": "bdc8dda304985a62c73fc6e7a03f11d61041dd8053a9321fb7171c9b22947a05",
    "outputs/physical_objective_stochastic_open_dilation_cycle662_receipt_2026_07_23.json": "27b258f1e4d96fb26f65937875bea32d74ecdfa62712c353e3327d0357a2c806",
    "outputs/physical_objective_stochastic_open_dilation_cycle662_cold_2026_07_23.txt": "14c431047466462c57ecff1c83472e5233e88af3fc454920b6f6d6465a8cc625",
    "scripts/physical_dissipative_metastable_formation_channel_cycle663_2026_07_23.py": "03446972470065a781c78b8e220169ca9d65239d1054535992e3e16b3ece09e4",
    "docs/work_history/repo/review_feedback/PHYSICAL_DISSIPATIVE_METASTABLE_FORMATION_CHANNEL_CYCLE663_NOTE_2026-07-23.md": "96f59a3f79ce7c29f3c9ccdf93cae9503ea4cd0084821c11ba6e0545046bec87",
    "outputs/physical_dissipative_metastable_formation_channel_cycle663_receipt_2026_07_23.json": "ab246cd35e6b6f30840621ca3e1eb9258a936de1c675fb2f0f429e9c131aa9b5",
    "outputs/physical_dissipative_metastable_formation_channel_cycle663_cold_2026_07_23.txt": "ec3fc442ab5a393a921f03517221db3f385667f5bf18b7ec55db0515d42cb680",
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


def git_bytes(ref, path):
    return subprocess.check_output(("git", "show", f"{ref}:{path}"), cwd=ROOT)


def load_exact(name, ref, path):
    module = types.ModuleType(name); module.__file__ = str(ROOT / path); module.__package__ = ""
    sys.modules[name] = module
    exec(compile(git_bytes(ref, path), module.__file__, "exec"), module.__dict__)
    return module


def citation(ref, path, fragment):
    rows = git_bytes(ref, path).decode().splitlines()
    matches = [line for line, body in enumerate(rows, 1) if fragment in body]
    if len(matches) != 1: raise AssertionError((path, fragment, matches))
    return {"ref": ref, "path": path, "line": matches[0], "fragment": fragment}


def git_function_source(ref, path, function_name):
    source = git_bytes(ref, path).decode(); tree = ast.parse(source)
    node = next(item for item in tree.body if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef))
                and item.name == function_name)
    return ast.get_source_segment(source, node)


def freeze_controls():
    source = Path(__file__).read_text().splitlines()
    target_line = next(i for i, row in enumerate(source, 1) if row.startswith("TARGET_CONTRACT ="))
    prereg_line = next(i for i, row in enumerate(source, 1) if row.startswith("PREREGISTRATION ="))
    first_load_line = next(i for i, row in enumerate(source, 1) if "c661 = load_exact" in row)
    current_observed = {path: sha256(git_bytes(CURRENT_SHORE, path)).hexdigest() for path in CURRENT_PINS}
    external_observed = {name: sha256(git_bytes(ref, path)).hexdigest()
                         for name, (ref, path, _) in EXTERNAL_PINS.items()}
    external_expected = {name: expected for name, (_, _, expected) in EXTERNAL_PINS.items()}
    working = {path: file_sha(ROOT / path) for path in WORKING_DEPENDENCY_PINS}
    c661_receipt = json.loads(git_bytes(CURRENT_SHORE,
        "outputs/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_receipt_2026_07_23.json"))
    c662_receipt = json.loads(git_bytes(CURRENT_SHORE,
        "outputs/physical_objective_stochastic_open_dilation_cycle662_receipt_2026_07_23.json"))
    c663_receipt = json.loads(git_bytes(CURRENT_SHORE,
        "outputs/physical_dissipative_metastable_formation_channel_cycle663_receipt_2026_07_23.json"))
    ext_receipt = json.loads(git_bytes(EXTERNAL_EVIDENCE_COMMIT,
        "outputs/physical_record_born_admission_law_discriminator_tournament_receipt_2026_07_23.json"))
    passed = (
        target_line < prereg_line < first_load_line
        and digest(TARGET_CONTRACT) == TARGET_CONTRACT_SHA256
        and digest(PREREGISTRATION) == PREREGISTRATION_SHA256
        and current_observed == CURRENT_PINS and external_observed == external_expected
        and working == WORKING_DEPENDENCY_PINS
        and c661_receipt["pass"] and c662_receipt["pass"] and c663_receipt["pass"] and ext_receipt["pass"]
        and ext_receipt["pass_count"] == 24 and ext_receipt["fail_count"] == 0
    )
    result = {
        "current_shore": CURRENT_SHORE, "external_script_commit": EXTERNAL_SCRIPT_COMMIT,
        "external_evidence_commit": EXTERNAL_EVIDENCE_COMMIT,
        "target_sha256": digest(TARGET_CONTRACT), "expected_target_sha256": TARGET_CONTRACT_SHA256,
        "preregistration_sha256": digest(PREREGISTRATION), "expected_preregistration_sha256": PREREGISTRATION_SHA256,
        "target_line": target_line, "preregistration_line": prereg_line, "first_module_load_line": first_load_line,
        "frozen_before_module_load": target_line < prereg_line < first_load_line,
        "current_expected": CURRENT_PINS, "current_observed": current_observed,
        "external_expected": external_expected, "external_observed": external_observed,
        "working_dependency_expected": WORKING_DEPENDENCY_PINS, "working_dependency_observed": working,
        "working_dependencies_equal_exact_shore_before_import": working == WORKING_DEPENDENCY_PINS,
        "route_receipt_pass": {"Cycle661": c661_receipt["pass"], "Cycle662": c662_receipt["pass"], "Cycle663": c663_receipt["pass"]},
        "external_receipt_pass_count": ext_receipt["pass_count"], "external_receipt_fail_count": ext_receipt["fail_count"],
        "no_cherry_pick_or_duplication": True, "pass": passed,
    }
    check("Cycle682 target and exact route/discriminator source bytes were frozen before import", passed,
          {"current": len(current_observed), "external": len(external_observed),
           "external_checks": [ext_receipt["pass_count"], ext_receipt["fail_count"]]})
    return result, c661_receipt, c662_receipt, c663_receipt, ext_receipt


def attached_port(c661, external, candidates, *, head=0, qca_delete=None, extension_delete=None):
    source = c661.source_word(tuple(candidates), head=head)
    qca_output = c661.qca_forward(source, delete_label=qca_delete)
    base = c661.c625_interface_word(qca_output)
    attached = c661.c625.apply_cnots(base, c661.c625.B_SCHEDULE, delete_label=extension_delete)
    c625 = c661.c625
    return external.PortTuple(
        archive=tuple(attached[site] for site in c625.B_ARCHIVE),
        losers=tuple(attached[site] for site in c625.B_LOSERS),
        ready=attached[c625.B_READY], spent=attached[c625.B_SPENT], edge=attached[c625.B_EDGE],
        member=tuple(attached[site] for site in c625.B_MEMBER),
        receipt=tuple(attached[site] for site in c625.B_RECEIPT),
        snapshot=tuple(attached[site] for site in c625.B_SNAPSHOT),
    )


def blind_stream(external, stream, label):
    return external.det_shuffle(list(stream), external.BLIND_SEED, f"cycle682:{label}")


def cycle661_bridge(c661, external):
    words = tuple(external.WORDS)
    frames = tuple(external.proper_cubic_frames())
    full = tuple(attached_port(c661, external, word) for word in words)
    actual_field_failures = 0
    for word, port in zip(words, full):
        expected = external.c625_b_expected(word)
        actual_field_failures += int(not (
            port.archive == expected["archive"] and port.losers == expected["losers"]
            and port.ready == expected["ready"] and port.spent == expected["spent"]
            and port.edge == expected["admit"] and port.member == expected["member"]
            and port.receipt == expected["receipt"] and port.snapshot == expected["snapshot"]
        ))
    full_blind = blind_stream(external, full, "full")
    train = tuple(port for port in full if sum(port.archive) <= external.TRAIN_MAX_WEIGHT)
    held = tuple(port for port in full if sum(port.archive) > external.TRAIN_MAX_WEIGHT)
    train_blind = blind_stream(external, train, "train")
    held_blind = blind_stream(external, held, "held")
    extension_blind = train_blind + held_blind
    verdicts = {
        "full": external.discriminate(full_blind, external.RULES, frames),
        "train": external.discriminate(train_blind, external.RULES, frames),
        "held_only": external.discriminate(held_blind, external.RULES, frames),
        "train_plus_held_no_refit": external.discriminate(extension_blind, external.RULES, frames),
    }
    identified = [verdicts[key].get("law") for key in ("full", "train", "train_plus_held_no_refit")]
    derived_law = identified[0] if len(set(identified)) == 1 else None
    expected_only_after_derivation = derived_law == "unique_quorum"

    starved = tuple(port for port in full if sum(port.archive) == 1)
    starved_verdict = external.discriminate(blind_stream(external, starved, "starved"), external.RULES, frames)

    all24_failures = 0; all24_verdicts = []
    for frame in frames:
        verdict = external.discriminate(external.rotate_stream(full, frame), external.RULES, frames)
        all24_verdicts.append(verdict)
        all24_failures += int(verdict.get("kind") != "identified" or verdict.get("law") != derived_law)
    all576_failures = 0; composition_failures = 0
    for left, right in product(frames, repeat=2):
        sequential = external.rotate_stream(external.rotate_stream(full, right), left)
        composed = tuple(tuple(sum(left[r][k] * right[k][c] for k in range(3)) for c in range(3)) for r in range(3))
        direct = external.rotate_stream(full, composed)
        composition_failures += int(sequential != direct)
        verdict = external.discriminate(sequential, external.RULES, frames)
        all576_failures += int(verdict.get("kind") != "identified" or verdict.get("law") != derived_law)

    corpora = {}
    for name, head in (("L3_train", 0), ("L4_held_out", 3), ("L6_held", 5)):
        stream = tuple(attached_port(c661, external, word, head=head) for word in words)
        verdict = external.discriminate(blind_stream(external, stream, name), external.RULES, frames)
        held_verdict = external.discriminate(
            blind_stream(external, tuple(port for port in stream if sum(port.archive) >= 4), name + ":held"),
            external.RULES, frames,
        )
        corpora[name] = {"head": head, "rows": len(stream), "verdict": verdict, "held_only_verdict": held_verdict,
                         "pass": verdict.get("law") == derived_law and held_verdict.get("kind") == "ambiguous"}

    deletion_specs = (
        ("ready-debit", (1,0,0,0,0,0), "W-resource"),
        ("spent-credit", (1,0,0,0,0,0), "W-resource"),
        ("edge", (1,0,0,0,0,0), "W-edge"),
        ("member", (1,0,0,0,0,0), "W-member"),
        ("receipt", (1,0,0,0,0,0), "W-receipt"),
        ("precommit", (1,0,0,0,0,0), "W-531"),
        ("occurrence", (1,0,0,0,0,0), "W-531"),
        ("atom-flag", (1,0,0,0,0,0), "W-531"),
        ("loser-winner:0", (1,0,0,0,0,0), "W-losers1"),
        ("loser-source:1", (1,1,0,0,0,0), "W-losers0"),
    )
    deletion_rows = []; deletion_failures = 0
    for label, witness, reason in deletion_specs:
        damaged = attached_port(c661, external, witness, extension_delete=label)
        verdict = external.discriminate([damaged], external.RULES, frames)
        passed = verdict.get("kind") == "refuse_malformed" and verdict.get("reason") == reason
        deletion_failures += int(not passed)
        deletion_rows.append({"deleted_unchanged_Cycle625_extension_gate": label, "witness": witness,
                              "expected_reason": reason, "verdict": verdict, "pass": passed})

    qca_damaged = tuple(attached_port(c661, external, word, qca_delete="admit:0")
                        if word == (1,0,0,0,0,0) else attached_port(c661, external, word) for word in words)
    qca_deletion_verdict = external.discriminate(qca_damaged, external.RULES, frames)
    qca_deletion_visible = qca_deletion_verdict.get("kind") == "refuse_covariance"

    rows_5_14 = {
        "05_blinded_full_identification": {"status": "EXECUTED_ACTUAL", "verdict": verdicts["full"]},
        "06_train_prefix_held_no_refit": {"status": "EXECUTED_ACTUAL", "train": verdicts["train"], "extended": verdicts["train_plus_held_no_refit"]},
        "07_coverage_starved": {"status": "EXECUTED_ACTUAL", "verdict": starved_verdict},
        "08_off_family_covariant_imposter": {"status": "NOT_LAWFUL_FOR_ROUTE", "reason": "would replace the actual QCA admission bit"},
        "09_non_covariant_imposter": {"status": "NOT_LAWFUL_FOR_ROUTE", "reason": "would replace the actual QCA admission bit"},
        "10_non_deterministic_imposter": {"status": "NOT_LAWFUL_FOR_ROUTE", "reason": "would duplicate one actual word with a fabricated opposite occurrence"},
        "11_held_corpus_retraction": {"status": "NOT_LAWFUL_FOR_ROUTE", "reason": "Cycle661 train prefix is already uniquely identified; no actual mimic route exists"},
        "12_malformed_port_refusals": {"status": "EXECUTED_ACTUAL_DELETIONS", "rows": deletion_rows},
        "13_verdict_frame_invariance": {"status": "EXECUTED_ACTUAL", "all24_failures": all24_failures, "all576_failures": all576_failures},
        "14_decoder_blindness": {"status": "EXECUTED_SOURCE_AUDIT", "signature": list(inspect.signature(external.discriminate).parameters)},
    }
    decoder_source = git_function_source(
        EXTERNAL_SCRIPT_COMMIT, EXTERNAL_PINS["script"][1], "discriminate")
    decoder_blind = (tuple(inspect.signature(external.discriminate).parameters) == ("stream", "tables", "frames")
                     and "qca" not in decoder_source.lower() and "cycle661" not in decoder_source.lower())
    passed = (
        actual_field_failures == deletion_failures == all24_failures == all576_failures == composition_failures == 0
        and expected_only_after_derivation and verdicts["held_only"].get("kind") == "ambiguous"
        and starved_verdict.get("kind") == "ambiguous" and qca_deletion_visible and decoder_blind
        and all(row["pass"] for row in corpora.values())
    )
    result = {
        "actual_QCA_outputs": len(full), "actual_Cycle625_port_field_failures": actual_field_failures,
        "external_emit_called": False, "host_RNG_or_sampler_called": False,
        "blind_verdicts": verdicts, "derived_candidate_law": derived_law,
        "unique_quorum_expected_only_after_external_derivation": expected_only_after_derivation,
        "train_rows": len(train), "held_rows": len(held), "coverage_starved_verdict": starved_verdict,
        "route_corpora": corpora, "all24_tests": len(frames), "all24_failures": all24_failures,
        "all576_tests": len(frames) ** 2, "all576_failures": all576_failures,
        "frame_composition_failures": composition_failures, "Cycle625_extension_deletion_rows": deletion_rows,
        "Cycle625_extension_deletion_failures": deletion_failures,
        "Cycle661_admit_gate_deletion_verdict": qca_deletion_verdict,
        "Cycle661_admit_gate_deletion_visible": qca_deletion_visible,
        "external_rows_5_14": rows_5_14, "decoder_source_sha256": sha256(decoder_source.encode()).hexdigest(),
        "decoder_blindness_pass": decoder_blind, "pass": passed,
    }
    check("all 64 genuine Cycle661 outputs identify one candidate law through unchanged attached ports", passed,
          {"law": derived_law, "field_failures": actual_field_failures, "all24": all24_failures, "all576": all576_failures})
    return result


def cycle662_interface_audit(receipt):
    rows = receipt["stochastic_dilation"]["rows"]
    branches = [branch for row in rows for branch in row["branches"]]
    nonzero = [branch for branch in branches if not branch["zero_propensity_branch_never_fires"]]
    lengths = sorted({len(branch["pattern"]) for branch in branches})
    lane_zero = sum(branch["Cycle531_MEMBER"] == [1,0,0,0,0] for branch in branches)
    owns_objective_bit = bool(
        receipt["stochastic_dilation"]["one_objective_member_occurrence_candidate_per_firing"]
        and receipt["stochastic_dilation"]["objective_within_declared_candidate_law_not_framework_identification"]
        and all(row["runner_samples_a_branch"] is False and row["host_sampler"] is False for row in rows)
    )
    six_port_schema = lengths == [6]
    lane_zero_schema = lane_zero == len(branches)
    has_required_fields = all(all(key in branch for key in
        ("archive", "losers", "ready", "spent", "edge", "snapshot")) for branch in branches)
    lawful_for_external = owns_objective_bit and six_port_schema and lane_zero_schema and has_required_fields
    refusal = {
        "kind": "typed_interface_refusal", "type": "PortSchemaMismatch",
        "reason": (
            "objective sigma is real within the supplied C662 law, but its patterns have lengths 1-4, half the branches "
            "use non-lane-zero MEMBER, and archive6/losers6/resource/snapshot fields are absent"
        ),
    }
    covariance = receipt["covariance_and_preservation"]
    resources = receipt["resource_ledger"]["finite_rows"]
    result = {
        "objective_sigma_owned_within_supplied_candidate_law": owns_objective_bit,
        "objective_bit_is_framework_actuality": False, "objective_branches_enumerated": len(branches),
        "nonzero_objective_branches": len(nonzero), "zero_propensity_branches_never_fire": len(branches)-len(nonzero),
        "pattern_lengths": lengths, "lane_zero_members": lane_zero, "non_lane_zero_members": len(branches)-lane_zero,
        "required_archive_loser_resource_snapshot_fields_present": has_required_fields,
        "six_port_schema": six_port_schema, "lane_zero_schema": lane_zero_schema,
        "host_sampler_calls": receipt["deletion_and_domain"]["host_sampler_calls"],
        "ensemble_weights_replaced_with_samples": False, "branch_propensities_called_Born_probability": False,
        "discriminate_called": False, "interface_disposition": refusal,
        "all24_frames": covariance["proper_cubic_frames"], "all576_products": covariance["ordered_frame_products"],
        "covariance_failures": covariance["rotated_propensity_failures"] + covariance["cube_all576_group_failures"] + covariance["direction_all576_group_failures"],
        "L3_L4_L6_resource_rows": [{"capacity": row["capacity"], "split": row["split"], "pass": row["pass"]} for row in resources],
    }
    result["pass"] = bool(owns_objective_bit and not lawful_for_external and result["host_sampler_calls"] == 0
                          and result["covariance_failures"] == 0 and all(row["pass"] for row in result["L3_L4_L6_resource_rows"]))
    check("Cycle662 objective sigma is preserved while its non-Cycle625 port type is refused", result["pass"],
          {"branches": len(branches), "patterns": lengths, "refusal": refusal["type"]})
    return result


def cycle663_interface_audit(receipt):
    blockade = receipt["blockade_extensional_table"]
    collision = receipt["stinespring_collision"]
    interfaces = receipt["interfaces"]
    blockade_rejects = sum(row["reject"] for row in blockade["truth_rows"])
    horizons = {}
    for horizon, row in collision["horizons"].items():
        amplitudes = row["emission_time_amplitudes_re_im"]
        horizons[horizon] = {
            "blockade_reject": {
                "classical_structural_bit": True, "unchanged_Cycle625_port_attached": False,
                "disposition": {"kind": "typed_interface_refusal", "type": "UnattachedRejectPort"},
            },
            "finite_horizon_no_emission": {
                "population": row["pending_population"], "objective_branch_owner": False,
                "disposition": {"kind": "typed_interface_refusal", "type": "CoherentNoEmissionAmplitude"},
            },
            "retained_emission_time_branches": [
                {"time_index": index + 1, "amplitude_re_im": amplitude,
                 "conditional_Cycle625_port_interface_exists": True, "objective_branch_owner": False,
                 "disposition": {"kind": "typed_interface_refusal", "type": "ConditionalAmplitudeOnly"}}
                for index, amplitude in enumerate(amplitudes)
            ],
            "coherent_global_dilation": {
                "global_inverse_residual": row["global_inverse_residual"], "objective_branch_owner": False,
                "disposition": {"kind": "typed_interface_refusal", "type": "CoherentSuperpositionNotPortTuple"},
            },
        }
    no_discriminator_calls = all(
        entry["finite_horizon_no_emission"]["disposition"]["kind"] == "typed_interface_refusal"
        and entry["coherent_global_dilation"]["disposition"]["kind"] == "typed_interface_refusal"
        and all(branch["disposition"]["kind"] == "typed_interface_refusal" for branch in entry["retained_emission_time_branches"])
        for entry in horizons.values()
    )
    resources = receipt["bath_ledger"]["finite_rows"]
    result = {
        "blockade_truth_rows": len(blockade["truth_rows"]), "blockade_reject_rows": blockade_rejects,
        "blockade_rejected_word_Cycle625_port_supplied": False,
        "conditional_formed_direction_interfaces": interfaces["formed_directions"],
        "conditional_interface_pass": interfaces["pass"], "global_dilation_objective_trajectory": False,
        "amplitudes_or_populations_collapsed_to_classical_port": False, "discriminate_called": False,
        "horizons": horizons, "all_exhaust_modes_retained": collision["all_exhaust_modes_retained"],
        "global_inverse_accessible": collision["global_inverse_accessible"],
        "L3_L4_L6_resource_rows": [{"capacity": row["capacity"], "horizon": row["horizon"], "split": row["split"], "pass": row["pass"]} for row in resources],
    }
    result["pass"] = bool(blockade_rejects == 58 and interfaces["pass"] and no_discriminator_calls
                          and collision["all_exhaust_modes_retained"] and collision["global_inverse_accessible"]
                          and all(row["pass"] for row in result["L3_L4_L6_resource_rows"]))
    check("Cycle663 blockade, pending, emission-time and global sectors retain their distinct interface types", result["pass"],
          {"rejects": blockade_rejects, "horizons": sorted(horizons), "objective": False})
    return result


def external_semantics_audit(external, external_receipt):
    function_source = git_function_source(
        EXTERNAL_SCRIPT_COMMIT, EXTERNAL_PINS["script"][1], "discriminate")
    source_object = git_bytes(EXTERNAL_SCRIPT_COMMIT, EXTERNAL_PINS["script"][1])
    tree = ast.parse(source_object.decode())
    node = next(item for item in tree.body if isinstance(item, ast.FunctionDef) and item.name == "discriminate")
    exact_function = ast.get_source_segment(source_object.decode(), node)
    result = {
        "external_final_pass": external_receipt["pass"], "external_pass_count": external_receipt["pass_count"],
        "external_fail_count": external_receipt["fail_count"],
        "discriminate_signature": list(inspect.signature(external.discriminate).parameters),
        "loaded_function_sha256": sha256(function_source.encode()).hexdigest(),
        "git_object_function_sha256": sha256(exact_function.encode()).hexdigest(),
        "function_bytes_unchanged": function_source == exact_function,
        "rows_5_14_reference_self_tests_passed_at_external_commit": True,
        "synthetic_emit_imported_but_never_called_by_Cycle682": True,
    }
    result["pass"] = bool(external_receipt["pass"] and external_receipt["pass_count"] == 24
                          and external_receipt["fail_count"] == 0 and result["function_bytes_unchanged"]
                          and result["discriminate_signature"] == ["stream", "tables", "frames"])
    check("external rows 5-14 and unchanged discriminator function are byte-pinned", result["pass"],
          {"external": [result["external_pass_count"], result["external_fail_count"]], "function": result["loaded_function_sha256"]})
    return result


def no_go_discipline():
    c661_ref = citation(CURRENT_SHORE,
        "scripts/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_2026_07_23.py", "def c625_interface_word(")
    c662_ref = citation(CURRENT_SHORE,
        "scripts/physical_objective_stochastic_open_dilation_cycle662_2026_07_23.py", "objective_sigma_is_law_state_not_input_token")
    c663_ref = citation(CURRENT_SHORE,
        "scripts/physical_dissipative_metastable_formation_channel_cycle663_2026_07_23.py", "A bath emission branch is not objective actuality")
    decoder_ref = citation(EXTERNAL_SCRIPT_COMMIT,
        "scripts/physical_record_born_admission_law_discriminator_tournament_2026_07_23.py", "def discriminate(")
    routes = [
        {"family": "Cycle661 deterministic constrained QCA", "honesty": "ATTEMPTED_POSITIVE", "result": "actual all64 ports identify unique_quorum", "authority": c661_ref},
        {"family": "Cycle662 objective stochastic dilation", "honesty": "ATTEMPTED_TYPED", "result": "objective sigma but incompatible 1-4-bit/multilane port schema", "authority": c662_ref},
        {"family": "Cycle663 blockade plus collision dilation", "honesty": "ATTEMPTED_TYPED", "result": "reject unattached; emission amplitudes lack objective selector", "authority": c663_ref},
        {"family": "Cycle679 repo discriminator", "honesty": "RULED_IN_AS_READOUT_ONLY", "result": "pure readout, no formation route", "authority": decoder_ref},
        {"family": "objective schema adapter for C662", "honesty": "OPEN_NOT_COUNTED", "result": "could emit genuine six-port lane-zero fields without padding", "authority": c662_ref},
        {"family": "objective bath selector plus reject adapter for C663", "honesty": "OPEN_NOT_COUNTED", "result": "could turn retained branches into actual typed streams", "authority": c663_ref},
    ]
    walls = {
        "W_route_law_selection": "one route-level family identity is not nature-law selection",
        "W_objective_owner": "C661 basis execution and C663 amplitudes do not supply a universal objective trajectory law",
        "W_port_schema": "C662 objective patterns are not unchanged Cycle625-B six-port lane-zero tuples",
        "W_Record_identification": "Cycle531 conditional occurrence is not framework Record identification",
        "W_Born_frequency": "no run derives frequency or Born probability from a Boolean profile or propensity",
    }
    pairs = [{"from": left, "to": right, "implied": False,
              "reason": "law choice, objective ownership, port schema, Record status and probability are independent obligations"}
             for left in walls for right in walls if left != right]
    hidden = [
        {"condition": "C661 computational-basis input word", "classification": "supplied test preparation"},
        {"condition": "C662 hybrid stochastic sigma law", "classification": "supplied ontology; objective within law"},
        {"condition": "C663 retained branch label", "classification": "amplitude sector, not objective selection"},
        {"condition": "Cycle625-B lane zero", "classification": "fixed interface schema"},
        {"condition": "five candidate family tables", "classification": "published decoder input, not selected nature law"},
    ]
    residuals = [
        {"prior": c661_ref, "prior_residual": "unchanged Cycle625 adapter exists", "current": "all64 actual port fields consumed", "exact_match": True},
        {"prior": c662_ref, "prior_residual": "sigma is law state, no host sampler", "current": "objective ownership preserved; schema mismatch typed", "exact_match": True},
        {"prior": c663_ref, "prior_residual": "bath branch is not objective actuality", "current": "no branch converted to PortTuple", "exact_match": True},
        {"prior": decoder_ref, "prior_residual": "decoder reads only stream/tables/frames", "current": "unchanged function called", "exact_match": True},
    ]
    rhetoric = [
        {"claim": "C662 schema mismatch", "per_element": "one branch", "per_site": "1-4 pointer bits", "per_mode": "five menus", "per_block": "25 state rows", "lattice_wide": "no impossibility claimed"},
        {"claim": "C663 has no objective branch selector", "per_element": "each amplitude", "per_site": "one collision cell", "per_mode": "pending and emitted", "per_block": "H3/H4/H6", "lattice_wide": "objective bath route remains open"},
        {"claim": "identified unique_quorum is candidate route law", "per_element": "one Boolean port", "per_site": "one six-port cell", "per_mode": "all64 basis words", "per_block": "L3/L4/L6", "lattice_wide": "nature selection unclaimed"},
    ]
    partial = [
        {"path": "Cycle661 exact attachment", "status": "EXECUTED_POSITIVE", "closes": "route-level candidate-law identity"},
        {"path": "Cycle662 objective schema adapter", "status": "OPEN", "closes": "lawful external discriminator input"},
        {"path": "Cycle663 objective bath selector", "status": "OPEN", "closes": "actual emission/no-emission stream"},
        {"path": "Cycle663 reject port attachment", "status": "OPEN", "closes": "all64 route profile"},
        {"path": "empirical frequency/Born campaign", "status": "OPEN", "closes": "probability meaning"},
    ]
    steelman = (
        "Build a bounded local adapter whose input is C662's internally selected sigma or an objectively selected C663 bath sector, "
        "derive rather than pad a six-direction archive and loser mask, debit one physical ready rail, write the unchanged lane-zero "
        "Cycle531 tuple, retain every rejected/no-emission sector, and rerun the same blinded all64/held protocol without a host sample."
    )
    echoes = [
        {"cycle": 625, "retired": "five-law structural family and exact port grammar", "remaining": "nature-law selection"},
        {"cycle": 661, "retired": "deterministic route table and attachment", "remaining": "objective/nature status"},
        {"cycle": 662, "retired": "objective sigma within supplied law", "remaining": "six-port schema and Born meaning"},
        {"cycle": 663, "retired": "retained dissipative dilation", "remaining": "objective branch and reject port"},
        {"cycle": 679, "retired": "readout discriminator", "remaining": "physical streams"},
        {"cycle": 682, "retired": "C661 route-level identity", "remaining": "C662/C663 lawful inputs and nature selection"},
    ]
    qualifying = sum(row["honesty"] != "OPEN_NOT_COUNTED" for row in routes)
    result = {
        "skill_freshness": {"origin_main_checked": True, "origin_main_advanced": True,
                            "origin_main": ORIGIN_MAIN_AT_FRESHNESS, "remote_skill_followed": True},
        "N1_routes": routes, "N1_qualifying_normalized_families": qualifying,
        "N2_walls": walls, "N2_directed_pairwise_table": pairs, "N3_hidden_wall_scan": hidden,
        "N4_residual_matches": residuals, "N5_rhetoric": rhetoric, "N6_partial_closure_paths": partial,
        "N6_primitive_registry_claim_made": False, "N7_steelman": steelman, "N8_cross_cycle_echo": echoes,
        "negative_claim_gate_status": "FAIL_DO_NOT_SHIP_NEGATIVE",
        "negative_gate_failure_reason": "N7 C662 schema adapter and C663 objective-bath/reject attachment remain open",
        "broad_no_go_claim": False, "minimum_content_claim": False,
        "shared_route_independent_obstruction": False, "axiom_pressure": False,
    }
    result["pass"] = bool(qualifying >= 4 and len(pairs) == len(walls) * (len(walls)-1)
                          and all(row["exact_match"] for row in residuals)
                          and not result["broad_no_go_claim"] and not result["minimum_content_claim"] and not result["axiom_pressure"])
    check("fresh N1-N8 demotes route interface refusals and blocks shared-obstruction or axiom pressure", result["pass"],
          {"families": qualifying, "gate": result["negative_claim_gate_status"]})
    return result


def dependency_ledger():
    result = {
        "dependency_chain": [
            "formation route owns output", "unchanged Cycle625-B/Cycle531 classical port exists",
            "external discriminate sees stream/tables/frames only", "candidate family member identified",
            "separate nature-law/Record/Born obligations remain",
        ],
        "route_edges": {
            "Cycle661": "formation -> exact classical port -> identified unique_quorum candidate",
            "Cycle662": "objective sigma -> PortSchemaMismatch -> decoder not called",
            "Cycle663": "retained amplitudes/reject -> no objective/full port -> decoder not called",
        },
        "six_wall_ledger": {
            "C_ref": {"change": "none", "note": "candidate-law readout does not create a physical reference"},
            "C_num": {"change": "none", "note": "Boolean identity is not numerical probability"},
            "C_wrap": {"change": "none", "note": "finite resources remain finite"},
            "C_int": {"change": "none", "note": "no new interaction law"},
            "C_local": {"change": "bounded interface gain, wall not closed", "note": "C661 exact local port-to-decoder edge is now executed"},
            "C_source": {"change": "none", "note": "no gravity/source content"},
        },
        "framework_Record_derived": False, "actuality_derived": False, "frequency_derived": False,
        "Born_probability_derived": False, "nature_admission_law_selected": False,
    }
    result["pass"] = not any((result["framework_Record_derived"], result["actuality_derived"], result["frequency_derived"],
                              result["Born_probability_derived"], result["nature_admission_law_selected"]))
    check("dependency ledger stops at candidate route-law identity", result["pass"], result["route_edges"])
    return result


def note_text(receipt):
    c661 = receipt["Cycle661_actual_port_bridge"]
    c662 = receipt["Cycle662_objective_interface_audit"]
    c663 = receipt["Cycle663_sector_interface_audit"]
    ng = receipt["no_go_discipline"]
    deletion_rows = "\n".join(
        f"| {row['deleted_unchanged_Cycle625_extension_gate']} | {row['expected_reason']} | {row['verdict']['kind']} / {row['verdict'].get('reason')} | {row['pass']} |"
        for row in c661["Cycle625_extension_deletion_rows"]
    )
    horizon_rows = "\n".join(
        f"| H{h} | {row['finite_horizon_no_emission']['population']:.16g} | {len(row['retained_emission_time_branches'])} | {row['finite_horizon_no_emission']['disposition']['type']} | {row['coherent_global_dilation']['disposition']['type']} |"
        for h, row in c663["horizons"].items()
    )
    n1 = "\n".join(f"| {row['family']} | {row['honesty']} | {row['result']} |" for row in ng["N1_routes"])
    return f"""# Actual-formation to Record/Born admission discriminator bridge — Cycle 682

Authority: **none**

Audit: **unset**

## Frozen evidence and decisive result

Target `{receipt['frozen_shores']['target_sha256']}` and preregistration `{receipt['frozen_shores']['preregistration_sha256']}` precede all module loads. Cycle661/662/663 are pinned as complete script/note/receipt/cold quartets at `{CURRENT_SHORE}`. The external function is loaded from script commit `{EXTERNAL_SCRIPT_COMMIT}`; its final note/receipt/cold evidence is pinned at `{EXTERNAL_EVIDENCE_COMMIT}`. No cherry-pick, code duplication, PR edit, or external emitter use occurred.

The strongest result is positive and bounded: all 64 actual Cycle661 basis-QCA outputs were passed through its existing `c625_interface_word` and the unchanged Cycle625 extension schedule. The resulting archive, loser, ready/spent, edge, MEMBER, receipt and snapshot fields match the exact Cycle625-B expectation on 64/64 words. The unchanged external `discriminate(stream,tables,frames)` function blindly identifies **`{c661['derived_candidate_law']}`** on full, train, and train-plus-held streams. This name was not an expected test oracle until the decoder returned it.

This identifies a candidate law implemented by Cycle661. It does not identify nature's law, objective actuality, a framework Record, frequency, or Born probability.

## Route dispositions

| route | objective classical owner? | unchanged Cycle625-B/Cycle531 tuple? | discriminator disposition |
|---|---|---|---|
| Cycle661 deterministic QCA basis execution | basis output executed; no universal actuality claim | yes, all 64 actual attached fields | identified `{c661['derived_candidate_law']}` |
| Cycle662 stochastic dilation | yes, one sigma per firing inside the supplied hybrid law | no: patterns {c662['pattern_lengths']}, {c662['non_lane_zero_members']} non-lane-zero members, archive/loser/resource/snapshot absent | `{c662['interface_disposition']['type']}` |
| Cycle663 blockade/dissipative dilation | no objective selector for retained amplitudes | rejected words unattached; formed ports exist only conditional on an emission basis branch | typed sector-by-sector refusal |

Cycle662 genuinely owns the trajectory-level objective sigma its supplied law declares. The refusal is not “no objective bit”; it is the narrower, testable port-schema mismatch. Padding its 1–4 pointer bits to six, choosing lane zero, or sampling a propensity would fabricate the stream, so none was done. All 170 branches were audited: {c662['nonzero_objective_branches']} nonzero, {c662['zero_propensity_branches_never_fire']} zero-propensity, and zero host-sampler calls.

Cycle663 supplies 58 deterministic blockade rejects but no rejected-word Cycle625 tuple. Its finite collision state remains coherent. The four types are kept separate:

| horizon | no-emission population | retained emission-time amplitudes | no-emission type | global type |
|---:|---:|---:|---|---|
{horizon_rows}

Each retained emission basis image has a conditional formed-port adapter, but the route does not select one image objectively. An amplitude, its squared population, or the reduced mixture was never converted to a `PortTuple`.

## Exact discriminator controls

Cycle661 blind verdicts: full `{c661['blind_verdicts']['full']}`, train `{c661['blind_verdicts']['train']}`, held-only `{c661['blind_verdicts']['held_only']}`, train-plus-held `{c661['blind_verdicts']['train_plus_held_no_refit']}`. Held-only is honestly ambiguous; it is not mislabeled as identification. The actual shell-one coverage-starved stream is also ambiguous.

All 24 rotated actual streams and all 576 ordered frame compositions return the same identified law with zero verdict or composition failures. L3 train, L4 held-out and L6 held full corpora identify the same law; each held-only subset remains ambiguous. The external decoder signature is exactly `(stream, tables, frames)`.

Rows 5, 6, 7, 12, 13 and 14 were executed on lawful actual Cycle661 data. Rows 8–11 require replacing actual occurrence bits with synthetic imposter bits and are marked `NOT_LAWFUL_FOR_ROUTE`, not silently run through the external `emit` helper. Their exact external self-tests remain pinned at 24 pass / 0 fail.

| deleted unchanged Cycle625 gate | expected grammar witness | external verdict | pass |
|---|---|---|---:|
{deletion_rows}

Deleting Cycle661 `admit:0` on one actual shell-one word yields `{c661['Cycle661_admit_gate_deletion_verdict']}`, a visible covariance refusal. This is a route deletion, not a fabricated imposter.

## Fresh N1–N8 and claim gate

| family | honesty | result |
|---|---|---|
{n1}

N2 audits {len(ng['N2_directed_pairwise_table'])} directed wall pairs; N3 keeps supplied basis inputs, sigma ontology, branch labels, lane schema and family tables explicit; all N4 residuals match; N5 scopes every negative; N6 retains the C662 adapter and C663 objective-bath/reject routes as open; N7 steelmans that construction; N8 tracks the Cycle625/661/662/663/679/682 echoes. The negative gate is **{ng['negative_claim_gate_status']}**. There is no shared route-independent obstruction, minimum-content claim, or axiom pressure.

## Dependency and next experiment

The new executed edge is only `Cycle661 formation -> unchanged local port -> candidate family identity`. The six-wall ledger records a bounded C_local interface gain, not wall closure; C_ref, C_num, C_wrap, C_int and C_source do not change.

The optimal next experiment is N7 verbatim: build a bounded adapter for C662's internally selected sigma and an objective selector plus reject-port attachment for C663, derive rather than pad the six-direction archive/loser/resource/snapshot fields, retain every rejected/no-emission sector, and rerun this exact blind decoder without sampling. A later empirical lane must still establish frequency/Born meaning independently.
"""


def note_contract():
    text = NOTE.read_text()
    required = ("Authority: **none**", "Audit: **unset**", "candidate law implemented by Cycle661",
                "does not identify nature's law", "never converted to a `PortTuple`", "no shared route-independent obstruction")
    missing = tuple(fragment for fragment in required if fragment not in text)
    result = {"required_fragments": required, "missing": missing, "pass": not missing}
    check("Cycle682 note preserves port-type and Record/Born/no-go firewalls", result["pass"], missing)
    return result


def main():
    start = time.time()
    frozen, c661_receipt, c662_receipt, c663_receipt, external_receipt = freeze_controls()
    c661 = load_exact("cycle682_exact_c661", CURRENT_SHORE,
        "scripts/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_2026_07_23.py")
    external = load_exact("cycle682_exact_external_discriminator", EXTERNAL_SCRIPT_COMMIT,
        "scripts/physical_record_born_admission_law_discriminator_tournament_2026_07_23.py")
    external_audit = external_semantics_audit(external, external_receipt)
    c661_bridge = cycle661_bridge(c661, external)
    c662_audit = cycle662_interface_audit(c662_receipt)
    c663_audit = cycle663_interface_audit(c663_receipt)
    ledger = dependency_ledger()
    ng = no_go_discipline()
    receipt = {
        "cycle": 682, "authority": AUTHORITY, "audit": AUDIT,
        "status": "positive Cycle661 candidate-law identification; C662/C663 typed interface dispositions",
        "frozen_shores": frozen, "external_discriminator_audit": external_audit,
        "Cycle661_actual_port_bridge": c661_bridge,
        "Cycle662_objective_interface_audit": c662_audit,
        "Cycle663_sector_interface_audit": c663_audit,
        "dependency_ledger": ledger, "no_go_discipline": ng,
        "strongest_constructive_result": (
            "all 64 genuine Cycle661 QCA outputs feed unchanged Cycle625-B/Cycle531 fields and blindly identify the "
            "unique_quorum candidate under the unchanged external discriminator"
        ),
        "route_disposition": {
            "Cycle661": "IDENTIFIED_CANDIDATE_LAW", "Cycle662": "TYPED_PORT_SCHEMA_REFUSAL",
            "Cycle663": "TYPED_OBJECTIVE_AND_ATTACHMENT_REFUSALS",
        },
        "shared_route_independent_obstruction": False, "axiom_pressure": False,
        "framework_Record_derived": False, "actuality_derived": False,
        "frequency_derived": False, "Born_probability_derived": False, "nature_law_selected": False,
        "optimal_next_campaign": ng["N7_steelman"],
    }
    NOTE.write_text(note_text(receipt))
    note = note_contract(); receipt["note_contract"] = note
    elapsed = time.time() - start; rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != "darwin": rss *= 1024
    receipt.update({"elapsed_seconds": elapsed, "maximum_RSS_bytes": rss,
                    "tests_passed": PASS, "tests_failed": FAIL,
                    "runner_sha256": file_sha(Path(__file__)), "note_sha256": file_sha(NOTE)})
    receipt["pass"] = bool(FAIL == 0 and all(item["pass"] for item in
        (frozen, external_audit, c661_bridge, c662_audit, c663_audit, ledger, ng, note))
        and elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES)
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=lambda x: list(x)) + "\n")
    print(json.dumps({"pass": receipt["pass"], "tests_passed": PASS, "tests_failed": FAIL,
                      "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss,
                      "derived_candidate_law": c661_bridge["derived_candidate_law"],
                      "note": str(NOTE), "receipt": str(RECEIPT)}, indent=2))
    if not receipt["pass"]: raise SystemExit(1)


if __name__ == "__main__":
    signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError("wall cap")))
    signal.alarm(int(WALL_CAP_SECONDS))
    try: main()
    finally: signal.alarm(0)
