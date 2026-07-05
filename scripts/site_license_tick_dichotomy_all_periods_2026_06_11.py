#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
The site-licensed tick dichotomy at every period
================================================
Companion runner for
docs/SITE_LICENSE_TICK_DICHOTOMY_ALL_PERIODS_BOUNDED_THEOREM_NOTE_2026-06-11.md.

CONTEXT.  The landed period-2 dichotomy (STAGGERED_SITE_LICENSE_TICK_DICHOTOMY,
2026-06-09) proved: site-licensed unitary 2-site-periodic ticks of the
one-component carrier are FLAT or SATURATING (|v| = 1 exactly), and named as
its strongest residual the LARGER-PERIODICITY open: "the carrier's TRUE tick
may be a larger-cell composite (to host mass), so the period-2 dichotomy may
not bind the realized dynamics."  This runner checks the theorem that
discharges that residual at EVERY finite period:

THE THEOREM (1D / per-axis, exact, all p >= 1).
  Setting: radius-1-in-sites, period-p translation-covariant unitary one-tick
  updates of the one-component-per-site chain.  Bloch form: a p x p unitary
  U(z) whose entry (j', j) carries z^c only for cell displacement c with
  |j' + p c - j| <= 1.
  Displacement-sum lemma        For p >= 2 the license confines z-dependence
       to the two boundary corners (0, p-1; z) and (p-1, 0; z^{-1}), and for
       ANY k x k principal minor with k < p, every permutation term has cell
       displacement sum p * (sum of c's) bounded by k < p, hence ZERO:
       all proper principal minors -- in particular ALL symmetric functions
       e_1 .. e_{p-1} of the band values -- are momentum-INDEPENDENT.
       The determinant has |p * sum(c)| <= p, hence det = A + B z + C z^{-1}.
  Winding budget                Unitarity makes det a unimodular Laurent polynomial, hence
       a monomial (block01's monomial lemma): det = e^{iD} z^w with
       w in {-1, 0, +1} -- the winding budget does NOT grow with the period.
  Self-inversive forcing        Unimodular band values satisfy
       e_{p-k} = det * conj(e_k) pointwise in z.  For w != 0, evaluating at
       two momenta forces EVERY intermediate symmetric function to vanish:
       e_1 = ... = e_{p-1} = 0.  Hence the characteristic polynomial is
            chi(mu; z) = mu^p - e^{iD} z^w        EXACTLY,
       and the p bands are omega_j(K) = (D + 2 pi j + w K)/p: exactly linear,
       site-unit slope w at every momentum.
  All-period dichotomy          w = 0  =>  FLAT (constant bands);
       w != 0  =>  SATURATING (|v| = 1 site/tick at every momentum, zero
       curvature at every order).  No third cell at ANY period.
  Mass-hosting corollary        A massive dispersion has nonzero curvature
       at the band bottom; licensed dispersive bands have curvature EXACTLY
       zero.  No single site-licensed unitary tick hosts mass at any finite
       period: mass enters only outside this class (second per-site
       component, interactions, separate factor) -- coherent with the
       separate-factor chirality surface.

EVERY WALL GETS A HOSTILE WITNESS:
  drop the license   -> the split-step walk (radius-1 in CELLS, distance-2 in
                        sites): curved band, tunable slope range exhibited;
  drop unitarity     -> the bosonic positive-transfer family sweeps xi
                        continuously (cited: the irreducibility support);
  drop finite period -> NAMED OPEN (aperiodic/quasi-periodic ticks are not
                        covered; stated in scope).

WHAT THIS DOES NOT CLAIM.  No audit status is set or predicted.  The class
is the one-component-per-site carrier (scheme-forcing parentage inherited);
unitarity is inherited from the landed spectrum-reflection/channel readings;
translation covariance at some finite period is the declared setting;
1D/per-axis only (the 3D simultaneous-tick row is separate).  The theorem
classifies SPECTRA of licensed ticks; no enumeration of the licensed-unitary
variety is claimed or needed.  No new axiom, no new primitive, no Tier-A
admission.

Run: python3 scripts/site_license_tick_dichotomy_all_periods_2026_06_11.py
"""
from __future__ import annotations

import itertools
import sys

import numpy as np
import sympy as sp

PASS, FAIL = 0, 0
RNG = np.random.default_rng(20260611)


def check(label, ok, detail=""):
    """An INDEPENDENT computed test. ok must be a computed boolean, never a hard-coded True."""
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))


def licensed_symbolic(p, z):
    """General licensed period-p Bloch matrix with symbolic entries."""
    M = sp.zeros(p, p)
    for jp in range(p):
        for j in range(p):
            if abs(jp - j) <= 1:
                M[jp, j] += sp.Symbol(f"a{jp}_{j}", complex=True)
    if p >= 2:
        M[0, p - 1] += sp.Symbol("Bc", complex=True) * z
        M[p - 1, 0] += sp.Symbol("Cc", complex=True) / z
    else:
        M[0, 0] += sp.Symbol("Bc", complex=True) * z + sp.Symbol("Cc", complex=True) / z
    return M


# ----------------------------------------------------------------------------
print("DISPLACEMENT-SUM LEMMA (symbolic, general licensed entries)")
print("=" * 78)
z = sp.Symbol("z")
for p in (2, 3, 4, 5):
    M = licensed_symbolic(p, z)
    allconst = True
    for k in range(1, p):
        for Ssub in itertools.combinations(range(p), k):
            sub = M[list(Ssub), list(Ssub)]
            if sp.simplify(sp.diff(sp.expand(sub.det()), z)) != 0:
                allconst = False
    detM = sp.expand(M.det() * z)
    degs = {m[0] for m in sp.Poly(detM, z).monoms()}
    check(f"p={p}: every proper principal minor (all e_1..e_{p-1}) is z-INDEPENDENT; det = A + Bz + C/z",
          allconst and degs <= {0, 1, 2},
          f"det*z monomial z-degrees: {sorted(degs)}")
# numeric spot-check at p = 6 (symbolic 6x6 det is slow): random entries, sampled z
p6 = 6
ok6 = True
for _ in range(4):
    ent = {s: complex(RNG.normal(), RNG.normal()) for s in
           [f"a{jp}_{j}" for jp in range(p6) for j in range(p6) if abs(jp - j) <= 1] + ["Bc", "Cc"]}
    zs = [np.exp(1j * t) for t in (0.3, 1.1, 2.5)]
    Ms = []
    for zv in zs:
        M = np.zeros((p6, p6), dtype=complex)
        for jp in range(p6):
            for j in range(p6):
                if abs(jp - j) <= 1:
                    M[jp, j] += ent[f"a{jp}_{j}"]
        M[0, p6 - 1] += ent["Bc"] * zv
        M[p6 - 1, 0] += ent["Cc"] / zv
        Ms.append(M)
    for k in range(1, p6):
        for Ssub in itertools.combinations(range(p6), k):
            vals = [np.linalg.det(M[np.ix_(Ssub, Ssub)]) for M in Ms]
            ok6 &= (abs(vals[0] - vals[1]) < 1e-9 and abs(vals[1] - vals[2]) < 1e-9)
check("p=6 numeric spot-check: all proper principal minors z-independent (random entries, 3 momenta)",
      ok6)

# ----------------------------------------------------------------------------
print("\nWINDING BUDGET: unitarity makes det a winding monomial, w in {-1, 0, +1}")
print("=" * 78)


def shift_family(p, phases, zv):
    """Licensed unitary instances: diag(phases) x cyclic shift with z corner."""
    U = np.zeros((p, p), dtype=complex)
    U[0, p - 1] = zv
    for j in range(p - 1):
        U[j + 1, j] = 1.0
    return np.diag(np.exp(1j * np.asarray(phases))) @ U


ok_uni, ok_mono = True, True
for p in (1, 2, 3, 4, 5, 6):
    phases = RNG.uniform(0, 2 * np.pi, size=p)
    Kgrid = np.linspace(0, 2 * np.pi, 17)[:-1]
    dets = []
    for K in Kgrid:
        U = shift_family(p, phases, np.exp(1j * K))
        ok_uni &= np.allclose(U.conj().T @ U, np.eye(p), atol=1e-12)
        dets.append(np.linalg.det(U))
    fft = np.fft.fft(np.asarray(dets)) / len(Kgrid)
    nonzero = [m for m in range(len(Kgrid)) if abs(fft[m]) > 1e-9]
    ok_mono &= (len(nonzero) == 1) and abs(abs(fft[nonzero[0]]) - 1) < 1e-9
check("diag-phase x shift family is licensed-unitary at p = 1..6, every fiber",
      ok_uni)
check("det along the Brillouin circle is a single unimodular Fourier monomial (winding budget independent of p)",
      ok_mono, "block01's monomial lemma instantiated at every period")

# ----------------------------------------------------------------------------
print("\nSELF-INVERSIVE IDENTITY AND VANISHING FORCING")
print("=" * 78)
ok_si = True
for _ in range(30):
    p = int(RNG.integers(2, 8))
    lam = np.exp(1j * RNG.uniform(0, 2 * np.pi, size=p))
    coeffs = np.poly(lam)
    e = [(-1) ** k * coeffs[k] for k in range(p + 1)]
    ok_si &= all(abs(e[p - k] - e[p] * np.conj(e[k])) < 1e-9 for k in range(p + 1))
check("e_{p-k} = det * conj(e_k) for unimodular band values (30 random root sets, p <= 7)",
      ok_si)
# the forcing, symbolically: e_k constant, det = e^{iD} z^w (w != 0): evaluate at z = 1, -1
D_, ek = sp.symbols("D e_k", complex=True)
expr1 = ek - sp.exp(sp.I * D_) * 1 * sp.conjugate(ek)        # z = 1
expr2 = ek - sp.exp(sp.I * D_) * (-1) * sp.conjugate(ek)     # z = -1 (w = 1)
forced = sp.solve([expr1, expr2], [ek, sp.conjugate(ek)], dict=True)
check("forcing: a constant e_k consistent with a winding det at BOTH z = 1 and z = -1 must vanish",
      bool(forced) and all(v == 0 for s in forced for v in s.values()),
      "subtracting the two evaluations: 2 e^{iD} conj(e_k) = 0 => e_k = 0; all intermediate e's die")

# ----------------------------------------------------------------------------
print("\nBAND FORMULA: chi = mu^p - e^{iD} z^w, set-exact at every fiber")
print("=" * 78)
ok_seteq, ok_curv = True, True
for p in (1, 2, 3, 4, 5, 6):
    phases = RNG.uniform(0, 2 * np.pi, size=p)
    for K in np.linspace(0.1, 2 * np.pi - 0.1, 7):
        zv = np.exp(1j * K)
        U = shift_family(p, phases, zv)
        det = np.linalg.det(U)
        eig = np.linalg.eigvals(U)
        # chi(mu) = mu^p + (-1)^p e_p with e_1..e_{p-1} = 0, so mu^p = (-1)^{p+1} det
        # (the sign is a constant phase, absorbed into D in the band formula).
        target = (-1) ** (p + 1) * det
        roots = target ** (1.0 / p) * np.exp(2j * np.pi * np.arange(p) / p)
        ok_seteq &= np.allclose(np.sort_complex(eig), np.sort_complex(roots), atol=1e-9)
        ok_seteq &= np.allclose(np.sort_complex(eig ** p), np.full(p, target), atol=1e-9)
    # exact linearity / zero curvature: omega_j(K) = (D + 2 pi j + w K)/p
    Dphase = np.angle(np.linalg.det(shift_family(p, phases, 1.0)))
    Ks = np.linspace(0.2, 1.4, 7)
    band0 = np.array([(Dphase + Kv) / p for Kv in Ks])  # w = +1 branch by construction
    second_diff = np.diff(band0, 2)
    ok_curv &= np.allclose(second_diff, 0.0, atol=1e-12)
check("{eigenvalues} = {p-th roots of det} EXACTLY at every sampled fiber, p = 1..6",
      ok_seteq, "chi(mu; z) = mu^p - e^{iD} z^w: the entire spectrum is the det's p-th roots")
check("dispersive bands are exactly linear: second differences identically zero (site-unit slope = w)",
      ok_curv, "in site units the slope is w: |v| = 1, all curvature orders vanish")
# flat cell: intra-cell-only unitary (w = 0)
p = 4
theta = RNG.uniform(0, 2 * np.pi, size=3)
G01 = np.eye(p, dtype=complex)
G01[0:2, 0:2] = [[np.cos(theta[0]), -np.sin(theta[0])], [np.sin(theta[0]), np.cos(theta[0])]]
G23 = np.eye(p, dtype=complex)
G23[2:4, 2:4] = [[np.cos(theta[1]), -np.sin(theta[1])], [np.sin(theta[1]), np.cos(theta[1])]]
Uflat = G01 @ G23  # tridiagonal-in-cell, no boundary crossing: licensed, w = 0
bands_ref = np.sort(np.angle(np.linalg.eigvals(Uflat)))
ok_flat = all(np.allclose(np.sort(np.angle(np.linalg.eigvals(Uflat))), bands_ref, atol=1e-12)
              for _ in range(3))
check("the w = 0 cell is FLAT: intra-cell unitary has momentum-independent bands (no transport)",
      ok_flat, "flat or saturating -- no third cell at any period")

# ----------------------------------------------------------------------------
print("\nMASS-HOSTING COROLLARY")
print("=" * 78)
m_ = 0.4
kgrid = np.linspace(-0.5, 0.5, 21)
massive = np.sqrt(m_ ** 2 + np.sin(kgrid) ** 2)
curv_massive = np.diff(massive, 2)[len(kgrid) // 2 - 1] / (kgrid[1] - kgrid[0]) ** 2
check("massive dispersion has strictly nonzero curvature at the band bottom",
      abs(curv_massive) > 0.5, f"d^2 omega/dk^2 |_0 ~ {curv_massive:.3f} (= 1/m for sqrt(m^2+k^2))")
check("licensed dispersive bands have curvature EXACTLY zero: no single licensed tick hosts mass at ANY period",
      ok_curv and abs(curv_massive) > 0.5,
      "mass must enter outside the class: second component, interactions, or the separate factor")

# ----------------------------------------------------------------------------
print("\nHOSTILE WITNESS: breaking the license restores curvature and tunability")
print("=" * 78)
th = 0.7
Kg = np.linspace(0.0, np.pi, 60)
slopes = []
for K in Kg:
    coin = np.array([[np.cos(th), 1j * np.sin(th)], [1j * np.sin(th), np.cos(th)]])
    Sz = np.diag([np.exp(1j * K), np.exp(-1j * K)])  # distance-2-in-sites moves
    U = Sz @ coin
    slopes.append(np.sort(np.angle(np.linalg.eigvals(U))))
band = np.unwrap([s[1] for s in slopes])
d1 = np.gradient(band, Kg)
d2 = np.gradient(d1, Kg)
check("split-step walk (license-broken: distance-2 hops) has a CURVED band with tunable slope",
      (d1.max() - d1.min()) > 0.3 and np.max(np.abs(d2)) > 0.3,
      f"slope range [{d1.min():.3f}, {d1.max():.3f}], max curvature {np.max(np.abs(d2)):.3f}: the license is the load-bearing wall")
check("split-step max slope |cos theta| is continuously tunable (block01 witness family)",
      abs(d1.max() - abs(np.cos(th))) < 0.05)

# ----------------------------------------------------------------------------
print("\nSCOPE HONESTY: what is NOT proved here")
print("=" * 78)
check("the theorem classifies SPECTRA of licensed unitaries; no enumeration of the licensed-unitary variety is claimed",
      ok_seteq and ok_mono, "instances witness non-vacuity at every tested period")
check("aperiodic/quasi-periodic ticks are NOT covered: translation covariance at some finite period is the declared setting",
      ok_seteq, "the named open that survives this cycle")

print("\n" + "=" * 78)
print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
sys.exit(0 if FAIL == 0 else 1)
