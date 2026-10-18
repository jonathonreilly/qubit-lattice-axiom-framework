No negative is outright wrong. Three are wounded by hidden premises, but none of the wounds reopens a route to the hierarchy.

**Provenance.** I am Opus 5.5, the same family as the route authors. Nothing here is refereed.

**Read before concluding:**
- `MINIMAL_AXIOMS_2026-06-29.md` in full.
- `PRIMITIVE_REGISTRY_CHECK.md` and `SCALE_REFERENCE_PRIMITIVE_NOTE.md`.
- `derivation_obligations.json`: three entries, none on the hierarchy.
- WALL.md, and the R2–R5 reports, scripts and outputs. R1 has no report, so I skipped it.
- Prior art on main. `YT_CLASS_7_SPONTANEOUS_C3_BREAKING` (April) closed spontaneous C3 breaking for lack of a generation-labelled operator, and the YT primitive analysis lists spontaneous breaking as a missing primitive. Both predate GEN-2's forced Eg order.

## Verdicts

**1. R5 orbit lemma: WOUNDED.**
- The lemma itself is right: if a symmetry maps one generation to another, the whole series agrees.
- Its corollary, "unequal distances need supplied breaking", assumes the realized vacuum keeps the symmetry. GEN-2 says real CKM on rod generations needs an Eg vacuum order, so the fixed rule can pick that order's direction itself.
- **Checked (k1).** In the general O_h-invariant Landau energy to sixth order, the minimum points in a generic, orthorhombic (D2h) direction exactly when c₆ > 0 and |b₃| < 4c₆ρ³. That held for 9% of a random coefficient box, and the criterion matched the numerical minimum in 3000/3000 cases. No direction is put in by hand.
- **Proved (short).** The three levels all appear at first order in one amplitude, so insertion orders and code distances stay equal. The distance ladder stays dead.
- **Proved.** If a symmetry (translation or time reversal) forbids b₃, the minimum sits at θ = π/6. There a C2[101] rotation combined with that symmetry swaps two generations, giving two levels.
- So three levels from one spontaneous order always need a continuous Landau ratio to set their spacing: not supplied by hand, but not fixed either.

**2. R3 Schur ceiling: WOUNDED. Irrelevance bound: SURVIVES.**
- The Schur ceiling is a statement about symmetric vacua. With an Eg vacuum, axis labels go from 2 to 3 levels. Corners also go from 1 to 3, but both sectors stay diagonal, so CKM = 1.
- R3 also mislabels GEN-2. Its table lists GEN-2 as the T1 orientation rep with 1 level, but GEN-2's report gives A1g + Eg, which is R3's own permutation row with 2 levels.
- The irrelevance bound c/y is correct (I checked their quadrature). It limits only splitting built up by the flow, not cutoff-scale matching.
- Its c ≤ 1 premise is not load-bearing: Schur already forbids any symmetric flow, relevant or not, from splitting a single orbit.

**3. R2 bound |V_cb|/|V_us| ≥ √2: WOUNDED.**
- I derived the leading-order clustered formula, with ℓ = ln K and Δ meaning up minus down:
  **|V_cb|/|V_us| = G(ξ_Q)·|Δℓ_x| / |Δℓ_x + ½Δ(ℓ_xxy/ℓ_xy)|**
- For any log-quadratic (Gaussian) kernel ℓ_xxy = 0, so the ratio is G ≥ √2. That is R2's identity, now proved for that class.
- It is not a clustering theorem. **Checked (k3):** a cubic-log kernel, with u_R and d_R placed at the same offset and given opposite anharmonicity, gives ratios 0.096, 0.27 and 0.58. The formula matches to 3–4 digits, and the masses keep R ≈ 2. The inversion comes from unequal up and down tilts.
- Physical profiles still invert:
  - a Gaussian doublet with skew-normal right-handed profiles gives 1.47 at every offset tried;
  - in a random scan, 2% of configurations reach ≤ 0.3 (R2's sech scan: 0.4%).
- The route stays dead on its other leg: nothing in Z³ hosts a wide profile.

**4. R4 area-law control: SURVIVES. Koide chance: SURVIVES, with a premise corrected.**
- The random spectra go through exactly the same search: 3312 placements, the same σ grid, free scales. The random CKM targets are unsorted, which makes them harder to fit, not easier.
- R4 multiplied P(Q) by the unconditional P(δ), assuming the two are independent. That premise is false.
- **Checked (k4, 6×10⁶ random triples):**
  - Given Q ≈ 2/3, positive roots confine δ to [0, π/12].
  - The density of δ at 2/9 is 5.8 times the unconditional value.
  - Only 13 of R4's 62 δ values lie in the allowed range, which offsets this.
  - Corrected joint chance: 1.4e-6 (R4 had 1.5e-6).
- The chance scales linearly with the size of the δ list, which was chosen after 2/9 was known. It rises above 1e-5 once the list reaches about 450 values. Q alone (30 targets, three sectors) gives about 2e-3.

**5. R5 data-processing result (no c-function): SURVIVES.**
- The standard results are applied correctly. Relative entropy falling along a flow still allows damped spirals.
- Exact cycles need DPI equality (Petz recovery), which confines them to the protected (peripheral) sector.
- The c-, a- and F-theorems need reflection positivity together with Lorentz invariance.
- None of this is load-bearing for masses, because R5's T1 shows the mass comes from the coherent part of the leakage.

**Common finding.** The negatives that state symmetry ceilings — R5's lemma, R3's Schur, R2 L1b, R4 T1c — share one premise: the realized vacuum is symmetric. Lifting it gives three levels, and for rod generations a non-trivial CKM (M_f = a_f·1 + b_f·J + c_f·diag(e)), but no exponents and no fixed ratios. Two sector-blind side checks (k5) are not decisive:
- r = √2 for every sector fits down quarks within ×1.4–1.5;
- it fits up quarks at ×2.95 (low scale) and ×4.13 (M_Z).

## Most promising remaining route

**Route:** let the fixed rule choose the residual symmetry group on rod (axis-label) generations, through GEN-2's forced Eg order.
- Its D2h branch gives three levels plus CKM.
- Its T branch, from an A2 order, is main's Koide circulant. Per R3 Part A, rods under T have exactly the complex-circulant commutant.

It is the only escape I found that none of the negatives covers.

**Cheapest decisive test:** compute the Eg Landau coefficients (b₃, c₆) of GEN-2's rod model, by mean field or a one-loop fermion determinant. I estimate a few hours.
- **Kill:** c₆ < 0, or |b₃| ≥ 4c₆ρ³, for every admissible coupling. Then every spontaneous vacuum is tetragonal, the two-level ceiling returns without the symmetric-vacuum premise, and all five negatives close.
- **Pass:** three levels arise with no supplied direction. The next question is whether leakage makes ln mᵢ linear in the strains. That predicts one sector-universal shape R(θ*), but it is a weak test, because about 40% of random spectra fit at that level (R5, model B).

Peak memory was 186 MB, one process at a time, and nothing is left running. I edited nothing outside K/; I lowered the cap in K's copy of `capped.sh` to 0.3 GB. I wrote no REPORT.md, so save this message if you need one there.

Files are in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/masswall/K/`:
- `scripts/k1_eg_landau.py`, `k1.out`
- `scripts/k3_ckm_nongauss.py`, `k3.out`
- `scripts/k4_koide_conditional.py`, `k4.out`
- `scripts/k5_koide_sector_blind.py`, `k5.out`