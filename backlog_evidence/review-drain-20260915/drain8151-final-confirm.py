import pathlib,json,hashlib,subprocess,gzip,sys,re
r=pathlib.Path('/private/tmp/review-drain-20260915');w=r/'drain-author-slot';sha=lambda b:hashlib.sha256(b).hexdigest()
def load(n):return json.loads((r/n).read_text())
def git(*a):return subprocess.check_output(['git','-C',str(w),*a])
cold=load('drain8151-preexecution-review.json');f=load('drain8151-author-final-freeze.json');e=load('drain8151-execution-8151.json');assert git('write-tree').decode().strip()==f['tree']=='c2476d552344e829c735e332dfd822af2bcee7fc';assert not git('diff','--name-only')
cache='logs/runner-cache/'+pathlib.Path(e['runner']).stem+'.txt';assert git('diff','--name-status',cold['source']['tree'],f['tree']).decode().strip()=='A\t'+cache
for x in cold['source']['paths']:assert sha((w/x['path']).read_bytes())==x['sha256']
for entries in cold['inputs'].values():
 for x in entries:assert sha((w/x['path']).read_bytes())==x['sha256']
for p,h in f['source_paths'].items():assert sha((w/p).read_bytes())==h
for x in cold['original_dispositions']:assert sha(gzip.decompress((w/x['final_path']).read_bytes()))==x['original_sha256']
assert e['exit_code']==0 and e['status']=='ok' and e['stderr']=='' and 'TOTAL: PASS=20 FAIL=0' in e['stdout'];assert e['elapsed_sec']<e['timeout_sec']==180
watch=e['whole_tree_watchdog'];assert watch['samples']>0 and not watch['violations'] and watch['peak_tree_rss_bytes']<watch['limit_bytes']==3221225472
assert sha((r/'drain8151-capture.py').read_bytes())==e['capture_script_sha256']
sys.path.insert(0,str(w/'scripts'));import runner_cache as c
assert c.cache_status(w/e['runner'])=='fresh';text=(w/cache).read_text();assert e['stdout'].strip() in text;fp=c.declared_input_fingerprint(w/e['runner']);assert fp==cold['actual_api']['declared_input_fingerprint'] and fp in text
old=next((r/'drain8153-originals/8151/logs/runner-cache').glob('*.txt')).read_text()
def nums(s):return [re.findall(r'\d+(?:\.\d+)?',l) for l in s.splitlines()if re.match(r'PASS: [BCD]\d+ ',l)]
assert nums(old)==nums(e['stdout'])
for row in cold['original_dispositions']:
 if row['path'].startswith('logs/runner-cache/'):
  row['current_execution_cache']={'path':cache,'sha256':sha((w/cache).read_bytes())};row['disposition']+=' Original cache retained as historical; this fresh cache supersedes it for corrected source only.'
refs=cold['references'][:]
for n in ['drain8151-preexecution-review.json','drain8151-execution-8151.json','drain8151-capture.py','drain8151-author-final-freeze.json']:
 refs.append(dict(path=str(r/n),sha256=sha((r/n).read_bytes())))
out=dict(cold);out.pop('capture',None);out.update(status='FINAL SOURCE PASS: PARTIAL POSITIVE SALVAGE AND EXPLICIT CONDITIONAL IMPLICATIONS',source={'base':f['base'],'commit':f['base'],'tree':f['tree'],'paths':[dict(path=p,sha256=h)for p,h in f['source_paths'].items()],'deleted_paths':[]},execution={'receipt':str(r/'drain8151-execution-8151.json'),'pass':20,'fail':0,'exit_code':0,'stderr':'','elapsed_sec':e['elapsed_sec'],'timeout_sec':180,'watchdog':watch,'cache_path':cache,'cache_sha256':sha((w/cache).read_bytes()),'input_fingerprint':fp,'cache_status':'fresh'},output_comparison='All numerical tokens in mathematical B/C/D check lines match historical output exactly. Changed labels explicitly describe finite comparisons, arithmetic and deferred phase conclusion. Only cache added after cold confirmation; all26 original cold source bytes and actual inputs unchanged.',scope='Retain spectrum, real reflection identity, all-direction count, finite controls and explicitly conditional contour/limit implications. Uniform bad-bond estimate is not proved; unconditional threshold216/phase coexistence and state-orbit assertions not accepted. Preserve original PR8151 branch and all22 exact original versions. No audit verdict.',references=refs,final_cache_preflight_owner='root; reviewer performed lightweight freshness API verification only, no versioned preflight or science rerun')
p=r/'drain8151-final-review.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n');(r/'drain8151-final-review.md').write_text('# PR8151 final source review\n\nPASS for partial positive salvage and explicit conditional implications at tree `'+f['tree']+'`. Sole capture20/0,29.60103seconds, sampled peak1,812,561,920bytes under180seconds/3GiB. Only fresh cache added; source/input hashes and all22 archived originals verified. Mathematical output numbers match historical output.\n\nUnconditional phase/threshold216 and orbit conclusions remain unaccepted. Preserve the original branch and proof. Root owns the sole final versioned cache preflight; no audit verdict or reviewer rerun.\n');print(sha(p.read_bytes()))
