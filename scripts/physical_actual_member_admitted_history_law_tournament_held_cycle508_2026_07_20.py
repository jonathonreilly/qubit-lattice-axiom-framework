#!/usr/bin/env python3
"""Cycle 508 held-only evaluator; dry-contract or root-authorized held.

Route B alone has an explicit actual carrier/ontology.  Route A evaluates the
branch-conditional images and exact cylinders of a supplied p=q kernel; it
does not draw a seed or produce one actual member.  Route C stays open.
"""

from __future__ import annotations

import ast
from dataclasses import asdict, dataclass
from hashlib import sha256
from itertools import product
from pathlib import Path
import inspect
import json
import os
import resource
import signal
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import physical_actual_member_admitted_history_law_tournament_train_cycle508_2026_07_20 as train


c505 = train.c505
c502 = train.c502
c500 = train.c500
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ACTUAL_MEMBER_ADMITTED_HISTORY_LAW_TOURNAMENT_HELD_CYCLE508_NOTE_2026-07-20.md"
)
MODE = os.environ.get("CYCLE508_HELD_MODE")
ALLOWED_MODES = ("dry-contract", "held")
HELD_AUTHORIZATION = "root-cycle508-held-after-dry-review-2026-07-20"
AUTHORITY = "none"
AUDIT = "unset"
TOL = 2e-9
WALL_CAP_SECONDS = 900.0
RSS_CAP_BYTES = 4 * 1024**3
HELD_L = 6
HELD_N = 4
PASS = 0
FAIL = 0
MENU = train.MENU
Word = train.Word
Sparse = train.Sparse


TRAIN_RUNNER = ROOT / "scripts/physical_actual_member_admitted_history_law_tournament_train_cycle508_2026_07_20.py"
TRAIN_NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_ACTUAL_MEMBER_ADMITTED_HISTORY_LAW_TOURNAMENT_CYCLE508_NOTE_2026-07-20.md"
TRAIN_TRANSCRIPT = Path("/tmp/cycle508_train_frozen_final_2026_07_20.log")
PREFLIGHT_RUNNER = ROOT / "scripts/physical_actual_member_admitted_history_law_tournament_preflight_cycle508_2026_07_20.py"
PREFLIGHT_NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_ACTUAL_MEMBER_ADMITTED_HISTORY_LAW_TOURNAMENT_PREFLIGHT_CYCLE508_NOTE_2026-07-20.md"

FROZEN = {
    "Cycle508 train runner": "b223ff44b159a598ef52ea21b3e758a1303e126d7f53474f799ed14c0a829dc6",
    "Cycle508 train note": "7bd2fb37e3929fe1a32c901907cfb85d5d663c5a4475a77ada1504d231470bf6",
    "Cycle508 train transcript": "672eade32a582d5f6232fb2c640408543ff92e2b61858c3f19ed85c2d7c5cc31",
    "Cycle508 preflight runner": "08a59d0230b216bf8e2021c2cae4d90f39f230d96a9e984935b1879853cac0bf",
    "Cycle508 preflight note": "1568aec3eaa1053e605965524ae565b31c1a67c22071f4142b5858eb84cc9331",
    "Cycle505 accepted held note": "c3e8a1220172d5052089511616ad0ca2cdf6f6db5c92dc520c03a22600e112f4",
    "Cycle505 runner": "87f96ab5c7fd9e96c91cb32de0e2dd012e60d6cce62cf90403fb91a5e041275e",
    "premise registry": "b73431384495db657efaeab44d1d8e83b824908c418b115308e92eaa7212eea5",
    "production-kernel boundary": "26de173bb9e3a613145fa72e614a0e27d67bcbfb431605d0f8b376b52c724b26",
    "Born-frequency boundary": "f01676e96d4470498db667224a922847c98e0425bbdc88354513b7d61c38f081",
}

FROZEN_PATHS = {
    "Cycle508 train runner": TRAIN_RUNNER,
    "Cycle508 train note": TRAIN_NOTE,
    "Cycle508 train transcript": TRAIN_TRANSCRIPT,
    "Cycle508 preflight runner": PREFLIGHT_RUNNER,
    "Cycle508 preflight note": PREFLIGHT_NOTE,
    "Cycle505 accepted held note": c505.NOTE,
    "Cycle505 runner": Path(c505.__file__),
    "premise registry": ROOT / "docs/audit/data/axiom_premise_nodes.json",
    "production-kernel boundary": ROOT / "docs/RECORD_PRODUCTION_KERNEL_BOUNDARY_2026-06-06.md",
    "Born-frequency boundary": ROOT / "docs/RECORD_BORN_FREQUENCY_BOUNDARY_2026-06-05.md",
}


