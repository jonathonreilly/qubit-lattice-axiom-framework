---
claim_id: admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_generated_interaction_bounded_theorem_note_2026-08-28
claim_type: bounded_theorem
claim_scope: "For the supplied Block227 co-scaled exterior-character step on a finite O(3) ladder and the supplied Block229 retain-every-r physical Haar isometry J_r, prove the exact positive direct-versus-staged temporal-spatial compression defect J_r* S^2 J_r-(J_r*S J_r)^2=J_r*S(I-J_rJ_r*)S J_r. On the Block227 Peter--Weyl core derive its leading generated interaction Gamma=J_r*G(I-J_rJ_r*)GJ_r. For retain-every-two on the actual two-cell ladder, prove that the kinetic generator preserves the cylindrical range while the equal-coefficient exterior spatial potential generates a nonconstant conditional-variance interaction, and evaluate an exact Z2 finite control. For arbitrary fixed finite r and q, disclose an action-amplitude lambda in the complete Block227 step and prove that the rth lambda response of the actual J_r defect, after epsilon^-r scaling and projection off the scalar coarse channel, converges strongly on the core to (-1)^r(2^r-2) times the r-fold centered exterior convolution, summed once per retained cell. Prove the (r-1)-wise Haar mechanism, the scalar leading variance for r>=3, and the finite leading Peter--Weyl response carrier. At quadratic action-response order derive the exact finite-epsilon Gram insertion and the next core coefficient K=B*A_fB+{Gamma,A_c}/2; for r>=3 prove the exact decomposition K=2 gamma A_c+u I, with u the explicit rq-accumulated exterior Dirichlet energy, so the epsilon^3 lambda^2 response has a non-scalar coarse-kinetic term but no first-order or coarse-word-dependent multiplication remainder. On the actual original-link carrier, prove the exact all-(r,q) determinant-sector offdiagonal selection rule: quadratic coarse determinant mixing occurs only for r=2 coarse-hypercube neighbors, including the positive seven-link vacuum witness, while r>=3 determinant-to-determinant offdiagonals vanish at this response order. For every pair of coarse determinant words at Hamming distance d, prove the first possible finite-epsilon offdiagonal response is derivative order rd, give its positive full-O(3) residual-subset formula after deleting all 2^d block-cylindrical subsets, and recover the small-step coefficient 2^(rd)-2^d. Derive the shared-retained-rung context dependence. Bound finite Peter--Weyl approximation of the complete defect value, its exact quadratic Gram response, and the selected all-pairs determinant responses, with explicit rq accumulation and common normalization. This is a conditional finite mathematical generated-interaction and supplied-action-response theorem, not a physical time, continuum, action-selection, Lorentz, gravity, metric/source, or matter-current theorem."
depends_on:
  - admissibility_exterior_character_co_scaled_temporal_trotter_and_cylindrical_refinement_boundary_bounded_theorem_note_2026-08-28
  - admissibility_exterior_character_bounded_degree_ladder_history_message_flow_bounded_theorem_note_2026-08-28
  - admissibility_exterior_character_jr_peter_weyl_operator_truncation_bounded_theorem_note_2026-08-28
  - minimal_axioms
runner: scripts/admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_2026_08_28.py
independent_checker: scripts/admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_independent_2026_08_28.py
status: proposed_retained
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_exterior_character_co_scaled_temporal_trotter_and_cylindrical_refinement_boundary_bounded_theorem_note_2026-08-28
target_blocker_text: "Compare the Block227 co-scaled temporal generator with Block228/229 changing-carrier compression and derive either commutation or the exact generated interaction."
source_of_blocker_text: user_goal
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "Any multiscale construction must retain the generated coarse-kinetic descendant, the exact determinant-sector response-order selection and shared-rung context, and the finite leading multiplication-response channels, or approximate the exact exterior weight with those errors controlled; physical spacing, time, states, and observables remain separate suppliers."
conditional_surface_status: "exact finite physical-space temporal-spatial compression defect, nonconstant two-cell generated interaction, arbitrary-fixed-r complete-step supplied-action response, quadratic-response coarse-kinetic descendant, exact all-(r,q) finite-epsilon determinant selection, exact all-pairs Hamming-distance response-order filtration, and response-specific finite packet bounds, conditional on the supplied co-scaled action, ladder, Haar measure, projector, and J_r stack"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the compression identity, core limit, cylindrical kinetic calculation, conditioned-product Haar lemma, arbitrary-r complete-step response limit, quadratic-response Gram/Dirichlet coefficient, original-link determinant scale-selection and all-pairs finite-step response-order rules, exterior convolution coefficients, exact finite controls, and finite-packet defect/response bounds are exact mathematical results with no fitted datum"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# `J_r` temporal--spatial compression defect and generated interaction

**Date:** 2026-08-28

**Type:** `bounded_theorem`

**Status:** `proposed_retained` — an author proposal on an unmerged
conditional stack, not an audit verdict.

## Result up front

The [Block227 theorem](ADMISSIBILITY_EXTERIOR_CHARACTER_CO_SCALED_TEMPORAL_TROTTER_AND_CYLINDRICAL_REFINEMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md)
proves a strong temporal product limit on one fixed carrier and separately
falsifies bare same-action spatial subdivision.  The
[Block229 ladder theorem](ADMISSIBILITY_EXTERIOR_CHARACTER_BOUNDED_DEGREE_LADDER_HISTORY_MESSAGE_FLOW_BOUNDED_THEOREM_NOTE_2026-08-28.md)
constructs the actual changing-carrier Haar isometry and shared-frame
compression.  Neither asks whether temporal evolution and spatial
compression form a consistent square.

Their exact discrepancy is positive.  Let `J=J_r` be the physical
retain-every-`r` isometry, let `Q=JJ*` be the orthogonal cylindrical-range
projector on the fine physical space, and let `S_epsilon` be the self-adjoint
Block227 fine step.  Directly evolve two fine temporal steps and compress, or
compress after each step.  Their exact difference is

```text
D_epsilon
 :=J* S_epsilon^2 J-(J*S_epsilon J)^2
  =J*S_epsilon(I-Q)S_epsilon J
  =[(I-Q)S_epsilon J]*[(I-Q)S_epsilon J] >=0.       (1)
```

The square commutes exactly if and only if `S_epsilon Ran J` remains in
`Ran J`.  On the Block227 Peter--Weyl core,

```text
epsilon^-2 D_epsilon ->
Gamma=J*G_f(I-Q)G_fJ                              (2)
```

in quadratic form, where `G_f=A_f+V_f` is the fine temporal generator.  On
the actual retain-every-two/two-cell ladder the kinetic part maps cylindrical
functions to cylindrical functions, albeit with a derived anisotropic coarse
coefficient.  Therefore

```text
Gamma=J*V_f(I-Q)V_fJ
     =E[V_f^2|coarse]-E[V_f|coarse]^2.              (3)
```

For equal fine plaquette coefficients and fixed coarse plaquette word
`delta=W_1W_0`, equation (3) is the nonconstant central function

```text
Gamma(delta)
 =2(<v^2>-<v>^2)+2[(v*v)(delta)-<v>^2],            (4)
v=f_n(Q).
```

It is strictly nonconstant because the exterior potential has nontrivial
Peter--Weyl coefficients.  The exact `Z_2={I,-I}` finite control gives

```text
Gamma(+)=256/n^2,       Gamma(-)=0.                 (5)
```

Thus the equal-coefficient two-cell member has a strictly positive leading
separation coefficient on one coarse sector.  A nonconstant positive
interaction/memory term is generated at order `epsilon^2`.  A common nonzero
scalar normalization maps it to `c_epsilon^2 Gamma`, which stays nonzero.

This is distinct from the fixed-carrier BCH residual already in Block227,
the one-cell induced crossing in Block228, and an auxiliary `B`-chain tail.
It compares the two paths around the actual temporal--spatial square on the
physical `J_r` spaces.  The pure-gauge parent carrier contains no matter,
source, or coframe variables, so this theorem supplies no such response.

The scale dependence is sharp.  In one retain-every-`r` cell the constrained
increments `W_(r-1)...W_0=delta` are `(r-1)`-wise independent Haar variables.
Consequently the leading variance in (3) is a scalar for every `r>=3`; the
nonconstant order-`epsilon^2` interaction in (4) is special to `r=2`.

