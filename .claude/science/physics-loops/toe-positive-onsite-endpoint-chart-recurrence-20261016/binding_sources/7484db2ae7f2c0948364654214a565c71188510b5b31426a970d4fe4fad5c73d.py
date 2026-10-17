"""Record root's completed reflection adapter review and actual published base."""
from pathlib import Path
from datetime import datetime,timezone
import ast,gzip,hashlib,json,subprocess
N=Path(__file__).resolve().parents[1];W=N.parent/'correlation_worktree'
O=N/'endpoint_chart_recurrence_integration_proposal';S=N/'endpoint_chart_recurrence_qualified_publication_draft'
D=N/'publication_integration/endpoint_chart_recurrence';B=N/'publication_integration/reflection_preparation_runner_repair'
R=N/'root_endpoint_chart_recurrence_qualified_publication_review'
def rd(p):return json.loads(Path(p).read_text())
def pin(p):
 p=Path(p);b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def same(p,r):assert all(pin(p)[k]==r[k] for k in ('bytes','sha256')),str(p)
def wr(p,v):
 with Path(p).open('x') as f:f.write(json.dumps(v,indent=2)+'\n')
assert not D.exists()
assert pin(O/'FINAL_FREEZE.json')['sha256']=='e9d70efe7dde9f4174ad46c75d025da3c0ca32c0cff3f1752787a5d4d0d5e150'
f=rd(O/'FINAL_FREEZE.json');assert len(f['files'])==345
for r in f['files']:same(O/r['path'],r)
assert {str(p.relative_to(O)) for p in O.rglob('*') if p.is_file()}=={r['path'] for r in f['files']}|{'FINAL_FREEZE.json'}
assert pin(S/'FINAL_FREEZE.json')['sha256']=='996e7619f1bd198225d245a211d48420c8d6ef6ed0ffe10f21743966c59cc326'
for r in rd(S/'FINAL_FREEZE.json')['members']:same(S/r['path'],r)
# Reconstruct exact function reuse and complete source archive identities without executing any adapter.
B0=N/'reflection_preparation_runner_repair_proposal';helper='scripts/positive_onsite_endpoint_chart_recurrence_2026_10_16.py';pack='.claude/science/physics-loops/toe-positive-onsite-endpoint-chart-recurrence-20261016'
def functions(path):
 text=Path(path).read_text();return {n.name:''.join(text.splitlines(True)[n.lineno-1:n.end_lineno]) for n in ast.parse(text).body if isinstance(n,ast.FunctionDef)}
newprimary=functions(O/'proposed_primary_unbound.py')
components={'common':(functions(B0/'reflection_preparation_common.py'),functions(O/'endpoint_chart_recurrence_common.py')),'primary_extension':(functions(B0/'primary_extension.py'),functions(O/'primary_extension.py')),'source_validator':(functions(S/'proposal'/helper),newprimary)}
reuse=rd(O/'FUNCTION_REUSE_MAP.json')['functions'];assert len(reuse)==50
for row in reuse:
 a,b=components[row['component']];old=a.get(row['name']);new=b[row['name']]
 assert row['old_sha256']==(hashlib.sha256(old.encode()).hexdigest() if old is not None else None)
 assert row['new_sha256']==hashlib.sha256(new.encode()).hexdigest() and row['exact']==(old==new)
for name,src in functions(O/'primary_extension.py').items():assert newprimary[name]==src
capture=rd(O/'SOURCE_CAPTURE_MANIFEST.json')['records'];assert len(capture)==238
for row in capture:
 same(row['path'],row);assert gzip.decompress((O/row['recovery']).read_bytes())==Path(row['path']).read_bytes()
# Literal changes carry exact reviewed source values, not duplicated new claims.
def vals(p):
 d={}
 for n in ast.parse(Path(p).read_text()).body:
  if isinstance(n,ast.Assign) and len(n.targets)==1 and isinstance(n.targets[0],ast.Name):
   try:d[n.targets[0].id]=ast.literal_eval(n.value)
   except ValueError:pass
 return d
