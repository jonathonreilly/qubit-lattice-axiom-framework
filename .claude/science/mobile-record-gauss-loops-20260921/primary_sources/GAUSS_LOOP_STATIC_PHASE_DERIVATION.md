# Static phase of the permanently labeled axis-loop model

2026-09-21. Primary derivation; selective independent reconstruction pending.
The finite-volume coefficient checks are complete. The polymer proof below
is newly derived and has not yet received an independent proof check.
This note specifies an equilibrium ensemble for the conservative model;
it does not assert that the irreversible formation process reaches it.

## 1. Ensemble and exact current representation

Use the thirteen labels and centered divergence of
`MICROSCOPIC_GAUSS_IMPULSE_AND_RECORD_LOOPS.md`. On an odd torus of side
N>=7 and volume V=N^3 define

    Z_N(zA,zB)=sum_eta zA^nA(eta) zB^nB(eta)
                         1_(D2 E=0,D2 B=0),
    mu_N(eta)=Z_N^-1 zA^nA zB^nB 1_(D2 E=0,D2 B=0),       (1)

where D2=2D and the vacuum has weight one. Positive real fugacities give
the conditional product law proved stationary for conservative loop moves.
The parameters are not formation rates, nor do they specify a mixing time.

A record at x with signed axis sigma e_i is an oriented edge between
x-e_i and x+e_i of the charge graph with nearest steps +/-2e_i. Its sign
orients that edge. At every vertex D2=0 is equality of incoming and
outgoing edges, separately in the two species. Every connected component
of occupied edges is therefore a balanced directed graph and decomposes
into directed cycles. The decomposition into connected components is
unique; a decomposition into individual cycles need not be unique.

Physical capacity remains an extra condition: the three charge-graph
edges with midpoint x, in either species, compete for the same record
slot. Treating them as six independently occupiable bonds changes (1).

For odd N the charge graph is connected, although its local step-two
geometry has the parity structure of eight sublattices on the infinite
lattice. Even-volume variants have eight disconnected charge graphs.
Neither fact removes the physical midpoint capacity or establishes a
continuum interpretation of the additional centered-difference zeros.

The ensemble in (1) is broader than the set reached from empty by the
specified dynamics. Translations and reversals preserve every label count;
formation adds four records of one species and zero total vector. Thus
empty-start histories have nA=nB=0 modulo four and zero total E and B.
A six-record rectangular loop satisfies both Gauss constraints but violates
that count condition. A straight winding line of N identically signed
axis records has nonzero total vector and also satisfies Gauss. Neither
example can be generated from empty by the supplied rules. No ergodicity
or equivalence between this grand ensemble and the growing state is used.

For completeness, the leading zero-mode covariance in the full finite
ensemble comes from straight winding lines. For each axis there are N^2
lines and two signs, with Ehat(0)=+/-N e_i/sqrt(V). Consequently
along zA=epsilon a,zB=epsilon b it is
2N a^N epsilon^N I+O_N(epsilon^(N+2)) in the A sector. A detour adds at
least two edges; contractible components add at least four. This finite
effect is consistent with an exponentially suppressed winding contribution
in the small-fugacity thermodynamic limit proved below.

## 2. Exact low-order finite-volume coefficients

There is no nonempty balanced current with fewer than four records.
For N>=7 a four-edge cycle cannot wind around the torus. It must be a
coordinate square of side two in the charge graph. Its four midpoints
are exactly the cross template in the construction note. There are
three planes, two circulations and V centers: 6V configurations per
species. There is also no balanced five-edge configuration: every edge
lies on a directed cycle, the shortest cycle has length four, a five-cycle
is absent, and disjoint cycles require at least eight edges. Winding
cycles of odd length N are allowed at higher order.

Set zA=epsilon a and zB=epsilon b at fixed finite N. Then

    Z_N=1+6V epsilon^4(a^4+b^4)+O_N(epsilon^6),
    rho_A=24a^4 epsilon^4+O_N(epsilon^6),
    rho_B=24b^4 epsilon^4+O_N(epsilon^6).                   (2)

