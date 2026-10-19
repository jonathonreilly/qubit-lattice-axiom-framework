# Native discrete symmetry and a derived collective readout

Claim type: bounded_theorem.
Primary runner: [native_infrared_readout.py](../scripts/native_infrared_readout.py).


**Type:** bounded_theorem

**Status:** conditional-support; exact finite symmetry and checked leading-theory form factors, unaudited.

[Runner](../scripts/native_infrared_readout.py). Detailed derivation (`outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9720/DERIVED_INFRARED_ROUTE.md`).

The supplied one-qubit compass Hamiltonian has an exact discrete symmetry on its positive-parity 2x2xL tube. A physical square rotation combined with spin rotation and a native plane operation induces a quarter rotation of the previously derived collective axes. It permits changes by four collective flips while forbidding two-flip charge violation. Thus the known sixth-order violation of continuous charge conservation does not itself exclude an emergent long-distance continuous symmetry.

The derived weak-longitudinal XY chain has the standard free compact-boson continuum limit. Its symmetry-allowed leading charge-changing and umklapp vertices have scaling dimension4 at the free point. This is a conditional perturbative infrared route using established bosonization; it is not a native equal-coupling phase proof. Separately, the complete positive-parity rung carries the displayed projective Z2xZ2 representation. Its conditional application of [Ogata–Tachikawa–Tasaki Theorem4](https://arxiv.org/pdf/2004.06458), including the infinite-chain exclusion and allowed alternatives, is preserved as deferred scientific source pending its promotion packet. That exclusion is not an active conclusion of this finite readout note.

The original composite has a calculated readout, rather than an assigned linear scalar coupling. In the leading free theory its low-energy smooth part is

C2=a²[-(3pi+6)(rho_R²+rho_L²)+12rho_R rho_L]+
 higher-dimension and oscillating terms,

where chiral density products are normal ordered. The physical amplitude also carries lambda², lambda=Jz/Jperp, hence low-band spectral weights carry lambda^4. The collective density is odd under collective spin reflection; C2 is even. Their mixed response vanishes in a collective spin-reflection eigenstate. Coincident excitation energies therefore do not identify the same one-boson readout.

Independent fermionic form-factor checks and root spin-basis calculations for periodic effective chains L8,12,16,20 agree within8e-16. The one-pair low-energy weight scales as L^-3 rather than the density's L^-1; the two-pair coefficient and relative continuum sign also check independently. These are leading-theory mathematical tests, not observations.

A separate full-H scan at L4,6,8 and six anisotropy ratios compares native gaps and readout weights against the derived expansion. At L8 and lambda=.1, the maximum first-three-gap discrepancy divided by t is .00010288; weak-ratio errors are consistent with omitted sixth order. At equal strength the approximation is inadequate and sorted-state source weights cannot be matched across level reordering. A failed pure warm-start solve was preserved: it missed lower symmetry-sector states despite small Ritz residuals. The corrected scan includes random components. Neither scan certifies all sectors or the bulk ground state.

The runner reproduces the symmetry and effective-theory computations; it explicitly hashes and consumes the frozen full-H scan JSON rather than rerunning that expensive solve. The native scan source and failed diagnostic remain inspectable. Independent checks cover symmetry/theorem scope, form factors and finite comparison. No observational data, fitted coupling, added interaction, physical source identification or three-dimensional cosmological scalar is claimed. Those remain the target, not consequences of this thin-grid result.

## Source and promotion boundary

The projective rung representation and finite readout calculations are constructive results. The conditional imported infinite-chain LSM exclusion remains supporting mathematics with its full hypotheses; negative promotion is packet-pending. It supplies neither compulsory gaplessness nor a native scalar pole.

Full supporting mathematics and provenance are indexed in `outputs/neutral_composite_continuation_review_2026_10_18/INPUT_CLOSURE.json`. The scope register is `docs/work_history/repo/review_feedback/NEUTRAL_CONTINUATION_BOUNDARIES_2026-10-18.md`. The primary binds literal source/input identities, stages owning-head helpers and frozen inputs in a temporary directory, and captures their diagnostics. Frozen expensive producers are provenance only and are not rerun. Historical reports and executions do not supply a fresh verdict.
