# Mixed-Transient Pair-Barrier Phase — Cycle 68

**Date:** 2026-07-14  
**Authority:** none  
**Status:** exact mixed-local causal closure; scratch candidate-law result  
**Constitutional effect:** none

## Question

Does the Cycle-62 `F/A/T` phase shell remain safe when composed with every
reachable asynchronous transient of the Cycle-60 comb, rather than only with
the completed Cycle-60 terminal?

## Legacy counterexample

No. One shortest representative is a reachable Cycle-60 rank-26 state with

```text
S8  at (0,-1,-4) present;
R2  at (1,-2,-4) present;
R2  at (1,-3,-3) absent;
S8  at (0,-3,-2) absent.
```

The old table can then append

```text
F at (0,-2,-4);
A at (0,-3,-4) from that one F;
T at (0,-3,-3) from that one A.
```

The last append permanently steals a site whose intended role is the delayed
second `F`. Proper-cubic symmetry gives six wrong-write classes. This does not
block the Cycle-60 comb and does not create a simultaneous output conflict; it
is a schedule-dependent role theft between the two tables.

Merely saying that a bridge `A` must wait for both adjacent `F` records is not
a physical repair. The one-`F` input needed at the twelve outer `A` sites is
canonically identical and still writes the bridge site. A pure relabel with no
locally different record context therefore hides site authority. The explicit
`AB`-only compilation has 34 canonical rows and 684 rotated inputs; its mixed
scan retains 96 causally feasible contexts in which `A` steals an intended
`AB` site.

## Physical pair-barrier repair

The surviving repair reuses all 51 Cycle-62 sites and changes their roles:

```text
F6 -> J3 -> K9 -> A12 -> T21.
```

- `J` occupies the three bridge sites and requires both adjacent `F` records.
- `K` occupies the exact nine-site `J`-only outer shell.
- Each outer `A` requires one adjacent `F` and one adjacent `K`.
- Each remaining `T` requires an adjacent `A`.

Thus no record carrying the later `A/T` phase exists next to a missing member
of an `F` pair. The repair costs no extra record and no extra site. Relative
to `F/A/T`, it costs two distinguishable record roles (`J` and `K`). Its exact
proper-cubic table has 32 canonical rows and 696 rotated inputs.

## Mixed-local exhaustion

The runner first reconstructs all 242,033 reachable Cycle-60 states. For each
candidate site it projects those states onto every locally relevant comb bit,
including the comb ancestors of nearby phase records. It then enumerates every
nearest-neighbour phase subset that can extend through the acyclic physical
requirements. This is stronger than sampling and avoids an irrelevant global
`2^103` product.

Results:

| table | mixed contexts | causally feasible | wrong/off-footprint | conflicts | comb blockers |
|---|---:|---:|---:|---:|---:|
| legacy `F/A/T` | 7,687 | 2,737 | 6 classes | 0 | 0 |
| repaired `F/J/K/A/T` | 8,911 | 2,353 | 0 | 0 | 0 |

An unrestricted completed-comb subset scan reports 27 apparent later-rank
matches in the repaired table. All are causally impossible: `K` cannot exist
while its `J` target is open, and `A` cannot exist while its required `K`
target is open. The mixed causal exhaustion removes all 27 without a ruling.

## Scope

This is candidate-law engineering, not an axiom or a probability law. It
repairs the phase shell through the Cycle-60 transient interface. It does not
yet validate the downstream `P/GUIDE/HEAD/C/X/Z` extension or the recurrent
`B/D/H` renewal interface; those rows require the same mixed-causal audit.
