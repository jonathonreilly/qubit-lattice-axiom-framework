"""Root-dispatched staging/schema2 binding; never executes science or cache checks."""
from pathlib import Path
import argparse,ast,gzip,hashlib,json,re,subprocess,sys
sys.dont_write_bytecode=True
R=Path('/private/tmp/review-drain-20260915');W=R/'author-draft-slot'
ap=argparse.ArgumentParser();ap.add_argument('--expected-base',required=True);ap.add_argument('--stage-authorized',action='store_true',required=True);ap.add_argument('--version',required=True);args=ap.parse_args()
assert args.stage_authorized and re.fullmatch('[0-9a-f]{40}',args.expected_base) and re.fullmatch('v[1-9][0-9]*',args.version)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ref=lambda p:dict(path=str(p),sha256=sha(p))
bind=lambda ps:[dict(path=p,sha256=sha(W/p)) for p in sorted(set(ps))]
git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
prep=R/'drain8030-author-prepared-v2.json';assert sha(prep)=='1590d90251d6bcf433cb67d59bbeda58a7dd81c81a5a73c6eb2ed7d753d55f2f'
d=json.loads(prep.read_text());frozen=d['files'];assert len(frozen)==94
owner=json.loads((R/'author-draft-slot.json').read_text());assert owner['owner']=='PR8030-author' and Path(owner['path']).resolve()==W.resolve()
assert git('rev-parse','HEAD')==args.expected_base==git('rev-parse','origin/main')
assert not git('diff','--name-only','HEAD') and not git('diff','--cached','--name-only')
assert set(git('ls-files','--others','--exclude-standard').splitlines())=={e['path'] for e in frozen}
for e in frozen:assert sha(W/e['path'])==e['sha256'],e['path']
for e in d['parents']:assert sha(W/e['path'])==e['sha256'],'Parent changed; original reviewer must confirm: '+e['path']
files={k:R/f'drain8030-author-{k}-{args.version}.json' for k in ['unit-draft','source-handoff','cache-api']};assert all(not p.exists() for p in files.values())
review=R/'drain8030-original-review.json';original=json.loads(review.read_text());m=json.loads((W/'docs/work_history/review_loop/pr8030/manifest.json').read_text());orig={e['path']:e for e in original['original_dispositions']};assert len(m['paths'])==len(orig)==89
assert {e['path'] for e in m['paths']}==set(orig);disps=[]
for e in m['paths']:
 o=orig[e['path']];assert all(e[k]==o[k] for k in ['mode','blob','sha256'])
 b=gzip.decompress((W/e['stored']).read_bytes());assert hashlib.sha256(b).hexdigest()==e['sha256'];assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['blob']
 disps.append(dict(original_path=e['path'],original_mode=e['mode'],original_blob=e['blob'],original_sha256=e['sha256'],final_path=e['stored'],final_sha256=sha(W/e['stored']),recovery=m['head']+':'+e['path'],recovery_encoding='gzip; exact decoded original bytes',disposition=e['disposition'],canonical_path=e.get('canonical_path')))
registry=['scripts/audit_packet_script_deps.py','docs/audit/scripts/build_citation_graph.py'];replacements={};preservation={}
def mapping(text):
 return ast.literal_eval(next(n.value for n in ast.parse(text).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='EXPLICIT_PACKET_HELPER_RUNNER_PATHS' for t in n.targets)))
assert len(d['helper_map_plan'])==1
for p in registry:
 text=(W/p).read_text();old=mapping(text);assert not set(old)&set(d['helper_map_plan']);marker='EXPLICIT_PACKET_HELPER_RUNNER_PATHS = {';assert text.count(marker)==1
 new=text.replace(marker,marker+'\n'+''.join('    '+repr(k)+': '+repr(v)+',\n' for k,v in d['helper_map_plan'].items()),1);after=mapping(new);assert after==dict(old,**d['helper_map_plan']);replacements[p]=new;preservation[p]={'before_sha256':sha(W/p),'existing_entries_preserved':len(old),'added':d['helper_map_plan']}
