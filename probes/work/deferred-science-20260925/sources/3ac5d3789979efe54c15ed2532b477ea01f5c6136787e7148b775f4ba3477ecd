"""Independent finite reference/count-inequality/SI arithmetic; no parent runner."""
from decimal import Decimal, localcontext
from math import exp, expm1, sqrt
import json
import time
import numpy as np


def gaussian_rates(alpha, d, g, order):
    x, w = np.polynomial.hermite.hermgauss(order)
    xx, yy = np.meshgrid(x, x, indexing='ij')
    weights = np.outer(w, w)/np.pi
    # |one-alpha wavefunction / vacuum wavefunction|^2 in dimensionless coordinates.
    density = 2*abs(alpha[0]*xx+alpha[1]*yy)**2
    effect = 2*np.sin(g*(d[0]*xx+d[1]*yy)/sqrt(2))**2
    return (float(np.sum(weights*effect)),
            float(np.sum(weights*density*effect)),
            float(np.sum(weights*density)))


def finite_count_moments(probabilities):
    assert min(probabilities) >= 0
    assert abs(sum(probabilities)-1) < 1e-14
    mean = sum(n*p for n, p in enumerate(probabilities))
    factorial = sum(n*(n-1)*p for n, p in enumerate(probabilities))
    at_least_one = sum(probabilities[1:])
    assert -1e-16 <= mean-at_least_one <= factorial/2+1e-16
    return mean, factorial, at_least_one


def main():
    started = time.perf_counter()
    d = np.array([.3, .4])
    v = float(np.dot(d, d))
    states = {
        'bright': np.array([.6, .8], dtype=complex),
        'orthogonal': np.array([-.8, .6], dtype=complex),
        'mode_1': np.array([1., 0.], dtype=complex),
        'mode_2': np.array([0., 1.], dtype=complex),
        'relative_i': np.array([1., 1j], dtype=complex)/sqrt(2),
        'relative_minus_i': np.array([1., -1j], dtype=complex)/sqrt(2),
    }
    rows = []
    for name, alpha in states.items():
        assert abs(np.vdot(alpha, alpha)-1) < 1e-14
        chi_squared = float(abs(np.dot(d, alpha))**2)
        fraction = chi_squared/v
        assert -1e-14 <= fraction <= 1+1e-14
        for g in (.5, .2, .1, .025):
            z = g*g*v/2
            reference_0 = -expm1(-z)
            reference_1 = reference_0+g*g*exp(-z)*chi_squared
            exact_ratio = 1+g*g*chi_squared/expm1(z)
            assert abs(reference_1/reference_0-exact_ratio) < 1e-14
            q20 = gaussian_rates(alpha, d, g, 20)
            q28 = gaussian_rates(alpha, d, g, 28)
            assert abs(q28[2]-1) < 2e-14
            error = max(abs(q28[0]-reference_0), abs(q28[1]-reference_1))
            refinement = max(abs(q28[i]-q20[i]) for i in (0, 1))
            assert error < 2e-14 and refinement < 2e-14
            ceiling = 1+2*z/expm1(z)
            assert 1-1e-14 <= exact_ratio <= ceiling+1e-14
            assert ceiling < 3
            rows.append({
                'state': name, 'g': g, 'v': v, 'chi_squared': chi_squared,
                'overlap_fraction': fraction, 'vacuum_rate_over_kappa': reference_0,
                'one_rate_over_kappa': reference_1,
                'ratio': exact_ratio, 'finite_g_reference_ceiling': ceiling,
                'limiting_ratio': 1+2*fraction,
                'quadrature_absolute_error': error, 'quadrature_refinement': refinement,
            })
    count_rows = []
    for g in (.2, .1, .05, .025):
        b = g**3.5
        z = g*g*v/2
        r0 = -expm1(-z)
        r1 = r0+g*g*exp(-z)*v
        distributions = []
        moments = []
        # A finite arithmetic example, not an original-model trajectory.
        # The same two-count probability saturates m-P(N>=1) <= F2/2.
        for rate in (r0, r1):
            mean = b*rate
            p2 = b*b/2
            p1 = mean-2*p2
            law = [1-p1-p2, p1, p2]
            distributions.append(law)
            moments.append(finite_count_moments(law))
        probability_ratio = moments[1][2]/moments[0][2]
        assert moments[0][1] <= b*b+1e-18
        assert moments[1][1] <= b*b+1e-18
        assert probability_ratio > 3
        count_rows.append({
            'g': g, 'b': b, 'b_over_g_cubed': b/g**3,
            'vacuum_law_on_0_1_2': distributions[0],
            'one_law_on_0_1_2': distributions[1],
            'vacuum_mean': moments[0][0], 'one_mean': moments[1][0],
            'vacuum_factorial_second': moments[0][1],
            'one_factorial_second': moments[1][1],
            'vacuum_probability': moments[0][2], 'one_probability': moments[1][2],
            'mean_ratio': moments[1][0]/moments[0][0],
            'at_least_one_ratio': probability_ratio,
            'probability_ratio_limit': 3,
            'scope': 'Moment-consistent finite count law only; not an original-generator counterexample.',
        })
    with localcontext() as ctx:
        ctx.prec = 55
        D = Decimal
        pi = D('3.141592653589793238462643383279502884197169399375105820975')
        h = D('6.62607015e-34')
        c = D('299792458')
        e = D('1.602176634e-19')
        hbar = h/(2*pi)
        si_rows = []
        for name, energy_GeV in [('MAGIC_Table6_systematics', D('5.9e10')),
                                 ('LHAASO_v2_ML_MINOS_Table1', D('6.9e11'))]:
            energy_joule = energy_GeV*D('1e9')*e
            directional_length = D(12).sqrt()*hbar*c/energy_joule
            directional_time = directional_length/c
            for A4 in (D(1), D(1)/2, D(1)/3):
                a_max = directional_length/A4.sqrt()
                tau_max = a_max/c
                assert abs(tau_max-D(12).sqrt()*hbar/(energy_joule*A4.sqrt())) < D('1e-85')
                si_rows.append({
                    'benchmark': name, 'E_QG_GeV': str(energy_GeV), 'A4': str(A4),
                    'a_sqrt_A4_upper_m': str(directional_length),
                    'tau_sqrt_A4_upper_s': str(directional_time),
                    'a_upper_m_for_A4': str(a_max), 'tau_upper_s_for_A4': str(tau_max),
                    'tau_upper_times_g_cubed_at_g_0_1_s': str(tau_max*D('.1')**3),
                    'tau_upper_times_g_cubed_at_g_0_01_s': str(tau_max*D('.01')**3),
                    'scope': 'Conditional scale conversion, not a selected spacing, finite-g validity threshold or necessary detector bandwidth.',
                })
        constants = {'h_J_s': str(h), 'c_m_s': str(c), 'elementary_charge_C': str(e),
                     'pi_decimal_used': str(pi), 'hbar_J_s': str(hbar),
                     'precision_digits': ctx.prec,
                     'energy_benchmarks_status': 'Rounded primary table values imported from the named photon parent; no likelihood reanalysis.'}
    result = {
        'scope': 'Independent finite harmonic quadrature, elementary count bounds, and conditional SI conversion only.',
        'not_executed': ['original cube builder', 'full compensated dynamics', 'microscopic spin process',
                         'author candidate or control', 'observational likelihood'],
        'reference_rate_rows': rows, 'count_bound_rows': count_rows,
        'SI_constants': constants, 'SI_rows': si_rows,
        'elapsed_seconds': time.perf_counter()-started,
    }
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
