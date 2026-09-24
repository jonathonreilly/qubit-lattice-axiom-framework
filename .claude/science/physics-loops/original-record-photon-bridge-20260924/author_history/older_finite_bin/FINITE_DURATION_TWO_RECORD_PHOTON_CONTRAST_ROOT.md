# Finite-duration formation counts for a prepared photon packet

Personal root derivation, 2026-09-24. Conditional on the supplied common rotor
law and the previously sealed two-mark packet calculation. No microscopic
limit exchange, source selection, practical detector or empirical agreement
is asserted. All constants below refer to one fixed finite cubic graph, fixed
positive c,a,kappa, a fixed finite time horizon, and the stated preparations.

## 1. Replace the boundary density by an event with positive probability

Use the geometry, original resolved marks j,l, and all matter sectors of
TWO_FORMATION_RECORDS_READ_A_PHOTON_PACKET_ROOT.md, SHA256
6710b11cede13fc0cb8c7d9e83fac816d590acef8401bd1e98f432c3252840ce.
That source is a provisional personally derived argument, separately undergoing
blind review. Its exact initial effects are B_j*B_j=5I and
(B_l B_j)*(B_l B_j)=23I+W_p+W_p*. Use its normalized vacuum and one-particle
compact preparations, denoted psi_g^0 and psi_g^1. Set K=k0 g^2,
delta=delta0/g^2, with k0=c/(2a), delta0=c/(4a), and 0<g<=1.

Fix a time interval I=[t,t+h] within [0,T], h>0. The event is: the first
formation has the specified mark j at a time s in I, and the next formation
has the specified mark l within b>0 time units after s. Subsequent events are
unrestricted; no event between j and l is allowed. These are positive-width
conditions on the original labeled trajectory, not simultaneous events.
Let P_n(g;I,b) be its probability for preparation n=0,1.

With lambda=30 kappa V and the full postbirth no-event generator
A_+=-i h_+-kappa Lambda_+/2, the exact target expression is

 P_n = kappa^2 integral_I exp(-lambda s) integral_0^b
       || B_l exp(u A_+) B_j psi_g^n(s) ||^2 du ds,       (1)
 psi_g^n(s)=exp(-i h0 s)psi_g^n.

There is no replacement of h_+ by a field Hamiltonian. In particular its
electric coefficient is D(q,E), with the actual newly occupied B vertices
and actual A charges. Assume t+h+b is in the observation horizon when a
fixed terminal recording time is needed.

## 2. A sufficient bound on the full postbirth short-time error

Put Q=1+sum_e E_e^2. A scalar-shifted initial Hamiltonian is

 H0_g = k0 g^2 sum_e E_e^2 + g^-2 V0(theta),
 V0=(c/(2a)) sum_p(2-W_p-W_p*),       V0>=0.             (2)

On this finite graph V0 is bounded. The compact prepared finite-Hermite
packets satisfy ||H0_g psi_g^n||<=C uniformly for small g. This follows
directly from the cutoff/rescaling construction: g^2 E^2 becomes a fixed
second derivative; g^-2(2-2 cos(g y))<=y^2; derivatives of the fixed cutoff
are supported in Gaussian tails and are bounded despite inverse powers of g.
The normalization tends to one exponentially. Thus the same bound holds for
psi_g^n(s), uniformly for all s, by conservation of the spectral graph norm.
From the exact identity (2),

 || Q psi_g^n(s) || <= C g^-4.                         (3)

This estimate is deliberately crude: the bounded potential term was estimated
by its full norm, not by an unproved propagated fourth moment. The compact
packet has the required operator domain initially. A bounded perturbation of
the diagonal kinetic operator preserves its domain under its own unitary.
Equation (3) concerns that same full initial Hamiltonian, not an error vector
with an assumed weighted norm.

Every original B is a finite sum of bounded matter operations and fixed
integer field translations. For a fixed shift d,

 Q(E+d) <= C_d Q(E),

pointwise, giving ||Q B_j psi||<=C||Q psi||. The actual D in every P matter
word obeys |D(q,E)|<=C Q(E), since |q_a|=1 and its B-vacancy gates lie in
{0,1}. The full H4^C is bounded on the fixed graph, as is Lambda_+.
Consequently B_j psi_g^n(s) belongs to the domain of A_+, and

 || A_+ B_j psi_g^n(s) || <= C g^-2.                   (4)

