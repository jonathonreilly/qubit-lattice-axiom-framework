# Fourier energy and prescribed Gaussian/contact derivatives

Personal proof candidate, 2026-09-15. This extends the prescribed-contact
source estimate to derivatives of its complete Gaussian dressing. The scope
is a specified decorated signed loop on the infinite cubic kernel. Physical
connected graph summation and the full characteristic law remain open.

## 1. A direct cochain energy estimate

Use ordinary counting inner products on oriented cubic r-cells of Z^4,
one positive representative per orientation. In a site-based Fourier gauge,
the coboundary symbol is exterior multiplication by
z(p)=(exp(ip_1)-1,...,exp(ip_4)-1), and its adjoint is contraction by the
conjugate vector. Their anticommutator on the exterior algebra is

    Delta_r(p)=lambda(p) I, lambda(p)=4 sum_mu sin^2(p_mu/2).

Cell-center phases change the gauge unitarily and do not change this scalar
symbol. Thus G_r is the multiplier 1/lambda on finite cochains; the point
p=0 has zero integration measure. For p in [-pi,pi]^4,

    4|p|^2/pi^2 <= lambda(p) <= 16.

Let j be any nonzero finite real cochain, m=||j||_1 and r=||j||_2<=m.
The notation r for a norm in the next formulas is unrelated to cell degree.
The vector Fourier transform obeys ||jhat(p)||_2<=m, and Parseval gives
integral ||jhat||_2^2 dp/(2pi)^4=r^2. Split at the ball of radius R,
where R^2=pi^2 r/m<=pi^2, so the entire ball lies in the Brillouin cube.
Its low-frequency contribution is at most

    (pi^2/4) m^2 integral_(|p|<=R) |p|^-2 dp/(2pi)^4
       =m^2 R^2/64.

The complement contributes at most pi^2 r^2/(4R^2). Consequently

    <j,G_r j> <= H m r,   H=1/4+pi^2/64 < 0.405.       (1)

As a separate normalization check, a unit plaquette boundary has Fourier
norm squared |z_mu|^2+|z_nu|^2. Symmetry of the four coordinate integrals
gives its exact infinite Green energy 1/2. On an N^4 momentum grid with
the zero mode removed, the corresponding sum is exactly (1-N^(-4))/2.

The zero cochain is immediate. No closure, connected support or integer
hypothesis is used in (1). Those enter the component interpretation and
activity reserve below. This improves the initially recorded R^2=r/m
constant by using a larger ball that still lies entirely in the cube.
The argument is elementary Fourier integration, not an imported HLS theorem.

For the stable Gaussian Gram feature

    psi(j)=sqrt(x) (G_r-I/32)^(1/2) j,

lambda<=16 ensures G_r-I/32 is positive on finite cochains. More precisely
these finite cochains lie in the square-root form domain by (1), defining
psi in the common l2 cochain Hilbert space. Thus

    ||psi(j)||^2 <= x H m r.                           (2)

This is an infinite-cubic statement. It is not automatically a bound for
finite free-boundary relative cochains or torus zero modes. A finite Fourier
sum below is a discretization check only; no boundary matching is inferred.

## 2. Gaussian derivatives as feature-register contractions

Retain D(S)=product_u det S[I_u,I_u] and the complete Gaussian

    G_sigma(S)=exp[-1/2 sum_same i,j S_ij sigma_i sigma_j
                                           <psi_i,psi_j>],

including its diagonal. S is a fixed positive semidefinite unit-diagonal
matrix independent of the component labels/positions. For a specified set
E_G of distinct off-diagonal pair parameters,

    partial_(E_G) G_sigma
        =G_sigma product_((i,j) in E_G) [-sigma_i sigma_j <psi_i,psi_j>].

Pairs in different species give zero. Species Hilbert spaces can be placed
in orthogonal summands to implement this condition without changing norms.

For every edge use a register C|vac> direct-sum H_feature. In any total
vertex order, its first endpoint is the row <psi_i| from the feature sector
to vacuum and its last endpoint is the column |psi_j> from vacuum to the
feature sector; intermediate vertices act as identity on it. Vacuum
expectation gives exactly the inner product. Their operator norms are
||psi_i|| and ||psi_j||. A sign -sigma_i sigma_j splits into unit scalar
endpoint factors. The real Gaussian replica representation of G_sigma
adds local phases of modulus one, just as in the earlier source proof.
No trace over the feature Hilbert space is taken. In infinite dimension
the Gaussian is an isonormal family of scalar pairings with these features,
not a purported Hilbert-valued random vector with identity covariance.

Tensor these registers with the complete contact registers and their CAR
blocks from BLOCK2_CONTACT_REGISTER_SUM. For a fixed partition E=E_H union
E_G, let h_i,g_i be its incident contact/Gaussian degrees, d_i=h_i+g_i.
For one contact orientation the vertex norm is bounded by

    |A_i|^(h_i/2) ||psi_i||^(g_i).