Nevertheless the complete step has an exact arbitrary-fixed-`r` response.
Multiply only the already-supplied spatial action by a disclosed amplitude
`lambda`, keep `J_r`, every projector, Haar measure, and temporal
normalization fixed, and call the resulting complete defect
`D_epsilon(lambda)`.  On the physical Peter--Weyl core, after projecting the
limiting multiplication symbol off its scalar coarse-Haar channel,

```text
NC (s-lim_(epsilon downarrow 0) [
  (r! epsilon^r)^-1
  partial_lambda^r D_epsilon(lambda)|_(lambda=0)])

 =M_{(-1)^r(2^r-2) sum_(c=0)^(q-1)
      (product_(i=0)^(r-1) a_(c,i))
      (v-<v>)^(*r)(delta_c)}.                      (5a)
```

The `2^r` is the direct path and the `2` is the pair of staged Leibniz
endpoints. This is the first nonconstant multiplication coefficient whose
`lambda^r` response is taken at its minimal `epsilon^r` degree; it does not exclude lower `lambda`
degree mixed kinetic terms at higher powers of `epsilon`. At fixed exterior
member `n`, the right
side closes in the finite character support of `Lambda^(tensor n)`. Thus no
additional Peter--Weyl support is needed in this leading response: for each
blocking factor `r`, the first nonconstant multiplication-symbol coefficient
at its minimal `epsilon` degree is
`epsilon^r lambda^r` inside that fixed finite carrier.

That order statement concerns the multiplication-symbol channel.  The
complete operator response has an earlier kinetic descendant.  Put
`B=(I-Q)V_fJ_r`, `Gamma=B*B`, and
`A_c^ind=J_r*A_fJ_r`.  For `r>=3`, `Gamma=gamma I`, where
`gamma` is the positive conditional variance summed over the retained cells.
Then, on the same physical core,

```text
(1/2) partial_lambda^2 D_epsilon(lambda)|_(lambda=0)
 =epsilon^2 gamma I-epsilon^3 mathcal K+o_psi(epsilon^3),

mathcal K=B*A_fB+gamma A_c^ind.                    (5b)
```

For `r>=3` the remainder closes exactly:

```text
mathcal K=2gamma A_c^ind+u_(r,q)I,
u_(r,q)=2D E_v sum_(c,i)a_(c,i)^2,
E_v=<v,(-Delta_G)v>.
```

Thus the response at bidegree `epsilon^3 lambda^2` has a non-scalar induced
coarse-kinetic term but no first-order or coarse-word-dependent multiplication
remainder.  It is not a new multiplication potential or a metric/source
current.

The same exact Gram consumer has a response-specific finite packet bound. If
every spatial half packet has cutoff at least one, its first action-amplitude
derivative at zero is exact.  Only the `3rq+1` temporal tails accumulate, and

```text
||R_epsilon-R_epsilon^K||_op
 <=2epsilon^2||Gamma||[1-(1-delta_kappa)^(3rq+1)]. (5c)
```

Here `R=(1/2)partial_lambda^2D|_0`; the full second derivative has twice the
right side.  Exact and packet families use the same Block231 normalization.

At `r=2`, for every finite `q`, the exact finite-`epsilon` Gram response is
more restrictive than its small-step coefficient.  Let `phi_det` be the normalized coarse
determinant plaquette spin network and let `t_det` be the normalized
single-original-link determinant multiplier of the supplied temporal
crossing.  With positive plaquette amplitudes `a_0,a_1`,

```text
<1,R_epsilon phi_det>
 =epsilon^2(c_det^(n))^2 a_0a_1/2
  (1+t_det^4)(t_det^4+t_det^6)>0,                 (5d)

c_det^(n)=16 m_(det,n)/(n 8^n)>0.
```

For the vacuum and a single coarse-cell determinant state, the coefficient is
independent of the other empty retained cells. The powers four and six count
the actual original links of a fine plaquette
and of the pulled-back coarse outer boundary.  Thus the complete physical
quadratic response is not a central convolution at any supplied finite
positive `epsilon`; it contains a genuine conjugation-compatible off-block.
More generally, the full determinant offdiagonal is supported only on
coarse-hypercube neighbors at `r=2`; for `r>=3` it vanishes exactly at
quadratic order. Shared retained rungs make the nonzero `q>1` coefficients
background dependent, so they do not factor into one-cell responses. This is
an exact response/memory consumer, not a reduced increment model or
a generic compactness statement.

## Authority and imports

The refreshed landed authority is `origin/main` commit
`004f64e1c87dad696b282cf2b526f3e7312dc82d`; its only change after the
previous science pin `66e478505e055faf4a5b9e6f4883211e44304718` is audit
automation, not new scientific authority.  The exact parent of this branch
is reviewed Block231 head
`6c6302daa0c7512298266cd01a229ba1f1537d92`; every scientific parent remains
an open, unmerged, conditional proposal.

| Input | Role | Provenance | Open boundary |
|---|---|---|---|
| `G=O(3)`, normalized product Haar, finite member `n`, exterior `v=f_n(Q)` | action carrier and integration | supplied parent stack | no action or measure selection |
| finite open ladder `Gamma_L`, `L=rq`, original-link map `pi_r` | changing spatial carrier | supplied Block229 | no spacing or continuum embedding |
| physical projectors `P_(rq),P_q` and residual forest-gauge projector `P_lr` | gauge-invariant Hilbert spaces | supplied Block229 | not a physical-state selector |
| `J_r=pi_r^*`, `P_(rq)J_r=J_rP_q` | physical coarse isometry | supplied Block229 | no transfer intertwining inferred from isometry |
| co-scaled `S_epsilon=M_epsilon P C_epsilon P M_epsilon` | fine temporal step | supplied Block227 | mathematical Euclidean parameter, not physical time |
| core derivative `(S_epsilon-I)/epsilon -> -G_f` | leading generator | supplied Block227 | strong/core statement, not operator norm |
| positive fine plaquette coefficients `a_(c,i)` and fixed amplitude `lambda` | two-cell witness and arbitrary-`r` supplied-action response | disclosed here inside the Block227 action family | no uniqueness, physical coefficient, metric, or source claim |
| Block231 finite positive packet and full-transfer error | defect approximation | supplied Block231 | no generic Poisson-tail novelty |

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) provide no action,
transfer, time, coarse map, measure, generator, or interaction interpretation.
No axiom or approved primitive is changed.

## Typed physical square

Let

```text
H_f^phys=P_(rq)H_(rq),       H_c^phys=P_qH_q,
J=J_r|_(H_c^phys):H_c^phys -> H_f^phys,
Q=JJ*:H_f^phys -> H_f^phys.                         (6)
```

Block229 proves that `J` is an isometry and that the same statement is
unitarily equivalent in rail-forest gauge with `P_lr`.  Therefore `Q` is the
orthogonal conditional-Haar projector onto the cylindrical range.  It is not
an action postulate.

On the fine ladder use the Block227 co-scaled step

```text
S_epsilon=M_epsilon P_(rq) C_epsilon P_(rq) M_epsilon,
M_epsilon=exp[-epsilon V_f/2].                      (7)
```

It is a self-adjoint positive contraction on `H_f^phys`.  Define the direct
and staged coarse two-step operators

```text
T_dir(epsilon)=J*S_epsilon^2J,
T_stage(epsilon)=(J*S_epsilon J)^2.                 (8)
```

Every fine temporal link, plaquette half-action, local frame, and retained
shared frame belongs to `S_epsilon` before either path is evaluated.  Equation
(8) does not multiply independently marginalized strip kernels.

Insert `Q=JJ*` between the two factors in the staged path.  Then

```text
T_dir-T_stage
 =J*S_epsilon(I-Q)S_epsilon J.                     (9)
```

Self-adjointness gives the last Gram form in (1).  Hence the defect is
positive operator order, and

```text
D_epsilon=0  iff  (I-Q)S_epsilon J=0.              (10)
```

This is a precise range-invariance condition, not a generic claim that every
compression fails to preserve every semigroup.

## Block227 core limit

Let `D_core` be the gauge-invariant algebraic Peter--Weyl core used by
Block227.  For `psi in D_core`, its core derivative is

```text
(S_epsilon-I)Jpsi/epsilon -> -G_fJpsi.              (11)
```