# All guards/archive checks precede mutation. Registry imports below are metadata APIs only.
for p,new in replacements.items():(W/p).write_text(new)
sys.path[:0]=[str(W/'scripts'),str(W/'docs/audit/scripts')]
import runner_cache as c,audit_packet_script_deps as a,build_citation_graph as g
note=d['note'];body=(W/note).read_text();primary=re.search(r'^runner: (.+)$',body,re.M)[1];cid=g.claim_id_from_path(W/note);hp=list(g.helper_runner_paths_for_claim(cid,primary));packet=list(a.helper_runner_paths_for_claim(cid,Path(primary).stem));assert set(hp)==set(packet)==set(d['runners'][1:]);assert primary==d['runners'][0]
deps=json.loads(re.search(r'^upstream_dependencies: (.+)$',body,re.M)[1]);assert deps==[e['path'] for e in d['parents']]
cites=sorted(x.relative_to(W).as_posix() for x in g.extract_citations(body,W/note));assert set(deps)<=set(cites)
apis=[];runtime=[]
for p in d['runners']:
 tree=ast.parse((W/p).read_text());compile(tree,p,'exec');ins=list(c.declared_input_paths(W/p));assert ins==d['inputs'];assert c.declared_timeout_for(W/p)==180;assert not a.transitive_helpers(Path(p).stem)
 for n in tree.body:
  if isinstance(n,ast.Assert) and isinstance(n.test,ast.Compare) and isinstance(n.test.left,ast.Constant) and isinstance(n.test.comparators[0],ast.Subscript):
   sub=n.test.comparators[0]
   if isinstance(sub.value,ast.Name) and sub.value.id=='_INPUT_TEXT':assert n.test.left.value in (W/ast.literal_eval(sub.slice)).read_text()
 runtime+=ins+[p];apis.append(dict(primary=p,timeout=180,declared_inputs=ins,runtime_closure=bind(ins+[p]),declared_input_fingerprint=c.declared_input_fingerprint(W/p),cache_status=c.cache_status(p),packet_transitive_helpers=[]))
subprocess.run(['git','-C',str(W),'add','--',*[e['path'] for e in frozen],*registry],check=True);subprocess.run(['git','-C',str(W),'diff','--cached','--check'],check=True)
paths=git('diff','--cached','--name-only').splitlines();assert set(paths)=={e['path'] for e in frozen}|set(registry);assert not git('diff','--name-only');tree=git('write-tree')
files['cache-api'].write_text(json.dumps(apis,indent=2)+'\n')
refs=[ref(R/x) for x in ['drain8030-author-prepared-v2.json','drain8030-early-affected-review-v1.json','drain8030-affected-fix-confirmation-v2.json','drain8030-capture-plan-v1.json']]+[ref(files['cache-api'])]
h=dict(status='AUTHOR HANDOFF ONLY; FINAL ORIGINAL REVIEWER COLD CONFIRMATION PENDING',author='/root/resume_8077',base=args.expected_base,tree=tree,original_dispositions=disps,claim_dispositions={'retained':d['accepted_scope'],'deferred':d['deferred_scope'],'branch_preservation_required':True},registry_preservation=preservation,execution_plan=d['resource_plan'],references=refs)
files['source-handoff'].write_text(json.dumps(h,indent=2)+'\n')
context=set(cites)|set(d['inputs'])|{'docs/work_history/review_loop/pr8030/README.md','docs/work_history/review_loop/pr8030/manifest.json'}
tooling=['docs/audit/scripts/build_citation_graph.py','docs/audit/scripts/static_pipeline_checkpoint.py','scripts/runner_cache.py','scripts/audit_packet_script_deps.py','docs/audit/scripts/ledger_io.py','docs/audit/data/axiom_premise_nodes.json','docs/audit/data/doc_authority_registry.json']
record=dict(schema_version=2,unit_id='PR8030',constituents=[dict(id='PR8030',head=m['head'],delta_base=m['delta_base'],dispositions=dict(ref(files['source-handoff']),json_pointer='/original_dispositions'))],source=dict(base=args.expected_base,commit=args.expected_base,tree=tree,paths=bind(paths),deleted_paths=[]),inputs=dict(runtime=bind(runtime),helpers=bind(hp),parents=bind(deps),context=bind(context),tooling=bind(tooling)),reviewer=dict(session='/root/review_8012; final source confirmation pending',report=ref(review),references=refs+[ref(files['source-handoff'])]),notes=[dict(path=note,claim_id=cid,declared_claim_id=re.search(r'^claim_id: (.+)$',body,re.M)[1],claim_type='bounded_theorem',primary_runner=primary,helpers=hp,citations=cites,repository_dependencies=deps,dependency_rationale='Four actual linked mathematical parents; partial quantitative/FDD salvage, with both negative certifications deferred.')],supporting_proofs=[],non_science_notes=[dict(path='docs/work_history/review_loop/pr8030/README.md',rationale='Exact recovery and deferred-scope provenance only.',review_reference=ref(review))])
files['unit-draft'].write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(ref(files['unit-draft'])));print(tree)
