# Sector-selection proof search: live obligations

This file records attempts, not established phase results. The desired bound
compares the actual charge sectors of the supplied Hamiltonian with couplings
fixed independently of volume. A premise merely restating that comparison is
not counted as progress toward its proof.

## Exact decomposition worth using

The local all-or-none wrap argument in BLOCK1_DERIVATION.md applies whenever
Q'=Q, not just when both are zero. Thus the charge-conserving part
A_cons=sum_q P_q A_mu P_q is the same spin-one first-plus-second-harmonic
operator on every allowed integer sector. Since it is a pinching of A_mu>=0,
A_cons>=0. Write A_mu=A_cons-V, with V the nonnegative off-diagonal mixed-wrap
moves. Each local V_l has norm at most v_local=2t exp(-mu), from its symmetric
row sums. This decomposition separates finite-penalty charge mixing from the
within-sector harmonic; the latter is not a virtual process.

Let R_l indicate a nonzero integer charge in any cube incident on edge l.
Then (I-R_l) V_l (I-R_l)=0. For any normalized state, with p_l=<R_l>,

    |<V_l>| <= 2 v_local sqrt(p_l(1-p_l)) + v_local p_l
             <= 2 v_local sqrt(p_l) + v_local p_l.

Every cube has twelve edges, so sum_l p_l <=12 <N>. Cauchy-Schwarz gives

    |<V>| <= 2 v_local sqrt(12 |E| <N>) + 12 v_local <N>.

This is a local structural estimate. If one could prove

    A_cons >= e_neutral I - c N

with c independent of volume, then the variational neutral trial would imply,
for a ground state of A_mu+lambda N and lambda>c+12 v_local,

    <N>/|E| <= 48 v_local^2/(lambda-c-12 v_local)^2.

The displayed operator lower bound is still unproved. c=0 is precisely
neutral-sector ground selection for A_cons. The density conclusion is a
conditional consequence, not a solution of that comparison. Even if proved,
a small density would not by itself establish a Coulomb phase.

## Direct Perron comparison

Perron-Frobenius selects a positive vector in each connected configuration
component. It does not order components with different integer charge. The
original finite-mu gauge transformations act as permutations and therefore
fix the unique positive ground vector; integer divergence acts diagonally and
does not receive the same argument. This distinction survives the hard limit.

One possible comparison would embed every charged configuration graph into a
neutral one while lowering the electric potential and retaining every kinetic
edge. A fixed charge-canceling integer flow does not presently do this: its
translation can leave the bounded electric cube. No such embedding is assumed.

## Single-jump reduction

For one jump vector f with r nonzero entries, each +/-1 and electric states
in {-1,0,1}, a connected orbit is a line of length at most three. Ignore
inactive coordinates, which add a nonnegative constant when K>=0. The central
three-state line has diagonal (g r,0,g r), off-diagonal -t, and energy

    e_c = g r/2 - sqrt((g r/2)^2+2t^2),  g=3K/2.

A distinct two-state line has diagonal g n and g(r-n), possibly plus a
nonnegative inactive-coordinate contribution, where 1<=n<=r-1. Its energy is

    e_2 = g r/2 - sqrt([g(2n-r)/2]^2+t^2) > e_c

for t>0 and g>=0. A one-state orbit has nonnegative energy, also above e_c.
Thus the central line wins for a single jump. The inequality follows directly
by comparing the two radicands. Multiple overlapping plaquettes do not share
these single-term minimizing vectors, so summing this result does not order
their full sector energies. The unresolved step is compatibility of local
comparison maps on overlaps, not the one-plaquette calculation.

## Reflection route: source and exact missing match

[Lieb and Schupp, math-ph/9910037v1](https://arxiv.org/pdf/math-ph/9910037)
was read through its proof and discussion, including the crossing-bond ice-rule
argument. It uses a reflected tensor factorization and a trace inequality to
compare coefficient matrices. A local-field energy bound then constrains
ground-state magnetization. Its crossing interactions have a specific sign
and reflected product form. No factorization of our complete constrained
plaquette Hamiltonian into that form has yet been established. In particular,
zero charge expectation in a charge-conjugation mixture would not select a
sector; the useful target is a bound applying to every ground vector.

## Discrete rearrangement route

For an untruncated quadratic electric model, Fourier duality suggests a
diamagnetic comparison with a continuous-coordinate kinetic operator. The
hard electric cutoff does not commute with taking the modulus of a wave
function in the angle representation. Thus the usual modulus argument does
not immediately stay in the finite-spin carrier. A discrete replacement must
preserve both the cutoff and the allowed jump paths; it is not supplied by
the continuum proof.

A small exploratory non-geometric example with charge row (2,1,1,1) and all
unit-coordinate kernel jumps did not produce a counterexample: central and
nearest charged fibers have dimension 13, with adjacency radii 6 and
5.817301527..., respectively. It is not a cubic incidence matrix and is not
evidence for the desired theorem. It was only a test of an overly general
discrete-fiber intuition. No universal comparison is inferred from it.
