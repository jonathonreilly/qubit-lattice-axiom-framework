# Cover-difference rank and rational Gram spectrum for a finite cutting incidence — Cycle 758

Date: 2026-08-09

Authority: none; proposed for independent audit.

Audit: unset.

Status: proposed_retained

Claim type: bounded_theorem

Primary runner:

- [finite rebuild-and-gate runner](../scripts/physical_cell_cutting_cover_table_rank_cycle758_2026_08_09.py)

Direct scientific dependencies: none. The runner reconstructs its finite
labelled object from the coordinates and rules declared in its source.

```yaml
actual_current_surface_status: exact-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "No downstream framework claim is identified; this packet records finite incidence identities only."
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "independent audit of the finite reconstruction, exact arithmetic, and stated boundary"
conditional_surface_status: "bounded to the supplied labelled unit-four-cube construction and declared cost and cover rules"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "an exhaustive theorem on one explicitly reconstructed finite incidence object, with no physical or multicell extension"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact target

For the finite incidence object reconstructed by the runner, let `A` be the
15,800 by 192 cutting-by-piece matrix and let `M` be the 192 by 192
cover-by-piece matrix. Certify the following identities over the rationals:

1. `A M^T` is the all-ones matrix, and `M` is 8-regular on both sides.
2. If `H` is the zero-sum subspace of cover coefficients and
   `B = M^T H`, then `B` is a 104-dimensional subspace of `ker(A)`.
3. The row space of `M` is the direct sum of `B` and the all-ones piece
   direction. Consequently `rank(M) = 105`.
4. The cover-side and piece-side Gram matrices `S = M M^T` and
   `N = M^T M` both have rank 105. Their rational eigenvalues, with exact
   multiplicities, are
   `0:87, 2:8, 4:8, 8:3, 10:8, 12:6, 16:2, 20:10, 24:3, 64:1`.
   The other 56 eigenvalues are not rational.

These are finite combinatorial statements. They carry no framework-premise
weight and no physical interpretation.

## Inputs and primitive-registry result

The supplied mathematical object consists of the labelled unit-four-cube
coordinates, normalized-volume simplex rule, adjacency-cost function,
least-cost restriction, exact-cover rule, and the declared finite action used
during reconstruction. These choices are not derived from the framework; they
are the explicit conditional surface that bounds this theorem.

There are no measured, fitted, observational, literature, normalization, or
framework-science inputs. Python and NumPy are computational machinery. The
runner reads no repository science file and declares no `AUDIT_INPUT_PATHS`.
Its canonical cache is generated only by the validation and independent-audit
machinery, rather than treated as a scientific premise.

The primitive-registry check is therefore **not applicable** to the proof
surface: no registered axiom or primitive is consumed, added, or modified.
No minimal-axiom dependency edge is asserted.

## Finite reconstruction

The runner begins with the 16 corners of the labelled unit four-cube. It
enumerates the 4,368 five-corner subsets and retains 2,672 unit
normalized-volume simplices. The adjacency-cost floor is 6, with 400 pieces
at that floor. The declared 48-element action generates 2,736 labelled sample
points with no label collision and no point on a simplex boundary. Exhaustive
exact-cover recursion then gives 15,800 cuttings, each containing 24 pieces.
Exactly 192 pieces occur, each in 1,975 cuttings.

Among those supported pieces the runner enumerates 192 free sets of size
eight. Each meets every cutting exactly once, so each is an exact cover. Their
incidence rows form `M`; its row and column sums are both eight.

The runner gates the subset, simplex, cost-floor, action, sample-point,
collision, boundary, and cover-size invariants before using the reconstructed
object in the rank or spectrum claims. It also checks both sides of every
rounded candidate inverse against the exact integer identity matrix before
using those inverses to classify sample points.

## The 104-dimensional blind subspace

Let

`H = {c in Q^192 : 1^T c = 0}`

and define `B = M^T H`. Since every exact cover meets every cutting once,

`A M^T = J`.

For `c` in `H`, this gives `A M^T c = J c = 0`, hence

`B subset ker(A)`.

It remains to compute the dimension of `B`. If `M^T c = 0`, then row
regularity gives

`0 = 1^T M^T c = (M 1)^T c = 8 (1^T c)`.

Thus `ker(M^T)` is contained in `H`. Fraction-free elimination gives
`rank(M^T) = 105`, so its nullity is 87. Rank-nullity on the restricted map
`M^T : H -> Q^192` therefore yields

`dim(B) = dim(H) - dim(ker(M^T)) = 191 - 87 = 104`.

This proves a 104-dimensional subspace of cutting-blind piece weights. It does
not identify the full kernel of `A`. Equality `B = ker(A)` would additionally
require an independent lower bound `rank(A) >= 88`; that statement is outside
this packet.

## The all-ones complement

Column regularity gives `M^T 1 = 8 1`, so the all-ones piece vector belongs
to the row space of `M`. It does not belong to `B`: every cutting contains 24
supported pieces, hence `A 1 = 24 1`, whereas `A B = 0`.

Every cover-coefficient vector is the sum of a zero-sum vector and a multiple
of the all-ones cover vector. Applying `M^T` gives

`row(M) = B direct-sum span{1}`.

The two summands have dimensions 104 and 1, agreeing with the independently
computed exact rank `rank(M) = 105`.

## Exact rational Gram spectrum

The runner forms the symmetric integer matrices `S = M M^T` and
`N = M^T M`. Fraction-free elimination gives rank 105 for `M`, `S`, and `N`.

For `S`, positive semidefiniteness puts every eigenvalue at or above zero and
the constant row sum 64 bounds the spectrum above by 64. A rational
eigenvalue of an integer matrix is a rational algebraic integer and therefore
an integer. It is consequently enough to test the integers from 0 through 64.

The runner first rejects candidates with full rank modulo the prime 1,000,003.
Such a modular full-rank result forces full rank over the rationals. Every
survivor is then checked by fraction-free integer elimination, so the reported
nullities and multiplicities are exact. The result is:

| eigenvalue | 0 | 2 | 4 | 8 | 10 | 12 | 16 | 20 | 24 | 64 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| multiplicity | 87 | 8 | 8 | 3 | 8 | 6 | 2 | 10 | 3 | 1 |

These account for 136 dimensions. The other 56 eigenvalues are not rational.
The trace identities `tr(S) = 1536` and `tr(S^2) = 36096` provide aggregate
bookkeeping checks: the rational eigenvalues contribute 592 and 12,352,
respectively. These moments are not presented as an independent uniqueness or
completeness proof for the spectral list.

Because `M` is square, `M M^T` and `M^T M` have the same nonzero spectrum and
the same nullity. The runner's matching scan for `N` is therefore a consistency
check, not a separate structural claim. No claim about permutation similarity
or the discriminatory power of spectral data is made here.

The scan has two small controls. It exactly recovers the known spectrum of the
four-cube adjacency matrix, then detects a symmetric one-pair perturbation and
a reduced count of rational eigenvalues.

## Proof-obligation ledger

| obligation | discharge |
|---|---|
| reconstruct the finite object | exhaustive coordinate enumeration plus gated subset, simplex, cost-floor, action, sample-point, collision, boundary, and cover-size invariants |
| establish exact covers and regularity | full incidence multiplication and complete row and column sums |
| prove `B subset ker(A)` | `A M^T = J` followed by restriction to zero-sum coefficients |
| compute `dim(B)` | `ker(M^T) subset H`, exact rank 105, and rank-nullity on the restricted map |
| identify the row-space complement | `M^T 1 = 8 1`, `A 1 = 24 1`, and coefficient-space decomposition |
| bind exact ranks | fraction-free integer elimination, with independent review-time modular checks |
| bind the rational spectrum | finite integer scan with modular rejection and exact rational nullities |
| exercise the spectrum scan | fixed four-cube spectrum plus a symmetric perturbation control |

## Machine evidence and boundary

The runner has 15 contiguous gates and exits nonzero if any gate fails. The
machine-readable timeout is 600 seconds and the measured memory ceiling is
2,500 MB. Validation generates its canonical cache before the changed-evidence
check; generated audit outputs are not source authority.

Outside scope: equality of `B` with the full kernel of `A`, a structural
derivation of rank 105 or nullity 87, individual identification of the 56
non-rational eigenvalues, physical-cell identification, framework primitives,
and any multicell or continuum extension.
