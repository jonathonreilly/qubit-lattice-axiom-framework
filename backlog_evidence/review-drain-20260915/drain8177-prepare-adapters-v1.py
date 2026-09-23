from pathlib import Path
import ast,json,hashlib,re,subprocess
R=Path('/private/tmp/review-drain-20260915');W=R/'drain-author-slot';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ref=lambda p:dict(path=str(p),sha256=sha(p))
def put(n,x):
 p=R/n;assert not p.exists();p.write_text(x if isinstance(x,str) else json.dumps(x,indent=2)+'\n');return p
j=json.loads((R/'drain8177-author-prepared-v2.json').read_text());d=json.loads((R/'drain8177-source-input-discovery-v2.json').read_text());h=json.loads((R/'drain8177-author-handoff-v2.json').read_text());e=json.loads((R/'drain8177-early-review-v2.json').read_text());eh=sha(R/'drain8177-early-review-v2.json');assert e['source']==j['source']
for x in j['source']:assert sha(W/x['path'])==x['sha256']
put('drain8177-adapter-authority-v1.json',dict(schema_version=1,base=j['base'],authority=h['authority'],context=[]))
names=['author-prepared-v2.json','source-freeze-v2.json','author-handoff-v2.json','author-dispositions-v1.json','author-corrections-v2.patch','source-input-discovery-v2.json','resource-plan-v2.json','review-original.json','review-original.md','early-review-v2.json','early-review-v2.md','adapter-authority-v1.json']
refs=[ref(R/('drain8177-'+n)) for n in names]+[e['verification_artifact']];bp=put('drain8177-adapter-bindings-v1.json',refs)
b=(R/'drain8176-build-staged-draft-v1.py').read_text().replace('8176','8177').replace('review-draft-slot','drain-author-slot').replace('len(f)==35','len(f)==56').replace('len(mapping)==29','len(mapping)==50')
for stem in ['author-prepared','source-freeze','author-handoff','source-input-discovery','resource-plan','early-review']:b=b.replace(stem+'-v1.json',stem+'-v2.json')
a=b.index('        assert sha(rp)==');z=b.index('        owner=json.loads',a)
b=b[:a]+f'''        assert sha(rp)=='{eh}'
        assert review['schema_version']==1 and review['kind']=='same-session-affected-source-review-not-landing-pass'
        assert review['reviewer']=='/root/review_8177' and review['pr']==8177 and review['iteration']==2
        assert review['verdict']=='CLEAR FOR COLD REVIEW AND BOUNDED EVIDENCE CAPTURE' and review['new_material_findings']==[]
        assert review['original_head']==d['head'] and review['source']==f
        assert review['source_freeze_sha256']==sha(R/'drain8177-source-freeze-v2.json') and review['handoff_sha256']==sha(R/'drain8177-author-handoff-v2.json')
        vv=review['verification'];assert vv['frozen_sources']==56 and vv['original_payloads_verified']==50 and vv['delta_verified'] and vv['eight_certificates_unchanged']
        assert vv['literal_input_pins_verified']=={{e['path']:e['sha256'] for e in discovery['runtime_inputs']}}
        ec=review['resource_plan_clearance'];assert ec['baseline_runs']==ec['targeted_mutation_runs']==1 and ec['targeted_mutation']=='predecessor_profile_wrong'
        assert ec['expected_baseline']=='TOTAL: PASS=18 FAIL=0' and ec['expected_mutation']=='TOTAL: PASS=17 FAIL=1; C1 only'
        assert ec['wall_seconds_per_run']==plan['timeout_seconds']==120 and ec['sampled_process_tree_memory_bytes']==plan['memory_limit_bytes']==402653184
''' +b[z:]
b=b.replace("o=old[e['original_path']]['head']","o=old[e['original_path']]['original']['head']").replace('drain8177-original/delta.patch','drain8177-original/original.delta').replace('all 29 original','all 50 original').replace('declared_timeout_for(W/runner)==60','declared_timeout_for(W/runner)==120')
a=b.index("        rationale='");z=b.index('\n        handoff=',a)
b=b[:a]+"        rationale='Complete finite extension/seed/induction proofs with explicit sufficient H implication, corrected finite profiles, and weight-preserving relaxed lifted-tree injection. Eight rational points unchanged; no exact occupancy count or universal restricted admissibility. Four actual runtime source pins; product model and landed two-level full-slot/application parents explicitly scoped; no unlanded sibling import. Complete50original recovery and readable negative/history limitations; branch retention required.'"+b[z:]
# The future base supplies its CURRENT APIs, methodology and registry bytes.
needle="        tools_before=bind(tooling);verify();"
b=b.replace(needle,"""        assert len(tooling[:5])==5 and len(set(tooling))==len(tooling)
        # Bind installed-at-base tooling/methodology, never reuse old discovery tooling hashes.
        for p in set(tooling)|context:
            if p in {e['path'] for e in f}:continue
            committed=subprocess.check_output(['git','-C',str(W),'show',a.expected_base+':'+p])
            assert sha(W/p)==hashlib.sha256(committed).hexdigest(), 'Tool/context differs from fresh base: '+p
        tools_before=bind(tooling);verify();""")
