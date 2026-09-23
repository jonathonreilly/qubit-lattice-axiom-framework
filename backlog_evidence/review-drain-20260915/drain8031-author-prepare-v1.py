import pathlib,json,hashlib,gzip,difflib,ast,subprocess
R=pathlib.Path('/private/tmp/review-drain-20260915'); W=R/'review-draft-slot'; O=R/'drain8031-originals'
sha=lambda b:hashlib.sha256(b).hexdigest()
assert json.loads((R/'review-draft-slot.json').read_text())['owner']=='PR8031-author'
assert not subprocess.check_output(['git','-C',str(W),'status','--porcelain'])
inv=json.loads((R/'drain8031-original-manifest.json').read_text()); oldnote='docs/GAUGE_WILSON_FINITE_TRANSPORTER_UNITARITY_PW_DEFECT_BOUNDED_THEOREM_NOTE_2026-09-07.md'
note='docs/GAUGE_WILSON_PW_COMPRESSION_SHELL_AND_ENERGY_PATH_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-07.md'; runner='scripts/gauge_wilson_finite_transporter_pw_defect_check_2026_09_07.py'
parent='docs/GAUGE_WILSON_COMPACT_CUBE_FINITE_QUBIT_CUTOFF_BOUNDED_THEOREM_NOTE_2026-09-07.md'
hist='docs/work_history/review_loop/pr8031'; rows=[]; owned=[]
def put(p,b):
 q=W/p; assert not q.exists(),p; q.parent.mkdir(parents=True,exist_ok=True); q.write_bytes(b if isinstance(b,bytes) else b.encode()); owned.append(p)
for i,r in enumerate(inv['files']):
 b=(O/r['path']).read_bytes(); assert sha(b)==r['sha256']; assert sha(b)==sha(subprocess.check_output(['git','-C',str(W),'show',inv['head']+':'+r['path']]))
 dest=f'{hist}/original-{i+1:03d}-{r["sha256"][:12]}.gz'; put(dest,gzip.compress(b,mtime=0)); assert gzip.decompress((W/dest).read_bytes())==b
 rows.append({**{k:v for k,v in r.items() if k!='recovery'},'recovery':dest,'encoding':'gzip; decoded bytes exact','disposition':'complete historical recovery; negative certification deferred' if r['path']!=oldnote and r['path']!=runner else 'canonical scoped port plus complete original recovery','canonical':note if r['path']==oldnote or r['path'].endswith('DERIVATION.md') else runner if r['path']==runner else None})
put(hist+'/manifest.json',json.dumps({'schema_version':2,'pr':8031,'head':inv['head'],'base':inv['base'],'files':rows},indent=2)+'\n')
put(hist+'/README.md','# PR8031 original recovery\n\nThe [manifest](manifest.json) records all 70 original paths, Git modes, blobs and SHA256 hashes. Each uniquely named gzip payload decodes to the exact original bytes, including full native/root proofs, original negative arguments, reviews and the initial R0 check failure. These are historical records, not current execution or certification. The manifest and archived payloads preserve original source independently of branch retention. This partial salvage leaves formal negative certification deferred; the original branch must remain available for that unresolved work.\n')
s=(O/oldnote).read_text(); body=s[s.index('# Finite transporter unitarity obstruction'):]
def replace(a,b):
 global body
 assert body.count(a)==1,a; body=body.replace(a,b)
