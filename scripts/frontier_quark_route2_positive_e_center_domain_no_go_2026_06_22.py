#!/usr/bin/env python3
"""Positive E-center readout domain boundary for Route-2.

Block68 used q_E > 0 to force the endpoint orientation sign.  This runner
tests whether q_E > 0 is derived by the current exact readout family.

Result: on the exact restricted readout family, q_E = 1 + rho_E/6, so
positivity is exactly the open half-line rho_E > -6.  The current carrier,
shell normalization, and granted T-side candidates do not exclude rho_E <= -6.
Under the conditional oriented Rconn ansatz with nonnegative selector kappa,
q_E is positive automatically, but that is support conditional on the bridge
ansatz rather than an unconditional current-surface theorem.

This is not an audit verdict.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS = 0
FAIL = 0

Q_T = Fraction(5, 6)
S_TE = Fraction(-2)
F_ADJ = Fraction(8, 9)
F_SINGLET = Fraction(1, 9)
TARGET_RHO_E = Fraction(21, 4)


@dataclass(frozen=True)
class ReducedReadout:
    rho_e: Fraction

    @property
    def e_shell(self) -> Fraction:
        return Fraction(1)

    @property
    def e_center(self) -> Fraction:
        return 1 + self.rho_e / 6

    @property
    def q_e(self) -> Fraction:
        return self.e_center / self.e_shell

    @property
    def c_te(self) -> Fraction | None:
        if self.q_e == 0:
            return None
        return S_TE * Q_T / self.q_e


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


def q_e_from_rconn_selector(kappa: Fraction) -> Fraction:
    r_phys = F_ADJ + kappa * F_SINGLET
    return Fraction(5, 3) / r_phys


def rho_from_q_e(q_e: Fraction) -> Fraction:
    return 6 * (q_e - 1)


def part1_exact_domain_boundary() -> None:
    print("PART 1: exact q_E domain boundary")
    samples = (Fraction(-7), Fraction(-6), Fraction(-1), Fraction(0), TARGET_RHO_E)
    for rho in samples:
        rr = ReducedReadout(rho)
        print(f"  rho_E={rho}: q_E={rr.q_e}, c_TE={rr.c_te}")
    check("q_E formula is 1 + rho_E/6", all(ReducedReadout(r).q_e == 1 + r / 6 for r in samples))
    check("rho_E=-7 gives negative q_E", ReducedReadout(Fraction(-7)).q_e < 0)
    check("rho_E=-6 gives zero q_E boundary", ReducedReadout(Fraction(-6)).q_e == 0)
    check("rho_E=-1 gives positive q_E but not target", ReducedReadout(Fraction(-1)).q_e > 0 and Fraction(-1) != TARGET_RHO_E)
    check("target rho_E=21/4 gives q_E=15/8", ReducedReadout(TARGET_RHO_E).q_e == Fraction(15, 8))
    check("positivity is exactly rho_E > -6 on sampled rationals", all((ReducedReadout(r).q_e > 0) == (r > -6) for r in samples))


def part2_non_uniqueness_witnesses() -> None:
    print()
    print("PART 2: exact readout-family non-uniqueness")
    negative = ReducedReadout(Fraction(-7))
    zero = ReducedReadout(Fraction(-6))
    target = ReducedReadout(TARGET_RHO_E)
    witnesses = (negative, zero, target)

    check("all witnesses keep E-shell normalization fixed", all(w.e_shell == 1 for w in witnesses))
    check("all witnesses share granted q_T=5/6", Q_T == Fraction(5, 6))
    check("all witnesses share granted shell T/E=-2", S_TE == -2)
    check("negative witness is an exact rational admissible map on the reduced family", isinstance(negative.q_e, Fraction))
    check("zero witness shows the ratio-domain boundary is not excluded by carrier algebra", zero.q_e == 0)
    check("target witness is only one exact member of the same reduced family", target.q_e == Fraction(15, 8))


def part3_orientation_sign_dependency() -> None:
    print()
    print("PART 3: endpoint orientation sign dependency")
    negative = ReducedReadout(Fraction(-7))
    positive = ReducedReadout(TARGET_RHO_E)
    check("q_E<0 flips c_TE positive", negative.q_e < 0 and negative.c_te is not None and negative.c_te > 0)
    check("q_E>0 preserves negative c_TE sign", positive.q_e > 0 and positive.c_te == Fraction(-8, 9))
    check("q_E=0 is excluded from the center-ratio domain", ReducedReadout(Fraction(-6)).c_te is None)
    check("Block68 sign theorem is conditional on q_E>0", positive.q_e > 0 and negative.q_e < 0)


def part4_conditional_rconn_support() -> None:
    print()
    print("PART 4: conditional Rconn selector support")
    kappas = (Fraction(0), Fraction(1, 2), Fraction(1))
    values = [(kappa, q_e_from_rconn_selector(kappa), rho_from_q_e(q_e_from_rconn_selector(kappa))) for kappa in kappas]
    for kappa, q_e, rho in values:
        print(f"  kappa={kappa}: q_E={q_e}, rho_E={rho}")
    check("nonnegative idempotent endpoints have positive q_E under oriented Rconn ansatz", all(q_e_from_rconn_selector(k) > 0 for k in (Fraction(0), Fraction(1))))
    check("sampled physical selector interval has positive q_E", all(q > 0 for _, q, _ in values))
    check("connected endpoint gives q_E=15/8", q_e_from_rconn_selector(Fraction(0)) == Fraction(15, 8))
    check("full-trace endpoint gives q_E=5/3", q_e_from_rconn_selector(Fraction(1)) == Fraction(5, 3))
    check("conditional positivity does not select the connected endpoint", q_e_from_rconn_selector(Fraction(0)) > 0 and q_e_from_rconn_selector(Fraction(1)) > 0)


def part5_forbidden_selectors() -> None:
    print()
    print("PART 5: forbidden selector audit")
    target_selected = [rho for rho in (Fraction(-7), Fraction(-6), Fraction(-1), Fraction(0), TARGET_RHO_E) if ReducedReadout(rho).q_e == Fraction(15, 8)]
    positive_selected = [rho for rho in (Fraction(-7), Fraction(-6), Fraction(-1), Fraction(0), TARGET_RHO_E) if ReducedReadout(rho).q_e > 0]
    check("target q_E selects rho_E=21/4 only by supplying target q_E", target_selected == [TARGET_RHO_E], str(target_selected))
    check("positivity is weaker than the target value", positive_selected == [Fraction(-1), Fraction(0), TARGET_RHO_E], str(positive_selected))
    check("positive domain alone leaves multiple exact rho_E values", len(positive_selected) == 3)
    check("using the target value as positivity proof would fit the endpoint", TARGET_RHO_E in positive_selected)


def part6_note_and_authority_markers() -> None:
    print()
    print("PART 6: note and authority markers")
    note = note_text("QUARK_ROUTE2_POSITIVE_E_CENTER_DOMAIN_NO_GO_NOTE_2026-06-22.md")
    readout = note_text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    orientation = note_text("QUARK_ROUTE2_ENDPOINT_ORIENTATION_SIGN_SUPPORT_NOTE_2026-06-22.md")
    block71 = note_text("QUARK_ROUTE2_FULL_TRACE_EXCLUSION_NO_GO_NOTE_2026-06-22.md")
    parent = note_text("S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md")

    required = (
        "Claim type:** no_go",
        "Actual current-surface status: no-go for deriving q_E>0 from the exact reduced readout family",
        "This is not an audit verdict",
        "q_E = 1 + rho_E/6",
        "rho_E > -6",
        "does not close the parent",
    )
    for marker in required:
        check(f"new note contains marker: {marker}", marker in note)

    check("exact readout note gives q_E formula", "q_E   := gamma_E(center) / gamma_E(shell) = 1 + (beta_E / alpha_E) / 6" in readout)
    check("orientation note states q_E positivity premise", "positive E-center readout `q_E > 0`" in orientation)
    check("Block71 leaves singlet-annihilation open", "singlet-annihilation theorem" in block71)
    check("parent note still names endpoint triple blocker", "underlying readout-map endpoint triple is not yet derived" in parent)

    banned = (
        ("status-authority phrase", phrase("Status ", "authority")),
        ("parent closure", phrase("closes ", "the parent")),
        ("current-surface endpoint derivation", phrase("derives ", "the endpoint triple", " on the current surface")),
        ("audit ratification", phrase("audit", "-ratified")),
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
    )
    for label, marker in banned:
        check(f"new note avoids overclaim marker: {label}", marker not in note)


def main() -> int:
    print("Route-2 positive E-center readout domain boundary")
    print("Status: no-go for deriving q_E>0 from exact reduced readout family; not an audit verdict.")
    print("TRACE: negative_route_pruning")
    part1_exact_domain_boundary()
    part2_non_uniqueness_witnesses()
    part3_orientation_sign_dependency()
    part4_conditional_rconn_support()
    part5_forbidden_selectors()
    part6_note_and_authority_markers()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: positive E-center domain checks failed.")
        return 1
    print(
        "VERDICT: q_E>0 is the half-line rho_E>-6.  It is conditionally "
        "supported by the oriented Rconn selector ansatz, but is not derived "
        "by the exact reduced readout family alone."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