b=b.replace("api=dict(discovery,actual_current_base=a.expected_base,source_tree=stagedtree)","api=dict(discovery,actual_current_base=a.expected_base,source_tree=stagedtree,current_tooling=tools_before,current_context=bind(context),current_api=dict(declared_inputs=list(c.declared_input_paths(W/runner)),timeout=c.declared_timeout_for(W/runner),fingerprint=c.declared_input_fingerprint(W/runner),citations=cites,graph_helpers=list(g.helper_runner_paths_for_claim(cid,runner)),packet_helpers=sorted(aapi.transitive_helpers(Path(runner).stem))))")
b=re.sub(r"BINDINGS_SHA256='[0-9a-f]+'",f"BINDINGS_SHA256='{sha(bp)}'",b);compile(b,'builder','exec');put('drain8177-build-staged-draft-v1.py',b)
plan=json.loads((R/'drain8176-capture-plan-v1.json').read_text());runner=W/j['primaries'][0];t=ast.parse(runner.read_text());mut=next(ast.literal_eval(n.value) for n in t.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='MUTATION_GATE')
plan.update(primary=j['primaries'][0],primary_sha256=sha(runner),runtime_inputs=d['runtime_inputs'],input_fingerprint=d['input_fingerprint'],cache_destination='logs/runner-cache/'+runner.stem+'.txt',completed_check_count=18,all_mutation_definitions=mut,source_resource_plan=ref(R/'drain8177-resource-plan-v2.json'),recovery_and_source_counts=dict(source_paths=56,original_payloads=50,full_original_delta=True))
plan['primary_limits']['wall_seconds']=120;plan['mutation_limits']['wall_seconds_each']=120
plan['mathematical_controls']={'predecessor_profile_wrong':dict(expected_family='C',expected_failed_tags=['C1'],expected_exit_code=1,expected_total=dict(passed=17,failed=1),mechanism='Demand ZA profile[-1,-1,-1] at ZB instead of actual[-1,-1,0], preserving all coordinates and DP mathematics.')}
plan['not_proposed_packaging_mutations']=[n for n in mut if n not in plan['mathematical_controls']];plan['not_proposed_other_mutations_reason']='Original same-session reviewer cleared only new exact-profile corruption; unchanged mathematical controls reused.'
plan['scientific_scope']='Finite rooted lemmas and relaxed lifted-tree upper sum. Unchanged140/60tiny-fixture batches remain primary fixtures; no historical MILP/search.'
plan['mutation_limits']['sequence']='Only predecessor_profile_wrong once after preserved baseline; no baseline repeat, retry or cap increase.'
plan['dual_base_guard']='Staging requires explicit expected-base==HEAD==origin/main. Capture requires HEAD==record.source.base==cold.frozen_base, origin/main==cold.reviewed_main, ancestral advance and no changed bound source/input path; actual original reviewer must bind semantic current-main clearance. Any methodology/tooling overlap blocks capture for fresh record/review, never silently accepted.'
pp=put('drain8177-capture-plan-v1.json',plan)
for kind in ['capture','mutation-capture']:
 s=(R/f'drain8176-{kind}-v2.py').read_text().replace('8176','8177').replace('review-draft-slot','drain-author-slot')
 s=re.sub(r'^COLD_CLEARANCE_BINDING = .*$', 'COLD_CLEARANCE_BINDING = None',s,flags=re.M)
 s=s.replace('early-review-v1.json','early-review-v2.json').replace('prepared-v1','prepared-v2').replace('15fa0b9c897716f04ef96791c2b23cb10285dac78d16713873e8a74ba242a77f',eh)
 s=s.replace('TOTAL: PASS=22 FAIL=0','TOTAL: PASS=18 FAIL=0').replace('TOTAL: PASS=21 FAIL=1','TOTAL: PASS=17 FAIL=1').replace('==21','==17').replace('completed_checks=22,passed=21','completed_checks=18,passed=17').replace('len(mutations)==11','len(mutations)==8').replace('Only the three original-reviewer-cleared changed-claim routes are authorized here','Only predecessor_profile_wrong is cleared here')
 s=s.replace('==60','==120').replace('limit_sec=60','limit_sec=120').replace('sys.argv[2],60','sys.argv[2],120')
 s=re.sub(r"PLAN_SHA256='[0-9a-f]+'",f"PLAN_SHA256='{sha(pp)}'",s)
 # Require explicit actual cold predicates for both base identities, not mere adapter literals.
 needle="    b = COLD_CLEARANCE_BINDING\n    assert git"
 s=s.replace(needle,"    b = COLD_CLEARANCE_BINDING\n    assert b['frozen_base'] in b['required_predicates'].values() and b['reviewed_main'] in b['required_predicates'].values(), 'Both base identities must be actual cold-report predicates'\n    assert git")
 assert 'COLD_CLEARANCE_BINDING = None' in s and 'def confirm_reviewed_main' in s;compile(s,kind,'exec');put(f'drain8177-{kind}-v1.py',s)
