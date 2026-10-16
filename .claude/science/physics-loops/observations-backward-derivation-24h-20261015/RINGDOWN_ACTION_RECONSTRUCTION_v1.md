# Reconstructing the conditional action from the second harmonic

Direct derivation by /root, 2026-10-16; exploratory, pending focused checking.
This extends COMMON_ACTION_RINGDOWN_v1.md. Its full declared classical class,
force convention, smoothness, rest-linearization and nondegeneracy premises
remain. All numerical examples are synthetic. No new physical axiom is adopted.

## What is removed, and what is not

The first relation only eliminates hidden parameters in a necessary test. The
complex second harmonic supplies an additional observable: it can reconstruct
the hidden inertia *as a function of environment*, up to one constant unit.
Together with a complete calibrated dynamic stiffness and static holding force,
it reconstructs a representative of the candidate action and Rayleigh function.
This is a conditional inverse within an explicitly restricted class; it does
not derive that class, identify a gravity scalar or recover quantum statistics.
The force/frequency connection is known prior art, as documented in the parent
note. Novelty is not certified. Exact continuous functions below are ideal
identifiability inputs, not quantities supplied by finitely many noisy records.

Use the parent notation O=C/tau, lambda=-Gamma/2+i omega,
rho=Res_lambda Z_x, and clamped-force coefficients R0,f,h,g. Assume a connected
interval with Gamma>0, omega>0, f!=0 and rho!=0. Define the observable functions

    K=|(2lambda+Gamma)rho|,
    Q=K h/|f|²,
    S=-2(2lambda+Gamma)rho g/f²,
    L=O-lambda²,
    r=(S-Q)/L.                                                  (1)

Here L=2omega²+i Gamma omega is nonzero. The parent equations directly yield

    Q=O',
    S=O'+(tau'/tau)(O-lambda²),
    r=tau'/tau, real.                                           (2)

The complex phase of the residue and second harmonic matters; moduli alone
cannot replace S. The chosen initial coefficient c cancels as c², including
its phase. A real-only second-harmonic power spectrum loses this information.
The imaginary part of r is a new consistency residual. Q=O' alone does not
test it. Both relations require the same signed calibrated force convention.

## Removing the kinetic cross term by a proved coordinate freedom

One must not assume k=0 as a physical selector. It is instead a coordinate
freedom within this declared class. Write w=v+F(x) with F'=-k/tau. Substitution
in T,V,D gives

    k_new=0,       tau_new=tau,          C_new=C,
    M_new=M-k²/tau,
    nu_new=nu-gamma k/tau,
    d_new=d-2nu k/tau+gamma k²/tau²,
    B_new=B+C F,   U_new=U+B F+C F²/2,
    w0_new=w0-F,   G_new=G-C k/tau.                             (3)

The kinetic and damping matrices transform by the same invertible coordinate
congruence, preserving positivity. No dissipative cross term has been silently
deleted. The force conjugate to x on solutions with no hidden external drive
is unchanged: the added F' times the hidden equation is zero. With a hidden
external force it would not be the same single-port experiment.

The off-diagonal operator becomes N_new(s)=N(s)-k(s²+Gamma s+O).
Consequently N_new(lambda)=N(lambda), so the measured residue and all clamped
coefficients are unchanged. This reduction stays inside the functions-of-x
quadratic class. An x-dependent *rescaling* of w would generally introduce
w-dependent kinetic coefficients and is not invoked.

## Explicit inverse in the k=0 coordinate chart

1. Check Q=O' and that r in (1) is real. Set

       tau(x)=tau_* exp(integral_(x_*)^x r(u) du), tau_*>0,
       C=tau O,       gamma=tau Gamma.                          (4)

   tau_* is an undetermined hidden-coordinate normalization. If an independent
   physical unit for w were already specified, that constant would require
   physical calibration; it is not inferred here.

2. Choose one continuous square root on the interval

       n(x)²=-tau(x)(2lambda+Gamma)rho(x).

   The argument is nonzero; on an interval such a smooth branch exists. Its
   overall sign corresponds to hidden reflection, not a selected dynamical law.
   Branch continuity is required; choosing unrelated signs at each point does
   not reconstruct a smooth action. Define the real functions

       nu=Im(n)/omega,
       G=Re(n)-nu Re(lambda),       N(s)=G+nu s.                 (5)

   Then N(lambda)=n. No k, B, gamma or coupling profile has been supplied to
   this reconstruction.

3. Define

       P(s)=Z_x(s)+N(s)²/[tau(s²+Gamma s+O)].                   (6)

   Check that P is a real polynomial of degree at most two and write
   P=M s²+d s+P0. This excludes extra hidden poles, delay and analytic frequency
   dependence not present in the declared local two-coordinate action. Check
   M>0 and d gamma-nu²>=0. These are additional compatibility conditions, not
   consequences of (1) alone. Also require

       P0=R0'+G²/C, equivalently Z_x(0)=R0'.                    (7)

   R0' is the derivative of the measured equilibrium holding force along the
   equilibrium curve. It is not a derivative at fixed hidden w. This distinction
   fixes the sign and the extra G²/C term.

