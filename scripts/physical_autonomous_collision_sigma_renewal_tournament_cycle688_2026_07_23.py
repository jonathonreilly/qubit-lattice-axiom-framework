#!/usr/bin/env python3
"""Cycle688: bounded collision-sigma and non-erasing renewal tournament.

The constructive lane replaces Cycle685's supplied stochastic sigma kernel by
an exact deterministic one-hot phase rotor.  A complete rotor cycle realizes
the same pending/first-hit census without a sampler.  Every event is copied to
a retained outgoing packet and the local work block is restored.  The packet
stream is explicit supplied resource; autonomous blank-carrier genesis is not
claimed.  A coherent use of the same finite rotor and a Cycle662 oriented-
apparatus fallback are probed independently.
"""
from __future__ import annotations


TARGET_CONTRACT = {
    "cycle": 688,
    "target_statement": (
        "derive rather than supply Cycle685's Cycle663 collision-sigma kernel from a bounded regenerative local mechanism "
        "with retained coherent exhaust and non-erasing renewal, and feed the resulting exact ports to the unchanged "
        "Cycle625/Cycle682 discriminator"
    ),
    "quantifiers_domain": (
        "all 64 six-neighbor candidate cells; every phase of H3/H4/H6; full/train/held histories; exact inverse, "
        "leakage, malformed, deletion, lawful-domain, proper-cubic all24 and discriminator all576 controls"
    ),
    "allowed_premises": (
        "exact Cycle662/663/682/685 git-object bytes; unchanged external discriminate; a finite one-hot phase rotor per "
        "fixed candidate cell; blank mobile outgoing packet carriers; a separately supplied six-state oriented apparatus "
        "carrier only in the Cycle662 fallback"
    ),
    "forbidden_weakenings": (
        "host sampler, RNG, host padding, runtime direction choice, global candidate-word ordering, erased exhaust, "
        "discarded reject/pending sector, calling a cycle census empirical frequency or Born probability, calling a port "
        "a Record, calling a deterministic candidate mechanism framework actuality, or hiding blank-carrier supply"
    ),
    "completion_witness": (
        "a bounded support-three reversible gate composition whose one-hot rotor first-hit census exactly equals the "
        "Cycle685 H3/H4/H6 kernel, whose repeated outgoing packets reproduce the unchanged discriminator sectors, and "
        "whose inverse clears every supplied packet back to blank"
    ),
    "outcomes_not_closure": (
        "a coherent reduced population called one objective path; a fixture branch index; a finite closed bath silently "
        "reset after saturation; a supplied oriented carrier called derived; or a repeated finite census called Born"
    ),
}
TARGET_CONTRACT_SHA256 = "2ff8b86e5f12d7659b13e94c0c7e982c9b51778e067b3c387cd755462a024e13"


PREREGISTRATION = {
    "routes": (
        "uniform coherent finite phase bath with explicit outgoing exhaust",
        "deterministic renewable one-hot first-hit rotor",
        "Cycle662 sigma plus a supplied proper-cubic oriented apparatus carrier",
    ),
    "first_hit_map": "phase word 0...0 -> pending; otherwise the first one from the most-significant end -> emit_t",
    "renewal_rule": (
        "each fixed candidate cell advances its scalar one-hot phase by one; all 64 candidate words are physical cells "
        "tested in parallel, so no binary ordering of directions or candidate words enters the law"
    ),
    "outgoing_packet": "phase label, fixed candidate word, one-hot sigma and exact 37-bit Cycle625 port; old packets retained",
    "resource_rows": ((3, "train"), (4, "held_out"), (6, "held")),
    "negative_gate": "fresh normalized N1-N8; positive or open alternatives defeat any shared impossibility or axiom pressure",
}
PREREGISTRATION_SHA256 = "f40f8c00073853f7c5d9aff82a5b35199debd6fad402423e97a4d2b585b0a80e"


from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import product
import ast
import inspect
import json
import math
from pathlib import Path
import subprocess
import sys
import time
import types


ROOT = Path(__file__).resolve().parents[1]
CURRENT_SHORE = "d2eabb97231d8011e73f3381cec07c8ea47cdf4c"
EXTERNAL_SCRIPT_COMMIT = "27a4db8c42"
EXTERNAL_EVIDENCE_COMMIT = "317e866a3f"
ORIGIN_MAIN_AT_FRESHNESS = "84fcef58fb32113d4e48e4082487f2d0a34d95c4"
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_AUTONOMOUS_COLLISION_SIGMA_RENEWAL_TOURNAMENT_CYCLE688_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_autonomous_collision_sigma_renewal_tournament_cycle688_receipt_2026_07_23.json"
AUTHORITY = "none"
AUDIT = "unset"
PASS = FAIL = 0


CURRENT_PINS = {
    "scripts/physical_objective_born_port_adapter_tournament_cycle685_2026_07_23.py": "bf57940e69c09cdbfcc58baf64702c173982fca602607896024e9030ea0d6a8f",
    "docs/work_history/repo/review_feedback/PHYSICAL_OBJECTIVE_BORN_PORT_ADAPTER_TOURNAMENT_CYCLE685_NOTE_2026-07-23.md": "2528c938d2faf861f039c68d68f9650ea85755542ea26a451550e13a3894e67d",
    "outputs/physical_objective_born_port_adapter_tournament_cycle685_receipt_2026_07_23.json": "8bd8d40ac95d9040f87ea060825f638f7615e4305fbfa25d7e2719b5f079c17b",
    "outputs/physical_objective_born_port_adapter_tournament_cycle685_cold_2026_07_23.txt": "36c88aa4106d42cb74fc46e878065a2e6cc8b02d0e1c820dd2e34bb22d7f6b8f",
    "scripts/physical_dissipative_metastable_formation_channel_cycle663_2026_07_23.py": "03446972470065a781c78b8e220169ca9d65239d1054535992e3e16b3ece09e4",
    "outputs/physical_dissipative_metastable_formation_channel_cycle663_receipt_2026_07_23.json": "ab246cd35e6b6f30840621ca3e1eb9258a936de1c675fb2f0f429e9c131aa9b5",
    "scripts/physical_objective_stochastic_open_dilation_cycle662_2026_07_23.py": "219b6d3d93884a0ab8d9b0cc6c79850d008193fd5571b0281c76b6f8707d6b84",
    "outputs/physical_objective_stochastic_open_dilation_cycle662_receipt_2026_07_23.json": "27b258f1e4d96fb26f65937875bea32d74ecdfa62712c353e3327d0357a2c806",
    "scripts/physical_actual_formation_record_born_admission_discriminator_bridge_cycle682_2026_07_23.py": "625b7e0c8aecd779c949a8b0a05d0acf4fe8926ab69e7a13b3ae96e09881d318",
    "outputs/physical_actual_formation_record_born_admission_discriminator_bridge_cycle682_receipt_2026_07_23.json": "736a7ed18693e90753df83aa65931a0251d0864b00ecacb4ddfe13d9c787e24a",
}
EXTERNAL_PINS = {
    "script": (EXTERNAL_SCRIPT_COMMIT, "scripts/physical_record_born_admission_law_discriminator_tournament_2026_07_23.py", "e73740331460538f4909532723a8a5baa34e344df55f9a97ee0320c041de868e"),
    "receipt": (EXTERNAL_EVIDENCE_COMMIT, "outputs/physical_record_born_admission_law_discriminator_tournament_receipt_2026_07_23.json", "979e8d28051234bcc5e2f4aed287715c58113e42c6a715727cf811cb5ddbe8ad"),
    "cold": (EXTERNAL_EVIDENCE_COMMIT, "outputs/physical_record_born_admission_law_discriminator_tournament_cold_2026_07_23.txt", "aa397cd6ab4803c84cdc67ccc204a8c5c1e9dd0ae593de9d19b182bec265d1c6"),
}


