"""Primitive rotor words and separate finite balance controls; no cube builder import."""

from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import math


HERE = Path(__file__).resolve().parent
A = (0, 3, 5, 6)
B = (1, 2, 4, 7)
EDGES = tuple((a, b) for a in A for b in B if a ^ b in (1, 2, 4))
OMEGA = (tuple(1 if v in A else 0 for v in range(8)), (0,) * 12)


def legal(word):
    q, electric = word
    div = [0] * 8
    for value, (a, b) in zip(electric, EDGES):
        div[a] += value
        div[b] -= value
    assert all(div[v] == q[v] - int(v in A) for v in range(8))
    assert sum(q) == 4 and all(x in (-1, 0, 1) for x in q)


def combine(*terms):
    out = defaultdict(Fraction)
    for factor, vector in terms:
        for word, coefficient in vector.items():
            out[word] += factor * coefficient
    return {word: c for word, c in out.items() if c}


def hop(vector, inward=False, center=None):
    out = defaultdict(Fraction)
    for (charges, electric), coefficient in vector.items():
        for index, (a, b) in enumerate(EDGES):
            if center is not None and a != center:
                continue
            src, dst = (b, a) if inward else (a, b)
            if not charges[src] or charges[dst]:
                continue
            q, fields = list(charges), list(electric)
            sign = q[src]
            q[src], q[dst] = 0, sign
            fields[index] += sign if inward else -sign
            word = tuple(q), tuple(fields)
            legal(word)
            out[word] += coefficient
    return dict(out)


def mark(vector, edge, signs):
    a, b = EDGES[edge]
    out = defaultdict(Fraction)
    for (charges, electric), coefficient in vector.items():
        if charges[a] or charges[b]:
            continue
        for sign in signs:
            q, fields = list(charges), list(electric)
            q[a], q[b] = sign, -sign
            fields[edge] += sign
            word = tuple(q), tuple(fields)
            legal(word)
            out[word] += coefficient
    return dict(out)


def norm2(vector):
    return sum((c * c for c in vector.values()), Fraction())


def primitive_words():
    initial = {OMEGA: Fraction(1)}
    f = hop(initial)
    f2 = hop(f)
    rows, totals = [], {}
    assert norm2(f) == 12 and norm2(f2) == 168
    for instrument, cases in [('resolved', [('plus', (1,)), ('minus', (-1,))]),
                              ('coherent', [('coherent', (1, -1))])]:
        total_b = total_r = total_c = Fraction()
        for edge, (a, b) in enumerate(EDGES):
            for name, signs in cases:
                beta = mark(f, edge, signs)
                remainder = combine((Fraction(1, 2), mark(f2, edge, signs)), (-1, hop(beta)))
                local = combine((-1, hop(beta, center=a)))
                assert remainder == local
                g = combine((1, hop(hop(remainder, inward=True))), (-1, hop(hop(remainder), inward=True)))
                loss_r = sum(norm2(mark(remainder, k, (s,))) for k in range(12) for s in (1, -1))
                loss_g = sum(norm2(mark(g, k, (s,))) for k in range(12) for s in (1, -1))
                nb, nr = norm2(beta), norm2(remainder)
                assert (nb, nr) == {'plus': (2, 4), 'minus': (2, 2), 'coherent': (4, 6)}[name]
                assert loss_r == 0 and loss_g == 24 * nr
                wrong = combine((1, mark(f2, edge, signs)), (-1, hop(beta)))
                mutation_error = norm2(combine((1, wrong), (-1, remainder)))
                assert mutation_error > 0
                total_b += nb
                total_r += nr
                total_c += loss_g
                rows.append({'edge': [a, b], 'mark': name, 'b': int(nb), 'r': int(nr),
                             'initial_loss_form': int(loss_r), 'loss_after_G': int(loss_g),
                             'wrong_half_factor_squared_residual': int(mutation_error)})
        assert (total_b, total_r, total_c) == (48, 72, 1728)
        totals[instrument] = {'sum_b': int(total_b), 'sum_r': int(total_r), 'sum_loss_after_G': int(total_c)}
    return {'F_Omega_norm_squared': 12, 'F_squared_Omega_norm_squared': 168,
            'initial_rotor_energy_over_delta': -84, 'rows': rows, 'totals': totals,
            'scope': 'New exact integer/rational rotor word calculation at zero field; no finite-spin dynamics or joint-limit simulation.'}


