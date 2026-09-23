"""Exact shift-support and weighted-generator control for the rotor target.

The physical sweeps use the root elementary builder. The independent
seven-site PRE matrices give a separately constructed field-shift control.
This does not replace the analytic finite-graph or infinite-volume proof.
"""

from pathlib import Path
import hashlib
import importlib.util
import json
import os
import sys
import sympy as sp

sys.dont_write_bytecode = True
HERE=Path(__file__).resolve().parent
D=HERE.parent
OUTPUT=Path(os.environ.get('FIELD_EXPONENTIAL_OUTPUT_DIR',HERE))
OUTPUT.mkdir(parents=True,exist_ok=True)
BUILDER=D/'formation_capacity_author/capacity_and_dark_state_check.py'
PRE=D/'formation_capacity_independent/FINITE_PATH_RESULTS.json'
assert hashlib.sha256(BUILDER.read_bytes()).hexdigest()=='3e9621b36280d19373909922b104c1ead0df9aa47c043d372abd9f9424393a4a'
assert hashlib.sha256(PRE.read_bytes()).hexdigest()=='cea5eadb26ba699d2230befbcbb805ec6df29db52ca1b78c4da19d720ff85553'
spec=importlib.util.spec_from_file_location('root_rotor_builder_for_field_shift',BUILDER)
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

def displacement(initial, final):
    assert len(initial[1])==len(final[1])
    return max((abs(a-b) for a,b in zip(initial[1],final[1])),default=0)

physical=[]
for name,g in [('path8',mod.box(1,8,False)),
               ('ring8',mod.box(1,8,True)),
               ('cube8',mod.box(3,2,False))]:
    states=list(mod.all_physical_words(g))
    assert len(states)==65
    counts={'name':name,'physical_words':len(states),'magnetic_rows':0,
            'resolved_jump_columns':0,'resolved_jump_outputs':0,
            'max_magnetic_single_link_shift':0,'max_jump_single_link_shift':0,
            'shift_two_rows':0,'all_output_Gauss':True}
    for state in states:
        for output,amp in g.magnetic(state).items():
            assert amp and g.gauss(output)
            m=displacement(state,output)
            counts['magnetic_rows']+=1
            counts['max_magnetic_single_link_shift']=max(counts['max_magnetic_single_link_shift'],m)
            counts['shift_two_rows']+=int(m>=2)
        for e in range(len(g.edges)):
            for sigma in (-1,1):
                counts['resolved_jump_columns']+=1
                for output,amp in g.jump(state,e,sigma).items():
                    assert amp and g.gauss(output)
                    m=displacement(state,output)
                    counts['resolved_jump_outputs']+=1
                    counts['max_jump_single_link_shift']=max(counts['max_jump_single_link_shift'],m)
                    counts['shift_two_rows']+=int(m>=2)
    assert counts['max_magnetic_single_link_shift']<=1
    assert counts['max_jump_single_link_shift']<=1
    physical.append(counts)

# On ring8 a uniform oriented circulation changes every field while
# preserving Gauss. The physical path amplitudes must covary under it.
ring=mod.box(1,8,True)
assert ring.edges[-1]==(7,0)
covariant=0
for shift in (-2,3):
    def translated(state):
        q,field=state
        result=(q,tuple(e+shift for e in field))
        assert ring.gauss(result)
        return result
    for state in mod.all_physical_words(ring):
        magnetic=ring.magnetic(state)
        assert ring.magnetic(translated(state))=={translated(s):v for s,v in magnetic.items()}
        for e in range(len(ring.edges)):
            for sigma in (-1,1):
                jump=ring.jump(state,e,sigma)
                assert ring.jump(translated(state),e,sigma)=={translated(s):v for s,v in jump.items()}
        covariant+=1
assert covariant==130

independent=json.loads(PRE.read_text())
states=independent['states']
matrix={'magnetic_rows':0,'jump_rows':0,'max_magnetic_shift':0,
        'max_jump_shift':0,'shift_two_rows':0}
for i,j,v in independent['sparse_H4']:
    assert v
    m=max(abs(a-b) for a,b in zip(states[i]['E'],states[j]['E']))
    matrix['magnetic_rows']+=1
    matrix['max_magnetic_shift']=max(matrix['max_magnetic_shift'],m)
    matrix['shift_two_rows']+=int(m>=2)
for column in independent['resolved_jumps'].values():
    for i,j,v in column:
        assert v
        m=max(abs(a-b) for a,b in zip(states[i]['E'],states[j]['E']))
        matrix['jump_rows']+=1
        matrix['max_jump_shift']=max(matrix['max_jump_shift'],m)
        matrix['shift_two_rows']+=int(m>=2)
assert matrix['max_magnetic_shift']<=1 and matrix['max_jump_shift']<=1

# Generic exact weighted dissipator identity on a truncated five-level rotor.
# W has adjacent ratios at most two, with saturation on its positive end.
W=sp.diag(sp.Rational(1,4),sp.Rational(1,2),1,2,2)
J=sp.diag(*[sp.sqrt(W[i,i]) for i in range(5)])
Jinv=J.inv()
L=sp.zeros(5)
for i in range(5):
    L[i,i]=sp.Rational(i+1,7)
    if i<4:L[i+1,i]=sp.Rational(i+2,5)
    if i>0:L[i-1,i]=sp.Rational(2*i+1,11)
B=J*L*Jinv
C=Jinv*L*J
lhs=Jinv*(L.T*W*L-(L.T*L*W+W*L.T*L)/2)*Jinv
rhs=(B.T*(B-C)+(B-C).T*B)/2
assert lhs.applyfunc(sp.simplify)==rhs.applyfunc(sp.simplify)

out={'arithmetic':'exact integer fields plus SymPy rational/square-root matrices',
     'sources':{str(x):hashlib.sha256(x.read_bytes()).hexdigest() for x in (BUILDER,PRE)},
     'physical_builder_controls':physical,
     'ring_circulation_translations_checked':covariant,
     'separate_PRE_matrix_shift_control':matrix,
     'generic_weighted_dissipator_identity_exact':True,
     'scope':'These finite controls do not prove the all-graph shift lemma or the unbounded-domain passage.'}
(OUTPUT/'SHIFT_AND_WEIGHT_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='sources'},indent=2))
