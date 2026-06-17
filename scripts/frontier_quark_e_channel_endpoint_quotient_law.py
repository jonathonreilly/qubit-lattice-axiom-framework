#!/usr/bin/env python3
"""
Bounded endpoint-quotient law candidate for the remaining E-channel quark
readout primitive.

Status:
  theory-first bounded derivation candidate on top of the exact endpoint
  readout reduction

Safe claim:
  The live support/tensor stack still does not derive the E-channel readout
  ratio `r_E = b_E / a_E` exactly.

  But the current endpoint structure is now rigid enough to support a sharper
  theory-first candidate:

    1. exact endpoint algebra rewrites `r_E` in terms of the shell/center
       quotient `gamma_E(center) / gamma_E(shell)`;
    2. the T-channel quotient already sits on the exact-support candidate
       `5/6`, which implies `r_T = -1`;
    3. inside a controlled low-rational endpoint class, the nearest E-channel
       shell/center quotient is `15/8`, implying `r_E = 21/4`;
    4. combined with the live shell-multiplicity candidate `a_T / a_E = -2`,
       this gives a bounded anchored denominator candidate `D_E = 21/8`.

  This does not prove a theorem-grade law. It does build a concrete
  endpoint-derived candidate that is closer to the live anchored denominator
  than the older direct `sqrt(7)` proxy.
"""

from __future__ import annotations


# Heavy compute / sweep runner — `AUDIT_TIMEOUT_SEC = 1800`
# means the audit-lane precompute and live audit runner allow up to
# 30 min of wall time before recording a timeout. The 120 s default
# ceiling is too tight under concurrency contention; see
# `docs/audit/RUNNER_CACHE_POLICY.md`.
AUDIT_TIMEOUT_SEC = 1800

import math
from dataclasses import dataclass
from pathlib import Path

from frontier_quark_endpoint_readout_constraints import endpoint_readout
from frontier_quark_projector_parameter_audit import solve_anchored_surface
from frontier_quark_up_amplitude_candidate_scan import evaluate_candidate

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PARENT_NOTE = DOCS / "QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md"
SCOPE_NARROW_NOTE = DOCS / "QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_AUDITED_SCOPE_NARROW_BOUNDED_NOTE_2026-05-10.md"
NATURALITY_NO_GO_NOTE = DOCS / "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md"


PASS_COUNT = 0
FAIL_COUNT = 0

SMALL_RATIONAL_Q_MAX = 32
SMALL_RATIONAL_P_MAX = 96
LOW_TOL_PERCENT = 0.3


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


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


def part1_exact_endpoint_algebra() -> tuple[float, float, float, float]:
    print("\n" + "=" * 72)
    print("PART 1: Exact Endpoint Quotient Algebra")
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

    check(
        "The E-channel ratio is fixed exactly by the shell/center endpoint quotient",
        abs(r_e - 6.0 * (q_e - 1.0)) < 1.0e-12,
        f"residual = {abs(r_e - 6.0 * (q_e - 1.0)):.3e}",
    )
    check(
        "The T-channel ratio is fixed exactly by the shell/center endpoint quotient",
        abs(r_t - 6.0 * (q_t - 1.0)) < 1.0e-12,
        f"residual = {abs(r_t - 6.0 * (q_t - 1.0)):.3e}",
    )
    check(
        "The live T-channel endpoint quotient stays tightly near 5/6",
        percent_gap(q_t, 5.0 / 6.0) < 0.001,
        f"q_T = {q_t:.12f}, gap = {percent_gap(q_t, 5.0 / 6.0):.6f}%",
    )
    check(
        "The live T-channel quotient candidate 5/6 implies the known bounded T law r_T = -1",
        abs(6.0 * ((5.0 / 6.0) - 1.0) + 1.0) < 1.0e-12,
        "6 * (5/6 - 1) = -1 exactly",
    )

    return q_e, q_t, r_e, r_t


def part2_small_rational_e_candidate(q_e: float) -> RationalCandidate:
    print("\n" + "=" * 72)
    print("PART 2: Small-Rational E-Quotient Candidate")
    print("=" * 72)

    q_t_candidate = nearest_rational(5.0 / 6.0, 0.7, 1.0)
    q_e_candidate = nearest_rational(q_e, 1.6, 2.1)

    print(f"\n  controlled low-rational class:")
    print(f"    numerator <= {SMALL_RATIONAL_P_MAX}")
    print(f"    denominator <= {SMALL_RATIONAL_Q_MAX}")
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

    check(
        "The controlled T-channel rational scan recovers 5/6 exactly",
        q_t_candidate.numerator == 5 and q_t_candidate.denominator == 6,
        f"candidate = {q_t_candidate.label}",
    )
    check(
        "The controlled E-channel rational scan selects 15/8 as the nearest candidate",
        q_e_candidate.numerator == 15 and q_e_candidate.denominator == 8,
        f"candidate = {q_e_candidate.label}",
    )
    check(
        "The bounded 15/8 E-channel quotient candidate stays within 0.1% of the live quotient",
        q_e_candidate.rel_gap_percent < 0.1,
        f"gap = {q_e_candidate.rel_gap_percent:.6f}%",
    )

    return q_e_candidate


