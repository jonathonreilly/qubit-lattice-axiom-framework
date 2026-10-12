# Moving scalar currents and the Fein2019 interference observable

For an explicitly specified closed triangular pair of moving, rigid molecular currents, the common scalar vacuum at gravitational-strength universal coupling gives a visibility-loss upper bound of **4.20e-54** for a stipulated 1 nm Gaussian profile. The bound holds for every nonnegative, unit-total mass measure, including the campaign's gamma measure. It includes the longitudinal Doppler phase. It is **not the visibility predicted for the actual Talbot–Lau apparatus**: that requires a weighted sum over grating histories, internal states, source preparation and detector response. No new exclusion of a scalar force is obtained from this calculation.

The important bridge is a moving-source influence functional, not the static hold overlap. In the declared recoil-scale benchmark the factor proportional to molecular mass squared cancels the inverse-mass-squared recoil velocity. This makes the relevant small parameter proportional to the squared Planck-length/grating-period ratio.

All field, coupling, state, source-current and apparatus identifications below are conditional physical hypotheses. The work changes no axioms or audit standing. The protocol was frozen before the numerical calculation in [FROZEN_PROTOCOL.md](FROZEN_PROTOCOL.md). The public interference result was already known.

## Primary-source readout and inputs

The source is [Fein et al., DOI 10.1038/s41567-019-0663-9](https://www.nature.com/articles/s41567-019-0663-9). The accessible primary typeset-text [article copy](https://pub.math.leidenuniv.nl/~gillrd/Peking/Files/two-slit_expt.pdf) has an unfilled publication-date placeholder; it is not certified here as the final version of record. The [publisher supplement](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41567-019-0663-9/MediaObjects/41567_2019_663_MOESM1_ESM.pdf) is separately pinned. Relevant article pages and supplementary figures were rendered and visually inspected.

| Article input / role | Value or definition |
|---|---|
| Observable | Sinusoid amplitude/offset of dark-corrected laser-on/laser-off count ratio versus final-grating displacement |
| Control | Diffraction laser chopped at 2 Hz; typically 5 s on and 5 s off per position |
| Gratings | Separation 0.98 m; period 266 nm; mechanical opening 43%, thickness 160 nm |
| Beam | Mean 261 +/-9 m/s; Gaussian width 52 +/-7 m/s; uncertainty from seven measurements |
| Source | 532 nm, <10 ns, 1 kHz, 1.8 mJ desorption; 500/400 micrometre collimation |
| Optical response | 532 nm; effective waist 690 micrometres calibrated with C60; absorption 1.6e-20 m² estimated; polarizability 1321 +/-18 cubic angstroms calculated |
| Detection | Electron-impact ionization; broad 30% mass-filter resolution |
| Reported result | 25 +/-3% visibility at 1.2 W; fitted theory scale 0.93 +/-0.06 |
| Figure errors | 68% sine-amplitude intervals; at least two scans per power point |
| Background context | 2e-8 mbar; molecular temperature below 1000 K; residual Coriolis, roll alignment and effective openings |
| Access | Underlying plot data available on request; no public count table found |

The supplement lists prominent masses 25390, 25853, 26312, 26777, 27239 and 27703 Da, with relative MALDI intensities 40, 72, 88, 100, 62 and 35. These are not a calibrated transmitted-beam likelihood. Supplementary Figs. 2–3 investigate detector fragmentation and source survival; the authors retain a recollection-contamination uncertainty. Fig. 5 checks the 266 nm component against the laser-off control.

The source's fitted scale is a calibration/reproduction datum. It is not a held-out scalar test. A complete mass/velocity/optical covariance, raw on/off counts and timing records were not available. Nor is there a measured three-dimensional molecular mass density or conformer/rotation ensemble to insert into a scalar form factor. The widths used below are explicit new profile assumptions.

## A probability map and its influence functional

Use natural length units `u=ct`, inverse-length mass parameter mu, and

\[
 d\nu(\mu)=\frac{\ell^s}{\Gamma(s)}\mu^{s-1}e^{-\ell\mu}d\mu,
 \quad \int d\nu=1,\qquad
 W^+(u,\mathbf x)=\int d\nu(\mu)\int\frac{d^3k}{(2\pi)^3 2\omega}
 e^{-i\omega u+i\mathbf k\cdot\mathbf x},\quad \omega=\sqrt{k^2+\mu^2}.
\]

The same positive measure generates the static scalar interaction. With

\[
 g_A=\sqrt{\frac{4\pi G}{\hbar c}}\,\alpha m_A,
 \qquad
 V_{AB}(r)=-\frac{G\alpha^2m_Am_B}{r}
 \left(\frac{\ell}{\ell+r}\right)^s,
\]

alpha=1 is the supplied strength normalization; s and ell are not selected by this experiment. Extended sources require convolution with their mass densities. An externally sourced coherent field has the same connected vacuum covariance but a nonzero mean and hence can change interferometer phases. A bound on connected vacuum damping says nothing by itself about that force/phase response.

For a prescribed pair of branch currents, write

\[
 J_\pm(u,\mathbf x)=g_A\chi_\pm(u)
 f_\pm(u,\mathbf x-\mathbf X_\pm(u)),\quad \int d^3x\,f_\pm=1.
\]

This is the leading nonrelativistic scalar-charge current. For a point scalar charge the relativistic action is `-g_A integral d(tau_length) Phi(X)`: the lab-time current has a proper-time factor `1/gamma`, with the appropriate transformed spatial profile. The benchmark is an explicitly stipulated nonrelativistic rigid profile; the real beam speed/c is 8.71e-7. The branch speed/proper-time factor is common to the two symmetric legs and at most one, so omitting it gives a conservative amplitude bound for those currents. A fully time-dependent, rotating or internally excited density belongs in the general current, not in an unchanged static form factor.

Let `Delta J=J_+-J_-`, `Jbar=(J_++J_-)/2`, `N=Re W+`, and `G_R=i theta(u-u')<[Phi(u),Phi(u')]>`. For a centered Gaussian field initially specified independently of the controlled branch label,

\[
 \mathcal F[J_+,J_-]
 =\exp\left[i\int\Delta J\,G_R\,\bar J
              -\frac12\int\Delta J\,N\,\Delta J\right],
\]

with an additional `-i integral Delta J <Phi>` for a nonzero mean. The damping exponent has the positive on-shell form

\[
 \chi[J_+,J_-]=\frac12\int d\nu(\mu)
 \int\frac{d^3k}{(2\pi)^3 2\omega}
 \left|\int du\,d^3x\,\Delta J(u,\mathbf x)
 e^{i\omega u-i\mathbf k\cdot\mathbf x}\right|^2. \tag{1}
\]

It is the covariance norm of the **whole difference current**. The environmental overlaps are a unitary Gram kernel, so inserting them into the prepared system's history sum preserves a positive normalized probability map. Replacing (1) by an arbitrary positive damping rate need not preserve this physical construction.

A suitable apparatus count model is

\[
 R_P(X_3)=R_{\rm bg}+\int dm\,dv\,d\zeta\;w(m,v,\zeta)
 \operatorname{Tr}\!\left[M_{X_3}\,U_P
 (\rho_{m,v,\zeta}\otimes\rho_\Phi)U_P^\dagger\right], \tag{2}
\]

where preparation and the first mask, the optical grating (including absorption), the last-grating POVM, detector efficiencies and the internal label zeta are included explicitly. Losses are outcomes of a full instrument; conditioning on transmitted counts is done only after normalization. Expanding (2) in COM histories supplies (1) for each pair, with the corresponding phases and weights. Counts are then combined into the actual on/off ratio and sinusoid fit. A Talbot–Lau visibility is generally not `V0 exp(-chi)` for a single guessed pair, nor can intervals of a vacuum with memory be reset to independent channels without another assumption.

For microscopic mass density, a rigid approximation gives

\[
 F(\mathbf k)=m_A^{-1}\int d^3r\,\rho_A(\mathbf r)e^{-i\mathbf k\cdot\mathbf r}.
\]

Conformer/rotational distributions, atomic positions, nuclear profiles and internal dynamics can change this function. Resolving individual constituents changes coherent mass-squared addition. If the density is an operator, internal histories must also be summed/traced; the molecule's temperature does not simply become the scalar field's temperature. A warm internal molecule and a scalar vacuum are different state specifications.

## Closed moving-current benchmark and bound

Stipulate a fixed common profile satisfying `|F(k)| <= exp(-a² k²/2)`, a common longitudinal drift beta, and the symmetric closed paths

\[
 \mathbf X_\pm(u)=\big(\pm b\min(u,S-u),0,\beta u\big),
 \quad 0\le u\le S,\quad b=\Delta_{\max}/S.
\]

They coincide before and after the interval. Their hard velocity turns are an idealization requiring the finite source profile; the actual optical interaction/switching must replace them in an apparatus calculation. The Gaussian has tails and is not an exact compact molecular density. A common pre-existing coherent dressing changes mean-field phases, not the connected covariance in (1). Branch-dependent initial dressing/correlations are a different preparation and must be modeled. Creating separated charges suddenly and holding them is not this preparation.

With `Omega=omega-beta*k_z`, `K=b*k_x`, the exact time transform of the difference of these two paths is

\[
 D_{\mu\mathbf k}
 =-\frac{4iK\,e^{i\Omega S/2}}{\Omega^2-K^2}
 \left[\cos(k_x\Delta_{\max}/2)-\cos(\Omega S/2)\right]. \tag{3}
\]

Thus

\[
 \chi=\frac{g_A^2}{4}\int d\nu\int\frac{d^3k}{(2\pi)^3\omega}
 |F(\mathbf k)|^2|D_{\mu\mathbf k}|^2. \tag{4}
\]

The denominator contains the moving-source frequency, not a static spectrum transplanted along the beam. For subluminal constant motion, `omega-k dot beta` remains positive; the kicks and preparation supply the energy for a nontrivial vacuum transient. In the reflection-symmetric benchmark the retarded self-phase cancels between the mirrored branches. Generic external-source phases need not cancel.

Set `A=(1-|beta|)^2-b^2>0`. The inequalities

\[
 |D|\le\min\left(\frac{|K|S^2}{2},\frac{8|K|}{\Omega^2-K^2}\right),
 \quad \Omega^2-K^2\ge A\omega^2,\quad \omega\ge k
\]

follow from `|cos x-cos y| <= min(2, |y²-x²|/2)`. Angular integration and `integral dnu=1` give

\[
 \chi\le\frac{g_A^2b^2}{24\pi^2}
 \int_0^\infty dk\,e^{-a^2k^2}
 \min\left(\frac{k^3S^4}{4},\frac{64}{A^2k}\right)
 \le\frac{2g_A^2b^2}{3\pi^2A^2}
 \left[1+2E_1\!\left(\frac{16a^2}{AS^2}\right)\right]. \tag{5}
\]

The split occurs at `k=4/(S sqrt(A))`; the lower integral was bounded by dropping its Gaussian. `E1(z)=integral_z^infinity exp(-t)dt/t`. This is an analytic envelope for every unit-total positive mass measure; no numerical selection of s or ell is needed. A larger total spectral weight multiplies it and must not be hidden in the word gravitational-strength. The mass cutoff alone does not replace the spatial/temporal ultraviolet condition.

For the declared first-harmonic recoil scale,

\[
 T=2L/v,\quad S=cT,\quad
 \Delta_{\max}=hL/(m_Avd),\quad
 b=h/(2m_Acd),\quad
 g_A^2b^2=4\pi^3\alpha^2\ell_P^2/d^2. \tag{6}
\]

This triangular separation is also the argument appearing in the Markov localization response below. That does **not** make it the unique pair of paths representing the non-Markov quantum-field effect in (2).

The modal-mass/mean-speed benchmark gives `T=7.50958 ms`, `Delta_max=210.353 nm`, `b=9.34357e-14`, `g_A²=5.24494e-29`, and `g_A² b²=4.57895e-55` at alpha=1. The resulting conditional region is

| Stipulated Gaussian width a | Upper bound on chi and on 1-exp(-chi) |
|---|---:|
| 1 fm, separate ultraviolet-envelope diagnostic | 5.90646e-54 |
| 0.1 nm | 4.48209e-54 |
| 1 nm | 4.19722e-54 |
| 10 nm | 3.91234e-54 |

These values include the conservative longitudinal-Doppler factor A. They are analytic model bounds, not experimental error bars or full-apparatus predictions. Equation (6) removes the modal-mass dependence from the leading prefactor; changing the geometry, diffraction orders, source histories or current model can remove that cancellation. The dependence on the stipulated ultraviolet width is only logarithmic for these long-duration closed paths. Nothing here fixes that width from molecular size, and an internally evolving density is outside this rigid-current bound.

## An explicitly different Markov rival

A valid translation-covariant, completely positive Gaussian momentum-kick generator is

\[
 (\mathcal L\rho)(\mathbf X,\mathbf X')
 =-\lambda_0(m_A/m_0)^2
 \left[1-e^{-|\mathbf X-\mathbf X'|^2/(4r_C^2)}\right]
 \rho(\mathbf X,\mathbf X'),\quad m_0=1\;{\rm Da}. \tag{7}
\]

Its positive kick density is `lambda_0 (m/m0)^2 (r_C/sqrt(pi))^3 exp(-r_C² k²)`. This is the point-composite mass-proportional CSL convention, valid when the internal size is small relative to r_C; a finite density inserts `|F(k)|²`. It is also realizable by a classical Gaussian white random potential. Fringe attenuation alone does not distinguish those two interpretations. The covariance is Markovian and has a different frequency support from the vacuum in (1).

For the first harmonic at fixed mass and speed, the standard paraxial localization response has `Delta(t)=h min(t,T-t)/(md)` and

\[
 R_1=\exp[-\lambda_0(m/m_0)^2T\,H(\Delta_{\max}/r_C)],
 \quad H=1-\frac{\sqrt\pi r_C}{\Delta_{\max}}
 \operatorname{erf}\left(\frac{\Delta_{\max}}{2r_C}\right). \tag{8}
\]

The Markov step is essential. Equation (8) follows by integrating (7) and agrees with the convention of [Nimmrichter et al., arXiv:1103.1236v2](https://arxiv.org/abs/1103.1236v2), eqs. (3)–(4). The broader near-field formalism is [Hornberger, Sipe and Arndt, quant-ph/0407245v1](https://arxiv.org/abs/quant-ph/0407245v1). Neither equation is imported as a local-in-time approximation to the supplied vacuum.

| r_C | Modal benchmark R1 at lambda0=1e-8/s | Rate giving R1=0.5, per second |
|---|---:|---:|
| 10 nm | 0.951889 | 1.40577e-7 |
| 100 nm | 0.985421 | 4.71982e-7 |
| 1000 nm | 0.999802 | 3.50275e-5 |

At lambda0=1e-16/s the corresponding losses range from about 2e-12 to 5e-10. The half-visibility column is a **benchmark response threshold**, not a newly fitted experimental bound or a reconstruction of the paper's exclusion contour. It demonstrates a different possible scale and time/separation dependence. In a real experiment the harmonic coefficients must be averaged over mass, velocity and response, before taking their absolute value. Averaging attenuation factors alone can be wrong because different classes carry different phases.

There is an honest discriminator only for fixed physical families with calibrated backgrounds and controls. Additional white-noise attenuation of percent scale would not be explained by the alpha=1 rigid vacuum-pair benchmark; both a collapse generator and a classical white potential could explain it. The present fitted 7% scale deficit is not such a discovery and has identified apparatus explanations. A classical Gaussian process chosen to have the same symmetric covariance as the vacuum gives the same damping functional; the quantum retarded phase or a separate energy-exchange witness would be needed to go further.

## What the reported summary can and cannot constrain

Suppose, additionally, every relevant visibility is multiplied by a common `exp(-chi_extra)`, the remaining calibrated background factor B is independent and lies in [0,1], and the fitted scale f has a valid lower bound f_L. Then

\[
 f=B e^{-\chi_{\rm extra}}\ge f_L
 \quad\Longrightarrow\quad\chi_{\rm extra}\le-\log f_L. \tag{9}
\]

For an *illustrative Gaussian-summary assumption*, `.93-.06=.87` gives .139262 and `.93-1.96*.06=.8124` gives .207762. The quoted scale uncertainty is not supplied with a complete nuisance likelihood, and the vacuum need not act as a common multiplicative factor. These numbers are therefore labeled scenarios in the runtime JSON, not asserted confidence limits on the common scalar model. The published paper's own 50% criterion can be reported as its model-specific criterion; it cannot be applied to arbitrary currents or force laws.

The decisive next action is to specify independently measured mass/velocity detection weights, grating amplitude/phase/absorption maps, time-dependent molecular density and source preparation, then evaluate (2) with the full influence functional and the same on/off estimator. The optical-force/calibration parameters must have fixed roles before comparing an additional scalar response. Exact source data and uncertainty information are needed for a likelihood. Until then, (5) is a reproducible conditional prediction region and (8) a calibrated-convention rival, not an apparatus-specific fit.

## Verification and provenance

`moving_scalar_check.py` checks (3) against direct segmented time integration, including a nonzero longitudinal drift. Maximum amplitude discrepancy is below 1e-16. It independently integrates the positive continuum expression at two quadrature resolutions: dimensionless synthetic examples give `chi/g²=.0053991448653` and `.0023980130260`, both below their .010991210596 envelope; resolution changes are below 3e-13. It verifies the mass cancellation and (8) against direct time quadrature. These are numerical checks, not interval certification of the quadrature. The bound itself follows from the displayed inequalities and does not depend on numerical integration.

Run from the campaign worktree:

```bash
python3 .claude/science/physics-loops/observations-to-toe-24h-20261012/agents/neutrino/interference/moving_scalar_check.py
```

The runner sets one numerical thread and checks deadline/stop markers. It writes runtime `neutrino/interference/moving_scalar_results.json` and was captured in `moving_scalar_run.log`; computation took under one second. Upstream main was searched at pin `7f9fac6cb89c6c7b86cde4f5716870d0dfc4b9de`: the literature-positioning note already names influence functionals, and an archived historical note mentions Fein2019. Neither is used as empirical authority or as a retained derivation of the present conditional model. No novelty claim for influence functionals, CSL response, or general vacuum radiation is made.

The article-copy SHA256 is `ffac6916a434faf0740eec08eb9e057fdeebea5b45f3d1c137caa404af492315`; publisher supplement SHA256 is `e92f6d0e8bcd06fb8c04cf7d0d481f3e099ab6d5e6c1d407a1b522b39e1448cf`. Complete URLs, retrieval times and primary-theory PDF receipts are in runtime `inputs/`. The final delivery receipt hashes this protocol, code, report and numerical results.
