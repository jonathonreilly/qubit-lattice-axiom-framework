"""Bounded unchanged-author replays and separately labelled comparison controls."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    "comparison_controls_v1.py", "POST_EXPOSURE_COMPARISON_DERIVATION_v1.md", "POST_EXPOSURE_PLAN_FREEZE_v1.json",
    "AUTHOR_SNAPSHOT_BINDING_v1.json", "run_comparison_bounded_v1.py",
    "author_snapshot/MODE_INVERSE_ROOT_FREEZE_v1.json", "author_snapshot/MODE_GAIN_ROOT_FREEZE_v1.json",
    "author_snapshot/MODE_INVERSE_NEUTRAL_CONTRACT_v1.json", "author_snapshot/MODE_INVERSE_DERIVATION_v1.md",
    "author_snapshot/MODE_GAIN_DERIVATION_v1.md", "author_snapshot/check_mode_inverse_v1.py",
    "author_snapshot/check_mode_inverse_jets_v1.py", "author_snapshot/check_mode_gain_v1.py", "author_snapshot/check_mode_gain_jets_v1.py",
    "author_snapshot/MODE_INVERSE_CONTROLS_v1.json", "author_snapshot/MODE_INVERSE_JETS_v1.json",
    "author_snapshot/MODE_GAIN_CONTROLS_v1.json", "author_snapshot/MODE_GAIN_JETS_v1.json",
    "author_snapshot/SCALAR_RESPONSE_DERIVATION_v1.md", "author_snapshot/SCALAR_RESPONSE_CLOSURE_v1.md",
    "author_snapshot/MATTER_CLOCK_DERIVATION_v2.md", "author_snapshot/run_mode_inverse_mutations_v1.py",
    "author_snapshot/mode_inverse_mutations_v1/REPORT.json",
]
import hashlib,json,os,resource,subprocess,sys,time
from pathlib import Path
from datetime import datetime,timezone
here=Path(__file__).resolve().parent
def bind():
    return {n:{"sha256":hashlib.sha256((here/n).read_bytes()).hexdigest(),"bytes":(here/n).stat().st_size} for n in AUDIT_INPUT_PATHS}
cases=[
    ("comparison_attempt01","comparison_controls_v1.py",None),
    ("author_primary_replay01","author_snapshot/check_mode_inverse_v1.py","author_snapshot/MODE_INVERSE_CONTROLS_v1.json"),
    ("author_jets_replay01","author_snapshot/check_mode_inverse_jets_v1.py","author_snapshot/MODE_INVERSE_JETS_v1.json"),
    ("author_gain_replay01","author_snapshot/check_mode_gain_v1.py","author_snapshot/MODE_GAIN_CONTROLS_v1.json"),
    ("author_gain_jets_replay01","author_snapshot/check_mode_gain_jets_v1.py","author_snapshot/MODE_GAIN_JETS_v1.json"),
]
if any((here/(label+".run.json")).exists() for label,_,_ in cases):raise FileExistsError("Preserve earlier attempts")
before=bind();all_records=[]
for label,script,expected in cases:
    argv=[sys.executable,"-B",str(here/script)];cwd=(here/script).parent
    started=datetime.now(timezone.utc).isoformat();start=time.monotonic();r0=resource.getrusage(resource.RUSAGE_CHILDREN)
    timeout=False
    try:
        run=subprocess.run(argv,cwd=cwd,env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1"),
                           stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=AUDIT_TIMEOUT_SEC,check=False)
        stdout,stderr,code=run.stdout,run.stderr,run.returncode
    except subprocess.TimeoutExpired as exc:stdout,stderr,code=exc.stdout or b"",exc.stderr or b"",None;timeout=True
    wall=time.monotonic()-start;r1=resource.getrusage(resource.RUSAGE_CHILDREN)
    (here/(label+".stdout.json")).write_bytes(stdout);(here/(label+".stderr.txt")).write_bytes(stderr)
    try:result=json.loads(stdout);parse_error=None
    except (ValueError,UnicodeDecodeError) as exc:result=None;parse_error=repr(exc)
    summary=(result.get("summary") or {k:result[k] for k in ("passed","failed")}) if result else None
    record={"argv":argv,"cwd":str(cwd),"timeout_seconds":AUDIT_TIMEOUT_SEC,"PYTHONDONTWRITEBYTECODE":"1",
            "start_utc":started,"end_utc":datetime.now(timezone.utc).isoformat(),"wall_seconds":wall,
            "child_user_seconds":r1.ru_utime-r0.ru_utime,"child_system_seconds":r1.ru_stime-r0.ru_stime,
            "child_peak_rss_platform_units":r1.ru_maxrss,"platform":sys.platform,"returncode":code,"timed_out":timeout,
            "stdout_bytes":len(stdout),"stdout_sha256":hashlib.sha256(stdout).hexdigest(),"stderr_bytes":len(stderr),
            "stderr_sha256":hashlib.sha256(stderr).hexdigest(),"output_parse_error":parse_error,"summary":summary,
            "stage":"post-author-exposure correspondence" if expected is None else "unchanged copied author replay",
            "script_sha256":before[script]["sha256"],"expected_output":expected,
            "stdout_byte_identical_to_expected":stdout==(here/expected).read_bytes() if expected else None}
    (here/(label+".run.json")).write_text(json.dumps(record,indent=2)+"\n")
    all_records.append(record)
    print(json.dumps({"attempt":label,**{k:record[k] for k in ("returncode","timed_out","wall_seconds","summary","stdout_byte_identical_to_expected")}}),flush=True)
after=bind()
out={"records":all_records,"input_binding_before":before,"input_binding_after":after,"inputs_unchanged":before==after,
     "no_parent_sources_run_in_place":True,"mutation_report_inspection_only":True}
(here/"COMPARISON_REPLAY_RUN_v1.json").write_text(json.dumps(out,indent=2)+"\n")
if before!=after or any(r["returncode"]!=0 or r["timed_out"] or r["summary"] is None or r["summary"]["failed"] for r in all_records):raise SystemExit(1)

