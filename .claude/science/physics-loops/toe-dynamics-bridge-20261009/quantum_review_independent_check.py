#!/usr/bin/env python3
"""Review-owned exact checks. No imports from the author discriminator.

The dilation is reconstructed as a polynomial of its joint skew generator,
not by filling the author's two-state rotation blocks. A different N=5
projector census checks normalization. Formal polynomials expose finite-order
schedule asymmetry; a rational lower bound tests the necessity of time-floor
control. These finite checks supplement the independent written argument.
"""

from fractions import Fraction as F
from itertools import product, combinations


def zeros(n):
    return [[F(0) for _ in range(n)] for _ in range(n)]


def identity(n):
    out = zeros(n)
    for i in range(n):
        out[i][i] = F(1)
    return out


def mul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return list(map(list, zip(*a)))


def linear(*terms):
    n = len(terms[0][1])
    return [[sum(c*a[i][j] for c, a in terms) for j in range(n)] for i in range(n)]


def dilation_check():
    # A genuine partial injection with overlapping source/target subspaces,
    # a nontrivial cycle, and a directed edge. It is not a symmetric swap.
    mapping = {0: 1, 1: 2, 2: 0, 3: 4}
    d = 5
    J = zeros(d)
    for source, target in mapping.items():
        J[target][source] = F(1)
    P = mul(transpose(J), J)
    A = zeros(2*d)
    for x in range(d):
        for y in range(d):
            A[2*x+1][2*y] = J[x][y]
            A[2*x][2*y+1] = -J[y][x]
    A2 = mul(A, A)
    assert mul(A2, A) == linear((-1, A))
    co, si = F(12, 13), F(5, 13)
    W = linear((1, identity(2*d)), (si, A), (1-co, A2))
    assert mul(transpose(W), W) == identity(2*d)
    K0 = [[W[2*x][2*y] for y in range(d)] for x in range(d)]
    K1 = [[W[2*x+1][2*y] for y in range(d)] for x in range(d)]
    assert K0 == linear((1, identity(d)), (co-1, P))
    assert K1 == linear((si, J))
    assert linear((1, mul(transpose(K0), K0)),
                  (1, mul(transpose(K1), K1))) == identity(d)
    for a, b in product(range(d), repeat=2):
        joint = zeros(2*d)
        joint[2*a][2*b] = F(1)
        output = mul(mul(W, joint), transpose(W))
        reduced = [[output[2*x][2*y]+output[2*x+1][2*y+1]
                    for y in range(d)] for x in range(d)]
        expected = [F(int(a == b == x)) for x in range(d)]
        if a == b and a in mapping:
            expected[a] -= si**2
            expected[mapping[a]] += si**2
        assert [reduced[x][x] for x in range(d)] == expected
    print('Joint-generator polynomial: 10x10 exact unitary; all 25 matrix-unit populations close.')
    print('Derived Kraus pair I+(cos-1)P, sin*J; proper partial injection, cos=12/13.')


def projector_count_check():
    N, w = 5, F(1, 27)
    Omega = N*w
    c, kappa = F(7, 11), F(13, 17)
    gamma = c*kappa/(2*Omega)
    states = tuple(product(range(2), range(3)))  # two cells; i, j, spectator
    compared = 0
    nonzero = 0
    for config in product(states, repeat=N):
        for cell in range(2):
            projector_value = sum(
                int(config[a] == (cell, 0) and config[b] == (cell, 1)) +
                int(config[a] == (cell, 1) and config[b] == (cell, 0))
                for a, b in combinations(range(N), 2))
            ni = config.count((cell, 0))
            nj = config.count((cell, 1))
            assert projector_value == ni*nj
            outgoing = 2*gamma*projector_value
            density_drift = outgoing/Omega
            mass_action = c*kappa*F(ni, Omega)*F(nj, Omega)
            assert density_drift == mass_action
            if mass_action:
                assert 2*density_drift != mass_action
                assert density_drift/2 != mass_action
                nonzero += 1
            compared += 1
    print(f'N=5 pair-projector census: {compared} cell configurations; {nonzero} nonzero reactions.')
    print(f'gamma=c*kappa/(2*N*w)={gamma}; doubled or halved rates rejected when active.')


def padd(a, b):
    return tuple((a[i] if i < len(a) else F(0)) +
                 (b[i] if i < len(b) else F(0))
                 for i in range(max(len(a), len(b))))


def pscale(c, a):
    return tuple(c*x for x in a)


def pmul(a, b):
    out = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def schedule_check():
    p, one_minus_p = (F(0), F(1)), (F(1), F(-1))
    results = []
    for start in (0, 1):
        values = [(F(int(start == i)),) for i in range(4)]
        for a, b in ((0, 2), (0, 3), (1, 2), (1, 3)):
            old_a, old_b = values[a], values[b]
            values[a] = padd(pmul(one_minus_p, old_a), pmul(p, old_b))
            values[b] = padd(pmul(p, old_a), pmul(one_minus_p, old_b))
        results.append(padd(values[2], values[3]))
    difference = padd(results[0], pscale(-1, results[1]))
    assert results[0][1] == results[1][1] == 2
    assert difference[0] == difference[1] == 0
    assert difference[2] != 0
    print('Finite ordered-schedule target probability coefficients, ascending powers of p:')
    print(f'  input orientation 1: {results[0]}')
    print(f'  input orientation 2: {results[1]}')
    print(f'  difference: {difference}; equal infinitesimal rates, unequal finite occupation laws.')


def norm_and_time_floor_checks():
    first_order_remainder = 2*F(1, 24) + F(1, 4) + F(1, 3)
    local_total = first_order_remainder + 2
    assert first_order_remainder == F(2, 3)
    assert local_total == F(8, 3)
    assert 4 <= 2*local_total
    # For q=Lambda=1, T=h/2, there are zero scheduled macrosteps.
    # A directed jump from its source gives trace distance 2(1-exp(-T)).
    # The exponential alternating bound gives the rigorous rational lower
    # bound 2*T-T*T. Omitting the floor term violates the proposed rate.
    h, T = F(1, 16), F(1, 32)
    assert h <= F(1, 4)
    error_lower = 2*T-T*T
    without_floor = F(8, 3)*T*h
    full_bound = without_floor+2*h
    assert error_lower > without_floor
    assert error_lower < full_bound
    print(f'Taylor norm arithmetic: {first_order_remainder} + 2 = {local_total}; pair splitting 4 fits 2*(8/3).')
    print(f'Time-floor discriminator h={h}, T={T}: error >= {error_lower} > omitted-floor bound {without_floor}.')
    print(f'Including the declared 2*h*Lambda gives {full_bound}.')


if __name__ == '__main__':
    dilation_check()
    projector_count_check()
    schedule_check()
    norm_and_time_floor_checks()
    print('Review-owned finite checks complete. All-size and diamond conclusions use the written derivation.')
