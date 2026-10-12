#!/usr/bin/env python3
"""Reproduce a packet in a new explicit directory without changing frozen bytes."""
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('--packet',choices=('sphere','composition'),default='sphere')
parser.add_argument('--output-dir',type=Path,required=True,help='A new directory; must not already exist or be inside either source packet.')
args=parser.parse_args()
output=args.output_dir.resolve()
for source in (HERE,HERE.parent/'composition'):
    if output==source or output.is_relative_to(source):
        raise SystemExit('Output must be outside the source packets')
if args.packet=='sphere':
    source=HERE
    script='sphere_certificate.py'
    inputs=('PRECOMPUTE_FREEZE.json','POST_EXPLORATION_PROOF_PROTOCOL.json')
    results=('CERTIFICATE_RESULTS.json',)
else:
    source=HERE.parent/'composition'
    script='composition_check.py'
    inputs=('PRECOMPUTE_FREEZE.json','VISIBILITY_EXTENSION_FREEZE.json')
    results=('COMPUTATION_RESULTS.json','finite_directions.json')
output.mkdir(parents=True,exist_ok=False)
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
copied=[]
for name in (script,*inputs):
    shutil.copy2(source/name,output/name)
    copied.append({'file':name,'source_sha256':sha(source/name),'copy_sha256':sha(output/name)})
with (output/'execution.log').open('w') as log:
    run=subprocess.run([sys.executable,str(output/script)],cwd=output,stdout=log,stderr=subprocess.STDOUT)
checks=[]
if run.returncode==0:
    for name in results:
        original=json.loads((source/name).read_text())
        reproduced=json.loads((output/name).read_text())
        if isinstance(original,dict):
            for field in ('started_at','completed_at'):
                original.pop(field,None);reproduced.pop(field,None)
        checks.append({'file':name,'numerical_content_matches_after_removing_execution_timestamps':original==reproduced,'new_sha256':sha(output/name),'original_sha256':sha(source/name)})
receipt={'at':datetime.now(timezone.utc).isoformat(),'packet':args.packet,'source':str(source),'output':str(output),'returncode':run.returncode,'copies':copied,'comparisons':checks,'scope':'Foreground run of unchanged code and inputs in a new directory; original packet files remain unchanged. Campaign stop/deadline guards remain active.'}
(output/'REPRODUCTION_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
raise SystemExit(run.returncode or (0 if all(c['numerical_content_matches_after_removing_execution_timestamps'] for c in checks) else 1))
