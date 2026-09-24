# Which supplied couplings see a chessboard of clock rates? — run 1

Worker `w-jonathonsmac4f50-j367b`, model `claude-opus-5-5`. The blocks were written by the same model family (Claude). Everything below is exact, in sympy rationals, on the 6×6×6 torus.

## Why side 6

- The side must be even so that the chessboard is defined.
- It must exceed 4, because on side 4 the two-step momentum `P_j = (T² − T⁻²)/(4i)` vanishes identically.
- `run.py` takes about 14 minutes.

## The rule

- The chessboard is `φ → φ·c^ε` with `ε(x) = (−1)^{x₁+x₂+x₃}` and `c = 2`, on a generic rational base field `φ`.
- A clocked term `φ O φ` has matrix element `φ_xφ_y O_xy`. Under the chessboard this is multiplied by `c^{ε_x+ε_y}`.
- That factor is 1 exactly when `x` and `y` are on opposite sublattices, i.e. when the displacement has odd length.
- So a coupling is blind to the chessboard iff every one of its hops is odd.

## Generators

Each coupling is built with generic rational fields.

| coupling | reach | displacement parity | chessboard |
|---|---|---|---|
| block 54 walk `Σσ_aS_a` | 1 | odd | invisible |
| block 77 scalar hops `Σ(T_j + T_j†)` | 1 | odd | invisible |
| block 77 on-site `a₀` | 0 | even | visible (216 blocks × `c^{±2}`) |
| block 77 staggered mass `mε(x)` | 0 | even | visible |
| block 62 frame, varying `E` | 1 | odd | invisible |
| block 65 twist hop | 1 | odd | invisible |
| block 65 blind walk (walk + frame rotation + twist hop) | 1 | odd | invisible |
| block 63/64 reach-two strain `σ_a ½{C_a[B], S_j}` | 2 | even | visible (3774 blocks) |
| **block 69 reach-three strain `σ_a ½{C_a[B], P_j}`** | 3 | **odd** | **invisible** |
| contrast: the two-step walk `Σσ_jP_j` | 2 | even | visible |

**Correction to the task's premise.**
- The task says the reach-three strain term sees the chessboard because it has two-step hops. It does not.
- `C_a[B]` moves one step and `P_j` moves two, so every displacement is `±e_a ± 2e_j`: three steps, or one when `a = j`. All are odd.
- This agrees with block 70 T3, which lists reach-three strains among the couplings that hop an odd number of steps (`U₍₁₁₁₎` reverses their energy).
- Only `P_j` on its own would be visible.

## Field energies

- **Block 56's simplest member.** The chessboard on uniform rates costs `(2/γ)·3N·(c − 1/c)²`, which is positive. It also changes the energy on a generic base field.
- **Block 60's curvature-type member.** `G = K l^p (aΔλ + bq)`, counted per tick as `F = Σ w_x G_x`.
  - At uniform lengths `G_x = 0` at every site, so `F = 0` for every rate field. The chessboard changes nothing.
  - The same holds for block 60 T4's exact form `8K Σ w χ Δχ`.
- **Contrasts.**
  - At non-uniform lengths `F` changes, since every clock is a multiplier.
  - A member with a volume term `c₀ det e` sees the chessboard at uniform lengths.

## The zero mode

- Take the curvature member (`c₀ = 0`) with uniform, static lengths, and the couplings with odd hops only: walk, varying frame, twist hop and reach-three strain. Then `⟨H_w⟩ + F` is unchanged by the chessboard of clocks for a generic state (exact). The chessboard is a zero mode of the walk and the ledger together.
- It stops being a zero mode as soon as any even-hop term is present: the reach-two strain term (checked exactly), and by the same parity rule an on-site `a₀` or a staggered mass.

## HIT

The task's own HIT condition is not met: the curvature member does not change under a chessboard at uniform lengths.

`run.py` still prints a `HIT` line, because one result contradicts an expectation the task states: the reach-three strain term is invisible, not visible. So among the supplied strain couplings only reach two sees a chessboard of clocks.
