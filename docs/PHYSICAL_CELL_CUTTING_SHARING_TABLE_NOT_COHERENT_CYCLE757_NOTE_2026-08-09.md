# Exact-cover sharing-table finite identities — Cycle 757

Date: 2026-08-09

Authority: none; proposed for independent audit.

Audit: unset.

Status: proposed_retained

Claim type: bounded_theorem

Primary runner:

- [finite rebuild-and-gate runner](../scripts/physical_cell_cutting_sharing_table_not_coherent_cycle757_2026_08_09.py)

Direct scientific dependencies: none. The runner reconstructs its finite
labelled object from the declared unit-four-cube coordinates in the source.

```yaml
actual_current_surface_status: exact-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "No downstream framework claim is identified; this packet records finite incidence identities only."
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "independent audit of the finite reconstruction, arithmetic, and stated boundary"
conditional_surface_status: "bounded to the supplied labelled unit-four-cube construction and the declared refinement/action"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "an exhaustive theorem on one explicitly reconstructed finite incidence object, with no physical or multicell extension"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact target

For the finite incidence object reconstructed by the runner, certify the
following identities:

1. There are 15,800 minimum-cost cuttings and 192 supported pieces. Every
   cutting contains 24 pieces and every supported piece occurs in 1,975
   cuttings.
2. The 192 enumerated free eight-piece sets meet every cutting exactly once.
   Their cover-by-piece matrix is 8-regular on both sides.
3. The cover-side and piece-side sharing profiles are row-regular with the
   exact profiles listed below, and their off-diagonal multisets differ.
4. Two same-relation entries of `A0^2` have values 134 and 132, while one
   entry of `A0 A1` and `A1 A0` has values 16 and 15.
5. The declared pair-colour refinement has class counts
   `5, 76, 120, 120`.
6. The declared 48-element spatial-rotation/time-flip action has cover-orbit
   sizes `24, 24, 48, 48, 48`; the full cover-difference rank is 104 and the
   five orbit ranks are `23, 47, 23, 35, 29` in runner order.

These are finite combinatorial statements. They carry zero framework-premise
weight and zero physical interpretation.

## Inputs and primitive-registry result

The scientific input surface is empty. The coordinates, adjacency cost,
simplex enumeration, free-set rule, refinement rule, and action are declared
inside the runner. Python and NumPy are computational machinery rather than
scientific inputs.

The primitive-registry check is therefore **not applicable** to the proof
surface: no registered axiom or primitive is consumed or modified. In
particular, this note creates no dependency edge to the framework's minimal
axiom document.

## Reconstruction and counting

The runner begins with the 16 corners of the labelled unit four-cube. It
enumerates five-corner simplices, keeps unit normalized-volume pieces, and
then enumerates cuttings at the declared adjacency-cost floor. Independent
reconstruction guards gate 4,368 five-corner subsets, 2,672 unit-volume
simplices, cost floor 6, and 2,736 orbit-generated sample points with zero
label collisions and zero sample points on a simplex boundary. Every completed
cover has 24 pieces. Independent row and column sums of the resulting incidence
matrix then give

| finite quantity | exact value |
|---|---:|
| cuttings | 15,800 |
| supported pieces | 192 |
| pieces per cutting | 24 |
| cuttings through each supported piece | 1,975 |

Call a set of supported pieces *free* when each cutting contains at most one
of them. If a free set has size `k`, the sets of cuttings incident to its
members are disjoint, so

`1,975 k <= 15,800 = 8 x 1,975`.

Thus `k <= 8`. Equality partitions all 15,800 cuttings into eight incidence
sets, giving exactly one selected piece in every cutting. The runner
independently enumerates 192 free sets of size eight and gates their complete
incidence columns against the all-ones vector.

Each exact cover contains eight pieces. Conversely, fix a cutting. Its 24
pieces receive one member from each of the 192 exact covers. The gated column
sums show eight covers through every supported piece, so the 192 by 192
cover-by-piece matrix has row and column sum eight.

## Sharing profiles

For distinct covers, the number of shared pieces and the count seen from each
cover are

| shared pieces | covers at that value |
|---:|---:|
| 0 | 157 |
| 1 | 20 |
| 2 | 10 |
| 4 | 4 |

For distinct supported pieces, the analogous regular profile is

| shared covers | pieces at that value |
|---:|---:|
| 0 | 158 |
| 1 | 18 |
| 2 | 10 |
| 3 | 2 |
| 4 | 3 |

Across all ordered off-diagonal entries, the cover-side multiset is
`{0:30144, 1:3840, 2:1920, 4:768}` and the piece-side multiset is
`{0:30336, 1:3456, 2:1920, 3:384, 4:576}`. The runner gates both complete
multisets rather than extrapolating from one row.

## Product witnesses and controls

Let `AI` be the identity relation on covers and let `A0`, `A1`, `A2`, and
`A4` mark the four sharing values. The five zero-one matrices are symmetric,
pairwise disjoint, and sum to the all-ones matrix. Their valencies are
`1, 157, 20, 10, 4`.

On the `A0` relation, `A0^2` assumes the eleven exact values

`122, 124, 125, 126, 127, 128, 129, 130, 131, 132, 134`.

The runner records two explicit entries in that same relation with values
134 and 132. It also records an explicit entry where the two ordered products
`A0 A1` and `A1 A0` have values 16 and 15.

The product-value classifier is exercised on two separate 16-vertex
controls. The ordinary Hamming-distance partition of the four-cube reports a
single value for every product/relation combination. Moving one symmetric
pair between two relations preserves a symmetric partition and produces a
multiple-value profile. These controls test both outcomes through the same
code path used for the cover relations.

## Declared refinement and action

The declared refinement recolours each ordered pair by its current colour and
the sorted multiset of colour pairs obtained through every intermediate
cover. Starting with the five sharing relations, repeated application gives

`5 -> 76 -> 120 -> 120` classes.

At stabilization, 48 classes have size 192 and 72 have size 384. The original
five relations split into `1, 100, 10, 6, 3` parts. This is a statement about
the declared iteration only; global minimality among other refinements lies
outside the target.

The declared finite action combines each of the 24 orientation-preserving
spatial signed-permutation rotations with either the identity or a flip of
the fourth coordinate. All 48 transformations permute the reconstructed
pieces and exact covers. Their cover-orbit sizes are `24, 24, 48, 48, 48`.

Fraction-free integer elimination gives orbit-difference ranks
`23, 47, 23, 35, 29` in runner order and full cover-difference rank 104. The
runner also checks each orbit rank against its orbit-size ceiling.

## Proof-obligation ledger

| obligation | discharge |
|---|---|
| reconstruct the finite object | exhaustive coordinate enumeration plus gated subset, simplex, cost-floor, sample-point, collision, boundary, and cover-size invariants |
| justify the eight-piece count | incidence inequality above plus independently gated exact-cover columns |
| establish regular sharing profiles | all rows and complete off-diagonal multisets are gated |
| establish product witnesses | exact integer products and explicit same-relation/ordered-product entries |
| bind the refinement claim | exact round counts, final class sizes, and relation split profile |
| bind the action label | exact signed-permutation parity, optional fourth-coordinate flip, and cover permutation gates |
| bind the ranks | fraction-free integer elimination, with independent review-time rank checks required |

## Machine evidence and boundary

The note declares an empty scientific input surface. The runner declares
`AUDIT_TIMEOUT_SEC = 600`, contains 15 contiguous gates, and exits nonzero if
any gate fails. Its canonical machine evidence is the paired entry under
`logs/runner-cache/`; duplicate cold stdout and hand-authored receipt surfaces
are intentionally absent.

Outside scope: any physical-cell identification, framework primitive,
multicell or continuum extension, group-orbit characterization of the 120
refinement classes, global minimality across alternative refinements, and any
claim inherited from an unlanded predecessor.
