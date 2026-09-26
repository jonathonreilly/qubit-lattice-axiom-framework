# Rotor-tail residual: the dark phases of the fibre generator, and when the exponent 5/2 is exact

Task `J:derive:deferred-20260924-residuals:a1`, worker `w-macbookpro9927a-j1af8`, model claude-opus-5-5 (owner-requested deferred-science recovery, batch 15, first bounded pass).

**Files.**
- `check.py`: 8 exact checks, about 10 s.
- `make_status.py` writes `RECOVERY_STATUS.json`: dispositions for every batch-15 group, sha256 verification, and log links.

## Choice of residual, and why not #8960 first

The task starts at #8960. Its review deferred two residuals: the unsupported GR mass/stress identification and the unproved lattice-error order.

**The stress identification overlaps my own earlier work.**
- #8960's note itself cites my probe `internal-hop-energy-and-the-two-masses` a1 (`w-macbookpro90c72-jdb03`, issue #8732) for exactly that stress question.
- The related `bending-over-fall-at-strong-field` has my attempt `w-macbookpro9927a-j7735` and two other workers' files.
- `p-equals-q-for-compact-and-strong-bodies` has no attempt.

Under my standing rule against repeating my own work, I took the task's stated alternative: a distinct rotor-tail residual from #8957/#8958 (codex mobile-record lane). The two #8960 residuals stay open and are listed in the status file.

**The residual taken.** #8958 proves `f_i(τ) ≥ c_i(1+τ)^{−5/2}` and states: "The exponent 5/2 in (1) is a sufficient lower bound, not a claimed exact power law. Other exceptional phases or flatter dispersion may give slower decay." #8957 records only "a perfectly sharp flat Fourier phase has a dark vector". The question here is when the exponent is exact.

## Sources

Reused, landed at `1cb2a082bf` and identical on `origin/main` `78db61c32a` (sha256 recorded and verified):
- the two notes;
- the exact control `scripts/mobile_rotor_exact_tail_control_20260924.py` (sha256 `53170069…`). `check.py` copies its construction logic unchanged: the words, the dark/bright split, and the bright-from-dark Laurent block with its winding exponents.

