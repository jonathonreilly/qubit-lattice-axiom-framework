from pathlib import Path
import json,subprocess,hashlib,sys
w=Path.cwd();r=w.parent;j=json.loads((r/'check8096/inventory.json').read_text());g=lambda *a:subprocess.check_output(['git',*a],text=True).strip();assert not g('status','--porcelain');base=g('rev-parse','HEAD');patch=subprocess.check_output(['git','diff','--binary',j['original_base'],j['head'],'--',*j['canonical']]);(r/'8096-author-original-source.patch').write_bytes(patch);subprocess.run(['git','apply','--index'],input=patch,check=True)
sys.path[:0]=[str(w/'docs/ai_methodology/skills/review-loop/scripts'),str(w/'scripts')];import review_workspace as op;import runner_cache
prefix='.claude/science/physics-loops/toe-formation-order-derivation-20260913/';keep=[p['path'].removeprefix(prefix) for p in j['paths'] if p['path'].startswith(prefix)];dest=w/'docs/work_history/repo/review_feedback/pr8096-evidence';m=op.archive(w,j['head'],prefix,dest,keep,'pr8096');(r/'8096-author-archive.json').write_text(json.dumps(m,indent=2)+'\n');sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mh=sha(dest/'archive-manifest.json');op.verify_archive(dest,mh)
# All scientific sources/inputs/cache are left byte-identical. The archive and
# receipt provide historical provenance without optional source-note churn.
subprocess.run(['git','add',str(dest)],check=True);paths=g('diff','--cached','--name-only').splitlines();subprocess.run(['python3','scripts/vocab_lint.py','--fix','--report-path',str(r/'8096-author-vocab.json'),*paths],check=True);subprocess.run(['git','add','--',*paths],check=True)
for args in [('diff','--check'),('diff','--cached','--check'),('diff','HEAD','--check')]:subprocess.run(['git',*args],check=True)
for p in j['canonical']:assert sha(w/p)==next(x['sha256'] for x in j['paths'] if x['path']==p)
runner=next(p for p in j['canonical'] if p.endswith('.py'));status=runner_cache.cache_status(runner)
(r/'8096-author-packaging.json').write_text(json.dumps({'base':base,'tree':g('write-tree'),'source_paths':{p:sha(w/p) for p in paths},'archive_manifest_sha256':mh,'original_cache_status':status,'change':'Original scientific note, primary and canonical cache retained byte-identical; all10 historical files preserved as raw identity payloads. No new execution. Independent review still required for any evidence reuse.'},indent=2)+'\n');print(len(paths),g('write-tree'),'original cache',status)
