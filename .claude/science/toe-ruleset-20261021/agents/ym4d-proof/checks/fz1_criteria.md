# checks/fz1_criteria.md — pre-registered criteria for check fz1

**Written 2026-10-28 22:1x UTC, BEFORE `checks/fz1_fwd.py` exists.** No constant below is derived in
this session: every exponent and weight quoted is read from a file written in an earlier session
(`BFT_A.md` §1.3, §1.4, §7.2, `[RBA1-fix]`; `BFT_B.md` §15.0), by file:line, and the only arithmetic
the script does is exact integer exponent bookkeeping in `fractions.Fraction` / integer powers.

## What fz1 tests

A single question of **unit bookkeeping**, in exact arithmetic:

> For the flat composite chain Hessian `𝓑` (the Feynman-free Hessian at the trivial chain, `BFT_B`
> l.2035), is the FORWARD operator norm `‖𝓑‖_{𝔐^∇ → 𝒴^∇}` bounded uniformly in `k`?

This is the object `HESSREL.md` l.193 names **(FWD-0)** and reports as *"stated nowhere in the lane"*.

## Inputs, all quoted by file:line (none produced this session)

- `BFT_A` l.31-32 (§1.3): level-`j` 1-form coarse value `x^c_j := L^{k-j}x_j`; residual
  `r_j(x) := Q x_j − x_{j+1}`, coarse `r^c_j := L^{k-1-j}r_j`.
- `BFT_A` l.38 (§1.4): `‖x‖_𝔐 := max_{0≤j<k}[ ‖x^c_j‖_{∞,m} + ‖∇^cx^c_j‖_{∞,m} + [∇^cx^c_j]_{α,m} +
  L^{k-1-j}‖r^c_j‖_{∞,m} ]`. **No level weight ω appears.**
- `BFT_A` l.396-400 (`[RBA1-fix]`, the corrected `𝒴^∇`, which supersedes §1.4's): slot **(R)**
  residual-type `s_l` (a level-`(l+1)` 1-form) `= max_l ω_l L^{k-1-l}‖s^c_l‖_{∞,m}`; slot **(Pl, F3)**
  plain level-`l` currents `= max_l ω_l L^{(2+α)(k-l)}‖j_l‖_{own,∞,m}`.
- `BFT_A` l.466 (§7.2 (R)) and l.768 (`BL-5 (c)`, **PROVEN-HERE**): the (R) weight is
  `ω^R_l := L^{θ(k−l)}` **for every `0 ≤ l < k`**, i.e. `ω^R_0 = L^{θk}`, not 1.
- `BFT_A` l.447 (§7.1): the chain energy's soft term is `Σ_{l<k}(κ_l/2)‖r_l(x)‖²` and a residual-type
  source enters as `−⟨s_l, r_l(x)⟩`, so the gradient of the soft term **is** a residual-type source
  with `s_l = −κ_l r_l(x)`.
- `BFT_A` l.453 (BL-2 (b)): `Q_l` maps constant 1-forms to `L` times themselves.
- `BFT_A` l.834: the proven window is `θ > 0`, `θ < 1`, `α ≤ θ`. **`θ = 0` is not available**
  (`BFT_A` §3.11 row 1: the soft bound is "uniform iff `Ω < ∞`, i.e. `θ > 0`").

## The witness, fixed before the script runs

`k ≥ 2`, `L ≥ 3` odd. The displacement `x` with `x_1 := −c` for a **constant** level-1 1-form `c` of
own size `|c| = 1`, and `x_j := 0` for every `j ≠ 1` (in particular `x_k = 0`, so it is a
displacement). Then `r_0 = c`, `r_1 = −Lc`, `r_j = 0` for `j ≥ 2`, and `∇^cx^c_1 = 0`.

## Pre-registered verdicts

- **fz1-A (the main gate).** Compute, exactly, `ρ(k, L, θ) := ‖𝓑x‖_{𝒴^∇,(R)} / ‖x‖_{𝔐^∇}` for the
  witness, as a function of `(k, L, θ)` with `κ_l ≡ 1`.
  - **PASS** if `ρ` is **unbounded in `k`** for every `θ ∈ (0, 1)` — specifically if
    `ρ(k, L, θ) = L^{θk}` exactly (so `ρ → ∞`).
  - **FAIL** if `ρ` is bounded uniformly in `k` for some `θ ∈ (0, 1)`, or if the computed `ρ` differs
    from `L^{θk}` by any factor depending on `k`.
  A PASS means **(FWD-0) is FALSE** as a `k`-uniform statement in the pair `(𝔐^∇, 𝒴^∇)`.
- **fz1-B (the alternative-representation gate).** Compute the same ratio when the soft gradient is
  instead represented in the **(Pl, F3)** plain-current slot (`j_l := κ_lQ_l^Tr_l` at level `l` and
  `j_{l+1} := −κ_lr_l` at level `l+1`, which is the only other exact representation among the four
  slots of `[RBA1-fix]`), using `BL-2 (c)`'s coarse-plain contraction `‖(Q^Tj)^c‖_∞ ≤ ‖j^c‖_∞`.
  - **PASS** if the (Pl) ratio is **≥** the (R) ratio for every `k ≥ 2`, `0 < α ≤ θ < 1`, `L ≥ 3`
    (i.e. the alternative representation does not rescue (FWD-0)).
  - **FAIL** otherwise — in which case (FWD-0) may survive via the (Pl) slot and fz1-A does not settle it.
- **fz1-C (DESIGNED-FAIL CONTROL 1, must NOT return "unbounded").** Re-run fz1-A's computation with
  the weights set to `ω_l ≡ 1` (the `θ = 0` reading, which `BFT_A` l.834 excludes). The gate must
  return **bounded** (`ρ = 1`). If it returns "unbounded" here, the gate is firing on something other
  than the weight asymmetry and fz1-A is void.
- **fz1-D (DESIGNED-FAIL CONTROL 2, must NOT return "unbounded").** Run the same ratio on the
  **(G) divergence-form slot** for the level-0 Wilson term: the gradient of `½‖dx_0‖²` is
  `G_0 = dx_0` with `ω_0 = 1`, against `𝔐^∇`'s `‖∇^cx^c_0‖_∞ + [∇^cx^c_0]_α` at level 0. The gate must
  return **bounded** (ratio `≤ 2`, the antisymmetrisation count). If every slot comes back
  "unbounded", the gate does not discriminate between slots and fz1-A is void.

## Not success

- Any verdict obtained by floating-point arithmetic.
- Treating `θ = 0` as an admissible repair (it is excluded by `BFT_A` l.834).
- Reading a PASS on fz1-A as a statement about `‖𝓑^{-1}‖` (the inverse direction); fz1 tests the
  forward direction only, and the two are not reciprocal because the pair is not symmetric.
