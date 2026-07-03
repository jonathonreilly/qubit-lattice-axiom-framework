#!/usr/bin/env python3
"""
Route probes for the dm-leptogenesis I_seed minimum-information selector gate.

Gate note (ledger effective_status: audited_conditional; the note's own scope
declares an open selector gate):
  docs/DM_LEPTOGENESIS_PMNS_MINIMUM_INFORMATION_SOURCE_LAW_NOTE_2026-04-16.md

Paired note:
  docs/DM_LEPTOGENESIS_PMNS_ISEED_SELECTOR_ROUTE_PROBES_NOTE_2026-07-02.md

That note is explicit that the minimum-information selector `I_seed` and the
favored-column equality constraint `eta_{i_*} / eta_obs = 1` are ADOPTED
(imported from information geometry), not derived from the Lattice + Qubit +
Admissibility + Record baseline. These probes test three route claims about WHY
the selector is non-baseline. Each probe is refutation-shaped: it states a
hypothesis that could be false, computes a witness, and FAILS honestly if the
witness does not exist. An honest miss reported as a FAIL is a win; a fake pass
is not.

Objects reused verbatim from the gate note and its primary runner
(scripts/frontier_dm_leptogenesis_pmns_mininfo_source_law.py):
  - seed surface: x_seed = (xbar, xbar, xbar), y_seed = (ybar, ybar, ybar)
    with xbar = 0.5633333333333334, ybar = 0.30666666666666664
  - I_seed(x, y, delta) = D_KL(x||x_seed) + D_KL(y||y_seed) + (1 - cos delta),
    KL taken on the L1-normalized columns (identical to the runner's info_cost)
  - the exact transport map eta_columns_from_active(x, y, delta) and eta_obs,
    imported from the same modules the gate runner imports, so eta ratios here
    are the note's real transport object, not a re-invented proxy.

The "realized_state primitive: pointwise evaluation only, no typicality" rule is
respected: each admissible realized-state assignment is a single explicit point
on the fixed native seed surface, evaluated pointwise. No measure, no ensemble,
no typicality assumption is used anywhere.

Runs from the worktree root:  python3 scripts/dm_iseed_selector_route_probes_2026_07_02.py
Exit code 0 iff every probe PASSes.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np

from dm_leptogenesis_exact_common import (
    C_SPH,
    D_THERMAL_EXACT,
    ETA_OBS,
    S_OVER_NGAMMA_EXACT,
    exact_package,
)
from frontier_dm_leptogenesis_flavor_column_functional_theorem import (
    flavored_column_functional,
    flavored_transport_kernel,
)
from frontier_dm_leptogenesis_pmns_active_projector_reduction import active_packet_from_h
from frontier_dm_leptogenesis_pmns_projector_interface import canonical_h

ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "DM_LEPTOGENESIS_PMNS_MINIMUM_INFORMATION_SOURCE_LAW_NOTE_2026-04-16.md"

# Seed surface (verbatim from the gate note, lines 53-54, 62-63).
XBAR = 0.5633333333333334
YBAR = 0.30666666666666664
X_SEED = np.full(3, XBAR, dtype=float)
Y_SEED = np.full(3, YBAR, dtype=float)

# Exact transport package (same objects the gate runner imports).
PKG = exact_package()
Z_GRID, SOURCE_PROFILE, WASHOUT_TAIL = flavored_transport_kernel(PKG.k_decay_exact)

PASS_COUNT = 0
FAIL_COUNT = 0


def verdict(name: str, passed: bool, witness: str) -> None:
    global PASS_COUNT, FAIL_COUNT
    tag = "PASS" if passed else "FAIL"
    if passed:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"[{tag}] {name}")
    print(f"       witness: {witness}")


def soft3(u: float, v: float, total: float) -> np.ndarray:
    """Positive 3-vector with fixed sum `total` (same simplex-surface map as the
    gate runner's soft3, so every point lies on the fixed native seed surface:
    mean(x) = xbar when total = 3*xbar)."""
    logits = np.array([u, v, 0.0], dtype=float)
    logits -= np.max(logits)
    weights = np.exp(logits)
    weights /= np.sum(weights)
    return total * weights


def info_cost(x: np.ndarray, y: np.ndarray, delta: float) -> float:
    """The gate note's I_seed, byte-for-byte the runner's info_cost:
    KL on L1-normalized columns against the uniform seed, plus (1 - cos delta)."""
    px = x / np.sum(x)
    py = y / np.sum(y)
    qx = X_SEED / np.sum(X_SEED)
    qy = Y_SEED / np.sum(Y_SEED)
    kl_x = float(np.sum(px * np.log(px / qx)))
    kl_y = float(np.sum(py * np.log(py / qy)))
    return kl_x + kl_y + (1.0 - math.cos(float(delta)))


def info_cost_weighted(x: np.ndarray, y: np.ndarray, delta: float, wx: float, wy: float) -> float:
    """A legitimately reweighted minimum-information functional: the same two KL
    divergences and the same phase term, but the x-modality and y-modality blocks
    carry positive weights (wx, wy) -- a modality weighting principle. Each KL
    block is a genuine (non-negative) divergence, so a positive-weighted sum stays
    non-negative; (wx, wy) = (1, 1) recovers info_cost exactly. This is a bona-fide
    reweighting of the same information cost, not a sub-unit-per-column rescaling
    that could push the functional below zero."""
    px = x / np.sum(x)
    py = y / np.sum(y)
    qx = X_SEED / np.sum(X_SEED)
    qy = Y_SEED / np.sum(Y_SEED)
    kl_x = float(np.sum(px * np.log(px / qx)))
    kl_y = float(np.sum(py * np.log(py / qy)))
    return wx * kl_x + wy * kl_y + (1.0 - math.cos(float(delta)))


def eta_columns(x: np.ndarray, y: np.ndarray, delta: float) -> np.ndarray:
    """eta_{i}/eta_obs for i in {0,1,2}, using the gate note's exact transport
    map (imported, not re-derived)."""
    h_e = canonical_h(x, y, delta)
    packet = active_packet_from_h(h_e).T
    return np.array(
        [
            S_OVER_NGAMMA_EXACT
            * C_SPH
            * D_THERMAL_EXACT
            * PKG.epsilon_1
            * flavored_column_functional(packet[:, idx], Z_GRID, SOURCE_PROFILE, WASHOUT_TAIL)
            / ETA_OBS
            for idx in range(3)
        ],
        dtype=float,
    )


def favored_column(x: np.ndarray, y: np.ndarray, delta: float) -> int:
    """The transport-favored column i_* = argmax_i eta_i, exactly the quantity the
    gate note's step 1 ('transport-favored flavor column i_* from the exact
    transport-extremal class') maximizes."""
    return int(np.argmax(eta_columns(x, y, delta)))


