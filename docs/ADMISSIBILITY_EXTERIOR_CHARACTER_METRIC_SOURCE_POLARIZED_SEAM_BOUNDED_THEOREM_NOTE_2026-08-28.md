---
claim_id: admissibility_exterior_character_metric_source_polarized_seam_bounded_theorem_note_2026-08-28
final_path: docs/ADMISSIBILITY_EXTERIOR_CHARACTER_METRIC_SOURCE_POLARIZED_SEAM_BOUNDED_THEOREM_NOTE_2026-08-28.md
claim_type: bounded_theorem
claim_scope: "For a supplied compact common-chart positive inverse-metric domain, a supplied compact real scalar-source interval and strictly positive relative source normalization, normalized full-support product measure, the supplied exterior-character plaquette family, and a supplied polarization/mismatch coefficient, one exact finite seam action reduces at the flat zero-source point to the exterior-character action, gives nonzero reciprocal metric/source/connection variations on curved histories, and has a nonnegative joint metric-source-connection Gram expansion for nonnegative coupling. Strict coupling gives an injective temporal-gauge seam operator on the explicit metric quotient and an injective gauge-projected operator only on the gauge-invariant Hilbert space; zero coupling or zero source normalization, coframe gauge copies, shared-variable pullbacks, arbitrary independent coordinate frames, and negative coupling retain exact qualifications. A three-history rational Gram falsifies the naive positive endpoint-average extension. The compact domain, measure, common chart, scalar-source normalization and reading, polarization counterterm, coupling, temporal extension, coframe quotient, and physical metric/source/Hamiltonian interpretation are explicit inputs rather than framework-selected consequences."
runner: scripts/admissibility_exterior_character_metric_source_polarized_seam_2026_08_28.py
independent_checker: scripts/admissibility_exterior_character_metric_source_polarized_seam_independent_2026_08_28.py
status: proposed_retained
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_dirac_kahler_exterior_character_action_transfer_bounded_theorem_note_2026-08-28
target_blocker_text: "derive a metric/source extension with nonzero reciprocal response and re-test the complete coupled reflected kernel"
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Test a supplied gauge-vector matter hopping term on the resulting positive metric/source seam, including the complete gauge-matter projector, strict transfer support, and spectral response; do not identify the scalar source with a Record or physical stress without a separate supplier."
conditional_surface_status: "exact supplied common-chart metric/source seam, reciprocal variations, joint reflection-positive Gram, injectivity qualifications, and naive-average falsifier; no framework-selected metric, source, measure, action, dynamics, or physical identification"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the polarization identity, reciprocal derivatives, finite Gram factorization, strict-support argument, and exact counterexamples are finite mathematical theorems for a fully disclosed supplied family, while every physical supplier remains open"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Metric/source polarized seam for the exterior-character action

**Date:** 2026-08-28

**Type:** `bounded_theorem`

**Status:** `proposed_retained` — a review proposal, not an audit verdict.

## Result up front

The [metric-compatible exterior transport](ADMISSIBILITY_DIRAC_KAHLER_METRIC_COMPATIBLE_EXTERIOR_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-08-27.md)
supplies positive cell metrics and independent orthogonal edge factors.  The
[exterior-character action and transfer theorem](ADMISSIBILITY_DIRAC_KAHLER_EXTERIOR_CHARACTER_ACTION_TRANSFER_BOUNDED_THEOREM_NOTE_2026-08-28.md)
then shows that its fixed-weight connection action has exactly zero endpoint
metric response.  This note supplies one new metric/source seam and asks the
complete question again: does the same coupled action have reciprocal
connection, metric, and source variation, and is its full reflected kernel
positive?

The answer is conditionally yes.  Put a positive inverse metric `G` and one
real scalar source coordinate `r` in a common seven-dimensional Euclidean
feature space.  For reflected data `X=(G,r)`, `Y=(H,s)` and relative
orthogonal holonomy `W`, define

```text
S_(n,kappa)(X,U;Y,V)
  = kappa b(X,Y) f_n(Q(W))
    + (8 kappa/n) ||X-Y||_b^2,                  (1)
W = U V^-1.
```

At `X=Y=(I,0)`, equation (1) is exactly the prior supplied action
`kappa f_n(Q)`, including `kappa Q` when `n=1`.  The mismatch term is not
decoration.  It cancels the constant part of `f_n` and yields

```text
exp[-S_(n,kappa)]
 = d(X)d(Y)
   exp[c_(n,kappa) b(X,Y) chi(W)^n],            (2)
```

where `chi=Tr Lambda^*(W)`, `d>0`, and `c_(n,kappa)>=0` for
`kappa>=0`.  Both `b(X,Y)` and `chi(UV^-1)^n` are Gram kernels.  Their product
and exponential therefore have an exact nonnegative tensor-feature
expansion.  This proves joint metric/source/connection reflection positivity,
not merely positivity after freezing the new variables.

The same action gives nonzero metric and source response on the displayed curved matched
histories and exact equality of the mixed variation in either order.  On the
improper holonomy component, metric/source response can be nonzero for
nonzero coupling and suitable matched features/directions although the
within-component connection force is zero.  A naive replacement
`kappa Q -> kappa(v+w)Q/2` with positive endpoint weights fails: an exact
three-history normalized Gram has determinant `-1/64`.

