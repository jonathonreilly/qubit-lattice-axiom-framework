---
claim_id: finite_clock_static_charge_transfer_hamiltonian_and_path_comparison_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "For the supplied finite-clock Villain law at fixed finite N and beta>0, uniform inverse transfer moments and positive Fourier surface comparisons construct a common injective transfer operator for finite charged insertions. Its nonnegative Hamiltonian has an insertion-path-independent spectral bottom. The prior large-beta Wilson estimate additionally gives a Coulomb-form upper bound on finite neutral static charge energies. This concerns the specified free-boundary static correlation space, not moving matter or physical-law selection."
upstream_dependencies:
  - finite_clock_ginibre_free_state_and_static_charge_bound_bounded_theorem_note_2026-09-15
runner: scripts/finite_clock_static_charge_transfer_hamiltonian_and_path_comparison_2026_09_15.py
---

# Finite-clock static-charge Hamiltonian and path comparison

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** proposed_retained

For the supplied finite-clock Villain law, the static correlation functions
below determine one transfer Hilbert space for each finite charge profile.
The transfer operator is injective, so its logarithm is a densely defined
nonnegative Hamiltonian. Its spectral bottom agrees for all finite path
insertions with that charge profile. These are author proof proposals,
with personal finite checks and independent review still pending.

## Target and explicit dependencies

The [free-state and static-transfer source](FINITE_CLOCK_GINIBRE_FREE_STATE_AND_STATIC_CHARGE_BOUND_BOUNDED_THEOREM_NOTE_2026-09-15.md)
identifies the clock law's free-boundary limit and each path's positive
spectral measure. It left a possible zero-transfer atom and did not identify
a common path-independent bottom. Parts I-III supply those stronger
statements. Part IV extends its Green calculation to arbitrary fixed spatial
paths and neutral charge profiles. The linked theorem and its explicit
source-curvature premises supply the mathematical inputs. Historical branch
pins remain in the [original author packet](work_history/review_loop/pr8145/README.md)
as provenance; they confer no scientific authority.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: finite_clock_ginibre_free_state_and_static_charge_bound_bounded_theorem_note_2026-09-15
target_blocker_text: "Construct a common static-charge transfer Hamiltonian and identify the path-independent bottom in the same free-boundary state."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Independently review the common-space construction, then address the full field algebra and dynamical charged matter."
conditional_surface_status: "The specified clock Villain law, beta>0, fixed finite N and free-boundary state; the Coulomb-form quantitative bound additionally uses the source's explicit large-beta curvature assumptions."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Finite operator identities, positive Fourier comparisons and a matrix-moment construction with distinct direct-law finite challenges."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

| Input or obligation | Provenance and use | Status within this proposal |
|---|---|---|
| Finite-clock Villain measure and fixed beta>0,N>=1 | Supplied law in the linked source | Model choice; native selection open |
| Cofinal free state and temporal transfer identity | Source Parts II.4-5 | Provisional proof input; full source review required |
| Positive one-link Fourier coefficients | Gaussian alias formula below | Recalled and checked directly |
| Inverse moments and positive Fourier surface comparison | Parts I-II | Derived here for every beta>0 |
| Common matrix-moment Hilbert space and its spectral bottom | Part III | Derived here from the actual mixed static kernel |
| General path Green energy | Part IV | Derived here |
| Quantitative separation bound | Source Part I Wilson inequality | Additional explicit large-beta premise |
| Complete local field algebra, moving charges, physical clock and law | Separate physical targets | Open; no impossibility claim |

All boxes in the state passage are free cubic boxes as in the source. Fixed
spatial currents and fillings fit inside sufficiently large spatial boxes;
no thin-slab curvature estimate is imported. A zero-transfer bound is about
this reconstructed static space, not every possible infinite-volume charged
representation. The continuous semigroup is in selected lattice time units.

## Part I. Uniform inverse moments

### 1. A local Fourier comparison

