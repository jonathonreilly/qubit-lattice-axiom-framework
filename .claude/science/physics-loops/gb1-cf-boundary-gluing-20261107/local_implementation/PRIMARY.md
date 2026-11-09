# Frozen candidate: finite neighborhood verifier and controller

Supervisor candidate, 2026-11-08 local date. Parent e022e91b22, main 1e0d3b58dc.
Conditional theorem candidate, not an axiom-derived dynamics or audit verdict.
Written before opening the independent checker's deliverable. The checker has
reported only an early independent full-projector/cleanup route and timing caveat.

## Target and premises

Use the previous spacing-five register on Lambda=(Z/(5n)Z)^3, n>=2M+8,
M=d+N, d,N>=1. There are m=3n^3 four-qubit links, V_p free vertices and
112n^3 frozen F_p sites. A prepared frame and origin are fixed by the seven
record markers. Tensor quantum kinematics, exact driven onsite/two-site gates,
clean unrecorded work, Born readout and permanent registration remain supplied.
Borrow F_p during a compiled word and restore it exactly at completion; suspend
the supplied Hamiltonian during that word. Intermediate code/Gauss membership
is not required, as in the existing electric reader. No old record may change.

## Full rank-one herald, without an input-code promise

On each link use W=SWAP34,SWAP23,CX12,H1,CX34, so W J0=0100.
Apply W to every link, then X to bits 1,3,4. The resulting unitary T sends
Omega=(J0)^tensor m to the all-one word on r=4m data bits.
Compute their conjunction into a clean chain of r-1 work bits by r-1 Toffolis;
copy its final bit to a fresh herald; uncompute the chain and apply T inverse.
Thus the full data-space unitary on clean work is

    (I-P_Omega) tensor I_herald + P_Omega tensor X_herald.

This holds on every data vector, including passive references. Unlike testing
only the reader's two flag bits, it has rank one on the full native data space.
Both branches preserve the code and Gauss subspace when the input has them.
A nonzero success fixes Omega and decouples a passive reference. Unknown input
success odds and occurrence are not derived. Failure is not overmeasured:
there are no intermediate records of separate links or syndrome bits.

The abstract pair count is 8m+10(4m-1)+1=48m-9, using the exact five-pair
controlled-square-root decomposition of each Toffoli; the onsite count is 8m.
Work is 4m-1=12n^3-1. Allocate up to twelve work sites per coarse cell at
offsets (i,j,0), i=1..4, j=1..3, all in F_p. One unused allocation is omitted.
Fresh herald is the first history output. No per-link permanent records.

## Routing and old-record protection

G=Lambda minus V_p is connected. A vertex not in V_p can reach the plane x=1
(coordinates relative to p) without hitting V_p: if y,z are multiples of five,
first change y by one, which is safe because x is then not a multiple of five;
otherwise change x directly. Within x=1, move y,z freely. Connecting via this
plane and reversing the target access route gives length <=30n; remove cycles.
Allowing endpoints in V_p adds at most two edges: D=30n+2 is a safe bound.

For an unrecorded pair gate, move one operand along all but the last path edge,
perform the pair gate and undo every SWAP. This is exact conjugation, identity
on every spectator even when entangled. All intermediate sites avoid V_p.
For reading a record, move a clean work operand to a neighbor of that record,
use the record solely as CNOT control, then return the work operand. Its known
basis content is unchanged at every elementary gate. Never SWAP a record or
use it as the target of a classical decomposition. Pair overhead <=2D+1.
Herald cost <=(48m-9)(2D+1) adjacent pair gates plus 8m onsite gates.

## Presence is not automatically a gate input

A present value-zero record and an absent pointer in |0> have identical qubit
density operators. A unitary acting only on those operators cannot distinguish
the two. The abstract record configuration does distinguish presence. A
gate-level compiler must encode it or supply an additional presence interface.
This is a two-input witness, not a no-go for the record state axiom.

