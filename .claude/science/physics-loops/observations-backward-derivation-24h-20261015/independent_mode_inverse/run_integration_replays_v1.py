"""Capture and replay only the newly authorized trace/joint integration."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
 "MODE_TRACE_JOINT_ROOT_FREEZE_v1.json","MODE_TRACE_ROOT_DERIVATION_v1.md",
 "check_mode_trace_root_v1.py","MODE_TRACE_ROOT_CONTROLS_v1.json",
 "MODE_JOINT_GAIN_DERIVATION_v1.md","check_mode_joint_gain_v1.py","MODE_JOINT_GAIN_CONTROLS_v1.json",
 "MODE_GAIN_DERIVATION_v1.md","check_mode_inverse_jets_v1.py",
 "independent_mode_inverse/DERIVATION_BEFORE_AUTHOR_EXPOSURE_v1.md",
]
import argparse,hashlib,json,os,resource,subprocess,sys,time
from pathlib import Path
from datetime import datetime,timezone
pa=argparse.ArgumentParser();pa.add_argument("pack");args=pa.parse_args()
pack=Path(args.pack).resolve();here=Path(__file__).resolve().parent;dest=here/"integration_snapshot"
if dest.exists():raise FileExistsError("Preserve frozen integration copy")
dest.mkdir();bound={}
for n in AUDIT_INPUT_PATHS:
    data=(pack/n).read_bytes();p=dest/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
    bound[n]={"sha256":hashlib.sha256(data).hexdigest(),"bytes":len(data)}
fr=json.loads((dest/AUDIT_INPUT_PATHS[0]).read_text())
for n,h in fr["sources"].items():
    if bound[n]["sha256"]!=h:raise RuntimeError("Frozen source mismatch: "+n)
binding={"captured_utc":datetime.now(timezone.utc).isoformat(),"source_pack":str(pack),"files":bound,"all_freeze_matches":True,
         "stage":"After own supplement output freeze; unchanged author trace and joint-gain replay"}
(here/"INTEGRATION_SOURCE_BINDING_v1.json").write_text(json.dumps(binding,indent=2)+"\n")
results=[]
for label,script,cache in [
    ("author_trace_replay01","check_mode_trace_root_v1.py","MODE_TRACE_ROOT_CONTROLS_v1.json"),
    ("author_joint_replay01","check_mode_joint_gain_v1.py","MODE_JOINT_GAIN_CONTROLS_v1.json")]:
    argv=[sys.executable,"-B",str(dest/script)];begin=datetime.now(timezone.utc).isoformat();start=time.monotonic()
    r0=resource.getrusage(resource.RUSAGE_CHILDREN);timeout=False
    try:
        rr=subprocess.run(argv,cwd=dest,env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1"),stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=AUDIT_TIMEOUT_SEC,check=False)
        stdout,stderr,rc=rr.stdout,rr.stderr,rr.returncode
    except subprocess.TimeoutExpired as ex:stdout,stderr,rc=ex.stdout or b"",ex.stderr or b"",None;timeout=True
    r1=resource.getrusage(resource.RUSAGE_CHILDREN);wall=time.monotonic()-start
    (here/(label+".stdout.json")).write_bytes(stdout);(here/(label+".stderr.txt")).write_bytes(stderr)
    try:parsed=json.loads(stdout);error=None
    except (ValueError,UnicodeDecodeError) as ex:parsed=None;error=repr(ex)
    r={"argv":argv,"cwd":str(dest),"start_utc":begin,"end_utc":datetime.now(timezone.utc).isoformat(),"wall_seconds":wall,
       "timeout_seconds":AUDIT_TIMEOUT_SEC,"PYTHONDONTWRITEBYTECODE":"1","returncode":rc,"timed_out":timeout,
       "child_user_seconds":r1.ru_utime-r0.ru_utime,"child_system_seconds":r1.ru_stime-r0.ru_stime,
       "child_peak_rss_platform_units":r1.ru_maxrss,"platform":sys.platform,"output_parse_error":error,
       "summary":{k:parsed[k] for k in ("passed","failed")} if parsed else None,
       "script_sha256":bound[script]["sha256"],"stdout_sha256":hashlib.sha256(stdout).hexdigest(),
       "stderr_sha256":hashlib.sha256(stderr).hexdigest(),"stdout_bytes":len(stdout),"stderr_bytes":len(stderr),
       "stdout_byte_identical_to_expected":stdout==(dest/cache).read_bytes(),"stage":"unchanged copied post-exposure author integration"}
    (here/(label+".run.json")).write_text(json.dumps(r,indent=2)+"\n");results.append(r)
    print(json.dumps({k:r[k] for k in ("returncode","summary","wall_seconds","timed_out","stdout_byte_identical_to_expected")}),flush=True)
drift={}
for n,v in bound.items():
    now=(pack/n).read_bytes()
    drift[n]={"source_sha256":hashlib.sha256(now).hexdigest(),"source_unchanged":hashlib.sha256(now).hexdigest()==v["sha256"],
              "copy_unchanged":hashlib.sha256((dest/n).read_bytes()).hexdigest()==v["sha256"]}
r={"records":results,"final_source_and_copy_binding":drift,"all_unchanged":all(v["source_unchanged"] and v["copy_unchanged"] for v in drift.values())}
(here/"INTEGRATION_REPLAY_RUN_v1.json").write_text(json.dumps(r,indent=2)+"\n")
if not r["all_unchanged"] or any(x["returncode"]!=0 or x["timed_out"] or x["summary"] is None or x["summary"]["failed"] for x in results):raise SystemExit(1)

