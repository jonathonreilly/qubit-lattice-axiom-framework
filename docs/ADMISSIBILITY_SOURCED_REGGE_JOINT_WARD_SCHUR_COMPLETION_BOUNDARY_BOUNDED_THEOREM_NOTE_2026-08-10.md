---
claim_id: admissibility_sourced_regge_joint_ward_schur_completion_boundary_bounded_theorem_note_2026-08-10
claim_type: bounded_theorem
claim_scope: "For the three full-rank six-dimensional O(source) physical mass matrices reconstructed by the sourced-Regge flat-gauge quotient calculation, a pure Schur cancellation M=B C^{-1} B^dagger with invertible Hermitian C needs at least six auxiliary directions on each branch, with C carrying at least the negative and positive inertia of M; the spectral construction attains this bound. A single fixed nonsingular C capable of serving all three retained source tangents needs at least four negative and four positive directions, and an explicit eight-direction construction attains that common bound. If the full mixed block is analytic in the signed source coordinate, source-decoupled at zero, and C(0) is invertible, its Schur correction begins at O(source^2) and cannot cancel the nonzero O(source) mass coefficient. The explicit analytic coefficient-level completion instead scales both mixed and auxiliary blocks as O(source), so the auxiliary block has a zero-source rank jump. These are finite-dimensional algebraic and double-precision reconstructed-matrix statements, not a local carrier, common source law, physical auxiliary sector, continuous-momentum theorem, Lorentzian stability theorem, gravity no-go, axiom necessity result, or axiom adoption."
upstream_dependencies:
  - minimal_axioms
  - admissibility_sourced_regge_flat_gauge_quotient_ward_completion_boundary_bounded_theorem_note_2026-08-10
  - admissibility_cut_surface_coframe_stress_higher_form_ward_geometry_dynamics_boundary_bounded_theorem_note_2026-08-10
  - admissibility_closed_helical_defect_history_ward_neutral_ir_regge_response_boundary_bounded_theorem_note_2026-08-10
runner: scripts/admissibility_sourced_regge_joint_ward_schur_completion_boundary_2026_08_10.py
---

# Sourced Regge Joint Ward-Schur Completion Boundary

**Date:** 2026-08-10
**Type:** `bounded_theorem`
**Role:** turn Block 22's unwanted `O(source)` gravity mass into a minimum
joint-sector and coupling-order classification.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[admissibility_sourced_regge_joint_ward_schur_completion_boundary_2026_08_10.py](../scripts/admissibility_sourced_regge_joint_ward_schur_completion_boundary_2026_08_10.py)

