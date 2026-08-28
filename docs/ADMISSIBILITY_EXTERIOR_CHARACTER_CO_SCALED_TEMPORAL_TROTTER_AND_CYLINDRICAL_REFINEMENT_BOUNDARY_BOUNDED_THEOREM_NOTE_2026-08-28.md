---
claim_id: admissibility_exterior_character_co_scaled_temporal_trotter_and_cylindrical_refinement_boundary_bounded_theorem_note_2026-08-28
claim_type: bounded_theorem
claim_scope: "For every fixed finite exterior-character member f_n on a supplied fixed finite O(3) gauge 2-complex with an ordered plaquette-loop list, derive the large-coupling normalized character expansion, a corrected co-scaled temporal clock, and the strong gauge-projected symmetric-product limit to component-preserving rotational heat plus the bounded same-action spatial potential. Quantify the unavoidable cubic channel residual and prove that the same one-coupling family does not satisfy exact cylindrical edge subdivision or natural equal-flux plaquette subdivision. This is a fixed-spatial-carrier mathematical temporal limit and a bounded same-action refinement obstruction, not an exact finite-step semigroup, changing-carrier continuum theorem, physical clock, Hamiltonian identification, selected action, Lorentz result, or gravity result."
depends_on:
  - admissibility_exterior_character_time_refinement_semigroup_obstruction_bounded_theorem_note_2026-08-28
  - minimal_axioms
runner: scripts/admissibility_exterior_character_co_scaled_temporal_trotter_refinement_2026_08_28.py
independent_checker: scripts/admissibility_exterior_character_co_scaled_temporal_trotter_refinement_independent_2026_08_28.py
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_exterior_character_time_refinement_semigroup_obstruction_bounded_theorem_note_2026-08-28
target_blocker_text: "Supply an indexed carrier/coefficient/measure refinement map and test the co-scaled complete transfer; the present exact common-clock obstruction does not decide a different action family or a Trotterized refinement construction."
source_of_blocker_text: frontier_question
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "For genuine spatial refinement, control the renormalized compression J* T_f J or construct a perfect/nonlocal action with an exact comparison; the fixed-carrier temporal product and the bare cylindrical obstruction do not supply a spacetime continuum or physical clock."
conditional_surface_status: "exact all-f_n fixed-carrier temporal strong-product theorem and exact bare cylindrical/equal-flux refinement defects, conditional on the supplied exterior-character time-refinement semigroup-obstruction family and new mathematical scaling laws; no physical time or changing-carrier continuum theorem"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact symbolic large-coupling character asymptotics, a contraction/core product argument, component-rate separation, gauge-typed Haar pullback, and two independent same-action subdivision defects prove the stated bounded theorem without fitted data"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Exterior-character co-scaled temporal Trotter limit and cylindrical-refinement boundary

**Date:** 2026-08-28

**Type:** `bounded_theorem`

**Status:** `proposed_retained` — a review proposal, not an audit verdict.

## Result up front

The finite exterior-character steps are not one exact semigroup family, but a
different and honest statement survives: after a supplied small-step
co-scaling, repeated actual exterior-character kernels converge strongly on a
fixed finite gauge carrier to rotational heat plus the co-scaled spatial
potential.

Fix an integer `n>=1`.  Put

```text
q = 1/(8 kappa),       L_l = l(l+1).                 (1)
```

Let `u_l^(n)(q)` be the normalized proper-component multiplier of the actual
parent crossing kernel in spin `l`.  Direct expansion of the parent action,
the normalized `SO(3)` class measure, and the character gives

```text
log u_l^(n)(q)
 = -L_l q/2 - L_l(5n-2)q^2/8
   + L_l{(12n-4)L_l-(255n^2-171n+24)}q^3/192
   + O_l(q^4).                                           (2)
```

The remainder is for each fixed finite `n,l`; no uniform-in-spin or
uniform-in-member estimate is asserted.

This is an asymptotic of the actual compact integral, not only a formal
Gaussian series.  On the proper component the action
`f_n(theta)=16[1-cos^(2n)(theta/2)]/n` has its unique zero on
`0<=theta<=pi` at `theta=0`.  For every fixed small `delta>0` it has a
strict positive minimum on `delta<=theta<=pi`, so that part of the normalized
class integral is exponentially small in `1/q`.  On `theta<delta`, Taylor's
theorem with a uniform remainder, the scaling `theta=sqrt(q)x`, and a
Gaussian majorant allow termwise integration; the scaled tail is again
exponentially small.  The normalized class measure then gives

