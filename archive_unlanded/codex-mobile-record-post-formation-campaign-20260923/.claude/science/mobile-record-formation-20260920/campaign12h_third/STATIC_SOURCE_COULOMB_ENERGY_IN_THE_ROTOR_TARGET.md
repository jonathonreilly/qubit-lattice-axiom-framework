# Static-source Coulomb energy in the compact rotor target

Date: 2026-09-22. Author proof and controls; independent check pending.
This is a statement about a specified compact U(1) rotor Hamiltonian with
static integer sources. The campaign has a separate controlled neutral-field
limit from mobile records. A matching theorem for moving charged-record
defects has not been established. Static source sectors must not be silently
identified with those microscopic defects.

The result is a finite-box ground-energy comparison. At weak coupling, a
static source contributes the lattice Coulomb energy and its allowed
harmonic electric energy, with an exponentially small correction in this
fixed box. Taking the weak-coupling coefficient first, then the infinite-box
and long-distance limits, gives the usual attractive 1/r coefficient for
opposite charges. This does not prove a Coulomb phase at fixed coupling or
a uniform joint continuum limit.

## 1. Exact model and affine electric lattice

Use a cubic L by L by L torus with L>=3, volume V=L^3, positive-axis
orientation and the Euclidean inner product on its 3V real link fields.
Let B be the outgoing-minus-incoming divergence matrix and C the oriented
plaquette curl matrix, so BC-transpose=0. Let H be the three-dimensional
space of constant link fields and
\[
 {\cal S}=\ker B\cap{\cal H}^{\perp},\qquad
 \Lambda={\cal S}\cap\mathbb Z^{3V},\qquad
 {\cal Q}={\cal S}/(2\pi\Lambda^*).                    \tag{1}
\]
The dual in (1) is within S with its inherited Euclidean metric.
The dimension of S is 2(V-1). The lattice Lambda has full rank in S
because S is the kernel of integer linear constraints. Q is therefore
a compact flat torus.

Fix integer charges rho_x with sum rho=0, and choose one integer link
field e0 satisfying Be0=rho. Such a field exists by routing integer
charge along a spanning tree. Fix also its harmonic class. The sector
contains exactly the fields e0+lambda, lambda in Lambda. Different
allowed harmonic classes can be studied separately; they are not all
zero-harmonic sectors.

Set L0=BB-transpose, and let L0-plus be its inverse on zero-mean site
functions, zero on constants. The orthogonal decomposition is
\[
 e_0=E_{\mathrm L}+E_{\mathrm H}+\alpha,\quad
 E_{\mathrm L}=B^\mathsf T L_0^+\rho,\quad
 E_{\mathrm H}=P_{\cal H}e_0,\quad \alpha\in{\cal S},
 \quad
 \|E_{\mathrm L}\|^2=\rho^\mathsf T L_0^+\rho.          \tag{2}
\]
Hence every allowed electric word obeys
\[
 \|e_0+\lambda\|^2
 =\rho^\mathsf T L_0^+\rho+\|E_{\mathrm H}\|^2
                         +\|\lambda+\alpha\|^2.      \tag{3}
\]
Fourier transformation from ell-squared(Lambda) to L-squared(Q) turns
the transverse electric operator into \(-i\nabla_{\cal S}+\alpha\).
The offset alpha is a flat connection, defined modulo Lambda.

