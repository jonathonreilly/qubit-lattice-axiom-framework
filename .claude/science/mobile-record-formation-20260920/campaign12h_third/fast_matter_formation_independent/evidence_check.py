"""Authenticate authorized packet and reconstruct one no-event endpoint independently."""
from pathlib import Path
import sys,json,hashlib,difflib,math
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;BASE=HERE.parent
sys.path.insert(0,str(BASE/'finite_formation_independent'))
from finite_control import model,npmat
import numpy as np
from scipy.linalg import expm

def sha(q):return hashlib.sha256(q.read_bytes()).hexdigest()
seal=BASE/'FAST_MATTER_FORMATION_AUTHOR_SEAL.json'
assert sha(seal)=='5aeee4c3db513daafc32c22ceb7e2a7c5dc0c1a3e7d89208fec4244806c67577'
obj=json.loads(seal.read_text())
for row in obj['artifacts']:
    q=Path(row['path']);assert q.stat().st_size==row['bytes'] and sha(q)==row['sha256']

historical=[
 ('fast_matter_formation_history/initial_polar_orthogonality','fast_matter_formation_check.py','FAST_MATTER_FORMATION_CHECK_RECEIPT.json'),
 ('first_formation_field_history/initial_eigenbasis_condition','first_formation_field_check.py','FIRST_FORMATION_FIELD_CHECK_RECEIPT.json'),
 ('first_formation_field_history/subtractive_distance_roundoff','first_formation_field_check.py','FIRST_FORMATION_FIELD_SCHUR_CHECK_RECEIPT.json')]
history=[];diffs=[]
for rel,name,receipt in historical:
    directory=BASE/rel;r=json.loads((directory/receipt).read_text())
    for key in ['source','stdout','stderr']:
        old=r[key];q=directory/Path(old['path']).name
        assert q.stat().st_size==old['bytes'] and sha(q)==old['sha256']
    history.append({'archive':rel,'receipt_recovery_verified':True,'exit_code':r['exit_code']})
    diffs.append(''.join(difflib.unified_diff((directory/name).read_text().splitlines(True),(BASE/name).read_text().splitlines(True),fromfile=rel+'/'+name,tofile=name)))
oldbase=BASE/'fast_matter_formation_history/before_cubic_period_qualification'
oldseal=json.loads((oldbase/'FAST_MATTER_FORMATION_AUTHOR_SEAL.json').read_text())
for row in oldseal['artifacts']:
    q=Path(row['path'])
    if q.name=='FINITE_FORMATION_WITH_RETAINED_FOURTH_ORDER_DYNAMICS.md':q=oldbase/q.name
    assert q.stat().st_size==row['bytes'] and sha(q)==row['sha256']
diffs.append(''.join(difflib.unified_diff((oldbase/'FINITE_FORMATION_WITH_RETAINED_FOURTH_ORDER_DYNAMICS.md').read_text().splitlines(True),(BASE/'FINITE_FORMATION_WITH_RETAINED_FOURTH_ORDER_DYNAMICS.md').read_text().splitlines(True),fromfile='before_period_qualification',tofile='current_note')))
(HERE/'AUTHOR_HISTORY_DIFFS.txt').write_text('\n'.join(diffs))
for stem in ['FAST_MATTER_FORMATION_REPAIRED_CHECK','FIRST_FORMATION_FIELD_STABLE_CHECK']:
    r=json.loads((BASE/(stem+'_RECEIPT.json')).read_text());assert r['exit_code']==0
    for key in ['source','stdout','stderr']:
        row=r[key];q=Path(row['path']);assert q.stat().st_size==row['bytes'] and sha(q)==row['sha256']

fast=json.loads((BASE/'FAST_MATTER_FORMATION_RESULTS.json').read_text())
first=json.loads((BASE/'FIRST_FORMATION_FIELD_RESULTS.json').read_text())
assert fast['source_sha256']==sha(BASE/'fast_matter_formation_check.py')
assert first['source_sha256']==sha(BASE/'first_formation_field_check.py')
for x in fast['full_density_comparisons']:
    assert abs(x['trace_norm_error']/x['epsilon']-x['error_divided_by_epsilon'])<1e-12
    for kind in ['microscopic','target']:
        vals=[z[kind] for z in x['counts'].values()]
        assert abs(sum(vals)-1)<2e-9 and min(vals)>-2e-9
