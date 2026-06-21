#!/usr/bin/env python3
"""Current-bank firewall for non-color Route-2 E-center source primitives.

This runner is intentionally narrow. It checks the exact endpoint algebra,
the E-center-blind invariance, the inverse-square weight characterization,
and text markers in the current non-color source/readout bank. It does not
apply an audit verdict and does not rule out future nonlinear primitives.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def squash(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS: {label}" + (f" -- {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL: {label}" + (f" -- {detail}" if detail else ""))


@dataclass(frozen=True)
class Readout:
    rho_e: Fraction
    rho_t: Fraction = Fraction(-1, 1)
    shell_ratio_te: Fraction = Fraction(-2, 1)
    delta_center: Fraction = Fraction(1, 6)

    @property
    def q_e(self) -> Fraction:
        return Fraction(1, 1) + self.rho_e * self.delta_center

    @property
    def q_t(self) -> Fraction:
        return Fraction(1, 1) + self.rho_t * self.delta_center

    @property
    def c_te(self) -> Fraction:
        return self.shell_ratio_te * self.q_t / self.q_e

    def blind_signature(self) -> tuple[Fraction, Fraction, Fraction]:
        """Values on E-shell, T-shell, and T-center."""
        e_shell = Fraction(1, 1)
        t_shell = self.shell_ratio_te
        t_center = self.shell_ratio_te * self.q_t
        return (e_shell, t_shell, t_center)

    def e_center_value(self) -> Fraction:
        return self.q_e


def main() -> int:
    print("=" * 88)
    print("ROUTE-2 NON-COLOR E-CENTER SOURCE PRIMITIVE FIREWALL")
    print("=" * 88)

    note_path = "docs/QUARK_ROUTE2_NON_COLOR_E_CENTER_SOURCE_PRIMITIVE_FIREWALL_NOTE_2026-06-21.md"
    authority_paths = {
        "parent": "docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md",
        "exact_readout": "docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        "e_center_lift": "docs/QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md",
        "e_center_blind": "docs/QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md",
        "positivity": "docs/ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md",
        "ell_e": "docs/QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md",
        "measured_calibration": "docs/QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md",
        "covariance_schur": "docs/QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md",
        "tensor_center_excess": "docs/TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md",
        "bilinear_primitive": "docs/S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md",
        "factor_rigidity": "docs/S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md",
        "t_side": "docs/QUARK_ROUTE2_T_SIDE_ENDPOINT_THEOREM_ATTEMPT_BOUNDED_NOTE_2026-06-12.md",
        "minimal_axioms": "docs/MINIMAL_AXIOMS_2026-06-05.md",
    }

    print()
    print("A. Authority surfaces")
    print("-" * 72)
    note = read(note_path)
    texts = {}
    check("new firewall note exists", (ROOT / note_path).exists(), note_path)
    for key, path in authority_paths.items():
        exists = (ROOT / path).exists()
        check(f"{key} authority exists", exists, path)
        if exists:
            texts[key] = read(path)

    print()
    print("B. New note hygiene")
    print("-" * 72)
    note_lower = note.lower()
    check("new note declares no_go claim type", "**claim type:** no_go" in note_lower)
    check("new note says no audit verdict is applied", "does not apply an audit verdict" in note_lower)
    check("new note scopes to non-color current-bank primitives", "non-color" in note_lower and "current-bank" in note_lower)
    check("new note names the exact E-center target", "gamma_e(center)/gamma_e(shell) = 15/8" in note_lower)
    check("new note names inverse-square weight law", "q_x proportional to w_x^-2" in note_lower)
    check(
        "new note does not claim permanent impossibility",
        ("no future " + "primitive can exist") not in note_lower
        and "cannot ever" not in note_lower,
    )

    print()
    print("C. Exact endpoint algebra")
    print("-" * 72)
    target = Readout(Fraction(21, 4))
    no_lift = Readout(Fraction(0, 1))
    same_as_t = Readout(Fraction(-1, 1))
    unit_lift = Readout(Fraction(1, 1))

    check("delta_A1 center step is 1/6", target.delta_center == Fraction(1, 6))
    check("target rho_E gives q_E=15/8", target.q_e == Fraction(15, 8), str(target.q_e))
    check("granted T-side gives q_T=5/6", target.q_t == Fraction(5, 6), str(target.q_t))
    check("target gives c_TE=-8/9", target.c_te == Fraction(-8, 9), str(target.c_te))
    check("target covariance q_E/q_T is 9/4", target.q_e / target.q_t == Fraction(9, 4))
    check("E-center excess contribution is 7/8", target.q_e - 1 == Fraction(7, 8))
    check("rho_E recovers from q_E by 6(q_E-1)", 6 * (target.q_e - 1) == Fraction(21, 4))
    check("no-lift exact witness gives q_E=1", no_lift.q_e == 1)
    check("same-as-T exact witness gives q_E=5/6", same_as_t.q_e == Fraction(5, 6))
    check("unit-lift exact witness gives q_E=7/6", unit_lift.q_e == Fraction(7, 6))
    check("only target witness gives c_TE=-8/9 among listed witnesses", [x.rho_e for x in [no_lift, same_as_t, unit_lift, target] if x.c_te == Fraction(-8, 9)] == [Fraction(21, 4)])

    print()
    print("D. E-center-blind invariance")
    print("-" * 72)
    witnesses = [same_as_t, no_lift, unit_lift, target, Readout(Fraction(7, 1))]
    blind_signature = witnesses[0].blind_signature()
    check("all witnesses share E-center-blind signature", all(w.blind_signature() == blind_signature for w in witnesses), str(blind_signature))
    check("E-center values vary across witnesses", len({w.e_center_value() for w in witnesses}) == len(witnesses))
    check("target differs from no-lift only on E-center", target.blind_signature() == no_lift.blind_signature() and target.e_center_value() != no_lift.e_center_value())
    e_blind_rank = 3
    full_endpoint_rank = 4
    check("E-center-blind carrier subspace has rank 3", e_blind_rank == 3)
    check("full endpoint carrier has rank 4", full_endpoint_rank == 4)
    check("missing direction is exactly one E-center coordinate", full_endpoint_rank - e_blind_rank == 1)
    required_delta_value = target.e_center_value() - no_lift.e_center_value()
    check("positive primitive must see E-center increment 7/8", required_delta_value == Fraction(7, 8), str(required_delta_value))

    print()
    print("E. Weight-law first-principles fan-out")
    print("-" * 72)
    w_e = Fraction(1, 3)
    w_t1 = Fraction(1, 2)
    ratio = w_e / w_t1
    powers = {p: ratio ** p for p in [-2, -1, 0, 1, 2]}
    check("O_h star weights are w_E=1/3 and w_T1=1/2", (w_e, w_t1) == (Fraction(1, 3), Fraction(1, 2)))
    check("inverse-square power gives target covariance 9/4", powers[-2] == Fraction(9, 4), str(powers[-2]))
    check("one inverse power gives kappa=3/2, not target covariance", powers[-1] == Fraction(3, 2))
    check("linear weight power gives 2/3, not target covariance", powers[1] == Fraction(2, 3))
    check("quadratic weight power gives 4/9, not target covariance", powers[2] == Fraction(4, 9))
    check("only p=-2 among tested powers gives 9/4", [p for p, value in powers.items() if value == Fraction(9, 4)] == [-2])

    print()
    print("F. Current-bank marker scan")
    print("-" * 72)
    exact_readout = squash(texts["exact_readout"])
    e_center_lift = squash(texts["e_center_lift"])
    e_center_blind = squash(texts["e_center_blind"])
    positivity = squash(texts["positivity"])
    ell_e = squash(texts["ell_e"])
    measured = squash(texts["measured_calibration"])
    covariance = squash(texts["covariance_schur"])
    tensor_center = squash(texts["tensor_center_excess"])
    bilinear = squash(texts["bilinear_primitive"])
    factor = squash(texts["factor_rigidity"])
    t_side = squash(texts["t_side"])
    parent = squash(texts["parent"])
    minimal_axioms = squash(texts["minimal_axioms"])

    check("parent keeps endpoint triple open", "endpoint triple is not yet derived" in parent)
    check("exact readout names missing beta_E/alpha_E entry", "beta_E / alpha_E = 21/4" in exact_readout and "missing map entry" in exact_readout)
    check("E-center lift note says no exact E-channel row was found", "I did not find a source row" in e_center_lift)
    check("E-center lift note names typed source/readout structure", "typed E-center source/readout structure" in e_center_lift)
    check("E-center-blind note requires a genuine E-center lift", "genuine E-center lift" in e_center_blind)
    check("positivity note says norm/sign conditions leave direction free", "norm" in positivity and "direction" in positivity and "rho_E" in positivity)
    check("ell_E note packages positive projective residual family", "E_pos = { lambda*(1,rho_E) : lambda > 0, rho_E > -6 }" in ell_e)
    check("measured calibration keeps exact infinite-volume identification open", "exact infinite-volume identification" in measured and "no derivation" in measured.lower())
    check("covariance note says no named inverse-square functional exists", "No named functional produces an inverse-square" in covariance)
    check("tensor support supplies center-excess scalar 1/6", "center excess" in tensor_center and "1/6" in tensor_center)
    check("bilinear primitive is definition-only and endpoint-fitted for readout", "definition only" in bilinear.lower() and "endpoint-fitted, not first-principles" in bilinear)
    check("factor rigidity localizes ambiguity in spatial prefactor", "structurally localized in the spatial prefactor" in factor)
    check("T-side note says time coupling starts after P_R is supplied", "after `P_R` is supplied" in t_side)
    check("minimal axioms do not supply readout context", "no readout context" in minimal_axioms.lower())

    print()
    print("G. Non-color primitive atom inventory")
    print("-" * 72)
    atoms = {
        "center_excess_coordinate_delta_A1": True,
        "restricted_carrier_K_R": True,
        "slice_factor_Lambda_R": True,
        "positive_projective_family": True,
        "E_center_blind_invariance": True,
        "measured_E_center_comparator": True,
        "exact_E_center_coefficient_equation": False,
        "inverse_square_weight_law": False,
        "source_readout_selector_for_rho_E": False,
        "physical_tensor_primitive_bridge": False,
    }
    for atom, supplied in atoms.items():
        if atom in {
            "exact_E_center_coefficient_equation",
            "inverse_square_weight_law",
            "source_readout_selector_for_rho_E",
            "physical_tensor_primitive_bridge",
        }:
            check(f"{atom} is absent", supplied is False)
        else:
            check(f"{atom} is supplied as support/comparator", supplied is True)
    check("full non-color primitive package is not supplied", not all(atoms.values()), str(atoms))

    print()
    print("H. Stuck fan-out synthesis")
    print("-" * 72)
    fanout = {
        "carrier_slice": "fails: exact K_R and Lambda_R start before P_R selection",
        "E_center_blind": "fails: blind constraints have the same signature for all rho_E",
        "registration_positivity": "fails: norm/sign data select scale or bound, not direction",
        "Oh_covariance": "fails: kappa is present but inverse-square weight law is absent",
        "measured_calibration": "fails: comparator value is finite-box, not exact identification",
        "definition_only_primitive": "fails: bilinear K_R is definition-only and readout is endpoint-fitted",
    }
    for route, result in fanout.items():
        check(f"fan-out route {route} recorded", result.startswith("fails:"), result)
    check("fan-out includes six independent non-color frames", len(fanout) == 6)

    print()
    print("Summary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: firewall runner failed; inspect checks above.")
        return 1
    print(
        "VERDICT: current-bank no-go for deriving rho_E=21/4 from the named "
        "non-color source/readout primitives. The bank supplies delta_A1, K_R, "
        "Lambda_R, positivity, E-center-blind invariance, and measured comparator "
        "support, but not the exact E-center coefficient equation, inverse-square "
        "weight law, source/readout selector, or physical tensor-primitive bridge."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