def balance_toy():
    # Four levels: initial, low output, high output, terminal.
    # H=(0,0,delta/epsilon^4,0); the source mark maps initial to
    # epsilon*sqrt(b)*low + epsilon^2*sqrt(r)*high, and the loss mark
    # maps high to sqrt(gamma)*terminal. Both rates are kappa/epsilon^2.
    delta, kappa, b, r, gamma = 1.3, .07, 2., 6., 1.8
    rows = []
    for epsilon in (.2, .1, .05, .025):
        a, d = kappa * (b + epsilon**2 * r), kappa * gamma / epsilon**2
        def energy(t):
            source_integral = math.exp(-a*t) * (-math.expm1(-(d-a)*t)) / (d-a)
            return kappa * delta * r / epsilon**2 * source_integral
        for clock, t in [('physical', .7), ('initial_layer', epsilon**2 * .6)]:
            high = energy(t)
            gain = kappa * delta * r / epsilon**2 * math.exp(-a*t)
            loss = d * high
            h = min(t/20, epsilon**2 * .001)
            fd1 = (energy(t+h)-energy(t-h))/(2*h)
            fd2 = (energy(t+h/2)-energy(t-h/2))/h
            err1, err2 = abs(fd1-(gain-loss)), abs(fd2-(gain-loss))
            assert err2 < max(0.35*err1, 1e-8)
            assert abs(fd2-(gain-loss)) < 1e-5 * max(1, abs(gain-loss))
            assert abs(fd2-gain) > 100 * max(err2, 1e-10)
            target = (delta*r/gamma*math.exp(-kappa*b*t) if clock == 'physical'
                      else delta*r/gamma*(-math.expm1(-kappa*gamma*.6)))
            rows.append({'epsilon': epsilon, 'clock': clock, 'time': t, 'energy': high,
                         'limiting_energy': target, 'absolute_energy_error': abs(high-target),
                         'scaled_gain': epsilon**2*gain, 'scaled_loss': epsilon**2*loss,
                         'drift': gain-loss, 'finite_difference_error_h': err1,
                         'finite_difference_error_h_over_2': err2,
                         'omitted_loss_error': abs(fd2-gain)})
    for clock in ['physical', 'initial_layer']:
        errors = [x['absolute_energy_error'] for x in rows if x['clock'] == clock]
        assert errors[-1] < errors[-2] < errors[-3] < errors[-4]
        assert errors[-1] < .3*errors[-2]
    p = .01
    diagonal = p
    coherence = -math.sqrt(p*(1-p))
    signed_loss = diagonal + coherence
    assert signed_loss < 0
    return {'rows': rows, 'positive_operator_anticommutator_counterexample': {
        'A': [[0, 0], [0, 1]], 'Gamma': [[1, 1], [1, 1]],
        'pure_state': [math.sqrt(1-p), -math.sqrt(p)],
        'diagonal_loss': diagonal, 'coherence_loss': coherence,
        'Re_Tr_A_Gamma_rho': signed_loss,
        'scope': 'Finite algebraic example; does not claim a negative loss on the original cube trajectory.'},
        'scope': 'Separate four-level GKLS population solution and finite-difference balance test; not a proxy proof for the cube.'}


def main():
    output = {'primitive_words': primitive_words(), 'balance_toy': balance_toy(),
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    text = json.dumps(output, indent=2) + '\n'
    (HERE/'CONTROL_RESULTS.json').write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()
