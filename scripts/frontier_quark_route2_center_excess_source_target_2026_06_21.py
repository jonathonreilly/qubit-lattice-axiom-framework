#!/usr/bin/env python3
"""Exact center-excess source target for the Route-2 endpoint triple.

This runner does not claim that the current repo already derives the source
map. It isolates the exact normalized source-excess theorem that would be
needed if the readout side supplies one inverse Schur-weight factor.

Status:
  bounded-support for the next source-map theorem target.

Safe claim:
  Under the T-side candidates, shell normalization, and the one-power readout
  premise rho_E = 3/2, an endpoint-normalized source map

      S = diag(a_E, a_T, b_E, b_T)

  reaches the target triple exactly iff

      a_T/a_E = 1,
      b_T/a_T = 1,
      b_E/a_E = 7/2.

  This sharpens the next proof obligation. It is not an audit verdict and does
  not assert that such an S is present in the current authority bank.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SCRIPTS = ROOT / "scripts"

PASS = 0
FAIL = 0

READOUT_NOTE = "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
SCHUR_RUNNER = "frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py"

READOUT_MARKERS = (
    "P_R = [[alpha_E, 0, beta_E, 0]",
    "q_E   := gamma_E(center) / gamma_E(shell) = 1 + (beta_E / alpha_E) / 6",
    "beta_E / alpha_E = 21/4",
    "irreducible missing map entry",
)

SCHUR_MARKERS = (
    "weights (1/6, 1/3, 1/2)",
    "(w_E/w_T1)^{-1} = 3/2 = kappa",
    "(w_E/w_T1)^{-2} = 9/4",
    "No named functional produces an",
)

TARGET_RHO_T = Fraction(-1, 1)
TARGET_SHELL_TE = Fraction(-2, 1)
TARGET_RHO_E = Fraction(21, 4)
TARGET_Q_T = Fraction(5, 6)
TARGET_Q_E = Fraction(15, 8)
TARGET_CENTER_TE = Fraction(-8, 9)
W_E = Fraction(1, 3)
W_T = Fraction(1, 2)


def phrase(*parts: str) -> str:
    return "".join(parts)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"\n      {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def q_from_rho(rho: Fraction) -> Fraction:
    return Fraction(1, 1) + rho / 6


def rho_from_q(q: Fraction) -> Fraction:
    return 6 * (q - 1)


def center_te(shell_te: Fraction, q_t: Fraction, q_e: Fraction) -> Fraction:
    return shell_te * q_t / q_e


@dataclass(frozen=True)
class ReadoutRatios:
    rho_t: Fraction
    shell_te: Fraction
    rho_e: Fraction

    @property
    def q_t(self) -> Fraction:
        return q_from_rho(self.rho_t)

    @property
    def q_e(self) -> Fraction:
        return q_from_rho(self.rho_e)

    @property
    def center_te(self) -> Fraction:
        return center_te(self.shell_te, self.q_t, self.q_e)


@dataclass(frozen=True)
class SourceExcessRatios:
    shell_scale_te: Fraction
    excess_t: Fraction
    excess_e: Fraction

    def apply(self, readout: ReadoutRatios) -> ReadoutRatios:
        return ReadoutRatios(
            rho_t=readout.rho_t * self.excess_t,
            shell_te=readout.shell_te * self.shell_scale_te,
            rho_e=readout.rho_e * self.excess_e,
        )


def one_power_readout() -> ReadoutRatios:
    one_power_lambda = (W_E / W_T) ** -1
    q_e = TARGET_Q_T * one_power_lambda
    return ReadoutRatios(
        rho_t=TARGET_RHO_T,
        shell_te=TARGET_SHELL_TE,
        rho_e=rho_from_q(q_e),
    )


def normalized_source_target(readout: ReadoutRatios) -> SourceExcessRatios:
    return SourceExcessRatios(
        shell_scale_te=TARGET_SHELL_TE / readout.shell_te,
        excess_t=TARGET_RHO_T / readout.rho_t,
        excess_e=TARGET_RHO_E / readout.rho_e,
    )


def main() -> int:
    print("Route-2 center-excess source target")
    print("Status: bounded-support for the normalized source-map theorem target; not an audit verdict.")
    print("TRACE: upstream_support")

    print("\nPART 1: authority markers")
    readout_path = DOCS / READOUT_NOTE
    schur_path = SCRIPTS / SCHUR_RUNNER
    check(f"readout authority exists: {READOUT_NOTE}", readout_path.is_file())
    check(f"Schur runner authority exists: {SCHUR_RUNNER}", schur_path.is_file())
    readout_text = read(readout_path)
    schur_text = read(schur_path)
    for marker in READOUT_MARKERS:
        check(f"readout note contains marker: {marker}", marker in readout_text)
    for marker in SCHUR_MARKERS:
        check(f"Schur runner contains marker: {marker}", marker in schur_text)

    print("\nPART 2: one-power readout premise")
    one_power = one_power_readout()
    one_power_lambda = (W_E / W_T) ** -1
    square_lambda = (W_E / W_T) ** -2
    check("Schur weights are w_E=1/3 and w_T=1/2", (W_E, W_T) == (Fraction(1, 3), Fraction(1, 2)))
    check("one inverse Schur factor gives lambda=3/2", one_power_lambda == Fraction(3, 2))
    check("two inverse Schur factors give lambda=9/4", square_lambda == Fraction(9, 4))
    check("one-power readout gives q_E=5/4 from q_T=5/6", one_power.q_e == Fraction(5, 4))
    check("one-power readout gives rho_E=3/2", one_power.rho_e == Fraction(3, 2))
    check("one-power readout keeps the granted T-side values", one_power.rho_t == TARGET_RHO_T and one_power.q_t == TARGET_Q_T)

    print("\nPART 3: normalized source-excess target")
    source_target = normalized_source_target(one_power)
    final = source_target.apply(one_power)
    print(
        f"  normalized source target: shell_scale={source_target.shell_scale_te}, "
        f"b_T/a_T={source_target.excess_t}, b_E/a_E={source_target.excess_e}"
    )
    check("preserving shell T/E from -2 forces a_T/a_E=1", source_target.shell_scale_te == 1)
    check("preserving q_T=5/6 from rho_T=-1 forces b_T/a_T=1", source_target.excess_t == 1)
    check("raising one-power rho_E=3/2 to 21/4 forces b_E/a_E=7/2", source_target.excess_e == Fraction(7, 2))
    check("the normalized source target gives final rho_T=-1", final.rho_t == TARGET_RHO_T)
    check("the normalized source target gives final shell T/E=-2", final.shell_te == TARGET_SHELL_TE)
    check("the normalized source target gives final rho_E=21/4", final.rho_e == TARGET_RHO_E)
    check("the normalized source target gives q_T=5/6", final.q_t == TARGET_Q_T)
    check("the normalized source target gives q_E=15/8", final.q_e == TARGET_Q_E)
    check("the normalized source target gives center T/E=-8/9", final.center_te == TARGET_CENTER_TE)

    print("\nPART 4: necessity in the endpoint-normalized class")
    solved_shell = TARGET_SHELL_TE / one_power.shell_te
    solved_t = TARGET_RHO_T / one_power.rho_t
    solved_e = TARGET_RHO_E / one_power.rho_e
    check("solving the shell equation returns a_T/a_E=1", solved_shell == 1)
    check("solving the T-center equation returns b_T/a_T=1", solved_t == 1)
    check("solving the E-center equation returns b_E/a_E=7/2", solved_e == Fraction(7, 2))
    low_rationals = {
        Fraction(n, d)
        for n in range(1, 33)
        for d in range(1, 17)
    }
    hits = [
        x
        for x in sorted(low_rationals)
        if SourceExcessRatios(Fraction(1), Fraction(1), x).apply(one_power).rho_e == TARGET_RHO_E
    ]
    check("low-rational sweep has a unique E-excess hit", hits == [Fraction(7, 2)], f"hits={hits}")
    check(
        "nearby simple tilts miss the target",
        all(
            SourceExcessRatios(Fraction(1), Fraction(1), x).apply(one_power).rho_e != TARGET_RHO_E
            for x in (Fraction(3), Fraction(4), Fraction(5, 2), Fraction(9, 2))
        ),
    )

    print("\nPART 5: note and status firewall")
    note = read(DOCS / "QUARK_ROUTE2_CENTER_EXCESS_SOURCE_TARGET_NOTE_2026-06-21.md")
    required_note_markers = (
        "Actual current-surface status: bounded-support for the normalized center-excess source target",
        "This is not an audit verdict",
        "does not resolve the parent gate",
        "b_E/a_E = 7/2",
        "the exact next source theorem target",
    )
    for marker in required_note_markers:
        check(f"note contains marker: {marker}", marker in note)
    banned_markers = (
        ("status-authority phrase", phrase("Status ", "authority")),
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

    print("\nTOTAL: PASS=%d, FAIL=%d" % (PASS, FAIL))
    if FAIL:
        return 1
    print(
        "VERDICT: bounded support. Under the one-power readout premise, the "
        "endpoint-normalized source theorem target is uniquely b_E/a_E=7/2 "
        "with a_T/a_E=1 and b_T/a_T=1. Existence of that source map remains open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
