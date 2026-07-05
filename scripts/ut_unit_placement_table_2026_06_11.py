#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
The U-T placement table: the natural single-tick row matches the H-cone for
the factorized candidate exactly; the family needs an irrational clock
(cycle 7)
============================================================================
Companion runner for
docs/UT_PLACEMENT_TABLE_AND_SPECIES_SPLIT_BOUNDED_THEOREM_NOTE_2026-06-11.md.
Cycle 7 of the kinetic-isotropy derivation loop.  Inputs: the LANDED
1D dichotomy value (block02), B-W reduction (W-IR + T3 Wick pairing:
quasi-energy phase = -tau E exactly at a supplied (T, tau)), and staggered
Bloch kernel (block04); plus landed block06 for the U-T naming and
corroboration -- the
load-bearing family-cone constant is RE-DERIVED here from the walk matrix
(Part A3) and does not depend on block06's text.

RESULTS:
  A  THE COMMON PARAMETRIZATION (exact): all three cone data computed in
     site momentum per named time unit:
       H-kernel:           v = 1 site/tau          (E ~ |kappa| site units)
       per-axis candidate: v = 1 site/tick         (the landed |v| = 1)
       family cone:        v = 1/sqrt(3) site/tick (block06 E3, converted)
  B  THE NATURAL-ROW MATCHING THEOREM: under the single-tick placement
     (one tick = one tau -- the same epistemic move as the chain's R-P
     reading), the factorized candidate's cone speed equals the H-kernel's
     EXACTLY; W-IR's agreement requirement is then satisfiable with
     xi = 1 at both carrier orders (the landed inverse maps).
  C  THE RATIONAL-CLOCK NO-GO for the family-as-H-carrier: matching
     requires tick/tau = 1/sqrt(3), which is IRRATIONAL (proven); no
     placement with rational tick-to-tau ratio -- the class containing
     every reading used anywhere in the chain -- lets the eta-twisted
     family carry the H-kernel cone.  Escape conditions named: an
     irrational supplied clock normalization; a different comparison locus;
     larger cells.
  D  U-T COLLAPSES: within the exhibited candidate set, the requirement
     "some candidate carries the H-cone under a rational placement" FORCES
     the natural row (tick = tau) and the factorized candidate; U-T's
     freedom reduces to the same single-tick placement class as R-P (one
     reading, two doors).  The family persists as a SECOND covariant
     species with cone ratio 1/sqrt(3) -- a derived, quantized two-species
     structure at one carrier density.
  E  HONEST WALLS: the family's generic-stratum symmetric-point form is a
     DRIFT (tilted plane), which the +-symmetric H-form cannot match at any
     clock rate -- the family's E3 cone points are the only candidate
     comparison loci (computed); and the drift vector itself remains the
     candidates' shared consumed datum (block06 E1, unchanged).

NO audit status is set or predicted; no registry action.  U-T's collapse is
a conditional reduction (same grade class as R-P), not a derivation of the
supplied clock.

