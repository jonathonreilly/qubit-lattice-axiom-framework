from pathlib import Path
import hashlib, json
from datetime import datetime, timezone

N=Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023')
D=N/'positive_bias_publication_draft'
R=N/'root_positive_bias_publication_review'
P=D/'proposal'
Q=P/'.claude/science/physics-loops/toe-positive-bias-suppliers-20261016'
def read(p): return json.loads(p.read_text())
def pin(p):
 b=p.read_bytes(); return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def same(p,row):
 a=pin(p); assert (a['bytes'],a['sha256'])==(row['bytes'],row['sha256']),str(p)
freeze=read(D/'FINAL_FREEZE.json')
assert pin(D/'FINAL_FREEZE.json')['sha256']=='8b8c172a101b5cf35a4f542b55d7c5c3249da99dd78a896078805518dfe12d53'
for row in freeze['files']: same(D/row['path'],row)
manifest=read(Q/'INPUT_MANIFEST.json')
for row in manifest['inputs']: same(P/row['path'],row)
bodies=read(Q/'BODY_MAP.json')['bodies']
note=P/'docs/POSITIVE_BIAS_SUPPLIERS_BOUNDED_THEOREM_NOTE_2026-10-16.md'
raw=note.read_bytes(); assert raw.startswith((D/'wrapper.md').read_bytes())
sources=read(Q/'SOURCE_MANIFEST.json')['sources']
for row in sources:
 same(Path(row['source']),row)
 rec=row['recovery']
 if rec['kind']=='blob': same(P/rec['path'],row)
 else:
  b=raw[rec['start_byte_inclusive']:rec['end_byte_exclusive']]
  assert len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256'] and raw.count(b)==1
for row in bodies:
 b=raw[row['start_byte_inclusive']:row['end_byte_exclusive']]
 assert len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256'] and raw.count(b)==1
parent=read(Q/'PARENT_BINDING.json')
assert len(parent['direct_mathematical_parents'])==1
for row in parent['direct_mathematical_parents']: same(N.parent/'correlation_worktree'/row['path'],row)
acceptances={row['role']:row['sha256'] for row in sources if row['role'] in ['transfer_acceptance','edge_acceptance','chain_acceptance','box_acceptance']}
assert len(acceptances)==4
substitutions={'__EXPECTED_ACCEPTANCES__':repr(acceptances),'__EXPECTED_BODIES__':repr({row['name']:row['sha256'] for row in bodies}),'__EXPECTED_PARENT__':repr(parent['direct_mathematical_parents'][0]),'__INPUT_MANIFEST_SHA256__':pin(Q/'INPUT_MANIFEST.json')['sha256'],'__AUDIT_INPUT_PATHS__':repr(sorted([row['path'] for row in manifest['inputs']]+[str((Q/'INPUT_MANIFEST.json').relative_to(P))]))}
template=(D/'primary_template.py').read_text()
for key,value in substitutions.items(): template=template.replace(key,value)
primary=P/'scripts/positive_bias_suppliers_2026_10_16.py'
assert template==primary.read_text()
receipts=[]
for root in sorted((D/'metadata_runs').iterdir()):
 launch,run=read(root/'LAUNCH.json'),read(root/'EXECUTION.json')
 assert all(run[k]==v for k,v in launch.items())
 assert run['exit_code']==(1 if root.name=='default_refusal_01' else 0) and not run['timed_out']
 for k in ['source_at_launch','source_capture','source_after_execution','recorder','stdout','stderr']: same(Path(run[k]['path']),run[k])
 receipts.append(pin(root/'EXECUTION.json'))
controls=read(D/'metadata_runs/controls_01/stdout')['controls']
assert len(controls)==7 and all(x['detected'] for x in controls)
original_members=0
for row in read(Q/'FREEZE_VERIFICATION.json')['freezes']:
 p=Path(row['path']); assert pin(p)['sha256']==row['sha256']; f=read(p)
 members=next(f[k] for k in ['members','files','artifacts'] if k in f)
 assert len(members)==row['verified_members']
 for member in members:
  q=Path(member['path']); same(q if q.is_absolute() else p.parent/q,member)
 original_members+=len(members)
