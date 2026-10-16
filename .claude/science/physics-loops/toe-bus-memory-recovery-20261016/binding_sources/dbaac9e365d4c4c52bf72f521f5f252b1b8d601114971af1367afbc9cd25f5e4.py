"""Actual root canonical-source review, preserving prior scientific qualifications."""
from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json,subprocess,difflib
N=Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023')
W=N.parent/'correlation_worktree';D=N/'publication_integration/bus_memory_recovery';I=N/'bus_memory_recovery_integration_refresh'
S=N/'bus_memory_recovery_publication_draft/proposal';P='.claude/science/physics-loops/toe-bus-memory-recovery-20261016'
NOTE='docs/BUS_MEMORY_RECOVERY_BOUNDED_THEOREM_NOTE_2026-10-16.md';HELPER='scripts/bus_memory_recovery_2026_10_16.py'
def pin(p):
 p=Path(p);b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def rd(p):return json.loads(Path(p).read_text())
def same(p,r):
 z=pin(p);assert z['bytes']==r['bytes'] and z['sha256']==r['sha256'],p
def write(p,v):assert not p.exists(),p;p.write_text(json.dumps(v,indent=2,sort_keys=True)+'\n')
prep=rd(D/'PREPARED.json');assert prep['base_head']=='9f2c922307afc1354e75b2da0dc9a8ce0ac2b3bd'
assert subprocess.check_output(['git','-C',str(W),'rev-parse','HEAD'],text=True).strip()==prep['base_head']
assert subprocess.check_output(['git','-C',str(W),'branch','--show-current'],text=True).strip()=='physics-loop/toe-bus-memory-recovery-20261016'
assert not subprocess.check_output(['git','-C',str(W),'diff','--name-only']) and not subprocess.check_output(['git','-C',str(W),'diff','--cached','--name-only'])
diff='';unchanged=[];copies=[];changed=[]
for name,row in sorted(prep['canonical_files'].items()):
 same(W/name,row);assert (W/name).read_bytes()==(D/'canonical_source'/name).read_bytes()
 old=(S/name).read_bytes() if (S/name).exists() else b'';new=(W/name).read_bytes()
 if old==new:unchanged.append(name)
 else:
  changed.append(name);diff+=''.join(difflib.unified_diff(old.decode().splitlines(True),new.decode().splitlines(True),fromfile='draft/'+name,tofile='canonical/'+name))
  if '/binding_sources/' in name:assert hashlib.sha256(new).hexdigest()==Path(name).stem;copies.append(name)
assert diff==(D/'CANONICALIZATION.diff').read_text() and pin(D/'CANONICALIZATION.diff')['sha256']=='71fea03af2ea0248c8f4c9980b00260a46457712750afe9c0d12219e11853411'
assert len(unchanged)==124 and len(copies)==28
assert set(changed)-set(copies)=={P+'/'+x for x in ['ACTUAL_BINDING.json','ACTUAL_REFRESH_PROVENANCE.json','BODY_MAP.json','CANONICAL_BINDING.json','INPUT_MANIFEST.json','PR_TITLE.txt']}|{NOTE,HELPER}
note=(W/NOTE).read_bytes();body=rd(W/P/'BODY_MAP.json')['bodies']
for row in body:
 raw=note[row['start_byte']:row['end_byte_exclusive']];assert raw==Path(row['original']).read_bytes() and len(raw)==row['bytes'] and hashlib.sha256(raw).hexdigest()==row['sha256']
assert len(body)==5
parents=rd(W/P/'PARENT_BINDING.json')
for row in parents['direct_canonical_parents']:same(W/row['path'],row)
assert parents['git_base'] is None
for name in ['PARENT_BINDING.json','PUBLICATION_STATE.json','ACTUAL_EVIDENCE.json','SOURCE_MANIFEST.json']:assert (W/P/name).read_bytes()==(S/P/name).read_bytes()
def funcs(p):
 s=p.read_text();return {x.name:ast.get_source_segment(s,x) for x in ast.parse(s).body if isinstance(x,ast.FunctionDef)}
