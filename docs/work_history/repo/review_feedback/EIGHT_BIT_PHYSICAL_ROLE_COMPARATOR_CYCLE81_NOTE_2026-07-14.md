# Eight-Bit Physical Role Comparator — Cycle 81

**Date:** 2026-07-14  
**Authority:** none  
**Status:** exact bounded comparator; harness remains supplied  
**Constitutional effect:** none

Companion runner:

```text
scripts/eight_bit_physical_role_comparator_cycle81_2026_07_14.py
```

## Result

Cycle 80 changes the bounded source-preserving operational alphabet from 83
to 134 roles. Its 51 recurrent roles are disjoint from the prior inventory.
Seven bits provide only 128 words, so this selected recurrent route requires
eight bits.

The accounting distinction remains important:

```text
selected output roles                 113 -> 7 bits
selected exact input/output roles     120 -> 7 bits
source-preserving bounded roles       134 -> 8 bits
```

The eight-bit codebook preserves every Cycle-75 word beneath a leading zero.
The 51 recurrent roles occupy leading-one words. All 134 words are distinct
and 122 of 256 possible words remain reserved.

The physical comparator is the Cycle-75 two-rail cage extended by one bit.
The 38-record comparator harness is supplied. It contains only `H0/H1`
records. Its exact law still needs only three canonical rows: two
five-neighbour equality rows and one six-neighbour MATCH row. Proper-cubic
closure gives 56 raw rows.

The runner composes those rows with all 132 Cycle-58 binary rows and all 4,376
selected Cycle-60/67/72/80 raw rows. The 4,564-row provisional union is
single-valued. Across every ordered pair of the 256 possible words:

```text
ordered pairs                 65,536
reachable states             131,072
append edges                  65,536
terminals                     65,536
physical MATCH terminals         256
false MATCH                        0
parasites                          0
output conflicts                   0
maximum simultaneously enabled     1
```

The comparator never receives a role label. It compares two ordered physical
spines of eight `H0/H1` records. MATCH is an appended `H1` record at a fully
caged site, not a host-language Boolean returned by a symbolic decoder.

## Exact first-difference census

For unequal words, the certificate chain stops at the first differing bit.
The complete census is:

```text
bit 0   32768
bit 1   16384
bit 2    8192
bit 3    4096
bit 4    2048
bit 5    1024
bit 6     512
bit 7     256
equal     256
```

Thus each pair has one linear natural path and one terminal. The total state
count is exactly twice the pair count and the total edge count equals it.

The rejected one-rail design remains unsafe. Its first `H0/H1` mismatch in
one ordering is an existing Cycle-58 copy signature and appends parasitic
`H0`. At eight bits that collision affects exactly 32,640 ordered unequal
pairs. The second cage rail is load-bearing physical structure.

## Coordinate disposition

The fixed 22-record cage has trivial stabilizer under proper cubic rotations.
Every comparator rule is installed under all 24 rotations, and transformed
frontier controls agree exactly. The displayed bit order and axes are carried
by that finite asymmetric record frame; coordinate congruence is not a rule
input.

## What changed and what did not

Cycle 81 closes the bit-width update forced by the selected recurrent route.
It does not make the harness autonomous. The candidate word, reference word,
two cage rails, start record, and terminal cage are all supplied in the finite
probe.

The exact residuals are:

### `SEED_TO_EIGHT_BIT_COMPARATOR_HARNESS`

Grow and reserve the 38-record physical word/cage pattern from the official
seed or selected terminal, route an actual neighbour word into its candidate
spine, and route a law-program word into its reference spine. No global axis,
symbolic role register, or supplied macrocell placement may survive.

### `DIRECTIONAL_MULTIWORD_MATCH_TO_RULE_PORT`

Encode the six seed-frame neighbour directions, compare all occupied-role and
open-direction slots required by one selected row, reject extras, and expose
one physical rule port only after the whole exact signature matches.

### `RULE_PORT_TO_EIGHT_BIT_OUTPUT_WORD`

Use the selected physical port to copy the row's associated eight-bit output
program into fresh space, append completion last, and make the resulting word
available to the next comparator.

No axiom addition follows from the wider word, physical comparator, or any of
these finite compiler obligations.

## Verification

```text
python3 scripts/eight_bit_physical_role_comparator_cycle81_2026_07_14.py
```
