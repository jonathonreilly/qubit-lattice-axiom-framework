"""Future root-dispatched staging/schema2 builder. Never executes science or gates.
Requires explicit dispatch after preceding shared-map integration and base advance.
Evidence files are immutable ROOT artifacts; mutable checkout is source only.
"""
from pathlib import Path
import argparse,ast,gzip,hashlib,json,re,subprocess,sys
sys.dont_write_bytecode=True
assert __debug__, 'Do not run this guarded builder with Python optimization'
R=Path('/private/tmp/review-drain-20260915');W=R/'review-meta-slot'
ap=argparse.ArgumentParser();ap.add_argument('--expected-base',required=True);ap.add_argument('--stage-authorized',action='store_true',required=True);ap.add_argument('--version',required=True);args=ap.parse_args()
assert args.stage_authorized and re.fullmatch('[0-9a-f]{40}',args.expected_base) and re.fullmatch('v[1-9][0-9]*',args.version)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ref=lambda p:dict(path=str(p),sha256=sha(p))
bind=lambda ps:[dict(path=p,sha256=sha(W/p)) for p in sorted(set(ps))]
git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
prep=R/'drain8163-author-prepared-v2.json';assert sha(prep)=='c256784ae1b7de82957f535d1e769b75076c29a282a6edd491d9b2f80cd33163';d=json.loads(prep.read_text())
freeze=R/'drain8163-owned-prepared-v2-freeze.json';assert sha(freeze)=='c157a36ed874fe516964a591051efda6199b0364dd415742bd7e0b041a526f55';frozen=json.loads(freeze.read_text())['files'];assert len(frozen)==120
confirmation=R/'drain8163-affected-fix-confirmation-v2.json';assert sha(confirmation)=='76a1f839bdb67c3ef058abddb9d9ba167017c3bcb9e565415899c3ff526a969f'
review=R/'drain8163-original-review.json';assert sha(review)==d['original_review_sha256'];original=json.loads(review.read_text())
plan=R/'drain8163-author-input-resource-plans-v2.json';assert sha(plan)=='1d1ad5a288b3c8d5052055aded72be5bed105439eb1e573f7c8696099e7933e3';plans=json.loads(plan.read_text())
capture=R/'drain8163-capture-plan-v1.json';assert sha(capture)=='923ef78b20ef7083a9381861fe1901ec70b7fd5b03719daa2e964fb45ad0635c'
owner=json.loads((R/'review-meta-slot.json').read_text());assert owner['owner']=='PR8163-author' and Path(owner['path']).resolve()==W.resolve()
assert git('rev-parse','HEAD')==args.expected_base==git('rev-parse','origin/main')
assert not git('diff','--name-only','HEAD') and not git('diff','--cached','--name-only')
assert set(git('ls-files','--others','--exclude-standard').splitlines())=={e['path'] for e in frozen}
for e in frozen:
 p=W/e['path'];assert p.is_file() and not p.is_symlink() and sha(p)==e['sha256'],e['path']
 assert ('100755' if p.stat().st_mode&0o111 else '100644')==e['mode']
for row in plans:
 for e in row['ordered_inputs']:assert sha(W/e['path'])==e['sha256'],'Changed parent/input requires original reviewer: '+e['path']
# Actual cache API consumes AUDIT_INPUT_PATHS, not the historical FILES spelling.
# This catches the known prepared-v2 omission before any registry or index mutation.
for row in plans:
 t=ast.parse((W/row['runner']).read_text())
 declarations={n.targets[0].id:n.value for n in t.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name)}
 assert 'AUDIT_INPUT_PATHS' in declarations, 'Prepared-v2 defect: missing literal AUDIT_INPUT_PATHS; source correction and original-reviewer confirmation required before staging'
 assert ast.literal_eval(declarations['AUDIT_INPUT_PATHS'])==[e['path'] for e in row['ordered_inputs']]
