"""Root-dispatched future staging only; no primary execution or helper-map mutation."""
from pathlib import Path
import argparse,ast,gzip,hashlib,json,re,subprocess,sys
sys.dont_write_bytecode=True
PR=8162
R=Path('/private/tmp/review-drain-20260915');W=R/('author-draft-slot' if PR==8029 else 'review-meta-slot');owner='PR8029' if PR==8029 else 'PR8162-author'
ap=argparse.ArgumentParser();ap.add_argument('--expected-base',required=True);ap.add_argument('--stage-authorized',action='store_true',required=True);ap.add_argument('--version',required=True);args=ap.parse_args();assert re.fullmatch('v[1-9][0-9]*',args.version)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ref=lambda p:dict(path=str(p),sha256=sha(p));bind=lambda ps:[dict(path=p,sha256=sha(W/p)) for p in sorted(set(ps))];git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
prep=R/f'drain{PR}-author-prepared-v{1 if PR==8029 else 3}.json';d=json.loads(prep.read_text());frozen=d['files'] if PR==8029 else d['paths'];notes=[d['note']] if PR==8029 else d['notes'];runners=[d['runner']] if PR==8029 else d['runners'];count=57 if PR==8029 else 90
assert len(frozen)==(61 if PR==8029 else 96);assert json.loads((R/(W.name+'.json')).read_text())['owner']==owner
assert git('rev-parse','HEAD')==args.expected_base==git('rev-parse','origin/main');assert not git('diff','--name-only','HEAD');assert not git('diff','--cached','--name-only')
for e in frozen:assert sha(W/e['path'])==e['sha256'],e['path']
assert set(git('ls-files','--others','--exclude-standard').splitlines())=={e['path'] for e in frozen}
if PR==8029:assert sha(W/d['parent']['path'])==d['parent']['sha256'],'Actual landed8028 parent changed: original reviewer confirmation required'
files={k:R/f'drain{PR}-author-{k}-{args.version}.json' for k in ['unit-draft','source-handoff','cache-api']};assert all(not p.exists() for p in files.values())
sys.path[:0]=[str(W/'scripts'),str(W/'docs/audit/scripts')];import runner_cache as c,audit_packet_script_deps as a,build_citation_graph as g
context=[];parents=[];runtime=[];ns=[];apis=[]
for p in notes:
 body=(W/p).read_text();primary=re.search(r'^runner: (.+)$',body,re.M)[1];cid=g.claim_id_from_path(W/p);hp=g.helper_runner_paths_for_claim(cid,primary);packet=a.helper_runner_paths_for_claim(cid,Path(primary).stem);assert not hp and not packet
 deps=[d['parent']['path']] if PR==8029 else json.loads(re.search(r'^upstream_dependencies: (.+)$',body,re.M)[1]);cites=sorted(x.relative_to(W).as_posix() for x in g.extract_citations(body,W/p));assert set(deps)<=set(cites)
 parents+=deps;context+=cites
 ns.append(dict(path=p,claim_id=cid,declared_claim_id=re.search(r'^claim_id: (.+)$',body,re.M)[1],claim_type='bounded_theorem',primary_runner=primary,helpers=[],citations=cites,repository_dependencies=deps,dependency_rationale='Exactly the linked mathematical parent; other history and context do not supply premises.'))
for p in runners:
 ins=list(c.declared_input_paths(W/p));assert not a.transitive_helpers(Path(p).stem);assert c.declared_timeout_for(W/p)==180;context+=ins;runtime+=ins+[p]
 apis.append(dict(primary=p,timeout=180,declared_inputs=ins,runtime_closure=bind(ins+[p]),declared_input_fingerprint=c.declared_input_fingerprint(W/p),cache_status=c.cache_status(p),packet_transitive_helpers=[]))
