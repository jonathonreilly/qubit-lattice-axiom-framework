import ast,itertools,sys,json,collections
from pathlib import Path
import numpy as np
root=Path(__file__).resolve().parents[2]
tree=ast.parse((root/'scripts/corner_fermion_qubit_code_genuine_cube_rotation_action_spin_half_class_2026_10_17.py').read_text())
fn=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='_run_reviewed_program')
body=[]
for x in fn.body:
    if isinstance(x,ast.ClassDef):break
    if not isinstance(x,ast.Global):body.append(x)
ns={'itertools':itertools,'sys':type('Args',(),{'argv':['check','4','1011']})(),'np':np}
exec(compile(ast.Module(body=body,type_ignores=[]),'<upstream definitions>','exec'),ns)
# No A,loop_op,pmul,pcomm,edge_qubits,INC used in independent geometry calculation.
site_id={v:i for i,v in enumerate(ns['SITES'])};loc=ns['LOC'];L=4
q=lambda v,label:48*site_id[v]+loc[label]
def support(u,v):
    x,c=u;y,d=v
    if x==y:return {q(x,('o',tuple(sorted((c,d)))))}
    diff=[(y[i]-x[i])%L for i in range(3)]
    direction=tuple(-1 if z==L-1 else z for z in diff)
    assert sum(abs(z) for z in direction)==1
    opposite=tuple(-z for z in direction)
    assert direction in c and opposite in d
    return {q(x,('h',(c,direction))),q(y,('h',(d,opposite)))}
rows=[]
for kind,seq in ns['cycles']():
    bits=set()
    for j in range(len(seq)):bits.symmetric_difference_update(support(seq[j],seq[(j+1)%len(seq)]))
    rows.append(bits)
syndromes=[set() for _ in range(ns['NQ'])]
for j,row in enumerate(rows):
    for i in row:syndromes[i].add(j)
groups=collections.defaultdict(list)
for i,col in enumerate(syndromes):groups[tuple(sorted(col))].append(i)
diam=0
for inds in groups.values():
    for i,j in itertools.combinations(inds,2):
        dx=[abs(a-b) for a,b in zip(ns['SITES'][i//48],ns['SITES'][j//48])]
        diam=max(diam,sum(min(x,L-x) for x in dx))
# Only now compare independent binary supports to original Pauli loop construction.
orig=[ns['loop_op'](seq,ns['FLUX'][kind])[0] for kind,seq in ns['cycles']()]
exact=all(sum(1<<i for i in row)==orig[j] for j,row in enumerate(rows))
res={'qubits':ns['NQ'],'loops':len(rows),'classes':len(groups),'class_size_histogram':dict(collections.Counter(map(len,groups.values()))),'max_diameter':diam,'empty_syndromes':sum(not col for col in syndromes),'independent_geometry_matches_original_pauli_X':exact}
# Direct physical paired-half validation, not merely max diameter.
expected=[]
for v in ns['SITES']:
    for a,b in ns['ONS']:expected.append(frozenset([q(v,('o',(a,b)))]))
    for c,d in ns['HALF']:
        other=tuple((v[i]+d[i])%L for i in range(3));neg=tuple(-x for x in d);rest=next(x for x in c if x!=d);oc=tuple(sorted((neg,rest)))
        expected.append(frozenset([q(v,('h',(c,d))),q(other,('h',(oc,neg)))]))
res['classes_are_exactly_onsite_edges_and_repetition_pairs']=set(map(frozenset,groups.values()))==set(expected)
(root/'outputs/microscopic_flux_interaction/independent.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
assert exact and diam==1 and res['empty_syndromes']==0 and res['classes_are_exactly_onsite_edges_and_repetition_pairs']