authority_file=R/'drain8163-authority-bindings.json'
assert sha(authority_file)=='4358fcdf0f4bb36341f0dc17ea76a904a485fd323fdfaabad2818b6bf674cf54'
authorities=json.loads(authority_file.read_text())
for e in authorities:assert sha(W/e['path'])==e['sha256'], 'Authority changed; original reviewer confirmation required: '+e['path']
files={k:R/f'drain8163-author-{k}-{args.version}.json' for k in ['unit-draft','source-handoff','cache-api']};assert all(not p.exists() for p in files.values())
archive=Path(d['archive_manifest']['path']).parent;assert sha(W/d['archive_manifest']['path'])==d['archive_manifest']['sha256'];m=json.loads((W/d['archive_manifest']['path']).read_text())
orig={e['path']:e for e in original['path_dispositions']};assert len(orig)==len(m['entries'])==165;assert {e['original_path'] for e in m['entries']}==set(orig)
mapfile=R/'drain8163-author-full-mapping-v2.json';assert sha(mapfile)=='9e645be203eabdf4430337a579852da5e015f381bef9a2ea177fe3b560bcc85e';mapped={e['original_path']:e for e in json.loads(mapfile.read_text())};assert set(mapped)==set(orig);disps=[]
for e in m['entries']:
 o=orig[e['original_path']];assert e['original_mode']==o['mode'] and e['git_blob']==o['blob'] and e['raw_sha256']==o['sha256']
 stored=(archive/e['stored_path']).as_posix();assert sha(W/stored)==e['stored_sha256'];payload=(W/stored).read_bytes();raw=gzip.decompress(payload) if e['encoding']=='gzip' else payload
 assert hashlib.sha256(raw).hexdigest()==e['raw_sha256'];assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==e['git_blob']
 row=mapped[e['original_path']];canonical=row['final_path'];target=canonical or stored
 if canonical:assert sha(W/canonical)==row['final_sha256']
 disps.append(dict(original_path=e['original_path'],original_mode=e['original_mode'],original_blob=e['git_blob'],original_sha256=e['raw_sha256'],final_path=target,final_sha256=sha(W/target),recovery=m['revision']+':'+e['original_path']+'; exact stored payload '+stored,recovery_encoding=e['encoding'],disposition=row['disposition'],canonical_path=canonical))
registry=['scripts/audit_packet_script_deps.py','docs/audit/scripts/build_citation_graph.py'];replacements={};preservation={};helper_plan=d['requested_explicit_packet_helpers'];assert len(helper_plan)==1 and len(next(iter(helper_plan.values())))==3

def mapping(text):
 return ast.literal_eval(next(n.value for n in ast.parse(text).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='EXPLICIT_PACKET_HELPER_RUNNER_PATHS' for t in n.targets)))
for p in registry:
 text=(W/p).read_text();old=mapping(text);assert not set(old)&set(helper_plan),'Owner already registered; inspect rather than overwrite'
 marker='EXPLICIT_PACKET_HELPER_RUNNER_PATHS = {';assert text.count(marker)==1
 new=text.replace(marker,marker+'\n'+''.join('    '+repr(k)+': '+repr(v)+',\n' for k,v in helper_plan.items()),1);assert mapping(new)==dict(old,**helper_plan);replacements[p]=new
 preservation[p]=dict(before_sha256=sha(W/p),existing_entries_preserved=len(old),added=helper_plan)
# All original/source/owner/base guards precede any mutation. Preserve current-base maps.
for p,new in replacements.items():(W/p).write_text(new)
sys.path[:0]=[str(W/'scripts'),str(W/'docs/audit/scripts')]
import runner_cache as c,audit_packet_script_deps as a,build_citation_graph as g
# Imports are metadata tooling only; no scientific runner module is imported.
notes=[];allcites=set();allparents=set();helpers=set();runtime=set();apis=[]
parent_paths={Path(x).stem.lower():x for x in d['notes']}
for x in plans[-3]['ordered_inputs']:parent_paths[Path(x['path']).stem.lower()]=x['path']
# Explicitly derive all declared-input candidates, including both landed8162 parents.
for row in plans:
 for x in row['ordered_inputs']:parent_paths[Path(x['path']).stem.lower()]=x['path']
for note in d['notes']:
 body=(W/note).read_text();cid=g.claim_id_from_path(W/note);primary=re.search(r'^runner: (.+)$',body,re.M)[1];hp=list(g.helper_runner_paths_for_claim(cid,primary));packet=list(a.helper_runner_paths_for_claim(cid,Path(primary).stem));expected=helper_plan.get(cid,[]);assert set(hp)==set(packet)==set(expected)
 deps=[parent_paths[x] for x in json.loads(re.search(r'^upstream_dependencies: (.+)$',body,re.M)[1])]
 cites=sorted(x.relative_to(W).as_posix() for x in g.extract_citations(body,W/note));assert set(deps)<=set(cites)
 assert primary in d['runners'];allcites.update(cites);allparents.update(deps);helpers.update(hp)
 rationale='Self-contained supplied massive Wilson determinant and curl argument.' if note==d['notes'][0] else ('Temporal Wilson definitions and open normalization only; m>0 algebra does not import heavy-curl hypothesis.' if note==d['notes'][1] else 'Exact linked temporal/model-match and landed8162 transfer/state parents; supplied fixed-graph scope.')
 notes.append(dict(path=note,claim_id=cid,declared_claim_id=re.search(r'^claim_id: (.+)$',body,re.M)[1],claim_type='bounded_theorem',primary_runner=primary,helpers=hp,citations=cites,repository_dependencies=deps,dependency_rationale=rationale))
