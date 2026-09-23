from pathlib import Path
import json,hashlib,gzip,shutil,subprocess,ast,difflib,re
R=Path('/private/tmp/review-drain-20260915');W=R/'drain-author-slot';O=R/'drain8170-original';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
assert json.loads((R/'drain-author-slot.json').read_text())['owner']=='PR8170-author'
assert git('rev-parse','HEAD')=='012c276a64c80cf5256d68fa7dbb06939586153b' and not git('status','--porcelain','--untracked-files=all')
m=json.loads((O/'manifest.json').read_text());originalnote=next(e['path'] for e in m['paths'] if e['path'].startswith('docs/ADMISSIBILITY'));originalrunner=next(e['path'] for e in m['paths'] if e['path'].startswith('scripts/'))
oldnote=(O/'source'/originalnote).read_text();oldrunner=(O/'source'/originalrunner).read_text()
notepath='docs/SPHERE_LEVEL_KERNEL_MOMENTS_WALK_LOCAL_LIMIT_AND_FINITE_PLANE_MIXING_BOUNDED_THEOREM_NOTE_2026-09-16.md';runnerpath='scripts/sphere_level_kernel_moments_walk_local_limit_finite_plane_mixing_2026_09_16.py';cid=Path(notepath).stem.lower();archivepath='docs/work_history/repo/review_feedback/pr8170-evidence';A=W/archivepath;assert not A.exists();(A/'kept').mkdir(parents=True)
entries=[];mapping=[]
for e in m['paths']:
 raw=(O/'source'/e['path']).read_bytes();mode,_,blob=e['head_entry'].split('\t')[0].split();assert hashlib.sha256(raw).hexdigest()==e['sha256'];assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==blob
 # Preserve readable proofs/code. Compress complete large generated topology and stdout with trailing blank lines; never trim originals.
 compress=e['path'].endswith('.txt') or e['path']=='docs/audit/data/citation_graph_manifest.json'
 name=Path(e['path']).stem+'-'+blob[:16]+Path(e['path']).suffix+('.gz' if compress else '')
 dest=A/'kept'/name;dest.write_bytes(gzip.compress(raw,mtime=0) if compress else raw);dest.chmod(0o644 if compress else int(mode[-3:],8))
 if compress:assert gzip.decompress(dest.read_bytes())==raw
 stored='kept/'+name;entries.append(dict(original_path=e['path'],original_mode=mode,git_blob=blob,raw_sha256=e['sha256'],encoding='gzip' if compress else 'identity',stored_path=stored,stored_sha256=sha(dest)))
 final=notepath if e['path']==originalnote else runnerpath if e['path']==originalrunner else None
 disposition='Narrowed and corrected canonical mathematical source; complete exact original retained' if final else 'Deferred historical science and provenance; all failures/NaNs/observables retained, not current execution or authority'
 if e['path']=='docs/audit/data/citation_graph_manifest.json':disposition='Historical topology superseded; preserve current-main map, coordinator rebuilds final graph'
 mapping.append(dict(original_path=e['path'],original_mode=mode,original_blob=blob,original_sha256=e['sha256'],recovery=archivepath+'/'+stored,recovery_encoding=entries[-1]['encoding'],disposition=disposition,final_path=final,final_sha256=None))