files=['build-staged-draft-v1.py','capture-v1.py','mutation-capture-v1.py','capture-plan-v1.json','adapter-bindings-v1.json','adapter-authority-v1.json']
assert not subprocess.check_output(['git','-C',str(W),'diff','--cached','--name-only'],text=True)
assert not subprocess.check_output(['git','-C',str(W),'diff','--name-only'],text=True)
assert set(subprocess.check_output(['git','-C',str(W),'ls-files','--others','--exclude-standard'],text=True).splitlines())=={x['path'] for x in j['source']}
for x in j['source']:assert sha(W/x['path'])==x['sha256']
put('drain8177-adapter-verification-v1.json',dict(schema_version=1,kind='syntax-and-guard-review-only-not-execution',references=[ref(R/('drain8177-'+n)) for n in files],source_unchanged=True,source_count=56,original_count=50,cold_binding=None,staging=False,builder_executed=False,primary_runs=0,mutation_runs=0,preflight=False,tooling_rediscovery='Future current-base APIs and five core tool files plus registries and all review-loop references; actual source/context bytes checked against expected-base Git objects',dual_base_guard=plan['dual_base_guard'],raw_preservation='Transparent execute_runner wrapper serializes original full return before execute_and_write_cache postidentity checks and returns unchanged object; exclusive external attempts and full hash/stat snapshots preserved'))
print(json.dumps({n:sha(R/('drain8177-'+n)) for n in files+['adapter-verification-v1.json']},indent=2))
