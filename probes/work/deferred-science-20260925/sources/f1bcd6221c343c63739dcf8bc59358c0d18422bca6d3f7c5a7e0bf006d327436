"""One-time root correspondence and publication source freeze."""
from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json,re,subprocess,sys
E=Path(__file__).resolve().parent;R=E/'local-charge-observation-publication'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((E/'LOCAL_CHARGE_OBSERVATION_PUBLICATION_WORKING_SOURCES.json').read_text())
for p,h in m['source_files_sha256'].items():assert sha(R/p)==h
note=(R/m['note']).read_text()
for source,changes in zip(m['source_notes'],m['presentation_replacements']):
 s=Path(source).read_text()
 for row in changes:assert s.count(row['old'])==1;s=s.replace(row['old'],row['new'],1)
 s=re.sub(r'^(#{1,6}) ',lambda x:'#'*(len(x[1])+2)+' ',s,flags=re.M)
 assert note.count(s)==1
decl={x.targets[0].id:ast.literal_eval(x.value) for x in ast.parse((R/m['runner']).read_text()).body if isinstance(x,ast.Assign) and isinstance(x.targets[0],ast.Name) and x.targets[0].id in {'AUDIT_INPUT_PATHS','AUDIT_TIMEOUT_SEC','RUNTIMES','OUTPUT_DIRECTORY'}}
assert set(decl['AUDIT_INPUT_PATHS'])=={m['note'],*m['runtime'],*m['parent_paths']}
assert list(decl['RUNTIMES'])==m['runtime'] and decl['OUTPUT_DIRECTORY']==m['output_directory'] and decl['AUDIT_TIMEOUT_SEC']==120
def leaves(x):
 if isinstance(x,dict):return sum(leaves(v) for v in x.values())
 if isinstance(x,list):return sum(leaves(v) for v in x)
 return 1
comparisons=[]
for label,directory in [('current','native-charge-current-noise-personal'),('finite_time','native-charge-finite-time-personal')]:
 old=json.loads((E/directory/'attempt01/stdout.json').read_text());new=json.loads((R/m['output_directory']/(label+'.stdout.json')).read_text())
 ot=old.pop('elapsed_seconds');nt=new.pop('elapsed_seconds');assert old==new
 assert (R/m['output_directory']/(label+'.stderr.txt')).read_bytes()==b''
 comparisons.append(dict(label=label,all_non_timing_leaves_exact=leaves(new),old_elapsed_seconds=ot,new_elapsed_seconds=nt))
result=(R/m['result']).read_text();j=json.loads(result);assert j['source_sha256']==sha(R/m['runner']) and j['all_assertions_passed']
execution=json.loads((E/'LOCAL_CHARGE_OBSERVATION_PRIMARY_EXECUTION.json').read_text())['execution']
assert execution['exit_code']==0 and execution['stderr']=='' and execution['stdout']==result+'TOTAL_PASS: 1\n'
assert result+'TOTAL_PASS: 1\n' in (R/m['cache']).read_text()
for row in j['artifacts']:
 p=R/row['path'];assert sha(p)==row['sha256'] and p.stat().st_size==row['bytes'] and row['exit_code']==row['stderr_bytes']==0
manifest='docs/audit/data/citation_graph_manifest.json'
old=json.loads(subprocess.check_output(['git','show',m['base_revision']+':'+manifest],cwd=R));new=json.loads((R/manifest).read_text())
cid=Path(m['note']).stem.lower();assert set(new['nodes'])-set(old['nodes'])=={cid}
assert all(new['nodes'][k]==v for k,v in old['nodes'].items()) and new['edge_count']==old['edge_count']+3
sys.path.insert(0,str(R/'scripts'));import runner_cache
assert runner_cache.cache_status(m['runner'])=='fresh'
report=dict(at=datetime.now(timezone.utc).isoformat(),source_proofs_reused_at_verified_identity=True,
 complete_new_frontmatter_front_footer_wrapper_and_presentation_changes_read=True,
 exact_embedded_proofs_after_listed_qualifications=True,comparisons=comparisons,
 wrapper_runtime_artifact_execution_cache_identity_passed=True,cache_status='fresh',
 old_graph_nodes_unchanged=len(old['nodes']),added_nodes=1,added_edges=3,
 no_time_propagator_or_experimental_fit=True,
 limitations='Conditional preparation and matter-charge functions. Fixed-local-support error only; conservative model-time window. No measured identification, calibration, infinite-volume evolution, Fourier-volume remainder, or microscopic joint transfer.',
 PRE_additions_separately_attributed=True,
 failed_scientific_executions=[],failed_build_attempts=['Premature graph-manifest writer failed because graph build was still running; freeze verifier rejected unchanged base topology. No graph manifest or verification receipt was written by that attempt; exact prior verifier and failure record preserved.'])
with (E/'LOCAL_CHARGE_OBSERVATION_PRIMARY_ROOT_VERIFICATION.json').open('x') as f:json.dump(report,f,indent=2);f.write('\n')
paths={m['note'],m['runner'],*m['runtime'],*m['parent_paths'],m['cache'],manifest}
paths|={str(p.relative_to(R)) for p in (R/m['output_directory']).iterdir() if p.is_file()}
m['files_sha256']={p:sha(R/p) for p in sorted(paths)};m['frozen_utc']=datetime.now(timezone.utc).isoformat()
with (E/'LOCAL_CHARGE_OBSERVATION_FROZEN_SOURCES.json').open('x') as f:json.dump(m,f,indent=2);f.write('\n')
print(json.dumps(report,indent=2))
