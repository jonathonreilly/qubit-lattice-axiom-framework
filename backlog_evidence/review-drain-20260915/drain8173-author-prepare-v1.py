from pathlib import Path
import ast,hashlib,gzip,json,subprocess,difflib,shutil
R=Path('/private/tmp/review-drain-20260915');W=R/'review-draft-slot';O=R/'drain8173-original/head'
BASE='8bf464953779b8ada8415208e89a656411f9f525';HEAD='e5b3aa31686d88d8a2fe0aad5e938acac0e39404'
assert subprocess.check_output(['git','-C',str(W),'rev-parse','HEAD'],text=True).strip()==BASE
assert not subprocess.check_output(['git','-C',str(W),'status','--porcelain'],text=True)
sha=lambda b:hashlib.sha256(b).hexdigest()
def emit(p,s,mode=0o644):
 p=W/p;assert not p.exists(),p;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(s.encode() if isinstance(s,str) else s);p.chmod(mode)
def dump(p,x):
 assert not p.exists(),p;p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
disp=json.loads((R/'drain8173-review-original.json').read_text())['dispositions'];assert len(disp)==20
oldnote=next(d['path'] for d in disp if d['path'].startswith('docs/ADMISSIBILITY'))
oldrun=next(d['path'] for d in disp if d['path'].startswith('scripts/'))
note='docs/SPHERE_STATIC_FINITE_VOLUME_GAUSSIAN_COVARIANCE_FIXED_AXIS_RESPONSE_AND_PROJECTED_MODE_SUM_BOUNDED_THEOREM_NOTE_2026-09-16.md'
runner='scripts/sphere_static_finite_volume_covariance_response_projected_mode_sum_check_2026_09_16.py'
cid=Path(note).stem.lower();stem=Path(runner).stem
hist='docs/work_history/review_loop/pr8173';readable=hist+'/pr8173-original-note-and-measurement-corrections.txt'
entries=[]
for i,d in enumerate(disp):
 raw=(O/d['path']).read_bytes();assert sha(raw)==d['sha256']
 assert subprocess.check_output(['git','-C',str(W),'cat-file','blob',d['blob']])==raw
 dest=f'{hist}/originals/{i+1:02d}-{Path(d["path"]).name}.gz';enc=gzip.compress(raw,mtime=0);emit(dest,enc)
 entries.append(dict(original_path=d['path'],mode=d['mode'],git_blob=d['blob'],original_sha256=sha(raw),recovery=dict(path=dest,encoding='gzip',sha256=sha(enc),decoded_sha256=sha(raw)),disposition='narrowed' if d['path'] in [oldnote,oldrun] else 'historical-recovery-only',canonical_path=note if d['path']==oldnote else runner if d['path']==oldrun else None))
