from pathlib import Path
import json, hashlib, gzip, re, ast, subprocess, difflib
R=Path('/private/tmp/review-drain-20260915'); W=R/'drain-author-slot'; O=R/'drain8160-author-originals'; prefix='.claude/science/physics-loops/toe-interacting-scale-20260916/'
rows=json.loads((R/'drain8160-original-inventory.json').read_text()); sha=lambda b:hashlib.sha256(b).hexdigest()
oldnotes=['BLOCK01_UNIFORM_COMPACT_FIELD_AND_SOFT_RESPONSE.md','BLOCK02_UNIFORM_GROUND_ENERGY_AND_OSCILLATOR_DEFECT.md','BLOCK03_JOINT_EQUAL_TIME_GAUGE_LIMIT.md','BLOCK04_JOINT_GAUGE_AND_MATTER_STATE.md','BLOCK05_JOINT_REAL_TIME_GAUGE_TWO_POINT.md','BLOCK06_JOINT_BOUNDED_MATTER_DYNAMICS.md']
stems=['ROTOR_UNIFORM_COMPACT_FIELD_SOFT_RESPONSE','ROTOR_JOINT_GROUND_ENERGY_OSCILLATOR_DEFECT','ROTOR_JOINT_LOCAL_GAUGE_CHARACTERISTIC_LIMIT','ROTOR_JOINT_EQUAL_TIME_WEYL_CAR_STATE','ROTOR_JOINT_REAL_TIME_GAUGE_TWO_POINT_LIMIT','ROTOR_JOINT_BOUNDED_NEUTRAL_MATTER_DYNAMICS']
notes=['docs/'+s+'_BOUNDED_THEOREM_NOTE_2026-09-16.md' for s in stems]
labels=['compact-field concentration theorem','ground-energy and oscillator-defect theorem','gauge characteristic theorem','joint Weyl/CAR state theorem','gauge two-point propagation theorem','bounded matter dynamics theorem']
oldruns=['block01_uniform_response_check.py','block02_integer_gaussian_square_check.py','block02_tree_slater_check.py','block03_characteristic_check.py','block04_weyl_zero_mode_check.py','block05_generator_propagation_check.py','block06_rooted_matter_check.py']
runs=['scripts/'+s+'_2026_09_16.py' for s in ['rotor_uniform_compact_response_check','rotor_integer_gaussian_positive_square_check','rotor_tree_slater_dressing_check','rotor_joint_characteristic_check','rotor_joint_weyl_car_state_check','rotor_joint_gauge_propagation_check','rotor_joint_rooted_matter_dynamics_check']]
owners=[0,1,1,2,3,4,5]; primary=[runs[j] for j in [0,1,3,4,5,6]]
depindices=[[],[0],[0,1],[0,1,2],[0,1,2],[0,3]]
deps=[[notes[j] for j in ix] for ix in depindices]
scopes=[
'Exact integer Gauss-neutral Gaussian trial, uniform compact-field and spectral-response bounds in the supplied homogeneous rotor/CAR model; finite-volume soft weight, not a fixed-coupling phase.',
'Supplied quadratic paired Wilson/rotor model without additional onsite charge interaction: uniform ground-energy and positive-square defect densities tending to zero along every joint g to zero and L to infinity sequence.',
'Same supplied model and normalized full ground trace: local equal-time single-exponential gauge characteristic convergence along every joint weak-coupling/large-volume sequence, with fixed support.',
'Same supplied model: fixed local Weyl words and finite-path neutral CAR polynomials converge jointly to the Gaussian gauge state times the pure filled-band Slater state; equal-time and fixed support.',
'Same supplied model: local electric/magnetic two-point propagation along arbitrary joint weak-coupling/large-volume sequences, uniformly on fixed compact time intervals; no full nonlinear gauge dynamics assertion.',
'Same supplied model on full Gauss Hilbert space: bounded local neutral matter multi-time words converge to free Slater dynamics along arbitrary joint weak-coupling/large-volume sequences, uniformly on fixed compact time intervals.'
]
manifest=[]; owned=[]; maps={}
for i,row in enumerate(rows):
 b=(O/row['original_path']).read_bytes(); assert sha(b)==row['original_sha256']
 dest=f'docs/work_history/review_loop/pr8160/8160_{i:03d}_{Path(row["original_path"]).name}.gz'; p=W/dest; assert not p.exists(); p.parent.mkdir(parents=True,exist_ok=True); p.write_bytes(gzip.compress(b,mtime=0)); owned.append(dest)
 e={**row,'head':'3210315c2cddeb5b0a9e32c9b35e30c196eaa65a','stored':dest,'encoding':'gzip; deterministic mtime=0','archive_sha256':sha(p.read_bytes())};manifest.append(e);maps[row['original_path']]=e