def fmt(v: np.ndarray) -> str:
    return np.array2string(np.round(np.asarray(v, dtype=float), 6), separator=", ")


# ---------------------------------------------------------------------------
# P1: axiom-surface independence of the favored column
# ---------------------------------------------------------------------------
def probe1_axiom_surface_independence() -> None:
    """Hypothesis: the I_seed-relevant favored column i_* = argmax_i eta_i is NOT
    fixed by the axiom surface alone; two law-admissible realized-state
    assignments on the SAME fixed native seed surface can transport-favor
    DIFFERENT columns. If such a pair exists, i_* is state-contingent registered
    data, so no axiom-level derivation can pin it without the realized state.

    Refutation-shaped: if an exhaustive small-grid search of on-surface
    realized states all favor the SAME column, the hypothesis is unsupported and
    this probe FAILS honestly (the favored column would then be surface-rigid).
    """
    print("\n" + "=" * 88)
    print("PROBE 1: axiom-surface independence of the favored column i_*")
    print("=" * 88)

    grid = np.linspace(-3.0, 3.0, 7)
    seen: dict[int, tuple[np.ndarray, np.ndarray, float]] = {}
    for ax in grid:
        for ay in grid:
            for bx in grid:
                for by in grid:
                    for delta in (0.0, 0.6, 1.2):
                        x = soft3(ax, ay, 3.0 * XBAR)
                        y = soft3(bx, by, 3.0 * YBAR)
                        col = favored_column(x, y, delta)
                        if col not in seen:
                            seen[col] = (x, y, delta)
        if len(seen) >= 2:
            break

    passed = len(seen) >= 2
    if passed:
        cols = sorted(seen.keys())
        c_a, c_b = cols[0], cols[1]
        xa, ya, da = seen[c_a]
        xb, yb, db = seen[c_b]
        # Confirm both assignments are on the fixed native seed surface (pointwise).
        on_surface = (
            abs(np.mean(xa) - XBAR) < 1e-12
            and abs(np.mean(ya) - YBAR) < 1e-12
            and abs(np.mean(xb) - XBAR) < 1e-12
            and abs(np.mean(yb) - YBAR) < 1e-12
        )
        eta_a = eta_columns(xa, ya, da)
        eta_b = eta_columns(xb, yb, db)
        witness = (
            f"assignment A favors column {c_a}: x={fmt(xa)}, y={fmt(ya)}, "
            f"delta={da:g}, eta/eta_obs={fmt(eta_a)} | "
            f"assignment B favors column {c_b}: x={fmt(xb)}, y={fmt(yb)}, "
            f"delta={db:g}, eta/eta_obs={fmt(eta_b)} | "
            f"both on fixed seed surface (mean-xbar/mean-ybar)={on_surface} | "
            f"distinct favored columns {c_a} != {c_b}"
        )
        passed = passed and on_surface
    else:
        only = next(iter(seen.keys())) if seen else None
        witness = (
            f"exhaustive on-surface grid favored a single column {only} for every "
            f"admissible realized state searched; no differing pair found "
            f"(favored column is surface-rigid across the grid)"
        )
    verdict(
        "Two law-admissible realized states favor DIFFERENT transport columns",
        passed,
        witness,
    )


