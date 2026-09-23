from pathlib import Path
import json,gzip,hashlib,subprocess,ast,difflib,re
R=Path('/private/tmp/review-drain-20260915');W=R/'drain-author-slot';O=R/'drain8168-originals';sha=lambda b:hashlib.sha256(b).hexdigest();head='c3bbf3758eb59b1d6c997389ae35738ce986dcbc'
assert json.loads((R/'drain-author-slot.json').read_text())['owner']=='PR8168-author';assert not subprocess.check_output(['git','-C',str(W),'status','--porcelain'])
inv=json.loads((R/'drain8168-manifest.json').read_text());n=next(x['path'] for x in inv if x['path'].startswith('docs/ADMISSIBILITY_'));p=next(x['path'] for x in inv if x['path'].startswith('scripts/'));hist='docs/work_history/review_loop/pr8168';owned=[]
def put(p,b):
 q=W/p;assert not q.exists();q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(b if isinstance(b,bytes) else b.encode());owned.append(p)
rows=[]
for i,e in enumerate(inv):
 b=(O/e['path']).read_bytes();h=e['head'];assert sha(b)==h['sha256'];assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==h['blob'];dest=f'{hist}/original-{i+1:03d}-{h["sha256"][:12]}.gz';put(dest,gzip.compress(b,mtime=0));assert gzip.decompress((W/dest).read_bytes())==b
 rows.append(dict(original_path=e['path'],original_mode=h['mode'],original_blob=h['blob'],original_sha256=h['sha256'],recovery=dest,encoding='gzip',canonical=e['path'] if e['path'] in [n,p] else None,disposition='scoped canonical port and exact historical recovery' if e['path'] in [n,p] else 'exact historical recovery; no overwrite of current-main shared source'))
