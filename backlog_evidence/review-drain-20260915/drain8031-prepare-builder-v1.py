from pathlib import Path
import json,hashlib,sys,ast
R=Path('/private/tmp/review-drain-20260915');W=R/'review-draft-slot';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
d=json.loads((R/'drain8031-author-prepared-v2.json').read_text());assert sha(R/'drain8031-author-prepared-v2.json')=='f206fc8429d05078570eb74b21a14b6b7ed025e10ffb5284b3848bba8bcc181d'
frozen=[dict(e,mode=oct((W/e['path']).stat().st_mode&0o777)) for e in d['source']];assert len(frozen)==74
(R/'drain8031-source-freeze-v2.json').write_text(json.dumps(frozen,indent=2)+'\n')
skill='docs/ai_methodology/skills/review-loop';paths=[skill+'/SKILL.md',skill+'/PREFLIGHT.md',skill+'/scripts/review_receipt.py',skill+'/scripts/review_workspace.py']+[p.relative_to(W).as_posix() for p in (W/skill/'references').glob('*.md')]
authorities=[dict(path=p,sha256=sha(W/p)) for p in paths];(R/'drain8031-builder-authority-v1.json').write_text(json.dumps(authorities,indent=2)+'\n')
plan=json.loads((R/'drain8031-resource-plan-v2.json').read_text());p=plan['runner'];tree=ast.parse((W/p).read_text());call=next(x.value for x in tree.body if isinstance(x,ast.Expr) and isinstance(x.value,ast.Call) and isinstance(x.value.func,ast.Name) and x.value.func.id=='_emit');assert ast.literal_eval(call.args[1])==17;scopes=ast.literal_eval(call.args[2]);assert sum(v['checks'] for v in scopes.values())==17
plan.update(schema_version=1,unique_programs=1,sequence=[p],source_sha256=sha(W/p),total_stdout='TOTAL: PASS=17 FAIL=0',json_TOTAL=17,scientific_checks=16,resource_checks=1,N5=scopes,local_import_helpers=[],import_cost='SymPy initialization after alarm and literal proof reads; no local helper or top-level imported primary.',status='Plan only; root dispatch after fresh-base cheap and original reviewer cold confirmation')
(R/'drain8031-capture-plan-v1.json').write_text(json.dumps(plan,indent=2)+'\n')
refs=['drain8031-review.json','drain8031-review.md','drain8031-early-affected-review-v2.json','drain8031-early-affected-review-v2.md','drain8031-author-prepared-v2.json','drain8031-author-prepared-v1.json','drain8031-original-manifest.json','drain8031-author-corrections-v1.patch','drain8031-author-corrections-v2.patch','drain8031-canonical-note-snapshot-v1.md','drain8031-canonical-runner-snapshot-v1.py','drain8031-source-freeze-v2.json','drain8031-builder-authority-v1.json','drain8031-capture-plan-v1.json','drain8031-author-discovery-v2.json']
refs=[dict(path=str(R/p),sha256=sha(R/p)) for p in refs]
body='''"""Future root-run PR8031 staging builder. Preparation does not execute this script."""
from pathlib import Path
import argparse,ast,gzip,hashlib,json,re,subprocess,sys,traceback
sys.dont_write_bytecode=True
assert __debug__
R=Path('/private/tmp/review-drain-20260915');W=R/'review-draft-slot'
IMMUTABLE_REFS=__REFS__
ap=argparse.ArgumentParser();ap.add_argument('--expected-base',required=True);ap.add_argument('--stage-authorized',action='store_true',required=True);ap.add_argument('--version',required=True);args=ap.parse_args()
assert args.stage_authorized and re.fullmatch('[0-9a-f]{40}',args.expected_base) and re.fullmatch('v[1-9][0-9]*',args.version)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ref=lambda p:dict(path=str(p),sha256=sha(p))
bind=lambda ps:[dict(path=p,sha256=sha(W/p)) for p in sorted(set(ps))]
git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
failure=R/f'drain8031-builder-failure-{args.version}.json'
def run():
 assert not failure.exists()
 for e in IMMUTABLE_REFS:assert sha(Path(e['path']))==e['sha256']
 d=json.loads((R/'drain8031-author-prepared-v2.json').read_text());frozen=json.loads((R/'drain8031-source-freeze-v2.json').read_text());assert len(frozen)==74
 owner=json.loads((R/'review-draft-slot.json').read_text());assert owner['owner']=='PR8031-author' and Path(owner['path']).resolve()==W.resolve()
 assert git('rev-parse','HEAD')==args.expected_base==git('rev-parse','origin/main')
 assert not git('diff','--name-only','HEAD') and not git('diff','--cached','--name-only')
 assert set(git('ls-files','--others','--exclude-standard').splitlines())=={e['path'] for e in frozen}
 assert not git('ls-files','--others','--ignored','--exclude-standard')
 for e in frozen:
  p=W/e['path'];assert p.is_file() and not p.is_symlink() and sha(p)==e['sha256'] and oct(p.stat().st_mode&0o777)==e['mode']
 authorities=json.loads((R/'drain8031-builder-authority-v1.json').read_text())
 for e in authorities:assert sha(W/e['path'])==e['sha256'],'Authority changed; rebind with reviewer: '+e['path']
 outputs={k:R/f'drain8031-author-{k}-{args.version}.json' for k in ['unit-draft','source-handoff','cache-api']};assert all(not p.exists() for p in outputs.values())
 manifest=json.loads((W/'docs/work_history/review_loop/pr8031/manifest.json').read_text());orig=json.loads((R/'drain8031-original-manifest.json').read_text());assert len(manifest['files'])==len(orig['files'])==70
 originals={e['path']:e for e in orig['files']};disps=[]
 for e in manifest['files']:
  o=originals[e['path']];assert all(e[k]==o[k] for k in ['mode','blob','sha256'])
  raw=gzip.decompress((W/e['recovery']).read_bytes());assert hashlib.sha256(raw).hexdigest()==e['sha256'] and hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\\0'+raw).hexdigest()==e['blob']
  target=e['canonical'] or e['recovery'];disps.append(dict(original_path=e['path'],original_mode=e['mode'],original_blob=e['blob'],original_sha256=e['sha256'],final_path=target,final_sha256=sha(W/target),recovery=orig['head']+':'+e['path']+'; exact gzip '+e['recovery'],disposition=e['disposition']))
 sys.path[:0]=[str(W/'scripts'),str(W/'docs/audit/scripts')]
 import runner_cache as c,audit_packet_script_deps as a,build_citation_graph as g
 registry=['scripts/audit_packet_script_deps.py','docs/audit/scripts/build_citation_graph.py'];before={p:sha(W/p) for p in registry}
 note=next(e['path'] for e in frozen if e['path'].startswith('docs/GAUGE_'));body=(W/note).read_text();p='scripts/gauge_wilson_finite_transporter_pw_defect_check_2026_09_07.py';parent='docs/GAUGE_WILSON_COMPACT_CUBE_FINITE_QUBIT_CUTOFF_BOUNDED_THEOREM_NOTE_2026-09-07.md';cid=g.claim_id_from_path(W/note)
 assert g.extract_runner(body,note)==p
 assert not g.helper_runner_paths_for_claim(cid,p) and not a.helper_runner_paths_for_claim(cid,Path(p).stem) and not a.transitive_helpers(Path(p).stem) and not g.resolve_helper_runner_paths(p),'Helper discovery changed; no registry edits permitted'
 cites=sorted(x.relative_to(W).as_posix() for x in g.extract_citations(body,W/note));assert {x for x in cites if x.startswith('docs/GAUGE_')}=={parent}
 assert '  - '+Path(parent).stem.lower() in body
 inputs=list(c.declared_input_paths(W/p));assert inputs==[note,parent] and c.declared_timeout_for(W/p)==180
 tree=ast.parse((W/p).read_text());compile(tree,p,'exec');values={n.targets[0].id:ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id in ['_INPUT_SHA256','AUDIT_RSS_LIMIT_MIB']}
 assert values['_INPUT_SHA256']==d['runtime_inputs']=={x:sha(W/x) for x in inputs} and values['AUDIT_RSS_LIMIT_MIB']==180
 apis=[dict(runner=p,declared_inputs=inputs,runtime_closure=bind(inputs+[p]),declared_input_fingerprint=c.declared_input_fingerprint(W/p),timeout=180,rss_MiB=180,packet_transitive_helpers=[])]
 assert git('rev-parse','HEAD')==args.expected_base==git('rev-parse','origin/main')
 assert not git('diff','--name-only','HEAD') and not git('diff','--cached','--name-only')
 for e in frozen:assert sha(W/e['path'])==e['sha256']
 subprocess.run(['git','-C',str(W),'add','--',*[e['path'] for e in frozen]],check=True)
 subprocess.run(['git','-C',str(W),'diff','--cached','--check'],check=True)
 staged=git('diff','--cached','--name-only').splitlines();assert set(staged)=={e['path'] for e in frozen};assert before=={p:sha(W/p) for p in registry} and not git('diff','--name-only')
 stagedtree=git('write-tree');outputs['cache-api'].write_text(json.dumps(apis,indent=2)+'\\n')
 claims=[dict(claim='Supplied full-irrep PW compression, shell support, kernel/eigenvalue/norm identities and energy/distinct-link path estimates',disposition='Complete positive analytic proof retained, with explicit a>0, integer R>=1 for energy, retained input and acceptance conditions.'),dict(claim='General finite tensor trace identity',disposition='Positive identity without covariance-unitarity contradiction inference.'),dict(claim='Universal finite-unitarity and negative-convergence certification',disposition='Deferred; full original proof and v1 author snapshot retained, branch must survive partial closure. N1 packet incomplete does not refute mathematics.'),dict(claim='Finite numerical evidence',disposition='Actual57x57 one-link R1 fixture;16 mathematics plus1resource; no spatial or lattice-wide/path execution.')]
 refs=IMMUTABLE_REFS+[ref(outputs['cache-api'])]
 handoff=dict(status='AUTHOR HANDOFF ONLY; CURRENT-BASE COLD AND FINAL EVIDENCE CONFIRMATION PENDING',author='/root/resume_8077',base=args.expected_base,tree=stagedtree,original_dispositions=disps,claim_dispositions=claims,registry_changes=[],registry_unchanged=before,references=refs,branch_retention_required=True)
 outputs['source-handoff'].write_text(json.dumps(handoff,indent=2)+'\\n')
 context=set(cites)|{e['path'] for e in authorities}|{'docs/work_history/review_loop/pr8031/manifest.json'}
 tooling=registry+['scripts/runner_cache.py','docs/audit/scripts/static_pipeline_checkpoint.py','docs/audit/scripts/ledger_io.py','docs/audit/data/axiom_premise_nodes.json','docs/audit/data/doc_authority_registry.json']
 record=dict(schema_version=2,unit_id='PR8031',constituents=[dict(id='PR8031',head=orig['head'],delta_base=orig['base'],dispositions=dict(ref(outputs['source-handoff']),json_pointer='/original_dispositions'))],source=dict(base=args.expected_base,commit=args.expected_base,tree=stagedtree,paths=bind(staged),deleted_paths=[]),inputs=dict(runtime=bind(inputs+[p]),helpers=[],parents=bind([parent]),context=bind(context),tooling=bind(tooling)),reviewer=dict(session='/root/review_8031; fresh-base cold and final confirmation pending',report=ref(R/'drain8031-review.json'),references=refs+[ref(outputs['source-handoff'])]),notes=[dict(path=note,claim_id=cid,declared_claim_id=Path(note).stem.lower(),claim_type='bounded_theorem',primary_runner=p,helpers=[],citations=cites,repository_dependencies=[parent],dependency_rationale='Actual supplied Haar full-irrep cutoff and electric spectrum; static-source trial context does not create a premise edge.')],supporting_proofs=[],non_science_notes=[dict(path='docs/work_history/review_loop/pr8031/README.md',rationale='Exact archival recovery and historical scope, no autonomous scientific claim.',review_reference=ref(R/'drain8031-early-affected-review-v2.json'))])
 outputs['unit-draft'].write_text(json.dumps(record,indent=2)+'\\n');print(json.dumps(ref(outputs['unit-draft'])));print(stagedtree)
try:run()
except BaseException as exc:
 if not failure.exists():failure.write_text(json.dumps(dict(status='FAILED; preserve state',error=repr(exc),traceback=traceback.format_exc()),indent=2)+'\\n')
 raise
'''.replace('__REFS__',repr(refs))
ast.parse(body);(R/'drain8031-build-staged-draft-v1.py').write_text(body)
print(json.dumps({'builder_sha256':sha(R/'drain8031-build-staged-draft-v1.py'),'capture_plan_sha256':sha(R/'drain8031-capture-plan-v1.json'),'executed':False}))
