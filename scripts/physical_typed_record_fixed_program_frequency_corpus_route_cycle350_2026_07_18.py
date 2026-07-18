#!/usr/bin/env python3
"""Cycle 350 Route 3: fixed-program typed-Record frequency corpus.

This runner joins the existing six-state Cycle-323 fixed program carrier to
the conditional Cycle-342 complete-cylinder Record sector.  Each corpus atom
is one typed 30-M2 Record plus one supplied, explicitly registered 13-M2
preparation/program/pointer/trial/use tag; the whole 43-M2 atom is not promoted
to Record type.  The join is an explicit finite corpus, not a sampler.  The
tag words are supplied basis data, while pointer-event registration,
occurrence, commit, typing, permanence, fibre, close, transition, and blank
capacity remain exposed formation inputs.  Numerical grades are attached
only after the corpus is immutable.

Five Cycle-194-style repeated-history laws are compared on an already formed
quarter-coin corpus.  They share a one-block marginal but none chooses the
actual member.  No sampler, frequency theorem, Born derivation, or broad
negative is claimed.
"""

from __future__ import annotations

from contextlib import redirect_stdout
from dataclasses import dataclass, replace
from fractions import Fraction
from hashlib import sha256
from inspect import signature
from io import StringIO
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import cycle189_record_corpus_frequency_bridge_cycle194_2026_07_16 as c194
import physical_fixed_program_carrier_two_use_cycle323_2026_07_18 as c323
import physical_registered_cylinder_future_equivalence_route_cycle342_2026_07_18 as c342


c321 = c323.c321
c317 = c321.c317
c338 = c342.c338
c311 = c317.c311

TOL = 8.0e-11
LENGTHS = (3, 6)
PROGRAM_SCHEDULE = tuple(range(c323.LAWFUL_PROGRAMS))
PREPARATION_SCHEDULE = (0, 1, 2, 3, 0, 1)
FIRST_USE_POINTERS = (0, 0, 0, 1, 0, 2)
SECOND_USE_POINTERS = (3, 2, 2, 3, 1, 0)
PROGRAM_FINE_LABELS = (8, 4, 3, 4, 3, 3)
PAGE_ATOMS = 6

RECORD_M2 = c342.RECORD_BITS
PREPARATION_M2 = 2
PROGRAM_M2 = c323.PROGRAM_M2
FINE_POINTER_M2 = c323.POINTER_M2
TRIAL_M2 = 4
USE_M2 = 1
ATOM_M2 = (
    RECORD_M2
    + PREPARATION_M2
    + PROGRAM_M2
    + FINE_POINTER_M2
    + TRIAL_M2
    + USE_M2
)

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


def bits(value: int, width: int) -> tuple[int, ...]:
    if not isinstance(value, int) or not 0 <= value < 2**width:
        raise ValueError(("value is outside its M2 register", value, width))
    return tuple((value >> index) & 1 for index in range(width))


@dataclass(frozen=True)
class CorpusAtom:
    record: c342.CylinderRecord
    preparation: int
    program: int
    fine_pointer: int
    trial: int
    use: int


@dataclass(frozen=True)
class AtomBook:
    pages: tuple[tuple[CorpusAtom | None, ...], ...]
    active_page: int


@dataclass(frozen=True)
class CorpusSpec:
    name: str
    length: int
    count: int
    fixed_schedule: bool


@dataclass(frozen=True)
class LawAttachment:
    name: str
    corpus_hash: str
    one_block_marginal: tuple[tuple[int, Fraction], ...]
    actual_member_selector: None = None


def atom_word(atom: CorpusAtom) -> tuple[int, ...]:
    if not atom.record.typed or not atom.record.permanent:
        raise ValueError("a corpus atom requires one typed permanent Record")
    if not 0 <= atom.preparation < 4:
        raise ValueError("preparation does not fit its two M2")
    if not 0 <= atom.program < c323.LAWFUL_PROGRAMS:
        raise ValueError("program is outside the six-state code")
    if not 0 <= atom.fine_pointer < c323.POINTER_DIMENSION:
        raise ValueError("fine pointer does not fit its three M2")
    if atom.fine_pointer >= PROGRAM_FINE_LABELS[atom.program]:
        raise ValueError("fine pointer is outside its tagged apparatus program")
    if not 0 <= atom.trial < 16:
        raise ValueError("trial does not fit its four M2")
    if atom.use not in (0, 1):
        raise ValueError("use tag must be one M2 basis value")
    word = (
        c342.record_word(atom.record)
        + bits(atom.preparation, PREPARATION_M2)
        + bits(atom.program, PROGRAM_M2)
        + bits(atom.fine_pointer, FINE_POINTER_M2)
        + bits(atom.trial, TRIAL_M2)
        + (atom.use,)
    )
    if len(word) != ATOM_M2 or any(bit not in (0, 1) for bit in word):
        raise RuntimeError("the declared corpus-atom register drifted")
    return word


