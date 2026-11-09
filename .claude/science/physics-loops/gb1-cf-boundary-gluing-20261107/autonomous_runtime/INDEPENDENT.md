# Autonomous permanent-phase construction: independent check

Claim type: explicit conditional construction, not retained status or an axiom derivation.
Source science pin: `9213a55c3636c8bdbf4a1f692e902d4d6d7ac44a`.
Current-main snapshot: `1e0d3b58dcda7f83152b0bb51729260247454d65`.
Worker checkout HEAD: `f5af11cd0102cfd0b51aef0911f600130bf5beb1`.
Same-family/fresh-context independent derivation; no supervisor candidate was read.
Task: make the finite compiled quantum program's phase and formation part of
its permanent record state, and distinguish this from selecting its physics.

## Sources, launch, and method

Exactly five science sources were read at the science pin: the minimal axioms;
`local_implementation/RESULT.md`; `preparation_history/RESULT.md`; the November 8
SU2 neighborhood/record-readout note; and the September 13 fixed-first-target
local-program note. The current workflow/workhorse/freshness texts were read;
their checkout copies have no diff from the named main snapshot.
`lab_ops.py preflight --target .claude/science/physics-loops/gb1-cf-boundary-gluing-20261107
--role checker --effort max` returned `preflight: go`: disk 110 GB, free memory
31%, load 3.2, nice available, origin reachable. No model floor was declared;
the host's inherited model was used without substitution. No numerical job ran.

Targeted primary-source search found Richard Feynman's *Quantum Mechanical
Computers* (1985) and Frank Verstraete, Michael Wolf and J. Ignacio Cirac's
*Quantum computation, quantum state engineering, and quantum phase transitions
driven by dissipation*, https://arxiv.org/abs/0803.1447. The useful method is to
attach a clock raising operator to each gate. No published theorem is imported:
the one-way, permanently recorded version needed here is proved directly below.
The supplied September probability-tree construction supplies odds in its bank;
it does not implement the live gauge circuit and is not used as that substitute.

## 1. The input obstruction, before construction

With identical preparation/header/clock records, allow arbitrary unobserved
native input X. For the exact herald let P=|Omega><Omega|. Inputs X=P and
X'=|eta><eta| with eta perpendicular to Omega have success odds 1 and 0.
Thus no function of those identical records gives both odds. This refutes only
the arbitrary-input record-sufficiency claim; it is not a general no-go.

There are two valid domains: (A) a fixed finite record-indexed dictionary
X_alpha, including all work and blank pointers; or (B) the domain beginning
after a recorded successful rank-one herald, where the certified state is P.
The latter forgets arbitrary pre-herald input only after success. It does not
assign its success probability. The construction uses one of these domains.
A passive reference is allowed: the known reduced density suffices provided
the reference never interacts subsequently. No arbitrary unknown input is
silently replaced by P. Clean work is part of the declared seed.

## 2. Finite event word and genuine quantum dynamics

Take the already supplied finite adjacent-pair/onsite circuit, including all
controller computations, inverse computations, routes, pointer flips and
registrations. Unroll its at most N macrocycles into a finite event word of
maximum length T. A unitary elementary event has one Kraus operator U_j;
a registration event at a pointer has the two projectors K_(j,b)=|b><b|.
The other tensor factors are implicit. Selection/halt can depend on previous
recorded outcomes. The source controller's failed-herald guard is retained.
For every enabled event, sum_b K_(j,b)^dagger K_(j,b)=I on its declared sector.
All selection is determined before the current outcome. No arbitrary magnetic
exponential, six-edge unobserved mixture, or new gate synthesis is imported.

For each reached classical phase/history s define the unnormalized quantum
state recursively by sigma_empty=X_alpha and

    sigma_(s,b)=K_(s,b) sigma_s K_(s,b)^dagger.

Positive-trace children are the domain. Their trace ratios are the next-event
probabilities and sum to one. This formula keeps ALL live data, pointer and
work qubits, including entanglement and dirty intermediate scratch. It does
not reset work between microgates; the source's exact uncomputation clears it
only at its proved completion phases. A passive reference obeys the same CP
identity. On successful herald branches the reduced gauge seed is P.

