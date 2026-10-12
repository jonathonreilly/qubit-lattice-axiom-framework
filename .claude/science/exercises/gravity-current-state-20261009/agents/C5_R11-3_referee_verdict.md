# VERDICT: CONFIRMED WITH CORRECTIONS

The three option readings survive in their stated, bounded senses: V1 is SOURCED in the supplied linear preferred-time gravity; V2 is SOURCED through the homogeneous energy constraint but EXCLUDED when both cell volume and the existing site set are fixed; and V3 DECOUPLES constant isotropic vacuum tadpoles at linear order while the same fixed-site realization is EXCLUDED by the absence of isotropic expansion. The main corrections are to the claimed quantifiers and interpretations: M-coupling positivity needs a nonnegative kinetic contribution, the advertised edge tuning belongs only to the infinitesimal small-mass derivative and not the finite \(m:1\to0.3\) phase-transition step, the transition-sector pressure was not derived, and V3's displayed \(\omega=0\) determinant zero is a restored static gauge direction rather than a demonstrated additional physical scalar.

## 1. Vacuum stress formulas, integration by parts, and rerun

The formulas are correct conditional on the two stipulated forward stress vertices. With \(p_i=\partial_i(\epsilon^2/2)\), \(v_i=p_i/\epsilon\), and \(A_{ij}=\partial_i\partial_j(\epsilon^2/2)-\delta_{ij}\), the U prescription gives

\[
\rho=\frac12\langle\epsilon\rangle,
\qquad
p_U=\frac16\left\langle\frac{|p|^2}{\epsilon}\right\rangle.
\]

Periodicity gives

\[
0=\langle\nabla\!\cdot(\epsilon p)\rangle
=\left\langle\frac{|p|^2}{\epsilon}\right\rangle
+\langle\epsilon(3+\operatorname{tr}A)\rangle,
\]

and hence exactly

\[
\rho+p_U=-\frac16\langle\epsilon\operatorname{tr}A\rangle.
\]

This confirms the proof at `R11-3_report.md:117-123`. I reran `scripts/r113_tadpoles.py:17-81`; every displayed tadpole, box/edge split, and identity residual reproduced (`scripts/r113_tadpoles.out:3-34`). The supplied output file was restored byte-for-byte after the rerun.

Two scope qualifications matter. First, the identity is for U, not M; M differs by the edge-supported moment stated at `R11-3_report.md:123`. Second, “edge-carried” applies to the **full-zone sum** because \(A=0\) inside the box. It does not say that the box contribution to \(\rho+p\) vanishes: the box alone has positive \(w=0.2602,0.3246,1/3\) (`scripts/r113_tadpoles.out:21-24`). Finally, these are source formulas only after supplying the U or M stress completion; the report itself says the U pair-stress completion is assumed (`R11-3_report.md:52-56`), consistently with the prior referee's warning that the pair-creating scalar's Ward-exact completion was not built (`C5_R9-9_referee_verdict.md:5`).

## 2. Positivity theorem

For U, positivity is exact for every real positive dispersion: \(p_U\ge0\), so \(w_U\ge0\) (strict unless the band is flat). For M,

\[
p_M=\frac16\left\langle\frac{\sum_i u_i}{\epsilon}\right\rangle,
\]

so \(w_M\ge0\) follows only if \(\sum_i u_i\ge0\) pointwise (or at least if its weighted average is nonnegative). All actual L, G, NN, and L–G profiles used here meet that stronger condition, so the numerical and class-specific conclusion “no tested edge shape has \(w=-1\)” is sound (`scripts/r113_tadpoles.out:25-27`). But a merely positive band energy is insufficient: the smooth stable band \(m=2\), \(u_i=-1\) has \(\epsilon=1\) and \(w_M=-1\) (`referee_r113_checks.out:6-7`). Thus `R11-3_report.md:125-129` must replace “every positive band and both couplings” by “every positive dispersion for U, and every band with nonnegative spatial kinetic contribution for M.” Signed boson–fermion sums also have no positivity theorem, although a single sea copy keeps the same ratio because it flips both \(\rho\) and \(p\).

## 3. V1 and the “two tunings” claim

The linear codimension count is correct. At homogeneous \(q=0\), flat V1 requires both \(\rho_{\rm tot}=0\) from the lapse constraint and \(p_{\rm tot}=0\) from the spatial equation (`R11-3_report.md:166-175`). Proper-cubic \(\times\) time admits two invariant symmetric tadpoles, whereas \(W(B_4)\) or Lorentz symmetry admits one; this is exactly O1's confirmed \((V,S_2)=(1,2)\) versus \((0,1)\) count (`C5_O1_referee.md:7`; `TESTS.md:2377-2380`). A covariant \(\Lambda\sqrt{-g}\) counterterm moves only along \((\rho,p)\propto(1,-1)\), while the computed lattice vectors do not, so one such coefficient cannot make Minkowski stationary.

