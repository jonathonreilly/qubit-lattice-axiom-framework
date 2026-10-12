# E1′-b: a uniform bound on the massless link-field Fano factor (supervisor, Claude Opus 5.5; 2026-10-09)

**Setting.** Π is a Poisson process on M^{1,3} with intensity ρ = ℓ⁻⁴. x is a fixed event. J is the indicator of a source region S that straddles x's past light cone at distance about D, with size s and D ≫ s ≫ ℓ.
- L_Π(x,y) = 1 iff y ≺ x and Π ∩ I(y,x) = ∅.
- F(Π) = Σ_{y∈Π} J(y)L_Π(x,y) is the direct massless link field, up to the factor ρ⁻¹a.

**Mecke (exact):**
- E F = ρ∫J e^{−ρV};
- Diag = ρ∫J² e^{−ρV} = E F (for J an indicator), written N̄.

**Step 1 (Poisson Poincaré inequality; Wu 2000; Last–Penrose 2017, Thm 18.7).** Var F ≤ E∫(D_zF)² ρ dz, where D_zF = F(Π+δ_z) − F(Π).

**Step 2 (the add-one cost; exact).** Adding z links z itself if its interval is empty, and cuts every link whose interval contains z:

  D_zF = J(z)L_Π(x,z) − Σ_{y∈Π} J(y)L_Π(x,y)·1{z ∈ I(y,x)}.

So (D_zF)² ≤ 2J(z)²L_Π(x,z) + 2(Σ_y J(y)L_Π(x,y)1{z∈I(y,x)})².

**Step 3 (the three terms).**
- **Term A:** E∫2J(z)²L(x,z)ρdz = 2·Diag.
- **Term B_diag (pairs y = y'):** 2ρ²∫J²V e^{−ρV} = 2⟨ρV⟩·Diag.
  - Near the cone the shell measure in m = ρV is ∝ m^{−1/2}dm. This follows from d⁴y = 2πT²τdτ asymptotically, with τdτ ∝ m^{−1/2}dm.
  - So ⟨m⟩ = Γ(3/2)/Γ(1/2) = ½ and B_diag = Diag.
  - Hypothesis: the source is thick compared with the shell. This holds for every macroscopic source.
- **Term B_off (pairs y ≠ y'):** 2ρ³∫∫J(y)J(y')|I(y,x)∩I(y',x)|·P(both linked) ≤ 2ρ³∫∫JJ'|I∩I'|e^{−ρ(V+V')/2}.

**Step 4 (needle geometry).**
- **Shape of a link interval.** Write y at distance r ≈ D below the cone by δ, so τ² ≈ 2rδ and ρV = O(1) gives δ ~ ℓ²/(2D). In null coordinates along y's direction, I(y,x) has u ∈ (−δ,0), |v| < 2r and |ζ|² < |u||v|. It is a needle of transverse half-width ≤ √(δ|v|) that tapers to the apex x.
- **Overlap of two needles.** For a second needle at angle θ, the axes are separated by about θ|v|/2 at depth |v|. The needles intersect only where θ|v|/2 ≤ (√δ + √δ')√|v|, i.e. |v| ≤ v* = 4(√δ+√δ')²/θ².
- **The bound.** The cross-section at depth |v| has measure ≤ πδ²|v|/2, giving |I∩I'| ≤ πδ²v*²/4 ≈ 64πδ⁴/θ⁴ ≈ 4πℓ⁸/b⁴ with b = Dθ. Also |I∩I'| ≤ min(V,V').
- **Checked by Monte Carlo** (`scripts/E1p/S2_needle_overlap.py`, r = 1000ℓ, ρV = 1):

  | b/ℓ | 0.25 | 0.5 | 1 | 2 | 4 | 8 | 16 | 32 |
  |---|---|---|---|---|---|---|---|---|
  | overlap / V | 0.85 | 0.71 | 0.48 | 0.21 | 0.043 | 4.5e-3 | 3.3e-4 | 2.2e-5 |
  | overlap·b⁴/ℓ⁸ | 0.003 | 0.045 | 0.48 | 3.3 | 11 | 18.4 | 21.6 | 23.0 |

  So overlap ≈ 23ℓ⁸/b⁴ asymptotically, in line with the estimate 4π = 12.6 up to a factor of 2. The b⁻⁴ law is confirmed.

**Step 5 (integrate).**
- **The y' integral, for fixed y.**
  - The shell thickness gives ∫dδ' e^{−ρV'/2} ≈ (√12/2)·ℓ²/r'. *(Corrected per referee: no ρ prefactor.)*
  - The transverse integral gives ∫d²b·overlap ≈ 13ℓ⁶. It is finite, because b⁻⁴ is integrable in 2D.
  - The depth integral gives at most s.
  - Altogether ρ²∫dy'(…) ≤ c₀·s/D, using ρ²ℓ⁸ = 1.
- **The y integral** with e^{−ρV/2} gives at most √2·Diag.
- So B_off ≤ c·(s/D)·Diag, with c a finite geometric constant independent of s/ℓ and of ρ.

**Result.**
- Var F ≤ (3 + c·s/D)·N̄, so the relative noise is ≤ √((3 + c·s/D)/N̄), **uniformly in s/ℓ**.
- The measured Fano factors (1.0–2.45 at s/D ≤ 0.3) obey the bound.
- At physical parameters (neutron-star merger, 1 Gpc), s/D ≈ 4e-22 and N̄ = 2.2e57, so the relative noise is ≤ 3.7e-29.

**Hypotheses.**
- The source is an indicator, or bounded, and thick compared with the link shell.
- D ≫ s ≫ ℓ.
- The flat, infinite sprinkling of the E1′ setting.
- A scalar link field. This is not a tensor bridge.

## After the referee (codex sol: CONFIRMED WITH CORRECTIONS; `E1p_b_referee.md`)

**E1′ gravity is PASS for the registered scalar, source-driven proxy G₀ = aL.** The tensor bridge is a scope caveat, not a PASS gate.

**Corrections.**
1. **B_diag = Diag is a leading-order asymptotic.**
   - Corrections are O(ℓ²/(Ds) + s/D) and are absorbed into c·s/D.
   - "Thick" means thick in the cone-normal direction compared with ℓ²/D, with a non-vanishing, slowly varying cross-section where the cone passes.
   - A thin source at m = m₀ gives B_diag/Diag ≈ 2m₀.
2. **The overlap depends on the two shell depths.** The usable bound is |I∩I'| ≤ min{ℓ⁴m, ℓ⁴m', Cℓ⁸b⁻⁴·min(m,m')(m^{1/4}+m'^{1/4})⁴}.
   - The 23 plateau is specific to r = r' and m = m' = 1. The referee's independent runs give about 22.6.
   - The polynomial m-dependence is harmless, because every moment is exponentially integrable.
   - 4π is an order of magnitude, not an upper bound.
3. **The transverse integral is finite:** 2π∫b·db·min(M, A/b⁴) = 2π√(MA).
4. **"F ≤ 3" means F ≤ 3 + c·s/D.** That is indistinguishable from 3 at physical s/D of about 4e-22.

**Strongest correct statement (referee).** For a bounded, regular source crossing the past cone transversely, with cone-normal thickness ≫ ℓ²/D, bounded aspect ratios and D ≫ s ≫ ℓ:

  Var F ≤ (3 + C′_S·s/D)·N̄, with C′_S independent of ρ and of s/ℓ.

For the neutron-star proxy at 1 Gpc this gives sd/mean ≲ 3.7e-29.

**Not established:** tensor propagation, nonlinear gravity, strain response, or stable initial-value dynamics.
