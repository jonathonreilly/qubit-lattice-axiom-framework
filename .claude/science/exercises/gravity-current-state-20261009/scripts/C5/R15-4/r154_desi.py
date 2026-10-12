"""R15-4 (c): the linear reader on DESI-like evolving w.

Units: rho in units of the critical density today (3H0^2/kappa = 1); u = ln a; Omega_m = 0.31 (stated; radiation
neglected at z < 3). DESI DR2 w0wa (arXiv:2503.14738 v3, Table 5 / Eqs. 25-28, fetched this run):
   DESI+CMB (-0.42, -1.75); +Pantheon+ (-0.838, -0.62); +Union3 (-0.667, -1.09); +DESY5 (-0.752, -0.86).
CPL: w(a) = w0 + wa(1-a);  rho_DE(a) = Om_DE a^{-3(1+w0+wa)} exp(-3 wa (1-a))  (-> 0 as a -> 0 for all four).
Reader (r154_reader.py): y_j' = E - beta_j y_j, rho_hat = sum k_j y_j, E = -d rho/du; linear, so matter is read
exactly and rho_hat_tot = rho_m + R[rho_DE].
(c0) constant w: rho_hat/rho = G(3(1+w)); compared with the positivity bound x(4-x)/3 (r154_nogo.py).
(c1) TRACKING: the true DE is the DESI CPL. Reported: R[rho_DE]/rho_DE(z); w_eff(z) := -1 - (1/3) dln R[rho_DE]/du
     against w(z); and, after the one unobservable renormalisation A (A R[rho_DE](0) = rho_DE(0), keeps H0 and
     flatness), the distortion dH/H(z) and dD_M/D_M(z) at DESI DR2 effective redshifts.
(c2) INVERSE: the true enthalpy history E_true(u) whose reading is exactly the DESI CPL density (effective DE).
     E_true = (T' + sum k_j beta_j y_j)/K(0), K(0) = sum k_j. E_true >= 0 everywhere <=> the true DE never violates
     the NEC (w_true >= -1), whatever its unobservable constant part.
Subtraction rule: Lt := rho_hat - rho_nc with rho_nc = rho_m + rho_DE (the CPL has no constant part); nothing else.
"""
import numpy as np
from scipy.integrate import solve_ivp, quad
import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from r154_reader import DESIGNS, G

Om = 0.31
Ode = 1 - Om
SETS = {'DESI+CMB': (-0.42, -1.75), 'DESI+CMB+Pantheon+': (-0.838, -0.62),
        'DESI+CMB+Union3': (-0.667, -1.09), 'DESI+CMB+DESY5': (-0.752, -0.86)}
ZD = [0.295, 0.51, 0.706, 0.934, 1.321, 1.484, 2.33]   # DESI DR2 effective redshifts (RECALLED)


def rde(u, w0, wa):
    a = np.exp(u)
    return Ode * a ** (-3 * (1 + w0 + wa)) * np.exp(-3 * wa * (1 - a))


def wcpl(u, w0, wa):
    return w0 + wa * (1 - np.exp(u))


def read(Efun, b, k, u0=-12.0, u1=0.0):
    us = np.linspace(u0, u1, 24001)
    sol = solve_ivp(lambda u, y: Efun(u) - b * y, (u0, u1), np.zeros(len(b)), t_eval=us, rtol=1e-11, atol=1e-16,
                    method='DOP853', max_step=0.01)
    y = sol.y
    rh = k @ y
    drh = k.sum() * np.array([Efun(u) for u in us]) - (k * b) @ y
    return us, rh, drh


def DM(zs, Hfun):
    return np.array([quad(lambda z: 1 / Hfun(z), 0, zz, epsrel=1e-10)[0] for zz in zs])


