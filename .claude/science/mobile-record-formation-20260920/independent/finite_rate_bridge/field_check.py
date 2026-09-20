#!/usr/bin/env python3
"""Independent exact configuration checks of local field/occupancy drift."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
import hashlib
import json

OUT = Path(__file__).resolve().parent
V = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
ZERO = (0,0,0)


def field(s, x):
    return ZERO if s[x] == -1 else V[s[x]]


class Model:
    def __init__(self, size, edges, j):
        self.size, self.edges, self.j = size, tuple(edges), j
        self.nb = tuple(tuple(y if x == z else x for x, y in edges if z in (x,y)) for z in range(size))

    def w(self, a, b):
        return 1 + self.j * sum(x*y for x,y in zip(V[a],V[b]))

    @lru_cache(None)
    def global_weight(self, s):
        out = F(1)
        for x,y in self.edges:
            if s[x] >= 0 and s[y] >= 0:
                out *= self.w(s[x],s[y])
        return out

    def local_birth(self, s, x, a):
        out = F(1)
        for y in self.nb[x]:
            if s[y] >= 0:
                out *= self.w(a,s[y])
        return out

    def hops(self, s):
        for x,y in self.edges:
            if (s[x] == -1) != (s[y] == -1):
                t = list(s)
                t[x],t[y] = t[y],t[x]
                t = tuple(t)
                yield t, self.global_weight(t)/(self.global_weight(s)+self.global_weight(t))

    def ball(self, x, radius):
        found = {x}
        for _ in range(radius):
            found |= {y for z in tuple(found) for y in self.nb[z]}
        return found

    def field_drift(self, s, x):
        motion, birth = [F(0)]*3, [F(0)]*3
        old = field(s,x)
        for t,rate in self.hops(s):
            new = field(t,x)
            for i in range(3):
                motion[i] += rate * (new[i]-old[i])
        if s[x] == -1:
            for a in range(6):
                rate = self.local_birth(s,x,a)
                for i in range(3):
                    birth[i] += rate*V[a][i]
        return tuple(motion),tuple(birth)

    def linear_field(self, s, x):
        adj = [sum(field(s,y)[i] for y in self.nb[x]) for i in range(3)]
        motion = tuple(F(1,2)*(adj[i]-len(self.nb[x])*field(s,x)[i]) for i in range(3))
        birth = tuple(2*self.j*adj[i] for i in range(3))
        return motion,birth


edges = ((0,1),(1,2),(2,3),(3,4))
all_states = tuple(product(range(-1,6),repeat=5))
sparse_counts, tested = {}, 0
for j in (F(-1,2),F(0),F(1,3),F(3,4)):
    model = Model(5,edges,j)
    for x in range(5):
        ball = model.ball(x,2)
        ss = [s for s in all_states if sum(s[y]>=0 for y in ball)<=1]
        sparse_counts[x] = len(ss)
        for s in ss:
            assert model.field_drift(s,x) == model.linear_field(s,x)
            tested += 1

# Uniform-weight occupancy identity holds at every density, without sparsity.
model = Model(5,edges,F(0))
occupancy_cases = 0
for mask in product((False,True),repeat=5):
    s = tuple(x % 6 if occupied else -1 for x,occupied in enumerate(mask))
    for x in range(5):
        nx = int(mask[x])
        motion = sum((rate*(int(t[x]>=0)-nx) for t,rate in model.hops(s)),F(0))
        birth = sum((model.local_birth(s,x,a) for a in range(6)),F(0)) if not nx else F(0)
        laplacian = sum(int(mask[y])-nx for y in model.nb[x])
        assert motion == F(1,2)*laplacian
        assert birth == 6*(1-nx)
        # Vacancy is exactly 1-occupancy for each configuration.
        vacancy_laplacian = sum((1-int(mask[y]))-(1-nx) for y in model.nb[x])
        assert -motion == F(1,2)*vacancy_laplacian
        assert -birth == -6*(1-nx)
        occupancy_cases += 1

# Necessity of the declared domain: occupied-occupied edges do not exchange.
full = Model(2,((0,1),),F(0))
full_state = (0,1)
actual_full = full.field_drift(full_state,0)
linear_full = full.linear_field(full_state,0)
assert actual_full[0][0] == 0 and linear_full[0][0] == -1

# Radius one is insufficient: a second record changes the incoming hop weight.
short = Model(3,((0,1),(1,2)),F(1,2))
short_state = (-1,0,0)
assert sum(short_state[y]>=0 for y in short.ball(0,1)) == 1
assert sum(short_state[y]>=0 for y in short.ball(0,2)) == 2
actual_short = short.field_drift(short_state,0)
linear_short = short.linear_field(short_state,0)
assert actual_short[0][0] == F(2,5) and linear_short[0][0] == F(1,2)
assert actual_short[1][0] == linear_short[1][0] == 1

# Exact Gaussian-integer Fourier checks on side-four tori in d=1,2,3.
# Roots and all intermediate arithmetic are in {integer + i*integer}; the
# Python complex representation is exact for these small integer values.
roots, cosine = (1,1j,-1,-1j), (1,0,-1,0)
fourier_modes = 0
for d in (1,2,3):
    sites = tuple(product(range(4),repeat=d))
    for mode in sites:
        def phase(x):
            value = 1
            for coord,k in zip(x,mode):
                value *= roots[(k*coord)%4]
            return value
        eigen_adjacency = 2*sum(cosine[k] for k in mode)
        for x in sites:
            adjacent_sum = 0
            for axis in range(d):
                for step in (-1,1):
                    y = list(x)
                    y[axis] = (y[axis]+step)%4
                    adjacent_sum += phase(tuple(y))
            assert adjacent_sum == eigen_adjacency*phase(x)
            assert adjacent_sum-2*d*phase(x) == (eigen_adjacency-2*d)*phase(x)
        fourier_modes += 1

summary = {
    'sparse_configuration_site_j_cases': tested,
    'sparse_states_per_site_on_five_path': sparse_counts,
    'j_values': ['-1/2','0','1/3','3/4'],
    'occupancy_all_density_site_cases': occupancy_cases,
    'fourier_modes_checked': fourier_modes,
    'field_generator_motion': 'Delta m_i/2',
    'field_generator_birth_coefficient_of_epsilon': '2 j A m_i',
    'fourier_eigenvalue': '(1+4 epsilon j) sum_r cos(k_r)-d',
    'full_density_counterexample': {
        'state': full_state, 'j': '0',
        'actual_motion_component_1': str(actual_full[0][0]),
        'linear_motion_component_1': str(linear_full[0][0])},
    'radius_one_counterexample': {
        'state': short_state,'j':'1/2',
        'actual_motion_component_1':str(actual_short[0][0]),
        'linear_motion_component_1':str(linear_short[0][0]),
        'birth_component_1_coefficient_of_epsilon':str(actual_short[1][0])},
    'all_checks_satisfied': True,
    'sha256_field_check_py': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'primary_calculations_read': False,
}
(OUT/'FIELD_RESULTS.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
