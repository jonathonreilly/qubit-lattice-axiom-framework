# Finite-clock Hamiltonian limits, Fourier aliases and anisotropic phase estimates

Working personal derivation. Supplied clock gauge law; no phase or axiom
conclusion. Prior block3 already derives the fixed-box Villain transfer, and
Pasztor–Pesznyak 2609.07886v2 derives Wilson logarithmic temporal scaling.
Do not claim either as new. The new target is the exact resummation and
uniformity obligation when applying a pure Euclidean phase proof to this law.

## 1. Two positive Euclidean actions, one generator

Fix N>=3, t,K>0, time step delta, and alpha_N=1-cos(2pi/N).
The normalized Wilson single-link temporal kernel is

 Q_W = [sum_(q mod N) exp(-beta_tau[1-cos(2pi q/N)]) X^q]
       /[sum_(q mod N) exp(-beta_tau[1-cos(2pi q/N)])].

Choose beta_tau=alpha_N^-1 log[1/(delta t)]. Terms q=+/-1 have weight
x=delta t. For N>=4, all other nonzero terms have exponent
[1-cos(2pi q/N)]/alpha_N>=2; for N=3 there are no others. Thus, at fixed N,
Q_W=I-delta t(2-X-X†)+O(delta²). The spatial multiplier
exp[-delta K(1-cos phi)] gives beta_s=delta K exactly. Every transfer
eigenvalue is positive because the sampled Wilson kernel has positive
Fourier coefficients (sums of positive modified-Bessel coefficients).
At N=2 the one nontrivial jump is its own inverse: use x=2delta t to obtain
the same displayed t(2-X-X†) generator. This edge case must not be silently
counted twice in the probability normalization.

For the Villain regulator, prior block3 gives the same generator with

 beta_tau=N²/(2pi²) log[1/(delta t)],
 beta_s=1/[2log(2/(delta K))].

Positive symmetric products on any fixed finite spatial complex converge to

 H=sum_links t(2-X-X†)+sum_faces K(1-Re W).

All steps commute with finite-group Gauss projection. Yet beta_tau beta_s
 tends to zero for Wilson and to N²/(4pi²) for Villain. A bare coupling-product
criterion therefore cannot by itself be a physical phase criterion for this
Hamiltonian. This comparison adds no thermodynamic phase theorem to the
fixed-box transfer limit; its purpose is to identify regulator-dependent
quantities before importing an estimate.

## 2. Exact temporal Fourier aliases and a false divergent gap

For Villain let ell=log[1/(delta t)] and beta_tau=N² ell/(2pi²). Its exact
temporal transfer eigenvalue in electric residue k mod N is

 lambda_k = A_k/A_0,
 A_k=sum_(m in Z) exp[-(k+mN)²/(2beta_tau)].

Poisson summation gives the equivalent short-jump expression

 lambda_k = [sum_(r in Z) x^(r²) exp(2pi i rk/N)]/[sum_r x^(r²)],
 x=delta t.

Hence -delta^-1 log lambda_k -> t[2-2cos(2pi k/N)]. The infinite alias sum
is essential in this order of limits. If it is cut to -M<=m<=M with M fixed
and k!=0 fixed, symmetry sum_m m=0 gives

 A_k^M/A_0^M=1-k²/(2beta_tau)+O(beta_tau^-2),
 -delta^-1 log(A_k^M/A_0^M)~pi² k²/(N² delta ell) -> infinity.

This is a spurious divergent electric energy produced by the truncated
representation; the exact finite-clock generator has a finite energy.
The truncation also requires a chosen residue representative and need not
preserve exact residue periodicity. It is not a counterexample to the exact
clock model, nor proof of physical freezing or of an absent Coulomb phase.

## 3. A constructive alias cutoff that controls the generator

Choose representatives |k|<=N/2 and M>=1. Put a=pi²/ell. The discarded
positive alias weight obeys uniformly in k

 R_M <= 2 exp[-a(M+1/2)²]/[1-exp(-a(2M+2))].

For |m|>=M+1, use |m+k/N|>=|m|-1/2; successive squared distances increase
by at least 2M+2. This proves the geometric-series bound. Since A_0^M>=1
and 0<A_k<=A_0, the normalized eigenvalue error is at most 2R_M.
For delta t<=1/8 and 2R_M<=1/4, the short-jump tail obeys R_short<=2x^4/(1-x^5), and
lambda_k>=(1-2x-R_short)/(1+2x+R_short)>=1/2. Thus both exact and
truncated eigenvalues are at least 1/4. The logarithm is 4-Lipschitz there, so the generator error
is at most 8R_M/delta.

