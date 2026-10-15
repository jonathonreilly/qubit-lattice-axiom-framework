# Curved coherent finite-count construction and comparison-Gram check v1

Date: 2026-10-15. Reviewer: /root/localized_history_check. Root remains scientific author. This report records a focused construction/source check, not a formal audit or a combined landing verdict. The preceding mass-order proof and report remain unchanged.

## Independence, exposure and scope

I read all 230 lines of CURVED_COUNT_WORKING_v1.md, treating its final finite-count section as the target and the rest as context. I then froze my derivation and numerical protocol before reading any curved author implementation, and executed the resulting 63-control independent script. After the root requested the H-dependent comparison Gram, I froze a separate Gram derivation/protocol and executed a second independent script with 10 controls. Only after both executions did I open the complete 85-line CURVED_COUNT_COMPOSITION_v1.md and 219-line curved_count_controls_v1.py; this exposure is timestamped and bound to the independent Gram result in CURVED_COMPOSITION_EXPOSURE_v1.json. The author result JSON was subsequently inspected for identities and reported diagnostics. No author code was imported or executed. No actual observations were accessed.

The construction check covers original conformal test-body/clock/null equations, all stated finite-dimensional initial orbit/clock columns, the three proper-count implementation, transformed clock/force weights, their regularity, the zero comparison-field offset, and the exact massless comparison Gram. The time-varying-potential operator comparison, its high-frequency proof and conservative energy/error suppliers are not independently validated by this report; the separately assigned curvature reviewer owns that work. Reading those sections is not being counted as checking them.

## Original equations and scale factors

Use the supplied physical metric exp(2 epsilon h) a(t)^2 eta, a(t)=1/d(t), d(t)=1-Ht, a(0)=1, and chi=a h. Epsilon contains alpha for this calculation. The reference station and craft are comoving at 0 and L e1, and the observations use ideal instantaneous coherent turnaround with known multiplier kappa and constant source proper frequency nu_0.

The exact coordinate test-body equation is

  u'=-(1-|u|^2)[mathcal H u+epsilon(grad h+u partial_t h)].

At the comoving reference, its linearization is delta u'+mathcal H delta u=-grad chi/a. Therefore

  (a delta u)'=-grad chi,
  xi(t)=xi_0+v_0 P(t)-int_0^t [P(t)-P(s)]grad chi(s,x_A)ds,
  P(t)=t-Ht^2/2.

There is no extra d(s) factor in this position kernel: d(r) multiplies the velocity and integrates to P(t)-P(s). The proper-clock equation tau'=a exp(epsilon h)sqrt(1-|u|^2) gives eta'=chi at the reference. Thus eta=eta_0+int chi. The zero first derivative of sqrt(1-|u|^2) at u=0 matters; this simplification is not valid for a general moving reference.

Let reception, bounce and emission reference times be r=t, b=t-L and e=t-2L. Fixed receiver proper time gives delta r=-eta_s(r)/a(r). Linearizing the two separate conformal null equations gives

  delta e=delta r+e1.[xi_s(e)+xi_s(r)-2xi_b(b)].

Consequently the emitted phase response divided by kappa nu_0 is

  Phi(t)=eta_s(e)-a(e)/a(r) eta_s(r)
          +a(e)e1.[xi_s(e)+xi_s(r)-2xi_b(b)].

This reproduces the author endpoint formula and identifies which clock and scale factor belong to each event. The spacecraft clock has no direct response in this ideal coherent model. The spacecraft force/position response survives. A proper turnaround delay, independent oscillator, medium, non-geodesic force or electronics response requires additional modeling.

## Initial data, finite proper counts and transformed kernels

For t_i=t_0+i Delta, gamma=(-1,3,-3,1) and beta_i=d(t_i-2L)gamma_i, beta_i a(e_i)=gamma_i. Gamma annihilates all degree <=2 polynomials. Initial station/craft positions and velocities therefore vanish from sum beta_i Phi(t_i), since their position histories are xi_0+v_0 P(t). The shared station initial clock offset has coefficient sum gamma_i[d(e_i)-d(r_i)]=2HL sum gamma_i=0. Transverse initial orbit components have zero first-order line-of-sight row at this comoving reference. The craft clock is absent. These are initial orbit/clock cancellations, not cancellation of arbitrary scalar initial data or arbitrary clock-rate histories.

The endpoint sum is zero because beta is gamma times an affine function. For normalized successive proper counts

  Y_i=[phase(tau_{i+1})-phase(tau_i)]/(kappa nu_0 Delta_tau_i),

