#!/usr/bin/env python3
"""Record author controls and all declared mutations on one frozen source pair."""
from pathlib import Path
import hashlib,json,os,subprocess,sys,time
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
RUNNER=ROOT/'scripts/mobile_records_immutable_context_exchange_acoustic_limits_2026_09_21.py'
NOTE=ROOT/'docs/MOBILE_RECORDS_IMMUTABLE_CONTEXT_EXCHANGE_ACOUSTIC_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-21.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
identities={str(p.relative_to(ROOT)):sha(p) for p in (RUNNER,NOTE)}
env=os.environ.copy();env['OPENBLAS_NUM_THREADS']='1'
names=subprocess.check_output([sys.executable,str(RUNNER),'--list-mutations'],text=True,env=env).splitlines()
records=[]
for mutation in [None]+names:
    args=[sys.executable,str(RUNNER)]
    if mutation: args+=['--mutation',mutation]
    else: args+=['--output',str(HERE/'PRIMARY_RESULTS.json')]
    start=time.monotonic();r=subprocess.run(args,cwd=ROOT,env=env,capture_output=True,text=True)
    record={'mutation':mutation,'returncode':r.returncode,'elapsed_seconds':time.monotonic()-start,
            'stdout':r.stdout,'stderr':r.stderr}
    records.append(record)
    # Write exact strings in JSON, preserving whitespace in any traceback.
    (HERE/'AUTHOR_RUNS.json').write_text(json.dumps({'identities':identities,'runs':records},indent=2)+'\n')
    assert r.returncode==(1 if mutation else 0),(mutation,r.stdout,r.stderr)
    assert 'FAIL:' in r.stdout if mutation else 'TOTAL: PASS=49 FAIL=0' in r.stdout
    print(json.dumps({'mutation':mutation,'returncode':r.returncode,'last_lines':r.stdout.splitlines()[-2:]}),flush=True)
assert identities=={str(p.relative_to(ROOT)):sha(p) for p in (RUNNER,NOTE)}
(HERE/'AUTHOR_VERIFICATION.json').write_text(json.dumps({'identities':identities,'primary_pass':True,
    'declared_mutations':len(names),'all_mutations_rejected':True,
    'scientific_scope':'Author checks only. General proofs and independent reports are separate evidence.'},indent=2)+'\n')
