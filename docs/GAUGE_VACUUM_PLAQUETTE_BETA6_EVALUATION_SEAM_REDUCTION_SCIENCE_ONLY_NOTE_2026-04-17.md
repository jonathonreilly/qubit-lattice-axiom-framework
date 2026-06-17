# Gauge-Vacuum Plaquette Beta=6 Evaluation-Seam Reduction (Formal Algebraic Lemma)

**Date:** 2026-04-17 (original); 2026-05-27 (conditional-reduction
narrowing); 2026-05-28 (further narrowed to a purely formal
if-premises-then-algebra lemma per audit path (b)).
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome.
**Status:** purely formal finite-dimensional linear-algebra lemma —
GIVEN abstract operators `(S, η, ell_W)` on the class-sector space with the
stated abstract hypotheses, the coefficient relations `z` and `Z(W)`
follow by linear algebra, while normalized `ρ` statements are made only on
the explicit domain `z_(0,0) != 0`. The note makes **no claim** that these abstract
objects ARE the physical β=6 Wilson/Haar kernel/rim; that physical
identification depends on four unsupplied authorities and is explicitly
out of scope.
**Runner:** `scripts/frontier_gauge_vacuum_plaquette_first_three_sample_environment_evaluator_route_2026_04_17.py`

## 2026-05-28 Further narrowing (purely formal algebraic lemma)

The 2026-05-28 audit verdict on the prior (2026-05-27) conditional-reduction
form was still `audited_conditional`:

> *"The retained one-hop deps cover only the finite transfer witness
> packet and the finite structural-surface underdetermination no-go. The
> four authorities that make this an actual β=6 matrix-element reduction
> remain required-but-unsupplied retained inputs, so the row cannot be
> retained as closed."*

with the offered repair: re-audit after retained authorities exist for the
four Wilson/Haar identities, **OR narrow the note further to a purely formal
if-premises-then-algebra lemma**.

This revision takes the **second path** and completes the reframe the prior
narrowing only began. The load-bearing content is hereby scoped as a
**purely formal, finite-dimensional linear-algebra lemma**:

- **In scope (formal lemma, unconditional on any physics):** Let `H` be the
  finite-dimensional class-sector inner-product space with orthonormal
  class basis `{χ_(p,q)}`. Let `S` be **any** linear operator on `H`, `η ∈ H`
  **any** vector, and `ell_W: H -> C` **any** linear evaluation functional.
  When inner-product notation is used, `k(W) ∈ H` denotes the Riesz
  representative of `ell_W`, so `ell_W(v) = ⟨k(W), v⟩`. Define
  `z_(p,q) = ⟨χ_(p,q), S^{L⊥−1} η⟩`, `v = Σ z_(p,q) χ_(p,q)`,
  and `Z(W) = ell_W(v) = ⟨k(W), v⟩`. Define normalized
  `ρ_(p,q) = z_(p,q)/z_(0,0)` **only on the domain `z_(0,0) != 0`**.
  If `z_(0,0) = 0`, the formal lemma retains the unnormalized `z` and
  `Z(W)` statements but makes no `ρ` claim. Then the relations in
  Theorem 1 / Corollaries 1–2 below hold **by elementary linear algebra**.
  This is true for arbitrary abstract `(S, η, ell_W)`; it carries **no**
  Wilson/Haar, β=6, or plaquette content and is conditional on nothing
  beyond the abstract hypotheses just stated.
- **Out of scope (the physical identification — NOT claimed here):** that the
  abstract `S` equals the compressed β=6 Wilson/Haar environment kernel
  `S_6^env = P_cls K_6^env P_cls`, that `η` equals the β=6 rim lift
  `η_6 = P_cls B_6`, and that `ell_W` is represented by the canonical
  Peter–Weyl evaluation Riesz vector. Each of those identifications requires the four
  required-but-unsupplied retained authorities enumerated below
  (full Wilson/Haar one-slab kernel, full-slice rim-lift, exact kernel/rim
  compression, exact compressed rim-evaluation). They remain **unsupplied**;
  the β=6 application is therefore **not** part of this note's load-bearing
  claim.
- The runner is a **finite-block structural check of the formal algebra**
  (it verifies the coefficient relations on small explicit `(S, η, ell_W)`
  instances); it does **not** derive the four physical Wilson/Haar
  identities.