(A/'archive-manifest.json').write_text(json.dumps(dict(schema_version=1,revision=m['head'],entries=entries),indent=2)+'\n')
def section(name,end):return oldnote.split('## '+name+'\n',1)[1].split('## '+end+'\n',1)[0]
t1=section('Theorem T1 — the kernel','Theorem T2 — gain one')
t1=t1.replace("and `A'(κ) ≤ 1/(3 + κ²)`.","and `A(κ) < 1`.")
a=t1.index("(b) `A'(κ)",t1.index('**Proof.**'));b=t1.index('(c) At the aligned plane',a)
t1=t1[:a]+"""(b) For `κ > 0`, define `f(κ) = (κ² + 3)sinh κ − 3κ cosh κ`. Expanding the entire functions gives
`f(κ) = Σ_{n≥2} 4n(n−1) κ^{2n+1}/(2n+1)! > 0`:
the coefficient is `[ (2n)(2n+1) + 3 − 3(2n+1) ]/(2n+1)! = 4n(n−1)/(2n+1)!`, with the constant/linear/cubic terms zero.
Dividing `f(κ)>0` by `3κ sinh κ>0` gives `A(κ)<κ/3`.
Also `A'(κ)=1/κ²−1/sinh²κ>0` since `sinh κ>κ`, and `A(0+)=0`, so `A>0`.
Since the kernel has a strictly positive continuous density on the sphere and `w<1` almost surely, `A=E[w]<1`.
The former derivative upper bound is false: at `κ=1`, `sinh²1 > 1+1/3+2/45=62/45>4/3`, whence `A'(1)>1/4`.
This counterexample is retained as a rejection control; it is not used to infer an upper derivative bound. """+t1[b:]
t2="""**Statement.** Near the pole, `s=(θ,√(1−|θ|²))` and `s_i=(θ_i,√(1−|θ_i|²))`. The exponent has expansion
`β s·Σ_i s_i = 3β − (β/2)Σ_i|θ−θ_i|² + O(4)`.
Its quadratic maximum is the average `Σ_i θ_i/3`, with Hessian `−3β I`.
The exact conditional transverse mean has derivative `A(3β)Σ_i θ_i/3`, not gain one. The normalized mean direction has derivative `Σ_i θ_i/3`. The exact aligned one-step variance is `A(3β)/(3β)` per component.

**Proof.** `s·s_i=θ·θ_i+√(1−|θ|²)√(1−|θ_i|²)=1−|θ−θ_i|²/2+O(4)`; summing proves the expansion. The squared-distance sum has gradient zero at the average and Hessian `6I`, so the exponent has negative Hessian and a maximum there. Put `S=Σ_i s_i`. Its transverse part is `Σ_i θ_i`, its longitudinal part is `3+O(|θ_i|²)`, and `|S|=3+O(|θ_i|²)`. Substitution into the exact mean `A(β|S|)S/|S|` gives transverse derivative `A(3β)Σ_i θ_i/3`; normalization divides out the nonzero mean length. For a common rotation by angle `h`, the exact transverse mean is `A(3β)sin h`, whose derivative is `A(3β)<1`. Rotational covariance rotates this shorter mean vector, not a unit vector. The variance follows from the two equal transverse entries of the second-moment tensor at `κ=3β`. ∎

The gain-one additive-noise recursion below is separately supplied. Matching its noise variance to this one-step variance is a declared modeling choice. It does not derive an exact nonlinear evolution equation.

"""
t3=section('Theorem T3 — the level walk\'s constant','Theorem T4 — finite planes forget')
t4=section('Theorem T4 — finite planes forget','Theorem T5 — the linearized field').split('*Reading.*')[0]
t5=section('Theorem T5 — the linearized field','Executed: the nonlinear law simulated (frontier discovery, not proved)').split('*Reading.*')[0]
t5=t5.replace('the linearized field has no stationary law with finite variance; and the second-order proxy `e^{−v_t}` of the magnetization decays like `t^{−γ(β)}`.','the declared scalar proxy `e^{−v_t}` is of order `t^{−γ(β)}`. This proxy is not asserted to equal any nonlinear sphere magnetization.')
t5=t5.replace('`γ(β) → √3/(4πβ)`','`γ(β) ∼ √3/(4πβ)`')
neg='A stationary law with finite variance would give, started from it, a variance at level `t` at least `v_t` (the noise terms of levels `1..t` are independent of the initial field), impossible as `v_t → ∞`. '
assert neg in t5;t5=t5.replace(neg,'')
t5=t5.replace('The bounds are T3 with `Σ_{k≥1}(27/k² + e^{−√k/7}) < 150`.','The bounds are the local-limit theorem with `P_0=1` explicitly included: `1 + 27π²/6 + 98 < 150`, since the decreasing exponential tail is bounded by `∫_0^∞ e^{−√x/7} dx=98`. The lower bound may discard the positive `P_0` term. Summability of the two-sided error gives the stated logarithmic asymptotic. Since `A(3β)→1`, the displayed large-β equivalence follows.')
objects=section('Premises and declared objects','Prior art and what is new').split('Declared objects.\n',1)[1]
objects=objects.replace('**The linearized field.**','**The supplied auxiliary field.**').replace("(the unsoldered reading of the qubit, block 18's menu)","(a supplied continuous menu)").replace("(the static law of this weight is blocks 19–23's object)","(a supplied coupling family)")
objects=objects.split('- **The six-axis side-by-side.**')[0]
head=f'''---
claim_id: {cid}
claim_type: bounded_theorem
claim_scope: "Supplied sphere level kernel: exact moments and conditional mean Jacobian; three-step planar walk local-limit and harmonic bounds; finite periodic-plane minorization and invariant law; separately supplied additive-noise recursion variance and scalar proxy. No nonlinear infinite-plane decay or physical selection claim."
upstream_dependencies: [minimal_axioms, admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06]
runner: {runnerpath}
---

# Sphere level-kernel moments, walk local limits and finite-plane mixing

**Type:** bounded_theorem
**Status:** conditional-support; source review and execution remain separate from audit status.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
artifact_role: theorem_plus_decisive_artifact
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Scope and premises

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply lattice, site possibility, local admissibility and records. The [finite-window product-rule classification](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md) supplies records-only product-rule vocabulary. Neither selects the continuous sphere menu, exponential pair weight, β, level schedule, conditional independence across a level, or a physical stochastic process. These are the explicit conditions below.

The proof uses sphere integration, convergent power series, Parseval on the torus, Gaussian integration, independent-noise variance addition, the tower property, and uniform minorization for a Markov kernel. These mathematical tools are disclosed; no empirical fit enters any theorem. Complete originals, attempted routes and raw outputs are preserved in [historical recovery](work_history/repo/review_feedback/pr8170-evidence/README.md).

## Declared objects

'''
end=f'''## Six-axis finite conditional identities

For the supplied six-point menu `{{±e_1,±e_2,±e_3}}`, assign pair weights `p=e^β`, `q=e^{{−β}}`, `r=1` for equal, antipodal and orthogonal records. With an aligned target value and respectively three equal predecessors, two equal plus one antipodal, or two equal plus one orthogonal, direct enumeration gives target weights `p³`, `p²q`, `p²r` and total weights `p³+q³+4r³`, `pq(p+q)+4r³`, `r(p²+q²)+r²(p+q)+2r³`. Subtracting their normalized probabilities from one yields
`(e^{{−3β}}+4)/(e^{{3β}}+e^{{−3β}}+4)`,
`(e^{{−β}}+4)/(e^β+e^{{−β}}+4)`, and
`(e^{{−2β}}+e^β+e^{{−β}}+2)/(e^{{2β}}+e^{{−2β}}+e^β+e^{{−β}}+2)`.
For the aligned triple the deviation is below `1/1600` at β=3 and below `1/10^7` at β=6, using the exponential series lower bounds. These are one-site identities, not infinite-time simulation claims.

## Boundary and recovery

Finite-plane minorization supplies the displayed contraction rate. It supplies neither a βL² nonlinear memory scale nor a lower bound on memory time. The time/size limits are not interchanged. The separately supplied auxiliary model does not determine the effect of cubic nonlinear terms. No nonlinear exponent ordering or asymptotic phase comparison follows from the archived histories.

Current-main context has changed since the original packet: the six-axis formation result now has a reviewed T0–T7 construction under its stated small-noise assumptions. The static six-axis reflection/contour result remains conditional. Neither is a premise of this sphere proof; the former four-cell settled memory map is withdrawn. Their exact paths and hashes are recorded as context in the author input plan, without adding theorem dependencies here.

The complete auxiliary finite-variance contradiction is retained readably in the recovery appendix. Its conditional mathematics is not rejected; formal negative certification and separate active promotion are deferred. Historical nonlinear decay/exponent conjectures and the time-dependent twist entropy obligation remain open, with branch recovery retained. Historical fitting scripts are not promoted: missing split inputs and absent projections are not manufactured.

## No-Go Discipline Gate

### N1 — Actual routes and limits
The historical five entries are diagnostics/attempts, not five closed independent attacks: later plateau remains open; finite-size exclusion was unsupported and withdrawn; sampler comparisons are finite diagnostics; the fixed-twist entropy outline leaves time-dependent twists and terminal entropy control open; exponent ordering is contradicted by retained historical rows. No broad negative certification is claimed. Finite-plane convergence is the direct corollary of the explicit uniform minorization proved above, not a route no-go.

### N2 — Premise independence
No repository wall is imported. The sphere kernel, β>0, finite periodic geometry and level-product kernel are supplied together as the finite-plane theorem's hypotheses. No unsupported independence certificate is issued.

### N3 — Hidden conditions
The auxiliary recursion additionally requires independent centered noise of the declared finite variance, independent of the initial field. It is not the exact nonlinear conditional mean map.

### N4 — Dependency roles
Only the two linked authorities supply framework and finite-product vocabulary. All moment, walk and finite-plane arguments are written here. Historical phase/simulation comparisons and certificates confer no current authority.

### N5 — Resolution
The runner checks symbolic moments, finite coefficient identities and rational enclosures; finite path enumeration and return sums through k=150; symbolic one-site/minorization identities; auxiliary variance constants. General local-limit and invariant-law results have written proofs. No nonlinear simulation or infinite-plane execution is part of this corrected primary. Exact execution counts belong to its future captured stdout, not this preparation.

### N6 — Open choices
No new axiom or primitive is proposed. Selecting a physical menu, coupling or formation schedule remains outside this supplied model.

### N7 — Strong alternative
Finite histories can be compatible with later plateaus, size-dependent behavior or nontrivial infinite-plane laws. Those possibilities are not ruled out here. The finite-plane theorem and auxiliary variance identity retain their own stated domains.

### N8 — Historical comparisons
The former equilibrium analogy and fixed-twist outline do not close a nonequilibrium infinite-plane theorem. The corrected current-main formation result concerns its own six-axis model and threshold. No echo between these results supplies the missing sphere argument.

## Verification

Paired [exact runner](../{runnerpath}) retains the complete finite return-sum fixtures and exact rational enclosures. Future cache path: `logs/runner-cache/{Path(runnerpath).stem}.txt`; JSON uses the same stem under `logs/runner-cache`. No cache is asserted present by this source preparation.

```bash
python3 {runnerpath}
python3 {runnerpath} --list-mutations
```

The original 14 mutation sources remain recoverable. Twelve mathematical mutation names remain active; two prose-policy mutations are retired with the old prose scanner, and two decisive new mathematical controls cover the corrected series coefficient and exact mean gain. No mutation census has been executed on this source. The inherited 900-second cap is retained, with a proposed external 768 MiB process-tree cap for SymPy and the fixed exact k≤150 workload.
'''
newnote=head+objects+'\n## Kernel moments and strict mean bound\n\n'+t1+'## Conditional mean derivative and quadratic mode\n\n'+t2+"## Level-walk local-limit constant (historical proof label T3)\n\n"+t3+'## Finite periodic-plane mixing (historical proof label T4)\n\n'+t4+'The displayed finite-plane rate is the only nonlinear memory bound asserted here.\n\n## Supplied auxiliary-field variance (historical proof label T5)\n\n'+t5+end
(W/notepath).write_text(newnote)
# Appendices preserve complete valid argument while explicitly outside current claim authority.
(A/'DEFERRED_SCIENCE.md').write_text('''# Deferred scientific conclusions and historical diagnostics

This appendix is recovery, not a live theorem dependency or a formal negative PASS. Preserve the original PR head branch while unique science remains deferred.

## Auxiliary finite-variance obstruction: complete conditional proof

For the separately supplied gain-one average recursion on Z², with independent centered noise of variance σ²>0, independent of the initial field, suppose a stationary law had finite variance at every site. Unfold t steps at a fixed site. Its new-noise contribution has variance `v_t=σ²Σ_{k<t}P_k`; this noise is independent of the initial-field contribution, which has nonnegative variance. Thus that site's stationary variance is at least v_t for every t. The local-limit/harmonic proof gives v_t→∞, a contradiction. The finite linear combination of initial coordinates has finite variance under the stated hypothesis. This is a valid conditional mathematical argument for this auxiliary recursion, not for the nonlinear sphere model. Its formal negative packet/active promotion remains deferred; reopening requires an honestly complete scoped packet and independent review, not invented routes.

## Failed twist route and nonlinear scope

The original fixed in-plane twist φ(x_perp) changes conditional weights through spatial twist differences. Its outlined entropy cost accumulates over T levels. That fixed-twist observation does not exclude T-dependent twists, joint space/time limits or another terminal entropy bound. The terminal obligation remains open. Nonlinear infinite-plane loss of initial magnetization, its exponent, a βL² memory scale, and an ordering of all nonlinear decay exponents against the auxiliary γ are deferred. The conjectures remain recoverable in full original source; the unsupported universal extrapolations are withdrawn from current claims, not replaced by the opposite theorem.

## Historical observations and missing materialization

The raw sphere controls record |m| and m_z every 500 levels in their 20000-level runs; the refuter β12 history records only |m|. Its missing projection cannot be recovered from the present source that now prints m_z. The fit chooses m_z when available and otherwise |m|, so its rows mix observables explicitly. The original fit globs nonexistent split filenames; it is preserved but is not promoted as a reproducible current parser. Reopening requires a deterministic pinned parser/materialization of existing concatenated sources and failure on absent expected series, never fabricated split inputs or reruns replacing the old history.

All rows survive, including β12 refuter slopes 0.0076 and 0.0103 below γ≈0.011167, β24 early slope 0.0055 below γ≈0.00566, negative fitted slopes for small planes, negative m_z and NaNs. Reported norm-minus-projection discrepancies reach 0.01189, contradicting the old <10^-3 blanket statement. The six-axis output samples every 75 levels and rounds to five decimals; 1.00000 at sampled times is not an infinite-time zero-dissent theorem. A 512² plane has 262144 sites; 256²/20000=3.2768. No plateau exclusion, monotonic decay, finite-size exclusion or asymptotic exponent inference is made from these finite histories.

## Original route dispositions

1. Later plateau: open; finite records do not exclude it.
2. Finite-size effect: old exclusion unsupported; size/time interchange open.
3. Sampler comparison: finite diagnostics retained with source/output mismatch noted.
4. Fixed-twist entropy: unsuccessful outline; time-dependent/terminal control open.
5. Exponent comparison: universal ordering contradicted by preserved rows; no certification.

These five entries are not five independent closed routes. No formal negative certification is inferred from their number.
''')
readme='''# Exact historical recovery

All 25 original source paths at `'''+m['head']+'''` retain distinct mode, Git blob and raw SHA-256 identities in [archive-manifest.json](archive-manifest.json). The complete original proof, computational programs, 14 mutation definitions, raw NaNs/negative histories and campaign context remain recoverable. Historical certificates, cache PASS text and topology are not current scientific authority. Current-main shared boards and maps are not overwritten.

[Deferred science and corrected historical interpretation](DEFERRED_SCIENCE.md) preserves the complete auxiliary obstruction argument and unresolved nonlinear/twist obligations. Formal negative certification is withheld; no missing inputs or new simulation history are manufactured. Branch retention is required.

Plain proof/code files retain exact bytes and modes. Stdout and the large generated topology use deterministic gzip with mtime 0; decompression reproduces every byte, including blank lines and NaNs. Storage is explicitly distinguished from raw identity.

## Original paths

'''
for e in entries:readme+='- `'+e['original_path']+'`: [exact '+e['encoding']+' recovery]('+e['stored_path']+').\n'
(A/'README.md').write_text(readme)
# Runner: retain arithmetic helpers and all B-E fixture domains, replace only evidenced incorrect proof logic and reporting/metadata.
s=oldrunner
start=s.index('"""');stop=s.index('"""',start+3)+3;s=s[:start]+'''"""Exact supplied sphere-kernel and walk controls. Auxiliary recursion is separately supplied.
No nonlinear simulation or historical fit execution. Exact arithmetic and SymPy only.
"""'''+s[stop:]
s=s.replace('import re\n','import re\nimport hashlib, json\n')
s=s.replace('AUDIT_TIMEOUT_SEC = 900','AUDIT_TIMEOUT_SEC = 900\nAUDIT_MEMORY_MB = 768').replace(originalnote,notepath).replace(Path(originalnote).stem.lower(),cid)
inputpaths=[notepath,'docs/MINIMAL_AXIOMS_2026-06-29.md','docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md'];pins={p:sha(W/p) for p in inputpaths}
s=s.replace('ROOT = Path(__file__).resolve().parents[1]','EXPECTED_INPUT_SHA256 = '+repr(pins)+'\nROOT = Path(__file__).resolve().parents[1]')
s=s.replace('    "claim_order_injected": "F",\n    "claim_classical_name_in_theorem": "F",','    "positive_series_coefficient_wrong": "B",\n    "exact_mean_gain_wrong": "C",')
s=s.replace('        self.passed = 0','        self.results = []\n        self.passed = 0').replace('        if ok:\n','        self.results.append(dict(tag=tag, passed=bool(ok), detail=msg))\n        if ok:\n',1)
s=s.replace('all(Path(ROOT, p).exists() for p in AUDIT_INPUT_PATHS), "all declared inputs exist"','all(Path(ROOT, p).exists() and hashlib.sha256(Path(ROOT,p).read_bytes()).hexdigest()==EXPECTED_INPUT_SHA256[p] for p in AUDIT_INPUT_PATHS), "all three declared inputs match exact source/parent pins"')
a=s.index('    # A(kappa) < kappa/3:');b=s.index('    encl =',a)
s=s[:a]+'''    # Positive entire-series argument for f(k)=(k^2+3)sinh(k)-3k cosh(k).
    n = sp.symbols("n", integer=True, positive=True)
    coefficient_numerator = (2*n)*(2*n+1)+3-3*(2*n+1)
    expected = 4*n*(n-1)
    if mut("positive_series_coefficient_wrong"):
        expected = 4*n*(n+1)
    coefficient_identity = sp.expand(coefficient_numerator-expected)==0
    f = (k**2+3)*sp.sinh(k)-3*k*sp.cosh(k)
    ser=sp.series(f,k,0,16).removeO()
    series_ok=all(ser.coeff(k,2*j+1)==sp.Rational(4*j*(j-1),factorial(2*j+1)) for j in range(0,7))
    positive=all(Fraction(4*j*(j-1),factorial(2*j+1))>0 for j in range(2,21))
    bridge=sp.simplify((f/(3*k*sp.sinh(k))-(k/3-(sp.coth(k)-1/k))).rewrite(sp.exp))==0
    slope=Fraction(1,3)
    if mut("langevin_bound_wrong"):
        slope=Fraction(1,4)
    pts=[Fraction(1,10),Fraction(1,2),Fraction(1),Fraction(2),Fraction(3),Fraction(6),Fraction(9),Fraction(18),Fraction(36),Fraction(72)]
    below=all(A_bounds(kp)[1]<slope*kp for kp in pts)
    checks.check("B2",coefficient_identity and series_ok and positive and bridge and below,"Positive-series coefficient 4n(n-1)/(2n+1)! proves f>0 for k>0 and A<k/3; ten original rational enclosure fixtures retained")
    checks.check("B4",Fraction(1)+Fraction(1,3)+Fraction(2,45)>Fraction(4,3),"At k=1, sinh^2(1)>62/45>4/3 gives A_prime(1)>1/4; historical derivative upper bound rejected")
'''+s[b:]
s=s.replace('the minimizer of the quadratic form is the average','the maximum of the quadratic exponent is the average').replace('the minimizer is the average of the three (gain one)','the maximum is the average of the three (mode gain one, not exact mean gain)')
a=s.index('\n\n# ============================================================================================ family D')
s=s[:a]+'''
    h=sp.symbols("h",real=True)
    gain=sp.coth(3*beta)-1/(3*beta)
    target_gain=sp.Integer(1) if mut("exact_mean_gain_wrong") else gain
    common=sp.simplify(sp.diff(gain*sp.sin(h),h).subs(h,0)-target_gain)==0
    # Independent formal first-order expansion of exact A(beta*|S|) S/|S|.
    a1,a2,a3=sp.symbols("a1 a2 a3",real=True)
    S=sp.Matrix([h*(a1+a2+a3),0,sum(sp.sqrt(1-h*h*z*z) for z in (a1,a2,a3))])
    length=sp.sqrt(S.dot(S))
    mean=(sp.coth(beta*length)-1/(beta*length))*S[0]/length
    jac=sp.simplify(sp.diff(mean,h).subs(h,0)-target_gain*(a1+a2+a3)/3)==0
    checks.check("C2",common and jac,"Exact common-rotation mean gain A(3 beta), Jacobian A(3 beta)/3 times transverse predecessor sum; gain-one auxiliary model is separate")
'''+s[a:]
s=s.replace('upper_const = 27 * PI_HI ** 2 / 6 + 98 < 150','upper_const = 1 + 27 * PI_HI ** 2 / 6 + 98 < 150').replace('the upper error sum 27 pi^2/6 + 98 is below 150','the upper sum including P0 is 1 + 27 pi^2/6 + 98 < 150')
a=s.index('# ============================================================================================ family F');b=s.index('# ============================================================================================ main',a)
s=s[:a]+'''# ============================================================================================ scope reporting
N5_LINES = (
    "per_element: executed — symbolic kernel moments, positive-series coefficients, ten rational bound fixtures and quadratic exponent",
    "per_site: executed — exact mean Jacobian, one-site recursion and minorization identities; finite six-axis conditional deviations",
    "per_mode: executed — paths through k=6, return sums through k=150, symbolic Gaussian integrals; no physical spectrum",
    "per_block: executed — harmonic deficit through 150 and auxiliary variance coefficient at four beta values",
    "lattice_wide: checked and not executed — general local-limit and finite-plane results use written proofs; no nonlinear infinite-plane simulation or phase inference",
)

def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)


'''+s[b:]
s=s.replace('    family_f(checks, texts[0])\n','')
s=s.replace('    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")','''    output=ROOT/'logs'/'runner-cache'/(Path(__file__).stem+("--"+ACTIVE_MUTATION if ACTIVE_MUTATION else "")+'.json')
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(dict(checks=checks.results,passed=checks.passed,failed=checks.failed,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),input_sha256=EXPECTED_INPUT_SHA256,mutation=ACTIVE_MUTATION),indent=2)+'\\n')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")''')
s=s.replace('# float-scan-marker-line','')
compile(s,runnerpath,'exec');(W/runnerpath).write_text(s);(W/runnerpath).chmod(0o755)
for row in mapping:
 if row['final_path']:row['final_sha256']=sha(W/row['final_path'])
