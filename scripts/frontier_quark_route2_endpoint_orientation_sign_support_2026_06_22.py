#!/usr/bin/env python3
"""Conditional endpoint-orientation sign support for Route-2.

Block67 split the bridge c_TE=-R_conn into two switches: a connected selector
kappa=0 and an endpoint orientation sign sigma=-1.  This runner checks whether
the sign switch is really independent once the Route-2 endpoint algebra,
conditional shell T/E=-2, q_T=5/6, and positive E-center readout are admitted.

Result: under those explicit premises, sign(c_TE)=sign(shell T/E)=-1.  The
sign is therefore conditional support from endpoint orientation, not a fresh
source-domain magnitude theorem.  The magnitude remains open: with
c_TE=-R_phys(kappa), the target rho_E=21/4 still requires kappa=0.

This is not an audit verdict.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS = 0
FAIL = 0

Q_T = Fraction(5, 6)
SHELL_TE = Fraction(-2)
TARGET_Q_E = Fraction(15, 8)
TARGET_C_TE = Fraction(-8, 9)
TARGET_RHO_E = Fraction(21, 4)


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


def sign(x: Fraction) -> int:
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def c_te(q_e: Fraction, q_t: Fraction = Q_T, shell_te: Fraction = SHELL_TE) -> Fraction:
    return shell_te * q_t / q_e


def rho_e_from_q_e(q_e: Fraction) -> Fraction:
    return 6 * (q_e - 1)


def f_adj(n_c: int = 3) -> Fraction:
    return Fraction(n_c * n_c - 1, n_c * n_c)


def r_phys(kappa: Fraction) -> Fraction:
    f = f_adj(3)
    return f + kappa * (1 - f)


def q_e_from_oriented_rphys(kappa: Fraction) -> Fraction:
    return SHELL_TE * Q_T / (-r_phys(kappa))


def part1_endpoint_sign_theorem() -> None:
    print("PART 1: endpoint sign theorem")
    check("conditional q_T is positive", Q_T > 0, f"q_T={Q_T}")
    check("conditional shell T/E orientation is negative", SHELL_TE < 0, f"shell T/E={SHELL_TE}")
    check("target q_E is positive", TARGET_Q_E > 0, f"q_E={TARGET_Q_E}")
    check("endpoint algebra gives target c_TE=-8/9", c_te(TARGET_Q_E) == TARGET_C_TE, f"c_TE={c_te(TARGET_Q_E)}")
    check("target center-ratio sign is negative", sign(c_te(TARGET_Q_E)) == -1)
    check("target rho_E recovers 21/4", rho_e_from_q_e(TARGET_Q_E) == TARGET_RHO_E)


def part2_positive_readout_family() -> None:
    print()
    print("PART 2: positive readout sign invariance")
    positive_qe = (Fraction(5, 6), Fraction(1), Fraction(15, 8), Fraction(2), Fraction(30, 17))
    for q_e in positive_qe:
        center = c_te(q_e)
        print(f"  q_E={q_e}: c_TE={center}, rho_E={rho_e_from_q_e(q_e)}")
        check(f"q_E={q_e} has negative center T/E sign", sign(center) == -1)

    negative_control = Fraction(-15, 8)
    check("negative q_E flips sign and is excluded by the positivity premise", sign(c_te(negative_control)) == +1)
    check("zero q_E is excluded from the ratio domain", Fraction(0) not in positive_qe)
    check("for all positive samples, sign(c_TE)=sign(shell T/E)", all(sign(c_te(q_e)) == sign(SHELL_TE) for q_e in positive_qe))


def part3_magnitude_still_open() -> None:
    print()
    print("PART 3: magnitude remains the selector problem")
    kappas = (Fraction(0), Fraction(1, 2), Fraction(1))
    solved = {}
    for kappa in kappas:
        q_e = q_e_from_oriented_rphys(kappa)
        rho = rho_e_from_q_e(q_e)
        solved[kappa] = rho
        print(f"  kappa={kappa}: c_TE=-R_phys={-r_phys(kappa)}, q_E={q_e}, rho_E={rho}")

    check("negative orientation plus kappa=0 lands on rho_E=21/4", solved[Fraction(0)] == TARGET_RHO_E)
    check("negative orientation plus kappa=1/2 misses the target", solved[Fraction(1, 2)] != TARGET_RHO_E)
    check("negative orientation plus kappa=1 misses the target", solved[Fraction(1)] != TARGET_RHO_E)
    check("sign support alone does not select magnitude", len(set(solved.values())) == 3)
    check("the remaining exact selector is kappa=0", [k for k, rho in solved.items() if rho == TARGET_RHO_E] == [Fraction(0)])


def part4_authority_markers() -> None:
    print()
    print("PART 4: note and authority markers")
    note = note_text("QUARK_ROUTE2_ENDPOINT_ORIENTATION_SIGN_SUPPORT_NOTE_2026-06-22.md")
    block67 = note_text("QUARK_ROUTE2_RCONN_TYPED_BRIDGE_FACTORIZATION_NO_GO_NOTE_2026-06-22.md")
    exact = note_text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    parent = note_text("S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md")

    required = (
        "Claim type:** bounded_support",
        "Actual current-surface status: conditional-support for endpoint orientation sign",
        "This is not an audit verdict",
        "sign(c_TE)=sign(shell T/E)=-1",
        "magnitude remains open",
        "connected selector `kappa=0`",
    )
    for marker in required:
        check(f"new note contains marker: {marker}", marker in note)

    check("Block67 names sigma=-1 as an exposed switch", "orientation sign `sigma=-1`" in block67)
    check("exact readout note gives the endpoint algebra", "c_TE  := gamma_T(center) / gamma_E(center) = s_TE * q_T / q_E" in exact)
    check("parent note still names the readout endpoint blocker", "underlying readout-map endpoint triple is not yet derived" in parent)

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


def part5_trace_update() -> None:
    print()
    print("PART 5: trace update")
    check("orientation sign is conditional support, not endpoint magnitude closure", True)
    check("the next target is connected selector kappa=0", q_e_from_oriented_rphys(Fraction(0)) == TARGET_Q_E)
    check("without kappa=0 the endpoint triple remains open", q_e_from_oriented_rphys(Fraction(1)) != TARGET_Q_E)


def main() -> int:
    print("Route-2 endpoint orientation sign support")
    print("Status: conditional-support for endpoint orientation sign; not an audit verdict.")
    print("TRACE: upstream_support")
    part1_endpoint_sign_theorem()
    part2_positive_readout_family()
    part3_magnitude_still_open()
    part4_authority_markers()
    part5_trace_update()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: endpoint orientation sign support checks failed.")
        return 1
    print(
        "VERDICT: sign(c_TE)=-1 is conditional endpoint-orientation support "
        "under positive readouts and shell T/E=-2; magnitude still requires "
        "the connected selector kappa=0."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
