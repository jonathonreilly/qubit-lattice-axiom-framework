"""Immutable source-bound PRE for the original-cube consequence."""
from pathlib import Path
import hashlib,json,datetime

HERE=Path(__file__).resolve().parent
def ident(p):
    b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
destination=HERE/'PRE_COMPARISON_SEAL.json'
assert not destination.exists(),'Never overwrite PRE.'
source=json.loads((HERE/'SOURCE_IDENTITIES.json').read_text())
for item in source['science_sources']:
    assert ident(Path(item['path']))==item
prior=json.loads(Path(source['science_sources'][0]['path']).read_text())
for item in prior['independent_artifacts']:
    assert ident(Path(item['path']))==item
receipts=[]
for stem in ('cube_controls','count_bound','source'):
    p=HERE/(stem+'_RECEIPT.json');r=json.loads(p.read_text())
    assert r['exit_code']==0
    assert ident(Path(r['command'][1]))['sha256']==r['script_sha256']
    for stream in ('stdout','stderr'):
        assert ident(HERE/(stem+'.'+stream))['sha256']==r[stream+'_sha256']
    receipts.append(ident(p))
artifacts=[ident(p) for p in sorted(HERE.iterdir()) if p.is_file()]
seal={
    'phase':'PRE_COMPARISON',
    'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'status':'Complete conditional independent consequence reconstruction before candidate access; not a formal retained/audit/no-go verdict.',
    'scope':'Original eight-vertex cube, all A plus/B vacant, fixed normalizable physical field with trace-convergent spin embeddings, eta=K S(S+1)=delta/epsilon^2, fixed compact time intervals and fixed finite electric windows, both stipulated creation instruments.',
    'provisional_dependency':source['provisional_dependency'],
    'candidate_exposure':'No cube_unprepared_author or cube_point_spectrum_author read. No candidate formula or freeze identity supplied. Mathematical progress findings were sent to the coordinator before this PRE; no reciprocal author blindness is asserted.',
    'result':'N4 trace-norm limit exp(-48 kappa t) times generated electric/face field evolution. Actual first-source trace-norm convergence and positive compact-source covering upgrade N6 time-averaged local escape to uniform compact-time local disappearance; N8 follows by finite jump range. Full local trace exp(-48 kappa t), hence no full trace-norm convergent subsequence at fixed t>0. Global first-count limit and explicit N6/N8 bounds; no unique second-count law claimed. Deterministic microscopic transfer by the parent estimate.',
    'counterexamples_preserved':['Finite-spin zero-field first clock is not exactly exponential: spin-one survival cubic difference224 for K=delta=kappa=1','Eight next-birth paths do not imply an eight-unit loss bound: compact rotor expectation10 and finite-S expectation>8','Bounded rapidly varying positive sources can refocus despite time-averaged escape; actual source compactness is required','Translated absorbing N8 states vanish in fixed windows while retaining unit N8 count; not asserted to be actual original-state outputs'],
    'uniform_loss_bounds':'R4,S<=48 I and R6,S<=16 I; coherent/resolved total losses agree. All are complete physical-space bounds.',
    'science_sources':source['science_sources'],
    'own_previous_artifacts_authenticated':len(prior['independent_artifacts']),
    'read_boundary':source['read_boundary'],
    'actual_execution_receipts':receipts,
    'independent_artifacts':artifacts,
    'execution_limits':'No failed execution discarded; all three commands exited zero. No full five-dimensional spin evolution or quantitative convergence rate claimed. No prior science builder imported.',
    'authority_limits':'No Git operation, new proposal/counterterm read, broader research scan, onward delegation, publication, formal audit, or no-go packet PASS.',
    'preservation':'All bound PRE bytes are immutable. Any post-comparison correction must be recorded separately with its source exposure.'
}
destination.write_text(json.dumps(seal,indent=2)+'\n')
print(json.dumps({'seal':ident(destination),'sources':len(source['science_sources']),'artifacts':len(artifacts),'all_receipts_exit_zero':True},indent=2))
