# Two held sources under light-cone formation — attempt 2

Worker `w-jonathonsmac4f50-j7576`, model `claude-opus-5-5`. Task `J:derive:the-two-source-interaction-under-light-cone-formation:a2`.

**Provenance.** Blocks 19, 20 and 90 to 92 were written by the same model family (Claude Opus). They are open and unrefereed, except block 20, which is closed and archived. I restate what I use. The referee should come from another family. There were no prior attempts at claim time.

**Scope.** This works within block 90's supplied light-cone clause, which block 92's corrigendum marks as excluded by the axioms memo as written; every statement is conditional on it. The sources are held sources in block 91's sense. Nothing is adopted. The parked statistical postulate is not touched. No gravitational claim is made.

**Checks.** The exact checks run on the doubled ring, the one-dimensional light-cone clause, with contents `±1` and weights `t = e^β`, `u_i = e^{βh_i}`, `v = e^{βε}` as symbols. The sphere-menu statements use the same algebra together with rotation invariance.

## 1. The exact statement attempted

**Setting.** Sources `h₁` at `x₁` and `h₂` at `x₂`, with a uniform field `ε`. A record at `(t+1, x)` forms with weight `exp(β s′·(h_x(s) + ε + h₁[x = x₁] + h₂[x = x₂]))`, where `h_x(s)` is the sum of the records below it (block 91).

**(a) Exact at second order.**
- The chain is reversible. Its stationary law is the level marginal of
  `μ ∝ exp(β Σ_edges s·s′ + βε·Σ s + βh₁·σ(x₁) + βh₂·σ(x₂))`
  on the doubled graph, where `σ(x)` is the sum of the two records at `x`, one on each level.
- At zero uniform field:

  `log Z(h₁, h₂) − log Z(h₁, 0) − log Z(0, h₂) + log Z(0, 0) = 2β (h₁·h₂) R(x₁ − x₂) + O(|h|⁴)`,

  where `R(x) = N⁻¹ Σ_k e^{ik·x} R̂(k)`, per component, is block 91's response kernel.
- **The quantity of the formation law itself** that measures the coupling is the **mutual alignment** of the records each pinned site holds:

  `∂⟨σ(x₁)⟩/∂h₂ = ∂⟨σ(x₂)⟩/∂h₁ = 2R(x₁ − x₂)` (times the identity).

  Source 2 turns the records that source 1 holds, by exactly as much as source 1 turns source 2's: action equals reaction. The cross term of the normalisation is `β` times this alignment. It is not a free energy that must be read thermodynamically.

**(b) Separation.**
- In wave vectors the coupling is `2β R̂(k)`, with `R̂(k)E(k)` between block 92's zero-field floor and 1 for every `k ≠ 0`: the inverse lattice Laplacian within a factor.
- In real space, exactly in every finite volume:

  `R(0) − R(r) = N⁻¹ Σ_{k≠0} (1 − cos k·r) R̂(k)`

  lies between block 92's floor applied to the same sum and `Γ_L(r) = N⁻¹ Σ_{k≠0} (1 − cos k·r)/E(k)`.
- The `k = 0` term, the long-range order, adds a constant that does not depend on the separation.

**(c) Sign.** For sources that are mirror images under a reflection of block 90's family (an odd number of steps apart along one axis), `⟨σ(x₁)·σ(x₂)⟩ ≥ 0`. So the cross term is non-negative for aligned sources: they raise the normalisation, and each turns the other's records toward itself. For other separations no sign is claimed.

## 2. Steps

### Step 1 — reversibility with two sources (PROVED; CHECKED 1.1, 1.2)
- **Detailed balance.** Block 91 T1's proof goes through unchanged: `π(s)P(s′|s) = exp(βA(s′, s) + βε·(Σs + Σs′) + βh₁·(s_{x₁} + s′_{x₁}) + βh₂·(s_{x₂} + s′_{x₂}))`, with `A` symmetric for a symmetric past.
- **Checked** for every pair of levels on the ring of 4, with `t, v, u₁, u₂` symbolic (1.1).
- **The marginal.** The level marginal of `μ` is `π` (1.2).

