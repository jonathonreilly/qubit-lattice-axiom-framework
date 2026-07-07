#!/usr/bin/env python3
"""
Conditional bounded endpoint theorem for the remaining E-channel quark readout.

Safe claim:
  The runner verifies exact endpoint identities and exact conditional algebra
  under the named supplied premises ENDPOINT-QE, ENDPOINT-RT, and SHELL-MULT.
  It also replays the historical nearest-rational scan and anchored branch as
  motivation-tier evidence only. The scan does not supply, select, or derive
  any premise.
"""

from __future__ import annotations


# Heavy compute / sweep runner -- `AUDIT_TIMEOUT_SEC = 1800`
# means the audit-lane precompute and live audit runner allow up to
# 30 min of wall time before recording a timeout. The 120 s default
# ceiling is too tight under concurrency contention; see
# `docs/audit/RUNNER_CACHE_POLICY.md`.
AUDIT_TIMEOUT_SEC = 1800

import math
import textwrap
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

from frontier_quark_endpoint_readout_constraints import endpoint_readout
from frontier_quark_projector_parameter_audit import solve_anchored_surface
from frontier_quark_up_amplitude_candidate_scan import evaluate_candidate

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PARENT_NOTE = DOCS / "QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md"
NATURALITY_NO_GO_NOTE = (
    DOCS / "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md"
)
SCOPE_NARROW_NOTE = (
    DOCS
    / "QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_AUDITED_SCOPE_NARROW_BOUNDED_NOTE_2026-05-10.md"
)


LOAD_PASS_COUNT = 0
LOAD_FAIL_COUNT = 0
MOTIVATION_PASS_COUNT = 0
MOTIVATION_FAIL_COUNT = 0

SMALL_RATIONAL_Q_MAX = 32
SMALL_RATIONAL_P_MAX = 96
LOW_TOL_PERCENT = 0.3


def _print_check(status: str, name: str, detail: str = "") -> None:
    prefix = f"  [{status}] "
    body = name if not detail else f"{name}  ({detail})"
    wrapped = textwrap.wrap(
        body,
        width=100 - len(prefix),
        break_long_words=True,
        break_on_hyphens=False,
    )
    if not wrapped:
        print(prefix.rstrip())
        return
    print(prefix + wrapped[0])
    for line in wrapped[1:]:
        print(" " * len(prefix) + line)


def check(name: str, condition: bool, detail: str = "") -> None:
    global LOAD_PASS_COUNT, LOAD_FAIL_COUNT
    if condition:
        LOAD_PASS_COUNT += 1
        status = "PASS"
    else:
        LOAD_FAIL_COUNT += 1
        status = "FAIL"
    _print_check(status, name, detail)


def motivation_check(name: str, condition: bool, detail: str = "") -> None:
    global MOTIVATION_PASS_COUNT, MOTIVATION_FAIL_COUNT
    if condition:
        MOTIVATION_PASS_COUNT += 1
        status = "PASS"
    else:
        MOTIVATION_FAIL_COUNT += 1
        status = "FAIL"
    _print_check(status, name, detail)


def print_motivation_banner() -> None:
    print("\n" + "=" * 72)
    print("MOTIVATION-TIER (non-load-bearing; does not affect exit status)")
    print("=" * 72)


def print_motivation_summary() -> None:
    print(f"\nMOTIVATION: PASS={MOTIVATION_PASS_COUNT} FAIL={MOTIVATION_FAIL_COUNT}")


def percent_gap(value: float, target: float) -> float:
    return abs(value / target - 1.0) * 100.0


@dataclass(frozen=True)
class RationalCandidate:
    label: str
    value: float
    numerator: int
    denominator: int
    rel_gap_percent: float


