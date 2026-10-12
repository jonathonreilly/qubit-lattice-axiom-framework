---
claim_id: hstar_threshold_spectral_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
claim_scope: "For the supplied globally compressed sine-Pauli operator and the actual initial source direction, the kernel-complement scalar spectral measure has an explicit positive threshold density and the free fast primitive has a sharp square-root scaling with a uniform absolute squared-norm remainder. The full noncommuting actual-error comparison is a separate theorem."
upstream_dependencies:
  - excluded_walk_boost_bracket_control_bounded_theorem_note_2026-10-11
runner: scripts/hstar_threshold_spectral_2026_10_12.py
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# The physical H-star threshold seen by the actual source direction

2026-10-12. Bounded derivation by `boost_kernel_dynamics`; root proposed
the spectral lead and is a coauthor. Status: conditional-support. A separate
complete scientific reconstruction found no required correction. This note
uses the source-checked B/E/X physical setup and rederives the needed kernel
identities. No conclusion from the quantitative Q theorem is a premise here.

For the supplied physical operator H_*=H(0), put

    h0(q)=2 sin(q) dot T,  Pi=1_{0}(H_*),  Q=I-Pi,
    I0=integral_T3 dq/[(2pi)^3 4|sin q|^2].

The spectral measure of Qh0 is absolutely continuous in a neighborhood
of zero and has the two-sided threshold density

    rho_Qh0(E)=1/(4pi^2 I0^2)+O(E^2),         E->0.          (S1)

There is no zero atom after this projection. An explicit neighborhood and
an error constant are proved below. Consequently, for every fixed real
t!=0 and the free fast primitive only,

    J_lambda(t)=integral_0^t exp[-i(t-s)H_*/lambda]Qh0 ds,
    ||J_lambda(t)||^2
        =|t|lambda/(2pi I0^2)+O(lambda^2),
    ||J_lambda(t)||/sqrt(lambda)
        ->sqrt[|t|/(2pi I0^2)]>0.                          (S2)

This establishes sharp square-root-lambda scaling for this fixed source
direction under H_*/lambda. It does not establish a lower bound for the
full noncommuting slow generator, the time-dependent actual residual,
W_lambda-z, a boost expectation, or an optimal growing-time window.
All times in S2 are the integration variable of this free fast problem.
They are not silently substituted into a result for the actual walk.

## 1. Exact source contract and mathematical imports

S denotes the original research source collection, preserved losslessly in the
[complete milestone packet](../.claude/science/physics-loops/toe-boost-threshold-sharpness-20261012/). EVIDENCE_MAP.json maps the exact source identities below
to their preserved bytes. The in-branch [boost theorem](EXCLUDED_WALK_BOOST_BRACKET_CONTROL_BOUNDED_THEOREM_NOTE_2026-10-11.md)
contains the complete B/E/BR/T/X arguments and their supplied-model boundaries.

| Source | SHA-256 | Use |
|---|---|---|
| `ROOT_HSTAR_SPECTRAL_LEAD.md` | `5f46fe463706253f02ed8d8d42d0c89fac69a3b295999d4aac531bcd4300f4de` | Root proposal; signs and constants checked here |
| `EXCLUDED_WALK_BOOST_CURRENT_PROBE.md` | `903261f54d72d6e81d0c82d5cd976bd4dd46a55c1dd4567fe23d8bce07fe1923` | Exact sine-Pauli model, exclusion, parity and normalized torus |
| `EXCLUDED_WALK_EVOLVED_BOOST_CONTROL_DRAFT.md` | `d89611986626dbabcf6f9f5c487733d2a520cb9249b7ed0b3a27be35874fd929` | Exact forced comparison; no quantitative spectral premise imported |
| `BOOST_CURRENT_INVERSE_ENERGY_PROBE.md` | `76ed691c581d4da282041b99fa53da48d1461b47ddccb765b736969a191b4990` | T12 full physical kernel, rederived below |
| `BOOST_CURRENT_EXPECTATION_PROBE.md` | `a7161d796001df4af243263acbd03e731d75d0eab2d93795f4b5960eff5acb68` | X2/X7 physical source and initial residual identification |
| `BOOST_CURRENT_EXPECTATION_REVIEW.md` | `0e17f9647141c200b1efcbe78f60ef6beedc1e249ce1b85544293dddbebe8690` | Prior source-bound X review; no coverage of this new derivation |
| `boost_expectation_review/PROOF_RECONSTRUCTION.md` | `04adc0b81d3865f4819b8441e25279ef084bda755e9c0a3206be7d314ea04f9f` | Prior complete reconstruction reused at unchanged identity |

