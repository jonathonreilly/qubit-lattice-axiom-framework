#!/usr/bin/env python3
"""Precision check: the exact Brannen pair (r = 1/2, delta = 2/9) against
measured charged-lepton POLE masses.

WHAT THIS RUNNER CHECKS (class D comparator arithmetic; derives nothing)
------------------------------------------------------------------------
Several charged-lepton notes say the Brannen phase delta = 2/9 "fits within
1 sigma", or present the pair

    sqrt(m_k) = a * (1 + 2*sqrt(r)*cos(delta + 2*pi*k/3)),   r = 1/2,  delta = 2/9

as matching the measured masses.  That statement is true only for estimators
of delta that are limited by the tau-mass error (about 5e-5 relative).  It is
not true for the pair taken exactly.  The muon-to-electron ratio is known to
2e-8 relative precision, and the exact pair predicts

    m_mu / m_e  =  206.77032   against the PDG 2024 value  206.76828,

a relative miss of 9.8e-6, i.e. about 450 sigma.  The delta that fits
m_mu/m_e exactly at r = 1/2 is 2/9 - 1.75e-7.

So, with pole masses as the comparator, the exact pair is excluded.  Any exact
claim about (r, delta) must name its mass scheme and scale; leading-order QED
scheme conversions move Q by about 1e-3 and the muon/electron ratio by about
2e-2 (illustration in PART F only, not a scheme derivation).

WHAT THIS RUNNER DOES NOT DO
----------------------------
It does not derive r = 1/2 or delta = 2/9, does not dispute the closeness of
the pair (about 1e-5 in the ratio, unchanged), and does not decide which mass
scheme, if any, the pair could hold in.  The three mass sets below are external
comparator inputs: PDG 2024; the older set with CODATA-2014-era electron and
muon masses and m_tau = 1776.86 +- 0.12 MeV; and the mixed set of the
delta-eta chain runner (PDG 2024 electron and muon with m_tau = 1776.86 +-
0.12 MeV).

Check classes: [A] exact algebra (mpmath, 50 digits), [X] two-implementation
cross-check (mpmath vs numpy circulant eigenvalues), [D] external comparator.
Runtime: about a second.  Deterministic (no random numbers).
"""

from __future__ import annotations

import math

import mpmath as mp
import numpy as np

mp.mp.dps = 50

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> None:
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"  PASS: {name}" + (f" ({detail})" if detail else ""))
    else:
        FAIL += 1
        print(f"  FAIL: {name}" + (f" ({detail})" if detail else ""))


# ----------------------------------------------------------------------------
# Comparator inputs, MeV: (value, 1-sigma)
# ----------------------------------------------------------------------------
MASS_SETS = {
    "PDG2024": {
        "e": (mp.mpf("0.51099895000"), mp.mpf("0.00000000015")),
        "mu": (mp.mpf("105.6583755"), mp.mpf("0.0000023")),
        "tau": (mp.mpf("1776.93"), mp.mpf("0.09")),
    },
    # The older set the charged-lepton notes quote: electron and muon from
    # CODATA 2014 (PDG 2018 listings), and the tau line 1776.86 +- 0.12.
    "older(CODATA2014-e-mu)": {
        "e": (mp.mpf("0.5109989461"), mp.mpf("0.0000000031")),
        "mu": (mp.mpf("105.6583745"), mp.mpf("0.0000024")),
        "tau": (mp.mpf("1776.86"), mp.mpf("0.12")),
    },
    # The mixed set used by the delta-eta chain runner (frontier_koide_delta_eta_
    # density_readout_chain_2026_06_09.py): PDG 2024 electron and muon with the
    # older tau line.
    "PDG2024-e-mu+tau1776.86": {
        "e": (mp.mpf("0.51099895000"), mp.mpf("0.00000000015")),
        "mu": (mp.mpf("105.6583755"), mp.mpf("0.0000023")),
        "tau": (mp.mpf("1776.86"), mp.mpf("0.12")),
    },
}

TWO_NINTHS = mp.mpf(2) / 9
HALF = mp.mpf(1) / 2
# Species assignment at small positive delta: tau = k0, electron = k1, muon = k2.
K_TAU, K_E, K_MU = 0, 1, 2


def root(k: int, delta, r=HALF):
    """sqrt(m_k)/a for the Brannen form."""
    return 1 + 2 * mp.sqrt(r) * mp.cos(delta + 2 * mp.pi * k / 3)


