from pathlib import Path
import datetime, hashlib, json, platform, subprocess, sys, time
ROOT=Path(__file__).resolve().parent
script=ROOT/'local_background_control.py'
def sh(p): return hashlib.sha256(p.read_bytes()).hexdigest()
start=datetime.datetime.now(datetime.timezone.utc).isoformat(); timer=time.perf_counter()
with (ROOT/'local_background_control.stdout.txt').open('wb') as stdout, (ROOT/'local_background_control.stderr.txt').open('wb') as stderr:
    result=subprocess.run([sys.executable,str(script)],cwd=ROOT,stdout=stdout,stderr=stderr)
out=dict(command=[sys.executable,str(script)],cwd=str(ROOT),started_utc=start,
         completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),wall_seconds=time.perf_counter()-timer,
         exit_code=result.returncode,python=sys.version,platform=platform.platform(),script_sha256=sh(script),
         stdout_sha256=sh(ROOT/'local_background_control.stdout.txt'),stderr_sha256=sh(ROOT/'local_background_control.stderr.txt'))
if (ROOT/'CONTROL_RESULTS.json').exists(): out['result_sha256']=sh(ROOT/'CONTROL_RESULTS.json')
(ROOT/'EXECUTION.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
raise SystemExit(result.returncode)
