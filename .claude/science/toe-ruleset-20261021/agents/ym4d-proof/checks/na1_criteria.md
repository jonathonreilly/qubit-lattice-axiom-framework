# checks/na1_criteria.md — PRE-REGISTERED criteria for check na1 (background-vertex exponent bookkeeping)

Written 2026-10-28, BEFORE `na1_exp.py` exists. Exact integer/rational arithmetic in plain python only
(sympy-free, numpy-free, no BLAS): no numeric lock needed (brief rule 6). No constant appearing below is
derived in this session; every imported number is cited to a file written in an earlier session.

## What is being checked

The scaling exponent, in powers of L, of each family of terms in `D³𝔉_k(Z; V)[ζ^c·, ζ^c·, ζ^c·]` when `Z`
is a **nontrivial** critical chain, computed from the SAME five primitive ingredients NORMS §N6 uses, with
three weight parameters `(θ_w^c, θ_w^r, θ_A)` carried symbolically as NORMS §N7 carries them.

**Primitive ingredient table (all five imported, none derived here).** For a level-k link `x`, level `j`,
`n := k − j`:
| id | ingredient | value (exponent of L) | source |
|---|---|---|---|
| P1 | ℓ¹ mass of the **differentiated** level-0 response to a level-k delta | `(d − θ_w^c)k` | NORMS.md l.563 (at θ_w^c = 2: `(d−2)k`) |
| P2 | ℓ¹ mass of the level-j **residual** response to a level-k delta | `n + θ_w^r` | NORMS.md l.564 (at θ_w^r = d−1) |
| P3 | ℓ¹ mass of the level-j **undifferentiated** (potential) response to a level-k delta | `(d − θ_A)n` | NORMS.md l.565 (at θ_A = 1: `(d−1)n`) |
| P4 | sup of the level-j **curvature** response per unit level-k potential | `−θ_w^c n` | NORMS.md l.566 |
| P5 | sup of the level-j **potential** response per unit level-k potential | `−θ_A n` | NORMS.md l.567 |
Plus, for the background only:
| P6 | own-units level-j **background curvature** of the critical chain | `−θ_w^c n` | BFT-1 curvature clause (REVIEW_S22 l.410-411); PROVEN siblings: NORMS Lemma N1-4 (l.267-272) for the linear chain, BFT_B Theorem N2 l.3228 (`f_j ≤ 2Λ_2 f_k`, own units `ρ_j² f_j`) for the R^ax chain |
| P7 | own-units level-j **background soft fluctuation** of the critical chain | `−θ_w^r (n−1)` | J-str (c) as quoted at NORMS.md l.118-120; BFT_B (C_g-θ) l.2876-2879 at θ = 1 |

**The six families.** By the Taylor expansion of a local term `W(Y(A))` about a nontrivial value `Y(0) = X`
there are exactly three families per term type (Wilson at level 0; soft at level j), indexed by how many of
the three legs enter **differentiated** (through the covariant coboundary, resp. the residual):
`D³[W∘Y](0) = W'''(X)[Y',Y',Y'] + 3·W''(X)[Y'',Y'] + W'(X)[Y''']`, with `Y' ` linear (one derivative),
`Y''` quadratic and `Y'''` cubic in the legs (no derivative). So: **3-derivative, 1-derivative,
0-derivative**, with coefficients `W'''(X) = O(|X|)`, `W''(X) = 1 + O(|X|²)`, `W'(X) = O(|X|)`.

## Pre-registered PASS/FAIL verdicts

- **na1-A (CONTROL on the ingredient table).** The **1-derivative** families, computed from P1-P5 by the
  script, must reproduce NORMS §N7's table (NORMS.md l.650-651) **exactly and symbolically**:
  Wilson `(d − θ_w^c − 2θ_A)·k`; soft `(d − θ_w^r − 2θ_A)·n + θ_w^r`.
  **PASS** iff both symbolic expressions match after expansion. **FAIL** otherwise — and a FAIL means my
  ingredient table is wrong, not that NORMS is.
  *This clause exists because of pre-stated failure mode NBGA-F5: without it the whole check is a
  tautology of my own bookkeeping.*
- **na1-B (the new families).** The script must report, symbolically:
  3-derivative Wilson `d − 4θ_w^c` per unit k; 0-derivative Wilson `d − θ_w^c − 3θ_A` per unit k;
  3-derivative soft `(d − θ_w^r − 2θ_w^c − θ_A)n + …`; 0-derivative soft `(d − θ_w^r − 3θ_A)n + …`.
  **PASS** iff the four leading coefficients are as named. (The `…` constants are not pre-registered: only
  the n-coefficients decide convergence.)
- **na1-C (the verdict at the delivered weight pair).** At `(d, θ_w^c, θ_w^r, θ_A) = (4, 2, 3, 1)`:
  **PASS** iff every one of the four NEW leading coefficients is `≤ −1` (strictly subcritical, geometric
  with ratio `≤ 1/L`), **and** the 1-derivative Wilson coefficient is `0` (marginal, as NORMS records).
  **FAIL** if any new coefficient is `≥ 0`.
- **na1-D (the condition, and the critical dimension).** For each new family the script must solve
  `leading coefficient < 0` for `d`, reporting the largest `d` at which it still holds with
  `(θ_w^c, θ_w^r, θ_A) = (2, 3, 1)`.
  **PASS** iff the reported critical dimensions are **strictly greater than 4** for all four new families
  (i.e. `d = 4` is not the marginal case for any of them). **FAIL** if any is `≤ 4`.
- **na1-E (DESIGNED-FAIL CONTROL — this input is expected to FAIL na1-C).** Re-run na1-C at
  `θ_w^c = 0`, i.e. at the **weightless** form of the background regularity that Proposition COMP actually
  delivers — "(CL-3) `‖X‖_𝔐 ≤ η` implies own-units plaquette logs … `≤ C_3(ε + η)` at every level"
  (PROOF.md l.6608-6610), with no scale weight — and at the induced `θ_A = min(1, θ_w^c − 1)`
  (NORMS.md l.656-657) clipped at `0`.
  **The control is PASSED** iff the script reports **FAIL** for na1-C at this input, i.e. iff at least one
  new coefficient is `≥ 0`. If the script reports PASS at `θ_w^c = 0`, the check has no discriminating
  power and **every na1 verdict is void**.
- **na1-F (second DESIGNED-FAIL CONTROL, on the ingredient table).** Corrupt P6 by replacing the background
  curvature exponent `−θ_w^c n` with `0` (a background whose own-units curvature does not decay with
  depth). **The control is PASSED** iff na1-C then reports **FAIL**.

## Scope, stated in advance
na1 decides **exponents only**. It says nothing about any constant, nothing about whether `ζ^c(V)` obeys
the background versions of (I3)-(I5) (that is (GAP-Z)), nothing about (N-loc), nothing about whether the
critical chain satisfies P6/P7, and nothing about `𝔐`'s own consistency. A PASS of na1-C is **not** a proof
of (N-bg); it is the statement that the background vertex adds no exponent condition.

## Record
Script: `checks/na1_exp.py`. Output: `checks/na1_out.txt`. Both kept unaltered; any re-run gets a new id.
