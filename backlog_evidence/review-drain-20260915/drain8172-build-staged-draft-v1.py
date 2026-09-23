"""Proposed root-dispatched builder; never executes science. Unknown review schemas fail closed."""
from pathlib import Path
import argparse,ast,gzip,hashlib,io,json,re,subprocess,sys,tarfile,traceback
sys.dont_write_bytecode=True
assert __debug__
R=Path('/private/tmp/review-drain-20260915');W=R/'review-meta-slot'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ref=lambda p:dict(path=str(p),sha256=sha(p))
git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
bind=lambda ps:[dict(path=p,sha256=sha(W/p)) for p in sorted(set(ps))]
def pointer(d,p):
    assert p.startswith('/')
    for key in p[1:].split('/'):d=d[key.replace('~1','/').replace('~0','~')]
    return d
def report(path,digest,verdict_pointer,allowed):
    p=Path(path);assert p.is_absolute() and p.resolve().is_relative_to(R) and not p.resolve().is_relative_to(W) and not p.is_symlink()
    assert re.fullmatch('[0-9a-f]{64}',digest) and sha(p)==digest
    d=json.loads(p.read_text());assert d.get('reviewer_session')=='/root/review_8172'
    assert pointer(d,verdict_pointer) in allowed,'Missing or unrecognized reviewer verdict; preserve report and adapt separately, never infer approval'
    return p,d

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--expected-base',required=True);ap.add_argument('--stage-authorized',action='store_true',required=True);ap.add_argument('--version',required=True);ap.add_argument('--review',required=True);ap.add_argument('--review-sha256',required=True);ap.add_argument('--review-verdict-pointer',required=True);a=ap.parse_args()
    assert a.stage_authorized and re.fullmatch('[0-9a-f]{40}',a.expected_base) and re.fullmatch('v[1-9][0-9]*',a.version)
    failure=R/f'drain8172-builder-failure-{a.version}.json';assert not failure.exists()
    try:
        assert sha(R/'drain8172-builder-bindings-v1.json')=='849643a316435ba1b5c22f5ab2a63eaba02e74b12e7b8a077245c28f96874473'
        refs=json.loads((R/'drain8172-builder-bindings-v1.json').read_text())
        for e in refs:assert sha(Path(e['path']))==e['sha256'],e['path']
        d=json.loads((R/'drain8172-author-prepared-v1.json').read_text());f=json.loads((R/'drain8172-prepared-v1-source-freeze.json').read_text())['files'];assert len(f)==31
        plan=json.loads((R/'drain8172-author-input-resource-plan-v1.json').read_text());discovery=json.loads((R/'drain8172-author-discovery-v1.json').read_text())
        rp,review=report(a.review,a.review_sha256,a.review_verdict_pointer,{'EARLY SOURCE CLEARANCE FOR ROOT-OWNED STAGING, COLD FREEZE AND BOUNDED CAPTURE; NOT FINAL PASS'})
        assert a.review_sha256=='fe87a74880688bbfcc113cb932943ee206dd7aa069882397e0b2c0abfa0ea503' and a.review_verdict_pointer=='/verdict'
        assert review['source_files']==f and not review['new_findings'] and ref(R/'drain8172-prepared-v1-source-freeze.json') in review['references']
        owner=json.loads((R/'review-meta-slot.json').read_text());assert owner['owner']=='PR8172-author' and Path(owner['path']).resolve()==W.resolve()
        assert git('rev-parse','HEAD')==a.expected_base==git('rev-parse','origin/main')
        assert not git('diff','--name-only','HEAD') and not git('diff','--cached','--name-only')
        assert set(git('ls-files','--others','--exclude-standard').splitlines())=={e['path'] for e in f}
        assert not git('ls-files','--others','--ignored','--exclude-standard')
        def verify():
            for e in f:
                p=W/e['path'];q=Path(e['immutable_copy']);assert not p.is_symlink() and not q.is_symlink()
                assert sha(p)==sha(q)==e['sha256'] and oct(p.stat().st_mode&0o777)==oct(q.stat().st_mode&0o777)==e['mode']
            for e in plan['ordered_inputs']+plan['context_only']:assert sha(W/e['path'])==e['sha256'],'Input/context changed; obtain affected confirmation'
        verify()
        archive=Path(d['archive_manifest']['path']).parent;manifest=json.loads((W/d['archive_manifest']['path']).read_text());mapping=json.loads((R/'drain8172-author-full-mapping-v2.json').read_text());inv=json.loads((R/'drain8172-original/inventory.json').read_text())
        originals={e['path']:e for e in inv['paths']};mapped={e['original_path']:e for e in mapping}
        assert len(originals)==len(mapping)==len(manifest['entries'])==24 and set(originals)==set(mapped)=={e['original_path'] for e in manifest['entries']}
        for e in manifest['entries']:
            o=originals[e['original_path']];m=mapped[e['original_path']];assert [o['original']['mode'],'blob',o['original']['blob']]==[e['original_mode'],'blob',e['git_blob']]
            p=W/archive/e['stored_path'];assert sha(p)==e['stored_sha256'];payload=p.read_bytes();raw=gzip.decompress(payload) if e['encoding']=='gzip' else payload
            assert hashlib.sha256(raw).hexdigest()==o['original']['sha256']==e['raw_sha256']==m['original_sha256']
            assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==m['original_blob']==e['git_blob']
            assert m['original_mode']==e['original_mode'] and m['recovery']==str(archive/e['stored_path'])
            if m['final_path']:assert sha(W/m['final_path'])==m['final_sha256']
        inherited=manifest['inherited_packet'];ip=W/archive/inherited['path'];assert sha(ip)==inherited['stored_sha256']
        tarraw=gzip.decompress(ip.read_bytes());assert hashlib.sha256(tarraw).hexdigest()==inherited['raw_tar_sha256']
        inventory_path=W/archive/inherited['inventory_path'];assert sha(inventory_path)==inherited['inventory_sha256']
        inherited_rows=json.loads(inventory_path.read_text());assert len(inherited_rows)==79
        with tarfile.open(fileobj=io.BytesIO(tarraw)) as tar:
            members={m.name:m for m in tar.getmembers() if m.isfile()}
            assert set(members)=={e['path'] for e in inherited_rows}
            for e in inherited_rows:
                m=members[e['path']];raw=tar.extractfile(m).read()
                assert hashlib.sha256(raw).hexdigest()==e['sha256'] and hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==e['blob']
                assert (m.mode&0o111)==(int(e['mode'],8)&0o111)
        # Original tar headers are preserved; Git modes in inventory are the restoration authority.
        sys.path[:0]=[str(W/'scripts'),str(W/'docs/audit/scripts')]
        import runner_cache as c,audit_packet_script_deps as aapi,build_citation_graph as g
        note=d['notes'][0]['path'];runner=d['runners'][0]['path'];body=(W/note).read_text();cid=g.claim_id_from_path(W/note)
        assert cid==discovery['claim_id'] and g.extract_runner(body,note)==runner
        assert list(g.helper_runner_paths_for_claim(cid,runner))==list(aapi.helper_runner_paths_for_claim(cid,Path(runner).stem))==[]
        assert not aapi.transitive_helpers(Path(runner).stem) and not g.resolve_helper_runner_paths(runner)
        cites=sorted(p.relative_to(W).as_posix() for p in g.extract_citations(body,W/note));assert cites==discovery['citations']
        tree=ast.parse((W/runner).read_text());decl={n.targets[0].id:n.value for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name)}
        ins=[e['path'] for e in plan['ordered_inputs']]
        assert list(ast.literal_eval(decl['AUDIT_INPUT_PATHS']))==list(c.declared_input_paths(W/runner))==ins
        assert ast.literal_eval(decl['EXPECTED_INPUT_SHA256'])=={e['path']:e['sha256'] for e in plan['ordered_inputs']}
        assert c.declared_timeout_for(W/runner)==900 and ast.literal_eval(decl['AUDIT_MEMORY_MB'])==768
        assert c.declared_input_fingerprint(W/runner)==discovery['input_fingerprint']
        skill='docs/ai_methodology/skills/review-loop'
        tooling=['docs/audit/scripts/build_citation_graph.py','docs/audit/scripts/static_pipeline_checkpoint.py','scripts/runner_cache.py','scripts/audit_packet_script_deps.py','docs/audit/scripts/ledger_io.py','docs/audit/data/axiom_premise_nodes.json','docs/audit/data/doc_authority_registry.json']
        context=set(cites)|{e['path'] for e in plan['context_only']}|{d['deferred_science']['path'],d['archive_manifest']['path'],skill+'/SKILL.md',skill+'/PREFLIGHT.md',skill+'/scripts/review_receipt.py',skill+'/scripts/review_workspace.py'}|{p.relative_to(W).as_posix() for p in (W/skill/'references').glob('*.md')}
        outputs={k:R/f'drain8172-author-{k}-{a.version}.json' for k in ['unit-draft','source-handoff','cache-api']};assert all(not p.exists() for p in outputs.values())
        tools_before=bind(tooling);verify();assert git('rev-parse','HEAD')==a.expected_base==git('rev-parse','origin/main') and not git('diff','--name-only','HEAD')
        subprocess.run(['git','-C',str(W),'add','--',*[e['path'] for e in f]],check=True)
        subprocess.run(['git','-C',str(W),'diff','--cached','--check'],check=True)
        assert set(git('diff','--cached','--name-only').splitlines())=={e['path'] for e in f} and not git('diff','--name-only') and tools_before==bind(tooling)
        stagedtree=git('write-tree');evidence=refs+[ref(rp)]
        api=dict(discovery,actual_current_base=a.expected_base,source_tree=stagedtree);outputs['cache-api'].write_text(json.dumps(api,indent=2)+'\n')
        claims=json.loads((R/'drain8172-author-finding-dispositions-v1.json').read_text())['claims']
        handoff=dict(status='AUTHOR MAPPING; ORIGINAL REVIEWER CURRENT-BASE COLD AND FINAL CONFIRMATION REQUIRED',original_dispositions=mapping,claim_dispositions=claims,base=a.expected_base,tree=stagedtree,mathematical_closure=plan['mathematical_closure'],runtime_scope='One SymPy/standard-library primary plus three literal proof inputs; historical simulations and all79 inherited entries remain recovery only',branch_retention_required=True,inherited_dispositions=[dict(e,recovery=str(archive/inherited['path'])+' member '+e['path'],mode_recovery='Restore original Git mode from pinned inventory') for e in inherited_rows],registry_changes=[],references=evidence)
        outputs['source-handoff'].write_text(json.dumps(handoff,indent=2)+'\n')
        history=[e['path'] for e in f if e['path'].startswith(str(archive)+'/') and e['path'].endswith('.md')]
        record=dict(schema_version=2,unit_id='PR8172',constituents=[dict(id='PR8172',head=d['original_head'],delta_base=d['original_merge_base'],dispositions=dict(ref(outputs['source-handoff']),json_pointer='/original_dispositions'))],source=dict(base=a.expected_base,commit=a.expected_base,tree=stagedtree,paths=bind(e['path'] for e in f),deleted_paths=[]),inputs=dict(runtime=bind(ins+[runner]),helpers=[],parents=bind(discovery['parents']),context=bind(context),tooling=tools_before),reviewer=dict(session='/root/review_8172; current-base cold and final evidence confirmation pending',report=ref(R/'drain8172-review-original.json'),references=evidence+[ref(outputs['cache-api']),ref(outputs['source-handoff'])]),notes=[dict(path=note,claim_id=cid,declared_claim_id=re.search(r'^claim_id: (.+)$',body,re.M)[1],claim_type='bounded_theorem',primary_runner=runner,helpers=[],citations=cites,repository_dependencies=discovery['parents'],dependency_rationale=plan['mathematical_closure'])],supporting_proofs=[],non_science_notes=[dict(path=p,rationale='Historical or explicitly deferred science, not current premise authority. Original threshold, sphere coupling and broader scientific claims remain readable with exact failures; formal negative promotion is deferred with branch retention. Current complete proofs reside in canonical note, with no supporting proof omitted.',review_reference=ref(rp)) for p in history])
        outputs['unit-draft'].write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(ref(outputs['unit-draft'])))
    except BaseException as e:
        if not failure.exists():failure.write_text(json.dumps(dict(status='FAILED; preserve partial index state and evidence',error=repr(e),traceback=traceback.format_exc()),indent=2)+'\n')
        raise
if __name__=='__main__':main()