Use value sites v_(d+j)=a+10(d+j)e1+20e2 as before and completion sites
w_j=a+10(d+j)e1+30e2, j=1..N. At stable stage k, the first k values are
recorded and the first k completion bits are recorded 1; later sites are blank0.
Headers remain v_1..v_d. The existing bound n>=2M+8 separates all these sites,
and the new sites are isolated in the distance-five marker graph. The same
intrinsic frame works. Permanent count is 7+d+2k, using only V_p. This changes
the output allocation, not the five-state code, local site dimension or axioms.

## Record controller with clean work

Let f_j be the completion bit and b_j the value bit. Copy headers and flags to
clean work and store only masked history y_j=f_j b_j. To copy y_j without
changing records, copy b_j into a temporary work bit, Toffoli on the work copy
of f_j and that temporary bit into y_j, and uncopy b_j immediately. Temporary
bit is clean. Records are only CNOT controls, never Toffoli work targets.

For every k=0..N-1, header alpha and k-bit history h, compute an indicator of
the conjunction [header=alpha, y_1..y_k=h, f_k=1, f_(k+1)=0], with f_0=1.
Use negative controls only on work copies. A conjunction chain suffices; its
length is at most M+1 controls. Exactly one indicator is 1 on a legal nonterminal
prefix. Apply its controlled finite recipe word, then uncompute the indicator.
All words are enumerated in one fixed finite schedule. Old controls and flags
do not change during this schedule. The active recipe changes only live data
and its next fresh value pointer. At terminal stage all indicators vanish.

The initial masked-copy map has the SAME value before and after that recipe:
its new output has f_(k+1)=0 until registration completes. Therefore uncomputing
the entire record-copy map after the unitary clears all work even when the new
pointer is entangled. Copying all future unmasked pointer values instead would
leave outcome-dependent work and is a rejected candidate.

Workspace <=(d+2N)+1+M <=3M+1, reusable in the herald's 12n^3-1 F sites.
The finite candidate branches number 2^d(2^N-1); no efficient-scaling claim.
Copying bits and conjunction gates have the explicit routing above. Controlled
X/CX/CV/H/SWAP words reduce to onsite and pair gates: controlled CX is Toffoli,
controlled CV uses the same square-root identity, controlled H is a pair gate,
and controlled SWAP is CX,Toffoli,CX. Thus the existing reader is one exact
integrated recipe. Other recipes require supplied finite words or a separately
checked exact synthesis; no full magnetic exponential compilation is claimed.

## Registration and microscopic timing boundary

At the selected next value site use the supplied gated Born/Record append,
then flip its fresh completion pointer and register 1. The flag is written
only after the selected unitary and controller cleanup. Selection is from the
old record flags, before the value outcome. Failure of the first herald can
be declared absorbing; post-success history starts from P_Omega as before.

These two appends and all microgates form a driven compiled macrostep. An
intermediate state after value registration but before its completion record
must not be treated as another stable input to the compiled controller. The
prepared domain and supplied sequencer distinguish this boundary. The theorem
does not derive that sequencer, the physical gated registration rule, an
autonomous clock, or a record-only state at EVERY microscopic gate. Such a
claim would require a further controller-phase/formation construction.

Translation/proper-rotation transport of the prepared frame transports every
path, word and allocation. No preferred native origin is introduced. The
finite torus regulator still needs a separate infinite-Z3 limit/embedding.

## Planned discriminating checks

Check the full one-link herald on all native basis inputs and both pointer
inputs against the rank-one operator, using independent target construction;
check two-link failure coherence (no per-link records). Check AND uncompute,
old-record read-only routing, all legal small controller prefixes, branch
selection, clean masked-copy cleanup after changing the next output, and
counterexamples for using only two vacuum flags or omitting completion flags.
Pure proof supplies the arbitrary-size claim; finite arithmetic is diagnostic.