def mass_factors(delta, r=HALF):
    """(f_e, f_mu, f_tau) with m_k = a^2 f_k."""
    return (root(K_E, delta, r) ** 2, root(K_MU, delta, r) ** 2, root(K_TAU, delta, r) ** 2)


def ratio_mu_e(delta, r=HALF):
    return (root(K_MU, delta, r) / root(K_E, delta, r)) ** 2


def koide_q(masses) -> mp.mpf:
    s = sum(masses)
    return s / sum(mp.sqrt(m) for m in masses) ** 2


def circulant_ratio_numpy(delta: float, r: float = 0.5) -> float:
    """Second implementation: eigenvalues of the 3x3 Hermitian circulant
    H = a I + b C + conj(b) C^2 with 2|b| = 2 sqrt(r) a, arg b = delta."""
    a = 1.0
    b = math.sqrt(r) * a * complex(math.cos(delta), math.sin(delta))
    c = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
    h = a * np.eye(3) + b * c + np.conj(b) * (c @ c)
    lam = np.linalg.eigvalsh(h)  # ascending: electron-like, muon-like, tau-like
    return float((lam[1] / lam[0]) ** 2)


def delta_from_triple(masses_e_mu_tau, r_free: bool = True):
    """delta from the three sqrt-masses.

    r_free=True: exact character projection, 3 masses -> (a, |b|, delta).
    r_free=False: assume r = 1/2 and use the tau normalised by the mean sqrt
    (the estimator of the open-gate note)."""
    me, mm, mt = masses_e_mu_tau
    v = {K_TAU: mp.sqrt(mt), K_E: mp.sqrt(me), K_MU: mp.sqrt(mm)}
    a = (v[0] + v[1] + v[2]) / 3
    if r_free:
        w = mp.e ** (2j * mp.pi / 3)
        b = sum(v[k] * w ** (-k) for k in range(3)) / 3
        return mp.arg(b), 2 * abs(b) / a
    x = (v[K_TAU] / a - 1) / mp.sqrt(2)
    return mp.acos(x), mp.sqrt(2)


def sigma_via_jacobian(func, mass_triple, sigmas):
    """Linear (Jacobian) propagation of the three mass errors, independent
    errors; returns (value, sigma, variance fractions from e, mu, tau)."""
    val = func(mass_triple)
    var = []
    for i in range(3):
        h = sigmas[i] / 1000
        up = [mass_triple[j] + (h if j == i else 0) for j in range(3)]
        dn = [mass_triple[j] - (h if j == i else 0) for j in range(3)]
        d = (func(up) - func(dn)) / (2 * h)
        var.append((d * sigmas[i]) ** 2)
    total = sum(var)
    return val, mp.sqrt(total), [v / total for v in var]


def chi2_fixed_shape(masses, sigmas, f):
    """chi^2 of m_k = s*f_k with the single scale s = a^2 free (closed form)."""
    num = sum(m * fk / sg ** 2 for m, fk, sg in zip(masses, f, sigmas))
    den = sum(fk ** 2 / sg ** 2 for fk, sg in zip(f, sigmas))
    s = num / den
    return sum(((m - s * fk) / sg) ** 2 for m, fk, sg in zip(masses, f, sigmas)), s


def min_chi2(masses, sigmas, delta=None, r=None):
    """chi^2 over the free parameters among (a^2 always, delta, r).  Golden
    section / bracketed scan in the single free shape parameter, exact in a^2."""
    if delta is not None and r is not None:
        return chi2_fixed_shape(masses, sigmas, mass_factors(delta, r))[0]
    if r is not None:  # delta free
        lo, hi = mp.mpf("0.15"), mp.mpf("0.30")
        var = lambda d: chi2_fixed_shape(masses, sigmas, mass_factors(d, r))[0]
    else:  # r free at fixed delta
        lo, hi = mp.mpf("0.40"), mp.mpf("0.60")
        var = lambda x: chi2_fixed_shape(masses, sigmas, mass_factors(delta, x))[0]
    g = (mp.sqrt(5) - 1) / 2
    c, d = hi - g * (hi - lo), lo + g * (hi - lo)
    fc, fd = var(c), var(d)
    for _ in range(200):
        if fc < fd:
            hi, d, fd = d, c, fc
            c = hi - g * (hi - lo)
            fc = var(c)
        else:
            lo, c, fc = c, d, fd
            d = lo + g * (hi - lo)
            fd = var(d)
    return min(fc, fd)


