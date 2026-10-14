# A finite-mode inverse with arbitrary scalar preparation

**Date:** 2026-10-14
**Status:** proposed_retained
**Claim type:** bounded_theorem
**Actual current surface status:** conditional-support
**Primary runner:** [exponential_scalar_finite_mode_inverse_check.py](../scripts/exponential_scalar_finite_mode_inverse_check.py)

Setting unobserved scalar waves to zero would supply an initial-state rule.
This note instead retains them and proves a parameter inverse within a
specified vacuum Fourier experiment. Two weighted potential measurements
identify two parameters when their moment matrix has nonzero determinant.
An ideal continuous trace is identifiable, while a preselected pair of windows
can fail. A separate certificate expresses uncertainty using measured values
and adopted error envelopes. No actual initial state, action, absolute scale,
environment or empirical parameter value is derived.

## Supplied action and experimental domain

Use the full action and coefficients in the
[future-confinement note](EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md):

    Q integral sqrt(-g_E)[R_E/2-K_AB partial(phi^A)partial(phi^B)-2Hv^2 U]
        +S_m[C g_E,matter],
    Q=Q0(1+k)>0, Hv>0, 0<k<1/3, nu>0.

The chosen homogeneous state is its exact vacuum phi=(u,x,y)=0 on the
expanding spatially flat de Sitter sheet, H=Hv. Write
a=(1-k)(1+3k)/4, alpha=sqrt(a), s=(1+k)/[k(1-3k)],
E=exp(2alpha u), F=1+sE, J=1+(1-3a)sE. Along x=y=0,

    K_uu=J/F^2, C=(1+s)E/F,
    U=3/2+3s(E-1)^2/(2F^2)+nu(1+s)u^2/(2F^2).

Direct differentiation at the vacuum gives C=1, grad U=0,
|grad_K ln sqrt(C)|^2=k, and coupled scalar mass

    B=m_u^2/H^2=4[3(1+k)+nu]/(1-3k)>12.             (1)

The other two linear scalar directions do not couple to the matter trace at
this state. They are not observationally determined by this experiment.
The complete supplied action remains a premise, including the choice of
potential away from the vacuum and the normalization Q0,Hv.

Take a nonzero comoving Fourier wave number q, p=q/a_E and z=p/H>0.
A weak cold comoving source has density coefficient delta rho proportional
to a_E^-3, zero first-order momentum and pressure. It is conserved to this
order. An individual signed Fourier coefficient is a calculation component;
it is not asserted to be a positive material density by itself. It can be
part of a small nonnegative localized distribution over the finite interval.
Weak-source linear validity and actual access to the paired physical metric
potentials at known times and known z are experimental premises.

## Exact finite-wave equation

The Einstein density, momentum and pressure equations give the common
Einstein potential Phi=-delta rho/(2Q p^2), with Phi_dot=-H Phi. Scalar
excitation energy and momentum beyond the constant vacuum term begin at
quadratic order. The constant vacuum stress's linear metric variation is
already included in the background Einstein equations.

Let b=grad_K ln sqrt(C) at the vacuum and write its coupled scalar
perturbation xi=b Phi y. Keeping both free initial data for y, its exact
linear equation is

    y_tt+H y_t+[p^2+(B-2)H^2]y=p^2,
    y_zz+(1+A/z^2)y=1, A=B-2.                       (2)

The physical potentials are Phi_J=Phi(1+k y) and Psi_J=Phi(1-k y).
Where their mean is nonzero define the same-mode observable

    g=(Phi_J-Psi_J)/(Phi_J+Psi_J)=k y,
    g_NN+g_N+(z^2+A)g=k z^2, N=ln a_E.             (3)

This is a time-dependent comoving Fourier coefficient, not a fixed-radius
static force law or automatically a survey's phenomenological parameter.
The explicit source amplitude cancels from (3) and the inverse. Holding an
independent free scalar wave fixed while changing source amplitude still
changes g. Its physical effect remains in the measured trace.

## Weighted reconstruction and a necessary reserved check

Choose real nonnegative C^2 weights w_i on finite intervals, with w_i and
their first derivatives zero at both endpoints. Define

    U_i=integral w_i g dN,
    V_i=integral w_i z^2 dN>0,
    L_i=integral (w_i,NN-w_i,N+z^2 w_i)g dN.

Twice integrating (3) by parts gives L_i+A U_i=k V_i. The boundary
concomitant is w g_N-w_N g+w g; it vanishes by the specified weights,
without an assumption about the scalar state at the interval boundaries.
For D=V_1 U_2-V_2 U_1 nonzero,

    k=(L_1 U_2-L_2 U_1)/D,
    A=(V_2 L_1-V_1 L_2)/D,
    nu=(A+2)(1-3k)/4-3(1+k).                        (4)

