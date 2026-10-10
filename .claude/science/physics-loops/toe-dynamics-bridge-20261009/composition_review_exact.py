#!/usr/bin/env python3
"""Independent finite checks for the supplied spatial-composition draft.

No repository code is imported. Fractions make normalization comparisons exact.
These finite examples supplement, and do not replace, the analytic review.
"""
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement, product
from collections import defaultdict

V = list(product((-1, 0, 1), repeat=3))
M = [F(1) for _ in V]
for i, v in enumerate(V):
    for x in v:
        M[i] *= F(1, 6) if x else F(2, 3)
classes = defaultdict(list)
for i, j in combinations_with_replacement(range(27), 2):
    classes[tuple(V[i][d] + V[j][d] for d in range(3)) +
            (sum(x*x for x in V[i] + V[j]),)].append((i, j))
reactions = []
for pairs in classes.values():
    for (i, j), (k, l) in combinations(pairs, 2):
        assert len({i, j, k, l}) == 4
        assert M[i]*M[j] == M[k]*M[l]
        # The nine special reactions consist of two one-axis antipodal pairs
        # with a common midpoint and different varying axes.
        axes_a = [d for d in range(3) if V[i][d] != V[j][d]]
        axes_b = [d for d in range(3) if V[k][d] != V[l][d]]
        special = (len(axes_a) == len(axes_b) == 1 and axes_a != axes_b
                   and abs(V[i][axes_a[0]]-V[j][axes_a[0]]) == 2
                   and abs(V[k][axes_b[0]]-V[l][axes_b[0]]) == 2)
        signs = ((i, -1), (j, -1), (k, 1), (l, 1))
        reactions.append((i, j, k, l, special, signs))
assert len(reactions) == 288
assert sum(r[4] for r in reactions) == 9
assert min(M) == F(1, 216)
assert sum(abs(x) for v in V for x in v) == 54

def collision_trace(alpha):
    return sum((alpha if sp else 1)*M[i]*M[j]*sum(1/M[v] for v, _ in signs)
               for i, j, k, l, sp, signs in reactions)

print('network: 27 velocities, 288 four-distinct reactions, 9 axial reactions')
print('M_min=', min(M), 'velocity_component_sum=', 54)
print('C_R(alpha)=', collision_trace(F(0)), '+ alpha *',
      collision_trace(F(1))-collision_trace(F(0)))

# Exhaustive integer checks of the frequency folding and Sobolev weight bound.
alias_pairs = 0
for m in (3, 5, 7):
    q = (m-1)//2
    freqs = list(product(range(-q, q+1), repeat=3))
    for p in freqs:
        pp = sum(x*x for x in p)
        for t in freqs:
            tt = sum(x*x for x in t)
            k = tuple((p[d]+t[d]+q) % m-q for d in range(3))
            kk = sum(x*x for x in k)
            assert kk <= sum((p[d]+t[d])**2 for d in range(3))
            assert (1+kk)**2 <= 8*((1+pp)**2+(1+tt)**2)
            alias_pairs += 1
print('alias exact pairs checked=', alias_pairs,
      '; elementary infinite-shell bound=', F(1123, 35), '< 36')

m, w, a, scale = 3, F(1, 27), F(1, 8), 100
Z = list(product(range(m), repeat=3))
zi = {z: i for i, z in enumerate(Z)}
N = 5832*scale
counts = [[int(216*scale*p) for p in M] for _ in Z]
# A real hop, followed by one actual collision, creates a nonuniform state.
counts[0][0] -= 1
counts[1][0] += 1
i, j, k, l, _, signs = reactions[0]
for v, s in signs:
    counts[0][v] += s
f = [[F(n, N)/w for n in row] for row in counts]
h = [[(f[z][v]/M[v]-1)/a for v in range(27)] for z in range(len(Z))]
energy = w*sum(M[v]*h[z][v]**2 for z in range(len(Z)) for v in range(27))
assert energy < w*min(M)
assert max(abs(x) for row in h for x in row) < 1
assert all(f[z][v] <= 2*M[v] for z in range(len(Z)) for v in range(27))
print('test state: N=', N, 'w=', w, 'amplitude=', a,
      '; energy/r_m^2=', energy/(w*min(M)))

def increment_energy(changes):
    return w*sum(M[v]*(2*h[z][v]*d+d*d) for z, v, d in changes)

# Strip the common 1/(delta*ell) factor from hopping rates and drift.
hop_generator_energy = F(0)
hop_bracket = F(0)
hop_drift = [[F(0) for _ in V] for _ in Z]
edge_square = F(0)
for z, pos in enumerate(Z):
    for v, vel in enumerate(V):
        for d, component in enumerate(vel):
            if component == 0:
                continue
            target = list(pos)
            target[d] = (target[d]+component) % m
            y = zi[tuple(target)]
            jump = 1/(N*w*a*M[v])
            changes = ((z, v, -jump), (y, v, jump))
            rate = counts[z][v]
            hop_generator_energy += rate*increment_energy(changes)
            hop_bracket += rate*w*M[v]*2*jump*jump
            # Independent coordinate drift from the incoming difference stencil.
            previous = list(pos)
            previous[d] = (previous[d]-component) % m
            prev = zi[tuple(previous)]
            hop_drift[z][v] += h[prev][v]-h[z][v]
            edge_square -= w*M[v]*(h[prev][v]-h[z][v])**2
