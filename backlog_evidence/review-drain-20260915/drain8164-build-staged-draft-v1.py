"""Future root-run staging/binding only. Current APIs already resolve03→02; no registry edit."""
from pathlib import Path
import argparse,ast,gzip,hashlib,json,re,subprocess,sys
sys.dont_write_bytecode=True
R=Path('/private/tmp/review-drain-20260915');W=R/'drain-author-slot'
ap=argparse.ArgumentParser();ap.add_argument('--expected-base',required=True);ap.add_argument('--stage-authorized',action='store_true',required=True);ap.add_argument('--version',required=True);args=ap.parse_args();assert args.stage_authorized and re.fullmatch('[0-9a-f]{40}',args.expected_base) and re.fullmatch('v[1-9][0-9]*',args.version)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ref=lambda p:dict(path=str(p),sha256=sha(p));bind=lambda ps:[dict(path=p,sha256=sha(W/p)) for p in sorted(set(ps))];git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
prep=R/'drain8164-author-prepared-v1.json';assert sha(prep)=='2ed40d6f9d42e7053822e4ca62d63041518d145417f414345f3e98275130a11a';d=json.loads(prep.read_text());assert len(d['files'])==196
owner=json.loads((R/'drain-author-slot.json').read_text());assert owner['owner']=='PR8164-author' and Path(owner['path']).resolve()==W.resolve()
assert git('rev-parse','HEAD')==args.expected_base==git('rev-parse','origin/main');assert not git('diff','--name-only','HEAD') and not git('diff','--cached','--name-only')
assert set(git('ls-files','--others','--exclude-standard').splitlines())=={e['path'] for e in d['files']}
for e in d['files']:assert sha(W/e['path'])==e['sha256'],e['path']
files={k:R/f'drain8164-author-{k}-{args.version}.json' for k in ['unit-draft','source-handoff','cache-api']};assert all(not p.exists() for p in files.values())
review=R/'drain8164-original-review.json';original=json.loads(review.read_text());assert sha(review)=='2df0a061e704714b80e35d067ddd72d3ded9fa17c5fae7e448138897b33a6da6'
early=R/'drain8164-early-affected-review-v1.json';assert sha(early)=='44e96fd0b67e3475191e7a0b73e2f7130b7da26db2e2879452454a7a422516bb'
refs=[ref(R/x) for x in ['drain8164-author-prepared-v1.json','drain8164-early-affected-review-v1.json','drain8164-author-resource-plan-v1.json','drain8164-author-preservation-checks-v1.json','drain8164-capture-plan-v1.json']]
disps=[];orig={e['path']:e for e in original['path_dispositions']}
for e in d['original_dispositions']:
 o=orig[e['original_path']];assert e['original_mode']==o['mode'] and e['original_blob']==o['blob'] and e['original_sha256']==o['sha256']
 b=gzip.decompress((W/e['archive']).read_bytes());assert hashlib.sha256(b).hexdigest()==e['original_sha256'];assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['original_blob']
 disps.append(dict(original_path=e['original_path'],original_mode=e['original_mode'],original_blob=e['original_blob'],original_sha256=e['original_sha256'],final_path=e['archive'],final_sha256=sha(W/e['archive']),recovery=e['recovery'],disposition=e['disposition'],canonical_path=e['canonical_path']))
assert len(disps)==178 and {e['original_path'] for e in disps}==set(orig)
sys.path[:0]=[str(W/'scripts'),str(W/'docs/audit/scripts')];import runner_cache as c,audit_packet_script_deps as a,build_citation_graph as g
notes=[];context=set();helpers=set();runtime=set();parents=set();apis=[];mathclosure=[]
def closure(p,seen=None):
 seen=set() if seen is None else seen
 for dep in d['dependencies'][p]:
  if dep not in seen:seen.add(dep);closure(dep,seen)
 return seen
