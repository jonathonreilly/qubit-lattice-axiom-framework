from pathlib import Path
import json,hashlib
r=Path('/private/tmp/toe-autonomous-resource-density-20260930');o=Path(__file__).parent
p=r/'.claude/science/physics-loops/autonomous-resource-density-20260930'
a=json.loads((p/'PREFLIGHT_RECORD_CORRECTED_BEFORE_PRIMARY.json').read_text());f=json.loads((o/'FINAL_CONFIRMATION.json').read_text())
def ref(p):return {'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
a['unit_id']='autonomous-resource-density-source-only-final-c393428136'
a['source']={'base':f['base'],'commit':f['head'],'tree':f['tree'],'deleted_paths':[],'paths':[{'path':x['final_path'],'sha256':x['final_sha256']} for x in f['final_dispositions']]}
a['constituents']=[{'id':'autonomous-resource-density-c393428136','head':f['head'],'delta_base':f['base'],'dispositions':dict(ref(o/'FINAL_CONFIRMATION.json'),json_pointer='/final_dispositions')}]
a['reviewer']={'session':f['reviewer_session'],'report':ref(o/'REVIEW.md'),'references':[ref(o/x) for x in ['FINAL_CONFIRMATION.json','frozen_inventory.json','archive_verification.json','authority_identities.json']]}
existing={x['path'] for x in a['inputs']['context']}
for path,h in json.loads((o/'authority_identities.json').read_text()).items():
 if path not in existing:a['inputs']['context'].append({'path':path,'sha256':h})
for cat in a['inputs'].values():
 for row in cat: assert hashlib.sha256((r/row['path']).read_bytes()).hexdigest()==row['sha256']
# This graph discovers docs Markdown, not the provenance pack; no current proof
# is declared non-scientific or exempted by directory.
a['non_science_notes']=[]
(o/'unit-v2.json').write_text(json.dumps(a,indent=2)+'\n')
print(hashlib.sha256((o/'unit-v2.json').read_bytes()).hexdigest())