In the notation of the linked source, T=V^(1/2) C V^(1/2), beta>0, and Omega_0 is
its normalized positive Perron vector, T Omega_0=lambda_0 Omega_0.
The one-link convolution in C has strictly positive Fourier coefficients

 c_k proportional sum_(r congruent k mod N) exp[-r^2/(2beta)],
 k in Z_N.                                              (1)

Let j be any integer spatial-link vector of finite support and U_j the
multiplication operator exp[2pi i j.a/N]. Fourier transformation makes C
diagonal with eigenvalues product_e c_(k_e); U_j shifts k by j. Hence

 U_j^* C^(-1) U_j <= K(j) C^(-1),
 K(j)=product_e max_(k in Z_N) c_k/c_(k+j_e).              (2)

This is a positive operator inequality, not a bound on individual matrix
entries. Each factor is finite, positive and at least1; edges with j_e=0
contribute1. For a simple length-R path with charge q, K(j)=kappa_q^R,
kappa_q=max_k c_k/c_(k+q). The choice of Fourier sign changes q to-q and
gives the same maximum since c_k=c_(-k).

U_j commutes with V and its inverse square root. Therefore

 U_j^* T^(-1) U_j <= K(j) T^(-1).

Taking the expectation in Omega_0 gives the volume-independent bound

 <U_j Omega_0,(T/lambda_0)^(-1) U_j Omega_0> <=K(j).       (3)

The comparison requires no source-curvature estimate or large-beta regime.
It is valid on every finite spatial box containing j, for every fixed finite
N and beta>0. K(j) can be extremely large and grows with path length; no
uniform bound in N or R is asserted. For a charge alias j=0 modN, K=1.

### 2. Removing the possible zero atom after the spatial limit

The finite path-insertion spectral law nu_(L,j) is supported on(0,1], and
(3) says integral lambda^(-1) nu_(L,j)(dlambda)<=K(j). The free-state
matching proof in the linked source identifies its weak limit nu_j on[0,1]. For each
positive integer m the function min(m,1/lambda), assigned value m at0,
is bounded and continuous on[0,1]. Weak convergence and then monotone
convergence give

 integral_[0,1] lambda^(-1) nu_j(dlambda)<=K(j),          (4)

where the integrand is infinite at0. Consequently nu_j({0})=0. This is
stronger than merely knowing finitely many positive-time moments.

On the ENTIRE cyclic Hilbert space L2(nu_j), multiplication by
H_j=-log lambda is now a densely defined nonnegative self-adjoint operator,
and the transfer multiplication operator is exactly exp(-H_j). The vectors
cut off to lambda>=1/m give the required dense domain. Its semigroup is
strongly continuous by dominated convergence, and for the cyclic vector1

 <1,exp(H_j)1> <=K(j),
 <1,H_j^p 1> <=p! K(j), p a nonnegative integer.         (5)

The second inequality uses E^p<=p! exp(E) for E>=0. In particular the
continuous-time interpolation W_j(t)=integral exp(-tE) nu_j(dlambda)
has every finite one-sided time derivative at0, determined by these moments.
It extends analytically to Re t>-1 by (4), with derivatives justified on
compact subsets using the spare exponential margin. This interpolates the
same integer-time static correlation; no empirical continuous time is derived.


## Part II. Positive Fourier surface comparison

### 1. Positive electric-coordinate transfer

For the same finite spatial clock box, put A=V^(1/2) C^(1/2), so

 T=A A^*, Ttilde=A^* A=C^(1/2) V C^(1/2).               (1)

All operators are invertible. In the Fourier basis, C is diagonal with
strictly positive products of the one-link coefficients c_k. V is a
convolution matrix whose coefficients are nonnegative: each plaquette
Villain weight has coefficients c_r>0, and their product expands as

 Vhat(m)=sum_(d1* s=m modN) product_p c_(s_p).           (2)