```text
I_proper(q)
 = integral_SO(3) exp[-f_n(theta)/(8q)] dR
 = q^(3/2)/(2 sqrt(2 pi)) [1+O(q)],                 (2a)
I_improper(q)=exp[-2/(nq)].                         (2b)
```

The same fixed-`n,l` Taylor/remainder argument through two more even powers
gives the stated `O_l(q^4)` remainder in (2).  Put

```text
alpha_n(q)=I_proper/(I_proper+I_improper)
          =(1+r_det^(n)(q))/2,
r_(l,p)^(n)(q)=alpha_n(q) u_l^(n)(q),  l>=1.        (2c)
```

The improper density is constant, so (2c) is independent of parity `p` for
`l>=1`.  Moreover `1-alpha_n` is smaller than every algebraic power of `q`.
Thus (2) is also the algebraic logarithmic expansion of the full `O(3)`
multiplier `r_(l,p)`, while (2a)--(2c) keep the disconnected component
normalization explicit.

The scalar clock invariant between two nonzero spins is therefore

```text
log(u_l)/L_l - log(u_j)/L_j
 = (3n-1)(L_l-L_j)q^3/48 + O(q^4).             (3)
```

Equation (3) is the local large-coupling version of the exact finite-step
obstruction in the linked [common-clock theorem](ADMISSIBILITY_EXTERIOR_CHARACTER_TIME_REFINEMENT_SEMIGROUP_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-28.md).
It does not prevent convergence.  Supply a mathematical diffusivity `D>0`, a
small parameter `epsilon>0`, and the corrected clock

```text
q_epsilon
 = D epsilon -(5n-2)D^2 epsilon^2/4
   +(15n^2-23n+8)D^3 epsilon^3/32.             (4)
```

Then

```text
log u_l(q_epsilon)
 = -D L_l epsilon/2
   +D^3(3n-1)L_l^2 epsilon^3/48
   +O_l(epsilon^4).                              (5)
```

Thus the exterior kernel has the right first derivative for rotational heat,
while retaining an unavoidable action-family residual at cubic order.  A
further scalar clock correction changes only the part linear in `L_l`; it
cannot remove the `L_l^2` term simultaneously in all channels.

## Supplied fixed-carrier family

Let `Gamma` be a supplied finite spatial gauge 2-complex: a finite oriented
edge graph together with a supplied ordered plaquette-loop list, with at least
one cycle and at least one plaquette.  Its kinematic Hilbert space is
`H=L^2(O(3)^E,dHaar^E)`.  Let `P` be the simultaneous local `O(3)` Haar
projector.  For fixed nonnegative plaquette coefficients `a_p`, with at least
one positive coefficient on a nonconstant plaquette word, define the bounded
nonconstant same-member spatial action

```text
V_n(U) = sum_p a_p f_n(Q(W_p(U))) >= 0.           (6)
```

Both multiplication by `V_n` and the temporal convolution commute with the
gauge action, so `P H` is reducing.  Set

```text
M_epsilon = exp[-epsilon V_n/2],
S_epsilon = M_epsilon P C_(n,q_epsilon) P M_epsilon.  (7)
```

Here `C_(n,q)` is the product of independently normalized actual crossing
convolutions over the finitely many stored links, and `epsilon` is restricted
to the sufficiently small positive range where `q_epsilon>0`.

This is a newly supplied anisotropic mathematical family.  The temporal
coupling and the spatial half-action co-scale; it is not the fixed-`M` family
refuted by the endpoint commutator in Block226.

Let

```text
A = -(D/2) sum_e Delta_e >= 0                     (8)
```

with `-Delta_e` having eigenvalue `L_l` in the spin-`l` channel.  On the
gauge-invariant algebraic Peter--Weyl core, (2)--(5) and boundedness of `V_n`
give

```text
(S_epsilon-I)/epsilon psi -> -(A+V_n)psi.          (9)
```

