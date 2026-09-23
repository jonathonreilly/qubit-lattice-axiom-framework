"""Future root-run PR8168 staging builder. Preparation does not execute this script."""
from pathlib import Path
import argparse,ast,gzip,hashlib,json,re,subprocess,sys,traceback
sys.dont_write_bytecode=True
assert __debug__
R=Path('/private/tmp/review-drain-20260915');W=R/'drain-author-slot'
IMMUTABLE_REFS=[{'path': '/private/tmp/review-drain-20260915/drain8168-report.json', 'sha256': 'a934e181b84b8b0329ad11ba95f805e042f7be897a2793b601e03c48d9304836'}, {'path': '/private/tmp/review-drain-20260915/drain8168-report.md', 'sha256': '5241978303d313789f2d077dfa81879b1e5c31b52aa05efd94a12e0cff849fc6'}, {'path': '/private/tmp/review-drain-20260915/drain8168-early-v2-review.json', 'sha256': 'c021b0da480f41da562b4ba584b506d1c6fd2c331f47737407dfc50714db38de'}, {'path': '/private/tmp/review-drain-20260915/drain8168-early-v2-review.md', 'sha256': '4dde4217fbb4614583fd57102e55f69a53d14c731d63f1bc05078e059bbd62f1'}, {'path': '/private/tmp/review-drain-20260915/drain8168-author-prepared-v3.json', 'sha256': '671224aafc0200851d6e34bc659a222e324b6876d00ba4f0d8d6f2f038e67ba9'}, {'path': '/private/tmp/review-drain-20260915/drain8168-author-source-freeze-v3.json', 'sha256': 'fbc259909980595b9872fdf5b0cffcb6f4e34c0308dbf0c90c654c29b75dd09e'}, {'path': '/private/tmp/review-drain-20260915/drain8168-author-prepared-v2.json', 'sha256': 'c9c30e23a8ae66bd62c76325532b265ba9d8127dea8420fb1c94ab3d0bab3309'}, {'path': '/private/tmp/review-drain-20260915/drain8168-manifest.json', 'sha256': 'b3d7699a6f5f8f1c49f39147f2b3acf6322222ccd5c36ad5eeab359ba5d74073'}, {'path': '/private/tmp/review-drain-20260915/drain8168-dispositions.json', 'sha256': '67cd989fe9729d7d35ef2f01580c0f0d70a68c8a39b79c113357a4767b399699'}, {'path': '/private/tmp/review-drain-20260915/drain8168-freeze.json', 'sha256': '577876db59c98d4423b97d8e5f5f22502d9bd9897fc07dfcfb3e7144f13c7c5f'}, {'path': '/private/tmp/review-drain-20260915/drain8168-provenance-checks.json', 'sha256': 'f5a04f28cfd886187c9d3dcc0c3f4db0e9c11936b4f8f6ae8e9139e602c18525'}, {'path': '/private/tmp/review-drain-20260915/drain8168-author-corrections-v1.patch', 'sha256': '9d3e0d390f8ee40b6c68d2a570d44f4c8732cea31125cdf80a855961653543e0'}, {'path': '/private/tmp/review-drain-20260915/drain8168-author-corrections-v2.patch', 'sha256': '500018326c9289cd1e5fd0f0a6cd8add753501a3b81e683a7030f0405860a7cc'}, {'path': '/private/tmp/review-drain-20260915/drain8168-author-corrections-v3.patch', 'sha256': '78c87ca97151bd345231767bec68d6c3c338f0baf1481713cdccf6e77139f491'}, {'path': '/private/tmp/review-drain-20260915/drain8168-capture-plan-v1.json', 'sha256': 'fca207b3776ddedc53e8305ddf2a67c26c98726da55a296a63d6371e6f4a9140'}, {'path': '/private/tmp/review-drain-20260915/drain8168-builder-authority-v1.json', 'sha256': '33f4bd65415b8296667bbd7e550125ce3a27518a2f56f502987258ffa15bf617'}]
ap=argparse.ArgumentParser();ap.add_argument('--expected-base',required=True);ap.add_argument('--stage-authorized',action='store_true',required=True);ap.add_argument('--version',required=True);args=ap.parse_args()
assert args.stage_authorized and re.fullmatch('[0-9a-f]{40}',args.expected_base) and re.fullmatch('v[1-9][0-9]*',args.version)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ref=lambda p:dict(path=str(p),sha256=sha(p))
bind=lambda ps:[dict(path=p,sha256=sha(W/p)) for p in sorted(set(ps))]
git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
failure=R/f'drain8168-builder-failure-{args.version}.json'
def run():
 assert not failure.exists()
 for e in IMMUTABLE_REFS:assert sha(Path(e['path']))==e['sha256']
 d=json.loads((R/'drain8168-author-prepared-v3.json').read_text());frozen=json.loads((R/'drain8168-author-source-freeze-v3.json').read_text());assert len(frozen)==31
 owner=json.loads((R/'drain-author-slot.json').read_text());assert owner['owner']=='PR8168-author' and Path(owner['path']).resolve()==W.resolve()
 assert git('rev-parse','HEAD')==args.expected_base==git('rev-parse','origin/main')
 assert not git('diff','--name-only','HEAD') and not git('diff','--cached','--name-only')
 assert set(git('ls-files','--others','--exclude-standard').splitlines())=={e['path'] for e in frozen}
 assert not git('ls-files','--others','--ignored','--exclude-standard')
 for e in frozen:
  p=W/e['path'];assert p.is_file() and not p.is_symlink() and sha(p)==e['sha256'] and oct(p.stat().st_mode&0o777)==e['mode']
 authorities=json.loads((R/'drain8168-builder-authority-v1.json').read_text())
 for e in authorities:assert sha(W/e['path'])==e['sha256'],'Authority changed; rebind with reviewer: '+e['path']
 outputs={k:R/f'drain8168-author-{k}-{args.version}.json' for k in ['unit-draft','source-handoff','cache-api']};assert all(not p.exists() for p in outputs.values())
 manifest=json.loads((W/'docs/work_history/review_loop/pr8168/manifest.json').read_text());orig=json.loads((R/'drain8168-freeze.json').read_text());originals={e['path']:e['head'] for e in json.loads((R/'drain8168-manifest.json').read_text())};assert len(manifest['files'])==len(originals)==27
 disps=[]
 for e in manifest['files']:
  o=originals[e['original_path']];assert e['original_mode']==o['mode'] and e['original_blob']==o['blob'] and e['original_sha256']==o['sha256']
  raw=gzip.decompress((W/e['recovery']).read_bytes());assert hashlib.sha256(raw).hexdigest()==o['sha256'] and hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==o['blob']
  target=e['canonical'] or e['recovery'];disps.append(dict(e,final_path=target,final_sha256=sha(W/target),recovery=orig['headRefOid']+':'+e['original_path']+'; exact gzip '+e['recovery']))
 sys.path[:0]=[str(W/'scripts'),str(W/'docs/audit/scripts')]
 import runner_cache as c,audit_packet_script_deps as a,build_citation_graph as g
 registry=['scripts/audit_packet_script_deps.py','docs/audit/scripts/build_citation_graph.py'];before={p:sha(W/p) for p in registry}
 note='docs/ADMISSIBILITY_RULE_THREE_DIMENSIONAL_FORMATION_LAW_ORDERED_PHASE_STABILITY_OF_THE_NOISY_LEVEL_AUTOMATON_EXPLICIT_THRESHOLD_SIX_INVARIANT_LAWS_BOUNDED_THEOREM_NOTE_2026-09-16.md';p='scripts/admissibility_rule_three_dimensional_formation_law_ordered_phase_stability_noisy_level_automaton_2026_09_16.py';body=(W/note).read_text();cid=g.claim_id_from_path(W/note)
 assert g.extract_runner(body,note)==p
 assert not g.helper_runner_paths_for_claim(cid,p) and not a.helper_runner_paths_for_claim(cid,Path(p).stem) and not a.transitive_helpers(Path(p).stem) and not g.resolve_helper_runner_paths(p),'No registry changes authorized'
 parents=[e['path'] for e in d['mathematical_parents']]
 for e in d['mathematical_parents']+d['context']:assert sha(W/e['path'])==e['sha256']
 cites=sorted(x.relative_to(W).as_posix() for x in g.extract_citations(body,W/note));assert set(parents)<=set(cites)
 assert set(cites)-set(parents)=={'docs/work_history/review_loop/pr8168/README.md'}
 inputs=list(c.declared_input_paths(W/p));assert inputs==list(d['runtime_inputs']) and c.declared_timeout_for(W/p)==900
 tree=ast.parse((W/p).read_text());compile(tree,p,'exec');values={x.targets[0].id:ast.literal_eval(x.value) for x in tree.body if isinstance(x,ast.Assign) and isinstance(x.targets[0],ast.Name) and x.targets[0].id in ['EXPECTED_INPUT_SHA256','AUDIT_RSS_LIMIT_MIB']}
 assert values['EXPECTED_INPUT_SHA256']==d['runtime_inputs']=={x:sha(W/x) for x in inputs} and values['AUDIT_RSS_LIMIT_MIB']==512
 apis=[dict(runner=p,declared_inputs=inputs,runtime_closure=bind(inputs+[p]),mathematical_closure=bind(parents),declared_input_fingerprint=c.declared_input_fingerprint(W/p),timeout=900,rss_MiB=512,packet_transitive_helpers=[],output_contract='stdout only; no JSON output')]
 assert git('rev-parse','HEAD')==args.expected_base==git('rev-parse','origin/main')
 assert not git('diff','--name-only','HEAD') and not git('diff','--cached','--name-only')
 for e in frozen:assert sha(W/e['path'])==e['sha256']
 subprocess.run(['git','-C',str(W),'add','--',*[e['path'] for e in frozen]],check=True)
 subprocess.run(['git','-C',str(W),'diff','--cached','--check'],check=True)
 staged=git('diff','--cached','--name-only').splitlines();assert set(staged)=={e['path'] for e in frozen};assert before=={p:sha(W/p) for p in registry} and not git('diff','--name-only')
 stagedtree=git('write-tree');outputs['cache-api'].write_text(json.dumps(apis,indent=2)+'\n')
 claims=d['claim_dispositions']
 refs=IMMUTABLE_REFS+[ref(outputs['cache-api'])]
 handoff=dict(status='AUTHOR HANDOFF ONLY; CURRENT-BASE COLD AND FINAL EVIDENCE CONFIRMATION PENDING',author='/root/resume_8077',base=args.expected_base,tree=stagedtree,original_dispositions=disps,claim_dispositions=claims,registry_changes=[],registry_unchanged=before,references=refs,branch_retention_required=True)
 outputs['source-handoff'].write_text(json.dumps(handoff,indent=2)+'\n')
 context=set(cites)|{e['path'] for e in d['context']}|{e['path'] for e in authorities}|{'docs/work_history/review_loop/pr8168/manifest.json'}
 tooling=registry+['scripts/runner_cache.py','docs/audit/scripts/static_pipeline_checkpoint.py','docs/audit/scripts/ledger_io.py','docs/audit/data/axiom_premise_nodes.json','docs/audit/data/doc_authority_registry.json']
 record=dict(schema_version=2,unit_id='PR8168',constituents=[dict(id='PR8168',head=orig['headRefOid'],delta_base=orig['merge_base'],dispositions=dict(ref(outputs['source-handoff']),json_pointer='/original_dispositions'))],source=dict(base=args.expected_base,commit=args.expected_base,tree=stagedtree,paths=bind(staged),deleted_paths=[]),inputs=dict(runtime=bind(inputs+[p]),helpers=[],parents=bind(parents),context=bind(context),tooling=bind(tooling)),reviewer=dict(session='/root/review_8168; fresh-base cold and final confirmation pending',report=ref(R/'drain8168-report.json'),references=refs+[ref(outputs['source-handoff'])]),notes=[dict(path=note,claim_id=cid,declared_claim_id=Path(note).stem.lower(),claim_type='bounded_theorem',primary_runner=p,helpers=[],citations=cites,repository_dependencies=parents,dependency_rationale='Supplied product-rule conditional and spatially invariant stationary-law correspondence; static reflection result is context only.')],supporting_proofs=[],non_science_notes=[dict(path='docs/work_history/review_loop/pr8168/README.md',rationale='Exact archival recovery and historical scope, no autonomous scientific claim.',review_reference=ref(R/'drain8168-early-v2-review.json'))])
 outputs['unit-draft'].write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(ref(outputs['unit-draft'])));print(stagedtree)
try:run()
except BaseException as exc:
 if not failure.exists():failure.write_text(json.dumps(dict(status='FAILED; preserve state',error=repr(exc),traceback=traceback.format_exc()),indent=2)+'\n')
 raise
