"""Bound and preserve independent synthetic supplement execution."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/FUCHS_RELATIVE_MOTION_AND_WEAK_INVERSE_v2.md",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/FUCHS_COMPLEX_PROBE_EXTENSION_v1.md",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/FUCHS_COMPLEX_PROBE_PLAN_v1.json",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_fuchs_weak/independent_complex_probes_v1.py",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_fuchs_weak/run_supplement_bounded_v1.py",
]
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import resource
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[4]
prefix=HERE/"supplement_attempt01"
if prefix.with_suffix(".run.json").exists():raise FileExistsError("Preserve existing attempts")
def binding():
    return {p:{"sha256":hashlib.sha256((ROOT/p).read_bytes()).hexdigest(),"bytes":(ROOT/p).stat().st_size} for p in AUDIT_INPUT_PATHS}
before=binding();start=time.monotonic();utc=datetime.now(timezone.utc).isoformat();r0=resource.getrusage(resource.RUSAGE_CHILDREN)
argv=[sys.executable,"-B",str(HERE/"independent_complex_probes_v1.py")];timeout=False
try:
    result=subprocess.run(argv,cwd=ROOT,env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1"),stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=AUDIT_TIMEOUT_SEC,check=False)
    stdout,stderr,code=result.stdout,result.stderr,result.returncode
except subprocess.TimeoutExpired as exc:
    timeout=True;stdout,stderr,code=exc.stdout or b"",exc.stderr or b"",None
wall=time.monotonic()-start;r1=resource.getrusage(resource.RUSAGE_CHILDREN)
prefix.with_suffix(".stdout.json").write_bytes(stdout);prefix.with_suffix(".stderr.txt").write_bytes(stderr)
after=binding()
try:parsed=json.loads(stdout);parse_error=None
except (ValueError,UnicodeDecodeError) as exc:parsed=None;parse_error=repr(exc)
meta={"command_argv":argv,"cwd":str(ROOT),"timeout_seconds":AUDIT_TIMEOUT_SEC,"PYTHONDONTWRITEBYTECODE":"1","observer_dont_write_bytecode":sys.dont_write_bytecode,"start_utc":utc,"end_utc":datetime.now(timezone.utc).isoformat(),"wall_seconds":wall,"child_user_seconds":r1.ru_utime-r0.ru_utime,"child_system_seconds":r1.ru_stime-r0.ru_stime,"child_peak_rss_platform_units":r1.ru_maxrss,"platform":sys.platform,"returncode":code,"timed_out":timeout,"python":sys.version,"stdout_bytes":len(stdout),"stdout_sha256":hashlib.sha256(stdout).hexdigest(),"stderr_bytes":len(stderr),"stderr_sha256":hashlib.sha256(stderr).hexdigest(),"source_binding_before":before,"source_binding_after":after,"sources_unchanged":before==after,"output_parse_error":parse_error,"summary":parsed["summary"] if parsed else None,"raw_trace_access":False}
prefix.with_suffix(".run.json").write_text(json.dumps(meta,indent=2)+"\n")
print(json.dumps({k:meta[k] for k in ("wall_seconds","returncode","timed_out","summary","sources_unchanged")},indent=2))
if code!=0 or timeout or before!=after:sys.exit(1)