emit(hist+'/pr8173-original-manifest.json',json.dumps(dict(schema_version=1,kind='exact-original-recovery-manifest',pr=8173,head=HEAD,delta_base='6dda46fc1af02827e9c6b64b2f7d05c381a3ce07',entries=entries),indent=2,ensure_ascii=False)+'\n')
original=(O/oldnote).read_text()
emit(readable,'''PR8173 — historical original note, with current scope corrections

STATUS: recovery history, not a live theorem or current empirical evidence.
The text after ORIGINAL NOTE below is the complete original note, unchanged.
Its errors and unsupported claims are preserved, not endorsed.

The original fixed-axis response proof's penultimate /N is erroneous; the
canonical complete proof has N E[m3] = beta h N^2 E[m1^2]. Its projected
instantaneous-frame field has zero total spin samplewise and is different
from that fixed-axis field. The current zero-field component bounds cannot
be transferred to the sample-relative projection. The original Gaussian
proof needs a real eigenbasis, conjugate Fourier modes and component factors.

The heat-bath output has 11 parameter combinations, not 15: five at L=16,
four at L=24 and two at L=32. For n>=2 the printed values range from 0.861
to 1.013. The independent proposal-chain output includes 1.077 at n=2.
The three printed field comparisons have relative differences approximately
+23.3%, -14.1%, +14.7%. They are not quantified error bars. The scripts and
outputs record no autocorrelation, effective sample size, independent-start,
equilibration or uncertainty certificate. Both chains use aligned starts.
The squared sample-average magnitude is neither E|m|^2 nor the infinite-volume
M^2 in the fixed-component theorem. No normalization window, large-beta limit,
approach from below, absence of size dependence, or physical identification
follows from these records. The real-space ratios and all disagreeing raw
values remain preserved below and in byte-exact output archives.

Formal negative/exhaustive certification remains DEFERRED: four historical
concerns are not five closed route families. This procedural boundary does
not refute the retained finite-volume identities. Preserve the original branch
on partial closure. No historical sampler was rerun during this preparation.

================ ORIGINAL NOTE (unchanged) ================

'''+original)
emit(hist+'/README.md',f'''# PR8173 complete original recovery

The [manifest](pr8173-original-manifest.json) and deterministic gzip payloads
preserve all 20 original paths, modes, Git blobs and decoded SHA-256 hashes
independently of branch retention. Decode with `gzip -dc originals/<name>.gz`
and restore the original mode from the manifest. Full source, three controls,
all raw outputs, original cache, campaign history and submitted graph manifest
are preserved. Submitted status claims and the graph are historical, not
current authority. No stale shared file is installed over current main.

The [readable original note and correction record](pr8173-original-note-and-measurement-corrections.txt)
retains every original proof and measurement paragraph. Full corrected finite
proofs are in the canonical note. Historical sampler estimates carry no
quantified uncertainty or convergence certificate; contradictory values are
preserved explicitly. They are neither runtime inputs nor fresh evidence.
Broader physical, asymptotic and negative-certification conclusions remain
deferred. The original branch must remain available on partial closure.
''')
fences=(
'This note proves finite-volume identities for explicitly supplied sphere and Gaussian laws; it selects no physical menu, reading, order, coupling or normalization.',
'The instantaneous-magnetization projection is distinct from the fixed laboratory components; no fixed-component bound is transferred to that projection.',
'Historical numerical estimates are recovery records only; formal negative certification and infinite-volume or asymptotic conclusions remain deferred.')
newnote=f'''---
claim_id: {cid}
claim_type: bounded_theorem
claim_scope: "For beta>0 and integer L>=3 with each forward nearest-neighbor bond counted once: full Gaussian covariance on the zero-mean subspace, fixed laboratory-axis finite-volume rotation response, and vector Fourier mode-sum identity for the instantaneous-magnetization projection. Supplied finite laws only. Historical numerical estimates and broader negative or asymptotic conclusions are excluded from this claim."
upstream_dependencies:
  - minimal_axioms
runner: {runner}
---

# Finite-volume Gaussian covariance, fixed-axis sphere response and projected mode sum

**Date:** 2026-09-16
**Type:** bounded_theorem
**Status:** bounded-support; supplied-model finite theorem, unaudited.
**Primary runner:** [exact finite checks](../{runner}).
**Execution evidence:** [exact-source cache](../logs/runner-cache/{stem}.txt).
**Recovery:** [original proofs, controls and raw discrepancies](work_history/review_loop/pr8173/README.md).

## Result up front

The quadratic two-component field has covariance `(beta Delta)^(-1)` on the
zero-mean subspace: each scalar nonzero Fourier component has mean-square
`1/(beta E(k))`, while the two-component norm has mean-square `2/(beta E(k))`.
The supplied finite sphere law in a field has the fixed-axis identity
`beta h N E[(m^1)^2]=E[m^3]`. Separately, the vector projection perpendicular
to each sample's own magnetization obeys the unitary Fourier mode-sum identity;
its zero mode vanishes samplewise. These are three complete finite proofs.
They do not identify the two sphere observables or a physical normalization.

The primary contains 14 checks: four source checks, five finite mathematical
checks, four packaging checks and one five-line resolution-report check.
No primary or historical simulator was executed during author preparation.
The written proofs provide the arbitrary finite-volume statements; finite
fixtures are not executions at every lattice size or an infinite-volume test.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "finite supplied-law covariance, rotation response and projected mode sum"
source_of_blocker_text: author_source
reachability_to_target: supports
artifact_role: theorem_plus_decisive_artifact
next_trace_action: "independent affected-source confirmation and exact-source finite evidence; broader interpretation deferred"
conditional_surface_status: "complete finite-law identities under the explicit domains and bond convention; historical estimates excluded"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The [axioms memo](MINIMAL_AXIOMS_2026-06-29.md) provides framework context:
“There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.”; “For each site, the probability
distribution over the possibilities is determined by, and varies with, the
nearest-neighbor conditions.”; “Records form.”; “Only records are readable.”
These sentences do not select the sphere menu, static reading, product
surface measure, Gaussian reference or beta. All are supplied below. The
finite identities use their explicit definitions, not a theorem asserting
that a physical system adopts them.

The context-only source
`docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`
is read and pinned by the primary for product-law provenance; no theorem from
it is required to prove these identities. The current-main context sources
`docs/ADMISSIBILITY_RULE_SPHERE_STATIC_LAW_ZERO_FIELD_COMPONENT_FOURIER_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md`
and
`docs/ADMISSIBILITY_RULE_CUBIC_WALK_RETURN_SUM_AND_SPHERE_STATIC_MAGNETIZATION_SUFFICIENT_BOUND_BOUNDED_THEOREM_NOTE_2026-09-15.md`
have distinct hypotheses and fixed-component conclusions. They are not
mathematical premises here, and supply no instantaneous-frame transverse
bound. No unpublished sibling result supplies an ordered state.

- **Finite graph.** `T_L=(Z/LZ)^3`, integer `L>=3`, `N=L^3`. Sum once over
  each forward bond `(x,x+e_j)`, `j=1,2,3`, including the periodic seam.
  There are `3N` undirected bonds, and each vertex has six neighbors. This
  convention avoids the side-two parallel-bond ambiguity.
- **Sphere law.** `s_x in S^2`, normalized uniform surface measure `sigma`,
  `beta>0`, `h>=0`, and density
  `w/Z=exp(beta sum_bonds s_x dot s_y + beta h sum_x s_x^3)/Z`
  relative to the product surface measure. The positive smooth finite density
  exists by compactness. Its single-site conditional is proportional to
  `exp(beta s_x dot (sum_neighbors s_y+h e_3))`.
- **Fourier convention.** For a scalar or vector field,
  `fhat(k)=N^(-1/2) sum_x exp(-ik dot x) f_x`,
  `k=2pi n/L`, `n in {{0,...,L-1}}^3`. The graph Laplacian is
  `(Delta f)_x=sum_neighbors(f_x-f_y)` and `E(k)=2 sum_j(1-cos k_j)`.
- **Two frames.** `m=N^(-1)sum_x s_x`. A fixed lab component `s_x^1` is
  perpendicular to the applied field direction `e_3`, independent of the
  sample. For `m!=0`, set `u=m/|m|`, `P=I-u u^T`, `s_x^perp=P s_x`.
  Set `u=e_3` when `m=0`; this defines a measurable projection everywhere.
  The exceptional event has product-surface measure zero: conditional on all
  but one spin, zero total spin requires that remaining spin equal one specified
  point (or an impossible vector); a sphere singleton has measure zero.
  Absolute continuity gives zero probability under the supplied finite law.
  The convention is translation invariant, and even on that event
  `sum_x P s_x=P N m=0`.
- **Projected observables.** `S_perp(k)=E[|shat^perp(k)|^2]/2`, the average
  over the two-dimensional transverse subspace, computed using the full
  three-vector norm. Set `c(beta,k)=beta E(k) S_perp(k)` as notation only,
  and `T(r)=E[s_0^perp dot s_(r e_1)^perp]/2`.
- **Gaussian reference.** `theta_x in R^2`, `sum_x theta_x=0`, density
  proportional to `exp(-(beta/2)sum_bonds |theta_x-theta_y|^2)` with respect
  to Lebesgue measure on that subspace. The removed constant mode is a free
  translation. `G_L(r)=N^(-1)sum_(k!=0) exp(ik dot r)/E(k)`.
- **Rotation.** `L_x F=d/da F(...,R_a s_x,...)|_(a=0)` for rotation about
  `e_2` with `L_x s_x^1=s_x^3`, `L_x s_x^3=-s_x^1`.

## Exact target and obligation graph

| Obligation | Statement | Proof and finite check |
|---|---|---|
| Gaussian covariance | `E[|thetahat^a(k)|^2]=1/(beta E(k))`, `a=1,2`, `k!=0` | real eigenbasis and Fourier covariance; four cubic waves and two ring modes |
| Fixed-axis response | `beta h N E[(m^1)^2]=E[m^3]` | global rotation and bond cancellation; one-site moments and rotation integral |
| Projected mode sum | `N^(-1)sum_k S_perp(k)=E[|s_x^perp|^2]/2` | vector Fourier orthogonality and translation invariance; rational ring data |

## Theorem T1 — complete Gaussian covariance

**Statement.** For the supplied Gaussian law and every nonzero `k`, each
scalar component `a=1,2` satisfies `E[|thetahat^a(k)|^2]=1/(beta E(k))`.
Thus `beta E(k) E[|thetahat^a(k)|^2]=1`,
`E[|thetahat(k)|^2]=2/(beta E(k))`, and
`E[theta_0 dot theta_r]=2G_L(r)/beta`.

**Proof.** Each undirected bond contributes
`(theta_x-theta_y)^2` to the scalar quadratic energy, hence
`sum_bonds(theta_x-theta_y)^2=sum_x theta_x(Delta theta)_x`.
For a plane wave,
`sum_neighbors(exp(ik dot x)-exp(ik dot y))`
`=exp(ik dot x) sum_j(2-exp(ik_j)-exp(-ik_j))`
`=E(k)exp(ik dot x)`. This calculation holds for every stated `L`;
the primary checks four waves on the `4^3` graph. The connected graph has
one constant zero eigenvector, and its real symmetric Laplacian has a real
orthonormal eigenbasis with positive eigenvalues `lambda_r` on the zero-mean
subspace. Writing `theta^a=sum_r q_(r,a) v_r` gives independent real scalar
coordinates with density proportional to
`product_(r,a) exp(-beta lambda_r q_(r,a)^2/2)`.
The one-dimensional Gaussian integral, scaled by `sqrt(beta lambda_r)`,
gives variance `1/(beta lambda_r)`. Consequently
`Cov(theta^a)=(beta Delta)^(-1)` on this subspace and the two components
are independent copies. Transforming this covariance by the unitary Fourier
matrix gives `E[thetahat^a(k) conjugate(thetahat^a(l))]`
`=delta_(k,l)/(beta E(k))` for nonzero modes. The coordinates at `k` and
`-k` are complex conjugates for a real field; they are not separate independent
complex Gaussians. Self-conjugate modes are real. The covariance formula
covers both cases without an extra factor. Inverse transforming yields
`E[theta_0^a theta_r^a]=G_L(r)/beta`; summing the two components gives the
stated factor two. The primary separately verifies the inverse eigenvalues
on a four-site ring. This completes the proof. ∎

This is an exact reference law. Approximating the nonlinear sphere law by
it, or taking an ordered-state or large-beta limit, would require additional
error estimates not supplied here.

## Theorem T2 — complete fixed-axis response identity

**Statement.** On the supplied finite sphere torus, for `h>0`,
`beta h N E[(m^1)^2]=E[m^3]`. Therefore the fixed lab-axis zero-mode
mean-square is `E[|shat^1(0)|^2]=N E[(m^1)^2]=E[m^3]/(beta h)`.
At `h=0` the undivided identity also holds; division by `h` is not used.

**Proof.** Surface measure is invariant under `R_a`, so for smooth `F`,
`integral L_x F d sigma(s_x)=0`. Applying this to `Fw` and dividing by the
partition function gives `E[L_x F]=-E[F L_x log w]`. Take
`F=sum_y s_y^1=N m^1` and sum over `x`. The left side is
`E[sum_x L_x F]=E[sum_x s_x^3]=N E[m^3]`. On the right,
`sum_x L_x log w`
`=beta sum_x sum_(y~x)(s_x^3 s_y^1-s_x^1 s_y^3)-beta h sum_x s_x^1`.
For each bond its contribution from `x` is the negative of that from `y`;
all bond terms cancel exactly, leaving `-beta h F`. Hence
`N E[m^3]=beta h E[F^2]=beta h N^2 E[(m^1)^2]`.
Dividing by `N` yields the identity. The original extra `/N` in this
penultimate step is corrected. The one-site instance follows also by
integrating the exponential density: `kappa E[(s^1)^2]=E[s^3]` for
`kappa=beta h`. The primary evaluates those moments and checks the generator
and the zero surface integral of `L(s^1 s^3)=(s^3)^2-(s^1)^2`. ∎

At fixed finite `N`, inversion `s->-s` at zero field gives `E_0[m^3]=0`.
The bounded finite integrands make partition function and numerator analytic
in real `h` near zero, with positive denominator. Thus `E_h[m^3]=O(h)`.
More explicitly, differentiating at zero gives
`d E_h[m^3]/dh|_0=beta N E_0[(m^3)^2]`; rotational invariance gives
`E_0[(m^3)^2]=E_0[(m^1)^2]<=1/3` because `|m|<=1`.
The ratio in the statement has finite limit `N E_0[(m^1)^2]<=N/3`.
No divergent finite-volume response or thermodynamic order of limits is
asserted. This response is not the instantaneous-frame zero mode below.

## Theorem T3 — complete projected vector mode sum

**Statement.** For the supplied translation-invariant finite sphere law,
`N^(-1)sum_k S_perp(k)=E[|s_x^perp|^2]/2`
`=E[1-(s_x dot u)^2]/2` for every site `x`. Moreover
`shat^perp(0)=0` for every configuration under the defined convention.

**Proof.** Finite Fourier orthogonality says
`sum_k exp(ik dot (y-x))=N delta_(x,y)`: each coordinate sum is `L` when
the coordinate difference is zero modulo `L` and otherwise is the geometric
sum of nontrivial roots of unity, equal to zero. For any vector field `v`,
expand the squared transformed norm:
`sum_k |vhat(k)|^2`
`=N^(-1)sum_(x,y) v_x dot v_y sum_k exp(ik dot (y-x))`
`=sum_x |v_x|^2`.
Apply this samplewise to `v_x=P s_x`, take expectations, and divide by `2N`.
The projection is measurable and `|P s_x|<=1`, so all finite averages exist.
Translation leaves `m`, `u` and `P` unchanged and permutes the sites; the
supplied law is translation invariant. Thus each expected local norm is the
same, giving the claimed site-independent right side. Since `|s_x|=|u|=1`,
`|P s_x|^2=1-(s_x dot u)^2`. Finally
`sum_x s_x^perp=P sum_x s_x=P N m=0`, both for nonzero `m` and by the
chosen convention for `m=0`; its Fourier zero mode therefore vanishes.
The primary's four-site rational test uses an unnormalized transform and
checks the equivalent identity `sum_k |F(k)|^2/N=sum_x |f_x|^2`. ∎

A rigid rotation preserves scalar products and squared projected norms, but
it does not replace this configuration-dependent projection by a fixed
laboratory component. No comparison bound is inferred from such a rotation.

## No-Go Discipline Gate — DEFERRED applicability record

This live row contains the three positive finite identities. The original
four concerns and broader conclusions are fully recoverable in history;
they do not constitute five closed route families. No negative or exhaustive
certification is claimed.

- **N1 — DEFERRED.** Frame choice, longest mode, equilibration/aligned start,
  and bounds' hypotheses are the four recorded concerns. Their original
  replies do not close the observable and uncertainty gaps. No fifth route
  is invented.
- **N2 — Wall independence.** No repository no-go wall is used in the three
  finite proofs; this is not a negative-certification PASS.
- **N3 — Hidden premises.** Finite volume, beta positivity, surface measure,
  field, bond convention and Gaussian reference are explicit supplies. No
  physical order, coupling or infinite-volume state is inferred.
- **N4 — Citation roles.** The axioms are framework context. Product-law and
  zero-field Fourier/return-sum notes are context only, not proof imports.
  The finite Fourier, Gaussian and rotation calculations are supplied in full.
- **N5 — Resolution.** The runner checks finite matrix elements, one-site
  moments, four cubic waves, two ring modes, one rational ring mode sum and
  a surface integral. Arbitrary finite tori are covered by written proofs,
  not by numerical execution. Historical samplers are not primary evidence.
- **N6 — Partial closure.** Retain complete finite proofs and exact history.
  Broader normalization, asymptotic and physical conclusions stay deferred;
  preserve the original branch on partial closure. No primitive selects them.
- **N7 — Strong objection.** Finite estimates of a sample-dependent
  projection do not identify an infinite fixed-component response. This is
  accepted as a scope limitation; no error bars or equilibration guarantee
  are supplied to answer it.
- **N8 — Earlier work.** The current-main fixed-component results do not
  restore the withdrawn transverse identification. Historical numerical
  agreements and disagreements remain history, without cross-cycle promotion.

## Boundaries and non-claims

{fences[0]}

{fences[1]}

{fences[2]}

## Falsifiers and evidence targets

An incorrect forward-bond eigenvalue or scalar inverse covariance contradicts
the Gaussian formula. A failure of global rotation bond cancellation or the
one-site identity contradicts the response derivation. A failure of finite
Fourier orthogonality contradicts the mode sum. The projected zero-mode
cancellation distinguishes the two frames. The existing primary's five
mathematical checks address the listed finite fixtures; global bond and
projected-zero-mode decisive controls should be bound separately before any
new evidence is called complete. They were independently checked in the
original review, not executed by this primary during preparation.

## Imports

Finite-dimensional real spectral theorem, Gaussian integration, invariance
of sphere surface measure under rotations, differentiation of bounded
finite-volume integrals, and finite Fourier orthogonality are the only
mathematical tools. The covariance, cancellation and mode-sum calculations
are written above. No phase, selected-state, infinite-volume or physical
normalization theorem is imported. Historical heat-bath and proposal chains
are not part of the proof or runtime closure.

## Verification

The primary has 14 check invocations and seven mutation definitions. Its five
mathematical checks use exact symbolic/integer/rational calculations; four
source checks, four packaging checks and one resolution-line check complete
the total. Expected successful output is `TOTAL: PASS=14 FAIL=0`; this is an
expectation, not a new execution receipt. The original cache is archived and
must not be relabelled as evidence for these corrected bytes. The primary
writes stdout only and no JSON or simulation output.

```bash
python3 {runner}
python3 {runner} --list-mutations
python3 {runner} --mutation sum_rule_wrong
```
'''
emit(note,newnote)
s=(O/oldrun).read_text();docstart=s.index('"""');docend=s.index('"""',docstart+3)+3
s=s[:docstart]+'''"""Exact finite checks for the supplied Gaussian covariance, fixed-axis sphere
response and projected-field mode-sum proof. Four cubic plane waves, two ring
inverse eigenvalues, one-site exponential moments, a rotation surface integral
and rational ring Fourier data are checked symbolically. No two-site quadrature,
sampler or empirical normalization is executed. Arbitrary-volume statements
and the distinction between frames are written proofs, not simulation results.
"""'''+s[docend:]
s=s.replace('import itertools','import hashlib\nimport itertools',1).replace(oldnote,note).replace(Path(oldnote).stem.lower(),cid)
s=s.replace('AUDIT_TIMEOUT_SEC = 900','AUDIT_TIMEOUT_SEC = 60')
inputs=[note,'docs/MINIMAL_AXIOMS_2026-06-29.md','docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md']
pins={p:sha((W/p).read_bytes()) for p in inputs}
s=s.replace('ROOT = Path(__file__).resolve().parents[1]','INPUT_SHA256 = '+repr(pins)+'\nROOT = Path(__file__).resolve().parents[1]')
s=s.replace('all(Path(ROOT, p).exists() for p in AUDIT_INPUT_PATHS)','all(Path(ROOT, p).is_file() and hashlib.sha256(Path(ROOT, p).read_bytes()).hexdigest() == INPUT_SHA256[p] for p in AUDIT_INPUT_PATHS)')
s=s.replace('"all declared inputs exist"','"all three declared source/context inputs match literal SHA-256 pins"')
s=s.replace('"block 01\'s note (on main) carries its claim_id and the rule\'s product form"','"the context-only finite-menu note carries its identity and product-law heading; no sphere bound is imported"')
s=s.replace('Check L in spherical coordinates: L = -d/dtheta for the polar angle\n    # measured from e_3 in the (1,3) plane, and the surface measure\'s invariance under this rotation.', 'Check the specified rotation directly in Cartesian components and check\n    # the surface measure\'s invariance; no global polar-angle derivative formula is assumed.')
s=s.replace('T3: Parseval on a 4-site ring with rational data: N^{-1} sum_k |f_hat(k)|^2 = sum_x f_x^2, so the transverse structure factor\'s average is the local transverse moment', 'T3: the unnormalized 4-site rational ring transform obeys sum_k |F(k)|^2/N = sum_x f_x^2; the vector projection and translation steps are written proofs')
a=s.index('FENCES = (');b=s.index('FORBIDDEN = (',a);s=s[:a]+'FENCES = '+repr(fences)+'\n'+s[b:]
# Names of mathematical identities and legitimate limit vocabulary are not overclaims.
s=s.replace(', "converge"','').replace(', "Parseval", "Ward"','')
a=s.index('N5_LINES = (');b=s.index('\n\n\ndef family_g',a)
n5=(
'per_element: executed — exact 64-by-64 Laplacian entries and four plane-wave identities; scalar covariance factors checked on a ring',
'per_site: executed — one-site exponential moments and the rotation surface integral; no stochastic spin updates or field-chain estimates',
'per_mode: executed — four selected cubic waves, two selected ring inverse eigenvalues and four rational Fourier coefficients; no all-mode numerical sweep',
'per_block: executed — one finite cubic matrix and finite ring fixtures; no sampled spatial blocks, measured normalization or simulation output',
'lattice_wide: checked and not executed — arbitrary finite-volume covariance, global rotation cancellation and projected vector mode sum are written proofs')
s=s[:a]+'N5_LINES = '+repr(n5)+s[b:]
compile(s,runner,'exec');emit(runner,s,0o755)
oldast=ast.parse((O/oldrun).read_text());newast=ast.parse(s)
class Normalize(ast.NodeTransformer):
 def visit_Constant(self,n):return ast.copy_location(ast.Constant('<text>'),n) if isinstance(n.value,str) else n
