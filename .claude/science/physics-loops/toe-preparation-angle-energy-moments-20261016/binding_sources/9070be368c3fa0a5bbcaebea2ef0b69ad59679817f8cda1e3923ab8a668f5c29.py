"""Record the root's completed adapter review and real selected-base evidence."""
from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json,subprocess
N=Path(__file__).resolve().parents[1];W=N.parent/'correlation_worktree'
O=N/'preparation_angle_moment_runner_repair_proposal';S=N/'preparation_angle_moment_qualified_publication_draft'
D=N/'publication_integration/preparation_angle_moment_runner_repair';B=N/'publication_integration/interacting_control'
R=N/'root_preparation_angle_moment_qualified_publication_review'
def rd(p):return json.loads(Path(p).read_text())
def pin(p):
 p=Path(p);b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def same(p,r):assert all(pin(p)[k]==r[k] for k in ('bytes','sha256')),str(p)
def wr(p,v):
 with Path(p).open('x') as f:f.write(json.dumps(v,indent=2)+'\n')
def functions(p):
 s=Path(p).read_text();out={}
 def walk(nodes,prefix=''):
  for n in nodes:
   if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)):
    key=prefix+n.name;out[key]=ast.get_source_segment(s,n);walk(n.body,key+'.')
   elif isinstance(n,(ast.For,ast.While,ast.If,ast.With,ast.Try)):walk(n.body,prefix)
 walk(ast.parse(s).body);return out
assert pin(O/'FINAL_FREEZE.json')['sha256']=='735041bb46ddf510b3971985485951d70891c924218cbca5cd6477c7ab8e6218'
f=rd(O/'FINAL_FREEZE.json');assert len(f['files'])==429
for r in f['files']:same(O/r['path'],r)
assert {str(p.relative_to(O)) for p in O.rglob('*') if p.is_file()}=={r['path'] for r in f['files']}|{'FINAL_FREEZE.json'}
for r in rd(S/'FINAL_FREEZE.json')['members']:same(S/r['path'],r)
recovery=rd(D/'recovery/RECOVERY_RESULT.json');assert recovery['owned_files_removed']==152 and recovery['scientific_executions']==0
same(recovery['review']['path'],recovery['review']);same(recovery['preservation']['path'],recovery['preservation']);same(W/'docs/audit/data/citation_graph.json',recovery['graph_restored_exactly']);same(W/'docs/audit/data/citation_graph_manifest.json',recovery['manifest_unchanged'])
for label,expected in [('angle_runner_recovery',1),('angle_runner_recovery_v2',0)]:
 r=rd(N/'runs'/label/'EXECUTION.json');assert r['exit_code']==expected
 for k in ('source_capture','stdout','stderr','recorder'):same(r[k]['path'],r[k])
 same(r['source_capture']['path'],r['child_source_at_launch'])
receipts=[]
for label in ('build','validate'):
 p=O/'metadata_runs'/label/'EXECUTION.json';r=rd(p);assert r['exit_code']==0 and not r['timed_out']
 for k in ('original_source','source_at_launch','launcher_at_launch','stdout','stderr'):same(r[k]['path'],r[k])
 receipts.append(pin(p))
note=(O/'PROPOSED_NOTE.md').read_bytes();bodies=rd(O/'PROPOSED_BODY_MAP.json')['bodies'];assert len(bodies)==3
for r in bodies:same(N/r['source'],r);assert note[r['start_byte']:r['end_byte_exclusive']]==(N/r['source']).read_bytes()
parents=rd(O/'PARENT_BINDING.json')['direct_canonical_parents'];assert len(parents)==1 and parents[0]['sha256']=='6db93809f12315668f720006c6a443301ad682381ce5629c173b1ff1c6d66a7f'
for r in parents:same(W/r['path'],r)
for r in rd(O/'EXECUTION_TOOL_PINS.json')['files']:same(W/r['path'],r)
assert pin(R/'REVIEW.json')['sha256']=='c5b71bbf62eeffeb26d4a0ba0c51690eac3e5d4600b78897675daa7d4846eb90'
observed={'actual_argv':rd(N/'runs/angle_moment_source_publication_review/EXECUTION.json')['argv']}
pub=rd(B/'PUBLICATION.json');assert pub['number']==9649 and pub['headRefOid']=='ff46be4883eb97457adc4d4c17af08ddbb05f20c' and pub['tree']=='ca0b288f84bc004590fba03e913817912b2826b5'
assert rd(B/'ATTACHMENT.json')['actual_result']['isError'] is False
obs={}
for role in ('head','tree','branch','status','parent_pr'):
 p=N/'runs'/('angle_repair_base_'+role)/'EXECUTION.json';r=rd(p);assert r['cwd']==str(W) and r['exit_code']==0 and not r['timed_out']
 for k in ('stdout','stderr','recorder','recorder_capture'):same(r[k]['path'],r[k])
 assert Path(r['stderr']['path']).read_bytes()==b'';obs[role]=pin(p)
