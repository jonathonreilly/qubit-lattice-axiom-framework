"""Proposed recorder for root's completed static-edge adapter review and actual published base."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,ast,gzip,hashlib,json,subprocess
N=Path(__file__).resolve().parents[1];W=N.parent/'correlation_worktree'
O=N/'commuting_static_edge_integration_proposal';S=N/'commuting_static_edge_qualified_publication_draft'
D=N/'publication_integration/commuting_static_edge';B=N/'publication_integration/endpoint_target_compilation'
R=N/'root_commuting_static_edge_qualified_publication_review'
def rd(p):return json.loads(Path(p).read_text())
def pin(p):
 p=Path(p);b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def same(p,r):assert all(pin(p)[k]==r[k] for k in ('bytes','sha256')),str(p)
def wr(p,v):
 with Path(p).open('x') as f:f.write(json.dumps(v,indent=2)+'\n')

parser=argparse.ArgumentParser(description='Unexecuted root recorder proposal; only root may record a completed actual review.')
parser.add_argument('--root-reviewed',action='store_true',required=True)
args=parser.parse_args();assert args.root_reviewed
assert not D.exists()
assert pin(O/'FINAL_FREEZE.json')['sha256']=='23bc904d202993554d09795b0783968b6f494768b9091bff1321a754ee1527a6'
f=rd(O/'FINAL_FREEZE.json');assert len(f['files'])==391
for r in f['files']:same(O/r['path'],r)
assert {str(p.relative_to(O)) for p in O.rglob('*') if p.is_file()}=={r['path'] for r in f['files']}|{'FINAL_FREEZE.json'}
assert pin(S/'FINAL_FREEZE.json')['sha256']=='c0f7a24933d585f168b2e724911ef0707126a596daa7495c8db582c4e172fe40'
for r in rd(S/'FINAL_FREEZE.json')['members']:same(S/r['path'],r)
# Reconstruct exact function reuse and complete source archive identities without executing any adapter.
B0=N/'endpoint_target_compilation_integration_proposal';helper='scripts/commuting_static_edge_fixed_target_2026_10_16.py';pack='.claude/science/physics-loops/toe-commuting-static-edge-fixed-target-20261016'
def functions(path):
 text=Path(path).read_text();return {n.name:''.join(text.splitlines(True)[n.lineno-1:n.end_lineno]) for n in ast.parse(text).body if isinstance(n,ast.FunctionDef)}
newprimary=functions(O/'proposed_primary_unbound.py')
components={'common':(functions(B0/'endpoint_target_compilation_common.py'),functions(O/'commuting_static_edge_common.py')),'primary_extension':(functions(B0/'primary_extension.py'),functions(O/'primary_extension.py')),'source_validator':(functions(S/'proposal'/helper),newprimary)}
reuse=rd(O/'FUNCTION_REUSE_MAP.json')['functions'];assert len(reuse)==50
for row in reuse:
 a,b=components[row['component']];old=a.get(row['name']);new=b[row['name']]
 assert row['old_sha256']==(hashlib.sha256(old.encode()).hexdigest() if old is not None else None)
 assert row['new_sha256']==hashlib.sha256(new.encode()).hexdigest() and row['exact']==(old==new)
for name,src in functions(O/'primary_extension.py').items():assert newprimary[name]==src
capture=rd(O/'SOURCE_CAPTURE_MANIFEST.json')['records'];assert len(capture)==249
extra_capture=rd(O/'IMPLEMENTATION_EXECUTION_EVIDENCE.json')['records']+rd(O/'SUPPLEMENTAL_REFRESH.json')['records'];assert len(extra_capture)==57
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
for label in ('build','capture_review','validate','seal'):
 p=O/'metadata_runs'/label/'EXECUTION.json';r=rd(p);assert r['exit_code']==0 and not r['timed_out']
 for k in ('source_at_launch','launcher_at_launch','stdout','stderr'):same(r[k]['path'],r[k])
 assert r['original_source']['sha256']==r['source_at_launch']['sha256']
 assert Path(r['stderr']['path']).read_bytes()==b''
 receipts.append(pin(p))
note=(O/'PROPOSED_NOTE.md').read_bytes();bodies=rd(O/'PROPOSED_BODY_MAP.json')['bodies'];assert len(bodies)==5
for r in bodies:same(N/r['source'],r);assert note[r['start_byte']:r['end_byte_exclusive']]==(N/r['source']).read_bytes()
parents=rd(O/'PARENT_BINDING.json')['direct_canonical_parents'];assert parents==[]
assert rd(R/'REVIEW.json')['proposed_graph_disposition']=='one_new_root_zero_direct_parent_edges'
for name in ['NO_GO_DISCIPLINE_CHECKLIST.md','APPROACH_REGISTRY.md','NO_GO_LEDGER.md','NO_GO_STATUS.json']:
 assert (O/'payload'/pack/name).read_bytes()==(S/'proposal'/pack/name).read_bytes()
for r in parents:same(W/r['path'],r)
for r in rd(O/'EXECUTION_TOOL_PINS.json')['files']:same(W/r['path'],r)
assert pin(R/'REVIEW.json')['sha256']=='8c734556a0ffab117468cbcc993cb95f61ad32bb0b1f123c4ea549fffa182d3b'
pub=rd(B/'PUBLICATION.json');assert pub['number']==9653 and pub['headRefOid']=='8b7b8b4768e2831b273bada5bcebf2b4175583f4'
assert rd(B/'ATTACHMENT.json')['actual_result']['isError'] is False
obs={}
for role in ('head','tree','branch','status','parent_pr'):
 p=N/'runs'/('static_base_'+role)/'EXECUTION.json';r=rd(p);assert r['cwd']==str(W) and r['exit_code']==0 and not r['timed_out']
 for k in ('stdout','stderr','recorder','recorder_capture'):same(r[k]['path'],r[k])
 assert Path(r['stderr']['path']).read_bytes()==b'';obs[role]=pin(p)
for role,key in [('head','headRefOid'),('tree','tree'),('branch','headRefName')]:assert (N/'runs'/('static_base_'+role)/'stdout').read_text().strip()==pub[key]
assert (N/'runs/static_base_status/stdout').read_bytes()==b''
live=rd(N/'runs/static_base_parent_pr/stdout');assert live['state']=='OPEN' and not live['isDraft'] and live['headRefOid']==pub['headRefOid']
refs=(N/'runs/static_live_refs_2110/stdout').read_text().splitlines()
assert refs==(N/'runs/static_base_refs/stdout').read_text().splitlines()
assert refs==[pub['headRefOid'],pub['tree'],'5b0e1cc44f422fb0138b02eb071d3d16b40dfbb2','56c5c0ab64f532c5784e895b2f9aa6894fa334e0']
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=W).decode().strip()==pub['headRefOid']
assert subprocess.check_output(['git','status','--porcelain','-z'],cwd=W)==b''
rr=[]
for label in ('source_fetch_2110','open_inventory_2110','static_live_refs_2110'):
 p=N/'runs'/label/'EXECUTION.json';r=rd(p);assert r['exit_code']==0
 for k in ('stdout','stderr'):same(r[k]['path'],r[k])
 rr.append(pin(p))
D.mkdir(parents=True)
refresh=dict(utc=datetime.now(timezone.utc).isoformat(),refs={'HEAD':refs[0],'origin/main':refs[2],'origin/ai/execution':refs[3]},active_tree=refs[1],inventory=pin(N/'runs/open_inventory_2110/stdout'),actual_receipts=rr,scope='Actual21:10 root fetch/refs/inventory with unchanged selected refs and seven regular open PRs; clean regular OPEN9653 transport selected. Root reports unrelated campaign recovery/queue change only. Git transport is not a mathematical premise.')
wr(D/'FRESH_REFRESH.json',refresh)
base=dict(status='bound_actual_root_published_base',base_head=pub['headRefOid'],base_tree=pub['tree'],base_branch=pub['headRefName'],base_pr=pub['number'],base_parent_branch=live['baseRefName'],publication=pin(B/'PUBLICATION.json'),attachment=pin(B/'ATTACHMENT.json'),refresh=pin(D/'FRESH_REFRESH.json'),expected_refs=refresh['refs'],observations=obs)
wr(D/'ACTUAL_BASE_BINDING_INPUT.json',base)
review=dict(kind='root_integration_source_review',utc=datetime.now(timezone.utc).isoformat(),root_read_complete_for_changed_implementation=True,retained_audit=False,proposal_freeze=pin(O/'FINAL_FREEZE.json'),common=pin(O/'commuting_static_edge_common.py'),primary_unbound=pin(O/'proposed_primary_unbound.py'),source_publication_review=pin(R/'REVIEW.json'),actual_base_binding=pin(D/'ACTUAL_BASE_BINDING_INPUT.json'),metadata_receipts=receipts,local_members=391,immutable_bodies=5,direct_mathematical_parents=parents,source_review_command=rd(N/'runs/static_publication_source_review/EXECUTION.json')['argv'],scientific_executions=0,actual_canonical_acceptance=None,editable_prompt_files_changed=[],verified_reuse_functions=len(reuse),source_captures=len(capture),required_canonical_replacements=rd(R/'REVIEW.json')['required_canonical_replacements'],scope='Root completed review of the exact static adapter, full changed functions/globals, wrapper/status/certificate/PR scope, actual metadata source/receipts/full streams and copied evidence. Four actual adapter metadata runs; five scientific/source bodies unchanged. All249 primary source records,57 selected additional implementation/freshness records and391 adapter freeze members checked. Zero mathematical parents, one new root, no new edges; preserve every old graph datum.21 future canonical mutants;12 graph and7 receipt-predicate metadata corruptions. Supplied extra positive XX edge with full scalar and finite output window; original four-onsite microscopic supplier unresolved. N1FAIL partial negative material preserved. Exact clean OPEN9653 transport, current main/authority unchanged. Integration review is distinct from pending canonical/staged review. No science replay, native supply, mediator, autonomous halt/reuse or retained audit claim.')
wr(D/'ROOT_INTEGRATION_REVIEW.json',review)
print(json.dumps(dict(review=pin(D/'ROOT_INTEGRATION_REVIEW.json'),actual_base=pin(D/'ACTUAL_BASE_BINDING_INPUT.json'),refresh=pin(D/'FRESH_REFRESH.json'),scientific_executions=0)))

