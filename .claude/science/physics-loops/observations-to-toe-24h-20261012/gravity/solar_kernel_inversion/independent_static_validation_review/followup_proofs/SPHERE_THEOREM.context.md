# Full-sphere classification of the fixed conditioned pair law

This is a post-exposure mathematical classification of the already declared
family. No parameter, observation map, source fit or empirical prediction is
changed. The earlier `composition/` packet remains frozen. The argument below
is offered for independent mathematical review; it has not been formally
verified in a proof assistant.

## Statement

For k≥0 define

\[
 f_k(c)=\tanh\left[\operatorname{atanh}\left(\frac2\pi\arcsin c\right)+kc\right],
 \quad -1<c<1,\qquad f_k(\pm1)=\pm1,
\]
\[
 a_\ell(k)=\frac{2\ell+1}{2}\int_{-1}^1f_k(c)P_\ell(c)\,dc.
\]

Let k₃ be the unique nonnegative root of a₃(k)=0. Then

\[
 \boxed{f_k(a\cdot b)\text{ is a PSD isotropic kernel on }S^2
 \quad\Longleftrightarrow\quad 0\le k\le k_3.}
\]

Exact-rational integration certificates give
0.3183<k₃<0.3184. An independent high-precision numerical location is
k₃≈0.31833135954123448054. The many displayed numerical digits are not a
certificate of a correspondingly narrow root interval.

Equivalently, in precisely this parameter interval, the entire fair-marginal
pair law E(a,b)=−f_k(a·b) has one common projective bipartite tensor-Hilbert
realization, allowing countably infinite local dimension. Necessity follows
from exact anticorrelation; sufficiency is constructed below. This is an
abstract operator realization. It does not identify finite-dimensional spin
observables, a finite-energy laboratory source, or microscopic dynamics for
the setting-conditioned reference measure.

The load-bearing new part is an all-order coefficient bound: for
0≤k≤8/25 every odd Taylor coefficient of degree at least five is strictly
positive. A finite coefficient scan would not establish this statement.

## 1. Analytic domain, poles, and absence of other singularities

Use the principal analytic arcsine on
\(D=\mathbb C\setminus(({-\infty},-1]\cup[1,\infty))\), and write

\[
 u(z)=\frac2\pi\arcsin z,\qquad H_k(z)=\operatorname{atanh}u(z)+kz.
\]

Arcsine maps D into the strip |Re w|<π/2. Since
Re(sin(x+iy))=sin x cosh y, Re(arcsin z) and Re z have the same sign.
Consequently |Re u|<1, so the principal atanh is analytic on u(D), and

\[
 \operatorname{Re}\operatorname{atanh}u
 =\tfrac12\log\frac{|1+u|}{|1-u|}
\]

has the sign of Re u. Thus Re H_k(z) has the sign of Re z. For k>0,
|Re H_k(z)|≥k|Re z|. The poles of tanh occur only at purely imaginary
arguments, so every finite pole of f_k in D must lie on the imaginary axis.
This excludes off-axis poles analytically, without a root scan.

For y>0 put

\[
 a(y)=\frac2\pi\operatorname{asinh}y,\quad
 v(y)=\arctan a(y),\quad
 d(y)=v'(y)=\frac{2/\pi}{\sqrt{1+y^2}(1+a(y)^2)}>0.
\]

Then H_k(iy)=i[v(y)+ky]. For each m=0,1,… there is one positive solution

\[
 v(y_m)+ky_m=\pi(m+1/2).
\]

It is simple because H_k′(iy_m)=k+d(y_m)>0. The two poles ±iy_m have
the same positive residue

\[
 r_m=\frac1{k+d(y_m)}<\frac1k.
\]

For m≥1, y_m>πm/k, because 0<v(y)<π/2. At k=0, f₀=u exactly and there
are no finite poles. Apparent poles of tanh(kz) in the alternative addition
formula do not create extra singularities: the analytic expression is

\[
 f_k(z)=\frac{u(z)\cosh(kz)+\sinh(kz)}{\cosh(kz)+u(z)\sinh(kz)}.
\]

The branch endpoints ±1 have finite one-sided limits ±1 and square-root
local behavior; their small contour contributions therefore vanish.

## 2. Contour closure and a cut-plus-poles coefficient formula

