# A finite quantum completion criterion for partially allowed gauge hops

Date: 2026-09-22. Status: author conditional theorem and exact finite controls;
independent check pending. All Hilbert spaces, Hamiltonians, monitoring and
birth instruments are supplied. This is not a native-site or photon theorem.

## 1. What replaces unrestricted unitary hopping

The earlier completion theorem required every neighboring occupied/vacant
pattern to be connected by an invertible transport map. A bounded U(1) field
does not satisfy that condition: some electric-field configurations block a
hop. Nevertheless, the allowed part of each hop is a partial bijection. For
a fixed changed occupation pattern, it maps distinct input field states to
distinct output field states, while preserving the entire moving record.

This suffices to propagate stationary populations along the allowed basis
graph even when the density operator retains electric-field coherences.
Occupation monitoring alone is used. Electric-field measurement is not a
premise of the theorem below.

## 2. Precise finite statement

Decompose a finite Hilbert space as a direct sum

    H = direct_sum_(c in C) K_c.

Each configuration c carries an occupied-site pattern n(c), a vacancy count
Q(c), and a finite internal record space K_c. The projectors n_x act as the
corresponding zero or one on each entire K_c. Configurations with the same
occupied pattern may be different gauge states. They may be coherently
superposed; the decomposition is a mathematical basis organization.

Supply a Hermitian Hamiltonian H=H0+Hhop. H0 commutes with every n_x. The
off-pattern blocks of Hhop obey this partial-bijection hypothesis:

For any two distinct occupation patterns S,S', the nonzero maps between
configuration blocks are a matching. Each source c in S maps to at most one
target c' in S', and each target has at most one source. Each nonzero map is
t_(c'c) U_(c'c), with t nonzero and U a unitary identification of the complete
internal spaces. The reverse map is its adjoint. Hhop preserves vacancy count.

Supply Hermitian monitoring jumps sqrt(d_x) n_x, all d_x>0. Birth jumps obey
[Q,J_alpha]=-2 J_alpha and

    Gamma = sum_alpha J_alpha^dagger J_alpha
          = direct_sum_c gamma_c I_(K_c),  gamma_c>=0.

Each gamma is finite. Birth acts only when vacancies are present. Full
occupation is invariant under the Hamiltonian and monitoring and annihilated
by all birth jumps. Define the undirected allowed-hop graph on C using the
nonzero t U maps. Assume the initial state lies in an even-vacancy invariant
sector.

**Sufficient connectivity condition.** Every connected component of the
allowed-hop graph with Q>=2 contains at least one c with gamma_c>0.

**Theorem.** Under these hypotheses every initial density operator in the
specified sector has full-occupation probability tending to one. Each fixed
finite model has an exponential upper bound on its survival tail and a finite
mean completion time. H0 can be any occupation-preserving Hermitian operator,
including operators that mix gauge configurations within a pattern.

The graph condition is about complete configurations, not merely whether the
underlying spatial lattice is connected. A field-dependent forbidden hop is
an absent graph edge. A separate stochastic process is not substituted for
the quantum generator.

## 3. Proof with coherent internal and field blocks retained

For any stationary density rho,

    0 = d Tr(Q rho)/dt = -2 Tr(Gamma rho).

Positivity implies Gamma^(1/2)rho=0. In particular J_alpha rho=0 for every
alpha, and every birth dissipator vanishes. The Hilbert-Schmidt pairing with
the remaining stationary equation gives

    0 = -1/2 sum_x d_x ||[n_x,rho]||_HS^2.

Therefore rho commutes with every occupation projector, and then with H.
It is block diagonal in occupation pattern, but it need not be block diagonal
in c within a pattern.

Consider an allowed hop c->c' between distinct patterns. The (c',c) block of
[H,rho]=0 contains no H0 contribution. By the partial-bijection hypothesis,
there is exactly one relevant source in the first product and exactly one
target in the second product. Thus even in the presence of other same-pattern
coherences it reads

    t_(c'c) U_(c'c) rho_(c,c)
       - rho_(c',c') t_(c'c) U_(c'c) = 0.

Consequently rho_(c',c')=U rho_(c,c) U^dagger and
Tr rho_(c',c')=Tr rho_(c,c). These nonnegative weights are equal along every
connected component. If gamma_c>0, stationary birth loss forces that block's
weight to zero. The connectivity condition therefore removes every component
with two or more vacancies. Even parity leaves only full occupation.

All stationary densities are fully occupied. Since full occupation is an
absorbing subspace, its probability is monotone. Finite Cesaro averages have
stationary limit points, proving convergence of that probability to one.
Compressing the semigroup to the nonfull subspace gives a finite-dimensional
completely positive trace-nonincreasing semigroup T_t. Its survival effect
T_t^*(I) decreases to zero in norm. Select t0>0 and c<1 with
||T_t0^*(I)||<=c; then Pr(tau>n t0)<=c^n and E[tau]<=t0/(1-c).

As in the earlier monitored theorem, an initial total-vacancy measurement
with discarded outcome leaves full-occupation statistics unchanged by phase
covariance. This specifies the counted first-completion distribution for
initial coherences between different vacancy sectors. No unmeasured coherent
history is assigned a unique classical first-hitting time.