def part3_implied_e_ratio_law(q_e_candidate: RationalCandidate, r_e_live: float, r_t_live: float) -> tuple[float, float]:
    print("\n" + "=" * 72)
    print("PART 3: Implied E-Channel Ratio Law")
    print("=" * 72)

    r_e_candidate = 6.0 * (q_e_candidate.value - 1.0)
    d_candidate = r_e_candidate / 2.0
    d_live = abs(endpoint_readout().ratio_be_bt_abs)

    print(f"\n  candidate shell/center quotient   q_E = {q_e_candidate.label} = {q_e_candidate.value:.12f}")
    print(f"  implied E-channel ratio           r_E = 6 * ({q_e_candidate.label} - 1) = {r_e_candidate:.12f}")
    print(f"  live E-channel ratio              r_E(live) = {r_e_live:.12f}")
    print()
    print("  shell-multiplicity bridge candidate:")
    print("    a_T / a_E = -2")
    print("    r_T       = -1")
    print("    => |b_E / b_T| = r_E / 2")
    print(f"  implied anchored denominator      D_E = r_E / 2 = {d_candidate:.12f}")
    print(f"  live bounded anchored denominator D_live       = {d_live:.12f}")

    check(
        "The bounded E-channel ratio candidate implies the clean exact law r_E = 21/4",
        abs(r_e_candidate - 21.0 / 4.0) < 1.0e-12,
        f"candidate = {r_e_candidate:.12f}",
    )
    check(
        "The live shell/intercept ratio still stays near the theory-first shell multiplicity candidate a_T/a_E = -2",
        percent_gap(abs(endpoint_readout().ratio_at_ae), 2.0) < LOW_TOL_PERCENT,
        f"|a_T/a_E| gap = {percent_gap(abs(endpoint_readout().ratio_at_ae), 2.0):.6f}%",
    )
    check(
        "The implied anchored denominator candidate is the clean exact law D_E = 21/8",
        abs(d_candidate - 21.0 / 8.0) < 1.0e-12,
        f"candidate = {d_candidate:.12f}",
    )
    check(
        "The rationalized denominator 21/8 sits closer to the live bounded denominator than the older sqrt(7) proxy",
        percent_gap(d_candidate, d_live) < percent_gap(math.sqrt(7.0), d_live),
        (
            f"gap(21/8) = {percent_gap(d_candidate, d_live):.6f}%, "
            f"gap(sqrt7) = {percent_gap(math.sqrt(7.0), d_live):.6f}%"
        ),
    )
    check(
        "The implied E-law ratio stays within 0.2% of the live E-channel ratio",
        percent_gap(r_e_candidate, r_e_live) < 0.2,
        f"gap = {percent_gap(r_e_candidate, r_e_live):.6f}%",
    )
    check(
        "The live T-channel ratio remains compatible with the exact-support law r_T = -1",
        percent_gap(abs(r_t_live), 1.0) < 0.01,
        f"|r_T| gap = {percent_gap(abs(r_t_live), 1.0):.6f}%",
    )

    return r_e_candidate, d_candidate


def part4_quark_anchored_candidate(d_candidate: float) -> None:
    print("\n" + "=" * 72)
    print("PART 4: Quark Anchored Denominator Candidate")
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

    print(f"\n  exact-support anchored solve       a_u* = {anchored.amp_u:.12f}")
    print(f"  candidate denominator             D_E  = {d_candidate:.12f}")
    print(f"  candidate amplitude               a_u  = {a_u_candidate:.12f}")
    print(f"  live bounded endpoint amplitude   a_u  = {a_u_live:.12f}")
    print(f"  direct sqrt(7) proxy amplitude    a_u  = {a_u_sqrt7:.12f}")
    print()
    print(
        f"  candidate anchored aggregate      = {cand_eval.anchor_aggregate:.6f}%"
        f"  (max = {cand_eval.anchor_max:.6f}%, fast replay skips non-load-bearing refit)"
    )
    print(
        f"  live bounded anchored aggregate   = {live_eval.anchor_aggregate:.6f}%"
        f"  (max = {live_eval.anchor_max:.6f}%, fast replay skips non-load-bearing refit)"
    )
    print(
        f"  direct sqrt(7) anchored aggregate = {sqrt7_eval.anchor_aggregate:.6f}%"
        f"  (max = {sqrt7_eval.anchor_max:.6f}%, fast replay skips non-load-bearing refit)"
    )

    check(
        "The rationalized denominator candidate 21/8 keeps the anchored CKM+J package below 1%",
        cand_eval.anchor_max < 1.0,
        f"anchor max = {cand_eval.anchor_max:.6f}%",
    )
    check(
        "The rationalized denominator candidate stays within 0.2% of the live bounded anchored amplitude",
        percent_gap(a_u_candidate, a_u_live) < 0.2,
        f"gap = {percent_gap(a_u_candidate, a_u_live):.6f}%",
    )
    check(
        "The candidate 21/8 anchored quality remains essentially on the same branch as the live bounded endpoint law",
        abs(cand_eval.anchor_aggregate - live_eval.anchor_aggregate) < 0.01,
        (
            f"candidate = {cand_eval.anchor_aggregate:.6f}%, "
            f"live = {live_eval.anchor_aggregate:.6f}%"
        ),
    )