For k>0 choose radii R_N→∞ satisfying v(R_N)+kR_N=Nπ. These pass through
imaginary-axis zeroes of f_k, between its poles. On the outer circle where
|Re z|≥δ, with δ=min(1,1/(4k)),
|tanh H_k(z)|≤coth(kδ). On the remaining arcs near ±iR_N,

\[
 H_k'(z)=k+O\!\left(\frac1{R_N(\log R_N)^2}\right)
\]

uniformly in a fixed-width tube around the imaginary axis. This follows
from u′(z)=O(1/R_N), u(z)=±i(2/π)asinh R_N+O(1/R_N), and hence
|1−u(z)²| of order (log R_N)². A segment from ±iR_N to an arc point
has horizontal length at most δ and imaginary displacement O(1/R_N).
Therefore H_k(z) differs from ±iNπ by at most kδ+o(1)≤1/4+o(1).
Tanh is bounded on these fixed disks, which stay away from its poles.
Thus f_k is uniformly bounded along this outer-circle sequence for each
fixed k>0, including lateral limits at the real cuts.

For the Taylor coefficient of degree 2n+1, the outer integral of
f_k(z)/z^{2n+2} is consequently O(R_N^{−2n−1}) and vanishes, including
n=0. Small endpoint circles vanish as described above. This justifies the
keyhole-contour closure rather than assuming the contribution at infinity
is absent. At k=0 the known arcsine function grows only logarithmically and
its corresponding closure also vanishes.

On the upper bank of the positive cut, x>1,
u(x+i0)=1+i(2/π)acosh x. The imaginary part of the Möbius addition formula is

\[
 \rho_k(x)=\operatorname{Im}f_k(x+i0)
 =\frac{(2/\pi)\operatorname{acosh}x\ e^{-2kx}}
 {1+(\operatorname{acosh}x/\pi)^2(1-e^{-2kx})^2}>0.
\]

Write f_k(z)=Σ_{n≥0}β_n(k)z^{2n+1} near zero. The two real cuts and the
imaginary pole residues give

\[
 \boxed{\beta_n(k)=C_n(k)+(-1)^nP_n(k),}
\]
\[
 C_n(k)=\frac2\pi\int_1^\infty\frac{\rho_k(x)}{x^{2n+2}}\,dx>0,
 \qquad
 P_n(k)=2\sum_{m=0}^\infty\frac{r_m}{y_m^{2n+2}}>0.
\]

The sign can be checked directly: the pair of pole residues of
f_k(z)/z^{2n+2} is 2r_m(−1)^{n+1}/y_m^{2n+2}, which is subtracted
when expressing the origin coefficient through the real-cut integral.
For k=0, P_n=0 and C_n is the positive arcsine coefficient.

Every integral and sum here is absolutely convergent. Near x=1, ρ_k is
O(√(x−1)); for k>0 its large-x growth is bounded by a logarithm times
e^{−2kx}. At k=0, a logarithm times x^{−2n−2} is integrable. For the pole
series, r_m<1/k and y_m>πm/k for m≥1 give a convergent p-series with
p=2n+2≥2. No cancellation is needed to define C_n or P_n.

As an independent numerical check of the sign and normalization, the
script reconstructs Taylor degrees 3,5,7 at k=.1 and .32 using the real-cut
integral and the first 40 poles. In every case the difference from a
separate Riccati-series recurrence lies inside an explicit bound on the
remaining pole sum. This check supports the contour algebra but is not
the proof of pole completeness or contour closure.

## 3. Uniform comparison in k

The cut density decreases with k: its numerator decreases and its
denominator increases. Hence C_n(k)≥C_n(K) when k≤K.

The pole moments of order p≥4 increase with k. Implicit differentiation gives
y_m′=−y_m r_m and

