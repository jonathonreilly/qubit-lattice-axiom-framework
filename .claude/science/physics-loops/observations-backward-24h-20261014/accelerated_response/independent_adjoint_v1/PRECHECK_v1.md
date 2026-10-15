# Independent finite-observation adjoint precheck

Reviewer `/root/force_energy_bridge_check`. No accelerated-response author draft
or code has been opened. No raw observations are read. Root remains author.

## Supplied dynamical and observation model

On [a,b], let z'=L(s)z+P(s)f(s), with known coefficients and continuous state
z. For readout i, let

 y_i = integral_a^b q_i(s)^T z(s)ds
       +sum_r d_ir^T z(t_r)+(X beta)_i+e_i.

Readout atoms include a and b when present. These coefficients encode whatever
clock, count and retarded map is supplied; the archive alone does not determine
them. Let Phi(s,t) be the state transition matrix. Variation of constants gives

 N_i = integral_a^b Phi(s,a)^T q_i(s)ds
       +sum_r Phi(t_r,a)^T d_ir,

 lambda_i(t)=integral_t^b Phi(s,t)^T q_i(s)ds
       +sum_{t_r>t} Phi(t_r,t)^T d_ir,
 w_i(t)=P(t)^T lambda_i(t),

 y_i-X_i beta-e_i=N_i^T z(a)+integral_a^b w_i(t)^T f(t)dt.

The value at an isolated atom does not affect the force integral. Use terminal
lambda_i(b^+)=0, backward jumps lambda_i(t_r^-)=lambda_i(t_r^+)+d_ir,
and -lambda_i'=L^T lambda_i+q_i between atoms. At the left endpoint
N_i=lambda_i(a^+)+d_ia. This explicitly retains the initial endpoint atom.
The terminal atom is imposed as lambda_i(b^-)=d_ib, not discarded by a zero
terminal condition.

A real contrast c removes arbitrary initial state and nuisance exactly when
N^T c=0 and X^T c=0. It then has force weight w_c=sum c_i w_i. If only a
subspace of initial state is unknown, replace N by its response to that
subspace and subtract the known initial contribution. Cancellation is not
inferred from row sums when the state dynamics are nontrivial.

## Energy-trace regularity is a distinct condition

For a free scalar gradient sampled at one fixed spatial point, begin with
smooth fields and extend only when the zero-extended w_c is in H1(R) intersect
L1. For piecewise H1 weights this requires zero traces at a,b and no internal
jumps. The ordinary derivative must also be L2. Under bounded L, P in W1,infty,
and q_i in L2 between finitely many atoms,

 w_c' = P'^T lambda_c-P^T L^T lambda_c-P^T q_c

on each open smooth segment. For continuous P,

 w_c(t_r^-)-w_c(t_r^+)=P(t_r)^T d_cr,
 w_c(b^-)=P(b)^T d_cb,
 w_c(a^+)=P(a)^T lambda_c(a^+)=-P(a)^T d_ca

in an initial-state-free contrast. Initial-state cancellation alone does not
make these force traces vanish when velocity endpoint atoms are present.
For discontinuous P, the actual jump is
P_-^T(lambda_+ +d_cr)-P_+^T lambda_+, and must be checked directly.

When these conditions hold, the massless fixed-point gradient Gram is
(6pi)^-1 integral w_c'.w_d'; nonnegative masses have the corresponding
spectral enclosure. A moving spatial trace or the complete conformal force
requires its actual operator and cannot inherit this exact stationary Gram.
Omitting delta contributions from a jump in w and integrating only its smooth
interior derivative would falsely assign a finite or even zero trace norm.
For the specified flat massless energy space, such jumps are real obstructions
to this bounded-functional extension, not exclusions of the scalar theory.

## Recognizable trajectory and endpoint distinction

For a supplied Newtonian reference trajectory, z=(delta x,delta v),

 L=[[0,I],[K,D]], P=[[0],[B]],
 K=partial_x a_reference, D=partial_v a_reference.

Then -lambda_x'=K^T lambda_v+q_x,
-lambda_v'=lambda_x+D^T lambda_v+q_v, and w=B^T lambda_v.
For a conservative Newtonian point source in c=1 units,
a_reference=-M_g x/r^3 and K=M_g(3 rhat rhat^T-I)/r^3, D=0.
The reference orbit, force scale and the validity of linearization are inputs.

A pure position readout atom has d=(d_x,0), hence P^T d=0: it jumps
lambda_x but not w. A velocity atom has d=(0,d_v), and generally creates a
force-weight jump B^T d_v. These distinctions also apply at the outer endpoints.
For a free particle, v(b)-v(a) cancels its initial velocity but produces the
rectangular force weight 1_[a,b], which is not H1. Its finite-cutoff massless
squared dual norm is [Lambda-sin(Lambda*(b-a))/(b-a)]/(3pi^2).
In contrast x(0)-2x(T)+x(2T) cancels initial position and velocity and gives
a continuous triangular weight, slopes +/-1, whose squared norm is T/(3pi).
A position endpoint combined with an explicit velocity initial endpoint may
still violate the left force-trace condition; the atom type matters at both ends.

## Planned independent executable check

Use a synthetic circular Newtonian reference to obtain genuinely time-varying
4D planar tidal dynamics. Compare a directly integrated variational state with
central finite differences of nonlinear forced trajectories. For distributed
count-like velocity readouts and explicit position/velocity atoms, solve the
adjoints backward with all jumps, compare propagated initial coefficients and
direct-versus-adjoint force integrals, and check nuisance-free contrasts.
Demonstrate allowed position jumps, disallowed uncancelled velocity jumps, and
the free-particle rectangular/triangular distinction. Freeze all controls and
report before opening author sources. No physical calibration is inferred.