Nothing here derives the metric, source, measure, seam action, or physical
interpretation from the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).  The
common chart, compact domain, polarization coefficient, temporal extension,
and physical reading remain disclosed inputs.  This is not an Einstein
equation, a Record source law, local coordinate covariance, Lorentz
covariance, or a physical Hamiltonian theorem.

## Imports and open boundaries

| Input | Role | Provenance | Open boundary |
|---|---|---|---|
| orthogonal seam variables `U,V` and defect `Q(UV^-1)` | connection/curvature carrier | supplied by the linked exterior-character parent on its conditional chain | physical selection of the orthogonal connection remains open |
| positive inverse metric `G=E^T E` | dynamic seam feature | linked metric-compatible parent supplies the metric/coframe distinction; compact domain below is new | no framework-selected metric field, coordinate law, or gravity meaning |
| real scalar coordinate `r` and relative normalization `alpha>0` | source feature and its scale inside the joint inner product | supplied mathematical variable and convention | neither scale nor variable is selected or identified as Record content, matter density, or energy |
| common lattice coordinate chart | makes `Tr(GH)` a cross-seam pairing | supplied global cubical chart | independent local coordinate frames require a separately supplied trivialization |
| compact domains `K_(epsilon,M)` and `[-R,R]` | control continuity, full support, and metric-tail separation | supplied finite domains | no noncompact or continuum completion follows |
| normalized full-support Lebesgue/Haar product measure | finite reflected integration | supplied mathematical measure | no metric-dependent or physical path measure is derived |
| `f_n`, `kappa`, and the mismatch coefficient `8 kappa/n` | complete action tested | supplied definition (1) | neither the member `n`, magnitude, sign, nor polarization law is selected |
| temporal seam, link reflection, gauge-invariant spatial half-action, and temporal-link Haar projection | OS/transfer construction | supplied finite extension, including `[M_m,P]=0` | no clock, physical time, or Lorentzian continuation follows |
| metric quotient rather than raw coframes | domain of the strict-support statement | required because `E` and `QE` give the same `G` | no injective operator on unquotiented coframe copies is claimed |
| physical metric/source stress and Hamiltonian readings | none | absent | mathematical derivatives and spectral logarithms are not renamed as physical observables |

The scalar coordinate may have either sign.  The proof uses the Euclidean
feature inner product, not pointwise positivity of `b(X,Y)`.  Compactness makes
the action finite even when the cross pairing is negative.

## Supplied metric/source feature

Let

```text
K_(epsilon,M)
 = {G in Sym(3,R): epsilon I <= G <= M I},
X = (G,r) in K_(epsilon,M) x [-R,R],               (3)
```

with fixed `0<epsilon<M` and finite `R`.  The general theorem uses any such
domain with nonempty interior.  The explicit reduction and witnesses below
use the compatible supplied choice `epsilon<=1`, `M>=4`, and `R>=1`, so
that `I`, `2I`, `diag(1,2,3)`, `diag(4,1,1)`, and the source values
`0,1/2,1` lie in the domain.  The source interval is nontrivial.
Read `G=E^T E` as the positive
inverse metric Gram from the compatible transport theorem.  Define

```text
b_alpha((G,r),(H,s)) = Tr(GH)/3 + alpha r s,
||X||_b^2 = b(X,X).                                (4)
```

Here `alpha>0` is a supplied relative source normalization; the exact witness
below uses `alpha=1`.  Equation (4) is the restriction of the ordinary
Euclidean inner product after rescaling the scalar coordinate by
`sqrt(alpha)`.  In particular, `b` is a positive-definite kernel
even though an off-diagonal value can be negative.  For positive `G,H`,
`Tr(GH)>0` because it equals
`Tr(G^(1/2) H G^(1/2))`.
Below `b` abbreviates `b_alpha` at the disclosed fixed `alpha`.

A simultaneous proper-cubic frame change acts by

```text
G -> C G C^T,   H -> C H C^T,   r -> r,   s -> s,
C^T C=I.                                             (5)
```

Cyclicity of trace proves that (4) is invariant.  Equation (5) does not
license independent changes `C_G,C_H`.  Metrics in separate local coordinate
charts need a factorized map into one seam space before (4) is meaningful.
An arbitrary pairwise transporter is not enough for the Gram proof.

The left-orthogonal coframe gauge is already quotiented:

```text
E -> Q E,   Q in O(3),   (QE)^T(QE)=E^T E.          (6)
```

Thus the kernel can separate metrics but cannot distinguish raw coframe gauge
copies.  This exact null direction is retained below.

## Exterior-character action and the polarization identity

Let `rho=Lambda^* R^3` and

```text
chi(W)=Tr rho(W),
Q(W)=16-2 chi(W),
f_n(Q)=16/n - 2 chi(W)^n/[n 8^(n-1)],   n>=1.       (7)
```

For `O(3)`, `0<=chi<=8`, so `0<=f_n<=16/n`.  The linear member is
`f_1(Q)=Q`.  Substitute (7) and

```text
||X-Y||_b^2=||X||_b^2+||Y||_b^2-2b(X,Y)            (8)
```

into (1).  The terms `16 kappa b(X,Y)/n` cancel exactly:

```text
S_(n,kappa)
 = (8 kappa/n)(||X||_b^2+||Y||_b^2)
   - [2 kappa/(n 8^(n-1))] b(X,Y) chi(W)^n.         (9)
```

