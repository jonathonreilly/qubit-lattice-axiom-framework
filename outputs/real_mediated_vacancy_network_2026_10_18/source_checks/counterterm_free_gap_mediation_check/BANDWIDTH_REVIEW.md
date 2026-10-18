# Distinct check of the ladder bandwidth and constructed packet

**Disposition: SUPPORT at the stated infinite-graph scattering/constructed-packet scope. No required correction found.** The full core inverse estimates and first derivative bounds are valid. The normalized packet argument can be completed directly using half-line Fourier tails, without an absence-of-bound-states or spectral-completeness assumption. This does not supply a physical product launcher, a finite-time released gate, or a finite physical implementation of the infinite leads.

## Sources and exposure

N denotes `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`. I fully read and hash-verified `N/counterterm_free_gap_mediation/BANDWIDTH.md`, 9106 bytes, SHA256 `1193e84952ce9cd8d80fdc79b8723f474b9319b0d1c70d65ea31e56f66806e90`.

Its exact stationary core source is `LADDER_SCATTERING_REDUCTION.md`, SHA256 `4f22fdb84d7636a6caad536323e5f02f971fba04a22ae9e8292e3c4e234929cc`. I just fully checked that source in `LADDER_SCATTERING_REVIEW.md`, SHA256 `e2aaddf2f55f39fa82aebea45c22dbade0fbc3e245b489f7ea8d9b1e06bc6c01`. That unchanged work is reused, not counted as a second independent check. In particular its actual positive diagonal sums, port phases, and center transmission are premises here. The earlier compensated network and mediator approximation retain their separate finite-global-norm scopes; neither is used to infer an infinite physical approximation.

ROOT requested this bandwidth interface, and the source author and I share campaign and design exposure. I did not author the changed bandwidth proof. This is a distinct same-model source-exposed analytical check, not blind checking, retained audit, publication approval or a general physical-realization claim. No scientific executable, coefficient scan, delegation or model override was used.

## 1. Finite matching convention

Let P insert the two port amplitudes. With z=exp(ik), the first exterior value is z times the port value plus (z^{-1}−z)a. Inserting this into the core stationary equation indeed gives

    F=H_core−E I−z PP†,
    F T a=−2i sin(k) P a,
    S=P†T−I.

Thus the source has the correct sign of the outgoing self-energy and incident forcing. At each port, incoming plus outgoing equals P†T a. The port is counted only as n=0 of its lead, with the four remaining internal vertices added separately. Both leads have the same E=2−2cos k and positive velocity 2sin k on the stated band. No sector-dependent Jacobian is required.

## 2. Full inverse and derivative estimates

Write the four internal vertices as outer pair (v,w) and inner pair (A,B). Their outer block at the center is d I, d=f/4, while the residual inner Schur block is [0,−p;−p,0]. Its inverse norm is one. The outer-to-inner elimination map has norm two. The inverse blocks therefore obey

    ||K^{-1}_{oo}|| <= d^{-1}+4,
    ||K^{-1}_{oi}|| <= 2,
    ||K^{-1}_{ii}|| <= 1.

For an arbitrary vector decomposed into these two groups, applying the triangle inequality separately to its two component norms bounds the operator by the symmetric nonnegative comparison matrix [d^{-1}+4,2;2,1]. Its norm is at most its largest row sum d^{-1}+6=8sqrt(2)+6<18. This is a full four-dimensional estimate, independent of p.

The port/internal coupling columns have disjoint supports and squared lengths (f/2)^2+(3f)^2=37/32, so their matrix norm is sqrt(37/32)<2. The outgoing port Schur matrix has eigenvalues 2p−i and −p/2−i, hence inverse norm 2/sqrt(5)<1. The block inverse identity then yields

    ||F(k0)^{-1}|| < 18+(1+18*2)^2=1387<1400.

The lifted factors used in this bound are valid even though the port Schur inverse is complex: the internal inverse and coupling maps are real symmetric/adjoint pairs, and only submultiplicativity is used.

Since ||F(k)−F(k0)||<=3|k−k0|, the Neumann product is at most 0.42 on the closed 10^{-4} interval. Thus the sharper immediate estimate 1400/(1−0.42)<2414 is available, and the source's 2800 is valid. Separately, the internal K perturbation has norm at most 2*10^{-4}, whose product with 18 is below one. Both elimination and outgoing matching remain nonsingular.

Differentiation gives R'=−R F' R with ||F'||<=3 and therefore ||R'||<=3*2800^2=23,520,000. Differentiating −2i sin(k) R P gives the valid bound

    ||T'|| <= 2*2800+2*23,520,000=47,045,600
             <48,000,000.

Projection gives the same bound for T_int' and S'. The maps themselves obey ||T||,||T_int||<=5600. All are full maps, not transmission-only estimates. Direct sums over old sectors preserve these constants, as do passive tensor extensions.

## 3. Current conservation and spectral error

For a real stationary energy, sum the local continuity equations over the finite six-vertex core. Internal currents cancel in pairs because the matrix is selfadjoint, leaving the two outgoing lead currents. Each is 2sin(k)(||a_j||^2−||(Sa)_j||^2); incident/outgoing interference contributes no net current. Thus ||Sa||=||a|| for every a. Since S is a square finite matrix, it is unitary. This also follows algebraically from F−F†=−2i sin(k) PP† and the forcing convention above.

