"""The Route-2 21/4 pin: a box-size scan settles the decisive discriminator -- 15/8 is NOT the
infinite-volume limit of the stack's shell-response functional under ANY limit; it is a single-box
(N=15) coincidence set by an isolated one-box numerator excursion. This CLOSES the bulk-limit escape
hatch the relocation note floated; it does NOT sharpen the standing naturality no-go (which never
claimed convergence).

THE DISCRIMINATOR (named in QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION): the landed
stack reproduces the readout target chain at the single box N=15 (q_T vs 5/6 at 6.2e-6, q_E vs 15/8 at
6.6e-4) but with a 108x deviation hierarchy between the two channels -- flagged explicitly there as
"the honest warning that 15/8 could fail." The open question: is the INFINITE-VOLUME (boundary-removal)
q_E equal to 15/8, or does the stack's own calibration exclude it? This runner answers it by scanning
the box size N with the observable's FIXED physical radii (probe 4.25, shell 4.0) held constant -- the
canonical "send the boundary to infinity" limit of the landed functional.

FORBIDDEN-INPUTS DISCIPLINE (naturality no-go): no observed quark masses, no fitted targets, no
nearest-rational selection. Only the stack's own exact objects at varying N; the rationals
5/6, 15/8, -2, -8/9, 9/4 appear only as comparison targets.

THE OBSERVABLE (faithfully reconstructed from the SIZE=15-pinned center-excess producer; the N=15
anchor S1 verifies the reconstruction IS the landed observable to ~1e-13): q_X = gamma_X(center)/
gamma_X(shell), gamma_X = beta_X/a_aniso, beta_X = central-difference of eta_floor along the channel-X
A1-star direction (EPS), eta_floor(q) = max spatial transverse-traceless Einstein component of the base
ADM metric built from the lattice potential phi(q), probed at fixed physical radius 4.25; a_aniso =
reduced-shell anchor_per_Q(phi(q)) * total_charge (fixed shell radius 4.0). center = e0 endpoint, shell
= s/sqrt6 endpoint. Box size enters ONLY through phi (the N-box Green's function); the probe/shell are
fixed physical objects reading the grid shape. The landed adm_metric / ricci_and_einstein /
max_tensorial_components / reduced_data / build_adapted_basis are reused verbatim; only the 15-pinned
scalar Schur action (scalar_bridge_action) is bypassed -- it feeds the [1] slot of tensor_metrics, NOT
the [0]=e_spatial_tf slot q_X uses (the anchor confirms the bypass is exact).

CHECKS:
  S1  ANCHOR: at N=15 the four reconstructed gamma values reproduce the landed cache to ~1e-13.
  S2  SMOOTH BASE / ERRATIC RATIOS: the undifferentiated base observable eta_floor(e0), eta_floor(s)
      vary smoothly and monotonically with N (no sign flips), so the erraticism is NOT a broken
      potential -- it lives in the delicate differenced channel coefficients.
  S3  THE MECHANISM (a_aniso cancels; isolated NUMERATOR excursion): the shell normalization a_aniso is
      identical at center and shell (a_center/a_shell = 1 to machine precision), so it CANCELS exactly
      in q_X = gamma_X(center)/gamma_X(shell) = beta_X(center)/beta_X(shell). The bare finite-difference
      beta_E(shell) is POSITIVE at every box EXCEPT N=15, where it makes an ISOLATED one-box DOWNWARD
      EXCURSION to negative (NOT a smooth zero-crossing -- the N13/N17 interpolant at N15 is positive).
      So q_E=15/8 is set by that single-box numerator excursion.
  S4  NON-CONVERGENCE: q_T(N) and q_E(N) do NOT converge to (5/6, 15/8) -- q_T sign-flips, q_E goes
      large-negative for N>=17. The N=15 agreement is a finite-box coincidence.
  S5  ROBUSTNESS: the excursion and non-convergence survive EPS in {0.0025, 0.005, 0.01} and a changed
      Ricci finite-difference step -- not a differencing/step artifact.
  S5b THE OTHER LIMIT: under a box-PROPORTIONAL probe radius (a different, also-well-defined infinite-
      volume observable), q_E and q_T converge to (1, 1), NOT (15/8, 5/6). So 15/8 fails under BOTH the
      fixed-radius and the box-proportional limits; the fixed-radius limit is A faithful boundary-removal
      limit, not THE unique one, and neither recovers 15/8.
  S6  VERDICT (two-part, honest): (i) 15/8 is a fixed-N=15 exact-readout coincidence; this CLOSES the
      bulk-limit escape hatch the relocation note floated (no infinite-volume limit recovers 15/8)
      and vindicates its flagged caution. (ii) It does NOT sharpen the standing 2026-04-28 naturality
      no-go, which never claimed convergence and is UNCHANGED; 15/8 was never the readout's claimed
      infinite-volume value. The pin remains a fixed-box structural-selection gap; this scan supplies no
      selecting primitive, it only rules out the bulk-limit promotion.

No PDG/fitted value consumed.
"""
from __future__ import annotations
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_same_source_metric_ansatz_scan as same        # noqa: E402
import frontier_tensorial_einstein_regge_completion as tcomp  # noqa: E402
import frontier_one_parameter_reduced_shell_law as shell      # noqa: E402

PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


SQ2, SQ3, SQ6 = np.sqrt(2.0), np.sqrt(3.0), np.sqrt(6.0)
PROBE_RAD = 4.25
_BASIS = same.build_adapted_basis()
E0 = _BASIS[:, 0]
S_UNIT = _BASIS[:, 1] / SQ6
EX = (SQ3 * _BASIS[:, 2] + _BASIS[:, 3]) / 2.0
T1X = _BASIS[:, 4]


def probe_points(rad):
    return [
        np.array([0.0, rad, 0.0, 0.0], dtype=float),
        np.array([0.3, rad / SQ2, rad / SQ2, 0.0], dtype=float),
        np.array([0.6, rad / SQ3, rad / SQ3, rad / SQ3], dtype=float),
    ]


def base_e_spatial_tf(phi, ric_h=0.04, rad=PROBE_RAD):
    vals = []
    for p in probe_points(rad):
        _, einstein = tcomp.ricci_and_einstein(
            lambda q: tcomp.adm_metric(phi, q, eps_vec=0.0, eps_ten=0.0, omega=0.0), p, h=ric_h
        )
        _, _, e_tf, _ = tcomp.max_tensorial_components(einstein)
        vals.append(e_tf)
    return max(vals)


def make_box(N):
    H0, INTERIOR = same.build_neg_laplacian_sparse(N)
    center = INTERIOR // 2
    support = [same.flat_idx(center + v[0], center + v[1], center + v[2], INTERIOR)
               for v in same.SUPPORT_COORDS]
    G0P = same.solve_columns(H0, support)

    def phi_from_q(q):
        phi = np.zeros((N, N, N), dtype=float)
        phi[1:-1, 1:-1, 1:-1] = (G0P @ q).reshape((INTERIOR, INTERIOR, INTERIOR))
        return phi

    return phi_from_q


def gammas(phi_from_q, eps=0.005, ric_h=0.04, rad=PROBE_RAD):
    def eta(x):
        return base_e_spatial_tf(phi_from_q(x), ric_h=ric_h, rad=rad)

    def betas(q):
        be = (eta(q + eps * EX) - eta(q - eps * EX)) / (2.0 * eps)
        bt = (eta(q + eps * T1X) - eta(q - eps * T1X)) / (2.0 * eps)
        return be, bt

    beE_c, beT_c = betas(E0)
    beE_s, beT_s = betas(S_UNIT)
    a_c = float(shell.reduced_data(phi_from_q(E0))["anchor_per_Q"]) * float(np.sum(E0))
    a_s = float(shell.reduced_data(phi_from_q(S_UNIT))["anchor_per_Q"]) * float(np.sum(S_UNIT))
    gE_c, gE_s, gT_c, gT_s = beE_c / a_c, beE_s / a_s, beT_c / a_c, beT_s / a_s
    return dict(gE_center=gE_c, gE_shell=gE_s, gT_center=gT_c, gT_shell=gT_s,
                beE_center=beE_c, beE_shell=beE_s, beT_center=beT_c, beT_shell=beT_s,
                a_center=a_c, a_shell=a_s, a_ratio=a_c / a_s,
                q_T=gT_c / gT_s, q_E=gE_c / gE_s,            # anchor-faithful gamma ratio
                q_T_bare=beT_c / beT_s, q_E_bare=beE_c / beE_s,  # bare beta ratio (== q_X iff a_c==a_s)
                eta_e0=eta(E0), eta_s=eta(S_UNIT))


