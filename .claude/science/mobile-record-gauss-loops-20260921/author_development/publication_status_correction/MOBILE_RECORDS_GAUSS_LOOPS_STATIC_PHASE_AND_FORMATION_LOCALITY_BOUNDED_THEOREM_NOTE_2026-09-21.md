---
claim_id: mobile_records_gauss_loops_static_phase_and_formation_locality_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "For the supplied thirteen-label centered-divergence model: atomic four-record translations, permutations and vacant-cross births preserve record identities, capacity and both Gauss identities. The conservative Gauss-conditioned product is stationary; the irreversible births need not select it. Its exact leading fugacity coefficients and balanced-component polymer representation yield an explicit uniform low-fugacity region with exponentially decaying covariance, a periodic thermodynamic limit and an analytic quadratic infrared spectrum. A reachable-background counterexample shows that the specified constant-rate collective birth does not satisfy the framework's nearest-neighbor conditional forming-label law. These are bounded supplied-model statements, not a realization of all minimal axioms, a collective wave theorem, a selected physical phase or a derivation of electromagnetism."
upstream_dependencies:
  - minimal_axioms
runner: scripts/mobile_records_gauss_loops_static_phase_and_formation_locality_2026_09_21.py
---

# Mobile permanent records: exact Gauss loops, their dilute phase and formation locality

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support
**Author support:** conditional-support; no independent audit verdict.

Four permanent records can move together, empty their former sites and allow
new records to form there while preserving an exact discrete Gauss identity.
For the specified conservative ensemble, a convergent polymer expansion
also determines the dilute long-wavelength state. The constant-rate birth
rule has an exact locality counterexample: it is not a model of every axiom.
These three results belong together; the constructive event history must
not be presented without the conditional-formation qualification.

The alphabet, collective generator, centered field encoding and fugacities
are supplied choices, not a derivation from the
[minimal axioms](MINIMAL_AXIOMS_2026-06-29.md). The original
fifteen-state comparison in Part A uses vacancy, six labels with e=+/-e_i,b=0,
and eight labels with e=0,b in {+/-1}^3. The new loop model instead has two
six-axis orbits. Fugacity is an equilibrium parameter, not a formation clock.
The quantum and physical field interpretations remain additional obligations.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "Can immutable-record transport and renewed formation coexist with exact microscopic Gauss identities, and what state and forming-label law result?"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Construct or select a genuinely nearest-neighbor formation law and a correlated physical field state; keep kinematic constraints, equilibrium and formation-selected laws distinct."
conditional_surface_status: "Exact finite-event and locality identities; conservative equilibrium and a uniform low-fugacity polymer theorem for the specified encoding."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Complete supplied-model arguments with separate finite-event, polymer-proof and locality review."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The proofs below preserve the checked working arguments. Their original
source bytes and the publication transformation are in the evidence packet.
Each part retains its own equation numbering.

## Part A. Exact local Gauss constraints with mobile, permanently labeled records

2026-09-21. Primary construction and exact finite controls; selective
independent reconstruction completed. This is a new supplied microscopic model, separate
from the fifteen-state positive-floor transverse-wave generator. Its limit
theory has not been proved. The purpose is to test whether departure and
fresh formation can coexist with an exact local divergence constraint.

### 1. The charge impulse of a two-site swap

On a cubic torus of side N>=5, define the centered discrete divergence

    D F(z)=(1/2) sum_j [F_j(z+e_j)-F_j(z-e_j)].

This is an explicitly chosen encoding of a local Gauss quantity. It is
covariant under the usual signed cubic action on positions and polar
vectors. For an axial vector its divergence is a pseudoscalar, whose zero
constraint is also invariant. At even N it has additional high-frequency
zeros at components k_j in {0,pi}; no continuum claim discards those modes.

Swap two whole records at x and x+e_i. If the feature difference between
the arriving and departing label is d, then

    Delta F(z)=d [1_(z=x)-1_(z=x+e_i)].

