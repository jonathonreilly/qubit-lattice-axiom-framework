"""Bounded launch with actual serialized/fsynced bindings before subprocess creation."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import collections
import decimal
import fractions
import numbers
import _decimal
import json
import os
import platform
import resource
import subprocess
import sys
import time

D=Path(__file__).resolve().parent
R=D/"run01"
R.mkdir(exist_ok=False)
def now(): return datetime.now(timezone.utc).isoformat()
def identity(path):
    s=path.stat()
    return {"sha256":sha256(path.read_bytes()).hexdigest(),"bytes":s.st_size,"device":s.st_dev,"inode":s.st_ino,"mtime_ns":s.st_mtime_ns}
def save(path,obj):
    with path.open("x") as f:
        json.dump(obj,f,indent=2); f.write("\n"); f.flush(); os.fsync(f.fileno())
executed=R/"executed_source.py"
with executed.open("xb") as f:
    f.write((D/"check_route.py").read_bytes()); f.flush(); os.fsync(f.fileno())
paths=[("checker",D/"check_route.py"),("executed_copy",executed),("launcher",Path(__file__).resolve()),("resource_plan",D/"RESOURCE_PLAN.json"),("original_plan",D/"PLAN.md"),("scalar_inputs",D/"SCALAR_INPUTS.json"),("source_manifest",D/"SOURCE_MANIFEST.json"),("snapshot_preparer",D/"prepare_inputs.py")]
manifest=json.loads((D/"SOURCE_MANIFEST.json").read_text())
paths += [("snapshot:"+e["snapshot"],D/e["snapshot"]) for e in manifest["entries"]]
runtime=[("runtime:interpreter",Path(sys.executable).resolve())]
runtime += [("runtime:"+m.__name__,Path(m.__file__).resolve()) for m in (fractions,numbers,decimal,_decimal,json,collections)]
bindings=[]
for label,path in paths+runtime:
    try: recorded=str(path.relative_to(D))
    except ValueError: recorded=str(path)
    bindings.append({"label":label,"path":recorded,"identity":identity(path)})
plan=json.loads((D/"RESOURCE_PLAN.json").read_text())
pre={"created_before_subprocess_utc":now(),"mode":"serialized, flushed, fsynced and closed before subprocess creation","bindings":bindings,"runtime_python_version":sys.version,"platform":platform.platform(),"cpu_soft_hard_seconds":[plan["cpu_soft_seconds"],plan["cpu_hard_seconds"]],"external_wall_seconds":plan["external_wall_seconds"],"requested_thread_environment":plan["requested_thread_environment"],"no_transitive_runtime_completeness_claim":True}
prepath=R/"PRELAUNCH.json"
save(prepath,pre)
directory_fd=os.open(R,os.O_RDONLY)
try: os.fsync(directory_fd)
finally: os.close(directory_fd)
preid=identity(prepath)
fsync_completed_utc=now()
env=dict(os.environ); env.update(plan["requested_thread_environment"]); env["PYTHONDONTWRITEBYTECODE"]="1"
def limits(): resource.setrlimit(resource.RLIMIT_CPU,(plan["cpu_soft_seconds"],plan["cpu_hard_seconds"]))
cmd=[str(Path(sys.executable).resolve()),"-B",str(executed),"--packet-root",str(D),"--prelaunch",str(prepath)]
before=resource.getrusage(resource.RUSAGE_CHILDREN)
launch_utc=now(); started=time.monotonic(); timeout=False
with (R/"stdout.json").open("xb") as stdout,(R/"stderr.txt").open("xb") as stderr:
    proc=subprocess.Popen(cmd,cwd=D,env=env,stdout=stdout,stderr=stderr,preexec_fn=limits)
    try: code=proc.wait(timeout=plan["external_wall_seconds"])
    except subprocess.TimeoutExpired:
        timeout=True; proc.kill(); code=proc.wait()
    stdout.flush(); os.fsync(stdout.fileno()); stderr.flush(); os.fsync(stderr.fileno())
elapsed=time.monotonic()-started; finish_utc=now()
after=resource.getrusage(resource.RUSAGE_CHILDREN)
post=[]
for entry in bindings:
    path=Path(entry["path"])
    if not path.is_absolute(): path=D/path
    current=identity(path)
    post.append({"label":entry["label"],"identity":current,"unchanged":current==entry["identity"]})
source_pairs=[]
for e in manifest["entries"]:
    current=sha256(Path(e["original"]).read_bytes()).hexdigest()
    source_pairs.append({"snapshot":e["snapshot"],"original":e["original"],"current_sha256":current,"unchanged_content":current==e["sha256"]})
receipt={"status":"completed" if code==0 and not timeout else "failed_or_timeout","prelaunch_fsync_completed_utc":fsync_completed_utc,"subprocess_created_after_utc":launch_utc,"finished_utc":finish_utc,"command":cmd,"returncode":code,"timed_out":timeout,"wrapper_wall_seconds":elapsed,"child_user_cpu_seconds":after.ru_utime-before.ru_utime,"child_system_cpu_seconds":after.ru_stime-before.ru_stime,"child_peak_rss_raw":after.ru_maxrss,"child_peak_rss_units":"bytes on Darwin; KiB on Linux","cpu_soft_hard_seconds":[plan["cpu_soft_seconds"],plan["cpu_hard_seconds"]],"external_wall_seconds":plan["external_wall_seconds"],"prelaunch_identity":preid,"prelaunch_unchanged":identity(prepath)==preid,"bindings_after":post,"all_bindings_unchanged":all(e["unchanged"] for e in post),"original_source_pairs_after":source_pairs,"all_original_source_contents_unchanged":all(e["unchanged_content"] for e in source_pairs),"stdout":identity(R/"stdout.json"),"stderr":identity(R/"stderr.txt"),"thread_count_measured":False,"source_count":len(manifest["entries"]),"binding_count":len(bindings)}
save(R/"RECEIPT.json",receipt)
print(json.dumps({k:receipt[k] for k in ["status","returncode","wrapper_wall_seconds","child_user_cpu_seconds","child_system_cpu_seconds","child_peak_rss_raw","prelaunch_unchanged","all_bindings_unchanged","all_original_source_contents_unchanged","source_count","binding_count"]},indent=2))
if code!=0 or timeout or not receipt["prelaunch_unchanged"] or not receipt["all_bindings_unchanged"] or not receipt["all_original_source_contents_unchanged"]:
    raise SystemExit(1)
