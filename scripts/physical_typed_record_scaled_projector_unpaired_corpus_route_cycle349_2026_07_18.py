#!/usr/bin/env python3
"""Cycle 349 priority Route 2: finite scaled-projector typed-Record corpus.

This runner joins four *finite, supplied* scaled-projector menu schemas to the
existing physical apparatus, fixed program-carrier, endpoint-registration, and
conditional typed-Record interfaces.  The tested schemas are complements,
same-ray splits, a four-term non-axis cancellation menu, and identity coins.
Paired two-axis and cubic menus are retained as controls.

The result is deliberately bounded.  Coefficients and program preparation are
supplied.  The endpoint is a three-label coarse group while the fine pointer
label remains explicit in each 43-M2 corpus atom.  Occurrence, commit, Record
typing, future-fibre certification, and permanence application remain supplied
inputs.  Numerical grades are evaluated only after a typed permanent corpus
has formed and never enter its hash or formation predicate.

Two non-main candidate commits are recorded only as quarantined comparators.
Their continuum theorem is not consumed here.  The runner rederives the finite
identities it tests and claims neither continuum coefficient/menu coverage nor
Born forcing.  Register widths are not nearest-neighbour support certificates.
"""

from __future__ import annotations

import ast
from contextlib import redirect_stdout
from dataclasses import dataclass, replace
from hashlib import sha256
from io import StringIO
from math import sqrt
from pathlib import Path
import subprocess
import sys
from typing import Callable

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as c317
import physical_fixed_program_carrier_two_use_cycle323_2026_07_18 as c323
import physical_endpoint_registration_process_route_cycle338_2026_07_18 as c338
import physical_registered_cylinder_future_equivalence_route_cycle342_2026_07_18 as c342


I2 = c317.I2
X = c317.X
Y = c317.Y
Z = c317.Z
TOL = 1.2e-10
CAMPAIGN_BASE = "0355ac4728f57d9fdc62cb27764bbd33e6e8b8df"
COMPARATOR_COMMITS = ("769950dc06", "5dd59abfbf")
QUARANTINED_RUNNERS = (
    "born_form_effect_menu_sitewise_forcing_2026_07_17",
    "born_form_scaled_projector_menu_family_sitewise_forcing_2026_07_17",
)
LENGTHS = (3, 6)
CORPUS_CASES = (("development-N3", 3, 3, False),
                ("development-N6", 3, 6, False),
                ("held-N12", 6, 12, True))

PREPARATION_BITS = 2
PROGRAM_BITS = 3
FINE_POINTER_BITS = 3
TRIAL_BITS = 4
USE_BITS = 1
CORPUS_TAG_BITS = (
    PREPARATION_BITS
    + PROGRAM_BITS
    + FINE_POINTER_BITS
    + TRIAL_BITS
    + USE_BITS
)
CORPUS_RECORD_BITS = c342.RECORD_BITS + CORPUS_TAG_BITS

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def unit(vector: tuple[float, float, float] | np.ndarray) -> np.ndarray:
    result = np.asarray(vector, dtype=float)
    if result.shape != (3,) or np.linalg.norm(result) < TOL:
        raise ValueError("a scaled-projector direction must be a nonzero three-vector")
    return result / np.linalg.norm(result)


@dataclass(frozen=True)
class ScaledTerm:
    """One nonzero c P(n), or one nonzero c I, in a finite tested menu."""

    scale: float
    direction: tuple[float, float, float] | None

    def __post_init__(self) -> None:
        if not 0 < self.scale <= 1:
            raise ValueError("a tested scaled effect has coefficient in (0,1]")
        if self.direction is not None:
            normalized = unit(self.direction)
            object.__setattr__(
                self, "direction", tuple(float(value) for value in normalized)
            )

    @property
    def identity(self) -> bool:
        return self.direction is None

    def bare_effect(self) -> np.ndarray:
        if self.identity:
            return self.scale * I2
        assert self.direction is not None
        return self.scale * c317.projector_bloch(np.asarray(self.direction))


