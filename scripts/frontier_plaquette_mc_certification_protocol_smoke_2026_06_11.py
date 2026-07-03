#!/usr/bin/env python3
"""Block13: plaquette MC certification protocol — smoke-scale feasibility
runner (measurement-fallback design, Stage 1)

    docs/PLAQUETTE_MC_CERTIFICATION_PROTOCOL_NOTE_2026-06-11.md

The plaquette authority (docs/PLAQUETTE_SELF_CONSISTENCY_NOTE.md) states
that the canonical <P> = 0.5934 at beta = 6 is an admitted reuse number
"unless a separate retained MC certificate or analytic beta=6 closure is
supplied".  This block designs exactly that certificate's protocol and
calibrates its statistics budget at smoke scale.  NOTHING here certifies
the value: the smoke run is a budget-calibration diagnostic only.

What this runner establishes:

  Section M1 (classes [A]/[B]): PRECISION-TARGET DERIVATION (exact
      arithmetic, Fraction where stated).  4-decimal license grade:
      total error < 5e-5 (half-step), relative 8.4260e-5, propagated
      through d ln v / d ln <P> = -4 to a 0.0337% window on v_cand
      (cross-checked against the honest-status note's quoted number).
      5-decimal (decisive) grade: < 5e-6, i.e. 0.0034% on v — BELOW the
      B2 attribution scale 0.0255% (ratio ~7.6).  The F4 anti-tuning
      target <P>_needed = 0.5934379 (literal verified on disk in the
      honest-status note) sits +3.79e-5 from the licensed 0.5934 — LESS
      than the 4-decimal half-step (the licensed grid cannot encode it)
      but EIGHT 5-decimal half-steps from 0.59340: a 5-decimal
      certification is DECISIVE (it lands on 0.59344 or it does not).
      Decision-grade table printed.

  Section M2 (classes [C]/[A]): STATISTICS BUDGET FROM SMOKE (the
      computable core).  Reuses the update algorithm of
      scripts/frontier_plaquette_self_consistency_finite_mc_repair.py
      (Metropolis with projected near-identity SU(3) proposals), adapted
      to a vectorized full-lattice checkerboard sweep; reuse fidelity is
      checked against the imported module (batched projection vs its
      project_su3; vectorized average plaquette vs its average_plaquette
      on an L=2 random configuration; staple identity sum Re Tr[U A] =
      4 sum_P Re Tr U_P).  Smoke chain (declared, deterministic):
      L = 4, beta = 6, cold start, eps = 0.20, 2 hits/link/sweep,
      seed 20260611, 500 thermalization + 2500 measurement sweeps.
      Measured: per-configuration sigma_P, Madras-Sokal windowed
      tau_int (c = 5, declared), per-sweep wall-clock.  Computed budget:
      N_indep = (z sigma_P / target)^2 at z = 2 for target in
      {5e-5, 5e-6}; sweeps = N_indep x 2 tau_int; projected wall-clock
      at L = 8, 16, 24, 32 under the DECLARED cost model t_sweep(L) =
      t_sweep(4) x (L/4)^4 (links ~ L^4), conservative envelope
      (sigma_P, tau_int held at L = 4 values) plus the declared
      variance-scaling refinement sigma_P^2 ~ 1/L^4.  HONESTY FENCE:
      the smoke <P> estimate at L = 4 is a finite-volume diagnostic,
      NOT comparable to the infinite-volume 0.5934 target, and the
      smoke error of mean is checked to be ABOVE certification grade —
      the smoke run certifies NOTHING about the value.

  Section M3 (classes [B]/[A]): PROTOCOL SPECIFICATION.  Verifies the
      parent note carries the numbered protocol, the pre-registration
      block (decision bands declared BEFORE any production run), the
      explicit falsification warning, and the finite-volume ansatz
      <P>_L = <P>_inf + c L^-4 with >= 3 fit points; verifies the band
      arithmetic (edges ordered, bands disjoint and exhaustive; the
      Band-C minimum displacement on v_cand is exactly 2x the B1
      window); verifies the plaquette note's escape clause (the
      certificate this protocol designs) is present on disk.

  Section M4 (class [B] + residuals): STAGE 2 (staircase flat-cost
      measurement) is DESIGN-ONLY.  Verifies the flat per-rung target
      Delta_S = 2.270081 literal on disk in the action-cost note and
      the design-only fencing in the parent note.  RESIDUAL lines
      declare: the Stage-1 certification is NOT performed here; Stage 2
      stays design-only pending Stage 1; the plaquette note's status is
      unchanged (0.5934 remains an admitted reuse number until the
      pre-registered production run lands).

  Terminal class-D fence: the canonical 0.5934 enters this runner ONLY
      as the licensed target of the protocol (B1 license, declared);
      the single PDG-derived quantity touched (the comparator-residual
      scale that the F4 offset reproduces under elasticity -4) is
      confined to the fenced class-D check; a self-scan certifies the
      PDG VEV literal is absent from this runner's source.

Deterministic: fixed seeds (20260611 for the smoke chain, 20260611xx
for auxiliary tests), numpy Generator; no network.  Total runtime well
under 120 s on the reference machine (the smoke chain ~25 s dominates).
Exit code 0 iff TOTAL: PASS=n FAIL=0.
"""
from __future__ import annotations