Define `S_0=I` on `P H`.  Every `S_epsilon` is a self-adjoint contraction,
the family is strongly continuous at zero, and the core is invariant under
the finite character-polynomial potential and is a core for the positive
self-adjoint bounded perturbation `G=A+V_n`.  The precise general bridge is
the Chernoff contraction-product theorem: if `F(0)=I`, `F(s)` is a strongly
continuous contraction family, `(F(s)psi-psi)/s -> -G psi` on a core for the
generator `-G`, and the closure/range condition for that core holds, then
`F(t/m)^m -> exp(-tG)` strongly.  Here (9) supplies the derivative, the
algebraic Peter--Weyl space is a core for `G`, `G` is nonnegative
self-adjoint, hence the range condition holds, and (7) supplies contraction
and strong continuity.  Therefore

```text
[S_(t/m)]^m psi -> exp[-t(A+V_n)] psi,
psi in P H,       m -> infinity.                  (10)
```

Only the small-`epsilon` germ enters this limit.  Equivalently, one may extend
the contraction family constantly beyond the positive domain of (4) before
applying the global formulation of the product theorem.

The statement is strong convergence, not operator-norm convergence.  For
every finite exterior step the convolution is compact on the infinite
Peter--Weyl carrier and its high-spin multipliers tend to zero, so

```text
||C_(n,q)-I|| = 1.                                (11)
```

No uniform one-step norm approximation to the identity is claimed.

## Exact symmetric-product residual

On any fixed finite Peter--Weyl compression, or vectorwise for an analytic
vector lying in the domains of the displayed nested commutators, put
`A_l=D L_l/2`.  Symmetric multiplication and the corrected channel logarithm
give

```text
log S_epsilon
 = -epsilon(A+V_n)
   +epsilon^3{
      D(3n-1)A^2/12
      +[V_n,[V_n,A]]/24
      -[A,[A,V_n]]/12
    }
   +O_psi(epsilon^4).                             (12)
```

The first term in braces is specific to the actual exterior action.  The other
two are the symmetric-product commutator residuals.  On any fixed finite
Peter--Weyl compression or fixed smooth vector with the required graph norms,
the local cubic remainder gives the expected global `O(epsilon^2)` diagnostic.
Equation (10), rather than a finite compression, carries the full strong
theorem.  No global operator-norm rate is asserted.

## The determinant sector freezes

The same exterior family does not generate a finite component-jump rate.
Equations (2a)--(2b) give, in the variable (1),

```text
1-r_det^(n)(q)
 ~ 4 sqrt(2 pi) q^(-3/2) exp[-2/(nq)].             (13)
```

For `q=q_epsilon` and `m=t/epsilon`,

```text
[r_det(q_epsilon)]^m -> 1.                         (14)
```

The limiting kinetic operator is rotational heat separately on the connected
components.  Before gauge projection it preserves every link determinant;
after projection it preserves the surviving `Z_2` holonomy sectors.  A tree
may have no nontrivial sector.  A nonzero component-jump rate requires a new
independently scaled `Z_2` law.

There is no alternative one-parameter scaling that gives both finite positive
rotational diffusion and finite positive component mixing.  Finite rotational
diffusion requires `kappa(epsilon)` of order `1/epsilon`; then (13) gives zero
jump rate.  Scaling `kappa` only logarithmically to retain determinant jumps
makes the accumulated rotational rate diverge.  This is a component-rate
dichotomy, not a selection of one component.

## Genuine cylindrical pullback and exact failure

Temporal repetition on one fixed graph is not spatial carrier refinement.  To
test the latter, subdivide one coarse edge into `m>1` oriented fine edges and
define

```text
pi(g_1,...,g_m)=g_m ... g_1,
(J f)(g_1,...,g_m)=f(pi(g_1,...,g_m)).              (15)
```

Product normalized Haar measure makes `J` an exact isometry.  Internal fine
gauge transformations cancel in the ordered product, so

```text
P_f J = J P_c.                                     (16)
```

On a coarse irrep matrix coefficient, independently convolving the `m` fine
edges multiplies by the full normalized multiplier `r_(l,p)(q_f)^m`.  Exact
bare cylindrical intertwining inside the same one-coupling family would
require

```text
r_(l,p)(q_c)=r_(l,p)(q_f)^m       for every l,p,    (17a)
r_det(q_c)=r_det(q_f)^m.                          (17b)
```

