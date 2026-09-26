# Finite-coupling corrections for the excluded nearest-neighbour pair: a controlled expansion, and the bound 3/2 is leading order only

Task `J:derive:deferred-20260925-nearest-neighbour-finite-coupling:a1`, worker `w-macbookpro9927a-jce96`, model claude-opus-5-5 (owner-requested recovery).

**Files.**
- `check.py`: 9 checks, about 4 s, peak about 280 MB.
  - Families R, F, X, N and I are exact. The Laurent matrices hold Gaussian integers, and the rest is sympy rationals.
  - Family C is floating point and labelled.
- `make_status.py` writes `RECOVERY_STATUS.json`.

## Sources, corrections and overlap

**Block 142 as landed on main.**
- PR #9227, landed at `25b8c1874f`. The note is identical on current `origin/main` `78db61c32a`: sha256 `fb9b11df…`.
- The task's frozen head is `5c7c52847e`, note sha256 `350fd6eb…`.
- The landing review record is `probes/work/deferred-science-20260925/unit-29.json` (sha256 `5e36b2d6…`). Its scope boundary reads: "In three dimensions, a fixed nonzero isolated bond eigenvalue and fixed spectral gaps admit the displayed second-order effective generator as g tends to infinity … finite-g corrections and other interactions remain open."

**Supplied model, taken from the landed note.**
- Two excluded records of block 54's walk.
- The relative generator `⟨r|H₂|r ± e_a⟩` of block 142.
- The neighbour term `V = g Σ_{r=±e_a} |r⟩⟨r| ⊗ M(r)`.

**Choice.** I take the coin-blind case `M = 1`, one of block 142 T3(c)'s rows. Its only bond eigenvalue is `μ₀ = 1`, so no mixing through other bond eigenspaces enters. That mixing is listed as an obligation.

**Corrections preserved.**
- The curvatures are not established physical speeds, inertial stability or fall coefficients.
- Zero bond eigenvalues and gaps that shrink with `g` stay outside the statement.
- The line results of T1 are exact at every `V` and need no correction.

**Provenance.** The claim printed no prior attempts on this problem. The related task `charge-threshold-and-transport` is distinct. I released it earlier and it is not duplicated. No earlier unit of mine treats block 142.

## 1. Statement attempted

**Setting.** Block 142's excluded pair on `ℤ³` at total wave vector `K`, with coin-blind bond term `g`, in either exchange sector. Each sector's bound space has 3 positive bonds × 4 coins, that is 12 states.

- **(a) Control.** Let `F(E) = g + Λ₂/E + Λ₄/E³ + …` be the exact Feshbach series on the bond space. Here `Λ_{2k} = P H₂ (Q H₂ Q)^{2k−2} H₂ P` over paths that avoid bonds and coincidence. For `|g| ≥ 20` and every real `K`:
  - the 12 sector levels near `g` are exactly the fixed points `E_j = g + γ_j(E_j)`, all in `|E − g| ≤ 1`;
  - `|E_j − E_j⁽⁴⁾| ≤ 1856/(|g| − 1)⁵`, where the `E_j⁽⁴⁾` are the fixed points with the series truncated after `Λ₄`.
- **(b) The next order.** To relative order `g⁻²`, `E²/2 − g²/2` is the spectrum of `Ω = Λ₂ + (Λ₄ − Λ₂²/2)/g²`, with `Λ₄` exact from path enumeration.
  - The rest values are `ω + δ/g²`, with `(ω, δ) = (0, 0), (1, 9/2), (4, 8), (5, −15/2)` for fermions and `(1, 9/2), (2, 6), (5, −15/2)` for bosons.
  - Equivalently, `E₀ = g + ω/g + (δ − ω²/2)/g³`.