import math
import sys
import time
from fractions import Fraction
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS = REPO_ROOT / "docs"
SCRIPTS = REPO_ROOT / "scripts"
PARENT_NOTE = DOCS / "PLAQUETTE_MC_CERTIFICATION_PROTOCOL_NOTE_2026-06-11.md"
PLAQUETTE_NOTE = DOCS / "PLAQUETTE_SELF_CONSISTENCY_NOTE.md"
HONEST_STATUS_NOTE = DOCS / "HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md"
ACTION_COST_NOTE = (
    DOCS / "HIERARCHY_DELTA0_S1PRIME_ACTION_COST_DECOMPOSITION_NOTE_2026-06-11.md"
)

sys.path.insert(0, str(SCRIPTS))
import frontier_plaquette_self_consistency_finite_mc_repair as base  # noqa: E402

PASS_COUNT = 0
FAIL_COUNT = 0
RESIDUAL_COUNT = 0
CLASS_COUNTS = {"A": 0, "B": 0, "C": 0, "D": 0}

# ---------------------------------------------------------------------------
# Declared boundary inputs (cited, not asserted).
#   <P> = 0.5934 enters ONLY as the licensed target of the certification
#   protocol (B1 reuse license, docs/PLAQUETTE_SELF_CONSISTENCY_NOTE.md).
#   The F4 anti-tuning target 0.5934379 and the B2 attribution scale
#   0.0255% are quoted literals of the honest-status note (verified on
#   disk below).  Delta_S = 2.270081 is the action-cost note's flat
#   per-rung staircase target (Stage 2; verified on disk below).
# ---------------------------------------------------------------------------
P_LICENSED = Fraction(5934, 10000)        # B1 licensed reuse number (4 d.p.)
HALF_STEP_4 = Fraction(5, 100000)         # 5e-5: 4-decimal rounding half-step
HALF_STEP_5 = Fraction(5, 1000000)        # 5e-6: 5-decimal rounding half-step
ELASTICITY = -4                           # d ln v_cand / d ln <P> (honest-status T1.v)
P_NEEDED_F4 = Fraction(5934379, 10000000)  # honest-status F4 anti-tuning target
B2_ATTRIB_REL = 2.55e-4                   # 0.0255%: honest-status B2 attribution scale
Z_SCORE = 2                               # declared coverage factor for the budget

# Smoke-run declared parameters (fixed; deterministic).
SMOKE_L = 4
SMOKE_BETA = 6.0
SMOKE_EPS = 0.20
SMOKE_NHITS = 2
SMOKE_SEED = 20260611
SMOKE_N_THERM = 500
SMOKE_N_MEAS = 2500
TAU_WINDOW_C = 5.0                        # Madras-Sokal automatic-window constant
NDIM, N_C = 4, 3


