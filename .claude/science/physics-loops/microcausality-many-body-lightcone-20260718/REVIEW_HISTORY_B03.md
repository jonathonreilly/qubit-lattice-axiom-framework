# Review history — block03 (all-time volume-uniform walk-expansion LR bound)

## Round 1 — combined adversarial lens (codex, read-only), 2026-07-18

Spec: `lens_b03_spec.md`. Output: `lens_b03_out.txt`. Verdict as issued:
NEEDS REVISION (reject as written; central walk-series bound
salvageable). Dispositions:

### Blockers (4)

1. **`d = 0` not excluded by hypotheses; theorem false there**
   (counterexample `X = Y`, `||[A,B]|| = 2` vs claimed `1/5`). ACCEPTED.
   Fixed: `X ∩ Y = ∅` (`d ≥ 1`) now explicit in Hypotheses, frontmatter
   claim_scope, and the G6 statement; runner gates the hypothesis
   sentence (G6e2) and the exact counterexample as an
   exclusion-necessity exhibit (G6e3).
2. **Norm-transport display false for `t < 0`** (R integrated on the
   wrong side; concrete counterexample given). ACCEPTED. Fixed: G2/G3
   restated as directed-time (`t ≥ 0`); negative times via the `H → −H`
   symmetry of the supplied class, gated (G2f) with the even-in-`t`
   instance norm (G3d). The final `|t|` theorem is unchanged.
3. **False-green runner on both defects** (G6e was a placeholder
   predicate; no negative-time gate). ACCEPTED. Fixed: G6e2/G6e3/G2f/G3d
   added; all mutation-tested.
4. **No-Go section format drift** (missing ATTEMPTED markers,
   per-citation N4, prior-wall N8, Status line). ACCEPTED. Rewritten to
   the strict format with `Status: PASS` recorded after repairs.

### Major (5)

1. **`20J` presented as exponential cone velocity; ratio argument
   insufficient** (`x = 100`, `d = 101` counterexample). ACCEPTED AND
   ADOPTED AS MATH: the lens's `μ`-reweighted tail bound
   `Σ_{k≥d} x^k/k! ≤ e^{−μd + xe^μ}` is now stated in G6 (credited as a
   review-lens contribution), gated (G6f identity + exponent
   comparison, G6g instance), with the `μ = 1` readout `v ≤ 20eJ`;
   `20J` renamed the walk-series activity scale; monotone-decrease and
   exponential decay kept as separate statements.
2. **Iteration cannot reuse G3 verbatim (self term).** ACCEPTED as
   exposition: G4 now displays the per-bond re-derivation with the self
   term dropped BEFORE the Jacobi step and the reduced generator
   `H̃_b(t)`; the supporting identity was already gated (G1d).
3. **Instance gates described as universal.** ACCEPTED: Verification
   section now distinguishes symbolic-identity gates from
   exact-instance gates; G5c strengthened to all six start bonds; G4c
   strengthened with the symbolic threshold form; frontmatter says
   "as marked".
4. **Referenced runner cache absent.** ACCEPTED as timing: the cache is
   produced by the SHA-pinned precompute flow at landing (as for the
   siblings); Verification now says "at landing time". Verified present
   in the landed commit.
5. **`G1`-`G7` heading labels alleged to violate naming rules.**
   DECLINED WITH REASONING: the labels follow the exact landed family
   pattern (block01 `L1/T1-T3`, block02 `W1-W5`) — bold inline labels
   whose parentheticals carry the scientific names; both siblings
   passed review in this format. No new vocabulary is introduced.
   Recorded here for the audit lane's attention rather than silently
   dropped.

### Minor (1)

1. **"Sharper function-level" ordering undefined.** ACCEPTED: now
   "broader time-domain function-level statement" with an explicit
   no-within-window-smallness disclaimer (also added to Non-Claims).

### Lens-confirmed survivals (for the record)

G1 signs/bookkeeping; G2 setup legitimacy (Hermiticity declared);
self-drop placement; all walk counts (6/10/60/100, `k` bonds =
`k−1` steps, `k ≥ d`, induced-region transfer, `n_X` counts `E(Λ)`);
series bookkeeping for `d ≥ 1`; tail arithmetic
(`3^200·200^800/800! ≈ 2.297×10^−41`, independently recomputed by the
lens); fairness of both sibling comparisons; sympy `is True` hygiene;
scope boundary.

### Post-repair state

Runner 38/0. Mutation battery: 18 probes, each flipping exactly the
targeted gate (two with expected same-mechanism collateral), every
mutated run completing with a single TOTAL line.