# External author records, never passed off as scientific execution.
def dump(name,value):
 p=R/name;assert not p.exists();p.write_text(json.dumps(value,indent=2)+'\n');return p
mappingp=dump('drain8170-author-full-mapping-v1.json',mapping)
diff=''.join(difflib.unified_diff(oldnote.splitlines(True),newnote.splitlines(True),fromfile=originalnote,tofile=notepath))+''.join(difflib.unified_diff(oldrunner.splitlines(True),s.splitlines(True),fromfile=originalrunner,tofile=runnerpath))
(R/'drain8170-author-correction-v1.diff').write_text(diff)
oldasts={n.name:ast.dump(n,include_attributes=False) for n in ast.parse(oldrunner).body if isinstance(n,(ast.FunctionDef,ast.ClassDef))};newasts={n.name:ast.dump(n,include_attributes=False) for n in ast.parse(s).body if isinstance(n,(ast.FunctionDef,ast.ClassDef))}
identical=[k for k in oldasts if oldasts[k]==newasts.get(k)]
assert section('Theorem T3 — the level walk\'s constant','Theorem T4 — finite planes forget') in newnote
assert section('Theorem T4 — finite planes forget','Theorem T5 — the linearized field').split('*Reading.*')[0] in newnote
preserve=dump('drain8170-author-preservation-v1.json',dict(originals=25,raw_sha_blob_verified=True,unchanged_function_asts=identical,complete_local_limit_proof_literal=True,complete_finite_plane_proof_literal=True,formula_changes=['Replace false derivative upper-bound argument with positive-series identity; retain exact counterexample','Correct exact mean gain and quadratic maximum; auxiliary model explicit','Include P0=1 in upper summation','Gamma asymptotic equivalence, proxy not nonlinear observable'],retired_mutations=['claim_order_injected','claim_classical_name_in_theorem'],added_mutations=['positive_series_coefficient_wrong','exact_mean_gain_wrong'],all_original_mutation_sources_recoverable=True,primary_runs=0,simulation_runs=0,mutation_runs=0))
paths=git('ls-files','--others','--exclude-standard').splitlines();snapshot=R/'drain8170-prepared-v1-source';assert not snapshot.exists();snapshot.mkdir();f=[]
for path in paths:
 p=W/path;q=snapshot/path;q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q);f.append(dict(path=path,sha256=sha(p),mode=oct(p.stat().st_mode&0o777),immutable_copy=str(q)))