For the unhalved divergence 2D, the three columns mapping d into its
charge impulse have Gram matrix 4I. The column for component i has support
x-e_i,x,x+e_i,x+2e_i, with unit coefficients. A component j!=i has support
x-e_j,x+e_j,x+e_i-e_j,x+e_i+e_j. Those three supports are disjoint for
N>=5. Each column has four unit-magnitude entries. Therefore exactly

    sum_z |Delta D F(z)|^2=|d|^2.                         (1)

For the original fifteen-state label features (e,b), this gives

    ||Delta D e||_2^2+||Delta D b||_2^2
        =|e(a)-e(d)|^2+|b(a)-b(d)|^2.                    (2)

The combined feature map distinguishes all fifteen labels. A swap of
distinct labels has a positive impulse in (2), regardless of the external
read context or its rate. This statement is only about this site-feature
encoding and a single two-site event. It does not rule out other gauge
encodings, collective events, effective constraints or the previously
proved finite-mode preparation. The constructive alternative below changes
the microscopic event support explicitly.

### 2. Four permanently labeled records make a closed loop

For a center c and the xy plane, put four A records at

| Site | Immutable vector feature |
|---|---|
| c-e_y | +e_x |
| c+e_x | +e_y |
| c+e_y | -e_x |
| c-e_x | -e_y |

Every other site is vacant. Call this field L_c. Direct substitution gives
D L_c=0: at the four corners c+/-e_x+/-e_y, the two incident contributions
cancel; there are no other nonzero charges. Its opposite circulation also
has zero divergence. This uses four distinct occupied sites and one record
per site. No feature is a superposition of two records.

Exchange the two opposite horizontal sites simultaneously with the two
opposite vertical sites. The resulting field is -L_c, but each individual
record kept its own label and merely changed position. Doing just one of
the two swaps produces a nonzero charge; the combined event matters.

Translate all four records by any one nearest-neighbor displacement a.
The old and new sets of four sites are disjoint: in an unwrapped local footprint the old cross has one
parity of x+y+z, while translation changes it; N>=5 prevents a modular alias. Require every destination
vacant. Each record makes a nearest-neighbor hop and all four hops happen
as one event. The field becomes L_(c+a), so the divergence stays zero and
the old four sites are vacant. This is a bounded eight-site update, not a
sequence of separately Gauss-preserving single-record hops.

The same formulas work in all three coordinate planes and for either
circulation. The entire template family is closed under all signed cubic
actions. A reflected axial feature changes the circulation assignment;
both assignments are already present.

### 3. A two-sector alphabet with capacity, transport and fresh formation

For this construction choose vacancy plus two six-label axis orbits:

    A_(+/-i): e=+/-e_i, b=0;
    B_(+/-i): e=0, b=+/-e_i.

This is a thirteen-state alphabet. In particular the B cube orbit of the
earlier fifteen-state model is replaced by an axis orbit. The new alphabet
and the collective events are supplied additional choices. Neither the
old full-field formulas nor its positive-floor mixing theorem can simply
be transferred to this generator.

For each species, plane, circulation and center, permit:

1. Translation of the four-record loop to four vacant destination sites,
   at a fixed symmetric rate kappa for each nearest-neighbor displacement.
2. Reversal by the opposite-site record permutation, at a fixed rate nu.
3. Formation of a new four-record loop when all four template sites are
   vacant, at microscopic rate beta/N per species/plane/circulation.

Templates examine actual labels, not a permanently assigned loop identity.
In a dense configuration they can overlap; every enabled event must satisfy
the full footprint conditions. The finite generator is the sum of these
bounded local event rates. Simultaneous Poisson events have probability zero,
so conflicting enabled templates do not violate site capacity.

Every transport or reversal event is a permutation of whole records and
vacancies. Formation creates four new record identities; it does not remove
or relabel an existing record. Every event has zero change in both D e and
D b. Thus these two entire microscopic charge fields are conserved exactly,
including during birth. Starting from empty sites gives the source-free
sector at every finite time and volume, without conditioning an ensemble.

An explicit departure-and-reformation sequence is:

    empty -> A loop at c -> same four A records at c+e_z
          -> four new B records at c.

