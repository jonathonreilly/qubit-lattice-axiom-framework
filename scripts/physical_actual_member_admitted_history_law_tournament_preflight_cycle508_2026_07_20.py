#!/usr/bin/env python3
"""Cycle 508 contract-only preflight for actual-member/admitted-history laws.

This runner freezes inputs, manifests, types, route interfaces, and test
obligations.  It deliberately refuses train and held candidate-law execution.
No stochastic draw, hidden-carrier trajectory, bath trajectory, Kraus state,
or candidate-law prediction is constructed here.
"""

from __future__ import annotations

import ast
from dataclasses import asdict, dataclass
from hashlib import sha256
from itertools import permutations, product
import inspect
import json
import os
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ACTUAL_MEMBER_ADMITTED_HISTORY_LAW_TOURNAMENT_PREFLIGHT_CYCLE508_NOTE_2026-07-20.md"
)
AUTHORITY = "none"
AUDIT = "unset"
MODE = os.environ.get("CYCLE508_MODE", "preflight")
PASS = 0
FAIL = 0
MENU_ARITY = 5
MAX_PRIMITIVE_SUPPORT_M2 = 3
ALGEBRAIC_TOLERANCE = 2e-9
RSS_CAP_BYTES = 4 * 1024**3
WALL_CAP_SECONDS = 900.0


FROZEN = {
    "minimal axioms": "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    "realized-state primitive": "755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
    "premise registry": "b73431384495db657efaeab44d1d8e83b824908c418b115308e92eaa7212eea5",
    "production-kernel boundary": "26de173bb9e3a613145fa72e614a0e27d67bcbfb431605d0f8b376b52c724b26",
    "Born-frequency boundary": "f01676e96d4470498db667224a922847c98e0425bbdc88354513b7d61c38f081",
    "Cycle21 note": "3bfe04c7ac2416d1d4586823ef9d1f23f2c15121cca55ad75f14277b65286d31",
    "Cycle194 note": "55ff10103b6cbf2f884897af938d36c67fbcb8982a95c8c8492ec831bb8e1ca7",
    "Cycle351 note": "19a0bc407c74c4700ae6a39ccb842285419b0611477904f378c9c7fb6f170e81",
    "Cycle478 note": "87ed2bfbcff03b155496123d664050e80e01c67e668b06d751c3ecef2415652f",
    "Cycle478 runner": "b700a8d5bede8037af025d9df65b1223c0159170e2c3f21992741a3b593ab99f",
    "Cycle500 note": "0ba90e82d3759726914cf72d5f27f1687995045ce0c642e809f7bce713f79caa",
    "Cycle500 runner": "01c459cd067e4b02b60558a3c29c95a0f93b3fd1d916a27176e35128f1668a90",
    "Cycle502 note": "36e156581d5f3d3dddea1e0ce1344834bd31d65883160c3c3b04c4d4671b41c2",
    "Cycle502 runner": "5494b7fd9d1411023ac2427b92c323cea9b7c26720b3a6b8d58ee32835e1e8a9",
    "Cycle505 accepted held note": "c3e8a1220172d5052089511616ad0ca2cdf6f6db5c92dc520c03a22600e112f4",
    "Cycle505 runner": "87f96ab5c7fd9e96c91cb32de0e2dd012e60d6cce62cf90403fb91a5e041275e",
    "Cycle219 note": "999e88c014f22637caeeb904bba3c27ee5beff8f4bbf04975f625094035a28ec",
    "Cycle219 runner": "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
}