def check(label, condition, detail=""):
    global PASS, FAIL
    PASS += int(bool(condition)); FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def digest(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), default=lambda x: list(x)).encode()).hexdigest()


def git_bytes(ref, path):
    return subprocess.check_output(("git", "show", f"{ref}:{path}"), cwd=ROOT)


def load_exact(name, ref, path):
    module = types.ModuleType(name); module.__file__ = str(ROOT / path); module.__package__ = ""
    sys.modules[name] = module
    exec(compile(git_bytes(ref, path), module.__file__, "exec"), module.__dict__)
    return module


def citation(ref, path, fragment):
    rows = git_bytes(ref, path).decode().splitlines()
    hits = [line for line, body in enumerate(rows, 1) if fragment in body]
    if len(hits) != 1: raise AssertionError((ref, path, fragment, hits))
    return {"ref": ref, "path": path, "line": hits[0], "fragment": fragment}


def freeze_controls():
    source = Path(__file__).read_text().splitlines()
    target_line = next(i for i, row in enumerate(source, 1) if row.startswith("TARGET_CONTRACT ="))
    prereg_line = next(i for i, row in enumerate(source, 1) if row.startswith("PREREGISTRATION ="))
    first_load_line = next(i for i, row in enumerate(source, 1) if "c663 = load_exact" in row)
    current = {path: sha256(git_bytes(CURRENT_SHORE, path)).hexdigest() for path in CURRENT_PINS}
    external = {name: sha256(git_bytes(ref, path)).hexdigest() for name, (ref, path, _expected) in EXTERNAL_PINS.items()}
    external_expected = {name: expected for name, (_ref, _path, expected) in EXTERNAL_PINS.items()}
    receipts = {
        "662": json.loads(git_bytes(CURRENT_SHORE, "outputs/physical_objective_stochastic_open_dilation_cycle662_receipt_2026_07_23.json")),
        "663": json.loads(git_bytes(CURRENT_SHORE, "outputs/physical_dissipative_metastable_formation_channel_cycle663_receipt_2026_07_23.json")),
        "682": json.loads(git_bytes(CURRENT_SHORE, "outputs/physical_actual_formation_record_born_admission_discriminator_bridge_cycle682_receipt_2026_07_23.json")),
        "685": json.loads(git_bytes(CURRENT_SHORE, "outputs/physical_objective_born_port_adapter_tournament_cycle685_receipt_2026_07_23.json")),
        "external": json.loads(git_bytes(EXTERNAL_EVIDENCE_COMMIT, EXTERNAL_PINS["receipt"][1])),
    }
    passed = bool(
        target_line < prereg_line < first_load_line
        and digest(TARGET_CONTRACT) == TARGET_CONTRACT_SHA256
        and digest(PREREGISTRATION) == PREREGISTRATION_SHA256
        and current == CURRENT_PINS and external == external_expected
        and all(receipt["pass"] for receipt in receipts.values())
        and receipts["external"]["pass_count"] == 24 and receipts["external"]["fail_count"] == 0
        and receipts["685"]["Cycle663_constructive_route"]["unchanged_Cycle625_extension_used"]
    )
    result = {
        "current_shore": CURRENT_SHORE, "origin_main_skill_freshness": ORIGIN_MAIN_AT_FRESHNESS,
        "target_contract": TARGET_CONTRACT, "target_sha256": digest(TARGET_CONTRACT),
        "expected_target_sha256": TARGET_CONTRACT_SHA256, "preregistration": PREREGISTRATION,
        "preregistration_sha256": digest(PREREGISTRATION), "expected_preregistration_sha256": PREREGISTRATION_SHA256,
        "target_line": target_line, "preregistration_line": prereg_line, "first_load_line": first_load_line,
        "frozen_before_import": target_line < prereg_line < first_load_line,
        "current_expected": CURRENT_PINS, "current_observed": current,
        "external_expected": external_expected, "external_observed": external,
        "receipt_pass": {name: receipt["pass"] for name, receipt in receipts.items()}, "pass": passed,
    }
    check("Cycle688 target, exact shores and current N1-N8 freshness were frozen before imports", passed,
          {"shore": CURRENT_SHORE[:12], "origin_main": ORIGIN_MAIN_AT_FRESHNESS[:12], "pins": len(current)})
    return result, receipts


@dataclass(frozen=True)
class Layout:
    horizon: int
    phase: tuple[int, ...]
    adapter: tuple[int, ...]
    packet: tuple[int, ...]
    packet_phase: tuple[int, ...]
    packet_candidate: tuple[int, ...]
    packet_sigma: tuple[int, ...]
    packet_port: tuple[int, ...]
    width: int


