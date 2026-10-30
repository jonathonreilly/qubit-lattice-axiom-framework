# Lane LFPRICE: the large-field price with boundary debit, which RD4's Route L now needs
**Why.** RD4.md (REVIEW in checks/rd4_review.md and REVIEW_RD4.md, HOLD) left Route L open. Route L is the Balaban-style small/large-field split, and three inputs are unproved:
- the matched reference;
- the boundary debit;
- the joint factorization (I5/I6).

RD4 (L9) also derives a summability condition: fixed component size n is summable only if n·a_eff·β₋ > 4 + c_B. Here a_eff is the final large-field price after all debits, L^{4r} is the volume factor, and c_B is the boundary cost. Small components are the binding case. This is the same tension F17 met: an instanton-strength-type condition.

RLARGE v3 is conditional, at SU(2) and bad-only scope (REVIEW_RLARGE_V3 S-1/S-2). In LARGE55, PRICE needs a boundary debit, and E13 retracts zero boundary cost (CODEX_REVIEW_LARGE F9).

**Probe all three mechanisms. Report which closes.**
- **(M1) Coupling-dependent threshold** (Balaban's device). Define large-field regions by |curvature| > p(g_k), with p(g) → ∞ slowly, for example p(g) = g^{-δ}. Then the price per large plaquette is about p(g_k)²/g_k² and grows with scale. Check that this makes n·a_eff·β₋ > 4 + c_B hold for all n ≥ 1, including n = 1, and what it costs the small-field expansion: the radius of analyticity, and fluctuation fields up to p(g).
- **(M2) Component-size resummation.** Absorb small components into the small-field polymer gas, with boundary-condition activities, so that only n ≥ n₀ components need the large-field price.
- **(M3) Boundary debit construction.** Build a consistent local action allocation that gives an explicit c_B: LARGE55 PRICE / I5, using the soft kernel's finite-cost response (SOFTHARD G2).

Do all of these, PROVEN where possible:
- give τ, c_ref, t_ref, b_∂ and the connected multiplicities for (L6) on the all-cut reference, or the exact remaining sub-lemma;
- check SU(N) for every N, not only SU(2);
- check the good/bad scope.

Rebuild everything from scratch. Credit Balaban and Dimock for the method, and do not let any citation carry weight in the proof.

**Deliverable: LFPRICE.md.** Read RD4.md, RD3.md, REVIEW_RD3.md, RLARGE.md v3 with REVIEW_RLARGE_V3, LARGE55.md with CODEX_REVIEW_LARGE, LCONV55 with its review, F17.md and SOFTHARD.md G2.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/lfprice_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only LFPRICE.md, LFPRICE_LOG.md and checks/lfprice_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB, with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.