sourcevals=vals(S/'proposal'/helper);v=vals(O/'proposed_primary_unbound.py')
for key in ['EXPECTED_BODIES','EXPECTED_FREEZES','EXPECTED_ACCEPTANCES']:assert v[key]==sourcevals[key]
assert v['SOURCE_AUDIT_INPUT_PATHS']==sourcevals['AUDIT_INPUT_PATHS'] and v['SOURCE_MANIFEST_SHA256']==sourcevals['MANIFEST_SHA256']
assert v['EXPECTED_SOURCE_BODY_PINS']==rd(S/'proposal'/pack/'BODY_MAP.json')['bodies']
assert v['EXPECTED_REQUIRED_SOURCE_QUALIFICATIONS']==rd(R/'REVIEW.json')['required_canonical_replacements']
for key,p in [('EXPECTED_SOURCE_MAP_SHA',S/'proposal'/pack/'BODY_MAP.json'),('EXPECTED_SOURCE_MANIFEST_SHA',S/'proposal'/pack/'SOURCE_MANIFEST.json'),('EXPECTED_SOURCE_VALIDATOR_SHA',S/'proposal'/helper),('EXPECTED_CANONICAL_TRAILER_SHA',O/'CANONICAL_TRAILER.md'),('EXPECTED_CANONICAL_CERTIFICATE_SHA',O/'PROPOSED_CLAIM_STATUS_CERTIFICATE.md'),('EXPECTED_PUBLICATION_STATE_SHA',S/'proposal'/pack/'PUBLICATION_STATE.json')]:assert v[key]==pin(p)['sha256']
receipts=[]
for label in ('build','build_v2','validate','build_final','capture_review','validate_v2','seal'):
 p=O/'metadata_runs'/label/'EXECUTION.json';r=rd(p);assert r['exit_code']==0 and not r['timed_out']
 for k in ('source_at_launch','launcher_at_launch','stdout','stderr'):same(r[k]['path'],r[k])
 assert r['original_source']['sha256']==r['source_at_launch']['sha256']
 assert Path(r['stderr']['path']).read_bytes()==b''
 receipts.append(pin(p))
note=(O/'PROPOSED_NOTE.md').read_bytes();bodies=rd(O/'PROPOSED_BODY_MAP.json')['bodies'];assert len(bodies)==9
for r in bodies:same(N/r['source'],r);assert note[r['start_byte']:r['end_byte_exclusive']]==(N/r['source']).read_bytes()
parents=rd(O/'PARENT_BINDING.json')['direct_canonical_parents'];assert parents==[]
for r in parents:same(W/r['path'],r)
for r in rd(O/'EXECUTION_TOOL_PINS.json')['files']:same(W/r['path'],r)
assert pin(R/'REVIEW.json')['sha256']=='9e1c630af138b3c4e8a5846f6063ae2ff8f048b23b7d36bb6bb26499b2c3969c'
pub=rd(B/'PUBLICATION.json');assert pub['number']==9651 and pub['headRefOid']=='9d5cd6d2fe59cd95d226e97e3ae818112256c32f'
assert rd(B/'ATTACHMENT.json')['actual_result']['isError'] is False
obs={}
for role in ('head','tree','branch','status','parent_pr'):
 p=N/'runs'/('chart_base_'+role)/'EXECUTION.json';r=rd(p);assert r['cwd']==str(W) and r['exit_code']==0 and not r['timed_out']
 for k in ('stdout','stderr','recorder','recorder_capture'):same(r[k]['path'],r[k])
 assert Path(r['stderr']['path']).read_bytes()==b'';obs[role]=pin(p)