history='docs/work_history/review_loop/pr8160/'
for j,n in enumerate(oldnotes):maps[prefix+'notes/'+n].update(final_path=notes[j],disposition='complete argument retained with canonical packaging and explicit supplied-model scope')
for j,n in enumerate(oldruns):maps[prefix+'evidence/'+n].update(final_path=runs[j],disposition='scientific calculations retained; canonical paths, literal inputs and resolution reporting added')
working={'BLOCK01_WORKING_DERIVATION.md':[0],'BLOCK02_WORKING_JOINT_LIMIT.md':[1,2,3],'BLOCK04_WORKING_MIXED_STATE.md':[3],'BLOCK05_WORKING_REAL_TIME_ELECTRIC.md':[4,5],'BLOCK06_WORKING_BOUNDED_MATTER_DYNAMICS.md':[5]}
for n,ix in working.items():maps[prefix+'notes/'+n].update(disposition='historical development retained byteexact; completed arguments retained in canonical notes',canonical_argument_paths=[notes[j] for j in ix])
status='''**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```
'''
gate='''## No-Go Discipline Gate

N1: this is a positive supplied-model theorem. Fixed-positive-coupling infrared behavior, nonlinear gauge dynamics, growing-support limits, finite-clock realization and native law selection are open directions, not five completed exclusion attempts. No broad negative certificate is claimed.

N2: the model assumptions are stated hypotheses, not independent physical walls. The finite counterexamples refute only the particular inference specified beside them.

N3: the proof retains the normalized full ground trace, possible ground degeneracy, exact Gauss constraint, fixed coefficients, observable domain and order-of-limits quantifiers. Notes requiring free matter exclude an extra unscaled onsite charge interaction.

N4: the supplied continuous rotor/CAR carrier, Hamiltonian, homogeneous weights, Wilson parameters, time and ground ensemble are conditional inputs. Linked proofs below are the actual mathematical dependencies; historical campaign pins confer no authority or additional premise.

N5: the paired programs report finite element/site/mode/block coverage and unchanged tolerances. Uniform-volume estimates, arbitrary joint-sequence convergence and bounded-time analytical arguments are written proofs, not executed infinite-lattice simulations.

N6: conditional mathematical progress does not select the supplied model from the framework axioms or require a new axiom.

N7: alternative interacting fixed-coupling constructions and different physical carriers remain open. Neither finite check success nor the explicit toy counterexamples excludes them.

N8: original personal reviews, failed runs and 28 mutation failures are historical evidence, preserved with their original source hashes. They are not fresh independent review or an audit verdict.
'''
patch=[]
for i,n in enumerate(oldnotes):
 original=(O/prefix/'notes'/n).read_text(); body=original[original.index('## 1.'):]
 # Replace original live branch aliases while preserving every mathematical section.
 for old,new in zip(oldnotes,notes): body=body.replace(old,Path(new).name)
 for old,new in zip(oldruns,runs):
  body=body.replace('../evidence/'+old,'../'+new)
  body=body.replace('../evidence/'+old[:-3]+'.json','../'+history+Path(maps[prefix+'evidence/'+old[:-3]+'.json']['stored']).name)
 body=body.replace('Blocks01--02','the compact-field and ground-energy theorems')
 for j in range(6,0,-1):body=body.replace('Block0'+str(j),labels[j-1])
 body=body.replace('Positive matched\nanisotropic weights from the prior comparator also satisfy','Positive homogeneous\nanisotropic weights also satisfy')
 body=body.replace('No independent review or audit has been performed.','Independent review and audit remain separate.')
 body=body.replace('The accompanying working note records the target before testing. Personal\nadversarial review and its exact input hashes are in review/. All checks\nare by the same author; independent mathematical review remains required.\nPrimary-source reading limits are in the campaign ledger.','The original working derivation, personal review, reading ledger and exact input hashes are historical records in the recovery archive linked below. Historical outputs are not current execution evidence.')
 body=body.replace('## Verification status','## Historical finite verification').replace('## 8. Evidence and outstanding scope','## 8. Finite evidence and scope').replace('## 10. Checks and limits of the result','## 10. Finite checks and limits of the result')
 title=original.splitlines()[0]
 header='---\nclaim_id: '+Path(notes[i]).stem.lower()+'\nclaim_type: bounded_theorem\nrunner: '+primary[i]+'\nupstream_dependencies: '+json.dumps([Path(p).stem.lower() for p in deps[i]])+'\nclaim_scope: '+json.dumps(scopes[i])+'\n---\n\n'+status+'\n'+title+'\n\n'+scopes[i]+'\n\n'
 header+='The model and state are supplied conditions. The proof uses no physical identification from another PR. Historical author checks are distinguished from current source-bound execution below.\n\n'
 if i>0:header+='**Matter restriction:** no additional unscaled onsite charge interaction is included. Use the normalized trace over the entire finite-volume ground space. Local probes and paths are fixed; time claims are uniform only on fixed compact intervals.\n\n'
 links='\n## Mathematical dependencies and current evidence\n\n'
 if deps[i]:links+='Actual load-bearing proofs: '+', '.join('['+labels[j]+']('+Path(notes[j]).name+')' for j in depindices[i])+'.\n\n'
 else:links+='The supplied model and complete argument are defined in this note; no earlier campaign theorem is imported.\n\n'
 if i==4:links+='The Fourier covariance bound used in section 3 is proved in section 2 of the linked gauge characteristic theorem. Its characteristic-function conclusion is not substituted for the separate second-moment argument.\n\n'
 rr=[runs[j] for j,k in enumerate(owners) if k==i]
 links+='Reproduction programs: '+', '.join('['+Path(p).name+'](../'+p+')' for p in rr)+'. Each declares 120 seconds; all calculations and tolerances retain the original finite scope.\n\n'
 links+='Current canonical caches: '+', '.join('['+Path(p).stem+'](../logs/runner-cache/'+Path(p).stem+'.txt)' for p in rr)+'. These links describe the required current evidence; historical outputs do not certify the new source bytes.\n\n'
 links+='[Original recovery](work_history/review_loop/pr8160/README.md) and [exact manifest](work_history/review_loop/pr8160/original-manifest.json) preserve all 86 original files, including full proof development, original outputs, failed propagation runs and mutations.\n'
 text=header+body+'\n'+gate+'\n'+links
 assert not (W/notes[i]).exists();(W/notes[i]).write_text(text);owned.append(notes[i]);patch.extend(difflib.unified_diff(original.splitlines(True),text.splitlines(True),fromfile=prefix+'notes/'+n,tofile=notes[i]))
