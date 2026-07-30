# Fixed-target X/CNOT preparation count — Cycle 753 bounded conditional theorem

Date: 2026-07-29

Authority: none

Audit: unset

Status: bounded conditional theorem

Claim type: bounded_theorem

Runners:

- [`frontier_cycle753_genesis_selection_attempt_2026_07_28.py`](../scripts/frontier_cycle753_genesis_selection_attempt_2026_07_28.py)
- [`frontier_cycle753_selection_independent_check_2026_07_28.py`](../scripts/frontier_cycle753_selection_independent_check_2026_07_28.py)

Fixture:

- [`fixed_target_x_cnot_cycle753_fixture_2026_07_28.json`](../outputs/fixed_target_x_cnot_cycle753_fixture_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status. Independent audit remains required.

## Result

For one supplied 5,979-bit target of Hamming weight 27, starting from the
all-zero bit string and charging unit cost for every logical `X` or ordered
logical `CNOT`, the following finite statements hold:

1. every exact preparation word has length at least 27;
2. exactly `(27!)^2` words have length 27; and
3. quotienting those minimum words by adjacent swaps of semantically commuting
   gates gives exactly `28^26` classes.

The supplied 27-gate word is one member of this minimum family. These are
conditional logical-combinatorics statements, not a physical compilation,
selection law, uniqueness theorem, or axiom consequence.

## Supplied theorem data

The fixture supplies:

- the register width, all-zero initial state, and one exact target support;
- the full-placement logical alphabet `X(i)` and
  `CNOT(control, target)` with distinct ordered wires;
- one unit of cost per gate;
- exact final-state equality as the landing rule;
- adjacent semantic commutation as the equivalence relation; and
- one landed minimum word.

The target and word were copied from the current reviewed
[fixed logical genesis fixture](GENESIS_WORD_SELF_VERIFICATION_CYCLE732_BOUNDED_THEOREM_NOTE_2026-07-28.md).
That source is proposal-only bounded support: this note uses it as provenance,
not as retained authority. Its current transitive support includes the
[token-count certificate](TOKEN_COUNT_CERTIFICATE_CYCLE731_BOUNDED_THEOREM_NOTE_2026-07-28.md),
[charge-row enforcement fixture](CHARGE_ROW_ENFORCEMENT_CYCLE730_BOUNDED_THEOREM_NOTE_2026-07-28.md),
and [recurrent matter-history controller](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md).
None is promoted here.

## Analytic proof

An `X` changes Hamming weight by one. A `CNOT` changes it by at most one.
Reaching weight 27 from weight zero therefore requires at least 27 gates.

Equality forces every gate to raise the weight by one. At a stage with `k`
prepared target wires, setting any wire outside the supplied support would make
exact landing impossible without a later weight decrease. The next gate
therefore has:

- `27-k` choices for its new target; and
- `k+1` choices for its parent: the super-root (an `X`) or one of the `k`
  prepared controls (a `CNOT`).

Multiplying from `k=0` through `26` gives

`product (27-k)(k+1) = (27!)^2`.

Add a fixed super-root labeled `0`. Each `X(v)` is edge `0-v`; each
`CNOT(u,v)` is edge `u-v`. Every minimum word yields a tree on the fixed
super-root plus 27 fixed physical-wire labels, and every such tree yields the
corresponding preparation partial order. The noncommuting pairs are exactly
the parent-child precedence pairs. Adjacent swaps of incomparable events
connect all linear extensions, so one commutation class is one labeled tree.
Cayley/Prüfer counting gives `28^(28-2) = 28^26`.

The independent checker verifies the gate semantics and commutation relation,
exhausts the complete word spaces through width four, exhausts a small Prüfer
tree family, reconstructs the exact arithmetic, and requires a clean primary
subprocess with an identical report. The small enumerations are implementation
tests; the global result is the analytic proof above, not an exhaustive search
through the 5,979-bit word space.

## Scope boundary

This theorem does **not** claim:

- that translated targets are lawful for the nonuniform parent fixture;
- physical, nearest-neighbor, or fault-tolerant gate minimality;
- minimality under any alphabet or cost other than the supplied one;
- autonomous target, alphabet, equivalence, or word selection;
- uniqueness of the minimum word or class;
- that the axioms force any supplied datum; or
- a route-independent negative result.

The Prüfer code and integer rank of the landed class use a supplied coordinate
convention recorded separately in
`GENESIS_TREE_PRUFER_RANK_CYCLE753_META_NOTE_2026-07-28.md`. That coordinate
has no theorem or physical authority.
