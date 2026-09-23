from pathlib import Path
import ast,collections,difflib,gzip,hashlib,json,re,subprocess
R=Path('/private/tmp/review-drain-20260915');W=R/'drain-author-slot';O=R/'drain8164-originals';sha=lambda b:hashlib.sha256(b).hexdigest()
report=R/'drain8164-original-review.json';assert sha(report.read_bytes())=='2df0a061e704714b80e35d067ddd72d3ded9fa17c5fae7e448138897b33a6da6';rv=json.loads(report.read_text());rows=rv['path_dispositions'];assert len(rows)==178
assert json.loads((R/'drain-author-slot.json').read_text())['owner']=='PR8164-author'
base=subprocess.check_output(['git','-C',str(W),'rev-parse','HEAD'],text=True).strip();assert base=='16574d8f023c06a3ef86fe6d8993a257e0936c81'
assert not subprocess.check_output(['git','-C',str(W),'status','--porcelain']).strip()
proofs=sorted([e for e in rows if e['role']=='complete-proof'],key=lambda e:e['path']);assert len(proofs)==8
labels=['WEIGHTED_GAUSSIAN_DAMPING_AND_INTEGER_TIME_BLOCKING','FINITE_BOX_ELECTRIC_OFFSET_RESPONSE_AND_TAIL_BOUNDS','WEIGHTED_PHASE_CORRECTOR_AND_MAGNETIC_GRAM_CERTIFICATES','LOCAL_ROTOR_DENSITY_AND_FINITE_TEMPLATE_BOUNDS','COMPACT_ROTOR_GROUND_CORRELATION_COMPARISON','PRINCIPAL_LINK_RAW_CURL_WITNESS_AND_MASS_BOUND','POSITIVE_WILSON_VILLAIN_MIXTURE_AND_WEAK_REGION_BOUNDS','SHORT_TIME_ROTOR_BRIDGE_AND_ENDPOINT_HESSIAN_BOUNDS']
titles=['Weighted Gaussian damping and integer time blocking','Finite-box electric offset response and factorial tail bounds','Weighted phase correctors and magnetic Gram certificates','Local rotor density and finite-template bounds','Compact rotor ground correlation comparison','Principal-link raw-curl witness and mass-dependent bound','Positive Wilson–Villain mixtures and weak-region bounds','Short-time rotor bridges and endpoint Hessian bounds']
notes=['docs/'+x+'_BOUNDED_THEOREM_NOTE_2026-09-16.md' for x in labels]
runners=['scripts/'+x.lower()+'_check_2026_09_16.py' for x in labels]
deps=[[],[0],[1],[1,2],[],[],[],[]];groups=[['weighted_gaussian_check','integer_temporal_blocking'],['transfer','electric_response','ground_tail'],['one_plaquette','two_square','cube'],['heat_comparison','geometry','circle_bounds','principal_cube_event'],['connected','covering','negative_coupling_control'],['exact_failure_certificate'],['radial_heat','cube_mixture','circle_convolution','infinite_mean_cusp'],['cosine_bridge','endpoint_nonconvex_control','time_limit']]
scopes=[['conditional precision and half-factor','finite4D curl complex','finite512-mode convolution and cutoffs','Gaussian quadrature and Skellam arithmetic'],['electric offset and commutator','two adjacent square cycles','finite625-state cutoff spectra and inverse solve','65-state transfer and factorial recurrence'],['phase/Gram normalization','one plaquette,two squares and one cube','finite character radii and harmonic grids','shared response helper; no independent implementation claim'],['heat kernel and character identities','finite cubes and4096 cube corners','finite Haar-character arithmetic and wrapped images','81-state two-angle kernel'],['cosine and electric-square derivatives','two-angle model; not growing boxes','finite225-state Galerkin spectra','49-mode lifted kernel and parity trace'],['rational-angle action inequality','nine-vertex free square','not executed: no spectral/Fourier modes','one exact finite counterexample only'],['radial transform and mixture normalization','one cube with64 two-point masks','selected radial modes and4096 circle FFT','finite mixture,convolution and cusp controls'],['endpoint derivatives and covariance sign','one/two plaquette coordinates','finite time slices and Gaussian quadrature','16^4/20^4 refinements and compact kernel']]
archive='docs/work_history/review_loop/pr8164';made=[];patches=[];mapping=[]
def write(p,b):
 f=W/p;assert not f.exists(),p;f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes(b);made.append(p)
