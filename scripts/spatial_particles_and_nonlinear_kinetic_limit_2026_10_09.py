#!/usr/bin/env python3
"""Exact, standalone checks of the supplied spatial population generator.

No imports from the repository's author runners. Reactions are reconstructed
from four-element species subsets and their three perfect matchings. Literal
count jumps are compared with density-space drift and bracket formulas.
This is finite author evidence, not an audit or proof of limit estimates.
"""

from fractions import Fraction as F
from itertools import combinations, product


AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ['docs/SPATIAL_PARTICLES_AND_NONLINEAR_KINETIC_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-09.md', 'docs/SUPPLIED_FINITE_VELOCITY_COLLISIONS_AND_GIBBS_EQUILIBRATION_BOUNDED_THEOREM_NOTE_2026-10-08.md']

def main():
    velocities = tuple(product((-1, 0, 1), repeat=3))
    q = len(velocities)
    invariants = tuple((1,) + v + (sum(x*x for x in v),) for v in velocities)
    channels = []
    for a, b, c, d in combinations(range(q), 4):
        for i, j, k, l in ((a, b, c, d), (a, c, b, d), (a, d, b, c)):
            if all(invariants[i][z] + invariants[j][z] ==
                   invariants[k][z] + invariants[l][z] for z in range(5)):
                channels.append((i, j, k, l))
    assert len(channels) == len(set(channels)) == 288

    m = 3
    sites = tuple(product(range(m), repeat=3))
    site_index = {z: k for k, z in enumerate(sites)}
    w = F(1, m**3)
    # A rational instance of the arbitrary-side-length version. Side L=2,
    # mesh h=2/3, normalized weight w=1/27 are deliberately different.
    h = F(2, m)
    sigma, gamma, mass = F(3, 2), F(5, 7), F(5, 3)
    rates = tuple(F(1 + (r % 7), 13) for r in range(len(channels)))
    K = sum(rates)
    counts = tuple((7*z + 11*i + 3*z*i) % 5
                   for z in range(len(sites)) for i in range(q))
    N = sum(counts)
    increment = mass / (N*w)
    density = tuple(increment*n for n in counts)
    R = max(density)
    assert w * sum(density) == mass

    def index(z, i):
        return site_index[z] * q + i

    def neighbor(z, axis, direction):
        return tuple((z[d] + (direction if d == axis else 0)) % m
                     for d in range(3))

    drift_events = [F(0) for _ in counts]
    collision_events = [F(0) for _ in counts]
    hop_events = [F(0) for _ in counts]
    qv_hop = F(0)
    qv_collision = F(0)
    event_count = 0
    # Every item is a literal occupation-number jump. This route never uses
    # the density polynomial when calculating event drift or bracket trace.
    for z in sites:
        for i, v in enumerate(velocities):
            source = index(z, i)
            for axis in range(3):
                if not v[axis]:
                    continue
                target_z = neighbor(z, axis, v[axis])
                target = index(target_z, i)
                rate = sigma * abs(v[axis]) * counts[source] / h
                delta = {source: -1, target: 1}
                assert source != target
                assert target_z == neighbor(z, axis, v[axis])
                if rate:
                    assert all(counts[k]+dn >= 0 for k, dn in delta.items())
                for moment in range(5):
                    assert sum(invariants[k % q][moment] * dn
                               for k, dn in delta.items()) == 0
                for k, dn in delta.items():
                    value = rate * increment * dn
                    drift_events[k] += value
                    hop_events[k] += value
                qv_hop += rate * w * increment**2 * sum(dn*dn for dn in delta.values())
                event_count += 1

        for coefficient, (i, j, k, l) in zip(rates, channels):
            for aa, bb, cc, dd in ((i, j, k, l), (k, l, i, j)):
                a, b, c, d = (index(z, species) for species in (aa, bb, cc, dd))
                delta = {a: -1, b: -1, c: 1, d: 1}
                assert len(delta) == 4
                assert len({key // q for key in delta}) == 1
                rate = gamma * coefficient * mass * counts[a] * counts[b] / (N*w)
                if rate:
                    assert all(counts[key]+dn >= 0 for key, dn in delta.items())
                for moment in range(5):
                    assert sum(invariants[key % q][moment] * dn
                               for key, dn in delta.items()) == 0
                for key, dn in delta.items():
                    value = rate * increment * dn
                    drift_events[key] += value
                    collision_events[key] += value
                qv_collision += rate * w * increment**2 * sum(dn*dn for dn in delta.values())
                event_count += 1

    def reaction_polynomial(field):
        out = [F(0) for _ in field]
        for z in sites:
            for coefficient, (i, j, k, l) in zip(rates, channels):
                ii, jj, kk, ll = (index(z, species) for species in (i, j, k, l))
                flux = gamma * coefficient * (field[ii]*field[jj]-field[kk]*field[ll])
                for at, sign in ((ii, -1), (jj, -1), (kk, 1), (ll, 1)):
                    out[at] += sign * flux
        return out

    def upwind(field):
        out = [F(0) for _ in field]
        for z in sites:
            for i, v in enumerate(velocities):
                at = index(z, i)
                for axis in range(3):
                    if v[axis]:
                        previous = index(neighbor(z, axis, -v[axis]), i)
                        out[at] += sigma * abs(v[axis]) * (field[previous]-field[at]) / h
        return out

    collision_density = reaction_polynomial(density)
    hop_density = upwind(density)
    assert collision_events == collision_density
    assert hop_events == hop_density
    assert drift_events == [a+b for a, b in zip(collision_density, hop_density)]

    qv_hop_formula = 2*sigma*mass/(N*h) * sum(
        sum(abs(x) for x in velocities[i]) * density[index(z, i)]
        for z in sites for i in range(q))
    qv_collision_formula = 4*gamma*mass/N * sum(
        coefficient * (density[index(z, i)]*density[index(z, j)] +
                       density[index(z, k)]*density[index(z, l)])
        for z in sites for coefficient, (i, j, k, l) in zip(rates, channels))
    assert qv_hop == qv_hop_formula
    assert qv_collision == qv_collision_formula
    hop_bound = 6*sigma*mass**2/(N*w*h)
    collision_bound = 2*gamma*K*R*mass**2/(N*w)
    assert qv_hop <= hop_bound
    assert qv_collision <= collision_bound

    # Nonconstant spatial test with both signs: the exact negative square
    # identity challenges the sign and locality of the streaming drift.
    test_field = tuple(F(((19*z+7*i+z*i) % 23)-11, 7)
                       for z in range(len(sites)) for i in range(q))
    Atest = upwind(test_field)
    pairing = w * sum(a*b for a, b in zip(test_field, Atest))
    squares = -w*sigma/(2*h) * sum(
        abs(v[axis]) * (test_field[index(neighbor(z, axis, -v[axis]), i)]-
                        test_field[index(z, i)])**2
        for z in sites for i, v in enumerate(velocities)
        for axis in range(3) if v[axis])
    assert pairing == squares < 0
    assert -pairing > 0  # A reversed streaming sign fails dissipativity.

    # Lifted displacement moments of one particle, including zero velocity.
    for v in velocities:
        drift = [F(0)]*3
        cov = [[F(0)]*3 for _ in range(3)]
        for axis in range(3):
            if v[axis]:
                rate = sigma*abs(v[axis])/h
                step = [h*v[axis] if d == axis else F(0) for d in range(3)]
                for a in range(3):
                    drift[a] += rate*step[a]
                    for b in range(3):
                        cov[a][b] += rate*step[a]*step[b]
        assert drift == [sigma*x for x in v]
        assert cov == [[sigma*h*abs(v[a]) if a == b else F(0)
                        for b in range(3)] for a in range(3)]

    local_mass_collision = tuple(sum(collision_events[index(z, i)] for i in range(q)) for z in sites)
    local_mass_hop = tuple(sum(hop_events[index(z, i)] for i in range(q)) for z in sites)
    assert set(local_mass_collision) == {0}
    assert any(local_mass_hop)
    assert sum(local_mass_hop) == 0

    # Mutations challenge the contested interfaces, not expected constants.
    wrong_volume = [w*x for x in collision_events]  # omit 1/w from the count rate
    assert wrong_volume != collision_density
    global_mean = tuple(w*sum(density[index(z, i)] for z in sites) for i in range(q))
    averaged_field = tuple(global_mean[i] for _ in sites for i in range(q))
    global_collision = reaction_polynomial(averaged_field)
    assert global_collision != collision_density
    wrong_transport = [F(0)] * len(counts)
    assert wrong_transport != hop_density

    # Multinomial initial covariance trace derived directly from category
    # variances, independent of the displayed closed normalization formula.
    probabilities = tuple(w*x/mass for x in density)
    initial_variance = sum(w*increment**2*N*p*(1-p) for p in probabilities)
    initial_formula = mass**2/(N*w)*(1-sum(p*p for p in probabilities))
    assert initial_variance == initial_formula <= mass**2/(N*w)

    print('Standalone exact spatial-generator check; no repository imports')
    print(f'velocities={q}; channels={len(channels)}; cells={len(sites)}; particles={N}')
    print(f'mesh={h}; normalized_cell_weight={w}; total_mass={mass}')
    print(f'event_types={event_count}; literal count drift equals upwind + local polynomial')
    print(f'hop bracket trace={qv_hop}; upper_bound={hop_bound}')
    print(f'collision bracket trace={qv_collision}; upper_bound={collision_bound}')
    print(f'transport energy pairing={pairing}; negative_square_identity=exact')
    print(f'local mass transport witness cell 0={local_mass_hop[0]}')
    print('each collision: one cell, four species, five conserved moments')
    print('each transport event: one neighbor, unchanged velocity, five global conserved moments')
    print('lifted single-particle drift sigma*v and covariance sigma*h*diag(abs(v)): exact')
    print('multinomial initial covariance normalization: exact')
    print('mutations detected: omitted cell-volume factor; globally averaged collisions; removed transport; reversed streaming sign')
    print('finite algebra checks completed; stochastic/PDE inequalities require the written proof')


if __name__ == '__main__':
    main()
