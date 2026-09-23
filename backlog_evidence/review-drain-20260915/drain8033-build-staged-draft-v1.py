"""Future guarded builder: parent must actually be present on the fresh main base."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
sys.dont_write_bytecode=True
assert __debug__
R=Path('/private/tmp/review-drain-20260915');W=R/'author-draft-slot';h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ref=lambda p:dict(path=str(p),sha256=h(p));git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
def main():
 base=sys.argv[1];assert re.fullmatch('[0-9a-f]{40}',base);assert git('rev-parse','HEAD')==base==git('rev-parse','origin/main');assert json.loads((R/'author-draft-slot.json').read_text())['owner']=='PR8033-author'
 assert not git('diff','--name-only','HEAD') and not git('diff','--cached','--name-only')
 rp=R/'drain8033-early-review-v1.json';assert h(rp)=='c6f42cecc763967deec0e6e0e4e9522d3382225b2255d61442741023a0ab50e4';review=json.loads(rp.read_text());assert review['reviewer_session']=='/root/review_8033' and review['status']=='SOURCE ACCEPTED conditional on actual parent8032 landing and executable closure; not execution/cold/final landing clearance'
 dp=R/'drain8033-author-prepared-v1.json';fp=R/'drain8033-prepared-v1-source-freeze.json';assert h(dp)=='b6bb3c0f2e3e7c1c16b211a633e57ee8bf5d15dc37984109f0eccdd555ad0403' and h(fp)=='488698c6912ecf689fc068bb894df145dbcf357c9147ec4d58c5c47764c6e944'
 d=json.loads(dp.read_text());f=json.loads(fp.read_text())['files'];assert len(f)==81 and set(git('ls-files','--others','--exclude-standard').splitlines())=={e['path'] for e in f};assert not git('ls-files','--others','--ignored','--exclude-standard')
 for e in f:
  p=W/e['path'];assert not p.is_symlink() and h(p)==h(Path(e['immutable_copy']))==e['sha256'] and oct(p.stat().st_mode&0o777)==e['mode']
 parent=d['pending_parent'];assert h(W/parent['path'])==parent['sha256']=='af043363c9ff1bb69829cb991c2ddd7f5bcde0ae9d57fc550ac55f58fccd71c6';assert hashlib.sha256(subprocess.check_output(['git','-C',str(W),'show',base+':'+parent['path']])).hexdigest()==parent['sha256']
 for e in d['ordered_inputs']:assert h(W/e['path'])==e['sha256']
 sys.path[:0]=[str(W/'scripts'),str(W/'docs/audit/scripts')]
 import runner_cache as c,build_citation_graph as g,audit_packet_script_deps as a
 N=d['note']['path'];P=d['runner']['path'];body=(W/N).read_text();cid=g.claim_id_from_path(W/N);assert g.extract_runner(body,N)==P;assert g.helper_runner_paths_for_claim(cid,P)==a.helper_runner_paths_for_claim(cid,Path(P).stem)==[] and not g.resolve_helper_runner_paths(P) and not a.transitive_helpers(Path(P).stem)
 assert list(c.declared_input_paths(W/P))==[e['path'] for e in d['ordered_inputs']];fingerprint=c.declared_input_fingerprint(W/P);assert fingerprint and c.declared_timeout_for(W/P)==180
 old=json.loads((R/'drain8033-author-discovery-v1.json').read_text());cites=sorted(p.relative_to(W).as_posix() for p in g.extract_citations(body,W/N));assert cites==old['intended_citations'];parents=[e['path'] for e in d['ordered_inputs']][1:]
 for e in old['context']:assert h(W/e['path'])==e['sha256'],'Changed context requires affected review'
 existing=git('ls-tree','-r','--name-only',base,'--','docs').splitlines()
 for e in f:
  if e['path'].endswith('.md') and Path(e['path']).name not in ['README.md','SKILL.md']:assert not any(Path(p).name.casefold()==Path(e['path']).name.casefold() for p in existing)
 for name in ['unit-draft','source-handoff','cache-api','resource-plan']:assert not (R/f'drain8033-author-{name}-staged-v1.json').exists()
 bind=lambda ps:[dict(path=p,sha256=h(W/p)) for p in sorted(set(ps))]
 tools=['docs/audit/scripts/build_citation_graph.py','docs/audit/scripts/static_pipeline_checkpoint.py','scripts/runner_cache.py','scripts/audit_packet_script_deps.py','docs/audit/scripts/ledger_io.py','docs/audit/data/axiom_premise_nodes.json','docs/audit/data/doc_authority_registry.json']
 toolpins=bind(tools);paths=[e['path'] for e in f];subprocess.run(['git','-C',str(W),'add','--',*paths],check=True);assert set(git('diff','--cached','--name-only').splitlines())==set(paths) and not git('diff','--name-only');tree=git('write-tree');assert toolpins==bind(tools)
 def save(name,x):
  p=R/f'drain8033-author-{name}-staged-v1.json'
  with p.open('x') as o:json.dump(x,o,indent=2);o.write('\n')
  return p
 refs=[ref(p) for p in [dp,fp,rp,R/'drain8033-author-handoff-v1.json',R/'drain8033-author-full-mapping-v1.json',Path(__file__).resolve()]]
 sp=save('source-handoff',dict(original_dispositions=json.loads((R/'drain8033-author-full-mapping-v1.json').read_text()),proof_obligations=json.loads((R/'drain8033-author-finding-dispositions-v1.json').read_text())['proof_obligations'],base=base,tree=tree,references=refs))
 ap=save('cache-api',dict(actual_base=base,source_tree=tree,claim_id=cid,primary_runner=P,helpers=[],citations=cites,parents=parents,input_fingerprint=fingerprint,inputs=bind([e['path'] for e in d['ordered_inputs']]),tooling=toolpins,parent_landed_exact=True))
 plan=json.loads((R/'drain8033-author-input-resource-plan-v1.json').read_text());plan['status']='Actual source/input closure frozen; execution remains pending cold clearance';plan['actual_base']=base;plan['actual_tree']=tree;plan['actual_api']=ref(ap);plan['parent_landed_exact']=True
 for e in plan['ordered_inputs']:e['state']='present on actual frozen candidate'
 pp=save('resource-plan',plan)
 history=[p for p in paths if p.endswith('.md') and p!=N];context={e['path'] for e in old['context']}|set(cites)|{'docs/ai_methodology/skills/review-loop/scripts/review_receipt.py'}
 record=dict(schema_version=2,unit_id='PR8033',constituents=[dict(id='PR8033',head=d['original_head'],delta_base=d['original_base'],dispositions=dict(ref(sp),json_pointer='/original_dispositions'))],source=dict(base=base,commit=base,tree=tree,paths=bind(paths),deleted_paths=[]),inputs=dict(runtime=bind([e['path'] for e in d['ordered_inputs']]+[P]),helpers=[],parents=bind(parents),context=bind(context),tooling=toolpins),reviewer=dict(session='/root/review_8033; actual cold and final confirmation pending',report=ref(rp),references=refs+[ref(sp),ref(ap),ref(pp)]),notes=[dict(path=N,claim_id=cid,declared_claim_id=re.search(r'^claim_id: (.+)$',body,re.M)[1],claim_type='bounded_theorem',primary_runner=P,helpers=[],citations=cites,repository_dependencies=parents,dependency_rationale=plan['mathematical_closure'])],supporting_proofs=[],non_science_notes=[dict(path=p,rationale='Exact historical packet recovery, including failures and prospective planning; both accepted complete proofs are inline in current canonical note, no historical review/audit authority adopted.',review_reference=ref(rp)) for p in history])
 p=save('unit-draft',record);print(json.dumps(ref(p)))
if __name__=='__main__':main()
