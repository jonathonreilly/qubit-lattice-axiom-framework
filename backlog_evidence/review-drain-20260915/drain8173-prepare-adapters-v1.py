from pathlib import Path
import ast,hashlib,json,re,subprocess
R=Path('/private/tmp/review-drain-20260915');W=R/'review-draft-slot'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ref=lambda p:dict(path=str(p),sha256=sha(p))
def put(name,s):
 p=R/name;assert not p.exists(),p;p.write_text(s if isinstance(s,str) else json.dumps(s,indent=2,ensure_ascii=False)+'\n');return p
prepared=json.loads((R/'drain8173-author-prepared-v3.json').read_text());discovery=json.loads((R/'drain8173-source-input-discovery-v3.json').read_text())
assert sha(R/'drain8173-early-review-v3.json')=='9ad28d3417d6c1a3b10d92dc7027ee029c39a58d98e042de25ed50f29e04adb0'
for x in prepared['source']:
 p=W/x['path'];assert sha(p)==x['sha256'] and p.stat().st_mode&0o777==int(x['mode'][-3:],8)
# Artifact-only preparation: no stage, science import or execution.
authority_paths=['docs/MINIMAL_AXIOMS_2026-06-29.md','docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md','docs/audit/data/axiom_premise_nodes.json','docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md','docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md','docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md']
authority=put('drain8173-adapter-authority-v1.json',dict(schema_version=1,base=prepared['base'],kind='source-hash-authority-binding-not-new-review',authority=[dict(path=p,sha256=sha(W/p)) for p in authority_paths],context=discovery['context_parents']))
refs=[ref(R/p) for p in ['drain8173-author-prepared-v3.json','drain8173-source-freeze-v3.json','drain8173-author-handoff-v3.json','drain8173-author-dispositions-v1.json','drain8173-author-corrections-v3.patch','drain8173-source-input-discovery-v3.json','drain8173-resource-plan-v3.json','drain8173-review-original.json','drain8173-review-original.md','drain8173-early-review-v3.json','drain8173-early-review-v3.md','drain8173-adapter-authority-v1.json']]
early=json.loads((R/'drain8173-early-review-v3.json').read_text())
for key in ['script','stdout','stderr']:refs.append(ref(Path(early['independent_controls'][key])))
bp=put('drain8173-adapter-bindings-v1.json',refs)
b=(R/'drain8171-build-staged-draft-v1.py').read_text().replace('8171','8173').replace('author-draft-slot','review-draft-slot')
b=b.replace('prepared-v2.json','prepared-v3.json').replace('discovery-v2.json','discovery-v3.json').replace('resource-plan-v2.json','resource-plan-v3.json').replace('handoff-v2.json','handoff-v3.json').replace('early-review-v2.json','early-review-v3.json')
b=b.replace('len(f)==23','len(f)==25').replace("prior=json.loads((R/'drain8173-author-handoff-v3.json').read_text())","prior=json.loads((R/'drain8173-adapter-authority-v1.json').read_text())")
a=b.index("        assert sha(rp)==");z=b.index('        owner=json.loads',a)
b=b[:a]+'''        assert sha(rp)=='9ad28d3417d6c1a3b10d92dc7027ee029c39a58d98e042de25ed50f29e04adb0'
        assert review['kind']=='same-session-early-affected-source-review'
        assert review['pr']==8173 and review['source_revision']==3 and review['disposition']=='stage-cold-capture-clearance'
        assert review['final_pass'] is False and review['landing_pass'] is False and not review['blockers']
        assert review['source_files_verified']==25 and review['original_payloads_verified']==20 and review['branch_preservation_required'] is True
        assert review['prepared_sha256']==sha(R/'drain8173-author-prepared-v3.json') and review['source_freeze_sha256']==sha(R/'drain8173-source-freeze-v3.json')
        assert review['handoff_sha256']==sha(R/'drain8173-author-handoff-v3.json') and review['original_manifest_sha256']==d['original_manifest']['sha256']
''' +b[z:]
b=b.replace("discovery['runtime_inputs']+prior['authority']","discovery['runtime_inputs']+prior['authority']+discovery['context_parents']")
b=b.replace("original=json.loads((R/'drain8173-disposition-original.json').read_text());old={x['path']:x for x in original}","original=json.loads((R/'drain8173-review-original.json').read_text())['dispositions'];old={x['path']:x for x in original}")
b=b.replace('len(old)==len(mapping)==18','len(old)==len(mapping)==20')
b=b.replace("assert o['head_tree'].split()[:3]==[e['mode'],'blob',e['git_blob']]","assert (o['mode'],o['blob'])==(e['mode'],e['git_blob'])")
b=b.replace("o['head_sha256']==e['sha256']","o['sha256']==e['original_sha256']").replace("original_sha256=e['sha256']","original_sha256=e['original_sha256']")
b=b.replace("set(d['deferred_science'])","set(d['readable_history'])|{e['path'] for e in discovery['context_parents']}")
b=b.replace("discovery['mathematical_dependencies']","discovery['framework_dependencies']")
a=b.index("        rationale='");z=b.index('\n        handoff=',a)
b=b[:a]+'''        rationale='Complete self-contained finite Gaussian covariance, fixed laboratory-axis rotation response and instantaneous projected-vector mode-sum proofs remain live. Explicit beta>0, L>=3, forward bonds and component conventions; current axiom memo is framework boundary only. Finite-menu and zero-field Fourier/return-sum sources are context, not mathematical premises. Original samplers and unsupported empirical/physical/asymptotic interpretation remain exact history; negative certification deferred and original branch retained.'
''' .rstrip()+b[z:]
b=b.replace("'Recovery index only. Full corrected deferred scientific proof is a separately preserved text artifact, not live supporting proof or premise. Complete positive proofs reside in canonical source; original histories and failures remain exact.'","'Recovery index only; complete original note remains readable history with explicit corrections, and all20 original payloads are exact. Complete corrected finite proofs reside in the canonical note; historical samplers and empirical claims are not inputs or supporting premises.'")
b=b.replace("BINDINGS_SHA256='308c4d6f5f79e5e6363c92afb4c14593bb41ed68e1a3cb8bf85a0cd65a492d7d'",f"BINDINGS_SHA256='{sha(bp)}'")
# Never borrow obsolete field names or wrong count/proof roles from the template.
assert all(x not in b for x in ['8171','head_tree','head_sha256',"d['deferred_science']",'len(f)==23'])
compile(b,'drain8173-build-staged-draft-v1.py','exec');builder=put('drain8173-build-staged-draft-v1.py',b)
runner=W/prepared['primaries'][0];tree=ast.parse(runner.read_text());decl={n.targets[0].id:ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id in ['MUTATION_GATE','AUDIT_INPUT_PATHS','INPUT_SHA256','AUDIT_TIMEOUT_SEC']}
plan=json.loads((R/'drain8171-capture-plan-v1.json').read_text());plan.update(primary=prepared['primaries'][0],primary_sha256=sha(runner),runtime_inputs=discovery['runtime_inputs'],input_fingerprint=discovery['input_fingerprint'],cache_destination='logs/runner-cache/'+runner.stem+'.txt',completed_check_count=14,all_mutation_definitions=decl['MUTATION_GATE'],source_resource_plan=ref(R/'drain8173-resource-plan-v3.json'),limits_measured=False)
controls={
'eigenvalue_wrong':('B1','Replace eigenvalue coefficient2 by1 on the same four64-site plane waves; exact matrix residual must fail.'),
'spin_wave_normalization_wrong':('B2','Replace first ring variance1/(2beta) by1/(4beta); same inverse eigenvalue equation must fail.'),
'sum_rule_wrong':('C1','Double kappa times the unchanged single-site transverse moment; exact response identity must fail.'),
'integration_by_parts_wrong':('C2','Reverse the target sign of the generator action on s3, leaving derivative and surface integration unchanged.'),
'parseval_wrong':('D1','Double the exact rational real-space squared norm while keeping all four Fourier coefficients unchanged.')}
plan['mathematical_controls']={n:dict(expected_family=t[0],expected_failed_tags=[t],expected_exit_code=1,expected_total=dict(passed=13,failed=1),mechanism=m) for n,(t,m) in controls.items()}
plan['not_proposed_packaging_mutations']=['claim_source_injected','claim_classical_name_in_theorem']
plan['scientific_scope']='Five existing finite mathematical corruption routes only; no global, asymptotic, empirical or negative-certification PASS. Original independent bond-cancellation/frame controls are reused without rerun; original samplers stay unexecuted.'
plan['recovery_and_source_counts']=dict(source_paths=25,original_payloads=20)
plan['canonical_evidence_binding']='Canonical cache is owned by source unit at cache_destination; final unit must bind its bytes. No extra mutable checkout cache path is added to reviewer references. External preserved raw capture is execution provenance only.'
pp=put('drain8173-capture-plan-v1.json',plan)
for kind in ['capture','mutation-capture']:
 s=(R/f'drain8171-{kind}-v2.py').read_text().replace('8171','8173').replace('author-draft-slot','review-draft-slot').replace('early-review-v2.json','early-review-v3.json').replace('primary-prepared-v2','primary-prepared-v3').replace('mutation-prepared-v2','mutation-prepared-v3')
 s=re.sub(r'^COLD_CLEARANCE_BINDING = .*$', 'COLD_CLEARANCE_BINDING = None',s,flags=re.M)
 # Future cold schema is unknown: explicit pointer predicates must be bound from the actual report, not guessed reviewer_session fields.
 s=s.replace("    assert cold['reviewer_session']=='/root/review_8173'", "    assert b.get('same_session_provenance'), 'Actual original-reviewer provenance must be recorded in the new binding'\n    assert isinstance(b.get('required_predicates'),dict) and b['required_predicates']")
 s=s.replace("    assert read_pointer(b['tree_pointer'])==tree==b['tree']", "    assert read_pointer(b['tree_pointer'])==tree==b['tree']\n    for p,v in b['required_predicates'].items():assert p.startswith('/') and read_pointer(p)==v")
 s=s.replace('5da6fcfb236143f5a01623be0ec909d7dd4b1fde666b77e8c2c37debd1fd6995','9ad28d3417d6c1a3b10d92dc7027ee029c39a58d98e042de25ed50f29e04adb0')
 s=s.replace('TOTAL: PASS=16 FAIL=0','TOTAL: PASS=14 FAIL=0').replace('TOTAL: PASS=15 FAIL=1','TOTAL: PASS=13 FAIL=1')
 s=s.replace('==15','==13').replace('completed_checks=16,passed=15','completed_checks=14,passed=13').replace('len(mutations)==10','len(mutations)==7').replace('eight reviewed mathematical','five reviewed mathematical')
 s=s.replace("PLAN_SHA256='12b72e616fd0579db2e76fbe74c8b18884db853416da60a460bca3662d68b352'",f"PLAN_SHA256='{sha(pp)}'")
 if kind=='capture':
  # Explicit API declarations must agree with the plan before reserving an invocation.
  mark="    cache=W/plan['cache_destination'];live=W/'logs/runner-cache/.in-progress'/cache.name"
  s=s.replace(mark,"""    sys.path[:0]=[str(W/'scripts'),str(W/'docs/audit/scripts')]
    import runner_cache as c,audit_packet_script_deps as deps
    assert sha(W/primary)==plan['primary_sha256'] and not deps.transitive_helpers(Path(primary).stem)
    assert list(c.declared_input_paths(W/primary))==[e['path'] for e in plan['runtime_inputs']]
    assert c.declared_input_fingerprint(W/primary)==plan['input_fingerprint'] and c.declared_timeout_for(W/primary)==60
"""+mark)
  # Preserve raw stream to a portable external artifact even if cache API deletes its live log on generation failure.
  # Raw execute_runner result is always saved before original API identity comparison; retain its object unchanged.
 else:
  # Require and revalidate the completed cheap receipt inherited from the actual primary capture.
  anchor="    assert primary['primary_runs_attempted']==1 and primary['mutation_runs']==0 and primary['simulation_runs']==0"
  s=s.replace(anchor,anchor+"\n    cheap_path,cheap=load(primary['cheap']['path'],primary['cheap']['sha256'])\n    assert cheap['mechanical_status']=='ok' and cheap['tree']==record['source']['tree'] and cheap['record_sha256']==sha(rp) and not cheap['cache_checked']")
  # Source-owned canonical cache hash is verified, not added to independent reviewer reference list.
 compile(s,f'drain8173-{kind}-v1.py','exec');assert '8171' not in s;put(f'drain8173-{kind}-v1.py',s)
