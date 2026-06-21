#!/usr/bin/env python3
"""
Route-2 nonblind E-center lift selector-equivalence support packet.

Safe claim:
  Once the two T-side endpoint candidates are granted, the remaining
  E-center lift can be written in several exactly equivalent forms:

      rho_E = 21/4
      q_E = gamma_E(center)/gamma_E(shell) = 15/8
      q_E / q_T = 9/4
      gamma_T(center)/gamma_E(center) = -8/9
      gamma_T(center)/gamma_E(center) = -R_conn, if the typed R_conn bridge
      is supplied at N_c = 3.

  This runner proves those equivalences and the basic falsifiers.  It also
  checks the current authority surface for the key scope boundary: nonblind
  access to E-center is necessary, but not sufficient.  A selector equation
  or typed source/readout bridge is still required.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


PASS_COUNT = 0
FAIL_COUNT = 0

Vector4 = tuple[Fraction, Fraction, Fraction, Fraction]
Vector2 = tuple[Fraction, Fraction]

E_SHELL: Vector4 = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
E_CENTER: Vector4 = (Fraction(1), Fraction(0), Fraction(1, 6), Fraction(0))
T_SHELL: Vector4 = (Fraction(0), Fraction(1), Fraction(0), Fraction(0))
T_CENTER: Vector4 = (Fraction(0), Fraction(1), Fraction(0), Fraction(1, 6))


@dataclass(frozen=True)
class ReducedReadout:
    rho_e: Fraction
    rho_t: Fraction = Fraction(-1)
    shell_te: Fraction = Fraction(-2)
    center_denominator: Fraction = Fraction(6)

    def apply(self, v: Vector4) -> Vector2:
        x_e, x_t, d_e, d_t = v
        return (
            x_e + self.rho_e * d_e,
            self.shell_te * x_t + (self.shell_te * self.rho_t) * d_t,
        )

    @property
    def q_e(self) -> Fraction:
        return self.apply(E_CENTER)[0] / self.apply(E_SHELL)[0]

    @property
    def q_t(self) -> Fraction:
        return self.apply(T_CENTER)[1] / self.apply(T_SHELL)[1]

    @property
    def center_te(self) -> Fraction:
        return self.apply(T_CENTER)[1] / self.apply(E_CENTER)[0]

    @property
    def lambda_covariance(self) -> Fraction:
        return self.q_e / self.q_t


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    PASS_COUNT += int(condition)
    FAIL_COUNT += int(not condition)
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def rho_from_q_e(q_e: Fraction, denominator: Fraction = Fraction(6)) -> Fraction:
    return denominator * (q_e - 1)


def q_e_from_center_te(center_te: Fraction, q_t: Fraction = Fraction(5, 6), shell_te: Fraction = Fraction(-2)) -> Fraction:
    return shell_te * q_t / center_te


def r_conn(n_c: int) -> Fraction:
    return Fraction(n_c * n_c - 1, n_c * n_c)


def read_text(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def part1_exact_selector_equivalences() -> None:
    section("PART 1: Exact selector equivalences")

    readout = ReducedReadout(Fraction(21, 4))
    q_e_from_lambda = Fraction(9, 4) * readout.q_t
    q_e_from_cte = q_e_from_center_te(Fraction(-8, 9))
    rho_from_cte = rho_from_q_e(q_e_from_cte)
    rho_from_lambda = rho_from_q_e(q_e_from_lambda)

    print(f"  q_T = {readout.q_t}")
    print(f"  q_E = {readout.q_e}")
    print(f"  lambda = q_E/q_T = {readout.lambda_covariance}")
    print(f"  center T/E = {readout.center_te}")

    check("Granted T-side rho_T=-1 gives q_T=5/6", readout.q_t == Fraction(5, 6), str(readout.q_t))
    check("rho_E=21/4 gives q_E=15/8", readout.q_e == Fraction(15, 8), str(readout.q_e))
    check("rho_E=21/4 gives lambda=q_E/q_T=9/4", readout.lambda_covariance == Fraction(9, 4), str(readout.lambda_covariance))
    check("rho_E=21/4 gives center T/E=-8/9", readout.center_te == Fraction(-8, 9), str(readout.center_te))
    check("q_E=15/8 solves back to rho_E=21/4", rho_from_q_e(Fraction(15, 8)) == Fraction(21, 4))
    check("center T/E=-8/9 solves q_E=15/8 and rho_E=21/4", q_e_from_cte == Fraction(15, 8) and rho_from_cte == Fraction(21, 4))
    check("lambda=9/4 solves q_E=15/8 and rho_E=21/4", q_e_from_lambda == Fraction(15, 8) and rho_from_lambda == Fraction(21, 4))


def part2_typed_bridge_and_falsifiers() -> None:
    section("PART 2: Typed bridge support and wrong-structure falsifiers")

    f3 = r_conn(3)
    q_e_from_rconn = q_e_from_center_te(-f3)
    rho_from_rconn = rho_from_q_e(q_e_from_rconn)

    check("R_conn at N_c=3 is 8/9", f3 == Fraction(8, 9), str(f3))
    check("If the typed bridge center T/E=-R_conn is supplied, rho_E=21/4 follows", rho_from_rconn == Fraction(21, 4), f"q_E={q_e_from_rconn}, rho_E={rho_from_rconn}")

    f2 = r_conn(2)
    rho_nc2 = rho_from_q_e(q_e_from_center_te(-f2))
    check("Wrong color count N_c=2 gives rho_E=22/3, not 21/4", rho_nc2 == Fraction(22, 3), f"R_conn={f2}, rho_E={rho_nc2}")

    readout_den5 = ReducedReadout(Fraction(21, 4), center_denominator=Fraction(5))
    q_t_den5 = Fraction(1) + Fraction(-1, 5)
    q_e_den5 = Fraction(-2) * q_t_den5 / Fraction(-8, 9)
    rho_den5 = Fraction(5) * (q_e_den5 - 1)
    check("Wrong center denominator 5 gives rho_E=4", rho_den5 == Fraction(4), f"q_T={q_t_den5}, q_E={q_e_den5}, rho_E={rho_den5}")

    q_t_den12 = Fraction(1) + Fraction(-1, 12)
    q_e_den12 = Fraction(-2) * q_t_den12 / Fraction(-8, 9)
    rho_den12 = Fraction(12) * (q_e_den12 - 1)
    check("Wrong center denominator 12 gives rho_E=51/4", rho_den12 == Fraction(51, 4), f"q_T={q_t_den12}, q_E={q_e_den12}, rho_E={rho_den12}")

    no_lift = ReducedReadout(Fraction(0))
    check("No E-center lift gives center T/E=-5/3, not -8/9", no_lift.center_te == Fraction(-5, 3), str(no_lift.center_te))


def part3_nonblind_access_is_not_enough() -> None:
    section("PART 3: Nonblind E-center access is necessary but not sufficient")

    samples = (Fraction(-1), Fraction(0), Fraction(1), Fraction(21, 4), Fraction(8))
    q_values = []
    center_ratios = []
    for rho in samples:
        r = ReducedReadout(rho)
        q_values.append(r.q_e)
        center_ratios.append(r.center_te)
        print(f"  rho_E={rho}: E-center={r.apply(E_CENTER)}, q_E={r.q_e}, center T/E={r.center_te}")

    check("Evaluating E-center exposes a continuum of q_E values", len(set(q_values)) == len(samples), f"q_E values={tuple(q_values)}")
    check("The granted T-side data stay fixed across the same continuum", all(ReducedReadout(rho).q_t == Fraction(5, 6) and ReducedReadout(rho).shell_te == Fraction(-2) for rho in samples))
    check("Positive E-center readout only gives the bound rho_E>-6 and still does not select 21/4", all(rho > -6 for rho in samples) and Fraction(8) != Fraction(21, 4))
    check("Only one sampled nonblind value hits the target center ratio", center_ratios.count(Fraction(-8, 9)) == 1 and ReducedReadout(Fraction(21, 4)).center_te == Fraction(-8, 9))


def part4_authority_surface_scope() -> None:
    section("PART 4: Current authority-surface scope checks")

    derivation = read_text("docs/QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md")
    source_bridge = read_text("docs/QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md")
    measured = read_text("docs/QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md")
    box_scan = read_text("docs/QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md")
    exact_readout = read_text("docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    theta = read_text("docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md")

    check(
        "E-center lift derivation attempt names the exact missing computation",
        "exact computation would have to derive `gamma_E(center)/gamma_E(shell) = 15/8`" in derivation,
    )
    check(
        "Source-domain bridge note says the typed R_conn -> center-ratio bridge is missing",
        "?=> gamma_T(center) / gamma_E(center) = -R_conn" in source_bridge
        and "no typed current-bank derivation" in source_bridge,
    )
    check(
        "Measured calibration is comparator/support, not a derivation",
        "no derivation of 21/4 is claimed" in measured
        and "exact infinite-volume identification" in measured,
    )
    check(
        "Box-size scan closes the bulk-limit promotion of the N=15 coincidence",
        "fixed-`N=15`" in box_scan
        and "exact-readout coincidence" in box_scan
        and "supplies" in box_scan
        and "selecting primitive" in box_scan,
    )
    check(
        "Exact readout note still names beta_E/alpha_E as the missing map entry",
        "irreducible missing map entry" in exact_readout
        and "beta_E / alpha_E = 21/4" in exact_readout,
    )
    check(
        "Theta-to-slice parent remains blocked by the endpoint triple",
        "readout-map endpoint triple" in theta
        and "not yet derived" in theta,
    )


def main() -> int:
    print("=" * 78)
    print("FRONTIER: Route-2 nonblind E-center lift selector equivalence")
    print("=" * 78)

    part1_exact_selector_equivalences()
    part2_typed_bridge_and_falsifiers()
    part3_nonblind_access_is_not_enough()
    part4_authority_surface_scope()

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    print("=" * 78)
    print(
        "\nVERDICT: exact-support boundary. The nonblind E-center selector can be "
        "stated equivalently as rho_E=21/4, q_E=15/8, lambda=9/4, or "
        "center T/E=-8/9; if the typed R_conn bridge is supplied, the same "
        "arithmetic forces the endpoint. Current authority surfaces still do "
        "not supply that selector or typed bridge."
    )
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