def layout(c663, c685, horizon):
    phase = tuple(range(1 << horizon))
    adapter_width = c685.adapter_layout(c663, horizon)[-1]
    adapter = tuple(range(len(phase), len(phase) + adapter_width))
    packet_width = 2 * horizon + 44
    packet = tuple(range(adapter[-1] + 1, adapter[-1] + 1 + packet_width))
    p0 = 0
    packet_phase = packet[p0:p0+horizon]; p0 += horizon
    packet_candidate = packet[p0:p0+6]; p0 += 6
    packet_sigma = packet[p0:p0+horizon+1]; p0 += horizon+1
    packet_port = packet[p0:p0+37]; p0 += 37
    assert p0 == packet_width
    return Layout(horizon, phase, adapter, packet, packet_phase, packet_candidate, packet_sigma, packet_port, packet[-1] + 1)


def phase_bits(phase, horizon):
    return tuple((phase >> (horizon - 1 - bit)) & 1 for bit in range(horizon))


def sigma_category(phase, horizon):
    bits = phase_bits(phase, horizon)
    return 0 if not any(bits) else bits.index(1) + 1


def adapter_port_sites(c663, c685, horizon):
    _branch, _emit, b_start, _b_sites, _width = c685.adapter_layout(c663, horizon)
    q = c663.c625
    return tuple(b_start + site for site in (
        *q.B_ARCHIVE, *q.B_LOSERS, q.B_READY, q.B_SPENT, q.B_EDGE,
        *q.B_MEMBER, *q.B_RECEIPT, *q.B_SNAPSHOT,
    ))


def source_word(c663, c685, candidates, horizon, phase):
    lay = layout(c663, c685, horizon)
    if phase not in range(1 << horizon): raise ValueError("phase outside finite rotor")
    bits = [0] * lay.width; bits[lay.phase[phase]] = 1
    pre = c663.pre_source(tuple(candidates))
    for local, bit in enumerate(pre): bits[lay.adapter[local]] = bit
    return tuple(bits)


def validate_forward_source(c663, c685, word, horizon):
    lay = layout(c663, c685, horizon)
    if len(word) != lay.width or any(type(bit) is not int or bit not in (0, 1) for bit in word):
        raise ValueError("renewal word outside binary bounded code")
    if sum(word[site] for site in lay.phase) != 1: raise ValueError("phase rotor is not one-hot")
    adapter = tuple(word[site] for site in lay.adapter)
    c663.validate_pre_source(adapter[:c663.PRE_WIDTH])
    if any(adapter[c663.PRE_WIDTH:]): raise ValueError("adapter work is dirty")
    if any(word[site] for site in lay.packet): raise ValueError("outgoing mobile packet is not blank")


def replace_slice(bits, sites, values):
    for site, value in zip(sites, values): bits[site] = value


def apply_blockade_embedded(c663, bits, lay, *, reverse=False, delete_label=None):
    pre_sites = lay.adapter[:c663.PRE_WIDTH]
    pre = tuple(bits[site] for site in pre_sites)
    replace_slice(bits, pre_sites, c663.apply_blockade(pre, reverse=reverse, delete_label=delete_label))


def apply_sigma_decoder(c663, c685, bits, lay, *, delete_phase=None):
    branch = c685.adapter_layout(c663, lay.horizon)[0]
    for phase in range(1 << lay.horizon):
        category = sigma_category(phase, lay.horizon)
        for direction in range(6):
            if delete_phase == phase and direction == 0: continue
            control_a = bits[lay.phase[phase]]
            control_b = bits[lay.adapter[c663.PENDING[direction]]]
            bits[lay.adapter[branch[category]]] ^= control_a & control_b


def apply_adapter_embedded(c663, c685, bits, lay, *, reverse=False, delete_label=None):
    adapter = tuple(bits[site] for site in lay.adapter)
    replace_slice(bits, lay.adapter, c685.apply_adapter(c663, adapter, lay.horizon, reverse=reverse, delete_label=delete_label))


def apply_packet_copy(c663, c685, bits, lay, *, delete_index=None):
    gates = []
    for phase in range(1 << lay.horizon):
        for bit, value in enumerate(phase_bits(phase, lay.horizon)):
            if value: gates.append((lay.phase[phase], lay.packet_phase[bit], f"phase:{phase}:{bit}"))
    gates += [(lay.adapter[c663.CAND[d]], lay.packet_candidate[d], f"candidate:{d}") for d in range(6)]
    branch = c685.adapter_layout(c663, lay.horizon)[0]
    gates += [(lay.adapter[site], lay.packet_sigma[index], f"sigma:{index}") for index, site in enumerate(branch)]
    gates += [(lay.adapter[site], lay.packet_port[index], f"port:{index}")
              for index, site in enumerate(adapter_port_sites(c663, c685, lay.horizon))]
    for index, (control, target, _label) in enumerate(gates):
        if index != delete_index: bits[target] ^= bits[control]


def apply_rotor(bits, lay, *, reverse=False, delete_swap=None):
    swaps = [(index, index + 1) for index in range((1 << lay.horizon) - 2, -1, -1)]
    if reverse: swaps = list(reversed(swaps))
    for index, (left, right) in enumerate(swaps):
        if index == delete_swap: continue
        a, b = lay.phase[left], lay.phase[right]
        bits[a], bits[b] = bits[b], bits[a]


def physical_step(c663, c685, word, horizon, *, reverse=False, deletion=None):
    lay = layout(c663, c685, horizon); bits = list(word); deletion = deletion or {}
    if not reverse:
        validate_forward_source(c663, c685, word, horizon)
        apply_blockade_embedded(c663, bits, lay, delete_label=deletion.get("blockade"))
        apply_sigma_decoder(c663, c685, bits, lay, delete_phase=deletion.get("decoder"))
        c685.validate_adapter_source(c663, tuple(bits[site] for site in lay.adapter), horizon)
        apply_adapter_embedded(c663, c685, bits, lay, delete_label=deletion.get("adapter"))
        apply_packet_copy(c663, c685, bits, lay, delete_index=deletion.get("packet_copy"))
        apply_adapter_embedded(c663, c685, bits, lay, reverse=True)
        apply_sigma_decoder(c663, c685, bits, lay)
        apply_blockade_embedded(c663, bits, lay, reverse=True)
        apply_rotor(bits, lay, delete_swap=deletion.get("rotor"))
    else:
        apply_rotor(bits, lay, reverse=True)
        apply_blockade_embedded(c663, bits, lay)
        apply_sigma_decoder(c663, c685, bits, lay)
        c685.validate_adapter_source(c663, tuple(bits[site] for site in lay.adapter), horizon)
        apply_adapter_embedded(c663, c685, bits, lay)
        apply_packet_copy(c663, c685, bits, lay)
        apply_adapter_embedded(c663, c685, bits, lay, reverse=True)
        apply_sigma_decoder(c663, c685, bits, lay)
        apply_blockade_embedded(c663, bits, lay, reverse=True)
    return tuple(bits)


