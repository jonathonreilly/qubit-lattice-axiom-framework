"""Guarded fast-forward of a tracked-clean author checkout with owned new files.
Never stages or removes source. Bind expected head and exact declared additions.
"""
from pathlib import Path
import subprocess,json,hashlib,argparse
ap=argparse.ArgumentParser();ap.add_argument('slot');ap.add_argument('expected_head');ap.add_argument('receipt');a=ap.parse_args();r=Path(__file__).resolve().parent;w=r/a.slot;out=r/a.receipt;assert not out.exists()
git=lambda *args:subprocess.check_output(['git','-C',str(w),*args],text=True).strip();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert git('rev-parse','HEAD')==a.expected_head;assert not git('diff','--name-only') and not git('diff','--cached','--name-only')
paths=git('ls-files','--others','--exclude-standard').splitlines();hashes={p:sha(w/p) for p in paths};new=git('rev-parse','origin/main');changes=git('diff','--name-only',a.expected_head,new).splitlines();assert not set(paths)&set(changes)
subprocess.run(['git','-C',str(w),'merge','--ff-only',new],check=True,stdout=subprocess.DEVNULL)
assert git('rev-parse','HEAD')==new and not git('diff','--name-only') and not git('diff','--cached','--name-only');assert paths==git('ls-files','--others','--exclude-standard').splitlines();assert all(sha(w/p)==h for p,h in hashes.items())
out.write_text(json.dumps({'slot':a.slot,'old_head':a.expected_head,'new_head':new,'preserved_owned_additions':hashes,'intervening_paths':changes,'tracked_clean':True},indent=2)+'\n');print(a.slot,new,len(paths),'owned paths preserved')
