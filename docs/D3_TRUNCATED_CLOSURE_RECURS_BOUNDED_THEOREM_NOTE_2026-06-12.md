# The d=3 Truncated Flow Closes From Step 1: H_kd = 0 by the Parity Lemma Forces All Three Truncated Steps to Share the Landed Couplings Exactly (Theorem by Algebra), With the Measured Budget Table (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_d3_truncated_closure_recurs_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_d3_truncated_closure_recurs_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=42 FAIL=0`.

## Findings

On the framework's cubic lattice with the even-`d²` `{2,4}` truncation: the
kept-to-decimated block is zero **after the even-`d²` projection of the step-1
output** (the raw step-1 `H_kd` is nonzero, max `1` — the zero is what truncation
enforces by the parity lemma, in the original-coordinate convention, stated; gated
`10⁻¹⁴` per step, `L = 8/12`), which forces **exact invariance of the kept couplings
from the first truncated step onward** (`max difference = 0` across all three truncated
steps — stronger than the `d = 2` post-step-2 closure). The accumulated retained-block
resolvent budget is measured (frozen labeled ceiling; the `L = 8` vs `12` pattern
gated); identity truncation is the labeled tautological control.

## Scope

Finite-`L`, `E = 0`, free; the by-algebra closure + the measured budgets are the data;
no flow/fixed-point claims. No new axiom/primitive/measure/weight; `r` untouched. The
audit lane grades.