The density coefficients follow either by counting four records per
configuration or by z_s d(log Z)/dz_s divided by V. Every one of the six
labels in a species has coefficient four at each physical site.

Let Ehat(k)=V^-1/2 sum_x exp(-ik.x)E(x), and put s_i=sin k_i. The
means vanish by reversing all signs in either species. Directly summing
the two circulations in the three planes gives

    <Ehat(k) Ehat(k)^*>
       =8a^4 epsilon^4 (|s|^2 I-ss^T)+O_N(epsilon^6),
    <Bhat(k) Bhat(k)^*>
       =8b^4 epsilon^4 (|s|^2 I-ss^T)+O_N(epsilon^6).       (3)

The cross E/B covariance is exactly zero at every fugacity and volume:
global A-sign reversal preserves (1), reverses E and leaves B unchanged.
The order-four coefficient at k=0 vanishes. Winding currents at higher
order can carry nonzero total vector on a finite torus.

The script `gauss_loop_fugacity_check.py` enumerates all self-avoiding
four-step closed charge-graph walks at N=7 without using the template
list. It obtains 2058 distinct oriented configurations per species,
checks every integer divergence and label count, and checks (3) by direct
Fourier summation. These are finite-volume coefficients. The symbols
O_N in (2)-(3) alone imply no uniform thermodynamic statement.

## 3. Exact compact-phase representation, with the capacity factor intact

Fourier orthogonality for each integer charge gives the identity

    Z_N = integral product_x [dtheta_x dphi_x/(2pi)^2]
          product_x {1
            +2zA sum_i cos(theta_(x+e_i)-theta_(x-e_i))
            +2zB sum_i cos(phi_(x+e_i)-phi_(x-e_i))}.       (4)

Each term in a one-site brace is vacancy or one of twelve labels.
Expanding the product before integration recovers (1) exactly. A product
over axes or species inside that brace would permit multiple records at
one site and is not this model. The brace is bounded below by
1-6(zA+zB), so nonnegative local factors are guaranteed when
6(zA+zB)<=1. At zA=zB=1/10, choosing every incident difference pi at a
particular site makes its brace negative. Those six neighboring phase
differences can be assigned simultaneously for N>=7. Thus (4) is not
automatically a positive XY-type Gibbs weight at general fugacity.

## 4. Exact hard-core polymer representation

A polymer gamma is a nonempty connected balanced signed edge set of
one species in the charge graph, with at most one record at each physical
midpoint. Its size n(gamma) is its number of records and its activity is

    w(gamma)=z_species^n(gamma).

Two polymers are incompatible if they share a physical record slot, or
if they have the same species and share a charge vertex. A polymer is
incompatible with itself. The latter condition ensures that compatible
same-species polymers really are distinct connected components. Every
configuration in (1) has exactly one compatible collection of polymers,
and every such collection gives one configuration. Therefore its partition
function is the hard-core polymer partition function with these activities.
This representation includes branched balanced components, long loops,
winding loops and every hard-capacity interaction. It is not a gas of
independent four-record templates.

The external mathematical input used below is Theorem 1 and its rooted
bound (5) in D. Ueltschi, *Cluster expansions & correlation functions*,
Moscow Mathematical Journal 4 (2004), 511-522, arXiv version v3:
https://arxiv.org/pdf/math-ph/0304003. Its hypotheses and proof in Section 2
have been read. For a finite hard-core polymer set, pair factor zeta=-1
on incompatible pairs and zero otherwise satisfies |1+zeta|<=1. If

    sum_(eta incompatible gamma) |w(eta)| exp(a(eta))
                 <=a(gamma),                            (5)

then the connected expansion for log Z converges absolutely, with a
bound on clusters incompatible with a fixed root. The following estimates
check (5) for this specific model; applicability is not inferred merely
from the name of the theorem.

## 5. A deliberately conservative uniform convergence domain

