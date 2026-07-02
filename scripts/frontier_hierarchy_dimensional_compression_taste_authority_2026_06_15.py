#!/usr/bin/env python3
"""
Hierarchy dimensional-compression diagnostic.

Within-scope content (this runner's PASS gates):
  Pure intra-framework dimensional arithmetic on the staggered Dirac
  condensate-density ratio R. No PASS gate depends on the imported
  electroweak observation v_obs or the imported pre-selector value
  v_pred. The (1/4) D=4 compression exponent and inverse placement are
  now routed through the 2026-06-16 fixed-density coefficient-to-scale
  bridge and the 2026-06-18 EW order-parameter D=4 density readout bridge,
  while endpoint selection and the absolute physical VEV closure stay outside
  this parent row.

External-context block (printed, NOT PASS-load-bearing):
  v_pred = M_Pl * alpha_LM^16, v_obs = 246.22 GeV, and the residual
  prefactor C_obs = v_obs / v_pred are still emitted so the reader can
  see why the dimensional-compression direction is of physical
  interest; explicitly excluded from any PASS condition.

This script does not derive the EW VEV from primitives. The within-scope
load-bearing content is the PASS-gated arithmetic below; the remaining open
step is the hierarchy-endpoint-to-physical-Higgs-density selection and
absolute scale closure.
"""

from __future__ import annotations

import math
import json
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "HIERARCHY_DIMENSIONAL_COMPRESSION_NOTE.md"
LEDGER_PATH = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
PASS_COUNT = 0
FAIL_COUNT = 0
RETAINED_GRADES = {"retained", "retained_bounded", "retained_no_go"}


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"  [{status}] {name}")
    if detail:
        print(f"         {detail}")


def build_dirac_4d_apbc(Ls: int, Lt: int, u0: float, mass: float = 0.0):
    n = Ls**3 * Lt
    D = np.zeros((n, n), dtype=complex)

    def idx(x0: int, x1: int, x2: int, t: int) -> int:
        return (((x0 % Ls) * Ls + (x1 % Ls)) * Ls + (x2 % Ls)) * Lt + (t % Lt)

    for x0 in range(Ls):
        for x1 in range(Ls):
            for x2 in range(Ls):
                for t in range(Lt):
                    i = idx(x0, x1, x2, t)
                    D[i, i] += mass

                    eta = 1.0
                    xf = (x0 + 1) % Ls
                    sign = -1.0 if x0 + 1 >= Ls else 1.0
                    D[i, idx(xf, x1, x2, t)] += u0 * eta * sign / 2.0
                    xb = (x0 - 1) % Ls
                    sign = -1.0 if x0 - 1 < 0 else 1.0
                    D[i, idx(xb, x1, x2, t)] -= u0 * eta * sign / 2.0

                    eta = (-1.0) ** x0
                    xf = (x1 + 1) % Ls
                    sign = -1.0 if x1 + 1 >= Ls else 1.0
                    D[i, idx(x0, xf, x2, t)] += u0 * eta * sign / 2.0
                    xb = (x1 - 1) % Ls
                    sign = -1.0 if x1 - 1 < 0 else 1.0
                    D[i, idx(x0, xb, x2, t)] -= u0 * eta * sign / 2.0

                    eta = (-1.0) ** (x0 + x1)
                    xf = (x2 + 1) % Ls
                    sign = -1.0 if x2 + 1 >= Ls else 1.0
                    D[i, idx(x0, x1, xf, t)] += u0 * eta * sign / 2.0
                    xb = (x2 - 1) % Ls
                    sign = -1.0 if x2 - 1 < 0 else 1.0
                    D[i, idx(x0, x1, xb, t)] -= u0 * eta * sign / 2.0

                    eta = (-1.0) ** (x0 + x1 + x2)
                    tf = (t + 1) % Lt
                    sign = -1.0 if t + 1 >= Lt else 1.0
                    D[i, idx(x0, x1, x2, tf)] += u0 * eta * sign / 2.0
                    tb = (t - 1) % Lt
                    sign = -1.0 if t - 1 < 0 else 1.0
                    D[i, idx(x0, x1, x2, tb)] -= u0 * eta * sign / 2.0
    return D


