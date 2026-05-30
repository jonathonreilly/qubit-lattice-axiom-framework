# Flavor — the loop preserves block-count; lightness selects Q=2/3

**Date:** 2026-05-30
**Claim type:** bridge-gap attack move 4 / native mechanism (a LEAN, not a
forcing). Imports nothing.
**Runner:** `scripts/flavor_loop_preserves_block_count_2026_05_30.py` (+ cache).
Answers the move-3 open question: does the dynamics preserve or collapse the
covariant block-count measure?

## The question
Move 3: the covariant matrix-field action `Tr(M²)` realizes the **block-count**
measure → Q=2/3. But the fermion dynamics (3 computations this session) drives the
uniform condensate, `b→0`, Q=1/3. Does the loop **preserve** block-count (2/3) or
**collapse** it (1/3)?

## Answer — two separate effects, and lightness picks 2/3
**(A) The measure (quadratic / polarization) is PRESERVED.** The one-loop
correction in channel `X` is the bubble `Π_X = Tr[G₀ X G₀ X]`, `G₀` = free
generation propagator. At free level the three corners are **degenerate**
(`G₀ = c·I₃`), so
```
Π_X = c² Tr(X²)   ⟹   Π_I : Π_{J−I} = 3 : 6 = 1 : 2 = the bare HS ratio.
```
The loop has the **same channel ratio** as the bare `Tr(M²)` measure, so
`K_X^eff ∝ Tr(X²)` ⟹ `r^eff = 1/2` ⟹ **Q=2/3, RG-stable for any coupling** (while
`G₀` stays near-degenerate). The block-count lean **survives** the dynamics at the
measure level.

**(B) The collapse to 1/3 is a SEPARATE effect — the VEV/tadpole — and it is
suppressed for light fermions.** The loop's *linear* term drives the uniform
condensate `a_VEV` (with `b_VEV→0`). The physical operator is
`M = a_VEV·I + δM` (block-count fluctuations). Its √-mass spectrum:
- **heavy** (large `a_VEV`): `M ≈ a_VEV·I` → nearly degenerate → Q ≈ 1/3
- **light** (small `a_VEV`): `M ≈ δM` (fluctuation-dominated) → block-count → Q ≈ 2/3

(Verified: with a fixed block-count fluctuation `b/a_f=1/√2`, Q rises 0.347 → 0.417
→ 0.565 → **0.667** as the uniform VEV `v` shrinks 4 → 1 → 0.2 → 0.)

Charged leptons are **light** (near-critical, small uniform VEV) → fluctuation-
dominated → the covariant block-count measure sets the spectrum → **Q ≈ 2/3**.
Heavier sectors (up quarks) are more VEV-dominated — consistent with their weaker
Koide adherence.

## Honest caveats
1. The VEV-vs-fluctuation **crossover is qualitative** here; the quantitative
   threshold needs the actual VEV and fluctuation scales from the `g_bare=1` matter
   action (open).
2. Block-count is the **expected/typical** measure, not a per-operator forcing.
3. **One-loop**, valid while `G₀` stays near-degenerate.

## Net
A genuine, coherent native mechanism **linking the lightness of the charged
leptons to their Koide-perfection (Q=2/3)**: the covariant block-count measure is
RG-stable (the loop preserves it because the free generations are degenerate), and
for light (small-VEV) fermions the block-count *fluctuations* — not the uniform VEV
— govern the spectrum, giving Q→2/3. The move-3 lean survives the dynamics. The one
open quantitative piece is the VEV/fluctuation scale ratio from the matter action.
No false closure; Q=2/3 is a native lean, now dynamically stable and tied to lepton
lightness.
