# Block 06 — V1-V5 Variants

**Target:** `universal_gr_tensor_action_blocker_note`
**Date:** 2026-05-17
**Constraint:** Each variant must NOT be a one-step relabeling of
- iter28 (`universal_gr_casimir_block_localization_note` — works the algebraic 4-block Casimir split on `Sym^2(R^4)`)
- iter13 (`universal_gr_block_constraint_interpretation_note` — splits algebraic block-split half from GR-canonical labeling half)

## Diagnosis of the blocker

The target note `UNIVERSAL_GR_TENSOR_ACTION_BLOCKER_NOTE` is `audited_conditional`
because:

- it makes an inventory claim ("no retained-grade object on the current branch
  identifies the scalar-generator Hessian with full Einstein/Regge metric
  dynamics") with no cited authorities and no machine-checkable inventory
  proof;
- it imports several "exact" objects (scalar generator, kinematic lift,
  tensor variational candidate, A1 projector) without authority edges;
- the runner `frontier_universal_gr_tensor_action_blocker.py` is text-grep,
  not an algebraic check, so the blocker statement is not anchored in
  exact-precision computation.

The auditor's stated re-audit path (verbatim from ledger):
> missing_dependency_edge — add direct cited authorities for the imported
> exact objects and a machine-checkable or note-level retained inventory
> showing that no supplied tensor-localization primitive identifies the
> Hessian with Einstein/Regge dynamics.

So the target is fixable in either of two structural directions:
- (D-A) sharpen the inventory CLAIM SCOPE so it is a bounded statement
  whose load-bearing step is class-A algebraic (the "small claim becomes
  exact theorem" closure pattern); or
- (D-B) prove a NO-GO theorem that establishes, from A_min only, why no
  retained-grade tensor-localization primitive of a specified class can
  identify the Hessian with Einstein/Regge dynamics (the "blocker becomes
  named obstruction" closure pattern).

## V1 — Localization-class no-go theorem on Sym^2(R^4)

**Idea.** Prove an exact algebraic no-go: for every linear projector
`Pi: Sym^2(R^4) -> Sym^2(R^4)` that is SO(3)-equivariant (commutes with
the spatial-block rho(R)h = R^T h R) AND has the rank-2 invariant `Pi_A1`
as a sub-projector, the image `Pi(Sym^2(R^4))` cannot simultaneously
- (i) be 6-dimensional (the canonical Einstein-tensor degree count
      Sym^2(R^4) - {1 lapse + 3 shift constraints} = 6) and
- (ii) be a single SO(3) irrep.

This is a pure rep-theory no-go: it says no linear SO(3)-equivariant
projector class can yield a canonical curvature-localization map within
the retained Casimir split, because the rank-6 image always decomposes
into multiple irreps that the spatial Casimir splits non-trivially.

**Strength:** Class-A algebraic theorem on `Sym^2(R^4)`. Pure no-go.
**Weakness:** Restricts the localization class to "linear SO(3)-equivariant
projector containing Pi_A1". A nonlinear or non-projector localization map
could in principle escape. But it sharpens the blocker into a named class.
**Differentiation from iter13/iter28:** iter28 proved positive existence
and ranks of the 4-block split (lapse=1, shift=3, trace=1, shear=5);
iter13 was about renaming-vs-derivation; V1 proves NO single rank-6
SO(3)-irrep image projector exists. This is a no-go on the *quotient*
side, not on the algebraic split side.

## V2 — Sharpened blocker note (claim restructure to bounded inventory)

**Idea.** Restructure the target note from an open-gate inventory-claim
into a bounded inventory theorem: list the seven retained UNIVERSAL_GR
authorities on the current branch (lambda_bypass, block_normalization,
supermetric_normal_form, bd_congruence_invariance, polarization_frame_bundle_blocker,
so3_isotypic_orbit_flat, lorentzian_global_atlas_closure) and certify, by
note-hash inspection, that each of their effective_status="retained"
claim scopes is BOUNDED to (a) algebraic block decomposition or
(b) frame-bundle ORBIT-FLATNESS without a SECTION. The bounded claim
becomes: "by structural inspection of seven cited retained sources,
the retained universal_gr lane's union claim scope is closed under
block algebra and orbit invariants but does not include
Einstein/Regge Hessian-identification."

**Strength:** Honest scope-restriction. Pure note-level cert with
runner-verifiable note-hash table.
**Weakness:** Doesn't close anything new — just makes the open-gate
inventory bounded and auditable. Closes audited_conditional via the
"sharpen to bounded" pattern.
**Differentiation:** Neither iter13 nor iter28 did this. iter28 was a
positive existence theorem; iter13 was about labeling. V2 is a
note-level inventory certificate.

## V3 — Derive a tensor action via direct lift (positive closure attempt)

**Idea.** Attempt to derive the Einstein/Regge action from A_min alone
by (a) projecting the Hessian into the canonical 4-block decomposition
(retained), (b) reading off the block coefficients on the isotropic
diag(a,b,b,b) background (retained Schur localization), (c) computing
the action's variation in each block, and (d) checking whether the
variation matches the Einstein constraint structure (lapse stationarity
gives Hamiltonian constraint, shift stationarity gives momentum
constraint).

**Strength:** If it works, positive closure.
**Weakness:** Past iterations (constraint_action_stationarity_note,
canonical_projector_connection_note) already explored this and found
the SO(3) complement-frame ambiguity. The orbit-flatness no-go
(so3_isotypic_orbit_flat) tells us no quadratic SO(3)-equivariant
energy functional can canonically section the complement. So V3 is
likely to fail.
**Differentiation:** Different from iter13/iter28 because it would
work in the action variational layer, not the algebraic split layer.

## V4 — Cross-confirmation of the polarization-frame-bundle no-go from a tensor-action angle

**Idea.** The retained `universal_gr_polarization_frame_bundle_blocker_note`
already establishes that the localized channel coefficients move under
frame rotation. Cross-confirm this from the tensor-action angle: prove
that for any choice of "candidate tensor action" S[h] that is (a) quadratic
in h, (b) SO(3)-equivariant, (c) built from the Hessian D^2 W[g*], the
variation delta S / delta h_(perp) does NOT vanish in a frame-invariant
way. I.e. the Euler-Lagrange equations have frame-dependent solution sets
when restricted to the complement. This gives a second-route confirmation
of the polarization-frame bundle no-go from the action-variation side.

**Strength:** Cross-confirms two retained results from a third
independent angle. Class-A algebraic if framed on quadratic action
class.
**Weakness:** It's essentially a reformulation of the orbit-flatness
result (so3_isotypic_orbit_flat) in EL-equation language. Risk: it's
too close to a one-step variant of that retained narrow theorem.
**Differentiation:** Different angle from iter13/iter28 but possibly
too close to existing retained universal_gr narrow theorem.

## V5 — Tensor-action class taxonomy theorem

**Idea.** Define three explicit classes of candidate "tensor actions" on
the universal-GR route:
- Class I: quadratic in h, built from D^2 W[g*] and SO(3)-equivariant
  linear projectors on Sym^2(R^4) (Casimir-equivariant);
- Class II: quadratic in h, built from D^2 W[g*] plus an arbitrary
  SO(3)-equivariant scalar combination of Pi_lapse, Pi_shift, Pi_trace,
  Pi_shear with real coefficients (alpha, beta, gamma, delta);
- Class III: arbitrary quadratic SO(3)-equivariant functional on
  Sym^2(R^4) (the orbit-flat no-go class from so3_isotypic_orbit_flat).

Prove:
- (T1) Class I = Class II as variational classes (any Class II can be
  realized as a single Class I projector linear combination);
- (T2) Class II is, up to a real four-parameter family, the maximal
  Casimir-equivariant linear action class on Sym^2(R^4);
- (T3) The Einstein-Hilbert action restricted to the linearized
  symmetric metric perturbation lies in Class II IF AND ONLY IF
  (alpha, beta, gamma, delta) satisfies a specific linear constraint
  derived from the linearized Einstein operator;
- (T4) But Class II is orbit-flat in the sense of
  so3_isotypic_orbit_flat (already retained), so no Class II action
  can canonically select a complement section.

The result: NO Class II tensor action can be the Einstein-Hilbert
action AND canonically select a complement section. This is a sharp
named obstruction for the entire linear-Casimir-equivariant tensor
action class.

**Strength:** Class-A theorem on a well-defined and exhaustive class.
Combines four retained authorities (casimir_block, so3_isotypic, A1
invariant section, block_normalization) into a single sharp no-go.
**Weakness:** Need to verify exhaustiveness of Class II via
representation theory (Schur's lemma on Casimir-equivariant operators).
**Differentiation:** A genuinely new structural theorem at the action
class level, not at the algebraic split level (iter28) and not at
the labeling level (iter13). Combines retained authorities into a
named obstruction that closes the audit-stated re-audit gap.

## Selection

V5 is the strongest because:
1. It is the only variant that produces a class-A NEGATIVE theorem at
   the action layer (closing the blocker as a SHARPENED named
   obstruction rather than a vague inventory statement);
2. It cites multiple retained authorities (casimir_block_localization,
   so3_isotypic_orbit_flat, A1_invariant_section, block_normalization),
   so it directly addresses the audit-stated re-audit path
   "missing_dependency_edge: add direct cited authorities";
3. It supplies machine-checkable algebra (the four-parameter linear
   combinations on Sym^2(R^4) with their projector ranks are exact
   over Q);
4. It is differentiated from iter13 (renaming vs derivation) and iter28
   (algebraic 4-block existence) by working at the tensor-ACTION class
   layer, defining and exhausting the linear Casimir-equivariant action
   class.

V1 has the same flavor but is narrower (one-projector image instead of
the full four-parameter action class). V5 subsumes V1 as a special
case.

V2 is a fallback if V5's exhaustiveness step turns out to require
non-A_min input.

V3 is unlikely to close anything new.
V4 is too close to so3_isotypic_orbit_flat.

**Selected:** V5.
