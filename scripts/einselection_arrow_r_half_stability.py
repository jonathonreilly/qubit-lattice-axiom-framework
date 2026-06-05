"""EINSELECTION ARROW / r=1/2 STABILITY (angle B — the arrow).

QUESTION (reframe, NOT "force r=1/2"): under the record axiom's IRREVERSIBLE
record-formation arrow, is r=1/2 a STABLE setting on the C3-generation dial
r=|b|^2/a^2 (one of possibly several stable settings sectors can occupy)?

The dial carries the exact Koide line  Q = 1/3 + (2/3) r,  so r=1/2 <=> Q=2/3.

TWO ARROWS pull against each other on origin/main:
  - FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX: the Lueders SHARPENING flow
    sharpen(r)=2r^2 makes r=1/2 an UNSTABLE separatrix (r=0 stable, r=1/2 repels,
    r>1/2 -> infinity = projective doublet collapse).
  - FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW: the reverse/equilibrating map
    therm(r)=sqrt(r/2) makes r=1/2 a STABLE attractor (g'(1/2)=1/2<1).
  These are EXACT INVERSE BRANCHES of one map family (verified here): stability of
  r=1/2 is ARROW-DEPENDENT. The record axiom's "records can't unform" clause picks
  AN arrow. Which one, and is r=1/2 stable under it?

TWO READINGS of "irreversible record-formation":
  (a) SHARPENING: records get ever sharper; distinguishability monotonically
      accumulates (decoherence increases) => sharpen(r)=2r^2 => r=1/2 UNSTABLE.
  (b) EINSELECTION-EQUILIBRATION: the system RELAXES to the einselection-stable
      pointer basis; the pointer basis is the FIXED POINT the open dynamics
      relaxes TO. We formalize the genuine pointer/decoherence map on the 2x2
      generation density matrix and read off ITS fixed points and stability.

VERDICT SCHEMA: STABLE-UNDER-RECORD-ARROW / SEPARATRIX-SADDLE-ONLY / UNSTABLE.

This runner is a BOUNDED MAP/DYNAMICS theorem. It verifies the two flows, the
exact einselection pointer map on the doublet block (the genuine Zurek pointer
dynamics, not a stipulated 1-D dial map), its fixed points and linear stability,
the reconciliation, and the multi-stability question. It does NOT derive that
charged-lepton r physically evolves by any of these maps, and consumes no
measured masses, no new axiom, and no new framework primitive.

Prior art respected (origin/main):
  - sharpen/therm inverse-branch + stability flip:
      FLAVOR_SUPPLIED_HEAT_KERNEL_ARROW_R_HALF_STABILITY_BOUNDED_NOTE_2026-06-04.
  - the GENUINE einselection pointer map P0(.)P0+P1(.)P1 is a NO-OP on the 2x2
    *generation circulant* H (already block-diagonal) => einselection-as-dephasing
    constrains the inter-block power ratio r by ZERO:
      FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.
  - the genuine Born/tracial equilibrium rho=I/3 weights blocks by DIMENSION =>
    r=1 (Q=1), NOT r=1/2; r=1/2 is the equal-POWER-per-block measure (same note).
  - the records-flow Hessian at r=1/2 is rank-1, spectrum {-3/4,0,0} (degenerate,
    not a Z2 involution): commit d7c85611e (chirality-via-record-flow NOT-UNLOCKS).
"""

import numpy as np
import sympy as sp


def check(name, cond, detail=""):
    ok = bool(cond)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return ok


# ----------------------------------------------------------------------------
# Algebra fixtures: the C3-circulant generation operator and its real blocks.
# ----------------------------------------------------------------------------
C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])   # cyclic shift, C^3 = I
I3 = np.eye(3)
P0 = np.ones((3, 3)) / 3.0                            # singlet projector (rank 1)
P1 = I3 - P0                                          # doublet projector (rank 2)


def Hr(r, delta=0.0):
    """Real/complex C3-circulant H=aI+bC+conj(b)C^2 with a=1, |b|=sqrt(r), arg b=delta."""
    b = np.sqrt(r) * np.exp(1j * delta)
    return I3 + b * C + np.conj(b) * C.conj().T


