# Independent local-implementation check

Date: 2026-11-08. Checker: same-family, fresh restricted context; no access to
the supervisor's new primary construction. This is a pure proof check, not an
audit or retained-status decision. Assigned effort: max; host runtime model
metadata was not independently exposed to this checker.

Science sources are frozen at e022e91b224e8323f27352c367fc2648a7031104:
the minimal axiom memo; native-code note; neighborhood electric-reader note;
native_records/RESULT.md; preparation_history/RESULT.md (exact paths in brief).
Methodology is origin/main 1e0d3b58dcda7f83152b0bb51729260247454d65,
refreshed from origin. Workflow, workhorse and freshness instructions read;
planning AGENTS read at 56c5c0ab64f532c5784e895b2f9aa6894fa334e0.
Preflight command: `python3 scripts/lab_ops.py preflight --target
.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107 --role checker
--model gpt-6-astra --effort max`. Result: go (114 GB free, 31% memory free,
load 5.0); this model argument is a requested profile, not runtime attestation.
No numerical job, extra science source, commit, push, branch change or axiom edit.

## Current finding

An exact finite driven empty-flux herald can be constructed with native
adjacent gates, one fresh output, and clean scratch drawn from the existing
unrecorded frozen sites. Its failure branch must remain coherent: measuring
each edge and classically ANDing the results is a different instrument.
The scratch and routing sites return exactly; old records can be excluded
from every herald gate. Borrowing frozen sites temporarily leaves E_p, so
the native Hamiltonian/phase-detector preservation theorem cannot be used at
intermediate microsteps. Whether that temporary borrowing is permitted must
be explicit in the supplied experiment, rather than hidden in a compiler.

Existing sources prove event-level history sufficiency; they do not themselves
prove sufficiency at every internal circuit microstep.

## Geometry and resources

Fix the prepared origin/frame p, L=3n^3 encoded links, K=4L=12n^3 active
qubits, and a classical old-record set O contained in V_p. There are n^3
vertex qubits, K active qubits and 112n^3 frozen qubits. Every frozen qubit
starts in a product |0>; old records have their fixed classical bit content.

The induced native nearest-neighbor graph on Lambda minus O is connected.
Translate p to zero. A frozen site has at least two coordinates nonzero mod 5.
Keep those coordinates fixed and move the third to 1; then move each other
coordinate to 1, retaining two nonzero residues throughout. This reaches
(1,1,1) entirely inside F_p. Each coordinate move takes at most floor(5n/2)
native steps. An active site reaches F_p in one perpendicular step; a fresh
vertex reaches it in two steps in distinct directions. Thus every two
unrecorded sites admit a path avoiding O of length at most
ell_max=6 floor(5n/2)+4. Delete loops if necessary.

For a simple path v_0,...,v_l between two operands, swap v_0 successively
to v_(l-1), apply the intended pair gate there and at v_l, and reverse the
swaps. Tensor-factor conjugation proves the exact original pair gate, with
identity on every other operand, even for arbitrary entanglement. It costs
2l-1 adjacent pair gates. No intermediate operation touches O. It can
temporarily move data or scratch through other unrecorded data/scratch sites;
those carriers return exactly after each routed pair operation.

## Empty-flux herald (construction)

On each edge apply W from the allowed electric-reader source, then X at
edge position 2. Call this unitary D_e=X_2 W. Since W J0=0100,
D_e J0=0000 exactly. Therefore D=product_e D_e sends the full empty-flux
vector Omega=product_e J0 to the all-zero K-qubit vector. This identity also
implies D^dagger |0^K><0^K| D=|Omega><Omega| on the full active Hilbert
space, not merely on the encoded subspace.

Reserve a fresh vertex herald h in |0> and K-2 distinct frozen scratch
qubits a_1,...,a_(K-2), also |0>. This fits since K-2<112n^3. Apply X to
each decoded data qubit, giving bits b_1,...,b_K. Reversibly compute
a_1=b_1 AND b_2 and a_j=a_(j-1) AND b_(j+1) for 2<=j<=K-2 by Toffoli;
apply Toffoli(a_(K-2),b_K;h), reverse the scratch computation, undo the K
input X gates, then apply D^dagger. No bit is measured before h.

There are 2K-3 Toffolis. An exact Toffoli with controls a,b and target t is
CV(a,t), CX(b,a), CV^dagger(a,t), CX(b,a), CV(b,t), where
V=(I+X)/2+i(I-X)/2 and V^2=X. On controls a,b the exponent is
a-(a XOR b)+b=2ab; this preserves every relative phase and restores controls.
Route each of these five pair gates as above. With the explicit D_e and its
inverse the total is at most 8L+5(2ell_max-1)(2K-3) adjacent pair gates and 12L
onsite gates, followed by one supplied permanent Born record append at h.
The bound is deliberately loose; no efficiency or physical-duration claim.

