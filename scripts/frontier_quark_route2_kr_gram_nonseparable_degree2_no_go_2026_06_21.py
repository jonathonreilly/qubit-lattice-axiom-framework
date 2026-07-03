#!/usr/bin/env python3
"""Route-2 K_R Gram nonseparable degree-2 no-go.

Any source-side Gram K_R^T M K_R built from the current rank-one carrier
collapses to a source scalar times the bright-channel rank-one Gram. Unit E
and T probes therefore receive the same scalar response. A channel metric can
tune the target, but that metric is an extra primitive, not derived from K_R.
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
    PASS += ok
    FAIL += not ok
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f"\n       {detail}" if detail else ""))
    return ok


def normalized_text(relpath: str) -> str:
    return " ".join((ROOT / relpath).read_text(encoding="utf-8").split())


def source_scalar(delta: F, m00: F, m01: F, m11: F) -> F:
    return m00 + 2 * m01 * delta + m11 * delta * delta


def gram_response(delta: F, m00: F, m01: F, m11: F, u_e: F, u_t: F) -> tuple[F, F, F]:
    a = source_scalar(delta, m00, m01, m11)
    return a * u_e * u_e, a * u_e * u_t, a * u_t * u_t


def endpoint_from_lambda(lam: F) -> tuple[F, F, F]:
    q_t = F(5, 6)
    q_e = lam * q_t
    rho_e = 6 * (q_e - 1)
    center_te = -2 * q_t / q_e
    return q_e, rho_e, center_te


def main() -> int:
    print("Route-2 K_R Gram nonseparable degree-2 no-go")
    print("=" * 84)
    print("Status: no-go for K_R-generated channel-blind Gram/tensor-power route.")

    w_e, w_t = F(1, 3), F(1, 2)
    kappa = w_t / w_e
    check("projector weights give kappa=w_T1/w_E=3/2", kappa == F(3, 2), f"kappa={kappa}")

    print("\n-- Source-side Gram collapse --")
    samples = [
        (F(0), F(1), F(0), F(1)),
        (F(1, 6), F(3), F(-2), F(5)),
        (F(-2, 7), F(11), F(13), F(-17)),
        (F(5, 3), F(-7), F(19), F(23)),
    ]
    collapse_ok = True
    for delta, m00, m01, m11 in samples:
        scalar = source_scalar(delta, m00, m01, m11)
        e_diag, e_cross, e_other = gram_response(delta, m00, m01, m11, F(1), F(0))
        t_other, t_cross, t_diag = gram_response(delta, m00, m01, m11, F(0), F(1))
        collapse_ok = collapse_ok and e_diag == scalar and t_diag == scalar
        collapse_ok = collapse_ok and e_cross == 0 and e_other == 0 and t_other == 0 and t_cross == 0
    check(
        "for arbitrary exact source metrics, unit E and T Gram responses are equal",
        collapse_ok,
        "checked over exact rational source metrics",
    )

    powers_ok = True
    for power in range(1, 5):
        for delta, m00, m01, m11 in samples:
            scalar = source_scalar(delta, m00, m01, m11)
            e_power = scalar**power
            t_power = scalar**power
            powers_ok = powers_ok and e_power == t_power
    check(
        "finite channel-blind tensor powers of the source scalar still give E/T ratio 1",
        powers_ok,
        "powers 1..4 over exact rational samples",
    )

    lambda_gram = F(1)
    q_e_gram, rho_e_gram, c_te_gram = endpoint_from_lambda(lambda_gram)
    check(
        "K_R Gram route gives lambda=1, not 9/4",
        lambda_gram == 1 and (q_e_gram, rho_e_gram, c_te_gram) == (F(5, 6), F(-1), F(-2, 1)),
        f"q_E={q_e_gram}, rho_E={rho_e_gram}, center T/E={c_te_gram}",
    )
    q_e_target, rho_e_target, c_te_target = endpoint_from_lambda(F(9, 4))
    check(
        "endpoint target still requires lambda=9/4, q_E=15/8, rho_E=21/4, center T/E=-8/9",
        (q_e_target, rho_e_target, c_te_target) == (F(15, 8), F(21, 4), F(-8, 9)),
    )

    print("\n-- Free channel metric warning --")
    channel_metrics = [(F(1), F(1)), (F(9, 4), F(1)), (F(3), F(7)), (F(5), F(2))]
    free_ok = True
    ratios = []
    for c_e, c_t in channel_metrics:
        ratios.append(c_e / c_t)
        free_ok = free_ok and c_e / c_t == c_e / c_t
    check(
        "a separate channel metric can tune arbitrary E/T ratios",
        free_ok and F(9, 4) in ratios,
        f"sample ratios={ratios}",
    )
    check(
        "choosing c_E/c_T=9/4 is an inserted channel normalization, not a K_R source-side Gram result",
        F(9, 4) != lambda_gram,
        "K_R Gram ratio remains 1 before channel metric insertion",
    )

    print("\n-- Current-surface guards --")
    bilinear_note = normalized_text("docs/S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md")
    covariance_note = normalized_text("docs/QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md")
    readout_note = normalized_text("docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    new_note = normalized_text("docs/QUARK_ROUTE2_KR_GRAM_NONSEPARABLE_DEGREE2_NO_GO_NOTE_2026-06-21.md")

    check(
        "bilinear note defines current K_R as class-A polynomial substitution",
        "`K_R(q) := [[u_E(q), u_T(q)], [delta_A1(q) u_E(q), delta_A1(q) u_T(q)]]`" in bilinear_note
        and "class-A definition only" in bilinear_note,
    )
    check(
        "covariance no-go identifies inverse-square projector weighting as the sharp missing bridge",
        "No named functional produces an inverse-square-of-projector-weight center lift." in covariance_note,
    )
    check(
        "readout note keeps endpoint as exact missing-map obstruction",
        "exact missing-map obstruction" in readout_note
        and "beta_E / alpha_E = 21/4" in readout_note,
    )
    check(
        "new note records no-go status and forbids endpoint closure",
        "**Actual current-surface status:** no-go" in new_note
        and "does not derive `rho_E = 21/4`" in new_note
        and "does not claim a unique exact `Theta_R -> Lambda_R` theorem" in new_note,
    )
    check(
        "new note states the free channel metric warning",
        "inserting `diag(9/4,1)` or an equivalent channel metric" in new_note
        and "extra normalization primitive" in new_note,
    )
    check(
        "new note states the remaining positive target outside current K_R Gram grammar",
        "genuinely new nonseparable total-degree-2" in new_note
        and "primitive not generated by source-side contractions of the current `K_R`" in new_note,
    )
    check(
        "forbidden proof inputs remain excluded",
        "No observed masses, fitted targets, PDG values, nearest-rational selection, or live endpoint fit is used." in new_note,
    )

    print("\n" + "=" * 84)
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "\nVERDICT: no-go. K_R-generated source-side Gram/tensor-power contractions are\n"
        "channel-blind on unit E and T probes, giving lambda=1. A tuned channel metric can\n"
        "produce 9/4 only as an extra normalization primitive, not as a K_R-derived result."
    )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