Thus Ttilde is entrywise nonnegative. Its largest eigenvalue lambda0 is
simple because T has a strictly positive configuration-space kernel.
Perron-Frobenius supplies a normalized nonnegative Fourier-coordinate
eigenvector Psi0. The original Perron vector is
Omega0=A Psi0/sqrt(lambda0), up to its positive overall phase.

For a spatial character U_j, define v_j=A^* U_j Omega0. Since U_j commutes
with V and shifts Fourier coordinates,

 v_j=C^(1/2) V U_j C^(1/2) Psi0/sqrt(lambda0).           (3)

Every Fourier coordinate of v_j is nonnegative. This assertion concerns
these transformed insertion vectors; it does not assume that sqrt(V) has
nonnegative Fourier coefficients.

For every integer time T>=1,

 W_j(T)=lambda0^(-T) <v_j,Ttilde^(T-1) v_j>.            (4)

This follows from (AA*)^T=A(A*A)^(T-1)A*. The distinction between T and
T-1 is essential.

### 2. A fixed surface bounds coefficient ratios

Suppose j-k=b=d1* S for a finite integer spatial plaquette field S. On Z3
every finite conserved difference b has such a finite filling. Work in
spatial boxes containing its support. Define

 R(S)=product_(p in support S) max_(r in Z_N) c_r/c_(r+S_p).

It is finite and at least1. Because c_r=c_(-r), the maximum for S_p and
-S_p agrees. In (2), changing the plaquette current variable s to s+S
is a bijection between the fibers for m and m+b, and each product weight
changes by a factor between R(S)^(-1) and R(S). Therefore

 R(S)^(-1) Vhat(m)<=Vhat(m-b)<=R(S) Vhat(m)             (5)

for every m. If a coefficient vanishes, the shifted one vanishes too by
the same bijection, so no division by an unsupported coefficient is made.

Equation(3), term by term, now gives

 R(S)^(-1) v_k <= v_j <= R(S) v_k                     (6)

in the Fourier coordinate order. Since every power Ttilde^(T-1) is
entrywise nonnegative, (4) implies

 R(S)^(-2) W_k(T)<=W_j(T)<=R(S)^2 W_k(T), T>=1.         (7)

The constant depends only on the fixed filling and local positive couplings,
not the spatial box or time length. It may be very large, and no optimized
surface or continuum parameter estimate is claimed.

### 3. Infinite free state and common thresholds

Pass (7) through the matched free-boundary limit at each fixed T. All
correlations have positive spectral representations, hence their long-time
rates exist. The fixed multiplicative comparison proves equal rates for
j and k, at every beta>0 and fixed finite N. Positivity at finite T follows
also from the transformed nonnegative vectors and positive definiteness;
the infinite positivity and finite rate follow from Part I's inverse
moment bound, which gives E_visible<=log K(j) by Jensen for the spectral
probability measure.

This removes the smallness premise from the path-independence input of
Part III's common transfer-space construction. Under the additional curvature
conditions, the sharper separation-uniform Coulomb upper bound continues to
hold. At other couplings no such separation bound is inferred from R(S),
K(j), or path independence alone. In particular a confining phase can still
have a path-independent static energy growing with endpoint separation.


## Part III. Common static-charge transfer space

### 1. The mixed moment kernel exists in the matched free state

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

### 2. A direct matrix-moment Hilbert construction

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

### 3. A genuine Hamiltonian on the whole common space

Part I gives integral lambda^(-1) nu_j(dlambda)<=K(j)<infinity for every
generating e_j. Hence the spectral projection P_{0} of S annihilates every
e_j. It commutes with S, so it annihilates every S polynomial times e_j and
therefore the entire dense span. Thus P_0=0: S is injective.

The spectral functional calculus defines a nonnegative self-adjoint

 H_rho=-log S, S=exp(-H_rho),                           (3)

