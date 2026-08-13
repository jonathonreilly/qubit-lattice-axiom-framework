#!/usr/bin/env python3
"""Exact checks: a lock-history length is not the Wick clock parameter a.

Histories are finite lock words. omega_coeff is derived by substituting
k4 = i a_w omega into Q_E = (k4^2 + k^2)/4 using exact Fraction
arithmetic. The runner does not install a_w = 1 and does not adopt
L_phys. No cache is written.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/LOCK_HISTORY_LENGTH_IS_NOT_WICK_CLOCK_A_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
PRIMITIVE_REL = "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/LOCK_HISTORY_LENGTH_IS_NOT_WICK_CLOCK_A_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
PRIMITIVE_PATH = ROOT / PRIMITIVE_REL
AXIOM_PATH = ROOT / AXIOM_REL

LOCK_ALPHABET = frozenset("ABCD")
H0 = ""
H2 = "AB"
H4 = "ABCD"
ALLOWED_LENGTHS = frozenset({0, 1, 2, 3, 4})
A_SAMPLES = (Fraction(1), Fraction(2))

READOUT_SENTENCES = (
    "Only records are readable.",
    "A readout value is determined by record content alone.",
    "A site with no record cannot be read.",
)
WICK_PHRASES = (
    "k4 = i a_w omega",
    "k_4 = i a_w",
    "omega_coeff",
    "a_w",
    "Wick clock",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def live_record_section(axiom: str) -> str:
    start = axiom.index("### Record / Fixed Reality")
    end = axiom.index("## Qualification")
    return axiom[start:end]


def history_length(history: str) -> int:
    """Cardinality of a finite lock word. Independent of a_w."""
    if any(letter not in LOCK_ALPHABET for letter in history):
        raise ValueError("history uses a letter outside the lock alphabet")
    n = len(history)
    if n not in ALLOWED_LENGTHS:
        raise ValueError("history length is outside the declared set")
    return n


def q_e(k4_sq: Fraction, k_sq: Fraction) -> Fraction:
    """Euclidean OS0 form Q_E = (k4^2 + k^2)/4. No Wick parameter."""
    return (k4_sq + k_sq) / Fraction(4)


def wick_k4_squared(a_w: Fraction, omega: Fraction) -> Fraction:
    """k4 = i a_w omega implies k4^2 = -a_w^2 omega^2."""
    return -(a_w * a_w) * (omega * omega)


def omega_coeff(a_w: Fraction) -> Fraction:
    """Coefficient of omega^2 after substituting k4 = i a_w omega into Q_E."""
    return q_e(wick_k4_squared(a_w, Fraction(1)), Fraction(0))


def omega_coeff_equals_length_for_all(
    a_values: tuple[Fraction, ...], histories: tuple[str, ...]
) -> bool:
    """Hostile predicate: omega_coeff(a_w) equals |H| for all a_w, H."""
    return all(
        omega_coeff(a_w) == Fraction(history_length(history))
        for a_w in a_values
        for history in histories
    )


def live_memo_contains_i_empty(axiom: str) -> bool:
    """Hostile predicate: live Record section contains I(empty)=0."""
    return "I(empty)=0" in live_record_section(axiom)


def n_or_reciprocal(n: int) -> set[Fraction]:
    if n == 0:
        raise ValueError("1/n is undefined for the empty history")
    return {Fraction(n), Fraction(1, n)}


@dataclass
class Checks:
    passed: int = 0
    failed: int = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    primitive = PRIMITIVE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    note_n = normalize(note)
    primitive_n = normalize(primitive)
    axiom_n = normalize(axiom)
    live = live_record_section(axiom)
    live_n = normalize(live)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print(
        "external_scientific_inputs: axiom memo and kinetic-isotropy "
        "primitive; no observational or fitted inputs"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read "
        "for claim-surface consistency; no runner cache is written"
    )
    print(
        "negative_scope: lock-history length as a selector of a_w is "
        "rejected; a declared continuation remains extra"
    )

    checks.check(
        "audit-input-paths",
        "declared audit inputs are the new note, kinetic isotropy, and axiom memo",
        AUDIT_INPUT_PATHS == (NOTE_REL, PRIMITIVE_REL, AXIOM_REL)
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )
    checks.check(
        "source-record-readout",
        "the three live Record readout sentences occur verbatim",
        all(sentence in live_n for sentence in READOUT_SENTENCES),
    )
    checks.check(
        "source-records-form-lock-permanence",
        "live Record names formation, locking, and permanence",
        "Records form." in live
        and "a record locks exactly one admissible local possibility" in live_n
        and "records are permanent" in live_n,
    )
    checks.check(
        "source-named-I-not-content",
        "named I and I(empty)=0 are stated not to be Record axiom content",
        "a named scalar collection functional `I`" in axiom
        and "`I(empty)=0` are not Record axiom content" in axiom_n,
    )
    checks.check(
        "source-kinetic-os0",
        "the primitive supplies Euclidean c_t = c_s / OS0, not a_w",
        "c_t = c_s" in primitive
        and "Osterwalder-Schrader OS0 kinetic" in primitive_n
        and all(phrase not in primitive for phrase in WICK_PHRASES),
    )

    n2 = history_length(H2)
    n4 = history_length(H4)
    n0 = history_length(H0)
    checks.check(
        "theorem-1-histories",
        "H2=AB and H4=ABCD are lawful lock words with n=2 and n=4",
        n2 == 2
        and n4 == 4
        and n0 == 0
        and set(H2) <= LOCK_ALPHABET
        and set(H4) <= LOCK_ALPHABET
        and H2 != H4
        and {n0, n2, n4} <= ALLOWED_LENGTHS,
    )
    checks.check(
        "theorem-1-blank-unread",
        "blank unread: empty history has no lock content and is not a clock readout",
        n0 == 0
        and "A site with no record cannot be read." in live_n
        and "Do not assign a readout to empty sites" in note_n,
    )

    coeff_one = omega_coeff(Fraction(1))
    coeff_two = omega_coeff(Fraction(2))
    length_values = n_or_reciprocal(n2) | n_or_reciprocal(n4)
    checks.check(
        "theorem-2-omega-coeff",
        "derived omega_coeff(1)=-1/4 and omega_coeff(2)=-1",
        coeff_one == Fraction(-1, 4) and coeff_two == Fraction(-1),
    )
    checks.check(
        "theorem-2-distinct",
        "omega_coeff(1) and omega_coeff(2) are different",
        coeff_one != coeff_two,
    )
    checks.check(
        "theorem-2-neither-n-nor-reciprocal",
        "neither coefficient equals n or 1/n for n=2 and n=4",
        coeff_one not in length_values and coeff_two not in length_values,
    )
    checks.check(
        "theorem-2-q-e-independent",
        "Q_E has no a_w argument and is unchanged across Wick samples",
        q_e(Fraction(4), Fraction(9)) == Fraction(13, 4)
        and q_e.__code__.co_argcount == 2
        and omega_coeff(Fraction(1)) == q_e(wick_k4_squared(Fraction(1), Fraction(1)), Fraction(0)),
    )
    checks.check(
        "theorem-3-os0-not-function-of-H",
        "OS0 is c_t=c_s, not a function of |H|",
        "c_t = c_s" in primitive
        and q_e(Fraction(1), Fraction(1)) == Fraction(1, 2)
        and history_length(H2) != history_length(H4)
        and "not a function of `|H|`" in note,
    )
    checks.check(
        "theorem-3-record-names-no-wick",
        "live Record names no Wick parameter; a_w remains extra",
        all(phrase not in live for phrase in WICK_PHRASES)
        and "clock map `a_w` remains extra" in note,
    )
    checks.check(
        "theorem-3-no-a1-no-lphys",
        "the note does not install a_w=1 and does not adopt L_phys",
        "does not install `a_w = 1`" in note
        and "does not adopt `L_phys`" in note
        and "L_phys" not in live
        and "L_phys" not in primitive,
    )

    displayed = (H2, H4)
    checks.check(
        "mutation-omega-equals-length-fails",
        "predicate omega_coeff(a_w) equals |H| for all a_w,H fails",
        omega_coeff_equals_length_for_all(A_SAMPLES, displayed) is False
        and coeff_one != Fraction(n2)
        and coeff_two != Fraction(n4),
    )
    checks.check(
        "mutation-live-I-empty-fails",
        "predicate live memo contains I(empty)=0 fails",
        live_memo_contains_i_empty(axiom) is False
        and "I(empty)=0" not in live
        and "A site with no record cannot be read." in live_n,
    )

    checks.check(
        "note-quotes-live-record",
        "the note quotes the live Record sentences and that named I is not content",
        all(sentence in note_n for sentence in READOUT_SENTENCES)
        and "Named `I` is not axiom content" in note,
    )
    checks.check(
        "note-parents-and-witnesses",
        "the note links both parents and records the displayed algebra",
        "MINIMAL_AXIOMS_2026-06-29.md" in note
        and "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md" in note
        and "H2 = AB" in note
        and "H4 = ABCD" in note
        and "omega_coeff(1) = -1/4" in note
        and "omega_coeff(2) = -1" in note
        and "omega_coeff(a_w) = -a_w^2 / 4" in note,
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
    )
    checks.check(
        "machine-status-contract",
        "the source uses the controlled bounded-support fields",
        "actual_current_surface_status: bounded-support" in note
        and "target_claim_type: bounded_theorem" in note
        and "trace_class: negative_route_pruning" in note
        and "This is current Record, not a retype." in note,
    )

    forbidden = ("new axiom", "we adopt", "promoted", "Codex")
    retained_hits = [
        line
        for line in note.splitlines()
        if "retained" in line
        and "audit_required_before_effective_retained" not in line
        and "bare_retained_allowed" not in line
    ]
    checks.check(
        "forbidden-rhetoric-absent",
        "the note avoids axiom-adoption, promotion, and executor-name rhetoric",
        all(phrase not in note for phrase in forbidden) and retained_hits == [],
    )
    checks.check(
        "identity-gates-present",
        "identity gates history_length and omega_coeff are the called maps",
        history_length.__doc__ is not None
        and "Independent of a_w" in (history_length.__doc__ or "")
        and omega_coeff(Fraction(2)) == Fraction(-1)
        and "def omega_coeff(" in Path(__file__).read_text(encoding="utf-8"),
    )

    print(
        "per_element: a_w in {1, 2} tested against lock words of length 2 and 4"
    )
    print(
        "per_site: a history is a word of already-formed locks; blanks are unread"
    )
    print(
        "per_mode: quadratic OS0 TT form only; no spectral-mode exhaustion"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