for i,e in enumerate(rows):
 b=(O/e['path']).read_bytes();assert sha(b)==e['sha256'];assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['blob']
 dst=f'{archive}/originals/{i:03d}-{Path(e["path"]).name}.gz';z=gzip.compress(b,mtime=0);write(dst,z)
 mapping.append(dict(original_path=e['path'],original_mode=e['mode'],original_blob=e['blob'],original_sha256=e['sha256'],archive=dst,archive_sha256=sha(z),encoding='gzip; exact decoded original bytes',recovery=rv['head']+':'+e['path'],disposition=e['disposition'],canonical_path=None))
for i,e in enumerate(proofs):
 old=(O/e['path']).read_text();body=old
 # Only three explicit historical Markdown link destinations are replaced. No Markdown-pattern matching.
 for target in ['../CLAIM_STATUS_CERTIFICATE.md','../ASSUMPTIONS_AND_IMPORTS.md','../NO_GO_DISCIPLINE_CHECKLIST.md']:
  body=body.replace(']('+target+')','](work_history/review_loop/pr8164/README.md)')
 assert [x for x in old.splitlines() if x.startswith(' ')]==[x for x in body.splitlines() if x.startswith(' ')]
 cid=Path(notes[i]).stem.lower();header='---\nclaim_id: '+cid+'\nclaim_type: bounded_theorem\nrunner: '+runners[i]+'\nupstream_dependencies: '+json.dumps([notes[j] for j in deps[i]])+'\nclaim_scope: '+json.dumps(rv['claims_and_boundaries'][i])+'\n---\n\n# '+titles[i]+'\n\n**Type:** bounded_theorem\n\n```yaml\nactual_current_surface_status: conditional-support\nconditional_surface_status: conditional-support\ntrace_class: upstream_support\nreachability_to_target: supports\naudit_required_before_effective_retained: true\nbare_retained_allowed: false\nhypothetical_axiom_status: null\nadmitted_observation_status: null\n```\n\n## Scope and provenance\n\n'+rv['claims_and_boundaries'][i]+'\n\nThe complete original mathematical argument follows. Its personal reading, timing, proposal and review statements describe historical work, not a new review or current execution. Model parameters are supplied. No PR8160, PR8162 or PR8163 result is implicitly a premise. Narrow quantitative bounds and explicit witnesses do not supply a broad negative certificate or a physical phase. No five-route no-go PASS is asserted.\n\n'
 if deps[i]:header+='Actual mathematical dependencies:\n\n'+''.join('- ['+titles[j]+']('+Path(notes[j]).name+').\n' for j in deps[i])+'\n'
 else:header+='The supplied model and proof are redeclared here; other campaign mentions are context.\n\n'
 header+='## Complete argument\n\n'
 footer='\n\n## Canonical evidence boundary\n\n[Program](../'+runners[i]+'); [current stdout cache](../logs/runner-cache/'+Path(runners[i]).stem+'.txt). The canonical TOTAL counts '+str(len(groups[i]))+' completed finite control families, not each loop iteration or an analytical theorem. All original assertion expressions and tolerances are retained. No canonical capture has run during preparation. Historical outputs, failed refinements and mutations remain in the [exact recovery archive](work_history/review_loop/pr8164/README.md).\n'
 new=header+body+footer;write(notes[i],new.encode());patches.extend(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=e['path'],tofile=notes[i]));mapping[next(k for k,x in enumerate(mapping) if x['original_path']==e['path'])]['canonical_path']=notes[i]
