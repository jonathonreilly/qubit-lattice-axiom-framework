#!/usr/bin/env python3
"""Execute one local checker and preserve its exact command/streams/source hashes."""
from pathlib import Path
from datetime import datetime,timezone
import subprocess,hashlib,json,sys
HERE=Path(__file__).resolve().parent
script=HERE/sys.argv[1];prefix=sys.argv[2]
assert script.parent==HERE and script.exists()
paths={suffix:HERE/(prefix+suffix) for suffix in ['.stdout','.stderr','_RECEIPT.json','_RESULTS.json']}
assert not any(p.exists() for p in paths.values())
cmd=[sys.executable,str(script)];start=datetime.now(timezone.utc).isoformat()
r=subprocess.run(cmd,cwd=HERE,capture_output=True)
paths['.stdout'].write_bytes(r.stdout);paths['.stderr'].write_bytes(r.stderr)
rec={'command':cmd,'cwd':str(HERE),'started_utc':start,'finished_utc':datetime.now(timezone.utc).isoformat(),'exit_code':r.returncode,
 'script_sha256':hashlib.sha256(script.read_bytes()).hexdigest(),'builder_sha256':hashlib.sha256((HERE/'finite_blocks.py').read_bytes()).hexdigest(),
 'stdout_sha256':hashlib.sha256(r.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(r.stderr).hexdigest()}
paths['_RECEIPT.json'].write_text(json.dumps(rec,indent=2)+'\n')
if r.returncode==0:json.loads(r.stdout);paths['_RESULTS.json'].write_bytes(r.stdout)
print(json.dumps(rec,indent=2))
if r.returncode:print(r.stderr.decode())
sys.exit(r.returncode)
