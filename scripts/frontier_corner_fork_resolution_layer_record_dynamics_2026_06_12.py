#!/usr/bin/env python3
"""Verification runner for

    docs/CORNER_MODE_SET_FORK_RESOLUTION_LAYER_IS_RECORD_DYNAMICS_BOUNDED_NOTE_2026-06-12.md

No cache is regenerated. The runner checks the supplied free corner-axis class,
both registrable fork branches, and the note/dependency firewall surfaces.

Run:
    python3 scripts/frontier_corner_fork_resolution_layer_record_dynamics_2026_06_12.py
"""
from __future__ import annotations

import math
import re
import sys
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "CORNER_MODE_SET_FORK_RESOLUTION_LAYER_IS_RECORD_DYNAMICS_BOUNDED_NOTE_2026-06-12.md"
DEP_RP = ROOT / "docs" / "AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md"
DEP_REG = ROOT / "docs" / "REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md"

L_S = 2
POINTS = (
    ("witness-1", 1.0, 0.25, 2.0 / 9.0),
    ("witness-2", 1.2, 0.2, -1.0 / 3.0),
)
TOL = 5.0e-13

pass_count = 0
fail_count = 0


def check(name: str, condition: bool, detail: str) -> None:
    global pass_count, fail_count
    if bool(condition):
        pass_count += 1
        status = "PASS"
    else:
        fail_count += 1
        status = "FAIL"
    print(f"[{status}] {name}: {detail}")


def lambdas(a: float, b: float, delta: float) -> np.ndarray:
    return np.array(
        [a + 2.0 * b * math.cos(delta + 2.0 * math.pi * k / 3.0) for k in range(3)],
        dtype=np.float64,
    )


def momenta(ls: int = L_S) -> np.ndarray:
    return np.array([(2 * n + 1) * math.pi / ls for n in range(ls)], dtype=np.float64)


def energy(lam: float, p: float) -> float:
    return math.asinh(math.sqrt(lam * lam + math.sin(p) ** 2))


