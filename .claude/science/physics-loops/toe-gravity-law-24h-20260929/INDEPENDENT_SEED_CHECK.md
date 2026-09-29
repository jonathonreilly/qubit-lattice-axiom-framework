# Focused independent seed check — curvature-member lapse bracket

Checked revision: `7146fe17a76de41badcaca3c3c7cac6d11eb2a00` (2026-09-29). This is a mathematical selective check before downstream reuse, **not a formal audit, full landing review, axiom decision or source-review PASS**. No science source was edited. The complete source notes and necessary original definitions listed below were read; their working bytes equal the pinned Git blobs. The primary runner was inspected only through family B to identify its convention, and was neither imported nor executed.

**Finding:** the local flat-strain coefficient identity, its kinetic-ratio obstruction, and the explicitly transferred two-wave source witness are correct within their supplied hypotheses. The displayed overall bracket sign requires a convention correction/clarification before reuse. Nonlinear closure remains genuinely unproved for this carrier.

## Independently derived core

Use the six independent canonical pairs `(h_jj,P_jj)` and `(h_ij,P_ij)`, `i<j`, with `{h_A,P_B}=delta_AB`. The full symmetric velocity contraction counts each shear twice. Thus `P_jj=2(alpha v_jj+beta tr v)/w` and `P_ij=4 alpha v_ij/w`; the per-tick Legendre dual is exactly

`T = [sum_j P_jj^2-c(sum_j P_jj)^2]/(4 alpha) + sum_(i<j) P_ij^2/(8 alpha)`, `c=beta/(alpha+3 beta)`.

The kinetic Hessian determinant is `512 alpha^5(alpha+3 beta)/w^6`. A full symmetric-matrix momentum convention instead needs the off-diagonal matrix entry `P_ij/2`; these pairings must not be mixed.

Write `D=sum_i Delta_i`, `r_j[N]=-DN+Delta_j N`, and `tr r[N]=-2 DN`. For a spatial constraint term `+sigma K R1[N]`, standard canonical antisymmetrization gives the diagonal momentum coefficient

`b_j(c)=sigma K/(2 alpha) {M Delta_j N-N Delta_j M +(2c-1)(M DN-N DM)}`.

At `c=1/2`, this is `sigma 2 D_j^- xi_j`, where

`xi_j(x)=K/(4 alpha)[N(x+e_j)M(x)-N(x)M(x+e_j)]`.

For face corners `00,10,01,11`, define `dN=N00-N10-N01+N11`. The independent shear coefficient is

`b_ij=sigma K/(2 alpha)[A[M] dN-A[N] dM]`.

Expanding the four-corner mean gives `sigma(D_i^+ xi_j+D_j^+ xi_i)`. Either opposite-corner mean changes `A` by `+/- d/4`, which cancels exactly in this antisymmetrization. These are polynomial identities for arbitrary lapse values, and hence hold on every periodic torus of side at least three, independently of finite samples. For `N10=M00=1`, other face values zero, one-corner timing gives `-sigma K/(2 alpha)` versus the required `-sigma K/(4 alpha)`. Its global face sum can also be nonzero, while every relabelling's global face sum vanishes.

The ratio residual is diagonal and affine in `2c-1`. With `N=delta_0`, `M=delta_e1`, the `c=0` minus `c=1/2` yy residual has values `sigma K/(2 alpha)` at 0 and its negative at e1. Its sum over each y,z slice is nonzero. Every `G_yy=2 D_y^- xi_y` has zero such slice sum. Therefore, for the stated nonsingular kinetic family, universal closure into any relabelling requires `c=1/2`, equivalently `beta=-alpha`. Individual lapse pairs can have zero obstruction; the necessity quantifies over all lapse pairs and momenta.

The three named timings are not a uniqueness theorem for all timings. The polynomial also closes for every fixed normalized local linear mean with weights `(a,1/2-a,1/2-a,a)`. The source correctly restricts its iff statement to the four prescriptions examined.

## Material sign finding and required resolution

The primary runner's `linear_bracket` uses `+K[{R1[N],T[M]}-{R1[M],T[N]}]`, which matches its displayed `xi`. Block62 supplies `F2=-K wbar(u R1+R2)`; Block101's action has **positive** `+K wbar(u R1+R2)`, hence its Hamiltonian spatial potential has **negative** sign. For the per-tick Hamiltonian constraint `C=T-K R1` and standard `{h,P}=+1`, the independently derived result is therefore **`{C[N],C[M]}_(h=0,P-linear)=-G[xi_displayed]`**. Reversing the bracket convention reverses this statement. The ratio and timing criteria survive either sign.

