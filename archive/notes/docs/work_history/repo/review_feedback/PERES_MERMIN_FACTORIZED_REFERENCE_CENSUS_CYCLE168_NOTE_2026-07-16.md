# Peres–Mermin factorized reference census — Cycle 168

**Type:** bounded_theorem

Status: retained-grade source note for a bounded finite reference certificate.
No audit-ledger verdict is issued here.

Authority: conditional on the already retained finite component tables and the
declared two-qubit stabilizer / Peres–Mermin reference domain. This note changes
no axiom, primitive, registry, policy, or audit surface.

## Question

Does the factorized composition of the retained signed-row readers, Boolean
ALU, equality chain, symplectic checker, commuting multiplier, four-case
update, and product/parity checker reproduce the complete finite
Peres–Mermin stabilizer reference census?

## Result

Yes, on the exact finite domain tested.

The primary runner exhausts

```text
60 pure two-qubit stabilizer states
× 6 ordered generator bases per state
× 6 Peres–Mermin contexts
× 6 measurement orders
× 8 candidate sign triples
= 103,680 transcripts.
```

For every transcript, the factorized result agrees with the compact tableau
reference on:

1. support or rejection and the first rejecting step;
2. the supported conditional update and final stabilizer group;
3. the unsigned context product;
4. scalar outcome-sign parity;
5. the full signed-row product; and
6. the final conjunction terminal.

The exact global census is:

```text
attempts                                      103,680
supported                                      38,880
rejected                                       64,800
first rejection at step 1                      10,368
first rejection at step 2                      15,552
first rejection at step 3                      38,880

scalar parity q = unsigned context sign u       51,840
scalar parity q != unsigned context sign u      51,840
q = u and supported                             38,880
q = u and rejected                              12,960
q != u and supported                                 0

unsigned product +II                            86,400
unsigned product -II                            17,280
full signed product +II                         51,840
full signed product -II                         51,840

supported unsigned +II                          32,400
supported unsigned -II                           6,480
supported full signed +II                       38,880
supported full signed -II                            0
supported third step deterministic              38,880
terminal H1                                     38,880
```

Each context contributes exactly:

```text
attempts                       17,280
supported                       6,480
rejected                       10,800
q = u                           8,640
q != u                          8,640
q = u and supported             6,480
q = u and rejected              2,160
```

Each of the 36 context/order cells contributes exactly
`2,880 / 1,080 / 1,800` attempts / supported / rejected.

The single-stage preflight independently covers all 10,800
state-basis/signed-Pauli inputs:

```text
supported                       9,720
rejected                        1,080
anticommuting update            8,640
commuting membership            1,080
commuting opposite              1,080
```

The checker preflight covers all 288 context/order/sign inputs. It has
`144/144` equal/different scalar parities, `144/144` positive/negative full
signed products, and `30/6` positive/negative unsigned context-order products.

The complete factorized census is basis- and order-invariant in the claimed
result signature: 17,280 classes produce 86,400 nonreference comparisons in
each invariance test. It exposes 38 stage-type shapes and 76 representative
keys for a later routed-geometry campaign.

## Correct Peres–Mermin semantics

The six declared unsigned contexts have products

```text
R1, R2, R3, C1, C2 -> +II
C3                 -> -II.
```

Let `u` be that unsigned-product sign and `q` the parity of the three scalar
outcome signs. A lawful completed context requires `q = u`. Therefore the
three full signed outcome rows multiply to `+II` in every supported completed
context, including `C3`: its odd scalar sign cancels its unsigned `-II`.

The census also shows why the parity checker is not itself the state-support
test. There are 12,960 `q = u` candidate histories rejected by the sequential
state update. Conversely, no `q != u` history is supported.

## Independent audit

The Cycle-168 verifier reconstructs the 60 pure stabilizer groups from named
two-letter Pauli strings and an explicit one-qubit multiplication table. It
does not import the compact symplectic tableau implementation for that
calculation. Its independent stage, checker, transcript, per-context, and
per-context/order counts equal the primary runner's exact totals.

This closes a shared-implementation risk in the numerical census. It does not
turn a mathematical reference calculation into a physical execution.

## Oracle and host boundary

The exact boundary is load-bearing.

The imported component tables were populated in their predecessor modules
from algebraic reference values before the dynamic firewall is installed.
The present result is therefore a finite composition certificate conditional
on those retained component tables, not an oracle-free synthesis of those
tables.

After the imported tables exist:

- the Cycle-168 cache assembly makes no direct call to the forbidden compact
  symplectic, commuting-product, tableau-measurement, pivot-row, or old
  host-membership functions;
- every factorized transcript leaves those forbidden-call counters unchanged;
- the old `membership_bits` path is called zero times; and
- the separately executed oracle is used only for comparison.

The host still enumerates the domain, addresses component tables and complete
stage/checker caches, decodes finite roles, selects tuple entries, and drives
control flow. The component truth tables are separately retained physical
device semantics, but this runner does not place all of those devices in one
causal lattice geometry.

Thus this is finite factorized semantics. It is not a routed row-native
physical-membership theorem.

