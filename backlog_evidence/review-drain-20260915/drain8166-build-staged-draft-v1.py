"""Future PR8166 root-dispatched builder; preparation never executes this file."""
from pathlib import Path
import argparse,ast,gzip,hashlib,json,re,subprocess,sys,traceback
sys.dont_write_bytecode=True
assert __debug__
R=Path('/private/tmp/review-drain-20260915');W=R/'review-meta-slot'
REFS=[{'path': '/private/tmp/review-drain-20260915/drain8166-original-review.json', 'sha256': 'd46fa51e307c98eb295be9e5e746dc6dffb383b2260901ba3247ab2f617d6b10'}, {'path': '/private/tmp/review-drain-20260915/drain8166-original-review.md', 'sha256': '0a6fb3fcfcbb201b09a775fe71050c68a9efd26f3c8f039e9a6d9b54eadc44d3'}, {'path': '/private/tmp/review-drain-20260915/drain8166-early-review-v2.json', 'sha256': 'd182629d34b3c2bd1fae7f4823b6fc7fce4bde40b371973ab4179e25b8cd29aa'}, {'path': '/private/tmp/review-drain-20260915/drain8166-early-review-v2.md', 'sha256': 'b50a656f0731402729c4ff34830a82984c2ef65a73e9bf77e236c7b16331d024'}, {'path': '/private/tmp/review-drain-20260915/drain8166-author-prepared-v3.json', 'sha256': 'd370c74c677eb87546f788b4a711db02e0fc7608a2c387d173522652f392723a'}, {'path': '/private/tmp/review-drain-20260915/drain8166-source-freeze-v3.json', 'sha256': '2d8f40b46c53a62b8d382041dec17313b121b53b7996eb3c20e61ab7520c070c'}, {'path': '/private/tmp/review-drain-20260915/drain8166-author-corrections-v3.patch', 'sha256': '6a9ca09736bb5787534eab66efebef6998d544a8ecca4109fbc12706f988a59b'}, {'path': '/private/tmp/review-drain-20260915/drain8166-author-corrections-v1.patch', 'sha256': '4d6738d891ad31e07d1f6679dd18c79ceb7211631bd3378ce7a0ab4e7fcb8a9a'}, {'path': '/private/tmp/review-drain-20260915/drain8166-author-corrections-v2.patch', 'sha256': 'bbfdaa231f6d1fd01af06c86a8578573e2186b0210878410f40f613ad9ebdd2f'}, {'path': '/private/tmp/review-drain-20260915/drain8166-proof-preservation-v1.json', 'sha256': 'a46a3c61cd6b18e92feb74667fb09d64fa1a2f16cfadfc255f13fc288808d632'}, {'path': '/private/tmp/review-drain-20260915/drain8166-resource-input-plan-v3.json', 'sha256': '8f54bf0cac1ed12e409678cfed6576fa762f78602156e8f0f0409fd7e8e1113b'}, {'path': '/private/tmp/review-drain-20260915/drain8166-builder-authority-v1.json', 'sha256': '33f4bd65415b8296667bbd7e550125ce3a27518a2f56f502987258ffa15bf617'}, {'path': '/private/tmp/review-drain-20260915/drain8166-capture-plan-v1.json', 'sha256': '9254889a9f7e64a665e75d6fedc4b8d20caa42f67648e9dff3264d7fa34c6f12'}]
ap=argparse.ArgumentParser();ap.add_argument('--expected-base',required=True);ap.add_argument('--stage-authorized',action='store_true',required=True);ap.add_argument('--version',required=True);args=ap.parse_args()
assert args.stage_authorized and re.fullmatch('[0-9a-f]{40}',args.expected_base) and re.fullmatch('v[1-9][0-9]*',args.version)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ref=lambda p:dict(path=str(p),sha256=sha(p))
bind=lambda paths:[dict(path=p,sha256=sha(W/p)) for p in sorted(set(paths))]
git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
failure=R/f'drain8166-builder-failure-{args.version}.json'
def run():
 assert not failure.exists()
 for e in REFS:assert sha(Path(e['path']))==e['sha256']
 d=json.loads((R/'drain8166-author-prepared-v3.json').read_text());frozen=d['source'];assert len(frozen)==133
 owner=json.loads((R/'review-meta-slot.json').read_text());assert owner['owner']=='PR8166-author' and Path(owner['path']).resolve()==W.resolve()
 assert git('rev-parse','HEAD')==args.expected_base==git('rev-parse','origin/main')
 assert not git('diff','--name-only','HEAD') and not git('diff','--cached','--name-only')
 assert set(git('ls-files','--others','--exclude-standard').splitlines())=={e['path'] for e in frozen}
 assert not git('ls-files','--others','--ignored','--exclude-standard')
 for e in frozen:
  p=W/e['path'];assert p.is_file() and not p.is_symlink() and sha(p)==e['sha256'] and oct(p.stat().st_mode&0o777)==e['mode']
 authorities=json.loads((R/'drain8166-builder-authority-v1.json').read_text())
 for e in authorities+d['mathematical_external_closure']:assert sha(W/e['path'])==e['sha256'],'Authority/parent change requires reviewer rebinding: '+e['path']
 outputs={k:R/f'drain8166-author-{k}-{args.version}.json' for k in ['unit-draft','source-handoff','cache-api']};assert all(not p.exists() for p in outputs.values())
 original=json.loads((R/'drain8166-original-review.json').read_text());orig={e['path']:e for e in original['original_dispositions']};manifest=json.loads((W/'docs/work_history/review_loop/pr8166/manifest.json').read_text());assert len(orig)==len(manifest['files'])==123
 disps=[]
 for e in manifest['files']:
  o=orig[e['original_path']];assert e['original_mode']==o['mode'] and e['original_blob']==o['blob'] and e['original_sha256']==o['sha256']
  raw=gzip.decompress((W/e['recovery']).read_bytes());assert hashlib.sha256(raw).hexdigest()==o['sha256'] and hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==o['blob']
  target=e['canonical'] or e['recovery'];disps.append(dict(e,final_path=target,final_sha256=sha(W/target),recovery=original['head']+':'+e['original_path']+'; gzip '+e['recovery']))
 sys.path[:0]=[str(W/'scripts'),str(W/'docs/audit/scripts')]
 import runner_cache as c,audit_packet_script_deps as a,build_citation_graph as g
 registry=['scripts/audit_packet_script_deps.py','docs/audit/scripts/build_citation_graph.py'];before={p:sha(W/p) for p in registry}
 notes=[];apis=[];runtime=set();parents=set();citesall=set();helpers=set()
 for row,plan in zip(d['notes'],d['runtime_plan']):
  n=row['path'];p=row['primary'];text=(W/n).read_text();cid=g.claim_id_from_path(W/n);assert g.extract_runner(text,n)==p
  expected=plan['helpers'];assert list(g.helper_runner_paths_for_claim(cid,p))==list(a.helper_runner_paths_for_claim(cid,Path(p).stem))==expected
  assert sorted(a.transitive_helpers(Path(p).stem))==sorted(Path(x).stem for x in expected),'Actual imports differ; no map changes authorized'
  inputs=list(c.declared_input_paths(W/p));assert inputs==[e['path'] for e in plan['runtime_inputs']] and c.declared_timeout_for(W/p)==120
  tree=ast.parse((W/p).read_text());compile(tree,p,'exec');vals={x.targets[0].id:ast.literal_eval(x.value) for x in tree.body if isinstance(x,ast.Assign) and isinstance(x.targets[0],ast.Name) and x.targets[0].id in ['EXPECTED_INPUT_SHA256','AUDIT_RSS_LIMIT_MIB']};assert vals['EXPECTED_INPUT_SHA256']=={x:sha(W/x) for x in inputs}=={e['path']:e['sha256'] for e in plan['runtime_inputs']} and vals['AUDIT_RSS_LIMIT_MIB']==384
  closure=set(inputs+[p])
  for h in expected:closure.update(c.declared_input_paths(W/h));closure.add(h)
  citations=sorted(x.relative_to(W).as_posix() for x in g.extract_citations(text,W/n));assert set(row['mathematical_parents'])<=set(citations)
  assert json.loads(re.search(r'^upstream_dependencies: (.+)$',text,re.M)[1])==[Path(x).stem.lower() for x in row['mathematical_parents']]
  notes.append(dict(path=n,claim_id=cid,declared_claim_id=Path(n).stem.lower(),claim_type='bounded_theorem',primary_runner=p,helpers=expected,citations=citations,repository_dependencies=row['mathematical_parents'],dependency_rationale='Full scoped positive proof dependencies; integer Hamiltonian application includes actual infinite-volume path construction, abstract probability theorem remains conditional.'))
  apis.append(dict(runner=p,declared_inputs=inputs,declared_input_fingerprint=c.declared_input_fingerprint(W/p),runtime_closure=bind(closure),actual_helpers=expected,timeout=120,rss_MiB=384));runtime.update(closure);parents.update(row['mathematical_parents']);citesall.update(citations);helpers.update(expected)
 assert git('rev-parse','HEAD')==args.expected_base==git('rev-parse','origin/main') and not git('diff','--name-only','HEAD')
 for e in frozen:assert sha(W/e['path'])==e['sha256']
 subprocess.run(['git','-C',str(W),'add','--',*[e['path'] for e in frozen]],check=True);subprocess.run(['git','-C',str(W),'diff','--cached','--check'],check=True)
 staged=git('diff','--cached','--name-only').splitlines();assert set(staged)=={e['path'] for e in frozen} and not git('diff','--name-only') and before=={p:sha(W/p) for p in registry}
 tree=git('write-tree');outputs['cache-api'].write_text(json.dumps(apis,indent=2)+'\n');refs=REFS+[ref(outputs['cache-api'])]
 handoff=dict(status='AUTHOR HANDOFF; CURRENT-BASE COLD AND FINAL EVIDENCE CONFIRMATION PENDING',author='/root/resume_8077',base=args.expected_base,tree=tree,original_dispositions=disps,claim_dispositions=d['claim_dispositions'],negative_certification=d['negative_certification'],branch_retention_required=True,registry_changes=[],registry_unchanged=before,references=refs)
 outputs['source-handoff'].write_text(json.dumps(handoff,indent=2)+'\n')
 context=citesall|{e['path'] for e in authorities}|{'docs/work_history/review_loop/pr8166/manifest.json'}
 tooling=registry+['scripts/runner_cache.py','docs/audit/scripts/static_pipeline_checkpoint.py','docs/audit/scripts/ledger_io.py','docs/audit/data/axiom_premise_nodes.json','docs/audit/data/doc_authority_registry.json']
 record=dict(schema_version=2,unit_id='PR8166',constituents=[dict(id='PR8166',head=original['head'],delta_base=original['merge_base'],dispositions=dict(ref(outputs['source-handoff']),json_pointer='/original_dispositions'))],source=dict(base=args.expected_base,commit=args.expected_base,tree=tree,paths=bind(staged),deleted_paths=[]),inputs=dict(runtime=bind(runtime),helpers=bind(helpers),parents=bind(parents),context=bind(context),tooling=bind(tooling)),reviewer=dict(session='/root/review_8166; current-base cold and final evidence confirmation pending',report=ref(R/'drain8166-original-review.json'),references=refs+[ref(outputs['source-handoff'])]),notes=notes,supporting_proofs=[],non_science_notes=[dict(path='docs/work_history/review_loop/pr8166/README.md',rationale='Exact historical recovery and scope only, not an autonomous scientific claim.',review_reference=ref(R/'drain8166-early-review-v2.json'))])
 outputs['unit-draft'].write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(ref(outputs['unit-draft'])));print(tree)
try:run()
except BaseException as exc:
 if not failure.exists():failure.write_text(json.dumps(dict(error=repr(exc),traceback=traceback.format_exc(),status='FAILED; preserve source/index state'),indent=2)+'\n')
 raise
