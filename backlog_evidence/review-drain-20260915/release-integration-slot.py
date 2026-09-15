"""Preserve generated validation bytes, then invoke the reviewed pool's strict release.
No source reset, clean, forced removal, audit decision or publication occurs.
"""
from pathlib import Path
import argparse,hashlib,json,subprocess,tarfile
ap=argparse.ArgumentParser();ap.add_argument('label');a=ap.parse_args()
r=Path(__file__).resolve().parent;w=r/'integration-one';skill=Path('/Users/jonBridger/.codex/skills/review-loop/scripts/review_workspace.py')
def git(*args):return subprocess.check_output(['git','-C',str(w),*args],text=True).strip()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
landing=json.loads((r/(a.label+'-landing.json')).read_text());head=git('rev-parse','HEAD')
assert landing['landing_state']=='LANDED' and head==landing['candidate_commit']
assert not git('status','--porcelain','--untracked-files=all')
state=json.loads((r/'integration-one.json').read_text());assert state['owner']==a.label and state['path']==str(w)
subprocess.run(['git','-C',str(w),'merge-base','--is-ancestor',head,'origin/main'],check=True)
ignored=subprocess.check_output(['git','-C',str(w),'ls-files','--others','--ignored','--exclude-standard','-z'],text=True).split('\0');paths={}
for name in filter(None,ignored):
 p=w/name;assert p.is_file() and not p.is_symlink()
 assert name.startswith('docs/audit/') or ('__pycache__' in p.parts and p.suffix=='.pyc'),name
 paths[name]=sha(p)
archive=r/(a.label+'-pool-validation-recovery.tar.gz');record=r/(a.label+'-pool-validation-recovery.json');assert not archive.exists() and not record.exists()
with tarfile.open(archive,'w:gz') as t:
 for name in paths:t.add(w/name,arcname=name,recursive=False)
with tarfile.open(archive) as t:
 assert {m.name for m in t.getmembers()}==set(paths)
 for m in t.getmembers():assert m.isfile() and hashlib.sha256(t.extractfile(m).read()).hexdigest()==paths[m.name]
record.write_text(json.dumps({'head':head,'owner':a.label,'archive':archive.name,'archive_sha256':sha(archive),'paths':paths,'boundary':'Generated validation only; preserved decoded identities before releasing an exclusively owned landed checkout'},indent=2)+'\n')
for name,h in paths.items():
 p=w/name;assert sha(p)==h;p.unlink()
assert not git('status','--porcelain','--untracked-files=all','--ignored')
release=r/(a.label+'-integration-pool-release.json');assert not release.exists()
with release.open('x') as out:
 subprocess.run(['python3',str(skill),'release','--repo',str(w),'--pool',str(r),'--slot','integration-one','--owner',a.label,'--expected-head',head],stdout=out,check=True)
print(a.label,'released at',head)