put(hist+'/manifest.json',json.dumps(dict(schema_version=2,head=head,base='6dda46fc1af02827e9c6b64b2f7d05c381a3ce07',files=rows),indent=2)+'\n');put(hist+'/README.md','# PR8168 exact original recovery\n\nThe [manifest](manifest.json) binds all 27 original paths, modes, Git blobs and raw SHA256 hashes. Each gzip payload decodes to the complete original bytes: full T0–T7 proof, five historical control programs, outputs, failed adjacency and outward-arrow proposals, later untraced arrow-budget report, original cache and campaign records. Historical claims and author certificates are not current review authority. The manifest and archives preserve source independently of branch retention. Deferred threshold/route-exhaustion work retains the original branch.\n')
s=(O/n).read_text();r=(O/p).read_text();orig=s;origr=r
axiom='docs/MINIMAL_AXIOMS_2026-06-29.md';parent='docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md';eroder='docs/ADMISSIBILITY_RULE_STRONG_COUPLING_FORMATION_LAW_LEVEL_AUTOMATON_ERODER_METASTABILITY_ORDERED_PHASE_OBLIGATION_BOUNDED_THEOREM_NOTE_2026-09-15.md';static='docs/ADMISSIBILITY_RULE_STATIC_SIX_AXIS_REFLECTION_IDENTITIES_AND_CONDITIONAL_CONTOUR_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md'
# Exact bounded section replacements, never a generic Markdown-link rewrite.
a=s.index('## No-Go Discipline Gate');b=s.index('## Falsifiers',a)
s=s[:a]+'''## No-Go Discipline Gate

### N1 — Positive theorem, negative certification deferred
T0–T7 provide a positive theorem for the supplied process. The historical list checked parts of one contour construction; it is not five distinct alternative negative-proof families. No broad negative certificate or route-exhaustion conclusion is asserted.

### N2 — Historical controls
The exact archive retains the original control sources and outputs, including failed proposals. Historical author checks do not become independent wall proofs.

### N3 — Supplied process and imports
Positive weights, six-axis menu, constant initial plane, conditionally independent product updates and independent comparison noise are supplied. Compactness and extremal decomposition are mathematical imports with hypotheses stated under Imports.

### N4 — Parent boundary
Only the actual rule, axiom sentences and spatially invariant stationary-law correspondence are imported. The current static reflection result is conditional; no unconditional static phase is used.

### N5 — Resolution
per_element: finite kernel forms, derivatives, charge increments and fork sizes.
per_site: 216 candidate triples enumerated, 16 majority triples for fixed a tested for the deviation bound; four coupling thresholds.
per_mode: finite exhaustive backward cones, 1200 seeded random cones, structured seeds and 66103 finite trees; exact domains unchanged.
per_block: rational super-solution, bound at epsilon_0 and finite-chain Cesaro identity.
lattice_wide: checked and not executed; T4–T7 are written proofs, not a numerical infinite-lattice execution.

### N6 — Primitive boundary
No primitive selects the process, coupling or initial plane.

### N7 — Unknown threshold and improvements
Finite periodic simulations over finite times and floating fixed-point searches on a finite t-grid with a stopping cutoff are exploratory observations. They do not locate the infinite-system threshold or prove optimality of the count or arrow budget. No new simulation is used here.

### N8 — Preserved failures and open scope
The noiseless eroder and current static dissemination gap remain intact. The full original history and unresolved negative/optimization claims remain recoverable; no missing attack route is invented.

'''+s[b:]
a=s.index('## Review record');b=s.index('## Verification',a)
s=s[:a]+'''## Review record

The [exact original recovery](work_history/review_loop/pr8168/README.md) preserves all author/campaign records, full proofs and historical controls. The first cause graph allowed fork–fork adjacency and failed the edge bound; its corrected bipartite construction is retained. The outward-arrow proposal failed on 538 of the earlier 4308 explained trees and on 32 of an independent historical 3253-tree recount. The earlier sample's maximum a/f of 12/7 is a sample observation only. Later HANDOFF and OPPORTUNITY_QUEUE report 743 larger random trees, including a depth-12 a/f=7/3 example against the proposed a<=2f budget. The submitted files contain no seed/configuration or saved output for this later report; it is historical and unverified in this review, not a reconstructed witness or universal bound. All these failures concern particular constructions or candidate lemmas, not every improved contour method.

The original first depth-first count and its valid threshold 1/169869312 remain in the archive. The exact rational super-solution here is retained unchanged. The historical finite-grid floating search near 7.4 times 10^-6 and finite periodic simulations are exploratory only; neither establishes a true threshold nor excludes improving the count.

'''+s[b:]
a=s.index('*Placement.*');b=s.index('## No-Go Discipline Gate',a)
s=s[:a]+f'''*Placement.* The [level-automaton source]({Path(eroder).name}) S0 identifies spatially invariant stationary level laws with fully translation-invariant formation laws. The six laws constructed here have both invariances. Only this correspondence and the stated stability target are used; its deferred classifications are not imported. The current static result, `{Path(static).name}`, is conditional because site-reflection parity leaves a dissemination gap. Formation stability here does not depend on static order. The true threshold and intermediate coupling region remain open.

'''+s[b:]
# Remove campaign-specific wrappers while preserving analytic T0–T7 paragraphs.
s=s.replace("Block 12 (PR #8146) read",'The level-automaton source read').replace("The block-12 obligation S6 is closed at scope;",'The supplied stability obligation is proved at scope;')
a=s.index('target_blocker_text:');b=s.index('conditional_surface_status:',a)
s=s[:a]+'''target_blocker_text: "stability of the supplied noisy majority automaton"
source_of_blocker_text: source
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "six invariant formation laws at the explicit sufficient noise bound; true threshold and unconditional static order remain open"
'''+s[b:]
s=s.replace('three standard mathematical imports named at definition level','mathematical compactness and decomposition imports explicitly stated')
a=s.index('The axioms memo (');b=s.index('\nDeclared objects.',a)
s=s[:a]+f'''The [axioms memo]({Path(axiom).name}) supplies the four sentences quoted in the exact original recovery. The [finite-window product-rule source]({Path(parent).name}) supplies only the six-axis menu, positive product weights and one-site conditional. The process below additionally supplies independent level updates, a constant initial plane and independent comparison noise; these are not selected by the axioms. The level-automaton correspondence is used only with spatial invariance as stated in Placement.
'''+s[b:]
s=s.replace("(iii) the consequence for the campaign: both readings of the Admissibility rule, static (block 17) and formation (this note), order at strong coupling on `Z³`;",'(iii) six stationary formation laws under the supplied process, independently of the unresolved unconditional static phase;')
s=s.replace('What is new here:', 'The result established here:').replace('the obligation S6 of block 12 closed at scope','the supplied stability obligation proved at scope').replace("block 12's S1, S3 re-proved",'level-kernel identities re-proved').replace('(from block 12, re-proved)','(re-proved)')
s=s.replace('all `216` triples with at least two entries `a`','the 16 majority triples among 216 candidate triples for fixed `a`')
s=s.replace("between block 08's uniqueness region and this one",'between a weak-coupling uniqueness region and this sufficient region').replace("differs from block 01's conditional",'differs from the supplied product conditional')
s=s.replace('No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.','Mathematical compactness and extremal decomposition are explicit theorem imports; no physical selection follows from them.')
a=s.index('## Imports');b=s.index('## Review record',a)
s=s[:a]+'''## Imports

- The linked axiom memo and product-rule source supply the stated sentences, menu and conditional; positivity, synchronous conditionally independent updates, initial plane and comparison-noise law are explicit supplied conditions.
- T0–T6 are proved in full here: kernel algebra, coupling, explanation-tree construction, charge accounting, typed-tree lift, rational super-solution and union bound.
- Weak compactness of probability laws on the compact metrizable finite-alphabet configuration space M^{Z²}, together with the Feller property of this finite-range product kernel, supplies the subsequential Cesaro limit in T7. Translation commutation and invariant initial laws preserve spatial invariance.
- For the optional extremal-count conclusion, import barycentric decomposition of stationary probability laws for a Feller Markov kernel on this compact metrizable space into extreme stationary laws. The stationary-law set is nonempty, compact and convex; cylinder marginals are continuous affine functions. The six directly constructed invariant laws and their separation do not require this optional decomposition conclusion.
- Historical attribution only: Toom, Berman–Simon, Gács, Swart–Szabó–Toninelli and Bramson–Gray. No numerical threshold is imported from them; no exhaustive novelty claim is made.

'''+s[b:]
s=s.replace('  - minimal_axioms\n','  - minimal_axioms\n  - '+Path(eroder).stem.lower()+'\n')
s=s.replace('claim_type: bounded_theorem\n','claim_type: bounded_theorem\nbodyType: bounded_theorem\n',1)
s=s.replace('Executed with exact arithmetic: 22 checks, 13 mutations.','The paired runner defines 22 checks and 13 mutations; the archive preserves historical evidence. Fresh corrected-source capture is pending.')
s=s.replace('and exactly one of `C` and `Y_0` has its pole at `v`','and, when `v ∈ Y_0`, exactly one of `C` and `Y_0` has its pole at `v`').replace('So `#{X ∈ I(v)', 'When `v ∉ Y_0`, neither contributes at `v` and the other incident forks supply `|I(v)| − 1`. So `#{X ∈ I(v)')
s=s.replace('for every `ε ≤ ε_0 := 7/10⁶`','for every `0 ≤ ε ≤ ε_0 := 7/10⁶`').replace('≤ ε·R̄ < (391/100)·ε','≤ ε·R̄ ≤ (391/100)·ε')
s=s.replace('## Theorem T7 —', 'The middle bound is strict when ε>0; at ε=0 the probability bound is zero.\n\n## Theorem T7 —',1)
put(n,s)
# Preserve calculations; only metadata, pins and reporting/scoping text change.
r=r.replace('the exact maximum over the 216 triples with two entries a','the exact maximum over the16 majority triples among216 candidates for fixed a').replace('all 216 triples with two entries a','the16 majority triples among216 candidate triples for fixed a').replace('lattice_wide: T4-T7 proved','lattice_wide: checked and not executed; T4-T7 written proofs')
# Three runtime inputs remain the ones actually read by the primary; S0 is a mathematical premise separately.
pins={x:sha((W/x).read_bytes()) for x in [n,axiom,parent]}
r=r.replace('ROOT = Path(__file__).resolve().parents[1]','ROOT = Path(__file__).resolve().parents[1]\nEXPECTED_INPUT_SHA256 = '+repr(pins)+'\nAUDIT_RSS_LIMIT_MIB = 512')
r=r.replace('import random\n','import random\nimport hashlib\n')
r=r.replace('    checks = Checks()\n','    assert all(hashlib.sha256((ROOT / pth).read_bytes()).hexdigest() == EXPECTED_INPUT_SHA256[pth] for pth in AUDIT_INPUT_PATHS)\n    checks = Checks()\n')
r=r.replace("between block 08's uniqueness region and this one",'between a weak-coupling uniqueness region and this sufficient region').replace('No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.','Mathematical compactness and extremal decomposition are explicit theorem imports; no physical selection follows from them.')
r=r.replace("block 01's",'the product-rule source’s').replace('block 01', 'the product-rule source')
put(p,r);(W/p).chmod(0o755);ast.parse(r)
# Independently compare all computation ASTs, allowing changed string-only reporting text.
def science(t):
 out={}
 for x in ast.parse(t).body:
  if isinstance(x,(ast.FunctionDef,ast.ClassDef)) and x.name not in ['family_a','family_f','family_g','main']:
   class Strings(ast.NodeTransformer):
    def visit_Constant(self,n):return ast.copy_location(ast.Constant(value='<string>'),n) if isinstance(n.value,str) else n
   out[x.name]=ast.dump(Strings().visit(x),include_attributes=False)
 return out