On clean scratch the completed unitary is
U=P_Omega tensor X_h+(I-P_Omega) tensor I_h, with scratch identity on |0>.
Thus success Kraus operator is P_Omega and failure is I-P_Omega, exactly.
All old records, vertex pointers other than h, and frozen scratch return
unchanged. Success certifies the rank-one empty-flux state. Tensoring the
identity on any passive reference A gives
(P_Omega tensor I_A) X (P_Omega tensor I_A)
=P_Omega tensor <Omega|X|Omega>, including arbitrary initial entanglement.
No earlier preparation label fixes the unknown pre-herald success odds.

## Finite control: independently derived construction and limits

At a stable event boundary R determines the frame, old word length m=d+k,
the old word, and the fresh next target. A supplied drive can use that decoded
geometry and length to choose a finite circuit layout; this is not an
autonomous native scheduler. Copy only the m old record bits into m clean
frozen qubits. A vertex has no adjacent frozen qubit: its neighbors are active
data. Accordingly route a clean destination to an active neighbor, apply CX
with the old record as control, then reverse the route. The active neighbor's
original state returns exactly. The old record remains its fixed |b> at every
gate; no old record is ever a SWAP operand or target. This is a nondemolition
use of a recorded value, unlike treating an absent |0> as readable zero.

Any finite Boolean table can be implemented reversibly: for each input word w,
X-conjugate its zero controls, compute their AND into a selector using an
AND chain, perform the selected recipe, uncompute the selector and undo the
X gates. Exhausting all words applies exactly one branch. The copy registers
are never changed by recipe execution. At the end the same old-record CX
operations erase their copies exactly; predicate scratch also returns to zero.
The current output must NOT be included among these immutable copy inputs.
No claim is made that an unknown quantum input is read by this process.

For recipes supplied as finite unitary words followed by a single binary
pointer instrument, the entire lookup can be coherent and its scratch clean
before the final record append. One- and two-qubit gates gain a selector
control. An exact three-qubit implementation exists by finite row elimination:
Givens rotations and diagonal phases factor its 8-by-8 unitary into two-level
unitaries; Gray-path basis transpositions conjugate each level pair into a
single target bit with two prescribed controls. Compute those controls into
one clean flag, apply the corresponding controlled 2-by-2 pair unitary and
uncompute. Every transposition is an exact Toffoli with possible X-conjugated
controls. This is a finite constructive factorization, including phases;
it presupposes the resulting exact pair gates as supplied driven operations.
An arbitrary evolution exp(-i tau H) is not automatically an exact word in
a fixed finite discrete gate alphabet. Its exact synthesis or an error bound
must be stated. This caveat is separate from record-state sufficiency.

Fewer than 2M+4 clean controller qubits suffice for copies, predicate chain,
selector and this three-qubit decomposition, in addition to the K-2 herald
scratch if all are reserved simultaneously. The bound n>=2M+8 makes
K+2M+4<112n^3. A fixed enumeration in the recovered marker frame chooses
workspace and routes covariantly; use anchor a+(1,1,1), not a hidden host
origin. The selected final event is then transported by every proper cubic
rotation and translation. This statement concerns prepared single-origin
domains, not arbitrary coherent origin superpositions.

## A cleanup trap in the six-edge mixture

The source's Eq.(2) averages six CP branches, not amplitudes. A coherent
three-qubit uniform edge selector generally stays entangled with the gauge
data and cannot simply be uncomputed. For an exact witness let L_A and L_B
be Gauss singlet plaquette loops using respectively the (+e1,+e2) and
(-e1,-e2) edge pairs at x. They have distinct occupation patterns and are
orthogonal. On (L_A+L_B)/sqrt(2), the b=1 branch of the six-edge mixture is
(|L_A><L_A|+|L_B><L_B|)/6, a rank-two operator. A unitary implementation
with one measured binary pointer and every other ancilla returned pure has
one Kraus operator per b and maps a pure input to a rank-at-most-one branch.
Thus that particular clean implementation does not implement the mixture.
This is a direct counterexample to erasing its unobserved selector, not a
no-go for the record law. Supplied classical randomness, retained environment,
additional recorded selector bits, or a deterministic programmed edge each
changes the resource/instrument contract and must be declared.

## Frozen sites, capacity and timing

The circuit deliberately visits states outside E_p, both by decoding links
and borrowing F_p. Neither D_x phase selection nor the H_native preservation
identity is valid on those intermediate states. Switch off unsolicited
H_native evolution during the driven circuit, or include and compensate its
actual action. Frozen |0> is restored at the completed boundary. If "frozen"
means fixed at every microstep, this construction does not meet that stricter
contract. No old record may be written on F_p if it must later be reset.

The herald consumes one vertex record, including on failure. In the source's
post-success domain it occupies the first of N slots, leaving N-1 recipes;
failure can terminate rather than reset the permanent record. Ordinary data
records use at most 7+d+N<=n^3 vertices. Extra selector, completion or timing
records must be added explicitly to that count. The 125 phase sectors do
not multiply capacity once the apparatus records fix p.