The necessary source arguments and applicable instructions were previously
read completely at these revisions. The lead, physical/source setup, T12
and full E note were freshly read in this task. Exact copies and coverage
are in `hstar_threshold_spectral/source_manifest.json`. The supplied lattice,
clock, antisymmetric pair sector and contact rule remain premises. No axiom
or registered native primitive supplies or changes them here.

The imported functional calculus and inversion theorem were checked in
Gerald Teschl's author-hosted [Mathematical Methods in Quantum Mechanics](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
version February 12, 2009: Theorems 3.1, 3.7 and 3.21, with their necessary
proof passages. They apply to our bounded self-adjoint operators and finite
scalar spectral measures. Teschl uses (A-z)^(-1); this note uses (z-A)^(-1),
so the inversion density is minus the upper-boundary imaginary part divided
by pi. The fetched PDF has SHA-256
`8dc8de0b58aa0a3fedfe594a345f9b5875322e5526ea581cb640a98d55b82818`.
The evidence records its URL, byte identity and read scope; no full book is
copied into the packet. The rank-one identity, threshold change of variables,
boundary regularity and primitive integral are proved here rather than
imported from an unverified rank-one or threshold theorem.

## 2. Parity, domains and the longitudinal square

Write s=sin q, epsilon=|s|, n=s/epsilon off its null set, and let c be the
constant unit singlet. The three T_j=sigma_(1,j)c form an orthonormal triplet
basis. All relative inner products use the complete normalized measure
`dmu=dq/(2pi)^3`, with total mass one, and are conjugate linear first.
Antisymmetry requires even singlet and odd triplet coefficient fields.
The source's physical projection removes the one global constant singlet:
`P=I-|c><c|`, not a pointwise spin projection.

Let E_even be the scalar even subspace of L2(dmu), with unit constant 1,
and E_even,0 its mean-zero subspace. Put

    h(q)=2epsilon(q),   Y(q)=h(q)^2,
    P0=I-|1><1| on E_even.

An odd triplet field has the unique orthogonal decomposition
`u(q)=v(q)n(q)+u_tr(q)`, where v is even and n dot u_tr=0. Thus

    U(f,v)=f c+v n

is a unitary identification of E_even,0 plus E_even with the physical
singlet/longitudinal subspace. It has no additional factor of two: both
sides use full-torus norms. Its complement is the physical transverse
triplet subspace.

The Pauli action at K=0 is the singlet/triplet matrix
`[[0,2s^T],[2s,0]]`. Compression by the global P gives on this reducing
subspace

    U^*H_*U=[0    A^*],
             [A      0],
    A:E_even,0 -> E_even,      Af=hf,
    A^*v=P0(hv).                                         (S3)

All these operators are bounded; their domains are the entire indicated
Hilbert spaces. No q derivative, unbounded dipole or self-adjoint extension
is involved. The transverse subspace is killed by H_*. The longitudinal
square is exactly

    L_long:=AA^*=M_Y-|h><h| on E_even,
    <v,L_long v>=||hv||^2-|<h,v>|^2>=0.                  (S4)

Here |h><h| is the full-torus rank-one operator. Positivity alone does
not determine the sign: M_Y+|h><h| is also nonnegative. The factorization
in S3 and the kernel equation below fix the minus sign.

Folding the eight sine cells into [-pi/2,pi/2]^3 and using
`epsilon>=(2/pi)|q|` there proves `I0=||1/h||^2<infinity`, with the inherited
explicit upper bound pi sqrt(3)/8. Cauchy–Schwarz gives the useful lower
bound `6I0>1`: indeed ||h||^2=integral Y=6 and h is nonconstant, so equality
cannot hold in `<h,1/h>=1`. Therefore

    zeta_long=1/(h sqrt(I0)),
    ker L_long=span{zeta_long},
    ker H_*=transverse direct-sum span{zeta},
    zeta=U(0,zeta_long),
    Pi h0=zeta/sqrt(I0),
    Qh0=U(0,r),  r=h-1/(I0 h),
    ||Qh0||^2=6-1/I0>0.                                  (S5)

