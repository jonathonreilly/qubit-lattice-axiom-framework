# The table-parameterized mapper — capacity becomes a parameter — Cycle 740

Date: 2026-07-29

Authority: none

Audit: unset

Status: bounded conditional theorem

Claim type: bounded_theorem

Runners:

- [`frontier_cycle740_table_parameterized_mapper_2026_07_28.py`](../scripts/frontier_cycle740_table_parameterized_mapper_2026_07_28.py)
- [`frontier_cycle740_mapper_independent_check_2026_07_28.py`](../scripts/frontier_cycle740_mapper_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status. Landed files are untouched; the mapper is a new module.

## Result up front

Cycle 739 froze the capacity edge: the landed mapper's finite placement
tables cap the bank domain at `b ≤ 12`, with eight rows failing by
IndexError at `b = 13`. This cycle converts that frozen limit into a
supplied integer:

- **the table law is derived from the tables themselves**: the frozen
  `BANK_BASES` and `LINK_BASES` values satisfy exactly
  `BANK_BASE(i) = 41 + 131·i` and `LINK_BASE(i, C) = 41 + 131·C +
  382·i` — the link offsets depend on the capacity `C`, which is why
  the frozen tables capped together. The law reproduces both landed
  tables byte-exactly on their full length (no fitted constants beyond
  the solved strides/offsets, which the independent checker re-solves
  from the table values without assuming them);
- **byte-exact equivalence on the landed domain**: for every
  `b = 1..12` at `C = 12`, the parameterized emission and mapping
  pipeline produces programs and mapped gate words byte-identical to
  the landed machinery (per-`b` shas frozen);
- **the extension is clean**: `b = 13..16` at `C = 16` emit without
  error — 99/107/115/123 rows, all 444 passing the per-row clean-work
  property — and the eight formerly-failing rows (stations 57–64) now
  map lawfully with full template verification;
- **orbits confirm at the first new ring**: a declared `b = 13`
  (`n = 99`) sample family (`k ≤ 2` configurations, five placements,
  495 invariant boundaries) runs invariant-checked lawful orbits with
  zero violations and exact register closure and inverse;
- **the theorem transfers table-uniformly**: the Cycle-738 structural
  lemmas, the Cycle-739 amended predicate, and the nine template
  properties are all `b`-independent given lawful mapping; with the
  parameterized mapper lawful at every `b ≤ C`, the sector theorem
  holds for all capacities and all `b ≤ C`, conditional only on the
  derived table law being the intended geometry — a supplied
  convention anchored byte-exactly to the landed tables on the landed
  domain.

## Supplied / derived / open

### Supplied

- the derived table-generating law as the intended geometry (a
  convention, anchored byte-exactly to the landed tables on
  `b ≤ 12`); the capacity parameter `C`;
- everything the Cycle-737/738/739 packages supply.

### Derived

- the law itself from the frozen table values (checker re-solved
  independently); the byte-exact equivalence sweep; the clean
  extension with the eight recovered rows; the `b = 13` orbit spot
  family; the table-uniform theorem transfer.

### Open

- exhaustive sector censuses beyond the four anchor rings are not
  attempted (the transfer is structural, not enumerative — stated
  plainly);
- true in-word renewal (recycling exhausted banks physically, rather
  than declaring larger capacity) — W4's renewal component remains
  the named open mechanism, now with a precise substrate to build on;
- adjacent-pair control; everything inherited at original scopes; no
  time/Record/Born/source content is touched.

## Negative-claim discipline

No negative claim ships. The Cycle-739 capacity census stands as the
boundary of the *landed* mapper; this package supersedes the limit by
construction without disturbing the landed module.

## Verdict

Capacity was a table, and the table was a law: two strides and an
offset, solved from the landed values, reproduce the machinery exactly
and extend it indefinitely. The sector theorem is now table-uniform —
every capacity, every admissible bank count — with the one supplied
convention named and anchored. What W4 still owns is physical renewal:
not more capacity, but reuse. Independent audit still required.