FROZEN_PATHS = {
    "minimal axioms": ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "realized-state primitive": ROOT / "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "premise registry": ROOT / "docs/audit/data/axiom_premise_nodes.json",
    "production-kernel boundary": ROOT / "docs/RECORD_PRODUCTION_KERNEL_BOUNDARY_2026-06-06.md",
    "Born-frequency boundary": ROOT / "docs/RECORD_BORN_FREQUENCY_BOUNDARY_2026-06-05.md",
    "Cycle21 note": ROOT / "docs/work_history/repo/review_feedback/CERTIFIED_RECORD_CORPUS_ERGODIC_FREQUENCY_CYCLE21_NOTE_2026-07-14.md",
    "Cycle194 note": ROOT / "docs/work_history/repo/review_feedback/CYCLE189_RECORD_CORPUS_FREQUENCY_BRIDGE_CYCLE194_NOTE_2026-07-16.md",
    "Cycle351 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_TYPED_RECORD_BORN_CORPUS_TOURNAMENT_SYNTHESIS_CYCLE351_NOTE_2026-07-18.md",
    "Cycle478 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_BORN_SUPPORT_NINE_MIXED_QUOTIENT_AUXILIARY_CYCLE478_NOTE_2026-07-19.md",
    "Cycle478 runner": ROOT / "scripts/physical_born_support_nine_mixed_quotient_auxiliary_cycle478_2026_07_19.py",
    "Cycle500 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_KRAUS_GRADE_REPEATED_HISTORY_LAW_TOURNAMENT_CYCLE500_NOTE_2026-07-20.md",
    "Cycle500 runner": ROOT / "scripts/physical_kraus_grade_repeated_history_law_tournament_cycle500_2026_07_20.py",
    "Cycle502 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_KRAUS_RECORD_LOCK_CANDIDATE_GRADE_FORMATION_TOURNAMENT_CYCLE502_NOTE_2026-07-20.md",
    "Cycle502 runner": ROOT / "scripts/physical_kraus_record_lock_candidate_grade_formation_tournament_cycle502_2026_07_20.py",
    "Cycle505 accepted held note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_KRAUS_RETAINED_CARRIER_RECORD_BINDING_TOURNAMENT_CYCLE505_NOTE_2026-07-20.md",
    "Cycle505 runner": ROOT / "scripts/physical_kraus_retained_carrier_record_binding_tournament_cycle505_2026_07_20.py",
    "Cycle219 note": ROOT / "docs/work_history/repo/review_feedback/COMMON_MATTER_FIELD_COIN_FAMILY_CYCLE219_NOTE_2026-07-16.md",
    "Cycle219 runner": ROOT / "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
}


@dataclass(frozen=True)
class CoherentCandidateSurface:
    retained_sector_count: str
    actual_member: None = None


@dataclass(frozen=True)
class OperationalGrade:
    squared_sector_norm: str
    probability: None = None


@dataclass(frozen=True)
class LawState:
    route: str
    local_M2_encoding: str


@dataclass(frozen=True)
class LawEnsembleWeight:
    candidate_law_owner: str
    relation_to_grade: str


@dataclass(frozen=True)
class ActualMemberToken:
    label: str
    law_provenance: str
    ontology: str


@dataclass(frozen=True)
class OccurrenceReceipt:
    member_provenance: str
    physical_trigger: str


@dataclass(frozen=True)
class RecordBindingCandidate:
    singleton_site_content_predicate: str
    framework_Record: None = None


@dataclass(frozen=True)
class AdmittedRecordAtom:
    occurrence_receipt: str
    binding_provenance: str


@dataclass(frozen=True)
class CertifiedCorpusBlock:
    preparation: str
    context: str
    member: str
    atom: str
    close: str


@dataclass(frozen=True)
class RepeatedProcessLaw:
    projective_family: str
    stationary_or_pointwise_obligation: str


@dataclass(frozen=True)
class EmpiricalFrequency:
    admitted_count: str
    denominator: str


@dataclass(frozen=True)
class ExecutionManifest:
    name: str
    preparations: tuple[str, ...]
    L: int
    coherent_N: int
    a_seed_envelope: int
    b_phase_period: int
    c_bath_window: int
    correlation_lags: tuple[int, ...]
    algebraic_tolerance: float
    candidate_laws_executed: bool = False


@dataclass(frozen=True)
class RouteLawInterface:
    route: str
    primary_object: str
    actual_member_provenance: str
    probability_or_weight_status: str
    genesis_or_boundary_status: str
    physical_inverse_scope: str
    repeated_history_obligation: str
    pointer_copy_sufficient: bool
    conclusion_qualification: str


@dataclass(frozen=True)
class TestObligation:
    route: str
    test_id: str
    frozen_relation: str
    train_required: bool
    held_required: bool
    result: None = None


TRAIN = ExecutionManifest(
    name="train",
    preparations=("z-plus:(1,0)", "y-plus:(1,i)/sqrt(2)"),
    L=3,
    coherent_N=2,
    a_seed_envelope=3,
    b_phase_period=5,
    c_bath_window=5,
    correlation_lags=(1, 2, 3, 4),
    algebraic_tolerance=ALGEBRAIC_TOLERANCE,
)