For any eta>0, take M=ceil[sqrt(1+eta) ell/pi+1/2]. The denominator in
the bound is bounded away from zero as ell increases, and
R_M=O(exp[-(1+eta)ell]). Therefore the generator error is O(delta^eta),
with fixed t. An O(log(1/delta)) alias cutoff is a sufficient constructive
schedule; no optimality claim is made. The Poisson-dual short-jump series
is a more economical exact representation in this regime.

## 4. Full spatial Villain curvature, not its single Gaussian term

For V_beta(phi)=sum_m exp[-beta(phi+2pi m)²/2], Fourier summation yields

 -[d²/dphi² log V_beta(phi)]_(phi=0)
    = [sum_n n² y^(n²)]/[sum_n y^(n²)],  y=exp[-1/(2beta)].

Along the matched spatial trajectory y=delta K/2, this is
 delta K+O(delta²), in agreement with the Wilson spatial multiplier.
The coefficient beta_s of one unperiodized Gaussian is of order
1/log(1/delta), much larger than delta. Ignoring the other Gaussian images
therefore fails at the level of the matched local source Hessian, before
any phase conclusion. The omitted images cancel the putative bare Gaussian
stiffness to the actual O(delta) coefficient.

## 5. Optimizing the local complex-shift estimate does not make it uniform

Frohlich–Spencer IHES/P/81/40 section3.5, pp61–64, integrates selected links
by a complex translation. For an anisotropic Wilson action, the relevant
coefficient on a link l is B_l=sum_(p incident to l) beta_p. A source charge
q on that link acquires the exact pointwise estimate

 exp[-alpha q+B_l(cosh alpha-1)].

The optimal real alpha is asinh(q/B_l), with suppression exp[-I_B(q)],

 I_B(q)=q asinh(q/B)-sqrt(B²+q²)+B
       =q²/(2B)+O(B^-3) for fixed q and large B.

In 3+1 dimensions B_l=6beta_tau for a time link, and
B_l=2beta_tau+4beta_s for a spatial link. On the fixed-N Wilson Hamiltonian
trajectory every B_l diverges logarithmically, so I_(B_l)(N)->0.
The best factor from this particular pointwise one-link estimate tends
to one. Optimizing the shift cannot restore a delta-independent small
factor for charge N at fixed N.

This loss is not merely a poor optimization: with all surrounding link
phases zero, the conditional one-link distribution is proportional to
exp(B_l cos theta), and its Nth Fourier moment is I_N(B_l)/I_0(B_l)->1.
Thus no uniform conditional bound <c<1 can hold over all backgrounds as
delta decreases. This is a boundary of pointwise local suppression, not a
lower bound on full closed-current activities or a no-go for the phase.
Collective shifts, temporal blocking and source-preserving resummation
are not ruled out. In particular the exact alias resummation above already
shows how finite Hamiltonian dynamics survives this singular local limit.

## 6. Live next attacks

Derive anisotropic cellular duality with explicit global sectors, and test
whether a controlled collective or blocked-time estimate supplies the missing
uniform response. The fixed-box generator, a self-dual coupling relation or
a Gaussian linearization cannot substitute for that estimate. Any spectral
consequence must keep the same physical source, time normalization, ground
ensemble and order of limits. These remaining items are research obligations,
not conclusions already established in this working note.


## 7. Local clock wraps change the physical source test

On a cubic L-torus, L>=3, orient each face in its positive Cartesian
orientation. In electric residues, a plaquette move changes E by +/-boundary p
modulo N. Insert phase exp(+/-i theta) on every positively oriented xy move.
For a closed history let S be its signed integer face count and A=sum_xy S_p.
Closure now says boundary S=0 mod N, not boundary S=0 over the integers.
Summing the x and y edge equations over z shows that
s(x,y)=sum_z S_xy(x,y,z) is constant modulo N. Consequently

 A = L² W mod N,
 A belongs to gcd(N,L²) Z.

Conversely, N successive positive moves on one xy face give A=N and return
the configuration, while one complete xy sheet gives A=L² and returns it.
All clock moves are allowed, so these cycles and their reversals can be
concatenated. The additive group of closed source periods is exactly

 gcd(N,L²) Z.