The charge graph has degree six. Its edge-adjacency graph has degree
at most ten. Fix an unoriented edge and a species. A connected set of n
edges containing that edge has a canonical spanning-tree depth-first
walk of length 2(n-1) in the edge-adjacency graph. Its visited set recovers
the edge set, so there are at most 10^(2n-2) such sets. Assigning signs
gives at most

    2^n 10^(2n-2)                                      (6)

polymers before imposing balance and physical capacity. Discarding invalid
sets only improves the bound. Every valid polymer has n>=4 for the
specified odd N>=7, and the same statement holds in the infinite lattice.

A polymer incompatible with a fixed record of gamma can be anchored
either at one of the eleven same-species edges incident to that record's
two charge endpoints, or at one of the six axis/species choices with the
same physical midpoint. The union actually overlaps; using seventeen
anchors is a safe overcount. Thus at most 17 n(gamma) anchor families
suffice for all incompatibilities.

Put z=max(|zA|,|zB|) and use the enlarged activity

    w_tilde(gamma)=|w(gamma)| exp(n(gamma)),
    a(gamma)=n(gamma),
    q=200 e^2 z.

For any fixed typed edge, (6) gives

    sum_(gamma containing edge) w_tilde(gamma) exp(a(gamma))
       <= (1/100) sum_(n>=4) q^n
       =q^4/[100(1-q)] =: S(q).                         (7)

Consequently, if

    max(|zA|,|zB|) <= z_star=1/(400 e^2),                (8)

then q<=1/2, S<=1/800, and the left side of (5), with the
enlarged activities, is at most (17/800)n(gamma)<a(gamma).
The remaining total-variation integrability condition is automatic on
every finite torus because its polymer set is finite. All constants are
independent of N. The resulting small domain is a sufficient domain,
not an estimate of a critical fugacity or a realistic density threshold.

For a useful spatial root add an auxiliary zero-activity polymer g_x,
incompatible with each polymer occupying the physical site x, with
a(g_x)=1. There are six typed-edge anchors at x, so its condition is
bounded by 6S<=6/800<1. The theorem's rooted bound (5), applied to g_x,
therefore gives, with M=sum_gamma n(gamma) for a cluster and R_x the
number of its polymer occurrences occupying x,

    sum_clusters |cluster_weight| exp(M) R_x <= 1.       (9)

Repeated polymers in the connected expansion count with multiplicity;
the bound and R_x do also. They are not claimed to be physically
simultaneous records. The n!-normalization is the one in the cited theorem.

## 6. Exponential connected correlations in the controlled ensemble

Introduce finite-support local sources h_i(x) by multiplying a polymer
activity by exp(sum_x h(x).E_gamma(x)), and similarly for B. Differentiating
log Z twice yields the connected covariance. For components E_i(x),E_j(y)
its cluster insertion has absolute value at most R_x R_y. Since R_y<=M,
it is bounded by R_x M. The enlarged-activity convergence in (9) justifies
the differentiations: a bounded source costs an exponential in M, and
the remaining exponential controls the polynomial insertions.

In a polymer, successive edge midpoints sharing a charge vertex have
physical lattice distance at most two. Incompatible polymers also meet
at a midpoint or share such a charge vertex. A cluster containing x,y
therefore has a connected graph of its record occurrences with edges
of length at most two. For the torus distance r=d_1(x,y),

    r<=2(M-1)<=2M.

For every term with R_x R_y>0,

    M exp(-M) <= (2/e) exp(-r/4),

using M exp(-M/2)<=2/e. Combining with (9) gives the uniform bound

    |Cov_mu_N(E_i(x),E_j(y))| <= (2/e) exp(-d_1(x,y)/4). (10)

The same component bound applies to B. For general bounded one-slot
functions f,g, put A_f=max_occupied |f(label)-f(vacancy)| and similarly A_g.
The same proof gives (2/e) A_f A_g exp(-d_1/4); the E/B components have
A_f=A_g=1. Subtracting the vacancy values makes these sources additive
over the records in compatible polymers. No dynamical
relaxation bound follows from this equilibrium estimate. In particular,
the conservative local generator can still have many invariant subsets.

