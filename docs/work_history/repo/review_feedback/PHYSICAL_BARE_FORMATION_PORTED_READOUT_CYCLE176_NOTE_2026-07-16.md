# Physical bare formation followed by ported readout — Cycle 176

**Status:** constructive probe; audit unset.

**Companion runner:**
[`scripts/physical_bare_formation_ported_readout_cycle176_2026_07_16.py`](../../../../scripts/physical_bare_formation_ported_readout_cycle176_2026_07_16.py)

## Question

Can the current candidate substrate cleanly separate **formation then readout**?
That is:

1. two matching physical witnesses first make one signed-row record at an
   otherwise bare site;
2. only after that record forms, ordinary row transport carries it away; and
3. the transported record enters a frozen exterior decoder/fanout and is used
   by a complete downstream physical test?

This directly probes the conceptual route in which a record forms first and a
later read consumes or further distributes it. It does not define “read” or
“lock” by assertion.

## Frozen inputs

Cycle 176 consumes two frozen results:

- Cycle 173's cable-fed whole-row port and fifteen-leaf exterior decoder comb;
- Cycle 174's positive 96-row ingress law for two matching opposite row
  witnesses.

The Cycle 173 input is deliberately not treated as a bare formation site. Its
first comb path group has functional `MARK` furniture on the two transverse
faces. Those records are retained exactly. A new bare source is placed eighty
lattice steps outside that interface, and an ordinary row cable joins the two.

Only five inherited global-cage `FRAME` records in the cable's closed support
are removed. No functional `MARK`, decoder, reader, comparison, or cable
furniture is carved.

The merged candidate law has:

```text
Cycle-173 unified rows                 101,708
new opposite-witness ingress rows           96
merged rows                            101,804
deterministic conflicts                      0
```

## Result

The construction closes.

```text
initial records                      1,599,160
dynamic records                        133,525
declared dynamic edges                 133,544
causal roots                                11
source depth                                  1
cable-fed P-input depth                       81
first comb splitter depth                     82
selected payload decoder depth                93
membership-output depth                    8,075
```

Every one of the 133,525 declared writes compiles to exactly its expected
record. Removing each of the 133,544 dynamic parents separately suppresses
its intended child. All 24 proper-cubic images compile, covering 3,204,600
transformed dynamic-site checks.

Both complete physical scheduler extremes close with no residual enabled site:

```text
order       frontier work   maximum frontier   final source/port/output
minimum         2,175,861                 27    row / row / H1
maximum         1,557,139                 21    row / row / H1
```

## Exact causal statement

The intended physical order is:

```text
two matching witnesses
          ↓
 one newly formed P row
          ↓
 ordinary row transport
          ↓
 frozen Cycle-173 comb splitter
          ↓
 decoder payload leaf
          ↓
 signed-membership output
```

The source has exactly the two row witnesses at opposite faces and no fixed
record on its other four nearest-neighbor faces. The downstream input keeps
Cycle 173's functional transverse `MARK` pair and is reached by cable, as its
frozen contract requires.

Every declared dynamic edge is tested against the actual local law. The full
dependency depth must place the formed source before the cable endpoint, comb
root, selected payload decoder, and final membership output.

## Deletion distinctions

The probe requires three physically different controls.

- Delete either of the **two matching physical witnesses**: the source record
  must not form, the port must not be reached, and downstream readout must
  remain absent.
- Delete a load-bearing fixed guard on one **payload-only deletion** branch:
  the source record and cable-fed port must still form, while the downstream
  membership output remains absent.

This prevents the two formation witnesses from being renamed payload copies.
It also prevents successful source formation from being inferred merely
because a later readout happened.

Both witness deletions remove 66,898 causal descendants and leave:

```text
source absent / cable-fed port absent / membership output absent
```

The first witness deletion also reconstructs the affected radius-one
enablement set from the full initial frontier and compares it with a fresh
global open-candidate scan. They agree exactly.

The payload-only deletion removes 1,967 descendants and leaves:

```text
source present / cable-fed port present / membership output absent
```

## What the positive result means

The positive result shows that the current finite substrate can represent
the sequence “form first, then transport and read” without placing readout
furniture in the formation neighborhood and without adding a contextual
marker to the bare formation rule.

That makes the second conceptual route materially stronger than
“formation is identical to being read.” It shows a real intermediate
record whose existence can be separated by deletion from one later payload
use.

More precisely, the runner proves exact local enablement and causal closure
under both exhaustive lawful scheduler extremes. It proves that every
required event is enabled by the stated record neighborhood when its parents
exist, that every declared parent is load-bearing, and that every lawful
completion tested reaches the same clean terminal corpus.

It does **not** derive which one of several simultaneously enabled events
actually occurs next. It supplies no scheduler-selection law, fairness
condition, occurrence rate, probability weight, or Born frequency. It also
does not explain the first record or a cosmological seed. Those are distinct
framework gaps and are not hidden inside the successful causal replay.

The signed whole-row roles used here are extensional record-law labels in M2.
This runner does not yet show that they are a nondisturbing, physically
distinguishable 32-symbol qubit code. The formation/readout causal separation
is exact at the record-law level; a five-bit orthogonal spatial compile or an
equivalent CP/instrument bridge is still required before calling the apparatus
a literal qubit implementation.

## Scope

This is not yet a two-stage Cycle-166 stabilizer update. The recurrent output
rows of one complete stabilizer update have not yet been routed into the next
update's generator inputs in this runner. That serial-stage integration
remains the next compiler test. In particular, the stock next-stage generator
readers are not cable-fed whole-row ports; like the stock measured-row reader,
they require exterior source-interface recompilation. This is a compiler
residual under the current law, not evidence by itself for new axiom content.

This is not a universal record-formation theorem, probability result, Born
rule, Lüders theorem, clock theorem, metric-time result, or storage-capacity
law. It does not establish that two witnesses are necessary in every physical
realization.

It does not choose axiom language. The 96-row ingress remains a candidate-law
probe whose constitutional status must be decided only after the remaining
routes and serial-stage integration are compared.

No axiom, primitive, registry, policy, or audit edit follows.
