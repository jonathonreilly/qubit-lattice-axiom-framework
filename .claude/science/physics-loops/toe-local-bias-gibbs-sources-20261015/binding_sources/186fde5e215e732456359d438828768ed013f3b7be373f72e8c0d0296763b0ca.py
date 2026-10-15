from pathlib import Path
import ast,datetime,hashlib,json,difflib
N=Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261014_214309');O=N/'local_bias_integration_proposal';S=N/'local_bias_publication_draft';D=N/'publication_integration/local_bias';D.mkdir(exist_ok=True)
def digest(b):return hashlib.sha256(b).hexdigest()
def pin(p):
 p=Path(p);b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':digest(b)}
def read(p):return json.loads(Path(p).read_text())
def same(p,row):
 a=pin(p);assert all(a[k]==row[k] for k in ('bytes','sha256')),str(p)
def funcs(p):
 s=Path(p).read_text();return {n.name:ast.get_source_segment(s,n) for n in ast.parse(s).body if isinstance(n,ast.FunctionDef)}
assert pin(O/'FINAL_FREEZE.json')['sha256']=='6dcdcf650900c3901905ffb23b0175b1bc8d390f78db223cd2d0960c8b7d9c0d'
f=read(O/'FINAL_FREEZE.json');assert len(f['files'])==156
for r in f['files']:same(O/r['path'],r)
assert {str(p.relative_to(O)) for p in O.rglob('*') if p.is_file()}=={r['path'] for r in f['files']}|set(f['excluded_exact_root_paths'])
for r in read(O/'SOURCE_PINS.json')['sources']:same(r['path'],r)
old=funcs(O/'reference/correlated_common.py');new=funcs(O/'local_bias_common.py');templates=funcs(O/'templates/new_functions.py')
changed={k for k in old if old[k]!=new[k]};assert changed=={'run','parent_query','prepare','verify','finish','publish','main'}
assert len([k for k in old if old[k]==new[k]])==21 and set(new)-set(old)=={'require_bound_base'}
for k in templates:assert templates[k]==new[k]
packet='.claude/science/physics-loops/toe-local-bias-gibbs-sources-20261015';helper='scripts/local_conditional_bias_and_rotated_gibbs_2026_10_15.py'
pf=funcs(O/'proposed_primary_unbound.py');oldpf=funcs(S/'proposal'/helper)
assert {k for k in pf if pf[k]!=oldpf[k]}=={'main'} and len(pf)==9
before=(S/'proposal'/helper).read_text();after=(O/'proposed_primary_unbound.py').read_text()
diff=''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='frozen_source/'+helper,tofile='proposed/'+helper,n=1))
assert diff==(O/'PRIMARY_BINDING.diff').read_text()
# Recovery selection lists historical membership/status, not relocated note offsets.
selection=read(S/'proposal'/packet/'RECOVERY_SELECTION.json')
assert 'start_byte_inclusive' not in json.dumps(selection)
for name in ('assemble_metadata.py','validate_metadata.py'):
 receipt=read(O/'DELIVERY.json')['final_actual_metadata_receipts'][name];same(receipt['path'],receipt);r=read(receipt['path']);assert r['exit_code']==0
 same(O/name,r['child_source_at_launch'])
 for key in ('stdout','stderr'):same(r[key]['path'],r[key])
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'proposal_freeze':pin(O/'FINAL_FREEZE.json'),'members_verified':156,'source_pins_verified':len(read(O/'SOURCE_PINS.json')['sources']),'common':pin(O/'local_bias_common.py'),'primary_preview':pin(O/'proposed_primary_unbound.py'),'root_read_scope':'Complete seven changed common functions and new require_bound_base; complete preamble, primary binding diff, wrapper and packet changes, integration sections, body/handoff templates, assembly/inspection/recorder/sealer. Twenty-one prior common functions and eight prior primary helpers reused at exact identity. Template functions checked exact to reviewed common. Earlier full scientific source/wrapper review 0cada325 remains valid. Preliminary large combined tool display was truncated; all affected packet and handoff text reread in bounded complete calls.','source_review':pin(N/'local_bias_root_publication_review/ROOT_REVIEW.json'),'decision':'Proceed with exact prepare, then inspect actual canonicalization before installation. No scientific or native-supply conclusion from packaging.','science_runs':0,'editable_prompt_files_changed':[]}
(D/'ROOT_INTEGRATION_SOURCE_REVIEW.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'review':pin(D/'ROOT_INTEGRATION_SOURCE_REVIEW.json')}))