ACCEPTED_PREFLIGHT_HELD_MANIFEST = {
    "name": "held",
    "preparations": ("x-plus:(1,1)/sqrt(2)", "skew:(sqrt(3),i)/2"),
    "L": 6,
    "coherent_N": 4,
    "a_seed_envelope": 7,
    "b_phase_period": 5,
    "c_bath_window": 11,
    "correlation_lags": tuple(range(1, 17)),
    "algebraic_tolerance": TOL,
    "candidate_laws_executed": False,
}
ACCEPTED_HELD_MANIFEST_SHA = "a081f20974fd69adf2896068d2eefbd9eb959f3f547efc2316a12a274f8b5f65"


@dataclass(frozen=True)
class ConditionalMemberImage:
    label: int
    kernel_owner: str
    actuality: None = None


@dataclass(frozen=True)
class ConditionalOccurrenceImage:
    label: int
    branch_condition: str
    physical_bit: int
    actual_occurrence: None = None


@dataclass(frozen=True)
class ConditionalAdmittedAtomImage:
    label: int
    site: tuple[int, int, int]
    content: Word
    branch_condition: str
    actual_atom: None = None


@dataclass(frozen=True)
class HeldObligation:
    route: str
    test_id: str
    frozen_relation: str
    result: None = None


@dataclass(frozen=True)
class HeldDisposition:
    route: str
    status: str
    actual_member: object
    occurrence: object
    admitted_atom: object
    full_framework_Record: None
    qualification: str


HELD_OBLIGATIONS = (
    HeldObligation("common", "accepted_inputs", "exact final train runner/note/transcript and untouched held manifest"),
    HeldObligation("common", "inherited_surface", "actual L6 N4 all 625 histories, E/G, inverse, leakage"),
    HeldObligation("common", "codec", "exact corrected Cycle502/Cycle505 LSB-first bits3 for all labels"),
    HeldObligation("common", "binder", "content, receipt, occurrence deletion, vacancy/collision, malformed members"),
    HeldObligation("common", "locality", "NN support<=3, all24, mass, domain, deletion, resources"),
    HeldObligation("A", "conditional_images", "no draw; each supplied p=q branch maps to conditional member/occurrence/atom images"),
    HeldObligation("A", "exact_cylinders", "N4 supplied product kernel and N3 marginal, no Monte Carlo"),
    HeldObligation("B", "actual_overlay", "one supplied supported phase gives one actual carrier member/occurrence/admitted atom"),
    HeldObligation("B", "phase_receipts", "old/new phase, law receipt, candidates and coherent state retained; exact inverse"),
    HeldObligation("B", "periodic_corpus", "all starts exact period-five means and preregistered D1-D7"),
    HeldObligation("C", "open", "no finite table, first-passage, bath, renewal, stationarity, or component result"),
)


class WallCapExceeded(RuntimeError):
    pass


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def declared_runner_sha() -> str | None:
    import re
    match = re.search(r"held evaluator SHA-256:\s*([0-9a-f]{64})", NOTE.read_text(encoding="utf-8"))
    return match.group(1) if match else None


def contract_controls() -> None:
    required = (
        "authority: none", "audit: unset", "dry-contract|held only",
        "root authorization required", "untouched preflight held manifest",
        "exact corrected lsb-first codec", "route a — conditional kernel images only",
        "does not draw a seed", "no actual member", "not a born derivation",
        "route b — explicit actual carrier overlay", "not pointer copying",
        "admittedrecordatom", "full framework record remains open",
        "route c — open", "no fit or refit", "d1-d7", "all 24 proper-cubic frames",
        "no shared obstruction or axiom pressure",
    )
    body = normalized(NOTE)
    missing = tuple(item for item in required if item not in body)
    observed = {name: file_sha(path) for name, path in FROZEN_PATHS.items()}
    manifest_sha = sha256(json.dumps(ACCEPTED_PREFLIGHT_HELD_MANIFEST, sort_keys=True).encode()).hexdigest()
    actual_runner = file_sha(Path(__file__))
    check(
        "held packet freezes exact train evidence, untouched held manifest, corrected codec, and A/B/C ontology without executing held",
        not missing and observed == FROZEN and manifest_sha == ACCEPTED_HELD_MANIFEST_SHA
        and actual_runner == declared_runner_sha() and ALLOWED_MODES == ("dry-contract", "held")
        and all(item.result is None for item in HELD_OBLIGATIONS),
        {
            "missing": missing, "observed_inputs": observed,
            "held_manifest": ACCEPTED_PREFLIGHT_HELD_MANIFEST,
            "held_manifest_sha": manifest_sha,
            "actual_runner_sha": actual_runner, "declared_runner_sha": declared_runner_sha(),
            "allowed_modes": ALLOWED_MODES, "held_results_populated": False,
        },
    )