def part5_audit_traceability() -> None:
    print("\n" + "=" * 72)
    print("PART 5: Audit Traceability Cross-References")
    print("=" * 72)

    parent_text = PARENT_NOTE.read_text()
    scope_narrow_text = SCOPE_NARROW_NOTE.read_text()
    no_go_text = NATURALITY_NO_GO_NOTE.read_text()

    print(f"\n  parent note:        {PARENT_NOTE.name}")
    print(f"  scope-narrow note:  {SCOPE_NARROW_NOTE.name}")
    print(f"  naturality no-go:   {NATURALITY_NO_GO_NOTE.name}")

    check(
        "the parent note exposes its 2026-05-05 audit verdict as audited_numerical_match (class G)",
        "audited_numerical_match" in parent_text and "class G" in parent_text,
        "verdict and class are surfaced in the parent note's audit-traceability section",
    )
    check(
        "the parent note names both missing bridge theorems flagged by the audit re-audit guidance",
        "gamma_E(center)/gamma_E(shell) = 15/8" in parent_text
        and "a_T/a_E = -2" in parent_text
        and "missing_bridge_theorem" in parent_text,
        "both 15/8 and a_T/a_E=-2 missing-bridge-theorem entries appear in the parent note",
    )
    check(
        "the parent note cross-references the 2026-05-10 audited-scope-narrowing companion",
        "QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_AUDITED_SCOPE_NARROW_BOUNDED_NOTE_2026-05-10.md" in parent_text,
        "scope-narrow companion is reachable from the parent note",
    )
    check(
        "the parent note cross-references the retained Route-2 E-channel naturality no-go",
        "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md" in parent_text,
        "the retained_no_go authority is named explicitly",
    )
    check(
        "the retained naturality no-go states the conditional non-uniqueness it bounds",
        "rho_E" in no_go_text
        and "remains a free parameter" in no_go_text
        and ("21/4" in no_go_text or "rho_E = 21/4" in no_go_text),
        "the no-go names rho_E as a free parameter under the granted T-side conditions",
    )
    check(
        "the scope-narrowing companion is internally consistent with the parent note's two missing-bridge names",
        "gamma_E(center) / gamma_E(shell) = 15/8" in scope_narrow_text
        and "a_T / a_E = -2" in scope_narrow_text,
        "both missing bridges appear in the companion as well",
    )


def main() -> int:
    print("Quark E-channel endpoint quotient law")
    print("=" * 72)

    q_e, _q_t, r_e, r_t = part1_exact_endpoint_algebra()
    q_e_candidate = part2_small_rational_e_candidate(q_e)
    _r_e_candidate, d_candidate = part3_implied_e_ratio_law(q_e_candidate, r_e, r_t)
    part4_quark_anchored_candidate(d_candidate)
    part5_audit_traceability()

    print("\nVerdict:")
    print(
        "The exact endpoint reduction now supports one new theory-first bounded "
        "law candidate. The open E-channel primitive can be rewritten as the "
        "shell/center quotient gamma_E(center)/gamma_E(shell), and inside a "
        "controlled low-rational endpoint class that quotient is best "
        "rationalized by 15/8. That implies the exact bounded ratio law "
        "r_E = 21/4 and, under the live shell-multiplicity candidate "
        "a_T/a_E = -2 together with the exact-support T law r_T = -1, the "
        "anchored denominator candidate D_E = 21/8. This lands on the same "
        "anchored quark branch as the live bounded endpoint solve. It is a "
        "new bounded derivation candidate, not yet a theorem. The bounded "
        "status is anchored to the retained Route-2 E-channel readout "
        "naturality no-go (2026-04-28, audited_clean), which proves that the "
        "exact restricted carrier class plus the granted T-side conditions "
        "do not force rho_E = 21/4: an additional E-center primitive is "
        "required before the 15/8 identification can become a derivation."
    )

    print("\n" + "=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