inputs=[]
for j,i in enumerate(owners):
 inp=[notes[i]]+deps[i]
 if j==3:inp +=[runs[1]]
 if j==6:inp +=[runs[5]]
 inputs.append(list(dict.fromkeys(inp)))
coverage=[
['executed — direct/dual Gaussian sums and literal CAR matrices at unchanged tolerances','executed — finite cubic wave packets R=3,4,7,12 and translated ensembles L=3,4,5,6','executed — selected transverse sine/cosine modes and finite spectral measures','executed — rank-two cycles, 16-dimensional CAR and degenerate-ground fixtures'],
['executed — integer Smith invariants, weighted metrics and parity sums','executed — literal periodic 3-cube incidence and plaquette boundaries','executed — positive-range matrix calculus and finite Fourier cutoff7','executed — padded-core square identity with full-cutoff discrepancy retained'],
['executed — integer paths, signed loop fillings and Slater determinant curvature','executed — open cubic blocks R=2,3,4 with explicit subtree charges','executed — occupied open-Wilson eigenvectors and particle-hole symmetry','executed — 64-state charged dressing and paired Slater variances'],
['executed — differentiated commutators, Fourier normalization and Duhamel quadrature','executed — 3-cube geometry and seven-site two-component covariance fixture','executed — four single-rotor cutoffs at g=0.6,0.4,0.25,0.16','executed — finite weighted matrices, translated defects and rotor exponentials'],
['executed — Weyl signs and nonprojection covariance discriminator','executed — local versus global covariance on finite rings L=8,16,32,64','executed — single-rotor Fourier cutoffs and exact auxiliary zero momenta','executed — ground and excited rotor vectors, two-band and four-state fixtures'],
['executed — charged flux increments, current signs and residual identities','executed — four-site charged ring at g=0.6,0.4,0.25','executed — weighted symbols on grids L=5,8,12 and three small radii; finite norms are diagnostic','executed — sparse charged Duhamel comparisons and hidden-oscillator witness'],
['executed — CAR signs, quadratic path term and residual decomposition','executed — four-site charged ring in a 36-configuration fixed-number sector','executed — three finite flux cutoffs with original 1e-16 tail threshold','executed — bounded matter propagation at times0.7 and1.4 with sign discriminator']]
for j,n in enumerate(oldruns):
 original=(O/prefix/'evidence'/n).read_text();text=original
 for a,b in zip(oldruns,runs):text=text.replace(a,Path(b).name).replace('from '+a[:-3]+' import','from '+Path(b).stem+' import')
 text=re.sub(r'AUDIT_INPUT_PATHS = \[[\s\S]*?\]\n','AUDIT_INPUT_PATHS = '+repr(tuple(inputs[j]))+'\n',text,count=1)
 text=re.sub(r'# No external scientific data are read\. The source self-hash is an integrity read\.','# Literal proof inputs are read below; the source self-hash is an integrity read.',text)
 pin='''\n_REPO = Path(__file__).resolve().parents[1]
for _input_path in AUDIT_INPUT_PATHS:
    _input_bytes = (_REPO / _input_path).read_bytes()
    if _input_path.endswith('.md'):
        assert ('claim_id: ' + Path(_input_path).stem.lower()).encode() in _input_bytes
'''
 pos=text.index('\nTOL');text=text[:pos]+pin+text[pos:]
 text=text.replace('The charged ring basis adapts the explicit Gauss construction in the previous\ncampaign\'s block24 runner at ccca36e505a4cc5d0cd4735b377c15d69042fc41.','Historical provenance: the charged ring basis was adapted from a prior\nGauss construction. Exact original source and provenance are archived under\ndocs/work_history/review_loop/pr8160; no prior executable is loaded.')
 text=text.replace('Uses the same Gauss basis as the preceding campaign and Block05, while','Uses the explicit Gauss basis of the gauge propagation program, while')
 lines=[k+': '+v for k,v in zip(['per_element','per_site','per_mode','per_block'],coverage[j])]+['lattice_wide: checked and not executed — uniform bounds and joint-limit/time arguments are written proofs; finite fixtures do not execute an infinite lattice']
 at='    print(f"TOTAL: PASS={checks} FAIL=0")';assert text.count(at)==1
 text=text.replace(at,''.join('    print('+repr(x)+')\n' for x in lines)+at)
 ast.parse(text);assert not (W/runs[j]).exists();(W/runs[j]).write_text(text);owned.append(runs[j]);patch.extend(difflib.unified_diff(original.splitlines(True),text.splitlines(True),fromfile=prefix+'evidence/'+n,tofile=runs[j]))
