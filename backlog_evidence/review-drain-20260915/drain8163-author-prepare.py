import ast,copy,difflib,gzip,hashlib,json,re
from pathlib import Path
R=Path('/private/tmp/review-drain-20260915'); W=R/'review-meta-slot'; P=R/'drain8163-originals/.claude/science/physics-loops/toe-temporal-fermion-resummation-20260916'
def sha(b):return hashlib.sha256(b).hexdigest()
def pin(p):return {'path':p,'sha256':sha((W/p).read_bytes())}
notes=['TEMPORAL_WILSON_RESUMMATION_PHYSICAL_CURL_BOUNDED_THEOREM_NOTE_2026-09-16.md','OPEN_BOUNDARY_WILSON_FOCK_MODEL_MATCH_BOUNDED_THEOREM_NOTE_2026-09-16.md','OPEN_WILSON_GAUGE_MATTER_FIXED_GRAPH_STATE_JOIN_BOUNDED_THEOREM_NOTE_2026-09-16.md']
orig=['BLOCK02_UNIFORM_TEMPORAL_RESUMMATION_AND_CURL_RESPONSE.md','BLOCK03_EXACT_OPEN_BOUNDARY_FERMION_MODEL_MATCH.md','BLOCK04_ACTUAL_GAUGE_MATTER_TRANSFER_AND_STATE_JOIN.md']
runners=['temporal_wilson_resummation_check_2026_09_16','temporal_wilson_physical_curl_hessian_check_2026_09_16','open_boundary_wilson_hamiltonian_check_2026_09_16','open_wilson_dynamical_gauge_join_check_2026_09_16','temporal_wilson_integer_local_filling_check_2026_09_16','temporal_wilson_third_curl_variation_check_2026_09_16']
oldrun=['block01_temporal_resummation_check','block02_physical_curl_hessian_check','block03_open_boundary_hamiltonian_check','block04_dynamical_gauge_join_check','block05_integer_local_filling_check','block06_third_curl_variation_check']
parents=['CLOCK_VARIANCE_CALIBRATED_JOINT_ROTOR_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-16.md','CLOCK_ALL_MODE_COERCIVITY_FINITE_GRAPH_STATES_BOUNDED_THEOREM_NOTE_2026-09-16.md']
owners=[0,0,1,2,0,0]; prim=[0,2,3]
scopes=['Supplied paired massive Wilson determinant on a free spatial cube and open time interval; heavy-mass physical curl bounds uniform in time step and volume.','Supplied finite spatial Wilson model; exact open-boundary Fock amplitude and fixed-graph continuous-time match.','Supplied paired Wilson matter and variance-calibrated clock gauge transfer; joint regulator and physical-state convergence on a fixed finite graph.']
intros=['This is a conditional result for a supplied paired massive Wilson determinant on a free spatial cube times an open time interval. It addresses temporal-run resummation in the compact determinant/current context. It establishes neither a compact-gauge phase nor a derived native matter law.','This is a conditional normalization and boundary-condition join for the supplied Wilson operator. Wilson transfer matrices, dimensional reduction and exterior-power factorization are established machinery. The purpose is to identify exactly which fermionic boundary amplitude the physical curl estimate controls. No audit or compact phase is claimed.','This conditional result joins the exact open-boundary Wilson determinant to a positive compact gauge transfer. It uses the linked canonical model-match, variance-calibrated transfer and all-mode state-limit arguments as supplied mathematical parents. Their landing establishes source availability, not an audit verdict or a phase theorem.']
diffs=[]; preservation=[]
for j,name in enumerate(notes):
 old=(P/'notes'/orig[j]).read_text();lines=old.splitlines(keepends=True); title=lines[0]; body=''.join(lines[4:]) if lines[3]=='\n' else None
 # Replace only original first prose paragraph; preserve every subsequent proof line except explicit prose cross-reference labels.
 body=old[old.index('\n\n',old.index('\n\n')+2)+2:]
 out=[]
 for line in body.splitlines(keepends=True):
  if not line.startswith('    '):
   line=line.replace('[Block03 model-match proposal](BLOCK03_EXACT_OPEN_BOUNDARY_FERMION_MODEL_MATCH.md)',f'`{notes[1]}` (context only)')
   line=line.replace('[Block04 dynamical gauge proposal](BLOCK04_ACTUAL_GAUGE_MATTER_TRANSFER_AND_STATE_JOIN.md)',f'`{notes[2]}` (context only)')
   line=line.replace('That proposal remains author-checked','That companion result remains conditional')
   line=line.replace('frozen provisional PR8162 proofs','supplied variance-calibrated transfer and all-mode state proofs')
   line=line.replace('prior PR8162 Block02 sections6-8 and Block03','the variance-calibrated transfer proof sections6-8 and the all-mode state proof')
   line=line.replace('prior Block02','the variance-calibrated transfer proof').replace('prior Block03','the all-mode state proof')
   line=line.replace('Block02','the temporal-resummation note').replace('Block03','the model-match note').replace('Block04','the gauge/state-join note')
   line=line.replace('bounded campaign outcome','bounded result')
   line=line.replace('particular the temporal-resummation note bound','particular temporal-resummation bound')
   line=line.replace('the previous campaign','the earlier supplied spatial construction')
   if line.startswith('the temporal-resummation note'): line='The'+line[3:]
   if line.startswith('the model-match note'): line='The'+line[3:]
  out.append(line)
 body=''.join(out)
 deps=[] if j<2 else [notes[0],notes[1],*parents]
 header='---\nclaim_id: '+name[:-3].lower()+'\nclaim_type: bounded_theorem\nrunner: scripts/'+runners[prim[j]]+'.py\nclaim_scope: '+json.dumps(scopes[j])+'\nupstream_dependencies: '+json.dumps([x[:-3].lower() for x in deps])+'\n---\n\n'
 status='**Type:** bounded_theorem\n\n```yaml\nactual_current_surface_status: conditional-support\nconditional_surface_status: conditional-support\ntrace_class: upstream_support\nreachability_to_target: supports\naudit_required_before_effective_retained: true\nbare_retained_allowed: false\nhypothetical_axiom_status: null\nadmitted_observation_status: null\n```\n\n'
 deptext='' if not deps else 'Load-bearing supplied-model parents: '+', '.join(f'[{x}]({x})' for x in deps)+'.\n\n'
 boundary='\n\n## Evidence and execution boundary\n\n'
 boundary+='Primary runner: `scripts/'+runners[prim[j]]+'.py`.\n\n'
 if j==0:boundary+='Companion diagnostics: '+', '.join('`scripts/'+runners[k]+'.py`' for k in [1,4,5])+'. They are separate completed diagnostic families with separate captures; none substitutes for the full proof above.\n\n'
 boundary+='All original arithmetic, assertions, finite domains, seeds and tolerances are preserved. Each program retains its 180-second limit; memory limits and sole sequential captures are coordinator-owned and must be frozen before execution. `TOTAL: PASS=1 FAIL=0` means one complete diagnostic family finished all its original assertions, not one assertion or exhaustive physical coverage. Source and ordered owner/parent notes are read and hash-bound. JSON diagnostics are written under `logs/runner-cache/`.\n\n'
 boundary+='The [historical recovery packet](work_history/repo/review_feedback/pr8163-evidence/README.md) preserves all original paths, modes, blobs, complete working derivations, two initial failures and 23 final formula-fault outcomes. Those historical runs are not current-source execution evidence.\n\n'
 boundary+='## No-Go Discipline Gate\n\n**N1 — Actual alternatives.** The preserved finite diagnostics and 23 specified formula faults test the stated algebra. Five future research routes are open alternatives, not completed attacks or exhaustive exclusions.\n\n**N2 — Shared scope.** Results use the supplied massive Wilson/open-boundary model and its explicit finite-graph or physical-curl quantifiers; no independent-wall theorem is asserted.\n\n**N3 — Inputs.** Model parameters, external time, gauge kernel, CAR representation and endpoint state are supplied. No framework premise selects them.\n\n**N4 — Failed attempts.** The slow refinement failed its original factor-three target, and an initially equivalent orientation mutation survived; both failures and their exact subsequent source corrections remain preserved.\n\n**N5 — Resolution.** Completed finite matrices, integer cycles or sampled directions support the corresponding algebra. They do not exhaust all graphs, native laws or physical spectra.\n\n**N6 — Remaining routes.** Periodic winding, gapless matter, thermal identification, global ground-state selection and infinite-volume phase control remain open.\n\n**N7 — Strongest boundary.** Volume-uniform heavy physical-curl estimates differ from fixed-graph state limits; an open amplitude is not a thermal trace or a global ground-state selection.\n\n**N8 — Reopening.** New model matching, sector/overlap proofs or spatial-volume controls could resolve those extensions; the current result does not exclude them.\n'
 text=header+title+'\n'+status+intros[j]+'\n\n'+deptext+body.rstrip()+boundary
 (W/'docs'/name).write_text(text)
 oldmath=[x for x in old.splitlines() if x.startswith('    ')];newmath=[x for x in text.splitlines() if x.startswith('    ')]
 assert oldmath==newmath
 preservation.append({'original':'notes/'+orig[j],'canonical':'docs/'+name,'indented_formula_lines':len(oldmath),'exact_formula_line_sequence_sha256':sha('\n'.join(oldmath).encode()),'preserved':True})
 diffs.extend(difflib.unified_diff(old.splitlines(True),text.splitlines(True),fromfile='original/notes/'+orig[j],tofile='docs/'+name))