assert science(origr)==science(r)
patch=''.join(difflib.unified_diff(orig.splitlines(True),s.splitlines(True),fromfile=n+'@original',tofile=n)) + ''.join(difflib.unified_diff(origr.splitlines(True),r.splitlines(True),fromfile=p+'@original',tofile=p));(R/'drain8168-author-corrections-v1.patch').write_text(patch)
source=[dict(path=x,sha256=sha((W/x).read_bytes()),mode=oct((W/x).stat().st_mode&0o777)) for x in sorted(owned)]
record=dict(schema_version=2,pr=8168,status='untracked author preparation; original reviewer confirmation pending',base=subprocess.check_output(['git','-C',str(W),'rev-parse','HEAD'],text=True).strip(),source=source,original_dispositions=rows,claim_dispositions=json.loads((R/'drain8168-dispositions.json').read_text())['claims'],runtime_inputs=pins,mathematical_parents=[dict(path=x,sha256=sha((W/x).read_bytes())) for x in [axiom,parent,eroder]],context=[dict(path=static,sha256=sha((W/static).read_bytes()))],verification=dict(computational_ASTs_preserved=list(science(r)),archive_roundtrips=27,primary_executed=False),formula_changes=['T6 nonstrict bound at epsilon0=0; strict only positiveepsilon','T3 prose clarifies Y0 contains-v case, identity unchanged'])
(R/'drain8168-author-prepared-v1.json').write_text(json.dumps(record,indent=2)+'\n');(R/'drain8168-author-source-freeze-v1.json').write_text(json.dumps(source,indent=2)+'\n')
plan=dict(runner=p,timeout_seconds=900,rss_limit_MiB=512,reason='Original900s limit retained. Historical cache reports1.44s, not new measurement. Peak live structures: up to66103 small frozenset trees and retained word-lift keys with <=5 vertices, plus old/new enumeration generations; Python tuple/set overhead conservatively hundreds of MiB, not dense lattice arrays. SymPy only small kernel identities and3x3 matrices. 512MiB proposed watchdog; no peak measurement inferred. Largest explanation cone depth8 has165 sites,1200 sequential random cases, finite polynomial dict5x5. No primary run.',json_output=None,stdout_TOTAL='PASS=22 FAIL=0',helpers=[],runtime_inputs=pins,mathematical_dependency_closure=record['mathematical_parents'])
(R/'drain8168-resource-plan-v1.json').write_text(json.dumps(plan,indent=2)+'\n');print(json.dumps({'owned':len(owned),'prepared_sha256':sha((R/'drain8168-author-prepared-v1.json').read_bytes())}))