Net effect: where the prior form said "conditional reduction of the β=6
PF seam," this form says "a linear-algebra identity about abstract operators,
plus an explicitly out-of-scope physical bridge awaiting four authorities."
The β=6 references throughout the body below are retained only as the
**intended application** of the formal lemma, and are governed by this
out-of-scope boundary. No new axiom, import, or retained bridge is
introduced. Downstream plaquette-lane siblings that cite "the reduction"
inherit the same formal-lemma + out-of-scope-bridge scope.

## 2026-05-27 Audit Repair (conditional-reduction narrowing)

The 2026-05-25 audit verdict was `audited_conditional` with closure
issue:

> *"The reduction would be algebraic if the full Wilson/Haar
> kernel/rim integral boundary theorems and full boundary-amplitude
> identity were retained inputs. In this packet, the supplied
> transfer authority is only retained_bounded and explicitly does not
> claim the actual full Wilson-environment transfer identity, while
> the asserted exact integral objects and rim/compression authorities
> are not supplied as retained load-bearing inputs."*

Repair instruction: *"supply retained full-scope authorities proving
the actual Wilson/Haar one-slab kernel, full-slice rim lift, and
untruncated boundary-amplitude identity used by the reduction."*

Supplying the named retained authorities is substantive new work
(each of the integral boundary theorems is itself an open theoretical
target) and is out of scope for a review-loop PR per the framework
policy on adding new retained authorities. This revision takes the
**conditional-reduction narrowing path**:

- demote claim_type `positive_theorem` -> `bounded_theorem`;
- restate the load-bearing claim explicitly as a **conditional
  reduction**: GIVEN the named integral boundary theorems and the
  untruncated boundary-amplitude identity as supplied premises, the
  reduction of the beta=6 plaquette PF seam to matrix-element
  evaluation is algebraic;
- explicitly enumerate the assumed (not-retained) inputs in the
  "Required-but-unsupplied retained authorities" section below;
- the runner remains as a structural finite-block check on the
  bounded surface; it does not by itself derive the assumed integral
  identities.

