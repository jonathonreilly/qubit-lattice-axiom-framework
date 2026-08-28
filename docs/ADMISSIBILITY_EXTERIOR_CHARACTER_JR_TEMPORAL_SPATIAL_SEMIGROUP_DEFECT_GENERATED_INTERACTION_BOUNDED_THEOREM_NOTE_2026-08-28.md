---
claim_id: admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_generated_interaction_bounded_theorem_note_2026-08-28
claim_type: bounded_theorem
claim_scope: "For the supplied Block227 co-scaled exterior-character step on a finite O(3) ladder and the supplied Block229 retain-every-r physical Haar isometry J_r, prove the exact positive direct-versus-staged temporal-spatial compression defect J_r* S^2 J_r-(J_r*S J_r)^2=J_r*S(I-J_rJ_r*)S J_r. On the Block227 Peter--Weyl core derive its leading generated interaction Gamma=J_r*G(I-J_rJ_r*)GJ_r. For retain-every-two on the actual two-cell ladder, prove that the kinetic generator preserves the cylindrical range while the equal-coefficient exterior spatial potential generates a nonconstant conditional-variance interaction, and evaluate an exact Z2 finite control. Bound finite Peter--Weyl approximation of the complete defect by four times the Block231 physical-transfer error with explicit rq accumulation. This is a conditional finite mathematical generated-interaction theorem, not a physical time, continuum, action-selection, Lorentz, gravity, metric/source, or matter-current theorem."
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
next_trace_action: "Any multiscale construction must retain or approximate the generated conditional-variance interaction and control its accumulation; physical spacing, time, states, and observables remain separate suppliers."
conditional_surface_status: "exact finite physical-space temporal-spatial compression defect and nonconstant generated exterior interaction, conditional on the supplied co-scaled action, ladder, Haar measure, projector, and J_r stack"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the compression identity, core limit, cylindrical kinetic calculation, conditional-variance formula, nonconstancy proof, exact finite control, and finite-packet defect bound are exact mathematical results with no fitted datum"
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

## Authority and imports

The pinned landed authority is `origin/main` commit
`66e478505e055faf4a5b9e6f4883211e44304718`.  The exact parent of this branch
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
| equal positive coefficients on the two fine plaquettes | explicit witness specialization | supplied here inside the Block227 action family | no uniqueness or physical coefficient claim |
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
 =(3rq+1)delta_kappa+2rq delta_beta,                (25)
```

where the local tails and cutoffs are exactly those of Block231.  Its
absolute physical operator theorem gives

```text
||S_epsilon-S_epsilon^K||_op<=eta_(K,r,q).          (26)
```

Both steps are contractions.  For the defect map

```text
Def_J(S)=J*S^2J-(J*SJ)^2,                           (27)
```

two telescoping products give

```text
||Def_J(S)-Def_J(S^K)||_op
 <=4||S-S^K||_op
 <=4 eta_(K,r,q).                                  (28)
```

The same `3rq+1`/`2rq` census therefore controls the actual square, not an
auxiliary message.  Generic Poisson tails are prior art; equation (28) is
their typed consumer here.

For the Block227 co-scaled family, the temporal packet scale grows as the
inverse small step.  To resolve the nonzero coefficient `Gamma` in (13), the
cutoff must be chosen so

```text
eta_(K,r,q)=o(epsilon^2).                           (29)
```

Block231's explicit rule supplies such a finite cutoff at every finite
`epsilon,r,q`; it grows at least linearly with the local coupling scale and
logarithmically with `rq/epsilon^2`.  This is a quantitative approximation
cost, not a continuum theorem.

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
- Generic compression inequalities and conditional variances are credited
  mathematical machinery, not the novelty claim.

The exact increment is the physical `J_r` square (1), its Block227 core
interaction (14), the kinetic-range reduction (15)--(16), and the explicit
nonconstant exterior variance (4)--(5), with the full packet consumer (28).

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
| finite packet error with explicit `rq` | proved | (25)--(29) |
| physical scale/time/state/observable family | open | not supplied |
| metric/source/matter response | open | pure-gauge carrier omits these variables |
| continuum, Lorentz, gravity, action selection | open and not inferred | scope fence |

The result supplies a concrete multiscale consumer: retaining the generated
interaction `Gamma` (or a controlled approximation to it) reproduces the
order-`epsilon^2` direct/staged separation that an inherited one-step
recompression omits.  Enlarged perfect actions, memory kernels, and continuum
limits remain separate open constructions.

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