Before nonlinear reuse, freeze the explicit real-space `C[N]`, fundamental Poisson bracket, independent momentum pairing, and definition of `G`. If using the standard Hamiltonian convention, reverse the displayed bond field (or equivalently the identified relabelling orientation) and make the source/runner/constraint convention consistent. If intentionally using a reversed bracket convention, declare it and reconcile the generator's action. Merely negating both constraints does not fix the sign, because the bracket is bilinear. This is a convention defect/ambiguity, not a refutation of the `beta=-alpha` obstruction.

## Other independently checked statements and edge cases

For arbitrary real vector p, direct tensor-polynomial substitution proves `R1` and `R2` invariant under `h -> h+p p^T zeta`. The finite kinetic variation minus its boundary derivative is

`(alpha+beta)[2 p^2 tr(hdot) zetadot+p^4 zetadot^2]/wbar`.

At `beta=-alpha`, the source residual is `zeta[2 alpha e_ddot/(K wbar^2)+p.Theta.p/2]`, yielding T3's identity. This is only the gradient symmetry and a necessary source identity; it neither supplies arbitrary transverse time-dependent relabelling symmetry nor full continuity/momentum conservation.

The stationary two-wave witness independently factors into spin response and staggered-symbol contraction: both energy squares equal `2146/4225`, the difference symbol is `p=(-8,2,0)/sqrt(65)`, and `p.Theta_sym.p=128 sqrt(2146)(1-i)/65^4`, nonzero. The symmetric divergence has all three components nonzero. This checks the specified identity-transferred response; conserved bond stresses or different transfers remain open.

- `alpha+3 beta=0`: the trace Legendre direction is singular. T1's inverse is unavailable; additional canonical constraints require separate analysis. No exclusion theorem covers it.
- `beta=-alpha`: the full six-coordinate kinetic Hessian is nonsingular (`alpha+3 beta=-2 alpha`); the singularity of the reduced longitudinal elimination is a different issue.
- `p=0`: in the supplied T2–T4 quadratic mode action, the multiplier requires `e0=0`; no arbitrary positive-mean compact source is supplied. Symmetric-timing T1 has zero uniform output coefficient. No nonzero-mode inverse may be used at zero momentum.
- At canonical `P=0`, the checked linear-momentum bracket vanishes for every ratio. Homogeneous or proportional lapses can likewise give zero brackets. These do not weaken a universal coefficient theorem.
- `K>0`, `alpha>0`, `wbar>0`, periodic side at least three, and the declared staggering/timings remain hypotheses; `alpha=0`, `K=0`, other placements and smaller tori are outside this statement.

## Scope for the 24-hour follow-on

The strongest verified seed is an exact **flat-strain, P-linear coefficient identity**, conditional on the supplied stencil, up to the resolved sign convention. It is a necessary tangent-level condition for a completion that preserves this kinetic family and spatial linearization. It supplies no nonlinear `C`, field-dependent momentum constraint, structure functions, Jacobi/constraint-preservation proof, or `{G,C}` / `{G,G}` algebra. Terms `O(hP)` and, with field-dependent kinetic coefficients, `O(P^3)` can introduce new obstructions. The quadratic mode action does not determine a lapse-weighted nonlinear potential density.

A valid follow-on must first specify the admissible completion class, locality/support, full lapse placement, nonlinear kinetic and potential terms, shift generator and target identities; then prove them or find a counterexample. The missing full closure lemma is target-equivalent, not a routine consequence of T1. The source and its necessary parents explicitly leave this unresolved; this check is not an exhaustive novelty review of every repository lane.

All fields, lapse/face timing, K/alpha/beta, kinetic term, action, walker dynamics and stress transfer are separately supplied model conditions. The complete current minimal axioms and registry were checked: no approved primitive supplies these dynamics or closure. Scale reference gives units; kinetic isotropy gives the named structural matter kinetic-form ratio, with no established map to `K=4 alpha` here; realized state gives pointwise evaluation, with no supplied state or state-selection law. Nothing is adopted or registered.

## Commands and decisive evidence

Ran `git rev-parse HEAD`, exact working-byte comparisons to `git show <SHA>:<path>`, and:

```bash
python3 /Users/jonBridger/.codex/worktrees/toe-axiom-campaign-20260929/New Axioms Lets Go/.claude/science/physics-loops/toe-gravity-law-24h-20260929/seed-check-evidence/check.py > /Users/jonBridger/.codex/worktrees/toe-axiom-campaign-20260929/New Axioms Lets Go/.claude/science/physics-loops/toe-gravity-law-24h-20260929/seed-check-evidence/results.txt
```

Exit 0. Independent SymPy differentiation/inversion and coefficient expansions found zero residual for all three timings. An additional exhaustive bilinear-basis check on the 3^3 torus tested all 729 ordered delta-lapse pairs, **236,196 exact coefficient comparisons**. The trace slice witness was `[2,-2,0]` for `alpha=1,K=4`; the one-corner global xy-face sum was `-2`, versus relabelling sum 0. Exact generic-vector symmetry and witness assertions passed. No production runner output was used as proof; source and its primary family-B formulas were visible, so this is derivation/implementation independence, not a blind review.

