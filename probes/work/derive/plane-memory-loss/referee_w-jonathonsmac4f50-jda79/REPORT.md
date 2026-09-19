# Referee report: J:derive:plane-memory-loss:a2

- **Author:** w-macbookpro90c72-jddd3 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-jda79 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` at sha `59181689`, and its log.

`check.py` in this directory re-verifies the finite facts with independent code (mpmath quadrature at 25 digits).

## The claim

Route (i) is claimed to fail for uniform twists:
- `KL(f_u ‖ f_{R_θ u}) = κA(κ)(1 − cos θ)`.
- "A spatially uniform rotation of the whole plane therefore costs `N κ A(κ)(1 − cos θ)` per level. This is extensive in
  `N` and `T`."
- A constant `θ` "has Dirichlet form 0 and still pays the on-site KL", so the recurrence of the walk cannot help.

## Step by step

**Step 1 (the relative-entropy identity): holds.** Quadrature at `(κ, θ) = (1, 0.4), (3, 1.1), (9, 0.25)` agrees with
`κA(κ)(1 − cos θ)` to 15 digits (Q1).

**Step 2 (uniform against slowly varying twists): does not follow.**
- The one-site kernel is `O(3)`-covariant: `R_* vMF(κu) = vMF(κRu)` (Q2, checked at 20 random points).
- So in the path measure, rotating *every* record of levels `≥ 1` by the same `R` leaves every conditional law of levels
  `≥ 2` unchanged.
- A twist constant in space and in level time therefore costs `N κ A(κ)(1 − cos θ)` once, at the level where it is switched
  on, and 0 at every later level.
- The exact single-site chain (`L = 1`, `S = 3s`) shows this by the chain rule with Q2's identity (Q3):

  | twist | path relative entropy |
  |---|---|
  | constant in level time | `3βA(3β)(1 − cos θ)` for every `T` (level-1 term confirmed by quadrature) |
  | angle growing by `θ` per level | `T` times that |

- A per-level cost arises only when the angle changes from level to level. That change is exactly the level-time Dirichlet
  form `Σ_{x,t} ‖θ(x, t+1) − (Pθ_t)(x)‖²` that the step sets to 0 for constant `θ`.
- So "Dirichlet form 0 and still pays the on-site KL" is inconsistent. To leading order the on-site relative entropy of a
  twist is that level-time form, not a cost separate from it.
- Uniform twists are useless on the infinite plane for the trivial reason that `N` is infinite, not because their cost is
  "extensive in `T`".
- The substantive question the attempt leaves, space-time twists that decay in space, is the one the task poses, and it is
  not addressed.

**Step 3 (`3A(3) > 0`): holds** trivially.

## Classic failure modes

- *A cost read off the wrong object.* Step 2 puts a per-site "on-site KL" where the relevant quantity is the rotation
  mismatch between a record and its predecessors.
- *A missing symmetry.* The `O(3)` covariance of the kernel is not used.

## Verdict

**First failing step: 2.** Its cost statement for uniform twists ("per level", "extensive in `T`", "Dirichlet form 0 yet
pays KL") contradicts the `O(3)` covariance of the kernel.

Step 1's identity holds.

`check.py` prints `SUMMARY: fails at step 2 - ...` and no `HIT: confirmed` line.
