from pathlib import Path
import ast,json,hashlib,re,subprocess
R=Path('/private/tmp/review-drain-20260915');W=R/'drain-author-slot';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ref=lambda p:dict(path=str(p),sha256=sha(p))
def put(n,s):
 p=R/n;assert not p.exists();p.write_text(s if isinstance(s,str) else json.dumps(s,indent=2,ensure_ascii=False)+'\n');return p
j=json.loads((R/'drain8175-author-prepared-v2.json').read_text());d=json.loads((R/'drain8175-source-input-discovery-v2.json').read_text());h=json.loads((R/'drain8175-author-handoff-v2.json').read_text());early=json.loads((R/'drain8175-early-review-v2.json').read_text())
assert sha(R/'drain8175-early-review-v2.json')=='02359b04e8bfb23212e3b3fd90061d87ef80d015562bb73302ff4bde508363ad'
assert early['source']==j['source']
for x in j['source']:assert sha(W/x['path'])==x['sha256']
put('drain8175-adapter-authority-v1.json',dict(schema_version=1,base=j['base'],authority=h['authority'],context=[]))
names=['drain8175-author-prepared-v2.json','drain8175-source-freeze-v2.json','drain8175-author-handoff-v2.json','drain8175-author-dispositions-v2.json','drain8175-author-corrections-v2.patch','drain8175-source-input-discovery-v2.json','drain8175-resource-plan-v2.json','drain8175-review-original.json','drain8175-review-original.md','drain8175-early-review-v2.json','drain8175-early-review-v2.md','drain8175-adapter-authority-v1.json']
refs=[ref(R/n) for n in names]+[ref(Path(early['independent_check'][k])) for k in ['path','output']]
bp=put('drain8175-adapter-bindings-v1.json',refs)
b=(R/'drain8173-build-staged-draft-v1.py').read_text().replace('8173','8175').replace('review-draft-slot','drain-author-slot').replace('-v3.json','-v2.json').replace('dispositions-v1.json','dispositions-v2.json')
b=b.replace('len(f)==25','len(f)==34').replace("+discovery['context_parents']",'').replace("|{e['path'] for e in discovery['context_parents']}",'').replace("d['readable_history']","d['deferred_science']")
a=b.index('        assert sha(rp)==');z=b.index('        owner=json.loads',a)
b=b[:a]+'''        assert sha(rp)=='02359b04e8bfb23212e3b3fd90061d87ef80d015562bb73302ff4bde508363ad'
        assert review['kind']=='same-session-early-affected-review-not-final-source-pass' and review['reviewer_session']=='/root/review_8175'
        assert review['pr']==8175 and review['verdict']=='CLEAR FOR STAGING AND COLD CAPTURE' and not review['findings']
        assert review['original_head']==d['head'] and review['source']==f
        assert review['preservation']['all_original_paths']==28 and review['preservation']['source_additions']==34
        assert review['prepared_sha256']==sha(R/'drain8175-author-prepared-v2.json') and review['source_freeze_sha256']==sha(R/'drain8175-source-freeze-v2.json')
        assert review['handoff_sha256']==sha(R/'drain8175-author-handoff-v2.json')
        ec=review['execution_clearance'];assert ec['cold_primary_allowed'] is True and ec['wall_limit_seconds']==60 and ec['process_tree_rss_limit_bytes']==402653184 and ec['expected_primary_checks']==20 and ec['helpers']==[] and ec['input_count']==3
        assert ec['runner_sha256']==discovery['primary_sha256'] and ec['historical_search_reruns'] is False
''' +b[z:]
b=b.replace("['dispositions'];old=","['path_dispositions'];old=").replace('len(old)==len(mapping)==20','len(old)==len(mapping)==28')
b=b.replace("o=old[e['original_path']];assert","o=old[e['original_path']]['head'];assert")
b=b.replace("        sys.path[:0]=", "        delta=manifest['original_delta'];assert sha(W/delta['path'])==delta['sha256']\n        assert hashlib.sha256(gzip.decompress((W/delta['path']).read_bytes())).hexdigest()==delta['decoded_sha256']\n        assert (R/'drain8175-original/original.patch').read_bytes()==gzip.decompress((W/delta['path']).read_bytes())\n        existing={Path(p).name for p in git('ls-files','docs').splitlines()}\n        newdocs=[e['path'] for e in f if e['path'].startswith('docs/') and Path(e['path']).name not in ['README.md','SKILL.md']]\n        assert not [p for p in newdocs if Path(p).name in existing] and len({Path(p).name for p in newdocs})==len(newdocs)\n        sys.path[:0]=")
a=b.index("        rationale='");z=b.index('\n        handoff=',a)
b=b[:a]+"        rationale='Complete finite marked-automaton constructions, conditional finite pole-assignment identity and exact rational recursion certificates. All fixtures and certificate mathematics retained; only B3 exact per-witness period target repaired. Framework memo is context authority; product-law input is context only, no theorem import. Complete corrected negative argument and original note remain readable deferred science, no supporting-proof edge or universal upper budget; branch retention required.'"+b[z:]
b=b.replace("original_dispositions=rows,claim_dispositions", "original_dispositions=rows,original_delta=delta,claim_dispositions")
b=b.replace('all20 original payloads','all 28 original payloads').replace('complete corrected finite proofs','complete finite constructions and conditional accounting proofs')
b=re.sub(r"BINDINGS_SHA256='[0-9a-f]+'",f"BINDINGS_SHA256='{sha(bp)}'",b)
compile(b,'builder','exec');put('drain8175-build-staged-draft-v1.py',b)
run=W/j['primaries'][0];tree=ast.parse(run.read_text());mut=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and n.targets[0].id=='MUTATION_GATE')
p=json.loads((R/'drain8173-capture-plan-v1.json').read_text());p.update(primary=j['primaries'][0],primary_sha256=sha(run),runtime_inputs=d['runtime_inputs'],input_fingerprint=d['input_fingerprint'],cache_destination='logs/runner-cache/'+run.stem+'.txt',completed_check_count=20,all_mutation_definitions=mut,source_resource_plan=ref(R/'drain8175-resource-plan-v2.json'),recovery_and_source_counts=dict(source_paths=34,original_payloads=28,full_original_delta=True))
p['mathematical_controls']={'period_counts_wrong':dict(expected_family='B',expected_failed_tags=['B3'],expected_exit_code=1,expected_total=dict(passed=19,failed=1),mechanism='Keep total4 unchanged but substitute expected per-witness distribution(2,2,0) for the actual(2,1,1); exact B3 must reject, all other checks unchanged.')}
p['not_proposed_packaging_mutations']=[n for n in mut if n!='period_counts_wrong'];p['not_proposed_other_mutations_reason']='Original reviewer cleared only the newly affected period-count mutation; unchanged historical mathematical mutation routes need no routine reruns.'
p['scientific_scope']='Finite witnessed accounting and rational arithmetic only. One unchanged seeded300-cone fixture belongs to the primary; no separate historical search/sampler/control run. No global sharpness or formal negative-certification verdict.'
p['mutation_limits']['sequence']='Only period_counts_wrong once after preserved baseline receipt, serial; no baseline repeat, other mutation census, implicit retry or cap increase.'
pp=put('drain8175-capture-plan-v1.json',p)
for kind in ['capture','mutation-capture']:
 s=(R/f'drain8173-{kind}-v1.py').read_text().replace('8173','8175').replace('review-draft-slot','drain-author-slot').replace('early-review-v3.json','early-review-v2.json').replace('prepared-v3','prepared-v2')
 s=s.replace('9ad28d3417d6c1a3b10d92dc7027ee029c39a58d98e042de25ed50f29e04adb0','02359b04e8bfb23212e3b3fd90061d87ef80d015562bb73302ff4bde508363ad')
 s=s.replace('TOTAL: PASS=14 FAIL=0','TOTAL: PASS=20 FAIL=0').replace('TOTAL: PASS=13 FAIL=1','TOTAL: PASS=19 FAIL=1').replace('==13','==19').replace('completed_checks=14,passed=13','completed_checks=20,passed=19').replace('len(mutations)==7','len(mutations)==10').replace('Only the five reviewed mathematical corruption routes are proposed here','Only the newly affected period_counts_wrong route is authorized here')
 s=re.sub(r"PLAN_SHA256='[0-9a-f]+'",f"PLAN_SHA256='{sha(pp)}'",s)
 assert 'COLD_CLEARANCE_BINDING = None' in s;compile(s,kind,'exec');put(f'drain8175-{kind}-v1.py',s)