The strongest justified phrasing is therefore **two independent tadpole renormalization conditions in the linear preferred-time EFT**. The report verifies linear gauge compatibility of separate lapse and trace tadpoles, but supplies neither a nonlinear local completion nor radiative stability for them. If nonlinear diffeomorphism invariance is imposed, the second counterterm is unavailable and the result becomes an obstruction rather than “two allowed tunings.” Conversely, a structural correlation such as exact signed spectral pairing can cancel both conditions together. The report's bare “two tunings” language at `R11-3_report.md:28,166-176` is too broad without this qualification. The invariant count itself is confirmed; the further inference from one Euclidean \(W(B_4)\) tadpole to Lorentzian \(w=-1\) presupposes the appropriate Wick/source continuation, as the W-native note keeps its coupling conclusion conditional (`UNIVERSAL_GR_INDUCED_COSMOLOGICAL_CONSTANT_BOUNDED_THEOREM_NOTE_2026-06-08.md:37-45`).

## 4. Bianchi recovery, modes, and V2/V3 readings

The Bianchi-recovery algebra is correct provided the parent linearized identity and conservation of the **complete** matter stress hold. In V2 the imposed equations are \(E_{00}=E_{0i}=E_{ij}^{\rm TL}=0\), hence \(\partial_jE_{kk}=0\) and \(E_{kk}=f(t)\). In V3, \(E_{00}\) is no longer imposed and \(\partial_tE_{00}=0\), hence \(E_{00}=C(x)\), while \(E_{kk}=f(t)\) remains (`R11-3_report.md:180-186`). It follows that V2 retains the homogeneous energy constraint but absorbs homogeneous pressure, while V3 absorbs both constant isotropic tadpoles into two independent integration data at linear order. Calling only \(C_0\) “the residual \(\Lambda\)” is incomplete for a grid vacuum with \(p\ne-\rho\): \(f(t)\) is the separate pressure datum.

The determinant rerun reproduces V1 and V2's two TT poles and V3's factor \(-64q^6\omega^2(\omega^2-q^2)^2\) (`scripts/r113_options.out:7-10`). But the V3 \(\omega=0\) null occurs exactly because the \(\xi_0\) gauge vector has \(\delta h_{00}=-2\omega\xi_0\) and re-enters the constrained \(h_{00}=0\) subspace at \(\omega=0\), with \(\delta h_{03}=q\xi_0\) (`referee_r113_checks.out:8-9`; see also the residual-gauge choice in `scripts/r113_options.py:103-106`). The run therefore establishes two propagating TT modes plus a static gauge/integration sector; it does **not** by itself establish an additional physical scalar or its nonlinear strong coupling. RN L3's Hořava result is an external comparator, not a consequence of this determinant (`RN_L3_referee.md:14-15`).

The fixed-volume phase-transition discussion also overreaches at `R11-3_report.md:192-200`: conservation at fixed volume gives \(\Delta\rho_{\rm tot}=0\), but it does not give \(\Delta p_{\rm tot}=\Delta p_{\rm vac}-\Delta\rho_{\rm vac}/3\). That formula assumes the compensating latent energy becomes radiation. A specified transition sector is needed to compute its pressure. This does not change the constant-tadpole readings, but it removes the claimed universal V1 transient coefficient \(+0.128\) and limits local-bubble claims further because the full Ward-completed pair stress is absent.

“EXCLUDED as a fixed-site option” is legitimate under the registered text. The FIXED EXCLUDED criterion explicitly includes inconsistency with observed expansion (`TESTS.md:4180-4184`). With fixed local \(\sqrt h\) and unchanged lattice sites/adjacency, the isotropic expansion scalar vanishes; a homogeneous lapse is gauge in V2 and fixed in V3. Site creation/refinement would add structure beyond the supplied fixed \(Z^3\) Lattice (`MINIMAL_AXIOMS_2026-06-29.md:35-41`). Thus V2 and V3 are EXCLUDED **only as fixed-site metric realizations of observed isotropic expansion**. With a new site-creation/redshift law they remain OPEN, exactly as the report says (`R11-3_report.md:218-235`); nonmetric clock/redshift mechanisms are also outside this exclusion.