Therefore (2) holds with

```text
d(X)=exp[-8 kappa ||X||_b^2/n],
c_(n,kappa)=2 kappa/[n 8^(n-1)].                   (10)
```

The coefficient `8 kappa/n` in (1) is load-bearing.  Replacing it by an
independently chosen geometry stiffness leaves an uncancelled cross term and
requires a fresh Fourier/Gram sign audit.  Equation (1) is one supplied
polarized action, not the unique way to couple a metric or source.

## Exact reciprocal variations

Let `dot X=(dot G,dot r)` and vary the left seam feature while holding the
right feature and connection fixed.  Direct differentiation of the same
action gives

```text
D_X S[dot X]
 = kappa b(dot X,Y) f_n(Q)
   + (16 kappa/n) b(dot X,X-Y).                    (11)
```

For a left connection variation `U(t)=exp(tZ)U`, `Z in so(3)`,

```text
D_U S[Z]
 = kappa b(X,Y) f_n'(Q) D_U Q[Z].                 (12)
```

The ordered plaquette derivative `D_UQ` is exactly the one derived in the
linked exterior-character action theorem.  No untransported plaquette words
from different base points are added here.

Equations (11)–(12) have exact mixed reciprocity:

```text
D_X D_U S[dot X,Z]
 = D_U D_X S[Z,dot X]
 = kappa b(dot X,Y) f_n'(Q) D_UQ[Z].              (13)
```

In coordinates,

```text
D_G S[dot G]
 = (kappa/3)Tr(dot G H) f_n(Q)
   + (16 kappa/(3n))Tr[dot G(G-H)],                (14)

partial_r S
 = alpha kappa s f_n(Q)
   + (16 alpha kappa/n)(r-s).                      (15)
```

At a matched seam `G=H,r=s`, the mismatch response vanishes but the curvature
response remains:

```text
D_GS[dot G] = (kappa/3)Tr(dot G G) f_n(Q),
partial_r S = alpha kappa r f_n(Q).                (16)
```

This is nonzero stress/source response only because the new complete action
depends on the metric and scalar features.  It does not contradict the fixed-
weight zero derivative of the source-free parent.

If the covariant metric is `g=G^-1`, then
`dot G=-G dot g G`.  Translating (14) into a derivative with respect to `g`
is a chain rule, not a gravity equation.  If the orthogonal connection is
later made a function of `G`, its chain-rule contribution must also be added;
it is held independent in (11)–(16).

## Exact curved witness

Take the linear member `n=1`, `kappa=1`, `alpha=1`,

```text
G=H=diag(1,2,3),      r=s=1/2,
W = [[3/5,-4/5,0],[4/5,3/5,0],[0,0,1]].            (17)
```

The rotation has `cos(theta)=3/5`, so

```text
Q(W)=8(1-cos theta)=16/5,
b(X,X)=Tr(G^2)/3+r^2=59/12,
S=236/15.                                           (18)
```

For `dot G=diag(1,0,0)`, equations (14)–(16) give

```text
D_GS[dot G]=16/15,       partial_r S=8/5.           (19)
```

Varying the rotation angle has `D_theta Q=8 sin(theta)=32/5`.  Hence the two
mixed derivatives are, exactly,

```text
D_GD_theta S[dot G]=32/15,
partial_r D_theta S=16/5.                           (20)
```

Every number in (18)–(20) is derived rationally from the supplied witness; no
floating-point value is reconstructed as exact.

## Improper component and topology boundaries

For every improper `W in O(3)`, `chi(W)=0`, so

```text
Q(W)=16,       f_n(Q(W))=16/n.                     (21)
```

The character is constant within that component.  Thus `D_UQ=0` for every
continuous tangent variation that stays improper, and (12) vanishes.  At a
matched curved feature with `kappa!=0`, a nonzero source response additionally
needs `r!=0`, and a nonzero metric response needs a direction with
`Tr(dot G G)!=0`.  Under those explicit conditions (14)–(16) can be nonzero;
for example `n=kappa=alpha=1`, `G=I`, `r=1`, and
`dot G=diag(1,0,0)` give metric response `16/3` and source response `16`.
The action can therefore give metric/source response with no within-component
connection force.  This does not select the proper determinant sector: both a proper
`pi` rotation and every improper holonomy have `Q=16`.

The seam construction is local.  It does not remove noncontractible flat
holonomies on a spatial torus, and it supplies no plaquette Bianchi-to-source
conservation theorem.  Spatial topology may be open or periodic in the finite
reflection proof, but global flat-sector selection remains separate.

## Joint reflection-positive Gram

Let `mu_X` be a supplied normalized full-support measure on the compact domain
(3) and use normalized Haar measure on `O(3)`.  For `kappa>=0`, expand (2):

```text
exp[-S_(n,kappa)]
 = d(X)d(Y) sum_(m>=0) c_(n,kappa)^m/m!
     b(X,Y)^m chi_(rho^(tensor nm))(UV^-1).         (22)
```

The first factor in each summand is the Gram kernel of
`X^(tensor m)` in `Sym^m(Sym(3) direct_sum R)`.  The character factor is the
trace of the unitary representation `rho^(tensor nm)` and hence a sum of
matrix-coefficient squares across the reflection.  Their product is the Gram
kernel of the tensor-product feature