Because `(I-Q)J=0`,

```text
(I-Q)S_epsilon Jpsi/epsilon
 ->-(I-Q)G_fJpsi.                                   (12)
```

Taking the Gram form in (1) yields

```text
<psi,D_epsilon psi>/epsilon^2
 ->||(I-Q)G_fJpsi||^2
 =<psi,Gamma psi>,                                  (13)

Gamma=J*G_f(I-Q)G_fJ
     =([Q,G_f]J)*([Q,G_f]J)>=0.                    (14)
```

Equations (13)--(14) are a quadratic-form/core limit.  No global
operator-norm expansion of `S_epsilon` is claimed.

## Kinetic cylindrical range

Write `G_f=A_f+V_f`, where `A_f` is the sum of link Casimirs and `V_f` is the
bounded spatial exterior potential.  For the retain-every-two map on one
two-cell ladder:

- a hidden rung does not occur in `Jpsi`, so its Casimir annihilates `Jpsi`;
- each retained rung occurs once and its fine Casimir becomes the same coarse
  rung Casimir;
- each coarse rail link is an ordered product of two fine rail links, and the
  sum of their two bi-invariant Casimirs becomes twice the coarse rail
  Casimir.

Thus there is an explicitly induced anisotropic coarse kinetic operator

```text
A_c^ind
 =A_(retained rungs)+2A_(coarse bottom rails)+2A_(coarse top rails)
```

at the common fine diffusivity, with

```text
A_fJ=J A_c^ind,       (I-Q)A_fJ=0.                 (15)
```

The factor two is not renamed kinetic isotropy or a physical scale law.  A
separately co-scaled fine rail diffusivity would absorb it, but that choice is
not needed for the range statement.

Equation (15) reduces the generated term without assuming `[A_f,V_f]=0`:

```text
(I-Q)G_fJ=(I-Q)V_fJ,
Gamma=J*V_f(I-Q)V_fJ.                              (16)
```

## Exact two-cell generated interaction

In Block229 rail-forest gauge, let

```text
W_0=X_1X_0^-1,       W_1=X_2X_1^-1,
delta=X_2X_0^-1=W_1W_0.                            (17)
```

The retained variables fix `delta`; normalized Haar on the hidden rung makes
`W_0=x` Haar and `W_1=delta x^-1`.  Specialize the Block227 spatial action to
equal unit plaquette coefficients:

```text
V_f(x;delta)=v(x)+v(delta x^-1),       v=f_n(Q).    (18)
```

Let

```text
mu=int_G v,
nu=int_G v^2,
(v*v)(delta)=int_G v(x)v(delta x^-1)dx.             (19)
```

Conditional Haar expectation gives

```text
E[V_f|delta]=2mu,
E[V_f^2|delta]=2nu+2(v*v)(delta).                   (20)
```

Substitution into (16) proves (4).  More generally, unequal supplied
coefficients `a,b` give

```text
Gamma_(a,b)(delta)
 =(a^2+b^2)(nu-mu^2)+2ab[(v*v)(delta)-mu^2].        (21)
```

Equation (4) is nonconstant.  A real central Peter--Weyl expansion of
nonconstant `v` has at least one nontrivial coefficient.  Convolution squares
those real Fourier multipliers, so `v*v` retains a nonzero nontrivial channel.
The exterior member is indeed nonconstant on `O(3)`: `v(I)=0`, while a proper
pi rotation and every improper element have `v=16/n`.  No connected component
is discarded.

The generated term contains the full convolution square as a function of the
coarse product word.  In the two-step compressed operator it is a finite
mathematical memory interaction between the two paths around the square; no
claim about observed memory is made.

## Exact finite control and normalization

On the central subgroup `Z_2={I,-I}` take

```text
v(+)=0,       v(-)=a=16/n.                          (22)
```

Then

```text
mu=a/2,       nu=a^2/2,
(v*v)(+)=a^2/2,       (v*v)(-)=0.                  (23)
```

Equations (4), (22), and (23) give (5).  The plus coarse word has two fine
histories `(W_0,W_1)=(+,+),(-,-)` with different action, while the minus word
has `(+,-),(-,+)` with equal action; the variance calculation is exact.

If `S_epsilon` is multiplied by any nonzero scalar `c_epsilon`, both paths in
(8) scale by `c_epsilon^2` and

```text
D_epsilon[cS]=c_epsilon^2 D_epsilon[S].             (24)
```

Thus a temporal partition factor or common top-operator normalization rescales
the nonconstant defect and leaves it nonzero for `c_epsilon !=0`.  Separately
normalizing the direct and staged two-step operators by different scalars
defines a different square and is not covered.

## Arbitrary-`r` conditioned-Haar hierarchy

Fix finite `r>=2` and `q>=1`. In rail-forest gauge, write the fine plaquette
increments in retained cell `c` as

```text
W_(c,i)=X_(cr+i+1)X_(cr+i)^-1,       0<=i<r,
delta_c=X_((c+1)r)X_(cr)^-1
       =W_(c,r-1)...W_(c,0).                         (25)
```

At fixed retained `X_(cr),X_((c+1)r)`, normalized Haar on the `r-1` hidden
rungs is the conditional Haar fiber in (25). If coordinate `k` is omitted,
put `A=W_(r-1)...W_(k+1)` and `B=W_(k-1)...W_0`. The constraint solves
uniquely as `W_k=A^-1 delta B^-1`. Left/right Haar invariance therefore makes
every proper subset of the `r` increments independent product Haar. This
remains true on disconnected `O(3)`; only the total determinant product is
fixed. Different retained cells use disjoint hidden variables and are
conditionally independent at fixed retained rungs.

The kinetic range statement also extends. A hidden rung does not occur in a
pullback, a retained rung occurs once, and each of the `r` fine bi-invariant
rail Casimirs becomes the same coarse rail Casimir. Hence

```text
A_fJ_r=J_r A_c^(r),
A_c^(r)=A_(retained rungs)+r A_(coarse rails).       (26)
```

The factor `r` is an induced anisotropic coefficient, not a physical scale
law. Equations (16) and (26) reduce the leading generated operator to the
conditional variance in every retained cell.

Let

```text
V_f=sum_(c=0)^(q-1) sum_(i=0)^(r-1)
        a_(c,i)v(W_(c,i)),
mu=int_G v,       sigma_v^2=int_G v^2-mu^2.
```

For one cell, `(r-1)`-wise independence gives

```text
Gamma_2(delta)
 =sigma_v^2(a_0^2+a_1^2)
  +2a_0a_1[(v*v)(delta)-mu^2],

Gamma_r(delta)=sigma_v^2 sum_i a_i^2,       r>=3.  (27)
```

Thus the order-`epsilon^2` leakage remains positive but is a scalar coarse
operator for `r>=3`. Equation (32) locates the first nonconstant
minimal-bidegree multiplication-symbol response for general `r` at order `r`.

More generally, for `V_r=sum_i a_i v(W_i)`, every conditional moment and
cumulant below order `r` equals the independent-Haar value. At order `r`,
only a monomial using every coordinate once can depend on `delta`. With
`h=v-mu`,

```text
kappa_m(V_r|delta)=kappa_m^Haar(v) sum_i a_i^m,
                                                    m<r,

kappa_r(V_r|delta)
 =kappa_r^Haar(v) sum_i a_i^r
  +r!(product_i a_i)h^(*r)(delta).                 (28)
```

Convolution follows the ordered product in (25). Centrality of the exterior
`v` makes the order immaterial, but it cannot be permuted for a noncentral
insertion. If any `a_i=0`, the full conditional law depends on a proper subset
and is `delta`-independent.

## Complete-step arbitrary-`r` action response

Disclose a scalar amplitude `lambda` multiplying only the already-supplied
spatial potential. Keep `J_r`, `Q`, every physical projector, normalized Haar
measure, and temporal normalization fixed, and define

```text
M_(epsilon,lambda)=exp[-epsilon lambda V_f/2],
S_epsilon(lambda)
 =M_(epsilon,lambda)P_(rq)C_epsilon P_(rq)
  M_(epsilon,lambda),

D_epsilon(lambda)
 =J_r*S_epsilon(lambda)^2J_r
  -(J_r*S_epsilon(lambda)J_r)^2.                   (29)
```

