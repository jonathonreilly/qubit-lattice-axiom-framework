"""Record root's completed review of actual installed canonical preparation sources."""
from pathlib import Path
from datetime import datetime, timezone
import ast, hashlib, json, subprocess
N=Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023')
D=N/'publication_integration/bus_preparation'; P=N/'bus_preparation_integration_proposal'; W=N.parent/'correlation_worktree'
K='.claude/science/physics-loops/toe-bus-installed-preparation-20261016'
NOTE='docs/BUS_INSTALLED_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-16.md'
HELPER='scripts/bus_installed_preparation_2026_10_16.py'
def read(p):return json.loads(p.read_text())
def pin(p):
 b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def same(p,r):assert all(pin(p)[k]==r[k] for k in ('bytes','sha256')),str(p)
def write(p,d):assert not p.exists();p.write_text(json.dumps(d,indent=2)+'\n')
pre=read(D/'PREPARED.json');assert read(D/'actions/install/EXECUTION.json')['exit_code']==0
for name,row in pre['canonical_files'].items():same(W/name,row)
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=W).decode().strip()=='142cbd74aa146848b246795f8bf7007f3e38976d'
assert subprocess.check_output(['git','branch','--show-current'],cwd=W).decode().strip()=='physics-loop/toe-bus-preparation-20261016'
assert (W/NOTE).read_bytes()==(P/'PROPOSED_NOTE.md').read_bytes()
mapping=read(W/K/'BODY_MAP.json');assert mapping==read(P/'PROPOSED_BODY_MAP.json')
assert read(W/K/'PARENT_BINDING.json')==read(P/'PARENT_BINDING.json')
a=ast.parse((P/'proposed_primary_unbound.py').read_bytes());b=ast.parse((W/HELPER).read_bytes());assert len(a.body)==len(b.body)
changed={}
for x,y in zip(a.body,b.body):
 if ast.dump(x)!=ast.dump(y):
  assert isinstance(x,ast.Assign) and isinstance(y,ast.Assign) and ast.dump(x.targets[0])==ast.dump(y.targets[0])
  changed[x.targets[0].id]=ast.literal_eval(y.value)
assert set(changed)=={'MANIFEST_SHA256','AUDIT_INPUT_PATHS'}
manifest=read(W/K/'INPUT_MANIFEST.json')
assert changed['MANIFEST_SHA256']==pin(W/K/'INPUT_MANIFEST.json')['sha256']
assert set(changed['AUDIT_INPUT_PATHS'])=={r['path'] for r in manifest['inputs']}|{K+'/INPUT_MANIFEST.json'}
for row in manifest['inputs']:same(W/row['path'],row)
source=P/'source_snapshot/proposal'
for path in source.rglob('*'):
 if path.is_file() and str(path.relative_to(source)) not in {NOTE,HELPER,K+'/BODY_MAP.json'}:
  assert (W/path.relative_to(source)).read_bytes()==path.read_bytes()
for path in (W/K/'binding_sources').iterdir():assert pin(path)['sha256']==path.stem
actual=read(W/K/'ACTUAL_BINDING.json')
assert actual['root_read_complete'] is False and actual['canonical_review_evidence'] is None
assert actual['parent_binding']==read(P/'PARENT_BINDING.json')
review=dict(utc=datetime.now(timezone.utc).isoformat(),kind='root_actual_canonical_source_review',root_read_complete=True,
 git_base=pre['base_head'],bound_note_sha256=pin(W/NOTE)['sha256'],canonical_body_pins=mapping['bodies'],
 parent_binding=read(W/K/'PARENT_BINDING.json'),source_draft_freeze_sha256='ed576446fcbf5f0aae92054730165082e2c68567b09baaf389d36b49f6d87278',
 source_draft_review_sha256='2a3a63df329ab362081fe3c8f65cffcffb29b644398a70ace2c396a332db3990',
 prebinding_primary=pin(W/HELPER),integration_common=pin(P/'bus_preparation_common.py'),
 integration_source_review=pin(N/'root_bus_preparation_integration_review/REVIEW.json'),reviewed_diff=pin(D/'CANONICALIZATION.diff'),
 review_basis='Reviewed all new wrapper and implementation text, actual binding/refresh metadata and actual preparation receipts. Reused prior complete body/source reviews by exact identities. Generated literal tables and copied evidence were checked deterministically in full; truncated raw-diff display was not treated as verification.',
 actual_installed_files_checked=len(pre['canonical_files']),primary_logic_delta_from_reviewed_unbound=0,
 actual_next_step='Bind this real review and run scoped provenance/cache checks; staged review still required before regular PR.',
 limitations='No new scientific executions, physical supplier, model independence or retained-audit verdict. Literal-Q and U_E contracts remain distinct. Resource and memory-recovery work excluded.',
 retained_audit=False,editable_prompt_files_changed=[])
failed=N/'runs/bus_preparation_canonical_review'
failure=read(failed/'EXECUTION.json');assert failure['exit_code']==1
for key in ('stdout','stderr','source_capture'):same(Path(failure[key]['path']),failure[key])
review['previous_recording_failure']={'reason':'Original review output name already held the install-phase diff acknowledgement; all checks ran, but exclusive creation stopped before a review write.',
 'execution':failure,'execution_pin':pin(failed/'EXECUTION.json'),
 'source':(failed/'executed_source.py').read_text(),'stdout':(failed/'stdout').read_text(),'stderr':(failed/'stderr').read_text(),
 'preservation':'Original action acknowledgement, failed script and complete failed receipt streams are unchanged; this corrected source writes a distinct name.'}
write(D/'ACTUAL_ROOT_CANONICAL_REVIEW.json',review)
print(json.dumps({'review':pin(D/'ACTUAL_ROOT_CANONICAL_REVIEW.json')},indent=2))
