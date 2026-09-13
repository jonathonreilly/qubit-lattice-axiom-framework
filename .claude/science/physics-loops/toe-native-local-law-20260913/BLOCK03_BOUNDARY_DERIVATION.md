# Interacting finite windows and Euclidean comparison

Working continuation of BLOCK03_DERIVATION, written before its checker.

## Cell interaction norms

For the selected t1=t2=1 Wilson symbol, the oriented neighboring-cell
coefficient matrices, using h(k)=sum_delta h_delta exp(-ik.delta), are

    W1=(-sigma3+i sigma1)/2,
    W2=(-sigma3+i sigma2)/2,
    W3=-sigma3/2.

Each has trace norm1. The first two have singular values1,0; the third
has1/2,1/2. The bond Fock operator
c_n* W_a c_(n+e_a)+h.c. therefore has norm1: diagonalizing its one-particle
block gives paired singular values, and its largest many-body energy is
their positive sum. This is a norm of the actual bond, not a coefficient
count proxy.

All interaction and counterterm terms are onsite in MODEL-cell space,
whose local Fock dimension is four. Passing to their product onsite
interaction picture leaves every cell-bond term even, on the same two
cells, and norm1. Consequently the following propagation estimate has
no hidden volume factor or onsite-interaction norm in its velocity.
The onsite Hamiltonian is bounded per cell, so that interaction picture
exists on every local observable, uniformly in the finite volume.

## A coarse boundary estimate

Let Lambda be an open model-cell box, x in Lambda, and
d=dist_Z3(x,Lambda_complement). Let tau^Lambda_t and tau_t be finite and
infinite dynamics for (3.1). For any unit-norm operator A supported in
cell x, including an odd field, the proposed bound is

    ||tau^Lambda_t(A)-tau_t(A)||
       <=2 sum_(n>=d) (24|t|)^n/n!
       <=2 exp(24e|t|-d).                              (B.1)

A proof must retain the support-chain resummation; a naive unrestricted
nested-commutator count would introduce spurious factorials.

The time-dependent even-CAR commutator recursion is the one in
[Nachtergaele, Sims and Young, v3](https://arxiv.org/pdf/1705.08553v3),
Lemma3.3 and Eqs.(3.28)–(3.31), whose statement and proof were read.
Here there are two fermion labels per cell, norm-continuous even finite-range
terms, and the comparison boundary operator is even. Its disjoint commutator
therefore vanishes even when A is odd. The specialized bond counting below
derives our constants; no numerical velocity is imported from that paper.

In the onsite interaction picture, the standard commutator differential
inequality iterates over chains of bonds with consecutive intersections.
Its n-fold time-ordered integral is |t|^n/n!, and each commutator costs
a factor2 times the bond norm. An initial cell meets6bonds; a bond meets
at most11bonds, including itself. In the Duhamel difference of the two
dynamics the final bond crosses the boundary. Every such chain has at
least d bonds. Summing boundary bonds inside the chain count, rather
than multiplying by the boundary area afterwards, gives at most
6*11^(n-1) chains, each contributing at most(2|t|)^n/n! after the
Duhamel integration. Their bound is no larger than the deliberately looser
2*12^n count used in(B.1). The same argument works for an odd A because
the Hamiltonian terms are even and commute with disjoint odd observables.
The time-dependent interaction-picture terms have the same norms.
For the last inequality, use1_(n>=d)<=exp(n-d) in the exponential series.

For a finite observable support X, replace the right side by |X| times
it and let d be the minimum boundary distance. This is only a finite-time
comparison, not a norm bound uniform as time tends to infinity.

## State restriction and neutral correlators

Let omega be the infinite interacting state supplied by the primary theorem.
Take its exact finite marginal rho_Lambda, and extend its parity by the
one idle boundary fermion. The native even-sector state has exactly that
bulk marginal. For y also in Lambda, the finite real-time neutral function

    f_Lambda(t)=Tr rho_Lambda tau^Lambda_t(c_x) c_y*

is represented by an even native observable. Its infinite counterpart is
f(t)=omega(tau_t(c_x)c_y*), and(B.1) implies
|f_Lambda(t)-f(t)|<=2 exp(24e|t|-d).
The rho_Lambda used here is a marginal of omega, not claimed to be the
Gibbs state of the open Hamiltonian. Preparation remains supplied.
Using the dressed fields c_x g_ancilla makes the full finite CAR matrix
representation explicit, but does not create a local charged readout.

## Recovering a fixed Euclidean correlator

The infinite ground-state GNS generator is nonnegative. Therefore the
positive-time Euclidean two-point function can be recovered by the Poisson
smearing of its real-time function:

    G(tau)=integral_R P_tau(t) f(t) dt,
    P_tau(t)=tau/[pi(t²+tau²)], tau>0.

Indeed Fourier transformation of P_tau gives exp(-tau|omega|), which
equals exp(-tau omega) on the nonnegative ground-state spectral support.
The spectral theorem justifies the identity also for the complex
cross-spectral measure of distinct fields. The norm bound |f(t)|<=1
is sufficient for the tail estimate.

Define the FINITE observable
G_(Lambda,T)(tau)=integral_(-T)^T P_tau(t) f_Lambda(t) dt.
It is not the open marginal's own imaginary-time Gibbs correlator.
The explicit comparison is

    |G_(Lambda,T)(tau)-G(tau)|
       <=2 exp(24eT-d)+2tau/(pi T).                    (B.2)

The second term bounds the omitted Cauchy-kernel tail. For0<epsilon<1,
choose T>=4tau/(pi epsilon) and d>=24eT+log(4/epsilon); then the error
is at most epsilon. Negative Euclidean times use the reversed occupied
correlator and its fermionic sign. Equal time is already a marginal identity.

This transfers FIXED-time correlators of the theorem-matched interacting
model to finite native protected observables. The continuum infrared
asymptotic is taken only after this finite-window approximation converges.
It gives no uniform finite-resource limit all the way to zero energy.

## Containing the growing Record process

For the two-seed program process, each program vertex has degree at most6.
A simple length-n path from a seed with no other seed in its interior
has a sum of n independent exponential waiting times. For a union bound on unusually fast arrival,
an actual arrival by T implies SOME simple path whose sum is at most T.
Markov's inequality for exp(-11gamma sum E) gives

    Pr(sum_(j=1)^n E_j<=T)<=exp(11gamma T) 12^-n.

From two seeds there are at most2*6^n candidate paths. Thus the probability
of reaching program graph distance at least D by T is at most

    2^(2-D) exp(11gamma T).                             (B.3)

All newly formed native sites are adjacent to already formed program sites.
A program window with D>=(11gamma T+log(4/epsilon))/log2, with a fixed
one-site native margin, therefore couples to the infinite Record process
up to time T except on an event of probability at most epsilon.
This is a stated probability error, not a pathwise bound for all clocks.

Combining the model-cell matter margin with its physical embedding and this
program margin gives finite site resources of order
(R+T+gamma T+log(1/epsilon))³, with T itself scaling as tau/epsilon in(B.2).
The native paths have length at most3 and fixed star support, and there
is one parity spectator. Optional collision storage/control is additional.
No rate, clock, infinite state or preparation procedure is derived.

The support-chain coefficient and every Fourier/path convention still need
the dedicated author checker and a cold proof review. These equations are
working analytical claims, not independent certification.
