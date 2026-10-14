#!/usr/bin/env python3
"""Independent finite checks; no author helpers imported and no data fitted."""
import os
for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import datetime
import json
import math
import platform
import time
from pathlib import Path
import mpmath as mp
import numpy as np
import scipy
import sympy as sp
from scipy.integrate import quad

mp.mp.dps = 60
checks = []


def check(name, condition, evidence):
    checks.append({'name': name, 'passed': bool(condition), 'evidence': evidence})
    print(('PASS ' if condition else 'FAIL ') + name, flush=True)


def angular_force(mu, r, u):
    """r^2 times the actual Yukawa point-force projection averaged on a shell."""
    def integrand(z):
        d = mp.sqrt(r*r + u*u - 2*r*u*z)
        return r*r*(r-u*z)*(1+mu*d)*mp.exp(-mu*d)/(2*d**3)
    return mp.quad(integrand, [-1, 0, 1])


def shell_formula(mu, r, u):
    z = mu*u
    form = mp.sinh(z)/z if z else mp.mpf(1)
    return (1+mu*r)*mp.exp(-mu*r)*form


def angular_checks():
    errors = []
    for mu in map(mp.mpf, ('0', '.2', '1.7', '10')):
        for u in map(mp.mpf, ('0', '.4', '1')):
            for r in map(mp.mpf, ('1.2', '2.3')):
                errors.append(abs(angular_force(mu, r, u)-shell_formula(mu, r, u)))
    check('direct_angular_force_normalization', max(errors) < mp.mpf('1e-50'),
          {'samples': len(errors), 'max_absolute_error': mp.nstr(max(errors), 20)})

    cm = [(mp.mpf(x), mp.mpf(w)) for x, w in [('0', '.2'), ('.2', '.3'), ('.4', '.5')]]
    mm = [(mp.mpf(x), mp.mpf(w)) for x, w in [('.4', '.1'), ('.65', '.4'), ('1', '.5')]]
    nu = [(mp.mpf(x), mp.mpf(w)) for x, w in [('0', '.15'), ('.3', '.4'), ('2', '.45')]]
    radii = list(map(mp.mpf, ('1.2', '2.3')))

    def kernel(profile, spectral, r):
        return sum(wp*wm*angular_force(mu, r, u)
                   for u, wp in profile for mu, wm in spectral)

    matrix = mp.matrix([[kernel(cm, nu, r), kernel(mm, nu, r)] for r in radii])
    determinant = mp.det(matrix)
    ratios = [matrix[i, 0]/matrix[i, 1] for i in (0, 1)]
    controls = {}
    for name, core, mantle, measure, rr in [
        ('one_mass', cm, mm, [(mp.mpf('.3'), mp.mpf(1))], radii),
        ('equal_profile', cm, cm, nu, radii),
        ('coincident_radius', cm, mm, nu, [radii[0], radii[0]])]:
        controls[name] = mp.det(mp.matrix([[kernel(core, measure, r), kernel(mantle, measure, r)] for r in rr]))
    check('ordered_discrete_profiles_and_degeneracies', determinant < 0 and ratios[1] > ratios[0]
          and all(abs(v) < mp.mpf('1e-50') for v in controls.values()),
          {'determinant': mp.nstr(determinant, 20), 'ratios': list(map(lambda x: mp.nstr(x, 20), ratios)),
           'degenerate_determinants': {k: mp.nstr(v, 20) for k, v in controls.items()}})

    fc, fm = mp.mpf('.27'), mp.mpf('.73')
    response = matrix*mp.diag([fc, fm])
    truth = mp.matrix([mp.mpf('-.8'), mp.mpf('.35')])
    observed = response*truth
    # LU solution independently checks the source reconstruction and column units.
    inverse = mp.lu_solve(response, observed)
    cramer = mp.matrix([(observed[0]*matrix[1, 1]-observed[1]*matrix[0, 1])/(fc*determinant),
                       (matrix[0, 0]*observed[1]-matrix[1, 0]*observed[0])/(fm*determinant)])
    check('source_charge_inverse_direct_force', mp.norm(inverse-truth) < mp.mpf('1e-50')
          and mp.norm(cramer-inverse) < mp.mpf('1e-50'),
          {'lu_error': mp.nstr(mp.norm(inverse-truth), 20),
           'cramer_to_lu_error': mp.nstr(mp.norm(cramer-inverse), 20)})


def symbolic_checks():
    eps, x, r1, r2, c2, m2, c4, m4, v2, v3, v4 = sp.symbols('eps x r1 r2 c2 m2 c4 m4 v2 v3 v4')
    def kernel(a2, a4, r):
        raw = sp.series((1+a2*(eps*x)**2/6+a4*(eps*x)**4/120)
                        *(1+r*eps*x)*sp.exp(-r*eps*x), eps, 0, 5).removeO().expand()
        # Replace exact monomials simultaneously. Sequential subs(x**2, v2)
        # would incorrectly turn x**4 into v2**2 before taking its moment.
        return raw.xreplace({x**4: v4, x**3: v3, x**2: v2})
    det = sp.series(kernel(c2,c4,r1)*kernel(m2,m4,r2)
                    -kernel(c2,c4,r2)*kernel(m2,m4,r1), eps, 0, 5).removeO().expand()
    coeff = sp.factor(det.coeff(eps, 4))
    target = -(m2-c2)*(r2*r2-r1*r1)*(v4-v2*v2)/12
    s = sp.symbols('s', positive=True)
    variance = sp.prod(s+i for i in range(4))-(s*(s+1))**2
    check('symbolic_small_mass_determinant', sp.simplify(coeff-target) == 0
          and all(sp.simplify(det.coeff(eps, n)) == 0 for n in range(4))
          and sp.simplify(variance-2*s*(s+1)*(2*s+3)) == 0,
          {'coefficient_epsilon4': str(coeff), 'gamma_variance_numerator': str(sp.factor(variance))})
    t, xx = sp.symbols('t xx', nonnegative=True)
    formulas = []
    for n in range(1, 6):
        direct = sp.diff((1+t*xx)*sp.exp(-t*xx), xx, 2*n)
        expected = t**(2*n)*(t*xx-(2*n-1))*sp.exp(-t*xx)
        formulas.append(sp.simplify(direct-expected) == 0)
    # Exact n=s=1 force errors change sign, unlike potential errors.
    errors = [(1+2*tt)/(1+tt)**2-(1+tt)*math.exp(-tt) for tt in (.1, 10.)]
    check('force_remainder_absolute_not_one_sided', all(formulas) and errors[0] < 0 < errors[1],
          {'orders_symbolically_checked': 5, 'force_errors_at_0p1_and_10': errors})


