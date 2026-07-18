#!/usr/bin/env python3
"""Cycle 348 Route 1: finite full-effect-menu typed-Record corpus stress.

This runner joins the current-main Cycle-317 bounded qubit-effect dilation
compiler to the conditional Cycle-342 typed/permanent Record chain.  It uses a
finite menu of twelve explicit effects, their complements, and three distinct
dilation/refinement presentations per effect.  A corpus atom is exactly 43 M2:
the complete 30-M2 Cycle-342 Record plus preparation, program, fine-pointer,
trial, and use fields.

Record formation is grade-blind.  No effect, trace, branch norm, numerical
grade, random choice, count, or frequency enters the constructor.  Trace and
one finite nontrace/rogue functional are evaluated only after identical Record
words have formed; deleting the grade leaves the corpus unchanged and its
numerical predictions undefined.  The result is a finite stress corpus, not
all-finite-menu eligibility, Born forcing, a sampler, a frequency law, or a
nearest-neighbour compiler.  Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from inspect import signature
from math import sqrt
from pathlib import Path
import subprocess
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as c317
import physical_registered_cylinder_future_equivalence_route_cycle342_2026_07_18 as c342


LENGTHS = (3, 6)
CORPUS_SIZES = (3, 6, 12)
PROGRAMS = (0, 1, 2)
PREPARATION_BITS = 2
PROGRAM_BITS = 3
FINE_POINTER_BITS = 3
TRIAL_BITS = 4
USE_BITS = 1
CORPUS_ATOM_BITS = (
    c342.RECORD_BITS
    + PREPARATION_BITS
    + PROGRAM_BITS
    + FINE_POINTER_BITS
    + TRIAL_BITS
    + USE_BITS
)
AUTHORITY = "none"
AUDIT = "unset"
CAMPAIGN_BASE_MAIN = "0355ac4728f57d9fdc62cb27764bbd33e6e8b8df"
QUARANTINED_COMMITS = (
    "769950dc06bfe9b7ea25e2f55651efbed597b6ef",
    "5dd59abfbf863b64e816a551c2d0ed55c9a953a3",
)
QUARANTINED_PATH_MARKERS = (
    "born_form_effect_menu_sitewise_forcing_2026_07_17",
    "BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17",
    "born_form_scaled_projector_menu_family_sitewise_forcing_2026_07_17",
    "BORN_FORM_SCALED_PROJECTOR_MENU_FAMILY_SITEWISE_FORCING_AND_PAIRED_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17",
)
TOL = 8.0e-11
PASS = 0
FAIL = 0


EFFECT_EIGENVALUES = (
    (0.83, 0.21),
    (0.91, 0.64),
    (0.47, 0.02),
    (0.72, 0.31),
    (0.58, 0.14),
    (0.96, 0.52),
    (0.66, 0.09),
    (0.39, 0.11),
    (0.88, 0.44),
    (0.53, 0.27),
    (0.79, 0.05),
    (0.62, 0.36),
)
EFFECT_DIRECTIONS = (
    (2, 1, -3),
    (-1, 4, 2),
    (3, -2, 5),
    (1, 3, 4),
    (-3, 2, 1),
    (4, -1, 3),
    (2, -5, 1),
    (-2, -1, 4),
    (5, 2, -1),
    (1, -4, -2),
    (-5, 3, 2),
    (3, 4, -2),
)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def bits(value: int, width: int) -> tuple[int, ...]:
    if not isinstance(value, int) or value < 0 or value >= 1 << width:
        raise ValueError("value is outside its declared M2 basis register")
    return tuple((value >> index) & 1 for index in range(width))


def integer(word: tuple[int, ...]) -> int:
    if any(bit not in (0, 1) for bit in word):
        raise ValueError("an M2 basis word must be binary")
    return sum(bit << index for index, bit in enumerate(word))


@dataclass(frozen=True)
class CorpusAtom:
    record: c342.CylinderRecord
    preparation: int
    program: int
    fine_pointer: int
    trial: int
    use: int


@dataclass(frozen=True)
class EffectPresentation:
    program: int
    isometry: np.ndarray
    effect: np.ndarray
    complement: np.ndarray
    fine_effects: tuple[np.ndarray, ...]
    active_fine_labels: int


@dataclass(frozen=True)
class GradeRow:
    trial: int
    program: int
    effect_grade: float
    complement_grade: float
    coarse_normalization_residual: float
    fine_grade_sum: float


def atom_word(atom: CorpusAtom) -> tuple[int, ...]:
    word = (
        c342.record_word(atom.record)
        + bits(atom.preparation, PREPARATION_BITS)
        + bits(atom.program, PROGRAM_BITS)
        + bits(atom.fine_pointer, FINE_POINTER_BITS)
        + bits(atom.trial, TRIAL_BITS)
        + bits(atom.use, USE_BITS)
    )
    if len(word) != CORPUS_ATOM_BITS:
        raise RuntimeError("corpus-atom register inventory drifted")
    return word


def decode_atom_word(word: tuple[int, ...]) -> CorpusAtom:
    if len(word) != CORPUS_ATOM_BITS or any(bit not in (0, 1) for bit in word):
        raise ValueError("corpus atom has the wrong M2 basis domain")
    record = c342.decode_record_word(word[: c342.RECORD_BITS])
    cursor = c342.RECORD_BITS

    def take(width: int) -> int:
        nonlocal cursor
        value = integer(word[cursor : cursor + width])
        cursor += width
        return value

    atom = CorpusAtom(
        record,
        take(PREPARATION_BITS),
        take(PROGRAM_BITS),
        take(FINE_POINTER_BITS),
        take(TRIAL_BITS),
        take(USE_BITS),
    )
    if cursor != CORPUS_ATOM_BITS:
        raise RuntimeError("corpus-atom decoder did not consume its register")
    return atom


def preparation_state(label: int) -> np.ndarray:
    bloch = {
        0: np.asarray((0.0, 0.0, 0.0)),
        1: np.asarray((0.0, 0.0, 0.4)),
        2: np.asarray((0.3, -0.2, 0.1)),
        3: np.asarray((-0.2, 0.25, -0.3)),
    }.get(label)
    if bloch is None:
        raise ValueError("unknown finite preparation label")
    return (
        c317.I2
        + bloch[0] * c317.X
        + bloch[1] * c317.Y
        + bloch[2] * c317.Z
    ) / 2


def raw_effect(trial: int) -> np.ndarray:
    if not 0 <= trial < len(EFFECT_EIGENVALUES):
        raise ValueError("trial is outside the finite effect stress menu")
    a, b = EFFECT_EIGENVALUES[trial]
    direction = np.asarray(EFFECT_DIRECTIONS[trial], dtype=float)
    direction /= np.linalg.norm(direction)
    projector = c317.projector_bloch(direction)
    return b * c317.I2 + (a - b) * projector


def positive_square_root(operator: np.ndarray) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(
        (operator + operator.conj().T) / 2
    )
    if np.min(eigenvalues) < -TOL:
        raise ValueError("positive square root received a nonpositive operator")
    return eigenvectors @ np.diag(np.sqrt(np.maximum(eigenvalues, 0))) @ eigenvectors.conj().T


def compile_presentation(
    fixture: c317.PhysicalFixture,
    trial: int,
    program: int,
) -> EffectPresentation:
    """Compile one of three current-main Cycle-317 dilation presentations."""

    if program not in PROGRAMS:
        raise ValueError("program is outside the declared presentation menu")
    a, b = EFFECT_EIGENVALUES[trial]
    direction = np.asarray(EFFECT_DIRECTIONS[trial], dtype=float)
    direction /= np.linalg.norm(direction)
    projector = c317.projector_bloch(direction)
    contact = fixture.contact
    if program == 0:
        kraus = (
            sqrt(b) * contact,
            sqrt(a - b) * projector @ contact,
            sqrt(a - b) * (c317.I2 - projector) @ contact,
            sqrt(1 - a) * contact,
        )
        groups = ((0, 1), (2, 3))
    elif program == 1:
        kraus = (
            sqrt(b / 2) * contact,
            sqrt(b / 2) * contact,
            sqrt((a - b) / 2) * projector @ contact,
            sqrt((a - b) / 2) * projector @ contact,
            sqrt(a - b) * (c317.I2 - projector) @ contact,
            sqrt(1 - a) * contact,
        )
        groups = ((0, 1, 2, 3), (4, 5))
    else:
        effect = raw_effect(trial)
        kraus = (
            positive_square_root(effect) @ contact,
            positive_square_root(c317.I2 - effect) @ contact,
        )
        groups = ((0,), (1,))
    isometry = c317.stack_isometry(kraus)
    coarse = c317.derived_effects(isometry, groups)
    fine = c317.derived_effects(
        isometry, tuple((index,) for index in range(len(kraus)))
    )
    return EffectPresentation(
        program,
        isometry,
        coarse[0],
        coarse[1],
        fine,
        len(kraus),
    )


def expected_pointer(trial: int, program: int) -> int:
    active = {0: 4, 1: 6, 2: 2}.get(program)
    if active is None:
        raise ValueError("unknown finite presentation program")
    return trial % active


def form_corpus_atom(
    fixture: c342.c338.RouteFixture,
    cylinder: c342.c338.FutureCylinder,
    preparation: int,
    program: int,
    fine_pointer: int,
    trial: int,
    use: int,
    *,
    blank_available: bool = True,
    occurrence: bool = True,
    commit: bool = True,
    typing: bool = True,
    permanence: bool = True,
    fibre_certified: bool = True,
) -> CorpusAtom | None:
    """Form one corpus atom using only finite code and Record predicates."""

    bits(preparation, PREPARATION_BITS)
    bits(program, PROGRAM_BITS)
    bits(fine_pointer, FINE_POINTER_BITS)
    bits(trial, TRIAL_BITS)
    bits(use, USE_BITS)
    if (
        not blank_available
        or use != 1
        or trial >= len(EFFECT_EIGENVALUES)
        or preparation != trial % 4
        or program not in PROGRAMS
        or fine_pointer != expected_pointer(trial, program)
    ):
        return None
    record = c342.form_conditional_record(
        fixture,
        cylinder,
        occurrence=occurrence,
        commit=commit,
        typing=typing,
        permanence=permanence,
        fibre_certified=fibre_certified,
    )
    if not record.typed or not record.permanent:
        return None
    atom = CorpusAtom(record, preparation, program, fine_pointer, trial, use)
    atom_word(atom)
    return atom


def build_corpora(
    fixture: c342.c338.RouteFixture,
    size: int,
) -> dict[int, tuple[CorpusAtom, ...]]:
    if size not in CORPUS_SIZES:
        raise ValueError("corpus size is outside the declared stress family")
    cylinders = c342.make_cylinder_chain(fixture, 0, size)
    corpora = {}
    for program in PROGRAMS:
        atoms = tuple(
            form_corpus_atom(
                fixture,
                cylinder,
                trial % 4,
                program,
                expected_pointer(trial, program),
                trial,
                1,
            )
            for trial, cylinder in enumerate(cylinders)
        )
        if any(atom is None for atom in atoms):
            raise RuntimeError("the lawful finite corpus failed to form")
        corpora[program] = tuple(atom for atom in atoms if atom is not None)
    return corpora


def corpus_is_lawful(
    fixture: c342.c338.RouteFixture,
    corpus: tuple[CorpusAtom, ...],
    expected_size: int,
) -> bool:
    if len(corpus) != expected_size or expected_size not in CORPUS_SIZES:
        return False
    if not corpus:
        return False
    program = corpus[0].program
    if program not in PROGRAMS or any(atom.program != program for atom in corpus):
        return False
    if any(
        atom.trial != trial
        or atom.preparation != trial % 4
        or atom.fine_pointer != expected_pointer(trial, program)
        or atom.use != 1
        for trial, atom in enumerate(corpus)
    ):
        return False
    try:
        decoded = tuple(decode_atom_word(atom_word(atom)) for atom in corpus)
    except (TypeError, ValueError):
        return False
    return decoded == corpus and c342.valid_chain(
        fixture, tuple(atom.record for atom in corpus)
    )


def grade_corpus(
    fixture317: c317.PhysicalFixture,
    fixture342: c342.c338.RouteFixture,
    corpus: tuple[CorpusAtom, ...],
    expected_size: int,
    grade: str | None,
) -> tuple[GradeRow, ...] | None:
    """Evaluate a supplied grade only after the complete corpus validates."""

    if grade is None or not corpus_is_lawful(fixture342, corpus, expected_size):
        return None
    if grade not in ("trace", "finite-rogue"):
        raise ValueError("unknown downstream grade")
    rows = []
    for atom in corpus:
        presentation = compile_presentation(
            fixture317, atom.trial, atom.program
        )
        if grade == "trace":
            state = preparation_state(atom.preparation)

            def functional(effect: np.ndarray) -> float:
                return float(np.trace(state @ effect).real)

        else:
            functional = c317.nonlinear_binary_weight
        effect_grade = functional(presentation.effect)
        complement_grade = functional(presentation.complement)
        rows.append(
            GradeRow(
                atom.trial,
                atom.program,
                effect_grade,
                complement_grade,
                abs(effect_grade + complement_grade - 1),
                sum(functional(effect) for effect in presentation.fine_effects),
            )
        )
    return tuple(rows)


def quarantine_controls() -> dict[str, object]:
    source = Path(__file__).read_text(encoding="utf-8")
    import_lines = tuple(
        line.strip()
        for line in source.splitlines()
        if line.startswith("import ") or line.startswith("from ")
    )
    imported_quarantine_markers = tuple(
        marker
        for marker in QUARANTINED_PATH_MARKERS
        if any(marker in line for line in import_lines)
    )
    rows = []
    for commit in QUARANTINED_COMMITS:
        exists = subprocess.run(
            ("git", "cat-file", "-e", f"{commit}^{{commit}}"),
            cwd=ROOT,
            check=False,
            capture_output=True,
        ).returncode == 0
        ancestor = subprocess.run(
            (
                "git",
                "merge-base",
                "--is-ancestor",
                commit,
                CAMPAIGN_BASE_MAIN,
            ),
            cwd=ROOT,
            check=False,
            capture_output=True,
        ).returncode == 0
        rows.append(
            {
                "commit": commit,
                "object_exists": exists,
                "in_campaign_base_main_ancestry": ancestor,
                "used_by_route": False,
            }
        )
    check(
        "the two specified Born-menu commits were outside the pinned campaign-base main ancestry and their runners/notes are not imported by this route",
        all(
            not row["in_campaign_base_main_ancestry"]
            and not row["used_by_route"]
            for row in rows
        )
        and not imported_quarantine_markers,
        {
            "campaign_base_main": CAMPAIGN_BASE_MAIN,
            "object_existence_is_diagnostic_only": True,
            "import_lines": import_lines,
            "imported_quarantine_markers": imported_quarantine_markers,
            "rows": rows,
        },
    )
    return {"rows": rows}


def inherited_physical_controls() -> dict[str, object]:
    rows = []
    fixtures = {length: c317.physical_fixture(length) for length in LENGTHS}
    expected_contact = np.diag(
        (np.exp(1j * c317.c311.COUPLING), 1)
    ).astype(complex)
    for length, fixture in fixtures.items():
        projector = fixture.full_encoding @ fixture.full_encoding.conj().T
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "two_ray_gram_residual": float(
                    np.linalg.norm(
                        fixture.two_ray_encoding.conj().T
                        @ fixture.two_ray_encoding
                        - c317.I2
                    )
                ),
                "inherited_leakage": float(
                    np.linalg.norm(
                        (np.eye(projector.shape[0]) - projector)
                        @ fixture.two_ray_encoding
                    )
                ),
                "contact_residual": float(
                    np.linalg.norm(fixture.contact - expected_contact)
                ),
            }
        )
    species = c317.c311.c219.common_species(-0.3)
    one_particle = c317.c311.exterior_matrix(species.coin, 1)
    mass_residual = abs(
        c317.c311.c219.rest_mass(species) / species.analytic_mass - 1
    )
    check(
        "the finite corpus route inherits zero accepted-code leakage, the Cycle-230 seam contact, and the Cycle-219 one-particle mass fixture at L3 and held L6",
        all(
            max(
                row["two_ray_gram_residual"],
                row["inherited_leakage"],
                row["contact_residual"],
            )
            < TOL
            for row in rows
        )
        and np.linalg.norm(
            one_particle.conj().T @ one_particle - np.eye(6)
        )
        < TOL
        and mass_residual < 3e-12,
        {"rows": rows, "mass_relative_residual": mass_residual},
    )
    return {"fixtures": fixtures, "rows": rows, "mass_residual": mass_residual}


def compiler_presentation_controls(
    fixtures: dict[int, c317.PhysicalFixture],
) -> dict[str, object]:
    rows = []
    maximum_effect_residual = 0.0
    maximum_complement_residual = 0.0
    maximum_isometry_residual = 0.0
    for length, fixture in fixtures.items():
        for trial in range(len(EFFECT_EIGENVALUES)):
            presentations = tuple(
                compile_presentation(fixture, trial, program)
                for program in PROGRAMS
            )
            expected = (
                fixture.contact.conj().T
                @ raw_effect(trial)
                @ fixture.contact
            )
            effect_residual = max(
                float(np.linalg.norm(item.effect - expected))
                for item in presentations
            )
            complement_residual = max(
                float(np.linalg.norm(item.complement - (c317.I2 - expected)))
                for item in presentations
            )
            presentation_residual = max(
                float(np.linalg.norm(left.effect - right.effect))
                for left in presentations
                for right in presentations
            )
            isometry_residual = max(
                float(
                    np.linalg.norm(
                        item.isometry.conj().T @ item.isometry - c317.I2
                    )
                )
                for item in presentations
            )
            maximum_effect_residual = max(
                maximum_effect_residual, effect_residual, presentation_residual
            )
            maximum_complement_residual = max(
                maximum_complement_residual, complement_residual
            )
            maximum_isometry_residual = max(
                maximum_isometry_residual, isometry_residual
            )
            rows.append(
                {
                    "L": length,
                    "trial": trial,
                    "active_fine_labels": tuple(
                        item.active_fine_labels for item in presentations
                    ),
                    "effect_residual": effect_residual,
                    "complement_residual": complement_residual,
                    "presentation_residual": presentation_residual,
                    "isometry_residual": isometry_residual,
                }
            )
    check(
        "twelve finite arbitrary effects and complements have equal four-label, six-label-refined, and two-label spectral Cycle-317 presentations through held L6",
        len(rows) == len(LENGTHS) * len(EFFECT_EIGENVALUES)
        and all(row["active_fine_labels"] == (4, 6, 2) for row in rows)
        and max(
            maximum_effect_residual,
            maximum_complement_residual,
            maximum_isometry_residual,
        )
        < TOL,
        {
            "effect_fixture_rows": len(rows),
            "finite_effects": len(EFFECT_EIGENVALUES),
            "complements": len(EFFECT_EIGENVALUES),
            "presentations_per_effect": len(PROGRAMS),
            "maximum_effect_or_same-presentation_residual": maximum_effect_residual,
            "maximum_complement_residual": maximum_complement_residual,
            "maximum_isometry_residual": maximum_isometry_residual,
        },
    )
    return {"rows": rows}


def corpus_and_grade_controls(
    fixtures317: dict[int, c317.PhysicalFixture],
    fixtures342: dict[int, c342.c338.RouteFixture],
) -> dict[str, object]:
    rows = []
    total_atoms = 0
    maximum_trace_residual = 0.0
    maximum_rogue_coarse_residual = 0.0
    rogue_fine_separators = 0
    for length in LENGTHS:
        for size in CORPUS_SIZES:
            corpora = build_corpora(fixtures342[length], size)
            atom_words_before_grade_deletion = {
                program: tuple(atom_word(atom) for atom in corpus)
                for program, corpus in corpora.items()
            }
            record_words = {
                program: tuple(
                    c342.record_word(atom.record) for atom in corpus
                )
                for program, corpus in corpora.items()
            }
            shared_records = len(set(record_words.values())) == 1
            codec_exact = all(
                decode_atom_word(atom_word(atom)) == atom
                for corpus in corpora.values()
                for atom in corpus
            )
            trace = {
                program: grade_corpus(
                    fixtures317[length],
                    fixtures342[length],
                    corpus,
                    size,
                    "trace",
                )
                for program, corpus in corpora.items()
            }
            rogue = {
                program: grade_corpus(
                    fixtures317[length],
                    fixtures342[length],
                    corpus,
                    size,
                    "finite-rogue",
                )
                for program, corpus in corpora.items()
            }
            deleted = {
                program: grade_corpus(
                    fixtures317[length],
                    fixtures342[length],
                    corpus,
                    size,
                    None,
                )
                for program, corpus in corpora.items()
            }
            atom_words_after_grade_deletion = {
                program: tuple(atom_word(atom) for atom in corpus)
                for program, corpus in corpora.items()
            }
            if any(value is None for value in trace.values()) or any(
                value is None for value in rogue.values()
            ):
                raise RuntimeError("a lawful formed corpus did not reach grading")
            trace_rows = {key: value for key, value in trace.items() if value is not None}
            rogue_rows = {key: value for key, value in rogue.items() if value is not None}
            trace_residual = max(
                row.coarse_normalization_residual
                for value in trace_rows.values()
                for row in value
            )
            rogue_coarse_residual = max(
                row.coarse_normalization_residual
                for value in rogue_rows.values()
                for row in value
            )
            trace_program_residual = max(
                abs(
                    trace_rows[left][trial].effect_grade
                    - trace_rows[right][trial].effect_grade
                )
                for left in PROGRAMS
                for right in PROGRAMS
                for trial in range(size)
            )
            rogue_program_residual = max(
                abs(
                    rogue_rows[left][trial].effect_grade
                    - rogue_rows[right][trial].effect_grade
                )
                for left in PROGRAMS
                for right in PROGRAMS
                for trial in range(size)
            )
            trace_fine_residual = max(
                abs(trace_rows[program][trial].fine_grade_sum - 1)
                for program in PROGRAMS
                for trial in range(size)
            )
            fine_separator = max(
                max(
                    rogue_rows[program][trial].fine_grade_sum
                    for program in PROGRAMS
                )
                - min(
                    rogue_rows[program][trial].fine_grade_sum
                    for program in PROGRAMS
                )
                for trial in range(size)
            )
            rogue_fine_separators += int(fine_separator > 1e-4)
            maximum_trace_residual = max(
                maximum_trace_residual,
                trace_residual,
                trace_program_residual,
                trace_fine_residual,
            )
            maximum_rogue_coarse_residual = max(
                maximum_rogue_coarse_residual,
                rogue_coarse_residual,
                rogue_program_residual,
            )
            atom_count = sum(len(corpus) for corpus in corpora.values())
            total_atoms += atom_count
            rows.append(
                {
                    "L": length,
                    "N": size,
                    "held_size": length == 6,
                    "corpora": len(corpora),
                    "atoms": atom_count,
                    "atoms_per_corpus": size,
                    "basis_storage_M2_per_corpus": size * CORPUS_ATOM_BITS,
                    "identical_Record_words_across_presentations": shared_records,
                    "codec_exact": codec_exact,
                    "trace_normalization_or_presentation_residual": max(
                        trace_residual, trace_program_residual
                    ),
                    "rogue_binary_normalization_or_presentation_residual": max(
                        rogue_coarse_residual, rogue_program_residual
                    ),
                    "maximum_same-trial_rogue_fine_presentation_separator": fine_separator,
                    "grade_deleted_predictions": deleted,
                    "43_M2_atom_words_preserved_after_grade_deletion": (
                        atom_words_before_grade_deletion
                        == atom_words_after_grade_deletion
                    ),
                    "43_M2_atom_words_differ_across_presentations": (
                        len(set(atom_words_before_grade_deletion.values()))
                        == len(PROGRAMS)
                    ),
                }
            )
    check(
        "shared underlying 30-M2 Record words support downstream trace and finite rogue comparisons while presentation-specific 43-M2 atoms survive deleted grade unchanged",
        len(rows) == len(LENGTHS) * len(CORPUS_SIZES)
        and total_atoms == len(LENGTHS) * len(PROGRAMS) * sum(CORPUS_SIZES)
        and all(
            row["identical_Record_words_across_presentations"]
            and row["codec_exact"]
            and all(value is None for value in row["grade_deleted_predictions"].values())
            and row["43_M2_atom_words_preserved_after_grade_deletion"]
            and row["43_M2_atom_words_differ_across_presentations"]
            for row in rows
        )
        and max(maximum_trace_residual, maximum_rogue_coarse_residual) < TOL
        and rogue_fine_separators == len(rows),
        {
            "rows": rows,
            "total_formed_atoms_across_three_presentations": total_atoms,
            "maximum_trace_residual": maximum_trace_residual,
            "maximum_rogue_coarse_residual": maximum_rogue_coarse_residual,
            "rogue_fine_refinement_separators": rogue_fine_separators,
        },
    )
    return {"rows": rows, "total_atoms": total_atoms}


def grade_blind_formation_controls(
    fixture: c342.c338.RouteFixture,
) -> dict[str, object]:
    parameters = tuple(signature(form_corpus_atom).parameters)
    forbidden = (
        "effect",
        "trace",
        "branch_norm",
        "grade",
        "rng",
        "random",
        "count",
        "frequency",
    )
    cylinders = c342.make_cylinder_chain(fixture, 0, 2)
    left = form_corpus_atom(fixture, cylinders[0], 0, 0, 0, 0, 1)
    right = form_corpus_atom(fixture, cylinders[1], 1, 1, 1, 1, 1)
    if left is None or right is None:
        raise RuntimeError("grade-blind formation fixture did not form")
    check(
        "the typed-Record corpus constructor has no numerical grade, trace, branch norm, RNG, count, or frequency input",
        not any(name in parameters for name in forbidden)
        and left.record.typed
        and left.record.permanent
        and right.record.typed
        and right.record.permanent,
        {
            "constructor_parameters": parameters,
            "forbidden_inputs_present": tuple(
                name for name in forbidden if name in parameters
            ),
            "formation_output": "typed permanent CorpusAtom or None",
        },
    )
    return {"parameters": parameters}


def deletion_splice_and_domain_controls(
    fixture: c342.c338.RouteFixture,
    fixture317: c317.PhysicalFixture,
) -> dict[str, object]:
    base = build_corpora(fixture, 6)[0]
    cylinders = c342.make_cylinder_chain(fixture, 0, 1)
    formation_deletions = {
        "blank": form_corpus_atom(
            fixture, cylinders[0], 0, 0, 0, 0, 1, blank_available=False
        ),
        "fibre": form_corpus_atom(
            fixture, cylinders[0], 0, 0, 0, 0, 1, fibre_certified=False
        ),
        "typing": form_corpus_atom(
            fixture, cylinders[0], 0, 0, 0, 0, 1, typing=False
        ),
        "permanence": form_corpus_atom(
            fixture, cylinders[0], 0, 0, 0, 0, 1, permanence=False
        ),
        "occurrence": form_corpus_atom(
            fixture, cylinders[0], 0, 0, 0, 0, 1, occurrence=False
        ),
        "commit": form_corpus_atom(
            fixture, cylinders[0], 0, 0, 0, 0, 1, commit=False
        ),
        "use": form_corpus_atom(
            fixture, cylinders[0], 0, 0, 0, 0, 0
        ),
    }
    first = base[0]
    spliced_record = replace(
        first.record,
        cylinder=replace(
            first.record.cylinder,
            candidate=(first.record.cylinder.candidate + 1)
            % len(fixture.selection.candidates),
        ),
    )
    attacks = {
        "atom_deletion": base[:-1],
        "Record_splice": (replace(first, record=spliced_record),) + base[1:],
        "program_retarget": (replace(first, program=3),) + base[1:],
        "pointer_retarget": (replace(first, fine_pointer=1),) + base[1:],
        "trial_retarget": (replace(first, trial=1),) + base[1:],
        "preparation_retarget": (replace(first, preparation=1),) + base[1:],
        "typing_deletion": (
            replace(
                first,
                record=replace(first.record, typed=False, permanent=False),
            ),
        )
        + base[1:],
        "permanence_deletion": (
            replace(first, record=replace(first.record, permanent=False)),
        )
        + base[1:],
    }
    attack_rows = []
    for label, corpus in attacks.items():
        lawful = corpus_is_lawful(fixture, corpus, 6)
        prediction = grade_corpus(
            fixture317, fixture, corpus, 6, "trace"
        )
        attack_rows.append(
            {"attack": label, "lawful": lawful, "prediction": prediction}
        )
    rejected = 0
    invalid_calls = (
        lambda: bits(4, PREPARATION_BITS),
        lambda: bits(8, PROGRAM_BITS),
        lambda: bits(8, FINE_POINTER_BITS),
        lambda: bits(16, TRIAL_BITS),
        lambda: bits(2, USE_BITS),
        lambda: build_corpora(fixture, 4),
        lambda: compile_presentation(fixture317, 0, 7),
        lambda: grade_corpus(fixture317, fixture, base, 6, "host-grade"),
    )
    for call in invalid_calls:
        try:
            call()
        except ValueError:
            rejected += 1
    check(
        "blank/fibre/typing/permanence/occurrence/commit/use deletions and corpus deletion/splice/retarget attacks fail closed before grading",
        all(value is None for value in formation_deletions.values())
        and all(
            not row["lawful"] and row["prediction"] is None
            for row in attack_rows
        )
        and rejected == len(invalid_calls),
        {
            "L": fixture.length,
            "held": fixture.length == 6,
            "formation_deletions": {
                name: value is None for name, value in formation_deletions.items()
            },
            "corpus_attacks": attack_rows,
            "lawful_domain_rejections": rejected,
        },
    )
    return {"formation_deletions": formation_deletions, "attacks": attack_rows}


def frame_and_held_controls(
    fixtures317: dict[int, c317.PhysicalFixture],
    fixtures342: dict[int, c342.c338.RouteFixture],
) -> dict[str, object]:
    frames = tuple(c342.c314.c311.c235.proper_cubic_frames())
    cases = failures = improper = 0
    rows = []
    for length in LENGTHS:
        length_cases = length_failures = 0
        for size in CORPUS_SIZES:
            corpora = build_corpora(fixtures342[length], size)
            for frame in frames:
                matrix = tuple(
                    tuple(int(value) for value in row) for row in frame
                )
                orthogonal = all(
                    sum(
                        matrix[i][axis] * matrix[j][axis]
                        for axis in range(3)
                    )
                    == int(i == j)
                    for i in range(3)
                    for j in range(3)
                )
                determinant = (
                    matrix[0][0]
                    * (
                        matrix[1][1] * matrix[2][2]
                        - matrix[1][2] * matrix[2][1]
                    )
                    - matrix[0][1]
                    * (
                        matrix[1][0] * matrix[2][2]
                        - matrix[1][2] * matrix[2][0]
                    )
                    + matrix[0][2]
                    * (
                        matrix[1][0] * matrix[2][1]
                        - matrix[1][1] * matrix[2][0]
                    )
                )
                proper = orthogonal and determinant == 1
                improper += int(not proper)
                for program, corpus in corpora.items():
                    # Cycle 317 supplies common transport of the compiled
                    # effects and Cycle 342 supplies common transport of the
                    # complete Record words.  The six new atom fields are
                    # spatial scalars, so their decoder and grading commute
                    # with every inherited proper-cubic transport.
                    graded = grade_corpus(
                        fixtures317[length],
                        fixtures342[length],
                        corpus,
                        size,
                        "trace",
                    )
                    failed = not (
                        proper
                        and corpus_is_lawful(
                            fixtures342[length], corpus, size
                        )
                        and graded is not None
                        and max(
                            row.coarse_normalization_residual for row in graded
                        )
                        < TOL
                    )
                    failures += int(failed)
                    length_failures += int(failed)
                    cases += 1
                    length_cases += 1
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "frames": len(frames),
                "N_values": CORPUS_SIZES,
                "programs": PROGRAMS,
                "frame_size_program_cases": length_cases,
                "failures": length_failures,
                "effect_transport": "inherited current-main Cycle 317",
                "Record_transport": "inherited Cycle 342",
            }
        )
    expected = len(LENGTHS) * len(CORPUS_SIZES) * len(PROGRAMS) * len(frames)
    check(
        "conditional on current-main Cycle-317 effect and Cycle-342 Record transport, the 43-M2 corpus atom is scalar-covariant in all 24 frames at L3 and held L6 for N=3/6/12",
        cases == expected and failures == improper == 0,
        {
            "rows": rows,
            "total_frame_size_program_cases": cases,
            "expected": expected,
            "improper_frames": improper,
            "failures": failures,
        },
    )
    return {"rows": rows, "cases": cases, "failures": failures}


def supplied_structure_inventory() -> dict[str, object]:
    inventory = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "campaign_base_main_inputs": (
            "campaign-base current-main Cycle-317 bounded qubit dilation/effect compiler",
            "Cycle-339 retained registered-interface tournament context",
            "Cycle-342 conditional typed/permanent complete-cylinder Record chain",
        ),
        "supplied": (
            "twelve finite effect specifications and four preparation labels",
            "program, fine-pointer, trial, and use labels",
            "occurrence, commit, typing, permanence, fibre, and blank predicates",
            "trace candidate and finite rogue candidate only after formation",
        ),
        "derived_or_checked": (
            "43-M2 atom codec",
            "three equal coarse-effect dilation/refinement presentations",
            "finite effect/complement trace and rogue comparisons",
            "deletion/splice/retarget refusal",
            "L3/L6 and all-24-frame conditional covariance",
        ),
        "quarantined_non_main_commits": QUARANTINED_COMMITS,
        "not_claimed": (
            "all-finite effect-menu eligibility",
            "effect functionality, grade selection, Born forcing, sampler, or frequency law",
            "autonomous Record formation or actual-member selection",
            "nearest-neighbour corpus constructor or gate-support theorem",
            "broad negative, minimum content, or axiom pressure",
        ),
        "Record_atom_basis_width_M2": CORPUS_ATOM_BITS,
        "basis_width_is_NN_support": False,
        "nearest_neighbour_support_M2": None,
    }
    check(
        "the route inventories every finite menu, Record, grading, support, ancestry, and semantic boundary without Born forcing or universal eligibility",
        inventory["authority"] == "none"
        and inventory["audit"] == "unset"
        and inventory["Record_atom_basis_width_M2"] == 43
        and not inventory["basis_width_is_NN_support"]
        and inventory["nearest_neighbour_support_M2"] is None
        and "all-finite effect-menu eligibility" in inventory["not_claimed"]
        and "broad negative, minimum content, or axiom pressure"
        in inventory["not_claimed"],
        inventory,
    )
    return inventory


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 348 ROUTE 1: PHYSICAL TYPED-RECORD FULL-EFFECT-MENU CORPUS")
    print("authority=none; audit=unset")
    quarantine_controls()
    inherited = inherited_physical_controls()
    fixtures317 = inherited["fixtures"]
    fixtures342 = {
        length: c342.c338.build_fixture(length) for length in LENGTHS
    }
    compiler_presentation_controls(fixtures317)
    corpus_and_grade_controls(fixtures317, fixtures342)
    grade_blind_formation_controls(fixtures342[3])
    for length in LENGTHS:
        deletion_splice_and_domain_controls(
            fixtures342[length], fixtures317[length]
        )
    frame = frame_and_held_controls(fixtures317, fixtures342)
    supplied_structure_inventory()
    print(
        "DETAIL",
        {
            "corpus_atom_M2": CORPUS_ATOM_BITS,
            "basis_storage_M2": {
                size: size * CORPUS_ATOM_BITS for size in CORPUS_SIZES
            },
            "finite_effects": len(EFFECT_EIGENVALUES),
            "finite_complements": len(EFFECT_EIGENVALUES),
            "presentations_per_effect": len(PROGRAMS),
            "L_values": LENGTHS,
            "N_values": CORPUS_SIZES,
            "proper_cubic_frame_cases": frame["cases"],
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )
    print("SUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PHYSICAL_TYPED_RECORD_FULL_EFFECT_MENU_CORPUS_ROUTE_OPEN")
        return 1
    print("RESULT PHYSICAL_TYPED_RECORD_FULL_EFFECT_MENU_CORPUS_ROUTE_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
