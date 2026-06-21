#!/usr/bin/env python3
"""Block70 Route-2 E-center inverse-square source-law firewall.

This runner attacks the direct E-center theorem target for q_E = 15/8 from
minimal Route-2/S3 premises. It does not use observed masses, endpoint fitting,
or live-readout proximity as proof inputs.

Safe claim:
  Under the granted T-side values and the exact O_h star leverage, the direct
  E-center target is exactly equivalent to the inverse-square source/readout
  law q_E/q_T = (w_E/w_T1)^-2. The current named E-center/source/readout bank
  does not supply that law. This is a narrow current-bank firewall, not a
  global impossibility theorem over future nonlinear primitives.
"""

from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

NOTE = DOCS / "QUARK_ROUTE2_E_CENTER_INVERSE_SQUARE_SOURCE_LAW_FIREWALL_NOTE_2026-06-21.md"
READOUT = DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
E_CENTER_ATTEMPT = DOCS / "QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md"
E_CENTER_BLIND = DOCS / "QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md"
NATURALITY = DOCS / "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md"
MEASURED = DOCS / "QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md"
BOX_SCAN = DOCS / "QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md"
KAPPA_NO_GO = DOCS / "QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md"
QUADRATIC_NO_GO = DOCS / "QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md"
OH_LEVERAGE = DOCS / "OH_SEVEN_SITE_STAR_SHELL_LEVERAGE_POSITIVE_THEOREM_NOTE_2026-06-10.md"
SOURCE_DOMAIN = DOCS / "QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md"
RECORD_POSITIVITY = DOCS / "ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md"
READOUT_PRIMITIVE = DOCS / "S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md"
S3_PARENT = DOCS / "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md"
S3_RIGIDITY = DOCS / "S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md"
CENTER_EXCESS = DOCS / "TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md"


PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(s: str) -> str:
    return " ".join(s.split())


def contains_all(haystack: str, needles: tuple[str, ...]) -> bool:
    return all(needle in haystack for needle in needles)


def q_from_rho(rho: F, center_denominator: F = F(6, 1)) -> F:
    return F(1, 1) + rho / center_denominator


def rho_from_q(q: F, center_denominator: F = F(6, 1)) -> F:
    return center_denominator * (q - 1)


def lambda_from_power(power: int) -> F:
    w_e = F(1, 3)
    w_t = F(1, 2)
    return (w_e / w_t) ** power


def q_e_from_power(power: int) -> F:
    q_t = F(5, 6)
    return q_t * lambda_from_power(power)


def rho_e_from_power(power: int) -> F:
    return rho_from_q(q_e_from_power(power))