- **(c) The curvature axis sums.** The energy-squared curvature, summed over the three axes, becomes:
  - fermions: `7/10 + 6/(5g²)`; `3/2 + {3/2, 3/2, −21/2}/g²`; `−1/2 − 12/g²`; `−17/10 + 123/(10g²)`;
  - bosons: `3/2 − 5/(2g²)`; `1/2 − 7/g²`; `−5/2 + 31/(2g²)`.

  So block 142's bound "none exceeds 3/2" holds at leading order only. Two fermion states of the coin-blind `3/2` level reach `3/2 + 3/(2g²)`. T3(d)'s conclusion, that no rest level reaches the free sum 3, persists to this order for `g² > 1`.
- **(d) Inertia at rest.** At a rest point the inertial `K²`-form of `E` is the energy-squared form divided by `E₀`, exactly at every order.

## 2. Steps

**S1. Reproduction. CHECKED R1, R2.**
- The engine enumerates paths with Gaussian-integer Laurent matrices in `u_a = e^{iK_a/2}`.
- It reproduces block 142 T2's same-bond law exactly. No path joins `e_a` to `−e_a` at order 2 or 4, and orders 3 and 5 are empty.
- The coin-blind rest levels are `0, 1, 4, 5` (each ×3) for fermions and `1` (×3), `2` (×6), `5` (×3) for bosons. The leading axis sums are T3(c)'s `7/10, 3/2, −1/2, −17/10` and `3/2, 1/2, −5/2`.

**S2. The Feshbach reduction. PROVED.**

On the excluded relative space, `H(K) = H₂(K) + gP`, where `P` is the projection onto the six bond positions.

*No bond-to-bond term.* `PH₂P = 0`, because every bond position has an odd coordinate sum and each hop changes the parity.

*The Schur complement.* Write `ψ = ψ_P + ψ_Q`. Then `(E − H)ψ = 0` is equivalent to two equations:
- `(E − QH₂Q)ψ_Q = QH₂Pψ_P`;
- `(E − g)ψ_P = PH₂Qψ_Q`.

When `E ∉ spec(QH₂Q)`, `ψ_Q` is determined by `ψ_P`, and `E − g ∈ spec(G(E))` with `G(E) = PH₂Q(E − QH₂Q)⁻¹QH₂P`. Also `ψ_P ≠ 0`, since `ψ_P = 0` forces `ψ = 0`.

*Exchange.* Exchange commutes with everything, so the reduction holds sector by sector. Each sector is represented on the positive bonds as `Λ[a][b] = Λ(e_a, e_b) + sign · Λ(e_a, −e_b)·SWAP`, as in block 142's runner.

**S3. Control for `|g| ≥ 20`. PROVED; CHECKED F1.**

*The series.*
- `‖H₂(K)‖ ≤ 2√3`. The symbol at relative momentum `q` is `σ·s(K/2+q) ⊗ 1 + 1 ⊗ σ·s(K/2−q)`, and `|s|² ≤ 3`. Compressions do not raise the norm.
- For `|E| > 2√3`, `(E − QH₂Q)⁻¹ = Σ_n (QH₂Q)^n/E^{n+1}`. The odd-`n` terms vanish by parity. So `G(E) = Σ_{k≥1} Λ_{2k}/E^{2k−1}`, with `‖Λ_{2k}‖ ≤ 12^k`.

*The window and the contraction.* Take `|g| ≥ 20` and `|E − g| ≤ 1`, so `|E| ≥ 19` and `12/E² ≤ 12/361`.
- `‖G(E)‖ ≤ 228/349 < 1`, so the window is kept.
- `‖G′(E)‖ ≤ 4476/121801 < 1`.
- By Weyl's inequality, the `j`-th ordered eigenvalue `γ_j(E)` is Lipschitz with that constant. So `E ↦ g + γ_j(E)` is a contraction of the window, and each `j` has exactly one fixed point.

*Comparison with the truncation.* Truncating the series after `Λ₄` changes `G` by at most `12³/(|E|⁵(1 − 12/E²))` in norm. By Weyl, it changes each `γ_j` by at most the same amount. The fixed points therefore differ by at most that amount divided by `1 − Lipschitz`, which gives `1856/(|g| − 1)⁵`, uniformly in `K`.

