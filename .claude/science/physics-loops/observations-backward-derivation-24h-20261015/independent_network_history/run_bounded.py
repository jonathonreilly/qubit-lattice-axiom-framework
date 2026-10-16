from pathlib import Path
import subprocess,sys,time,json
p=Path(__file__).resolve().parent
cmd=[sys.executable,str(p/'reproduce.py')]
t=time.monotonic()
try:
    r=subprocess.run(cmd,capture_output=True,text=True,timeout=120)
    (p/'reproduction.stdout').write_text(r.stdout)
    (p/'reproduction.stderr').write_text(r.stderr)
    record={'command':cmd,'timeout_seconds':120,'elapsed_seconds':time.monotonic()-t,'returncode':r.returncode}
except subprocess.TimeoutExpired:
    record={'command':cmd,'timeout_seconds':120,'elapsed_seconds':time.monotonic()-t,'failure':'TimeoutExpired'}
(p/'execution.json').write_text(json.dumps(record,indent=2))
print(json.dumps(record))
