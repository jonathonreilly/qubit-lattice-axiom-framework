# The conservation defect of the walk's frame response (block 62 W3), mapped — run 1

Worker `w-jonathonsmac4f50-jb426`, model `claude-opus-5-5`. Blocks 62 and 63 were written by the same model family (Claude). The derivation `a-bond-placed-stress-for-the-walk` had same-family J attempts, which were not read.

## Setup

- The walk is `H = Σσ_aS_a` in the identity frame, on L³ tori.
- The states are stationary superpositions of positive-branch plane waves of equal energy.
- The frame response is `Θ_a^j = Re ψ†σ_a(S_jψ)`, and `Θ_(aj)` is its symmetric part.
- The **relative defect** is `max_x |Σ_j D_jΘ_(aj)| / max_x |oscillating part of Θ_(aj)|`, as in block 62 W3.

## Exact structure (two waves)

**The cross amplitude.** With `s_i = sin k_i`, `M_a = u₁†σ_a u₂`, `q = k₂ − k₁` and `K = (k₁ + k₂)/2`, the cross term of `Θ_(aj)` is `Re[C_(aj) e^{iq·x}]`, where

`C_(aj) = ½ c₁*c₂ [M_a(s₁+s₂)_j + M_j(s₁+s₂)_a]`.

**The identity.** `Σ_j (s₂ − s₁)_j C_(aj) = 0` for every equal-energy pair. The proof has two parts:
- `u₁†(σ·s₂ − σ·s₁)u₂ = (E − E)u₁†u₂ = 0`;
- `(s₂ − s₁)·(s₁ + s₂) = E² − E² = 0`.

This is also checked in 50-digit arithmetic at 20 random pairs, where it is below `10⁻⁴⁰`.

**The defect.** The symmetric site difference has symbol `sin q_j = ρ_j (s₂ − s₁)_j`, with `ρ_j = cos(q_j/2)/cos K_j`. So the divergence is `Σ_j (ρ_j − ρ̄)(s₂ − s₁)_j C_(aj)`. It vanishes iff `sin q` lies in the null space of `C`. Generically (`C` of rank 2) that happens iff `ρ_j` is equal on the support of `q`.

## (i) The third-power law and its dependence on the pair

**Block 62 W3's pair**, `(1,2,3) + (3,1,2)`, with the symmetric site difference:

| L | lattice | symbol formula | × (L/12)³ |
|---|---|---|---|
| 12 | 0.1733 | 0.1773 | 0.173 |
| 24 | 0.02233 | 0.02218 | 0.179 |
| 32 | 0.00937 | 0.00937 | 0.178 |
| 48 | 0.00278 | 0.00278 | 0.178 |
| 64 | 0.00117 | 0.00117 | 0.178 |

The fitted power of `1/L` is 3.003. The bond current of `π_j` is conserved to `10⁻¹⁴` in every case.

**Dependence on the pair**, at L = 24:

| pair | relation | defect | spread of ρ on supp(q) |
|---|---|---|---|
| (1,2,3)+(3,1,2) | cyclic rotation | 2.2e-2 | 0.18 |
| (1,2,3)+(2,3,1) | cyclic rotation | 2.2e-2 | 0.18 |
| (1,2,4)+(4,1,2) | cyclic rotation | 6.4e-2 | 0.29 |
| (1,2,3)+(1,−2,−3) | half turn about x | 6.2e-2 | 0.16 |
| (1,2,3)+(−2,1,3) | quarter turn about z | 1.8e-2 | 0.14 |
| (1,2,3)+(−3,−1,−2) | rotation × inversion | 6.8e-2 | 0.13 |
| (1,2,3)+(2,1,3) | mirror x↔y | 1e-14 | 0 |
| (1,2,3)+(3,2,1) | mirror x↔z | 1e-14 | 0 |
| (1,2,3)+(−1,2,3) | mirror x → −x | 6e-15 | 0 |
| (2,1,1)+(1,2,1), (1,1,2)+(1,2,1) | mirrors | 1e-14 | 0 |
| (1,2,0)+(2,1,0) | in a coordinate plane, mirror | 6e-15 | 0 |
| **(1,3,0)+(−3,1,0)** | **in a coordinate plane, quarter turn** | **9.8e-2** | 0.22 |

**The characterisation (exact).** The defect is zero if and only if `ρ_j = cos(q_j/2)/cos K_j` is the same on every component where `q_j ≠ 0`.
- Every pair related by a mirror of the cube satisfies this. For a coordinate plane, `q` has one component. For a diagonal plane, the two components have equal `cos(q/2)` and equal `cos K`.
- Rotations generally do not, and neither does a rotation composed with inversion.

**The HIT.** The defect does **not** vanish in coordinate planes in general. An in-plane pair vanishes only when it is a mirror pair. The task's parenthetical said it vanishes in coordinate planes.

**Three waves.** At L = 24 and 48:
- the cyclic triple `(1,2,3)+(3,1,2)+(2,3,1)` gives 0.195·(12/L)³;
- the mirror triple `(1,2,3)+(2,1,3)+(−1,2,3)` gives 0.052·(12/L)³, a nonzero cross term, because `(2,1,3)` and `(−1,2,3)` are related by a rotation, not a mirror.

## (ii) Local recombinations

Relative defect for the W3 pair, at L = 24 and L = 48:

| recombination | L = 24 | L = 48 |
|---|---|---|
| site values, symmetric difference | 2.2e-2 | 2.8e-3 |
| site values, forward difference | 0.15 | 3.9e-2 |
| site values, backward difference | 0.17 | 4.1e-2 |
| bond-end average (a = j and a ≠ j), backward difference | 2.2e-2 | 2.8e-3 |
| face average for a ≠ j (bond average for a = j), backward difference | 8.7e-2 | 2.2e-2 |

**None is divergence-free to rounding, and no fixed local recombination can be.**
- A recombination's symbol is a function `F(q)`.
- The null vector of `C` is `(s₂ − s₁)_j = 2cos K_j sin(q_j/2)`, which depends on `K`.
- Two equal-energy pairs with the same `q` but different `K` would need different `F`.
- The exactly conserved bond current of `π_j` is not a recombination of `Θ`: its cross symbol carries phases `e^{±ik_a}` of the individual waves.

## (iii) The antisymmetric part

- Its oscillating amplitude relative to the symmetric part is 0.24–0.26 for the W3 pair, 0.10 for the x↔y mirror and 0.20 for the x → −x mirror. It does not shrink with L.
- The unsymmetrised response has relative divergence 2.1e-2 and 2.7e-3 for the W3 pair (about the same as the symmetric part) and about `10⁻¹⁴` for the mirror pairs.
