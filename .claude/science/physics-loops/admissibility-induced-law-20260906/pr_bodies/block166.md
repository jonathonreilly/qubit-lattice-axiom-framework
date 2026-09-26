## Summary

This harvests probe #9231 (a Claude Opus 5.5 worker, the supervisor's own model family). An other-family referee confirmed it in #9326 (`grok-4.6`). The note works within block 110 as landed: the curvature member's exterior and the long-wave ray model, in the continuum exterior.

- **T1.** The turn at every order is `χ(b) = Σ_k m_k [uᵏ] n(u)ᵏ b^{−k}`, with `m_k = √π Γ((k+1)/2)/Γ(k/2 + 1)`.
  - The series has the radius of `log n` along the inverse of `1/(r n)`.
  - An independent direct expansion of the orbit integral agrees to order 5.
- **T2.** The member's coefficients are `Σ_j C(3k, k − j) C(k + j − 1, j) a^{k−j} p^j`.
  - They reproduce block 110's T4 and T5, and the comparator's series at equal charges.
  - New: at a fixed first-order turn, the third-order term is `(64/3)(42 + 54ρ + 27ρ² + 5ρ³)/(3 + ρ)³ (M/b)³`. It rises with the charge ratio, from `896/27` through `128/3` to `320/3`.
- **T3.** Block 110's capture threshold is the one positive root of the turning-point cubic's discriminant.
- **T4.** The member's series sums to the turn exactly for `b > b_c`, and diverges below and at `b_c`, at every charge ratio.
  - The supervisor gives a second proof through the nonnegative coefficients, and the divergence at `b_c` itself. Neither has an other-family check.
  - Exact coefficient ratios up to `k = 81` sit in the window of a square-root singularity at `1/b_c`.

Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_THE_MEMBERS_RAYS_TURN_BY_A_CLOSED_SERIES_AT_EVERY_ORDER_AND_THE_SERIES_REACHES_EXACTLY_DOWN_TO_THE_CAPTURE_THRESHOLD_AT_EVERY_CHARGE_RATIO_BOUNDED_THEOREM_NOTE_2026-09-26.md`
- Runner: `scripts/admissibility_rule_the_members_rays_turn_by_a_closed_series_at_every_order_2026_09_26.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block166.md`, `RESULTS_block166.md`, `CLAIM_STATUS_CERTIFICATE_block166.md` and `CHECKER_block166_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_members_rays_turn_by_a_closed_series_at_every_order_2026_09_26.py
```

- The runner gives `TOTAL: PASS=27 FAIL=0` in about 35 s.
- Mutation census 7/7: five in families A–E and two in F, each failing in its own family only.

## Review findings, imports, reachability

- **Imports.** Bouguer's invariant; the Lagrange–Bürmann inversion formula; Beta integrals; the Vivanti–Pringsheim theorem; the discriminant of a cubic; exact arithmetic.
- **Trace.** `frontier_discovery`.
- **Not ported.** The attempt's exact-box re-checks of block 110 T2, whose identities block 110's runner already executes.
- **Remaining.** Lattice corrections to the exterior; finite wave numbers.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