On `H_f^phys` the fine projector is the identity. The class potential commutes
with it and, under forest-gauge equivalence, with `P_lr`. The algebraic Peter--
Weyl core is stable under every fixed power of bounded `V_f`. Block227's
channel expansion gives `C_epsilon-I=O_psi(epsilon)` on each fixed core vector
required below; uniform boundedness and strong convergence to `I` would
already suffice for the leading fixed-`r` limit.

After `r` `lambda` derivatives, every multiplier derivative supplies one
factor `epsilon`. Any occurrence of `C_epsilon-I` supplies an additional small
factor on the core. Dividing by `epsilon^r` therefore reduces (29) in the
strong/core limit to

```text
J_r*exp[-2epsilon lambda V_f]J_r
 -(J_r*exp[-epsilon lambda V_f]J_r)^2.              (30)
```

No commutation of `C_epsilon` with `V_f` is assumed. Put
`m_k=E[V_f^k|delta_0,...,delta_(q-1)]`. Direct differentiation of (30) gives

```text
epsilon^-r partial_lambda^r D_epsilon|_0
 ->(-1)^r[2^r m_r
          -sum_(k=0)^r binom(r,k)m_k m_(r-k)].      (31)
```

For `k<r`, every monomial misses at least one increment in every retained
cell, so `m_k` is independent of all coarse words. The nonconstant part of
`m_r` is

```text
r! sum_(c=0)^(q-1)(product_(i=0)^(r-1)a_(c,i))
    h^(*r)(delta_c).
```

Only the `k=0,r` endpoints in the staged sum in (31) contain this term. Thus
the direct coefficient `2^r` loses exactly the two staged endpoints.

Type `NC` only on the limiting multiplication operator: if the strong limit
in (31) is `c_r I+M_F` with `int F=0` over all retained coarse words, set
`NC(c_r I+M_F)=M_F`. Then

```text
NC (s-lim_(epsilon downarrow 0) [
 (r! epsilon^r)^-1
 partial_lambda^r D_epsilon(lambda)|_(lambda=0)])

 =M_{(-1)^r(2^r-2) sum_(c=0)^(q-1)
      (product_(i=0)^(r-1)a_(c,i))
      h^(*r)(delta_c)}.                            (32)
```

Within the leading `C_epsilon -> I` hierarchy used in (32), dependence on two
different coarse words first requires `2r` action-amplitude derivatives.
Equation (32) is fixed in finite `r,q,n` and
strong/core topology. It is not a fixed-`epsilon` identity, an operator-norm
limit, or a joint `r,q -> infinity` statement. It also does not exclude
nonconstant mixed kinetic terms of lower `lambda` degree at higher powers of
`epsilon`.

A common temporal scalar `c_epsilon`, independent of `lambda`, multiplies the
answer by `lim c_epsilon^2`; (32) uses Block227's normalized convention
`c_epsilon ->1`. Varying `J_r`, Haar measure, a projector, or normalization
with `lambda`, or separately normalizing the two paths, adds derivative terms
and defines a different response. The amplitude in (29) is an auxiliary
action response, not a metric, coframe, physical source, or matter current.

For the exterior member, let `m_(rho,n)` be the multiplicity of nontrivial
`O(3)` irrep `rho` in `Lambda^(tensor n)`. The centered scalar Fourier
multiplier is

```text
h_rho=-(16/n)m_(rho,n)/(d_rho 8^n),
h^(*r)(delta)=sum_(rho!=1)d_rho h_rho^r chi_rho(delta). (33)
```

Vector and determinant channels occur by trivial padding, so (33) is
nonconstant for every finite `r`; odd/even `r` changes signs, not survival of
the improper component. At fixed `n`, `h` is a finite character polynomial,
so every leading response in (32) lies in one fixed finite Peter--Weyl span.
For `n=1` exactly,

```text
h=-2(chi_V+chi_(det tensor V)+chi_det),
h^(*r)=3(-2/3)^r(chi_V+chi_(det tensor V))
       +(-2)^r chi_det.                            (34)
```

The resulting leading response carrier has the supplied action coordinate
and the generated `h^(*r)` coordinate, both inside the same finite
Peter--Weyl support.  Its response order is `r` in the leading simultaneous
`epsilon,lambda` hierarchy.

## Quadratic response generates a coarse kinetic descendant

The actual factorized central temporal convolution preserves `Ran J_r`
exactly: independent convolution of the `r` fine rail factors induces a
coarse convolution, whether or not that induced kernel belongs to the same
one-coupling family.  Therefore, for every fixed `epsilon`,

```text
C_epsilon J_r=J_r C_c,epsilon,
[C_epsilon,Q]=0,
C_c,epsilon=J_r*C_epsilon J_r.                    (34a)
```

Let `R=I-Q`, `B=RV_fJ_r`, and `Gamma=B*B`.  Since `RS_epsilon(0)J_r=0`,
the complete defect has zero linear action response.  Differentiating the
two symmetric multiplier halves once gives the exact finite-`epsilon` Gram
insertion

```text
(1/2) partial_lambda^2 D_epsilon(lambda)|_(lambda=0)
 =L_epsilon*L_epsilon>=0,

L_epsilon
 =-(epsilon/2)(B C_c,epsilon+C_epsilon B).         (34b)
```

This identity already contains the residual projector, both normalization-
matched paths, the induced crossing, and the complete physical `J_r`
consumer.  It is not differentiation of an auxiliary message.

Block227 gives `C_epsilon=I-epsilon A_f+o_psi(epsilon)` on every required
Peter--Weyl core vector.  Equation (34a) gives
`C_c,epsilon=I-epsilon A_c^ind+o_psi(epsilon)`, with
`A_c^ind=J_r*A_fJ_r` and `[A_f,Q]=0` on the core.  Expanding (34b),

```text
(1/2) partial_lambda^2 D_epsilon|_0
 =epsilon^2 Gamma-epsilon^3 mathcal K+o_psi(epsilon^3),

mathcal K
 =B*A_fB+(1/2){Gamma,A_c^ind}.                    (34c)
```

Equivalently, the difference after subtracting `epsilon^2 Gamma` and dividing
by `epsilon^3` converges strongly on the fixed finite-volume core, or in its
quadratic forms, to `-mathcal K`.  Only the first temporal derivative enters;
Block227's cubic channel residual contributes at a later `epsilon` order.

For every `r>=3`, the proper-subset Haar result (27) gives

```text
Gamma=gamma I,
gamma=sigma_v^2 sum_(c=0)^(q-1) sum_(i=0)^(r-1)
                         a_(c,i)^2>0.              (34d)
```

On the actual `O(3)` ladder, `A_f` is the supplied sum of link Casimirs and
`B=M_fJ_r`, where `f=V_f-E[V_f|coarse]`.  On the algebraic Peter--Weyl core,
the exact double-commutator identity is

```text
M_f A_f M_f
 =(1/2){A_f,M_(f^2)}+(1/2)[M_f,[A_f,M_f]],

B*A_fB
 =(1/2){A_c^ind,M_Gamma}
  +(1/2)J_r*[M_f,[A_f,M_f]]J_r.                  (34e)
```

For `r>=3`, `M_Gamma=gamma I`, so the first term is exactly
`gamma A_c^ind`, not merely its principal part.  With
`A_f=-(D/2)sum_e Delta_e`, the second term in (34e) is multiplication by the
conditional carré-du-champ

```text
(D/2) E[sum_(e,a)|X_(e,a)f|^2 | coarse].          (34f)
```

Every self term contains one supplied plaquette insertion.  Only adjacent
plaquettes can contribute cross terms, through their shared rung.  Each such
term is, up to its disclosed coefficient and orientation,
`-sum_a(L_a v)(W_(i-1))(R_a v)(W_i)`.  Conditioned-product Haar is pairwise
independent for `r>=3`, including across the independent retained cells, and
the Haar integral of a left- or right-invariant derivative vanishes.  Hence
all cross terms in (34f) vanish and the remaining coefficient is independent
of every retained coarse word.  Each ladder plaquette has two rail and two
rung links.  Therefore, with

```text
E_v=<v,(-Delta_G)v>,
u_(r,q)=2D E_v sum_(c=0)^(q-1)sum_(i=0)^(r-1)a_(c,i)^2,

B*A_fB=gamma A_c^ind+u_(r,q)I,
mathcal K=2gamma A_c^ind+u_(r,q)I.                (34g)
```

