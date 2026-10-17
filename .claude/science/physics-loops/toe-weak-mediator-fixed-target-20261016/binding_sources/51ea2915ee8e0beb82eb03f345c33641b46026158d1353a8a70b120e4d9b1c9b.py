"""Proposed recorder for root's completed weak-mediator adapter review and actual published base."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,ast,gzip,hashlib,json,subprocess
N=Path(__file__).resolve().parents[1];W=N.parent/'correlation_worktree'
O=N/'weak_mediator_integration_proposal';S=N/'weak_mediator_qualified_publication_draft'
D=N/'publication_integration/weak_mediator'
R=N/'root_weak_mediator_qualified_publication_review'
def rd(p):return json.loads(Path(p).read_text())
def pin(p):
 p=Path(p);b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def same(p,r):assert all(pin(p)[k]==r[k] for k in ('bytes','sha256')),str(p)
def wr(p,v):
 with Path(p).open('x') as f:f.write(json.dumps(v,indent=2)+'\n')


parser=argparse.ArgumentParser(description='Source-only proposal: root must supply a pinned completed judgment.')
parser.add_argument('--root-reviewed',action='store_true',required=True)
parser.add_argument('--expectations',type=Path,required=True)
parser.add_argument('--expectations-sha',required=True)
args=parser.parse_args();assert args.root_reviewed
expect_raw=args.expectations.read_bytes();assert hashlib.sha256(expect_raw).hexdigest()==args.expectations_sha
expect=json.loads(expect_raw)
assert expect['kind']=='weak_mediator_integration_review_expectations' and expect['root_completed_actual_read'] is True
assert all(v is not None for v in expect.values()),'Null templates are not actual review inputs'
assert isinstance(expect['review_markdown'],str) and expect['review_markdown'].strip()
assert not D.exists()
assert pin(O/'FINAL_FREEZE.json')['sha256']==expect['adapter_freeze_sha256']
f=rd(O/'FINAL_FREEZE.json');assert len(f['files'])==expect['adapter_member_count']
for r in f['files']:same(O/r['path'],r)
assert {str(p.relative_to(O)) for p in O.rglob('*') if p.is_file()}=={r['path'] for r in f['files']}|{'FINAL_FREEZE.json'}
assert pin(S/'FINAL_FREEZE.json')['sha256']=='32b3edb257c7695c24242b6ef36680468e31e5d8ee6d1156936fb2b44128fa0f'
for r in rd(S/'FINAL_FREEZE.json')['members']:same(S/r['path'],r)
# Reconstruct exact function reuse and complete source archive identities without executing any adapter.
B0=N/'commuting_static_edge_integration_proposal';helper='scripts/weak_mediator_fixed_target_2026_10_16.py';pack='.claude/science/physics-loops/toe-weak-mediator-fixed-target-20261016'
def functions(path):
 text=Path(path).read_text();return {n.name:''.join(text.splitlines(True)[n.lineno-1:n.end_lineno]) for n in ast.parse(text).body if isinstance(n,ast.FunctionDef)}
newprimary=functions(O/'proposed_primary_unbound.py')
components={'common':(functions(B0/'commuting_static_edge_common.py'),functions(O/'weak_mediator_common.py')),'primary_extension':(functions(B0/'primary_extension.py'),functions(O/'primary_extension.py')),'source_validator':(functions(S/'proposal'/helper),newprimary)}
reuse=rd(O/'FUNCTION_REUSE_MAP.json')['functions'];assert len(reuse)==expect['function_reuse_entry_count']
for row in reuse:
 a,b=components[row['component']];old=a.get(row['name']);new=b[row['name']]
 assert row['old_sha256']==(hashlib.sha256(old.encode()).hexdigest() if old is not None else None)
 assert row['new_sha256']==hashlib.sha256(new.encode()).hexdigest() and row['exact']==(old==new)
for name,src in functions(O/'primary_extension.py').items():assert newprimary[name]==src
capture=rd(O/'SOURCE_CAPTURE_MANIFEST.json')['records'];assert len(capture)==expect['source_capture_count']
extra_capture=rd(O/'IMPLEMENTATION_EXECUTION_EVIDENCE.json')['records']+rd(O/'SUPPLEMENTAL_REFRESH.json')['records'];assert len(extra_capture)==expect['supplemental_capture_count']
for row in capture+extra_capture:
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
metadata_specs=expect['metadata_runs'];assert isinstance(metadata_specs,list) and metadata_specs
labels=[x['label'] for x in metadata_specs]
assert len(labels)==len(set(labels)) and all(isinstance(x,str) and x.replace('_','').isalnum() for x in labels)
assert set(labels)=={p.parent.name for p in (O/'metadata_runs').glob('*/EXECUTION.json')}
assert not {p.name for p in (O/'metadata_runs').iterdir() if p.is_dir()}-set(labels), 'Unrecorded metadata directory'
for spec in metadata_specs:
 label=spec['label'];p=O/'metadata_runs'/label/'EXECUTION.json';same(p,spec['receipt']);r=rd(p)
 assert type(spec['expected_exit_code']) is int and type(spec['expected_timed_out']) is bool
 assert r['exit_code']==spec['expected_exit_code'] and r['timed_out']==spec['expected_timed_out']
 for k in ('source_at_launch','launcher_at_launch','stdout','stderr'):same(r[k]['path'],r[k])
 assert r['original_source']['sha256']==r['source_at_launch']['sha256']
 if r['exit_code']==0:assert not r['timed_out'] and Path(r['stderr']['path']).read_bytes()==b''
 # A historical failed capture and its old source remain evidence, not a new success.
 receipts.append(pin(p))
note=(O/'PROPOSED_NOTE.md').read_bytes();bodies=rd(O/'PROPOSED_BODY_MAP.json')['bodies'];assert len(bodies)==12
for r in bodies:same(N/r['source'],r);assert note[r['start_byte']:r['end_byte_exclusive']]==(N/r['source']).read_bytes()
parents=rd(O/'PARENT_BINDING.json')['direct_canonical_parents'];assert parents==[]
assert rd(R/'REVIEW.json')['proposed_graph_disposition']=='one_new_root_zero_direct_parent_edges'
for r in parents:same(W/r['path'],r)
for r in rd(O/'EXECUTION_TOOL_PINS.json')['files']:same(W/r['path'],r)
assert pin(R/'REVIEW.json')['sha256']==expect['source_review_sha256']
context=rd(O/'BASE_CONTEXT.json');selection=context['selected_base'];refs=context['expected_refs']
assert isinstance(selection,dict) and selection and isinstance(refs,dict)
for field in ['publication','attachment','source_review_execution','inventory']:
 same(expect[field]['path'],expect[field])
pub=rd(expect['publication']['path']);live_values={};obs=expect['observations']
assert set(obs)=={'head','tree','branch','status','parent_pr'}
assert pub['state']=='OPEN' and pub['isDraft'] is False
attachment=rd(expect['attachment']['path'])
assert attachment['tool']=='mcp__codex_app__attach_artifact' and attachment['arguments']=={'artifact_type':'pull_request','url':pub['url']}
assert attachment['actual_result']['isError'] is False
assert any(json.loads(x['text'])==attachment['arguments'] for x in attachment['actual_result']['content'] if x['type']=='text')
commands={'head':['git','rev-parse','HEAD'],'tree':['git','rev-parse','HEAD^{tree}'],'branch':['git','branch','--show-current'],'status':['git','status','--porcelain','-z'],
 'parent_pr':['gh','pr','view',str(pub['number']),'--repo',expect['repository'],'--json','number,url,state,isDraft,headRefName,headRefOid,baseRefName']}
for role,row in obs.items():
 same(row['path'],row);r=rd(row['path'])
 assert r['argv']==commands[role] and r['cwd']==str(W) and r['exit_code']==0 and not r.get('timed_out',r.get('timeout',False))
 assert r['start_utc']<=r.get('end_utc',r.get('finished_utc'))
 for key in ['stdout','stderr','recorder','recorder_capture']:
  if r.get(key) is not None:same(r[key]['path'],r[key])
 assert Path(r['stderr']['path']).read_bytes()==b'';live_values[role]=Path(r['stdout']['path']).read_bytes()
assert live_values['head'].decode().strip()==pub['headRefOid'] and live_values['tree'].decode().strip()==pub['tree']
assert live_values['branch'].decode().strip()==pub['headRefName'] and live_values['status']==b''
live=json.loads(live_values['parent_pr']);assert live['state']=='OPEN' and not live['isDraft'] and live['number']==pub['number']
assert live['headRefOid']==pub['headRefOid'] and live['headRefName']==pub['headRefName'] and live['url']==pub['url']
base_values=dict(base_head=pub['headRefOid'],base_tree=pub['tree'],base_branch=pub['headRefName'],base_pr=pub['number'],base_parent_branch=live['baseRefName'])
assert {k:base_values[k] for k in selection}==selection
assert refs['HEAD']==pub['headRefOid'] and refs['origin/ai/execution']=='56c5c0ab64f532c5784e895b2f9aa6894fa334e0'
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=W).decode().strip()==pub['headRefOid']
assert subprocess.check_output(['git','status','--porcelain','-z'],cwd=W)==b''
assert subprocess.check_output(['git','rev-parse','origin/main'],cwd=W).decode().strip()==refs['origin/main']
assert subprocess.check_output(['git','rev-parse','origin/ai/execution'],cwd=W).decode().strip()==refs['origin/ai/execution']
rr=expect['refresh_receipts'];assert isinstance(rr,list) and rr
for row in rr:
 same(row['path'],row);r=rd(row['path']);assert r['exit_code']==0
 for key in ['stdout','stderr','recorder','recorder_capture','child_source_at_launch','source_capture']:
  if r.get(key) is not None:same(r[key]['path'],r[key])
D.mkdir(parents=True)
refresh=dict(utc=datetime.now(timezone.utc).isoformat(),refs=refs,active_tree=pub['tree'],inventory=expect['inventory'],actual_receipts=rr,scope=expect['review_markdown'])
wr(D/'FRESH_REFRESH.json',refresh)
base=dict(status='bound_actual_root_published_base',base_head=pub['headRefOid'],base_tree=pub['tree'],base_branch=pub['headRefName'],base_pr=pub['number'],base_parent_branch=live['baseRefName'],publication=expect['publication'],attachment=expect['attachment'],refresh=pin(D/'FRESH_REFRESH.json'),expected_refs=refresh['refs'],observations=obs)
wr(D/'ACTUAL_BASE_BINDING_INPUT.json',base)
review=dict(kind='root_integration_source_review',utc=datetime.now(timezone.utc).isoformat(),root_read_complete_for_changed_implementation=True,retained_audit=False,proposal_freeze=pin(O/'FINAL_FREEZE.json'),common=pin(O/'weak_mediator_common.py'),primary_unbound=pin(O/'proposed_primary_unbound.py'),source_publication_review=pin(R/'REVIEW.json'),actual_base_binding=pin(D/'ACTUAL_BASE_BINDING_INPUT.json'),metadata_receipts=receipts,local_members=len(f['files']),immutable_bodies=12,direct_mathematical_parents=parents,source_review_command=rd(expect['source_review_execution']['path'])['argv'],scientific_executions=0,actual_canonical_acceptance=None,editable_prompt_files_changed=[],verified_reuse_functions=len(reuse),source_captures=len(capture),required_canonical_replacements=rd(R/'REVIEW.json')['required_canonical_replacements'],scope=expect['review_markdown'],review_expectations=expect,review_expectation_source=pin(args.expectations),review_expectations_original_utf8=expect_raw.decode('utf-8'))
wr(D/'ROOT_INTEGRATION_REVIEW.json',review)
print(json.dumps(dict(review=pin(D/'ROOT_INTEGRATION_REVIEW.json'),actual_base=pin(D/'ACTUAL_BASE_BINDING_INPUT.json'),refresh=pin(D/'FRESH_REFRESH.json'),scientific_executions=0)))

