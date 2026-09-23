# Finite-rate renewed formation: an exactly solvable gauge-record star

Author result, 2026-09-22. Conditional finite-model theorem and complete
six-state calculation; independent reconstruction pending. The Hamiltonian,
quantum probability law, reservoir and scales below are supplied. This note
does not claim a native-axiom derivation, photon coexistence, or finite fuel.

## 1. Declared model and physical sector

A center A joins two leaves B1,B2. Each site has hard-core charge q=0,+1,-1,
with n=q². Orient both links outwards. The supplied constraint is
div E+1_A-q=0. Its total charge-one sector has E_j=-q_Bj. Integer spin one
with normalized raising/lowering matrix elements already realizes every
allowed shift with amplitude one. There are exactly six physical states:
three one-record states and three fully occupied states with one minus charge.

The hopping operator T moves a record and its unchanged charge into a vacancy,
updates the traversed electric link to preserve Gauss, and has matrix element
-1. It conserves total record number N. On each wholly vacant edge, a pair
jump j_e either coherently creates both charge orientations, or those two
orientations are separate jumps. Jumps preserve total charge and raise N by
two. These are distinct instruments.

Use
H=Delta N_B+t T,  L=sqrt(beta) j.
Initially g is the state with the sole plus record at A and E=0.
Put Q=1-n_A. Since N_B-Q=N-1, the replacement
H'=Delta Q+t T
changes the Hamiltonian only by Delta(N-1). Every trajectory density starts
number diagonal, hopping conserves N and each jump raises N by two. Therefore
H and H' give identical number-block-diagonal densities and marked trajectory
laws. This replacement does not remove a physical energy cost.

All full states are absorbing: hopping and pair jumps vanish there. Let b be
the normalized symmetric combination of the two states with the plus record
on a leaf. The no-event state remains in span(g,b), with matrix

H_nh = [[0,-r],[-r,Delta-i beta]],  r=sqrt(2)t.

Denote the bright basis vector by B below. The antisymmetric one-record state
is not populated. Both instruments have
the same total loss sum j†j=2Q.

## 2. Exact solution and a nonzero limiting clock

For delta,kappa>0 set epsilon=t/Delta and choose
Delta=delta epsilon^-4, t=delta epsilon^-3, beta=kappa epsilon^-2.
This is a different scaling from the previously checked vanishing-birth
field theorem. The microscopic formation coefficient diverges.

Write z=Delta-i beta, D=sqrt(z²+4r²), choosing D/z near one for small epsilon.
For all sufficiently small epsilon its real part is positive. Define
lambda_s=-2r²/(z+D), lambda_f=z-lambda_s. Then

a(tau)=(lambda_f exp(-i lambda_s tau)-lambda_s exp(-i lambda_f tau))/D,
b(tau)=r[exp(-i lambda_s tau)-exp(-i lambda_f tau)]/D.

These obey the initial condition (a,b)=(1,0) and the full no-event equation.
Let S=|a|²+|b|². Its derivative is -2 beta |b|². The normalized absorbed state
is independent of event time, since every jump annihilates g and maps the
single bright vector to a fixed output. In negative-at-A/B1/B2 order it is

sigma_coherent = [[2,1,1],[1,1,0],[1,0,1]]/4,
sigma_resolved = diag(1/2,1/4,1/4).

Thus the complete density, including the surviving coherence, is exactly

rho_epsilon(tau)=|a g+b B><a g+b B|+(1-S)sigma.

The full-state and one-record blocks are orthogonal.
For s0=exp(-4 kappa tau), define
rho_0=s0 |g><g|+(1-s0)sigma. Direct diagonalization of the two-dimensional
difference block gives the exact trace-norm identity

||rho_epsilon-rho_0||_1
 = sqrt((S-s0)²+4 s0 |b(tau)|²)+|S-s0|.                 (1)

To control this limit put u=epsilon². Taylor expansion of the explicit roots,
with delta,kappa fixed and positive, gives

lambda_s=-2delta/u+4delta-2i kappa
 +u(-16delta+12i kappa+2kappa²/delta)+O(u²).

Consequently gamma=-2 Im lambda_s=4kappa+O(u),
eta=-2 Im lambda_f=2beta-gamma, and
A_epsilon=2beta r²/|D|²=4kappa+O(u).
For small epsilon both gamma and eta are positive. The event-time density is