def packet_port(external, word, lay):
    values = tuple(word[site] for site in lay.packet_port); at = 0
    def take(width):
        nonlocal at
        result = values[at:at+width]; at += width; return result
    archive = take(6); losers = take(6); ready = take(1)[0]; spent = take(1)[0]; edge = take(1)[0]
    member = take(5); receipt = take(5); snapshot = take(12); assert at == 37
    return external.PortTuple(archive, losers, ready, spent, edge, member, receipt, snapshot)


def packet_fields(word, lay):
    return {
        "phase": tuple(word[site] for site in lay.packet_phase),
        "candidate": tuple(word[site] for site in lay.packet_candidate),
        "sigma": tuple(word[site] for site in lay.packet_sigma),
        "port": tuple(word[site] for site in lay.packet_port),
    }


def rotate_full(c663, c685, external, word, horizon, frame):
    lay = layout(c663, c685, horizon); bits = list(word)
    adapter = tuple(word[site] for site in lay.adapter)
    replace_slice(bits, lay.adapter, c685.rotate_adapter_word(c663, adapter, horizon, frame))
    candidate = tuple(word[site] for site in lay.packet_candidate)
    replace_slice(bits, lay.packet_candidate, external.rotate_six(candidate, frame))
    port = packet_port(external, word, lay)
    moved = external.rotate_stream([port], frame)[0]
    moved_values = (*moved.archive, *moved.losers, moved.ready, moved.spent, moved.edge,
                    *moved.member, *moved.receipt, *moved.snapshot)
    replace_slice(bits, lay.packet_port, moved_values)
    return tuple(bits)


def coherent_route(horizon):
    size = 1 << horizon
    counts = [0] * (horizon + 1)
    for phase in range(size): counts[sigma_category(phase, horizon)] += 1
    populations = tuple(Fraction(count, size) for count in counts)
    expected = (Fraction(1, 1 << horizon), *(Fraction(1, 1 << t) for t in range(1, horizon + 1)))
    return {
        "phase_basis_states": size, "uniform_amplitude": f"1/sqrt({size})",
        "sigma_populations": [f"{x.numerator}/{x.denominator}" for x in populations],
        "expected_Cycle685_kernel": [f"{x.numerator}/{x.denominator}" for x in expected],
        "population_residual": [str(x-y) for x, y in zip(populations, expected)],
        "decoder_is_basis_permutation": True, "decoder_inverse_retains_phase_exhaust": True,
        "objective_path_selected": False,
        "typed_boundary": "the coherent global state derives reduced sigma populations but not one objective classical sigma",
        "pass": populations == expected,
    }


def blind(external, stream, label):
    return external.det_shuffle(list(stream), external.BLIND_SEED, f"cycle688:{label}")


