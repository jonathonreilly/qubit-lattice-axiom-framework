"""Portable bounded independent launcher; all explicit reads are sibling files."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    "NEUTRAL_CONTRACT_SNAPSHOT_v1.json",
    "DERIVATION_BEFORE_AUTHOR_EXPOSURE_v1.md",
    "PRE_CODE_FREEZE_v1.json",
    "independent_controls_v1.py",
    "run_independent_bounded_v1.py",
]
import argparse
from datetime import datetime,timezone
import hashlib,json,os,re,resource,subprocess,sys,time
from pathlib import Path
parser=argparse.ArgumentParser();parser.add_argument("--attempt",default="independent_attempt01");args=parser.parse_args()
if not re.fullmatch(r"[A-Za-z0-9_]+",args.attempt):raise ValueError("Use a fresh simple attempt label")
here=Path(__file__).resolve().parent;prefix=here/args.attempt
if prefix.with_suffix(".run.json").exists():raise FileExistsError("Earlier evidence is immutable")
def bind():
    return {n:{"sha256":hashlib.sha256((here/n).read_bytes()).hexdigest(),"bytes":(here/n).stat().st_size} for n in AUDIT_INPUT_PATHS}
before=bind();argv=[sys.executable,"-B",str(here/"independent_controls_v1.py")]
started=datetime.now(timezone.utc).isoformat();start=time.monotonic();r0=resource.getrusage(resource.RUSAGE_CHILDREN);timeout=False
try:
    run=subprocess.run(argv,cwd=here,env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1"),stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=AUDIT_TIMEOUT_SEC,check=False)
    stdout,stderr,code=run.stdout,run.stderr,run.returncode
except subprocess.TimeoutExpired as exc:stdout,stderr,code=exc.stdout or b"",exc.stderr or b"",None;timeout=True
wall=time.monotonic()-start;r1=resource.getrusage(resource.RUSAGE_CHILDREN)
prefix.with_suffix(".stdout.json").write_bytes(stdout);prefix.with_suffix(".stderr.txt").write_bytes(stderr)
try:result=json.loads(stdout);parse_error=None
except (ValueError,UnicodeDecodeError) as exc:result=None;parse_error=repr(exc)
after=bind()
record={"argv":argv,"cwd":str(here),"timeout_seconds":AUDIT_TIMEOUT_SEC,"PYTHONDONTWRITEBYTECODE":"1",
        "start_utc":started,"end_utc":datetime.now(timezone.utc).isoformat(),"wall_seconds":wall,
        "child_user_seconds":r1.ru_utime-r0.ru_utime,"child_system_seconds":r1.ru_stime-r0.ru_stime,
        "child_peak_rss_platform_units":r1.ru_maxrss,"platform":sys.platform,"returncode":code,"timed_out":timeout,
        "stdout_bytes":len(stdout),"stdout_sha256":hashlib.sha256(stdout).hexdigest(),"stderr_bytes":len(stderr),
        "stderr_sha256":hashlib.sha256(stderr).hexdigest(),"output_parse_error":parse_error,
        "summary":result["summary"] if result else None,"input_binding_before":before,"input_binding_after":after,
        "inputs_unchanged":before==after,"new_author_mode_inverse_sources_read":False}
prefix.with_suffix(".run.json").write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps({k:record[k] for k in ("wall_seconds","returncode","timed_out","summary","output_parse_error","inputs_unchanged")},indent=2))
if code!=0 or timeout or before!=after:raise SystemExit(1)