```text
X^(tensor m) tensor rho^(tensor nm)(U).             (23)
```

Every coefficient in (22) is nonnegative.  Uniform convergence on the compact
domain permits termwise finite integration.  Thus any finite product of seam
factors has a sum-of-squares reflected form.  Real reflection-matched spatial
half-actions are absorbed as positive diagonal multipliers exactly as in the
source-free transfer construction.

Restoring temporal vertex links Haar-averages the group variables by the
orthogonal gauge projector `P`.  The metric and scalar variables are gauge
singlets.  Projection preserves the nonnegative form, so the complete finite
metric/source/connection seam is reflection positive for `kappa>=0`.

If multiple crossing plaquettes share one metric/source variable, identifying
their feature coordinates is a pullback of a positive kernel and preserves
positivity.  Such an identification need not preserve strict feature
separation; injectivity on an aggregated metric model requires a separate
proof.  The strict theorem below is for the explicit site-separating seam
domain or its tensor product.

## Transfer, strict support, and logarithm

For one seam item, let `C_(n,kappa)` be the integral operator with kernel
(22) on

```text
L^2(K_(epsilon,M) x [-R,R] x O(3), mu_X x Haar).    (24)
```

It is continuous on a compact domain, hence Hilbert–Schmidt, bounded, compact,
self-adjoint, and positive for `kappa>=0`.

For `kappa>0` and `alpha>0`, it is injective on (24).  The proof has two exact ingredients.
First, every `O(3)` irrep occurs in `rho^(tensor nm)` for all sufficiently
large `m`: `rho=1 direct_sum det direct_sum V direct_sum det tensor V`, and
the trivial summand pads tensor degree.  Second, homogeneous metric/source
polynomials of all sufficiently large degrees are dense on (3).  Indeed
`ell(X)=Tr G` has the strict lower bound `3 epsilon`; for a continuous target,
approximate its quotient by `ell^M` with ordinary polynomials and multiply
back by `ell^M`.  The resulting polynomial uses only degrees at least `M`.
Peter–Weyl and polynomial density then show that a vector orthogonal to every
feature (23) vanishes.  The multiplier `d` is boundedly invertible on the
compact domain.

At `alpha=0`, every pair of states that differs only in the scalar coordinate
has an identical kernel row.  The metric/connection subkernel remains
positive, but source injectivity and nonzero source response are lost.  A
negative `alpha` is not covered because (4) is then not the Euclidean feature
inner product used in (22).  More sharply, with equal group elements,
`G=H=I`, sources `0,1`, `n=1`, and `kappa=log(2)/8`, taking `alpha=-1`
makes the Boltzmann-kernel off-diagonal equal to `2`; its two-history Gram is again
`[[1,2],[2,1]]` and is indefinite.

For a finite site-separating product and a reflection-matched continuous,
gauge-invariant spatial half-action `S_sp`, the one-step operator is

```text
T = M_m P C M_m,       m=exp(-S_sp/2),              (25)
```

where `M_m` is multiplication by the displayed `m`; it is strictly positive
and boundedly invertible on the compact domain.  Gauge invariance is the
load-bearing inherited hypothesis `[M_m,P]=0`, so the restriction to `P H`
is well typed.  In temporal
gauge before `P`, strict positive couplings give injectivity.  After temporal-
link integration, injectivity holds only on the gauge-invariant Hilbert space
`P H`, never on the full kinematic space when the gauge action is nontrivial.

At `kappa=0`, the complete joint kernel is constant and rank one.  Because the
metric/source domain is nontrivial, the physical-space operator is already
noninjective even when the spatial gauge graph is a forest.  If raw coframes
rather than `G` are retained, equation (6) supplies further exact null
directions.  No coframe-level injectivity is claimed.

On an injective positive carrier, normalize by the top eigenvalue and define
the densely defined self-adjoint logarithm by spectral calculus.  If a gauge,
aggregation, coframe, or zero-coupling kernel remains, restrict to the support
or OS null quotient first.  The logarithm is a finite mathematical transfer
generator, not an identified physical Hamiltonian or clock.

## Negative coupling and the naive-average falsifier

For negative `kappa`, set `X=Y=(I,0)` so the mismatch term vanishes.  Choose
`r=diag(-1,-1,1) in SO(3)`, for which `f_n(Q(r))=16/n`, and take

```text
kappa = -n log(2)/16.
```

The exact two-history Gram is

```text
[[1,2],[2,1]],                                       (26)
```

with eigenvalues `3,-1`.  Positive half-action multipliers only apply an
invertible diagonal congruence and cannot repair the negative inertia.

An exact positive hostile control shows what the polarization repairs.  Take
`n=1`, `alpha=1`, `kappa=log(2)/8`, zero scalar source, and

```text
y_1=(I,I),   y_2=(diag(4,1,1),I),   y_3=(I,r).
```

The polarized Gram is

```text
G_pol = [[1,1/8,1/4],
         [1/8,1,1/128],
         [1/4,1/128,1]].
```

Its leading principal minors are `1`, `63/64`, and `15111/16384`, so it is
positive definite.  This is a control for (29), not a finite sample standing
in for the general proof (22).

More subtly, positive endpoint metric weights do not by themselves imply
joint positivity.  Consider the naive action

```text
S_av((v,U),(w,V))=kappa(v+w)Q(UV^-1)/2,             (27)
```