## 3. Permanent unary phase tape and capacity

Keep the finite gauge box, original seven frame records, header, value and
completion sites, and existing work allocations. Attach an EXTERNAL finite
tape of T fresh qubits and an initial bit-one seed. In recovered coordinates,
the original box lies in 0<=x,y,z<5n. One explicit tape is

    c_j=a+(10j)e1-20e2,  j=0,...,T.

Only c_0 is initially recorded; every c_j, j>0, is initially blank |0>.
No tape site is in the gauge box. All tape sites are isolated in the source's
distance-five marker graph, so its unique 1/2/3-arm spatial frame persists.
The tape cannot be allocated from the old n^3 vertices without a separate
capacity proof: T can exceed that budget. This enlarged finite apparatus is
the declared resource change. It does not enlarge the on-site dimension.

Event j permanently writes bit 1 at c_j as part of the SAME atomic instrument
that applies K_(j,b). A registration event additionally locks b at its original
value/completion site. Thus every unitary event consumes one new record;
every registration event consumes its existing output record AND one tick.
No later channel changes an old clock or data record's content; source data
records may still be used as unchanged basis controls. The next phase is the
first unrecorded tape slot. A failed herald still executes its completion
pointer flip and completion registration, then disables every later event.
A terminal phase likewise disables all events. No overwritten clock exists.

After k events and q completed binary-history stages, the record count is

    7+d+1+k+2q

at stable phases (the extra 1 is c_0). Intermediate phases add exactly their
already completed value/flag appends; the generic bound is 8+d+T+2N.
Post-herald starting domains count the preexisting success value and flag.
All T tick pointers require T additional initially clean qubits. Tick writing
does not borrow herald/controller scratch and never stores their quantum data.

## 4. One time-homogeneous jump law

Here is an explicit candidate formation mechanism, not a derived one. Choose
one positive constant gamma. At an enabled phase s=j-1, let

    L_(s,b)=sqrt(gamma) [K_(s,b) tensor |1><0|_(c_j)] Pi_s.

Pi_s is the diagonal projector onto the applicable OLD clock/header/record
controls; it excludes c_j and all live target operands. Identity extensions are
implicit; K and Pi commute on any shared old basis controls. Pi selects one
legal phase/history; failure-with-completion and terminal sectors have no
enabled channel. The failed-value-before-completion phase remains enabled. Include
the c_j vacancy in the raising factor itself. If a source elementary gate
already uses an old record as control, its K is block diagonal on that record
and hence leaves its known basis content exactly fixed. On every legal sector
exactly the next phase's channels are enabled; their total L^dagger L is
gamma I on that sector. Define no other live evolution.

Consequently the normalized no-jump state is unchanged: the survival factor
is exp(-gamma t), independent of the live state. The next wait is exponential
with rate gamma; conditional on a jump, its b probability is exactly the trace
ratio in section 2. At that jump lock c_j=1 and, for registration events, lock
the measured pointer b. The next clock prefix then enables the next channel.
Induction proves that these fixed channels execute precisely the supplied
circuit instrument, with its exact outcome cylinders and halt behavior.
This is a finite-dimensional time-independent jump process on the declared
domain. It has no external microstep index or elapsed-time dependence of the
normalized state. Choosing gamma sets a candidate rate; no physical time unit
or formation-rate prediction follows. Absorption occurs after at most T jumps.

The simultaneous gate-plus-tick jump is an explicit primitive of this proposed
law. It is NOT claimed to have been synthesized using only the earlier driven
pair gates and an already derived formation channel. Likewise the simultaneous
value-plus-tick append is supplied, and removes the value-zero/absence ambiguity
from its phase latch. Splitting either atomic event into unrecorded intermediate
operations would reopen the microscopic sufficiency question for that model.

## 5. Full record-state sufficiency and covariance

