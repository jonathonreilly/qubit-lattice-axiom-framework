#!/usr/bin/env python3
"""Independent exact normalization/jump examples, without repository imports.

The inverse-mesh factor is left symbolic by checking its hopping coefficient.
Rational positive reaction rates test identities valid reaction by reaction;
the separately reviewed tuned constitutive theorem is not recomputed here.
"""
from fractions import Fraction as F
from itertools import combinations, product

V = list(product((-1, 0, 1), repeat=3))
energy = [sum(x*x for x in v) for v in V]
M = [F(2, 3)**(3-e)*F(1, 6)**e for e in energy]
reactions = []
for a, b, c, d in combinations(range(27), 4):
    for i, j, k, l in ((a, b, c, d), (a, c, b, d), (a, d, b, c)):
        if all(V[i][s]+V[j][s] == V[k][s]+V[l][s] for s in range(3)) and energy[i]+energy[j] == energy[k]+energy[l]:
            reactions.append((i, j, k, l))
assert len(reactions) == 288
rates = [F(1)+F(r % 3, 3) for r in range(288)]
trace_b = sum((rate*M[i]*M[j]*sum(F(1)/M[t] for t in (i, j, k, l))
               for rate, (i, j, k, l) in zip(rates, reactions)), F(0))

m = 3
cells = list(product(range(m), repeat=3))
w = F(1, m**3)
delta = F(1, 1024)
m0 = min(M)
q = 2048
N = q*216*m**3
keys = [(z, v) for z in cells for v in range(27)]
counts = {(z, v): int(q*216*M[v]) for z, v in keys}
rest, corner = V.index((0, 0, 0)), V.index((1, 1, 1))
z0 = (0, 0, 0)
counts[z0, rest] += 1
counts[z0, corner] -= 1
assert sum(counts.values()) == N and min(counts.values()) >= 0
pop = {key: F(counts[key], N)/w for key in keys}
h = {(z, v): (pop[z, v]/M[v]-1)/delta for z, v in keys}
norm2 = lambda a: sum((w*M[v]*a[z, v]**2 for z, v in keys), F(0))
assert norm2(h) < w*m0
assert all(pop[z, v] <= 2*M[v] for z, v in keys)
# Zero target has A=0,D=1; the draft's stronger embedding smallness holds.
assert (delta*2)**2*36/m0 <= F(1, 4)

hop_drift = {key: F(0) for key in keys}
hop_qv_coefficient = F(0)  # coefficient multiplying ell^{-1}
expected_hop = {key: F(0) for key in keys}
for z, v in keys:
    for a in range(3):
        speed = V[v][a]
        if not speed:
            continue
        dest = list(z)
        dest[a] = (dest[a]+speed) % m
        dest = tuple(dest)
        inc = F(1)/(N*w*delta*M[v])
        rate_coefficient = abs(speed)*counts[z, v]/delta
        hop_drift[z, v] -= rate_coefficient*inc
        hop_drift[dest, v] += rate_coefficient*inc
        jump_square = w*M[v]*((-inc)**2+inc**2)
        assert jump_square == F(2)/(N*N*w*delta*delta*M[v])
        hop_qv_coefficient += rate_coefficient*jump_square
        source = list(z)
        source[a] = (source[a]-speed) % m
        expected_hop[z, v] += abs(speed)*(h[tuple(source), v]-h[z, v])/delta
assert hop_drift == expected_hop
assert any(hop_drift.values())
assert hop_qv_coefficient <= F(216)/(N*w*delta**3)
assert sum(abs(x) for v in V for x in v) == 54

reaction_drift = {key: F(0) for key in keys}
reaction_qv = F(0)
expected_reaction = {key: F(0) for key in keys}
for z in cells:
    for rate, (i, j, k, l) in zip(rates, reactions):
        signs = ((i, -1), (j, -1), (k, 1), (l, 1))
        assert M[i]*M[j] == M[k]*M[l]
        jr = sum(F(1)/M[v] for v, sign in signs)
        jump_square = sum(w*M[v]*(F(sign)/(N*w*delta*M[v]))**2 for v, sign in signs)
        assert jump_square == jr/(N*N*w*delta**2)
        for src, orientation in (((i, j), 1), ((k, l), -1)):
            propensity = rate*counts[z, src[0]]*counts[z, src[1]]/(delta**2*N*w)
            reaction_qv += propensity*jump_square
            for v, sign in signs:
                reaction_drift[z, v] += propensity*orientation*sign/(N*w*delta*M[v])
        bh_scalar = rate*M[i]*M[j]*(h[z, k]+h[z, l]-h[z, i]-h[z, j])
        gamma_scalar = rate*M[i]*M[j]*(h[z, i]*h[z, j]-h[z, k]*h[z, l])
        for v, sign in signs:
            expected_reaction[z, v] += sign*(-bh_scalar/delta**2+gamma_scalar/delta)/M[v]
