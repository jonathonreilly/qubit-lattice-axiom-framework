# Edge-case delta confirmation

Source: supervisor `autonomous_runtime/RESULT.md`, sections 3-4 actual deltas.
SHA256: `7c156869a4b8fe1a29ef5eb997fa78f2e553546c03dc812798004ac4eb104e88`.
This is source-exposed repair confirmation, not a new independent derivation.
All earlier checks are preserved. No numerical computation was run.

The replacement fallback closes the T=0 finding. Since 0<=l<=k<infinity,

    0 < 1/[2(1+k)] <= q <= 1-1/[2(1+k)] < 1.

Adding a P1 record changes q by
(k+1/2-l)/[(k+1)(k+2)]>0; adding P0 changes it by
-(1/2+l)/[(k+1)(k+2)]<0. In particular the empty condition gives q=1/2,
and one P1 gives q=3/4. With T=0 there are no enabled-predecessor matches,
but this fallback still varies. The earlier constant-kernel defect is removed.

Every fallback case in the previously checked old-record partition requires
only positive support on P0 and P1, not equal weights. The new rule therefore
preserves that proof. Latest-tick cases that recover a legal predecessor still
use its unchanged deterministic tick menu. Enabled value sites still use their
unchanged Born menus. No fallback event is enabled, so neither circuit outcome
cylinders nor formation rates change. The target is excluded from its own
condition, and the finite-ball counts preserve the declared spatial covariance.
The prepared pointer basis remains an explicit supplied condition.

The theorem now explicitly uses simultaneous value/tick appends and assigns a
sequential decomposition its own phase/formation obligation. This removes the
previously unproved alternative from the claimed construction.

No further defect was found in these deltas. This confirms the identified
edge-case repairs only: the result remains a chosen finite-radius joint jump
law, without uniform short-range physical implementation or axiom-selected
gates, Born probabilities, formation rates or timing.
