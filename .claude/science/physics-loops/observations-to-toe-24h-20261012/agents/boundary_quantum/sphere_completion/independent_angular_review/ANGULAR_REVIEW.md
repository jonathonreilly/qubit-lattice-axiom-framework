Focused independent angular robustness review, 2026-10-12 UTC.

Disposition: the signed-measure bound, sharp angular constant, rational tolerances, and all ten counts are correct under the stated reflection premises. The original stochastic-averaging sentence needed an explicit source-independence qualification; the separately preserved V2 supplies it and explicitly places heralding/inclusion before the fresh branch/settings. I read the complete V2 and find those two qualifications resolved. No numerical table correction is needed. This is a narrow independent check, not a formal audit, new scientific authorship, empirical calibration, or validation of the original full-sphere classification.

Source continuity is exact. The original note SHA256 is `89bb0524439fa58b453fe473d312d58bfcb2ec6600fb31af4bbdd811ae31ae30`, checker `04c83b5e6362c3d79aeac4ec340421524dc6cd37240a6d683586ea2d642d548d`, and V2 `5c953c127b522b23de3c8b3a237996a7ceb89a0d4fc24eb21aeb2e00a0d83e6a`. The reflection V2 premise is `8346f7aac3260325f443b6a1b031790caacef56a85ae072fdb4286b12bf4dafd`; its numerical result is `a911495b6d1f60b48334d03346c45393911031bead3288c2e0c1aad2e7b25ea9`. Freeze `e2b44b90578e11899629b58183b793b5d70276c92a579b364bd7d4ec6fb877d4` precedes result `5f3913d3508ff38b5a8bda32ec3689df272bddc01a6838bee230145fa778dba9`. Both identify the original frozen note and checker. V2 is an additional premise clarification, not a replacement hash asserted for that prior execution. All originals and snapshots matched before and after my checks.

For normalized sphere measure, the coefficient measure is

    dν = -d(Δ_*μ) + 14 P3(a·b) d(μ⊗μ).

The diagonal D has product measure zero, while Δ_*μ is concentrated on D. The two parts are mutually singular even though P3(1)=1. Writing q²=3/5 and H(x)=5x⁴/8-3x²/4 gives H(q)=-9/40 and H(1)=-1/8, hence ∫[-1,1]|P3|=2[H(1)-2H(q)]=13/20. Thus ||ν||TV=1+7(13/20)=111/20. A bounded measurable error equal to -ε on D and ε sign(P3) off D attains that norm in the unrestricted function space. An error supported on D has zero product-a.e. size and can change B by ε. This verifies the separate diagonal allowance and shows why product-a.e. control alone is insufficient; it says nothing about whether those extremizers are realizable correlations.

The angular derivative is also exact. For the first half of the interval, u=1-2θ/π and t=tanh(k cosθ) both lie in [0,1]. Differentiating g=(u+t)/(1+ut) gives

    g_u=(1-t²)/(1+ut)²,  g_t=(1-u²)/(1+ut)²,
    F'(θ)=-(1-t²)/(1+ut)² [2/π+k(1-u²)sinθ].

Both partial derivatives are between zero and one, so |F'|≤2/π+k. Oddness about π/2 extends the result to the other half. At the midpoint F'=-(2/π+k), proving sharpness of the global Lipschitz constant. Endpoint continuity closes the bound; the one-sided slope at θ=0 is -(2/π)e^(-2k), which is finite. There is no omission of the coincidence cusp. Spherical distance's triangle inequality then gives the stated V L(δA+δB) pointwise allowance, including the diagonal and almost-sure bounded direction mixtures. Monotonic F verifies the optional diagonal refinement when 2δ≤π/2.

The quantum calibration argument requires common local observables for the two sampling branches. With Π3's kernel 7P3, S=I-2Π3 is an isometry on the vector-valued L² space and B(C)=-⟨u,Sv⟩. Observable contractions give ||u||,||v||≤1; hence |B|≤1. A deterministic local relabeling changes u and v without changing this argument and need not preserve sphere measure. A product of source-independent classical calibration kernels, conditional on the past, can be averaged into local Hermitian contractions on the same conditional source state.

The original wording did not state the latter independence explicitly enough. Independent local signs λA,λB may choose observables λAσz and λBσz while a correlated source emits |λA⟩z⊗|λB⟩z. The signs are mutually independent, but actual C=1, whereas separately averaging those observables on the averaged original state gives C=0. This is a counterexample to that averaging shortcut, not to the quantum bound: local controlled observables on a common state enlarged by the calibration records reproduce C=1 and B=-1. V2 now requires source-independent conditional kernels for separate averaging and explicitly flags the enlarged-state treatment for source-correlated records. An arbitrary correlated mechanism still needs the common local quantum representation and fresh-choice independence; naming a register alone is not a substitute for those premises.

