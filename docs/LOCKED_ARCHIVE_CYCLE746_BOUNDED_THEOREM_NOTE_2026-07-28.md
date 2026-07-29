# The locked archive — renewed history becomes immutable by refusal — Cycle 746

Date: 2026-07-29

Authority: none

Audit: unset

Status: bounded conditional theorem

Claim type: bounded_theorem

Runners:

- [`frontier_cycle746_locked_archive_2026_07_28.py`](../scripts/frontier_cycle746_locked_archive_2026_07_28.py)
- [`frontier_cycle746_locked_archive_independent_check_2026_07_28.py`](../scripts/frontier_cycle746_locked_archive_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

Three landed pieces compose: the Cycle-741 renewal archive, the
Cycle-745 one-cell enforced lock, and the Cycle-742 readout feed. The
result is the **locked archive** — the W4/W5 junction's mechanism
candidate, end to end:

- **the tiling**: the 745 lock cell tiled over all 909 archive payload
  sites (7 rails per tile; 6,363 M2 sites); the per-cell same-word
  lock property is preserved under tiling — each archived payload bit
  is written-and-locked in one word (2,424 tiled write gates per
  generation);
- **immutability by refusal, exhaustively**: 1,818/1,818 direct
  overwrite attempts and 2,727/2,727 renewal-word attempts against
  locked cells complete as clean REFUSED transitions with locked bytes
  byte-invariant;
- **the archive-level induction**: base (909 post-write cells satisfy
  the lock invariant) and step (all 6,363 transitions across the seven
  archive words preserve it) — machine-checked, so every finite
  in-alphabet word sequence over the archive preserves locked content;
- **renewal still works**: at every generation all 303 fresh-cell
  first-writes are accepted — the lock never blocks lawful archiving,
  only re-writing;
- **readout unchanged**: the Cycle-742 feed reads the locked archive
  byte-exactly at all three generations.

## The honest ceiling

Mechanism-level archive immutability under the declared alphabet.
`record_permanence_claimed` remains **false** at the axiom level: the
W5 residual is the axiom-level permanence semantics beyond the declared
alphabet — what the Record axiom itself grants or must grant, which no
mechanism theorem can settle from below. That question is now exactly
one sentence wide, which is what this campaign exists to produce.

## Supplied / derived / open

### Supplied

- the tiling convention (declared); everything the Cycle-741/742/745
  packages declare at their scopes.

### Derived

- the tiled same-word locking; the exhaustive refusal censuses; the
  archive-level induction; the fresh-write non-blocking property; the
  byte-exact locked readout across generations.

### Open

- the W5 residual (axiom-level permanence semantics beyond the
  alphabet — the one-sentence question for the owner's axiom
  conversation);
- out-of-alphabet operations; larger archives; everything inherited at
  original scopes.

## Negative-claim discipline

No negative claim ships. The alphabet bound and the axiom-level
residual are scope statements.

## Verdict

The chain the two campaigns built now runs end to end with permanence
as enforcement: matter history → renewal → locked archive → Record
readout, every arrow a literal physical word, every immutability
property a refusal law with an induction behind it. What remains of W5
is no longer a mechanism question — it is the axiom-level sentence,
and producing that sentence precisely was the point. Independent audit
still required.
