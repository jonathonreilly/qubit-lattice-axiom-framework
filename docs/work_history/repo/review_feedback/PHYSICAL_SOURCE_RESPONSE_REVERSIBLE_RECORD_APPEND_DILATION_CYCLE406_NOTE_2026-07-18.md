# Physical source-response reversible Record-append dilation — Cycle 406

Date: 2026-07-18
Authority: none
Audit: unset

## Result

Cycle 406 gives Route B a constructive physical calculation that Cycle 403
did not have.  A blank preallocated Record register, proposal-payload register,
prior-Record register, local predicate inputs, work M2, and one retained
allocation-history M2 are attached to the exact Cycle-399 response interface.
A fixed connected-nearest-neighbor X/CNOT/Toffoli schedule then coherently
copies the Cycle-364 payload exactly when all of the following are present:

- the target content and occupied label are blank;
- the adjacent predecessor Record is occupied;
- readiness and fresh-interface labels are one;
- all 30 payload-presence labels are one;
- the site/payload/predecessor-bound provenance interface is accepted; and
- the exact Cycle-399 target-reservoir response label is one.

The circuit is the same for every input basis state.  There is no host branch
query, numerical threshold, sampled outcome, or state-dependent gate
selection.  It has an exact inverse on the enlarged binary domain and obeys

`E_406 G_406 = G_physical,406 E_406`

on the declared code space.

This does **not** yet compile the semantic Cycle-364 immutable append.  The
filled output is a coherent candidate label, not a framework Record.  The
global state still contains coherent blank and filled alternatives and the
same local circuit reverses either alternative.  No actual member is selected,
no dependency edge is added, and dependency depth remains four.  The retained
history label is not permanence or a Record.  No law or branch is selected.

All squared-norm quantities below are sector weight, not probability or Born
weight.  Dependency depth is a dimensionless partial-order certificate, not
proper time.  No physical energy or source stress is inferred.  No gravity or
axiom pressure is claimed.

## Exact enlarged-state circuit

The installed block contains 224 represented sites, one of which is the
existing local response-interface M2 already counted by Cycle 399.  The other
223 are new:

- 30 target-content M2 plus one target-occupied M2;
- 30 proposal-payload M2;
- 30 prior-content M2 plus one prior-occupied M2;
- 31 blank-match work M2;
- 66 prefix/bus work M2;
- 30 payload-presence M2;
- readiness, fresh-interface, and provenance M2; and
- one allocation-history M2.

The one-block schedule has 272 layers and 482 primitive gates.  Every gate is
X, CNOT, or Toffoli; every support has at most three sites and is connected by
nearest-neighbor edges in the declared cubic micro-layout.  Work sites are
preallocated, so the 223-M2 overhead is constant per candidate-append block.
Together with the Cycle-399 common installation this test uses 5,078 M2.  That
is a bounded resource count, not a minimum claim.

The calculation first complements the 31 target data/occupied bits and builds
a reversible conjunction prefix over those blank labels plus predecessor,
readiness, fresh, 30 presence, provenance, and response.  It copies the final
conjunction into allocation history while the target is still blank, then
uncomputes the complete conjunction workspace.  A local fanout bus transports
the retained bit alongside each target lane.  Toffoli gates copy all 30
proposal bits and a CNOT sets occupied; the bus and bridge work are cleaned.

Reverse order first removes occupied and the payload, rebuilds the blank
conjunction, clears allocation history, and cleans the work sites.  This is why
the history M2 is load-bearing for invertibility.  Dropping it would identify
a newly filled target with a target that was already filled before the call.
Cycle 406 retains the distinction rather than silently treating that many-to-
one projection as a reversible append.

## Blank and nonblank admission

Four basis cases are frozen before the held test:

| target input | response | output |
|---|---:|---|
| content zero, occupied zero | 1 | payload copied, occupied one, history one |
| content zero, occupied zero | 0 | unchanged blank target |
| lawful nonblank content, occupied one | 1 | unchanged pre-existing target |
| dirty content, occupied zero | 1 | unchanged malformed-blank target |

Every case has zero workspace leakage and is restored bit-for-bit by the
reverse schedule.  On the lawful blank cases, response zero agrees with the
Cycle-364 `blocked:faithful_close` answer and response one agrees branchwise
with its `formed` site, content, and predecessor.  The nonblank case agrees
with Cycle 364's `overwrite-rejected` answer.

The agreement is a branchwise content/interface comparison.  The physical
output decoder intentionally returns a `CoherentCandidateLabel`, not a
Cycle-364 `SiteContentRecord`.

## L5 and blind held-L6 response

The source law, depth three, initial column, exact target-reservoir projector,
compiler layout, payload packet, circuit, and readout are frozen before the
blind held L6 call.  The same dilation is applied at both orientations and for
both source routes.

| source route | A→C candidate-label sector weight | C→A candidate-label sector weight |
|---|---:|---:|
| unit-weight | `5.958479723237607e-06` | `5.958479723237605e-06` |
| coefficient-two | `3.0046754132975383e-05` | `3.004675413297537e-05` |

The L5 and blind held-L6 values agree without retuning.  In every case the
candidate-label sector weight equals the predeclared Cycle-399 target sector
weight.  The source routes remain quantitatively distinct and A/C reciprocity
is exact to the tested tolerance.

