#!/usr/bin/env python3
"""Route-2 nonblind source/readout primitive admissibility gate.

This runner checks the current-bank candidates for the S3/Route-2 endpoint
triple obstruction. It does not audit or assign an effective repo status. It
formalizes the minimum conditions an independent nonblind primitive would need
to satisfy before it could derive the remaining E-center value
rho_E = beta_E/alpha_E = 21/4.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS_COUNT = 0
FAIL_COUNT = 0

DELTA_CENTER = Fraction(1, 6)
RHO_T = Fraction(-1, 1)
S_TE = Fraction(-2, 1)
Q_T = Fraction(5, 6)
TARGET_RHO_E = Fraction(21, 4)
TARGET_Q_E = Fraction(15, 8)
TARGET_C_TE = Fraction(-8, 9)
F_ADJ_NC3 = Fraction(8, 9)


@dataclass(frozen=True)
class Candidate:
    name: str
    source: str
    sees_e_center: bool
    selects_unique_value: bool
    target_free: bool
    typed_route2_readout: bool
    current_surface: bool
    gives_target: bool
    defect: str

    @property
    def passes_gate(self) -> bool:
        return (
            self.sees_e_center
            and self.selects_unique_value
            and self.target_free
            and self.typed_route2_readout
            and self.current_surface
            and self.gives_target
        )


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        print(f"PASS: {name}")
    else:
        FAIL_COUNT += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def q_e(rho_e: Fraction) -> Fraction:
    return Fraction(1, 1) + rho_e * DELTA_CENTER


def rho_from_q(q: Fraction) -> Fraction:
    return Fraction(6, 1) * (q - 1)


def c_te_from_rho(rho_e: Fraction) -> Fraction:
    return S_TE * Q_T / q_e(rho_e)


def f_adj(n_c: int) -> Fraction:
    return Fraction(n_c * n_c - 1, n_c * n_c)


def current_candidates() -> list[Candidate]:
    return [
        Candidate(
            name="carrier_time_factor_rigidity_family",
            source="S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md",
            sees_e_center=True,
            selects_unique_value=False,
            target_free=True,
            typed_route2_readout=True,
            current_surface=True,
            gives_target=False,
            defect="universal time factor; spatial prefactor keeps rho_E arbitrary",
        ),
        Candidate(
            name="registration_idempotency_positivity",
            source="ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md",
            sees_e_center=True,
            selects_unique_value=False,
            target_free=True,
            typed_route2_readout=True,
            current_surface=True,
            gives_target=False,
            defect="norm/sign conditions leave the direction rho_E free or bounded only",
        ),
        Candidate(
            name="ell_E_positive_projective_sign_universality",
            source="QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md",
            sees_e_center=True,
            selects_unique_value=False,
            target_free=True,
            typed_route2_readout=True,
            current_surface=True,
            gives_target=False,
            defect="derives c_TE < 0 on the positive family, not |c_TE| = 8/9",
        ),
        Candidate(
            name="active_branch_eta_floor_endpoint_slopes",
            source="QUARK_ROUTE2_ENDPOINT_STEP_FREE_ACTIVE_BRANCH_SLOPES_BOUNDED_NOTE_2026-06-12.md",
            sees_e_center=True,
            selects_unique_value=False,
            target_free=False,
            typed_route2_readout=False,
            current_surface=True,
            gives_target=False,
            defect="finite implemented-envelope comparator; no closed-form endpoint triple",
        ),
        Candidate(
            name="measured_e_center_lift_calibration",
            source="QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md",
            sees_e_center=True,
            selects_unique_value=False,
            target_free=False,
            typed_route2_readout=False,
            current_surface=True,
            gives_target=False,
            defect="nonblind comparator evidence; exact infinite-volume identification remains open",
        ),
        Candidate(
            name="F_adj_or_R_conn_color_fraction",
            source="QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md",
            sees_e_center=False,
            selects_unique_value=True,
            target_free=True,
            typed_route2_readout=False,
            current_surface=True,
            gives_target=True,
            defect="exact target only after missing color/support endpoint bridge is supplied",
        ),
        Candidate(
            name="register_not_read_color_trace_shortcut",
            source="RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md",
            sees_e_center=False,
            selects_unique_value=False,
            target_free=True,
            typed_route2_readout=False,
            current_surface=True,
            gives_target=False,
            defect="Record supplies no physical EW readout or weighting rule",
        ),
        Candidate(
            name="explicit_q_E_15_8_or_c_TE_minus_8_9_premise",
            source="QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md",
            sees_e_center=True,
            selects_unique_value=True,
            target_free=False,
            typed_route2_readout=True,
            current_surface=False,
            gives_target=True,
            defect="this is exactly the missing premise, not an independent derivation",
        ),
    ]


def part1_exact_endpoint_algebra() -> None:
    print("PART 1: exact endpoint algebra")
    check("delta_A1 center step is 1/6", DELTA_CENTER == Fraction(1, 6))
    check("granted T side gives q_T = 5/6", Fraction(1, 1) + RHO_T / 6 == Q_T)
    check("target rho_E gives target q_E", q_e(TARGET_RHO_E) == TARGET_Q_E)
    check("target q_E gives target rho_E", rho_from_q(TARGET_Q_E) == TARGET_RHO_E)
    check("target rho_E gives target center ratio", c_te_from_rho(TARGET_RHO_E) == TARGET_C_TE)
    check("F_adj(N_c=3) is 8/9", f_adj(3) == F_ADJ_NC3)
    check("minus F_adj equals target center ratio", -F_ADJ_NC3 == TARGET_C_TE)
    check("rho_E=0 is exact but not the target", q_e(Fraction(0, 1)) == 1 and c_te_from_rho(Fraction(0, 1)) != TARGET_C_TE)


def part2_sign_not_magnitude() -> None:
    print()
    print("PART 2: sign universality is not a magnitude selector")
    samples = [Fraction(-5, 1), Fraction(0, 1), Fraction(1, 1), TARGET_RHO_E, Fraction(7, 1)]
    for rho in samples:
        check(
            f"positive E-family sample rho_E={rho} gives negative c_TE",
            rho > Fraction(-6, 1) and c_te_from_rho(rho) < 0,
            f"c_TE={c_te_from_rho(rho)}",
        )
    check(
        "sign condition alone admits a non-target exact witness",
        c_te_from_rho(Fraction(0, 1)) < 0 and c_te_from_rho(Fraction(0, 1)) == Fraction(-5, 3),
        "rho_E=0 gives c_TE=-5/3",
    )
    check(
        "pinning c_TE=-8/9 is exactly equivalent to rho_E=21/4 under granted T side",
        rho_from_q(S_TE * Q_T / TARGET_C_TE) == TARGET_RHO_E,
    )


def part3_source_markers() -> None:
    print()
    print("PART 3: source-surface marker checks")
    required = {
        "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md": [
            "endpoint triple",
            "not derived by the current exact stack",
            "open_gate",
        ],
        "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md": [
            "beta_E / alpha_E = 21/4",
            "rho_E",
            "exact missing map entry",
        ],
        "S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md": [
            "structurally localized in the spatial prefactor",
            "valid for every admissible readout",
            "derive the unresolved readout-triple",
        ],
        "ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md": [
            "`rho_E` is the readout direction",
            "rho_E > -6",
            "Selecting `rho_E` requires a shell-vs-center",
        ],
        "QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md": [
            "c_TE < 0",
            "magnitude remains open",
            "rho_E > -6",
        ],
        "QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md": [
            "source bank does not contain an exact E-channel row",
            "derive gamma_E(center)/gamma_E(shell) = 15/8",
            "does not establish:",
        ],
        "QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md": [
            "`MISSING_BRIDGE` remains outside the derived",
            "gamma_T(center)/gamma_E(center) = -R_conn",
            "beta_E/alpha_E = 21/4",
        ],
        "RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md": [
            "Count is not weight.",
            "Record does not supply the missing readout context.",
            "the separate Route-2 `c_TE = -R_conn` bridge",
        ],
        "QUARK_ROUTE2_ENDPOINT_STEP_FREE_ACTIVE_BRANCH_SLOPES_BOUNDED_NOTE_2026-06-12.md": [
            "does not claim a closed form",
            "finite Route-2 tensor-stencil endpoint observable",
            "The named open target remains",
        ],
        "QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md": [
            "exact infinite-volume",
            "E-center",
        ],
    }
    for filename, markers in required.items():
        text = read_text(DOCS / filename)
        check(f"{filename} exists", bool(text))
        for marker in markers:
            check(f"{filename} contains marker: {marker}", marker in text)


def part4_candidate_gate() -> None:
    print()
    print("PART 4: current-bank nonblind primitive gate")
    candidates = current_candidates()
    for candidate in candidates:
        print(
            "  "
            + candidate.name
            + ": sees_e_center="
            + str(candidate.sees_e_center)
            + ", selects_unique_value="
            + str(candidate.selects_unique_value)
            + ", target_free="
            + str(candidate.target_free)
            + ", typed_route2_readout="
            + str(candidate.typed_route2_readout)
            + ", current_surface="
            + str(candidate.current_surface)
            + ", gives_target="
            + str(candidate.gives_target)
        )
        print("      defect: " + candidate.defect)
        check(f"{candidate.name} has at least one named gate defect", not candidate.passes_gate)
    check(
        "no current-bank candidate satisfies all nonblind primitive gate conditions",
        not any(candidate.passes_gate for candidate in candidates),
    )
    check(
        "the gate preserves an explicit positive path",
        any(candidate.name == "explicit_q_E_15_8_or_c_TE_minus_8_9_premise" and candidate.gives_target for candidate in candidates),
        "future primitive must supply q_E=15/8 or typed c_TE=-8/9 without using the target as input",
    )


def part5_note_hygiene() -> None:
    print()
    print("PART 5: companion note hygiene")
    note = DOCS / "QUARK_ROUTE2_NONBLIND_SOURCE_READOUT_PRIMITIVE_GATE_NO_GO_NOTE_2026-06-21.md"
    text = read_text(note)
    check("companion note exists", bool(text), str(note.relative_to(ROOT)))
    required_phrases = [
        "Actual current-surface status: no-go over the named current-bank candidate families",
        "This is not an audit verdict",
        "A_min",
        "Forbidden proof inputs",
        "Admissibility Gate",
        "Theorem",
        "does not rule out a future primitive",
        "**TRACE:** negative_route_pruning",
    ]
    for phrase in required_phrases:
        check(f"companion note contains phrase: {phrase}", phrase in text)
    banned_overclaim = [
        ("parent closure", "closes the " + "parent " + "open_gate"),
        ("endpoint triple derivation", "derives the endpoint " + "triple"),
        ("current-surface rho_E derivation", "derives rho_E = 21/4 on the current " + "surface"),
        ("global future-primitive impossibility", "all possible future primitives are " + "impossible"),
    ]
    for label, phrase in banned_overclaim:
        check(f"companion note avoids overclaim: {label}", phrase not in text)


def main() -> int:
    print("Route-2 nonblind source/readout primitive admissibility gate")
    print("Status: no-go over named current-bank candidate families; not an audit verdict.")
    print("TRACE: negative_route_pruning")
    print()
    part1_exact_endpoint_algebra()
    part2_sign_not_magnitude()
    part3_source_markers()
    part4_candidate_gate()
    part5_note_hygiene()
    print()
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print(
            "VERDICT: no named current-bank nonblind source/readout primitive "
            "satisfies the admissibility gate. A future positive route must "
            "supply a target-free typed E-center selector q_E=15/8 or the "
            "typed center bridge c_TE=-8/9."
        )
        return 0
    print("VERDICT: gate checks failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
