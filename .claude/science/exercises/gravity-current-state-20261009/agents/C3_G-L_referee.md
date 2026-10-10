# C3 lane G-L: referee verdict (codex gpt-5.6-sol, xhigh; other vendor; 2026-10-10)

## VERDICT: CONFIRMED WITH CORRECTIONS

The pre-registered outcome is **FAIL** for the mean of the unweighted massless one-hop scalar kernel \(G_0=aL\) on a fixed curved Poisson sprinkling. The corrections narrow the geometric, operator, and tensor scope; they do not change the FAIL.

### Findings

1. **Volume law and \(\nu\): confirmed, pre-caustically.**

   For a regular, causally isolated null tube with \(Q=P_y+P_x>0\),
   \[
   \int(\delta-\tfrac12\xi^TQ\xi)_+d^2\xi
   =\frac{\pi\delta^2}{\sqrt{\det Q}},
   \qquad
   \det Q=\frac{\det J(\Lambda)}
                 {\det J(\lambda)\det K(\lambda)}.
   \]
   Hence
   \[
   V=\frac{\pi}{24}\tau^4\nu,\qquad
   \nu=\frac6{\Lambda^2}\int_0^\Lambda
   \sqrt{\frac{\det J(\lambda)\det K(\lambda)}
                {\det J(\Lambda)}}\,d\lambda .
   \]
   This confirms `C3_G-L_report.md:47-55` and `work/gl_A_planewave.py:45-54`. It is exact for the plane-wave models; for a general smooth metric it is the leading thin-diamond coefficient. “No conjugate points” should be strengthened to exclude cut points/competing causal paths and require a regular tube (`C3_G-L_report.md:137`).

