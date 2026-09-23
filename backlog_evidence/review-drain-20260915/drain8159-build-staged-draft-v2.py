"""Future root-only stage/bind operation. No primary, gate, or cache execution."""
from pathlib import Path
import argparse,ast,gzip,hashlib,json,re,subprocess,sys
sys.dont_write_bytecode=True
R=Path('/private/tmp/review-drain-20260915');W=R/'review-draft-slot'
p=argparse.ArgumentParser();p.add_argument('--expected-base',required=True);p.add_argument('--stage-authorized',action='store_true',required=True);p.add_argument('--version',required=True);args=p.parse_args();assert args.stage_authorized and re.fullmatch('[0-9a-f]{40}',args.expected_base) and re.fullmatch('v[1-9][0-9]*',args.version)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ref=lambda p:dict(path=str(p),sha256=sha(p));bind=lambda ps:[dict(path=p,sha256=sha(W/p)) for p in sorted(set(ps))];git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
prep=R/'drain8159-author-canonical-draft-v4.json';assert sha(prep)=='d5104ade42349c641bb2ef39de5ff23f65c2e9d6aa78cd35bea4275d86537554';d=json.loads(prep.read_text())
q=json.loads((R/'drain8159-author-input-discovery-v4.json').read_text());assert sha(R/'drain8159-author-input-discovery-v4.json')=='b7da2c9ab85b40b7ee84f707b6129eab6bae91960dc0f91a8d09bcc7a993c3b1'
proof=json.loads((R/'drain8159-author-full-proof-map-v4.json').read_text());assert sha(R/'drain8159-author-full-proof-map-v4.json')=='8038972a62394af72da542193bd2ff223754e8e7d9ce5ee4aabfa4a7f134133e'
cost={e['runner']:e for e in json.loads((R/'drain8159-author-resource-plan-v3.json').read_text())};scope=json.loads((R/'drain8159-affected-scope-confirmation-v4.json').read_text())
assert len(d['files'])==436 and len(d['notes'])==25 and len(d['runners'])==41 and len(d['helper_map_plan'])==9 and len(proof)==72
owner=json.loads((R/'review-draft-slot.json').read_text());assert owner['owner']=='PR8159-author' and Path(owner['path']).resolve()==W.resolve()
assert args.expected_base=='631d6b36cd1e9b860763ebcad36e40a2bbe7439c'
assert git('rev-parse','HEAD')==args.expected_base==git('rev-parse','origin/main');assert not git('diff','--cached','--name-only')
assert set(git('diff','--name-only','HEAD').splitlines())=={'scripts/audit_packet_script_deps.py','docs/audit/scripts/build_citation_graph.py'}
assert set(git('ls-files','--others','--exclude-standard').splitlines())=={e['path'] for e in d['files']}
for e in d['files']:assert sha(W/e['path'])==e['sha256'],e['path']
# Guard both evidence memberships separately; changed current-main premises require reviewer confirmation.
for e in q['programs']:
 for x in e['runtime_closure']:assert sha(W/x['path'])==x['sha256'],x['path']
for e in q['mathematical_premise_closure']:
 for x in e['parents']:assert sha(W/x['path'])==x['sha256'],x['path']
files={k:R/f'drain8159-author-{k}-{args.version}.json' for k in ['unit-draft','source-handoff','cache-api']};assert all(not p.exists() for p in files.values())
refs=[ref(R/x) for x in ['drain8159-author-canonical-draft-v4.json','drain8159-author-input-discovery-v4.json','drain8159-author-resource-plan-v3.json','drain8159-author-full-proof-map-v4.json','drain8159-affected-scope-confirmation-v4.json','drain8159-block27-import-recovery-v1.json','drain8159-capture-plan-v1.json','drain8159-negative-certification-disposition-v1.json','drain8159-builder-fix-explanation-v2.json']]
review=R/'drain8159-final366-original-dispositions.json';original=json.loads(review.read_text());orig={e['path']:e for e in original['paths']};m=json.loads((W/'docs/work_history/review_loop/pr8159/manifest.json').read_text());assert len(m['paths'])==len(orig)==366
updates={e['path']:e['scope_disposition'] for e in scope['updated_exact_original_dispositions']};disps=[]
for e in m['paths']:
 assert e['path'] in orig
 for k in ['mode','blob','sha256']:assert e[k]==orig[e['path']][k]
 b=gzip.decompress((W/e['archive']).read_bytes());assert hashlib.sha256(b).hexdigest()==e['sha256'];assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['blob']
 destinations=[x for x in proof if x['original']==e['path']]
 disps.append(dict(original_path=e['path'],original_mode=e['mode'],original_blob=e['blob'],original_sha256=e['sha256'],final_path=e['archive'],final_sha256=sha(W/e['archive']),recovery=e['recovery'],disposition=updates.get(e['path'],e['disposition']),canonical_proof_destinations=destinations))