# Runtime output adapter preserves the original report expression and each scientific function body.
checks=[];runtime=[];cost=[]
for i,prim in enumerate(rv['primary_programs']):
 src=next(e for e in rows if Path(e['path']).name==prim['source']);old=(O/src['path']).read_text();assert sha(old.encode())==prim['source_sha256'];tree=ast.parse(old)
 ins=[notes[i]]+[notes[j] for j in deps[i]]
 if i==2:ins += [runners[1],notes[0]]
 new=old
 # Remove only the exact legacy metadata assignment lines, verified AST below.
 for n in reversed(tree.body):
  if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUDIT_INPUT_FILES' for t in n.targets):
   lines=new.splitlines(True);del lines[n.lineno-1:n.end_lineno];new=''.join(lines)
 if i==2:
  new=new.replace('PARENT = HERE / AUDIT_INPUT_FILES[0]','PARENT = _REPO_ROOT / '+repr(runners[1]));new=new.replace('5981a5204073001efa670d996adfb45be698275e5a6ae8914ba88755e70f280b',sha((W/runners[1]).read_bytes()))
 # Replace the sole report print by an adapter; expression contents are unchanged.
 nt=ast.parse(new);calls=[n for n in ast.walk(nt) if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=='print'];assert len(calls)==1
 call=calls[0];assert isinstance(call.args[0],ast.Call) and ast.unparse(call.args[0].func)=='json.dumps'
 lines=new.splitlines(True);line=lines[call.lineno-1];assert line[call.col_offset:].startswith('print(');lines[call.lineno-1]=line[:call.col_offset]+'_emit_json('+line[call.col_offset+6:];new=''.join(lines)
 pin=next(x.strip() for x in (O/proofs[i]['path']).read_text().splitlines() if x.startswith('    ') and x.strip())
 adapter='\nfrom pathlib import Path as _InputPath\n_REPO_ROOT = _InputPath(__file__).resolve().parents[1]\nAUDIT_INPUT_PATHS = '+repr(ins)+'\n_INPUT_TEXT = {p: (_REPO_ROOT / p).read_text() for p in AUDIT_INPUT_PATHS}\nassert '+repr(pin)+' in _INPUT_TEXT['+repr(notes[i])+']\n'
 for j in deps[i]:adapter+='assert '+repr(Path(notes[j]).stem.lower())+' in _INPUT_TEXT['+repr(notes[j])+']\n'
 adapter+='''def _emit_json(text):
    import json as _json
    payload = _json.loads(text)
'''
 adapter+='    families = '+repr(groups[i])+'\n    assert all(k in payload for k in families)\n'
 adapter+='    payload["canonical_completed_families"] = families\n    payload["canonical_total"] = len(families)\n    output = _REPO_ROOT / '+repr('logs/runner-cache/'+Path(runners[i]).stem+'.json')+'\n    output.parent.mkdir(parents=True, exist_ok=True)\n    output.write_text(_json.dumps(payload, indent=2, allow_nan=False)+"\\n")\n    print(_json.dumps(payload, indent=2, allow_nan=False))\n    print("TOTAL: PASS="+str(len(families))+" FAIL=0")\n'
 for label,scope in zip(['per_element','per_site','per_mode','per_block'],scopes[i]):adapter+='    print('+repr(label+': '+scope)+')\n'
 adapter+='    print("lattice_wide: analytical statements checked in written proof, not executed; no volume-uniform phase computation")\n\n'
 # Insert after docstring, preserving shebang and all original imports/calculations.
 nt=ast.parse(new);end=nt.body[0].end_lineno if isinstance(nt.body[0],ast.Expr) and isinstance(nt.body[0].value,ast.Constant) and isinstance(nt.body[0].value.value,str) else 0
 lines=new.splitlines(True);new=''.join(lines[:end])+adapter+''.join(lines[end:]);compile(new,runners[i],'exec')
 # Reverse only authored IO adaptation before comparing every original scientific function/class AST.
 back=new.replace('_emit_json(json.dumps','print(json.dumps');ot=ast.parse(old);bt=ast.parse(back)
 funcs=lambda t:{n.name:ast.dump(n,include_attributes=False) for n in t.body if isinstance(n,(ast.FunctionDef,ast.ClassDef))}
 before=funcs(ot);after=funcs(bt);assert all(after[k]==v for k,v in before.items()),prim['source']
 write(runners[i],new.encode());patches.extend(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=src['path'],tofile=runners[i]));mapping[next(k for k,x in enumerate(mapping) if x['original_path']==src['path'])]['canonical_path']=runners[i]
 checks.append({'runner':runners[i],'scientific_function_ASTs_unchanged':len(before),'original_assertion_expressions':sum(isinstance(n,ast.Assert) for n in ast.walk(ot)),'families':groups[i],'no_execution':True});runtime.append({'runner':runners[i],'declared_inputs':ins,'helpers':[runners[1]] if i==2 else [],'note_pin':pin})
 basis=['216-link4D curl precision (~0.36MiB square),512 Fourier modes and13 jumps; finite quadrature','65x65 transfer matrices;625-state sparse eigsh k8 and conjugate gradient;90-digit recurrence160','73x8192 harmonic grid (~4.6MiB),625-state sparse solve and at most24-character Gram; shared02 definitions only','81x81 heat matrices,144-plaquette geometry,4096x12 cube corners (~0.38MiB)','225x225 full eigensystems retained for finite differences;49x49 lifted kernel','Exact Fraction arithmetic on12 edges and4 faces','Radial size ceil(8*1024.5)=8196; stebz selects eigenvalues in[-100a,0],vectors8196×selected modes. Even full real eigenvector array~512MiB;1GiB operational ceiling includes LAPACK/library workspace. Selected count observed only during eventual capture.','160000 Gaussian points×8 noise entries~9.8MiB; order16 and20 quadratures coexist, several field/trig/gradient arrays (~10MiB each); sequential evaluates, no160000-square matrix.384MiB includes temporary arrays and libraries.'][i]
 cost.append({'runner':runners[i],'timeout_seconds':180,'process_tree_rss_cap_bytes':(1024 if i==6 else 384)*1024**2,'basis':basis,'estimate_kind':'Source-derived operational ceiling, not measured peak or guaranteed bound','failure_policy':'Sequential bounded capture only after cold/cheap; preserve failure; no fixture/tolerance reduction'})
