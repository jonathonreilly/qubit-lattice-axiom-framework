from pathlib import Path
import hashlib,json,subprocess,sys
w=Path.cwd();r=w.parent;j=json.loads((r/'check8106/inventory.json').read_text())
g=lambda *a:subprocess.check_output(['git',*a],text=True).strip()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert not g('status','--porcelain');base=g('rev-parse','HEAD')
cache_path=next(x['path'] for x in j['paths'] if x['path'].startswith('logs/runner-cache/'))
patch=subprocess.check_output(['git','diff','--binary',j['original_base'],j['head'],'--',*j['canonical'],cache_path])
(r/'8106-author-original-source.patch').write_bytes(patch)
subprocess.run(['git','apply','--index'],input=patch,check=True)
sys.path.insert(0,'/Users/jonBridger/.codex/skills/review-loop/scripts');import review_workspace as op
prefix='.claude/science/physics-loops/toe-charged-phase-20260914/'
dest=w/'docs/work_history/repo/review_feedback/pr8106-evidence'
m=op.archive(w,j['head'],prefix,dest,['HANDOFF.md','REVIEW_HISTORY.md'],'pr8106')
(r/'8106-author-archive.json').write_text(json.dumps(m,indent=2)+'\n')
mh=sha(dest/'archive-manifest.json');op.verify_archive(dest,mh)
note=w/next(p for p in j['canonical'] if p.endswith('.md'))
handoff=next(x for x in m['entries'] if x['original_path']==prefix+'HANDOFF.md')
old='../'+prefix+'HANDOFF.md';new=(dest/handoff['stored_path']).relative_to(w/'docs').as_posix()
s=note.read_text();assert s.count(old)==1;note.write_text(s.replace(old,new))
sys.path.insert(0,str(w/'scripts'));import runner_cache
sys.path.insert(0,str(w/'docs/audit/scripts'));import build_citation_graph as graph
runner=next(p for p in j['canonical'] if p.endswith('.py'))
assert runner_cache.cache_status(runner)=='fresh'
assert runner_cache.declared_timeout_for(runner)==90
hint=graph.extract_claim_type_hint(note.read_text())
if hint[1] is None:
 s=note.read_text();needle='**Claim type:** bounded_theorem';assert s.count(needle)==1
 note.write_text(s.replace(needle,'**Type:** bounded_theorem'))
assert graph.extract_claim_type_hint(note.read_text())[1]=='bounded_theorem'
subprocess.run(['git','add','--',*j['canonical'],cache_path,str(dest)],check=True)
paths=g('diff','--cached','--name-only').splitlines()
subprocess.run(['python3','scripts/vocab_lint.py','--fix','--report-path',str(r/'8106-author-vocab.json'),*paths],check=True)
subprocess.run(['git','add','--',*paths],check=True)
assert (w/runner).read_bytes()==subprocess.check_output(['git','show',j['head']+':'+runner])
assert (w/cache_path).read_bytes()==subprocess.check_output(['git','show',j['head']+':'+cache_path])
assert runner_cache.cache_status(runner)=='fresh'
for a in [('diff','--check'),('diff','--cached','--check'),('diff','HEAD','--check')]:subprocess.run(['git',*a],check=True)
out={'base':base,'tree':g('write-tree'),'source_paths':{p:sha(w/p) for p in paths},'archive_manifest_sha256':mh,'changes':'Recovery link remapped to exact raw handoff; actual displayed Type normalized only if required. Primary and original cache byte-identical. No new execution or scientific verdict.','cache_sha256':sha(w/cache_path),'actual_cache_status':'fresh','declared_timeout':90,'original_type_hint':hint}
(r/'8106-author-packaging.json').write_text(json.dumps(out,indent=2)+'\n');print(len(paths),out['tree'])