b27=json.loads((R/'drain8159-block27-import-recovery-v1.json').read_text());assert hashlib.sha256(gzip.decompress((W/b27['archive']).read_bytes())).hexdigest()==b27['sha256'];b27['recovery']=b27['original_commit']+':'+b27['original_path']
registry=['scripts/audit_packet_script_deps.py','docs/audit/scripts/build_citation_graph.py'];replacements={};preserved={}
def mapof(text):return ast.literal_eval(next(n.value for n in ast.parse(text).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='EXPLICIT_PACKET_HELPER_RUNNER_PATHS' for t in n.targets)))
for path in registry:
 text=(W/path).read_text();base_text=subprocess.check_output(['git','-C',str(W),'show','HEAD:'+path],text=True);old=mapof(base_text);assert not set(old)&set(d['helper_map_plan']);mark='EXPLICIT_PACKET_HELPER_RUNNER_PATHS = {';assert base_text.count(mark)==1
 expected=base_text.replace(mark,mark+'\n'+''.join('    '+repr(k)+': '+repr(v)+',\n' for k,v in d['helper_map_plan'].items()),1)
 assert text==expected,'Registry has changes beyond exact reviewed additions: '+path
 assert mapof(text)==dict(old,**d['helper_map_plan']);preserved[path]={'before_sha256':hashlib.sha256(base_text.encode()).hexdigest(),'current_sha256':sha(W/path),'preserved_entries':len(old),'added_entries':9,'continuation_no_write':True}
sys.path[:0]=[str(W/'scripts'),str(W/'docs/audit/scripts')];import runner_cache as c,audit_packet_script_deps as a,build_citation_graph as g
notes=[];context=set();helpers=set();runtime=set();parents=set();apis=[];discovery={e['runner']:e for e in q['programs']};note_expected={e['path']:e for e in q['notes']}
for path in d['notes']:
 body=(W/path).read_text();primary=re.search(r'^runner: (.+)$',body,re.M)[1];cid=g.claim_id_from_path(W/path);hp=list(g.helper_runner_paths_for_claim(cid,primary));packet=list(a.helper_runner_paths_for_claim(cid,Path(primary).stem));assert set(hp)==set(packet)
 expected=set(d['helper_map_plan'].get(cid,[]))|{'scripts/'+h+'.py' for h in a.transitive_helpers(Path(primary).stem)};assert set(hp)==expected
 cites=sorted(x.relative_to(W).as_posix() for x in g.extract_citations(body,W/path));assert cites==sorted(note_expected[path]['actual_citations']);deps=d['dependencies_by_note'][path];assert set(deps)<=set(cites)
 helpers.update(hp);context.update(cites);notes.append(dict(path=path,claim_id=cid,declared_claim_id=re.search(r'^claim_id: (.+)$',body,re.M)[1],claim_type='bounded_theorem',primary_runner=primary,helpers=hp,citations=cites,repository_dependencies=deps,dependency_rationale='Owned full proofs and exact reviewed mathematical dependencies; supplied-model scopes and v4 partial-salvage boundaries apply.'))
