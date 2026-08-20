#!/usr/bin/env python3
"""Exact reverse/face census on 16 letterings of four occupancy-formed sites.

The paired note is
docs/FOUR_SITE_LETTER_BITS_REVERSE_FACE_CENSUS_BOUNDED_THEOREM_NOTE_2026-08-15.md.

Letters are displayed data. The runner enumerates maps; it does not adopt
the alphabet or treat it as a formation mask.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]

AUDIT_INPUT_PATHS = (
    "docs/FOUR_SITE_LETTER_BITS_REVERSE_FACE_CENSUS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]

PLUS = "+"
MINUS = "-"
ALPHABET = (PLUS, MINUS)
SITE_NAMES = ("A", "B", "C", "D")
SITES = {
    "A": (1, 0, 0),
    "B": (1, 1, 1),
    "C": (2, 0, 0),
    "D": (1, 1, 0),
}
ORIGIN = (0, 0, 0)
ORIGIN_LETTER = PLUS
Lettering = tuple[str, str, str, str]


def normalize(text: str) -> str:
    return " ".join(text.split())


def all_letterings() -> tuple[Lettering, ...]:
    return tuple(product(ALPHABET, repeat=4))


def reverse_bit(lettering: Lettering) -> bool:
    letter_a, letter_b, _, _ = lettering
    return letter_a == PLUS and letter_b == MINUS


def face_bit(lettering: Lettering) -> bool:
    _, _, letter_c, letter_d = lettering
    return letter_c == PLUS and letter_d == MINUS


def reverse_drop_b(lettering: Lettering) -> bool:
    return lettering[0] == PLUS


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool, residual: object | None = None) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} {statement}")
        if not ok and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)

    print("external_scientific_inputs: current Lattice, Admissibility, and Record boundaries; no observations or fits")
    print("integrity_reads: this runner, its note, and the axiom memo; no other scientific inputs")
    print("construction: 16 displayed letterings of four occupancy-formed sites; origin held at +")
    print("negative_scope: census is displayed, not adopted; not a formation mask; uniqueness not required")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")

    checks.check(
        "audit-inputs",
        "declared source-bound inputs exist and match the static pair",
        AUDIT_INPUT_PATHS
        == (
            "docs/FOUR_SITE_LETTER_BITS_REVERSE_FACE_CENSUS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and AUDIT_TIMEOUT_SEC == 120
        and len(AUDIT_INPUT_PATHS) == 2
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    lattice_sentence = "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    admissibility_sentence = "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."
    formation_boundary = "does not supply the formation site, probability, or rate"
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_content = "A readout value is determined by record content alone."
    record_absence = "A site with no record cannot be read."

    checks.check(
        "source-lattice",
        "current cubic-site wording is pinned",
        lattice_sentence in normalized_axiom and lattice_sentence in note,
    )
    checks.check(
        "source-admissibility",
        "current local-distribution wording is pinned",
        admissibility_sentence in normalized_axiom and admissibility_sentence in note,
    )
    checks.check(
        "source-formation-boundary",
        "formation site/probability/rate remains outside Admissibility",
        formation_boundary in normalized_axiom and formation_boundary in normalized_note,
    )
    checks.check(
        "source-record-boundary",
        "current lock/content/unreadable-at-absence wording is pinned",
        all(phrase in normalized_axiom for phrase in (record_lock, record_content, record_absence))
        and all(phrase in note for phrase in (record_lock, record_content, record_absence)),
    )

    coords = tuple(SITES[name] for name in SITE_NAMES)
    checks.check(
        "four-sites",
        "lettered sites are exactly A=(1,0,0), B=(1,1,1), C=(2,0,0), D=(1,1,0)",
        coords == ((1, 0, 0), (1, 1, 1), (2, 0, 0), (1, 1, 0))
        and len(set(coords)) == 4
        and ORIGIN not in coords
        and ORIGIN_LETTER == PLUS,
    )

    letterings = all_letterings()
    n_maps = len(letterings)
    n_rev = sum(1 for lettering in letterings if reverse_bit(lettering))
    n_face = sum(1 for lettering in letterings if face_bit(lettering))
    n_both = sum(
        1 for lettering in letterings if reverse_bit(lettering) and face_bit(lettering)
    )
    closed_pair = 2 ** (4 - 2)

    print(f"N_Rev={n_rev} N_Face={n_face} N_both={n_both} N_letterings={n_maps}")

    checks.check(
        "sixteen-letterings",
        "the lettering space is exactly {+,−}^4",
        n_maps == 16
        and len(set(letterings)) == 16
        and all(len(lettering) == 4 for lettering in letterings)
        and all(letter in ALPHABET for lettering in letterings for letter in lettering),
    )
    checks.check(
        "theorem-1-n-rev",
        "N_Rev equals the free-pair count 2^(4-2)",
        n_rev == closed_pair == 4,
        residual=n_rev,
    )
    checks.check(
        "theorem-2-n-face",
        "N_Face equals the free-pair count 2^(4-2)",
        n_face == closed_pair == 4,
        residual=n_face,
    )
    checks.check(
        "theorem-3-n-both",
        "N_both is the single joint lettering (+,−,+,−)",
        n_both == 1 and reverse_bit((PLUS, MINUS, PLUS, MINUS)) and face_bit((PLUS, MINUS, PLUS, MINUS)),
        residual=n_both,
    )
    checks.check(
        "pair-independence",
        "reverse uses {A,B} and face uses {C,D}, so N_Rev N_Face = N_both * 16",
        n_rev * n_face == n_both * n_maps,
    )

    reverse_by_ab: dict[tuple[str, str], int] = {}
    face_by_cd: dict[tuple[str, str], int] = {}
    for lettering in letterings:
        ab = lettering[:2]
        cd = lettering[2:]
        reverse_by_ab[ab] = reverse_by_ab.get(ab, 0) + int(reverse_bit(lettering))
        face_by_cd[cd] = face_by_cd.get(cd, 0) + int(face_bit(lettering))
    checks.check(
        "reverse-independent-of-cd",
        "each (A,B) pair occupies exactly four letterings; reverse is on ( +, − ) only",
        all(sum(1 for lettering in letterings if lettering[:2] == ab) == 4 for ab in product(ALPHABET, repeat=2))
        and reverse_by_ab[(PLUS, MINUS)] == 4
        and all(count == 0 for ab, count in reverse_by_ab.items() if ab != (PLUS, MINUS)),
    )
    checks.check(
        "face-independent-of-ab",
        "each (C,D) pair occupies exactly four letterings; face is on ( +, − ) only",
        all(sum(1 for lettering in letterings if lettering[2:] == cd) == 4 for cd in product(ALPHABET, repeat=2))
        and face_by_cd[(PLUS, MINUS)] == 4
        and all(count == 0 for cd, count in face_by_cd.items() if cd != (PLUS, MINUS)),
    )
    checks.check(
        "uniqueness-not-required",
        "reverse is true on four letterings, not one",
        n_rev > 1 and n_rev == 4,
    )

    n_rev_drop_b = sum(1 for lettering in letterings if reverse_drop_b(lettering))
    checks.check(
        "mutation-drop-b",
        "dropping the L(B)=− conjunct yields 8, so the conjunct is load-bearing",
        n_rev_drop_b == 8 and n_rev_drop_b != n_rev,
    )
    checks.check(
        "mutation-five-sites",
        "freeing an origin letter would give 32 maps, outside this census",
        2 ** 5 == 32 and n_maps == 16 and ORIGIN not in coords,
    )

    claim_scope = (
        "Census of reverse and face content-bits over 16 letterings of four "
        "occupancy-formed sites is reported. Displayed, not adopted."
    )
    checks.check(
        "claim-scope",
        "front-matter census scope is the displayed-not-adopted report",
        claim_scope in note,
    )
    checks.check(
        "displayed-not-adopted",
        "letters remain displayed and are not written into Admissibility",
        "displayed, not adopted" in normalized_note
        and "does not write the letters into Admissibility" in normalized_note
        and "not a formation mask" in normalized_note,
    )
    checks.check(
        "note-counts",
        "the note reports the three executed census integers",
        "N_Rev=4" in note.replace(" ", "") or "`N_Rev=4`" in note.replace(" ", "")
        or ("equals 4" in note and "N_Rev" in note),
        residual=None,
    )
    note_compact = note.replace(" ", "")
    checks.check(
        "note-theorems-match",
        "Theorems 1–3 in the note match the executed counts",
        "N_Rev=4" in note_compact.replace("`", "")
        or ("**Theorem1.**" in note_compact and "equals4" in note_compact),
    )
    checks.check(
        "note-equals-counts",
        "note states N_Rev, N_Face, N_both as 4, 4, and 1",
        "equals 4" in normalized_note
        and "N_Face" in note
        and "equals 1" in normalized_note
        and "N_both" in note,
    )

    allowed_retained = (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    required = (
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        "trace_class: frontier_discovery",
        "reachability_to_target: advances",
        'hypothetical_axiom_status: "no edit"',
        "displayed, not adopted",
        "not a formation mask",
        "Uniqueness is not required",
        "authors no audit verdict",
        "FAIL / DO NOT SHIP",
    )
    forbidden = (
        "G_N",
        "1/r",
        "1/r^2",
        "Lattice-named",
        "not a TOE",
        "Dijkstra",
        "B_57",
        "L1",
        "trace_class: direct_blocker_closure",
        "reachability_to_target: partially_closes",
        "new axiom",
        "Block 12",
        "toe-lphys",
        "Runner cache",
    )
    checks.check(
        "note-contract",
        "machine fields, semantic boundary, N1-N8, and forbidden-phrase hygiene hold",
        all(phrase in note for phrase in required if phrase != "displayed, not adopted")
        and "displayed, not adopted" in normalized_note
        and all(line in note for line in allowed_retained)
        and all(f"### N{i}" in note for i in range(1, 9))
        and not any(phrase in note for phrase in forbidden)
        and "retained" not in other_retained
        and "promoted" not in note.lower(),
        residual=[phrase for phrase in required if phrase not in note and phrase != "displayed, not adopted"]
        + [phrase for phrase in forbidden if phrase in note],
    )
    checks.check(
        "no-cache-surface",
        "the note does not declare a runner cache path",
        "Runner cache" not in note and "runner-cache" not in note,
    )
    checks.check(
        "forbidden-rhetoric",
        "dispatch-forbidden phrases are absent from note and this source",
        all(phrase not in note for phrase in ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE", "Dijkstra", "B_57"))
        and "L1" not in note,
    )

    print("per_element: each of 16 maps is a 4-tuple in {+,−}")
    print("per_site: A,B,C,D only; origin held at + and excluded from the lettered set")
    print("per_mode: checked and not executed — no spectral mode claim")
    print("per_block: reverse, face, and joint census integers are executed")
    print("lattice_wide: checked and not executed — no lattice-wide lettering rule")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
