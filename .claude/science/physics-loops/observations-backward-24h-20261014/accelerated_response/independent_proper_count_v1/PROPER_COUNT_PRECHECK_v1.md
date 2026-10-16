# Independent fixed-proper-endpoint radio-count precheck

Reviewer `/root/localized_history_check`; root remains the scientific author.
This derivation and its separate numerical protocol are frozen before opening
any new author file in accelerated_response. Only the assignment's supplied
reference model is used. This is not an empirical model identification or an
audit verdict. Coordinates below use c=1; one may use s=ct and express proper
clock readings in length units consistently. A constant proper frequency nu_e
then has cycles per chosen proper-time unit.

## Supplied model and regularity

The Einstein coordinate metric is eta, and the physical metric is A^2 eta with
A>0. Let ell=log A. The two externally specified paths x_E(u), x_R(t) are
subluminal, at least C2 when frequency variations are used, and share a smooth
positive clock factor. The emitter emits constant proper frequency nu_e. There
is no dispersive medium, transponder, receiver oscillator correction, electronics,
unknown phase propagation term or independent clock-frequency variation in this
reference problem. Those would be further measurement assumptions.

A perturbation family has ell_epsilon(t,x)=ell_0(t,x)+epsilon a(t,x)+O(epsilon^2),
a=alpha h, and x_A,epsilon(t)=x_A(t)+epsilon xi_A(t)+O(epsilon^2), A=E,R.
Here xi_A is defined at fixed coordinate time, and eta_A=xi_A' is its velocity
variation. External paths alone do not determine xi_A from h. A constant ell_0
is an important special case, but the clock formulas below also display the
background-position term for nonconstant ell_0. No trajectory law is silently
added to the supplied paths.

For the relevant retarded events assume a unique null root with nonzero spatial
separation L, both endpoint events within the specified histories, and a uniform
subluminal bound. Put v_A=x_A', gamma_A=(1-|v_A|^2)^(-1/2). The proper-clock rate is

    f_A(t)=tau_A'(t)=A_0(t,x_A(t))/gamma_A(t)>0.

Clock readings include their initial synchronization constants. Pick a common
fixed coordinate anchor t_* only as notation; histories may instead have
separate anchors if their offset variations are transformed consistently.

## Exact emission map and count before linearization

The conformal factor cancels from the null eikonal equation and from unparameterized
null rays. Under the stated propagation model the ray joins the same Minkowski
null endpoints. No additional line integral of a along the ray is supplied.
At receiver coordinate time t, the emission time u(t) therefore solves

    F(t,u)=t-u-|x_R(t)-x_E(u)|=0.

Define n=(x_R(t)-x_E(u))/L, D_R=1-n.v_R(t), D_E=1-n.v_E(u).
Both D_R,D_E are positive. Differentiating the null equation gives

    du/dt=D_R/D_E.

The received phase is the emitted phase at the retarded event,
Phi_R(t)=Phi_0+2pi nu_e tau_E(u(t)). For fixed receiver proper-clock labels
T_a<T_b, let t_i solve tau_R(t_i)=T_i and u_i=u(t_i). The finite cycle count is

    N=nu_e [tau_E(u_b)-tau_E(u_a)].

No average of a coordinate-time frequency may replace this endpoint expression
without its proper-clock Jacobian. Its instantaneous receiver proper frequency is

    nu_R/nu_e=K(t)=f_E(u) D_R/[f_R(t) D_E].

Consequently N=integral_(T_a)^(T_b) nu_R(T) dT. A finite proper-time average
frequency is N/(T_b-T_a), with fixed denominator in this assignment.

## All first variations at fixed receiver proper endpoints

Define chi_A(t)=delta tau_A(t) at fixed coordinate time, and allow
chi_A(t_*)=kappa_A. The direct rate variation is

    delta f_A(t)=f_A(t) [a(t,x_A(t))
                      + grad ell_0(t,x_A(t)).xi_A(t)
                      - gamma_A(t)^2 v_A(t).eta_A(t)],
    chi_A(t)=kappa_A+integral_(t_*)^t delta f_A(s) ds.

For constant A_0, the background-gradient term vanishes. These expressions keep
proper-clock variations caused by both the metric and velocity perturbation.
Replacing chi_A by just an integral of a drops the kinetic clock response.

At each fixed receiver proper endpoint T_i,

    delta t_i=-chi_R(t_i)/f_R(t_i).

Varying the null equation at that shifted event, including the emitter's own
retarded displacement, gives

    D_R delta t_i-D_E delta u_i-n.(xi_R(t_i)-xi_E(u_i))=0,
    delta u_i=[D_R delta t_i-n.(xi_R(t_i)-xi_E(u_i))]/D_E.

The total endpoint position variations are

    delta X_R=xi_R(t_i)+v_R(t_i) delta t_i,
    delta X_E=xi_E(u_i)+v_E(u_i) delta u_i.

The total emitter clock change at emission is chi_E(u_i)+f_E(u_i) delta u_i.
The total receiver clock change is chi_R(t_i)+f_R(t_i) delta t_i=0, as required.
Thus the complete finite-count response is

    delta N=nu_e [S_b-S_a],
    S_i=chi_E(u_i)-K_i chi_R(t_i)
        -[f_E(u_i)/D_E,i] n_i.(xi_R(t_i)-xi_E(u_i)).

