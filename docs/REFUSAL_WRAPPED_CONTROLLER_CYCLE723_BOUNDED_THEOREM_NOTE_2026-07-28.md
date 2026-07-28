# Per-station reversible refusal wrapper for the two-rail controller

Date: 2026-07-28

Authority: none

Audit: unset

Status: proposed_retained; bounded theorem under the supplied inventory below

Claim type: bounded_theorem

Primary runner:

- [`frontier_cycle723_refusal_wrapped_controller_2026_07_28.py`](../scripts/frontier_cycle723_refusal_wrapped_controller_2026_07_28.py)

Independent check:

- [`frontier_cycle723_refusal_wrap_independent_check_2026_07_28.py`](../scripts/frontier_cycle723_refusal_wrap_independent_check_2026_07_28.py)

All controller ordinals, stations, and orbit counts are circuit structure.
None is called physical time, duration, rate, or energy.

## Result up front

The
[recurrent matter-to-history controller](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md)
constructed a five-M2 local refusal primitive (`syndrome := B OR work; data-X
only if A AND NOT syndrome`) as a one-station diagnostic. This bounded theorem
integrates that primitive, reversibly, around **every** controlled macro of the
full padded 130-station two-rail controller:

- every controlled data macro (all 91 nonidentity stations; X, CNOT, and
  TOF lifts alike) is wrapped in a per-station reversible refusal sandwich:
  compute `syndrome_s ^= B_s OR work_s`; guard; every lifted primitive
  carries an additional NOT-syndrome control; unguard; uncompute. The
  sandwich is exactly reversible because `B_s` and `work_s` are invariant
  inside a controlled-macro station block, and each lifted Toffoli uses a clean
  scratch pool, never the dirty decomposer bit;
- the wrapped `H` word has 95,850 gates (against 61,562 unwrapped) and
  stays in the self-inverse classical X/CNOT/TOF/MCX family, with the
  literal reversed word verified as its exact inverse;
- **lawful behavior is unchanged**: for the supplied one-token/clean
  genesis, wrapped `H^P` reproduces the allocator result on the held
  2/5/12-bank programs and the padded 130-station program; `A` returns to
  `A_0`; `B`, work, syndrome, and scratch all return to zero; the reversed
  word restores the complete input; the zero/adjacent/distant/offset token
  sector controls keep their lawful-zero counters and hostile residuals;
- **dirty sectors are refused at every macro, visibly**: the literal compiled
  word is executed for all 91 nonidentity stations and both dirt kinds
  (`B_s = 1`, `work_s = 1`). In all 182 cases the dirt bit survives to return,
  syndrome and scratch return clean, and the data output equals an
  independently constructed identity-substituted prediction. Five cases
  contain an output-active refused macro and all five differ from the lawful
  fixture; the other 177 cases coincide with the lawful fixture because the
  refused macro is inactive on that particular data state;
- deletion controls are active: removing one syndrome-compute gate produces
  33 data-bit mismatches at the affected station; removing one uncompute
  gate leaves a retained syndrome detected at return;
- the physical-layer checks pass on the extended layout (per-station syndrome
  and scratch sites below the work rail): placement collisions, cyclic rail
  nearest-neighbor checks, forward/inverse streaming routes (1,419,186
  physical primitives, 17,945,266 routed NN gates at 12 banks), coordinate
  round trips under all 24 proper-cubic frames, closure of their 576 ordered
  products, and translation round trips all have zero failures. The compiled
  wrapped orbit executes literally on all six parent endpoint-instrument
  origin-zero branches with exact host equality and inverse; the parent
  endpoint-instrument pin and mass/contact residual anchors rerun unchanged.

## The honest trade

The wrap replaces an unchecked clean-`B`/work precondition at each controlled
macro with an explicit local check: a dirty rail suppresses the station's data
action and remains visible. The wrap **adds** clean per-station syndrome and
scratch genesis to the supplied inventory (2P additional registers at P = 130
stations plus the scratch pool). The unique token, oriented ring geometry,
program content, and clean data genesis remain supplied. The theorem is only
about the declared finite reversible circuit under that inventory.

## Construction detail

The station block, for a macro word `W_s` on data wires:

```text
CN(B_s, synd_s); CN(work_s, synd_s); TOF(B_s, work_s, synd_s)   # compute OR
X(synd_s)                                                        # guard on
  X(t)        -> TOF(A_s, synd_s, t)
  CNOT(c,t)   -> MCX((A_s, synd_s, c), t, scratch)
  TOF(c1,c2,t)-> MCX((A_s, synd_s, c1, c2), t, scratch)
X(synd_s)                                                        # guard off
TOF(B_s, work_s, synd_s); CN(work_s, synd_s); CN(B_s, synd_s)   # uncompute
```

The two token-swap layers, program rows, controlled-macro-before-swap order,
and identity stations are untouched. The unwrapped word is rebuilt in-runner
as a regression anchor and matches the parent-controller counters and digest
before any wrapped claim is made.

## Supplied / derived / scope

### Supplied

- the
  [parent controller inventory](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md)
  unchanged: exactly one token at the source, the finite oriented program
  ring, program content and order, clean data/bank/link/route genesis, and the
  bounded matter-law/coframe surface declared there;
- NEW: clean per-station syndrome and scratch genesis (the refusal
  sandwich's working registers).

### Derived

- a reversible refusal wrap of every controlled data macro on the padded
  130-station program, lawful behavior unchanged (held 2/5/12 and padded,
  forward and inverse, sector controls preserved);
- the exhaustive 182-case dirty-rail refusal census with independent
  identity-substituted predictions and zero mismatches;
- active deletion controls on the compute and uncompute legs;
- the extended physical layer with zero route/frame/product failures and
  the literally executed wrapped orbit on all six branches;
- regenerated counts and digests (95,850-gate wrapped `H`; physical and
  routed totals above).

### Outside this theorem

The claim stops at reversible circuit semantics for the supplied finite
controller and register inventory. It neither derives that inventory nor
assigns physical time, occurrence, Record, Born weighting, or source/gravity
meaning to the controller ordinals.

## Conclusion

The refusal wrapper is total on the declared controller: lawful behavior is
byte-equivalent at the certificate surface, and the literal compiled word
matches independent identity-substituted predictions for every tested dirty
rail, at the declared cost of clean syndrome/scratch genesis. Independent
audit remains required before the row may receive any retained-grade status.
