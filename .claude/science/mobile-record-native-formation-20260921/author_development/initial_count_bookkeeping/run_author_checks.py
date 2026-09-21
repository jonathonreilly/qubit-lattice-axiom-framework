#!/usr/bin/env python3
"""Record author controls and every declared mutation against frozen inputs."""
from pathlib import Path
import hashlib,json,os,subprocess,sys,time,runpy
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
RUNNER=ROOT/'scripts/mobile_records_native_formation_euler_and_cubic_centering_2026_09_21.py'
module=runpy.run_path(str(RUNNER),run_name='source_inventory')
paths=[str(RUNNER.relative_to(ROOT)),*module['AUDIT_INPUT_PATHS']]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
identities={p:sha(ROOT/p) for p in paths}
names=list(module['MUTATIONS']);env=os.environ.copy();env['OPENBLAS_NUM_THREADS']='1'
records=[]
for mutation in [None]+names:
 output=HERE/('PRIMARY_RESULTS.json' if mutation is None else 'mutation_results/'+mutation+'.json')
 output.parent.mkdir(exist_ok=True)
 args=[sys.executable,str(RUNNER),'--output',str(output)]
 if mutation:args+=['--mutation',mutation]
 start=time.monotonic();r=subprocess.run(args,cwd=ROOT,env=env,capture_output=True,text=True)
 records.append(dict(mutation=mutation,returncode=r.returncode,elapsed_seconds=time.monotonic()-start,
                     stdout=r.stdout,stderr=r.stderr,result_path=str(output.relative_to(HERE)),result_sha256=sha(output) if output.exists() else None))
 (HERE/'AUTHOR_RUNS.json').write_text(json.dumps(dict(identities=identities,runs=records),indent=2)+'\n')
 assert r.returncode==(1 if mutation else 0),(mutation,r.stdout,r.stderr)
 assert 'FAIL:' in r.stdout if mutation else 'TOTAL: PASS=91 FAIL=0' in r.stdout
 # A rejected mutation must fail in the actual selected mathematical suite,
 # not merely a wrapper, syntax or source-inventory error.
 result=json.loads(output.read_text())
 if mutation:
  suite=result['suites'][-1]
  assert suite['suite']==module['MUTATIONS'][mutation][0] and suite['returncode']!=0
  assert 'AssertionError' in suite['stderr'] and 'SyntaxError' not in suite['stderr']
 print(json.dumps(dict(mutation=mutation,returncode=r.returncode,last_line=r.stdout.splitlines()[-1])),flush=True)
assert identities=={p:sha(ROOT/p) for p in paths}
(HERE/'AUTHOR_VERIFICATION.json').write_text(json.dumps(dict(identities=identities,primary_declared_controls=91,
 declared_mutations=len(names),all_mutations_rejected_by_mathematical_assertions=True,
 scope='Author controls only. Independent proof review and audit are separate.'),indent=2)+'\n')
