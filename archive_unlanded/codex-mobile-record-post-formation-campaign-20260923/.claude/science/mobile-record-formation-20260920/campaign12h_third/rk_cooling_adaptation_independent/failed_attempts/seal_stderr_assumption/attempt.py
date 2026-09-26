from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,platform,sys
import numpy,scipy,sympy
b=Path('/Users/jonreilly/Documents/Codex/mobile-record-formation-20260920/.claude/science/mobile-record-formation-20260920/campaign12h_third/rk_cooling_adaptation_independent'); a=b.parent
row=lambda p:{'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
expected={
'LOCAL_GAUGE_RECORD_COOLING_TO_RK_STATES.md':'7fa8e6b7a84b3467b784283f596ef192ceab6fbc18172f18fd93e1d139a2791f',
'gauge_readout_cooling_independent/REPORT.md':'d72068c4dae9a210224f5c7217dc9b6ded91ea0422f7f14ec9ff1b659302747f',
'gauge_readout_cooling_independent/cooling_check.py':'cce65c2ad05e2956bf1d9b5786435b07b1e99bb9705505a57b3b375172cffcc9',
'gauge_readout_cooling_independent/COOLING_RESULTS.json':'0707122f13d02f7c283df20dd8f50543872f97266311b9c598ac93573fbba0e4',
'gauge_readout_cooling_independent/FINAL_SEAL.json':'24abda952a7f728c5408dc5846dc4fdf7cc913c5552d12fe50b4a773c550eb81'}
sources=[]
for name,digest in expected.items():
 r=row(a/name);assert r['sha256']==digest,name;sources.append(r)
(b/'DEPENDENCIES.json').write_text(json.dumps({'created_utc':datetime.now(timezone.utc).isoformat(),'source_role':'Identity-matched previously reviewed unweighted cooler and independent evidence; no author adaptation source accessed.','sources':sources},indent=2)+'\n')
(b/'RUNTIME.json').write_text(json.dumps({'executable':sys.executable,'python':sys.version,'platform':platform.platform(),'numpy':numpy.__version__,'scipy':scipy.__version__,'sympy':sympy.__version__},indent=2)+'\n')
results=[]
for stem,script in [('FINITE_COOLER','finite_cooler_check.py'),('GAUSSIAN','gaussian_check.py'),('VARIATIONAL','variational_geometry_check.py')]:
 result=json.loads((b/(stem+'_RESULTS.json')).read_text());receipt=json.loads((b/(stem+'_RUN_RECEIPT.json')).read_text())
 assert receipt['returncode']==0
 assert receipt['script_sha256']==row(b/script)['sha256']==result['script_sha256']
 assert (b/(stem+'_RUN.log')).read_bytes()==(b/(stem+'_RESULTS.json')).read_bytes()
 assert not (b/(stem+'_RUN.stderr')).read_bytes()
 results.append({'stem':stem,'runner':row(b/script),'result':row(b/(stem+'_RESULTS.json')),'receipt':row(b/(stem+'_RUN_RECEIPT.json')),'full_output_read':True,'stdout_equals_result':True,'stderr_empty':True})
import numpy as np
with np.load(b/'VARIATIONAL_COMPONENT.npz',allow_pickle=False) as data:
 assert set(data.files)=={'states','degree','ground','variational','eigenvalues'}
 assert data['states'].shape==data['degree'].shape==data['ground'].shape==data['variational'].shape==(864,)
 assert abs(float(data['ground']@data['ground'])-1)<1e-12
 assert abs(float(data['variational']@data['variational'])-1)<1e-12
 assert ((data['ground']>0).all() and (data['variational']>0).all())
 assert ((data['states'][1:]-data['states'][:-1])>0).all()
 assert abs(float((data['ground']@data['variational'])**2)-0.9974398958364804)<1e-14
boundary={'created_utc':datetime.now(timezone.utc).isoformat(),'neutral_input':row(b/'SPECIFICATION.md'),'author_seal_name_known_only':'RK_COOLING_ADAPTATION_AUTHOR_SEAL.json','author_seal_sha256_known_only':'4b707760dab45089bda59645caadc1a3d7bdc6e9ee3cc730a3be5c48a29b3937','author_seal_or_new_author_contents_opened':False,'new_author_notes_runners_results_context_opened':False,'author_checkpoint_or_registry_opened':False,'previous_sources_reused_at_matched_identity':True,'old_unweighted_author_runner':'Hash inspected as already allowed prior source; not imported, executed, or used for the new numerical calculation.','new_external_literature_access':False,'primary_or_prior_files_modified':False,'delegation_or_git_or_audit_actions':False,'independent_methods':['finite nilpotent-jump stationarity criterion and quantitative trace-norm output bound','new weighted polynomial degree-lowering proof','exact noncommutative Weyl-polynomial dual-generator reconstruction','actual periodic link enumeration and rational variational root isolation','exact rational Collatz bounds from a numerical positive vector'],'execution_evidence':results,'failed_attempts':[],'limitations':['Finite-model attraction and rate bounds are not uniform in volume or theta.','Weighted parent Hamiltonian is H_theta, not an implicit replacement by H_delta.','Gaussian oscillator is stipulated, not a microscopic derivation.','The one finite variational fidelity and eigenvector residual are numerical.','No publication or formal audit status.']}
(b/'READ_BOUNDARY.json').write_text(json.dumps(boundary,indent=2)+'\n')
artifacts=[row(p) for p in sorted(b.iterdir()) if p.is_file() and p.name not in ['PRE_COMPARISON_SEAL.json','CHECKPOINT.md']]
seal={'created_utc':datetime.now(timezone.utc).isoformat(),'status':'Independent reconstruction complete before author adaptation access; finite conditional proofs, exact controls and one finite numerical variational calculation.','sources':sources,'artifacts':artifacts,'counts':{'sources':len(sources),'artifacts':len(artifacts)},'outcomes':{'detuned_criterion':'Uniform/pure stationary target iff delta=0 or flippability constant; otherwise positive long-time resolved output.','weighted_attraction':'Proved with independently reconstructed weighted polynomial degree lowering under stated finite physical hypotheses.','gaussian':'Exact covariance and distinct occupation/output formulas; retuning scope explicit.','variational_theta':0.06193838841673542,'variational_energy':-1.6341599084844516,'ground_energy':-1.6424425919679508,'fidelity_numeric':0.9974398958364804},'checks':{'all_three_runs_exit0_first_execution':True,'full_result_fields_read':True,'all_stdout_equal_results':True,'all_stderr_empty':True,'failed_attempts':[]},'read_boundary':{'author_contents_unopened':True,'details':row(b/'READ_BOUNDARY.json')},'limits':boundary['limitations']}
(b/'PRE_COMPARISON_SEAL.json').write_text(json.dumps(seal,indent=2)+'\n')
for r in seal['sources']+seal['artifacts']:assert row(Path(r['path']))==r
print(json.dumps({'report':row(b/'REPORT.md'),'pre_seal':row(b/'PRE_COMPARISON_SEAL.json'),'counts':seal['counts'],'runners':[{r['path']:r['sha256']} for r in artifacts if r['path'].endswith('.py')]},indent=2))