assert {x['primary_runner'] for x in notes}|helpers==set(d['runners'])
for path in d['runners']:
 ins=list(c.declared_input_paths(W/path));assert ins==discovery[path]['declared_inputs'];assert c.declared_timeout_for(W/path)==cost[path]['time_cap_seconds']
 hp=sorted('scripts/'+h+'.py' for h in a.transitive_helpers(Path(path).stem))
 selected=['scripts/polarized_word_check_2026_09_15.py'] if path=='scripts/local_spectrum_check_2026_09_15.py' else []
 assert set(hp)|set(selected)==set(discovery[path]['proposed_transitive_helpers'])
 if selected:
  assert hp==[] and set(selected)<=set(ins)
  source=(W/path).read_text();assert "if isinstance(node,(ast.Import,ast.ImportFrom)):" in source and "elif isinstance(node,ast.FunctionDef) and node.name in needed:" in source
 actual_closure=set(ins)
 for h in hp:actual_closure.add(h);actual_closure.update(c.declared_input_paths(W/h) or [])
 conservative=set(actual_closure)
 for h in selected:conservative.add(h);conservative.update(c.declared_input_paths(W/h) or [])
 assert conservative=={e['path'] for e in discovery[path]['runtime_closure']}
 runtime.update(actual_closure|{path});context.update(conservative);apis.append(dict(primary=path,timeout=cost[path]['time_cap_seconds'],declared_inputs=ins,packet_transitive_helpers=hp,selected_source_helpers=selected,runtime_closure=bind(actual_closure),conservative_selected_source_closure=bind(conservative),not_executed_selected_helper_note_reads=bind(conservative-actual_closure),closure_scope='Actual direct reads plus normal imported-module reads. AST-selected helper imports and nine definitions execute, but helper module top-level note reads/fixtures do not. Conservative extra note bindings retained as context and separately identified.',declared_input_fingerprint=c.declared_input_fingerprint(W/path),cache_status=c.cache_status(path)))
for e in q['mathematical_premise_closure']:parents.update(x['path'] for x in e['parents'])
context.update(d['notes']);context.update(['docs/work_history/review_loop/pr8159/README.md','docs/work_history/review_loop/pr8159/manifest.json','docs/work_history/review_loop/pr8159/imports/manifest.json'])
subprocess.run(['git','-C',str(W),'add','--',*[e['path'] for e in d['files']],*registry],check=True);subprocess.run(['git','-C',str(W),'diff','--cached','--check'],check=True)
paths=git('diff','--cached','--name-only').splitlines();assert set(paths)=={e['path'] for e in d['files']}|set(registry);assert not git('diff','--name-only');tree=git('write-tree')
files['cache-api'].write_text(json.dumps(apis,indent=2)+'\n')
h=dict(status='AUTHOR HANDOFF ONLY; FINAL ORIGINAL REVIEWER COLD CONFIRMATION REQUIRED',author='/root/resume_8077',base=args.expected_base,tree=tree,original_dispositions=disps,supplementary_import_recovery=b27,full_proof_mapping=proof,mathematical_premise_closure=q['mathematical_premise_closure'],claim_dispositions={'partial_salvage':True,'deferred_negative_certification_owners':[6,18,5],'foundation_nonselection_owner3':'REJECTED AS UNPROVED; not procedural deferral alone','branch_preservation_required':True,'affected_originals':scope['updated_exact_original_dispositions']},registry_preservation=preserved,references=refs+[ref(files['cache-api'])]);files['source-handoff'].write_text(json.dumps(h,indent=2)+'\n')
tooling=['docs/audit/scripts/build_citation_graph.py','docs/audit/scripts/static_pipeline_checkpoint.py','scripts/runner_cache.py','scripts/audit_packet_script_deps.py','docs/audit/scripts/ledger_io.py','docs/audit/data/axiom_premise_nodes.json','docs/audit/data/doc_authority_registry.json']
record=dict(schema_version=2,unit_id='PR8159',constituents=[dict(id='PR8159',head=m['head'],delta_base=m['delta_base'],dispositions=dict(ref(files['source-handoff']),json_pointer='/original_dispositions'))],source=dict(base=args.expected_base,commit=args.expected_base,tree=tree,paths=bind(paths),deleted_paths=[]),inputs=dict(runtime=bind(runtime),helpers=bind(helpers),parents=bind(parents),context=bind(context),tooling=bind(tooling)),reviewer=dict(session='Original PR8159 reviewer; final staged confirmation pending',report=ref(review),references=refs+[ref(files['source-handoff']),ref(files['cache-api'])]),notes=notes,supporting_proofs=[],non_science_notes=[dict(path='docs/work_history/review_loop/pr8159/README.md',rationale='Exact recovery, honest untraced evidence qualifications, and partial-salvage branch preservation.',review_reference=ref(review))])
files['unit-draft'].write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(ref(files['unit-draft'])));print(tree)