def channel_kernel(lam: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    ps = momenta()
    energies = np.array([energy(lam, p) for p in ps], dtype=np.float64)
    t = np.exp(-2.0 * energies)
    residuals = np.array(
        [math.sinh(e) ** 2 - lam * lam - math.sin(p) ** 2 for e, p in zip(energies, ps)],
        dtype=np.float64,
    )
    return ps, energies, t, residuals


def branch_objects(a: float, b: float, delta: float) -> dict[str, object]:
    lam = lambdas(a, b, delta)
    t_values = []
    residuals = []
    determinants = []
    energies = []
    for lam_k in lam:
        ps, es, ts, res = channel_kernel(float(lam_k))
        t_values.append(ts)
        energies.append(es)
        residuals.extend(res.tolist())
        determinants.append(float(np.prod(1.0 + ts)))

    d = np.array(determinants, dtype=np.float64)
    log_d = np.log(d)
    z_ch = float(np.prod(d))
    d_orb = float(math.sqrt(d[1] * d[2]))
    z_orb = float(d[0] * d_orb)
    return {
        "lambda": lam,
        "momenta": ps,
        "energies": np.array(energies),
        "t": np.array(t_values),
        "residuals": np.array(residuals),
        "D": d,
        "logD": log_d,
        "D_orb": d_orb,
        "Z_ch": z_ch,
        "Z_orb": z_orb,
        "log_Z_ch_add": float(np.sum(log_d)),
        "log_Z_orb_add": float(log_d[0] + 0.5 * (log_d[1] + log_d[2])),
    }


def symbolic_lambda_identity() -> bool:
    a, b, delta = sp.symbols("a B delta", real=True)
    lam1_neg = a + 2 * b * sp.cos(-delta + 2 * sp.pi / 3)
    lam2_pos = a + 2 * b * sp.cos(delta + 4 * sp.pi / 3)
    diff = sp.trigsimp(sp.expand_trig(lam1_neg - lam2_pos))
    return diff == 0


def symbolic_swap_and_log_checks() -> dict[str, bool]:
    d0, d1, d2 = sp.symbols("D0 D1 D2", positive=True)
    z_ch = d0 * d1 * d2
    z_orb = d0 * sp.sqrt(d1 * d2)
    log_ch = sp.log(d0) + sp.log(d1) + sp.log(d2)
    log_ch_expanded = sp.expand_log(sp.log(z_ch), force=True)
    log_orb = sp.log(d0) + sp.Rational(1, 2) * (sp.log(d1) + sp.log(d2))
    log_orb_expanded = sp.expand_log(sp.log(z_orb), force=True)
    return {
        "z_ch_swap_exact": sp.simplify(z_ch - z_ch.xreplace({d1: d2, d2: d1})) == 0,
        "z_orb_swap_exact": sp.simplify(z_orb - z_orb.xreplace({d1: d2, d2: d1})) == 0,
        "log_ch_add_exact": sp.simplify(log_ch_expanded - log_ch) == 0,
        "log_orb_add_exact": sp.simplify(log_orb_expanded - log_orb) == 0,
    }


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def link_inventory(note_text: str) -> list[tuple[str, str]]:
    return re.findall(r"\[([^\]]+)\]\(([^)]+)\)", note_text)


def main() -> int:
    print("SCOPE:")
    print("supplied free U=1 corner-axis class; three decoupled 1+1d staggered channels; L_s=2.")
    print("NOT claimed: branch selection, fixed r, OO adoption, R-D adoption, physical realization of the orbit factor.")
    print("No cache regeneration; audit lane remains the status authority.")

    sym = symbolic_swap_and_log_checks()
    lambda_identity = symbolic_lambda_identity()
    check(
        "symbolic K identity lambda_2(delta)=lambda_1(-delta)",
        lambda_identity,
        "sympy trigsimp(expand_trig(lambda_1(-delta)-lambda_2(delta))) == 0",
    )

    check(
        "Y1a Z_ch doublet-swap invariance exact",
        sym["z_ch_swap_exact"],
        "D0*D1*D2 is unchanged by D1 <-> D2",
    )
    check(
        "Y1c log-additivity exact over channel factors",
        sym["log_ch_add_exact"],
        "expand_log(log(D0*D1*D2)) = logD0 + logD1 + logD2",
    )
    check(
        "Y2a Z_orb doublet-swap invariance exact",
        sym["z_orb_swap_exact"],
        "D0*sqrt(D1*D2) is unchanged by D1 <-> D2",
    )
    check(
        "Y2b log-additivity exact over singlet/orbit factors",
        sym["log_orb_add_exact"],
        "expand_log(log(D0*sqrt(D1*D2))) = logD0 + 1/2(logD1+logD2)",
    )

    rows = []
    all_lambdas_positive = True
    all_domain = True
    all_dispersion_small = True
    y1_even_all = True
    y2_even_all = True
    y1_log_numeric_all = True
    y2_log_numeric_all = True
    y3_diff_all = True
    y3_positive_all = True
    relative_gaps = []

    print("\nNUMERIC WITNESSES:")
    for label, a, b, delta in POINTS:
        obj = branch_objects(a, b, delta)
        neg = branch_objects(a, b, -delta)
        lam = obj["lambda"]
        residual_max = float(np.max(np.abs(obj["residuals"])))
        z_ch = float(obj["Z_ch"])
        z_orb = float(obj["Z_orb"])
        gap = abs(z_ch - z_orb) / max(abs(z_ch), abs(z_orb))
        relative_gaps.append(gap)

        domain_ok = a > 2.0 * b > 0.0
        lambdas_positive = bool(np.all(lam > 0.0))
        y1_even = abs(z_ch - float(neg["Z_ch"])) <= TOL * max(1.0, abs(z_ch), abs(float(neg["Z_ch"])))
        y2_even = abs(z_orb - float(neg["Z_orb"])) <= TOL * max(1.0, abs(z_orb), abs(float(neg["Z_orb"])))
        y1_log_numeric = abs(math.log(z_ch) - float(obj["log_Z_ch_add"])) <= TOL
        y2_log_numeric = abs(math.log(z_orb) - float(obj["log_Z_orb_add"])) <= TOL
        y3_diff = not math.isclose(z_ch, z_orb, rel_tol=1.0e-10, abs_tol=1.0e-12)
        y3_positive = z_ch > 0.0 and z_orb > 0.0

        all_domain = all_domain and domain_ok
        all_lambdas_positive = all_lambdas_positive and lambdas_positive
        all_dispersion_small = all_dispersion_small and residual_max <= 1.0e-14
        y1_even_all = y1_even_all and y1_even
        y2_even_all = y2_even_all and y2_even
        y1_log_numeric_all = y1_log_numeric_all and y1_log_numeric
        y2_log_numeric_all = y2_log_numeric_all and y2_log_numeric
        y3_diff_all = y3_diff_all and y3_diff
        y3_positive_all = y3_positive_all and y3_positive
        rows.append((label, obj, neg))

        print(
            f"{label}: a={a:.12g}, B={b:.12g}, delta={delta:.12g}, "
            f"domain={domain_ok}, lambdas={np.array2string(lam, precision=15)}"
        )
        print(
            f"{label}: momenta={np.array2string(obj['momenta'], precision=15)}, "
            f"max dispersion residual={residual_max:.3e}"
        )
        print(
            f"{label}: D={np.array2string(obj['D'], precision=15)}, "
            f"D_orb={obj['D_orb']:.15e}"
        )
        print(
            f"{label}: Z_ch={z_ch:.15e}, Z_orb={z_orb:.15e}, "
            f"relative_gap={gap:.15e}"
        )

    check(
        "1 positivity domain a > 2B > 0 at both points",
        all_domain,
        "; ".join(f"{label}: a={a}, B={b}, a-2B={a - 2*b:.6g}" for label, a, b, _ in POINTS),
    )
    check(
        "1 lambda_k(delta) all positive at both points",
        all_lambdas_positive,
        "; ".join(f"{label}: min_lambda={np.min(obj['lambda']):.15e}" for label, obj, _ in rows),
    )
    check(
        "2 retained two-step dispersion residual",
        all_dispersion_small,
        "; ".join(f"{label}: max_abs_residual={np.max(np.abs(obj['residuals'])):.3e}" for label, obj, _ in rows),
    )
    check(
        "Y1b Z_ch(delta)=Z_ch(-delta) at both points",
        y1_even_all,
        "; ".join(
            f"{label}: abs_diff={abs(float(obj['Z_ch']) - float(neg['Z_ch'])):.3e}"
            for label, obj, neg in rows
        ),
    )
    check(
        "Y1c numeric log-additivity over channel factors",
        y1_log_numeric_all,
        "; ".join(
            f"{label}: residual={abs(math.log(float(obj['Z_ch'])) - float(obj['log_Z_ch_add'])):.3e}"
            for label, obj, _ in rows
        ),
    )
    check(
        "Y2a Z_orb(delta)=Z_orb(-delta) at both points",
        y2_even_all,
        "; ".join(
            f"{label}: abs_diff={abs(float(obj['Z_orb']) - float(neg['Z_orb'])):.3e}"
            for label, obj, neg in rows
        ),
    )
    check(
        "Y2b numeric log-additivity over singlet/orbit factors",
        y2_log_numeric_all,
        "; ".join(
            f"{label}: residual={abs(math.log(float(obj['Z_orb'])) - float(obj['log_Z_orb_add'])):.3e}"
            for label, obj, _ in rows
        ),
    )
    check(
        "Y3 positive branch values",
        y3_positive_all,
        "; ".join(
            f"{label}: Z_ch={float(obj['Z_ch']):.6e}, Z_orb={float(obj['Z_orb']):.6e}"
            for label, obj, _ in rows
        ),
    )
    check(
        "Y3 Z_ch != Z_orb at both domain points",
        y3_diff_all,
        "; ".join(f"{label}: relative_gap={gap:.6e}" for (label, _, _), gap in zip(rows, relative_gaps)),
    )

    y1_registrable = bool(sym["z_ch_swap_exact"] and sym["log_ch_add_exact"] and y1_even_all)
    y2_registrable = bool(sym["z_orb_swap_exact"] and sym["log_orb_add_exact"] and y2_even_all)
    branch_set = {"per-channel": y1_registrable, "per-K-orbit": y2_registrable}
    admissible = tuple(name for name, ok in branch_set.items() if ok)
    check(
        "Y3 structural admissible branch set is BOTH branches",
        admissible == ("per-channel", "per-K-orbit"),
        f"assembled from Y1/Y2 booleans: {branch_set}",
    )
    check(
        "Y4 negative control registration layer cannot select",
        y1_registrable and y2_registrable and y3_diff_all,
        "branch values differ while both satisfy additivity and K/CPT orbit-constancy",
    )

    rp_text = read_text(DEP_RP)
    reg_text = read_text(DEP_REG)
    note_text = read_text(NOTE)

    rp_phrases = (
        "2-step blocked transfer matrix",
        "free fermion-sector two-step positivity factor",
    )
    for phrase in rp_phrases:
        check(
            f"B dep RP phrase present: {phrase!r}",
            phrase in rp_text,
            f"{DEP_RP.relative_to(ROOT)} contains the real phrase",
        )

    reg_phrases = (
        "finitely additive over finite",
        "constant on `K`/CPT",
    )
    for phrase in reg_phrases:
        check(
            f"B dep registrability phrase present: {phrase!r}",
            phrase in reg_text,
            f"{DEP_REG.relative_to(ROOT)} contains the real phrase",
        )

    firewall_phrases = (
        "neither fork branch is selected",
        "`r` is never fixed",
        "the binary stays open",
        "supplied in-note",
        "not a physical realization claim",
    )
    check(
        "B note firewall sentences present",
        all(phrase in note_text for phrase in firewall_phrases),
        "required firewall fragments found in note",
    )

    forbidden_closing = (
        "selects the per-channel branch",
        "selects the per-K-orbit branch",
        "fixes `r`",
        "forces `r`",
        "fork is resolved",
        "resolves the fork",
        "binary is closed",
        "closes the binary",
    )
    absent_forbidden = all(phrase not in note_text for phrase in forbidden_closing)
    check(
        "B closing language absent",
        absent_forbidden,
        "forbidden branch-selection/fork-closure phrases absent",
    )

    links = link_inventory(note_text)
    expected_links = [
        (
            "`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`",
            "AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md",
        ),
        (
            "`REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md`",
            "REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md",
        ),
    ]
    check(
        "B link inventory exactly two load-bearing links",
        links == expected_links,
        f"links={links}",
    )
    companion_tokens = (
        "`wave-6 corner-extension note`",
        "`wave-4 corner companion`",
        "`wave-5 corner companion`",
        "`KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`",
        "`KOIDE_R_HALF_DURABILITY_STATIONARITY_CONDITIONAL_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-11.md`",
    )
    companions_backticked = all(token in note_text for token in companion_tokens)
    companions_not_linked = not re.search(r"\[[^\]]*(wave-|KOIDE_ORBIT_OCCUPANCY|KOIDE_R_HALF)[^\]]*\]\(", note_text)
    check(
        "B context companions are backticked only",
        companions_backticked and companions_not_linked,
        "wave companions, occupancy note, and R-D chain are context tokens, not markdown links",
    )
    check(
        "B No-promotion statement present",
        "**No-promotion statement:**" in note_text and "independent audit lane is the only status authority" in note_text,
        "No-promotion statement and status authority sentence found",
    )

    print("\nSUMMARY:")
    print(f"PASS={pass_count} FAIL={fail_count}")
    print(
        "Result: both fork branches are registrable and generically unequal; "
        "the fork is registration-blind, leaving branch discrimination to record dynamics."
    )
    return 0 if fail_count == 0 and pass_count >= 14 else 1


if __name__ == "__main__":
    sys.exit(main())
