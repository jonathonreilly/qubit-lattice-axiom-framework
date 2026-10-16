"""Actual bounded metadata launch recorder; does not launch scientific code."""
from pathlib import Path
import datetime
import hashlib
import json
import os
import subprocess
import sys

OUT = Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/local_conserving_control_root_exposed_check')
run = OUT / 'runs' / 'source_capture'
run.mkdir(parents=True, exist_ok=False)
source = OUT / 'capture_sources.py'
launcher = Path(__file__)
executed = run / 'executed_source.py'
executed.write_bytes(source.read_bytes())
(run / 'launcher_source.py').write_bytes(launcher.read_bytes())
sha = lambda b: hashlib.sha256(b).hexdigest()
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
argv = [sys.executable, '-B', str(executed)]
env = dict(os.environ)
env['PYTHONDONTWRITEBYTECODE'] = '1'
result = subprocess.run(argv, cwd=str(OUT), env=env, capture_output=True, timeout=90)
(run / 'stdout').write_bytes(result.stdout)
(run / 'stderr').write_bytes(result.stderr)
receipt = {
    'kind': 'actual_metadata_only_execution',
    'scientific_execution': False,
    'start_utc': start,
    'end_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'argv': argv,
    'cwd': str(OUT),
    'timeout_seconds': 90,
    'exit_code': result.returncode,
    'source_original_path': str(source),
    'source_at_launch_path': str(executed),
    'source_sha256': sha(executed.read_bytes()),
    'launcher_original_path': str(launcher),
    'launcher_at_launch_path': str(run / 'launcher_source.py'),
    'launcher_sha256': sha((run / 'launcher_source.py').read_bytes()),
    'stdout_bytes': len(result.stdout),
    'stdout_sha256': sha(result.stdout),
    'stderr_bytes': len(result.stderr),
    'stderr_sha256': sha(result.stderr),
    'scope': 'Copy and verify the three authorized sources, extract primary pages, optionally render page 16. No scientific computation or prior science replay.'
}
(run / 'EXECUTION.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print(json.dumps(receipt, indent=2))
sys.exit(result.returncode)