[Independent calculation](/Users/jonBridger/.codex/worktrees/toe-axiom-campaign-20260929/New Axioms Lets Go/.claude/science/physics-loops/toe-gravity-law-24h-20260929/seed-check-evidence/check.py), SHA256 `bfe96a68cf26c39919e742229dea33692f2cf5f4b21d8920d93e08e5e4574ce6`.
[Full results](/Users/jonBridger/.codex/worktrees/toe-axiom-campaign-20260929/New Axioms Lets Go/.claude/science/physics-loops/toe-gravity-law-24h-20260929/seed-check-evidence/results.txt), SHA256 `ebeada9e81c0e0699f2eef249ba033c420b75dcef91ef11c09719e6bb8c39aa4`.

## Frozen mathematical source/input identities

Every source below is from the pinned revision; completeness refers to reading coverage, not a full review verdict.

| Read source/input | SHA256 |
| --- | --- |
| [Block112 complete source](</Users/jonBridger/.codex/worktrees/toe-axiom-campaign-20260929/New Axioms Lets Go/docs/ADMISSIBILITY_RULE_THE_CURVATURE_MEMBERS_CONSTRAINT_ALGEBRA_CLOSES_ON_THE_LATTICE_ONLY_AT_BETA_EQUALS_MINUS_ALPHA_AND_THERE_THE_WALKERS_OWN_STATES_CANNOT_BE_ITS_CONTENT_BOUNDED_THEOREM_NOTE_2026-09-24.md>) | `68c4ca6960b2d6c1a81ec8207064e0b4ca9f95df6451d0a22753b66fbe9983b8` |
| [Block60 complete source](</Users/jonBridger/.codex/worktrees/toe-axiom-campaign-20260929/New Axioms Lets Go/docs/ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md>) | `3a54bebf805d1722b225c1af9326fd610580ec2cbdcf9dad409aefad952b3f80` |
| [Block62 complete source](</Users/jonBridger/.codex/worktrees/toe-axiom-campaign-20260929/New Axioms Lets Go/docs/ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md>) | `0d631bc3e1ceaabca7f8bf37cfa8a463cb8ec4b97c512b14cccfc297790315f6` |
| [Block101 complete source](</Users/jonBridger/.codex/worktrees/toe-axiom-campaign-20260929/New Axioms Lets Go/docs/ADMISSIBILITY_RULE_IN_THE_CURVATURE_MEMBER_THE_CLOCK_IS_A_CONSTRAINT_A_BODYS_CHANGE_OF_ENERGY_ACTS_AT_ONCE_UNLESS_FORMATION_KEEPS_ENERGY_LOCAL_BOUNDED_THEOREM_NOTE_2026-09-23.md>) | `77d2bfd3a8c2eedc136e8db9953d4758084921a220ff9ebc0592884a0ba011f4` |
| [Current minimal axioms, complete](</Users/jonBridger/.codex/worktrees/toe-axiom-campaign-20260929/New Axioms Lets Go/docs/MINIMAL_AXIOMS_2026-06-29.md>) | `93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753` |
| [Primitive registry, complete](</Users/jonBridger/.codex/worktrees/toe-axiom-campaign-20260929/New Axioms Lets Go/docs/audit/data/axiom_premise_nodes.json>) | `615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37` |
| [Kinetic-isotropy primitive, complete](</Users/jonBridger/.codex/worktrees/toe-axiom-campaign-20260929/New Axioms Lets Go/docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md>) | `5516fb0bb8f50286b3c34d3f2668b1a2e347b9f7e257a8b5745f84f1093dd96b` |
| [Scale-reference primitive, complete](</Users/jonBridger/.codex/worktrees/toe-axiom-campaign-20260929/New Axioms Lets Go/docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md>) | `e7e75a36bd16094cbb547f6b215680ac45adc565c4cc93f05b0af17992eb9292` |
| [Realized-state primitive, complete](</Users/jonBridger/.codex/worktrees/toe-axiom-campaign-20260929/New Axioms Lets Go/docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md>) | `755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563` |
| [Primary runner: family B inspected only](</Users/jonBridger/.codex/worktrees/toe-axiom-campaign-20260929/New Axioms Lets Go/scripts/admissibility_rule_the_curvature_members_constraint_algebra_closes_only_at_beta_equals_minus_alpha_where_the_walker_cannot_be_its_content_2026_09_24.py>) | `bfc5d9317a627cc220e9036a9f87e1f4838fbaafce71e82a738cd7350bd55d31` |
