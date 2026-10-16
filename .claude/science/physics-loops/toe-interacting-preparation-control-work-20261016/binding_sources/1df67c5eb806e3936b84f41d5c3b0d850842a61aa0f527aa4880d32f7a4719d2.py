"""Record root's actual reviewed source correspondence; no scientific replay."""
from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json,subprocess,sys
N=Path(__file__).resolve().parents[1];O=N/'interacting_control_integration_proposal';D=N/'publication_integration/interacting_control';W=N.parent/'correlation_worktree';S=N/'interacting_control_qualified_publication_draft'
P='.claude/science/physics-loops/toe-interacting-preparation-control-work-20261016';NOTE='docs/INTERACTING_PREPARATION_CONTROL_WORK_BOUNDED_THEOREM_NOTE_2026-10-16.md';H='scripts/interacting_preparation_control_work_2026_10_16.py'
mode=sys.argv[1];assert mode in ('prepared','installed');R=D/'canonical_source' if mode=='prepared' else W
base='7cce8eaa5a72862e0ba884028a21e792c04a6df7'
def pin(p):
 p=Path(p);b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def read(p):return json.loads(Path(p).read_text())
def same(p,r):assert all(pin(p)[k]==r[k] for k in ('bytes','sha256')),str(p)
def write(p,v):
 with Path(p).open('x') as f:f.write(json.dumps(v,indent=2)+'\n')
def git(*a):return subprocess.check_output(['git',*a],cwd=W).decode().strip()
assert git('rev-parse','HEAD')==base and git('diff','--cached','--name-only')==''
prepared=read(D/'PREPARED.json');assert prepared['base_head']==base and len(prepared['canonical_files'])==229
same(D/'CANONICALIZATION.diff',prepared['diff'])
assert prepared['diff']['sha256']=='32f294ad73c8921835d94441e9f6279cbfa82de52ac6c05c1aac74f99bc33bbc'
for name,row in prepared['canonical_files'].items():same(R/name,row)
for p in (O/'payload').rglob('*'):
 if p.is_file(): assert (R/p.relative_to(O/'payload')).read_bytes()==p.read_bytes()
for p in S.rglob('*'):
 if p.is_file(): assert (R/P/'frozen_source'/p.relative_to(S)).read_bytes()==p.read_bytes()
mapping=read(R/P/'BODY_MAP.json');note=(R/NOTE).read_bytes()
for row in mapping['bodies']:
 raw=(N/row['source']).read_bytes();assert note[row['start_byte']:row['end_byte_exclusive']]==raw and note.count(raw)==1
 same(N/row['source'],row)
