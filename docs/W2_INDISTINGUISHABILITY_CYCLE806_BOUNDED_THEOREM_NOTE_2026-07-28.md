# Ordering was never the bottleneck — the W2 wall is a satisfiability ceiling — Cycle 806

Date: 2026-07-30

Authority: none

Audit: unset

Status: bounded worked result (the whole-function-class decision at the
Cycle-752 fixture scope; the per-start satisfiability census)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle806_w2_indistinguishability_2026_07_28.py`](../scripts/frontier_cycle806_w2_indistinguishability_2026_07_28.py)
- [`frontier_cycle806_w2_independent_check_2026_07_28.py`](../scripts/frontier_cycle806_w2_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

W2's wall stood as an ordering-search failure: no fixed order is
position-uniform (752: 0/2,046; best witness 1/11) and every landed
covariant functional order scores 0/11 (783). This cycle set out to
decide the ENTIRE function class at once — extract every contested
boundary's complete landed-local profile (15 components,
provenance-cited) and its forced order, then either exhibit a profile
collision (killing all functions of landed-local data) or construct
the order function. The decision procedure found something stronger
than either branch:

- **ten of the eleven starts are UNSATISFIABLE outright**: complete
  enumeration of all 2,048 order-assignments per start gives
  per-start success counts **(512, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)** —
  from starts 1-10, NO assignment of orders at the contested
  boundaries meets the landed success criterion. Ordering information
  of ANY kind — landed, omniscient, oracular — cannot succeed there;
- **the one satisfiable start is barely constrained**: 512 of 2,048
  assignments succeed; only 2 of its boundaries are forced (9
  flexible), and the two forced profile pairs do not collide
  (`NO_COLLISION`);
- **the omniscient lookup ceiling equals the landed witness**: the
  121-row profile-lookup scores exactly 1/11 — the same ceiling the
  752 witness and every 783 functional hit. The ceiling is the
  satisfiability structure, not a property of any candidate;
- **the checker confirmed everything with the landed criterion**:
  criterion fidelity exact against the copied 752 allocator (no
  strawman strictness); the 752 identity numbers reproduce (best
  fixed order 1/11; 0/2,046 position-uniform; the witness's start is
  the satisfiable one); independent exhaustive re-enumeration matches
  the primary start-by-start. Overall: **CONFIRMED**.

**What this does to W2**: the search for "the location-adaptive order
source" is CLOSED at the Cycle-752 fixture scope — not because the
source hides beyond landed quantities, but because none can exist:
the battery is unsatisfiable by any boundary-order policy from 10 of
11 starts. The 752/783 results are subsumed (every candidate's 0/11
or 1/11 is now explained by one structure). The lane's open question
inverts: what distinguishes the satisfiable start from the ten
unsatisfiable ones, and what — other than ordering — would the
fixtures need? That is data for the eventual W2 resolution, which
does not run through order sources at this scope.

## Supplied / derived / open

### Supplied

- the Cycle-752 fixture battery and success criterion (copied,
  sha-pinned, reimplemented — never imported); the 783 functional
  definitions as context; everything those packages declare.

### Derived

- the 15-component landed-local profile with provenance; the 121
  contested boundaries with the 2/9/110 forced/flexible/unresolved
  split; the complete per-start satisfiability census; the
  NO_COLLISION verdict on the forced pairs; the 1/11 lookup ceiling.

### Open

- what distinguishes the satisfiable start (a follow-on
  discriminator question); fixture families beyond the 752 battery
  (no claim); the W2 resolution itself, which at this scope is not an
  ordering problem.

## Negative-claim discipline

The unsatisfiability is scoped to the Cycle-752 fixture battery (11
starts) under its landed success criterion, verified by complete
enumeration (2,048 assignments per start); nothing is claimed about
other fixture families, other criteria, or non-ordering resolutions.

## Verdict

Asked to decide the whole function class, the decision procedure
dissolved the question: from ten of eleven starts there is nothing
for ANY function to find, and from the eleventh, almost anything
works. The wall W2 has been pushing against is not made of missing
information — it is the fixtures themselves. Independent audit still
required.
