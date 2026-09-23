import sys,subprocess,time,json,hashlib,platform,os
from pathlib import Path
here=Path(__file__).resolve().parent
script=here/sys.argv[1];stem=sys.argv[2];start=time.time()
env=dict(os.environ);env['PYTHONDONTWRITEBYTECODE']='1'
p=subprocess.run([sys.executable,str(script),*sys.argv[3:]],cwd=here,capture_output=True,env=env)
(here/(stem+'.stdout')).write_bytes(p.stdout);(here/(stem+'.stderr')).write_bytes(p.stderr)
receipt={'command':[sys.executable,str(script),*sys.argv[3:]],'cwd':str(here),'started_unix':start,'elapsed_seconds':time.time()-start,'exit_code':p.returncode,'python':sys.version,'platform':platform.platform(),'script_sha256':hashlib.sha256(script.read_bytes()).hexdigest(),'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(p.stderr).hexdigest()}
(here/(stem+'_RECEIPT.json')).write_text(json.dumps(receipt,indent=2)+'\n')
print(p.stdout.decode(),end='');print(p.stderr.decode(),end='',file=sys.stderr)
sys.exit(p.returncode)
