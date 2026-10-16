"""Preserve bounded actual executions; gate author reads on independent freeze."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/LAB_GEOMETRY_TRANSPORT_v1.md",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_lab_geometry_transport/independent_controls_v1.py",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_lab_geometry_transport/run_bounded_v1.py",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/check_lab_geometry_transport_v1.py",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/LAB_GEOMETRY_TRANSPORT_CONTROLS_v1.json",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/LAB_GEOMETRY_TRANSPORT_FROZEN_v1.json",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/LAB_GEOMETRY_TRANSPORT_RUN_v1.json",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/LAB_GEOMETRY_TRANSPORT_STDERR_v1.txt",
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_lab_geometry_transport/INDEPENDENT_OUTPUT_FREEZE_v1.json",
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

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]
mode=sys.argv[1]
assert mode in ("independent","author")
prefix=HERE/(mode+"_attempt01")
if prefix.with_suffix(".run.json").exists():
    raise FileExistsError("Preserve prior attempt; use a new version for a rerun.")
selected=AUDIT_INPUT_PATHS[:3]
if mode=="author":
    assert (ROOT/AUDIT_INPUT_PATHS[8]).exists(),"Freeze independent outputs before author access"
    selected=AUDIT_INPUT_PATHS
def binding():
    return {p:{"sha256":hashlib.sha256((ROOT/p).read_bytes()).hexdigest(),"bytes":(ROOT/p).stat().st_size} for p in selected}
before=binding()
if mode=="author":
    snapshots={}
    for path in [AUDIT_INPUT_PATHS[0]]+AUDIT_INPUT_PATHS[3:8]:
        raw=(ROOT/path).read_bytes()
        snapshots[Path(path).name]={"sha256":hashlib.sha256(raw).hexdigest(),"bytes":len(raw),"utf8":raw.decode()}
    (HERE/"AUTHOR_SOURCE_SNAPSHOT_v1.json").write_text(json.dumps({"captured_at_utc":datetime.now(timezone.utc).isoformat(),"after_independent_output_freeze_sha256":before[AUDIT_INPUT_PATHS[8]]["sha256"],"sources":snapshots},indent=2)+"\n")
target=ROOT/AUDIT_INPUT_PATHS[1 if mode=="independent" else 3]
argv=[sys.executable,"-B",str(target)]
utc=datetime.now(timezone.utc).isoformat();start=time.monotonic()
usage0=resource.getrusage(resource.RUSAGE_CHILDREN)
timed_out=False
try:
    run=subprocess.run(argv,cwd=ROOT,env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1"),stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=AUDIT_TIMEOUT_SEC,check=False)
    stdout,stderr,code=run.stdout,run.stderr,run.returncode
except subprocess.TimeoutExpired as exc:
    timed_out=True;stdout,stderr,code=exc.stdout or b"",exc.stderr or b"",None
elapsed=time.monotonic()-start;usage1=resource.getrusage(resource.RUSAGE_CHILDREN)
prefix.with_suffix(".stdout.json").write_bytes(stdout)
prefix.with_suffix(".stderr.txt").write_bytes(stderr)
after=binding()
try:
    result=json.loads(stdout);parse_error=None
except (ValueError,UnicodeDecodeError) as exc:
    result=None;parse_error=repr(exc)
summary=result.get("summary",{"passed":result.get("passed"),"failed":result.get("failed")}) if result else None
meta={"mode":mode,"command_argv":argv,"cwd":str(ROOT),"timeout_seconds":AUDIT_TIMEOUT_SEC,"PYTHONDONTWRITEBYTECODE":"1","observer_dont_write_bytecode":sys.dont_write_bytecode,"start_utc":utc,"end_utc":datetime.now(timezone.utc).isoformat(),"wall_seconds":elapsed,"child_user_seconds":usage1.ru_utime-usage0.ru_utime,"child_system_seconds":usage1.ru_stime-usage0.ru_stime,"child_peak_rss_platform_units":usage1.ru_maxrss,"platform":sys.platform,"returncode":code,"timed_out":timed_out,"python":sys.version,"stdout_bytes":len(stdout),"stdout_sha256":hashlib.sha256(stdout).hexdigest(),"stderr_bytes":len(stderr),"stderr_sha256":hashlib.sha256(stderr).hexdigest(),"source_binding_before":before,"source_binding_after":after,"sources_unchanged":before==after,"output_parse_error":parse_error,"summary":summary}
if mode=="author":
    receipt=(ROOT/AUDIT_INPUT_PATHS[4]).read_bytes()
    meta.update(matches_original_receipt_bytes=stdout==receipt,matches_original_receipt_json=result==json.loads(receipt),independent_outputs_frozen_before_author_read=True)
else:
    meta["author_runner_or_results_read"]=False
prefix.with_suffix(".run.json").write_text(json.dumps(meta,indent=2)+"\n")
print(json.dumps({k:meta[k] for k in ("mode","wall_seconds","returncode","timed_out","summary","sources_unchanged")},indent=2))
if code!=0 or timed_out or before!=after:
    sys.exit(1)