The inclusion condition matters separately from outcome selection. For common constant +1 outputs the unselected statistic is B=-1. If an apparatus retains only positive-P3 settings in the product branch, every retained Z is +111/20; this happens with probability 91/222 under the original sampling law and does not inspect any outcomes. Thus a claim of “no outcome postselection” alone would be insufficient. V2 explicitly puts the herald and inclusion decision before the fresh branch and setting draw, excludes retention by fresh settings, and retains the common-map/hidden-branch requirement. The exact sampling law, no setting dependence of the conditional source, and no remote fresh setting in a local response remain substantive assumptions.

For arbitrary extra systematic error that can also move the quantum statistic by η, the gap is B_candidate,lower-b_candidate-(1+η), not just Δ0-b_candidate. A corresponding test threshold is 1+η plus half that remaining gap. The note correctly requires a separately justified null allowance. Its frozen ε column is explicitly candidate-side correlation error under an otherwise unchanged quantum-null bound; it cannot establish an apparatus-wide bias budget. All scores must also remain bounded by J for the quoted tail bound.

I independently enclosed π using π=4[atan(1/2)+atan(1/3)] with exact alternating-series endpoints, rather than the author's Machin identity. This yields the same outward-rounded rational L_upper=1.106234053435949145898798293064. The κ interval was cross-checked numerically at 90 digits with κ=√2 log((1+√2)/√3); this is a consistency check, not an independent interval recertification. Propagating the pinned a3 endpoints gives Δ0=0.05123468688990720817613836399686861439531449 and sufficient strict equal-angle tolerance δ<0.00439208239723237483107475789163979640114649 radians. The latter is a coarse-bound certificate, not a necessary or optimized tolerance.

Every allowance, gap, and integer count was recomputed with exact fractions, without importing author helpers:

| Per-arm angle δ (rad) | Candidate ε | Effective gap, approximately | N |
| --- | --- | ---: | ---: |
| 0 | 0 | 0.05123469 | 469373 |
| 0 | 1/1000 | 0.04568469 | 590344 |
| 1/2000 | 0 | 0.04540207 | 597716 |
| 1/2000 | 1/1000 | 0.03985207 | 775791 |
| 1/1000 | 0 | 0.03956945 | 786912 |
| 1/1000 | 1/1000 | 0.03401945 | 1064613 |
| 1/500 | 0 | 0.02790421 | 1582365 |
| 1/500 | 1/1000 | 0.02235421 | 2465627 |
| 1/250 | 0 | 0.00457373 | 58898476 |
| 1/250 | 1/1000 | -0.00097627 | No count |

For fixed N, conditional Hoeffding bounds for Z∈[-J,J] give each one-sided error ≤exp[-N Δeff²/(8J²)] at the midpoint threshold. The prescribed N=ceil(40J²/Δeff²) makes this ≤e^-5<0.01. I checked every ceiling by N-1<40J²/Δeff²≤N and preserved the negative final gap rather than squaring it into a false sample count. Outcome memory is allowed if each included trial satisfies the relevant conditional mean bound under its fresh sampling law; an unconditional average mean alone does not suffice. These are fixed-horizon guarantees, not an optional-stopping result. Primary context on memory and randomized Bell tests was read in [Barrett et al.](https://arxiv.org/abs/quant-ph/0205016) and [Gill](https://arxiv.org/abs/quant-ph/0301059); the constants here were independently derived.

Additional lightweight controls used a 136-node degree-exact sphere quadrature. The l=3 projector had rank 7 and idempotence residual 1.11e-16; the reflection-square residual was 5.55e-16. Common identity, warped, and source-independent mixture maps all obeyed |B|≤1. This is an operator control, not an approximation to the singular-measure total-variation proof. Symbolic derivatives and 1001 high-precision angle points verified the formula, symmetry, monotonicity, endpoint slope, midpoint saturation, and optional diagonal bound. The independent script took 0.30 seconds with maximum RSS 76.3 MB and one numerical-library thread.

Evidence is in `check_angular_independent.py` and runtime `quantum/angular_robustness/independent_angular_review/angular_independent_checks_v1.json`, with exact source identities in the receipt. Only designated review directories were written. No actual field driver, targets, fits, author source, Git state, or audit state was changed. The frozen reflection coefficient interval is an input premise; no all-orders sphere theorem, measured apparatus tolerance, detector performance, or empirical exclusion follows from this scoped review.