The no-event semigroup is a contraction. For v in its generator domain,
||(exp(u A_+)-I)v||<=u||A_+v||, by integrating exp(r A_+)A_+v.
Using ||B_l||<infinity and ||exp(uA_+)B_j psi||<=||B_j psi|| gives

 | ||B_l exp(u A_+) B_j psi_g^n(s)||^2
                -||B_l B_j psi_g^n(s)||^2 |
                  <= C u g^-2.                       (5)

The constant can depend on the graph and supplied parameters, but is uniform
in 0<=s<=T, 0<g<=g0 and u>=0. A trivial bounded-probability estimate may be
smaller for large u; only short u is used here. No closure, commutativity,
postbirth weak-field approximation or optimality is assumed.

## 3. Controlled finite-bin signal

Use the wave-packet amplitude chi_p(s) and constant v_p from the sealed
source. Define two fixed finite integrals

 S_I = integral_I exp(-lambda s) ds > 0,
 H_I = integral_I exp(-lambda s)|chi_p(s)|^2 ds >= 0.     (6)

Combining (5) with the source's O(g^4) boundary-expectation error yields

 P_1-P_0 = -2 kappa^2 b g^2 exp(-g^2 v_p/2) H_I
               + kappa^2 b O(g^4+b/g^2),              (7)
 P_0 = kappa^2 b [25 S_I-g^2 v_p S_I
                         +O(g^4+b/g^2)].              (8)

Constants include the fixed interval and survival integrals. The b/g^2 term
comes from integrating the actual postbirth evolution, including the possible
rapid matter motion. A sufficient joint choice is

 b=b_g>0,        b_g/g^4 -> 0.                         (9)

Then these are actual event probabilities at every g, and

 (P_1-P_0)/(kappa^2 b_g g^2) -> -2 H_I,
 P_0/(kappa^2 b_g) -> 25 S_I,
 (P_1-P_0)/P_0 = -(2g^2/25)(H_I/S_I)+o(g^2).           (10)

For H_I>0 the sign is a deficit, not a positive photon-click count. The limit
can resolve the signal despite the shrinking time separation. Condition (9)
is sufficient from a rough global graph-norm estimate; no necessity or best
resolution bound is claimed. It does not establish a finite positive b limit
as g tends to zero. The first time interval h can stay fixed: it averages the
moving packet intensity with the known pre-first survival weight. If h also
shrinks, a separate uniform relative estimate must keep track of its size;
the displayed constants and assertions deliberately hold h fixed.

The source's narrow-band group-translation error can be integrated in (6).
If | |chi|^2-|chi_lin|^2 |<=A^2 M |s| sigma^2, then

 |H_I-H_I,lin| <= A^2 M sigma^2 integral_I s exp(-lambda s)ds. (11)

Thus the finite-bin record contrast follows the time-averaged translated
packet within both the stated bandwidth error and the small-g/bin error.
All these claims are on a fixed finite volume and finite horizon.

## 4. Signal size and what is still missing

As a diagnostic, suppose N independently prepared repetitions can be supplied
and the vacuum probability is known. The selected event count has mean NP_n
and variance NP_n(1-P_n). The squared mean-count contrast divided by the
vacuum count variance is exactly N(P_1-P_0)^2/[P_0(1-P_0)]. Equations (7)-(10)
give, for H_I>0,

 SNR^2 = [4 N kappa^2 b_g g^4 H_I^2/(25 S_I)](1+o(1)). (12)

This is the shot-noise statistic of this particular supplied protocol, not a
fundamental bound on every measurement, an apparatus cost theorem, or a claim
that the model supplies independent resets. If both preparations are estimated
from samples, their variances must both be included. For a fixed exponent
choice b_g proportional to g^(4+eta), eta>0, the displayed SNR requires N of
order g^(-8-eta) for a fixed nonzero target value, with all other quantities
fixed. The global survival exp(-30 kappa V s) further suppresses late first
pairs. An efficient local detector, replenished preparation and long-distance
protocol are not supplied by this argument.

The microscopic lattice still requires a convergence estimate for the labeled
finite-bin instrument. It must be applied at fixed g and positive b first;
an error in either P_n must be o(kappa^2 b_g g^2) along a chosen joint sequence
to resolve (7). Unconditioned density convergence alone is not that statement,
and a bare microscopic jump at time zero cannot be interchanged with the
common-target rate. No rate or existence of this instrument comparison is
proved here. It is an explicitly remaining bridge obligation.

The physical interpretation is conditional: the calculation now connects a
prepared target wave packet to a finite-probability event in the original
formation record. It does not establish measured photon response, select the
couplings/spacing/clock, produce a stationary physical vacuum or source, supply
cosmology, fit observations, or confirm a theory of everything.