The supplied drive has a microstep index j while R is unchanged during
unrecorded gates. A law whose entire state is R cannot automatically recover
the different gate instructions from that unchanged R. At stable event
boundaries the history recursion remains valid, but extending it to every
microstep requires an actual clock/scheduler construction or another explicit
domain convention. "Log each gate" is not a resource proof: the loose herald
bound above is O(n^4) and only n^3 vertex outputs exist. A better parallel
layout or separately budgeted clock might work; no impossibility is asserted.
Ordinary gate synthesis does not discharge this timing obligation.

## Discriminating hand checks and disposition

I independently propagated J0 through W: after its swaps and CX it is
(1100+0100)/sqrt(2), and H_1 gives 0100 with positive phase. The source's
J1 instead becomes -1100, so population-only substitution fails. Reversing
the AND computation is necessary to return clean scratch; omitting it leaves
which-input information. Measuring each edge before the AND dephases a
superposition of two distinct nonempty loops even though the desired failure
map (I-P_Omega) preserves it. Routing through an old vertex would move its
record and is excluded by the proved path construction. The six-edge
mixture witness above catches a different, branch-rank cleanup defect.

Conclusion of the independent portion: exact adjacent-gate rank-one herald
and finite driven record-dependent unitary recipes are supported with the
declared temporary workspace and drive conditions. A fully autonomous
microstep record-only law is not supplied by those constructions. This is
same-family research checking with shared source premises, not audit evidence.
The controlled-square-root identity is credited in the allowed reader note
to Barenco and colleagues; it was checked algebraically here rather than
importing an unexamined external universality theorem. No extra literature
source was opened under this five-science-source check contract.

Independent portion completed before opening the supervisor's primary. A
parent message after the herald derivation disclosed that the primary uses
deterministic edges, finite words, completion flags and stable macrosteps;
those details are not claimed as independent discoveries here.

## Separate source-exposed check of the supervisor candidate

Read the complete primary at gb1-cf-pair/Physics under the assigned
local_implementation/PRIMARY.md, SHA256
2cbf5ff6c0eb3ea502e0b15c1c4d3203d059c2222803275af53d1045ee35ef47.
This section checks that source; it is not part of the restricted derivation.

The primary's alternate decoder W then X_1 X_3 X_4 sends J0 to 1111.
Its r-1=12n^3-1 work-bit chain, copy to herald, uncompute and inverse decoder
therefore give the stated full-data-space projector. Counts 48m-9 abstract
pair gates and 8m onsite gates are correct. The twelve offsets per cell are
distinct frozen sites. No phase is dropped. The endpoint routing and its
loose D=30n+2 bound work; excluding every V_p from path interiors is stronger
than necessary and avoids all possible old records.

The completion allocation is valid: value and flag rows differ by ten native
units; each row's consecutive sites differ by ten; n>=2M+8 prevents wrapping
into the seven-marker component. All new sites remain isolated in its
distance-five graph. Capacity 7+d+2N<=7+2M<n<=n^3 is ample. Completion flags
encode presence without pretending a blank zero is distinguishable from a
recorded zero by its density operator.

Masked-copy cleanup is exact. With flags held fixed, the copy map computes
y_j=f_j b_j. An active recipe changes only b_(k+1), whose f_(k+1)=0. Hence
all copied y_j and f_j have the same values before and after the recipe, so
the inverse copy map clears work even on a coherent superposition of the
new pointer's values. Intermediate copy/un-copy of that live pointer is a
unitary operation, not a readable record. Recorded pointers are only CX
controls and keep their fixed basis contents. For legal prefixes exactly one
nonterminal indicator is selected; at all-complete flags none is selected.
Its maximum conjunction length M+1 and controller count <=3M+1 are valid.

Controlled CV is exact using R^2=V in the same five-pair identity (R has
eigenvalues 1 and exp(i*pi/4)). These new controlled-R pairs are permitted by
the declared exact pair-gate premise. Controlled SWAP decomposes as
CX(a,b), Toffoli(s,b;a), CX(a,b). The scope restriction to finite recipe
words, deterministic selected edges, suspended H_native and stable driven
macrosteps avoids the unproved synthesis, mixture-cleanup and timing claims.

Required clarifications/repairs before treating the whole candidate as checked:

1. Do not reuse controller copies/indicator scratch simultaneously as the
   herald's clean AND chain. If k=0 executes the herald inside the unified
   controlled schedule, allocate disjoint blocks. The combined requirement
   (12n^3-1)+(3M+1)=12n^3+3M<112n^3 still fits. Alternatively run the herald
   separately before those copies become live and state that execution order.
2. The displayed indicators enumerate histories with failed first herald,
   so they do not by themselves implement its stated absorbing failure.
   Guard subsequent indicators/registration on herald success, or explicitly
   give failed-herald configurations a halted sequencer/domain disposition.
3. Anchor the routing plane and tie breaks at marker center a in its recovered
   frame. A chosen residue representative p alone need not transport under
   coarse translations. The completed routed operator is path-independent,
   but the claim that every microscopic route itself transports needs this
   explicit choice.

These are narrow implementation/statement repairs, not evidence that an axiom
change is needed. The primary correctly leaves physical registration,
microscopic scheduling and an autonomous record-only law open. Pending the
three repairs, the full source is not reported as unconditionally confirmed.