def corpus_hash(atoms: tuple[CorpusAtom, ...]) -> str:
    payload = bytes(bit for atom in atoms for bit in atom_word(atom))
    return sha256(payload).hexdigest()


def form_atom(
    fixture: c338.RouteFixture,
    cylinder: c338.FutureCylinder,
    *,
    preparation: int,
    program: int,
    fine_pointer: int,
    trial: int,
    use: int,
    occurrence: bool = True,
    commit: bool = True,
    typing: bool = True,
    permanence: bool = True,
    fibre: bool = True,
    close: bool = True,
    transition: bool = True,
    blank: bool = True,
    pointer_event_registered: bool = True,
) -> CorpusAtom | None:
    """Conditionally form one atom; deliberately accepts no grade argument."""
    if not pointer_event_registered:
        return None
    if not 0 <= program < c323.LAWFUL_PROGRAMS:
        raise ValueError("program is outside the six-state tag code")
    if not 0 <= fine_pointer < PROGRAM_FINE_LABELS[program]:
        raise ValueError("fine pointer is outside its tagged apparatus program")
    if not blank or not close or fixture.export.close_certificate != 1:
        return None
    if not transition or not c342.cylinder_is_lawful(fixture, cylinder):
        return None
    record = c342.form_conditional_record(
        fixture,
        cylinder,
        occurrence=occurrence,
        commit=commit,
        typing=typing,
        permanence=permanence,
        fibre_certified=fibre,
    )
    if not record.typed or not record.permanent:
        return None
    atom = CorpusAtom(
        record,
        preparation,
        program,
        fine_pointer,
        trial,
        use,
    )
    atom_word(atom)
    return atom


def schedule_fields(trial: int) -> tuple[int, int, int, int]:
    slot = trial % len(PROGRAM_SCHEDULE)
    use = trial // len(PROGRAM_SCHEDULE)
    if use not in (0, 1):
        raise ValueError("the declared fixed corpus has at most two uses")
    pointers = FIRST_USE_POINTERS if use == 0 else SECOND_USE_POINTERS
    return (
        PREPARATION_SCHEDULE[slot],
        PROGRAM_SCHEDULE[slot],
        pointers[slot],
        use,
    )


def form_fixed_corpus(
    fixture: c338.RouteFixture,
    count: int,
) -> tuple[CorpusAtom, ...]:
    if count not in (3, 6, 12):
        raise ValueError("fixed corpus count must be smoke, full-cover, or held")
    cylinders = c342.make_cylinder_chain(fixture, 0, count)
    atoms = []
    for trial, cylinder in enumerate(cylinders):
        preparation, program, pointer, use = schedule_fields(trial)
        atom = form_atom(
            fixture,
            cylinder,
            preparation=preparation,
            program=program,
            fine_pointer=pointer,
            trial=trial,
            use=use,
        )
        if atom is None:
            raise RuntimeError("a lawful fixed-program corpus atom did not form")
        atoms.append(atom)
    return tuple(atoms)


def form_quarter_coin_corpus(
    fixture: c338.RouteFixture,
    count: int = 12,
) -> tuple[CorpusAtom, ...]:
    if count != 12:
        raise ValueError("the held quarter-coin control is exactly N=12")
    word = (0, 1, 2, 2) * 3
    cylinders = c342.make_cylinder_chain(fixture, 1, count)
    atoms = []
    for trial, (cylinder, pointer) in enumerate(zip(cylinders, word)):
        atom = form_atom(
            fixture,
            cylinder,
            preparation=trial % 4,
            program=5,
            fine_pointer=pointer,
            trial=trial,
            use=trial // PAGE_ATOMS,
        )
        if atom is None:
            raise RuntimeError("a lawful quarter-coin corpus atom did not form")
        atoms.append(atom)
    return tuple(atoms)


def validate_fixed_corpus(
    fixture: c338.RouteFixture,
    atoms: tuple[CorpusAtom, ...],
) -> bool:
    if not atoms or len(atoms) not in (3, 6, 12):
        return False
    if not c342.valid_chain(fixture, tuple(atom.record for atom in atoms)):
        return False
    for trial, atom in enumerate(atoms):
        preparation, program, pointer, use = schedule_fields(trial)
        if (
            atom.trial,
            atom.preparation,
            atom.program,
            atom.fine_pointer,
            atom.use,
        ) != (trial, preparation, program, pointer, use):
            return False
    return True


def empty_atom_book() -> AtomBook:
    return AtomBook(((None,) * PAGE_ATOMS,), 0)


def append_atom(book: AtomBook, atom: CorpusAtom) -> AtomBook:
    atom_word(atom)
    page = list(book.pages[book.active_page])
    try:
        slot = page.index(None)
    except ValueError as error:
        raise ValueError("finite atom page is exhausted") from error
    page[slot] = atom
    pages = list(book.pages)
    pages[book.active_page] = tuple(page)
    return AtomBook(tuple(pages), book.active_page)


