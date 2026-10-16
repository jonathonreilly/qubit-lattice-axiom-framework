"""Record completed root prepared/installed source review; deterministic metadata only."""
from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json,re,subprocess,sys
N=Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023');O=N/'local_conserving_sparse_parent_refresh_recovery';D=N/'publication_integration/local_conserving_sparse';W=N.parent/'correlation_worktree';S=N/'local_conserving_sparse_qualified_publication_draft'
P='.claude/science/physics-loops/toe-local-conserving-sparse-20261016';NOTE='docs/LOCAL_CONSERVING_SPARSE_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-16.md';H='scripts/local_conserving_sparse_2026_10_16.py';base='98c9eaf1702d74f5f19649f8140e9fbdc83a2345'
mode=sys.argv[1];assert mode in ['prepared','installed'];R=D/'canonical_source' if mode=='prepared' else W
def pin(p):
 p=Path(p);b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def read(p):return json.loads(Path(p).read_text())
def same(p,r):assert all(pin(p)[k]==r[k] for k in ['bytes','sha256']),str(p)
def write(p,v):
 with Path(p).open('x') as f:f.write(json.dumps(v,indent=2)+'\n')
def git(*a):return subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
assert git('rev-parse','HEAD')==base and git('diff','--cached','--name-only')==''
prepared=read(D/'PREPARED.json');assert prepared['base_head']==base and len(prepared['canonical_files'])==209
same(D/'CANONICALIZATION.diff',prepared['diff'])
assert prepared['diff']['sha256']=='173b4c82649bc872b10a1f756da8f6d5b6a09261cf0b0aa71b8088c579828d2d'
for name,row in prepared['canonical_files'].items():same(R/name,row)
for name,preview in [(NOTE,'PROPOSED_NOTE.md'),(P+'/BODY_MAP.json','PROPOSED_BODY_MAP.json'),(P+'/SOURCE_MANIFEST.json','PROPOSED_SOURCE_MANIFEST.json'),(P+'/CLAIM_STATUS_CERTIFICATE.md','PROPOSED_CLAIM_STATUS_CERTIFICATE.md')]:assert (R/name).read_bytes()==(O/preview).read_bytes()
mapping=read(R/P/'BODY_MAP.json');note=(R/NOTE).read_bytes()
for row in mapping['bodies']:
 raw=Path(row['original_path']).read_bytes();assert note[row['start_byte']:row['end_byte_exclusive']]==raw and note.count(raw)==1
 assert hashlib.sha256(raw).hexdigest()==row['sha256'] and len(raw)==row['bytes']
assert len(mapping['bodies'])==7
for p in S.rglob('*'):
 if p.is_file():assert (R/P/'frozen_source'/p.relative_to(S)).read_bytes()==p.read_bytes()
for parent in read(R/P/'PARENT_BINDING.json')['direct_canonical_parents']:same(W/parent['path'],parent)
trees=[ast.parse(p.read_text()) for p in [O/'proposed_primary_unbound.py',R/H]]
assert len(trees[0].body)==len(trees[1].body)
changed=[]
for a,b in zip(trees[0].body,trees[1].body):
 if ast.dump(a,include_attributes=False)!=ast.dump(b,include_attributes=False):
  assert isinstance(a,ast.Assign) and isinstance(b,ast.Assign) and [ast.dump(x) for x in a.targets]==[ast.dump(x) for x in b.targets]
  changed.append(a.targets[0].id);ast.literal_eval(b.value)
