#!/usr/bin/env python3
"""
Conditional bounded endpoint-ratio-chain theorem for the quark E-channel law.

Safe claim:
  The runner verifies exact endpoint-chain identities and exact conditional
  algebra under the named supplied premises ENDPOINT-QE, ENDPOINT-RT, and
  SHELL-MULT. It also replays the historical nearest-rational chain scan and
  anchored branch as motivation-tier evidence only. The scan does not supply,
  select, or derive any premise.
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

from frontier_quark_e_channel_endpoint_quotient_law import (
    anchored_a_u_from_denominator,
    fenced_block_after,
    percent_gap,
    section_body,
)
from frontier_quark_endpoint_readout_constraints import endpoint_readout
from frontier_quark_projector_parameter_audit import solve_anchored_surface
from frontier_quark_up_amplitude_candidate_scan import evaluate_candidate

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PARENT_NOTE = DOCS / "QUARK_ENDPOINT_RATIO_CHAIN_LAW_NOTE_2026-04-19.md"
NATURALITY_NO_GO_NOTE = (
    DOCS / "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md"
)
SCOPE_NARROW_NOTE = (
    DOCS
    / "QUARK_ENDPOINT_RATIO_CHAIN_LAW_AUDITED_SCOPE_NARROW_BOUNDED_NOTE_2026-05-10.md"
)


LOAD_PASS_COUNT = 0
LOAD_FAIL_COUNT = 0
MOTIVATION_PASS_COUNT = 0
MOTIVATION_FAIL_COUNT = 0
SMALL_Q_MAX = 32
SMALL_P_MAX = 96


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
    for q in range(1, SMALL_Q_MAX + 1):
        for p in range(-SMALL_P_MAX, SMALL_P_MAX + 1):
            if p == 0:
                continue
            g = math.gcd(abs(p), q)
            num = p // g
            den = q // g
            key = (num, den)
            if key in seen:
                continue
            seen.add(key)
            val = num / den
            if not (lower < val < upper):
                continue
            gap = percent_gap(val, value)
            cand = RationalCandidate(f"{num}/{den}", val, num, den, gap)
            if best is None or cand.rel_gap_percent < best.rel_gap_percent:
                best = cand
    assert best is not None
    return best


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


def local_check(name: str, condition: bool, detail: str = "") -> None:
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


def part1_exact_endpoint_chain_identity() -> tuple[float, float, float]:
    print("\n" + "=" * 72)
    print("PART 1: Exact Endpoint Chain Identity (Unconditional)")
    print("=" * 72)

    data = endpoint_readout()
    q_t = data.gamma_t_center / data.gamma_t_shell
    s_te = data.gamma_t_shell / data.gamma_e_shell
    c_te = data.gamma_t_center / data.gamma_e_center
    q_e = data.gamma_e_center / data.gamma_e_shell

    print(f"\n  gamma_T(center)/gamma_T(shell) = {q_t:.12f}")
    print(f"  gamma_T(shell)/gamma_E(shell)  = {s_te:.12f}")
    print(f"  gamma_T(center)/gamma_E(center)= {c_te:.12f}")
    print(f"  gamma_E(center)/gamma_E(shell) = {q_e:.12f}")
    print()
    print("  exact chain identity:")
    print("    gamma_E(center)/gamma_E(shell)")
    print("      = [gamma_E(center)/gamma_T(center)]")
    print("        * [gamma_T(center)/gamma_T(shell)]")
    print("        * [gamma_T(shell)/gamma_E(shell)]")

    chain_qe = (1.0 / c_te) * q_t * s_te

    motivation_check(
        "live replay: E quotient tracks the three-factor chain identity",
        abs(chain_qe - q_e) < 1.0e-12,
        f"residual = {abs(chain_qe - q_e):.3e}",
    )

    return q_t, s_te, c_te


def part2_motivation_tier_chain_scan(
    q_t: float,
    s_te: float,
    c_te: float,
) -> None:
    print("\n" + "=" * 72)
    print("PART 2: Motivation-Tier Small-Rational Chain Scan (Evidence Only)")
    print("=" * 72)

    t_cand = nearest_rational(q_t, 0.7, 1.0)
    shell_cand = nearest_rational(s_te, -3.0, -1.0)
    center_cand = nearest_rational(c_te, -1.2, -0.6)

    print("\n  evidence only; not load-bearing; no scan value is a premise")
    print(f"  controlled low-rational numerator <= {SMALL_P_MAX}")
    print(f"  controlled low-rational denominator <= {SMALL_Q_MAX}")
    print()
    print(
        f"  T endpoint candidate = {t_cand.label:>5s}"
        f" = {t_cand.value:+.12f}  gap = {t_cand.rel_gap_percent:.6f}%"
    )
    print(
        f"  shell T/E candidate  = {shell_cand.label:>5s}"
        f" = {shell_cand.value:+.12f}  gap = {shell_cand.rel_gap_percent:.6f}%"
    )
    print(
        f"  center T/E candidate = {center_cand.label:>5s}"
        f" = {center_cand.value:+.12f}  gap = {center_cand.rel_gap_percent:.6f}%"
    )

    motivation_check(
        "Motivation scan: the T endpoint scan recovers 5/6",
        (t_cand.numerator, t_cand.denominator) == (5, 6),
        f"candidate = {t_cand.label}",
    )
    motivation_check(
        "Motivation scan: the shell T/E scan selects -2",
        (shell_cand.numerator, shell_cand.denominator) == (-2, 1),
        f"candidate = {shell_cand.label}",
    )
    motivation_check(
        "Motivation scan: the center T/E scan selects -8/9",
        (center_cand.numerator, center_cand.denominator) == (-8, 9),
        f"candidate = {center_cand.label}",
    )
    motivation_check(
        "Motivation scan: shell and center T/E candidates stay within 0.3%",
        shell_cand.rel_gap_percent < 0.3 and center_cand.rel_gap_percent < 0.3,
        (
            f"shell gap = {shell_cand.rel_gap_percent:.6f}%, "
            f"center gap = {center_cand.rel_gap_percent:.6f}%"
        ),
    )
    motivation_check(
        "Motivation replay: T-chain factor remains near 5/6",
        percent_gap(q_t, 5.0 / 6.0) < 0.001,
        f"gap = {percent_gap(q_t, 5.0 / 6.0):.6f}%",
    )


def part3_conditional_exact_chain() -> float:
    print("\n" + "=" * 72)
    print("PART 3: Conditional Exact Chain Under Named Premises")
    print("=" * 72)

    q_t = Fraction(5, 6)
    shell_te = Fraction(-2, 1)
    center_te = Fraction(-8, 9)
    q_e = (1 / center_te) * q_t * shell_te
    r_e = 6 * (q_e - 1)
    r_t = 6 * (q_t - 1)
    d_e = r_e / (r_t * shell_te)

    print("\n  chain-leg mapping:")
    print("    5/6  maps to ENDPOINT-RT")
    print("    -2   maps to SHELL-MULT")
    print("    -8/9 maps to the ENDPOINT-QE equivalence")
    print()
    print(f"  q_E = (-9/8) * (5/6) * (-2) = {q_e}")
    print(f"  r_E = 6 * (15/8 - 1)        = {r_e}")
    print(f"  D_E = r_E/(r_T * a_T/a_E)   = {d_e}")

    local_check(
        "ENDPOINT-QE/RT/SHELL-MULT imply q_E = 15/8 exactly",
        q_e == Fraction(15, 8),
        f"chain = {q_e}",
    )
    local_check(
        "The conditional ratio chain implies r_E = 21/4 exactly",
        r_e == Fraction(21, 4),
        f"chain = {r_e}",
    )
    local_check(
        "ENDPOINT-RT conditionally implies r_T = -1 exactly",
        r_t == Fraction(-1, 1),
        f"chain = {r_t}",
    )
    local_check(
        "The conditional ratio chain implies D_E = 21/8 exactly",
        d_e == Fraction(21, 8),
        f"chain = {d_e}",
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
        local_check(
            f"P_R^prem maps {name} to the displayed endpoint image",
            images[name] == expected_images[name],
            f"image = {images[name]}",
        )

    q_e = images["E-center"][0] / images["E-shell"][0]
    q_t = images["T-center"][1] / images["T-shell"][1]
    s_te = images["T-shell"][1] / images["E-shell"][0]
    c_te_from_image_ratio = images["T-center"][1] / images["E-center"][0]
    c_te_from_chain = s_te * q_t / q_e

    local_check(
        "endpoint images recompute q_E = 15/8 independently",
        q_e == Fraction(15, 8),
        f"q_E = {q_e}",
    )
    local_check(
        "endpoint images recompute q_T = 5/6 independently",
        q_t == Fraction(5, 6),
        f"q_T = {q_t}",
    )
    local_check(
        "image-ratio route recomputes c_TE = -8/9",
        c_te_from_image_ratio == Fraction(-8, 9),
        f"c_TE = {c_te_from_image_ratio}",
    )
    local_check(
        "quotient-chain route recomputes c_TE = -8/9",
        c_te_from_chain == Fraction(-8, 9),
        f"s_TE*q_T/q_E = {c_te_from_chain}",
    )

    return images


def part5_motivation_tier_anchored_replay(d_chain: float) -> None:
    print("\n" + "=" * 72)
    print("PART 6: Motivation-Tier Anchored Replay (Evidence Only)")
    print("=" * 72)

    anchored = solve_anchored_surface()
    a_u_chain = anchored_a_u_from_denominator(d_chain)
    a_u_live = anchored_a_u_from_denominator(endpoint_readout().ratio_be_bt_abs)
    eval_chain = evaluate_candidate(
        "21/8",
        "ratio-chain",
        a_u_chain,
        anchored.r_uc,
        anchored.r_ct,
        run_refit=False,
    )
    eval_live = evaluate_candidate(
        "|b_E/b_T|",
        "bounded-endpoint",
        a_u_live,
        anchored.r_uc,
        anchored.r_ct,
        run_refit=False,
    )

    print("\n  evidence only; anchored replay is not load-bearing")
    print(f"  chain-implied amplitude      = {a_u_chain:.12f}")
    print(f"  live bounded amplitude       = {a_u_live:.12f}")
    print(
        f"  chain anchor aggregate       = {eval_chain.anchor_aggregate:.6f}%"
        f"  (max = {eval_chain.anchor_max:.6f}%)"
    )
    print(
        f"  live anchor aggregate        = {eval_live.anchor_aggregate:.6f}%"
        f"  (max = {eval_live.anchor_max:.6f}%)"
    )

    motivation_check(
        "Motivation replay: 21/8 keeps the anchored CKM+J package below 1%",
        eval_chain.anchor_max < 1.0,
        f"anchor max = {eval_chain.anchor_max:.6f}%",
    )
    motivation_check(
        "Motivation replay: chain amplitude stays within 0.01% of live endpoint",
        percent_gap(a_u_chain, a_u_live) < 0.01,
        f"gap = {percent_gap(a_u_chain, a_u_live):.6f}%",
    )
    motivation_check(
        "Motivation replay: chain branch is numerically indistinguishable",
        abs(eval_chain.anchor_aggregate - eval_live.anchor_aggregate) < 0.001,
        (
            f"chain = {eval_chain.anchor_aggregate:.6f}%, "
            f"live = {eval_live.anchor_aggregate:.6f}%"
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

    local_check(
        "the parent note advertises supported Type: bounded_theorem",
        "**Type:** bounded_theorem" in parent_text,
        "author hint uses the audit parser's supported Type header",
    )
    local_check(
        "the parent note defines ENDPOINT-QE as a named supplied premise",
        "E-channel center/shell endpoint" in parent_text
        and "rho_E = beta_E/alpha_E = 21/4" in parent_text
        and "rho_E is written r_E in the endpoint notes" in parent_text,
        "ENDPOINT-QE definition is present",
    )
    local_check(
        "the parent note defines ENDPOINT-RT as a named supplied premise",
        "T-channel center/shell endpoint" in parent_text
        and "r_T = beta_T/alpha_T = -1" in parent_text,
        "ENDPOINT-RT definition is present",
    )
    local_check(
        "the parent note defines SHELL-MULT as a named supplied premise",
        "the shell coefficient ratio" in parent_text
        and "a_T/a_E = alpha_T/alpha_E = -2" in parent_text,
        "SHELL-MULT definition is present",
    )
    local_check(
        "the parent note marks the no-go as used at its audited no-go scope",
        "used at its audited no-go scope" in parent_text,
        "no current no-go audit_status is asserted",
    )
    local_check(
        "the parent note does not assert a current no-go status marker",
        ("audited" + "_clean") not in parent_text,
        "no no-go status parenthetical remains",
    )
    local_check(
        "the parent note maps {5/6, -2, -8/9} to the named premises",
        "5/6  maps to ENDPOINT-RT" in parent_text
        and "-2   maps to SHELL-MULT" in parent_text
        and "-8/9 maps to the ENDPOINT-QE equivalence" in parent_text,
        "chain-leg mapping is explicit",
    )
    local_check(
        "the parent note displays the premise readout matrix",
        "P_R^prem = [[1, 0, 21/4, 0]," in parent_text
        and "[0, -2, 0, 2]]" in parent_text,
        "displayed matrix is present",
    )
    local_check(
        "the parent note displays all four carrier endpoint images",
        "E-shell  = (1, 0, 0, 0) -> (1, 0)" in parent_text
        and "E-center = (1, 0, 1/6, 0) -> (15/8, 0)" in parent_text
        and "T-shell  = (0, 1, 0, 0) -> (0, -2)" in parent_text
        and "T-center = (0, 1, 0, 1/6) -> (0, -5/3)" in parent_text,
        "displayed images are present",
    )
    local_check(
        "the parent note quotes Section 6 of the no-go verbatim",
        fenced_block_after(parent_text, "Section 6 of the no-go note, quoted verbatim:")
        == section_body(no_go_text, "## 6. Theorem", "## 7."),
        "parent quote matches the source theorem section",
    )
    local_check(
        "the parent note quotes the Section 4 equivalence trio verbatim",
        fenced_block_after(parent_text, "Section 4 of the no-go note, quoted verbatim:")
        == fenced_block_after(no_go_text, "The target value is equivalent"),
        "parent quote matches the source equivalence trio",
    )
    local_check(
        "the motivation exhibit labels all live values as evidence only",
        "Evidence only; not load-bearing; no value below is consumed by any claim"
        in parent_text,
        "motivation exhibit has the required firewall label",
    )
    local_check(
        "the parent note preserves the 2026-05-05 audited_numerical_match history",
        "audited_numerical_match" in parent_text and "class G" in parent_text,
        "audit verdict and class are surfaced",
    )
    local_check(
        "the parent note preserves the missing first-principles chain target",
        "endpoint_readout()" in parent_text
        and "first-principles derivation" in parent_text
        and "exact ratio chain" in parent_text,
        "re-audit target is preserved",
    )
    local_check(
        "the parent note links the 2026-05-10 scope-narrow companion",
        "[QUARK_ENDPOINT_RATIO_CHAIN_LAW_AUDITED_SCOPE_NARROW_BOUNDED_NOTE_2026-05-10.md]"
        in parent_text,
        "scope-narrow companion is a markdown link",
    )
    local_check(
        "the parent note links the Route-2 naturality no-go",
        "[QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md]"
        "(QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md)"
        in parent_text,
        "no-go authority is an inline markdown link outside the premise block",
    )
    local_check(
        "the naturality no-go states the non-uniqueness boundary",
        "rho_E" in no_go_text
        and "remains a free parameter" in no_go_text
        and "21/4" in no_go_text,
        "the no-go keeps rho_E free under granted T-side conditions",
    )
    local_check(
        "the 2026-05-10 scope-narrow companion exists",
        SCOPE_NARROW_NOTE.exists(),
        str(SCOPE_NARROW_NOTE.relative_to(ROOT)),
    )
    local_check(
        "the scope-narrow companion records all three chain legs",
        "5/6" in scope_text and "-2" in scope_text and "-8/9" in scope_text,
        "companion content needle is present",
    )
    local_check(
        "the parent note forbids citing named premises as derived",
        "The named premises may not be cited as derived." in parent_text,
        "premise firewall is explicit",
    )


def main() -> int:
    print("Quark endpoint ratio-chain law")
    print("=" * 72)

    q_t, s_te, c_te = part1_exact_endpoint_chain_identity()
    d_chain = part3_conditional_exact_chain()
    part4_premise_readout_matrix()
    part5_text_needles()
    print_motivation_banner()
    part2_motivation_tier_chain_scan(q_t, s_te, c_te)
    part5_motivation_tier_anchored_replay(d_chain)
    print_motivation_summary()

    print("\nDeclaration:")
    print("ENDPOINT-QE, ENDPOINT-RT, and SHELL-MULT are supplied premises.")
    print("This runner verifies only exact conditional chain algebra under those")
    print("premises plus the Route-2 no-go boundary used at its audited no-go scope.")
    print("It does not claim the premises or chain legs are derived, selected,")
    print("natural, or load-bearing from the motivation scan.")

    print("\n" + "=" * 72)
    print(f"TOTAL: PASS={LOAD_PASS_COUNT} FAIL={LOAD_FAIL_COUNT}")
    return 0 if LOAD_FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