def renew_atom_book(book: AtomBook, blank_page: tuple[None, ...]) -> AtomBook:
    if len(blank_page) != PAGE_ATOMS or any(item is not None for item in blank_page):
        raise ValueError("renewal requires one separately supplied blank atom page")
    if any(item is None for item in book.pages[book.active_page]):
        raise ValueError("renewal is allowed only after exhaustion")
    return AtomBook(book.pages + (blank_page,), len(book.pages))


def flatten_book(book: AtomBook) -> tuple[CorpusAtom, ...]:
    return tuple(item for page in book.pages for item in page if item is not None)


def fixed_corpus_and_capacity_controls(
    record_fixtures: dict[int, c338.RouteFixture],
) -> dict[str, object]:
    specs = (
        CorpusSpec("N3 smoke", 3, 3, True),
        CorpusSpec("N6 full six-program cover", 3, 6, True),
        CorpusSpec("N12 held two-use two-page", 6, 12, True),
    )
    corpora = {
        spec.name: form_fixed_corpus(record_fixtures[spec.length], spec.count)
        for spec in specs
    }
    rows = []
    for spec in specs:
        atoms = corpora[spec.name]
        book = empty_atom_book()
        first = atoms[: min(PAGE_ATOMS, len(atoms))]
        for atom in first:
            book = append_atom(book, atom)
        exhaustion_rejected = False
        if len(first) == PAGE_ATOMS:
            try:
                append_atom(book, atoms[0])
            except ValueError:
                exhaustion_rejected = True
        old_page = book.pages[0]
        if len(atoms) > PAGE_ATOMS:
            book = renew_atom_book(book, (None,) * PAGE_ATOMS)
            for atom in atoms[PAGE_ATOMS:]:
                book = append_atom(book, atom)
        rows.append(
            {
                "name": spec.name,
                "L": spec.length,
                "N": spec.count,
                "pages": len(book.pages),
                "atoms": len(flatten_book(book)),
                "atom_M2": ATOM_M2,
                "corpus_M2": ATOM_M2 * len(atoms),
                "valid": validate_fixed_corpus(record_fixtures[spec.length], atoms),
                "programs": tuple(atom.program for atom in atoms),
                "uses": tuple(atom.use for atom in atoms),
                "hash": corpus_hash(atoms),
                "exhaustion_rejected": exhaustion_rejected,
                "old_page_preserved": book.pages[0] == old_page,
            }
        )
    held = corpora[specs[-1].name]
    check(
        "the exact 43-M2 atom forms N3 smoke, N6 six-program, and N12 held two-use corpora with explicit finite renewal",
        RECORD_M2 == 30
        and ATOM_M2 == 43
        and rows[0]["programs"] == (0, 1, 2)
        and rows[1]["programs"] == PROGRAM_SCHEDULE
        and rows[2]["programs"] == PROGRAM_SCHEDULE * 2
        and rows[0]["uses"] == (0,) * 3
        and rows[1]["uses"] == (0,) * 6
        and rows[2]["uses"] == (0,) * 6 + (1,) * 6
        and all(row["valid"] and row["atoms"] == row["N"] for row in rows)
        and rows[0]["pages"] == rows[1]["pages"] == 1
        and rows[2]["pages"] == 2
        and rows[1]["exhaustion_rejected"]
        and rows[2]["exhaustion_rejected"]
        and rows[2]["old_page_preserved"]
        and len({row["hash"] for row in rows}) == 3
        and len(held) == 12,
        rows,
    )
    return {"specs": specs, "corpora": corpora, "rows": rows}


def finite_nontrace_grade(programs: tuple[c321.Program, ...]):
    unique, menus = c321.unique_effects_and_menus(programs)
    matrix = np.zeros((len(menus), len(unique)))
    for row, menu in enumerate(menus):
        for index in menu:
            matrix[row, index] += 1
    trace_grade = np.asarray([np.trace(effect).real / 2 for effect in unique])
    singular = np.linalg.svd(matrix, full_matrices=True)
    rank = int(np.sum(singular[1] > 1e-10))
    null_basis = singular[2][rank:].T
    bloch = np.asarray(
        [
            [0.5 * np.trace(pauli @ effect).real for pauli in (c321.X, c321.Y, c321.Z)]
            for effect in unique
        ]
    )
    q, _ = np.linalg.qr(bloch)
    candidates = tuple(vector - q @ (q.T @ vector) for vector in null_basis.T)
    chosen = max(candidates, key=np.linalg.norm)
    chosen /= np.linalg.norm(chosen)
    margin = min(
        np.min(trace_grade[trace_grade > 1e-10]),
        np.min(1 - trace_grade[trace_grade < 1 - 1e-10]),
    )
    epsilon = 0.3 * margin / np.max(np.abs(chosen))
    values = trace_grade + epsilon * chosen

    def evaluate(effect: np.ndarray, _preparation: int) -> float | None:
        matches = tuple(
            index for index, existing in enumerate(unique)
            if np.linalg.norm(effect - existing) < 1e-10
        )
        return None if len(matches) != 1 else float(values[matches[0]])

    return evaluate, {
        "normalization_residual": float(np.linalg.norm(matrix @ values - np.ones(len(menus)))),
        "minimum": float(np.min(values)),
        "maximum": float(np.max(values)),
        "unique_effects": len(unique),
        "normalization_rank": rank,
    }


