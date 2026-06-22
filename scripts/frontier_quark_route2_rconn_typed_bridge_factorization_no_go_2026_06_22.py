#!/usr/bin/env python3
"""Factor the missing Route-2 R_conn typed bridge into exact switches.

The tempting bridge is

    c_TE := gamma_T(center)/gamma_E(center) = -R_conn = -8/9.

The current support bank already has the SU(3) adjoint fraction
F_adj = 8/9 and the Route-2 endpoint algebra.  This runner classifies the
minimal typed bridge ansatz

    c_TE = sigma * R_phys(kappa),
    R_phys(kappa) = F_adj + kappa * (1 - F_adj),

where kappa is the connected/disconnected selector from the R_conn repair and
sigma is the endpoint orientation sign.  The target lands if and only if the
two switches are both supplied:

    kappa = 0 and sigma = -1.

Neither switch is derived by the current bank.  This is not an audit verdict.
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
SHELL_TE = Fraction(-2)
TARGET_CENTER_TE = Fraction(-8, 9)
TARGET_Q_E = Fraction(15, 8)
TARGET_RHO_E = Fraction(21, 4)


@dataclass(frozen=True)
class BridgeSwitches:
    sigma: int
    kappa: Fraction

    @property
    def r_phys(self) -> Fraction:
        return r_phys(self.kappa)

    @property
    def c_te(self) -> Fraction:
        return Fraction(self.sigma) * self.r_phys

    @property
    def q_e(self) -> Fraction:
        return q_e_from_center_ratio(self.c_te)

    @property
    def rho_e(self) -> Fraction:
        return rho_e_from_center_ratio(self.c_te)

    @property
    def lands_target(self) -> bool:
        return self.c_te == TARGET_CENTER_TE and self.rho_e == TARGET_RHO_E


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


def f_adj(n_c: int = 3) -> Fraction:
    return Fraction(n_c * n_c - 1, n_c * n_c)


def r_phys(kappa: Fraction, n_c: int = 3) -> Fraction:
    f = f_adj(n_c)
    return f + kappa * (1 - f)


def q_e_from_center_ratio(c_te: Fraction) -> Fraction:
    return SHELL_TE * Q_T / c_te


def rho_e_from_center_ratio(c_te: Fraction) -> Fraction:
    return 6 * (q_e_from_center_ratio(c_te) - 1)


def solve_kappa_for_target(sigma: int) -> Fraction:
    # sigma * (8/9 + kappa/9) = -8/9
    return 9 * (TARGET_CENTER_TE / Fraction(sigma) - Fraction(8, 9))


def part1_exact_support_and_target() -> None:
    print("PART 1: exact support and target")
    f = f_adj(3)
    check("SU(3) adjoint fraction is 8/9", f == Fraction(8, 9), f"F_adj={f}")
    check("connected selector kappa=0 gives R_phys=8/9", r_phys(Fraction(0)) == Fraction(8, 9))
    check("full selector kappa=1 gives R_phys=1", r_phys(Fraction(1)) == Fraction(1))
    check("half selector kappa=1/2 gives R_phys=17/18", r_phys(Fraction(1, 2)) == Fraction(17, 18))
    check("target center ratio -8/9 gives q_E=15/8", q_e_from_center_ratio(TARGET_CENTER_TE) == TARGET_Q_E)
    check("target center ratio -8/9 gives rho_E=21/4", rho_e_from_center_ratio(TARGET_CENTER_TE) == TARGET_RHO_E)


def part2_two_switch_classifier() -> None:
    print()
    print("PART 2: two-switch bridge classifier")
    cases = (
        BridgeSwitches(-1, Fraction(0)),
        BridgeSwitches(+1, Fraction(0)),
        BridgeSwitches(-1, Fraction(1)),
        BridgeSwitches(+1, Fraction(1)),
        BridgeSwitches(-1, Fraction(1, 2)),
        BridgeSwitches(+1, Fraction(1, 2)),
    )
    for case in cases:
        print(
            f"  sigma={case.sigma:+d}, kappa={case.kappa}: "
            f"R_phys={case.r_phys}, c_TE={case.c_te}, q_E={case.q_e}, rho_E={case.rho_e}"
        )

    landed = [(case.sigma, case.kappa) for case in cases if case.lands_target]
    check("only sigma=-1 with kappa=0 lands in the tested physical selector set", landed == [(-1, Fraction(0))], str(landed))
    check("connected selector alone is insufficient without the negative orientation sign", not BridgeSwitches(+1, Fraction(0)).lands_target)
    check("negative orientation sign alone is insufficient without the connected selector", not BridgeSwitches(-1, Fraction(1)).lands_target)
    check("intermediate disconnected coefficient misses the endpoint", not BridgeSwitches(-1, Fraction(1, 2)).lands_target)
    check("wrong sign sends the connected selector to wrong signed q_E", BridgeSwitches(+1, Fraction(0)).q_e == Fraction(-15, 8))


def part3_exact_solution_over_selector_line() -> None:
    print()
    print("PART 3: exact solution over the selector line")
    kappa_negative_sign = solve_kappa_for_target(-1)
    kappa_positive_sign = solve_kappa_for_target(+1)
    print(f"  sigma=-1 target kappa = {kappa_negative_sign}")
    print(f"  sigma=+1 target kappa = {kappa_positive_sign}")
    check("negative orientation requires kappa=0 exactly", kappa_negative_sign == 0)
    check("positive orientation would require unphysical kappa=-16", kappa_positive_sign == -16)
    check("physical selector interval contains only the negative-orientation solution", Fraction(0) <= kappa_negative_sign <= Fraction(1) and not (Fraction(0) <= kappa_positive_sign <= Fraction(1)))
    check("target bridge is equivalent to the pair (sigma=-1, kappa=0)", BridgeSwitches(-1, kappa_negative_sign).lands_target)


def part4_import_boundary() -> None:
    print()
    print("PART 4: import-boundary split")
    rconn = note_text("RCONN_DERIVED_NOTE.md")
    obstruction = note_text("QUARK_ROUTE2_RCONN_CENTER_RATIO_BRIDGE_OBSTRUCTION_NOTE_2026-04-28.md")
    source = note_text("QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md")
    block66 = note_text("QUARK_ROUTE2_DIRECT_E_CENTER_READOUT_FAMILY_NO_GO_NOTE_2026-06-22.md")
    note = note_text("QUARK_ROUTE2_RCONN_TYPED_BRIDGE_FACTORIZATION_NO_GO_NOTE_2026-06-22.md")

    check("RCONN repair leaves kappa_EW as a selector", "kappa_EW" in rconn and "does not derive\nthe selector `kappa_EW = 0`" in rconn)
    check("bridge obstruction names c_TE=-F_adj as the missing identification", "c_TE = -F_adj = -8/9" in obstruction)
    check("source-domain no-go says no current typed edge supplies the bridge", "There is no current typed edge" in source)
    check("Block66 classifies c_TE=-8/9 as a non-invariant E-center premise", "c_TE = -8/9" in block66 and "non-invariant E-center premise" in block66)

    required = (
        "Claim type:** no_go",
        "Actual current-surface status: no-go for typed R_conn bridge closure",
        "This is not an audit verdict",
        "two independent switches",
        "connected-trace selector `kappa=0`",
        "orientation sign `sigma=-1`",
    )
    for marker in required:
        check(f"new note contains marker: {marker}", marker in note)

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


def part5_next_targets() -> None:
    print()
    print("PART 5: next target split")
    open_switches = {
        "connected_trace_selector": "derive kappa=0 from the R_conn/EW-current packet",
        "endpoint_orientation": "derive sigma=-1 from a typed Route-2 source-domain functor",
    }
    check("Block67 exposes exactly two independent missing bridge switches", set(open_switches) == {"connected_trace_selector", "endpoint_orientation"})
    check("proving both switches would force the endpoint algebra", BridgeSwitches(-1, Fraction(0)).rho_e == TARGET_RHO_E)
    check("proving only one switch leaves a non-target witness", BridgeSwitches(-1, Fraction(1)).rho_e != TARGET_RHO_E and BridgeSwitches(+1, Fraction(0)).rho_e != TARGET_RHO_E)


def main() -> int:
    print("Route-2 R_conn typed-bridge factorization")
    print("Status: no-go for typed R_conn bridge closure; not an audit verdict.")
    print("TRACE: negative_route_pruning")
    part1_exact_support_and_target()
    part2_two_switch_classifier()
    part3_exact_solution_over_selector_line()
    part4_import_boundary()
    part5_next_targets()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: R_conn typed-bridge factorization checks failed.")
        return 1
    print(
        "VERDICT: the bridge c_TE=-R_conn requires two current-surface imports: "
        "connected selector kappa=0 and endpoint orientation sigma=-1."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