choose l_i=-Delta_tau_i sum_{j<=i} beta_j. Then sum l_i delta Y_i=sum beta_i Phi(t_i) exactly. The proper labels are tau_0(t)=-log(1-Ht)/H, continuously extended to tau_0=t when H=0. Their spacings differ from the conformal spacing Delta. Multiplication by kappa nu_0 restores raw phase/count units; these known calibration factors have not been derived from observations.

Substituting the orbit and clock solutions gives

  O[chi]=int c_s chi(s,0)ds-int W_s.grad chi(s,0)ds-int W_b.grad chi(s,L e1)ds,
  F_a(s)=sum gamma_i[P(t_i-a)-P(s)]1_{s<t_i-a},
  W_s=e1(F_2L+F_0), W_b=-2e1 F_L,
  c_s=sum gamma_i[d(e_i)1_{s<e_i}-d(r_i)1_{s<r_i}], c_b=0.

These are already transformed chi weights. Another factor a or d must not be applied. Each F is continuous, compact, piecewise quadratic, and has a derivative of bounded variation. Cancellation before its first knot follows from sum gamma=0 and sum gamma P(t_i-a)=0. Its derivative is -d(s) times the active step sum. The clock density is compact and piecewise constant. This confirms the regularity claimed in the construction section.

The zero moment is exact:

  int c_s=sum gamma_i[d(e_i)e_i-d(r_i)r_i]=0,

because the bracket is affine in r_i. This eliminates a constant comparison field chi. It does not generally eliminate constant physical h, for which chi=a h. As a synthetic distinction, the same kernel gives 0.00020606761793495995 at H=0.04 and 0.005462524827664879 at H=0.1 for chi=a (h=1), while it gives zero within 2e-14 for chi=1. Constant h in this diagnostic is not asserted to solve massive KG. Neither cancellation selects H, a physical homogeneous field, an energy budget or a scalar initial state.

## Exact comparison Gram

For L=3/5, t_i=7/5+i and z=n.e1, use common null time s=t-n.x. The correct density is

  H_z(s)=sum gamma_i {
    [d(e_i)+z d(s)]1_{s<e_i}
    +[-d(r_i)+z d(s)]1_{s<r_i}
    -2z d(s+zL)1_{s<b_i-zL} }.

In particular the craft derivative is evaluated at its own coordinate time s+zL. The factor d(s+zL) cannot be replaced by d(s). Station and craft contributions are summed before squaring, retaining their common-field covariance.

With the real massless energy norm N=int(p^2+|grad chi|^2), angular/temporal Parseval gives

  G_0(H)=(1/(4 pi))int_{-1}^1 dz int_R H_z(s)^2 ds.

I independently integrated all pairwise products of the 12 step-polynomial terms, from 0 to their exact minimum knot. Each pair is split only at its rational knot crossings. Across the full set the direction cuts are -1,-2/3,2/3,1; there are 84 pair pieces. Exact rational integration gives

  G_0(H)=[646969 H^2-454020 H+98700]/(16200 pi).

This agrees exactly with the author G1 and exact_gram. The H=0 value is 329/(54 pi), as obtained separately in the first script. The coefficient Gram in (1,H), after multiplying by pi, has determinant 20537167/437400>0, a consistency check on positivity and interference. As a different representation, I sorted the 12 knots at direction quadrature nodes and integrated the squared summed density on each adjacent temporal interval. Those values agree with the rational polynomial at H=0,1/25,1/10,1/5 with maximum absolute error 1.333e-15 in pi G. All these H values lie below 5/22 except the formal polynomial is not restricted algebraically; the physical chart interpretation is restricted to 0<=H<5/22.

This is the norm of the curved-derived count weights propagated by a free massless comparison field. It is not the actual curved/massive propagation norm. It supplies the comparison term in a further bound only if that bound's separate hypotheses are established. It also does not establish a measurement-derived energy calibration.

## Execution evidence and source correspondence

Both independent scripts passed on their first run; no failed attempts or tolerance repairs occurred in this phase. All stdout/stderr and exact identities are preserved. The first script has 63 controls, including exact symbolic initial/count/moment identities, independent kernel-versus-linear-ODE checks, and finite differences of the original nonlinear conformal geodesic/clock equations at fixed receiver proper endpoints. It inverts the actual receiver clock, solves both actual null events, then reads actual emission proper time. The two smooth synthetic fields were tested at H=0,0.04,0.1 with nonzero initial orbit and clock perturbations. Epsilon steps were 0.002,0.001,0.0005 with both signs. The largest final error against the linear kernel was 9.717401661113456e-8, below the frozen 3e-6 max(1,|prediction|) criterion. The three-count and four-endpoint representations were checked independently within those runs. These synthetic fields test response kinematics; they are not asserted to solve the scalar field equation.

