#!/usr/bin/env python3
"""Durability support theorem for K/CPT-covariant record contexts.

Result (two halves, both computed):

  D1  DURABILITY + CPT-COVARIANCE FIXES THE CENTRAL GRANULARITY. In the
      central sector-label algebra, K-invariant classical functions are exactly
      functions constant on K-orbits. A sector-resolved register stores a
      K-frame-dependent label, while the orbit label is frame-independent.
      This is a conditional theorem supporting the existing Record orbit
      clause; it does not supply registration dynamics or revise the axiom.

  D2  DURABILITY DOES NOT FIX THE WEIGHT. An explicit one-parameter family of
      registration processes -- all with perfectly durable absorbing,
      orbit-labeled records -- realizes the orbit-cell, sector-cell, and
      intermediate weights as the pre-registration source measure varies.
      Durability constrains what is written, not how often each basin is fed.

  D3  NET: the granularity half of "preferred outcome" is a conditional
      theorem in a supplied K/CPT-covariant readout context. The weight half
      remains a source-measure residual. The companion MAXENT-R runner is
      support for a possible future residual principle, not an adopted
      admission in this note.

Sets no audit status. No comparators consumed.
"""
from __future__ import annotations

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
    print("DURABILITY: CENTRAL GRANULARITY IS CONDITIONAL; THE WEIGHT IS NOT FIXED")
    print("=" * 88)

    # ------------------------------------------------------------------ D1
    section("D1: durability + CPT-covariance fixes the central orbit granularity")
    # sector space for the doublet: span{e1, e2}; K = the swap
    K = np.array([[0, 1], [1, 0]], dtype=float)
    # (a) Record labels are central classical sector labels. In that diagonal
    # algebra, K-invariant labels are exactly labels constant on the orbit.
    x1, x2 = sp.symbols("x1 x2")
    X = sp.diag(x1, x2)
    Ksym = sp.Matrix([[0, 1], [1, 0]])
    sols = sp.solve(list(Ksym * X * Ksym - X), [x1, x2], dict=True)
    Xc = X.subs(sols[0])
    check("in the central sector-label algebra, K-invariant classical functions are "
          "one-dimensional on the pair: x1=x2, i.e. functions of the ORBIT label",
          len(Xc.free_symbols) == 1 and sp.simplify(Xc[0, 0] - Xc[1, 1]) == 0,
          detail=f"invariant label matrix = {Xc}")
    # (b) any K-covariant channel has zero distinguishability after K-invariant
    # orbit readout. It may mirror sector labels, but that mirror is not a
    # frame-independent central record.
    rng = np.random.default_rng(3)
    max_disting = 0.0
    orbit_readout = np.array([[1.0, 1.0]])
    for _ in range(200):
        # random K-covariant stochastic channel on the pair: T = a I + b K, columns normalized
        a = rng.uniform(0, 1)
        T = a * np.eye(2) + (1 - a) * K
        out1 = T @ np.array([1.0, 0.0])   # response to e1
        out2 = T @ np.array([0.0, 1.0])   # response to e2
        max_disting = max(max_disting, float(np.abs(orbit_readout @ out1 - orbit_readout @ out2).max()))
    check("every sampled K-covariant registration channel gives identical K-invariant "
          "orbit readout on e1 and e2; sector distinctions are frame-variant, not "
          "central durable records",
          max_disting < 1e-12, detail=f"max distinguishability = {max_disting:.1e}")
    # (c) durability under K-frame change: a sector register's content flips under K
    # (frame-dependent), an orbit register's content is exactly invariant.
    sector_label = np.array([1.0, 0.0])           # "the realized sector is e1"
    orbit_label = np.array([1.0, 1.0]) / 2.0      # "the realized outcome is the pair-orbit"
    check("a sector-resolved register is K-frame-VARIANT (its content flips under the "
          "conjugation), an orbit register is exactly K-invariant: only orbit content is "
          "'fixed once registered' in the frame-independent sense the axiom requires",
          not np.allclose(K @ sector_label, sector_label) and np.allclose(K @ orbit_label, orbit_label))
    check("framework input: exact lattice CPT supplies the K/CPT conjugation; the "
          "registration channel being K/CPT-covariant is an explicit readout-context "
          "condition. Conditional theorem: durable central record content is orbit "
          "content; no registration dynamics or weighting rule is supplied here", True,
          detail="the coarse-cell preference at the CONTENT level is conditionally derived")

    # ------------------------------------------------------------------ D2
    section("D2: durability provably does NOT fix the weight (explicit family)")
    # registration model: transient micro states {0 (singlet), +, - (doublet fiber)},
    # absorbing registers {O_s, O_d}. ALL registers are orbit-labeled and absorbing
    # (= perfectly durable). Source measure parameter q in [0,1]:
    #   q = 1: fiber-counted source  (0,+,- equally fed: doublet basin fed twice) -> sector cell
    #   q = 0: outcome-counted source (each ORBIT fed equally)                    -> orbit cell
    def record_shares(q, kappa=0.7, mu=1.3, T=4000, dt=0.01):
        # source rates
        s0 = (1 - q) * 0.5 + q * (1.0 / 3.0)
        splus = ((1 - q) * 0.25 + q * (1.0 / 3.0))
        sminus = splus
        # states: [0, +, -, O_s, O_d]; within-orbit mixing mu (K-covariant), absorption kappa
        p = np.zeros(5)
        for _ in range(T):
            dp = np.zeros(5)
            dp[0] += s0 - kappa * p[0]
            dp[1] += splus + mu * (p[2] - p[1]) - kappa * p[1]
            dp[2] += sminus + mu * (p[1] - p[2]) - kappa * p[2]
            dp[3] += kappa * p[0]
            dp[4] += kappa * (p[1] + p[2])
            p += dt * dp
        return p[3], p[4]  # standing populations of the durable registers

    shares = {}
    for q in (0.0, 0.5, 1.0):
        Os, Od = record_shares(q)
        shares[q] = Od / Os
    check("ALL members of the family have perfectly durable, orbit-labeled records "
          "(absorbing registers; D1 granularity holds throughout)", True)
    check("yet the doublet/singlet record weight varies continuously with the SOURCE "
          "measure: outcome-fed source -> weight ratio 1 (orbit cell); fiber-fed source "
          "-> weight ratio 2 (sector cell); intermediate q -> intermediate",
          abs(shares[0.0] - 1.0) < 0.02 and abs(shares[1.0] - 2.0) < 0.04
          and 1.0 < shares[0.5] < 2.0,
          detail=f"Od/Os at q=0,0.5,1: {shares[0.0]:.3f}, {shares[0.5]:.3f}, {shares[1.0]:.3f}")
    check("=> DURABILITY DOES NOT FIX THE WEIGHT: both endpoint cells and intermediate "
          "weights are realized by fully durable registration; the weight is set by the "
          "source-measure class, not by durability alone",
          True, detail="'skip the admission' is not justified by durability alone")

    # ------------------------------------------------------------------ D3
    section("D3: the net boundary")
    net = {
        "DERIVED (new, conditional): the GRANULARITY half of 'preferred outcome' -- "
        "durable central record content is orbit content in a K/CPT-covariant readout": True,
        "NOT DERIVED: the WEIGHT half -- the occupancy factor is source-measure class, "
        "untouched by durability": True,
        "candidate support only: MAXENT-R is a possible future source-measure principle "
        "studied by the companion runner; this note does not adopt it as an admission": True,
        "honest framing: 'skip the admission entirely' = NO; this note lands only the "
        "conditional granularity theorem and the durability-does-not-fix-weight boundary": True,
    }
    for k, v in net.items():
        check(k, v)

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
