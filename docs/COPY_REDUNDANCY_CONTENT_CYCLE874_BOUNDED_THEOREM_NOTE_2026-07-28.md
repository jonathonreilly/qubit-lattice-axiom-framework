# Whole-state-digest replication on dead-wire registers: exact finite support certificates — Cycle 874

Date: 2026-08-03 (revised 2026-08-08 on physics review)

Authority: none

Audit: unset

Status: bounded support note (one worker-authored primary and one
independent checker spec'd to refute; no axiom surface touched).
Demoted on physics review from a submitted negative bounded-theorem
wrapper: the earlier headline — that copy redundancy does not protect
record content, that the restore contrast is a near/far locality
effect, and that sharding is the protective lever — is RETIRED and must
not be cited from this note. What remains is the exact finite content
below.

Claim type: bounded_theorem (machine class for the exact finite
certificates; carried as a bounded support note, not as a main closure
or negative claim)

Runners:

- [`frontier_cycle874_copy_redundancy_content_2026_07_28.py`](../scripts/frontier_cycle874_copy_redundancy_content_2026_07_28.py)
- [`frontier_cycle874_redundancy_independent_check_2026_07_28.py`](../scripts/frontier_cycle874_redundancy_independent_check_2026_07_28.py)

Receipt:

- [`copy_redundancy_content_cycle874_receipt_2026_07_28.json`](../outputs/copy_redundancy_content_cycle874_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: originally authored by a Claude Opus 5 worker under
supervisor spec (substitution disclosed). Revised 2026-08-08 by a
review-loop fix worker applying the iteration-1 physics review.
Independent audit still required.

## The instrument

The stored "content word" is a STIPULATED model convention: the first
32 bits of SHA-256 over the packed lane state with every register slot
wire zeroed. It is a model-defined state fingerprint and nothing more.
Whether such a fingerprint corresponds to framework record content —
one admissible local possibility locked by a record — is an OPEN bridge
that this package does not supply; no Record-axiom or locality
conclusion is drawn here.

The word is written bit-by-bit into R disjoint structurally-dead slot
groups (R in {1,2,3}; 321 slots, zero pairwise overlaps, zero gate
inputs/targets, zero dead-activation conflicts through the horizon) and
read back from the mutated state columns (0 readback-versus-host
mismatches over 977 written words). Both runners are self-contained
over the landed, sha-pinned Cycle-719 kernel — their only computed
input; census, seeds, schedules, dirty partition, and dead-wire pool
are all derived in-file.

## Result 1 — an exact common-mode identity, not a redundancy no-go

Across R = 1 → 3, in the two declared modes (replicated; staggered at
consecutive clean edges) and the checker's 4x-wider deep-staggered
scheme, zero of eight majority-readback cells change and the
flip-and-restore bank gap is flat in R (0.09375 replicated, 0.107143
staggered, at every R).

Read this exactly: every perturbation in this package changes the
SOURCE state BEFORE any copy is formed, so all copies of a perturbed
walk digest the same changed state. For identical replicas,
majority([w]*R, R) = w for every tested R — the replicated-mode
R-invariance is forced by the construction. The staggered copies are
different-time digests of one trajectory (register agreement only
115/157 lanes at R=3), not independent transmissions of one fixed
word. No stored copy slot is ever mutated, erased, or read under a
fault after writing.

This is therefore NOT a copy-redundancy no-go. Untested routes, named:
post-write faults on a proper subset of the allocated copy groups,
erasure of selected copies, channel-local noise, error-detecting or
erasure codes rather than raw repetition, and any decoder acting on a
fixed message. The obvious partial closure — fault a proper subset of
the already-allocated disjoint dead-wire copy groups after writing and
test reconstruction of the fixed baseline word — needs no new axiom and
was not exercised here.

## Result 2 — fixed-bank restore decomposition (no locality reading)

The perturbation sides are FIXED banks: bank0 probes pack-state bank-0
payload wires, bank1 probes bank-1 payload wires. An earlier revision
labelled these sides "near"/"far" via a record-bank selector; that
selector was tautological (the accepted-candidate cleanliness condition
forces bank 0), so the near/far locality reading is RETIRED. Whether
the bank0/bank1 asymmetry reflects distance from a record or mere
bank-order asymmetry is undetermined until a non-tautological
record-location definition and a bank-swap control are run.

The exact sampled numbers: in the flip-and-restore class, bank0 fired
32/32 and bank1 29/32 (replicated; 28/28 and 25/28 staggered), and
every fired restore probe returned to the baseline digest —
content_gap_given_fired = 0.0 exactly, both modes, at every R. The
3/32 and 3/28 gaps are firing gaps between the two fixed banks in this
sample.

Scope limits, stated plainly: the zero conditional content gap holds
for the flip-and-restore class ONLY. In every direct-flip class the
probes fired with changed content (one_flip 32/32 fired and 0
content-equal on both banks; late_acting 13/13 and 25/25 fired, 0
content-equal; untouched_in_chunk 19/19 and 15/15 fired, 0
content-equal), so no "content survives whenever formation fires"
generalization is available. The three unfired bank1 restores were
checked only at the selected formation boundary; nothing here
establishes a permanent trace at later times.

## Result 3 — a projection-shard partial observation

The checker's projection-sharded scheme (each copy digesting a
different state block: bank-0 rows, bank-1 rows, link rows + source
pointer) shows any_copy_survives_at_R3 = 1.0 for one_flip, late_acting,
and untouched_in_chunk on both banks: at least one of the three
disjoint shard digests remains equal to its own baseline under every
sampled direct single-wire probe.

That is the whole result. It does not show that the original word, the
changed shard, or any complete content can be reconstructed from
surviving shards — reconstruction is target-equivalent to a content-
protection claim and is untouched here. "Sharding is the lever" is
RETIRED; the observation is carried as adjacent support only.

## Review record

Physics review iteration 1 (Sol, 2026-08-08, disposition
FIX_THEN_PROCEED) demoted this note from its submitted negative
bounded-theorem wrapper to a bounded support note:

- The redundancy negative failed no-go discipline (N1, N3, N5, N6, N7,
  N8): the probes are common-mode source perturbations, no stored-copy
  fault model was declared or exercised, and the replicated
  R-invariance is an identity of the construction. A compact
  negative-claim discipline paragraph that previously stood here is
  REMOVED and must not be cited as a passed gate.
- The near/far locality reading rested on a tautological record-bank
  selector (verified: the selector constant-folds to bank 0); the cells
  are retained only as fixed bank0/bank1 sample counts.
- The unqualified "content never dies in a record that forms" verdict
  contradicted the runner's own direct-flip cells and is retired; the
  fired-conditioned zero gap is stated for the flip-and-restore class
  only.
- The sharding-protection conclusion stopped short of reconstruction
  and is retained only as the partial observation in Result 3.
- The framework-Record identification of the truncated SHA-256
  fingerprint is declared an open bridge; the digest is a stipulated
  model convention.
- Both runners were made self-contained over the landed Cycle-719
  kernel: the unlanded Cycle-863/866/867 ancestors were removed from
  both input closures (pins, imports, blocklists, and reproduction
  gates), the replay-annotation and landed-867 comparison controls were
  retired with them, and the sample is now selected from the composed
  scan's own first-clean moments. All emitted numbers reproduced
  exactly under the rewrite; logs and receipt were regenerated.

## Trace gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "robust formation of record content under perturbation (owner goal); this package contributes finite model diagnostics only"
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "if the redundancy question is to be decided, declare a fault model on the stored copies (post-write subset faults / erasure / channel-local noise) and a decoder on a fixed message, then rerun; for any locality reading, define a non-tautological record-location selector and run a bank-swap control; for the shard observation, attempt reconstruction from surviving shards"
```

## Status fields

```yaml
actual_current_surface_status: bounded support note
target_claim_type: bounded_theorem
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact finite certificates only: write/readback construction, the forced common-mode R-invariance identity, fixed-bank restore tallies, and the shard partial observation; the checker replicated with a different allocator and wider schemes, zero refutations; no negative, locality, framework-record, or protection claim is carried"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports (stipulated definitions and explicit scope inputs only)

- the landed Cycle-719 kernel
  ([`frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py`](../scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py)),
  sha/blob-pinned in both runners and present on `origin/main` — the
  only computed input;
- the stipulated content-word convention: first 32 bits of SHA-256 over
  the packed lane state with register slots zeroed (an explicit
  encoding convention; carries no framework record-content meaning);
- the stipulated decoder: strict bitwise majority, even-R tie → 0;
- the declared scope caps: B=2 banks, k=2..5 census (748 lanes),
  horizon 16,384 orbits, dead windows 512/4,096 orbits, existence
  register cap 64, 32-bit words, R ≤ 3, stagger walk cap 64, sample 32
  lanes with first-clean boundary ≤ 1,100, 4 payload wires per side.

### Provenance context (non-load-bearing)

The design descends from the unlanded Cycle-863/866/867 line (time-from-
records replay substrate, composed record-write model, and their finale
checker). Those artifacts are cited here as history only: after the
2026-08-08 revision nothing in this package reads, pins, imports, or
gates on them, and no claim in this note depends on their contents or
their landing status.

### Derived (exact, within the declared scope)

- the disjoint inert-slot write/readback construction (0 mismatches,
  977 words, 321 slots);
- the common-mode R-invariance identity of majority readback (both
  modes, plus the checker's deep-staggered scheme);
- the fixed-bank flip-and-restore decomposition: firing gaps 3/32 and
  3/28 with zero fired-conditioned content gap in this sample;
- the shard partial observation (at least one unchanged shard digest
  under every sampled direct flip).

### Open

- the framework record-content bridge for the stipulated fingerprint;
- a declared fault/channel model on stored copies, and with it any
  actual redundancy verdict;
- a non-tautological record-location selector plus bank-swap control,
  and with it any locality reading of the bank gap;
- reconstruction from surviving shards;
- persistence of the unfired-restore discrepancy beyond the formation
  boundary.

## Verdict

This package certifies four exact finite results on a stipulated model
over the landed Cycle-719 kernel: the register construction, a
constructionally forced common-mode R-invariance, a fixed-bank
restore-firing decomposition, and a shard-survival partial observation.
It decides nothing about whether copy redundancy protects record
content — that question needs a stored-copy fault model this package
does not have. Independent audit still required.
