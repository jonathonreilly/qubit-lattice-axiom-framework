from pathlib import Path
import ast,gzip,hashlib,json,re,subprocess,sys
sys.dont_write_bytecode=True
R=Path('/private/tmp/review-drain-20260915');W=R/'review-meta-slot';h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ref=lambda p:dict(path=str(p),sha256=h(p));git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
base=sys.argv[1];assert re.fullmatch('[0-9a-f]{40}',base)
assert json.loads((R/'review-meta-slot.json').read_text())['owner']=='PR8032-author'
assert git('rev-parse','HEAD')==base==git('rev-parse','origin/main');assert not git('diff','--cached','--name-only')
rp=R/'drain8032-early-review-v2.json';assert h(rp)=='a440feea0e62644e0ca0190f11b1cb1f69e9d9420b5514783675cfcd81fc138e';review=json.loads(rp.read_text());assert review['verdict']=='IO BLOCKER RESOLVED; SOURCE ACCEPTED FOR STAGING AND ACTUAL COLD FREEZE' and review['findings']==[]
f=json.loads((R/'drain8032-prepared-v2-source-freeze.json').read_text())['files'];d=json.loads((R/'drain8032-author-prepared-v2.json').read_text());application=json.loads((R/'drain8032-registry-application-v1.json').read_text());maps=application['changes'];assert len(f)==82 and len(maps)==2
assert set(git('ls-files','--others','--exclude-standard').splitlines())=={e['path'] for e in f};assert not git('ls-files','--others','--ignored','--exclude-standard');assert set(git('diff','--name-only').splitlines())=={e['path'] for e in maps}
for e in f:
 p=W/e['path'];assert not p.is_symlink() and h(p)==h(Path(e['immutable_copy']))==e['sha256'] and oct(p.stat().st_mode&0o777)==e['mode']
for e in maps:
 assert h(W/e['path'])==h(Path(e['proposed']['path']))==e['proposed']['sha256'];assert hashlib.sha256(subprocess.check_output(['git','-C',str(W),'show',base+':'+e['path']])).hexdigest()==e['current_sha256']
plan=json.loads((R/'drain8032-author-input-resource-plan-v2.json').read_text());dis=json.loads((R/'drain8032-author-discovery-v2.json').read_text());mapping=json.loads((R/'drain8032-author-full-mapping-v2.json').read_text());manifest=json.loads((W/d['archive_manifest']['path']).read_text());archive=Path(d['archive_manifest']['path']).parent
assert len(mapping)==len(manifest['entries'])==84
for e in manifest['entries']:
 p=W/archive/e['stored_path'];assert h(p)==e['stored_sha256'];raw=gzip.decompress(p.read_bytes()) if e['encoding']=='gzip' else p.read_bytes();assert hashlib.sha256(raw).hexdigest()==e['raw_sha256'];assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==e['git_blob']
for e in plan['current_context']:assert h(W/e['path'])==e['sha256']
sys.path[:0]=[str(W/'scripts'),str(W/'docs/audit/scripts')]
import runner_cache as c,audit_packet_script_deps as a,build_citation_graph as g
N=d['notes'][0]['path'];P=d['runners'][0]['path'];J=d['runners'][1]['path'];cid=g.claim_id_from_path(W/N);body=(W/N).read_text();assert g.extract_runner(body,N)==P;assert g.helper_runner_paths_for_claim(cid,P)==a.helper_runner_paths_for_claim(cid,Path(P).stem)==[J]
assert not g.resolve_helper_runner_paths(P) and not a.transitive_helpers(Path(P).stem)
cites=sorted(p.relative_to(W).as_posix() for p in g.extract_citations(body,W/N));assert cites==dis['citations']
for e in dis['runners']:
 assert h(W/e['path'])==e['sha256'];assert list(c.declared_input_paths(W/e['path']))==[x['path'] for x in e['ordered_inputs']];assert c.declared_input_fingerprint(W/e['path'])==e['input_fingerprint'];assert c.declared_timeout_for(W/e['path'])==180
