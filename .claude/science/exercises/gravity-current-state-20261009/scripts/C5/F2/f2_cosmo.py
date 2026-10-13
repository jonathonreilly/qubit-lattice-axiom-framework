"""F2 case (iv): cosmology. Tensor modes with m_g^2(T) = A(T) H^2 through the hot era and today.

(a) Placeholder A(T): R19-34 mapping (r1934_sizes.py:10-21, quarks t,b,c only) reproduced; extended to 150 GeV -> 1 MeV with
    u,d,s (T > 0.155 GeV), leptons (weight e^2 = 0.1), thermal nucleons + baryon asymmetry below 0.155 GeV (weight 5.2).
    Hadronic (pion) scalar densities are NOT included (partial below T_QCD; stated).
(b) Branch T (tachyonic): growth exponent N = int |m_g| dt = int sqrt|A| dlnT  (radiation era; k -> 0 modes; superhorizon modes
    grow as t^p, p = (-1/2 + sqrt(1/4 + A))/2 -> same exponent for A >> 1).
(c) Observational ceiling on N from Delta N_eff < 0.3 (Planck 2018 + BBN; Omega_GW h^2 < 1.6e-6): irreducible seed = graviton
    vacuum in the tachyonic band p < |m_g|, rho_seed = |m_g|^4/(8 pi^2); require e^{2N} rho_seed < f_GW rho_rad, f_GW = 0.04.
(d) Today (branch T): cosmic-mean baryons |m_g| vs H0; ceiling |m_g| <= N_max H0.
(e) Branch M: superhorizon damping a^{-3/2} while |m_g| > H -> primordial tensors erased (no current bound).
"""
import numpy as np
from f2_common import MU_RHO_PLACEHOLDER, hbar, m_u

MP = 1.22089e19; gs2 = 0.3; c = -0.040475
TQCD = 0.155


def gstar(T):
    for Tc, g in ((173., 106.75), (80., 96.25), (4.2, 86.25), (1.3, 75.75), (0.2, 61.75), (0.1, 17.25), (5e-4, 10.75)):
        if T > Tc:
            return g
    return 3.36


def Ha2(T, g=None):
    g = gstar(T) if g is None else g
    return (8 * np.pi / 3) * (np.pi**2 / 30) * g * (T / MP)**4


def ppbar(m, T):
    k = np.linspace(1e-6 * T, 60 * T + 10 * m, 200001); E = np.sqrt(k * k + m * m)
    return 4 * np.trapezoid(k * k / (2 * np.pi**2) * m / E / (np.exp(np.minimum(E / T, 700)) + 1), k)


quarks_heavy = {'t': 172.69, 'b': 4.18, 'c': 1.27}
quarks_light = {'s': 0.093, 'd': 0.0047, 'u': 0.0022}
leptons = {'tau': 1.777, 'mu': 0.10566, 'e': 0.000511}


def mu_lattice(T, extended=True):
    mu = sum(3 * ppbar(m, T) / MP**3 * (4 / 3) * gs2 * c / 4 for m in quarks_heavy.values())
    if extended:
        if T > TQCD:
            mu += sum(3 * ppbar(m, T) / MP**3 * (4 / 3) * gs2 * c / 4 for m in quarks_light.values())
        else:
            wN = 13 * (4 / 3) * gs2
            nB = 6.1e-10 * 2 * 1.2020569 / np.pi**2 * T**3
            mu += (2 * ppbar(0.939, T) + nB) / MP**3 * wN * c / 4
        mu += sum(ppbar(m, T) / MP**3 * 0.1 * c / 4 for m in leptons.values())
    return mu