plans=[]
certs=[
 ['finite Wilson matrices, temporal-run inverses and rectangle traces','two fixed free spatial shapes and open temporal boundaries','Clifford sandwich and gauge conjugation controls; no physical spectrum','closed-time sums and leading rectangle continuum diagnostic','finite diagnostics only; general uniform bounds use the supplied-model proof'],
 ['analytic finite-matrix Hessians and determinant differences','fixed three-slice spatial box, with shrinking duration as delta decreases','gauge null directions and physical-metric quotient spectrum','three time spacings and five heavy-mass bound evaluations','no all-direction empirical or infinite-volume state test'],
 ['full time-Dirac determinants, Schur and complementary minors','noncommuting two-site external histories','70-state CAR sector and exterior-power comparison','five time resolutions with original ODE tolerances','fixed-graph boundary amplitude only; no thermal or global ground-state identification'],
 ['27 three-slice clock histories versus an independently assembled transfer','one spatial edge; no magnetic plaquette or propagating photon','1296-dimensional physical invariant sector with exact electric-charge energy','three joint-refinement paths and arbitrary-vector generator controls','finite-graph diagnostics only; no volume-uniform phase or global ground-state selection'],
 ['exact integer boundaries plus physical curl and image-phase checks','120 sampled closed walks with visited-box support and translations','all six spatial contraction orders; no physical spectral computation','three physical time spacings and preserved failed-orientation history','finite samples challenge orientations; general chain homotopy is proved in the note'],
 ['analytic third variations versus determinant finite differences','fixed physical duration 0.3 and three time resolutions','sampled physical curl directions and pure-gauge controls','original Richardson comparison and sufficient general bound','sampled directions only; no exhaustive all-direction numerical proof']]
