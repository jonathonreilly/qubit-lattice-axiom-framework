from pathlib import Path
import json,hashlib,datetime
root=Path('.')
author=root.parent
manifest=json.loads((author/'BIRTH_BACKACTION_AUTHOR_PRECOMPARISON_SEAL.json').read_text())
source_rows=list(manifest['artifacts'])
p=author/'BIRTH_BACKACTION_AUTHOR_PRECOMPARISON_SEAL.json';b=p.read_bytes()
source_rows.append({'path':str(p.resolve()),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
for row in source_rows:
 p=Path(row['path']);b=p.read_bytes();assert len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256']
pre=json.loads((root/'PRE_COMPARISON_SEAL.json').read_text())
for row in pre['artifacts']:
 p=Path(row['path']);b=p.read_bytes();assert len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256']
rows=[]
for p in sorted(root.rglob('*')):
 if not p.is_file() or p.name in {'CHECKPOINT.md','FINAL_COMPARISON_SEAL.json'} or '__pycache__' in p.parts:continue
 b=p.read_bytes();rows.append({'path':str(p.resolve()),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
seal={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'completed bounded post-seal source comparison; F1 remains open in reviewed bytes','findings':[{'id':'F1','source':'OCCUPATION_MONITORING_AND_PAIR_BIRTH_COMPLETION.md Section 5 and checker result conditions','correction':'Explicitly impose H0=0 for the exact square mean.','countercontrol':'Allowed H0=P_holes02+P_holes13 changes the unit-rate mean to 55/16 from 161/48.','status':'Author agreed; correction is outside the reviewed frozen revision.'}],'sources':source_rows,'artifacts':rows,'counts':{'sources':len(source_rows),'artifacts':len(rows)},'precomparison_unchanged':True,'limitations':'Source/proof scrutiny with selective exact controls, not audit status; author numerical points authenticated with one additional closed-form point checked; no author rerun; performance-interruption archive not replayed; no unrelated campaign access.'}
p=root/'FINAL_COMPARISON_SEAL.json'
with p.open('x') as f:json.dump(seal,f,indent=2);f.write('\n')
for name in ['COMPARISON.md','comparison_check.py','COMPARISON_RESULTS.json','FINAL_COMPARISON_SEAL.json']:
 p=root/name;print(name,hashlib.sha256(p.read_bytes()).hexdigest())
print('sources',len(source_rows),'artifacts',len(rows))