Consider the shifted target Hamiltonian
\[
 H_g=\frac{c}{2a}\left[g^2\sum_e E_e^2+
        \frac{2}{g^2}\sum_p(1-\cos (CA)_p)\right],
 \qquad c,a>0,\quad g>0.                              \tag{4}
\]
In electric language this is
\(K\sum E^2-J\sum_p(W_p+W_p^\dagger)+2J\,\#p\), with
K=cg^2/(2a), J=c/(2ag^2). Equation (3) gives the exact sector identity
\[
 H_g^{\rho,E_{\mathrm H}}
 =K\left(\rho^\mathsf T L_0^+\rho+\|E_{\mathrm H}\|^2\right)
       +\frac{c}{2ah}P_{h,\alpha},\quad h=g^2,
\]
\[
 P_{h,\alpha}=h^2(-i\nabla+\alpha)^2+{\cal V}(A),\qquad
 {\cal V}(A)=2\sum_p[1-\cos(CA)_p].                    \tag{5}
\]
The scalar in (5) is exact. The issue is whether the ground energy of
P depends on alpha at a comparable order.

The zero-source physical electric basis and its topological sectors are
standard; see [Kaplan and Stryker, Section I and the start of Section II](https://arxiv.org/html/1806.08797v2).
The affine source and flat-connection decomposition used here is written
out in (1)-(5); no change of Gauss sector is inferred from their
source-free model.

## 2. The harmonic term cannot be omitted at finite volume

For a positive charge Q at zero and a negative charge -Q at r=m e1,
choose the straight integer reference path Q on its m edges, with m<L.
Its total oriented electric field is (Qm,0,0). Thus
\[
 \|E_{\mathrm H}\|^2=Q^2m^2/V.                         \tag{6}
\]
Adding a winding loop changes an axis total by Q-independent integer
multiples of L. More generally all allowed harmonic totals differ by
L times an integer vector, as follows by decomposing an integer
divergence-free current into closed loops and their winding numbers.

Consequently zero harmonic field is usually not allowed for a charged
pair at finite separation. If one minimizes over harmonic sectors, the
permitted shifted lattice of totals must be minimized, not replaced by
a continuous zero. The chosen short-path value (6) tends to zero at fixed
m as L tends to infinity. Other fixed winding numbers do so as well.

On an oriented single face with charges (1,0,-1,0), the exact reference
field (1,1,0,0) has longitudinal part (1/2,1/2,-1/2,-1/2). The remaining
loop coordinate is shifted by one half:
\[
 \|e\|^2=1+4(n+1/2)^2,\quad n\in\mathbb Z.             \tag{7}
\]
This is a simple exact illustration of why dropping the affine shift is
incorrect. This one-face geometry is not the cubic photon model.

## 3. Ground energies are insensitive to the flat connection at weak coupling

At every fixed torus there are constants C_L,b_L,h_L>0 such that
\[
 |\lambda_0(h,\alpha)-\lambda_0(h,\alpha')|
       \le C_L h^3 e^{-b_L/h},\qquad 0<h<h_L,          \tag{8}
\]
for arbitrary constant flat connections alpha,alpha'. Here lambda0
is the ground eigenvalue of P in (5). The constants depend on the
finite configuration torus and potential; no uniform L bound is asserted.

A proof follows, including the needed localization estimate.

First, the zeros Z of V are finite isolated minima. At a zero all
plaquette phases are integer multiples of 2pi and
\(\operatorname{Hess}{\cal V}=2 C^\mathsf T C|_{\cal S}>0\).
The positivity follows from the exact real lattice Hodge decomposition:
a curl-free divergence-free field on a periodic cubic grid is constant.
For example, each nonzero Fourier mode has the usual gradient/curl
decomposition, leaving only the three zero-momentum constant modes,
which have been removed in S. The same positive Hessian at every zero
gives a uniform local isolation radius. Compactness then gives a finite
set Z. A unique minimum is not required for the proof.

The operator P is a positive elliptic operator on a compact torus and
has a normalized smooth ground eigenfunction psi. A smooth Gaussian
trial function of width sqrt(h), supported in one coordinate ball
about a minimum, has Rayleigh quotient at most C_L h. Its local phase
can cancel any alpha exactly. Therefore
\[
 0\le\lambda_0(h,\alpha)\le C_L h                     \tag{9}
\]
with the same constant for every alpha.

Choose delta>0 so the balls of radius 4delta around distinct minima
are disjoint and are valid flat coordinate charts. On the complement
of the delta-balls the potential has a strictly positive minimum v.
Take eta^2<=v/4 and
\[
 \phi(A)=\eta\,\min\{\max(\operatorname{dist}(A,Z)-\delta,0),\delta\}.
\]
It is bounded Lipschitz, zero in the delta-balls, has gradient at most
eta, and equals eta delta outside the 2delta-balls.
Multiplying the eigenvalue equation by the exponential weight and
integrating by parts gives the exact real-part identity
\[
 h^2\|(-i\nabla+\alpha)(e^{\phi/h}\psi)\|^2
 +\int[{\cal V}-\lambda_0-|\nabla\phi|^2]
                 e^{2\phi/h}|\psi|^2=0.              \tag{10}
\]
Lipschitz weights follow by smooth approximation in the quadratic form
domain; for fixed h all weights are bounded. The connection is real and
constant, so the same integration by parts is valid as for zero alpha.

For h small enough that C_L h<=v/4, the integrand coefficient outside
the delta-balls is at least v/2. Inside those balls it is at least
-lambda0, and phi=0. Thus
\[
 \int_{\operatorname{dist}(A,Z)\ge\delta}
       e^{2\phi/h}|\psi|^2\le 2C_L h/v.
\]
In particular
\[
 \int_{\operatorname{dist}(A,Z)\ge2\delta}|\psi|^2
        \le (2C_L h/v)e^{-2\eta\delta/h}.             \tag{11}
\]
This estimate is derived for the actual ground function, not an assumed
Gaussian approximation.

Let chi_j be real smooth cutoffs equal to one in the 2delta-ball about
minimum j and zero outside its 3delta-ball. Their supports are disjoint.
With \(N=\sum_j\|\chi_j\psi\|^2\), equation (11) implies
\(1-N\le C_L h e^{-b_L/h}\).
The eigenvalue equation also gives the exact cutoff identity
\[
 \langle\chi_j\psi,P_{h,\alpha}\chi_j\psi\rangle
 =\lambda_0(h,\alpha)\|\chi_j\psi\|^2
              +h^2\int|\nabla\chi_j|^2|\psi|^2.       \tag{12}
\]
The derivative supports lie outside the 2delta-balls. In each chart
multiply chi_j psi by
\(\exp(i(\alpha-\alpha')\cdot(A-A_j))\).
This changes the connection from alpha to alpha' without changing
the local quadratic form. Extension by zero is smooth and periodic.
The resulting pieces have disjoint supports, so their sum has norm
squared N and target quadratic form
\(\lambda_0(h,\alpha)N+O_L(h^3e^{-b_L/h})\).
Rayleigh-Ritz and N>=1/2 give the upper bound (8). Interchange alpha and
alpha' to obtain the absolute bound. All constants were independent of
the chosen connection.

This proof is the usual weighted localization and local gauge removal
argument in a finite-dimensional configuration space. It proves only
the displayed fixed-box statement. It does not bound thermodynamic
tunneling, monopole proliferation, or a massless phase.

## 4. Static source energy and the lattice Coulomb coefficient

Combining (5) and (8), with the neutral zero-winding ground as reference,
gives the actual ground-energy difference
\[
 {\cal E}_0(\rho,E_{\mathrm H};g)-{\cal E}_0(0,0;g)
 =\frac{cg^2}{2a}
       \left(\rho^\mathsf T L_0^+\rho+\|E_{\mathrm H}\|^2\right)
       +O_L\!\left(\frac ca g^4 e^{-b_L/g^2}\right).  \tag{13}
\]
This uses the exactly quadratic electric term of the Hamiltonian (4).
It is not an assertion about every Euclidean lattice action with the
same continuum expansion or about a renormalized finite-coupling force.

For opposite charges at zero and m,
\[
 \rho^\mathsf T L_0^+\rho
 =2Q^2[G_L(0)-G_L(m)],\qquad
 G_L(m)=\frac1V\sum_{k\ne0}
 \frac{e^{ik\cdot m}}{4\sum_{j=1}^3\sin^2(k_j/2)}.     \tag{14}
\]
The zero mode is omitted. The source-neutrality premise is essential.
Taking g->0 in the normalized energy difference (13), at fixed L and a,
then L->infinity at fixed m, gives the infinite-lattice coefficient
with the harmonic contribution gone:
\[
 \lim_{L\to\infty}\lim_{g\to0}
 \frac{2a[{\cal E}_0(\rho,E_{\mathrm H};g)-{\cal E}_0(0,0;g)]}{cg^2}
 =2Q^2[G_\infty(0)-G_\infty(m)].                      \tag{15}
\]
For the chosen bounded winding sectors, (6) vanishes in this order.
The Fourier integral for G-infinity exists because 1/|k|^2 is locally
integrable in three dimensions. The finite sums converge: the
contribution of modes |k|<eta is uniformly O(eta) by lattice-shell
counting, and away from zero ordinary Riemann convergence applies.

After subtracting the separation-independent self-energy coefficient,
the interaction coefficient is
\[
 U_{\mathrm{lead}}(m)
 =-\frac{cg^2Q^2}{a}G_\infty(m).                      \tag{16}
\]
This is the standard lattice Coulomb kernel. For context, the tree
kernel in [Cella et al., equations 7-9](https://arxiv.org/pdf/hep-lat/9704012)
has the same spatial Fourier denominator. Their Euclidean Wilson-loop
calculation and higher-order corrections are not imported as results
for (4).

## 5. Long-distance form, with the order of limits retained

For large nonzero integer m,
\[
 G_\infty(m)=\frac1{4\pi|m|}+O(|m|^{-3}).              \tag{17}
\]
One direct Fourier proof is as follows. Choose a smooth cutoff chi
supported near k=0 and equal to one in a smaller ball. Write
\[
 \frac1{\lambda(k)}
 =\frac{\chi(k)}{|k|^2}
 +\chi(k)\left[\frac1{\lambda(k)}-\frac1{|k|^2}\right]
 +\frac{1-\chi(k)}{\lambda(k)},\quad
 \lambda(k)=4\sum_j\sin^2(k_j/2).
\]
The last term is smooth on the periodic Brillouin zone, so its Fourier
coefficients decay faster than any power. Since lambda=|k|^2+O(|k|^4),
the middle term is a bounded symbol whose derivative of order r
is O(|k|^-r). On a dyadic shell of radius s, its Fourier coefficient
is bounded by
\(C_N s^3(1+|m|s)^{-N}\).
Summing the shells with N>3 gives O(|m|^-3), uniformly in direction.
The first term is the continuum inverse-Laplacian kernel 1/(4pi|m|)
plus a rapidly decaying term: the complementary whole-space symbol
(1-chi)/|k|^2 is smooth, and derivatives of any order greater than one
are integrable at infinity, so repeated integration by parts in its
oscillatory Fourier integral gives that remainder. A decaying regulator
justifies the integrations before removing it. This proves (17).

With physical separation R=a|m|, (16)-(17) give
\[
 U_{\mathrm{lead}}(R)
 =-\frac{cg^2Q^2}{4\pi R}
         +O(cg^2Q^2a^2/R^3).                         \tag{18}
\]
This is a statement about the weak-coupling coefficient after the
fixed-box weak-coupling limit, not a simultaneous limit of the original
microscopic dynamics. At strictly g=0 the unnormalized interaction
vanishes. The meaningful claim is the g^2 coefficient and its
continuum shape; c and g are supplied parameters, not predicted constants.

## 6. Relation to permanent mobile records and open obligations

In the campaign Gauss law div E+1_A-q=0, moving a plus record from A to
B produces a negative relative charge at the vacated A site and a
positive one at B. This makes static-source electrostatics a relevant
target diagnostic. It does not put that excited microscopic sector
under the proved neutral-field theorem. Such defects have their own
fast motion and altered virtual paths.

To obtain a force law for actual permanent moving records, one still
needs a controlled charged-sector dynamics, a definition and scale of
record inertia/rest energy, and a matching of static or slowly moving
sources to (4). Alternatively, changing the supplied Gauss background
can define externally imposed static sources, but that changes the model
premise and is not a derivation of a record's physical charge. A
separation-independent number-energy shift cannot by itself change the
static interaction between configurations with the same record count;
it also cannot supply the missing charged-sector matching.

The exponential constants in (13) may deteriorate with volume. This
argument therefore does not resolve the fixed-coupling phase or allow
g, a, L, spin cutoff and observation time to be interchanged freely.
The field/charge roles, Hamiltonian time, couplings, link Hilbert spaces
and state selection remain supplied. There is no new fundamental-force
or TOE claim here.

## 7. Checks and provenance

The companion static_source_coulomb_check.py contains three distinct
controls assembled without importing the prior physics runners:

* Four cubic Poisson/decomposition examples with L=6,6,8,12 and
  separations 1,2,3,4. Divergence residuals are at most 2.3e-16, the
  longitudinal Green identity and all orthogonal norms agree, and the
  nonzero allowed harmonic term is kept.
* Exact rational one-face affine decomposition (7), plus a compact
  pendulum with connection 0,1/4,1/2. Its half-twist ground-energy
  difference drops from about 0.02379 at g=1.2 to 3.225e-9 at g=0.6.
  Cutoffs 32 and 48 agree within 1.2e-13. These are numerical controls
  on localization, not the proof of (8).
* Independent Bessel-integral quadrature of the infinite-lattice Green
  kernel along an axis. It gives G(0)=0.252731009858663 and verifies
  6[G(0)-G(e1)]=1 within 2.3e-16. At distance 64,
  4pi|m|G(m)=1.00006107807. Error estimates from quadrature are not
  rigorous interval bounds; the analytic Fourier proof establishes
  (17).

The runner's first scientific execution passed with empty stderr;
all result fields were read. Full stdout, receipts and source hashes
are preserved. This author packet remains pending independent check.