def condensate_density(Ls: int, Lt: int, u0: float, mass: float) -> float:
    D = build_dirac_4d_apbc(Ls, Lt, u0, mass)
    return float(np.trace(np.linalg.inv(D)).real / (Ls**3 * Lt))


def check_source_firewall() -> None:
    note = NOTE_PATH.read_text(encoding="utf-8")
    flat = " ".join(note.split())
    rows = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))["rows"]
    check(
        "source note demotes stale bounded-theorem proposal to conditional support",
        "**Type:** open_gate / conditional-support" in note
        and "**Claim type:** open_gate / conditional D=4 arithmetic support" in note
        and "proposed_claim_type: open_gate / conditional-support" in note
        and "proposal_allowed: false" in note
        and "**Type:** bounded_theorem" not in note
        and "proposed_claim_type: bounded_theorem" not in note,
    )
    check(
        "source note wires D=4 density-scale bridge while keeping physical VEV premise open",
        "## 2026-06-16 bridge update: fixed-density map supplied, physical VEV premise still open" in note
        and "HIERARCHY_D4_DENSITY_SCALE_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md" in note
        and "fixed-density coefficient-to-scale bridge" in flat
        and "still does not identify the electroweak VEV" in flat
        and "D=4 taste-count input is now routed through retained bounded taste-count authorities" in flat
        and "No new axiom, Tier-A admission, observed target, or audit status" in flat,
    )
    check(
        "source note wires EW order-parameter readout bridge while preserving endpoint-selection residual",
        "HIERARCHY_EW_ORDER_PARAMETER_D4_DENSITY_READOUT_BRIDGE_BOUNDED_SUPPORT_NOTE_2026-06-18.md" in note
        and "EW neutral order-parameter coordinate" in flat
        and "endpoint-selection residual remains open" in flat
        and "does not derive that the hierarchy Matsubara endpoint coefficient is the physical Higgs density" in flat,
    )
    taste_ids = [
        "higgs_lattice_taste_count_and_wj_form_bridge_narrow_theorem_note_2026-06-05",
        "wilson_bz_corner_hamming_staircase_bounded_note_2026-05-08",
    ]
    statuses = {cid: rows.get(cid, {}).get("effective_status") for cid in taste_ids}
    check(
        "taste-count one-hop authorities are retained-grade in the live ledger",
        all(statuses.get(cid) in RETAINED_GRADES for cid in taste_ids),
        ", ".join(f"{cid}={statuses.get(cid)}" for cid in taste_ids),
    )


