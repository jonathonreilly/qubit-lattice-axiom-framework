from pathlib import Path
import json,hashlib,gzip,subprocess
r=Path('/private/tmp/review-drain-20260915');w=r/'author-slot-one';h=r/'check8071';inv=json.loads((h/'inventory.json').read_text());d=w/'docs/work_history/repo/review_feedback/pr8071-evidence';m=json.loads((d/'archive-manifest.json').read_text());sha=lambda b:hashlib.sha256(b).hexdigest()
for e in m['entries']:
 b=(d/e['stored_path']).read_bytes();assert sha(b)==e['stored_sha256'];raw=gzip.decompress(b) if e['encoding']=='gzip' else b;assert sha(raw)==e['raw_sha256'];assert raw==subprocess.check_output(['git','-C',str(w),'show',inv['head']+':'+e['original_path']])
statuses=dict(x.split('\t',1)[::-1] for x in subprocess.check_output(['git','-C',str(w),'diff','--name-status','--no-renames',inv['original_base'],inv['head']],text=True).splitlines())
(h/'original-statuses.json').write_text(json.dumps(statuses,indent=2)+'\n');(h/'history-verification.json').write_text(json.dumps({'entries':len(m['entries']),'all_decoded_original_bytes_equal':True,'manifest_sha256':sha((d/'archive-manifest.json').read_bytes()),'original_paths':len(inv['paths']),'statuses':statuses},indent=2)+'\n');print(len(m['entries']),len(statuses))