HELD = ExecutionManifest(
    name="held",
    preparations=("x-plus:(1,1)/sqrt(2)", "skew:(sqrt(3),i)/2"),
    L=6,
    coherent_N=4,
    a_seed_envelope=7,
    b_phase_period=5,
    c_bath_window=11,
    correlation_lags=tuple(range(1, 17)),
    algebraic_tolerance=ALGEBRAIC_TOLERANCE,
)

INHERITED_M2 = {"Cycle478": 1493, "Cycle502": 28, "Cycle505_binding": 17}
NEW_M2_CEILINGS = {"A": 256, "B": 256, "C": 1024}
CONSERVATIVE_TOTAL_CEILINGS = {
    route: sum(INHERITED_M2.values()) + ceiling
    for route, ceiling in NEW_M2_CEILINGS.items()
}


def route_a_physical_schedule_spec() -> tuple[str, ...]:
    return (
        "bounded five-port stochastic primitive",
        "retained seed word and spent receipt",
        "member provenance then occurrence then singleton binding",
        "no runtime host amplitude service",
    )


def route_b_physical_schedule_spec() -> tuple[str, ...]:
    return (
        "bounded retained five-phase hidden carrier",
        "reversible phase advance and threshold receipt",
        "explicit added hidden-carrier actuality ontology",
        "state-blind non-Born comparator",
    )


def route_c_physical_schedule_spec() -> tuple[str, ...]:
    return (
        "bounded retained first-passage collision window",
        "incoming spent losing and renewal carriers retained",
        "stationary and component-mean obligation",
        "conditional if bath state or grade-to-hazard map is supplied",
    )


ROUTES = (
    RouteLawInterface(
        route="A",
        primary_object="explicit local stochastic seed/hazard kernel",
        actual_member_provenance="candidate-law stochastic transition",
        probability_or_weight_status="p_A=q is supplied candidate-law content, never derived from grade",
        genesis_or_boundary_status="seed genesis and distribution supplied",
        physical_inverse_scope="seed preprocessing/receipt reversible; actualization has no inverse claim",
        repeated_history_obligation="projective product law only with supplied independent seeds and exact re-preparation",
        pointer_copy_sufficient=False,
        conclusion_qualification="conditional stochastic construction with supplied seeds",
    ),
    RouteLawInterface(
        route="B",
        primary_object="deterministic local hidden-carrier/threshold law",
        actual_member_provenance="explicit added carrier-designated actuality ontology",
        probability_or_weight_status="uniform phase ensemble is comparator object; actual orbit is deterministic",
        genesis_or_boundary_status="initial carrier phase/boundary supplied",
        physical_inverse_scope="carrier motion and receipts require exact inverse with exhaust retained",
        repeated_history_obligation="every-phase period-five frequency and discrepancy theorem",
        pointer_copy_sufficient=False,
        conclusion_qualification="actual/corpus comparator, deliberately non-Born",
    ),
    RouteLawInterface(
        route="C",
        primary_object="renewable local bath/first-passage law",
        actual_member_provenance="candidate-law ontic first arrival and occurrence receipt",
        probability_or_weight_status="p_C from first-passage law; p_C=q only if physical hazard theorem passes",
        genesis_or_boundary_status="conditional whenever bath measure or grade-to-hazard coupling is supplied",
        physical_inverse_scope="finite microscopic bath dynamics reversible with exhaust; actualization separately typed",
        repeated_history_obligation="projective stationary bath/corpus law plus component means or every-orbit bound",
        pointer_copy_sufficient=False,
        conclusion_qualification="conditional supplied-bath construction unless genesis/coupling are derived",
    ),
)


DISCRIMINATORS = (
    ("D1", "max over frozen preparations of L1(p_r-q)"),
    ("D2", "max N=4 total variation from product-grade cylinder; diagnostic, not universal Born condition"),
    ("D3", "maximum invariant-component mean spread"),
    ("D4", "lag-1 through lag-16 covariance and periodic spectrum"),
    ("D5", "first-passage survival, tie, no-click, and censoring residuals"),
    ("D6", "actual-member / occurrence / admitted-atom count residual"),
    ("D7", "E/G, inverse where claimed, deletion, leakage, all24, mass, and resources"),
)


