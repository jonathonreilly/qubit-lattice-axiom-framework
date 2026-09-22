import json,subprocess,hashlib
from pathlib import Path
r=Path('/private/tmp/review-drain-20260915');w=r/'integration-resume';git=lambda *a:subprocess.check_output(['git','-C',str(w),*a]);sha=lambda b:hashlib.sha256(b).hexdigest();rows=json.loads((r/'drain8153-fresh-metadata.json').read_text());current=git('rev-parse','0ee1a0396c').decode().strip()
for x in rows:
 h=x['headRefOid'];b=git('merge-base',h,x['baseRefOid']).decode().strip();x['delta_base']=b;x['current_main_comparison']=current
 patch=git('diff','--binary','--full-index',b,h);p=r/f"drain8153-pr{x['number']}-original.patch";p.write_bytes(patch);x['delta_file']=str(p);x['delta_sha256']=sha(patch);x['original_paths']=[]
 for path in git('diff','--no-renames','--name-only','-z',b,h).decode().split('\0'):
  if not path:continue
  entry=git('ls-tree',h,'--',path).decode().strip();rev=h
  if not entry:entry=git('ls-tree',b,'--',path).decode().strip();rev=b
  meta,_=entry.split('\t',1);mode,kind,blob=meta.split();data=git('cat-file','blob',blob);dest=r/'drain8153-originals'/str(x['number'])/path;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
  current_entry=git('ls-tree',current,'--',path).decode().strip()
  x['original_paths'].append(dict(path=path,mode=mode,blob=blob,sha256=sha(data),bytes=len(data),original_revision=rev,recovery_path=str(dest),current_main_blob=current_entry.split()[2] if current_entry else None))
 print(x['number'],b,len(x['original_paths']))
 for y in x['original_paths']:
  if y['path'].startswith(('docs/','scripts/')):print(' ',y['path'])
(r/'drain8153-original-inventory.json').write_text(json.dumps(rows,indent=2)+'\n')
