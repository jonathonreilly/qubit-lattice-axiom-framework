# Universal GR `Pi_curv` Route-Exhaustion No-Go Gate on the Current Direct-Universal Surface

**Date:** 2026-06-18
**Claim type:** no_go
**Source-side status:** bounded-support
**Status authority:** source-side proposal only; independent audit sets any
effective status.
**Primary runner:** [`scripts/frontier_universal_gr_picurv_route_exhaustion_no_go_2026_06_18.py`](../scripts/frontier_universal_gr_picurv_route_exhaustion_no_go_2026_06_18.py)
**Cached runner output:** [`logs/runner-cache/frontier_universal_gr_picurv_route_exhaustion_no_go_2026_06_18.txt`](../logs/runner-cache/frontier_universal_gr_picurv_route_exhaustion_no_go_2026_06_18.txt)
(`PASS=22 FAIL=0 TOTAL=22`)
**Target audited row:** `universal_gr_polarization_frame_bundle_blocker_note`

## Target blocker

The current audit repair request for
`universal_gr_polarization_frame_bundle_blocker_note` is:

> `scope_too_broad: narrow to the finite frame-delta/orbit support result or provide an exhaustive no-go gate covering at least five alternative Pi_curv construction routes.`

This note takes the second path. It supplies an N1-N8 no-go gate for the
current direct-universal surface. It does not edit the audit ledger, does not
retag the parent row, and does not assert that future stronger GR inputs are
impossible.

## Scope

The target object is a full current-stack curvature-localization operator
`Pi_curv` on the direct-universal `PL S^3 x R` surface:

1. it starts from the scalar observable generator, the exact `3+1` lift, the
   tensor-valued Hessian candidate, and the unique symmetric quotient kernel;
2. it extends the exact rank-2 A1 projector on lapse and spatial trace to the
   complementary channels;
3. it supplies a distinguished covariant connection or horizontal
   distribution on the complement;
4. it performs the TT/gauge reduction needed to identify the local channel
   data with curvature degrees of freedom; and
5. it identifies the resulting operator with an Einstein/Regge dynamics law on
   the same direct-universal surface without importing a supplied geometric
   action or a different atlas.

The no-go here is local to that target. It is not an absolute no-go against
GR, not a no-go against canonical pointwise channel projectors, not a no-go
against supplied-action Regge routes, and not a no-go against the flat-atlas
spin-2 generator.

Firewall summary: not an absolute no-go; not a no-go against
supplied-action Regge routes; not a no-go against the flat-atlas spin-2
generator; not a mathematical impossibility theorem; not a claim that future
stronger GR inputs are impossible. Independent audit sets any effective
status.

## Current exact positives preserved

The current stack already has real positive structure:

- exact scalar generator `W[J] = log|det(D+J)| - log|det D|`;
- exact `3+1` kinematic scaffold `PL S^3 x R`;
- exact tensor-valued Hessian candidate;
- exact unique symmetric quotient kernel on the finite prototype;
- exact A1 projector onto lapse and spatial trace;
- exact representation-level Casimir block projectors into lapse, shift,
  trace, and shear;
- supplied round-`PL S^3` Regge Hessian channel data; and
- supplied flat-atlas spin-2/two-derivative curvature generator data.

Those positives are not demoted. The result below says only that none of them,
alone or in their current registered combinations, derives the full `Pi_curv`
object defined above on the current direct-universal surface.

## Theorem

**Theorem (current-stack `Pi_curv` route exhaustion).** On the current
direct-universal `PL S^3 x R` surface, each reviewed route family in the table
below fails to derive a full `Pi_curv` without adding an extra load-bearing input:
a distinguished connection/horizontal distribution, a TT/gauge reduction, a
source-coupling or matter-readout law, a supplied geometric action, or a
different supplied atlas. Therefore the parent blocker can be read as a
bounded-support no-go for current-stack derivation of full `Pi_curv`, not as a
claim that all future curvature-localization routes are impossible.

The theorem is a route-exhaustion gate over current repo surfaces, not a
mathematical impossibility theorem over all possible extensions.

## Route table

