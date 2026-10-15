#!/usr/bin/env python3
"""Metadata-only source freshness check. No matrix, dynamics, or adjacency recomputation."""
import datetime as dt
import difflib
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

OUT=Path(__file__).resolve().parent
FINAL=OUT/'sources/final_author'
REPO=Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree')
checks=[]
def now(): return dt.datetime.now(dt.timezone.utc).isoformat()
def sha(b): return hashlib.sha256(b).hexdigest()
def check(name, condition, **details):
    checks.append(dict(name=name, passed=bool(condition), **details))
def filecheck(name, path, expected, size=None):
    b=Path(path).read_bytes()
    check(name,sha(b)==expected and (size is None or len(b)==size),
          path=str(path),sha256=sha(b),bytes=len(b),expected_sha256=expected,expected_bytes=size)
def git(*args):
    env=dict(os.environ,GIT_OPTIONAL_LOCKS='0')
    r=subprocess.run(['git','-C',str(REPO),*args],capture_output=True,env=env)
    if r.returncode: raise RuntimeError(f'git {args}: {r.returncode}: {r.stderr.decode()}')
    return r.stdout
started=now()
error=None
refs={}
status=None
try:
    manifest=json.loads((OUT/'SOURCE_MANIFEST.json').read_text())
    for item in manifest['files']:
        filecheck('initial snapshot '+item['snapshot'],OUT/item['snapshot'],item['sha256'],item['bytes'])
    for item in manifest['final_files']:
        filecheck('final snapshot '+item['snapshot'],OUT/item['snapshot'],item['sha256'],item['bytes'])
        filecheck('final live '+item['snapshot'],item['source'],item['sha256'],item['bytes'])
    initial=manifest['frozen_initial_source']
    filecheck('root immutable initial source',initial['source'],initial['sha256'],initial['bytes'])
    freeze=json.loads((FINAL/'FINAL_FREEZE.json').read_text())
    for item in freeze['files']:
        filecheck('author final seal '+item['path'],FINAL/item['path'],item['sha256'],item['bytes'])
    pre=json.loads((FINAL/'PREEXEC_FREEZE.json').read_text())
    for item in pre['items']:
        name='PREEXEC_DERIVATION_RECOVERED.md' if item['path']=='DERIVATION.md' else item['path']
        filecheck('preexecution sealed identity '+item['path'],FINAL/name,item['sha256'],item['bytes'])
    dependencies=json.loads((FINAL/'SOURCE_MANIFEST.json').read_text())
    for item in dependencies['sources']:
        filecheck('author pinned dependency snapshot '+item['snapshot'],FINAL/item['snapshot'],item['sha256'],item['bytes'])
        filecheck('author pinned dependency live '+item['snapshot'],item['source'],item['sha256'],item['bytes'])
    for item in manifest['instruction_reuse_checks']:
        current=git('show','refs/remotes/origin/main:'+item['path'])
        check('origin/main unchanged instruction '+item['path'],sha(current)==item['old_sha256'],
              sha256=sha(current),expected_sha256=item['old_sha256'])
    for skill in ['physics-claim-reviewer','workhorse']:
        expected=next(i['old_sha256'] for i in manifest['instruction_reuse_checks'] if i['path'].endswith('/'+skill+'/SKILL.md'))
        filecheck('installed skill '+skill,Path('/Users/jonreilly/.codex/skills')/skill/'SKILL.md',expected)
    for ref in manifest['refs']:
        refs[ref]=git('rev-parse',ref).decode().strip()
    check('origin/main ref unchanged',refs['refs/remotes/origin/main']==manifest['refs']['refs/remotes/origin/main'],
          actual=refs['refs/remotes/origin/main'])
    status=git('status','--porcelain=v1','--untracked-files=normal').decode()
    def udiff(a,b,la,lb):
        return ''.join(difflib.unified_diff(a.splitlines(keepends=True),b.splitlines(keepends=True),fromfile=la,tofile=lb))
    final=(FINAL/'DERIVATION.md').read_text()
    recovered=(FINAL/'PREEXEC_DERIVATION_RECOVERED.md').read_text()
    expected=udiff(recovered,final,'PREEXEC_DERIVATION_RECOVERED.md (sealed before execution)','DERIVATION.md (final author argument)')
    check('complete preexecution to final text delta',expected==(FINAL/'POST_RUN_DERIVATION.diff').read_text())
    expected=udiff((OUT/'sources/initial_derivation.md').read_text(),final,'initial_6f2b94ba','final_d4ed04f7')
    check('complete initial review to final text delta',expected==(OUT/'FINAL_ARGUMENT_DELTA.diff').read_text())
    raw=json.loads((FINAL/'ISOLATION_ADJACENCY_INVENTORY.raw.json').read_text())
    corrected=json.loads((FINAL/'ISOLATION_ADJACENCY_INVENTORY.json').read_text())
    differences=sorted(k for k in set(raw)|set(corrected) if raw.get(k)!=corrected.get(k))
    check('adjacency correction changes descriptive metadata only',
          differences==['metadata_correction_utc','raw_output_sha256','status'],changed_keys=differences)
    check('raw adjacency output retained',corrected['raw_output_sha256']==sha((FINAL/'ISOLATION_ADJACENCY_INVENTORY.raw.json').read_bytes()))
    result=json.loads((FINAL/'EXACT_RESULT.json').read_text())
    check('saved fixture input hash matches',result['input_sha256']==sha((FINAL/'INPUT.json').read_bytes()))
    check('saved fixture source hash matches',result['source_sha256']==sha((FINAL/'exact_fixture.py').read_bytes()))
    check('saved predicate count and booleans only',len(result['checks'])==159 and all(c['pass'] for c in result['checks']),
          scope='Reading saved declarations only, not scientific verification.')
except Exception as exc:
    error=repr(exc)
    check('metadata execution completed',False,error=error)
record=dict(started_utc=started,finished_utc=now(),scope=__doc__,source_sha256=sha(Path(__file__).read_bytes()),
            refs=refs,working_tree_status_porcelain=status,checks=checks,error=error,
            count=len(checks),all_metadata_checks_pass=all(c['passed'] for c in checks))
(OUT/'METADATA_CHECK.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'metadata_checks':len(checks),'all_metadata_checks_pass':record['all_metadata_checks_pass'],
                  'failure_names':[c['name'] for c in checks if not c['passed']],
                  'refs':refs,'working_tree_clean':status==''},sort_keys=True))
sys.exit(0 if record['all_metadata_checks_pass'] else 1)

