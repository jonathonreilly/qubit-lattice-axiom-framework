# Block 86's walls with the scalar hop through the same bonds — run 1

Worker `w-jonathonsmac4f50-jf900`, model `claude-opus-5-5`. Blocks 77, 84, 86 and 89 were written by the same model family (Claude).

## Model

- **One-axis operators:** `h = (1/2i)(tT − T†t)` (the walk's hop) and `g = tT + T†t` (the scalar hop; its symbol is `2 cos k` at `t = 1`).
- **Bonds:** `t_x = 1 + δ s_x (−1)^x` (linear) or `exp(δ s_x (−1)^x)` (log rates, block 89).
- **Walls:** `s = ±1` on the two halves of an axis, giving a weak-weak and a strong-strong wall on each walled axis.
- **Generator:** `H = Σ_j σ_j ⊗ h_j + a Σ_j g_j ⊗ 1`.

## Exact results (sympy, ring of four with rational amplitudes)

- `ε h ε = −h` and `ε g ε = −g`: both hop one step. So the staggered sign `ε = ε_x ε_y ε_z` anticommutes with every term, and the spectrum stays symmetric for every `a`.
- The one-axis `h` with two walls has exactly two zero modes, one on each sublattice.
- The 16 point zero modes of the three-axis walk are products (block 86 T4). Their chirality is the product of the three sublattice signs, which gives **8 with `ε = +1` and 8 with `ε = −1`: index 0**. Nothing protects them once `a ≠ 0`.

## Dense spectra (floating point, 8³ and 12³)

**At `a = 0` block 86 is reproduced exactly** in every case, linear and log:
- least `|E|` = bulk `√3 m`, sheet `√2 m`, line `m`, point 0, with `m = δ` (linear) or `sinh δ` (log);
- 16 zero modes at the point and none elsewhere.

**At `a = 0.1` and `0.25`:**
- All zero modes are lifted (none in any configuration).
- At the point, least `|E|` is 0.136 and 0.039 (L = 8, linear, δ = 0.3), and 0.080 and 0.025 at L = 12.
- The bulk least `|E|` falls roughly linearly in `a`, by 3.6–3.9 per unit `a`. It reaches the lattice's resolution near `a ≈ δ/2`: at δ = 0.3 it drops below half the bulk mass at `a = 0.07` and to 0.03 by `a = 0.14`; at δ = 0.5 it drops below half at `a = 0.12`. The log parametrisation behaves the same.
- This is the scalar hop's species offsets reaching the alternation mass.

**What follows for sheets and lines.** Past that point the least `|E|` values of the sheet, line and point configurations (for example 0.125, 0.097 and 0.080 at L = 12, δ = 0.3, a = 0.1) are finite-size numbers of a gapless spectrum. They are not masses of bound bands, so they cannot be compared with block 86's separable values.

The complete per-configuration table is in the log: `logs/probes/C:the-sheet-and-line-modes-with-the-scalar-hop:a1/w-jonathonsmac4f50-jf900__a4443716__20260925T012949Z.txt`.

## Summary

- The scalar hop keeps the chiral symmetry.
- It lifts the three-wall zero modes, because their index is 0.
- It closes the bulk gap near `a ≈ δ/2`.

The sheet, line and point hierarchy of block 86 survives only for `a` well below `δ/2`, where the masses shift down roughly linearly in `a`. The task stated no expectation, so there is no HIT.
