# Physical Bit Router And Patricia Selector — Cycle 87

**Date:** 2026-07-14
**Authority:** none
**Status:** positive physical branch primitive plus exact selector reduction
**Constitutional effect:** none

Companion runner:

```text
scripts/physical_bit_router_patricia_selector_cycle87_2026_07_14.py
```

## Result up front

A strict-nearest-neighbour physical gate can route one active `H1` token left
or right according to one supplied physical `H0/H1` candidate bit. It uses no
symbolic Boolean or role label:

```text
token H1 + bit H0 -> gate H0 -> branch-0 H1
token H1 + bit H1 -> gate H1 -> branch-1 H1
```

The twelve-record gate source is supplied. Four canonical rows implement the
two gate writes and two branch writes. Proper-cubic closure gives 51 raw rows;
24 safely coincide with earlier `H1` rows. The complete Cycle-86 plus router
union has 4,651 single-valued raw rows.

Both input cases have exactly three states and two append edges. Only the
correct branch forms, the other branch remains open, and the terminal is
quiet. Every supplied gate cage has trivial stabilizer. All 144 transformed
stage controls—two inputs, three stages, and 24 proper rotations—have the
exact transformed frontier.

The 198 distinct 48-bit row programs also admit an exact shared-prefix
selector:

```text
explicit prefix-trie nodes       6,785
explicit prefix-trie edges       6,784
two-child branch nodes             197
one-child unary nodes             6,390
leaves                              198
compressed Patricia nodes           395
compressed Patricia edges           394
total compressed edge-label bits  6,784
longest compressed edge label        42
```

Every exact program reaches one unique leaf with its selected output
association intact. Across all 9,504 one-bit perturbations, each altered word
either rejects or lands exactly on the other valid row carrying that word.
Thirty directed one-bit changes connect two valid leaves.

This supplies a concrete serial/branching alternative to 198 full parallel
48-bit comparators at the logical-network level. It is not yet a physical
395-node selector: candidate-bit delivery and cubic embedding remain open.
No seed-grown selector is claimed.

## 1. Physical router geometry

The open gate site lies between an active token and the candidate bit. Two
fixed `H1` markers complete its exact four-neighbour signature. The gate writes
the same physical bit it reads.

Two open branch sites lie on the remaining transverse axis. Each has a
different four-record cage. After the gate forms:

- branch 0's five-neighbour signature exists only when the gate content is
  `H0`; and
- branch 1's five-neighbour signature exists only when the gate content is
  `H1`.

The selected branch writes `H1`. Because the cages differ, no proper rotation
aliases the two demanded outputs. The full provisional table was used when
scanning every open neighbour; the result is not an isolated four-row toy.

The router can be placed after a physical prefix token and before two possible
continuations. It therefore supplies the local branching atom a binary trie
needs.

## 2. Why a Patricia selector is the right serial target

The Cycle-86 bank has 198 exact programs of 48 bits each. Independent full
comparators would expose:

```text
198 x 48 = 9,504 programmed bit positions.
```

The ordinary prefix trie shares common initial segments and contains 6,784
non-root bit edges. Only 197 nodes genuinely branch; 6,390 have one child.
Compressing unary runs leaves 197 branch nodes, 198 leaves, and 394 labelled
edges. Compression changes the number of apparatus nodes, not the total 6,784
program-bit tests represented by those edges.

At run time only one root-to-leaf path should carry the active token. The
Cycle-87 gate performs a one-bit branch at a physical node. Unary Patricia
edge labels can in principle use Cycle-81-style equality chains, with a branch
gate only where the program set actually splits.

This avoids a 198-way equality fanout as the logical architecture. It does not
avoid moving the relevant candidate bit to whichever trie node is active.
That is now the load-bearing physical routing problem.

## 3. Exact remaining construction

### `CANDIDATE_BIT_BUS_TO_ACTIVE_TRIE_NODE`

At depth `i`, deliver candidate bit `i` to the one active physical prefix node
without supplying 198 labelled copies, activating an inactive node, or
allowing the permanent bus history to impersonate a later bit. The bit bus
may copy orthogonal `H0/H1` records, but every copy and reservation must be an
exact local append.

### `PROPER_CUBIC_PATRICIA_EMBEDDING`

Embed the 395 significant nodes and 394 labelled edges in the cubic lattice,
route edge-label equality chains, keep nonincident cages disjoint, and show
that every asynchronous schedule reaches exactly the correct leaf. The
displayed abstract trie does not itself prove this embedding.

### `TRIE_LEAF_TO_ASSOCIATED_OUTPUT_PORT`

Bind each of the 198 physical leaves to the eight-bit output program already
validated in Cycle 82, while ensuring rejected partial paths never expose a
writer port.

### `SEED_TO_TRIE_SELECTOR_HARNESS`

Grow the bit buses, node cages, edge programs, branch sites, output bindings,
and all reserved open footprints from the official seed or recurrent front.
Every Cycle-87 gate input and cage is supplied.

These are constructive compiler tasks. Cycle 87 does not assert that a cubic
Patricia selector is impossible, that physical fanout is forbidden, or that
the route is closed. It records a positive local router and the exact finite
network it would have to realize.

## 4. Scope

Cycle 87 does not replace Cycle 82's supplied six-slot input geometry, attach
the selector to actual neighbour macroblocks, establish multi-front
confluence, or select the exact physical law. It supplies no occurrence,
probability, clock, rate, mass, gravity, or resource-price theorem.

No foundation edit, queue edit, audit verdict, commit, push, or PR is made.
No axiom addition follows from the bit router, Patricia census, or remaining
physical embedding work.

## Verification

```text
python3 scripts/physical_bit_router_patricia_selector_cycle87_2026_07_14.py
```