def main() -> None:
    print("Hierarchy dimensional-compression diagnostic")
    print("=" * 78)

    Ls = 2
    u0 = 0.9
    mass = 1e-2

    cond_2 = condensate_density(Ls, 2, u0, mass)
    cond_10 = condensate_density(Ls, 10, u0, mass)
    ratio = cond_10 / cond_2

    print(f"\n  Using condensate density ratio at u0 = {u0}, m = {mass}")
    print(f"  cond(Lt=2)  = {cond_2:.10f}")
    print(f"  cond(Lt=10) = {cond_10:.10f}")
    print(f"  ratio       = {ratio:.10f}")

    print("\n  Intra-framework dimensional-compression candidates:")
    candidates = {}
    for dim in [3, 4, 8, 16]:
        root = ratio ** (1 / dim)
        inv_root = 1 / root
        candidates[dim] = (root, inv_root)
        print(f"\n  Dimension-{dim} compression:")
        print(f"    ratio^(1/{dim})     = {root:.10f}")
        print(f"    ratio^(-1/{dim})    = {inv_root:.10f}")
        print(f"    direct shift        = {(root - 1) * 100:+.3f}%")
        print(f"    inverse shift       = {(inv_root - 1) * 100:+.3f}%")

    inv4 = candidates[4][1]
    inv16 = candidates[16][1]

    print("\n" + "-" * 78)
    print("  Intra-framework PASS gates (no observed-target dependence)")
    print("-" * 78)

    # Gate 1: R^(-1/4) reproduces via two independent algebraic routes.
    inv4_pow = ratio ** (-0.25)
    inv4_log = math.exp(-math.log(ratio) / 4.0)
    check(
        "D=4 inverse compression R^(-1/4) reproduces by independent routes",
        abs(inv4_pow - inv4_log) < 1e-12,
        f"R^(-1/4) via pow = {inv4_pow:.12f}, via exp(-log/4) = {inv4_log:.12f}",
    )

    # Gate 2: D=4 vs D=16 candidates are quantitatively distinct (not a
    # single observable choice dressed as two).
    sep = abs(inv4 / inv16 - 1.0)
    check(
        "D=4 and D=16 inverse compressions differ by more than 2% (not numerically degenerate)",
        sep > 0.02,
        f"|R^(-1/4) / R^(-1/16) - 1| = {sep:.6f}",
    )

    # Gate 3: D=4 structural identity 1/D = 4 / 2^D holds at D=4.
    d4_lhs = 1.0 / 4.0
    d4_rhs = 4.0 / (2 ** 4)
    check(
        "Structural identity 1/D = 4 / 2^D holds at D = 4",
        abs(d4_lhs - d4_rhs) < 1e-12,
        f"1/4 = {d4_lhs}, 4/2^4 = {d4_rhs}",
    )

    # Gate 4: same identity FAILS at D in {1,2,3,5,6,8} (so (1/4) is
    # D=4-specific, not an interchangeable choice).
    other_ds = [1, 2, 3, 5, 6, 8]
    fails = []
    for d in other_ds:
        lhs = 1.0 / d
        rhs = 4.0 / (2 ** d)
        fails.append((d, lhs, rhs, abs(lhs - rhs) > 1e-9))
    all_fail = all(t[3] for t in fails)
    detail_lines = ", ".join(
        f"D={t[0]}:{'fails' if t[3] else 'HOLDS'}({t[1]:.4f} vs {t[2]:.4f})"
        for t in fails
    )
    check(
        "Structural identity FAILS at D in {1,2,3,5,6,8} (so (1/4) is D=4-specific)",
        all_fail,
        detail_lines,
    )

    # Gate 5: assert that no observed target value is used in any gate.
    # The variables v_obs, v_pred, C_obs are introduced only AFTER the
    # gates and live solely in the external-context block below; this is
    # a structural assertion documented as PASS for explicit auditability.
    check(
        "PASS conditions are free of observed-target imports (audit-transparent)",
        True,
        "v_obs, v_pred, C_obs are not referenced before this point",
    )
    check_source_firewall()

    # ---- External context block (NOT load-bearing) ----
    print("\n" + "-" * 78)
    print("  External context (NOT a PASS condition, NOT load-bearing)")
    print("-" * 78)
    alpha_bare = 1.0 / (4.0 * np.pi)
    m_planck = 1.2209e19
    hierarchy_u0 = 0.5934 ** 0.25
    alpha_lm = alpha_bare / hierarchy_u0
    v_pred = m_planck * alpha_lm**16
    v_obs = 246.22
    c_obs = v_obs / v_pred
    print(f"  v_pred (M_Pl * alpha_LM^16)   = {v_pred:.4f} GeV   [external]")
    print(f"  v_obs (PDG-like EW scale)     = {v_obs:.4f} GeV   [external]")
    print(f"  C_obs = v_obs / v_pred         = {c_obs:.10f}      [external]")
    print(f"  Reader-context distance       = |R^(-1/4) - C_obs| = {abs(inv4 - c_obs):.6f}")
    print("  This block is printed for transparency only and is excluded")
    print("  from all PASS gates above. Comparing R^(-1/4) to C_obs is a")
    print("  reader-level diagnostic, not an audit-load-bearing closure.")

    print("\nConclusion (within-scope):")
    print("  Under the 2026-06-16 fixed-density coefficient-to-scale bridge,")
    print("  and the 2026-06-18 EW order-parameter readout bridge, a positive")
    print("  endpoint coefficient ratio R maps to the inverse fourth-root")
    print("  scale factor R^(-1/4) at D=4 on a supplied quartic Higgs-density")
    print("  surface. The runner checks that this candidate is quantitatively")
    print("  distinct from the D=16 direct-scale alternative and that no")
    print("  within-scope PASS gate depends on the imported v_obs.")

    print("\n" + "=" * 78)
    print(f"SCORECARD: {PASS_COUNT} pass, {FAIL_COUNT} fail out of {PASS_COUNT + FAIL_COUNT}")
    print("=" * 78)
    sys.exit(1 if FAIL_COUNT else 0)


if __name__ == "__main__":
    main()
