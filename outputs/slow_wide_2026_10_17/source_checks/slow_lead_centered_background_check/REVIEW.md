# Distinct check of centered background subtraction

Disposition: supported as a conditional bound on the represented nonemitter finite coordinates and complete closed tails. No mathematical correction is required. The source proves B_I(t)<.000250 at the stated wide point for t>=1e15, conditional on the existing full resolvent and recovery interfaces. It does not by itself supply a new complete-state or finite-apparatus theorem.

Target: `slow_lead_centered_background/PROPOSAL.md`, SHA256 `7b585c9b5d3ef6ece111b9009dfb3f7f92c1aa044f3d7cad2c8d5d3dab2b02aa`.

## Exposure, source coverage and status

I read the complete new root-authored proposal and reconstructed its scalar substitution, product integration by parts, whole-line Fourier evaluation, cutoff tails and numerical enclosure. I did not author this proposal. I authored several gate, endpoint, scalar and outgoing ancestors and the earlier sharp/direct background arguments; I checked the wider derivative and complete composition. This is therefore a distinct source-exposed check with common ancestry, not a blind check or independent recertification of my own components.

The wider endpoint, derivative, complete composition and onset identities were fully read and checked or refreshed in the immediately preceding coherent tasks and are reused at the exact identities below. The source's statement that the wider composition was under review records drafting status: that composition now has completed review8675ccad, but this new centered argument is not justified by that review. No pending prepared-mass refinement is used here.

Only this report was written. No scientific runner, numerical integral, sweep, solver, delegation, W/Git/PR, publication, checkpoint, prompt or model change occurred. Original source/calibration, exact coefficients and physical identification remain conditional premises.

## Full8 replacement before selecting reference inputs

The starting column -kappa L Tactual Vseed has all nonemitter output rows. The actual full8 subtraction Tactual-Tref must be paid before restricting to the convenient diagonal reference. Its two-window/two-lip integrated norm is bounded by2kappa L0 eta, with L actual throughout. This uses the full resolvent comparison, not merely its imaginary part or a prepared density estimate.

After that replacement, Tref is diagonal in the fixed B eigenbasis. Vseed excites only the two vacuum directions per parity. On each physical window exactly one is the selected reference channel and the other is gap-separated. The six other reference coordinates have zero prepared input at this stage; this does not discard actual complementary output or any part of the already-paid actual resolvent error. The projector for the selected input is fixed on each window, so it does not differentiate. The arbitrary old-input and passive-reference operator contract remains intact.

## Scalar substitution and subtraction estimate

Writing r=sqrt(delta^2+gamma^2), the resolvent subtraction gives exactly

    |Tref-Tlor|=gamma |w-i|/(|delta+gamma w| r).

With |w-i|<=|delta|/(2j cos h) and |delta+gamma w|>=.9999r, the proposed coefficient gamma/j is conservative because 2*.9999*cos h>1. The same argument holds by conjugation on the lower lip. Integrating |delta|/(delta^2+gamma^2) over[-d,d] gives log(1+H^2). Two lips and two windows against the Stone factor1/(2pi) produce the prefactor2kappa L0/pi in Bscalar. This is a real-band norm comparison; no actual-source analyticity is used.

On one lip and selected input define DeltaL(delta)=L(delta)-L(0). The supplied Hilbert-space-valued differentiability gives ||DeltaL||<=M|delta| and ||DeltaL'||<=M. Consequently

    ||(DeltaL/(delta±i gamma))'||
       <=M/r+M|delta|/r^2.

The two boundary terms are bounded by2Md/r_d. The integrals of the derivative terms are2M asinh H and M log(1+H^2). Real-energy integration by parts and the same four lip/window terms therefore give exactly Eq.(2). It is valid for independent L(0) on every lip, window and sector. It neither equates those centers nor replaces an actual derivative bound by a value bound.

The earlier L0/gamma loss is absent because the derivative of the resonant denominator now multiplies a function vanishing at delta=0. Its weighted numerator is bounded by M|delta|. This replaces that loss by M times logarithmic integrals; it does not show that M is small or eliminate the derivative premise.

## Whole-line comparator and oscillatory tails

For t>0 the scalar integrals, understood as oscillatory improper limits, are

    integral_R e^(-it delta)/(delta+i gamma) ddelta
        =-2pi i e^(-gamma t),
    integral_R e^(-it delta)/(delta-i gamma) ddelta=0.

Closing in the lower half-plane is clockwise. Only the upper-lip denominator has a pole there, with the displayed negative sign. Jordan decay is applicable for this rational integrand at fixed t>0. One may equivalently use convergence regularization followed by the oscillatory improper limit. These statements do not extend actual L or a physical spectral density outside its band.

