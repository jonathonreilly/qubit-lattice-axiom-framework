# Referee: bodies that slow records without keeping them a3

Author `w-macbookpro90c72-j12a7` (claude-opus-5-5). Referee `w-macbookpro90c72-j7578` (grok-4.6).

Own directed sweep on `[-4,4]^3`. Rates below are in units of `1/√3`, as in the attempt: the hop rate is `m|s_k|/√3`, and the printed force is the code-unit vector divided by `√3`.

## Steps

1. **One site.** Fifty-four signed permutations of `(1,0,0)`, `(3/5,4/5,0)`, and `(2/3,2/3,1/3)`, at `κ=1/3`. The slowed class at each site equals the forward-octant multinomial `h`, the unslowed class is `1−h`, and every site sums to 1. Each shell `|x|_1=n≤4` carries slowed flux 1.

2. **Two sites.** Magnitudes `1` and `1/2`, each with weight `1/2`, so `⟨m²⟩=5/8`. At `(2,0,0)` with `(κ₁,κ₂)=(1/3,1/2)`, `(2,1,1)` with the same, and `(1,2,0)` with `(3/4,1/5)`, the joint sweep equals `(1−κ₁)(1−κ₂)⟨m²⟩` times the collisionless sum, the two forces are opposite, and the pull points toward the other site. A lone site takes nothing. At `(2,1,1)` the code-unit pull is `(-1/675,-8/6075,-8/6075)`.

3. **Run-down.** After `N=7` steps at `n_b=1/5` and `κ=1/3`, `E[κ^K]=(13/15)^7` and `E[κ^{2K}]=(37/45)^7`. The field `m=m0/(1+c t)` with `c=(1−κ) n_b |s|_1 m0/√3` solves `dm/dt=−C m²`, `C=c/m0`, and `∫_0^∞ m² dt=m0/C`. Keeping half the magnitude out to time `T` needs `(1−κ)≤√3/(n_b |s|_1 m0 T)`. On the uniform sphere `⟨|s|_1⟩=3/2`, the two written ceilings are the same number: `4⟨m²⟩|F|/(3 n_b² ⟨m⟩² T²)`.

4. **Healing.** At `κ=1/3`, `a=3/2`, `γ=1/10`, `q=κ a/(κ a+γ)=5/6`. The powers `q^n` for `n=1,5,10,20` are `5/6`, `3125/7776`, `9765625/60466176`, `95367431640625/3656158440062976`.

The occupancy claim “slowed density `ρ f h/κ`” is the slowed flux divided by the reduced hop rate. It is not a second lattice count. Screening past the healing length, and block 52’s biased walk, are the attempt’s arguments.

## Verdict

A slowing site leaves the number flux unchanged, shells sum to 1, and a pair pulls equally and oppositely with a factor `(1−κ₁)(1−κ₂)⟨m²⟩`. The run-down is linear in `(1−κ)` and the pull is quadratic.

`HIT: confirmed`.
