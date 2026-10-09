# Step 8: tests (pre-registered before running)

**Budget.** The default 2 hours; the owner asked for the exercise without a different budget.

**Rules (skill PR #9472):**
- Readings are fixed before the run and never changed after it; a follow-up gets a dated new entry.
- Searches state their class.
- No verdict rests on long extrapolation.
- Every FAIL or no-go gets the other-vendor referee (codex gpt-5.6-sol xhigh) before it is reported.

## T0: the IR-cone cutoff identity (step 3 "shrink"; run 2026-10-09)

- **Script:** `scripts/S0_ir_cone_cutoff_identity.py`, with its output.
- **Result (EXACT):** a fixed label-space window gives a TT second derivative of K₀⁴/(120π²) per bosonic mode and −K₀⁴/(60π²) per Weyl sea, the same for every shear direction. A proper-space window gives 0.
- **Effect on the wall:** none. This is the smallest object in which the wall bites. R3's surface-term lemma generalizes it to any covariant integrand and any window (`agents/R3_price.md`).

## T1: the one-light-cone test for the surviving shape-blind regulators (pre-registered 2026-10-09)

**Why.** Every surviving way to remove the TT stiffness changes the regulator so that it no longer has the hypercubic Z³ × Z_τ symmetry. That symmetry is what K7a and the kinetic-isotropy primitive used to protect one light cone. Without it, loops generically split the speeds of different species at O(g²/16π²), whatever the cutoff scale. That is the Collins–Perez–Sudarsky–Urrutia–Vucetich mechanism (COMPARATOR). Both R1 and R2 propose this test and predict FAIL.

**Method.**
- **Theory.** A Yukawa theory g·ψ̄ψφ: one Dirac or Weyl fermion ψ and one real scalar φ, both massless at tree level, with equal bare speeds.
- **Time.** Continuous. Space is regulated in two ways:
  - **(a) Fixed Z³ with a smooth proper-distance kernel of width σ** (route F2). Run σ = 1, 2, 3 in lattice units, or as far as converged.
  - **(b) A 3D Poisson–Delaunay spatial lattice** (route F1a), with circumcentric (Voronoi-dual) weights. Use the law average plus the per-configuration spread. If (b) cannot be completed within the budget, report it as INCONCLUSIVE and say why.
- **Quantity.** The one-loop renormalized low-momentum speeds, δc_ψ and δc_φ, and their split Δ ≡ (δc_ψ − δc_φ)/(g²/16π²). Tree-level speeds are equalized before the loop.

**Readings (fixed now):**
- **(a)**
  - **PASS:** |Δ| falls by at least 10× from σ = 1 to σ = 3, trending to zero.
  - **FAIL:** |Δ| ≥ 0.1 and σ-independent within 20%.
  - **INCONCLUSIVE:** otherwise.
- **(b)**
  - **PASS:** |⟨Δ⟩| < 0.01, with per-configuration spread < 0.01.
  - **FAIL:** |⟨Δ⟩| ≥ 0.1, or per-configuration spread ≥ 0.1.
  - **INCONCLUSIVE:** otherwise.

**What a FAIL means.** That regulator cannot have both a protected light cone and zero shear stiffness without tuning. This is one corner of R2's regulator trilemma.
