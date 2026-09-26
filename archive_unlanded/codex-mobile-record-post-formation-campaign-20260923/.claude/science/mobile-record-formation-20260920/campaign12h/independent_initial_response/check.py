#!/usr/bin/env python3
"""Independent exact finite-state initial-response check; no primary imports."""
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import json


def prod(xs):
    out = F(1)
    for x in xs:
        out *= x
    return out


def case(name, n, edges, chi, W, theta, rhos):
    chi = tuple(map(F, chi))
    W = tuple(tuple(map(F, row)) for row in W)
    assert all(x > 0 for row in W for x in row)
    assert all(sum(row) == 6 for row in W)
    assert all(W[a][b] == W[b][a] for a in range(6) for b in range(6))
    assert sum(chi) == 0
    assert all(sum(W[a][b] * chi[b] for b in range(6)) == theta * chi[a]
               for a in range(6))
    adj = [[] for _ in range(n)]
    for x, y in edges:
        adj[x].append(y)
        adj[y].append(x)
    z = len(adj[0])
    assert all(len(a) == z for a in adj)
    s2 = sum(x*x for x in chi) / 6
    s3 = sum(x*x*x for x in chi) / 6
    epsilon = F(1, 7)
    fields = ['mass', 'M', 'N', 'M2', 'H', 'GM', 'GN', 'GM2', 'GH', 'bracket']
    totals = {rho: {key: [F(0), F(0)] for key in fields} for rho in rhos}
    hop_count = birth_count = 0

    def obs(s):
        N = sum(a >= 0 for a in s)
        M = sum(chi[a] for a in s if a >= 0)
        return (M, F(N), M*M, M / N if N else F(0))

    def weight(s):
        return prod(W[s[x]][s[y]] for x, y in edges if s[x] >= 0 and s[y] >= 0)

    for s in product(range(-1, 6), repeat=n):
        M, N, M2, H = obs(s)
        generators = [F(0)] * 4
        bracket = F(0)
        B = F(0)
        J = F(0)
        D = F(0)
        for x, y in edges:
            if (s[x] < 0) != (s[y] < 0):
                t = list(s)
                t[x], t[y] = t[y], t[x]
                rate = weight(t) / (weight(s) + weight(t))
                out = obs(t)
                assert out == (M, N, M2, H)
                for k in range(4):
                    generators[k] += rate * (out[k] - (M, N, M2, H)[k])
                hop_count += 1
        for x in range(n):
            if s[x] >= 0:
                continue
            for a in range(6):
                u = prod(W[a][s[y]] for y in adj[x] if s[y] >= 0)
                B += u
                J += chi[a] * u
                D += chi[a]**2 * u
                t = list(s)
                t[x] = a
                out = obs(t)
                for k in range(4):
                    generators[k] += epsilon * u * (out[k] - (M, N, M2, H)[k])
                bracket += epsilon * u * (out[0] - M)**2
                birth_count += 1
        GM, GN, GM2, GH = generators
        assert GM == epsilon * J
        assert GN == epsilon * B
        assert GM2 == epsilon * (2 * M * J + D)
        assert bracket == epsilon * D == GM2 - 2 * M * GM
        assert GH == epsilon * (J - H * B) / (N + 1)
        values = [F(1), M, N, M2, H, GM, GN, GM2, GH, bracket]
        for rho in rhos:
            p0 = prod(1-rho if a < 0 else rho/6 for a in s)
            # d/dh product_a(1+h chi(a)) at h=0 is the total M.
            p1 = p0 * M
            for key, value in zip(fields, values):
                totals[rho][key][0] += p0 * value
                totals[rho][key][1] += p1 * value

    rows = []
    for rho in rhos:
        q = 1-rho
        expected = {
            'mass': (1, 0), 'M': (0, n*rho*s2), 'N': (n*rho, 0),
            'M2': (n*rho*s2, n*rho*s3),
            'H': (0, s2*(1-q**n)),
            'GM': (0, epsilon*n*z*theta*rho*q*s2),
            'GN': (6*epsilon*n*q, 0),
            'GM2': (epsilon*n*q*s2*(6+2*z*rho*theta),
                    epsilon*n*q*s3*(3*z*rho*theta+F(1,3)*z*(z-1)*rho*rho*theta*theta)),
            'bracket': (6*epsilon*n*q*s2, epsilon*n*q*z*rho*theta*s3),
        }
        # Hypergeometric construction, valid also for n=1,2 and rho=0,1.
        ratio_response = F(0)
        for k in range(1, n):
            pk = F(comb(n-1, k)) * rho**k * q**(n-1-k)
            for ell in range(max(0, k-(n-1-z)), min(k, z)+1):
                pell = F(comb(z, ell)*comb(n-1-z, k-ell), comb(n-1, k))
                ratio_response += pk * pell * (
                    ell*theta - 6 - F(ell*(ell-1), 6*k)*theta*theta
                ) / (k+1)
        ratio_response *= epsilon*n*q*s2
        expected['GH'] = (0, ratio_response)
        for key, target in expected.items():
            assert tuple(totals[rho][key]) == tuple(target), (name, rho, key, totals[rho][key], target)
        record = {'rho': str(rho), 'exact_sums': {k: list(map(str,v)) for k,v in totals[rho].items()}}
        if rho > 0:
            response_of_ratio = ((totals[rho]['GM'][1]*totals[rho]['N'][0]
                                  - totals[rho]['M'][1]*totals[rho]['GN'][0])
                                 / totals[rho]['N'][0]**2)
            assert response_of_ratio == epsilon*q*s2*(z*theta-6/rho)
            record['ratio_of_expectations_response'] = str(response_of_ratio)
            P = 1-q**n
            conditional_response = (ratio_response-s2*6*epsilon*n*q**n)/P
            record['conditional_expected_ratio_response'] = str(conditional_response)
            if n >= 3:
                U = P/(n*rho)
                p = q**(n-1)
                closed = epsilon*n*q*s2*(
                    F(z,n-1)*theta*(1-U)-6*(U-p)
                    - F(z*(z-1),6*(n-1)*(n-2))*theta**2*(1+p-2*U))
                assert ratio_response == closed
                record['closed_expected_ratio_response'] = str(closed)
        rows.append(record)
    return {'case': name, 'n': n, 'degree': z, 'theta': str(theta),
            'chi': list(map(str, chi)), 'sigma2': str(s2), 'sigma3': str(s3),
            'states': 7**n, 'explicit_hop_transitions': hop_count,
            'explicit_birth_transitions': birth_count, 'rows': rows}