The trace at positive inverse temperature has a positive history expansion
at theta=0, so its Fourier harmonics cannot cancel. The primitive positive
period of the complete trace family is therefore 2pi/gcd(N,L²). This is a
finite-clock source statement, not a no-go for emergent U(1). The integer
ice identity A=L²W from block9 does not carry over without the no-wrap premise.

If a history has n<N moves, every component of boundary S has absolute value
less than N; modular closure implies integer closure. If additionally
n<L², integer closure gives A=0. Thus no source-dependent trace or ground
energy coefficient occurs below order min(N,L²).

When N<L², the order-N histories with A=+N must be N repetitions of one
positive xy face (and similarly for -N). Indeed all N moves must be positive
xy moves. Integer closure is impossible since 0<A<L². Some edge boundary
is therefore +/-N. All N faces must touch that edge with the same incidence;
there is only one xy face with either fixed incidence at that edge. This
proves the local-cycle classification, without enumerating a large box.

## 8. Positive intensive curvature inside a rigorously gapped regime

Drop the source-independent constant K per face. The clock Hamiltonian is

 H(theta)=sum_l t[2-X_l-X_l†]
          -(K/2)sum_p[exp(i theta a_p)W_p+exp(-i theta a_p)W_p†],
 a_p=1 on xy faces and 0 otherwise.

Its K=0 ground state has every electric residue zero. One repeated face
cycle passes through m=1,...,N-1, with four-link excitation energy

 D_m=4t[2-2cos(2pi m/N)].

The first phase-dependent ground-energy term per xy face is

 -2(K/2)^N cos(N theta)/product_(m=1)^(N-1) D_m.

There is no intermediate return on this cycle. Lower-order subtraction terms
in nondegenerate perturbation theory carry zero source and cannot change its
coefficient. The preceding classification excludes other order-N histories
with nonzero source, when L²>N. The elementary root-of-unity sine product
product_m[2-2cos(2pi m/N)]=N² gives

 chi = (1/L³) partial_theta² E0(theta)|0
     = 2(K/2)^N/(4t)^(N-1)+O(K^(N+1)/t^N)
     = 8t[K/(8t)]^N+O(t(K/t)^(N+1)).

N=2 keeps the two geometric orientations even though W=W†. Its magnetic
term is -K cos(theta)W; the same coefficient is K²/(8t), not zero.

A uniform thermodynamic regime for this expansion follows from Yarotsky,
math-ph/0412040v1, Theorem1 pp2-4 and its convergent local cluster expansion
on p11. The hypothesis mapping is explicit. Group the three positive links
based at x into an onsite Hilbert space C^(N³). The onsite electric Hamiltonian
h_site has a unique product ground state and gap

 Delta=2t[1-cos(2pi/N)]>0.

Take Lambda0={0,e_x,e_y,e_z}, and h_x=(1/4)sum_(s in Lambda0)
h_site(x+s). Then sum_x h_x=H0 and each h_x has a nondegenerate ground state
on its ENTIRE support, with gap at least Delta/4. Rescaling by 4/Delta gives
the paper's unit local-gap hypothesis. Group the three positive face terms
based at x into phi_x. For real theta, ||phi_x||<=3K, and the rescaled bound
is 12K/Delta. Theorem1 therefore supplies a positive, volume-independent
small-coupling interval (no numerical endpoint is claimed) with unique ground
state, uniform spectral gap, thermodynamic local expectations and analyticity.
The complex theta extension is bounded in any fixed strip, so the convergent
cluster expansion is locally uniform in K and theta there. The local energy
density and its derivatives have the thermodynamic limit. At each finite
perturbative order the coefficient stabilizes once the torus is larger than
the participating clusters; the order-N coefficient above thus persists.

Gauge symmetry commutes with H(theta). The unique ground state, continuously
connected to the invariant electric-zero state, stays in the neutral Gauss
sector; restricting to that sector preserves its gap. This establishes a
supplied-model, strong-electric GAPPED regime with strictly positive intensive
uniform-plaquette source curvature for sufficiently small K>0 at fixed N.
It establishes neither confinement nor a Coulomb phase and gives no uniform
interval as N tends to infinity. A positive curvature or a 1/L energy cost
for theta=Phi/L² is therefore not alone a photon-phase diagnostic at finite N:
the same local clock-wrap term produces both scalings in this gapped regime.

## 9. A source-preserving way to remove this local ambiguity (open development)

