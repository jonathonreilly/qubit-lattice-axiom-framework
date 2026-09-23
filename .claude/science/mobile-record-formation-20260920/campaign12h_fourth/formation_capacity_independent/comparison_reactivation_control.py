"""Post-PRE exact reconstruction. No author/previous builder imports.

Uses a different A-to-B orientation, a different Gauss tree, and a generic
occupied-source to empty-destination move to compose the full pair action.
The author result is loaded only after the new fixture is computed.
"""
from pathlib import Path
from itertools import product, combinations
from collections import Counter
from fractions import Fraction
import hashlib
import json

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent / 'formation_capacity_author'
L = 6
COORD = tuple(product(range(L), repeat=2))
ID = {x:i for i,x in enumerate(COORD)}
A = tuple(i for i,x in enumerate(COORD) if sum(x)%2 == 0)
B = tuple(i for i in range(len(COORD)) if i not in A)
ASET = set(A)
NB = {}
for i,x in enumerate(COORD):
    adjacent = set()
    for axis in range(2):
        for sign in (-1,1):
            y = list(x)
            y[axis] = (y[axis]+sign)%L
            adjacent.add(ID[tuple(y)])
    NB[i] = tuple(sorted(adjacent))
EDGES = tuple((a,b) for a in A for b in NB[a])
EDGE = {frozenset(e):k for k,e in enumerate(EDGES)}
PAIRS = tuple(sorted({tuple(sorted((a,c))) for b in B for a,c in combinations(NB[b],2)}))
HOLES = {ID[(5,0)],ID[(2,1)]}
OCCUPIED = sorted(set(B)-HOLES)
q = [int(i in ASET) for i in range(len(COORD))]
for j,b in enumerate(OCCUPIED): q[b] = 1 if j<len(OCCUPIED)//2 else -1

# A new tree rooted at the last coordinate, with sorted-neighbor traversal.
parent = {len(COORD)-1: None}
order = [len(COORD)-1]
for u in order:
    for v in NB[u]:
        if v not in parent:
            parent[v] = u
            order.append(v)
subtree = [q[i]-int(i in ASET) for i in range(len(COORD))]
electric = [0]*len(EDGES)
for child in reversed(order[1:]):
    par = parent[child]
    e = EDGE[frozenset((child,par))]
    electric[e] = subtree[child] if EDGES[e][0] == child else -subtree[child]
    subtree[par] += subtree[child]
assert subtree[order[0]] == 0
PSI = (tuple(q),tuple(electric))
validated = set()

def validate(state):
    if state in validated: return
    charges, fields = state
    divergence = [0]*len(COORD)
    for (a,b),value in zip(EDGES,fields):
        divergence[a] += value
        divergence[b] -= value
    assert all(divergence[i] == charges[i]-int(i in ASET) for i in range(len(COORD)))
    assert all(x in (-1,0,1) for x in charges)
    validated.add(state)

validate(PSI)

def move(state,source,dest):
    charges,fields = state
    assert charges[source] != 0 and charges[dest] == 0
    value = charges[source]
    nc,nf = list(charges),list(fields)
    nc[source],nc[dest] = 0,value
    edge = EDGE[frozenset((source,dest))]
    orientation = 1 if EDGES[edge][0] == source else -1
    nf[edge] -= orientation*value
    result = (tuple(nc),tuple(nf))
    validate(result)
    return result

def outward(state,a):
    if not state[0][a]: return []
    return [move(state,a,b) for b in NB[a] if not state[0][b]]

def inward(state,a):
    if state[0][a]: return []
    return [move(state,b,a) for b in NB[a] if state[0][b]]

def magnetic(state):
    result = Counter()
    for a,c in PAIRS:
        for s1 in outward(state,a):
            for s2 in outward(s1,c):
                for s3 in inward(s2,c):
                    for s4 in inward(s3,a):
                        result[s4] -= 2
    return {s:v for s,v in result.items() if v}

def jump_on_vector(vector,a,b,sigma):
    result = Counter()
    for state,amplitude in vector.items():
        if state[0][b]: continue
        for old_dest in NB[a]:
            if old_dest == b or state[0][old_dest]: continue
            interim = move(state,a,old_dest)
            nc,nf = list(interim[0]),list(interim[1])
            assert nc[a] == nc[b] == 0
            nc[a],nc[b] = sigma,-sigma
            nf[EDGE[frozenset((a,b))]] += sigma
            output = (tuple(nc),tuple(nf))
            validate(output)
            assert sum(x!=0 for x in output[0]) == sum(x!=0 for x in state[0])+2
            result[output] += amplitude
    return {s:v for s,v in result.items() if v}

