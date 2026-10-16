#!/usr/bin/env python3
"""Record a unique actual attempt with executed source and all raw streams."""
import argparse,datetime,hashlib,json,os,platform,shutil,subprocess,sys,time
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--run',required=True);p.add_argument('--source',required=True);p.add_argument('args',nargs=argparse.REMAINDER);a=p.parse_args()
r=Path(a.run);r.mkdir();source=Path(a.source).resolve();before=source.read_bytes();(r/'executed_source.py').write_bytes(before)
cmd=[sys.executable,str(source)]+(a.args[1:] if a.args[:1]==['--'] else a.args)
start=datetime.datetime.now(datetime.timezone.utc).isoformat();tick=time.monotonic()
with (r/'stdout.txt').open('wb') as stdout,(r/'stderr.txt').open('wb') as stderr:
 rc=subprocess.run(cmd,stdout=stdout,stderr=stderr,cwd=source.parent).returncode
end=datetime.datetime.now(datetime.timezone.utc).isoformat();after=source.read_bytes()
def info(p):b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
d={'started_utc':start,'finished_utc':end,'wall_seconds':time.monotonic()-tick,'command':cmd,'exit_code':rc,'python':sys.version,'platform':platform.platform(),'source':str(source),'source_sha256_before':hashlib.sha256(before).hexdigest(),'source_sha256_after':hashlib.sha256(after).hexdigest(),'source_unchanged':before==after,'stdout':info(r/'stdout.txt'),'stderr':info(r/'stderr.txt')}
(r/'RECEIPT.json').write_text(json.dumps(d,indent=2,sort_keys=True)+'\n');print(json.dumps(d,indent=2));sys.exit(rc)
