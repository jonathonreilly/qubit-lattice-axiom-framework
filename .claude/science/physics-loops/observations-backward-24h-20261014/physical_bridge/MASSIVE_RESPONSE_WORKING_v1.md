# Finite-observation mass correction without a field-state selector

Date: 2026-10-15. Status: open working derivation, not yet independently checked.
Author: /root in the user chat. Base: c6b3c14760d0d2efb5f7eacf3b9ff7ae25cbf0ee.
Trace: upstream_support; consumer is the count-derived field-energy inverse.

## Target and allowed premises

Start with the finite observation derived in M6, rather than choose a new
field readout. Its field component is

    O[h]=sum_A integral [c_A(s) h(s,x_A(s))
       -(1-|u_A|^2) W_A(s).(grad h+u_A partial_s h)] ds.

The physical response model remains supplied: flat Einstein patch, constant
conformal background, specified smooth timelike reference trajectories,
linear conformal forcing and proper-clock response, and calibrated ideal
link/count dynamics. The M6 adjoint derives c,W from those observations.
No field state, energy upper budget, mass, action or potential is selected here.
No new observed values are opened. Day169 remains exposed development data.

Replace only the homogeneous field equation by

    h_ss-Delta h+mu^2 h=0,    mu>=0,
    ||h||_mu^2=integral [p0^2+|grad h0|^2+mu^2 h0^2]=2 E_mu.

For mu=0 use the anchored homogeneous-H1 representative, or the already
derived exact constant-offset cancellation. A spatially constant massive
oscillation on all R3 has infinite energy and is not a missing finite-energy
datum. Curvature, nonconstant background, matter sources and nonlinear terms
are separate obligations. In the supplied revised action, mu^2/H^2=B>12;
that relation is derived from the specified action, not a numerical mass or
curvature supplier and not a permission to drop either correction.

## Common energy space and exact massive response

Use

    h=(2pi)^(-3/2) integral [a(k) exp(i omega s-i k.x)+conjugate] d^3k,
    omega=sqrt(k^2+mu^2),    p(k)=2 omega a(k).

Here p is a complex function with the real Hilbert pairing Re integral p* q;
no additional p(-k)=p(k)* restriction is imposed. Reality is supplied by the
explicit conjugate branch. The energy norm is integral |p|^2. The identification
of p for different masses is an isometry of their energy data spaces, not an
assertion that their physical initial fields or velocities are identical.

Put n=k/k, v=k/omega, q_v=(1-|u|^2)(v n-u). Then

    F_mu(k,n)=sum_A integral [c_A/omega+i q_v,A.W_A]
                          exp(i omega s-i k n.x_A(s)) ds,
    O_mu[p]=(2pi)^(-3/2) Re integral p(k) F_mu(k,n) d^3k,
    G_mu,ij=(2pi)^(-3) integral_0^infinity integral_S2
                    k^2 Re[F_mu,i conjugate(F_mu,j)] dOmega dk.

This retains the partial-time force, common-field cross terms, clocks and
spatial phases. It is not an instantaneous inertial replacement. Complex
conjugation of the Riesz kernel changes no real Gram or difference norm.

## Explicit high-frequency control

All weights are zero-extended. Assume c is BV and compact, W is continuous
and compact with W'=w in BV, and the path is C3 on a neighborhood of the
weight support. A finite partition with these one-sided regularities also
works when the stated variations include its jumps. Require uniform speed
|u|<=beta<1. These are stronger regularity hypotheses than M6, not a silent
extension of its entire L2/H1 domain. Finite endpoint counts with sufficiently
smooth reference dynamics satisfy this class; their jumps must be included.

For fixed v,n define

    d_v=1-v n.u, b_v=q_v/d_v,
    j_v=c-partial_s(b_v.W),   g_v=j_v/d_v.

One integration by parts of the force, using W's zero outer traces, gives
F_mu=omega^(-1) integral j_v exp(i omega s-i k n.x) ds. A second BV integration
by parts, including every jump of the zero extension, gives

    |F_mu,A(k,n)| <= TV(g_v,A)/omega^2.

No high-frequency endpoint term is dropped. Let V_A bound TV(g_v,A) uniformly
for 0<=v<=1 and n in S2, and let V=sum_A V_A. Then |F_mu|<=V/omega^2.
This proves boundedness jointly with the low-frequency estimate below.

A conservative computable supplier for V_A is as follows. Put delta=1-beta,
a=||u'||_infinity, j=||u''||_infinity, Q0=1+beta,
Q1=1+2 beta(1+beta), and

    B0=Q0/delta,
    B1=Q1 a/delta+Q0 a/delta^2,
    B2=[(2+6beta)a^2+Q1 j]/delta
          +[2 Q1 a^2+Q0 j]/delta^2+2 Q0 a^2/delta^3.

These bound |b_v|, |b_v'| and |b_v''| by the quotient rule. With
C=||c||_1, W=||W||_1, W1=||W'||_1, Tc=TV(c), T1=TV(W'),

    V_A <= [Tc+B2 W+2 B1 W1+B0 T1]/delta
              +a [C+B1 W+B0 W1]/delta^2.

Norms and vector total variations are the Euclidean ones. Compact support and
zero extension are part of each variation. A tighter directly computed V is
allowed if its uniform bound is proved. Supremum sampling alone is not proof.

## Low-frequency comparison and an explicit mass-error enclosure

