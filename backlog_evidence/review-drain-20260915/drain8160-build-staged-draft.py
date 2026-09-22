"""Future root-dispatched staging/binding only. Not run during preparation.
Requires exact guarded base and explicit --stage-authorized. No primary/cache runs.
"""
from pathlib import Path
import argparse,ast,json,hashlib,gzip,subprocess,sys,re
sys.dont_write_bytecode=True
ap=argparse.ArgumentParser();ap.add_argument('--expected-base',required=True);ap.add_argument('--stage-authorized',action='store_true',required=True);ap.add_argument('--version',required=True);args=ap.parse_args()
R=Path('/private/tmp/review-drain-20260915');W=R/'drain-author-slot';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ref=lambda p:dict(path=str(p),sha256=sha(p));bind=lambda ps:[dict(path=p,sha256=sha(W/p)) for p in sorted(set(ps))];git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
assert re.fullmatch(r'v[1-9][0-9]*',args.version)
files={k:R/f'drain8160-author-{k}-{args.version}.json' for k in ['unit-draft','source-handoff','cache-api']};assert all(not p.exists() for p in files.values())
d=json.loads((R/'drain8160-author-prepared-v2.json').read_text());assert git('rev-parse','HEAD')==args.expected_base==git('rev-parse','origin/main');assert json.loads((R/'drain-author-slot.json').read_text())['owner']=='PR8160';assert not git('diff','--name-only','HEAD')
for e in d['files']:assert sha(W/e['path'])==e['sha256'],e['path']
assert set(git('ls-files','--others','--exclude-standard').splitlines())=={e['path'] for e in d['files']}
registry=['scripts/audit_packet_script_deps.py','docs/audit/scripts/build_citation_graph.py']; oldmaps={}
for p in registry:
 text=(W/p).read_text();tree=ast.parse(text);node=next(n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='EXPLICIT_PACKET_HELPER_RUNNER_PATHS' for t in n.targets));before=ast.literal_eval(node.value);oldmaps[p]=before
 assert not set(d['helper_map_plan'])&set(before),'PR8160 already registered; inspect instead of overwriting'
 marker='EXPLICIT_PACKET_HELPER_RUNNER_PATHS = {';assert text.count(marker)==1
 extra='\n'+''.join('    '+repr(k)+': '+repr(v)+',\n' for k,v in d['helper_map_plan'].items());new=text.replace(marker,marker+extra,1)
 parsed=ast.parse(new);after=ast.literal_eval(next(n.value for n in parsed.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='EXPLICIT_PACKET_HELPER_RUNNER_PATHS' for t in n.targets)));assert all(after[k]==v for k,v in before.items());(W/p).write_text(new)
subprocess.run(['git','-C',str(W),'add','--',*[e['path'] for e in d['files']],*registry],check=True)
for a in [('diff','--check'),('diff','--cached','--check'),('diff','HEAD','--check')]:subprocess.run(['git','-C',str(W),*a],check=True)
sys.path[:0]=[str(W/'scripts'),str(W/'docs/audit/scripts')];import runner_cache as c,audit_packet_script_deps as a,build_citation_graph as g
notes=[];context=[];parents=[];helpers=[];runtime=[];apis=[]
for p in d['notes']:
 body=(W/p).read_text();primary=re.search(r'^runner: (.+)$',body,re.M)[1];cid=g.claim_id_from_path(W/p);hp=g.helper_runner_paths_for_claim(cid,primary);packet=a.helper_runner_paths_for_claim(cid,Path(primary).stem);assert set(hp)==set(packet),(p,hp,packet)
 expected=set(d['helper_map_plan'].get(cid,[]))|{'scripts/'+x+'.py' for x in a.transitive_helpers(Path(primary).stem)};assert set(hp)==expected
 cites=sorted(x.relative_to(W).as_posix() for x in g.extract_citations(body,W/p));deps=d['dependencies'][p];assert set(deps)<=set(cites);context+=cites;parents+=deps;helpers+=hp
 notes.append(dict(path=p,claim_id=cid,declared_claim_id=re.search(r'^claim_id: (.+)$',body,re.M)[1],claim_type='bounded_theorem',primary_runner=primary,helpers=hp,citations=cites,repository_dependencies=deps,dependency_rationale='Complete supplied rotor/Wilson model proofs; exact linked concentration, defect and state lemmas. Gauge dynamics uses characteristic note only for Fourier positivity, with separate second-moment proof. No automatic PR8161 premise.'))