manifest=W/f'docs/work_history/review_loop/pr{PR}'/('original-manifest.json' if PR==8029 else 'manifest.json')
m=json.loads(manifest.read_text());m=m if PR==8029 else m['paths'];assert len(m)==count;disps=[]
for e in m:
 stored=e['stored'] if PR==8029 else e['archive'];assert hashlib.sha256(gzip.decompress((W/stored).read_bytes())).hexdigest()==e['sha256'];disps.append(dict(original_path=e['path'],original_mode=e['mode'],original_blob=e['blob'],original_sha256=e['sha256'],final_path=stored,final_sha256=sha(W/stored),disposition=e['disposition'],canonical_path=e.get('canonical_path')))
if PR==8162:
 mapped={x['original']:x['disposition'] for x in json.loads((R/'drain8162-author-checks-v2.json').read_text())['all90_dispositions']}
 for x in disps:x['disposition']+='; '+mapped[x['original_path']]
subprocess.run(['git','-C',str(W),'add','--',*[e['path'] for e in frozen]],check=True)
subprocess.run(['git','-C',str(W),'diff','--cached','--check'],check=True);paths=git('diff','--cached','--name-only').splitlines();assert set(paths)=={e['path'] for e in frozen}
files['cache-api'].write_text(json.dumps(apis,indent=2)+'\n');review=ref(R/f'drain{PR}-original-review.json');refs=[ref(prep),ref(manifest),ref(files['cache-api'])]
if PR==8162:refs.extend([ref(R/'drain8162-author-checks-v2.json'),ref(R/'drain8162-author-checks-v3.json')])
h=dict(status='AUTHOR DRAFT; SAME ORIGINAL REVIEWER COLD CONFIRMATION REQUIRED',base=args.expected_base,tree=git('write-tree'),original_dispositions=disps,claim_dispositions=d.get('finding_dispositions',d.get('proof_mapping')),current_main_preservation='Only frozen new additions; no tracked-file or helper-map changes.',references=refs,execution_plan=d.get('resource_plan',d.get('proposed_capture')));files['source-handoff'].write_text(json.dumps(h,indent=2)+'\n')
context+=notes+[f'docs/work_history/review_loop/pr{PR}/README.md']
if PR==8162:context+=['docs/COMPACT_DETERMINANT_CURRENTS_SIGNED_SECTORS_AND_FINITE_CYCLIC_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-14.md']
tooling=['docs/audit/scripts/build_citation_graph.py','docs/audit/scripts/static_pipeline_checkpoint.py','scripts/runner_cache.py','scripts/audit_packet_script_deps.py','docs/audit/scripts/ledger_io.py','docs/audit/data/axiom_premise_nodes.json','docs/audit/data/doc_authority_registry.json']
head='c5f58f84246c7ee938152dcc317264f8b1384a3f' if PR==8029 else '0f02dc5127416f347e231bbd8aa7c2a8b58a02fa';base='36843ba7b46901269911496f8dfdef6fd5f63cae' if PR==8029 else 'e0ef7cf4633034a8c1e6d57f5812cc4275bf1349'
record=dict(schema_version=2,unit_id=f'PR{PR}',constituents=[dict(id=f'PR{PR}',head=head,delta_base=base,dispositions=dict(ref(files['source-handoff']),json_pointer='/original_dispositions'))],source=dict(base=args.expected_base,commit=args.expected_base,tree=git('write-tree'),paths=bind(paths),deleted_paths=[]),inputs=dict(runtime=bind(runtime),helpers=[],parents=bind(parents),context=bind(context),tooling=bind(tooling)),reviewer=dict(session=('/root/review_8012' if PR==8029 else '/root/review_8161')+'; final source confirmation pending',report=review,references=refs+[ref(files['source-handoff'])]),notes=ns,supporting_proofs=[],non_science_notes=[dict(path=f'docs/work_history/review_loop/pr{PR}/README.md',rationale='Exact original recovery only.',review_reference=review)])
files['unit-draft'].write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(ref(files['unit-draft'])))