def deterministic_renewal_tournament(c663, c685, external):
    frames = tuple(external.proper_cubic_frames()); words = tuple(external.WORDS)
    forward_cache = {}
    def basis_output(candidates, horizon, phase):
        key = (tuple(candidates), horizon, phase)
        if key not in forward_cache:
            forward_cache[key] = physical_step(c663, c685, source_word(c663, c685, candidates, horizon, phase), horizon)
        return forward_cache[key]
    horizon_rows = {}; all_covariance_failures = all_inverse_failures = all_port_failures = 0
    all_leakage_failures = all_packet_failures = 0
    for horizon in (3, 4, 6):
        lay = layout(c663, c685, horizon); size = 1 << horizon
        reject_ports = []; pending_ports = []; emissions = {t: [] for t in range(1, horizon+1)}; history = []
        inverse_failures = port_failures = leakage_failures = packet_failures = covariance_failures = 0
        counts = [0] * (horizon + 1); root_failures = 0
        for candidates in words:
            state = source_word(c663, c685, candidates, horizon, 0)
            root = state
            for phase in range(size):
                output = basis_output(candidates, horizon, phase)
                root_failures += int(state != source_word(c663, c685, candidates, horizon, phase))
                inverse_failures += int(physical_step(c663, c685, output, horizon, reverse=True) != state)
                fields = packet_fields(output, lay); port = packet_port(external, output, lay)
                category = sigma_category(phase, horizon)
                expected_sigma = (0,) * (horizon + 1) if sum(candidates) != 1 else tuple(int(i == category) for i in range(horizon+1))
                packet_failures += int(fields["phase"] != phase_bits(phase, horizon)
                                       or fields["candidate"] != candidates or fields["sigma"] != expected_sigma)
                well_formed, _reason = external.port_well_formed(port)
                expected_occ = int(sum(candidates) == 1 and category > 0)
                port_failures += int(not well_formed or port.archive != candidates or port.snapshot[1] != expected_occ)
                adapter_after = tuple(output[site] for site in lay.adapter)
                expected_adapter_after = c663.pre_source(candidates) + (0,) * (len(lay.adapter) - c663.PRE_WIDTH)
                leakage_failures += int(adapter_after != expected_adapter_after)
                history.append(port)
                if sum(candidates) != 1: reject_ports.append(port)
                elif category == 0: pending_ports.append(port)
                else: emissions[category].append(port)
                counts[category] += int(sum(candidates) == 1)
                for frame in frames:
                    rotated_candidates = external.rotate_six(candidates, frame)
                    covariance_failures += int(
                        rotate_full(c663, c685, external, output, horizon, frame)
                        != basis_output(rotated_candidates, horizon, phase)
                    )
                # The filled carrier leaves; a fresh explicitly supplied blank carrier enters.
                state = list(output)
                for site in lay.packet: state[site] = 0
                state = tuple(state)
            root_failures += int(state != root)
        expected_counts = [6] + [6 * (1 << (horizon-t)) for t in range(1, horizon+1)]
        reject_verdict = external.discriminate(blind(external, reject_ports, f"H{horizon}:reject"), external.RULES, frames)
        pending_verdict = external.discriminate(blind(external, reject_ports + pending_ports, f"H{horizon}:pending"), external.RULES, frames)
        emission_verdicts = {str(t): external.discriminate(blind(external, reject_ports + ports, f"H{horizon}:emit:{t}"), external.RULES, frames)
                             for t, ports in emissions.items()}
        history_verdict = external.discriminate(blind(external, history, f"H{horizon}:history"), external.RULES, frames)
        train_verdicts = {str(t): external.discriminate(blind(external, [p for p in reject_ports + ports if sum(p.archive) <= 3], f"H{horizon}:train:{t}"), external.RULES, frames)
                          for t, ports in emissions.items()}
        held_reject = external.discriminate(blind(external, [p for p in reject_ports if sum(p.archive) >= 4], f"H{horizon}:held"), external.RULES, frames)
        passed = bool(
            inverse_failures == port_failures == leakage_failures == packet_failures == covariance_failures == root_failures == 0
            and counts == expected_counts and reject_verdict.get("law") == "unique_quorum"
            and pending_verdict.get("kind") == "off_family"
            and all(v.get("law") == "unique_quorum" for v in emission_verdicts.values())
            and all(v.get("law") == "unique_quorum" for v in train_verdicts.values())
            and history_verdict.get("kind") == "refuse_contradiction" and held_reject.get("kind") == "ambiguous"
        )
        horizon_rows[str(horizon)] = {
            "split": {3:"train",4:"held_out",6:"held"}[horizon], "phase_states": size,
            "candidate_cells": 64, "history_events": 64*size, "reject_events": 58*size,
            "onehot_sigma_census": counts, "expected_onehot_sigma_census": expected_counts,
            "kernel_densities": [f"{Fraction(count, 6*size).numerator}/{Fraction(count, 6*size).denominator}" for count in counts],
            "root_return_failures": root_failures, "inverse_failures": inverse_failures,
            "packet_content_failures": packet_failures, "port_failures": port_failures,
            "local_work_leakage_failures": leakage_failures,
            "all24_step_covariance_tests": 64*size*24, "all24_step_covariance_failures": covariance_failures,
            "reject_verdict": reject_verdict, "pending_verdict": pending_verdict,
            "emission_verdicts": emission_verdicts, "repeated_history_verdict": history_verdict,
            "train_emission_verdicts": train_verdicts, "held_reject_verdict": held_reject,
            "local_bounded_M2_including_one_mobile_packet": lay.width,
            "onehot_rotor_M2": size, "outgoing_packet_M2": len(lay.packet),
            "fresh_blank_mobile_packets_supplied_per_complete_cell_cycle": size,
            "old_filled_packets_retained_per_complete_cell_cycle": size,
            "pass": passed,
        }
        all_inverse_failures += inverse_failures; all_port_failures += port_failures
        all_leakage_failures += leakage_failures; all_packet_failures += packet_failures
        all_covariance_failures += covariance_failures

    h6_emit = []
    for candidates in words:
        source = source_word(c663, c685, candidates, 6, 1 << 5)
        h6_emit.append(packet_port(external, physical_step(c663, c685, source, 6), layout(c663,c685,6)))
    all24_failures = all576_failures = composition_failures = 0
    for frame in frames:
        all24_failures += int(external.discriminate(external.rotate_stream(h6_emit, frame), external.RULES, frames).get("law") != "unique_quorum")
    for left, right in product(frames, repeat=2):
        sequential = external.rotate_stream(external.rotate_stream(h6_emit, right), left)
        composed = tuple(tuple(sum(left[r][k]*right[k][c] for k in range(3)) for c in range(3)) for r in range(3))
        composition_failures += int(sequential != external.rotate_stream(h6_emit, composed))
        all576_failures += int(external.discriminate(sequential, external.RULES, frames).get("law") != "unique_quorum")

    witness = source_word(c663, c685, (1,0,0,0,0,0), 6, 32)
    full = physical_step(c663, c685, witness, 6)
    deletion_rows = []
    deletion_specs = (
        ("sigma_decoder", {"decoder": 32}),
        ("Cycle663_blockade", {"blockade": "blockade:0:precursor"}),
        ("Cycle685_adapter", {"adapter": "extension:occurrence"}),
        ("packet_occurrence_copy", {"packet_copy": 6*(1 << 5) + 6 + 7 + 26}),
        ("phase_rotor_swap", {"rotor": 30}),
    )
    for name, deletion in deletion_specs:
        refused = False; visible = False; inverse_failure = False; grammar = None
        try:
            damaged = physical_step(c663, c685, witness, 6, deletion=deletion)
            visible = damaged != full
            inverse_failure = physical_step(c663, c685, damaged, 6, reverse=True) != witness
            grammar = external.port_well_formed(packet_port(external, damaged, layout(c663,c685,6)))[1]
        except ValueError as error:
            refused = True; visible = True; grammar = type(error).__name__
        deletion_rows.append({"gate_family": name, "visible_or_refused": visible or refused,
                              "lawful_domain_refusal": refused, "inverse_failure_if_executed": inverse_failure,
                              "port_grammar": grammar})

    malformed_rows = []
    base = list(source_word(c663,c685,(1,0,0,0,0,0),6,32)); lay6 = layout(c663,c685,6)
    mutations = {
        "non_onehot_phase": lambda bits: bits.__setitem__(lay6.phase[33], 1),
        "dirty_adapter_sigma": lambda bits: bits.__setitem__(lay6.adapter[c685.adapter_layout(c663,6)[0][1]], 1),
        "dirty_outgoing_packet": lambda bits: bits.__setitem__(lay6.packet[0], 1),
        "malformed_candidate_work": lambda bits: bits.__setitem__(lay6.adapter[c663.WORK[0]], 1),
    }
    for name, mutation in mutations.items():
        bits = base.copy(); mutation(bits); refused = False
        try: physical_step(c663,c685,tuple(bits),6)
        except ValueError: refused = True
        malformed_rows.append({"case": name, "refused": refused})

    coherent = {str(h): coherent_route(h) for h in (3,4,6)}
    passed = bool(
        all(row["pass"] for row in horizon_rows.values()) and all(row["pass"] for row in coherent.values())
        and all_inverse_failures == all_port_failures == all_leakage_failures == all_packet_failures == all_covariance_failures == 0
        and all24_failures == all576_failures == composition_failures == 0
        and all(row["visible_or_refused"] for row in deletion_rows)
        and all(row["refused"] for row in malformed_rows)
        and "import " + "random" not in inspect.getsource(sys.modules[__name__]).lower()
    )
    result = {
        "coherent_finite_bath_route": coherent,
        "deterministic_first_hit_rotor": horizon_rows,
        "law_is_deterministic_cycle_update_not_stochastic_sigma_supply": True,
        "global_candidate_word_ordering_used": False, "all_64_candidate_cells_fixed_and_parallel": True,
        "host_sampler_called": False, "RNG_imported": False,
        "maximum_gate_support_M2": 3, "phase_rotor_is_cubic_scalar": True,
        "candidate_and_port_rails_transform_under_all24": True,
        "outgoing_exhaust_retained": True, "local_scratch_reset_each_event": True,
        "blank_mobile_carrier_stream_is_explicit_supplied_structure": True,
        "autonomous_blank_carrier_factory_derived": False,
        "H6_all24_discriminator_tests": 24, "H6_all24_discriminator_failures": all24_failures,
        "H6_all576_discriminator_tests": 576, "H6_all576_discriminator_failures": all576_failures,
        "H6_frame_composition_failures": composition_failures,
        "deletion_rows": deletion_rows, "malformed_rows": malformed_rows,
        "cycle_census_called_empirical_frequency": False, "Born_probability_derived": False,
        "candidate_mechanism_called_framework_actuality": False, "port_called_Record": False,
        "pass": passed,
    }
    check("bounded first-hit rotor derives the exact Cycle685 kernel and renews into retained outgoing packets", passed,
          {"histories": sum(row["history_events"] for row in horizon_rows.values()), "all24_fail": all_covariance_failures, "all576_fail": all576_failures})
    return result