def norm2(v): return sum(a*a for a in v.values())

def electric_value(state):
    return sum(e*(e-state[0][a]) for (a,b),e in zip(EDGES,state[1]) if not state[0][b])

def compact(state,amplitude):
    return dict(amplitude=amplitude,
                charge_changes=[[i,v] for i,v in enumerate(state[0]) if v!=PSI[0][i]],
                field_changes=[[i,v-PSI[1][i]] for i,v in enumerate(state[1]) if v!=PSI[1][i]])

initial_channels = [jump_on_vector({PSI:1},a,b,sigma) for a,b in EDGES for sigma in (-1,1)]
assert not any(initial_channels)
VPSI = magnetic(PSI)
assert all(sum(x!=0 for x in s[0]) == 34 for s in VPSI)
channels = {}
rows = []
resolved_total = coherent_total = 0
for a,b in EDGES:
    signs = []
    for sigma in (-1,1):
        v = jump_on_vector(VPSI,a,b,sigma)
        channels[(COORD[a],COORD[b],sigma)] = v
        signs.append(v)
        resolved_total += norm2(v)
        if v:
            rows.append(dict(A=COORD[a],B=COORD[b],sigma=sigma,
                             squared_norm=norm2(v), output_words=len(v),
                             outputs=[compact(s,amp) for s,amp in sorted(v.items())]))
    assert not (set(signs[0]) & set(signs[1]))
    merged = Counter(signs[0])
    merged.update(signs[1])
    coherent_total += norm2(merged)
assert resolved_total == coherent_total > 0

# Reconstruct the specific route in the new argument, including its field.
a,c = ID[(0,0)],ID[(1,1)]
route = move(PSI,a,ID[(5,0)])
route = move(route,c,ID[(2,1)])
route = move(route,ID[(1,0)],c)
route = move(route,ID[(0,1)],a)
assert {COORD[b] for b in B if not route[0][b]} == {(1,0),(0,1)}
assert VPSI[route] < 0
assert jump_on_vector({route:1},a,ID[(0,1)],1)

# The coefficient is independent of the physical base field for fixed q.
# Check one nonzero circulation translation directly, besides the proof.
circulation = [0]*len(EDGES)
loop = [ID[(0,0)],ID[(1,0)],ID[(1,1)],ID[(0,1)],ID[(0,0)]]
for u,v in zip(loop,loop[1:]):
    e = EDGE[frozenset((u,v))]
    circulation[e] += 3 if EDGES[e][0] == u else -3
def shift(state):
    new = (state[0],tuple(x+y for x,y in zip(state[1],circulation)))
    validate(new)
    return new
shifted_magnetic = magnetic(shift(PSI))
assert shifted_magnetic == {shift(s):v for s,v in VPSI.items()}
probe = (ID[(0,0)],ID[(1,0)],1)
probe_output = jump_on_vector(shifted_magnetic,*probe)
assert probe_output == {shift(s):v for s,v in jump_on_vector(VPSI,*probe).items()}

# Only now load the frozen author result for exact source comparison.
AUTHOR_RESULT = json.loads((AUTHOR/'CAPACITY_CONTROL_RESULTS.json').read_text())
ar = AUTHOR_RESULT['motion_reactivation']
assert len(VPSI) == ar['H_magnetic_output_words'] == 65
assert norm2(VPSI) == ar['H_magnetic_norm_squared'] == 616
assert resolved_total == ar['sum_squared_norm_L_H_psi_over_kappa_delta_squared'] == 3136
assert str(Fraction(resolved_total,3)) == ar['first_birth_t_cubed_coefficient_over_kappa_delta_squared']
actual = {(tuple(r['A']),tuple(r['B']),r['sigma']):(r['squared_norm'],r['output_words']) for r in rows}
expected = {}
for row in ar['nonzero_channels']:
    u,v = map(tuple,row['oriented_edge'])
    a,b = (u,v) if sum(u)%2 == 0 else (v,u)
    expected[(a,b,row['sigma'])] = (row['squared_norm_L_H_psi'],row['output_words'])
assert actual == expected