At every event boundary, the frame, header, tick prefix and actually present
outputs reconstruct s and sigma_s/Tr(sigma_s), including all work. There are
no states between atomic jumps with additional live evolution: during a wait
the normalized quantum state is constant. Since the next-event law and wait
rate are fixed functions of these same records, the FULL record configuration
is a sufficient Markov state at every time, not just macrocycle boundaries.
This proves sufficiency on the specified seed domain, not on arbitrary inputs
having identical records. Forgetting time does not forget any variable which
alters future probabilities in this particular law.

The quantum realization is genuine under the supplied tensor/Born/gate model:
the L operators apply the actual K operators to coherent native gauge data.
They retain the source's instrument identity with passive references. No
probability tree is substituted for those operators. Record sufficiency allows
an abstract classical representation of its trajectories, as it does for any
finite monitored quantum experiment; that does not replace the quantum proof.

Translate or properly rotate the entire prepared apparatus and every channel
in its recovered frame. Uniqueness of that frame makes the transported rule
single-valued on the entire orbit. This is covariance of an apparatus with a
prepared frame, not a homogeneous unframed vacuum or a coherent origin sum.
The gate alphabet and its quantum calibration remain the source's supplied
data. No additional algebraic covariance of their absolute matrix coordinates
is asserted beyond those premises.

## 6. Locality: the exact bounded claim

All records and operands lie in the finite box
0<=x<=max(10T,5n-1), -20<=y<=5n-1, 0<=z<=5n-1.
Its graph diameter is at most R=10T+15n+20. Each event's complete phase controls,
native gate operands, next tick and value target are within radius R of its
forming site. The law therefore has one fixed FINITE neighborhood radius R
for this chosen finite program. Its elementary U still acts on the source's
onsite/adjacent pair, and all native SWAP routing remains exactly that source's.

For the record-content kernel, match a target's radius-R condition against
legal predecessor records (with that target omitted), and assign the proved
next-content probabilities there. Else use the fair basis measure. This is
well-defined: two legal predecessors with the same neighborhood have the same
full seed/history/phase and hence the same probabilities. Occupied sites retain
support: immediately after their formation the predecessor odds still support
the realized value; after further ticks, deleting an older record gives a hole
and falls into the fair fallback. Initial records also fall in that fallback.
All recorded contents are basis projectors. Only legal enabled events form;
the fallback completes the conditional content law, not an extra event rate.

The clock enable and its native gate can be separated by O(R), so this theorem
does NOT prove nearest-neighbor actuation, a uniform range independent of T,n,
or a finite-speed native propagation law. Calling its gates adjacent does not
erase this control range. It closes the finite-neighborhood/autonomy question
under the literal current neighborhood wording, with the range fully priced.

## 7. Failed alternatives and precise next obligation

An unrecorded reversible/Feynman clock generally changes live states while R
is fixed and therefore does not by itself close record-only sufficiency. A
per-gate permanent tape placed in the original vertex pool lacks its required
capacity bound. A stored probability-tree program matches cylinders but does
not establish implementation of this quantum gauge register. An arbitrary
pre-herald input is excluded by the two-input witness in section 1.

A stricter local route is to unroll the quantum register spatially, move live
qubits through fresh computation cells, and accompany every gate/transport
with an adjacent irreversible clock tick. Old value records would stay fixed;
classical copies can travel as controls. This is only a proposal here: a
complete native layout, permanent-marker noninterference proof, local gate-
tick implementation and microscopic seed/reconstruction invariant have not
been completed. The exact remaining obligation is a uniform bounded-range
implementation of the L channels (or a replacement), including formation,
without unrecorded phase evolution. The present finite-radius construction
must not be relabeled as that stronger result or as an axiom-selected law.

## Checkpoint

Closed by explicit proof: finite-radius autonomous conditional gate/Record
process with permanent phase, full intermediate state reconstruction, exact
native circuit instruments, explicit finite storage and clock rate, and halt.
Still supplied: seed/calibration, gate and Born model, atomic jump/formation law
and gamma. Still open: uniform short-range physical implementation and law
selection. No axiom/prompt/audit file, branch, commit, or push was changed.