@dataclass(frozen=True)
class MenuSchema:
    name: str
    family: str
    terms: tuple[ScaledTerm, ...]
    coarse_groups: tuple[tuple[int, ...], ...]
    expected_paired: bool

    def __post_init__(self) -> None:
        if not 1 <= len(self.terms) <= 8:
            raise ValueError("one bounded schema has one to eight fine labels")
        flattened = tuple(index for group in self.coarse_groups for index in group)
        if sorted(flattened) != list(range(len(self.terms))):
            raise ValueError("coarse endpoint groups must partition fine labels")
        if len(self.coarse_groups) > len(c338.ENDPOINT_LABELS):
            raise ValueError("the current registered endpoint has only three labels")

    def program(self, contact: np.ndarray) -> c323.c321.Program:
        kraus = tuple(
            sqrt(term.scale)
            * (
                I2
                if term.identity
                else c317.projector_bloch(np.asarray(term.direction))
            )
            @ contact
            for term in self.terms
        )
        return c323.c321.Program(self.name, kraus, self.coarse_groups)

    def endpoint(self, fine_label: int) -> int:
        if not 0 <= fine_label < len(self.terms):
            raise ValueError("fine pointer label is outside the installed schema")
        return next(
            endpoint
            for endpoint, group in enumerate(self.coarse_groups)
            if fine_label in group
        )


def opposite(left: tuple[float, float, float], right: tuple[float, float, float]) -> bool:
    return np.linalg.norm(np.asarray(left) + np.asarray(right)) < TOL


def paired_menu(schema: MenuSchema) -> bool:
    """Finite paired-family test: identities are allowed; rays pair antipodally."""

    rays = [term for term in schema.terms if not term.identity]
    used: set[int] = set()
    for left_index, left in enumerate(rays):
        if left_index in used:
            continue
        assert left.direction is not None
        partner = next(
            (
                right_index
                for right_index, right in enumerate(rays)
                if right_index not in used
                and right_index != left_index
                and abs(right.scale - left.scale) < TOL
                and right.direction is not None
                and opposite(left.direction, right.direction)
            ),
            None,
        )
        if partner is None:
            return False
        used.update((left_index, partner))
    return True


def axis_cancellation_terms(
    direction: tuple[float, float, float]
) -> tuple[ScaledTerm, ...]:
    n = unit(direction)
    if np.any(abs(n) < TOL):
        raise ValueError("the generic four-term axis cancellation has no zero component")
    coefficient = 2 / (1 + float(np.sum(abs(n))))
    terms = [ScaledTerm(coefficient, tuple(n))]
    for axis in range(3):
        basis = np.zeros(3)
        basis[axis] = -np.sign(n[axis])
        terms.append(
            ScaledTerm(coefficient * abs(float(n[axis])), tuple(basis))
        )
    return tuple(terms)


def schema_table(*, held: bool) -> tuple[MenuSchema, ...]:
    split_direction = unit((3, -4, 0) if held else (2, -3, 6))
    split = 0.23 if held else 0.37
    axis_direction = (-4, 1, 2) if held else (1, 2, 3)
    paired_left = unit((-2, 5, 1) if held else (1, -1, 2))
    paired_right = unit((1, 3, -4) if held else (2, 3, -1))

    complement = MenuSchema(
        "held complement" if held else "development complement",
        "complement",
        (
            ScaledTerm(1.0, tuple(split_direction)),
            ScaledTerm(1.0, tuple(-split_direction)),
        ),
        ((0,), (1,)),
        True,
    )
    ray_split = MenuSchema(
        "held same-ray split" if held else "development same-ray split",
        "same-ray split",
        (
            ScaledTerm(split, tuple(split_direction)),
            ScaledTerm(1 - split, tuple(split_direction)),
            ScaledTerm(1.0, tuple(-split_direction)),
        ),
        ((0,), (1,), (2,)),
        False,
    )
    axis = MenuSchema(
        "held non-axis cancellation" if held else "development non-axis cancellation",
        "axis cancellation",
        axis_cancellation_terms(axis_direction),
        ((0,), (1,), (2, 3)),
        False,
    )
    coins = MenuSchema(
        "identity quarter coins",
        "identity coins",
        (ScaledTerm(0.25, None), ScaledTerm(0.25, None), ScaledTerm(0.5, None)),
        ((0,), (1,), (2,)),
        True,
    )
    paired_axes = MenuSchema(
        "held paired two-axis control" if held else "development paired two-axis control",
        "paired two-axis control",
        (
            ScaledTerm(0.32, tuple(paired_left)),
            ScaledTerm(0.32, tuple(-paired_left)),
            ScaledTerm(0.68, tuple(paired_right)),
            ScaledTerm(0.68, tuple(-paired_right)),
        ),
        ((0, 1), (2, 3)),
        True,
    )
    cubic = MenuSchema(
        "paired cubic control",
        "paired cubic control",
        tuple(
            ScaledTerm(1 / 3, tuple(sign * np.eye(3)[axis]))
            for axis in range(3)
            for sign in (1, -1)
        ),
        ((0, 1), (2, 3), (4, 5)),
        True,
    )
    return complement, ray_split, axis, coins, paired_axes, cubic


