# Independent displaced-Floquet review

The proposed displacement and induced-charge-drive sign are correct for the supplied infinite oscillator with Ω≠w. The completed original and displaced calculations agree in their selected avoided-gap minimum. An independent continuous-time monodromy computation reproduces the displaced result. No consequential algebra or numerical discrepancy was found at this fixed ng=0 point. This is a selective exploratory check, not an audit, refit, experimental line-center determination, or certified infinite-cutoff bound.

## Analytic derivation and exact scope

Use cyclic GHz units, so the Schrödinger generator is 2πH/h. Set θ=2πwt and write the state as ψ=D(α)χ, with D(α)=exp(αa†−α* a). Then D†aD=a+α, and cancellation of linear cavity terms requires

`i dot(alpha)/(2π) = Ω alpha + D cos(theta)`.

The supplied periodic solution

`alpha = −D/2 [exp(−iθ)/(Ω−w) + exp(iθ)/(Ω+w)]`

satisfies this equation. Its imaginary part is `D w sin(θ)/(Ω²−w²)`. Consequently P=i(a†−a) transforms to P+2 Im(alpha), and GnP generates the **positive** charge term

`F n sin(theta), F=2 G D w/(Ω²−w²)`.

The charging potential and charge operator commute with the displacement. The construction is exact for the supplied oscillator and coupling, not an expansion in D. It is singular at Ω=w: a bounded periodic displacement of this form does not exist there. The checked optimization interval stays away from that singularity.

The residual scalar is `s(t)=D cos(theta) Re(alpha)` in this displacement convention. Its mean is

`mean(s)=−D² Ω/[2(Ω²−w²)]`.

Its oscillating part can be removed by a periodic scalar phase. Removing its mean requires a nonperiodic global phase and shifts every quasienergy equally; therefore “Floquet equivalence” must mean equal quasienergy **differences**, or absolute quasienergies after adding this common shift. At the final displaced minimum, the mean is −0.193009685053224 GHz. The two original-minus-displaced quasienergy offsets are −0.193009684908737 and −0.193009685106228 GHz, consistent with it at sub-Hz scale and the slightly different fitted frequencies.

For the e^(imθ) Sambe convention the diagonal is Em+mw. A sine drive has the upper sideband matrix element +iFQ/2 and the lower −iFQ/2, matching `1j*(T-T.T)`. The original cosine construction likewise uses equal real sideband couplings DX/2. The quadrature convention in drive_correction_probe.py remains GnP with an X drive, as checked in DRIVE_CORRECTION_REVIEW.md.

Exact oscillator displacement is not an exact unitary identity between arbitrary finite photon/Sambe truncations: finite ladder matrices do not obey the full canonical commutator, and displacement mixes photon numbers and sidebands. Agreement must therefore be checked as cutoffs grow; the scripts correctly describe finite-cutoff diagnostics.

## Branch selection and minimum definition

Both author scripts select the two eigenvectors with greatest summed projection onto |g,m=0> and |e,m=−1>, then minimize their unwrapped quasienergy separation over base±35 MHz. This is a local, specified avoided-gap diagnostic. Projection weights depend on representation; 0.94446 in the displaced and 0.79274 in the original representation are not contradictory. A periodic displacement also changes the Floquet mode projections.

This selector is not general branch continuation and can switch eigenvectors or pick Floquet replicas in other regimes. `minimize_scalar` success does not prove global minimality or branch continuity. At the checked point, the high pair weights, agreement of the two representations, and independent 15-point interval scan support the intended smooth avoided crossing. No branch-switch discrepancy was found here. Future reuse near additional resonances should explicitly track the pair and inspect the gap curve. There is no dissipative preparation/readout calculation, so this minimum cannot be identified automatically with a spectroscopy peak.

## Independent numerical evidence

`independent_displacement_check.py` reuses the preserved independent direct charge–photon construction from `independent_drive_check.py`, not either author's Floquet or system builder. It uses charge cutoff 20 and six photon states, constructs the charge operator in its own dressed basis, and integrates the displaced time-dependent Schrödinger equation over θ∈[0,2π]. Eigenphases of that monodromy matrix supply quasienergies. Thus it has **no Sambe sideband cutoff**. Frozen parameters and pulse settings are shared inputs, and the author outputs were visible before the check; no measured targets or fit objective enter this computation.