if __name__ == '__main__':
    print('=== (a) placeholder A(T) = m_g^2/H^2 ===')
    print('  reproduction of r1934_sizes.out (t,b,c only, g* = 106.75 above 90 GeV else 86.25):')
    for T in (150., 100., 50., 10., 1.):
        g = 106.75 if T > 90 else 86.25
        print('    T = %6.1f GeV: m_g^2/H^2 = %+.3e' % (T, 16 * np.pi * mu_lattice(T, extended=False) / Ha2(T, g)))
    Ts = np.geomspace(150., 1e-3, 241)
    A = np.array([16 * np.pi * mu_lattice(T) / Ha2(T) for T in Ts])
    print('  extended (this run; g* steps; hadrons partial below 0.155 GeV):')
    for T in (150., 100., 10., 1., 0.2, 0.1, 0.01, 0.001):
        i = np.argmin(abs(Ts - T))
        print('    T = %8.4f GeV: A = %+.3e   |m_g|/H = %.3e' % (Ts[i], A[i], np.sqrt(abs(A[i]))))

    print('\n=== (b) branch T growth exponent N = int sqrt|A| dlnT ===')
    lnT = np.log(Ts)
    sq = np.sqrt(np.abs(A))
    Ncum = np.concatenate([[0], np.cumsum(0.5 * (sq[1:] + sq[:-1]) * (lnT[:-1] - lnT[1:]))])
    for T in (100., 10., 1., 0.1, 0.01, 0.001):
        i = np.argmin(abs(Ts - T))
        print('    from 150 GeV to %8.4f GeV: N = %.3e e-folds of tensor amplitude' % (Ts[i], Ncum[i]))
    print('    (superhorizon check at A = 3e13: p = %.4e vs sqrt(A)/2 = %.4e per ln t)'
          % ((-0.5 + np.sqrt(0.25 + 3e13)) / 2, np.sqrt(3e13) / 2))

    print('\n=== (c) ceiling from Delta N_eff (vacuum seed) ===')
    fGW = 0.04

    def Nmax(T, Aval):
        g = gstar(T)
        H = np.sqrt(Ha2(T)) * MP
        M = np.sqrt(Aval) * H
        rho_rad = np.pi**2 / 30 * g * T**4
        return 0.5 * np.log(fGW * rho_rad * 8 * np.pi**2 / M**4)

    for T in (150., 1., 1e-3):
        for span, lab in ((1.0, 'one e-fold'), (np.log(150. / 1e-3), 'whole 150 GeV->1 MeV')):
            a = 1.0
            for _ in range(200):
                a = (Nmax(T, a) / span)**2
            print('    T = %7.3f GeV, %-22s: N_max = %.1f -> |A| <= %.2e  (|m_g|/H <= %.1f)' % (T, lab, Nmax(T, a), a, np.sqrt(a)))
    print('    placeholder N over the era = %.2e  vs N_max ~ 50-100 -> excess factor in sqrt|A| ~ %.1e, in |A| ~ %.1e'
          % (Ncum[-1], Ncum[-1] / 80, (Ncum[-1] / 80)**2))

    print('\n=== (d) today, branch T: cosmic-mean baryons ===')
    H0 = 67.4 * 1e3 / 3.0857e22 * hbar
    rho_b = 0.0493 * 3 * (67.4e3 / 3.0857e22)**2 / (8 * np.pi * 6.67430e-11)
    mg = np.sqrt(MU_RHO_PLACEHOLDER * rho_b)
    print('    rho_b = %.3e kg/m3 (n_b = %.3f /m3); placeholder |m_g| = %.3e eV; H0 = %.3e eV; |m_g|/H0 = %.3e' % (
        rho_b, rho_b / m_u, mg, H0, mg / H0))
    print('    e-fold time 1/|m_g| = %.2e s = %.1f yr; matter era |m_g|/H ~ const ~ %.1e' % (hbar / mg, hbar / mg / 3.156e7, mg / H0 / np.sqrt(0.315)))
    Nm = 100.
    mu_bound = (Nm * H0)**2 / rho_b
    print('    ceiling |m_g(rho_b)| <= N_max H0 (N_max ~ 100): %.2e eV  -> mu_rho <= %.2e eV^2 m^3/kg ; placeholder/bound = %.1e'
          % (Nm * H0, mu_bound, MU_RHO_PLACEHOLDER / mu_bound))

    print('\n=== (e) branch M: superhorizon tensor damping ===')
    T0 = 2.35e-13
    lna = np.log(150. / T0)
    print('    placeholder |m_g| > H from 150 GeV to today: ln(a0/a) ~ %.1f -> amplitude factor ~ e^-%.0f' % (lna, 1.5 * lna))
    print('    -> primordial tensors erased; r ~ 0, consistent with r_0.05 < 0.036 (BICEP/Keck 2021). No current bound on branch M.')