Choose `q_c` by exact full spin-one matching near zero.  Since `log alpha_n`
is beyond every algebraic order, its power series is the same as the solution
obtained from `u_1`, namely

```text
q_c=m q_f-m(m-1)(5n-2)q_f^2/4+O(q_f^3).           (17c)
```

The full spin-two channel then has the unavoidable algebraic defect

```text
log r_(2,p)(q_c)-m log r_(2,p)(q_f)
 = (3n-1)(m^3-m)q_f^3/2 + O(q_f^4).                (18)
```

The determinant channel fails independently at this same matched clock.  If
`d_n(q)=1-r_det^(n)(q)`, then

```text
d_n(q_c)/(m d_n(q_f))
 ~ m^(-5/2)
   exp[-(m-1)(5n-2)/(2nm)]
   exp[2(1-1/m)/(n q_f)] -> infinity.              (19)
```

Equation (17b) would instead require
`d_n(q_c)=m d_n(q_f)+O(d_n(q_f)^2)`, contradicting (19).  Thus the natural
same-family edge pullback is gauge typed but is not an exact transfer
intertwiner.  A perfect or nonlocal action, an irrep-dependent coupling, an
enlarged coarse basis, or a separately scaled determinant factor is not ruled
out.

## Equal-flux plaquette subdivision also changes the action

The natural local spatial lift fails even before transfer integration.  On a
proper `SO(2)` plaquette with angle `theta`, split the flux equally among four
fine plaquettes and multiply each fine coefficient by four so that the
quadratic Hessian matches.  The total fine-minus-coarse action is

```text
16 f_n(Q(theta/4))-f_n(Q(theta))
 = 5(3n-1)theta^4/32 + O(theta^6).                 (20)
```

At `theta=pi` the difference is exactly

```text
16/n {16[1-((2+sqrt(2))/4)^n]-1} > 0.              (21)
```

For `n=1`, (21) is `112-64 sqrt(2)>0`.  Matching the tangent Hessian does not
give exact same-action refinement.  This does not rule out a renormalized
compression `J* T_f J`, coefficient flow, or perfect action.

## Imports and open boundaries

The load-bearing dependencies are the linked Block226 theorem and the
[minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).  The latter explicitly do not
supply an action, clock, time metric, or physical Hamiltonian.

| Input | Role here | Provenance | Open boundary |
|---|---|---|---|
| every fixed finite `f_n`, normalized exterior crossing, full `O(3)` carrier | actual kernel expanded and iterated | linked Block226/its parent | no action-family selection |
| fixed finite gauge 2-complex with an ordered plaquette-loop list | carrier for (6)--(12) | supplied topology and incidence data | no volume or thermodynamic theorem |
| normalized product Haar measure | Hilbert and pullback isometry | supplied mathematical measure | no physical measure selection |
| `D>0`, `epsilon`, corrected law (4) | mathematical temporal co-scaling | supplied here | not a derived clock or lattice spacing |
| fixed nonnegative spatial coefficients `a_p` | nonconstant same-member potential | supplied action data | not observational or framework-selected values |
| common local Haar projector `P` | gauge-invariant reducing subspace | supplied parent construction | not a physical-state identification |
| Chernoff contraction-product theorem | strong product bridge | P. R. Chernoff, *J. Functional Analysis* **2** (1968), 238--242, DOI `10.1016/0022-1236(68)90020-7`; exact hypotheses instantiated above | no operator-norm rate |
| ordered edge subdivision and equal-flux plaquette split | hostile carrier/action tests | supplied refinement maps | no claim about all possible refinements |
| determinant jump factor | absent from the actual family | would be a new supplied law | no orientation-flip dynamics derived |

No literature coefficient, fitted spectrum, or observed value is used.  The
sole external mathematical theorem is the explicitly cited Chernoff
contraction-product lemma.  No physical time,
mass, Hamiltonian, continuum embedding, Lorentz transformation, Standard Model
input, stress law, Einstein equation, or gravity selection is used.

## Proof-obligation graph