def rank_matrix(chi, coefficient, extra=None):
    return [[F(1)+coefficient*chi[a]*chi[b]
             +(F(1,10)*extra[a]*extra[b] if extra else 0)
             for b in range(6)] for a in range(6)]


def main():
    c = [2,-1,-1,0,0,0]
    e = [0,0,0,1,-1,0]
    positive = rank_matrix(c, F(1,4), e)
    negative = rank_matrix(c, F(-1,8), e)
    zero = [[F(1)]*6 for _ in range(6)]
    balanced = [1,1,1,-1,-1,-1]
    strong = rank_matrix(balanced, F(4,5))
    rho_values = [F(0), F(1,4), F(2,3), F(1)]
    results = [
        case('singleton_positive', 1, [], c, positive, F(3,2), rho_values),
        case('edge_positive', 2, [(0,1)], c, positive, F(3,2), rho_values),
        case('triangle_positive', 3, [(0,1),(1,2),(0,2)], c, positive, F(3,2), rho_values),
        case('cycle4_positive', 4, [(0,1),(1,2),(2,3),(0,3)], c, positive, F(3,2), rho_values),
        case('triangle_negative', 3, [(0,1),(1,2),(0,2)], c, negative, F(-3,4), rho_values),
        case('cycle4_uniform', 4, [(0,1),(1,2),(2,3),(0,3)], c, zero, F(0), rho_values),
        case('cycle4_opposite_ratio_signs', 4, [(0,1),(1,2),(2,3),(0,3)], balanced, strong, F(24,5), [F(3,4)]),
    ]
    example = results[-1]['rows'][0]
    assert example['ratio_of_expectations_response'] == str(F(2,35))
    assert example['exact_sums']['GH'][1] == str(F(-27,896))
    assert example['conditional_expected_ratio_response'] == str(F(-26,595))
    U = F(85,256)
    p = F(1,64)
    wrong_without_hazard_correlation = F(1,7)*(F(16,5)*(1-U)-6*(U-p))
    assert wrong_without_hazard_correlation == F(153,4480)
    assert wrong_without_hazard_correlation-F(example['exact_sums']['GH'][1]) == F(9,140)
    psi = [0,1,-1,0,0,0]
    W_kernel = rank_matrix(psi, F(1,2))
    assert all(sum(W_kernel[a][b]*c[b] for b in range(6)) == 0 for a in range(6))
    two_neighbor_J = sum(c[a]*W_kernel[a][1]**2 for a in range(6))
    assert two_neighbor_J == F(-1,2)
    # Falsifiers: omitting six uniform birth channels, the second-moment jump
    # square, or replacing E[M/N] by E[M]/E[N] fails an explicit rational value.
    falsifiers = {
        'ratio_normalizations_can_have_opposite_signs': {
            'epsilon': '1/7', 'ratio_of_expectations': '2/35',
            'expectation_of_ratio_zero_on_empty': '-27/896',
            'conditional_expectation_of_ratio': '-26/595'},
        'uniform_birth_hazard_is_six_per_empty_site': True,
        'empty_state_second_moment_drift': '6 epsilon n sigma2; not zero',
        'nonzero_third_content_moment_checked': True,
        'omitting_theta_squared_term_fails_cycle4_strong': {
            'incorrect_value': str(wrong_without_hazard_correlation),
            'actual_value': example['exact_sums']['GH'][1]},
        'zero_eigenvalue_does_not_imply_pointwise_content_conservation': {
            'chi': c, 'psi': psi, 'W': '1+(1/2) psi psi^T',
            'state_on_triangle': [-1,1,1], 'J': str(two_neighbor_J)},
    }
    output = {'status': 'all exact checks passed',
              'cases': results, 'falsifiers': falsifiers,
              'total_state_cases': sum(r['states'] for r in results),
              'initial_laws_checked': sum(len(r['rows']) for r in results)}
    text = json.dumps(output, indent=2)+'\n'
    (Path(__file__).parent/'RESULTS.json').write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()
