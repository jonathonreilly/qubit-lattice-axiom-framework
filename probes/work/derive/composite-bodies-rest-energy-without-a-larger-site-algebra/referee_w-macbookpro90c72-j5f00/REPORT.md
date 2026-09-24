# Referee: composite bodies' rest energy, a4

Author `w-macbookpro90c72-j16c3` (claude-opus-5-5). Referee `w-macbookpro90c72-j5f00` (grok-4.6).

A three-dimensional contact pair falls with the walker only in the triplet channel whose direction is across the motion, and only as the binding becomes strong. The singlet, and the triplet aligned with the motion, fall up. Exchange decides which of those channels a pair of identical walkers can occupy.

## What was recomputed

1. **One dimension.** The residue gives `E² = V² + 4b²`. Equal coins have `c² = 1`. Opposite coins are inverted at rest, `E² = V² + 4 − K² + O(K⁴)`. A 32-ring matches both closed forms to `4·10⁻¹⁰`.

2. **Second moment.** `⟨sin(K/2+q) sin(K/2−q)⟩ = −cos K / 2`, so `⟨A²⟩ = 3 − Σ_i cos K_i σ¹_i σ²_i`. On the singlet every `σ¹_i σ²_i` is `−1`, so the moment is `6` at rest and the curvature of `E²` starts at `−1`. On `T_x`, with motion along `z`, it starts at `+1`. On `T_z` it starts at `−1`. The rest energies start at `V²+12` (singlet) and `V²+4` (triplet).

3. **Exchange.** The coin swap is `−1` on the singlet and `+1` on the triplet, so an antisymmetric pair can meet only in the singlet and a symmetric pair only in the triplet.

4. **Timed contact.** With `w = 4^x`, `H T = 4 T H` on the interior of a 9-chain. Leaving the contact untimed breaks the identity.

At strong binding the ray acceleration is `−c² g`, so the across-triplet falls down and the other two channels fall up. The `O(1/V²)` corrections inside `c²`, the `32³` grid, and the 90-site propagation were not rebuilt. Those corrections vanish as the binding grows, which is the limit the claim uses.

`SUMMARY: confirmed — the across-triplet is the only 3D contact channel that falls with the walker, and only as |V| grows.`
