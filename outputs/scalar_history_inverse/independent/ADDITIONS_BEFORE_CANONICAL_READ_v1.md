# Independent additions argument before canonical-source access

This supplement follows full exposure to the original note and runners. In
particular, their registered-density expression and conditioning fixture
are known. The argument below was checked algebraically by hand rather than
copied from a canonical helper. No canonical note, helper, primary runner or
output has yet been opened. The parent reports having incorporated the
independent exceptional-class result with attribution; that is correspondence
after the original proof freeze, not a second blinded derivation.

## Positive squared coupling and orientation

For known M>0, suppose B(t)=beta(t)^2>0 on a connected interval and alpha is
continuous. Since alpha^2=B/M^2, alpha is nowhere zero and its sign cannot
change on the interval. Thus alpha=epsilon sqrt(B)/M with one constant
epsilon in {+1,-1}. Differentiation gives
alpha_dot=epsilon B_dot/(2 M sqrt(B)). A zero of B or a disconnected chart
would require separate sign analysis.

The canonical field reflection phi -> -phi plus a constant sends
(v,alpha,alpha_dot) to (-v,-alpha,-alpha_dot), while leaving mu,H,r and V(t)
unchanged and reflecting the field-space functions A and V. Direct inspection
of each polynomial term gives

    P(-v,-alpha,-alpha_dot)=P(v,alpha,alpha_dot),
    G(t,-v;-alpha)=-G(t,v;alpha).

Both oriented choices therefore describe the same histories modulo canonical
field reflection when no independent orientation convention is supplied.
The six-candidate upper bound holds after one sign convention is chosen;
counting both signs before quotienting merely duplicates reflected labels.
This claim must not extend across unspecified zeros or field-space boundary
conditions that select an orientation.

## A registered Einstein dust history

For positive r(t) of class C2, define

    K=-2 M^2 H_dot-r>0, q=r_dot/r+3H.

Choose one constant sign sigma and set v=sigma sqrt(K). Dust conservation
then requires alpha=q/v. The differentiated scalar equation gives

    mu = -K_ddot/(2K)+K_dot^2/(4K^2)-3H K_dot/(2K)
         -3 H_dot+3H r q/K.                         (A)

No derivative of the sign appears because v never crosses zero. Changing
sigma flips alpha, leaves mu invariant, and reflects the canonical field.
If alpha and mu are also prescribed inputs, these are compatibility checks,
not replacements that make arbitrary inputs consistent. For example,
q^2=alpha^2 K is necessary, and the global sign relation still matters.
Known bare density rho_* alone does not supply r; r is A rho. A single
registered r(t0) determines only the initial speed magnitude, whereas (A)
needs a registered differentiable density history. Divisions by r and K
exclude dust-free and stationary-scalar endpoints.

As an additional post-exposure check of the author's variable-coupling
fixture, H=1/t, r=1/(4t), v=sqrt(8-t)/(2t) on 1<t<4 gives

    alpha=4/sqrt(8-t),
    mu=(1024-48t-9t^2)/(4 t^2 (8-t)^2).

These follow by applying (1/v)d/dt twice to the stated A=t^2/4 and
V=2/t^2-1/(8t), with rho=t^-3 held fixed in the second field derivative.
They will be compared to (A) without importing an author helper.

## Frame and units

If g_J=A^2 g_E, a comoving volume obeys Vol_J=A^3 Vol_E and the conserved
particle counts agree. Constant Jordan particle mass gives
rho=A^3 rho_J and r=A rho=A^4 rho_J. Proper times and scale factors obey
dt_J=A dt_E and a_J=A a_E, hence H_J=(H+alpha v)/A. Those kinematic relations
do not register measured Jordan inputs to Einstein time by themselves.

The dimension of q is inverse time; q/v has inverse field dimension;
all terms of (A) have inverse time squared. Power/log fixtures use numerical
coordinates with a fixed reference time and canonical mass normalization.
They must not be read as dimensionful powers with a derived reference scale.

## Near-degenerate root conditioning

In numerical units M=t_*=1 at t=1, let p=(2+e)/3, v=1,
alpha=e>0 and use the exact forward power-family mass. Its value is

    mu=2+(8e+5e^2+2e^3)/3.

Hand differentiation of the compatibility polynomial at its true root gives

    P_v(1)=e(4e^3+16e^2+139e+174)/9.

This is positive for e>0 and tends to zero linearly. Since P_mu=4v^4,
the implicit sensitivity of the instantaneous root, with the other local
input jets fixed, is

    dv/dmu=-36/[e(4e^3+16e^2+139e+174)]
           ~ -6/(29e).

Away from t=1, the corresponding statement can be made with c=t v and
dimensionless mu_hat=t^2 mu; their derivative is the same numerical ratio.
This is conditioning of an instantaneous algebraic candidate. A freely
perturbed local mu need not extend to any compatible full history, so the
calculation does not itself prove a statistical or functional stability
theorem for physically realizable histories.

The next controls will test these identities and the original checker
recovery using exact symbolic expressions. A later direct comparison to
canonical helper functions will be explicitly marked as correspondence
testing after exposure; it will not replace the independent proof.
