#!/usr/bin/env python3
"""
Hierarchy-VALUE frontier probe — decade accounting for the Planck -> EW and
Planck -> charged-lepton mass hierarchies.

Authority: docs/HIERARCHY_VALUE_FRONTIER_PROBE_2026-06-05.md  (claim_type=meta)

The framework AVOIDS the hierarchy PROBLEM (no fundamental scalar m_H^2 ->
no relevant-operator fine-tuning; established in
SCALE_AXIS_HIERARCHY_TRANSMUTATION_SCOPING_2026-06-05 and the absence of an
	m_H^2 counterterm in the Lattice + Quantum + Record baseline). This probe addresses the
VALUE question: which decade-budget mechanisms the framework supplies, and
which decades remain unpinned.

It introduces NO new axiom, selector, import, or fit. PDG masses, the Cabibbo
angle, and Froggatt-Nielsen charge ladders enter ONLY as post-hoc comparators,
never as derivation inputs. The Froggatt-Nielsen integer-charge readout in
Section 4 is reported as a BOUNDED NUMERICAL OBSERVATION (a coincidence-or-not
flag), explicitly NOT a derivation and explicitly NOT a framework mechanism
(positing FN charges would be an unauthorized import).

Three angles from the probe brief:

  Angle 1 (gauge cascade / single dimensional transmutation).
    Reproduces the sister-branch SCALE_AXIS result: the framework's O(1)
    Planck coupling (1/alpha ~ 11) transmutes only ~4 decades via a single
    1-loop gauge pole exp(-2pi/(b0 alpha)), short of the ~17 (EW) needed.
    Also: does a SEQUENCE of the three SM gauge factors COMPOUND to the
    full hierarchy? (Answer: no -- see Section 1.)

  Angle 2 (Yukawa-sector / power-of-a-small-parameter for the lepton scale).
    The framework's ACTUAL EW formula is a 16th POWER of alpha_LM
    (v = M_Pl (7/8)^(1/4) alpha_LM^16), not a single transmutation. The
    16-fold power already supplies ~17 decades. The charged-lepton scale
    needs ~19-22 decades = the EW ~17 PLUS the small Yukawa y_l. This
    section accounts the small-Yukawa decades and tests whether y_l is a
    clean power of a framework small parameter.

  Angle 3 (is 1/alpha~11 the right input, or a weaker derived coupling).
    Compares the framework bare 1/alpha~11 against the 1/alpha~43-52 that a
    single transmutation WOULD need, and against alpha_s(M_Z) run UP to M_Pl.

Total expected check count is printed at the end as TOTAL: PASS=N FAIL=0.
"""

from __future__ import annotations

import math
import sys

from canonical_plaquette_surface import (
    CANONICAL_ALPHA_BARE,
    CANONICAL_ALPHA_LM,
    CANONICAL_ALPHA_S_V,
    CANONICAL_U0,
)

# ---------------------------------------------------------------------------
# Inputs.  Framework-side: M_Pl (Planck lane), canonical plaquette surface.
# PDG-side: masses, Cabibbo angle, alpha_s(M_Z) -- COMPARATORS ONLY.
# ---------------------------------------------------------------------------

M_PL = 1.2209e19  # GeV  (framework UV scale anchor, Planck lane; primitive P1)
APBC = (7.0 / 8.0) ** 0.25  # (7/8)^(1/4) APBC selector

ALPHA_BARE = CANONICAL_ALPHA_BARE     # 1/(4 pi)         ~ 0.0796
ALPHA_LM = CANONICAL_ALPHA_LM         # alpha_bare / u_0 ~ 0.0907
ALPHA_S_V = CANONICAL_ALPHA_S_V       # alpha_bare / u_0^2 ~ 0.1033
U0 = CANONICAL_U0

# PDG 2024 comparators (NOT derivation inputs).
V_OBS = 246.22          # GeV  electroweak VEV
M_E = 0.51099895e-3     # GeV
M_MU = 0.1056583755     # GeV
M_TAU = 1.77686         # GeV
ALPHA_S_MZ = 0.1180     # alpha_s(M_Z), PDG
M_Z = 91.1880           # GeV
CABIBBO = 0.2250        # sin(theta_C), Wolfenstein lambda