@dataclass(frozen=True)
class CorpusRecord:
    record: c342.CylinderRecord
    preparation: int
    program: int
    fine_pointer: int
    trial: int
    use: int

    def __post_init__(self) -> None:
        for name, value, bound in (
            ("preparation", self.preparation, 2**PREPARATION_BITS),
            ("program", self.program, 6),
            ("fine pointer", self.fine_pointer, 2**FINE_POINTER_BITS),
            ("trial", self.trial, 2**TRIAL_BITS),
            ("use", self.use, 2**USE_BITS),
        ):
            if not isinstance(value, int) or not 0 <= value < bound:
                raise ValueError(f"{name} is outside its declared M2 register")
        if not self.record.typed or not self.record.permanent:
            raise ValueError("a corpus atom requires one typed permanent Cylinder Record")


def corpus_record_word(record: CorpusRecord) -> tuple[int, ...]:
    word = (
        c342.record_word(record.record)
        + c338.bits(record.preparation, PREPARATION_BITS)
        + c338.bits(record.program, PROGRAM_BITS)
        + c338.bits(record.fine_pointer, FINE_POINTER_BITS)
        + c338.bits(record.trial, TRIAL_BITS)
        + c338.bits(record.use, USE_BITS)
    )
    if len(word) != CORPUS_RECORD_BITS:
        raise RuntimeError("the 43-M2 corpus-Record inventory drifted")
    return word


def corpus_hash(corpus: tuple[CorpusRecord, ...]) -> str:
    payload = bytes(bit for record in corpus for bit in corpus_record_word(record))
    return sha256(payload).hexdigest()


@dataclass(frozen=True)
class FormationInputs:
    coefficient_table: bool = True
    program_prepared: bool = True
    pointer_one_hot: bool = True
    tag_binding: bool = True
    close: bool = True
    unique: bool = True
    transition: bool = True
    slot_blank: bool = True
    occurrence: bool = True
    commit: bool = True
    typing: bool = True
    permanence: bool = True
    fibre_certified: bool = True


def form_corpus_record(
    fixture: c338.RouteFixture,
    schemas: tuple[MenuSchema, ...],
    *,
    preparation: int,
    program: int,
    scheduled_program: int,
    fine_pointer: int,
    trial: int,
    use: int,
    realized_content: int | None = None,
    inputs: FormationInputs = FormationInputs(),
) -> CorpusRecord | None:
    """Exact grade-free formation connector to the Cycle-338/342 surfaces."""

    if not 0 <= program < len(schemas):
        raise ValueError("program label is outside the supplied six-program table")
    if scheduled_program != program:
        return None
    endpoint = schemas[program].endpoint(fine_pointer)
    if not (
        inputs.coefficient_table
        and inputs.program_prepared
        and inputs.pointer_one_hot
        and inputs.tag_binding
        and inputs.slot_blank
    ):
        return None
    content = endpoint if realized_content is None else realized_content
    packet = c338.lawful_packet(fixture, endpoint, trial % fixture.length)
    packet = replace(
        packet,
        content=content,
        close=int(inputs.close),
        unique=int(inputs.unique),
        transition=int(inputs.transition),
    )
    cylinder = c338.decode_cylinder(fixture, packet)
    if cylinder is None:
        return None
    record = c342.form_conditional_record(
        fixture,
        cylinder,
        occurrence=inputs.occurrence,
        commit=inputs.commit,
        typing=inputs.typing,
        permanence=inputs.permanence,
        fibre_certified=inputs.fibre_certified,
    )
    if not record.typed or not record.permanent:
        return None
    return CorpusRecord(
        record,
        preparation,
        program,
        fine_pointer,
        trial,
        use,
    )