**S4. The effective operator. PROVED; CHECKED X1.**
- For `M = 1`, a level satisfies `E(E − g) = λ(E)`, with `λ` an eigenvalue of `Λ₂ + Λ₄/E² + O(E⁻⁴)`.
- The root near `g` gives `E²/2 − g²/2 = λ − λ²/(2g²) + O(g⁻⁴)`.
- With `λ ∈ spec(Λ₂ + Λ₄/g²) + O(g⁻⁴)`, applying `x ↦ x − x²/(2g²)` as a matrix function gives `Ω`.
- At rest, `E₀ = g + ω/g + (δ − ω²/2)/g³`.

**S5. The next-order curvature. PROVED; CHECKED N1, N2.**

*The structure at rest.* Let `ε = g⁻²` and `Δ = Λ₄ − Λ₂²/2`.
- `[Λ₂(0), Δ(0)] = 0`, and `Δ(0)` is scalar (`δ`) on every rest level (N1).
- So the rest projectors do not change at `O(ε)`, and the reduced resolvent is `R(ε) = R − εR′`, with `R′ = Σ_m P_m (δ_ℓ − δ_m)/(ω_ℓ − ω_m)²`.
- The first-order `K` terms vanish on every level at both orders.

*The formula.* Block 142's weight matrix `W = P(Ω_dd + 2Ω_d R Ω_d)P` therefore has the first-order correction

`W₄ = P[Δ_dd + 2(Λ_d R Δ_d + Δ_d R Λ_d) − 2Λ_d R′ Λ_d]P`,

computed exactly.

*Analyticity.* For `|g| ≥ 20` the level groups stay isolated. Their Riesz projections are analytic in `K` and `ε`. So these are the first two Taylor coefficients of each level's `K²`-form.

*Robustness.* A splitting at `O(ε²)` inside a level cannot enter with small denominators, because `PΩ_dP = 0` on the whole level.

**S6. Inertia at rest. PROVED; CHECKED I1.** `E = √(g² + 2X)` gives `E″ = X″/E₀ − X′²/E₀³`. So where the first-order terms vanish, the inertial `K²`-form of each branch is `W/E₀`, exactly at every order.

**S7. A float cross-check. CHECKED C1 (floating point).**
- Setup: exact diagonalisation of the pair in the box `|r_i| ≤ 3`, at `g = 20`, `K = 0` and `(0.3, 0.2, −0.1)`, in both sectors.
- Result: the 12 levels of each sector agree with `√(g² + 2 spec Ω(K))` to `2.5·10⁻⁵`. The leading order misses by at least `8.7·10⁻⁴`.
- A separate run with `|r_i| ≤ 4` at three `K` gave the same picture (at most `2.5·10⁻⁵`).

## ASSUMED

Nothing beyond block 142's supplied model: the walk, exclusion, and the coin-blind neighbour term. Every step is argued in full. Weyl's inequality for Hermitian matrices and the Riesz projection are used with their elementary proofs.

## 3. Result, first unresolved step and obligations

**Result.**
- For `|g| ≥ 20` the coin-blind pair's levels are controlled to `O(g⁻⁵)`, and the `g⁻³` term is exact.
- The first finite-coupling corrections to the curvature axis sums are exact.
- Block 142's axis-sum bound `3/2` is a leading-order statement. At next order two fermion states of the `3/2` level reach `3/2 + 3/(2g²)`. The conclusion that the free sum 3 is not reached survives to this order.

**First unresolved step.** An explicit constant for the `O(g⁻⁴)` remainder of the curvatures. The energies are controlled, and the `K²`-forms are analytic in `g⁻²`, but they are not bounded explicitly here.

**Remaining obligations.**
1. The covariant non-coin-blind shifts (a ray, the spin `±1` plane). There, mixing through the other bond eigenspaces enters at the same order as `Λ₄`.
2. Moderate coupling, `|g| < 20`. The truncated shifts put the fermion rest levels `4 + 8/g²` and `5 − 15/(2g²)` on a collision course near `g² ≈ 15.5`. That lies outside the controlled region and is not a claim.
3. The passive (fall) response under block 115's conditional ray model. The inertial response at rest is fixed by S6.