TESTS = (
    TestObligation("common", "kernel_intertwiner", "E_r L_r = L_r^M2 E_r on declared code space", True, True),
    TestObligation("common", "member_occurrence_binding", "exactly one provenance member then occurrence then at most one admitted atom", True, True),
    TestObligation("common", "projective_cylinders", "N-cylinder marginal equals N-1 cylinder", True, True),
    TestObligation("common", "component_mean", "E[X_0^j|I_T]=p_r(j) or stronger every-orbit bound", True, True),
    TestObligation("common", "all24_mass_locality", "24 proper-cubic frames, mass fixture, support<=3", True, True),
    TestObligation("common", "domain_deletion_leakage", "zero/unit grade, malformed winner, collision, dirty work, deletion, leakage", True, True),
    TestObligation("common", "held_no_refit", "held changes only frozen size/preparation/window fields", False, True),
    TestObligation("A", "stochastic_kernel", "normalized p_A with zero/unit branches and p_A=q as supplied law hypothesis", True, True),
    TestObligation("A", "seed_accounting", "seed genesis/distribution supplied; seed and spent receipt retained", True, True),
    TestObligation("A", "product_qualification", "product cylinder only under supplied independent renewal and re-preparation", True, True),
    TestObligation("B", "added_actuality", "carrier ontology, not pointer copy, owns actual-member provenance", True, True),
    TestObligation("B", "period_five", "every phase has exact state-blind frequency (1/5,...,1/5)", True, True),
    TestObligation("B", "non_born_comparator", "generic held L1 response differs from q without refit", True, True),
    TestObligation("B", "retained_inverse", "phase, receipt, candidates, and exhaust exactly restore", True, True),
    TestObligation("C", "first_passage", "normalized first-hit law plus survival/tie/no-click/censoring", True, True),
    TestObligation("C", "hazard_provenance", "no host grade query; supplied coupling forces conditional classification", True, True),
    TestObligation("C", "renewal_stationarity", "recurrence, projective stationarity, invariant-component audit", True, True),
    TestObligation("C", "retained_bath_inverse", "finite reversible microdynamics restores all bath exhaust where claimed", True, True),
)


N1_FAMILIES = (
    ("local stochastic instrument and seed", "normalized state-dependent transition kernel", "one actual member plus admitted corpus and held p=q"),
    ("local hidden carrier and threshold partition", "deterministic retained carrier orbit", "pointwise member/corpus law and non-Born discriminator"),
    ("renewable local bath and first-passage field", "stationary collision flux plus first-hit invariant", "actual member, renewal, component means, and held p=q"),
    ("grade-matched deterministic symbolic history", "unique ergodicity or bounded discrepancy", "every-orbit frequencies and local physical compiler"),
    ("superselection or consistent-history sector algebra", "exact interference exclusion", "law-selected realized sector and physical occurrence"),
    ("boundary-conditioned hidden history", "global initial/final constraint", "locality/covariance compatibility and predictive boundary law"),
    ("objective stochastic field/collapse process", "local martingale or change-of-measure dynamics", "normalized member law, locality, and admitted-history calibration"),
)


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
    match = re.search(r"preflight runner SHA-256:\s*([0-9a-f]{64})", NOTE.read_text(encoding="utf-8"))
    return match.group(1) if match else None


def contract_controls() -> None:
    required = (
        "authority: none",
        "audit: unset",
        "preflight only",
        "no cycle-508 train or held execution",
        "route a — explicit local stochastic seed/hazard law",
        "p_a(j | psi)=q_j",
        "supplied candidate-law content",
        "route b — deterministic local hidden-carrier/threshold comparator",
        "explicit added hidden-carrier actuality ontology",
        "route c — renewable local bath / first-passage law",
        "conditional if bath state or grade-to-hazard coupling is supplied",
        "operationalgrade",
        "actualmembertoken",
        "occurrencereceipt",
        "admittedrecordatom",
        "repeatedprocesslaw",
        "frozen train/held",
        "all 24 proper-cubic",
        "cycle-219 one-particle mass fixture",
        "no shared obstruction or axiom pressure assessed",
    )
    body = normalized(NOTE)
    missing = tuple(phrase for phrase in required if phrase not in body)
    actual = file_sha(Path(__file__))
    declared = declared_runner_sha()
    check(
        "the Cycle508 note freezes this exact preflight runner and the actual/member/occurrence/Record/corpus firewall",
        not missing and actual == declared,
        {"missing": missing, "actual_runner_sha": actual, "declared_runner_sha": declared},
    )


