from pathlib import Path
import ast,difflib,hashlib,json,os,shutil,stat,subprocess,sys
sys.dont_write_bytecode=True
R=Path('/private/tmp/review-drain-20260915');W=R/'author-draft-slot';O=R/'drain8174-original'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ref=lambda p:dict(path=str(p),sha256=sha(p))
def out(name,data):
 p=R/name
 with p.open('x') as f:json.dump(data,f,indent=2);f.write('\n')
 return p
d=json.loads((R/'drain8174-author-prepared-v1.json').read_text());paths=d['source_paths'];note=d['notes'][0]['path'];runner=d['runners'][0]['path'];np=W/note;rp=W/runner
for version in ['v1']:
 snap=R/f'drain8174-prepared-{version}-source';assert not snap.exists()
 for p in paths:
  q=snap/p;q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(W/p,q)
 out(f'drain8174-prepared-{version}-source-freeze.json',dict(files=[dict(path=p,sha256=sha(W/p),mode=oct(stat.S_IMODE((W/p).stat().st_mode)),immutable_copy=str(snap/p)) for p in sorted(paths)]))
s=np.read_text().replace('actual_current_surface_status: proposed_retained','actual_current_surface_status: bounded-support').replace('source_of_blocker_text: source_note','source_of_blocker_text: review_loop').replace('bare_retained_allowed: false','bare_retained_allowed: false\nclaim_type_reason: "Conditional complete coupling/tree proofs and four rational sufficient certificates; deferred negative claims are not premises"').replace('in the closed forms of the front matter','in the closed forms of T1').replace('Independent affected-source review and bounded evidence capture; sharper counting remains research','Independent affected-source review and bounded evidence capture; consumer is a future sharper supplied-process stability bound')
old=np.read_text();np.write_text(s)
r=rp.read_text().replace(hashlib.sha256(old.encode()).hexdigest(),sha(np)).replace('original1200','original 1200').replace('the runner scans\nexact arithmetic bodies are preserved; no float-scan or prose-count PASS is used.','the exact arithmetic bodies are preserved; no float-scan or prose-count PASS is used.').replace('the axioms memo carries the four sentences quoted under Premises','the axioms memo carries the four framework sentences used by the conditional model').replace("the route's ceiling on (p, 1, 2) lies between 4150 and 4165",'the deferred necessary comparison is bracketed by these points; no optimal integer is asserted')
rp.write_text(r);compile(r,runner,'exec')
# Metadata-only actual repository APIs; never import the scientific runner.
sys.path[:0]=[str(W/'scripts'),str(W/'docs/audit/scripts')]
import runner_cache as c,audit_packet_script_deps as a,build_citation_graph as g
cid=g.claim_id_from_path(np);assert g.extract_runner(s,note)==runner
helpers=list(g.helper_runner_paths_for_claim(cid,runner));packet=list(a.helper_runner_paths_for_claim(cid,Path(runner).stem));transitive=list(a.transitive_helpers(Path(runner).stem));resolved=list(g.resolve_helper_runner_paths(runner));assert helpers==packet==transitive==resolved==[]
ins=list(c.declared_input_paths(rp));decl={n.targets[0].id:n.value for n in ast.parse(r).body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name)}
assert len(ins)==4 and ast.literal_eval(decl['EXPECTED_INPUT_SHA256'])=={p:sha(W/p) for p in ins}
cites=sorted(p.relative_to(W).as_posix() for p in g.extract_citations(s,np));parents=ins[1:];assert all(p in cites for p in parents)
discovery=dict(status='Actual metadata APIs only; no science execution',claim_id=cid,note=note,runner=runner,helpers=helpers,packet_helpers=packet,transitive_helpers=transitive,resolved_helpers=resolved,citations=cites,parents=parents,ordered_inputs=[dict(path=p,sha256=sha(W/p)) for p in ins],input_fingerprint=c.declared_input_fingerprint(rp),timeout=c.declared_timeout_for(rp),memory_mb=768,registry_edits_needed=False)
out('drain8174-author-discovery-v2.json',discovery)
mutations=ast.literal_eval(decl['MUTATION_GATE']);assert len(mutations)==11
plan=dict(runner=dict(path=runner,sha256=sha(rp)),ordered_inputs=discovery['ordered_inputs'],mathematical_parents=[dict(path=p,sha256=sha(W/p),role='Framework vocabulary' if p==ins[1] else 'Product conditional and six-axis model' if p==ins[2] else 'Single-noise sufficient certificate comparison and complete reproduced pole transport') for p in parents],mathematical_closure='Complete supplied-domain coupling, finite ancestor-cone localization, extended cluster/tree refinement and transport, exact lifted slot count, four preserved rational super-solutions, compact Feller Cesaro argument and optional extreme stationary-law decomposition. No unlanded sibling, simulation, historical output or deferred negative proof is a premise.',runtime_read_set='Four literal AUDIT_INPUT_PATHS plus own source for identity; no external helper, simulation file or historical payload read. Sympy and Python standard library are dependencies.',timeout_sec=900,proposed_external_process_tree_limit_bytes=768*1024*1024,source_basis='Original 900-second declared cap retained. Original all1024 depth2 configurations, depth3 configurations with one through four noise sites, random.seed(30) and1200 cones depths3..8 unchanged. Original 66103 lifted-tree enumeration through4edges and all four rational certificates unchanged. Additional symbolic three derivatives/factorization and endpoint denominator are bounded small expressions. 768MiB conservative proposed import/tree-enumeration headroom, unmeasured; original historical cache1.54seconds is not a fresh performance measurement. Preserve any failure; no automatic retry or cap increase.',json_output='logs/runner-cache/'+rp.stem+'.json',mutation_json_pattern='logs/runner-cache/'+rp.stem+'--<mutation>.json',stdout='logs/runner-cache/'+rp.stem+'.txt',checks_source_derived_not_executed=d['checks'],mutation_names=mutations,mutation_status='Nine original mathematical mutations retained, two corrected-domain/endpoint mutations added. Two original prose-only mutations preserved only in exact historical runner. No outcomes asserted.',primary_executions=0,mutation_executions=0,simulation_executions=0)
out('drain8174-author-input-resource-plan-v2.json',plan)
# Versioned exact changes and mappings; prior prepared files stay immutable.
oldnote=next((O/'head/docs').glob('*.md'));oldrun=next((O/'head/scripts').glob('*.py'))
patch=''.join(difflib.unified_diff(oldnote.read_text().splitlines(True),s.splitlines(True),fromfile=str(oldnote.relative_to(O/'head')),tofile=note))+''.join(difflib.unified_diff(oldrun.read_text().splitlines(True),r.splitlines(True),fromfile=str(oldrun.relative_to(O/'head')),tofile=runner))
with (R/'drain8174-author-correction-v2.diff').open('x') as f:f.write(patch)
mp=json.loads((R/'drain8174-author-full-mapping-v1.json').read_text())
for e in mp:
 if e['final_path']:e['final_sha256']=sha(W/e['final_path'])
