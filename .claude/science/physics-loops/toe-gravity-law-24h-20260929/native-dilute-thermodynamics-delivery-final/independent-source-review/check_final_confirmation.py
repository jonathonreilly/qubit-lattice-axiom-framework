import ast,datetime,gzip,hashlib,json,pathlib,subprocess,sys
R=pathlib.Path.cwd(); P=R/'.claude/science/physics-loops/native-dilute-thermodynamics-20260930'; C=P/'review-correction'; O=R/'independent-source-review'
def sha(b):return hashlib.sha256(b).hexdigest()
def git(*a):return subprocess.check_output(['git',*a])
def read(p):return (R/p).read_bytes()
base='ea3d4f6236160233f6f9e183b4b6eb5ba3252607';old='e4b261bde8908d41acbf69663901ac96164080bf';head=git('rev-parse','HEAD').decode().strip();tree=git('rev-parse','HEAD^{tree}').decode().strip()
assert head=='d6197654f4100621083f72a421da2b8aff6b7391';assert tree=='09a725e9af7608b63232d23b586877b74a27b7d0'
assert not git('diff','HEAD','--');assert not git('diff','--cached','--')
stop=pathlib.Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929/STOP_REQUESTED.json');assert not stop.exists()
paths=git('diff','--name-only',base,head).decode().splitlines();assert len(paths)==191
m=json.loads(pathlib.Path('/Users/jonBridger/.codex/worktrees/toe-axiom-campaign-20260929/New Axioms Lets Go/.claude/science/physics-loops/toe-gravity-law-24h-20260929/native-dilute-thermodynamics-milestone-cold-read/FINAL_STAGED_MAP.json').read_text());assert m['tree']==tree;assert {x['path']:x['sha256'] for x in m['paths']}=={p:sha(read(p)) for p in paths}
orig=json.loads((O/'ORIGINAL_DISPOSITIONS.json').read_text());rec=json.loads((C/'ORIGINAL_158_PATH_RECOVERY.json').read_text());assert len(rec['paths'])==158
mapped=[]; changed=[]
for r in rec['paths']:
 p=r['original_path'];b=read(r['recovery_path']);b=gzip.decompress(b) if r['encoding']=='gzip' else b
 assert sha(b)==r['original_sha256'];assert b==git('show',old+':'+p)
 q=next(x for x in orig['original_dispositions'] if x['original_path']==p).copy();q.update(final_sha256=sha(read(p)),recovery=r['recovery_path'],recovery_encoding=r['encoding'],recovery_sha256=sha(read(r['recovery_path'])))
 if sha(read(p))!=sha(b):changed.append(p);q['disposition']='accepted narrow evidence wording correction or actual refreshed primary cache; old exact bytes retained at recovery'
 mapped.append(q)
assert len(changed)==6
for p in paths:assert read(p)==git('show',head+':'+p)
copies=list((P/'independent-source-review').iterdir());assert len(copies)==9
for p in copies:assert p.read_bytes()==(O/p.name).read_bytes()
runner='scripts/native_dilute_thermodynamics_2026_09_30.py';assert ast.dump(ast.parse(read(runner)))==ast.dump(ast.parse(git('show',old+':'+runner)))
pre=json.loads((C/'UNIT_V2_PREEXECUTION.json').read_text());assert len(pre['source']['paths'])==164
pre_deltas=[]
for x in pre['source']['paths']:
 assert sha(git('show',pre['source']['tree']+':'+x['path']))==x['sha256']
 if sha(read(x['path']))!=x['sha256']:pre_deltas.append(x['path'])
assert set(pre_deltas)=={str(P.relative_to(R)/'PR_BODY_DRAFT.md'),'logs/runner-cache/native_dilute_thermodynamics_2026_09_30.txt'}
inputs=[]
for kind,entries in pre['inputs'].items():
 for x in entries:assert sha(read(x['path']))==x['sha256'];inputs.append(dict(x,kind=kind))
for prefix in ['PREFLIGHT','REFRESH_PRIMARY']:
 d=json.loads((C/(prefix+'.execution.json')).read_text());assert d['exit_code']==0 and d['termination_reason'] is None
 for p,h in d['capture_sha256'].items():assert sha((C/p).read_bytes())==h
receipt=json.loads((C/'PREFLIGHT.stdout.txt').read_text());assert receipt['mechanical_status']=='ok' and receipt['cache_checked'] is False;assert receipt['record_sha256']==sha((C/'UNIT_V2_PREEXECUTION.json').read_bytes())
result=json.loads((C/'REFRESH_CACHE_RESULT.json').read_text());stdout=(C/'REFRESH_PRIMARY.stdout.txt').read_text();assert result['result']['stdout']==stdout==(P/'primary/run.stdout.txt').read_text();assert 'TOTAL: PASS=7 FAIL=0' in stdout
sys.path.insert(0,str(R/'scripts'));import runner_cache
fresh=runner_cache.cache_status(runner);assert fresh=='fresh'
pr=json.loads(subprocess.check_output(['gh','pr','view','9401','--json','headRefOid,baseRefName,state,url,mergedAt']));assert pr['headRefOid']==base and pr['state']=='OPEN' and pr['baseRefName']=='main'
remote=subprocess.check_output(['git','ls-remote','origin','refs/heads/main']).decode().strip();assert remote.split()[0]=='fb5da8dd5ac1b001b0c619070f27e5b7f8fe4be7'
final=[]
for p in paths:
 x=next((x for x in mapped if x['original_path']==p),None)
 if x:role=x['role_and_rationale'];scope=x['actual_read_scope']+'; final bytes compared with original, changed text separately read'
 elif '/independent-source-review/' in p:role='Lossless prior same-session reviewer record, not new independent endorsement';scope='Own original record and full byte identity comparison'
 elif p.endswith('.gz'):role='Lossless original-byte recovery';scope='Decompressed and compared in full with original tree'
 elif p.endswith('FINAL_DELIVERY_ADDENDUM.md'):role='Final author chronology and bounded delivery status';scope='Full text read'
 else:role='Correction, preflight or actual cache-refresh provenance; no new science';scope='Narrative and worker full read; structured records fully parsed, identities/capture hashes and relevant fields checked; large path arrays programmatically verified'
 final.append({'path':p,'sha256':sha(read(p)),'disposition':'accepted for source-only bounded unit','role_and_rationale':role,'actual_read_scope':scope})
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer_session':'/root/native_thermodynamics_source_review','head':head,'tree':tree,'base':base,'verdict':'SOURCE-ONLY PASS WITH BOUNDED CLAIMS','original_dispositions':mapped,'final_dispositions':final,'input_identities':inputs,'changed_original_paths':changed,'preflight_to_final_deltas':pre_deltas,'cache_status':fresh,'runner_sha256':sha(read(runner)),'cache_sha256':sha(read('logs/runner-cache/native_dilute_thermodynamics_2026_09_30.txt')),'pr9401':pr,'remote_main':remote,'stop_absent':True,'proofs_and_primary_AST_unchanged':True,'reviewer_copies_identical':9,'combined_gate_claimed':False,'final_schema2_cache_receipt_claimed':False}
(O/'FINAL_DISPOSITIONS_AND_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['original_dispositions','final_dispositions','input_identities']},indent=2))