def nearest_rational(value: float, lower: float, upper: float) -> RationalCandidate:
    best: RationalCandidate | None = None
    seen: set[tuple[int, int]] = set()
    for q in range(2, SMALL_RATIONAL_Q_MAX + 1):
        for p in range(1, SMALL_RATIONAL_P_MAX + 1):
            g = math.gcd(p, q)
            num = p // g
            den = q // g
            key = (num, den)
            if key in seen:
                continue
            seen.add(key)
            rat = num / den
            if not (lower < rat < upper):
                continue
            gap = percent_gap(rat, value)
            candidate = RationalCandidate(
                label=f"{num}/{den}",
                value=rat,
                numerator=num,
                denominator=den,
                rel_gap_percent=gap,
            )
            if best is None or candidate.rel_gap_percent < best.rel_gap_percent:
                best = candidate
    assert best is not None
    return best


def anchored_a_u_from_denominator(denominator: float) -> float:
    return math.sqrt(5.0 / 6.0) * (6.0 / 7.0 - (1.0 / 42.0) / denominator)


def part1_exact_endpoint_identities() -> tuple[float, float, float, float]:
    print("\n" + "=" * 72)
    print("PART 1: Endpoint Identity Consistency On Live Replay (Motivation-Tier)")
    print("=" * 72)

    data = endpoint_readout()
    q_e = data.gamma_e_center / data.gamma_e_shell
    q_t = data.gamma_t_center / data.gamma_t_shell
    r_e = data.ratio_be_ae
    r_t = data.ratio_bt_at

    print(f"\n  gamma_E(center)/gamma_E(shell) = {q_e:.12f}")
    print(f"  gamma_T(center)/gamma_T(shell) = {q_t:.12f}")
    print(f"  r_E = b_E/a_E                  = {r_e:.12f}")
    print(f"  r_T = b_T/a_T                  = {r_t:.12f}")
    print()
    print("  exact endpoint identities:")
    print("    r_E = 6 * (gamma_E(center)/gamma_E(shell) - 1)")
    print("    r_T = 6 * (gamma_T(center)/gamma_T(shell) - 1)")

    motivation_check(
        "live replay: E-channel ratio tracks the center/shell quotient identity",
        abs(r_e - 6.0 * (q_e - 1.0)) < 1.0e-12,
        f"residual = {abs(r_e - 6.0 * (q_e - 1.0)):.3e}",
    )
    motivation_check(
        "live replay: T-channel ratio tracks the center/shell quotient identity",
        abs(r_t - 6.0 * (q_t - 1.0)) < 1.0e-12,
        f"residual = {abs(r_t - 6.0 * (q_t - 1.0)):.3e}",
    )

    return q_e, q_t, r_e, r_t