To check completeness, Af=0 implies f=0 since h>0 almost everywhere;
A^*v=0 implies hv is constant, hence v is a multiple of 1/h. The vector
h0 equals U(0,h) and has no transverse component. The excluded constant
singlet is not a physical zero mode. Cone singularities of zeta are L2;
no q-Sobolev regularity is assumed or needed.

## 3. Exact source resolvent and its zero atom

Let nu_Y be the probability distribution of the multiplication function Y
under dmu, and use the convention

    F_Y(z)=integral dmu/(z-Y)=integral dnu_Y(s)/(z-s),
    G(z)=<h,(z-L_long)^(-1)h>,           Im z>0.

These transforms have negative imaginary parts. Let R0=(z-M_Y)^(-1).
The scalar `G0=<h,R0 h>=zF_Y(z)-1`. Solving the rank-one resolvent equation,
or directly multiplying the following expression by z-L_long, gives

    (z-L_long)^(-1)
       =R0-R0|h><h|R0/(1+G0),
    G(z)=G0/(1+G0)=1-1/[zF_Y(z)].                         (S6)

There is no sign or conjugation ambiguity in R0 on its right side: the
resolvent product is an operator product, not a norm square. The denominator
is nonzero in the upper half-plane, since F_Y has strictly negative
imaginary part and z!=0. A second direct calculation is to solve
`(z-Y)v+h<h,v>=h`; pairing gives G=G0(1-G), reproducing S6.

For a>0, dominated convergence against 1/Y gives
`F_Y(-a)->-I0`. Since L_long is nonnegative,

    mu_h^{L_long}({0})=lim_(a down to0)(-a)G(-a)=1/I0.     (S7)

The same weight follows directly from `<zeta_long,h>=1/sqrt(I0)` in S5.
These are two checks of the zero residue. This negative-axis limit alone
would not establish a real-axis density or exclude singular continuous
measure. The necessary boundary statement is proved next.

## 4. The eight-cone density, including the numerical coefficient

For any bounded Borel phi,

    integral phi(Y)dmu
      =pi^(-3) integral_[-pi/2,pi/2]^3 phi(4|sin q|^2)dq
      =(8pi^3)^(-1) integral_[-2,2]^3
            phi(|u|^2) product_j(1-u_j^2/4)^(-1/2)du.     (S8)

The first factor accounts for all eight periodic zeros; the second is
u_j=2sin q_j and its exact Jacobian. For 0<s<4, the sphere |u|=sqrt(s)
is entirely inside the cube. Spherical coordinates and r^2=s therefore
give an exact local density

    rho_Y(s)=sqrt(s) a(s),
    a(s)=(16pi^3)^(-1) integral_S2
                  product_j(1-s omega_j^2/4)^(-1/2)dOmega,
    a_*=a(0)=1/(4pi^2),
    a'(0)=a_*/8,
    rho_Y(s)=sqrt(s)/(4pi^2)[1+s/8+O(s^2)].              (S9)

The sphere area 4pi and `r^2 dr=(sqrt(s)/2)ds` are both retained.
The function a is positive and smooth on [0,4), indeed analytic there.
Parity does not divide this density by two: the even constant and all
vectors in this calculation retain the complete normalized torus norm.

For an independent coefficient calculation, each scalar variable
`y_j=4sin^2(q_j)` has probability density
`p(y)=1/[pi sqrt(y(4-y))]`, 0<y<4, obtained from its four one-dimensional
preimages. Near zero it equals `(2pi)^(-1)y^(-1/2)[1+y/8+O(y^2)]`.
The three variables are independent. Their convolution coefficient uses

    integral_(x>0,y>0,x+y<1) [xy(1-x-y)]^(-1/2)dxdy=2pi,

because the inner beta integral is pi and the remaining integral is 2.
Thus the coefficient is `(2pi)^(-3)2pi=1/(4pi^2)`, and the first relative
correction is `(y1+y2+y3)/8=s/8`, independently recovering S9.

