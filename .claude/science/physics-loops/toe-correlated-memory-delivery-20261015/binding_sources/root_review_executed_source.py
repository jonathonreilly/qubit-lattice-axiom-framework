"""Root source-publication identity checks and actual reading decision; no science execution."""
from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json,subprocess
N=Path(__file__).resolve().parents[1];D=N/'correlated_memory_publication_draft';W=N.parent/'correlation_worktree';O=D/'proposal';R=N/'correlated_memory_root_publication_review'
PACK='.claude/science/physics-loops/toe-correlated-memory-delivery-20261015';NOTE='docs/CORRELATED_MEMORY_DELIVERY_AND_READINESS_BOUNDED_THEOREM_NOTE_2026-10-15.md';PRIMARY='scripts/correlated_memory_delivery_and_readiness_2026_10_15.py'
def read(p):return json.loads(p.read_bytes())
def pin(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def verify(p,row):
 v=pin(p);assert (v['bytes'],v['sha256'])==(row['bytes'],row['sha256']),str(p)
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
assert pin(D/'FINAL_FREEZE.json')['sha256']=='6ab1df30d82b0ee7abb39c2da9739a2d9745e120e565e55355838ab841e7f003'
freeze=read(D/'FINAL_FREEZE.json')
for row in freeze['files']:verify(D/row['path'],row)
assert len(freeze['files'])==179
for row in read(D/'SOURCE_FRESHNESS.json')['identities']:verify(Path(row['original']),row)
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=W,text=True).strip()=='1ac15c4a9116d14a7f1e9eec971aea7b0e750360'
assert subprocess.check_output(['git','status','--porcelain'],cwd=W,text=True).strip()==''
bodymap=read(O/PACK/'BODY_MAP.json');note=(O/NOTE).read_bytes();assert pin(O/NOTE)['sha256']=='5d812f813a8d5f6b43e3c6911b2fc58dc943a2145869e14786a0d69ec928be90'
for row in bodymap['bodies']:
 b=note[row['start_byte_inclusive']:row['end_byte_exclusive']];assert len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256'] and note.count(b)==1
parents=read(O/PACK/'DEPENDENCIES.json')['dependencies']
for row in parents:
 verify(W/row['path'],row);r=row['accepted_body_interval'];b=(W/r['container']).read_bytes()[r['start_byte_inclusive']:r['end_byte_exclusive']];assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256']
sources=read(O/PACK/'SOURCE_MANIFEST.json')['sources']
for row in sources:
 r=row['recovery']
 if r['kind']=='blob':b=(O/r['path']).read_bytes()
 elif r['kind']=='external_pinned':b=(W/r['path']).read_bytes()
 else:
  p=O/r['container'];p=p if p.exists() else W/r['container'];b=p.read_bytes()[r['start_byte_inclusive']:r['end_byte_exclusive']]
 assert len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256']
for row in read(O/PACK/'INPUT_MANIFEST.json')['inputs']:verify(O/row['path'],row)
parsed=ast.parse((O/PRIMARY).read_text());literals={n.targets[0].id:ast.literal_eval(n.value) for n in parsed.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id in {'AUDIT_INPUT_PATHS','MANIFEST_SHA256','EXPECTED_BODIES','AUDIT_TIMEOUT_SEC'}}
expected={r['path'] for r in read(O/PACK/'INPUT_MANIFEST.json')['inputs']}|{PACK+'/INPUT_MANIFEST.json',PACK+'/ACTUAL_BINDING.json'}|{r['path'] for r in parents};assert set(literals['AUDIT_INPUT_PATHS'])==expected and literals['AUDIT_TIMEOUT_SEC']==60
assert literals['MANIFEST_SHA256']==pin(O/PACK/'INPUT_MANIFEST.json')['sha256'];assert literals['EXPECTED_BODIES']=={r['name']:r['sha256'] for r in bodymap['bodies']}
receipts=[]
for label in ['build','inspection']:
 p=D/'metadata_runs'/label/'EXECUTION.json';r=read(p);assert r['exit_code']==0 and r['scientific_execution'] is False
 for key in ['child_source_at_launch','stdout','stderr','recorder']:verify(Path(r[key]['path']),r[key])
 assert r['stderr']['bytes']==0
 receipts.append({'label':label,'receipt':pin(p),'actual_start_utc':r['start_utc'],'actual_end_utc':r['end_utc'],'actual_exit_code':r['exit_code']})
R.mkdir(exist_ok=False)
result={'kind':'root_source_publication_review','reviewed_utc':datetime.now(timezone.utc).isoformat(),'root_read_complete':True,'source_draft_freeze':pin(D/'FINAL_FREEZE.json'),'note':pin(O/NOTE),'primary':pin(O/PRIMARY),'wrapper':pin(D/'wrapper.md'),'current_reading':'Complete 27,691-byte wrapper; entire primary template and structural literal/input expansion; complete build/record/inspect/seal programs; all seven packet Markdown files; outer handoff, coverage, read guide, delivery and actual two metadata receipts. Seven exact mathematical bodies and necessary accepted parent arguments reused from prior complete readings at unchanged identities.','sealed_members_verified':len(freeze['files']),'body_pins':bodymap['bodies'],'source_rows_verified':len(sources),'parents':parents,'metadata_receipts':receipts,'existing_source_acceptances':{'markov':pin(N/'correlated_memory_root_review/MARKOV_ACCEPTANCE.md'),'gibbs':pin(N/'correlated_memory_root_review/GIBBS_ACCEPTANCE.md'),'composition':pin(N/'gibbs_markov_composition_root_review/ACCEPTANCE.md')},'decision':'Publication interpretation accepted at existing conditional source scope; actual checkout binding and integration remain pending.','mandatory_interpretations':['Exact actual-marginal lemma and fixed ideal H0-aged readiness target are distinct; full-space turn-on pays the difference.','Preserve seven complete source bodies; accepted source statements do not imply independent retained audit.','Q is entrywise positive, not necessarily PSD; nonincreasing 0<=u<=1 switch, separately supplied diagonal channels and actual physical consumer duration are necessary.','Gibbs composition retains all records, full correlation phases, chronological K_Z then H0 aging, global diagonal calibration floor and distinct initial/final memory Hamiltonians.','Two canonical mathematical parents are joint readiness and finite memory resources; PR9609 is only Git ancestry.','No new local-bias or rotated-Gibbs candidate belongs to this milestone.'],'integration_requirement':'Create actual binding with present source/receipt identities; regenerate all affected body intervals, source recovery offsets, manifest and literal declarations after current framing changes; retain historical null publication state. Inspect every changed integration argument/code before execution.','scope':'Source integrity and publication reading only; no new independent mathematical replication or retained verdict.','scientific_programs_run':0,'primary_runs':0,'historical_programs_replayed':0,'editable_prompt_files_changed':[],'actual_binding':None,'verification_limits':['Actual primary/cache/mutations/graph and source integration pending','Current-main cumulative-stack landing and strict full pipeline open','Independent retained audit open','Native source/controller, full program, energy/detector and reuse remain open']}
save(R/'ROOT_REVIEW.json',result)
save(R/'FINAL_FREEZE.json',{'frozen_utc':datetime.now(timezone.utc).isoformat(),'files':[pin(R/'ROOT_REVIEW.json')],'scope':'Root publication interpretation only'})
print(json.dumps({'review':pin(R/'ROOT_REVIEW.json'),'freeze':pin(R/'FINAL_FREEZE.json'),'members_verified':len(freeze['files']),'source_rows_verified':len(sources),'science_executions':0}))
