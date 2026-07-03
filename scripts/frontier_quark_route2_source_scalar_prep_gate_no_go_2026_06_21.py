#!/usr/bin/env python3
"""Route-2 channel-scalar source-preparation gate.

This runner tests the first obvious source-preparation candidate left by the
S3/Route-2 endpoint campaign: a channel-scalar source map

    S(a_E,a_T) = diag(a_E, a_T, a_E, a_T)

on the restricted carrier coordinates

    c = (u_E, u_T, delta_A1 u_E, delta_A1 u_T).

Status:
  no-go for channel-scalar source preparation as the missing source-side
  inverse-Schur theorem.

Safe claim:
  A channel-scalar source map rescales E and T shell amplitudes but leaves the
  center/shell ratios q_E and q_T invariant. Therefore it cannot create the
  missing E-center factor beta_E/alpha_E = 21/4 unless that factor is already
  supplied by the readout map. A future source-preparation theorem must be
  center-excess nonuniform, or the readout map must supply an inverse-square
  coefficient law directly.
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
    "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
    "QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md",
    "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md",
    "S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md",
)

REQUIRED_MARKERS = {
    "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md": (
        "E-shell  = (1, 0, 0,   0)",
        "E-center = (1, 0, 1/6, 0)",
        "T-shell  = (0, 1, 0,   0)",
        "T-center = (0, 1, 0, 1/6)",
        "P_R = [[alpha_E, 0, beta_E, 0]",
        "q_E   := gamma_E(center) / gamma_E(shell) = 1 + (beta_E / alpha_E) / 6",
        "beta_E / alpha_E = 21/4",
        "irreducible missing map entry",
    ),
    "QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md": (
        "Given any admissible readout map `P_R`",
        "Xi_P(t ; c) = (P_R c)",
        "lacks is a theorem that selects one unique `P_R`",
    ),
    "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md": (
        "(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E) = (-1, -2, 21/4)",
        "exact conditional readout-to-slice family",
        "The next theorem target is the missing readout-map endpoint triple",
    ),
    "S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md": (
        "`|| (P_R c) ||` factor cancels",
        "right factor `V_R(t)`",
    ),
}

SOURCE_SLOT_ABSENT_MARKERS = (
    "S_dual",
    "source-preparation map",
    "source preparation map",
    "source slot",
    "S_R c",
    "P_R S",
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


def note_text(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


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
class ChannelScalarPrep:
    a_e: Fraction
    a_t: Fraction

    def effective(self, ratios: ReadoutRatios) -> ReadoutRatios:
        return ReadoutRatios(
            rho_t=ratios.rho_t,
            shell_te=ratios.shell_te * self.a_t / self.a_e,
            rho_e=ratios.rho_e,
        )


@dataclass(frozen=True)
class NonuniformPrep:
    a_e: Fraction
    a_t: Fraction
    b_e: Fraction
    b_t: Fraction

    def q_t(self, ratios: ReadoutRatios) -> Fraction:
        return Fraction(1, 1) + ratios.rho_t * (self.b_t / self.a_t) / 6

    def q_e(self, ratios: ReadoutRatios) -> Fraction:
        return Fraction(1, 1) + ratios.rho_e * (self.b_e / self.a_e) / 6

    def shell_te(self, ratios: ReadoutRatios) -> Fraction:
        return ratios.shell_te * self.a_t / self.a_e

    def center_te(self, ratios: ReadoutRatios) -> Fraction:
        return center_te(self.shell_te(ratios), self.q_t(ratios), self.q_e(ratios))


def main() -> int:
    print("Route-2 channel-scalar source-preparation gate")
    print("Status: no-go for channel-scalar source preparation; not an audit verdict.")
    print("TRACE: negative_route_pruning")

    print("\nPART 1: current authority markers")
    for name in AUTHORITY_FILES:
        check(f"authority file exists: {name}", (DOCS / name).is_file())
    for name, markers in REQUIRED_MARKERS.items():
        text = note_text(name)
        for marker in markers:
            check(f"{name} contains marker: {marker}", marker in text)

    bank = "\n".join(note_text(name) for name in AUTHORITY_FILES)
    lower_bank = bank.lower()
    for marker in SOURCE_SLOT_ABSENT_MARKERS:
        check(
            f"current authority bank does not already name source slot: {marker}",
            marker.lower() not in lower_bank,
        )

    print("\nPART 2: endpoint algebra target")
    target = ReadoutRatios(
        rho_t=TARGET_RHO_T,
        shell_te=TARGET_SHELL_TE,
        rho_e=TARGET_RHO_E,
    )
    check("rho_T=-1 gives q_T=5/6", target.q_t == TARGET_Q_T)
    check("rho_E=21/4 gives q_E=15/8", target.q_e == TARGET_Q_E)
    check("target shell and center ratios give center T/E=-8/9", target.center_te == TARGET_CENTER_TE)
    check("rho_E=21/4 is equivalent to q_E=15/8", rho_from_q(TARGET_Q_E) == TARGET_RHO_E)
    check("inverse Schur square ratio is (w_E/w_T)^-2 = 9/4", (W_E / W_T) ** -2 == Fraction(9, 4))

    print("\nPART 3: channel-scalar source-preparation invariance")
    base = ReadoutRatios(
        rho_t=TARGET_RHO_T,
        shell_te=TARGET_SHELL_TE,
        rho_e=Fraction(3, 2),
    )
    source_cases = (
        ChannelScalarPrep(Fraction(1), Fraction(1)),
        ChannelScalarPrep(Fraction(3), Fraction(2)),
        ChannelScalarPrep(Fraction(7), Fraction(5)),
        ChannelScalarPrep(Fraction(5), Fraction(7)),
    )
    for prep in source_cases:
        eff = prep.effective(base)
        print(
            f"  S=diag({prep.a_e},{prep.a_t},{prep.a_e},{prep.a_t}): "
            f"rho_E'={eff.rho_e}, rho_T'={eff.rho_t}, "
            f"shell T/E'={eff.shell_te}, q_E'={eff.q_e}, q_T'={eff.q_t}"
        )
        check(
            f"channel scalar {prep.a_e},{prep.a_t} leaves q_E invariant",
            eff.q_e == base.q_e,
            f"q_E={base.q_e}",
        )
        check(
            f"channel scalar {prep.a_e},{prep.a_t} leaves q_T invariant",
            eff.q_t == base.q_t,
            f"q_T={base.q_t}",
        )
        check(
            f"channel scalar {prep.a_e},{prep.a_t} changes only shell T/E by a_T/a_E",
            eff.shell_te == base.shell_te * prep.a_t / prep.a_e,
        )

    canonical_source = ChannelScalarPrep(Fraction(1, W_E), Fraction(1, W_T))
    canonical_eff = canonical_source.effective(base)
    check(
        "canonical inverse Schur channel source keeps rho_E at the readout value",
        canonical_eff.rho_e == Fraction(3, 2),
        "rho_E remains 3/2, not 21/4",
    )
    check(
        "canonical inverse Schur channel source changes shell T/E from -2 to -4/3",
        canonical_eff.shell_te == Fraction(-4, 3),
    )
    check(
        "no channel scalar can turn readout-only rho_E=3/2 into rho_E=21/4",
        all(prep.effective(base).rho_e != TARGET_RHO_E for prep in source_cases),
    )

    print("\nPART 4: center-excess nonuniform condition")
    nonuniform_identity = NonuniformPrep(Fraction(1), Fraction(1), Fraction(1), Fraction(1))
    check("identity nonuniform prep reproduces base q_E", nonuniform_identity.q_e(base) == base.q_e)
    check("identity nonuniform prep reproduces base q_T", nonuniform_identity.q_t(base) == base.q_t)
    check(
        "keeping q_T=5/6 with rho_T=-1 forces b_T/a_T=1",
        NonuniformPrep(Fraction(1), Fraction(1), Fraction(1), Fraction(1)).q_t(base) == TARGET_Q_T
        and NonuniformPrep(Fraction(1), Fraction(1), Fraction(1), Fraction(2)).q_t(base) != TARGET_Q_T,
    )
    required_be_over_ae_from_base = TARGET_RHO_E / base.rho_e
    witness = NonuniformPrep(Fraction(1), Fraction(1), required_be_over_ae_from_base, Fraction(1))
    check(
        "hitting q_E=15/8 from readout-only rho_E=3/2 requires b_E/a_E=7/2",
        required_be_over_ae_from_base == Fraction(7, 2) and witness.q_e(base) == TARGET_Q_E,
    )
    check(
        "the nonuniform condition is rho_E*(b_E/a_E)=21/4",
        base.rho_e * required_be_over_ae_from_base == TARGET_RHO_E,
    )
    target_readout = ReadoutRatios(TARGET_RHO_T, TARGET_SHELL_TE, TARGET_RHO_E)
    target_identity = nonuniform_identity
    check(
        "if the readout map already has rho_E=21/4, no source excess tilt is needed",
        target_identity.q_e(target_readout) == TARGET_Q_E,
    )

    print("\nPART 5: note and status firewall")
    note = note_text("QUARK_ROUTE2_SOURCE_SCALAR_PREP_GATE_NO_GO_NOTE_2026-06-21.md")
    required_note_markers = (
        "**Actual current-surface status:** no-go for channel-scalar source-preparation shortcut",
        "This is not an audit verdict",
        "does not resolve the parent gate",
        "S(a_E,a_T) = diag(a_E, a_T, a_E, a_T)",
        "leaves q_E and q_T unchanged",
        "rho_E * (b_E/a_E) = 21/4",
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

    print("\nTOTAL: PASS=%d, FAIL=%d" % (PASS, FAIL))
    if FAIL:
        return 1
    print(
        "VERDICT: channel-scalar source preparation cannot supply the missing "
        "Route-2 endpoint factor. A source-side theorem must be center-excess "
        "nonuniform, or the readout map must supply the inverse-square law."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