There is no first-order remainder and no coarse-word-dependent zero-order
remainder at `epsilon^3 lambda^2`.  The order-two term is the exact induced
anisotropic coarse Casimir from (26).  At the minimal `epsilon` degree
isolated in (32), the nonconstant multiplication symbol is the order-`r`
coefficient; no all-order multiplication filtration is inferred.

For the exterior member, (33) and character orthogonality make the scalar
coefficient explicit:

```text
E_v=(16/(n 8^n))^2
    sum_(rho!=1)L_rho m_(rho,n)^2 >0,             (34h)
```

where `L_rho` is the rotational Casimir.  The determinant-only `l=0` channel
has zero rotational energy, while the padded vector channels make (34h)
strictly positive.

A common `lambda`-independent scalar normalization
`c_epsilon=1+c_1epsilon+o(epsilon)` sends
`mathcal K` to `mathcal K-2c_1Gamma`.  For `r>=3` this shifts only the scalar
`u_(r,q)` and leaves the exact coefficient `2gamma A_c^ind` unchanged.
Varying the normalization with `lambda`, or normalizing the direct and staged
paths separately, still defines a different response.

An independent normalized-counting-Haar `S_3` enumeration at `r=3` checks the
entire mechanism.  With central
`v(e)=0`, `v(transposition)=2`, `v(3-cycle)=5` and the transposition-average
Laplacian, every product fiber has 36 points,
`A_fJ=3J A_c`, and `Gamma=(29/3)I`.  Exact fractions give

```text
(1/2) partial_lambda^2 D_epsilon|_0
 =epsilon^2(29/3)I
  +epsilon^3(-11I-47A_c)+O(epsilon^4),             (34i)
```

while the order-`epsilon^3 lambda^3` diagonal symbol is the separate centered
cubic convolution.  Scaling `A_f` scales the mixed term, setting `A_f=0`
removes it, a constant potential removes the whole defect, and a common
scalar normalization changes only the scalar part.  Because the finite-group
Laplacian is a jump generator rather than a second-order differential
Casimir, its `47A_c` coefficient is not a control for the `O(3)` coefficient
in (34g).  It controls the existence, sign, normalization, and non-scalar
kinetic character of the mixed response only.

A second independent differential-Casimir control uses normalized `U(1)`
Haar, `r=3,4,5`, unequal rational coefficients, and `v(x)=cos x`.  In the
coarse Fourier mode `k`, multiplication by `v(W_i)` shifts exactly one fine
index by `+1` or `-1`.  Direct finite support enumeration gives

```text
B*A_fB e_k=gamma(r k^2+1)e_k
             =gamma A_c^ind e_k+gamma e_k,         (34j)
```

for every enumerated `-4<=k<=4`.  The result is even in `k`, so it has no
first-order drift, and its remainder is the coefficient-square scalar.  This
checks the differential product-rule mechanism independently of both the
`O(3)` proof and the finite jump-generator `S_3` control; it is not a physical
group substitution.

## Exact finite-`epsilon` determinant off-block on the actual `r=2` carrier

The quadratic identity (34b) also admits an exact all-finite-step witness on
the complete original-link carrier.  Fix one retained cell, so `r=2,q=1` and
there are `3r+1=7` fine original links.  In the Block229 forest gauge define

```text
psi_0=det W_0,       psi_1=det W_1,
phi_det=det(W_1W_0).
```

The coarse states `1,phi_det` are normalized and residual-gauge invariant,
and their pullbacks are `1,J_2 phi_det`.  The fine determinant cycle space is
the orthonormal four-state Peter--Weyl sector

```text
{1,psi_0,psi_1,J_2 phi_det}.                       (34k)
```

In original-link incidence, `psi_0,psi_1` are the two four-link plaquette
boundaries.  Their product cancels the shared hidden rung and is the
six-link outer boundary `J_2 phi_det`; the seventh link is trivial in that
outer state.  If
`t_det=t_det(epsilon)=r_det^(n)(q_epsilon)` denotes the normalized determinant
multiplier of one supplied Block227 link crossing, the exact fine and induced
coarse temporal operators on (34k) are therefore

```text
C_epsilon=diag(1,t_det^4,t_det^4,t_det^6),
C_c,epsilon=diag(1,t_det^6),                       (34l)
```

with rows ordered as in (34k).  For a supplied positive finite step,
`0<t_det<1`.  No continuum or physical-time interpretation is used.

Let `m_(det,n)` be the determinant multiplicity in
`Lambda^(tensor n)`.  The centered exterior insertion has determinant
coefficient

```text
c_det^(n):=-<v-<v>,chi_det>
          =16 m_(det,n)/(n 8^n)>0.                (34m)
```

Trivial padding makes `m_(det,n)>0` for every fixed `n`.  Project `B` onto
the residual determinant rows `psi_0,psi_1` and restrict its columns to
`1,phi_det`.  The exact block is

```text
P_det B|_{1,phi_det}
 =-c_det^(n) [[a_0,a_1],[a_1,a_0]].               (34n)
```

This is not a determinant-quotient assumption.  It is a Peter--Weyl block of
the full `O(3)` operator.  Moreover it gives the complete cross matrix
element: any non-determinant one-plaquette component in the vacuum column,
paired with an outer-determinant-twisted component in the `phi_det` column,
leaves a determinant label on a unique exclusive rail edge of the other
plaquette.  Normalized edgewise Peter--Weyl orthogonality kills that overlap.
The central link convolution preserves the edge labels.  Only the determinant
component cancels both added determinant labels, so no omitted channel can
cancel the following value.

Substitution of (34l)--(34n) in the exact physical Gram formula (34b) gives

```text
<1,R_epsilon phi_det>
 =epsilon^2(c_det^(n))^2 a_0a_1/2
  (1+t_det^4)(t_det^4+t_det^6)>0,                 (34o)

R_epsilon=(1/2)partial_lambda^2D_epsilon|_0.
```

The inequality holds for `a_0a_1>0` and every supplied finite positive step.
A common nonzero scalar normalization multiplies (34o) by its square and
cannot remove it.  A central convolution preserves every coarse
Peter--Weyl block, in particular the vacuum line; (34o) is a nonzero
vacuum-to-determinant coefficient.  Hence the exact complete `J_2`
quadratic response is not a central convolution.  It requires a generated
conjugation-compatible history/perfect-action coordinate downstream.

The original-link census is load-bearing.  A reduced independent-increment
model tuned to reproduce `t_det^4` on each fine plaquette would give
`t_det^8`, not the actual `t_det^6`, on the coarse outer state.  Its predicted
off-block would differ from (34o) by

```text
epsilon^2(c_det^(n))^2a_0a_1/2
 (1+t_det^4)t_det^6(1-t_det^2).                   (34p)
```

Thus neither the formula nor its positivity is imported from the auxiliary
two-increment model.  The exact seven-link normalized-counting-Haar `Z_2`
control uses plaquette incidence weights `4,4`, outer weight `6`, and raw
`pi_2` fibers of size eight.  At `epsilon=1`, `t_det=1/2`, `c_det=8`, and
unit amplitudes, direct enumeration gives

```text
<1,R_epsilon phi_det>=85/32,                      (34q)
```

exactly as in (34o).  The finite quotient controls normalization, incidence,
and the Gram algebra; the full `O(3)` Peter--Weyl orthogonality argument above
is load-bearing.  This seven-link derivation fixes `r=2,q=1`; equation (34t)
below proves that (34o) is the vacuum-to-single-cell entry for every finite
`q`. Positivity requires the two local amplitudes to have positive product.
No all-`r` nonconvolution theorem, metric/source response, or action-selection
principle is asserted.

### All-`(r,q)` determinant offdiagonal selection and shared-rung context

The preceding witness is one entry of an exact determinant-sector selection
rule on every finite open ladder.  Label normalized coarse determinant spin
networks by `y in F_2^q`,

```text
Phi_y=product_(c=0)^(q-1) det(delta_c)^(y_c),
```

and let `iota_r(y) in F_2^(rq)` repeat each coarse bit on its `r` fine
plaquettes.  If `x` is a fine plaquette subset, its determinant cycle occupies

```text
w(x)=2|x|+2 runs(x)                                (34r)
```