Admissibility requires 0<k<1/3 and A>(10+18k)/(1-3k), equivalent
to nu>0. A third disjoint interval supplies the no-refit residual
L_3+A U_3-k V_3. A zero residual is only necessary: a nonzero deviation
orthogonal to this single functional can escape it. It is not a uniqueness
test among actions, a full differential-equation test or a held-out empirical
validation when the trace itself was synthetically generated.

## Continuous-trace uniqueness and fixed-window limitations

For k>0, g/z^2 cannot be constant on any open interval. If g=c z^2,
(3) would require k=c(z^2+A+2). Its derivative gives 0=-2c z^2,
forcing c=0 and then k=0, a contradiction. If the same entire trace solved
two parameter pairs, subtraction would give
(A_1-A_2)g=(k_1-k_2)z^2. The contradiction forces both parameters equal.
Equation (1) then fixes nu within this supplied family.

There consequently exist two disjoint positive compact weights with different
U_i/V_i: choose separated values of the continuous function g/z^2 and
sufficiently small neighborhoods. This proves existence, not success of
any preselected pair or a lower conditioning bound. Unknown preparation
can make a fixed pair singular. High wave number, narrow windows, sampling
or rapid free waves can make the inverse practically unusable. Ideal
structural uniqueness does not establish feasible measurement precision.

## Certificate in measured quantities

For real traces put s_i=U_i/V_i and b_i=L_i/V_i, so b_i=k-A s_i.
Assume measured hats obey |s_hat_i-s_i|<=e_si and |b_hat_i-b_i|<=e_bi.
For example, a justified uniform |g_hat-g|<=epsilon_i gives
e_si=epsilon_i integral|w_i|/V_i and
e_bi=epsilon_i integral|w_i,NN-w_i,N+z^2 w_i|/V_i.
Sampling/quadrature errors must also be covered. Errors in z and time
calibration require additional bounds and are not silently included.

Set Delta_hat=s_hat_2-s_hat_1, E_s=e_s1+e_s2, E_b=e_b1+e_b2.
When |Delta_hat|>E_s, compute A_hat=(b_hat_1-b_hat_2)/Delta_hat,
k_hat=b_hat_1+A_hat s_hat_1 and nu_hat by (4). Then

    e_A=(E_b+|A_hat| E_s)/(|Delta_hat|-E_s),
    e_k=e_b1+|A_hat|e_s1+(|s_hat_1|+e_s1)e_A,
    e_nu=[|1-3k_hat|e_A+3|A_hat+6|e_k+3e_A e_k]/4.   (5)

These bound the absolute errors in A,k,nu respectively. With ds_i=s_hat_i-s_i
and db_i=b_hat_i-b_i, the first bound follows from the exact identity

    A-A_hat=[-(db_1-db_2)+A_hat(ds_2-ds_1)]
                       /[Delta_hat-(ds_2-ds_1)].

Expanding nu about the measured parameters gives
4 delta nu=(1-3k_hat)delta A-3(A_hat+6)delta k-3 delta A delta k,
which proves the last bound. The sufficient domain certificate is
k_hat-e_k>0, k_hat+e_k<1/3 and nu_hat-e_nu>0. Failure is inconclusive,
not a model rejection. The error envelopes are adopted measurement premises,
not precision achieved in this campaign.

## Verification and surviving assumptions

The runner differentiates the supplied vacuum action, checks the metric and
mode equations, weak adjoint, inverse/domain identities, and exact error
relations. Its synthetic protocol uses k=1/20,nu=1 and k=2/17,nu=3/5,
two freely different preparations each, DOP853 in z and Radau in N, and
weights 140x^3(1-x)^3 on N intervals [0,.4],[.5,.9],[1,1.4]. The first
two calibrate; the third is a reserved synthetic consistency interval.
Full profiles, actual failed attempts, equation-damage checks and independent
mathematical reviews are preserved in the companion work-history archive.
Numerical quadrature error estimates are not rigorous enclosures.
The duration of each synthetic window is0.4/H. Observational feasibility
of that time span and matched-mode access is not established. A set of
redshift bins does not automatically supply the same mode's time history.

Only the need to prescribe the coupled scalar's initial amplitude and phase
for this particular inverse is removed. The physical initial state is still
free. General rolling backgrounds, dust/radiation transfer and radiation
anisotropic stress require different equations. They cannot use (3) merely
because a source changes slowly. Published survey or orbital constraints
have not been substituted for the paired, calibrated mode trace assumed
here. Action selection, matter/environment selection, absolute scales,
bounded past history and a theory of everything remain open. No observed
data are fitted or independently tested in this note.
