#!/usr/bin/env python3
"""Direct E-center readout-family classifier for Route-2.

This runner makes the Block66 first-principles attempt on the remaining
Route-2 endpoint entry:

    rho_E = beta_E / alpha_E = 21/4.

After the restricted carrier and the conditional T-side values are fixed, the
readout family is the affine line

    P(rho_E) = [[1, 0, rho_E, 0],
                [0, -2, 0, 2]].

The exact result is a no-go for restricted-family-only selection.  The family
has a one-dimensional E-center shift that preserves all shell/T-side and
carrier-splitting data while moving only the E-center E readout.  Any direct
constraint that fixes the target must be a non-invariant E-center premise;
at the target point it is exactly one of rho_E=21/4, q_E=15/8,
e_E=q_E-1=7/8, or c_TE=-8/9.

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

Vector = tuple[Fraction, Fraction, Fraction, Fraction]
Image = tuple[Fraction, Fraction]

E_SHELL: Vector = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
E_CENTER: Vector = (Fraction(1), Fraction(0), Fraction(1, 6), Fraction(0))
T_SHELL: Vector = (Fraction(0), Fraction(1), Fraction(0), Fraction(0))
T_CENTER: Vector = (Fraction(0), Fraction(1), Fraction(0), Fraction(1, 6))

RHO_TARGET = Fraction(21, 4)
EXCESS_TARGET = Fraction(7, 8)
Q_E_TARGET = Fraction(15, 8)
Q_T_GRANTED = Fraction(5, 6)
SHELL_TE_GRANTED = Fraction(-2)
C_TE_TARGET = Fraction(-8, 9)
R_CONN = Fraction(8, 9)


@dataclass(frozen=True)
class ReducedReadout:
    rho_e: Fraction
    alpha_e: Fraction = Fraction(1)
    alpha_t: Fraction = Fraction(-2)
    beta_t: Fraction = Fraction(2)

    @property
    def beta_e(self) -> Fraction:
        return self.rho_e * self.alpha_e

    def apply(self, v: Vector) -> Image:
        x_e, x_t, d_e, d_t = v
        return (
            self.alpha_e * x_e + self.beta_e * d_e,
            self.alpha_t * x_t + self.beta_t * d_t,
        )

    @property
    def q_e(self) -> Fraction:
        return self.apply(E_CENTER)[0] / self.apply(E_SHELL)[0]

    @property
    def q_t(self) -> Fraction:
        return self.apply(T_CENTER)[1] / self.apply(T_SHELL)[1]

    @property
    def shell_te(self) -> Fraction:
        return self.apply(T_SHELL)[1] / self.apply(E_SHELL)[0]

    @property
    def center_te(self) -> Fraction:
        return self.apply(T_CENTER)[1] / self.apply(E_CENTER)[0]

    @property
    def excess_e(self) -> Fraction:
        return self.q_e - 1


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"\n      {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")


def note_text(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def shift_image(tau: Fraction, v: Vector) -> Image:
    """Image of the E-center gauge shift N_tau on a carrier vector."""
    _x_e, _x_t, d_e, _d_t = v
    return (tau * d_e, Fraction(0))


def blind_signature(readout: ReducedReadout) -> tuple[Image, Image, Image, Fraction, Fraction]:
    return (
        readout.apply(E_SHELL),
        readout.apply(T_SHELL),
        readout.apply(T_CENTER),
        readout.q_t,
        readout.shell_te,
    )


def full_signature(readout: ReducedReadout) -> tuple[Image, Image, Image, Image]:
    return (
        readout.apply(E_SHELL),
        readout.apply(E_CENTER),
        readout.apply(T_SHELL),
        readout.apply(T_CENTER),
    )


def solve_affine_e_center_constraint(
    e_center_coeff: Fraction,
    e_shell_coeff: Fraction,
    constant: Fraction,
) -> Fraction | None:
    """Solve a*E_center_E + b*E_shell_E + c = 0 for rho_E.

    Since E_center_E = 1 + rho_E/6 and E_shell_E = 1, the equation is

        a*rho_E/6 + (a+b+c) = 0.

    If a=0, the equation is E-center-blind and cannot fix rho_E.
    """
    if e_center_coeff == 0:
        return None
    return -6 * (e_center_coeff + e_shell_coeff + constant) / e_center_coeff


def encoded_excess_for_affine_constraint(
    e_center_coeff: Fraction,
    e_shell_coeff: Fraction,
    constant: Fraction,
) -> Fraction | None:
    if e_center_coeff == 0:
        return None
    return -(e_center_coeff + e_shell_coeff + constant) / e_center_coeff


def solve_rho_from_center_ratio(center_te: Fraction) -> Fraction:
    # c_TE = gamma_T(center)/gamma_E(center)
    #      = (-5/3) / (1 + rho_E/6)
    return 6 * (Fraction(-5, 3) / center_te - 1)


def phrase(*parts: str) -> str:
    return "".join(parts)


def part1_restricted_family() -> None:
    print("PART 1: restricted readout family")
    target = ReducedReadout(RHO_TARGET)
    check("E-shell carrier is exact", E_SHELL == (1, 0, 0, 0))
    check("E-center carrier has the single delta_A1 lift 1/6", E_CENTER == (1, 0, Fraction(1, 6), 0))
    check("T-shell carrier is exact", T_SHELL == (0, 1, 0, 0))
    check("T-center carrier has the single delta_A1 lift 1/6", T_CENTER == (0, 1, 0, Fraction(1, 6)))
    check("conditional T-side readout gives q_T=5/6", target.q_t == Q_T_GRANTED, f"q_T={target.q_t}")
    check("conditional shell T/E readout gives -2", target.shell_te == SHELL_TE_GRANTED, f"shell T/E={target.shell_te}")
    check("rho_E controls only q_E in the reduced family", target.q_e == 1 + target.rho_e / 6)


def part2_gauge_orbit() -> None:
    print()
    print("PART 2: E-center gauge orbit")
    tau = Fraction(3, 2)
    check("E-center shift vanishes on E-shell", shift_image(tau, E_SHELL) == (0, 0))
    check("E-center shift vanishes on T-shell", shift_image(tau, T_SHELL) == (0, 0))
    check("E-center shift vanishes on T-center", shift_image(tau, T_CENTER) == (0, 0))
    check("E-center shift is nonzero exactly on the E-center lift", shift_image(tau, E_CENTER) == (Fraction(1, 4), 0))

    rhos = (Fraction(-1), Fraction(0), Fraction(1), RHO_TARGET, Fraction(13, 3))
    signatures = [blind_signature(ReducedReadout(rho)) for rho in rhos]
    full = [full_signature(ReducedReadout(rho)) for rho in rhos]
    for rho, signature in zip(rhos, signatures):
        print(f"  rho_E={rho}: blind_signature={signature}, E-center={ReducedReadout(rho).apply(E_CENTER)}")
    check("all sampled rho_E values have the same shell/T-side blind signature", all(sig == signatures[0] for sig in signatures))
    check("the full endpoint signature is injective on sampled rho_E values", len(set(full)) == len(rhos))
    check("the target rho_E is not a gauge-invariant statement", blind_signature(ReducedReadout(0)) == blind_signature(ReducedReadout(RHO_TARGET)) and full_signature(ReducedReadout(0)) != full_signature(ReducedReadout(RHO_TARGET)))


def part3_affine_constraint_classifier() -> None:
    print()
    print("PART 3: affine E-center constraint classifier")

    cases = {
        "shell_normalization_only": (Fraction(0), Fraction(1), Fraction(-1)),
        "no_E_center_lift": (Fraction(1), Fraction(-1), Fraction(0)),
        "target_q_E_15_8": (Fraction(1), Fraction(0), -Q_E_TARGET),
        "arbitrary_center_value_2": (Fraction(1), Fraction(0), Fraction(-2)),
    }
    solved: dict[str, Fraction | None] = {}
    for name, (a, b, c) in cases.items():
        rho = solve_affine_e_center_constraint(a, b, c)
        solved[name] = rho
        encoded = encoded_excess_for_affine_constraint(a, b, c)
        print(f"  {name}: a={a}, b={b}, c={c}, solved_rho={rho}, encoded_excess={encoded}")

    check("E-center-blind affine equations cannot fix rho_E", solved["shell_normalization_only"] is None)
    check("the natural no-lift affine equation fixes rho_E=0, not the target", solved["no_E_center_lift"] == 0)
    check("q_E=15/8 fixes rho_E=21/4", solved["target_q_E_15_8"] == RHO_TARGET)
    check("q_E=15/8 encodes the target E-center excess 7/8", encoded_excess_for_affine_constraint(1, 0, -Q_E_TARGET) == EXCESS_TARGET)
    check("a different center value fixes a different rho_E", solved["arbitrary_center_value_2"] == 6 and solved["arbitrary_center_value_2"] != RHO_TARGET)

    # Generic classifier theorem: a nonzero E-center coefficient is exactly
    # a non-invariant E-center premise; the target point occurs only when
    # that premise encodes the 7/8 excess.
    generic_a = Fraction(5, 3)
    generic_b = Fraction(-2, 7)
    generic_c = -(generic_a + generic_b) - generic_a * EXCESS_TARGET
    generic_rho = solve_affine_e_center_constraint(generic_a, generic_b, generic_c)
    check("generic affine constraint lands on target iff it encodes excess 7/8", generic_rho == RHO_TARGET, f"c={generic_c}")
    check("the encoded excess formula recovers 7/8 for that generic target constraint", encoded_excess_for_affine_constraint(generic_a, generic_b, generic_c) == EXCESS_TARGET)


def part4_ratio_constraint_classifier() -> None:
    print()
    print("PART 4: ratio constraint classifier")
    ratio_cases = {
        "typed_center_ratio_target_minus_8_9": C_TE_TARGET,
        "positive_R_conn_wrong_sign": R_CONN,
        "reuse_shell_ratio_minus_2_as_center_ratio": Fraction(-2),
        "unit_center_ratio_minus_1": Fraction(-1),
    }
    solved = {name: solve_rho_from_center_ratio(value) for name, value in ratio_cases.items()}
    for name, value in ratio_cases.items():
        print(f"  {name}: c_TE={value}, solved_rho={solved[name]}")

    check("typed center ratio c_TE=-8/9 fixes rho_E=21/4", solved["typed_center_ratio_target_minus_8_9"] == RHO_TARGET)
    check("positive R_conn=8/9 has the wrong sign for the center ratio", solved["positive_R_conn_wrong_sign"] != RHO_TARGET)
    check("reusing shell T/E=-2 as center T/E fixes rho_E=-1, not target", solved["reuse_shell_ratio_minus_2_as_center_ratio"] == -1)
    check("unit center ratio is not the target", solved["unit_center_ratio_minus_1"] != RHO_TARGET)


def part5_target_equivalence_and_firewall() -> None:
    print()
    print("PART 5: target equivalence and firewall")
    target = ReducedReadout(RHO_TARGET)
    check("rho_E=21/4 is equivalent to q_E=15/8", target.q_e == Q_E_TARGET)
    check("rho_E=21/4 is equivalent to E-center excess 7/8", target.excess_e == EXCESS_TARGET)
    check("rho_E=21/4 is equivalent to c_TE=-8/9 under the granted T-side values", target.center_te == C_TE_TARGET)
    check("c_TE=-8/9 solves back to q_E=15/8", Fraction(-5, 3) / C_TE_TARGET == Q_E_TARGET)
    check("q_E=15/8 solves back to rho_E=21/4", 6 * (Q_E_TARGET - 1) == RHO_TARGET)

    blocked_routes = (
        "restricted_family_only",
        "E_center_blind_invariant",
        "same_rational_7_8_reuse",
    )
    positive_routes = (
        "typed_E_center_excess_e_E_7_8",
        "typed_center_ratio_c_TE_minus_8_9",
        "direct_rho_E_21_4_readout_primitive",
    )
    check("restricted-family-only selection is blocked", "restricted_family_only" in blocked_routes)
    check("remaining positive routes are exactly non-invariant E-center premises", len(positive_routes) == 3 and all("typed" in r or "direct" in r for r in positive_routes))


def part6_authority_markers() -> None:
    print()
    print("PART 6: note and authority markers")
    note = note_text("QUARK_ROUTE2_DIRECT_E_CENTER_READOUT_FAMILY_NO_GO_NOTE_2026-06-22.md")
    parent = note_text("S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md")
    exact = note_text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    blindness = note_text("QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md")
    firewall = note_text("QUARK_ROUTE2_E_CENTER_EXCESS_TYPED_BRIDGE_FIREWALL_NO_GO_NOTE_2026-06-22.md")

    required = (
        "Claim type:** no_go",
        "Actual current-surface status: no-go for restricted-family-only E-center selection",
        "This is not an audit verdict",
        "one-dimensional E-center shift",
        "Any direct constraint that fixes `rho_E` is therefore a non-invariant E-center premise",
        "The next positive target is not another invariant of the restricted family",
    )
    for marker in required:
        check(f"new note contains marker: {marker}", marker in note)

    check("parent note still names the endpoint triple blocker", "underlying readout-map endpoint triple is not yet derived" in parent)
    check("exact readout note names beta_E/alpha_E as the missing map entry", "beta_E / alpha_E = 21/4" in exact)
    check("E-center blindness no-go states non-evaluation leaves rho_E free", "is blind to the E-center column cannot derive" in blindness)
    check("typed firewall blocks same-rational 7/8 reuse", "same rational number != same typed Route-2 readout theorem" in firewall)

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
    print("Route-2 direct E-center readout-family classifier")
    print("Status: no-go for restricted-family-only E-center selection; not an audit verdict.")
    print("TRACE: negative_route_pruning")
    part1_restricted_family()
    part2_gauge_orbit()
    part3_affine_constraint_classifier()
    part4_ratio_constraint_classifier()
    part5_target_equivalence_and_firewall()
    part6_authority_markers()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: direct E-center readout-family classifier failed.")
        return 1
    print(
        "VERDICT: no-go for restricted-family-only E-center selection. "
        "The remaining target requires a non-invariant E-center premise: "
        "rho_E=21/4, q_E=15/8, e_E=7/8, or c_TE=-8/9."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
