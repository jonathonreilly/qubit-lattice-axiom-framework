#!/usr/bin/env python3
"""Post-seal selective author comparison, without executing author main/imports."""
from pathlib import Path
import ast,datetime,hashlib,importlib.util,itertools,json,math,sys
import numpy as np
import sympy as sp
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;RAW=HERE.parent
def identity(path):
    return {'path':str(path),'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
def load(path):return json.loads(path.read_text())
pre=load(HERE/'PRE_COMPARISON_SEAL.json')
for row in pre['artifacts']:assert identity(Path(row['path']))['sha256']==row['sha256']
author=RAW/'geometric_polynomial_relaxation_check.py'
assert identity(author)['sha256']=='fded420e936b93bee16aeba4bfed676363d0298e6c1268fa5193cea5ef0c0202'
parsed=ast.parse(author.read_text())
selected=[n for n in parsed.body if isinstance(n,ast.FunctionDef) and n.name in ['matrix','positive_gap','killing_one']]
assert len(selected)==3
ns={'np':np,'math':math}
exec(compile(ast.Module(body=selected,type_ignores=[]),str(author),'exec'),ns)
spec=importlib.util.spec_from_file_location('independent_polynomial_check',HERE/'independent_check.py')
own=importlib.util.module_from_spec(spec);spec.loader.exec_module(own)
own_results=load(HERE/'INDEPENDENT_RESULTS.json')
matrix_comparisons=[]
for row in own_results['graphs']:
    d=own.assemble(row['vertices'],row['edges'])
    G={'sites':tuple(range(row['vertices'])),'edges':sorted(d['edges'])}
    LS,LT,LB,A,h=ns['matrix'](G,list(map(frozenset,d['near'])),list(map(frozenset,d['full'])))
    assert sp.Matrix(LS)==d['L'] and sp.Matrix(LB)==d['B'] and sp.Matrix(A)==d['A']
    assert np.max(abs(LT-np.array(d['T'],dtype=float)))<1e-12
    assert sp.Matrix(h)==d['h']
    matrix_comparisons.append({'case':row['name'],'near':d['n'],'full':d['Z'],'integer_matrices_identical':True})

author_result=load(RAW/'geometric_polynomial_relaxation_checks/RESULTS.json')
for name,digest in author_result['sources_sha256'].items():
    assert identity(RAW/name)['sha256']==digest
groups={x['name']:x for x in author_result['rows']}
assert len(groups)==4 and all(x['pass'] is True for x in groups.values())
g1=author_result['rows'][0]
assert len(g1['rows'])==g1['graphs']==123
assert sum(x['routed_pairs'] for x in g1['rows'])==g1['routed_pairs']==3776
for row in g1['rows']:
    K=row['vertices']//2;C=1+2*K*(K-1)
    assert row['routed_pairs']==row['full']*K*K
    assert row['max_length']<=2*(K-1)
    assert row['max_reference_matchings_per_micro_edge']<=2
    assert row['max_micro_edge_path_count']<=2*K*K
    assert row['trace_gap']+1e-10>=row['Broder_gap']
    assert row['slide_gap']+1e-10>=row['trace_gap']/C
    bound=1/(256*row['edges']*(row['near']/row['full'])**4*C)
    assert math.isclose(row['lower_bound'],bound,rel_tol=1e-14)
    assert row['slide_gap']>=bound

name_map={'path4':'path4','cycle4':'cycle4','cycle6':'cycle6','K4':'complete4','odd_barbell':'triangles_with_bridge'}
independent_by_name={x['name']:x for x in own_results['graphs']}
exact_rows=[]
for row in author_result['rows'][1]['rows']:
    fixture=independent_by_name[name_map[row['case']]]
    d=own.assemble(fixture['vertices'],fixture['edges'])
    conductance=own.exact_conductance(d['P'])
    imported=sp.Rational(1,16*len(d['edges']))*sp.Rational(d['Z'],d['n'])**2
    beta=sp.Rational(1,13)
    U=(d['L']+beta*d['H']).inv()*beta*d['A']
    mean=(d['L']+beta*d['H']).inv()*sp.ones(d['n'],1)
    recomputed={'conductance':str(conductance),'imported_lower_bound':str(imported),
                'hazard_mean':str(sp.Rational(sum(d['h']),d['n'])),
                'uniform_exit_error_max':str(max(abs(x-sp.Rational(1,d['Z'])) for x in U)),
                'mean_clock_stationary':str(sum(mean)/d['n'])}
    for key,val in recomputed.items():assert row[key]==val,(row,key,val)
    exact_rows.append({'case':row['case'],'all_five_reported_rational_values_recomputed':True})

# Read and authenticate the entire JSON stream, including every author log row.
def json_stream(path):
    text=path.read_text();decoder=json.JSONDecoder();values=[];pos=0
    while pos<len(text):
        while pos<len(text) and text[pos].isspace():pos+=1
        if pos==len(text):break
        value,pos=decoder.raw_decode(text,pos);values.append(value)
    return values
log_path=RAW/'GEOMETRIC_POLYNOMIAL_RELAXATION_RUN.log'
log_values=json_stream(log_path)
assert log_values[:-1]==author_result['rows']
assert log_values[-1]=={'groups':4,'sources_sha256':author_result['sources_sha256']}
stderr=RAW/'GEOMETRIC_POLYNOMIAL_RELAXATION_RUN.stderr';assert stderr.read_bytes()==b''
killing_rows=author_result['rows'][2]['rows']
assert len(killing_rows)==35
for row in killing_rows:
    r=row['beta_times_T'];assert row['exit_TV']<=min(1,2*r)+1e-8
    if 2*r<1:assert row['relative_mean_error']<=2*r/(1-2*r)+1e-8
    assert row['max_joint_subset_transform_error']<=8*r+1e-8

# The centered Schur solver is tested on a separate 12-state path with endpoint
# killing and a direct exact rational inverse at each of its five chosen rates.
n=12;L=sp.zeros(n)
for i in range(n-1):L[i,i]+=1;L[i+1,i+1]+=1;L[i,i+1]-=1;L[i+1,i]-=1
A=sp.zeros(n,2);A[0,0]=A[-1,1]=1;h=A*sp.ones(2,1);H=sp.diag(*h)
checked=ns['killing_one']('independent_path12',np.array(L,dtype=float),np.array(A,dtype=float),np.array(h,dtype=float).ravel())
checks=[]
for row in checked:
    TG=(1+math.log(n))/row['gap'];beta=sp.Rational(row['beta_times_T']/TG);p=sp.Rational(2,n)
    U=(L+beta*H).inv()*beta*A
    tv=max(sum(abs(U[i,j]-sp.Rational(1,2)) for j in range(2))/2 for i in range(n))
    z=beta*p*(L+beta*H).inv()*sp.ones(n,1)
    err=max(abs(x-1) for x in z)
    assert abs(float(tv)-row['exit_TV'])<1e-11
    assert abs(float(err)-row['relative_mean_error'])<1e-11
    joint=0
    for lam in [sp.Integer(0),sp.Rational(1,4),sp.Integer(1),sp.Integer(3)]:
        X=(L+beta*(H+lam*p*sp.eye(n))).inv()*beta*A-sp.ones(n,2)/(2*(1+lam))
        joint=max(joint,max(max(sum(max(x,0) for x in X[i,:]),sum(max(-x,0) for x in X[i,:])) for i in range(n)))
    assert abs(float(joint)-row['max_joint_subset_transform_error'])<1e-11
    checks.append({'beta_times_T':row['beta_times_T'],'exact_rational_TV':str(tv),
                   'exact_scaled_mean_error':str(err),'maximum_numeric_difference':max(abs(float(tv)-row['exit_TV']),abs(float(err)-row['relative_mean_error']),abs(float(joint)-row['max_joint_subset_transform_error']))})

function=next(x for x in parsed.body if isinstance(x,ast.FunctionDef) and x.name=='killing_bounds')
selection=next(x for x in ast.walk(function) if isinstance(x,ast.Compare) and isinstance(x.left,ast.Name) and x.left.id=='name')
selectors=ast.literal_eval(selection.comparators[0])
graph_names={x['case'] for x in g1['rows']}
missing=sorted(set(selectors)-graph_names)
assert missing==['cycle6'] and 'cycle_6' in graph_names
assert 'cycle6' not in {x['case'] for x in killing_rows}
dev=RAW/'geometric_polynomial_relaxation_development'
evidence=[RAW/'geometric_polynomial_relaxation_checks/RESULTS.json',log_path,stderr,
          RAW/'GEOMETRIC_POLYNOMIAL_RELAXATION_LITERATURE_RECEIPT.json',
          RAW/'geometric_general_graph_check.py',
          dev/'attempt01_geometric_polynomial_relaxation_check.py',
          dev/'attempt01_GEOMETRIC_POLYNOMIAL_RELAXATION_RUN.log',
          dev/'attempt01_GEOMETRIC_POLYNOMIAL_RELAXATION_RUN.stderr']
failed_log=json_stream(dev/'attempt01_GEOMETRIC_POLYNOMIAL_RELAXATION_RUN.log')
assert failed_log==author_result['rows'][:2]
assert 'U.sum(axis=1)-1' in (dev/'attempt01_GEOMETRIC_POLYNOMIAL_RELAXATION_RUN.stderr').read_text()
result={'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'precomparison_seal':identity(HERE/'PRE_COMPARISON_SEAL.json'),
        'author_evidence_sources':list(map(identity,evidence)),
        'integer_and_trace_matrix_comparisons':matrix_comparisons,
        'exact_author_rows_independently_recomputed':exact_rows,
        'centered_solver_exact_path12_controls':checks,
        'all_recorded_rows_checked_for_internal_arithmetic_and_log_identity':True,
        'author_groups':4,'author_graph_cases_authenticated':123,
        'author_routed_pairs_including_zero_length_self_pairs':3776,
        'author_killing_rows_authenticated':35,
        'not_claimed':'Entire author suite rerun, independently reconstructed 1989/Taggi theorem proofs, or production simulation review.',
        'findings':[{'id':'F1','severity':'minor executable coverage omission','line':selection.lineno,
                     'source_sha256':identity(author)['sha256'],
                     'actual':'killing_bounds selects cycle6; graph_cases supplies cycle_6, silently omitting this intended numerical killing fixture.',
                     'correction':'Replace only cycle6 by cycle_6 in the killing_bounds selector and rerun that affected group, retaining old outputs.',
                     'impact':'No theorem defect; exact_small_controls already checks cycle6, and the independent precomparison suite also checks its killed resolvent.'}],
        'failed_attempts_reviewed':{'independent':'Unsimplified symbolic structural equality; preserved checker and raw logs.',
                                    'author':'Unscaled ill-conditioned killed solve failed row-normalization assertion; preserved original, changed to a mathematically checked centered Schur calculation.'}}
(HERE/'AUTHOR_COMPARISON.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
print(json.dumps({k:result[k] for k in ['author_groups','author_graph_cases_authenticated','author_killing_rows_authenticated','findings']},indent=2))
print('Compared 11 matrix assemblies, 25 exact published rational values, and 5 stabilized solver cases against exact inverses.')