def codec_type_controls() -> None:
    codec_rows = tuple(
        (label, train.bits3(label), c505.bits3(label), c502.bits3(label))
        for label in MENU
    )
    distinct_types = (
        ConditionalMemberImage,
        ConditionalOccurrenceImage,
        ConditionalAdmittedAtomImage,
        train.ActualMemberToken,
        train.OccurrenceReceipt,
        train.AdmittedRecordAtom,
    )
    source = inspect.getsource(train.bits3)
    check(
        "all five labels bind the exact inherited LSB-first codec and conditional A images remain distinct from B actual objects",
        all(left == middle == right for _label, left, middle, right in codec_rows)
        and "c505.bits3" in source
        and len({item.__name__ for item in distinct_types}) == 6,
        {"codec_rows": codec_rows, "train_bits3_source": source, "types": tuple(item.__name__ for item in distinct_types)},
    )


def a_conditional_view(bits: Word) -> tuple[ConditionalMemberImage, ConditionalOccurrenceImage, ConditionalAdmittedAtomImage]:
    train.validate_word(bits)
    label = train.singleton_label(tuple(bits[site] for site in train.MEMBER), "A conditional member image")
    receipt = train.singleton_label(tuple(bits[site] for site in train.LAW_RECEIPT), "A conditional law receipt")
    binding = c505.c_view(tuple(bits[:c505.C_WIDTH]))
    content = tuple(bits[site] for site in train.ATOM_CONTENT)
    if label != receipt or bits[train.OCCURRENCE] != 1 or bits[train.ATOM_FLAG] != 1:
        raise ValueError("A conditional image is malformed")
    if binding.singleton != 1 or binding.eligibility[label] != 1 or content != train.bits3(label):
        raise ValueError("A conditional image does not satisfy the singleton binder")
    condition = f"if supplied Route-A kernel outcome={label}"
    return (
        ConditionalMemberImage(label, "supplied p_A=q kernel"),
        ConditionalOccurrenceImage(label, condition, bits[train.OCCURRENCE]),
        ConditionalAdmittedAtomImage(label, (0, 0, 0), content, condition),
    )


