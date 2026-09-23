"""Writes external proposed adapters only; never invokes them or scientific source."""
from pathlib import Path
import json,hashlib,ast
R=Path('/private/tmp/review-drain-20260915');W=R/'author-draft-slot';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
refs=['drain8171-author-prepared-v2.json','drain8171-author-handoff-v2.json','drain8171-author-dispositions-v1.json','drain8171-source-input-discovery-v2.json','drain8171-resource-plan-v2.json','drain8171-disposition-original.json','drain8171-review-original.json','drain8171-review-original.md','drain8171-early-review-v2.json','drain8171-early-review-v2.md','drain8171-preparation-discovery-failures-v1.json']
bp=R/'drain8171-adapter-bindings-v1.json';assert not bp.exists();bp.write_text(json.dumps([dict(path=str(R/p),sha256=sha(R/p)) for p in refs],indent=2)+'\n')
p=R/'drain8171-build-staged-draft-v1.py';p.write_text(p.read_text().replace('BINDINGS_PLACEHOLDER',sha(bp)))
# Both capture entry points deliberately block before any attempt reservation while the actual cold report is absent.
block='''# Deliberately unbound: a new immutable adapter version must bind the ACTUAL
# original-reviewer cold report path/hash, exact verdict pointer/value and tree.
# Early source clearance is insufficient. No hypothetical verdict is accepted.
COLD_CLEARANCE_BINDING = None
def confirm_cold(cp,cold,tree):
    b=COLD_CLEARANCE_BINDING
    assert isinstance(b,dict), 'BLOCKED: actual same-session cold report schema/clearance has not yet been bound; root must prepare a new immutable adapter version'
    assert str(cp)==b['path'] and sha(cp)==b['sha256']
    assert cold['reviewer_session']=='/root/review_8171'
    def read_pointer(p):
        cur=cold
        for key in p.lstrip('/').split('/'):
            cur=cur[key.replace('~1','/').replace('~0','~')]
        return cur
    assert b['verdict_pointer'].startswith('/') and b['tree_pointer'].startswith('/')
    assert read_pointer(b['verdict_pointer'])==b['verdict_value']
    assert read_pointer(b['tree_pointer'])==tree==b['tree']

'''
s=(R/'drain8170-capture-v2.py').read_text().replace('8170','8171').replace("W=R/'drain-author-slot'","W=R/'author-draft-slot'").replace("R/'drain-author-slot.json'","R/'author-draft-slot.json'")
s=s.replace('def main():',block+'def main():',1).replace(",'cold-verdict-pointer'",'')
a=s.index("    assert cold['reviewer_session']",s.index('def main():'));b=s.index("    assert git('rev-parse'",a);s=s[:a]+"    confirm_cold(cp,cold,record['source']['tree'])\n"+s[b:]
a=s.index("    plan=json.loads(");b=s.index('    identities={}',a)
s=s[:a]+'''    planpath=R/'drain8171-capture-plan-v1.json';assert sha(planpath)==PLAN_SHA256;plan=json.loads(planpath.read_text())
    early=R/'drain8171-early-review-v2.json';assert sha(early)=='5da6fcfb236143f5a01623be0ec909d7dd4b1fde666b77e8c2c37debd1fd6995'
    primary=plan['primary'];assert {n['primary_runner'] for n in record['notes']}=={primary} and all(not n['helpers'] for n in record['notes'])
    cache=W/plan['cache_destination'];live=W/'logs/runner-cache/.in-progress'/cache.name
    for p in [cache,live]:assert not p.exists(),f'Existing evidence must not be overwritten: {p}'
'''+s[b:]
s=s.replace('limit_sec=900;limit_bytes=768*1024*1024','limit_sec=60;limit_bytes=384*1024*1024').replace('c.execute_and_write_cache(sys.argv[2],900)','c.execute_and_write_cache(sys.argv[2],60)').replace('PASS=17 FAIL=0','PASS=16 FAIL=0')
a=s.index('        data=json.loads(raw.read_text())');b=s.index("        assert Path(result['cache'])",a);s=s[:a]+s[b:]
s=s.replace('[raw,cache,live,worker_result,supervisor_log,raw_result]','[cache,live,worker_result,supervisor_log,raw_result]')
s=s.replace("if __name__=='__main__':main()","PLAN_SHA256='PLAN_PLACEHOLDER'\nif __name__=='__main__':main()")
# Keep the raw execute_runner result before execute_and_write_cache performs its original identity comparison.
assert 'original_execute_runner=c.execute_runner' in s and 'return result' in s and 'json.dump(result,evidence' in s
(R/'drain8171-capture-v1.py').write_text(s)
m=(R/'drain8170-mutation-capture-v1.py').read_text().replace('8170','8171').replace("W=R/'drain-author-slot'","W=R/'author-draft-slot'").replace("R/'drain-author-slot.json'","R/'author-draft-slot.json'")
m=m.replace('def main():',block+'def main():',1).replace(",'cold-verdict-pointer'",'')
a=m.index("    assert cold['reviewer_session']",m.index('def main():'));b=m.index("    assert primary['status']",a);m=m[:a]+"    confirm_cold(cp,cold,record['source']['tree'])\n"+m[b:]
m=m.replace("==900 and watch0['limit_bytes']==768*1024*1024","==60 and watch0['limit_bytes']==384*1024*1024").replace('PASS=17 FAIL=0','PASS=16 FAIL=0')
a=m.index('    planpath=');b=m.index('    ids={}',a)
m=m[:a]+'''    planpath=R/'drain8171-capture-plan-v1.json';assert sha(planpath)==PLAN_SHA256;plan=json.loads(planpath.read_text())
    runner=plan['primary'];assert sha(W/runner)==plan['primary_sha256'] and {n['primary_runner'] for n in record['notes']}=={runner}
    tree=ast.parse((W/runner).read_text());decl={n.targets[0].id:n.value for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name)}
    mutations=ast.literal_eval(decl['MUTATION_GATE']);assert mutations==plan['all_mutation_definitions'] and len(mutations)==10
    assert a.mutation in plan['mathematical_controls'], 'Only the eight reviewed mathematical corruption routes are proposed here'
    assert list(ast.literal_eval(decl['AUDIT_INPUT_PATHS']))==[e['path'] for e in plan['runtime_inputs']]
    assert ast.literal_eval(decl['INPUT_SHA256'])=={e['path']:e['sha256'] for e in plan['runtime_inputs']}
    assert ast.literal_eval(decl['AUDIT_TIMEOUT_SEC'])==60
    assert ref(W/plan['cache_destination']) in primary['artifacts']
'''+m[b:]
m=m.replace("for p in [baseline,W/plan['stdout']]:","for p in [W/plan['cache_destination']]:")
m=m.replace(";raw=W/plan['mutation_json_pattern'].replace('<mutation>',name)","")
m=m.replace('[stdout,stderr,receipt,raw]','[stdout,stderr,receipt]').replace('limit_seconds=900,limit_bytes=768*1024*1024','limit_seconds=60,limit_bytes=384*1024*1024').replace('elapsed>=900','elapsed>=60').replace('rss>768*1024*1024','rss>384*1024*1024')
a=m.index('        data=json.loads(raw.read_text())');b=m.index('        after=snapshot()',a)
m=m[:a]+'''        assert exit_code==1,'Mutation survived or exited abnormally; neither is a successful mutation control'
        body=stdout.read_text();assert not stderr.read_bytes(), 'Unexpected stderr retained for review'
        failures=re.findall(r'^FAIL: ([A-Z][0-9]+) ',body,re.M)
        expected=plan['mathematical_controls'][name]['expected_failed_tags']
        assert failures==expected, f'Wrong failure target: {failures}, expected {expected}'
        failed_families={t[0] for t in failures};assert failed_families=={family}
        assert f'mutation_family_expected: {family}' in body and f"mutation_family_observed: {family}" in body
        assert re.search(r'^TOTAL: PASS=15 FAIL=1$',body,re.M)
        assert len(re.findall(r'^PASS: [A-Z][0-9]+ ',body,re.M))==15
        data=dict(parsed_stdout=True,failed_tags=failures,expected_failed_tags=expected,completed_checks=16,passed=15,failed=1)
'''+m[b:]
m=m.replace('[stdout,stderr,raw]','[stdout,stderr]').replace("if __name__=='__main__':main()","PLAN_SHA256='PLAN_PLACEHOLDER'\nif __name__=='__main__':main()")
(R/'drain8171-mutation-capture-v1.py').write_text(m)
d=json.loads((R/'drain8171-source-input-discovery-v2.json').read_text());p=W/d['primary'];tree=ast.parse(p.read_text());decl={n.targets[0].id:n.value for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name)}
mut=ast.literal_eval(decl['MUTATION_GATE'])
controls={
'variance_identity_wrong':('B1','Replace the derivative variance target by half its value; independent integrated variance should reject it.'),
'directional_moment_wrong':('B2','Change the longitudinal coefficient from 3A/kappa to 2A/kappa.'),
'sign_lemma_wrong':('B3','Change the entire-series coefficient factor m/2 to m/3.'),
'sensitivity_bound_wrong':('B4','Change the tested mean/variance slope from 1/3 to 1/4 at the unchanged ten rational points.'),
'contraction_constant_wrong':('C1','Replace sqrt(3) enclosures by 3/2; unchanged two beta boundary fixtures reject the crossing.'),
'one_site_rate_wrong':('C2','Halve the comparison slope of A(3beta) on unchanged rational fixtures.'),
'reach_wrong':('D1','Remove the negative quadratic term from the lower comparison; same five enclosures reject it.'),
'reach_upper_wrong':('D1','Reduce the upper comparison slope from 1/3 to 3/10; same fixtures reject it.')}
plan=dict(schema_version=1,kind='proposed-root-owned-capture-and-mathematical-control-plan-not-executed',primary=d['primary'],primary_sha256=sha(p),runtime_inputs=d['runtime_inputs'],input_fingerprint=d['input_fingerprint'],helpers=[],cache_destination='logs/runner-cache/'+p.stem+'.txt',stdout_only=True,json_outputs=[],primary_output_writes=[],runner_cache_result_contract='Original API merges primary stderr into stdout; result.stderr is empty by design. Raw result is serialized before original source/input generation comparison, unchanged return identity.',primary_limits=dict(wall_seconds=60,memory_bytes=384*1024*1024,enforcement='External sampled aggregate process-tree RSS including supervisor, worker and descendants; interval .02s plus ps overhead; not an OS hard reservation; kills process group and recorded descendants on violation.'),completed_check_count=16,primary_invocations=1,all_mutation_definitions=mut,mathematical_controls={n:dict(expected_family=mut[n],expected_failed_tags=[tag],expected_exit_code=1,expected_total=dict(passed=15,failed=1),mechanism=why) for n,(tag,why) in controls.items()},mutation_limits=dict(wall_seconds_each=60,memory_bytes_each=384*1024*1024,sequence='Serial individual invocations of --mutation <name>, after preserved primary receipt; no baseline invocation; once-only marker per name; abort on unexpected result, no retry.'),not_proposed_packaging_mutations=['claim_transition_injected','claim_classical_name_in_theorem'],scientific_scope='Finite corruption sensitivity only; not execution of compactness, measurable coupling or infinite-plane proofs. Original independent mathematical controls are reused without rerun.',required_before_execution=['Exact staged schema2 source and input record','Cheap mechanical preflight tied to that record/tree','Original same-session actual cold report clearance, explicitly bound in a new immutable adapter version; v1 deliberately refuses execution','Root explicit capture dispatch'],failure_policy='Preserve markers, raw result, live merged stream, supervisor log, mutation stdout/stderr, receipt and source/input generations. No automatic retry, baseline repeat, cap increase, evidence replacement or fabricated JSON.',source_resource_plan=dict(path=str(R/'drain8171-resource-plan-v2.json'),sha256=sha(R/'drain8171-resource-plan-v2.json')))
pp=R/'drain8171-capture-plan-v1.json';pp.write_text(json.dumps(plan,indent=2,ensure_ascii=False)+'\n')
for f in ['drain8171-capture-v1.py','drain8171-mutation-capture-v1.py']:
 p=R/f;p.write_text(p.read_text().replace('PLAN_PLACEHOLDER',sha(pp)))
for f in ['drain8171-build-staged-draft-v1.py','drain8171-capture-v1.py','drain8171-mutation-capture-v1.py']:compile((R/f).read_text(),str(R/f),'exec')
print(json.dumps({f:sha(R/f) for f in ['drain8171-build-staged-draft-v1.py','drain8171-capture-v1.py','drain8171-mutation-capture-v1.py','drain8171-capture-plan-v1.json','drain8171-adapter-bindings-v1.json']},indent=2))
