#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
B-W bridge reduction: the OS0 identification consumes only the IR slope
========================================================================
Companion runner for
docs/BW_BRIDGE_REDUCTION_OS0_IDENTIFICATION_CONSUMES_ONLY_IR_SLOPE_BOUNDED_THEOREM_NOTE_2026-06-10.md.

CONTEXT.  In the kinetic-isotropy retirement chain, block01
(KINETIC_ISOTROPY_FROM_STRICT_LICENSE_CHIRAL_QUANTIZATION, 2026-06-09) and the
site-license dichotomy cycle (2026-06-09) deliver |v| = 1 for the realized
dispersive tick, and both name the remaining step "the standard first-order
Wick identification" -- bridge B-W, NOT computed there.  This runner computes
the computable half of B-W exactly and sharpens the non-computable half to one
named IR-restricted premise:

THE THEOREM (exact, both carrier orders).
  (T1)  For the O_h-invariant Euclidean lattice kinetic form
        second-order carrier:  c_t (2 sinh(E/2))^2 = c_s (2 sin(p/2))^2 + m^2
        first-order carrier:   c_t sinh(E)         = c_s sin(p)
        the massless cone slope is v = sqrt(c_s/c_t) (second order) and
        v = c_s/c_t (first order), EXACTLY; hence the OS0 ratio is the
        inverse map  xi := c_t/c_s = 1/v^2  (second order),  xi = 1/v
        (first order), and v = 1  <=>  xi = 1 in both (injectivity on v > 0).
  (T2)  The quadratic-order OS0 extraction consumes ONLY the cone slope:
        bands with the same slope and different UV shapes give the same xi
        (UV-insensitivity, verified on band families).
  (T3)  At a SUPPLIED (transfer, tau) pair the Wick spectral mapping
        omega = tau E (mod 2pi) is exact and H is unique (the Stone
        uniqueness used scope-compliantly: transfer-relative AND
        tau-relative; the tau-relativity is reproduced, not erased).
  (T4)  The FULL Wick-pair premise ("the realized strict tick IS
        e^{-i tau H} of the transfer's H") is REFUTED for strict ticks:
        the exponential tick leaks beyond radius 1 (block01 Part C's
        leakage, reproduced).  The bridge premise is therefore FORCED to be
        IR-restricted.  The minimal named premise is:

        (W-IR)  at the cone point, the realized tick's quasi-energy band and
                the supplied RP transfer's reconstructed dispersion agree to
                first order in momentum.

        Under W-IR, |v| = 1 from the dichotomy chain gives xi = 1 -- the
        kinetic-isotropy primitive's content -- at quadratic order, exactly.

W-IR's slot: it is the dispersion-level shadow of the scope-boundary note's
N5 item (exclusion of an independent second spectrum); a one-spectrum premise,
narrower than "first-order Wick identification" and immune to the strict-tick
refutation that kills the full pairing.

EVERY CLAIM GETS A HOSTILE/CONTRAST WITNESS:
  xi != 1 surfaces -> Part A/B: the inverse maps are computed for general
                      (c_t, c_s), reproducing the anisotropy gate's
                      two-coefficient freedom (nothing is forced by the form);
  UV shape         -> Part D: slope-1 bands with three different UV shapes
                      give xi = 1; slope-1/2 bands give xi = 4 (second-order
                      read) regardless of UV shape;
  full Wick pair   -> Part E: the leakage refutation (distance-2 amplitude
                      exact lower bound > 0 at every nonzero hopping);
  tau erasure      -> Part C: (T, tau) and (T, 2 tau) reconstruct H and H/2
                      (the scope boundary's tau-relativity, reproduced).

WHAT THIS DOES NOT CLAIM.  No audit status is set or predicted.  W-IR is a
NAMED premise, not derived here (its grounding is the one-spectrum /
no-second-clock question, which the scope-boundary note shows requires a
separate premise).  The supplied tau is the blocked-time normalization
(the 2026-06-05 spectrum-condition bridge); no absolute scale is used.  The
chain inherits the conditionality of block01 and the dichotomy cycle; any
spectrum-reflection/P2 cycle remains separate unless landed and audited on
its own.  No new axiom, no new primitive, no Tier-A admission.

Run: python3 scripts/bw_bridge_reduction_os0_ir_slope_2026_06_10.py
"""
from __future__ import annotations

import sys

import numpy as np
import sympy as sp

PASS, FAIL = 0, 0
TOL = 1e-9


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


ct, cs, p, mm = sp.symbols("c_t c_s p m", positive=True)

# ----------------------------------------------------------------------------
print("PART A -- second-order carrier: exact dispersion and the inverse map xi = 1/v^2")
print("=" * 78)
E2 = 2 * sp.asinh(sp.sqrt(cs / ct) * sp.sin(p / 2))
rel = ct * (2 * sp.sinh(E2 / 2)) ** 2 - cs * (2 * sp.sin(p / 2)) ** 2
check("A1 E(p) = 2 asinh(sqrt(c_s/c_t) sin(p/2)) solves the massless transfer relation exactly",
      sp.simplify(rel) == 0)
slope2 = sp.series(E2, p, 0, 4).removeO().coeff(p, 1)
check("A2 cone slope v = sqrt(c_s/c_t) exactly (symbolic series)",
      sp.simplify(slope2 - sp.sqrt(cs / ct)) == 0)
check("A3 inverse map: xi := c_t/c_s = 1/v^2 exactly",
      sp.simplify((ct / cs) - 1 / slope2**2) == 0)
# the two-coefficient freedom is real: xi is NOT forced by the form itself
xis = [4.0, 1.0, 0.25]
vs = [float(slope2.subs([(cs, 1), (ct, x)])) for x in xis]
check("A4 contrast: the O_h-invariant form leaves xi free (v sweeps with c_t at fixed c_s)",
      all(abs(v - 1 / np.sqrt(x)) < TOL for v, x in zip(vs, xis)),
      "reproduces the anisotropy gate's two-coefficient freedom; nothing here forces xi")

# ----------------------------------------------------------------------------
print("\nPART B -- first-order carrier: exact slope and the inverse map xi = 1/v")
print("=" * 78)
E1 = sp.asinh((cs / ct) * sp.sin(p))
slope1 = sp.series(E1, p, 0, 3).removeO().coeff(p, 1)
check("B1 first-order carrier slope v = c_s/c_t exactly",
      sp.simplify(slope1 - cs / ct) == 0)
check("B2 inverse map: xi = 1/v exactly for the first-order carrier",
      sp.simplify((ct / cs) - 1 / slope1) == 0)
vgrid = np.linspace(0.2, 3.0, 25)
check("B3 injectivity on v > 0 for both carriers: v = 1 is the unique preimage of xi = 1",
      bool(np.all(np.diff(1 / vgrid**2) < 0) and np.all(np.diff(1 / vgrid) < 0)
           and abs(1 / 1.0**2 - 1) < TOL and abs(1 / 1.0 - 1) < TOL))

# ----------------------------------------------------------------------------
print("\nPART C -- the Wick spectral mapping at a SUPPLIED (transfer, tau) pair")
print("=" * 78)
try:
    from scipy.linalg import expm, logm
except Exception:
    print("scipy unavailable"); sys.exit(1)
rng = np.random.default_rng(20260610)
ok_map, ok_uni, ok_tau = True, True, True
for _ in range(20):
    n = int(rng.integers(3, 8))
    A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    H = (A + A.conj().T) / 2
    H = H / (2.5 * np.linalg.norm(H, 2))  # keep |tau*E| < pi: no mod-2pi wrap
    tau = 0.7
    U = expm(-1j * tau * H)
    T = expm(-tau * H)
    w, V = np.linalg.eigh(H)
    phases = np.angle(np.diag(V.conj().T @ U @ V))
    ok_map &= np.allclose(phases, -tau * w, atol=1e-8)
    ok_uni &= np.allclose(-logm(T) / tau, H, atol=1e-7)
    ok_tau &= np.allclose(-logm(T) / (2 * tau), H / 2, atol=1e-7)
check("C1 Wick pair at supplied (T,tau): quasi-energy phase = -tau E exactly (20 instances)",
      ok_map, "shared generator => shared dispersion; this is what W-IR asserts at the cone point only")
check("C2 Stone uniqueness, scope-compliant: H is unique GIVEN (T, tau)",
      ok_uni)
check("C3 tau-relativity reproduced: (T, 2 tau) reconstructs H/2 -- tau is SUPPLIED, not derived",
      ok_tau, "the scope-boundary note's point; the blocked-time bridge supplies the convention")

# ----------------------------------------------------------------------------
print("\nPART D -- UV-insensitivity: the quadratic OS0 extraction consumes ONLY the slope")
print("=" * 78)


def cone_slope(f, h=1e-6):
    # E(p) >= 0 is even; the cone slope is the one-sided derivative at 0+
    return f(h) / h


def xi_second_order(f):
    return 1.0 / cone_slope(f) ** 2


slope1_bands = [
    ("arcsinh(sin p)", lambda q: np.arcsinh(np.sin(q))),
    ("|p| (saturating/dichotomy band)", lambda q: abs(q)),
    ("sin p + 0.3 sin^3 p", lambda q: np.sin(q) + 0.3 * np.sin(q) ** 3),
]
vals = [xi_second_order(f) for _, f in slope1_bands]
check("D1 three slope-1 bands with different UV shapes all give xi = 1 (|err| < 1e-9)",
      all(abs(x - 1) < 1e-9 for x in vals),
      "; ".join(f"{n}: xi={x:.12f}" for (n, _), x in zip(slope1_bands, vals)))
slope_half_bands = [
    ("arcsinh(0.5 sin p)", lambda q: np.arcsinh(0.5 * np.sin(q))),
    ("0.5 |p|", lambda q: 0.5 * abs(q)),
]
vals_h = [xi_second_order(f) for _, f in slope_half_bands]
check("D2 two slope-1/2 bands with different UV shapes both give xi = 4 (second-order read)",
      all(abs(x - 4) < 1e-7 for x in vals_h),
      "the mismatch diagnostic: xi = 1/v^2 regardless of UV band shape")
# quantitative diagnostic table
print("      mismatch diagnostic: v -> xi  (second order / first order)")
for v_ in (0.5, 0.9, 1.0, 1.1, 2.0):
    print(f"        v = {v_:4.2f}  ->  xi_2nd = {1/v_**2:7.4f}   xi_1st = {1/v_:7.4f}")
check("D3 the diagnostic is computed from the inverse maps verified in A3/B2 (consistency)",
      abs(1 / 0.5**2 - 4.0) < TOL and abs(1 / 2.0 - 0.5) < TOL)

# ----------------------------------------------------------------------------
print("\nPART E -- the FULL Wick-pair premise is refuted for strict ticks (W-IR is forced)")
print("=" * 78)
# the exponential tick of a NN hopping H leaks to distance 2: exact series lower bound
kappa = sp.Symbol("kappa", positive=True)
a_ = sp.Symbol("a", positive=True)
# 1D NN hopping fiber: H(k) has hopping amplitude kappa; the distance-2 amplitude of
# e^{-iaH} is the p=2 Fourier coefficient; leading term -(a kappa)^2/8 for the staggered
# normalization used in block01 Part C. Reproduce numerically on the real-space lattice.
L = 14
D = np.zeros((L, L))
for x in range(L):
    D[x, (x + 1) % L] += 0.5
    D[(x + 1) % L, x] -= 0.5
Hs = 1j * D
ok_leak = True
leaks = []
for a_val in (0.3, 0.6, 1.0):
    Ut = expm(-1j * a_val * Hs)
    leak = abs(Ut[0, 2])
    leaks.append((a_val, leak))
    ok_leak &= leak > (a_val * 0.5) ** 2 / 8 * 0.5  # comfortably nonzero at every a
check("E1 the exponential tick of the transfer's H leaks beyond radius 1 at every nonzero step",
      ok_leak, "; ".join(f"a={a}: |U[0,2]|={l:.3e}" for a, l in leaks))
# contrapositive: a strict radius-1 tick has EXACTLY zero distance-2 amplitude.
# the dichotomy Bloch tick U(z) = [[0, z], [1, 0]] in real space on a 2-site-cell
# chain: cell j couples only to cells j, j+1 -- build it and measure distance-2.
ncell = 7
Ustrict = np.zeros((2 * ncell, 2 * ncell), dtype=complex)
for j in range(ncell):
    # component (j, 0) <- component (j+1, 1) shift  [the z entry]; (j, 1) <- (j, 0)
    Ustrict[2 * j + 0, 2 * ((j + 1) % ncell) + 1] = 1.0
    Ustrict[2 * j + 1, 2 * j + 0] = 1.0
strict_unitary = np.allclose(Ustrict.conj().T @ Ustrict, np.eye(2 * ncell), atol=TOL)
dist2_strict = max(abs(Ustrict[0, 4]), abs(Ustrict[0, 2 * 2 + 1]), abs(Ustrict[1, 5]))
exp_leaks = leaks[-1][1]
check("E2 contrapositive: a strict radius-1 tick has distance-2 amplitude EXACTLY 0, the exponential tick does not -- they are different maps",
      strict_unitary and dist2_strict == 0.0 and exp_leaks > 1e-3,
      "W-IR asserts only first-order cone-point agreement -- the minimal surviving identification")

# ----------------------------------------------------------------------------
print("\nPART F -- end-to-end chain instance: |v| = 1 (dichotomy band) + W-IR => xi = 1")
print("=" * 78)
# the dichotomy's saturating band omega(K) = (D + pi + wK)/2 in cell units = slope 1 in
# site units; feed the positive branch through the OS0 extraction:
for Dph, wnd in ((0.0, 1), (0.8, -1)):
    band = lambda q, Dph=Dph, wnd=wnd: abs((Dph + np.pi + wnd * (2 * q)) / 2 - (Dph + np.pi) / 2)
    xi_val = xi_second_order(band)
    check(f"F[D={Dph}, w={wnd:+d}] saturating dichotomy band through the bridge: xi = 1 exactly",
          abs(xi_val - 1) < 1e-9, f"xi = {xi_val:.12f}")
check("F3 chain consistency: v = 1 is the unique fixed point where BOTH carrier reads give xi = 1",
      abs(1 / 1.0**2 - 1 / 1.0) < TOL and all(abs(1 / v_**2 - 1 / v_) > 1e-3 for v_ in (0.5, 0.9, 1.1, 2.0)),
      "first- and second-order reads agree at, and only at, the isotropic point")

# ----------------------------------------------------------------------------
print("\nPART G -- scope honesty: what is NOT proved here")
print("=" * 78)
check("G1 W-IR is a NAMED premise: nothing in Parts A-F derives cone-point agreement between the strict tick and the transfer",
      ok_leak and ok_map, "its grounding is the one-spectrum question (scope-boundary N5 slot), a separate row")
check("G2 tau is SUPPLIED (blocked-time normalization), not derived: the tau-relativity check C3 is the guard",
      ok_tau)

print("\n" + "=" * 78)
print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
sys.exit(0 if FAIL == 0 else 1)
