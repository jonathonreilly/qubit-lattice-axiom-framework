# Local collective record circulation releases the tested U(1) trap

Date: 2026-09-22. Status: author construction and exact finite certificate;
independent check pending. This is an added supplied interaction, not a
derivation of that interaction from the minimal axioms or from the previously
specified vacancy-only hopping Hamiltonian.

## 1. The question changed by the trapped configuration

The spin-half U(1) counterexample showed that ordinary vacancy hopping and
pure field loops can leave sites permanently vacant. It did not include
collective movement of occupied records. The original research objective
allows records themselves to move; the earlier classical routed process
even moves records after every site is occupied. It is therefore useful to
test a local simultaneous circulation of existing records with the field
adjusted along their paths.

The construction below preserves the same spin-half U(1) Gauss law and every
existing record. It unlocks the exact N=4 extreme-flux witness by one local
four-record circulation, two ordinary hops, and one neutral-pair birth. A
short-time amplitude calculation establishes strictly positive quantum
completion probability for this witness. No all-state or almost-sure
completion theorem is asserted.

## 2. Gauge-dressed occupied plaquette operator

Use the matter and gauge spaces in
`GAUGE_COVARIANT_PERMANENT_RECORD_DYNAMICS.md`. Let an oriented plaquette
cycle visit vertices v_0,v_1,v_2,v_3 and links e_0,...,e_3. Let s_i=+1 if its
traversal follows a link's reference orientation, and -1 otherwise. For an
occupied charge word q=(q_0,...,q_3), q_i in {+1,-1}, define the cyclic matter
permutation Cq=(q_3,q_0,q_1,q_2). Supply

    K_C = sum_q |Cq><q| tensor product_i L_(e_i)(-s_i q_i),
    L_e(+1)=U_e,  L_e(-1)=U_e^dagger.

It acts as zero if any cycle vertex is vacant. Each link change is the
electric-field change needed to carry its source record to the next vertex.
On a spin-half field, the term is nonzero exactly when

    2E_(e_i) = s_i q_i,  i=0,...,3.

When nonzero, all four link fields reverse. The charge change at vertex i is
q_(i-1)-q_i. The corresponding divergence change is

    s_i(-s_i q_i) - s_(i-1)(-s_(i-1)q_(i-1))
       = q_(i-1)-q_i.

Therefore every G_v=div E-Q commutes with K_C. Reversing the cycle gives
K_C^dagger: in the output, the record at v_(i+1) is the original q_i, and
reversing its link change returns both charge and field to their input.

The local Hamiltonian may include

    H_cycle = g sum_plaquettes (K_C + K_C^dagger),  g > 0,

with one chosen orientation C per plaquette. The adjoint is included exactly
once; equivalent basis transitions from two terms add their amplitudes.
Summing over all plaquettes with equal coefficients gives the corresponding
cubic-covariant supplied interaction. Each occupied record is permuted to
another vertex, so both species counts and total record count are unchanged.
There is no annihilation or overwrite.

An occupied record may have an additional internal Hilbert space besides its
charge. Replace |Cq><q| by the cyclic permutation of the entire occupied
content, controlled only by its charge labels. This transports arbitrary
internal states and their entanglement. The finite qutrit example itself
does not encode arbitrarily many unique birth identities; such additional
record data require their own explicit carrier.

The exact local checker enumerates all 3^4*2^4=1296 matter/link basis inputs.
There are sixteen nonzero forward matrix elements, one for each occupied
charge word with its eligible field word. It verifies every local Gauss
difference, species count and inverse circulation. No continuum or weak-field
approximation is used in this operator test.

## 3. A complete local renewal path

Take exactly the N=4 integer matching certificate in
`GAUGE_RECORD_EXTREME_FLUX_RESULTS.json`, with vacancies 000 and111. Initially
every ordinary vacancy hop and every elementary pure-field plaquette flip
vanishes. There are sixty-eight permitted oriented occupied-record cycles.
One is the square traversed as

    001 -> 002 -> 102 -> 101 -> 001.