def check(klass: str, name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
        CLASS_COUNTS[klass] += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}][{klass}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def residual(msg: str) -> None:
    global RESIDUAL_COUNT
    RESIDUAL_COUNT += 1
    print(f"  RESIDUAL (declared-open): {msg}")


# ---------------------------------------------------------------------------
# Section M1 — precision-target derivation (exact arithmetic).
# ---------------------------------------------------------------------------
def section_m1():
    print("\n--- Section M1 [A]/[B]: precision-target derivation "
          "(exact arithmetic) ---")

    # M1-A1 [A]: half-step and relative target at the 4-decimal grade.
    rel4 = HALF_STEP_4 / P_LICENSED          # = 1/11868
    check("A", "A1 4-decimal grade: half-step 5e-5, relative "
               "5e-5/0.5934 = 1/11868 = 8.4260e-5 (honest-status quotes "
               "8.43e-5)",
          rel4 == Fraction(1, 11868) and abs(float(rel4) - 8.43e-5) < 5e-8,
          f"rel={float(rel4):.6e}")

    # M1-A2 [A]: propagate through elasticity -4 to the v_cand window.
    win4 = abs(ELASTICITY) * rel4            # = 1/2967
    check("A", "A2 elasticity -4 propagation: 4-decimal grade -> "
               "|d v/v| = 4 x 8.4260e-5 = 3.3704e-4 = 0.0337% "
               "(matches honest-status '+/- 0.0337 %')",
          win4 == Fraction(1, 2967) and abs(float(win4) - 3.3704e-4) < 5e-9,
          f"window={float(win4) * 100:.4f}%")

    # M1-A3 [A]: the 5-decimal (decisive) grade.
    rel5 = HALF_STEP_5 / P_LICENSED
    win5 = abs(ELASTICITY) * rel5
    check("A", "A3 5-decimal grade: half-step 5e-6 -> relative 8.4260e-6 "
               "-> 0.0034% on v_cand (exactly the 4-decimal window / 10)",
          win5 == win4 / 10 and abs(float(win5) - 3.3704e-5) < 5e-10,
          f"window={float(win5) * 100:.5f}%")

    # M1-A4 [A]: the 5-decimal grade resolves BELOW the B2 attribution
    # scale (0.0255%); the 4-decimal grade does NOT.
    ratio = B2_ATTRIB_REL / float(win5)
    check("A", "A4 5-decimal v-window 0.0034% < B2 attribution scale "
               "0.0255% (ratio ~7.6) while 4-decimal window 0.0337% > it: "
               "only the 5-decimal grade can attribute the residual",
          float(win5) < B2_ATTRIB_REL < float(win4),
          f"B2/win5={ratio:.2f}")

    # M1-A5 [B]: the F4 anti-tuning target literal is on disk in the
    # honest-status note (declared input, not recomputed from PDG here).
    hs_text = HONEST_STATUS_NOTE.read_text()
    check("B", "A5 F4 anti-tuning target literal '0.5934379' verified on "
               "disk in the honest-status note (declared input)",
          "0.5934379" in hs_text and "LESS than the rounding half-step" in hs_text)

    # M1-A6 [A]: the F4 offset is below the 4-decimal half-step — the
    # licensed grid cannot encode it (0.5934379 rounds to 0.5934).
    offset = P_NEEDED_F4 - P_LICENSED        # = 379/10^7 = 3.79e-5
    rounded4 = Fraction(round(P_NEEDED_F4 * 10000), 10000)
    check("A", "A6 F4 offset = 0.5934379 - 0.5934 = +3.79e-5 < 5e-5 "
               "half-step; <P>_needed rounds to the licensed 0.5934 at 4 "
               "decimals (the licensed grid cannot encode the target)",
          offset == Fraction(379, 10000000) and offset < HALF_STEP_4
          and rounded4 == P_LICENSED,
          f"offset={float(offset):.3e}")

    # M1-A7 [A]: at 5 decimals the question separates: 0.5934379 rounds
    # to 0.59344, eight 5-decimal half-steps from 0.59340.
    rounded5 = Fraction(round(P_NEEDED_F4 * 100000), 100000)
    sep = rounded5 - Fraction(59340, 100000)
    check("A", "A7 5-decimal separation: round(0.5934379, 5) = 0.59344; "
               "0.59344 - 0.59340 = 4e-5 = EIGHT 5-decimal half-steps -> "
               "a 5-decimal certification is decisive on F4",
          rounded5 == Fraction(59344, 100000)
          and sep == 8 * HALF_STEP_5,
          f"separation={float(sep):.1e} = {sep / HALF_STEP_5} half-steps")

    # M1-A8 [A]: decision-grade table (printed; consistency checked).
    print("\n  Decision-grade table (M1):")
    print("    grade      total-error    rel. on <P>   |dv/v| window   decides")
    print(f"    4-decimal  < 5e-5         {float(rel4):.4e}    "
          f"{float(win4) * 100:.4f}%         B1 license: does <P> round to 0.5934?")
    print(f"    5-decimal  < 5e-6         {float(rel5):.4e}    "
          f"{float(win5) * 100:.5f}%        F4 / residual attribution: "
          "0.59344 vs 0.59340 (B1 vs B2)")
    check("A", "A8 decision-grade table consistency: 5-decimal target = "
               "4-decimal target / 10 exactly; both windows = 4 x relative "
               "target exactly",
          HALF_STEP_5 == HALF_STEP_4 / 10
          and win4 == 4 * rel4 and win5 == 4 * rel5)


# ---------------------------------------------------------------------------
# Vectorized full-lattice machinery (adapted from the reuse module's
# Metropolis-with-projected-near-identity-proposal update; reuse fidelity
# is checked in M2 against the imported scalar functions).
# ---------------------------------------------------------------------------
def batched_project_su3(z: np.ndarray) -> np.ndarray:
    q, r = np.linalg.qr(z)
    d = np.einsum("...ii->...i", r)
    ph = d / np.where(np.abs(d) == 0, 1.0, np.abs(d))
    q = q * np.conj(ph)[..., None, :]
    detq = np.linalg.det(q)
    return q * np.exp(-1j * np.angle(detq) / 3.0)[..., None, None]


def batched_near_identity(rng: np.random.Generator, n: int, eps: float) -> np.ndarray:
    h = rng.normal(size=(n, 3, 3)) + 1j * rng.normal(size=(n, 3, 3))
    h = (h + np.conj(np.swapaxes(h, -1, -2))) / 2.0
    tr = np.einsum("...ii->...", h) / 3.0
    h = h - tr[..., None, None] * np.eye(3)
    return batched_project_su3(np.eye(3, dtype=complex) + 1j * eps * h)


def dag(a: np.ndarray) -> np.ndarray:
    return np.conj(np.swapaxes(a, -1, -2))


def staple_field(U: np.ndarray, mu: int) -> np.ndarray:
    """Sum of staples A_mu(x) with Re Tr[U_mu(x) A_mu(x)] the local
    plaquette-trace contribution; summed over mu and x it equals
    4 sum_P Re Tr U_P (checked in M2)."""
    A = np.zeros_like(U[mu])
    for nu in range(NDIM):
        if nu == mu:
            continue
        Unu = U[nu]
        fwd = (np.roll(Unu, -1, axis=mu)
               @ dag(np.roll(U[mu], -1, axis=nu)) @ dag(Unu))
        Unu_m = np.roll(Unu, 1, axis=nu)
        Umu_m = np.roll(U[mu], 1, axis=nu)
        bwd = dag(np.roll(Unu_m, -1, axis=mu)) @ dag(Umu_m) @ Unu_m
        A = A + fwd + bwd
    return A


def vector_avg_plaquette(U: np.ndarray, L: int) -> float:
    tot = 0.0
    for mu in range(NDIM):
        for nu in range(mu + 1, NDIM):
            P = (U[mu] @ np.roll(U[nu], -1, axis=mu)
                 @ dag(np.roll(U[mu], -1, axis=nu)) @ dag(U[nu]))
            tot += float(np.einsum("...ii->...", P).real.sum())
    return tot / (6 * L**NDIM * N_C)


def metropolis_sweep(U: np.ndarray, rng: np.random.Generator, L: int,
                     beta: float, eps: float, nhits: int,
                     masks: list[np.ndarray]) -> float:
    """One checkerboard Metropolis sweep (same accept rule and proposal
    family as the reuse module's one-plaquette chain, vectorized)."""
    acc = 0
    tot = 0
    for mu in range(NDIM):
        for parity in (0, 1):
            A = staple_field(U, mu)
            m = masks[parity]
            for _ in range(nhits):
                R = batched_near_identity(rng, L**NDIM, eps).reshape(
                    L, L, L, L, 3, 3)
                Up = R @ U[mu]
                dS = -(beta / N_C) * np.einsum(
                    "...ij,...ji->...", Up - U[mu], A).real
                r = rng.random(size=(L,) * NDIM)
                accm = ((dS < 0) | (r < np.exp(-np.clip(dS, 0.0, 700.0)))) & m
                U[mu] = np.where(accm[..., None, None], Up, U[mu])
                acc += int(accm.sum())
                tot += int(m.sum())
    return acc / tot


def tau_int_windowed(x: np.ndarray, c: float, max_lag: int) -> tuple[float, int]:
    """Madras-Sokal integrated autocorrelation time with the automatic
    window: smallest W with W >= c * tau_int(W)."""
    n = len(x)
    xc = x - x.mean()
    var = float(np.var(x, ddof=0))
    tau = 0.5
    for w in range(1, max_lag):
        rho = float((xc[: n - w] * xc[w:]).sum() / ((n - w) * var))
        tau += rho
        if w >= c * tau:
            return tau, w
    return tau, max_lag


# ---------------------------------------------------------------------------
# Section M2 — statistics budget from smoke (the computable core).
# ---------------------------------------------------------------------------
def section_m2() -> None:
    print("\n--- Section M2 [C]/[A]: statistics budget from smoke "
          "(reused finite-MC machinery; L=4, beta=6, seed declared) ---")

    # M2-C1 [C]: reuse fidelity — batched projection vs the imported
    # module's scalar project_su3 on the same inputs.
    rng = np.random.default_rng(2026061101)
    zs = rng.normal(size=(20, 3, 3)) + 1j * rng.normal(size=(20, 3, 3))
    batched = batched_project_su3(zs)
    max_dev = max(float(np.abs(batched[i] - base.project_su3(zs[i])).max())
                  for i in range(20))
    check("C", "C1 reuse fidelity: batched SU(3) projection reproduces the "
               "imported module's project_su3 element-wise",
          max_dev < 1e-12, f"max dev={max_dev:.2e}")

    # M2-C2 [C]: batched proposals are unitary determinant-one.
    props = batched_near_identity(rng, 50, SMOKE_EPS)
    uni = float(np.abs(props @ dag(props) - np.eye(3)).max())
    det = float(np.abs(np.linalg.det(props) - 1.0).max())
    check("C", "C2 batched near-identity proposals are unitary and "
               "determinant-one (same proposal family as the reuse module)",
          uni < 1e-12 and det < 1e-12, f"uni={uni:.2e}, det={det:.2e}")

    # M2-C3 [C]: vectorized average plaquette vs the imported module's
    # reference implementation on an L=2 random configuration.
    rng2 = np.random.default_rng(2026061102)
    L2 = 2
    Uarr = np.empty((NDIM, L2, L2, L2, L2, 3, 3), dtype=complex)
    links_dict = {}
    for coords in np.ndindex(*([L2] * NDIM)):
        mats = [base.random_su3(rng2) for _ in range(NDIM)]
        links_dict[coords] = mats
        for mu in range(NDIM):
            Uarr[(mu,) + coords] = mats[mu]
    ref = base.average_plaquette(links_dict, L2)
    vec = vector_avg_plaquette(Uarr, L2)
    check("C", "C3 reuse fidelity: vectorized average plaquette matches the "
               "imported module's average_plaquette on an L=2 random config",
          abs(ref - vec) < 1e-12, f"|diff|={abs(ref - vec):.2e}")

    # M2-C4 [C]: staple identity sum_{mu,x} Re Tr[U A] = 4 sum_P Re Tr U_P.
    s_link = sum(float(np.einsum("...ij,...ji->...",
                                 Uarr[mu], staple_field(Uarr, mu)).real.sum())
                 for mu in range(NDIM))
    s_plaq = vec * 6 * L2**NDIM * N_C
    rel = abs(s_link - 4 * s_plaq) / abs(4 * s_plaq)
    check("C", "C4 staple identity: sum Re Tr[U_mu A_mu] = 4 x total "
               "plaquette trace sum (validates the local Delta_S used by "
               "the sweep)",
          rel < 1e-10, f"rel err={rel:.2e}")

    # M2-C5 [C]: the smoke chain (declared parameters; deterministic).
    print(f"\n  Smoke chain (declared): L={SMOKE_L}, beta={SMOKE_BETA}, "
          f"cold start, eps={SMOKE_EPS}, hits={SMOKE_NHITS}, "
          f"seed={SMOKE_SEED}, {SMOKE_N_THERM} therm + {SMOKE_N_MEAS} "
          "measurement sweeps")
    rng_mc = np.random.default_rng(SMOKE_SEED)
    L = SMOKE_L
    U = np.tile(np.eye(3, dtype=complex), (NDIM, L, L, L, L, 1, 1))
    parity = np.indices((L,) * NDIM).sum(axis=0) % 2
    masks = [parity == 0, parity == 1]

    t0 = time.perf_counter()
    therm_first = None
    for i in range(SMOKE_N_THERM):
        metropolis_sweep(U, rng_mc, L, SMOKE_BETA, SMOKE_EPS, SMOKE_NHITS, masks)
        if i == 0:
            therm_first = vector_avg_plaquette(U, L)
    acc_sum = 0.0
    series = np.empty(SMOKE_N_MEAS)
    for i in range(SMOKE_N_MEAS):
        acc_sum += metropolis_sweep(U, rng_mc, L, SMOKE_BETA, SMOKE_EPS,
                                    SMOKE_NHITS, masks)
        series[i] = vector_avg_plaquette(U, L)
    t1 = time.perf_counter()
    t_sweep = (t1 - t0) / (SMOKE_N_THERM + SMOKE_N_MEAS)
    acc = acc_sum / SMOKE_N_MEAS

    check("C", "C5 smoke chain ran; Metropolis acceptance inside the "
               "declared integrity band (0.30, 0.70)",
          0.30 < acc < 0.70, f"acceptance={acc:.3f}")

    # M2-C6 [C]: thermalization detected.
    mean = float(series.mean())
    sigma_p = float(series.std(ddof=1))
    h1 = float(series[: SMOKE_N_MEAS // 2].mean())
    h2 = float(series[SMOKE_N_MEAS // 2:].mean())
    tau, W = tau_int_windowed(series, TAU_WINDOW_C, max_lag=SMOKE_N_MEAS // 8)
    err_half = sigma_p * math.sqrt(2 * tau / (SMOKE_N_MEAS / 2))
    transient = therm_first is not None and therm_first > mean + 10 * sigma_p
    halves_ok = abs(h1 - h2) < 5 * math.sqrt(2) * err_half
    check("C", "C6 thermalization detected: cold-start transient (first-"
               "sweep P > mean + 10 sigma_P) was cut, and post-cut halves "
               "agree within 5x combined error",
          transient and halves_ok,
          f"P[1]={therm_first:.4f}, halves |{h1:.6f}-{h2:.6f}|="
          f"{abs(h1 - h2):.2e} vs {5 * math.sqrt(2) * err_half:.2e}")

    # M2-C7 [C]: tau_int automatic window converged.
    check("C", f"C7 tau_int windowed estimator converged: automatic window "
               f"W found with W >= {TAU_WINDOW_C} tau_int(W) and "
               f"W <= N/8",
          W >= TAU_WINDOW_C * tau * 0.999 and W <= SMOKE_N_MEAS // 8,
          f"tau_int={tau:.2f} sweeps, W={W}")

    err_mean = sigma_p * math.sqrt(2 * tau / SMOKE_N_MEAS)
    print(f"\n  Smoke measurements (DIAGNOSTIC ONLY — L=4 finite volume; "
          "NOT comparable to the")
    print("  infinite-volume 0.5934 target; certifies NOTHING about the "
          "value):")
    print(f"    <P>_smoke(L=4) = {mean:.5f} +/- {err_mean:.5f}   [fenced "
          "diagnostic]")
    print(f"    sigma_P (per-config) = {sigma_p:.6f}")
    print(f"    tau_int = {tau:.2f} sweeps (window W={W}, c={TAU_WINDOW_C})")
    print(f"    t_sweep(L=4) = {t_sweep * 1000:.2f} ms "
          "(this machine, this implementation)")

    # M2-C8 [C]: honesty fence — the smoke error is ABOVE certification
    # grade; the smoke run cannot certify and does not.
    check("C", "C8 honesty fence: smoke error of mean is ABOVE the "
               "4-decimal certification grade 5e-5 (the smoke run "
               "calibrates the budget and certifies NOTHING about the value)",
          err_mean > float(HALF_STEP_4), f"err={err_mean:.2e} >> 5e-5")

    # M2-C9 [A]: budget identities (exact given the measured inputs).
    n_indep_4 = (Z_SCORE * sigma_p / float(HALF_STEP_4)) ** 2
    n_indep_5 = (Z_SCORE * sigma_p / float(HALF_STEP_5)) ** 2
    sweeps_4 = n_indep_4 * 2 * tau
    sweeps_5 = n_indep_5 * 2 * tau
    check("A", "C9 budget identities: N_indep = (z sigma_P/target)^2 with "
               "z = 2; N_indep(5e-6) = 100 x N_indep(5e-5) exactly; "
               "sweeps = N_indep x 2 tau_int",
          abs(n_indep_5 / n_indep_4 - 100.0) < 1e-9
          and abs(sweeps_4 - n_indep_4 * 2 * tau) < 1e-9)

    # Budget table.  Declared cost model: t_sweep(L) = t_sweep(4) (L/4)^4
    # (work ~ number of links ~ L^4); conservative envelope holds sigma_P
    # and tau_int at their L=4 values; the declared variance-scaling
    # refinement sigma_P^2 ~ 1/L^4 divides the conservative wall-clock by
    # (L/4)^4 (total ~ L-independent), tau_int still held fixed.
    print("\n  Certification budget (from smoke; z = 2; this "
          "implementation, single core):")
    print(f"    N_indep(5e-5) = {n_indep_4:.3e}; sweeps = {sweeps_4:.3e}")
    print(f"    N_indep(5e-6) = {n_indep_5:.3e}; sweeps = {sweeps_5:.3e}")
    print("    Projected wall-clock [conservative | variance-scaled "
          "refinement]:")
    print("      L    t_sweep      4-decimal grade            "
          "5-decimal grade")
    for Lp in (8, 16, 24, 32):
        scale = (Lp / 4) ** 4
        ts = t_sweep * scale
        wc4 = sweeps_4 * ts
        wc5 = sweeps_5 * ts
        print(f"      {Lp:<3d}  {ts * 1000:9.1f} ms  "
              f"{wc4 / 3600:9.1f} h | {wc4 / scale / 3600:7.1f} h   "
              f"{wc5 / 3600:11.1f} h | {wc5 / scale / 3600:9.1f} h")
    print("    (Finite-volume plan: certify <P>_inf by the declared "
          "ansatz <P>_L = <P>_inf + c L^-4")
    print("     over L in {8, 12, 16, 24, 32}; see the parent note "
          "Section M3, step 6.)")

    # M2-C10 [C]: wall-clock measured and the declared smoke budget held.
    elapsed = t1 - t0
    check("C", "C10 per-sweep wall-clock measured and the smoke chain "
               "respected the declared < 120 s runner budget",
          t_sweep > 0 and elapsed < 120.0,
          f"t_sweep={t_sweep * 1000:.2f} ms, chain={elapsed:.1f} s")


# ---------------------------------------------------------------------------
# Section M3 — protocol specification and pre-registered decision bands.
# ---------------------------------------------------------------------------
def section_m3() -> None:
    print("\n--- Section M3 [B]/[A]: protocol specification and "
          "pre-registered decision bands ---")
    note = PARENT_NOTE.read_text()

    # M3-B1 [B]: the pre-registration block is in the note.
    required = [
        "## Pre-registration block",
        "Band A",
        "Band B-i",
        "Band B-ii",
        "Band C",
        "Band D",
        "declared BEFORE any production sweep",
        "can FALSIFY the bounded match",
    ]
    check("B", "B1 parent note carries the pre-registration block: bands "
               "A/B-i/B-ii/C/D declared before any production run, with "
               "the explicit falsification warning",
          all(s in note for s in required))

    # M3-B2 [A]: band-edge arithmetic — ordered, disjoint, exhaustive.
    edges_ok = (HALF_STEP_5 < HALF_STEP_4 < Fraction(1, 10000)
                and Fraction(1, 10000) == 2 * HALF_STEP_4)
    check("A", "B2 band edges ordered and exhaustive: 5e-6 < 5e-5 < 1e-4 "
               "with 1e-4 = 2 x half-step exactly; |d| <= 5e-5 (A), "
               "5e-5 < |d| <= 1e-4 (C), |d| > 1e-4 (D) partition the axis",
          edges_ok)

    # M3-B3 [A]: Band-C minimum displacement on v_cand is exactly 2x the
    # B1 window (deviation 1e-4 = 2 x 5e-5; elasticity -4 linear).
    disp_c_min = 4 * Fraction(1, 10000) / P_LICENSED
    win4 = 4 * HALF_STEP_4 / P_LICENSED
    check("A", "B3 broken-license displacement: |d| = 1e-4 moves v_cand by "
               "4 x 1e-4/0.5934 = 6.7408e-4 = 0.0674% = exactly 2x the B1 "
               "window (elasticity -4, linear in the deviation)",
          disp_c_min == 2 * win4
          and abs(float(disp_c_min) - 6.7408e-4) < 5e-9,
          f"min Band-C/D displacement={float(disp_c_min) * 100:.4f}%")

    # M3-B4 [B]: finite-volume extrapolation plan declared in the note.
    fv_ok = ("<P>_L = <P>_inf + c L^-4" in note
             and "L in {8, 12, 16, 24, 32}" in note)
    check("B", "B4 finite-volume plan declared: ansatz "
               "<P>_L = <P>_inf + c L^-4 at fixed beta = 6 over "
               "L in {8, 12, 16, 24, 32} (5 points, 2 fit parameters)",
          fv_ok and 5 >= 3)

    # M3-B5 [B]: the plaquette note's escape clause — the certificate this
    # protocol designs — is present on disk.
    plaq = PLAQUETTE_NOTE.read_text()
    check("B", "B5 plaquette-note escape clause on disk: downstream reuse "
               "of 0.5934 is licensed 'unless a separate retained MC "
               "certificate or analytic beta=6 closure is supplied' — this "
               "protocol designs exactly that certificate",
          "unless a separate retained MC certificate or analytic beta=6 "
          "closure is supplied" in plaq)


# ---------------------------------------------------------------------------
# Section M4 — Stage 2 (staircase flat-cost measurement): design only.
# ---------------------------------------------------------------------------
def section_m4() -> None:
    print("\n--- Section M4 [B] + residuals: Stage 2 staircase flat-cost "
          "measurement (design only) ---")
    note = PARENT_NOTE.read_text()

    # M4-B6 [B]: the flat per-rung target literal on disk.
    ac = ACTION_COST_NOTE.read_text()
    check("B", "B6 Stage-2 target literal on disk: the action-cost note "
               "carries the flat per-rung staircase prediction "
               "Delta_S = 2.270081 (k-independent; T4 consequence 2 is "
               "what a Stage-2 measurement would contrast)",
          "2.270081" in ac and "independent of the threshold index k" in ac)

    # M4-B7 [B]: the parent note fences Stage 2 as design-only.
    check("B", "B7 parent note fences Stage 2 as design-only pending "
               "Stage 1 (no Stage-2 computation anywhere in this block)",
          "design-only pending Stage 1" in note
          and "spectral flow" in note)

    residual("R1: the Stage-1 certification is NOT performed here. The "
             "smoke run calibrates the statistics budget only; the "
             "pre-registered decision bands await a production run at "
             "the M3 protocol's scales.")
    residual("R2: Stage 2 (the per-rung flat-cost measurement: spectral "
             "flow of the staggered operator under blocking; "
             "per-threshold condensate shares) is DESIGN-ONLY, pending "
             "Stage 1; it is multi-scale and strictly harder.")
    residual("R3: the plaquette note's status is UNCHANGED by this block: "
             "<P> = 0.5934 remains an admitted reuse number under the B1 "
             "license until the pre-registered production run lands a "
             "retained MC certificate (or an analytic beta=6 closure is "
             "supplied).")


# ---------------------------------------------------------------------------
# Terminal class-D fence (external comparators).
# ---------------------------------------------------------------------------
def section_fence() -> None:
    print("\n--- Terminal class-D fence: external comparators ---")
    print("  (The canonical 0.5934 enters this runner ONLY as the licensed "
          "target of the")
    print("   certification protocol — B1 reuse license, "
          "PLAQUETTE_SELF_CONSISTENCY_NOTE.md.")
    print("   The smoke <P> estimate is a fenced finite-volume diagnostic, "
          "never compared")
    print("   to it. The one PDG-derived quantity below is context only; "
          "no load-bearing")
    print("   PASS rests on it.)")

    # D1 [D]: the F4 offset, pushed through elasticity -4, reproduces the
    # honest-status comparator-residual scale (0.025513%) — context only:
    # this is WHY Band B-i re-attributes the residual to B1.
    resid_from_offset = 4 * float(P_NEEDED_F4 - P_LICENSED) / float(P_LICENSED)
    check("D", "D1 fenced context: F4 offset x elasticity = "
               "4 x 3.79e-5/0.5934 = 2.5548e-4, the honest-status "
               "comparator-residual scale (~0.0255%) — a Band B-i landing "
               "re-attributes exactly that residual from B2 to B1",
          abs(resid_from_offset - 2.5513e-4) < 2e-6,
          f"4x offset/<P> = {resid_from_offset * 100:.4f}%")

    # D2 [D]: self-scan — the PDG VEV literal is absent from this source.
    src = Path(__file__).read_text()
    pdg_literal = "246." + "22"  # composed so the scan finds only real uses
    check("D", "D2 self-scan: the PDG VEV literal appears ZERO times in "
               "this runner's source — no comparator consumed anywhere",
          src.count(pdg_literal) == 0)


def main() -> int:
    print("=" * 78)
    print(" frontier_plaquette_mc_certification_protocol_smoke_2026_06_11.py")
    print(" Block13: MEASUREMENT-FALLBACK PROTOCOL — Stage 1: MC "
          "certification of <P>")
    print(" at beta = 6 to 5 decimals (precision targets derived exactly; "
          "statistics")
    print(" budget calibrated from a deterministic L=4 smoke run; decision "
          "bands")
    print(" PRE-REGISTERED).  Stage 2 (staircase flat-cost) design-only.")
    print(" The certification itself is NOT performed: smoke numbers "
          "calibrate the")
    print(" budget and certify NOTHING about the value.")
    print(" Parent note: docs/PLAQUETTE_MC_CERTIFICATION_PROTOCOL_"
          "NOTE_2026-06-11.md")
    print("=" * 78)

    section_m1()
    section_m2()
    section_m3()
    section_m4()
    section_fence()

    print()
    print("=" * 78)
    print(f" Breakdown: A={CLASS_COUNTS['A']} B={CLASS_COUNTS['B']} "
          f"C={CLASS_COUNTS['C']} D={CLASS_COUNTS['D']} "
          f"RESIDUAL={RESIDUAL_COUNT}")
    print(f" TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(" VERDICT: established (bounded): the precision-target arithmetic "
          "is exact —")
    print("   4-decimal grade (< 5e-5) decides the B1 license, 5-decimal "
          "grade (< 5e-6)")
    print("   decides F4 / the B1-vs-B2 residual attribution (0.59344 vs "
          "0.59340, eight")
    print("   5-decimal half-steps apart); the smoke run is a calibration "
          "DIAGNOSTIC")
    print("   (sigma_P, tau_int, t_sweep measured; budget table computed; "
          "the smoke <P>")
    print("   is fenced and certifies nothing); the decision bands are "
          "pre-registered in")
    print("   the parent note BEFORE any production run, keeping the F4 "
          "anti-tuning")
    print("   certificate meaningful — and the production measurement can "
          "FALSIFY the")
    print("   bounded match, which is its scientific value.  NOT "
          "established: any")
    print("   certified value of <P> (Stage 1 not performed); any Stage-2 "
          "measurement")
    print("   (design-only).  The plaquette note's B1 license is unchanged "
          "by this row.")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