The cited one-hop authority
([`GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TRANSFER_THEOREM_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TRANSFER_THEOREM_NOTE.md))
is `retained_bounded` and supplies a bounded transfer surface, not
the full Wilson-environment transfer identity that the reduction
needs. The
[`GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TRANSFER_UNDERDETERMINATION_NOTE_2026-04-17.md`](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TRANSFER_UNDERDETERMINATION_NOTE_2026-04-17.md)
dep records the underdetermination explicitly. The reduction theorem
in §"Theorem 1" below is therefore conditional, not unconditional.

### Required-but-unsupplied retained authorities

The reduction theorem in §"Theorem 1" assumes the following four
inputs as supplied premises. None is currently in retained inventory
as a one-hop authority for this row; each is named here so any future
audit can confirm or supply them.

1. **Full Wilson/Haar one-slab kernel theorem** — exact form of
   `K_beta^env(U_{k+1}, U_k)` as a single Wilson/Haar bulk slab
   integral, with the untruncated kernel identity used by the
   compression step.
2. **Full-slice rim-lift theorem** — exact form of `B_beta(W)` as a
   single local Wilson/Haar rim integral on the full slice, with the
   untruncated rim-lift identity used by the compression step.
3. **Exact kernel/rim compression theorem** — the canonical
   compression law `S_6^env = P_cls K_6^env P_cls`,
   `eta_6(W) = P_cls B_6(W)` with the untruncated compression
   identity used downstream.
4. **Exact compressed rim-evaluation theorem** —
   `Z_6^env(W) = ell_W(v_6) = <k(W), v_6>` via the canonical
   Peter-Weyl evaluation law on the compressed boundary, where `k(W)`
   is the Riesz representative of the evaluation functional.

Downstream consumers that need the reduction as a closed bounded
theorem (not a conditional reduction) must wait until retained
one-hop authorities for (1)-(4) land; until then this row's
load-bearing scope is the conditional reduction only.

### Bounded-Wall Discipline Gate

**Status:** PASS for the conditional reduction only. This is not a
positive closure of the beta=6 plaquette seam, and it is not a claim
that the four required authorities already exist. It records the
strongest current source-science result: if the named Wilson/Haar
kernel, rim-lift, compression, and compressed rim-evaluation inputs are
supplied, the remaining reduction to matrix-element evaluation is
algebraic.

#### N1 - Alternative route enumeration

| route | what it would attempt | why it fails for unconditional closure | marker |
|---|---|---|---|
| Use the retained-bounded transfer theorem as full transfer authority | Treat `GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TRANSFER_THEOREM_NOTE.md` as supplying the full Wilson-environment transfer identity. | That authority is bounded and does not claim the untruncated full transfer identity required here. | ATTEMPTED |
| Use the underdetermination note as a positive bridge | Treat the underdetermination note as closing the transfer gap. | It records the missing authority boundary; it does not supply the missing kernel/rim identities. | ATTEMPTED |
| Let the finite-block runner derive the integral theorems | Promote the runner's structural checks into proof of the Wilson/Haar integral objects. | The runner checks the conditional reduction form; it does not derive the full one-slab kernel, rim lift, compression, or rim-evaluation identities. | ATTEMPTED |
| Collapse compression into kernel/rim existence | Assume exact kernel/rim existence automatically implies the untruncated compression law. | Compression is a separate identity on the projected class-sector object and is named as its own required input. | ATTEMPTED |
| Treat matrix-element evaluation as already complete | Say the seam is solved because it is reduced to matrix elements. | The matrix elements are explicit evaluation targets, not evaluated coefficients or an analytic `P(6)` closure. | ATTEMPTED |
| Add the four missing authorities in review-loop | Introduce new full-scope retained theorems in this repair PR. | That would be substantive new theory and requires separate source work plus independent audit, not a review-loop metadata repair. | RULED OUT BY PRIOR |

#### N2 - Wall-independence audit

The collapsed wall set is the four authorities listed above. The full
kernel and full rim inputs are separate integral objects. The
compression law uses those objects but is not implied by merely naming
them. The compressed rim-evaluation law is downstream of compression
but still requires its own exact Peter-Weyl evaluation identity. None
of the four walls is dropped or presented as independently retained.

#### N3 - Hidden-wall scan

Terms such as "exact", "already fixed", and "canonical" are now scoped
inside the conditional premise stack. The live source claim does not
use those phrases as hidden retained authorities. The hidden admission
found by the scan is exactly the four-item wall set above.

#### N4 - Residual matching

The residual being narrowed is the same one recorded by the
underdetermination dependency: full Wilson/Haar transfer and boundary
amplitude identities are not retained as one-hop inputs for this row.
This note does not cite the runner, the bounded transfer theorem, or
the underdetermination note as witnesses that those residuals are
closed.

#### N5 - Rhetoric audit

Unqualified phrases such as "exact reduction" are replaced or governed
by "conditional reduction". The note does not claim explicit
closed-form matrix elements, explicit normalized `rho_(p,q)(6)` outside
the domain `z_(0,0)^env(6) != 0`, plaquette PF data, or analytic `P(6)`
closure.

#### N6 - Partial-closure path scan

The legitimate path is the standard import-retirement path: first land
the four named source theorems as bounded/positive candidates, then let
the independent auditor decide whether they become retained-grade
authorities, then re-audit this reduction. This path does not require a
new axiom or repo-wide premise.

#### N7 - Steelman

A hostile reviewer could argue that the retained-bounded spatial
environment transfer theorem plus the runner already gives enough
support for a bounded theorem. That succeeds only for the conditional
version kept here. It does not support the prior unconditional
positive theorem, because the full untruncated kernel/rim and
boundary-amplitude identities remain unsupplied.

#### N8 - Cross-cycle echo

Plaquette-lane repairs have repeatedly failed when bounded transfer
support was treated as retained full-scope authority. This revision
avoids that echo by making the premise stack explicit, leaving the
row unaudited for the independent audit lane, and requiring future
source work before any unconditional parent promotion.

## Question

If the named Wilson/Haar kernel, rim-lift, compression, and compressed
rim-evaluation identities are supplied as premises, what is the
strongest honest next theorem on the explicit `beta = 6` PF seam?

## Answer

It is a **conditional** reduction theorem: under the four required-
but-unsupplied retained authorities listed in §"2026-05-27 Audit
Repair" above (full Wilson/Haar one-slab kernel, full-slice rim-lift,
exact kernel/rim compression, and exact compressed rim-evaluation
laws), the reduction below is algebraic. Until those authorities are
retained one-hop on this row, the in-scope content is the conditional
form of the reduction, not an unconditional bounded theorem.

At `beta = 6`, the remaining framework-point seam is **conditionally**
not:

- a search for a new post-compression operator formalism,
- a search for a new compressed `W`-dependence law,
- or an unsupported claim of analytic closure.

It is exactly the evaluation problem for the class-sector matrix
elements of the premise integral objects.

Let

`S_6^env = P_cls K_6^env P_cls`,

`eta_6(W) = P_cls B_6(W)`.

Then the boundary coefficients are exactly

`z_(p,q)^env(6)
 = <chi_(p,q), (S_6^env)^(L_perp-1) eta_6(e)>`,

and, when `z_(0,0)^env(6) != 0`,

`rho_(p,q)(6)
 = z_(p,q)^env(6) / z_(0,0)^env(6)`.

This normalized statement is part of the theorem only on the explicit
domain `z_(0,0)^env(6) != 0`. If that denominator vanishes for a supplied
premise packet, the unnormalized `z_(p,q)^env(6)` and `Z_6^env(W)` reduction
statements remain well-defined, but no normalized `rho_(p,q)(6)` statement
is made.

Under the premise that `K_6^env` and `B_6(W)` are supplied as exact
Wilson/Haar integrals, the remaining explicit `beta = 6` problem is
evaluation of the integral-defined class-sector matrix elements
entering `S_6^env` and `eta_6`.

Under the compressed rim-evaluation premise, the marked-holonomy
dependence is canonical:

`Z_6^env(W) = ell_W(v_6) = <k(W), v_6>`,

with

`v_6 = sum_(p,q) z_(p,q)^env(6) chi_(p,q)`.

So the strongest honest next theorem is a reduction of the seam to explicit
matrix-element evaluation, not a claim that those evaluations are already in
closed form.

## Setup

From the full one-slab orthogonal-kernel integral premise:

- `K_beta^env(U_(k+1), U_k)` is one exact Wilson/Haar bulk slab integral,
- but no explicit closed-form `beta = 6` evaluation is yet derived.

From the full-slice rim-lift integral premise:

- `B_beta(W)` is one exact local Wilson/Haar rim integral on the full slice,
- `eta_beta(W) = P_cls B_beta(W)`,
- but no explicit closed-form `beta = 6` evaluation is yet derived.

From the exact kernel/rim compression premise:

- once `K_6^env` and `B_6` are explicit, `S_6^env`, `eta_6`, the
  unnormalized `z_(p,q)^env(6)`, and the downstream plaquette PF data
  follow canonically; normalized `rho_(p,q)(6)` follows only on the
  explicitly stated nonzero-denominator domain.

From the exact compressed rim-evaluation premise:

- after compression, `Z_beta^env(W) = ell_W(v_beta) = <k(W), v_beta>`,
- so the compressed `W`-dependence is explicit through the canonical
  Peter-Weyl evaluation functional, represented in `H` by the Riesz
  vector `k(W)` when inner-product notation is used.

Therefore the only honest next theorem seam is evaluation of the beta-side
matrix elements generated by the premise integral objects.

## Theorem 1: conditional beta=6 matrix-element reduction of the integral seam

**Conditional on** the four required-but-unsupplied retained
authorities in §"2026-05-27 Audit Repair" above (full Wilson/Haar
one-slab kernel, full-slice rim-lift, exact kernel/rim compression,
and exact compressed rim-evaluation laws), the following holds.

Let `chi_(p,q)` denote the marked class-function basis and let

`S_6^env = P_cls K_6^env P_cls`,

`eta_6(W) = P_cls B_6(W)`.

Define the class-sector matrix elements

`S_((p,q),(r,s))(6) = <chi_(p,q), S_6^env chi_(r,s)>`,

`b_(p,q)(W;6) = <chi_(p,q), eta_6(W)>`.

Then the framework-point boundary coefficients satisfy the exact reduction law

`z_(p,q)^env(6)
 = <chi_(p,q), (S_6^env)^(L_perp-1) eta_6(e)>`,

so every `z_(p,q)^env(6)` is determined entirely by the matrix elements
`S_((p,q),(r,s))(6)` and `b_(r,s)(e;6)`.

If `z_(0,0)^env(6) != 0`, the normalized coefficients are then

`rho_(p,q)(6) = z_(p,q)^env(6) / z_(0,0)^env(6)`.

Because `K_6^env` and `B_6(W)` are supplied as premise Wilson/Haar
integrals in this conditional theorem, those class-sector matrix
elements are themselves explicit integral-evaluation targets.

So the remaining explicit `beta = 6` seam is exactly:

- evaluate the compressed bulk matrix elements of `K_6^env`,
- evaluate the compressed rim matrix elements of `B_6(W)`,
- propagate them through the supplied boundary-amplitude law.

No additional structural unknown is introduced at this stage.

## Corollary 1: conditional compressed evaluation-boundary law

Let

`v_6 = sum_(p,q) z_(p,q)^env(6) chi_(p,q)`.

Then for every marked holonomy `W`,

`Z_6^env(W) = ell_W(v_6) = <k(W), v_6>`,

with `ell_W` the canonical Peter-Weyl evaluation functional and `k(W)` its
Riesz representative in the finite class-sector Hilbert space.

Therefore, conditional on the compressed rim-evaluation premise, once
the matrix elements determining `v_6` are evaluated, the full
compressed boundary class function is explicit automatically. The
compressed `W`-dependence is not an additional open seam under that
premise.

## Corollary 2: strongest honest framework-point statement now supportable

At the framework point `beta = 6`, the strongest honest next theorem-grade
statement is:

- the bulk side is conditionally reduced to matrix-element evaluation
  of the supplied one-slab Wilson/Haar kernel `K_6^env`,
- the local marked side is conditionally reduced to matrix-element
  evaluation of the supplied full-slice Wilson/Haar rim lift `B_6(W)`,
- the compressed `W`-dependence is canonical under the supplied
  compressed rim-evaluation law,
- so the remaining PF seam is evaluation, not a missing new formalism
  and not analytic closure.

## What this closes

- conditional reduction of the live `beta = 6` PF seam to evaluation of
  the integral-defined class-sector matrix elements of `K_6^env` and
  `B_6(W)`
- conditional clarification that the compressed `W`-dependence is fixed
  by the supplied Peter-Weyl evaluation law
- conditional clarification that no additional post-compression
  structural theorem is needed before explicit evaluation once the
  four premise authorities are supplied

## What this does not close

- explicit closed-form matrix elements of `K_6^env`
- explicit closed-form matrix elements of `B_6(W)`
- explicit normalized coefficients `rho_(p,q)(6)` outside the nonzero
  denominator domain `z_(0,0)^env(6) != 0`
- explicit framework-point plaquette PF data
- analytic closure of canonical `P(6)`

## Why this matters

This is the strongest honest next theorem because it keeps the missing
integral authorities explicit.

The branch no longer has to say only that `K_6^env` and `B_6(W)` exist as
integrals, and it also does not have to pretend they are already solved
or retained.

It can now say exactly what explicit work remains:

- evaluate the bulk integral matrix elements,
- evaluate the rim integral matrix elements,
- then read off the compressed boundary data and downstream PF data
  canonically.

## Command

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_first_three_sample_environment_evaluator_route_2026_04_17.py
```

Expected summary:

- `THEOREM PASS=5 SUPPORT=5 FAIL=0`

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [gauge_vacuum_plaquette_spatial_environment_transfer_theorem_note](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TRANSFER_THEOREM_NOTE.md)
- `gauge_vacuum_plaquette_compressed_rim_functional_uniqueness_note_2026-04-17`
  (downstream consumer; backticked to avoid length-3 cycle through
  beta6_scalar_value_insufficiency — citation graph direction is
  *compressed_rim_functional_uniqueness → beta6_scalar_value_insufficiency
  → this_evaluation_seam*)
- `gauge_vacuum_plaquette_first_symmetric_three_sample_exact_radical_reconstruction_map_note_2026-04-17`
  (downstream consumer; backticked to avoid length-2 cycle —
  citation graph direction is *first_symmetric_reconstruction_map → this_seam*)
- `gauge_vacuum_plaquette_first_symmetric_three_sample_current_stack_constraint_boundary_note_2026-04-17`
  (downstream consumer; backticked to avoid length-3 cycle through
  first_symmetric_reconstruction_map — citation graph direction is
  *current_stack_constraint_boundary → first_symmetric_reconstruction_map
  → this_seam*)
- [gauge_vacuum_plaquette_spatial_environment_transfer_underdetermination_note_2026-04-17](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TRANSFER_UNDERDETERMINATION_NOTE_2026-04-17.md)
- `gauge_vacuum_plaquette_first_three_sample_local_wilson_retained_positive_cone_obstruction_note_2026-04-17`
  (see-also cross-reference; backticked to break residual plaquette-cluster
  cycles through the local-Wilson positive-cone-obstruction surfaced after
  the underdetermination see-also edges were demoted in this PR. The
  positive-cone-obstruction note is a downstream three-sample positive-cone
  reduction; the present beta6 evaluation-seam reduction note closes the
  explicit beta=6 seam upstream and does not consume the positive-cone
  reduction for its own scope. The load-bearing citation direction is
  *positive_cone_obstruction → this_seam*, not vice versa.)