## Probability boundary

For supported reference transcripts, the compact supplied stabilizer
instrument assigns:

```text
reference branch weight 1/4        27,648
reference branch weight 1/2        10,368
reference branch weight 1             864
```

Those values are oracle metadata used to stratify the finite support census.
The runner supplies the stabilizer instrument and enumerates candidate
histories; it does not produce trial occurrences, a normalized physical
history measure, prepared-state identity, a corpus-frequency theorem, or an
empirical sampling law. This is not a probability or Born-rule derivation.

## Contextuality boundary

This certificate is context-wise. The occurrence of the same unsigned
observable in its row and column contexts is not yet one routed physical
ancestry, and no record-faithful instrument-equivalence theorem identifies the
two implementations.

Accordingly the result is a Peres–Mermin parity-support reference certificate,
not yet a physical contextuality certificate or a no-classical-memory theorem.

## Bare-metal and TOE meaning

The result matters because it fixes the exact finite behavior a later
bare-metal construction must reproduce:

- **O:** the full declared two-qubit stabilizer support/update/parity interface
  is internally consistent at component-table level;
- **T:** transcript order is enumerated, but no duration or local time rate is
  derived;
- **I:** signed Pauli rows are finite information carriers in this interface,
  not derived matter, particles, or chirality;
- **B:** lawful candidate histories are classified, but no outcome occurrence
  or frequency law is supplied; and
- **G:** cache sizes and future geometry keys are compiler bookkeeping, not a
  derived resource-stress or gravity law.

No axiom conclusion follows. In particular, this result neither selects the
candidate local law as fundamental nor supplies record formation, actuality,
probability, local time, matter content, continuum dynamics, gravity, or law
selection.

## No-Go Discipline Gate

Status: **PASS for narrow scope discipline; FAIL for any general no-go.**

### N1 — live extension routes

Five distinct routes remain live rather than ruled out:

1. route the readers, product, three membership comparisons, update lanes, and
   checker into one causal lattice apparatus;
2. replace cache-addressed membership with physical signed-row ancestry from
   source records through the final accept/reject record;
3. give repeated row/column observables one ancestry or prove a
   record-faithful instrument equivalence;
4. add an independently justified history measure, prepared-state link, and
   corpus theorem to test a Born/frequency claim; and
5. connect the finite construction to a selected fundamental law and then test
   whether any axiom consequence follows.

Because these are live, this note says only what the present runners do not
establish. It does not say that any route is impossible.

### N2 — wall independence

The five items above are future claim targets, not asserted independent
constitutional walls. No wall count is claimed.

### N3 — hidden-condition scan

The load-bearing conditions are explicit: the declared finite stabilizer
domain, imported component truth tables, host domain/cache addressing, and
separate algebraic oracle. No phrase such as “by construction” is used to hide
their provenance.

### N4 — residual matching

No prior no-go is cited as evidence that a stronger route cannot close.
[Cycle 167](SIGNED_ROW_EGRESS_AND_MEMBERSHIP_SEAM_CYCLE167_NOTE_2026-07-16.md)
is cited only for the exact predecessor interface and its still-live routed
composition target.

### N5 — rhetoric audit

The negative language is confined to this executable resolution: one finite,
factorized, cache-addressed two-qubit stabilizer census. It is not generalized
to all physical implementations, larger systems, arbitrary instruments, or
the lattice as a whole.

### N6 — partial-closure and axiom classification

The next routed construction is a compiler/geometry path under fixed axioms.
This note does not relabel an engineering seam as a need for new constitutional
physics.

### N7 — strongest hostile steelman

A hostile reviewer can correctly argue that the same retained components may
be physically routed, that one source row can feed both contexts, and that a
separate normalized record-history theorem may later attach frequencies.
That steelman defeats every broad negative reading and is why the present
claim remains only the positive finite census.

### N8 — cross-cycle echo

[Cycle 166](PHYSICAL_JOINT_STABILIZER_UPDATE_CYCLE166_NOTE_2026-07-16.md)
already converted separately tested update gadgets into one positive joint
apparatus for four representatives. [Cycle 167](SIGNED_ROW_EGRESS_AND_MEMBERSHIP_SEAM_CYCLE167_NOTE_2026-07-16.md)
then made signed information physically readable and named routed membership
as the next target. Those positive closures are evidence to keep the five
extension routes open, not to declare a no-go.

## Files and verification

- [primary exhaustive census](../../../../scripts/peres_mermin_factorized_reference_census_2026_07_16.py)
- [independent Cycle-168 verifier](../../../../scripts/peres_mermin_factorized_reference_census_cycle168_2026_07_16.py)

```text
python3 -m py_compile \
  scripts/peres_mermin_factorized_reference_census_2026_07_16.py \
  scripts/peres_mermin_factorized_reference_census_cycle168_2026_07_16.py

PYTHONPATH=scripts python3 \
  scripts/peres_mermin_factorized_reference_census_2026_07_16.py

PYTHONPATH=scripts python3 \
  scripts/peres_mermin_factorized_reference_census_cycle168_2026_07_16.py
```