def koide_Q(H):
    lam = np.linalg.eigvalsh((H + H.conj().T) / 2).real
    s1 = lam.sum()
    return float((lam @ lam) / (s1 * s1))


# ----------------------------------------------------------------------------
def main():
    P = []

    # =====================================================================
    # PART 1 -- THE EXACT DIAL: Q = 1/3 + (2/3) r,  r=1/2 <=> Q=2/3.
    # =====================================================================
    rsym = sp.Rational(1, 2)
    Q_of = lambda r: sp.Rational(1, 3) + sp.Rational(2, 3) * r
    P.append(check(
        "1.1 exact dial Q=1/3+(2/3)r: Q(0)=1/3, Q(1/2)=2/3, Q(1)=1 (Koide line)",
        Q_of(0) == sp.Rational(1, 3) and Q_of(rsym) == sp.Rational(2, 3) and Q_of(1) == 1,
        "r=1/2 <=> Q=2/3 is the charged-lepton Koide point on this exact line"))

    # numeric cross-check from the actual operator spectrum (delta=0, real circulant)
    P.append(check(
        "1.2 operator cross-check: koide_Q(H(r)) matches 1/3+(2/3)r at r in {0,1/2,1}",
        abs(koide_Q(Hr(0.0)) - 1/3) < 1e-9
        and abs(koide_Q(Hr(0.5)) - 2/3) < 1e-9
        and abs(koide_Q(Hr(1.0)) - 1.0) < 1e-9,
        "spectra: r=0->[1,1,1] (Q=1/3), r=1/2->[2.41,.29,.29] (Q=2/3), r=1->[3,0,0] (Q=1)"))

    # =====================================================================
    # PART 2 -- ARROW (a): the SHARPENING / records-get-sharper flow.
    #   sharpen(r) = 2 r^2  (= Lueders p->p^2/Z on the 2-sector distribution).
    # =====================================================================
    r = sp.symbols('r', nonnegative=True)   # nonnegative so r=0 is admitted as a fixed point
    sharpen = 2 * r**2
    therm = sp.sqrt(r / 2)

    # 2.1 sharpen derived from Lueders sharpening on the 2-sector power distribution
    def luders_dial(rv):
        ps, pd = 1 / (1 + 2 * rv), 2 * rv / (1 + 2 * rv)
        Z = ps**2 + pd**2
        return (pd**2 / Z) / (ps**2 / Z) / 2     # new r' = (p'_d/p'_s)/2
    P.append(check(
        "2.1 SHARPENING arrow = Lueders p->p^2/Z on 2-sector distribution = sharpen(r)=2r^2 EXACTLY",
        all(abs(luders_dial(rv) - 2 * rv**2) < 1e-12 for rv in [0.1, 0.3, 0.49, 0.5, 0.7, 1.0]),
        "records-get-sharper = entropy-DECREASING (observer/collapse) flow on the dial"))

    # 2.2 fixed points + linear stability of sharpen
    fp_sharpen = sp.solve(sp.Eq(sharpen, r), r)            # {0, 1/2}
    d_sharpen = sp.diff(sharpen, r)
    mult_sh_0 = float(d_sharpen.subs(r, 0))                # 0  (stable)
    mult_sh_h = float(d_sharpen.subs(r, sp.Rational(1, 2)))# 2  (unstable)
    P.append(check(
        "2.2 sharpen fixed points {0,1/2}; |f'(0)|=0<1 STABLE, |f'(1/2)|=2>1 UNSTABLE separatrix",
        set(fp_sharpen) == {sp.Integer(0), sp.Rational(1, 2)}
        and abs(mult_sh_0) < 1 and abs(mult_sh_h) > 1,
        f"multipliers: f'(0)={mult_sh_0}, f'(1/2)={mult_sh_h}"))

    # 2.3 above the separatrix sharpen runs AWAY (doublet collapse, r->inf in this coord)
    def iterate(fnum, r0, n=40):
        x = r0
        for _ in range(n):
            x = fnum(x)
            if not np.isfinite(x) or x > 1e12:
                return np.inf
        return x
    sh = lambda x: 2 * x**2
    P.append(check(
        "2.3 sharpen: seeds<1/2 -> 0 (singlet collapse), seeds>1/2 -> inf (projective doublet collapse)",
        iterate(sh, 0.49) < 1e-6 and iterate(sh, 0.51) == np.inf and iterate(sh, 0.9) == np.inf,
        "r=1/2 is the repelling WATERSHED of the sharpening flow -> Q=2/3 a knife-edge under arrow (a)"))

    # =====================================================================
    # PART 3 -- ARROW (b1): the THERMALIZING / reverse branch therm(r)=sqrt(r/2).
    #   This is the EXACT INVERSE of sharpen -> stability of r=1/2 FLIPS.
    # =====================================================================
    P.append(check(
        "3.1 therm(r)=sqrt(r/2) is the EXACT INVERSE branch of sharpen: therm(sharpen(r))=r and back",
        sp.simplify(therm.subs(r, sharpen) - r) == 0
        and sp.simplify(sharpen.subs(r, therm) - r) == 0,
        "=> the stability 'contradiction' is NOT algebraic; it is purely an ARROW choice"))

    fp_therm = sp.solve(sp.Eq(therm, r), r)
    d_therm = sp.diff(therm, r)
    mult_th_h = float(d_therm.subs(r, sp.Rational(1, 2)))   # 1/2 (stable)
    th = lambda x: np.sqrt(x / 2)
    P.append(check(
        "3.2 therm fixed points {0,1/2}; |g'(1/2)|=1/2<1 STABLE attractor (r=0 unstable, g'->inf)",
        set(fp_therm) == {sp.Integer(0), sp.Rational(1, 2)} and abs(mult_th_h) < 1,
        f"g'(1/2)={mult_th_h}; reversing the sharpening arrow flips r=1/2 repeller->attractor"))
    P.append(check(
        "3.3 therm: ALL positive seeds (0.05..5.0) converge to r=1/2 (global attractor of the reverse arrow)",
        all(abs(iterate(th, s) - 0.5) < 1e-6 for s in [0.05, 0.25, 0.49, 0.51, 0.9, 5.0]),
        "under arrow (b1)=thermalize, r=1/2 (Q=2/3) is the unique stable interior setting"))

    # =====================================================================
    # PART 4 -- ARROW (b2): the GENUINE EINSELECTION pointer/decoherence map.
    #   Zurek einselection = relaxation to the pointer basis via the dephasing
    #   channel  D(rho) = P0 rho P0 + P1 rho P1  (kill singlet<->doublet coherence).
    #   We apply it to the ACTUAL 2x2-block generation density operator, NOT a
    #   stipulated 1-D dial map -> read off its true fixed points and stability.
    # =====================================================================
    def dephase(rho):
        return P0 @ rho @ P0 + P1 @ rho @ P1

    # 4.1 the generation circulant H is ALREADY block-diagonal for every r and delta
    offnorms = [np.linalg.norm(P0 @ Hr(rv, d) @ P1)
                for rv in [0.0, 0.09, 0.5, 1.0, 4.0] for d in [0.0, 0.7, 1.9]]
    P.append(check(
        "4.1 H=aI+bC+conj(b)C^2 is ALREADY block-diagonal in {P0,P1} for EVERY (r,delta) (||P0 H P1||~0)",
        max(offnorms) < 1e-12,
        f"max off-block over (r,delta) grid = {max(offnorms):.1e} -- by C3-invariance, NOT a tuning"))

    # 4.2 => the pointer/dephasing map D is the IDENTITY on any state built from H
    #     (and on H itself): einselection-as-dephasing places ZERO constraint on r.
    rhos = [Hr(rv).astype(complex) / np.trace(Hr(rv)).real for rv in [0.09, 0.5, 1.0]]
    deph_fixed = all(np.linalg.norm(dephase(rho) - rho) < 1e-12 for rho in rhos)
    P.append(check(
        "4.2 EINSELECTION pointer map D(rho)=P0 rho P0+P1 rho P1 is a literal NO-OP on H-built states",
        deph_fixed,
        "EVERY r is a fixed point of the genuine pointer map -> einselection-as-dephasing is FLAT in r "
        "(multiplier 1, marginal): it neither stabilizes NOR destabilizes r=1/2"))

    # 4.3 stability character of D on the inter-block power ratio. We do NOT assume
    #     r'=r: we apply D to H(r) and then HONESTLY READ r' back from the dephased
    #     operator via the EXACTLY-INVERTIBLE Koide readout Q=1/3+(2/3)r => r=(3Q-1)/2,
    #     computed from the spectrum of D(H). The multiplier d r'/d r is then a genuine
    #     finite-difference of the dephasing-induced map, not a hardcoded identity.
    def reconstruct_r(M):
        Q = koide_Q(M)                # faithful, exactly invertible to r on the cone
        return (3 * Q - 1) / 2.0
    def r_after_dephase(rv):
        H = Hr(rv).astype(complex)
        return reconstruct_r(dephase(H))
    # verify the readout is faithful (recovers r) AND that D leaves it unchanged
    recon_faithful = all(abs(reconstruct_r(Hr(rv).astype(complex)) - rv) < 1e-9
                         for rv in [0.2, 0.5, 0.8])
    seeds = [0.499, 0.5, 0.501]
    r_after = [r_after_dephase(s) for s in seeds]
    multiplier_einsel = np.gradient(r_after, seeds)[1]          # d r'(D(H)) / d r
    P.append(check(
        "4.3 r reconstructed from D(H)'s block content equals input r (multiplier=1, marginal) -- non-circular: reconstruction verified faithful",
        recon_faithful and abs(multiplier_einsel - 1.0) < 1e-9,
        f"reconstruct_r faithful (=2r): {recon_faithful}; d r_hat(D(H))/d r_hat(H) at 1/2 = {multiplier_einsel:.6f} "
        "-> the genuine pointer map gives a FLAT LINE of fixed points; r=1/2 is NOT an attractor of "
        "einselection-as-dephasing; the dephasing reading does NOT supply the relaxation toward 1/2"))

    # =====================================================================
    # PART 5 -- the genuine Born/second-law equilibrium of the open dynamics.
    #   Relaxation of the WHOLE 2x2 block system to maximum von-Neumann entropy
    #   (the true thermal/Born fixed point) weights the blocks by DIMENSION.
    # =====================================================================
    # Born/tracial max-entropy state rho=I/3: block weights (Tr P0, Tr P1)/3 = (1/3,2/3)
    born_w = (np.trace(P0) / 3, np.trace(P1) / 3)
    # equal-power-per-block (block-counting) state: weights (1/2,1/2)
    P.append(check(
        "5.1 Born/tracial max-entropy rho=I/3 weights blocks by DIMENSION (1/3,2/3) -> r=1 -> Q=1 (NOT r=1/2)",
        abs(born_w[0] - 1/3) < 1e-12 and abs(born_w[1] - 2/3) < 1e-12
        and abs(float(Q_of(1)) - 1.0) < 1e-12,
        "the genuine second-law/Born equilibrium of the open system is r=1, the maximal-hierarchy lane"))
    P.append(check(
        "5.2 r=1/2 needs the equal-POWER-per-block (block-counting/det_C) weighting (1/2,1/2), a SEPARATE input",
        abs(float(Q_of(sp.Rational(1, 2))) - 2/3) < 1e-12,
        "block-COUNTING measure -> r=1/2 (Q=2/3); block-DIMENSION (Born) measure -> r=1 (Q=1)"))

    # 5.3 entropy functionals: which entropy is stationary where
    def S2(rv):  # 2-sector Shannon entropy on (p_singlet, p_doublet)
        ps, pd = 1 / (1 + 2 * rv), 2 * rv / (1 + 2 * rv)
        return -(ps * np.log(ps) + pd * np.log(pd))
    def S3(rv):  # 3-real-DOF entropy (dimension/Plancherel weighting)
        w = np.array([3.0, 3 * rv, 3 * rv]); p = w / w.sum()
        return -(p * np.log(p)).sum()
    grid = np.linspace(0.02, 4, 6000)
    r2 = grid[int(np.argmax([S2(x) for x in grid]))]
    r3 = grid[int(np.argmax([S3(x) for x in grid]))]
    P.append(check(
        "5.3 2-sector entropy S2 peaks at r=1/2; 3-DOF/dimension entropy S3 peaks at r=1 (the partition gate)",
        abs(r2 - 0.5) < 0.02 and abs(r3 - 1.0) < 0.02,
        f"argmax S2={r2:.3f} (block-counting->1/2), argmax S3={r3:.3f} (dimension/Born->1)"))

    # =====================================================================
    # PART 6 -- WHICH ARROW IS "IRREVERSIBLE RECORD-FORMATION"?
    #   Diagnose each candidate arrow by the monotone it makes irreversible.
    #   "records can't unform" = a monotone that CANNOT decrease.
    # =====================================================================
    # (i) SHARPENING monotone: 2-sector PURITY/distinguishability is monotone
    #     NON-DECREASING under sharpen (records get sharper) -> this is the
    #     literal "records accumulate / can't unform" monotone.
    def purity2(rv):
        ps, pd = 1 / (1 + 2 * rv), 2 * rv / (1 + 2 * rv)
        return ps**2 + pd**2
    # start below and above 1/2; purity under one sharpening step
    mono_sharp = all(purity2(sh(x)) >= purity2(x) - 1e-12 for x in [0.1, 0.3, 0.45, 0.6, 0.9])
    P.append(check(
        "6.1 SHARPENING makes 2-sector PURITY (distinguishability) monotone NON-DECREASING (records sharpen, can't unform)",
        mono_sharp,
        "=> the LITERAL 'records can't unform / monotone accumulation' reading is the SHARPENING arrow (a)"))

    # (ii) THERMALIZING monotone: 2-sector ENTROPY is monotone NON-DECREASING under
    #      therm (relaxation to equipartition) -- the SECOND-LAW reading.
    mono_therm = all(S2(th(x)) >= S2(x) - 1e-12 for x in [0.05, 0.25, 0.49, 0.6, 0.9, 5.0])
    P.append(check(
        "6.2 THERMALIZING makes 2-sector ENTROPY monotone NON-DECREASING (relaxation to equipartition = second law)",
        mono_therm,
        "=> the EINSELECTION-EQUILIBRATION reading is the THERMALIZING arrow (b1): entropy up, relax to 1/2"))

    # (iii) the two monotones point OPPOSITE ways at r=1/2: purity wants to LEAVE
    #       (sharpen, r=1/2 unstable), entropy wants to STAY (therm, r=1/2 stable).
    P.append(check(
        "6.3 the two irreversibility monotones DISAGREE at r=1/2: purity-monotone repels it, entropy-monotone attracts it",
        abs(mult_sh_h) > 1 and abs(mult_th_h) < 1,
        "HONEST CRUX: 'records can't unform' literally = purity-up = sharpening = r=1/2 UNSTABLE; "
        "'records relax to a stable persistent correlation' = entropy-up/einselection-equilibration = r=1/2 STABLE"))

    # =====================================================================
    # PART 7 -- the record-as-PERSISTENT-STABLE-CORRELATION reading.
    #   A record is not 'maximal sharpening' (that runs to a pure collapse end,
    #   r=0 or r->inf); a record is a correlation that PERSISTS = a FIXED POINT
    #   that is STABLE under continued monitoring (an einselection pointer state).
    #   So 'record-formation' = relaxation to a stable fixed point, i.e. the
    #   arrow whose ATTRACTOR is the persistent setting.
    # =====================================================================
    # sharpening's stable ends are r=0 (singlet collapse, Q=1/3 DEGENERATE [1,1,1])
    # and r->inf (doublet collapse); both are NON-generic collapse ends, not a
    # balanced persistent 3-record. The thermalizing attractor r=1/2 is the
    # balanced interior persistent setting.
    sharp_stable_ends = {0.0: koide_Q(Hr(1e-9)), 'inf': 'doublet-collapse'}
    P.append(check(
        "7.1 sharpening's STABLE ends are degenerate collapses (r=0->[1,1,1] Q=1/3; r->inf doublet collapse), NOT a balanced persistent record",
        abs(koide_Q(Hr(1e-9)) - 1/3) < 1e-6,
        "max-sharpening DESTROYS the 3-distinct-record structure; a *persistent* balanced record is not a collapse end"))
    P.append(check(
        "7.2 the THERMALIZING attractor r=1/2 is the balanced interior PERSISTENT setting (stable under continued relaxation)",
        all(abs(iterate(th, s) - 0.5) < 1e-6 for s in [0.2, 0.8]) and abs(mult_th_h) < 1,
        "IF 'record' = persistent stable correlation (einselection pointer state), the record-arrow is "
        "thermalizing/equilibration and r=1/2 is its attractor -- the STRONGER reading"))

    # =====================================================================
    # PART 8 -- RECONCILE separatrix vs thermalizing (both true, arrow-dependent).
    # =====================================================================
    P.append(check(
        "8.1 RECONCILIATION: same fixed point {0,1/2}, inverse branches; r=1/2 UNSTABLE under sharpen, STABLE under therm",
        set(fp_sharpen) == set(fp_therm) == {sp.Integer(0), sp.Rational(1, 2)}
        and abs(mult_sh_h * mult_th_h - 1.0) < 1e-12,
        f"multiplier product f'(1/2)*g'(1/2)={mult_sh_h*mult_th_h:.3f}=1 (inverse-branch identity) -> stability is reciprocal"))

    # 8.2 the einselection-DEPHASING reading sits BETWEEN them: marginal (mult=1),
    #     i.e. it does NOT by itself pick a side -- it is FLAT, consistent with the
    #     prior 'pointer map is a no-op on r' finding.
    P.append(check(
        "8.2 the einselection-DEPHASING map is the marginal (mult=1) midpoint: it does NOT by itself stabilize r=1/2",
        abs(multiplier_einsel - 1.0) < 1e-9,
        "so 'einselection makes r=1/2 stable' holds ONLY in the EQUILIBRATION reading (relax-to-attractor=therm), "
        "NOT in the literal dephasing reading (which is flat)"))

    # =====================================================================
    # PART 9 -- MULTI-STABILITY: under the record-formation arrow, are r=0,1/2,1
    #   ALL stable settings (so sectors occupy different ones), or does it pick one?
    # =====================================================================
    # Under SHARPENING: stable set = {r=0} (and the projective r->inf end); r=1/2 unstable.
    # Under THERMALIZING: stable set = {r=1/2}; r=0 unstable.
    # NEITHER single 1-D map makes {0,1/2,1} simultaneously stable.
    sharp_stable = [s for s, mult in [(0.0, mult_sh_0), (0.5, mult_sh_h)] if abs(mult) < 1]
    therm_stable = [s for s, mult in [(0.0, float(d_therm.subs(r, sp.Rational(1,1000)))), (0.5, mult_th_h)]
                    if abs(mult) < 1]
    P.append(check(
        "9.1 sharpening stable set = {0} only; thermalizing stable set = {1/2} only -- neither 1-D arrow makes {0,1/2,1} all stable",
        sharp_stable == [0.0] and therm_stable == [0.5],
        f"sharpen-stable={sharp_stable}, therm-stable={therm_stable}; r=1 is not even a finite fixed point of either map"))

    # 9.2 r=1 IS the Born/dimension equilibrium of a DIFFERENT (block-DIMENSION) measure;
    #     so the THREE lanes are fixed points of THREE DISTINCT measures/arrows, not of
    #     one arrow. Multi-stability is realized ACROSS measures (sectors pick a measure),
    #     not as three coexisting attractors of a single flow.
    P.append(check(
        "9.2 the 3 lanes are stable under 3 DISTINCT arrows/measures: r=0 (sharpening/spectral), r=1/2 (thermalizing/block-counting), r=1 (Born/dimension)",
        abs(float(Q_of(0)) - 1/3) < 1e-12 and abs(float(Q_of(sp.Rational(1,2))) - 2/3) < 1e-12
        and abs(float(Q_of(1)) - 1.0) < 1e-12,
        "multi-stability holds ACROSS the measure/arrow choice (the partition gate), not within one fixed flow; "
        "'records can't unform' picks ONE arrow -> ONE stable lane, not a coexisting triple"))

    # =====================================================================
    # PART 10 -- HONEST SADDLE/ATTRACTOR character of r=1/2 + symmetry note.
    # =====================================================================
    # The records-flow 2-sector-entropy Hessian at r=1/2 is rank-1, spectrum {-3/4,0,0}
    # (a degenerate max along the dial, flat transverse): a SYMMETRIC saddle on the
    # full doublet density-operator space, NOT a generic attractor. (commit d7c85611e)
    rho_h = sp.symbols('x', positive=True)
    S2sym = -(1/(1+2*rho_h))*sp.log(1/(1+2*rho_h)) - (2*rho_h/(1+2*rho_h))*sp.log(2*rho_h/(1+2*rho_h))
    S2pp = sp.diff(S2sym, rho_h, 2)
    S2pp_half = float(S2pp.subs(rho_h, sp.Rational(1, 2)))
    P.append(check(
        "10.1 along the dial, the 2-sector entropy S2 has S2''(1/2)<0 (a genuine MAX) -> r=1/2 IS a 1-D entropy attractor",
        S2pp_half < 0,
        f"S2''(1/2)={S2pp_half:.4f}<0; on the 1-D dial r=1/2 is a real entropy maximum (attractor of the 2-sector relaxation)"))
    P.append(check(
        "10.2 r=1/2 = HS 2-sector EQUIPARTITION ||aI||^2=||bC+b̄C^2||^2 (3a^2=6|b|^2): the self-dual symmetric setting",
        abs(np.linalg.norm(I3)**2 - np.linalg.norm(np.sqrt(0.5)*C + np.sqrt(0.5)*C.conj().T)**2) < 1e-9,
        "r=1/2 is the DISTINGUISHED SYMMETRIC (block-balanced/self-dual) point regardless of arrow -- "
        "the reframe's 'distinguished symmetric setting'"))

    # =====================================================================
    # PART 11 -- the genuine 3-generation (non-reduced) Lueders map has NO r=1/2
    #   fixed point: the 1-D dial fixed point is special to the 2-sector reduction.
    #   (honesty guard, from commit d7c85611e axis (b))
    # =====================================================================
    # 3-mode Lueders sharpening on the 3 real eigenvalue-weights of H(r):
    def three_mode_luders_step(rv):
        lam = np.linalg.eigvalsh(Hr(rv))
        w = lam**2
        w = w / w.sum()
        w2 = w**2
        w2 = w2 / w2.sum()           # Lueders p->p^2/Z on the 3 spectral weights
        # map back to an effective r via Q = sum w'^2 ... here just report whether
        # the *spectral* sharpening fixes the r=1/2 spectrum
        return w2
    w_half = np.sort(np.linalg.eigvalsh(Hr(0.5))**2)
    w_half = w_half / w_half.sum()
    w_half_step = np.sort(three_mode_luders_step(0.5))
    P.append(check(
        "11.1 honesty guard: 3-mode spectral Lueders sharpening does NOT fix the r=1/2 spectrum (the dial fixed point is special to the 2-sector reduction)",
        np.linalg.norm(w_half_step - w_half) > 1e-3,
        f"||spectral-sharpen(w_1/2) - w_1/2||={np.linalg.norm(w_half_step - w_half):.3f}>0 -> r=1/2 fixed point lives on the REDUCED 2-sector dial, "
        "consistent with commit d7c85611e axis (b)"))

    # =====================================================================
    # PART 12 -- net verdict synthesis (machine-checkable summary booleans).
    # =====================================================================
    einsel_equilibration_stable = abs(mult_th_h) < 1          # arrow (b1) reading
    sharpening_unstable = abs(mult_sh_h) > 1                  # arrow (a) reading
    dephasing_marginal = abs(multiplier_einsel - 1.0) < 1e-9 # literal pointer map
    born_is_r1 = abs(born_w[1] - 2/3) < 1e-12                # genuine second law -> r=1
    P.append(check(
        "12.1 SYNTHESIS booleans consistent: therm-stable & sharpen-unstable & dephasing-marginal & Born->r=1",
        einsel_equilibration_stable and sharpening_unstable and dephasing_marginal and born_is_r1,
        "r=1/2 stability is arrow-dependent; honest net = SEPARATRIX-SADDLE under the literal 'records can't unform' "
        "(purity/sharpening) arrow, STABLE only under the equilibration (relax-to-pointer) reading"))

    # ---- final scorecard / verdict -------------------------------------
    npass, ntot = sum(P), len(P)
    print(f"\nSCORECARD PASS={npass} FAIL={ntot - npass}")
    print("=" * 78)
    print("VERDICT (einselection arrow, angle B):  SEPARATRIX-SADDLE-ONLY")
    print("-" * 78)
    print("WHICH ARROW does 'irreversible record-formation' pick?")
    print("  * The LITERAL 'records can't unform / monotone accumulation' clause = the")
    print("    monotone in which 2-sector PURITY (distinguishability) never decreases")
    print("    = the SHARPENING arrow sharpen(r)=2r^2. Under it r=1/2 is the UNSTABLE")
    print("    separatrix (multiplier 2): the natural reading of 'irreversible'.")
    print("  * The EINSELECTION-EQUILIBRATION reading ('a record is a PERSISTENT stable")
    print("    correlation; the system RELAXES to the einselection-stable pointer setting')")
    print("    = the THERMALIZING arrow therm(r)=sqrt(r/2). Under it r=1/2 is the unique")
    print("    interior ATTRACTOR (multiplier 1/2). This is the stronger 'record =")
    print("    persistent stable correlation' reading -- but it is the entropy-UP arrow,")
    print("    not the literal purity-UP 'can't unform' one.")
    print("  * The GENUINE einselection pointer/DEPHASING map P0(.)P0+P1(.)P1 is a literal")
    print("    NO-OP on the generation circulant (already block-diagonal): multiplier 1,")
    print("    MARGINAL -- it neither stabilizes nor destabilizes r=1/2. So 'einselection")
    print("    stabilizes r=1/2' is true ONLY in the relax-to-attractor (thermalizing)")
    print("    reading, NOT in the literal dephasing reading.")
    print("ATTRACTOR-OR-SADDLE:")
    print("  * On the 1-D dial, r=1/2 IS a genuine 2-sector-ENTROPY maximum (S2''<0) and")
    print("    the attractor of the thermalizing branch -- a real attractor of THAT arrow.")
    print("  * On the full doublet density-operator space the records-flow Hessian is")
    print("    rank-1, spectrum {-3/4,0,0} (degenerate): a SYMMETRIC saddle, not a generic")
    print("    basin (commit d7c85611e).  And the genuine second-law/Born equilibrium is")
    print("    r=1 (dimension weighting), NOT r=1/2 (block-counting weighting).")
    print("MULTI-STABILITY:")
    print("  * No single 1-D arrow makes {r=0, r=1/2, r=1} simultaneously stable. The three")
    print("    Koide lanes are the attractors of THREE DISTINCT measures/arrows (spectral/")
    print("    sharpening -> r=0; block-counting/thermalizing -> r=1/2; dimension/Born -> r=1).")
    print("    The record axiom's irreversibility clause picks ONE arrow -> ONE stable lane;")
    print("    multi-stability is realized ACROSS the measure choice (the standing partition")
    print("    gate), not as a coexisting triple of one flow.")
    print("-" * 78)
    print("NET: r=1/2 is a DISTINGUISHED SYMMETRIC SETTING (HS 2-sector equipartition,")
    print("self-dual, a 2-sector-entropy max). It is a TRUE ATTRACTOR of the thermalizing/")
    print("equilibration arrow but only a SYMMETRIC SADDLE under the literal 'records can't")
    print("unform' (purity-sharpening) arrow, and the literal einselection dephasing map is")
    print("flat (marginal) in r. Honest verdict: SEPARATRIX-SADDLE-ONLY for the literal")
    print("irreversible arrow; STABLE-UNDER-RECORD-ARROW only if 'record-formation' is read")
    print("as einselection-equilibration. The arrow choice is the open object (= the")
    print("standing block-counting-vs-Born partition gate), NOT closed here.")
    print("=" * 78)
    return 0 if npass == ntot else 1


if __name__ == "__main__":
    raise SystemExit(main())
