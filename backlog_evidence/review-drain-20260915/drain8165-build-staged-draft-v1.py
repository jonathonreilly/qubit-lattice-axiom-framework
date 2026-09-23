"""Future root-dispatched PR8165 staging/schema2 builder. NOT executed during preparation.
No science, gates, registry mutations, commits or pushes. All guards precede staging.
"""
from pathlib import Path
import argparse,ast,gzip,hashlib,json,re,subprocess,sys,traceback
sys.dont_write_bytecode=True
assert __debug__, 'Do not optimize away guards'
R=Path('/private/tmp/review-drain-20260915');W=R/'author-draft-slot'
ap=argparse.ArgumentParser();ap.add_argument('--expected-base',required=True);ap.add_argument('--stage-authorized',action='store_true',required=True);ap.add_argument('--version',required=True);args=ap.parse_args()
assert args.stage_authorized and re.fullmatch('[0-9a-f]{40}',args.expected_base) and re.fullmatch('v[1-9][0-9]*',args.version)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ref=lambda p:dict(path=str(p),sha256=sha(p))
bind=lambda ps:[dict(path=p,sha256=sha(W/p)) for p in sorted(set(ps))]
git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
IMMUTABLE_REFS = [{'path': '/private/tmp/review-drain-20260915/drain8165-original-review.json', 'sha256': '686b5b035052e7d793a126d7d7b24626dd07c98c03d6613efb87d0c20806ba0d'}, {'path': '/private/tmp/review-drain-20260915/drain8165-original-review.md', 'sha256': 'a449dd5809555fb38ae20a0e9a42c6c6a01a83ed4150c90321f9a26179e0f197'}, {'path': '/private/tmp/review-drain-20260915/drain8165-early-affected-review-v1.json', 'sha256': 'b668974f0c980b4c839d390236e0635d021bceb81a64ba2fb719a711b84aa2b6'}, {'path': '/private/tmp/review-drain-20260915/drain8165-early-affected-review-v1.md', 'sha256': 'e31d9c03234f91f9c08ba34c95cf62f51a429c6e4abc6d82454baf5feee2840b'}, {'path': '/private/tmp/review-drain-20260915/drain8165-author-prepared-v1.json', 'sha256': '61656f86004b0288198f6f754177ad24437c76ccffece2c0dac3e8dcb770e698'}, {'path': '/private/tmp/review-drain-20260915/drain8165-prepared-v1-source-freeze.json', 'sha256': '5fce38e2aa062930ba5828249477f339e35fca91f10eb190ec1971d845916149'}, {'path': '/private/tmp/review-drain-20260915/drain8165-author-preservation-v1.json', 'sha256': 'f607873a8463e9d39f6dad622fb559d6d976e74e955e42d56d99619c4ced613e'}, {'path': '/private/tmp/review-drain-20260915/drain8165-author-full-mapping-v1.json', 'sha256': 'e43c6b46a5bb52a77ec07b1e4f7c74ed27b14a6a4f7078b1b3a54bd68fc75b7d'}, {'path': '/private/tmp/review-drain-20260915/drain8165-author-input-resource-plan-v1.json', 'sha256': 'c75830ab22229060e80ab3963926efc20f6b9ec71f2d22da2fd968994f7a82b8'}, {'path': '/private/tmp/review-drain-20260915/drain8165-author-correction-v1.diff', 'sha256': '29c19187dcf40cdb74063d38640d56ec4f0ad7f2b2649d06c85085f080adbfd0'}, {'path': '/private/tmp/review-drain-20260915/drain8165-author-metadata-verification-v1.json', 'sha256': '6c2846bdd183dbf05191065cb733a60bd6f641281742429b32278981dd1ee03d'}, {'path': '/private/tmp/review-drain-20260915/drain8165-future-builder-api-check-v1.json', 'sha256': 'a8907242d2064b5bc9ccd931dd97c76571828e2029de16c18c93e76a203ed3ac'}, {'path': '/private/tmp/review-drain-20260915/drain8165-fetch.json', 'sha256': 'c3ce125ca7d4bd47aab3246434263927fe3cf487c92538b2ed72e241ec5b8857'}, {'path': '/private/tmp/review-drain-20260915/drain8165-original-inventory.json', 'sha256': 'c39d733f74b13797ab61c67dfc94f3064f58fd6dca8919cb1be1b4276283e628'}, {'path': '/private/tmp/review-drain-20260915/drain8165-original-delta.patch', 'sha256': '4e270dcd572e9caf32b5fa9be142a35b7b5f1bba98e8fb63f5e7f29a12b17362'}, {'path': '/private/tmp/review-drain-20260915/drain8165-provenance-checks.json', 'sha256': 'c1a8fb330cb1c437e5f44149ffae71749925c1c36551f73dc5f19aa7849d70ae'}, {'path': '/private/tmp/review-drain-20260915/check8165/independent_controls.py', 'sha256': 'f8d56cb5f5c2ee2860508d27c36be1ba4ad3be40d6964f1b877189c60bcb5714'}, {'path': '/private/tmp/review-drain-20260915/check8165/independent_controls.json', 'sha256': '47c4e01c2f6967cdf642d5941d0835ba7fe7a06f9385a6b4508e607b202a0792'}, {'path': '/private/tmp/review-drain-20260915/check8165/independent_controls_attempt1.py', 'sha256': 'd0f5ed5af1fd762fc63f3ca917d8c92facfacd4fedc8a91248c5afae8fc99fcb'}, {'path': '/private/tmp/review-drain-20260915/check8165/independent_controls_attempt1.json', 'sha256': '77129a03eb0814b23e736ddbb1b8e2c219f00ed261bc7cc111585bbfffc69f13'}, {'path': '/private/tmp/review-drain-20260915/check8165/final-github.json', 'sha256': 'a0057893ee9dbee82a4cba2463caa145d071a6f54d9bec29b0378f975e953939'}, {'path': '/private/tmp/review-drain-20260915/drain8165-future-authority-bindings-v1.json', 'sha256': '4358fcdf0f4bb36341f0dc17ea76a904a485fd323fdfaabad2818b6bf674cf54'}, {'path': '/private/tmp/review-drain-20260915/drain8165-capture-plan-v1.json', 'sha256': '72c562ec6ce768dab8c86385fe87345aeebada911e2cbc1836e40946f0e73a76'}]
failure=R/f'drain8165-builder-failure-{args.version}.json'
def run():
    assert not failure.exists(), 'Use a new version; preserve prior failure'
    for e in IMMUTABLE_REFS:
        p=Path(e['path']);assert p.is_relative_to(R) and not p.is_relative_to(W) and sha(p)==e['sha256'],str(p)
    d=json.loads((R/'drain8165-author-prepared-v1.json').read_text())
    frozen=json.loads((R/'drain8165-prepared-v1-source-freeze.json').read_text())['files'];assert len(frozen)==74
    original=json.loads((R/'drain8165-original-review.json').read_text())
    confirmation=R/'drain8165-early-affected-review-v1.json'
    plans=json.loads((R/'drain8165-author-input-resource-plan-v1.json').read_text())
    authorities=json.loads((R/'drain8165-future-authority-bindings-v1.json').read_text())
    owner=json.loads((R/'author-draft-slot.json').read_text());assert owner['owner']=='PR8165-author' and Path(owner['path']).resolve()==W.resolve()
    assert git('rev-parse','HEAD')==args.expected_base==git('rev-parse','origin/main')
    assert not git('diff','--name-only','HEAD') and not git('diff','--cached','--name-only')
    assert set(git('ls-files','--others','--exclude-standard').splitlines())=={e['path'] for e in frozen}
    assert not git('ls-files','--others','--ignored','--exclude-standard')
    for e in frozen:
        p=W/e['path'];q=Path(e['immutable_copy'])
        assert p.is_file() and not p.is_symlink() and q.is_file() and not q.is_symlink()
        assert sha(p)==sha(q)==e['sha256'] and oct(p.stat().st_mode&0o777)==oct(q.stat().st_mode&0o777)==e['mode']
    for e in authorities:assert sha(W/e['path'])==e['sha256'], 'Authority changed; original reviewer confirmation required: '+e['path']
    outputs={k:R/f'drain8165-author-{k}-{args.version}.json' for k in ['unit-draft','source-handoff','cache-api']}
    assert all(not p.exists() for p in outputs.values())
    archive=Path(d['archive_manifest']['path']).parent
    assert sha(W/d['archive_manifest']['path'])==d['archive_manifest']['sha256']
    manifest=json.loads((W/d['archive_manifest']['path']).read_text())
    orig={e['path']:e for e in original['original_inventory']}
    mapped={e['original_path']:e for e in json.loads((R/'drain8165-author-full-mapping-v1.json').read_text())}
    assert len(orig)==len(manifest['entries'])==len(mapped)==88
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
        deps=paths[:i];declared=json.loads(re.search(r'^upstream_dependencies: (.+)$',body,re.M)[1]);assert declared==[Path(x).stem.lower() for x in deps]
        cites=sorted(x.relative_to(W).as_posix() for x in g.extract_citations(body,W/note));assert set(deps)<=set(cites)
        assert {p for p in cites if p.startswith('docs/COMPACT_ROTOR_')}==set(deps)
        allcites.update(cites);allparents.update(deps)
        notes.append(dict(path=note,claim_id=cid,declared_claim_id=re.search(r'^claim_id: (.+)$',body,re.M)[1],claim_type='bounded_theorem',primary_runner=primary,helpers=[],citations=cites,repository_dependencies=deps,dependency_rationale='Self-contained supplied compact rotor model and complete sampled-event proof; no current-main scientific parent.' if i==0 else 'Complete linked in-unit mathematical parents, including full compact path specification for the coarse-current result. PR8164 is context only, not a dependency.'))
    assert len({n['primary_runner'] for n in notes})==3
    for row in plans:
        p=row['runner'];tree=ast.parse((W/p).read_text());compile(tree,p,'exec')
        declarations={n.targets[0].id:n.value for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name)}
        ins=[x['path'] for x in row['ordered_inputs']]
        assert ast.literal_eval(declarations['AUDIT_INPUT_PATHS'])==list(c.declared_input_paths(W/p))==ins
        assert c.declared_timeout_for(W/p)==120 and ast.literal_eval(declarations['AUDIT_MEMORY_MB'])==512
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
    claims=[dict(note=paths[i],disposition=text) for i,text in enumerate(original['claims_and_boundaries'])]
    claims.extend([dict(history='All 88 distinct originals',disposition='All four complete proofs, three calculations, eleven mutation histories, failed Fourier32/48 attempt, diagnostic and prior sources recovered exactly. No unique proved science omitted or historical output restamped.'),dict(negative_certification='Deferred formal N1 negative packet',disposition='Fewer than five qualifying refuted routes; no packet PASS. Positive conditional results and exact finite countercontrols remain intact; no fabricated route coverage.'),dict(open_extensions=['native Hamiltonian selection','photon/source response','unique vacuum','microscopic T->0 currents','global harmonic sectors','physical electric reconstruction'],disposition='Open extensions, not impossibility theorems.')])
    refs=IMMUTABLE_REFS+[ref(outputs['cache-api'])]
    handoff=dict(status='AUTHOR HANDOFF ONLY; CURRENT-BASE COLD AND FINAL EVIDENCE CONFIRMATION PENDING',author='/root/resume_8078_method',base=args.expected_base,tree=stagedtree,original_dispositions=disps,claim_dispositions=claims,mathematical_closure='Four complete in-unit claims, acyclic sampled -> excursion -> path law -> coarse currents. No external current-main science parent. Framework authorities are context only; supplied model not inferred from them.',runtime_scope='Three unique programs, one shared primary; own source and literal proof input reads distinguished from mathematical dependency edges.',registry_changes=[],registry_unchanged=registry_before,references=refs)
    outputs['source-handoff'].write_text(json.dumps(handoff,indent=2)+'\n')
    skill='docs/ai_methodology/skills/review-loop'
    context=allcites|set(paths)|{d['archive_manifest']['path'],skill+'/SKILL.md',skill+'/PREFLIGHT.md',skill+'/scripts/review_receipt.py',skill+'/scripts/review_workspace.py'}|{str(p.relative_to(W)) for p in (W/skill/'references').glob('*.md')}|{e['path'] for e in authorities}
    tooling=['docs/audit/scripts/build_citation_graph.py','docs/audit/scripts/static_pipeline_checkpoint.py','scripts/runner_cache.py','scripts/audit_packet_script_deps.py','docs/audit/scripts/ledger_io.py','docs/audit/data/axiom_premise_nodes.json','docs/audit/data/doc_authority_registry.json']
    history=[e['path'] for e in frozen if e['path'].startswith(archive.as_posix()+'/') and e['path'].endswith('.md')]
    record=dict(schema_version=2,unit_id='PR8165',constituents=[dict(id='PR8165',head=original['head'],delta_base=original['merge_base'],dispositions=dict(ref(outputs['source-handoff']),json_pointer='/original_dispositions'))],source=dict(base=args.expected_base,commit=args.expected_base,tree=stagedtree,paths=bind(staged),deleted_paths=[]),inputs=dict(runtime=bind(runtime),helpers=[],parents=bind(allparents),context=bind(context),tooling=bind(tooling)),reviewer=dict(session='/root/review_8165; current-base cold and final evidence confirmation pending',report=ref(R/'drain8165-original-review.json'),references=refs+[ref(outputs['source-handoff'])]),notes=notes,supporting_proofs=[],non_science_notes=[dict(path=p,rationale='Exact historical original/provisional proof, scope or review record. All current scientific proof bodies are preserved completely in four canonical claims; no autonomous historical claim/status adopted.',review_reference=ref(confirmation)) for p in history])
    outputs['unit-draft'].write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(ref(outputs['unit-draft'])));print(stagedtree)
try:run()
except BaseException as exc:
    if not failure.exists():failure.write_text(json.dumps(dict(status='FAILED; preserve source/index state for diagnosis',error=repr(exc),traceback=traceback.format_exc()),indent=2)+'\n')
    raise
