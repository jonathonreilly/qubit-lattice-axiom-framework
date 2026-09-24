# Referee report: J:derive:many-bodies-of-both-signs-at-rest:a1

- **Author:** `w-macbookpro90c72-j3f15` (`claude-opus-5-5`).
- **Referee:** `w-macbookpro90c72-j286a` (`grok-4.6`). Different model family.
- **Checks:** the 5³ Dirichlet Green function by a sparse solve, the certificate, the quartic, and the symbolic bounds. The author's elimination is not called.

## The statement

On the box with walls held, charges `Q = (4, −2)` put a negative body past its single-body bound while every rate stays positive. A positive neighbour extends that bound. Two negative bodies stay inside their single bounds. A zero-ledger pair is static, with no length monopole and a negative rate monopole. Walk content on a closed lattice rests only if `e = 0`.

## Steps

**S1.** An independent solve of `−Δg = δ` on `{1..5}³` reproduces `G_AA = 68/297`, `G_AB = 37/594`, `G_BB = 34706593/153333180`. The residual is `10⁻¹⁶`.

**S2.** At `Q = (4, −2)`, `μ ≈ (7.165, −1.593)`, below `−1/(4G_BB) ≈ −1.104`. Lengths stay at least `0.797`, `N` at least `0.872`, and the rates lie in `[0.487, 2.556]`. The smallest eigenvalue of `L` is positive, and `LN = 0` with `N = 1` on the walls.

**S3.** `v_B > −(1 + a v_A)/(b + D v_A)` is the determinant condition, and it equals `−1/b − c² v_A/(b(b + D v_A))`. For `v_A > 0` the threshold lies below `−1/b`.

**S4.** The exact quartic in `Q_B` has degree 4 and two real roots. Both have positive lengths. Only one makes `G⁻¹ + V` positive definite.

**S5–S6.** `Q(1 + gQ) ≥ −1/(4g)`, with equality only at the single-body fold, so a second negative body makes the inequality strict when `G_AB > 0`. A symmetric pair folds at `−1/(4(g₀ + g_d))`. On the box that fold is about `−1.010`, above the single bound `−1.104`; `0.99` of it is real and `1.01` of it is not. The zero-ledger pair `Q = (1, −1)` has `P_A + P_B ≈ −0.774`.

**S7–S9.** Differentiating `F + ⟨H⟩` on a ring of four sites gives the two field equations. If `e = τ`, then `S_N = −3 S_χ`, so both sums of squares vanish. One opposite-sign pair never has `Σe < 0 < Στ`. The capacity bound `Σμ ≥ −Cap/4` is the Cauchy–Schwarz estimate `QᵀGQ ≥ q²/Cap`.

The `Z³` continuation table was not recomputed. It is not needed for the exact box certificate.

## Verdict

The partial result survives. A negative body can sit past its single-body bound when a positive neighbour is present, with every rate positive.
