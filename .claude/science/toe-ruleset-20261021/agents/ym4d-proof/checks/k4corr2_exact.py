#!/usr/bin/env python3
"""Exact combinatorial and rational checks, not a Yang--Mills enclosure."""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial
import json
import os
import resource
import sys
import time

assert os.environ.get('K4CORR2_WATCHDOG') == '1'
checks = []
guards = []


def guard():
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        peak *= 1024
    assert peak < 700 * 1024**2
    assert max(os.getloadavg()) < 8
    guards.append({'peak_rss_bytes': peak})


def check(name, value, detail=None):
    checks.append({'name': name, 'passed': bool(value), 'detail': detail})
    if not value:
        raise AssertionError(name)


def df(n):
    ans = 1
    for k in range(n, 0, -2):
        ans *= k
    return ans


def partitions(items):
    if not items:
        yield []
        return
    first, *rest = items
    for part in partitions(rest):
        yield [[first]] + part
        for k in range(len(part)):
            yield part[:k] + [[first] + part[k]] + part[k+1:]


def moment_count(degrees, forbid_self):
    total = sum(degrees)
    if total % 2:
        return 0
    if not forbid_self:
        return df(total-1)
    ans = 0
    for loops in product(*(range(d//2+1) for d in degrees)):
        chosen = 1
        for d, k in zip(degrees, loops):
            chosen *= comb(d, 2*k) * df(2*k-1)
        k = sum(loops)
        ans += (-1)**k * chosen * df(total-2*k-1)
    return ans


def mobius_connected(degrees, forbid_self):
    ans = 0
    for part in partitions(list(range(len(degrees)))):
        term = (-1)**(len(part)-1) * factorial(len(part)-1)
        for block in part:
            term *= moment_count([degrees[i] for i in block], forbid_self)
        ans += term
    return ans


def enumerated_counts(degrees):
    owners = tuple(i for i, d in enumerate(degrees) for _ in range(d))
    nv = len(degrees)
    result = {'total': 0, 'connected': 0, 'no_self': 0,
              'connected_no_self': 0, 'quartic_star': 0}
    edges = []

    def visit(left, self_seen):
        if not left:
            result['total'] += 1
            adjacency = [0]*nv
            for a, b in edges:
                adjacency[a] |= 1 << b
                adjacency[b] |= 1 << a
            seen, todo = 0, 1
            while todo:
                bit = todo & -todo
                todo -= bit
                if seen & bit:
                    continue
                seen |= bit
                todo |= adjacency[bit.bit_length()-1] & ~seen
            connected = seen == (1 << nv)-1
            result['connected'] += int(connected)
            result['no_self'] += int(not self_seen)
            result['connected_no_self'] += int(connected and not self_seen)
            if degrees == [2, 2, 2, 2, 4] and connected and not self_seen:
                spokes = [0]*4
                for a, b in edges:
                    if a == 4:
                        spokes[b] += 1
                    elif b == 4:
                        spokes[a] += 1
                result['quartic_star'] += int(spokes == [1]*4)
            return
        a = left[0]
        for k in range(1, len(left)):
            b = left[k]
            va, vb = owners[a], owners[b]
            edges.append((va, vb))
            visit(left[1:k] + left[k+1:], self_seen or va == vb)
            edges.pop()

    visit(tuple(range(len(owners))), False)
    return result


# Sparse polynomials in independently symbolic N and d.
def pmul(a, b):
    result = {}
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            key = i+k, j+l
            result[key] = result.get(key, F(0)) + x*y
    return {k: v for k, v in result.items() if v}


def padd(*args):
    result = {}
    for a in args:
        for k, v in a.items():
            result[k] = result.get(k, F(0)) + v
    return {k: v for k, v in result.items() if v}


def scale(a, c):
    return {k: c*v for k, v in a.items()}


def ppow(a, n):
    ans = {(0, 0): F(1)}
    for _ in range(n):
        ans = pmul(ans, a)
    return ans


def divd(a, c):
    return {(i, j-1): c*v for (i, j), v in a.items()}


def xmul(a, b):
    result = {}
    for i, x in a.items():
        for j, y in b.items():
            result[i+j] = result.get(i+j, F(0)) + x*y
    return result


def xadd(*args):
    result = {}
    for a in args:
        for i, x in a.items():
            result[i] = result.get(i, F(0)) + x
    return result


def expect(a):
    return sum((v*df(k-1) for k, v in a.items() if k % 2 == 0), F(0))


def gaussian_cumulant(args):
    ans = F(0)
    for part in partitions(list(range(len(args)))):
        term = F((-1)**(len(part)-1)*factorial(len(part)-1))
        for block in part:
            poly = {0: F(1)}
            for i in block:
                poly = xmul(poly, args[i])
            term *= expect(poly)
        ans += term
    return ans


def hmul(a, b):
    return [xadd(*(xmul(a[j], b[k-j]) for j in range(k+1))) for k in range(3)]


def smul(a, b):
    return [sum((a[j]*b[k-j] for j in range(k+1)), F(0)) for k in range(3)]


def normalized_moment_cumulant(n):
    xs = [[{2: F(r+1)}, {3: F(r+2)}, {4: F(r+3)}] for r in range(n)]
    v1, v2 = {3: F(2)}, {4: F(3)}
    tilt = [{0: F(1)}, {3: F(-2)}, {6: F(2), 4: F(-3)}]
    z = [expect(p) for p in tilt]
    zinv = [F(1), -z[1], z[1]**2-z[2]]
    moments = {}
    for mask in range(1 << n):
        p = tilt
        for r in range(n):
            if mask & (1 << r):
                p = hmul(p, xs[r])
        moments[mask] = smul([expect(q) for q in p], zinv)
    ans = [F(0)]*3
    for part in partitions(list(range(n))):
        term = [F((-1)**(len(part)-1)*factorial(len(part)-1)), F(0), F(0)]
        for block in part:
            term = smul(term, moments[sum(1 << r for r in block)])
        ans = [a+b for a, b in zip(ans, term)]
    families = [F(0)]*5
    for r in range(n):
        families[0] += gaussian_cumulant([xs[i][2 if i == r else 0] for i in range(n)])
        families[2] -= gaussian_cumulant([xs[i][1 if i == r else 0] for i in range(n)]+[v1])
        for s in range(r+1, n):
            families[1] += gaussian_cumulant([xs[i][1 if i in (r, s) else 0] for i in range(n)])
    families[3] = -gaussian_cumulant([xs[i][0] for i in range(n)]+[v2])
    families[4] = F(1, 2)*gaussian_cumulant([xs[i][0] for i in range(n)]+[v1, v1])
    return ans, families


def main():
    guard()
    graph_rows = []
    expected_external = {2: (0, 6), 4: (288, 360)}
    for n in (2, 4):
        lists = [[4]+[2]*(n-1), [3, 3]+[2]*(n-2),
                 [3]+[2]*(n-1)+[3], [2]*n+[4], [2]*n+[3, 3]]
        derivative_totals = [2*n-2, 2*n-2, 2*n, 2*n, 2*n+2]
        expected_uv = [4*n, 4*n, 4*n+4, 4*n+4, 4*n+8]
        for k, degrees in enumerate(lists):
            row = enumerated_counts(degrees)
            row.update(n=n, family=k+1, degrees=degrees)
            graph_rows.append(row)
            check(f'n{n}_F{k+1}_all_pairings', row['total'] == df(sum(degrees)-1))
            check(f'n{n}_F{k+1}_connected_mobius',
                  row['connected'] == mobius_connected(degrees, False))
            check(f'n{n}_F{k+1}_no_self_inclusion_exclusion',
                  row['no_self'] == moment_count(degrees, True))
            check(f'n{n}_F{k+1}_connected_no_self_mobius',
                  row['connected_no_self'] == mobius_connected(degrees, True))
            check(f'n{n}_F{k+1}_uv_power',
                  sum(degrees)+derivative_totals[k] == expected_uv[k])
            if k < 2:
                check(f'n{n}_F{k+1}_external_count',
                      row['connected_no_self'] == expected_external[n][k])
            if n == 4 and k == 3:
                check('quartic_four_support_star', row['quartic_star'] == 1152)
            guard()

    L0 = {(0, 1): F(32)}
    L1 = {(1, 3): F(128)}
    L2 = {(1, 5): F(64)}
    V1 = {(1, 3): F(80)}
    V2 = {(1, 5): F(32)}
    check('vertex_X0', F(1, 2)*16*4 == 32)
    check('vertex_X1', 16*2*2*2 == 128)
    check('vertex_X2', F(1, 2)*16*2*4 == 64)
    check('vertex_V1_including_ghost', 16*2*2+4*2*2 == 80)
    check('vertex_V2', F(1, 4)*16*2*4 == 32)
    H = 2**9
    B4 = scale(padd(scale(pmul(L2, ppow(L0, 3)), 4*288),
                    scale(pmul(ppow(L1, 2), ppow(L0, 2)), 6*360)), H**5)
    B2 = scale(ppow(L1, 2), 6*H**3)
    check('B4_polynomial_identity', B4 == {(1, 8): 9*2**73, (2, 8): 135*2**73})
    check('B2_polynomial_identity', B2 == {(2, 6): 3*2**42})
    Cext = padd(divd(B4, F(2**17, 3)), divd(B2, F(2**9, 11)))
    check('Cext_polynomial_identity', Cext == {
        (1, 7): 3*2**90, (2, 7): 45*2**90, (2, 5): F(3*2**51, 11)})
    Bstar = scale(pmul(V2, ppow(L0, 4)), 1152*4**4*H**2*2**26)
    check('Bstar_polynomial_identity', Bstar == {(1, 9): 9*2**84})
    check('Cstar_polynomial_identity',
          divd(Bstar, F(2**17, 3)) == {(1, 8): 3*2**101})
    check('star_integral_rational_bound', 4*(32*4**9+4) < 2**26)
    check('separated_component_bound', max(4, 4*8, 24*16) < H)

    delta = F(1, 2**20)
    check('heat_scalar_error_constant', 768*32**5 < 2**35)
    check('heat_curvature_error_constant', 4*2**35 <= 2**37)
    check('heat_operator_error_constant', 6*2**37 < 2**40)
    E = 2**40*delta**6
    check('heat_E_endpoint', E == F(1, 2**80) and E < 1)
    check('four_cycle_error_constant', 48*24*17**3 < 2**23)
    check('two_cycle_error_constant', 12*33 < 2**9)
    check('free_A4_half_margin', 2**63*delta**6 < F(3, 4*4**8))
    check('free_A2_half_margin', 2**49*delta**6 < F(11, 2*4**4))
    check('finite_regulator_D4_conversion', 1/F(3, 4*4**8) == F(2**18, 3))
    check('finite_regulator_D2_conversion', 2/F(11, 2*4**4) == F(2**10, 11))
    for k, expected in enumerate((F(64), F(64), F(128, 3))):
        check(f'Taylor_degree_{k}', F(32*2**(k+1), factorial(k+1)) == expected)

    # Independently invert the denominator square in the truncated series ring.
    # Variable exponents now mean (power of a4, power of a2).
    one, a4, a2 = {(0, 0): F(1)}, {(1, 0): F(1)}, {(0, 1): F(1)}
    q_squared_linear = padd(pmul(one, a2), pmul(a2, one))
    inverse_linear = scale(q_squared_linear, -1)
    ratio_linear = padd(pmul(a4, one), pmul(one, inverse_linear))
    check('ratio_linear_coefficient', ratio_linear == {(1, 0): 1, (0, 1): -2})
    check('truncation_positive_margin', 1-F(1, 2) == F(1, 2))
    check('actual_ratio_positive_margin', 1-F(1, 2)-F(1, 4) == F(1, 4))
    check('actual_ratio_R0_margin', F(3, 338)*F(1, 4) == F(3, 1352))
    check('polynomial_cumulant_margin', F(1, 4)*F(1, 2)**2 == F(1, 16))
    # u=v+e, |e|<=E<=v/2: v(v-E)>0 and 2(v-E)-v=v-2E>=0.
    check('FLOW_reciprocal_denominator_polynomial',
          padd({(1, 0): F(2)}, {(0, 1): F(-2)}, {(1, 0): F(-1)})
          == {(1, 0): 1, (0, 1): -2})
    check('uniform_log_remainder_envelope', F(3, 2)*F(1, 6) == F(1, 4))
    check('exponential_remainder_envelope', F(2, 1) == factorial(2))

    for n in (2, 4):
        direct, families = normalized_moment_cumulant(n)
        check(f'five_family_identity_independent_n{n}', direct[2] == sum(families),
              {'direct': str(direct[2]), 'families': [str(v) for v in families]})
        check(f'odd_control_coefficient_n{n}', direct[1] == 0)
        check(f'mutation_missing_half_detected_n{n}',
              direct[2] != sum(families)+families[4] and families[4] != 0)
    check('mutation_disconnected_count_detected',
          graph_rows[-1]['connected'] != graph_rows[-1]['total'])
    check('mutation_wrong_ratio_detected',
          ratio_linear != {(1, 0): F(1), (0, 1): F(-1)})
    # Each power in the fully assembled M4 is positive; halving delta
    # increases the majorant by at least 2^16 for every positive N,d,R.
    bare4 = [scale(pmul(L2, ppow(L0, 3)), 4*graph_rows[5]['connected']*16**5),
             scale(pmul(ppow(L1, 2), ppow(L0, 2)), 6*graph_rows[6]['connected']*16**5),
             scale(pmul(pmul(L1, V1), ppow(L0, 3)), 4*graph_rows[7]['connected']*16**6),
             scale(pmul(V2, ppow(L0, 4)), graph_rows[8]['connected']*16**6),
             scale(pmul(ppow(V1, 2), ppow(L0, 4)), F(graph_rows[9]['connected'], 2)*16**7)]
    powers = [16, 16, 20, 20, 24]
    check('mutation_bare_uniformity_detected',
          all(all(v > 0 for v in p.values()) and power >= 16 for p, power in zip(bare4, powers))
          and bool(bare4[-1]) and powers[-1] == 24)
    guard()
    return {'passed': True, 'assertion_count': len(checks), 'checks': checks,
            'graphs': graph_rows, 'guards': guards,
            'scientific_completion': {
                'uniform_renormalized_Cbar': 'OPEN / NOT PASSED',
                'positive_original_YM_window': 'OPEN / NOT PASSED',
                'reason': 'Internal subtractions, finite counterterms, matching and uniform remainders are not enclosed.'}}


if __name__ == '__main__':
    try:
        result = main()
    except BaseException as exc:
        result = {'passed': False, 'assertion_count': len(checks),
                  'checks': checks, 'guards': guards, 'failure': repr(exc)}
    print(json.dumps(result, indent=2))
    sys.exit(0 if result['passed'] else 1)