freeze=dump('drain8170-prepared-v1-source-freeze.json',dict(files=f,count=len(f)))
prepared=dump('drain8170-author-prepared-v1.json',dict(status='UNTRACKED AUTHOR PREPARATION; ORIGINAL REVIEWER AFFECTED CONFIRMATION REQUIRED',owner='PR8170-author',base=git('rev-parse','HEAD'),original_head=m['head'],original_merge_base=m['merge_base'],notes=[dict(path=notepath,sha256=sha(W/notepath))],runners=[dict(path=runnerpath,sha256=sha(W/runnerpath))],archive_manifest=dict(path=archivepath+'/archive-manifest.json',sha256=sha(A/'archive-manifest.json')),deferred_science=dict(path=archivepath+'/DEFERRED_SCIENCE.md',sha256=sha(A/'DEFERRED_SCIENCE.md')),source_files=len(f),originals=25,branch_retention_required=True,primary_runs=0,mutations=0,simulations=0,staged=False,original_report=dict(path=str(R/'drain8170-review-original.json'),sha256=sha(R/'drain8170-review-original.json'))))
print(json.dumps(dict(prepared_sha256=sha(prepared),freeze_sha256=sha(freeze),source_files=len(f),preservation_sha256=sha(preserve),identical_function_asts=identical),indent=2))
