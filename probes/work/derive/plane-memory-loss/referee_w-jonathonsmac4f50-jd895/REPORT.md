# Referee report: J:derive:plane-memory-loss:a1

- **Author:** w-macbookpro90c72-j8231 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-jd895 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` at sha `4e191693`, and its log.

`check.py` in this directory re-verifies the finite facts with independent code (exact rationals, sympy, mpmath).

## The claim

The attempt makes two claims.
- **Route (ii) fails.** The linear formation law has `φ(0) = 1`, so "the spatial-mean mode is a martingale and does not
  decay", and "a comparison that dominates the nonlinear law by the linear law cannot prove `m_t → 0`".
- **Mean field.** `A(k) = k/3 − k³/45 + O(k⁵)`. At `β = 1`, `|m'| = |m| − (3/5)|m|³`. The mean-field map forgets for
  `β ≤ 1`, and block 27's `1/√3` is smaller.

## Step by step

**Step 1 (`φ(0) = 1`): holds.** The zero mode of the linear AR is a random walk, and its mean is conserved (P1).

**Step 2 (the linear comparison is a no-go): does not follow.**
- The step's premise is that the linear law does not forget. On the plane that is false.
- Starting from the aligned plane, the linear transverse site variance is `v_t = σ² Σ_{k<t} P_k`, where `P_k` is the return
  sum of the walk with steps `0, e₁, e₂`.
- P2 computes it exactly: `v_t/σ²` is `1.646`, `2.239`, `2.817` and `3.391` at `t = 4, 16, 64, 256`. It grows by `0.414`
  per unit `log t`, against `c₀ = 3√3/(4π) = 0.4135`.
- So `v_t → ∞`, and the linear magnetization proxy `e^{−v_t}` of block 26 T5 tends to 0. The linear law on the plane
  forgets its initial direction.
- The mechanism is the random walk of the zero mode. The conserved *mean* of the zero mode is not the magnetization.
- So the stated obstruction is the forgetting mechanism itself. A comparison bounding the nonlinear transverse variance below
  by the linear one would prove `m_t → 0`, not fail to.
- This is not a proof of route (ii). The attempt's no-go simply does not hold.
- For contrast, the 3D 7-stencil's return sums decay like `k^{−3/2}` and are summable, so there the linear proxy stays
  positive (P2). The attempt treats both stencils alike, but only the plane is the task's object.

**Step 3 (mean-field jet): holds.**
- `A(k) = k/3 − k³/45 + 2k⁵/945 + O(k⁷)`.
- `3k cosh k − 3 sinh k − k² sinh k = −k⁵/15 − k⁷/210 + O(k⁹)`.
- `A(3m) = m − (3/5)m³ + O(m⁵)`.
- `A(k) < k/3` at 500 points of `(0, 50]`, and it is marked ASSUMED globally.
- P3 checks all of these.

**Step 4 (Dobrushin against mean field): holds.** `A(3βm) ≤ βm` for `β < 1`. There is a positive fixed point for
`β > 1`: at `β = 1.5`, `m = 0.6757`. And `1/√3 < 1` (P4).

## Classic failure modes

- *The wrong statistic.* Step 2 reads the conserved mean of the zero mode as the magnetization.
- *Quantifier and circularity.* None.

## Verdict

**First failing step: 2.** The stated no-go for route (ii) rests on the false premise that the linear model on the plane
does not forget.

Steps 1, 3 and 4 hold and were re-verified independently.

`check.py` prints `SUMMARY: fails at step 2 - ...` and no `HIT: confirmed` line.
