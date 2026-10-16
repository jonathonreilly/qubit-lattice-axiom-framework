"""Replay unchanged author copies inside the allowed evidence directory."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/NON_EQUILIBRIUM_SCALAR_INVERSE_v1.md",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/check_nonequilibrium_scalar_v1.py",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/check_nonequilibrium_scalar_v2.py",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/NON_EQUILIBRIUM_SCALAR_CONTROLS_v1.json",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/NON_EQUILIBRIUM_SCALAR_CONTROLS_v2.json",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/NON_EQUILIBRIUM_CONTROL_RECOVERY_v1.json",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/NON_EQUILIBRIUM_REVIEW_INPUT_v1.json",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_non_equilibrium_scalar/original_replay/NON_EQUILIBRIUM_SCALAR_INVERSE_v1.md",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_non_equilibrium_scalar/original_replay/check_nonequilibrium_scalar_v1.py",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_non_equilibrium_scalar/original_replay/check_nonequilibrium_scalar_v2.py",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_non_equilibrium_scalar/replay_original_unit_bounded_v1.py",
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

HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[4];PACK=HERE.parent;REPLAY=HERE/"original_replay"
def binding():
    return {p:{"sha256":hashlib.sha256((ROOT/p).read_bytes()).hexdigest(),"bytes":(ROOT/p).stat().st_size} for p in AUDIT_INPUT_PATHS}
unexpected=False
for ver,expected_return in ((1,1),(2,0)):
    runner=f"check_nonequilibrium_scalar_v{ver}.py";receipt=f"NON_EQUILIBRIUM_SCALAR_CONTROLS_v{ver}.json"
    prefix=HERE/f"author_original_v{ver}_attempt01"
    if prefix.with_suffix(".run.json").exists() or (REPLAY/receipt).exists():raise FileExistsError("Preserve prior replay evidence")
    before=binding();start=time.monotonic();utc=datetime.now(timezone.utc).isoformat();r0=resource.getrusage(resource.RUSAGE_CHILDREN)
    argv=[sys.executable,"-B",str(REPLAY/runner)];timeout=False
    try:
        run=subprocess.run(argv,cwd=REPLAY,env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1"),stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=AUDIT_TIMEOUT_SEC,check=False)
        stdout,stderr,code=run.stdout,run.stderr,run.returncode
    except subprocess.TimeoutExpired as exc:
        timeout=True;stdout,stderr,code=exc.stdout or b"",exc.stderr or b"",None
    wall=time.monotonic()-start;r1=resource.getrusage(resource.RUSAGE_CHILDREN)
    prefix.with_suffix(".stdout.txt").write_bytes(stdout);prefix.with_suffix(".stderr.txt").write_bytes(stderr)
    after=binding();reference=(PACK/receipt).read_bytes();output=(REPLAY/receipt).read_bytes() if (REPLAY/receipt).exists() else b""
    try:parsed=json.loads(output);parse_error=None
    except (ValueError,UnicodeDecodeError) as exc:parsed=None;parse_error=repr(exc)
    meta={"argv":argv,"cwd":str(REPLAY),"timeout_seconds":AUDIT_TIMEOUT_SEC,"PYTHONDONTWRITEBYTECODE":"1","observer_dont_write_bytecode":sys.dont_write_bytecode,"start_utc":utc,"end_utc":datetime.now(timezone.utc).isoformat(),"wall_seconds":wall,"child_user_seconds":r1.ru_utime-r0.ru_utime,"child_system_seconds":r1.ru_stime-r0.ru_stime,"child_peak_rss_platform_units":r1.ru_maxrss,"platform":sys.platform,"returncode":code,"expected_historical_returncode":expected_return,"timed_out":timeout,"stdout_bytes":len(stdout),"stdout_sha256":hashlib.sha256(stdout).hexdigest(),"stderr_bytes":len(stderr),"stderr_sha256":hashlib.sha256(stderr).hexdigest(),"input_binding_before":before,"input_binding_after":after,"inputs_unchanged":before==after,"output_parse_error":parse_error,"summary":{"passed":parsed["passed"],"failed":parsed["failed"]} if parsed else None,"replay_output":str(REPLAY/receipt),"replay_output_sha256":hashlib.sha256(output).hexdigest(),"reference_sha256":hashlib.sha256(reference).hexdigest(),"output_byte_identical_to_original":output==reference,"author_sources_executed_in_place":False,"replay_sources_unchanged_copies":all((REPLAY/n).read_bytes()==(PACK/n).read_bytes() for n in (runner,"NON_EQUILIBRIUM_SCALAR_INVERSE_v1.md"))}
    prefix.with_suffix(".run.json").write_text(json.dumps(meta,indent=2)+"\n")
    print(json.dumps({"version":ver,**{k:meta[k] for k in ("wall_seconds","returncode","expected_historical_returncode","timed_out","summary","inputs_unchanged","output_byte_identical_to_original")}},indent=2),flush=True)
    unexpected=unexpected or code!=expected_return or timeout or before!=after or output!=reference
if unexpected:sys.exit(1)
