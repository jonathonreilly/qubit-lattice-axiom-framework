# One scalar, composition acceleration and clock response

Status: conditional exploratory construction and bounded algebraic results; independent review pending. This is not a derived TOE or a globally viable scalar model. Baseline/skill pin: `7f9fac6cb89c6c7b86cde4f5716870d0dfc4b9de`. No adopted premise, audit verdict, commit or PR is changed here.

The substantive result is a joint inverse calculation. The same three couplings predict two calibration measurements and an additional solar acceleration response. The complete nominal calibration region contains a continuous range of solar Be–Al accelerations at least as wide as **[-230.232, +94.5108] fm/s²**, and is contained in the certified conservative envelope **[-563.342, +563.342] fm/s²**. The latter is an outer bound, not a sharp optimization. An electron-only subfamily is strongly restricted by the later, exposed solar measurement, while a different family cancels both source charges and survives all three source-mediated summaries.

The scalar action, dilaton basis and charge formulas are established controls from [Damour and Donoghue, version 2](https://arxiv.org/abs/1007.2792v2). No novelty is claimed for them. The campaign contribution is the reproducible joint calculation, explicit continuous witnesses, source-stress accounting and public estimator response check.

## Observations and empirical roles

| Role | Primary observation | Direct summary used |
|---|---|---|
| Calibration | [MICROSCOPE final Ti/Pt result, 2209.15487v1](https://arxiv.org/abs/2209.15487v1) | η(TiAlV,PtRh)=(-1.5 ±2.3 statistical ±1.5 systematic)×10^-15 |
| Separate calibration | [Lange et al., 2010.06620v2, Table II](https://arxiv.org/abs/2010.06620v2) | Annual Yb+ E3/E2 ratio coefficient k_O=-9.7(7.7)×10^-8 |
| Model-development holdout | [Ross et al., 2602.02815v1](https://arxiv.org/abs/2602.02815v1) | Sun-directed Be–Al differential acceleration 0.66(0.61) fm/s² |
| Additional marginal check | Lange et al., Table II | Annual E3/Cs coefficient -4(44)×10^-8 |
| Older solar comparison | [Wagner et al., 1207.2442v1, Table 3](https://arxiv.org/abs/1207.2442v1) | Sun Be/Ti η=(-3.1±4.7)×10^-13 |

MICROSCOPE uses actual mass-fraction alloy compositions Ti/Al/V=90/6/4 and Pt/Rh=90/10. Pure Ti and pure Pt are not substituted. The clock observable is the measured ratio coefficient, not a separately inferred constraint on a fundamental constant.

The Ross source was selected after the original solar source failed to provide the sought coefficient. Its measured amplitude was exposed before the model-region freeze. It is excluded from calibration fitting but is **not blind evidence**. Discovery/exposure times and the unchanged witness grid are in [POST_FREEZE_CORRECTIONS.md](POST_FREEZE_CORRECTIONS.md) and [MODEL_FREEZE.json](MODEL_FREEZE.json). The original protocol and frozen artifacts remain intact.

## Supplied physical bridge

Supply an Einstein metric and an unscreened, exactly massless scalar ϕ, with gravitational action proportional to

    ∫sqrt(-g) [R - 2 g^{μν} ∂μϕ ∂νϕ],

and matter masses/couplings depending on ϕ. In this normalization a point-body scalar charge is α_B=∂ln(m_B)/∂ϕ and the Newtonian pair force is proportional to 1+α_S α_B. Universal metric coupling supplies the common gravitational response; the scalar supplies the material-dependent part. This model is distinct from any finite-mass or continuous-spectrum mediator considered elsewhere in the campaign.

The full low-energy coupling basis is

    (d_g, d_hatm-d_g, d_deltam-d_g, d_me-d_g, d_e),

with hatm=(m_u+m_d)/2, deltam=m_d-m_u, and d_e=∂ln(α_EM)/∂ϕ. Restrict the two quark/QCD-ratio slopes to zero and keep

    d=(g,x,e)=(d_g, d_me-d_g, d_e),
    α_B=q_B·d,  q_B=(1,Qme_B,Qem_B).

This restriction is an explicit premise of this comparison, not an empirical derivation. All non-electronic masses co-scale with the QCD scale in the electron-only slice. The charge convention is invariant under simultaneous reversal of all three couplings in the force and annual-clock observables.

For transparency, the unreduced Damour–Donoghue sensitivities are

    Qhat ≈ .093-.036 A^(-1/3)-.020 (A-2Z)^2/A^2
                 -1.4e-4 Z(Z-1)/A^(4/3),
    Qdelta ≈ .0017 (A-2Z)/A,
    Qme ≈ 5.5e-4 Z/A,
    Qem ≈ 1e-4[-1.4+8.2 Z/A+7.7 Z(Z-1)/A^(4/3)].

The common nuclear factor F_A is set to one. The calculation refines the leading electron rest-mass term to Qme=(m_e/u)Z/A with m_e/u=5.485799090441e-4 from the preserved [CODATA 2022 table](https://physics.nist.gov/cuu/Constants/Table/allascii.txt). It uses declared atomic-weight approximations from [CIAAW](https://ciaaw.org/atomic-weights.htm). Electronic binding, detailed nuclear responses, isotope assays and their covariance are not supplied. These are effective charge approximations, not a precision ab initio atomic/nuclear calculation.

Mixtures are mass-weighted. Earth starts with .32 Fe + .68 SiO2, the explicit simple source model used in the dilaton literature. The Sun uses mass-coordinate integrals of the preserved [BS05(OP) and BS05(AGS,OP) primary tables](https://www.sns.ias.edu/~jnb/SNdata/Export/BS2005/). These 2005 models are source-stress inputs, not a current solar confidence distribution. The integrated H mass fractions are .671079 and .688264; replacing them by the surface values .74045 and .75830 would be a material source error.

| Effective body/contrast | Qme | Qem |
|---|---:|---:|
| Earth baseline | 2.67986546e-4 | 1.92001117e-3 |
| Sun baseline | 4.55341032e-4 | 6.42954666e-4 |
| TiAlV | 2.52683988e-4 | 2.25145008e-3 |
| PtRh | 2.21392827e-4 | 4.18574966e-3 |
| TiAlV minus PtRh | 3.12911606e-5 | -1.93429957e-3 |
| Be minus Al | -2.08280995e-5 | -1.02276881e-3 |

Extra printed digits permit reproduction; they do not express physical precision. An alloy-fraction error propagates explicitly, for example

    δ(Δq_M)=δf_Al(q_Al-q_Ti)+δf_V(q_V-q_Ti)
             -δf_Rh(q_Rh-q_Pt).

No assay covariance is available here to turn that expression into a calibrated probability distribution. Electron-binding changes also affect Qme, including the Be/Al contrast. Consequently, bounds using that contrast below are conditional on the leading electronic approximation.

## One forward map for every channel

Take positive potential depth U=G_*M/(rc²), with ϕ-ϕ_infinity=-α_S U. The annual cosine is positive at perihelion. For any frequency ratio R, b_R=∂ln(R)/∂ϕ and k_R=-α_S b_R/D, where

    D=1+α_E α_S

converts the bare solar GM to the explicitly selected Earth-orbit dynamical GM reference. It is not silently set to one in the generic calculation. The common metric contribution cancels in a co-located ratio.

Write E=q_Earth, S=q_Sun, T=q_TiAlV, P=q_PtRh, B=q_Be-q_Al, H=(0,0,1), and α_E=E·d, α_S=S·d. Then

    η_M = (E·d)((T-P)·d) / [1+(E·d)((T+P)·d)/2],
    k_O = 6.95 (H·d)(S·d) / D,
    h_BeAl = (S·d)(B·d) / D,
    Δa_BeAl = (5.9e-3 m/s²) h_BeAl.

The Yb E3/E2 intrinsic slope is b_O=-6.95e. Its annual fractional amplitude is ε k_O, ε=1.65e-10. On e=0 only, an optical/hyperfine ratio has b_H=-x and therefore k_H=α_S x/D. This follows from the leading proton/electron mass-ratio response; no nuclear magnetic sensitivity is needed in that slice. The general e≠0 optical/hyperfine response is deliberately not supplied without the additional magnetic and relativistic sensitivities.

These equations are exact for the stated Newtonian effective model, including its point-source/monopole reduction. Post-Newtonian terms, compact-body self-energy sensitivity, screening, time-dependent cosmological scalar background, finite range and environmental field noise are not included. They are not established properties of reality by this construction.

For the real Earth, composition-dependent multipoles can produce different spatial templates. Canceling its integrated scalar monopole does not prove that the complete MICROSCOPE time series vanishes. An effective source row for a single fitted amplitude would involve the orbit, source distribution and instrument template; multiple resolved templates can add independent rows. Their scalar transfer coefficients/covariance are not reconstructed here. The exact algebraic identities apply to this declared summary forward map, while the numerical Earth model is a conditional monopole approximation.

## Nuisance treatment and full calibration region

The frozen exploratory box is |g|≤.001, |x|≤.1, |e|≤.1. It is a supplied weak-coupling domain, not an inferred prior. In this box D≥.9999986473, so no rational singularity occurs.

The frozen summary approximation treats the MICROSCOPE systematic as an additive Gaussian nuisance b with scale 1.5e-15, independent of the statistical scale 2.3e-15. Profiling

    (y_M-η_M-b)^2/σ_stat² + b²/σ_sys²

gives (y_M-η_M)^2/(σ_stat²+σ_sys²), with σ_M=2.74590604e-15. At η_M=0 the fitted nuisance is -4.47612732e-16. The actual paper describes systematic upper bounds; the Gaussian nuisance is our approximation. Treating it instead as |b|≤1.5e-15 gives the distinct profiled cost

    max(|y_M-η_M|-1.5e-15,0)^2/(2.3e-15)^2.

The exact zero-prediction families below remain allowed under either convention; their MICROSCOPE cost is .298408 under the Gaussian choice and zero under the bounded choice. This robustness of the cancellation example does not establish coverage for either whole parameter region.

MICROSCOPE's quoted errors already summarize miscentering/calibration, thermal response and glitch treatment. Those are not independently re-added as new Gaussian penalties. The Lange annual fit already includes the stated 1.6e-17 reproducibility contribution; its 3.3e-17 absolute E2 systematic is not added again to the annual coefficient. A constant offset does not mimic the specified annual template. Seasonal environmental nuisance covariance is not reconstructed from raw clock data. MICROSCOPE and the PTB ratio experiment are distinct; E3/Cs shares the E3 apparatus and is used only marginally because its covariance with E3/E2 is unavailable.

The **complete frozen nominal acceptance set** is the following implicit, closed set; no branch is dropped:

    A0 = {d in the box:
      ((η_M(d)+1.5e-15)/2.74590604e-15)^2
       +((k_O(d)+9.7e-8)/7.7e-8)^2 ≤5.9914645471 }.

The threshold is a joint two-observable Gaussian acceptance ellipse. It is not a three-parameter Wilks region or a parameter posterior. With source coefficients treated as nuisances, the family is A0(q_E,q_S,q_tests); the source-stress union is not assigned a probability measure.

An analytic chart supplies every nonsingular fiber at any (p,k) in this ellipse. Put r=x/e, a=α_E, w=ae, v=e², z=k/6.95 and

    A=(Q_T-Q_P)·(r,1),
    C=((Q_T+Q_P)/2-Q_E)·(r,1),
    L=(Q_S-Q_E)·(r,1), Q=Q_E·(r,1),
    J=[z(A/p+L-C)-1]/L,
    w=1/(A/p-C-1/J),  v=wJ.

For positive v and nonsingular denominators, e=±sqrt(v), x=re, g=w/e-Qe, followed by the box check. Substitution is checked with high-precision intermediate arithmetic. The chart is not the entire region by itself: e=0, p=0, L=0 or a vanishing chart denominator must be evaluated using the original forward equations. A0 includes all such singular fibers.

For e≠0 the held-out transfer simplifies exactly to

    h_BeAl=(k/6.95)[ΔQme_BeAl r+ΔQem_BeAl].

Its dependence on r makes the calibration degeneracy visible; fitting p and k does not fix the new response. Seven supplied simultaneous central fits illustrate it, including h corresponding to -87.2894, +67.0693 and +94.5108 fm/s². These are calibration fits, not predictions of the constants.

## Propagating the entire allowed set

The exact prediction region is {Δa_BeAl(d):d∈A0}. [global_bounds.py](global_bounds.py) proves a conservative bound on that entire set without grid selection or numerical optimization. Let

    δ_M=m x+n e, Δ_B=b_m x+b_e e,
    α_S=α_E+s_m x+s_e e,
    ρ=.016,
    |α_E δ_M|≤Pmax=8.22129630e-15,
    |e α_S|/D≤Zmax=4.10757563e-8.

These inequalities follow from the calibration ellipse and bounded denominators. In |e|≤ρ|x|,

    |h|≤ |b_m|[Pmax/(m-|n|ρ)+(|s_m|+|s_e|ρ).1²]/Dmin
          +|b_e|Zmax =8.57893726e-11.

In its complement, |xα_S|/D≤Zmax/ρ, so

    |h|≤Zmax(|b_m|/ρ+|b_e|)=9.54816236e-11.

These cases exhaust the box, including e=0 and all singular fibers. Thus |Δa_BeAl|≤563.342 fm/s² throughout A0. Enlarging the ellipse to separate absolute bounds makes this deliberately conservative. It is much tighter than the original full-box-only bound retained in joint_results.json.

The continuous electron branch below attains every value in [-230.232,0]. Scaling a supplied positive central-fit vector continuously from zero to its full value keeps both residuals no larger than their zero-prediction residuals and attains [0,94.5108]. Hence the guaranteed attainable interval is [-230.232,94.5108]. The true sharp projection lies between this interval and the certified outer envelope. It is not represented by one preferred witness.

## Frozen Earth-neutral electron branch and solar comparison

For every t∈[-.1,.1], take

    e=0, x=t, g=-Qme_E t.

Then α_E=0, η_M=0 and k_O=0 exactly within the model, and the calibration cost is 1.88535401. Defining s_m=Qme_S-Qme_E=1.87354485e-4 gives

    k_H=s_m t²,
    Δa_BeAl=-23023.2034 t² fm/s²,
    annual optical/hyperfine amplitude=3.09134901e-14 t².

| Frozen t | Solar Be–Al prediction (fm/s²) | Annual optical/hyperfine fractional amplitude |
|---:|---:|---:|
| 0 | 0 | 0 |
| .001 | -.0230232 | 3.09135e-20 |
| .01 | -2.30232 | 3.09135e-18 |
| .03 | -20.7209 | 2.78221e-17 |
| .1 | -230.232 | 3.09135e-16 |

Using only the **conditional published-summary comparison** 0.66±1.96(.61) fm/s², the branch has |t|≤.00482322. This is a central marginal compatibility interval, not a combined confidence set. For the fixed t=.01 witness, (prediction-.66)/.61=-4.85626 is a standardized residual under those specific summary and charge assumptions; it is not a full exclusion significance.

On this branch, the shared scalar factor cancels from the transfer relation

    h_BeAl=ΔQme_BeAl k_H.

Consequently the same conditional marginal comparison gives annual optical/hyperfine amplitude ≤7.19156e-19. This cancellation removes Earth/Sun source composition from the transfer; it does not remove uncertainty in the Be/Al effective contrast or the measured estimator response.

Twenty-four source stresses vary Earth core mass fraction .30/.32/.34, mantle SiO2/MgSiO3, both solar tables, and Fe/O proxies for their unresolved metal remainder. **Retuning g to the corresponding Earth-neutral value** gives |t| limits .00475301–.00482799. These are sensitivity variants, not a confidence interval. Holding a numerical g fixed instead is a different calculation; it generally destroys the cancellation. No alloy or nuclear-response uncertainty distribution is supplied, so a fully propagated empirical coupling confidence region is unavailable.

The older solar Be/Ti and E3/Cs checks are retained in joint_results.json; they are not pooled into a likelihood. For example t=.01 has older solar Be/Ti standardized residual .315 and E3/Cs residual .133 under their marginal summaries. This emphasizes why a new source/material response can discriminate a branch allowed by the original two summaries.

## A distinct double-source-null family

The rank-one lift exposes the common inverse map. Put X=dd^T, X positive semidefinite with rank one, and sym(u,v)=(uv^T+vu^T)/2. Then each scalar numerator is linear in X:

    η_M = Tr[sym(E,T-P)X] / {1+Tr[sym(E,(T+P)/2)X]},
    k_O = 6.95 Tr[sym(S,H)X] / {1+Tr[sym(E,S)X]},
    h_BeAl = Tr[sym(S,B)X] / {1+Tr[sym(E,S)X]}.

The calibration uses the same rank-one X throughout. Replacing it by an arbitrary positive-semidefinite matrix would be a new multi-mediator model, not an innocuous fitting convenience.

Because E and S are independent rows in three coupling dimensions, their common kernel is one-dimensional. With x normalized to one, it is

    v=(-.000549667665158667, 1, .146708062435235),
    d=t v, |t|≤.1.

For every t, α_E=α_S=0 and all three source-mediated signals vanish. This **does not undo the Ross restriction on the different electron-only branch**. The intrinsic E3/E2 slope remains

    b_O=-1.01962103392 t,

which is -.101962 at t=.1. If an independently specified scalar field covariance C_ϕ is present, the leading ideal clock covariance is b_O² C_ϕ, before sensor filtering. The source measurements do not determine C_ϕ; this expression is a transfer coefficient, not an observed or predicted noise amplitude.

For a pure-Fe source at t=.1, the same vector gives α_Fe(α_TiAlV-α_PtRh)=-2.15110e-10. A controlled third source with a charge row independent of E and S is therefore a concrete next experiment. Its acceleration scale, geometry and nuisance floor must be specified before a detectability claim. A scalar fluctuation probe can also help if its state and response are independently calibrated.

Source uncertainty cannot be hidden in this construction. For the **fixed** nominal t=.1 vector, a source-charge error δα_E≈1.08755e-10 already produces one MICROSCOPE combined summary standard error. Under the 24 explicit source stresses, the fixed vector predicts η_M between -6.32676e-12 and +1.21422e-11. It is therefore not a robust numerical cancellation across that stress set. If couplings may be **retuned for each source model**, a kernel vector exists each time, with e/x between .144039 and .154012 and g/x between -.000558647 and -.000546996. An existential identifiability result and robust survival of a single chosen vector are different claims.

## Scope of the identifiability result and escape tests

The admissible objects are the stated three-coupling, fixed-charge, massless scalar model and these source-mediated summaries. The result is the explicit existence of nonzero null families, not a prohibition on learning scalar couplings in general.

1. Changing only test materials while retaining Earth/Sun sources cannot remove the double-source-null family: each new numerator still contains α_E or α_S. This follows directly from the forward map.
2. Adding the Sun source removes the single Earth-null electron degeneracy over much of its range, but leaves the one-dimensional intersection in three couplings. Both outcomes are calculated above.
3. Adding a genuinely independent source can remove that intersection. The Fe-source product above provides a nonzero witness rather than assuming this escape works.
4. A different clock sensitivity can be nonzero intrinsically, but another annual Sun-driven signal remains zero when α_S=0. An externally excited field or specified fluctuation covariance is additional information, not another rephrasing of the same null source.
5. Restoring the two quark-ratio couplings does not remove the exhibited examples: the present three-dimensional slice remains a subset. It instead requires more material/nuclear responses to constrain the enlarged class. Imposing a one-channel prior or forbidding cancellations would remove examples by changing the admitted model, not by deriving a bound from these measurements.

No global equivalence-principle no-go theorem, no absence of scalar effects, and no material-independent impossibility of identification follows. This packet does not claim a completed general no-go audit.

## Public Ross estimator response audit

All Ross-derived limits above remain **conditional published-summary comparisons pending independent normalization/source review**. The released source and processed fits are sufficient to examine the second-stage estimator, but not to reproduce the raw torque extraction or every data-dependent cut. The pinned upstream is [EotWash/EP-Analysis-Sun at 1e103b78](https://github.com/EotWash/EP-Analysis-Sun/tree/1e103b78b5c3f2d948a30da4f1e7301c6b6f83f5).

[ross_response.py](ross_response.py) ports the published run list, thermal rejection, per-run linear detrending, joint C/S percentile rejection, filter correction, two-day mean subtraction, nearest-basis matching and complex fit. MATLAB's documented default quantiles correspond to the midpoint/Hazen convention. Its [decimation algorithm](https://www.mathworks.com/help/signal/ref/decimate.html) reduces filter order when rounded transfer-function coefficients distort the cutoff; the port diagnoses an order-five choice and preserves endpoint alignment. Alternative orders are retained, not selected by agreement with the published result. Filtering absolute time coordinates also makes filter DC normalization consequential.

The upstream source sets m=.01936 kg, later assigns `[m,minI]=min(...)` during nearest-time lookup, and finally divides torque by r*m. The first port reports both literal-source and physical-mass normalizations. At the diagnosed order-five port, the literal assignment gives 0.664582±0.614068 fm/s², matching the paper's rounded 0.66±0.61; retaining the declared physical mass gives 0.829370±0.766331 fm/s². This is an observed source/normalization discrepancy requiring independent reconstruction and actual execution-version information. It is not yet a corrected experimental result.

With the observed cuts frozen, injecting a unit signal into the released first-stage amplitudes before per-run trend removal gives the conditional transfer matrix

    [[ .8299200073, -.0005261075],
     [ .0005261075,  .8299200073]].

This response uses the physical mass convention. It includes mean/trend projection but omits unavailable first-stage response, data-dependent cut movement and the scalar force's solar 1/r² seasonal amplitude. Those omissions prevent promoting this conditional injection to an end-to-end correction. The mean-subtraction-only response independently satisfies the exact identity 1-|mean(x)|²/mean(|x|²) in every segment. Source hashes and that projection check pass; exact MATLAB/raw-data reproduction remains unresolved. An independent agent has been given only the pinned upstream inputs for reconstruction.

## Reproduction and provenance

Run with one BLAS/OpenMP thread. Downloads are external; repository artifacts contain code, compact results and notes only. No jobs are detached. The stop-aware runner checks the immutable campaign deadline and both JSON and extensionless stop-marker names.

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 run_v2.py \
      --runtime /Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012 \
      --script joint_scalar.py -- \
      --source-dir /Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012/composition \
      --output /path/to/a/new/result.json

Use script names source_null.py or ross_response.py with the same arguments. global_bounds.py takes --results joint_results.json and --output instead. Preserve frozen outputs; write a new result filename.

The first script checks primary source hashes, solar shell integration by two summations, exact null identities, central-fiber substitution, simultaneous sign reversal and analytic nuisance profiling. The source-null script checks direct versus rank-one maps, source annihilation and all 24 retuned stress variants. These are author checks, not independent scientific audit verdicts. [V1_RESULTS_FREEZE.json](V1_RESULTS_FREEZE.json) records the pre-review hashes; individual results also preserve script/input hashes.

Main/source overlap inspected: current main EQUIVALENCE_PRINCIPLE_NOTE.md and matching code/text search; open PR #9476 head 3a4733871bcbdd731251052a65d5bf60457d7c3e, including its C5_O2_referee_full composition discussion; open PR #9477 head 18b7dce754488789eb539d2a6fae3d00d6c37e31 inventory. The existing warning that MICROSCOPE constrains actual-alloy response differences is respected. This limited overlap check does not support a global novelty claim. No known dilaton formula is presented as new.

The most useful next work is an independent completion of the Ross response audit, followed by an experiment/probe with a third source charge or independently specified scalar fluctuation covariance. Sharper numerical fitting of the same two summaries cannot by itself remove the exact source-null families.
