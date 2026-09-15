from pathlib import Path
import sys,json,hashlib,subprocess,re,gzip
root=Path('/private/tmp/review-drain-20260915');repo=root/'author-slot-one'
sys.path[:0]=[str(repo/'docs/audit/scripts'),str(repo/'scripts')]
import build_citation_graph as graph,runner_cache as cache,audit_packet_script_deps as packet
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
git=lambda *args:subprocess.check_output(['git','-C',str(repo),*args],text=True).strip()
assert len(sys.argv)==3, 'expected frozen base and tree'; expected_base,expected_tree=sys.argv[1:]; assert git('rev-parse','HEAD')==expected_base and git('write-tree')==expected_tree
inv=json.loads((root/'check8090/inventory.json').read_text());mapping=json.loads((root/'8090-reviewer-archive-map.json').read_text());by={e['original_path']:e for e in mapping['entries']}
inv['confirmation_base']=expected_base
paths=git('diff','--cached','--name-only',expected_base).splitlines()
binding=lambda p:{'path':p,'sha256':sha(repo/p)}
rows=[]
for raw in inv['paths']:
 status,p=raw['status'],raw['path'];f=root/'check8090/original'/p
 if p in by:
  m=by[p];target=m['final_path'];b=(repo/target).read_bytes();decoded=gzip.decompress(b) if m['encoding']=='gzip' else b;assert decoded==f.read_bytes()
  disp='Preserved byte-exact historical evidence, decoded through archive manifest; author procedural claims are not current review authority.'
 elif p in paths:target=p;disp='Canonical source and proof retained; path/input packaging corrections reviewed; cache is original historical cache pending fresh execution.' if p.startswith('logs/') else 'Canonical mathematical source retained with independently confirmed path/input packaging and explicit historical scope correction only.'
 else:target=None;disp='Generated citation authority excluded; current-main version retained, combined gate regenerates independently.'
 rows.append({'original_path':p,'original_sha256':sha(f),'disposition':disp,'recovery':{'head':inv['head'],'path':p},'final_path':target,'final_sha256':sha(repo/target) if target else None})
notes=[];runtime=set();helpers=set();parents=set()
for p in inv['canonical_paths']:
 if not p.startswith('docs/'):continue
 path=repo/p;body=path.read_text();cid=graph.claim_id_from_path(path);primary=graph.extract_runner(body,path.relative_to(repo/'docs').as_posix());hs=set(graph.helper_runner_paths_for_claim(cid,primary));ps={'scripts/'+n+'.py' for n in packet.transitive_helpers(Path(primary).stem)};assert ps==set(graph.resolve_helper_runner_paths(primary))
 cs={str(x.relative_to(repo)) for x in graph.extract_citations(body,path)};deps={x for x in cs if '/work_history/' not in x}
 declared=re.findall(r'^claim_id:\s*(\S+)\s*$',body.split('---',2)[1] if body.startswith('---\n') else '',re.M)
 notes.append({'path':p,'claim_id':cid,'declared_claim_id':declared[0] if declared else None,'claim_type':graph.extract_claim_type_hint(body)[1],'primary_runner':primary,'helpers':sorted(hs),'citations':sorted(cs),'repository_dependencies':sorted(deps),'dependency_rationale':'Current axiom memo supplies ontology; native edge/CAR parent supplies conditional finite code and nonbridge isometry. External RG theorem and even-CAR LR method separately bound. Hamiltonian, counterterm, state, controls and clocks are supplied.'})
 helpers|=hs;parents|=deps
 for script in hs|{primary}:
  ds=cache.declared_input_paths(script);assert ds and cache.declared_timeout_for(script);runtime.update(ds)
context=['docs/MINIMAL_AXIOMS_2026-06-29.md','docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md','docs/audit/data/axiom_premise_nodes.json']
skill='docs/ai_methodology/skills/review-loop/'
context += ['docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md','docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md','docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md']
context +=[skill+p for p in ['SKILL.md','PREFLIGHT.md','references/OPERATIONS.md','references/UNIT_RECEIPT.md','scripts/review_receipt.py','scripts/review_workspace.py','agents/openai.yaml']]
tooling=['docs/audit/scripts/build_citation_graph.py','docs/audit/scripts/static_pipeline_checkpoint.py','scripts/runner_cache.py','scripts/audit_packet_script_deps.py','docs/audit/scripts/ledger_io.py','docs/audit/data/doc_authority_registry.json']
report=json.loads((root/'review-8090-draft.json').read_text());report.update(status='PREEXECUTION_SOURCE_CORRECTIONS_CONFIRMED_NOT_FINAL_PASS',source_tree=git('write-tree'),original_dispositions=rows,source_paths=[binding(p) for p in paths],runtime_scientific_inputs=[binding(p) for p in sorted(runtime)],notes=notes,correction_confirmation='All source differences cold-read; unchanged mathematics, thresholds, execution count and caps. Archive16 decoded payloads exact, including original recovery and mutations. One fresh primary execution and final cache binding pending.')
provisional=root/'review-8090-preexecution.json';assert not provisional.exists();provisional.write_text(json.dumps(report,indent=2)+'\n');ref={'path':str(provisional),'sha256':sha(provisional)}
discovered={str(p.relative_to(repo)) for p in graph.discover_notes()};exempt=[{'path':p,'rationale':'Reviewed historical checklist or archive navigation only; preserved original author scope, no live scientific theorem or executable claim.', 'review_reference':ref} for p in paths if p.endswith('.md') and p not in inv['canonical_paths'] and p in discovered]
record={'schema_version':1,'unit_id':'pr8090-preexecution','constituents':[{'id':'8090','head':inv['head'],'delta_base':inv['original_base'],'dispositions':dict(ref,json_pointer='/original_dispositions')}],'source':{'base':inv['confirmation_base'],'commit':git('rev-parse','HEAD'),'tree':git('write-tree'),'paths':[binding(p) for p in paths],'deleted_paths':[]},'inputs':{k:[binding(p) for p in sorted(set(v))] for k,v in {'runtime':runtime,'helpers':helpers,'parents':parents,'context':context,'tooling':tooling}.items()},'reviewer':{'session':'/root/review_8011','report':ref,'references':[{'path':str(root/p),'sha256':sha(root/p)} for p in ['check8090/independent-result.json','check8090/independent.py','check8090/mutation-binding.json','8090-reviewer-archive-map.json','check8090/external-source-bindings.json','check8090/weyl-v3.pdf','check8090/lr-v3.pdf','check8090/original/outputs/native_interacting_weyl_2026_09_13.json']]},'notes':notes,'non_science_notes':exempt,'boundary':'Preexecution mechanical receipt only. Independent source corrections confirmed; no final review PASS or fresh execution claimed.'}
assert not (root/'8090-unit-v1-preexecution.json').exists();(root/'8090-unit-v1-preexecution.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'tree':record['source']['tree'],'source_paths':len(paths),'original_dispositions':len(rows),'history_exemptions':len(exempt),'runtime':len(runtime),'helpers':len(helpers),'parents':len(parents),'notes':notes},indent=2))