\[
 \frac d{dk}\log\left(r_my_m^{-p}\right)
 =r_m\left[p-1+\frac{y_md'(y_m)}{k+d(y_m)}\right].
\]

Since

\[
 \frac{yd'(y)}{d(y)}
 =-\frac{y^2}{1+y^2}-\frac{2a(y)y a'(y)}{1+a(y)^2}
 >-1-\frac2\pi,
\]

the bracket exceeds p−2−2/π>0 for p≥4. The last inequality uses
2a/(1+a²)≤1 and ya′<2/π. Thus each positive term of P_n(k) increases
for n≥1. Comparing terms and then summing proves P_n(k)≤P_n(K), without
interchanging an unbounded derivative and an infinite sum. The series at
K supplies a uniform summable majorant for these n.

Fix the declared rational constants

\[
 K=8/25,\qquad R=3/2,\qquad Y=12/5.
\]

At y=Y, asinh(12/5)=ln5. The inequality
atan((2/π)ln5)+96/125<π/2 implies y₀(K)>Y. The certificate establishes it
using elementary rational bounds: ln5<1.61, π>3.1415,
(2/π)ln5<41/40<tan(4/5), and 4/5+96/125<π/2. It does not substitute
a fitted pole location. Since y_m decreases with k, all poles for 0<k≤K
have y_m>Y.

For P₃ at K, r_m<1/K, y₀>Y, and y_m>3m/K for m≥1 yield

\[
 P_3(K)<\frac2K\left[\left(\frac5{12}\right)^8
 +2\left(\frac K3\right)^8\right]
 =:\overline P_3
 =0.00567814012713821988\ldots<\frac3{500}.
\]

Here Σ_{m≥1}m^{−8}<2 is an elementary integral bound. The final comparison
is performed with exact rational numbers.

For the restricted positive-cut moment,

\[
 C_3^{[1,R]}(K)=\frac4{\pi^2}\int_1^{3/2}
 \frac{\operatorname{acosh}x\ e^{-2Kx}}
 {1+(\operatorname{acosh}x/\pi)^2(1-e^{-2Kx})^2}\frac{dx}{x^8}.
\]

On this interval, 4/π²>2/5, e^{−2Kx}>1/3, and the denominator is less
than 10/9. These follow from π²<10, 2Kx≤24/25<1, e<3,
acosh(3/2)<1 and π>3. Thus

\[
 C_3^{[1,R]}(K)>\frac3{25}I,\qquad
 I=\int_1^{3/2}\frac{\operatorname{acosh}x}{x^8}\,dx.
\]

Since acosh x≥2√(2/5)√(x−1) on [1,3/2], partitioning that interval into
32 equal panels and using each panel's upper x in x⁻⁸ gives the lower bound

\[
 I\ge\frac{4\sqrt{2/5}}{3\cdot512}
 \sum_{j=0}^{31}\left[(j+1)^{3/2}-j^{3/2}\right]
 \left(\frac{64}{65+j}\right)^8.
\]

Integer-square-root bounds, directed according to each term's sign, give a
rational lower bound 0.052185846797466…>1/20. Consequently

\[
 C_3^{[1,R]}(K)>3/500>\overline P_3>P_3(K).
\]

The constants were chosen during exposed proof development and then
recorded before the certificate run. They are analytical bounding constants,
not physical parameters or fitted angular freedom.

## 4. All-order positivity and a controlled coefficient tail

For every n≥3 and 0<k≤K, positivity of the measures gives

\[
 C_n(k)\ge C_n^{[1,R]}(k)
 \ge R^{-2(n-3)}C_3^{[1,R]}(K),
\]
\[
 P_n(k)\le Y^{-2(n-3)}P_3(k)
 \le Y^{-2(n-3)}P_3(K).
\]

Because R<Y and the n=3 cut bound strictly exceeds the pole bound,
C_n>P_n for every n≥3. Therefore β_n>0 for every n≥3, irrespective of
the alternating pole sign. Also β₂=C₂+P₂>0. The k=0 arcsine coefficients
are positive directly. Hence every Taylor coefficient of degree ≥5 is
strictly positive throughout 0≤k≤K. Only β₁, the cubic coefficient, may
be negative.

There is an explicit summable majorant. Define q=(5/12)²=25/144. Since
ρ_k≤ρ₀, for n≥3,

\[
 0<\beta_n(k)\le
 u_n+\overline P_3q^{n-3},\qquad
 u_n=\frac2\pi\frac{\binom{2n}{n}}{4^n(2n+1)}.
\]

The central-binomial bound \(\binom{2n}{n}/4^n\le1/\sqrt{n+1}\) follows
by induction from the ratio (2n+1)/(2n+2). Thus, for N≥3,

\[
 \boxed{\sum_{n>N}\beta_n(k)
 \le\frac2{\pi\sqrt N}
 +\frac{\overline P_3q^{N-2}}{1-q}.}
\]

This is a conservative uniform tail bound, not an asymptotic fit. The two
low-order coefficients are finite, so the full Taylor series converges
absolutely and uniformly on [−1,1]. Its sum equals the continuous f_k
there, and Σβ_n=f_k(1)=1. This establishes the interchange and boundary
normalization needed below.

## 5. Transfer to all Legendre coefficients and the unique threshold

The Legendre expansion of every integer monomial has nonnegative
coefficients:

\[
 c^m=\sum_{\substack{0\le\ell\le m\\m-\ell\text{ even}}}
 d_{m\ell}P_\ell(c),\qquad
 d_{m\ell}=\frac{(2\ell+1)m!}{(m-\ell)!!(m+\ell+1)!!}>0.
\]

Rodrigues' formula and ℓ integrations by parts establish this expression;
the remaining integrand is c^{m−ℓ}(1−c²)^ℓ≥0. Evaluating at c=1 gives
Σ_ℓd_{mℓ}=1. Absolute summability above permits exchanging the Taylor and
Legendre sums. All odd a_ℓ with ℓ≥5 are therefore strictly positive for
0≤k≤K: every term contributing to them has degree at least five and
positive β_n. Even a_ℓ vanish by oddness. Further,
a₁=3∫₀¹c f_k(c)dc>0. Thus only a₃ can fail in this interval.

The inherited monotonicity argument is repeated here to make the result
self-contained. Put r(c)=cP₃(c). It has zero integral on [0,1], is negative
below c*=√(3/5), and positive above it. The function w(c)=1−f_k(c)² is
strictly decreasing, so

\[
 a_3'(k)=7\int_0^1r(c)[w(c)-w(c_*)]dc<0.
\]

Differentiation under the integral is justified by the bounded derivative
c(1−f_k²). Integration by parts gives a₃(0)=7/64; dominated convergence
gives lim_{k→∞}a₃(k)=−7/8. Hence a₃ has exactly one zero.

The exact-arithmetic certificate in the next section proves a₃(K)<0,
so that zero lies below K. For k≤k₃, all Legendre coefficients are
nonnegative, absolutely summable, and sum to one. The standard Schoenberg
criterion, or the harmonic feature construction below, proves PSD.
For k>k₃, a₃<0, which violates the necessary Schoenberg condition,
including all k>K. Therefore the stated classification covers every k≥0,
not merely the interval used for the positive-tail bound.

The theorem is specific to S². As an optional dimensional check, the
all-sphere Schoenberg power-series criterion gives a smaller interval
for PSD on every sphere simultaneously. Here the first possible negative
Taylor coefficient is

\[
 \beta_1=\frac{1/\pi+8/\pi^3-(2/\pi+k)^3}{3},
\]

so that simultaneous all-sphere threshold is
\((1/\pi+8/\pi^3)^{1/3}-2/\pi\approx0.1955688490612622\).
The higher-coefficient proof covers this smaller interval as well. This
dimension-dependent corollary changes no physical direction space in the
declared S² model.

### An explicit finite witness for every excluded parameter

The negative a₃ condition can be converted into a deterministic finite
construction, even where the earlier triangle or tetrahedron does not
detect failure. Let μ be normalized area measure, let
Y(a)=√7 P₃(a_z), and let L_k=2/π+k. Harmonic projection gives

\[
 \int\!\int Y(a)f_k(a\cdot b)Y(b)\,d\mu(a)d\mu(b)=a_3(k)/7.
\]

The full-angle function f_k(cos θ) is L_k-Lipschitz; this follows from
|g′|≤2/π+k on the half-circle and its odd reflection. Also |Y|≤√7 and
the geodesic Lipschitz constant of Y is at most 6√7. Replacing each of a,b
by a representative within geodesic distance δ therefore changes the
integrand by at most 14(6+L_k)δ.

For an integer N, partition polar angle into N equal intervals and
azimuth into N equal intervals. Choose the N² explicit directions

\[
 \theta_i=(i+1/2)\pi/N,\quad \phi_j=2\pi(j+1/2)/N,
 \quad a_{ij}=(\sin\theta_i\cos\phi_j,\sin\theta_i\sin\phi_j,\cos\theta_i).
\]

Their cell masses are
\(\mu_{ij}=[\cos(i\pi/N)-\cos((i+1)\pi/N)]/(2N)\), and their center
distance bound is δ≤3π/(2N). Set w_{ij}=μ_{ij}Y(a_{ij}). Then

\[
 \left|w^TGw-a_3(k)/7\right|
 \le\frac{21\pi(6+L_k)}N,\qquad G_{ij,pq}=f_k(a_{ij}\cdot a_{pq}).
\]

For any certified d>0 with a₃(k)≤−d, choose
N>147π(6+L_k)/d. The finite quadratic form is strictly negative.
Every associated binary probability remains explicitly
p(A,B|ij,pq)=[1−AB G_{ij,pq}]/4. Thus the excluded interval has a
constructive finite witness with an error bound, rather than only an
existence assertion from a negative integral coefficient. The grid bound
is very conservative and may require an impractically large finite set;
the compact triangle remains the useful prospective witness where it
already detects the candidate.

## 6. Exact-rational integration certificates

The certificate avoids relying on black-box transcendental interval
arithmetic. It uses Python integers and `Fraction`, directed fixed-point
interval arithmetic with scale 10⁴⁰, and explicit elementary remainders.
The method is reproducible, though the code and Python runtime are not
formally verified.

First, a rational π enclosure follows from Machin's identity
π=16 atan(1/5)−4 atan(1/239), with 50 and 12 alternating-series terms and
their first omitted terms. The tangent-addition identity verifies the
angle relation and selects the branch in (0,π/2).
The bound ln5<1.61 follows from the first 13 positive terms of exp(1.61),
whose rational sum exceeds 5. The lower bound tan(.8)>41/40 uses an
alternating sine lower polynomial through degree seven and a cosine upper
polynomial through degree four. Integer square roots bound the algebraic
32-panel sum. All final inequalities in the cut/pole comparison are exact
rational comparisons.

For a₃ put θ=acos c, a=2/π, u=1−aθ, q=e^{2k cos θ},
D=(1+u)q+(1−u), and g=1−2aθ/D. On 0≤θ≤π/2 and 0≤k≤K,
q<2, D≥2, |D′|<4, |D″|<6, |g′|≤a+k<1 and |g″|<14.
For example, |q′|<32/25 and |q″|<1312/625 imply the stated D bounds;
direct differentiation of g then gives |g″|<14. The q<2 bound is itself
checked by an elementary exponential-series upper bound at 16/25.

For H(θ)=P₃(cos θ)sin θ, |H|≤1, |H′|≤7 and |H″|≤25, using
|P₃′|≤6 and |P₃″|≤15. Therefore for F=gH,

\[
 |F''|\le14+2\cdot7+25=53.
\]

The N-panel midpoint estimate of a₃=7∫₀^{π/2}F has error at most
\(7\cdot53(\pi/2)^3/(24N^2)\), bounded rationally using π/2<11/7.
At each midpoint, u=1−(2j+1)/(2N) is exactly rational. Sine and cosine
are enclosed by their degree 25 and 24 Taylor polynomials with absolute
remainders 2²⁷/27! and 2²⁶/26!. Exponentials of arguments in [0,1) use
degree 24 with positive remainder bounded by 3/25!, because e<3.
Every interval operation rounds outward using integer arithmetic.

The resulting proved arithmetic enclosures are

| k | Panels | Enclosure for a₃(k) |
|---:|---:|---:|
| 0.32 | 1024 | [−0.000644575910, −0.000530162563] |
| 0.3183 | 4096 | [0.000007518686, 0.000014669522] |
| 0.3184 | 4096 | [−0.000027721705, −0.000020570870] |

Displayed endpoints are expanded outward; exact rational endpoints are
preserved in `CERTIFICATE_RESULTS.json`. The first row closes the theorem
by placing k₃ below K, and the next two give the declared rigorous bracket.
Separate 80-digit integration locates the root more precisely for reference.

## 7. A common operator realization of the whole admissible family

For k≤k₃, choose real orthonormal spherical harmonics Y_{ℓm}. The standard
addition theorem supplies the unit feature vector

\[
 w_\ell(a)_m=\sqrt{\frac{4\pi}{2\ell+1}}Y_{\ell m}(a),\qquad
 w_\ell(a)\cdot w_\ell(b)=P_\ell(a\cdot b).
\]

The direct-sum feature v(a)=⊕_ℓ√a_ℓ w_ℓ(a) is a unit vector and has
inner product f_k(a·b). This already constructs the abstract Gram kernel.
The following gives actual bipartite binary operators and one normalized
state, rather than assuming that a Gram condition suffices for a fixed
physical system.

For each nonzero odd harmonic weight a_ℓ, take 2ℓ+1 Hermitian Clifford
matrices Γ_{ℓm} of size D_ℓ=2^ℓ, satisfying
{Γ_{ℓm},Γ_{ℓn}}=2δ_{mn}I and Tr Γ_{ℓm}=0. Finite Pauli tensor products
give these explicitly. Define

\[
 A_\ell(a)=w_\ell(a)\cdot\Gamma_\ell,\qquad
 B_\ell(b)=-[w_\ell(b)\cdot\Gamma_\ell]^T.
\]

Their squares are I and on the maximally entangled vector |Φ_{Dℓ}⟩ they
have zero marginals and correlation −P_ℓ(a·b). On the countable local
direct sums H_A=⊕_ℓ C^{Dℓ}, H_B=⊕_ℓ C^{Dℓ}, set

\[
 |\Psi_k\rangle=\sum_\ell\sqrt{a_\ell(k)}\,|\Phi_{D_\ell}\rangle,
 \qquad A(a)=\bigoplus_\ell A_\ell(a),\quad B(b)=\bigoplus_\ell B_\ell(b).
\]

The state occupies matching sectors on the two parties and has norm one
because Σa_ℓ=1. Both block-diagonal observables are bounded Hermitian
involutions. They act on different tensor factors and commute. Orthogonality
of the sectors gives, for every a,b simultaneously,

\[
 \langle A(a)\otimes B(b)\rangle_{\Psi_k}
 =-\sum_\ell a_\ell P_\ell(a\cdot b)=-f_k(a\cdot b),
\]

with fair marginals. Thus p(A,B|a,b)=[1−AB f_k(a·b)]/4 is realized as a
joint Born probability with no setting-dependent state or operator retuning.
The proof accommodates a₃=0 at the endpoint simply by omitting that sector.

There are infinitely many positive harmonics, so an exact finite-dimensional
common Hilbert realization is impossible: any finite-dimensional common
state/operator model would give a finite-rank correlation-vector Gram
kernel, whereas each positive a_ℓ contributes 2ℓ+1 independent harmonic
features. The provided realization is therefore deliberately of infinite
local dimension. Normalizability is established; an energy Hamiltonian or
finite resource requirement is not supplied by this construction.

Finite approximations are controlled. For L=2N+1, N≥3, let
r_L=Σ_{ℓ>L}a_ℓ. Positive monomial-to-Legendre coefficients imply

\[
 r_L\le\sum_{n>N}\beta_n
 \le\frac2{\pi\sqrt N}+\frac{\overline P_3q^{N-2}}{1-q}.
\]

Move this residual weight to the ℓ=1 sector. The resulting finite harmonic
kernel is PSD, normalized at c=1, and differs from f_k by at most 2r_L
uniformly in c. It has the finite Clifford block construction above. This
is a certified truncation of fixed positive weights, not a new angular fit
parameter or an asserted economical laboratory implementation.

## 8. Imported facts, checks and scope

The standard Schoenberg criterion, Legendre addition theorem and finite
Clifford realization are not novelty claims. The pinned accessible sources
are Berg–Porcu arXiv:1505.05682v2, Theorem 2.1 and its harmonic preliminaries,
and Cirel'son/Tsirelson (1980), Theorem 1. They were already read in the
preceding packet; `SOURCE_MANIFEST.json` pins those exact bytes again.
The cut/pole decomposition, uniform tail bound, parameter threshold and
operator assembly above are the present candidate-specific derivation.

Frozen numerical scans through Taylor degree 101 and Legendre degree 101
agree with the theorem; they supply independent recurrence/quadrature
checks. Their highest numerical coefficients are not used to infer the
unsampled tail. Complete scans, exact rational certificates, source hashes,
and execution logs are retained. The argument's analytic assumptions,
contour closure, summability, and construction remain visible for review.

The theorem classifies the unattenuated one-k family. The earlier visibility
results remain a separate finite-table calculation. This completion changes
neither those frozen predictions nor the parent source-fit limitations.
