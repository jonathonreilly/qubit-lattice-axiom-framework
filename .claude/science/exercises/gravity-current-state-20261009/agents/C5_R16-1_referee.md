# VERDICT: CONFIRMED WITH CORRECTIONS

The fixed R16-1 reading is **DERIVED** for the stated one-loop Peierls Wilson subclass described below. The proof does cover the subluminal D1 laws with (0<r\le 1/\sqrt3) at (b=1.4,1.2,1.0) and every fixed \(\lambda>0\). Corrections are needed to the sharp K′ threshold, the registration and endpoint scope of (H0), one momentum-independent term in the displayed static energy, and claims of uniqueness for the numerical zero. The P-b Yukawa extension remains **SUGGESTED**, as the worker ultimately labels it.

## 1. Theorem W: heavy expansion, \(\Omega\), and photon derivative

**Confirmed, with two local corrections.** At fixed \(|p|<b\), (H0) gives (E_k\ge m), while (E_p=\sqrt{m^2+p^2}\). Thus the normal denominator is not literally “at least \(\lambda\)” for nonzero (p), as stated at `R16-1_report.md:116`; the correct uniform bound is

\[
W_\gamma+E_k-E_p\ge \lambda-\frac{p^2}{2m}\ge \frac\lambda2
\]

for (m) sufficiently large in a fixed small (p)-neighbourhood. The Z denominator is at least (2m+\lambda). Together with bounded (C^2) symbols and bounded Peierls difference quotients, this is enough to justify the (1/m) expansion with two (p)-derivatives. In particular,

\[
E_k-E_p=w(k)-w(p)+O(m^{-1}),\qquad
X_+=\sum_j\frac{[W(p_j)-W(k_j)]^2}{d_j^2}-1+O(m^{-1}),
\]

uniformly with the required derivatives, while the Z graph is (O(m^{-1})). This validates `R16-1_report.md:116-122` after the denominator wording is repaired.

The algebraic identity for the momentum-dependent part is correct:

\[
\Phi(u)-\Phi(0)
=\frac{u[D^2-t(1-A')]}{2tW_\gamma D(D+u)}=\Omega(q;u).
\]

An independent symbolic reduction gives zero residual for this identity, the (h(s)) decomposition, and the (q)-derivative identity (`r161_referee_checks.out:1`; implementation at `r161_referee_checks.py:93-100,321-352`). The torus shift correctly moves (p) into the photon slot while holding (u=W(q_x)) fixed, so

\[
L=\frac12\left\langle \partial_{q_x}^2\Omega(q;u)\big|_{u=W(q_x)}\right\rangle .
\]

The correction is that the equality for the full static energy at `R16-1_report.md:123` omits the (p)-independent transverse tadpole

\[
C_\perp=\left\langle\frac{W(q_y)}{2d_y^2W_\gamma}+\frac{W(q_z)}{2d_z^2W_\gamma}\right\rangle.
\]

It should read (\delta E^{(0)}(p)=C_\perp+\langle\Phi(q;0)\rangle+\langle\Omega(q;W(p-q_x))\rangle). This has zero (p)-derivative and does not change (L) or the no-interval theorem.

The conversion from energy to speed has the correct factor: (\delta c_e=m\delta E''(0)/2+\delta E(0)/(2m)=Lm+O(1)) (`R16-1_report.md:124`). On the photon side, the R10-1 moment has scalings (a x^2/E^3=O(m^{-3})), (AX^2/E^5=O(m^{-2})), (c_1(h\cdot h')X/E^5=O(m^{-3})), and (c_2X/E^3=O(m^{-2})), confirming \(\delta c_\gamma=O(m^{-2})\) (`R16-1_report.md:126`; source moment at `scripts/r101_dirac_moment_copy.py:28-41`).

The independent coefficient computation uses second-order automatic differentiation in (t=d_x^2), rather than finite-differencing \(\Omega\). It gives, in (16\pi^2) units:

- D1\((1.4,1/\sqrt3)\), naive photon: (L=+0.2265459594);
- BQ S3, naive photon: (L=+0.5066378991);
- BQ S3 with photon box \((2,3)\): (L=-0.2864994078).

These reproduce the worker values (`r161_referee_checks.out:3-5` versus `R16-1_report.md:135,139,196`). The independently evaluated tuned law converges to (L\,16\pi^2=-8.1\times10^{-10}) (`r161_referee_checks.out:7`), corroborating the sign-changing behavior outside (H2′). The reported (c_0\simeq-2.15) is a three-mass numerical extrapolation, correctly not a proof (`R16-1_report.md:197`; `scripts/r161_tuneL.out:3-4`).

## 2. Lemmas K and K′

**Confirmed, with a corrected sharp threshold.** In Lemma K, (A'=\rho_y^2+\rho_z^2\le2), so (2-A'\ge0). If (A'\le1), (K_0=B'^2+T(1-A')\ge0). If (A'>1), both transverse Wilson legs are outside the box and

\[
K_0=d_y^2+d_z^2-(\rho_zd_y-\rho_yd_z)^2+\lambda^2(1-A')
\ge \min(d_y,d_z)^2-\lambda^2\ge0.
\]

The product-of-resolvents argument then makes (g(t)) decreasing and convex, and the displayed identity

\[
\partial_q^2\Omega=(6-t)(g/t^2-g_t/t)+(4-t)g_{tt}>0
\]

is correct for (t=2-2\cos q); its (t=q^2) analogue is also correct (`R16-1_report.md:149-160`; symbolic residual `r161_referee_checks.out:1`).

For K′, the split into \(\Omega_1+\Omega_2\), the bound \(|\phi_t|\le3\phi/(2s^2)\), and (B'^2\ge A'\tau) are valid (`R16-1_report.md:161-167`). Solving the tangency of

\[
2(6-t)\tau(t+\tau)-3(2-t)t^2
\]

gives \(\tau_*=0.248715478877561\) and

\[
b_*=\arccos(1-\tau_*/2)=0.504032267857\ldots .
\]

Thus (b=0.505) is a safe rounded-up sufficient threshold, but `R16-1_report.md:60,161` should not call it the smallest threshold. The independent minimum is negative at (b=0.504), positive at (b=0.505), and strongly positive at all three D1 values (`r161_referee_checks.out:8-14`). This correction does not affect any claimed D1 member.

## 3. Lemma A_W and (H0)

**Lemma A_W is confirmed under (H0), but (H0) is not part of the registered \(\mathcal Q_W\) definition.** The fixed registration only requires (W) even, periodic, and (C^2) (`TESTS.md:5044-5047`); the minimal axioms do not select a Hamiltonian or kinetic branch (`MINIMAL_AXIOMS_2026-06-29.md:114-130`). The report itself introduces (W\ge0\), (W\not\equiv0) only in the narrower \(\mathcal Q_W^+\) (`R16-1_report.md:56-60`). It must therefore travel as an explicit law-class restriction, not as registered content.

Under that restriction, (E_k\ge m) at (p=0), the normal denominator is at least \(\lambda\), the Z denominator is positive, and compactness supplies a uniform complex-(m) neighbourhood. The electron and Theorem-D photon integrals are therefore real-analytic for (m>0), so the identity theorem applies (`R16-1_report.md:95-105`; compare the previously refereed scope at `C5_R13-7_referee_verdict.md:24`).

There is one endpoint correction: \(\mathcal Q_W^+\) contains D1 only for (0<r\le1/\sqrt3), because (r=0) has (W\equiv0) and violates (H0). The report acknowledges (r>0) in its membership table (`R16-1_report.md:66`) but overstates “every (r\le1/\sqrt3)” at `R16-1_report.md:192,277`. If the fixed notation is intended to include (r=0), that literal-edge boundary is covered separately by the refereed R13-7 theorem (`C5_R13-7_referee_verdict.md:17-24,30`); it is not covered by Theorem W.

## 4. Probe (c) and numerical checks

**Confirmed as numerical evidence, not as a uniqueness proof.** The reported (m=0.005,0.01) values give the stated linear intercept \(\Delta(0^+)\,16\pi^2\simeq-10.877\) (`R16-1_report.md:204-223`). Independent cubature with separately assembled on-shell and photon-moment integrands gives

- (m=0.1): \(\Delta\,16\pi^2=-10.793668\), versus (-10.7937);
- (m=2.0): \(\Delta\,16\pi^2=-7.648614\), versus (-7.6487).

The two independent resolutions are recorded at `r161_referee_checks.out:16-19`, and the implementation is at `r161_referee_checks.py:167-293`. A focused refined run brackets a crossing between (m=24.0) and (24.5), with \(\Delta\,16\pi^2=-0.00258\) and (+0.11700), respectively (`r161_referee_checks.out:20-23`). Analyticity makes every such zero isolated. However, neither analyticity nor the sampled monotonic table proves that this is the *unique* zero on all (m>0); “one zero near 24” should be read as one observed/bracketed zero, not a global zero count (`R16-1_report.md:223-225`).

## 5. Partner variants

**(P-a) confirmed; (P-b) only SUGGESTED.** For two matched selectrons without a Yukawa coupling, the electron self-energy is unchanged at one loop. In the scalar photon moment, the heavy vertex grows at most as (mW'), while the matched scalar energy grows as (m); after the Ward/f-sum subtraction the surviving terms are (O(m^{-2})) or smaller. This is consistent with the exact scalar formulas (`scripts/r131_photon_sqed.py:20-43`) and the reported heavy scans (`R16-1_report.md:227-229`). Hence P-a has the same positive (L), analytic \(\Delta\), and interval no-go.

P-b does not reach proof level. The asserted normal-denominator bound \((1-v)|q|\) at `R16-1_report.md:231` is not uniform on the boundary law (r=1/\sqrt3), whose (v_{\max}=1). More importantly, the report does not supply an integrable bound uniform in (m) after two (p)-derivatives, nor the promised complex-(m) treatment of the massless-photino threshold; finite scans through (m=102.4) cannot replace those steps (`R16-1_report.md:230-235`). The worker's final classification of P-b as SUGGESTED is therefore correct (`R16-1_report.md:281-283`). The fixed \(\mathcal Q_W^P\) variant itself names the two selectrons, not this extra Yukawa extension (`TESTS.md:5048`).

## 6. Whole-zone \(v_{\max}\)

**Confirmed at the level needed by R16-1.** R14-1's exact componentwise Cauchy--Schwarz bound gives

\[
|\nabla E|^2\le\frac{3r^2M^2+\sum_j s_j^2}{M^2+\sum_j s_j^2}\le1
\]

for D1 with (r\le1/\sqrt3) (`C5_R14-1_report.md:188-193`; referee confirmation at `C5_R14-1_referee_verdict.md:15`). At the boundary (r=1/\sqrt3), an independent diagonal optimization finds (v=1) at (k=1.450216519) for (b=1.4,m=0.3), agreeing with the worker (`r161_referee_checks.out:25`; `scripts/r161_vmax_D1.out:1-3`). For (r<1/\sqrt3) and (m>0), the final inequality is strict.

The R8-5 boxes are certainly superluminal: independent diagonal witnesses already give (v=3.311813220) for S1 and (4.651256536) for S3 at (m=0.3) (`r161_referee_checks.out:26-27`), matching `scripts/r161_firstorder.out:11-12`. The full table's exact maxima are numerical grid/line estimates rather than certified global optimizations, but that caveat cannot change the superluminal classification (`scripts/r161_vmax_BQ.out:1-8`).

## 7. Fixed-reading decision

**DERIVED is met.** The load-bearing class is: one loop, Feynman gauge, Peierls coupling, fixed \(\lambda>0\); (s,W,t=d^2\) with the regularity and box exactness in `R16-1_report.md:55-56`; (W\ge0\), (W\not\equiv0); (H2′); and either (H3) or (H3′), with any additional photon-only species required explicitly to have analytic, bounded one-loop contributions (`R16-1_report.md:57-61,184-192`). This class contains D1 at (b=1.4,1.2,1.0) for every (0<r\le1/\sqrt3) and fixed \(\lambda>0\). In it (L>0), \(\delta c_e=Lm+O(1)\), and \(\delta c_\gamma=O(m^{-2})\), so \(\Delta_\lambda\to+\infty\); Lemma A_W then excludes an open interval of zeros. This is exactly the fixed criterion's allowance for a “stated Wilson class containing D1” (`TESTS.md:5057-5061`). Counter-routes outside (H2′), a tuned (L=0), \(\lambda=0\), P-b, non-Peierls vertices, and two loops remain explicitly outside the theorem, so the result is not a universal all-Wilson no-go.

**Strongest correct statement.** At one loop in (Z^3\times\mathbb R), with Feynman gauge, Peierls coupling and fixed \(\lambda>0\), every box-exact Wilson law with (W\ge0\), (W\not\equiv0), an (H2′) photon, and either (H3) or the naive-edge condition (H3′) has \(\delta c_e(m)=Lm+O(1)\) with the displayed photon-slot coefficient (L>0), while its Dirac photon contribution is (O(m^{-2})); hence the real-analytic split \(\Delta_\lambda(m)\) is not identically zero and cannot vanish on any open mass interval. This class contains the subluminal D1 laws for (0<r\le1/\sqrt3) at (b=1.4,1.2,1.0) (with the (r=0) boundary supplied separately by R13-7), and it extends unchanged to the selectron-only P-a variant. It does not establish the P-b Yukawa extension, \(\lambda=0\), photon transitions on the Wilson edge, or a global count of isolated zeros; numerically D1\((1.4,1/\sqrt3)\) has \(\Delta(0^+)16\pi^2\simeq-10.877\) and a bracketed isolated crossing near (m=24\).
