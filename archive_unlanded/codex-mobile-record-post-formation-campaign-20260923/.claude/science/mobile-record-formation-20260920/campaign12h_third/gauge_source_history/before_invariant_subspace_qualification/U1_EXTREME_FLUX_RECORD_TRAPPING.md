# Extreme-flux trapping of permanent records in a spin-half U(1) model

Date: 2026-09-22. Status: author exact finite certificates and analytic
conditional trapping argument; independent check and N1-N8 publication gate
pending. This private result is restricted to the supplied model in
`GAUGE_COVARIANT_PERMANENT_RECORD_DYNAMICS.md`.

## 1. The precise claim

Take the periodic N-cubed cubic lattice with reference-positive oriented links
in its three coordinate directions, N even. Local matter is |0>,|+>,|->;
each link is E=+-1/2. Physical states obey div E=Q with Q=0,+-1. Movement is
the gauge-covariant nearest-neighbor hopping in the companion note. Formation
is irreversible opposite-charge pair birth on adjacent vacancies. All birth
rates are finite and positive. Occupation monitoring may have any positive
rates. Include an arbitrary elementary plaquette-flip Hamiltonian and
diagonal electric/charge energies if desired.

For N=4,6,8 there are exactly verified birth histories from the completely
vacant state with every link E=+1/2 to a state with two separated vacancies
and no allowed hop, pair birth, or elementary plaquette flip. Hence reliable
completion for every initial state is false for this specified model.
The histories also imply a strictly positive trapping probability from the
stated empty initial state under the continuous quantum dynamics. The
argument does not estimate an appreciable probability or a thermodynamic
vacancy density. Uniform positive electric flux is a special initial sector,
not a claim about a low-energy vacuum.

There is a stronger scoped stability statement: the trapped sector remains
closed under any collection of contractible Wilson-loop field terms and
diagonal field/charge terms, even if such larger loops mix its basis states.
Winding loops, other record moves, higher-dimensional link representations,
different gauge constraints, or annihilation laws are different targets.

## 2. Integer formulation and the saturation bound

Let b_e=1 for E_e=+1/2 and b_e=0 for -1/2 on each reference-positive link.
On the periodic lattice, the all-one vector has zero divergence, and Gauss's
law becomes Q=B b, where B has +1 at the source and -1 at the target of a
reference link. Define the negative-link count

    F = sum_e (1-b_e),  N_record = sum_x |Q_x|.

For a vertex, let in_-(x) and out_-(x) count its incident negative links
according to their reference orientations. Then

    Q_x = in_-(x) - out_-(x),
    N_record = sum_x |in_-(x)-out_-(x)| <= 2F.

If F=N_record/2, equality holds at every vertex. Since Q_x is only 0,+-1,
each occupied vertex has exactly one incident negative link and each vacancy
has none. Thus the negative links are a matching of occupied vertices. A
negative link from x to y gives Q_x=-1 and Q_y=+1. Conversely every such
matching defines a valid saturated Gauss configuration.

Starting from all-positive flux and all vacancies, a birth on a reference
link flips that link to negative and creates (-,+) at its endpoints. Any
sequence of disjoint births therefore stays on this saturation boundary.

## 3. Constructing a jammed matching

Leave vacancies h=(0,0,0) and k=(1,1,1). They are nonadjacent and lie on
opposite bipartite sublattices for the stated even N. Require, for each hole,

    Q_(hole+e_i)=+1,  Q_(hole-e_i)=-1,  i=1,2,3.

The two holes have disjoint neighbor sets for N=4,6,8, and the requirements
are consistent. Choose a nearest-neighbor matching covering every other
vertex such that each reference link a->b in the matching has Q_a=-1,
Q_b=+1, including these prescribed neighbor charges.

`gauge_record_extreme_flux_check.py` finds such a matching by a deterministic
bipartite augmenting-path procedure and verifies the witness directly for
N=4,6,8. The proof relies on the returned finite matchings, not an assumed
all-size success of that search. Every matching edge, endpoint, charge,
vacancy and complete birth history is retained in its JSON result. In
particular, the certificate does not depend on a mixed-integer solver's
optimality or infeasibility judgment.

Now every link incident to a vacancy is positive. Flipping hole->neighbor
changes the hole charge by -1 and its positive neighbor by +1, which would
produce charge +2. Flipping neighbor->hole similarly would produce charge
-2 at its negative neighbor. Neither is in the allowed matter space, so
every record hop into either vacancy is zero. All other links have two
occupied endpoints and cannot perform a vacancy hop. Since the two vacancies
are nonadjacent, every pair-birth operator also vanishes.

