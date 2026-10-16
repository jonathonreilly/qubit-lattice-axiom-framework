"""Replay unchanged author synthetic controls only; no development runner."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/FUCHS_RELATIVE_MOTION_AND_WEAK_INVERSE_v1.md",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/FUCHS_COMPLEX_PROBE_EXTENSION_v1.md",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/fuchs_weak_math_v1.py",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/fuchs_weak_modulated_v1.py",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/check_fuchs_weak_v1.py",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/check_fuchs_complex_probes_v2.py",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/FUCHS_WEAK_CONTROLS_v1.json",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/FUCHS_COMPLEX_CONTROLS_v2.json",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_fuchs_weak/replay_author_synthetic_bounded_v1.py",
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

HERE=Path(__file__).resolve().parent;PACK=HERE.parent;ROOT=HERE.parents[4]
def binding():
    return {p:{"sha256":hashlib.sha256((ROOT/p).read_bytes()).hexdigest(),"bytes":(ROOT/p).stat().st_size} for p in AUDIT_INPUT_PATHS}
failed=False
for label,runner,receipt in (
    ("author_weak_v1_attempt01","check_fuchs_weak_v1.py","FUCHS_WEAK_CONTROLS_v1.json"),
    ("author_complex_v2_attempt01","check_fuchs_complex_probes_v2.py","FUCHS_COMPLEX_CONTROLS_v2.json"),
):
    prefix=HERE/label
    if prefix.with_suffix(".run.json").exists():raise FileExistsError("Preserve existing attempts")
    before=binding();start=time.monotonic();utc=datetime.now(timezone.utc).isoformat();r0=resource.getrusage(resource.RUSAGE_CHILDREN)
    argv=[sys.executable,"-B",str(PACK/runner)];timeout=False
    try:
        result=subprocess.run(argv,cwd=ROOT,env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1"),stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=AUDIT_TIMEOUT_SEC,check=False)
        stdout,stderr,code=result.stdout,result.stderr,result.returncode
    except subprocess.TimeoutExpired as exc:
        timeout=True;stdout,stderr,code=exc.stdout or b"",exc.stderr or b"",None
    wall=time.monotonic()-start;r1=resource.getrusage(resource.RUSAGE_CHILDREN)
    prefix.with_suffix(".stdout.json").write_bytes(stdout);prefix.with_suffix(".stderr.txt").write_bytes(stderr)
    after=binding();reference=(PACK/receipt).read_bytes()
    try:parsed=json.loads(stdout);parse_error=None
    except (ValueError,UnicodeDecodeError) as exc:parsed=None;parse_error=repr(exc)
    meta={"command_argv":argv,"cwd":str(ROOT),"timeout_seconds":AUDIT_TIMEOUT_SEC,"PYTHONDONTWRITEBYTECODE":"1","observer_dont_write_bytecode":sys.dont_write_bytecode,"start_utc":utc,"end_utc":datetime.now(timezone.utc).isoformat(),"wall_seconds":wall,"child_user_seconds":r1.ru_utime-r0.ru_utime,"child_system_seconds":r1.ru_stime-r0.ru_stime,"child_peak_rss_platform_units":r1.ru_maxrss,"platform":sys.platform,"returncode":code,"timed_out":timeout,"python":sys.version,"stdout_bytes":len(stdout),"stdout_sha256":hashlib.sha256(stdout).hexdigest(),"stderr_bytes":len(stderr),"stderr_sha256":hashlib.sha256(stderr).hexdigest(),"source_binding_before":before,"source_binding_after":after,"sources_unchanged":before==after,"output_parse_error":parse_error,"summary":{"passed":parsed["passed"],"failed":parsed["failed"]} if parsed else None,"reference_receipt":receipt,"reference_sha256":hashlib.sha256(reference).hexdigest(),"stdout_byte_identical_to_receipt":stdout==reference,"raw_trace_access":False,"development_runner_executed":False,"source_inspection":"Complete local runner/helper bodies inspected before execution. Only synthetic fixture generation, library imports, and explicit source-byte hash reads occur."}
    prefix.with_suffix(".run.json").write_text(json.dumps(meta,indent=2)+"\n")
    print(json.dumps({"label":label,**{k:meta[k] for k in ("wall_seconds","returncode","timed_out","summary","sources_unchanged","stdout_byte_identical_to_receipt")}},indent=2),flush=True)
    failed=failed or code!=0 or timeout or before!=after or stdout!=reference
if failed:sys.exit(1)