where `v=Tr G/3>0`.  Take

```text
x_1=(I,I),   x_2=(2I,I),   x_3=(I,r),
kappa=log(2)/8.                                     (28)
```

Because `Q(I)=0` and `Q(r)=16`, the already diagonally normalized Gram is

```text
G_av = [[1,1,1/4],
        [1,1,1/8],
        [1/4,1/8,1]],
det G_av = -1/64.                                   (29)
```

Thus pointwise-positive geometry coefficients and positive Boltzmann weights
are insufficient.  The polarized Gram structure of (1), not positivity of an
endpoint average, is what proves (22).  This exact falsifier is narrow: it
does not say that every metric-dependent Wilson action fails reflection
positivity.

## Nonselection and strongest missing lemma

Every `n>=1` admits the same construction (1)–(23).  Metric/source response,
joint reflection positivity, and strict seam support therefore do not select
the linear member `f_1=Q`.  Changing the compact domain, measure, feature
normalization, source coordinate, or polarization law gives further supplied
families.  None is selected by consistency alone.

The strongest missing lemma is a framework-native supplier for the actual
metric/source feature, its common-chart or local-trivialization law, the
polarized action and measure, and the physical identification of (14)–(16),
with a selected coupling and source observable.  Without that supplier this
note is a nonvacuous conditional model and discriminator, not near closure of
metric dynamics or gravity.

## Proof-obligation graph

| Obligation | Status |
|---|---|
| positive metric/source feature pairing | proved by (3)–(5) |
| exact reduction to the source-free action | proved by (1) at `X=Y=(I,0)` |
| polarization cancellation | proved by (7)–(10) |
| metric/source/connection variation | proved by (11)–(16) |
| nonzero exact witness | proved by (17)–(20) |
| improper-sector response boundary | proved by (21) |
| full joint reflection-positive Gram | proved by (22)–(23) |
| strict seam injectivity | proved on the metric quotient by representation support and polynomial-tail density |
| negative sign falsifier | proved by (26) |
| naive positive-average falsifier | proved by (27)–(29) |
| physical metric/source/action selection | open; strongest missing lemma above |
| local-coordinate, continuum, Lorentz, or gravity law | open and not approached by relabeling |

The graph is acyclic.  The physical target-equivalent supplier is not used to
prove the finite conditional theorem.

## No-Go Discipline Gate

The theorem includes bounded negative statements, so N1–N8 are recorded even
though the claim type is not `no_go`.

### N1 — alternative routes

| Route | Attempt and result | Exact authority / residual | Marker |
|---|---|---|---|
| fixed metric/source multipliers | Keep geometry and source external in the spatial half-action.  This preserves the old crossing Gram but supplies no dynamic seam measure or strict source support. | This note, Imports table and (25); exterior-character parent, metric/source boundary. | `ATTEMPTED` |
| positive endpoint average | Use (27) with positive metric weights.  The exact Gram (29) is indefinite. | This note, (27)–(29). | `ATTEMPTED` |
| independent local coordinate frames | Pair metrics only after unrelated endpoint frame changes.  `Tr(GH)` is not invariant and a cocyclic/factorized trivialization is missing. | This note, (4)–(6). | `ATTEMPTED` |
| raw coframe kernel | Replace `G` by `E` and seek full injectivity.  Left-orthogonal gauge copies have identical metric rows. | This note, (6) and transfer qualifications. | `ATTEMPTED` |
| zero source normalization | Set `alpha=0` while retaining a nontrivial scalar interval.  Distinct scalar histories then have identical kernel rows, so source response and strict source support fail. | This note, source-scale boundary and exact zero-scale Gram. | `ATTEMPTED` |
| negative crossing coupling | Reverse the crossing sign while retaining the displayed exterior-character action.  The exact two-history Gram (26) has eigenvalue `-1`. | This note, (26) and exact runner witness. | `ATTEMPTED` |

The failed average and coframe routes are exact boundaries only for their
displayed mechanisms.  The successful polarized common-chart feature (1) is
the shipped construction and is not counted as a failed attack route.  Three
routes were deliberately not counted as attempts here: a metric-dependent
integration measure, a gauge-vector matter
source, and a Record/physical-source supplier.  Each remains live and would
require respectively a reflected-measure Gram, a joined gauge-matter action,
or a native readout-to-action identification.  Local trivializations and
other metric-dependent actions also remain live.

### N2 — wall independence

Dependencies are collapsed before the pairwise audit.  The compact metric and
source domains, common chart, pairing, and quotient jointly type one feature
carrier.  The member `f_n`, sign, magnitude, and mismatch coefficient jointly
define one action-polarization unit.  Seam reflection, temporal links, spatial
half-actions, and gauge projection jointly define one temporal-gauge unit.

