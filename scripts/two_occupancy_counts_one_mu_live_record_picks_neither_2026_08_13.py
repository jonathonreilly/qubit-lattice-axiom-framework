#!/usr/bin/env python3
"""Exact checks: two occupancy counts at one μ; live Record picks neither rate.

The runner builds a four-site window, one shared content law μ, and two
record configurations. It counts formed locks, computes the empirical
window ratios in Fraction arithmetic, and checks the live Record block
for blank-unread wording without restoring I. It adopts no rate law.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "TWO_OCCUPANCY_COUNTS_ONE_MU_LIVE_RECORD_PICKS_NEITHER_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/TWO_OCCUPANCY_COUNTS_ONE_MU_LIVE_RECORD_PICKS_NEITHER_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

WINDOW = ("w", "x", "y", "z")
A = "A"
B = "B"
BLANK = None
MU = {A: Fraction(3, 5), B: Fraction(2, 5)}

SIGMA1 = {"w": A, "x": BLANK, "y": BLANK, "z": BLANK}
SIGMA2 = {"w": A, "x": A, "y": BLANK, "z": BLANK}


def normalize(text: str) -> str:
    return " ".join(text.split())


def formed_sites(sigma: dict[str, str | None]) -> tuple[str, ...]:
    return tuple(site for site in WINDOW if sigma[site] is not BLANK)


def n_formed(sigma: dict[str, str | None]) -> int:
    return len(formed_sites(sigma))


def empirical_rate(sigma: dict[str, str | None]) -> Fraction:
    return Fraction(n_formed(sigma), len(WINDOW))


def locked_contents(sigma: dict[str, str | None]) -> tuple[str, ...]:
    return tuple(sigma[site] for site in formed_sites(sigma))


def compatible_with_mu(sigma: dict[str, str | None]) -> bool:
    return all(MU[content] > 0 for content in locked_contents(sigma))


def record_axiom_block(axiom_text: str) -> str:
    start = axiom_text.index("### Record / Fixed Reality")
    end = axiom_text.index("## Qualification")
    return axiom_text[start:end]


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
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    live_record = record_axiom_block(axiom)
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)
    live_record_flat = normalize(live_record)

    print("external_scientific_inputs: live axiom wording only; no observational or fitted inputs")
    print("package_local_integrity_reads: the source note is read for claim-surface consistency")
    print("negative_scope: neither displayed window ratio is adopted; I is not restored")

    rate1 = empirical_rate(SIGMA1)
    rate2 = empirical_rate(SIGMA2)
    readout1 = formed_sites(SIGMA1)
    readout2 = formed_sites(SIGMA2)
    blanks1 = tuple(site for site in WINDOW if site not in readout1)
    blanks2 = tuple(site for site in WINDOW if site not in readout2)

    checks.check(
        "window-cardinality",
        "the declared window has four sites",
        WINDOW == ("w", "x", "y", "z") and len(WINDOW) == 4,
    )
    checks.check(
        "content-law",
        "μ assigns 3/5 and 2/5 and is a probability on {A,B}",
        MU[A] == Fraction(3, 5)
        and MU[B] == Fraction(2, 5)
        and MU[A] + MU[B] == 1
        and set(MU) == {A, B},
    )
    checks.check(
        "same-mu",
        "both configurations are compatible with that one content law",
        compatible_with_mu(SIGMA1)
        and compatible_with_mu(SIGMA2)
        and locked_contents(SIGMA1) == (A,)
        and locked_contents(SIGMA2) == (A, A),
    )
    checks.check(
        "occupancy-split",
        "formed counts are 1 and 2 on the same window",
        n_formed(SIGMA1) == 1 and n_formed(SIGMA2) == 2,
    )
    checks.check(
        "empirical-rates",
        "computed window ratios are exactly 1/4 and 1/2",
        rate1 == Fraction(1, 4) and rate2 == Fraction(1, 2),
    )
    checks.check(
        "theorem-1-rates-differ",
        "same μ does not force equal occupancy ratios",
        rate1 != rate2 and n_formed(SIGMA1) != n_formed(SIGMA2),
    )
    checks.check(
        "theorem-2-sigma1-readout",
        "site readout of σ1 is defined only at w",
        readout1 == ("w",) and blanks1 == ("x", "y", "z"),
    )
    checks.check(
        "theorem-2-sigma2-readout",
        "site readout of σ2 is defined only at w and x",
        readout2 == ("w", "x") and blanks2 == ("y", "z"),
    )
    checks.check(
        "theorem-2-blank-not-readout",
        "blank occupancy is not a site readout: unread sites have no content",
        all(SIGMA1[site] is BLANK for site in blanks1)
        and all(SIGMA2[site] is BLANK for site in blanks2)
        and BLANK not in MU,
    )
    checks.check(
        "theorem-2-rate-uses-blanks",
        "each ratio puts unread blanks in the denominator",
        n_formed(SIGMA1) + len(blanks1) == len(WINDOW)
        and n_formed(SIGMA2) + len(blanks2) == len(WINDOW)
        and rate1 == Fraction(n_formed(SIGMA1), len(WINDOW))
        and rate2 == Fraction(n_formed(SIGMA2), len(WINDOW))
        and len(blanks1) > 0
        and len(blanks2) > 0,
    )
    checks.check(
        "mutation-equal-rates",
        "predicate r(σ1)==r(σ2) fails",
        (rate1 == rate2) is False,
    )
    checks.check(
        "mutation-i-empty",
        "predicate live memo contains I(empty)=0 fails",
        "I(empty)=0" not in live_record and "I(empty)=0" not in live_record_flat,
    )
    checks.check(
        "source-blank-unread",
        "live Record states that a site with no record cannot be read",
        "A site with no record cannot be read." in live_record,
    )
    checks.check(
        "source-content-only",
        "live Record names content-only readout and does not name I",
        "A readout value is determined by record content alone." in live_record_flat
        and "Only records are readable." in live_record
        and "Records form." in live_record
        and "`I`" not in live_record,
    )
    checks.check(
        "source-i-not-content",
        "the memo states that I(empty)=0 is not Record axiom content",
        "assigned value `I(empty)=0` are not Record axiom content" in axiom_flat,
    )
    checks.check(
        "source-rate-downstream",
        "the memo keeps formation rate outside axiom supply",
        "it does not supply the formation site, probability, or rate" in axiom_flat
        and "at what rate" in axiom_flat,
    )
    checks.check(
        "note-displays-both-rates",
        "the note displays 1/4 and 1/2 and adopts neither",
        "`r(σ1)=1/4`" in note
        and "`r(σ2)=1/2`" in note
        and "Neither rate is adopted" in note
        and "does not install a rate law" in note,
    )
    checks.check(
        "note-does-not-restore-i",
        "the note quotes live blank-unread Record and does not restore I",
        "A site with no record cannot be read." in note
        and "they are not restored here" in note
        and "does not restore `I` or `I(empty)=0`" in note,
    )
    checks.check(
        "machine-status-contract",
        "the source uses the controlled bounded-support fields",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "claim_type_reason:",
                "trace_class: negative_route_pruning",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the new note and the axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/TWO_OCCUPANCY_COUNTS_ONE_MU_LIVE_RECORD_PICKS_NEITHER_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and Path(__file__).name in note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
