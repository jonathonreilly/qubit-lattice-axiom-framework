"""Route-2 coefficient-selection boundary for the E-center readout datum.

Question
--------
Can a target-free coefficient-selection principle on the reduced Route-2
readout family select rho_E = 21/4?

Result
------
Within the tested exact classes, no. After the two T-side entries are granted,
the endpoint algebra reduces the residual to one positive projective E-row
direction

    ell_E ~ (1, rho_E),  rho_E > -6.

The familiar target-free selectors either leave rho_E free or pick other exact
values. A general quadratic/variational selector can be made to pick 21/4 only
by placing the target-equivalent coefficient ratio in the functional. The
inverse-square projector-weight rule lands exactly, but that rule is precisely
the missing coefficient selector, not a consequence of the current surface.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F


PASS = 0
FAIL = 0


def check(label: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(cond)
    PASS += int(ok)
    FAIL += int(not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    if detail:
        print(f"       {detail}")
    return ok


RHO_T = F(-1, 1)
S_TE = F(-2, 1)
Q_T = F(1, 1) + RHO_T / 6
RHO_TARGET = F(21, 4)
Q_E_TARGET = F(15, 8)
C_TE_TARGET = F(-8, 9)
W_E = F(1, 3)
W_T = F(1, 2)
KAPPA = W_T / W_E


def q_e(rho_e: F) -> F:
    return F(1, 1) + rho_e / 6


def lambda_from_rho(rho_e: F) -> F:
    return q_e(rho_e) / Q_T


def c_te(rho_e: F) -> F:
    return S_TE * Q_T / q_e(rho_e)


def rho_from_lambda(lam: F) -> F:
    return 6 * (lam * Q_T - 1)


@dataclass(frozen=True)
class Selector:
    name: str
    rho: F | None
    status: str


def stationary_q_for_quadratic(A: F, B: F) -> F:
    """Stationary point of A*q^2 + B*q + C with A>0."""
    return -B / (2 * A)


def main() -> int:
    print("Route-2 coefficient-selection boundary")
    print("=" * 88)

    check(
        "granted T-side algebra gives q_T=5/6 and leaves rho_E as the only E-row slope",
        RHO_T == F(-1, 1) and S_TE == F(-2, 1) and Q_T == F(5, 6),
        f"rho_T={RHO_T}, s_TE={S_TE}, q_T={Q_T}",
    )

    check(
        "target chain is exactly rho_E=21/4 <-> q_E=15/8 <-> c_TE=-8/9 <-> lambda=9/4",
        q_e(RHO_TARGET) == Q_E_TARGET
        and c_te(RHO_TARGET) == C_TE_TARGET
        and lambda_from_rho(RHO_TARGET) == F(9, 4),
        f"q_E={q_e(RHO_TARGET)}, c_TE={c_te(RHO_TARGET)}, lambda={lambda_from_rho(RHO_TARGET)}",
    )

    admissible_samples = [F(-5, 1), F(-1, 1), F(0, 1), F(1, 1), RHO_TARGET, F(6, 1)]
    check(
        "positivity/admissibility gives an interval rho_E>-6, not a selected point",
        all(q_e(rho) > 0 for rho in admissible_samples)
        and len({lambda_from_rho(rho) for rho in admissible_samples}) == len(admissible_samples),
        f"samples={[(rho, q_e(rho), lambda_from_rho(rho)) for rho in admissible_samples]}",
    )

    blind_signature = (Q_T, S_TE)
    check(
        "E-center-blind data are identical across distinct rho_E choices",
        all((Q_T, S_TE) == blind_signature for _ in admissible_samples)
        and len({q_e(rho) for rho in admissible_samples}) == len(admissible_samples),
        f"blind_signature=(q_T={Q_T}, s_TE={S_TE}); q_E varies",
    )

    selectors = [
        Selector("minimal slope / no E-center lift", F(0, 1), "target-free"),
        Selector("same E and T center/shell lift", RHO_T, "target-free"),
        Selector("single reciprocal projector-weight lift", rho_from_lambda(KAPPA), "target-free-one-power"),
        Selector("inverse-square projector-weight lift", rho_from_lambda(KAPPA * KAPPA), "missing-selector"),
    ]
    selector_values = {s.name: (s.rho, q_e(s.rho) if s.rho is not None else None, lambda_from_rho(s.rho) if s.rho is not None else None) for s in selectors}
    check(
        "ordinary target-free selectors do not pick rho_E=21/4; only inverse-square weighting lands",
        selector_values["minimal slope / no E-center lift"][0] == F(0, 1)
        and selector_values["same E and T center/shell lift"][0] == F(-1, 1)
        and selector_values["single reciprocal projector-weight lift"][0] == F(3, 2)
        and selector_values["inverse-square projector-weight lift"][0] == RHO_TARGET,
        f"selector_values={selector_values}",
    )

    q0_target = Q_E_TARGET
    required_B_over_A = -2 * q0_target
    check(
        "a quadratic variational selector picks the target only if its coefficient ratio imports q_E=15/8",
        stationary_q_for_quadratic(F(1, 1), required_B_over_A) == Q_E_TARGET
        and required_B_over_A == F(-15, 4),
        f"For F(q)=A q^2+B q+C, q*=15/8 requires B/A={required_B_over_A}",
    )

    target_free_quadratic_anchors = {
        "q*=1 (no lift)": F(1, 1),
        "q*=q_T": Q_T,
        "q*=kappa*q_T": KAPPA * Q_T,
    }
    check(
        "target-free quadratic anchors land at q_E in {1,5/6,5/4}, not 15/8",
        set(target_free_quadratic_anchors.values()) == {F(1, 1), F(5, 6), F(5, 4)}
        and all(q != Q_E_TARGET for q in target_free_quadratic_anchors.values()),
        f"anchors={target_free_quadratic_anchors}",
    )

    free_reduced_matrix_ratios = [F(1, 1), KAPPA, KAPPA * KAPPA, F(4, 3)]
    check(
        "free quadratic/readout coefficient ratios can realize target and non-target values in the same algebraic class",
        [rho_from_lambda(lam) for lam in free_reduced_matrix_ratios]
        == [F(-1, 1), F(3, 2), RHO_TARGET, F(2, 3)]
        and len(set(free_reduced_matrix_ratios)) == 4,
        f"ratios_to_rho={[(lam, rho_from_lambda(lam)) for lam in free_reduced_matrix_ratios]}",
    )

    required_power = 2
    powers = {n: rho_from_lambda(KAPPA**n) for n in [0, 1, 2]}
    check(
        "projector-weight power law selects the endpoint only after the exponent is set to n=2",
        powers == {0: F(-1, 1), 1: F(3, 2), 2: RHO_TARGET} and required_power == 2,
        f"rho(n)={powers}",
    )

    print("\n" + "=" * 88)
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "\nVERDICT: no-go boundary for target-free coefficient selection. The reduced\n"
        "Route-2 endpoint algebra leaves rho_E as a positive projective slope.\n"
        "Common target-free selectors pick rho_E=-1,0,3/2 or leave the slope free.\n"
        "General quadratic/variational selectors can hit 21/4 only by inserting\n"
        "the target-equivalent coefficient ratio B/A=-15/4. The inverse-square\n"
        "projector-weight rule lands exactly, but selecting that rule or exponent\n"
        "n=2 is the missing theorem content, not a current derivation."
    )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