| Label | Independently closable wall | Deliberate collapse |
|---|---|---|
| feature-carrier | compact positive metric domain, scalar interval and positive relative normalization, common chart, Euclidean pairing, and metric quotient | these jointly type `X` and `b` |
| action-polarization | `f_n`, coupling, sign, and mismatch coefficient | positivity is a property of this complete action, not isolated coefficients |
| measure | full-support metric/source measure and Haar connection measure | required for the stated Hilbert operator, not for the algebraic identity |
| temporal-gauge | reflection, crossing assignment, temporal links, half-action, and physical gauge subspace | these jointly type the OS/transfer construction |
| aggregation | map identifying local seam features into a shared metric/source field | pullback preserves positivity but may change injectivity |
| connection-selection | physical selection of the orthogonal edge factors | not supplied by the coupled seam |
| source-identification | physical meaning of `r` | does not identify a metric derivative or select its action |
| stress-identification | physical meaning of derivatives (14)–(16) | does not identify the scalar coordinate as a Record or matter source |
| continuum-scaling | refinement and continuum limit | does not select a Lorentzian continuation or time observable |
| Lorentzian-continuation | continuation from the finite Euclidean seam | does not prove a continuum limit or identify a Hamiltonian |
| Hamiltonian-identification | physical meaning of the transfer logarithm | does not select a clock or Lorentzian continuation |
| clock-identification | physical time observable | does not establish continuum scaling or identify the logarithm as its generator |

In the table, `I` means closing either named unit does not close the other; the
diagonal is `--`.

| | feature | action | measure | temporal | aggregation | connection | source-reading | stress-reading | continuum | Lorentzian | Hamiltonian-reading | clock-reading |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| feature | -- | I | I | I | I | I | I | I | I | I | I | I |
| action | I | -- | I | I | I | I | I | I | I | I | I | I |
| measure | I | I | -- | I | I | I | I | I | I | I | I | I |
| temporal | I | I | I | -- | I | I | I | I | I | I | I | I |
| aggregation | I | I | I | I | -- | I | I | I | I | I | I | I |
| connection | I | I | I | I | I | -- | I | I | I | I | I | I |
| source-reading | I | I | I | I | I | I | -- | I | I | I | I | I |
| stress-reading | I | I | I | I | I | I | I | -- | I | I | I | I |
| continuum | I | I | I | I | I | I | I | I | -- | I | I | I |
| Lorentzian | I | I | I | I | I | I | I | I | I | -- | I | I |
| Hamiltonian-reading | I | I | I | I | I | I | I | I | I | I | -- | I |
| clock-reading | I | I | I | I | I | I | I | I | I | I | I | -- |

Exact separators support the closest pairs.  The same feature carrier accepts
the failed average (27) and successful polarization (1), so it does not close
action-polarization.  Equation (9) is algebraic before a measure is chosen.
A full-support measure does not select (1).  Projection can be supplied with a
constant rank-one kernel at zero coupling, so temporal-gauge does not close
action-polarization or strict support.  Independent features give the strict
theorem; a shared-feature pullback preserves positivity but leaves aggregation
injectivity open.  The entire finite construction can be supplied without
selecting the connection, physical source, or stress meaning.  A scalar
reading does not identify a derivative as stress, and a stress convention
does not identify the scalar as matter or Record content.  A continuum
sequence, Lorentzian continuation, transfer-logarithm interpretation, and
clock can likewise be separately stipulated or withheld; none proves another
or proves the finite Gram.

### N3 — hidden-wall scan

The literal scan used `assume`, `assuming`, `suppose`, `choose`, `supplied`,
`canonical`, `background`, `by construction`, and `registered`, together with
the required close variants.

| Hit family | Disposition |
|---|---|
| `supplied` throughout | every occurrence maps to the Imports table: metric/source domain and relative scale, common chart, measure, action, seam, or physical identification boundary |
| `choose` in the negative witnesses and N1 | exact witness states, coupling, and alternative mechanisms are test data, not selected physics |
| `positive`, `metric`, and `source` | `positive` distinguishes SPD/Gram/sign claims; `metric` is the coordinate inverse-metric feature; `source` is a scalar coordinate until separately identified |
| `canonical` | no scientific hit claims canonical metric, source, action, measure, or polarization; the canonical cache is audit mechanics only |
| `background` | no background is promoted; fixed external multipliers appear only as an alternative route with their limitation stated |
| `assume`, `assuming`, `suppose`, `by construction`, `registered`, `as is standard`, `framework provides`, `bridge context`, `naturally`, `obviously`, `standard QFT` | no hidden scientific premise is carried by these phrases; hypotheses use explicit definitions and the Imports table |

“Stress” means only the displayed metric derivative until a physical
observable theorem is supplied.  “Source response” means only derivative with
respect to `r`.  “Hamiltonian” appears only in a negative physical-
identification boundary.  No literature value, fitted coefficient, Record
scalar, or unlisted measure is hidden.

### N4 — residual matching

| Source and literal location | Residual supplied | Use here | Match |
|---|---|---|---:|
| metric-compatible transport, `docs/ADMISSIBILITY_DIRAC_KAHLER_METRIC_COMPATIBLE_EXTERIOR_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-08-27.md:48-76`, `:234-250`, `:297-306` | positive metric/coframe carrier; orthogonal edge freedom and physical geometry remain open | supplies only `G=E^T E` and its quotient boundary | yes |
| exterior-character action, `docs/ADMISSIBILITY_DIRAC_KAHLER_EXTERIOR_CHARACTER_ACTION_TRANSFER_BOUNDED_THEOREM_NOTE_2026-08-28.md:57-69`, `:255-286`, `:286-367`, `:388-468` | `Q,f_n`, fixed-weight zero stress, and source-free OS/transfer with explicit imports | action recovered at `(I,0)`; coupled Gram and response are derived anew | yes |
| minimal axioms, `docs/MINIMAL_AXIOMS_2026-06-29.md:114-130`, `:173-190`, `:205-213` | cell/Qubit/Admissibility/Record premises; no metric action, source law, measure, or dynamics | premise boundary only | yes |

