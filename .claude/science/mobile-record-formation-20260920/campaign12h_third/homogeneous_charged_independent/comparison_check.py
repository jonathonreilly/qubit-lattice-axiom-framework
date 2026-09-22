"""Selective independent post-seal controls. Never imports author code."""
from pathlib import Path
from datetime import datetime, timezone
from itertools import product
from math import comb
import hashlib, json, difflib
import sympy as s

HERE=Path(__file__).resolve().parent
BASE=HERE.parent
OUT=HERE/'COMPARISON_RESULTS.json'
assert not OUT.exists(), 'Preserve prior results and failed attempts.'

def row(p):
    p=Path(p); raw=p.read_bytes()
    return {'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}

def verify(bindings):
    for r in bindings:
        actual=row(r['path'])
        assert actual['bytes']==r['bytes'] and actual['sha256']==r['sha256'], (r,actual)
    return len(bindings)

pre_path=HERE/'PRE_COMPARISON_SEAL.json'
author_path=BASE/'HOMOGENEOUS_CHARGED_RECORDS_AUTHOR_SEAL.json'
assert row(pre_path)['sha256']=='1678d9365ac5c3460d70a13d16b8b3fbeedd0f09b658a023c5ee515e4e213b48'
assert row(author_path)['sha256']=='ec6d68f95a67c810e442fe52d8e453183f4d9723e55e52df36a0d8010727b9b0'
pre=json.loads(pre_path.read_text()); author=json.loads(author_path.read_text())
pre_count=verify(pre['sources']+pre['artifacts']); author_count=verify(author['artifacts'])
context=json.loads((BASE/'HOMOGENEOUS_CHARGED_RECORDS_SOURCE_CONTEXT.json').read_text())
context_rows=[]
def collect_rows(obj):
    if isinstance(obj,dict):
        if {'path','sha256','bytes'} <= obj.keys(): context_rows.append(obj)
        else:
            for v in obj.values(): collect_rows(v)
    elif isinstance(obj,list):
        for v in obj: collect_rows(v)
collect_rows(context)
context_count=verify(context_rows)
# Merely hash any contextual receipt, not its unrelated scientific source.

results=json.loads((BASE/'HOMOGENEOUS_CHARGED_RECORDS_RESULTS.json').read_text())

def guarded_square(spin,z):
    # Independent basis: electric tuples first, then infer matter from local divergence.
    # No fixed external electric divergence. External occupation guards are retained.
    C=s.Integer(spin*(spin+1))
    states=[]
    for es in product(range(-spin,spin+1),repeat=4):
        qs=tuple(es[i]-es[(i-1)%4] for i in range(4))
        if all(abs(q)<=1 for q in qs) and sum(q*q for q in qs)==2:
            states.append((es,qs))
    index={es:i for i,(es,_) in enumerate(states)}
    T=s.zeros(len(states)); costs=[]
    for j,(es,qs) in enumerate(states):
        ns=[q*q for q in qs]
        internal=sum(s.Rational(1,2)*(ns[i]+ns[(i+1)%4]-1)**2 for i in range(4))
        outside=sum(s.Rational(z-2,2)*(ns[i]+(i%2)-1)**2 for i in range(4))
        costs.append(internal+outside)
        for e in range(4):
            for direction in (1,-1):
                x,y=(e,(e+1)%4) if direction==1 else ((e+1)%4,e)
                if qs[x]==0 or qs[y]!=0: continue
                delta=-direction*qs[x]
                if not -spin<=es[e]+delta<=spin: continue
                after=list(es); after[e]+=delta; after=tuple(after)
                i=index[after]
                amp=s.sqrt(1-s.Rational(es[e]*(es[e]+delta),C))
                T[i,j]-=amp
    assert T==T.T
    P=[i for i,c in enumerate(costs) if c==0]
    Q=[i for i,c in enumerate(costs) if c!=0]
    assert all(states[i][1][1]==states[i][1][3]==0 for i in P)
    assert T.extract(P,P)==s.zeros(len(P))
    K=T.extract(Q,P); A=T.extract(Q,Q)
    R=s.diag(*[1/costs[i] for i in Q])
    second=K.T*R*K
    norm=K.T*R**2*K
    h2=-second
    h4=-(K.T*R*A*R*A*R*K)+(norm*second+second*norm)/2
    alpha=z-1
    h2=(alpha*h2).applyfunc(s.simplify)
    h4=(alpha**3*h4).applyfunc(s.simplify)
    ref=next(r for r in results['guarded_square_controls'] if r['spin']==spin and r['bulk_coordination']==z)
    order=[P.index(index[tuple(st['E'])]) for st in ref['low_states']]
    for i,st in enumerate(ref['low_states']):
        assert states[P[order[i]]][1]==tuple(st['q'])
    h2=h2.extract(order,order); h4=h4.extract(order,order)
    reference2=s.Matrix([[s.Rational(x) for x in r] for r in ref['H2_times_Delta']])
    reference4=s.Matrix([[s.Rational(x) for x in r] for r in ref['H4_times_Delta_cubed']])
    assert len(states)==ref['dimension'] and len(P)==ref['code_dimension']
    assert h2==reference2 and h4==reference4
    return {'spin':spin,'bulk_coordination':z,'complete_dimension':len(states),
            'code_dimension':len(P),'basis_method':'Enumerate electric tuples; infer zero-external-divergence charges.',
            'penalty_method':'Sum internal squared occupation defects and fixed external squared defects.',
            'H2_times_Delta':[[str(x) for x in r] for r in h2.tolist()],
            'H4_times_Delta_cubed':[[str(x) for x in r] for r in h4.tolist()],
            'every_entry_equals_recorded_author_result':True}

square_results=[guarded_square(1,6),guarded_square(2,4)]

# Normalize two independently derived formulas symbolically, not by matching floats.
d,K,J,C,t,V0=s.symbols('d K J C t V0',positive=True)
alpha=2*d-1; gamma=2*alpha/(alpha-1)
Delta=alpha*V0
oursK=t**2/(alpha*V0*C)
oursJ=2*t**4/(V0**3*alpha**2*(alpha-1))
authorK=t**2/(Delta*C)
authorJ=gamma*t**4/Delta**3
assert s.simplify(oursK-authorK)==0 and s.simplify(oursJ-authorJ)==0
oursV0=2*K**2*C**2/(J*(alpha-1))
authorV0=gamma*K**2*C**2/(J*alpha)
assert s.simplify(oursV0-authorV0)==0
ours_eps_squared=J*alpha*(alpha-1)/(2*K*C)
author_eps_squared=J/(gamma*K*C)
assert s.simplify(ours_eps_squared-alpha**2*author_eps_squared)==0
ell=2*d*(alpha**2-1)/(alpha**3*(2*alpha-1))
author_scalar=8*d**2*(d-1)/(4*d-3)
assert s.simplify(alpha**3*ell-author_scalar)==0
normalization={'alpha':'2*d-1','Delta':'alpha*V0','epsilon_independent':'t/V0',
    'epsilon_author':'t/Delta = epsilon_independent/alpha',
    'same_K':str(s.factor(oursK)),'same_J':str(s.factor(oursJ)),
    'same_V0_schedule':str(s.factor(oursV0)),
    'epsilon_independent_squared':str(s.factor(ours_eps_squared)),
    'epsilon_author_squared':str(s.factor(author_eps_squared)),
    'fourth_scalar_relation':'author c_d = alpha^3 * independent ell_d',
    'same_birth_exponent':'3*d; beta0 differs by a fixed alpha^(3*d) if comparing the same numerical beta.',
    'same_order':'m=3*d+6; full speed O(epsilon^-3), remainder-source volume error O(epsilon^3).'}

# Closed combinatorial control of the selected-edge halo, independent of 2^16 enumeration.
expected_grade={str(g):256*sum(comb(3,i)*comb(3,j) for i in range(4) for j in range(4) if j-i==g)
                for g in range(-3,4)}
occupation=json.loads((BASE/'HOMOGENEOUS_OCCUPANCY_PENALTY_RESULTS.json').read_text())
assert expected_grade==occupation['hop_grade_multiplicities']
assert sum(expected_grade.values())==occupation['complete_hop_count']==16384
assert sum(occupation['penalty_eigenvalue_multiplicities'].values())==65536

# Compare author combinatorics with PRE independently assembled cubic graphs.
blind=json.loads((HERE/'ALGEBRA_BULK_RESULTS.json').read_text())
# Parse only recorded fields; prove counts directly from torus incidence formulas.
cubic=[]
for r in results['cubic_controls']:
    dd=r['dimension']; vertices=r['vertices']; edges=dd*vertices; aa=2*dd-1
    meet=vertices*(2*dd)*(2*dd-1)//2
    r2=edges*(dd-1); r1=edges*((2*dd-1)**2-2*(dd-1))
    r0=edges*(edges-1)//2-meet-r2-r1
    assert r['pair_counts']=={'meet':meet,'r0':r0,'r1':r1,'r2':r2}
    scalar=s.Rational(8*dd**2*(dd-1),4*dd-3)*vertices
    assert scalar==s.Rational(r['unit_shift_diagonal_constant'])
    assert s.Rational(r['oriented_plaquette_gamma'])==s.Rational(2*aa,aa-1)
    for exchange in r['local_exchange_controls']:
        assert exchange['two_orientations_same_joint_target']==(exchange['charge_pair']=='opposite')
        for orientation in exchange['orientations']:
            paths=orientation['paths']
            assert len(paths)==4
            assert all(p['denominators']==[aa,2*(aa-1),aa] for p in paths)
            assert {tuple(p['order']) for p in paths}=={(0,2,1,3),(0,2,3,1),(2,0,1,3),(2,0,3,1)}
    cubic.append({'dimension':dd,'vertices':vertices,'pair_counts':r['pair_counts'],
                  'author_Delta_units_scalar':str(scalar),
                  'same_scalar_in_V0_units':str(scalar/aa**3),
                  'scope':'Counts and recorded path denominators authenticated/algebraically compared; no replay of the author cubic routine.'})

# Authenticate current receipts and archived initial failure without resolving stale paths to current bytes.
receipts=[]
for prefix in ['HOMOGENEOUS_CHARGED_RECORDS_CHECK','HOMOGENEOUS_OCCUPANCY_PENALTY_CHECK']:
    p=BASE/(prefix+'_RECEIPT.json'); data=json.loads(p.read_text())
    assert data['exit_code']==0
    verify([data['source'],data['stdout'],data['stderr']])
    results_path=BASE/('HOMOGENEOUS_CHARGED_RECORDS_RESULTS.json' if 'CHARGED_RECORDS' in prefix else 'HOMOGENEOUS_OCCUPANCY_PENALTY_RESULTS.json')
    assert Path(data['stdout']['path']).read_bytes()==results_path.read_bytes()
    receipts.append({'receipt':row(p),'exit_code':0,'all_three_bound_files_verified':True,'stdout_equals_results':True})
history=BASE/'homogeneous_charged_source_history/initial_edge_index_failure'
old=json.loads((history/'HOMOGENEOUS_CHARGED_RECORDS_CHECK_RECEIPT.json').read_text())
for role in ['source','stdout','stderr']:
    rr=old[role]
    actual=row(history/Path(rr['path']).name)
    assert actual['sha256']==rr['sha256'] and actual['bytes']==rr['bytes']
assert old['exit_code']==1
old_text=(history/'homogeneous_charged_records_check.py').read_text()
new_text=(BASE/'homogeneous_charged_records_check.py').read_text()
a='eindex={(x,a):i*d+a for i,x in enumerate(vertices)}'
b='eindex={(x,a):i*d+a for i,x in enumerate(vertices) for a in range(d)}'
assert old_text.count(a)==1 and old_text.replace(a,b)==new_text
failure={'preserved':True,'original_exit_code':1,'type':'UnboundLocalError in geometry-index comprehension',
    'exact_delta_only':'Add missing for a in range(d) to the edge-index dictionary comprehension.',
    'archived_receipt_rebound_by_basename_to_recorded_recovery_directory':True,
    'rerun_of_failed_author_attempt':False,'scientific_assertions_changed':False}

out={'created_utc':datetime.now(timezone.utc).isoformat(),'runner':row(__file__),
    'pre_seal':row(pre_path),'author_seal':row(author_path),
    'authentication':{'PRE_bindings':pre_count,'author_bindings':author_count,'context_bindings':context_count},
    'independent_guarded_square_controls':square_results,'symbolic_normalization':normalization,
    'independent_halo_count':expected_grade,'cubic_comparison':cubic,'author_receipts':receipts,
    'preserved_author_failure':failure,'new_failed_executions':[],
    'finding':'No material discrepancy found in the bounded comparison.',
    'limits':['Only two author guarded-square physical sectors were independently rebuilt in this comparison.',
              'No full author suite rerun; all scripts, results and their source-bound streams were read/authenticated.',
              'Unrelated charged-band/phase and finite-rate formation sources remain unopened.',
              'Finite exact checks support coefficients; the uniform-volume statement is assessed through its explicit proof and pinned prior machinery.']}
OUT.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