coverage='''# Root publication content review\n\nRead the complete new 168-line wrapper, all four packet prose files, primary template, builder, recorder, inspector and direct sealer. A first oversized aggregate truncated; relevant beginning/guide and remaining code were reread completely. The rest of the wrapper was visible completely and the beginning was repaired separately. Verified generated primary exactly substitutes five literal pin collections; no unseen new function is inferred from an older approval. Read all five actual metadata-run streams, actual command/cwd/timing/status fields, and verified launch/receipt/captured source/recorder identities. The default refusal exit1 is expected and preserved. No science executable was replayed.\n\nReused the previously completely read qualified transfer, positive chain, explicit edge and padding source arguments and independent-check evidence at their unchanged identities, controlled by8353563c,38253192,440ae5bf and89eec7c0. Nine exact body intervals and eight original freeze closures are verified, including narrow onsite appendix and four final qualifications. Root's original scientific-read records remain controlling; archive hashing is not a new independent scientific review.\n\nThe wrapper preserves full computable data, positive occupied-site/edge access, no cancellation of literal H, scalar/reserve ledger, target-uniform bounds before actual T, rational target afterward, both old time flows and all outputs, fixed path before accuracy, leading-Gram witness without p(1)>0, actual corner/exterior permissions and correlated fillers. Nonidle decoupled filler drift changes the full comparator. The sole mathematical parent is the exact qualified bus, whose complete finite construction supplies the imported theorem. Git stack ancestry creates no extra mathematical parent.\n\nThe static-bias no-go submission remains FAIL/partial-narrowing; this positive conditional theorem uses narrow supporting implication failures, not broad architecture impossibility or exhausted alternatives. Same-model/source-exposed checking limits, failed structural-equality diagnostics and historical pending-chain statement are unchanged. Native sources, actual release/isolation/timing, measured-energy identity, records and reset remain open. No favorable runtime or uniform changing-plant cap follows.\n\nAccept source-only packaging for separate canonical integration. Normal draft invocation rightly refuses certification. Canonical current-base and root/canonical review guards must be independently bound to real captured records before success, and reviewed changed code/header/offsets require actual checks. No publication or retained audit is inferred.\n'''
assert not (R/'READ_COVERAGE.md').exists()
(R/'READ_COVERAGE.md').write_text(coverage)
result={'kind':'root_source_publication_review','utc':datetime.now(timezone.utc).isoformat(),'root_read_complete':True,'source_draft_freeze':pin(D/'FINAL_FREEZE.json'),'note':pin(note),'primary':pin(primary),'body_pins':bodies,'parent_binding':parent,'source_acceptances':[pin(Path(row['source'])) for row in sources if row['role'] in acceptances],'read_coverage':pin(R/'READ_COVERAGE.md'),'verified_freeze_members':len(freeze['files']),'verified_original_members':original_members,'source_records':len(sources),'metadata_receipts':receipts,'decision':'Accept reviewed source-preserving positive conditional theorem package for separate root integration; canonical binding remains pending.','static_bias_no_go_submission':'FAIL/partial-narrowing','scientific_programs_run_this_review':0,'historical_programs_replayed':0,'canonical_primary_runs':0,'limits':['New source-only code checks identity, not mathematics.','No blind replication, native device supplier, measured energy or retained audit.','Actual Git base and canonical changed content remain to be reviewed and bound.'],'editable_prompt_files_changed':[]}
assert not (R/'REVIEW.json').exists()
(R/'REVIEW.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'review':pin(R/'REVIEW.json'),'freeze_members':len(freeze['files']),'original_members':original_members,'body_count':len(bodies),'canonical_binding':None},indent=2))