The contact matching signs depend only on contact registers; the Gaussian
registers introduce no extra inversion sign. The scalar coefficient has
such a representation in EVERY cyclic order. Different realizations can
therefore be used for the different coincident-source boundaries of the
scalar three-lines proof. No commutation of one-sided maps is asserted.

## 3. One activity reserve absorbs all vertex degrees

For integer currents |A_i|<=3m_i and r_i^2>=m_i. Choose the positive
weight, independent of the prescribed derivative graph,

    q_i=(2/384) exp(-x_i r_i^2/64) 2^|A_i|
                         exp(m_i+x_i r_i^2/512) exp(R|L_i|).     (3)

Set t=x r^2. The elementary maxima and d!>=(d/e)^d give

    m^(d/2) exp(-m) <= sqrt(d!) 2^(-d/2),
    t^(g/4) exp(-t/512) <= (g!)^(1/4) 128^(g/4).

The degree-zero cases use the evident upper bound one. Equations (2)-(3)
then yield the normalized vertex bound

    C_H^h C_G(x)^g sqrt(d!) (g!)^(1/4),
    C_H=sqrt(3/2), C_G(x)=sqrt(H/2) (128x)^(1/4).       (4)

Indeed x^(g/2) r^(g/2)=x^(g/4)t^(g/4). In particular (4) is at most
C(x)^d (d!)^(3/4), C(x)=max(C_H,C_G(x)). This preserves a smaller
factorial power than estimates based on powers of a filling area.

For |z|<=R and a<=min(sqrt(x_e),sqrt(x_m))/(128 C_f R), the existing
physical source bound gives R|L_i|<=x_i m_i/128. Thus (3) satisfies

    q_i <=(2/384) exp[-3x_i m_i/512+(3log2+1)m_i]
        <=(2/384) exp[-x_i m_i/256]

if x_i/512>=3log2+1. Both x_i>=32768 suffice. The previous anchored
moments, sine matrix norm rho<3.862e-33, and S4=Tr |L|^4 J^2=O(a^4)
therefore apply to this NEW weight as upper bounds. No limit of x or N
with a is taken.

## 4. The precise prescribed-graph source consequence

Put q into the same scalar sine matrix J and let l be the protected loop
length. For fixed E_H,E_G and any placement of four source powers, the
complete contact-resource/orientation sum with Gaussian derivatives obeys

    |F_(E_H,E_G)| <= [product_i C_H^(h_i) C_G(x_i)^(g_i)
                                      sqrt(d_i!) (g_i!)^(1/4)]
                                rho^(l-2) S4.          (5)

As before, the factor 2^(-|E_H|) in each oriented CAR representation is
canceled by summing the 2^|E_H| contact orientations. Gaussian signs have
modulus one. Expectation over replicas and orientation signs preserves (5).
The same statement with two source powers uses S2=Tr |L|^2 J^2.

For the full derivative partial_E(D G_sigma), apply the ordinary Leibniz
partition of E. If C=max_species C(x), all 2^|E| terms give the uniform
bound

    (2 C^2)^|E| product_i (d_i!)^(3/4) rho^(l-2) S4.    (6)

Some cross-species terms vanish; (6) does not rely on counting that gain.
Taylor subtraction through quadratic order adds at most R^4 l^4/24.
At one fixed decorated graph, the earlier absolute graph/source estimates
justify the component-cutoff passage; extra Gaussian factors have the
existing polynomial filling bounds, and extra contact factors are local.
The operator bounds are uniform in that cutoff. No graph-order limit is
interchanged and no arbitrary forest sum is claimed here.

The remaining mixed pair factors are NOT replaced by arbitrary bounded
multipliers. The earlier counterexample rules out that shortcut. A separate
representation or summation for them, plus the actual physical graph
multiplicities and selected-state matching, is still required.


## Author verification and personal review scope

The cochain wedge/contraction symbols match lambda I with maximum matrix
error 3.79e-15. The Fourier grids reproduce the exact single-plaquette
normalization and sample two other finite cochains; no numerical
infinite-volume error estimate is claimed. Explicit tensor registers in
576 graph/order fixtures reproduce feature inner products and endpoint
norms. Full determinant/Gaussian nilpotent jets match the Leibniz form,
and four generic graph fixtures satisfy all35 four-source placements,
including the sharper direct vertex-norm bound. The analytic reserve
extrema are checked for degrees through40.

An initial synthetic random feature exceeded the declared energy premise
and stopped the check before the source assertion. Its script and failure
record are preserved under review/block4_initial_fixture_failure. The
revised synthetic fixture explicitly rescales into that premise; this is
a setup correction, not a change of the theorem or evidence for arbitrary
random features. A product-of-derivatives substitution is rejected by a
nonzero discrepancy. All verification is by the author; no independent
review or retained-grade conclusion is claimed.
