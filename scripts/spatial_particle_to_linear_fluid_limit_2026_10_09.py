#!/usr/bin/env python3
"""Finite author controls for the simultaneous supplied particle/fluid theorem.

Exact rational collision, preparation and weighted jump calculations;
floating-point finite Fourier controls are supplementary. No repository
imports, external data or general stochastic/PDE theorem from sampling.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement, product
from math import lcm, pi, prod, sin, sqrt
from cmath import exp as cexp

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = [
    'docs/SPATIAL_PARTICLE_TO_LINEAR_FLUID_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-09.md',
    'docs/SUPPLIED_FINITE_VELOCITY_COLLISIONS_AND_GIBBS_EQUILIBRATION_BOUNDED_THEOREM_NOTE_2026-10-08.md',
    'docs/D3Q27_DISSIPATIVE_HYDRODYNAMIC_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-10-09.md',
    'docs/SPATIAL_QUANTUM_COLLISION_REALIZATION_BOUNDED_THEOREM_NOTE_2026-10-09.md',
]


def network():
    v = tuple(product((-1, 0, 1), repeat=3))
    e = [sum(t*t for t in row) for row in v]
    M = [F(2, 3)**(3-u)*F(1, 6)**u for u in e]
    groups = defaultdict(list)
    for i, j in combinations_with_replacement(range(27), 2):
        key = tuple(v[i][d]+v[j][d] for d in range(3))+(e[i]+e[j],)
        groups[key].append((i, j))
    reactions = [tuple(sorted((ij, kl))) for g in groups.values()
                 for ij, kl in combinations(g, 2)]
    # Construct the nine special exchanges geometrically, without selecting
    # them by the pair-difference predicate used in the parent runner.
    vi = {row: i for i, row in enumerate(v)}
    special = set()
    for remaining in range(3):
        axes = [d for d in range(3) if d != remaining]
        for s in (-1, 0, 1):
            pairs = []
            for axis in axes:
                rows = []
                for sign in (-1, 1):
                    row = [0]*3
                    row[remaining], row[axis] = s, sign
                    rows.append(vi[tuple(row)])
                pairs.append(tuple(sorted(rows)))
            special.add(tuple(sorted(pairs)))
    assert len(reactions) == 288 and len(special) == 9
    assert special <= set(reactions)
    assert all(len(set(ij+kl)) == 4 and M[ij[0]]*M[ij[1]] == M[kl[0]]*M[kl[1]]
               for ij, kl in reactions)
    base = sum(M[i]*M[j]*sum(1/M[t] for t in (i, j, k, l))
               for (i, j), (k, l) in reactions if ((i, j), (k, l)) not in special)
    slope = sum(M[i]*M[j]*sum(1/M[t] for t in (i, j, k, l))
                for (i, j), (k, l) in special)
    assert (base, slope) == (F(124, 3), F(4, 3))
    assert sum(M) == 1 and min(M) == F(1, 216)
    alpha = F(7, 3)  # A rational supplied rate for exact finite controls.
    rates = [alpha if r in special else F(1) for r in reactions]
    cr = base+slope*alpha
    print(f'network: 288 reactions, 9 geometric axial exchanges; C_R(alpha)={base}+{slope}*alpha')
    return v, e, M, reactions, rates, cr


def collision_controls(M, reactions, rates):
    h = [F((11*i+3) % 17-8, 9) for i in range(27)]
    g = [F((7*i+1) % 13-6, 5) for i in range(27)]
    amplitude = F(2, 13)
    f = [m*(1+amplitude*t) for m, t in zip(M, h)]
    q, bh, gamma, mixed = ([F(0)]*27 for _ in range(4))
    squares = F(0)
    for ((i, j), (k, l)), rate in zip(reactions, rates):
        nu = ((i, -1), (j, -1), (k, 1), (l, 1))
        nh = h[k]+h[l]-h[i]-h[j]
        direct = rate*(f[i]*f[j]-f[k]*f[l])
        linear = rate*M[i]*M[j]*nh
        quadratic = rate*M[i]*M[j]*(h[i]*h[j]-h[k]*h[l])
        bilinear = rate*M[i]*M[j]*(h[i]*g[j]+h[j]*g[i]-h[k]*g[l]-h[l]*g[k])/2
        for t, sign in nu:
            q[t] += sign*direct
            bh[t] += sign*linear/M[t]
            gamma[t] += sign*quadratic/M[t]
            mixed[t] += sign*bilinear/M[t]
        squares += rate*M[i]*M[j]*nh*nh
    reconstructed = [m*(-amplitude*b+amplitude**2*c) for m, b, c in zip(M, bh, gamma)]
    assert q == reconstructed
    assert sum(m*x*b for m, x, b in zip(M, h, bh)) == squares > 0
    cr = sum(rate*M[i]*M[j]*sum(1/M[t] for t in (i, j, k, l))
             for ((i, j), (k, l)), rate in zip(reactions, rates))
    mixed_norm_sq = sum(m*t*t for m, t in zip(M, mixed))
    upper_sq = (cr/2)**2 * max(abs(t) for t in h)**2 * sum(m*t*t for m, t in zip(M, g))
    assert mixed_norm_sq <= upper_sq
    print('collision: exact nonlinear expansion, weighted edge-square identity and bilinear bound')


def weighted_population_controls(v, energy, M, reactions, rates, cr):
    m, w, ell = 3, F(1, 27), F(2, 3)  # Side 2 rational instance; normalized weight differs.
    cells = tuple(product(range(m), repeat=3))
    cell_index = {x: z for z, x in enumerate(cells)}
    a, delta = F(1, 12), F(2, 5)
    U = [F((1, -1, 0)[x[0]])*(F(5-3*energy[i], 2)+v[i][1])
         for x in cells for i in range(27)]
    probs = [w*M[i]*(1+a*U[27*z+i]) for z in range(27) for i in range(27)]
    assert sum(probs) == 1 and min(probs) > 0
    N = lcm(*(p.denominator for p in probs))
    counts = [int(N*p) for p in probs]
    assert sum(counts) == N and all(F(n, N) == p for n, p in zip(counts, probs))
    assert all(F(n, N*w) <= 2*M[i % 27] for i, n in enumerate(counts))
    metric = [w*M[i] for _ in cells for i in range(27)]
    jump_scale = [1/(N*w*a*M[i]) for _ in cells for i in range(27)]
    hop, collision = F(0), F(0)
    for z, x in enumerate(cells):
        for i, velocity in enumerate(v):
            at = 27*z+i
            for d, direction in enumerate(velocity):
                if not direction:
                    continue
                y = list(x); y[d] = (y[d]+direction) % m
                target = 27*cell_index[tuple(y)]+i
                rate = abs(direction)*counts[at]/(delta*ell)
                hop += rate*(metric[at]*jump_scale[at]**2+metric[target]*jump_scale[target]**2)
        for ((i, j), (k, l)), coefficient in zip(reactions, rates):
            for aa, bb in ((i, j), (k, l)):
                rate = coefficient*counts[27*z+aa]*counts[27*z+bb]/(delta**2*N*w)
                collision += rate*sum(metric[27*z+t]*jump_scale[27*z+t]**2 for t in (i, j, k, l))
    # Separate bracket formula in terms of densities and reaction supports.
    density = [F(n, N*w) for n in counts]
    hop_formula = 2/(N*a*a*delta*ell)*sum(
        sum(abs(t) for t in v[i])*density[27*z+i]/M[i]
        for z in range(27) for i in range(27))
    coll_formula = 1/(N*a*a*delta**2)*sum(
        coefficient*(density[27*z+i]*density[27*z+j]+density[27*z+k]*density[27*z+l])
        *sum(1/M[t] for t in (i, j, k, l))
        for z in range(27) for ((i, j), (k, l)), coefficient in zip(reactions, rates))
    assert hop == hop_formula and collision == coll_formula
    assert hop <= F(216)/(N*w*a*a*delta*ell)
    assert collision <= 8*cr/(N*w*a*a*delta**2)
    # E||X-E X||^2 from one categorical draw, then divide by N. X has
    # one nonzero density coordinate; this avoids the covariance formula.
    expected_norm_sq = sum(p/(w*a*a*M[j % 27]) for j, p in enumerate(probs))
    mean_norm_sq = sum(p*p/(w*a*a*M[j % 27]) for j, p in enumerate(probs))
    initial = (expected_norm_sq-mean_norm_sq)/N
    covariance_trace = sum(p*(1-p)/(N*w*a*a*M[j % 27]) for j, p in enumerate(probs))
    assert initial == covariance_trace <= 54/(N*w*a*a)
    print(f'weighted population: N={N}, 27 cells; direct jump QV=({hop}, {collision})')
    print(f'initial preparation: exact mass/positivity and multinomial weighted variance={initial}')


def fourier_controls():
    alias_cases = mode_cases = 0
    for m in (3, 5):
        half = (m-1)//2
        modes = tuple(product(range(-half, half+1), repeat=3))
        for p in modes:
            for q in modes:
                k = tuple((u+v+half) % m-half for u, v in zip(p, q))
                norm = lambda row: sum(t*t for t in row)
                assert norm(k) <= norm(tuple(u+v for u, v in zip(p, q)))
                assert (1+norm(k))**2 <= 8*((1+norm(p))**2+(1+norm(q))**2)
                alias_cases += 1
        ell = 2*pi/m
        for k in modes:
            kk = sum(t*t for t in k)
            sinc_product = prod(sin(t*ell/2)/(t*ell/2) if t else 1 for t in k)
            interp_sq = 2*(1-sinc_product)  # Exact cell integral for this Fourier mode.
            assert -1e-14 <= interp_sq <= 3*ell*ell*kk+1e-14
            for v in product((-1, 0, 1), repeat=3):
                symbol = sum((cexp(-1j*s*k[d]*ell)-1)/ell
                             for d, s in enumerate(v) if s)
                continuum = -1j*sum(s*t for s, t in zip(v, k))
                assert symbol.real <= 1e-14
                assert abs(symbol-continuum) <= ell*kk/2+1e-13
                mode_cases += 1
    # Independent quadrature of a three-mode field exercises the actual
    # piecewise-constant interpolation, including cross-mode cancellation.
    m, subdivisions = 3, 12
    ell = 2*pi/m
    chosen = ((1, 0, 0), (0, 1, -1), (-1, 1, 0))
    coefficients = (1, 1+1j, -1j/3)
    field = lambda x: sum(c*cexp(1j*sum(kd*xd for kd, xd in zip(k, x)))
                          for c, k in zip(coefficients, chosen))
    integral = 0.0
    for z in product(range(m), repeat=3):
        center = tuple(ell*t for t in z)
        frozen = field(center)
        for u in product(range(subdivisions), repeat=3):
            point = tuple(x+ell*((t+0.5)/subdivisions-0.5) for x, t in zip(center, u))
            integral += abs(frozen-field(point))**2
    integral /= (m*subdivisions)**3
    phase_formula = sum(abs(c)**2*2*(1-prod(sin(kd*ell/2)/(kd*ell/2) if kd else 1 for kd in k))
                        for c, k in zip(coefficients, chosen))
    assert abs(integral-phase_formula) < 0.01
    shell_upper = 1+24*F(6, 5)+2*F(8, 7)
    assert shell_upper == F(1123, 35) < 36
    print(f'Fourier controls: {alias_cases} exact alias pairs, {mode_cases} float symbol tests; exact shell majorant={shell_upper}')
    print(f'Interpolation: independent midpoint integral={integral:.9g}, exact-phase formula={phase_formula:.9g}; finite float control, not an enclosure.')


def scaling_controls():
    # Exponents are derived by balancing each displayed term. Positive power
    # means decay as delta -> 0; these calculations do not prove a limit alone.
    amp, cell, mesh, count, step = 3, 6, 2, -23, 76
    nonlinear = amp-2
    discretization = mesh-1
    noise = cell/2
    failure = min(-1-mesh, -2)-(count+2*cell+2*amp)
    mark_rate = min(count-1-cell-mesh, count-2-2*cell)
    quantum = min(step+2*mark_rate, step+mark_rate)
    assert min(nonlinear, discretization, noise, 1, 2) == 1
    assert failure == quantum == 2 and mark_rate == -37
    assert step+mark_rate > 0
    alpha = (-4579+3*sqrt(7614177))/1072
    assert alpha > 1
    print(f'scaling: classical error power>=1, failure={failure}, Lambda power={mark_rate}, gate error={quantum}')
    print(f'tuned positive axial rate={alpha:.12g}; sufficient exponents, no optimality or physical scaling claim')


def main():
    v, e, M, reactions, rates, cr = network()
    collision_controls(M, reactions, rates)
    weighted_population_controls(v, e, M, reactions, rates, cr)
    fourier_controls()
    scaling_controls()
    print('Finite author controls completed; analytic stochastic/Sobolev/fluid claims rely on the written proofs.')


if __name__ == '__main__':
    main()
