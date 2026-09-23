import ast,difflib,gzip,hashlib,json,subprocess
from pathlib import Path
R=Path('/private/tmp/review-drain-20260915'); W=R/'review-meta-slot'
report=json.loads((R/'drain8162-original-review.json').read_text()); rows=report['path_dispositions']; assert len(rows)==90
P=R/'drain8162-originals/.claude/science/physics-loops/toe-continuous-time-bridge-20260916'
notes=['docs/CLOCK_VARIANCE_CALIBRATED_JOINT_ROTOR_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-16.md','docs/CLOCK_ALL_MODE_COERCIVITY_FINITE_GRAPH_STATES_BOUNDED_THEOREM_NOTE_2026-09-16.md']
runners=['scripts/clock_variance_calibrated_transfer_check_2026_09_16.py','scripts/clock_all_mode_finite_graph_states_check_2026_09_16.py']
oldnotes=['BLOCK02_CALIBRATED_CLOCK_ROTOR_TRANSFER_THEOREM.md','BLOCK03_ALL_MODE_COERCIVITY_AND_FINITE_VOLUME_STATES.md']; oldruns=['block02_calibrated_transfer_check.py','block03_all_mode_and_states_check.py']
hist='docs/work_history/review_loop/pr8162'; owned=[];diffs=[]
def sha(b):return hashlib.sha256(b).hexdigest()
def put(path,data):
 p=W/path;assert not p.exists(),path;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data if isinstance(data,bytes) else data.encode());owned.append(path)
manifest=[]
for i,row in enumerate(rows,1):
 b=Path(row['export']).read_bytes();assert sha(b)==row['sha256'];assert subprocess.check_output(['git','-C',str(W),'cat-file','blob',row['blob']])==b
 dest=f'{hist}/originals/{i:03d}-{Path(row["path"]).name}.gz';put(dest,gzip.compress(b,mtime=0));assert gzip.decompress((W/dest).read_bytes())==b
 manifest.append({k:row[k] for k in ['path','mode','blob','sha256','bytes']}|{'archive':dest,'encoding':'gzip; decoded bytes exact','disposition':row['disposition']})
put(hist+'/manifest.json',json.dumps({'original_head':report['original_head'],'original_delta_base':report['original_delta_base'],'paths':manifest},indent=2)+'\n')
put(hist+'/README.md','# PR8162 exact source recovery\n\nThe [manifest](manifest.json) records all 90 original paths, modes, Git blobs and decoded SHA256 hashes. Each payload is gzip encoded without altering its decoded bytes. The manifest and archived payloads preserve original source independently of branch retention.\n\nThe complete transfer and state proofs are canonical; charged-ring conventions are the state-note appendix. Both working derivations are retained as historical appendices to the transfer note. All original failures, three failed state attempts, tiny-gap correction and 14 mutation programs and outcomes remain exact historical payloads. Historical outputs are not current-source cache evidence.\n')
prior='COMPACT_DETERMINANT_CURRENTS_SIGNED_SECTORS_AND_FINITE_CYCLIC_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-14.md'
boundary='''\n## Evidence and boundary obligations\n\n- N1: Naive sampled scaling, variance calibration and noncommuting-factor tests address the stated supplied model. They are not five independent attacks on a physical impossibility claim; negative certification is withheld.\n- N2: Native law/time selection, spatial thermodynamic control, fixed payload, volume-uniform defects and interacting gapless matter remain OPEN. Distinct obligations are not a proof of independent exclusion routes.\n- N3: Coupling, time, finite graph, finite-dimensional matter and gauge-compatible Laurent multiplier are supplied. Scalar shifts are tracked; nonempty physical sectors are required for normalized states.\n- N4: Core residuals are C_f(delta²+delta/N²); compactness sends the sequence limit before the Fourier cutoff. The heat majorant depends on graph size and coupling.\n- N5: The program executes finite ring configurations and finite Fourier modes. Whole-lattice checks here mean only the explicitly enumerated finite ring. Infinite-mode identities and every-joint-path limits are written proofs, not executed lattice simulations. Cutoff comparisons are floating diagnostics, not interval bounds.\n- N6: Uniform anisotropic estimates, direct Hamiltonian arguments and alternative finite-clock constructions remain open research routes.\n- N7: The principal finite-graph objection is modular high-mode spectral escape; the explicit theta floor and compactness argument address it only under the stated assumptions.\n- N8: Prior fixed-clock and spatial matching are contextual prior art; no earlier result is promoted to a thermodynamic phase. No native clock, coupling, physical phase or axiom update follows.\n'''
for i,(old,new,runner) in enumerate(zip(oldnotes,notes,runners)):
 s=(P/'notes'/old).read_text();title=s.splitlines()[0];s=s[s.index('\n## 1.'):]
 header=f'''---\nclaim_id: {Path(new).stem.lower()}\nclaim_type: bounded_theorem\nrunner: {runner}\nupstream_dependencies: {json.dumps([] if i==0 else [notes[0]])}\nclaim_scope: "Supplied fixed finite graph and coupling; every joint delta to zero and N to infinity path."\n---\n\n{title}\n\n**Type:** bounded_theorem\n\n```yaml\nactual_current_surface_status: conditional-support\nconditional_surface_status: conditional-support\ntrace_class: upstream_support\nreachability_to_target: supports\naudit_required_before_effective_retained: true\nbare_retained_allowed: false\nhypothetical_axiom_status: null\nadmitted_observation_status: null\n```\n\nThis is a conditional mathematical result for fixed supplied g>0, external time, a finite spatial graph and finite-dimensional gauge-compatible matter. No spatial-volume or varying-coupling uniformity is asserted.\n\n'''
 if i==0:header+=f'Contextual prior art: [compact currents and finite cyclic transfer, Part III]({prior}); the complete argument used here is given below.\n'
 else:header+=f'Actual dependency: [variance-calibrated joint rotor transfer]({Path(notes[0]).name}), with its supplied model and core-consistency hypotheses.\n'
 s=s.replace('Block02','the variance-calibrated transfer theorem').replace('BLOCK02','the variance-calibrated transfer theorem')
 if i==0:
  s=s.replace('All calculations and review in this campaign are by the author.','These statements describe the original author campaign; they are historical provenance, not current independent-review or cache claims.')
  s+='\n## Historical working derivations\n\nThe following complete working texts preserve the original exploratory arguments. Their provisional language and prior-art claims are historical; the current theorem and its hypotheses are in sections 1–8 above.\n'
  for f in ['BLOCK01_WORKING_TRANSFER_MATCHING.md','BLOCK02_VARIANCE_CALIBRATED_TEMPORAL_TRANSFER_WORKING.md']:
   s+='\n### Historical '+f+'\n\n'+(P/'notes'/f).read_text().replace('\n#','\n###')
 else:
  conv=(P/'notes/BLOCK03_CHARGED_RING_CHECK_CONVENTIONS.md').read_text().replace('# Charged-ring conventions for the finite state check','## Appendix: charged-ring conventions for the finite state check').replace('in Block03','in sections 1–6 above')
  s+='\n'+conv
 s=header+s+boundary+f'\n[Canonical program](../{runner}) · [Current cache](../{runner[:-3]}.cache.txt) · [Exact original recovery](work_history/review_loop/pr8162/README.md).\n'
 put(new,s);diffs.extend(difflib.unified_diff((P/'notes'/old).read_text().splitlines(True),s.splitlines(True),fromfile=old,tofile=new))
