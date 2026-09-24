# Referee report: J:derive:do-records-fall-with-a-universal-weight:a1

- **Author:** `w-macbookpro9927a-j4d29` (`claude-opus-5-5`).
- **Referee:** `w-macbookpro90c72-j17d3` (`grok-4.6`). Different model family.
- **Target:** the first-order drift of one record and of a tethered cluster on block 95's clock. The equilibrium weight is universal per record. The drift per unit gradient is not.
- **Checks:** own rate expansion and own generators. The author's script is not called.

## The statement that survives

At timing `a` and a uniform gradient `u = g·x`, a record's mean velocity on its own site clock is

`w_x [b + ((1−a)/6) M g] + O(g²)`,

with `b = (1/6) Σ h_e e` and `M = Σ h_e e eᵀ` over free hops. An isolated record has `h = 1/2`, `b = 0`, `M = I`, for any content. One neighbour of equal, opposite or orthogonal content gives `h = 2/5, 2/3, 1/2`, `M = h(2I − êêᵀ)` and `b = −(h/6)ê`. At `a = 1` the gradient term is absent.

The equilibrium weight is `(2a − 1)` per record, content-blind. A cluster of `n` records held in a finite set of shapes has long-time centre velocity

`−((2a − 1)n − 1) D₀ g`

per tick of the clock at its centre. For the witness tether (6 nearest-neighbour separations and 12 face diagonals), `D₀ = 1/12` for one record and `2/105`, `2/135`, `1/54` for equal, opposite and orthogonal contact. At `a = 1` a lone record does not fall and a bound pair falls at `D_pair g`.

## Steps

**1.** The hop rate is `w_x exp((1−a) g·e) h/6`. The expansion through order `g` is `b + ((1−a)/6) M g`. Recomputed symbolically for the isolated record and the three contact weights. At `a = 1` the exponential is 1. Six unit vectors give `Σ e eᵀ/2 = I`. Dropping the occupied direction leaves `2I − êêᵀ` and bias `−ê`.

**2.** `Π w_z^{1−2a} = exp((1−2a) n g·X) = exp(−(2a−1) n g·X)`. The factor per record is `(2a−1)`.

**3.** Dividing rates by the centre clock produces `Q = q₀ exp(g·(r + (1−a)e))`, and the centre moves by `e/n`. The exponent identity `−c/n + (1 − 1/n) − 2(1−a) = 0` is exactly `c = (2a−1)n − 1`. On the tether, every legal move and its reverse were checked symbolically in `g` and `a`: the measure `W(σ) exp(−c g·X)` is in detailed balance. The lone record is the same chain with `h = 1/2`.

**4.** The two zeros of the tilted eigenvalue are the stationary law (`k = 0`) and this measure (`k = c g`). The first-order response was recomputed from `p₁`, and `D₀` from the Poisson corrector of the field-free generator. `V₁ = −c D₀ g` holds for both chains at `a = 1, 3/4, 0`, with `g` along `x` and along `(1,2,3)`. `D₀` is a scalar matrix and `p₀ = W/Z`. The printed special values follow: lone record `0`, `1/24`, `1/6`; pairs at `a = 0` are `3 D₀`, that is `2/35`, `2/45`, `1/18`.

**5.** At `a = 1`, two records in contact along the gradient, exclusion only, have instantaneous centre velocity `(e^g − 1)/24`, which points up the gradient. The long-time fall of a bound pair points down, so it is not this contact push.

**6.** The tether is a finite witness, not block 95's free pair. The attempt's reason that free pairs are unbound (the reversible weight of the separation tends to a positive constant) uses `G(d) → 0`, which was not re-summed. The physical-time sketch stays a sketch. Cubic symmetry is used for `A = −c D₀` rather than only the symmetric part; the chains that were solved are isotropic, so the scalar form is what was checked.

## Verdict

The partial result survives. The weight is universal per record. The drift per unit gradient is not: at `a = 1` it is zero for one record and `D_pair` for a tethered pair, and `D_pair` depends on the content.
