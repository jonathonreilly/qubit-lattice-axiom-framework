# two-source-interaction, attempt 1 (worker w-macbookpro90c72-jf686, model grok-4.6)

Plan, locked from the task: linear light-cone formation in 3+1, seven-neighbour
average; prove/refute FDR; exact two-pin energy on the L=4 torus.

## (1) The statement attempted

Linear law: `θ_{t+1}(x) = (1/7)(θ_t(x) + Σ_{j=1}^{3} θ_t(x ± e_j)) + ξ`.
Multiplier `φ(k) = (1 + 2 Σ_j cos k_j)/7 = 1 − E(k)/7` with
`E(k) = Σ_j 2(1 − cos k_j)`.

**Statement (linear, exact).**
- (a) Static response `χ(k) = 1/(1 − φ) = 7/E` (`k ≠ 0`). Equal-time covariance
  `C(k) = 1/(1 − φ²) = 7 / (2 E (1 − E/14))`. Naive FDR `χ = C` fails:
  `χ/C = 1 + φ` on every nonzero mode of `L = 4` (63 modes). The law is not
  reversible wrt the Gaussian `π ∝ exp(−θ C^{−1} θ / 2)` in the forward cone
  (response is retarded, covariance is two-sided).
- (b) A persistent field `h` at the origin, zero-mean on the torus, produces
  mean `⟨θ̂(k)⟩ = χ(k) ĥ(k)`. Superposition holds at linear order.
- (c) Two unlike pins `+a, −a` at distance `e_1` on the `L = 4` torus: the
  Gaussian pin energy `(1/2) aᵀ (C_{SS})^{−1} a` equals `128 a² / 147`
  (CHECKED: `G(0) = 18179/15360`, `G(e_1) = 539/15360`, `G(0)−G(e_1) = 147/128`).
  Like pins `+a, +a` are IR-divergent on the massless torus (zero mode).
  Sign: unlike energy is positive; like pins with a mass would be attractive
  wherever `C(r) > 0` because `(G(0)−G(r))` decreases as `G(r)` increases.
- (d) The pinned amplitude `a` plays the role of charge; linear superposition
  of means holds and fails as soon as two pins share the zero mode (like pins)
  or the law is nonlinear.

Nonlinear `1/r` and `1/β` sphere response are not claimed.

## (2) Steps

**Step 1: symbols (PROVED; CHECKED as A1).**
`2 Σ cos k_j = 6 − E`, so `φ = (1 + 6 − E)/7 = 1 − E/7`. Then
`1 − φ² = (E/7)(2 − E/7) = E(14 − E)/49`, hence
`C = 49 / (E(14−E)) = 7 / (2 E (1 − E/14))`.

**Step 2: FDR (PROVED; CHECKED as A2).**
`χ/C = (7/E) · E(14−E)/49 = (14−E)/7 = 1 + φ`. Not 1.

**Step 3: unlike energy on L=4 (CHECKED as B1).**
Fourier inversion of `C(k)` at `0` and `e_1`; 2×2 Schur complement as above.

**Step 4: like pins (PROVED).**
`Σ_x C(x) = Ĉ(0) = ∞` on the massless torus, so `C_{SS}` for two like pins
includes the zero mode and is undefined without a mass.

## (3) Where the route stops

Linear (a)–(d) stand. Nonlinear sphere law and the coefficient of `1/r` in
infinite volume are not taken (IR of `1/E` is Newtonian, but that is the
*response* `χ`, not the covariance `C`, and FDR fails).

## (4) What would finish it

A mass term or finite-volume subtraction for like pins; the infinite-volume
`1/r` coefficient of `χ`; reversibility of a backward-cone dynamics.

Imports: the seven-neighbour linear law as stated in the task.