def noise_and_bins():
    a = .37
    direct, err = quad(lambda k: k*math.exp(-a*a*k*k)/(4*math.pi**2), 0, np.inf,
                       epsabs=1e-13, epsrel=1e-13)
    exact = 1/(8*math.pi**2*a*a)
    check('massless_gaussian_vacuum_normalization', abs(direct-exact) < 1e-13,
          {'momentum_integral': direct, 'analytic': exact, 'quadrature_error_estimate': err})

    M, h, R, Omega = 4., .25, 2., 4.
    masses = np.array([0., h-1e-10, h+1e-10, 1.-1e-10, 1.+1e-10, M, M+1e-10, 100*M])
    weights = np.array([.07, .13, .11, .09, .16, .14, .12, .18])
    midpoints = np.where(masses <= M, (np.minimum(np.floor(masses/h), M/h-1)+.5)*h, M+1)
    tail = weights[masses>M].sum()
    def y(mu, r): return np.exp(-r*mu)
    def f(mu, r): return (1+r*mu)*np.exp(-r*mu)
    def j(mu, omega):
        k = np.sqrt(np.maximum(0., omega*omega-mu*mu))
        return k*np.exp(-a*a*k*k)/(4*math.pi**2)
    relative_to_bound = {'Y': [], 'H': [], 'j': []}
    for r in (0., .01, .5, R):
        relative_to_bound['Y'].append(abs(weights @ (y(masses,r)-y(midpoints,r)))/(R*h/2+tail))
        relative_to_bound['H'].append(abs(weights @ (f(masses,r)-f(midpoints,r)))/(R*h/(2*math.e)+tail))
    for omega in (0., .01, h, 1., 2., M):
        relative_to_bound['j'].append(abs(weights @ (j(masses,omega)-j(midpoints,omega)))/(math.sqrt(Omega*h)/(4*math.pi**2)))
    check('atomic_bin_boundary_and_threshold_controls', all(max(v) <= 1+1e-13 for v in relative_to_bound.values()),
          {'max_error_divided_by_bound': {k: max(v) for k,v in relative_to_bound.items()},
           'mass_at_cap_and_zero': True, 'tail_atom': M+1})

    # rho(mu)=(1+mu)^-2 has total one and infinite first moment; any tail atom suffices.
    edges = np.linspace(0., M, 17)
    mid = np.r_[(edges[:-1]+edges[1:])/2, M+1]
    w = np.r_[np.diff(edges/(1+edges)), 1/(1+M)]
    p = w[-1]
    ratios = {'Y': [], 'H': [], 'j': []}
    for r in (0., .01, .5, R):
        ey = 1. if r == 0 else quad(lambda mu: math.exp(-r*mu)/(1+mu)**2, 0, np.inf, epsabs=2e-12)[0]
        ef = 1. if r == 0 else quad(lambda mu: (1+r*mu)*math.exp(-r*mu)/(1+mu)**2, 0, np.inf, epsabs=2e-12)[0]
        ratios['Y'].append(abs(ey-w@y(mid,r))/(R*h/2+p))
        ratios['H'].append(abs(ef-w@f(mid,r))/(R*h/(2*math.e)+p))
    for omega in (.01, .25, 1., M):
        ej = quad(lambda mu: float(j(mu,omega))/(1+mu)**2, 0, omega, epsabs=2e-12)[0]
        ratios['j'].append(abs(ej-w@j(mid,omega))/(math.sqrt(Omega*h)/(4*math.pi**2)))
    check('infinite_first_moment_bin_construction', all(max(v) <= 1+1e-11 for v in ratios.values()),
          {'measure': 'density (1+mu)^-2, mu>=0', 'tail_mass': p,
           'max_error_divided_by_bound': {k: max(v) for k,v in ratios.items()}})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    angular_checks()
    symbolic_checks()
    noise_and_bins()
    result = {'scope': 'independent finite diagnostic checks; no author helpers; no empirical fit',
              'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'versions': {'python': platform.python_version(), 'numpy': np.__version__,
                           'scipy': scipy.__version__, 'mpmath': mp.__version__, 'sympy': sp.__version__},
              'mpmath_decimal_precision': mp.mp.dps, 'checks': checks,
              'elapsed_seconds': time.monotonic()-started,
              'pass': sum(c['passed'] for c in checks), 'fail': sum(not c['passed'] for c in checks)}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(f"TOTAL: PASS={result['pass']} FAIL={result['fail']}")
    return bool(result['fail'])


if __name__ == '__main__':
    raise SystemExit(main())
