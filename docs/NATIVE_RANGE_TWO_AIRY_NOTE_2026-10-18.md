# Range-two composite asymptotics and closed-arm elimination

**Status:** bounded-support.
**Claim type:** bounded_theorem.
**Primary runner:** [scripts/native_range_two_airy.py](../scripts/native_range_two_airy.py)
**Closed-arm control:** [scripts/native_frozen_arm_control.py](../scripts/native_frozen_arm_control.py)

The [earlier corrected model](NATIVE_CORRECTED_FAST_STRIP_NOTE_2026-10-18.md)
left its range-two Airy expansion as a prediction. This block supplies the
infinite-arm asymptotic proof for that specified coefficient model. A
separate argument controls the other long-separation arms at every fixed
order. Neither statement is a full microscopic resonance theorem.

## Infinite-arm mass and width expansion

In slow units set f=lambda^2/8, epsilon=f^(1/3), n>=1, and

    H_arm=-T+f(n+2)+lambda^2[d I+a T+b(S^2+S*^2)+F],
    d=29/192, a=19/32, b=-13/128, c=d+2a+2b=109/96.

F is any fixed-supported bounded endpoint matrix. The outgoing boundary
self-energy Sigma(E) is analytic near -2, with Sigma0=Sigma(-2),
Im Sigma0<0 and 1+Sigma0 bounded away from zero. These assumptions are
satisfied by the previously specified slow-host continuation; they are not
asserted for an arbitrary microscopic environment.

With alpha1 the first positive Airy zero and a0=Sigma0/(1+Sigma0), the simple
pole obeys

    E=-2+alpha1 epsilon^2+f(2+a0)+lambda^2 c+O(epsilon^4).

The proof (`outputs/neutral_continuation4_review_2026_10_18/proofs/RANGE_TWO_AIRY_PROOF.md`)
starts from the exact nearest-neighbor Bessel boundary equation

    J_nu(2/f)+Sigma(E) J_(nu+1)(2/f)=0,
    nu=-(E-2f)/f.

Uniform complex turning-point asymptotics from
[DLMF10.19.8](https://dlmf.nist.gov/10.19.E8) and
[DLMF10.20](https://dlmf.nist.gov/10.20) give the nearest-neighbor root with
O(epsilon^4) error. On a contour of radius proportional to epsilon^2, the
full resolvent is O(epsilon^-2), while each endpoint resolvent vector is
O(epsilon^-1/2). The non-Hermitian rank-one projection is treated as a Riesz
projection, not as a positive probability.

Since lambda^2=8epsilon^3, bounded range-two perturbation changes the energy
by lambda^2 c+O(epsilon^4). Localized contour estimates preserve the endpoint
projection O(epsilon^3), allowing energy-dependent Sigma to be restored with
only O(epsilon^5) additional error. Independent
Bessel (`outputs/neutral_continuation4_review_2026_10_18/proofs/INDEPENDENT_RANGE_TWO_BESSEL.md`)
and perturbation (`outputs/neutral_continuation4_review_2026_10_18/proofs/INDEPENDENT_RANGE_TWO_PERTURBATION.md`)
checks pass.

In original units this gives

    E_phys/Jz = 8-6lambda^2
      +alpha1 lambda^2 (lambda^2/8)^(2/3)
      +lambda^4[109/96+(2+a0)/8]+O(lambda^(14/3)),
    Gamma = (-Im a0)/4 Jz lambda^4+O(Jz lambda^(14/3)).

For the stated host, the real fourth-order coefficient is1.35046015003 and
the leading width coefficient is0.11360791220. The already controlled
corrected-fast boundary contribution is holomorphic and O(lambda/log(1/lambda))
on a depth-f disk around this pole. Its physical shift is O(Jz lambda^5/log),
smaller than the displayed remainder. Uniform holomorphy on that disk is
needed; a pointwise estimate would not suffice.

## Other long arms are closed channels at this energy

Fix all three center-of-mass momenta to zero. In the compact four-wall,
even-longitudinal-plane-parity sector, retain both short-length hosts and
the adjacent and axial-distance-two long arms. Let F denote the remaining
arms of length at least three. Their exact second-order operator is -4I;
there is no first- or second-order coupling to the retained channels.
The diagonal two-step XY/YX endpoint paths cancel.

The all-length structural proof (`outputs/neutral_continuation4_review_2026_10_18/proofs/FROZEN_ARM_ELIMINATION_PROOF.md`)
and independent check (`outputs/neutral_continuation4_review_2026_10_18/proofs/INDEPENDENT_FROZEN_ARM.md`)
give, at any fixed order m>=4 in the zero-block local homological convention,

    H_F/Jz = 8-4lambda^2+lambda^4 s_r(lambda) ell+B_F(lambda),
    s_r(0)>=3/32, ||B_F(lambda)||<=C_m lambda^3.

Connected finite support makes the slope positive uniformly in separation
for sufficiently small lambda at fixed m. Thus the F spectrum lies above
8-4lambda^2-C_m lambda^3, separated from the slow pole region near
8-6lambda^2. The cross-channel coupling starts at lambda^3 and has finite
support in the fixed momentum fiber. Its Schur contribution is therefore
finite-rank O(Jz lambda^4), with energy derivative O(lambda^2).

Finite rank is a fiberwise statement, not a claim over all untranslated
states. The possible O(Jz lambda^6) pole effect requires stability of the
retained host matching and is not concluded merely from this norm bound.
Higher coefficients are not replaced by chosen values.

## Numerical controls and remaining work

The Airy runner uses a cutoff that grows as
(18+4 log(1/lambda))/epsilon and compares a20% larger cutoff for
lambda=.2,.1,.05,.02,.01,.005. At .005 the real coefficient is1.35025035,
the width coefficient is0.11359639, and the scalar Schur residual is below
4.2e-12. These finite controls supplement the infinite-arm proof; the
residual is not a certified pole-error bound. The closed-arm runner checks
six exact K2 examples and the minimum six changed plaquettes.

The full retained-channel outgoing resolvent, complete microscopic
remainder-to-pole transfer, original readout residue accuracy, state
selection, and source/detector/cosmological identification remain open.
The mass still starts at8Jz; large internal extent has not produced a light
cosmological mediator. No observed value is fitted or independently tested.

## Current source and execution boundary

The complete live mathematical sources are listed in the primary's literal input closure. Historical reviewer dispositions and saved numerical results are provenance, not current evidence. The primary computes its declared finite controls in a fresh preserved temporary directory, enforces its aggregate wall-clock cap before scientific imports, and streams partial diagnostics. Frozen native coefficient tables are explicitly labeled input checks, not newly enumerated paths. Distinct primary assertion groups are counted; helper assertions are additional uncounted fail-closed checks. No audit status or physical primitive is introduced.
