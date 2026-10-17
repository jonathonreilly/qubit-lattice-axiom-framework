#!/usr/bin/env python3
"""Assemble the complete review and freeze; deterministic bookkeeping only."""
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path

R=Path(__file__).resolve().parent
def identity(p):
    b=p.read_bytes();return {'bytes':len(b),'sha256':sha256(b).hexdigest()}
def write(p,b):
    with p.open('xb') as f:f.write(b);f.flush();os.fsync(f.fileno())
af=json.loads((R/'ANALYTIC_FREEZE.json').read_text())
for e in af['files']:assert identity(R/e['path'])=={k:e[k] for k in ('bytes','sha256')}
parts=['REVIEW_HEADER.md','PRECHECK_ANALYSIS.md','REVIEW_POSTCHECK.md']
write(R/'REVIEW.md',b'\n'.join((R/p).read_bytes() for p in parts))
files=[{'path':str(p.relative_to(R)),**identity(p)} for p in sorted(R.rglob('*')) if p.is_file() and p!=R/'FREEZE.json']
freeze={'frozen_utc':datetime.now(timezone.utc).isoformat(),
    'primary':'REVIEW.md','primary_identity':identity(R/'REVIEW.md'),
    'candidate_sha256':'57e1cebcee12bf6499564051f91f981fe11814d73d45b9e1168c045e65ab9b8c',
    'candidate_freeze_sha256':'41ce93b77d46c1dbecdde6f674201ca8b6e20026ae10231fe9b925fb69468e49',
    'disposition':'Supported conditional local preparation and runtime composition; no required mathematical correction; one nonblocking checker-coverage finding',
    'realifier_dependency_status':'Explicitly provisional; no root qualification inferred',
    'analysis_frozen_before_new_author_executable_exposure':True,
    'analytic_freeze_identity':identity(R/'ANALYTIC_FREEZE.json'),
    'scientific_executions_by_reviewer':0,'author_checker_replayed_or_imported':False,
    'private_root_preparation_idea_accessed':False,
    'independence':'same model, substantial shared prior source authorship/exposure; selective new analytical derivation',
    'source_W_Git_PR_checkpoint_prompt_axiom_audit_edits':False,
    'editable_prompt_files_changed':[],'model_effort_override':False,'subdelegation':False,
    'files':files,'self_in_inventory':False}
write(R/'FREEZE.json',(json.dumps(freeze,indent=2,sort_keys=True)+'\n').encode())
fd=os.open(R,os.O_RDONLY)
try:os.fsync(fd)
finally:os.close(fd)
print(json.dumps({'frozen_entries':len(files),'report':identity(R/'REVIEW.md'),
                  'freeze':identity(R/'FREEZE.json')},indent=2))