for i,(old,new) in enumerate(zip(oldruns,runners)):
 original=(P/'evidence'/old).read_text();s=original
 inputs=[notes[0]] if i==0 else notes
 code='AUDIT_INPUT_PATHS = '+repr(inputs)+'\n'
 s=s.replace('AUDIT_INPUT_FILES=[]',code.rstrip())
 marker='from pathlib import Path\n'
 pins='\n_REPO_ROOT = Path(__file__).resolve().parents[1]\n_INPUT_TEXT = {p: (_REPO_ROOT / p).read_text() for p in AUDIT_INPUT_PATHS}\n'
 for p in inputs:pins+=f'assert {Path(p).stem.lower()!r} in _INPUT_TEXT[{p!r}]\n'
 pins+=f'assert {"v(c)=delta g² N²/(4pi²)"!r} in _INPUT_TEXT[{notes[0]!r}]\n'
 if i:pins+=f'assert {"I-T=(I-M^2)+M(I-Q)M"!r} in _INPUT_TEXT[{notes[1]!r}]\n'
 s=s.replace(marker,marker+pins)
 tail=f'''\n    print("TOTAL: PASS={5 if i==0 else 3} FAIL=0")\n    print("N5 per_site: finite four-link ring configurations and explicit Gauss labels checked")\n    print("N5 per_block: finite mode/parameter families completed; see JSON rows")\n    print("N5 whole_lattice: supplied finite ring only; no infinite-lattice execution")\n    print("N5 lattice_wide: analytical joint-limit proof not executed; floating cutoffs are diagnostics")\n'''
 pos=s.index("\nif __name__") if '\nif __name__' in s else -1
 s=s[:pos].rstrip()+tail+'\n'+s[pos:]
 ast.parse(s);put(new,s)
 origfunc={n.name:ast.dump(n,include_attributes=False) for n in ast.parse(original).body if isinstance(n,ast.FunctionDef) and n.name!='run'}
 newfunc={n.name:ast.dump(n,include_attributes=False) for n in ast.parse(s).body if isinstance(n,ast.FunctionDef) and n.name!='run'};assert origfunc==newfunc
 diffs.extend(difflib.unified_diff(original.splitlines(True),s.splitlines(True),fromfile=old,tofile=new))
receipt={'status':'AUTHOR PREPARATION ONLY; cold review and execution pending','base':subprocess.check_output(['git','-C',str(W),'rev-parse','HEAD'],text=True).strip(),'notes':notes,'runners':runners,'original_count':90,'paths':[{'path':p,'sha256':sha((W/p).read_bytes())} for p in owned],'proof_mapping':{'transfer':'complete final sections1–9; both full working derivations historical appendices','states':'complete final sections1–7 plus complete charged-ring convention appendix'},'inputs':{r:([notes[0]] if i==0 else notes) for i,r in enumerate(runners)},'helpers':[],'proposed_capture':{'seconds_each':180,'memory_bytes_each':536870912,'sequence':'two serial captures after cold and cheap confirmation','basis':'Original declared180s; largest neutral dense rotor201, charged rotor388 and finite full clock1024x16 arrays, theta arrays ~10667; historical wall outputs0.275s/0.494s are not current measurements;512MiB allows numerical-library overhead.'},'checks':'90 decoded archives exact Git/SHA; AST parsed; scientific non-run functions unchanged; no primary imports/execution; no staging/maps'}
assert len(owned)==96
(R/'drain8162-author-prepared-v1.json').write_text(json.dumps(receipt,indent=2)+'\n');(R/'drain8162-author-corrections-v1.patch').write_text(''.join(diffs))
print(json.dumps({'paths':len(owned),'receipt_sha256':sha((R/'drain8162-author-prepared-v1.json').read_bytes())}))