The second independent script has 10 controls and supplies the exact H-dependent Gram plus the distinct sorted-interval checks described above. These 73 new controls are separate from my prior 120 mass-order controls and from the author's 20 recorded controls. No unchanged author suite was rerun.

After exposure, the author weights, exact_gram, proper-count endpoint conversion, and mode-and-observation endpoint map correspond to the derivation above. Its exact Gram uses sorted active intervals, whereas my primary exact computation uses pairwise minimum-knot overlaps. The author mode ODE check is linear and supplies a different field family from my nonlinear metric/null-event finite differences. The author result identities match the frozen sources. Its reported response error 2.1519505332378858e-10 and initial-state leakage 3.8284420997391375e-10 match the companion note's rounded statements; those numbers remain author-run evidence. The author global angular quadrature is explicitly labeled a finite diagnostic; the rational interval integration is the exact supplier.

## Scoped outcome and remaining premises

No discrepancy was found in the checked endpoint/count construction, transformed weights, stated cancellations or exact comparison Gram. The claims require the specified chart, a(0)=1, comoving geodesic reference, fixed receiver proper labels, supplied constant source proper frequency, known coherent multiplier and instantaneous ideal turnaround. Initial orbit/clock cancellation is first order; no nonlinear cancellation theorem is asserted. The construction removes those finite-dimensional nuisance columns without determining the scalar initial data. Actual observed H, action parameters, energy normalization, calibration, non-geodesic forces, hardware/media effects and observation residual/error budgets remain open. This report does not endorse the separate propagation enclosure, apply a formal audit verdict, or authorize a combined landing.

## Exact identities

The following source and evidence identities are frozen for this report. Full paths and this report's own hash are in the identity sidecar.

- Author `CURVED_COUNT_WORKING_v1.md`: `84cb8fb11a008f6ca8fd268f20f1dede6d5aaded0b4a206065e93f57acba4ba2`.
- Author `CURVED_COUNT_COMPOSITION_v1.md`: `dae8894dd8740055d12a9f84b59a33146e95e9284fc2046cd132c514593c7ce3`.
- Author `curved_count_controls_v1.py`: `4a272c55ab3ba6a81b51bd3c1d33519a38cd13bd3b7d3a382c600baf43f79ae2`.
- Author `CURVED_COUNT_RESULTS_v1.json`: `204a5b8eaed4773dc8cc8d69e52557544d83483a86d5bc4463f902b9609cb46c`.
- Independent `CURVED_COUNT_PRECHECK_v1.md`: `21a052975ec0a87df00e8f9dd1e704f09d7ae755fc067dc276bc0f2a248d3619`.
- Independent `CURVED_COUNT_PRECHECK_IDENTITY_v1.json`: `0a525306fa0441cfda42757b05399735c9f27244f55fbb4a25b464a0fa68756f`.
- Independent `independent_curved_count_check_v1.py`: `6a4d6c3df4734a733a33f74b2267625db6de44806edce0c8b5c592a0d42eb770`.
- Independent `INDEPENDENT_CURVED_COUNT_RESULTS_v1.json`: `356d19394c40a0cb90fdd1709aa508e060c8165d1e4d2a5bcfb038c03fd6352d`.
- Independent `INDEPENDENT_CURVED_COUNT_RUN_v1.stdout`: `e0c02a21c95feccd6c5333d457c704dc8b9278d4f55b93f23f79e6c687cdf454`.
- Independent `INDEPENDENT_CURVED_COUNT_RUN_v1.stderr`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- Independent `CURVED_GRAM_PRECHECK_v1.md`: `be7bd0f52840ac47c9f3671218fc3daf45dc24775314e0628263ea32bba9b907`.
- Independent `CURVED_GRAM_PRECHECK_IDENTITY_v1.json`: `25623ab2b789169af7e83225f189f448213816e23404b91998230d54564c612b`.
- Independent `independent_curved_gram_check_v1.py`: `8ed31e5a33d937cfe5dbd66a8af0f8849b54484fec76de4e0f9f4923df168fc3`.
- Independent `INDEPENDENT_CURVED_GRAM_RESULTS_v1.json`: `5c93dbd32dc2615589b036e67b087ff7bd81e365f788d75bd887cdd563f899a1`.
- Independent `INDEPENDENT_CURVED_GRAM_RUN_v1.stdout`: `b4b2289b70605c6932926bd995ba2461b0d5ea90346839d32858348cac96ad01`.
- Independent `INDEPENDENT_CURVED_GRAM_RUN_v1.stderr`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- Independent `CURVED_COMPOSITION_EXPOSURE_v1.json`: `acc512240e503449ee1569d663be1a550318ba6fa7f05a60d6f198dea4f232e1`.
