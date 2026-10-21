# A controlled envelope for the bulk pole component

**Status:** bounded-support.
**Claim type:** bounded_theorem.
**Primary runner:** [scripts/native_pole_envelope.py](../scripts/native_pole_envelope.py)

The outgoing compact-mode contribution has a controlled spatial envelope
on its lifetime scale, even though pointwise derivatives of the exact
coefficient pole remain uncontrolled. This is a theorem about a defined
component of the response, not a physical particle probability or a proof
that it dominates the full microscopic signal.

## Derive the smooth fourth-order momentum coefficient

Use the supplied Hamiltonian and the [bulk COM pole/readout construction](NATIVE_BULK_COM_PROPAGATION_NOTE_2026-10-18.md).
Native fourth-order endpoint coefficients are 19/64 for one-site growth
and -13/256 for two-site growth; the two-end combined motions cancel
against folded terms. The long-arm diagonal is ell/8+29/192.
Opposite-end Bloch phases therefore yield, with gamma=cos(p/2),

    V4(p)=29/192 I+(19/32)gamma T-(13/128)cos(p)(S^2+S*^2),
    c(p)=29/192+(19/16)gamma-(13/64)cos(p).

The connected support classification covers all sufficiently long arms;
short intervals remain finite boundary terms. The native coefficient
c(0)=109/96 is recovered. No kinetic or potential term is added.

The previous uniform real-momentum Airy estimates now refine the pole to

    E_lambda(p)/Jz = 8+lambda^2 e2(p)+lambda^(10/3)e10(p)
                       +lambda^4 e4(p)+O_m(lambda^(14/3)),
    e2=-4-2gamma,  e10=alpha1 gamma^(1/3)/4,
    e4=c(p)+(2+a_p)/8,  g(p)=-Im(a_p)/4>0.

The original Fourier readout residue satisfies
r_lambda(p)=Res(C_p)/lambda^6 -> R(p) uniformly near zero momentum.
These are the same fixed-order coefficient poles and original readout;
the failed complex-momentum derivative extension is not being assumed.

## Use a bounded multiplier comparison instead of differentiating an error

Let f be a fixed square-integrable momentum profile with compact support
in that neighborhood. Define the pole-component kernel on integer
longitudinal source/readout displacements x by

    Psi_lambda(x,t)=integral dp/(2pi) f(p) r_lambda(p)
                                      exp[ipx-i E_lambda(p)t].

The Fourier convention gives
sum_x |Psi(x,t)|^2=integral |f r|^2 exp[2t Im E(p)] dp/(2pi).
Internal half-integer interval centers are a fiber gauge; x labels the
integer bond-center readout displacement. Take t=T0/(Jz lambda^4) with
fixed T0>=0. Replacing the pole by the smooth displayed expansion and
r_lambda by R gives Psi_app, with

    ||Psi_lambda-Psi_app||_l2
       <= C_T0 ||f||_L2 [sup|r_lambda-R|+O_m(lambda^(2/3))] = o(1).

The proof uses Parseval and the uniform energy error multiplied by time.
Even the rapidly varying fast-channel correction O(Jz lambda^5 log(1/lambda))
has vanishing phase error O(lambda log(1/lambda)). No derivative of that
correction is needed.

Define the unnormalized squared-kernel characteristic transform

    Chi_lambda(k)=sum_x exp[ik lambda^2 x] |Psi_lambda(x,t)|^2.

Exact Fourier translation, followed by differentiation only of the smooth
approximation, gives

    Chi_lambda(k) -> integral dp/(2pi) |f(p)R(p)|^2
                         exp[-T0 g(p)] exp[ik T0 sin(p/2)].

This is a weak transport limit in the scaled coordinate lambda^2 x for
the defined pole-component intensity. Its total mass decays. It is not a
normalized probability, and normalizing it would still not identify a
physical particle distribution.

## Evidence and remaining obstacle

The root proof (`outputs/neutral_continuation4_review_2026_10_18/proofs/POLE_ENVELOPE_PROOF.md`),
independent native fourth-order check and independent multiplier check
separate coefficient derivation from envelope analysis. FFT controls test
the approximate envelope and its weak limit on two grids. A deliberately
rapid phase perturbation tests the multiplier bound only; it is not
represented as an actual native correction. Host coefficients are
interpolated numerical development data, not empirical inputs.

The full response contains continuum background and fine structure.
Neither this envelope nor the smooth-window microscopic comparison
establishes pole dominance, a full-H resonance, a ballistic microscopic
particle, Lorentz invariance, a cosmological state or a universal detector
coupling. The next obstacle is extracting a controlled real-axis signal
while retaining that background. No observation is calibrated or tested.

## Current source and execution boundary

The complete live mathematical sources are listed in the primary's literal input closure. Historical reviewer dispositions and saved numerical results are provenance, not current evidence. The primary computes its declared finite controls in a fresh preserved temporary directory, enforces its aggregate wall-clock cap before scientific imports, and streams partial diagnostics. Frozen native coefficient tables are explicitly labeled input checks, not newly enumerated paths. Distinct primary assertion groups are counted; helper assertions are additional uncounted fail-closed checks. No audit status or physical primitive is introduced.
