"""Future PR8178 builder. Not a science runner; execute only after root advances the owned source."""
from pathlib import Path
import argparse,gzip,hashlib,json,re,subprocess,sys
sys.dont_write_bytecode=True
assert __debug__
R=Path('/private/tmp/review-drain-20260915');W=R/'review-draft-slot'
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ref=lambda p:dict(path=str(p),sha256=h(p))
git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
PINNED={
 'drain8178-early-review-v1.json':'1aa3082d5da3e60d9f85f998227f709521bbb78564a60c6d5d1d6e6b53dcd865',
 'drain8178-author-prepared-v2.json':'cc775343be72cc2d20828846ccc05887f8b2248bdeea743502836fec3e952fb7',
 'drain8178-prepared-v2-source-freeze.json':'ae109a49dbcbe6705ecbc1008f9d03a0ab75ca6a711f0cb07083c6891c73d3c1',
 'drain8178-author-handoff-v2.json':'36970f1be22879c07dbc7984c114b75ad460cbadb8f2f12e47d5a5b2d115d852',
 'drain8178-vocab-verification-v2.json':'b02d5856d575b3d70b66fd5a52080986f9732a993eabd547b25031ffe5937b53'}
METADATA_CONFIRMATION_BINDING=None
# Actual reviewer report, exact hash, verdict and source predicates must be
# bound by a future immutable revision. No early-v1 approval of v2 is inferred.
def at(d,p):
 for key in p.lstrip('/').split('/'):d=d[key.replace('~1','/').replace('~0','~')]
 return d
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--expected-base',required=True);ap.add_argument('--version',required=True);a=ap.parse_args()
 assert re.fullmatch('[0-9a-f]{40}',a.expected_base) and re.fullmatch('v[0-9]+',a.version)
 base=a.expected_base
 def ownerbase():
  assert json.loads((R/'review-draft-slot.json').read_text())['owner']=='PR8178-author'
  assert git('rev-parse','HEAD')==base==git('rev-parse','origin/main')
 ownerbase();assert not git('diff','--name-only','HEAD') and not git('diff','--cached','--name-only')
 for n,s in PINNED.items():assert h(R/n)==s
 early=json.loads((R/'drain8178-early-review-v1.json').read_text());assert early['verdict']=='EARLY_AFFECTED_SOURCE_ACCEPTED' and early['reviewer_session']=='/root/review_8178' and early['same_session'] is True and early['source_acceptance'] is True and not early['material_science_blockers'] and not early['blockers']
 d=json.loads((R/'drain8178-author-prepared-v2.json').read_text());f=json.loads((R/'drain8178-prepared-v2-source-freeze.json').read_text())['files'];assert len(f)==43
 mb=METADATA_CONFIRMATION_BINDING;assert isinstance(mb,dict),'Actual metadata affected confirmation must be bound before staging'
 mr=Path(mb['path']);assert mr.is_absolute() and mr.resolve().is_relative_to(R) and not mr.resolve().is_relative_to(W) and h(mr)==mb['sha256']
 confirmation=json.loads(mr.read_text());assert confirmation['reviewer_session']=='/root/review_8178' and confirmation['same_session'] is True
 assert mb['required_predicates'] and mb['prepared_v2_freeze_sha256']==PINNED['drain8178-prepared-v2-source-freeze.json']
 for pointer,value in mb['required_predicates'].items():assert at(confirmation,pointer)==value
 old=json.loads((R/'drain8178-author-discovery-v2.json').read_text());handoff=json.loads((R/'drain8178-author-handoff-v2.json').read_text())
 for e in handoff['references']:assert h(Path(e['path']))==e['sha256']
 assert not json.loads((R/'drain8178-vocab-verification-v2.json').read_text())['changed']
 paths=[e['path'] for e in f];assert set(git('ls-files','--others','--exclude-standard').splitlines())==set(paths) and not git('ls-files','--others','--ignored','--exclude-standard')
 def sourcecheck():
  for e in f:
   p=W/e['path'];assert not p.is_symlink() and h(p)==h(R/'drain8178-prepared-v2-source'/e['path'])==e['sha256'];assert ('100755' if p.stat().st_mode&0o111 else '100644')==e['mode']
 sourcecheck()
 mapping=json.loads((R/'drain8178-author-full-mapping-v1.json').read_text());assert len(mapping['originals'])==21
 for row in mapping['originals']:
  for state,x in row['states'].items():
   if x is None:continue
   raw=gzip.decompress((W/x['recovery_path']).read_bytes());assert hashlib.sha256(raw).hexdigest()==x['sha256'] and len(raw)==x['bytes'];assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==x['blob']
 # Fixed scientific/context inputs cannot silently change; new tooling/skill state
 # is frozen explicitly and still requires actual current-main cold confirmation.
 for e in old['ordered_inputs']:assert h(W/e['path'])==e['sha256']
 for e in old['context']:
  if e['path'].startswith('docs/ai_methodology/skills/') or e['role']=='tooling':continue
  assert h(W/e['path'])==e['sha256'],'Changed scientific context requires affected review'
 sys.path[:0]=[str(W/'scripts'),str(W/'docs/audit/scripts')]
 import runner_cache as c,build_citation_graph as g,audit_packet_script_deps as deps
 N=d['note'];P=d['runner'];body=(W/N).read_text();cid=g.claim_id_from_path(W/N)
 assert cid==d['claim_id'] and g.extract_runner(body,N)==P
 assert g.extract_claim_type_hint(body)[1]=='bounded_theorem','Explicit native Type metadata absent; source correction and affected confirmation required before staging'
 assert g.helper_runner_paths_for_claim(cid,P)==deps.helper_runner_paths_for_claim(cid,Path(P).stem)==[] and not g.resolve_helper_runner_paths(P) and not deps.transitive_helpers(Path(P).stem)
 assert list(c.declared_input_paths(W/P))==d['runtime_inputs'] and c.declared_timeout_for(W/P)==60
 fingerprint=c.declared_input_fingerprint(W/P);assert fingerprint==old['actual_input_fingerprint']
 cites=sorted(p.relative_to(W).as_posix() for p in g.extract_citations(body,W/N));assert cites==old['resolved_citations']
 existing=git('ls-tree','-r','--name-only',base,'--','docs').splitlines()
 for p in paths:
  if p.endswith('.md') and Path(p).name not in ['README.md','SKILL.md']:assert not any(Path(p).name.casefold()==Path(q).name.casefold() for q in existing)
 names=['source-handoff','cache-api','resource-plan','unit-draft'];outputs={n:R/f'drain8178-author-{n}-staged-{a.version}.json' for n in names};assert all(not p.exists() for p in outputs.values())
 bind=lambda ps:[dict(path=p,sha256=h(W/p)) for p in sorted(set(ps))]
 tools=['docs/audit/scripts/build_citation_graph.py','docs/audit/scripts/static_pipeline_checkpoint.py','scripts/runner_cache.py','scripts/audit_packet_script_deps.py','docs/audit/scripts/ledger_io.py','docs/audit/data/axiom_premise_nodes.json','docs/audit/data/doc_authority_registry.json']
 context={e['path'] for e in old['context'] if e['role']=='context-not-recursion-premise'}|set(cites)|{'docs/ai_methodology/skills/review-loop/scripts/review_receipt.py','scripts/vocab_lint.py','docs/repo/controlled_vocabulary.yaml'}
 toolpins=bind(tools);contextpins=bind(context);runtime=bind(d['runtime_inputs']+[P]);parents=bind(d['runtime_inputs'][1:])
 ownerbase();sourcecheck();subprocess.run(['git','-C',str(W),'add','--',*paths],check=True)
 assert set(git('diff','--cached','--name-only').splitlines())==set(paths) and not git('diff','--name-only');subprocess.run(['git','-C',str(W),'diff','--cached','--check'],check=True)
 tree=git('write-tree');ownerbase();sourcecheck();assert toolpins==bind(tools) and contextpins==bind(context) and runtime==bind(d['runtime_inputs']+[P])
 def save(name,value):
  p=outputs[name]
  with p.open('x') as f:json.dump(value,f,indent=2);f.write('\n')
  return p
 original=json.loads((R/'drain8178-review-original.json').read_text());judgments={x['path']:x for x in original['coverage']};rows=[]
 for x in mapping['originals']:
  head=x['states']['head'];rows.append(dict(original_path=x['original_path'],original_sha256=head['sha256'],disposition=judgments[x['original_path']]['disposition'],recovery=dict(states=x['states'],full_mapping=ref(R/'drain8178-author-full-mapping-v1.json')),final_path=head['recovery_path'],final_sha256=h(W/head['recovery_path'])))
 refs=[ref(R/n) for n in PINNED]+handoff['references']+[ref(mr),ref(Path(__file__).resolve())]
 sp=save('source-handoff',dict(base=base,tree=tree,original_dispositions=rows,scientific_claim_dispositions=json.loads((R/'drain8178-author-finding-dispositions-v1.json').read_text()),complete_recovery=mapping,original_review=ref(R/'drain8178-review-original.json'),early_review=ref(R/'drain8178-early-review-v1.json'),references=refs))
 api=save('cache-api',dict(actual_base=base,source_tree=tree,claim_id=cid,runner=P,helpers=[],citations=cites,input_fingerprint=fingerprint,inputs=runtime,tooling=toolpins,context=contextpins,registry_edits=[]))
 plan=json.loads((R/'drain8178-author-input-resource-plan-v2.json').read_text());plan.update(status='Actual candidate source/API frozen; cold execution clearance still pending',actual_base=base,actual_tree=tree,actual_api=ref(api));pp=save('resource-plan',plan)
 record=dict(schema_version=2,unit_id='PR8178',constituents=[dict(id='PR8178',head=d['original_head'],delta_base=json.loads((R/'drain8178-original/manifest.json').read_text())['base'],dispositions=dict(ref(sp),json_pointer='/original_dispositions'))],source=dict(base=base,commit=base,tree=tree,paths=bind(paths),deleted_paths=[]),inputs=dict(runtime=runtime,helpers=[],parents=parents,context=contextpins,tooling=toolpins),reviewer=dict(session='/root/review_8178; actual cold and final confirmation pending',report=ref(R/'drain8178-early-review-v1.json'),references=refs+[ref(sp),ref(api),ref(pp)]),notes=[dict(path=N,claim_id=cid,declared_claim_id=re.search(r'^claim_id: (.+)$',body,re.M)[1],claim_type='bounded_theorem',primary_runner=P,helpers=[],citations=cites,repository_dependencies=d['runtime_inputs'][1:],dependency_rationale=plan['mathematical_premise_closure'])],supporting_proofs=[],non_science_notes=[dict(path=p,rationale='Historical full original argument and recovery mapping; corrected/deferred explicitly, not current theorem or audit authority.',review_reference=ref(R/'drain8178-early-review-v1.json')) for p in paths if p.endswith('.md') and p!=N])
 print(json.dumps(ref(save('unit-draft',record))))
if __name__=='__main__':main()
