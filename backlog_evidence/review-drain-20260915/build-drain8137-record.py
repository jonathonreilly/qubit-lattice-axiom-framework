from pathlib import Path
import sys, json, hashlib, subprocess, importlib.util
r=Path('/private/tmp/review-drain-20260915'); w=r/'drain-author8137'
phase=sys.argv[1]; report=r/sys.argv[2]; dispositions=r/sys.argv[3]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ref=lambda p:{'path':str(p),'sha256':sha(p)}
git=lambda *args:subprocess.check_output(['git','-C',str(w),*args],text=True).strip()
spec=importlib.util.spec_from_file_location('rr',w/'docs/ai_methodology/skills/review-loop/scripts/review_receipt.py');rr=importlib.util.module_from_spec(spec);spec.loader.exec_module(rr);g,c,a=rr.repository_apis(w)
paths=git('diff','--cached','--name-only').splitlines(); n='docs/SEQUENTIAL_FORMATION_PATH_AND_STAR_IDENTITIES_BOUNDED_THEOREM_NOTE_2026-09-15.md';primary='scripts/possibility_symmetric_sequential_variation_forces_order_dependence_2026_09_15.py';body=(w/n).read_text();citations=sorted(x.relative_to(w).as_posix() for x in g.extract_citations(body,w/n));parents=[p for p in citations if p.startswith('docs/')]
helpers=g.helper_runner_paths_for_claim(g.claim_id_from_path(w/n),primary);assert not helpers
runtime=list(c.declared_input_paths(primary));runtime.append(primary)
tooling=['docs/audit/scripts/build_citation_graph.py','docs/audit/scripts/static_pipeline_checkpoint.py','scripts/runner_cache.py','scripts/audit_packet_script_deps.py','docs/audit/scripts/ledger_io.py','docs/audit/data/axiom_premise_nodes.json','docs/audit/data/doc_authority_registry.json']
bind=lambda ps:[{'path':p,'sha256':sha(w/p)} for p in sorted(set(ps))]
context_paths={x['path'] for x in json.loads((r/'drain8137-original-review.json').read_text())['input_bindings']}
context_paths.update(str(p.relative_to(w)) for p in (w/'docs/ai_methodology/skills/review-loop').rglob('*.md'))
references=[ref(r/p) for p in ['drain8137-original-review.json','drain8137-independent-controls.py','drain8137-independent-controls.json']]
if phase=='final':references=json.loads(report.read_text())['references']
for reference in references:assert sha(Path(reference['path']))==reference['sha256']
record={'schema_version':2,'unit_id':'PR8137-positive-'+phase,'constituents':[{'id':'8137','head':'d15d5d9074e343563700691afcfddb5afc761a21','delta_base':'5deabeb698a27c2c3f68c5df685af2521ef15307','dispositions':dict(ref(dispositions),json_pointer='/original_dispositions')}], 'source':{'base':'59024639572d6d3a1091c727297b18c350d3f484','commit':git('rev-parse','HEAD'),'tree':git('write-tree'),'paths':bind(paths),'deleted_paths':[]},'inputs':{'runtime':bind(runtime),'helpers':[],'parents':bind(parents),'context':bind(context_paths | (set(citations)-set(parents))),'tooling':bind(tooling)},'reviewer':{'session':'/root/review_8011','report':ref(report),'references':references},'notes':[{'path':n,'claim_id':g.claim_id_from_path(w/n),'declared_claim_id':'sequential_formation_path_and_star_identities_bounded_theorem_note_2026-09-15','claim_type':'bounded_theorem','primary_runner':primary,'helpers':[],'citations':citations,'repository_dependencies':parents,'dependency_rationale':'Linked current framework authority and realized-state primitive delimit premise grants. Sequential products, menus and covariance are explicitly supplied mathematical model assumptions; positive identities do not use deferred general negative certification.'}],'non_science_notes':[{'path':p,'rationale':'Exact historical campaign narrative; no additional current proof or scientific authority. Independent reviewer read all ten original campaign files and confirmed this disposition.','review_reference':ref(report)} for p in paths if p.endswith('.md') and p!=n],'supporting_proofs':[]}
target=r/('drain8137-unit-'+phase+'.json');assert not target.exists();target.write_text(json.dumps(record,indent=2)+'\n');print(target)
