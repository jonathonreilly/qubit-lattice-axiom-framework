"""Record root's completed wrapper/code review; verify exact existing evidence without replay."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,difflib
N=Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023');S=N/'inhomogeneous_comb_qualified_publication_draft';P=S/'proposal';O=N/'root_inhomogeneous_comb_qualified_publication_review'
PK='.claude/science/physics-loops/toe-inhomogeneous-comb-local-control-20261016';NOTE='docs/INHOMOGENEOUS_COMB_LOCAL_CONTROL_BOUNDED_THEOREM_NOTE_2026-10-16.md';H='scripts/inhomogeneous_comb_local_control_2026_10_16.py'
def pin(p):
 p=Path(p);b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def read(p):return json.loads(Path(p).read_text())
def same(p,r):assert all(pin(p)[k]==r[k] for k in ['bytes','sha256']),str(p)
def write(p,v):
 with Path(p).open('x') as f:f.write(json.dumps(v,indent=2)+'\n')
assert pin(S/'FREEZE.json')['sha256']=='25812bc2fb455c702fb471fefaafee254667e6d0907bdc95d68358d0a46d0a1e'
freeze=read(S/'FREEZE.json');assert len(freeze['members'])==193
for r in freeze['members']:same(S/r['path'],r)
assert {str(p.relative_to(S)) for p in S.rglob('*') if p.is_file()}=={r['path'] for r in freeze['members']}|{'FREEZE.json'}
assert not any(p.is_symlink() for p in S.rglob('*'))
rows=read(P/PK/'SOURCE_MANIFEST.json')['sources'];assert len(rows)==288
for r in rows:same(P/r['recovery_path'],r);same(r['original_path'],r)
assert len({r['sha256'] for r in rows})==126
mapping=read(P/PK/'BODY_MAP.json');body=(P/NOTE).read_bytes();assert len(mapping['bodies'])==6
for r in mapping['bodies']:
 raw=(N/r['source']).read_bytes();same(N/r['source'],r)
 assert body[r['start_byte_inclusive']:r['end_byte_exclusive']]==raw and body.count(raw)==1
assert body[:mapping['new_wrapper_bytes'][1]]==(S/'packet_text/WRAPPER.md').read_bytes()
manifest=read(P/PK/'INPUT_MANIFEST.json')
for r in manifest['inputs']:same(P/r['path'],r)
source=(S/'primary_template.py').read_text();generated=source.replace('__MANIFEST_SHA256__',pin(P/PK/'INPUT_MANIFEST.json')['sha256']).replace('__AUDIT_INPUT_PATHS__',repr([r['path'] for r in manifest['inputs']]+[PK+'/INPUT_MANIFEST.json'])).replace('__EXPECTED_BODIES__',repr({r['name']:r['sha256'] for r in mapping['bodies']}))
assert (P/H).read_text()==generated
receipts=[]
for label in ['build','inspection','inspection_02']:
 folder=S/'metadata_runs'/label;r=read(folder/'EXECUTION.json');launch=read(folder/'LAUNCH.json')
 assert all(r[k]==v for k,v in launch.items()) and r['exit_code']==0 and not r['timed_out']
 assert r['argv'][2]==r['child_source_at_launch']['path'] and r['child_source_at_launch']['path']!=r['original_source_at_launch']['path']
 assert r['child_source_at_launch']['sha256']==r['original_source_at_launch']['sha256'] and r['inputs_unchanged_after_run'] is True
 assert r['started_utc']<=r['finished_utc'] and r['scientific_programs_run']==0
 for k in ['child_source_at_launch','recorder_at_launch','input_identities_at_launch','stdout','stderr']:same(r[k]['path'],r[k])
 assert Path(r['stderr']['path']).read_bytes()==b'';receipts.append(pin(folder/'EXECUTION.json'))
v=read(S/'VERIFICATION.json');assert v==read(S/'metadata_runs/inspection_02/stdout')
assert len(v['scoped_metadata_mutants'])==6 and all(r['rejected'] for r in v['scoped_metadata_mutants']) and v['mathematics_tested_by_this_execution'] is False
seal=read(S/'metadata_runs/seal/EXECUTION.json');assert seal['exit_code']==0
for k in ['source_at_launch','stdout','stderr']:same(seal[k]['path'],seal[k])
assert (S/'SEAL_STDOUT.txt').read_bytes()==(S/'SEAL_STDERR.txt').read_bytes()==b''
for path in sorted((S/'metadata_runs/seal').glob('authority_*/EXECUTION.json')):
 r=read(path);assert r['exit_code']==0
 for k in ['stdout','stderr']:same(r[k]['path'],r[k])
assert read(P/PK/'PARENT_BINDING.json')['canonical_binding_complete'] is False
assert all(v is None for k,v in read(P/PK/'PUBLICATION_STATE.json').items() if k not in ['scientific_programs_run_this_draft','scientific_replays'])
O.mkdir(exist_ok=False)
text='''# Root source publication review

The complete new wrapper, proposed PR body, binding contract and five metadata programs were read. The generated primary is exactly its template with six body identities and the declared manifest expanded. All193 frozen members and288 original source aliases/126 unique recovery objects match. Six complete proof/review/qualification bodies retain their earlier qualified review at identical bytes. No scientific source or finite discriminator was replayed here.

This source package is approved for separate canonical integration. The fixed-word result remains conditional on a literal noninteracting old generator with supplied positive gaps, matched reservoir branches, degree-three comb, full within-species SWAP, cross-species diagonal control, independent readiness and calibrated timing. Complete product-charge-block semantics and word-dependent off-code behavior are distinct. Ideal packet error is word-independent; actual implementation errors telescope with retained correlated ancillas. The added static contribution is included separately from the driven g/2 cap.

The uniform logical bound R(q), scalar/determinant and routing-return corrections, computable finite-error search, target W=VE* and full preparation aging support fixed-q nominal laboratory O(epsilon^-4) runtime. Classical compiler time and native supply are excluded. Runtime phase-generator allowance O(epsilon^5) is distinct from cancellation-input precision O(epsilon^9). Initial/final old-energy errors, complete resource/ancilla moments, scalar reserves and actuator-state limitations are preserved. The separate direct candidate is still a proposal; interacting-old-H, autonomous halt and indefinite reuse remain outside this theorem.

Three actual packaging runs exited0. The first mutation called altered_original_body appended to the note; its name and independent_interval_comparison wording were too strong. A distinct inspected correction flips a byte inside the declared original interval and says direct_original_interval_comparison. Both exact source captures and streams remain. These are source-integrity controls, not scientific replication. The sealer's internal completion record precedes its final writes; the complete produced freeze and actual delivered packet were checked here, without treating self-report as independent execution evidence.

The two historical exact finite scientific runs and the sparse parent's pre-execution launcher failure remain bounded evidence. The original two root acceptances are actual captured metadata decisions, not retained audits. Parent6db93809 is bound; the sparse canonical parent, current base, actual canonical review/primary and PR remain pending. The source primary refuses canonical use unconditionally. No audit verdict, science merge, main push or editable prompt change is approved by this review.
'''
with (O/'REVIEW.md').open('x') as f:f.write(text)
r=dict(kind='root_qualified_source_publication_review',utc=datetime.now(timezone.utc).isoformat(),root_read_complete=True,disposition='QUALIFIED_SOURCE_INTEGRATION_APPROVED_CANONICAL_CHECKS_PENDING',source_freeze=pin(S/'FREEZE.json'),source_note=pin(P/NOTE),source_validator=pin(P/H),source_manifest=pin(P/PK/'SOURCE_MANIFEST.json'),source_wrapper=pin(S/'packet_text/WRAPPER.md'),review=pin(O/'REVIEW.md'),immutable_bodies=6,source_aliases=288,archive_objects=126,metadata_receipts=receipts,scientific_executions=0,actual_canonical_acceptance=None,actual_publication=None,retained_audit=False,editable_prompt_files_changed=[])
write(O/'REVIEW.json',r)
write(O/'FREEZE.json',dict(members=[dict(path=p.name,bytes=pin(p)['bytes'],sha256=pin(p)['sha256']) for p in [O/'REVIEW.md',O/'REVIEW.json']],retained_audit=False))
print(json.dumps(dict(review=pin(O/'REVIEW.json'),freeze=pin(O/'FREEZE.json'),source_freeze=pin(S/'FREEZE.json'),scientific_executions=0),indent=2))
