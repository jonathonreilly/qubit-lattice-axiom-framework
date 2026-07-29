# The genesis word, self-verified by its own certificate — Cycle 732

Date: 2026-07-28

Authority: none

Audit: unset

Status: bounded conditional theorem

Claim type: bounded_theorem

Runners:

- [`frontier_cycle732_genesis_word_self_verification_2026_07_28.py`](../scripts/frontier_cycle732_genesis_word_self_verification_2026_07_28.py)
- [`frontier_cycle732_genesis_independent_check_2026_07_28.py`](../scripts/frontier_cycle732_genesis_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

Cycle 731 enforced the token-count law but left W1's remaining gap as
the declared inventory itself: `expected_count = 1` was a supply line.
This cycle moves that boundary one level down. A **genesis word** — 27
literal M2 gates (one X, twenty-six CN; fixed unrolling from the
layout, no runtime Python branch) — prepares the full lawful genesis
configuration from the all-blank state, and composes with the certified
Cycle-731 word so the preparation is **verified by the machine it
feeds**:

- **genesis exactness**: on ring-11 (full width 5,979) and the 2-bank
  fixture, the genesis word's output is bit-exact against the declared
  lawful configuration in every register (source token, references,
  `h`, data, and all blanks — zero mismatches);
- **composed self-verification**: genesis + certified word = 123,293
  semantic gates (frozen sha); the certificate accepts the genesis
  output; all auxiliaries return clean; the literal reverse is exact;
  the Cycle-731 anchor (112,912 gates) and its full 8,388,608-case
  theorem rerun unchanged in-package with the same frozen outcome-table
  sha;
- **corrupted preparation is refused**: an exhaustive single-gate
  deletion sweep over the genesis word — **all 27 deletions produce
  unlawful outputs and every one is refused** by the composed
  certificate (zero output-neutral deletions); all 23 single-bit
  corruptions of the genesis output on the A-rail/references/`h` are
  refused, in exact agreement with the Cycle-731 theorem's predicted
  verdicts case by case;
- **no hidden selection**: AST audit — the genesis word is fixed
  unrolling with no data-dependent branch; the gate census is printed;
  the physical layer routes the word collision-free with returned work;
  the Cycle-713 pins are byte-unchanged.

After this cycle the supplied items are the all-blank state and the
genesis word **as a convention**; the one-token inventory is no longer
a separately declared supply (`one_token_inventory_separately_declared:
false`) — it is the machine-verified output of a physical preparation
word whose errors are refusals.

## Supplied / derived / open

### Supplied

- the all-blank M2 state on the declared ring-11 register layout;
- the selected literal genesis-word gate ordering (a convention —
  stated plainly: word **selection** remains supplied even though word
  **correctness** is now machine-enforced);
- the ring-11/two-bank oriented program and physical layout convention;
- the unchanged Cycle-731 certificate word and pins.

### Derived

- the genesis word's bit-exact preparation of the lawful configuration;
- the composed self-verifying word and its exact reversibility;
- the exhaustive deletion and bit-flip refusal censuses with exact
  Cycle-731 theorem agreement;
- the unchanged inherited anchors.

### Open

- W1's narrowed remaining gap: the genesis word **selection** — deriving
  the preparation convention itself from the axioms (occurrence/Record
  structure), not just enforcing its correctness;
- uniform ring families beyond the held fixtures; everything the landed
  surfaces leave open at their scopes; no time/Record/Born/source
  content is touched.

## Negative-claim discipline

No negative claim ships. The zero-output-neutral deletion census is a
completeness statement about this genesis word on these fixtures, not a
general theorem about all preparation words.

## Verdict

The W1 supply chain is now: all-blanks → genesis word (supplied
convention, enforced correctness) → one-token configuration (derived,
verified in-word) → count law (enforced) → parity law (enforced). Each
arrow is a literal physical word with refusal semantics; the one
remaining declared item on this chain is the genesis word's selection.
Independent audit still required.
