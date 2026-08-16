---
claim_id: plus_seed_chiral_pair_fire_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the 6-NN star with six occupied neighbors and unread center, whether the July-3 k=3 pair fires at the center for the fully-mixed labeling and how many of the 64 {+,−} plus-labelings fire, is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/plus_seed_chiral_pair_fire_2026_08_15.py
---

# Plus-Seed Fire Of The July-3 `k=3` Chiral Pair (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the same six-axis star as the July-3 classification, with unread
center and six occupied axis neighbors; the July-3 unique `k=3` chiral pair
evaluated at tick 1 on that 6-tuple, and on the `2^6=64` `{+,−}` plus
labelings. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/plus_seed_chiral_pair_fire_2026_08_15.py`](../scripts/plus_seed_chiral_pair_fire_2026_08_15.py)

Framework context on `origin/main`: the axiom memo
[`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) and the
July-3 classification
[`docs/ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md`](ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md).
The Qubit axiom is not edited. A plus-seed is not written into Admissibility.
L1 is not attached.

## Result Up Front

Seed-grown ℓ¹ fronts never present six occupied nearest neighbors, so the
July-3 unique `k=3` pair cannot fire during ordinary growth. That growth
statement is not repeated as a theorem here. The residual is initial data
that is already a plus: six occupied axis neighbors around one unread
center, on the same 6-NN star.

On that star the pair is scored in two ways.

1. Label the six axis slots with the July-3 lex-first handed fully-mixed
   representative `(0, 1, 0, 2, 1, 2)` in direction order
   `(+x, −x, +y, −y, +z, −z)`. That 6-tuple is a member of the unique `k=3`
   chiral pair. Tick 1 at the unread center therefore fires:
   `N_new = 1`.
2. Restrict the six occupied neighbors to lock contents `{+, −}` (empty
   not allowed on the plus). Among the `64` such plus-labelings,
   `N_fire = 0`. None is a handed fully-mixed `k=3` coloring.

The pair *can* turn on as this fully-mixed seed labeling. It does *not*
turn on as an `M_2` `{+, −}` plus-seed. Both counts are displayed, not
adopted. No plus-seed is written into Admissibility. L1 is not attached.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact classification of the July-3 k=3 pair on one 6-NN plus star: the lex-first fully-mixed representative fires at the unread center, and none of the 64 {+,−} plus-labelings fire. Displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "does the July-3 k=3 pair fire at an unread center whose six axis neighbors are already a plus?"
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "leave the plus-seed counts displayed; do not adopt a plus-seed rule and do not attach L1"
conditional_surface_status: "exact on the declared 6-NN star, the July-3 k=3 pair, and the 64 plus-labelings; not a rule selection and not a growth-front restatement"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Support Boundary

- **Lattice / Admissibility / Record quotes** from
  [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), used only
  to name the cubic nearest-neighbor star, the one fixed nearest-neighbor
  rule, and unreadability of an absent record. No axiom sentence is edited.
- **Qubit** remains one-site `M_2(C)`. The two lock letters `{+, −}` are
  the spectral contents of one `M_2` record. The third neighbor letter is
  unread/empty. This note does not enlarge Qubit.
- **July-3 parent:** at `k=3` there is exactly one chiral pair, whose
  members are the handed fully-mixed patterns (every axis bi-colored, every
  value used twice). The runner re-earns the lex-first representative.
- **Geometry:** the same 6-NN star only. No new spatial patch is grown.
  Ordinary seed-grown front support is a closed parent residual, not this
  theorem.
- **External physics inputs:** none.

## Exact Objects

Write the six axis directions in the July-3 order

`D = ((1,0,0), (−1,0,0), (0,1,0), (0,−1,0), (0,0,1), (0,0,−1))`.

The plus star is the unread center `0` together with those six neighbors.
A neighbor condition is a letter in the `k=3` alphabet `{0, 1, 2}`. The
`M_2` plus-labelings identify `{1, 2}` with `{+, −}` and forbid letter `0`
on the six axis slots.

Proper cubic rotations act on colorings by the faithful direction
permutation of the 24 determinant-`+1` signed permutation matrices.
Inversion `P = −I` swaps opposite axis slots. A coloring lies in the unique
`k=3` chiral pair when it is not proper-equivalent to its `P`-image. The
pair fires at the unread center on a 6-tuple `c` exactly when `c` is in
that pair. Then `N_new = 1` if it fires and `N_new = 0` if it does not.

The July-3 lex-first representative of the pair is

`c★ = (0, 1, 0, 2, 1, 2)`.

Every axis is bi-colored and the letter counts are `2/2/2`.

## Theorem 1 — Fully-mixed representative fires

On the plus star, label the six occupied axis slots by `c★`. That 6-tuple
is a member of the unique `k=3` chiral pair. Tick 1 at the unread center
therefore fires the pair:

`N_new = 1`.

The representative uses all three `k=3` letters. Scoring `c★` is the
specified fully-mixed labeling, not a claim that letter `0` is a second
`M_2` lock content.

## Theorem 2 — None of the 64 `{+, −}` plus-labelings fire

Empty is not allowed on the plus. The 64 content assignments are the
colorings `{1, 2}^6`. Each uses only two letters, so none can be fully
mixed at `k=3` (three letters, each used twice). Direct orbit membership
confirms

`N_fire = 0`.

If `N_fire` had been positive, the pair could turn on as an `M_2` plus
seed rather than as a growth front. It is not positive.

## Theorem 3 — Displayed, not adopted

The two counts are displayed. They are not adopted as a rule. This note
does not write a plus-seed into Admissibility. It does not attach L1. It
does not change Qubit. It does not reopen ordinary growth: fronts never
presenting six occupied neighbors remains a parent residual.

`claim_scope`: On the 6-NN star with six occupied neighbors and unread
center, whether the July-3 `k=3` pair fires at the center for the
fully-mixed labeling and how many of the 64 `{+,−}` plus-labelings fire,
is reported. Displayed, not adopted.

## Honest Auditor / Boundary

- The parent growth statement is used only as motivation. The theorems
  score one already-plus 6-NN star.
- Membership in the July-3 pair is a predicate on a 6-tuple. It is not a
  dynamics, a formation rate, or a selected physical rule.
- `N_new = 1` for `c★` does not license three lock contents. `N_fire = 0`
  does not license a plus-seed axiom.
- Observed weak `P`-violation is not derived here and is not used as a
  fit target.
- No audit verdict is authored.

## Falsifiers And Mutation Targets

The predicate `N_new == 0` on `c★` must fail.
The predicate `N_fire == 64` must fail.
The predicate `N_fire == 0` must hold.

The runner re-earns `c★`, the unique pair, and both counts.

## Quoted Live Premises

From [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

A site with no record cannot be read.

A readout value is determined by record content alone.

The July-3 parent states that at `k = 3` there is exactly one chiral pair,
whose members are the handed fully-mixed patterns.