An elementary plaquette could flip only if the two links to be raised and
the two to be lowered have the appropriate saturated field values. In the
reference-positive convention, each pair of same-sign changes meets at a
plaquette vertex. In a matching there cannot be two incident negative links.
Thus neither orientation of any elementary plaquette acts. The checker
also enumerates all 3N^3 plaquettes directly and finds zero flippable faces.

The exact certificate counts are:

| N | Vertices | Record count | Negative links / birth events | Vacancies |
| --- | ---: | ---: | ---: | ---: |
| 4 | 64 | 62 | 31 | 2 |
| 6 | 216 | 214 | 107 | 2 |
| 8 | 512 | 510 | 255 | 2 |

These are finite constructions, not a fitted scaling law. They use the same
two hole coordinates and independently verified matching lists.

## 4. Why contractible field loops cannot repair this sector

Fix the resulting charge configuration and the value F=N_record/2. Let D be
the span of every spin-link basis configuration with those same charges and
that F. The saturation argument forces every basis vector in D to be a
matching on the same occupied vertices; in particular all links incident to
the holes remain positive.

A contractible oriented Wilson loop changes E by one unit with signs given
by its traversals. Its total signed coordinate displacement is zero, so the
sum of its electric-field changes is zero and F is preserved. It also
preserves every Gauss charge. Its nonzero action therefore maps D to D.
The adjoint has the same property. This reasoning covers longer contractible
loops, not only plaquettes, and does not assume they all annihilate each
individual matching.

The prescribed neighbor charges and positive hole-incident links make every
record hop vanish throughout D. Birth vanishes because the hole positions
remain nonadjacent. Diagonal charge or electric terms, and monitoring of
occupation or electric fields, preserve D. Consequently D is a closed
nonfull subspace under the stated entire generator. Arbitrarily increasing
the monitoring strength cannot create a transition out of it.

A winding loop is an explicit boundary to this statement. For example, in
the preliminary N=4 solver witness, a four-link loop winding once around a
coordinate direction changes F and enables a hop. Such a loop is not an
elementary plaquette even though their lengths happen to agree at N=4.
Its support grows with N. No local contractible-loop theorem is being
extended to those operators.

## 5. Empty-start quantum reachability

For the standard elementary plaquette model the final matching basis state
is itself stationary, apart from an irrelevant Hamiltonian phase. Choose
the ordered disjoint birth channels in the certificate. The corresponding
unnormalized quantum-jump trajectory amplitude is a finite product of birth
operators and no-jump exponentials. As all waiting intervals tend to zero,
it tends to a nonzero scalar times that matching basis state. Continuity of
the finite-dimensional exponentials implies a positive-measure region of
strictly positive small waiting times whose trajectories have nonzero
projection on the trapped state. Their probabilities are nonnegative and
their integrated weight is strictly positive.

For the extension with arbitrary contractible field loops, replace the
stationary basis vector by the closed subspace D. The same limiting product
has nonzero projection onto D, and that component cannot subsequently leave.
Its occupation pattern and vacancy count never change. This establishes
positive-probability trapping from the specified empty state without
evolving an exponentially large density matrix or mistaking a zero-time
history for an event of positive probability.

## 6. Discovery record, counterroutes, and open questions

The first orientation MILP found a two-hole hop jam with 30 flippable
plaquettes. It failed the attempted direct birth matching (size 30 of31),
and several plaquette flips enabled immediate record hops. Those results are
preserved, not recast as trapping under magnetic dynamics. Its two holes
also lay on the same bipartite sublattice, precluding the proposed direct
disjoint-birth history; that was a search limitation, not a reachability
proof by other processes.

A subsequent MILP with opposite-sublattice holes and a built-in birth
matching found both an ordinary jam and a fully plaquette-frozen jam. Some
fixed-charge no-plaquette searches returned infeasible. These solver outcomes
are preserved as discovery history and are not mathematical no-go evidence.
The final uniform-flux matching argument above replaces them with a simpler
integer certificate and an analytic explanation.

The positive Z2 construction in the companion note remains a material
alternative: its unitary field shift transports each whole gauge block and
admits the monitored completion proof. It changes the gauge theory. A
second constructive route now keeps the spin-half U1 gauge constraint:
`COLLECTIVE_RECORD_CIRCULATION_RELEASES_GAUGE_TRAP.md` supplies a four-record
plaquette circulation, gives an exact completion path for the N4 witness,
and proves its leading quantum birth amplitude is nonzero. That interaction
changes the charges within occupied regions and need not preserve F, so it
is outside the trapped generator quantified above. It is an added term,
with no all-state completion theorem. A
spin-half U(1) model with a different initial flux sector, a larger field
space, additional record moves, or suitably suppressed winding processes
requires its own analysis. No universal incompatibility between permanent
records and gauge physics has been established. The absence of an empirical
prediction or a native microscopic derivation remains explicit.
