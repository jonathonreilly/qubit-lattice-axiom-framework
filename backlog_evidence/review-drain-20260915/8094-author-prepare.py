"""Narrow packaging of independently read frozen8091/92/94 source; no executions."""
from pathlib import Path
import subprocess,json,hashlib,sys
r=Path('/private/tmp/review-drain-20260915');w=Path.cwd();g=lambda *a:subprocess.check_output(['git',*a],cwd=w,text=True).strip();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert not g('status','--porcelain');base=g('rev-parse','HEAD')
sys.path.insert(0,str(w/'docs/ai_methodology/skills/review-loop/scripts'));import review_workspace as workspace
rows=json.loads((r/'check8094/inventory.json').read_text());archives={}
for row in rows:
 n=row['number'];head=row['head'];canonical=row['canonical'];prefix=next(p['path'] for p in row['paths'] if p['path'].startswith('.claude/')).split('/')[0:4];prefix='/'.join(prefix)+'/'
 patch=subprocess.check_output(['git','diff','--binary',row['original_base'],head,'--',*canonical],cwd=w)
 (r/f'{n}-author-original-source.patch').write_bytes(patch)
 subprocess.run(['git','apply','--index'],cwd=w,input=patch,check=True)
 dest=w/f'docs/work_history/repo/review_feedback/pr{n}-evidence'
 manifest=workspace.archive(w,head,prefix,dest,['REVIEW_HISTORY.md'],f'pr{n}')
 (r/f'{n}-author-archive.json').write_text(json.dumps(manifest,indent=2)+'\n')
 h=sha(dest/'archive-manifest.json');workspace.verify_archive(dest,h)
 archives[str(n)]={'destination':str(dest.relative_to(w)),'manifest_sha256':h,'original_paths':len(manifest['entries'])}
 entry=next(x for x in manifest['entries'] if x['original_path']==prefix+'REVIEW_HISTORY.md')
 note=w/next(p for p in canonical if p.endswith('.md'));s=note.read_text();assert '.claude/' not in s
 rel=str((dest/entry['stored_path']).relative_to(w/'docs'))
 s+='\n## Historical evidence\n\nThe [historical author packet]('+rel+') preserves the original source review and execution history. It is provenance, not a current independent review or an audit verdict. The complete original path and payload map is preserved in the adjacent archive manifest.\n';note.write_text(s)
 primary=w/next(p for p in canonical if p.endswith('.py'));s=primary.read_text()
 if n==8092:
  needle="    print('Elapsed seconds:',out['elapsed_seconds'])";assert s.count(needle)==1;s=s.replace(needle,needle+"\n    print('TOTAL: PASS='+str(out['checks'])+' FAIL=0')")
 if n==8094:
  needle="    print(json.dumps(result,indent=2))";assert s.count(needle)==1;s=s.replace(needle,needle+"\n    print('TOTAL: PASS='+str(result['check_count'])+' FAIL=0')")
 primary.write_text(s)
 subprocess.run(['git','add','--',*canonical,str(dest)],cwd=w,check=True)
changed=g('diff','--cached','--name-only').splitlines()
subprocess.run(['python3','scripts/vocab_lint.py','--fix','--report-path',str(r/'8094-author-vocab.json'),*changed],cwd=w,check=True)
subprocess.run(['git','add','--',*changed],cwd=w,check=True)
for a in [('diff','--check'),('diff','--cached','--check'),('diff',base,'--check')]:subprocess.run(['git',*a],cwd=w,check=True)
(r/'8094-author-packaging.json').write_text(json.dumps({'base':base,'tree':g('write-tree'),'source_paths':{p:sha(w/p) for p in changed},'archives':archives,'change':'Three historical packet citations and two canonical count footers. No formulas changed. Original outputs must be preserved before single60sec primary captures.'},indent=2)+'\n')
print('PACKAGED',len(changed),g('write-tree'))
