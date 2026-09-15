from pathlib import Path
import json,subprocess,hashlib,sys,gzip
w=Path.cwd();r=w.parent;j=json.loads((r/'check8097/inventory.json').read_text());g=lambda *a:subprocess.check_output(['git',*a],text=True).strip();assert not g('status','--porcelain');base=g('rev-parse','HEAD')
patch=subprocess.check_output(['git','diff','--binary',j['original_base'],j['head'],'--',*j['canonical']]);(r/'8097-author-original-source.patch').write_bytes(patch);subprocess.run(['git','apply','--index'],input=patch,check=True)
sys.path.insert(0,'/Users/jonBridger/.codex/skills/review-loop/scripts');import review_workspace as op
prefix='.claude/science/physics-loops/native-local-quartic-20260913/';dest=w/'docs/work_history/repo/review_feedback/pr8097-evidence';m=op.archive(w,j['head'],prefix,dest,['REVIEW_HISTORY.md'],'pr8097');(r/'8097-author-archive.json').write_text(json.dumps(m,indent=2)+'\n');sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mh=sha(dest/'archive-manifest.json');op.verify_archive(dest,mh)
# Restore the exact original cache bytes, without executing or rewriting metadata.
compressed=subprocess.check_output(['git','show',j['head']+':'+prefix+'canonical_cache.txt.gz']);raw=gzip.decompress(compressed);cache=w/'logs/runner-cache/native_weyl_local_interaction_covariance_2026_09_13.txt';assert not cache.exists();cache.write_bytes(raw)
sys.path.insert(0,str(w/'scripts'));import runner_cache
runner=next(p for p in j['canonical'] if p.endswith('.py'));status=runner_cache.cache_status(runner)
(r/'8097-historical-cache-restoration.json').write_text(json.dumps({'source_head':j['head'],'original_path':prefix+'canonical_cache.txt.gz','compressed_sha256':hashlib.sha256(compressed).hexdigest(),'decoded_sha256':sha(cache),'restored_path':str(cache.relative_to(w)),'actual_cache_status':status,'new_execution':False,'metadata_rewritten':False,'requires_independent_scientific_review':True},indent=2)+'\n')
assert status=='fresh',status
subprocess.run(['git','add','--',*j['canonical'],str(dest),str(cache)],check=True);paths=g('diff','--cached','--name-only').splitlines()
for args in [('diff','--check'),('diff','--cached','--check'),('diff','HEAD','--check')]:subprocess.run(['git',*args],check=True)
(r/'8097-author-packaging.json').write_text(json.dumps({'base':base,'tree':g('write-tree'),'source_paths':{p:sha(w/p) for p in paths},'archive_manifest_sha256':mh,'change':'Scientific note and primary exact original bytes. Complete historical CAS archive. Exact original gzipped cache decoded, no metadata changes, actual cache_status fresh. No new scientific execution or verdict.'},indent=2)+'\n');print(len(paths),g('write-tree'),status)
