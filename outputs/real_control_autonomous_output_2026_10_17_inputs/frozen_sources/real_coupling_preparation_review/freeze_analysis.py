#!/usr/bin/env python3
"""Bookkeeping only: preserve byte-pinned inputs and freeze the analytic review."""
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path

R=Path(__file__).resolve().parent
A=R.parent/'real_coupling_preparation_candidate'
def identity(p):
    b=p.read_bytes()
    return {'bytes':len(b),'sha256':sha256(b).hexdigest()}
def save(p,obj):
    with p.open('x') as f:
        json.dump(obj,f,indent=2,sort_keys=True);f.write('\n');f.flush();os.fsync(f.fileno())
def copy(src,dest,pin,size=None):
    d=identity(src)
    assert d['sha256']==pin
    if size is not None: assert d['bytes']==size
    dest.parent.mkdir(parents=True,exist_ok=True)
    with dest.open('xb') as f: f.write(src.read_bytes())
    return {'original':str(src),'snapshot':str(dest.relative_to(R)),**d}

entries=[]
for name,pin in {
    'CANDIDATE.md':'57e1cebcee12bf6499564051f91f981fe11814d73d45b9e1168c045e65ab9b8c',
    'FREEZE.json':'41ce93b77d46c1dbecdde6f674201ca8b6e20026ae10231fe9b925fb69468e49',
    'SOURCE_MAP.json':'c1a701881fdeb81ce3f878b7851f9f6f0b36f15d04b879f213d2fb76f902f1f9',
}.items():
    entries.append(copy(A/name,R/'inputs'/name,pin))
sources=json.loads((A/'SOURCE_MAP.json').read_text())['sources']
for e in sources:
    entry=copy(A/e['snapshot'],R/'inputs'/'inherited'/Path(e['snapshot']).name,e['sha256'],e['bytes'])
    entry['upstream_original']=e['original']
    entry['upstream_current']=identity(Path(e['original']))
    entry['upstream_matches_snapshot']=entry['upstream_current']=={k:e[k] for k in ('bytes','sha256')}
    assert entry['upstream_matches_snapshot']
    entries.append(entry)
save(R/'SOURCE_BINDINGS.json',{'created_utc':datetime.now(timezone.utc).isoformat(),
    'scientific_execution':False,'new_author_checker_output_exposure':False,
    'private_root_idea_accessed':False,'realifier_status':'provisional, prior selective review not yet root-qualified',
    'entries':entries})
files=[{'path':str(p.relative_to(R)),**identity(p)} for p in sorted(R.rglob('*')) if p.is_file()]
save(R/'ANALYTIC_FREEZE.json',{'frozen_utc':datetime.now(timezone.utc).isoformat(),
    'stage':'complete analytical result before new author checker/launcher/output inspection',
    'review_scientific_runs':0,'files':files})
fd=os.open(R,os.O_RDONLY)
try:os.fsync(fd)
finally:os.close(fd)
print(json.dumps({'snapshot_count':len(entries),'upstream_pairs':len(sources),
    'frozen_entries':len(files),'analysis':identity(R/'PRECHECK_ANALYSIS.md'),
    'analytic_freeze':identity(R/'ANALYTIC_FREEZE.json')},indent=2))
