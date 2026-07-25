# Record migration is invisible to readout, and its gate is strictly weaker than the formation gate — Cycle 704

Date: 2026-07-25

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. **It does not decide whether records
migrate, does not adopt either reading of permanence, proposes no axiom-text
edit, and supplies no formation rule.**

Runner: `scripts/physical_record_migration_gate_identity_cycle704_2026_07_25.py`
(4 PASS / 0 FAIL, exit 0; exact arithmetic, with a negative control on the
decisive rows).

## The open question this addresses

Two landed notes leave record migration explicitly open, in these words:

> "**Migrating-record semantics — OPEN.** Bare permanence does not separately
> state site immobility."
> — `RECORD_PERMANENCE_FORCES_FRESH_SITE_DOUBLE_REGISTRATION_AND_AGREEMENT_SURVIVAL_BOUNDED_THEOREM_NOTE_2026-07-11.md`

> "The current Record text says records are permanent but does not separately
> state site immobility or a formation-successor relation. **A migrating-record
> semantics remains an untested alternative.**"
> — `ADMISSIBILITY_RECORD_CONTINUATION_REFINEMENT_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-13.md`

This cycle tests it. It does not settle whether records migrate; it settles
**where a discriminator can and cannot come from**, and finds one structural
consequence that holds either way.

## M1 — no readout can decide it

A migration moves one record to a vacant site and preserves its content, so it
preserves the configuration's content multiset. By the landed singleton-weight
factorization, every Record scalar readout is a function of that multiset alone.
Therefore **every Record readout is invariant under every migration**.

The runner checks this on a three-record fixture against three weight
assignments, with the negative control that changing a *content* is detected.

So no readout argument can distinguish migrating from immobile records, in
either direction. Any discriminator must come from elsewhere — which, on the
current surface, means Admissibility.

## M2 — Admissibility does see it, and the two gates are not the same

A migrating record carries its already-locked content, so the destination must
make that content available. It is tempting to conclude that migrating into a
site with `k` occupied neighbours is gated by exactly the condition a newly
formed record faces at a site with `k` occupied neighbours.

**That is false, and the reason is geometric.** A mover *vacates its origin*. If
the origin is adjacent to the destination, the post-move destination sees one
fewer occupied neighbour than a newly formed record at the same site would.

On the exhibited fixture the runner computes:

| quantity | value |
|---|---|
| neighbours seen by a record **forming** at the destination | 2 |
| neighbours seen by a record **migrating** from an adjacent origin | 1 |
| neighbours seen by a record **migrating** from a distant origin | 2 |

so the gates differ by exactly one neighbour for adjacent moves and agree
otherwise.

**A first draft of this cycle claimed the two gates were the same predicate and
"verified" it by writing the same function body twice and scanning 2187 rules.**
That is a tautology; it is withdrawn, and the geometric statement above replaces
it.

## M3 — the consequence: migration is strictly more permissive

Under an exhibited covariant rule whose available set is never empty — both
contents available until two neighbours are occupied, then the central one only
— a record carrying the non-central content **can reach the destination by
migrating from an adjacent origin, but could not have formed there**.

So migration is strictly more permissive than formation for short moves, and:

> **A rule cannot bound record density by bounding formation alone.** If records
> may migrate, configurations are reachable that the formation gate does not
> admit.

That is a constraint on how the law can be specified, and it holds whichever way
the migration question is eventually settled. A framework that wants a density
bound must either forbid migration in the axiom text or impose the bound
separately.

## M4 — the two readings of permanence, reported and not chosen

The axiom says records are permanent. That leaves two readings of what a
migration must satisfy, and they differ on a concrete move.

Starting from a configuration admissible under both readings, move a distant
record to a site adjacent to an existing one:

- **Formation-time checking** — a formed record is never re-examined, which is
  the most direct reading of "permanent". Only the mover is checked, and the
  move is admissible.
- **Revalidation** — bystanders are re-examined. The record at the origin now
  has two occupied neighbours and loses the content it had already locked, so
  the move is rejected.

Both are reported. **Neither is adopted.** A prior review in this campaign
correctly objected to a cycle that presumed one reading without saying so; that
objection is honoured here by exhibiting the split rather than resolving it.

## What this does not do

- It does not decide whether records migrate. That remains open, exactly as the
  two landed notes leave it.
- It does not adopt a reading of permanence, and does not propose an axiom-text
  edit.
- It supplies no formation rule: no site selection, no possibility selection, no
  weight, no rate.
- It does not claim the exhibited rules are the framework's rule; they are
  witnesses.
- It changes no lane, row, or obligation status, and awards itself no N1–N8
  verdict.

## Scope for independent review

Every decisive row is exact arithmetic on explicit finite configurations, with
no sampling and no floating point. M1's invariance is checked against three
weight assignments with a content-change control. M2's counts are computed from
the neighbour relation directly, and include the non-adjacent case as the
contrast. M4's starting configuration is verified admissible under **both**
readings before the move, so the split is a property of the move and not of a
badly chosen start. The witnesses use a two-letter content alphabet and a
count-only rule; larger alphabets, pattern-sensitive rules, and moves of more
than one record at a time are outside scope.

## Dependency citations

The runner imports nothing from the repository. The load-bearing framework
authority is [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md). The open question
is quoted from
`RECORD_PERMANENCE_FORCES_FRESH_SITE_DOUBLE_REGISTRATION_AND_AGREEMENT_SURVIVAL_BOUNDED_THEOREM_NOTE_2026-07-11.md`
and
`ADMISSIBILITY_RECORD_CONTINUATION_REFINEMENT_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-13.md`,
which are navigation context for the question rather than load-bearing
dependencies. M1 uses the singleton-weight factorization established in
[Cycle 693](PHYSICAL_RECORD_READOUT_CARRIER_THREE_WAY_SPLIT_CYCLE693_NOTE_2026-07-25.md).
