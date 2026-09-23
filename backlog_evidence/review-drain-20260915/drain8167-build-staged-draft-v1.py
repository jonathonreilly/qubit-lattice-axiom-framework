"""Future root-dispatched PR8167 staging/schema2 builder. NOT executed during preparation.
No science, gates, registry mutations, commits or pushes. Requires separately supplied clean original-reviewer affected report pinned by SHA; corrections invalidate this v1 builder. All guards precede staging.
"""
from pathlib import Path
import argparse,ast,gzip,hashlib,json,re,subprocess,sys,traceback
sys.dont_write_bytecode=True
assert __debug__, 'Do not optimize away guards'
R=Path('/private/tmp/review-drain-20260915');W=R/'review-meta-slot'
ap=argparse.ArgumentParser();ap.add_argument('--expected-base',required=True);ap.add_argument('--stage-authorized',action='store_true',required=True);ap.add_argument('--version',required=True);ap.add_argument('--confirmation',required=True);ap.add_argument('--confirmation-sha256',required=True);args=ap.parse_args()
assert args.stage_authorized and re.fullmatch('[0-9a-f]{40}',args.expected_base) and re.fullmatch('v[1-9][0-9]*',args.version)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ref=lambda p:dict(path=str(p),sha256=sha(p))
bind=lambda ps:[dict(path=p,sha256=sha(W/p)) for p in sorted(set(ps))]
git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
IMMUTABLE_REFS = [{'path': '/private/tmp/review-drain-20260915/drain8167-original-review.json', 'sha256': 'ad566688ec255c2a878cbddc3c73a17e451bbd6a5dc677fd4d41391156dd093b'}, {'path': '/private/tmp/review-drain-20260915/drain8167-original-review.md', 'sha256': '3237e37b066cd5141dae1cba43cb5bbb4868c66ddc10a0c2b3c979f5a1ad7b1d'}, {'path': '/private/tmp/review-drain-20260915/drain8167-author-prepared-v1.json', 'sha256': 'b1249f0427dc7e1a8523775fd6341a2a7bbb7b007b373f19af7296d63b8aa597'}, {'path': '/private/tmp/review-drain-20260915/drain8167-prepared-v1-source-freeze.json', 'sha256': '4f2760ea5c4f5cc48161f617e427039537403c99d8392d0ec628919f00fcb6ba'}, {'path': '/private/tmp/review-drain-20260915/drain8167-author-preservation-v1.json', 'sha256': '4247fc1ad2bf3f287a06afc5b3e978928c270c23d210681050a9bfb7d37302ad'}, {'path': '/private/tmp/review-drain-20260915/drain8167-author-full-mapping-v1.json', 'sha256': 'cbca5229814e6e6eae64f38d880fbf3c546711daff9361e5623d50d2c52764dc'}, {'path': '/private/tmp/review-drain-20260915/drain8167-author-input-resource-plan-v1.json', 'sha256': '872655510f529cf80c574a640a4d3e700a1dc8d6cb171db410c8d8a35c5de309'}, {'path': '/private/tmp/review-drain-20260915/drain8167-author-correction-v1.diff', 'sha256': 'fa59f54cd0ea2c9888a8c8e67f4c8069228e21a18172c26e5ffed26ac2080bf8'}, {'path': '/private/tmp/review-drain-20260915/drain8167-author-discovery-v1.json', 'sha256': 'b190ad1ef585cdc6d2460a16504c16bf21f9e8dc24e545c90ddd2b4bc9194867'}, {'path': '/private/tmp/review-drain-20260915/drain8167-capture-plan-v1.json', 'sha256': '62074117c6f73c8466b2d15104a2c9c1cc0ba317973173c89988bf68f31de4d4'}, {'path': '/private/tmp/review-drain-20260915/drain8167-original-inventory.json', 'sha256': '89dc423ecb70ead70f972fe20ea439e4f8a53951490d466a7f2aa4b8acf2a6e8'}, {'path': '/private/tmp/review-drain-20260915/drain8167-original.patch', 'sha256': '2c7e4401f6fe95cb8b1c238e3cdf4be57daaeb8c2e19e24ec85a2298c322740c'}, {'path': '/private/tmp/review-drain-20260915/drain8167-head-fetch.json', 'sha256': '4bfab24fedd4e10d71a0de75faec20ce3650dab0b5d7a4dca98462ce59480050'}, {'path': '/private/tmp/review-drain-20260915/drain8167-provenance-checks.json', 'sha256': 'ff6cf3fad7719a10c07966a2fc22179c1c3262f4d3d693b1abccbe8ccf30a5b8'}, {'path': '/private/tmp/review-drain-20260915/check8167/independent_controls.py', 'sha256': 'e7a69a07c087cb4d269c345669378427dba433810e91c0d1b5af608be7257b31'}, {'path': '/private/tmp/review-drain-20260915/check8167/independent_controls.json', 'sha256': 'f87760972e1f2e62207f2ad7c0241e5fccf798057861765c18fbf632c7944a34'}, {'path': '/private/tmp/review-drain-20260915/check8167/final-github.json', 'sha256': 'e04d311cee42fe1778bcb5ca0d63797a277f84bf771dafb16eaad4c020f32e3e'}, {'path': '/private/tmp/review-drain-20260915/drain8167-future-authority-bindings-v1.json', 'sha256': '4358fcdf0f4bb36341f0dc17ea76a904a485fd323fdfaabad2818b6bf674cf54'}]
failure=R/f'drain8167-builder-failure-{args.version}.json'
def run():
    assert not failure.exists(), 'Use a new version; preserve prior failure'
    for e in IMMUTABLE_REFS:
        p=Path(e['path']);assert p.is_relative_to(R) and not p.is_relative_to(W) and sha(p)==e['sha256'],str(p)
    d=json.loads((R/'drain8167-author-prepared-v1.json').read_text())
    frozen=json.loads((R/'drain8167-prepared-v1-source-freeze.json').read_text())['files'];assert len(frozen)==68
    original=json.loads((R/'drain8167-original-review.json').read_text())
    confirmation=Path(args.confirmation)
    assert confirmation.is_relative_to(R) and not confirmation.is_relative_to(W) and not confirmation.is_symlink()
    assert re.fullmatch('[0-9a-f]{64}',args.confirmation_sha256) and sha(confirmation)==args.confirmation_sha256
    confirmation_data=json.loads(confirmation.read_text())
    assert confirmation_data.get('reviewer_session')=='/root/review_8167'
    assert 'b1249f0427dc7e1a8523775fd6341a2a7bbb7b007b373f19af7296d63b8aa597' in json.dumps(confirmation_data), 'Report does not bind frozen prepared-v1'
    assert str(confirmation_data.get('verdict','')).startswith('PASS'), 'Clean affected-source confirmation required'
    assert not confirmation_data.get('findings'), 'Unresolved findings require new preparation, never edit frozen-v1'

    plans=json.loads((R/'drain8167-author-input-resource-plan-v1.json').read_text())
    authorities=json.loads((R/'drain8167-future-authority-bindings-v1.json').read_text())
    owner=json.loads((R/'review-meta-slot.json').read_text());assert owner['owner']=='PR8167-author' and Path(owner['path']).resolve()==W.resolve()
    assert git('rev-parse','HEAD')==args.expected_base==git('rev-parse','origin/main')
    assert not git('diff','--name-only','HEAD') and not git('diff','--cached','--name-only')
    assert set(git('ls-files','--others','--exclude-standard').splitlines())=={e['path'] for e in frozen}
    assert not git('ls-files','--others','--ignored','--exclude-standard')
    for e in frozen:
        p=W/e['path'];q=Path(e['immutable_copy'])
        assert p.is_file() and not p.is_symlink() and q.is_file() and not q.is_symlink()
        assert sha(p)==sha(q)==e['sha256'] and oct(p.stat().st_mode&0o777)==oct(q.stat().st_mode&0o777)==e['mode']
    for e in authorities:assert sha(W/e['path'])==e['sha256'], 'Authority changed; original reviewer confirmation required: '+e['path']
    outputs={k:R/f'drain8167-author-{k}-{args.version}.json' for k in ['unit-draft','source-handoff','cache-api']}
    assert all(not p.exists() for p in outputs.values())
    archive=Path(d['archive_manifest']['path']).parent
    assert sha(W/d['archive_manifest']['path'])==d['archive_manifest']['sha256']
    manifest=json.loads((W/d['archive_manifest']['path']).read_text())
    orig={e['path']:e for e in original['original_dispositions']}
    mapped={e['original_path']:e for e in json.loads((R/'drain8167-author-full-mapping-v1.json').read_text())}
    assert len(orig)==len(manifest['entries'])==len(mapped)==116
    assert set(orig)==set(mapped)=={e['original_path'] for e in manifest['entries']}
    disps=[]
    for e in manifest['entries']:
        o=orig[e['original_path']];assert e['original_mode']==o['mode'] and e['git_blob']==o['blob'] and e['raw_sha256']==o['sha256']
        stored=(archive/e['stored_path']).as_posix();assert sha(W/stored)==e['stored_sha256']
        payload=(W/stored).read_bytes();raw=gzip.decompress(payload) if e['encoding']=='gzip' else payload
        assert hashlib.sha256(raw).hexdigest()==e['raw_sha256']
        assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==e['git_blob']
        row=mapped[e['original_path']];canonical=row['final_path'];target=canonical or stored
        if canonical:assert sha(W/canonical)==row['final_sha256']
        disps.append(dict(original_path=e['original_path'],original_mode=e['original_mode'],original_blob=e['git_blob'],original_sha256=e['raw_sha256'],final_path=target,final_sha256=sha(W/target),recovery=manifest['revision']+':'+e['original_path']+'; exact stored payload '+stored,recovery_encoding=e['encoding'],disposition=row['disposition'],canonical_path=canonical))
    sys.path[:0]=[str(W/'scripts'),str(W/'docs/audit/scripts')]
    import runner_cache as c,audit_packet_script_deps as a,build_citation_graph as g
    # Metadata tools only; scientific modules are never imported or executed.
    registry=['scripts/audit_packet_script_deps.py','docs/audit/scripts/build_citation_graph.py']
    registry_before={p:sha(W/p) for p in registry}
    notes=[];allcites=set();allparents=set();runtime=set();apis=[]
    paths=[e['path'] for e in d['notes']];runnerpaths=[e['path'] for e in d['runners']]
    for i,note in enumerate(paths):
        body=(W/note).read_text();cid=g.claim_id_from_path(W/note);primary=g.extract_runner(body,note)
        assert primary==re.search(r'^runner: (.+)$',body,re.M)[1] and primary in runnerpaths
        hp=list(g.helper_runner_paths_for_claim(cid,primary));packet=list(a.helper_runner_paths_for_claim(cid,Path(primary).stem))
        assert hp==packet==[] and not a.transitive_helpers(Path(primary).stem) and not g.resolve_helper_runner_paths(primary), 'Discovery changed; preserve failure, no map mutation'
        deps=[];declared=json.loads(re.search(r'^upstream_dependencies: (.+)$',body,re.M)[1]);assert declared==[Path(x).stem.lower() for x in deps]
        cites=sorted(x.relative_to(W).as_posix() for x in g.extract_citations(body,W/note));assert set(deps)<=set(cites)
        assert cites==['docs/work_history/repo/review_feedback/pr8167-evidence/README.md']
        allcites.update(cites);allparents.update(deps)
        notes.append(dict(path=note,claim_id=cid,declared_claim_id=re.search(r'^claim_id: (.+)$',body,re.M)[1],claim_type='bounded_theorem',primary_runner=primary,helpers=[],citations=cites,repository_dependencies=deps,dependency_rationale='Complete self-contained positive proof for the supplied rotor/source/state. No external current-main science parent or unlanded PR8165/8166 theorem is imported. Historical recovery is context only.'))
    assert len({n['primary_runner'] for n in notes})==2
    for row in plans:
        p=row['runner'];tree=ast.parse((W/p).read_text());compile(tree,p,'exec')
        declarations={n.targets[0].id:n.value for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name)}
        ins=[x['path'] for x in row['ordered_inputs']]
        assert ast.literal_eval(declarations['AUDIT_INPUT_PATHS'])==list(c.declared_input_paths(W/p))==ins
        assert c.declared_timeout_for(W/p)==120 and ast.literal_eval(declarations['AUDIT_MEMORY_MB'])==768
        assert ast.literal_eval(declarations['EXPECTED_INPUT_SHA256'])=={x:sha(W/x) for x in ins}=={x['path']:x['sha256'] for x in row['ordered_inputs']}
        assert sha(W/p)==row['source_sha256'];runtime.update(ins+[p])
        apis.append(dict(runner=p,timeout=120,declared_inputs=ins,runtime_closure=bind(ins+[p]),declared_input_fingerprint=c.declared_input_fingerprint(W/p),packet_transitive_helpers=[],source_reads='Own source SHA and ordered literal proof inputs; calculations use original internal fixtures and external numpy/scipy/mpmath libraries. No local scientific modules.'))
    # All source, archive, input, authority, owner, base and metadata guards precede staging.
    assert git('rev-parse','HEAD')==args.expected_base==git('rev-parse','origin/main')
    assert not git('diff','--name-only','HEAD') and not git('diff','--cached','--name-only')
    for e in frozen:assert sha(W/e['path'])==e['sha256']
    subprocess.run(['git','-C',str(W),'add','--',*[e['path'] for e in frozen]],check=True)
    subprocess.run(['git','-C',str(W),'diff','--cached','--check'],check=True)
    staged=git('diff','--cached','--name-only').splitlines();assert set(staged)=={e['path'] for e in frozen}
    assert not git('diff','--name-only') and registry_before=={p:sha(W/p) for p in registry}
    stagedtree=git('write-tree');outputs['cache-api'].write_text(json.dumps(apis,indent=2)+'\n')
    claims=d['claim_dispositions']
    assert len(claims)==5 and claims[-1]['disposition'].startswith('Deferred')
    refs=IMMUTABLE_REFS+[ref(confirmation),ref(outputs['cache-api'])]
    handoff=dict(status='AUTHOR HANDOFF ONLY; CURRENT-BASE COLD AND FINAL EVIDENCE CONFIRMATION PENDING',author='/root/resume_8078_method',base=args.expected_base,tree=stagedtree,original_dispositions=disps,claim_dispositions=claims,mathematical_closure='Two full self-contained positive arguments: exact compact-cover/source identities, and compact sine MGF/static exact-curl conditional Gaussian proof. Sparse-law construction and universal negative implication deferred in exact historical recovery. No false sibling theorem dependency. Framework authorities are context only.',runtime_scope='Two unique programs, no helper/sibling invocation; own source and own-note reads distinguished from mathematical closure. Sparse-law runner remains historical only.',registry_changes=[],registry_unchanged=registry_before,references=refs)
    outputs['source-handoff'].write_text(json.dumps(handoff,indent=2)+'\n')
    skill='docs/ai_methodology/skills/review-loop'
    context=allcites|set(paths)|{d['archive_manifest']['path'],skill+'/SKILL.md',skill+'/PREFLIGHT.md',skill+'/scripts/review_receipt.py',skill+'/scripts/review_workspace.py'}|{str(p.relative_to(W)) for p in (W/skill/'references').glob('*.md')}|{e['path'] for e in authorities}
    tooling=['docs/audit/scripts/build_citation_graph.py','docs/audit/scripts/static_pipeline_checkpoint.py','scripts/runner_cache.py','scripts/audit_packet_script_deps.py','docs/audit/scripts/ledger_io.py','docs/audit/data/axiom_premise_nodes.json','docs/audit/data/doc_authority_registry.json']
    history=[e['path'] for e in frozen if e['path'].startswith(archive.as_posix()+'/') and e['path'].endswith('.md')]
    record=dict(schema_version=2,unit_id='PR8167',constituents=[dict(id='PR8167',head=original['head'],delta_base=original['merge_base'],dispositions=dict(ref(outputs['source-handoff']),json_pointer='/original_dispositions'))],source=dict(base=args.expected_base,commit=args.expected_base,tree=stagedtree,paths=bind(staged),deleted_paths=[]),inputs=dict(runtime=bind(runtime),helpers=[],parents=bind(allparents),context=bind(context),tooling=bind(tooling)),reviewer=dict(session='/root/review_8167; current-base cold and final evidence confirmation pending',report=ref(R/'drain8167-original-review.json'),references=refs+[ref(outputs['source-handoff'])]),notes=notes,supporting_proofs=[],non_science_notes=[dict(path=p,rationale='Exact historical proof or review record. Two current positive arguments are complete in canonical claims. The entire sparse construction and its negative implication are deferred scientific recovery, not a live claim, not discarded, and not mathematically refuted; preserve original branch.',review_reference=ref(confirmation)) for p in history])
    outputs['unit-draft'].write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(ref(outputs['unit-draft'])));print(stagedtree)
try:run()
except BaseException as exc:
    if not failure.exists():failure.write_text(json.dumps(dict(status='FAILED; preserve source/index state for diagnosis',error=repr(exc),traceback=traceback.format_exc()),indent=2)+'\n')
    raise
