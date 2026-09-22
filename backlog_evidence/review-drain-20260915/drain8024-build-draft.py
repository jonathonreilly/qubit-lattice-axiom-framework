from pathlib import Path
import hashlib,json,subprocess,sys,re,gzip
r=Path(__file__).resolve().parent;w=r/'author-draft-slot'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ref=lambda p:dict(path=str(p),sha256=sha(p))
bind=lambda ps:[dict(path=p,sha256=sha(w/p)) for p in sorted(set(ps))]
git=lambda *a:subprocess.check_output(['git','-C',str(w),*a],text=True).strip()
review=r/'drain8024-original-review.json';assert review.exists()
original=json.loads((r/'drain8024-original-inventory.json').read_text())
mapping=json.loads((w/'docs/work_history/review_loop/pr8024/original-manifest.json').read_text())
assert len(mapping)==len(original['original_paths'])==75
disps=[]
for e in mapping:
 p=e['stored'];assert hashlib.sha256(gzip.decompress((w/p).read_bytes())).hexdigest()==e['sha256']
 disps.append(dict(original_path=e['path'],original_sha256=e['sha256'],final_path=p,final_sha256=sha(w/p),disposition='Exact original historical recovery; one new canonical note/runner pair separately retained with packaging corrections. Prior main repairs preserved instead of stale branch versions. Independent scientific dispositions remain in original reviewer report.',recovery=e['head']+':'+e['path']))
sys.path[:0]=[str(w/'scripts'),str(w/'docs/audit/scripts')]
import build_citation_graph as g,audit_packet_script_deps as a,runner_cache as c
paths=git('diff','--cached','--name-only').splitlines();notes=[];parents=[];context=[];runners=[];apis=[]
for p in paths:
 if not p.startswith('docs/GAUGE_WILSON_') or not p.endswith('.md'):continue
 body=(w/p).read_text();primary=re.search(r'^runner: (.+)$',body,re.M)[1]
 cites=sorted(x.relative_to(w).as_posix() for x in g.extract_citations(body,w/p));context+=cites;runners.append(primary)
 deps=[x for x in cites if x.startswith('docs/GAUGE_WILSON_')];parents+=deps
 assert not a.transitive_helpers(Path(primary).stem)
 inputs=c.declared_input_paths(w/primary);assert inputs;context+=list(inputs)
 apis.append(dict(primary=primary,primary_sha256=sha(w/primary),timeout=c.declared_timeout_for(w/primary),declared_inputs=list(inputs),declared_input_fingerprint=c.declared_input_fingerprint(w/primary),cache_status=c.cache_status(w/primary),helpers=[]))
 notes.append(dict(path=p,claim_id=g.claim_id_from_path(w/p),declared_claim_id=re.search(r'^claim_id: (.+)$',body,re.M)[1],claim_type='bounded_theorem',primary_runner=primary,helpers=[],citations=cites,repository_dependencies=deps,dependency_rationale='Supplied compact SU(3) Hamiltonian, all-label Casimir bound and full-irrep cutoff carrier; explicit Yarotsky stability import supplies volume-uniform theorem. No physical action or clock selection. Original independent confirmation required.'))
api=r/'drain8024-author-cache-api-v1.json';assert not api.exists();api.write_text(json.dumps(apis,indent=2)+'\n')
context += [n['path'] for n in notes]+['docs/MINIMAL_AXIOMS_2026-06-29.md','docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md','docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md','docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md','docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md']
tooling=['docs/audit/scripts/build_citation_graph.py','docs/audit/scripts/static_pipeline_checkpoint.py','scripts/runner_cache.py','scripts/audit_packet_script_deps.py','docs/audit/scripts/ledger_io.py','docs/audit/data/axiom_premise_nodes.json','docs/audit/data/doc_authority_registry.json']
handoff={'status':'AUTHOR DRAFT; NOT SCIENTIFIC PASS','author':'/root','base':git('rev-parse','HEAD'),'tree':git('write-tree'),'original_dispositions':disps,'original_inventory':ref(r/'drain8024-original-inventory.json'),'original_review':ref(review),'preservation':'All 75 original path/mode/blob versions preserved; all existing current-main paths untouched. New note/runner retain all mathematics and finite fixtures. Only input pins, cache links, canonical footer and historical label wording changed.','execution_plan':{'timeout_seconds_per_runner':180,'process_tree_rss_limit_bytes':180*1048576,'concurrency':1,'state':'Not executed; original cold confirmation plus cheap preflight required.'}}
h=r/'drain8024-author-source-handoff-v1.json';assert not h.exists();h.write_text(json.dumps(handoff,indent=2)+'\n')
rr=ref(h);record={'schema_version':2,'unit_id':'PR8024','constituents':[dict(id='PR8024',head=original['headRefOid'],delta_base=original['delta_base'],dispositions=dict(rr,json_pointer='/original_dispositions'))],'source':dict(base=git('rev-parse','HEAD'),commit=git('rev-parse','HEAD'),tree=git('write-tree'),paths=bind(paths),deleted_paths=[]),'inputs':dict(runtime=bind(runners),helpers=[],parents=bind(parents),context=bind(context),tooling=bind(tooling)),'reviewer':dict(session='/root/review_8012 original session; affected-source confirmation pending',report=ref(review),references=[rr,ref(api)]),'notes':notes,'supporting_proofs':[],'non_science_notes':[dict(path=p,rationale='Historical recovery instructions; no current science authority or active proof input.',review_reference=ref(review)) for p in paths if p.endswith('.md') and p not in [n['path'] for n in notes]]}
out=r/'drain8024-author-unit-draft-v1.json';assert not out.exists();out.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(ref(out)));print(record['source']['tree'])