for k,stem in enumerate(runners):
 old=(P/'evidence'/(oldrun[k]+'.py')).read_text(); owner=owners[k]
 inputs=['docs/'+notes[owner]]
 if owner==2:inputs+=['docs/'+notes[0],'docs/'+notes[1]]+['docs/'+x for x in parents]
 hashes={x:sha((W/x).read_bytes()) for x in inputs}
 src=old.replace('AUDIT_INPUT_FILES=[]','AUDIT_INPUT_FILES='+repr(inputs)+'\nAUDIT_MEMORY_MB=768\nEXPECTED_INPUT_SHA256='+repr(hashes),1)
 # Only replace the final report emitter; the argument dict expressions are unchanged.
 target="    print(json.dumps({'source_sha256':"
 assert src.count(target)==1
 src=src.replace(target,"    _emit({'source_sha256':",1)
 assert src.count("'seconds':time.time()-start},indent=2))")==1
 src=src.replace("'seconds':time.time()-start},indent=2))","'seconds':time.time()-start})",1)
 src=src.replace("if __name__=='__main__':run()", "if __name__=='__main__':\n    _check_inputs()\n    run()")
 extra='\n\ndef _check_inputs():\n    root = Path(__file__).resolve().parents[1]\n    for name in AUDIT_INPUT_FILES:\n        actual = hashlib.sha256((root / name).read_bytes()).hexdigest()\n        if actual != EXPECTED_INPUT_SHA256[name]:\n            raise RuntimeError("input identity mismatch: " + name)\n\ndef _emit(report):\n    report["input_sha256"] = dict(EXPECTED_INPUT_SHA256)\n    report["completed_diagnostic_families"] = 1\n    output = Path(__file__).resolve().parents[1] / "logs" / "runner-cache" / (Path(__file__).stem + ".json")\n    output.parent.mkdir(parents=True, exist_ok=True)\n    output.write_text(json.dumps(report, indent=2) + "\\n")\n    print(json.dumps(report, indent=2))\n    print("TOTAL: PASS=1 FAIL=0")\n'
 for label,detail in zip(['per_element','per_site','per_mode','per_block','lattice_wide'],certs[k]):extra+='    print('+repr(label+': '+detail+'.')+')\n'
 src=src.replace("if __name__=='__main__':",extra+"\nif __name__=='__main__':")
 out=W/'scripts'/(stem+'.py');out.write_text(src);out.chmod(0o755)
 # Independent AST preservation: every original function except run must be exact; run differs only in its final report call wrapper.
 a=ast.parse(old);b=ast.parse(src);af={n.name:n for n in a.body if isinstance(n,ast.FunctionDef)};bf={n.name:n for n in b.body if isinstance(n,ast.FunctionDef)}
 for name,node in af.items():
  expected=copy.deepcopy(node);actual=copy.deepcopy(bf[name])
  if name=='run':
   assert isinstance(expected.body[-1],ast.Expr) and isinstance(actual.body[-1],ast.Expr)
   expected.body[-1].value=ast.Call(func=ast.Name(id='_emit',ctx=ast.Load()),args=[expected.body[-1].value.args[0].args[0]],keywords=[])
  assert ast.dump(expected,include_attributes=False)==ast.dump(actual,include_attributes=False),name
 preservation.append({'original':'evidence/'+oldrun[k]+'.py','canonical':'scripts/'+stem+'.py','all_original_function_ASTs_preserved':True,'exception':'run final print(json.dumps(report)) wrapper replaced by _emit(the identical report expression)','original_assert_count':sum(isinstance(n,ast.Assert) for n in ast.walk(a)),'new_assert_count':sum(isinstance(n,ast.Assert) for n in ast.walk(b))})
 plans.append({'runner':'scripts/'+stem+'.py','owner':'docs/'+notes[owner],'ordered_inputs':[pin(x) for x in inputs],'timeout_sec':180,'proposed_external_process_tree_limit_bytes':768*1024**2,'memory_cap_status':'proposal for coordinator cold-freeze; not execution authorization','capture_status':'not run','json_output':'logs/runner-cache/'+stem+'.json','completed_family_total':1,'scope':certs[k]})
 diffs.extend(difflib.unified_diff(old.splitlines(True),src.splitlines(True),fromfile='original/evidence/'+oldrun[k]+'.py',tofile='scripts/'+stem+'.py'))