def born_trace_grade(effect: np.ndarray, preparation: int) -> float:
    rho = c321.held_states()[preparation]
    return float(np.trace(rho @ effect).real)


def nonlinear_grade(effect: np.ndarray, _preparation: int) -> float:
    return c317.nonlinear_binary_weight(effect)


def paired_rogue_grade(effect: np.ndarray, _preparation: int) -> float | None:
    """Qubit paired rogue on scalar identities or scaled rank-one effects."""
    hermitian = (effect + effect.conj().T) / 2
    values = np.linalg.eigvalsh(hermitian)
    if np.linalg.norm(hermitian - np.trace(hermitian).real * c321.I2 / 2) < TOL:
        return float(np.trace(hermitian).real / 2)
    scale = float(values[-1])
    if values[0] < -TOL or scale <= TOL or abs(values[0]) > TOL:
        return None
    projector = hermitian / scale
    z_coordinate = float(np.trace(projector @ c321.Z).real)
    return scale * (1 + z_coordinate**3) / 2


def atom_effect(atom: CorpusAtom, programs: tuple[c321.Program, ...]) -> np.ndarray:
    program = programs[atom.program]
    if not 0 <= atom.fine_pointer < len(program.kraus):
        raise ValueError("supplied fine pointer is outside its program block")
    operator = program.kraus[atom.fine_pointer]
    return operator.conj().T @ operator


def prediction_diagnostic(
    atoms: tuple[CorpusAtom, ...],
    programs: tuple[c321.Program, ...],
    grade,
) -> tuple[float | None, ...] | None:
    if grade is None:
        return None
    values = tuple(grade(atom_effect(atom, programs), atom.preparation) for atom in atoms)
    return values


def two_use_prediction_diagnostic(
    atoms: tuple[CorpusAtom, ...],
    programs: tuple[c321.Program, ...],
    grade,
) -> tuple[float | None, ...] | None:
    if grade is None:
        return None
    if len(atoms) != 12:
        raise ValueError("two-use diagnostic requires the held two-page corpus")
    values = []
    for program_label in PROGRAM_SCHEDULE:
        first = next(atom for atom in atoms if atom.program == program_label and atom.use == 0)
        second = next(atom for atom in atoms if atom.program == program_label and atom.use == 1)
        left = programs[program_label].kraus[first.fine_pointer]
        right = programs[program_label].kraus[second.fine_pointer]
        sequence_effect = (right @ left).conj().T @ (right @ left)
        values.append(grade(sequence_effect, first.preparation))
    return tuple(values)