assert set(changed)=={'MANIFEST_SHA256','AUDIT_INPUT_PATHS','EXPECTED_BASE_PARENT_BRANCH'}
assert pin(R/H)['sha256']=='c0592bd09d493675515ae478d0ff4ec238646b139afd7d786cfd0e2624ed8738'
manifest=read(R/P/'INPUT_MANIFEST.json')
for row in manifest['inputs']:same(R/row['path'] if (R/row['path']).exists() else W/row['path'],row)
assigned={a.targets[0].id:ast.literal_eval(a.value) for a in trees[1].body if isinstance(a,ast.Assign) and isinstance(a.targets[0],ast.Name) and a.targets[0].id in ['MANIFEST_SHA256','AUDIT_INPUT_PATHS','EXPECTED_BASE_PARENT_BRANCH']}
assert assigned['MANIFEST_SHA256']==pin(R/P/'INPUT_MANIFEST.json')['sha256'] and assigned['EXPECTED_BASE_PARENT_BRANCH']=='main'
assert set(assigned['AUDIT_INPUT_PATHS'])=={row['path'] for row in manifest['inputs']}|{P+'/INPUT_MANIFEST.json'}
actual=read(R/P/'ACTUAL_BINDING.json');assert actual['root_read_complete'] is False and actual['canonical_review_evidence'] is None and actual['git_base']==base
assert actual['source_proposal_freeze']['sha256']=='8f59a94d8583f02f04b1df7824a47496de789e12d8a4094affc54a38da0b954c'
assert actual['observed_parent_prs']['base']['baseRefName']=='main'
originals={}
roots=[S,O,N/'root_local_conserving_sparse_qualified_publication_review',D/'runs',N/'runs/qualified_sparse_source_review',N/'sparse_parent_refresh',N/'runs/fetch_sparse_parent_refresh',N/'runs/inventory_sparse_parent_refresh',N/'runs/sparse_parent_refresh_pr_9646']
paths=[p for root in roots for p in root.rglob('*') if p.is_file()]+[p for p in D.iterdir() if p.is_file()]+[N/'review_run.py']
for p in paths:originals.setdefault(pin(p)['sha256'],p)
binding_copies=[]
for p in (R/P/'binding_sources').iterdir():
 h=pin(p)['sha256'];assert p.stem==h and h in originals and p.read_bytes()==originals[h].read_bytes()
 binding_copies.append(dict(copy=pin(p),original=pin(originals[h])))
def parser(path):
 selected=[]
 for node in ast.parse(Path(path).read_text()).body:
  if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id in ['CLAIM_TYPES','CLAIM_TYPE_LINE_RE','TYPE_LINE_RE'] for t in node.targets):selected.append(node)
  elif isinstance(node,ast.FunctionDef) and node.name in ['normalize_claim_type','extract_claim_type_hint']:selected.append(node)
 ns={'re':re};exec(compile(ast.Module(body=selected,type_ignores=[]),'<exact source-pinned parser functions>','exec'),ns);return ns
oldpath=W/'docs/audit/scripts/build_citation_graph.py';newpath=N/'sparse_publication_refresh/build_citation_graph_current_main.py'
old=parser(oldpath)['extract_claim_type_hint'](note.decode());new=parser(newpath)['extract_claim_type_hint'](note.decode())
assert old==new and old[1]=='bounded_theorem'
assert subprocess.check_output(['git','-C',str(W),'show','de540f645a284854753e19f5b5f954cb41185b6e:docs/audit/scripts/build_citation_graph.py'])==newpath.read_bytes()
assert read(D/'actions/prepare_parent_refresh/EXECUTION.json')['exit_code']==0 and read(D/'actions/prepare/EXECUTION.json')['exit_code']==1
if mode=='prepared':
 assert git('status','--porcelain')==''
 r=dict(kind='root_prepared_diff_review',utc=datetime.now(timezone.utc).isoformat(),diff=prepared['diff'],canonical_files=209,unchanged_bodies=7,primary_changed_literal_assignments=changed,binding_copies=binding_copies,current_main_claim_parser=dict(pinned=pin(oldpath),current=pin(newpath),pinned_result=old,current_result=new),
  scope='All new wrapper/code/actual-binding changes reviewed. Exact historical bodies, archives, copied receipts and mechanical membership reuse checked by identity, not described as a full fresh science review. Original prepare failure retained; distinct recovery prepare actually succeeded.',scientific_executions=0,retained_audit=False)
 write(D/'ROOT_DIFF_REVIEW.json',r);print(json.dumps(dict(review=pin(D/'ROOT_DIFF_REVIEW.json'),diff=prepared['diff'],primary=pin(R/H),binding_objects=len(binding_copies),parser_result=new)))
