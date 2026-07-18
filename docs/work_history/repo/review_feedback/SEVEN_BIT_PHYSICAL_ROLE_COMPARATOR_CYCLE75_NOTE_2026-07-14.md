# Seven-Bit Physical Role Comparator — Cycle 75

**Date:** 2026-07-14  
**Authority:** none  
**Status:** positive bounded local comparator; supplied-harness residual remains  
**Constitutional effect:** none

Companion runner:

```text
scripts/seven_bit_physical_role_comparator_cycle75_2026_07_14.py
```

## Result

The selected Cycle-60 + Cycle-67 + Cycle-72 compiler contains exactly **62
distinct output roles**. Output words alone therefore fit in six bits. That is
not the operational compiler bound: seven additional contents occur in exact
input signatures and must be distinguished to select the right row. The exact
input/output alphabet has **69 roles**, so six bits are impossible and seven
are sufficient. Including fourteen contents present in the concrete source
but inert in this bounded union gives **83 roles**, still requiring exactly
seven bits. An injective seven-bit codebook leaves 45 of 128 words reserved.

A supplied physical comparator then tests two seven-bit words. It contains no
69-way site and performs no symbolic decode. Candidate bits, reference bits,
cage bits, certificates, and MATCH are all records of the already selected
orthogonal `H0/H1` pair. The comparator never receives a role label. Across
all 16,384 ordered pairs of seven-bit words and every one of their 32,768
reachable states, it reaches MATCH exactly for the 128 equal pairs:

```text
new canonical comparator rows       3
new proper-cubic raw rows           56
all ordered word pairs          16,384
reachable pair states           32,768
append edges                    16,384
pair terminals                  16,384
MATCH terminals                    128
false MATCH                           0
parasites                             0
output conflicts                      0
maximum enabled writes                1
```

The new raw domain is disjoint from all 132 Cycle-58 binary raw rows and all
3,206 selected compiler raw rows. Their provisional union has 3,394
single-valued raw rows. Proper-cubic closure, an asymmetric seed-carried cage,
and direct transformed-frontier checks remove coordinate congruence from the
rule input.

This closes only the **one-word physical equality comparator**. The 34-record
comparator harness is supplied. It is not grown from the official seed, does
not yet conjoin one to six directional word comparisons into a selected union
row, and does not yet build the selected output word in fresh space.

## 1. Exact role census

The 147 canonical rows have arity census

```text
one neighbour     10
two neighbours    39
three neighbours  52
four neighbours   28
five neighbours   15
six neighbours     3
```

Their exact output inventory is:

```text
ALL AUXY AUXZ B0 B1 BTG BTP BTQ B_0_2 COMP6 C_Q D0 D1 DONE E F FP
H0 H1 I1 I2 J6 L1 L10 L11 L12 L2 L3 L4 L5 L6 L7 L8 L9 MARK OPEN_B
OPEN_C OY OZ P0 P1 P2 P3 PAIR R1 R2 S7 S8 START TJ TY TZ U W1 W2 W3
W4 W5 W6 X_B Z_A Z_C
```

There are 62. The exact signatures additionally consume seven input-only
contents:

```text
ARM A_0_2 B_1_2 COMPLETE JOIN RING Z0
```

Thus the active transition alphabet is 69. The concrete completed Cycle-67
source also contains fourteen source-only contents:

```text
AUX A_0_0 A_0_1 A_1_0 A_1_2 A_2_0 A_2_1 A_2_2 A_3_0 A_3_1 A_3_2
BACKSTOP JOINT LAUNCH_A
```

Thus a fully injective replacement of every content at this bounded source
boundary has 83 words. The exact information statement is therefore:

```text
output-only:        ceil(log2 62) = 6 bits
active row matcher: ceil(log2 69) = 7 bits
full source union:  ceil(log2 83) = 7 bits
```

The seven-bit lower bound is conditional only on preserving these distinct
extensional contents injectively. A later proved physical quotient could lower
the number of codewords, but no such quotient is assumed here.

## 2. Why the naive comparator fails

The first candidate placed each open equality certificate between its
candidate and reference bits, behind the preceding certificate, with one
fixed cage marker. That gives four recorded neighbours. It works in isolation
but not in the already selected binary law.

For a physical `H0/H1` mismatch in one ordering, the exact local signature is
already a Cycle-58 DATA rule that writes `H0`. It therefore makes a parasitic,
permanent write inside the certificate footprint instead of leaving the
mismatch terminal quiet. Exactly 8,128 of the 16,256 unequal ordered words
have that ordering at their first mismatch. No decoder wording can repair
this; the local physical contexts are identical.

