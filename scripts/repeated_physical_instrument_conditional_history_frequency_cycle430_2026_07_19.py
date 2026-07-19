#!/usr/bin/env python3
"""Cycle 430: repeated physical instrument and conditional-history laws.

Repeat independent fresh copies of the constructed Cycle-427 scalar class-13
instrument.  Every detector word receives an explicit factorized physical
branch map/effect/norm.  Separately, an explicitly supplied independent-product
law attaches B0, B1, or trace/amplitude-square candidate weights, and every
basis word receives a conditional Cycle-364 typed-Record history adapter.

No detector word is selected.  Physical norm, candidate grade, product-law
weight, conditional Record corpus, empirical word frequency, sampler, and
actual history remain distinct.  Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import reduce
from hashlib import sha256
from itertools import product
from math import comb
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_absorption_instrument_effect_registry_bridge_cycle427_2026_07_19 as c427


c424 = c427.c424
c364 = c424.c364
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "REPEATED_PHYSICAL_INSTRUMENT_CONDITIONAL_HISTORY_FREQUENCY_"
    "CYCLE430_NOTE_2026-07-19.md"
)
CYCLE351_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_TYPED_RECORD_BORN_CORPUS_TOURNAMENT_SYNTHESIS_CYCLE351_NOTE_2026-07-18.md"
)
CYCLE367_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RECORD_FORMATION_LAW_TOURNAMENT_SYNTHESIS_CYCLE367_NOTE_2026-07-18.md"
)
CYCLE403_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SOURCE_RESPONSE_ACTUALIZATION_LAW_TOURNAMENT_CYCLE403_NOTE_2026-07-18.md"
)
CYCLE424_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ABSORPTION_EVENT_RECORD_TIME_BRIDGE_CYCLE424_NOTE_2026-07-19.md"
)
CYCLE427_NOTE = c427.NOTE

TRAIN_N = (1, 2, 3)
HELD_N = 6
HELD_WORD = (1, 0, 1, 0, 0, 1)
TRIAL_M2 = 3
OUTCOME_M2 = 1
CLOSE_M2 = 1
TOL = 5e-10
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0

LAW_GRADES = {
    "B0": Fraction(0, 96),
    "B1": Fraction(7, 96),
    "trace/amplitude-square": Fraction(39, 100),
}

Word = tuple[int, ...]


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    required = (
        "authority: none",
        "audit: unset",
        "n=1,2,3 training",
        "held n=6",
        "every detector basis word",
        "factorized physical branch map",
        "physical branch norm",
        "b0 click grade 0/96",
        "b1 click grade 7/96",
        "trace/amplitude-square click grade 39/100",
        "explicitly supplied independent-product law",
        "typed precommit payload for click and no-click",
        "supplied trial-valid close",
        "cycle-364 formation is conditional and unselected",
        "all 24 proper-cubic frames",
        "101001",
        "not observed or realized",
        "binomial concentration or frequency does not follow",
        "no no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-430 note freezes the repeated-instrument and conditional-history contract", not missing, missing)


def source_contract() -> None:
    c351 = normalized(CYCLE351_NOTE)
    c367 = normalized(CYCLE367_NOTE)
    c403 = normalized(CYCLE403_NOTE)
    c424_note = normalized(CYCLE424_NOTE)
    c427_note = normalized(CYCLE427_NOTE)
    check(
        "the inherited corpus, formation, actualization, detector, and instrument boundaries remain explicit",
        "grade-blind finite record-tag corpora" in c351
        and "supplied occurrence/commit/future-fibre inputs" in c351
        and "actual-history sampling" in c351
        and "none is selected by the framework" in c367
        and "complete lawful 30-bit payload" in c367
        and "faithful close" in c367
        and "no law or outcome branch is selected" in c403
        and "sector weight, not probability or born weight" in c403
        and "reversible absorption is not a record" in c424_note
        and "branch weight is not occurrence, probability, or a born weight" in c424_note
        and "actual cycle-424 unitary" in c427_note
        and "deliberately supplied and inverse-designed" in c427_note,
        {
            "typed_corpus_requires_supplied_actualization": True,
            "Cycle364_selected": False,
            "detector_branch_selected": False,
            "native_scalar_instrument": "constructed Cycle427 class13 seam",
        },
    )


@dataclass(frozen=True)
class LocalScalarInstrument:
    direction: int
    apparatus: np.ndarray
    update: np.ndarray
    stinespring: np.ndarray
    kraus: tuple[np.ndarray, np.ndarray]
    effects: tuple[np.ndarray, np.ndarray]


def local_scalar_instrument(
    direction: int = c424.EDGE_DIRECTION,
    *,
    delete_detector: bool = False,
) -> LocalScalarInstrument:
    nominal = c427.one_update(c427.ANGLE, direction)
    click_final = np.zeros(len(c427.ONE_BASIS), dtype=complex)
    click_final[c427.ONE_INDEX[(0, 0, 1)]] = 1
    vacuum_final = np.zeros(len(c427.ONE_BASIS), dtype=complex)
    vacuum_final[c427.ONE_INDEX[(0, 0, 0)]] = 1
    apparatus = (
        np.sqrt(c427.SCALAR_WEIGHT) * (nominal.conj().T @ click_final)
        + np.sqrt(1 - c427.SCALAR_WEIGHT) * (nominal.conj().T @ vacuum_final)
    )
    c427.validate_detector_blank(apparatus, c427.ONE_BASIS)
    physical = c427.one_update(
        c427.ANGLE, direction, delete_detector=delete_detector
    )
    logical_embedding = np.kron(np.eye(2), apparatus.reshape(-1, 1))
    joint_update = np.kron(np.eye(2), physical)
    stinespring = joint_update @ logical_embedding
    extractors = tuple(
        np.kron(
            np.eye(2),
            c427.branch_extractor(c427.ONE_BASIS, (detector,)),
        )
        for detector in (0, 1)
    )
    kraus = tuple(extractor @ stinespring for extractor in extractors)
    effects = tuple(operator.conj().T @ operator for operator in kraus)
    return LocalScalarInstrument(direction, apparatus, physical, stinespring, kraus, effects)


def detector_words(count: int) -> tuple[Word, ...]:
    if count not in TRAIN_N + (HELD_N,):
        raise ValueError("word count leaves frozen N=1,2,3 training / N=6 held domain")
    return tuple(product((0, 1), repeat=count))


def validate_word(word: Word, count: int) -> None:
    if not isinstance(word, tuple) or len(word) != count or any(bit not in (0, 1) for bit in word):
        raise ValueError("detector word has the wrong held/train width or a non-bit value")


def tensor_product(operators: tuple[np.ndarray, ...]) -> np.ndarray:
    if not operators:
        raise ValueError("a tensor branch needs at least one local map")
    return reduce(np.kron, operators)


def physical_scalar(word: Word) -> Fraction:
    return Fraction(39, 100) ** sum(word) * Fraction(61, 100) ** (len(word) - sum(word))


@dataclass(frozen=True)
class FactorizedBranchMap:
    word: Word
    local_output_dimension: int
    local_input_dimension: int
    physical_effect_scalar: Fraction

    @property
    def clicks(self) -> int:
        return sum(self.word)

    @property
    def input_dimension(self) -> int:
        return self.local_input_dimension ** len(self.word)

    @property
    def formal_output_dimension(self) -> int:
        return self.local_output_dimension ** len(self.word)

    def effect(self) -> np.ndarray:
        return float(self.physical_effect_scalar) * np.eye(self.input_dimension, dtype=complex)


def branch_map(word: Word, local: LocalScalarInstrument) -> FactorizedBranchMap:
    validate_word(word, len(word))
    return FactorizedBranchMap(
        word,
        local.kraus[0].shape[0],
        local.kraus[0].shape[1],
        physical_scalar(word),
    )


def normalized_probe(dimension: int) -> np.ndarray:
    values = np.arange(1, dimension + 1, dtype=float) + 1j * np.arange(dimension, 0, -1, dtype=float)
    return values / np.linalg.norm(values)


def independent_physical_copy_controls() -> tuple[LocalScalarInstrument, dict[int, tuple[FactorizedBranchMap, ...]]]:
    print("\nINDEPENDENT FRESH PHYSICAL COPIES")
    local = local_scalar_instrument()
    local_completeness = float(np.linalg.norm(sum(local.effects) - np.eye(2)))
    local_stinespring = float(np.linalg.norm(local.stinespring.conj().T @ local.stinespring - np.eye(2)))
    certificates = {}
    rows = []
    failures = 0
    for count in TRAIN_N + (HELD_N,):
        branches = tuple(branch_map(word, local) for word in detector_words(count))
        certificates[count] = branches
        probe = normalized_probe(2**count)
        completeness = np.zeros((2**count, 2**count), dtype=complex)
        maximum_effect_residual = 0.0
        maximum_norm_residual = 0.0
        direct_map_residual = 0.0
        for branch in branches:
            effect = branch.effect()
            completeness += effect
            expected = float(branch.physical_effect_scalar)
            maximum_norm_residual = max(
                maximum_norm_residual,
                abs(float(np.vdot(probe, effect @ probe).real) - expected),
            )
            if count <= max(TRAIN_N):
                direct = tensor_product(tuple(local.kraus[bit] for bit in branch.word))
                direct_effect = direct.conj().T @ direct
                maximum_effect_residual = max(
                    maximum_effect_residual,
                    float(np.linalg.norm(direct_effect - effect)),
                )
                direct_map_residual = max(
                    direct_map_residual,
                    abs(float(np.linalg.norm(direct @ probe) ** 2) - expected),
                )
        completeness_residual = float(np.linalg.norm(completeness - np.eye(2**count)))
        failures += int(
            completeness_residual > 4e-12
            or maximum_effect_residual > 5e-12
            or maximum_norm_residual > 4e-13
            or direct_map_residual > 5e-13
        )
        rows.append({
            "N": count,
            "held": count == HELD_N,
            "detector_words": len(branches),
            "logical_input_dimension": 2**count,
            "formal_physical_branch_output_dimension": 30**count,
            "completeness_residual": completeness_residual,
            "maximum_direct_Kword_effect_residual": maximum_effect_residual if count <= 3 else None,
            "maximum_branch_norm_residual": maximum_norm_residual,
            "maximum_direct_Kword_norm_residual": direct_map_residual if count <= 3 else None,
            "direct_dense_Kword_executed": count <= 3,
            "factorized_Kword_executed": True,
        })
    held = next(branch for branch in certificates[HELD_N] if branch.word == HELD_WORD)
    check(
        "N=1,2,3 training and held N=6 enumerate every physical detector word with explicit fresh-copy branch maps, effects, and norms",
        local_completeness < 3e-12
        and local_stinespring < 3e-12
        and failures == 0
        and held.clicks == 3
        and held.physical_effect_scalar == Fraction(13464285939, 10**12),
        {
            "local_no_click_effect_residual": float(np.linalg.norm(local.effects[0] - 0.61 * np.eye(2))),
            "local_click_effect_residual": float(np.linalg.norm(local.effects[1] - 0.39 * np.eye(2))),
            "local_completeness_residual": local_completeness,
            "local_Stinespring_residual": local_stinespring,
            "rows": rows,
            "held_word": HELD_WORD,
            "held_click_count": held.clicks,
            "held_physical_branch_norm_exact": str(held.physical_effect_scalar),
            "held_physical_branch_norm_decimal": float(held.physical_effect_scalar),
            "physical_branch_norm_called_occurrence_or_probability": False,
            "failures": failures,
        },
    )
    return local, certificates


def word_weight(word: Word, click_grade: Fraction) -> Fraction:
    if not isinstance(click_grade, Fraction) or not 0 <= click_grade <= 1:
        raise ValueError("a candidate click grade must be one exact Fraction in [0,1]")
    validate_word(word, len(word))
    return click_grade ** sum(word) * (1 - click_grade) ** (len(word) - sum(word))


def independent_product_law_controls(certificates: dict[int, tuple[FactorizedBranchMap, ...]]) -> dict[str, object]:
    print("\nSUPPLIED INDEPENDENT-PRODUCT CANDIDATE LAWS")
    rows = []
    failures = 0
    tables = {}
    for name, grade in LAW_GRADES.items():
        tables[name] = {}
        for count in TRAIN_N + (HELD_N,):
            words = detector_words(count)
            fine = {word: word_weight(word, grade) for word in words}
            tables[name][count] = fine
            total = sum(fine.values(), Fraction(0))
            bins = {
                clicks: sum(weight for word, weight in fine.items() if sum(word) == clicks)
                for clicks in range(count + 1)
            }
            expected_bins = {
                clicks: comb(count, clicks) * grade**clicks * (1 - grade) ** (count - clicks)
                for clicks in range(count + 1)
            }
            exchange_failures = sum(
                len({fine[word] for word in words if sum(word) == clicks}) != 1
                for clicks in range(count + 1)
            )
            marginal_failures = 0
            if count > 1:
                previous = tables[name][count - 1] if count - 1 in tables[name] else {
                    word: word_weight(word, grade)
                    for word in tuple(product((0, 1), repeat=count - 1))
                }
                marginal_failures = sum(
                    fine[prefix + (0,)] + fine[prefix + (1,)] != weight
                    for prefix, weight in previous.items()
                )
            failures += int(total != 1 or bins != expected_bins or exchange_failures or marginal_failures)
            rows.append({
                "law": name,
                "N": count,
                "held": count == HELD_N,
                "fine_words": len(words),
                "normalization": str(total),
                "count_bins": tuple(str(bins[index]) for index in range(count + 1)),
                "exchangeability_failures": exchange_failures,
                "marginal_failures": marginal_failures,
                "refinement_bin_to_fine_residuals": tuple(str(bins[index] - expected_bins[index]) for index in range(count + 1)),
            })

    held_weights = {name: table[HELD_N][HELD_WORD] for name, table in tables.items()}
    held_bins = {
        name: comb(HELD_N, sum(HELD_WORD)) * value
        for name, value in held_weights.items()
    }
    exact_separations = {
        "B1_minus_B0_word": held_weights["B1"] - held_weights["B0"],
        "trace_minus_B1_word": held_weights["trace/amplitude-square"] - held_weights["B1"],
        "trace_to_B1_nonzero_ratio": held_weights["trace/amplitude-square"] / held_weights["B1"],
        "B1_minus_B0_click_grade": LAW_GRADES["B1"] - LAW_GRADES["B0"],
        "trace_minus_B1_click_grade": LAW_GRADES["trace/amplitude-square"] - LAW_GRADES["B1"],
    }
    physical_held = next(
        branch.physical_effect_scalar
        for branch in certificates[HELD_N]
        if branch.word == HELD_WORD
    )
    reversed_word = tuple(reversed(HELD_WORD))
    reversed_order_equal_weights = all(
        tables[name][HELD_N][reversed_word] == held_weights[name]
        for name in LAW_GRADES
    )
    grade_deleted_prediction = None
    check(
        "the supplied independent-product laws normalize, coarse-grain, exchange, refine, and marginalize exactly while sharply separating the frozen held word",
        failures == 0
        and held_weights["B0"] == 0
        and held_weights["B1"] == Fraction(241804367, 782757789696)
        and held_weights["trace/amplitude-square"] == Fraction(13464285939, 10**12)
        and held_bins["B1"] == Fraction(1209021835, 195689447424)
        and held_bins["trace/amplitude-square"] == Fraction(13464285939, 50000000000)
        and physical_held == held_weights["trace/amplitude-square"]
        and exact_separations["trace_to_B1_nonzero_ratio"] > 40
        and reversed_word != HELD_WORD
        and reversed_order_equal_weights
        and grade_deleted_prediction is None,
        {
            "candidate_click_grades": {
                "B0": "0/96",
                "B1": "7/96",
                "trace/amplitude-square": "39/100",
            },
            "independent_product_law_supplied": True,
            "rows": rows,
            "held_word": HELD_WORD,
            "reversed_held_word": reversed_word,
            "reversed_order_equal_candidate_weights": reversed_order_equal_weights,
            "held_word_declared_observed_or_realized": False,
            "held_empirical_count_frequency": str(Fraction(sum(HELD_WORD), HELD_N)),
            "held_word_weights": {name: str(value) for name, value in held_weights.items()},
            "held_count_bin_weights": {name: str(value) for name, value in held_bins.items()},
            "exact_separations": {name: str(value) for name, value in exact_separations.items()},
            "physical_norm_matches_trace_candidate": physical_held == held_weights["trace/amplitude-square"],
            "candidate_grade_or_product_law_selected": False,
            "grade_deleted_prediction": grade_deleted_prediction,
            "binomial_concentration_or_frequency_theorem_claimed": False,
            "failures": failures,
        },
    )
    return {"tables": tables, "held_weights": held_weights, "held_bins": held_bins}


@dataclass(frozen=True)
class PrecommitOutcomePayload:
    event: c424.DetectorEventCandidate
    trial: int
    trial_valid_close: int

    @property
    def detector_outcome(self) -> int:
        return self.event.detected

    @property
    def is_Record(self) -> bool:
        return False


def trial_bits(trial: int) -> tuple[int, ...]:
    if not 0 <= trial < 2**TRIAL_M2:
        raise ValueError("trial label leaves its three-M2 held register")
    return tuple((trial >> bit) & 1 for bit in range(TRIAL_M2))


def precommit_payload_table(count: int):
    fixture = c364.c342.c338.build_fixture(6)
    payload_words = c364.words(fixture, 2 * count)
    table = {}
    for trial in range(count):
        site = (trial, 0, 0)
        table[trial] = tuple(
            PrecommitOutcomePayload(
                c424.DetectorEventCandidate(
                    event_id=f"Cycle430_trial{trial}_outcome{outcome}",
                    detector_site=site,
                    detected=outcome,
                    payload=payload_words[2 * trial + outcome],
                    source_case="Cycle430_repeated_scalar_instrument_basis_sector",
                ),
                trial,
                1,
            )
            for outcome in (0, 1)
        )
        for item in table[trial]:
            c424.validate_event(item.event)
            trial_bits(item.trial)
    return fixture, table


def conditional_history(
    fixture,
    table: dict[int, tuple[PrecommitOutcomePayload, PrecommitOutcomePayload]],
    word: Word,
    *,
    delete_close_trial: int | None = None,
):
    validate_word(word, len(table))
    state = c364.FormationState()
    statuses = []
    proposals = []
    atoms = []
    for trial, outcome in enumerate(word):
        item = table[trial][outcome]
        predecessors = () if trial == 0 else ((trial - 1, 0, 0),)
        close = 0 if delete_close_trial == trial else item.trial_valid_close
        proposal = c364.proposal(
            (trial, 0, 0),
            item.event.payload,
            predecessors,
            close=close,
        )
        answer = c364.apply_candidate_law(fixture, state, proposal)
        statuses.append(answer.status)
        proposals.append(proposal)
        if answer.formed is not None:
            state = answer.state
        atoms.append(
            item.event.payload
            + (item.detector_outcome,)
            + trial_bits(trial)
            + (close,)
        )
    digest = sha256(bytes(bit for atom in atoms for bit in atom)).hexdigest()
    return state, tuple(statuses), tuple(proposals), digest


def typed_precommit_and_conditional_corpus_controls(product_laws: dict[str, object]) -> dict[str, object]:
    print("\nTYPED PRECOMMIT PAYLOADS / CONDITIONAL CYCLE364 CORPORA")
    fixture, table = precommit_payload_table(HELD_N)
    both_outcome_rows = []
    for outcome in (0, 1):
        item = table[0][outcome]
        formed = c364.apply_candidate_law(
            fixture,
            c364.FormationState(),
            c364.proposal((0, 0, 0), item.event.payload, close=1),
        )
        closed_deleted = c364.apply_candidate_law(
            fixture,
            c364.FormationState(),
            c364.proposal((0, 0, 0), item.event.payload, close=0),
        )
        both_outcome_rows.append({
            "outcome": outcome,
            "typed_precommit": not item.is_Record and item.event.reversible_precommit,
            "trial_valid_close_supplied": item.trial_valid_close,
            "conditional_status_with_close": formed.status,
            "status_without_close": closed_deleted.status,
        })

    histories = {}
    failures = 0
    for word in detector_words(HELD_N):
        state, statuses, proposals, digest = conditional_history(fixture, table, word)
        histories[word] = {
            "state": state,
            "statuses": statuses,
            "proposals": proposals,
            "hash": digest,
        }
        failures += int(len(state.records) != HELD_N or any(status != "formed" for status in statuses))
    close_deleted = conditional_history(
        fixture, table, HELD_WORD, delete_close_trial=2
    )
    close_blocked = sum(status.startswith("blocked:") for status in close_deleted[1])

    frame_failures = mapping_failures = locality_failures = 0
    reference = histories[HELD_WORD]
    reversed_word = tuple(reversed(HELD_WORD))
    reversed_order_hash_distinct = (
        histories[HELD_WORD]["hash"] != histories[reversed_word]["hash"]
    )
    for frame in c364.c362.c353.proper_cubic_frames():
        rotated_fixture, mapping, mapped_failures = c364.c342.mapped_fixture(fixture, frame)
        mapping_failures += mapped_failures
        state = c364.FormationState()
        for proposal in reference["proposals"]:
            moved = c364.transform_proposal(proposal, frame, (0, 0, 0), mapping)
            answer = c364.apply_candidate_law(rotated_fixture, state, moved)
            if answer.formed is not None:
                state = answer.state
            locality_failures += sum(
                c364.distance(moved.site, predecessor) > c364.LOCAL_RADIUS
                for predecessor in moved.readiness.predecessors
            )
        expected = c364.transform_state(reference["state"], frame, (0, 0, 0), mapping)
        frame_failures += int(state != expected)

    attachments = {
        name: {
            word: (history["hash"], product_laws["tables"][name][HELD_N][word])
            for word, history in histories.items()
        }
        for name in LAW_GRADES
    }
    normalization = {
        name: sum(weight for _digest, weight in values.values())
        for name, values in attachments.items()
    }
    check(
        "both detector labels have typed precommit payloads, and every held basis word has a covariant conditional Cycle364 corpus only when a trial-valid close is supplied",
        all(row["typed_precommit"] for row in both_outcome_rows)
        and all(row["conditional_status_with_close"] == "formed" for row in both_outcome_rows)
        and all("faithful_close" in row["status_without_close"] for row in both_outcome_rows)
        and failures == 0
        and len({value["hash"] for value in histories.values()}) == 2**HELD_N
        and reversed_order_hash_distinct
        and close_blocked >= 1
        and len(c364.c362.c353.proper_cubic_frames()) == 24
        and frame_failures == mapping_failures == locality_failures == 0
        and all(value == 1 for value in normalization.values()),
        {
            "both_outcomes": both_outcome_rows,
            "held_basis_words": len(histories),
            "unique_conditional_corpus_hashes": len({value["hash"] for value in histories.values()}),
            "reversed_equal_count_word": reversed_word,
            "reversed_order_corpus_hash_distinct": reversed_order_hash_distinct,
            "conditional_Records_per_complete_branch": HELD_N,
            "whole_payload_outcome_trial_close_word_is_Record": False,
            "close_deleted_blocked_statuses": close_blocked,
            "proper_cubic_frames": 24,
            "payload_mapping_failures": mapping_failures,
            "formation_frame_failures": frame_failures,
            "locality_failures": locality_failures,
            "candidate_law_attachment_normalizations": {name: str(value) for name, value in normalization.items()},
            "Cycle364_candidate_selected": False,
            "detector_word_selected": False,
            "actual_history_or_sampler": None,
            "failures": failures,
        },
    )
    return {"fixture": fixture, "table": table, "histories": histories, "attachments": attachments}


def frame_deletion_domain_and_support_controls(
    local: LocalScalarInstrument,
    certificates: dict[int, tuple[FactorizedBranchMap, ...]],
    corpus: dict[str, object],
) -> None:
    frame_rows = []
    for frame in c427.c423.c210.proper_cubic_frames():
        directions = c427.c423.c210.direction_permutation(frame)
        target_direction = int(np.argmax(directions[:, c424.EDGE_DIRECTION]))
        moved = local_scalar_instrument(target_direction)
        representation = c427.frame_representation(
            c427.ONE_BASIS, c427.ONE_INDEX, frame
        )
        frame_rows.append((
            float(np.linalg.norm(representation @ local.apparatus - moved.apparatus)),
            max(float(np.linalg.norm(left - right)) for left, right in zip(local.effects, moved.effects)),
        ))

    detector_deleted = local_scalar_instrument(delete_detector=True)
    held_nominal = next(branch for branch in certificates[HELD_N] if branch.word == HELD_WORD)
    held_deleted_scalar = (
        Fraction(0) if HELD_WORD[0] else Fraction(1)
    ) * physical_scalar(HELD_WORD[1:])
    detector_deleted_click = float(np.linalg.norm(detector_deleted.effects[1]))

    dirty = np.zeros(len(c427.ONE_BASIS), dtype=complex)
    dirty[c427.ONE_INDEX[(0, 0, 1)]] = 1
    invalid = (
        lambda: detector_words(0),
        lambda: detector_words(4),
        lambda: validate_word((0, 2), 2),
        lambda: validate_word((0,), HELD_N),
        lambda: word_weight((0, 1), Fraction(-1, 2)),
        lambda: word_weight((0, 1), Fraction(3, 2)),
        lambda: word_weight((0, 1), 0.5),
        lambda: trial_bits(8),
        lambda: c427.validate_detector_blank(dirty, c427.ONE_BASIS),
    )
    rejected = 0
    for call in invalid:
        try:
            call()
        except (TypeError, ValueError, OverflowError, IndexError):
            rejected += 1

    omitted_factor_total = Fraction(2, 1)
    support_rows = tuple({
        "N": count,
        "held": count == HELD_N,
        "independent_physical_instrument_M2": 16 * count,
        "Cycle424_transport_M2": 14 * count,
        "spectator_logical_M2": count,
        "fresh_detector_blank_M2": count,
        "conditional_payload_M2": 30 * count,
        "outcome_trial_close_interface_M2": (OUTCOME_M2 + TRIAL_M2 + CLOSE_M2) * count,
        "incremental_candidate_adapter_M2_excluding_reused_detector": (30 + TRIAL_M2 + CLOSE_M2) * count,
        "modular_instrument_plus_candidate_adapter_M2": 50 * count,
    } for count in TRAIN_N + (HELD_N,))
    check(
        "all-frame scalar covariance, detector/use deletion, lawful domains, and the fresh-copy support ledger remain explicit",
        len(frame_rows) == 24
        and max(row[0] for row in frame_rows) < 4e-12
        and max(row[1] for row in frame_rows) < 4e-12
        and detector_deleted_click == 0
        and held_deleted_scalar == 0
        and held_nominal.physical_effect_scalar > 0
        and omitted_factor_total != 1
        and rejected == len(invalid)
        and support_rows[-1]["independent_physical_instrument_M2"] == 96
        and support_rows[-1]["modular_instrument_plus_candidate_adapter_M2"] == 300,
        {
            "proper_cubic_frames": len(frame_rows),
            "maximum_apparatus_frame_residual": max(row[0] for row in frame_rows),
            "maximum_effect_frame_residual": max(row[1] for row in frame_rows),
            "detector_deleted_local_click_effect_norm": detector_deleted_click,
            "held_word_norm_with_trial0_detector_deleted": str(held_deleted_scalar),
            "nominal_held_word_norm": str(held_nominal.physical_effect_scalar),
            "N_word_normalization_if_one_product_factor_is_omitted_but_two_labels_retained": str(omitted_factor_total),
            "lawful_domain_rejections": rejected,
            "support_rows": support_rows,
            "maximum_physical_gate_support_M2": 7,
            "candidate_adapter_is_coherent_physical_Record_compiler": False,
            "minimum_resource_claim": False,
        },
    )


def semantic_inventory() -> None:
    inventory = {
        "physical_branch_norm": "derived from tensor Kraus effect",
        "candidate_numerical_grade": "B0/B1/trace input",
        "independent_product_law": "explicitly supplied",
        "conditional_Record_corpus": "Cycle364 branch-indexed candidate-law output",
        "empirical_frequency": "finite word count divided by N only",
        "sampler": None,
        "occurrence": None,
        "actual_history": None,
        "law_selector": None,
        "derived": (
            "all fine physical branch maps/effects/norms through held N6",
            "exact product-law normalization, bins, exchangeability, refinement, and marginals",
            "conditional typed precommit click/no-click payload and all-word Cycle364 corpora",
            "exact frozen held-word likelihood and candidate-frequency separations",
        ),
        "supplied": (
            "N independent scalar apparatus preparations and detector blanks",
            "B0/B1/trace click grades and independent-product interpretation",
            "trial labels, both outcome payloads, trial-valid close, provenance, readiness, and fresh sites",
            "Cycle364 candidate law and every formation/corpus binding",
        ),
        "binomial_concentration_or_frequency_from_physics": False,
        "actual_Record_claim": False,
        "observed_or_realized_word": False,
        "negative_or_no_go_claim": False,
        "minimum_content_claim": False,
        "shared_obstruction_claim": False,
        "axiom_pressure": False,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "the physical norm, numerical law, conditional corpus, empirical count, sampler, occurrence, and actual-history layers remain distinct",
        inventory["sampler"] is None
        and inventory["occurrence"] is None
        and inventory["actual_history"] is None
        and inventory["law_selector"] is None
        and not inventory["binomial_concentration_or_frequency_from_physics"]
        and not inventory["actual_Record_claim"]
        and not inventory["observed_or_realized_word"]
        and not inventory["negative_or_no_go_claim"]
        and not inventory["minimum_content_claim"]
        and not inventory["shared_obstruction_claim"]
        and not inventory["axiom_pressure"]
        and inventory["authority"] == "none"
        and inventory["audit"] == "unset",
        inventory,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 430: REPEATED PHYSICAL INSTRUMENT / CONDITIONAL HISTORY-FREQUENCY DISCRIMINATOR")
    note_contract()
    source_contract()
    local, certificates = independent_physical_copy_controls()
    product_laws = independent_product_law_controls(certificates)
    corpus = typed_precommit_and_conditional_corpus_controls(product_laws)
    frame_deletion_domain_and_support_controls(local, certificates, corpus)
    semantic_inventory()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT REPEATED_PHYSICAL_INSTRUMENT_CONDITIONAL_HISTORY_FREQUENCY_NOT_CERTIFIED")
        return 1
    print("RESULT REPEATED_PHYSICAL_INSTRUMENT_CONDITIONAL_HISTORY_FREQUENCY_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
