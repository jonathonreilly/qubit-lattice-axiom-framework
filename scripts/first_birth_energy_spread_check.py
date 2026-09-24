"""Exact first-birth energy moments in the seven-site compensated target.

Derive with the root rotor-path builder, then compare every first-channel
physical vector to the separately constructed independent PRE matrix.
"""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/first_birth_energy_spread_check.py', 'scripts/capacity_and_dark_state_check.py', 'scripts/finite_path_control.py')

from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import hashlib
import importlib.util
import json
import os
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
D = HERE
OUT = Path(os.environ.get('ENERGY_SPREAD_OUTPUT_DIR', HERE))
OUT.mkdir(parents=True, exist_ok=True)
BUILDER = D / 'capacity_and_dark_state_check.py'
PRE = D / 'FINITE_PATH_RESULTS.json'
assert hashlib.sha256(BUILDER.read_bytes()).hexdigest() == '8dcfb8ec32f08cf267c73105c89c5da2c6894f1c294cbd9be2b79f3a042dcd96'
assert hashlib.sha256(PRE.read_bytes()).hexdigest() == 'cea5eadb26ba699d2230befbcbb805ec6df29db52ca1b78c4da19d720ff85553'
spec = importlib.util.spec_from_file_location('capacity_builder_for_energy_spread', BUILDER)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
g = mod.Graph([(i+1,) for i in range(7)], [(i,i+1) for i in range(6)])
assert g.A == (1,3,5) and g.B == (0,2,4,6)
assert len(list(mod.all_physical_words(g))) == 52
omega = g.flow([int(i in g.A) for i in range(7)])
assert g.electric(omega) == 0 and g.magnetic(omega) == {omega:-12}

pre = json.loads(PRE.read_text())
pre_states = [(tuple(s['q']), tuple(s['E'])) for s in pre['states']]
pre_index = {s:i for i,s in enumerate(pre_states)}
pre_edge_order = ((1,0),(1,2),(3,2),(3,4),(5,4),(5,6))


def pre_rep(state):
    charges, fields = state
    edge_field = {frozenset(edge):(edge,value) for edge,value in zip(g.edges,fields)}
    return (charges, tuple(edge_field[frozenset((u,v))][1] *
                           (1 if edge_field[frozenset((u,v))][0] == (u,v) else -1)
                           for u,v in pre_edge_order))


initial_index = pre_index[pre_rep(omega)]
assert pre_states[initial_index][1] == (0,)*6


def pre_column(entries):
    return {pre_states[i]:amplitude for i,j,amplitude in entries if j == initial_index}


def moments(vector):
    image = mod.apply(g.magnetic, vector)
    norm2 = mod.norm2(vector)
    h1 = sum(amplitude * image.get(state,0) for state,amplitude in vector.items())
    h2 = mod.norm2(image)
    assert all(g.gauss(state) and mod.number(state) == 5 and g.electric(state) == 0
               for state in vector)
    return norm2,h1,h2


rows = {'resolved':[], 'coherent':[]}
for edge_index, pair in enumerate(g.edges):
    a,b = pair if pair[0] in g.A else pair[::-1]
    signed = []
    for sigma in (-1,1):
        vector = g.jump(omega,edge_index,sigma)
        assert {pre_rep(state):amp for state,amp in vector.items()} == \
            pre_column(pre['resolved_jumps'][str((a,b,sigma))])
        n,h,h2 = moments(vector)
        assert (n,h,h2) == ((1,0,0) if a == 3 else (1,-2,12))
        rows['resolved'].append(dict(channel=[a,b,sigma],norm2=n,h4_first=h,h4_second=h2))
        signed.append(vector)
    coherent = defaultdict(int)
    for vector in signed:
        for state,amplitude in vector.items():
            coherent[state] += amplitude
    coherent = {state:amp for state,amp in coherent.items() if amp}
    assert {pre_rep(state):amp for state,amp in coherent.items()} == \
        pre_column(pre['coherent_jumps'][str((a,b))])
    n,h,h2 = moments(coherent)
    assert (n,h,h2) == ((2,0,0) if a == 3 else (2,-4,24))
    rows['coherent'].append(dict(channel=[a,b],norm2=n,h4_first=h,h4_second=h2))

for convention in ('resolved','coherent'):
    totals = {key:sum(row[key] for row in rows[convention])
              for key in ('norm2','h4_first','h4_second')}
    assert totals == dict(norm2=12,h4_first=-16,h4_second=96)

mean_post = Fraction(-16,12)
second_post = Fraction(96,12)
variance = second_post - mean_post**2
mean_change = mean_post + 12
initial_power_divided_by_kappa_delta = 12*mean_change
assert (mean_post,second_post,variance,mean_change,initial_power_divided_by_kappa_delta) == \
    (Fraction(-4,3),Fraction(8),Fraction(56,9),Fraction(32,3),Fraction(128))

result = dict(arithmetic='integer path vectors and Fraction moments',
              sources={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in (BUILDER,PRE)},
              physical_words=52, initial_H4_eigenvalue=-12, first_rate_divided_by_kappa=12,
              pre_matrix_first_vectors_all_match=True,
              post_H_mean_divided_by_delta=str(mean_post),
              post_H_second_divided_by_delta_squared=str(second_post),
              post_H_variance_divided_by_delta_squared=str(variance),
              mean_transition_energy_divided_by_delta=str(mean_change),
              initial_power_divided_by_kappa_delta=str(initial_power_divided_by_kappa_delta),
              number_offset_mean_shift_per_birth='2 mu',
              number_offset_variance_shift='0',
              rows=rows,
              scope='Supplied compensated target; fixed seven-site physical path, first actual birth only.')
(OUT/'FIRST_BIRTH_ENERGY_SPREAD_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('sources','rows')},indent=2))