assert (N/'runs/angle_repair_base_head/stdout').read_text().strip()==pub['headRefOid']
assert (N/'runs/angle_repair_base_tree/stdout').read_text().strip()==pub['tree']
assert (N/'runs/angle_repair_base_branch/stdout').read_text().strip()==pub['headRefName']
assert (N/'runs/angle_repair_base_status/stdout').read_bytes()==b''
live=rd(N/'runs/angle_repair_base_parent_pr/stdout');assert live['state']=='OPEN' and not live['isDraft'] and live['headRefOid']==pub['headRefOid']
refs=(N/'runs/angle_repair_base_refs/stdout').read_text().splitlines()
assert refs==[pub['headRefOid'],pub['tree'],'5b0e1cc44f422fb0138b02eb071d3d16b40dfbb2','56c5c0ab64f532c5784e895b2f9aa6894fa334e0']
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=W).decode().strip()==pub['headRefOid']
assert subprocess.check_output(['git','status','--porcelain','-z'],cwd=W)==b''
rr=[]
for label in ('source_fetch_1929','open_inventory_1929','angle_repair_base_refs'):
 p=N/'runs'/label/'EXECUTION.json';r=rd(p);assert r['exit_code']==0
 for k in ('stdout','stderr'):same(r[k]['path'],r[k])
 rr.append(pin(p))
D.mkdir(parents=True,exist_ok=True)
refresh=dict(utc=datetime.now(timezone.utc).isoformat(),refs={'HEAD':refs[0],'origin/main':refs[2],'origin/ai/execution':refs[3]},active_tree=refs[1],inventory=pin(N/'runs/open_inventory_1929/stdout'),actual_receipts=rr,scope='Actual19:29 fetch, refs and inventory; main/authority unchanged, selected regular PR9649. New unrelated remote campaign branch is not adopted.')
wr(D/'FRESH_REFRESH.json',refresh)
base=dict(status='bound_actual_root_published_base',base_head=pub['headRefOid'],base_tree=pub['tree'],base_branch=pub['headRefName'],base_pr=pub['number'],base_parent_branch=live['baseRefName'],publication=pin(B/'PUBLICATION.json'),attachment=pin(B/'ATTACHMENT.json'),refresh=pin(D/'FRESH_REFRESH.json'),expected_refs=refresh['refs'],observations=obs)
wr(D/'ACTUAL_BASE_BINDING_INPUT.json',base)
review=dict(kind='root_integration_source_review',utc=datetime.now(timezone.utc).isoformat(),root_read_complete_for_changed_implementation=True,retained_audit=False,proposal_freeze=pin(O/'FINAL_FREEZE.json'),common=pin(O/'preparation_angle_moment_common.py'),primary_unbound=pin(O/'proposed_primary_unbound.py'),source_publication_review=pin(R/'REVIEW.json'),actual_base_binding=pin(D/'ACTUAL_BASE_BINDING_INPUT.json'),metadata_receipts=receipts,local_members=429,immutable_bodies=3,direct_mathematical_parents=parents,source_review_command=observed['actual_argv'],scientific_executions=0,actual_canonical_acceptance=None,editable_prompt_files_changed=[],recovery_result=pin(D/'recovery/RECOVERY_RESULT.json'),recovery_review=pin(D/'recovery/ROOT_RECOVERY_REVIEW.json'),recovery_actual_receipts=[pin(N/'runs'/q/'EXECUTION.json') for q in ['angle_runner_recovery','angle_runner_recovery_v2']],scope='Complete changed common/guards/parser and build/validate/record/seal code, narrow note/interval/recovery/PR prose and both actual metadata streams reviewed. Original primary, three mathematical bodies and sole preparation parent unchanged. Old graph action failed despite graph builder exit0, all old evidence preserved. Exact152 owned files backed up and removed, baseline graph restored by byte identity, failed branch retained. First root recovery record stopped before mutations on an overly broad unchanged-PR assertion; distinct v2 included the fully read failure-disclosure paragraph and completed recovery. Fresh regular OPEN9649 base and source/authority refs observed. No scientific replay, new proof acceptance, future canonical success or retained status asserted.')
wr(D/'ROOT_INTEGRATION_REVIEW.json',review)
print(json.dumps(dict(review=pin(D/'ROOT_INTEGRATION_REVIEW.json'),actual_base=pin(D/'ACTUAL_BASE_BINDING_INPUT.json'),refresh=pin(D/'FRESH_REFRESH.json'),scientific_executions=0)))