The frozen heads are `fb9edf315a` (#8957) and `1aec3ad3e4` (#8958). All manifest hashes match there: 97 and 40 files.

## Setting

As in #8957/#8958:
- the rotor cube with `N = 6`, total charge 4 and `W = 1`;
- the fibre generator `L(θ) = −iδG(θ) − κP_bright` on `L²(T⁵; ℂ⁹⁶)`, with `δ, κ > 0`;
- `G`'s dark/dark block vanishes identically, and `B(θ)` is its 72×24 bright-from-dark block;
- `f_i(τ) = ‖V(τ)r_i‖²` for the three actual first-mark inputs.

## 1. Statement attempted

- **(a) Dark phases ⟺ rank drop.** `L(θ)` has an eigenvalue on the imaginary axis if and only if `B(θ)` has a nonzero kernel. Such eigenvalues are 0, and their eigenvectors are the dark kernel vectors.
- **(b) The half-period lattice.** Among the 32 phases in `{0, π}⁵`, exactly 8 are dark, not only the flat one:

  | `z = e^{iθ}` | kernel dim |
  |---|---|
  | `(1,1,1,1,1)` | 1 |
  | `(1,1,1,−1,−1)` | 1 |
  | `(1,−1,−1,1,−1)` | 2 |
  | `(1,−1,−1,−1,1)` | 1 |
  | `(−1,1,−1,1,1)` | 1 |
  | `(−1,1,−1,−1,−1)` | 2 |
  | `(−1,−1,1,1,−1)` | 4 |
  | `(−1,−1,1,−1,1)` | 2 |

  The total dimension is 14.
- **(c) Non-degeneracy.** At each of these points the pencil `[B | ∂₁B·K | … | ∂₅B·K]` has full column rank `r + 5 dim K`. Hence `Re⟨w, E(θ)w⟩ ≤ −c|θ − θ*|²‖w‖²` on the dark kernel, where `E` is the second-order reduced generator.
- **(d) Overlaps.** The three actual inputs overlap every dark kernel with weights `1/12, 1/12, 1/6` per kernel dimension. At the flat phase these are #8958's values.
- **(e) Conditional exact exponent.** If no dark phase lies off `{0, π}⁵`, then `c_i(1+τ)^{−5/2} ≤ f_i(τ) ≤ C_i(1+τ)^{−5/2}`: the exponent 5/2 is exact.
- **(f) Reduction of the off-lattice question.**
  - 20 monomial pivots, which are units on `(ℂ*)⁵`, reduce `B(z)` to a 52×4 residual with the same kernel dimension at every `z`.
  - A dark phase then needs one of two things:
    - (i) a rank-deficient 4×3 block, one of whose 3×3 minors is `−(z₂³ − z₄³z₅)(z₂³z₅ − z₄³)(z₁z₃ + 1)`; or
    - (ii) all 48 last-column entries zero, which forces `z = (−1, −1, 1, 1, −1)`, already a half-period dark point.

## 2. Steps

**S1. Dark phases ⟺ rank drop. PROVED.**
- For a unit vector `v`, `Re⟨v, L(θ)v⟩ = −κ‖P_bright v‖²`, since `G(θ)` is Hermitian.
- So if `L(θ)v = iωv`, then `v` is dark. Because the dark/dark block of `G` is zero, `L(θ)v = −iδB(θ)v`, which is bright, and it must equal `iωv`, which is dark. Hence `B(θ)v = 0` and `ω = 0`.
- Conversely, every `v ∈ ker B(θ)` has `L(θ)v = 0`, and also `L(θ)*v = iδG(θ)v − κP_bright v = 0`, so the left and right kernels agree.

**S2. The source's invariants. CHECKED S1.** Grades 36/96/36, 24 dark and 72 bright words, flat-phase rank 23 with the uniform kernel.

**S3. The half-period lattice. CHECKED H1.**
- At `z ∈ {±1}⁵` every entry of `B` is an integer, so the ranks are exact.
- Exactly the 8 points of (b) are rank-deficient.
- An earlier float-based pass mis-evaluated `1**(−1)` as a float. The check uses exact parities.

**S4. Non-degeneracy. PROVED; CHECKED H2.**

*The reduced generator.* At a dark point `θ*` with orthonormal kernel `K`:
- the first-order reduced term `K*L₁K` vanishes, because `G`'s dark/dark block is zero identically in `θ`, and `K*L₂K` vanishes for the same reason;
- so the reduced generator is `E(θ) = K*L₁SL₁K + O(|θ − θ*|³)`, with `S = −L(θ*)⁻¹` on `K^⊥`.

*Its real part.* Put `a = G₁w` and `y = L(θ*)⁻¹a`. Then `Re⟨w, L₁SL₁w⟩ = δ² Re⟨a, L⁻¹a⟩ = −δ²κ‖P_bright y‖²`.

*When it vanishes.* This is zero if and only if `y` is dark. Then `a = L(θ*)y = −iδB(θ*)y`, so `a ∈ range B(θ*)`. The full-rank pencil excludes `Σ_k θ_k ∂_kB(θ*)w ∈ range B(θ*)` for real `θ ≠ 0` and `w ≠ 0`. By compactness of the unit sphere this gives the bound in (c), for every `δ, κ > 0`.

**S5. Overlaps. CHECKED H3.**
- The winding of each input word `(q, E)` is the chord part of `E − ref(q)`.
- Evaluate each input's Fourier vector at the eight points and project onto the kernel. This gives `(1/12, 1/12, 1/6)` times the kernel dimension.

**S6. Conditional exact exponent. PROVED given the hypothesis in (e).**

*Away from the dark phases.* Suppose the dark set `Z` is the 8 points. Take any neighbourhood `U` of `Z`. Continuity and compactness give a spectral abscissa at most `−2γ < 0` on `T⁵ ∖ U`, and a Riesz–Dunford contour uniform in `θ` gives `sup ‖e^{τL(θ)}‖ ≤ Ce^{−γτ}` there.

*Near each dark point.*
- The eigenvalue group at 0 has an analytic total projector `P(θ)`.
- By S4 the reduced generator obeys `Re ≤ −c|θ − θ*|²`, up to a uniformly equivalent norm on `ran P(θ)` for small `|θ − θ*|`.
- The complement decays exponentially, uniformly in `θ`.

*Conclusion.* Plancherel gives `f_i(τ) ≤ Σ_{θ*} C∫e^{−2cτ|θ−θ*|²}dθ + Ce^{−2γτ} ≤ C_i(1+τ)^{−5/2}`. #8958 supplies the lower bound. By S5 every dark point contributes at the same order, so `C_i` sums eight Gaussian contributions.

**S7. Reduction of the off-lattice question. PROVED; CHECKED G1, G2.**

*The unit-pivot elimination.* Pivoting on single-monomial entries with coefficient `±1` keeps every entry in `ℤ[z^{±1}]`, and each pivot is nonzero on `(ℂ*)⁵`. So `dim ker B(z) = dim ker Res(z)` for the 52×4 residual `Res(z)`, at every `z`.

*The case split.* Four residual rows avoid the last column. If their 4×3 block has rank 3 at `z`, a kernel vector must vanish in those three coordinates. The 48 other rows then leave only `w₂₁`, which must vanish unless all 48 last-column entries are zero. So a dark phase needs either:
- **(i)** a rank-deficient block, whose minors include `−(z₂³ − z₄³z₅)(z₂³z₅ − z₄³)(z₁z₃ + 1)`; or
- **(ii)** all last-column entries zero.

*Branch (ii).* The entries include `z₅ + 1`, `z₂ + z₄`, `z₃ + z₄z₅` and `z₃ + z₅`. So branch (ii) forces `(z₂, z₃, z₄, z₅) = (−1, 1, 1, −1)`, and the remaining entries have gcd `z₁ + 1`.

**Numerical evidence (floating point; not part of check.py).**
- 300 Nelder–Mead starts minimising `σ_min(B(θ))` on `T⁵` converged only to half-period points.
- A 7⁵ grid found `σ_min ≥ 0.2` at every grid point.

## ASSUMED

- **A1.** #8957/#8958's premises as landed: the fibre representation, the compact-fast-time reduction, and the actual first-mark vectors. The joint limit is taken first, and no laboratory-time or physical-selection conclusion is drawn.

## 3. First failing step and next obligation

**First unresolved step: branch (i).** Show that on `T⁵` the 4×3 block is rank-deficient, and the remaining 48 rows leave a kernel, only at half-period points. This is needed in each of the three sub-cases `z₁z₃ = −1`, `z₂³ = z₄³z₅` and `z₂³z₅ = z₄³`. Each is a codimension-one torus set. The other three minors have degree 11–12, about 100 terms each.

**Next obligation.** A Gröbner or resultant computation of the common torus zeros in each sub-case, or a positivity certificate for `det(B*B)` away from the 8 points. Either would make (e) unconditional.

**Preserved.**
- #8957's strong-versus-uniform distinction (`‖V(τ)‖ = 1`).
- #8958's lower bound, with this attempt's upper bound conditional.
- #8960's two residuals stay open.
