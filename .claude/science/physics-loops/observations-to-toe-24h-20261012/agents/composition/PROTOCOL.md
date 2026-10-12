# Joint composition/clock reconstruction protocol

Status: conditional-support. Claim type: bounded_theorem / explicit candidate calculation.
Trace: frontier_discovery; no adopted-premise or audit-status change.
Source baseline and skill: `7f9fac6cb89c6c7b86cde4f5716870d0dfc4b9de`.

This is an assigned research subtask of the campaign. Only this agent directory and the assigned external download/log directory are writable. The coordinator owns commits, PRs, locks, shared state, independent review and stopping the overall campaign.

## Frozen model and empirical roles

One unscreened, exactly massless canonical scalar plus an Einstein metric. Constant first derivatives of low-energy masses and couplings are supplied; there is no derivation of these choices from the adopted lattice premises. Full basis: `(d_g, d_hatm-d_g, d_deltam-d_g, d_me-d_g, d_e)`. Main concrete subfamily sets the two light-quark/QCD-ratio slopes to zero and leaves `(g,x,e)=(d_g,d_me-d_g,d_e)` free. The common scalar charge is `alpha_B=g+Qme_B*x+Qem_B*e`, using mass fractions for mixtures. Test-mass and clock responses share this charge and the same three couplings.

Calibration observations: MICROSCOPE final TiAlV/PtRh differential acceleration (`2209.15487v1`), and Lange et al. Yb+ E3/E2 solar-annual frequency-ratio coefficient (`2010.06620v2`, Table II). Use the **direct ratio coefficient**, not derived bounds on fundamental constants. The experiments are separate. The summary-data likelihood assumes Gaussian independent errors, profiles the MICROSCOPE quoted systematic as an additive Gaussian nuisance, and retains the published clock reproducibility treatment. The raw time-series likelihood is not reconstructed.

Potential/sign convention: `U=+G*M/(r*c^2)` is positive depth. A canonical attractive scalar has `phi-phi_inf=-alpha_S*U`. The annual cosine is positive at perihelion. Thus `k_R=A/(R*epsilon)=-alpha_S*(d ln R/d phi)` (with the orbital-GM normalization correction stated in the note), where `epsilon=1.65e-10`. Optical E3/E2 has `d ln R/d phi=-6.95*e`.

Selected held-out channels, **excluded from calibration fitting**:

1. Sun-directed Be/Ti response from Schlamminger et al. `0712.0607v1`; unlike MICROSCOPE this changes both material contrast and source. The existence and approximate sensitivity of this published test were previously known, so this is not blind.
2. Yb+ E3/Cs annual ratio in Lange et al.; its Table II central value and uncertainty have already been read. It is a distinct measured ratio but shares E3 apparatus; its unavailable covariance with E3/E2 prevents an independent combined likelihood. Use it only as a marginal held-out compatibility check.

Freeze illustrative electron-only Earth-neutral witnesses at `x=0,0.001,0.01,0.03,0.1`, `e=0`, `g=-Qme_E*x`. Do not choose these values from held-out residuals. Also derive the full summary-data allowed-set equations for the three-coupling model and an analytic chart of their exact central fibers. Any generic center-fitting witnesses will be labelled calibration fits, not predictions of the constants.

The Earth sensitivity starts with the explicit Damour--Donoghue 32% Fe / 68% SiO2 composition model. Solar sensitivities use integrated mass fractions from the primary BS05(OP) and BS05(AGS,OP) tables, not photospheric hydrogen abundance. Two old SSM variants are a source-model sensitivity exercise, not a modern observational confidence distribution. Nuclear/electronic charge formulas, binding corrections, alloy/isotope tolerances, and missing source covariance remain visible. Exact degeneracy statements will be expressed for arbitrary fixed effective charges so they do not depend on the chosen Earth model.

No claim of novelty is made for the scalar action, Damour--Donoghue sensitivities or factorization. The intended new campaign evidence is an explicit reproducible joint inverse calculation, cancellation witnesses and their frozen cross-channel responses.

## Source correction after freezing (2026-10-12)

Full reading of `0712.0607v1` found the Earth Be/Ti result and a **galactic-center** fit, but no published numerical solar Be/Ti coefficient. The quoted bound on space-fixed acceleration is not silently applied to the moving Sun. The solar held-out forward response remains frozen; locating the actual primary solar coefficient is additional evidence work. A source correction will be recorded separately from any model or witness change. The E3/Cs marginal comparison is already available if the solar coefficient cannot be sourced.
