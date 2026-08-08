# The checkpoint law — syndrome completeness achieved, and the guard regress that stops everything after it — Cycle 781

Date: 2026-07-30

Authority: none

Audit: unset

Status: bounded worked result (LAW_PARTIAL; the regress confirmed
mechanically on every tested guard; the new-primitive requirement
stated exactly)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle781_checkpoint_refusal_law_2026_07_28.py`](../scripts/frontier_cycle781_checkpoint_refusal_law_2026_07_28.py)
- [`frontier_cycle781_checkpoint_independent_check_2026_07_28.py`](../scripts/frontier_cycle781_checkpoint_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

Cycle 777 specified the missing permanence law: see every dirty flip,
and undo what you refuse. This cycle built the best candidate the
framework's reversible primitives allow — and found, with its checker,
exactly why no such candidate can finish the job:

- **the construction works where the landed law was blind**: a
  checkpoint guard compiled purely from X/CNOT/TOF over the landed
  layout — CNOT fan-out checkpoint at lock engagement, XOR-difference
  syndrome, compiled conditional restore. **All 744 prefix-6 dirty
  flips are detected and rolled back byte-exactly** (the checker
  recounted every one): syndrome completeness for the class that
  defeated Cycles 770 and 777 is achieved;
- **and the battery still wins**: 14/26, 38/50, 38/81. The obstruction
  is not an implementation gap but a structure: **state-null attacks**
  — words that edit the guarded region and the checkpoint consistently
  — produce zero syndrome by construction, and an editable checkpoint
  cannot identify the correct restoration direction;
- **the checker confirmed the regress mechanically, both directions**:
  the majority-of-three variant improves to 69/81 and is defeated by a
  **four-X null mutator constructed from the guard's own fan-out
  structure**; the every-boundary refresh variant (38/81) falls to a
  two-X mutator. For every guard tested, the null-syndrome word is
  built from the guard's own wiring — the attack is not found by
  search but derived from the defense. **REGRESS_CONFIRMED** under
  arbitrary M2 words (the constructed mutators lie outside the
  declared 770/777 battery families — the scoping that made earlier
  partial numbers look better than the truth);
- **`law_requires_new_primitive: true`, stated exactly**: within the
  reversible sector, any tamper-evidence mechanism is itself tamperable
  state, and its wiring hands the attacker the null-syndrome word. The
  missing element is a state component outside the reach of the
  reversible attack alphabet — which is precisely what the Record
  axiom's primitive permanence IS;
- `permanence_witness_established: false`; non-interference with
  lawful dynamics verified; unguarded 5/26 and landed-guard 38/50
  reproduced as controls.

**What this contributes to the axioms conversation**: campaign 2 closed
W5 as never-a-gap on the plain reading — permanence is primitive
content. This cycle and its two predecessors (770, 777) now give that
reading a constructive mechanical demonstration from below: the
derived reversible surface, exhaustively censused (777) and then
extended with its best checkpoint constructions (781), cannot witness
permanence, and each attempted witness generates its own defeater. The
axiom is not redundant; it does work nothing beneath it can do. That is
support for axiom NECESSITY, not evidence of an axiom gap — and it is
scoped to the constructions tested, stated as a construction pattern,
not a closed universal theorem.

## Supplied / derived / open

### Supplied

- the composition point and attack families (770/777); everything the
  Cycle-693/719/745/769/770/777 packages declare.

### Derived

- the checkpoint guard and its full gate provenance; the 744/744
  detection-and-rollback fact; the battery results; the majority-3 and
  refresh variants; the per-guard mechanical null-mutator
  constructions; the regress confirmation; the exact new-primitive
  requirement.

### Open

- a closed universal regress theorem (every compiled guard, proven
  abstractly — the construction pattern is the evidence, the
  quantified theorem is not claimed); multi-origin charts; the
  permanence-witnessed census (now understood to rest on the axiom's
  primitive content at this scope).

## Negative-claim discipline

REGRESS_CONFIRMED is scoped to the guards constructed and tested (the
primary's, majority-3, refresh) under arbitrary M2 words, with the
defeaters exhibited mechanically; the universal statement over all
possible guards is explicitly not claimed. `law_requires_new_primitive`
names what is missing without asserting the framework must add it —
the Record axiom already contains it as primitive content.

## Verdict

The reversible sector was given every chance: the landed law (770),
the exhaustive inventory (777), and now its best checkpoint
constructions with majority voting and refresh — and each guard's own
blueprint yields the word that erases its memory of the crime. The
axiom that says records are permanent is doing exactly the work this
campaign proved nothing else can do. Independent audit still required.
