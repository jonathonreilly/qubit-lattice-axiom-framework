from pathlib import Path
import hashlib,json,subprocess,sys,re,gzip
r=Path(__file__).resolve().parent;w=r/'author-draft-slot'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ref=lambda p:dict(path=str(p),sha256=sha(p))
bind=lambda ps:[dict(path=p,sha256=sha(w/p)) for p in sorted(set(ps))]
git=lambda *a:subprocess.check_output(['git','-C',str(w),*a],text=True).strip()
review=r/'drain8027-original-review.json';assert review.exists()
original=json.loads((r/'drain8027-original-inventory.json').read_text())
mapping=json.loads((w/'docs/work_history/review_loop/pr8027/original-manifest.json').read_text())
assert len(mapping)==len(original['original_paths'])==73
disps=[]
for e in mapping:
 p=e['stored'];assert hashlib.sha256(gzip.decompress((w/p).read_bytes())).hexdigest()==e['sha256']
 disps.append(dict(original_path=e['path'],original_sha256=e['sha256'],final_path=p,final_sha256=sha(w/p),disposition='Exact original historical recovery; one new canonical note and two runners separately retained with packaging corrections. Prior main repairs preserved instead of stale branch versions. Independent scientific dispositions remain in original reviewer report.',recovery=e['head']+':'+e['path']))
sys.path[:0]=[str(w/'scripts'),str(w/'docs/audit/scripts')]
import build_citation_graph as g,audit_packet_script_deps as a,runner_cache as c
paths=git('diff','--cached','--name-only').splitlines();notes=[];parents=[];context=[];runners=[];apis=[]
for p in paths:
 if not p.startswith('docs/GAUGE_WILSON_') or not p.endswith('.md'):continue
 body=(w/p).read_text();primary=re.search(r'^runner: (.+)$',body,re.M)[1]
 cites=sorted(x.relative_to(w).as_posix() for x in g.extract_citations(body,w/p));context+=cites;runners.append(primary)
 deps=[x for x in cites if x.startswith('docs/GAUGE_WILSON_')];parents+=deps
 helper_paths=g.helper_runner_paths_for_claim(g.claim_id_from_path(w/p),primary);assert len(helper_paths)==1
 for hp in helper_paths:
  context.extend(c.declared_input_paths(w/hp));runners.append(hp)
  apis.append(dict(primary=hp,primary_sha256=sha(w/hp),timeout=c.declared_timeout_for(w/hp),declared_inputs=list(c.declared_input_paths(w/hp)),declared_input_fingerprint=c.declared_input_fingerprint(w/hp),cache_status=c.cache_status(w/hp),helpers=[]))
 inputs=c.declared_input_paths(w/primary);assert inputs;context+=list(inputs)
 apis.append(dict(primary=primary,primary_sha256=sha(w/primary),timeout=c.declared_timeout_for(w/primary),declared_inputs=list(inputs),declared_input_fingerprint=c.declared_input_fingerprint(w/primary),cache_status=c.cache_status(w/primary),helpers=[]))
 notes.append(dict(path=p,claim_id=g.claim_id_from_path(w/p),declared_claim_id=re.search(r'^claim_id: (.+)$',body,re.M)[1],claim_type='bounded_theorem',primary_runner=primary,helpers=helper_paths,citations=cites,repository_dependencies=deps,dependency_rationale='Supplied compact SU(3) Hamiltonian normalization and explicit static source carrier; complete finite-box geodesic equality space, exact first-order matrix and planar spectrum with next-branch splitting. Analytical classification and fixed-box remainder are distinct from finite controls. No uniform confinement or axiom selection. Original independent confirmation required.'))
api=r/'drain8027-author-cache-api-v1.json';assert not api.exists();api.write_text(json.dumps(apis,indent=2)+'\n')
context += [n['path'] for n in notes]+['docs/MINIMAL_AXIOMS_2026-06-29.md','docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md','docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md','docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md','docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md']
tooling=['docs/audit/scripts/build_citation_graph.py','docs/audit/scripts/static_pipeline_checkpoint.py','scripts/runner_cache.py','scripts/audit_packet_script_deps.py','docs/audit/scripts/ledger_io.py','docs/audit/data/axiom_premise_nodes.json','docs/audit/data/doc_authority_registry.json']
handoff={'status':'AUTHOR DRAFT; NOT SCIENTIFIC PASS','author':'/root/resume_8077','base':git('rev-parse','HEAD'),'tree':git('write-tree'),'original_dispositions':disps,'original_inventory':ref(r/'drain8027-original-inventory.json'),'original_review':ref(review),'preservation':'All 73 original path/mode/blob versions preserved; existing current-main science untouched; two tool mappings retain all existing entries and add exactly the reviewed claim helper. New note and two runners retain all mathematics and finite fixtures. Input pins, cache links, canonical footers and historical labels repaired; original primary section4 next-branch corollary surfaced from the existing full spectrum. Honest N1–N8 finite/analytical scope added.','execution_plan':{'timeout_seconds_per_runner':180,'process_tree_rss_limit_bytes':180*1048576,'concurrency':1,'state':'Not executed; original cold confirmation plus cheap preflight required.'}}
h=r/'drain8027-author-source-handoff-v1.json';assert not h.exists();h.write_text(json.dumps(handoff,indent=2)+'\n')
rr=ref(h);record={'schema_version':2,'unit_id':'PR8027','constituents':[dict(id='PR8027',head=original['head'],delta_base=original['delta_base'],dispositions=dict(rr,json_pointer='/original_dispositions'))],'source':dict(base=git('rev-parse','HEAD'),commit=git('rev-parse','HEAD'),tree=git('write-tree'),paths=bind(paths),deleted_paths=[]),'inputs':dict(runtime=bind(runners),helpers=bind([hp for n in notes for hp in n['helpers']]),parents=bind(parents),context=bind(context),tooling=bind(tooling)),'reviewer':dict(session='/root/review_8012 original session; affected-source confirmation pending',report=ref(review),references=[rr,ref(api)]),'notes':notes,'supporting_proofs':[],'non_science_notes':[dict(path=p,rationale='Historical recovery instructions; no current science authority or active proof input.',review_reference=ref(review)) for p in paths if p.endswith('.md') and p not in [n['path'] for n in notes]]}
out=r/'drain8027-author-unit-draft-v1.json';assert not out.exists();out.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(ref(out)));print(record['source']['tree'])
