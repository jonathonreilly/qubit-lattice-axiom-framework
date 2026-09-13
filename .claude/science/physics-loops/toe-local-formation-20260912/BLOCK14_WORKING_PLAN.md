# Infrared spectral dominance of a quasi-local odd transition

2026-09-13 around07:27UTC. Personal derivation-first campaign, no agents.
This is a new target after the positive Ward scalar milestone. It is not an
interacting-phase claim. First prove a general CAR/locality spectral theorem,
then make the native-star application with its exact provisional dependencies.

The new idea is a factorial-moment estimate, not a finite-volume spectral fit.
Let H0=dGamma(omega) in the supplied pure Gaussian Fock representation of the
native pi-flux bath. In a doubled8-site cell, k∈[-pi,pi]^3,
omega(k)=2h sqrt(sum_a sin²(k_a/2)), with4 positive-frequency bands.
The one-particle low-energy measure obeys
nu(E)=sum_band integral_(omega<=E) dk/(2pi)^3 <= pi E³/(12h³).
Indeed omega>=2h|k|/pi. This upper bound is valid for all E, though loose at
large E. For small E, omega<=h|k| supplies the corresponding inner ball.

Let an odd bounded quasi-local operator have a norm-convergent decomposition
Y=sum_n Y_n, each Y_n supported on m_n physical Majoranas, and
sum_n m_n^(3/2)||Y_n||<infinity. A superpolynomially localized creator has
such a decomposition by parity-preserving local conditional expectations.
For a normalized generalized annihilator a(k,b), {a(k,b),gamma_j} has modulus
at most sqrt2 in this Fourier convention. Its graded derivation on a local
algebra equals that of b_S=(1/2)sum_(j∈S){a,gamma_j}gamma_j, with
||b_S||<=sqrt(m). Thus three successive graded derivations have norm at most
8m^(3/2)||Y_n||. Put D3(Y)=8sum m_n^(3/2)||Y_n||.
Vacuum annihilation makes a3 a2 a1 Y Omega equal this triple derivation on
Omega. The localization sum gives a uniform Hilbert-vector bound D3.

For chi=Y Omega, oddness means particle sectors1,3,5,... only. The positive
free energy spectral projector below E in sectors>=3 is dominated by
binom(N_low(E),3). Therefore

||1_(H0<=E) P_(N>=3) chi||²
 <= (1/6) integral_(low³)||a3 a2 a1 chi||²
 <= D3(Y)² nu(E)³/6
 <= [D3(Y)² pi³/(10368h^9)] E^9.

This controls the entire higher-particle tail without separate assumptions
on every particle sector. Local polynomials contain at most m particles;
the same localization sum establishes the necessary N^(3/2) domain before
taking the integrated triple-annihilation limit. Check all normalization and
domain details; a Fock-space number cutoff alone is not an independent proof.

The one-particle coefficient is c_j=omega_vac({gamma_j,Y})/2. With smooth
cell vector c(k), the amplitude is sqrt2 P_+(k)c(k). If c(0)=alpha e_s,
alpha!=0, then P_+(k) has diagonal1/2 in the native cell gauge. Uniformly at
small k, its squared amplitude is alpha²+O(|k|). The exact substitution
y_a=2sin(k_a/2) gives sublevel volume
E³/(6pi²h³)+O(E^5). Hence

mu_1([0,E])=alpha² E³/(6pi²h³)+O(E^4),
mu_>=3([0,E])=O(E^9),
mu_>=3/mu_1=O(E^6).

An explicit coarse lower bound follows by choosing the smooth coefficient
remainder <=|alpha|/(2sqrt2): mu_1([0,E])>=alpha² E³/(24pi²h³).
Laplace integration then gives
<chi,e^(-tau H0)chi> ~ alpha²/(pi²h³ tau³),
while the full higher-particle contribution is bounded by9! K tau^-9.
This is a free-reference response/scaling statement, not an interacting
renormalization theorem or a physical clock identification.

The exponent9 should be sharp in this native model: Wick-order a product of
three distinct same-cell Majoranas chosen from three different Γ_z pairs,
for example internal labels0,2,4 with Γ_z=Z1 Z2 X3. Along the positive z ray,
their projected columns are independent (Gram=I/2). A small angular cap
therefore supplies a nonzero three-particle exterior product; integrating
three energies with sum<=E yields a positive E^9 contribution. Derive this
carefully with measurable band frames, rather than inferring it from a sample.
This is optional sharpness, not needed for the upper bound.

Native application: the earlier infinite-star source64c1efc6984b16cf95c61e7ac148add85d741606
was reread fully now. It defines chi_v=(1/8)sum_disjoint R_C gamma_v R_A Omega,
provides a rapidly quasi-local odd creator, and proves C(0)=alpha I8 plus the
bounded soft-resolvent scalar. Re and pair interchange convert its two half
Ward terms to exactly the bounded scalar in PR8086 (head6e0541d4e6717c938c1bef380d0ed90a3438e228),
whose elementary witness proves7<h²alpha<330. State these as separate
provisional source dependencies unless the quasi-local and node bridge are
reconstructed within the new proof unit.

A direct reconstruction is available if useful: choose a smooth inverse
filter f(x)=-1/x for x>=delta, with Fourier transform having every weighted
L1 moment finite. For U_A(t)=exp(it(H0+B_A))exp(-itH0), define the odd creator
by integrating U_C(t) tau_t(gamma_v U_A(s)) against fhat(t)fhat(s).
It acts on Omega as R_C gamma_v R_A Omega. Free finite-range propagation and
bounded local cocycles give superpolynomial localization. The reconstructed
finite energy shifts converge to a strictly larger than h/4 limit, so all
sufficiently large AP tori share a positive resolvent lower bound. The soft
annihilator identity then uses only bounded local commutators and three
inverses. Complementary opposite-ray positive-band projectors extend it to
all cell spinors. No generalized Hermitian zero mode annihilates the vacuum.

Next: write the analytical theorem and proof completely; run small CAR
factorial-moment/normalization and spectrum-density comparators only after
that. Preserve any failed assumption. No agents, new axioms or audit verdicts.
Campaign deadline11:38:24UTC.
