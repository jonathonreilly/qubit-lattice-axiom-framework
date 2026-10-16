"""Record root's actual reviewed source correspondence; no scientific replay."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,ast,difflib,hashlib,json,subprocess,sys
N=Path(__file__).resolve().parents[1];O=N/'commuting_static_edge_integration_proposal';D=N/'publication_integration/commuting_static_edge';W=N.parent/'correlation_worktree';S=N/'commuting_static_edge_qualified_publication_draft'
P='.claude/science/physics-loops/toe-commuting-static-edge-fixed-target-20261016';NOTE='docs/COMMUTING_STATIC_EDGE_FIXED_TARGET_BOUNDED_THEOREM_NOTE_2026-10-16.md';H='scripts/commuting_static_edge_fixed_target_2026_10_16.py'

parser=argparse.ArgumentParser(description='Unexecuted root recorder proposal; only root may record a completed actual review.')
parser.add_argument('--root-reviewed',action='store_true',required=True)
parser.add_argument('mode',choices=['prepared','installed'])
EXPECTATION_KIND='static_canonical_review_expectations'

parser.add_argument('--expectations',type=Path,required=True)
parser.add_argument('--expectations-sha',required=True)
args=parser.parse_args()
assert args.root_reviewed
expect_raw=args.expectations.read_bytes()
assert hashlib.sha256(expect_raw).hexdigest()==args.expectations_sha
expect=json.loads(expect_raw)
assert expect['kind']==EXPECTATION_KIND and expect['root_completed_actual_read'] is True
assert expect['adapter_freeze_sha256']=='23bc904d202993554d09795b0783968b6f494768b9091bff1321a754ee1527a6'
assert all(value is not None for value in expect.values()), 'Null source templates are not actual review inputs'
mode=args.mode;assert expect['mode']==mode;R=D/'canonical_source' if mode=='prepared' else W
base='8b7b8b4768e2831b273bada5bcebf2b4175583f4'
def pin(p):
 p=Path(p);b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def read(p):return json.loads(Path(p).read_text())
def same(p,r):assert all(pin(p)[k]==r[k] for k in ('bytes','sha256')),str(p)
def write(p,v):
 with Path(p).open('x') as f:f.write(json.dumps(v,indent=2)+'\n')
def git(*a):return subprocess.check_output(['git',*a],cwd=W).decode().strip()
assert pin(O/'FINAL_FREEZE.json')['sha256']=='23bc904d202993554d09795b0783968b6f494768b9091bff1321a754ee1527a6'
assert git('rev-parse','HEAD')==base and git('diff','--cached','--name-only')==''
assert pin(D/'PREPARED.json')['sha256']==expect['prepared_sha256']
prepared=read(D/'PREPARED.json');expected_count=expect['canonical_file_count'];assert isinstance(expected_count,int) and expected_count>0
assert prepared['base_head']==base and len(prepared['canonical_files'])==expected_count
same(D/'CANONICALIZATION.diff',prepared['diff'])
assert prepared['diff']['sha256']==expect['canonicalization_diff_sha256']
for name,row in prepared['canonical_files'].items():same(R/name,row)
for p in (O/'payload').rglob('*'):
 if p.is_file(): assert (R/p.relative_to(O/'payload')).read_bytes()==p.read_bytes()
for p in S.rglob('*'):
 if p.is_file(): assert (R/P/'frozen_source'/p.relative_to(S)).read_bytes()==p.read_bytes()
mapping=read(R/P/'BODY_MAP.json');note=(R/NOTE).read_bytes()
for row in mapping['bodies']:
 raw=(N/row['source']).read_bytes();assert note[row['start_byte']:row['end_byte_exclusive']]==raw and note.count(raw)==1
 same(N/row['source'],row)
assert len(mapping['bodies'])==5
parent_binding=read(R/P/'PARENT_BINDING.json');assert parent_binding['direct_canonical_parents']==[]
assert parent_binding==read(O/'PARENT_BINDING.json')
for name in ['NO_GO_DISCIPLINE_CHECKLIST.md','APPROACH_REGISTRY.md','NO_GO_LEDGER.md','NO_GO_STATUS.json']:
 assert (R/P/name).read_bytes()==(S/'proposal'/P/name).read_bytes()
for parent in parent_binding['direct_canonical_parents']:same(W/parent['path'],parent)
originals={}
roots=[S,O,N/'root_commuting_static_edge_qualified_publication_review',D/'runs',N/'runs/static_publication_source_review',N/'runs/static_integration_review',N/'runs/source_fetch_2110',N/'runs/open_inventory_2110',N/'runs/static_base_refs',N/'runs/static_live_refs_2110',N/'publication_integration/endpoint_target_compilation']+[N/('runs/static_base_'+q) for q in ['head','tree','branch','status','parent_pr']]
paths=[p for root in roots for p in root.rglob('*') if p.is_file()]+[p for p in D.iterdir() if p.is_file()]+[N/'review_run.py',N/'run.py',N/'bootstrap/record_worktree_observation.py']
for p in paths:originals.setdefault(pin(p)['sha256'],p)
copies=[]
for p in (R/P/'binding_sources').iterdir():
 h=pin(p)['sha256'];assert p.stem==h and h in originals and p.read_bytes()==originals[h].read_bytes()
 copies.append(dict(copy=pin(p),original=pin(originals[h])))
manifest=read(R/P/'INPUT_MANIFEST.json')
for row in manifest['inputs']:same(R/row['path'] if (R/row['path']).exists() else W/row['path'],row)
trees=[ast.parse(p.read_text()) for p in [O/'proposed_primary_unbound.py',R/H]];assert len(trees[0].body)==len(trees[1].body)
changed=[];values={}
for a,b in zip(trees[0].body,trees[1].body):
 if ast.dump(a)!=ast.dump(b):
  assert isinstance(a,ast.Assign) and isinstance(b,ast.Assign) and [ast.dump(t) for t in a.targets]==[ast.dump(t) for t in b.targets]
  changed.append(a.targets[0].id);values[a.targets[0].id]=ast.literal_eval(b.value)
expected=dict(MANIFEST_SHA256=pin(R/P/'INPUT_MANIFEST.json')['sha256'],AUDIT_INPUT_PATHS=tuple(sorted({row['path'] for row in manifest['inputs']}|{P+'/INPUT_MANIFEST.json'})),EXPECTED_GIT_BASE=base,EXPECTED_BASE_PR=9653,EXPECTED_BASE_BRANCH='physics-loop/toe-positive-onsite-target-compilation-20261016',EXPECTED_BASE_PARENT_BRANCH='physics-loop/toe-positive-onsite-endpoint-chart-recurrence-20261016',EXPECTED_ROOT_REVIEW_SHA='8c734556a0ffab117468cbcc993cb95f61ad32bb0b1f123c4ea549fffa182d3b',EXPECTED_ROOT_REVIEW_COMMAND=tuple(read(N/'runs/static_publication_source_review/EXECUTION.json')['argv']),EXPECTED_ROOT_EXECUTION_SHA=pin(N/'runs/static_publication_source_review/EXECUTION.json')['sha256'],EXPECTED_ROOT_RECORDER_SHA=pin(N/'review_run.py')['sha256'])
assert values==expected
actual=read(R/P/'ACTUAL_BINDING.json');canonical=read(R/P/'CANONICAL_BINDING.json')
assert actual['root_read_complete'] is False and actual['canonical_review_evidence'] is None
assert actual['git_base']==base and actual['raw_bodies']==mapping['bodies'] and actual['parent_binding']==parent_binding
assert actual['source_body_pins']==read(S/'proposal'/P/'BODY_MAP.json')['bodies']
assert actual['note_sha256']==pin(R/NOTE)['sha256'] and actual['source_proposal_freeze']['sha256']==pin(S/'FINAL_FREEZE.json')['sha256']
assert actual['observed_parent_prs']=={'base':read(D/'runs/prepare_parent_base/stdout')}
assert actual['origin_main']=='5b0e1cc44f422fb0138b02eb071d3d16b40dfbb2' and actual['instruction_revision']=='56c5c0ab64f532c5784e895b2f9aa6894fa334e0'
assert canonical['actual_git_base']==base and canonical['actual_checkout_head']==base and canonical['receipt_paths']==actual['receipt_paths']
assert canonical['root_read_complete'] is False and canonical['bound_note_sha256']==pin(R/NOTE)['sha256']
def verify_copies(value):
 if isinstance(value,dict):
  if {'path','bytes','sha256'}<=set(value) and value['path'].startswith(P+'/binding_sources/'):same(R/value['path'],value)
  for v in value.values():verify_copies(v)
 elif isinstance(value,list):
  for v in value:verify_copies(v)
for data in [actual,canonical,read(R/P/'ACTUAL_REFRESH_PROVENANCE.json')]:verify_copies(data)
assert read(D/'actions/prepare/EXECUTION.json')['exit_code']==0
delta=(O/'NOTE_FULL.diff').read_text()
for name in sorted(prepared['canonical_files']):
 path=R/name
 old=O/'payload'/name
 if name.startswith(P+'/frozen_source/'):old=S/name.removeprefix(P+'/frozen_source/')
 if old.exists() and old.read_bytes()==path.read_bytes():continue
 delta+=''.join(difflib.unified_diff(old.read_text().splitlines(True) if old.exists() else [],path.read_text().splitlines(True),fromfile='draft/'+name,tofile='canonical/'+name))
assert delta==(D/'CANONICALIZATION.diff').read_text()

scope='Root completed actual read of the exact changed wrapper, adapter and bindings. Five unchanged bodies retain controlling qualifications; all actual prepared canonical paths, full frozen source, every binding copy and ten literal assignments are checked. Full generated diff reconstructed byte-for-byte. Zero mathematical parents; staged runner and N1FAIL sidecars retained. Canonical and staged decisions remain distinct. No science replay or physical validation.'
if mode=='prepared':
 assert git('status','--porcelain')==''
 r=dict(kind='root_prepared_diff_review',utc=datetime.now(timezone.utc).isoformat(),diff=prepared['diff'],canonical_files=expected_count,unchanged_bodies=5,primary_changed_literal_assignments=changed,binding_copies=copies,scope=scope,scientific_executions=0,retained_audit=False)
 r.update(review_expectations=expect,review_expectation_source=pin(args.expectations),review_expectations_original_utf8=expect_raw.decode('utf-8'))
 write(D/'ROOT_DIFF_REVIEW.json',r);print(json.dumps(dict(review=pin(D/'ROOT_DIFF_REVIEW.json'),diff=prepared['diff'],primary=pin(R/H),binding_objects=len(copies))))
else:
 assert git('branch','--show-current')=='physics-loop/toe-commuting-static-edge-fixed-target-20261016'
 assert read(D/'INSTALLED.json')['files']==prepared['canonical_files'] and read(D/'actions/install/EXECUTION.json')['exit_code']==0
 assert read(D/'ROOT_DIFF_REVIEW.json')['diff']==prepared['diff']
 r=dict(kind='root_canonical_source_review',utc=datetime.now(timezone.utc).isoformat(),root_read_complete=True,git_base=base,bound_note_sha256=pin(R/NOTE)['sha256'],canonical_body_pins=mapping['bodies'],parent_binding=parent_binding,source_draft_freeze_sha256=pin(S/'FINAL_FREEZE.json')['sha256'],source_draft_review_sha256=expected['EXPECTED_ROOT_REVIEW_SHA'],prebinding_primary=pin(R/H),integration_common=pin(O/'commuting_static_edge_common.py'),prepared=pin(D/'PREPARED.json'),installed=pin(D/'INSTALLED.json'),root_diff_review=pin(D/'ROOT_DIFF_REVIEW.json'),canonical_file_count=expected_count,root_diff_review_payload=read(D/'ROOT_DIFF_REVIEW.json'),scope=scope,qualifications='Fixed K,W,T and supplied extra positive XX interaction on existing old edge, full scalar and arbitrary old/reference output, finite quiet window and explicit coefficient/timing/energy/covariance allowances. Original four-onsite microscopic supplier remains open. One historical author rational fixture, no replay or imposed OS CPU/RAM quota. Static-X negative submission remains N1FAIL partial material. Optional driven ramps are separate; installation, native hardware, autonomous halt and reuse remain unresolved. No mediator or retained audit',scientific_executions=0,retained_audit=False,editable_prompt_files_changed=[])
 r.update(review_expectations=expect,review_expectation_source=pin(args.expectations),review_expectations_original_utf8=expect_raw.decode('utf-8'))
 write(D/'ACTUAL_ROOT_CANONICAL_REVIEW.json',r);print(json.dumps(dict(review=pin(D/'ACTUAL_ROOT_CANONICAL_REVIEW.json'),canonical_file_count=expected_count,unchanged_bodies=5,scientific_executions=0)))
