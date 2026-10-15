"""Exact rational-knot composition of coherent counts and the massless Gram.

Independent representations within the author calculation: piecewise arrival
density overlap versus original coherent harmonic response and the radial
|time difference| kernel. No floating nullspace or numeric quadrature needed.
"""
AUDIT_TIMEOUT_SEC = 180

from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sympy as s

z = s.symbols('z', real=True)
L = s.Rational(3, 5)
T = s.Integer(1)
beta = [1, -2, 1]


def times(channel):
    return [s.Rational(7, 5)+channel+j for j in range(3)]


def rectangles(channel, omit_clock=False, wrong_same_coordinate=False):
    ts = times(channel)
    result = []
    # H_clock+force at the station; spacecraft at x=L e1.
    early = -z if omit_clock else -(1+z)
    late = -z if omit_clock else 1-z
    for coeff, shift in [(early, -2*L), (late, 0),
                         (2*z, -L if wrong_same_coordinate else -L-L*z)]:
        result.extend([(ts[0]+shift, ts[1]+shift, coeff),
                       (ts[1]+shift, ts[2]+shift, -coeff)])
    return result


def wave_events(channel):
    """T_wave=-i/k times these events, from orbit/clock particular solutions."""
    result = []
    for b, time in zip(beta, times(channel)):
        result += [(time-2*L, b*(1+z)), (time, b*(z-1)),
                   (time-L-L*z, -2*b*z)]
    return result


def partitions(endpoints):
    breaks = {s.Integer(-1), s.Integer(1)}
    for i, x in enumerate(endpoints):
        for y in endpoints[i+1:]:
            diff = s.expand(x-y)
            slope = diff.coeff(z)
            if slope:
                root = -diff.subs(z, 0)/slope
                if -1<root<1:
                    breaks.add(root)
    return sorted(breaks)


def integrate_poly(expr, lo, hi):
    p = s.Poly(s.expand(expr), z)
    return sum(c*(hi**(power[0]+1)-lo**(power[0]+1))/(power[0]+1)
               for power, c in p.terms())


def time_matrix(**options):
    rects = [rectangles(i, **options) for i in range(2)]
    edges = list(set(edge for rs in rects for lo, hi, c in rs for edge in [lo, hi]))
    breaks = partitions(edges)
    g = s.zeros(2)
    for loz, hiz in zip(breaks[:-1], breaks[1:]):
        midz = (loz+hiz)/2
        ordered = sorted(edges, key=lambda q:q.subs(z, midz) if hasattr(q, 'subs') else q)
        for lot, hit in zip(ordered[:-1], ordered[1:]):
            midt = (lot+hit)/2
            probe = midt.subs(z, midz)
            h = []
            for rs in rects:
                total = 0
                for left, right, c in rs:
                    if left.subs(z, midz)<probe<right.subs(z, midz):
                        total += c
                h.append(s.expand(total))
            for i in range(2):
                for j in range(2):
                    g[i, j] += integrate_poly((hit-lot)*h[i]*h[j], loz, hiz)
    return s.simplify(g), breaks


def spectral_matrix():
    events = [wave_events(i) for i in range(2)]
    edges = list(set(t for ev in events for t, _ in ev))
    breaks = partitions(edges)
    g = s.zeros(2)
    for loz, hiz in zip(breaks[:-1], breaks[1:]):
        midz = (loz+hiz)/2
        for i in range(2):
            for j in range(2):
                polynomial = 0
                for ti, ai in events[i]:
                    for tj, aj in events[j]:
                        dt = s.expand(ti-tj)
                        sign = s.sign(dt.subs(z, midz))
                        polynomial -= ai*aj*sign*dt/2
                g[i, j] += integrate_poly(polynomial, loz, hiz)
    # Both return 4*pi*G. The -1/2 is the real half-line radial kernel.
    return s.simplify(g), breaks


def run_checks():
    checks = []
    def exact(name, expr):
        residual = s.simplify(expr)
        assert residual == 0, (name, residual)
        checks.append({'name':name, 'exact_residual':str(residual)})
    tm, breaks = time_matrix()
    sp, _ = spectral_matrix()
    for i in range(2):
        for j in range(2):
            exact(f'arrival_vs_original_coherent_spectral_gram_{i}_{j}', tm[i, j]-sp[i, j])
        ts = times(i)
        exact(f'initial_position_moment_{i}', sum(beta))
        exact(f'initial_velocity_moment_{i}', sum(b*t for b, t in zip(beta, ts)))
        exact(f'original_harmonic_zero_sum_{i}', sum(a for _, a in wave_events(i)))
        # Constant direct field response integrates early minus late pulses.
        exact(f'constant_background_response_{i}', sum(b*((t-2*L)-t) for b, t in zip(beta, ts)))
    assert tm[0, 0]>0 and tm.det()>0
    checks.append({'name':'exact_positive_definite_count_gram', 'determinant_of_4pi_gram':str(tm.det())})
    wrong_clock, _ = time_matrix(omit_clock=True)
    wrong_phase, _ = time_matrix(wrong_same_coordinate=True)
    assert wrong_clock != tm and wrong_phase != tm
    checks.append({'name':'reject_omitted_station_direct_clock', 'exact_4pi_matrix_difference':str(wrong_clock-tm)})
    checks.append({'name':'reject_equal_coordinate_cross_path_composition', 'exact_4pi_matrix_difference':str(wrong_phase-tm)})
    result = {
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'checks_passed':len(checks), 'checks':checks,
              'fixture':{'light_time_L':str(L),'count_duration_T':str(T),'coupling_times_turnaround':'1','reference':'two stationary free bodies, same station clock at emission/reception','contrast':'adjacent finite count difference, two time-translated channels'},
              'four_pi_times_gram':[[str(tm[i, j]) for j in range(2)] for i in range(2)],
              'gram_decimal':[[float(tm[i, j]/(4*s.pi)) for j in range(2)] for i in range(2)],
              'angular_partition':[str(q) for q in breaks],
              'scope':'Exact conditional symbolic composition, no observed data or fitted constants. Free massless conformal scalar, ideal coherent link, stationary reference. Actual action/state/energy/calibration remain supplied. The accelerated theorem is separately checked; this exact fixture tests count-to-multipath composition and normalization.'}
    return result


if __name__ == '__main__':
    print(json.dumps(run_checks(), indent=2))