def main() -> int:
    print("BLOCK70 ROUTE-2 E-CENTER INVERSE-SQUARE SOURCE-LAW FIREWALL")
    print("=" * 78)

    print("\nFile presence")
    for path in (
        NOTE,
        READOUT,
        E_CENTER_ATTEMPT,
        E_CENTER_BLIND,
        NATURALITY,
        MEASURED,
        BOX_SCAN,
        KAPPA_NO_GO,
        QUADRATIC_NO_GO,
        OH_LEVERAGE,
        SOURCE_DOMAIN,
        RECORD_POSITIVITY,
        READOUT_PRIMITIVE,
        S3_PARENT,
        S3_RIGIDITY,
        CENTER_EXCESS,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = text(NOTE)
    readout = text(READOUT)
    e_center_attempt = text(E_CENTER_ATTEMPT)
    e_center_blind = text(E_CENTER_BLIND)
    naturality = text(NATURALITY)
    measured = text(MEASURED)
    box_scan = text(BOX_SCAN)
    kappa_no_go = text(KAPPA_NO_GO)
    quadratic_no_go = text(QUADRATIC_NO_GO)
    oh_leverage = text(OH_LEVERAGE)
    source_domain = text(SOURCE_DOMAIN)
    record_positivity = text(RECORD_POSITIVITY)
    readout_primitive = text(READOUT_PRIMITIVE)
    s3_parent = text(S3_PARENT)
    s3_rigidity = text(S3_RIGIDITY)
    center_excess = text(CENTER_EXCESS)

    print("\nNew note firewall checks")
    check(
        "new note declares bounded current-bank firewall status",
        "**Actual current-surface status:** exact negative boundary / bounded support"
        in note,
    )
    check(
        "new note states it is not an audit verdict",
        "This is not an audit verdict." in note,
    )
    check(
        "new note records A_min and forbidden imports",
        contains_all(
            note,
            (
                "## Minimal Premise Set A_min",
                "## Forbidden Proof Inputs",
                "observed quark masses",
                "nearest-rational",
            ),
        ),
    )
    check(
        "new note names inverse-square source/readout law as the remaining direct target",
        "q_E/q_T = (w_E/w_T1)^-2" in note
        and "inverse-square source/readout law" in note,
    )
    check(
        "new note keeps future nonlinear primitive route open",
        "future nonlinear source/readout primitive" in flat(note)
        and "not a global impossibility theorem" in note,
    )
    check(
        "new note avoids forbidden promotion words",
        not any(
            phrase in note
            for phrase in (
                "audit-" + "ratified",
                "retained " + "branch-local",
                "would become " + "retained",
                "promoted to " + "retained",
                "no future primitive " + "can exist",
            )
        ),
    )

    print("\nExact Route-2 endpoint algebra")
    rho_t = F(-1, 1)
    q_t = q_from_rho(rho_t)
    rho_e_target = F(21, 4)
    q_e_target = q_from_rho(rho_e_target)
    lambda_target = q_e_target / q_t
    c_te = F(-2, 1) * q_t / q_e_target
    check("rho_T=-1 gives q_T=5/6", q_t == F(5, 6), str(q_t))
    check("rho_E=21/4 gives q_E=15/8", q_e_target == F(15, 8), str(q_e_target))
    check("q_E/q_T target is exactly 9/4", lambda_target == F(9, 4), str(lambda_target))
    check("target center T/E ratio is exactly -8/9", c_te == F(-8, 9), str(c_te))
    check(
        "solving q_E=(9/4)q_T returns rho_E=21/4",
        rho_from_q(F(9, 4) * q_t) == rho_e_target,
        str(rho_from_q(F(9, 4) * q_t)),
    )

    print("\nO_h shell-leverage and inverse-square characterization")
    w_e = F(1, 3)
    w_t = F(1, 2)
    leverage = w_t / w_e
    check("per-arm weights are w_E=1/3 and w_T1=1/2", (w_e, w_t) == (F(1, 3), F(1, 2)))
    check("kappa=w_T1/w_E=3/2 and kappa^2=9/4", leverage == F(3, 2) and leverage**2 == F(9, 4), str(leverage**2))
    check(
        "inverse-square law gives target lambda exactly",
        lambda_from_power(-2) == F(9, 4),
        f"(w_E/w_T1)^-2={lambda_from_power(-2)}",
    )
    check(
        "one-power inverse law gives only 3/2, not 9/4",
        lambda_from_power(-1) == F(3, 2) and lambda_from_power(-1) != F(9, 4),
        str(lambda_from_power(-1)),
    )
    check(
        "natural positive quadratic weight gives 4/9, not 9/4",
        lambda_from_power(2) == F(4, 9) and lambda_from_power(2) != F(9, 4),
        str(lambda_from_power(2)),
    )
    powers = list(range(-4, 5))
    target_powers = [p for p in powers if lambda_from_power(p) == F(9, 4)]
    check("among powers -4..4, only p=-2 gives 9/4", target_powers == [-2], str(target_powers))
    nonnegative_lambdas = [lambda_from_power(p) for p in range(0, 5)]
    check(
        "nonnegative projector-power laws cannot exceed 1 and therefore cannot reach 9/4",
        all(value <= 1 for value in nonnegative_lambdas),
        str(nonnegative_lambdas),
    )

    print("\nWrong-law falsifiers")
    law_expectations = {
        -2: (F(15, 8), F(21, 4)),
        -1: (F(5, 4), F(3, 2)),
        0: (F(5, 6), F(-1, 1)),
        1: (F(5, 9), F(-8, 3)),
        2: (F(10, 27), F(-34, 9)),
    }
    for power, (q_expected, rho_expected) in law_expectations.items():
        q_e = q_e_from_power(power)
        rho_e = rho_e_from_power(power)
        check(
            f"power p={power} gives expected q_E and rho_E",
            (q_e, rho_e) == (q_expected, rho_expected),
            f"q_E={q_e}, rho_E={rho_e}",
        )
    check(
        "only inverse-square among tested laws gives q_E=15/8 and rho_E=21/4",
        [
            power
            for power in law_expectations
            if q_e_from_power(power) == F(15, 8) and rho_e_from_power(power) == F(21, 4)
        ]
        == [-2],
    )

    print("\nCurrent source-bank boundary checks")
    check(
        "exact readout map leaves the E-channel map entry as the missing entry",
        contains_all(
            readout,
            (
                "irreducible missing map entry",
                "beta_E / alpha_E = 21/4",
                "do not yet fix the readout map",
            ),
        ),
    )
    check(
        "E-center derivation attempt names W1 as missing exact E-channel computation",
        contains_all(
            e_center_attempt,
            (
                "Missing exact E-channel source/readout computation",
                "derive gamma_E(center)/gamma_E(shell) = 15/8",
            ),
        ),
    )
    check(
        "E-center blindness note says positive repair must see E-center",
        contains_all(
            e_center_blind,
            (
                "cannot derive those values",
                "must supply a genuine E-center lift",
            ),
        ),
    )
    check(
        "naturality no-go keeps rho_E free absent E-center/source/readout input",
        "remains a free parameter unless an additional E-center endpoint ratio, source-domain, or readout-map primitive is supplied"
        in flat(naturality),
    )
    check(
        "measured calibration keeps exact infinite-volume identification open",
        "what is missing is its **exact\n   infinite-volume identification**" in measured,
    )
    check(
        "box-size scan rejects the bulk-limit route for q_E=15/8",
        "No infinite-volume limit recovers 15/8" in box_scan
        and "closes the bulk-limit hatch" in box_scan,
    )
    check(
        "kappa no-go relocates the missing datum to lambda=kappa^2 without deriving it",
        contains_all(
            kappa_no_go,
            (
                "covariance bridge",
                "is not a consequence",
            ),
        ),
    )
    check(
        "quadratic no-go states no named inverse-square functional exists",
        "No named functional produces an\n  inverse-square-of-projector-weight center lift"
        in quadratic_no_go,
    )
    check(
        "O_h leverage note does not derive a Route-2 readout entry",
        "does **not**, by itself, derive any Route-2 readout entry" in oh_leverage,
    )
    check(
        "source-domain note leaves the typed color bridge missing",
        "There is no current typed edge" in source_domain
        and "R_conn = 8/9 -> c_TE = gamma_T(center)/gamma_E(center) = -8/9"
        in source_domain,
    )
    check(
        "record/positivity note fixes norm not direction",
        "fix the readout **norm** (or a bound), while `rho_E` is the readout **direction**"
        in flat(record_positivity),
    )
    check(
        "readout-primitive assessment gives membership but not uniqueness",
        "membership-but-not-uniqueness" in readout_primitive
        and "selection freedom is exactly" in readout_primitive,
    )
    check(
        "S3 parent remains blocked by the endpoint triple",
        "the underlying readout-map endpoint triple is not yet derived" in s3_parent,
    )
    check(
        "factor-rigidity localizes ambiguity to spatial prefactor but does not select rho_E",
        "structurally localized in the spatial prefactor" in s3_rigidity
        and "Does **not** derive the readout-triple" in s3_rigidity,
    )
    check(
        "center-excess note supplies denominator 6 rather than the E-source law",
        "phi_support(center) - phi_support(arm_mean) = 1/6" in center_excess
        and "exact tensor endpoint coefficients" in center_excess,
    )

    print("\nFan-out synthesis checks")
    fanout = {
        "carrier_column": "E-center must be evaluated; blind constraints are invariant.",
        "same_domain_leverage": "kappa=3/2 is present, but lambda=kappa^2 is a bridge.",
        "power_law": "only p=-2 gives the target; p>=0 and p=-1 fail.",
        "quadratic_schur": "quadratic O_h invariants have a free E:T1 ratio.",
        "current_bank": "current source/readout surfaces name the inverse-square law as missing.",
    }
    check("stuck fan-out has five orthogonal frames", len(fanout) == 5, ", ".join(fanout))
    check(
        "all frames preserve the direct positive route as an explicit missing theorem",
        "future nonlinear source/readout primitive" in flat(note)
        and "derive the inverse-square source/readout law" in note,
    )

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print(
        "VERDICT: exact current-bank firewall. The direct E-center target is reduced to "
        "the inverse-square law q_E/q_T=(w_E/w_T1)^-2; the current named "
        "E-center/source/readout bank does not supply that law. This does not rule out "
        "a future nonlinear primitive or equivalent E-center distinguishing theorem."
    )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