assert set(d['primary_runners']+helpers)==set(d['runners'])
for p in d['runners']:
 ins=list(c.declared_input_paths(W/p));hp=sorted('scripts/'+x+'.py' for x in a.transitive_helpers(Path(p).stem));closure=set(ins)
 for h in hp:closure.update(c.declared_input_paths(W/h));closure.add(h)
 assert c.declared_timeout_for(W/p)==120;runtime+=list(closure)+[p];context+=ins
 apis.append(dict(primary=p,timeout=120,declared_inputs=ins,runtime_closure=bind(closure),declared_input_fingerprint=c.declared_input_fingerprint(W/p),cache_status=c.cache_status(p),packet_transitive_helpers=hp))
assert set(d['notes'][:5])<={e['path'] for e in apis[-1]['runtime_closure']}
files['cache-api'].write_text(json.dumps(apis,indent=2)+'\n')
m=json.loads((W/'docs/work_history/review_loop/pr8160/original-manifest.json').read_text());disps=[]
for e in m:
 assert hashlib.sha256(gzip.decompress((W/e['stored']).read_bytes())).hexdigest()==e['original_sha256']
 disps.append(dict(original_path=e['original_path'],original_sha256=e['original_sha256'],final_path=e['stored'],final_sha256=sha(W/e['stored']),disposition=e['disposition']+'; exact full original version archived; canonical endpoint is separately mapped in manifest.',recovery=e['recovery'],canonical_path=e.get('final_path'),canonical_sha256=e.get('final_sha256'),working_argument_paths=e.get('canonical_argument_paths',[])))
assert len(disps)==86
paths=git('diff','--cached','--name-only').splitlines();assert set(paths)=={e['path'] for e in d['files']}|set(registry)
refs=[ref(R/x) for x in ['drain8160-original-review.json','drain8160-original-provenance-checks.json','drain8160-independent-controls.json','drain8160-early-affected-review-v1.json','drain8160-author-prepared-v2.json','drain8160-input-discovery-prestage-v1.json']]
h=dict(status='AUTHOR DRAFT; ORIGINAL FINAL COLD CONFIRMATION REQUIRED',author='/root/resume_8077',base=args.expected_base,tree=git('write-tree'),original_dispositions=disps,claim_dispositions='Six full supplied-model proofs preserve arbitrary joint sequences, fixed local support and compact time intervals. No extra onsite charge interaction in notes2–6. All historical failures/28 mutations preserved; no fixed-g phase or framework selection claim.',current_main_preservation='101 previously hash-frozen additions and exactly two additive maps; all old mappings preserved.',execution_plan=dict(timeouts=d['timeouts_seconds'],process_tree_rss_limit_bytes=536870912,concurrency=1,state='No primary executed; root dispatch after cheap and original cold'),references=refs+[ref(files['cache-api'])]);files['source-handoff'].write_text(json.dumps(h,indent=2)+'\n')
context+=d['notes'];tooling=['docs/audit/scripts/build_citation_graph.py','docs/audit/scripts/static_pipeline_checkpoint.py','scripts/runner_cache.py','scripts/audit_packet_script_deps.py','docs/audit/scripts/ledger_io.py','docs/audit/data/axiom_premise_nodes.json','docs/audit/data/doc_authority_registry.json'];review=refs[0]
record=dict(schema_version=2,unit_id='PR8160',constituents=[dict(id='PR8160',head='3210315c2cddeb5b0a9e32c9b35e30c196eaa65a',delta_base='e0ef7cf4633034a8c1e6d57f5812cc4275bf1349',dispositions=dict(ref(files['source-handoff']),json_pointer='/original_dispositions'))],source=dict(base=args.expected_base,commit=args.expected_base,tree=git('write-tree'),paths=bind(paths),deleted_paths=[]),inputs=dict(runtime=bind(runtime),helpers=bind(helpers),parents=bind(parents),context=bind(context),tooling=bind(tooling)),reviewer=dict(session='/root/review_8160; original session final source confirmation pending',report=review,references=refs[1:]+[ref(files['source-handoff']),ref(files['cache-api'])]),notes=notes,supporting_proofs=[],non_science_notes=[dict(path='docs/work_history/review_loop/pr8160/README.md',rationale='Historical recovery and original-to-canonical argument mapping only.',review_reference=review)])
files['unit-draft'].write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(ref(files['unit-draft'])));print(record['source']['tree'])