write(archive+'/manifest.json',(json.dumps({'head':rv['head'],'delta_base':rv['merge_base'],'paths':mapping},indent=2)+'\n').encode())
write(archive+'/README.md',('# PR8164 exact original recovery\n\nAll178 original files retain exact decoded bytes, original modes, Git blobs and SHA256 in [manifest](manifest.json). Eight complete arguments and eight active programs have canonical destinations. All48 original Python files,23 mutation failures, failed numerical attempts, diagnostics and historical verification remain archived. Historical claims and outputs are not current reviewer or execution evidence.\n\nThe manifest and archived payloads preserve original source independently of branch retention. The supplied fixed-coupling response/phase target remains open; bounded estimates and explicit witnesses are not broad no-go certification.\n').encode())
for name,obj in [('resource-plan',cost),('input-plan',runtime),('preservation-checks',checks)]:
 p=R/f'drain8164-author-{name}-v1.json';assert not p.exists();p.write_text(json.dumps(obj,indent=2)+'\n')
p=R/'drain8164-author-corrections-v1.patch';assert not p.exists();p.write_text(''.join(patches))
prepared={'status':'UNTRACKED AUTHOR PREPARATION; INDEPENDENT EARLY REVIEW PENDING','base':base,'notes':notes,'runners':runners,'dependencies':{notes[i]:[notes[j] for j in deps[i]] for i in range(8)},'helper_map_plan':{Path(notes[2]).stem.lower():[runners[1]]},'files':[{'path':p,'sha256':sha((W/p).read_bytes())} for p in sorted(made)],'original_count':178,'original_dispositions':mapping,'resource_plan':cost,'runtime_plan':runtime,'proof_preservation':'Full original proof bodies retained; only three explicit historical Markdown destinations changed. Independent indented mathematical lines exactly identical. Every original scientific function/class AST identical after reversing print adapter only.','review_reference':{'path':str(report),'sha256':sha(report.read_bytes())},'no_primary_execution':True}
p=R/'drain8164-author-prepared-v1.json';assert not p.exists();p.write_text(json.dumps(prepared,indent=2)+'\n');print(len(made),sha(p.read_bytes()))