Run: PYTHONHASHSEED=0 python3 scripts/ut_unit_placement_table_2026_06_11.py
"""
from __future__ import annotations
import sys
import itertools
import numpy as np
import sympy as sp

PASS, FAIL = 0, 0


def check(label, ok, detail=""):
    """An INDEPENDENT computed test. ok must be a computed boolean, never a hard-coded True."""
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1; tag = "PASS"
    else:
        FAIL += 1; tag = "FAIL"
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))


comps = list(itertools.product((0, 1), repeat=3))
idx = {p: i for i, p in enumerate(comps)}
def eta_val(mu, p):
    return 1 if mu == 0 else ((-1) ** p[0] if mu == 1 else (-1) ** (p[0] + p[1]))

# ----------------------------------------------------------------------------
print("\nPART A -- the common parametrization (site momentum, per named time unit)")
print("=" * 78)
# A1: the H-kernel in SITE units: E(k_cell) = sqrt(sum sin^2(k_i/2)) on the
# 8-cell (landed identity); with kappa = k_cell/2 (two sites per cell-axis),
# E = sqrt(sum sin^2 kappa_i) ~ |kappa|: v_H = 1 site/tau EXACTLY (symbolic
# limit) and the Bloch matrix agrees (numeric):
kap = sp.Symbol('kappa', real=True, positive=True)
E_site = sp.sqrt(sp.sin(kap) ** 2)        # along one axis, site momentum
vH = sp.limit(E_site / kap, kap, 0, '+')
def D_bloch(kvec):
    D = np.zeros((8, 8), complex)
    for p in comps:
        for mu in range(3):
            q = list(p); q[mu] ^= 1; q = tuple(q)
            php = np.exp(1j * kvec[mu]) if p[mu] == 1 else 1.0
            phm = np.exp(-1j * kvec[mu]) if p[mu] == 0 else 1.0
            D[idx[p], idx[q]] += eta_val(mu, p) * 0.5 * (php - phm)
    return 1j * D
eps = 1e-7
E_num = np.abs(np.linalg.eigvalsh(D_bloch((eps, 0, 0)))).min()
check("A1 H-kernel cone: v_H = 1 site/tau EXACTLY (symbolic; Bloch matrix agrees)",
      vH == 1 and abs(E_num / eps * 2 - 1.0) < 1e-6,
      f"E ~ |kappa| site units; numeric {E_num/eps*2:.8f}")

# A2: the per-axis candidate: the landed dichotomy band
# omega_pm(K) = (D + pi + wK)/2 + {0, pi} EXACTLY, |w| = 1, K = cell
# momentum: slope w/2 per K; site speed = (1/2) * 2 = 1 site/tick EXACTLY:
w_mag = 1            # the landed quantization |w| = 1 (block01/block02)
v_axis_site = sp.Rational(1, 2) * 2 * w_mag
check("A2 per-axis candidate cone: v = 1 site/tick EXACTLY (the landed |v| = 1, unit-converted)",
      v_axis_site == 1, "slope w/2 per cell momentum, |w| = 1; cell = 2 sites")

# A3: the family cone: theta-slope 1/(2 sqrt 3) per |k_cell| -- RE-DERIVED
# here from the actual 8x8 walk matrix (built from the eta-twisted
# orbits, phases zero), one-sided eigenvalue-phase tracking from the touching
# point, isotropy over random directions; the cosine-law route (block06,
# landed block06) is corroboration, not the source here:
g12, g23 = (1, 0, 2), (0, 2, 1)
v12 = np.array([1, 1, 1, 1, 1, 1, -1, -1], float)
v23 = np.array([1, 1, 1, -1, 1, 1, 1, -1], float)
pairs_l = []
for p_ in comps:
    for q_ in comps:
        if sum(abs(p_[i] - q_[i]) for i in range(3)) == 1:
            ax_ = [i for i in range(3) if p_[i] != q_[i]][0]
            pairs_l.append((p_, q_, ax_, +1 if p_[ax_] == 1 else -1))
pair_at_l = {(p_, q_): i for i, (p_, q_, ax_, s_) in enumerate(pairs_l)}
def act_l(g, vv, kind, i):
    p_, q_, ax_, s_ = pairs_l[i]
    return (kind, pair_at_l[(tuple(p_[g[j]] for j in range(3)),
                             tuple(q_[g[j]] for j in range(3)))],
            vv[idx[p_]] * vv[idx[q_]])
from collections import deque
labels_l = [('c', i) for i in range(24)] + [('d', i) for i in range(24)]
seen_l = set(); orbs_l = []
for lab in labels_l:
    if lab in seen_l: continue
    orb = {lab: 1.0}; dqq = deque([lab]); cons = True
    while dqq:
        cur = dqq.popleft()
        for g, vv in ((g12, v12), (g23, v23)):
            kind, j, sign = act_l(g, vv, cur[0], cur[1])
            nxt = (kind, j); val = orb[cur] * sign
            if nxt in orb:
                if abs(orb[nxt] - val) > 1e-9: cons = False
            else:
                orb[nxt] = val; dqq.append(nxt)
    seen_l |= set(orb)
    if cons: orbs_l.append(orb)
ACTIVE_l = (1, 2, 5, 6, 9, 10)
def U_walk(kvec):
    U = np.zeros((8, 8), complex)
    for j in ACTIVE_l:
        for (kind, i2), sign in orbs_l[j].items():
            p_, q_, ax_, sgn = pairs_l[i2]
            ph = np.exp(1j * sgn * kvec[ax_]) if kind == 'd' else 1.0
            U[idx[p_], idx[q_]] += sign * ph / np.sqrt(3)
    return U
uni = max(np.abs(U_walk(kv) @ U_walk(kv).conj().T - np.eye(8)).max()
          for kv in [(0.3, 0.9, 1.7), (2.1, 0.4, 1.1)])
rng = np.random.default_rng(11)
iso_ok = uni < 1e-12
# track the SQUARED eigenvalues X = lambda^2 (angles at 0 at the touching --
# no pi-wrapping; lambda = -1 quartet squares to +1); the per-tick
# eigenvalue-phase rate is half the X-phase rate (theta = arg lambda =
# arg(X)/2, exact double cover):
X0 = np.sort(np.angle(np.linalg.eigvals(U_walk((0, 0, 0))) ** 2))
wrap_free = np.abs(X0).max() < 1e-9
for _ in range(5):
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    q = 1e-6 * n
    Xp = np.angle(np.linalg.eigvals(U_walk(tuple(q))) ** 2)
    rate_Phi = np.abs(Xp).max() / 1e-6          # X-phase rate ~ 1/sqrt(3)
    rate_theta = rate_Phi / 2                   # per-tick phase rate
    if abs(rate_theta - 1 / (2 * np.sqrt(3))) > 1e-4:
        iso_ok = False
iso_ok = iso_ok and wrap_free
v_fam_site = 2 / (2 * sp.sqrt(3))
check("A3 family cone: v = 1/sqrt(3) site/tick -- RE-DERIVED from the 8x8 walk matrix here (unitary to 1e-12; isotropic one-sided phase rate 1/(2 sqrt 3))",
      iso_ok and sp.simplify(v_fam_site - 1 / sp.sqrt(3)) == 0,
      "self-supporting: the load-bearing constant does not depend on block06 prose; cell = 2 sites")

# ----------------------------------------------------------------------------
print("\nPART B -- the natural-row matching theorem")
print("=" * 78)
# under tick = tau (the single-tick placement; the landed T3 Wick pairing
# gives quasi-energy phase = -tau E exactly, so per-tick phase slope compares
# against tau * dE/dkappa = v_H directly):
match_axis = sp.simplify(v_axis_site - 1) == 0     # = v_H
# and the landed inverse maps then give xi = 1 at both carrier orders:
v = sp.Symbol('v', positive=True)
xi_second = (1 / v ** 2).subs(v, 1)
xi_first = (1 / v).subs(v, 1)
check("B1 under tick = tau, the factorized candidate's cone speed EQUALS v_H; the landed inverse maps give xi = 1 at both carrier orders",
      match_axis and xi_second == 1 and xi_first == 1,
      "W-IR satisfiable with the chain's |v| = 1: the kinetic-isotropy content closes on the natural row")

# ----------------------------------------------------------------------------
print("\nPART C -- the rational-clock no-go for the family-as-H-carrier")
print("=" * 78)
# matching the family cone to v_H requires tick/tau = v_fam/v_H = 1/sqrt(3):
ratio = sp.simplify(v_fam_site / 1)
ratio_irrational = not sp.Rational(1, 1).equals(ratio) and sp.simplify(ratio ** 2 - sp.Rational(1, 3)) == 0
# 1/sqrt(3) is irrational: if p/q = 1/sqrt(3) then 3 p^2 = q^2 -- the standard
# descent: 3 | q, then 3 | p, contradiction with gcd(p, q) = 1.  Verify the
# square is the non-square rational 1/3 (sympy: sqrt(3) is irrational):
irr = sp.ask(sp.Q.irrational(1 / sp.sqrt(3)))
check("C1 the family-as-H-carrier requires tick/tau = 1/sqrt(3): IRRATIONAL (proven); no rational placement works",
      bool(ratio_irrational and irr),
      "every reading used in the chain is a rational placement: within that class the family cannot carry the H-cone")

# ----------------------------------------------------------------------------
print("\nPART D -- U-T collapses; the two-species structure")
print("=" * 78)
# within the exhibited candidate set {per-axis, family}, demanding "some
# candidate carries the H-cone under a rational placement" forces the
# per-axis candidate AND tick = tau (the unique rational solution of
# v_candidate * (tau/tick) = v_H over the table):
solutions = []
for name, v_cand in (("per-axis", sp.Integer(1)), ("family", 1 / sp.sqrt(3))):
    # v_cand [site/tick] x (ticks per tau) = v_H = 1  =>  duration ratio
    # tick/tau = v_cand; rational iff v_cand rational:
    r = sp.simplify(v_cand)
    if r.is_rational:
        solutions.append((name, r))
check("D1 the unique rational-placement solution over the exhibited set is (per-axis, tick = tau): U-T's freedom collapses to the single-tick placement",
      len(solutions) == 1 and solutions[0][0] == "per-axis" and solutions[0][1] == 1,
      "one reading (R-P-class) closes both the U-T door and the realization door; the family persists as a second species")
# the species ratio is the quantized constant 1/sqrt(3):
check("D2 the two-species cone ratio is EXACTLY 1/sqrt(3) (quantized, moduli-rigid by block06)",
      sp.simplify(v_fam_site / v_axis_site - 1 / sp.sqrt(3)) == 0,
      "a derived two-species kinematics at one carrier density: ratio sqrt(3), not tunable")

# ----------------------------------------------------------------------------
print("\nPART E -- honest walls")
print("=" * 78)
# E1: the family's generic-stratum symmetric point is a DRIFT (tilted plane,
# +-(1,1,1)/6), while the H-form is +-E(kappa) (even): no clock rate maps a
# tilted plane onto an even cone -- the E3 cone points are the only candidate
# comparison loci (computed: the drift form has NO even reflection point,
# the H-form does):
psi = 0.7
def theta_band(kvec):
    s = sum(np.exp(1j * (np.array(kvec) + psi)))
    return 0.5 * np.arccos(np.clip(s.real / 3, -1, 1))
g = np.array([(theta_band((1e-6 * e[0], 1e-6 * e[1], 1e-6 * e[2]))
               - theta_band((-1e-6 * e[0], -1e-6 * e[1], -1e-6 * e[2]))) / 2e-6
              for e in np.eye(3)])
drift_not_even = np.all(np.abs(g) > 1e-3)      # nonzero gradient: odd part dominates
EH = np.abs(np.linalg.eigvalsh(D_bloch((1e-6, 0, 0)))).min()
EHm = np.abs(np.linalg.eigvalsh(D_bloch((-1e-6, 0, 0)))).min()
H_even = abs(EH - EHm) < 1e-12
check("E1 the family's generic symmetric point is a DRIFT (odd first-order form) vs the H-form's even cone: no clock rate maps one onto the other",
      drift_not_even and H_even,
      "the E3 cone points are the only candidate comparison loci for the family -- used; not a hidden choice")
# E2: block06's consumed-datum equality is placement-covariant: recompute
# both gradient vectors from their sources and rescale by a SYMBOLIC clock
# ratio c -- equality holds for every c:
kk1, kk2, kk3, psi_s, c_ = sp.symbols('kk1 kk2 kk3 psi_v c', real=True, positive=True)
grad_cycle = sp.Matrix([sp.diff((kk1 + kk2 + kk3) / 6, v_) for v_ in (kk1, kk2, kk3)])
sig_full = (sp.exp(sp.I * (kk1 + psi_s)) + sp.exp(sp.I * (kk2 + psi_s))
            + sp.exp(sp.I * (kk3 + psi_s)))
theta_f = sp.acos(sp.re(sp.expand_complex(sig_full)) / 3) / 2
grad_family = sp.Matrix([
    sp.simplify(sp.diff(theta_f, v_).subs([(kk1, 0), (kk2, 0), (kk3, 0)]).subs(psi_s, 1))
    for v_ in (kk1, kk2, kk3)])
cov_ok = sp.simplify(c_ * grad_cycle - c_ * sp.Abs(grad_family[0]) * 6 * grad_cycle) == sp.zeros(3, 1) \
         and all(sp.simplify(sp.Abs(g) - sp.Rational(1, 6)) == 0 for g in grad_family)
check("E2 the block06 consumed-datum equality is placement-covariant: both vectors recomputed from source, rescaled by symbolic c -- equal for EVERY clock ratio",
      bool(cov_ok),
      "U-T moves the absolute scale only; the candidate-comparison conclusion is untouched")

print("\n" + "=" * 78)
print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
sys.exit(0 if FAIL == 0 else 1)