assert len(mapping['bodies'])==9
parent_binding=read(R/P/'PARENT_BINDING.json')
for parent in parent_binding['direct_canonical_parents']:same(W/parent['path'],parent)
originals={}
roots=[S,O,N/'root_interacting_control_qualified_publication_review',D/'runs',N/'runs/interacting_control_source_publication_review_v2',N/'runs/interacting_integration_source_review',N/'runs/source_fetch_1854',N/'runs/open_inventory_1854',N/'runs/interacting_base_refs_1854']
paths=[p for root in roots for p in root.rglob('*') if p.is_file()]+[p for p in D.iterdir() if p.is_file()]+[N/'review_run.py']
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
expected=dict(MANIFEST_SHA256=pin(R/P/'INPUT_MANIFEST.json')['sha256'],AUDIT_INPUT_PATHS=tuple(sorted({row['path'] for row in manifest['inputs']}|{P+'/INPUT_MANIFEST.json'})),EXPECTED_GIT_BASE=base,EXPECTED_BASE_PR=9648,EXPECTED_BASE_BRANCH='physics-loop/toe-inhomogeneous-comb-local-control-20261016',EXPECTED_BASE_PARENT_BRANCH='physics-loop/toe-local-conserving-sparse-current-main-20261016',EXPECTED_ROOT_REVIEW_SHA='6359efd97be3f28ed504430a501269027ad279fd2738a258a9d222d801f47f67',EXPECTED_ROOT_REVIEW_COMMAND=tuple(read(N/'runs/interacting_control_source_publication_review_v2/EXECUTION.json')['argv']),EXPECTED_ROOT_EXECUTION_SHA=pin(N/'runs/interacting_control_source_publication_review_v2/EXECUTION.json')['sha256'],EXPECTED_ROOT_RECORDER_SHA=pin(N/'review_run.py')['sha256'])
assert values==expected
actual=read(R/P/'ACTUAL_BINDING.json');canonical=read(R/P/'CANONICAL_BINDING.json')
assert actual['root_read_complete'] is False and actual['canonical_review_evidence'] is None
assert actual['git_base']==base and actual['raw_bodies']==mapping['bodies'] and actual['parent_binding']==parent_binding
assert actual['source_body_pins']==read(S/'proposal'/P/'BODY_MAP.json')['bodies']
assert actual['note_sha256']==pin(R/NOTE)['sha256'] and actual['source_proposal_freeze']['sha256']==pin(S/'FREEZE.json')['sha256']
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
scope='All changed note wrapper and executable code reviewed. The complete prepared diff is accounted for through exact preview/source bodies, copied original evidence, all added binding fields and all ten literal assignments. Immutable source records retain nulls and failures. No scientific execution or new proof acceptance is implied by these metadata checks.'
if mode=='prepared':
 assert git('status','--porcelain')==''
 r=dict(kind='root_prepared_diff_review',utc=datetime.now(timezone.utc).isoformat(),diff=prepared['diff'],canonical_files=229,unchanged_bodies=9,primary_changed_literal_assignments=changed,binding_copies=copies,scope=scope,scientific_executions=0,retained_audit=False)
 write(D/'ROOT_DIFF_REVIEW.json',r);print(json.dumps(dict(review=pin(D/'ROOT_DIFF_REVIEW.json'),diff=prepared['diff'],primary=pin(R/H),binding_objects=len(copies))))
else:
 assert git('branch','--show-current')=='physics-loop/toe-interacting-preparation-control-work-20261016'
 assert read(D/'INSTALLED.json')['files']==prepared['canonical_files'] and read(D/'actions/install/EXECUTION.json')['exit_code']==0
 assert read(D/'ROOT_DIFF_REVIEW.json')['diff']==prepared['diff']
 r=dict(kind='root_canonical_source_review',utc=datetime.now(timezone.utc).isoformat(),root_read_complete=True,git_base=base,bound_note_sha256=pin(R/NOTE)['sha256'],canonical_body_pins=mapping['bodies'],parent_binding=parent_binding,source_draft_freeze_sha256=pin(S/'FREEZE.json')['sha256'],source_draft_review_sha256=expected['EXPECTED_ROOT_REVIEW_SHA'],prebinding_primary=pin(R/H),integration_common=pin(O/'interacting_control_common.py'),prepared=pin(D/'PREPARED.json'),installed=pin(D/'INSTALLED.json'),root_diff_review=pin(D/'ROOT_DIFF_REVIEW.json'),canonical_file_count=229,root_diff_review_payload=read(D/'ROOT_DIFF_REVIEW.json'),scope=scope,qualifications='Literal interacting old K, positive complements on actual supports, exact vacuum/isolation and complete controlled schedules remain supplied. Nine unchanged bodies retain noncommuting forward ramps, full preparation aging and target L_b* V E_p* R_b*, scalar reserves and complete resource/ancilla/reference outputs. M=L+2 and sufficiently-large idle intervals control the fault example. Fixed-q nominal laboratory O(epsilon^-4) excludes classical compilation. Generator epsilon^5 versus cancellation-input epsilon^9 differ. Original F0 work includes preparation; coherent runtime fixed-bandwidth/global-action work bounds do not automatically cover preparation or arbitrary baths; moments retain width/covariance. One historical floating bridge fixture is not certified ODE; other extensions analytical. No native supply, autonomous halt, microscopic controller accounting, retained audit or indefinite reuse.',scientific_executions=0,retained_audit=False,editable_prompt_files_changed=[])
 write(D/'ACTUAL_ROOT_CANONICAL_REVIEW.json',r);print(json.dumps(dict(review=pin(D/'ACTUAL_ROOT_CANONICAL_REVIEW.json'),canonical_file_count=229,unchanged_bodies=9,scientific_executions=0)))