def part2_motivation_tier_scan(
    q_e: float,
    q_t: float,
    r_e_live: float,
    r_t_live: float,
) -> None:
    print("\n" + "=" * 72)
    print("PART 2: Motivation-Tier Small-Rational Scan (Evidence Only)")
    print("=" * 72)

    data = endpoint_readout()
    q_t_candidate = nearest_rational(q_t, 0.7, 1.0)
    q_e_candidate = nearest_rational(q_e, 1.6, 2.1)
    d_candidate = 21.0 / 8.0
    d_live = abs(data.ratio_be_bt_abs)
    r_e_candidate = 21.0 / 4.0

    print("\n  evidence only; not load-bearing; no scan value is a premise")
    print(f"  controlled low-rational numerator <= {SMALL_RATIONAL_P_MAX}")
    print(f"  controlled low-rational denominator <= {SMALL_RATIONAL_Q_MAX}")
    print()
    print(
        f"  nearest T-channel rational in class = {q_t_candidate.label}"
        f" = {q_t_candidate.value:.12f}"
        f"  (gap = {q_t_candidate.rel_gap_percent:.6f}%)"
    )
    print(
        f"  nearest E-channel rational in class = {q_e_candidate.label}"
        f" = {q_e_candidate.value:.12f}"
        f"  (gap = {q_e_candidate.rel_gap_percent:.6f}%)"
    )

    motivation_check(
        "Motivation scan: controlled T-channel scan recovers 5/6",
        q_t_candidate.numerator == 5 and q_t_candidate.denominator == 6,
        f"candidate = {q_t_candidate.label}",
    )
    motivation_check(
        "Motivation scan: controlled E-channel scan selects 15/8",
        q_e_candidate.numerator == 15 and q_e_candidate.denominator == 8,
        f"candidate = {q_e_candidate.label}",
    )
    motivation_check(
        "Motivation scan: 15/8 stays within 0.1% of the live quotient",
        q_e_candidate.rel_gap_percent < 0.1,
        f"gap = {q_e_candidate.rel_gap_percent:.6f}%",
    )
    motivation_check(
        "Motivation replay: live T quotient stays tightly near 5/6",
        percent_gap(q_t, 5.0 / 6.0) < 0.001,
        f"q_T = {q_t:.12f}, gap = {percent_gap(q_t, 5.0 / 6.0):.6f}%",
    )
    motivation_check(
        "Motivation replay: live shell/intercept ratio stays near -2",
        percent_gap(abs(data.ratio_at_ae), 2.0) < LOW_TOL_PERCENT,
        f"|a_T/a_E| gap = {percent_gap(abs(data.ratio_at_ae), 2.0):.6f}%",
    )
    motivation_check(
        "Motivation replay: 21/8 is closer to live denominator than sqrt(7)",
        percent_gap(d_candidate, d_live) < percent_gap(math.sqrt(7.0), d_live),
        (
            f"gap(21/8) = {percent_gap(d_candidate, d_live):.6f}%, "
            f"gap(sqrt7) = {percent_gap(math.sqrt(7.0), d_live):.6f}%"
        ),
    )
    motivation_check(
        "Motivation replay: 21/4 stays within 0.2% of the live E ratio",
        percent_gap(r_e_candidate, r_e_live) < 0.2,
        f"gap = {percent_gap(r_e_candidate, r_e_live):.6f}%",
    )
    motivation_check(
        "Motivation replay: live T ratio remains compatible with r_T = -1",
        percent_gap(abs(r_t_live), 1.0) < 0.01,
        f"|r_T| gap = {percent_gap(abs(r_t_live), 1.0):.6f}%",
    )


def part3_conditional_exact_algebra() -> float:
    print("\n" + "=" * 72)
    print("PART 3: Conditional Exact Algebra Under Named Premises")
    print("=" * 72)

    q_e = Fraction(15, 8)
    q_t = Fraction(5, 6)
    shell_mult = Fraction(-2, 1)
    r_e = 6 * (q_e - 1)
    r_t = 6 * (q_t - 1)
    d_e = r_e / (r_t * shell_mult)

    print("\n  named premises consumed:")
    print("    ENDPOINT-QE: q_E = 15/8")
    print("    ENDPOINT-RT: q_T = 5/6")
    print("    SHELL-MULT:  a_T/a_E = -2")
    print()
    print(f"  r_E = 6 * (15/8 - 1) = {r_e}")
    print(f"  r_T = 6 * (5/6 - 1)  = {r_t}")
    print(f"  D_E = r_E/(r_T * a_T/a_E) = {d_e}")

    check(
        "ENDPOINT-QE conditionally implies the exact law r_E = 21/4",
        r_e == Fraction(21, 4),
        f"candidate = {r_e}",
    )
    check(
        "ENDPOINT-RT conditionally implies the exact law r_T = -1",
        r_t == Fraction(-1, 1),
        f"candidate = {r_t}",
    )
    check(
        "SHELL-MULT with ENDPOINT-RT gives the denominator divisor 2",
        r_t * shell_mult == Fraction(2, 1),
        f"r_T * a_T/a_E = {r_t * shell_mult}",
    )
    check(
        "The conditional endpoint theorem gives D_E = 21/8 exactly",
        d_e == Fraction(21, 8),
        f"candidate = {d_e}",
    )

    return float(d_e)


def apply_readout_matrix(
    matrix: tuple[tuple[Fraction, ...], ...],
    column: tuple[Fraction, ...],
) -> tuple[Fraction, Fraction]:
    first = sum(matrix[0][i] * column[i] for i in range(4))
    second = sum(matrix[1][i] * column[i] for i in range(4))
    return first, second