| Route | Candidate construction | What it proves | Why it does not derive full `Pi_curv` |
|---|---|---|---|
| ROUTE-1 A1 extension | Extend `Pi_A1 = diag(1,0,0,0,1,0,0,0,0,0)` to the complement. | A1 lapse/trace block is frame-invariant. | The complement remains frame-dependent; no distinguished connection or TT reduction is selected. |
| ROUTE-2 quotient-kernel eigenbasis | Use the unique symmetric Hessian kernel or an eigenbasis of it as the projector bundle. | The finite prototype kernel is unique and nondegenerate. | Eigenbasis data depend on the supplied finite prototype/background and do not supply a covariant bundle law over all valid `3+1` frames. |
| ROUTE-3 Casimir/block projectors | Use the SO(3) Casimir decomposition into lapse, shift, trace, and shear. | Representation-level channel projectors are exact. | Isotypic projectors do not choose internal frames, a connection, TT physical subspace, or Einstein/Regge dynamics. |
| ROUTE-4 frame-orbit averaging | Average over valid polarization frames to form an invariant aggregate. | The orbit and its A1 fixed sector are exact. | Averaging removes section data rather than selecting a canonical section; it yields an invariant aggregate, not `Pi_curv`. |
| ROUTE-5 complement orbit bundle | Use `(Pi_A1, O_{E plus T1}, omega_MC)` as the projector/connection candidate. | The natural SO(3) orbit bundle is the strongest candidate forced by the checked data. | The Maurer-Cartan orbit connection is equivariant but not a distinguished curvature-localization connection selecting a canonical complement section. |
| ROUTE-6 finite-rank/exterior helper route | Reuse finite-rank gravity residual and coarse-grained exterior-law helpers. | These helpers provide scalar finite-rank exterior-field support and radial-harmonic projection. | They do not supply tensorial `3+1` polarization localization, TT reduction, or a full curvature operator on the quotient kernel. |
| ROUTE-7 supplied round Regge route | Use the supplied round `PL S^3` Regge Hessian channel theorem. | On the supplied round spatial atlas, the Regge Hessian has a multiplicity-free canonical channel split. | It consumes a supplied action/background and is spatial/round-scoped; it does not derive direct-universal `Pi_curv` from scalar `W` alone on full `PL S^3 x R`. |
| ROUTE-8 supplied flat-atlas spin-2 route | Use the flat-atlas spin-2/two-derivative curvature generator. | A supplied flat-atlas geometric row gives the named spin-2 generator at linearized order. | It explicitly does not claim the `PL S^3 x R` version and consumes supplied flat-atlas/geometric-action structure. |

## Proof-surface dependencies

- [`UNIVERSAL_GR_A1_INVARIANT_SECTION_NOTE.md`](UNIVERSAL_GR_A1_INVARIANT_SECTION_NOTE.md)
  -- finite A1/lapse-trace invariant-section witness.
- [`UNIVERSAL_GR_CASIMIR_BLOCK_LOCALIZATION_NOTE.md`](UNIVERSAL_GR_CASIMIR_BLOCK_LOCALIZATION_NOTE.md)
  -- exact representation-level lapse/shift/trace/shear channel projectors.
- [`UNIVERSAL_GR_CANONICAL_PROJECTOR_CONNECTION_NOTE.md`](UNIVERSAL_GR_CANONICAL_PROJECTOR_CONNECTION_NOTE.md)
  -- strongest current orbit-connection candidate and its unfinished boundary.
- [`UNIVERSAL_GR_COMPLEMENT_CANONICAL_NOTE.md`](UNIVERSAL_GR_COMPLEMENT_CANONICAL_NOTE.md)
  -- local complement-section no-go boundary.
- [`UNIVERSAL_GR_ROUND_PL_S3_REGGE_HESSIAN_CANONICAL_CHANNELS_NARROW_THEOREM_NOTE_2026-06-10.md`](UNIVERSAL_GR_ROUND_PL_S3_REGGE_HESSIAN_CANONICAL_CHANNELS_NARROW_THEOREM_NOTE_2026-06-10.md)
  -- supplied round-spatial-Regge positive route and its supplied-input scope.
- [`UNIVERSAL_GR_SPIN2_TWO_DERIVATIVE_CURVATURE_GENERATOR_SUPPLIED_FLAT_ATLAS_NARROW_THEOREM_NOTE_2026-06-10.md`](UNIVERSAL_GR_SPIN2_TWO_DERIVATIVE_CURVATURE_GENERATOR_SUPPLIED_FLAT_ATLAS_NARROW_THEOREM_NOTE_2026-06-10.md)
  -- supplied flat-atlas spin-2 generator route and its surface boundary.
- [`FINITE_RANK_GRAVITY_RESIDUAL_HELPER_NOTE_2026-04-14.md`](FINITE_RANK_GRAVITY_RESIDUAL_HELPER_NOTE_2026-04-14.md)
  -- scalar finite-rank helper route boundary.
- [`COARSE_GRAINED_EXTERIOR_LAW_HELPER_NOTE_2026-04-14.md`](COARSE_GRAINED_EXTERIOR_LAW_HELPER_NOTE_2026-04-14.md)
  -- scalar/isotropic exterior-law helper route boundary.

Target parent, not a proof dependency:
`UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_BLOCKER_NOTE.md`.

## N1-N8 no-go discipline gate

**N1 alternative-route enumeration.** The route table lists eight distinct
families: A1 extension, quotient/eigenbasis, Casimir blocks, orbit averaging,
orbit connection, finite-rank/exterior helpers, supplied round Regge, and
supplied flat-atlas spin-2.

**N2 wall independence.** The collapsed wall set is: connection/horizontal
distribution selection, TT/gauge reduction, source/dynamics identification,
supplied atlas/action input, and spatial-versus-`3+1` scope. They are not
collapsed into a single prose wall.

| Pair | Does closing the first close the second? | Does closing the second close the first? |
|---|---|---|
| connection vs TT/gauge reduction | no | no |
| connection vs source/dynamics | no | no |
| TT/gauge reduction vs supplied atlas/action | no | no |
| supplied atlas/action vs spatial-versus-`3+1` scope | no | no |
| source/dynamics vs spatial-versus-`3+1` scope | no | no |