The linked scientific parents are load-bearing conditional sources on the
stack.  The prior-art rows below are non-linking method references and carry
no premise or grade authority.

### N5 — rhetoric audit

`T/H` means tested here and holds.  `U/N` means untested and no claim.  `N/A`
means the phrase has no quantifier at that scale.

| Negative phrase/class | `per_element` | `per_site` | `per_mode` | `per_block` | `lattice_wide` |
|---|---|---|---|---|---|
| fixed-weight character action has no metric/source response | `T/H`: character similarity removes `E` in the parent | `T/H`: derivative at fixed `R,kappa,measure` is zero | `T/H`: source-free fixed-weight mode only | `U/N`: no assertion for metric-dependent measures/actions | `U/N`: no continuum zero-stress theorem |
| positive endpoint weights do not imply joint RP | `T/H`: entries `1,1/4,1/8` exact | `T/H`: three displayed seam histories | `T/H`: naive average (27) has determinant `-1/64` | `U/N`: no census of all metric actions | `U/N`: no global RP no-go |
| negative crossing coupling fails local positivity | `T/H`: exact two-history entries `1,2` | `T/H`: one seam item | `T/H`: negative-sign mode has eigenvalue `-1` | `U/N`: gauge projection may remove a mode on degenerate topology | `U/N`: no infinite-volume sign theorem |
| zero/negative source normalization does not give the claimed source-positive injective kernel | `T/H`: identical scalar rows at `alpha=0`; exact `[[1,2],[2,1]]` Gram at `alpha=-1` | `T/H`: nontrivial compact metric/source domain | `T/H`: negative, zero, and strict-positive normalization modes | `T/H`: tensor product inherits a null or negative independent factor | `U/N`: no thermodynamic spectral assertion |
| coframe-level injectivity is not proved | `T/H`: `E` and `QE` give identical `G` | `T/H`: one local coframe-gauge orbit | `T/H`: quotient versus raw-coframe modes | `U/N`: shared/aggregated coframe field not classified | `U/N`: no continuum gauge-fixing theorem |
| common-chart covariance is not independent-local-frame covariance | `T/H`: trace invariance under common `C` | `T/H`: one reflected pair | `T/H`: common versus independent chart modes | `U/N`: no atlas cocycle construction | `U/N`: no diffeomorphism covariance claim |
| metric/source derivatives are not physical gravity or Record stress | `T/H`: exact rational derivatives only | `T/H`: one curved matched seam | `T/H`: proper and improper response modes | `U/N`: no conservation/Ward/source-law derivation | `U/N`: no Einstein, Lorentz, or continuum statement |

The cached runner emits substantive `per_element`, `per_site`, `per_mode`,
`per_block`, and `lattice_wide` certificates.  None says that metric actions,
sources, matter couplings, connections, or gravity are globally impossible.

### N6 — partial-closure, convention, and primitive scan

| Path scanned | Exact result | Disposition |
|---|---|---|
| convention/reframe | changing a common proper-cubic chart preserves (4); changing endpoint charts independently does not | common-chart bounded construction kept; local coordinate covariance remains open |
| interpretation/meta/vocabulary | `docs/repo/CONTROLLED_VOCABULARY.md` contains no ratified rule identifying a scalar seam coordinate with a physical Record source or metric derivative with gravity | no labeling closure and no vocabulary edit |
| approved premise registry | `docs/audit/data/axiom_premise_nodes.json` lists the four current premise nodes and none supplies this metric/source action, measure, or temporal seam | no primitive or registry edit proposed |
| fixed-background metric extension | `docs/ADMISSIBILITY_CODE_SWAP_CUT_AREA_LOCAL_SOURCE_IMPROVEMENT_METRIC_RESPONSE_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md:385-431` shows extension nonuniqueness, not this polarized action | mechanism remains open and is instantiated only conditionally here |
| gauge/matter action class | `docs/DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md:59-97` gives supplied local gauge/matter forms but leaves coefficients and nontriviality open | live next route; not imported into the scalar theorem |
| branch-local first-order common matter/geometry action | the in-flight stack path `docs/ADMISSIBILITY_INCIDENCE_SCALAR_GRAPH_MATTER_FIRST_ORDER_TOTAL_WARD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md:28-60` supplies one Hermitian candidate action with geometry source, reciprocal matter recoil, and commuting mixed Hessians | close branch-local prior-art hit, not current-source authority; it uses a different unretained carrier and proves neither this metric seam, joint OS Gram, nor action selection |
| finite reciprocal source precedents | `docs/work_history/repo/review_feedback/PHYSICAL_DYNAMICAL_METRIC_SOURCE_LAW_BRIDGE_TOURNAMENT_CYCLE576_NOTE_2026-07-22.md:46-85`, `:123-132`, `:568-586` uses supplied Regge/plaquette source rules and explicitly leaves physical stress open | method/prior art only; no authority or action borrowed |
| in-flight review paths | refreshed open-PR title/head scan found the stacked exterior-character and conditional-response packets but no ratified common-chart polarized metric/source supplier | PR state carries no premise weight |
| external theorem | no precise literature theorem is needed for the finite Gram, derivative, density, or exact counterexample proofs | self-contained proof; no literature bridge imported |