def frozen_input_controls() -> None:
    observed = {name: file_sha(path) for name, path in FROZEN_PATHS.items()}
    check(
        "all accepted physics, Record, realized-state, frequency, premise-registry, and mass inputs are exact-hash frozen",
        observed == FROZEN,
        {"observed": observed, "authority": AUTHORITY, "audit": AUDIT},
    )


def type_firewall_controls() -> None:
    types = (
        CoherentCandidateSurface,
        OperationalGrade,
        LawState,
        LawEnsembleWeight,
        ActualMemberToken,
        OccurrenceReceipt,
        RecordBindingCandidate,
        AdmittedRecordAtom,
        CertifiedCorpusBlock,
        RepeatedProcessLaw,
        EmpiricalFrequency,
    )
    names = tuple(item.__name__ for item in types)
    fields = {item.__name__: tuple(item.__dataclass_fields__) for item in types}
    required_provenance = (
        "law_provenance" in fields["ActualMemberToken"]
        and "member_provenance" in fields["OccurrenceReceipt"]
        and "occurrence_receipt" in fields["AdmittedRecordAtom"]
    )
    check(
        "eleven exact types remain distinct and member/occurrence/Record admission require explicit provenance",
        len(names) == len(set(names)) == 11 and required_provenance,
        {"types": names, "fields": fields},
    )


def manifest_controls() -> None:
    train = asdict(TRAIN)
    held = asdict(HELD)
    train_digest = sha256(json.dumps(train, sort_keys=True).encode()).hexdigest()
    held_digest = sha256(json.dumps(held, sort_keys=True).encode()).hexdigest()
    check(
        "train and held manifests are exact, disjoint, no-refit, and execute no candidate law in preflight",
        TRAIN.name == "train" and HELD.name == "held"
        and not set(TRAIN.preparations) & set(HELD.preparations)
        and (TRAIN.L, TRAIN.coherent_N, TRAIN.a_seed_envelope) == (3, 2, 3)
        and (HELD.L, HELD.coherent_N, HELD.a_seed_envelope) == (6, 4, 7)
        and TRAIN.b_phase_period == HELD.b_phase_period == 5
        and (TRAIN.c_bath_window, HELD.c_bath_window) == (5, 11)
        and TRAIN.algebraic_tolerance == HELD.algebraic_tolerance == ALGEBRAIC_TOLERANCE
        and not TRAIN.candidate_laws_executed and not HELD.candidate_laws_executed,
        {"train": train, "held": held, "train_sha": train_digest, "held_sha": held_digest},
    )


def called_names(function: object) -> tuple[str, ...]:
    tree = ast.parse(inspect.getsource(function))
    answer: list[str] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        if isinstance(node.func, ast.Name):
            answer.append(node.func.id)
        elif isinstance(node.func, ast.Attribute):
            answer.append(node.func.attr)
    return tuple(answer)


def route_interface_controls() -> None:
    schedule_functions = (
        route_a_physical_schedule_spec,
        route_b_physical_schedule_spec,
        route_c_physical_schedule_spec,
    )
    forbidden = {"branch_grades", "norm", "argmax", "choice", "choices", "random", "index", "find", "partial_trace"}
    calls = {function.__name__: called_names(function) for function in schedule_functions}
    violations = {
        name: tuple(call for call in names if call.lower() in forbidden)
        for name, names in calls.items()
    }
    route_map = {route.route: route for route in ROUTES}
    qualified = (
        "supplied candidate-law content" in route_map["A"].probability_or_weight_status
        and "explicit added" in route_map["B"].actual_member_provenance
        and "conditional" in route_map["C"].genesis_or_boundary_status
        and all(not route.pointer_copy_sufficient for route in ROUTES)
    )
    check(
        "A/B/C interfaces freeze supplied-law, added-ontology, and conditional-bath boundaries with no forbidden physical-schedule calls",
        len(ROUTES) == 3 and qualified and not any(violations.values()),
        {"routes": tuple(asdict(route) for route in ROUTES), "calls": calls, "violations": violations},
    )


