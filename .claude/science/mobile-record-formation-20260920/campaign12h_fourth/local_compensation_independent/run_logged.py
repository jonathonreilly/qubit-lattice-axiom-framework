"""Capture an actual subprocess and its exact input identities, never overwrite."""
from pathlib import Path
import datetime,hashlib,json,subprocess,sys,time
base=Path(__file__).resolve().parent
name,script,*args=sys.argv[1:]
paths={k:base/(name+s) for k,s in [('stdout','.stdout'),('stderr','.stderr'),('receipt','_RECEIPT.json')]}
assert all(not p.exists() for p in paths.values())
def bind(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
command=[sys.executable,str(base/script),*args]
t0=datetime.datetime.now(datetime.timezone.utc).isoformat();start=time.perf_counter()
with paths['stdout'].open('wb') as out,paths['stderr'].open('wb') as err:
 proc=subprocess.run(command,cwd=base,stdout=out,stderr=err)
receipt={'command':command,'cwd':str(base),'start_utc':t0,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.perf_counter()-start,'exit_code':proc.returncode,'inputs':[bind(base/script),bind(base/'model.py')],'outputs':[bind(paths['stdout']),bind(paths['stderr'])]}
paths['receipt'].write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'exit_code':proc.returncode,'receipt':str(paths['receipt'])}))
sys.exit(proc.returncode)
