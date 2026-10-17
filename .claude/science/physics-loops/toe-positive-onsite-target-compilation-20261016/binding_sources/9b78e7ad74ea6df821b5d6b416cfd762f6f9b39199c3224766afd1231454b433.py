"""Record root's completed target-compilation adapter review and actual published base."""
from pathlib import Path
from datetime import datetime,timezone
import ast,gzip,hashlib,json,subprocess
N=Path(__file__).resolve().parents[1];W=N.parent/'correlation_worktree'
O=N/'endpoint_target_compilation_integration_proposal';S=N/'endpoint_target_compilation_qualified_publication_draft'
D=N/'publication_integration/endpoint_target_compilation';B=N/'publication_integration/endpoint_chart_recurrence'
R=N/'root_endpoint_target_compilation_qualified_publication_review'
def rd(p):return json.loads(Path(p).read_text())
def pin(p):
 p=Path(p);b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def same(p,r):assert all(pin(p)[k]==r[k] for k in ('bytes','sha256')),str(p)
def wr(p,v):
 with Path(p).open('x') as f:f.write(json.dumps(v,indent=2)+'\n')
assert not D.exists()
assert pin(O/'FINAL_FREEZE.json')['sha256']=='739861728d983b8ab1942e59af87f349e9332df346648710b171308a4a30810f'
f=rd(O/'FINAL_FREEZE.json');assert len(f['files'])==457
for r in f['files']:same(O/r['path'],r)
assert {str(p.relative_to(O)) for p in O.rglob('*') if p.is_file()}=={r['path'] for r in f['files']}|{'FINAL_FREEZE.json'}
assert pin(S/'FINAL_FREEZE.json')['sha256']=='d8d497c515fa8f1eebf4f336a55435557cc3c8b60384f4a17a5ce2d40a8c37d7'
for r in rd(S/'FINAL_FREEZE.json')['members']:same(S/r['path'],r)
# Reconstruct exact function reuse and complete source archive identities without executing any adapter.
B0=N/'endpoint_chart_recurrence_integration_proposal';helper='scripts/positive_onsite_target_compilation_2026_10_16.py';pack='.claude/science/physics-loops/toe-positive-onsite-target-compilation-20261016'
def functions(path):
 text=Path(path).read_text();return {n.name:''.join(text.splitlines(True)[n.lineno-1:n.end_lineno]) for n in ast.parse(text).body if isinstance(n,ast.FunctionDef)}
newprimary=functions(O/'proposed_primary_unbound.py')
components={'common':(functions(B0/'endpoint_chart_recurrence_common.py'),functions(O/'endpoint_target_compilation_common.py')),'primary_extension':(functions(B0/'primary_extension.py'),functions(O/'primary_extension.py')),'source_validator':(functions(S/'proposal'/helper),newprimary)}
reuse=rd(O/'FUNCTION_REUSE_MAP.json')['functions'];assert len(reuse)==50
for row in reuse:
 a,b=components[row['component']];old=a.get(row['name']);new=b[row['name']]
 assert row['old_sha256']==(hashlib.sha256(old.encode()).hexdigest() if old is not None else None)
 assert row['new_sha256']==hashlib.sha256(new.encode()).hexdigest() and row['exact']==(old==new)
for name,src in functions(O/'primary_extension.py').items():assert newprimary[name]==src
capture=rd(O/'SOURCE_CAPTURE_MANIFEST.json')['records'];assert len(capture)==340
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
for label in ('build','capture_review','build_v2','validate','seal'):
 p=O/'metadata_runs'/label/'EXECUTION.json';r=rd(p);assert r['exit_code']==0 and not r['timed_out']
 for k in ('source_at_launch','launcher_at_launch','stdout','stderr'):same(r[k]['path'],r[k])
 assert r['original_source']['sha256']==r['source_at_launch']['sha256']
 assert Path(r['stderr']['path']).read_bytes()==b''
 receipts.append(pin(p))
note=(O/'PROPOSED_NOTE.md').read_bytes();bodies=rd(O/'PROPOSED_BODY_MAP.json')['bodies'];assert len(bodies)==6
for r in bodies:same(N/r['source'],r);assert note[r['start_byte']:r['end_byte_exclusive']]==(N/r['source']).read_bytes()
parents=rd(O/'PARENT_BINDING.json')['direct_canonical_parents'];assert len(parents)==1 and parents[0]['sha256']=='ab8fd20fb48aae14c9ae22df2b38de97755d717131195d0d4ad25f7236d475a8'
for r in parents:same(W/r['path'],r)
for r in rd(O/'EXECUTION_TOOL_PINS.json')['files']:same(W/r['path'],r)
assert pin(R/'REVIEW.json')['sha256']=='899f433630e38ebfc90eeb3577777dab6db294cd5e2a1836cafb28e1b90a1f07'
pub=rd(B/'PUBLICATION.json');assert pub['number']==9652 and pub['headRefOid']=='4864625c13b2f0cf44eb19ae3114a8cabafc238c'
assert rd(B/'ATTACHMENT.json')['actual_result']['isError'] is False
obs={}
for role in ('head','tree','branch','status','parent_pr'):
 p=N/'runs'/('target_base_'+role)/'EXECUTION.json';r=rd(p);assert r['cwd']==str(W) and r['exit_code']==0 and not r['timed_out']
 for k in ('stdout','stderr','recorder','recorder_capture'):same(r[k]['path'],r[k])
 assert Path(r['stderr']['path']).read_bytes()==b'';obs[role]=pin(p)