archive=W/'docs/work_history/repo/review_feedback/pr8163-evidence';manifest=json.loads((archive/'archive-manifest.json').read_text());assert len(manifest['entries'])==165
(archive/'README.md').write_text('# Historical source and numerical recovery\n\nThis packet preserves all 165 original paths at `f950bab266a2c2c82321b49d94e21f0f8d2bcf61`, including their modes and blob identities. `archive-manifest.json` maps each original separately to an exact raw SHA-256 and stored payload. Compressed payloads are historical recovery only, not current runtime inputs or audit authority.\n\nThe three full working derivations and complete numerical history remain readable under `kept/`; their provisional wording is superseded by the canonical notes. Both the initial coarse-refinement failure and initially equivalent orientation mutation, all mutant sources and streams, and the 23 final specified formula-fault outcomes remain in the exact archive. No historical successful output is restamped as current-source evidence.\n\nCanonical complete proofs:\n\n'+ '\n'.join('- `docs/'+x+'`' for x in notes)+'\n')
review=json.loads((R/'drain8163-original-review.json').read_text());original={x['path']:x for x in review['path_dispositions']};mapping=[]
canon={str(P/'notes'/x):'docs/'+y for x,y in zip(orig,notes)};canon.update({str(P/'evidence'/(x+'.py')):'scripts/'+y+'.py' for x,y in zip(oldrun,runners)})
for e in manifest['entries']:
 o=original[e['original_path']];stored=archive/e['stored_path'];raw=gzip.decompress(stored.read_bytes()) if e['encoding']=='gzip' else stored.read_bytes()
 assert sha(raw)==e['raw_sha256']==o['sha256'];assert e['git_blob']==o['blob'] and e['original_mode']==o['mode']
 target=canon.get(o['export']);mapping.append({'original_path':e['original_path'],'original_mode':e['original_mode'],'original_blob':e['git_blob'],'original_sha256':e['raw_sha256'],'disposition':'canonical complete source with packaging-only corrections; original recovered exactly' if target else 'superseded development history preserved exactly; no current claim/status imported','recovery':str(stored.relative_to(W)),'recovery_encoding':e['encoding'],'final_path':target,'final_sha256':sha((W/target).read_bytes()) if target else None})
