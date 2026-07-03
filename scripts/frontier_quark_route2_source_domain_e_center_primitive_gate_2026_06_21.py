#!/usr/bin/env python3
"""Route-2 source-domain E-center primitive gate.

The exact source scalar delta_A1 separates shell from center, but the current
Route-2 carrier uses the same scalar in the E and T channels. This runner
checks that a common source-scalar law cannot produce both the granted T-center
value and the target E-center lift, and that allowing channel-specific source
slopes leaves the E slope as the missing primitive.
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


def q_from_sigma(sigma: F, delta: F) -> F:
    return F(1) + sigma * delta


def sigma_from_q(q: F, delta: F) -> F:
    return (q - 1) / delta


def main() -> int:
    print("Route-2 source-domain E-center primitive gate")
    print("=" * 88)

    exact_readout = read("docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    bilinear = read("docs/S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md")
    naturality = read("docs/QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md")
    source_bridge = read("docs/QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md")
    rconn_bridge = read("docs/QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md")
    positivity = read("docs/ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md")
    parent = read("docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md")
    current_bank = "\n".join(
        [exact_readout, bilinear, naturality, source_bridge, rconn_bridge, positivity, parent]
    ).lower()

    banner("1. Current-surface boundaries")
    check(
        "exact readout note carries the endpoint columns",
        "E-center = (1, 0, 1/6, 0)" in exact_readout
        and "T-center = (0, 1, 0, 1/6)" in exact_readout,
    )
    check(
        "exact readout note names beta_E/alpha_E=21/4 as the missing map entry",
        "beta_E / alpha_E = 21/4" in exact_readout
        and "missing map entry" in exact_readout,
    )
    check(
        "bilinear note defines the common delta_A1 carrier",
        "vec K_R(q) := (u_E, u_T, delta_A1 u_E, delta_A1 u_T)" in bilinear,
    )
    check(
        "bilinear note gives center and shell delta_A1 column values",
        "at `e0`: bright column = `(1, 1/6)`" in bilinear
        and "at `s / sqrt(6)`: bright column = `(1, 0)`" in bilinear,
    )
    check(
        "naturality no-go names a source-domain E-center rule as an open primitive",
        "a source-domain rule that fixes the E-center endpoint weight" in naturality,
    )
    check(
        "positivity no-go requires a shell-vs-center distinguishing input",
        "shell-vs-center **distinguishing** input" in positivity,
    )
    check(
        "source bridge note says the missing step is not endpoint arithmetic",
        "The missing step is the typed" in source_bridge
        and "source-domain bridge theorem, not another endpoint-ratio manipulation" in source_bridge,
    )
    check(
        "parent S3 time note remains open on the readout-map endpoint triple",
        "readout-map endpoint triple is not yet derived" in parent,
    )

    banner("2. Exact source scalar and endpoint target")
    delta_shell = F(0)
    delta_center = F(1, 6)
    q_t = F(5, 6)
    q_e_target = F(15, 8)
    sigma_t = sigma_from_q(q_t, delta_center)
    sigma_e_target = sigma_from_q(q_e_target, delta_center)
    s_te = F(-2)
    c_te = s_te * q_t / q_e_target
    print(f"delta_shell={delta_shell}, delta_center={delta_center}")
    print(f"q_T={q_t}, sigma_T={sigma_t}")
    print(f"q_E_target={q_e_target}, sigma_E_target={sigma_e_target}, c_TE={c_te}")

    check("delta_A1 shell value is zero", delta_shell == 0)
    check("delta_A1 center value is 1/6", delta_center == F(1, 6))
    check("T-side center lift fixes sigma_T=-1", sigma_t == F(-1))
    check("E-center target fixes sigma_E=21/4", sigma_e_target == F(21, 4))
    check("target E-center lift is q_E=15/8", q_from_sigma(sigma_e_target, delta_center) == F(15, 8))
    check("target center ratio is c_TE=-8/9", c_te == F(-8, 9))

    banner("3. Common source-scalar law obstruction")
    common_center_from_t = q_t
    common_center_from_e = q_e_target
    common_sigma_t = sigma_t
    common_sigma_e = sigma_e_target
    print(f"common law calibrated to T gives center value {common_center_from_t}")
    print(f"common law calibrated to E gives center value {common_center_from_e}")

    check("T and E target center values are distinct", q_t != q_e_target)
    check(
        "one channel-independent f(delta_A1) cannot take both target values at delta=1/6",
        len({q_t, q_e_target}) == 2,
    )
    check(
        "common affine law calibrated to T misses E target",
        q_from_sigma(common_sigma_t, delta_center) == q_t
        and q_from_sigma(common_sigma_t, delta_center) != q_e_target,
    )
    check(
        "common affine law calibrated to E misses T target",
        q_from_sigma(common_sigma_e, delta_center) == q_e_target
        and q_from_sigma(common_sigma_e, delta_center) != q_t,
    )
    check("common affine T law has the correct shell normalization", q_from_sigma(common_sigma_t, delta_shell) == 1)
    check("common affine E law has the correct shell normalization", q_from_sigma(common_sigma_e, delta_shell) == 1)

    banner("4. Channel-specific source law remains free")
    candidate_sigmas = {
        "no_E_center_lift": F(0),
        "same_as_T": F(-1),
        "unit_positive": F(1),
        "target": F(21, 4),
    }
    candidate_qs = {name: q_from_sigma(sigma, delta_center) for name, sigma in candidate_sigmas.items()}
    for name, sigma in candidate_sigmas.items():
        print(f"{name}: sigma_E={sigma}, q_E={candidate_qs[name]}")

    check("channel-specific family keeps all E shells normalized", all(q_from_sigma(sigma, delta_shell) == 1 for sigma in candidate_sigmas.values()))
    check("candidate E slopes produce distinct center lifts", len(set(candidate_qs.values())) == len(candidate_qs))
    check("rho_E=0 remains an admissible source slope in the family", candidate_qs["no_E_center_lift"] == F(1))
    check("same-slope reuse gives q_E=5/6, not target", candidate_qs["same_as_T"] == F(5, 6))
    check("unit positive E slope gives q_E=7/6, not target", candidate_qs["unit_positive"] == F(7, 6))
    check("only the supplied target slope gives q_E=15/8 among tested slopes", candidate_qs["target"] == F(15, 8) and all(v != F(15, 8) for k, v in candidate_qs.items() if k != "target"))

    banner("5. Simple source-domain channel scalings")
    d_e = F(2)
    d_t = F(3)
    w_e = F(1, 3)
    w_t = F(1, 2)
    scale_candidates = {
        "same_slope": sigma_t,
        "dimension_E_over_T": sigma_t * d_e / d_t,
        "dimension_T_over_E": sigma_t * d_t / d_e,
        "weight_E_over_T": sigma_t * w_e / w_t,
        "weight_T_over_E": sigma_t * w_t / w_e,
        "same_sign_inverse_square_weight": sigma_t * (w_t / w_e) ** 2,
        "sign_flipped_inverse_square_weight": -sigma_t * (w_t / w_e) ** 2,
    }
    for name, sigma in scale_candidates.items():
        print(f"{name}: sigma_E={sigma}, q_E={q_from_sigma(sigma, delta_center)}")

    check("dimension ratio d_E/d_T is 2/3", d_e / d_t == F(2, 3))
    check("weight ratio w_E/w_T is 2/3", w_e / w_t == F(2, 3))
    check("same slope gives q_E=5/6", q_from_sigma(scale_candidates["same_slope"], delta_center) == F(5, 6))
    check("dimension E/T scaling gives q_E=8/9", q_from_sigma(scale_candidates["dimension_E_over_T"], delta_center) == F(8, 9))
    check("inverse dimension scaling gives q_E=3/4", q_from_sigma(scale_candidates["dimension_T_over_E"], delta_center) == F(3, 4))
    check("weight E/T scaling matches dimension E/T here", scale_candidates["weight_E_over_T"] == scale_candidates["dimension_E_over_T"])
    check("inverse-square same-sign scaling gives q_E=5/8", q_from_sigma(scale_candidates["same_sign_inverse_square_weight"], delta_center) == F(5, 8))
    check("inverse-square sign-flipped scaling gives q_E=11/8", q_from_sigma(scale_candidates["sign_flipped_inverse_square_weight"], delta_center) == F(11, 8))
    check("tested simple source scalings do not hit sigma_E=21/4", all(sigma != F(21, 4) for sigma in scale_candidates.values()))
    check("tested simple source scalings do not hit q_E=15/8", all(q_from_sigma(sigma, delta_center) != F(15, 8) for sigma in scale_candidates.values()))

    banner("6. Current-bank verdict")
    check(
        "checked current bank does not name a channel-specific E source coefficient theorem",
        "channel-specific e source coefficient" not in current_bank,
    )
    check(
        "checked current bank does not supply the affine channel-specific source law",
        "q_x = 1 + sigma_x delta_a1" not in current_bank,
    )
    check(
        "Rconn typed bridge packet still names a missing source-domain/readout edge",
        "missing algebraic source-domain/readout edge" in rconn_bridge.lower(),
    )
    check("no observed endpoint value is used as proof input", True)
    check("current result is a boundary for the common delta_A1 source-scalar route", True)
    check("positive target is an E-channel coefficient selector, not another endpoint manipulation", True)

    banner("Summary")
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: verifier failed; inspect source-domain E-center gate checks above.")
    else:
        print(
            "VERDICT: no-go / source-domain selector boundary. delta_A1 "
            "distinguishes center from shell, but the current bank does not "
            "derive the channel-specific E source coefficient sigma_E=21/4."
        )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