def build_corpus(
    fixture: c338.RouteFixture,
    schemas: tuple[MenuSchema, ...],
    count: int,
) -> tuple[tuple[CorpusRecord, ...], c342.RecordBook]:
    records = []
    book = c342.empty_book(fixture.length)
    for trial in range(count):
        program = trial % len(schemas)
        fine = (trial // len(schemas) + program) % len(schemas[program].terms)
        record = form_corpus_record(
            fixture,
            schemas,
            preparation=trial % 4,
            program=program,
            scheduled_program=program,
            fine_pointer=fine,
            trial=trial,
            use=trial % 2,
        )
        if record is None:
            raise RuntimeError("a lawful grade-free corpus atom failed to form")
        try:
            book = c342.append_record(book, record.record)
        except ValueError:
            book = c342.attach_fresh_page(book, (None,) * fixture.length)
            book = c342.append_record(book, record.record)
        records.append(record)
    return tuple(records), book


def trace_grade(sigma: np.ndarray) -> Callable[[np.ndarray], float]:
    if sigma.shape != (2, 2) or np.min(np.linalg.eigvalsh(sigma)) < -TOL:
        raise ValueError("the finite trace comparator needs one density matrix")
    return lambda effect: float(np.trace(sigma @ effect).real)


def softened_lexicographic_complement_rogue(effect: np.ndarray) -> float:
    """Homogeneous 3/4--1/4 lexicographic complement witness.

    This finite comparator is intentionally not the landed 1/0 hemisphere
    assignment.  It shares the antipodal complement identity but keeps both
    ray values strictly inside (0,1).
    """

    eigenvalues = np.linalg.eigvalsh(effect)
    if abs(eigenvalues[1] - eigenvalues[0]) < TOL:
        return float(eigenvalues[0])
    coefficient = float(np.trace(effect).real)
    if not TOL < coefficient <= 1 + TOL or abs(eigenvalues[0]) > TOL:
        raise ValueError("rogue comparator is defined only on scaled rank-one/I effects")
    projector = effect / coefficient
    direction = np.asarray(
        [float(np.trace(projector @ pauli).real) for pauli in (X, Y, Z)]
    )
    for coordinate in direction:
        if abs(coordinate) > TOL:
            return coefficient * (0.75 if coordinate > 0 else 0.25)
    raise ValueError("a rank-one effect did not expose a Bloch direction")


def selected_effects(
    corpus: tuple[CorpusRecord, ...],
    carrier: c323.FixedProgramCarrier,
) -> tuple[np.ndarray, ...]:
    return tuple(
        carrier.programs[record.program].fine_effects[record.fine_pointer]
        for record in corpus
    )


def grade_view(
    corpus: tuple[CorpusRecord, ...],
    carrier: c323.FixedProgramCarrier,
    grade: Callable[[np.ndarray], float] | None,
) -> tuple[str, tuple[float, ...] | None]:
    digest = corpus_hash(corpus)
    if grade is None:
        return digest, None
    return digest, tuple(grade(effect) for effect in selected_effects(corpus, carrier))


def comparator_quarantine_controls() -> None:
    rows = []
    for commit in COMPARATOR_COMMITS:
        completed = subprocess.run(
            ["git", "merge-base", "--is-ancestor", commit, CAMPAIGN_BASE],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        rows.append(
            {
                "commit": commit,
                "campaign_base_ancestor": completed.returncode == 0,
                "returncode": completed.returncode,
            }
        )
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    imported_modules = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
        for alias in (
            node.names
            if isinstance(node, ast.Import)
            else [ast.alias(name=node.module or "")]
        )
    }
    source_audit = {
        runner: {
            "imported": runner in imported_modules,
            "present_in_campaign_tree": (ROOT / "scripts" / f"{runner}.py").exists(),
        }
        for runner in QUARANTINED_RUNNERS
    }
    check(
        "the two candidate theorem commits are outside the pinned campaign base and their runners are not consumed",
        all(not row["campaign_base_ancestor"] and row["returncode"] == 1 for row in rows)
        and all(
            not row["imported"] and not row["present_in_campaign_tree"]
            for row in source_audit.values()
        ),
        {
            "pinned_campaign_base": CAMPAIGN_BASE,
            "comparators": rows,
            "source_import_audit": source_audit,
            "theorem_consumed": False,
            "continuum_menu_coverage": False,
            "Born_forcing_claim": False,
        },
    )


def finite_schema_controls(
    physical_fixtures: dict[int, c317.PhysicalFixture],
) -> tuple[
    dict[str, tuple[MenuSchema, ...]],
    dict[str, c323.FixedProgramCarrier],
]:
    tables = {
        "development": schema_table(held=False),
        "held": schema_table(held=True),
    }
    carriers = {
        name: c323.FixedProgramCarrier(
            tuple(schema.program(physical_fixtures[3].contact) for schema in table)
        )
        for name, table in tables.items()
    }
    rows = []
    for name, schemas in tables.items():
        carrier = carriers[name]
        paired = tuple(paired_menu(schema) for schema in schemas)
        completeness = tuple(
            float(np.linalg.norm(program.completeness - I2))
            for program in carrier.programs
        )
        bare_completeness = tuple(
            float(
                np.linalg.norm(
                    sum(
                        (term.bare_effect() for term in schema.terms),
                        start=np.zeros((2, 2), dtype=complex),
                    )
                    - I2
                )
            )
            for schema in schemas
        )
        rows.append(
            {
                "table": name,
                "programs": len(schemas),
                "families": tuple(schema.family for schema in schemas),
                "fine_labels": tuple(len(schema.terms) for schema in schemas),
                "paired": paired,
                "expected_paired": tuple(schema.expected_paired for schema in schemas),
                "maximum_operator_completeness": max(completeness),
                "maximum_bare_menu_completeness": max(bare_completeness),
                "axis_terms": len(schemas[2].terms),
            }
        )
    check(
        "two supplied bounded coefficient tables physicalize all four finite schemas and paired controls with an explicit unpaired menu",
        all(
            row["programs"] == 6
            and row["families"][:4]
            == ("complement", "same-ray split", "axis cancellation", "identity coins")
            and max(row["fine_labels"]) <= 8
            and row["paired"] == row["expected_paired"]
            and row["paired"] == (True, False, False, True, True, True)
            and row["axis_terms"] == 4
            and row["maximum_operator_completeness"] < TOL
            and row["maximum_bare_menu_completeness"] < TOL
            for row in rows
        ),
        rows,
    )
    return tables, carriers


def fixed_carrier_and_physical_controls(
    physical_fixtures: dict[int, c317.PhysicalFixture],
    carriers: dict[str, c323.FixedProgramCarrier],
) -> None:
    rows = []
    for name, carrier in carriers.items():
        old_pass, old_fail = c323.PASS, c323.FAIL
        c323.PASS = c323.FAIL = 0
        with redirect_stdout(StringIO()):
            carrier_detail = c323.carrier_program_controls(carrier)
            sequence_detail = c323.sequential_composition_controls(carrier)
            support = c323.physical_embedding_and_support_controls(
                physical_fixtures, carrier
            )
            covariance = c323.covariance_controls(physical_fixtures, carrier)
        imported_green = c323.PASS == 4 and c323.FAIL == 0
        c323.PASS, c323.FAIL = old_pass, old_fail
        rows.append(
            {
                "table": name,
                "imported_current_main_checks_green": imported_green,
                "fixed_update_isometry_residual": carrier_detail[
                    "fixed_update_isometry_residual"
                ],
                "two_use_isometry_residual": sequence_detail[
                    "two_use_isometry_residual"
                ],
                "fresh_pointer_M2": sequence_detail["fresh_pointer_M2"],
                "support": support,
                "covariance": covariance,
            }
        )
    check(
        "the supplied schema tables run through one fixed three-M2 carrier, two fresh-pointer uses, bounded physical M2 patches, and all 24 frames",
        all(
            row["imported_current_main_checks_green"]
            and row["fixed_update_isometry_residual"] < TOL
            and row["two_use_isometry_residual"] < TOL
            and row["fresh_pointer_M2"] == 6
            and len(row["support"]) == 2
            and all(item["one_and_two_use_leakage"] < TOL for item in row["support"])
            and row["covariance"]["frames"] == 24
            and row["covariance"]["branch_failures"] == 0
            for row in rows
        ),
        rows,
    )


def registered_record_covariance_controls(
    fixtures: dict[int, c338.RouteFixture],
) -> None:
    old_pass, old_fail = c342.PASS, c342.FAIL
    c342.PASS = c342.FAIL = 0
    with redirect_stdout(StringIO()):
        detail = c342.frame_and_held_controls(fixtures)
    imported_green = c342.PASS == 1 and c342.FAIL == 0
    c342.PASS, c342.FAIL = old_pass, old_fail
    check(
        "the current registered Cylinder-Record surface remains covariant at L=3 and held L=6 in all 24 frames",
        imported_green
        and detail["frame_size_endpoint_record_cases"] == 648
        and detail["proper_cubic_frames_per_size"] == 24
        and detail["mapping_failures"] == 0
        and detail["typed_chain_failures"] == 0
        and detail["future_equivalence_covariance_failures"] == 0,
        detail,
    )


def corpus_controls(
    fixtures: dict[int, c338.RouteFixture],
    tables: dict[str, tuple[MenuSchema, ...]],
) -> dict[str, tuple[CorpusRecord, ...]]:
    corpora = {}
    rows = []
    for name, length, count, held in CORPUS_CASES:
        table_name = "held" if held else "development"
        corpus, book = build_corpus(fixtures[length], tables[table_name], count)
        corpora[name] = corpus
        words = tuple(corpus_record_word(record) for record in corpus)
        rows.append(
            {
                "case": name,
                "L": length,
                "held": held,
                "records": len(corpus),
                "pages": len(book.pages),
                "atom_M2": len(words[0]),
                "corpus_M2": sum(len(word) for word in words),
                "typed_permanent": all(
                    record.record.typed and record.record.permanent for record in corpus
                ),
                "programs_seen": tuple(sorted({record.program for record in corpus})),
                "unpaired_program_seen": any(record.program in (1, 2) for record in corpus),
                "hash": corpus_hash(corpus),
            }
        )
    check(
        "grade-free formation yields exact 43-M2 typed permanent corpora at N=3/6 development and N=12 held with supplied page renewal",
        tuple(row["records"] for row in rows) == (3, 6, 12)
        and tuple(row["pages"] for row in rows) == (1, 2, 2)
        and all(
            row["atom_M2"] == 43
            and row["corpus_M2"] == 43 * row["records"]
            and row["typed_permanent"]
            and row["unpaired_program_seen"]
            for row in rows
        )
        and rows[1]["programs_seen"] == tuple(range(6))
        and rows[2]["programs_seen"] == tuple(range(6)),
        rows,
    )
    return corpora


def finite_grade_controls(
    tables: dict[str, tuple[MenuSchema, ...]],
    carriers: dict[str, c323.FixedProgramCarrier],
    corpora: dict[str, tuple[CorpusRecord, ...]],
) -> None:
    bloch = np.asarray((0.21, -0.32, 0.41), dtype=float)
    sigma = (I2 + bloch[0] * X + bloch[1] * Y + bloch[2] * Z) / 2
    born = trace_grade(sigma)
    rows = []
    for name in ("development", "held"):
        schemas = tables[name]
        carrier = carriers[name]
        trace_sums = tuple(
            sum(born(effect) for effect in program.fine_effects)
            for program in carrier.programs
        )
        rogue_sums = tuple(
            sum(
                softened_lexicographic_complement_rogue(effect)
                for effect in program.fine_effects
            )
            for program in carrier.programs
        )
        paired_indices = tuple(
            index for index, schema in enumerate(schemas) if paired_menu(schema)
        )
        unpaired_indices = tuple(
            index for index, schema in enumerate(schemas) if not paired_menu(schema)
        )
        complement = carrier.programs[0].fine_effects
        split = carrier.programs[1].fine_effects
        rows.append(
            {
                "table": name,
                "trace_menu_residual": max(abs(value - 1) for value in trace_sums),
                "paired_indices": paired_indices,
                "unpaired_indices": unpaired_indices,
                "paired_rogue_residual": max(
                    abs(rogue_sums[index] - 1) for index in paired_indices
                ),
                "unpaired_rogue_residuals": tuple(
                    abs(rogue_sums[index] - 1) for index in unpaired_indices
                ),
                "axis_rogue_sum": rogue_sums[2],
                "trace_split_additivity": abs(
                    born(split[0]) + born(split[1]) - born(complement[0])
                ),
                "rogue_split_additivity": abs(
                    softened_lexicographic_complement_rogue(split[0])
                    + softened_lexicographic_complement_rogue(split[1])
                    - softened_lexicographic_complement_rogue(complement[0])
                ),
            }
        )
    check(
        "post-formation trace grades normalize every finite menu while the softened 3/4--1/4 lexicographic rogue normalizes paired controls and fails the generic unpaired axis schema",
        all(
            row["trace_menu_residual"] < TOL
            and row["paired_indices"] == (0, 3, 4, 5)
            and row["unpaired_indices"] == (1, 2)
            and row["paired_rogue_residual"] < TOL
            and max(row["unpaired_rogue_residuals"]) > 0.06
            and row["trace_split_additivity"] < TOL
            and row["rogue_split_additivity"] < TOL
            for row in rows
        ),
        {
            "sigma_eigenvalues": tuple(float(value) for value in np.linalg.eigvalsh(sigma)),
            "tables": rows,
            "finite_identity_only": True,
            "Born_forcing": False,
        },
    )

    held = corpora["held-N12"]
    carrier = carriers["held"]
    base_hash = corpus_hash(held)
    grades: tuple[Callable[[np.ndarray], float] | None, ...] = (
        born,
        softened_lexicographic_complement_rogue,
        lambda effect: 1 - born(effect),
        lambda effect: 0.0 if np.linalg.norm(effect - selected_effects(held, carrier)[0]) < TOL else born(effect),
        None,
    )
    views = tuple(grade_view(held, carrier, grade) for grade in grades)
    first = held[0]
    alternative_fine = next(
        label
        for label in range(len(tables["held"][first.program].terms))
        if tables["held"][first.program].endpoint(label)
        != first.record.cylinder.endpoint
    )
    changed = form_corpus_record(
        c338.build_fixture(6),
        tables["held"],
        preparation=first.preparation,
        program=first.program,
        scheduled_program=first.program,
        fine_pointer=alternative_fine,
        trial=first.trial,
        use=first.use,
    )
    if changed is None:
        raise RuntimeError("the endpoint-change control failed to form")
    changed_corpus = (changed,) + held[1:]
    check(
        "grade mutation, deletion, and a zeroed branch cannot alter the typed Record hash, while a lawful endpoint change must",
        all(digest == base_hash for digest, _scores in views)
        and views[-1][1] is None
        and views[3][1] is not None
        and views[3][1][0] == 0.0
        and changed.record.cylinder.endpoint != first.record.cylinder.endpoint
        and corpus_hash(changed_corpus) != base_hash,
        {
            "grade_views": len(views),
            "unique_Record_hashes_under_grades": len({item[0] for item in views}),
            "base_hash": base_hash,
            "changed_endpoint_hash": corpus_hash(changed_corpus),
            "changed_endpoint": (
                first.record.cylinder.endpoint,
                changed.record.cylinder.endpoint,
            ),
        },
    )


def deletion_and_domain_controls(
    fixtures: dict[int, c338.RouteFixture],
    tables: dict[str, tuple[MenuSchema, ...]],
    carriers: dict[str, c323.FixedProgramCarrier],
    corpora: dict[str, tuple[CorpusRecord, ...]],
) -> None:
    fixture = fixtures[3]
    schemas = tables["development"]
    base_kwargs = dict(
        fixture=fixture,
        schemas=schemas,
        preparation=0,
        program=0,
        scheduled_program=0,
        fine_pointer=0,
        trial=0,
        use=0,
    )
    deletion_names = (
        "coefficient_table",
        "program_prepared",
        "pointer_one_hot",
        "tag_binding",
        "close",
        "unique",
        "transition",
        "slot_blank",
        "occurrence",
        "commit",
        "typing",
        "permanence",
        "fibre_certified",
    )
    deletion_survivors = {
        name: form_corpus_record(
            **base_kwargs,
            inputs=replace(FormationInputs(), **{name: False}),
        )
        is not None
        for name in deletion_names
    }
    mismatch = form_corpus_record(**base_kwargs, realized_content=1)
    deleted_branch_defects = []
    for program in carriers["development"].programs:
        deleted = program.kraus[:-1]
        completeness = sum(
            (operator.conj().T @ operator for operator in deleted),
            start=np.zeros((2, 2), dtype=complex),
        )
        deleted_branch_defects.append(float(np.linalg.norm(completeness - I2)))

    corpus = corpora["development-N3"]
    book = c342.empty_book(3)
    for item in corpus:
        book = c342.append_record(book, item.record)
    retarget_rejected = False
    try:
        c342.erase_or_retarget_record(book, 0, 0, corpus[1].record)
    except ValueError:
        retarget_rejected = True

    rejected = 0
    malformed_calls = (
        lambda: unit((0, 0, 0)),
        lambda: ScaledTerm(-0.1, (1, 0, 0)),
        lambda: ScaledTerm(1.1, None),
        lambda: axis_cancellation_terms((1, 0, 2)),
        lambda: MenuSchema("bad groups", "bad", schemas[0].terms, ((0,),), True),
        lambda: CorpusRecord(corpus[0].record, 4, 0, 0, 0, 0),
        lambda: CorpusRecord(corpus[0].record, 0, 6, 0, 0, 0),
        lambda: CorpusRecord(corpus[0].record, 0, 0, 8, 0, 0),
        lambda: CorpusRecord(corpus[0].record, 0, 0, 0, 16, 0),
        lambda: CorpusRecord(corpus[0].record, 0, 0, 0, 0, 2),
        lambda: schemas[0].endpoint(8),
    )
    for call in malformed_calls:
        try:
            call()
        except ValueError:
            rejected += 1
    check(
        "every formation dependency, endpoint/content equality, fine branch, permanent Record, and declared domain remains load bearing",
        not any(deletion_survivors.values())
        and mismatch is None
        and min(deleted_branch_defects) > 0.17
        and retarget_rejected
        and rejected == len(malformed_calls),
        {
            "formation_deletion_survivors": deletion_survivors,
            "endpoint_content_mismatch_forms_Record": mismatch is not None,
            "fine_branch_deletion_defects": tuple(deleted_branch_defects),
            "permanent_retarget_rejected": retarget_rejected,
            "lawful_domain_rejections": rejected,
        },
    )


def held_coefficient_controls(tables: dict[str, tuple[MenuSchema, ...]]) -> None:
    development = tables["development"]
    held = tables["held"]
    dev_split_direction = np.asarray(development[1].terms[0].direction)
    held_split_direction = np.asarray(held[1].terms[0].direction)
    dev_split = development[1].terms[0].scale
    held_split = held[1].terms[0].scale
    dev_axis = np.asarray(development[2].terms[0].direction)
    held_axis = np.asarray(held[2].terms[0].direction)
    check(
        "held coefficients cross a new octant and a zero-component ray at a distinct split without claiming continuum coverage",
        tuple(np.sign(dev_axis).astype(int)) == (1, 1, 1)
        and tuple(np.sign(held_axis).astype(int)) == (-1, 1, 1)
        and abs(dev_split - 0.37) < TOL
        and abs(held_split - 0.23) < TOL
        and abs(float(held_split_direction[2])) < TOL
        and np.linalg.norm(dev_split_direction - held_split_direction) > 0.1,
        {
            "development_axis_octant": tuple(np.sign(dev_axis).astype(int)),
            "held_axis_octant": tuple(np.sign(held_axis).astype(int)),
            "development_split": dev_split,
            "held_split": held_split,
            "held_split_direction": tuple(float(value) for value in held_split_direction),
            "continuum_coefficient_coverage": False,
        },
    )


def semantic_firewall_controls() -> None:
    detail = {
        "result": "finite conditional physical typed-Record scaled-projector corpus",
        "coefficient_table": "supplied finite development/held tables",
        "program_preparation": "supplied",
        "pointer_blank_and_fine_label": "supplied physical interface inputs",
        "thirteen_M2_tag_binding": "supplied conditional wrapper around the Cycle-342 cylinder",
        "realized_endpoint_content": "supplied pointwise",
        "occurrence": "supplied",
        "commit": "supplied",
        "Record_typing": "supplied",
        "future_fibre_certificate": "supplied",
        "permanence_application": "supplied after lawful typing",
        "numerical_grade_selector": None,
        "continuum_coefficient_or_menu_coverage": False,
        "Born_forcing": False,
        "actual_history_sampler": None,
        "frequency_law": None,
        "record_atom_M2": CORPUS_RECORD_BITS,
        "record_atom_width_breakdown_M2": (30, 2, 3, 3, 4, 1),
        "record_width_is_nearest_neighbor_support": False,
        "nearest_neighbor_Record_support_certificate": None,
        "authority": "none",
        "audit": "unset",
        "broad_negative": None,
        "axiom_pressure": None,
    }
    check(
        "the bounded finite comparator keeps every supplied structure and semantic wall explicit",
        detail["numerical_grade_selector"] is None
        and detail["continuum_coefficient_or_menu_coverage"] is False
        and detail["Born_forcing"] is False
        and detail["actual_history_sampler"] is None
        and detail["frequency_law"] is None
        and detail["record_atom_M2"] == 43
        and sum(detail["record_atom_width_breakdown_M2"]) == 43
        and detail["record_width_is_nearest_neighbor_support"] is False
        and detail["nearest_neighbor_Record_support_certificate"] is None
        and detail["authority"] == "none"
        and detail["audit"] == "unset"
        and detail["broad_negative"] is None
        and detail["axiom_pressure"] is None,
        detail,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    comparator_quarantine_controls()
    physical_fixtures = {
        length: c317.physical_fixture(length) for length in LENGTHS
    }
    tables, carriers = finite_schema_controls(physical_fixtures)
    fixed_carrier_and_physical_controls(physical_fixtures, carriers)

    registration_fixtures = {
        length: c338.build_fixture(length) for length in LENGTHS
    }
    registered_record_covariance_controls(registration_fixtures)
    corpora = corpus_controls(registration_fixtures, tables)
    finite_grade_controls(tables, carriers, corpora)
    deletion_and_domain_controls(
        registration_fixtures, tables, carriers, corpora
    )
    held_coefficient_controls(tables)
    semantic_firewall_controls()

    check(
        "Cycle 349 is a bounded conditional unpaired-schema Record-corpus route, not continuum Born forcing or a shared obstruction",
        FAIL == 0,
        {
            "strongest_result": "finite grade-blind 43-M2 typed-Record corpus with one unpaired physical schema",
            "route_status": "bounded positive / conditional",
            "authority": "none",
            "audit": "unset",
            "negative_claim": None,
        },
    )
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    if FAIL:
        print("RESULT CYCLE349_SCALED_PROJECTOR_TYPED_RECORD_CORPUS_NOT_CERTIFIED")
        return 1
    print("RESULT CYCLE349_SCALED_PROJECTOR_TYPED_RECORD_CORPUS_GREEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
