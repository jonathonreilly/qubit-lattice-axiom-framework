#!/usr/bin/env python3
"""Cycle 507 preflight: source/profile-carried dual echo with rollover.

This executable freezes only the target, manifests, finite geometry, response
subword obligation, resource envelope, covariance carriage, host comparators,
and N1-N8 boundary.  It executes no train or held evolution.  The proposed G
is a finite size-specific apparatus circuit built from support-at-most-three
nearest-neighbour terminal gates, not an arbitrary-N bounded-radius QCA.

The candidate ratios are relational dimensionless interval diagnostics.  They
are not lapse, proper time, Records, actuality, rates, or selected history.
Authority none; audit unset.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import permutations, product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SOURCE_PROFILE_DUAL_ECHO_ROLLOVER_PREFLIGHT_CYCLE507_NOTE_2026-07-20.md"
)
AUTHORITY = "none"
AUDIT = "unset"

CLOCK_BITS = 16
CORRIDOR_LENGTH = 2
SIGNAL_MODES = 2 * CORRIDOR_LENGTH
DISTINGUISHED_PROBE_MODE = 0  # the physical A0 / RETURN edge, once per echo
SOURCE_REGISTER_M2 = 9
LOCAL_MODE_M2 = 8  # actual Cycle451 Q1 word; mode 7 is receiver occupied
RESPONSE_PROGRAM_M2 = 2  # supplied DELAY / ADVANCE law interface
PROFILE_M2 = 5
LABEL_M2 = SOURCE_REGISTER_M2 + LOCAL_MODE_M2 + RESPONSE_PROGRAM_M2 + PROFILE_M2
RESPONSE_RECEIPT_M2_PER_EVENT = 9
NEW_CLEAN_WORK_M2 = 6
ENDPOINT_LABEL_M2_PER_EVENT = 2 * LABEL_M2
TRAIN_N = 8
HELD_N = 16
TRAIN_START = 1
HELD_START = 2
HARD_WALL_CAP_SECONDS = 600.0
HARD_RSS_CAP_BYTES = 2 * 1024**3

TRAIN_SOURCE_SECTORS = ("-2pi/9", "-4pi/9", "-2pi/3")
HELD_SOURCE_SECTORS = ("-8pi/9",)
MASS_ROUTES = ("cayley", "principal")
DECODER_FIELDS = (
    "reference endpoints/carries/predecessors",
    "probe endpoints/carries/predecessors",
    "source/profile bindings",
    "response receipts",
)
FORBIDDEN_DECODER_FIELDS = (
    "host application count", "loop ordinal", "schedule position", "circuit depth",
    "source beta lookup", "response-program lookup", "corridor selection",
)

PASS = 0
FAIL = 0


SOURCE_HASHES = {
    "Cycle441 runner": (
        ROOT / "scripts/coherent_multibeta_physical_mass_controller_tournament_cycle441_2026_07_19.py",
        "c274f75ff2b2fe427f04598b84a01247765c562f7ab014ffee2d63af2f27b5d4",
    ),
    "Cycle441 note": (
        ROOT / "docs/work_history/repo/review_feedback/COHERENT_MULTIBETA_PHYSICAL_MASS_CONTROLLER_TOURNAMENT_CYCLE441_NOTE_2026-07-19.md",
        "072e760c11f0f69345aa3cd118835842bc5a0be6c7786426ace30a0dd4b8aa22",
    ),
    "Cycle445 runner": (
        ROOT / "scripts/physical_mass_source_echo_lapse_candidate_tournament_cycle445_2026_07_19.py",
        "dd84bec596ec6c7ac548593c2f3e57f26cba601639c2bf4f156c46c21551b91d",
    ),
    "Cycle445 note": (
        ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_MASS_SOURCE_ECHO_LAPSE_CANDIDATE_TOURNAMENT_CYCLE445_NOTE_2026-07-19.md",
        "5a3e2af7b0d27d861f4233192f5a0fcfcaf4fccfb0051aee0ef8f899c2c3d6e4",
    ),
    "Cycle451 runner": (
        ROOT / "scripts/physical_source_conditioned_relational_dual_clock_cycle451_2026_07_19.py",
        "c89e3d47b42b05c0d723afb5e68548bbb15ee79401eaa72f3c8c715e897071a1",
    ),
    "Cycle451 note": (
        ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_SOURCE_CONDITIONED_RELATIONAL_DUAL_CLOCK_CYCLE451_NOTE_2026-07-19.md",
        "81f28e682b6b45d1572164a7a72b00d252bc81c542a4de5d83ed602b311320ca",
    ),
    "Cycle504 runner": (
        ROOT / "scripts/physical_autonomous_echo_wrap_epoch_conveyor_cycle504_2026_07_20.py",
        "fe1e96fbed14befd235b7799deecbf471f4862130d5fb0a1f905d75246bc226e",
    ),
    "Cycle504 note": (
        ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_AUTONOMOUS_ECHO_WRAP_EPOCH_CONVEYOR_CYCLE504_NOTE_2026-07-20.md",
        "e3e2a903ab7c83beebdce7d2c01f3f77383cafc5e6159a99fc64cc94ba3ab2a3",
    ),
}


@dataclass(frozen=True)
class Split:
    name: str
    horizon: int
    start_clock: int
    source_sectors: tuple[str, ...]
    response_program: str
    reference_cells_per_return: int
    probe_cells_per_return: int
    expected_ratio: Fraction
    held: bool


TRAIN = Split(
    "train", TRAIN_N, TRAIN_START, TRAIN_SOURCE_SECTORS, "DELAY", 4, 3,
    Fraction(3, 4), False,
)
HELD = Split(
    "blind-held", HELD_N, HELD_START, HELD_SOURCE_SECTORS, "ADVANCE", 4, 5,
    Fraction(5, 4), True,
)
SPLITS = (TRAIN, HELD)


@dataclass(frozen=True)
class RouteFamily:
    primary_object: str
    mechanism_or_invariant: str
    terminal_obligation: str
    status: str


ROUTE_FAMILIES = (
    RouteFamily(
        "actual joint Cycle441-register x Cycle451-local-mode controller plus two fixed equal-geometry echo corridors",
        "the coherent receiver-zero/receiver-one sectors control 4 versus 3 or 5 certified forward steps under a separately supplied physical D/A program",
        "compile one reversible finite apparatus and recover branch-conditional retained ratios without occurrence, schedule input, beta lookup, or norm threshold",
        "PRIORITY / PREFLIGHTED ONLY",
    ),
    RouteFamily(
        "two corridors embedded in one fixed short/neutral/long supergraph",
        "a local label-controlled reversible switch routes the probe through a bypass, neutral arm, or detour without changing host geometry",
        "prove local switch restoration and equal external endpoint matching for 3:4 and 5:4",
        "OPEN / UNTESTED",
    ),
    RouteFamily(
        "edge-token stream plus a finite source-labelled transducer",
        "a reversible 4-input accumulator emits exactly 3, 4, or 5 certified clock-step tokens per return",
        "derive retained ratio histories while returning transducer work blank at every cycle",
        "OPEN / UNTESTED",
    ),
    RouteFamily(
        "joint Cycle441 register x dual-clock block operator",
        "operator-first functional calculus coherently controls the probe accumulator while the reference is a spectator",
        "sparsely compile the common operator without beta/projector lookup and bind its output to renewable endpoints",
        "OPEN / UNTESTED",
    ),
    RouteFamily(
        "two independent clocks coupled by a transported common-profile handshake token",
        "a local rendezvous certificate admits one suppressed or extra probe step only after both device/profile identities match",
        "show autonomous certificate genesis, consumption, and retained predecessor lineage",
        "OPEN / UNTESTED",
    ),
    RouteFamily(
        "source-emitted mediator packet crossing the probe echo boundary",
        "one local collision changes the number of certified probe clock-step emissions while conserving a mediator ledger",
        "recover 3:4 and 5:4 from source/clock scattering with a size-stable local compiler",
        "OPEN / UNTESTED",
    ),
)


# Both response paths occur literally in every proposed apparatus word.  A
# supplied physical D/A program and occupancy of Cycle451 local mode 7 enable
# their reversible gates coherently; the host never observes or selects a
# receiver branch.  Multi-controls must be decomposed through the six declared
# clean work bits into support<=3 gates.
RESPONSE_SUBWORD = (
    "load-distinguished-edge-work",
    "load-distinguished-edge-and-local-mode-7-and-DELAY-enable",
    "load-distinguished-edge-and-local-mode-7-and-ADVANCE-enable",
    "load-probe-step-enable=edge XOR delay-enable",
    "15-Fredkin probe baseline forward rotation controlled by probe-step-enable",
    "write suppressed/neutral/extra response receipt",
    "15-Fredkin probe extra forward rotation controlled by advance-enable",
    "write ordinary/extra K15-to-K0 carry kind",
    "unload-probe-step-enable",
    "unload-local-mode-7-and-ADVANCE-enable",
    "unload-local-mode-7-and-DELAY-enable",
    "unload-distinguished-edge-work",
)


EXPECTED_TRAIN_MANIFEST_SHA256 = "7c98084fbc3ef6c64879e6994127984464a6c3cb625d9038d966b91bd7d36ed3"
EXPECTED_HELD_MANIFEST_SHA256 = "3a3814d2cac73bcf94ccc1f9ea2427fe098b2de861524dc02a5be84a91fc9e3f"


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
    body = path.read_text(encoding="utf-8").lower() if path.exists() else ""
    for marker in ("*", "`"):
        body = body.replace(marker, "")
    body = body.removeprefix("> ").replace("\n> ", "\n")
    return " ".join(body.split())


def manifest_digest(rows: list[dict]) -> str:
    return sha256(json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def c504_m2(horizon: int) -> int:
    return 74 + 4 * CORRIDOR_LENGTH + 54 * horizon


def bit_flips(horizon: int) -> int:
    return sum((cell ^ (cell + 1)).bit_count() for cell in range(horizon))


def event_popcount(horizon: int) -> int:
    return sum(value.bit_count() for value in range(2, horizon + 2))


def c504_logical_gates(horizon: int) -> int:
    modes = 2 * CORRIDOR_LENGTH
    return (
        2 * modes + 2 * modes + 4
        + 2 * horizon + horizon + horizon * modes + bit_flips(horizon) + horizon
        + (4 * horizon + 1) + 15
        + 2 * horizon + 16 * horizon + 5 * horizon
        + event_popcount(horizon) + 5 * horizon + 5 * horizon
        + event_popcount(horizon) + 3 * horizon + (4 * horizon + 1)
    )


def cycle507_m2(horizon: int) -> int:
    # Two complete Cycle504 finite corridors; one live source/receiver/program/
    # profile carrier; matching initial bindings; fresh bindings/receipts; and
    # six clean response work bits.
    return (
        2 * c504_m2(horizon) + LABEL_M2 + 2 * LABEL_M2
        + horizon * ENDPOINT_LABEL_M2_PER_EVENT
        + horizon * RESPONSE_RECEIPT_M2_PER_EVENT + NEW_CLEAN_WORK_M2
    )


def logical_gate_envelope(horizon: int) -> int:
    # Conservative preflight cap, not an implemented count: two inherited
    # tables, 57 fresh per-event binding/receipt gates, and 64 fixed response
    # and clean-work gates.  The eventual exact table must be <= this cap.
    return 2 * c504_logical_gates(horizon) + 57 * horizon + 64


def row_manifests() -> tuple[list[dict], list[dict]]:
    train: list[dict] = []
    for source_sector, mass_route in product(TRAIN.source_sectors, MASS_ROUTES):
        train.append({
            "disposition": "train", "role": "primary", "source_sector": source_sector,
            "mass_route": mass_route, "response_program": TRAIN.response_program,
            "controller": "coherent joint register9 x local_mode8-Q1; receiver branch=mode7",
            "profile_word": "one_hot_5(3)",
            "corridor_lengths": (CORRIDOR_LENGTH, CORRIDOR_LENGTH),
            "distinguished_probe_mode": DISTINGUISHED_PROBE_MODE,
            "horizon": TRAIN.horizon, "start_clock": TRAIN.start_clock,
            "expected_reference_total": TRAIN.horizon * TRAIN.reference_cells_per_return,
            "expected_probe_total": TRAIN.horizon * TRAIN.probe_cells_per_return,
            "expected_ratio": str(TRAIN.expected_ratio), "refit": False,
        })
    sentinel = {
        "source_sector": "-4pi/9", "mass_route": "cayley",
        "response_program": TRAIN.response_program,
        "controller": "coherent joint register9 x local_mode8-Q1; receiver branch=mode7",
        "profile_word": "one_hot_5(3)",
        "corridor_lengths": (CORRIDOR_LENGTH, CORRIDOR_LENGTH),
        "distinguished_probe_mode": DISTINGUISHED_PROBE_MODE,
        "horizon": TRAIN.horizon, "start_clock": TRAIN.start_clock,
        "refit": False,
    }
    for deletion in (
        "label-courier", "reference-profile-binding", "probe-profile-binding",
        "receiver-control", "DELAY-enable", "response-receipt",
        "ordinary-wrap-carry", "extra-wrap-carry", "reference-RETURN",
        "probe-RETURN", "host-cadence-comparator", "host-length-comparator",
        "source-sector-lookup-comparator",
    ):
        train.append({
            "disposition": "train", "role": "control", **sentinel,
            "deletion_or_comparator": deletion,
        })

    held: list[dict] = []
    for source_sector, mass_route in product(HELD.source_sectors, MASS_ROUTES):
        held.append({
            "disposition": "blind-held", "role": "primary", "source_sector": source_sector,
            "mass_route": mass_route, "response_program": HELD.response_program,
            "controller": "coherent joint register9 x local_mode8-Q1; receiver branch=mode7",
            "profile_word": "one_hot_5(3)",
            "corridor_lengths": (CORRIDOR_LENGTH, CORRIDOR_LENGTH),
            "distinguished_probe_mode": DISTINGUISHED_PROBE_MODE,
            "horizon": HELD.horizon, "start_clock": HELD.start_clock,
            "expected_reference_total": HELD.horizon * HELD.reference_cells_per_return,
            "expected_probe_total": HELD.horizon * HELD.probe_cells_per_return,
            "expected_ratio": str(HELD.expected_ratio), "refit": False,
        })
    return train, held


def determinant3(matrix: tuple[tuple[int, int, int], ...]) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def proper_cubic_frames() -> tuple[tuple[tuple[int, int, int], ...], ...]:
    frames = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = []
            for target in range(3):
                row = [0, 0, 0]
                row[perm[target]] = signs[target]
                rows.append(tuple(row))
            frame = tuple(rows)
            if determinant3(frame) == 1:
                frames.append(frame)
    return tuple(frames)


def rotate(coord: tuple[int, int, int], frame: tuple[tuple[int, int, int], ...]) -> tuple[int, int, int]:
    return tuple(sum(row[index] * coord[index] for index in range(3)) for row in frame)


def manhattan(left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def note_and_source_controls() -> None:
    required = (
        "authority: none", "audit: unset", "preflight only",
        "one common supplied opportunity delta", "two independently prepared echo corridors",
        "fixed equal ell=2 geometry", "train 3:4", "held 5:4",
        "actual coherent cycle-451", "branch-conditional",
        "separately supplied two-m2 d/a program",
        "receiver squared norm is a diagnostic, not occurrence or probability",
        "literal local reversible subword", "delay gates are not skipped by the host",
        "host-selected corridor length comparator", "decoder reads only retained",
        "not lapse or proper time", "no record or actuality claim",
        "all 24 proper-cubic frames", "n1", "n8", "no axiom pressure",
        "no train or held evolution has executed",
    )
    body = normalized(NOTE)
    missing = tuple(phrase for phrase in required if phrase not in body)
    check("the Cycle507 note freezes the exact preflight-only boundary", not missing, missing)
    observed = {name: file_sha(path) for name, (path, _expected) in SOURCE_HASHES.items()}
    expected = {name: digest for name, (_path, digest) in SOURCE_HASHES.items()}
    check("Cycle441/445/451/504 dependencies are hash frozen", observed == expected, observed)


def target_and_manifest_controls() -> None:
    train, held = row_manifests()
    train_digest = manifest_digest(train)
    held_digest = manifest_digest(held)
    check(
        "train/held manifests freeze equal geometries, physical programs, expected ratios, and no refit before evolution",
        train_digest == EXPECTED_TRAIN_MANIFEST_SHA256
        and held_digest == EXPECTED_HELD_MANIFEST_SHA256
        and len(train) == 19 and len(held) == 2
        and all(tuple(row["corridor_lengths"]) == (2, 2) for row in train + held),
        {
            "train_rows": len(train), "held_rows": len(held),
            "train_manifest_sha256": train_digest,
            "held_manifest_sha256": held_digest,
            "train_primary": 6, "train_controls": 13, "held_primary": 2,
        },
    )


def response_subword_controls() -> None:
    truth = []
    failures = 0
    expected = {"DELAY": 3, "ADVANCE": 5}
    for receiver_branch, program in product((0, 1), expected):
        # This table freezes the terminal obligation only.  The future train
        # must obtain it from the literal installed subword above.
        probe_steps = 4 if receiver_branch == 0 else expected[program]
        truth.append((receiver_branch, program, 4, probe_steps, Fraction(probe_steps, 4)))
        failures += int(receiver_branch == 0 and probe_steps != 4)
        failures += int(receiver_branch == 1 and probe_steps != expected[program])
    joined = " ".join(RESPONSE_SUBWORD).lower()
    check(
        "both supplied law paths act coherently on the actual receiver sectors; receiver-zero remains 4:4",
        failures == 0 and len(RESPONSE_SUBWORD) == 12
        and "15-fredkin probe baseline" in joined and "15-fredkin probe extra" in joined
        and "distinguished-edge-and-local-mode-7-and-delay" in joined
        and "distinguished-edge-and-local-mode-7-and-advance" in joined
        and "unload-local-mode-7-and-delay" in joined
        and "unload-local-mode-7-and-advance" in joined
        and TRAIN.expected_ratio == Fraction(3, 4) and HELD.expected_ratio == Fraction(5, 4),
        {"preflight_truth_table": truth, "installed_subword": RESPONSE_SUBWORD},
    )


def host_comparator_controls() -> None:
    # These comparators can reproduce the numbers but fail the frozen code
    # classifier.  This is a target-contract refusal, not a no-go against a
    # physical local switch or every possible clock.
    host_length = {
        "train_lengths": (4, 3), "train_ratio": Fraction(2 * 3, 2 * 4),
        "held_lengths": (4, 5), "held_ratio": Fraction(2 * 5, 2 * 4),
        "lawful_equal_geometry": False, "response_receipts": False,
    }
    host_cadence = {
        "train_steps": (4, 3), "held_steps": (4, 5),
        "endpoint_ratios_match": True, "response_receipts": False,
        "decoder_schedule_free": False,
    }
    source_lookup = {
        "mapping": {"train beta": "DELAY", "held beta": "ADVANCE"},
        "physical_program_carrier": False, "fixed_table_independent_of_sector": False,
    }
    check(
        "host length, cadence, and source-sector lookup can match arithmetic but fail the frozen physical classifier",
        host_length["train_ratio"] == Fraction(3, 4)
        and host_length["held_ratio"] == Fraction(5, 4)
        and not host_length["lawful_equal_geometry"] and not host_length["response_receipts"]
        and host_cadence["endpoint_ratios_match"] and not host_cadence["response_receipts"]
        and not host_cadence["decoder_schedule_free"]
        and not source_lookup["physical_program_carrier"],
        {"host_length": host_length, "host_cadence": host_cadence, "source_lookup": source_lookup},
    )


def resource_geometry_covariance_controls() -> None:
    frames = proper_cubic_frames()
    rows = {}
    locality_failures = 0
    for split in SPLITS:
        sites = cycle507_m2(split.horizon)
        logical_cap = logical_gate_envelope(split.horizon)
        max_forward_swaps = 3 * (sites - 1)
        nn_gate_cap = logical_cap * (2 * max_forward_swaps + 1)
        elementary_cap = logical_cap * (6 * max_forward_swaps + 3)
        line = tuple((site, 0, 0) for site in range(sites))
        for frame in frames:
            mapped = tuple(rotate(coord, frame) for coord in line)
            locality_failures += sum(
                manhattan(mapped[index], mapped[index + 1]) != 1
                for index in range(len(mapped) - 1)
            )
        rows[split.name] = {
            "horizon": split.horizon,
            "two_Cycle504_M2": 2 * c504_m2(split.horizon),
            "Cycle507_M2": sites,
            "constant_new_M2_per_event": ENDPOINT_LABEL_M2_PER_EVENT + RESPONSE_RECEIPT_M2_PER_EVENT,
            "logical_gate_envelope": logical_cap,
            "maximum_forward_SWAPS_per_gate_envelope": max_forward_swaps,
            "NN_gate_operation_envelope": nn_gate_cap,
            "elementary_CNOT_or_Toffoli_operation_envelope": elementary_cap,
        }
    check(
        "finite layout, compact restored-line routing envelope, and all24 carried adjacency are frozen before evolution",
        len(frames) == 24 and len(set(frames)) == 24 and locality_failures == 0
        and rows["train"]["Cycle507_M2"] == 1562
        and rows["blind-held"]["Cycle507_M2"] == 2882
        and rows["train"]["logical_gate_envelope"] == 1512
        and rows["blind-held"]["logical_gate_envelope"] == 2912,
        {
            "proper_cubic_frames": len(frames), "carried_line_adjacency_failures": locality_failures,
            "rows": rows, "future_route_manifest": "compact descriptors required; expanded SWAP tuples forbidden",
            "terminal_support_M2": "<=3 after multi-control decomposition",
            "global_circuit_warning": "restored routing is size-specific and not bounded-depth/radius as N grows",
            "wall_cap_seconds": HARD_WALL_CAP_SECONDS, "RSS_cap_bytes": HARD_RSS_CAP_BYTES,
        },
    )


def no_go_discipline_controls() -> None:
    normalized_families = tuple(
        (route.primary_object, route.mechanism_or_invariant, route.terminal_obligation)
        for route in ROUTE_FAMILIES
    )
    walls = (
        "finite response/profile compiler",
        "source/profile/program genesis or law selection",
        "Record occurrence and realized endpoints",
        "universal clock metric and continuum proper time",
    )
    pairwise = tuple(
        (left, right, "no", "no", "independent at preflight")
        for index, left in enumerate(walls) for right in walls[index + 1:]
    )
    hidden = (
        "common supplied delta", "two ell=2 corridor preparations", "Cycle441 source sector",
        "receiver-one conditioning without occurrence", "DELAY/ADVANCE program word",
        "profile identity", "blank finite banks", "distinguished probe edge",
        "size-specific restored router", "noiseless reversible gates",
    )
    residuals = (
        ("Cycle451", "joined response/latch schedule and renewable epoch carrier open", "finite response/profile plus Cycle504 rollover compiler", True),
        ("Cycle504", "source-conditioned dual echo open", "same source/profile-carried finite ratio apparatus", True),
        ("Cycle441", "beta lookup retired only for supplied operator functions", "forbid host beta-to-program lookup but do not derive law selection", True),
        ("Cycle451 continuum target", "lapse/proper time remains open", "dimensionless finite ratios only", False),
    )
    rhetoric = (
        ("host-selected corridor length is inadmissible", "only the frozen equal-ell=2 Cycle507 code", "a physical local supergraph switch remains open"),
        ("host cadence is not decoded", "endpoint/receipt decoder contract", "other autonomous transducers remain open"),
        ("source-sector lookup is forbidden", "G builder and response program transport", "operator-first physical source control remains open"),
    )
    partial_paths = (
        "compile the priority response subword with physical work/exhaust receipts",
        "replace supplied program preparation by a local Cycle441 receiver interaction",
        "replace the global line router by a bounded-radius tiling",
        "attach Record/actuality only after independent formation and occurrence laws",
        "attempt common-profile synchronization before any proper-time theorem",
    )
    steelman = (
        "A hostile reviewer should build the fixed short/neutral/long supergraph route: it obeys the no-host-length target "
        "because one immutable geometry contains every arm, while the transported physical label operates only a local "
        "reversible switch.  Its terminal obligation is exact route restoration plus matched external endpoints.  Until "
        "that construction and the transducer route are tested, failure of the priority clock-step compiler cannot support a no-go."
    )
    cross_cycle = (
        "Cycle451 replaced separately evaluated denominators by a co-registered pair; Cycle504 replaced finite no-wrap "
        "endpoints by retained rollover/renewal.  Cycle507 attempts their composition.  Both prior closures came from "
        "new physical carriers, so any future obstruction must keep the untested carrier/supergraph/transducer routes live."
    )
    check(
        "N1-N8 keeps the host-comparator refusal narrow and blocks broad no-go or axiom-pressure promotion",
        len(ROUTE_FAMILIES) >= 5 and len(set(normalized_families)) == len(ROUTE_FAMILIES)
        and len(pairwise) == 6 and len(hidden) >= 8
        and sum(row[-1] for row in residuals) == 3 and len(rhetoric) == 3
        and len(partial_paths) >= 4 and "supergraph" in steelman and "new physical carriers" in cross_cycle,
        {
            "N1_normalized_route_families": tuple(asdict(route) for route in ROUTE_FAMILIES),
            "N2_pairwise_collapsed_walls": pairwise,
            "N3_hidden_conditions": hidden,
            "N4_residual_matching": residuals,
            "N5_rhetoric_resolution": rhetoric,
            "N6_partial_closure_paths": partial_paths,
            "N7_hostile_steelman": steelman,
            "N8_cross_cycle_echo": cross_cycle,
            "broad_no_go_gate": "FAIL / DO NOT SHIP", "axiom_pressure": False,
        },
    )


def inventory_controls() -> None:
    supplied = (
        "one common opportunity delta and one finite size-specific apparatus family",
        "Cycle441 source sectors and selected Cayley/principal candidate routes",
        "actual coherent Cycle451 local-mode controller plus a separately supplied physical D/A program and profile identity",
        "two independent blank ell=2 Cycle504 corridors and finite event/carry banks",
        "distinguished probe edge, exact factor order, restored line placement, and noiseless gates",
    )
    preflight_derived = (
        "frozen receiver-one branch targets N8 DELAY 24/32=3/4 and N16 ADVANCE 80/64=5/4",
        "literal presence of both controlled response paths and their uncompute/exhaust obligations",
        "fixed equal geometry and narrow rejection of three arithmetic-only host comparators",
        "M2/gate/routing resource envelopes and all24 carried line adjacency",
        "normalized constructive registry and full N1-N8 preflight boundary",
    )
    open_items = (
        "all train and held evolution, E/G, inverse, deletions, exhaust, refinement, and exact routed manifests",
        "physical source/profile courier and response-receipt construction",
        "selection/genesis of source, receiver, response program, profile, identities, delta, and apparatus",
        "bounded-radius arbitrary-N QCA, noise protection, and universal synchronization",
        "Record/actuality, lapse/proper time, continuum/Lorentz, source/gravity, and Born law",
    )
    check(
        "supplied, preflight-derived, and open inventories prohibit premature science claims",
        len(supplied) == 5 and len(preflight_derived) == 5 and len(open_items) == 5,
        {"supplied": supplied, "preflight_derived": preflight_derived, "open": open_items},
    )


def main() -> int:
    print("CYCLE507 SOURCE/PROFILE DUAL-ECHO ROLLOVER PREFLIGHT ONLY")
    print({"authority": AUTHORITY, "audit": AUDIT, "train_rows_executed": 0, "held_rows_executed": 0})
    note_and_source_controls()
    target_and_manifest_controls()
    response_subword_controls()
    host_comparator_controls()
    resource_geometry_covariance_controls()
    no_go_discipline_controls()
    inventory_controls()
    print("PREFLIGHT_ONLY", {"train_evolution_executed": 0, "held_evolution_executed": 0, "stage_git_paths": 0})
    print(f"RESULT pass={PASS} fail={FAIL} mode=preflight")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