```text
Block226 actual exterior family and exact finite-step no-clock theorem
  + supplied fixed gauge 2-complex/ordered plaquette-loop list/Haar/P
  + supplied q_epsilon and epsilon V_n half-actions
  -> exact fixed-spin expansion (2)--(5)
  -> core derivative and contraction product
  -> strong fixed-carrier temporal limit (10)
  -> determinant-rate dichotomy (13)--(14)

ordered Haar-isometric edge pullback
  -> gauge intertwining (16)
  -> spin and determinant channel defects (18)--(19)

equal-flux plaquette split
  -> quartic and exact pi defects (20)--(21)
  -> no natural exact same-action spatial refinement
```

The first chain is constructive.  The second and third chains prune two bare
refinement routes.  None identifies the parameter with physical time.

## No-Go Discipline Gate

The negative content is restricted to exact common-clock/cylindrical and
natural equal-flux same-action routes.  It is not a no-go for perfect actions,
renormalized compressions, new component laws, or physical continuum models.

### N1 -- failed attack routes

| Route | Exact attempt | Why it fails | Marker |
|---|---|---|---|
| reuse the finite-step coupling as an exact clock | require all channel logs proportional | the branch-local Block226 calculation and (3) give incompatible channel ratios | `ATTEMPTED` |
| use only `q=D epsilon` for higher-order heat matching | try to cancel the local scalar error through quadratic order without a clock correction | the universal linear-in-`L` quadratic drift remains; the weaker first-derivative/strong limit still succeeds | `ATTEMPTED` |
| correct one scalar clock | use (4) to cancel all scalar channel drift through cubic order | the `L^2 epsilon^3` term in (5) remains | `ATTEMPTED` |
| fit finitely many irreps | solve channel equations on a truncation | this does not control the full Peter--Weyl carrier or (11) | `ATTEMPTED` |
| obtain determinant flips from the same scaling | accumulate (13) over `t/epsilon` steps | the rate tends to zero | `ATTEMPTED` |
| exact `m`-edge cylindrical lift | match spin one and reuse the coupling | spin two and determinant give (18)--(19) | `ATTEMPTED` |
| exact equal-flux plaquette lift | match the quadratic Hessian | (20)--(21) remain nonzero | `ATTEMPTED` |
| substitute a heat kernel | replace the actual exterior step by the target semigroup | this changes the action family and does not prove the stated theorem | `ATTEMPTED` |

The successful route is not counted as a failed attack: co-scale the actual
temporal and half-action factors, prove the core derivative, and take the
strong contraction product on the fixed carrier.

### N2 -- pairwise independence of remaining interfaces

Let `A` be exact finite-step semigroup law, `B` exact changing-carrier
cylindrical intertwining, `C` nonzero determinant-jump rate, `D` a
renormalized `J* T_f J` comparison, and `E` physical time/Hamiltonian
identification.

| Pair | First closes second? | Second closes first? | Independence evidence |
|---|---:|---:|---|
| `A,B` | no | no | finite-step composition and carrier pullback are different equations |
| `A,C` | no | no | a connected-component jump law is an independent generator coefficient |
| `A,D` | no | no | a conditional coarse kernel need not lie in the bare action family |
| `A,E` | no | no | mathematical composition supplies no physical clock |
| `B,C` | no | no | holonomy pullback does not set the determinant jump rate |
| `B,D` | no | no | bare intertwining and renormalized compression are distinct comparisons |
| `B,E` | no | no | a carrier map supplies no clock/readout identification |
| `C,D` | no | no | component mixing neither constructs nor follows from coarse disintegration |
| `C,E` | no | no | a supplied jump rate is still not physical time |
| `D,E` | no | no | an operator comparison does not identify its scale physically |

No pair collapses.  Fixed-carrier temporal convergence is already proved and
is not counted as one of these five remaining interfaces.

### N3 -- hidden-wall scan

| Scan family | Occurrences checked | Disposition |
|---|---|---|
| chosen / by construction | `D`, `epsilon`, graph, subdivision | explicit supplied mathematical choices; no law selection |
| background / fixed | fixed gauge 2-complex and plaquette-loop list, fixed `n`, fixed coefficients | theorem domain, not a claim of dynamical fixation |
| canonical / natural | ordered product, equal-flux split | exact route names only; alternative maps/actions remain open |
| registered / physical | clock, Hamiltonian, continuum, stress | absent and explicitly not inferred |
| assume / assumption / assumed | Chernoff hypotheses and supplied domains | every assumption is displayed in the fixed-carrier family or theorem statement |
| as is standard / framework provides / bridge context | whole note and runners | no hits; no unnamed framework bridge is consumed |
| obviously / standard QFT | whole note and runners | no hits; no rhetorical substitute for a derivation |
| imported exact values | coefficients in (2)--(5), (18), (20) | symbolically derived by primary and independent arithmetic checks |

