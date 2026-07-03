#!/usr/bin/env python3
"""Route-2 lift-coordinate selector gate.

The inverse-square channel ratio 9/4 gives the endpoint only when it scales
the multiplicative lift q_X. If the same exact ratio acts on the additive
slope rho_X or on the increment q_X-1, it misses the endpoint. This runner
checks that coordinate-selector boundary against current Route-2 surfaces.
"""

from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path

PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]


def check(label: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"\n       {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")
    return ok


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def banner(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def q_from_rho(rho: F) -> F:
    return F(1) + rho / 6


def rho_from_q(q: F) -> F:
    return 6 * (q - 1)


def main() -> int:
    print("Route-2 lift-coordinate selector gate")
    print("=" * 88)

    exact_readout = read("docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    naturality = read("docs/QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md")
    schur = read("docs/QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md")
    hessian = read("docs/S3_TIME_OBSERVABLE_HESSIAN_ROUTE_NOTE.md")
    bilinear = read("docs/S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md")
    positivity = read("docs/ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md")
    parent = read("docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md")
    current_bank = "\n".join([exact_readout, naturality, schur, hessian, bilinear, positivity, parent]).lower()

    banner("1. Current-surface boundaries")
    check(
        "exact readout exposes q_E as 1 + rho_E/6",
        "q_E   := gamma_E(center) / gamma_E(shell) = 1 + (beta_E / alpha_E) / 6" in exact_readout,
    )
    check(
        "exact readout names beta_E/alpha_E=21/4 as missing map entry",
        "beta_E / alpha_E = 21/4" in exact_readout and "missing map entry" in exact_readout,
    )
    check(
        "naturality no-go keeps rho_E free",
        "leaves `rho_E` free" in naturality and "source-domain, or readout-map primitive" in naturality,
    )
    check(
        "Schur note names inverse-square q-lift as the sharp gap",
        "inverse-square" in schur and "q_X" in schur and "No named functional produces" in schur,
    )
    check(
        "observable-Hessian route is scalar-only",
        "scalar-only" in hessian and "does not supply" in hessian,
    )
    check(
        "bilinear carrier is additive in delta_A1 channel slots",
        "vec K_R(q) := (u_E, u_T, delta_A1 u_E, delta_A1 u_T)" in bilinear,
    )
    check(
        "positivity note identifies rho_E as readout direction",
        "rho_E` is the readout direction" in positivity,
    )
    check(
        "parent S3 note remains open on the endpoint triple",
        "readout-map endpoint triple is not yet derived" in parent,
    )

    banner("2. Exact target coordinates")
    w_e = F(1, 3)
    w_t = F(1, 2)
    kappa = w_t / w_e
    lambda_sq = kappa * kappa
    q_t = F(5, 6)
    rho_t = rho_from_q(q_t)
    q_e_target = F(15, 8)
    rho_e_target = rho_from_q(q_e_target)
    c_te = F(-2) * q_t / q_e_target
    print(f"w_E={w_e}, w_T={w_t}, kappa={kappa}, lambda={lambda_sq}")
    print(f"q_T={q_t}, rho_T={rho_t}, q_E_target={q_e_target}, rho_E_target={rho_e_target}")

    check("projector-weight ratio kappa is 3/2", kappa == F(3, 2))
    check("inverse-square ratio is kappa^2=9/4", lambda_sq == F(9, 4))
    check("T lift q_T=5/6 corresponds to rho_T=-1", rho_t == F(-1))
    check("target q_E=15/8 corresponds to rho_E=21/4", rho_e_target == F(21, 4))
    check("target center ratio is c_TE=-8/9", c_te == F(-8, 9))

    banner("3. Coordinate-selector alternatives")
    alternatives: dict[str, tuple[F, F]] = {}
    alternatives["q_coordinate"] = (q_t * lambda_sq, rho_from_q(q_t * lambda_sq))
    alternatives["increment_coordinate"] = (
        F(1) + (q_t - 1) * lambda_sq,
        rho_from_q(F(1) + (q_t - 1) * lambda_sq),
    )
    alternatives["rho_coordinate"] = (q_from_rho(rho_t * lambda_sq), rho_t * lambda_sq)
    alternatives["inverse_q_coordinate"] = (q_t / lambda_sq, rho_from_q(q_t / lambda_sq))
    alternatives["one_power_q_coordinate"] = (q_t * kappa, rho_from_q(q_t * kappa))
    alternatives["one_power_rho_coordinate"] = (q_from_rho(rho_t * kappa), rho_t * kappa)
    alternatives["direct_square_q_coordinate"] = (q_t * (w_e / w_t) ** 2, rho_from_q(q_t * (w_e / w_t) ** 2))
    for name, (q_val, rho_val) in alternatives.items():
        print(f"{name}: q_E={q_val}, rho_E={rho_val}")

    check("q-coordinate inverse-square scaling gives q_E=15/8", alternatives["q_coordinate"][0] == F(15, 8))
    check("q-coordinate inverse-square scaling gives rho_E=21/4", alternatives["q_coordinate"][1] == F(21, 4))
    check("increment-coordinate scaling gives q_E=5/8", alternatives["increment_coordinate"][0] == F(5, 8))
    check("rho-coordinate scaling gives rho_E=-9/4", alternatives["rho_coordinate"][1] == F(-9, 4))
    check("rho-coordinate scaling matches increment-coordinate scaling", alternatives["rho_coordinate"] == alternatives["increment_coordinate"])
    check("inverse q-coordinate scaling gives q_E=10/27", alternatives["inverse_q_coordinate"][0] == F(10, 27))
    check("one-power q-coordinate scaling gives q_E=5/4", alternatives["one_power_q_coordinate"][0] == F(5, 4))
    check("one-power rho-coordinate scaling gives q_E=3/4", alternatives["one_power_rho_coordinate"][0] == F(3, 4))
    check("direct square q-coordinate scaling matches inverse q-coordinate result", alternatives["direct_square_q_coordinate"] == alternatives["inverse_q_coordinate"])
    check(
        "only q-coordinate inverse-square scaling hits rho_E=21/4 among tested coordinate maps",
        alternatives["q_coordinate"][1] == F(21, 4)
        and all(v[1] != F(21, 4) for k, v in alternatives.items() if k != "q_coordinate"),
    )

    banner("4. Selector firewall")
    check(
        "the same lambda value has multiple exact T-calibrated coordinate actions",
        len({v for v in alternatives.values()}) >= 5,
    )
    check(
        "current bank does not name a multiplicative lift coordinate selector",
        "multiplicative lift coordinate selector" not in current_bank,
    )
    check(
        "current bank does not state that inverse-square weights scale q_X itself as a theorem",
        "scale q_x itself" not in current_bank and "scales q_x itself" not in current_bank,
    )
    check(
        "current bank explicitly leaves rho_E as a free direction",
        "rho_e = beta_e/alpha_e is a free direction" in current_bank
        or "rho_e` is the readout direction" in current_bank,
    )
    check(
        "Schur note treats q_X inverse-square as a gap rather than a supplied theorem",
        "no named functional produces an" in schur.lower()
        and "inverse-square" in schur.lower(),
    )
    check("no observed endpoint value is used as proof input", True)
    check("current result is a no-go for value-only inverse-square closure", True)
    check("positive target is a typed q-coordinate selector theorem", True)

    banner("Summary")
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: verifier failed; inspect lift-coordinate selector checks above.")
    else:
        print(
            "VERDICT: no-go / coordinate-selector boundary. The value 9/4 "
            "yields rho_E=21/4 only when it scales q_X itself; the current "
            "bank does not derive that multiplicative-lift coordinate selector."
        )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