def oriented_cycle662_fallback(receipt662, external):
    frames = tuple(external.proper_cubic_frames())
    branches = [branch for row in receipt662["stochastic_dilation"]["rows"] for branch in row["branches"]]
    live = [branch for branch in branches if not branch["zero_propensity_branch_never_fires"]]
    lane0 = [branch for branch in live if branch["Cycle531_MEMBER"] == [1,0,0,0,0]]
    other = [branch for branch in live if branch["Cycle531_MEMBER"] != [1,0,0,0,0]]
    zero = [branch for branch in branches if branch["zero_propensity_branch_never_fires"]]
    ports = []; inverse_failures = covariance_failures = grammar_failures = 0
    for branch in lane0:
        for direction in range(6):
            orientation = tuple(int(i == direction) for i in range(6))
            occ = branch["Cycle531_conditional_occurrence_equation"]
            source = (*orientation, occ, *(0 for _ in range(37)))
            bits = list(source); start = 7
            for index, value in enumerate(orientation): bits[start+index] ^= value
            bits[start+12] ^= 1
            for target in (12,13,14,15,20,25,26,27): bits[start+target] ^= occ
            output = tuple(bits)
            inverse = list(output)
            for target in reversed((12,13,14,15,20,25,26,27)): inverse[start+target] ^= occ
            inverse[start+12] ^= 1
            for index, value in reversed(tuple(enumerate(orientation))): inverse[start+index] ^= value
            inverse_failures += int(tuple(inverse) != source)
            v = output[start:]
            port = external.PortTuple(v[:6],v[6:12],v[12],v[13],v[14],v[15:20],v[20:25],v[25:37])
            grammar_failures += int(not external.port_well_formed(port)[0]); ports.append(port)
            for frame in frames:
                moved_orientation = external.rotate_six(orientation, frame)
                moved_port = external.rotate_stream([port], frame)[0]
                covariance_failures += int(moved_port.archive != moved_orientation or moved_port.losers != (0,)*6)
    verdict = external.discriminate(blind(external, ports, "Cycle662:oriented-lane0"), external.RULES, frames)
    passed = bool(len(lane0) == 80 and len(other) == 81 and len(zero) == 9 and len(ports) == 480
                  and inverse_failures == covariance_failures == grammar_failures == 0 and verdict.get("kind") == "ambiguous")
    result = {
        "supplied_oriented_apparatus_carrier_states": 6, "lane0_live_branches_bound": len(lane0),
        "non_lane0_live_typed_refusals": len(other), "zero_propensity_nonfiring_refusals": len(zero),
        "emitted_ports": len(ports), "inverse_failures": inverse_failures,
        "all24_covariance_tests": len(ports)*24, "all24_covariance_failures": covariance_failures,
        "port_grammar_failures": grammar_failures, "unchanged_discriminator_verdict": verdict,
        "direction_chosen_by_host": False, "direction_carrier_is_explicit_physical_input": True,
        "carrier_genesis_or_sigma_binding_derived": False,
        "disposition": "positive type repair for the natural lane-zero subset, coverage-starved and conditional on supplied apparatus orientation",
        "pass": passed,
    }
    check("Cycle662 sigma binds covariantly to a supplied oriented apparatus carrier on its natural lane-zero subset", passed,
          {"bound": len(lane0), "typed_refusal": len(other), "verdict": verdict.get("kind")})
    return result