out('drain8174-author-full-mapping-v2.json',mp)
claims=[dict(claim='Coupling and deviations',disposition='narrowed',reason='p>=q>0,r>0; explicit factorization and all derivatives; exact unrestricted-domain counterexample retained',final_path=note),dict(claim='Extended explanation tree',disposition='accepted with complete proof expansion',reason='Original full construction plus finite ancestor-cone localization and full pole-transport identity; exact core implementation unchanged',final_path=note),dict(claim='Lifted bound and four certificates',disposition='accepted',reason='Exact four rational certificates and all fixtures unchanged; full slot and invariant-law proofs',final_path=note),dict(claim='Positive fixed-point parametrization',disposition='narrowed',reason='1<=v<3/2 gives positive denominator; scalar maxima preserved',final_path=note),dict(claim='Full-domain strict endpoint and necessary route-bound proof',disposition='deferred science',reason='Valid corrected proof remains complete and readable; formal negative certification deferred separately from mathematical validity',recovery=d['deferred_science']['path']),dict(claim='Actual threshold, whole-gap attribution, exhaustive optimality, overlap impossibility',disposition='deferred or withdrawn as unsupported',reason='Finite simulation/scan cannot prove these; unique proposals and exact failures preserved; branch retention required',recovery=d['deferred_science']['path'])]
report=json.loads((R/'drain8174-review-original.json').read_text())
out('drain8174-author-finding-dispositions-v2.json',dict(findings=[dict(id=e['id'],original_finding=e['finding'],correction=e['fix'],status='Author correction prepared; independent affected confirmation pending') for e in report['findings']],claims=claims,original_head=d['original_head'],branch_retention_required=True))
snap=R/'drain8174-prepared-v2-source';assert not snap.exists()
for p in paths:
 q=snap/p;q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(W/p,q)
freeze=out('drain8174-prepared-v2-source-freeze.json',dict(files=[dict(path=p,sha256=sha(W/p),mode=oct(stat.S_IMODE((W/p).stat().st_mode)),immutable_copy=str(snap/p)) for p in sorted(paths)]))
d['notes'][0]['sha256']=sha(np);d['runners'][0]['sha256']=sha(rp);d['source_freeze']=ref(freeze);d['status']='Prepared v2 source; complete original-review reconciliation; independent affected review pending';d['metadata_corrections']='Enum hygiene and stale phrasing corrected from v1; both snapshots retained'
prepared=out('drain8174-author-prepared-v2.json',d)
git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
assert not git('diff','--name-only','HEAD') and set(git('ls-files','--others','--exclude-standard').splitlines())==set(paths)
refs=[prepared,freeze,R/'drain8174-author-full-mapping-v2.json',R/'drain8174-author-correction-v2.diff',R/'drain8174-author-discovery-v2.json',R/'drain8174-author-input-resource-plan-v2.json',R/'drain8174-author-finding-dispositions-v2.json',R/'drain8174-author-preservation-v1.json']
out('drain8174-author-handoff-v2.json',dict(status='Source-only handoff to root for original same-session affected review; no PASS or execution',references=[ref(p) for p in refs],source_count=len(paths),original_recovery_count=25,inputs=4,helpers=0,registry_edits_needed=False,current_main_loss_guard='All seven existing conflict paths unchanged; tracked/index clean',checks='Syntax compiled in memory, actual metadata/input/helper APIs only, exact raw Git blob/hash preservation and computational AST comparisons; no preflight or science',original_reviewer='/root/review_8174',branch_retention_required=True))
print(json.dumps([ref(p) for p in refs]+[ref(R/'drain8174-author-handoff-v2.json')],indent=2))
