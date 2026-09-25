"""Harmonic reference controls; no cubic rotor propagation or detector fit."""
from math import factorial, pi, sqrt
import json
import time
import numpy as np
from scipy.special import eval_genlaguerre, eval_hermite


def displacement_element(m, n, z):
    lower, upper = min(m, n), max(m, n)
    return (np.exp(-z*z/2) * sqrt(factorial(lower)/factorial(upper))
            * (1j*z)**(upper-lower) * eval_genlaguerre(lower, upper-lower, z*z))


def characteristic(state, d, g, t, frequencies):
    result = 0j
    for m, cm in state.items():
        for n, cn in state.items():
            phase = np.exp(1j*np.dot(frequencies, np.subtract(m, n))*t)
            factors = np.prod([displacement_element(mm, nn, g*dd)
                               for mm, nn, dd in zip(m, n, d)])
            result += cm.conjugate()*cn*phase*factors
    return result


def quadrature_characteristic(state, d, g, t, frequencies, order):
    q, w = np.polynomial.hermite.hermgauss(order)
    q1, q2 = np.meshgrid(q, q, indexing='ij')
    weight = np.outer(w, w)/pi
    wave = np.zeros((order, order), dtype=complex)
    for n, cn in state.items():
        polynomial = (eval_hermite(n[0], q1)*eval_hermite(n[1], q2)
                      / sqrt(2**sum(n)*factorial(n[0])*factorial(n[1])))
        wave += cn*np.exp(-1j*np.dot(frequencies, n)*t)*polynomial
    norm = np.sum(weight*abs(wave)**2)
    assert abs(norm-1) < 2e-14
    return np.sum(weight*abs(wave)**2*np.exp(1j*g*sqrt(2)*(d[0]*q1+d[1]*q2)))


def lower(state, mode):
    output = {}
    for n, cn in state.items():
        if n[mode]:
            m = list(n); m[mode] -= 1; m = tuple(m)
            output[m] = output.get(m, 0j)+sqrt(n[mode])*cn
    return output


def inner(left, right):
    return sum(c.conjugate()*right.get(n, 0j) for n, c in left.items())


def moment_data(state, d, t, frequencies):
    lowered = [lower(state, r) for r in range(2)]
    normal = anomalous = 0j
    for r in range(2):
        for s in range(2):
            normal += d[r]*d[s]*np.exp(1j*(frequencies[r]-frequencies[s])*t)*inner(lowered[r], lowered[s])
            anomalous += d[r]*d[s]*np.exp(-1j*(frequencies[r]+frequencies[s])*t)*inner(state, lower(lowered[s], r))
    assert abs(normal.imag) < 1e-13
    return float(normal.real), anomalous


def main():
    start = time.perf_counter()
    # A three-row curl-like test matrix, not an actual periodic cubic curl.
    curl = np.array([[1/sqrt(2), 1], [1/sqrt(2), -1], [0, sqrt(2)]])
    lambdas = np.array([1., 4.]); frequencies = np.sqrt(lambdas)
    assert np.max(abs(curl.T@curl-np.diag(lambdas))) < 1e-14
    drows = curl/np.sqrt(2*np.sqrt(lambdas))[None, :]
    assert np.max(abs(drows.T@drows-np.diag(np.sqrt(lambdas)/2))) < 1e-14
    states = {
        'one_in_first': {(1, 0): 1.+0j},
        'one_two_mode_superposition': {(1, 0): 1/sqrt(2)+0j, (0, 1): 1j/sqrt(2)},
        'vacuum_plus_two': {(0, 0): sqrt(.9)+0j, (2, 0): sqrt(.1)+0j},
        'vacuum_minus_two': {(0, 0): sqrt(.9)+0j, (2, 0): -sqrt(.1)+0j},
    }
    rows = []; average_rows = []; max_quad = 0.; max_refinement = 0.
    for name, state in states.items():
        assert abs(inner(state, state)-1) < 1e-14
        energy = sum(abs(c)**2*np.dot(frequencies, n) for n, c in state.items())
        eta = np.array([inner(state, lower(lower(state, r), r)) for r in range(2)])
        for t in (0., .4, 1.1):
            leading = np.array([2*(n+a.real) for n, a in
                                (moment_data(state, d, t, frequencies) for d in drows)])
            sum_formula = energy+np.sum(frequencies*(eta*np.exp(-2j*frequencies*t)).real)
            assert abs(sum(leading)-sum_formula) < 1e-13
            for g in (.2, .1, .05):
                exact = []; errors = []
                for d in drows:
                    val = characteristic(state, d, g, t, frequencies)
                    quad = quadrature_characteristic(state, d, g, t, frequencies, 20)
                    fine = quadrature_characteristic(state, d, g, t, frequencies, 28)
                    max_quad = max(max_quad, abs(val-fine))
                    max_refinement = max(max_refinement, abs(quad-fine))
                    assert abs(val-fine) < 2e-13 and abs(quad-fine) < 2e-13
                    vacuum = np.exp(-g*g*np.dot(d, d)/2)
                    exact.append(float(2*(vacuum-val.real)/(g*g)))
                residual = np.array(exact)-leading
                rows.append(dict(state=name, t=t, g=g, energy=float(energy),
                                 deficit_over_g_squared=exact,
                                 leading_quadratic_response=leading.tolist(),
                                 maximum_scaled_remainder=float(max(abs(residual))/(g*g))))
        for window in (.3, 2., 20.):
            exact_average = float(energy+np.sum(frequencies*(eta*np.exp(-1j*frequencies*window)).real
                                               *np.sinc(frequencies*window/pi)))
            bound = float(sum(abs(eta))/window)
            assert abs(exact_average-energy) <= bound+1e-14
            average_rows.append(dict(state=name, time_window=window,
                                     averaged_leading_response=exact_average,
                                     excitation_energy=float(energy), oscillatory_bound=bound))
    phase = dict(p=.1, same_occupation=.2,
                 plus=.2+sqrt(.18), minus=.2-sqrt(.18))
    assert phase['plus'] > 0 and phase['minus'] < 0
    benchmark = dict(source='Brouri et al quant-ph/0007032v1 equations1-2 and Fig3 caption',
                     signal_fraction=.34, corrected_g2_zero=0.,
                     corresponding_raw_normalized_coincidence=1-.34**2,
                     poisson_reference_bin_counts=5780*5990*1e-9*11450,
                     scope='Printed-parameter arithmetic only, not digitized data or a model fit.')
    assert .84 < benchmark['corresponding_raw_normalized_coincidence'] < 1
    output = dict(scope='Finite two-mode harmonic reference and printed benchmark arithmetic; '
                       'no original cubic dynamics, full detector simulation, empirical fit or universal no-go.',
                  response_rows=rows, time_average_rows=average_rows,
                  same_energy_phase_example=phase, empirical_normalization_check=benchmark,
                  maximum_characteristic_quadrature_error=float(max_quad),
                  maximum_quadrature_refinement_error=float(max_refinement),
                  elapsed_seconds=time.perf_counter()-start)
    print(json.dumps(output, indent=2, allow_nan=False))
    print('per_element: finite reference characteristic elements checked against independent quadrature.')
    print('per_site: checked and not executed — no physical single-site detector dynamics is simulated.')
    print('per_mode: finite occupation and equal-energy phase-sensitive reference examples are exercised.')
    print('per_block: a two-mode, three-probe harmonic block checks anomalous and ordinary second moments.')
    print('lattice_wide: checked and not executed — the full cubic curl identity is analytic, not simulated here.')


if __name__ == '__main__':
    main()