## 5. Step values, scale estimate, and site numbers

The finite \(m:1\to0.3\) values reproduce: \(\Delta\rho=(-0.109932,-0.082000,-0.096082)\) and \(\Delta p_U=(+0.091611,+0.018132,+0.009673)\) for L, G, NN (`scripts/r113_tadpoles.out:28-31`). The small-m coefficients reproduce as well (`scripts/r113_steps_sizes.out:1-7`).

The claimed “one edge tuning” needs a material correction. The solver at `scripts/r113_step_family.py:20-22` finds \(t_*\simeq0.00117\) only for the **infinitesimal \(m^2\to0\) derivative**, and a bracketing root is not a uniqueness proof over arbitrary profiles. An independent 101-profile scan of the actual finite \(m:1\to0.3\) step finds \(\Delta(\rho+p_U)<0\) throughout and \(\Delta p_U/\Delta\rho\in[-0.83335,-0.17546]\); M gives \([-0.29926,-0.27488]\). There is no \(-1\) point for that finite step in the tested L–G family (`referee_r113_checks.out:1-5`). Thus `R11-3_report.md:147-158` conflates a small-m response coefficient with its stated finite phase transition.

The \(6\times10^{87}\rho_\Lambda\) arithmetic is correct under its stated cutoff assumptions:

\[
0.1(100\,\mathrm{GeV})^2M_{\rm Pl}^2
=1.49\times10^{41}\,\mathrm{GeV}^4
=5.92\times10^{87}\rho_\Lambda,
\]

using the unreduced \(M_{\rm Pl}=1.221\times10^{19}\) GeV and \(\rho_\Lambda=2.52\times10^{-47}\) GeV\(^4\) (`referee_r113_checks.out:10`; `C5_O3_report.md:39-43`). It is a quadratically cutoff-sensitive fixed-grid contribution conditional on \(a=\ell_P\), not a regulator-independent electroweak vacuum jump.

The site arithmetic also reproduces: \(8.455\times10^{184}\) cells, \(3H_0N=5.58\times10^{167}\,\mathrm{s}^{-1}\), and \(3H_0t_P=3.56\times10^{-61}\) per site per Planck time (`referee_r113_checks.out:11-12`; worker code at `scripts/r113_V1_flow_and_numbers.py:32-38`). The rate \(3H_0N\) applies to a fixed comoving region chosen to equal today's quoted observable volume; it is not the full time derivative of the particle-horizon volume.

## 6. Readings

- **V1: SOURCED**, confirmed within the supplied linear U/M stress and N-type coupling. There are two independent homogeneous tadpole conditions in the cubic-times-time linear EFT, with the nonlinear completion and transition dynamics open.
- **V2: EXCLUDED as a fixed-site cosmology; SOURCED through energy density inside V2**, confirmed. Homogeneous pressure is absorbed into \(f(t)\); site creation/refinement is OPEN.
- **V3: DECOUPLED at linear order for constant isotropic tadpoles and conserved homogeneous fixed-volume transitions; EXCLUDED as a fixed-site cosmology**, confirmed with corrections. Its energy and pressure are absorbed separately into \(C(x)\) and \(f(t)\); the displayed \(\omega=0\) null is not a proved extra physical scalar. Site creation and its assignment of integration data are OPEN.

## Strongest correct statement

Conditional on the supplied free Gaussian bands, zero-point/sea completion, U or M stress vertex, a conserved complete source, and the linear N-type gravity coupling, the full-zone U tadpole obeys the exact torus identity \(\rho+p_U=-\langle\epsilon\operatorname{tr}A\rangle/6\), so for the nonnegative L/G/NN kinetic profiles its failure to have \(w=-1\) is encoded by an edge-supported anomaly moment; U has \(w\ge0\) for every positive dispersion, while M has that property only when its spatial kinetic contribution is nonnegative. V1 is sourced and flat space imposes two independent cubic-times-time tadpole renormalization conditions; V2 retains the energy constraint but not the homogeneous pressure equation; V3 absorbs constant energy and pressure into independent static/spatially homogeneous integration data at linear order. Fixed-site V2 and V3 cannot realize metric FRW expansion and are therefore excluded in that bounded realization, whereas adding site creation/refinement is an open new law. The reported tadpole values, \(5.9\times10^{87}\rho_\Lambda\) cutoff estimate, and site-count arithmetic reproduce, but the lone edge root applies only to the infinitesimal small-mass derivative, not the finite \(m:1\to0.3\) transition, whose compensating pressure was not derived.
