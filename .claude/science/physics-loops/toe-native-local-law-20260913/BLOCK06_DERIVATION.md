# Native lapse commutators: proposed continuum algebra and lattice bound

2026-09-13. Written before the new finite challenges. These are author
calculations, not independent review. Ordinary CAR/Hamiltonian dynamics,
chosen free Wilson model, lapse fields and continuum scaling are supplied.
No interacting gravitational constraint theorem or physical axiom selection
is assumed. The purpose is to expose and test a precise dynamical interface.

## 1. Continuum normal/normal commutator

On smooth compactly supported two-component spinors in Euclidean spatial
coordinates y, let p=-i grad, h=sigma.p and

    H[N]={N,h}/2=-i[N sigma.grad+(sigma.grad N)/2].           (D1)

N,M are real smooth scalar smearing fields; positive fields give the physical
lapse subfamily. Set a=N grad M-M grad N. Direct use of the product rule and
sigma_i sigma_j=delta_ij I+i epsilon_ijk sigma_k gives

    [H[N],H[M]]=-[a.grad+div(a)/2] I
                       -(i/2) sigma.(grad N cross grad M).

Since curl(a)=2 grad N cross grad M,

    i[H[N],H[M]]=D[a],
    D[a]=-i[a.grad+div(a)/2]+sigma.curl(a)/4.                (D2)

All derivatives on the right act on the spinor except those explicitly on
a,N,M. For the second-derivative coefficient in the product, NM-MN vanishes.
The first-derivative spin pieces combine through the Pauli anticommutator to
-a.grad. The remaining scalar term is
-(N Delta M-M Delta N)/2=-div(a)/2, and the zero-order matrix commutator
is -(1/4)[sigma.grad N,sigma.grad M]. This proves the candidate identity
for arbitrary spinors without testing a selected eigenstate.

D[a] is symmetric on this domain: half the divergence is the density
correction and its spin potential is Hermitian. For a rigid rotation
 a=Omega cross y, it is Omega.(L+sigma/2). The spin term has a directly
checkable normalization and is not an arbitrary current improvement.
The identity is a statement about a specified free matter Hamiltonian;
it is not the full constraint algebra of a quantized metric.

For a continuum Dirac mass one may use four Hermitian alpha_i,beta with
{alpha_i,alpha_j}=2delta_ij, {alpha_i,beta}=0 and beta^2=I.
The corresponding normal/normal mass terms cancel: the derivative contribution
-im(N grad M-M grad N).alpha beta is canceled by the two half-density/mass
commutators. The spin generator uses the alpha commutator representation.
This optional continuum check does not introduce a massive Wilson model.

## 2. The remaining fixed-frame brackets

Let S(a)_ij=(partial_j a_i+partial_i a_j)/2 be the symmetric strain and set

    K[S]=-i sigma_j[S_ij partial_i+(partial_i S_ij)/2].     (D3)

The product rule gives

    i[D[a],h]=-K[S(a)],
    i[D[a],H[N]]=H[a.grad N]-{N,K[S(a)]}/2.               (D4)

For a rotation S=0 and this is the expected scalar-lapse transport.
For a dilation a=y, S=I and i[D,h]=-h: the residual is an operator, not a
statistical or cutoff effect. A candidate frame variation can supply it:

    h[e]=-i sigma_j[e_j^i partial_i+(partial_i e_j^i)/2],
    delta e_j^i=S(a)_ij  at e=I
           => delta H_e[N]={N,K[S(a)]}/2.                (D5)

Thus this explicitly stated infinitesimal frame response cancels the fixed-
frame residual in(D4), for the sign convention in(D2). A derivation of the
frame's own canonical dynamics, transformations at nonflat e and constraints
is still required before interpreting(D5) as a gravitational theory.

For two real vector fields, define [a,b]=a.grad b-b.grad a. Then

    i[D[a],D[b]]-D[[a,b]]
      = (1/4) sigma_k epsilon_kij [S(a),S(b)]_ji.          (D6)

One route to(D6) writes D=-i L+sigma.curl/4, uses
[L_a,L_b]=L_[a,b] for the half-density transport, and expands the curl of
[a,b]. The antisymmetric Jacobian commutators cancel against the Pauli spin
commutator. The antisymmetric part of the two symmetric strains remains.
The formula is to be challenged with arbitrary polynomial jets, including
nonlinear fields; a linear-field check alone is not sufficient.

There is a simple exact nonzero fixture. Take

    a=(y1,0,0), b=(y2,y1,0).

Both curls vanish, but [a,b]=(-y2,y1,0) is a unit rotation, giving

    i[D[a],D[b]]-D[[a,b]]=-sigma3/2.                     (D7)

This is an existence witness for the specified fixed-frame prescription.
Transporting the metric/frame can change this commutator. No general spinor,
diffeomorphism or axiom no-go is inferred. The symmetric-strain residual is
the exact data a full frame variation must address.

## 3. Native Wilson scaling about each node

Use the free native model specified in the previous source campaign, with
zeta in[1/2,1), pstar=acos(zeta), v=sqrt(1-zeta^2), and node sign w=+/-1.
The exact dimensionless Bloch symbol is

    d(k)=(sin k1,sin k2,2+zeta-cos k1-cos k2-cos k3).

For a supplied positive lattice spacing a_lat (a parameter, not a derived
Planck scale), remove the node modulation and scale time by1/a_lat. The
one-particle envelope symbol is

    h_a,w(p)=d((0,0,w*pstar)+a_lat*p).sigma/a_lat,
    h_w(p)=sigma1 p1+sigma2 p2+w*v sigma3 p3.             (D8)

Its third component has the exact form

    [1-cos(a_lat*p1)+1-cos(a_lat*p2)
      +zeta(1-cos(a_lat*p3))+w*v sin(a_lat*p3)]/a_lat.

