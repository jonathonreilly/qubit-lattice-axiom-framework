# Independent gauge-record reconstruction

This packet uses only the neutral task specification, `INPUT_WITNESS.json`
and the already checked corrected occupation-monitoring theorem. No new
author gauge note, script, output, seal or campaign checkpoint was opened.
The arguments below reconstruct the new gauge steps rather than assuming
the previous matter-only theorem applies unchanged.

**Results:** (A) the finite Z2 model completes from every physical initial
density, with a model-dependent exponential occupation-survival bound and
finite mean. (B) the spin-half-link model has the supplied nonfull closed
support, and that support is accessible from empty. Contractible field loops
and diagonal monitoring do not remove it. (C) the supplied occupied-record
cycle releases this particular witness: two coherent routes add, giving a
nonzero leading birth amplitude. This is positive completion probability
from a specified state, not an all-state completion theorem.

## A. Z2 gauge fibers retain the completion proof

Use the stated finite connected simple graph, even V, one vacancy/occupation
matter qubit at each vertex and one gauge qubit on each edge. All rates and
Hamiltonian coefficients are finite; hopping couplings are real and nonzero,
each d_x>0, and at least one birth edge has beta_e>0. Work in the common
G_x=+1 subspace, where

    G_x=(-1)^n_x product_(e incident x) Z_e.

A hop or birth flips matter parity at both endpoints and flips the edge Z
through X. The two signs cancel in each endpoint Gauss operator. Thus every
hop and birth commutes with all G_x; monitoring and the stipulated H0 do too.
With N_r=sum n_x and V-N_r the vacancy count,

    [N_r,H]=[N_r,D_x]=0,    [N_r,J_e]=2J_e,
    J_e^dagger J_e=beta_e q_x q_y,
    d E[V-N_r]/dt=-2 sum_e beta_e Tr(q_x q_y rho).

Crucially X is unitary, so the birth loss has no gauge-state kernel when the
matter endpoints are vacant. Multiplying all Gauss constraints gives
(-1)^N_r=1. Since V is even, every physical state has even vacancy parity.
For odd V, full occupation would not lie in this physical Gauss sector.

For an occupation pattern n, the gauge-Z constraints are the mod-two incidence
equations with boundary n. On a connected graph their image consists exactly
of even-cardinality vertex sets. Every allowed pattern therefore has a
nonempty gauge fiber of dimension `2^(|E|-V+1)`. An allowed vacancy hop across
e identifies the two neighboring fibers by X_e, a unitary map. The argument
allows arbitrary superpositions and entanglement in and between these fibers.

Here is a direct completion proof. For a stationary physical density, the
monotone-count identity and positivity force q_x q_y rho=rho q_x q_y=0 on
every birth edge. Every birth dissipator then vanishes. Pairing the remaining
stationarity equation with rho in Hilbert-Schmidt inner product gives

    0=-(1/2) sum_x d_x ||[n_x,rho]||_HS^2.