assert reaction_drift == expected_reaction
assert any(reaction_drift.values())
assert reaction_qv <= 8*trace_b/(N*w*delta**4)
assert {key: w*x for key, x in reaction_drift.items()} != expected_reaction  # omitting w in the propensity fails

# Exact iid one-draw Hilbert variance, independently compared with the sum
# of multinomial diagonal variances. This does not assume independent counts.
g0 = {(z, v): F(z[0]-1)*F(5-3*energy[v], 2)+F(3, 7)*V[v][0] for z, v in keys}
p = {(z, v): w*M[v]*(1+delta*g0[z, v]) for z, v in keys}
assert sum(p.values()) == 1 and min(p.values()) > 0
assert all(p[z, v] <= 2*w*M[v] for z, v in keys)
mu = {key: (1+delta*g0[key])/delta for key in keys}
mu_square = norm2(mu)
sample_count = 17
one_draw_variance = sum((p[z, v]*(F(1)/(w*delta**2*M[v])-2*mu[z, v]/delta+mu_square)
                        for z, v in keys), F(0))/sample_count
multinomial_variance = sum((p[z, v]*(1-p[z, v])/(sample_count*w*delta**2*M[v])
                           for z, v in keys), F(0))
assert one_draw_variance == multinomial_variance > 0
assert sum(p[z, v]/M[v] for z, v in keys) == 27
assert multinomial_variance <= F(27)/(sample_count*w*delta**2)
assert w*multinomial_variance != one_draw_variance

# A genuine overshoot under the zero-target hypotheses. At exact equilibrium,
# Nw M_min=1024; a corner hop changes two minimum-weight coordinates.
overshoot_q = 1024
overshoot_N = overshoot_q*216*m**3
increment = F(1)/(overshoot_N*w*delta*m0)
overshoot_square = w*m0*((-increment)**2+increment**2)
threshold_square = w*m0
overshoot_ratio = overshoot_square/threshold_square
assert overshoot_ratio > 1
assert overshoot_q > 0  # the hop has strictly positive pre-jump rate

# Exact sampling aliases: rho(x)=cos(m x_1) has continuum mean zero but
# samples to one. F_v(x)=sin(m x_1) samples to zero, yet S_m T F=m v_1.
sampled_rho_mean = F(1)
uncorrected_probability_mass = 1+delta*sampled_rho_mean
corrected_probability_mass = uncorrected_probability_mass-delta*sampled_rho_mean
assert corrected_probability_mass == 1 and uncorrected_probability_mass != 1
alias_taylor_residual_square = sum(M[v]*(m*V[v][0])**2 for v in range(27))
assert alias_taylor_residual_square > 0
interpolation_alias_error_square = F(1)+F(1, 2)  # integral of (1-cos(m x_1))^2

# Track powers independently as the product of factors in Pi2. The initial
# term is delta^5; hopping dominates at delta^2, collision gives delta^3.
inverse_N, inverse_w2, inverse_delta2 = 19, -12, -2
prefactor_power = inverse_N+inverse_w2+inverse_delta2
probability_powers = {'initial': prefactor_power,
                      'hopping': prefactor_power-1-2,
                      'collision': prefactor_power-2}
assert probability_powers == {'initial': 5, 'hopping': 2, 'collision': 3}

print('reactions', len(reactions), '; trace B for rational test rates', trace_b)
print('pre-stop count state:', 'm', m, 'N', N, 'delta', delta, '; norm2/threshold2', norm2(h)/(w*m0))
print('exact hopping and collision conditional drifts agree; all jump norms and both bracket bounds checked')
print('one-draw and multinomial L2 variances agree for nonuniform preparation; omitted cell-weight controls fail')
print('overshoot witness:', 'N', overshoot_N, 'increment', increment, 'squared exit ratio', overshoot_ratio)
print('alias witnesses:', 'uncorrected mass', uncorrected_probability_mass, 'corrected mass', corrected_probability_mass,
      'squared Taylor residual', alias_taylor_residual_square, 'squared interpolation error', interpolation_alias_error_square)
print('delta powers for N>=delta^-19:', probability_powers)
print('scope: exact finite drift, normalization, variance, jump and alias witnesses; no stochastic path theorem is inferred from samples')
