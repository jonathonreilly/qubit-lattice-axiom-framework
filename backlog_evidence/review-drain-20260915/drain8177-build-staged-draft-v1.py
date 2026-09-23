"""Proposed root-only guarded staging; no science execution or preflight. Unexecuted author artifact."""
from pathlib import Path
import argparse,ast,gzip,hashlib,json,re,subprocess,sys,traceback
sys.dont_write_bytecode=True
assert __debug__
R=Path('/private/tmp/review-drain-20260915');W=R/'drain-author-slot'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ref=lambda p:dict(path=str(p),sha256=sha(p))
git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
bind=lambda ps:[dict(path=p,sha256=sha(W/p)) for p in sorted(set(ps))]
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--expected-base',required=True);ap.add_argument('--stage-authorized',action='store_true',required=True);ap.add_argument('--version',required=True);a=ap.parse_args()
    assert a.stage_authorized and re.fullmatch('[0-9a-f]{40}',a.expected_base) and re.fullmatch('v[1-9][0-9]*',a.version)
    failure=R/f'drain8177-builder-failure-{a.version}.json';assert not failure.exists()
    try:
        bp=R/'drain8177-adapter-bindings-v1.json';assert sha(bp)==BINDINGS_SHA256
        refs=json.loads(bp.read_text())
        for e in refs:assert sha(Path(e['path']))==e['sha256'],e['path']
        d=json.loads((R/'drain8177-author-prepared-v2.json').read_text());f=d['source'];assert len(f)==56
        discovery=json.loads((R/'drain8177-source-input-discovery-v2.json').read_text());plan=json.loads((R/'drain8177-resource-plan-v2.json').read_text());prior=json.loads((R/'drain8177-adapter-authority-v1.json').read_text())
        rp=R/'drain8177-early-review-v2.json';review=json.loads(rp.read_text())
        assert sha(rp)=='ed75a124bfed8de37e9453cd050767e4353b498a7e4e30150c708b8ede5895fa'
        assert review['schema_version']==1 and review['kind']=='same-session-affected-source-review-not-landing-pass'
        assert review['reviewer']=='/root/review_8177' and review['pr']==8177 and review['iteration']==2
        assert review['verdict']=='CLEAR FOR COLD REVIEW AND BOUNDED EVIDENCE CAPTURE' and review['new_material_findings']==[]
        assert review['original_head']==d['head'] and review['source']==f
        assert review['source_freeze_sha256']==sha(R/'drain8177-source-freeze-v2.json') and review['handoff_sha256']==sha(R/'drain8177-author-handoff-v2.json')
        vv=review['verification'];assert vv['frozen_sources']==56 and vv['original_payloads_verified']==50 and vv['delta_verified'] and vv['eight_certificates_unchanged']
        assert vv['literal_input_pins_verified']=={e['path']:e['sha256'] for e in discovery['runtime_inputs']}
        ec=review['resource_plan_clearance'];assert ec['baseline_runs']==ec['targeted_mutation_runs']==1 and ec['targeted_mutation']=='predecessor_profile_wrong'
        assert ec['expected_baseline']=='TOTAL: PASS=18 FAIL=0' and ec['expected_mutation']=='TOTAL: PASS=17 FAIL=1; C1 only'
        assert ec['wall_seconds_per_run']==plan['timeout_seconds']==120 and ec['sampled_process_tree_memory_bytes']==plan['memory_limit_bytes']==402653184
        owner=json.loads((R/'drain-author-slot.json').read_text());assert owner['owner']=='PR8177-author' and Path(owner['path']).resolve()==W.resolve()
        assert git('rev-parse','HEAD')==a.expected_base==git('rev-parse','origin/main')
        assert not git('diff','--name-only','HEAD') and not git('diff','--cached','--name-only')
        assert set(git('ls-files','--others','--exclude-standard').splitlines())=={e['path'] for e in f}
        assert not git('ls-files','--others','--ignored','--exclude-standard')
        def verify():
            for e in f:
                p=W/e['path'];q=Path(d['snapshot'])/e['path'];assert not p.is_symlink() and not q.is_symlink()
                assert sha(p)==sha(q)==e['sha256'] and p.stat().st_mode&0o777==q.stat().st_mode&0o777==int(e['mode'][-3:],8)
            for e in discovery['runtime_inputs']+prior['authority']:assert sha(W/e['path'])==e['sha256'],'Changed input/authority requires affected review'
        verify()
        manifest=json.loads((W/d['original_manifest']['path']).read_text());assert sha(W/d['original_manifest']['path'])==d['original_manifest']['sha256']
        original=json.loads((R/'drain8177-review-original.json').read_text())['path_dispositions'];old={x['path']:x for x in original}
        authored=json.loads((R/'drain8177-author-dispositions-v1.json').read_text());mapping=authored['constituents'][0]['dispositions']
        assert mapping==manifest['entries'] and len(old)==len(mapping)==50 and set(old)=={e['original_path'] for e in mapping}
        rows=[]
        for e in mapping:
            o=old[e['original_path']]['original']['head'];assert (o['mode'],o['blob'])==(e['original_mode'],e['original_blob'])
            rec=e['recovery'];p=W/rec['path'];assert sha(p)==rec['sha256'];raw=gzip.decompress(p.read_bytes())
            assert hashlib.sha256(raw).hexdigest()==o['sha256']==e['original_sha256']==rec['decoded_sha256']
            assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==e['original_blob']
            final=e['final_path']
            rows.append(dict(original_path=e['original_path'],original_sha256=e['original_sha256'],original_mode=e['original_mode'],original_blob=e['original_blob'],disposition=e['disposition'],recovery=rec,final_path=final,final_sha256=sha(W/final) if final else None))
        delta=manifest['original_delta'];assert sha(W/delta['path'])==delta['sha256']
        assert hashlib.sha256(gzip.decompress((W/delta['path']).read_bytes())).hexdigest()==delta['decoded_sha256']
        assert (R/'drain8177-original/original.delta').read_bytes()==gzip.decompress((W/delta['path']).read_bytes())
        existing={Path(p).name for p in git('ls-files','docs').splitlines()}
        newdocs=[e['path'] for e in f if e['path'].startswith('docs/') and Path(e['path']).name not in ['README.md','SKILL.md']]
        assert not [p for p in newdocs if Path(p).name in existing] and len({Path(p).name for p in newdocs})==len(newdocs)
        sys.path[:0]=[str(W/'scripts'),str(W/'docs/audit/scripts')]
        import runner_cache as c,audit_packet_script_deps as aapi,build_citation_graph as g
        note=d['canonical_notes'][0];runner=d['primaries'][0];body=(W/note).read_text();cid=g.claim_id_from_path(W/note)
        assert g.extract_runner(body,note)==runner==discovery['primary']
        assert list(g.helper_runner_paths_for_claim(cid,runner))==list(aapi.helper_runner_paths_for_claim(cid,Path(runner).stem))==[]
        assert not aapi.transitive_helpers(Path(runner).stem) and not g.resolve_helper_runner_paths(runner)
        cites=sorted(p.relative_to(W).as_posix() for p in g.extract_citations(body,W/note));assert cites==sorted(discovery['citations'])
        tree=ast.parse((W/runner).read_text());decl={n.targets[0].id:n.value for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name)}
        ins=[e['path'] for e in discovery['runtime_inputs']]
        assert list(ast.literal_eval(decl['AUDIT_INPUT_PATHS']))==list(c.declared_input_paths(W/runner))==ins
        assert ast.literal_eval(decl['INPUT_SHA256'])=={e['path']:e['sha256'] for e in discovery['runtime_inputs']}
        assert c.declared_timeout_for(W/runner)==120 and c.declared_input_fingerprint(W/runner)==discovery['input_fingerprint']
        skill='docs/ai_methodology/skills/review-loop'
        tooling=['docs/audit/scripts/build_citation_graph.py','docs/audit/scripts/static_pipeline_checkpoint.py','scripts/runner_cache.py','scripts/audit_packet_script_deps.py','docs/audit/scripts/ledger_io.py','docs/audit/data/axiom_premise_nodes.json','docs/audit/data/doc_authority_registry.json']
        context=set(cites)|set(ins[2:])|set(d['deferred_science'])|{d['original_manifest']['path'],skill+'/SKILL.md',skill+'/PREFLIGHT.md',skill+'/scripts/review_receipt.py',skill+'/scripts/review_workspace.py'}|{e['path'] for e in prior['authority']}|{p.relative_to(W).as_posix() for p in (W/skill/'references').glob('*.md')}
        outputs={k:R/f'drain8177-author-{k}-{a.version}.json' for k in ['unit-draft','source-handoff','cache-api']};assert all(not p.exists() for p in outputs.values())
        assert len(tooling[:5])==5 and len(set(tooling))==len(tooling)
        # Bind installed-at-base tooling/methodology, never reuse old discovery tooling hashes.
        for p in set(tooling)|context:
            if p in {e['path'] for e in f}:continue
            committed=subprocess.check_output(['git','-C',str(W),'show',a.expected_base+':'+p])
            assert sha(W/p)==hashlib.sha256(committed).hexdigest(), 'Tool/context differs from fresh base: '+p
        tools_before=bind(tooling);verify();assert git('rev-parse','HEAD')==a.expected_base==git('rev-parse','origin/main') and not git('diff','--name-only','HEAD')
        subprocess.run(['git','-C',str(W),'add','--',*[e['path'] for e in f]],check=True)
        subprocess.run(['git','-C',str(W),'diff','--cached','--check'],check=True)
        assert set(git('diff','--cached','--name-only').splitlines())=={e['path'] for e in f} and not git('diff','--name-only') and tools_before==bind(tooling)
        stagedtree=git('write-tree');evidence=refs+[ref(bp),ref(Path(__file__).resolve())]
        api=dict(discovery,actual_current_base=a.expected_base,source_tree=stagedtree,current_tooling=tools_before,current_context=bind(context),current_api=dict(declared_inputs=list(c.declared_input_paths(W/runner)),timeout=c.declared_timeout_for(W/runner),fingerprint=c.declared_input_fingerprint(W/runner),citations=cites,graph_helpers=list(g.helper_runner_paths_for_claim(cid,runner)),packet_helpers=sorted(aapi.transitive_helpers(Path(runner).stem))));outputs['cache-api'].write_text(json.dumps(api,indent=2)+'\n')
        rationale='Complete finite extension/seed/induction proofs with explicit sufficient H implication, corrected finite profiles, and weight-preserving relaxed lifted-tree injection. Eight rational points unchanged; no exact occupancy count or universal restricted admissibility. Four actual runtime source pins; product model and landed two-level full-slot/application parents explicitly scoped; no unlanded sibling import. Complete50original recovery and readable negative/history limitations; branch retention required.'
        handoff=dict(status='AUTHOR IDENTITY ADAPTER; ORIGINAL REVIEWER CURRENT-BASE COLD AND FINAL CONFIRMATION REQUIRED',original_dispositions=rows,original_delta=delta,claim_dispositions=authored['claims'],base=a.expected_base,tree=stagedtree,mathematical_closure=rationale,branch_retention_required=True,registry_changes=[],references=evidence)
        outputs['source-handoff'].write_text(json.dumps(handoff,indent=2)+'\n')
        record=dict(schema_version=2,unit_id='PR8177',constituents=[dict(id='PR8177',head=d['head'],delta_base=manifest['delta_base'],dispositions=dict(ref(outputs['source-handoff']),json_pointer='/original_dispositions'))],source=dict(base=a.expected_base,commit=a.expected_base,tree=stagedtree,paths=bind(e['path'] for e in f),deleted_paths=[]),inputs=dict(runtime=bind(ins+[runner]),helpers=[],parents=bind(discovery['framework_dependencies']),context=bind(context),tooling=tools_before),reviewer=dict(session='/root/review_8177; staged current-base cold and final evidence confirmation pending',report=ref(R/'drain8177-review-original.json'),references=evidence+[ref(outputs['cache-api']),ref(outputs['source-handoff'])]),notes=[dict(path=note,claim_id=cid,declared_claim_id=re.search(r'^claim_id: (.+)$',body,re.M)[1],claim_type='bounded_theorem',primary_runner=runner,helpers=[],citations=cites,repository_dependencies=discovery['framework_dependencies'],dependency_rationale=rationale)],supporting_proofs=[],non_science_notes=[dict(path='docs/work_history/review_loop/pr8177/README.md',rationale='Recovery index only; complete original note remains readable history with explicit corrections, and all 50 original payloads are exact. Complete corrected finite proofs reside in the canonical note; historical samplers and empirical claims are not inputs or supporting premises.',review_reference=ref(rp))])
        outputs['unit-draft'].write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(ref(outputs['unit-draft'])))
    except BaseException as e:
        if not failure.exists():failure.write_text(json.dumps(dict(status='FAILED; preserve partial index state and evidence',error=repr(e),traceback=traceback.format_exc()),indent=2)+'\n')
        raise
BINDINGS_SHA256='743cd93222afc8f31063f65a58314979d9179ac6677608ba66ff445c4cc19b4e'
if __name__=='__main__':main()
