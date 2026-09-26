## Summary

This answers programme T of the 2026-09-26 afternoon panel, at leading order in the spacing. It works within blocks 62, 64 and 65, all landed. The question: the member supplies lengths only, so the walker sees the lengths' own symmetric frame, and it has no connection. Is that coupling consistent with the member's relabellings at second order in the fields?

- **T1.** The comparator's two-component operator on half-densities is the framed walk plus `(1/8) ε·C`, where `ε·C` is the frame's inversion-odd curl. This is checked through second order for general and symmetric frames. For the lengths' frame, `ε·C` vanishes at first order and equals `2ε_abc η_ad ∂_b η_cd` at second.
- **T2.** Relabel, and turn the coin so the frame stays the lengths' own. The framed walk keeps the relabelling at first order. At order strain times relabelling it misses by the coin scalar `t = −(1/8)ε_abc(η_ad ∂_b S_cd + S_ad ∂_b η_cd)`, which is nonzero: a stretched rod twisted about its axis gives `−λτ/4`. Adding `(1/8)ε·C` removes it.
- **T3.** Among local potentials with at most one derivative (linear or quadratic, scalar or coin vector, 612 coefficients), exactly one restores the relabelling: `(1/8)ε·C`, the comparator's term. No local law for turning the coin, and no phase, substitutes.

So consistency forces one connection-like term. It is built from the lengths, so no coin-rotation field is needed at this order, and it is the comparator's. With block 157, the member's next order and the walker's second-order coupling are both the comparator's at leading order. Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_THE_WALKER_ON_THE_MEMBERS_LENGTHS_KEEPS_RELABELLINGS_AT_FIRST_ORDER_AND_AT_THE_NEXT_NEEDS_EXACTLY_ONE_TERM_THE_COMPARATORS_INVERSION_ODD_CURL_BOUNDED_THEOREM_NOTE_2026-09-26.md`
- Runner: `scripts/admissibility_rule_the_walker_on_the_members_lengths_needs_the_comparators_inversion_odd_curl_at_second_order_2026_09_26.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block158.md`, `RESULTS_block158.md`, `CLAIM_STATUS_CERTIFICATE_block158.md` and `CHECKER_block158_findings.md`, plus appends to `HANDOFF.md`, `TRACE_GATE.md`, `REVIEW_HISTORY.md`, `STATE.yaml`, `OPPORTUNITY_QUEUE.md` and `APPROACH_REGISTRY.md`

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_walker_on_the_members_lengths_needs_the_comparators_inversion_odd_curl_at_second_order_2026_09_26.py
```

- The runner gives `TOTAL: PASS=16 FAIL=0` in about 25 s.
- Mutation census 6/6: four mutations in families A–D, and two in F, each failing in its own family only.

## Review findings, imports, reachability

- **For a referee.**
  - Bilinear identities are proved by polarization on every pair of basis jets, 1800 pairs.
  - The coin turn that keeps the frame symmetric is `Θ = ½(J − Jᵀ) + ¼[η, S]`.
  - The uniqueness system has 7320 equations in 612 unknowns, with rank 612.
- **Imports.**
  - Exact linear algebra.
  - Derivatives along vector fields on half-densities.
  - The comparator's two-component operator with its connection, as a comparator (T1 reproduces its standard identity).
- **Trace.** `frontier_discovery`, answering the panel's programme T.
- **Remaining.**
  - Relabellings in time (lapse and shift).
  - The lattice placement of the term for the eight species.
  - Third order.
  - An other-family referee.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
