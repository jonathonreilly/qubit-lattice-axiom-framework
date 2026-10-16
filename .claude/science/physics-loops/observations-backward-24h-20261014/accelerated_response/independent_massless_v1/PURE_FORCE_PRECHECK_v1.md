# Independent pure-force massless derivation before author access

Reviewer `/root/inertial_response_check`; root remains scientific author.
No new accelerated-response draft or code has been read. The only prior exposure
is the parent's statement that an unreviewed runtime scratch draft exists.
The previously frozen M5 inertial derivation is known, with its constant-velocity
scope. No observation is read and no massive extension is assumed.

Use unitary spatial Fourier transform. A real massless free field can be written

    h(s,x)=(2pi)^(-3/2) integral [a(k)e^(ik.x-i|k|s)+conjugate] d^3k,

where a(k) is an unconstrained complex function. Its real laboratory-energy
Hilbert norm is ||h||_E^2=2E=4 integral |k|^2 |a(k)|^2 d^3k. The complex
representation must not impose an extra a(-k)=conj(a(k)) condition: reality is
already implemented by the displayed conjugate term.

Take a prescribed C2 path x, u=x', acceleration v=u', with |u|<1 and bounded
acceleration on a finite interval containing the compact support of real vector
W in H1. Continuity gives a uniform subluminal margin on that interval. Define
for n in the unit sphere

    A=1-|u|^2, d_n=1-n.u>0, tau_n=s-n.x(s),
    b_n=A(n-u).W,
    B_n=A(n-u)/d_n,
    H_n(tau_n(s))=b_n(s)/d_n(s)=B_n(s).W(s).

The strictly increasing tau_n map has a regular inverse on the interval. Extend
H_n by zero outside the image of the compact window. Since W has vanishing
endpoint trace and B_n has bounded derivative, H_n is compact H1. This is the
regularity needed for the dual norm; no jerk is needed.

For the full linear conformal force a_h=-A(grad h+u partial_s h), each positive
frequency plane wave supplies -i k b_n exp(-ik tau_n), k>0. Consequently the
functional L_W has plane-wave coefficient

    F_W(k n)=-(2pi)^(-3/2) i k integral H_n(tau)e^(-ik tau) d tau.

Real-Hilbert duality with norm 4 integral k^2 |a|^2 gives

    G(W,V)=1/(2pi)^3 integral_S2 integral_0^infinity
             k^2 Re[Hhat_W(k) conj(Hhat_V(k))] dk dOmega
          =1/(8pi^2) integral_S2 integral H'_W(tau)H'_V(tau) d tau dOmega.

For W=V, |L_W|^2 <= 2E G(W,W), with equality in the energy completion at the
Riesz representative when the functional is nonzero. The pointwise force of
arbitrary energy data need not exist; this formula defines the continuous
extension from smooth data. Massless zero-energy constant representatives do not
affect the force. Numerical examples corroborate but do not establish the norm.

Writing R_W=partial_s(B_n.W), the exact same-path formula is

    G(W,V)=1/(8pi^2) integral ds integral_S2 R_W R_V / d_n dOmega,
    R_W=B_n.W' + Bdot_n.W,
    Bdot_n=[-2(u.v)(n-u)-A v]/d_n
            + A(n-u)(n.v)/d_n^2.

The frozen inertial tensor is only the W'-W' portion. Acceleration contributes
the two cross terms and the Bdot-W square. Integrating those terms by parts to
manufacture a jerk is neither necessary nor legitimate under only C2 path
regularity. At instantaneous u=0, angular integration gives

    g_s = |W'|^2/(6pi)
          + (|v|^2 |W|^2 + 7(v.W)^2)/(30pi),

with zero W'-W cross term at that instant. This local identity is an independent
polynomial angular oracle; it is not by itself a global counterexample.

A global counterexample is explicit. Let x point along e1, with

    u(s)=beta sin^2(pi s) e1 on 0<s<1, and zero otherwise;
    x(s)=beta [s/2-sin(2pi s)/(4pi)] e1 on [0,1],

continued constantly before and after. It is C2, with continuous bounded
acceleration, and 0<beta<1. Let W=e1 w, where w rises from zero to one on [-1,0],
is one on [0,1], falls to zero on [1,2], and is zero elsewhere. The rises can
be linear H1 ramps or the C2 quintic p(t)=10t^3-15t^4+6t^5. Velocity and
acceleration vanish on both ramps; W' vanishes throughout the moving portion.
Thus the instantaneous inertial substitution equals the static ramp norm,
whereas the true norm is that value plus the strictly positive integral

    1/(8pi^2) integral_0^1 ds integral_S2 |Bdot_n.e1|^2/d_n dOmega.

For linear ramps the static term is 1/(3pi); for the quintic ramps it is
10/(21pi). The extra term is nonzero because Bdot is not identically zero for
the stated nonconstant velocity. There is no omitted interference between the
disjoint ramp/moving intervals: their arrival-time images on a single timelike
path are disjoint for every n.

Independent numerical oracles to freeze with this derivation:

1. Integrate the exact s/n derivative expression for the plateau counterexample.
2. Separately integrate original laboratory plane-wave coefficients
   integral A(n-u).W exp[-ik(s-n.x)] ds over positive k and sphere directions;
   compare the finite-frequency truncation at increasing cutoffs with oracle 1.
   This uses neither the inverse phase map nor Bdot in the Fourier integral.
3. Compare the u=0 acceleration angular polynomial with direct sphere quadrature.
4. Check the constant-u limit against the already immutable M5 tensor, without
   treating that old evidence as proof for accelerated motion.

For several prescribed paths, define each H_{j,n} on its own arrival-time
coordinate and extend it by zero. The response to the same free field has

    G_total=1/(8pi^2) integral_S2 integral |sum_j H'_{j,n}(tau)|^2 d tau dOmega.

Cross terms are at equal arrival phase, not generally equal laboratory time.
They can cancel or reinforce; summing diagonal norms is not exact. In particular
two coincident paths with opposite windows give zero total response. For two
stationary paths with r=x_b-x_a, the cross Gram is

    1/(8pi^2) integral_S2 integral
       [n.W'_a(s)] [n.W'_b(s+n.r)] ds dOmega.

For a strictly subluminal path the exact expression is continuous on compact H1
windows. A simple, nonsharp bound follows from |B| <= (1+b)^2 and
|Bdot| <= 2(1+b)^2 a_max/(1-b), where b bounds |u|<1. With the known inertial
W'-tensor bound and Minkowski,

    sqrt(G) <= ||W'||_2/sqrt(6pi)
      + 2(1+b)^2 a_max ||W||_2/[sqrt(2pi)(1-b)^(3/2)].

This is a conditional regularity/resource statement, not an observed energy
budget. The massive phase sqrt(k^2+mu^2)s-k n.x does not admit this k-independent
arrival coordinate. Nothing here extends the accelerated result to mu>0.