original links, where `runs(x)` counts maximal occupied intervals in the open
ladder and `w(0)=0`.  Thus its exact temporal multiplier is
`tau_x=t_det^w(x)`.  With `e_p` the unit fine-plaquette word, the determinant
part of the residual insertion is

```text
(B_det)_(x,y)
 =-c_det^(n) sum_(p=0)^(rq-1)
       a_p 1_{x=iota_r(y) xor e_p}.                (34s)
```

For distinct coarse determinant words `y!=z`, this block gives the *complete*
full-`O(3)` response matrix element:

```text
<Phi_y,R_epsilon Phi_z>
 =epsilon^2(c_det^(n))^2/4 sum_(p,k) a_p a_k
   1_{iota_r(y) xor e_p=iota_r(z) xor e_k}
   (tau_(iota_r(y))+tau_x)
   (tau_(iota_r(z))+tau_x),                        (34t)

x=iota_r(y) xor e_p.
```

Equation (34t) uses Block227's normalized crossing.  A common nonzero scalar
normalization multiplies its right side by the scalar square, as in (24).

Indeed, a non-determinant insertion leaves an unmatched irrep on an exclusive
rail edge of a coarse cell in `y xor z`; linkwise central convolution cannot
change it.  For `r=2`, matching all exclusive rail labels forces both
insertions to be determinant.  For `r>=3`, one plaquette in every changed
coarse cell remains untouched and supplies the mismatch.  This is the same
edgewise Peter--Weyl argument as (34o), now with all retained backgrounds
included.

The indicator in (34t) is nonzero exactly when

```text
r=2 and z=y xor e_c                                  (34u)
```

where `e_c` is the unit coarse-cell word. For one coarse cell `c`, under
`t_det>0` and positive coefficients, the two
matched terms are strictly positive.  Thus `r=2` gives precisely the edges of
the coarse determinant hypercube for every finite `q`.  Its vacuum-to-single-
cell edge is (34o), independent of the other empty cells. No product of
action coefficients from two different retained cells occurs in this block.
For every `r>=3`
the whole vacuum-to-determinant and, more strongly, determinant-to-determinant
offdiagonal block vanishes at quadratic response order.  This exact sector
selection does not say that the full response is a convolution, does not
remove the mixed kinetic descendant (34c)--(34g), and does not exclude the
order-`r` multiplication response (32).

The arbitrary-`q` `r=2` response is not a tensor product of one-cell
responses.  From (34r),

```text
w(iota_r(y))=2r|y|+2 runs(y).                       (34v)
```

Adjacent occupied retained cells share and cancel a retained rung, changing
`4r+4` to `4r+2`.  With `r=2,q=2`, `t_det=1/2` and
`epsilon=c_det=a_p=1`, exact fractions give

```text
<Phi_00,R Phi_10>=85/2048,
<Phi_01,R Phi_11>=67/2097152,                       (34w)
```

whereas a tensor product of the one-cell responses predicts `85/8388608` for
the second entry.  Equations (34t)--(34w), not a copied local coefficient,
are the scale-compatible response law.  The zero entries for `r>=3` are a
finite determinant-sector orthogonality classification, not an all-route
no-go or an all-channel convolution theorem.

### Exact finite-step response order on the determinant channel

The quadratic zero at `r>=3` is not a disappearance of the determinant
response.  It is an exact response-order selection.  Fix a coarse cell `c`,
write `H_c` for its `r` consecutive fine plaquettes, and put

```text
Y=iota_r(y),        Z=Y xor H_c,
F_Y(X)=sum_(A subseteq X) tau_(Y xor A).            (34x)
```

Thus `Xi_Z=J_r Phi_(y xor e_c)` and `tau` is the actual
original-link multiplier from (34r), including every retained-background
and shared-rung cancellation.  Let

```text
L_epsilon(lambda)=(I-Q)S_epsilon(lambda)J_r.
```

For a proper nonempty `X subset H_c`, edgewise Peter--Weyl orthogonality and
the two half-action factors give the first possible determinant-cycle
coefficients

```text
1/|X|! <Xi_(Y xor X),partial_lambda^|X|L_epsilon(0)Phi_y>
 =(epsilon c_det^(n)/2)^|X|
   product_(p in X)a_p F_Y(X),

1/(r-|X|)! <Xi_(Y xor X),
 partial_lambda^(r-|X|)L_epsilon(0)Phi_(y xor e_c)>
 =(epsilon c_det^(n)/2)^(r-|X|)
   product_(p in H_c\X)a_p F_Z(H_c\X).             (34y)
```

Here `Xi_s` is the normalized fine determinant-cycle state.  The second sum
is based at `Z`, not at the vacuum word; replacing it by `F_0(H_c\X)` is
already false for `r=3`.  The residual projector deletes exactly the endpoint
words `X=emptyset,H_c`.  Leibniz's rule in the exact Gram identity
`D_epsilon=L_epsilon*L_epsilon` therefore gives

```text
1/r! <Phi_y,partial_lambda^rD_epsilon(0)
                  Phi_(y xor e_c)>
 =(epsilon c_det^(n)/2)^r product_(p in H_c)a_p
   sum_(emptyset != X proper_subset H_c)
       F_Y(X) F_Z(H_c\X) >0.                       (34z)
```

The inequality holds for the supplied positive finite crossing and positive
local amplitudes.  A common lambda-independent temporal normalization
multiplies the right side by its square.  All determinant offdiagonal
derivatives of order below `r` vanish.  At total order `r`, every fine
plaquette in `H_c` must be inserted exactly once: otherwise an exclusive rail
pair remains unmatched.  The same rail argument forces the inserted irrep on
every plaquette to be `det`, so (34z) is the complete full-`O(3)` matrix
element, not a determinant-quotient contribution vulnerable to cancellation.
No action coefficient outside `H_c` occurs; other retained cells enter only
through `tau_Y,tau_Z`.

For `r=2,y=0`, the two proper subsets in (34z) reproduce (34o) exactly.
As `epsilon` tends to zero, `t_det` and every `tau` tend to one, each summand
after the factor `2^-r` tends to one, and (34z) becomes

```text
1/r! <1,partial_lambda^rD_epsilon(0)Phi_(e_c)>
 =epsilon^r(c_det^(n))^r(2^r-2)
  product_(p in H_c)a_p+o(epsilon^r),               (34aa)
```

which is precisely the determinant Fourier matrix element of (32): the
displayed `(-1)^r` there combines with
`<h,chi_det>^r=(-c_det^(n))^r` to give the positive sign.  Thus the actual
changing-carrier square carries a nonzero finite-step determinant response
at exactly the blocking order `r`, even though its quadratic determinant
offdiagonal vanishes for `r>=3`.  This is a fixed-finite-`r,q,n` derivative at
`lambda=0`; it is not an all-lambda, all-channel, continuum, or physical-time
claim.

### All-pairs determinant response-order filtration

The one-cell formula extends to the whole coarse determinant block, but the
projector deletion is no longer an endpoint deletion.  Let `y!=z`, set

```text
C(y,z)={c:y_c!=z_c},       d=|C(y,z)|,
H=union_(c in C(y,z))H_c,  m=|H|=rd,
Y=iota_r(y),               Z=iota_r(z)=Y xor H,    (34ab)
```

and define the block-cylindrical subset family

```text
Cyl(H)={union_(c in E)H_c:E subseteq C(y,z)}.       (34ac)
```

It has exactly `2^d` members.  The determinant cycle `Xi_(Y xor X)` lies in
`Ran J_r` exactly when `X in Cyl(H)`.  Therefore the exact complete physical
matrix element is

```text
1/m! <Phi_y,partial_lambda^mD_epsilon(0)Phi_z>
 =(epsilon c_det^(n)/2)^m product_(p in H)a_p
   sum_(X subseteq H, X notin Cyl(H))
       F_Y(X) F_Z(H\X).                            (34ad)
```

Every determinant offdiagonal derivative of order below `m=rd` vanishes.
At total order `m`, the exclusive rail pair of every changed fine plaquette
forces exactly one insertion there and no insertion outside `H`; matching the
two columns forces every inserted irrep to be `det`.  Thus (34ad) is the full
`O(3)` coefficient, including `P_(rq),P_lr,J_r,Q`, not a quotient-sector
contribution.  No action coefficient outside `H` occurs.  Other cells and the
placement of the changed cells remain visible through the global
`tau_(Y xor A)` and `tau_(Z xor A)`, so the finite-step value is not a function
of Hamming distance alone.

