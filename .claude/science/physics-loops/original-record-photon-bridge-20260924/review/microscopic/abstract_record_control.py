#!/usr/bin/env python3
"""Small independent abstract-parent-class control, NOT a cube/rotor model.

Six states = three record-number stages, each with penalty 0 or 1.
Exact operator checks use integer/Fraction arithmetic. Numerical no-jump
exponentials and time-bin probabilities use 80 digits; they are corroborative,
not interval enclosures or the proof of either limiting statement.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import mpmath as mp


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def adj(a):
    return list(map(list, zip(*a)))


def plus(*terms):
    return [[sum(scale * mat[i][j] for scale, mat in terms)
             for j in range(6)] for i in range(6)]


def diag(values):
    return [[values[i] if i == j else 0 for j in range(6)] for i in range(6)]


def zero():
    return diag([0] * 6)


def operator_check():
    ident = diag([1] * 6)
    W = diag([0, 1] * 3); P = diag([1, 0] * 3); N = diag([0, 0, 2, 2, 4, 4])
    Q = W; C = P
    T = zero(); j = zero()
    for k in range(3):
        T[2*k][2*k+1] = T[2*k+1][2*k] = 1
    for k in range(2):
        j[2*k+2][2*k+1] = 1
    assert T == adj(T) and C == adj(C)
    assert mm(T, T) == ident and mm(C, C) == C
    assert mm(j, P) == zero()
    assert plus((1, mm(W, j)), (-1, mm(j, W))) == plus((-1, j))
    assert plus((1, mm(N, j)), (-1, mm(j, N))) == plus((2, j))
    assert mm(N, T) == mm(T, N) and mm(N, C) == mm(C, N)
    assert mm(W, C) == mm(C, W)
    assert mm(j, adj(j)) == diag([0, 0, 1, 0, 1, 0])
    assert mm(adj(j), j) == diag([0, 1, 0, 1, 0, 0])
    A = mm(mm(Q, T), P); M = mm(adj(A), A)
    C0 = mm(mm(P, C), P); C1 = mm(mm(Q, C), Q)
    H2 = plus((1, C0), (-1, M))
    # There is no W=2 sector, so Z=0.
    H4 = plus((1, mm(M, M)), (-F(1, 2), mm(M, C0)),
              (-F(1, 2), mm(C0, M)), (1, mm(mm(adj(A), C1), A)))
    B = plus((-1, mm(mm(mm(P, j), Q), mm(T, P))))
    expected = zero(); expected[2][0] = expected[4][2] = -1
    assert M == P and H2 == zero() and H4 == zero() and B == expected
    return {'dimension': 6, 'record_numbers': [0, 0, 2, 2, 4, 4],
            'penalty': [0, 1, 0, 1, 0, 1],
            'T_C_j_norms': [1, 1, 1],
            'jP_zero_W_lowering_N_raising_checked': True,
            'H2_and_H4_exactly_zero': True,
            'effective_B_nonzero_entries_row_col_value': [[2, 0, -1], [4, 2, -1]],
            'interpretation': 'One original mark advances the record stage; actual first jump resets exactly to the next stage ground state.'}


def dec(x):
    return mp.mpf(x.numerator) / x.denominator if isinstance(x, F) else mp.mpf(x)


def micro_two_event(eps, kappa, width):
    # delta=1; C=P. The first two record stages have the same no-jump matrix.
    H = mp.matrix([[eps**-2, eps**-3], [eps**-3, eps**-4]])
    generator = -mp.j * H
    generator[1, 1] -= kappa / (2 * eps**2)
    x = mp.expm(generator * width) * mp.matrix([1, 0])
    Fwait = 1 - abs(x[0])**2 - abs(x[1])**2
    assert -mp.mpf('1e-65') <= Fwait <= 1 + mp.mpf('1e-65')
    # I=[0,width], next gap <=width. The jump resets the next stage to ground.
    return Fwait**2


def target_two_event(kappa, width):
    return (-mp.expm1(-kappa * width))**2


def shrinking_window_rows():
    rows = []
    for n in (2, 4, 8, 16, 32, 64):
        eps = 1 / mp.sqrt(n * (n + 1)); width = eps**5
        p1 = target_two_event(1, width); p2 = target_two_event(2, width)
        r = p2 - p1
        m1 = micro_two_event(eps, 1, width); m2 = micro_two_event(eps, 2, width)
        bound1 = eps**14 / 9; bound2 = 4 * eps**14 / 9
        assert m1 <= bound1 + mp.mpf('1e-65')
        assert m2 <= bound2 + mp.mpf('1e-65')
        contrast = m2 - m1
        assert abs(contrast) <= bound1 + bound2 + mp.mpf('1e-65')
        rows.append({'n': n, 'epsilon': str(eps), 'width_equals_epsilon_to_5': str(width),
                     'target_contrast_r_n': str(r), 'microscopic_contrast': str(contrast),
                     'microscopic_contrast_over_target': str(contrast/r),
                     'proved_absolute_ratio_upper_bound': str((bound1 + bound2)/r),
                     'microscopic_probability_kappa_1': str(m1),
                     'microscopic_probability_kappa_2': str(m2)})
    assert mp.mpf(rows[-1]['proved_absolute_ratio_upper_bound']) < mp.mpf('1e-7')
    return rows


def fixed_window_rows():
    width = mp.mpf(1) / 4
    target = target_two_event(2, width) - target_two_event(1, width)
    rows = []
    for n in (4, 8, 16, 32, 64):
        eps = 1 / mp.sqrt(n * (n + 1))
        value = micro_two_event(eps, 2, width) - micro_two_event(eps, 1, width)
        rows.append({'resource_index': n, 'fixed_width': str(width),
                     'target_contrast': str(target), 'microscopic_contrast': str(value),
                     'absolute_error': str(abs(value-target))})
    assert mp.mpf(rows[-1]['absolute_error']) < mp.mpf(rows[0]['absolute_error'])
    return rows


def bin_bracket_rows():
    # Target first-two-time density in (s,t) is kappa^2 exp(-kappa*t), t>s.
    a, c, lag, horizon = F(1, 4), F(1, 2), F(1, 4), F(3, 4)
    kappa = mp.mpf(1)
    exact = (mp.exp(-dec(a))-mp.exp(-dec(c))) * (-mp.expm1(-dec(lag)))
    rows = []
    for m in (6, 12, 24, 48, 96):
        h = horizon / m; lower = mp.mpf(0); upper = mp.mpf(0)
        exps = [mp.exp(-dec(h * i)) for i in range(m + 1)]
        for k in range(m):
            slo, shi = k*h, (k+1)*h
            for l in range(k, m):
                tlo, thi = l*h, (l+1)*h
                if k == l:
                    mass = exps[k] - exps[k+1] * (1+dec(h))
                else:
                    mass = dec(h) * (exps[l] - exps[l+1])
                inner = slo >= a and shi <= c and thi-slo <= lag
                # Positive-area intersection with a<s<c and 0<t-s<lag.
                outer = max(slo, a, tlo-lag) < min(shi, c, thi)
                if inner: lower += mass
                if outer: upper += mass
        assert lower <= exact + mp.mpf('1e-65')
        assert exact <= upper + mp.mpf('1e-65')
        boundary_bound = 8 * kappa**2 * dec(horizon) * dec(h)
        assert upper-lower <= boundary_bound
        rows.append({'bins': m, 'mesh': str(dec(h)), 'inner_probability': str(lower),
                     'exact_probability': str(exact), 'outer_probability': str(upper),
                     'bracket_gap': str(upper-lower), 'proved_boundary_bound': str(boundary_bound)})
    assert mp.mpf(rows[-1]['bracket_gap']) < mp.mpf(rows[0]['bracket_gap'])
    return rows


def main():
    mp.mp.dps = 80
    base = Path(__file__).resolve().parent
    pins = json.loads((base/'SOURCE_PINS.json').read_text())
    for src in pins['sources']:
        assert hashlib.sha256((base/src['snapshot']).read_bytes()).hexdigest() == src['sha256']
    result = {'scope': 'Independent six-state abstract bounded-parent-class control. NOT the physical cube, compensated link construction, or rotor simulation. No theorem rate inferred from finite numerics.',
              'precision_decimal_digits': mp.mp.dps, 'mpmath_version': mp.__version__,
              'operator_checks': operator_check(),
              'finite_bin_brackets': bin_bracket_rows(),
              'fixed_window_corroboration': fixed_window_rows(),
              'arbitrary_shrinking_window_schedule_counterexample': shrinking_window_rows(),
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'source_pins_sha256': hashlib.sha256((base/'SOURCE_PINS.json').read_bytes()).hexdigest(),
              'overall': 'Exact operator checks and all stated numerical controls passed'}
    output = json.dumps(result, indent=2, sort_keys=True)+'\n'
    (base/'ABSTRACT_CONTROL_RESULTS.json').write_text(output)
    print(output, end='')


if __name__ == '__main__':
    main()
