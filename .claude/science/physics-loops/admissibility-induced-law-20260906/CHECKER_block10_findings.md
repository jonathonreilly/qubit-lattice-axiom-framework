# Refuting pass — block 10 (supervisor-run, disjoint machinery; 2026-09-15)

`specs/supervisor_control_block10_refuter.py` (output in `.out.txt`); not an independent review.

| item | runner's route | refuting route | result |
|---|---|---|---|
| the plaquette's `{b, c}` term | Möbius inversion of `log μ` over the 16 subsets at the witness | the closed form of T3(b): `exp(−Δ_2 log K_2(b, c))` from `Z_2` values | `12/13`, equal |
| the star's leaf triple | Möbius inversion over the 8 subsets of the leaves | `exp(−Δ_3 log K_3)` from `Z_3` values | `165/169`, equal |
| the `k`-body verdicts `k = 2..6` | mixed-difference ratios with the vacuum at `+x` | the same with the vacuum at `−x` (different values, same zero/nonzero verdict) | nonzero for every `k` |

Attempts to refute (nothing refuted): T3(a)'s clique argument — the grouping of the four subsets differing at a non-adjacent pair `x, y` yields brackets that are log-ratios of the conditional at `x` evaluated at two configurations differing only at `y`, which the Markov property equates; T3(b)'s maximality — a non-maximal set's term also receives contributions from the sets containing it, so only maximal sets are certified; T4's bipartiteness — two neighbors of a site differ by a vector of even coordinate sum. Findings: F1 (fixed) the token "certified" in the note; F2 (fixed) classical names in four sections outside Prior art / Imports (runner F4). Verdict of this pass: PASS-NO-BLOCKER at the supervisor's own standard, pending the owner's independent review.