def grade_blindness_controls(
    corpora: dict[str, tuple[CorpusAtom, ...]],
    programs: tuple[c321.Program, ...],
    record_fixtures: dict[int, c338.RouteFixture],
) -> dict[str, object]:
    finite_grade, finite_detail = finite_nontrace_grade(programs)
    grades = {
        "Born trace": born_trace_grade,
        "Cycle321 finite normalized nontrace": finite_grade,
        "Cycle317 nonlinear": nonlinear_grade,
        "paired rogue where defined": paired_rogue_grade,
        "grade deleted": None,
    }
    base_hashes = tuple((name, corpus_hash(atoms)) for name, atoms in corpora.items())
    full_hash = sha256("".join(value for _, value in base_hashes).encode()).hexdigest()
    formation_hashes = {}
    for grade_name in grades:
        # The grade label intentionally does not enter either constructor.
        fresh = (
            form_fixed_corpus(record_fixtures[3], 3),
            form_fixed_corpus(record_fixtures[3], 6),
            form_fixed_corpus(record_fixtures[6], 12),
        )
        hashes = tuple(corpus_hash(atoms) for atoms in fresh)
        formation_hashes[grade_name] = sha256("".join(hashes).encode()).hexdigest()
    held = corpora["N12 held two-use two-page"]
    diagnostics = {
        name: {
            "one_use": prediction_diagnostic(held, programs, grade),
            "two_use": two_use_prediction_diagnostic(held, programs, grade),
        }
        for name, grade in grades.items()
    }
    defined_diagnostic_hashes = {
        name: sha256(repr(row).encode()).hexdigest()
        for name, row in diagnostics.items()
        if name != "grade deleted"
    }
    rogue_one = diagnostics["paired rogue where defined"]["one_use"]
    rogue_two = diagnostics["paired rogue where defined"]["two_use"]
    assert rogue_one is not None and rogue_two is not None
    z_projector = c321.projector((0, 0, 1))
    x_projector = c321.projector((1, 0, 0))
    outside_rogue_domain = 0.2 * z_projector + 0.3 * x_projector
    rogue_pair_residual = abs(
        paired_rogue_grade(z_projector, 0)
        + paired_rogue_grade(c321.I2 - z_projector, 0)
        - 1
    )
    check(
        "Record formation is grade blind across Born, finite nontrace, nonlinear, paired-rogue, and grade-deleted diagnostics",
        "grade" not in signature(form_atom).parameters
        and len(set(formation_hashes.values())) == 1
        and len(set(defined_diagnostic_hashes.values())) == 4
        and diagnostics["grade deleted"] == {"one_use": None, "two_use": None}
        and finite_detail["normalization_residual"] < TOL
        and finite_detail["unique_effects"] == 20
        and finite_detail["normalization_rank"] == 7
        and sum(value is not None for value in rogue_one) > 0
        and sum(value is not None for value in rogue_two) > 0
        and paired_rogue_grade(outside_rogue_domain, 0) is None
        and rogue_pair_residual < TOL,
        {
            "full_corpus_hash": full_hash,
            "formation_hashes": formation_hashes,
            "post_formation_diagnostic_hashes": defined_diagnostic_hashes,
            "finite_grade": finite_detail,
            "paired_rogue_defined_one_use": sum(value is not None for value in rogue_one),
            "paired_rogue_undefined_one_use": sum(value is None for value in rogue_one),
            "paired_rogue_defined_two_use": sum(value is not None for value in rogue_two),
            "paired_rogue_undefined_two_use": sum(value is None for value in rogue_two),
            "paired_rogue_outside_domain_is_undefined": paired_rogue_grade(outside_rogue_domain, 0) is None,
            "paired_complement_residual": rogue_pair_residual,
            "constructor_parameters": tuple(signature(form_atom).parameters),
        },
    )
    return {
        "full_hash": full_hash,
        "grades": grades,
        "diagnostics": diagnostics,
        "finite": finite_detail,
    }


def instrument_and_contact_controls(
    held: tuple[CorpusAtom, ...],
    fixture: c317.PhysicalFixture,
    record_fixture: c338.RouteFixture,
) -> dict[str, object]:
    programs = c323.make_programs(fixture.contact)
    carrier = c323.FixedProgramCarrier(programs)
    with redirect_stdout(StringIO()):
        ray, axis = c323.two_use_equivalence_controls(programs)
        deletion = c323.contact_deletion_and_domain_controls(fixture, carrier)
    deleted_programs = c323.make_programs(c321.I2)
    before_hash = corpus_hash(held)
    freshly_formed_after_deletion = form_fixed_corpus(record_fixture, 12)
    after_hash = corpus_hash(freshly_formed_after_deletion)
    effect_residuals = tuple(
        float(np.linalg.norm(atom_effect(atom, programs) - atom_effect(atom, deleted_programs)))
        for atom in held
    )
    predictions = prediction_diagnostic(held, programs, born_trace_grade)
    deleted_predictions = prediction_diagnostic(held, deleted_programs, born_trace_grade)
    assert predictions is not None and deleted_predictions is not None
    prediction_residual = max(abs(left - right) for left, right in zip(predictions, deleted_predictions))
    p2 = held[2]
    p3 = held[3]
    check(
        "Cycle-321 ray refinement and axis process distinctions survive the registered supplied fine tag while contact deletion cannot rewrite actual words",
        ray["two_use_coarse_instrument_Choi_residual"] < TOL
        and ray["two_use_pointer_erased_Choi_residual"] < TOL
        and ray["two_use_fine_transcript_Choi_residual"] > 0.9
        and axis["two_use_coarse_effect_residual"] < TOL
        and axis["two_use_coarse_instrument_Choi_residual"] > 0.2
        and p2.program == 2
        and p3.program == 3
        and p2.fine_pointer != p3.fine_pointer
        and 0 in programs[2].coarse_groups[0]
        and 1 in programs[3].coarse_groups[0]
        and before_hash == after_hash
        and freshly_formed_after_deletion is not held
        and all(left is not right for left, right in zip(held, freshly_formed_after_deletion))
        and max(effect_residuals) > 0.15
        and prediction_residual > 0.02
        and deletion["one_use_fixed_update_contact_deletion_residual"] > 0.9,
        {
            "ray_two_use_coarse_CP_residual": ray["two_use_coarse_instrument_Choi_residual"],
            "ray_two_use_fine_transcript_residual": ray["two_use_fine_transcript_Choi_residual"],
            "axis_effect_residual": axis["two_use_coarse_effect_residual"],
            "axis_process_Choi_residual": axis["two_use_coarse_instrument_Choi_residual"],
            "p2_p3_fine_tags": (p2.fine_pointer, p3.fine_pointer),
            "maximum_contact_deleted_effect_residual": max(effect_residuals),
            "maximum_contact_deleted_prediction_residual": prediction_residual,
            "fresh_post_deletion_snapshot": True,
            "supplied_actual_word_hash_unchanged": before_hash == after_hash,
        },
    )
    return {"programs": programs, "carrier": carrier, "ray": ray, "axis": axis}


