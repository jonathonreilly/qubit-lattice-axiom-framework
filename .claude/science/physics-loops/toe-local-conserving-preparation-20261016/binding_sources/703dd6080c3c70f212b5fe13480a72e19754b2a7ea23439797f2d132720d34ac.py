from pathlib import Path
import ast,datetime,hashlib,json,subprocess
N=Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023');D=N/'publication_integration/local_conserving_preparation';O=N/'local_conserving_preparation_integration_proposal';W=N.parent/'correlation_worktree'
P='.claude/science/physics-loops/toe-local-conserving-preparation-20261016';NOTE='docs/LOCAL_CONSERVING_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-16.md';H='scripts/local_conserving_preparation_2026_10_16.py'
def pin(p):
 p=Path(p);b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def read(p):return json.loads(Path(p).read_text())
def same(p,r):
 a=pin(p);assert all(a[k]==r[k] for k in ['bytes','sha256']),str(p)
def git(*a):return subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
base='5379d02febf465dbca41dba0b9119da4dfe0b667'
assert git('rev-parse','HEAD')==base and git('branch','--show-current')=='physics-loop/toe-local-conserving-preparation-20261016'
assert git('diff','--cached','--name-only')==''
installed=read(D/'INSTALLED.json');prepared=read(D/'PREPARED.json')
assert installed['base_head']==base and installed['files']==prepared['canonical_files']
for name,row in installed['files'].items():same(W/name,row)
for phase in ['prepare','install']:assert read(D/'actions'/phase/'EXECUTION.json')['exit_code']==0
assert read(D/'ROOT_DIFF_REVIEW.json')['diff']==prepared['diff']
for name,preview in [(NOTE,'PROPOSED_NOTE.md'),(P+'/BODY_MAP.json','PROPOSED_BODY_MAP.json'),(P+'/SOURCE_MANIFEST.json','PROPOSED_SOURCE_MANIFEST.json'),(P+'/CLAIM_STATUS_CERTIFICATE.md','PROPOSED_CLAIM_STATUS_CERTIFICATE.md')]:assert (W/name).read_bytes()==(O/preview).read_bytes()
mapping=read(W/P/'BODY_MAP.json');note=(W/NOTE).read_bytes()
for row in mapping['bodies']:
 data=note[row['start_byte']:row['end_byte_exclusive']];assert data==Path(row['original']).read_bytes() and note.count(data)==1
 assert hashlib.sha256(data).hexdigest()==row['sha256'] and len(data)==row['bytes']
for parent in read(W/P/'PARENT_BINDING.json')['direct_canonical_parents']:same(W/parent['path'],parent)
assert pin(W/H)['sha256']=='21cee554a4a6ce63605dde848fce9c828f02eee843cc396f703bb2be8c7f6e72'
actual=read(W/P/'ACTUAL_BINDING.json');assert actual['root_read_complete'] is False and actual['canonical_review_evidence'] is None
assert actual['git_base']==base and actual['source_proposal_freeze']['sha256']=='34ee5fb0151e09ce59370cc397ecf1cc7a16203d254d3386e05809551d309f81'
manifest=read(W/P/'INPUT_MANIFEST.json')
for row in manifest['inputs']:same(W/row['path'],row)
payloads=[];selected={D/'PREPARED_DIFF_REVIEW_RECOVERY.json',D/'ROOT_DIFF_REVIEW.json'}
for label,exit_code in [('local_control_prepared_diff_review',1),('local_control_prepared_diff_review_recovery',0)]:
 run=N/'runs'/label;receipt=read(run/'EXECUTION.json');assert receipt['exit_code']==exit_code
 selected.add(run/'EXECUTION.json')
 for key in ['stdout','stderr','recorder','child_source_at_launch','source_capture']:
  same(receipt[key]['path'],receipt[key]);selected.add(Path(receipt[key]['path']))
for path in sorted(selected):payloads.append(dict(identity=pin(path),encoding='utf-8',content=path.read_text()))
text='''# Actual canonical source review

Installed note, maps, certificate, provenance implementation and all131 canonical files match the reviewed preparation exactly. The five source changes comprise the reviewed wrapper/body-map/manifest/certificate changes and canonical provenance adapter. Primary logic matches the reviewed source-only adapter; only its actual input-manifest hash and membership constants were filled at prepare. All8 complete scientific bodies are unchanged, with their earlier scoped analytical review reused. Complete meaningful wrapper/code differences were read; exact copied archives and mechanical binding data were checked by identity and full membership. The new149-byte trailing wrapper preserves the final body and normal note whitespace checks.

The source-only decisions, original null fields and partial imported-synthesis coverage remain historical. Actual source review, exact Git base and later canonical approval are separate records. The sole mathematical dependency is finite-energy lift fcc92808. Memory9643 is Git ancestry only. Period-wait versus fixed-duration dimensions/scalars remain distinct; explicit preparation composes with the author route and preserves W=VE* and gamma(W). Sparse compilation is excluded here. Physical fields, full control/SWAP, vacuum, phase, timing and calibration remain supplied; no microscopic driver, interacting-H or autonomous halt/reuse claim is added.

Prepare and install actually succeeded. The initial root diff-check recorder failed on a list-versus-dictionary schema assumption before changing canonical files. Its exact source, complete streams and failed receipt, and the explicit corrected source/successful receipt, are embedded below without relabeling. Subsequent normalization checks the actual dictionary keys and absolute paths. This was metadata, not a failed scientific argument or run.

This record approves installed canonical source for the remaining scoped provenance/cache/graph checks and separate final staged review. No primary has yet run at this canonical binding, and no scientific code or historical fixture is rerun. No retained audit, merge, main push or prompt/axiom change occurred.
'''
with (D/'ACTUAL_ROOT_CANONICAL_REVIEW.md').open('x') as f:f.write(text)
r=dict(kind='root_canonical_source_review',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),root_read_complete=True,git_base=base,
 bound_note_sha256=pin(W/NOTE)['sha256'],canonical_body_pins=mapping['bodies'],parent_binding=read(W/P/'PARENT_BINDING.json'),
 source_draft_freeze_sha256='34ee5fb0151e09ce59370cc397ecf1cc7a16203d254d3386e05809551d309f81',source_draft_review_sha256='7a8aee2ed961f86019774797ef924a0790f81731f49a03178f7028d6d05ee63b',
 prebinding_primary=pin(W/H),integration_common=pin(O/'local_conserving_preparation_common.py'),review=pin(D/'ACTUAL_ROOT_CANONICAL_REVIEW.md'),
 prepared=pin(D/'PREPARED.json'),installed=pin(D/'INSTALLED.json'),root_diff_review=pin(D/'ROOT_DIFF_REVIEW.json'),canonical_file_count=131,
 preserved_metadata_failure_and_recovery=payloads,scientific_executions=0,retained_audit=False,editable_prompt_files_changed=[])
with (D/'ACTUAL_ROOT_CANONICAL_REVIEW.json').open('x') as f:f.write(json.dumps(r,indent=2)+'\n')
print(json.dumps(dict(review=pin(D/'ACTUAL_ROOT_CANONICAL_REVIEW.json'),canonical_file_count=131,unchanged_bodies=8,scientific_executions=0)))
