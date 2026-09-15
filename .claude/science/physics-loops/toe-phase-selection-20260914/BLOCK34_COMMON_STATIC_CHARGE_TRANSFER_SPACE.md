# Block34: one transfer space for all finite charged insertions

Personal author construction, 2026-09-15; independent review pending.
The input is the same supplied finite-clock law and its free-boundary state.
Block32 supplies inverse moments. Block35 supplies equal visible thresholds
for finite spatial currents with a common divergence at every beta>0. No claim about other
Gibbs representations, dynamical matter or physical-law selection is made.

## 1. The mixed moment kernel exists in the matched free state

Fix a finite integer spatial charge profile rho with total sum0. Let J_rho
be the countable set of finite integer spatial currents j with d0*j=rho.
For each sufficiently large spatial box, let

 v_(L,j)=U_j Omega_(L,0), tau_L=T_L/lambda_(L,0).

For j,k in J_rho and n>=0 define

 C_n(j,k)=lim_L <v_(L,j),tau_L^n v_(L,k)>.              (1)

The temporal-gauge identity makes the finite expression a closed clock
character: insert -j at one endpoint slice, k at the other, and the common
temporal charge lines between them. Signs may be reversed together. The
current is conserved because d0*j=d0*k=rho. At n=0 it is the equal-time
closed spatial character k-j. Thus every limit exists by the same cofinal
free-boundary state argument as the diagonal Wilson moments. The n=0
diagonal is1. Every finite matrix C_n is Hermitian; positivity statements
below come from its finite-volume transfer representation, not merely from
the individual character signs.

This uses exact integer charge representatives. Equivalent Z_N charge
profiles can be represented by adjusting currents by N times a finite
integer flow: any finite integer charge difference of total sum0 is the
divergence of a finite integer flow. Their Fourier multiplication functions
then agree. The construction may consequently be grouped by charges mod N;
no representative-dependent physical charge is introduced.

## 2. A direct matrix-moment Hilbert construction

Start with finite formal sums x=sum_(m,j) a_(m,j) [m,j], m>=0, and put

 <x,y>=sum conjugate(a_(m,j)) b_(n,k) C_(m+n)(j,k).     (2)

This form is positive semidefinite: each finite-volume counterpart equals
the squared norm of sum a_(m,j) tau_L^m v_(L,j), and the finite sum has a
limit. Quotient null vectors and complete to obtain H_rho.

On formal sums define S[m,j]=[m+1,j]. Finite-volume inequalities
0<=tau_L<=I and tau_L^2<=I pass to all finite sums, giving

 0<=<x,Sx><=<x,x>, and ||Sx||<=||x||.

Therefore S respects null vectors and extends to a bounded positive
self-adjoint contraction on H_rho. The vectors e_j=[0,j] and their S
polynomials have dense span by construction. Their spectral measures have
the moments C_n(j,j), so uniqueness of the moment problem on[0,1] identifies
them with the previously constructed path-insertion measures nu_j.

This is a common minimal representation of the actual mixed static
correlation kernel. It is stronger than constructing unrelated one-vector
spaces, but does not by definition construct every local field operator or
all multi-time products of such operators.

## 3. A genuine Hamiltonian on the whole common space

Block32 gives integral lambda^(-1) nu_j(dlambda)<=K(j)<infinity for every
generating e_j. Hence the spectral projection P_{0} of S annihilates every
e_j. It commutes with S, so it annihilates every S polynomial times e_j and
therefore the entire dense span. Thus P_0=0: S is injective.

The spectral functional calculus defines a nonnegative self-adjoint

 H_rho=-log S, S=exp(-H_rho),                           (3)

on a dense domain. Its continuous-time semigroup is strongly continuous.
The e_j have the finite exponential energy moments from Block32. A finite
combination sum c_j e_j obeys

 ||S^(-1/2) sum c_j e_j||
             <=sum |c_j|sqrt(K(j)),                    (4)

by the triangle inequality on the domain of S^(-1/2). This is a domain
statement about a specific reconstructed transfer space, not an empirical
choice of continuous physical time.

## 4. The common static threshold is the spectral bottom of this space

By Block35, at every beta>0 and fixed finite N, each e_j has the same visible
threshold E_rho. Its spectral measure for H_rho has no support below E_rho
and has support arbitrarily close to it. The projection onto [0,E_rho)
therefore annihilates every e_j, hence their S-polynomial dense span. So

 inf spectrum(H_rho)=E_rho.                            (5)

This conclusion follows for this explicitly defined common space. It is
not a claim that every possible infinite-volume charged representation has
that bottom. For two endpoint test charges, E_rho obeys the derived
separation-uniform Coulomb-form upper bound; general finite neutral charge
profiles obey E_rho<=a<rho,G3 rho>/2. Destructive combinations of insertions
can have a higher individual visible threshold without changing (5).

For the neutral profile the constant insertion j=0 gives the unit vacuum
vector and E_0=0. Charges that are aliases mod N are identified as above.
The direct finite checks should use several same-charge paths and mixed
time powers, verify the moment Gram forms and contraction bounds, and
compare mixed moments to explicit charged temporal-link sums. Matrix
positivity alone is not a check of the physical mixed-character identity.
