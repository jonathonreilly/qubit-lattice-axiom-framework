# VERDICT: CONFIRMED WITH CORRECTIONS

1. **Lemma D — confirmed within the explicit E1 model.** For a rigid body with \(\omega=\mathbf k\!\cdot\!\mathbf v\), a frame-tied gain with \(\operatorname{Im}F_t=\delta\omega+\cdots\) gives
   \[
   \mathbf F_{\rm self}=-\frac{4\pi G}{3}\delta\!\int\!\rho^2\,d^3x\,\mathbf v+O(v^3).
   \]
   For \(F_t=(1-i\omega\tau)^{-n}\), \(\delta=n\tau>0\). The neutron-star polytrope coefficient is \(1.6424\times10^8\,{\rm s^{-2}}\). Double-Pulsar agreement with GR at \(1.3\times10^{-4}\) gives \(\Gamma<6.14\times10^{-21}\,{\rm s^{-1}}\), \(\delta<3.74\times10^{-29}\,{\rm s}\), and \(\ell<3.74\times10^{-21}\,{\rm m}\) for \(n=3\), excluding the stated interval by \(10^{11}\)–\(10^{15}\). The orbital relation \(\dot P_b/P_b=-3\Gamma\) remains valid after averaging an eccentric Kepler orbit; unequal stellar drags require a mass-weighted \(\Gamma_{\rm eff}\). The formula should retain spatial-smearing vertex factors, but \(\ell/R_{\rm NS}\) makes their effect negligible. (`R13-6_report.md:352-387`; `scripts/r136_referee_checks.out:1-7`.) Kramer et al.’s precision is verified in [arXiv:2112.06795](https://arxiv.org/abs/2112.06795).

   No GR-like cancellation exists inside the written preferred-frame scalar-feedback model. Such a cancellation would require additional reciprocal, Lorentz-covariant, or strong-field dynamics. Lemma D does **not** apply to R6-4, whose mean backreaction is instantaneous and has \(\delta=0\). (`C5_R11-5_report.md:131-145`; `C5_R6-4_report.md:49-68`.)

2. **P-r13b — repair confirmed, residual statement corrected.** For \(n=4\),
   \[
   (1-4ix)(1-ix)^{-4}:\qquad \operatorname{Im}F=20x^3-84x^5+\cdots .
   \]
   The smooth-polytrope residual is \(5.64\times10^{-29}\,{\rm s^{-1}}\) at \(\ell=5\,\mu{\rm m}\), safely below the bound. However, \(6(v\tau/a)^2\) is specific to the worker’s Gaussian width convention; the \(n=1\) polytrope coefficient is \(4\pi^2=39.4784\) when expressed using \(R\). The \(7.9\) ps \(\tau_c\) ceiling remains profile- and orbit-model-dependent. P-r13b changes R11-5’s literal gain, so it defines a repaired class rather than rescuing the literal one. (`R13-6_report.md:389-397,429-434`; `scripts/r136_referee_checks.out:9-16`.)

3. **Lemma S — confirmed at its stated scope.** The \(J_0\) Laplace transform gives the claimed causal factor
   \[
   \hat H=(\Omega^2-(\omega+i0)^2)^{-1/2},\qquad \hat H^2=G_R.
   \]
   R11-5’s \(s_0=0\) profile has Stieltjes density
   \[
   \rho(t)=\frac{\epsilon-t}{\pi\sqrt t\,(\epsilon^2-t)},
   \]
   which is negative for \(\epsilon^2<t<\epsilon\). Thus no positive cone-centred Lorentzian synthesis exists. This does not exclude other line shapes, finite \(s_0\), or R13’s single-port realization. (`R13-6_report.md:170-229`; `C5_R11-5_report.md:168-175`; `scripts/r136_referee_checks.out:18-22`.)

4. **Finite-start covariance and CP — partially confirmed.** The finite-age covariance of \(h\) is correct and \(\operatorname{Var}h\sim[\ln(8\Omega T)+\gamma_E]/(2\pi\Omega)\). But
   \[
   \dot h=\xi-\Omega(J_1*\xi),
   \]
   so the worker’s \(\dot h\) calculation omitted a white-noise boundary term. Pointwise \(\operatorname{Var}\dot h\) and naive derivative energy are therefore not finite without bandwidth regularization. Finite rational meter networks are CP; exact irrational \(s_0=0\) CP remains conditional on a specified convergence topology and quantum initial-state limit. (`R13-6_report.md:236-290`; `scripts/r136_checks.py:141-154`; `scripts/r136_referee_checks.out:24-28`.)

5. **E2-h drag — scale confirmed, status remains suggested.** The weak-field result
   \[
   \Gamma_{\rm E2}=\frac{2\gamma|U|}{3Mc^2}
   \]
   is correct. A uniform neutron star gives \(\gamma<0.0436H_0\); a polytrope gives roughly \(0.03\)–\(0.04H_0\). Calling the effect “common-mode” is incorrect: equal absolute-velocity drags also damp the relative orbit. Because E2-h lacks a nonlinear strong-field completion, this is an order-of-magnitude bound, not a controlled neutron-star theorem. Its inherited unrepaired \(F_u\) is separately excluded by Lemma D. (`C5_R12-7_report.md:140-145`; `C5_R12-7_referee.md:138-145`; `scripts/r136_referee_checks.out:30-33`.)

6. **Reading — confirmed with a sharper class boundary.** Under the fixed criteria (`TESTS.md:4682-4692`), the literal R11-5 gain is **EXCLUDED** for every \(\ell_s\). The zero-first-moment model is a changed, **OPEN** construction—not VIABLE—because exact-limit regularity/CP and the conserved spin-2 assembly remain unresolved. (`R13-6_report.md:460-479`.)

## Strongest correct statement

Within the explicitly stipulated linearized, preferred-CMB-frame E1 model using R11-5’s literal causal gain \(e^{-k^2\ell^2/2}(1-i\omega\ell/c)^{-n}\), \(n\ge3\), a compact body necessarily acquires a leading self-drag \(-(4\pi G/3)(n\ell/c)(\int\rho^2)\mathbf v\), up to negligible spatial-smearing and order-unity stellar-structure corrections; Double-Pulsar timing then requires \(\ell\lesssim4\times10^{-21}\,\mathrm m\), excluding every \(\ell_s\) in the stated class by at least eleven orders of magnitude. This does not cover R6-4’s instantaneous kernel or arbitrary Lorentz-covariant or reciprocal CQ completions. A signed zero-first-moment gain removes the leading drag and passes the strict \(\tau=\ell/c\) test, but it is a changed, still-OPEN model whose exact irrational finite-start regularity/CP and full spin-2 completion remain unresolved.

Artifacts: [concise verdict](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R13-6/C5_R13-6_referee_verdict.md:1>), [full report](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R13-6/C5_R13-6_referee.md:1>), and [independent checks](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R13-6/scripts/r136_referee_checks.out:1>). Both worker and independent check scripts rerun exactly.