Choose a common time origin such that |s|<=T on every response support.
Define C=sum_A ||c_A||_1, W=sum_A ||W_A||_1 and beta=max_A beta_A.
Write Delta=omega-k and theta=min(2,T Delta). Directly comparing the two
original integrands, whose spatial phases are identical at fixed k,n, gives

    |F_mu-F_0| <= D_mu(k),
    D_mu(k)=C[(1-v)/k+theta/omega]
                    +W[(1-v)+(1+beta)theta].

The k=0 value is understood by its integrable radial limit. This uses
|q_v-q_1|<=(1-v), |q_v|<=1+beta and
|exp(i omega s)-exp(i k s)|<=theta. No spatial-position or initial-state bound
is required; known paths enter through the response and the high-frequency V.

For any K>0,

    ||B_mu-B_0||^2 <= epsilon_mu(K)^2,
    epsilon_mu(K)^2 = [integral_0^K k^2 D_mu(k)^2 dk+4 V^2/K]/(2pi^2).

Here B is one real scalar observation operator on the common energy space.
The tail follows from |F_mu-F_0|<=2V/k^2, not from an unproved Loewner order.
The estimate is conservative. For fixed K the low integral tends to zero
as mu tends to zero by dominated convergence; then K can be made arbitrarily
large. Thus B_mu tends to B_0 in operator norm on this regularity class.
At exactly mu=0 the difference is exactly zero; do not retain the artificial
tail of a finite-K comparison.

A closed elementary upper bound on the low integral avoids trusting numerical
quadrature. For K>=mu>0 put

    Z=C T+W[1+(1+beta)mu T],
    A=C/2, D=(C T+W)/2, J=W(1+beta)T/2.

The contributions k in [0,mu] and [mu,K] are bounded respectively by

    L0=C^2 mu+C Z mu^2+Z^2 mu^3/3,
    L1=mu^4 { A^2/3 (mu^(-3)-K^(-3))
             +A D (mu^(-2)-K^(-2))
             +(D^2+2 A J)(mu^(-1)-K^(-1))
             +2 D J log(K/mu)+J^2(K-mu) }.

Each term is nonnegative. For k>=mu use Delta<=mu^2/(2k),
1-v<=mu^2/(2k^2) and 1/omega<=1/k; for k<=mu use Delta<=mu.
Replacing the low integral by L0+L1 gives an explicit analytic enclosure.
Choosing K is only optimizing a proven error bound, not fitting a theory.

## Consequence for inference without choosing a state

For a real contrast t, form its actual combined c,W first and apply the bound
to that scalar response. Let g0=t^T G0 t. Then

    max(0,sqrt(g0)-epsilon_t) <= sqrt(t^T G_mu t)
                                    <= sqrt(g0)+epsilon_t.

If a measured residual r and a justified projected error allowance e_t are
available, every compatible massive state obeys

    E_mu >= max(0,|t^T r|-e_t)^2 /
                   [2 (sqrt(g0)+epsilon_t)^2],

with the zero-denominator feasibility case handled separately. The ordinary
finite-observation range test remains necessary for exact vector data.
For a vector operator, epsilon_op<=sqrt(sum_i epsilon_i^2) is sufficient and

    ||G_mu-G0||op <= 2 sqrt(||G0||op) epsilon_op+epsilon_op^2.

There is no assertion G_mu<=G0 for arbitrary moving multipath clock/force
observations. An actual energy upper budget, measurement error bound, mu,
trajectory calibration and curved-background validity are not inferred from
these inequalities. The least-energy compatible state is not selected.

## Independently representable coherent count fixture

Keep the exact stationary two-body M6 reference: L=3/5, unit count duration,
alpha*kappa=1, station0 and spacecraft L e1, endpoint coefficients (1,-2,1).
For the massive plane wave, eta=-i alpha h/omega and
xi=-i alpha k n h/omega^2, up to removed homogeneous orbit/clock terms.
The original phase substitution, without reusing a guessed force window, gives

    T_i=(-i/omega) sum_j beta_j exp(i omega t_i,j)
        [(1+v z)exp(-2i omega L)+(v z-1)
                         -2v z exp(-i omega L-i k L z)],
    F_i=T_i/omega, z=n.e1.

The second channel is translated by one unit. Define a=omega L,b=kL,
I1(b)=integral_(-1)^1 z sin(bz)dz and
I2(b)=integral_(-1)^1 z^2 cos(bz)dz. Direct expansion gives

    J(k)=integral_(-1)^1 |bracket|^2 dz
        =8 sin(a)^2+(8/3)v^2[cos(a)^2+1]
             -8v^2 cos(a) I2(b)-8v sin(a) I1(b),
    I1=2[sin b-b cos b]/b^2,
    I2=2[(b^2-2)sin b+2b cos b]/b^3.

Use analytic limits I1(0)=0,I2(0)=2/3. Since the endpoint factor has modulus
squared16sin(omega/2)^4, the diagonal and lag-one Gram entries are

    G_lag=1/(4pi^2) integral_0^infinity
       k^2/omega^4 *16sin(omega/2)^4*J(k)*cos(omega lag) dk.

At mu=0 the exact M6 matrix is [[3064,-1871],[-1871,3064]]/(1620pi).
For any mu, |F_i|<=16/omega^2, so the absolute tail past K of each matrix
entry is <=128/(pi^2 K). This certifies only the tail; a floating finite
quadrature still needs its own error control and is labeled a diagnostic.
No curve is an observed scalar residual or a fitted parameter estimate.

## Open proof and implementation checks

Independently check the real-Hilbert normalization, BV jump terms, quotient
derivative supplier, low/high comparison and coherent angular integral.
Implement direct harmonic versus derived-weight response and nonzero-acceleration
controls. Preserve failed calculations. A curvature extension is not proved
by the massive flat-patch result, even though the action ties their scales.
