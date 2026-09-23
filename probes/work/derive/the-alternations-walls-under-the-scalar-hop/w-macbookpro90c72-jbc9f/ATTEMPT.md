# J:derive:the-alternations-walls-under-the-scalar-hop:a2: the scalar hop ends separability and lifts the zero modes where three walls cross

**Provenance.**
- Worker `w-macbookpro90c72-jbc9f`, model `claude-opus-5-5`, one session. Unit a2 (attempt 2 of 2); no prior attempt files exist on the branch.
- **Plan, formed after reading the setting:**
  - expand the square of the walk plus the scalar hop;
  - use the chessboard's anticommutation to reduce zero modes to one `64 × 64` block, with exact ranks;
  - use degenerate first-order perturbation theory on block 86's product zero modes;
  - compute floating-point least energies as a control.
- **Setting.** Read on their PR branches:
  - block 86 (#8660): T1–T4, the one-axis operator, the walls, the product zero modes;
  - block 84 (#8652) T4: the scalar hop through the same bond rates and its corner zeros at `δ = 2a`;
  - block 82 (#8628): the definition of the scalar hop through the same lengths, `aΣ_j(D_j + D_j†)`.
- Nothing is adopted and no gravitational claim is made.

## 1. The statement attempted

**Notation.**
- `D_jψ(x) = t_j(x_j)ψ(x + e_j)`, with `t = 1 + δ s(x)(−1)^x`. On the ring of four with two walls, `s = (+, +, −, −)`.
- `h_j = (D_j − D_j†)/(2i)` and `c_j = D_j + D_j†`.
- The walk with the scalar hop is `H_a = Σ_j σ_j ⊗ h_j + aΣ_j c_j`.

**(a) Separability fails (PROVED; CHECKED S1).**
- **The square, exactly:**

  `H_a² = Σ_j h_j² + a²(Σ_j c_j)² + aΣ_j σ_j{h_j, c_j} + 2aΣ_{j≠l} σ_j h_j c_l`,

  with `{h_j, c_j} = (D_j² − D_j†²)/i ≠ 0`.
- **Why the cross terms stay.** The scalar hop commutes with the coin, so the terms `2aσ_j h_j c_l` for `j ≠ l` do not cancel in pairs as the `σ_jσ_l` terms of block 86 T1 do.
- **The mixed part.** The part of `H_a²` acting on two axes at once is nonzero, so `H_a²` is not a sum of one-axis operators.
- **Checked** in exact integer arithmetic on the `128`-dimensional space, with walls on all axes and with walls on two.

**(b) The zero modes and the masses (PROVED; CHECKED S2–S4).**
- **Symmetry.** The chessboard `(−1)^{x+y+z}` anticommutes with every one-step hop, `h_j` and `c_j` alike. So the spectrum is symmetric and `H_a` is off-diagonal between the sublattices. The nullity is `2(64 − rank Q)`, computed by exact rank over `ℚ(i)`.
- **The sixteen point zero modes are lifted.**
  - On the ring of four the one-axis wall modes are `(t₁, 0, t₀, 0)` and `(0, 1, 0, 1)`, and `c` maps the first onto a multiple of the second.
  - At first order in `a`, the sixteen products therefore split into `a(±μ_x ± μ_y ± μ_z)`, each twice (coin), with

    `μ = 2(1 − δ²)/√(1 + δ²)`,  i.e. `μ² = 4(1 − δ²)²/(1 + δ²)` exactly.

  - For equal `δ` the values are `±aμ` (12 states) and `±3aμ` (4 states), never zero. The float control at `a = 10⁻⁴` confirms both.
- **Exact nullities on `4³`** (walls across 0, 1, 2, 3 axes), with least `|E|` in floating point:

  | `δ` | `a` | bulk | sheet | line | point |
  |---|---|---|---|---|---|
  | 3/10 | 0 | 0 / 0.5196 | 0 / 0.4243 | 0 / 0.3000 | **16** / 0 |
  | 3/10 | 1/10 | 0 / 0.1568 | 0 / 0.0910 | 0 / 0.0076 | 0 / 0.1732 |
  | 3/10 | 1/4 | 0 / 0.1583 | 0 / 0.1151 | 0 / 0.0651 | 0 / 0.1167 |
  | 1/2 | 0 | 0 / 0.8660 | 0 / 0.7071 | 0 / 0.5000 | **16** / 0 |
  | 1/2 | 1/10 | 0 / 0.4888 | 0 / 0.3849 | 0 / 0.2487 | 0 / 0.1323 |
  | 1/2 | 1/4 | **4** / 0 | 0 / 0.0560 | 0 / 0.0709 | 0 / 0.2307 |

  - At `a = 0` this is block 86: `√3δ`, `√2δ`, `δ`, and 16 zero modes.
  - With the scalar hop the only zero modes left are the bulk's four at `δ = 2a` (block 84 T4's corner zeros).
  - The bulk value at `a = 1/10, δ = 3/10` is the corner value `√(4a² + 3δ²) − 4a = (√31 − 4)/10`.
- **The hierarchy is broken.** The ordering bulk > sheet > line > point no longer holds: at `a = 1/10, δ = 3/10` the line (`0.0076`) lies below the point (`0.1732`).

## 2. Steps

**S1: (a) (PROVED; CHECKED).**
- Expand `(Σσ_jh_j + aΣc_j)²`:
  - `(Σσ_jh_j)² = Σh_j²`, by block 86 T1;
  - `a²(Σc_j)²` stays as it is;
  - the cross term is `aΣ_{j,l}σ_j{h_j, c_l}`.
- For `j ≠ l`, `h_j` and `c_l` act on different axes and commute, so `{h_j, c_l} = 2h_jc_l`.
- For `j = l`, `{h, c} = [(D − D†)(D + D†) + (D + D†)(D − D†)]/(2i) = (D² − D†²)/i`.
- The mixed part `σ_x ⊗ h_x ⊗ c_y + σ_y ⊗ c_x ⊗ h_y` involves two different coin matrices and traceless one-axis factors, so it is nonzero.
- The exact check scales `H_a` to Gaussian integers, whose magnitudes stay below `2⁵⁰`.

**S2: the chiral block (PROVED).** `h_j` and `c_j` move one step, so `ε h_j ε = −h_j` and `ε c_j ε = −c_j`. On an even ring the one-step hops always change the sublattice.

**S3: first order (PROVED; CHECKED).**
1. `hψ = 0` means `t_xψ(x+1) = t_{x−1}ψ(x−1)`. On the ring of four with walls this gives `(t₁, 0, t₀, 0)` on the even sites and `(0, 1, 0, 1)` on the odd sites.
2. `c(t₁, 0, t₀, 0) = 2t₀t₁ (0, 1, 0, 1)`.
3. The normalised matrix element is `μ` with `μ² = 2(2t₀t₁)²/(t₀² + t₁²) = 4(1 − δ²)²/(1 + δ²)`.
4. On the sixteen-dimensional null space of `H` (products; block 86 T4), `P A P = aΣ_j (0 μ; μ 0)_j`. Its eigenvalues are the tensor sums `±μ_x ± μ_y ± μ_z`.

**S4: exact nullities (CHECKED).** Exact ranks of the `64 × 64` block over `ℚ(i)` for all 24 cases. The float nullities agree.

## 3. The first failing step

- **Nothing fails** for the questions asked.
- **What is not proved:** the least `|E|` values at finite `a` are floating point (roots of high-degree factors), and the first-order formula is not continued to finite `a`.
- **Scope:** the results are for the ring of four. On longer rings `μ` depends on the decay of the wall modes, `(1 − δ)/(1 + δ)` per two sites.

## 4. What would finish it

1. `μ` on the ring of `L`, and its large-`L` limit, which needs the overlap of the two wall modes of one axis.
2. Whether any covariant choice keeps a protected zero mode at a triple wall crossing: the scalar hop breaks the product structure. One could ask for the index of `Q` restricted to a wall region.
3. Exact least energies as algebraic numbers, by exact characteristic polynomials of the symmetry-reduced blocks.
4. A referee from another model family.

## 5. Running it

```
python3 probes/work/derive/the-alternations-walls-under-the-scalar-hop/w-macbookpro90c72-jbc9f/check.py
```

The run takes about 12 s. It prints:
- S1 in exact integer arithmetic;
- S2 and S4 with exact ranks over `ℚ(i)`;
- S3 exact, with a float control;
- the least energies in labelled floating point;
- then the SUMMARY and HIT lines.

Standard mathematics used, none as authority:
- degenerate first-order perturbation theory;
- exact Gaussian elimination;
- chiral (sublattice) symmetry.
