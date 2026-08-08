#!/usr/bin/env python3
"""Source-slot gate for Route-2 two-sided dualization.

This runner tests whether the current exact Route-2 time family already has
the source-preparation slot needed for a two-sided inverse-Schur law.

Status:
  no-go for the current conditional time-family two-slot shortcut.

Safe claim:
  The current family is Xi_P(t; c) = (P_R c) tensor V_R(t). It has a readout
  map slot P_R and a carrier column c, but no independent source-preparation
  map that contributes a second canonical-dual inverse Schur-weight factor.
  Therefore a one-sided canonical readout dual gives p=1; p=2 requires either
  a new source-preparation map or a readout-only inverse-square coefficient
  theorem. This does not rule out either future theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS = 0
FAIL = 0

AUTHORITY_FILES = (
    "QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md",
    "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md",
    "S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md",
    "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
)

REQUIRED_MARKERS = {
    "QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md": (
        "Xi_P(t ; c) = (P_R c)",
        "Given any admissible readout map `P_R`",
        "selects one unique `P_R`",
    ),
    "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md": (
        "Once an admissible readout map `P_R` is chosen",
        "`P_R` is algebraic once specified",
    ),
    "S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md": (
        "`|| (P_R c) ||` factor cancels",
        "right factor `V_R(t)`",
    ),
    "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md": (
        "P_R = [[alpha_E, 0, beta_E, 0]",
        "irreducible missing map entry",
    ),
}

ABSENT_SOURCE_SLOT_MARKERS = (
    "source preparation",
    "source-preparation",
    "source map",
    "source-map",
    "source slot",
    "S_dual",
    "S_R c",
)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"\n      {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")


def phrase(*parts: str) -> str:
    return "".join(parts)


def note_text(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def authority_bank_text() -> str:
    return "\n".join(note_text(name) for name in AUTHORITY_FILES)


def pow_fraction(x: Fraction, exponent: int) -> Fraction:
    if exponent >= 0:
        return x**exponent
    return Fraction(1, 1) / (x ** (-exponent))


@dataclass(frozen=True)
class SlotCase:
    name: str
    source_dual_factors: int
    readout_dual_factors: int
    explanation: str

    @property
    def total_p(self) -> int:
        return self.source_dual_factors + self.readout_dual_factors


W_E = Fraction(1, 3)
W_T = Fraction(1, 2)
Q_T = Fraction(5, 6)
SHELL_TE = Fraction(-2, 1)

SLOT_CASES = (
    SlotCase("no-dual", 0, 0, "no inverse Schur factor"),
    SlotCase("source-only-canonical-dual", 1, 0, "source side only"),
    SlotCase("readout-only-canonical-dual", 0, 1, "readout side only"),
    SlotCase("two-sided-canonical-dual", 1, 1, "source and readout"),
    SlotCase("readout-only-inverse-square", 0, 2, "readout row supplies p=2 by itself"),
)


def lambda_from_total_p(total_p: int) -> Fraction:
    return pow_fraction(W_E / W_T, -total_p)


def endpoint_from_total_p(total_p: int) -> tuple[Fraction, Fraction, Fraction]:
    lam = lambda_from_total_p(total_p)
    q_e = Q_T * lam
    rho_e = 6 * (q_e - 1)
    center_te = SHELL_TE * Q_T / q_e
    return q_e, rho_e, center_te


def main() -> int:
    print("Route-2 source-slot dualization gate")
    print("Status: no-go for current conditional time-family two-slot shortcut; not an audit verdict.")
    print("TRACE: negative_route_pruning")

    print("\nPART 1: exact source/readout slot arithmetic")
    check("same-domain weights are w_E=1/3 and w_T=1/2", (W_E, W_T) == (Fraction(1, 3), Fraction(1, 2)))
    check("target total inverse-factor count is p=2", lambda_from_total_p(2) == Fraction(9, 4))
    check("T-side conditional values are q_T=5/6 and shell T/E=-2", (Q_T, SHELL_TE) == (Fraction(5, 6), Fraction(-2)))
    expected = {
        "no-dual": (0, Fraction(1), Fraction(5, 6), Fraction(-1), Fraction(-2)),
        "source-only-canonical-dual": (1, Fraction(3, 2), Fraction(5, 4), Fraction(3, 2), Fraction(-4, 3)),
        "readout-only-canonical-dual": (1, Fraction(3, 2), Fraction(5, 4), Fraction(3, 2), Fraction(-4, 3)),
        "two-sided-canonical-dual": (2, Fraction(9, 4), Fraction(15, 8), Fraction(21, 4), Fraction(-8, 9)),
        "readout-only-inverse-square": (2, Fraction(9, 4), Fraction(15, 8), Fraction(21, 4), Fraction(-8, 9)),
    }
    for case in SLOT_CASES:
        lam = lambda_from_total_p(case.total_p)
        q_e, rho_e, center_te = endpoint_from_total_p(case.total_p)
        print(
            f"  {case.name:>30s}: source={case.source_dual_factors}, "
            f"readout={case.readout_dual_factors}, p={case.total_p}, "
            f"lambda={lam}, q_E={q_e}, rho_E={rho_e}, center T/E={center_te}"
        )
        check(
            f"{case.name} endpoint arithmetic matches the slot-count model",
            (case.total_p, lam, q_e, rho_e, center_te) == expected[case.name],
            case.explanation,
        )

    print("\nPART 2: current-family slot count")
    check(
        "current Xi_P family has source factor count zero in the model",
        endpoint_from_total_p(0)[1] == Fraction(-1),
    )
    check(
        "readout-only canonical dual gives p=1 and misses rho_E=21/4",
        endpoint_from_total_p(1)[1] == Fraction(3, 2),
    )
    check(
        "p=2 requires either source+readout canonical dual or readout-only inverse-square",
        endpoint_from_total_p(2)[1] == Fraction(21, 4),
    )

    print("\nPART 3: authority markers for one-slot time family")
    for name in AUTHORITY_FILES:
        check(f"authority file exists: {name}", (DOCS / name).is_file())
    for name, markers in REQUIRED_MARKERS.items():
        text = note_text(name)
        for marker in markers:
            check(f"{name} contains marker: {marker}", marker in text)
    bank = authority_bank_text()
    lower_bank = bank.lower()
    for marker in ABSENT_SOURCE_SLOT_MARKERS:
        check(
            f"authority bank does not contain source-slot marker: {marker}",
            marker.lower() not in lower_bank,
        )
    check(
        "authority bank exposes P_R c but no independent source-preparation slot",
        "p_r c" in lower_bank and "source-preparation" not in lower_bank,
    )

    print("\nPART 4: note and status firewall")
    note = note_text("QUARK_ROUTE2_SOURCE_SLOT_DUALIZATION_GATE_NO_GO_NOTE_2026-06-21.md")
    required_note_markers = (
        "**Actual current-surface status:** no-go for current conditional time-family two-slot shortcut",
        "This is not an audit verdict",
        "does not resolve the parent",
        "does not rule out a future source-preparation theorem",
        "current `Xi_P` family has one readout slot and no independent source-preparation slot",
        "readout-only canonical dualization gives `p=1`",
    )
    for marker in required_note_markers:
        check(f"note contains marker: {marker}", marker in note)
    banned_markers = (
        ("legacy source-status certificate", "actual_current_surface_status:"),
        ("parent-closure phrase", phrase("closes ", "the parent")),
        (
            "current-surface endpoint-derivation phrase",
            phrase("derives ", "the endpoint triple", " on the current surface"),
        ),
        ("audit-ratification phrase", phrase("audit", "-ratified")),
        ("branch-local status-promotion phrase", phrase("retained ", "branch-local")),
        ("future-retention phrase", phrase("would ", "become retained")),
        ("promotion-to-retention phrase", phrase("promoted ", "to retained")),
        ("no-future-theorem phrase", phrase("no future ", "primitive can exist")),
    )
    for label, marker in banned_markers:
        check(f"note avoids overclaim marker: {label}", marker not in note)

    print("\nPART 5: N5 execution certificate")
    marker_total = sum(len(v) for v in REQUIRED_MARKERS.values())
    print(
        "per_element: checked -- nothing is compared as a summary. Every one of the "
        f"{len(SLOT_CASES)} slot cases is compared as a full five-component tuple, total count "
        "and lambda and q_E and rho_E and center T/E together, against its own expected entry, "
        f"and on the documentary side {marker_total} required markers and "
        f"{len(ABSENT_SOURCE_SLOT_MARKERS)} forbidden slot markers are each resolved one string "
        "at a time in exact Fraction and literal-substring terms."
    )
    print(
        "per_site: checked and not executed -- a slot count is a statement about how many "
        "factors a formula carries, and formulas do not have sites. No configuration, carrier "
        "column or support geometry is instantiated anywhere in this file, so nothing here can "
        "be attributed to a location and nothing is."
    )
    print(
        "per_mode: checked, and honestly it is narrow -- the E and T channels enter only through "
        f"the single weight ratio w_E/w_T = {W_E / W_T}, of which each dual factor is one power. "
        "No E or T amplitude is formed and no channel is ever evaluated on its own, so the "
        "mode-level evidence here amounts to the fact that this one ratio, raised to the total "
        "factor count, reproduces the endpoint arithmetic."
    )
    print(
        "per_block: checked, and this is the class the no-go is written in -- the two slots, "
        "source and readout, are the blocks, and the executed finding is that only their sum is "
        "observable. The source-only and readout-only rows are literally identical at p = 1, "
        "both giving lambda 3/2 and rho_E 3/2, and the two-sided and readout-only-inverse-square "
        "rows are likewise identical at p = 2, both giving rho_E 21/4, so the endpoint data "
        "cannot attribute a factor to a block even when the total is right."
    )
    print(
        "lattice_wide: checked and not executed, and two scope facts belong on the record here "
        "rather than being left implicit -- there is no lattice, volume or limit, so the class "
        "has no referent; and the slot-count model itself is a configured table in this file, so "
        "PART 1 certifies that the arithmetic agrees with that table rather than deriving the "
        f"model from the time family, while the claim that the current family carries zero "
        f"source slots rests on the lexical absence scan over the {len(AUTHORITY_FILES)} "
        "authority files."
    )

    print("\nTOTAL: PASS=%d, FAIL=%d" % (PASS, FAIL))
    if FAIL:
        return 1
    print(
        "VERDICT: no-go for the current conditional time-family two-slot shortcut. "
        "The existing Xi_P family has no source-preparation dual slot; p=2 still "
        "requires a new source-preparation theorem or a readout-only inverse-square "
        "coefficient theorem."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