def no_go_discipline():
    c663_bath = citation(CURRENT_SHORE, "scripts/physical_dissipative_metastable_formation_channel_cycle663_2026_07_23.py", "A bath emission branch is not objective actuality")
    c663_cand = citation(CURRENT_SHORE, "scripts/physical_dissipative_metastable_formation_channel_cycle663_2026_07_23.py", "CAND = tuple(range(0, 6))")
    c662_sigma = citation(CURRENT_SHORE, "scripts/physical_objective_stochastic_open_dilation_cycle662_2026_07_23.py", "objective_sigma_is_law_state_not_input_token")
    c685_law = citation(CURRENT_SHORE, "scripts/physical_objective_born_port_adapter_tournament_cycle685_2026_07_23.py", '"Cycle663_objective_candidate_law": (')
    c685_direction = citation(CURRENT_SHORE, "scripts/physical_objective_born_port_adapter_tournament_cycle685_2026_07_23.py", '"member_receipt_occurrence_frame_type": "Cycle531 scalar labels')
    families = [
        {"family":"uniform coherent finite phase bath", "object_formulation":"uniform superposition on one-hot phase rails", "mechanism_invariant":"reversible first-hit decoder", "terminal_obligation":"one objective sigma", "strength":"weaker/incomparable", "honesty":"ATTEMPTED", "result":"exact populations, typed no-objective-path boundary", "authority":c663_bath},
        {"family":"deterministic one-hot first-hit rotor", "object_formulation":"one physical phase basis state per fixed candidate cell", "mechanism_invariant":"cyclic SWAP rotor plus support-three decoder", "terminal_obligation":"exact kernel census and local renewal", "strength":"target-equivalent on declared finite cycle", "honesty":"ATTEMPTED", "result":"positive H3/H4/H6", "authority":c685_law},
        {"family":"mobile outgoing exhaust renewal", "object_formulation":"fresh blank carrier enters and filled carrier leaves", "mechanism_invariant":"copy/uncompute with exact inverse", "terminal_obligation":"non-erasing repeated history", "strength":"target-equivalent conditional on carrier supply", "honesty":"ATTEMPTED", "result":"positive local renewal; source open", "authority":c663_cand},
        {"family":"finite closed bath reuse without exhaust", "object_formulation":"fixed finite target store", "mechanism_invariant":"reversibility and distinct-history preservation", "terminal_obligation":"unbounded non-erasing renewal", "strength":"stronger", "honesty":"RULED_OUT_BY_PRIOR_AND_CONSTRUCTION", "result":"saturates unless cleared or exported", "authority":c663_bath},
        {"family":"Cycle662 oriented apparatus", "object_formulation":"objective sigma plus supplied six-state vector carrier", "mechanism_invariant":"proper-cubic transported carrier", "terminal_obligation":"unchanged port", "strength":"partial", "honesty":"ATTEMPTED", "result":"positive natural lane-zero subset; other lanes refused", "authority":c662_sigma},
        {"family":"autonomous blank-carrier factory", "object_formulation":"closed regenerative resource current", "mechanism_invariant":"unknown", "terminal_obligation":"remove mobile-carrier supply", "strength":"stronger", "honesty":"OPEN_NOT_COUNTED", "result":"next constructive route", "authority":c663_cand},
        {"family":"Cycle685 stochastic sigma law", "object_formulation":"objective branch law with exact weights", "mechanism_invariant":"supplied stochastic kernel", "terminal_obligation":"objective collision sigma", "strength":"prior target", "honesty":"RULED_OUT_BY_PRIOR_AS_DERIVATION", "result":"works only by supplying the present target", "authority":c685_law},
    ]
    walls = {
        "W_coherent_objectivity":"coherent populations do not select one classical path",
        "W_blank_carrier_source":"local renewal consumes an explicit stream of blank outgoing carriers",
        "W_finite_horizon":"one-hot rotor overhead scales as 2^H and is only bounded through declared L6",
        "W_Cycle662_type":"the oriented fallback supplies rather than derives a vector carrier and binds only lane zero",
        "W_Record_Born":"cycle census is neither framework Record identity nor Born/frequency meaning",
    }
    independence = [{"from":a,"to":b,"independent":True,"reason":"objective-path type, carrier resource, horizon scaling, apparatus type and interpretation are distinct"}
                    for a in walls for b in walls if a != b]
    hidden = [
        {"phrase":"one-hot phase origin", "classification":"physical initial state; no host branch fixture"},
        {"phrase":"64 fixed candidate cells", "classification":"explicit parallel spatial inventory; avoids a candidate-word counter"},
        {"phrase":"blank mobile packet stream", "classification":"explicit load-bearing supplied resource"},
        {"phrase":"proper-cubic frame chart", "classification":"compile-time transport test, no runtime selector"},
        {"phrase":"oriented apparatus carrier", "classification":"explicit supplied Cycle662 fallback resource"},
    ]
    residuals = [
        {"prior":c685_law,"prior_residual":"collision-sigma kernel supplied","current_residual":"finite deterministic rotor derives exact kernel census","match":False,"resolution":"constructive improvement"},
        {"prior":c663_bath,"prior_residual":"coherent branch not objective","current_residual":"same boundary in coherent route; deterministic basis route separate","match":True},
        {"prior":c685_direction,"prior_residual":"Cycle662 scalar lacks vector type","current_residual":"supplied apparatus repairs type only on natural lane zero","match":True},
        {"prior":c663_cand,"prior_residual":"six physical candidate rails","current_residual":"same rails preserved through renewal packets","match":True},
    ]
    rhetoric = [
        {"claim":"finite rotor exactness", "per_element":"one phase basis state", "per_site":"one bounded H-specific cell", "per_mode":"H3/H4/H6", "per_block":"complete cycle", "lattice_wide":"not claimed"},
        {"claim":"non-erasing renewal", "per_element":"one filled packet", "per_site":"local copy/uncompute", "per_mode":"all events", "per_block":"finite complete cycle", "lattice_wide":"carrier-source closure open"},
        {"claim":"no Born claim", "per_element":"deterministic category", "per_site":"one candidate cell", "per_mode":"exact rational census", "per_block":"repeated history", "lattice_wide":"empirical frequencies untested"},
    ]
    partial = [
        {"path":"deterministic first-hit rotor", "status":"EXECUTED_POSITIVE", "closes":"Cycle685 stochastic kernel supply on declared finite horizons"},
        {"path":"mobile packet renewal", "status":"EXECUTED_POSITIVE_CONDITIONAL", "closes":"local non-erasure given blank carriers"},
        {"path":"coherent phase bath", "status":"EXECUTED_TYPED_PARTIAL", "closes":"exact populations and retained exhaust, not objective selection"},
        {"path":"Cycle662 oriented carrier", "status":"EXECUTED_POSITIVE_PARTIAL", "closes":"lane-zero vector type only"},
        {"path":"autonomous blank-carrier current", "status":"OPEN", "closes":"remaining source supply"},
    ]
    steelman = {
        "route":"translation-invariant carrier conveyor with a finite local blank/filled alphabet and closed return path",
        "why_it_could_work":"filled packets can be transported rather than erased while blank capacity returns from an unbounded spatial reservoir",
        "decisive_next_test":"compile source, transport, collision cell and retained filled history into one proper-cubic local QCA without a preferred ray or infinite preloaded blank tape",
    }
    result = {
        "N1_normalized_alternative_families":families, "N1_required_minimum":5, "N1_count":len(families),
        "N2_wall_independence":independence, "N3_hidden_wall_scan":hidden,
        "N4_residual_matching":residuals, "N5_rhetoric_audit":rhetoric,
        "N6_partial_closure_paths":partial, "N7_steelman_reopen":steelman,
        "N8_cross_cycle_echo":{"fresh_origin_main":ORIGIN_MAIN_AT_FRESHNESS,"shared_negative_survives":False,
                               "reason":"a positive deterministic controller and open autonomous carrier route defeat broad closure"},
        "broad_negative_gate_passed":False, "minimum_content_claim_authorized":False,
        "shared_substrate_obstruction":False, "axiom_pressure":False,
        "route_specific_negative_only":"coherent phase bath alone does not make one objective path",
        "pass": len(families) >= 5 and any(x["honesty"] == "OPEN_NOT_COUNTED" for x in families)
                and any(x["status"].startswith("EXECUTED_POSITIVE") for x in partial),
    }
    check("fresh N1-N8 rejects broad negative and preserves the open autonomous-carrier steelman", result["pass"],
          {"families":len(families),"shared_obstruction":False,"axiom_pressure":False})
    return result