No hidden fitted, observational, literature, or authority-status input is
load-bearing.

### N4 -- residual matching

| Source anchor | Attacked residual | Claimed residual | Match? | Evidence |
|---|---|---|---:|---|
| `docs/ADMISSIBILITY_EXTERIOR_CHARACTER_TIME_REFINEMENT_SEMIGROUP_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-28.md:18` | indexed carrier/coefficient/measure map and co-scaled complete transfer | fixed-carrier actual-kernel product plus one typed edge pullback | yes, partially | (4)--(19) |
| `docs/ADMISSIBILITY_EXTERIOR_CHARACTER_TIME_REFINEMENT_SEMIGROUP_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-28.md:128-160` | full normalized `O(3)` multiplier family | proper expansion plus explicit `alpha_n` bridge | yes | (2)--(5) |
| `docs/ADMISSIBILITY_EXTERIOR_CHARACTER_TIME_REFINEMENT_SEMIGROUP_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-28.md:275-329` | common projector and topology survival | ordered Haar-isometric edge pullback | yes | (15)--(19) |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:114-130` | dynamics/time are not axiom inputs | no physical clock or Hamiltonian claim | yes | import and scope fences |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:173-190` | action/source/time remain downstream | supplied action and clock stay explicit | yes | import table |
| this note, changing-carrier target | all renormalized refinement | not claimed | no | `J* T_f J` remains open |

The trace is a partial closure, not target substitution.

### N5 -- rhetoric and resolution audit

`T` means proved theorem, `H` a proved hard boundary, `U` unproved, and `N`
not claimed.

| Negative phrase | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
| no one-step operator-norm approximation to `I` | `T`: high-spin link multipliers tend to zero | `T`: finite-link tensor retains the obstruction | `T`: (11) | `U`: no operator-norm product theorem is claimed | `U`: checked and not executed -- no graph-family norm theorem |
| no exact changing-carrier refinement | `T`: Haar edge map | `T`: internal gauge cancellation | `H`: spin/determinant defects | `U`: renormalized block open | `U`: checked and not executed -- no indexed graph comparison |
| no component-jump rate from this scaling | `T`: (13) | `T`: link determinant freezes | `T`: accumulated rate vanishes | `T`: surviving holonomy sectors only | `U`: checked and not executed -- no volume-uniform sector theorem |
| no physical time/Hamiltonian | `U` | `U` | `U` | `N` | `N`: checked and not executed -- no physical supplier |
| no action/continuum selection | `U` | `U` | `U` | `N` | `N`: checked and not executed -- alternative flows remain open |

Primary execution prints `per_element`, `per_site`, `per_mode`, `per_block`,
and an exact checked/not-executed `lattice_wide` certificate.

### N6 -- convention, primitive, and prior-art scan

The mandatory sweep was refreshed at
`origin/main=66e478505e055faf4a5b9e6f4883211e44304718` and separately across
the open connection stack through Block226.  Blocks224 and 225 are campaign
checkpoints only and have no science artifact or PR.  Both noun orders,
hyphen variants, and the
phrases `co-scaled`, `Trotter`, `character multiplier`, `cylindrical
refinement`, `component jump`, and `strong product` were searched.

```text
git fetch origin main --quiet
git rev-parse origin/main
git grep -n -i -E '(co[- ]scaled.{0,100}Trotter|Trotter.{0,100}co[- ]scaled|cylindrical.{0,100}refinement|refinement.{0,100}cylindrical|component.{0,40}jump|jump.{0,40}component|strong.{0,40}product|product.{0,40}strong)' origin/main -- docs scripts
git grep -n -i -E '(heat kernel|Trotter|strong product|operator norm remainder|same action.{0,80}continuum|continuum.{0,80}same action|refinement net)' origin/main -- docs scripts
for pr_number in 7761 7763 7764 7765 7767 7768 7774; do gh pr view "$pr_number" --json number,headRefOid,state,baseRefName; done
```

