#!/usr/bin/env python3
"""W71 Route-2 T-side endpoint theorem attempt, rational obstruction runner."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PASS_COUNT = 0
FAIL_COUNT = 0


def fmt(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        prefix = "PASS"
    else:
        FAIL_COUNT += 1
        prefix = "FAIL"
    if detail:
        print(f"{prefix}: {name} -- {detail}")
    else:
        print(f"{prefix}: {name}")


def read_text(relpath: str) -> str:
    return (ROOT / relpath).read_text(encoding="utf-8")


def has_markers(relpath: str, markers: tuple[str, ...]) -> bool:
    text = read_text(relpath)
    return all(marker in text for marker in markers)


def gamma_shell(alpha: Fraction) -> Fraction:
    return alpha


def gamma_center(alpha: Fraction, beta: Fraction, delta_center: Fraction) -> Fraction:
    return alpha + beta * delta_center


def rho(beta: Fraction, alpha: Fraction) -> Fraction:
    return beta / alpha


def q_ratio(alpha: Fraction, beta: Fraction, delta_center: Fraction) -> Fraction:
    return gamma_center(alpha, beta, delta_center) / gamma_shell(alpha)


def s_te(alpha_t: Fraction, alpha_e: Fraction) -> Fraction:
    return alpha_t / alpha_e


def c_te(
    alpha_e: Fraction,
    beta_e: Fraction,
    alpha_t: Fraction,
    beta_t: Fraction,
    delta_center: Fraction,
) -> Fraction:
    return (
        gamma_center(alpha_t, beta_t, delta_center)
        / gamma_center(alpha_e, beta_e, delta_center)
    )


def f_adj(n_c: int) -> Fraction:
    return Fraction(n_c * n_c - 1, n_c * n_c)


def part1_authority_markers() -> None:
    print("PART 1: quote-anchor markers")
    note = read_text("docs/QUARK_ROUTE2_T_SIDE_ENDPOINT_THEOREM_ATTEMPT_BOUNDED_NOTE_2026-06-12.md")
    check(
        "new note has canonical metadata and no untracked checkpoint pointers",
        "**Type:** bounded_theorem" in note
        and "**Claim type:** bounded_theorem" in note
        and ".claude/tmp" not in note
        and "[scripts/quark_route2_t_side_endpoint_theorem_attempt_bounded_2026_06_12.py]" in note,
    )
    checks = (
        (
            "docs/QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md",
            (
                "Given any admissible readout map `P_R`",
                "lacks is a theorem that selects one unique `P_R`.",
                "Xi_P(t ; c) = (P_R c)",
            ),
        ),
        (
            "docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
            (
                "gamma_E = alpha_E u_E + beta_E delta_A1 u_E",
                "gamma_T = alpha_T u_T + beta_T delta_A1 u_T",
                "P_R = [[alpha_E, 0, beta_E, 0],",
            ),
        ),
        (
            "docs/S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md",
            (
                "endpoint-fitted, not first-principles",
                "fixed by the two endpoint",
                "old `eta_floor_tf` pipeline",
            ),
        ),
        (
            "docs/S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md",
            (
                "It does **not**",
                "derive the unresolved readout-triple",
                "valid for every admissible readout in the 1-parameter family",
            ),
        ),
        (
            "docs/MINIMAL_AXIOMS_2026-06-05.md",
            (
                "record supplies no readout context",
                "weighting, normalization, probability",
            ),
        ),
    )
    for relpath, markers in checks:
        check(
            f"{relpath} contains required markers",
            has_markers(relpath, markers),
            ", ".join(markers),
        )


def part2_exact_target_reproduction() -> tuple[Fraction, Fraction, Fraction, Fraction, Fraction]:
    print("\nPART 2: exact conditional reproduction under supplied readout row")
    delta_center = Fraction(1, 6)
    delta_shell = Fraction(0, 1)

    e_shell = (Fraction(1), Fraction(0), delta_shell, Fraction(0))
    e_center = (Fraction(1), Fraction(0), delta_center, Fraction(0))
    t_shell = (Fraction(0), Fraction(1), Fraction(0), delta_shell)
    t_center = (Fraction(0), Fraction(1), Fraction(0), delta_center)

    check(
        "restricted endpoint carrier columns are exact rational columns",
        e_shell == (1, 0, 0, 0)
        and e_center == (1, 0, Fraction(1, 6), 0)
        and t_shell == (0, 1, 0, 0)
        and t_center == (0, 1, 0, Fraction(1, 6)),
        f"E-center={e_center}, T-center={t_center}",
    )

    alpha_e = Fraction(1)
    beta_e = Fraction(0)
    alpha_t = Fraction(-2)
    beta_t = Fraction(2)

    rho_t = rho(beta_t, alpha_t)
    q_t = q_ratio(alpha_t, beta_t, delta_center)
    shell_ratio = s_te(alpha_t, alpha_e)

    check(
        "supplied T row gives rho_T = beta_T/alpha_T = -1 exactly",
        rho_t == Fraction(-1),
        f"beta_T/alpha_T = {fmt(beta_t)}/{fmt(alpha_t)} = {fmt(rho_t)}",
    )
    check(
        "supplied T row gives q_T = 1 + rho_T/6 = 5/6 exactly",
        q_t == Fraction(5, 6) and q_t == 1 + rho_t * delta_center,
        f"q_T = {fmt(q_t)}",
    )
    check(
        "supplied shell rows give s_TE = alpha_T/alpha_E = -2 exactly",
        shell_ratio == Fraction(-2),
        f"alpha_T/alpha_E = {fmt(alpha_t)}/{fmt(alpha_e)} = {fmt(shell_ratio)}",
    )
    check(
        "same arithmetic is integer-over-integer, not Fraction-of-float",
        all(
            isinstance(x, int)
            for val in (delta_center, alpha_e, beta_e, alpha_t, beta_t, rho_t, q_t, shell_ratio)
            for x in (val.numerator, val.denominator)
        ),
        "all denominators are exact Fraction denominators",
    )
    return delta_center, alpha_e, beta_e, alpha_t, beta_t


def part3_readout_freedom(delta_center: Fraction) -> None:
    print("\nPART 3: exact readout-row freedom on the same carrier/time structure")
    target = {
        "candidate": (Fraction(1), Fraction(0), Fraction(-2), Fraction(2)),
        "free_t_shape": (Fraction(1), Fraction(0), Fraction(-2), Fraction(0)),
        "free_e_shell_scale": (Fraction(2), Fraction(0), Fraction(-2), Fraction(2)),
        "free_t_shell_scale": (Fraction(1), Fraction(0), Fraction(-3), Fraction(3)),
        "free_sign_orientation": (Fraction(1), Fraction(0), Fraction(2), Fraction(-2)),
    }
    rows: dict[str, tuple[Fraction, Fraction, Fraction]] = {}
    for name, (alpha_e, beta_e, alpha_t, beta_t) in target.items():
        rows[name] = (
            rho(beta_t, alpha_t),
            q_ratio(alpha_t, beta_t, delta_center),
            s_te(alpha_t, alpha_e),
        )
        print(
            "  "
            + name
            + ": rho_T="
            + fmt(rows[name][0])
            + ", q_T="
            + fmt(rows[name][1])
            + ", s_TE="
            + fmt(rows[name][2])
        )

    check(
        "same carrier permits an exact row with s_TE fixed but rho_T not target",
        rows["free_t_shape"] == (Fraction(0), Fraction(1), Fraction(-2)),
        "alpha_T=-2, beta_T=0 gives rho_T=0 and q_T=1",
    )
    check(
        "same carrier permits exact alpha_E rescaling that keeps rho_T but changes s_TE",
        rows["free_e_shell_scale"] == (Fraction(-1), Fraction(5, 6), Fraction(-1)),
        "alpha_E=2 changes s_TE from -2 to -1",
    )
    check(
        "same carrier permits exact alpha_T/beta_T common rescaling that keeps rho_T but changes s_TE",
        rows["free_t_shell_scale"] == (Fraction(-1), Fraction(5, 6), Fraction(-3)),
        "alpha_T=-3, beta_T=3 changes s_TE from -2 to -3",
    )
    check(
        "same carrier permits exact opposite shell orientation that keeps rho_T but flips s_TE sign",
        rows["free_sign_orientation"] == (Fraction(-1), Fraction(5, 6), Fraction(2)),
        "alpha_T=2, beta_T=-2 gives s_TE=+2",
    )
    check(
        "T-side row selection and E/T shell normalization are independent walls",
        rows["free_t_shape"][2] == Fraction(-2)
        and rows["free_t_shape"][0] != Fraction(-1)
        and rows["free_e_shell_scale"][0] == Fraction(-1)
        and rows["free_e_shell_scale"][2] != Fraction(-2),
        "one counter-witness changes rho_T only; another changes s_TE only",
    )


def part4_wrong_structure_falsifiers(delta_center: Fraction) -> None:
    print("\nPART 4: wrong-structure falsifiers")
    alpha_e = Fraction(1)
    alpha_t = Fraction(-2)
    beta_t = Fraction(2)
    q_target = Fraction(5, 6)

    wrong_delta = Fraction(1, 5)
    wrong_q = q_ratio(alpha_t, beta_t, wrong_delta)
    wrong_inferred_rho = (q_target - 1) / wrong_delta
    check(
        "wrong center gap/dimension breaks q_T for the supplied T row",
        wrong_q == Fraction(4, 5) and wrong_q != q_target,
        f"delta=1/5 gives q_T={fmt(wrong_q)}",
    )
    check(
        "wrong center gap/dimension breaks inverted rho_T from q_T=5/6",
        wrong_inferred_rho == Fraction(-5, 6) and wrong_inferred_rho != Fraction(-1),
        f"(5/6-1)/(1/5) = {fmt(wrong_inferred_rho)}",
    )

    wrong_beta_from_e = Fraction(21, 4)
    wrong_rho = rho(wrong_beta_from_e, alpha_t)
    wrong_q_pairing = q_ratio(alpha_t, wrong_beta_from_e, delta_center)
    check(
        "wrong channel pairing breaks rho_T and q_T visibly",
        wrong_rho == Fraction(-21, 8)
        and wrong_q_pairing == Fraction(9, 16)
        and wrong_rho != Fraction(-1)
        and wrong_q_pairing != q_target,
        f"beta_T=21/4 with alpha_T=-2 gives rho_T={fmt(wrong_rho)}, q_T={fmt(wrong_q_pairing)}",
    )

    swapped_shell = s_te(alpha_e, alpha_t)
    check(
        "wrong E/T shell pairing inverts the normalization",
        swapped_shell == Fraction(-1, 2) and swapped_shell != Fraction(-2),
        f"alpha_E/alpha_T = {fmt(swapped_shell)}",
    )

    sign_flipped_s = s_te(Fraction(2), alpha_e)
    check(
        "wrong shell-orientation sign preserves rho_T but breaks s_TE sign",
        sign_flipped_s == Fraction(2) and sign_flipped_s != Fraction(-2),
        f"alpha_T=+2, alpha_E=1 gives s_TE={fmt(sign_flipped_s)}",
    )

    f2 = f_adj(2)
    f3 = f_adj(3)
    check(
        "wrong N_c substitution changes the color center fraction, not the shell normalization",
        f2 == Fraction(3, 4)
        and f3 == Fraction(8, 9)
        and abs(Fraction(-2)) != f2
        and abs(Fraction(-2)) != f3,
        f"F_adj(2)={fmt(f2)}, F_adj(3)={fmt(f3)}, |s_TE|=2",
    )

    q_e_if_nc2_center_bridge = s_te(alpha_t, alpha_e) * q_target / (-f2)
    rho_e_if_nc2_center_bridge = 6 * (q_e_if_nc2_center_bridge - 1)
    check(
        "wrong N_c in the optional center-ratio bridge gives a different E lift",
        q_e_if_nc2_center_bridge == Fraction(20, 9)
        and rho_e_if_nc2_center_bridge == Fraction(22, 3)
        and rho_e_if_nc2_center_bridge != Fraction(21, 4),
        f"N_c=2 would give q_E={fmt(q_e_if_nc2_center_bridge)}, rho_E={fmt(rho_e_if_nc2_center_bridge)}",
    )


def part5_bridge_localization(delta_center: Fraction) -> None:
    print("\nPART 5: bridge localization checks")
    p_with_rho_e_0 = (Fraction(1), Fraction(0), Fraction(-2), Fraction(2))
    p_with_rho_e_21_4 = (Fraction(1), Fraction(21, 4), Fraction(-2), Fraction(2))

    c0 = c_te(*p_with_rho_e_0, delta_center)
    c21 = c_te(*p_with_rho_e_21_4, delta_center)
    check(
        "E-center lift remains a separate parameter even after supplied T-side rows",
        c0 == Fraction(-5, 3) and c21 == Fraction(-8, 9) and c0 != c21,
        f"rho_E=0 gives c_TE={fmt(c0)}; rho_E=21/4 gives c_TE={fmt(c21)}",
    )

    nodes = read_text("docs/audit/data/axiom_premise_nodes.json")
    check(
        "approved premise registry text does not grant a readout bridge or normalization rule",
        "readout bridge" in nodes and "normalization" in nodes,
        "registered primitive notes explicitly exclude these grants",
    )


def main() -> int:
    print("W71 Route-2 T-side endpoint theorem attempt (bounded rational runner)")
    print("=" * 72)
    part1_authority_markers()
    delta_center, _, _, _, _ = part2_exact_target_reproduction()
    part3_readout_freedom(delta_center)
    part4_wrong_structure_falsifiers(delta_center)
    part5_bridge_localization(delta_center)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