else:
 assert git('branch','--show-current')=='physics-loop/toe-local-conserving-sparse-20261016'
 installed=read(D/'INSTALLED.json');assert installed['files']==prepared['canonical_files'] and installed['base_head']==base
 assert read(D/'actions/install/EXECUTION.json')['exit_code']==0 and read(D/'ROOT_DIFF_REVIEW.json')['diff']==prepared['diff']
 text='''# Actual canonical source review

The installed canonical note and all209 prepared files match the reviewed proposal and actual preparation. Seven complete mathematical bodies remain byte-identical at their qualified source pins. The wrapper, source-specific primary and five-function parent-refresh amendment were read completely before execution. Prepared primary differs only in its exact input manifest, declared paths and actual current parent branch main. Exact copied archives and mechanical binding records were checked against their originals; no independent scientific replay is implied.

The original prepare exited1 because PR9645 was externally retargeted while its head remained98c9eaf1. Its failure, prior approval and binding stay immutable. The separate recovery prepare and install exited0. Historical publication parent and current live parent remain distinct. Current-main and pinned worktree parsers agree on this actual note's explicit bounded_theorem type; the new main parser was checked against de540f645a. This does not assert integrated-current-main validation.

The sole mathematical parent is local conserving preparation6db93809. Source acceptance999446a2 and fixture qualification449fed27 remain conditional. Fixed-q nominal laboratory time is O(epsilon^-4); classical finite-grid compilation time is excluded. The emitted-word fixture is one q1L1 floating propagation with structural/saved-matrix inspection, not independent propagation, interval certification or a general emitted compiler. Full scalars, equal-gap literal old K, initial/final energy errors, complete resource moments, ready input, supplied path/full SWAP/positive control/calibration remain explicit. No new preparation composition, native actuator, autonomous halt or indefinite reuse is established.

This approves actual installed canonical source for scoped provenance/cache/graph checks and later staged review. No scientific program or historical fixture has run in these metadata actions. No retained audit, main push, merge or prompt/axiom edit occurred.
'''
 with (D/'ACTUAL_ROOT_CANONICAL_REVIEW.md').open('x') as f:f.write(text)
 preserved=[]
 for label,expected in [('sparse_prepared_diff_review',1),('sparse_prepared_diff_review_path_recovery',0)]:
  run=N/'runs'/label;receipt=read(run/'EXECUTION.json');assert receipt['exit_code']==expected
  selected={run/'EXECUTION.json'}
  for key in ['stdout','stderr','recorder','child_source_at_launch','source_capture']:
   same(receipt[key]['path'],receipt[key]);selected.add(Path(receipt[key]['path']))
  preserved.extend(dict(identity=pin(p),encoding='utf-8',content=p.read_text()) for p in sorted(selected))
 r=dict(kind='root_canonical_source_review',utc=datetime.now(timezone.utc).isoformat(),root_read_complete=True,git_base=base,bound_note_sha256=pin(W/NOTE)['sha256'],canonical_body_pins=mapping['bodies'],parent_binding=read(W/P/'PARENT_BINDING.json'),source_draft_freeze_sha256='8f59a94d8583f02f04b1df7824a47496de789e12d8a4094affc54a38da0b954c',source_draft_review_sha256='9927849edd289e7ce206e0abb06d0908a9cc760d0b3dc749c7961c096e607f18',prebinding_primary=pin(W/H),integration_common=pin(O/'local_conserving_sparse_common.py'),review=pin(D/'ACTUAL_ROOT_CANONICAL_REVIEW.md'),prepared=pin(D/'PREPARED.json'),installed=pin(D/'INSTALLED.json'),root_diff_review=pin(D/'ROOT_DIFF_REVIEW.json'),canonical_file_count=209,root_diff_review_payload=(D/'ROOT_DIFF_REVIEW.json').read_text(),preserved_metadata_attempts=preserved,metadata_correction='Original diff recorder used scripts/build_citation_graph.py; actual pinned path is docs/audit/scripts/build_citation_graph.py. Original source and exit1 remain preserved. Two lookup paths corrected in a distinct source/run; no canonical file was altered by the failed record.',scientific_executions=0,retained_audit=False,editable_prompt_files_changed=[])
 write(D/'ACTUAL_ROOT_CANONICAL_REVIEW.json',r);print(json.dumps(dict(review=pin(D/'ACTUAL_ROOT_CANONICAL_REVIEW.json'),canonical_file_count=209,unchanged_bodies=7,scientific_executions=0)))
