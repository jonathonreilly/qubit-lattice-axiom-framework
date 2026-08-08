# Probability-readout underdetermination on a declared finite model: invisibility is forced, selection is not, and the existence premise selects nothing — Cycle 912

Date: 2026-08-04 (revised 2026-08-08, review loop iteration 1; file renamed
from `A3_CHANNEL_HALF_FORCED_...` — a bare premise code is not a lawful
primary science name)

Authority: none

Audit: unset

Status: bounded worked result, SELF-CONTAINED after review. Every
quantity is an in-file declared model or an explicitly stipulated
recorded count; the census/envariance closure the original block
consumed is not landed on origin/main and is carried below as
provenance context only.

Claim type: bounded_theorem (conditional on the declared model)

Runners:

- [`frontier_cycle912_a3_channel_2026_07_28.py`](../scripts/frontier_cycle912_a3_channel_2026_07_28.py)
- [`frontier_cycle912_a3_channel_independent_check_2026_07_28.py`](../scripts/frontier_cycle912_a3_channel_independent_check_2026_07_28.py)

Receipt:

- [`a3_channel_cycle912_receipt_2026_07_28.json`](../outputs/a3_channel_cycle912_receipt_2026_07_28.json)
- [`a3_channel_independent_check_cycle912_receipt_2026_07_28.json`](../outputs/a3_channel_independent_check_cycle912_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Review record (review loop iteration 1, Sol reviewer, 2026-08-08)

The original note claimed "the missing premise is exactly A3" — that
the probability-measure existence-and-state-functionality sentence
(shorthand "A3" in the historical envariance material) is the one
sentence separating the landed readout sentences from frequencies.
Review found this false as stated: the control that collapsed the
admissible simplex inserted a UNIFORM-COUNTING sentence ("the readout
assigns the same value to every record"), which is strictly stronger
than existence plus state-functionality; the existence premise is
satisfied by two distinct admissible probabilities and selects nothing.
Review also found that hash-collision-freedom on observed packed lane
states was promoted into "the digest partition IS the true
record-content partition" (an unproven bridge), that the original
checker assigned `pass = True` to substantive certificates and exited 0
regardless of survival, and that the entire computation consumed inputs
absent from this tree and unlanded on origin/main. The one-sentence
equivalence claim and the convergence claim with the orphaned
envariance note are WITHDRAWN and must not be cited as passed gates.
Both runners were replaced by self-contained fail-closed programs.

## Declared model (in-file stipulation)

Twelve record events in five content cells (sizes 4/3/2/2/1), with the
cell identifier playing the role of record content. The two landed-
sentence analogues are DECLARED for this model: additivity with
`I(empty) = 0`, and content determination ("a readout value is
determined by record content alone"). The identification of any
census weighting with the Record axiom's readout `I`, and the
identification of packed lane states with semantic Record content,
are OPEN bridges — no result below uses either.

## Result 1 — invisibility, conditional and exhaustive on the model

Under the declared sentences, every admissible readout is a function
of the record-content multiset alone: over all 48,352 content-preserving
pairs of event sets of the declared model, the coefficient difference
vector vanishes identically (exhaustive, exact). The checker probes
the same statement with 400 randomized cell-weight readouts and a
planted non-content-determined readout that its hunt correctly
separates.

## Result 2 — underdetermination: the sentences select no probability

The normalized non-negative content-determined weights form an affine
simplex of dimension `n_cells - 1` (= 4 on the model; vertex-rank
verified by two arithmetic routes). Two distinct admissible
probabilities are exhibited — uniform over content cells and uniform
over record events — with an explicit disagreement region. The
declared sentences constrain the SHAPE of a readout and select no
particular one.

## Result 3 — the existence premise does not select

The premise "a probability measure over outcomes exists and is a
function of the state" is satisfied by BOTH exhibited probabilities.
A premise satisfied by two distinct points selects neither: the
simplex dimension under the existence premise is unchanged (4 on the
model). The sentence that does collapse the simplex to a point is
uniform counting — a uniqueness/equiprobability sentence strictly
stronger than existence. **The target-equivalent missing lemma is a
selection/uniqueness law for the probability readout, and it is
OPEN.** The historical claim that the gap "is one sentence, namely the
existence premise" is not supported.

## Result 4 — recorded-scale arithmetic (stipulated counts)

Applying the same formula to the recorded census counts — 92,260
events, 52,018 content cells, stipulated from the uncertified prior
computation — gives the recorded simplex dimension 52,017. Only the
arithmetic is certified; the counts are provenance-scoped stipulations.

## Provenance context (non-load-bearing)

The original block computed on the unlanded Cycle-863/878/905/906/907
census stack and read an unmerged envariance branch
(`born-from-envariance-2026-06-05`). Its recorded outputs — the
content-measurability table (M1 0 violations; M2 85; M3 1,002; M4/M5
2,670; M6 5), the instrumented hash-preimage census (52,018 distinct
raw states, zero truncation collisions), the recovered envariance
note's `PASS=44` re-run, and the Cycle-909 recount corrections — are
recorded history from that uncertified computation. They certify
nothing here. Two specific promotions from that history are explicitly
OPEN bridges: packed-lane-state → semantic-Record-content (collision
freedom is a bijection on observed states, not this map), and
candidate-weighting → readout `I` (the "IF1-strong" reading). The
canonical Record-axiom sentences are in
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md); the
pointwise-evaluation primitive is
[REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md).

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "does the landed readout-sentence pair force a frequency readout, and what exactly is the missing sentence? (historical shorthand: the A3 channel)"
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "carry the corrected gap statement: additivity + content-determination force content-multiset invisibility and leave an (n_cells - 1)-dimensional simplex; the probability-measure existence premise does NOT select a point; the missing object is a SELECTION/UNIQUENESS law, which is open; the lane-state-to-record-content and weighting-to-readout-I bridges are open; census-scoped statements wait on the unlanded substrate"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: "Results 1-3 are conditional on the declared twelve-event/five-cell model and its declared sentence pair; Result 4 is arithmetic on stipulated recorded counts; the packed-state-to-record-content and weighting-to-readout-I identifications are OPEN bridges; no statement about the physical census or the envariance note's standing is certified"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exhaustive exact verification on the declared model by the primary, with the checker refuting by randomized functional probing, a planted non-content-determined readout, an independent vertex-rank route, and direct witness checking of the existence premise"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, stipulated definitions, open

### Stipulated definitions (declared scope inputs)

- the twelve-event/five-cell model and its two declared sentences;
- the recorded census counts 92,260 / 52,018 (uncertified history,
  arithmetic only).

### Imports

- none. The input closure contains no repository file beyond the
  paired runner/cache pins.

### Derived (conditional on the stipulations)

- content-multiset invisibility (exhaustive on the model);
- the (n_cells - 1)-dimensional admissible simplex with two exhibited
  distinct probabilities;
- the non-selection theorem for the existence premise, with the
  uniform-counting collapse as the strictly stronger contrast;
- the recorded-scale arithmetic 52,018 - 1 = 52,017.

### Open

- the selection/uniqueness law for the probability readout (the real
  missing object; not the existence sentence);
- the packed-lane-state-to-Record-content bridge;
- the weighting-to-readout-I identification ("IF1-strong");
- every census-scoped measurability verdict and the envariance-note
  landing question — all waiting on unlanded artifacts.

## Verdict

On a model small enough to check exhaustively, the landed sentence
pair does exactly two things: it makes every admissible readout blind
to anything but content, and it leaves a full simplex of admissible
probabilities standing. Adding "a probability measure exists and is a
function of the state" removes nothing from that simplex — two of its
points satisfy the premise and disagree. What would close the
frequency question is a selection law, which no landed sentence
supplies; naming that gap correctly is this note's only claim beyond
arithmetic. Independent audit still required.
