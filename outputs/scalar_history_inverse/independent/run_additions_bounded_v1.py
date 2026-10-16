"""Portable bundle-relative bounded execution; no original repo hierarchy needed."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = []
BUNDLE_INPUT_PATHS = [
    "ADDITIONS_BEFORE_CANONICAL_READ_v1.md",
    "independent_additions_v1.py",
    "run_additions_bounded_v1.py",
]
from datetime import datetime,timezone
import hashlib
import json
import os
from pathlib import Path
import resource
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent;prefix=HERE/"additions_attempt01"
if prefix.with_suffix(".run.json").exists():raise FileExistsError("Preserve existing evidence")
def binding():return {p:{"sha256":hashlib.sha256((HERE/p).read_bytes()).hexdigest(),"bytes":(HERE/p).stat().st_size} for p in BUNDLE_INPUT_PATHS}
before=binding();start=time.monotonic();utc=datetime.now(timezone.utc).isoformat();r0=resource.getrusage(resource.RUSAGE_CHILDREN)
argv=[sys.executable,"-B",str(HERE/"independent_additions_v1.py")];timeout=False
try:
    run=subprocess.run(argv,cwd=HERE,env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1"),stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=AUDIT_TIMEOUT_SEC,check=False)
    stdout,stderr,code=run.stdout,run.stderr,run.returncode
except subprocess.TimeoutExpired as exc:timeout=True;stdout,stderr,code=exc.stdout or b"",exc.stderr or b"",None
wall=time.monotonic()-start;r1=resource.getrusage(resource.RUSAGE_CHILDREN)
prefix.with_suffix(".stdout.json").write_bytes(stdout);prefix.with_suffix(".stderr.txt").write_bytes(stderr)
after=binding()
try:parsed=json.loads(stdout);parse_error=None
except (ValueError,UnicodeDecodeError) as exc:parsed=None;parse_error=repr(exc)
meta={"argv":argv,"cwd":str(HERE),"timeout_seconds":AUDIT_TIMEOUT_SEC,"PYTHONDONTWRITEBYTECODE":"1","start_utc":utc,"end_utc":datetime.now(timezone.utc).isoformat(),"wall_seconds":wall,"child_user_seconds":r1.ru_utime-r0.ru_utime,"child_system_seconds":r1.ru_stime-r0.ru_stime,"child_peak_rss_platform_units":r1.ru_maxrss,"platform":sys.platform,"returncode":code,"timed_out":timeout,"stdout_bytes":len(stdout),"stdout_sha256":hashlib.sha256(stdout).hexdigest(),"stderr_bytes":len(stderr),"stderr_sha256":hashlib.sha256(stderr).hexdigest(),"input_binding_before":before,"input_binding_after":after,"inputs_unchanged":before==after,"output_parse_error":parse_error,"summary":parsed['summary'] if parsed else None}
prefix.with_suffix(".run.json").write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps({k:meta[k] for k in ('wall_seconds','returncode','timed_out','summary','inputs_unchanged')},indent=2))
if code!=0 or timeout or before!=after:sys.exit(1)