For fixed local observables, a cluster that wraps around the torus has
size growing at least linearly in N. Its contribution is exponentially
small by (9). Nonwrapping finite clusters stabilize under the natural
local lift to the infinite lattice. Dominated convergence therefore
gives the periodic thermodynamic limit, as well as the same local limit
from boxes with vacant exterior, provided Gauss is imposed at every charge
vertex incident to an allowed record edge, including boundary/exterior
vertices. Dropping those constraints permits open currents and is a different
specification. This argument does not assert uniqueness
for every conceivable Gibbs boundary condition. Bound (10) survives in
the limiting state and makes its Fourier covariance analytic near k=0.

## 7. Exact Gauss constraints plus clustering determine the infrared order

Let S_E(k)=sum_x exp(-ik.x)Cov(E(0),E(x)) in that infinite-volume
state. Exponential summability from (10) makes this a real analytic
matrix function near every real k. The exact microscopic constraint
implies

    s(k)^T S_E(k)=0,    S_E(k)s(k)=0,
    s_i(k)=sin k_i.                                    (11)

Substitute k=t v, divide by t and let t->0. Since v is arbitrary,
v^T S_E(0)=0 for all v, hence S_E(0)=0. Spatial inversion is a symmetry
of (1), so S_E(-k)=S_E(k); its first derivatives vanish as well. Therefore

    S_E(k)=O(|k|^2),    S_B(k)=O(|k|^2).                 (12)

The cross-species covariance remains exactly zero. Cubic symmetry
further restricts the leading quadratic matrix to

    S_E(k)=c_A(zA,zB)(|k|^2 I-kk^T)+O(|k|^4),           (13)

and the corresponding formula with c_B. To see this, the most general
even cubic quadratic symmetric tensor has diagonal a|k|^2+b k_i^2 and
off-diagonal c k_i k_j. Equation (11) gives a+c=0 and b=c. Positivity
requires a>=0. The uniformly convergent expansion recovers (3), so along
zA=epsilon a0,zB=epsilon b0,

    c_A=8a0^4 epsilon^4+O(epsilon^6),
    c_B=8b0^4 epsilon^4+O(epsilon^6).                    (14)

Here the analytic expansion, unlike the finite-volume O_N alone, permits
the thermodynamic passage. If a0>0 then c_A>0 for sufficiently small
positive epsilon on that ray; this statement does not provide a sharp
uniform lower bound over the full sufficient domain (8).

The argument also makes S vanish at the other zeros of the centered
divergence symbol. No additional microscopic mode has been projected
away. Equation (12) describes a controlled dilute equilibrium regime;
it differs from a nonzero direction-dependent transverse covariance
approaching k=0. Reaching such a Coulomb-type regime would require leaving
this analytic state, changing the ensemble, or changing the construction.
It is not excluded by the record axioms or by this small-fugacity theorem.

## 8. Research consequence and remaining obligations

The supplied loop construction has a compatible exact microscopic Gauss
sector and a rigorously tractable dilute-ensemble route. Its small-loop
coefficient does not itself deliver the field covariance of a Coulomb
phase. The new proof strategy replaces that finite-order observation by
a proposed uniform dilute-domain result, conditional only on the explicit
model and checked applicability of the stated cluster-expansion theorem.
Independent checking of this proof and its counting constants is pending.

The scientifically useful next target is a state-selection mechanism at
larger density, or another constraint-preserving encoding with a controlled
extended-loop phase. A formation process selects a history-dependent state;
its exact charge preservation does not identify that state with (1).
Proving mixing, a phase transition, ballistic transverse dynamics, quantum
statistics, Lorentz symmetry or gravity requires additional work. No
parameter in this note has been derived from the repo's minimal axioms.

Literature comparison is limited: Henley's review describes the additional
disordered-flux assumptions behind a Coulomb phase, and Hermele, Fisher and
Balents study quantum ring-exchange models. Neither supplies the missing
state-selection or quantum proof for this classical thirteen-state process.

- https://arxiv.org/abs/0912.4531
- https://arxiv.org/abs/cond-mat/0305401
