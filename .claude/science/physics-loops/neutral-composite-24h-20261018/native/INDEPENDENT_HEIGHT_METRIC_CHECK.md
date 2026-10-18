# Fixed-height squared-energy curvature comparison

Disposition: PASS for the algebra and the fixed-height Q4/charged asymptotic comparison. The secondary ratio 5/2 is established by the currently proved L=10 block. Its all-even-height extension is a plausible coefficient generalization, but should remain conditional until the secondary isolation/orientation/transfer proof is extended explicitly.

Define the rest gap m and energy curvature a by E(q)=m+a|q|^2+o(|q|^2), in the common lattice momentum and energy units. Then E(q)^2=m^2+c_eff^2|q|^2+..., where c_eff^2=2ma. This is a squared-energy curvature coefficient; naming it c_eff does not itself establish Lorentz symmetry or a limiting signal speed.

## Charged versus Q4 bound mode

At each fixed even L>=10 the supplied leading coefficients are

 m_c=m_4=JDelta_L lambda^4[1+O(lambda^2)],
 a_c=Jgamma_L lambda^L[1+o(1)],
 a_4=2Jgamma_L^2/v_L lambda^(2L-8)[1+o(1)],
 gamma_L=binomial(2L-2,L-1)/8^(L-1),
 v_L=9L/32768, Delta_L=L/16.

Therefore

 c_4^2/c_c^2=(2gamma_L/v_L)lambda^(L-8)[1+o(1)] -> 0.

The equal leading rest gaps are important; this is not merely a comparison of the energy curvatures. The Q4 isotropic orientation regime still requires q<<lambda, because its diagonal imbalance and orientation splitting differ by two powers for every fixed L. Fixed-height local normal-form constants may depend on L. No bound uniform in growing L is implicit.

The generalization of the leading charged hopping and Q4 endpoint motion is supported by the native winding coefficient, the height-linear local diagonal coefficients, the same finite-support geometry, and the fixed-L construction in TEN_LAYER_NEUTRAL_BOUND_PROOF.md. A full actual-grid statement for each new L still chooses sufficient finite order and grid scaling for that L; one cannot reuse all L10 numerical exponents unchanged.

At L=8, v8/(2gamma8)=96/143<1, so the specific thin-arm endpoint binding mechanism does not produce a state below that continuum at leading order. Higher corrections cannot reverse a fixed strict threshold deficit asymptotically. This does not exclude other excitations. L=6 has a different upper bound-state mechanism and is not governed by the L>=10 formula.

## Secondary molecule

The proved secondary block is explicitly fixed at L=10. There

 m_s=2JDelta lambda^4[1+O(lambda^2)],
 a_s=(5/2)Jgamma^2/v lambda^12[1+o(1)],
 a_4=2Jgamma^2/v lambda^12[1+o(1)].

Consequently

 c_s^2/c_4^2 = (m_s/m_4)(a_s/a_4) -> 2*(5/4)=5/2.

This factor includes the doubled rest gap; comparing a_s/a_4 alone would incorrectly give 5/4. Both dispersions must be evaluated in their respective resolved isotropic regimes. For the L10 secondary molecule that requires q<<lambda^4, whereas Q4 needs only q<<lambda.

At any other fixed even L>8, the same local D8 geometry and two-hop calculation formally replace the powers by lambda^(2L-8), with the same a_s/a_4=5/4. The six-hop orientation process would have order lambda^(6L-40), implying the stronger crossover q<<lambda^(2L-16). The normal-form machinery is available at every fixed L, but that alone does not constitute the completed secondary spectral theorem: its competing-manifold isolation, leading orientation coefficient and remainder exponents must be restated and checked at that height. Thus publish the unconditional secondary ratio only at L10, and label the all-fixed-L expression as a coefficient consequence conditional on that extension.

## Common-metric boundary

A common rescaling of energy, time or lattice length multiplies both squared-energy curvatures by the same factor; it cannot remove either the fixed-L vanishing charged/Q4 ratio or the L10 ratio 5/2. A common reparameterization of the same lambda likewise does not equate these coefficients. Species-dependent coordinates would not be a common metric.

These results rule out identifying these particular derived branches with one common relativistic metric in this fixed-height weak-anisotropy limit. They are not a no-go theorem for all native excitations, other parameter regimes, growing-height limits, or all possible emergent theories. No observation or empirical speed is used.

Read native TEN_LAYER_NEUTRAL_BOUND_PROOF.md, CHARGED_COLUMN_POLE_PROOF.md and SECONDARY_NEUTRAL_MOLECULE_PROOF.md. No repository edits or formal audit.