The repair adds a second, oppositely valued cage rail. Each equality site now
sees exactly five neighbours:

```text
preceding H1 certificate
candidate H0 or H1
reference H0 or H1
fixed H0 cage record
fixed H1 cage record
```

The two equal cases have different H0/H1 populations from either mismatch
case and generate two proper-cubic equality rows. Those five-neighbour rows
are absent from both prior raw domains.

A five-neighbour terminal cage is still insufficient: its H0/H1 population
can alias the mismatch row under a proper rotation. MATCH is therefore the
third row and uses all six neighbours. It can form only after certificate 7,
and no mismatch signature can rotate into it because the arity differs.

## 3. Physical geometry

In the seed-carried presentation, seven candidate records and seven reference
records form parallel spines. Seven open certificate sites lie between them.
Two fixed cage spines lie on the remaining transverse sides. A supplied `H1`
start record precedes certificate 1. The five supplied records around the
terminal site plus certificate 7 fully surround MATCH.

The supplied record census is:

```text
candidate word            7
reference word            7
H0 cage spine             7
H1 cage spine             7
start record              1
terminal MATCH cage       5
total                    34
```

The fixed 20-record cage has trivial stabilizer under the 24 proper cubic
rotations. That makes its local frame intrinsic to the finite record pattern,
not a global coordinate class. The rule table contains every proper-cubic
image of its three canonical rows.

## 4. What the exhaustive result means

Let `k` be the first bit at which candidate and reference differ. Certificates
0 through `k-1` form in a unique chain. Certificate `k` sees a mismatch, so no
comparator row is available and the state is terminal. If no bit differs, all
seven certificates form and the six-neighbour MATCH row becomes available.

The exact first-difference census over all ordered words is:

```text
k=0   8192
k=1   4096
k=2   2048
k=3   1024
k=4    512
k=5    256
k=6    128
equal  128
```

The runner scans every open nearest neighbour in every reachable state using
the full provisional union, not merely the intended certificate target. No
other site is enabled. Each pair therefore has one linear append path and one
terminal. MATCH is a physical `H1` append at a caged site; equality is not
returned by a Python role oracle. The role-to-word dictionary is used only to
inventory and prepare test words.

This result does not prove robustness to an externally injected certificate
inside the reserved cage. It proves exact natural reachability under the
displayed homogeneous append rules. Composition with a seed-grown allocator
must show that no other rule can write inside that fresh footprint.

## 5. Exact residuals

### `SEED_TO_SEVEN_BIT_COMPARATOR_HARNESS`

The 34-record two-word/cage pattern is supplied. A retained compiler must grow
it append-only from the official seed or from the selected Cycle-72 terminal,
reserve the certificate and MATCH sites, route the actual neighbour word into
the candidate spine, and route a selected row's constant word into the
reference spine. It must do this without a preferred global axis or a
pre-existing symbolic role register.

### `DIRECTIONAL_MULTIWORD_MATCH_TO_RULE_PORT`

One comparator proves equality of one physical word. A selected exact union
row has one to six directional neighbours. The next compiler must certify the
seed-relative direction and openness of each required port, run the required
word comparisons, reject every extra occupied direction, conjoin all MATCH
tokens, and expose exactly one rule port. All 147 canonical rows and all their
proper-cubic images must remain single-valued under asynchronous overlap.

### `RULE_PORT_TO_SEVEN_BIT_OUTPUT_WORD`

After exactly one row port is selected, the law must write that row's
seven-bit output code into a fresh macroblock, issue completion last, and make
the new word available to later comparators. No extensional output label may
appear in this construction. The output builder must compose with the
seed-grown allocator and remain quiet outside its declared footprint.

These are finite exact-law/compiler obligations. No axiom addition follows
from the seven-bit bound, codebook, cage, equality chain, or remaining
construction work.

## 6. Scope

Cycle 75 establishes:

- the exact 62/69/83 census and the resulting seven-bit operational bound;
- a physical equality comparator over all 128 possible words;
- collision freedom against the current Cycle-58 and selected compiler rows;
- exact asynchronous natural reachability; and
- proper-cubic covariance without coordinate authority.

It does not establish seed-grown harness formation, a full 147-row binary
compiler, renewal, recurrence, occurrence/fairness, probability, rate, clock,
mass, gravity, or exact-law uniqueness.

## Verification

```text
python3 scripts/seven_bit_physical_role_comparator_cycle75_2026_07_14.py
```
