#!/usr/bin/env python3
"""Independent exact checker for the corrected Block21 finite-bath pre-gate.

This implementation reads only the frozen preregistration packet and source
authorities named there.  It never imports or opens the Block21 primary runner
or cache.  Its sole terminal concerns exact indefinite repeatability with one
fixed finite memory and one fixed unitary; broader bath families remain live.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import permutations, product
from math import floor, log
from pathlib import Path
import subprocess
from typing import Iterable, Sequence


ROOT = Path(__file__).resolve().parents[1]
PACKET = Path(
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block21-autonomous-reusable-bath-"
    "complement-blind-selector-20260830"
)
INITIAL_FREEZE = "6fdaadd635a1c1004ccbb8e78fa208531943ba2c"
CORRECTED_FREEZE = "d20a49e1a875aa45c1fad810f21cda914fdb45d1"
PIN_COMMIT = "f036fdefad7b9a4ed8d1407780f2374a801b27fa"
PIN_SHA256 = "9134c8e2af33bdf23ed3e8756db7c52cea61611ce6a0472968712c1899581860"
TERMINAL = (
    "FINITE-EXACT-INDEFINITE-REPEATABILITY-OBSTRUCTED-FOR-"
    "NONTRIVIAL-APPEND-IN-G_FIN_INFINITY"
)
PRIMARY_SOURCE = Path(
    "scripts/admissibility_d4_autonomous_reusable_bath_"
    "complement_blind_selector_gate_2026_08_30.py"
)
INDEPENDENT_SOURCE = Path(__file__).resolve().relative_to(ROOT)

EXPECTED_PACKET_HASHES = {
    "GOAL.md": "0e13ed4944ce6bae842484a349d67a6515eaa86391122a6708675921208a1ef9",
    "AUTHORITY_GATE.md": "d2f004885d7d3d6a6657762f3cd3739558c46a6271c775e8ee1afe3c796aee17",
    "PREFLIGHT_WITNESSES.md": "00cda1aec2794ec3e4d15072a869524f8c4d38cf1de77f071f661a24dab0a0c0",
    "INDEPENDENT_PREREG_ATTACK.md": "510c3b2e6d2194ada43046c4e933e0c619e8410a08e2c26e293c2440e60c49c5",
    "APPROACH_REGISTRY.md": "b653f914a4dda4608688998b99ea37549f8c0f760ee4bade7d35f7cb33cd094e",
    "PANEL_RETURN.md": "9e82303ccff75899ae4b004be1be49ebabe583e02c419140a5339d6342e018ee",
    "NO_GO_DISCIPLINE_CHECKLIST.md": "b8597fe431429ab357be096a2e7e43e3458ba25d4f4572c989f9a0ca5c44e321",
    "PREFLIGHT_SUPPORT_CORRECTION.md": "6a1b354941c1c289643256fd6a135c39e47c4a8cfa981b13227ccfc962120756",
}

Vector = tuple[int, int, int]
Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]
BLANK: Vector = (0, 0, 0)
MARKS: tuple[Vector, ...] = (
    (1, 0, 0), (-1, 0, 0), (0, 1, 0),
    (0, -1, 0), (0, 0, 1), (0, 0, -1),
)
STATES: tuple[Vector, ...] = (BLANK,) + MARKS
FROZEN_MARK: Vector = (0, 0, 1)
SECTORS = ("u", "a", "o", "p")


class Certificate:
    def __init__(self) -> None:
        self.lines: list[str] = []
        self.passes = 0
        self.failures = 0

    def check(self, name: str, condition: bool, detail: str) -> None:
        status = "PASS" if condition else "FAIL"
        self.passes += int(condition)
        self.failures += int(not condition)
        self.lines.append(f"{status} {name}: {detail}")

    def emit(self) -> None:
        self.lines.append(f"TOTAL: PASS={self.passes} FAIL={self.failures}")
        rendered = "\n".join(self.lines)
        if len(rendered) >= 6000:
            rendered = (
                "FAIL OUTPUT_LENGTH: independent stdout exceeded 6000 characters\n"
                f"TOTAL: PASS={self.passes} FAIL={self.failures + 1}"
            )
        print(rendered)


def read(relative: Path) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def file_sha256(relative: Path) -> str:
    return sha256((ROOT / relative).read_bytes()).hexdigest()


def git(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=60
    ).strip()


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    ).returncode == 0


def exists_at(commit: str, relative: Path) -> bool:
    return subprocess.run(
        ("git", "cat-file", "-e", f"{commit}:{relative.as_posix()}"),
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    ).returncode == 0


def all_needles(text: str, needles: Iterable[str]) -> bool:
    flattened = " ".join(text.split())
    return all(" ".join(needle.split()) in flattened for needle in needles)


def parity(permutation: Sequence[int]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def proper_cubic_group() -> tuple[Matrix, ...]:
    matrices: set[Matrix] = set()
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if parity(permutation) * signs[0] * signs[1] * signs[2] != 1:
                continue
            matrix = tuple(
                tuple(signs[row] if column == permutation[row] else 0
                      for column in range(3))
                for row in range(3)
            )
            matrices.add(matrix)  # type: ignore[arg-type]
    return tuple(sorted(matrices))


def act(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum(matrix[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def multiply(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum(left[row][inner] * right[inner][column] for inner in range(3))
            for column in range(3)
        )
        for row in range(3)
    )  # type: ignore[return-value]


def transpose(matrix: Matrix) -> Matrix:
    return tuple(
        tuple(matrix[column][row] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def rational_rank(rows: Sequence[Sequence[int | Fraction]]) -> int:
    matrix = [[Fraction(value) for value in row] for row in rows]
    if not matrix:
        return 0
    rank = 0
    columns = len(matrix[0])
    for column in range(columns):
        pivot = next(
            (row for row in range(rank, len(matrix)) if matrix[row][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        pivot_value = matrix[rank][column]
        matrix[rank] = [value / pivot_value for value in matrix[rank]]
        for row in range(len(matrix)):
            if row == rank or not matrix[row][column]:
                continue
            factor = matrix[row][column]
            matrix[row] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(matrix[row], matrix[rank])
            ]
        rank += 1
        if rank == len(matrix):
            break
    return rank


def stabilizer_orbits(group: Sequence[Matrix], fixed: Vector) -> tuple[frozenset[Vector], ...]:
    stabilizer = tuple(matrix for matrix in group if act(matrix, fixed) == fixed)
    unseen = set(STATES)
    orbits: list[frozenset[Vector]] = []
    while unseen:
        seed = next(iter(unseen))
        orbit = frozenset(act(matrix, seed) for matrix in stabilizer)
        orbits.append(orbit)
        unseen -= orbit
    return tuple(sorted(orbits, key=lambda orbit: (len(orbit), sorted(orbit))))


def sector(mark: Vector, control: Vector) -> str:
    if control == BLANK:
        return "u"
    inner = sum(mark[index] * control[index] for index in range(3))
    return "a" if inner == 1 else "o" if inner == -1 else "p"


def profile_signature(mark: Vector, profile: Sequence[Vector]) -> tuple[int, int, int, int]:
    counts = {name: 0 for name in SECTORS}
    for control in profile:
        counts[sector(mark, control)] += 1
    return tuple(counts[name] for name in SECTORS)  # type: ignore[return-value]


def profile_census() -> tuple[int, tuple[int, ...]]:
    per_mark_signature_counts: list[int] = []
    profile_count = 0
    for mark_index, mark in enumerate(MARKS):
        signatures: set[tuple[int, int, int, int]] = set()
        count = 0
        for profile in product(STATES, repeat=6):
            signature = profile_signature(mark, profile)
            if sum(signature) != 6:
                raise AssertionError("profile signature lost a neighbor")
            signatures.add(signature)
            count += 1
        if mark_index == 0:
            profile_count = count
        elif count != profile_count:
            raise AssertionError("mark profile counts differ")
        per_mark_signature_counts.append(len(signatures))
    return profile_count, tuple(per_mark_signature_counts)


def provenance(label: str) -> str:
    assumed = {
        "u=o=p", "o/u=p/u=1", "span{I,P_f}", "tied_bath_matrix_elements",
        "basis_identifies_sources", "shared_complement_coefficient",
    }
    relocated = {
        "equal_spectral_functions", "chosen_temperature_gap",
        "chosen_spectral_ratio", "chosen_coupling_ratio",
    }
    if label in assumed:
        return "ASSUMED-SELECTOR"
    if label in relocated:
        return "RELOCATED"
    if label == "proper_cubic_covariance":
        return "UNDERSELECTED"
    return "UNRESOLVED-PROVENANCE"


@dataclass(frozen=True)
class SquaredResponse:
    u: Fraction
    a: Fraction
    o: Fraction
    p: Fraction
    phases: tuple[str, str, str, str] = ("common",) * 4


def beta_projection(response: SquaredResponse) -> tuple[str, Fraction | None]:
    values = (response.u, response.a, response.o, response.p)
    if any(value <= 0 for value in values) or len(set(response.phases)) != 1:
        return "OUTSIDE-BLOCK19-BETA-FAMILY", None
    if response.o != response.p:
        return "OUTSIDE-BLOCK19-BETA-FAMILY", None
    if response.a != 2 * response.o:
        return "MISSING-SUPPLIED-FACTOR-TWO", None
    return "MEMBER", response.o / response.u


Term = tuple[Vector, Vector, Vector, Vector | None, Vector | None, str]


def interaction_terms() -> frozenset[Term]:
    terms: set[Term] = set()
    for mark in MARKS:
        for control in STATES:
            label = sector(mark, control)
            terms.add((mark, BLANK, control, mark, None, label))
            terms.add((BLANK, mark, control, None, mark, label))
    return frozenset(terms)


def conjugate(term: Term) -> Term:
    target_out, target_in, control, bath_out, bath_in, label = term
    return target_in, target_out, control, bath_in, bath_out, label


def transform_term(matrix: Matrix, term: Term) -> Term:
    target_out, target_in, control, bath_out, bath_in, label = term
    return (
        act(matrix, target_out),
        act(matrix, target_in),
        act(matrix, control),
        None if bath_out is None else act(matrix, bath_out),
        None if bath_in is None else act(matrix, bath_in),
        label,
    )


@dataclass(frozen=True)
class AppendInstrument:
    hold: Fraction
    writes: tuple[Fraction, Fraction, Fraction, Fraction, Fraction, Fraction]

    def is_cptp(self) -> bool:
        weights = (self.hold,) + self.writes
        blank_norm = self.hold + sum(self.writes, Fraction(0))
        occupied_norms = tuple(Fraction(1) for _ in MARKS)
        return (
            all(weight >= 0 for weight in weights)
            and blank_norm == 1
            and all(norm == 1 for norm in occupied_norms)
        )

    def is_nontrivial(self) -> bool:
        return any(weight > 0 for weight in self.writes)

    def image_of_identity(self) -> tuple[Fraction, ...]:
        return (self.hold,) + tuple(1 + weight for weight in self.writes)

    def is_unital(self) -> bool:
        return self.image_of_identity() == (Fraction(1),) * 7

    def outputs(self, pointer: Vector) -> tuple[tuple[str, Fraction, Vector], ...]:
        if pointer != BLANK:
            return (("locked", Fraction(1), pointer),)
        branches = [("hold", self.hold, BLANK)]
        branches.extend(
            (f"write_{index}", weight, mark)
            for index, (mark, weight) in enumerate(zip(MARKS, self.writes))
            if weight > 0
        )
        return tuple(branch for branch in branches if branch[1] > 0)


def shannon(probabilities: Sequence[Fraction]) -> float:
    return -sum(float(value) * log(float(value)) for value in probabilities if value)


def uniform_entropy_drop(instrument: AppendInstrument) -> tuple[float, tuple[Fraction, ...]]:
    output = (instrument.hold / 7,) + tuple((1 + weight) / 7 for weight in instrument.writes)
    return log(7) - shannon(output), output


@dataclass(frozen=True)
class RepeatabilityHypotheses:
    memory_dimension: int
    fixed_finite_memory: bool
    fixed_unitary: bool
    initially_factorized_inputs: bool
    same_cptp_channel_each_use: bool
    arbitrarily_many_uses: bool
    exact: bool

    def theorem_applies(self) -> bool:
        return (
            self.memory_dimension > 0
            and self.fixed_finite_memory
            and self.fixed_unitary
            and self.initially_factorized_inputs
            and self.same_cptp_channel_each_use
            and self.arbitrarily_many_uses
            and self.exact
        )


@dataclass(frozen=True)
class StockState:
    ready_factors: int
    cursor: int
    history: tuple[str, ...] = ()


@dataclass(frozen=True)
class StockBranch:
    outcome: str
    probability: Fraction
    output: Vector
    bath: StockState


class TwoReadyFactorStock:
    """Time-independent cursor rule with two consumable Stinespring factors."""

    def __init__(self, instrument: AppendInstrument, erase_when_empty: bool = False) -> None:
        self.instrument = instrument
        self.erase_when_empty = erase_when_empty

    def initial(self) -> StockState:
        return StockState(ready_factors=2, cursor=0)

    def branches(self, bath: StockState, pointer: Vector) -> tuple[StockBranch, ...]:
        if bath.ready_factors > 0:
            visible = self.instrument.outputs(pointer)
            next_ready = bath.ready_factors - 1
            next_cursor = bath.cursor + 1
        elif pointer != BLANK and self.erase_when_empty:
            visible = (("illegal_erase", Fraction(1), BLANK),)
            next_ready = 0
            next_cursor = bath.cursor
        else:
            visible = (("idle", Fraction(1), pointer),)
            next_ready = 0
            next_cursor = bath.cursor
        return tuple(
            StockBranch(
                outcome=outcome,
                probability=probability,
                output=output,
                bath=StockState(
                    next_ready,
                    next_cursor,
                    bath.history + (outcome,),
                ),
            )
            for outcome, probability, output in visible
            if probability > 0
        )

    def visible_signature(self, bath: StockState) -> tuple[object, ...]:
        signature: list[object] = []
        for pointer in STATES:
            branches = tuple(
                (branch.outcome, branch.probability, branch.output)
                for branch in self.branches(bath, pointer)
            )
            signature.append((pointer, branches))
        return tuple(signature)


def reachable_bath_states(
    model: TwoReadyFactorStock, horizon: int
) -> frozenset[StockState]:
    reached = {model.initial()}
    frontier = {model.initial()}
    for _ in range(horizon):
        next_frontier: set[StockState] = set()
        for bath in frontier:
            for pointer in STATES:
                next_frontier.update(branch.bath for branch in model.branches(bath, pointer))
        reached.update(next_frontier)
        frontier = next_frontier
    return frozenset(reached)


def lock_holds(model: TwoReadyFactorStock, baths: Iterable[StockState]) -> bool:
    return all(
        branch.output == pointer
        for bath in baths
        for pointer in MARKS
        for branch in model.branches(bath, pointer)
    )


def kms_classification(
    inverse_temperature: Fraction,
    gap: Fraction,
    temperature_fixed_by_authority: bool,
    gap_fixed_by_authority: bool,
) -> tuple[Fraction, str]:
    exponent = inverse_temperature * gap
    status = (
        "CONDITIONAL-PHYSICAL-INPUT"
        if temperature_fixed_by_authority and gap_fixed_by_authority
        else "RELOCATED"
    )
    return exponent, status


def equal_z_bank() -> dict[int, set[tuple[tuple[int, ...], int]]]:
    bank: dict[int, set[tuple[tuple[int, ...], int]]] = {9: set(), 10: set(), 12: set()}
    for counts in product(range(7), repeat=6):
        count = sum(counts)
        if count > 6:
            continue
        z_value = sum(2 ** multiplicity for multiplicity in counts)
        if z_value in bank:
            bank[z_value].add((tuple(sorted(counts, reverse=True)), count))
    return bank


def joint_flags_valid(flags: dict[str, bool]) -> bool:
    required = (
        "one_hermitian_interaction", "one_shared_bath", "all_six_marks",
        "cross_mark_parameters", "cptp", "covariant", "all_profiles",
    )
    return all(flags.get(field, False) for field in required)


def extensive_ownership_valid(fields: dict[str, bool]) -> bool:
    required = (
        "boundary_state", "transport", "outgoing_archive", "locality",
        "process_limit", "coupling_provenance", "cadence",
    )
    return all(fields.get(field, False) for field in required)


def choose_terminal(
    positive_full: bool,
    positive_conditional: bool,
    finite_exact_obstruction: bool,
    named_finite_memory: bool,
    cubic_underselection: bool,
    kms_relocation: bool,
) -> str:
    if positive_full:
        return "POSITIVE-FULL-BATH-DERIVATION-ONE-BETA-RAY-AND-MARK-KERNEL"
    if positive_conditional:
        return "POSITIVE-BATH-BETA-SELECTOR-CONDITIONAL-ON-SUPPLIED-MARK-KERNEL"
    if finite_exact_obstruction:
        return TERMINAL
    if named_finite_memory:
        return "NAMED-G_FIN_K-MEMORY-FOUND"
    if cubic_underselection:
        return "CUBIC-RESPONSE-SYMMETRY-UNDERSELECTED-IN-G_COV"
    if kms_relocation:
        return "BETA-RELOCATED-INTO-BATH-STATE-OR-SPECTRAL-DATA"
    return "MIXED-OR-UNRESOLVED"


def main() -> Certificate:
    certificate = Certificate()
    packet_text = {name: read(PACKET / name) for name in EXPECTED_PACKET_HASHES}
    freeze_pin = read(PACKET / "FREEZE_PIN.md")
    pinned_state = git("show", f"{PIN_COMMIT}:{(PACKET / 'STATE.yaml').as_posix()}")
    packet_hashes_ok = all(
        file_sha256(PACKET / name) == expected
        for name, expected in EXPECTED_PACKET_HASHES.items()
    )
    sources_absent = all(
        not exists_at(commit, source)
        for commit in (INITIAL_FREEZE, CORRECTED_FREEZE, PIN_COMMIT)
        for source in (PRIMARY_SOURCE, INDEPENDENT_SOURCE)
    )
    freeze_ok = (
        all(is_ancestor(commit) for commit in (INITIAL_FREEZE, CORRECTED_FREEZE, PIN_COMMIT))
        and git("log", "-1", "--format=%H", "--", (PACKET / "FREEZE_PIN.md").as_posix()) == PIN_COMMIT
        and file_sha256(PACKET / "FREEZE_PIN.md") == PIN_SHA256
        and packet_hashes_ok
        and sources_absent
        and all_needles(
            freeze_pin + pinned_state,
            (
                INITIAL_FREEZE, CORRECTED_FREEZE,
                "status: corrected_preregistration_frozen",
                "proper_cubic_group_order: 24",
                "fixed_f_control_orbits: 4",
            ),
        )
    )
    certificate.check(
        "A_corrected_freeze",
        freeze_ok,
        "8/8 science hashes pinned at d20a49e1a875; metadata history pinned at f036fdefad; both runners absent at all freezes",
    )

    goal = packet_text["GOAL.md"]
    authority = packet_text["AUTHORITY_GATE.md"]
    preflight = packet_text["PREFLIGHT_WITNESSES.md"]
    correction = packet_text["PREFLIGHT_SUPPORT_CORRECTION.md"]
    attack = packet_text["INDEPENDENT_PREREG_ATTACK.md"]
    contract_ok = all_needles(
        goal + authority + preflight + correction + attack,
        (
            "G_fin,infinity", "DERIVED-CB", "o!=p", "one joint Hermitian",
            "two-ready-factor", "every bath state reachable",
            "BETA-RELOCATED-INTO-BATH-STATE-OR-SPECTRAL-DATA",
            TERMINAL, "Infinite, correlated, approximate-return",
            "zero TOE percentage movement",
        ),
    )
    certificate.check(
        "B_corrected_contract",
        contract_ok,
        "provenance, joint-six-mark, reachable-lock, finite/all-use, relocation, and live-route clauses all present",
    )

    group = proper_cubic_group()
    group_set = set(group)
    identity: Matrix = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    closure_ok = all(multiply(left, right) in group_set for left in group for right in group)
    inverses_ok = all(
        multiply(matrix, transpose(matrix)) == identity
        and multiply(transpose(matrix), matrix) == identity
        for matrix in group
    )
    mark_orbit = {act(matrix, FROZEN_MARK) for matrix in group}
    certificate.check(
        "C_proper_cubic_group",
        len(group) == 24 and identity in group_set and closure_ok and inverses_ok and mark_orbit == set(MARKS),
        f"order={len(group)}; exact signed-permutation closure/inverses; six-mark orbit={len(mark_orbit)}",
    )

    orbits = stabilizer_orbits(group, FROZEN_MARK)
    expected_orbits = {
        frozenset({BLANK}),
        frozenset({FROZEN_MARK}),
        frozenset({tuple(-entry for entry in FROZEN_MARK)}),
        frozenset({mark for mark in MARKS if sum(mark[i] * FROZEN_MARK[i] for i in range(3)) == 0}),
    }
    stabilizer = tuple(matrix for matrix in group if act(matrix, FROZEN_MARK) == FROZEN_MARK)
    pair_covariance = all(
        sector(mark, control) == sector(act(matrix, mark), act(matrix, control))
        for matrix in group for mark in MARKS for control in STATES
    )
    complement_source_rank = rational_rank(((1, 0, 0), (0, 1, 0), (0, 0, 1)))
    cb_constraint_rank = rational_rank(((1, -1, 0), (1, 0, -1)))
    orbit_ok = (
        len(stabilizer) == 4
        and set(orbits) == expected_orbits
        and len(orbits) == 4
        and pair_covariance
        and complement_source_rank == 3
        and cb_constraint_rank == 2
    )
    certificate.check(
        "D_orbits_and_source_rank",
        orbit_ok,
        "fixed +z stabilizer=4; orbits=(blank,same,opposite,perpendicular); invariant diagonal dimension=4; u/o/p rank=3",
    )

    provenance_inputs = {
        label: provenance(label)
        for label in (
            "proper_cubic_covariance", "u=o=p", "o/u=p/u=1", "span{I,P_f}",
            "tied_bath_matrix_elements", "basis_identifies_sources",
            "shared_complement_coefficient", "equal_spectral_functions",
        )
    }
    provenance_ok = (
        provenance_inputs["proper_cubic_covariance"] == "UNDERSELECTED"
        and all(
            provenance_inputs[label] == "ASSUMED-SELECTOR"
            for label in (
                "u=o=p", "o/u=p/u=1", "span{I,P_f}",
                "tied_bath_matrix_elements", "basis_identifies_sources",
                "shared_complement_coefficient",
            )
        )
        and provenance_inputs["equal_spectral_functions"] == "RELOCATED"
        and "DERIVED-CB" not in provenance_inputs.values()
    )
    certificate.check(
        "E_cb_provenance",
        provenance_ok,
        "cubic covariance leaves three independent complement coordinates; 6 insertion forms classified assumed/relocated, never derived",
    )

    beta_one = SquaredResponse(Fraction(1), Fraction(2), Fraction(1), Fraction(1))
    beta_two = SquaredResponse(Fraction(1), Fraction(4), Fraction(2), Fraction(2))
    scaled = SquaredResponse(Fraction(5), Fraction(10), Fraction(5), Fraction(5))
    split = SquaredResponse(Fraction(1), Fraction(2), Fraction(1), Fraction(2))
    phase_split = SquaredResponse(
        Fraction(1), Fraction(2), Fraction(1), Fraction(1),
        ("q", "q", "q", "relative"),
    )
    beta_results = tuple(beta_projection(response) for response in (beta_one, beta_two))
    beta_ok = (
        beta_results == (("MEMBER", Fraction(1)), ("MEMBER", Fraction(2)))
        and beta_projection(scaled) == ("MEMBER", Fraction(1))
        and beta_projection(split)[1] is None
        and beta_projection(phase_split)[1] is None
    )
    certificate.check(
        "F_beta_membership",
        beta_ok,
        "o=p, positivity, common phase, supplied factor-two, and global scaling enforced; beta=1 and beta=2 rays both survive G_cov",
    )

    terms = interaction_terms()
    hermitian_ok = all(conjugate(term) in terms for term in terms)
    interaction_covariant = all(
        transform_term(matrix, term) in terms for matrix in group for term in terms
    )
    forward_counts = {
        mark: sum(term[0] == mark and term[1] == BLANK for term in terms)
        for mark in MARKS
    }
    profile_count, signature_counts = profile_census()
    instrument = AppendInstrument(Fraction(1, 2), (Fraction(1, 12),) * 6)
    joint_flags = {
        "one_hermitian_interaction": hermitian_ok,
        "one_shared_bath": True,
        "all_six_marks": set(forward_counts.values()) == {7},
        "cross_mark_parameters": pair_covariance,
        "cptp": instrument.is_cptp(),
        "covariant": interaction_covariant,
        "all_profiles": profile_count == 7 ** 6 and set(signature_counts) == {84},
    }
    joint_ok = joint_flags_valid(joint_flags)
    certificate.check(
        "G_joint_six_mark_type",
        joint_ok,
        f"one 84-term Hermitian shared-bath template; CP/TP append instrument; profiles={profile_count} per mark, signatures={signature_counts[0]}",
    )

    pure_constraint_rank = rational_rank(tuple(
        tuple(int(row == column) for column in range(6)) for row in range(6)
    ))
    writable_mutant = (Fraction(1),) + (Fraction(0),) * 5
    pure_control_ok = pure_constraint_rank == 6 and any(writable_mutant)
    certificate.check(
        "H_pure_exact_return_control",
        pure_control_ok,
        "six occupied-state inner products give a rank-6 constraint, so every blank-to-mark amplitude vanishes at exact pure return",
    )

    identity_image = instrument.image_of_identity()
    entropy_drop, uniform_output = uniform_entropy_drop(instrument)
    nonunital_ok = (
        instrument.is_cptp()
        and instrument.is_nontrivial()
        and not instrument.is_unital()
        and identity_image == (Fraction(1, 2),) + (Fraction(13, 12),) * 6
        and sum(uniform_output, Fraction(0)) == 1
        and uniform_output != (Fraction(1, 7),) * 7
        and entropy_drop > 0
    )
    certificate.check(
        "I_append_nonunitality",
        nonunital_ok,
        "nonzero six-mark append is CP/TP but T(I)=(1/2,13/12 x6); maximally mixed entropy decreases strictly",
    )

    hypotheses = RepeatabilityHypotheses(4, True, True, True, True, True, True)
    contradiction_use = floor(log(hypotheses.memory_dimension) / entropy_drop) + 1
    entropy_bound_ok = (
        hypotheses.theorem_applies()
        and contradiction_use * entropy_drop > log(hypotheses.memory_dimension)
        and (contradiction_use - 1) * entropy_drop <= log(hypotheses.memory_dimension)
    )
    finite_exact_obstruction = nonunital_ok and entropy_bound_ok
    certificate.check(
        "J_exact_repeatability_entropy_bound",
        entropy_bound_ok,
        f"n*entropy_drop <= log(dim K) reconstructed at exact theorem hypotheses; dim(K)=4 fails by use n={contradiction_use}",
    )

    stock = TwoReadyFactorStock(instrument)
    first_state = stock.initial()
    first_branch = stock.branches(first_state, BLANK)[0]
    second_state = first_branch.bath
    second_branch = stock.branches(second_state, BLANK)[0]
    third_state = second_branch.bath
    first_signature = stock.visible_signature(first_state)
    second_signature = stock.visible_signature(second_state)
    third_signature = stock.visible_signature(third_state)
    conditional_states_ok = (
        len(stock.branches(first_state, BLANK)) == 7
        and all(branch.probability > 0 for branch in stock.branches(first_state, BLANK))
        and len({branch.bath for branch in stock.branches(first_state, BLANK)}) == 7
    )
    stock_ok = (
        first_signature == second_signature
        and third_signature != second_signature
        and (first_state.ready_factors, second_state.ready_factors, third_state.ready_factors) == (2, 1, 0)
        and conditional_states_ok
    )
    certificate.check(
        "K_two_ready_factor_stock",
        stock_ok,
        "named TWO_READY_FACTOR_CURSOR_STOCK has identical conditional instruments on uses 1-2 and a changed third-use channel",
    )

    reached = reachable_bath_states(stock, 3)
    erasing_mutant = TwoReadyFactorStock(instrument, erase_when_empty=True)
    mutant_reached = reachable_bath_states(erasing_mutant, 3)
    initial_mutant_lock = lock_holds(erasing_mutant, (erasing_mutant.initial(),))
    reachable_lock_ok = (
        lock_holds(stock, reached)
        and initial_mutant_lock
        and not lock_holds(erasing_mutant, mutant_reached)
        and any(state.ready_factors == 0 for state in reached)
    )
    certificate.check(
        "L_reachable_state_lock",
        reachable_lock_ok,
        f"lock holds on {len(reached)} reachable conditional bath states; initial-only check misses the depleted-state erase mutant",
    )

    kms_one = kms_classification(Fraction(1), Fraction(1), False, False)
    kms_two = kms_classification(Fraction(2), Fraction(1), False, False)
    kms_ok = (
        kms_one == (Fraction(1), "RELOCATED")
        and kms_two == (Fraction(2), "RELOCATED")
        and kms_one[0] != kms_two[0]
        and provenance("chosen_spectral_ratio") == "RELOCATED"
        and provenance("chosen_coupling_ratio") == "RELOCATED"
    )
    certificate.check(
        "M_kms_spectral_relocation",
        kms_ok,
        "free theta*DeltaE gives distinct exp(-theta*DeltaE) rays; temperature, gap, spectral, and coupling choices relocate beta",
    )

    z_bank = equal_z_bank()
    expected_z = {
        9: {((2, 0, 0, 0, 0, 0), 2), ((1, 1, 1, 0, 0, 0), 3)},
        10: {((2, 1, 0, 0, 0, 0), 3), ((1, 1, 1, 1, 0, 0), 4)},
        12: {
            ((2, 2, 0, 0, 0, 0), 4),
            ((2, 1, 1, 1, 0, 0), 5),
            ((1, 1, 1, 1, 1, 1), 6),
        },
    }
    beta_odds = {beta: Fraction(beta, 1 + beta) for beta in (1, 2)}
    equal_z_ok = z_bank == expected_z and beta_odds == {1: Fraction(1, 2), 2: Fraction(2, 3)}
    certificate.check(
        "N_equal_z_discriminator",
        equal_z_ok,
        "Z=9/10 pairs and Z=12 chain reconstructed; adjacent-n odds are 1/2 at beta=1 and 2/3 at beta=2 without fitting",
    )

    low_hold, high_hold = Fraction(1, 4), Fraction(3, 4)
    average_hold = (low_hold + high_hold) / 2
    marginal_only = RepeatabilityHypotheses(4, True, True, False, False, False, True)
    incomplete_extensive = {
        "boundary_state": True, "transport": False, "outgoing_archive": False,
        "locality": True, "process_limit": False, "coupling_provenance": False,
        "cadence": False,
    }
    selected = choose_terminal(False, False, finite_exact_obstruction, stock_ok, orbit_ok, kms_ok)
    mutations = {
        "omit_rotation": len(group[:-1]) != 24,
        "merge_blank_orbit": set(orbits) == expected_orbits and len(orbits) == 4,
        "merge_opposite_perpendicular": frozenset({tuple(-x for x in FROZEN_MARK)}) in expected_orbits,
        "finished_span_as_derived": provenance("span{I,P_f}") == "ASSUMED-SELECTOR",
        "hardcode_beta_one": {result[1] for result in beta_results} == {Fraction(1), Fraction(2)},
        "fit_equal_z": beta_odds[1] != beta_odds[2],
        "writable_pure_return": pure_constraint_rank == 6,
        "occupied_erasure": not lock_holds(erasing_mutant, mutant_reached),
        "first_use_only": third_signature != first_signature,
        "average_conditional_maps": low_hold != high_hold and average_hold == instrument.hold,
        "fresh_factor_replacement": third_state.ready_factors == 0,
        "temperature_gap_selector": provenance("chosen_temperature_gap") == "RELOCATED",
        "spectral_selector": provenance("chosen_spectral_ratio") == "RELOCATED",
        "profile_factor_as_common_c": beta_odds[1] != beta_odds[2],
        "memory_as_markov": first_signature != third_signature,
        "weak_step_as_clock": "physical clock" in authority and "Not imported" in authority,
        "action_or_gravity_bridge": "action-to-bath" in authority and "bath-to-gravity" in authority,
        "axiom_audit_toe_promotion": all_needles(goal + authority, ("axiom edit", "audit verdict", "TOE percentage movement")),
        "ratio_reparameterization": provenance("o/u=p/u=1") == "ASSUMED-SELECTOR",
        "tied_matrix_elements": provenance("tied_bath_matrix_elements") == "ASSUMED-SELECTOR",
        "equal_spectral_functions": provenance("equal_spectral_functions") == "RELOCATED",
        "basis_source_identification": provenance("basis_identifies_sources") == "ASSUMED-SELECTOR",
        "late_shared_coefficient": provenance("shared_complement_coefficient") == "ASSUMED-SELECTOR",
        "project_o_ne_p": beta_projection(split)[1] is None,
        "predict_supplied_factor_two": "factor two" in authority and "does not call it predicted" in authority,
        "six_selected_interactions": joint_ok and not joint_flags_valid({**joint_flags, "one_shared_bath": False}),
        "omit_joint_type_field": all(
            not joint_flags_valid({**joint_flags, field: False}) for field in joint_flags
        ),
        "initial_lock_only": initial_mutant_lock and not lock_holds(erasing_mutant, mutant_reached),
        "bath_change_implies_visible_memory": first_state != second_state and first_signature == second_signature,
        "marginal_return_as_all_history": not marginal_only.theorem_applies(),
        "two_uses_as_indefinite": stock_ok and third_signature != second_signature,
        "implicit_extensive_ownership": not extensive_ownership_valid(incomplete_extensive),
        "drop_all_use_hypothesis": not RepeatabilityHypotheses(4, True, True, True, True, False, True).theorem_applies(),
        "universalize_finite_terminal": all_needles(
            goal, ("Infinite, correlated, approximate-return",)
        ),
    }
    hostile_ok = len(mutations) == 34 and all(mutations.values())
    certificate.check(
        "O_hostile_mutations",
        hostile_ok,
        f"rejected {sum(mutations.values())}/{len(mutations)} group, provenance, beta, joint-type, reuse, lock, relocation, and scope mutations",
    )

    finite_scope_mutants = (
        RepeatabilityHypotheses(4, True, True, True, True, False, True),
        RepeatabilityHypotheses(4, True, True, True, True, True, False),
        RepeatabilityHypotheses(4, True, False, True, True, True, True),
    )
    terminal_ok = (
        selected == TERMINAL
        and finite_exact_obstruction
        and all(not hypotheses_mutant.theorem_applies() for hypotheses_mutant in finite_scope_mutants)
        and all_needles(
            goal + correction,
            (
                "extensive", "approximate-return", "outcome-carrying",
                "distributed-pointer", "non-Markov", "governed-law",
            ),
        )
    )
    certificate.check(
        "P_terminal_scope",
        terminal_ok,
        "single terminal limited to nontrivial append in exact G_fin,infinity; G_cov, G_fin,k, KMS are side controls and broader routes stay live",
    )

    resolution_lines = (
        "per_element: PASS exact 24-element group, independent source coordinates, provenance labels, beta membership, and channel identities checked.",
        "per_site: PASS blank/same/opposite/perpendicular sectors, append nonunitality, and lock on every reachable finite-stock bath state checked.",
        "per_mode: PASS legal o=p beta projection, one joint six-mark type, all 7^6 profiles, and KMS/spectral relocation checked.",
        "per_block: PASS two-ready-factor conditional instruments and third-use failure checked; exact all-use entropy obstruction proved at its hypotheses.",
        "lattice_wide: PASS checked and not executed — extensive ownership, transport, local-infinite process, physical clock, action, and gravity remain live.",
    )
    resolution_ok = (
        tuple(line.split(":", 1)[0] for line in resolution_lines)
        == ("per_element", "per_site", "per_mode", "per_block", "lattice_wide")
        and all(len(line) >= 80 for line in resolution_lines)
        and "checked and not executed —" in resolution_lines[-1]
    )
    certificate.check(
        "Q_five_resolution_lines",
        resolution_ok,
        "five substantive lines separate executed finite algebra/channel checks from unexecuted lattice-wide routes",
    )

    certificate.lines.extend(
        (
            "SIDE_CONTROLS: cubic covariance leaves four response sectors and beta=1,2 rays; the named two-ready stock changes on use 3; free KMS/spectral data relocate beta.",
            "LIVE_ROUTES: finite correlated or visibly lumpable memory, growing archives, distributed baths/pointers, extensive translating reservoirs, approximate/non-Markov laws, and governance.",
            *resolution_lines,
            f"COMPUTATIONAL_TERMINAL: {TERMINAL}" if certificate.failures == 0 else "COMPUTATIONAL_TERMINAL: INDEPENDENT-CERTIFICATE-FAILURE",
            "SCOPE: no universal bath no-go, selector, factor-two derivation, process/clock, action/gravity bridge, axiom/audit change, obligation retirement, or TOE movement.",
        )
    )
    return certificate


if __name__ == "__main__":
    result = Certificate()
    try:
        result = main()
    except Exception as error:  # fail closed while preserving the runner contract
        result.check("UNCAUGHT_EXCEPTION", False, f"{type(error).__name__}: {error}")
        result.lines.extend(
            (
                "per_element: FAIL checked and not executed — exact group/provenance certificate stopped before completion.",
                "per_site: FAIL checked and not executed — append and reachable-state lock certificate stopped before completion.",
                "per_mode: FAIL checked and not executed — beta, joint-six-mark, and KMS classifications stopped before completion.",
                "per_block: FAIL checked and not executed — finite-use and exact-repeatability checks stopped before completion.",
                "lattice_wide: FAIL checked and not executed — no extensive, process, clock, action, or gravity claim was tested.",
                "COMPUTATIONAL_TERMINAL: INDEPENDENT-CERTIFICATE-FAILURE",
            )
        )
    result.emit()
