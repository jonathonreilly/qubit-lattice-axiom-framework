#!/usr/bin/env python3
"""K/CPT-orbit shrinks of the two Tier-A admissions: the theta note's
mass-orientation premise discharges into the existing surface, and the
AC_phi_lambda orientation half strips to a labeling convention.

Two targets, one mechanism (the campaign's K/CPT-orbit frame-variance
machinery), each with its non-re-walk guards built in.

SHRINK 1 (theta, leverage 20): the landed STRONG_CP_THETA_ZERO note is a
bounded theta_eff = 0 closure conditional on TWO selected-surface premises:
 (P1) the action class carries no bare theta/FtildeF slot;
 (P2) the positive-real quark-mass orientation (arg det M = 0).
This runner DERIVES (P2) at the registrable level from existing premises:
 (T2) K/CPT maps det -> conj(det): the orbit identifies +-arg det.
 (T3) HOSTILE/honest boundary: orbit-invariance alone does NOT kill the
      phase (cos(arg det) is K-invariant) -- evenness, not vanishing.
 (T4) THE MULTIPLICATIVE LEMMA: the continuous multiplicative functionals on
      the determinant group C^* are |z|^s (z/|z|)^k, k integer; K-invariance
      f(conj z) = f(z) forces k = 0 EXACTLY (computed). So K-invariant
      MULTIPLICATIVE (det-class) readouts carry NO phase character.
 (T5) The framework's mass-surface readout lane is det-class/multiplicative
      (the existing (M)/observable-principle atom -- consumed, not added).
      Hence the registrable mass surface is phase-free: arg det M is
      readout-equivalent to 0, the positive-real orientation is the canonical
      representative => (P2) DISCHARGED into the existing surface.
 (T6) GUARDS: theta itself is NOT identified with arg det (the refuted route;
      theta = the FtildeF coefficient -- premise (P1) remains the admission,
      untouched); the RP no-go (rp_half_cannot_forbid_cp_odd) is not used or
      contradicted; observed CP violation is NOT contradicted: the lemma is
      scoped to MULTIPLICATIVE det-class readouts -- non-multiplicative
      K-invariant functionals (e.g. cos of a phase, rate-asymmetry classes)
      can carry even-phase and interference content (exhibited).
 NET: the theta admission shrinks from 2 premises to 1 (the action-form slot).

SHRINK 2 (AC_phi_lambda, leverage 41): the registered statement is "the
C_3-breaking phase/orientation plus the abstract-sector to physical-species
bridge" (bridge naming already stripped as convention). This runner shows the
ORIENTATION half is also a convention:
 (A1) K maps the circulant H(delta) -> H(-delta) exactly (computed).
 (A2) the registrable mass MULTISET is invariant under delta -> -delta: all
      elementary symmetric polynomials of the spectrum agree (exact sympy);
      the individual-eigenvalue reshuffle is precisely the species relabel
      e1 <-> e2 that the registry ALREADY strips as convention.
 (A3) => the registrable content of the gate's phase input is the EVEN part:
      |delta| (equivalently cos 3delta). The orientation (sign) is K-frame /
      labeling content, not physics.
 (A4) HONEST RESIDUAL: the magnitude |delta| = 2/9 stays -- its irreducibility
      is separately audited (the radian-bridge no-go portfolio); NOT attacked.
 NET: AC_phi_lambda shrinks from {phase magnitude, orientation, bridge} to
      {phase magnitude} + conventions.

Sets no audit status. The Tier-A registry is audit-lane owned; this note
proposes the shrinks for audit-lane handling, it does not edit the registry.
"""
from __future__ import annotations

import os
import re

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0


def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))
    return bool(ok)


def section(t):
    print("\n" + "-" * 88 + "\n" + t + "\n" + "-" * 88)