# Framework 1-loop beta-coefficients (their OWN derived catalog; used as
# comparators for the single-transmutation benchmark only).
B3_FULL_SM = 7.0        # SU(3)_c, full SM content
B3_PURE_GAUGE = 11.0    # SU(3)_c, pure gauge

V_CHAIN_PUBLISHED = 246.282818290129  # GeV  canonical-chain published value


def _line(label: str, ok: bool) -> bool:
    print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    return ok


def _close(a: float, b: float, tol: float, label: str) -> bool:
    ok = abs(a - b) <= tol * max(abs(b), 1e-300)
    return _line(label, ok)


def _yukawa(mass: float) -> float:
    """SM tree relation m = y v / sqrt(2) -> y = sqrt(2) m / v."""
    return math.sqrt(2.0) * mass / V_OBS


def _decades(ratio: float) -> float:
    return math.log10(ratio)


def _power_law_exponent(target: float) -> float:
    """n such that target = M_PL * APBC * alpha_LM^n."""
    return math.log(target / (M_PL * APBC)) / math.log(ALPHA_LM)


def main() -> int:  # noqa: C901  (single linear verification script)
    passes = 0
    fails = 0

    def chk(ok: bool) -> None:
        nonlocal passes, fails
        if ok:
            passes += 1
        else:
            fails += 1

    print("=" * 72)
    print("HIERARCHY-VALUE FRONTIER PROBE 2026-06-05")
    print("=" * 72)
    print(f"  M_Pl        = {M_PL:.4e} GeV   (framework UV anchor, P1)")
    print(f"  <P>         = 0.5934   u_0 = {U0:.5f}")
    print(f"  alpha_bare  = {ALPHA_BARE:.5f}  (1/alpha = {1/ALPHA_BARE:.3f})")
    print(f"  alpha_LM    = {ALPHA_LM:.5f}  (1/alpha = {1/ALPHA_LM:.3f})")
    print(f"  alpha_s(v)  = {ALPHA_S_V:.5f}  (1/alpha = {1/ALPHA_S_V:.3f})")
    print()

    # ----- Section 0: the hierarchy depths (the numbers we must explain) -----
    print("-" * 72)
    print("SECTION 0  Hierarchy depths (PDG comparators)")
    print("-" * 72)
    d_v = _decades(V_OBS / M_PL)
    d_tau = _decades(M_TAU / M_PL)
    d_mu = _decades(M_MU / M_PL)
    d_e = _decades(M_E / M_PL)
    print(f"  log10(v    / M_Pl) = {d_v:8.3f}   (EW scale)")
    print(f"  log10(m_tau/ M_Pl) = {d_tau:8.3f}")
    print(f"  log10(m_mu / M_Pl) = {d_mu:8.3f}")
    print(f"  log10(m_e  / M_Pl) = {d_e:8.3f}   (deepest: the ~22-decade target)")
    # The brief states ~17 (EW) and ~22 (lepton).  Verify those framings.
    chk(_line("S0.1 EW depth ~ 17 decades (|log10(v/M_Pl)| in [16,17.5])",
              16.0 <= -d_v <= 17.5))
    chk(_line("S0.2 deepest lepton (m_e) depth ~ 22 decades (in [22,23])",
              22.0 <= -d_e <= 23.0))
    print()

    # ----- Section 1: Angle 1 -- single transmutation + gauge cascade -----
    print("-" * 72)
    print("SECTION 1  Angle 1: single 1-loop gauge transmutation + cascade")
    print("-" * 72)

    def single_dt_log10(b0: float, alpha: float) -> float:
        # Lambda/M_UV = exp(-2pi/(b0 alpha)); return log10 of that ratio.
        return (-2.0 * math.pi / (b0 * alpha)) / math.log(10.0)

    dt_su3_full = single_dt_log10(B3_FULL_SM, ALPHA_LM)
    dt_su3_pure = single_dt_log10(B3_PURE_GAUGE, ALPHA_LM)
    print(f"  single DT, SU(3) full-SM  (b0=7,  alpha_LM): {dt_su3_full:7.2f} decades")
    print(f"  single DT, SU(3) puregauge (b0=11, alpha_LM): {dt_su3_pure:7.2f} decades")
    # The sister-branch headline: ~4 decades, not ~17.
    chk(_line("S1.1 single gauge DT delivers only ~4 decades (|.|<6, full-SM)",
              abs(dt_su3_full) < 6.0))

    # Cascade: does SUMMING the three SM gauge factors compound to ~17?
    # Best-case compounding = adding the (negative log10) of each single pole.
    # Use each factor's most-suppressing framework benchmark.
    b2 = 19.0 / 6.0  # SU(2)_L 1-loop coefficient (framework catalog)
    dt_su2 = single_dt_log10(b2, ALPHA_BARE)
    # U(1)_Y is NOT asymptotically free (b1<0): it has NO IR pole / no
    # transmutation suppression.  Its cascade contribution is 0 decades.
    cascade_sum = dt_su3_full + dt_su2 + 0.0
    print(f"  single DT, SU(2)_L (b0=19/6, alpha_bare):    {dt_su2:7.2f} decades")
    print(f"  U(1)_Y (b1<0, not asymptotically free):        0.00 decades (no IR pole)")
    print(f"  CASCADE sum (SU3+SU2+U1):                     {cascade_sum:7.2f} decades")
    print(f"  needed for EW:                               {d_v:7.2f} decades")
    # Honest finding: even the optimistic cascade SUM overshoots/undershoots
    # and is not a controlled mechanism (the factors live at different
    # thresholds and do not multiply a single ruler).  Record that the
    # cascade SUM does not equal the EW depth in a controlled way: the SU(2)
    # pole alone already blows past v by sitting far below it, while SU(3)
    # stops ~13 decades short.  No single combination reproduces -16.7
    # without tuning which factors to include.
    chk(_line("S1.2 SU(3) full-SM cascade term stops >10 decades short of v",
              (-dt_su3_full) < (-d_v) - 10.0))
    # No SINGLE gauge factor reaches v: SU(3) stops ~12 decades short, SU(2)
    # ~6 decades short.  The naive SUM (-15.1) lands close to v (-16.7) only
    # if you select exactly {SU3 full-SM, SU2} AND drop the non-AF U(1) --
    # an uncontrolled post-hoc selection, not a mechanism multiplying a
    # common ruler.
    chk(_line("S1.3 no single gauge factor reaches v (each >5 decades short)",
              (-dt_su3_full) < (-d_v) - 5.0 and (-dt_su2) < (-d_v) - 5.0))
    chk(_line("S1.4 cascade SUM lands near v only by post-hoc factor "
              "selection (|sum-v|<3 but not controlled)",
              abs(cascade_sum - d_v) < 3.0))
    print("  => cascade is NOT a controlled compounding: the gauge factors do")
    print("     not multiply a common ruler; including/excluding factors to")
    print("     hit -16.7 would be a post-hoc selection (no mechanism).")
    print()

    # ----- Section 2: Angle 2a -- the framework's ACTUAL EW mechanism -----
    print("-" * 72)
    print("SECTION 2  Angle 2a: the framework's actual EW formula is a 16th")
    print("           POWER of alpha_LM (NOT a single transmutation)")
    print("-" * 72)
    v_pred = M_PL * APBC * ALPHA_LM ** 16
    print(f"  v = M_Pl (7/8)^(1/4) alpha_LM^16 = {v_pred:.4f} GeV")
    print(f"  PDG v_obs = {V_OBS} GeV   (rel dev {100*(v_pred-V_OBS)/V_OBS:+.4f} %)")
    chk(_close(v_pred, V_CHAIN_PUBLISHED, 1e-9,
               "S2.1 reproduces canonical-chain v = 246.2828... GeV"))
    chk(_close(v_pred, V_OBS, 3e-3,
               "S2.2 matches PDG v_obs within 0.3%"))
    # The exponent for v is EXACTLY 16 (integer); the suppression is the
    # 16-fold power, each factor of alpha_LM contributing ~log10(alpha_LM).
    n_v = _power_law_exponent(V_OBS)
    per_factor = _decades(ALPHA_LM)
    print(f"  power-law exponent for v:        n = {n_v:.4f}  (integer 16)")
    print(f"  decades per alpha_LM factor:     {per_factor:.4f}")
    print(f"  16 x per-factor:                 {16*per_factor:.4f}  (vs {d_v:.3f})")
    chk(_line("S2.3 v exponent is the integer 16 (|n-16|<0.01)",
              abs(n_v - 16.0) < 0.01))
    # Contrast with the DELTA0 gate: alpha_LM^16 = alpha_bare^16 u_0^-16, and
    # the suppression is dominated by alpha_bare^16 = (4 pi)^-16.
    abare16 = ALPHA_BARE ** 16
    print(f"  alpha_LM^16            = {ALPHA_LM**16:.4e}")
    print(f"  alpha_bare^16=(4pi)^-16= {abare16:.4e}  (DELTA0 gate: open transport)")
    chk(_close(ALPHA_LM ** 16, abare16 * U0 ** (-16), 1e-12,
               "S2.4 alpha_LM^16 = alpha_bare^16 u_0^-16 (DELTA0 algebra)"))
    print("  => the ~17 EW decades come from the 16th POWER (compounded),")
    print("     dominated by (4 pi)^-16; transport origin is the open DELTA0")
    print("     gate.  This is bounded-match, P1-P4 open -- NOT newly closed.")
    print()

    # ----- Section 3: Angle 2b -- the lepton scale = EW x small Yukawa -----
    print("-" * 72)
    print("SECTION 3  Angle 2b: lepton scale = (alpha_LM^16 EW) x (small y_l)")
    print("-" * 72)
    y_e, y_mu, y_tau = _yukawa(M_E), _yukawa(M_MU), _yukawa(M_TAU)
    print(f"  y_e   = {y_e:.4e}  (adds {_decades(y_e):+.3f} decades below v)")
    print(f"  y_mu  = {y_mu:.4e}  (adds {_decades(y_mu):+.3f} decades below v)")
    print(f"  y_tau = {y_tau:.4e}  (adds {_decades(y_tau):+.3f} decades below v)")
    print()
    print("  DECADE LEDGER (deepest = m_e):")
    print(f"    M_Pl -> v       : {d_v:8.3f}  (alpha_LM^16, bounded, P1-P4 open)")
    print(f"    v    -> m_e      : {_decades(y_e):8.3f}  (small Yukawa y_e, OPEN lane)")
    print(f"    total M_Pl->m_e  : {d_e:8.3f}  (= ~22 decades)")
    # Verify the ledger closes up to the sqrt(2) of the m = y v / sqrt(2)
    # convention: log10(v/M_Pl) + log10(y_e) = log10(m_e/M_Pl) + log10(sqrt2).
    chk(_close(d_v + _decades(y_e), d_e + _decades(math.sqrt(2.0)), 1e-6,
               "S3.1 ledger closes (up to sqrt2 of m=y v/sqrt2 convention)"))
    # The lepton power-law exponents are NON-integer (16 + small-Yukawa).
    n_tau = _power_law_exponent(M_TAU)
    n_mu = _power_law_exponent(M_MU)
    n_e = _power_law_exponent(M_E)
    print(f"  power-law exponents:  n(m_tau)={n_tau:.3f}  n(m_mu)={n_mu:.3f}"
          f"  n(m_e)={n_e:.3f}")
    chk(_line("S3.2 lepton exponents are NON-integer (m_e: frac part > 0.1)",
              abs(n_e - round(n_e)) > 0.1))
    print("  => the EXTRA lepton decades (~2 to ~5.5) ride on the small")
    print("     Yukawas y_l, which the framework does NOT derive (y_tau lane")
    print("     'stuck'; see CHARGED_LEPTON_Y_TAU_MECHANISM_STUCK_FANOUT).")
    print()

    # ----- Section 4: small-Yukawa = power of a small parameter? (FN test) -----
    print("-" * 72)
    print("SECTION 4  Is y_l a clean power of a framework small parameter?")
    print("           (BOUNDED NUMERICAL OBSERVATION -- NOT a derivation,")
    print("            NOT a framework mechanism, FN charges are an import)")
    print("-" * 72)

    def fn_charge(y: float, eps: float) -> float:
        # y ~ eps^q  ->  q = ln(y)/ln(eps).
        return math.log(y) / math.log(eps)

    for eps, lbl in [
        (ALPHA_BARE, "alpha_bare=1/(4pi)"),
        (ALPHA_LM, "alpha_LM"),
        (CABIBBO, "Cabibbo lambda=0.225 (comparator)"),
    ]:
        qe = fn_charge(y_e, eps)
        qmu = fn_charge(y_mu, eps)
        qtau = fn_charge(y_tau, eps)
        print(f"  eps={lbl:34s}: q(y_e)={qe:6.3f} q(y_mu)={qmu:6.3f}"
              f" q(y_tau)={qtau:6.3f}")
    # The cleanest near-integer ladder is eps=alpha_bare: q ~ (5.0, 2.9, 1.8).
    qe_ab = fn_charge(y_e, ALPHA_BARE)
    qmu_ab = fn_charge(y_mu, ALPHA_BARE)
    print(f"  -> eps=alpha_bare: q(y_e)={qe_ab:.3f} (~5), q(y_mu)={qmu_ab:.3f}"
          f" (~3): suggestive integer ladder, but loose (y_tau~1.81 != 2).")
    # Record honestly: this is a NUMERICAL near-coincidence (some charges
    # within ~0.1 of integers, y_tau off by ~0.19), NOT a derivation.  We do
    # NOT assert it; we flag it as an open path.  The check verifies only the
    # arithmetic (that q(y_mu) with eps=alpha_bare rounds to 3), not any claim.
    chk(_line("S4.1 [observation] q(y_mu | eps=alpha_bare) rounds to 3",
              round(qmu_ab) == 3))
    chk(_line("S4.2 [honesty] ladder is LOOSE: q(y_tau|alpha_bare) not within "
              "0.1 of 2", abs(fn_charge(y_tau, ALPHA_BARE) - 2.0) > 0.1))
    print()

    # ----- Section 5: Angle 3 -- is 1/alpha~11 the right input? -----
    print("-" * 72)
    print("SECTION 5  Angle 3: is the framework's 1/alpha~11 the right input?")
    print("-" * 72)
    # 1/alpha a single DT WOULD need to reach v with b0=7:
    need_alpha_v = -2.0 * math.pi / (B3_FULL_SM * math.log(V_OBS / M_PL))
    print(f"  single DT (b0=7) reaching v would need 1/alpha = "
          f"{1/need_alpha_v:.2f}")
    print(f"  framework actually has                1/alpha ~ {1/ALPHA_LM:.2f}")
    # alpha_s(M_Z) run UP to M_Pl (1-loop, b0=7): independent 'correct' UV value.
    # 1/alpha(M_Pl) = 1/alpha(M_Z) + (b0/2pi) ln(M_Pl/M_Z).
    inv_alpha_pl = 1.0 / ALPHA_S_MZ + (B3_FULL_SM / (2 * math.pi)) * math.log(
        M_PL / M_Z
    )
    print(f"  alpha_s(M_Z)=0.118 run UP to M_Pl (1-loop b0=7): 1/alpha = "
          f"{inv_alpha_pl:.2f}")
    chk(_line("S5.1 single-DT-to-v needs 1/alpha ~ 40-45 (framework has ~11)",
              40.0 <= 1 / need_alpha_v <= 45.0))
    chk(_line("S5.2 physical alpha_s(M_Z) run up gives 1/alpha(M_Pl) ~ 50-54",
              50.0 <= inv_alpha_pl <= 54.0))
    print("  => the framework's bare coupling is ~4-5x too STRONG for a single")
    print("     transmutation to span the hierarchy.  The framework instead")
    print("     uses the 16th POWER (Section 2), which DOES span ~17 decades")
    print("     at 1/alpha~11.  So the EW decades are mechanism-supplied (the")
    print("     power-law, bounded); the open gate is the (4pi)^-16 transport")
    print("     origin (DELTA0), not the decade COUNT.")
    print()

    # ----- Verdict -----
    print("=" * 72)
    print("VERDICT: FRAMEWORK-AVOIDS-PROBLEM; EW ~17 DECADES SUPPLIED BY THE")
    print("alpha_LM^16 POWER-LAW (bounded, P1-P4/DELTA0 open); LEPTON EXTRA")
    print("~2-5.5 DECADES RIDE ON UNDERIVED SMALL YUKAWAS (y_tau lane open).")
    print("Best mechanism-supplied decade count: 16.7 (EW power-law).")
    print("Single gauge transmutation: only ~4 decades (sister-branch result).")
    print("=" * 72)
    print(f"TOTAL: PASS={passes} FAIL={fails}")
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