The separately scanned live heads were `#7761@311036fd`,
`#7763@714ba06e`, `#7764@488c07b6`, `#7765@6894cdde`,
`#7767@5b9d9efe`, `#7768@9b8ae896`, and parent `#7774@205db872`;
all were open when refreshed and none is current-source authority.

Closest current-source rows are non-authoritative prior art:

| Row | Live status | Applicability |
|---|---|---|
| `EMERGENT_GAUGE_HEAT_KERNEL_CLT_ATTRACTOR_CONDITIONAL_ON_BI_INVARIANT_DYNAMICS_NARROW_THEOREM_NOTE_2026-06-08.md:23-55,65-94` | `bounded_theorem`, audit/effective/intrinsic `unaudited`; `docs/audit/data/ledger/em/emergent_gauge_heat_kernel_clt_attractor_conditional_on_bi_invariant_dynamics_narrow_theorem_note_2026-06-08.json:6,17,36,40` | generic supplied small-step compact-group CLT, no actual `f_n`, nonconstant half-action, or common projector |
| `NATIVE_GAUGE_TRANSFER_OPERATOR_NORM_REMAINDER_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md:50-87,104-161,193-221,273-288` | `bounded_theorem`, audit/effective/intrinsic `unaudited`; `docs/audit/data/ledger/na/native_gauge_transfer_operator_norm_remainder_rung_eight_bounded_note_2026-06-12.json:6,17,30,36` | `SU(3)` Wilson saddle/remainder route; exact operator comparison remains open |
| `ACTION_FAMILY_CHARACTER_SEMIGROUP_DISCRIMINATOR_BOUNDED_NOTE_2026-07-02.md:73-129,154-204` | `bounded_theorem`, audit/effective/intrinsic `unaudited`; `docs/audit/data/ledger/ac/action_family_character_semigroup_discriminator_bounded_note_2026-07-02.json:6,17,31,35` | `U(1)` finite nonsemigroup discriminator; continuum equivalence open |
| `HEAT_KERNEL_GAUGE_ACTION_NATIVE_RP_PLANE_CHARACTER_POSITIVITY_ALL_COMPACT_GROUPS_NARROW_THEOREM_NOTE_2026-07-09.md:32-69,102-123,167-188` | `bounded_theorem`, audit/effective/intrinsic `unaudited`; `docs/audit/data/ledger/he/heat_kernel_gauge_action_native_rp_plane_character_positivity_all_compact_groups_narrow_theorem_note_2026-07-09.json:6,17,30,34` | supplied heat action, not the actual exterior family |
| `FREE_STAGGERED_3PLUS1_SAME_ACTION_TRANSFER_GAUSSIAN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-07-12.md:51-78,164-216,231-267` | `bounded_theorem`, audit/effective/intrinsic `unaudited`; `docs/audit/data/ledger/fr/free_staggered_3plus1_same_action_transfer_gaussian_continuum_bounded_theorem_note_2026-07-12.json:6,17,33,37` | free CAR carrier with no shared `O(3)` projector |
| `UNIVERSAL_QG_CANONICAL_REFINEMENT_NET_NOTE.md:17-29,57-99,116-129` | `positive_theorem`, audit/effective/intrinsic `unaudited`; `docs/audit/data/ledger/un/universal_qg_canonical_refinement_net_note.json:6,17,31,35` | geometric refinement support, no exterior transfer comparison |
| `docs/historic_intake/HISTORIC_MASSIVE_WILSON_STAGGERED_SPATIAL_DLR_ACCUMULATION_OS_TRANSFER_BOUNDED_THEOREM_NOTE_2026_07_12_INTAKE_NOTE_2026-08-05.md:3-15,17-20,27-50` | authority `none`, audit `unset`, `branch_only_never_mainlined` | historic wrapper names an attached factor-two gauge coarse step, but supplies no current attached theorem or actual `O(3)` `f_n` comparison |

The linked in-flight Block226 is the direct supplier and explicitly leaves this
co-scaled route open.  The campaign-only Block224 checkpoint records a
gauge-typed dyadic-map/nonintertwining calculation and leaves `J* T_f J` open;
it has no tracked science artifact or PR and is not source authority.  No exact
current-source or in-flight hit supplies (2)--(21).