for e in manifest:
 if e['final_path']:e['final_sha256']=sha((W/e['final_path']).read_bytes())
(W/history/'original-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');owned.append(history+'original-manifest.json')
readme='''# PR8160 exact original recovery

The [manifest](original-manifest.json) binds all 86 original paths, modes, Git blobs and SHA-256 hashes at head `3210315c2cddeb5b0a9e32c9b35e30c196eaa65a`, delta base `e0ef7cf4633034a8c1e6d57f5812cc4275bf1349`. Each uniquely named gzip payload decodes to the exact original bytes. The manifest and archived payloads preserve original source independently of branch retention.

Six complete final proofs and seven active programs have canonical counterparts listed in the manifest. The five working derivations remain exact historical versions; their completed compact-response, weighted-metric/dual-pressure/tree-Slater, characteristic, Weyl/CAR, gauge residual and rooted-matter arguments are retained in the corresponding full live proofs. Working conjectures are not extra proved conclusions.

All eleven original Python sources remain recoverable, including the earlier preflight, both failed propagation sources and mutation harness. The original raw JSON/stdout/stderr bundles, personal reviews and all 28 mutation failures are historical source-bound evidence, not new runs or independent authority.

The first propagation failure was array-to-scalar conversion. The second retained outer-flux mass 4.984945699760506e-16 above the declared 1e-16 threshold; the final source enlarged cutoff ceil(6/g) to ceil(8/g) while preserving that threshold. Padded-core versus full hard-cutoff discrepancies, degenerate pure-ground elastic commutator, equal nonprojection covariance with different higher correlations, global/local zero-mode distinction and the hidden high-frequency oscillator are retained. Each witness has its stated narrow target; none establishes a model-wide exclusion.
'''
(W/history/'README.md').write_text(readme);owned.append(history+'README.md')
(R/'drain8160-author-corrections-v1.patch').write_text(''.join(patch))
# Static checks only: no imports or execution of scientific code.
for p in runs:
 t=ast.parse((W/p).read_text()); assignments=[n.lineno for n in ast.walk(t) if isinstance(n,ast.Name) and n.id=='AUDIT_INPUT_PATHS' and isinstance(n.ctx,ast.Store)];loads=[n.lineno for n in ast.walk(t) if isinstance(n,ast.Name) and n.id=='AUDIT_INPUT_PATHS' and isinstance(n.ctx,ast.Load)];assert assignments and loads and min(assignments)<min(loads)