We will use explicit derivative bounds for 0<=s<=1. Define

    A0=a_*(4/3)^(3/2),   B0=A0/6,   B1=A0/24.

Logarithmic differentiation of the integrand in S9 gives

    0<a(s)<=A0,   |a'(s)|<=B0,
    |a''(s)|<=A0/12,
    b(s):=[a(s)-a_*]/s,  b(0)=a'(0),
    ||b||_infinity<=B0,   ||b'||_infinity<=B1.             (S10)

For completeness, the integrand's logarithmic first and second derivatives
are bounded by `1/[8(1-s/4)]` and `1/[32(1-s/4)^2]`. Its second derivative
is bounded by its value times `3/[64(1-s/4)^2]`. At s<=1 these are the
bounds displayed. The b bounds follow from
`b(s)=integral_0^1 a'(theta s)dtheta` and its derivative.

## 5. Boundary values, uniformity and local absolute continuity

For every compact interval J inside (0,1), the upper boundary value exists
uniformly on J and is

    F_+(s):=F_Y(s+i0)
       =PV integral dnu_Y(y)/(s-y)-i pi rho_Y(s).          (S11)

Here is a direct justification of the uniformity needed later. Split the
measure at y=1. Its part on [1,12] has a resolvent analytic near J. On
(0,1), subtract rho_Y(s) from the density in the Cauchy integral. The
remaining quotient has a bounded integrable majorant near y=s, uniformly
in s in J, because rho_Y is smooth on a slightly larger compact interval.
For a small fixed neighborhood of y=s its integral is bounded by a constant
times that neighborhood's length. Away from that neighborhood, convergence
as Im z decreases to zero is uniform. The constant-density integral has
its explicit logarithmic limit with imaginary part -pi. These facts prove
S11 uniformly on J without assuming a boundary theorem at the endpoint.
The endpoint y=0 causes no problem for this local argument: rho_Y(y) is
integrable there and remains separated from s in J.

To control the actual threshold, take 0<s<=1/4. Subtract the convergent
scalar endpoint integral -I0 in the real principal value and split at y=1.
This endpoint integral is not an operator resolvent at zero:

    Re F_+(s)+I0
      =s PV integral_0^1 a(y)/[sqrt(y)(s-y)]dy
         +s integral_[1,12] dnu_Y(y)/[y(s-y)].             (S12)

The leading low-energy term has the exact value

    s a_* PV integral_0^1 dy/[sqrt(y)(s-y)]
      =a_* sqrt(s) log[(1+sqrt(s))/(1-sqrt(s))],

whose magnitude is at most `(8a_*/3)s`. For the remainder put
`g(y)=sqrt(y)b(y)`. It is one-half-Hölder with constant at most B0+B1.
Subtracting g(s) gives

    PV integral_0^1 g(y)/(s-y)dy
      =integral_0^1 [g(y)-g(s)]/(s-y)dy
                       +g(s) log[s/(1-s)].

The first integral has magnitude <=4(B0+B1). The second is <=2B0:
on (0,1/4], sqrt(s)|log[s/(1-s)]|<=sqrt(s)log(1/s)<=2/exp(1)<1.
The relaxed factor two is harmless. The tail in S12 has magnitude <=4s/3.
Thus, with the explicit constant

    C_F=8a_*/3+6B0+4B1+4/3,
    |Re F_+(s)+I0|<=C_F s,
    Im F_+(s)=-pi sqrt(s)a(s),
    F_+(s)=-I0-i pi a_*sqrt(s)+O(s).                       (S13)

In particular the real part has an O(s), not merely O(sqrt(s)), error.
No exchange of an off-axis endpoint limit with a boundary limit was used.
Choose

    delta=min{1/4,I0/(2C_F)},
    K_F=2I0 C_F+C_F^2 delta+pi^2 A0^2.

Then for 0<s<=delta,

    |F_+(s)|>=I0/2,
    ||F_+(s)|^2-I0^2|<=K_F s.                             (S14)

For every compact positive interval inside (0,delta), S11, S14 and S6 give
uniform convergence of G to its finite continuous boundary value. The
scalar Stieltjes inversion formula therefore gives the entire restricted
measure, not only its absolutely continuous part:

    dmu_h^{L_long}(s)=rho_L(s)ds,
    rho_L(s)=rho_Y(s)/[s|F_+(s)|^2],        0<s<delta.      (S15)

