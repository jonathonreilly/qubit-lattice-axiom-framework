#!/usr/bin/env python3
"""Route-2 source/readout factorization gauge no-go.

The current endpoint/readout algebra observes a product of any source and
readout leg normalizations. It fixes total reciprocal projector-weight degree,
not the source/readout split. This runner checks that obstruction exactly and
guards the current-surface wording.
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


def response_ratio_for_degree(degree: F, w_e: F = F(1, 3), w_t: F = F(1, 2)) -> F:
    """E/T response ratio for reciprocal degree `degree`."""
    return (w_t / w_e) ** degree


def endpoint_from_lambda(lam: F) -> tuple[F, F, F]:
    q_t = F(5, 6)
    q_e = lam * q_t
    rho_e = 6 * (q_e - 1)
    center_te = -2 * q_t / q_e
    return q_e, rho_e, center_te


def main() -> int:
    print("Route-2 source/readout factorization gauge no-go")
    print("=" * 84)
    print("Status: no-go for certifying independent legs from product-level readout alone.")

    w_a1, w_e, w_t = F(1, 6), F(1, 3), F(1, 2)
    kappa = w_t / w_e
    check(
        "exact projector weights and kappa are the Route-2 six-arm values",
        (w_a1, w_e, w_t, kappa) == (F(1, 6), F(1, 3), F(1, 2), F(3, 2)),
        f"(w_A1,w_E,w_T,kappa)=({w_a1},{w_e},{w_t},{kappa})",
    )

    lam_target = F(9, 4)
    q_e, rho_e, center_te = endpoint_from_lambda(lam_target)
    check(
        "total reciprocal degree d=2 gives the exact endpoint algebra",
        response_ratio_for_degree(F(2)) == lam_target
        and (q_e, rho_e, center_te) == (F(15, 8), F(21, 4), F(-8, 9)),
        f"lambda={lam_target}, q_E={q_e}, rho_E={rho_e}, center T/E={center_te}",
    )

    print("\n-- Degree split degeneracy --")
    splits = [(F(-1), F(3)), (F(0), F(2)), (F(1), F(1)), (F(2), F(0)), (F(3), F(-1))]
    split_rows = []
    for source_degree, readout_degree in splits:
        source_ratio = response_ratio_for_degree(source_degree)
        readout_ratio = response_ratio_for_degree(readout_degree)
        product = source_ratio * readout_ratio
        split_rows.append((source_degree, readout_degree, source_ratio, readout_ratio, product))
        print(
            f"  a={str(source_degree):>3}, b={str(readout_degree):>3}: "
            f"source={source_ratio}, readout={readout_ratio}, product={product}"
        )

    check(
        "all displayed source/readout degree splits have total degree two and product lambda=9/4",
        all(row[0] + row[1] == 2 and row[4] == lam_target for row in split_rows),
    )
    check(
        "the endpoint product does not select the desired split a=b=1",
        len({(row[2], row[3]) for row in split_rows}) == len(split_rows)
        and (F(1), F(1), F(3, 2), F(3, 2), F(9, 4)) in split_rows,
        "multiple distinct source/readout attributions have the same product",
    )

    print("\n-- Channelwise factorization gauge --")
    source_e, source_t = F(9), F(4)
    readout_e, readout_t = F(1, 9), F(1, 4)
    product_e = source_e * readout_e
    product_t = source_t * readout_t
    gauge_e, gauge_t = F(5), F(7)
    source_e_g = gauge_e * source_e
    source_t_g = gauge_t * source_t
    readout_e_g = readout_e / gauge_e
    readout_t_g = readout_t / gauge_t
    check(
        "channelwise source/readout gauge leaves products Q_X=S_X R_X invariant",
        source_e_g * readout_e_g == product_e and source_t_g * readout_t_g == product_t,
        f"Q_E={product_e}, Q_T={product_t}",
    )
    check(
        "the same gauge changes source/readout attribution while preserving endpoint products",
        (source_e_g / source_t_g) != (source_e / source_t)
        and (readout_e_g / readout_t_g) != (readout_e / readout_t),
        f"source ratio {source_e/source_t}->{source_e_g/source_t_g}; "
        f"readout ratio {readout_e/readout_t}->{readout_e_g/readout_t_g}",
    )

    print("\n-- Current-surface guards --")
    readout_note = normalized_text("docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    source_note = normalized_text("docs/QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md")
    prototype_note = normalized_text("docs/S3_TIME_TENSOR_PRIMITIVE_PROTOTYPE_NOTE.md")
    bilinear_note = normalized_text("docs/S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md")
    new_note = normalized_text("docs/QUARK_ROUTE2_SOURCE_READOUT_FACTORIZATION_GAUGE_NO_GO_NOTE_2026-06-21.md")

    check(
        "exact readout map exposes P_R and algebraic endpoint ratios, not source/readout legs",
        "P_R = [[alpha_E, 0, beta_E, 0]," in readout_note
        and "Once the readout is reduced to `P_R`, the endpoint ratios are algebraic:" in readout_note,
    )
    check(
        "source-domain note names the missing bridge as an extra source/readout rule",
        "There is no current typed edge" in source_note
        and "an extra source/readout rule" in source_note,
    )
    check(
        "current tensor primitive notes do not define Riesz or dual-normalized leg observables",
        "Riesz" not in prototype_note
        and "dual-normalized" not in prototype_note
        and "Riesz" not in bilinear_note
        and "dual-normalized" not in bilinear_note,
    )
    check(
        "prototype and bilinear notes remain definition/input-boundary surfaces",
        "derive the named inputs themselves" in prototype_note
        and "class-A definition only" in bilinear_note
        and "physical tensor primitive" in bilinear_note,
    )
    check(
        "new note records no-go status and forbids endpoint closure",
        "**Actual current-surface status:** no-go" in new_note
        and "does not derive `rho_E = 21/4`" in new_note
        and "does not claim a unique exact `Theta_R -> Lambda_R` theorem" in new_note,
    )
    check(
        "new note states the exact remaining target as a leg-level gauge-fixing primitive",
        "derive a leg-level factorization primitive that fixes source/readout gauges" in new_note,
    )
    check(
        "forbidden proof inputs remain excluded",
        "No observed masses, fitted targets, PDG values, nearest-rational selection, or live endpoint fit is used." in new_note,
    )

    print("\n" + "=" * 84)
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "\nVERDICT: no-go. Product-level endpoint/readout algebra fixes only total reciprocal\n"
        "degree two. It cannot certify the source/readout split or two independent dual legs\n"
        "without an additional leg-level factorization primitive that fixes the channel gauges."
    )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