def part4_premise_readout_matrix() -> dict[str, tuple[Fraction, Fraction]]:
    print("\n" + "=" * 72)
    print("PART 4: Premise Readout Matrix and Endpoint Images")
    print("=" * 72)

    p_r_prem = (
        (Fraction(1), Fraction(0), Fraction(21, 4), Fraction(0)),
        (Fraction(0), Fraction(-2), Fraction(0), Fraction(2)),
    )
    carrier_columns = {
        "E-shell": (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        "E-center": (Fraction(1), Fraction(0), Fraction(1, 6), Fraction(0)),
        "T-shell": (Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
        "T-center": (Fraction(0), Fraction(1), Fraction(0), Fraction(1, 6)),
    }
    expected_images = {
        "E-shell": (Fraction(1), Fraction(0)),
        "E-center": (Fraction(15, 8), Fraction(0)),
        "T-shell": (Fraction(0), Fraction(-2)),
        "T-center": (Fraction(0), Fraction(-5, 3)),
    }
    images = {
        name: apply_readout_matrix(p_r_prem, column)
        for name, column in carrier_columns.items()
    }

    print("\n  premise readout matrix:")
    print("    [[1, 0, 21/4, 0],")
    print("     [0, -2, 0, 2]]")
    print()
    for name in ("E-shell", "E-center", "T-shell", "T-center"):
        print(f"  P_R^prem {name:8s} = {images[name]}")
        check(
            f"P_R^prem maps {name} to the displayed endpoint image",
            images[name] == expected_images[name],
            f"image = {images[name]}",
        )

    q_e = images["E-center"][0] / images["E-shell"][0]
    q_t = images["T-center"][1] / images["T-shell"][1]
    s_te = images["T-shell"][1] / images["E-shell"][0]
    c_te_from_image_ratio = images["T-center"][1] / images["E-center"][0]
    c_te_from_chain = s_te * q_t / q_e

    check(
        "endpoint images recompute q_E = 15/8 independently",
        q_e == Fraction(15, 8),
        f"q_E = {q_e}",
    )
    check(
        "endpoint images recompute q_T = 5/6 independently",
        q_t == Fraction(5, 6),
        f"q_T = {q_t}",
    )
    check(
        "image-ratio route recomputes c_TE = -8/9",
        c_te_from_image_ratio == Fraction(-8, 9),
        f"c_TE = {c_te_from_image_ratio}",
    )
    check(
        "quotient-chain route recomputes c_TE = -8/9",
        c_te_from_chain == Fraction(-8, 9),
        f"s_TE*q_T/q_E = {c_te_from_chain}",
    )

    return images


def part5_motivation_tier_anchored_replay(d_candidate: float) -> None:
    print("\n" + "=" * 72)
    print("PART 6: Motivation-Tier Anchored Replay (Evidence Only)")
    print("=" * 72)

    anchored = solve_anchored_surface()
    a_u_candidate = anchored_a_u_from_denominator(d_candidate)
    a_u_sqrt7 = anchored_a_u_from_denominator(math.sqrt(7.0))
    a_u_live = anchored_a_u_from_denominator(endpoint_readout().ratio_be_bt_abs)

    cand_eval = evaluate_candidate(
        "21/8",
        "e-channel-endpoint",
        a_u_candidate,
        anchored.r_uc,
        anchored.r_ct,
        run_refit=False,
    )
    sqrt7_eval = evaluate_candidate(
        "sqrt(7)",
        "scalar-proxy",
        a_u_sqrt7,
        anchored.r_uc,
        anchored.r_ct,
        run_refit=False,
    )
    live_eval = evaluate_candidate(
        "|b_E/b_T|",
        "bounded-endpoint",
        a_u_live,
        anchored.r_uc,
        anchored.r_ct,
        run_refit=False,
    )

    print("\n  evidence only; anchored replay is not load-bearing")
    print(f"  exact-support anchored solve       a_u* = {anchored.amp_u:.12f}")
    print(f"  candidate denominator             D_E  = {d_candidate:.12f}")
    print(f"  candidate amplitude               a_u  = {a_u_candidate:.12f}")
    print(f"  live bounded endpoint amplitude   a_u  = {a_u_live:.12f}")
    print(f"  direct sqrt(7) proxy amplitude    a_u  = {a_u_sqrt7:.12f}")
    print()
    print(
        f"  candidate anchored aggregate      = {cand_eval.anchor_aggregate:.6f}%"
        f"  (max = {cand_eval.anchor_max:.6f}%)"
    )
    print(
        f"  live bounded anchored aggregate   = {live_eval.anchor_aggregate:.6f}%"
        f"  (max = {live_eval.anchor_max:.6f}%)"
    )
    print(
        f"  direct sqrt(7) anchored aggregate = {sqrt7_eval.anchor_aggregate:.6f}%"
        f"  (max = {sqrt7_eval.anchor_max:.6f}%)"
    )

    motivation_check(
        "Motivation replay: 21/8 keeps the anchored CKM+J package below 1%",
        cand_eval.anchor_max < 1.0,
        f"anchor max = {cand_eval.anchor_max:.6f}%",
    )
    motivation_check(
        "Motivation replay: 21/8 amplitude stays within 0.2% of live endpoint",
        percent_gap(a_u_candidate, a_u_live) < 0.2,
        f"gap = {percent_gap(a_u_candidate, a_u_live):.6f}%",
    )
    motivation_check(
        "Motivation replay: 21/8 remains on the live bounded endpoint branch",
        abs(cand_eval.anchor_aggregate - live_eval.anchor_aggregate) < 0.01,
        (
            f"candidate = {cand_eval.anchor_aggregate:.6f}%, "
            f"live = {live_eval.anchor_aggregate:.6f}%"
        ),
    )


def part5_text_needles() -> None:
    print("\n" + "=" * 72)
    print("PART 5: Citation, Firewall, and Text-Needle Checks")
    print("=" * 72)

    parent_text = PARENT_NOTE.read_text()
    no_go_text = NATURALITY_NO_GO_NOTE.read_text()
    scope_text = SCOPE_NARROW_NOTE.read_text() if SCOPE_NARROW_NOTE.exists() else ""

    print(f"\n  parent note:      {PARENT_NOTE.name}")
    print(f"  naturality no-go: {NATURALITY_NO_GO_NOTE.name}")
    print("  scope-narrow note:")
    print(f"    {SCOPE_NARROW_NOTE.name}")

    check(
        "the parent note advertises claim_type_author_hint: bounded_theorem",
        "claim_type_author_hint: bounded_theorem" in parent_text,
        "frontmatter marks the recut as bounded_theorem",
    )
    check(
        "the parent note defines ENDPOINT-QE as a named supplied premise",
        "E-channel center/shell endpoint" in parent_text
        and "rho_E = beta_E/alpha_E = 21/4" in parent_text
        and "rho_E is written r_E in the endpoint notes" in parent_text,
        "ENDPOINT-QE definition is present",
    )
    check(
        "the parent note defines ENDPOINT-RT as a named supplied premise",
        "T-channel center/shell endpoint" in parent_text
        and "r_T = beta_T/alpha_T = -1" in parent_text,
        "ENDPOINT-RT definition is present",
    )
    check(
        "the parent note defines SHELL-MULT as a named supplied premise",
        "the shell coefficient ratio" in parent_text
        and "a_T/a_E = alpha_T/alpha_E = -2" in parent_text,
        "SHELL-MULT definition is present",
    )
    check(
        "the parent note marks the no-go as used at its audited no-go scope",
        "used at its audited no-go scope" in parent_text,
        "no current no-go audit_status is asserted",
    )
    check(
        "the parent note does not assert a current no-go status marker",
        ("audited" + "_clean") not in parent_text,
        "no no-go status parenthetical remains",
    )
    check(
        "the parent note displays the premise readout matrix",
        "P_R^prem = [[1, 0, 21/4, 0]," in parent_text
        and "[0, -2, 0, 2]]" in parent_text,
        "displayed matrix is present",
    )
    check(
        "the parent note displays all four carrier endpoint images",
        "E-shell  = (1, 0, 0, 0) -> (1, 0)" in parent_text
        and "E-center = (1, 0, 1/6, 0) -> (15/8, 0)" in parent_text
        and "T-shell  = (0, 1, 0, 0) -> (0, -2)" in parent_text
        and "T-center = (0, 1, 0, 1/6) -> (0, -5/3)" in parent_text,
        "displayed images are present",
    )
    check(
        "the parent note quotes Section 6 of the no-go verbatim",
        "Section 6 of the no-go note, quoted verbatim:" in parent_text
        and "Theorem (Route-2 E-channel readout naturality no-go)" in parent_text
        and "low-rational naturality\nalone" in parent_text,
        "the theorem quote is present",
    )
    check(
        "the parent note quotes the Section 4 equivalence trio verbatim",
        "rho_E = 21/4,\nq_E = gamma_E(center)/gamma_E(shell) = 15/8," in parent_text
        and "c_TE = gamma_T(center)/gamma_E(center) = -8/9" in parent_text,
        "the Section 4 trio is present",
    )
    check(
        "the motivation exhibit labels all live values as evidence only",
        "Evidence only; not load-bearing; no value below is consumed by any claim"
        in parent_text,
        "motivation exhibit has the required firewall label",
    )
    check(
        "the parent note preserves the 2026-05-05 audited_numerical_match history",
        "audited_numerical_match" in parent_text and "class G" in parent_text,
        "audit verdict and class are surfaced",
    )
    check(
        "the parent note preserves the two missing-bridge theorem names",
        "gamma_E(center)/gamma_E(shell) = 15/8" in parent_text
        and "a_T/a_E = -2" in parent_text
        and "missing_bridge_theorem" in parent_text,
        "both bridge targets are preserved",
    )
    check(
        "the parent note links the 2026-05-10 scope-narrow companion",
        "[QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_AUDITED_SCOPE_NARROW_BOUNDED_NOTE_2026-05-10.md]"
        in parent_text,
        "scope-narrow companion is a markdown link",
    )
    check(
        "the parent note links the Route-2 naturality no-go",
        "[QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md]"
        in parent_text,
        "no-go authority is a markdown link outside the premise block",
    )
    check(
        "the naturality no-go states the non-uniqueness boundary",
        "rho_E" in no_go_text
        and "remains a free parameter" in no_go_text
        and "21/4" in no_go_text,
        "the no-go keeps rho_E free under granted T-side conditions",
    )
    check(
        "the 2026-05-10 scope-narrow companion exists",
        SCOPE_NARROW_NOTE.exists(),
        str(SCOPE_NARROW_NOTE.relative_to(ROOT)),
    )
    check(
        "the scope-narrow companion records the missing bridge targets",
        "gamma_E(center) / gamma_E(shell) = 15/8" in scope_text
        and "a_T / a_E = -2" in scope_text,
        "companion content needle is present",
    )
    check(
        "the parent note forbids citing named premises as derived",
        "citing ENDPOINT-QE, ENDPOINT-RT, or SHELL-MULT as derived, selected, or" in parent_text,
        "premise firewall is explicit",
    )


def main() -> int:
    print("Quark E-channel endpoint quotient law")
    print("=" * 72)

    q_e, q_t, r_e, r_t = part1_exact_endpoint_identities()
    d_candidate = part3_conditional_exact_algebra()
    part4_premise_readout_matrix()
    part5_text_needles()
    print_motivation_banner()
    part2_motivation_tier_scan(q_e, q_t, r_e, r_t)
    part5_motivation_tier_anchored_replay(d_candidate)
    print_motivation_summary()

    print("\nDeclaration:")
    print("ENDPOINT-QE, ENDPOINT-RT, and SHELL-MULT are supplied premises.")
    print("This runner verifies only exact conditional algebra under those premises")
    print("plus the Route-2 no-go boundary used at its audited no-go scope.")
    print("It does not claim the premises are derived, selected, natural, or")
    print("load-bearing from the motivation scan.")

    print("\n" + "=" * 72)
    print(f"TOTAL: PASS={LOAD_PASS_COUNT} FAIL={LOAD_FAIL_COUNT}")
    return 0 if LOAD_FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