The eight final records occupy eight different sites. The original four
labels and identities are unchanged. Both divergence fields vanish at
every step. All three events have positive rates when kappa,beta>0, so this
is an allowed finite history, not merely a proposed final configuration.

This does not prove endless formation in finite volume: the record count
is monotone and bounded by the number of sites. Nor does it prove ergodicity
or the absence of jammed configurations in the infinite system.

### 4. Exactly invariant conditional ensembles for conservative moves

Turn births off. Each translation has the reverse translation with the
same kappa, and each reversal is its own inverse. All events preserve every
label count. Consequently an arbitrary homogeneous positive product law
has equal probability on the configurations before and after an event.
Eventwise detailed balance proves its invariance under these conservative
moves, even though the generator is highly reducible.

Condition that product on any nonempty joint charge sector (D e,D b).
The sector is closed under the generator and the same pairwise equalities
still hold, so the conditional law is invariant. The source-free sector is
nonempty because it contains the vacuum. It also contains the explicitly
constructed nonempty loops. Product stationarity here is not a proof of
mixing within a sector, a canonical spectral gap or a Coulomb phase.

Births preserve charges but not the conditional product law established
for conservative moves. A density-only product closure is not justified.
For example, on macroscopic Euler time, the exact mean record-count rate
per site for a translation-invariant law is

    rho'(t)=16 beta sum_(three coordinate planes)
                  P(the four sites of that plane's cross are vacant).

There are two circulations and two species for each cross and four records
per event. At empty start rho'(0)=48 beta. Replacing each four-vacancy
probability by (1-rho)^4 would be an additional approximation; it has not
been made in this calculation.

### 5. Exact Fourier form factor and the cost of small local loops

With convention exp(-i k.x), the xy loop has Fourier feature

    Lhat_c(k)=2i exp(-i k.c)
                    [sin(k_y)e_x-sin(k_x)e_y].           (3)

The centered divergence symbol is i s(k), where s_j=sin k_j, so
s(k).Lhat_c(k)=0 exactly. Also

    |Lhat_c(k)|^2=4[sin^2(k_x)+sin^2(k_y)].               (4)

For a fixed continuum mode K with k=K/N this is O(N^-2). Each fixed-size
loop has zero total feature and a dipolar long-wavelength form factor.
An independent dilute gas of such bounded loops with bounded density and
orientation variance therefore has vanishing N^(3/2)-normalized vector
variance at a fixed continuum mode. This conditional dilute-gas observation
does not classify the interacting model: long loops or long-range
correlations of the local loops could change that conclusion.

The birth martingale can be bounded without assuming product independence.
Let the Fourier fluctuation normalization be N^(-3/2). At a fully vacant
configuration, the exact instantaneous covariance of the birth increments
in each vector sector is

    Q_E(k)=Q_B(k)=8 beta [|s(k)|^2 I-s(k)s(k)^T],
    Q_EB(k)=0.                                          (5)

Each plane has two opposite circulations. Summing their outer products
in (3) gives (5). Under an arbitrary law, each template is multiplied by
its vacancy indicator; hence its predictable covariance is bounded above
by the matrix in (5), in the positive-semidefinite order. The combined
instantaneous trace is at most32 beta |K|^2/N^2. Its integral to a fixed
macroscopic time T is at most32 beta T |K|^2/N^2.
Thus these loop births have no leading vector birth noise at that scale,
and the discrete Gauss projection vanishes exactly at every N.

This bracket calculation alone is not a fluctuation limit: tightness,
drift replacement, state selection and possible long-range correlations
remain unproved. In particular, it cannot be combined with the earlier
product fluctuation theorem after changing that theorem's generator.

### 6. The simplest isolated-loop dynamics is diffusive

With births disabled and only one loop present, its center jumps by each
of the six unit displacements at rate kappa. Reversal does not change the
center. Its exact Fourier generator eigenvalue is

    -2 kappa sum_i(1-cos k_i).

At k=K/N it becomes a heat symbol on N^2 time, while N time gives zero
limiting motion of the center. This exact one-loop test does not provide
a ballistic transverse wave. It is a useful distinction: compatibility
of permanent records, site reuse and a microscopic Gauss constraint is
established for the supplied events; a wave-supporting collective phase
of those events is still a separate research problem.

### 7. Evidence and next decisions

`microscopic_gauss_record_loop_check.py` has thirteen completed exact local
and symbolic control groups. It tests all630 ordered distinct-label swaps
in the original fifteen-state menu, the Gram identity, all six translations,
an explicit history with persistent record IDs, all48 signed cubic template
actions, Fourier form factors and birth covariance, product weights and the isolated-loop symbol.
No failed execution was discarded. These are primary controls, not an
independent review or a proof of a continuum gauge theory.

Next: separately reconstruct the collective construction; analyze whether
the admissible Gauss sectors have a nontrivial long-wavelength covariance
and a controlled mixing mechanism; determine whether coupling the two
sectors can give a first-order curl evolution without importing it. The
new rates and alphabet have no axiom-selection argument. Quantum dynamics,
physical charges, field units, Lorentz symmetry and gravity remain open.

## Part B. Static phase of the permanently labeled axis-loop model

2026-09-21. Primary derivation with completed selective independent
finite-volume and polymer-proof review. Two scope clarifications were
corrected and acknowledged; there is no formal audit verdict.
This note specifies an equilibrium ensemble for the conservative model;
it does not assert that the irreversible formation process reaches it.

### 1. Ensemble and exact current representation

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

### 2. Exact low-order finite-volume coefficients

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

### 3. Exact compact-phase representation, with the capacity factor intact

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

### 4. Exact hard-core polymer representation

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

### 5. A deliberately conservative uniform convergence domain

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

### 6. Exponential connected correlations in the controlled ensemble

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

### 7. Exact Gauss constraints plus clustering determine the infrared order

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

### 8. Research consequence and remaining obligations

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

## Part C. The constant-rate loop birth has a formation-locality gap

2026-09-21. Primary exact diagnostic. This examines the new thirteen-state
construction against the current Admissibility wording; it does not alter
the loop, transport or equilibrium identities already checked.

The loop construction preserves permanent labels, single-site capacity and
both exact Gauss constraints. Those facts do not establish the full set of
framework axioms. In particular, identifying its Poisson birth generator
with the complete forming-record probability law exposes a nearest-neighbor
odds problem. The following pair of source-free backgrounds proves it.

### 1. Compute the actual conditional birth law

Write v(y)=1 when y is vacant. Each allowed four-record template forms at
the same microscopic rate beta/N. Conditional on a birth at vacant x,
the rate for either sign of axis i, in either species, is

    h_i(x)=(beta/N) sum_(j!=i) sum_(sigma=+/-1)
       v(x+2sigma e_j) v(x+sigma e_j+e_i) v(x+sigma e_j-e_i).   (1)

These are precisely the four templates placing that signed label at x.
The two circulations give the same vacancy conditions. Species changes
also leave those conditions unchanged. Therefore, when a birth at x is
possible, its conditional probability for any particular label of axis i is

    p_(species,+/-i)(x)=h_i(x)/[4 sum_j h_j(x)].               (2)

The formula probes record sites at distance two from x. Such dependence
could still cancel after normalization, so the two backgrounds below test
the normalized law, not just an unnormalized rate.

### 2. Equal nearest-neighbor conditions, different forming-label odds

Take x=0 on a torus N>=7. Background A is empty. Background B contains
one A-species loop in the yz plane centered at (2,0,1), namely

    (2,0,0): +e_y,    (2,1,1): +e_z,
    (2,0,2): -e_y,    (2,-1,1): -e_z.

Background B is exactly Gauss-free and is reachable by one permitted birth
from empty. At x and all its six nearest neighbors
both backgrounds are vacant. Only the first listed record intersects any
candidate loop birth through x: it is the blocker at 2e_x. Consequently

    A: (h_x,h_y,h_z)=(4,4,4) beta/N,
    B: (h_x,h_y,h_z)=(4,3,3) beta/N.                         (3)

In A all twelve label probabilities equal 1/12. In B a particular signed
x label in either species has probability 1/10, while a signed y or z
label has probability 3/40. The nearest-neighbor record conditions are
identical, but the actual conditional formation law differs.

The Admissibility axiom says that the distribution at a site is determined
by its nearest-neighbor conditions. Its current reading concerns which
possibility a forming record locks, conditional on formation there. Under
that identification, the constant-rate loop birth is not a realization of
that requirement. Calling the remote factor only a formation-site rate
does not fix it: a common positive scalar multiplies every h_i and cancels
from (2), leaving the unequal probabilities.

### 3. Scope and constructive next obligations

This is a counterexample to one fully specified formation kernel. It is
not a proof that exact Gauss constraints and nearest-neighbor formation are
incompatible in general. Its conservative moves and constrained invariant
ensembles are unaffected. The successful departure/reformation history is
still a legal history of that supplied process, but the process must not
be advertised as satisfying all the minimal axioms.

A repair must specify a joint collective birth law whose single-site
conditional probabilities obey the same nearest-neighbor rule at every
background where formation occurs. Possible directions include compensated
template rates, more event types, a different microscopic Gauss encoding,
or a model with explicit charge sources rather than D E=D B=0 everywhere.
None has been supplied or ruled out by this diagnostic. A change in the
Admissibility axiom is not assumed or requested.

There is a useful geometric restriction on one tempting repair. A finite
nonzero divergence-free axis field on Z^3 supported in a fixed finite set S
cannot assign every axis at every occupied site with positive probability:
at a site with maximal first coordinate, a nonzero first component would
produce a charge one step beyond that maximal plane with no compensating
record. Hence that component is zero at every such boundary site. A fixed
finite birth footprint with a full isotropic marginal at each of its sites
is impossible under this particular source-free encoding. Randomizing the
footprint may avoid this restriction; the constant-rate version shows why
vacancy conditioning then needs a separate calculation.

`loop_birth_locality_check.py` independently enumerates every template
containing x, checks both backgrounds' exact divergence and nearest-neighbor
identity, and compares the conditional rational probabilities. Its finite
checks supplement the explicit calculation (1)-(3). The current four-axiom
source is `docs/MINIMAL_AXIOMS_2026-06-29.md`, SHA-256
93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753.

## Verification and review boundaries

The runner executes four byte-preserved author checkers in a temporary
workspace: finite moves and form factors, exact fugacity enumeration,
component-polymer controls, and normalized formation-locality odds. Their
34 groups supplement the proofs; the wrapper adds one declared-source check.
The general polymer convergence and thermodynamic-limit arguments are not
inferred from a finite test count.

Three independent review packets accompany the note. The loop packet
reconstructed the elementary dynamics and fugacity coefficients before
comparison. The polymer packet checked the complete proof, including the
specified cluster-expansion hypothesis; the general-observable norm and
vacant-box boundary conditions were corrected and acknowledged. The third
packet independently reconstructed the locality counterexample before
opening the corresponding author checker; its additional local-curl
results are not claimed in this note. Original read boundaries and failures
are preserved. No independent audit verdict or retained grade is supplied.

The cluster-expansion reference is Daniel Ueltschi,
[Cluster expansions and correlation functions, arXiv:math-ph/0304003v3](https://arxiv.org/abs/math-ph/0304003),
Theorem1 and its proof. The local review records the exact PDF identity;
the third-party PDF is not bundled. The packet verifier reports that explicit
external-reference exclusion separately from its verified bundled bytes.

Run from the repository root:

```bash
python3 scripts/mobile_records_gauss_loops_static_phase_and_formation_locality_2026_09_21.py
python3 .claude/science/mobile-record-gauss-loops-20260921/verify_evidence.py
```

See the [evidence README](../.claude/science/mobile-record-gauss-loops-20260921/README.md)
for source identities, complete reports and reproduction limits. Full pipeline,
strict audit lint and combined changed-evidence validation remain for an
integrated landing candidate. No primitive, editable prompt or audit verdict
is changed by this milestone.
