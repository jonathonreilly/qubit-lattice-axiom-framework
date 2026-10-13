"""F2 common: constants, PREM density, and the R19-34 placeholder mapping m_g^2(rho).

Placeholder mapping (copied from P/scripts/C5/R19-34/r1934_sizes.py:4-5,22-27; canonical reading conditional, SM mapping ESTIMATE):
  m_g^2 a^2 = 16 pi n a^3 w |c| / 4,  a = l_P,  c = d2(dm)/dh2 = -0.040475 e^2 (R18-9 root, H-cov),
  w_N = 13 * (4/3) * g_s^2(0.3) = 5.2 per nucleon,  w_e = 0.1 per electron (Y_e = 0.5 used here; R19-34 used n_e = n_N).
Sign: c < 0 and <psibar psi> > 0 for ordinary matter AND for the hot plasma -> m_g^2 < 0 (tachyonic) in both
(R19-34 report :151 sign branch: m_f < 0 relative to W flips both to massive). We carry both branches:
  branch T (tachyonic, the computed sign) and branch M (massive, the sign branch).
Everything is expressed through the universal coefficient  mu_rho := |m_g^2| / rho  [eV^2 m^3 / kg]
(valid for non-relativistic matter where <psibar psi> ~ n).
"""
import numpy as np

hbarc = 1.973269804e-7      # eV m
hbar = 6.582119569e-16      # eV s
c_light = 2.99792458e8
G = 6.67430e-11
m_u = 1.66053907e-27        # kg
lP = 1.616e-35              # m   (as in r1934_sizes.py)
EP = 1.22089e28             # eV  (MP*1e9 in r1934_sizes.py)
Msun = 1.98892e30
pc = 3.0857e16
Mpc = 3.0857e22
yr = 3.15576e7

C_HCOV = -0.040475          # r1934_root.out (R18-9 root, H-cov E_g Hessian per e^2)
W_N = 13 * (4 / 3) * 0.3    # nucleon weight (r1934_sizes.py:25)
W_E = 0.1                   # electron weight (r1934_sizes.py:25)
Y_E = 0.5


def mg2_per_number(w, c=C_HCOV):
    """|m_g^2| [eV^2] per unit number density [m^-3] for weight w (R19-34 formula)."""
    return 16 * np.pi * lP**3 * w * abs(c) / 4 * EP**2


# coefficient per unit mass density for ordinary matter (nucleons + Y_e electrons)
MU_RHO_PLACEHOLDER = (mg2_per_number(W_N) + Y_E * mg2_per_number(W_E)) / m_u   # eV^2 m^3 / kg


def mg_of_rho(rho, mu_rho=MU_RHO_PLACEHOLDER):
    return np.sqrt(mu_rho * np.asarray(rho))


def ev_to_inv_m(E):
    return E / hbarc


# ---------------- PREM (Dziewonski & Anderson 1981, PEPI 25, 297), density in g/cc, x = r / 6371 km -------------
R_E = 6371.0e3
_PREM = [  # (r_top_km, coefficients a0..a3)
    (1221.5, (13.0885, 0.0, -8.8381, 0.0)),
    (3480.0, (12.5815, -1.2638, -3.6426, -5.5281)),
    (3630.0, (7.9565, -6.4761, 5.5283, -3.0807)),
    (5600.0, (7.9565, -6.4761, 5.5283, -3.0807)),
    (5701.0, (7.9565, -6.4761, 5.5283, -3.0807)),
    (5771.0, (5.3197, -1.4836, 0.0, 0.0)),
    (5971.0, (11.2494, -8.0298, 0.0, 0.0)),
    (6151.0, (7.1089, -3.8045, 0.0, 0.0)),
    (6291.0, (2.6910, 0.6924, 0.0, 0.0)),
    (6346.6, (2.6910, 0.6924, 0.0, 0.0)),
    (6356.0, (2.900, 0.0, 0.0, 0.0)),
    (6368.0, (2.600, 0.0, 0.0, 0.0)),
    (6371.0, (1.020, 0.0, 0.0, 0.0)),
]


def prem_rho(r_m, ocean=True):
    """PREM density in kg/m^3 at radius r [m]; 0 outside the Earth. ocean=False replaces the 3 km ocean by upper crust."""
    r_km = np.atleast_1d(np.asarray(r_m, dtype=float)) / 1e3
    out = np.zeros_like(r_km)
    x = r_km / 6371.0
    lo = 0.0
    for top, (a0, a1, a2, a3) in _PREM:
        sel = (r_km >= lo) & (r_km < top) if top < 6371.0 else (r_km >= lo) & (r_km <= top)
        val = a0 + a1 * x + a2 * x**2 + a3 * x**3
        if top == 6371.0 and not ocean:
            val = 2.600 + 0 * x
        out[sel] = val[sel]
        lo = top
    return out * 1e3


if __name__ == '__main__':
    print('placeholder mu_rho = |m_g^2|/rho = %.4e eV^2 m^3/kg' % MU_RHO_PLACEHOLDER)
    for lab, rho in (('Earth mean 5500', 5500.), ('rock 2600', 2600.), ('air 1.225', 1.225), ('core 13000', 13000.),
                     ('NS 5e17', 5e17), ('IGM n_b=0.25/m3', 0.25 * m_u), ('ISM 1/cc', 1e6 * m_u), ('Local Bubble 0.005/cc', 5e3 * m_u)):
        m = mg_of_rho(rho)
        print('  %-24s |m_g| = %.3e eV   1/|m_g| = %.3e m   growth/decay time = %.3e s' % (lab, m, hbarc / m, hbar / m))
    # R19-34 cross-check: Earth n = 3.3e30 /m^3 nucleons -> 2.343e-9 eV
    print('  check R19-34 Earth nucleons only (n=3.3e30): %.4e eV (r1934_sizes.out: 2.34e-09)' % np.sqrt(mg2_per_number(W_N) * 3.3e30))
    # PREM checks
    r = np.linspace(0, R_E, 2000001)
    rho = prem_rho(r)
    M = np.trapezoid(4 * np.pi * r**2 * rho, r)
    I = np.trapezoid(8 * np.pi / 3 * r**4 * rho, r)
    print('PREM: M = %.4e kg (5.972e24), I/MR^2 = %.4f (0.3307), rho_c = %.0f kg/m3' % (M, I / (M * R_E**2), rho[0]))