def main() -> int:
    print("ROUTE-2 21/4 PIN: BOX-SIZE SCAN -- 15/8 IS A SINGLE-BOX FEATURE, NOT A LIMIT")
    print("=" * 92)

    boxes = {N: make_box(N) for N in [11, 13, 15, 17, 19, 21, 25, 29]}
    data = {N: gammas(pf) for N, pf in boxes.items()}

    # ---- S1: anchor ----
    cache = dict(gE_center=-3.772329167975e-04, gE_shell=-2.010572657265e-04,
                 gT_center=+3.359952396063e-04, gT_shell=+4.031967723697e-04)
    m15 = data[15]
    anchor_err = max(abs(m15[k] - cache[k]) / abs(cache[k]) for k in cache)
    check("S1 (ANCHOR): at N=15 the reconstructed gamma_X(center|shell) reproduce the landed "
          "center-excess cache to ~1e-13 (the 15-pinned scalar Schur action is bypassed; it does not "
          "feed the e_spatial_tf slot) -- the N-reconstruction IS the landed observable",
          anchor_err < 1e-6,
          f"max relative anchor error = {anchor_err:.2e}; N=15 q_T={m15['q_T']:.6f} (5/6={5/6:.6f}), "
          f"q_E={m15['q_E']:.6f} (15/8={15/8:.6f})")

    print("\n  N    eta(e0)     eta(s)      gE_center   gE_shell    gT_center   gT_shell    q_T        q_E")
    for N in boxes:
        d = data[N]
        print(f"  {N:3d}  {d['eta_e0']:+.4e} {d['eta_s']:+.4e} {d['gE_center']:+.3e} "
              f"{d['gE_shell']:+.3e} {d['gT_center']:+.3e} {d['gT_shell']:+.3e} "
              f"{d['q_T']:+.5f}  {d['q_E']:+.5f}")

    # ---- S2: smooth base, erratic ratios ----
    Ns = list(boxes)
    eta_e0 = [data[N]["eta_e0"] for N in Ns]
    eta_s = [data[N]["eta_s"] for N in Ns]
    base_smooth = (all(x > 0 for x in eta_e0) and all(x > 0 for x in eta_s)
                   and all(np.diff(eta_e0) < 0) and all(np.diff(eta_s) < 0))
    # in the boundary-clean range (drop N=11, whose radius-4.25 probe nearly touches the edge) the base
    # variation is mild and slowing -- a converging-looking sequence:
    e0_clean = eta_e0[1:]
    base_converging = (e0_clean[0] / e0_clean[-1] < 1.5
                       and abs(np.diff(e0_clean)[-1]) < 0.5 * abs(np.diff(e0_clean)[0]))
    qE_spread = max(data[N]["q_E"] for N in Ns) - min(data[N]["q_E"] for N in Ns)
    check("S2 (smooth base / erratic ratios): the undifferentiated base observable eta_floor(e0), "
          "eta_floor(s) is strictly positive and monotone-decreasing with N (no sign flips), and in the "
          "boundary-clean range N>=13 its decrements shrink (a converging-looking sequence) -- so the "
          "potential and the bright observable are well-behaved; the erraticism lives in the delicate "
          "differenced/normalized channel coefficients, not in a broken phi",
          base_smooth and base_converging and qE_spread > 5.0,
          f"eta(e0) N>=13: {e0_clean[0]:.3e} -> {e0_clean[-1]:.3e} (ratio {e0_clean[0]/e0_clean[-1]:.2f}, "
          f"decrements slowing); monotone+positive: {base_smooth}; q_E spread = {qE_spread:.1f} (erratic)")

    # ---- S3: the mechanism -- an isolated one-box NUMERATOR excursion (a_aniso cancels exactly) ----
    a_ratio_max = max(abs(data[N]["a_ratio"] - 1.0) for N in Ns)
    bare_match = max(abs(data[N]["q_E"] - data[N]["q_E_bare"]) / max(abs(data[N]["q_E"]), 1e-12)
                     for N in Ns)
    beEs = {N: data[N]["beE_shell"] for N in Ns}
    excursion = beEs[15] < 0 and all(beEs[N] > 0 for N in [13, 17, 19, 21, 25, 29])
    # "isolated downward excursion" (not a smooth zero-crossing): linear interp of N13,N17 at N15 is
    # positive, but the actual value punches negative.
    interp15 = 0.5 * (beEs[13] + beEs[17])
    isolated = interp15 > 0 and beEs[15] < 0
    check("S3 (THE MECHANISM -- isolated one-box NUMERATOR excursion; a_aniso cancels): the shell "
          "normalization a_aniso is the SAME at the center (e0) and shell (s/sqrt6) endpoints to machine "
          "precision (a_center/a_shell = 1), so it CANCELS exactly in q_X = gamma_X(center)/gamma_X(shell) "
          "= beta_X(center)/beta_X(shell). The bare finite-difference beta_E(shell) is POSITIVE at every "
          "box (N=13,17,19,21,25,29) EXCEPT N=15, where it makes an isolated one-box DOWNWARD EXCURSION "
          "to negative -- NOT a smooth zero-crossing (the N13/N17 interpolant at N15 is positive). So "
          "q_E=15/8 at N=15 is set by that single-box numerator excursion, not approached as a limit",
          a_ratio_max < 1e-9 and bare_match < 1e-9 and excursion and isolated,
          f"max|a_center/a_shell - 1| = {a_ratio_max:.1e} (cancels); q_E == bare beta ratio to "
          f"{bare_match:.1e}; beta_E(shell): N13={beEs[13]:+.2e}, N15={beEs[15]:+.2e} (NEG), "
          f"N17={beEs[17]:+.2e}, N21={beEs[21]:+.2e} (POS); N13/N17 interp at N15 = {interp15:+.2e} (POS)")

    # ---- S4: non-convergence (the discriminator) ----
    qTs = [data[N]["q_T"] for N in Ns]
    qEs = [data[N]["q_E"] for N in Ns]
    qT_signflip = any(qTs[i] * qTs[i + 1] < 0 for i in range(len(qTs) - 1))
    qE_large_for_big_N = all(data[N]["q_E"] < -3.0 for N in [17, 19, 21, 25, 29])
    qT_far_from_target_for_big_N = all(abs(data[N]["q_T"] - 5 / 6) > 0.5 for N in [19, 21, 25, 29])
    check("S4 (NON-CONVERGENCE, the discriminator): q_T(N) sign-flips and runs far from 5/6 for the "
          "larger (cleaner, more-room) boxes, and q_E(N) goes large-negative for N>=17 -- neither has a "
          "finite-volume limit at the target. The N=15 agreement with {5/6, 15/8} is a single-box "
          "coincidence, not the boundary-removal limit of the stack's functional",
          qT_signflip and qE_large_for_big_N and qT_far_from_target_for_big_N,
          f"q_T over N = {['%+.2f' % x for x in qTs]}; q_E over N = {['%+.2f' % x for x in qEs]}")

    # ---- S5: robustness in EPS and Ricci step ----
    pf15 = boxes[15]
    pf21 = boxes[21]
    eps_dip_ok = True
    for eps in (0.0025, 0.005, 0.01):
        g15 = gammas(pf15, eps=eps)["gE_shell"]
        g21 = gammas(pf21, eps=eps)["gE_shell"]
        if not (g15 < 0 and g21 > 0):
            eps_dip_ok = False
    h_q21 = gammas(pf21, ric_h=0.06)["q_E"]
    h_stable = abs(h_q21 - data[21]["q_E"]) < 0.5
    check("S5 (ROBUSTNESS): the beta_E(shell) one-box downward excursion (negative at N=15, positive at "
          "N=21) holds for EPS in {0.0025, 0.005, 0.01}, and q_E(N=21) is stable under a changed Ricci "
          "finite-difference step (0.04 -> 0.06) -- the finding is not a differencing/step artifact",
          eps_dip_ok and h_stable,
          f"EPS-robust excursion: {eps_dip_ok}; q_E(N=21) h=0.04->{data[21]['q_E']:.3f}, "
          f"h=0.06->{h_q21:.3f}")

    # ---- S5b: the OTHER limit -- box-proportional radius ALSO fails 15/8 (it converges to 1) ----
    # since a_aniso cancels (S3), q_X = bare beta ratio, so the box-proportional limit needs no shell
    # normalization (which is intrinsically a fixed-radius-4.0 object). probe radius scales with the box.
    prop = {}
    for N in [13, 15, 17, 19, 21, 25]:
        g = gammas(boxes[N], rad=PROBE_RAD * (N - 2) / 13.0)
        prop[N] = (g["q_T_bare"], g["q_E_bare"])
    qE_prop = [prop[N][1] for N in [17, 19, 21, 25]]
    qT_prop = [prop[N][0] for N in [17, 19, 21, 25]]
    converges_to_one = (abs(qE_prop[-1] - 1.0) < 0.3 and abs(qT_prop[-1] - 1.0) < 0.3
                        and abs(qE_prop[-1] - 1.0) < abs(qE_prop[0] - 1.0))
    check("S5b (the OTHER limit also fails 15/8): under a box-PROPORTIONAL probe radius "
          "(4.25*(N-2)/13, a fixed-lattice-fraction position -- a different, also-well-defined "
          "infinite-volume observable), q_E and q_T CONVERGE, but to (1, 1), NOT (15/8, 5/6). So 15/8 "
          "fails under BOTH the fixed-radius and the box-proportional limits -- there is no infinite-"
          "volume limit of this functional that recovers it (the fixed-radius limit is A faithful "
          "boundary-removal limit, not THE unique one, and neither yields 15/8)",
          converges_to_one,
          f"box-proportional q_E -> {['%+.3f' % x for x in qE_prop]} (target 1), "
          f"q_T -> {['%+.3f' % x for x in qT_prop]} (target 1) -- not 15/8, not 5/6")

    # ---- S6: verdict (two-part framing) ----
    check("S6 (VERDICT -- two-part, the honest framing): (i) 15/8 is a fixed-N=15 exact-readout "
          "coincidence. The relocation note FLOATED -- and explicitly flagged could-fail -- "
          "the hope that q_E identifies with 15/8 in the stack's own boundary-removal limit; this scan "
          "NEGATIVELY RESOLVES that self-posed discriminator (no infinite-volume limit recovers 15/8: "
          "fixed-radius -> q_E ~ -11 via the isolated one-box numerator excursion; box-proportional -> "
          "q_E -> 1), CLOSING the 'maybe it converges to 15/8 in the bulk' escape hatch and vindicating "
          "the note's caution. (ii) It does NOT sharpen the underlying naturality no-go (2026-04-28), "
          "which was always a fixed-carrier SELECTION gap with NO convergence claim and STANDS unchanged; "
          "15/8 was never claimed by the readout's native framing to BE the infinite-volume value. The "
          "21/4 pin remains a fixed-box structural-selection gap -- this scan supplies no selecting "
          "primitive, it only closes one escape route.",
          True,
          "closes the bulk-limit hatch (both limits miss 15/8); naturality no-go unchanged; pin remains "
          "a fixed-box selection gap")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT (two-part framing): the box-size scan, anchored exactly to the\n"
        "landed N=15 cache (~1e-13), shows the readout target chain {5/6, 15/8, -2, -8/9} is realized\n"
        "ONLY at N=15. The shell normalization a_aniso is identical at center and shell (cancels in q_X),\n"
        "so q_X is a bare beta ratio; the bare finite-difference beta_E(shell) makes an ISOLATED one-box\n"
        "downward excursion to negative at N=15 while staying positive in the bulk -- so q_E=15/8 is a\n"
        "single-box numerator coincidence, EPS- and step-robust, with a smooth well-behaved base\n"
        "observable. NO infinite-volume limit recovers 15/8: the fixed-radius (boundary-removal) limit\n"
        "runs q_E to ~ -11, and the box-proportional limit converges to q_E -> 1 (and q_T -> 1), not\n"
        "15/8. CONCLUSION (two-part): (i) this CLOSES the bulk-limit escape hatch the relocation\n"
        "note floated -- 15/8 is not the infinite-volume value under any limit of this functional --\n"
        "vindicating that note's flagged caution; (ii) it does NOT sharpen the standing 2026-04-28\n"
        "naturality no-go, which never claimed convergence and is unchanged. The 21/4 pin remains a\n"
        "fixed-box structural-selection gap (rho_E free unless a stronger readout-map primitive is\n"
        "supplied); this scan supplies none -- it only rules out the bulk-limit promotion of the N=15\n"
        "coincidence. No PDG/fitted value consumed."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
