"""Portable source-bound comparison and unchanged author replay, both bounded."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    "MATTER_CLOCK_NEUTRAL_CONTRACT_v1.json",
    "MATTER_CLOCK_DERIVATION_v1.md",
    "check_matter_clock_v1.py",
    "MATTER_CLOCK_CONTROLS_v1.json",
    "MATTER_CLOCK_RUN_v1.json",
    "MATTER_CLOCK_STDERR_v1.txt",
    "MATTER_CLOCK_AUTHOR_FREEZE_v1.json",
]
BUNDLE_INPUT_PATHS = [
    "AUTHOR_SOURCE_SNAPSHOT_v1.json",
    "INDEPENDENT_OUTPUT_FREEZE_v1.json",
    "independent_attempt01.stdout.json",
    "compare_author_formulas_v1.py",
    "run_author_comparison_v1.py",
]
import argparse
from datetime import datetime,timezone
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import subprocess
import sys
import time
parser=argparse.ArgumentParser()
parser.add_argument("--source-pack",required=True,type=Path)
parser.add_argument("--attempt",default="comparison_attempt01")
args=parser.parse_args()
if not re.fullmatch(r"[A-Za-z0-9_]+",args.attempt):raise ValueError("Use a simple fresh attempt label")
here=Path(__file__).resolve().parent;source=args.source_pack.resolve()
clone=here/(args.attempt+"_author_copy")
if clone.exists():raise FileExistsError("Preserve earlier evidence; use a fresh attempt label")
def bind(base,names):
    return {n:{"sha256":hashlib.sha256((base/n).read_bytes()).hexdigest(),"bytes":(base/n).stat().st_size} for n in names}
before=bind(source,AUDIT_INPUT_PATHS);bundle_before=bind(here,BUNDLE_INPUT_PATHS)
snapshot=json.loads((here/"AUTHOR_SOURCE_SNAPSHOT_v1.json").read_text())["sources"]
if not all(before[n]["sha256"]==snapshot[n]["sha256"] for n in AUDIT_INPUT_PATHS):
    (here/(args.attempt+".source_drift.json")).write_text(json.dumps({"actual":before,"expected":{n:snapshot[n]["sha256"] for n in AUDIT_INPUT_PATHS}},indent=2)+"\n")
    raise RuntimeError("Author source moved from frozen snapshot; preserved drift")
clone.mkdir()
for n in AUDIT_INPUT_PATHS[:3]:(clone/n).write_bytes((source/n).read_bytes())
summaries={}
for kind,program,cwd in [
    ("formulas",here/"compare_author_formulas_v1.py",here),
    ("author",clone/"check_matter_clock_v1.py",clone),
]:
    prefix=here/(args.attempt+"_"+kind)
    if prefix.with_suffix(".run.json").exists():raise FileExistsError("Preserve earlier output")
    argv=[sys.executable,"-B",str(program)]
    started=datetime.now(timezone.utc).isoformat();clock=time.monotonic()
    r0=resource.getrusage(resource.RUSAGE_CHILDREN);timeout=False
    try:
        run=subprocess.run(argv,cwd=cwd,env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1"),
                           stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=AUDIT_TIMEOUT_SEC,check=False)
        stdout,stderr,code=run.stdout,run.stderr,run.returncode
    except subprocess.TimeoutExpired as exc:
        stdout,stderr,code=exc.stdout or b"",exc.stderr or b"",None;timeout=True
    wall=time.monotonic()-clock;r1=resource.getrusage(resource.RUSAGE_CHILDREN)
    prefix.with_suffix(".stdout.json").write_bytes(stdout);prefix.with_suffix(".stderr.txt").write_bytes(stderr)
    try:result=json.loads(stdout);parse_error=None
    except (ValueError,UnicodeDecodeError) as exc:result=None;parse_error=repr(exc)
    after=bind(source,AUDIT_INPUT_PATHS);bundle_after=bind(here,BUNDLE_INPUT_PATHS)
    summary=(result["summary"] if kind=="formulas" else {"passed":result["passed"],"failed":result["failed"]}) if result else None
    identical=stdout==(source/"MATTER_CLOCK_CONTROLS_v1.json").read_bytes() if kind=="author" else None
    copied_unchanged=all((clone/n).read_bytes()==(source/n).read_bytes() for n in AUDIT_INPUT_PATHS[:3])
    record={"argv":argv,"cwd":str(cwd),"timeout_seconds":AUDIT_TIMEOUT_SEC,"PYTHONDONTWRITEBYTECODE":"1",
            "start_utc":started,"end_utc":datetime.now(timezone.utc).isoformat(),"wall_seconds":wall,
            "child_user_seconds":r1.ru_utime-r0.ru_utime,"child_system_seconds":r1.ru_stime-r0.ru_stime,
            "child_peak_rss_platform_units":r1.ru_maxrss,"platform":sys.platform,
            "returncode":code,"timed_out":timeout,"stdout_bytes":len(stdout),
            "stdout_sha256":hashlib.sha256(stdout).hexdigest(),"stderr_bytes":len(stderr),
            "stderr_sha256":hashlib.sha256(stderr).hexdigest(),"output_parse_error":parse_error,"summary":summary,
            "source_binding_before":before,"source_binding_after":after,"source_inputs_unchanged":before==after,
            "bundle_binding_before":bundle_before,"bundle_binding_after":bundle_after,"bundle_inputs_unchanged":bundle_before==bundle_after,
            "author_output_byte_identical":identical,"author_copies_unchanged":copied_unchanged,"author_script_executed_in_place":False}
    prefix.with_suffix(".run.json").write_text(json.dumps(record,indent=2)+"\n")
    summaries[kind]={k:record[k] for k in ("wall_seconds","returncode","timed_out","summary","author_output_byte_identical")}
    if code!=0 or timeout or before!=after or bundle_before!=bundle_after or not copied_unchanged or (kind=="author" and not identical):
        print(json.dumps(summaries,indent=2));raise SystemExit(1)
print(json.dumps(summaries,indent=2))
