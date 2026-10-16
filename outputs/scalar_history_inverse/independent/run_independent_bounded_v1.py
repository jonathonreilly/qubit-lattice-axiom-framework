"""Preserve one bounded pre-exposure exact computation and all failures."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_non_equilibrium_scalar/NEUTRAL_CONTRACT_BEFORE_EXPOSURE_v1.json",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_non_equilibrium_scalar/DERIVATION_BEFORE_AUTHOR_EXPOSURE_v1.md",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_non_equilibrium_scalar/PRE_CODE_FREEZE_v1.json",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_non_equilibrium_scalar/independent_exact_controls_v1.py",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_non_equilibrium_scalar/run_independent_bounded_v1.py",
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

HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[4]
prefix=HERE/"independent_attempt01"
if prefix.with_suffix(".run.json").exists():raise FileExistsError("Do not overwrite earlier attempts")
def binding():
    return {p:{"sha256":hashlib.sha256((ROOT/p).read_bytes()).hexdigest(),"bytes":(ROOT/p).stat().st_size} for p in AUDIT_INPUT_PATHS}
before=binding();start=time.monotonic();utc=datetime.now(timezone.utc).isoformat();r0=resource.getrusage(resource.RUSAGE_CHILDREN)
argv=[sys.executable,"-B",str(HERE/"independent_exact_controls_v1.py")];timeout=False
try:
    run=subprocess.run(argv,cwd=ROOT,env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1"),stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=AUDIT_TIMEOUT_SEC,check=False)
    stdout,stderr,code=run.stdout,run.stderr,run.returncode
except subprocess.TimeoutExpired as exc:
    timeout=True;stdout,stderr,code=exc.stdout or b"",exc.stderr or b"",None
wall=time.monotonic()-start;r1=resource.getrusage(resource.RUSAGE_CHILDREN)
prefix.with_suffix(".stdout.json").write_bytes(stdout);prefix.with_suffix(".stderr.txt").write_bytes(stderr)
after=binding()
try:parsed=json.loads(stdout);parse_error=None
except (ValueError,UnicodeDecodeError) as exc:parsed=None;parse_error=repr(exc)
meta={"argv":argv,"cwd":str(ROOT),"timeout_seconds":AUDIT_TIMEOUT_SEC,"PYTHONDONTWRITEBYTECODE":"1","observer_dont_write_bytecode":sys.dont_write_bytecode,"start_utc":utc,"end_utc":datetime.now(timezone.utc).isoformat(),"wall_seconds":wall,"child_user_seconds":r1.ru_utime-r0.ru_utime,"child_system_seconds":r1.ru_stime-r0.ru_stime,"child_peak_rss_platform_units":r1.ru_maxrss,"platform":sys.platform,"returncode":code,"timed_out":timeout,"stdout_bytes":len(stdout),"stdout_sha256":hashlib.sha256(stdout).hexdigest(),"stderr_bytes":len(stderr),"stderr_sha256":hashlib.sha256(stderr).hexdigest(),"input_binding_before":before,"input_binding_after":after,"inputs_unchanged":before==after,"output_parse_error":parse_error,"summary":parsed["summary"] if parsed else None,"author_artifacts_read":False}
prefix.with_suffix(".run.json").write_text(json.dumps(meta,indent=2)+"\n")
print(json.dumps({k:meta[k] for k in ("wall_seconds","returncode","timed_out","summary","inputs_unchanged")},indent=2))
if code!=0 or timeout or before!=after:sys.exit(1)
