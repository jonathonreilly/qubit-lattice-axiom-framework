"""Bounded replay of the unchanged post-exposure author witness program."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    "MATTER_CLOCK_DERIVATION_v2.md",
    "MATTER_CLOCK_REVISION_RECEIPT_v2.json",
    "check_matter_clock_witness_v1.py",
    "MATTER_CLOCK_WITNESS_CONTROLS_v1.json",
    "MATTER_CLOCK_WITNESS_RUN_v1.json",
    "MATTER_CLOCK_WITNESS_STDERR_v1.txt",
    "independent_matter_clock/DERIVATION_BEFORE_AUTHOR_EXPOSURE_v1.md",
]
BUNDLE_INPUT_PATHS = [
    "AUTHOR_REVISION_SNAPSHOT_v2.json",
    "replay_witness_bounded_v1.py",
]
import argparse
from datetime import datetime,timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
parser=argparse.ArgumentParser()
parser.add_argument("--source-pack",type=Path,required=True)
parser.add_argument("--attempt",default="witness_attempt01")
args=parser.parse_args()
if not re.fullmatch(r"[A-Za-z0-9_]+",args.attempt):raise ValueError("Use a simple fresh attempt label")
here=Path(__file__).resolve().parent;source=args.source_pack.resolve()
prefix=here/args.attempt;clone=here/(args.attempt+"_author_copy")
if clone.exists() or prefix.with_suffix(".run.json").exists():raise FileExistsError("Preserve earlier evidence")
def bind(base,names):
    return {n:{"sha256":hashlib.sha256((base/n).read_bytes()).hexdigest(),"bytes":(base/n).stat().st_size} for n in names}
before=bind(source,AUDIT_INPUT_PATHS);bundle_before=bind(here,BUNDLE_INPUT_PATHS)
expected=json.loads((here/BUNDLE_INPUT_PATHS[0]).read_text())["sources"]
if not all(before[n]["sha256"]==expected[n]["sha256"] for n in AUDIT_INPUT_PATHS):
    prefix.with_suffix(".source_drift.json").write_text(json.dumps({"actual":before,"expected":{n:expected[n]["sha256"] for n in AUDIT_INPUT_PATHS}},indent=2)+"\n")
    raise RuntimeError("Revision sources moved; drift preserved")
copies=[AUDIT_INPUT_PATHS[0],AUDIT_INPUT_PATHS[2],AUDIT_INPUT_PATHS[6]]
for n in copies:
    target=clone/n;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes((source/n).read_bytes())
argv=[sys.executable,"-B",str(clone/AUDIT_INPUT_PATHS[2])]
started=datetime.now(timezone.utc).isoformat();start=time.monotonic();timeout=False
try:
    run=subprocess.run(argv,cwd=clone,env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1"),stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=AUDIT_TIMEOUT_SEC,check=False)
    stdout,stderr,code=run.stdout,run.stderr,run.returncode
except subprocess.TimeoutExpired as exc:
    stdout,stderr,code=exc.stdout or b"",exc.stderr or b"",None;timeout=True
wall=time.monotonic()-start
prefix.with_suffix(".stdout.json").write_bytes(stdout);prefix.with_suffix(".stderr.txt").write_bytes(stderr)
try:result=json.loads(stdout);parse_error=None
except (ValueError,UnicodeDecodeError) as exc:result=None;parse_error=repr(exc)
after=bind(source,AUDIT_INPUT_PATHS);bundle_after=bind(here,BUNDLE_INPUT_PATHS)
identical=stdout==(source/AUDIT_INPUT_PATHS[3]).read_bytes()
copies_match=all((clone/n).read_bytes()==(source/n).read_bytes() for n in copies)
record={"argv":argv,"cwd":str(clone),"timeout_seconds":AUDIT_TIMEOUT_SEC,"PYTHONDONTWRITEBYTECODE":"1",
        "start_utc":started,"end_utc":datetime.now(timezone.utc).isoformat(),"wall_seconds":wall,
        "returncode":code,"timed_out":timeout,"stdout_bytes":len(stdout),"stdout_sha256":hashlib.sha256(stdout).hexdigest(),
        "stderr_bytes":len(stderr),"stderr_sha256":hashlib.sha256(stderr).hexdigest(),"output_parse_error":parse_error,
        "summary":{"passed":result["passed"],"failed":result["failed"]} if result else None,
        "source_binding_before":before,"source_binding_after":after,"source_inputs_unchanged":before==after,
        "bundle_binding_before":bundle_before,"bundle_binding_after":bundle_after,"bundle_inputs_unchanged":bundle_before==bundle_after,
        "author_output_byte_identical":identical,"copied_sources_unchanged":copies_match,"author_script_executed_in_place":False}
prefix.with_suffix(".run.json").write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps({k:record[k] for k in ("wall_seconds","returncode","timed_out","summary","author_output_byte_identical","source_inputs_unchanged","copied_sources_unchanged")},indent=2))
if code!=0 or timeout or not identical or before!=after or bundle_before!=bundle_after or not copies_match:raise SystemExit(1)
