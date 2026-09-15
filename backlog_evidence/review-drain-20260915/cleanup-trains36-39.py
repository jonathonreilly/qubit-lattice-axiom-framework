from pathlib import Path
import subprocess,hashlib,json,tarfile,sys
r=Path('/private/tmp/review-drain-20260915');repo=r/'train40';sys.path.insert(0,str(repo/'scripts'))
from science_fix_loop import cleanup_worktree
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
results=[]
for label in ('train36','train37b','train38','train39'):
 w=r/label;g=lambda *a:subprocess.check_output(['git','-C',str(w),*a],text=True).strip()
 landing=json.loads((r/(label+'-landing.json')).read_text());head=g('rev-parse','HEAD')
 assert landing['landing_state']=='LANDED' and landing['candidate_commit']==head
 subprocess.run(['git','-C',str(w),'merge-base','--is-ancestor',head,'origin/main'],check=True)
 assert not g('status','--porcelain','--untracked-files=all')
 paths=[p for p in subprocess.check_output(['git','-C',str(w),'ls-files','--others','--ignored','--exclude-standard','-z'],text=True).split('\0') if p]
 hashes={}
 for p in paths:
  q=w/p;assert q.is_file() and not q.is_symlink();assert p.startswith('docs/audit/') or '__pycache__' in q.parts,p;hashes[p]=sha(q)
 archive=r/(label+'-ignored-validation-recovery.tar.gz');assert not archive.exists()
 with tarfile.open(archive,'w:gz') as t:
  for p in paths:t.add(w/p,arcname=p,recursive=False)
 with tarfile.open(archive) as t:
  assert {m.name for m in t.getmembers()}==set(hashes)
  for m in t.getmembers():assert m.isfile() and hashlib.sha256(t.extractfile(m).read()).hexdigest()==hashes[m.name]
 rec={'head':head,'archive':archive.name,'archive_sha256':sha(archive),'paths':hashes,'boundary':'Ignored generated validation artifacts, not audit authority; exact decoded recovery verified before cleanup'}
 (r/(label+'-ignored-validation-recovery.json')).write_text(json.dumps(rec,indent=2)+'\n')
 for p,h in hashes.items():assert sha(w/p)==h;(w/p).unlink()
 ok,reason=cleanup_worktree(w);assert ok,reason
 results.append({'name':label,'head':head,'removed':ok,'reason':reason,'recovery':rec})
 (r/'cleanup-trains36-39-result.json').write_text(json.dumps(results,indent=2)+'\n');print(label,reason,flush=True)
