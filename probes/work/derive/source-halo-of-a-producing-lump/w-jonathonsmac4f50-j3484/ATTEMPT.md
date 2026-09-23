# source-halo-of-a-producing-lump, attempt a3: production lives on surface defects

**Provenance.** Written by Claude Opus 5.5 (`claude-opus-5-5`), worker `w-jonathonsmac4f50-j3484`, task
`J:derive:source-halo-of-a-producing-lump:a3`. There were no prior attempts at claim time. Blocks 39–41 were
supervisor-run in the same model family. The half-space census law used in (a) is the same derivation as my own facet
theorem in `J:derive:moving-jammed-clusters:a2` (#8680), re-stated here for irrational normals.

## 1. What is claimed

**Setting** (blocks 39–41, supplied and not adopted): the neutral scale `c₀ = 6/T`, with `T = p + q + 4r`. A lump is a set
of held records with agreeing contents. An empty site forms at rate `zZ_x`, and `Q = z Σ_{empty x touching the lump} (Z_x − 6)`.

**(a) The production excess.**
- **The formula.** An empty site touching `k` agreeing records has `Z − 6 = 6δ_k`, with **`δ_k = 6^{k−1}A_k/T^k − 1`** and
  `A_k = p^k + q^k + 4r^k`. So **`Q = 6z Σ_k n_k δ_k`** over the census `n_k` of touching sites.
- **One record contributes nothing.** `δ₁ = 0` identically, because every row of `W` sums to 6 at `c₀`.
- **Enumerated shapes:**

| lump | `Q` |
|---|---|
| cube (every touching site has `k = 1`) | `0` exactly |
| pit (a face record removed) | `6zδ₅` |
| adatom on a face | `24zδ₂` |
| step along a face | `6zδ₂` per unit length |
| lattice ball of radius `R` | a **surface** quantity; see below |
| porous cube (each site recorded with probability `f`) | proportional to the record count; see below |

  The given values reproduce: at `(3,1,2)`, `1 + δ₂ = 13/12` and `1 + δ₃ = 5/4`; at `(12,1,2)`, `46/21` and `2348/343`.
- **The ball.**
  - Its touching sites have `k ≤ 3`.
  - Per unit area of a surface with sorted `|normal|` `(n₁, n₂, n₃)`, the touching sites with `k = 1, 2, 3` have densities
    `n₁ − n₂`, `n₂ − n₃` and `n₃`.
  - Hence `Q/(zR²) → 6(δ₂I₂ + δ₃I₃)`, with `I₂ = ∫(n₂ − n₃)dΩ = 3.129928` and `I₃ = ∫n₃ dΩ = 2.637293`. That is `5.52` at
    `(3,1,2)`.
  - The censuses reach 5.41 at `R = 60`, 2% short and still approaching. `Q/(record count)` falls like `1/R`.
- **The porous cube.** Its holes are production sites, so
  `E[Q]/N → 6z((1−f)/f) Σ_{k≥2} C(6,k) f^k(1−f)^{6−k} δ_k`.

**(b) The halo.** Block 41's exact equation `d⟨n⟩/dt = κΔ⟨n⟩ + j` gives the stationary excess `u = (1/κ)Σ_y G(x − y)q_y`.
- **Far field.** `Q/(4πκ|x|) + d·x/(4πκ|x|³) + O(|x|⁻³)`, where `d = Σ_y q_y y` is the dipole of the production excess.
- **A cube has `Q = 0`.** Its halo starts at the dipole or higher: **a perfect cube draws no monopole halo.**

**(c) Disagreeing contents.**
- **Mean.** Next to `k` records of independent uniform contents, `E[Z] = 6`.
- **Variance.** `Var Z = (6/T)^{2k} Σ_{a,b}((Ω²)_{ab}/6)^k − 36`.
  - It is 0 for `k = 1`, so a cube with any contents has `Q = 0` exactly.
  - It is positive for `k ≥ 2`: `1/12` and `1/4` for `k = 2, 3` at `(3,1,2)`.
- **Sinks.** Disagreeing neighbours can make `Z < 6`: two opposite contents give `Z = 11/2` at `(3,1,2)`. So `Q` can have
  either sign.

**(d) When `Q` is proportional to the record count.** `Q = 6zΣ_{k≥2} n_k δ_k` is proportional to the record count only if
the census of touching sites with `k ≥ 2` grows linearly in the record count.
- That fails for compact lumps: cubes give 0, balls give `R²`.
- It holds for porous lumps at a fixed filling, where interior holes produce.

**Condition:** a halo strength proportional to the record count needs a lump whose interior is itself a production surface.

## 2. Steps

1. **PROVED / CHECKED (A1).** For aligned contents, `Z = Σ_a Π_y c₀ω(a, +z) = c₀^k A_k`. At `c₀ = 6/T`,
   `Z − 6 = 6(6^{k−1}A_k/T^k − 1)`, and `A₁ = T` gives `δ₁ = 0`. The given numbers are checked with sympy.

2. **CHECKED (A2).** Enumerated censuses of cubes of side 3–6, with a pit, an adatom and a one-high half-face step. The step
   has exactly `L` sites with `k = 2`.

3. **PROVED (density law) / CHECKED (censuses) / NUMERICAL (the integrals) (A3).**
   - **The law.** Take the half-space `{n·x ≤ 0}` with a unit normal. An outside site at height `h = n·t ∈ (0, n₁]` touches
     `k = #{i : n_i ≥ h}` records, and sites are spread uniformly in `h`. Integrating the per-area densities over the
     sphere of radius `R` gives the limit.
   - **The integrals.** `I₂` and `I₃` are computed by quadrature (relative `10⁻⁹`).
   - **The censuses.** They are exact integer counts for `R ≤ 60`.

4. **PROVED / CHECKED (A4).** By linearity, `E[Q] = 6zΣ_x P(x empty)E[δ_{k_x}]`, with `k_x ~ Bin(m_x, f)`. This matches all
   256 configurations of a `2³` porous cube at `f = 1/3`, and the bulk limit is approached like `1/L`.

5. **PROVED / CHECKED (C1).** The contents are independent, so `E[ZZ']` factorizes through `E_s[ω(a,s)ω(b,s)] = (Ω²)_{ab}/6`.
   The case `k = 2` is checked against all 36 content pairs.

6. **PROVED, given the ASSUMED far form of `G` (B1).** A Taylor expansion of `G(x − y)`, checked with sympy. The dilute-limit
   halo equation is block 41's T5; the held lump's no-entry boundary is neglected in the dilute limit.

## 3. Where the route stops

- **Dilute limit only.** The halo is taken in the dilute limit, where the held lump's exclusion boundary is neglected. Near a
  large lump the no-entry condition changes the near field; the far monopole of a finite lump is unaffected at leading
  order.
- **Two constants are not closed.** The ball's constant rests on two sphere integrals computed numerically. Closed forms were
  not sought.
- **A second lump in the halo is not treated.**

## 4. What would finish it

1. **Closed forms** for `I₂` and `I₃`.
2. **The near field** of a large lump with the exclusion boundary. This is a Dirichlet/Neumann problem for the lattice
   Laplacian.
3. **A second lump.** Its production responds to the first's halo only through its own surface census, so two cubes still
   do not produce.

## 5. Running it

```
python3 probes/work/derive/source-halo-of-a-producing-lump/w-jonathonsmac4f50-j3484/check.py
```

It needs `numpy`, `scipy` and `sympy`. It runs 6 checks in about 15 seconds.
