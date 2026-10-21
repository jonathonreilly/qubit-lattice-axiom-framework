# A native ultrasoft charged mode of large column features

**Status:** bounded-support.
**Claim type:** bounded_theorem.
**Primary runner:** [scripts/native_row_tunneling.py](../scripts/native_row_tunneling.py)

The original one-qubit Hamiltonian produces an ultrasoft finite-array mode
and its local-spin coupling without an added interaction. It is symmetry-
charged; the neutral scalar diagnostic has zero matrix element to this
charged transition under the stated plane symmetries.
This advances native collective dynamics while leaving the scalar bridge open.

## Deriving the scale instead of assigning it

Fix an even M by M transverse torus, M>=4, and open columns of even height
L>=6. Let Jx=Jy=lambda Jz>0 and take lambda to zero at fixed dimensions.
This is a different geometry and limit from the growing periodic cubes used
in the [neutral response bound](NATIVE_STATIC_NEUTRAL_RESPONSE_NOTE_2026-10-18.md).

Two previously derived native processes supply the ingredients:

- The [plaquette interaction](NATIVE_COLUMN_PLAQUETTE_SELECTION_NOTE_2026-10-18.md)
  has K=(L+14)Jz lambda^4/128 and favors signs s_xy=a_x b_y.
- [Pair-column tunneling](NATIVE_LARGE_COLUMN_DYNAMICS_NOTE_2026-10-18.md)
  has t=Jz lambda^L/2^(L-1).

A pair flip does **not** move within the plaquette-positive manifold on a
large transverse grid: it creates plaquette defects. The direct compression
of that pair operator is zero. This rules out simply relabeling its scale as
the ground-band splitting.

Instead, n=M/2 pair events cover an entire row or column. There are two
minimal perfect matchings. An intermediate matching subset with r runs
costs 8Kr. Summing every ordering gives the first nonconstant ground operator

    H_ground = scalar - tau_M (sum_x R_x + sum_y C_y) + o(tau_M),
    tau_M = 2 binom(2n-2,n-1) t^n/(8K)^(n-1).

The root proof (`outputs/neutral_continuation4_review_2026_10_18/proofs/HIERARCHICAL_ROW_TUNNELING_PROOF.md`)
uses two exact finite-dimensional analytic reductions, not just a truncated
column model. Native spin-flip counting bounds each aligned-block event;
small plaquette denominators are then accounted for explicitly. Grouping
events or inserting extra events is higher order. Folded terms cannot change
the first nonconstant transition. The independent native hierarchy check (`outputs/neutral_continuation4_review_2026_10_18/proofs/INDEPENDENT_HIERARCHICAL_NATIVE.md`)
records those controls.

Row and column flips commute and their total product is identity. Their
all-plus character is the unique leading ground state; the first allowed
excitation flips two signs and costs 4tau_M. For sufficiently small lambda
at the fixed dimensions, this gives the native gap 4tau_M+o(tau_M).
For M=4,L=6,

    tau_M = Jz lambda^8/320,
    gap = Jz lambda^8/80 + o(Jz lambda^8).

The native word uses at least twelve transverse bonds, but the intervening
plaquette denominator removes four powers of lambda. A bare word count is
not a bound on the resummed splitting exponent.

## A derived coupling and exact symmetry matrix elements

A local physical Z_xyz becomes the column sign a_x b_y in the aligned
manifold. It toggles one row and one column character with matrix element
one. Its native spectral weight at the corresponding low line therefore
tends to one as lambda tends to zero. This follows from the same microscopic
operator; no adjustable scalar source constant has been supplied.

But Z is charged under the x and y plane symmetries. In a symmetry-invariant
state its translated correlations vanish unless the two probes lie on the
same vertical column. The neutral distance-two diagnostic Z_r Z_(r+2ez)
preserves every character and has zero intraband inelastic matrix elements.

> **Deferred physical continuation (not promoted):** The interpretation that
> this soft charged line is not a neutral three-dimensional scalar mediator
> is separate from those exact matrix-element zeros.

The charge proof (`outputs/neutral_continuation4_review_2026_10_18/proofs/PLANE_CHARGE_MOBILITY_PROOF.md`)
and independent check (`outputs/neutral_continuation4_review_2026_10_18/proofs/INDEPENDENT_CHARGE_MOBILITY.md`)
give the general symmetry equation: in a symmetry-invariant state,
<C T_r(C)> = 0 whenever translation changes a nonempty plane-charge pattern
of the bounded Pauli template C. For single X, Y and Z templates, the
pattern-preserving displacements lie on their respective axes; for some
dipoles they lie in a plane.

> **Deferred physical continuation (not promoted):** Interpreting these
> correlation zeros as mobility restrictions or mediator-route exclusions
> is deferred. Pattern preservation alone does not prove propagation.
> Neutral templates, symmetry-breaking states, changed templates and
> nonlocal dressings require separate analysis.
Compass subsystem symmetry and dimensional reduction are established prior
structure; see [Nussinov and Fradkin](https://arxiv.org/abs/cond-mat/0410720).
The present contribution is the checked finite-array hierarchy and source
interpretation, not the invention of those symmetries.

## Checks and remaining assumptions

The matching check (`outputs/neutral_continuation4_review_2026_10_18/proofs/INDEPENDENT_ROW_TUNNELING.md`)
proves the all-n coefficient. The runner verifies exact rational path sums
through n=14 and diagonalizes the 16-column coefficient model in two
512-dimensional character sectors. As t/K decreases from .1 to .005, its
gap divided by 2t^2/K approaches one (1.05345 to 1.00013), while the Z
weight approaches one (.997423 to .999994). Residuals are below 7e-13.
These are development controls, not diagonalization of 96 physical qubits.

The native result is asymptotic at fixed finite dimensions. It supplies no
uniform threshold as features grow, no isotropic continuum, and no physical
unit or cosmological identification. The Hamiltonian, anisotropy, geometry,
ground-state problem and measurement interpretation remain premises. No
observation is fitted or independently tested. The large-feature scalar and
measured-gravity connection remains open.

## Current source and execution boundary

The complete live mathematical sources are listed in the primary's literal input closure. Historical reviewer dispositions and saved numerical results are provenance, not current evidence. The primary computes its declared finite controls in a fresh preserved temporary directory, enforces its aggregate wall-clock cap before scientific imports, and streams partial diagnostics. Frozen native coefficient tables are explicitly labeled input checks, not newly enumerated paths. Distinct primary assertion groups are counted; helper assertions are additional uncounted fail-closed checks. No audit status or physical primitive is introduced.

**Deferred terminal negative promotion:** The complete scoped selection-rule and response-bound derivations remain live and inspectable. Their terminal exclusion interpretations (neutral-mediator route exclusion, charged-template mobility restriction, square intraband darkness as an exclusion claim, and restored-join route pruning, as applicable) are not promoted by this package without the required qualifying negative-claim packet. This boundary does not erase or reverse the exact algebraic zeros or conditional estimates, and does not assert coverage of unexamined routes.