To make the exclusion of singular mass explicit, bounded scalar resolvent
boundary values imply there is no atom at any point of such a compact
interval (multiply the imaginary part by Im z). Inversion and uniform
convergence then identify the measure of every subinterval with the
integral of the displayed density. A countable cover excludes singular
continuous measure on (0,delta). At zero the entire mass is exactly S7.
No statement about the spectral type at energies away from this neighborhood
is required.

## 6. From the square to the signed H-star spectral measure

The grading Gamma(f,v)=(-f,v) is unitary, fixes U(0,h), and satisfies
Gamma H_* Gamma=-H_* on the longitudinal block. Thus the H_* source measure
is symmetric. Its pushforward under E->E^2 is mu_h^{L_long}. For s>0,
the two branches have equal weight. Their factor one-half and the Jacobian
`ds=2|E|dE` cancel, giving

    rho_h0^{H_*}(E)=|E|rho_L(E^2)
      =a(E^2)/|F_+(E^2)|^2,          0<|E|<sqrt(delta).    (S16)

An independent resolvent check is
`<h0,(w-H_*)^(-1)h0>=w G(w^2)`: the H_* term in
`(w+H_*)(w^2-H_*^2)^(-1)` has zero source pairing by the off-diagonal
block. For negative real w, w^2 approaches the lower boundary and conjugates
G; the resulting density is again |w|rho_L(w^2), with the same sign and
no extra factor two.

Projection Q deletes just the weight 1/I0 at E=0 from this source measure.
Consequently the measure of Qh0 is absolutely continuous throughout
(-sqrt(delta),sqrt(delta)); a measure supported only at zero would be an
atom, which has already been removed. With

    c_th=a_*/I0^2,
    C_rho=4B0/I0^2+4a_*K_F/I0^4,
    |rho_Qh0(E)-c_th|<=C_rho E^2,
                         0<|E|<=sqrt(delta),             (S17)

S1 follows. The estimate uses S10 and S14 in the difference
`a(s)/|F_+(s)|^2-a_*/I0^2`. It is symmetric and has the same positive
threshold value from both sides. It is a source-specific statement and
does not assert a scalar dispersion for the full physical operator.

## 7. Exact free primitive and its asymptotic

Bounded spectral calculus applies to J_lambda(t). Its scalar multiplier is
`lambda(1-exp(-itE/lambda))/(iE)`, with value t at E=0. Since the source is
Qh0, that value carries zero spectral mass. Therefore

    ||J_lambda(t)||^2
       =integral 4lambda^2 sin^2(tE/(2lambda))/E^2
                                       dmu_Qh0^{H_*}(E).  (S18)

Let e0=sqrt(delta). The part |E|>=e0 is at most
`4lambda^2(6-1/I0)/e0^2`, regardless of its spectral type. On |E|<e0,
S17 bounds the density-error contribution by `8C_rho e0 lambda^2`.
Extending the constant-density integral to the full real line changes it
by at most `8c_th lambda^2/e0`. The elementary identity

    integral_R 4sin^2(x/2)/x^2 dx=2pi

then gives the explicit error bound

    | ||J_lambda(t)||^2-2pi c_th |t|lambda |
       <=C_J lambda^2,
    C_J=8C_rho e0+8c_th/e0+4(6-1/I0)/e0^2.                (S19)

The constant is finite, positive and independent of lambda and t. S19 is
an estimate for this free primitive alone; only its fixed nonzero-t
consequence S2 is used here. Negative t follows from the squared multiplier.
At t=0 the primitive vanishes exactly.

For a normalization check on the elementary integral, damp the positive
integrand `(1-cos(ax))/x^2` by exp(-epsilon x) on x>0. Differentiating
with respect to a gives arctan(a/epsilon), obtained by one further
parameter derivative of the elementary Laplace integral. Integrating a
from zero and taking epsilon down to zero gives pi|a|/2. This proves the
displayed full-line constant, including both signs of energy.

