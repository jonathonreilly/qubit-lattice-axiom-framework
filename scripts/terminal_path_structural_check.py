"""Second seven-site derivation with the root rotor-path builder.

The independent PRE matrix supplies a separate source for comparison. Each
channel eigen-identity is computed with the root rotor builder first, then
the resulting physical output word is compared to the PRE matrix column.
"""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/terminal_path_structural_check.py', 'scripts/capacity_and_dark_state_check.py', 'scripts/finite_path_control.py')

from pathlib import Path
from collections import defaultdict
import hashlib
import importlib.util
import json
import os
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
D = HERE
OUTPUT = Path(os.environ.get('TERMINAL_PATH_OUTPUT_DIR', HERE))
OUTPUT.mkdir(parents=True, exist_ok=True)
BUILDER = D / 'capacity_and_dark_state_check.py'
PRE_RESULT = D / 'FINITE_PATH_RESULTS.json'
assert hashlib.sha256(BUILDER.read_bytes()).hexdigest() == '8dcfb8ec32f08cf267c73105c89c5da2c6894f1c294cbd9be2b79f3a042dcd96'
assert hashlib.sha256(PRE_RESULT.read_bytes()).hexdigest() == 'cea5eadb26ba699d2230befbcbb805ec6df29db52ca1b78c4da19d720ff85553'
spec = importlib.util.spec_from_file_location('capacity_builder_for_structural_check', BUILDER)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

graph = mod.Graph([(i+1,) for i in range(7)], [(i,i+1) for i in range(6)])
assert graph.A == (1,3,5) and graph.B == (0,2,4,6)
states = list(mod.all_physical_words(graph))
assert len(states) == 52
assert sum(mod.number(s)==5 for s in states)==30
psi = graph.flow([int(i in graph.A) for i in range(7)])
assert graph.electric(psi)==0 and graph.magnetic(psi)=={psi:-12}

def clean(vector):
    return {s:a for s,a in vector.items() if a}

def gamma(vector):
    result=defaultdict(int)
    for e in range(len(graph.edges)):
        for sigma in (-1,1):
            formed=mod.apply(lambda s:graph.jump(s,e,sigma),vector)
            returned=mod.apply(lambda s:graph.jump(s,e,sigma,True),formed)
            for s,a in returned.items(): result[s]+=a
    return clean(result)

def magnetic(vector):
    return mod.apply(graph.magnetic,vector)

def independent_rep(state):
    charges, fields=state
    independent_edges=((1,0),(1,2),(3,2),(3,4),(5,4),(5,6))
    lookup={frozenset(pair):(pair,field) for pair,field in zip(graph.edges,fields)}
    vals=[]
    for u,v in independent_edges:
        pair,field=lookup[frozenset((u,v))]
        vals.append(field if pair==(u,v) else -field)
    return (charges,tuple(vals))

pre=json.loads(PRE_RESULT.read_text())
pre_states=[(tuple(row['q']),tuple(row['E'])) for row in pre['states']]
pre_index={s:i for i,s in enumerate(pre_states)}
initial=pre_index[independent_rep(psi)]
assert pre_states[initial][1]==(0,)*6

def pre_column(entries):
    return {pre_states[i]:amp for i,j,amp in entries if j==initial}

rows=[]
resolved={}
coherent={}
for e, pair in enumerate(graph.edges):
    u,v=pair
    a,b=(u,v) if u in graph.A else (v,u)
    per_sign=[]
    for sigma in (-1,1):
        formed=graph.jump(psi,e,sigma)
        assert len(formed)==1 and mod.norm2(formed)==1
        assert all(graph.gauss(s) and mod.number(s)==5 for s in formed)
        eig=0 if a==3 else 4
        assert gamma(formed)==({} if eig==0 else {s:eig*x for s,x in formed.items()})
        if eig==0:
            assert magnetic(formed)=={}
            assert all(graph.electric(s)==0 for s in formed)
        expected=pre_column(pre['resolved_jumps'][str((a,b,sigma))])
        observed={independent_rep(s):x for s,x in formed.items()}
        assert observed==expected
        rows.append({'channel':(a,b,sigma),'norm_squared':1,
                     'Gamma_eigenvalue_divided_by_kappa':eig,
                     'H4_zero':not magnetic(formed),
                     'D_zero':all(graph.electric(s)==0 for s in formed),
                     'matches_separate_PRE_matrix':True})
        resolved[(a,b,sigma)]=formed
        per_sign.append(formed)
    merged=defaultdict(int)
    for formed in per_sign:
        for s,x in formed.items():merged[s]+=x
    merged=clean(merged)
    assert mod.norm2(merged)==2
    eig=0 if a==3 else 4
    assert gamma(merged)==({} if eig==0 else {s:eig*x for s,x in merged.items()})
    if eig==0:
        assert magnetic(merged)=={}
        assert all(graph.electric(s)==0 for s in merged)
    expected=pre_column(pre['coherent_jumps'][str((a,b))])
    observed={independent_rep(s):x for s,x in merged.items()}
    assert observed==expected
    coherent[(a,b)]=merged

assert len(rows)==12 and len(coherent)==6
assert sum(x['norm_squared'] for x in rows if x['Gamma_eigenvalue_divided_by_kappa']==0)==4
assert sum(x['norm_squared'] for x in rows if x['Gamma_eigenvalue_divided_by_kappa']==4)==8
result={
 'scope':'Seven-site physical tree; root second operator implementation; exact all first channels',
 'source_bindings':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in (BUILDER,PRE_RESULT)},
 'physical_states':52,'N5_states':30,'all_first_resolved':len(rows),
 'all_first_coherent':len(coherent),'first_total_norm_squared':12,
 'stationary_middle_norm_squared':4,'strictly_lossy_endpoint_norm_squared':8,
 'endpoint_Gamma_eigenvalue_divided_by_kappa':4,
 'all_first_channels_matched_separate_PRE_matrix':True,
 'universal_count_formula':'For all real K,delta and kappa>0: Pr(J_infinity=1)=1/3, Pr(J_infinity=2)=2/3 for both instruments.',
 'proof_condition':'The zero-loss middle vectors are annihilated by D and H4; each endpoint first vector lies in the positive eigenvalue-4 subspace of Gamma0, orthogonal to every future-surviving dark Hamiltonian subspace.',
 'resolved_rows':rows,
}
(OUTPUT/'TERMINAL_PATH_STRUCTURAL_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('source_bindings','resolved_rows')},indent=2))
