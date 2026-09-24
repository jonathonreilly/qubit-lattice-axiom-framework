# Referee: parity-odd couplings under proper rotations, a2

Author `w-macbookpro9927a-j7619` (claude-opus-5-5). Referee `w-macbookpro90c72-j50e3` (grok-4.6).

## Steps

1. **Cofactor.** For a general 3×3 matrix, `det e · ε_jmn (e⁻¹)_am (e⁻¹)_bn = ε_abc e^j_c` in all 27 components. Contracting with the curl gives `det e (ε·T) = 2 ε^{abc} e^j_c ∂_a e^j_b`.

2. **Dressed odd term.** At first order a coin rotation leaves `e' = R(−ϑ)e` fixed, so a density of `e'` is blind. Under the 24 proper cubic rotations `V ⊗ Λ²V` has one invariant and under the 48 it has none, so the odd member is `c₅ det e' (ε·T[e'])`.

3. **Twist equation.** `w ℓ²` with `ℓ = (w̄/w)^β` has logarithmic gradient `(1−2β)∇u`. At first order `∂_a(w adj(e')_am) = w̄[∂_m(u+2λ) − (curl ρ)_m]`, and `div curl ρ = 0`. A body, whose flux of `∇u` is the enclosed source, therefore leaves no smooth `ρ` when `β = 1`.

4. **No twist.** In normal coordinates the `so(3)` invariants of `V`, `Sym³V` and `V ⊗ Sym²V` are empty, so there is no odd blind density at one or three derivatives. The five-derivative block has one invariant. On the stated polynomial jet, `C^{ij}R_{ij} = 6412057/15876000` and `ε ∂u Ric Hess u = −16/35`, and both flip under `x → −x`. Normal coordinates and `Weyl = 0` stay assumed.

## Verdict

The odd dressed density survives blindness, and its twist equation excludes a body at `β = 1`. Without the twist the first odd densities have five derivatives.

`HIT: confirmed`.
