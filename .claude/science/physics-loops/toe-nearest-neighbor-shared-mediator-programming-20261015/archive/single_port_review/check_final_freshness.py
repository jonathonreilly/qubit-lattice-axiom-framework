#!/usr/bin/env python3
"""Final source freshness only; no scientific calculation."""
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

P=Path(__file__).resolve().parent
W=Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree')
now=lambda:dt.datetime.now(dt.timezone.utc).isoformat()
sha=lambda b:hashlib.sha256(b).hexdigest()
started=now()
m=json.loads((P/'SOURCE_MANIFEST.json').read_text())
checks=[]
def checkfile(name,path,h,n):
    b=Path(path).read_bytes()
    checks.append({'name':name,'path':str(path),'bytes':len(b),'sha256':sha(b),'same':sha(b)==h and len(b)==n})
for i in m['final_files']:
    checkfile('live final author',i['source'],i['sha256'],i['bytes'])
    checkfile('frozen final author',P/i['snapshot'],i['sha256'],i['bytes'])
i=m['frozen_initial_source']
checkfile('initial root snapshot',i['source'],i['sha256'],i['bytes'])
deps=json.loads((P/'sources/final_author/SOURCE_MANIFEST.json').read_text())
for i in deps['sources']:
    checkfile('live premise',i['source'],i['sha256'],i['bytes'])
env=dict(os.environ,GIT_OPTIONAL_LOCKS='0')
def git(*args):
    r=subprocess.run(['git','-C',str(W),*args],capture_output=True,env=env)
    if r.returncode: raise RuntimeError(r.stderr.decode())
    return r.stdout
for i in m['instruction_reuse_checks']:
    b=git('show','refs/remotes/origin/main:'+i['path'])
    checks.append({'name':'current origin/main instruction','path':i['path'],'sha256':sha(b),'same':sha(b)==i['old_sha256']})
refs={r:git('rev-parse',r).decode().strip() for r in m['refs']}
status=git('status','--porcelain=v1','--untracked-files=normal').decode()
r={'started_utc':started,'finished_utc':now(),'scope':__doc__,'source_sha256':sha(Path(__file__).read_bytes()),
   'checks':checks,'all_frozen_and_live_content_unchanged':all(i['same'] for i in checks),
   'refs':refs,'same_refs_as_review':refs==m['refs'],'working_tree_status_porcelain':status}
(P/'FINAL_SOURCE_FRESHNESS.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({k:v for k,v in r.items() if k!='checks'},sort_keys=True))
sys.exit(0 if r['all_frozen_and_live_content_unchanged'] else 1)