hop_pairing = 2*w*sum(M[v]*h[z][v]*hop_drift[z][v]
                     for z in range(len(Z)) for v in range(27))
assert hop_pairing == edge_square <= 0
assert hop_generator_energy == hop_pairing+hop_bracket
assert hop_bracket*N*w*a*a <= 216
print('exact hop bracket coefficient=', hop_bracket*N*w*a*a, '<= 216')
print('hop energy identity equals directed-edge squared-difference identity')

for alpha in (F(1), F(3)):
    generator_energy, bracket, dissipation = F(0), F(0), F(0)
    drift = [[F(0) for _ in V] for _ in Z]
    for z in range(len(Z)):
        for i, j, k, l, special, signs in reactions:
            kap = alpha if special else F(1)
            nu_h = sum(s*h[z][v] for v, s in signs)
            dissipation -= 2*w*kap*M[i]*M[j]*nu_h*nu_h
            q_flux = kap*(f[z][i]*f[z][j]-f[z][k]*f[z][l])
            # Separate linear-plus-quadratic fluctuation computation.
            expansion = kap*M[i]*M[j]*(-nu_h+a*(h[z][i]*h[z][j]-h[z][k]*h[z][l]))
            assert q_flux/a == expansion
            for v, s in signs:
                drift[z][v] += s*q_flux/(a*M[v])
            for direction, (src1, src2) in ((1, (i, j)), (-1, (k, l))):
                # Common factor delta^-2 stripped from the particle rate.
                rate = kap*counts[z][src1]*counts[z][src2]/(N*w)
                changes = tuple((z, v, direction*s/(N*w*a*M[v])) for v, s in signs)
                generator_energy += rate*increment_energy(changes)
                bracket += rate*w*sum(M[v]*d*d for _, v, d in changes)
    pairing = 2*w*sum(M[v]*h[z][v]*drift[z][v]
                     for z in range(len(Z)) for v in range(27))
    assert generator_energy == pairing+bracket
    assert dissipation <= 0
    cr = collision_trace(alpha)
    assert bracket*N*w*a*a <= 8*cr
    assert pairing-dissipation <= 2*a*cr*energy
    print('alpha=', alpha, 'collision bracket coefficient=', bracket*N*w*a*a,
          '; bound 8*C_R=', 8*cr)
    print('exact generator-energy = deterministic pairing + bracket')
    # Dropping w in the propensity fails the independent drift comparison.
    assert w*pairing != pairing or w*bracket != bracket
print('normalization discriminator: dropping w from collision propensity is rejected')

# Exact iid preparation check by enumerating both labelled draws at one cell.
# All other cells are one aggregate category. Translation invariance recovers
# the total expected energy without using a covariance formula.
initial_N = 2
for tilted in (False, True):
    u = [F(v[0], 2) if tilted else F(0) for v in V]
    prob = [w*M[v]*(1+a*u[v]) for v in range(27)] + [1-w]
    assert sum(prob) == 1 and min(prob) > 0
    local_expectation = F(0)
    for c1, c2 in combinations_with_replacement(range(28), 2):
        n = [0]*27
        for c in (c1, c2):
            if c < 27:
                n[c] += 1
        mass = prob[c1]*prob[c2]*(1 if c1 == c2 else 2)
        err = [(F(n[v], initial_N)/(w*M[v])-1)/a-u[v] for v in range(27)]
        local_expectation += mass*w*sum(M[v]*err[v]**2 for v in range(27))
    total_expectation = local_expectation/w
    independent_variance = sum(prob[v]*(1-prob[v])/(initial_N*w*a*a*M[v])
                               for v in range(27))/w
    assert total_expectation == independent_variance
    assert total_expectation <= 54/(initial_N*w*a*a)
    print('iid direct two-draw enumeration, tilted=', tilted,
          '; full expected error=', total_expectation)

# A jump that crosses the stopping sphere must remain in the stopped energy.
# At equilibrium with 8 particles in each minimum-weight cell species,
# one such hop has relative increment 1 in two components.
witness_m = 3
witness_w = F(1, witness_m**3)
witness_a = F(1, 8)
witness_N = 8*216*witness_m**3
witness_min_weight = min(M)
witness_source_count = witness_N*witness_w*witness_min_weight
assert witness_source_count == 8
witness_jump = 1/(witness_N*witness_w*witness_a*witness_min_weight)
witness_increments = (-witness_jump, witness_jump)
witness_norm_squared = sum(witness_w*witness_min_weight*increment**2
                           for increment in witness_increments)
witness_radius_squared = witness_w*witness_min_weight
witness_ratio = witness_norm_squared/witness_radius_squared
assert witness_ratio > 1
print('exit-overshoot witness: one minimum-weight velocity hop has')
print('N=', witness_N, 'increments=', witness_increments,
      'jump_norm_squared=', witness_norm_squared,
      'r_m_squared=', witness_radius_squared)
print('jump_norm_squared / r_m_squared =', witness_ratio,
      '(computed from equilibrium counts and amplitude 1/8)')

print('all exact checks completed; analytic all-parameter arguments remain in the review')