for role,key in [('head','headRefOid'),('tree','tree'),('branch','headRefName')]:assert (N/'runs'/('target_base_'+role)/'stdout').read_text().strip()==pub[key]
assert (N/'runs/target_base_status/stdout').read_bytes()==b''
live=rd(N/'runs/target_base_parent_pr/stdout');assert live['state']=='OPEN' and not live['isDraft'] and live['headRefOid']==pub['headRefOid']
refs=(N/'runs/target_base_refs/stdout').read_text().splitlines()
assert refs==[pub['headRefOid'],pub['tree'],'5b0e1cc44f422fb0138b02eb071d3d16b40dfbb2','56c5c0ab64f532c5784e895b2f9aa6894fa334e0']
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=W).decode().strip()==pub['headRefOid']
assert subprocess.check_output(['git','status','--porcelain','-z'],cwd=W)==b''
rr=[]
for label in ('source_fetch_2030','open_inventory_2025','target_base_refs'):
 p=N/'runs'/label/'EXECUTION.json';r=rd(p);assert r['exit_code']==0
 for k in ('stdout','stderr'):same(r[k]['path'],r[k])
 rr.append(pin(p))
D.mkdir(parents=True)
refresh=dict(utc=datetime.now(timezone.utc).isoformat(),refs={'HEAD':refs[0],'origin/main':refs[2],'origin/ai/execution':refs[3]},active_tree=refs[1],inventory=pin(N/'runs/open_inventory_2025/stdout'),actual_receipts=rr,scope='Actual20:25 fetch/refs and20:23 inventory; clean regular OPEN9652 selected; main/authority unchanged. Git transport is not a premise.')
wr(D/'FRESH_REFRESH.json',refresh)
base=dict(status='bound_actual_root_published_base',base_head=pub['headRefOid'],base_tree=pub['tree'],base_branch=pub['headRefName'],base_pr=pub['number'],base_parent_branch=live['baseRefName'],publication=pin(B/'PUBLICATION.json'),attachment=pin(B/'ATTACHMENT.json'),refresh=pin(D/'FRESH_REFRESH.json'),expected_refs=refresh['refs'],observations=obs)
wr(D/'ACTUAL_BASE_BINDING_INPUT.json',base)
review=dict(kind='root_integration_source_review',utc=datetime.now(timezone.utc).isoformat(),root_read_complete_for_changed_implementation=True,retained_audit=False,proposal_freeze=pin(O/'FINAL_FREEZE.json'),common=pin(O/'endpoint_target_compilation_common.py'),primary_unbound=pin(O/'proposed_primary_unbound.py'),source_publication_review=pin(R/'REVIEW.json'),actual_base_binding=pin(D/'ACTUAL_BASE_BINDING_INPUT.json'),metadata_receipts=receipts,local_members=457,immutable_bodies=6,direct_mathematical_parents=parents,source_review_command=rd(N/'runs/target_publication_source_review/EXECUTION.json')['argv'],scientific_executions=0,actual_canonical_acceptance=None,editable_prompt_files_changed=[],verified_reuse_functions=len(reuse),source_captures=len(capture),required_canonical_replacements=rd(R/'REVIEW.json')['required_canonical_replacements'],scope='Complete new adapter builder/validator/capture/recorder/seal, changed common/extension functions and binding constants, note/status/report/PR prose reviewed; exact unchanged function reuse mechanically checked. Five actual metadata receipts and full streams checked. Six original scientific bodies remain unchanged and qualified. All340 capture objects and457 frozen adapter members checked. One existing chart/recurrence parent edge and zero new roots required;22 future canonical mutants;12 graph and7 receipt-predicate metadata corruptions. No substantive source wording replacement required. Exact selected clean9652 with completed publication and actual attachment; current main and authority unchanged at actual20:25 refresh. Source/integration review distinct; canonical/staged phases pending. No ODE, science rerun, native physical validation or retained-audit claim.')
wr(D/'ROOT_INTEGRATION_REVIEW.json',review)
print(json.dumps(dict(review=pin(D/'ROOT_INTEGRATION_REVIEW.json'),actual_base=pin(D/'ACTUAL_BASE_BINDING_INPUT.json'),refresh=pin(D/'FRESH_REFRESH.json'),scientific_executions=0)))

