"""Read-only exact-Git source capture for one bounded preparation route."""
from pathlib import Path
import hashlib,json,subprocess
from datetime import datetime,timezone
D=Path(__file__).resolve().parent
W=D.parent.parent/'correlation_worktree'
COMMIT='0e3993770a7a2dd872018f9dd3c76c2d9a624db9'
sources={
 'family.md':'docs/EMITTER_COUPLING_FAMILY_BOUNDED_THEOREM_NOTE_2026-10-17.md',
 'product_seed.md':'docs/PRODUCT_SEED_EMITTER_BOUNDED_THEOREM_NOTE_2026-10-17.md',
 'two_body.md':'docs/TWO_BODY_AUTONOMOUS_HALT_BOUNDED_THEOREM_NOTE_2026-10-17.md',
 'local_gibbs.md':'docs/LOCAL_GIBBS_CONTROLLER_SOURCE_BOUNDED_THEOREM_NOTE_2026-10-15.md',
 'controlled_stop.md':'docs/PRODUCT_SOURCE_CONTROLLED_STOP_BOUNDED_THEOREM_NOTE_2026-10-16.md',
 'local_bias.md':'docs/LOCAL_CONDITIONAL_BIAS_AND_ROTATED_GIBBS_BOUNDED_THEOREM_NOTE_2026-10-15.md',
 'parameters.json':'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_certificate/inputs/two_body_interval_bridge__CERTIFICATE.json',
 'workflow.md':'docs/ai_methodology/SCIENCE_WORKFLOW.md',
 'physics_loop.md':'docs/ai_methodology/skills/physics-loop/SKILL.md',
 'discovery.md':'docs/ai_methodology/skills/physics-loop/references/DISCOVERY.md',
 'claim_status.md':'docs/ai_methodology/skills/physics-loop/references/CLAIM_STATUS.md',
 'delivery.md':'docs/ai_methodology/skills/physics-loop/references/DELIVERY.md'}
(D/'inputs').mkdir(exist_ok=True)
rows=[]
for name,rel in sources.items():
 raw=subprocess.check_output(['git','show',COMMIT+':'+rel],cwd=W)
 p=D/'inputs'/name
 with p.open('xb') as f:f.write(raw)
 rows.append({'snapshot':'inputs/'+name,'repository_path':rel,'commit':COMMIT,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'worktree_same_at_capture':(W/rel).read_bytes()==raw})
assert next(r for r in rows if r['snapshot']=='inputs/family.md')['sha256']=='f3a10874f4f52bef0bc5c393081590aff2f71b877a0f44cac9a3cbe05b34da87'
raw=(D/'inputs/family.md').read_bytes(); a=b'<!-- BEGIN UNCHANGED FAMILY AUTHOR BODY -->\n'; b=b'\n<!-- END UNCHANGED FAMILY AUTHOR BODY -->'
body=raw.split(a,1)[1].split(b,1)[0]
assert hashlib.sha256(body).hexdigest()=='9bcf538e7efb2285e1e9e8b67da8c3f29a308b0baa9004eec1dd4787393fa9ac'
record={'captured_utc':datetime.now(timezone.utc).isoformat(),'source_commit':COMMIT,'sources':rows,'inherited_family_body_sha256':hashlib.sha256(body).hexdigest(),'scope':'Complete exact source snapshots; reading coverage is separately stated. No live-source status inferred from historical embedded labels.'}
(D/'SOURCE_MAP.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'sources':len(rows),'all_worktree_copies_match':all(r['worktree_same_at_capture'] for r in rows),'family_body_sha256':record['inherited_family_body_sha256']},indent=2))