for p in d['notes']:
 body=(W/p).read_text();primary=re.search(r'^runner: (.+)$',body,re.M)[1];cid=g.claim_id_from_path(W/p);hp=list(g.helper_runner_paths_for_claim(cid,primary));packet=list(a.helper_runner_paths_for_claim(cid,Path(primary).stem));expected=d['helper_map_plan'].get(cid,[])
 assert set(hp)==set(packet)==set(expected),'API helper closure changed; stop for review, do not guess a registry patch'
 helpers.update(hp);cites=sorted(x.relative_to(W).as_posix() for x in g.extract_citations(body,W/p));deps=d['dependencies'][p];assert set(deps)<=set(cites);context.update(cites);mp=closure(p);parents.update(mp);mathclosure.append(dict(owner=p,parents=bind(mp),scope='Complete internal mathematical dependency closure; separate from actual runtime reads.'))
 notes.append(dict(path=p,claim_id=cid,declared_claim_id=re.search(r'^claim_id: (.+)$',body,re.M)[1],claim_type='bounded_theorem',primary_runner=primary,helpers=hp,citations=cites,repository_dependencies=deps,dependency_rationale='Actual supplied finite-box/response/corrector premises only;05–08 independently redeclare models; no implicit8160/8162/8163 premise.'))
for e in d['runtime_plan']:
 p=e['runner'];ins=list(c.declared_input_paths(W/p));assert ins==e['declared_inputs'] and c.declared_timeout_for(W/p)==180
 hp=sorted('scripts/'+h+'.py' for h in a.transitive_helpers(Path(p).stem));assert hp==sorted(e['helpers']);cl=set(ins)
 for h in hp:cl.add(h);cl.update(c.declared_input_paths(W/h) or [])
 runtime.update(cl|{p});context.update(ins);assert e['note_pin'] in (W/ins[0]).read_text()
 apis.append(dict(primary=p,timeout=180,declared_inputs=ins,packet_transitive_helpers=hp,runtime_closure=bind(cl),declared_input_fingerprint=c.declared_input_fingerprint(W/p),cache_status=c.cache_status(p)))
assert {x['primary_runner'] for x in notes}|helpers==set(d['runners'])
subprocess.run(['git','-C',str(W),'add','--',*[e['path'] for e in d['files']]],check=True);subprocess.run(['git','-C',str(W),'diff','--cached','--check'],check=True)
paths=git('diff','--cached','--name-only').splitlines();assert set(paths)=={e['path'] for e in d['files']};assert not git('diff','--name-only');tree=git('write-tree')
files['cache-api'].write_text(json.dumps(apis,indent=2)+'\n')
h=dict(status='AUTHOR HANDOFF ONLY; FINAL ORIGINAL REVIEWER COLD CONFIRMATION REQUIRED',author='/root/resume_8077',base=args.expected_base,tree=tree,original_dispositions=disps,claim_dispositions=original['claims_and_boundaries'],mathematical_premise_closure=mathclosure,registry_disposition='No changes: both actual APIs resolve03→02 already; every old registry byte preserved.',execution_plan=d['resource_plan'],references=refs+[ref(files['cache-api'])]);files['source-handoff'].write_text(json.dumps(h,indent=2)+'\n')
context.update(d['notes']);context.update(['docs/work_history/review_loop/pr8164/README.md','docs/work_history/review_loop/pr8164/manifest.json'])
tooling=['docs/audit/scripts/build_citation_graph.py','docs/audit/scripts/static_pipeline_checkpoint.py','scripts/runner_cache.py','scripts/audit_packet_script_deps.py','docs/audit/scripts/ledger_io.py','docs/audit/data/axiom_premise_nodes.json','docs/audit/data/doc_authority_registry.json']
record=dict(schema_version=2,unit_id='PR8164',constituents=[dict(id='PR8164',head=original['head'],delta_base=original['merge_base'],dispositions=dict(ref(files['source-handoff']),json_pointer='/original_dispositions'))],source=dict(base=args.expected_base,commit=args.expected_base,tree=tree,paths=bind(paths),deleted_paths=[]),inputs=dict(runtime=bind(runtime),helpers=bind(helpers),parents=bind(parents),context=bind(context),tooling=bind(tooling)),reviewer=dict(session='/root/review_8160; final staged source confirmation pending',report=ref(review),references=refs+[ref(files['source-handoff']),ref(files['cache-api'])]),notes=notes,supporting_proofs=[],non_science_notes=[dict(path='docs/work_history/review_loop/pr8164/README.md',rationale='Exact historical recovery and scope only.',review_reference=ref(review))])
files['unit-draft'].write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(ref(files['unit-draft'])));print(tree)
