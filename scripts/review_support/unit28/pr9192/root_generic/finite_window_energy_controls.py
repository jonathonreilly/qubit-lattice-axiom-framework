"""Root controls for a four-state compensation example, not a lattice truncation."""
from pathlib import Path
import hashlib
import json
import time
import mpmath as mp

mp.mp.dps = 80


def string(x):
    return mp.nstr(x, 60)


def complex_pair(x):
    return [string(mp.re(x)), string(mp.im(x))]


def spectrum(a, c, epsilon):
    z = 1 + (a*a+c)*epsilon**2
    d = mp.sqrt(z*z-4*c*a*a*epsilon**4)
    low = 2*c*a*a/(z+d)
    high = (z+d)/(2*epsilon**4)
    high_weight = (a*a/epsilon**2-low)/(high-low)
    matrix = mp.matrix([[a*a/epsilon**2, a/epsilon**3],
                        [a/epsilon**3, 1/epsilon**4+c/epsilon**2]])
    values, vectors = mp.eigsy(matrix)
    direct_weights = [abs(vectors[0, k])**2 for k in range(2)]
    eigen_error = max(abs(values[0]-low), abs(values[1]-high))
    weight_error = max(abs(direct_weights[0]-(1-high_weight)),
                       abs(direct_weights[1]-high_weight))
    mean = (1-high_weight)*low+high_weight*high
    variance = (1-high_weight)*(low-mean)**2+high_weight*(high-mean)**2
    mean_error = abs(mean-a*a/epsilon**2)
    variance_relative_error = abs(variance/(a*a/epsilon**6)-1)
    assert max(eigen_error, mean_error) < mp.mpf('1e-65')
    assert max(weight_error, variance_relative_error) < mp.mpf('1e-70')
    assert 0 < high_weight < 1
    return matrix, low, high, high_weight, {
        'a': string(a), 'c': string(c), 'epsilon': string(epsilon),
        'low_energy': string(low), 'high_energy': string(high),
        'high_weight': string(high_weight),
        'high_weight_over_a_squared_epsilon_squared': string(high_weight/(a*a*epsilon**2)),
        'limiting_energy': string(c*a*a),
        'mean': string(mean), 'variance': string(variance),
        'direct_eigenvalue_error': string(eigen_error),
        'direct_weight_error': string(weight_error),
        'mean_formula_error': string(mean_error),
        'variance_formula_relative_error': string(variance_relative_error),
    }


def main():
    tic = time.perf_counter()
    a0, c0, a2, c2, kappa = mp.mpf(1), mp.mpf(1)/3, mp.mpf(2), mp.mpf(3)/5, mp.mpf(7)/10
    epsilons = [mp.mpf(1)/q for q in [3, 5, 10, 20, 40]]
    spec_rows, count_rows, response_rows = [], [], []
    for epsilon in epsilons:
        h0, _, _, _, row0 = spectrum(a0, c0, epsilon)
        h2, low, high, high_weight, row2 = spectrum(a2, c2, epsilon)
        row0['number_sector'] = 0
        row2['number_sector'] = 2
        spec_rows.extend([row0, row2])
        loss = mp.matrix([[0, 0], [0, kappa/(2*epsilon**2)]])
        for window in [mp.mpf(3)/20, mp.mpf(3)/5, mp.mpf(13)/10]:
            no_event = mp.expm((-1j*h0-loss)*window)*mp.matrix([1, 0])
            survival = sum(abs(no_event[k])**2 for k in range(2))
            event_probability = 1-survival
            target = 1-mp.exp(-kappa*a0*a0*window)
            assert 0 < event_probability < 1
            count_rows.append({'epsilon': string(epsilon), 'window': string(window),
                               'actual_first_event_probability': string(event_probability),
                               'effective_probability': string(target),
                               'difference': string(event_probability-target),
                               'conditional_energy_law': 'Exactly row2: every actual jump produces p2; H2 evolution preserves its spectral measure.'})
        centre = c2*a2*a2
        for time_parameter in [mp.mpf(0), mp.mpf(1)/10, mp.mpf(1), mp.pi]:
            characteristic = (1-high_weight)*mp.exp(1j*time_parameter*low)+high_weight*mp.exp(1j*time_parameter*high)
            target = mp.exp(1j*time_parameter*centre)
            direct = mp.expm(1j*time_parameter*h2)[0, 0]
            error = abs(characteristic-target)
            bound = 2*high_weight+abs(time_parameter)*abs(low-centre)
            assert abs(characteristic-direct) < mp.mpf('1e-65')
            assert error <= bound+mp.mpf('1e-70')
            response_rows.append({'epsilon': string(epsilon), 'time_parameter': string(time_parameter),
                                  'characteristic': complex_pair(characteristic),
                                  'target_characteristic': complex_pair(target),
                                  'direct_exponential_error': string(abs(characteristic-direct)),
                                  'convergence_error': string(error), 'proved_error_bound': string(bound)})
        # A fixed soft response is continuous; a sharp endpoint at the limiting
        # atom deliberately is not a continuity set of the limiting measure.
        soft = lambda energy: 1/(1+(energy-centre)**2)
        soft_mean = (1-high_weight)*soft(low)+high_weight*soft(high)
        endpoint_probability = ((1-high_weight) if low >= centre else 0)+(high_weight if high >= centre else 0)
        interior_probability = ((1-high_weight) if abs(low-centre)<mp.mpf(1)/10 else 0)+(high_weight if abs(high-centre)<mp.mpf(1)/10 else 0)
        assert low < centre < high
        response_rows.append({'epsilon': string(epsilon), 'soft_response': string(soft_mean),
                              'soft_limit': '1', 'sharp_half_line_at_limit_probability': string(endpoint_probability),
                              'sharp_half_line_target_atom_probability': '1',
                              'fixed_point_one_half_width_interval_probability': string(interior_probability),
                              'interpretation': 'The half-line boundary carries the limiting atom, so weak convergence does not control it.'})
    result = {'scope': __doc__, 'precision_digits': mp.mp.dps,
              'parameters': {'a0': string(a0), 'c0': string(c0), 'a2': string(a2),
                             'c2': string(c2), 'kappa': string(kappa)},
              'spectrum_rows': spec_rows, 'first_event_rows': count_rows,
              'response_rows': response_rows,
              'original_lattice_simulation': False,
              'conditional_energy_identity': 'Analytic for this example; not a numerical integration of a lattice trajectory.',
              'all_assertions_passed': True,
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'elapsed_seconds': time.perf_counter()-tic}
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