For nonzero local amplitudes, (34ad) is the first possible nonzero determinant
offdiagonal order; it is strictly positive when all `a_p`, `p in H`, are
positive.  If any `a_p` in `H` vanishes, the exclusive-rail constraint leaves
the matrix element zero at every response order.  As `epsilon` tends to zero,
every retained subset contributes one after the global `2^-m` cancellation.
Since `Q` deletes `2^d`, not two, subsets,

```text
1/m! <Phi_y,partial_lambda^mD_epsilon(0)Phi_z>
 =epsilon^m(c_det^(n))^m(2^m-2^d)
   product_(p in H)a_p+o(epsilon^m),  m=rd.         (34ae)
```

Hence, for positive supplied amplitudes, the determinant response matrix has
the exact filtration `ord_lambda(y,z)=r d_H(y,z)`.  For arbitrary real
nonzero amplitudes the sign is `sign(product_(p in H)a_p)`.  This is a
positive all-pairs classification at fixed finite `r,q,n`, not an all-channel
or all-lambda no-go statement.

## Finite Peter--Weyl approximation of the defect

At each fixed `epsilon`, specialize the
[finite-packet physical-transfer theorem](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_PETER_WEYL_OPERATOR_TRUNCATION_BOUNDED_THEOREM_NOTE_2026-08-28.md)'s
original normalized physical transfer `mathcal T_(r,q)` to the Block227 temporal coefficient
`q_epsilon` and spatial half-action coefficients `epsilon a_p/2`.  This is
exactly `S_epsilon` from (7) on the physical ladder space.  Let
`S_epsilon^K` be the corresponding Block231 positive finite packet applied to
every actual factor before Haar contraction, with the same normalization
convention.  Write

```text
eta_(K,r,q)
 =(3rq+1)delta_kappa+2rq delta_beta,                (35)
```

where the local tails and cutoffs are exactly those of Block231.  Its
absolute physical operator theorem gives

```text
||S_epsilon-S_epsilon^K||_op<=eta_(K,r,q).          (36)
```

Both steps are contractions.  For the defect map

```text
Def_J(S)=J*S^2J-(J*SJ)^2,                           (37)
```

two telescoping products give

```text
||Def_J(S)-Def_J(S^K)||_op
 <=4||S-S^K||_op
 <=4 eta_(K,r,q).                                  (38)
```

The same `3rq+1`/`2rq` census therefore controls the actual square, not an
auxiliary message.  Generic Poisson tails are prior art; equation (38) is
their typed consumer here.

For the Block227 co-scaled family, the temporal packet scale grows as the
inverse small step.  To resolve the nonzero coefficient `Gamma` in (13), the
cutoff must be chosen so

```text
eta_(K,r,q)=o(epsilon^2).                           (39)
```

Block231's explicit rule supplies such a finite cutoff at every finite
`epsilon,r,q`; it grows at least linearly with the local coupling scale and
logarithmically with `rq/epsilon^2`.  This is a quantitative approximation
cost, not a continuum theorem.

For the pure-potential specialization, resolving the nonconstant order-`r`
value contribution underlying (32) at fixed nonzero `lambda` requires the stronger
`eta_(K,r,q)=o(epsilon^r)`.

There is also a distinct exact quadratic-response estimate.  Set

```text
R_epsilon=(1/2)partial_lambda^2D_epsilon|_0=L_epsilon*L_epsilon. (40)
```

Use the same exact Block231 temporal normalization for the exact and packet
families, with no separate truncated renormalization, and take
`K_beta>=1` on every spatial half-action.  For the local half packet
`ell_s^K=e^-s sum_(j=0)^K(su)^j/j!`,

```text
ell_0^K=1,       partial_s ell_s^K|_0=u-1,          (41)
```

exactly.  Thus the packet has the same first `lambda` derivative as the exact
spatial multiplier at `lambda=0`; the leakage map remains the same
`B=(I-Q)V_fJ_r`.  The packet temporal operator `C_epsilon^K` has the same
factorized central-convolution/product-map topology, so it preserves
`Ran J_r` and induces `C_c,epsilon^K=J_r*C_epsilon^KJ_r`.  Put

```text
N_t=3rq+1,
theta_K=1-(1-delta_kappa)^N_t<=N_t delta_kappa.    (42)
```

Block231's complete temporal-kernel sandwich at `lambda=0`, including its
common exact `Z_kappa` normalization, gives

```text
||C_epsilon-C_epsilon^K||_op<=theta_K,
||C_c,epsilon-C_c,epsilon^K||_op<=theta_K.         (43)
```

Define

```text
D_epsilon^K(lambda)=Def_(J_r)(S_epsilon^K(lambda)),
L_epsilon^K
 =-(epsilon/2)(B C_c,epsilon^K+C_epsilon^K B),
R_epsilon^K
 =(1/2)partial_lambda^2D_epsilon^K|_0
 =(L_epsilon^K)*L_epsilon^K.                       (44)
```

All four temporal operators in (43)--(44) are contractions and
`||B||^2=||Gamma||`.  Therefore

```text
||L_epsilon-L_epsilon^K||_op
 <=epsilon sqrt(||Gamma||) theta_K,

||R_epsilon-R_epsilon^K||_op
 <=2epsilon^2||Gamma|| theta_K
 <=2epsilon^2||Gamma||(3rq+1)delta_kappa.          (45)
```

For `r>=3`, `||Gamma||=gamma` from (34d).  Equation (45) is the requested
finite-Peter--Weyl bound for the complete physical quadratic *half-response*;
the bound for the full `partial_lambda^2D|_0` is twice its right side.  No
`delta_beta` term appears because (41) is exact, but the condition
`K_beta>=1` is load-bearing.  Separately top-normalizing the exact and packet
responses, or renormalizing the packet local density by its own partition
function, defines a different response and is not inferred here.

There is also a response-specific packet bound at the newly selected order
`r`.  Define the exact and packet determinant entries

```text
mathcal R_(c,y)^[r]
 =1/r! <Phi_y,partial_lambda^rD_epsilon(0)
                   Phi_(y xor e_c)>,

mathcal R_(c,y;K)^[r]
 =1/r! <Phi_y,partial_lambda^rD_epsilon^K(0)
                   Phi_(y xor e_c)>.               (46)
```

Keep the same exact Block231 temporal normalization in both paths, use no
separate packet renormalization, and require `K_beta>=1` on every spatial
half-action.  The exclusive-rail selection in (34y) uses one first derivative
on each of the `r` distinct plaquettes, so (41) makes every supplied action
insertion exact.  Only the temporal determinant-cycle multipliers change.
If `tau_s^K` is the packet multiplier and `N_t=3rq+1`, (42) gives

```text
|tau_s-tau_s^K|<=theta_K,
theta_K=1-(1-delta_kappa)^N_t<=N_t delta_kappa.     (47)
```

Let `F_Y^K(X)=sum_(A subseteq X)tau_(Y xor A)^K`.
Since both temporal transfers are positive contractions,

```text
|F_Y(X)-F_Y^K(X)|<=2^|X| theta_K,
|F_Y(X)|,|F_Y^K(X)|<=2^|X|.
```

Apply these bounds to the two factors in every proper-subset summand of
(34z).  With arbitrary real local amplitudes,

```text
|mathcal R_(c,y)^[r]-mathcal R_(c,y;K)^[r]|
 <=2(2^r-2)(epsilon c_det^(n))^r
      product_(p in H_c)|a_p| theta_K

 <=2(2^r-2)(epsilon c_det^(n))^r
      product_(p in H_c)|a_p|(3rq+1)delta_kappa.   (48)
```

There is no `delta_beta` term because the selected local first derivatives
are exact, but `K_beta>=1` is load-bearing.  Equation (48) controls the
complete physical `J_r` response matrix element, not an auxiliary message or
an undifferentiated transfer.  It is pointwise in fixed finite `r,q,n`; the
factor `2^r-2` is an honest response-order cost and is not claimed uniform in
blocking factor.  The leading `2` is also load-bearing: at `tau=1`, the
range-preserving scalar-loss control `C^K=(1-theta)C` sends the response to
`(1-theta)^2mathcal R`, whose error
`(2theta-theta^2)|mathcal R|` exceeds `theta|mathcal R|` for `0<theta<1`.

