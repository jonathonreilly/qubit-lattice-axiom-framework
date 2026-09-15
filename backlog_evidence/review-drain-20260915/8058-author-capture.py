from pathlib import Path
import sys,json,hashlib,subprocess
w=Path('/private/tmp/review-drain-20260915/author-pool/author-backlog');o=Path('/private/tmp/review-drain-20260915');sys.path.insert(0,str(w/'scripts'));import runner_cache as c
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();f=json.loads((o/'8058-author-preexecution.json').read_text());prepath=Path(sys.argv[1]);pre=json.loads(prepath.read_text());assert pre['mechanical_status']=='ok' and pre['tree']==f['source_tree'] and not pre['cache_checked']
def verify():
 for n,h in (f['source_sha256']|f['input_sha256']).items():assert sha(w/n)==h,n
verify();records=[];caches=[]
for pr,primary,count in zip((8052,8053,8058),f['primaries'],(93564,7960,40)):
 receipt=o/f'{pr}-group-author-final-execution.json';assert not receipt.exists(),str(receipt)
 r,cachepath=c.execute_and_write_cache(primary,180);receipt.write_text(json.dumps(r,indent=2)+'\n');records.append({'pr':pr,'path':str(receipt),'sha256':sha(receipt)})
 assert r['status']=='ok' and r['exit_code']==0 and not r['stderr'] and f'TOTAL: PASS={count} FAIL=0' in r['stdout'],r
 verify();assert c.cache_status(primary)=='fresh';caches.append(cachepath.relative_to(w).as_posix());print(pr,count,r['elapsed_sec'],flush=True)
subprocess.run(['git','-C',str(w),'add','--',*f['original_output_sha256'],*caches],check=True)
for args in (['diff','--check'],['diff','--cached','--check'],['diff','HEAD','--check']):subprocess.run(['git','-C',str(w),*args],check=True)
git=lambda *a:subprocess.check_output(['git','-C',str(w),*a],text=True).strip();paths=git('diff','--cached','--name-only').splitlines();r={'role':'author final binding; no independent verdict','base':git('rev-parse','HEAD'),'source_tree':git('write-tree'),'source_paths':{n:sha(w/n) for n in paths},'inputs':f['input_sha256'],'executions':records,'cache_status':{n:c.cache_status(n) for n in f['primaries']},'preflight_result':str(prepath),'preflight_result_sha256':sha(prepath)};(o/'8058-author-final-freeze.json').write_text(json.dumps(r,indent=2)+'\n');print('Final',r['source_tree'],flush=True)