def obligation_controls() -> None:
    ids = {(test.route, test.test_id) for test in TESTS}
    mandatory = {
        ("common", "kernel_intertwiner"),
        ("common", "member_occurrence_binding"),
        ("common", "projective_cylinders"),
        ("common", "component_mean"),
        ("common", "all24_mass_locality"),
        ("common", "domain_deletion_leakage"),
        ("common", "held_no_refit"),
        ("A", "stochastic_kernel"),
        ("A", "seed_accounting"),
        ("B", "added_actuality"),
        ("B", "period_five"),
        ("B", "non_born_comparator"),
        ("C", "first_passage"),
        ("C", "hazard_provenance"),
        ("C", "renewal_stationarity"),
    }
    check(
        "component/cylinder, empirical-discriminator, locality, domain, resource, and inverse obligations are frozen without results",
        mandatory <= ids and len(DISCRIMINATORS) == 7 and all(test.result is None for test in TESTS),
        {
            "tests": tuple(asdict(test) for test in TESTS),
            "discriminators": DISCRIMINATORS,
            "candidate_law_results_populated": False,
        },
    )


def permutation_parity(values: tuple[int, int, int]) -> int:
    inversions = sum(values[i] > values[j] for i in range(3) for j in range(i + 1, 3))
    return -1 if inversions % 2 else 1


def proper_cubic_frames() -> tuple[tuple[tuple[int, int, int], ...], ...]:
    frames = []
    for axes in permutations((0, 1, 2)):
        parity = permutation_parity(axes)
        for signs in product((-1, 1), repeat=3):
            if parity * signs[0] * signs[1] * signs[2] != 1:
                continue
            matrix = tuple(
                tuple(signs[row] if column == axes[row] else 0 for column in range(3))
                for row in range(3)
            )
            frames.append(matrix)
    return tuple(frames)


def geometry_resource_controls() -> None:
    frames = proper_cubic_frames()
    domain_cases = (
        "zero grade", "unit grade", "tie", "no click", "multiple click",
        "zero winner", "two winner", "three winner", "occupied collision",
        "exhausted carrier", "bath reentry", "nonbinary", "dirty work",
        "phase sensitive", "finite boundary", "unequal component means",
    )
    check(
        "all24, Cycle219 mass, bounded-support, domain, resource, and conservative-total obligations are explicit",
        len(frames) == len(set(frames)) == 24
        and MAX_PRIMITIVE_SUPPORT_M2 == 3
        and len(domain_cases) == 16
        and INHERITED_M2 == {"Cycle478": 1493, "Cycle502": 28, "Cycle505_binding": 17}
        and CONSERVATIVE_TOTAL_CEILINGS == {"A": 1794, "B": 1794, "C": 2562}
        and RSS_CAP_BYTES == 4 * 1024**3 and WALL_CAP_SECONDS == 900.0,
        {
            "proper_cubic_frames": len(frames),
            "maximum_support_M2": MAX_PRIMITIVE_SUPPORT_M2,
            "domain_cases": domain_cases,
            "inherited_M2": INHERITED_M2,
            "new_M2_ceilings": NEW_M2_CEILINGS,
            "conservative_total_ceilings": CONSERVATIVE_TOTAL_CEILINGS,
            "mass_fixture": {"note": FROZEN["Cycle219 note"], "runner": FROZEN["Cycle219 runner"]},
            "RSS_cap": RSS_CAP_BYTES,
            "wall_cap_seconds": WALL_CAP_SECONDS,
        },
    )


