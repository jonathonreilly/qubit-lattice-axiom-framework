# Cycle 197A — Cycle-190 / Cycle-193 Law-Union Compatibility Audit

Date: 2026-07-16

Status: authority-free bounded compatibility result; audit unset

Runner: `scripts/cycle190_cycle193_law_union_compatibility_audit_cycle197a_2026_07_16.py`

## Result

The literal union of the frozen Cycle-190 and Cycle-193 raw local-law tables
is **not globally single-valued**, but this is not a conflict created by either
cycle's new construction and it is not reached by any hard apparatus tested
here.

The exact table census is:

| Quantity | Count |
|---|---:|
| Cycle-190 raw rows | 102,338 |
| Cycle-193 raw rows | 101,768 |
| shared signatures | 93,614 |
| shared signatures with the same output | 92,582 |
| shared signatures with different outputs | 1,032 |
| distinct signatures in the union | 110,492 |

Every one of the 1,032 disagreements is already present between the frozen
Cycle-178 and Cycle-179 predecessor laws. Zero disagreements touch a
Cycle-190 `NEW_RAW` row, a Cycle-193 router row, or a Cycle-193 scan row. The
new matter interaction and physical dispatcher additions therefore coexist
at the row level; the remaining collision is inherited branch-law debt.

The disagreements are 43 complete proper-cubic orbits of 24 raw signatures.
They split into seven ordered output-pair families:

| Cycle-178/190 output | Cycle-179/193 output | Raw rows | Orbits |
|---|---|---:|---:|
| `R_A00` | `DONE` | 192 | 8 |
| `Z_C` | `BTQ` | 168 | 7 |
| `RING` | `B_0_2` | 168 | 7 |
| `R_A02` | `COMP6` | 144 | 6 |
| `Z_A` | `BTG` | 144 | 6 |
| `PAIR` | `A_0_1` | 120 | 5 |
| `Z0` | `A_0_2` | 96 | 4 |

Each orbit also has a distinct exact neighbor-role multiset. The runner
reproduces the named `I2 / MARK / MARK / COMPLETE / MARK` signature family,
for which the two outputs are respectively `Z_C` and `BTQ`.

## Reachability and hard-apparatus matrix

The runner does not decide applicability from a host-side context label.
For Cycle 190 and Cycle 196 it patches the candidate raw law and lets the
existing local-signature engine discover dependencies and replay both extreme
append schedules. For Cycle 193, the only context presented to the law is the
three physical H0/H1 records already present in the apparatus; the existing
physical dispatcher is run directly. Expected maps are validation oracles,
not inputs to the local-law lookup.

The frozen hard corpus is:

- all 32 Cycle-190 words;
- all four Cycle-196 XOR input pairs;
- all eight Cycle-193 contexts under minimum and maximum schedules, plus the
  R2 apparatus in all 24 proper-cubic rotations (40 runs).

No one of the 1,032 disagreement signatures is queried in any of those hard
schedules. This is the observed matrix:

| Law reading | Cycle 190 | Cycle 196 | Cycle 193 | Conflict rows queried |
|---|---:|---:|---:|---:|
| each source law | 32/32 | 4/4 | 40/40 | 0 |
| multivalued literal union | 32/32 | 4/4 | 40/40 | 0 |
| Cycle-190-priority union | 32/32 | 4/4 | 40/40 | 0 |
| Cycle-193-priority union | 32/32 | 4/4 | 40/40 | 0 |
| agreement-only union, with all 1,032 rows absent | 32/32 | 4/4 | 40/40 | 0 |

Thus all four union readings are extensionally identical on this tested
physical sector. Even the formally multivalued union acts single-valuedly on
every local signature actually queried by the corpus. Proper-cubic rotation
does not hide a partial collision: the disagreement set itself is a union of
complete proper-cubic orbits, and the rotated R2 corpus also queries none.

## What this establishes

Cycle 197A establishes a bounded **hard-sector compatibility theorem**:

> On the tested Cycle-190, Cycle-196, and Cycle-193 apparatus sector, the
> literal union, either predecessor priority, and deletion of every inherited
> disagreement produce exactly the same completed histories as the source
> laws.

This is stronger than table-size coexistence and weaker than a unified exact
law. The full literal union still assigns two different outputs to 1,032
signatures outside the tested sector. No claim is made that those signatures
are unreachable on the full lattice, unreachable under arbitrary boundaries,
or physically irrelevant. A globally predictive law still needs one lawful
domain that excludes them, a justified identification of the paired outputs,
or a recompilation that resolves them.

This result is also not quantum unification, a Born derivation, a scattering
theorem, a natural-law selection result, or a foundation result. No axiom
addition follows.

## No-Go Discipline Gate (N1–N8)

The negative atom being audited is deliberately narrow: **the unchanged
literal full-table union is not a globally single-valued local rule**. A
broader claim that the branches cannot be unified is not shipped.

### N1 — Alternative routes

1. **Cycle-190 priority — ATTEMPTED.** It makes the table single-valued and
   preserves all hard corpora, but replaces the Cycle-179/193 answer on all
   1,032 inherited collision rows rather than reconciling both source tables.
2. **Cycle-193 priority — ATTEMPTED.** It likewise preserves all hard corpora
   while replacing the Cycle-178/190 answer on the same rows.
3. **Delete every collision row — ATTEMPTED.** The agreement-only law preserves
   all hard corpora, proving that a lawful-domain restriction is a live repair;
   it is not the unchanged full-table union.
4. **Restrict the physical law domain to the tested reachable sector —
   ATTEMPTED.** The zero-query census closes this finite sector, but arbitrary
   boundaries and full-lattice reachability remain untested.