2. **Mean-link limit and GR comparison: confirmed, with a distributional qualification.**

   With \(s=\tau^2\) and \(a=\sqrt{\rho}/(2\pi\sqrt6)\),
   \[
   a e^{-\rho\pi\nu s^2/24}
   \xrightarrow[\rho\to\infty]{\mathcal D}
   \frac{\nu^{-1/2}}{2\pi}\,\theta_+\delta(s).
   \]
   The scalar Hadamard direct term is
   \[
   \frac{\Delta^{1/2}}{2\pi}\,\theta_+\delta(s),
   \]
   so
   \[
   M=\frac{\text{link}}{\text{GR}}=(\nu\Delta)^{-1/2}.
   \]
   This verifies `C3_G-L_report.md:28-36`; \(\Delta^{1/2}\) as the Hadamard direct coefficient is standard [Hadamard transport reference](https://arxiv.org/abs/0906.0005). The causal step function and distributional nature should be explicit. Exact plane-wave volume at all \(\tau\) does not make the finite-density kernel itself an exact delta distribution (`C3_G-L_report.md:124`).

3. **The NEC sign can be proved exactly—stronger than the appended check.**

   Raychaudhuri gives
   \[
   \operatorname{tr}P_y\le\frac2\lambda,\qquad
   \operatorname{tr}P_x\le\frac2{\Lambda-\lambda}.
   \]
   Because \(Q>0\),
   \[
   \sqrt{\det Q}\le\tfrac12\operatorname{tr}Q
   \le\frac{\Lambda}{\lambda(\Lambda-\lambda)},
   \]
   and therefore \(\nu\ge1\). The same comparison gives \(\Delta\ge1\). Thus under null convergence plus the regular pre-caustic assumptions, the link direct amplitude satisfies \(\nu^{-1/2}\le1\), while GR has \(\Delta^{1/2}\ge1\). Equality includes geometries with no optical focusing, such as conformally flat de Sitter null rays. This corrects the overly cautious statement at `C3_G-L_report.md:170`; “focusing” alone should be replaced by the precise hypotheses.

4. **Numerics: reproduced and decisive for the registered reading.**

   I reran the plane-wave Monte Carlo, independent deterministic plane-wave quadrature, thin-lens calculation, finite-difference Van Vleck check, conformal quadrature, and NEC search.

   - All 24 plane-wave Monte Carlo settings remain within \(2.52\sigma\): `work/gl_A_planewave.out:12-36`.
   - Independent quadrature agrees with the exact plane-wave volume law at roughly \(10^{-6}\): `work/verify/v1_planewave_quad.out:2-29`.
   - The clean thin-lens example has \(\Delta=4\), \(\nu=3/2\), and \(M=1/\sqrt6=0.408248\): `work/gl_C_thinlens.out:5,26`.
   - Deterministic conformal results converge to the same density-independent limits: `work/verify/v2_conformal_quad.out:2-7`.

   Caveats: the finite-difference check imports A’s world-function implementation (`work/gl_D_vanvleck_fd.py:5`), and B reuses correlated Monte Carlo point sets across densities (`work/gl_B_conformal.py:55-67`). The independent v1/v2 quadratures adequately close those gaps. The Gaussian conformal lenses violate NEC in their wings (`work/verify/v4_conformal_sign.out:5-6`), so they demonstrate net-focusing scalar mismatch, not a universal NEC lens theorem.

5. **Non-absorbability: endpoint claim confirmed; local-operator argument needs replacement.**

   The position dependence \(M=0.408\) versus \(0.426\) at fixed \(\Delta=4\) excludes a universal endpoint product \(f(x)f(y)\): `C3_G-L_report.md:76-79`, `work/gl_C_thinlens.out:5,16`.

   Flat endpoints alone do **not** prove that an arbitrary local first-derivative transport integral is position-independent. A correct stronger argument is:

   - For every short null segment, \(M=1+O(\Lambda^2)\).
   - A smooth scalar operator
     \[
     \Box_g+A^a\nabla_a+B
     \]
     has direct multiplier relative to \(\Delta^{1/2}\)
     \[
     \exp[-\tfrac12\int A\cdot k\,d\lambda]
     =1-\tfrac12\Lambda A\cdot k+O(\Lambda^2).
     \]
   - Matching all short null directions forces \(A\cdot k=0\) for every null \(k\), hence \(A=0\); \(B\) affects only the tail. That would leave multiplier one, contradicting the finite focusing examples.

   Thus non-absorbability holds for smooth second-order normally hyperbolic scalar operators with the same metric cone—not literally “any local operator.”

6. **Fixed reading and scope.**

   The controlled, asymptotically density-independent order-one mismatch meets the exact FAIL clause at `TESTS.md:645-648`, pre-registered before computation at `work/PREREG.md:13-30`.

   It does **not** automatically extend to:

   - **G-B tensor-on-links:** still **INCONCLUSIVE**, not PASS (`TESTS.md:603`). The report’s opening statement calling G-B a PASS is wrong (`C3_G-L_report.md:7`); its later scope statement is correct (`C3_G-L_report.md:138,143`). A tensor conclusion requires tensor parallel transport, gauge/source structure, polarization mixing, and tails.
   - **E1′:** unchanged. Its PASS is only the registered flat, scalar, source-driven proxy; the tensor/helicity-2 bridge remains outside scope (`TESTS.md:427-431`).
   - Weighted links, multi-hop propagation, BD-operator inversion, metric-aware density, and alternative readouts remain open (`C3_G-L_report.md:139-142`).

### Strongest correct statement

For a regular pre-caustic null geodesic in a smooth curved background, the continuum direct-cone mean of the unweighted one-hop kernel \(aL\) has weight \(\nu^{-1/2}\), whereas the scalar wave Green function has weight \(\Delta^{1/2}\). Their ratio is \((\nu\Delta)^{-1/2}\). Explicit Ricci- and Weyl-focusing plane waves and conformal lenses exhibit verified order-one discrepancies that survive \(\rho\to\infty\). Under null convergence, \(\nu,\Delta\ge1\), so genuine optical focusing makes the one-hop mean no larger than flat while GR’s direct amplitude is magnified. This confirms the bounded C3 G-L FAIL, without establishing a tensor-gravity no-go or excluding other link-based propagators.