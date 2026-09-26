#!/usr/bin/env python3
"""Independent finite controls for forward influence and a birth-only relay."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from math import factorial
import json
import platform

import sympy as sp

HERE = Path(__file__).resolve().parent


def neighbors(point):
    answer = set()
    for axis in range(len(point)):
        for sign in [-1, 1]:
            target = list(point)
            target[axis] += sign
            answer.add(tuple(target))
    return answer


def footprint_checks():
    results = []
    for d in [1, 2, 3]:
        origin = (0,)*d
        z = 2*d
        closed = neighbors(origin)|{origin}
        birth_centers = {center for center in closed if origin in neighbors(center)|{center}}
        edges = {tuple(sorted((x,y))) for x in closed for y in neighbors(x)}
        forward_pairs = []
        for x,y in edges:
            read = neighbors(x)|neighbors(y)|{x,y}
            assert origin in read
            for output in [x,y]:
                assert sum(abs(c) for c in output) <= 2
                forward_pairs.append(((x,y),output))
        backward_pairs = []
        for y in neighbors(origin):
            read = neighbors(origin)|neighbors(y)|{origin,y}
            backward_pairs.extend([((origin,y),source) for source in read])
        assert len(birth_centers) == z+1
        assert len(edges) == z*z
        assert len(forward_pairs) == len(backward_pairs) == 2*z*z
        assert len(forward_pairs) <= 2*z*(z+1)
        # Some forward edge events do not update the source site at all.
        nonincident = [(edge,out) for edge,out in forward_pairs if origin not in edge]
        assert nonincident
        results.append({'dimension':d,'degree':z,'forward_birth_centers':len(birth_centers),
                        'forward_edge_clocks':len(edges),
                        'forward_edge_to_output_pairs':len(forward_pairs),
                        'backward_edge_to_read_pairs':len(backward_pairs),
                        'conservative_hop_coefficient_in_Lambda':2*z*(z+1),
                        'nonincident_forward_clock_witness':nonincident[0]})
    return results


def shell_and_series_checks():
    shell_counts = []
    for d in [1,2,3]:
        for radius in range(1,7):
            actual = sum(sum(abs(x) for x in point)==radius
                         for point in product(range(-radius,radius+1),repeat=d))
            formula = sum(2**k*sp.binomial(d,k)*sp.binomial(radius-1,k-1)
                          for k in range(1,min(d,radius)+1))
            assert actual == formula
            shell_counts.append({'dimension':d,'radius':radius,'sites':actual})
    eta = 1/(1-1/(2*sp.E))
    path_tail_cases = []
    for m in [1,2,3,5,10,20,40]:
        mu = sp.Rational(m)/(2*sp.E)
        total = sp.exp(mu)-sum(mu**n/sp.factorial(n) for n in range(m))
        bound = eta*sp.Rational(1,2)**m
        assert sp.N(bound-total,100) > 0
        path_tail_cases.append({'m':m,'sum_over_paths_n_at_least_m':float(sp.N(total,50)),
                                'bound_eta_times_2_to_minus_m':float(bound)})
    for R in range(1,25):
        if R % 2:
            exact = 4*F(1,2)**((R+1)//2)
        else:
            exact = 3*F(1,2)**(R//2)
        finite = sum(F(1,2)**((r+1)//2) for r in range(R,101))
        rest = 4*F(1,2)**51  # tail from r=101
        assert finite+rest == exact
        assert exact <= 4*F(1,2)**((R+1)//2)
    return {'shell_counts':shell_counts,'chronological_path_tail_controls':path_tail_cases,
            'sum_r_positive_2_to_minus_ceil_r_over_2':'2',
            'radius_tail_sum_thresholds_checked':24,'eta':float(eta)}


def relay_checks():
    # d=1, kappa=0, epsilon=1, j=1/2, the actual six-content menu.
    # Initial copies differ only at 0: content 0 versus its antipode 1.
    j, epsilon = F(1,2), F(1)
    W = [[1+j if a==b else 1-j if (a^1)==b else F(1)
          for b in range(6)] for a in range(6)]
    u,z = F(3,2),2
    beta = 6*epsilon*u**z
    time = 1/beta
    rows = []
    for n in range(1,7):
        first = {x:-1 for x in range(-1,n+2)}
        second = first.copy()
        first[0],second[0] = 0,1
        product_widths = F(1)
        widths = []
        for x in range(1,n+1):
            def acceptance(state):
                value = F(1)
                for y in [x-1,x+1]:
                    if state[y]>=0:
                        value *= W[0][state[y]]
                return value/u**z
            upper,lower = acceptance(first),acceptance(second)
            assert 0 <= lower < upper <= 1
            shared_uniform = (lower+upper)/2
            assert shared_uniform < upper and shared_uniform > lower
            widths.append(upper-lower)
            product_widths *= upper-lower
            first[x] = 0  # only the first copy accepts this content-zero mark
            assert second[x] == -1
        assert widths[0] == 2*j/u**z
        assert all(width == j/u**z for width in widths[1:])
        # Exactly n ordered events at specified sites, no other guard events.
        guard_sites = n+3
        direct_prefactor = (beta*time)**n/F(factorial(n))*F(1,6)**n*product_widths
        asserted_prefactor = 2*(epsilon*j*time)**n/F(factorial(n))
        assert direct_prefactor == asserted_prefactor > 0
        probability = sp.Rational(direct_prefactor)*sp.exp(-sp.Rational(guard_sites*beta*time))
        rows.append({'distance_reached':n,'guard_site_count':guard_sites,
                     'acceptance_interval_widths':[str(x) for x in widths],
                     'favorable_event_probability_exact':str(probability),
                     'favorable_event_probability':float(probability),
                     'new_records_relays':n,'original_record_moves':0})
    return {'epsilon':str(epsilon),'j':str(j),'kappa':'0','beta':str(beta),
            'time':str(time),'fixed_initial_perturbation':'K={0}, content 0 versus 1',
            'cases':rows}


def main():
    result = {'forward_and_backward_footprints':footprint_checks(),
              'shell_and_series':shell_and_series_checks(),
              'birth_only_relay':relay_checks(),
              'versions':{'python':platform.python_version(),'sympy':sp.__version__},
              'all_checks_passed':True}
    text = json.dumps(result,indent=2)+'\n'
    (HERE/'RESULTS.json').write_text(text)
    print(text,end='')


if __name__ == '__main__':
    main()