Thus rho is block diagonal in the matter occupation patterns, with fully
quantum gauge blocks rho_S. The off-pattern block of [H,rho]=0 for a vacancy
exchange S->S' is

    kappa_e (X_e rho_S-rho_S' X_e)=0.

H0 contributes no off-pattern block. Hence rho_S'=X_e rho_S X_e and their
traces agree. The fixed-cardinality vacancy graph is connected, since edge
transpositions of a connected graph generate all vertex permutations. At any
vacancy count at least two, some pattern contains a birth edge and has zero
weight; all patterns of that count must then have zero weight. Only full
occupation supports stationary densities.

Full occupation is invariant. Its probability is monotone, and finite-
dimensional Cesaro limit points are stationary, so its probability tends to
one for every physical initial density. The nonfull corner is a CP,
trace-decreasing semigroup T_t. Its survival effect T_t^*(I) tends to zero in
operator norm. Choose t0>0 and c<1 with ||T_t0^*(I)||<=c. Then

    Pr(tau>t) <= c^floor(t/t0) Pr(tau>0),
    E[tau] <= t0 Pr(tau>0)/(1-c).

This proves a finite-model exponential tail and finite mean, with no uniform
volume/rate claim. For coherences between count sectors, initially measuring
N_r and discarding the result leaves occupation statistics unchanged by number
phase covariance; the resulting jump trajectories give the same distribution.
No unmeasured first-hitting interpretation of such superpositions is assumed.

Full occupation need not be a unique stationary quantum state. The full
physical gauge fiber has dimension `2^(|E|-V+1)`. When H0=0, every density on
it is stationary; otherwise H0 can keep acting there. Monitoring n_x does not
measure these full-occupation gauge degrees of freedom. Connectivity, nonzero
hop maps, even physical parity, an active birth edge and occupation-resolving
monitoring are sufficient hypotheses; this is not a classification of all
weaker hypotheses under which completion could still hold.

The exact C4 control eliminates the Gauss constraints without removing
coherences. Its physical Hilbert dimension is 16, full-occupation dimension 2,
and Liouvillian dimension 256. At unit hopping/monitoring and H0=0, both
all-edge births and one-edge births have stationary-operator nullity four,
precisely the full-sector operator dimension. On the 14-dimensional nonfull
space the exact adjoint mean operator solves L_trans^*(T)=-I and has all
leading principal minors positive. From all vacancies and all Z positive,
the means are respectively **7/4** and **275/24**. These are full physical
quantum controls, not a classical population restriction.

## B. Spin-half links: identities and a genuinely closed nonfull support

For a fixed positive-axis link x->y, let E have eigenvalues +-1/2 and
U=|+><-|, so [E,U]=U. Positive matter moving x->y uses U^dagger, and negative
matter moving x->y uses U. Their adjoints implement the reverse hops.
The changes in div E equal the changes in Q at each endpoint. The stipulated
pair births and every oriented pure-field closed loop also commute with
G=div E-Q. Hopping and pure-field loops preserve N_r=sum Q_x^2; each pair
birth raises it by two and preserves total charge.

Writing P_+ and P_- for the link E projectors, the exact loss identities are

    J_+^dagger J_+=beta q_x q_y P_-,
    J_-^dagger J_-=beta q_x q_y P_+,
    J_+^dagger J_+ + J_-^dagger J_-=beta q_x q_y.

The total hazard of a vacant edge is **beta, not 2 beta**, when both supplied
channels have coefficient sqrt(beta). Accordingly the vacancy-count drift is
`-2 beta sum_edges Tr(q_x q_y rho)` at equal rates. The independent 18-state
local matrix check verifies these as operator identities, including the
Gauss and number commutators.

Let M be the directed subgraph of negative links, and F=|M|. The all-positive
periodic field has zero divergence, so Gauss gives

    Q_x=indeg_M(x)-outdeg_M(x),
    N_r=sum_x |Q_x| <= sum_x [indeg_M(x)+outdeg_M(x)]=2F.

Equality requires at every vertex either indegree or outdegree to vanish.
Since |Q_x| is at most one, an occupied vertex then has precisely one incident
negative edge, and a vacant vertex has none. Thus F=N_r/2 is exactly the
negative-link matching sector. A negative link points from a negative record
to a positive record. For fixed Q, the quantum sector is the span of all such
matching configurations, not a prescribed diagonal mixture. Positivity also
makes zero expectation of 2F-N_r imply support in this kernel.

**This sector alone is not hopping invariant.** For example, a single negative
link 000->100 creates charges - at 000 and + at 100. That positive record can
hop to 200 through a positive link, increasing F from one to two while N_r
stays two. The supplied witness needs its additional charge-pattern property.

The neutral N4 witness has F=31, N_r=62 and holes h=000,111. It is physical,
and all negative links form the supplied matching. For either hole and each
axis i it satisfies

    Q_(h-e_i)=-1,    Q_(h+e_i)=+1.

Every link incident on a hole is positive in every matching with this Q.
The negative record at h-e_i cannot move forward into h: it would need to
raise an already positive link. The positive record at h+e_i cannot move
backward into h for the same reason. There are no other vacancy hops. The
holes are not adjacent, so every birth channel annihilates this sector.

A pure-field loop along a traversal with signs s_l changes E_l by s_l
(or by -s_l for its adjoint). For a contractible loop each axis has zero net
signed displacement, hence

    Delta F=-sum_l s_l=0.

Such operators preserve Q and F, and therefore preserve the matching sector
at this fixed witness Q. Even if they rearrange its matching, all hops and
births remain blocked. Arbitrary diagonal field/charge Hamiltonians and
diagonal monitoring preserve the same support. This establishes a closed
nonfull quantum subspace, including its coherences. The reason the proof in
A fails here is the kernel of the truncated U/U^dagger hopping maps.

The elementary field plaquettes actually annihilate this matching sector:
in either orientation, two adjacent links would have to be negative. Larger
contractible loops need not annihilate it. Among 768 explicitly tested
oriented six-edge channels, six were enabled on the witness. Every one
preserved its charge pattern, matching property and blocked holes. Thus the
closure argument is stronger than declaring one basis vector frozen.

The contractibility boundary matters. A winding loop with winding vector w
has Delta F=-N sum_i w_i in one orientation. The checked positive-x ring
000->100->200->300->000, applied with all links lowered, is enabled on the
witness. It changes F from 31 to 35 and allows the positive record 100 to
hop into 000. A plaquette crossing a periodic seam is still contractible;
it is not this winding operation. No completion theorem with general winding
operators is inferred from this one escape.

### Empty-start access is a separate argument

Start with all matter vacant and every link positive, a physical state. Apply
J_- once on each of the 31 supplied negative matching edges, in a fixed order.
Their endpoints are disjoint. The zero-waiting jump product produces exactly
the supplied matter charges and field mask. All required rates must be
positive; uniform positive births on all links suffice.

The actual trajectory argument uses an open region of small positive waiting
times: finite-dimensional no-jump propagators are continuous, so projection
of the trajectory amplitude onto the closed sector stays nonzero there.
The region has positive measure and positive jump density. The sector cannot
subsequently lose probability under hopping, contractible loops, births or
diagonal monitoring. Therefore the empty state has strictly positive
probability of never completing in model B. This is a finite supplied-model
countercontrol, not a large-volume vacancy phase or a claim about arbitrary
initial fields. No zero-duration trajectory was assigned positive probability.

## C. Occupied-record cycle: Gauss, transport and coherent escape

Number the square vertices cyclically and let s_i record whether its i-th
traversal follows the fixed link orientation. For an occupied input q_i=+-1,
the forward K_C rotates it to q_i'=q_(i-1) and changes that link by

    Delta E_i=-s_i q_i.

Its divergence change at v_i is

    s_i Delta E_i-s_(i-1) Delta E_(i-1)=q_(i-1)-q_i.

This is exactly Delta Q_i. Thus K_C and its adjoint commute with all Gauss
operators. They transport the existing charge labels cyclically, conserve
each global label count and N_r, and annihilate a square with any vacancy.
They are partial isometries conditioned on available link capacity, not
unconditional permutations of the field. The Hamiltonian K_C+K_C^dagger
is Hermitian. All 16 allowed fully occupied local cycle inputs were checked
for Gauss preservation, injectivity and content permutation.

On the specified square

    001 -> 002 -> 102 -> 101 -> 001,

the initial charges are (+,+,+,-) and s=(+,+,-,-). All required link operations
are legal. The cycle produces (-,+,+,+), changes F from 31 to 33, and leaves
the holes at 000,111. The specified negative-record hop 001->000 and
positive-record hop 101->111 are then both legal and commute with each other.
They leave adjacent holes 001,101 and F=35. The last edge 001->101 is negative,
so its J_+ raises the link and fills the two holes. The final physical state
has N_r=64 and F=34. Its record labels have been transported or newly born;
none was overwritten by these operations.

### A path is not yet a quantum amplitude

Let |w> denote the supplied witness, |u> the specified state just before the
last birth, and |f> its full final output. Count each elementary geometric
face once as g(K_C+K_C^dagger), and each hopping term once with its coefficient.
Let kappa_1,kappa_2 be the coefficients of the two specified hops. Equivalently
g is the actual matrix element of this single allowed cycle transition;
duplicating face orientations in a sum would require adjusting that rate.

The independent enumeration includes all 192 elementary record cycles and
field plaquettes, both orientations, and every allowed vacancy hop. It keeps
separate channels even if they land on the same basis state. It finds

    <u|H|w>=<u|H^2|w>=0,
    <u|H^3|w>=2 g kappa_1 kappa_2.

There are exactly two length-three routes: the specified cycle first, then
the two hops in either order. They have the same product of amplitudes and
add rather than cancel. Analytically at least two hops are needed to move
the holes from {000,111} to {001,101}; their assignment and edges are unique.
The remaining four changed links fix the square. The initial state has no
legal hop, and a contractible pure-field operation leaves a blocked matching
at this Q. Thus the third operation must be that record cycle, and no shorter
route or competing three-operation route is missed. Adding diagonal H0 or
diagonal no-jump losses cannot reduce this order. The same observation rules
out an additional contractible pure-field loop contributing at this order.

For the no-jump propagator A=-iH-(1/2)sum J^dagger J, including any specified
finite diagonal monitoring loss, the last-birth amplitude is consequently

    <f|J_+ exp(At)|w>
      = i sqrt(beta) g kappa_1 kappa_2 t^3/3 + O(t^4).

Its target-resolved no-prior-jump birth density is

    beta g^2 kappa_1^2 kappa_2^2 t^6/9 + O(t^7).

It is strictly positive at sufficiently small positive t when these
coefficients are nonzero. Integrating this contribution gives a positive
completion probability, with leading contribution
`beta g^2 kappa_1^2 kappa_2^2 t^7/63`. It is a lower contribution to full
occupation, not necessarily the entire first-birth law.

To transfer this positive event from the specified witness to an empty-start
history, use the 31-birth word above and then one fixed small interval where
this final amplitude is nonzero. In the zero-prefix-wait limit the composite
amplitude is a nonzero scalar times the one just computed. Continuity gives
an open region of positive prefix waiting times with nonzero amplitude. This
avoids assuming a measurement that projects the intermediate state onto |w>.
It does not prove that all initially physical states complete, that completion
is almost sure in the added-cycle model, or that no other closed sectors exist.

## Evidence, identities and limits

The three standalone controls are `z2_completion_check.py`,
`link_witness_check.py` and `local_operator_check.py`. The last imports only
the independently written geometry functions of the second. All ran
successfully on their first executions; complete stdout, empty stderr,
timestamped receipts and exact JSON outputs are preserved. There were no
discarded failures. The computations are finite operator/matrix-element
checks, not production simulations or full N4 density-matrix evolutions.

The neutral input file's actual SHA-256 is
`85ba81d38bf71f92045d833f549fb313ebc6d39a05bca17c0790fd069082adef`.
Its internal `source_identity_sha256` field is supplied provenance, not an
author source opened or authenticated by this reconstruction. The allowed
prior monitoring note is fixed at
`a4082e4764825510bce2c8430535fd5e8b5922733dbeb1e99d152ffc29052094`.
All current source and output identities are bound in the pre-comparison seal.

These are conditional finite-dimensional occupation/gauge constructions.
They do not supply a native M2-per-site encoding, derive the Hamiltonian or
birth instruments, identify a photon phase, or prove a thermodynamic limit.
The virtual-multiple-occupancy follow-up was not investigated. Author-source
comparison is a separate step after this seal; this report confers no audit
or publication status.