for x in first['rows']:
    for r in x['times']:
        a=r['microscopic_no_event_probability'];b=r['rotor_no_event_probability'];e=r['unnormalized_density_trace_error'];c=r['conditional_field_trace_error']
        assert abs(b-math.exp(-first['first_rate']*r['time']))<1e-14
        assert 0<=a<=1+1e-9 and 0<=c<=2+1e-9 and e>=abs(a-b)-1e-11
        assert abs(e*e-(a-b)**2-a*b*c*c)<1e-11
        assert abs(e/x['epsilon']-r['trace_error_divided_by_epsilon'])<1e-12

# Complete electric-tuple Gauss builder, distinct from author's site-word/circulation builder.
spin=4;C=spin*(spin+1);delta=1.3;kappa=.7;epsilon=math.sqrt(delta/C);time=.25
m=model(4,{0,2},[(0,1),(1,2),(2,3),(3,0)],spin)
idx=[i for i,n in enumerate(m['Ns']) if n==2];states=[m['states'][i] for i in idx]
T=npmat(m['T'].extract(idx,idx));W=npmat(m['W'].extract(idx,idx));loss=npmat(m['Gamma'].extract(idx,idx))
H=delta*W/epsilon**4+delta*T/epsilon**3
NH=H-.5j*kappa*loss/epsilon**2
bg=(1,0,1,0);g=np.zeros(len(idx),complex)
g[states.index(((0,0,0,0),bg))]=g[states.index(((1,1,1,1),bg))]=1/math.sqrt(2)
actual=expm(-1j*time*NH)@g
cut=20;flux=np.arange(-cut,cut+1);J=2*delta;rate=8*kappa
HR=np.diag(4*flux*flux).astype(float)+np.diag(np.full(2*cut,-J),1)+np.diag(np.full(2*cut,-J),-1)
initial=np.zeros(2*cut+1,complex);initial[cut]=initial[cut+1]=1/math.sqrt(2)
target=math.exp(-rate*time/2)*(expm(-1j*time*HR)@initial)
outside=[int(f) for f in flux if abs(f)>spin]
x=np.pad(actual,(0,len(outside)));y=np.zeros_like(x)
for f,z in zip(flux,target):
    if abs(f)<=spin:y[states.index(((int(f),)*4,bg))]=z
    else:y[len(idx)+outside.index(int(f))]=z
diff=np.outer(x,x.conjugate())-np.outer(y,y.conjugate())
distance=float(np.abs(np.linalg.eigvalsh((diff+diff.conjugate().T)/2)).sum())
prob=float(np.vdot(actual,actual).real)
ref=next(r for r in next(v for v in first['rows'] if v['spin']==spin)['times'] if r['time']==time)
assert abs(prob-ref['microscopic_no_event_probability'])<1e-11
assert abs(distance-ref['unnormalized_density_trace_error'])<1e-11

out={'author_seal_bindings_verified':len(obj['artifacts']),'old_seal_recovered_rows':len(oldseal['artifacts']),'historical_receipts':history,'author_fast_density_rows_parsed_and_sanity_checked':len(fast['full_density_comparisons']),'author_first_event_rows_parsed_and_probability_distance_checked':sum(len(r['times']) for r in first['rows']),'maximum_author_trace_error_over_epsilon':max(r['error_divided_by_epsilon'] for r in fast['full_density_comparisons']),'independent_first_event_endpoint':{'spin':spin,'time':time,'physical_full_dimension':len(m['states']),'N2_dimension':len(idx),'rotor_cutoff':cut,'method':'complete electric-tuple construction; direct matrix exponential; explicit enlarged-space density-difference eigenvalues','no_event_probability':prob,'trace_error':distance,'probability_difference_from_author':abs(prob-ref['microscopic_no_event_probability']),'trace_error_difference_from_author':abs(distance-ref['unnormalized_density_trace_error'])},'limits':'Author grid not rerun. Cutoff control is numerical, not a rigorous tail certificate. Independent analytic proof review is in REPORT.md. No author builders imported.'}
(HERE/'EVIDENCE_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