def formation_deletion_and_attack_controls(
    fixture: c338.RouteFixture,
    corpus: tuple[CorpusAtom, ...],
) -> dict[str, object]:
    cylinder = c342.make_cylinder_chain(fixture, 0, 1)[0]
    fields = dict(
        preparation=0,
        program=0,
        fine_pointer=0,
        trial=0,
        use=0,
    )
    deletions = {
        name: form_atom(fixture, cylinder, **fields, **{name: False})
        for name in (
            "occurrence",
            "commit",
            "typing",
            "permanence",
            "fibre",
            "close",
            "transition",
            "blank",
            "pointer_event_registered",
        )
    }
    grade_deleted = form_atom(fixture, cylinder, **fields)
    deleted = corpus[:1] + corpus[2:]
    spliced = list(corpus)
    spliced[1], spliced[2] = spliced[2], spliced[1]
    retargeted = list(corpus)
    retargeted[1] = replace(
        retargeted[1],
        record=replace(
            retargeted[1].record,
            cylinder=replace(retargeted[1].record.cylinder, endpoint=1),
        ),
    )
    rejected_domain = 0
    for call in (
        lambda: atom_word(replace(corpus[0], preparation=4)),
        lambda: atom_word(replace(corpus[0], program=6)),
        lambda: atom_word(replace(corpus[0], fine_pointer=8)),
        lambda: atom_word(replace(corpus[0], trial=16)),
        lambda: atom_word(replace(corpus[0], use=2)),
        lambda: renew_atom_book(empty_atom_book(), (None,) * PAGE_ATOMS),
        lambda: renew_atom_book(AtomBook((tuple(corpus[:PAGE_ATOMS]),), 0), (None,) * 5),
    ):
        try:
            call()
        except ValueError:
            rejected_domain += 1
    detail = {
        "semantic_deletions": tuple(deletions),
        "typed_survivors": sum(value is not None for value in deletions.values()),
        "grade_deleted_Record_survives": grade_deleted is not None,
        "Record_deletion_valid": validate_fixed_corpus(fixture, deleted),
        "Record_splice_valid": validate_fixed_corpus(fixture, tuple(spliced)),
        "Record_retarget_valid": validate_fixed_corpus(fixture, tuple(retargeted)),
        "domain_rejections": rejected_domain,
    }
    check(
        "formation inputs, permanent-chain attacks, exhaustion, and renewal remain explicit and deletion sensitive",
        all(value is None for value in deletions.values())
        and grade_deleted is not None
        and grade_deleted.record.typed
        and grade_deleted.record.permanent
        and not detail["Record_deletion_valid"]
        and not detail["Record_splice_valid"]
        and not detail["Record_retarget_valid"]
        and rejected_domain == 7,
        detail,
    )
    return detail


def law_marginals(law: c194.Law, horizon: int) -> tuple[dict[int, Fraction], ...]:
    return tuple(c194.marginal(law, index) for index in range(horizon))


