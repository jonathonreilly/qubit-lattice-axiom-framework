#!/usr/bin/env python3
"""Record real subprocess results without modifying frozen PRE or author bytes."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,subprocess,sys,time
HERE=Path(__file__).resolve().parent
FALLBACK=Path('/Users/jonreilly/Documents/Codex/mobile-record-formation-20260920/.claude/science/mobile-record-formation-20260920/campaign12h_fourth')
BASE=next(p for p in (HERE.parent,FALLBACK) if (p/'field_energy_completion_author/AUTHOR_SEAL.json').exists())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def verify_pre():
    seal=HERE/'PRE_SEAL.json'
    assert sha(seal)=='3c06c43ca8e216532709f929f6241d6b5c7f1c9d05a1152ad578a297fc5b6aa9'
    for name,row in json.loads(seal.read_text())['artifacts'].items():assert sha(HERE/name)==row['sha256'],name
verify_pre(); runs=[];env=dict(os.environ);env['PYTHONDONTWRITEBYTECODE']='1'
for label,script in [('OWN',HERE/'comparison_energy_control.py'),('AUTHOR',BASE/'field_energy_completion_author/completion_and_terminal_phase_check.py')]:
    start=datetime.now(timezone.utc).isoformat();tick=time.monotonic()
    command=[sys.executable,'-B',str(script)]
    result=subprocess.run(command,cwd=HERE,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    end=datetime.now(timezone.utc).isoformat()
    stdout=HERE/f'COMPARISON_{label}_STDOUT.log';stderr=HERE/f'COMPARISON_{label}_STDERR.log'
    stdout.write_bytes(result.stdout);stderr.write_bytes(result.stderr)
    runs.append({'label':label,'argv':command,'cwd':str(HERE),'start_utc':start,'end_utc':end,'duration_seconds':time.monotonic()-tick,'returncode':result.returncode,'script_sha256':sha(script),'stdout':{'path':stdout.name,'sha256':sha(stdout),'bytes':len(result.stdout)},'stderr':{'path':stderr.name,'sha256':sha(stderr),'bytes':len(result.stderr)}})
    (HERE/'COMPARISON_RUN_RECEIPT.json').write_text(json.dumps({'runs':runs,'bytecode_disabled':True},indent=2,sort_keys=True)+'\n')
    print(label,'returncode',result.returncode,'stdout_bytes',len(result.stdout),'stderr_bytes',len(result.stderr),flush=True)
    if result.returncode:raise SystemExit(result.returncode)
expected=BASE/'field_energy_completion_author/COMPLETION_AND_TERMINAL_PHASE_RESULTS.json'
assert (HERE/'COMPARISON_AUTHOR_STDOUT.log').read_bytes()==expected.read_bytes(),'author output differs'
verify_pre()
receipt={'runs':runs,'bytecode_disabled':True,'author_reproduction_exact_bytes':True,'author_expected_sha256':sha(expected),'PRE_unchanged_before_and_after':True,'wrapper_sha256':sha(Path(__file__))}
(HERE/'COMPARISON_RUN_RECEIPT.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
print('Author saved result reproduced byte-for-byte; PRE unchanged.')
