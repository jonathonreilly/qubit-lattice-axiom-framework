from pathlib import Path
import ast,json,hashlib,re
R=Path('/private/tmp/review-drain-20260915');W=R/'review-draft-slot';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ref=lambda p:dict(path=str(p),sha256=sha(p))
def put(n,x):
 p=R/n;assert not p.exists();p.write_text(x if isinstance(x,str) else json.dumps(x,indent=2)+'\n');return p
j=json.loads((R/'drain8176-author-prepared-v1.json').read_text());d=json.loads((R/'drain8176-source-input-discovery-v1.json').read_text());h=json.loads((R/'drain8176-author-handoff-v1.json').read_text());e=json.loads((R/'drain8176-early-review-v1.json').read_text());eh=sha(R/'drain8176-early-review-v1.json');assert e['source']==j['source']
put('drain8176-adapter-authority-v1.json',dict(schema_version=1,base=j['base'],authority=h['authority'],context=[]))
names=['author-prepared-v1.json','source-freeze-v1.json','author-handoff-v1.json','author-dispositions-v1.json','author-corrections-v1.patch','source-input-discovery-v1.json','resource-plan-v1.json','review-original.json','review-original.md','early-review-v1.json','early-review-v1.md','adapter-authority-v1.json']
refs=[ref(R/('drain8176-'+n)) for n in names]+[e['preservation_receipt']];bp=put('drain8176-adapter-bindings-v1.json',refs)
b=(R/'drain8175-build-staged-draft-v1.py').read_text().replace('8175','8176').replace('drain-author-slot','review-draft-slot').replace('-v2.json','-v1.json').replace('len(f)==34','len(f)==35').replace('len(mapping)==28','len(mapping)==29')
a=b.index("        assert sha(rp)==");z=b.index('        owner=json.loads',a)
b=b[:a]+f'''        assert sha(rp)=='{eh}'
        assert review['kind']=='same-session-early-affected-review-not-final-source-pass' and review['reviewer_session']=='/root/review_8176'
        assert review['pr']==8176 and review['verdict']=='CLEAR FOR STAGING AND COLD CAPTURE' and review['findings']==[]
        assert review['original_head']==d['head'] and review['source']==f
        assert review['source_freeze_sha256']==sha(R/'drain8176-source-freeze-v1.json') and review['handoff_sha256']==sha(R/'drain8176-author-handoff-v1.json')
        assert review['branch_preservation_required'] is True
        ec=review['resource_review'];assert ec['expected_stdout_checks']==22 and ec['changed_mutations']==['isolated_seed_cost_wrong','zb_mark_count_wrong','real_boundary_rounded']
        assert ec['primary_executed_in_affected_review'] is False and ec['science_executed_in_affected_review'] is False
        assert plan['timeout_seconds']==60 and plan['memory_limit_bytes']==402653184
''' +b[z:]
b=b.replace("e['mode']","e['original_mode']").replace("e['git_blob']","e['original_blob']")
# Source freeze rows use mode, original disposition rows use original_mode.
b=b.replace("int(e['original_mode'][-3:],8)","int(e['mode'][-3:],8)")
b=b.replace("final=e['canonical_path']","final=e['final_path']").replace('drain8176-original/original.patch','drain8176-original/delta.patch').replace('all 28 original','all 29 original')
a=b.index("        rationale='");z=b.index('\n        handoff=',a)
b=b[:a]+"        rationale='Complete finite component and single-seed dynamic-program proofs, explicit tree ratios, four supplied-recursion rational points and conditional scalar algebra. Restricted ratio domain,36-mark count and real/integer scope repaired; complete negative implication remains readable deferred science. Framework memo context and product-law context are explicit; no helper, upstream phase theorem or global construction premise. Branch retention required.'"+b[z:]
b=re.sub(r"BINDINGS_SHA256='[0-9a-f]+'",f"BINDINGS_SHA256='{sha(bp)}'",b);compile(b,'builder','exec');put('drain8176-build-staged-draft-v1.py',b)
plan=json.loads((R/'drain8175-capture-plan-v1.json').read_text());runner=W/j['primaries'][0];t=ast.parse(runner.read_text());mut=next(ast.literal_eval(n.value) for n in t.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='MUTATION_GATE')
plan.update(primary=j['primaries'][0],primary_sha256=sha(runner),runtime_inputs=d['runtime_inputs'],input_fingerprint=d['input_fingerprint'],cache_destination='logs/runner-cache/'+runner.stem+'.txt',completed_check_count=22,all_mutation_definitions=mut,source_resource_plan=ref(R/'drain8176-resource-plan-v1.json'),recovery_and_source_counts=dict(source_paths=35,original_payloads=29,full_original_delta=True))
plan['mathematical_controls']={n:dict(expected_family=tag[0],expected_failed_tags=[tag],expected_exit_code=1,expected_total=dict(passed=21,failed=1),mechanism=why) for n,tag,why in [('isolated_seed_cost_wrong','B3','Replace expected singleton zero cost with1; preserve fixture and algorithm.'),('zb_mark_count_wrong','C4','Replace true36 distinct marks target by erroneous108; preserve all coordinates.'),('real_boundary_rounded','E3','Add incorrect real p>=368 demand to exact p36799/100 scalar test; not a full certificate.') ]}
plan['not_proposed_packaging_mutations']=[n for n in mut if n not in plan['mathematical_controls']];plan['not_proposed_other_mutations_reason']='Only original-reviewer-cleared changed-claim predicates; no routine historical mutation duplication.'
plan['scientific_scope']='Finite single-seed DP and supplied rational points. Unchanged seeded tiny-fixture batch remains inside primary; no historical hill-climb, integer program or simulated annealing.'
plan['mutation_limits']['sequence']='Three listed changed-claim mutations once each, serial after preserved baseline; no baseline repeat, retry or cap increase.'
pp=put('drain8176-capture-plan-v1.json',plan)
for kind in ['capture','mutation-capture']:
 s=(R/f'drain8175-{kind}-v1.py').read_text().replace('8175','8176').replace('drain-author-slot','review-draft-slot').replace('early-review-v2.json','early-review-v1.json').replace('prepared-v2','prepared-v1').replace('02359b04e8bfb23212e3b3fd90061d87ef80d015562bb73302ff4bde508363ad',eh)
 s=s.replace('TOTAL: PASS=20 FAIL=0','TOTAL: PASS=22 FAIL=0').replace('TOTAL: PASS=19 FAIL=1','TOTAL: PASS=21 FAIL=1').replace('==19','==21').replace('completed_checks=20,passed=19','completed_checks=22,passed=21').replace('len(mutations)==10','len(mutations)==11').replace('Only the newly affected period_counts_wrong route is authorized here','Only the three original-reviewer-cleared changed-claim routes are authorized here')
 s=re.sub(r"PLAN_SHA256='[0-9a-f]+'",f"PLAN_SHA256='{sha(pp)}'",s);assert 'COLD_CLEARANCE_BINDING = None' in s;compile(s,kind,'exec');put(f'drain8176-{kind}-v1.py',s)
put('drain8176-adapter-verification-v1.json',dict(schema_version=1,kind='static-adapter-preparation-before-authorized-staging',references=[ref(R/n) for n in ['drain8176-build-staged-draft-v1.py','drain8176-capture-v1.py','drain8176-mutation-capture-v1.py','drain8176-capture-plan-v1.json','drain8176-adapter-bindings-v1.json']],cold_binding=None,source_count=35,original_count=29,primary_runs=0,mutation_runs=0,preflight=False,stdout_checks=22,json_outputs=[],inputs=3,helpers=[],raw_return_preserved_before_identity_rejection=True))
