"""Future root-dispatched PR8169 staging/schema2 builder. NOT executed during preparation.
No science, gates, registry mutations, commits or pushes. Requires separately supplied clean original-reviewer affected report pinned by SHA; corrections invalidate this builder. All guards precede staging.
"""
from pathlib import Path
import argparse,ast,gzip,hashlib,json,re,subprocess,sys,traceback
sys.dont_write_bytecode=True
assert __debug__, 'Do not optimize away guards'
R=Path('/private/tmp/review-drain-20260915');W=R/'author-draft-slot'
ap=argparse.ArgumentParser();ap.add_argument('--expected-base',required=True);ap.add_argument('--stage-authorized',action='store_true',required=True);ap.add_argument('--version',required=True);ap.add_argument('--confirmation',required=True);ap.add_argument('--confirmation-sha256',required=True);ap.add_argument('--archive-confirmation',required=True);ap.add_argument('--archive-confirmation-sha256',required=True);ap.add_argument('--archive-confirmation-assessment',required=True);args=ap.parse_args()
assert args.stage_authorized and re.fullmatch('[0-9a-f]{40}',args.expected_base) and re.fullmatch('v[1-9][0-9]*',args.version)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ref=lambda p:dict(path=str(p),sha256=sha(p))
bind=lambda ps:[dict(path=p,sha256=sha(W/p)) for p in sorted(set(ps))]
git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
IMMUTABLE_REFS = [{'path': '/private/tmp/review-drain-20260915/drain8169-review-original.json', 'sha256': '45ca03069aed000f9627c4471d080d288f8d0665261f19a3ad1914f31a98418d'}, {'path': '/private/tmp/review-drain-20260915/drain8169-review-original.md', 'sha256': 'ae16f7df7c32c5fc3588ebabfad8dd048b4c1bbc8778abab10853b3366267edc'}, {'path': '/private/tmp/review-drain-20260915/drain8169-author-prepared-v2.json', 'sha256': '0e4251711da8ce11cb206d93c1b351e97429d1506a4b226181b13b5b0dff240a'}, {'path': '/private/tmp/review-drain-20260915/drain8169-prepared-v2-source-freeze.json', 'sha256': 'aa2ad58e8fc3f117323540cfdde735fac8d4816c52ed08a055eefd2a8914a5b3'}, {'path': '/private/tmp/review-drain-20260915/drain8169-author-preservation-v1.json', 'sha256': '42996ac4c170102252547e5783135aa6db41b0b1f6d7d4624d9891a4271ee191'}, {'path': '/private/tmp/review-drain-20260915/drain8169-author-full-mapping-v2.json', 'sha256': 'd7fb9f7bcb3d203402d2f19496eb150eb852970e84ad081e138798d50f364070'}, {'path': '/private/tmp/review-drain-20260915/drain8169-author-input-resource-plan-v2.json', 'sha256': '76fcbffa8e65cb9e604c9ee3319a8638ea480aace054dac5f0b075b3f5882c09'}, {'path': '/private/tmp/review-drain-20260915/drain8169-author-correction-v2.diff', 'sha256': '7200e8515d27ca3283589975174bbf9db2951529901b90dd790889448bf306c5'}, {'path': '/private/tmp/review-drain-20260915/drain8169-author-v1-to-v2.diff', 'sha256': 'a14818ea18be1fecc25eba24c722519945e915e320a355a1487399294c43934a'}, {'path': '/private/tmp/review-drain-20260915/drain8169-author-discovery-v2.json', 'sha256': 'd030d5ddc46ee5178b95b4ce12aa9f2df4c0948e0af5da4f0eb29e60a62718f4'}, {'path': '/private/tmp/review-drain-20260915/drain8169-capture-plan-v2.json', 'sha256': '3d6b9eb2644e968f3d2c1b54d0b3388bf3e1cde9280d9577ceca79b21ab8fa2b'}, {'path': '/private/tmp/review-drain-20260915/drain8169-inventory.json', 'sha256': '31c7e291185b698123bb306f5d0f3f3b6e01bbc537e51b8e73d5e2a0f9e9906c'}, {'path': '/private/tmp/review-drain-20260915/drain8169-original.delta', 'sha256': '71ac9b6b22c2f1766f0635eeded2eb9becfd0d93d6fdfbb0ef9f245c699eba58'}, {'path': '/private/tmp/review-drain-20260915/drain8169-early-v2-review.json', 'sha256': '25687c1bc05b7cc03eca05d909184ad9d61f85403e1f841d42572049408cccb1'}, {'path': '/private/tmp/review-drain-20260915/drain8169-early-v2-review.md', 'sha256': 'db00e1cbcb2a0af6acabee45d5d4b78aca50bdf560b567d225248c0e1871dd99'}, {'path': '/private/tmp/review-drain-20260915/drain8169-future-authority-bindings-v1.json', 'sha256': 'b623d0475e8448e31677c1bb8c79760106f72d08b7dd4b8e48a4ee8c4d0151a5'}, {'path': '/private/tmp/review-drain-20260915/drain8169-mainadvance-record-context.md', 'sha256': '750bdd27065ef957228c7316996d6a9cfcb5af19a5407309e532e9c1edc6fce0'}, {'path': '/private/tmp/review-drain-20260915/drain8169-mainadvance-addendum.json', 'sha256': '53c25e71eb5ae0427073f3570710dc64c5596ce12dc45fafb25cdfd836f44224'}, {'path': '/private/tmp/review-drain-20260915/drain8169-mainadvance-addendum.md', 'sha256': '7a8e70967f024097cc1aa213d0b9662d4b5f4a9859e82eba89d7c8526f1389e2'}, {'path': '/private/tmp/review-drain-20260915/check8169.py', 'sha256': '32186a8f9f00d1b5d47b05f894037be3d5b526d2fda9788e68398ee630a97513'}, {'path': '/private/tmp/review-drain-20260915/check8169.json', 'sha256': 'c5a006776071d07c3b2db529a19309ec4420dfb09ebb67ecdb1d57275231a1c2'}, {'path': '/private/tmp/review-drain-20260915/drain8169-author-prepared-v3.json', 'sha256': 'a16a32d955f77fbb804143e2cd202f84314142710d8ea3a87fb42f19b951fa99'}, {'path': '/private/tmp/review-drain-20260915/drain8169-prepared-v3-source-freeze.json', 'sha256': '78507b371937b810a2b9c70cc59bb21782ad0797ba007855069abea7a054a8e6'}, {'path': '/private/tmp/review-drain-20260915/drain8169-author-full-mapping-v3.json', 'sha256': '886ee0e6b0618bd16856d74b2f4fd568a726caa782ac85a1f61078e376177fb6'}, {'path': '/private/tmp/review-drain-20260915/drain8169-author-v2-to-v3.diff', 'sha256': '51129f548c126008ac5bf0be2cbddc20e29e8910b476abc5e1fb211e95d3635f'}, {'path': '/private/tmp/review-drain-20260915/drain8169-archive-preservation-v3.json', 'sha256': '881458af8bc1d29fdc1e1cbc611e71d6c282939bc9824a057d2340a6896f162c'}, {'path': '/private/tmp/review-drain-20260915/drain8169-builder-failure-v1.json', 'sha256': '752e9899ccb23f86882271f1855b5a60bc8e2f7902cad437c9d8b872e8b6343e'}, {'path': '/private/tmp/review-drain-20260915/drain8169-build-staged-draft-v2.py', 'sha256': 'fea6555363013d31dde34a6cd877d83494f8e48b9dc4785d6a5fc26895ddf912'}, {'path': '/private/tmp/review-drain-20260915/drain8169-capture-plan-v3.json', 'sha256': '906c3cb71f71630a148899116ed6cfe00d92ce1506270f9c3eb30670d20b2458'}]
failure=R/f'drain8169-builder-failure-{args.version}.json'
def run():
    assert not failure.exists(), 'Use a new version; preserve prior failure'
    for e in IMMUTABLE_REFS:
        p=Path(e['path']);assert p.is_relative_to(R) and not p.is_relative_to(W) and sha(p)==e['sha256'],str(p)
    d=json.loads((R/'drain8169-author-prepared-v3.json').read_text())
    frozen=json.loads((R/'drain8169-prepared-v3-source-freeze.json').read_text())['files'];assert len(frozen)==13
    original=json.loads((R/'drain8169-review-original.json').read_text())
    confirmation=Path(args.confirmation)
    assert confirmation.is_relative_to(R) and not confirmation.is_relative_to(W) and not confirmation.is_symlink()
    assert re.fullmatch('[0-9a-f]{64}',args.confirmation_sha256) and sha(confirmation)==args.confirmation_sha256
    confirmation_data=json.loads(confirmation.read_text())
    assert confirmation_data.get('reviewer_session')=='/root/review_8169'
    assert sha(confirmation)=='25687c1bc05b7cc03eca05d909184ad9d61f85403e1f841d42572049408cccb1'
    assert confirmation_data.get('source_assessment')=='F1-F5 mathematically corrected on frozen prepared-v2; no new material mathematical finding'
    assert confirmation_data['anchors']['drain8169-author-prepared-v2.json']=='0e4251711da8ce11cb206d93c1b351e97429d1506a4b226181b13b5b0dff240a'

    archive_confirmation=Path(args.archive_confirmation)
    assert archive_confirmation.is_relative_to(R) and not archive_confirmation.is_relative_to(W) and not archive_confirmation.is_symlink()
    assert re.fullmatch('[0-9a-f]{64}',args.archive_confirmation_sha256) and sha(archive_confirmation)==args.archive_confirmation_sha256
    archive_review=json.loads(archive_confirmation.read_text())
    assert archive_review.get('reviewer_session')=='/root/review_8169'
    assert args.archive_confirmation_assessment and args.archive_confirmation_assessment in json.dumps(archive_review)
    assert 'a16a32d955f77fbb804143e2cd202f84314142710d8ea3a87fb42f19b951fa99' in json.dumps(archive_review), 'Archive confirmation does not bind prepared-v3'
    # Root supplies the exact independently clear assessment from the actual report; never invent reviewer fields or outcomes.
    plans=json.loads((R/'drain8169-author-input-resource-plan-v2.json').read_text())
    authorities=json.loads((R/'drain8169-future-authority-bindings-v1.json').read_text())
    owner=json.loads((R/'author-draft-slot.json').read_text());assert owner['owner']=='PR8169-author' and Path(owner['path']).resolve()==W.resolve()
    assert git('rev-parse','HEAD')==args.expected_base==git('rev-parse','origin/main')
    assert not git('diff','--name-only','HEAD') and not git('diff','--cached','--name-only')
    assert set(git('ls-files','--others','--exclude-standard').splitlines())=={e['path'] for e in frozen}
    assert not git('ls-files','--others','--ignored','--exclude-standard')
    for e in frozen:
        p=W/e['path'];q=Path(e['immutable_copy'])
        assert p.is_file() and not p.is_symlink() and q.is_file() and not q.is_symlink()
        assert sha(p)==sha(q)==e['sha256'] and oct(p.stat().st_mode&0o777)==oct(q.stat().st_mode&0o777)==e['mode']
    for e in authorities:assert sha(W/e['path'])==e['sha256'], 'Authority changed; original reviewer confirmation required: '+e['path']
    outputs={k:R/f'drain8169-author-{k}-{args.version}.json' for k in ['unit-draft','source-handoff','cache-api']}
    assert all(not p.exists() for p in outputs.values())
    archive=Path(d['archive_manifest']['path']).parent
    assert sha(W/d['archive_manifest']['path'])==d['archive_manifest']['sha256']
    manifest=json.loads((W/d['archive_manifest']['path']).read_text())
    inventory=json.loads((R/'drain8169-inventory.json').read_text())
    orig={e['path']:dict(mode=e['head'].split()[0],blob=e['head'].split()[2],sha256=e['head_sha256']) for e in inventory['files']}
    mapped={e['original_path']:e for e in json.loads((R/'drain8169-author-full-mapping-v3.json').read_text())}
    assert len(orig)==len(manifest['entries'])==len(mapped)==8
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
        deps=[x['path'] for x in plans['ordered_inputs'][1:]]
        declared=re.search(r'^upstream_dependencies: (.+)$',body,re.M)[1]
        assert declared=='[minimal_axioms, possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14]'
        cites=sorted(x.relative_to(W).as_posix() for x in g.extract_citations(body,W/note))
        assert cites==sorted(deps+['docs/work_history/repo/review_feedback/pr8169-evidence/README.md'])
        allcites.update(cites);allparents.update(deps)
        notes.append(dict(path=note,claim_id=cid,declared_claim_id=re.search(r'^claim_id: (.+)$',body,re.M)[1],claim_type='bounded_theorem',primary_runner=primary,helpers=[],citations=cites,repository_dependencies=deps,dependency_rationale='Current minimal axioms and covariance parent supply definitions and independent cubic/internal action. Complete corrected positive identities are in the canonical note. Valid conditional endpoint separation is deferred recovery, not a live premise; supplied-record common-kernel note is context only.'))
    assert len({n['primary_runner'] for n in notes})==1
    for row in [plans]:
        p=row['runner']['path'];tree=ast.parse((W/p).read_text());compile(tree,p,'exec')
        declarations={n.targets[0].id:n.value for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name)}
        ins=[x['path'] for x in row['ordered_inputs']]
        assert ast.literal_eval(declarations['AUDIT_INPUT_PATHS'])==list(c.declared_input_paths(W/p))==ins
        assert c.declared_timeout_for(W/p)==120 and ast.literal_eval(declarations['AUDIT_MEMORY_MB'])==256
        assert ast.literal_eval(declarations['EXPECTED_INPUT_SHA256'])=={x:sha(W/x) for x in ins}=={x['path']:x['sha256'] for x in row['ordered_inputs']}
        assert sha(W/p)==row['runner']['sha256'];runtime.update(ins+[p])
        apis.append(dict(runner=p,timeout=120,declared_inputs=ins,runtime_closure=bind(ins+[p]),declared_input_fingerprint=c.declared_input_fingerprint(W/p),packet_transitive_helpers=[],source_reads='Own source SHA and ordered literal proof inputs; calculations use original internal fixtures and standard-library Fraction and itertools. No local scientific modules.'))
    # All source, archive, input, authority, owner, base and metadata guards precede staging.
    assert git('rev-parse','HEAD')==args.expected_base==git('rev-parse','origin/main')
    assert not git('diff','--name-only','HEAD') and not git('diff','--cached','--name-only')
    for e in frozen:assert sha(W/e['path'])==e['sha256']
    subprocess.run(['git','-C',str(W),'add','--',*[e['path'] for e in frozen]],check=True)
    subprocess.run(['git','-C',str(W),'diff','--cached','--check'],check=True)
    staged=git('diff','--cached','--name-only').splitlines();assert set(staged)=={e['path'] for e in frozen}
    assert not git('diff','--name-only') and registry_before=={p:sha(W/p) for p in registry}
    stagedtree=git('write-tree');outputs['cache-api'].write_text(json.dumps(apis,indent=2)+'\n')
    claims=[{'claim': 'F1', 'disposition': 'Corrected live unordered exchange-symmetric classification requires independent cubic slot exchange, not SO3 alone; adjacent/opposite strata independent.'}, {'claim': 'F2', 'disposition': 'Corrected live support is subset of allowed menu, including singleton one-neighbor and two-atom boundary.'}, {'claim': 'F3', 'disposition': 'Corrected live lambda(t) bound and Gibbs formulas; constant lambda only subfamily.'}, {'claim': 'F4', 'disposition': 'Valid corrected conditional endpoint event proof deferred readably; chain probability zero versus independent-Haar ends-first one. Formal negative certification and live promotion pending complete packet, not false mathematics. Original support-count proof superseded.'}, {'claim': 'F5', 'disposition': 'Live raw sum two and normalized overlap identity; normalized law depends on second record and lacks exchange symmetry. No blanket variation violation.'}, {'claim': 'F6', 'disposition': 'Four historical routes retained with actual outcomes, unsupported Independent withdrawn, no fabricated fifth route or negative PASS.'}, {'claim': 'F7', 'disposition': 'Native input pins and truthful finite/N5 reporting; primary and decisive mutations pending.'}]
    refs=IMMUTABLE_REFS+[ref(archive_confirmation),ref(confirmation),ref(outputs['cache-api'])]
    handoff=dict(status='AUTHOR HANDOFF ONLY; CURRENT-BASE COLD AND FINAL EVIDENCE CONFIRMATION PENDING',author='/root/resume_8078_method',base=args.expected_base,tree=stagedtree,original_dispositions=disps,claim_dispositions=claims,mathematical_closure='Two explicit current-main parents bind minimal definitions and independent cubic/internal symmetry. Canonical proof supplies conditional unordered menu classification, lambda(t) domain, Gibbs and overlap identities. Endpoint theorem remains valid deferred science, with complete corrected proof and all eight originals recoverable; no active negative premise.',runtime_scope='One standard-library program; source plus three literal input reads; no helpers. Finite endpoint analogues do not replace analytic deferred Haar proof. Required final mutation evidence is pending.',registry_changes=[],registry_unchanged=registry_before,references=refs)
    outputs['source-handoff'].write_text(json.dumps(handoff,indent=2)+'\n')
    skill='docs/ai_methodology/skills/review-loop'
    context=allcites|set(paths)|{d['deferred_corrected_proof']['path'],d['archive_manifest']['path'],skill+'/SKILL.md',skill+'/PREFLIGHT.md',skill+'/scripts/review_receipt.py',skill+'/scripts/review_workspace.py'}|{str(p.relative_to(W)) for p in (W/skill/'references').glob('*.md')}|{e['path'] for e in authorities}
    tooling=['docs/audit/scripts/build_citation_graph.py','docs/audit/scripts/static_pipeline_checkpoint.py','scripts/runner_cache.py','scripts/audit_packet_script_deps.py','docs/audit/scripts/ledger_io.py','docs/audit/data/axiom_premise_nodes.json','docs/audit/data/doc_authority_registry.json']
    history=[e['path'] for e in frozen if e['path'].startswith(archive.as_posix()+'/') and e['path'].endswith('.md')]
    record=dict(schema_version=2,unit_id='PR8169',constituents=[dict(id='PR8169',head=d['original_head'],delta_base=d['original_merge_base'],dispositions=dict(ref(outputs['source-handoff']),json_pointer='/original_dispositions'))],source=dict(base=args.expected_base,commit=args.expected_base,tree=stagedtree,paths=bind(staged),deleted_paths=[]),inputs=dict(runtime=bind(runtime),helpers=[],parents=bind(allparents),context=bind(context),tooling=bind(tooling)),reviewer=dict(session='/root/review_8169; current-base cold and final evidence confirmation pending',report=ref(R/'drain8169-review-original.json'),references=refs+[ref(outputs['source-handoff'])]),notes=notes,supporting_proofs=[],non_science_notes=[dict(path=p,rationale='Historical source/review recovery or corrected deferred scientific endpoint proof. This classification excludes it from active claim authority, not from science: the conditional endpoint proof is valid, with formal negative certification/promotion deferred. All eight originals and stronger superseded claims remain recoverable; preserve branch and four actual route outcomes.',review_reference=ref(confirmation)) for p in history])
    outputs['unit-draft'].write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(ref(outputs['unit-draft'])));print(stagedtree)
try:run()
except BaseException as exc:
    if not failure.exists():failure.write_text(json.dumps(dict(status='FAILED; preserve source/index state for diagnosis',error=repr(exc),traceback=traceback.format_exc()),indent=2)+'\n')
    raise
