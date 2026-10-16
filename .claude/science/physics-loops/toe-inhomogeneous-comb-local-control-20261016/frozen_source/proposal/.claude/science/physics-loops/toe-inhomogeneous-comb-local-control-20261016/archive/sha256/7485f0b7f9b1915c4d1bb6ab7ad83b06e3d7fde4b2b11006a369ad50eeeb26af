"""Capture the actual bounded metadata launch, source, launcher and full streams."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import os
import subprocess
import sys
OUT=Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/local_conserving_sparse_compiler_exposed_check')
run=OUT/'runs'/'source_capture';run.mkdir(parents=True,exist_ok=False)
source=OUT/'capture_sources.py';executed=run/'executed_source.py';executed.write_bytes(source.read_bytes())
launcher=run/'launcher_source.py';launcher.write_bytes(Path(__file__).read_bytes())
sha=lambda b:hashlib.sha256(b).hexdigest()
argv=[sys.executable,'-B',str(executed)];start=datetime.now(timezone.utc).isoformat()
env=dict(os.environ);env['PYTHONDONTWRITEBYTECODE']='1'
r=subprocess.run(argv,cwd=str(OUT),env=env,capture_output=True,timeout=60)
(run/'stdout').write_bytes(r.stdout);(run/'stderr').write_bytes(r.stderr)
receipt={'kind':'actual_metadata_only_execution','scientific_execution':False,'start_utc':start,'end_utc':datetime.now(timezone.utc).isoformat(),'argv':argv,'cwd':str(OUT),'timeout_seconds':60,'exit_code':r.returncode,'source_original_path':str(source),'source_at_launch_path':str(executed),'source_sha256':sha(executed.read_bytes()),'launcher_original_path':str(Path(__file__)),'launcher_at_launch_path':str(launcher),'launcher_sha256':sha(launcher.read_bytes()),'stdout_bytes':len(r.stdout),'stdout_sha256':sha(r.stdout),'stderr_bytes':len(r.stderr),'stderr_sha256':sha(r.stderr),'scope':'Verify and copy frozen author sources and historical run evidence, extract authorized primary text, bind prior review identity. No scientific checker launched.'}
(run/'EXECUTION.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2));sys.exit(r.returncode)
