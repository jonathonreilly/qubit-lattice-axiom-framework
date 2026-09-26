#!/usr/bin/env python3
"""F1-only acknowledgment: exact delta, preserved seals and five C6 rates."""
from pathlib import Path
import ast,datetime,difflib,hashlib,importlib.util,json,math,sys
import numpy as np
import sympy as sp
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;REVIEW=HERE.parent;RAW=REVIEW.parent
FIX=RAW/'geometric_polynomial_fixture_fix'
OLD=FIX/'before_geometric_polynomial_relaxation_check.py'
NEW=RAW/'geometric_polynomial_relaxation_check.py'
def identity(p):
    p=Path(p);return {'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def load(p):return json.loads(p.read_text())
assert identity(OLD)['sha256']=='fded420e936b93bee16aeba4bfed676363d0298e6c1268fa5193cea5ef0c0202'
assert identity(NEW)['sha256']=='996c2098b94a0f3e3331cfb7152af40bf18e7b6307e5a806204e9569e04478f0'
old_line=b"if name not in ['all_four_63','cycle6','cube','odd_barbell','path_10']:continue"
new_line=old_line.replace(b"'cycle6'",b"'cycle_6'")
assert OLD.read_bytes().count(old_line)==1 and NEW.read_bytes().count(new_line)==1
assert OLD.read_bytes().replace(old_line,new_line)==NEW.read_bytes()
assert NEW.read_bytes().replace(new_line,old_line)==OLD.read_bytes()
assert identity(RAW/'GEOMETRIC_POLYNOMIAL_RELAXATION_AND_FORMATION.md')['sha256']=='f9d12f1fccc3ea54d3b640deaccdcbb04749db1d6ac5b7b2708193a4a0dd89bb'
delta=''.join(difflib.unified_diff(OLD.read_text().splitlines(True),NEW.read_text().splitlines(True),fromfile=str(OLD),tofile=str(NEW)))
(HERE/'VERIFIED_SOURCE_DELTA.diff').write_text(delta)

old_seals=[]
for filename,digest in [('PRE_COMPARISON_SEAL.json','2b20f617c76901ce78756702c6fac7a4390eec56776db74caef8a4caba14c8fd'),
                        ('FINAL_SEAL.json','44a5aa64f67c3570c4f3eeee106f314381c890492e4ba582f2bee457e262dc97')]:
    path=REVIEW/filename;assert identity(path)['sha256']==digest
    seal=load(path);rows=[]
    for key in ['sources','procedures_reused','dependencies_reused','external_extracts','artifacts']:
        rows.extend(seal[key])
    if 'precomparison_seal' in seal:rows.append(seal['precomparison_seal'])
    substitutions=[]
    for row in rows:
        declared=Path(row['path']);actual=OLD if declared==NEW else declared
        current=identity(actual)
        assert current['sha256']==row['sha256'] and current['bytes']==row['bytes'],(declared,current,row)
        if actual!=declared:substitutions.append({'original_binding':row,'preserved_source':current})
    old_seals.append({'seal':identity(path),'bindings_authenticated':len(rows),'old_runner_substitutions':substitutions})

prior=load(RAW/'geometric_polynomial_relaxation_checks/RESULTS.json')
fixed=load(FIX/'RESULTS.json')
assert fixed['original_results_sha256']==identity(RAW/'geometric_polynomial_relaxation_checks/RESULTS.json')['sha256']
assert fixed['old_source_sha256']==identity(OLD)['sha256'] and fixed['new_source_sha256']==identity(NEW)['sha256']
assert fixed['pass'] is True and len(fixed['rows'])==40
added=[r for r in fixed['rows'] if r['case']=='cycle_6']
reused=[r for r in fixed['rows'] if r['case']!='cycle_6']
assert len(added)==fixed['cycle_6_rows_added']==5
assert len(reused)==fixed['previous_rows_rechecked']==35
assert reused==prior['rows'][2]['rows']
assert fixed['maximum_delta_on_previous_rows']==0.0
assert (FIX/'RUN.stderr').read_bytes()==b''
decoder=json.JSONDecoder();text=(FIX/'RUN.log').read_text();pos=0;log=[]
while pos<len(text):
    while pos<len(text) and text[pos].isspace():pos+=1
    if pos==len(text):break
    value,pos=decoder.raw_decode(text,pos);log.append(value)
assert len(log)==2 and log[0]['rows']==fixed['rows'] and log[0]['pass'] is True
assert log[1]=={k:fixed[k] for k in ['cycle_6_rows_added','previous_rows_rechecked','maximum_delta_on_previous_rows','pass']}

# Reuse our unchanged independently assembled C6 generator. Extract only the
# author's pure numerical helper: no main, imports or other fixture execution.
spec=importlib.util.spec_from_file_location('own_polynomial',REVIEW/'independent_check.py')
own=importlib.util.module_from_spec(spec);spec.loader.exec_module(own)
data=own.assemble(6,[(i,(i+1)%6) for i in range(6)])
assert (data['n'],data['Z'])==(9,2)
tree=ast.parse(NEW.read_text())
selected=[f for f in tree.body if isinstance(f,ast.FunctionDef) and f.name in ['positive_gap','killing_one']]
assert len(selected)==2
ns={'np':np,'math':math};exec(compile(ast.Module(body=selected,type_ignores=[]),str(NEW),'exec'),ns)
rows=ns['killing_one']('cycle_6',np.array(data['L'],dtype=float),np.array(data['A'],dtype=float),np.array(data['h'],dtype=float).ravel())
assert rows==added
exact_controls=[]
for row in rows:
    n,Z=data['n'],data['Z'];L,H,A=data['L'],data['H'],data['A'];p=sp.Rational(2,3)
    TG=(1+math.log(n))/row['gap'];beta=sp.Rational(row['beta_times_T']/TG)
    U=(L+beta*H).inv()*beta*A
    tv=max(sum(abs(U[i,j]-sp.Rational(1,Z)) for j in range(Z))/2 for i in range(n))
    z=beta*p*(L+beta*H).inv()*sp.ones(n,1);err=max(abs(x-1) for x in z)
    joint=sp.Integer(0)
    for lam in [sp.Integer(0),sp.Rational(1,4),sp.Integer(1),sp.Integer(3)]:
        X=(L+beta*(H+lam*p*sp.eye(n))).inv()*beta*A-sp.ones(n,Z)/(Z*(1+lam))
        for i in range(n):
            for subset in [[],[0],[1],[0,1]]:
                joint=max(joint,abs(sum(X[i,j] for j in subset)))
    dif=max(abs(float(tv)-row['exit_TV']),abs(float(err)-row['relative_mean_error']),abs(float(joint)-row['max_joint_subset_transform_error']))
    assert dif<1e-12
    exact_controls.append({'beta_times_T':row['beta_times_T'],'beta_exact_binary_float_value':str(beta),
                           'exit_TV_exact':str(tv),'scaled_mean_error_exact':str(err),
                           'joint_event_error_exact':str(joint),'maximum_numeric_difference':dif})

sources=[OLD,NEW,RAW/'GEOMETRIC_POLYNOMIAL_RELAXATION_AND_FORMATION.md',
         RAW/'GEOMETRIC_POLYNOMIAL_FIXTURE_CORRECTION.md',FIX/'check_correction.py',FIX/'RESULTS.json',FIX/'RUN.log',FIX/'RUN.stderr',
         RAW/'geometric_polynomial_relaxation_checks/RESULTS.json',REVIEW/'REPORT.md',REVIEW/'independent_check.py']
result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'scope':'Narrow polynomial F1 correction acknowledgment only; prior mathematical review unchanged.',
        'finding':'F1 closed: cycle_6 is selected and contributes its five intended numerical killing rows.',
        'exact_one_line_forward_and_inverse_delta_verified':True,
        'old_seals_authenticated':old_seals,'sources':list(map(identity,sources)),
        'previous_35_rows_exactly_unchanged':True,'new_rows':5,'replayed_rows_match_author_exactly':True,
        'exact_inverse_controls':exact_controls,'new_failures':[],
        'limits':['Only the affected C6 fixture rerun, not unrelated author groups.',
                  'Old result bindings authenticated through preserved old runner bytes; they do not bind the corrected runner.',
                  'No primary edits, production observables, Git changes or formal audit disposition.']}
(HERE/'CORRECTION_ACK.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
print(json.dumps({'F1':'closed','old_seal_binding_counts':[x['bindings_authenticated'] for x in old_seals],
                  'new_cycle6_rows':5,'previous_rows_exactly_unchanged':35,
                  'largest_exact_vs_numeric_difference':max(x['maximum_numeric_difference'] for x in exact_controls)},indent=2))
