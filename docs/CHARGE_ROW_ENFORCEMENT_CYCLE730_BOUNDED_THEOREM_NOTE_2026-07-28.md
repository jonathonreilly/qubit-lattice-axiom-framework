# Charge-row projection and local refusal guard — Cycle 730

Date: 2026-07-28

Authority: none

Audit: unset

Status: bounded conditional theorem

Claim type: bounded_theorem

Runners:

- [`frontier_cycle730_charge_row_enforcement_2026_07_28.py`](../scripts/frontier_cycle730_charge_row_enforcement_2026_07_28.py)
- [`frontier_cycle730_enforcement_independent_check_2026_07_28.py`](../scripts/frontier_cycle730_enforcement_independent_check_2026_07_28.py)

Constitutional effect: none. This proposal changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

Cycle 730 establishes two separate bounded results.

First, let `n >= 1`, choose one marked station `s* = 0`, and define

`L_s = A_s XOR B_s XOR r_s XOR r_{s+1} XOR h*[s=s*]`.

For every supplied rail state `A,B` and supplied marked-edge sector bit `h`,

`(there exists r such that every L_s = 0) iff XOR_s(A_s XOR B_s) = h`.

When the parity condition holds, exactly two reference chains satisfy all
rows; they are global complements. For one fixed `r` and fixed `h`, only
`2^n` rail pairs pass, not the whole `2^(2n-1)` matching-parity sector.
On ring 11 the exhaustive recount covers 8,388,608 rail/`h` cases:
2,097,152 matching rail pairs per `h`, 4,194,304 satisfying
`(A,B,r)` extensions per `h`, and 2,048 passing rail pairs per `h` for
the fixed reference chain used by the parent fixture.

The proof is elementary GF(2) algebra. XORing all rows cancels each
reference bit twice and leaves `XOR_s(A_s XOR B_s) XOR h`, proving
necessity. After choosing either value of `r_0`, the row equations determine
the remaining chain recursively; ring closure is exactly the same parity
condition, proving sufficiency and the two-extension count. The independent
checker also exhausts rings `n = 1..5`, including the `n = 1` edge case.

Second, on the declared controller fixtures, every station with an active
macro computes its own charge row into a fresh scratch bit, includes that bit
as the seventh input to the existing recurrent OR syndrome, conditions that
station's macro on a clean syndrome, and uncomputes the OR and charge scratch.
This is a per-active-station guard. It is not a global parity acceptance
circuit.

## Computed fixture evidence

- The padded word has 99,310 semantic gates, versus 98,034 for the
  [Cycle 724 local refusal wrapper](LOCAL_TOKEN_ROW_ENFORCEMENT_CYCLE724_BOUNDED_THEOREM_NOTE_2026-07-28.md):
  1,276 added gates. Charge compute/uncompute is exact, and the word never
  writes the supplied reference chain or `h`.
- The declared lawful trajectories on the 11-, 35-, and 130-station fixtures
  have zero active-row charge failures. The extended wrap matches the parent
  data evolution and returns every supplied and scratch register.
- The 130-station fixture injects 183 single-input violations: 182 reference
  flips and one `h` flip. Prediction and simulation agree on 341 local refusal
  events with zero mismatches. All 183 literal fixture cases agree with the
  host simulation.
- A direct counterexample bounds the circuit claim:
  `(A,B,r,h) = (1,0,2,0)` has a parity mismatch, while active station 0 has a
  clean charge row and the only dirty charge row is inactive. The local macro
  therefore is not controlled by any global parity decision.
- The static row-system witness `(A,B,r,h) = (33,0,62,0)` has two tokens and
  all rows zero. It demonstrates only that this declared static radius-one
  row family does not distinguish token counts inside a matching-parity
  sector. No recurrent-orbit conclusion is drawn from it.
- The padded physical compilation has 1,435,386 physical primitives and
  18,051,374 routed nearest-neighbor gates in each direction, with maximum
  route distance 48. The 1,691 controller-register M2 total already includes
  the 130 charge-scratch registers and the single `h` register.
- The [Cycle 713 support runner](PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md)
  source hash matches the declared pin, and its inherited residual checks are
  re-evaluated. This is unaudited support-only evidence, not retained
  authority for a mass or contact claim.

## Supplies, conventions, and dependencies

The following remain explicit conditions:

- Boolean rails, an oriented finite ring, and the choice of marked station 0;
- a supplied static reference chain `r`, the supplied sector bit `h`, their
  genesis values, and clean B/work/syndrome/MCX/OR/charge scratch;
- one source controller token, clean data genesis, and the declared program;
- the unaudited controller and compiler chain described by the
  [Cycle 719 controller note](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md),
  the Cycle 724 wrapper linked above, and the
  [Cycle 728 marked-edge presentation note](BKSF_HOLONOMY_COMPRESSION_CYCLE728_BOUNDED_THEOREM_NOTE_2026-07-28.md).

Choosing station 0 is a presentation convention. Calling the solution with
`r_0 = 0` canonical merely selects one of the two complementary reference
chains. The bit `h` is a supplied marked-edge sector bit; this package does
not derive a physical interpretation, autonomous preparation, or unique
genesis for it.

## Open boundary

This package does not construct a global acceptance bit, aggregate dirty rows
at inactive stations, derive reference/`h` preparation, prove preservation of
the row condition through a recurrent orbit, or derive global one-token
existence and uniqueness.

The static witness bounds only this declared radius-one row family. Larger
finite-radius guards, hierarchical or multiscale rows, locally propagated
counters or accumulators, boundary or topological formulations, alternative
auxiliary presentations, and preparation/admission dynamics remain open.
Nothing here rules out any of those routes or requires a new axiom.

## Bounded conclusion

The exact positive content is the existential-reference GF(2) projection
theorem and the fixture-bounded reversible per-active-station guard,
violation census, and physical compilation. The marked edge, canonical
reference choice, and `h` name are conventions or supplied data. All cited
scientific dependencies remain unaudited. Independent audit is still
required.