f_epsilon(tau)=A_epsilon[
 exp(-gamma tau)+exp(-eta tau)
 -2exp(-beta tau)cos(Re D tau)].                       (2)

Subtract gamma0 exp(-gamma0 tau), gamma0=4kappa. Since
integral_0^infinity |exp(-gamma t)-exp(-gamma0 t)|dt
=|1/gamma-1/gamma0|, triangle inequality gives the explicit all-time bound

||f_epsilon-gamma0 exp(-gamma0 .)||_L1
 <= (|A_epsilon-gamma0|+|gamma-gamma0|)/gamma
    +A_epsilon/eta+2A_epsilon/beta
 =O(epsilon²).                                        (3)

The CDF difference is bounded by the same expression. Also
|b(tau)|<=2r/|D|=O(epsilon), uniformly for tau>=0. Equation (1), the CDF bound,
and s0<=1 prove an O(epsilon) trace-norm limit uniformly over all tau>=0.
This is a statement about densities: the divergent real slow eigenvalue is
a scalar phase in the surviving one-record branch.

The two edge marks are equiprobable. Their conditional charge output states
are fixed normalized rank-one outputs for coherent per-edge jumps; resolved
marks additionally name the charge orientation. Conditional states are the
same at finite epsilon and in the limit. Therefore (3) also bounds the
integrated trace norm of the marked event/output-state density. Ordinary
total variation for its classical marginal has the additional factor 1/2.
There is no atom at infinity: both no-event eigenmodes decay. The instantaneous
density at time zero is zero, so a uniform pointwise hazard limit at zero is
neither asserted nor needed.

## 3. Exact mean waiting time

Let X=integral_0^infinity exp(i H_nh† t)exp(-i H_nh t)dt.
It solves i(H_nh†X-XH_nh)=-I. Direct substitution gives

X=[[ (Delta²+beta²+2r²)/(2 beta r²),
      (Delta+i beta)/(2 beta r)],
   [ (Delta-i beta)/(2 beta r), 1/beta ]].

The central-start mean time is therefore exactly

E tau=Delta²/(4 beta t²)+beta/(4t²)+1/beta
     =1/(4kappa)+epsilon²/kappa+kappa epsilon^4/(4delta²).

The runner solves this equation independently with symbolic linear algebra.

## 4. Energy and scope

For the original stated Hamiltonian,

tr(H rho_epsilon)/Delta
 = |b|²-2sqrt(2)epsilon Re(a* b)+2(1-S)
 ->2(1-exp(-4kappa tau)).

In particular the energy per completed pair in this convention is 2Delta and
diverges. The number-energy offset used to solve the density evolution is
not an autonomous reservoir or an energy-conserving creation mechanism.
Coherent and resolved outputs have purities 5/8 and 3/8 respectively.

This star permits one birth then fills completely. Repeated renewal needs a
larger model, treated separately in FINITE_RATE_REPEATED_RECORD_FORMATION.md.
That separate result uses Delta proportional to epsilon^-2, so its rates and
effective matter motion must not be copied from this scaling.

The construction addresses vacancy-triggered formation while old charge
content survives. It does not derive arbitrary record information, preparation,
a preferred quantum instrument, electromagnetic waves with appreciable
formation, a thermodynamic phase or a TOE.

## 5. Evidence and prior machinery

finite_rate_record_formation_check.py constructs the entire physical sector,
all hopping and birth matrices, and checks the integer Gauss/number/loss
identities. It compares independent full 36-dimensional Liouville matrix
exponentials against the two-amplitude solution for both instruments,
epsilon=0.1,0.075,0.05,0.025 and seven times through two. All density, trace,
positivity, exact-error, energy and mean-clock controls passed the first run.
The full values, not only pass labels, are in FINITE_RATE_FORMATION_RESULTS.json.

For context, [Reiter and Sorensen, effective operator formalism for open quantum
systems, arXiv:1112.2806v2](https://arxiv.org/html/1112.2806v2) supplies standard
effective Hamiltonian/jump formulas using a non-Hermitian excited-state
resolvent. Sections II and III.1--III.5 were read. Their slow/weak-coupling
derivation is not being imported as a rigorous error theorem; equations
(1)--(3) above provide the error proof for this model. The elimination
mechanism itself is established machinery, not a discovery of new physics.