checks={}
for name in ['family_b','family_c','family_d']:
 a=next(x for x in oldast.body if isinstance(x,ast.FunctionDef) and x.name==name);b=next(x for x in newast.body if isinstance(x,ast.FunctionDef) and x.name==name)
 checks[name]=ast.dump(Normalize().visit(a))==ast.dump(Normalize().visit(b));assert checks[name]
paths=subprocess.check_output(['git','-C',str(W),'ls-files','--others','--exclude-standard'],text=True).splitlines();assert len(paths)==25,len(paths)
rows=[dict(path=p,mode='100755' if (W/p).stat().st_mode&0o111 else '100644',sha256=sha((W/p).read_bytes())) for p in paths]
snap=R/'drain8173-prepared-source-v1';assert not snap.exists()
for p in paths:(snap/p).parent.mkdir(parents=True,exist_ok=True);shutil.copy2(W/p,snap/p)
prepared=dict(schema_version=1,kind='author-preparation-not-review-verdict',pr=8173,owner='PR8173-author',base=BASE,head=HEAD,source_count=len(rows),source=rows,original_count=20,original_manifest=dict(path=hist+'/pr8173-original-manifest.json',sha256=sha((W/hist/'pr8173-original-manifest.json').read_bytes())),canonical_notes=[note],primaries=[runner],readable_history=[readable],snapshot=str(snap),primary_runs=0,simulation_runs=0,mutation_runs=0,staged=False,mathematical_function_ast_comparison=checks,branch_preservation_required=True)
dump(R/'drain8173-author-prepared-v1.json',prepared)
dump(R/'drain8173-source-freeze-v1.json',dict(schema_version=1,base=BASE,source=rows,snapshot=str(snap),prepared_sha256=sha((R/'drain8173-author-prepared-v1.json').read_bytes())))
dump(R/'drain8173-author-dispositions-v1.json',dict(schema_version=1,constituents=[dict(pr=8173,head=HEAD,dispositions=entries)],claims=[dict(original='T1 Gaussian covariance',destination=note,disposition='complete proof; real eigenbasis, conjugate modes, scalar/two-component factors and beta/L/bond domain explicit'),dict(original='T2 fixed-axis response',destination=note,disposition='complete rotation proof; corrected penultimate N and finite-volume h limit'),dict(original='T3 projected mode sum',destination=note,disposition='complete vector proof, translation invariance, measurable null-event convention and zero-mode cancellation'),dict(original='numerical measurement and asymptotic/physical/bound-transfer claims',destination=readable,disposition='withdrawn live; complete original prose, raw discrepancies, full controls and outputs preserved'),dict(original='N1-N8 negative/exhaustive certification',destination=readable,disposition='deferred, no fifth route invented, original branch preservation required')]))
patch=''.join(difflib.unified_diff(original.splitlines(True),newnote.splitlines(True),fromfile=oldnote,tofile=note))+''.join(difflib.unified_diff((O/oldrun).read_text().splitlines(True),s.splitlines(True),fromfile=oldrun,tofile=runner))
(R/'drain8173-author-corrections-v1.patch').write_text(patch)
print(json.dumps(dict(paths=len(rows),prepared_sha256=sha((R/'drain8173-author-prepared-v1.json').read_bytes()),note_sha256=sha(newnote.encode()),runner_sha256=sha(s.encode())),indent=2))