tracked=subprocess.check_output(['git','diff','--name-only','HEAD'],cwd=W,text=True);assert not tracked
receipt={'status':'UNTRACKED AUTHOR PREPARATION; NO FINAL REVIEW OR EXECUTION','base':subprocess.check_output(['git','rev-parse','HEAD'],cwd=W,text=True).strip(),'notes':notes,'runners':runs,'primary_runners':primary,'dependencies':dict(zip(notes,deps)),'inputs':dict(zip(runs,inputs)),'helper_map_plan':{Path(notes[1]).stem.lower():[runs[2]],Path(notes[2]).stem.lower():[runs[1]],Path(notes[5]).stem.lower():[runs[5]]},'original_count':86,'archive_manifest_sha256':sha((W/history/'original-manifest.json').read_bytes()),'timeouts_seconds':dict.fromkeys(runs,120),'proposed_external_memory_cap_bytes':536870912,'resource_assessment':'All seven original declarations are120s; retained unchanged. Largest charged sparse ring dimension36*(2*32+1)=2340; dense one-rotor139; Smith81x81 integer matrix; largest open Wilson128x128; finite symbol grid12^3. Propose512MiB process-tree cap sequentially. No original measured runtime/peak receipt identified; no new runtime measurement claimed. Actual original outputs and 28 source-bound mutation failures retained.','static_checks':{'ast_parse':7,'input_definition_before_load':7,'tracked_changes':0,'primary_executions':0},'original_report':{'path':str(R/'drain8160-original-review.json'),'sha256':sha((R/'drain8160-original-review.json').read_bytes())},'files':[{'path':p,'sha256':sha((W/p).read_bytes())} for p in sorted(owned)],'remaining':'No existing helper maps edited or staging. Wait root guarded base advance after train74 before helper union, schema2 cheap preflight and same-session final source review. Root owns captures.'}
p=R/'drain8160-author-prepared-v1.json';assert not p.exists();p.write_text(json.dumps(receipt,indent=2)+'\n');print('prepared',len(owned),'owned untracked files; no primary executed')
