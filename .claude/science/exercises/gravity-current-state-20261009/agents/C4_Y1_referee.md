# VERDICT: NOT CONFIRMED

The central non-Huygens mechanism is substantially correct, but the claimed observational **FAIL** does not follow from the available all-frequency variance bound. Under the FIXED readings, RY remains **INCONCLUSIVE, strongly leaning FAIL**.

1. **Non-Huygens noise and \(s_{\rm eff}\): confirmed within RL4’s bounded scope.**

   For a realization, \(H_P(x,y)\) is defined throughout \(y\prec x\); it is the ensemble mean that approaches the Huygens-supported propagator. RL3b’s second-moment/chaos formula and RL4’s positive ladder therefore genuinely permit growing variance for a source element strictly inside the past cone (`C4_RL3b_report.md:33`, `C4_RL3b_report.md:44`, `C4_RL3b_report.md:75`; `C4_RL4_report.md:129`).

   For an emission occurring \(\Delta t\) before the retarded time,
   \[
   \tau_e^2=(D+c\Delta t+s_e)^2-D^2,
   \]
   so \(\tau_e\simeq\sqrt{2D(c\Delta t+s_e)}\) when the time depth is small relative to \(D\). Thus writing \(s_{\rm eff}=cT_{\rm emit}\) is legitimate shorthand for a history composed of separately finite, regularly edged emission pulses. At the end of an observing baseline, \(T_{\rm emit}\ge T_{\rm obs}\) follows geometrically (`Y1_report.md:69`, `Y1_report.md:81`).

   The qualification is essential: RL4 transfers the rate only to currents with a spacelike past edge and regular nonzero turn-on patch; it is not a theorem for arbitrary atomic emissions, Gaussian/edgeless histories, or stationary sources extending indefinitely into the past (`C4_RL4_report.md:183`, `C4_RL4_report.md:201`; `C4_RL4_referee.md:21`). Y1 labels the per-emitter applicability as merely argued (`Y1_report.md:74`).

2. **“Variances add”: correct algebra, but overstated terminology and cross-covariance estimate.**

   For independent uniform emitter phases,
   \[
   E_\theta\!\left|\sum_e a_e\phi_{e,P}\right|^2
   =\sum_e|\phi_{e,P}|^2,
   \]
   pointwise in \(P\). Averaging over \(P\) then gives a sum of nonnegative **field variances**, so \(N\ge V_e\) for every emitter. Shared-sprinkling cross terms vanish exactly after the phase average (`Y1_report.md:50`, `Y1_report.md:58`). This is mean excess intensity, not “intensity variance,” and identifying the phase average with a detector time average still assumes ergodicity (`Y1_report.md:45`, `Y1_report.md:193`).

   For fixed phases, Minkowski supplies only an upper bound; it does not exclude destructive covariance or provide \(N\ge V_e\) (`Y1_report.md:63`).

   The claimed \(\sim10^{-40}\) cross-covariance suppression is not established for the full emitter covariance. RL3b proves \(O(1/(z|\Delta|))\) only for one displaced pair segment at fixed nonzero spacelike separation; timelike/null and near-null cases differ, and the all-orders transfer was only argued (`C4_RL3b_report.md:110`, `C4_RL3b_report.md:119`, `C4_RL3b_report.md:133`). Y1’s conversion of this into a full residue/correlation estimate is therefore heuristic, as it effectively acknowledges at `Y1_report.md:195`. This does not damage the independent-phase result because that result eliminates cross terms exactly.

3. **E-fold arithmetic: numerically correct, physically overinterpreted.**

   Independent reruns reproduced both stored outputs exactly. In particular,
   \[
   \epsilon=1.752\times10^{-63},\qquad
   \gamma_{\rm low}=0.628\,\frac{\sqrt\epsilon}{\ell_k}
   =3.327\times10^{-13}\ {\rm m}^{-1}.
   \]
   At 1 Gpc this gives \(\gamma\tau=4.526\times10^4\) for one second, \(2.54\times10^8\) for one year, and \(8.05\times10^{11}\) for \(10^7\) years (`y1_A_efolds.out:1`, `y1_A_efolds.out:16`, `y1_A_efolds.out:19`; `y1_B_observed_baseline.out:2`).

   These are **rate-exponent budgets**, not established finite-distance values of \(\log(N/S)\). RL4 proves a fixed-\(\epsilon\), asymptotic liminf rate but leaves the finite-source prefactor and onset at 1 Gpc open (`C4_RL4_report.md:224`; `TESTS.md:2023`). Y1’s claim that all relevant prefactors cost fewer than \(10^3\) log units is plausible but unproved (`Y1_report.md:153`). The observational “one e-fold” allowance is likewise recalled rather than derived (`Y1_report.md:142`).

   The lamp example also needs narrowing: one hour at 1 m gives only \(0.359\) e-fold under the proved \(c_{\rm low}\); \(1.56\) uses RL3b’s stronger node-ladder constant. One proved-rate e-fold occurs after roughly 2.8 hours (`y1_B_observed_baseline.out:9`). The \(\ell_k\simeq2.8\times10^{-15}\) m arithmetic is correct, but its collider exclusion remains conditional on transferring the collider form-factor bound to this photon operator (`C4_X1_report.md:67`, `C4_X1_report.md:89`).

4. **In-band fraction: this does threaten—and presently blocks—the FAIL.**

   RL4 bounds pointwise, all-frequency field variance. Lensing fluxes and VLBI constrain a band-filtered two-time observable. No lower bound on the variance surviving an optical or radio bandpass follows from the equal-time variance alone.

   The \(e^{-144}\) and \(e^{-10^2}\)–\(e^{-10^3}\) estimates use a rapidity/end-factor heuristic, not a calculation or lower bound for the temporal spectrum (`Y1_report.md:161`). Without the two-time covariance or an explicitly filtered chaos lower bound, the observable fraction could be much smaller or even spectrally absent. The huge exponent would overwhelm any *proved finite* \(e^{-1000}\) penalty, but no such finite lower bound was proved. Consequently the FIXED FAIL condition—noise exceeding what observed lensing permits—is not met (`TESTS.md:2072`).

5. **Fixed-reading verdict and near-no-go claim.**

   PASS is not established because the all-frequency edged-source rate is strongly unstable. FAIL is also not established because the detector-band fraction, finite-distance normalization/onset, and per-emission T′ bridge remain open. The correct fixed reading is therefore **INCONCLUSIVE, strongly leaning FAIL**.

   The proposed universal statement that every long-lived source fails is too strong. It additionally assumes independently phased finite-edge emissions, applicability of the scalar stable-layer result to the photon readout, a non-negligible detector-band fraction, a controlled finite-distance prefactor, and—if interpreted as an empirical exclusion—representative rather than rare-tail ensemble behavior. Edgeless histories are explicitly outside RL4’s theorem (`Y1_report.md:184`).

**Strongest correct statement:** Within the stable scalar layer-readout model, any individual finite emission current possessing a spacelike past edge and regular nonzero turn-on patch has an all-frequency ensemble field-variance rate governed by its full timelike separation from the observer, not merely its coherence length; for an emission \(\Delta t\) before the retarded time this gives \(\tau\simeq\sqrt{2Dc\Delta t}\), and independent phase averaging makes the corresponding unfiltered mean noise powers add. At \(\ell_k=7.9\times10^{-20}\,\mathrm m\), the resulting asymptotic exponent budget is \(4.5\times10^4\) already for one second at 1 Gpc. This is powerful evidence of an instability, but without a finite-distance normalization and a positive lower bound on the optical/radio band fraction it is not yet an observational lensing FAIL or a no-go theorem for every long-lived source.