The operator-valued fundamental theorem of calculus gives

    ||S_p(k)−S_p(k0)|| <= 48,000,000 |k−k0|.

Using the checked center S_p(k0)=−exp(−i theta) w_p X_ports gives the stated full scattering bound, including reflection and differing sector delays. It retains the common scalar −exp(−i theta). A narrow bandwidth does not imply that the constant is useful in practice; the estimate is simply explicit and sufficient at this scope.

## 4. Square summability and exact evolution

For smooth compactly supported g in the interior of the band, extend g by zero to the full momentum circle. Its complete integer-lattice incoming Fourier sequence has norm ||g||_2=1 by the convention 1/sqrt(2pi). The outgoing complete sequence has norm ||Sg||_2=1 as well. Restricting each to n>=0 preserves square summability, so their sum is square summable; the four internal integrals are finite. Port consistency from Section 1 ensures the stationary equation also holds at n=0.

The infinite graph has bounded degree and bounded coefficients, so its one-head Hamiltonian is a bounded selfadjoint operator. Differentiation of the packet integrals is justified by compact support and bounded E. More strongly, Fourier/Parseval estimates permit differentiation in Hilbert norm; the finite internal coordinates cause no additional issue. The packet therefore satisfies the exact Hilbert-space Schrodinger equation. This is not merely a collection of formal component solutions.

## 5. Remote-past normalization, including phase curvature

Here is the necessary tail estimate with the potentially time-dependent second derivative retained. On any forbidden half-line at remote time, the phase derivative has magnitude at least n+vT, where n>=0, T=|t| and v=min_I E'>0. For amplitude a(k) and phase phi(k), integration by parts yields

    |integral a exp(i phi) dk|
      <= ||a'||_1/(n+vT)
         + T ||E''||_infty ||a||_1/(n+vT)^2
      <= [||a'||_1+||E''||_infty ||a||_1/v]/(n+vT).

Boundary terms vanish by compact support. Thus the sum of squared forbidden amplitudes is bounded by a finite constant times sum_{n>=0}(n+vT)^{-2}, which tends to zero. The curvature term has not been omitted or incorrectly assumed independent of time.

For the incoming exponent −kn−tE at t=−T, the excluded negative indices have derivative |n|+T E'; hence the incoming n>=0 norm tends to one. For the outgoing exponent kn−tE at t=−T, every n>=0 has derivative n+T E', so its retained half-line norm tends to zero. The amplitude Sg and its derivative are integrable by the established estimates. The internal integrals tend to zero by the same one-dimensional nonstationary argument, with amplitudes T_int g. Cross terms vanish by Cauchy–Schwarz. The exact full packet norm therefore tends to one as t tends to minus infinity. Norm conservation then makes it exactly one at every finite time.

At positive infinite time, the incoming half-line instead vanishes and the outgoing complete sequence concentrates on n>=0. The internal integrals again vanish. The asymptotic outgoing spectral amplitude is Sg, with its actual phase. This proves the claimed construction without showing that the constructed packets span the whole Hilbert space. In particular, it does not exclude point spectrum or certify the continuum weight of an arbitrary localized seed.

The argument works for finite-dimensional vector amplitudes, including coherent old-sector inputs and passive references. The uniform operator estimates extend the map isometrically by density from smooth compactly supported amplitudes to arbitrary L2 amplitudes on the narrower support; the elementary integration-by-parts proof itself only needs to be applied on the smooth dense domain. This supplies the intended interpretation of the source's final arbitrary-amplitude statement.

## 6. Complete outgoing comparison and limits

For normalized amplitudes supported in |k−k0|<=h, pointwise operator multiplication and integration give

    ||Sg−[−exp(−i theta) W X_ports]g||_L2
       <=48,000,000 h.

The ideal comparator has norm one, and Parseval transfers this estimate to the complete outgoing sequences. The future asymptotic restriction to physical half-lines is justified above. This is not a uniform finite-time complete-state comparison: internal fields and residual incoming tails at a chosen finite time would need their own quantitative budgets. The source states this limitation correctly.

The conclusion preserves arbitrary coherent old-sector and passive inputs at the scattering-packet level. Restoring the physical application must still retain old elapsed aging, physical common scalars and effective mediator evolution from the separate approximation theorem. A stationary fiber result does not remove those factors.

A physical product-seed launcher, its spectral mass and localized remnants, finite lead endpoint diagonals, finite cuts/returns, quantitative release-window vacancies and actual network approximation costs remain unproved here. The infinite ideal graph cannot be substituted into a finite-global-norm mediator bound. No absence of bound states, full spectral completeness, permanent halt, native supplier or finished finite release is claimed or established.

## Verification record

I fully read the frozen changed source, verified its hash, and reconstructed the matching signs, complete inverse estimate, derivative arithmetic, current normalization, Hilbert-space evolution, nonstationary tails including their curvature term, and outgoing spectral comparison analytically. No scientific executable or numerical scan was used. This report was fully read back. Only BANDWIDTH_REVIEW.md was written for this check; source files, previous reports, Git, canonical/checkpoint files and editable prompts were unchanged.
