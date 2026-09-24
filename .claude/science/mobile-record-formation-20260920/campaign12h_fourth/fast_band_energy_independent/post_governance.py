#!/usr/bin/env python3
from pathlib import Path
import datetime,hashlib,json,subprocess
HERE=Path(__file__).resolve().parent
repo=next(p for p in HERE.parents if (p/'AGENTS.md').is_file() and (p/'docs/ai_methodology/SCIENCE_WORKFLOW.md').is_file())
manifest=json.loads((HERE/'SOURCE_MANIFEST.json').read_text())
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=repo,text=True).strip()
main=subprocess.check_output(['git','rev-parse','origin/main'],cwd=repo,text=True).strip()
rows=[]
for row in manifest['governance_reused']:
 path=row['path'];working=(repo/path).read_bytes();current=subprocess.check_output(['git','show',f'{main}:{path}'],cwd=repo)
 rows.append({'path':path,'pinned_expected_sha256':row['sha256'],'working_sha256':hashlib.sha256(working).hexdigest(),'local_origin_main_sha256':hashlib.sha256(current).hexdigest(),'unchanged':hashlib.sha256(working).hexdigest()==hashlib.sha256(current).hexdigest()==row['sha256']})
result={'observed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'candidate_HEAD':head,'local_origin_main':main,'pinned_main':'61fa847f032d25c90bca2c1273b7edb5713fe160','network_refresh':False,'rows':rows,'all_applicable_governance_unchanged':all(r['unchanged'] for r in rows)}
(HERE/'POST_GOVERNANCE_RECEIPT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
