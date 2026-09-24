# Referee report: J:derive:pinned-what-is-a-source:a3

- **Author:** `w-macbookpro90c72-j93fc` (`claude-opus-5-5`).
- **Referee:** `w-macbookpro90c72-j02f9` (`grok-4.6`). Different model family.
- **Checks:** the formation factor, the Dirichlet bound and the pocket counts, recomputed. The author's script is not called. The cube capacities on `Z³` were not re-solved.

## The statement

At the pinned scale `c₀ = β/sinh β`, no compact candidate gives a far field proportional to `N`. A pinned set is a Dirichlet condition whose capacity grows at most linearly. Production sits on agreement pockets, which a box does not have and a ball has only on its surface.

## Steps

**E1–E3.** `∫ e^{β cos θ} sin θ dθ/2 = sinh β/β`, so one bond averages to 1 exactly at `c₀`. The formation factor is `Z = c₀^k sinh(β|S|)/(β|S|)`. For aligned contents, `φ(x) = log(sinh x/x)` has `φ'' = (sinh²x − x²)/(x² sinh²x)`. Since `sinh x − x` vanishes with its first derivative at 0 and has second derivative `sinh x > 0`, `φ'' > 0`. Thus `log Z_k` is strictly convex, `Z₀ = Z₁ = 1`, and `Z_k > 1` for `k ≥ 2`. `Z₂ = β coth β`. An opposite pair has `|S| = 0`, so `Z = c₀² < 1`. At `β = 2` the aligned values are `2.075, 5.637, 17.228, 56.158, 190.685`.

**E4–E5.** The one-step response along a pinned direction is `L = coth β − 1/β`. At `β = 2` and `ρ = 1/2` the path amplitudes `(ρ L)^d` are `0.2687, 0.0722, 0.0194, 0.0052`.

**S4.** A perturbation invariant under rotations about the order cannot source a transverse vector. That is the symmetry lemma, and it holds at every order. It covers an unpinned aligned cluster, a density excess, and a formation-rate region.

**C1–C3.** The test function `min(1, R/‖x‖_∞)` has energy `6 R² Σ_{m≥R} (1/m + 1/(m+1))²`. Each term is at most `4/m²`, and the sum is at most `4(1/R² + 1/R)`, so the energy is at most `24 + 24R ≤ 48R`. The partial sums give `E/R = 25.74, …, 24.03` for `R = 1…8`. The massless Green function satisfies `G(0) − G(e) = 1/6`. A nearest pair then carries `0.746` of two separate charges, so pinned records add only when they are dilute. The executed cube capacities were not re-solved; they are not needed for the upper bound.

**P1–P3.** Every axis-aligned box with sides at most 6 has no outside site touching two records, so its excess production in empty surroundings is zero. Discrete balls at `R² = 4, 25, 64, 144` have pocket counts `(24,0), (84,56), (228,120), (528,272)`, which is surface scaling. The tree-level face excess starts at `5ρ(β coth β − 1) > 0`.

## Verdict

The partial result survives. No compact candidate in these channels has a far field proportional to `N`. The transverse results use the quadratic stand-in, which the attempt marks as assumed.
