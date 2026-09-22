import pathlib,json,hashlib,subprocess,gzip,sys,re,copy
r=pathlib.Path('/private/tmp/review-drain-20260915');w=r/'integration-resume'
sha=lambda b:hashlib.sha256(b).hexdigest()
load=lambda n:json.loads((r/n).read_text())
g=lambda *a:subprocess.check_output(['git','-C',str(w),*a])
f=load('drain8161c-author-final-freeze.json');cold=load('drain8161-correction-cold-v2.json');draft=load('drain8161-correction-draft-v2.json');old=load('drain8161-final-review.json')
assert g('write-tree').decode().strip()==f['tree']=='0f2fbf00b1c24108040992329fa2098c63fb8623'
assert g('rev-parse','HEAD').decode().strip()==f['base']
assert set(g('diff','--cached','--name-only').decode().splitlines())==set(f['source_paths'])
for p,h in f['source_paths'].items():assert sha((w/p).read_bytes())==h==sha(g('show',':'+p)),p
for p,h in f['inputs'].items():assert sha((w/p).read_bytes())==h,p
before={x['path']:x['sha256'] for x in cold['source']['paths']};assert set(before)==set(f['source_paths'])
changed=[p for p in before if before[p]!=f['source_paths'][p]]
assert len(changed)==4 and all(p.startswith('logs/runner-cache/') and 'coupled' not in p for p in changed)
disp=copy.deepcopy(old['original_dispositions']);assert len(disp)==47
for d in disp:
 b=g('show',d['recovery']);a=(w/d['final_path']).read_bytes();assert sha(b)==d['original_sha256'];assert sha(a)==d['final_sha256'];assert gzip.decompress(a)==b
 d['disposition']=d['disposition'].replace('characteristic identity kept as owned current supporting proof','characteristic identity kept verbatim in the canonical Gauss owner appendix')
proof='ROTOR_FIXED_COUPLING_GAUSS_CHARACTERISTIC_IDENTITY_SUPPORTING_PROOF_2026-09-16.md'
assert not (w/'docs'/proof).exists()
for p in ['docs/audit/scripts/build_citation_graph.py','scripts/audit_packet_script_deps.py']:assert proof not in (w/p).read_text()
sys.path.insert(0,str(w/'scripts'));import runner_cache as c
ex=[]
for e in f['executions']:
 p=pathlib.Path(e['receipt']);assert sha(p.read_bytes())==e['sha256'];v=json.loads(p.read_text());runner=v['runner'];cache='logs/runner-cache/'+pathlib.Path(runner).stem+'.txt';s=(w/cache).read_text()
 assert c.cache_status(runner)=='fresh';assert v['status']=='ok' and v['exit_code']==0 and not v['stderr'];assert v['stdout'].strip() in s
 wd=v['whole_tree_watchdog'];assert not wd['violations'] and wd['samples']>0 and wd['limit_bytes']==536870912 and wd['peak_tree_rss_bytes']<=wd['limit_bytes']
 assert 'runner_sha256: '+sha((w/runner).read_bytes()) in s
 fp=c.declared_input_fingerprint(runner);assert 'input_fingerprint_sha256: '+fp in s
 counts=re.search(r'^TOTAL: PASS=(\d+) FAIL=0$',v['stdout'],re.M);assert counts
 ex.append({'runner':runner,'completed_families':int(counts[1]),'failures':0,'elapsed_sec':v['elapsed_sec'],'peak_sampled_process_tree_rss_bytes':wd['peak_tree_rss_bytes'],'timeout_sec':v['timeout_sec'],'memory_cap_bytes':wd['limit_bytes'],'cache':cache,'cache_sha256':sha((w/cache).read_bytes()),'input_fingerprint':fp,'receipt':e})
assert next(x for x in ex if 'coupled' in x['runner'])['cache_sha256']=='fa4d966663fe6f24b92b78267587797175179a74c04c61734e5d241c298f6182'
refs=[{'path':str(r/n),'sha256':sha((r/n).read_bytes())} for n in ['drain8161-original-review.json','drain8161-authority-read-appendix.json','drain8161-authority-identity-clarifier.json','drain8161-final-review.json','drain8161-postintegration-compatibility-finding.json','drain8161-correction-cold-v2.json','drain8161-correction-draft-v2.json','drain8161-correction-cheap-v2.json','drain8161c-author-final-freeze.json','drain8161c-capture.py']]
out={'schema_version':2,'reviewer':'/root/review_8161','verdict':'PASS FOR CORRECTED SOURCE AND BOUNDED EVIDENCE','authority':old['authority'],'source':{'base':f['base'],'commit':f['base'],'tree':f['tree'],'paths':[{'path':p,'sha256':h} for p,h in sorted(f['source_paths'].items())],'deleted_paths':[]},'original_head':old['original_head'],'original_delta_base':old['original_delta_base'],'original_dispositions':disp,'inputs':draft['inputs'],'notes':draft['notes'],'supporting_proofs':[],'appendix_ownership':cold['appendix_ownership'],'executions':ex,'references':refs,'source_preservation':{'originals_verified':47,'staged_paths_verified':65,'changes_since_cold':changed,'result':'All noncache source and input identities unchanged from approved correction cold. Four changed-input caches replaced; coupled cache/source/inputs exactly reused. Complete diagnostic belongs to Gauss appendix within four notes; separate new proof absent and no orphan helper mapping.'},'findings':[],'numerical_interpretation':old['numerical_interpretation'],'scope':'Same-session narrow correction confirmation reuses complete prior original arguments, authority and affected proof review. Independently checked current disk/index identities, all47 exact original Git/archive bytes, five receipt/stdout/cache fingerprints and actual watchdog evidence. No primary rerun, full pipeline or audit performed. Counts are completed families, not individual assertions. Supplied rotor/CAR/Gaussian/Maxwell/Wilson model bounds do not derive a framework Hamiltonian or fixed-g interacting phase.','remaining':'Root sole final cache and train73a combined integration gate remain pending; this is not an audit/retained-grade verdict.'}
p=r/'drain8161c-final-review.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
m=r/'drain8161c-final-review.md';assert not m.exists();m.write_text('# PR8161 corrected final review\n\nPASS for corrected source and bounded evidence at tree `'+f['tree']+'` on base `'+f['base']+'`.\n\nAll65 staged path identities and47 original archive payloads verified against Git. The complete characteristic identity remains verbatim in the canonical Gauss appendix, within four notes; separate supporting_proofs is empty and orphan mappings are absent.\n\nOnly four cache files changed since approved correction cold. Four corrected captures pass4/3/2/3 completed families with zero failures, within180/180/180/120 seconds and512MiB sampled process-tree limits. Coupled3/0 cache/source/inputs are exactly reused. All five receipt/stdout and live cache fingerprints agree. These counts are families, not individual assertions.\n\nPrior full mathematical review and explicit supplied-model limits remain applicable. No primaries, full pipeline or audit were rerun by this reviewer. Root final cache and train73a combined gate remain pending.\n')
print(json.dumps({'report':str(p),'sha256':sha(p.read_bytes()),'markdown_sha256':sha(m.read_bytes()),'changed':changed,'executions':ex},indent=2))