4. Integrate

       w0'=-G/C,
       B=-C w0,
       E'=R0,
       U=E+C w0²/2.                                            (8)

   The integration constants in w0 and E are a hidden translation and an
   additive potential constant. In centered form the reconstructed potential is

       V(x,w)=E(x)+C(x)[w-w0(x)]²/2.                            (9)

This completes a representative action and symmetric Rayleigh function. The
visible mass M and damping d come from the polynomial response, not from an
assumed load model. Their signs must pass the stated conditions. Exact
identification of the complete calibrated dynamic stiffness is stronger than
merely knowing its one pole and residue.

## Sufficiency for these ideal observation functions

Assume the smooth functions satisfy (1)-(8), realness, nondegeneracy and the
positivity checks, and that each supplied force history has the parent's full
six-exponential closure. The constructed action has clamped poles lambda and
lambda*, equilibrium w0, rest holding force E'=R0, and linearized visible
curvature V_xx=R0'+C w0'²=R0'+G²/C. Its linear response is exactly the supplied
Z_x by (6)-(7). For each ringdown choose c=f/n; this is an inferred initial
coefficient for that record, not a universal initial-state distribution.
Equations (1)-(2) then reproduce its h and g exactly:

    h_pred=tau O' |f/n|²=h,
    g_pred=tau[O'+r(O-lambda²)](f/n)²/2=g.                     (10)

Thus the representative realizes all these ideal observed functions. The
necessary and sufficient statement concerns this selected response/ringdown
surface within the declared class, not arbitrary moving histories or all
possible forces. Independent moving histories can test it further.

After k is removed by (3), any compatible representative has the same r and
hence tau differs only by a positive multiplicative constant. Equation (5)
then fixes G and nu up to the corresponding hidden scale and one reflection;
(6) fixes M,d; (8) fixes w0 and E up to their constants. This characterizes the
remaining freedoms within the regular connected chart. No uniqueness outside
the candidate class, across a zero/pole cancellation, or on disconnected
intervals follows. Finite samples still leave functions between samples free.

## Calibration covariance and error propagation

For a smooth one-to-one visible coordinate y=j(x), j'!=0, the conjugate force
is R_y=R_x/j'. At rest,

    Z_y=Z_x/(j')²-R0 j''/(j')³,
    rho_y=rho_x/(j')²,
    f_y=f_x/j', h_y=h_x/j', g_y=g_x/j'.                        (11)

The extra equilibrium term is analytic and cannot affect the residue. Thus
Q_y=Q_x/j', S_y=S_x/j', r_y=r_x/j'. Integrals reconstruct the same tau and
potential in changed coordinates. A sensor relabeling with an unchanged force
channel is not this transformation. Independent work-conjugacy calibration
remains required.

For finite errors, retain the parent's true-value bounds and denominator bound
Dmin=Fmin², e_D=2Fmax e_f+e_f²<Dmin. Put a=2lambda+Gamma and bound true
|a|<=Amax, |rho|<=Pmax, |g|<=G2max. With e_a=2e_lambda+e_Gamma,

    e_numS=2[(Amax+e_a)(Pmax+e_rho)(G2max+e_g)-Amax Pmax G2max],
    e_S<=e_numS/(Dmin-e_D)
          +2 Amax Pmax G2max e_D/[Dmin(Dmin-e_D)].               (12)

The denominator here is complex f²; its modulus lower bound is still Fmin²
and its perturbation is at most e_D. Let true |L|>=Lmin and
e_L=e_O+2Lmax e_lambda+e_lambda²<Lmin, where Lmax bounds |lambda| as in the
parent. With true |S-Q|<=Wmax,

    e_r<=(e_S+e_Q)/(Lmin-e_L)
            +Wmax e_L/[Lmin(Lmin-e_L)].                        (13)

Consequently a compatible true model requires |Im(rhat)|<=e_r. Integrating
Re(rhat) gives relative inertia error in logarithmic form bounded by
|delta log tau_*|+integral e_r dx, with additional coordinate/interpolation
errors where appropriate. Complex square-root reconstruction also needs a
certified continuous branch; the exact identity
delta n=delta(n²)/(nhat+n) exposes its branch and conditioning margin.

These formulas propagate supplied certificates; they do not establish them
from the noiseless extractor. Finite-band extrapolation, phase calibration,
source correction, mode isolation, equilibrium preparation and physical
readout identity remain unresolved empirical obligations. No trajectory data
in this block constitutes an independent empirical test.

## Planned controls and failure modes

Check the cross-coordinate transformation directly in the action and verify
the full inverse on a nonconstant tau,C,B,k,nu family through independently
extracted force/frequency records. Changing the second-harmonic phase while
keeping the first identity fixed must violate the real-r condition. Changing
the equilibrium force slope independently must fail (7). Unphysical kinetic
or damping polynomials must fail positivity. Preserve the distinction between
a necessary identity, realization of an exact observation surface, and physical
validation. Parameter reconstruction is not an axiom derivation.
