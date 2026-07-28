# Cycle 723: the refusal primitive wraps every controlled macro of the two-rail controller

Date: 2026-07-28

Authority: none

Audit: unset

Status: bounded conditional construction

Claim type: bounded_theorem

Primary runner:

- [`frontier_cycle723_refusal_wrapped_controller_2026_07_28.py`](../scripts/frontier_cycle723_refusal_wrapped_controller_2026_07_28.py)

Independent check:

- [`frontier_cycle723_refusal_wrap_independent_check_2026_07_28.py`](../scripts/frontier_cycle723_refusal_wrap_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

All controller ordinals, stations, and orbit counts are circuit structure.
None is called physical time, duration, rate, or energy.

## Result up front

Cycle 719 constructed a five-M2 local refusal primitive (`syndrome := B OR
work; data-X only if A AND NOT syndrome`) as a diagnostic at one station and
named, in its own N6/N7 sections, the strongest next closure: integrate that
refusal around **every** actual controller macro. Cycle 723 performs that
integration, reversibly, on the full padded 130-station two-rail controller:

- every controlled data macro (all 91 nonidentity stations; X, CNOT, and
  TOF lifts alike) is wrapped in a per-station reversible refusal sandwich:
  compute `syndrome_s ^= B_s OR work_s`; guard; every lifted primitive
  carries an additional NOT-syndrome control; unguard; uncompute. The
  sandwich is exactly reversible because `B_s` and `work_s` are invariant
  inside a Q station block, and each lifted Toffoli uses a fresh clean
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
- **dirty sectors are now refused at every macro, visibly**: exhaustively
  over all 91 nonidentity stations and both dirt kinds (`B_s = 1`,
  `work_s = 1`), the dirt bit survives to return, syndrome and scratch
  return clean, and the data output equals an independently constructed
  identity-substituted host prediction — 182 cases, zero mismatches, zero
  coincidental matches with the lawful output;
- deletion controls are active: removing one syndrome-compute gate produces
  33 data-bit mismatches at the affected station; removing one uncompute
  gate leaves a retained syndrome detected at return;
- the physical layer re-certifies on the extended layout (per-station
  syndrome and scratch sites below the work rail): placement collisions,
  cyclic rail nearest-neighbor checks, forward/inverse streaming routes
  (1,419,186 physical primitives, 17,945,266 routed NN gates at 12 banks),
  all 24 proper-cubic frames, 576 ordered products, and translations, with
  zero failures; the compiled wrapped orbit executes literally on all six
  Cycle-713 origin-zero branches with exact host equality and inverse; the
  Cycle-713 pin and mass/contact residual anchors rerun unchanged.

## The honest trade

The wrap **retires** the per-macro unchecked assertion that `B` and work
rails are clean: a dirty rail is now locally checked and the station's data
action is refused, with the dirt left visible rather than hidden. The wrap
**adds** to the supplied inventory: clean per-station syndrome and scratch
genesis (2P additional registers at P = 130 stations plus the scratch
pool). Unique token, ring geometry, program content, and clean data genesis
remain supplied exactly as in Cycle 719. `W1` is narrowed, not closed:
`w1_closed: false` is hard-coded in the report. No autonomy, genesis,
boundary-free, occurrence, Record, Born, or source claim is made.

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

`R1`/`R2` token swaps, the program rows, the Q-before-R order, and identity
stations are untouched. The unwrapped word is rebuilt in-runner as a
regression anchor and matches the Cycle-719 counters and digest before any
wrapped claim is made.

## Supplied / derived / open

### Supplied

- the Cycle-719 controller inventory unchanged: exactly one token at the
  source, the finite oriented program ring, program content and order,
  clean data/bank/link/route genesis, the landed matter law and coframe;
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

### Open

- unique-token and clean-syndrome/scratch genesis (the refusal checks
  rails; it does not prepare its own working registers or the token
  sector);
- autonomous edge scheduling, boundary-free geometry, renewal, and every
  inherited Cycle-719 open item (`W2`-`W7`) at its original scope;
- occurrence, physical time, permanent Record, Born weighting, and
  source/gravity meaning.

## Negative-claim discipline

No new negative claim ships. The refusal census and deletion controls are
sensitivity demonstrations on the declared construction; every "not
derived" statement restates a supplied convention or an inherited open item
at its original scope.

## Verdict and next experiment

The Cycle-719 steelman's named terminal test — "combine a locally checked
charge/token row with that refusal around every actual controller macro,
then require the forward/inverse manifests, suffix stabilizers, compiled
deletions, and coordinate checks unchanged" — is now executed on the
refusal half: the wrap is total, lawful behavior is byte-equivalent at the
certificate surface, and dirty rails are refused everywhere, at the cost of
a declared clean syndrome/scratch inventory. The remaining half of that
test is the locally checked token/charge row: the local Gauss/charge-sector
route (Cycle 703's reference note) toward unique-token enforcement is the
next queued leg, followed by the source-lift tournament definition recorded
in the campaign handoff. `W1` remains open until the token sector is
locally enforced rather than supplied.