Before export the target/non-target response alternatives have nonzero
coherence.  After tracing only the 223 newly added M2, their reduced coherence
is zero because blank and filled register labels are orthogonal.  Globally no
branch is removed: the inverse residual is exactly zero in all eight
route/size/orientation cases.  This is coherent label export, not a frequency
or actualization rule.

## Proper-cubic covariance

All 24 proper-cubic frames are tested.  The Cycle-396 source update has maximum
covariance residual below `9.76e-15` and all 576 frame-group products close.
Every transformed X/CNOT/Toffoli support remains connected nearest-neighbor.

For each frame, the full Cycle-342 proposal and prior payloads are transformed
with the supplied payload mapping, the target and predecessor sites are
rotated, and the same lane-wise circuit is run.  The observed candidate label
equals the transformed reference label; the prior identity/payload is exact;
and the inverse restores the transformed input.  Payload-mapping, rotated-
support, candidate-answer, prior-preservation, and inverse failures are all
zero.

## Identity and physical fixtures

The payload-source register and the complete predecessor site/content packet
are controls or spectators; neither is modified.  Every coherent output branch
also preserves both Cycle-399 counter Record hashes, including their sites and
payloads.  The reference hash remains
`2bc2b272629ef89db2910d9598e8ef523f4ac3c2d998b8bf5ff1d719c5da11e7`.

Because the new gates act only on the added M2 and existing response label,
the matter-factor amplitudes and Cycle-399 bridge key are unchanged.  The
tested fixtures remain:

- Cycle-219 mass `0.4534056541748851`;
- global Q one;
- matter number `3.0 -> 3.000000000000002` within tolerance;
- zero coefficient-two and unit-weight local vector commutators; and
- 645 nontrivial Cycle-230 contact columns.

The six held matter Gram residuals remain at most `7.77e-16`; the inherited
Cycle-396 source intertwiner is below `9.76e-15`; and the new register
permutation intertwiner and enlarged inverse residuals are exactly zero.

## Deletion, leakage, and domain controls

Deleting any one of the following fixed gates prevents a valid decoded
candidate label:

- the allocation-history latch;
- one blank-detector inversion;
- one load-bearing payload-write Toffoli; or
- the occupied-write CNOT.

The payload-write deletion leaves an explicit content mismatch rather than a
silently accepted candidate.  Separately, removing the predecessor, readiness,
fresh-interface, one payload-presence label, or provenance blocks the
conjunction.  Nominal workspace leakage is zero.  Malformed word widths,
nonbinary response flags, and occupied/unoccupied predecessor aliases are
rejected at the declared encoder domain.

These tests distinguish a faulty reversible implementation from the semantic
question.  A deletion failure is not evidence for a shared substrate
obstruction.

## Record and actual-member audit

The constructive result is exact but narrower than a Record compiler:

- a conditional branch has the correct target, content, predecessor, and
  occupied label;
- the complete state is a coherent sum of branch labels;
- the allocation-history M2 keeps old-filled and newly-filled histories
  distinguishable;
- reversing the circuit deletes the candidate label exactly;
- no actual member, irreversible permanence condition, or framework append is
  supplied; and
- no new Cycle-170/255 event or load-bearing dependency edge exists.

Therefore causal depth is `4 -> 4`.  A candidate causal-depth response is
undefined, rather than five.  Calling the reversible filled register a Record
would erase the specific semantic distinction this probe was designed to
test.

This is an honest conditional semantic boundary for Route B, not an
impossibility, minimum-content theorem, shared obstruction, or axiom-pressure
claim.  The N1–N8 negative-claim gate is not triggered because no negative or
minimum claim is shipped.

## Supplied, derived, and open inventory

Supplied:

- Cycle 399's coherent source/counter common state, physical encoding,
  initial column, source depth, exact target-reservoir response interface, and
  prior counter Records;
- Cycle 364's lawful 30-bit payload grammar, predecessor Record, target and
  predecessor identities, presence/readiness/fresh/provenance interfaces;
- the 223 added M2, their blank/payload/prior/interface initialization, one
  allocation-history label, fixed micro-layout, and 272-layer circuit;
- finite L5/L6 boundaries, proper-cubic frames, and readout conventions.

Derived here:

- a fixed local coherent blank-admission and payload-copy circuit;
- exact workspace cleanup and enlarged-state inverse;
- branchwise Cycle-364 agreement, nonblank refusal, and all deletion controls;
- reciprocal L5/held-L6 candidate-sector weights;
- proper-cubic covariance, prior identity/payload preservation, and inherited
  physical-fixture preservation;
- the exact separation between a reversible candidate label and a framework
  Record.

Open:

- selection of this candidate law or any response branch;
- a physical irreversible/permanence rule that makes one output an actual
  framework Record;
- a corresponding load-bearing dependency edge and depth-five actual member;
- autonomous generation of all predicate interfaces;
- renewal, concurrent target allocation, and full-lattice capacity;
- normalized contextual statistics, frequency theorem, or Born law;
- metric normalization, interval/rate/proper time, physical source/stress,
  energy, or gravity interpretation.

No law or branch is selected.  No global ordering, parity service, host-side
branch query, probability/Born rule, proper-time claim, gravity law, or axiom
edit is used.