# ---------------------------------------------------------------------------
# P2: weighting-principle dependence of the argmin
# ---------------------------------------------------------------------------
def probe2_weighting_principle_dependence() -> None:
    """Hypothesis: the minimum-information selection presupposes a modality
    weighting principle. Over the SAME finite candidate set of admissible
    OFF-seed sources, the argmin of the uniform functional I_seed (equal x/y
    weight) and the argmin of a legitimately modality-weighted functional
    I_seed^{wx,wy} disagree.

    If they disagree, the reported minimizer is an artifact of the (unstated,
    equal-modality) weighting choice, not of the data. Refutation-shaped: if the
    two argmins coincide for every legitimate weighting tried, the selector is
    weighting-invariant and this probe FAILS honestly.

    The exact seed point is excluded from the bank: the note selects among
    off-seed sources, and at the seed both functionals are identically 0. With it
    excluded, both reported minima are strictly positive proper information costs
    (each KL block is a genuine non-negative divergence under positive modality
    weights), so the disagreement cannot be a sign/rounding artifact.
    """
    print("\n" + "=" * 88)
    print("PROBE 2: weighting-principle dependence of the I_seed argmin")
    print("=" * 88)

    # A finite, explicit candidate bank of admissible OFF-seed sources, each a
    # single pointwise realized state on the fixed native seed surface. The
    # equal-logit / zero-phase point (0,0),(0,0),delta=0 IS the seed, so it is
    # skipped: the selector ranges over off-seed sources only.
    logit_pairs = [
        (0.0, 0.0),
        (0.9, -0.4),
        (-0.7, 0.5),
        (0.3, 0.8),
        (-0.5, -0.9),
        (1.1, 0.2),
        (-1.0, 0.6),
        (0.4, -1.1),
    ]
    deltas = [0.0, 0.5, 1.0]
    candidates: list[tuple[np.ndarray, np.ndarray, float]] = []
    for (ax, ay) in logit_pairs:
        for (bx, by) in logit_pairs:
            for d in deltas:
                x = soft3(ax, ay, 3.0 * XBAR)
                y = soft3(bx, by, 3.0 * YBAR)
                # Exclude the exact seed (zero off-seed displacement, zero phase).
                if (
                    np.linalg.norm(x - X_SEED) < 1e-9
                    and np.linalg.norm(y - Y_SEED) < 1e-9
                    and abs(d) < 1e-12
                ):
                    continue
                candidates.append((x, y, d))

    # Uniform modality weighting (the gate note's I_seed): wx = wy = 1.
    # A legitimate modality reweighting: weight the x-block more than the y-block.
    # Both weights positive, so each KL block stays a non-negative divergence and
    # the functional stays >= 0; (wx, wy) = (1, 1) reproduces info_cost exactly.
    wx_dim, wy_dim = 2.0, 0.5

    costs_uniform = [info_cost_weighted(x, y, d, 1.0, 1.0) for (x, y, d) in candidates]
    costs_dim = [info_cost_weighted(x, y, d, wx_dim, wy_dim) for (x, y, d) in candidates]

    idx_uniform = int(np.argmin(costs_uniform))
    idx_dim = int(np.argmin(costs_dim))

    # Sanity: (wx, wy) = (1, 1) reproduces the note's info_cost exactly, and both
    # reported minima are strictly positive proper information costs.
    xr, yr, dr = candidates[idx_uniform]
    reproduces = abs(costs_uniform[idx_uniform] - info_cost(xr, yr, dr)) < 1e-12
    both_positive = costs_uniform[idx_uniform] > 1e-9 and costs_dim[idx_dim] > 1e-9

    passed = (idx_uniform != idx_dim) and reproduces and both_positive
    xu, yu, du = candidates[idx_uniform]
    xd, yd, dd = candidates[idx_dim]
    witness = (
        f"|bank|={len(candidates)} off-seed sources (seed excluded) | "
        f"uniform-argmin idx={idx_uniform} "
        f"(x={fmt(xu)}, y={fmt(yu)}, delta={du:g}, I_seed={costs_uniform[idx_uniform]:.9f}) | "
        f"modality-weighted (wx,wy)=({wx_dim:g},{wy_dim:g}) argmin idx={idx_dim} "
        f"(x={fmt(xd)}, y={fmt(yd)}, delta={dd:g}, I_seed^w={costs_dim[idx_dim]:.9f}) | "
        f"(1,1) reproduces note info_cost={reproduces} | "
        f"both minima strictly positive proper costs={both_positive} | "
        f"argmins differ={idx_uniform != idx_dim}"
    )
    verdict(
        "Uniform vs modality-weighted minimum-information argmins disagree",
        passed,
        witness,
    )


