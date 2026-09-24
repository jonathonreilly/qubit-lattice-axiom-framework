#!/usr/bin/env python3
"""Verify an immutable local packet without inspecting adjacent live sources."""
from pathlib import Path
import hashlib,json,sys
HERE=Path(__file__).resolve().parent
target=HERE/(sys.argv[1] if len(sys.argv)>1 else 'FINAL_SEAL.json')
obj=json.loads(target.read_text());failures=[]
for row in obj['artifacts']:
 p=HERE/row['path']
 if not p.is_file():failures.append({'path':row['path'],'error':'missing'});continue
 data=p.read_bytes();got=hashlib.sha256(data).hexdigest()
 if got!=row['sha256'] or len(data)!=row['bytes']:failures.append({'path':row['path'],'actual_sha256':got,'actual_bytes':len(data)})
result={'seal':target.name,'seal_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'artifact_count':len(obj['artifacts']),'all_bindings_match':not failures,'failures':failures}
print(json.dumps(result,indent=2))
raise SystemExit(bool(failures))