on a dense domain. Its continuous-time semigroup is strongly continuous.
The e_j have the finite exponential energy moments from Part I. A finite
combination sum c_j e_j obeys

 ||S^(-1/2) sum c_j e_j||
             <=sum |c_j|sqrt(K(j)),                    (4)

by the triangle inequality on the domain of S^(-1/2). This is a domain
statement about a specific reconstructed transfer space, not an empirical
choice of continuous physical time.

### 4. The common static threshold is the spectral bottom of this space

By Part II, at every beta>0 and fixed finite N, each e_j has the same visible
threshold E_rho. Its spectral measure for H_rho has no support below E_rho
and has support arbitrarily close to it. The projection onto [0,E_rho)
therefore annihilates every e_j, hence their S-polynomial dense span. So

 inf spectrum(H_rho)=E_rho.                            (5)

This conclusion follows for this explicitly defined common space. It is
not a claim that every possible infinite-volume charged representation has
that bottom. Under the source curvature assumptions, two endpoint test charges obey
the derived separation-uniform Coulomb-form upper bound, and general finite
neutral charge profiles obey E_rho<=a<rho,G3 rho>/2. Destructive combinations of insertions
can have a higher individual visible threshold without changing (5).

For the neutral profile the constant insertion j=0 gives the unit vacuum
vector and E_0=0. Charges that are aliases mod N are identified as above.


## Part IV. General spatial-path Green energy

Write a finite spatial current as eta, its divergence as rho=d0*eta, and
its three Fourier components as eta_hat(k). Put lambda=sum_i|exp(ik_i)-1|^2
and r=(lambda+2-sqrt(lambda(lambda+4)))/2. As in the rectangular calculation,
the temporal Green kernel is g_lambda(t)=r^|t|/sqrt(lambda(lambda+4)).
The temporal current contributes |rho_hat|^2 times the sum of g(t-s) for
0<=s,t<T. The two spatial caps contribute
2||eta_hat||^2(1-r^T)/sqrt(lambda(lambda+4)). Different orientations have
no cross term because the one-form Hodge Green is scalar in orientation.
Thus exactly

 E_eta(T)=T integral |rho_hat|^2/lambda
   +2 integral (1-r^T)/sqrt(lambda(lambda+4))
                   [||eta_hat||^2-|rho_hat|^2/lambda].   (7a)

All integrals use normalized measure on the three-torus. Fourier divergence
and Cauchy-Schwarz give |rho_hat|^2<=lambda||eta_hat||^2, so the remainder
is nonnegative. Since ||eta_hat||<=sum_e|eta_e|, it is at most
2||eta||_1^2 G4(0), uniformly in T. Therefore E_eta(T)/T decreases to
<rho,G3 rho>. For a pair rho=q(delta_y-delta_x), this is
2q^2[G3(0)-G3(y-x)], yielding the pair-charge bound. For any finite neutral external charge
profile the corresponding bound is E_rho<=a<rho,G3 rho>/2. These are
upper bounds; no equality for the physical interaction energy is inferred.


The source Wilson bound is W_eta(T)>=exp[-a E_eta(T)/2], where
 a=beta^-1+epsilon under its stated source smallness. Passing T to infinity
using the displayed Green identity therefore gives E_rho<=a<rho,G3 rho>/2
in the common space of Part III. For two charges q at separation y-x this
is a q_eff^2[G3(0)-G3(y-x)], with q_eff a smallest absolute representative
mod N. It is uniformly bounded in their separation. No equality for a
Coulomb force, photon dispersion or propagating charged particle is inferred.

## No-Go Discipline Gate

This is an affirmative theorem proposal. The following records the scope of
its conclusions; it submits no impossibility result, exhaustive route search,
independent wall count or requirement to change the axioms. No negative
packet PASS is claimed.