5. **Identify each paired output by physical equivalence — LIVE, NOT RULED
   OUT.** Seven role-pair families make this finite to test, but no operational
   equivalence proof exists here.
6. **Namespace or refine the predecessor signatures — LIVE, NOT RULED OUT.** A
   local discriminator could separate the two answers, at a priced row/role or
   geometry cost.
7. **Recompile both branches from their common predecessor — LIVE, NOT RULED
   OUT.** The fact that all conflicts predate Cycles 190 and 193 makes this the
   strongest direct next route.

The live routes defeat a branch-unification no-go. The shipped conclusion is
only the literal row-function fact plus the positive finite-sector theorem.

### N2 — Wall independence

| Pair | Does closing the first close the second? | Reverse? | Independent? |
|---|---|---|---|
| literal row conflict / hard-sector reachability | no | no | yes as mathematical statements |
| row resolution / proof that the lawful domain excludes every conflict | no | no | alternative physical closure routes, not conjunctive walls |
| hard-sector reachability / complete-domain reachability | no | yes only in the downward direction from a complete proof | no |

The collapsed physical residual is one item: make the candidate rule
single-valued on its complete lawful domain. Resolving the rows and proving
them unreachable are alternative ways to close that item. The literal table
census remains true even if a domain theorem makes the rows physically dead.
There is no separate Cycle190-new-row or Cycle193-new-row wall.

### N3 — Hidden-wall scan

- “Frozen” means the six runner/note SHA-256 values checked literally by the
  runner; it is provenance context, not retained authority.
- “Hard corpus” means exactly the 32 + 4 + 40 runs listed above; it does not
  mean arbitrary lattice states.
- The supplied scaffolds, program tapes, boundary context records, and
  expected output maps remain inherited construction conditions. None is
  silently treated as naturally generated.
- Schedule selection and expected maps validate the histories; they are not
  fed into local-law output lookup. The Cycle-193 run uses physical H0/H1
  context records and performs no host dictionary dispatch.
- “By construction,” “canonical,” “background,” “naturally,” and “obviously”
  are not used as load-bearing closure claims.

### N4 — Residual matching

| Witness | Witness residual | Cycle197A residual | Match? |
|---|---|---|---|
| Cycle-190 `FULL_RAW` | exact local rows used by five-lane egress/binding | left source of union and hard matter sector | yes |
| Cycle-193 `MERGED_RAW` | exact local rows used by physical dispatch | right source of union and hard dispatcher sector | yes |
| Cycle-196 interaction note | two-carrier XOR under Cycle-190 law | compatibility of that exact hard interaction under union readings | yes |
| Cycle-193 quantum scope caveat | missing coherent gate semantics | literal local-row collision | no; dropped |
| Cycle-190 inherited rotated-schedule caveat | full recurrent schedule aliases | literal local-row collision | no; disclosed but not cited as support |

### N5 — Resolution audit

- **Per raw row:** 1,032 signatures have two outputs.
- **Per proper-cubic orbit:** 43 complete orbits disagree.
- **Per added-row family:** zero disagreements involve the Cycle190 or
  Cycle193 additions.
- **Per tested apparatus:** zero disagreement rows are reached; all runs pass.
- **Full lattice / arbitrary boundary:** not tested.

Accordingly, “the union is incompatible” would be over-broad. The accurate
language is “the full literal table is non-single-valued, while the tested
hard sector is compatible.”

### N6 — Partial-closure paths

The agreement-only result exposes a non-foundational retirement path: specify
or derive a lawful domain on which the 1,032 rows never occur. Output-role
equivalence, signature refinement, or common-predecessor recompilation are
also law-definition or constructive routes. None is automatically a new
axiom. The registered scale-reference, kinetic-isotropy, and realized-state
primitives neither create nor resolve these local row outputs, and no extra
content is assigned to them here.

### N7 — Steelman

A hostile reviewer should reject any claim of genuine law incompatibility:
the runner itself proves that four materially different treatments of all
1,032 collision rows are observationally indistinguishable on every hard
apparatus tested. Since every collision is inherited and unused, the most
economical explanation may be that the compiled tables contain unreachable
compiler residue outside the intended lawful domain. A domain theorem or a
common-predecessor dead-row elimination could turn the agreement-only table
into one deterministic law without changing any demonstrated physics. This
steelman is convincing, so the broad no-go is explicitly not shipped.

### N8 — Cross-cycle echo

The immediate echo is the campaign's repeated distinction between raw-table
overlap and reachable-history conflict: predecessor rows can coexist in a
larger table without being exercised by the same apparatus sector, while later
endpoint and dispatcher constructions retire apparent interface walls. The
Cycle183-to-190 egress repair and Cycle191-to-193 physical dispatch repair both
show that an apparent framework obstruction can become a compiler/domain
problem. Cycle197A therefore queues domain proof or common-law recompilation,
not constitutional escalation.

Gate result: **PASS for the narrow literal-row statement and bounded positive
sector theorem; FAIL for any global branch-unification no-go.**

## Next decisive probe

For each of the 43 canonical disagreement orbits, ask whether any signature is
reachable from the union of the physically admitted Cycle-190/196 and
Cycle-193 boundary grammars—not merely the current hard fixtures. If none is
reachable, freeze an exact lawful-domain theorem and delete the dead rows. If
some is reachable, start with the seven output-role pairs: test operational
equivalence; if that fails, recompile the two predecessor branches with a
shared local discriminator. That is a law-engineering question, not an axiom
question.
