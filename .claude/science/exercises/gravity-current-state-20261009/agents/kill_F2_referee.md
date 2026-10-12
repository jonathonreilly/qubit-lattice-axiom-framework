# Other-vendor referee of the F2 kill (codex gpt-5.6-sol, xhigh), verbatim

## VERDICT ON THE KILL: **NOT CONFIRMED**

The calculations are reproducible and identify serious obstructions to the simplest Gaussian implementation of F2, but they do not establish the universal verdict “F2 is dead.” The decisive overreach is from particular free-field kernels, two gauge-path prescriptions, and an axis-curvature theorem to all reflection-positive, gauge-covariant, locally generated implementations and to a nonzero TT vacuum stiffness.

## Item findings

1. **Gauge transporters — numerical result confirmed; claimed Ward-identity no-go not confirmed.**

   The Ward identity and the reported \(O(e^2)\) residual are implemented correctly for the 2D scalar-QED model ([K4_gauge_paths_oe2_stiffness_2d.py:75](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_KF2/K4_gauge_paths_oe2_stiffness_2d.py:75>), [K4_L48.out:23](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_KF2/K4_L48.out:23>)). I reproduced the \(s=1.5\) result and found it stable when the Hessian step was varied from \(0.04\) to \(0.01\).

   The power fits are narrower than stated:

   - Uniform staircases, \(s=1.25\ldots2\): \(X_1\simeq s^{-2.59}\), but \(X_2\simeq s^{-1.78}\).
   - L-shaped paths: \(X_1\simeq s^{-2.54}\), whereas \(X_2\) is nonmonotone and gives only an ineffective \(s^{-0.73}\) fit ([K4b_lshape.out:2](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_KF2/K4b_lshape.out:2>)). This is persuasive evidence of a non-Gaussian residual for these paths, not an asymptotic theorem.

   More importantly, the Ward identity fixes only the longitudinal divergence of the flow. Arbitrary divergence-free lattice currents may be added, and the files do not optimize or bound that freedom. Only uniform monotone staircases and two L-shaped paths are tested ([K4_gauge_paths_oe2_stiffness_2d.py:33](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_KF2/K4_gauge_paths_oe2_stiffness_2d.py:33>), [K4b_mu_and_path_robustness.py:10](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_KF2/K4b_mu_and_path_robustness.py:10>)). Karsten–Smit concerns fermion doubling/chiral symmetry, not a theorem that every gauge-covariant transporter produces this power tail. Gauge-invariant fixed-point actions provide a concrete untested counter-family, including localized gauge transporters in 2D U(1) models ([Karsten–Smit](https://doi.org/10.1016/0550-3213(81)90549-6), [fixed-point Schwinger action](https://arxiv.org/abs/hep-lat/9707024)). Collins supports a generic radiative Lorentz-naturalness problem, not a strict impossibility theorem for one light cone ([Collins et al.](https://arxiv.org/abs/gr-qc/0403053)).

2. **Fermions — substantially confirmed, with scope corrections.**

   The odd, periodic Dirac kernel necessarily vanishes at every \(k_i\in\{0,\pi\}\), hence at all eight TRIM corners ([K1_dirac_sea_smooth_kernel.py:6](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_KF2/K1_dirac_sea_smooth_kernel.py:6>)). The rerun agrees exactly with the supplied output. Independent fits over \(s=1\ldots2\) give logarithmic slopes \(-4.82\) and \(-5.00\) against \(s^2\), consistent with \(-\pi^2/2=-4.935\).

   The “54–94% flat band” is specifically the fraction satisfying \(\omega<0.05\,\omega_{\max}\), not an exactly flat spectral band ([K1_dirac_sea_smooth_kernel.py:18](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_KF2/K1_dirac_sea_smooth_kernel.py:18>), [K1.out:33](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_KF2/K1.out:33>)). The smooth Wilson term removes that diagnostic flat region and is consistent with \(e^{-\pi^2s^2}\) until roundoff dominates ([K1.out:39](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_KF2/K1.out:39>)).

   Mass tuning is a generic interacting Wilson-fermion consequence because chiral symmetry is broken and additive mass renormalization is allowed, but it is not calculated by K1 and need not literally be independent for every flavor when symmetries relate them. ([Critical mass of Wilson fermions](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.63.017501)).

3. **Lemma N — bound confirmed, equality case incorrect, spatial/stiffness conclusions conditional.**

   For a scalar Gaussian covariance with a positive, normalized transfer matrix and sufficient differentiability, the representation is correct. At fixed spatial momentum,
   \[
   S(z)=c_0+\int_{t>1}\frac{d\mu(t)}{t-z},
   \]
   so \(-D=-1/S\) is Nevanlinna and
   \[
   D(z)=a-bz-\int\frac{d\nu(t)}{t-z},\qquad b,\nu\ge0.
   \]
   Expanding \(z=\cos q\) gives
   \[
   \sigma^2=\frac13+\frac{D''(1)}{D'(1)}.
   \]
   With \(u=t-1\), one can normalize \(-D'(1)\) to a probability measure and set \(y=u/(u+2)\), with the \(b\)-term represented by \(y=1\). Then
   \[
   R=E[y^2],\qquad \sigma^2+\frac23=E[y^{-1}],
   \]
   and Hölder yields \(R\,(\sigma^2+2/3)^2\ge1\). Thus the displayed bound at [K3_rp_face_curvature_bound.py:10](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_KF2/K3_rp_face_curvature_bound.py:10>) is correct.

   The equality statement is incomplete. Equality also occurs for the pure affine case \(\nu=0,\ b>0\), giving \(\sigma^2=1/3,\ R=1\). The runner itself exhibits this counterexample in its one-covariance-atom tests ([K3_rp_face_curvature_bound.py:74](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_KF2/K3_rp_face_curvature_bound.py:74>), [K3.out:3](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_KF2/K3.out:3>)). Correct equality: either pure \(b\), or \(b=0\) with \(\nu\) supported at one pole. For \(\sigma^2>1/3\), only the latter remains.

   Transfer to a spatial axis is exact only if the complete inverse propagator has a symmetry interchanging that axis with Euclidean time ([K3_rp_face_curvature_bound.py:12](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_KF2/K3_rp_face_curvature_bound.py:12>)). Equality of the origin kinetic coefficients \(c_t=c_s\) alone does not transfer the outer-zone bound.

   Most importantly, no supplied argument converts a nonzero axis face curvature into a lower bound on the integrated metric Hessian defining TT vacuum stiffness. Cancellations over the Brillouin zone are not excluded. Hence “face floor ⇒ stiffness floor” remains an open lemma, not an exact consequence of Lemma N. The Gaussian reflection-positivity violation itself is confirmed for the tested kernels ([K3.out:11](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_KF2/K3.out:11>)).

4. **Locality — arithmetic confirmed; universality overstated.**

   For a fixed-label cutoff, the reported residuals are roughly \(10\!-\!70\) times \(e^{-R^2/(2\sigma^2)}\) over the useful sampled range ([K2.out:6](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_KF2/K2.out:6>)). Solving for \(10^{-102}\) gives \(R/\sigma\simeq21.7\!-\!21.9\). The scalar fit reaches \(10^{-100}\) at \(\sigma\simeq4.82\), yielding \(R\simeq105\!-\!106\), reasonably rounded to 107. An integer radius-107 ball contains 5,130,710 noncentral sites, so “about \(5\times10^6\) couplings per site” is correct.

   The proper-distance hard cutoff is not described by the quoted \(10\!-\!70\) prefactor: its metric-dependent indicator changes the included lattice set under shear and can make the finite-difference Hessian nonsmooth ([K2_locality_truncation_and_nn_generation.py:57](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_KF2/K2_locality_truncation_and_nn_generation.py:57>), [K2.out:5](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_KF2/K2.out:5>)).

   The \(\sigma^{-6}\) and \(\sigma^{-8}\) behavior is evidence for the two heat-flow constructions actually coded ([K2_locality_truncation_and_nn_generation.py:63](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_KF2/K2_locality_truncation_and_nn_generation.py:63>), [K2.out:14](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/referee_KF2/K2.out:14>)), not a theorem for every finite-range generator. Higher-order improved stencils, auxiliary-field realizations, multiscale constructions, and fixed-point actions are unexamined. Effective long-range kernels generated by microscopic nearest-neighbor evolution also do not automatically contradict nearest-neighbor fundamental adjacency.

## Strongest correct statement

On fixed \(Z^3\), the specific smooth-kernel package studied here is badly obstructed: the free scalar Gaussian obtains exponential TT suppression, but its fully Euclidean-time-smooth version violates reflection positivity; an odd massless Dirac realization has unavoidable TRIM zeros and an increasingly large near-zero region, while the tested Wilson cure sacrifices chiral mass protection; direct truncation to the required accuracy costs roughly five million displacement couplings per site; and the tested low-order local generators and two gauge-path ensembles retain power-law rather than Gaussian interaction residuals. What is not established is a universal no-go for every reflection-positive, gauge-covariant, locally generated or perfect-action construction on fixed \(Z^3\), nor a theorem converting Lemma N’s face-curvature bound into a nonzero TT vacuum stiffness.