**N1 — Actual mechanisms.** The four constructive mechanisms are a local
inverse-operator comparison, a positive Fourier surface bijection, a mixed
moment Hilbert construction, and temporal Green summation. Their finite
controls test incorrect inverse constants, omitted surface constants,
omitted temporal charge phases and an incorrect longitudinal subtraction.
These are concrete author checks of this construction, not five exhausted
alternative research routes. The no-go route quota is not represented as met.

**N2 — Dependencies.** The common-space injectivity uses the inverse moment
bound. Its path-independent bottom additionally uses the surface comparison.
The quantitative charge bound adds the earlier Wilson inequality and Part IV.
These are dependencies in one proof, not independent physical walls. The
relations among native law selection, full field reconstruction and moving
matter are unresolved here; no independence assertion is made.

**N3 — Hidden-premise scan.** The supplied Villain law, beta>0, fixed finite N,
free-boundary state and matched cofinal limits are explicit inputs. "By
construction" refers to the specified moment-space completion and its dense
span, not to a pre-existing physical Hilbert space. Large-beta curvature is
used only for the quantitative charge bound. No all-state uniqueness, physical
time calibration or full local operator algebra is assumed.

**N4 — Residual match.** The linked free-state and static-transfer source supplies free-state limits and
individual path moments. It does not supply the inverse bound or a common
path-independent bottom; these are the present proof obligations. No prior
no-go, negative search or numerical failure is used as an impossibility witness.

**N5 — Resolution.** The primary runner evaluates local Fourier ratios,
spatial-square temporal-link sums, transfer spectra and finite surface/path
comparisons. Its five resolution lines state that the infinite-volume and
common-space conclusions require the written arguments. Finite floating
agreement does not certify either passage.

**N6 — Partial closure.** The present theorem closes a specified mathematical
construction under a supplied law. Deriving that law, extending the observable
algebra, and adding dynamical matter remain possible research routes. None is
claimed to require a new axiom. An improved physical interpretation alone
would not prove the missing dynamics.

**N7 — Strongest challenge.** A reviewer should challenge whether every mixed
kernel is obtained in the same free state, whether the transformed insertion
positivity really follows without positive Fourier coefficients for sqrt(V),
and whether the generators exhaust the claimed space. Parts II-III address
those precise issues. A larger physical representation could contain extra
states below this space's bottom; the conclusion deliberately identifies only
the common space reconstructed here.

**N8 — Earlier-cycle correction.** The immediately preceding static-source
proposal left a zero atom and a path-visible threshold. The inverse comparison
and positive surface bijection provide constructive ways to remove those
limitations. The separate private real-source square-root logarithm argument
uses stronger coupling assumptions; it is not needed for Part II. No prior
limitation is inherited as a permanent physical obstruction.

## Author evidence and limits

The primary runner combines four self-contained finite probes. Thirty
insertion cases compare direct inverse solves, Fourier alias ratios,
whitened inverse operators and spectral sums. Five square systems compare
positive transformed insertion vectors and ten fixed-surface bounds.
Three systems compare mixed same-charge moments with explicit temporal-link
sums and check their moment Gram forms. Twenty-four general-path Green
fixtures compare the reduced identity with direct temporal-kernel sums.
These floating checks are not interval certificates or infinite-volume proofs.

The first positive-Fourier fixture used a full nearly degenerate Perron
solve and produced a spurious negative sector component of about9.37e-13.
Its source and failure are preserved at campaign commit
`3c6b685f6d69393d7dab170713daff2073535812`. The corrected probe solves the
exact neutral Fourier block, reconstructs the configuration Perron vector,
and checks its full-matrix residual and largest eigenvalue. No tolerance
was loosened and no coordinate was clipped. This is numerical provenance,
not a scientific input required by the runner.

The primary reads only its own source for an integrity hash. All scientific
fixtures and actual control formulas are inside it. Its canonical cache uses
the declared300-second timeout. The author packet records actual mutation
checks, source hashes and repository validation. These are author checks;
independent source review and formal audit remain separate. No axiom,
primitive, editable prompt, audit verdict or main-branch science is changed.