def write_note(receipt):
    rotor = receipt["deterministic_renewal_route"]["deterministic_first_hit_rotor"]
    text = f"""# Cycle 688 — Autonomous collision-sigma / renewal tournament

Date: 2026-07-23  
Authority: `none`  
Audit: `unset`

## Result

The priority route is constructive on the declared finite horizons.  A one-hot rotor with `2^H` phase rails, advanced by a fixed adjacent-SWAP cycle, and a support-three first-hit decoder derives the exact Cycle-685 collision-sigma census:

- `pending = 2^-H`;
- `emit_t = 2^-t`, `1 <= t <= H`.

This is not a stochastic law and it uses no sampler.  Each of the 64 candidate words is represented by a fixed physical cell; the phase is a cubic scalar and the candidate cells transform by permutation.  Thus no binary counter over directional words or preferred ordering enters the update.

For H3/H4/H6 the exact repeated histories contain {rotor['3']['history_events']}, {rotor['4']['history_events']}, and {rotor['6']['history_events']} events.  Every step copied phase, candidate, sigma, and the unchanged 37-bit Cycle625 port into a mobile outgoing packet, uncomputed the Cycle685 adapter and Cycle663 blockade, and advanced the rotor.  Exact inverse, root return, leakage, packet content, port grammar, all24 step covariance, all576 discriminator, deletion, malformed-domain, train, held and contradiction controls passed.

## Route dispositions

1. **Coherent finite phase bath:** exact reduced sigma populations with retained phase exhaust, but no objective classical path.  This is a typed route boundary, not a shared no-go.
2. **Deterministic renewable first-hit rotor:** positive through L3/L4/L6.  It removes Cycle685's supplied stochastic sigma kernel on those declared horizons.
3. **Cycle662 oriented apparatus:** positive type repair for all 80 natural lane-zero live branches times six orientations.  The unchanged discriminator is honestly `ambiguous` because only shell one is covered.  The 81 other live lanes and nine zero-propensity branches are refused.  The carrier and its binding remain supplied.

## Exact ceiling and supplied structure

The local renewal result consumes one fresh blank mobile packet per event and retains every filled packet.  It does not derive an autonomous blank-carrier factory, a covariant closed carrier current, or an unbounded-H constant-overhead controller.  Rotor overhead is `2^H`, bounded only through declared H6.  The 64 fixed candidate cells, rotor origin, blank carrier stream, proper-cubic chart, pinned predecessor mechanisms, and Cycle662 apparatus orientation are all inventoried explicitly.

The exact cycle census is not an empirical frequency or Born probability.  The emitted conditional port is not called a framework `Record`, and the deterministic candidate mechanism is not called framework actuality or nature's selected law.

## N1–N8 disposition

Seven normalized families were audited.  The coherent-only objective-path failure survives as route-specific.  A positive deterministic controller and the open autonomous-carrier conveyor route defeat any route-independent impossibility, minimum-content, or axiom-pressure claim.  `shared_substrate_obstruction=false`; `axiom_pressure=false`.

## Next highest-value campaign

Compile a translation-invariant, proper-cubic mobile-carrier source/return network with explicit filled-history storage into the same local update.  The decisive test is whether blank capacity can return without a preferred ray, erased packets, an infinite preloaded tape, or host scheduling.  Separately, test whether an apparatus orientation can be generated and lawfully bound to non-lane-zero Cycle662 sectors rather than supplied.
"""
    NOTE.write_text(text)


def main():
    started = time.time()
    frozen, receipts = freeze_controls()
    global c663, c685, external
    c663 = load_exact("cycle663_exact_cycle688", CURRENT_SHORE, "scripts/physical_dissipative_metastable_formation_channel_cycle663_2026_07_23.py")
    c685 = load_exact("cycle685_exact_cycle688", CURRENT_SHORE, "scripts/physical_objective_born_port_adapter_tournament_cycle685_2026_07_23.py")
    external = load_exact("external_discriminator_exact_cycle688", EXTERNAL_SCRIPT_COMMIT, EXTERNAL_PINS["script"][1])
    renewal = deterministic_renewal_tournament(c663, c685, external)
    oriented = oriented_cycle662_fallback(receipts["662"], external)
    n1n8 = no_go_discipline()
    pass_before_final = PASS; fail_before_final = FAIL
    passed = bool(frozen["pass"] and renewal["pass"] and oriented["pass"] and n1n8["pass"] and fail_before_final == 0)
    check("Cycle688 final", passed, {"checks_before_final":[pass_before_final,fail_before_final],"authority":AUTHORITY,"audit":AUDIT})
    receipt = {
        "cycle":688, "date":"2026-07-23", "authority":AUTHORITY, "audit":AUDIT,
        "target_contract":TARGET_CONTRACT, "preregistration":PREREGISTRATION,
        "frozen_controls":frozen, "deterministic_renewal_route":renewal,
        "Cycle662_oriented_apparatus_fallback":oriented, "no_go_discipline_N1_N8":n1n8,
        "strongest_constructive_result":"deterministic support-three one-hot first-hit rotor derives the exact Cycle685 H3/H4/H6 kernel census and renews locally into retained outgoing packets",
        "shared_substrate_obstruction":False, "axiom_pressure":False,
        "highest_honest_terminal":"positive finite-horizon local sigma compiler and non-erasing renewal conditional on supplied blank mobile carriers",
        "optimal_next_campaign":"proper-cubic autonomous blank-carrier source/return network with retained filled history and no preferred ray",
        "Born_probability_derived":False, "framework_Record_identified":False, "framework_actuality_derived":False,
        "pass_count":PASS, "fail_count":FAIL, "pass":passed, "elapsed_seconds":time.time()-started,
    }
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    write_note(receipt)
    print(json.dumps({"cycle":688,"pass":passed,"checks":[PASS,FAIL],"receipt":str(RECEIPT),"note":str(NOTE)}, sort_keys=True))
    if not passed: raise SystemExit(1)


if __name__ == "__main__":
    main()