def no_go_controls() -> None:
    n2 = (
        ("A", "B", "stochastic normalization is independent of deterministic carrier ontology"),
        ("A", "C", "supplied seed does not prove bath first passage, renewal, or stationarity"),
        ("B", "C", "finite rotor does not test a renewable invariant bath"),
        ("actual member", "Record", "actuality does not prove occurrence/admission"),
        ("corpus law", "pointwise member", "measure law does not select its actual history"),
        ("local routes", "global routes", "A/B/C do not test superselection or boundary selection"),
    )
    n3 = (
        "seed genesis/distribution", "hidden carrier phase", "bath boundary/measure",
        "grade-to-hazard coupling", "law probability meaning", "actuality ontology",
        "occurrence provenance", "Record admissibility", "re-preparation",
        "delimiter recurrence", "stationarity", "component means", "decoder",
        "finite boundary", "noise", "all24 representation", "label ordering",
        "continuum", "empirical data absent",
    )
    n4 = (
        "Cycle478 member/occurrence/probability/corpus residual",
        "Cycle500 actual-member and repeated-law residual",
        "Cycle502 coherent all-sector actuality residual",
        "Cycle505 A/B actuality residual",
        "Cycle505 C occurrence residual",
        "Record producer residual",
        "Born process/convergence residual",
        "Cycle21 physical admitted-corpus/member residual",
    )
    n5 = (
        "basis", "finite coherent train", "finite coherent held", "finite process matrix",
        "simulated corpus", "empirical corpus", "arbitrary N", "infinite/noisy bath",
    )
    n6 = (
        "conditional A with seed genesis open", "B actuality with non-Born calibration",
        "C first passage with stationarity open", "stationarity with unequal components",
        "component means with pointwise seam", "unique-ergodic local orbit",
        "occurrence with Record/renewal open",
    )
    n7 = (
        "translation-covariant finite-density M2 lattice gas; reversible derived stationary renewal phase; "
        "five local collision ports coupled to exact C478/C502 candidates; unique actual first collision; "
        "retained microscopic exhaust; physical occurrence and exact C505 singleton binding; local theorem "
        "for first-passage intensities proportional to operational grades without host amplitude service; "
        "regenerative stationary ergodic admitted corpus with component means matching grades; held waiting-time "
        "and correlation discriminators separating it from supplied seeds and deterministic rotors"
    )
    n8 = (
        "Cycle478 candidate surface", "Cycle500 coherent cylinders", "Cycle502 hard-core candidate",
        "Cycle505 retained formation/binding", "Cycle21/194 component means",
    )
    primaries = tuple(item[0] for item in N1_FAMILIES)
    mechanisms = tuple(item[1] for item in N1_FAMILIES)
    terminals = tuple(item[2] for item in N1_FAMILIES)
    check(
        "origin-normalized N1-N8 remains constructive and licenses no shared obstruction or axiom pressure",
        len(N1_FAMILIES) == 7 and all(len(item) == 3 for item in N1_FAMILIES)
        and len(set(primaries)) == len(set(mechanisms)) == len(set(terminals)) == 7
        and len(n2) >= 6 and len(n3) >= 18 and len(n4) == 8 and len(n5) == 8
        and len(n6) >= 7 and len(n7) > 500 and len(n8) >= 5
        and file_sha(FROZEN_PATHS["premise registry"]) == FROZEN["premise registry"],
        {
            "N1_normalized_families": N1_FAMILIES,
            "N2_independence": n2,
            "N3_hidden_walls": n3,
            "N4_matched_residuals": n4,
            "N5_resolution": n5,
            "N6_partial_closures": n6,
            "N7_steelman": n7,
            "N8_echo": n8,
            "gate_disposition": "UNEXECUTED; no shared obstruction or axiom pressure assessed",
        },
    )


def main() -> int:
    if MODE != "preflight":
        print(f"REFUSE Cycle508 mode={MODE!r}: this artifact authorizes preflight only")
        return 2
    if os.environ.get("CYCLE508_EXECUTE_CANDIDATE_LAWS"):
        print("REFUSE candidate-law execution: root train authorization is absent")
        return 2

    print("CYCLE508 ACTUAL-MEMBER / ADMITTED-HISTORY LAW TOURNAMENT PREFLIGHT")
    print("AUTHORITY", AUTHORITY, "AUDIT", AUDIT, "MODE", MODE)
    print("CANDIDATE LAW TRAIN EXECUTED", False, "HELD EXECUTED", False)
    contract_controls()
    frozen_input_controls()
    type_firewall_controls()
    manifest_controls()
    route_interface_controls()
    obligation_controls()
    geometry_resource_controls()
    no_go_controls()
    print("RESULT", PASS, "passed /", FAIL, "failed")
    print("DISPOSITION UNEXECUTED — contracts frozen; candidate-law train and held both absent")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