A flat Z_N two-form source, with face angles 2pi b_p/N and db=0 mod N,
assigns phase one to every local N-fold face wrap and to cube boundaries.
A representative with b_xy=1 at fixed (x,y) in every z layer and zero elsewhere
has one unit of xy flux. Gauge-equivalent representatives differ by a
Z_N link coboundary and are unitarily conjugate. Unlike an arbitrary weak
continuous uniform source at fixed N, this is an exact microscopic twist.
Work still required: derive its finite-volume response and the uniform
large-volume estimate without confusing discrete topological sectors with
a continuous photon stiffness.

## 10. Quantized flux has no local analytic response and a controlled area tail

The continuous-twist diagnostic failure is established prior art for the
ordinary two-dimensional clock SPIN model: Kumano, Hukushima, Tomita and
Oshikawa, arXiv:1301.6166v2, pp1-2 Eqs2-5. Their local order-p character term
survives in the disordered phase, and a quantized seam twist removes it.
The present gauge-Hamiltonian extension changes links to faces, integer loops
to modular surfaces, and high-temperature coefficients to ground-state
resolvent coefficients with an explicitly mapped uniform gap theorem.
No BKT conclusion or numerical phase boundary from that paper is imported.

For the exact flat Z_N source b with one unit of xy flux, restrict first to
L coprime to N. Pick m_L with m_L L²=1 mod N. The translation-invariant
source theta=2pi m_L/N on every xy face is in the same cohomology class as
the single-stack source in section9. Both have zero cube coboundary and one
unit of integrated xy flux modulo N. An explicit link coboundary exists:
put g(x,y)=m_L-delta_(x,0)delta_(y,0), r(y)=sum_x g(x,y),

 lambda_y(x,y)=sum_(u=0)^(x-1)[g(u,y)-r(y)delta_(u,L-1)],
 lambda_x(x,y)=-delta_(x,L-1)sum_(v=0)^(y-1)r(v), lambda_z=0.

All expressions are modulo N and independent of z. The zero total of g
makes them periodic, and d lambda=g. Products of link clock translations
implement this coboundary unitarily and commute with Gauss projection.
Thus using the translation-invariant representative here keeps every
hypothesis of Yarotsky's translation-invariant theorem intact; no unstated
extension to arbitrary inhomogeneous perturbations is needed.

For any modular closed history S, its column sums s(x,y)=sum_z S_xy(x,y,z)
are a common residue W. If its phase in the unit-flux source is nontrivial,
W!=0 mod N. Every one of the L² columns then contains a nonzero face count.
Its number of jumps is at least sum_p |S_p|>=L². Thus all closed histories
of fewer than L² jumps have phase one in this exact quantized source, even
when N-fold local wraps occur. Consequently the twisted and untwisted
nondegenerate ground-energy Taylor series about K=0 agree through order
L²-1. Counterterms are products of lower-order closed histories and obey the
same phase identity. This statement is exact at fixed finite L.

There is also a uniform remainder bound in the small-coupling domain. Fix
a radius R>0 strictly inside the complex-K cluster-expansion disk supplied
by the checked Theorem1 proof. It can be chosen uniformly in L and in the
finite set m=0,...,N-1: the local interaction norm bound is the same for all
these real quantized source angles. The isolated ground-energy branch is
analytic there; its local energy-density expansion is uniformly convergent.
On |K|=R, the finite-volume norm gives

 |E_L(K,b)|/L³ <= 12t+3R,

since there are three links and three positive faces per vertex. This bound
also holds at complex K for the analytic eigenvalue, by the operator norm.
For g_L(K)=[E_L(K,b)-E_L(K,0)]/L³, Cauchy's estimate and the L² zero
Taylor coefficients therefore give, for 0<K<R,

 0 <= E_L(K,b)-E_L(K,0)
    <= L³(24t+6R) (K/R)^(L²)/(1-K/R).

The nonnegative lower bound is the finite-Hamiltonian diamagnetic inequality
in the electric basis. The upper bound is existential in R, with no numerical
radius advertised. It applies on the coprime volume subsequence, and hence
on every odd L for binary clock orders N=2^q. A full all-volume statement
using the inhomogeneous stack would need a separately justified uniform
inhomogeneous perturbation theorem; it is not silently included.

This gives a controlled discriminator: the same gapped regime has positive
intensive curvature for a continuously spread plaquette source, while its
EXACT quantized topological flux cost vanishes at least as a polynomial times
q^(L²), q<1, along the stated sequence. The construction removes a local
clock artifact from a phase test; it does not prove that a positive quantized
flux response elsewhere suffices for a photon, or establish a Coulomb phase.
