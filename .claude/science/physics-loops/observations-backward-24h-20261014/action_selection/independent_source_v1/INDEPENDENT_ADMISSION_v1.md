# Independent primary-source and input-admission conclusions v1

Scope: a focused source check, not an audit, reconstruction authorship, numerical fit, or publication gate. These conclusions were fixed before opening the parent's `action_selection/WORKING_v1.md`. Source PDFs are local reading evidence, not automatically approved redistribution assets. No raw strain, posterior samples, or observational data products were acquired.

## Source findings

**Reconstruction.** [Boisseau et al., gr-qc/0001066v1](https://arxiv.org/pdf/gr-qc/0001066v1), PDF pp. 1–4, particularly equations (2)–(8), (14), (22)–(24), construct a Jordan-frame scalar-tensor reconstruction from continuous distance and dust-growth functions, with specified matter coupling, scale conditions, initial information and approximations. This is not distance-only reconstruction. Equation (14) additionally assumes flat FLRW. Their cosmological coefficient and the locally measured effective gravitational coupling need not coincide; equation (7) displays the scalar contribution. The reconstruction reaches the field range sampled by the solution, rather than selecting a unique global action. Their historical numerical bounds are not adopted as current data.

**Homogeneous versus environmental endpoints.** [Dalang and Lombriser, 1906.12333v2](https://arxiv.org/pdf/1906.12333v2), sections 2, 3.3 and 5.1, give the homogeneous ratio as the observer/source effective Planck-mass ratio. Their environmental construction instead uses the actual local endpoint values, equation (5.20), PDF p. 30. Equal screened endpoint values can remove the intervening cosmological amplitude effect under that construction's premises. This is a conditional counterexample to inferring a constant cosmological coefficient from a unit distance ratio, not a universal no-go for standard sirens. In particular, temporal screening is not automatic. The source treatment assumes a controlled GR-like inspiral; it is not a generic proof about nonlinear binary generation. Their supernova luminosity correction is specific to that calibration model and must not be applied to SBF by substitution.

**Transport assumptions.** [Dalang, Fleury and Lombriser, 2009.11827v3](https://arxiv.org/pdf/2009.11827v3), PDF pp. 1–2 and 9–10, equations (95)–(97), supply a tensor-transport endpoint relation in the stated reduced scalar-tensor, linear/eikonal regime. The scalar background can be inhomogeneous: its endpoint values need not be FLRW values. The read derivation uses a decoupled luminal-scalar setting; this check does not certify every other regime discussed in the paper. Their electromagnetic luminosity-distance identification also requires the relevant distance-duality/photon-number premises. The Poisson or Cavendish coupling cannot generically be substituted for the tensor coefficient without an additional relation.

**Published GW inference.** [GW170817 standard-siren paper, 1710.05835v1](https://arxiv.org/pdf/1710.05835v1), PDF pp. 2–4 and 6–12, conditions parameter inference on GR, waveform assumptions, calibrated strain, detector noise and parameter priors. The optical counterpart fixes sky position. Distance and inclination are correlated. The quoted 43.8 Mpc estimate has asymmetric 68.3% intervals and is not a theory-free likelihood. The Hubble inference additionally uses host association and peculiar-velocity information. These ingredients do not make the GW amplitude distance a distance-ladder measurement, but they must remain in its provenance. Distances or inclinations subsequently conditioned on an electromagnetic distance or Hubble prior cannot be reused as an independent GW input against that same electromagnetic calibration.

[GW170817 detection paper, 1710.05832v1](https://arxiv.org/pdf/1710.05832v1), PDF pp. 4–5, section IV and Table I, uses post-Newtonian waveform models with spin and tidal assumptions and Bayesian calibration/noise treatment. Its 40 Mpc distance has 90% uncertainty bounds, incorporating model differences. It is not the same posterior summary as the fixed-sky standard-siren result. Cosmology-dependent source-frame masses and electromagnetically constrained inclination must be distinguished from the GW distance inference. No raw posterior or strain has been examined here.

**Electromagnetic calibration.** [Cantiello et al., 1801.06080v2](https://arxiv.org/pdf/1801.06080v2), PDF pp. 3–9, especially sections 3–5 and Tables 1–2, use HST SBF measurements, a stellar-population color calibration, PSF and contamination treatment, photometric/extinction corrections, and an absolute scale ultimately tied to Cepheids. Their adopted distance is 40.7 ± 1.4 statistical ± 1.9 systematic Mpc. It is obtained independently of the GW signal, but is not a geometric or ladder-free distance. Several band/color estimates are correlated. Subsequent SBF/GW inclination combinations do not create another independent distance observation. This paper does not calculate a varying-gravity response of its stellar population and anchor calibration; none is invented here.

## Independent admission reasoning

Let the explicitly chosen physical-frame action convention be
\[
S=\int\sqrt{-g}\,[F R/2-Z(\phi)(\nabla\phi)^2/2-U(\phi)]+S_m[g,\psi].
\]
For spatially flat FLRW and conserved minimally coupled matter, the background equations require
\[
Z\dot\phi^2=-2F\dot H-(\rho+p)-\ddot F+H\dot F,\qquad
U=3FH^2-\rho-\tfrac12 Z\dot\phi^2+3H\dot F.
\]
These are algebraic rearrangements of the specified action equations, used only to identify the input requirements. Any different normalization, including the parent's proposed \(F=Q/C\), must be matched to its actual action before applying factors. Smooth histories, derivative control, positivity, scalar-coordinate/branch choices, matter conservation and any absolute gravitational normalization remain explicit premises. Imported GR-fitted density histories are not automatically model-independent measurements in a different action.

In a regime where the tensor kinetic coefficient is proportional to this \(F\) and the cited transport/source assumptions apply, the distance-ratio relation is
\[
\mathcal R=D_G/D_L=\sqrt{F_o^{\rm local}/F_s^{\rm local}}.
\]
Admitting it as \(\sqrt{F(t_o)/F(t_s)}\) requires an independently specified endpoint-environment relation. Even then it fixes only a ratio, not an absolute normalization. Source-waveform inference, detector calibration and electromagnetic distance calibration remain part of the observation model; published GR distance summaries cannot simply become new-theory distance likelihoods.

A single ideal exact ratio cannot determine a continuous function or its required derivatives. For example, choose a smooth nonconstant bump \(b(t)\) with compact support strictly between the two endpoints and replace positive \(F(t)\) by \(F(t)e^{\epsilon b(t)}\). The endpoint ratio is unchanged, while interior derivatives change. Thus this datum alone cannot identify \(\dot F\) or \(\ddot F\). This is an elementary information-content example, not a claim of observational equivalence of complete theories or a universal obstruction to inference from additional observations. Parametric restrictions, additional events, environmental information and other measured functions could change the inference problem; they add inputs and assumptions that must be named.

Admission disposition: continuous physical \(H,F,\rho,p\) may be explicitly assumed for a conditional reconstruction. The inspected GW170817 and host-SBF publications do not supply that input tuple or a continuous \(F(t)\). They can inform a future, explicitly calibrated joint inference under a stated model. No fit, ratio-derived bound, new observation, novelty claim, universal screening theorem, or full-action selection is established here.

## Read scope and limits

All Boisseau pages were read. Dalang–Lombriser PDF pages read: 1, 2, 5–8, 14–17, 26–30, 37–38. Dalang–Fleury–Lombriser: 1, 2, 9–10. Standard-siren paper: 2, 3, 4, 6–12. Detection paper: 4–5. Cantiello: 3–9. Visual inspections confirmed Boisseau p. 2; Dalang–Lombriser p. 30; Dalang–Fleury–Lombriser p. 10; standard-siren p. 7; Cantiello pp. 5 and 7. Other rendered pages were not yet visually inspected. Full extraction does not mean full-paper reading where the scope above is partial.

Exact versioned URLs, access times, TLS status and PDF/HTML/extracted-text SHA-256 hashes are in `SOURCE_ACQUISITION_v1.json`; rendered-page identities are in `PAGE_RENDER_IDENTITIES_v1.json`. The initial pre-network Python syntax failure remains in `ACQUISITION_SETUP_FAILURE_v1.json`. No evidence was removed or treated as a successful acquisition. This memo precedes the author-note comparison and will remain unchanged.