assert not subprocess.check_output(['git','-C',str(W),'diff','--name-only'],text=True);assert not subprocess.check_output(['git','-C',str(W),'diff','--cached','--name-only'],text=True)
assert set(subprocess.check_output(['git','-C',str(W),'ls-files','--others','--exclude-standard'],text=True).splitlines())=={x['path'] for x in j['source']}
for x in j['source']:assert sha(W/x['path'])==x['sha256']
files=['drain8175-build-staged-draft-v1.py','drain8175-capture-v1.py','drain8175-mutation-capture-v1.py','drain8175-capture-plan-v1.json','drain8175-adapter-bindings-v1.json','drain8175-adapter-authority-v1.json']
put('drain8175-adapter-verification-v1.json',dict(schema_version=1,kind='static-adapter-preparation-not-execution',references=[ref(R/f) for f in files],source_unchanged=True,source_count=34,original_count=28,original_delta_bound=True,builder_executed=False,staging=False,preflight=False,primary_runs=0,mutation_runs=0,simulation_runs=0,cold_binding=None,required_future_binding='Actual original-session staged cold report hash/predicates/tree in new immutable adapter; completed cheap receipt bound to same record/tree',actual_primary_contract=dict(stdout_checks=20,json_outputs=[],runtime_inputs=3,helpers=[],limits=dict(seconds=60,bytes=402653184,measured_corrected_source=False)),only_mutation=dict(name='period_counts_wrong',expected_failed_tags=['B3'],passed=19,failed=1,exit_code=1),raw_preservation='Transparent execute_runner wrapper serializes actual returned result before original cache API identity rejection and returns same object. Existing API and additional whole-source stat-generation checks remain enforced.',no_mutable_pool_reviewer_cache_reference=True))
print(json.dumps({f:sha(R/f) for f in files+['drain8175-adapter-verification-v1.json']},indent=2))
