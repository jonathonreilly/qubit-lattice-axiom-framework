# The identities discharged — the sector theorem is unconditional to the machinery's capacity — Cycle 739

Date: 2026-07-29

Authority: none

Audit: unset

Status: bounded conditional theorem (unconditional over the admissible
capacity domain; two frozen corrections)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle739_identity_discharge_2026_07_28.py`](../scripts/frontier_cycle739_identity_discharge_2026_07_28.py)
- [`frontier_cycle739_discharge_independent_check_2026_07_28.py`](../scripts/frontier_cycle739_discharge_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

Cycle 738 left the general-n sector theorem conditional on two named
identities. The discharge attempt found both identities were **wrong as
stated** — in instructive ways — and both corrections are frozen here
as first-class results:

- **the I1 formula was too simple.** The implemented ownership
  predicate (both call sites in the lineage, byte-identical) is the
  **six-term** formula
  `not(a[left] or a[right] or b[left] or b[station] or b[right] or
  work[station])` — the Cycle-738 statement omitted the neighboring-B
  terms. The v1 four-vs-six mismatch is frozen verbatim. The amended
  formula is still a radius-one window; the L4 transport re-verifies:
  A- and B-windows transport identically under the `+1` shift, and
  along lawful separated orbits the B rail stays blank, so the extra
  terms vanish on the theorem's domain (both facts verified — symbolic
  transport plus a 44-placement direct orbit family);
- **the I2 "all b" claim hits a real capacity edge.** The finalizer is
  exonerated (its bank-count argument is never loaded — the same
  11-gate word for every `b`), and all 9 emitted-row templates pass
  clean-work inspection; but the mapper's placement tables are finite
  — `BANK_BASES` length 12, `LINK_BASES` length 11 — so at `b = 13`
  eight rows fail with IndexError (bank[12] ×1, cross[11] ×1,
  handoff[11] ×2, relay[11] ×4; census frozen verbatim). The
  admissible bank domain of the landed machinery is exactly
  **`b ≤ 12` (rings up to n = 91)**;
- **within capacity, nothing is left conditional**: template
  uniformity (9/9), finite-table inspection, and **exhaustive direct
  evaluation of every emitted row at every `b = 1..12`** — row totals
  3/11/19/27/35/43/51/59/67/75/83/91, 564 rows, zero failures.

Theorem status:
**`unconditional_for_admissible_b_le_12_with_amended_predicate`** —
the Cycle-738 contract, with the amended six-term predicate, holds for
every admissible bank count the landed machinery can express, with no
remaining identity conditions. Beyond `b = 12` the placement tables
end: extending is a new construction (larger tables), not a conjecture
and not a wall.

## Supplied / derived / open

### Supplied

- the amended predicate as the definition under test (uniformly
  applied; K itself still defines no ownership predicate — unchanged
  scope fact);
- everything the Cycle-737/738 packages supply per family member.

### Derived

- the six-term formula census (2/2 call sites exact); the amended
  transport lemma; the finalizer exoneration; the capacity
  characterization with the frozen b=13 boundary census; the 564-row
  exhaustive clean-work evaluation; the unconditional capacity-domain
  theorem.

### Open

- `b > 12`: enlarging the landed placement tables (construction, not
  proof); a table-parameterized mapper would make the theorem
  table-uniform;
- W4 renewal; adjacent-pair control; everything inherited at original
  scopes; no time/Record/Born/source content is touched.

## Negative-claim discipline

The two v1 findings ship as frozen corrections, not no-gos: the
four-term formula was the campaign's own statement error (now fixed at
its source of truth), and the b=13 boundary is a finite-table property
of the landed module with an exact witness, narrower than any
impossibility claim.

## Verdict

The theorem arc closes at the machinery's true edge: five structural
lemmas, four exhausted anchor rings, an amended predicate verified at
every use site, and every emitted row of every admissible program
checked — unconditional to `b = 12`, with the boundary an IndexError
census rather than an assumption. The two Cycle-738 conditions did not
survive contact with the code, and what replaced them is stronger.
Independent audit still required.