The conditional construction closes the explicit finite-object route.  The
physical supplier, local-frame, aggregation, and continuum routes remain open.

### N7 — steelman

A physical metric/source law could use local tetrads with a genuine parallel
trivialization, a metric-dependent path measure, gauge-vector matter, a Record
observable, or a reflection-positive action unrelated to (1).  Such a law may
select a coupling, member `n`, source sign, and physical stress tensor while
passing a different joint Gram.  The naive-average falsifier does not touch
those possibilities.  Conversely, a physical theory might keep geometry
external and require no dynamic metric transfer at all.  The strongest live
route is a supplied gauge-vector matter action whose connection current,
metric response, source susceptibility, and full projected transfer are all
derived from one action.  The steelman defeats a broad metric/source or
gravity no-go, so none is claimed.

### N8 — cross-cycle echo

| Earlier surface | Pinned status | Retired? / mechanism | Applicability |
|---|---|---|---|
| `docs/DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md:59-97` | `bounded_theorem`, audit `unaudited`, effective `unaudited` | not retired; Wilson plaquette, covariant hopping, and mass are a supplied leading class, while coefficients/truncation/nontriviality remain open | method precedent for the live matter route; supplies nothing to (1) |
| `docs/FINITE_SOURCE_INSERTION_ALGEBRA_CARRIER_LABEL_SUPPORT_CYCLE572_BOUNDED_THEOREM_NOTE_2026-07-22.md:20-55`, `:120-146` | `bounded_theorem`, audit `unaudited`, effective `unaudited` | not retired; a supplied finite source phase has reciprocal mixed derivatives but no physical stress, metric, or action selection | confirms reciprocity alone does not identify a physical source |
| in-flight stack path `docs/ADMISSIBILITY_INCIDENCE_SCALAR_GRAPH_MATTER_FIRST_ORDER_TOTAL_WARD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md:28-60` | branch-local source status `unretained`; absent from the refreshed current-source tree and without current audit authority | not retired into authority; one candidate Hermitian action supplies a geometry source, reciprocal matter recoil, and mixed-Hessian commutation on its declared incidence carrier | closest same-action branch-local hit, but it has no metric/source polarized seam, joint OS proof, or physical-action selection |
| `docs/work_history/repo/review_feedback/PHYSICAL_DYNAMICAL_METRIC_SOURCE_LAW_BRIDGE_TOURNAMENT_CYCLE576_NOTE_2026-07-22.md:46-85`, `:568-586` | work-history surface, authority `none`, audit `unset` | not retired; supplied Regge/plaquette source models leave joined matter-edge coordinate variation and physical stress open | prior-art route map only; no load-bearing dependency |
| `docs/SOURCE_ACTION_BRIDGE_PRICING_CYCLE871_BOUNDED_THEOREM_NOTE_2026-07-28.md:1-49`, `:93-114` | stale non-authoritative source surface: authority `none`, audit `unset`, and no current ledger shard found | not retired into authority; its old Record-additivity framing was removed by its own review record, while the conditional source/action identification wall remains open | only the still-valid open source/action boundary applies; no theorem is imported |

No echo is treated as authority for a stronger claim.  Each row states its
live mechanism, retirement status, and exact applicability.

```yaml
no_go_discipline:
  status: PASS
  negative_assertion_classes:
    - derived_no_go_boundary
    - bounded_with_named_walls
  demotion: null
```

## Prior-art sweep, review boundary, and reproduction

The statement-level sweep refreshed the pinned current-source tree and
searched both noun orders for metric-dependent plaquette weights, reciprocal
metric/source variation, same-action gauge/matter coupling, source-inclusive
reflection positivity, dynamic metric transfer, and Record stress suppliers.
It found generic Wilson and gauge-matter method precedents, supplied finite
source reciprocity, and Regge/source route studies.  A separate in-flight
stack scan found the closer unretained first-order incidence-scalar
common-action/Ward candidate; it is not a current-source authority.  That
candidate supplies source/recoil reciprocity on a different carrier but not
this metric seam, joint OS kernel, or action selection.  The sweep found no current-source
theorem with the polarized action (1), joint feature Gram (22), exact naive-
average falsifier (29), reciprocal matched metric/source witness, and strict
metric-quotient support at these premises.  Classification: open after
matched-hit review.  No literature was necessary.

The primary runner uses SymPy exact symbolic and rational arithmetic.  The
independent checker uses `fractions.Fraction` and shares no primary
implementation path.  Run:

```bash
python3 scripts/admissibility_exterior_character_metric_source_polarized_seam_2026_08_28.py
python3 scripts/admissibility_exterior_character_metric_source_polarized_seam_2026_08_28.py --mode independent
python3 scripts/admissibility_exterior_character_metric_source_polarized_seam_independent_2026_08_28.py
```

The primary runner declares fourteen hostile mutations covering the
polarization coefficient, crossing sign, naive Gram, chart covariance,
metric/source response, mixed reciprocity, improper tangent force,
zero-coupling support, source normalization, strict-support tails, coframe quotient, and
physical-source boundary.  Every
mutation must exit nonzero with exactly one intended failure.  Independent
audit remains required before any effective retained-grade status can be
assigned.