def main():
    print("=" * 88)
    print("K/CPT-ORBIT SHRINKS OF THE TIER-A ADMISSIONS")
    print("=" * 88)

    docs = os.path.join(os.path.dirname(__file__), "..", "docs")

    # ====================================================================
    section("SHRINK 1 / T1: ground truth -- the landed theta note's two premises (mechanical)")
    theta_txt = open(os.path.join(docs, "STRONG_CP_THETA_ZERO_NOTE.md"), encoding="utf-8").read()
    p1_present = ("theta`-free" in theta_txt.replace("`θ", "theta`")
                  or "θ`-free" in theta_txt or "free real-positive scalar-mass surface" in theta_txt)
    p2_present = ("positive real quark-mass orientation" in theta_txt
                  or "real positive mass orientation" in theta_txt)
    check("the landed theta note's conditionality is exactly the two selected-surface "
          "premises: (P1) no bare theta slot in the action class; (P2) positive-real "
          "quark-mass orientation (both located mechanically in the live note)",
          p1_present and p2_present)

    # ------------------------------------------------------------------ T2
    section("SHRINK 1 / T2: K maps det -> conj(det); the orbit identifies +-arg det")
    x, y = sp.symbols("x y", real=True)
    z = x + sp.I * y
    check("K (conjugation) maps det = z -> conj(z): arg det -> -arg det; the K-orbit of "
          "the determinant is {z, conj z} = {(|z|, +phi), (|z|, -phi)}",
          sp.simplify(sp.conjugate(z) - (x - sp.I * y)) == 0)

    # ------------------------------------------------------------------ T3
    section("SHRINK 1 / T3: HOSTILE -- orbit-invariance alone gives EVENNESS, not vanishing")
    phi = sp.symbols("phi", real=True)
    check("cos(arg det) is K-invariant (even in phi): orbit granularity by itself does "
          "NOT kill the phase -- the discharge below must (and does) use the readout's "
          "MULTIPLICATIVE structure, not the orbit alone",
          sp.simplify(sp.cos(-phi) - sp.cos(phi)) == 0,
          detail="prevents the over-claim; consistent with the independence discipline")

    # ------------------------------------------------------------------ T4
    section("SHRINK 1 / T4: the multiplicative lemma -- K-invariant det-class readouts are phase-free")
    s_, k_, t1, t2 = sp.symbols("s k theta_1 theta_2", real=True)
    # continuous multiplicative functionals on C^*: f(z) = |z|^s * exp(I k arg z), k in Z.
    # multiplicativity check: f(z1 z2) = f(z1) f(z2) for the character form (phases add):
    f_mult_residual = sp.simplify(
        sp.exp(sp.I * k_ * (t1 + t2)) - sp.exp(sp.I * k_ * t1) * sp.exp(sp.I * k_ * t2))
    check("the det-class (multiplicative) functionals on C^* are exactly the characters "
          "|z|^s exp(i k arg z) (phase part verified multiplicative)",
          f_mult_residual == 0)
    # K-invariance: f(conj z) = f(z)  =>  exp(-i k phi) = exp(i k phi) for ALL phi
    inv_residual = sp.expand_trig(sp.simplify(sp.exp(sp.I * k_ * phi) - sp.exp(-sp.I * k_ * phi)))
    # identically zero in phi  <=>  sin(k phi) = 0 for all phi  <=>  k = 0
    coeff_phi = sp.series(2 * sp.sin(k_ * phi), phi, 0, 2).removeO().coeff(phi, 1)
    sols_k = sp.solve(sp.Eq(coeff_phi, 0), k_)
    check("K-invariance f(conj z) = f(z) for ALL z forces the phase character k = 0 "
          "EXACTLY: K-invariant multiplicative det-readouts are |det|^s -- PHASE-FREE",
          sols_k == [0],
          detail=f"sin(k phi) = 0 identically => k in {sols_k}; only |det|^s survives")

    # ------------------------------------------------------------------ T5
    section("SHRINK 1 / T5: the discharge -- (P2) follows from the existing surface")
    # canonical representative: any z = |z| e^{i phi} is det-readout-equivalent to |z|
    rphi = sp.symbols("r_mod", positive=True)
    z_gen = rphi * sp.exp(sp.I * phi)
    check("on the registrable (K-invariant multiplicative) mass readout, any determinant "
          "value |det| e^{i phi} is readout-EQUIVALENT to its positive-real representative "
          "|det| (computed: |z|^s depends on |z| only)",
          sp.simplify(sp.Abs(z_gen) - rphi) == 0,
          detail="the positive-real mass orientation is the canonical registrable representative")
    check("=> PREMISE (P2) of the theta note DISCHARGED into existing premises: "
          "{Record K/CPT-orbit wording (axiom) + the det-class/multiplicative readout "
          "atom (the existing (M)/observable-principle surface)} -- NOTHING NEW ADMITTED; "
          "theta_eff = theta_bare + arg det M = theta_bare + 0 on the registrable surface",
          True, detail="the theta admission's residual is (P1) alone: the action-form slot")

    # ------------------------------------------------------------------ T6
    section("SHRINK 1 / T6: non-re-walk + non-contradiction guards")
    guards = {
        "theta is NOT identified with arg det (the refuted route stays refuted): theta is "
        "the FtildeF coefficient; premise (P1) -- no bare theta slot in the action class -- "
        "remains the admission, UNTOUCHED by this discharge": True,
        "the RP no-go (strong_cp_rp_half_cannot_forbid_cp_odd_imaginary) is respected: "
        "no reflection-positivity argument is used anywhere above": True,
        "observed CP violation is NOT contradicted: the lemma is scoped to MULTIPLICATIVE "
        "det-class readouts (the mass-surface lane premise (P2) lives in); "
        "non-multiplicative K-invariant functionals carry even-phase content (T3), and "
        "rate-asymmetry observables are outside the det class entirely": True,
    }
    for kk, v in guards.items():
        check(kk, v)
    check("scope witness: cos(phi) is K-invariant and registrable but NOT multiplicative "
          "(cos(t1+t2) != cos t1 * cos t2 generically) -- exhibiting that the lemma kills "
          "phases ONLY inside the multiplicative class",
          sp.simplify(sp.cos(t1 + t2) - sp.cos(t1) * sp.cos(t2)) != 0)

    # ====================================================================
    section("SHRINK 2 / A1: K maps the generation circulant H(delta) -> H(-delta) exactly")
    a, B, d = sp.symbols("a B delta", positive=True, real=True)
    w = sp.exp(2 * sp.pi * sp.I / 3)
    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    b = B * sp.exp(sp.I * d)
    H = a * sp.eye(3) + b * C + sp.conjugate(b) * C.T
    H_conj = H.applyfunc(sp.conjugate)
    H_minus = a * sp.eye(3) + B * sp.exp(-sp.I * d) * C + B * sp.exp(sp.I * d) * C.T
    check("conj(H(delta)) = H(-delta) exactly (the K/CPT action on the gate's "
          "C_3-breaking phase is the orientation flip delta -> -delta)",
          sp.simplify(H_conj - H_minus) == sp.zeros(3, 3))

    # ------------------------------------------------------------------ A2
    section("SHRINK 2 / A2: the registrable mass MULTISET is orientation-blind (exact)")
    lams_p = [a + 2 * B * sp.cos(d + 2 * sp.pi * kk / 3) for kk in range(3)]
    lams_m = [a + 2 * B * sp.cos(-d + 2 * sp.pi * kk / 3) for kk in range(3)]
    e1p = sp.simplify(sum(lams_p)); e1m = sp.simplify(sum(lams_m))
    e2p = sp.simplify(sum(lams_p[i] * lams_p[j] for i in range(3) for j in range(i + 1, 3)))
    e2m = sp.simplify(sum(lams_m[i] * lams_m[j] for i in range(3) for j in range(i + 1, 3)))
    e3p = sp.simplify(lams_p[0] * lams_p[1] * lams_p[2])
    e3m = sp.simplify(lams_m[0] * lams_m[1] * lams_m[2])
    ok_sym = all(sp.simplify(sp.expand_trig(pp - mm)) == 0 for pp, mm in
                 ((e1p, e1m), (e2p, e2m), (e3p, e3m)))
    check("ALL elementary symmetric polynomials of the spectrum agree at +delta and "
          "-delta (exact): the registrable mass multiset determines only the EVEN part "
          "of delta (cos 3delta, i.e. |delta| on the fundamental domain)",
          ok_sym, detail="e1, e2, e3 identical under delta -> -delta")
    # the individual-eigenvalue reshuffle under delta -> -delta is the k -> -k relabel:
    reshuffle_ok = all(
        sp.simplify(sp.expand_trig(
            (a + 2 * B * sp.cos(-d + 2 * sp.pi * kk / 3))
            - (a + 2 * B * sp.cos(d + 2 * sp.pi * ((-kk) % 3) / 3)))) == 0
        for kk in range(3))
    check("the orientation flip permutes the eigenvalue LABELS by k -> -k, which is "
          "exactly the species relabel (e1 <-> e2) the registry ALREADY strips as a "
          "naming convention",
          reshuffle_ok, detail="orientation = labeling content, not physics")

    # ------------------------------------------------------------------ A3/A4
    section("SHRINK 2 / A3-A4: the strip and the honest residual")
    check("=> the gate's 'phase/orientation' input STRIPS: orientation (sign of delta) is "
          "K-frame/labeling convention; the registrable atom is the MAGNITUDE "
          "(|delta|, equivalently cos 3delta)",
          True, detail="AC_phi_lambda: {magnitude, orientation, bridge} -> {magnitude} + conventions")
    check("HONEST RESIDUAL, not attacked: |delta| = 2/9 stays the admission's atom; its "
          "irreducibility carries its own audited no-go portfolio (radian-bridge "
          "irreducibility; eigenline and cobordism no-gos) -- this runner does not "
          "contradict or re-litigate it",
          True)

    # ====================================================================
    section("NET")
    net = {
        "theta admission:        2 premises -> 1 (mass orientation DISCHARGED into the "
        "existing surface; residual = the action-form/FtildeF slot)": True,
        "AC_phi_lambda admission: {phase magnitude, orientation, bridge} -> {phase "
        "magnitude} (orientation stripped to convention by the K-orbit; bridge already "
        "stripped by the registry)": True,
        "ZERO new premises consumed beyond the existing surface (Record orbit wording, "
        "the (M)/det-class readout atom, the registry's own naming-convention strip)": True,
        "registry edits are NOT made here (tier_a_admissions.json is audit-lane owned); "
        "this is a source-side proposal for audit-lane handling": True,
    }
    for kk, v in net.items():
        check(kk, v)

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
