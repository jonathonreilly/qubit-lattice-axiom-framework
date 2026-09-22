from pathlib import Path
import json,re,ast
r=Path('/private/tmp/review-drain-20260915');w=r/'drain-author-slot';inv=next(x for x in json.load(open(r/'drain8153-original-inventory.json')) if x['number']==8153);op=next(e['path'] for e in inv['original_paths'] if e['path'].startswith('docs/ADMISSIBILITY'));rp=next(e['path'] for e in inv['original_paths'] if e['path'].startswith('scripts/'));s=(r/'drain8153-originals/8153'/op).read_text();runner=(r/'drain8153-originals/8153'/rp).read_text();new='docs/ADMISSIBILITY_RULE_SPHERE_STATIC_LAW_ZERO_FIELD_COMPONENT_FOURIER_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md'
def change(t,b):
 global s
 s=re.sub(r'(?ms)^## '+re.escape(t)+r'\n.*?(?=^## |\Z)','## '+t+'\n\n'+b.strip()+'\n\n',s)
s=re.sub(r'(?m)^claim_id:.*$','claim_id: '+Path(new).stem.lower(),s)
s=re.sub(r'(?m)^claim_scope:.*$','claim_scope: "Supplied uniform-sphere nearest-neighbour exponential static law on even three-dimensional tori: Legendre positivity and real reflection form; finite Gaussian domination explicitly imported with normalized nearest-neighbour interaction; component infrared and zero-field rotation-generator bounds; controlled magnetization-square liminf and two-sided Fourier bounds along every nonzero limiting momentum sequence. No selected extremal-state transverse channel, pointwise real-space decay, physical identification or universal exclusion of other models is claimed."',s)
s=re.sub(r'(?m)^# .*$', '# Sphere static law: zero-field component Fourier bounds',s)
change('Result up front','''For the supplied sphere-spin static model, a precise finite-volume Gaussian-domination import gives an upper bound on each zero-field component structure factor. The rotation-generator argument gives a lower bound in terms of the finite-volume squared total magnetization. Together with the sum rule and a controlled small-momentum limit, these give the two-sided Fourier bounds stated below.

The finite torus law is rotation invariant: all three components are equivalent, and no magnetization direction is selected. These Fourier bounds do not identify an extremal-state transverse correlator, pointwise real-space `1/r` decay, or a physical gravity observable. They do not exclude any formation or discrete-spin model.

The original shifted-spin argument omitted variable norm factors and did not prove Gaussian domination. That argument and all original controls remain byte-exact in [the recovery manifest](work_history/review_loop/pr8153/original-manifest.json). Gaussian domination is now a declared mathematical import, not a claimed new proof.''')
change('Machine status and trace','''```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
artifact_role: theorem
next_trace_action: "Retain supplied-model zero-field component Fourier bounds; physical identification and negative classifications remain deferred."
conditional_surface_status: "Uniform sphere measure, positive exponential nearest-neighbour coupling, even periodic three-dimensional torus; Gaussian domination imported with explicit normalization."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
No negative certificate or gravity-channel identification is issued.''')
s=s.replace('the static reading of the rule (block 01 on `main`); the product rule with the','the static law explicitly defined below; the product rule with the')
importtext='''

**Gaussian-domination import.** Theorem 4.6, printed pages 40–41, of
[Marek Biskup, Reflection Positivity and Phase Transitions in Lattice Spin Models](https://www.math.ucla.edu/~biskup/PDFs/papers/Prague-School.pdf)
is load-bearing mathematics. Use its nearest-neighbour interaction, an even periodic torus, the identical compact single-site probability measure `dσ` on `S²⊂R³`, and nonnegative theorem parameter `b`. With ordered nearest-neighbour weights `J_xy=1/6` (periodized with multiplicities on side two), its twisted partition function has exponent `−b Σ_{x,y}J_xy |s_x−s_y+h_x−h_y|²` and is maximal at constant `h`. Set `b=3β/2` and `h_x=−φ_x e`. The ordered sum counts each bond twice, so the exponent becomes `−(β/2)Σ_{⟨xy⟩}|s_x−s_y−(φ_x−φ_y)e|²`, exactly the object below. No arbitrary site-dependent measure or single-site-factor extension is imported.
'''
s=s.replace('## Prior art and what is new',importtext+'\n## Prior art and what is new')
change('Prior art and what is new','''The infrared method is established mathematical work of Fröhlich–Simon–Spencer and Fröhlich–Israel–Lieb–Simon. Biskup's Gaussian-domination theorem is explicitly used above. The zero-field rotation-generator inequality is in the classical Bogoliubov/Mermin tradition. The contribution retained here is the normalization and combination for the supplied model, with explicit finite-volume and momentum limits; it does not locate a physical kernel among the framework's readings.''')
change('Exact target and obligation graph','''| Object | Status and scope |
|---|---|
| Legendre coefficients and real reflection form | Complete positive-integrand and factorization proofs; coefficients through degree four checked by primary |
| Gaussian domination | Named imported theorem with the exact normalization above |
| Infrared bound | Derived below, including self-inverse momenta |
| Sum rule and magnetization-square liminf | Small-momentum lattice shell estimate supplied below |
| Zero-field lower bound | Complete finite-volume rotation-generator proof |
| Two-sided component Fourier bound | Every allowed sequence `k_L→k≠0`, using eventual liminf control |
| Transverse extremal state, real-space asymptotic, physical model selection | Not established; deferred |''')
s=s.replace('any function `F` of the spins in `H^+` and any single-site factors\n`Π_x g_x(s_x)` with `g_x ≥ 0` reflection-symmetric,\n`E_L^{g}[F · F∘θ] ≥ 0`.','any real-valued square-integrable function `F` of the spins in `H^+`, `E_L[F · F∘θ] ≥ 0`.')
s=s.replace(' Π_{x∈H^+} g_x dσ',' Π_{x∈H^+} dσ')
change('Theorem G2 — Gaussian domination and the infrared bound','''**Imported starting bound.** For real `φ:T_L→R` and a unit vector `e`,
`Z(φ)=∫exp[−(β/2)Σ_{⟨xy⟩}|s_x−s_y−(φ_x−φ_y)e|²]Π_x dσ(s_x)≤Z(0)`
by the Gaussian-domination theorem and parameter mapping in Premises. The spins shifted by `φ_x e` are not unit vectors: the general identity contains the factors `exp[−β(|u|²+|v|²)/2]exp(βu·v)`. The false constant norm replacement is not used.

**Infrared derivation.** Put `φ=λψ` and
`X=Σ_{⟨xy⟩}(ψ_x−ψ_y)(s_x−s_y)·e`, `S_2=Σ_{⟨xy⟩}(ψ_x−ψ_y)²`.
Expansion gives `Z(λψ)/Z(0)=⟨exp(βλX−βλ²S_2/2)⟩`. Spin inversion implies `⟨X⟩=0`, so domination implies `β²⟨X²⟩≤βS_2`.
For a cosine or sine mode of momentum `k`, summation over bonds gives
`X=E(k)Σ_x s_x^e ψ_x` and `S_2=E(k)Σ_xψ_x²`.
If `2k≠0` modulo `2π`, both cosine and sine norms are `N/2`; their two variance bounds add to
`⟨|Σ_xe^{ik·x}s_x^e|²⟩≤N/(βE(k))`.
If `k≠0` but `2k=0`, the wave is real, its cosine norm is `N` and its sine vanishes. The single cosine bound is then `⟨(Σ_x s_x^e cos(k·x))²⟩≤N/(βE(k))`, giving the same normalized result directly. Thus for every nonzero allowed mode,
`⟨|ŝ^e(k)|²⟩≤1/(βE(k))`. ∎

The primary checks the algebraic shift and second-order expansion and two non-self-inverse modes on the `4³` torus. The self-inverse calculation above is written proof; original independent controls separately checked two such modes. Neither finite control executes the imported domination theorem.''')
s=s.replace('The Riemann sums\ntend to the integral (the integrand is bounded away from `k = 0` and\n`1/E(k) ≤ π²/(4|k|²)` near it, integrable in three dimensions). For the bound:', '''To justify the singular Riemann sum, write `h=π/L`, `k=hn` using representatives in `[-π,π)^3`. Since `E(k)≥4|k|²/π²`, the normalized contribution from `0<|k|≤δ` is at most a constant times `L^{-1} Σ_{0<|n|≤δ/h}|n|^{-2}`. The integer shell `j≤|n|<j+1` contains at most `C(j+1)²` points (cover each point by its disjoint unit cube in an annulus of fixed larger thickness), so this sum is at most `C'(δL+1)`. The contribution is therefore at most `C''δ+O(1/L)`, uniformly in `L`. Away from a small ball the integrand is continuous and ordinary Riemann sums apply; its integral inside the ball is also `O(δ)`. First take `L→∞`, then `δ→0`. For the bound:''')
change('Theorem G5 — the transverse channel is the lattice Green function up to constants','''**Statement.** Let `β>3√3π/8`, `M²=liminf_L M_N²`, and choose any sequence of nonzero torus momenta `k_L` tending modulo `2π` to a fixed `k≠0`. For every fixed component `e`,
`(M²/3)²/(βE(k)) ≤ liminf_L ⟨|ŝ^e(k_L)|²⟩ ≤ limsup_L ⟨|ŝ^e(k_L)|²⟩ ≤ 1/(βE(k))`,
where `M²≥1−3G(0)/β>0`.

*Proof.* The upper bound follows for every `L` from the infrared bound and continuity of `E` at nonzero `k`. Fix `η` with `0<η<M²`. Eventually `M_N²≥M²−η`, while `M_N²≤1`. The finite lower bound is therefore at least
`[2(M²−η)/3]²/[sqrt(βE(k_L))+sqrt(βE(k_L)+4/(3N))]²`.
Taking the liminf and then `η↓0` gives the displayed lower bound. This uses all sufficiently large volumes, not a selected subsequence attaining the magnetization liminf. Component symmetry extends the same result to all three components. ∎

The zero-field torus measures remain rotation invariant. The result compares Fourier structure factors with the inverse Laplacian symbol at fixed nonzero limiting momentum. It supplies no preferred magnetization direction, no extremal ordered-state transverse correlation, and no pointwise real-space decay law.''')
change('No-Go Discipline Gate','''### N1 — Negative certification deferred
The original route list did not establish five independent exact-target attacks. Universal exclusions of formation and discrete-spin laws, and a unique physical candidate, are withdrawn. No negative certificate is issued.

### N2 — Conditions and imports
The uniform sphere measure, static exponential interaction and periodic torus are supplied mathematical conditions. Gaussian domination is an explicit theorem import, not a new framework axiom or an assertion of independent walls.

### N3 — Corrected boundaries
Shifted spins are not unit. Self-inverse modes need their own normalization calculation. Rotation-invariant finite-volume component bounds do not identify an extremal-state transverse observable.

### N4 — Input scope
The linked possibility-covariance parent supplies conditional representation vocabulary. It does not select a static law or coupling. The Gaussian theorem supplies only the finite domination statement under its stated hypotheses.

### N5 — Evidence resolution
The primary executes coefficients through degree four, two non-self-inverse torus modes and four sphere-polynomial integrals. The self-inverse proof, shell estimate and momentum-sequence argument are written proofs, not new primary executions. The imported theorem is not independently executed by this runner.

### N6 — Primitive boundary
No primitive supplies an overlap, coupling, state or physical interpretation.

### N7 — Other kernels
The kernel `(1+t)/2` has Legendre coefficients `1/2,1/2,0,...` and is positive semidefinite, although not strictly positive in higher degrees. This note neither denies its reflection positivity nor extends the exponential Gaussian-domination argument to it.

### N8 — Recovery
The original complete arguments and controls are preserved in the recovery manifest. Corrected formation and discrete-model scopes supply no universal exclusion used here.''')
fences=['This note gives zero-field component Fourier bounds for the supplied sphere static law using an explicit Gaussian-domination import; it establishes no selected transverse-state correlator, pointwise real-space decay or physical model classification, and adopts no clause.','No plane, bridge, Born-weight or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.','The uniform sphere measure and exponential interaction are declared model inputs; all load-bearing mathematical imports are explicitly identified.']
change('Boundaries and non-claims','\n\n'.join(fences))
change('Imports','''The linked axiom memo supplies only its quoted sentences. The possibility-covariance parent supplies the conditional sphere/rotation representation, not a selected probability law. The finite static measure is explicitly defined here.

Biskup's Theorem 4.6, with the hypotheses and `b=3β/2` mapping in Premises, is a load-bearing Gaussian-domination import. It is not merely a reference. The remaining mathematical imports are the Legendre expansion of the exponential and spherical-harmonic addition formula, finite-torus transform unitarity, and integration by parts for the divergence-free sphere rotation field. The Rodrigues integral, infrared expansion, sum-rule estimates and zero-field quadratic argument are given here. Fröhlich–Simon–Spencer, Fröhlich–Israel–Lieb–Simon and Mermin identify the historical mathematical setting, not additional physical premises.''')
change('Review record','''All original proof versions, historical controls and outputs remain byte-exact in the recovery manifest. The original independent reviewer identified the shifted-norm, normalization, limit and interpretation defects. This source repair uses the named theorem import, preserves the useful finite identities and withdraws unsupported physical/negative conclusions. Same-session affected-source confirmation is pending; the author has executed no scientific primary or replacement control.''')
s=s.replace('## Theorem G5 — the transverse channel is the lattice Green function up to constants','## Theorem G5 — component bounds along momentum sequences')
(w/new).write_text(s);(w/op).unlink(missing_ok=True)
runner=runner.replace(op,new).replace(Path(op).stem.lower(),Path(new).stem.lower()).replace('AUDIT_TIMEOUT_SEC = 900','AUDIT_TIMEOUT_SEC = 180')
runner=re.sub(r'(?s)FENCES = \(.*?\n\)','FENCES = '+repr(tuple(fences)),runner,count=1)
runner=re.sub(r'(?m)^    "lattice_wide:.*$','    "lattice_wide: checked and not executed — imported Gaussian domination and written component Fourier/limit proofs; no infinite-lattice execution or transverse-state identification",',runner)
runner=runner.replace('so Z(lambda psi) <= Z(0) forces','the explicitly imported Z(lambda psi) <= Z(0) bound then forces')
runner=runner.replace('long-range order, and the zero-field Bogoliubov bound.','magnetization-square estimates, and the zero-field component bound; Gaussian domination is imported, not executed.')
ast.parse(runner);(w/rp).write_text(runner)
(r/'drain8153-author-live.json').write_text(json.dumps({'note':new,'runner':rp,'fences':fences},indent=2)+'\n')