**N3 hidden-wall scan.** Phrases such as "canonical", "covariant", "full
`Pi_curv`", and "current stack" are scoped to the five target conditions in
the Scope section. A route that adds a new primitive or supplied action is not
silently counted as current-stack closure.

**N4 residual matching.** The no-go matches the audited blocker only. It does
not claim full GR failure, does not weaken the existing A1/Casimir positives,
and does not decide later interpretation-theorem questions beyond the parent
row.

**N5 rhetoric audit.** "No-go" means "no current enumerated route derives the
target object without extra load-bearing input." It does not mean "Nature
forbids `Pi_curv`" or "all future curvature-localization routes fail."

**N6 partial-closure path.** A future positive route can still close the gate
by deriving a distinguished connection, deriving the TT/gauge reduction on
`PL S^3 x R`, or deriving the supplied-action/atlas bridge from retained
framework structure.

**N7 steelman.** The strongest positive steelman is that canonical channel
projectors and supplied geometric spin-2 generators are real and useful. This
note preserves them. They fail only the narrower full-current-stack `Pi_curv`
target because their current statements leave at least one extra input
load-bearing.

**N8 cross-cycle echo.** The note prevents reuse of the old finite
frame-delta example as an exhaustive proof by itself. The current source
surface now has a separate route-exhaustion gate that later review/audit can
inspect directly.

## Proof sketch

The proof is by current-stack route exhaustion.

First, the parent frame-bundle packet and A1 packet give a finite witness:
under valid spatial rotations the A1 lapse/trace projection is fixed while
the complement channel coefficients move. That witness blocks ROUTE-1 as a
full complement-section derivation.

Second, the Casimir block-localization packet proves exact representation
projectors, but its own boundary excludes a full complement-frame bundle, a
distinguished connection, and Einstein/Regge operator identification. That
blocks ROUTE-3 as full `Pi_curv` closure while preserving the channel
projectors as exact support.

Third, orbit-valued candidates and orbit averages are equivariant but do not
choose a section. An invariant average is a quotient of the orbit data; it
forgets the local complement coordinates that `Pi_curv` must localize. That
blocks ROUTE-4 and ROUTE-5 as derivations of a distinguished operator.

Fourth, helper and supplied-geometric routes are not failures; they are
different premise classes. The finite-rank/exterior helpers are scalar and
finite-support scoped. The round Regge and flat-atlas spin-2 routes consume
supplied geometry/action/atlas inputs and explicitly leave the direct
`PL S^3 x R` derivation outside their claimed scope. That blocks ROUTE-6,
ROUTE-7, and ROUTE-8 as current-stack derivations while preserving them as
support or alternative positive lanes.

Finally, quotient-kernel uniqueness is necessary but not sufficient. A unique
bilinear kernel does not by itself define a covariant localization bundle,
connection, TT reduction, or dynamics identification. That blocks ROUTE-2.

For the reviewed current construction routes in this packet, each route falls
into one of the eight classes above. The parent row can therefore be re-read as
bounded-support route-exhaustion for current-stack `Pi_curv`, not as an
absolute foreclosure of future routes.

## Assumptions and imports

| Item | Role in claim | Current class | Load-bearing? | Disposition |
|---|---|---|---|---|
| Scalar observable generator and `3+1` lift | Current direct-universal surface | framework/support context | yes | Used only to define the target surface. |
| A1 finite frame witness | Shows complement frame dependence remains | exact support on current runner surface | yes | Reproduced in the verifier. |
| Casimir block projectors | Preserved positive channel decomposition | exact support / source proposal | yes | Used as a positive route that still lacks connection and dynamics. |
| Finite-rank/exterior helpers | Candidate imported route family | retained-bounded helper context | yes | Classified as scalar/helper scoped, not full `Pi_curv`. |
| Round Regge and flat-atlas spin-2 notes | Steelman supplied-geometric positive routes | bounded/support context | yes | Classified as supplied-input routes, not direct-universal derivations. |
| Literature or observed values | None | none | no | No literature or measured comparator is consumed. |

## Verification contract

The primary runner checks:

1. the audited blocker quote is present;
2. all N1-N8 gates are present;
3. at least eight route families are explicitly enumerated;
4. the parent note points to this source-side repair packet;
5. the A1 finite witness has zero A1 movement and nonzero complement movement;
6. orbit averaging is not treated as a section selector;
7. existing source notes retain the boundaries used in the route table; and
8. this note contains the no-overclaim firewalls for canonical channel
   projectors, supplied spin-2/Regge routes, future primitives, and
   independent audit authority.

## Honest status

This is bounded-support no-go evidence for the audited parent blocker. It is
audit-ready source material, not an audit verdict. If independent review and
audit accept it, the downstream implication is that consumers of the parent
row can cite a real current-stack route-exhaustion gate rather than a lone
finite frame-delta example. If they reject it, the remaining repair path is
to narrow the parent row to finite frame-delta/orbit support only.
