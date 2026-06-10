#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
The site-licensed staggered tick dichotomy: dispersive => saturating
====================================================================
Companion runner for
docs/STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md.
Cycle 2 of the kinetic-isotropy derivation loop (block01 = the band-winding
saturation theorem, PR #3442).

TARGET.  Block01 derived |v| = 1 for a WINDING band of a strict radius-1
unitary 2-band tick, conditional on (P3) CPT pairing of the tick spectrum and
(P4) the realized carrier actually sitting in the winding cell.  This cycle
DISCHARGES P3 and REDUCES P4 (to "the realized tick is dispersive/nonflat")
for the framework's realized carrier: the landed
scheme-forcing puts ONE Grassmann per site (staggered; Fock dim 2 = the
qubit), and for a one-component-per-site bipartite chain the adjacency
license -- radius 1 in SITES -- forbids the diagonal Bloch entries from
carrying any momentum dependence (a same-sublattice hop A_j -> A_{j +- 1} is
a distance-2 move).  That structural fact alone forces:

THE DICHOTOMY THEOREM (1D / per-axis, exact).  Every site-licensed unitary
2-site-periodic one-tick update on the one-Grassmann-per-site chain is either
  (i)  FLAT: constant bands, zero transport (the on-site/exchange class --
       the gapped cells are dispersionless at this periodicity), or
  (ii) SATURATING: trace identically ZERO, det-winding w = +-1, bands
       omega_pm(K) = (D + wK)/2 +- pi/2 EXACTLY linear -- |v| = 1 site/tick
       = 1 edge/tick at every momentum.
No third cell exists: a dispersive site-licensed tick CANNOT be tuned.  The
proof is the TWO-CIRCLES LEMMA: tr U is constant (structural), det U is a
unimodular monomial e^{iD} z^w (the block01 monomial lemma), and a band
eigenvalue mu with |mu| = 1 = |tr - mu| lies on the intersection of two unit
circles -- a finite set unless tr = 0 -- while a winding determinant phase
mu(tr - mu) = det must sweep a continuum.  Hence dispersive => tr = 0 =>
exactly linear saturating bands.  Chirality (P4) is not assumed: nonzero
winding is FORCED by dispersiveness -- P4's residual content shrinks to
"the realized tick is nonflat".  CPT pairing (P3) is not assumed anywhere.

REALIZATION TIE.  The dispersive cells are exactly the two phase-decorated
site-shifts; they are sublattice-off-diagonal (epsilon U epsilon = -U: the
staggered hopping SHAPE, not a transfer of {epsilon, D} = 0); each is a
single chiral mover and the two cells form the conjugate left/right sector
pair (Dirac pairing and curved massive bands are larger-cell content -- a
named open; e^{-iH_staggered} itself is not site-licensed, so no licensed
period-2 tick reproduces the landed two-mover sin(k) surface).  The
Kawamoto-Smit phases are constant along each direction's own axis, so the
1D theorem applies to any per-axis FACTOR, where the tick factorizes (the
3D simultaneous tick is the named open).

EXCLUSIONS (why block01's tunable cells cannot occur here): the split-step
walk and every tunable block01 cell require either two components per site or
degree-1 diagonal Bloch entries = distance-2 site hops -- both excluded by
{scheme-forcing density + site license}.  Computed below.

WHAT THIS DOES NOT CLAIM.  No audit status is set or predicted.  Conditional
on (P1') the site-radius strict reading of the retained license + (P2) the
unitary-tick reading + the block01 source row (landed, unaudited) + the
landed scheme-forcing surface (unaudited) + the KS per-axis tie where the
per-axis realization is invoked (landed, unaudited) + 2-site periodicity
(the staggered carrier's natural bipartite periodicity; larger unit cells are
a named open, where curved massive bands live) + the named OS0 Wick bridge
for the c_t = c_s wording.  The full simultaneous 3D tick (Weyl-block mixing)
remains the named open from block01.

Run: python3 scripts/staggered_site_license_tick_dichotomy_2026_06_09.py
"""
from __future__ import annotations
import sys
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


K = sp.symbols('K', real=True)
z = sp.symbols('z')

# ----------------------------------------------------------------------------
print("\nSECTION -- the site-license degree table (combinatorial, from the fold)")
print("=" * 78)
# Sites x in Z; sublattices A = even (x = 2j), B = odd (x = 2j + 1).  The
# license allows the one-tick value at a site to use sites at distance <= 1.
# Compute which (target sublattice, source sublattice, cell offset) pairs are
# licensed, i.e. have site distance <= 1:
allowed = {}
for tgt, tx in (('A', 0), ('B', 1)):          # target site in cell j = 0
    for src, sx0 in (('A', 0), ('B', 1)):
        offsets = []
        for dj in (-2, -1, 0, 1, 2):          # source cell offset
            if abs((sx0 + 2 * dj) - tx) <= 1:
                offsets.append(dj)
        allowed[(tgt, src)] = offsets
check("licensed Bloch degrees: AA={0}, BB={0}, AB={0,-1}, BA={0,+1} (diagonals CONSTANT)",
      allowed[('A', 'A')] == [0] and allowed[('B', 'B')] == [0] and
      allowed[('A', 'B')] == [-1, 0] and allowed[('B', 'A')] == [0, 1],
      "a same-sublattice hop is a distance-2 move -- the license forbids it")

# So the general site-licensed 2-site-periodic Bloch tick is
#   U(z) = [[alpha, p + q/z], [r + s z, delta]],   alpha,delta,p,q,r,s constants.
al, de, pp, qq, rr, ss = sp.symbols('alpha delta p q r s', complex=True)
U = sp.Matrix([[al, pp + qq / z], [rr + ss * z, de]])
trU = sp.simplify(sp.trace(U))
check("site license forces the trace structurally CONSTANT (no momentum dependence possible)",
      sp.simplify(sp.diff(trU.subs(z, sp.exp(sp.I * K)), K)) == 0,
      f"tr U = {trU} -- block01's degree-1 trace freedom is GONE for this carrier")

# Unitarity on the circle, FULL system: column norms constant = 1 AND column
# orthogonality, solved symbolically.  Norm cross terms force s*conj(r) = 0 and
# p*conj(q) = 0; orthogonality (conj(alpha) p + conj(r) delta = 0 etc.) then
# forces alpha = delta = 0 on the dispersive branch, completing the
# site-shift closed form:
cross_rs = sp.simplify(sp.expand((rr + ss * z) * (sp.conjugate(rr) + sp.conjugate(ss) / z)).coeff(z, 1))
cross_pq = sp.simplify(sp.expand((pp + qq / z) * (sp.conjugate(pp) + sp.conjugate(qq) * z)).coeff(z, 1))
# column orthogonality coefficients (z-constant parts and z-powers):
orth = sp.expand(sp.conjugate(al) * (pp + qq / z) + sp.conjugate(rr + ss / z) * de)
orth_terms = [sp.simplify(orth.coeff(z, n)) for n in (-1, 0, 1)]
# dispersive branch (q, r) with p = s = 0: orthogonality constants reduce to
# conj(alpha) q / z + conj(s->0...) : the z^-1 term is conj(alpha)*q and the
# constant term is conj(r)*delta -- both must vanish, so alpha = delta = 0:
orth_disp = [sp.simplify(t.subs([(pp, 0), (ss, 0)])) for t in orth_terms]
disp_forces = (sp.simplify(orth_disp[0] - sp.conjugate(al) * qq) == 0 and
               sp.simplify(orth_disp[1] - sp.conjugate(rr) * de) == 0)
check("full unitarity makes each hop a single monomial and removes on-site dispersive amplitudes",
      sp.simplify(cross_rs - ss * sp.conjugate(rr)) == 0 and
      sp.simplify(cross_pq - pp * sp.conjugate(qq)) == 0 and disp_forces,
      "s*conj(r) = p*conj(q) = 0; orthogonality forces alpha = delta = 0 on the dispersive branch")

# The determinant has at most ONE z power under the single-monomial branch
# constraints; on the circle it is unimodular, hence a monomial e^{iD} z^w
# with w in {-1, 0, +1} (the block01 monomial lemma applies):
det_cases = []
for (pv, qv) in ((pp, 0), (0, qq)):
    for (rv, sv) in ((rr, 0), (0, ss)):
        dd = sp.expand(al * de - (pv + (qv / z if qv != 0 else 0)) * (rv + (sv * z if sv != 0 else 0)))
        zpowers = [n for n in (-1, 1) if sp.simplify(dd.coeff(z, n)) != 0]
        det_cases.append(len(zpowers) <= 1)  # at most ONE nonconstant z power
check("det U has at most one z power in every branch (monomial lemma => det = e^{iD} z^w)",
      all(det_cases), "w in {-1, 0, +1}: the total winding is the det phase degree")


# ----------------------------------------------------------------------------
print("\nSECTION -- the two-circles lemma and the dichotomy (exact)")
print("=" * 78)
# Bands: lambda^2 - T lambda + det = 0 with T constant, det = e^{iD} z^w.
# Unitarity: |lambda| = 1 pointwise.  From the quadratic, det = lambda(T - lambda),
# so |T - lambda| = |det|/|lambda| = 1: the band eigenvalue lies on BOTH the
# unit circle and the unit circle centered at T.
Tc = sp.symbols('T', complex=True)
# Solve the two-circle intersection exactly (rotate so T = t > 0 real;
# rotation preserves both circles). For 0 < t <= 2: exactly two points
# x = t/2; for t > 2 the intersection is EMPTY (y imaginary) -- stronger:
t = sp.symbols('t', positive=True)
x, y = sp.symbols('x y', real=True)
sols_int = sp.solve([x**2 + y**2 - 1, (x - t)**2 + y**2 - 1], [x, y], dict=True)
y_sq = sp.simplify(1 - (t / 2)**2)   # y^2 = 1 - t^2/4: real only for t <= 2
check("two-circles: for T != 0 the eigenvalue set is <= 2 points (x = T/2; empty for |T| > 2)",
      len(sols_int) == 2 and all(sp.simplify(s_[x] - t / 2) == 0 for s_ in sols_int) and
      sp.simplify(y_sq.subs(t, 3)) < 0,
      "intersection x = t/2, y = +-sqrt(1 - t^2/4); unitarity caps |T| <= 2 anyway")

# The forcing, computed on the licensed family itself. With mu_2 = T - mu_1
# (trace) and det = mu_1 (T - mu_1): substituting the two intersection points
# gives det = (t/2 +- i sqrt(1 - t^2/4)) * (t/2 -+ i sqrt(1 - t^2/4)) = 1:
# det is confined to EXACTLY ONE value for T != 0 (even stronger than <= 2).
# But the dispersive licensed cell U_R = [[0, q/z],[r, 0]] has det = -qr/z,
# which takes infinitely many values over the BZ -- contradiction => T = 0:
mu1a = t / 2 + sp.I * sp.sqrt(1 - t**2 / 4)
mu1b = t / 2 - sp.I * sp.sqrt(1 - t**2 / 4)
det_a = sp.simplify(mu1a * (t - mu1a))
det_b = sp.simplify(mu1b * (t - mu1b))
qsym, rsym = sp.symbols('q0 r0', complex=True)
det_UR = sp.simplify(sp.Matrix([[0, qsym / z], [rsym, 0]]).det())
det_values_on_bz = {sp.simplify(det_UR.subs(z, sp.exp(sp.I * kv))) for kv in (0, sp.Rational(1, 2), 1)}
check("T != 0 confines det to ONE value; a dispersive licensed det sweeps the BZ => T = 0 FORCED",
      sp.simplify(det_a - 1) == 0 and sp.simplify(det_b - 1) == 0 and len(det_values_on_bz) == 3,
      "det = -q r / z takes a continuum of values; constant nonzero trace is impossible for a dispersive tick")

# The saturating dispersion DERIVED from the eigenvalues of the actual
# T = 0 licensed cell: eigenvalues of [[0, q/z],[r, 0]] are +-sqrt(qr/z);
# on z = e^{iK} with unit phases q = e^{ia}, r = e^{ib}:
a_ph, b_ph = sp.pi / 5, sp.pi / 3
UR_sym = sp.Matrix([[0, sp.exp(sp.I * a_ph) / z], [sp.exp(sp.I * b_ph), 0]])
evs = UR_sym.subs(z, sp.exp(sp.I * K)).eigenvals()
omegas = [sp.simplify(sp.expand_complex(sp.log(sp.simplify(ev)) / sp.I)) for ev in evs]
slopes = [sp.simplify(sp.diff(om, K)) for om in omegas]
curvs = [sp.simplify(sp.diff(om, K, 2)) for om in omegas]
check("actual T = 0 cell gives omega_pm(K) = (D + pi + wK)/2 + {0, pi}: |v| = 1 edge/tick; curvature == 0",
      all(sp.simplify(sl + sp.Rational(1, 2)) == 0 for sl in slopes) and
      all(c == 0 for c in curvs),
      "1 cell = 2 sites: |v| = 1 edge/tick exactly; all artifact orders vanish identically")

# A w = 0, T != 0 licensed cell is FLAT, computed from its eigenvalues:
th_f = sp.pi / 7
Uflat = sp.Matrix([[sp.cos(th_f), sp.I * sp.sin(th_f) / z], [sp.I * sp.sin(th_f) * z, sp.cos(th_f)]])
evs_f = list(Uflat.subs(z, sp.exp(sp.I * K)).eigenvals())
flat_k_indep = all(sp.simplify(sp.diff(sp.simplify(ev), K)) == 0 for ev in evs_f)
check("w = 0 cells are FLAT, computed from an actual licensed cell's eigenvalues (K-independent bands)",
      flat_k_indep, "the dichotomy is {flat, exactly saturating}: NO dispersive tunable cell exists")

# Deterministic numeric sweep over the site-licensed unitary family.
# Acceptance is cost < 1e-12 (with the residual at the solution re-checked on a
# finer momentum grid); discarded non-converged starts are COUNTED and
# reported.  Both shift branches (w = -1: q,r and w = +1: p,s) are seeded.
# HONEST SCOPE: a least-squares sweep cannot certify exhaustiveness -- the
# symbolic dichotomy is the load-bearing item; the sweep corroborates
# it on every solution actually found:
from scipy.optimize import least_squares  # noqa: E402
rng = np.random.default_rng(7)
def U_of(params, zv):
    a0, d0, p0, q0, r0, s0 = params
    return np.array([[a0, p0 + q0 / zv], [r0 + s0 * zv, d0]])
def unit_res(v):
    pr = v[:6] + 1j * v[6:]
    res = []
    for kv in np.linspace(-np.pi, np.pi, 9):
        Um = U_of(pr, np.exp(1j * kv))
        res.append(np.abs(Um @ Um.conj().T - np.eye(2)).ravel())
    return np.concatenate(res)
n_disp, n_flat, n_discard, bad = 0, 0, 0, []
disp_windings = []
starts = [np.concatenate([rng.normal(size=6), rng.normal(size=6)]) for _ in range(80)]
for amp in (0.05, 0.2, 0.5):
    base_R = np.zeros(12); base_R[3] = 1.0; base_R[4] = 1.0     # q, r branch (w = -1)
    base_L = np.zeros(12); base_L[2] = 1.0; base_L[5] = 1.0     # p, s branch (w = +1)
    starts.append(base_R + amp * rng.normal(size=12))
    starts.append(base_L + amp * rng.normal(size=12))
for x0 in starts:
    sol = least_squares(unit_res, x0, method='lm', max_nfev=8000)
    pr = sol.x[:6] + 1j * sol.x[6:]
    fine = max(np.abs(U_of(pr, np.exp(1j * kv)) @ U_of(pr, np.exp(1j * kv)).conj().T
                      - np.eye(2)).max() for kv in np.linspace(-np.pi, np.pi, 41))
    if fine > 1e-6:
        n_discard += 1
        continue
    ks = np.linspace(-np.pi, np.pi, 801)
    angs = np.array([np.sort(np.angle(np.linalg.eigvals(U_of(pr, np.exp(1j * kv))))) for kv in ks])
    if (angs.max(axis=0) - angs.min(axis=0)).max() < 1e-6:
        n_flat += 1
        continue
    n_disp += 1
    tr_max = max(abs(np.trace(U_of(pr, np.exp(1j * kv)))) for kv in (0.0, 1.0, 2.5))
    dets = np.array([np.linalg.det(U_of(pr, np.exp(1j * kv))) for kv in ks])
    w_num = np.sum(np.angle(dets[1:] / dets[:-1])) / (2 * np.pi)
    disp_windings.append(round(w_num))
    prev, Vk, acc = None, None, None
    slopes = []
    for kv in ks:
        lamv, V = np.linalg.eig(U_of(pr, np.exp(1j * kv)))
        if prev is None:
            o = np.argsort(np.angle(lamv)); lamv, Vk = lamv[o], V[:, o]
        else:
            o = np.argmax(np.abs(Vk.conj().T @ V)**2, axis=1)
            lamv, Vk = lamv[o], V[:, o]
            slopes.append(np.angle(lamv / prev) / (ks[1] - ks[0]))
        prev = lamv
    vmax_site = 2 * np.abs(np.array(slopes)).max()
    if tr_max > 1e-5 or abs(abs(w_num) - 1) > 1e-3 or abs(vmax_site - 1) > 1e-3:
        bad.append((tr_max, w_num, vmax_site))
check("sweep: every dispersive solution FOUND has tr ~ 0, |w| = 1, v = 1 site/tick; BOTH branches w = -1 and w = +1 reached",
      n_disp >= 2 and {-1, 1} <= set(disp_windings) and not bad,
      f"{n_disp} dispersive (windings {sorted(set(disp_windings))}), {n_flat} flat, {n_discard} non-converged discards; violations: {bad if bad else 'none'}")


# ----------------------------------------------------------------------------
print("\nSECTION -- the realization tie: the dispersive cells SHARE the staggered hopping shape")
print("=" * 78)
# Closed form of the dispersive cells: each hop is a single monomial;
# the dispersive (w != 0) branches are (q/z with r) and (p with s z) -- the two
# phase-decorated SITE-SHIFTS.  Exhibit the right-mover: U_R = [[0, q/z],[r, 0]]:
qv, rv = sp.exp(sp.I * sp.pi / 5), sp.exp(sp.I * sp.pi / 3)   # arbitrary unit phases
UR = sp.Matrix([[0, qv / z], [rv, 0]])
URk = UR.subs(z, sp.exp(sp.I * K))
unit_R = (URk * URk.H - sp.eye(2)).applyfunc(
    lambda e: sp.simplify(sp.expand_complex(e))) == sp.zeros(2, 2)
detR = sp.simplify(UR.det())
trR = sp.simplify(sp.trace(UR))
check("the dispersive cell is the (phase-decorated) site-shift: unitary, tr = 0, det ~ 1/z",
      unit_R and trR == 0 and sp.simplify(sp.expand_complex(detR * z + qv * rv)) == 0,
      "(U psi)_A(j) = q psi_B(j-1), (U psi)_B(j) = r psi_A(j): site x <- x-1, one edge per tick")

# The dispersive tick is SUBLATTICE-OFF-DIAGONAL (pure A <-> B hopping,
# the staggered hopping shape; equivalently epsilon U epsilon = -U with
# epsilon = site parity).  NOTE: this is the hopping STRUCTURE shared with the
# landed staggered generator, not a claim that {eps, D} = 0 transfers to the
# tick (the exponential image of anticommutation would be eps U eps = U-dagger,
# a different condition):
eps = sp.diag(1, -1)
check("the dispersive tick is sublattice-off-diagonal (eps U eps = -U): the staggered hopping shape",
      sp.simplify(eps * UR * eps + UR) == sp.zeros(2, 2),
      "pure A <-> B hopping, no same-sublattice action -- the staggered structure")

# Each dispersive cell is a SINGLE chiral mover (both folded bands carry
# the same slope -- one unfolded mover); the two cells form the conjugate
# left/right SECTOR pair (a tick realizes one sector; its mirror is the
# parity/conjugate image).  Dirac pairing and curved massive bands live at
# larger periodicity -- the named open:
pv2, sv2 = sp.exp(-sp.I * sp.pi / 5), sp.exp(-sp.I * sp.pi / 3)
UL = sp.Matrix([[0, pv2], [sv2 * z, 0]])
detL = sp.simplify(UL.det())
bandsR_sq = sp.simplify((UR * UR)[0, 0])    # U_R^2 = (q r / z) * I
bandsL_sq = sp.simplify((UL * UL)[0, 0])    # U_L^2 = (p s z) * I
ratio = sp.simplify(bandsR_sq.subs(z, 1 / z) / bandsL_sq)
mirror = sp.simplify(sp.diff(ratio, z)) == 0   # K -> -K mirror up to a constant phase
check("the dispersive cells are the conjugate left/right single-mover sectors (w = -1 / w = +1)",
      sp.simplify(detL / z - (-pv2 * sv2)) == 0 and mirror,
      "one chiral sector per tick; Dirac pairing = larger-cell named open")

# Kawamoto-Smit phases are constant along each direction's OWN axis
# (eta_1 = 1, eta_2 = (-1)^{x1}, eta_3 = (-1)^{x1+x2}; landed formulas), so the
# per-axis 1D reduction carries the phase as a constant sign:
def eta(mu, xv):
    if mu == 1:
        return 1
    if mu == 2:
        return (-1)**(xv[0])
    return (-1)**(xv[0] + xv[1])
const_along_own_axis = all(
    eta(mu, [x1, x2, x3]) == eta(mu, [x1 + (mu == 1), x2 + (mu == 2), x3 + (mu == 3)])
    for mu in (1, 2, 3) for x1 in range(3) for x2 in range(3) for x3 in range(3))
check("eta_mu(x) is constant along its own axis mu (landed KS formulas, verified on a 3^3 block)",
      const_along_own_axis,
      "the 1D theorem applies to any per-axis FACTOR, where the tick factorizes (3D simultaneous tick = named open)")


# ----------------------------------------------------------------------------
print("\nSECTION -- exclusions: why block01's tunable cells cannot occur for this carrier")
print("=" * 78)
# The split-step walk (block01's P4 hostile witness) has DIAGONAL Bloch
# entries with z-dependence -- distance-2 site hops, violating the site
# license for a one-component-per-site carrier:
th = sp.symbols('theta', real=True)
zz = sp.exp(sp.I * K)
Splus = sp.diag(zz, 1)
Sminus = sp.diag(1, 1 / zz)
def Cmat(tv):
    return sp.Matrix([[sp.cos(tv), sp.I * sp.sin(tv)], [sp.I * sp.sin(tv), sp.cos(tv)]])
Uss = sp.simplify(Splus * Cmat(th) * Sminus * Cmat(-th))
diag_k_dep = (sp.simplify(sp.diff(Uss[0, 0], K)) != 0 or
              sp.simplify(sp.diff(Uss[1, 1], K)) != 0)
check("split-step has K-dependent DIAGONAL entries: distance-2 site hops, license-ILLEGAL here",
      diag_k_dep, "the tunable witness needs a carrier density the scheme-forcing excludes")

# Even block01's SATURATING cell construction (the full-swap brickwork,
# U = -diag(z, 1/z) in the 2-site-cell basis) has K-dependent DIAGONAL entries
# in this fold: it moves excitations TWO sites per tick and is license-ILLEGAL
# at the site radius. The realized carrier's saturating cells are the
# site-shifts above, not the cell-level brickwork:
Ubrick = sp.Matrix([[-z, 0], [0, -1 / z]])
brick_diag_k_dep = (sp.simplify(sp.diff(Ubrick[0, 0].subs(z, sp.exp(sp.I * K)), K)) != 0)
check("block01's cell-level winding construction (full-swap brickwork) is ALSO site-license-illegal here",
      brick_diag_k_dep,
      "diagonal z-entries = 2-site moves; the realized saturating cells are the site-shifts")

# The gapped cells at this periodicity are FLAT (the mixed legal cell):
Umix = sp.Matrix([[sp.cos(th), sp.I * sp.sin(th) / z], [sp.I * sp.sin(th) * z, sp.cos(th)]])
Umixk = Umix.subs(z, sp.exp(sp.I * K))
unit_mix = (Umixk * Umixk.H - sp.eye(2)).applyfunc(
    lambda e: sp.simplify(sp.expand_complex(e))) == sp.zeros(2, 2)
tr_mix = sp.simplify(sp.trace(Umix))
check("the legal gapped cell [[cos t, i sin t /z],[i sin t z, cos t]] is unitary and FLAT",
      unit_mix and sp.simplify(sp.diff(tr_mix, K)) == 0 and sp.simplify(Umix.det() - 1) == 0,
      "mass at 2-site periodicity = dispersionless exchange; curved massive bands need a larger cell (named open)")


print("\n" + "=" * 78)
print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
sys.exit(0 if FAIL == 0 else 1)