def main() -> int:
    print("Exact Brannen pair (r=1/2, delta=2/9) vs measured pole masses")
    print("=" * 72)

    # ---------------- PART A: exact algebra ----------------
    print("\nPART A: exact algebra [A]")
    # Signed roots, so the identity is checked for every delta including those
    # outside the positivity window (delta > pi/12 makes one root negative).
    qs = []
    for d in (mp.mpf(0), mp.mpf("0.1"), TWO_NINTHS, mp.mpf("0.7")):
        v = [root(k, d) for k in range(3)]
        qs.append(sum(x * x for x in v) / sum(v) ** 2)
    check("Q = sum v^2 / (sum v)^2 = 2/3 exactly at r = 1/2 for every delta (phase-blind)",
          all(abs(q - mp.mpf(2) / 3) < mp.mpf(10) ** -45 for q in qs))
    f_e, f_mu, f_tau = mass_factors(TWO_NINTHS)
    check("at delta = 2/9 the ordering is electron < muon < tau with k = 1, 2, 0",
          0 < f_e < f_mu < f_tau, f"f = ({float(f_e):.10f}, {float(f_mu):.10f}, {float(f_tau):.10f})")
    check("all three roots positive at delta = 2/9",
          all(root(k, TWO_NINTHS) > 0 for k in range(3)))

    # ---------------- PART B: two-implementation cross-check ----------------
    print("\nPART B: prediction of m_mu/m_e at the exact pair [A][X]")
    r_pred = ratio_mu_e(TWO_NINTHS)
    r_np = circulant_ratio_numpy(2.0 / 9.0)
    print(f"  m_mu/m_e (mpmath, exact pair)      = {mp.nstr(r_pred, 15)}")
    print(f"  m_mu/m_e (numpy circulant eigvals) = {r_np:.12f}")
    check("mpmath cosine form and numpy circulant eigenvalues agree",
          abs(float(r_pred) - r_np) < 1e-9, f"diff={abs(float(r_pred) - r_np):.2e}")
    check("exact-pair prediction is 206.77032 (to the digits quoted in the corrigenda)",
          mp.nstr(r_pred, 8) == "206.77032", mp.nstr(r_pred, 12))

    # ---------------- PART C: comparison with measured ratio ----------------
    print("\nPART C: m_mu/m_e, exact pair vs measurement [D]")
    zs = {}
    for label, ms in MASS_SETS.items():
        (me, sme), (mm, smm) = ms["e"], ms["mu"]
        r_obs = mm / me
        s_r = r_obs * mp.sqrt((sme / me) ** 2 + (smm / mm) ** 2)
        miss = r_pred - r_obs
        z = miss / s_r
        zs[label] = z
        print(f"  [{label}] m_mu/m_e = {mp.nstr(r_obs, 12)} +- {mp.nstr(s_r, 3)};"
              f" predicted - observed = {mp.nstr(miss, 5)};"
              f" relative {mp.nstr(miss / r_obs, 4)}; = {mp.nstr(z, 5)} sigma")
        check(f"[{label}] relative miss of m_mu/m_e is 9.8e-6",
              mp.mpf("9.7e-6") < miss / r_obs < mp.mpf("9.9e-6"), mp.nstr(miss / r_obs, 5))
        # Scale fixed by the electron alone (the reading behind the m_mu, m_tau
        # lines quoted in the delta-eta chain note's E4 comparator).
        m_mu_from_e = me * r_pred
        m_tau_from_e = me * mass_factors(TWO_NINTHS)[2] / mass_factors(TWO_NINTHS)[0]
        print(f"  [{label}] scale fixed by m_e: m_mu = {mp.nstr(m_mu_from_e, 9)} MeV,"
              f" m_tau = {mp.nstr(m_tau_from_e, 8)} MeV")
        check(f"[{label}] scale fixed by m_e gives m_mu = 105.6594 MeV (to the digits quoted in E4)",
              mp.nstr(m_mu_from_e, 7) == "105.6594", mp.nstr(m_mu_from_e, 9))
        check(f"[{label}] scale fixed by m_e gives m_tau = 1776.98 to 1776.99 MeV",
              mp.mpf("1776.975") < m_tau_from_e < mp.mpf("1776.995"), mp.nstr(m_tau_from_e, 8))
        check(f"[{label}] measured ratio is known to better than 3e-8 relative",
              s_r / r_obs < mp.mpf("3e-8"), mp.nstr(s_r / r_obs, 3))
        check(f"[{label}] the exact pair misses m_mu/m_e by more than 400 sigma",
              z > 400, mp.nstr(z, 5) + " sigma")

    # ---------------- PART D: the delta that fits, and estimator dependence ----------------
    print("\nPART D: delta estimators at r = 1/2 and the meaning of 'within 1 sigma' [D]")
    for label, ms in MASS_SETS.items():
        me, mm, mt = ms["e"][0], ms["mu"][0], ms["tau"][0]
        sig = [ms["e"][1], ms["mu"][1], ms["tau"][1]]
        triple = [me, mm, mt]
        print(f"  [{label}]")

        # Estimator 3: ratio estimator (r = 1/2, delta from m_mu/m_e)
        r_obs = mm / me
        d_ratio = mp.findroot(lambda d: ratio_mu_e(d) - r_obs, TWO_NINTHS)
        s_ratio = (ms["e"][1] / me) ** 2 + (ms["mu"][1] / mm) ** 2
        dr = (ratio_mu_e(TWO_NINTHS + mp.mpf("1e-15")) - ratio_mu_e(TWO_NINTHS - mp.mpf("1e-15"))) / mp.mpf("2e-15")
        sig_ratio = r_obs * mp.sqrt(s_ratio) / abs(dr)
        z_ratio = (d_ratio - TWO_NINTHS) / sig_ratio
        print(f"    ratio estimator (r=1/2): delta - 2/9 = {mp.nstr(d_ratio - TWO_NINTHS, 6)}"
              f" +- {mp.nstr(sig_ratio, 3)}  ({mp.nstr(z_ratio, 5)} sigma)")
        if label == "PDG2024":
            check("delta that fits m_mu/m_e exactly at r = 1/2 is 2/9 - 1.75e-7",
                  mp.mpf("-1.76e-7") < d_ratio - TWO_NINTHS < mp.mpf("-1.74e-7"),
                  mp.nstr(d_ratio - TWO_NINTHS, 6))

        # Estimator 1: tau-normalised, r = 1/2 assumed (open-gate note estimator)
        d1, s1, frac1 = sigma_via_jacobian(lambda t: delta_from_triple(t, r_free=False)[0], triple, sig)
        # Estimator 2: exact character projection, r free (circulant note estimator)
        d2, s2, frac2 = sigma_via_jacobian(lambda t: delta_from_triple(t, r_free=True)[0], triple, sig)
        z1, z2 = (d1 - TWO_NINTHS) / s1, (d2 - TWO_NINTHS) / s2
        print(f"    tau-normalised (r=1/2 assumed): delta - 2/9 = {mp.nstr(d1 - TWO_NINTHS, 4)}"
              f" +- {mp.nstr(s1, 3)}  ({mp.nstr(z1, 3)} sigma; tau share of variance {mp.nstr(frac1[2], 6)})")
        print(f"    character projection (r free):  delta - 2/9 = {mp.nstr(d2 - TWO_NINTHS, 4)}"
              f" +- {mp.nstr(s2, 3)}  ({mp.nstr(z2, 3)} sigma; tau share of variance {mp.nstr(frac2[2], 6)})")
        check(f"[{label}] tau-normalised estimator is within 1.5 sigma of 2/9 (the '1 sigma' statement)",
              abs(z1) < mp.mpf("1.5"), mp.nstr(z1, 3) + " sigma")
        check(f"[{label}] character-projection estimator is within 1.5 sigma of 2/9",
              abs(z2) < mp.mpf("1.5"), mp.nstr(z2, 3) + " sigma")
        # rho = 2|b|/a from the same projection; equipartition says sqrt(2)
        rho, s_rho, frac_rho = sigma_via_jacobian(lambda t: delta_from_triple(t, r_free=True)[1], triple, sig)
        z_rho = (rho - mp.sqrt(2)) / s_rho
        print(f"    character projection (r free):  rho - sqrt(2) = {mp.nstr(rho - mp.sqrt(2), 4)}"
              f" +- {mp.nstr(s_rho, 3)}  ({mp.nstr(z_rho, 3)} sigma; tau share of variance {mp.nstr(frac_rho[2], 6)})")
        check(f"[{label}] rho = 2|b|/a is within 1.5 sigma of sqrt(2) (tau-limited)",
              abs(z_rho) < mp.mpf("1.5") and frac_rho[2] > mp.mpf("0.999"),
              mp.nstr(z_rho, 3) + " sigma")
        check(f"[{label}] both tau-limited estimators get more than 99.9% of their variance from m_tau",
              frac1[2] > mp.mpf("0.999") and frac2[2] > mp.mpf("0.999"),
              f"{mp.nstr(frac1[2], 8)}, {mp.nstr(frac2[2], 8)}")
        check(f"[{label}] the ratio estimator is more than 1e4 times sharper than the tau-limited ones",
              s1 / sig_ratio > 1e4 and s2 / sig_ratio > 1e4,
              f"{mp.nstr(s1 / sig_ratio, 3)}x, {mp.nstr(s2 / sig_ratio, 3)}x")
        check(f"[{label}] the ratio estimator excludes 2/9 by more than 400 sigma",
              abs(z_ratio) > 400, mp.nstr(z_ratio, 5) + " sigma")

        # Independent path to the same delta: Koide-only tau from (m_e, m_mu),
        # then the character projection of that triple.
        se, sm = mp.sqrt(me), mp.sqrt(mm)
        # Q = 2/3  <=>  x^2 - 4(se+sm) x + (me + mm - 4 se sm)... solve (me+mm+x^2)*3 = 2(se+sm+x)^2
        # => x^2 - 4(se+sm) x + 3(me+mm) - 2(se+sm)^2 = 0 ; take the larger root.
        b_coef = -4 * (se + sm)
        c_coef = 3 * (me + mm) - 2 * (se + sm) ** 2
        x = (-b_coef + mp.sqrt(b_coef ** 2 - 4 * c_coef)) / 2
        m_tau_koide = x ** 2
        z_tau = (m_tau_koide - mt) / sig[2]
        d_kt, rho_kt = delta_from_triple([me, mm, m_tau_koide], r_free=True)
        print(f"    Koide-only m_tau from (m_e, m_mu) = {mp.nstr(m_tau_koide, 10)} MeV"
              f" ({mp.nstr(z_tau, 3)} sigma from the measured value)")
        check(f"[{label}] Koide-only tau prediction is within 1.5 sigma of the measured tau mass",
              abs(z_tau) < mp.mpf("1.5"), mp.nstr(z_tau, 3) + " sigma")
        check(f"[{label}] its rho = 2|b|/a is sqrt(2) to 1e-30 (Q = 2/3 exact)",
              abs(rho_kt - mp.sqrt(2)) < mp.mpf(10) ** -30)
        check(f"[{label}] second path to delta: projection of (m_e, m_mu, Koide tau) equals the ratio-fit delta",
              abs(d_kt - d_ratio) < mp.mpf(10) ** -25, mp.nstr(abs(d_kt - d_ratio), 3))

    # ---------------- PART E: joint and marginal chi-square ----------------
    print("\nPART E: joint test of the exact pair versus one-parameter marginals [D]")
    for label, ms in MASS_SETS.items():
        masses = [ms["e"][0], ms["mu"][0], ms["tau"][0]]
        sigmas = [ms["e"][1], ms["mu"][1], ms["tau"][1]]
        joint, s_fit = chi2_fixed_shape(masses, sigmas, mass_factors(TWO_NINTHS, HALF))
        chi_delta_free = min_chi2(masses, sigmas, r=HALF)          # delta free, 1 dof
        chi_r_free = min_chi2(masses, sigmas, delta=TWO_NINTHS)    # r free, 1 dof
        print(f"  [{label}] exact pair, scale free (2 dof): chi2 = {mp.nstr(joint, 4)}")
        print(f"  [{label}] r = 1/2, delta free (1 dof):    chi2 = {mp.nstr(chi_delta_free, 3)}")
        print(f"  [{label}] delta = 2/9, r free (1 dof):    chi2 = {mp.nstr(chi_r_free, 3)}")
        check(f"[{label}] exact pair joint chi2 (2 dof) exceeds 1e5",
              joint > 1e5, mp.nstr(joint, 4))
        # What stands: with the scale set to its chi^2 minimum the exact pair still
        # reproduces every mass to better than 1e-4 relative (3e-5 for PDG 2024).
        devs = [(s_fit * fk - m) / m for fk, m in zip(mass_factors(TWO_NINTHS, HALF), masses)]
        print(f"  [{label}] best-scale relative deviations (e, mu, tau) ="
              f" {', '.join(mp.nstr(d, 3) for d in devs)}")
        check(f"[{label}] with the scale fitted, each mass is reproduced to better than 1e-4 relative"
              " (closeness stands)",
              all(abs(d) < mp.mpf("1e-4") for d in devs),
              f"max |dev| = {mp.nstr(max(abs(d) for d in devs), 3)}")
        check(f"[{label}] r = 1/2 with delta free is acceptable (chi2 < 4 on 1 dof)",
              chi_delta_free < 4, mp.nstr(chi_delta_free, 3))
        check(f"[{label}] delta = 2/9 with r free is acceptable (chi2 < 4 on 1 dof)",
              chi_r_free < 4, mp.nstr(chi_r_free, 3))
    print("  reading: each number is compatible with the data given the other;"
          " the pair taken exactly is not.")

    # ---------------- PART F: scheme-shift illustration ----------------
    print("\nPART F: leading-order QED scheme illustration (fixed alpha) [D, illustration only]")
    ms = MASS_SETS["PDG2024"]
    pole = [ms["e"][0], ms["mu"][0], ms["tau"][0]]
    q_pole = koide_q(pole)
    print(f"  Q(pole) - 2/3 = {mp.nstr(q_pole - mp.mpf(2) / 3, 4)}")
    check("Q(pole) is 2/3 to better than 1e-5", abs(q_pole - mp.mpf(2) / 3) < mp.mpf("1e-5"),
          mp.nstr(q_pole - mp.mpf(2) / 3, 4))
    shifts = []
    for alpha in (mp.mpf(1) / mp.mpf("137.036"), mp.mpf(1) / 128):
        for mu in (mp.mpf("91187.6"), mp.mpf("1200"), mp.mpf("1e6")):
            conv = [m * (1 - alpha / mp.pi * (1 + mp.mpf(3) / 4 * mp.log(mu ** 2 / m ** 2))) for m in pole]
            dq = koide_q(conv) - q_pole
            ratio_shift = (conv[1] / conv[0]) / (pole[1] / pole[0]) - 1
            shifts.append((dq, ratio_shift))
            print(f"  alpha=1/{mp.nstr(1 / alpha, 6)}, mu={mp.nstr(mu, 6)} MeV:"
                  f" dQ = {mp.nstr(dq, 3)},  d(m_mu/m_e)/(m_mu/m_e) = {mp.nstr(ratio_shift, 3)}")
    check("leading-order pole -> MS-bar conversion moves Q by 1e-3 to 2e-3 in all six cases",
          all(mp.mpf("1e-3") < dq < mp.mpf("2e-3") for dq, _ in shifts),
          f"range {mp.nstr(min(s[0] for s in shifts), 3)} .. {mp.nstr(max(s[0] for s in shifts), 3)}")
    check("that shift is at least 100 times |Q(pole) - 2/3|",
          all(dq > 100 * abs(q_pole - mp.mpf(2) / 3) for dq, _ in shifts))
    check("the conversion moves m_mu/m_e by more than 1e-3 (>100 times the 9.8e-6 pole-mass miss)",
          all(abs(rs) > mp.mpf("1e-3") for _, rs in shifts),
          f"smallest |shift| = {mp.nstr(min(abs(s[1]) for s in shifts), 3)}")
    print("  reading: an exact (r, delta) statement is scheme-dependent at the 1e-3 to 1e-2 level;"
          " at pole masses it is excluded, elsewhere it needs the scheme and scale named.")

    print("\n" + "=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: exact-pair pole-mass precision check failed.")
        return 1
    print(
        "VERDICT: the exact pair (r=1/2, delta=2/9) misses the measured pole-mass "
        "m_mu/m_e by 9.8e-6 (about 450 sigma); the '1 sigma' statements hold only for "
        "tau-limited estimators of delta; closeness (1e-5 in m_mu/m_e, better than 1e-4 "
        "per mass with the scale fitted) is unchanged; derivation of r and delta remains open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