Two retained-level/ODE settings gave:

| Retained levels | ODE relative tolerance | Minimum shift (MHz) | Gap (GHz) | Unitarity defect, spectral norm |
|---|---:|---:|---:|---:|
| 24 | 1e−10 | 6.181682979255143 | .0513052130579125 | 9.33e−10 |
| 40 | 2e−11 | 6.181682972797198 | .05130521306240526 | 2.94e−10 |

The final frequency is 6.727033055704754 GHz, with distinct selected eigenphases near −.0232161893031803 and +.0280890237592249 GHz. Their time-zero pair projections are .943626 and .968811. The 15-point scans from −35 to +35 MHz detuning show a single resolved valley; scans and solver diagnostics are preserved in JSON. A finite scan is not a rigorous global-minimum certificate.

The author's completed displaced 70-level/six-sideband output gives 6.181682996411198 MHz: about **0.024 Hz** difference in frequency from the independent ODE result. Its gap differs by about .00035 Hz. The author's original 90-level/eight-sideband output gives 6.181683410298788 MHz and agrees with the displaced frequency within **.414 Hz**, and with its gap within **.198 Hz**. The previous original 70-level result changed by about 13.26 Hz in frequency; this illustrates the value of its cutoff extension. I inspected the full current scripts and completed JSON outputs; no claim about unseen intermediate runs is made.

## Interpretation and remaining limits

The converged diagnostic is approximately **+6.181683 MHz**, compared with **+8.508821 MHz** from the earlier second-order diagonal Floquet correction. The approximately 2.327138 MHz difference matters for any MHz-level downstream use. The finite-drive avoided-gap minimum is a stronger closed-system calculation than the second-order diagnostic, but remains a specifically defined observable proxy. Neither cutoff stability nor agreement between representations establishes an error bound against the actual dissipative line center, omitted circuit physics, pulse-area assumptions, frequency-dependent transfer, or fitted-parameter uncertainty.

The check covers the supplied ng=0 far point and full drive amplitude. It does not independently reconstruct the entire author amplitude sweep, certify all charge/photon/retained-level tails, refit calibration, or resolve state assignment. No author sources or other checkouts were modified. Preserved independent code, JSON and log are evidence of the numerical work actually performed.

## SHA-256 source and evidence identities

- `displaced_floquet.py`: `b5146f47f95e30e9312df7c608a3433247391cd9ff45f49ae7e73488fbb046b3`

- `displaced_floquet.json`: `ee7d67762611b6302ef400caf86974dd49cc0c30985236feef3ccdc3c3192b32`

- `displaced_floquet.log`: `52ee6a1aec0c3c051a704d9ccd834a42756300f26bf92cc9ac25179050328af5`

- `floquet_system_cutoffs.py`: `a6795d606d0a9ffa10779ab3953411928360ec51d38089d233be589ae6609a80`

- `floquet_system_cutoffs.json`: `277cfd3e3680bf2edb87ecfd9808fed9968b68c19ec5aab5a52d47b35524fb8a`

- `drive_correction_probe.py`: `3fd367d915b63c53c79d1465111d9fd6a143128545c6cbd7e43e9ec9d7379246`

- `drive_correction_probe.json`: `1c754a5f3f5b8aa81f38914d04901e70b6e4b4bc40af776211e14073703cc280`

- `resonator_joint_fits.json`: `2682d11612c900f7c521ea462bc724116e28eb61a6eb4ef9424de6b562828d3e`

- `far_fit_exploratory.json`: `cf8f416eba6cd3e646e8bd5557ebd10f58f644968ffae6f10ee2e0e1c0dd3815`

- `independent_drive_check.py`: `54a4dc66a2a064ef15f7d85fbeea4ee0b90eef0c69829991791bf47064239847`

- `independent_displacement_check.py`: `68fab6d227398cf161be118739bce30255b719056f99700b48044f9154be63e2`

- `independent_displacement_results.json`: `05a980f4a18e8c50038c1c7044249b3df7031009388364d97bc5fb2bfd9bee22`

- `independent_displacement_check.log`: `d8c872d28cf3005a2e34fcc30f92cab093dbd840409ef9f66ee853d0a43e54f9`