# Read every recorded period-six charge and field component, and independently
# recompute its physical and numerical summaries. This is not the author's
# spanning-tree generator or a replay of the old finite-column suite.
periodic_checks = []
for row in AUTHOR_RESULT['periodic_stationary_controls']:
    d,n = row['d'],row['period']
    coords = tuple(product(range(n),repeat=d))
    index = {x:i for i,x in enumerate(coords)}
    a_set = {i for i,x in enumerate(coords) if sum(x)%2 == 0}
    edges = []
    adjacency = {i:set() for i in range(len(coords))}
    for i,x in enumerate(coords):
        for axis in range(d):
            y = list(x); y[axis]=(y[axis]+1)%n
            j = index[tuple(y)]
            edges.append((i,j)); adjacency[i].add(j); adjacency[j].add(i)
    charges,fields = row['charge_word'],row['integer_Gauss_field']
    assert len(charges)==len(coords) and len(fields)==len(edges)
    divergence = [0]*len(coords)
    D_value = 0
    for (u,v),E in zip(edges,fields):
        divergence[u]+=E; divergence[v]-=E
        a,b,sgn = (u,v,1) if u in a_set else (v,u,-1)
        if not charges[b]: D_value += E*(E-sgn*charges[a])
    assert all(divergence[i]==charges[i]-int(i in a_set) for i in range(len(coords)))
    assert all(charges[a]==1 for a in a_set)
    holes = {i for i in range(len(coords)) if charges[i]==0}
    assert {coords[i] for i in holes}=={tuple(x) for x in row['vacancies']}
    lifted_distance = min(sum(abs(x-y-n*s) for x,y,s in zip(u,v,k))
        for u in map(tuple,row['vacancies']) for v in map(tuple,row['vacancies'])
        for k in product((-1,0,1),repeat=d) if u!=v or any(k))
    pairs = {tuple(sorted((a,c))) for b in range(len(coords)) if b not in a_set
             for a,c in combinations(adjacency[b],2)}
    empty = {a:adjacency[a]&holes for a in a_set}
    births = sum(len(v)*(len(v)-1) for v in empty.values())
    pair_routes = sum(sum(b!=e for b in empty[a] for e in empty[c]) for a,c in pairs)
    density = str(Fraction(sum(x!=0 for x in charges),len(coords)))
    moment = str(Fraction(sum(E*E for E in fields),len(coords)))
    assert lifted_distance == row['minimum_lifted_vacancy_distance'] == 6
    assert len(pairs)==row['overlapping_A_pairs_checked']
    assert births==row['first_birth_paths']==pair_routes==row['outward_pair_paths']==0
    assert D_value==row['electric_D_per_cell']
    assert density==row['density_exact'] and moment==row['finite_electric_second_moment_per_vertex']
    assert max(map(abs,fields))==row['largest_absolute_electric_field']
    periodic_checks.append(dict(d=d, all_recorded_components_consumed=True,
        vertices=len(coords), edges=len(edges), Gauss=True,
        pair_terms=len(pairs), birth_paths=births, pair_paths=pair_routes,
        D=D_value, density=density, field_second_moment=moment,
        max_abs_field=max(map(abs,fields))))

result = dict(arithmetic='exact integers and Fraction',
    independent_reactivation=dict(vertices=len(COORD),edges=len(EDGES),pair_terms=len(PAIRS),
        orientations='all A to B', own_Gauss_tree_root=COORD[order[0]],
        initial_q=PSI[0], initial_E=PSI[1], initial_D=electric_value(PSI),
        coordinates=COORD,edges_as_vertex_indices=EDGES,
        initial_channels_tested=len(initial_channels), initial_jump_norms_all_zero=True,
        magnetic_output_words=len(VPSI), magnetic_norm_squared=norm2(VPSI),
        magnetic_initial_word_amplitude=VPSI.get(PSI,0),
        all_magnetic_outputs=[compact(s,amp) for s,amp in sorted(VPSI.items())],
        total_squared_norm=resolved_total, cubic_coefficient=str(Fraction(resolved_total,3)),
        coherent_total_squared_norm=coherent_total,
        nonzero_resolved_channels=len(rows), all_author_channel_rows_match=True,
        specific_author_route_amplitude=VPSI[route],
        specific_route=compact(route,VPSI[route]),
        full_magnetic_circulation_covariance_checked=True,
        selected_jump_circulation_covariance_checked=True,
        unique_Gauss_states_checked=len(validated),nonzero_channels=rows),
    complete_author_periodic_data_checks=periodic_checks,
    author_old_finite_column_suite_rerun=False,
    no_author_or_inherited_builder_import=True,
    scope='Exact finite algebra and all recorded periodic Gauss data. No time-evolution fit, new volume theorem or unrelated frontier check.')
(HERE/'COMPARISON_CONTROL_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(magnetic_words=len(VPSI), magnetic_norm_squared=norm2(VPSI),
    initial_D=electric_value(PSI), total_squared_norm=resolved_total,
    cubic_coefficient=str(Fraction(resolved_total,3)),
    nonzero_resolved_channels=len(rows), all_author_channel_rows_match=True,
    unique_Gauss_states_checked=len(validated),
    author_periodic_data_checks=periodic_checks),indent=2))