def vals(p):return {x.targets[0].id:ast.literal_eval(x.value) for x in ast.parse(p.read_text()).body if isinstance(x,ast.Assign)}
assert funcs(W/HELPER)==funcs(I/'proposed_primary_unbound.py')
a=vals(I/'proposed_primary_unbound.py');b=vals(W/HELPER)
assert {k for k in a if a[k]!=b[k]}=={'MANIFEST_SHA256','AUDIT_INPUT_PATHS'}
manifest=rd(W/P/'INPUT_MANIFEST.json')
assert b['MANIFEST_SHA256']==pin(W/P/'INPUT_MANIFEST.json')['sha256']
for row in manifest['inputs']:same(W/row['path'],row)
assert set(b['AUDIT_INPUT_PATHS'])=={r['path'] for r in manifest['inputs']}|{P+'/INPUT_MANIFEST.json'}
actual=rd(W/P/'ACTUAL_BINDING.json');assert actual['canonical_review_evidence'] is None and not actual['root_read_complete']
assert actual['raw_bodies']==body and actual['parent_binding']==parents and actual['git_base']==prep['base_head']
for p in [D/'actions/prepare/EXECUTION.json',D/'actions/install/EXECUTION.json']:
 x=rd(p);assert x['exit_code']==0
 for key in ['launch','stdout','stderr']:same(x[key]['path'],x[key])
 assert Path(x['stderr']['path']).read_bytes()==b''
r=dict(kind='root_canonical_source_review',utc=datetime.now(timezone.utc).isoformat(),root_read_complete=True,
 git_base=prep['base_head'],bound_note_sha256=pin(W/NOTE)['sha256'],canonical_body_pins=body,parent_binding=parents,
 source_draft_freeze_sha256='5f680ad2dcd99182bd6e023e879963c8c23b6b22d8b737045c1ab50ad91c5e49',
 source_draft_review_sha256='03e1053a510f8c8df4847142e201f81c58f8e71f5bb2363b96df312cbe84f2e1',
 prebinding_primary=pin(W/HELPER),integration_common=pin(I/'bus_memory_recovery_common.py'),
 integration_source_review=pin(D/'ROOT_INTEGRATION_SOURCE_REVIEW.json'),reviewed_diff=pin(D/'CANONICALIZATION.diff'),
 root_binding=pin(D/'ROOT_BINDING_INPUT.json'),prepared=pin(D/'PREPARED.json'),
 inspection=dict(unchanged_source_files=124,content_addressed_bindings=28,new_noncopy_paths=sorted(set(changed)-set(copies)),
 primary_functions_exact_reused=9,declared_inputs=len(manifest['inputs']),source_nulls_preserved=True),
 scientific_scope=[
 'Qualified conditional endpoint recovery only. Five-stage opposite-axis and full-inverse triple-area schedules remain separate, with their own duration/scalar/error ledgers.',
 'Supplied positive complement range through coefficient two, matching, full SWAP/inverse access, calibration, readiness and phase/isolation remain explicit.',
 'Literal old H, full A2 and all D/C/E/R correlations/reserves remain; zero-area old-port error is still charged.',
 'Finite repeated use counts initial readiness once and all interval errors. Endpoint recovery is not autonomous halt or indefinite reset/reuse.',
 'Two exact mathematical parents only; resource Git ancestry adds no resource theorem or shrinking-bias recovery result.'],
 review_method='Full changed wrapper/metadata fields read; every unchanged scientific body and argument reused only after exact original/installed-byte identity. Complete changed implementation read in integration source review; all nine installed functions exact.',
 current_status='Canonical source accepted for scoped provenance execution and separate staged publication review; conditional-support, not retained audit',
 scientific_programs_run=0,retained_audit=False,editable_prompt_files_changed=[],
 limits=['Source-exposed analytical checks do not become blind or independent audit through packaging. No mathematical program rerun.',
 'Metadata/provenance guards establish identities and action history, not validity of physical suppliers or native realization.',
 'Current main refresh screen preserved separately; cumulative main landing integration remains outside this stacked PR.'])
failed=N/'runs/bus_memory_recovery_canonical_review'
frec=rd(failed/'EXECUTION.json');assert frec['exit_code']==1
for key in ['source_capture','stdout','stderr']:same(frec[key]['path'],frec[key])
r['preserved_failed_review_attempt']={'explanation':'The first recorder completed its identity checks but refused to overwrite the install-phase diff acknowledgement at ROOT_CANONICAL_REVIEW.json. It wrote no review. This separate recovery uses a distinct filename; failed attempt remains unchanged.','receipt':frec,'captured_source':(failed/'executed_source.py').read_text(),'stdout':(failed/'stdout').read_text(),'stderr':(failed/'stderr').read_text(),'recorder_source':(N/'review_run.py').read_text(),'existing_diff_acknowledgement':rd(D/'ROOT_CANONICAL_REVIEW.json')}
write(D/'ACTUAL_ROOT_CANONICAL_REVIEW.json',r)
print(json.dumps(dict(review=pin(D/'ACTUAL_ROOT_CANONICAL_REVIEW.json'),installed_note=pin(W/NOTE),prebinding_primary=pin(W/HELPER),scientific_programs_run=0),indent=2))