if __name__ == '__main__':
    print('# (c0) constant-w DE: rho_hat/rho = G(x), x = 3(1+w); positivity bound for dust-exact positive readers: x(4-x)/3')
    for w in (-0.99, -0.95, -0.9, -0.8, -0.75, -0.7, -0.5):
        x = 3 * (1 + w)
        print(f'   w={w:+.2f} (x={x:.2f}): ' + ', '.join(f'{n.split()[0]} G={G(x, *DESIGNS[n]):.4f}' for n in DESIGNS)
              + f'; bound x(4-x)/3 = {x*(4-x)/3:.4f}')

    for name in ('D1 minimal (2 regs)', 'R* fast (2 regs, beta 20,24)', 'D3 flat x in [0.15,4.5]'):
        b, k = DESIGNS[name]
        print(f'\n# reader {name}: K(0)={k.sum():+.4f}')
        for sname, (w0, wa) in SETS.items():
            E = lambda u: 3 * (1 + wcpl(u, w0, wa)) * rde(u, w0, wa)
            us, rh, drh = read(E, b, k)
            rd = rde(us, w0, wa)
            weff = -1 - drh / rh / 3
            sel = lambda z: np.searchsorted(us, -np.log1p(z))
            print(f' [{sname}] w0={w0}, wa={wa}')
            print('   (c1) R[rho_DE]/rho_DE: ' + ', '.join(f'z={z}: {rh[sel(z)]/rd[sel(z)]:+.3f}' for z in (0, 0.5, 1, 2, 3)))
            print('        w_eff (model) vs w_CPL: ' + ', '.join(f'z={z}: {weff[sel(z)]:+.3f}/{wcpl(us[sel(z)], w0, wa):+.3f}' for z in (0, 0.5, 1, 2)))
            print(f'        min over z<3 of rho_hat_tot = Om a^-3 + R[rho_DE]: {np.min((Om*np.exp(-3*us)+rh)[us > -np.log(4)]):+.4f} (>0 means H^2>0)')
            # Lt in units of 3H0^2/kappa, raw (no renormalisation)
            Lt0 = rh[-1] - rd[-1]
            A = rd[-1] / rh[-1]
            H_true = lambda z: np.sqrt(Om * (1 + z) ** 3 + rde(-np.log1p(z), w0, wa))
            H_mod = lambda z: np.sqrt(Om * (1 + z) ** 3 + A * np.interp(-np.log1p(z), us, rh))
            dH = [H_mod(z) / H_true(z) - 1 for z in ZD]
            dDM = DM(ZD, H_mod) / DM(ZD, H_true) - 1
            print(f'        raw Lt(z=0) = {Lt0:+.4f} (units 3H0^2/kappa; Lambda_obs ~ {Ode:.2f}); renormalisation A = {A:.4f} (unobservable amplitude)')
            print('        after A: dH/H at DESI z: ' + ', '.join(f'{z}:{d:+.3%}' for z, d in zip(ZD, dH)))
            print('                 dD_M/D_M     : ' + ', '.join(f'{z}:{d:+.3%}' for z, d in zip(ZD, dDM)))
            # (c2) inverse problem
            K0 = k.sum()
            T = lambda u: rde(u, w0, wa)
            Tp = lambda u: -3 * (1 + wcpl(u, w0, wa)) * rde(u, w0, wa)
            u0 = -12.0
            usI = np.linspace(u0, 0, 24001)
            solI = solve_ivp(lambda u, y: (Tp(u) + (k * b) @ y) / K0 - b * y, (u0, 0), np.zeros(len(b)), t_eval=usI,
                             rtol=1e-11, atol=1e-18, method='DOP853', max_step=0.01)
            yI = solI.y
            Etrue = (np.array([Tp(u) for u in usI]) + (k * b) @ yI) / K0
            chk = np.max(np.abs(k @ yI - np.array([T(u) for u in usI]))) / Ode
            m = usI > -np.log(4)
            print(f'   (c2) inverse: max|R[E_true] - rho_CPL|/Om_DE = {chk:.1e}; E_true over z<3: min={Etrue[m].min():+.4f}, '
                  f'max={Etrue[m].max():+.4f}; E_true at z=0,0.5,1,2: ' + ', '.join(f'{Etrue[np.searchsorted(usI, -np.log1p(z))]:+.4f}' for z in (0, 0.5, 1, 2)))
            gH2 = -(Etrue - 3 * (1 + wcpl(usI, w0, wa)) * rde(usI, w0, wa)) / (Om * np.exp(-3 * usI) + rde(usI, w0, wa))
            print('        g/H^2 = -(E_true - E_CPL)/rho_tot at z=0,0.5,1,2: ' + ', '.join(f'{gH2[np.searchsorted(usI, -np.log1p(z))]:+.3f}' for z in (0, 0.5, 1, 2)))
            gH2c = -(drh + np.array([E(u) for u in us])) / (Om * np.exp(-3 * us) + rh)
            print('        (c1 picture) g/H^2 at z=0,0.5,1,2: ' + ', '.join(f'{gH2c[sel(z)]:+.3f}' for z in (0, 0.5, 1, 2)))
            print(f'        E_true >= 0 for all z (true DE NEC-respecting, w_true >= -1)? {bool(np.all(Etrue >= -1e-12))};'
                  f' true DE decrease since z=3: int E_true du = {np.trapezoid(Etrue[m], usI[m]):.4f} (rho_c0)')