def repeated_law_controls(
    quarter_corpus: tuple[CorpusAtom, ...],
) -> dict[str, object]:
    distribution = {0: Fraction(1, 4), 1: Fraction(1, 4), 2: Fraction(1, 2)}
    horizon = 4
    laws = {
        "IID": c194.product_law(distribution, horizon),
        "sticky": c194.sticky_markov_law(distribution, horizon),
        "frozen": c194.frozen_law(distribution, horizon),
        "balanced": c194.balanced_law(distribution, horizon),
    }
    laws["equal-mean mixture"] = c194.mixture_law(laws["IID"], laws["balanced"])
    marginal_failures = tuple(
        (name, index, marginal)
        for name, law in laws.items()
        for index, marginal in enumerate(law_marginals(law, horizon))
        if marginal != distribution
    )
    balanced_period = c194.balanced_period(distribution)
    balanced_words = tuple(
        tuple(balanced_period[(phase + offset) % len(balanced_period)] for offset in range(12))
        for phase in range(len(balanced_period))
    )
    target = distribution
    balanced_exact = all(c194.empirical_distribution(word) == target for word in balanced_words)
    frozen_wrong = all(
        c194.empirical_distribution(word) != target
        for word in c194.frozen_law(distribution, 12)
    )
    attachments = tuple(
        LawAttachment(name, corpus_hash(quarter_corpus), tuple(sorted(distribution.items())))
        for name in laws
    )
    actual_word = tuple(atom.fine_pointer for atom in quarter_corpus)
    check(
        "five repeated-history laws attach after the quarter-coin Record-tag corpus with one marginal but no actual-member selector",
        not marginal_failures
        and all(c194.law_total(law) == 1 for law in laws.values())
        and c194.projectively_stationary(c194.product_law, distribution, 3)
        and c194.projectively_stationary(c194.sticky_markov_law, distribution, 3)
        and c194.projectively_stationary(c194.frozen_law, distribution, 3)
        and c194.projectively_stationary(c194.balanced_law, distribution, 3)
        and balanced_exact
        and frozen_wrong
        and c194.empirical_distribution(actual_word) == target
        and len({attachment.corpus_hash for attachment in attachments}) == 1
        and all(attachment.actual_member_selector is None for attachment in attachments),
        {
            "law_names": tuple(laws),
            "one_block_marginal": distribution,
            "horizon_checked": horizon,
            "balanced_N12_components": len(balanced_words),
            "balanced_N12_exact": balanced_exact,
            "frozen_components_with_wrong_frequency": len(c194.frozen_law(distribution, 12)),
            "actual_N12_frequency": c194.empirical_distribution(actual_word),
            "actual_member_selectors": tuple(attachment.actual_member_selector for attachment in attachments),
        },
    )
    return {"attachments": attachments, "laws": laws, "balanced_words": balanced_words}


def mapped_expected(
    source: c338.FutureCylinder,
    mapping: np.ndarray,
) -> c338.FutureCylinder:
    return c338.FutureCylinder(
        endpoint=source.endpoint,
        candidate=source.candidate,
        phase=source.phase,
        future_pre=int(mapping[source.future_pre]),
        future_post=int(mapping[source.future_post]),
    )


def frame_leakage_and_mass_controls(
    record_fixtures: dict[int, c338.RouteFixture],
    matter_fixtures: dict[int, c317.PhysicalFixture],
    carrier: c323.FixedProgramCarrier,
) -> dict[str, object]:
    frame_cases = mapping_failures = covariance_failures = 0
    specs = ((3, 3, False), (3, 6, False), (6, 12, False), (6, 12, True))
    for length, count, quarter in specs:
        fixture = record_fixtures[length]
        source = (
            form_quarter_coin_corpus(fixture, count)
            if quarter
            else form_fixed_corpus(fixture, count)
        )
        for frame in c311.c235.proper_cubic_frames():
            rotated, mapping, failures = c342.mapped_fixture(fixture, frame)
            mapping_failures += failures
            carried = (
                form_quarter_coin_corpus(rotated, count)
                if quarter
                else form_fixed_corpus(rotated, count)
            )
            for left, right in zip(source, carried):
                covariance_failures += int(
                    right.record.cylinder != mapped_expected(left.record.cylinder, mapping)
                    or right.preparation != left.preparation
                    or right.program != left.program
                    or right.fine_pointer != left.fine_pointer
                    or right.trial != left.trial
                    or right.use != left.use
                    or len(atom_word(right)) != ATOM_M2
                )
                frame_cases += 1
    with redirect_stdout(StringIO()):
        support_rows = c323.physical_embedding_and_support_controls(matter_fixtures, carrier)
        carrier_frame = c323.covariance_controls(matter_fixtures, carrier)
    species = c311.c219.common_species(-0.3)
    mass_residual = abs(c311.c219.rest_mass(species) / species.analytic_mass - 1)
    detail = {
        "corpus_frame_atom_cases": frame_cases,
        "proper_cubic_frames": 24,
        "record_mapping_failures": mapping_failures,
        "corpus_covariance_failures": covariance_failures,
        "support_rows": support_rows,
        "carrier_frame": carrier_frame,
        "one_particle_mass_relative_residual": mass_residual,
        "held_corpus_M2": 12 * ATOM_M2,
    }
    check(
        "the 43-M2 corpus words inherit zero-leakage fixed-carrier support, mass, and all-frame Record covariance through L=6",
        frame_cases == sum(count for _length, count, _quarter in specs) * 24
        and mapping_failures == covariance_failures == 0
        and all(
            row["one_and_two_use_leakage"] < TOL
            and row["role_constraint_residual"] < TOL
            and row["maximum_two_use_controlled_M2"] <= 29
            and row["port_constraint_failures"] == 0
            and row["local_check_or_Wilson_failures"] == 0
            for row in support_rows
        )
        and carrier_frame["frames"] == 24
        and carrier_frame["branch_failures"] == 0
        and carrier_frame["maximum_one_use_carrier_residual"] < TOL
        and carrier_frame["maximum_two_use_carrier_residual"] < TOL
        and mass_residual < 3e-12
        and detail["held_corpus_M2"] == 516,
        detail,
    )
    return detail


