# Referee report: J:derive:no-waves-under-positive-formation:a1

- **Author:** w-macbookpro90c72-jf118 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-jadef (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` at sha `1d13cbb0`, and its log.

`check.py` in this directory re-verifies the finite facts with independent code (sympy, numpy roots).

## The claim

The attempt claims three things:
- A two-level positive gain-one model `θ_{t+1} = aθ_t + b e^{iφ} θ_{t−1}` has spectral radius 1 only at the uniform mode:
  roots `1` and `−b` at `φ = 0`, and `|λ|² = 1/2` at `a = b = 1/2`, `φ = π`.
- "Positivity over two earlier levels does not produce waves."
- "Unitary phases are the weakest wave-producing drop of positivity", with `λ = e^{ic|k|}` given as the example.

## Step by step

**Step 1 (`φ = 0`): holds.** The roots are `1` and `a − 1 = −b`, and the discriminant is `(a − 2)²` (N1).

**Step 2 (`a = b = 1/2`, `φ = π`): holds.** The discriminant is `−7/4` and `|λ|² = 1/2` (N2).

**The general positive two-level statement: true, but only instantiated.**
- Steps 1–2 check two points, and the statement concludes for all `φ` and all positive `(a, b)`.
- The general claim holds, by a two-line argument the attempt does not give:
  - if `|z| > 1`, then `|z|² ≤ a|z| + b < |z|²`, a contradiction;
  - equality `|z| = 1` forces `z = e^{iφ} = 1`, i.e. `φ = 0 (mod 2π)`.
- N3 confirms it on 40 values of `a` and 360 phases: every root has `|λ| ≤ 1`, with `|λ| = 1` only at `φ = 0`.

**Step 3 (the weakest change that gives waves): does not follow.**
- The step checks only `|e^{ik}| = 1`, which exhibits no kernel with linear dispersion.
- The stated example `λ = e^{ic|k|}` is not the multiplier of any finite-range kernel. It has right derivative `ic` and left
  derivative `−ic` at `k = 0` (N4), while a finite-range multiplier is smooth.
- The ordering "unitary is the weakest" is contradicted by the exception the task itself names: a record formed from two
  earlier levels with a negative weight.
  - The discrete wave equation has weights `2 − 2c²`, `c²`, `c²` on level `t` and `−1` on level `t − 1`, sums to 1 (gain
    one), and keeps the records real.
  - It has `|z| = 1` exactly and `arg z = k/2 − k³/64 + O(k⁵)` at `c = 1/2` (N5).
  - It drops only positivity, whereas unitary complex weights also give up real records.

## Classic failure modes

- *A conclusion checked only at instances.* The general positive statement, which is true.
- *A superlative without comparison.* "Weakest", contradicted by the real negative-weight example.
- *An example outside the class.* `e^{ic|k|}` is not a finite-range multiplier.

## Verdict

**First failing step: 3.** Its conclusion that unitary phases are the weakest wave-producing change does not follow, and
the real negative-weight example contradicts it.

Steps 1–2 hold. The general positive two-level statement is true: its short proof is given above and confirmed on a grid.

`check.py` prints `SUMMARY: fails at step 3 - ...` and no `HIT: confirmed` line.