This is a kinematic identity for the supplied perturbation family. It includes
retarded emission-time changes, receiver coordinate-endpoint changes, both path
displacements, and both proper clocks. It does not equate an observed residual
to scalar acceleration. Neither a held-fixed coordinate receiving interval nor
omission of the receiver clock term is equivalent to the stated task.

## A distinct differential-frequency representation

For checking the finite endpoint formula, define total event velocity variations

    delta V_R=eta_R(t)+x_R''(t) delta t,
    delta V_E=eta_E(u)+x_E''(u) delta u.

Then

    delta n=(I-n n^T)(delta X_R-delta X_E)/L,
    delta D_A=-delta n.v_A-n.delta V_A,
    delta f_A,event=delta f_A,coordinate+f_A' delta(event time),
    delta K/K=delta f_E,event/f_E-delta f_R,event/f_R
               +delta D_R/D_R-delta D_E/D_E.

All quantities are evaluated at their own retarded events. At fixed receiver
proper labels, delta N=nu_e integral_(T_a)^(T_b) delta K(T) dT. This supplies an
independent local-frequency representation of the endpoint formula. Transverse
position changes enter delta n here even though the null-time first variation
contains only n.(xi_R-xi_E). Accelerations multiply the endpoint time shifts and
must remain when paths accelerate.

## Augmented trajectory and clock sensitivities

Externally supplied paths do not specify a scalar-induced trajectory response.
If a separate model supplies z_A' = F_A(t,z_A,epsilon), then its tangent variables
must obey eta_z,A'=F_A,z eta_z,A+partial_epsilon F_A at the reference trajectory,
with all initial trajectory variations retained. Append tau_A'=f_A and the chi_A'
equation above to that same system. The resulting trajectory/clock sensitivities
are inserted into S_i; the clock is not recovered afterward from position alone.
Fixed proper endpoints are implicit events and still require delta t_i above.

A useful explicitly conditional example is a massive test body minimally coupled
to A^2 eta. Its coordinate geodesic equation is

    x''=-(1-|v|^2) [grad ell+v partial_t ell].

This follows from varying -m integral A sqrt(1-|v|^2) dt, not from a null phase
shift. The time derivative in the second term is partial_t at fixed x, not the
convective derivative along the path. If an additional coordinate acceleration
F_ext(t,x,v,epsilon) is specified, and the reference ell_0 is constant, a supplied
additive-force model has the tangent system

    xi'=eta,
    eta'=F_ext,x xi+F_ext,v eta+delta F_ext
          -(1-|v|^2) [grad a+v partial_t a],
    chi'=f [a-gamma^2 v.eta].

This is conditional on that external-force prescription. A force specified in
proper units can have a nonzero delta F_ext; setting it to zero is an additional
choice, not implied by knowing the reference path. In a nonconstant background,
linearizing the full force also brings background spatial/time Hessians and
velocity derivatives; the generic tangent equation covers them. No geodesic or
force law is imposed on the externally given paths by the response identity.

## Initial-state and constant-background caveats

An additive emitter proper-clock offset kappa_E cancels from a finite count when
nu_e is constant. An emitter phase offset also cancels. Receiver synchronization
does not generally cancel: with no other perturbation it gives

    delta N=-nu_e kappa_R (K_b-K_a).

It changes the coordinate epochs selected by fixed receiver clock labels. This
term vanishes for constant K, but not for general accelerated or changing-line-of-
sight paths. Initial position/velocity perturbations likewise remain through
xi, eta and chi. A scalar field history cannot uniquely determine them without
a supplied initial-state rule or a nuisance/measurement treatment. Clock history
before the modeled interval may enter through kappa_A.

For stationary emitters/receivers at fixed coordinate positions, a spatially and
temporally constant a and unperturbed paths give delta N=0: both proper clocks
scale equally and the remaining phase shift is constant. In contrast, a(t)=b t
with stationary paths separated by L gives the exact ratio
nu_R/nu_e=exp(-epsilon b L), hence

    delta N=-nu_e b L (T_b-T_a).

A conformal clock response can therefore be nonzero even with zero path response.
A time-independent spatial gradient gives a corresponding endpoint clock ratio
for externally held stationary paths. It is not a photon line-integral term.

Do not generalize constant-background cancellation to arbitrary externally fixed
coordinate paths. For a stationary emitter and a receiver with
x_R(t)=L+(a_c/2)t^2 in one spatial dimension, the constant conformal perturbation
changes which points of this changing Doppler curve lie at fixed proper labels.
With anchor zero, A_0 constant, J(t)=integral_0^t sqrt(1-a_c^2 s^2) ds and
u(t)=t-L-(a_c/2)t^2, the variation is

    delta N=nu_e b [A_0 (nu(t_b)-nu(t_a))
                 -(K_b T_b-K_a T_a)],
    K(t)=(1-a_c t)/sqrt(1-a_c^2 t^2),  T_i=A_0 J(t_i).

It is generally nonzero. This does not establish physical observability of a
universal constant scale: a coordinate/unit rescaling must transform the supplied
paths, anchors, lengths, frequencies and external forces consistently. Holding
coordinate trajectories fixed while varying A is a different family. The
constant-background claim therefore needs a declared operational convention.

## Scope

The derivation presupposes the conformal metric, geometric propagation law,
constant proper emitter frequency, known paths/clock definitions and supplied
perturbations or trajectory dynamics. It supplies no actual radio-instrument
calibration, scalar equation of motion, energy normalization or observed residual.
No new author file, raw observation, state/lock, index or branch was read or
modified in creating this precheck.