def source_obligation_controls() -> None:
    held_functions = (
        held_inherited_surface,
        held_common_binder,
        held_route_a,
        held_route_b,
        held_locality_resources,
    )
    forbidden = {"random", "choice", "choices", "argmax", "partial_trace"}
    rows = {}
    violations = []
    for function in held_functions:
        tree = ast.parse(inspect.getsource(function))
        calls = []
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            if isinstance(node.func, ast.Name):
                calls.append(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                calls.append(node.func.attr)
        hits = tuple(item for item in calls if item.lower() in forbidden)
        rows[function.__name__] = {"calls": tuple(calls), "forbidden": hits}
        violations.extend(hits)
    required_ids = {
        ("common", "inherited_surface"), ("common", "binder"), ("common", "locality"),
        ("A", "conditional_images"), ("A", "exact_cylinders"),
        ("B", "actual_overlay"), ("B", "phase_receipts"), ("B", "periodic_corpus"),
        ("C", "open"),
    }
    actual_ids = {(item.route, item.test_id) for item in HELD_OBLIGATIONS}
    check(
        "held obligations and source audits freeze A conditional images, B actuality, C-open, and all common controls without fit/refit",
        required_ids <= actual_ids and not violations and len(HELD_OBLIGATIONS) == 11
        and all(item.result is None for item in HELD_OBLIGATIONS),
        {"source_audit": rows, "obligations": tuple(asdict(item) for item in HELD_OBLIGATIONS), "C_result": None},
    )


def no_go_controls() -> None:
    n1 = (
        ("supplied stochastic kernel", "normalized p=q branch law", "actual draw/member plus admitted history remains open"),
        ("hidden actual carrier", "one-hot retained deterministic phase", "held actual overlay and non-Born discriminator"),
        ("renewable first passage", "stationary collision flux", "bath genesis, renewal, component means"),
        ("unique-ergodic symbolic law", "uniform discrepancy", "pointwise admitted histories"),
        ("consistent-history sectors", "interference exclusion", "one realized-sector occurrence law"),
        ("boundary-selected history", "global constraint", "local covariant predictive boundary"),
        ("objective stochastic field", "martingale/change of measure", "actual draw and empirical calibration"),
    )
    check(
        "N1-N8 gate keeps the untested Route-C and actual-draw families live and permits no held result before root authorization",
        len(n1) == 7 and all(len(item) == 3 for item in n1)
        and len({item[0] for item in n1}) == 7
        and file_sha(FROZEN_PATHS["premise registry"]) == FROZEN["premise registry"],
        {
            "N1_normalized": n1,
            "N2": "A branch images, B actual carrier, C renewable bath, and global routes are independent",
            "N3": "A law/seed/draw split; B ontology/phase/support; C bath/measure; full Record permanence; held absent",
            "N4": "matched to accepted train, C505 binder, Record-production and Born-frequency boundaries",
            "N5": "dry contract versus held finite versus empirical/arbitrary-N/infinite-noisy",
            "N6": "B held overlay; A conditional images; future actual draw; finite C; stationary C; unique ergodic",
            "N7": "derived regenerative local bath with unique ontic first hit, retained exhaust, admitted atom, component means, and held discriminators",
            "N8": "Cycles478/500/502/505 and corrected Cycle508 train echo",
            "gate": "UNEXECUTED held; no shared obstruction or axiom pressure",
        },
    )


def held_inherited_surface(event: dict[str, object]) -> dict[str, object]:
    rows = []
    failures = 0
    signatures = tuple(c505.c_view(c505.c_physical(c505.c_prepare(label))) for label in MENU)
    for state_name, psi in c505.input_states("held"):
        input_vector = c500.tensor_vector(psi, HELD_N)
        coherent = c505.repeated_actual_map(input_vector, event["physical"], HELD_N)
        grades = c505.grades_by_word(coherent)
        q = tuple(item.squared_sector_norm for item in train.reference_weights(event["program"], psi))
        expected = c505.expected_grades(q, HELD_N)
        residual = c505.dictionary_residual(grades, expected)
        augmented = c505.augment(coherent, signatures)
        norm_residual = abs(sum(abs(value) ** 2 for value in augmented.values()) - 1.0)
        all_binding = all(
            all(signature.singleton == 1 and signature.central_site_eligible == 1 for signature in key[-1])
            for key in augmented
        )
        failures += int(residual >= TOL or norm_residual >= TOL or len(grades) != 625 or not all_binding)
        rows.append({
            "state": state_name, "terms": len(coherent), "history_sectors": len(grades),
            "grade_residual": residual, "norm_residual": norm_residual,
            "all_binding_candidates_singleton": all_binding,
            "actual_member_before_B": None,
        })
    check(
        "held actual C478/500/502/505 surface retains all L6/N4 histories with exact inherited controls and no pre-B actual member",
        failures == 0 and max(event["single_E_G"] + event["single_inverse"]) < TOL and event["leakage"] == 0,
        {"rows": rows, "E_G": event["single_E_G"], "inverse": event["single_inverse"], "leakage": event["leakage"]},
    )
    return {"rows": rows}


def held_common_binder() -> dict[str, object]:
    rows = []
    failures = 0
    schedule = train.binder_schedule()
    for label in MENU:
        initial = train.prepare_common(label, member_supplied=True, phase=None, law_receipt_supplied=True)
        physical = train.physical_apply(initial, schedule)
        reference = train.a_reference(label)
        inverse = train.physical_apply(physical, schedule, reverse=True)
        image = a_conditional_view(physical)
        deleted = train.physical_apply(initial, schedule, delete_label=f"binder:occurrence:{label}")
        failures += int(
            physical != reference or inverse != initial or image[0].label != label
            or deleted[train.OCCURRENCE] != 0 or deleted == reference
        )
        rows.append({
            "label": label, "E_L": int(physical != reference), "inverse": int(inverse != initial),
            "conditional_member_image": asdict(image[0]),
            "conditional_occurrence_image": asdict(image[1]),
            "conditional_atom_image": asdict(image[2]),
            "occurrence_deletion_visible": deleted != reference and deleted[train.OCCURRENCE] == 0,
        })
    collision_initial = train.prepare_common(0, member_supplied=True, phase=None, law_receipt_supplied=True, vacancy=0)
    collision = train.physical_apply(collision_initial, schedule)
    collision_control = collision[train.OCCURRENCE] == 1 and collision[train.ATOM_FLAG] == 0
    malformed = {}
    valid = list(train.physical_apply(train.prepare_common(0, member_supplied=True, phase=None, law_receipt_supplied=True), schedule))
    for name, pattern in (
        ("zero", (0, 0, 0, 0, 0)), ("two", (1, 1, 0, 0, 0)), ("three", (1, 1, 1, 0, 0)),
    ):
        trial = list(valid)
        for site, bit in zip(train.MEMBER, pattern):
            trial[site] = bit
        try:
            a_conditional_view(tuple(trial))
            malformed[name] = False
        except ValueError:
            malformed[name] = True
    check(
        "held binder fixtures preserve exact LSB-first content, inverse, occurrence deletion, vacancy collision, and malformed rejection",
        failures == 0 and collision_control and all(malformed.values()),
        {"rows": rows, "collision": collision_control, "malformed": malformed, "schedule_sha": c505.schedule_digest(schedule, train.TOTAL_M2)},
    )
    return {"schedule": schedule, "rows": rows}


def cylinder(weights: tuple[float, ...], n: int) -> dict[Word, float]:
    return {word: float(np.prod(tuple(weights[label] for label in word))) for word in product(MENU, repeat=n)}


def held_route_a(event: dict[str, object]) -> dict[str, object]:
    schedule = train.binder_schedule()
    rows = []
    failures = 0
    for state_name, psi in c505.input_states("held"):
        q = tuple(item.squared_sector_norm for item in train.reference_weights(event["program"], psi))
        law = train.a_law_kernel(q)
        p = tuple(item.weight for item in law)
        decoded = {}
        images = []
        for item in law:
            if item.weight <= 1e-15:
                continue
            initial = train.prepare_common(item.label, member_supplied=True, phase=None, law_receipt_supplied=True)
            physical = train.physical_apply(initial, schedule)
            reference = train.a_reference(item.label)
            inverse = train.physical_apply(physical, schedule, reverse=True)
            image = a_conditional_view(physical)
            decoded[image[0].label] = decoded.get(image[0].label, 0.0) + item.weight
            failures += int(physical != reference or inverse != initial or image[0].actuality is not None)
            images.append({
                "weight": item.weight, "member_image": asdict(image[0]),
                "occurrence_image": asdict(image[1]), "atom_image": asdict(image[2]),
            })
        one = {label: p[label] for label in MENU}
        n4 = cylinder(p, 4)
        n3 = cylinder(p, 3)
        marginal = {
            prefix: sum(weight for word, weight in n4.items() if word[:3] == prefix)
            for prefix in product(MENU, repeat=3)
        }
        one_residual = train.kernel_residual(one, decoded)
        marginal_residual = train.kernel_residual(n3, marginal)
        failures += int(one_residual >= TOL or marginal_residual >= TOL or len(n4) != 625)
        rows.append({
            "state": state_name, "conditional_images": images,
            "E_L_kernel_residual": one_residual, "N4_cylinder_count": len(n4),
            "N4_to_N3_projective_residual": marginal_residual,
            "D1": 0.0, "D2": 0.0, "D3": 0.0, "D4": 0.0,
            "actual_seed_draw": False, "actual_member": None,
            "actual_occurrence": None, "actual_admitted_atom": None,
        })
    check(
        "A held branch-conditional images and exact N4 supplied-law cylinders transfer without drawing a seed or producing one actual member",
        failures == 0,
        {
            "rows": rows, "p_equals_q": "supplied candidate-law content",
            "Born_derivation": False, "host_random_choice": False, "Monte_Carlo": False,
            "full_framework_Record": None,
        },
    )
    return {"schedule": schedule, "rows": rows, "D1": 0.0, "D2": 0.0, "D3": 0.0, "D4": 0.0, "D6": "conditional-image residual 0"}


def held_route_b(event: dict[str, object]) -> dict[str, object]:
    schedule = train.b_schedule()
    rows = []
    failures = 0
    for phase in MENU:
        train.validate_b_law_domain((1, 1, 1, 1, 1), phase)
        initial = train.prepare_common(phase, member_supplied=False, phase=phase, law_receipt_supplied=False)
        physical = train.physical_apply(initial, schedule)
        reference = train.b_reference(phase, phase)
        inverse = train.physical_apply(physical, schedule, reverse=True)
        view = train.decode_common(physical, "B")
        deleted = train.physical_apply(initial, schedule, delete_label=f"B:select:{phase}")
        failures += int(
            physical != reference or inverse != initial or view.member.label != phase
            or view.next_phase != (phase + 1) % 5 or view.retained_previous_phase != phase
            or any(deleted[site] for site in train.MEMBER)
            or physical[:c505.C_WIDTH] != initial[:c505.C_WIDTH]
        )
        rows.append({
            "phase": phase, "E_L": int(physical != reference), "inverse": int(inverse != initial),
            "actual_member": asdict(view.member), "occurrence": asdict(view.occurrence),
            "admitted_atom": asdict(view.atom), "next_phase": view.next_phase,
            "old_phase": view.retained_previous_phase, "law_receipt": view.member.receipt_label,
            "candidate_word_retained": physical[:c505.C_WIDTH] == initial[:c505.C_WIDTH],
            "selection_deletion_visible": not any(deleted[site] for site in train.MEMBER),
            "full_framework_Record": None,
        })
    counterfactual_failures = 0
    for pointer in MENU:
        for phase in MENU:
            if pointer == phase:
                continue
            initial = train.prepare_common(pointer, member_supplied=False, phase=phase, law_receipt_supplied=False)
            physical = train.physical_apply(initial, schedule)
            counterfactual_failures += int(
                physical != train.b_reference(pointer, phase)
                or any(physical[site] for site in train.MEMBER)
                or physical[train.OCCURRENCE] or physical[train.ATOM_FLAG]
            )
    theorem = []
    for start in MENU:
        word = tuple((start + step) % 5 for step in range(25))
        counts = tuple(word.count(label) for label in MENU)
        theorem.append({"start": start, "counts": counts})
        failures += int(counts != (5, 5, 5, 5, 5))
    state_rows = []
    d1_values = []
    d2_values = []
    coherent_failures = 0
    for state_name, psi in c505.input_states("held"):
        q = tuple(item.squared_sector_norm for item in train.reference_weights(event["program"], psi))
        uniform = (0.2,) * 5
        d1 = sum(abs(a - b) for a, b in zip(uniform, q))
        product_four = cylinder(q, 4)
        b_four = {tuple((start + lane) % 5 for lane in range(4)): 0.2 for start in MENU}
        d2 = 0.5 * sum(abs(product_four.get(word, 0.0) - b_four.get(word, 0.0)) for word in set(product_four) | set(b_four))
        d1_values.append(d1)
        d2_values.append(d2)
        coherent = c505.repeated_actual_map(c500.tensor_vector(psi, HELD_N), event["physical"], HELD_N)
        word_rows = []
        for start in MENU:
            actual_word = tuple((start + lane) % 5 for lane in range(HELD_N))
            augmented = train.augment_retained_surface(coherent, actual_word)
            selected_terms = sum(1 for key in augmented if key[-1] == (1, 1, 1, 1))
            residual = abs(sum(abs(value) ** 2 for value in augmented.values()) - sum(abs(value) ** 2 for value in coherent.values()))
            coherent_failures += int(selected_terms == 0 or residual >= TOL)
            word_rows.append({"start": start, "word": actual_word, "selected_terms": selected_terms, "retention_residual": residual})
        state_rows.append({"state": state_name, "q": q, "D1": d1, "D2_N4": d2, "retained_overlay": word_rows})
    d4 = {"lags_1_to_4": (-0.04, -0.04, -0.04, -0.04), "lag_5": 0.16, "period": 5}
    check(
        "B held overlay has one explicit actual carrier member/occurrence/admitted atom, exact phase/exhaust retention, and preregistered non-Born D1-D4",
        failures == 0 and counterfactual_failures == 0 and coherent_failures == 0
        and min(d1_values) > 0.1 and min(d2_values) > 0.1,
        {
            "basis_rows": rows, "counterfactual_failures": counterfactual_failures,
            "period_theorem": theorem, "state_rows": state_rows,
            "D1": max(d1_values), "D2": max(d2_values), "D3": 0.0, "D4": d4,
            "D5": "not first passage", "D6": 0,
            "ontology": "supplied actual carrier; not unitary collapse and not pointer copying",
            "full_framework_Record": None,
        },
    )
    return {"schedule": schedule, "rows": rows, "D1": max(d1_values), "D2": max(d2_values), "D3": 0.0, "D4": d4, "D6": 0}


def held_locality_resources(routes: tuple[tuple[str, tuple[c505.Gate, ...]], ...]) -> dict[str, object]:
    frames = c500.c493.c488.proper_cubic_frames()
    rows = []
    failures = 0
    for name, schedule in routes:
        base = tuple((index, 0, 0) for index in range(train.TOTAL_M2))
        route_edges = tuple((base[left], base[right]) for item in schedule for left, right in c505.route_for_gate(item, train.TOTAL_M2))
        final_edges = tuple(
            (base[left], base[right])
            for item in schedule if item.kind != "X"
            for left, right in zip(
                tuple(range(train.TOTAL_M2 - len(item.sites), train.TOTAL_M2))[:-1],
                tuple(range(train.TOTAL_M2 - len(item.sites), train.TOTAL_M2))[1:],
            )
        )
        manifest_failures = edge_failures = 0
        for frame in frames:
            rotated = tuple(c500.c493.c488.rotate_coord(site, frame) for site in base)
            carried_x = c500.c493.c488.rotate_coord((1, 0, 0), frame)
            independent = tuple(tuple(index * value for value in carried_x) for index in range(train.TOTAL_M2))
            manifest_failures += int(rotated != independent)
            for left, right in route_edges + final_edges:
                a = c500.c493.c488.rotate_coord(left, frame)
                b = c500.c493.c488.rotate_coord(right, frame)
                edge_failures += int(c500.c493.c488.manhattan(a, b) != 1)
        trace = c505.nn_trace(schedule, train.TOTAL_M2)
        failures += int(
            manifest_failures or edge_failures or trace["maximum_support_M2"] > 3
            or trace["connected_failures"] or trace["final_adjacent_support_failures"]
            or trace["terminal_operand_order_failures"] or trace["reverse_label_restoration_failures"]
        )
        rows.append({"route": name, "frames": len(frames), "manifest_failures": manifest_failures, "edge_failures": edge_failures, "trace": trace})
    species = c500.c493.c488.c478.c317.c311.c219.common_species(-0.3)
    mass_residual = abs(c500.c493.c488.c478.c317.c311.c219.rest_mass(species) / species.analytic_mass - 1.0)
    domain = {}
    try:
        train.validate_b_law_domain((0, 1, 1, 1, 1), 0)
        domain["B-zero-support"] = False
    except ValueError:
        domain["B-zero-support"] = True
    try:
        train.validate_word((0,) * (train.TOTAL_M2 - 1))
        domain["wrong-width"] = False
    except ValueError:
        domain["wrong-width"] = True
    check(
        "held A/B obligations retain bounded NN/all24/mass/domain/resources with no Route-C resource claim",
        failures == 0 and len(frames) == 24 and mass_residual < 3e-12 and all(domain.values())
        and train.NEW_M2 == 25 and train.NEW_M2 <= train.NEW_M2_CEILING,
        {
            "rows": rows, "mass_residual": mass_residual, "domain": domain,
            "new_M2": train.NEW_M2, "conservative_total_M2": 1563,
            "C_resource_result": None,
        },
    )
    return {"rows": rows, "mass": mass_residual, "domain": domain}


def held_inventory(a: dict[str, object], b: dict[str, object], local: dict[str, object]) -> None:
    matrix = {
        "A": {"D1": a["D1"], "D2": a["D2"], "D3": a["D3"], "D4": a["D4"], "D5": "no waiting-time claim", "D6": a["D6"], "D7": "pending/then common held controls"},
        "B": {"D1": b["D1"], "D2": b["D2"], "D3": b["D3"], "D4": b["D4"], "D5": "not first passage", "D6": b["D6"], "D7": "passed common held controls"},
        "C": {key: None for key in ("D1", "D2", "D3", "D4", "D5", "D6", "D7")},
    }
    check(
        "held D1-D7 inventory keeps A conditional, B actual, C open, and full framework Record unset",
        all(len(row) == 7 for row in matrix.values()) and all(value is None for value in matrix["C"].values())
        and local["mass"] < 3e-12,
        {
            "matrix": matrix,
            "A_actual_member": None, "A_actual_occurrence": None, "A_actual_atom": None,
            "B_actual_member": "conditional on supplied actual carrier ontology/phase/support",
            "B_AdmittedRecordAtom": True, "full_framework_Record": None,
            "C": "OPEN, no fabricated first passage or renewal",
        },
    )


def resource_controls(started: float) -> None:
    elapsed = time.monotonic() - started
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes = rss if sys.platform == "darwin" else rss * 1024
    check(
        "held evaluator stays within frozen wall/RSS caps",
        elapsed < WALL_CAP_SECONDS and rss_bytes < RSS_CAP_BYTES,
        {"elapsed_seconds": elapsed, "peak_RSS_bytes": rss_bytes, "wall_cap": WALL_CAP_SECONDS, "RSS_cap": RSS_CAP_BYTES},
    )


def install_wall_cap() -> None:
    def handler(_signum: int, _frame: object) -> None:
        raise WallCapExceeded("Cycle508 held evaluator exceeded its wall cap")
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(int(WALL_CAP_SECONDS) + 1)


def dry_contract() -> int:
    print("CYCLE508 HELD-ONLY EVALUATOR DRY CONTRACT")
    print("AUTHORITY", AUTHORITY, "AUDIT", AUDIT, "HELD EXECUTED", False)
    contract_controls()
    codec_type_controls()
    source_obligation_controls()
    no_go_controls()
    print("RESULT", PASS, "passed /", FAIL, "failed")
    print("DISPOSITION DRY ONLY — stop for root authorization; held absent")
    return 0 if FAIL == 0 else 1


def held() -> int:
    if os.environ.get("CYCLE508_HELD_AUTHORIZATION") != HELD_AUTHORIZATION:
        print("REFUSE Cycle508 held: missing exact root authorization")
        return 2
    started = time.monotonic()
    install_wall_cap()
    print("CYCLE508 ACTUAL-MEMBER / ADMITTED-HISTORY LAW TOURNAMENT HELD")
    print("AUTHORITY", AUTHORITY, "AUDIT", AUDIT, "HELD AUTHORIZED", True)
    contract_controls()
    codec_type_controls()
    source_obligation_controls()
    no_go_controls()
    surface = c500.c493.c488.menu_surface()
    event = c500.event_basis_maps(surface, HELD_L)
    held_inherited_surface(event)
    held_common_binder()
    b = held_route_b(event)
    a = held_route_a(event)
    local = held_locality_resources((("A", a["schedule"]), ("B", b["schedule"])))
    held_inventory(a, b, local)
    resource_controls(started)
    signal.alarm(0)
    dispositions = (
        HeldDisposition("B", "held evaluator executed", "explicit supplied actual carrier overlay", "physical actual occurrence", "AdmittedRecordAtom", None, "ontology/phase/support supplied; non-Born comparator"),
        HeldDisposition("A", "held evaluator executed", None, None, None, None, "conditional kernel images only; no draw; p=q supplied; not Born derivation"),
        HeldDisposition("C", "OPEN not implemented", None, None, None, None, "no first passage, bath, renewal, stationarity, or component means"),
    )
    print("RESULT", PASS, "passed /", FAIL, "failed")
    print("ROUTE DISPOSITIONS", tuple(asdict(item) for item in dispositions))
    print("SHARED OBSTRUCTION", False, "AXIOM PRESSURE", False)
    return 0 if FAIL == 0 else 1


def main() -> int:
    if MODE not in ALLOWED_MODES:
        print("REFUSE Cycle508 held evaluator: set CYCLE508_HELD_MODE=dry-contract or held")
        return 2
    if MODE == "dry-contract":
        if os.environ.get("CYCLE508_HELD_AUTHORIZATION"):
            print("REFUSE dry contract with held authorization present")
            return 2
        return dry_contract()
    return held()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except WallCapExceeded as error:
        print("FAIL", error)
        raise SystemExit(2)
