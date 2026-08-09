# Shard-partitioned fingerprint registers under formation-edge flips: exact finite support certificates — Cycle 877

Date: 2026-08-04 (revised 2026-08-08 and 2026-08-09 on physics review)

Authority: none

Audit: unset

Status: bounded support note (one worker-authored primary and one
independent checker spec'd to refute; no axiom surface touched).
Demoted on physics review from a submitted bounded-theorem wrapper: the
earlier headlines — that "the survival law is one wire", that full
record content is reconstructible from surviving shards, that the
result is "maximally local" or closes a record-locality story, that
contiguous blocks are a design rule, and that defeating sharding
"requires" k placed flips at a 70% formation-suppression price — are
all RETIRED and must not be cited from this note. What remains is the
exact finite content below.

Claim type: bounded_theorem (machine class for the exact finite
certificates; carried as a bounded support note, not as a main closure,
law, or negative claim)

Runners:

- [`frontier_cycle877_sharded_content_2026_07_28.py`](../scripts/frontier_cycle877_sharded_content_2026_07_28.py)
- [`frontier_cycle877_sharding_independent_check_2026_07_28.py`](../scripts/frontier_cycle877_sharding_independent_check_2026_07_28.py)

The independent checker is CLAIM-SCOPED and CO-LOAD-BEARING for this
note: the strided and hash-scattered boundary rules, the adversarial
single-flip sweep with its damage-size histogram (Result 4), and the
declared-tuple multi-flip observation exist only on the checker's
surface, and the checker is deliberately not imported by the primary,
so automatic import discovery cannot attach it to the audit packet. It
is declared as this note's packet helper runner in the Status fields
below, and its claim-scoped registration at landing is a hard landing
condition recorded in the Review record.

Receipt:

- [`sharded_content_survival_cycle877_receipt_2026_07_28.json`](../outputs/sharded_content_survival_cycle877_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: originally authored by a Claude Opus 5 worker under
supervisor spec (substitution disclosed). Revised 2026-08-08 and
2026-08-09 by a review-loop fix worker applying the physics review.
Independent audit still required.

## The instrument

Each stored "shard word" is a STIPULATED model convention: the live
payload projection (147 wires of the 5,815-wire state; 5,668 dead) is
cut into S blocks (S in {2, 4, 8}) that are contiguous in the ascending
list of live packed-state WIRE INDICES, and each block is digested to
the first 32 bits of SHA-256 over its bits. Three limits of that
convention are load-bearing for everything below:

- The digest map is NOT injective at these block sizes (at S=2 the 147
  payload bits map to 64 total digest bits; pigeonhole), and no decoder
  from stored words back to the payload exists in this package. Word
  equality is fingerprint agreement on the tested pairs, never payload
  reconstruction.
- Whether such a fingerprint corresponds to framework record content is
  an OPEN bridge that this package does not supply; no Record-axiom
  conclusion is drawn.
- "Contiguity" is wire-coordinate contiguity only. No map from wire
  indices or blocks to lattice sites, adjacency, or spatial regions is
  defined, so no physical-locality reading is available.

The words are written bit-by-bit into 14 disjoint structurally-dead
slot groups (577 slots total with the 129-slot existence register; zero
pairwise overlaps, zero gate inputs/targets, zero dead-activation
conflicts through the 16,384-orbit horizon) and read back from the
mutated state columns (0 readback-versus-host mismatches over 2,296
written words; register-versus-walked-trajectory agreement 448/448).
Every damage set below is computed by comparing the HOST-RESIDENT
perturbed and unperturbed states; nothing is inferred from the register
alone. Both runners are self-contained over the landed, sha-pinned
Cycle-719 kernel — their only computed input; census, seeds, schedules,
dirty partition, dead-wire pool, and sample selection are all derived
in-file.

## Result 1 — exact damage incidence on the six declared cells

The perturbation sides are FIXED banks: bank0 probes pack-state bank-0
payload wires, bank1 probes bank-1 payload wires (4 wires per side,
32 sample lanes with first-clean boundary <= 1,100). An earlier
revision labelled these sides "near"/"far" via a record-bank selector;
that selector was tautological (the accepted-candidate cleanliness
condition forces bank 0), so the near/far locality reading is RETIRED.

On the six direct-flip cells (one_flip 32/32 fired on both banks,
late_acting 13/13 and 25/25, untouched_in_chunk 19/19 and 15/15 — 136
fired direct probes), every fired probe's host-computed damage set was
exactly the flipped wire (mean = min = max = 1.0), although the
monotone structural forward cone would permit up to 295 wires. At every
S exactly one shard fingerprint changed, always the flip's own shard:
confined-to-flip-shard = 1.0 across all 18 cells, zero no-survivor
cells. In the flip-and-restore class (32/32 and 29/32 fired), every
fired probe returned to the baseline digest exactly.

Scope, stated plainly: this is a finite sample observation on six
declared cells under declared caps. It is not asserted as a one-wire
law and is not extended past those cells — the checker's own wider
sweep already contains one firing flip that damaged 10 wires
(Result 4) — and it is not a locality statement of any physical kind.

## Result 2 — fingerprint coverage, side-resolved and exact

Because the flipped shard's fingerprint always changed on the direct
cells, the all-shard-words-unchanged fraction is 0.0 there at every S,
honestly reported. The share of live wires lying in unhit shards is
exact integer arithmetic, and it is side-resolved because 147 is not
divisible by 2, 4, or 8:

| S | bank0 | bank1 |
|---|-------|-------|
| 2 | 73/147 = 0.496599 (hit block 74) | 74/147 = 0.503401 (hit block 73) |
| 4 | 110/147 = 0.748299 (hit block 37) | 110/147 = 0.748299 (hit block 37) |
| 8 | 128/147 = 0.870748 (hit block 19) | 129/147 = 0.877551 (hit block 18) |

The exact statement is: unhit fraction = 1 − |hit block|/147, with the
block-size branch shown. The compressed arrow 0.50 → 0.75 → 0.877 is a
rounded representative trend only; each doubling does NOT halve the
loss exactly. At one wire per shard the fraction would reach
1 − 1/147 = 0.993197 — an arithmetic endpoint of the convention, not a
measured recovery. None of this is reconstruction: it is bookkeeping
over host-computed damage under a stipulated fingerprint.

## Result 3 — slot arithmetic, exact under the stipulated conventions

Under the 32-bit word and 129-slot existence-register conventions:
S = 8 costs 385 slots (0.073 of the 5,270-slot safe pool); one shard
per wire costs 4,833 (0.917); the pool admits S ≤ 160, so payload
granularity (S ≤ 147) binds before the slot budget does. Exact
arithmetic, valid only under these declared conventions.

## Result 4 — the wider boundary sweep and its single 10-wire firing (checker surface)

The checker's adversarial single-flip sweep (12 lanes x 64 payload
wires = 768 probes, all 16 contiguous block-boundary wires included;
720 fired) found 719 firing flips that damaged exactly one wire and ONE
firing flip that damaged 10 wires — damage-size histogram
{1: 719, 10: 1}, published in full. That single firing is an EXISTENCE
observation inside this sweep's declared caps: a firing flip damaging
more than one wire exists in the model. It is the reason the one-wire
reading of Result 1 is stated only for the six declared cells and is
carried no further; nothing is asserted or denied about readings
outside these caps. In this sample the 10-wire case left no surviving
shard under the strided rules (S = 2, 4, 8) and the hash-scattered
rules (S = 2, 4), while the contiguous blocks lost at most 3 of 8
shards — a finite observation about one flip under fixed rules, not a
contiguity design rule.

Adjacent finite observation, exactly bounded: k-wire flips (k in
{2, 4, 8}) were run only at three DECLARED tuple offsets (first,
second, last payload wire of each targeted block) against the
contiguous S=8 partition. Those declared tuples fired in 11 of 36
probes at each k and, when they fired, killed exactly the targeted
number of shards. No optimization over tuples, no flip lower bound, and
no adversarial maximum was computed, so no attack-cost, suppression-
penalty, or necessity statement follows, and none is made.

## Review record

Physics review iteration 1 (Sol, 2026-08-08, disposition
FIX_THEN_PROCEED) demoted this note from its submitted bounded-theorem
wrapper to a bounded support note:

- The "reconstruction" claim ended at a target-equivalent gap: a
  truncated hash is neither the sharded payload nor a decoder, and the
  runner's success criterion used host-known damage. All reconstruction
  and recovery language is retired; the retained content is fingerprint
  agreement and unhit-wire coverage over host-computed damage
  (certificate C renamed accordingly on the runner surface).
- The one-wire "survival law" was restricted to the six declared sample
  cells, and the checker's wider sweep is now published as its full
  damage-size histogram (719 one-wire firings and one 10-wire firing)
  instead of being reported as "could not break the one-wire law".
- The k-flip necessity/attack-price claim ("defeating sharding requires
  k placed flips", "70% formation-suppression penalty") was withdrawn
  to a declared-tuple finite observation. No negative or necessity
  claim is carried anywhere in this package — the boundary sweep
  included, whose 10-wire firing is an existence observation and
  nothing wider — so no no-go discipline checklist exists for it and
  none may be cited.
- The near/far locality vocabulary was retired (tautological selector);
  sides are fixed bank0/bank1 pools on every surface. "Local"/
  "contiguous" are wire-coordinate properties; the physical-locality
  bridge is open.
- The exact side-resolved coverage fractions replaced the "exact curve
  ... halves the loss" compression (Result 2 table).
- Both runners were made self-contained over the landed Cycle-719
  kernel: the unlanded Cycle-863/867 ancestors and the stale pre-review
  Cycle-874 pins were removed from both input closures (pins, imports,
  blocklists, and reproduction gates); the replay-annotation and
  old-locality-cell controls were retired with them; the sample is now
  selected from the composed scan's own first-clean moments; the pool
  reproduction control now cites the landed Cycle-874 bounded support
  note. All emitted numbers reproduced exactly under the rewrite; logs
  and receipt were regenerated.
- Branch/campaign labels and unregistered status vocabulary were
  removed from all durable surfaces.
- The independent checker is co-load-bearing (Result 4 exists only on
  its surface) and is not imported by the primary, so import discovery
  cannot attach it to the audit packet. It is declared claim-scoped via
  the machine-readable `packet_helper_runner` line in the Status
  fields. HARD LANDING CONDITION: at landing, the orchestrator must add
  exactly this claim-scoped entry to `EXPLICIT_PACKET_HELPER_RUNNER_PATHS`
  in `docs/audit/scripts/build_citation_graph.py` (this stacked branch
  must not edit audit tooling):

  ```python
  "sharded_content_survival_law_cycle877_bounded_theorem_note_2026-07-28": [
      "scripts/frontier_cycle877_sharding_independent_check_2026_07_28.py",
  ],
  ```

Follow-up physics review round (Sol, 2026-08-09): the revision above
still turned the sweep's 10-wire firing into a universal negative about
one-wire readings the package had never tested. That sentence is
WITHDRAWN from every surface — note, review record, derived inventory,
verdict, both runners, both caches, and the receipt. What replaces it is
the bounded positive witness that was already there: the published
719 + 1 damage-size histogram, the single 10-wire firing stated as an
existence observation inside the declared caps, and the one-wire reading
scoped to the six declared cells. No figure, gate, certificate, or PASS
condition changed with this withdrawal.

## Trace gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "robust formation of record content under perturbation (owner goal); this package contributes finite model diagnostics only"
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "if reconstruction is to be decided, supply an injective encoding plus a decoder from stored register words to the payload and rerun without host-known damage; for any locality reading, define a wire-to-site map from the Lattice axiom; for any attack-cost statement, optimize over flip tuples and prove a lower bound; for the fingerprint-content bridge, derive or import a record-content identification"
```

## Status fields

```yaml
actual_current_surface_status: bounded support note
target_claim_type: bounded_theorem
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
packet_helper_runner: scripts/frontier_cycle877_sharding_independent_check_2026_07_28.py
claim_type_reason: "exact finite certificates only: the register write/readback construction (2,296 words, 0 mismatches), the six-cell damage-incidence tables on fixed bank0/bank1 pools, the gate-level monotone forward-cone superset check, the side-resolved coverage fractions 1 - |hit block|/147, the exact slot arithmetic (385, 4833, S<=160), and the checker's boundary sweep with its published damage-size histogram (719 one-wire firings, one 10-wire firing); the checker replicated the cells with a different allocator, arithmetic rank-map boundaries, and two extra shard rules, zero refutations; no reconstruction, locality, design-rule, negative, or necessity claim is carried"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports (stipulated definitions and explicit scope inputs only)

- the landed Cycle-719 kernel
  ([`frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py`](../scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py)),
  sha/blob-pinned in both runners and present on `origin/main` — the
  only computed input;
- the landed Cycle-874 bounded support note
  ([`COPY_REDUNDANCY_CONTENT_CYCLE874_BOUNDED_THEOREM_NOTE_2026-07-28.md`](COPY_REDUNDANCY_CONTENT_CYCLE874_BOUNDED_THEOREM_NOTE_2026-07-28.md)),
  cited as the certified source of the reproduced pool constants
  (5,668 dead wires; 5,270 safe slots) used as a control;
- the stipulated fingerprint convention: first 32 bits of SHA-256 over
  each block's bits (an explicit encoding convention; non-injective at
  the declared block sizes; carries no framework record-content
  meaning);
- the declared model conventions and caps, all visible in code and
  listed here: B=2 banks; the k=2..5 census (748 lanes); horizon 16,384
  orbits; dead-wire windows 512 orbits chunk-granular then 4,096
  orbit-granular; existence register cap 64 per (tag, lane); shard set
  S in {2, 4, 8}; sample 32 lanes with first-clean boundary <= 1,100
  and 4 payload wires per fixed side; the contiguous / strided /
  hash-scattered partition rules; the checker's 12-lane x 64-wire sweep
  caps; the three multi-flip tuple offsets (first, second, last);
  cost ladder up to S=512.

### Provenance context (non-load-bearing)

The design descends from the unlanded Cycle-863/867 line and the
pre-review Cycle-874 submission. Those artifacts are cited here as
history only: after the 2026-08-08 revision nothing in this package
reads, pins, imports, or gates on them, and no claim in this note
depends on their contents or their landing status.

### Derived (exact, within the declared scope)

- the balanced block decompositions and the checker's rank-map
  equivalence to them;
- the disjoint inert-slot write/readback construction (577 slots,
  2,296 words, 0 mismatches, 448/448 scan-versus-probe agreement);
- the six-cell damage-incidence tables on the fixed bank0/bank1 pools
  (finite samples; every fired direct probe damaged exactly the flipped
  wire in this sample);
- the gate-level monotone forward-cone superset lemma (exhaustively
  checked for the X/CNOT/Toffoli truth tables);
- the side-resolved coverage fractions 1 − |hit block|/147 and the
  exact slot costs 385, 4,833, and S_max = 160;
- the checker's 768-probe boundary sweep: of its 720 firing flips, 719
  damaged exactly one wire and one damaged 10 (histogram {1: 719,
  10: 1}, an existence observation inside the declared caps), plus the
  11/36 declared-tuple multi-flip observation.

### Open

- an injective encoding and decoder from stored register words to the
  payload, and with it any reconstruction claim;
- the framework record-content bridge for the stipulated fingerprint;
- a wire-to-site map, and with it any physical-locality reading of
  block contiguity or confinement;
- whether contiguity helps or hurts under an optimized adversary (the
  single 10-wire observation decides nothing);
- any attack-cost or necessity statement about multi-flip
  perturbations (requires optimization over tuples and a lower bound);
- the wider fault-model routes: coded/post-write faults, erasure of
  stored words, channel-local noise, decoders on a fixed message.

## Verdict

This package certifies exact finite results on a stipulated model over
the landed Cycle-719 kernel: a shard-partitioned fingerprint register
that writes and reads back without error; six declared sample cells in
which every fired direct flip damaged exactly its own wire and changed
exactly its own shard's fingerprint; side-resolved coverage fractions
and slot costs that are plain integer arithmetic; and a checker sweep
whose published damage-size histogram is 719 one-wire firings and one
10-wire firing, which is why the one-wire pattern is reported for the
sampled cells only and carried no further. It decides nothing about
record-content reconstruction, physical locality, contiguity as a
design principle, or the cost of defeating sharding — each of those
needs a bridge or a proof this package does not have. Independent audit
still required.
