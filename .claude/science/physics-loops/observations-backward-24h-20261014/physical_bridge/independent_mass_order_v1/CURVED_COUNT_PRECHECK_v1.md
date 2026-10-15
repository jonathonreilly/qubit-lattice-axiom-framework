# Independent curved finite-count derivation and frozen numerical protocol v1

This new check follows the frozen mass-order proof. It does not amend that proof. The root remains scientific author. I have read the full author curved working note but no curved implementation. The independent numerical protocol below is frozen before writing or executing my check. No author implementation of this fixture was exposed at this point.

## Scope and conventions

Take the supplied physical metric exp(2 epsilon h) a(t)^2 eta, a(t)=1/(1-Ht), on 0 <= t <= T < 1/H, a(0)=1. Set chi=a h and absorb alpha into epsilon. The unperturbed station and craft are comoving at x=0 and x=L e1. Assume prescribed constant source proper frequency and ideal instantaneous coherent turnaround with known phase multiplier. Receive at fixed station proper-time endpoints tau_0(t_i). Coordinate reception endpoints t_i=t_0+i Delta are equally spaced, but their proper-time spacings generally are not. No field equation is needed to derive this linear response. Actual curvature, field, energy, initial state and clock calibration are not inferred here.

## Independent derivation

The timelike geodesic equation in conformal coordinates is u'=-(1-|u|^2)[mathcal H u+epsilon(grad h+u partial_t h)]. At the comoving reference, linearizing gives delta u'+mathcal H delta u=-grad chi/a. Hence (a delta u)'=-grad chi. With initial velocity v_0, d(t)=1-Ht and P(t)=integral_0^t d(r)dr=t-Ht^2/2,

  delta u(t)=d(t)[v_0-integral_0^t grad chi(s,x_A)ds],
  xi(t)=xi_0+v_0 P(t)-integral_0^t [P(t)-P(s)] grad chi(s,x_A)ds.

In particular there is no extra d(s) in the force integral. The factor d(r) is integrated over the outer velocity-to-position propagation. The proper-clock equation tau'=a exp(epsilon h) sqrt(1-|u|^2) gives eta'=a h=chi: the velocity derivative vanishes at u=0 and the scale factor has no spatial gradient. Thus eta(t)=eta_0+integral_0^t chi(s,x_A)ds.

Conformal null curves obey the coordinate Minkowski light-time equations. For reference reception r=t, bounce b=t-L and emission e=t-2L, fixed receiver proper time requires delta r=-eta_s(t)/a(t). Linearizing the two separate null equations gives delta e=delta r+e1.[xi_s(e)+xi_s(t)-2xi_b(b)]. The source proper-time phase perturbation, divided by its known proper frequency and coherent multiplier, is therefore

  Phi(t)=eta_s(e)-a(e)/a(t) eta_s(t)
         +a(e)e1.[xi_s(e)+xi_s(t)-2xi_b(b)].

The craft clock has no direct term because the turnaround is an instantaneous phase copy. Its force response remains. A delayed/nonideal transponder or independent oscillator changes this model.

Let gamma=(-1,3,-3,1) and beta_i=d(e_i) gamma_i. Then beta_i a(e_i)=gamma_i. Gamma kills every degree <=2 polynomial in the equally spaced t_i. Consequently sum beta=0; initial station/craft positions and velocities cancel because P is quadratic; the single shared station clock initial offset cancels because beta_i[1-a(e_i)/a(t_i)]=2HL gamma_i. Transverse initial states have zero first-order range row. This cancellation concerns the supplied finite-dimensional initial state; it does not remove arbitrary clock-rate or model errors.

Define F_a(s)=sum_i gamma_i[P(t_i-a)-P(s)] 1_{s<t_i-a}. Then after initial-state cancellation the endpoint contrast is

  O[chi]=integral c_s(s) chi(s,0)ds
         -integral W_s(s).grad chi(s,0)ds
         -integral W_b(s).grad chi(s,L e1)ds,

  c_s=sum_i gamma_i[d(e_i)1_{s<e_i}-d(t_i)1_{s<t_i}],
  W_s=e1(F_2L+F_0), W_b=-2e1 F_L, c_b=0.

These are already chi weights; multiplying them by another a or d would be erroneous. The clock density is compact and piecewise constant. Each F is compact and continuous, piecewise quadratic with derivative -d(s)sum_active gamma; its derivative has finite jumps and bounded variation on the finite window. The moments sum gamma and sum gamma P(t_i-a) vanish, so the kernels are zero before their first knots, including before the initial slice.

The clock offset moment is exactly

  integral c_s = sum gamma_i[d(e_i)e_i-d(t_i)t_i]=0.

The bracket is affine in t_i; gamma annihilates it. This annihilates a constant comparison field chi. A constant physical h instead has chi=a h and need not be annihilated. It is not an initial-state or background selector.

For three adjacent normalized proper counts Y_i=[phase(tau_{i+1})-phase(tau_i)]/(kappa nu_0 Delta_tau_i), choose l_i=-Delta_tau_i sum_{j<=i} beta_j. Expanding sum l_i delta Y_i gives exactly sum beta_i Phi(t_i). Here tau_0(t)=-log(1-Ht)/H with its continuous H=0 limit t; using Delta rather than Delta_tau_i would not implement these normalized counts.

## Frozen independent protocol

1. Use exact rational/symbolic algebra for arbitrary H,L,t_0,Delta to verify beta moments, all scalar initial-state columns, clock moment and the three-count endpoint map.
2. With L=3/5,t_0=7/5,Delta=1, compute the H=0 massless common-field Gram from a different exact representation. For z=n.e1, the retarded-time density is a sum of 12 steps with coefficients gamma_i(1+z), gamma_i(z-1), -2z gamma_i at knots e_i,t_i,b_i-zL. Integrate its square by exact pairwise overlap min(k_j,k_l), splitting z only at rational knot crossings. The norm convention is integral(p^2+grad h^2), so pi G=(1/4)integral_{-1}^1 integral H_z(s)^2 ds dz. Compare to 329/54. This checks only the H=0 fixture, not a curved operator bound.
3. Independently compute the linear kernel action for smooth synthetic chi and compare with an independently integrated orbit/clock response followed by the two-null-event endpoint map. Include H=0, 1/25, 1/10, and nonzero initial position, velocity and shared clock perturbations. Check the proper-count realization using nonuniform proper-time spacings.
4. Integrate the original nonlinear conformal geodesic and proper-clock equations for epsilon=+/-0.002,+/-0.001,+/-0.0005 with DOP853 (rtol=2e-13, atol=2e-14). Invert the actual station clock at each fixed reference proper-time endpoint, solve the two null equations, and read actual emission proper time. Compare centered finite differences of the four-endpoint contrast and three-count realization against the linear kernel. Final error tolerance is 3e-6 max(1,|linear prediction|). Record all step errors; no claim of exact nonlinear cancellation beyond first order.
5. Check that a constant chi gives zero kernel action and include a constant physical-h diagnostic to distinguish it from constant chi. This diagnostic is not asserted to solve massive KG.

All checks are mathematical synthetic controls; no raw observations, author suite reruns, measured calibration, formal audit verdict or source edits. Preserve any failed run and subsequent changes as distinct versions.