(R/'drain8163-author-correction.diff').write_text(''.join(diffs))
(R/'drain8163-author-preservation.json').write_text(json.dumps(preservation,indent=2)+'\n')
(R/'drain8163-author-full-mapping.json').write_text(json.dumps(mapping,indent=2)+'\n')
(R/'drain8163-author-input-resource-plans.json').write_text(json.dumps(plans,indent=2)+'\n')
prepared={'status':'UNTRACKED_AUTHOR_PREPARED_V1_NOT_REVIEWED_OR_EXECUTED','base':'6b9c6183f24c01651d5a98394061bd88a52aef63','worktree':str(W),'owner':'PR8163-author','notes':['docs/'+x for x in notes],'runners':['scripts/'+x+'.py' for x in runners],'requested_explicit_packet_helpers':{notes[0][:-3].lower():['scripts/'+runners[k]+'.py' for k in [1,4,5]]},'archive_manifest':pin(str((archive/'archive-manifest.json').relative_to(W))),'original_review_sha256':sha((R/'drain8163-original-review.json').read_bytes()),'evidence_files':[str(R/x) for x in ['drain8163-author-correction.diff','drain8163-author-preservation.json','drain8163-author-full-mapping.json','drain8163-author-input-resource-plans.json']],'remaining':['Coordinator global explicit-helper registration, staged identity and actual discovery preflight','Original reviewer correction and cold-source confirmation','Coordinator freeze memory cap then six sole sequential 180-second captures','Final evidence confirmation and combined validation']}
(R/'drain8163-author-prepared-v1.json').write_text(json.dumps(prepared,indent=2)+'\n')
print(json.dumps({'status':prepared['status'],'proofs':3,'runners':6,'original_recoveries':165,'primary_executions':0,'staged':False},indent=2))