for role,key in [('head','headRefOid'),('tree','tree'),('branch','headRefName')]:assert (N/'runs'/('chart_base_'+role)/'stdout').read_text().strip()==pub[key]
assert (N/'runs/chart_base_status/stdout').read_bytes()==b''
live=rd(N/'runs/chart_base_parent_pr/stdout');assert live['state']=='OPEN' and not live['isDraft'] and live['headRefOid']==pub['headRefOid']
refs=(N/'runs/chart_base_refs/stdout').read_text().splitlines()
assert refs==[pub['headRefOid'],pub['tree'],'5b0e1cc44f422fb0138b02eb071d3d16b40dfbb2','56c5c0ab64f532c5784e895b2f9aa6894fa334e0']
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=W).decode().strip()==pub['headRefOid']
assert subprocess.check_output(['git','status','--porcelain','-z'],cwd=W)==b''
rr=[]
for label in ('source_fetch_2005','open_inventory_2005','chart_base_refs'):
 p=N/'runs'/label/'EXECUTION.json';r=rd(p);assert r['exit_code']==0
 for k in ('stdout','stderr'):same(r[k]['path'],r[k])
 rr.append(pin(p))
D.mkdir(parents=True)
refresh=dict(utc=datetime.now(timezone.utc).isoformat(),refs={'HEAD':refs[0],'origin/main':refs[2],'origin/ai/execution':refs[3]},active_tree=refs[1],inventory=pin(N/'runs/open_inventory_2005/stdout'),actual_receipts=rr,scope='Actual20:04 fetch/refs/inventory and clean regular OPEN9651 selected; main/authority unchanged. Git transport is not a premise.')
wr(D/'FRESH_REFRESH.json',refresh)
base=dict(status='bound_actual_root_published_base',base_head=pub['headRefOid'],base_tree=pub['tree'],base_branch=pub['headRefName'],base_pr=pub['number'],base_parent_branch=live['baseRefName'],publication=pin(B/'PUBLICATION.json'),attachment=pin(B/'ATTACHMENT.json'),refresh=pin(D/'FRESH_REFRESH.json'),expected_refs=refresh['refs'],observations=obs)
wr(D/'ACTUAL_BASE_BINDING_INPUT.json',base)
review=dict(kind='root_integration_source_review',utc=datetime.now(timezone.utc).isoformat(),root_read_complete_for_changed_implementation=True,retained_audit=False,proposal_freeze=pin(O/'FINAL_FREEZE.json'),common=pin(O/'endpoint_chart_recurrence_common.py'),primary_unbound=pin(O/'proposed_primary_unbound.py'),source_publication_review=pin(R/'REVIEW.json'),actual_base_binding=pin(D/'ACTUAL_BASE_BINDING_INPUT.json'),metadata_receipts=receipts,local_members=345,immutable_bodies=9,direct_mathematical_parents=parents,source_review_command=rd(N/'runs/endpoint_publication_source_review/EXECUTION.json')['argv'],scientific_executions=0,actual_canonical_acceptance=None,editable_prompt_files_changed=[],verified_reuse_functions=len(reuse),source_captures=len(capture),required_canonical_replacements=rd(R/'REVIEW.json')['required_canonical_replacements'],scope='Complete new adapter builder/validator/capture/recorder/seal, changed common/extension functions, primary source extension and all binding literals, generated note/wrapper/status/report/PR prose and seven metadata receipts/full streams read. Exact function reuse map verified against reviewed source; nine unchanged original scientific bodies retain qualified scope. All238 capture objects and345 frozen adapter members checked. New graph must add one root and zero edges with preservation;21 future provenance mutants,10 source synthetic graph controls. Sufficient-bound wording replacement required. Actual selected clean9651 with completed publication/attachment; source and integration reviews distinct, canonical/staged phases still pending. No ODE, scientific rerun, physical validation or retained claim.')
wr(D/'ROOT_INTEGRATION_REVIEW.json',review)
print(json.dumps(dict(review=pin(D/'ROOT_INTEGRATION_REVIEW.json'),actual_base=pin(D/'ACTUAL_BASE_BINDING_INPUT.json'),refresh=pin(D/'FRESH_REFRESH.json'),scientific_executions=0)))