replace('# Finite transporter unitarity obstruction and the actual PW cutoff error bridge','# Supplied Peter–Weyl compression, shell identities and energy/path bounds')
replace('2026-09-07. Written after the exposed candidate and prospective contract, before reading root\'s completed derivation. This is a precise matrix-unitarity obstruction plus an actual full-irrep cutoff approximation theorem. It is not a prohibition of finite-dimensional gauge-covariant quantum links.','The full native analytic argument is retained below with explicit supplied-model scope. Historical discovery and review provenance is preserved in the recovery archive; it is not a current certification.')
replace('## 1. A Cartan trace-square obstruction','## 1. Conditional Cartan trace-square identities')
replace('This is impossible. A first-trace argument alone would give zero and would fail. The opposite endpoint convention merely changes the sign of Tbar and gives the same positive square term. Exact endpoint covariance alone remains possible; exact matrix unitarity is the extra incompatible condition. In finite dimensions even one-sided isometry would imply unitarity and is equally excluded.','The offset dim(H) Tr T² is strictly positive under these hypotheses, whereas the displayed unitary similarity preserves the trace square. A first-trace argument alone would give zero and would fail. The opposite endpoint convention merely changes the sign of Tbar and gives the same positive square term. The original universal exclusion argument and its one-sided-isometry corollary remain exactly archived. Formal negative-classification certification is deferred; this does not refute the trace calculation.')
replace('; there is no operator-norm approximation to the full transporter on all cutoff inputs.','; this is an exact norm identity for the supplied compression. The associated negative convergence certification is deferred.')
replace('For R>=1 define','For a>0 and integer R>=1 define')
replace('The no-go concerns simultaneous finite dimension, exact fundamental endpoint covariance and exact matrix unitarity. It does not establish novelty of a generic quantum-link obstruction, nor prohibit unitary time evolution of a finite gauge Hamiltonian.','The historical negative argument concerns simultaneous finite dimension, exact fundamental endpoint covariance and exact matrix unitarity; its formal certification remains deferred. No novelty of a generic quantum-link obstruction or prohibition of unitary time evolution is certified here.')
replace("It explains why block38's exact unitary open-line trial identity cannot simply be copied to finite hardware with U replaced by U_R: the compressed transporter is not an isometry on all inputs, and energy-form errors need their own control.",'The contextual static-source trial uses an exact unitary open-line identity; transferring its energy estimate to compressed hardware requires an additional energy-form estimate.')
replace('Exact gauge covariance survives, low-energy transporter accuracy is available, and operator-norm unitarity convergence fails.','Exact gauge covariance and the supplied-model low-energy transporter estimate are retained. Broader negative convergence certification is deferred.')
header=s[:s.index('A finite nonzero link carrier')].replace('gauge_wilson_finite_transporter_unitarity_pw_defect_bounded_theorem_note_2026-09-07',pathlib.Path(note).stem.lower()).replace('Finite exact fundamental matrix-unitarity obstruction; actual full-irrep SU3 Peter–Weyl cutoff has sharp shell defect and energy-controlled distinct-link path approximation.','Supplied SU3 Haar compression identities, sharp shell eigenvalue and energy-controlled distinct-link path bounds; formal negative certification deferred.')
pref=f'''This bounded supplied-model result retains the complete compression, shell, kernel/eigenvalue and energy/path proof. Formal universal negative-classification and negative-convergence certification are **DEFERRED**, because the original N1 packet did not provide the required independent attack-family coverage. This procedural boundary does not invalidate the analytic identities. No axiom-selected carrier, hardware preparation or unbounded kinetic-form transfer is established.

The [actual cutoff and electric spectrum source]({pathlib.Path(parent).name}) supplies the full-irrep Haar cutoff and electric energy. The static-source trial is context only: `GAUGE_WILSON_UNIFORM_STATIC_SOURCE_ENERGY_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-07.md`.

The [finite runner](../{runner}) checks one actual R=1, 57×57 matrix (19 link states and 3 colors), with 16 mathematical checks and one resource check. Its [capture destination](../logs/runner-cache/{pathlib.Path(runner).stem}.txt) is an execution artifact, not an all-R or spatial-lattice proof. The [exact original recovery](work_history/review_loop/pr8031/README.md) preserves every original proof and failure. Historical native/root reviews are not a new independent certification; root's derivation was informed by the native stronger path bound.

'''
append='''
## Appendix A. Additional root-verification details

The original root proof also records the exponentiated conditional character identity on the Cartan torus: 3 chi_rho(g)=chi_rho(g) chi_fund(g), with chi_fund(g(t))=1+2cos(t) and chi_rho nonzero sufficiently near identity. This identity follows from the same conditional unitary similarity; its negative-classification certification is deferred with §1. The precise left-pullback convention is rho(g)f(V)=f(g^{-1}V); changing the inverse while retaining that representation would reverse noncommutative group composition.

For inverse link orientation, antifundamental fusion gives the same shell support, and a conjugate highest-column/row coefficient supplies the corresponding sharp witness. With K=-3 Delta/(2a), the shell energy is equivalently e_R=[ceil(3R²/4)+3R]/a=g_(R−1); the expectation bound can be capped by 1. The norm-one witness moves to increasing energy as R grows.

If all distinct path links start in their interiors P_(R−1), every shell expectation vanishes and path action is exact. The weaker telescoping estimate sqrt(L E_path/e_R) is valid but unnecessary; the proved projection estimate is sqrt(E_path/e_R). For p>0, the pure-state trace distance (one-half convention) between the exact output and normalized projected output is exactly sqrt(1−p). E_path<e_R is sufficient, not necessary, for p>0. An implementation still requires a channel or dilation and must price any postselection probability. These are supplied-state mathematical comparisons, not deterministic preparation claims.

## Appendix B. Applicability and deferred certification record

- N1: DEFERRED. No completed five-family negative-certification packet is asserted.
- N2: Historical root/native provenance is retained; it does not establish independent wall attacks.
- N3: The actual Haar full-irrep projection, supplied energy and distinct-link hypotheses are explicit; broader encodings are outside the positive result.
- N4: Conditional trace algebra and the exact supplied-compression norm identity are preserved; universal negative conclusions remain deferred.
- N5: Executed finite evidence is 16 mathematical checks plus one resource check on the 57×57 R=1 one-link fixture. Per-site and lattice-wide execution are not performed. All-R and path statements rely on the written proof.
- N6: The original R0 tautological-check failure and corrected vacuum-block check remain archived; no evidence is erased.
- N7: No axiom-selected representation, native preparation, repeated-link path bound or unbounded energy-form transfer is asserted.
- N8: Original reviews and present source preparation are not substituted for a completed negative-certification review. The unresolved original branch is retained.
'''
put(note,header+pref+body+append)
r=(O/runner).read_text(); original=r
pins={p:sha((W/p).read_bytes()) for p in [note,parent]}
insert='AUDIT_INPUT_PATHS = '+repr([note,parent])+'\n_SOURCE_ROOT = Path(__file__).resolve().parents[1]\n_INPUT_SHA256 = '+repr(pins)+'\nfor _input in AUDIT_INPUT_PATHS:\n    assert hashlib.sha256((_SOURCE_ROOT / _input).read_bytes()).hexdigest() == _INPUT_SHA256[_input], _input\n'
r=r.replace('started=_started\n',insert+'started=_started\n',1)
r=r.replace("print('TOTAL: '+str(expected))","print('TOTAL: PASS='+str(expected)+' FAIL=0')")
r=r.replace("    if sys.argv[1:] == ['--json']:","    _destination = Path(__file__).resolve().parents[1] / 'logs/runner-cache' / (Path(__file__).stem + '.json')\n    _destination.parent.mkdir(parents=True, exist_ok=True)\n    _destination.write_text(json.dumps(out, sort_keys=True, indent=2, allow_nan=False) + '\\n')\n    if sys.argv[1:] == ['--json']:")
r=r[:r.index('_emit(out, 17,')]+"_emit(out, 17, "+repr({'per_element':{'checks':5,'scope':'one-link matrix dimension, two Cartan tests, trace offset and R0 block'},'per_site':{'checks':0,'scope':'checked and not executed; no spatial-site resolution'},'per_mode':{'checks':4,'scope':'finite Gram Hermiticity/projection/rank and defect projection'},'per_block':{'checks':8,'scope':'one 57x57 block: defect rank/shell/interior/kernel/norm, energy-shell, fake identity and one resource check'},'lattice_wide':{'checks':0,'scope':'checked and not executed; all-R and distinct-link path claims use written proofs, not lattice execution'}})+")\n"
assert original[original.index('started=_started'):original.index('_emit(out, 17,')]==r[r.index('started=_started'):r.index('_emit(out, 17,')]
ast.parse(r); put(runner,r)
patch=''.join(difflib.unified_diff(s.splitlines(True),(W/note).read_text().splitlines(True),fromfile=oldnote,tofile=note))+''.join(difflib.unified_diff(original.splitlines(True),r.splitlines(True),fromfile=runner,tofile=runner))
(R/'drain8031-author-corrections-v1.patch').write_text(patch)
record={'schema_version':2,'pr':8031,'stage':'untracked author preparation; independent confirmation pending','base':subprocess.check_output(['git','-C',str(W),'rev-parse','HEAD'],text=True).strip(),'owner':'PR8031-author','source':[{'path':p,'sha256':sha((W/p).read_bytes())} for p in sorted(owned)],'original_dispositions':rows,'runtime_inputs':pins,'helpers':[],'proof_mapping':{'native':'complete sections 1–5 with explicit negative certification deferral; exact original archived','root':'shared full proof plus Appendix A unique character/convention/orientation/interior/trace-distance details; exact original archived'},'verification':{'mathematical_runner_region_byte_identical':True,'syntax_ast':'PASS','archive_roundtrip_count':len(rows)},'negative_certification':'DEFERRED; original branch retained; no mathematical refutation asserted','evidence_references':['drain8031-review.json','drain8031-original-manifest.json','drain8031-author-corrections-v1.patch']}
(R/'drain8031-author-prepared-v1.json').write_text(json.dumps(record,indent=2)+'\n')
plan={'pr':8031,'runner':runner,'timeout_seconds':180,'rss_limit_MiB':180,'basis':'Original declared limits retained; no capture performed. Fixed 57x57 exact SymPy matrices; seven principal square matrices U,Q,Tc,G,D,Pv,shell, each3249 entries, plus symbolic product temporaries; one57-vector and sparse output entries. No size-dependent grid allocation, dynamic helper or imported primary. Symbolic object overhead prevents claiming a numeric peak from entry count alone; watchdog required.','work':'Fixed nested3-valued construction, finite57-dimensional matrix products/simplifications;16 mathematical checks +1 resource.','json_destination':'logs/runner-cache/'+pathlib.Path(runner).stem+'.json','cache_destination':'logs/runner-cache/'+pathlib.Path(runner).stem+'.txt','runtime_inputs':pins,'mathematical_dependency':parent,'capture_authorized':False}
(R/'drain8031-resource-plan-v1.json').write_text(json.dumps(plan,indent=2)+'\n')
print(json.dumps({'owned_count':len(owned),'prepared_sha256':sha((R/'drain8031-author-prepared-v1.json').read_bytes())}))
