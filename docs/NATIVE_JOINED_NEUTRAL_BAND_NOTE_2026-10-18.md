# Character multiplicities and neutral matrix elements with native joining bonds

**Status:** bounded-support.
**Claim type:** bounded_theorem.
**Primary runner:** [scripts/native_joining.py](../scripts/native_joining.py)

The finite odd-height rectangle supports a derived neutral readout, but it is
not yet an embedded feature. This test restores the existing longitudinal
bonds between two such arrays. At the native endpoint the continued lowest
plaquette band has exactly one state per plane character, so its neutral
inelastic matrix elements within this band vanish.

> **Deferred physical continuation (not promoted):** Interpreting this as removal
> of the odd-half neutral line or pruning this boundary-based construction
> requires the separate negative-claim admission packet.

## A native completion, with no added interaction type

Start with two aligned 4 by 6 by 5 arrays, periodic transversely and open
longitudinally. Restore all 24 missing interface terms -Jz Z_A Z_B. The
result is the supplied Hamiltonian on a 4 by 6 by 10 array. A symbol g for
the interface strength is only a comparison parameter; the physical test is
g=Jz. All conclusions are fixed finite-size, small lambda=Jperp/Jz results.

Within each half's plaquette-positive patterns s_xy=a_x b_y, the interface
energy is

    E_interface = -g (sum_x aA_x aB_x)(sum_y bA_y bB_y).

For g>0 the minimum identifies the physical patterns. The least distinct
relative gauge pattern changes four columns and costs 8g. This is a
restricted comparison within pattern pairs: an arbitrary one-column
mismatch at lambda=0 costs 2g. Either scale precedes the small transverse
splittings for fixed positive g. The argument is not uniform as g tends
to zero with lambda.

## Exact selection in the joined band

The full X and Y plane operators intersect on ten sites and commute.
On aligned columns, their phases reduce to ordinary row and column flips.
The positive-plaquette pattern space has 2^(4+6-1)=512 states and is the
regular representation of the row/column-flip quotient. Every character
therefore occurs once.

For sufficiently small lambda, the isolated continued band preserves
these integer character ranks. Any observable commuting with the full
plane symmetries is diagonal inside the band. Its matrix elements between
different band energies vanish exactly, independently of tiny splittings.

The original distance-two longitudinal ZZ diagnostic is neutral. This
holds for the diagnostic restricted to an old half, for the full joined
diagnostic, and for its terms crossing the former interface. Their inelastic
matrix elements inside this joined band are zero. Transitions into other
bands remain possible; no claim tracks individual levels continuously
through the singular g=0 limit.

> **Deferred physical continuation (not promoted):** The original statement
> that the odd-half neutral transition "thus cannot survive" is retained as
> a deferred interpretation, separate from the exact matrix-element equation.

## The tunneling scale changes as well

The minimal pair-column path in an open longitudinal chain with positive
couplings J_i has the derived leading amplitude

    t_L = Jperp^L / product_(i=1,...,L-1)(2J_i).

Flipping the two columns together reduces the minimal path problem to an
open Ising chain with couplings 2J_i; the edge recurrence or exact subset
path sum gives the product denominator. With eight ordinary longitudinal
bonds and one joining bond,

    t_10 = Jperp^10 / [(2Jz)^8 (2g)],
    t_10(g=Jz) = Jz lambda^10/512.

This is pair-column tunneling, not direct motion within the positive
plaquette band. Its 1/g dependence cannot be extrapolated to g=0.

## What remains to derive

The isolated array's mode and readout were derived, but its open ends
were supplied. This joining test shows why that distinction matters.
A viable embedded feature needs native localization or another mechanism
that survives its actual environment. The earlier compact bulk resonance
avoids cut bonds but has a gap near 8Jz in the weak-coupling regime. Neither
construction yet supplies a light propagating cosmological scalar or
universal detector coupling. These are model-development calculations;
there is no empirical calibration or independent observational test here.

The root proof (`outputs/neutral_continuation4_review_2026_10_18/proofs/NATIVE_JOINING_PROOF.md`)
and independent check (`outputs/neutral_continuation4_review_2026_10_18/proofs/INDEPENDENT_NATIVE_JOINING.md`)
support the selection and coefficient claims. The runner checks all 512
patterns and exact path coefficients at three fixed interface strengths.
It does not diagonalize the 240-spin microscopic Hamiltonian.

## Current source and execution boundary

The complete live mathematical sources are listed in the primary's literal input closure. Historical reviewer dispositions and saved numerical results are provenance, not current evidence. The primary computes its declared finite controls in a fresh preserved temporary directory, enforces its aggregate wall-clock cap before scientific imports, and streams partial diagnostics. Frozen native coefficient tables are explicitly labeled input checks, not newly enumerated paths. Distinct primary assertion groups are counted; helper assertions are additional uncounted fail-closed checks. No audit status or physical primitive is introduced.

**Deferred terminal negative promotion:** The complete scoped selection-rule and response-bound derivations remain live and inspectable. Their terminal exclusion interpretations (neutral-mediator route exclusion, charged-template mobility restriction, square intraband darkness as an exclusion claim, and restored-join route pruning, as applicable) are not promoted by this package without the required qualifying negative-claim packet. This boundary does not erase or reverse the exact algebraic zeros or conditional estimates, and does not assert coverage of unexamined routes.