### Step 2 — the cross term and its meaning (PROVED; CHECKED 2.1–2.4)
- **Differentiating.** `∂² log Z/∂h₁^α ∂h₂^γ` at 0 is `β² Cov(σ^α(x₁), σ^γ(x₂))`.
  - At zero field the mean is 0, by the flip (two-valued menu) or by rotation invariance (sphere).
  - Rotation invariance gives `δ_{αγ}` for the sphere.
- **In terms of block 91's kernel.**
  - Block 91 T2 gives `R̂(k) = 2β N⁻¹ ⟨|Ŝ_+(k)|²⟩` with `S_+ = σ/2`.
  - Translation invariance gives `R(r) = 2β ⟨S_+(0) S_+(r)⟩ = (β/2)⟨σ(0) σ(r)⟩`.
  - Hence the cross term is `β² · (2/β) R = 2βR` (2.1, 2.2).
- **The next order.** The third-order cross terms vanish: by the flip on the ring, and for the sphere because no rotation-invariant cubic is built from two vectors. The statement therefore holds to `O(|h|⁴)` (2.3).
- **The meaning.** `∂⟨σ(x₁)⟩/∂h₂ = β Cov(σ(x₁), σ(x₂)) = 2R`, and the same with 1 and 2 exchanged. So `∂² log Z/∂h₁∂h₂ = β ∂⟨σ(x₁)⟩/∂h₂` (2.4).
- **Why this is a formation-law quantity.** `⟨σ(x₁)⟩` is the stationary mean direction of the records formed at `x₁`, on both levels. It can be read off the formation law with no thermodynamic interpretation.

### Step 3 — separation (PROVED from blocks 91 and 92)
- `R̂(k) ≥ 0` for every `k`: it is a variance.
- Block 91's upper side is `R̂ ≤ 1/E`. Block 92's zero-field floor is `R̂ ≥ ((1 − β_L/β)/3)²/(E + 2/(3βV))` for `k ≠ 0`, in 3+1, for `β > β_L`.
- Since `1 − cos k·r ≥ 0`, both bounds carry over term by term to `R(0) − R(r)`, in every finite volume.
- In infinite volume this is block 91's statement that `R(0) − R(x)` lies between `(m*²/P_b*) Γ_∞(x)` and `Γ_∞(x)`, now at zero field.

### Step 4 — sign (PROVED for mirror pairs; CHECKED instances 3.1, 3.2)
- **The reflection.** Block 90 T3 gives reflection positivity for the bilayer family, whose reflections fix no vertex. A reflection through a bond plane maps the two slabs at `x` to the two slabs at the mirror site `x′`, so `θσ(x) = σ(x′)`.
- **The inequality.** Reflection positivity gives `⟨F θF⟩ ≥ 0` with `F = σ^α(x)`, a function on one half. Hence `⟨σ(x)·σ(x′)⟩ ≥ 0`.
- **Instances.**
  - Ring of 4, sites one step apart: the correlation is a ratio of polynomials in `t` with non-negative coefficients (3.1).
  - Ring of 6, separations 1 and 3: the same, and the correlation falls with separation at `t = 2` (3.2).
  - The non-mirror separation 2 is reported in the output, not claimed.

## 3. Where the route stops

Nothing claimed fails. Not done:
- the sign for non-mirror pairs;
- the pointwise real-space shape of `R(r)` itself (only `R(0) − R(r)` is bracketed);
- movable sources, which a force between the sources would need;
- higher orders in `h`.

## 4. What would finish it

1. Sources that are themselves records formed by the rule. Then the cross term becomes the relative probability of the two source records' orientations: a pair weight `exp(2β h₁·h₂ R(r))` mediated by the formation law.
2. Block 91's open small-`k` limit of `R̂(k)E(k)`, which would give the coupling's strength at large separation.
3. A sign for every separation, for example through a correlation inequality for the sphere menu. Reflection positivity gives only the mirror pairs.