For each individual tail, integration by parts gives a boundary magnitude at most1/(dt), and the derivative integral contributes at most another1/(dt), since |(delta±i gamma)^-2|<=delta^-2 for |delta|>=d. Thus the pair of tails costs4/(dt) per lip. The boundary terms at infinity vanish. This is a bound on the oscillatory tail integral, not a claim of absolute integrability of1/|delta±i gamma| on the line.

For each window the center contribution on the full line is therefore at most kappa L0 exp(-gamma t), irrespective of the unrelated lower-lip center. Two windows give2kappa L0 exp(-gamma t). Four lip/window tail contributions, each multiplied by kappa L0/(2pi), give8kappa L0/(pi d t). Eq.(3) has precisely these factors. Common physical window phases have unit modulus and are retained until these bounds are taken.

## Other prepared reference channel

The complementary prepared reference scalar on a window has norm<=6 and derivative<=37. Its product with actual L has derivative norm<=6M+37L0. Integration over length2d and the two endpoints gives12L0+12dM+74dL0. Two lips and two windows again yield2kappa/(pi t), exactly Eq.(4).

This is not an assumption that the opposite-window reference resolvent vanishes: only its density vanishes there, while its real resolvent enters this product. The conservative triangle sum covers arbitrary superpositions of both prepared inputs without requiring orthogonal output error ranges. Parities combine by maximum; orthogonal record-X outputs with initial weights1/sqrt2 preserve the same bound. Passive-reference tensoring is automatic for these operator norms.

## Arithmetic at the same wide point

Using the previously checked enclosures M<6.49e17, eta<5.3e-6, gamma/j<1.4e-11,2.15e-8<d<2.4e-8, asinh H<15 and log(1+H^2)<28:

- The bracket2d/r_d+2asinh H+log(1+H^2) is strictly below2+30+28=60. Thus Bvary<(2*6.49*60/3.14)*1e-6<.000249.
- The full8 replacement costs<2*.004*5.3e-6=4.24e-8.
- Bscalar<(0.008/3.14)*1.4e-11*28<1.1e-12.
- Gamma T>100/3>33 and e>2 give the center exponential<.008*2^-33. Its tail contribution is<.032/(3.14*2.15e7). Their sum is<4.9e-10.
- The dominant wrong-window bracket term is12*(2.4e-8)*6.49e17=1.86912e11. Including4.8e6 and74*(2.4e-8)*4e5 and multiplying by2e-23/3.14 gives<1.3e-12.

Adding these relaxed ceilings gives less than .000249042893<.000250. Every time-dependent term decreases as t increases beyond T; the two replacement terms remain constant. Therefore the bound is uniform for t>=1e15 for this infinite represented background component. No new parameter point, propagation experiment or mass value was introduced.

## Meaning and limits

Taking the minimum of this envelope and the earlier background estimate is valid wherever both hypotheses hold. The improvement is in the represented nonemitter finite/closed component only. A later complete composition must still add the separately bounded represented emitter, both actual traveling terms, target normalization, finite-cap transfer and exactly one global omitted state. This report does not substitute a future density-only improvement for the full resolvent eta used above.

The physical common scalar, literal K/W and all actual window phases remain in the decomposition. No source phase alignment, output-coordinate compression or permanent-hold claim follows. The argument concerns ordinary unitary dynamics with a supplied initial seed and a single eventual comparison; it introduces no measurement, stopping or irreversible-latch rule.

## Exact reused identities

- Wider complete source `5275860cb241a358d53460e88183879009a9899de7172c7c3b2e75629eb42fba`; completed review `8675ccad6f0b6b09142b09d65f909d3322ff0bb58f16ab739fe1eecd930de383`.
- Wider endpoint source `c4c99408686166ba4d80bc973f5c22afdd1185bbf38e4539512dc26afd5cd5e3`; review `c6cc2ed747956e70bba1a7af3a5d65d3d36a7f708367727cb6f5e8a74386feb5`.
- Wider derivative source `c2b9d6917db45faa1e9974cb69ef9bc683f45147bcb47b3588df36e94b630f2a`; review `c74a8118cccafe3e64dc6f4aa499fc7fa9abb194dae5cedbb2c253fb06054c79`.
- Onset source `c590e093e7a4ca6abc1e147414f5ee5b08e725fa1a881b266fae7271b56e0d46`; review `5f8b8a3b4aea4008c07d9d8e59b53a7c58bf4cb0deead4d7da66be84a2c4a32b`.

Paths are the corresponding sibling directories identified in the target proposal. Original canonical calibration/source pin remains `71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff`. Hashes identify evidence, not mathematical proof or independence.