def semantic_firewall_controls() -> dict[str, object]:
    detail = {
        "formation_law": "conditional Cycle342 typed Record DAG",
        "Record_M2": RECORD_M2,
        "registered_supplied_tag_M2": ATOM_M2 - RECORD_M2,
        "whole_43_M2_atom_is_Record": False,
        "pointer_event_registration": "supplied explicit formation predicate; not derived by this route",
        "actual_words": "supplied preparation/program/fine-pointer/trial/use basis data",
        "fixed_program_schedule": PROGRAM_SCHEDULE,
        "grade_input_to_formation": None,
        "numerical_grade_selector": None,
        "actual_history_sampler": None,
        "frequency_theorem": None,
        "Born_derivation": None,
        "repeated_law_actual_member_selector": None,
        "pointer_copy_is_Record": False,
        "frequency_is_probability": False,
        "authority": "none",
        "audit": "unset",
        "negative_claim": None,
        "supplied_structure": (
            "six fixed carrier program states and coefficients",
            "fresh fine-pointer words",
            "preparation labels",
            "actual pointer member per trial",
            "pointer-event registration binding the supplied tag to the typed Record",
            "occurrence, commit, type, permanence, fibre, close, transition inputs",
            "blank Record pages and renewal",
            "optional post-formation numerical grade",
            "optional repeated-history law",
        ),
    }
    check(
        "the corpus route exposes actuality and law imports without promoting predictions into Records or frequencies into probability",
        detail["Record_M2"] == 30
        and detail["registered_supplied_tag_M2"] == 13
        and detail["whole_43_M2_atom_is_Record"] is False
        and "supplied explicit" in detail["pointer_event_registration"]
        and detail["grade_input_to_formation"] is None
        and detail["numerical_grade_selector"] is None
        and detail["actual_history_sampler"] is None
        and detail["frequency_theorem"] is None
        and detail["Born_derivation"] is None
        and detail["repeated_law_actual_member_selector"] is None
        and detail["pointer_copy_is_Record"] is False
        and detail["frequency_is_probability"] is False
        and detail["authority"] == "none"
        and detail["audit"] == "unset"
        and detail["negative_claim"] is None,
        detail,
    )
    return detail


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 350 ROUTE 3: PHYSICAL TYPED-RECORD FIXED-PROGRAM FREQUENCY CORPUS")
    print("authority=none; audit=unset")

    record_fixtures = {length: c338.build_fixture(length) for length in LENGTHS}
    with redirect_stdout(StringIO()):
        matter_fixtures = c323.physical_fixture_controls()
    programs = c323.make_programs(matter_fixtures[3].contact)
    carrier = c323.FixedProgramCarrier(programs)

    corpus_result = fixed_corpus_and_capacity_controls(record_fixtures)
    held = corpus_result["corpora"]["N12 held two-use two-page"]
    instrument_result = instrument_and_contact_controls(
        held, matter_fixtures[3], record_fixtures[6]
    )
    grade_result = grade_blindness_controls(
        corpus_result["corpora"], programs, record_fixtures
    )
    formation_result = formation_deletion_and_attack_controls(
        record_fixtures[3], corpus_result["corpora"]["N6 full six-program cover"]
    )
    quarter_corpus = form_quarter_coin_corpus(record_fixtures[6])
    law_result = repeated_law_controls(quarter_corpus)
    physical_result = frame_leakage_and_mass_controls(
        record_fixtures, matter_fixtures, carrier
    )
    semantics = semantic_firewall_controls()

    check(
        "Route 3 constructs a grade-blind corpus of typed Records plus registered supplied tags and attaches nonselecting repeated-history laws",
        len(corpus_result["rows"]) == 3
        and instrument_result["ray"]["two_use_coarse_instrument_Choi_residual"] < TOL
        and grade_result["finite"]["normalization_residual"] < TOL
        and formation_result["typed_survivors"] == 0
        and len(law_result["attachments"]) == 5
        and physical_result["corpus_covariance_failures"] == 0
        and semantics["authority"] == "none",
        {
            "strongest_positive": "conditional grade-blind 43-M2 atoms: typed 30-M2 Records plus registered supplied 13-M2 fixed-program tags",
            "corpus_hash": grade_result["full_hash"],
            "corpus_sizes": (3, 6, 12),
            "law_families": tuple(item.name for item in law_result["attachments"]),
            "not_derived": "pointer occurrence, actual-history sampling, a frequency theorem, or Born probability",
        },
    )

    print("SUMMARY", {"pass": PASS, "fail": FAIL})
    print(
        "RESULT",
        "PHYSICAL_TYPED_RECORD_FIXED_PROGRAM_FREQUENCY_CORPUS_ROUTE_CERTIFIED"
        if FAIL == 0
        else "PHYSICAL_TYPED_RECORD_FIXED_PROGRAM_FREQUENCY_CORPUS_ROUTE_OPEN",
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
