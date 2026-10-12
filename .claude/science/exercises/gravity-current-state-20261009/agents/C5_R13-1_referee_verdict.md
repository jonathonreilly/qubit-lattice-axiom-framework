# VERDICT: CONFIRMED WITH CORRECTIONS

1. **Free level — partly confirmed.** Lemma F is a correct *fiberwise* representation criterion only when \(E(k)\ge |p(k)|\) and the levels have the required \(2+2\) long or \(1+1\) short multiplicities; it is not true for literally “any” \(p\). Nor does it construct the smooth/quasi-local field-level vector-multiplet charge, which the report itself leaves open (`R13-1_report.md:124-137,250-252`). F1’s conclusion—algebra alone does not force a species-independent momentum—is correct, but its example \(p_\gamma=\lambda k\) is not periodic on \(T^3\); use \(p_\gamma=\lambda S(k)\), \(p_e=S(k)\) instead (`R13-1_report.md:138-144`). F3’s massless-short conclusion is correct, but the massive bound is false without an additional quadratic-dispersion or naturalness hypothesis. For example,
   \[
   M^2(k)=m^2e^{-A|S(k)|^2/m^2}
   \]
   is smooth, periodic and positive, gives \(E\ge |p|\), but \(c_e^2=1-A\), which can lie far below \(1-m^2/b^2\). The explicit check gives \(c_e^2=0.5\) versus the claimed \(0.99\) bound ([check:17](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R13-1/R13-1_referee_checks.py:17>), [output:1](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R13-1/R13-1_referee_checks.out:1>)).

2. **Theorem B and Jacobi — confirmed with a notation correction.** Conservation of \(Q\) and \(\bar Q\) indeed gives
   \[
   [H,\{Q_\alpha,\bar Q_{\dot\beta}\}]
   =2\sigma^i_{\alpha\dot\beta}[H,P_i]=0,
   \]
   and linear independence of the Pauli matrices forces every \([H,P_i]=0\) (`R13-1_report.md:162-167`). The transverse Peierls vertex then yields
   \[
   p_{e,x}(k_x+q)-p_{e,x}(k_x)=p_{\gamma,x}(q)
   \]
   for all \(k_x\), not necessarily the displayed equation with \(S\). Periodicity forces \(p_e\) constant, contradicting \(p_e=k\) on the box. Thus the no-go holds for \(C^1\), one-body, band-scalar \(P\) with the stated whole-zone Peierls coupling. It does not cover dressed/higher-body, band-matrix, nonlocal or infinite-flavour momentum; the checked \(2\!\to\!2\) example is not a class-wide dressed-\(P\) theorem (`R13-1_report.md:168-181`).

3. **Corollary BPS — only the photon half is confirmed.** With minimal one-particle content and axial \(C_4\), the two photon helicities cannot be the two bosons of a long multiplet because long-multiplet bosons have the same \(C_4\) eigenvalue. Hence the photon multiplets are short and \(E_\gamma=|P|\), giving \(c_\gamma=1\) (`R13-1_report.md:185-187`). The electron conclusion is only \(E_e(k)\ge |k|\) pointwise. It does **not** imply the claimed low-momentum bound or forbid \(c_e<c_\gamma\) at finite mass. Consequently, negative \(\Delta=c_e-c_\gamma\) is not by itself a BPS violation; the independently nonzero photon correction is still incompatible with that exact minimal-content algebra. GNP correctly assumes the ordinary supercharge–translation algebra and standard superfields, and excludes dimension-three LV and dimension-four LV in the MSSM, but it does not supply the report’s massive lattice slope inequality. [GNP](https://arxiv.org/html/hep-ph/0404271)

4. **One-loop numbers — confirmed as numbers for the defined model.** Fresh reruns reproduced `r131_checks`, the partner cross-check, and all eight \(m=0.05,N=128\) rows exactly. All 24 sampled laws have \(\Delta<0\), with the quoted \(m=0.05\) ranges (`scripts/r131_electron_sqed.out:3-18`; `scripts/r131_electron_sqed_m0.1.out:3-10`; `scripts/r131_electron_sqed_m0.05.out:3-10`). The \(4\times4/8\times8\) comparison again agrees within \(2.3\times10^{-13}\) (`scripts/r131_partner_crosscheck.out:1-2`). A separate brute-force eigenvector sum, avoiding the trace-reduced projector implementation, agrees in the self-energy and speed coefficient to \(1.4\times10^{-17}\) and \(2.2\times10^{-15}\), respectively ([check:30](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R13-1/R13-1_referee_checks.py:30>), [output:2](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R13-1/R13-1_referee_checks.out:2>)). These remain model results for the chosen off-D1 Yukawa and selectron gauging, with numerical rather than rigorous error bounds (`R13-1_report.md:227-238`).

5. **Lemma LIT — confirmed; scope matters.** One Dirac contribution contains
   \[
   \frac{a x^2}{4E^3}-\frac{AX^2}{4E^5},
   \]
   while two complex selectrons contribute \(+AX^2/(4E^5)\), so the \(A\)-moment cancels pointwise and leaves
   \[
   \delta c_\gamma=
   \left\langle
   \frac{(S_x'^2-1)S_y'^2}{4E^3}
   \right\rangle
   =
   \left\langle
   \frac{(\partial_q\Delta)(\partial_q\Delta+2)S_y'^2}{4E^3}
   \right\rangle .
   \]
   The independent algebraic residual is zero ([output:3](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R13-1/R13-1_referee_checks.out:3>); `R13-1_report.md:201-211`). Its sign varies by shape, so it is not a universal nonzero obstruction and can be tuned through zero. It establishes only the literal-edge photon leg—not the complete electron–photon split—as a defect moment. The \(4\times4\) Clifford maximum of five generators is correct, so the specific separable three-velocity/three-Wilson-direction Clifford-flat construction needs an eight-component module; it is not a no-go against every four-component regulator (`R13-1_report.md:212-213`).

6. **Reading — confirmed as INCONCLUSIVE.** PASS fails because no field-level exact spinor \(Q\) with zero one-loop split was constructed. FIXED FAIL also fails because no photon doubler is proved unavoidable, the full split is not proved to be a defect moment, and untuned removal is not excluded (`TESTS.md:4592-4595`; `R13-1_report.md:264-282`). The doubler-free Majorana–Wilson photino is confirmed only spectrally; smooth global intertwining by a quasi-local \(Q\) remains open (`R13-1_report.md:240-252`). “Leaning FAIL” is a fair description of the sampled minimal continuation, not a theorem about the registered class.

**Strongest correct statement.** On the free Brillouin zone, abstract modewise \(N=1\) representations exist when the stated multiplet multiplicities and pointwise inequality \(E\ge|p|\) hold, but the algebra neither identifies \(p\) with lattice translation momentum nor constrains a massive particle’s infrared speed by the claimed \(1-m^2/b^2\) bound; a smooth/quasi-local field-level charge for the proposed vector multiplet is still unconstructed. In the narrower interacting class with \(C^1\) periodic, one-body band-scalar momentum and the whole-zone Peierls vertex, Jacobi plus the nonvanishing transverse vertex rigorously forbids an exact D2 supercharge algebra. For the chosen off-D1 completion of minimal box SQED, the rerun one-loop split is negative in all 24 sampled laws, while the literal-edge photon coefficient is exactly a sign-indefinite moment of the product-rule defect; neither result proves untuned class-wide non-removability. Therefore the fixed campaign reading is **INCONCLUSIVE**, with a sharp bounded Theorem B and a confirmed model-specific one-loop obstruction.