for row in plans:
 p=row['runner'];tree=ast.parse((W/p).read_text());compile(tree,p,'exec');ins=list(c.declared_input_paths(W/p));assert ins==[x['path'] for x in row['ordered_inputs']];assert c.declared_timeout_for(W/p)==180;assert not a.transitive_helpers(Path(p).stem)
 pins=ast.literal_eval(next(n.value for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='EXPECTED_INPUT_SHA256'));assert pins=={x:sha(W/x) for x in ins};runtime.update(ins+[p])
 apis.append(dict(runner=p,timeout=180,declared_inputs=ins,runtime_closure=bind(ins+[p]),declared_input_fingerprint=c.declared_input_fingerprint(W/p),cache_status=c.cache_status(p),packet_transitive_helpers=[]))
subprocess.run(['git','-C',str(W),'add','--',*[e['path'] for e in frozen],*registry],check=True)
subprocess.run(['git','-C',str(W),'diff','--cached','--check'],check=True)
paths=git('diff','--cached','--name-only').splitlines();assert set(paths)=={e['path'] for e in frozen}|set(registry);assert not git('diff','--name-only');tree=git('write-tree')
files['cache-api'].write_text(json.dumps(apis,indent=2)+'\n')
refs=[ref(x) for x in [prep,freeze,review,confirmation,plan,capture,mapfile,authority_file,files['cache-api']]]
claim_dispositions=[dict(note=d['notes'][0],disposition='Complete supplied-model proof preserved: temporal inverse/log expansion, spin and closed-time gains, integer physical-area filling, physical Lp and Schur estimates, exact leading rectangle and heavy-mass improvement. Uniform physical curl bounds under heavy mass; no phase or native-law conclusion.'),dict(note=d['notes'][1],disposition='Complete m>0 model match preserved: positive recurrence, actual elimination determinant prefactor, complementary minors and chronological adjoint, filled-boundary Fock amplitude, fixed-graph Hamiltonian limit and conjugate-pair gauge covariance. No thermal or global-ground-state identification.'),dict(note=d['notes'][2],disposition='Complete exact finite gauge join and fixed-graph state proof preserved: calibrated kernel, endpoint factors and normalized measure, contraction shift, Fourier-core consistency, all-mode compactness, physical projection/spectral/heat limits and shift-restored boundary amplitude. No spatial-volume phase conclusion.'),dict(history='All165 original payloads',disposition='All three complete working derivations superseded by full final proofs; two initial failures, all mutant sources/streams and23 final fault outcomes preserved exactly, without current evidence restamping. No unique substantive result deferred.'),dict(open_extensions=['periodic winding','gapless matter','fixed-payload photon phase','native action/time selection','global-ground-state sector/overlap selection','spatial-volume state control'],disposition='Remain open extensions, not negative certifications or omitted proved results.')]
h=dict(status='AUTHOR HANDOFF ONLY; ORIGINAL REVIEWER STAGED COLD CONFIRMATION PENDING',author='/root/resume_8078_method',base=args.expected_base,tree=tree,original_dispositions=disps,claim_dispositions=claim_dispositions,registry_preservation=preservation,execution_plan=ref(capture),references=refs)
files['source-handoff'].write_text(json.dumps(h,indent=2)+'\n')
skill='docs/ai_methodology/skills/review-loop';context=allcites|set(d['notes'])|{d['archive_manifest']['path'],skill+'/SKILL.md',skill+'/PREFLIGHT.md',skill+'/scripts/review_receipt.py',skill+'/scripts/review_workspace.py'}|{str(p.relative_to(W)) for p in (W/skill/'references').glob('*.md')}
context.update(e['path'] for e in authorities)
tooling=['docs/audit/scripts/build_citation_graph.py','docs/audit/scripts/static_pipeline_checkpoint.py','scripts/runner_cache.py','scripts/audit_packet_script_deps.py','docs/audit/scripts/ledger_io.py','docs/audit/data/axiom_premise_nodes.json','docs/audit/data/doc_authority_registry.json']
history=[e['path'] for e in frozen if e['path'].startswith(archive.as_posix()+'/') and e['path'].endswith('.md')]
record=dict(schema_version=2,unit_id='PR8163',constituents=[dict(id='PR8163',head=original['original_head'],delta_base=original['original_delta_base'],dispositions=dict(ref(files['source-handoff']),json_pointer='/original_dispositions'))],source=dict(base=args.expected_base,commit=args.expected_base,tree=tree,paths=bind(paths),deleted_paths=[]),inputs=dict(runtime=bind(runtime),helpers=bind(helpers),parents=bind(allparents),context=bind(context),tooling=bind(tooling)),reviewer=dict(session='/root/review_8161; staged cold/final confirmation pending',report=ref(review),references=refs+[ref(files['source-handoff'])]),notes=notes,supporting_proofs=[],non_science_notes=[dict(path=p,rationale='Exact superseded working derivation or numerical/recovery history only; current full scientific argument preserved in canonical owner notes, no autonomous historical claim adopted.',review_reference=ref(confirmation)) for p in history])
files['unit-draft'].write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(ref(files['unit-draft'])));print(tree)