# ---------------------------------------------------------------------------
# P3: constraint independence of eta_{i_*}/eta_obs = 1
# ---------------------------------------------------------------------------
def probe3_constraint_independence() -> None:
    """Hypothesis: the equality eta_{i_*}/eta_obs = 1 is an INDEPENDENT imposed
    constraint, not implied by the note's other premises (fixed native seed
    surface + positive off-seed source + transport-favored-column identification).
    Witness: a finite admissible model satisfying all those other premises whose
    computed eta_{i_*}/eta_obs != 1.

    Refutation-shaped: if every admissible on-surface, positive, favored-column
    model forced eta_{i_*}/eta_obs = 1, the constraint would be a consequence of
    the other premises and this probe would FAIL honestly.
    """
    print("\n" + "=" * 88)
    print("PROBE 3: constraint independence of eta_{i_*}/eta_obs = 1")
    print("=" * 88)

    # An explicit admissible model: the pure-seed realized state itself
    # (x_seed, y_seed, delta = 0). It satisfies every OTHER premise:
    #   - on the fixed native seed surface (it IS the seed): mean = xbar, ybar
    #   - positive source columns
    #   - a well-defined transport-favored column i_* = argmax_i eta_i
    # but its off-seed displacement is zero, so it is not fitted to eta_obs.
    x0 = X_SEED.copy()
    y0 = Y_SEED.copy()
    d0 = 0.0
    eta0 = eta_columns(x0, y0, d0)
    i_star0 = int(np.argmax(eta0))
    ratio0 = float(eta0[i_star0])

    on_surface0 = abs(np.mean(x0) - XBAR) < 1e-12 and abs(np.mean(y0) - YBAR) < 1e-12
    positive0 = bool(np.all(x0 > 0) and np.all(y0 > 0))
    ne_one0 = abs(ratio0 - 1.0) > 1e-6

    # A second, off-seed admissible model to show the miss is generic, not a
    # boundary artifact of the seed point.
    x1 = soft3(0.7, -0.5, 3.0 * XBAR)
    y1 = soft3(-0.6, 0.4, 3.0 * YBAR)
    d1 = 0.4
    eta1 = eta_columns(x1, y1, d1)
    i_star1 = int(np.argmax(eta1))
    ratio1 = float(eta1[i_star1])
    on_surface1 = abs(np.mean(x1) - XBAR) < 1e-12 and abs(np.mean(y1) - YBAR) < 1e-12
    positive1 = bool(np.all(x1 > 0) and np.all(y1 > 0))
    ne_one1 = abs(ratio1 - 1.0) > 1e-6

    passed = (on_surface0 and positive0 and ne_one0) and (on_surface1 and positive1 and ne_one1)
    witness = (
        f"model A = pure seed (x_seed,y_seed,delta=0): on_surface={on_surface0}, "
        f"positive={positive0}, i_*={i_star0}, eta_(i_*)/eta_obs={ratio0:.9f} "
        f"(deviation from 1 = {ratio0 - 1.0:+.9f}) | "
        f"model B = off-seed (x={fmt(x1)}, y={fmt(y1)}, delta={d1:g}): "
        f"on_surface={on_surface1}, positive={positive1}, i_*={i_star1}, "
        f"eta_(i_*)/eta_obs={ratio1:.9f} (deviation from 1 = {ratio1 - 1.0:+.9f}) | "
        f"both satisfy the other premises with ratio != 1 ==> equality is an "
        f"independent imposed constraint"
    )
    verdict(
        "A model meeting all other premises has eta_(i_*)/eta_obs != 1",
        passed,
        witness,
    )


def main() -> int:
    print("=" * 88)
    print("I_seed SELECTOR ROUTE PROBES (dm-leptogenesis minimum-information gate)")
    print("=" * 88)
    print(f"gate note: {NOTE_PATH.relative_to(ROOT)}")
    print("seed surface: x_seed=(xbar,xbar,xbar), y_seed=(ybar,ybar,ybar)")
    print(f"  xbar={XBAR}, ybar={YBAR}, eta_obs={ETA_OBS}")
    print("I_seed = D_KL(x||x_seed) + D_KL(y||y_seed) + (1 - cos delta)  [note's info_cost]")
    print("transport map eta_columns imported from the gate note's own runner stack")
    print("realized_state primitive respected: pointwise evaluation, no typicality")

    probe1_axiom_surface_independence()
    probe2_weighting_principle_dependence()
    probe3_constraint_independence()

    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