The actual initial X averaging residual has the direction addressed here.
Using X's exact limiting equation with z(0)=0 gives

    r_X(0,kappa)=-c0 a(0,kappa) Qh0,
    c0=(2pi)^(-3/2).

For each fixed t!=0, the free H_* primitive of this initial, time-frozen
residual in the full rescaled direct integral obeys

    ||integral_0^t exp[-i(t-s)H_*/lambda]r_X(0)ds||^2/lambda
       ->c0^2||a(0)||_L2(kappa)^2 |t|/(2pi I0^2)>0.       (S20)

This is still a time-frozen free forcing statement. Its positivity follows
from the exact nonnegative packet: with m=integral f>0, w>=1/4 and the
single global Z0, `||a(0)||>=m/(4Z0)>0`. No quantitative Q result is needed
to identify this initial direction. S20 does not replace r_X(s,kappa) by
r_X(0,kappa) in the actual error equation.

## 8. Failed shortcuts, controls and remaining gate

The following routes are excluded by explicit mechanisms, not by an
unproved impossibility assertion.

- Keeping h0 instead of Qh0 leaves a zero atom of weight 1/I0. Its free
  primitive has the additional exact term t^2/I0 in its squared norm,
  orthogonal to the complementary primitive. The square-root scale would
  then be the wrong leading scale at fixed nonzero t.
- The formal singlet inverse producing Qh0 would be
  `1-1/(I0 h^2)`. It is not L2 near any cone, since h is comparable to
  distance and the integral of h^(-4) diverges in dimension three. A
  triplet input produces a singlet output and cannot repair this coefficient.
  Spectrally the same failure follows from the positive threshold density:
  `integral E^(-2)dmu_Qh0(E)=infinity`.
- The negative-axis limit F_Y(-a)->-I0 alone gives the zero residue, not
  the required boundary density. S11–S15 supply the missing uniformity and
  measure argument. No hidden singular component is discarded.
- A fixed finite momentum mesh has a nonzero smallest spectral energy
  after its kernel is removed. Its primitive is O(lambda), with squared
  norm divided by lambda tending to zero. Such a mesh can check rank-one
  algebra and normalization, but cannot establish the continuum threshold
  law by taking lambda to zero first.
- The elementary comparison bound for adding a bounded noncommuting
  perturbation is of order t^2 at fixed t, independent of lambda; it is
  too large to transfer S2. No lower bound for the full slow dynamics or
  actual W_lambda-z follows from this free calculation. The other supplied
  norm/mean results and their existing counterexamples are untouched.

The evidence directory records direct Pauli/block controls, two separate
cone-coefficient calculations, actual executions and literal failure probes.
An exact continuous radial model checks the boundary sign, square-root
Jacobian and primitive normalization; it is labeled as a model rather than
the torus. No finite mesh, fitted power or baseline count proves S1–S20.
The analytic proof and its hypotheses are the mathematical result.
`AUTHOR_CHECK.md` records the separate author arrangements and coverage.
Root and this worker are coauthors, so none of those controls is presented
as a fresh-context independent scientific review.

The separate review checked S3's even/mean-zero identification, the rank-one
sign and zero residue, all eight cones and both Jacobians, the uniform boundary
passage, the entire local measure and free-primitive normalization. Its report
is `913a9c81f6361981041034059cb2fc12f1485e257c18e9576cd016ffd74eda05`;
the 376-line reconstruction `0f66243e7a8322c1649990da27f56e509b1f18904ca2826d257e88ef05568377`
was frozen before new author evidence. The reviewer's corrected auxiliary
cubature and its first failed source/logs are preserved. Root is a contributor,
not this independent reviewer. The [finite control](../scripts/hstar_threshold_spectral_2026_10_12.py)
preserves the complete original helper; it does not prove continuum spectral
type. REVIEW_HISTORY.md and DELIVERY_CHECKS.md in the milestone packet record
each evidence role and publication checks. The separate downstream note
`ACTUAL_CORRECTOR_SMALL_TIME_LOWER_BOUNDED_THEOREM_NOTE_2026-10-12.md` proves
its own full actual-error comparison. S alone supplies no such lower bound.
No global spectral classification, optimal growing-time exponent, physical
boost law, Lean certificate, retained status or applied audit verdict is claimed.
No physical axiom or editable prompt changed.