For the all-pairs coefficient in (34ad), the same proof replaces `r` by
`m=rd` and the number of retained subsets by `2^m-2^d`.  Type the two
complete physical entries by

```text
mathcal R_(y,z)^[m]
 =1/m! <Phi_y,partial_lambda^mD_epsilon(0)Phi_z>,

mathcal R_(y,z;K)^[m]
 =1/m! <Phi_y,partial_lambda^mD_epsilon^K(0)Phi_z>,
m=r d_H(y,z).                                     (49a)
```

Then

```text
|mathcal R_(y,z)^[m]-mathcal R_(y,z;K)^[m]|
 <=2(2^m-2^d)(epsilon c_det^(n))^m
      product_(p in H)|a_p| theta_K

 <=2(2^m-2^d)(epsilon c_det^(n))^m
      product_(p in H)|a_p|(3rq+1)delta_kappa,
 m=r d_H(y,z).                                    (49b)
```

Again `K_beta>=1` is sufficient and load-bearing because the minimal
coefficient uses one first derivative on each distinct plaquette in `H`.
Equation (49b) is an all-pairs determinant-block response bound, not an
operator-norm bound on every response channel.

## Prior-art and exact increment

The closest current and in-flight surfaces are distinct:

- Block227's cubic BCH residual compares a symmetric temporal product on one
  fixed carrier; it does not insert `Q=J_rJ_r*` or compare the two paths (8).
- Block228 derives a one-cell generated crossing `p=aH/Z`; it does not test
  temporal semigroup multiplication across changing carriers.
- Block229 proves direct/staged *spatial* Haar associativity for the four-frame
  message; it does not claim temporal range invariance.
- Block231 controls a finite packet for one complete transfer; it does not
  form or bound the semigroup defect.
- Current source and the open stack contain generic free-Haar cumulants and
  character convolution powers, but no conditioned-product `(r-1)`-wise Haar
  hierarchy or `2^r-2` action response of the complete physical `J_r` square.
- Generic Duhamel and fixed-carrier BCH expansions do not contain the typed
  conditioned-fiber Dirichlet term `B*A_fB`, its physical `J_r` Gram consumer,
  or the actual `O(3)` scalar-remainder closure (34g).
- Generic compactness or character diagonality does not produce the exact
  determinant selection (34o), (34t)--(34w), whose original-link incidence,
  complete `J_r` response, and shared-rung context are carrier specific.
- Generic exponential differentiation does not supply the residual-projector
  endpoint deletion, full-`O(3)` exclusive-rail selection, or actual-link
  temporal subset sums in the exact finite-step response (34x)--(34aa).
- Neither the open stack nor generic cumulant algebra supplies the all-pairs
  filtration `ord_lambda=r d_H`, the deletion of every block-cylindrical
  residual, or the actual-link context and packet law (34ab)--(34ae), (49b).
- Generic compression inequalities and conditional variances are credited
  mathematical machinery, not the novelty claim.

The exact increment is the physical `J_r` square (1), its Block227 core
interaction (14), the kinetic-range reduction (15)--(16), and the explicit
nonconstant exterior variance (4)--(5), together with the arbitrary-`r`
conditioned-Haar hierarchy (25)--(28), the complete-step response (29)--(34),
the quadratic kinetic response (34a)--(34j), the finite-step determinant
selection and all-pairs response-order law (34k)--(34ae), and the full packet
consumer (38), (40)--(49b).

## Obligation graph and boundaries

| Obligation | Status | Evidence |
|---|---|---|
| type the physical coarse/fine spaces and `J,Q` | proved/imported | (6) |
| exact direct-versus-staged square | proved | (8)--(10) |
| leading Block227 generated interaction | proved on the core | (11)--(14) |
| kinetic cylindrical range | proved | (15) |
| reduce interaction to conditional variance | proved | (16)--(21) |
| prove nonconstant full-`O(3)` exterior channel | proved | Peter--Weyl argument after (21) |
| exact independent finite control | proved | (22)--(23) |
| normalization scaling | proved | (24) |
| arbitrary-`r` Haar independence and leading variance | proved | (25)--(28) |
| complete-step `r`th action response | proved strong/core at fixed finite `r,q,n` | (29)--(32) |
| finite leading exterior response carrier | proved | (33)--(34) |
| quadratic complete-step action response and induced kinetic descendant | proved strong/core at fixed finite `r,q,n` | (34a)--(34j) |
| exact finite-step determinant offdiagonal selection and context | proved for finite `r>=2,q`; positive only on `r=2` hypercube edges for positive coefficients | (34k)--(34w) |
| exact finite-step determinant response order | proved for fixed finite `r>=2,q,n`; orders below `r` vanish and the `r`th vacuum-to-cell derivative is positive for positive local coefficients | (34x)--(34aa) |
| exact all-pairs determinant response-order filtration | proved for fixed finite `r>=2,q,n`; order `r d_H`, `2^d` cylindrical deletions, and positive coefficient for positive changed-cell amplitudes | (34ab)--(34ae) |
| finite packet error with explicit `rq` | proved | (35)--(39) |
| finite packet quadratic half-response with explicit `rq` | proved | (40)--(45) |
| finite packet selected order-`r` determinant response with explicit `rq` | proved | (46)--(48) |
| finite packet all-pairs determinant response with explicit `rq` | proved | (49a)--(49b) |
| physical scale/time/state/observable family | open | not supplied |
| metric/source/matter response | open | pure-gauge carrier omits these variables |
| continuum, Lorentz, gravity, action selection | open and not inferred | scope fence |

The result supplies a concrete multiscale consumer.  At blocking factor two,
retaining `Gamma` reproduces the order-`epsilon^2` direct/staged separation
that inherited one-step recompression omits.  For arbitrary fixed `r`, the
leading nonconstant multiplication-symbol response at its minimal `epsilon`
degree occurs at bidegree `epsilon^r lambda^r` and remains in a finite leading
exterior character carrier. For each fixed `r`, equation (32) gives its exact
coefficient. Enlarged perfect actions, exact finite-`epsilon` memory kernels,
and continuum limits remain separate open constructions.

At the complete-operator level, equation (34c) supplies a distinct earlier
quadratic response: for `r>=3` its `epsilon^2` value is scalar, while its
`epsilon^3` descendant is exactly
`-2gamma A_c^ind-u_(r,q)I`.  This is the typed kinetic channel that the
multiplication-only hierarchy does not see; at this bidegree the exact
zero-order remainder is scalar and the first-order remainder vanishes.

At `r=2`, equations (34o) and (34t) go beyond the small-step expansion: the
exact finite-step quadratic response has positive determinant off-blocks
exactly on coarse-hypercube edges for every finite `q`.
It is therefore not an inherited central coarse crossing, even though it
remains residual-gauge/conjugation compatible.  This is the typed downstream
history coordinate forced by the actual shared-rung transfer.
For `q>1` its coefficients depend on the retained determinant background and
are not a tensor product of the `q=1` response. For `r>=3`, the determinant
offdiagonal vanishes at quadratic order while the earlier kinetic descendant
remains in force. Equations (34x)--(34aa) close the apparent response gap:
the first determinant vacuum-to-cell offdiagonal occurs at derivative order
`r`, is strictly positive at every supplied finite step for positive local
coefficients, and reduces to the earlier `2^r-2` small-step coefficient.
Equations (34ab)--(34ae) complete this determinant-block classification:
between words at Hamming distance `d`, the first possible order is `rd`, the
projector removes all `2^d` block-cylindrical residuals, and the small-step
coefficient is `2^(rd)-2^d`.  At finite step the global temporal multipliers
retain placement and background information, so equal-distance entries need
not agree.

## Reproduction and landing conditions

Run from repository root:

```bash
python3 scripts/admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_2026_08_28.py
python3 scripts/admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_2026_08_28.py --mode independent
python3 scripts/admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_independent_2026_08_28.py
```

Acceptance requires zero baseline failures, a separately implemented exact
helper, every hostile mutation failing exactly one intended gate, a fresh
cache and citation manifest, exact-byte root and independent review, and a
cumulative refreshed-main replay.  The PR, if the full promotion gate passes,
must remain stacked on Block231 and unmerged.

No claim in this note changes an axiom, primitive, audit verdict, or repo-wide
authority surface.
