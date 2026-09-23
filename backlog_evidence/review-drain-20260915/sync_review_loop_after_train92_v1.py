"""Install only reviewed remote bytes after verified landing; preserve full parity receipt."""
from pathlib import Path
import hashlib,json,subprocess
R=Path(__file__).resolve().parent;W=R/'integration-resume';L=Path('/Users/jonBridger/.codex/skills/review-loop');prefix='docs/ai_methodology/skills/review-loop/'
sha=lambda b:hashlib.sha256(b).hexdigest()
git=lambda *args:subprocess.check_output(['git','-C',str(W),*args])
land=json.loads((R/'train92-landing.json').read_text());assert land['landing_state']=='LANDED'
subprocess.run(['git','-C',str(W),'fetch','origin','main'],check=True)
main=git('rev-parse','origin/main').decode().strip();subprocess.run(['git','-C',str(W),'merge-base','--is-ancestor',land['candidate_commit'],main],check=True)
manifest=json.loads((R/'review-loop-efficiency-proposal-v1/manifest.json').read_text());changed=[]
for row in manifest['files']:
 p=L/row['path'];assert sha(p.read_bytes())==row['before_sha256'],('local drift',str(p))
 remote=git('show',main+':'+prefix+row['path']);assert sha(remote)==row['after_sha256'];changed.append((p,remote))
files=git('ls-tree','-r','--name-only',main,'--',prefix).decode().splitlines();assert len(files)==15
# Validate every unmodified installed file before any installation.
changed_paths={p.relative_to(L).as_posix() for p,_ in changed}
for f in files:
 rel=f.removeprefix(prefix)
 if rel not in changed_paths:assert (L/rel).read_bytes()==git('show',main+':'+f),('unrelated local drift',rel)
for p,b in changed:p.write_bytes(b)
rows=[]
for f in files:
 rel=f.removeprefix(prefix);b=git('show',main+':'+f);assert (L/rel).read_bytes()==b;rows.append({'path':rel,'sha256':sha(b),'byte_identical':True})
record={'main':main,'landing':land['candidate_commit'],'updated_files':[p.relative_to(L).as_posix() for p,_ in changed],'files':rows,'all15_byte_identical':True,'model_default_changed':False,'old_local_recovery':'review-loop-efficiency-local-before-recovery-v1.json'}
p=R/'review-loop-remote-parity-train92.json';assert not p.exists();p.write_text(json.dumps(record,indent=2)+'\n');print('SYNCHRONIZED four reviewed files; all15 match remote',main)
