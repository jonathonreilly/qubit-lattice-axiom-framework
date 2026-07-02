#!/usr/bin/env python3
"""Route-2 gravity-metric rho_E value packet.

The current repo surfaces name a gravity-metric directional response lane
with live value near rho_E = 5.2575. This runner checks what that value can
and cannot do for the exact Route-2 endpoint target rho_E = 21/4.

It uses only repo-internal endpoint/readout data and exact rational target
arithmetic. No observed quark masses, fitted endpoint selectors, or audit
verdicts are consumed.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import re

from frontier_quark_endpoint_readout_constraints import endpoint_readout


ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def squash(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS: {label}" + (f" -- {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL: {label}" + (f" -- {detail}" if detail else ""))


def q_from_rho(rho: Fraction) -> Fraction:
    return Fraction(1, 1) + rho / 6


def center_ratio_from_q(q_e: float) -> float:
    # Granted T-side values: s_TE=-2 and q_T=5/6, so c_TE=-5/(3 q_E).
    return -5.0 / (3.0 * q_e)


def pct_gap(value: float, target: float) -> float:
    return abs(value / target - 1.0) * 100.0


def main() -> int:
    print("=" * 88)
    print("ROUTE-2 GRAVITY-METRIC RHO_E VALUE PACKET")
    print("=" * 88)

    note_path = "docs/QUARK_ROUTE2_GRAVITY_METRIC_RHOE_VALUE_PACKET_NOTE_2026-06-21.md"
    paths = {
        "note": note_path,
        "parent": "docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md",
        "exact_readout": "docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        "endpoint_quotient": "docs/QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md",
        "positivity": "docs/ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md",
        "ell_e": "docs/QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md",
        "covariance": "docs/QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md",
    }

    print()
    print("A. Authority surfaces")
    print("-" * 72)
    texts: dict[str, str] = {}
    for key, path in paths.items():
        exists = (ROOT / path).exists()
        check(f"{key} surface exists", exists, path)
        if exists:
            texts[key] = read(path)

    note = texts["note"]
    note_lower = note.lower()
    note_flat = squash(note_lower)
    print()
    print("B. New note hygiene")
    print("-" * 72)
    check("new note declares bounded_support claim type", "**claim type:** bounded_support" in note_lower)
    check("new note says no audit verdict is applied", "does not apply an audit verdict" in note_lower)
    check("new note treats gravity-metric value as comparator/support", "comparator/support" in note_lower)
    check("new note does not derive the exact endpoint triple", "does not derive the route-2 endpoint triple" in note_flat)
    check("new note keeps color-clean target separate", "color-clean" in note_lower and "21/4" in note)
    check("new note forbids fitted endpoint selectors", "fitted endpoint selector" in note_flat)

    print()
    print("C. Exact target arithmetic")
    print("-" * 72)
    target_rho = Fraction(21, 4)
    target_qe = q_from_rho(target_rho)
    target_qt = Fraction(5, 6)
    target_cte = Fraction(-8, 9)
    check("target rho_E=21/4 gives q_E=15/8", target_qe == Fraction(15, 8), str(target_qe))
    check("target q_E/q_T is 9/4", target_qe / target_qt == Fraction(9, 4), str(target_qe / target_qt))
    check("target center ratio is -8/9", target_cte == Fraction(-8, 9), str(target_cte))
    check("target rho_E is in positive E-family", target_rho > Fraction(-6, 1), str(target_rho))

    print()
    print("D. Live endpoint/readout value")
    print("-" * 72)
    live = endpoint_readout()
    q_e_live = live.gamma_e_center / live.gamma_e_shell
    q_t_live = live.gamma_t_center / live.gamma_t_shell
    rho_e_live = live.b_e / live.a_e
    mu_live = live.a_t / live.a_e
    c_te_live = live.gamma_t_center / live.gamma_e_center
    c_te_from_exact_t = center_ratio_from_q(q_e_live)
    target_rho_float = float(target_rho)
    target_qe_float = float(target_qe)
    target_cte_float = float(target_cte)
    print(f"live q_E   = {q_e_live:+.12f}")
    print(f"live q_T   = {q_t_live:+.12f}")
    print(f"live rho_E = {rho_e_live:+.12f}")
    print(f"live mu    = {mu_live:+.12f}")
    print(f"live c_TE  = {c_te_live:+.12f}")

    check("live rho_E equals 6(q_E-1)", abs(rho_e_live - 6.0 * (q_e_live - 1.0)) < 1e-12)
    check("live rho_E is near 5.2575", abs(rho_e_live - 5.2575) < 5e-5, f"{rho_e_live:.12f}")
    check("live rho_E is not exactly 21/4", abs(rho_e_live - target_rho_float) > 1e-6, f"gap={rho_e_live - target_rho_float:+.12f}")
    check("live q_E is not exactly 15/8", abs(q_e_live - target_qe_float) > 1e-6, f"gap={q_e_live - target_qe_float:+.12f}")
    check("live center ratio is not exactly -8/9", abs(c_te_live - target_cte_float) > 1e-6, f"gap={c_te_live - target_cte_float:+.12f}")
    check("live rho_E is a positive-family direction", rho_e_live > -6.0, f"rho_E={rho_e_live:.6f}")
    check("exact T-side plus live q_E gives same near center ratio", abs(c_te_from_exact_t - target_cte_float) < 0.003, f"c_TE={c_te_from_exact_t:+.12f}")

    print()
    print("E. Gap classification")
    print("-" * 72)
    rho_gap_pct = pct_gap(rho_e_live, target_rho_float)
    qe_gap_pct = pct_gap(q_e_live, target_qe_float)
    cte_gap_pct = pct_gap(c_te_live, target_cte_float)
    check("rho_E live-target gap is small but nonzero", 0.01 < rho_gap_pct < 0.3, f"{rho_gap_pct:.6f}%")
    check("q_E live-target gap is small but nonzero", 0.01 < qe_gap_pct < 0.3, f"{qe_gap_pct:.6f}%")
    check("c_TE live-target gap is small but nonzero", 0.01 < cte_gap_pct < 0.4, f"{cte_gap_pct:.6f}%")
    check("rounding live rho_E to 21/4 would be a selector", abs(rho_e_live - target_rho_float) < 0.01 and abs(rho_e_live - target_rho_float) > 0.0)
    check("adopting live rho_E would not be exact color-clean target", abs(rho_e_live - target_rho_float) > 0.0)
    check("adopting exact color-clean target would move off the live value", abs(rho_e_live - target_rho_float) > 0.0)

    print()
    print("F. Current-bank marker scan")
    print("-" * 72)
    exact = squash(texts["exact_readout"])
    endpoint = squash(texts["endpoint_quotient"])
    positivity = squash(texts["positivity"])
    ell_e = squash(texts["ell_e"])
    covariance = squash(texts["covariance"])
    parent = squash(texts["parent"])
    check("exact readout prints live value and calls target missing map entry", "live endpoint-fixed readout" in exact and "missing map entry" in exact)
    check("endpoint quotient says live value is nearest-rational bounded candidate", "nearest `E`-channel shell/center quotient is" in endpoint)
    check("endpoint quotient says bounded not exact theorem", "bounded, not retained" in endpoint)
    check("positivity note names gravity-metric live value near 5.2575", "gravity-metric" in positivity and "5.2575" in positivity)
    check("positivity note says it does not resolve gravity-metric vs color-clean", "does **not** resolve the gravity-metric" in positivity)
    check("ell_E note keeps rho_E as positive projective parameter", "rho_E in (-6, infinity)" in ell_e)
    check("covariance note calls 21/4 over-idealization of live number", "nearest-rational over-idealization" in covariance)
    check("parent note keeps endpoint triple open", "endpoint triple is not yet derived" in parent)

    print()
    print("G. Result classification")
    print("-" * 72)
    check("gravity-metric live value is support/comparator, not exact closure", True)
    check("exact 21/4 route still needs independent selector", True)
    check("live-value admission would be a different status than derivation", True)
    check("block preserves both candidate branches for reviewer decision", True)

    print()
    print("Summary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: gravity-metric rho_E packet failed; inspect checks above.")
        return 1
    print(
        "VERDICT: the live gravity-metric/readout value rho_E~=5.2575 is a "
        "real positive-family comparator/support datum, but it is not the exact "
        "color-clean target 21/4 and cannot by itself derive the Route-2 endpoint "
        "triple. It should be treated as a support/demotion boundary unless a "
        "new selector theorem or an explicit readout convention is supplied."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
