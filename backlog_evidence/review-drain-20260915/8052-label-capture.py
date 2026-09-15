from pathlib import Path
import sys,json,subprocess,hashlib
w=Path('/private/tmp/review-drain-20260915/author-pool/author-backlog');o=Path('/private/tmp/review-drain-20260915');sys.path.insert(0,str(w/'scripts'));import runner_cache as c
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();f=json.loads((o/'8058-author-final-freeze.json').read_text());l=json.loads((o/'8052-label-source-freeze.json').read_text());prepath=Path(sys.argv[1]);pre=json.loads(prepath.read_text());assert pre['mechanical_status']=='ok' and pre['tree']==l['tree'];primary=l['changed_path'];expected=f['source_paths']|f['inputs'];expected[primary]=l['sha256']
for n,h in expected.items():assert sha(w/n)==h,n
receipt=o/'8052-label-author-final-execution.json';assert not receipt.exists();r,cache=c.execute_and_write_cache(primary,180);receipt.write_text(json.dumps(r,indent=2)+'\n');assert r['status']=='ok' and r['exit_code']==0 and not r['stderr'] and 'TOTAL: PASS=93564 FAIL=0' in r['stdout']
mutable={'outputs/native_zero_penalty_l4_delayed_splitting_2026_09_08.json',cache.relative_to(w).as_posix()}
for n,h in expected.items():assert n in mutable or sha(w/n)==h,n
subprocess.run(['git','-C',str(w),'add','--',*mutable],check=True)
for a in (['diff','--check'],['diff','--cached','--check'],['diff','HEAD','--check']):subprocess.run(['git','-C',str(w),*a],check=True)
git=lambda *a:subprocess.check_output(['git','-C',str(w),*a],text=True).strip();paths=git('diff','--cached','--name-only').splitlines();out={'role':'author final source binding after label correction; independent verdict required','base':git('rev-parse','HEAD'),'source_tree':git('write-tree'),'source_paths':{n:sha(w/n) for n in paths},'inputs':{n:sha(w/n) for n in f['inputs']},'executions':[{'pr':8052,'path':str(receipt),'sha256':sha(receipt)}]+[x for x in f['executions'] if x['pr']!=8052],'cache_status':{n:c.cache_status(n) for n in f['cache_status']},'affected_preflight':str(prepath),'affected_preflight_sha256':sha(prepath)};assert all(x=='fresh' for x in out['cache_status'].values());(o/'8058-author-after-label-final-freeze.json').write_text(json.dumps(out,indent=2)+'\n');print(out['source_tree'],r['elapsed_sec'])