**Retained dependency surface:**
[minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[Block 22 sourced flat-gauge quotient](ADMISSIBILITY_SOURCED_REGGE_FLAT_GAUGE_QUOTIENT_WARD_COMPLETION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md),
[the cut-coframe Ward/seagull carrier](ADMISSIBILITY_CUT_SURFACE_COFRAME_STRESS_HIGHER_FORM_WARD_GEOMETRY_DYNAMICS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md), and
[the closed-line Regge Ward carrier](ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md).

## 1. Result Up Front

Block 22 located the sourced-gravity failure at its leading infrared order.
On the six flat physical Regge modes, the three retained stationary source
tangents produce full-rank Hermitian mass coefficients

    M_two-stream, M_A, M_B,                                      (1)

with inertias `3-/3+`, `4-/2+`, and `2-/4+`. They multiply the signed source
coupling `c`, while the desired flat graviton operator begins at `O(k^2)`.

This note tests the narrowest auxiliary/constraint repair: enlarge the
coefficient Hessian by a mixed block `B` and an invertible Hermitian source or
constraint block `C`, then demand the pure Schur identity

    M - B C^{-1} B^dagger = 0.                                 (2)

There are three exact algebraic conclusions conditional on the reconstructed
matrices:

1. `rank(B) >= 6`, so at least six auxiliary directions are necessary for
   each individual branch. Six suffice.
2. One fixed nonsingular signature capable of serving all three branches
   needs at least `4-/4+`, hence at least **eight** directions. Eight suffice.
3. A regular analytic source-decoupled completion with `B(0)=0` and invertible
   `C(0)` contributes only at `O(c^2)`. It cannot cancel a nonzero `c M` term.

The explicit analytic completion escapes the third statement by scaling the
whole auxiliary coefficient block with `c`. It therefore has `p=q=1` in the
order notation of Section 5 and a source-zero **rank jump**. Algebra restores
a six-dimensional kernel, but it does not tell Nature to introduce eight
zero-stiffness auxiliary directions, does not decide whether they are gauge,
constraints, or propagating fields, and does not supply their local law.

That is the science gain. A routine regular auxiliary sector cannot fix the
Block 22 mass term. A physical repair must use at least one of the routes now
made explicit: a direct Ward/contact term in the geometry block, a singular
constraint sector, a square-root coupling coordinate, or nonzero flat
isotropic mixing. The first is the strongest live route because the retained
cut-coframe family already demonstrates same-family seagull structure.

## 2. Reconstructed Six-Mode Input

The runner repeats only Block 22's zero-source tangent calculation. It builds
the exact five-normal flat Hessian, solves each retained source tangent, forms
the flat gauge complement, isolates the six zero-mass physical modes, and
differentiates the complete Regge-plus-deficit-square kernel by step-halved
centered differences.

The resulting spectra are:

| source tangent | eigenvalues of `M_s` | inertia | gap |
|---|---|---:|---:|
| two-stream | `-0.14492085, -0.06960660, -0.02774481, 0.05695435, 0.10929393, 0.15489269` | `3-/3+` | `0.02774481...` |
| Bundle A | `-1.08476030, -0.40892304, -0.35817584, -0.14017315, 0.35228002, 0.52317444` | `4-/2+` | `0.14017315...` |
| Bundle B | `-0.38068367, -0.27251828, 0.04034727, 0.15236853, 0.34247085, 0.67698266` | `2-/4+` | `0.04034727...` |

The three matrices are linearly independent as real Hermitian vectors. The
singular values of their three-row vectorization are

    1.64335132, 0.23395416, 0.14055521.                       (3)

Thus one source-blind fixed correction cannot cancel all three. A common law
must let its mixed block, auxiliary block, or direct geometry contact term
respond to source direction.

The spectra and (3) are double-precision reconstructed facts. The linear
algebra below is exact for any nonsingular Hermitian matrices with those
inertias.

## 3. Per-Branch Minimum

### Proposition 1 — rank and signature lower bounds

Let `M` be a nonsingular Hermitian `6 x 6` matrix. Suppose an invertible
Hermitian `r x r` matrix `C` and a `6 x r` matrix `B` obey (2). Then

    r >= rank(B) >= rank(M) = 6,                               (4)

and

    n_-(C) >= n_-(M),       n_+(C) >= n_+(M).                 (5)

**Proof.** Rank submultiplicativity gives (4). Equation (2) represents `M` as
the pullback by `B^dagger` of the nondegenerate Hermitian form `C^{-1}`.
The positive and negative indices of a restriction cannot exceed those of
the ambient form. Since inversion preserves inertia, (5) follows. `QED`.

### Proposition 2 — the lower bound is attained

Write the spectral decomposition

    M = V Lambda V^dagger.                                    (6)

Define

    B = V |Lambda|^{1/2},       C = sign(Lambda).              (7)

Then `C^{-1}=C`, (2) holds, and `C` has exactly the inertia of `M`. The joint
coefficient Hessian

    H_joint = [[M, B], [B^dagger, C]]                          (8)

has the six-dimensional graph kernel

    R = [I_6; -C^{-1} B^dagger],                               (9)

and is congruent to `diag(0_6,C)`. Its inertia is therefore
`(n_-(M),n_+(M),6-zero)`.

The runner constructs (7) for all three source tangents. The largest
factorization, Schur, spectral, and kernel residual is below `2e-13`.

This is a coefficient-level theorem. The negative directions of `C` are a
signature budget, not automatically Lorentzian ghosts: that interpretation
depends on whether these variables are propagating, constrained, or pure
multipliers and on their kinetic operator, none of which is supplied here.

## 4. One Fixed Signature For All Three Sources

Suppose a single nonsingular auxiliary form `C_*` must be capable of
representing each `M_s`, while the mixed matrix `B_s` may depend on source
direction:

    M_s = B_s C_*^{-1} B_s^dagger.                             (10)

The Bundle-A matrix requires at least four negative directions in `C_*`.
The Bundle-B matrix requires at least four positive directions. Hence

    dim C_* >= 4 + 4 = 8.                                     (11)

This lower bound is attained by

    C_* = diag(-I_4,+I_4).                                    (12)

For each source, place the negative eigenvectors of `M_s`, weighted by the
square roots of their absolute eigenvalues, into the first four columns of
`B_s`; place the positive eigenvectors into the last four. Then (10) holds.
Each `14 x 14` joint matrix has inertia `4-/4+/6-zero` and the same graph
kernel (9).

Consequently there are two sharply different six-versus-eight options inside
the pure Schur class:

- six directions suffice branch by branch, but their required signatures
  change from `3-/3+` to `4-/2+` to `2-/4+`; a continuous nonsingular
  six-direction `C(J)` cannot change between those inertias without crossing
  a singular wall;
- eight directions with fixed `4-/4+` signature can serve all three, but the
  source-dependent `B_s` still requires a selected transformation/coupling
  law.

This is not a claim that a physical law needs eight new particles. Direct
geometry terms, flat mixing, gauge multipliers, or non-Schur mechanisms evade
the hypothesis.

## 5. Coupling-Order Boundary

Let the full geometry block on one source ray be

    A(c) = c M + O(c^2).                                      (13)

Assume a signed-coupling analytic auxiliary family which is decoupled at the
flat point and regular there:

    B(c) = c B_1 + O(c^2),       B(0)=0,
    C(c) = C_0 + O(c),           C(0)=C_0 invertible.          (14)

Then

    C(c)^{-1} = C_0^{-1} + O(c),
    B(c) C(c)^{-1} B(c)^dagger
      = c^2 B_1 C_0^{-1} B_1^dagger + O(c^3),                 (15)

so

    S(c) = A(c)-B(c)C(c)^{-1}B(c)^dagger
         = c M + O(c^2).                                     (16)

### Proposition 3 — regular analytic Schur non-cancellation

Under (13)--(14), a nonzero `M` cannot be canceled at first order by the
Schur term. Equivalently, `S'(0)=M`.

This is only a theorem about the regular, source-decoupled, invertible-`C(0)`
pure Schur route. It is not a gravity no-go.

More generally, if `B(c)=O(c^p)` and `C(c)=O(c^q)` on an invertible scaled
block, the Schur correction has order `O(c^{2p-q})`. Matching (13) requires

    2p-q=1.                                                    (17)

The live order-balanced routes are:

| route | exponents/mechanism | exact cost or open issue |
|---|---|---|
| analytic singular coefficient block | `p=q=1`; use `c H_joint` from (8) or its eight-mode version | works algebraically, but `C_full(0)=0`; all auxiliary stiffness vanishes and the rank jumps |
| square-root mixing | `p=1/2,q=0` | regular `C(0)`, but nonanalytic in signed `c`; it may be analytic only after deriving a physical amplitude `a` with `c=a^2` |
| direct Ward/contact term | add `-cM` directly to `A(c)` | no auxiliary rank cost; requires the selected joint action and differentiated Ward/seagull law |
| flat isotropic mixing | allow `B(0)=B_0 != 0` with `B_0 C_0^{-1}B_0^dagger=0`, then use cross terms at `O(c)` | possible only with an indefinite form and a derived flat coupling; excluded by (14), not tested physically |
| singular constraint/pseudoinverse | let `C(0)` be singular outside the ordinary Schur hypothesis | may encode gauge multipliers; requires a constraint-rank and locality theorem |

The explicit completion in Sections 3--4 occupies the first row, not the
regular analytic route. That distinction prevents a merely formal matrix
factorization from masquerading as a completed physical source law.

## 6. Ward Identity And Physical Boundary

For a joint invariant action with coordinates `z^a` and generator `R^a(z)`,

    S_a R^a = 0.                                               (18)

Differentiation gives

    H_{ba} R^a + S_a partial_b R^a = 0.                        (19)

At a full stationary solution the second term vanishes. On a partially
stationary external-source representative it need not. Block 22's inherited
flat projector supplies neither `partial_b R^a` nor the mixed/source Hessian
blocks. Equations (2) and (8) show one stationary algebraic cancellation, but
they do not derive the **connection term** in (19), the source transformation,
or the local generator.

Two retained artifacts make the constructive alternative concrete without
closing it here:

- the closed-line Regge carrier has an exact action-level telescoping Ward
  identity for a prescribed source;
- the cut-coframe family has a nonzero same-family coframe seagull in its
  second response.

Those carriers prove that direct Ward/contact structure is not an empty
phrase. They do not prove that their variables or coefficients are the ones
needed by the sourced Regge branch.

Locality remains open. Analytic coupling, source selection, constraint role,
causal signature, continuous momentum, the full nonuniform solution, and
nonlinear Lorentzian stability all remain open.

## 7. Candidate Geometry/Source Law Interface (Unadopted)

The minimum interface sharpened by this result is:

> A realized geometry/history law selects a local joint geometry, source,
> and constraint action, its action unit and geometry-dependent additive
> normalization; the physical source coordinate, its zero-source rank, and
> its analytic scaling; the transformation law and role of every auxiliary
> variable; and a full coupled stationary background. Its differentiated
> Ward identity
> supplies either a direct first-order geometry contact/connection term or a
> law-derived singular/flat-mixed constraint mechanism that cancels or
> physically reinterprets the sourced `O(k^0)` mass coefficient. A selected
> massless phase begins at `O(k^2)` on its physical quotient with no unintended
> modes; a selected massive or curved phase derives its scale and stability
> from the same law. The same variables admit a local Lorentzian nonlinear
> evolution.

This is sufficient or target-equivalent wording, not a proven necessary or
minimal axiom. It may be derived as a downstream law. **No canonical axiom is
edited** by this block.

## 8. No-Go Discipline Gate

The only bounded negative eligible to ship is:

> For the three named reconstructed full-rank six-mode source mass matrices,
> a pure Schur representation with invertible Hermitian auxiliary block needs
> at least six directions per branch and at least eight for one fixed
> signature serving all three. Within the narrower regular signed-coupling
> analytic class with `B(0)=0` and invertible `C(0)`, the Schur correction
> begins at `O(c^2)` and cannot cancel the nonzero `O(c)` coefficient.

This is not a gravity no-go, an action-family no-go, or an axiom-necessity
claim.

### N1 — Alternative route enumeration

| normalized route | attempted calculation | outcome | marker |
|---|---|---|---|
| per-branch spectral Schur completion | factor each `M_s` as `V|Lambda|V^dagger` with `C=sign Lambda` | succeeds with six directions and proves the rank/signature minimum | `ATTEMPTED` |
| common fixed-signature completion | embed all three spectra into `C_*=diag(-I_4,+I_4)` | succeeds with eight directions; inertia bounds prove seven cannot serve all three | `ATTEMPTED` |
| source-blind fixed correction | test whether one matrix correction can equal all three `M_s` | rejected because the three matrices are linearly independent with minimum family singular value `0.140555...` | `ATTEMPTED` |
| regular analytic decoupled Schur block | expand analytic `B(c)` with `B(0)=0` and invertible `C(0)` | correction starts at `O(c^2)` and misses the `O(c)` coefficient | `ATTEMPTED` |
| analytic singular coefficient block | scale both `B` and `C` as `O(c)` | cancels exactly, but produces a zero-source auxiliary rank jump | `ATTEMPTED` |
| square-root mixed block | solve the exponent balance with `p=1/2,q=0` | matches `O(c)` but is nonanalytic in signed `c`; remains live if a derived amplitude squares to `c` | `ATTEMPTED` |
| continuous six-direction signature | compare the three necessary `C_s` inertias along connected source directions | they cannot change inertia without a singular crossing; fixed `4-/4+` eight-mode embedding avoids it | `ATTEMPTED` |

The direct Ward/contact route and flat isotropic mixing are not counted as
failed. They are the strongest open mechanisms in N7.

### N2 — Wall-independence audit

The raw rank, signature, source direction, coupling order, locality, and
dynamics conditions collapse to four independent walls:

- `W1`: pure Schur form with finite-dimensional invertible Hermitian `C`;
- `W2`: regular signed-coupling analyticity with `B(0)=0` and invertible
  `C(0)`;
- `W3`: the three double-precision reconstructed homogeneous source tangents;
- `W4`: coefficient-level Euclidean algebra rather than a local Lorentzian
  nonlinear action.

| pair | closing first closes second? | closing second closes first? | independent? |
|---|---|---|---|
| `W1,W2` | no | no | yes |
| `W1,W3` | no | no | yes |
| `W1,W4` | no | no | yes |
| `W2,W3` | no | no | yes |
| `W2,W4` | no | no | yes |
| `W3,W4` | no | no | yes |

For example, a direct contact term leaves the pure Schur class without solving
local dynamics; interval-certifying `M_s` would not select a coupling law; and
a Lorentzian theory need not use a regular decoupled auxiliary block.

### N3 — Hidden-wall scan

| phrase/hit | classification | disposition |
|---|---|---|
| “minimum” | hidden class qualifier | always restricted to invertible-Hermitian pure Schur completion, per branch or common fixed signature as stated |
| “joint Ward” | hidden physical-law implication | only a graph kernel of the coefficient Hessian is proved; locality and `R(z)` remain `W4` |
| “source modes” | hidden particle interpretation | called auxiliary directions; propagation and constraint role are unselected |
| “analytic” | hidden coordinate choice | restricted to the signed coupling `c`; the amplitude-square escape is explicit |
| “all three” | hidden source-universality | only the three retained tangent matrices in `W3` |
| “signature” | hidden ghost claim | matrix inertia only; no Lorentzian kinetic interpretation |
| “rank jump” | possible universalizer | only the explicit `p=q=1` construction, not every repair |
| “axiom” | governance inflation | no necessity is claimed; the wording in Section 7 is unadopted and may be downstream |

### N4 — Residual matching

| path:line and cited fact | residual claimed here | match? |
|---|---|---:|
| `ADMISSIBILITY_SOURCED_REGGE_FLAT_GAUGE_QUOTIENT_WARD_COMPLETION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md:52` — three `O(c)` mass matrices | matrices reconstructed here | yes |
| `ADMISSIBILITY_SOURCED_REGGE_FLAT_GAUGE_QUOTIENT_WARD_COMPLETION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md:185` — differentiated joint Ward identity | missing connection/source blocks motivating Sections 5--6 | yes |
| `ADMISSIBILITY_CUT_SURFACE_COFRAME_STRESS_HIGHER_FORM_WARD_GEOMETRY_DYNAMICS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md:115` — connected plus same-family seagull response | concrete direct-contact steelman only | yes |
| `ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md:150` — exact prescribed-source Regge Ward identity | evidence that a source-compatible Ward carrier can exist, not this completion | yes |
| `MINIMAL_AXIOMS_2026-06-29.md:117` and `:183` — admissibility is not dynamics; source/action identification is open | reason no completion is promoted to axiom-selected physics | yes |
| Block 22 finite-path crossings | pure Schur coefficient minimum | no; not cited as proof of the new rank theorem |
| Block 21 fixed-normal no-overlap | joint completion boundary | no; deliberately excluded |

All nonmatching prior negatives are dropped from the proof count.

### N5 — Resolution-class execution

| resolution | executed evidence |
|---|---|
| per element | every entry of each reconstructed `6 x 6` `M_s`, each minimal `C_s`, and fixed `8 x 8` `C_*` enters the factorization |
| per site | checked and not executed: no new local site carrier or incidence law is constructed |
| per mode | the `k=0` `O(c)` coefficient on all six flat physical modes is checked; no nonzero-momentum completion is claimed |
| per block | all three source tangents, their individual minima, one common signature, graph kernels, and coupling orders are checked |
| lattice wide | checked and not executed: this is not a nonuniform local action, continuous-zone, finite-torus, Lorentzian, or nonlinear theorem |

The cached stdout carries these five resolution lines and the same boundary.

### N6 — Partial closure and premise scan

| existing surface | status and contribution | what remains open |
|---|---|---|
| minimal axioms | approved premise surface; explicitly leaves dynamics and source/action identification open | selects no `B`, `C`, auxiliary role, or coupling coordinate |
| Block 22 | bounded theorem; supplies the three `M_s` and exact target residual | supplies no joint local source law |
| closed-line Regge Ward carrier | retained bounded construction for a prescribed compatible source | does not generate the Block 22 stationary branch or its connection |
| cut-coframe seagull carrier | retained exact response identity in a different finite family | does not fix Regge variables, coefficient, or physical selection |
| Section 4 eight-mode completion | exact coefficient-level existence theorem | no locality, analytic background family, or dynamics |

No convention or label change supplies the missing action. No approved
primitive is treated as a wall, and no proposed primitive is given premise
weight. This block does not assert that no retained primitive supplies a
repair, does not assert primitive exhaustion, and does not require an axiom
edit.

### N7 — Actionable steelman

The strongest hostile response is convincing: Schur completion may be the
wrong physical language. A selected joint source/geometry action can add a
direct `O(c)` contact or seagull term to the geometry Hessian through the
source transformation and `S_a partial_b R^a` connection term in (19). That
route needs no eight-direction auxiliary signature and evades Proposition 3
because it changes `A(c)` itself. The retained cut-coframe response proves
that same-family seagulls occur in an explicit local probability family.

The actionable test is to build the full nonuniform Regge/source action,
derive `R_*(ell,J,lambda)`, solve the joint stationary equations, and compute
the complete second variation including the direct contact, mixed, source,
multiplier, and connection terms. If its physical Schur/constraint quotient
starts at `O(k^2)` with the target inertia, the bounded negative here is
retired. If it uses a singular block, its rank change must be identified as
gauge or constraint structure rather than silently introduced.

### N8 — Cross-cycle echo

| earlier boundary | later mechanism | lesson applied here |
|---|---|---|
| Block 19 fixed affine normal inertia | Block 20 changed the action and repaired the flat full quotient | do not mistake one reduced surface for gravity |
| Block 21 fixed-normal coefficient no-overlap | Block 22's momentum-dependent quotient escapes both witnesses | execute a live structural alternative before broadening a negative |
| Block 22 inherited flat quotient has `O(c)` mass | this block constructs exact algebraic cancellations and exposes their rank/scaling cost | replace “missing Ward law” with testable options |
| finite inventories can miss the infrared | Block 22's analytic order comparison found the hidden chamber | coupling-order analysis is required alongside finite spectra |
| source Ward/contact terms existed in other carriers | closed-line and cut-coframe constructions provide them | test transfer through a derived common action; do not assume it |

**N1--N8 status: `PASS` only** for the stated six-mode invertible-Hermitian
pure Schur minima and the regular analytic source-decoupled order boundary.

## 9. Promotion Value And Cluster Gate

| gate | evidence |
|---|---|
| V1 — exact obstruction | Block 22 names a nonzero first-order mass term and asks for joint Ward/source structure |
| V2 — new derivation | per-branch six-mode minimum, common eight-mode minimum, source-family linear independence, and coupling-order theorem are new |
| V3 — generic machinery | Schur/inertia algebra is generic, but the `6` and common `4-/4+` budget come from the three reconstructed Regge source tangents |
| V4 — marginal content | ordinary regular auxiliary completion is eliminated; four concrete escape mechanisms replace an unspecified “connection” |
| V5 — independently reviewable | one runner reconstructs the matrices and checks every factorization, inertia, kernel, family-rank, and scaling control |

This is independently reviewable from Block 22. Block 22 localizes the
unwanted operator; this block quantifies what the narrowest joint-sector
repair must contain and why the regular analytic version is too high order.

## 10. Exact Next Obligation

1. Attempt the direct Ward/seagull route first: derive the local joint
   Regge/source action and its background-dependent generator.
2. Solve one full nonuniform coupled stationary background.
3. Compute the direct geometry contact, mixed, source, multiplier, and
   connection terms and test whether the physical `O(c)` coefficient cancels.
4. If the law uses a singular `p=q=1` constraint sector, identify the six- or
   eight-direction zero-source rank jump as derived gauge/constraint content
   and prove that it introduces no physical extra modes.
5. If the law uses an amplitude `a` with `c=a^2`, derive that coordinate and
   its sign/orientation law rather than inserting square-root mixing.
6. Only then certify continuous momentum and Lorentzian nonlinear stability.

The exact axiom issue is now conditional and explicit: the current axioms do
not select any of these mechanisms. Evidence does not yet show that an axiom
must be added; the required law may be derivable downstream. Fixed TOE
percentages therefore do not move.

## 11. Reproduction

Run:

```bash
python3 scripts/admissibility_sourced_regge_joint_ward_schur_completion_boundary_2026_08_10.py
```

The runner reconstructs the three Block 22 mass matrices, proves their
full-rank inertia data numerically, constructs every six-direction minimal
completion, constructs the common fixed-signature eight-direction completion,
checks all graph kernels, verifies source-family linear independence, and
tests the regular analytic Schur order. No external scientific inputs are
used.