## 4. Application to the finite spin-half U(1) model

Matter at each vertex has states 0,+,-. Every reference-oriented link has
E=+/-1/2. In a fixed Gauss sector, its electric-field bit configuration fixes
the matter charge by div E-Q=G. Keep only charges in {0,+1,-1}, and identify
zero charge with vacancy in this supplied model. A label c is the full valid
electric-field configuration and its consequent charge pattern.

On a simple spatial graph, two distinct vacancy patterns joined by one hop
identify a unique edge: they differ exactly at its endpoints. A legal hop
flips that edge's electric bit and moves the record into the vacant endpoint.
For fixed source and target occupation patterns this is a partial bijection
of the valid c states, with its inverse given by the reverse hop. An attached
internal record factor is transported unitarily in full. Hence the theorem's
off-pattern hypothesis holds.

Summing the two neutral-pair birth orientations on an edge gives
beta q_x q_y tensor I_link. If all edge birth rates are positive, gamma_c>0
precisely when c has neighboring vacancies. More generally one checks vacancy
contact on the specified source edges. The local algebra and definitions are
in GAUGE_COVARIANT_PERMANENT_RECORD_DYNAMICS.md.

Thus if every ordinary-hop component has a configuration with a birth source,
occupation monitoring gives quantum completion for any occupation-preserving
H0. In particular, adding pure field loops or occupied-record circulation
cannot invalidate this sufficient statement, regardless of their strengths:
they have no matrix element between distinct occupation patterns.

## 5. Exhaustive controls on two finite open boxes

The boxes have shapes 2x2x2 and 2x2x3. Embed them as induced subgraphs of the
cubic lattice, retain the internal links, and hold all outside electric fields
fixed at +1/2. Omit movement and birth across the boundary. Initially all
internal links are also +1/2 and all matter is vacant. If m_e=1 marks an
internal link flipped negative, the physical charge is Q=-B m, with B the
oriented incidence matrix. The unchanged outside flux cancels the initial
internal divergence. This specifies a finite boundary sector, not a periodic
lattice or a translation-invariant infinite-volume state.

gauge_configuration_connectivity_screen.py exhausts all 2^E link words,
retains exactly |Q_x|<=1, builds every legal hop and birth, and computes
components. Direct inverse and Gauss checks accompany the graph enumeration.

| Box | Link words | Valid basis states | Ordinary-hop components | Nonfull components without birth contact |
|---|---:|---:|---:|---:|
| 2x2x2 | 4096 | 375 | 28 | 0 |
| 2x2x3 | 1048576 | 25386 | 234 | 0 |

The allowed-hop criterion therefore proves full-occupation convergence for
every initial quantum state in either complete finite Gauss sector, with
uniform nonzero hopping coefficient and arbitrary positive monitoring and
birth rates. Every valid state is also reachable by a sequence of hops and
births from the vacant positive-flux state. These are finite controls; they
do not prove a volume-uniform rate or a statement for all cubic boxes.

As a separate author implementation path, gauge_occupation_observability_check.py
constructs the Hamiltonian including correct multiplicities of forward and
reverse occupied-record cycles. It generates the subspace spanned by contact
states under H and occupation-pattern projectors, without measuring fields.
Full rank over the prime 1000003 certifies full rank over the rationals, since
all matrices have integer entries. Deficient modular rank would be inconclusive.
For the two boxes the nonfull-sector ranks are respectively

    (1,30,156,170),
    (1,82,1427,7394,11684,4598).

Each equals its full Hilbert-sector dimension. The check covers hopping alone,
hopping plus field loops, all three terms with coefficients (1,1,1), and
coefficients (2,3,5). It is a load-bearing calculation by the same author, not
an independent-agent check. The analytic partial-bijection proof explains why
the hopping-only certificate already suffices in the presence of arbitrary H0.

## 6. Larger controls and remaining scope

Do not extrapolate the two boxes to every finite graph. The separate exact
gauge_open_box_jam_screen.py constructs matching states in open cubic boxes
of side 4,6,8 with two interior vacancies, no ordinary hop, no birth contact,
and no elementary field plaquette move. Their integer matching lists and
empty-start ordered birth sequences are preserved in its results. They fail
the sufficient ordinary-hop graph criterion. This is compatible with the
theorem rather than a counterexample to it.

The occupied-record cycle extension can act inside a fixed occupation pattern.
It may release components that fail the ordinary-hop criterion; deciding that
case needs the full H-and-monitoring invariant-subspace test. General graph
connectivity of arbitrary Hamiltonian terms is not sufficient to exclude
coherent dark states. No all-state conclusion for the enlarged periodic
three-dimensional model is made here.

The model supplies a finite field, a matter carrier, a generator, monitoring
and source rates. The result separates a checkable quantum-completion
obligation from native encoding and long-distance phase questions. Neither
those hypotheses nor a physical field phase follow from the framework axioms
in this work. This draft includes scoped negative controls whose publication
packet remains subject to the current no-go discipline gate.
