# Referee report: J:derive:plane-memory-loss:a4

- **Author:** w-macbookpro90c72-jcb00 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j19a8 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-jcb00__ff0ae2f8__20260919T012130Z`.

**Disclosure.** This referee's model family refereed attempts a1, a2 and a3 of this problem (grok). The linear-model point below is the one
recorded against a1 (`referee_w-jonathonsmac4f50-j8129`). `check.py` is independent code: sympy with exponential rewrites, exact integers
and mpmath. Nothing is taken from the author's script.

## The claim

- **Mean-field.** The map `m ↦ A(3β|m|)` sends every `m ∈ [0,1]` to 0 iff `β ≤ 1`.
- **Route (ii) no-go.** The claim is that "`|S| ≥ |ES| = 3|m|`" together with `A` increasing gives `A(β|S|) ≥ A(3β|m|)`, which is the wrong
  sign for contraction.
- **The linear model.** "The linear model conserves the uniform mode (`φ(0) = 1`) so cannot supply the decay."

## Step by step

**Step 1 (`A(κ)/κ < 1/3`): holds.** M1:
- `(κ/3 − A)·3κ sinh κ = q`, where `q = (3+κ²) sinh κ − 3κ cosh κ`;
- `q' = κ(κ cosh κ − sinh κ)` and `(κ cosh κ − sinh κ)' = κ sinh κ`;
- `A/κ = 1/3 − κ²/45 + O(κ⁴)`.

**Step 2 (`A` increasing): holds.** M2.

**Step 3 (mean-field threshold `β = 1`): holds.** M3: orbits from `m = 1`:

| `β` | behaviour |
|---|---|
| 0.9 | goes to 0 |
| 1.0 | goes to 0 slowly (`m₃₀₀₀ = 0.0167`) |
| 1.2 | converges to the fixed point `0.502` |
| 2.0 | converges to the fixed point `0.789` |

**Step 4 (route (ii) no-go): does not follow.** Its inequality fails under either reading of `m`:
- **`m` is the plane magnetization, the mean of a record.** Then `|S| ≥ 3|m|` is false pointwise. On the second level of the aligned start,
  records `(+z, +z, −z)` lie in the support of the vMF law and give `|S| = 1 < 3A(3) = 2.0149` at `β = 1` (M4).
- **`m` is the average of the three realized records.** Then `|S| = 3|m|` is an identity and carries no sign. The attempt's "integer
  witness" `2e_z + e_x` is of this kind.

Either way, the stated no-go is not established.

**Step 5 (the linear model cannot forget): false.** M5:
- `φ(0) = 1` conserves the *mean* of the uniform mode, but not the magnetization.
- The linear model's per-site variance after `t` levels is `σ² Σ_{s<t} q_s`. Here `q_s` is the return probability of the difference of two
  three-point walks, `q_s = Σ (s!/(a!b!c!))²/9^s`, computed exactly.
- `s·q_s = 0.40940, 0.41247, 0.41324` at `s = 25, 100, 400`, approaching `3√3/(4π) = 0.41350`.
- So the variance grows like `0.4135 σ² log t`, and the projection on the initial direction decays. This is the same error recorded against a1.

## Verdict

The claim fails at step 4, and step 5 is also false. Steps 1–3 hold.

`check.py` prints `SUMMARY: fails at step 4 - ...` and no HIT line.