Using |sin u-u|<=|u|^3/6 and |1-cos u|<=u^2/2 gives, for |p|<=P,

    ||h_a,w(p)-h_w(p)|| <= delta_a(P),
    delta_a(P)=a_lat P^2/2+a_lat^2 P^3/6.                (D9)

For the quadratic part use zeta<=1; for the cubic part use
sum_i |p_i|^3<=|p|^3 and v<=1. The bound is uniform in the stated zeta
interval as an absolute multiplier estimate. The coordinate rescaling in the
continuum comparison is not uniform as v tends to zero at node merger.
Also ||h_w(p)||<=P and ||h_a,w(p)||<=P+delta_a(P).

The leading correction is

    (a_lat/2) sigma3(p1^2+p2^2+zeta*p3^2),               (D10)

with cubic remainder bounded by a_lat^2 P^3/6 plus the fourth-order cosine
remainder if the quadratic term is extracted explicitly. Equation(D9), not
an asymptotic fitted coefficient, will control the commutators.

## 4. Low-frequency operator comparison, without a finite-mode fit

Let N,M be bounded real finite Fourier sums with Fourier support in |q|<=B,
and let the initial envelope spinor have Fourier support in |p|<=K. Put
P=K+2B and require a_lat P<pstar, which separates the two node neighborhoods
and also stays inside the first-zone boundary because pstar<=pi/3.
Set n=||N||_infinity, m=||M||_infinity. Define

    H_a[N]={N,h_a,w}/2,  H_w[N]={N,h_w}/2.

For every intermediate vector with support at most K+B, multiplication by
N or M shifts support by at most B. The elementary multiplier estimates give

    ||(H_a[N]-H_w[N])f|| <= n delta_a(P)||f||,
    ||H_w[N]f|| <= n P||f||,
    ||H_a[N]f|| <= n(P+delta_a(P))||f||.                 (D11)

Here each use of(D11) carries the appropriate input support. The product
expansion, with two error-linear commutators and the error/error commutator,
therefore proves on the initial band

    ||(i[H_a[N],H_a[M]]-i[H_w[N],H_w[M]])f||
       <= n m[4P delta_a(P)+2delta_a(P)^2] ||f||.        (D12)

This is O(a_lat) at fixed K,B,N,M, with all constants explicit. The estimate
is an operator norm on the declared band; no large torus or spectral sample
proves it. A finite Fourier test will challenge its normalization separately.

One precise common Hilbert-space interpretation uses Shannon interpolation
of the infinite lattice envelope. To match the native convention c_n=sum_k
exp(-ik.n)c_k with the continuum convention exp(ip.x), identify x=-a_lat*n
and multiply the envelope by exp(-i w*pstar*n3). This is an explicit coordinate
orientation convention, not a physical parity-symmetry claim. The normalization a_lat^3 sum_n |f(-a_lat n)|^2
matches the continuum L2 norm inside the first Brillouin cube. The stated
support condition prevents aliasing in every product used above, so sampled
multiplication and continuum multiplication are intertwined on these bands.
Equivalently use sufficiently large finite periodic envelope boxes with a
node phase twist and the same nonaliasing support; their wrap bonds are a
spectral regulator, not bounded-length physical paths in an open Z3 box.

For anisotropic node w, define x_i=v_i y_i with v_i=(1,1,w*v). Then
h_w=-i sigma.grad_y, and the vector produced by(D2) in physical x coordinates
is

    a_x^i=v_i^2(N partial_i M-M partial_i N).             (D13)

The spin term uses curl_y and a_y^i=a_x^i/v_i; equivalently it is
(1/2) sigma_k epsilon_kij v_i v_j (partial_i N)(partial_j M).
Thus(D12) compares the exact native lapse commutator with this specified
spin-dependent spatial generator. It does not make the background velocities
isotropic or derive the metric coefficients from the axioms.

## 5. CAR lifting and the sea question

On every finite CAR space,

    [dGamma(A),dGamma(B)]=dGamma([A,B]).                  (D14)

This follows by applying the canonical anticommutation relations and canceling
the quartic terms. On a fixed r-particle sector the norm of dGamma(C) is at
most r||C||. Therefore(D12) lifts to finite-particle states whose one-particle
Fourier supports meet the same hypothesis, with a factor r.

For a finite supplied sea projector P, define
:B:_P=dGamma(B)-Tr(PB)I. Then

    [ :A:_P, :B:_P ]= :[A,B]:_P+Tr(P[A,B])I.            (D15)

A scalar term must be kept unless it is explicitly zero. For the free
traceless two-band Wilson model and the arithmetic energy vertex,
V(k,q)=[h(k)+h(k+q)]/2 is a Pauli vector, so V(k,q)^2 is scalar. Since the
negative-band projector has trace1, Tr P(k)V(k,q)^2 does not depend on its
spin orientation. Its summed coefficient is even in q by changing k to k-q.
Hence Tr P[H[N],H[M]]=0 for every finite gapped reciprocal lattice and real
N,M. This finite cancellation will be challenged with the actual matrix
construction. It does not establish an unregulated infinite-sea commutator,
a stress anomaly theorem or an interacting central-term cancellation.

## 6. Current scientific standing

The proposed normal/normal calculation and controlled native limit address one
precise dynamical interface missing from the static source result. The mixed
and shift/shift calculations identify explicit frame-strain terms. A full
metric variation that closes the whole algebra, including its canonical
gravity sector and matter stress, remains the stretch target. So do its
interacting validity and physical time/Record realization.
These are author proofs to check, not a negative theorem or an axiom update.
The continuum commutator and spinor Lie-derivative machinery are established
mathematics; any milestone must justify the added native-model derivation
rather than claim those general identities as new discoveries.
