from pathlib import Path
import ast,hashlib,gzip,json,subprocess,difflib,shutil
R=Path('/private/tmp/review-drain-20260915'); W=R/'author-draft-slot'; O=R/'drain8171-original/head'
BASE='8bf464953779b8ada8415208e89a656411f9f525'; HEAD='15b6e402b902964ada51ffdd8e8c88fb4e472013'
assert subprocess.check_output(['git','-C',str(W),'rev-parse','HEAD'],text=True).strip()==BASE
assert not subprocess.check_output(['git','-C',str(W),'status','--porcelain'],text=True)
sha=lambda b:hashlib.sha256(b).hexdigest()
def emit(p,s,mode=0o644):
 p=W/p; assert not p.exists(),p;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(s.encode() if isinstance(s,str) else s);p.chmod(mode)
def dump(p,x):
 assert not p.exists(),p;p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
disp=json.loads((R/'drain8171-disposition-original.json').read_text()); assert len(disp)==18
oldnote=next(x['path'] for x in disp if x['path'].startswith('docs/ADMISSIBILITY'))
oldrun=next(x['path'] for x in disp if x['path'].startswith('scripts/'))
note='docs/SPHERE_FORMATION_KERNEL_SENSITIVITY_AND_LEVEL_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-09-16.md'
runner='scripts/sphere_formation_kernel_sensitivity_level_contraction_check_2026_09_16.py'
cid=Path(note).stem.lower(); stem=Path(runner).stem
hist='docs/work_history/review_loop/pr8171'; deferred=hist+'/pr8171-deferred-uniform-route-ceiling.txt'
entries=[]
for i,d in enumerate(disp):
 raw=(O/d['path']).read_bytes();assert sha(raw)==d['head_sha256']
 mode,_,blob=d['head_tree'].split('\t')[0].split();assert subprocess.check_output(['git','-C',str(W),'cat-file','blob',blob])==raw
 dest=f'{hist}/originals/{i+1:02d}-{Path(d["path"]).name}.gz'
 enc=gzip.compress(raw,mtime=0);emit(dest,enc)
 entries.append(dict(original_path=d['path'],mode=mode,git_blob=blob,sha256=sha(raw),recovery=dict(path=dest,encoding='gzip',sha256=sha(enc),decoded_sha256=sha(raw)),disposition='narrowed' if d['path'] in [oldnote,oldrun] else 'historical-recovery-only',canonical_path=note if d['path']==oldnote else runner if d['path']==oldrun else None))