Primitive-registry and controlled-vocabulary scans found no clock, heat,
Trotter, refinement, component-jump, or physical-time primitive that could be
silently imported.  No physics literature, literature coefficient, or fitted
datum is used; the 1968 Chernoff product theorem is the sole external general
mathematical theorem and is cited explicitly in the import table.

### N7 -- steelman

The strongest escape is a genuine perfect or renormalized action: choose
scale-dependent spatial and temporal couplings, an independently scaled
determinant jump, and a coarse conditional kernel so that `J* T_f J` rather
than the bare pullback is compared.  A Chernoff/Trotter limit can exist even
when no finite step belongs to one exact semigroup, as (10) itself proves.
None of (18)--(21) rules out that mechanism.  A physical continuum claim would
still require spatial lattice embeddings, coefficient/measure scaling, a time
normalization, and uniform estimates.

### N8 -- cross-cycle echo and live status

| Echo | Live status | Retired here? | Mechanism/applicability |
|---|---|---:|---|
| generic compact-group CLT row | intrinsic/effective `unaudited` | no | supports method context but lacks actual action/full transfer |
| supplied heat-kernel row | `bounded_theorem`, effective `unaudited` | no | different action; no selection |
| `U(1)` finite semigroup discriminator | `bounded_theorem`, effective `unaudited` | no | finite-step method echo only |
| free staggered same-action scaling | `bounded_theorem`, effective `unaudited` | no | different CAR carrier and no common projector |
| historic massive Wilson--staggered intake wrapper | authority `none`, audit `unset`, `branch_only_never_mainlined` | no | names a factor-two coarse step but supplies no current attached theorem |
| Block226 in-flight parent | `bounded_theorem`, current surface `conditional-support` | partially | its exact open co-scaled route is closed only on a fixed carrier |
| Block224 campaign boundary | local checkpoint, no authority/audit status | no | keeps renormalized changing-carrier comparison open |

No row is imported as retained authority.  The theorem is a branch proposal
requiring independent audit.

## Review and landing conditions

This proposal is stacked directly on Block226 commit `205db872e6`.  Block226
and every declared upstream stack dependency must land first, or a reviewer
must re-establish the cumulative delta from refreshed `origin/main`; this note
must never merge out of order.  The independent helper is packet-reachable by
the primary runner's static import and `AUDIT_INPUT_PATHS`.  A fresh canonical
runner cache, a refreshed citation-graph manifest containing exactly the two
declared internal dependencies, and exact staged-byte review are hard landing
conditions.  No generated audit surface other than that manifest belongs in
the science delta.

## Runner certificate

The primary SymPy runner reconstructs (2) by expanding the actual `f_n`
action, normalized Haar factor, and normalized character after the radial
Gaussian rescaling; radial moments are generated by the exact
three-dimensional Gaussian recurrence and applied algebraically.  It derives (4)--
(5), the scalar channel defect, the symmetric free-word BCH coefficients, the
determinant scaling, the ordered Haar/projector identities, the spin-one-
matched spin-two cylindrical defect, and both plaquette witnesses.

The independent checker uses only `Fraction`, integer polynomial/series
arithmetic, a separate free-word exponential/logarithm implementation, exact
`Z_2` product enumeration, and exact `a+b sqrt(2)` pairs.  Its fixed `n`
samples cross-check rather
than replace the primary all-`n` proof.  Every check family has a dedicated
hostile mutation that changes its load-bearing input or formula.  No executable
uses fitted data, floating arithmetic, or float-to-exact reconstruction.

## Exact strongest remaining obligation

For changing spatial carriers, construct the renormalized compression

```text
T_eff,j = J_j^* T_(j+1) J_j
```

with explicit disintegration, coefficient and measure flow, common-projector
compatibility, and an error estimate against a disclosed coarse action.  Then
control the limit uniformly over an indexed graph family and supply any
physical time/spacing interpretation separately.  The fixed-carrier theorem
(10) and bare defects (18)--(21) do not supply that object.

No claim in this note is a framework axiom, primitive, audit verdict, or
authority-state mutation.
