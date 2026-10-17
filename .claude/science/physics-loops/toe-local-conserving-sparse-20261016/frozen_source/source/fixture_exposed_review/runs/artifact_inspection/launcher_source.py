"""Bounded actual saved-artifact inspection with source and launcher capture."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import os
import subprocess
import sys
import time
OUT=Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/local_conserving_sparse_fixture_exposed_check')
run=OUT/'runs/artifact_inspection';run.mkdir(parents=True,exist_ok=False)
source=OUT/'inspect_artifacts.py';executed=run/'executed_source.py';executed.write_bytes(source.read_bytes())
launcher=run/'launcher_source.py';launcher.write_bytes(Path(__file__).read_bytes())
sha=lambda raw:hashlib.sha256(raw).hexdigest()
argv=[sys.executable,'-B',str(executed)]
env=dict(os.environ);env.update(PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
receipt={'kind':'actual_saved_artifact_inspection_and_floating_reanalysis','compiler_replay':False,'gate_propagation':False,'argv':argv,'cwd':str(OUT),'start_utc':datetime.now(timezone.utc).isoformat(),'wall_timeout_seconds':60,'source_sha256':sha(executed.read_bytes()),'launcher_sha256':sha(launcher.read_bytes()),'environment_overrides':{'PYTHONDONTWRITEBYTECODE':'1','OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1'}}
(run/'EXECUTION.json').write_text(json.dumps(receipt,indent=2)+'\n')
started=time.monotonic()
try:
    result=subprocess.run(argv,cwd=OUT,env=env,capture_output=True,timeout=60)
    stdout,stderr=result.stdout,result.stderr;receipt['exit_code']=result.returncode
except Exception as exc:
    stdout=getattr(exc,'stdout',None) or b'';stderr=getattr(exc,'stderr',None) or b''
    stderr+=repr(exc).encode();receipt['exit_code']=None;receipt['exception']=repr(exc)
(run/'stdout').write_bytes(stdout);(run/'stderr').write_bytes(stderr)
receipt.update(end_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-started,stdout_bytes=len(stdout),stdout_sha256=sha(stdout),stderr_bytes=len(stderr),stderr_sha256=sha(stderr))
(run/'EXECUTION.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2));sys.exit(0 if receipt['exit_code']==0 else 1)
