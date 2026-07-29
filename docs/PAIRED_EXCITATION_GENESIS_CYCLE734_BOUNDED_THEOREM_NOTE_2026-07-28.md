# Paired-excitation genesis — source-boundary-free preparation, and the adjacency wall, frozen — Cycle 734

Date: 2026-07-28

Authority: none

Audit: unset

Status: bounded conditional theorem (positive preparation result + frozen
controller obstruction)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle734_paired_excitation_genesis_2026_07_28.py`](../scripts/frontier_cycle734_paired_excitation_genesis_2026_07_28.py)
- [`frontier_cycle734_paired_excitation_independent_check_2026_07_28.py`](../scripts/frontier_cycle734_paired_excitation_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

The Cycle-719 N1 table lists the paired-excitation family as live and
unexcluded; W2 names retirement of the source boundary among its
components. This cycle executes the family at the smallest honest scope
and returns one positive theorem and one precisely frozen wall:

**Positive — preparation no longer needs a distinguished site.**

- a **3-gate pair-creation template** (three X gates; fixed unrolling
  from `(layout, position)`; AST audit finds zero distinguished-site
  constants, zero runtime branches) creates a positive-oriented adjacent
  token pair with `h = 0` and lawful charge rows, bit-exactly from
  all-blanks, at **every** ring position (11/11);
- **exact translation covariance**: `T_shift · W(position) · T_shift⁻¹ =
  W(position + shift mod 11)` — all 121 conjugation identities hold
  exactly; the template is position-free and the applied position is an
  external parameter, so `source_boundary_retired_for_preparation:
  true` (for preparation — the controller is a separate matter, below);
- **count-2 enforcement through the parameterized public API**: the
  Cycle-731 constructor `count_certified_controller_build(...,
  expected_count=2)` reused unchanged (11,206-gate controller word,
  frozen sha); all 11 lawful pairs accepted, count-0/1/3/4 witnesses
  refused; the `h = 0, B = 0` ring-11 sector recount is exact (2,048
  cases; 55 = C(11,2) count-2 passes; 1,024 even-parity charge passes;
  full-law passes exactly the 55; zero iff exceptions; frozen outcome
  sha); the count comparison factors from the charge law;
- deletion controls: all 33 single-gate deletions (3 gates × 11
  positions) detected and refused by the composed law.

**Frozen — the adjacency wall.**

Applying the Cycle-719 two-rail controller to the adjacent pair
violates its own lawful-domain invariant — "an occupied A station
requires own B/work and both neighboring A/B rails blank at the Q
boundary" — at **step 0, stations 0 and 1**, and at two sites on every
one of the 11 steps. The obstruction
`ownership_uniqueness_at_adjacent_Q_sites` is frozen with a minimal
reproducing census (2 tokens at sites {0,1}, B and work empty,
ring-11); the single-token control triggers zero violations, so the
wall is specific to adjacency, not to the machinery. Notably, the bare
controller word still transports the pair coherently outside its
lawful domain (the orbit trace advances `[0,1] → [1,2] → …` with clean
A-pair returns and blank B; output sha frozen) — the failure is a
domain violation, not a dynamical breakdown.

## Supplied / derived / open

### Supplied

- the all-blank Cycle-731 ring-11 register with clean auxiliaries; the
  external application-position parameter (not a distinguished site);
  the `expected_count = 2` comparison parameter; the finite oriented
  ring geometry; program content/order on the held two-bank fixture;
  passive ring-translation relabeling; the held data genesis and
  direction for the controller probe.

### Derived

- the position-free pair template, its bit-exact outputs at all
  positions, and the exact 121-identity covariance;
- count-2 acceptance/refusal through the unchanged parameterized
  certificate, with the exact sector recount;
- the deletion census; the frozen adjacency obstruction with its
  minimal witness, its every-step violation trace, its single-token
  control, and the frozen bare-transport observation.

### Open

- **the sharpest next test**: the frozen invariant is
  adjacency-specific by its own text (neighboring-rail blankness);
  separated pairs (distance ≥ 2) are untested here — a distance-2 pair
  template or a separation word would probe whether the wall is
  adjacency-only or extends to all multi-token states;
- W2's remaining components (finite oriented geometry, program
  content/order, passive-only covariance) are untouched and stated;
- everything the landed surfaces leave open at their scopes; no
  time/Record/Born/source content is touched.

## Negative-claim discipline

The frozen obstruction is a bounded worked result on the declared
fixture: it states that the *existing* controller's lawful domain
excludes adjacent pairs, with a reproducing witness — not that
multi-token control is impossible, and not a new no-go beyond its
census. N1's "live and unexcluded" status for the family is narrowed,
not closed: preparation is now positive; adjacent-pair control is the
named residual with an exact invariant to either generalize or respect.

## Verdict

W2's source-boundary component splits cleanly: **preparation** is
boundary-free (a translation-covariant 3-gate template, enforced by the
unchanged parameterized certificate), while **control** of the adjacent
pair hits the ownership invariant at the first step — frozen with the
precision the wall has lacked since Cycle 719 named the family. The
next test is written into the invariant itself: separate the pair.
Independent audit still required.