Its occupied charge word is (+,+,+,-), which becomes (-,+,+,+). Apply it,
then perform these two independent ordinary gauge-dressed hops:

    negative record: 001 -> 000,
    positive record: 101 -> 111.

The vacancies are now001 and101, which share a nearest-neighbor link. The
allowed neutral-pair birth on that link fills both. The record count along
the complete path is62,62,62,62,64, with thirty-two records of each charge
at the end. Every link and site in the path obeys Gauss's law exactly.

`gauge_collective_record_cycle_check.py` reconstructs the original matching
from its bound result file, enumerates permitted cycles, and verifies every
step directly. The relevant deterministic edge indices are2 and52 for the
ordinary hops and3 for the birth. It also tracks arbitrary distinct payload
labels through the three transport operations and verifies that they are
permuted bijectively. Those labels are a check on content transport, not an
unstated extra capacity of the qutrit representation.

## 4. A nonzero quantum amplitude, not just a graph path

Let |I> be the original trapped basis vector and |A> the specific adjacent-hole
basis vector after circulation and the two hops. Use ordinary hopping
coefficient kappa>0 and circulation coefficient g>0. Include the earlier
elementary pure-field plaquette Hamiltonian if desired. Diagonal energies
and diagonal occupation/field monitoring do not change the following leading
matrix element.

The initial holes have graph distance three. An occupied-record circulation
or a pure-field loop does not change hole positions. At least two ordinary
hops are therefore needed to reach this adjacent-hole target. Initially
ordinary hops and pure-field plaquette flips vanish, so a contributing
three-step Hamiltonian path must first perform one occupied-record cycle
and then the two ordinary hops. The exact enumeration finds two such paths
to this particular target: the displayed cycle followed by either ordering
of the two disjoint hops. Thus

    <A|H^3|I> = 2 g kappa^2,
    <A|H^j|I> = 0 for j=0,1,2.

No other three-step path can cancel them; the two contributions have the
same positive real coefficient. For the no-jump generator
A_eff=-iH-(1/2)sum J^dagger J, with diagonal jump loss operators here,

    <A|exp(A_eff t)|I>
       = i g kappa^2 t^3/3 + O(t^4).

At these orders any diagonal energy or loss insertion would leave too few
hole-moving transitions, so it cannot alter the displayed coefficient.
Choose the final birth channel and its particular full-occupation output
|F>. That channel has |A> as the unique preimage of this output in the basis.
The joint probability density for no preceding jump and that birth outcome is

    |<F|J_birth exp(A_eff t)|I>|^2
       = beta g^2 kappa^4 t^6/9 + O(t^7).

Its integral over a sufficiently small positive time interval is strictly
positive. This proves that the additional local interaction releases the
tested trap with positive completion probability in the actual quantum
model. It does not replace an almost-sure completion proof or a finite mean
bound for every initial state.

## 5. Design implication and remaining obligations

Pure contractible field loops preserve the negative-link count F at fixed
charges, which protected the earlier saturated matching sector. A collective
record cycle also moves charge between occupied vertices and can change F;
the displayed cycle increases F by two while preserving every record. It
therefore acts outside the invariants used in that scoped trapping proof.
This is a concrete alternate mechanism that must accompany any account of
the negative result.

The interaction is not generated by repeatedly applying the earlier
Hamiltonian to the trapped state: that Hamiltonian annihilates it. Deriving
an effective cycle from a larger microscopic model would require new
intermediate states and a controlled reduction. No such derivation is
claimed here. Neither this added coupling nor its strength is selected by
the framework's axioms.

The next scientific obligations are to identify remaining invariant or
trapped sectors under the enlarged dynamics and determine what degree of
completion and long-distance field behavior can actually be proved. A
photon phase, relativistic limit, native qubit placement, and empirically
testable coupling remain open.

