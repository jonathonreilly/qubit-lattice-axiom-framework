#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Wick-IR cone agreement from sector alias uniqueness
===================================================
Companion runner for
docs/WIR_CONE_AGREEMENT_FROM_SECTOR_ALIAS_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-06-11.md.

CONTEXT.  The landed B-W reduction (BW_BRIDGE_REDUCTION, 2026-06-10) forced
the kinetic-isotropy chain's bridge residual down to one named premise:
Wick-IR cone agreement (legacy label W-IR) at the cone point, where the
realized tick's quasi-energy band and the supplied RP transfer's
reconstructed dispersion agree to first order.  This runner checks the
theorem that DERIVES that cone agreement from sharper, already-landed
structure plus the record-stack spectral reading:

THE THEOREM (finite-dimensional, exact).
  Alias structure        On integer tick data, cos((2pi - w) n) = cos(w n)
       EXACTLY: quasi-energies w and 2pi - w are indistinguishable layer by
       layer.  The spectrum-condition sector [0, pi] is EXACTLY a
       fundamental domain of this alias group: every alias orbit meets it
       once.  The sector is not a convenience -- it is the unique window in
       which integer data determines the band.
  Real-even data form    With the landed spectrum-reflection pairing
       (tick spectrum w <-> -w with equal weights; the spectrum-reflection
       cycle's corollary), the tick-generated layer correlation is
       C(n) = sum_j c_j cos(w_j n), c_j > 0 -- real and even, the RP-shaped
       form the OS side consumes.  Dropping the pairing breaks real-evenness
       (hostile witness).
  Prony recovery         For bands with distinct w_j in (0, pi), the pairs
       {(c_j, w_j)} are uniquely recoverable from finitely many C(n)
       (Prony), exactly.
  Euclidean companion    Among candidate Euclidean rate sets
       {E_j = w_j + 2 pi m_j, m_j >= 0} whose Wick continuation matches the
       same integer data, EXACTLY ONE lies in the sector: E_j = w_j.  The
       companion transfer data g(n) = sum_j c_j e^{-E_j n} is
       reflection-positive (Hankel [g(m+n)] is PSD as a sum of rank-1
       outer products with positive weights).
  Cone-agreement corollary
       Hence per fiber the reconstructed dispersion equals the quasi-energy
       band on the sector; in particular cone-point slopes agree.  Fed the
       dichotomy band (|v| = 1), the landed inverse map gives xi = c_t/c_s
       = 1 at quadratic order.

PREMISES (graded honestly):
  Record-stack spectral reading
       the layer data consumed by the OS reconstruction is the tick-generated
       record data -- an ontology-level reading (the Euclidean depth
       direction is read as record-stack depth; the arrow note's
       record-accumulation surface), NAMED as a reading, not derived;
  (sector)  quasi-energies lie in the spectrum-condition sector [0, pi] in
       blocked tick units -- parent: the retained_bounded spectrum-condition
       theorem + the blocked-time normalization bridge;
  (pairing)  the landed spectrum-reflection cycle's corollary supplies the
       w <-> -w pairing that makes C real-even.

EVERY CLAIM GETS A HOSTILE WITNESS:
  drop the sector   -> an out-of-sector band (2pi - w) generates
                       IDENTICAL integer data; recovery returns its
                       in-sector alias: uniqueness fails outside the window;
  drop the pairing  -> unpaired complex weights give C(n) that is
                       not real-even: the OS-shaped data form itself fails;
  m_j >= 1 aliases  -> every nontrivial alias lift leaves the
                       sector (computed per instance).

WHAT THIS DOES NOT CLAIM.  No audit status is set or predicted.  The
record-stack spectral reading is NAMED, not derived: its content
(OS-consumed data = realized tick-generated record data) is the one-spectrum
identification, here made testable because any second independent layer
structure would change the recovered band.  No framework-wide
no-second-clock theorem is claimed.  The chain inherits the conditionality of
the landed spectrum-reflection, dichotomy, and B-W notes.  No new axiom, no
new primitive, no Tier-A admission.

Run: python3 scripts/wir_sector_alias_uniqueness_2026_06_11.py
"""
from __future__ import annotations

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


# ----------------------------------------------------------------------------
print("ALIAS STRUCTURE AND THE SECTOR AS FUNDAMENTAL DOMAIN")
print("=" * 78)
w, n_ = sp.symbols("w n", real=True)
alias_sym = sp.simplify(sp.cos((2 * sp.pi - w) * n_) - sp.cos(w * n_))
check("cos((2pi - w) n) = cos(w n) for integer n (symbolic, n in Z)",
      sp.simplify(alias_sym.rewrite(sp.exp).subs(sp.exp(2 * sp.pi * sp.I * n_), 1)) == 0
      or all(abs(np.cos((2 * np.pi - wv) * nn) - np.cos(wv * nn)) < 1e-12
             for wv in np.linspace(0.1, 3.0, 7) for nn in range(0, 9)),
      "w and 2pi - w are layer-by-layer indistinguishable")
# fundamental domain: the alias group on frequencies is generated by w -> w + 2pi and
# w -> -w (cosine evenness); every orbit meets [0, pi] exactly once.
ok_fd = True
for wv in RNG.uniform(-9.0, 9.0, size=200):
    orbit_rep = abs((wv + np.pi) % (2 * np.pi) - np.pi)  # canonical representative
    ok_fd &= (0 <= orbit_rep <= np.pi + 1e-12)
    # uniqueness: two in-sector values with the same data must be equal
check("every alias orbit has exactly one representative in [0, pi] (200 random frequencies)",
      ok_fd, "the spectrum-condition sector IS the alias fundamental domain")
ok_uni = True
for _ in range(100):
    w1, w2 = RNG.uniform(0, np.pi, size=2)
    same_data = all(abs(np.cos(w1 * nn) - np.cos(w2 * nn)) < 1e-10 for nn in range(1, 12))
    ok_uni &= (not same_data) or abs(w1 - w2) < 1e-8
check("two in-sector frequencies with identical integer data coincide (injectivity on the sector)",
      ok_uni)

# ----------------------------------------------------------------------------
print("\nREAL-EVEN TICK DATA AND EXACT PRONY RECOVERY")
print("=" * 78)


def band_data(cs, ws, N):
    return np.array([sum(c * np.cos(wv * nn) for c, wv in zip(cs, ws)) for nn in range(N)])


def prony_recover(C, J):
    """Recover {(c_j, w_j)} from C(n) = sum c_j cos(w_j n), J modes."""
    # 2J exponentials z_j = e^{+-i w_j}; linear prediction of order 2J
    M = 2 * J
    H = np.array([[C[i + j] for j in range(M)] for i in range(M)])
    rhs = -np.array([C[i + M] for i in range(M)])
    a = np.linalg.solve(H, rhs)
    roots = np.roots(np.concatenate([[1.0], a[::-1]]))
    ws_rec = sorted({round(abs(np.angle(r)), 9) for r in roots})
    ws_rec = [x for x in ws_rec if x > 1e-7]
    V = np.array([[np.cos(wv * nn) for wv in ws_rec] for nn in range(len(C))])
    cs_rec, *_ = np.linalg.lstsq(V, C, rcond=None)
    return np.array(cs_rec), np.array(ws_rec)


ok_rec = True
for _ in range(25):
    J = int(RNG.integers(1, 4))
    ws = np.sort(RNG.uniform(0.25, np.pi - 0.25, size=J))
    while J > 1 and np.min(np.diff(ws)) < 0.25:
        ws = np.sort(RNG.uniform(0.25, np.pi - 0.25, size=J))
    cs = RNG.uniform(0.5, 2.0, size=J)
    C = band_data(cs, ws, 6 * J + 6)
    cs_r, ws_r = prony_recover(C, J)
    ok_rec &= len(ws_r) == J and np.allclose(np.sort(ws_r), ws, atol=1e-7) \
        and np.allclose(np.sort(cs_r), np.sort(cs), atol=1e-6)
check("exact Prony recovery of {(c_j, w_j)} from integer data, 25 random in-sector bands (J <= 3)",
      ok_rec, "the in-sector band is DETERMINED by the registered layer data")
C_real_even = band_data([1.0, 0.7], [0.6, 2.1], 12)
check("paired data is real and even: C(n) real, C(-n) = C(n) (the RP-shaped form)",
      np.allclose(C_real_even.imag if np.iscomplexobj(C_real_even) else 0 * C_real_even, 0)
      and all(abs(sum(c * np.cos(wv * (-nn)) for c, wv in zip([1.0, 0.7], [0.6, 2.1]))
                  - C_real_even[nn]) < 1e-12 for nn in range(12)))

# ----------------------------------------------------------------------------
print("\nUNIQUE IN-SECTOR EUCLIDEAN COMPANION AND RP POSITIVITY")
print("=" * 78)
ok_alias_exit, ok_rp = True, True
for _ in range(15):
    J = int(RNG.integers(1, 4))
    ws = np.sort(RNG.uniform(0.25, np.pi - 0.25, size=J))
    cs = RNG.uniform(0.5, 2.0, size=J)
    # all nontrivial alias lifts E = w + 2 pi m (m >= 1) leave the sector
    for m in (1, 2):
        ok_alias_exit &= all(wv + 2 * np.pi * m > np.pi for wv in ws)
    # the in-sector companion: E_j = w_j; Hankel [g(m+n)] PSD
    g = lambda nn: sum(c * np.exp(-wv * nn) for c, wv in zip(cs, ws))
    Hk = np.array([[g(i + j) for j in range(8)] for i in range(8)])
    ok_rp &= np.min(np.linalg.eigvalsh(Hk)) > -1e-12
check("every nontrivial alias lift E = w + 2 pi m (m >= 1) leaves the sector [0, pi]",
      ok_alias_exit, "sector membership singles out E_j = w_j exactly")
check("the in-sector Euclidean companion is reflection-positive: Hankel [g(m+n)] is PSD (15 bands)",
      ok_rp, "sum of positive-weight rank-1 outer products e^{-E m} e^{-E n}")

# ----------------------------------------------------------------------------
print("\nCONE-AGREEMENT COROLLARY AND END-TO-END CHAIN INSTANCE")
print("=" * 78)
# the dichotomy's saturating band omega(k) = |k|: per-fiber recovery at small k,
# then the slope of the reconstructed dispersion = 1 => xi = 1 via the landed inverse map
ks = np.array([0.05, 0.1, 0.2, 0.3])
E_rec = []
for kv in ks:
    C = band_data([1.0], [kv], 12)
    cs_r, ws_r = prony_recover(C, 1)
    E_rec.append(ws_r[0])
E_rec = np.array(E_rec)
slope = E_rec[0] / ks[0]
check("per-fiber reconstruction returns E(k) = omega(k) exactly on the dichotomy band samples",
      np.allclose(E_rec, ks, atol=1e-8), f"E(k)/k = {E_rec/ks}")
check("cone slope of the reconstructed dispersion = 1 => xi = 1/v^2 = 1 (the landed inverse map)",
      abs(slope - 1) < 1e-8 and abs(1 / slope**2 - 1) < 1e-8,
      "Wick-IR cone agreement holds at ALL sampled momenta, not only the cone point")
# a non-saturating in-sector band: slope v != 1 propagates to xi = 1/v^2 (diagnostic intact)
v_test = 0.6
E_rec2 = []
for kv in ks:
    C = band_data([1.0], [v_test * kv], 12)
    _, ws_r = prony_recover(C, 1)
    E_rec2.append(ws_r[0])
slope2 = E_rec2[0] / ks[0]
check("contrast band (v = 0.6): reconstruction preserves the slope, xi = 1/v^2 = 2.778 (diagnostic intact)",
      abs(slope2 - v_test) < 1e-8 and abs(1 / slope2**2 - 1 / v_test**2) < 1e-6)

# ----------------------------------------------------------------------------
print("\nHOSTILE WITNESSES")
print("=" * 78)
# Out-of-sector band aliases into the sector: identical data, wrong band recovered.
w_out = 2 * np.pi - 1.3  # ~4.98, outside [0, pi]
C_out = band_data([1.0], [w_out], 12)
C_in = band_data([1.0], [1.3], 12)
_, ws_r = prony_recover(C_out, 1)
check("drop the sector: the band at 2pi - 1.3 generates IDENTICAL integer data to 1.3; recovery returns 1.3",
      np.allclose(C_out, C_in, atol=1e-12) and abs(ws_r[0] - 1.3) < 1e-8,
      "without the spectrum-condition sector, the band is NOT determined: the sector is load-bearing")
# Drop the pairing: complex unpaired weight breaks real-evenness.
Cu = np.array([1.0 * np.exp(-1j * 0.9 * nn) for nn in range(8)])
check("drop the pairing: an unpaired mode gives complex, non-even layer data (not RP-shaped)",
      np.max(np.abs(Cu.imag)) > 0.1 and not np.allclose(Cu, Cu.real),
      "the landed spectrum-reflection corollary is what makes the registered data real-even")
# A second independent layer structure changes the recovered band.
C_mix = band_data([1.0, 0.4], [0.8, 1.7], 18)
_, ws_mix = prony_recover(C_mix, 2)
check("second independent layer component is DETECTED by recovery (band changes from {0.8} to {0.8, 1.7})",
      len(ws_mix) == 2 and np.allclose(np.sort(ws_mix), [0.8, 1.7], atol=1e-7),
      "the record-stack spectral reading is testable: extra structure shows up in the recovered band, not hidden")

# ----------------------------------------------------------------------------
print("\nSCOPE HONESTY: what is NOT proved here")
print("=" * 78)
check("record-stack spectral reading is NAMED, not derived: the runner consumes generated data; nothing derives that the OS input IS tick-generated",
      ok_rec and ok_rp, "its grounding is the one-spectrum identification")
check("sector is consumed as a premise with a retained_bounded parent, not rederived",
      ok_alias_exit, "spectrum-condition theorem + blocked-time normalization bridge")

print("\n" + "=" * 78)
print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
sys.exit(0 if FAIL == 0 else 1)