bind=lambda ps:[dict(path=p,sha256=h(W/p)) for p in sorted(set(ps))]
paths=[e['path'] for e in f]+[e['path'] for e in maps];tools=['scripts/runner_cache.py','scripts/audit_packet_script_deps.py','docs/audit/scripts/build_citation_graph.py','docs/audit/scripts/ledger_io.py','docs/audit/data/axiom_premise_nodes.json','docs/audit/data/doc_authority_registry.json'];skill='docs/ai_methodology/skills/review-loop';context={e['path'] for e in plan['current_context']}|set(cites)|{skill+'/SKILL.md',skill+'/scripts/review_receipt.py',skill+'/references/UNIT_RECEIPT.md'}
for n in ['unit-draft','source-handoff','cache-api','staged-freeze']:assert not (R/f'drain8032-author-{n}-v1.json').exists()
refs=[ref(R/n) for n in ['drain8032-author-handoff-v2.json','drain8032-author-prepared-v2.json','drain8032-prepared-v2-source-freeze.json','drain8032-author-full-mapping-v2.json','drain8032-author-input-resource-plan-v2.json','drain8032-author-discovery-v2.json','drain8032-registry-application-v1.json','drain8032-early-review-v2.json','drain8032-early-review-v1.json']]+[ref(Path(__file__).resolve())]
subprocess.run(['git','-C',str(W),'add','--',*paths],check=True)
assert set(git('diff','--cached','--name-only').splitlines())==set(paths) and not git('diff','--name-only')
tree=git('write-tree')
def save(n,x):
 p=R/f'drain8032-author-{n}-v1.json'
 with p.open('x') as o:json.dump(x,o,indent=2);o.write('\n')
 return p
for e in mapping:
 if e['original_path'] in [m['path'] for m in maps]:e['final_path']=e['original_path'];e['final_sha256']=h(W/e['original_path'])
sp=save('source-handoff',dict(original_dispositions=mapping,claims=json.loads((R/'drain8032-author-finding-dispositions-v2.json').read_text())['claims'],base=base,tree=tree,references=refs,full_proofs='Main, alternative and one-plaquette arguments are all inline in canonical note; no secondary autonomous proof note.',mathematical_closure=plan['mathematical_closure']))
ap=save('cache-api',dict(dis,actual_current_base=base,source_tree=tree,integrated_maps=bind(m['path'] for m in maps),actual_integrated_helpers=[J]))
history=[e['path'] for e in f if e['path'].startswith(str(archive)) and e['path'].endswith('.md')]
record=dict(schema_version=2,unit_id='PR8032',constituents=[dict(id='PR8032',head=d['original_head'],delta_base=d['original_merge_base'],dispositions=dict(ref(sp),json_pointer='/original_dispositions'))],source=dict(base=base,commit=base,tree=tree,paths=bind(paths),deleted_paths=[]),inputs=dict(runtime=bind([x['path'] for e in dis['runners'] for x in e['ordered_inputs']]+[P,J]),helpers=bind([J]),parents=bind(dis['parents']),context=bind(context),tooling=bind(tools)),reviewer=dict(session='/root/review_8032; actual cold/final confirmation pending',report=ref(rp),references=refs+[ref(sp),ref(ap)]),notes=[dict(path=N,claim_id=cid,declared_claim_id=re.search(r'^claim_id: (.+)$',body,re.M)[1],claim_type='bounded_theorem',primary_runner=P,helpers=[J],citations=cites,repository_dependencies=dis['parents'],dependency_rationale=plan['mathematical_closure'])],supporting_proofs=[],non_science_notes=[dict(path=p,rationale='Exact original historical source/review/control recovery; complete accepted current arguments are inline in canonical note. No historical audit/status or superseded normalization is current authority.',review_reference=ref(rp)) for p in history])
p=save('unit-draft',record);save('staged-freeze',dict(base=base,tree=tree,files=[dict(e,mode=oct((W/e['path']).stat().st_mode&0o777)) for e in record['source']['paths']],record=ref(p)));print(json.dumps(ref(p)))
