from pathlib import Path
import json,hashlib,stat,shutil,subprocess,difflib
R=Path('/private/tmp/review-drain-20260915');W=R/'author-draft-slot'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ref=lambda p:dict(path=str(p),sha256=sha(p))
def out(n,d):
 p=R/n
 with p.open('x') as f:json.dump(d,f,indent=2);f.write('\n')
 return p
git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
assert json.loads((R/'author-draft-slot.json').read_text())['owner']=='PR8174-author'
f=json.loads((R/'drain8174-prepared-v2-source-freeze.json').read_text())['files']
assert not git('diff','--name-only','HEAD')
assert set(git('ls-files','--others','--exclude-standard').splitlines())=={e['path'] for e in f}
for e in f:assert sha(W/e['path'])==sha(Path(e['immutable_copy']))==e['sha256']
old='docs/work_history/repo/review_feedback/pr8174-evidence/DEFERRED_SCIENCE.md';new=old.replace('DEFERRED_SCIENCE','pr8174-deferred-science');readme=str(Path(old).parent/'README.md')
assert not (W/new).exists();(W/old).rename(W/new)
prior=(W/readme).read_text();assert prior.count('(DEFERRED_SCIENCE.md)')==1;(W/readme).write_text(prior.replace('(DEFERRED_SCIENCE.md)','(pr8174-deferred-science.md)'))
paths=sorted(new if e['path']==old else e['path'] for e in f)
main=git('rev-parse','origin/main');tracked=git('ls-tree','-r','--name-only',main,'--','docs').splitlines();collisions=[]
for p in paths:
 if p.endswith('.md') and Path(p).name not in ('README.md','SKILL.md'):
  matches=[q for q in tracked if Path(q).name.casefold()==Path(p).name.casefold()]
  if matches:collisions.append(dict(path=p,existing=matches))
assert not collisions,collisions
snap=R/'drain8174-prepared-v3-source';assert not snap.exists()
for p in paths:
 q=snap/p;q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(W/p,q)
freeze=out('drain8174-prepared-v3-source-freeze.json',dict(files=[dict(path=p,sha256=sha(W/p),mode=oct(stat.S_IMODE((W/p).stat().st_mode)),immutable_copy=str(snap/p)) for p in paths]))
d=json.loads((R/'drain8174-author-prepared-v2.json').read_text());d['source_paths']=paths;d['deferred_science']['path']=new;d['source_freeze']=ref(freeze);d['status']='Prepared v3: appendix basename/link packaging correction only; affected confirmation pending';d['metadata_corrections']='v2 snapshot immutable; only appendix path and README link changed; all runtime/source mathematical bytes unchanged'
prep=out('drain8174-author-prepared-v3.json',d)
for name in ['full-mapping','discovery','input-resource-plan','finding-dispositions']:
 p=R/f'drain8174-author-{name}-v2.json';txt=p.read_text().replace(old,new)
 q=R/f'drain8174-author-{name}-v3.json'
 with q.open('x') as stream:stream.write(txt)
diff=R/'drain8174-packaging-v2-to-v3.diff'
with diff.open('x') as stream:stream.write(f'diff --git a/{old} b/{new}\nsimilarity index 100%\nrename from {old}\nrename to {new}\n'+''.join(difflib.unified_diff(prior.splitlines(True),(W/readme).read_text().splitlines(True),fromfile=readme,tofile=readme)))
col=out('drain8174-basename-collision-check-v3.json',dict(main=main,checked_paths=[p for p in paths if p.endswith('.md')],exceptions=['README.md','SKILL.md'],casefold_comparison=True,collisions=collisions,runtime_inputs_unchanged=True,runner_unchanged=True,renamed_payload_unchanged=sha(W/new)==next(e['sha256'] for e in f if e['path']==old),tracked_index_clean=True))
refs=[prep,freeze,diff,col]+[R/f'drain8174-author-{n}-v3.json' for n in ['full-mapping','discovery','input-resource-plan','finding-dispositions']]+[R/'drain8174-author-correction-v2.diff',R/'drain8174-author-preservation-v1.json',R/'drain8174-early-review-v2.json']
h=out('drain8174-author-handoff-v3.json',dict(status='Packaging correction only; v3 affected reviewer confirmation pending',references=[ref(p) for p in refs],source_count=31,original_recovery_count=25,inputs=4,helpers=0,registry_edits_needed=False,science_executions=0,staging=False,branch_retention_required=True,source_changes=['Rename exact appendix payload', 'README link target only'],original_reviewer='/root/review_8174'))
print(json.dumps([ref(prep),ref(freeze),ref(diff),ref(h)],indent=2))