manifest=dict(schema_version=1,kind='exact-original-recovery-manifest',pr=8171,head=HEAD,delta_base='6dda46fc1af02827e9c6b64b2f7d05c381a3ce07',entries=entries)
emit(hist+'/pr8171-original-manifest.json',json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
emit(hist+'/README.md','''# PR8171 original recovery and deferred science

The manifest and deterministic gzip payloads preserve all 18 original paths,
Git modes, blob identities and decoded SHA-256 hashes independently of branch
retention. [Manifest](pr8171-original-manifest.json) maps every occurrence.
Decode a payload with `gzip -dc originals/<name>.gz`; restore its original mode
from the manifest. These are historical records, including original proof,
source, cache, controls, refuter, failures and author-written status claims.
They confer no current review or audit verdict and are not runtime helpers.

The [readable corrected route-ceiling argument](pr8171-deferred-uniform-route-ceiling.txt)
preserves the complete mathematical correction and its explicit domain as
**deferred science**, outside the live bounded claim. The original branch must
be retained on partial closure. The four historical attack items do not meet
the five-family negative-certification contract; this is not a mathematical
refutation. The canonical note retains the positive mean-map inequalities.

Historical simulation limitation: the refuter caps residual rejection at 200
attempts, leaves unresolved entries at their initial common draw, and reports
only the final level's unresolved count. A zero final count does not prove that
every earlier level had valid marginals. Its contraction ratios are historical
observations, not fresh exact-kernel evidence. The zero-concentration sampler
failure and correction are preserved in the historical checker report.
Neither historical simulator is imported or executed by the primary.
''')
original=(O/oldnote).read_text()
def section(a,b):return original.split(a,1)[1].split(b,1)[0]
t1='## Theorem T1 — the sensitivity of the sphere kernel'+section('## Theorem T1 — the sensitivity of the sphere kernel','## Theorem T2')
t1=t1.replace("By block 26's T1(a), `E[s] = Aû` and `E[ssᵀ] = (A/κ)I + (1 − 3A/κ)ûûᵀ`;", "Direct integration gives `Z(κ)=∫_{−1}^1 e^{κw}dw=2 sinhκ/κ`, `E[w]=Z'/Z=A`, and `E[w²]=Z''/Z=1−2A/κ`. Axial rotation symmetry gives zero transverse means and cross moments; each transverse second moment is `(1−E[w²])/2=A/κ`. Thus `E[s] = Aû` and `E[ssᵀ] = (A/κ)I + (1 − 3A/κ)ûûᵀ`;")
t1=t1.replace("Finally `A/κ ≤ 1/3` is block 26's bound `A(κ) < κ/3` (`A' ≤ 1/(3 + κ²)`), re-checked (B4).", "Finally the expansions `sinhκ=κ+κ³/6+O(κ⁵)` and `coshκ=1+κ²/2+O(κ⁴)` give `lim_{κ→0} A(κ)/κ=1/3`. The proved decrease gives `A/κ≤1/3`, strictly for κ>0 because the m=3 coefficient is positive. At κ=0 the uniform law has mean zero and covariance `I/3`, so the directional bound extends continuously. B4 checks ten rational points; the all-parameter bound is this written proof.")
header=f'''---
claim_id: {cid}
claim_type: bounded_theorem
claim_scope: "For the supplied sphere exponential kernel, records-only reading and three-predecessor synchronous level order: all-parameter moment and sensitivity bounds; measurable causal contraction q=sqrt(3) beta; compact-Feller invariant-law existence and uniqueness for 0<=beta<1/sqrt(3); finite-marginal exponential approach and absolute aligned magnetization bound; exact one-site recursion and positive mean-map inequalities. Formal negative route certification is deferred outside this row. No physical kernel, menu, order or threshold is selected."
upstream_dependencies:
  - minimal_axioms
runner: {runner}
---

# Sphere-kernel sensitivity and contraction of the supplied level law

**Date:** 2026-09-16
**Type:** bounded_theorem
**Status:** bounded-support; supplied-model theorem, unaudited.
**Primary runner:** [exact finite checks](../{runner}).
**Cache destination:** [source-bound stdout](../logs/runner-cache/{stem}.txt).

## Result up front

For the supplied kernel and synchronous level order below, the total-variation
sensitivity is at most `|V−V'|/(2√3)`. A measurable causal coupling contracts
expected chordal distance per site by `q=√3β` per level. For `0≤β<1/√3`,
compactness and the Feller property give an invariant law, the contraction
makes it unique and rotation invariant, and every initial law approaches it
in finite marginals with the stated explicit bound. The aligned magnetization
satisfies `|m_t|≤q^t`. The one-site periodic law has exact rate `A(3β)^t`.
All four original argument surfaces survive: sensitivity, invariant-law
contraction, magnetization/one-site recursion, and mean-map bounds. The
complete corrected uniform-route ceiling is readable deferred science in
[recovery](work_history/review_loop/pr8171/README.md), not a conclusion of this
bounded row. Finite symbolic controls do not execute an infinite level plane.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Behavior outside the supplied contraction region and physical selection of kernel, menu and order remain open."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Study larger-coupling behavior using an explicitly defined coupling or finite-block mechanism."
conditional_surface_status: "Supplied sphere kernel, records-only reading and synchronous three-predecessor level order; standard compact probability imports stated below."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises and declared objects

The [current axiom memo](MINIMAL_AXIOMS_2026-06-29.md) supplies the framework
boundary: "There is one fixed nearest-neighbor admissibility rule, covariant
under lattice translations and proper cubic rotations.", "For each site, the
probability distribution over the possibilities is determined by, and varies
with, the nearest-neighbor conditions.", "Records form.", and "Only records
are readable." The following kernel, menu, reading and order are additional
supplied mathematical conditions, not selected by those sentences.

The current finite-menu formation/static note
`ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`
is context for the terminology only. No classification or static-law theorem
is imported from it; the sphere proof below is self-contained. The primary
checks that historical context identity and binds its current bytes as a
context input, which is not a mathematical dependency edge.

- Values are unit vectors `s∈S²`; `β≥0` is supplied. Write `κ=|V|`,
  `û=V/|V|` for V≠0, `A(κ)=cothκ−1/κ`, `A(0)=0`, and
  `K_V(ds)=(κ/(4π sinhκ)) exp(V·s)dσ(s)`, uniform at V=0.
  Here dσ is sphere area measure; `F(V)=E[s]=A(κ)û`, F(0)=0.
- A level is `X=(S²)^{{Z²}}`. The new spin at coordinate `(i,j)` has law
  `K_{{βS}}`, where `S=s_(i,j)+s_(i−1,j)+s_(i,j−1)` from the preceding
  level. Sites draw independently conditional on that level. These are the
  three predecessors `x−e_j` in the supplied monotone level order on `Z³`.
- Chordal distance is `|s−s'|≤2`. `TV=(1/2)∫|f−g|dσ`, and
  `W_1=inf E|s−s'|` on the sphere. For a specified joint level coupling γ,
  `D(γ)=sup_x E_γ|s_x−s'_x|`; for laws define
  `d_∞(μ,ν)=inf_γ D(γ)`. Bounds below construct couplings, without assuming
  the infimum is attained. Finite marginal metrics use the sum of chordal
  distances over the specified finite set.
- For a fixed unit e, the aligned initial plane is identically e and
  `m_t=E[s_x·e]`. Translation invariance makes this independent of x.

## Imports

Standard mathematical imports are the existence of countable product
probability measures and iterated kernels on standard Borel spaces; compactness
of countable products of compact metric spaces; weak sequential compactness
of probability measures on a compact metric space; uniform density of continuous
cylinder functions; and determination of a countable-product law by its finite
marginals. Every use and its hypotheses appear below. No external theorem
supplies the kernel, order or physical interpretation. The finite-menu context
is not needed for these imports. No primitive supplies a state-selection rule.

## Exact target and obligation graph

| Argument | Claim and proof obligation | Finite primary coverage |
|---|---|---|
| Sphere sensitivity (T1) | direct moments, entire-series sign and continuity at zero | symbolic identities, 12 coefficients, ten rational enclosures |
| Level contraction (T2) | measurable common-density coupling, compact-Feller existence, finite-marginal uniqueness | contraction factor and two boundary enclosures |
| Magnetization (T3) | antipodal absolute-value inequality and conditional-mean recursion | six one-site rate enclosures |
| Mean-map bounds (T4) | linear test function and global entire-series lower bound | series through degree six and five rational enclosures |

'''
t2='''## Theorem T2 — the causal coupling contracts

**Measurable coupling.** Given densities f=f_V and g=f_V', set h=min(f,g)
and α=∫h dσ. With probability α draw a common point with density h/α;
with probability 1−α draw the two points independently from
`(f−h)/(1−α)` and `(g−h)/(1−α)`. At α=0 or 1 use just the nonzero branch.
This is a measurable probability kernel in (V,V'): the densities and their
integrals are Borel functions, and normalized integrals on each nonzero branch
are measurable. Its marginals are f and g; its expected chordal cost is at
most `2(1−α)=2TV≤|V−V'|/√3`. Countable products give independent site pairs
conditional on the preceding coupled levels. This avoids any measurable
selection of optimal transport plans and needs no additive η error.

**Statement and contraction.** For that coupling, `D_(t+1)≤√3β D_t`.
Indeed at x, condition on the coupled preceding level:
`E[|s_x−s'_x||previous]≤(β/√3)|S_x−S'_x|≤(β/√3)Σ_(j=1)^3 |s_(x−e_j)−s'_(x−e_j)|`.
Take expectations and the supremum over x. Thus `D_t≤2q^t` for `q=√3β`.
At β=0 all new-site laws are uniform and one common draw couples them exactly;
the bound for t≥1 is zero, while the initial bound is D_0≤2.

**Existence.** The countable product X is compact metrizable. The transition
P sends a continuous cylinder function to a continuous cylinder function:
only finitely many predecessor coordinates enter, and their sphere densities
vary continuously, uniformly on compact parameter sets. Dominated integration
gives continuity. Continuous cylinders are uniformly dense in C(X), and P
is a sup-norm contraction, so P maps all C(X) to C(X): it is Feller.
For any initial law ν, take `ν_N=N^(-1)Σ_(t=0)^(N−1)νP^t`.
Compactness of probability laws on X gives a weakly convergent subsequence.
For f∈C(X), `(ν_NP−ν_N)(f)=(νP^N(f)−ν(f))/N→0`.
The Feller property lets the subsequential limit pass through Pf, hence the
limit μ is invariant. This existence argument works at every finite β;
the uniqueness and rate below require q<1.

**Uniqueness.** Let μ,μ' be invariant laws, couple their initial planes
arbitrarily and apply the measurable causal coupling. At each t their marginals
remain μ,μ'. For any finite Λ, the Wasserstein distance of their Λ marginals
for `Σ_(x∈Λ)|s_x−s'_x|` is at most `2|Λ|q^t→0`. Thus every finite marginal
coincides, and μ=μ'. Simultaneous rotations commute with P, so every rotated
μ is invariant and uniqueness makes μ rotation invariant. Couple any initial
law with μ to get `d_∞(νP^t,μ)≤2q^t` and the same finite-marginal bound.
Rotation invariance gives zero one-site mean, hence exponential decay of
one-site magnetization from any initial law. ∎

'''
t3='''## Theorem T3 — exponential loss of aligned magnetization

For `0≤β<1/√3`, the aligned plane obeys `|m_t|≤(√3β)^t`.
Run the coupling from e and −e. Rotation by π about an axis perpendicular
to e maps the first marginal process to the second, so their projected means
are m_t and −m_t. Therefore
`2|m_t|=|E[s_x·e]−E[s'_x·e]|≤E|s_x−s'_x|≤2(√3β)^t`.
This uses no unproved nonnegativity of m_t.

On the one-site periodic plane the three predecessors are the same unit spin,
so the T1 mean identity gives
`E[s_(t+1)·e|s_t]=A(3β)(s_t·e)`.
Conditional expectation and m_0=1 give `m_t=A(3β)^t` exactly.
T1 gives `A(3β)≤β`, strictly for β>0. At β=0 the rate is zero after the
first update. These exact one-site conclusions do not assert equality of
one-site and infinite-plane rates. ∎

'''
t4='''## Theorem T4 — positive mean-map bounds

For every V,V', `W_1(K_V,K_V')≥|F(V)−F(V')|`. Indeed for any coupling and
unit d, `|(E s−E s')·d|≤E|s−s'|`. Choose d parallel to the mean difference
(the zero case is immediate), then take the infimum over couplings.
For V=0,V'=δd with δ>0, the mean difference is A(δ).

The global bound is `1/3−δ²/45≤A(δ)/δ<1/3` for δ>0.
For the lower bound multiply by the positive number δ² sinhδ. The resulting
expression is
`H(δ)=δ coshδ−(1+δ²/3−δ⁴/45)sinhδ`.
Its coefficient of δ^(2n+1), for n≥1, is
`16n(n−1)(n−2)(n+2)/(45(2n+1)!)`; the n=0 coefficient is zero.
To verify it, combine `2n/(2n+1)!−1/[3(2n−1)!]`
with `1/[45(2n−3)!]` when n≥2. The n=1,2 coefficients vanish and all n≥3
are positive. Entire-series convergence gives H(δ)≥0 for every δ>0.
The upper bound follows from the strict decrease proved in T1.
The series `A(δ)/δ=1/3−δ²/45+2δ⁴/945−δ⁶/4725+…` and five rational
checks are finite corroboration, not the all-δ proof. ∎

'''
# Complete corrected negative implication is readable recovery, outside the live theorem.
emit(deferred,'''DEFERRED SCIENCE — corrected uniform single-predecessor route ceiling

This is the full corrected fourth proof surface of original PR8171. It is
retained for scientific recovery, not promoted as a live bounded/no-go row.
Formal negative certification remains DEFERRED: fewer than five qualified
attack families were supplied. This procedural limitation does not refute
this mathematical argument. The original branch must survive partial closure.

'''+t4+'''Scoped ceiling argument (not a physical threshold).

Fix beta>=0. Let c_beta be the supremum of
W_1(K_{beta(s1+s2+s3)}, K_{beta(s1'+s2+s3)}) / |s1-s1'|
over all unit s1,s1',s2,s3 with s1!=s1', with chordal transport cost.
This is a uniform one-predecessor Lipschitz sensitivity over the full supplied
domain. A one-step sum-of-three-sensitivities criterion asks 3c_beta<1.

Take s1=(1,0,0), s2=(-1/2,sqrt(3)/2,0), s3=(-1/2,-sqrt(3)/2,0).
Their sum is zero. Replace only s1 by s1'(theta)=(cos(theta),0,sin(theta));
each predecessor remains a unit vector, while h=|s1'-s1| tends to zero.
The positive mean-map lower bound above gives a ratio at least
A(beta h)/h >= beta/3-beta^3 h^2/45.
For beta=0 this is zero; for beta>0 the limit as theta->0 is beta/3.
Hence c_beta>=beta/3, including the supremum limit. For beta>=1 the strict
criterion 3c_beta<1 cannot hold; equality beta=1 is covered by the limit.
This excludes only that uniform one-step chordal-Wasserstein criterion.
It says nothing against block, multistep, state-restricted or different-metric
couplings, or against actual loss of memory at any larger coupling.

For the particular 2*TV triangle-bound route, at V=0 a displacement delta*d
has TV/|delta| -> (1/2) E_uniform |s.d| = 1/4, since w=s.d is uniform on[-1,1].
The same admissible predecessors therefore force its uniform one-slot
2*TV coefficient to be at least beta/2. Its 3c<1 sufficient criterion is
silent at beta>=2/3. This lower bound does not prove a global TV sensitivity
upper bound of 1/4, and does not supply a contraction region beta<2/3.
The historical quadrature maximum is a finite sample only.

Strong counter-route: a multistep/block transport coupling may use correlations
and state-dependent cancellation inaccessible to the uniform one-site
triangle bound. Its terminal obligation is a controlled strict block cost
contraction for a specified time step and admissible joint law. It remains
open and is outside the theorem's narrow criterion domain.

Original proof, including its small-delta alternating-series shortcut and
placeholder bound, remains exact in the adjacent 18-entry gzip manifest.
''')
fences=("The sphere kernel, records-only reading and level order are supplied conditions; the theorem makes no physical selection.","The constant `1/√3` is a sufficient contraction bound, not a physical threshold.","Formal negative route certification is deferred; the full corrected argument is preserved as readable recovery science.")
tail='''## No-Go Discipline Gate

### N1 — Deferred negative certification
The historical packet names four items: sensitivity, coupling independence,
finite-marginal uniqueness and region. These are mostly proof obligations for
the positive theorem, not five distinct attacks against the uniform-route
ceiling. No fifth route is invented and no negative packet PASS is claimed.
The full corrected negative implication is deferred in recovery; the live
mean-map inequalities remain affirmative mathematical bounds.

### N2 — Wall relationships
No independent-wall count is asserted. Kernel, menu and order are joint
supplied hypotheses; their absence is not a proved physical obstruction.

### N3 — Explicit hypotheses
Sphere area measure, exponential kernel, records-only reading, synchronous
three-predecessor order and standard compact-probability imports are named.
The rotation symmetry used here is a property of the supplied kernel.

### N4 — Citation and residual matching
The axiom memo fixes the framework boundary only. The finite-menu note is
context, not authority for sphere moments or infinite-volume uniqueness.
No sibling static-law result or historical simulation closes a residual here.

### N5 — Actual primary resolutions
- per_element: symbolic variance/directional identities, twelve sign coefficients,
  log-density derivatives and finite exact rational bounds.
- per_site: six rational one-site rate checks and five mean-map bound checks;
  no stochastic one-site chains are executed by this primary.
- per_mode: checked and not executed — no spectral decomposition, quadrature,
  Monte Carlo or mode-resolved simulation is called by this primary.
- per_block: the contraction-factor arithmetic and two boundary enclosures;
  no finite block sampler is called.
- lattice_wide: checked and not executed — compactness, measurable coupling and
  infinite-plane uniqueness are written proofs, not finite runner executions.

### N6 — Partial closure and primitives
The accepted surface is the positive supplied-model proof. The deferred
negative argument and every original remain recoverable, with branch retention
required for partial closure. No additional axiom or primitive is adopted.

### N7 — Concrete strongest counter-route
A multistep block coupling could exploit correlations and cancellations lost
by the one-site triangle estimate. Its terminal task is a strict expected block
cost bound for a specified joint transition. State-restricted or alternative
transport costs also remain open. The present positive region is compatible
with success of those routes at larger beta; the deferred ceiling concerns
only the explicitly defined uniform single-predecessor criterion.

### N8 — Historical comparison
The original finite-menu causal-contraction and sphere static-law campaign
comparisons are preserved in recovery. They concern different kernels or
transition/specification objects and supply no additional route closure here.
Historical finite strong-coupling memory plots do not settle an infinite-plane
threshold. No claim of a completed cross-menu phase classification survives.

## Boundaries and non-claims

'''+ '\n\n'.join(fences)+'''

## Review record

[Exact history and limitations](work_history/review_loop/pr8171/README.md)
contains all original proof/source/cache/control/refuter versions. Historical
numerical and mutation results remain historical; no corrected-source primary,
simulation or mutation was executed during author preparation. In particular,
the refuter's capped residual-rejection routine can retain unresolved common
draws, and its printed last-level zero does not verify all preceding levels.
Its observed ratios are not promoted as valid exact-marginal coupling evidence.
The primary performs symbolic/rational checks only. The original zero-parameter
sampler failure and historical correction remain available in the archive.

## Verification

The primary's intended completed count is 16: four source checks, four kernel
checks, two contraction/rate checks, one mean-map check, four packaging checks
and one N5 printing check. Ten existing mutations remain available; their old
census is not fresh evidence. The primary emits stdout only, with no JSON
output, simulation or external helper invocation. Written compactness and
all-parameter proofs are separately reviewed mathematical content.
'''
newnote=header+t1+t2+t3+t4+tail
emit(note,newnote)
s=(O/oldrun).read_text().replace(oldnote,note).replace(Path(oldnote).stem.lower(),cid)
s=s.replace('import re\n','import re\nimport hashlib\n')
s=s.replace('AUDIT_TIMEOUT_SEC = 900','AUDIT_TIMEOUT_SEC = 60')
# Literal pins preserve the original three actual reads, including context-only finite-menu input.
inputs=[note,'docs/MINIMAL_AXIOMS_2026-06-29.md','docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md']
pins={p:sha((W/p).read_bytes()) for p in inputs}
s=s.replace('ROOT = Path(__file__).resolve().parents[1]','INPUT_SHA256 = '+repr(pins)+'\nROOT = Path(__file__).resolve().parents[1]')
s=s.replace('all(Path(ROOT, p).exists() for p in AUDIT_INPUT_PATHS)', 'all(Path(ROOT, p).is_file() and hashlib.sha256(Path(ROOT, p).read_bytes()).hexdigest() == INPUT_SHA256[p] for p in AUDIT_INPUT_PATHS)')
s=s.replace('"all declared inputs exist"','"all three declared source/context inputs match literal SHA-256 pins"')
s=s.replace('"block 01\'s note (on main) carries its claim_id and the rule\'s product form"','"the context-only finite-menu note carries its identity and product-form heading; no sphere theorem is imported"')
# Check computations are unchanged; correction only narrows prose describing those computations.
s=s.replace(', so the directional second moment is at most A/kappa <= 1/3 and TV(K_V, K_V\') <= |V - V\'|/(2 sqrt3), W_1 <= |V - V\'|/sqrt3', '; the written proof supplies the all-parameter variance and sensitivity bounds')
s=s.replace(', so the one-site rate A(3 beta)^t is below beta^t and the antipodal comparison gives m_t <= (sqrt3 beta)^t for beta < 1/sqrt3', '; the written conditional-mean recursion and absolute antipodal comparison give the rate bounds')
s=s.replace(': the mean map moves by at least a third of a small change, so no coupling of this kind contracts for beta >= 1', '; these finite checks do not certify a global negative route claim')
a=s.index('FENCES = ('); b=s.index('FORBIDDEN = (',a);s=s[:a]+'FENCES = '+repr(fences)+'\n'+s[b:]
# "certified"/"converge" are not prohibited scientific concepts; original packaging scan list retained to detect actual injected claims.
s=s.replace('"## Theorem T4", phrase + "\\n\\n## Theorem T4"','"## Theorem T4", phrase + "\\n\\n## Theorem T4"')
a=s.index('N5_LINES = (');b=s.index('\n\n\ndef family_g',a)
n5=("per_element: executed — symbolic variance and directional moments, twelve sign coefficients, log-density derivatives and ten rational enclosures", "per_site: executed — six rational one-site rate bounds and five rational mean-map bounds; no stochastic site chains", "per_mode: checked and not executed — no spectral decomposition, quadrature or Monte Carlo is invoked by this symbolic primary", "per_block: executed — contraction-factor arithmetic and its exact boundary enclosures at two rational beta values; no block sampler", "lattice_wide: checked and not executed — infinite-plane compactness, measurable coupling and invariant-law uniqueness are written proofs")
s=s[:a]+'N5_LINES = '+repr(n5)+s[b:]
s=s.replace('and the reach of the route.', 'and positive mean-map bounds; negative route certification remains deferred.')
compile(s,runner,'exec');emit(runner,s,0o755)
# Compare computational AST independently of string-report substitutions.
oldast=ast.parse((O/oldrun).read_text()); newast=ast.parse(s)
class Normalize(ast.NodeTransformer):
 def visit_Constant(self,n):
  return ast.copy_location(ast.Constant('<text>'),n) if isinstance(n.value,str) else n
checks={}
for name in ['exp_bounds','A_bounds','sqrt_bounds','family_b','family_c','family_d']:
 old=next(x for x in oldast.body if isinstance(x,ast.FunctionDef) and x.name==name);new=next(x for x in newast.body if isinstance(x,ast.FunctionDef) and x.name==name)
 checks[name]=ast.dump(Normalize().visit(old))==ast.dump(Normalize().visit(new));assert checks[name],name
paths=subprocess.check_output(['git','-C',str(W),'ls-files','--others','--exclude-standard'],text=True).splitlines();assert len(paths)==23,len(paths)
rows=[dict(path=p,mode='100755' if (W/p).stat().st_mode&0o111 else '100644',sha256=sha((W/p).read_bytes())) for p in paths]
snap=R/'drain8171-prepared-source-v1';assert not snap.exists()
for p in paths:(snap/p).parent.mkdir(parents=True,exist_ok=True);shutil.copy2(W/p,snap/p)
dump(R/'drain8171-author-prepared-v1.json',dict(schema_version=1,kind='author-preparation-not-review-verdict',pr=8171,owner='PR8171-author',base=BASE,head=HEAD,source_count=len(rows),source=rows,original_count=18,original_manifest=dict(path=hist+'/pr8171-original-manifest.json',sha256=sha((W/hist/'pr8171-original-manifest.json').read_bytes())),canonical_notes=[note],primaries=[runner],deferred_science=[deferred],snapshot=str(snap),primary_runs=0,staged=False,mathematical_function_ast_comparison=checks,branch_preservation_required=True))
dump(R/'drain8171-author-dispositions-v1.json',dict(schema_version=1,constituents=[dict(pr=8171,head=HEAD,dispositions=entries)],claims=[dict(original='T1',destination=note,disposition='complete proof retained; direct sphere integrations, strict decrease and zero continuity supplied'),dict(original='T2',destination=note,disposition='complete contraction and uniqueness retained; measurable coupling and compact-Feller existence supplied'),dict(original='T3',destination=note,disposition='absolute magnetization corrected; complete one-site recursion proved'),dict(original='T4 positive inequalities',destination=note,disposition='complete mean bound with global entire-series coefficient proof'),dict(original='T4 uniform-route negative ceiling',destination=deferred,disposition='complete corrected proof and admissible predecessor construction readable but formal negative certification deferred'),dict(original='campaign/static/physical and numerical global promotions',destination=hist+'/pr8171-original-manifest.json',disposition='withdrawn live; originals exact recovery')]))
patch=''.join(difflib.unified_diff(original.splitlines(True),newnote.splitlines(True),fromfile=oldnote,tofile=note))+''.join(difflib.unified_diff((O/oldrun).read_text().splitlines(True),s.splitlines(True),fromfile=oldrun,tofile=runner))
(R/'drain8171-author-corrections-v1.patch').write_text(patch)
print(json.dumps(dict(paths=len(rows),prepared_sha256=sha((R/'drain8171-author-prepared-v1.json').read_bytes()),note_sha256=sha(newnote.encode()),runner_sha256=sha(s.encode())),indent=2))
