*(Saved by the coordinator from the agent's final message.)*

# A41 report: does charged triplet matter, hopping through light's links, move like light?

Supplied model, finite diagnostics. Light's links are a fixed classical background (U → a number on each link), so this is a single-particle toy, not light's quantum vacuum. Units: t is the per-channel hop amplitude (each hop matrix has singular values t, t, 0). Lengths are in coarse-lattice spacings (2 fine grid spacings). In c13's normalization (unit total norm), t = 1/√6.

## 1. Question

Take the covariant charged-triplet hop through light's links (A34 c13: a 2-real-parameter family). Put it on two classical link backgrounds:
- (a) zero flux;
- (b) a uniform π flux in KS gauge (η_x = 1, η_y = (−1)^x, η_z = (−1)^(x+y)).

Build the Bloch bands (3 bands; 24 for the 2×2×2 KS cell) and scan the family. Then answer five questions:
- Are there zero-energy touchings? Are they linear and isotropic?
- How many cones are there, and with what slopes?
- Are there flat or heavy bands beside them?
- Is the spectrum symmetric about zero?
- Does light's π flux create cones that zero flux lacks?

## 2. Answer (graded)

**The family in closed form (EXACT; CHECKED against c13 to 9e-16).**
- The hop through link (x, x+e_a) is ψ†_x [u_{x,a} M^(a)] ψ_{x+e_a} + h.c., with M^(a) = α e₋^(a) e_aᵀ − ᾱ e_a e₋^(a)ᵀ.
  - α = t e^{iθ}, e₋^(a) = (e_b − i e_c)/√2, and (a, b, c) is cyclic.
- In the spin-1 basis about the hop axis, M^(a) has only two amplitudes: ⟨0|M|+1⟩ ∝ e^{−iθ} and ⟨−1|M|0⟩ ∝ e^{+iθ}. It lowers the matter's spin component along the hop by one, matching the link raising it by one.

**One real parameter matters (EXACT).**
- t only rescales energies.
- θ → θ + π is −H, the same as the momentum shift (π,π,π).
- θ → −θ is complex conjugation plus that shift.
- So θ ∈ [0, π/2] covers everything:
  - θ = 0 is the "dipole" hop, M ∝ S⁻.
  - θ = π/2 is the "quadrupole" hop, M ∝ {S⁻, S^a}; every Bloch block is then real symmetric.
- Each single-direction Bloch block h_a(k) has eigenvalues (0, ±√2 t) for every k and θ (EXACT).

**π flux reduces exactly (EXACT; CHECKED to 7e-15).**
- The 24-band KS-cell Hamiltonian is H24(k) ≅ 2·H6(k) ⊕ 2·(−H6(k)), with H6(k) = Σ_a σ_a ⊗ h_a(k).
- The minimal 2×2×1 cell (12 bands, c14's layout) is H6 ⊕ (−H6).
- The 2×2×2 cell is twice the minimal magnetic cell, so all 24 bands come in degenerate pairs.

**Negative energies and symmetry about zero.**
- **Negative energies (EXACT).** Tr M^(a) = 0, so Tr H(k) = 0 at every k in both backgrounds. Negative one-particle energies therefore exist wherever H(k) ≠ 0, for every member of the family. The empty matter vacuum is never the lowest state of the one-particle sector. This holds whether or not there is a touching, so it is stronger than A39's positivity lemma needs.
- **Symmetric as a whole (EXACT).** The bipartite sign (−1)^(x+y+z) gives spec H(k+(π,π,π)) = −spec H(k) in both backgrounds, so the spectrum taken over all k is symmetric about 0.
- **Symmetric at each k:**
  - π flux: always (EXACT).
  - zero flux: only at θ = 0, where H0 is imaginary antisymmetric (EXACT). Not at other θ (CHECKED).

**(a) Zero flux.**
- **θ = 0 (EXACT).** H0 = √2 t B(k)·S, with B = (cos k_z + sin k_y, cos k_x + sin k_z, cos k_y + sin k_x).
  - An exactly flat band sits at E = 0.
  - **8 spin-1 triple points** sit at E = 0, at k ∈ (π/4)·(odd)³. Their chiralities are 4 of + and 4 of −.
  - Each cone is linear but **not isotropic**: slope 2t along one body diagonal and t across it.
- **θ = π/2 (location EXACT, slopes CHECKED).**
  - **8 triple points** sit at E = 0, at k ∈ (π/4)·(odd)³ where H0 = 0. All three bands are linear there.
  - They are anisotropic: |slopes| range over 0.62–2.31 t.
  - The middle band also crosses E = 0 on surfaces that pass through them.
- **0 < θ < π/2 (CHECKED at 7 interior angles).**
  - There is no zero-energy touching: the refined minimum of the second-smallest |E| stays between 0.39 and 1.4 t.
  - The middle band crosses E = 0 on a surface.
  - Linear but anisotropic Weyl-type touchings sit at energies ±E ≠ 0:
    - θ = π/16: 24 lower-pair touchings, at E = −0.738 t (8), −0.499 t (12) and −0.390 t (4), with |slopes| 0.15–1.9 t;
    - θ = π/4: at least 21 at E = −√2 t, with |slopes| 1.0–1.41 t;
    - in both cases mirror images sit at +E.

**(b) π flux.**
- **θ = 0 (EXACT).** H6 = √2 t Σ N_ai(k) σ_a ⊗ S^i, where the rows of N are unit vectors.
  - The spectrum depends only on the signed singular values of N.
  - The bands come in Kramers pairs at every k.
  - Zero modes occur exactly on the **surface** cos k_x cos k_y cos k_z + sin k_x sin k_y sin k_z = 0. There, 4 of the 12 bands cross E = 0 with slope 2√2 t|∇det N|/3 normal to the surface (CHECKED to 6e-7) and 0 along it. The other bands sit at ±√6 t.
  - There are no point cones.
- **θ = π/2.**
  - **Symmetry (EXACT).** C = (σ_y K) ⊗ 1, with C² = −1, gives C H6 C⁻¹ = −H6.
  - **Isotropic cones (CHECKED).** There are **16 isotropic linear cones at E = 0** in H6's zone: the 8 points with each k_a ∈ {0, π}, and the 8 points (±π/2)³. That is 4 per magnetic Brillouin zone, each a point where 4 of the 12 bands meet.
    - The slope is 0.9428 t in all 300 directions tested. This equals 2√2/3 to 4 digits; I have not derived the closed form.
    - At the cones the other bands sit at |E| ≥ √6 t, and no flat band runs through them.
  - **Nodal lines (CHECKED).** Alongside the cones run **12 straight zero-energy nodal lines**: k_a free, k_b ∈ {0, π}, k_c = ±π/2, with (a, b, c) cyclic.
- **θ ≠ π/2 (CHECKED).**
  - The 16 cones are gapped. For example, the gap is 0.089 t at θ = 0.49π, so θ − π/2 acts like a mass.
  - The zero-energy set is a surface (det H6 changes sign at all 7 interior angles), not points.

**Comparison of (a) and (b) (CHECKED for the scanned angles; EXACT at θ = 0).**
- **The triplet hop already twists things without flux.** At θ = 0, zero flux already gives point cones at E = 0, as neutral vector matter does with the hop i S^a. These cones sit at odd multiples of π/4 and are 2:1 anisotropic. The link's −i under a quarter turn acts like a built-in momentum shift.
- **π flux at θ = 0 destroys the point cones**, replacing them with a zero-energy surface.
- **π flux creates isotropic cones only at θ = π/2.** Covariance does not single out that angle, and even there the cones come with zero-energy nodal lines.
- **Generic θ:** both backgrounds have zero-energy surfaces and no point cones at E = 0.

**Verdict (ARGUED).** Within this family and these two classical backgrounds, light-like motion (linear, isotropic, gapped elsewhere) is not obtained. The closest case is π flux at the single angle θ = π/2. It has exact isotropic cones, but they share E = 0 with nodal lines. Moving off that angle gaps the cones.

## 3. Derivation and checks

**Closed form (EXACT, by hand).**
- A quarter turn about the link multiplies its raising operator by −i (c13 (1)), so covariance needs R M^(a) Rᵀ = i M^(a).
- In the basis e₊, e₋, e_a, the only outer products that pick up i are e₋ e_aᵀ and e_a e₋ᵀ.
- The link-reversing half turns force the second coefficient to be −ᾱ.
- The three-fold turn (phase 1) generates M^(x) and M^(y) from M^(z).
- This gives a real 2-dimensional span, as c13 found. In d1 the closed form lies in c13's null space (residual 8.9e-16; c13 run by exec) and vice versa (3.1e-16).

**Blocks.**
- h_a(k) = √2 t [e^{iφ} v_a e_aᵀ + e^{−iφ} e_a v_aᵀ], with φ = θ + π/2 and v_a = n_a × e_a. Here n_z = (cos k_z, sin k_z, 0), and the others follow cyclically.
- At φ = π/2, h_a = √2 t n_a·S, so H0 = √2 t (Σ_a n_a)·S = √2 t B·S.

**Zero-flux nodes at θ = 0 (EXACT).**
- Each equation cos u = −sin w has the branches u = ±(w + π/2).
- Of the 8 sign choices, those with odd product give 2 points each, and the rest give none: 8 nodes in total.
- At each node the Jacobian is (1/√2) times a matrix with eigenvalues {2, −1, −1} up to sign. So the slopes are √2 × (√2, 1/√2, 1/√2) = (2, 1, 1) t.

**π-flux reduction (EXACT).**
- In true-displacement Bloch form, H24(k) = Σ_a P_a ⊗ h_a(k).
- The P_a are 8×8 signed shifts with {P_a, P_b} = 2δ_ab (exactly 0 deviation in d1) and Tr(P_x P_y P_z) = 0.
- So the cell carries 2 copies of each Clifford irrep, ±σ_a.

**π flux at θ = 0 (EXACT).**
- If all signed singular values λ_i ≠ 0, then (Λσ) × χ = 0 has only χ = 0. If λ₃ = 0, the kernel is 2-dimensional.
- To first order, both kernel states shift by the same amount, 2√2 t λ₁λ₂λ₃/(λ₁² + λ₂²).
- Σλ_i² = 3, because the rows of N are unit vectors.
- T = (iσ_y K) ⊗ e^{iπS_y}K commutes with H6 because the coefficients are real, and T² = −1.

| Script | What it checks | Result | Time, peak memory |
|---|---|---|---|
| `d1_family_and_theta0` | Span vs c13; reductions; θ = 0 in both backgrounds | (1) residuals 8.9e-16 and 3.1e-16; sv(M) = (1,1,0); Tr M = 0. (2) H24, H12 vs ±H6: 7.1e-15, 5.3e-15; spec H6(k+πe_a) = −spec H6(k) to 4e-15. (3) H0 = √2 B·S to 8.9e-16; middle band \|E\| ≤ 2.6e-15 on 36³; 8 nodes, singular-value slopes (2,1,1) at each; 300 directions at q = 1e-5 give outer bands 1.000–1.993 and middle 1e-15; min \|B\| away from the nodes 0.24. (4) Spectrum = √2 Σλ_i σ_i S^i to 4e-15; det N changes sign (±0.994); at 232 surface points, 2 zero modes (≤ 2.8e-15) with next \|E\| = 2.449; both zero modes move the same way; normal slope 0.943–1.154 (formula to 6e-7); tangent slope ≤ 4.8e-6 | 0.77 s, 133 MB |
| `d2_theta_scan` | θ = 0, π/16, …, π/2 on a 28³ grid plus Nelder–Mead | Zero flux: det H0 signs 50/50 for interior θ. Refined second-smallest \|E\|, θ = π/16 … 7π/16: 0.39, 0.77, 1.1, 1.4, 1.2, 0.86, 0.45; 2e-15 at θ = 0 and π/2. Off-zero touchings at ±E (gap → 1e-15). π flux: det H6 changes sign at all interior θ; min \|E(H6)\| → 1e-17 | 2.74 s, 129 MB |
| `d3_touchings` | Off-zero touchings; θ = π/2 zeros; θ = π/4 surface | θ = π/16: splitting ∝ q in every direction (linear), slopes 0.15–1.92. θ = π/4: slopes 0.38–1.23. θ = π/2, π flux: det H6 ≤ −0.74 on the grid; zeros come in pairs. θ = π/4, π flux: 176 surface points, normal slope 0.20–1.56 | 1.88 s, 106 MB |
| `d4_census` | Weyl census at zero flux | θ = π/16: 24 lower-pair touchings; θ = π/4: 21 at −√2; the upper pair is the image under (π,π,π) to 1e-14. My first nodal-line guess (all 24 axis lines) was wrong; d8 corrects it | 1.85 s, 87 MB |
| `d5_zero_set_dimension` | Rank of the first-order zero conditions | θ = π/2: C symmetry to 2e-16, ranks {2, 3} (lines and points). θ = 0: rank 1 (surface). θ = π/4 and 7π/16: ranks {1, 2} | 2.64 s, 78 MB |
| `d6_pi2_lines` | θ = π/2 lines | 26 rank-2 zeros, \|E\| along the null direction ≤ 7e-16 at δ = 1e-2. 4 rank-3 zeros, linear in every direction. A line tracked over 0.955π stays at k_y = π, k_z = −π/2 with \|E\| ≤ 6.4e-16 | 1.68 s, 78 MB |
| `d7_pi2_points` | θ = π/2 isolated zeros | 11 distinct from 60 starts (points with k_a ∈ {0, π}, and (±π/2)³); 4 bands with slopes ±0.943 in all 300 directions; other bands at ≥ 2.4495 | 2.16 s, 78 MB |
| `d8_pi2_census` | (π/2)Z³ census | 16 points isotropic at 0.9428; 48 on lines; 12 of 24 axis lines carry 2 zero modes at all 121 points (cyclic (a,b,c)) | 0.53 s, 34 MB |
| `d9_cones_vs_theta` | Do the cones survive θ ≠ π/2? | π flux: the 16 cone points are gapped for θ = 0 … 0.49π (gap 0.089 t at 0.49π); isotropic only at θ = π/2 | 3.75 s, 34 MB |

**How the runs were made.**
- Every run went through `run.sh`: nice 10, all four BLAS thread caps at 1, a 38 s alarm, and a load gate below 6. Loads at run time were 2.1–3.3.

**Superseded runs.**
- d1's first run peaked at 218 MB, over the 200 MB cap, from a 48³ grid and a broadcast. It was rerun at 36³ with a loop: 133 MB, same results.
- d6's first version started tracking from an isolated cone point and so found no line. It was replaced by the version that splits zeros by rank.

**Why c14 was inconclusive (ARGUED).**
- Its 20³ grid sits at odd multiples of π/40, so it never lands on the nodes at odd multiples of π/4.
- Its angle t is in an arbitrary SVD basis, so it never sits at θ = 0 or θ = π/2.
- It tested symmetry about 0 at each k for zero flux, which fails except at θ = 0.

**Reuse.**
- `A34/c13_glued_link_hops.py` is run by exec in d1; only its `vector` null space is used.
- c14's 12-band layout is re-implemented in `common.H12` as a cross-check.

## 4. Open edges

1. **The angle θ is free.** Covariance does not fix it. Isotropic cones need exactly θ = π/2 (real-symmetric blocks), which would be a further supplied choice.
2. **Nodal lines at θ = π/2.** They share E = 0 with the cones. Gapping the lines without gapping the cones would need a further term, not studied here.
3. **Exact values.** The cone slope matches 2√2/3, but the closed form is not derived. Why exactly the cyclic lines carry the zeros is also not derived.
4. **Quantum links.** U = σ⁺ is nilpotent (|⟨U⟩| ≤ 1/2), so replacing it with a number is a mean-field toy. The real problem couples matter and link qubits under Gauss's law. On a torus, the cycle holonomies also matter (A40 ERRATA, T5).
5. **The sea.** Negative energies exist at every k, so the empty matter vacuum is not lowest (A39 loophole (a), A40 T9). Filling a sea would need pair creation, which A39 (e) excludes.
6. **Census completeness.** The off-zero Weyl counts for generic θ are lower bounds from a finite number of starts.
7. **Comparator.** Spin-1 "triple-point" fermions with a flat band (Bradlyn et al. 2016; COMPARATOR, from memory, unverified) have the same form as the θ = 0 zero-flux nodes.

## 5. Plain-language summary for the owner

I took the only kind of charged matter that can hop through light's links while respecting the grid's turns. That matter has three internal states, which turn as it hops. With no twist in light's links, it already has point-like crossings at zero energy for one setting of its one free angle. But they are lopsided, twice as fast along one diagonal as across it, with a dead-flat band running through them. With light's half-turn twist on every square, most settings give zero-energy sheets or lines instead of cones. At exactly one setting, perfectly round cones appear (same speed in every direction), but they come with straight lines of zero-energy states, and nudging the setting gives the cones a gap. In every case negative energies exist, so the empty state of matter is never the lowest one.

---

## ERRATA from review round 9 (A34/REVIEW5.md), added by the coordinator
- "Never the lowest state of the one-particle sector" holds for the hop alone; the turn-allowed on-site energy μ·1 (Schur) shifts Tr H to 3μ and can lift all energies above 0, moving every zero-energy crossing to E = μ (A39 (a′)) (C146, C149).
- With two qubits per corner, charge has one sign only (no antimatter); a filled sea would carry net charge, which Gauss's law on a closed grid forbids (EXACT) (C147, C149).
- Verdict scope: nearest-corner hops only; zero and π flux are the only uniform backgrounds the turns allow (EXACT) (C149).