# Static-only verification of intended source controls and untouched pool.
assert not subprocess.check_output(['git','-C',str(W),'diff','--name-only'],text=True)
assert not subprocess.check_output(['git','-C',str(W),'diff','--cached','--name-only'],text=True)
assert set(subprocess.check_output(['git','-C',str(W),'ls-files','--others','--exclude-standard'],text=True).splitlines())=={x['path'] for x in prepared['source']}
for x in prepared['source']:assert sha(W/x['path'])==x['sha256']
files=['drain8173-build-staged-draft-v1.py','drain8173-capture-v1.py','drain8173-mutation-capture-v1.py','drain8173-capture-plan-v1.json','drain8173-adapter-bindings-v1.json','drain8173-adapter-authority-v1.json']
put('drain8173-adapter-verification-v1.json',dict(schema_version=1,kind='static-adapter-preparation-not-execution',references=[ref(R/p) for p in files],frozen_source_count=25,original_recovery_count=20,primary_functions_imported=False,primary_runs=0,mutation_runs=0,simulation_runs=0,builder_executed=False,staging=False,preflight=False,registry_changes=False,source_unchanged=True,capture_block='COLD_CLEARANCE_BINDING=None; requires actual cold report predicates and tree in new immutable version before marker reservation',actual_api=dict(execute_runner_signature='(runner_path: str, timeout_sec: int) -> dict',execute_and_write_cache='Original before/after source/input generation equality remains enforced; wrapper writes actual execute_runner result then returns same object before the comparison',stderr_contract='Primary stderr merged into stdout by original API; mutation streams kept separately',helpers=[],runtime_inputs=3,primary_stdout_total=14,math_mutations=5,mutation_expected_pass=13,mutation_expected_fail=1,source_derived_unmeasured_limits=dict(seconds=60,bytes=384*1024*1024)),canonical_cache_scope='Final source-owned unit binds canonical cache; no duplicate mutable-pool reviewer reference required'))
print(json.dumps({p:sha(R/p) for p in files+['drain8173-adapter-verification-v1.json']},indent=2))
