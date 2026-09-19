# Referee report: J:derive:lightcone-formation:a3

- **Author:** w-macbookpro90c72-j05f1 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j2e27 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-j05f1__e5602bda__20260919T013457Z`.

**Disclosure.** This referee's model family has already refereed other attempts of this problem:
- `referee_w-jonathonsmac4f50-j4e7c`;
- `referee_w-jonathonsmac4f50-j63d8`;
- `referee_w-jonathonsmac4f50-j7037`;
- `referee_w-jonathonsmac4f50-j8aa7`;
- `referee_w-jonathonsmac4f50-jdb2a`.

`check.py` here is independent code using exact Fractions.

## The claim

The claim is a finite exact partial result.
1. **Reversibility.** The 7-stencil light-cone chain for the six-axis menu at `(p,1,2)` is reversible with respect to `π ∝ ∏_x Z_x`. The
   product identity is checked exhaustively on `C₃` at `(5,1,2)`.
2. **The cube.** On the `2×2×2` cube, the `π`-weight of a one-site antipodal or orthogonal flip is below that of a constant at
   `p = 3, 5, 10, 20`, and "both ratios decrease in `p`".

The attempt says this is not an infinite-volume ordered-phase theorem.

## Step by step

**Step 1 (product identity): holds, and more generally.** `π(s)T(s→s') = ∏_x ∏_{y∈N[x]} φ(s'_x, s_y)` is symmetric in `(s, s')` whenever `φ`
is symmetric and the stencil is undirected. R1 finds:
- 0 failures, exhaustively, on the 3-ring with the 3-stencil (`6⁶` pairs);
- 0 failures on 300 random pairs on the nondegenerate `3³` torus with the 7-stencil, at `(5,1,2)`;
- exactness to machine precision for sphere spins with `φ = e^{βs·s'}`, which is the task's menu.

**Step 2 (cube flip ratios): holds.** R2 uses my own closed form (the flip site, its three neighbours counted twice on `L = 2`, and four
unaffected sites). It is cross-checked against the direct product over all eight sites. It reproduces the attempt's exact values:

| `p` | antipodal flip / constant | orthogonal flip / constant |
|---|---|---|
| 3 | `2167007881/207594140625` (`1.04·10⁻²`) | `28796658496/207594140625` (`1.39·10⁻¹`) |
| 5 | as stated (`2.07·10⁻⁵`) | as stated (`2.09·10⁻³`) |
| 10 | below 1 (`1.02·10⁻⁷`) | below 1 (`1.31·10⁻⁵`) |
| 20 | below 1 (`7.8·10⁻¹⁰`) | below 1 (`1.0·10⁻⁷`) |

**Correction on "both ratios decrease in `p`".** This holds on the sampled `p ≥ 3`. R3 finds it also holds on every grid point from 3 to 200.
It fails just above `p = max(q,r) = 2`. The orthogonal-flip ratio rises from `0.5658` at `p = 2.01` to a peak of `0.57761` at `p = 2.11`,
then falls. Both ratios stay below 1 on `2.01 … 200`. This is the classic "holds only at the points checked" pattern. The claim as stated
(four points) survives, but the general monotonicity does not.

**Step 3 (what this is not): holds as a limitation.** A one-site cost on the degenerate `L = 2` torus controls no contour sum. The attempt
says so.

## Scope

The task's light-cone law uses `exp(β s·S)` on the sphere. The six-axis restriction of that weight is `(p,q,r) = (e^β, e^{−β}, 1)`, with
`q < r`. The attempt's `(p,1,2)` has `r > q` and is a different weight family.

For comparison, R4 computes the same flip ratios for the exp weights. They are far smaller:
- antipodal: `1.5·10⁻⁶`, `7·10⁻¹³` and `6·10⁻¹⁹` at `β = 1, 2, 3`;
- orthogonal: `1.1·10⁻³`, `8·10⁻⁷` and `8·10⁻¹⁰`.

Not addressed:
- the task's (a) Gibbs identification of `π` and its reflection positivity;
- (b) long-range order for the sphere;
- (c) kernel bounds;
- (d) uniqueness;
- (e) the comparison with the static law.

## Verdict

**The finite claim survives.**
- The reversibility identity holds, and more generally than stated.
- The exact cube ratios at `p = 3, 5, 10, 20` re-derive and are all below 1.
- Monotonicity holds on `p ≥ 3`.

One correction: monotonicity fails for the orthogonal ratio on `(2, 2.11)`. One scope caveat: `(p,1,2)` is a different weight family from
the task's exp law.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
