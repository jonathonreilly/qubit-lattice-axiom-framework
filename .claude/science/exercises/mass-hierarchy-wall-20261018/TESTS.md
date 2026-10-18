# Mass wall exercise: tests

**T-2AMP. Two isotropy-safe amplitudes** (pre-registered 2026-10-18T21:49Z, before any run; R1's cheapest next test; Jon asked to "run the two-amplitude test").
- **Model.** Use R1's menu (masswall/R1/scripts). Two isotropy-safe breaking fields together:
  - (a) the A2 pseudoscalar plus the staggered field;
  - (b) the A2 pseudoscalar plus the (111) corner star.

  Every particle type shares one native generation label: the axis-permutation representation and the node representation, both tested. The Yukawa matrices are polynomials in (ε₁, ε₂) with random complex O(1) coefficients. Use at least 3 coefficient draws. Free parameters: ε₁, ε₂, and one scale per sector.
- **Data.** All 9 charged masses and |V_us|, |V_cb|, |V_ub|, on all three of HIER-2's mass sets.
- **Control.** The same search on at least 200 random log-uniform spectra paired with random CKM values.
- **Readings.**
  - **2AMP-PASS:** the best fit is within ×3 on all 12 numbers, in at least 2 of 3 draws, and the random pass rate under the same search is at most 5%.
  - **2AMP-FAIL:** no fit within ×3, or the random pass rate is above 20%.
  - **OPEN:** otherwise.
- **Check also:**
  - whether the residual symmetry still makes up and down give the same ratios (the predicted failure: m_u/m_t and m_d/m_b differ by about ×120);
  - whether speeds stay isotropic at every order.

**T-2AMP result (recorded 22:00Z; same family; unrefereed): 2AMP-FAIL on all three sets.**
- **Residual symmetry.** Both isotropy-safe pairs leave a tetrahedral residual. It contains the C3 about (111).
- **P and S labels.** The CKM is a permutation (|V| ∈ {0, 1} to 1e-11), or the masses are exactly degenerate. This holds for every placement and coefficient (proved: R1 Lemma B with Schur; prior art is main's shared-C3 theorem).
- **Hierarchy.** A generation-blind Yukawa is allowed, so m₁/m₃ ≥ 1.5e-2.
- **Control.** 0/300 random spectra pass.
- **Character labels** (secondary arm) fail ×3, and random spectra fit as well.
- **Reading.** For P and S labels, isotropy and CKM are in tension: the residual that protects isotropy forces a permutation CKM.

**T-LANDAU. Vacuum-direction test** (pre-registered 2026-10-18T22:49Z, before any run; the kill round's top route; Jon: "run the vacuum-direction test").
- **Model.** GEN-2's rod / axis-label generations (campaign/GEN2 on branch claude/chirality-grid-exercise-20261014), coupled to an Eg order parameter Φ.
- **Task.** Compute the Eg Landau coefficients from the model itself, not chosen: the cubic b₃, the quartic, and the sixth-order c₆. Use the one-loop fermion determinant (integrating out the generation fermions) and/or mean field, over the admissible coupling range. Then decide whether the minimum is a generic D2h direction. The criterion: c₆ > 0 and |b₃| < 4c₆ρ³ (K/REPORT.md, k1).
- **Readings.**
  - **LANDAU-D2H:** some admissible coupling gives a D2h minimum. State the range, and whether it is generic or tuned.
  - **LANDAU-TETRAGONAL:** every admissible coupling gives a tetragonal or trigonal minimum. The two-level ceiling then returns without the symmetric-vacuum premise.
  - **OPEN:** otherwise.
- **Also report:**
  - the Lorentz-violation cost of the order, in units of the order parameter;
  - the three mass levels that result, compared with the data and with a random control.

**First-principles derivation (FP/derivations/generations-from-lattice-symmetry-2026-10-18.md; same family; unrefereed).**
- **Generations.** Three generations are available only as the number of axes. Nothing forces the count.
- **Mass ratios.** No symmetry fixes any mass ratio (proved). The observed CKM leaves the shared residual nothing to act on (proved). All 13 charged-sector numbers are unavoidable inputs. Mass hierarchy: BLOCKED at the values wall.
- **Conditional prediction: TM1 lepton mixing.** It needs F2 (star or T1 generations) and F3 (exact residuals per sector), with a bond-centred C₂[110]∘T(e₃) half-turn for the neutrinos. It is the only survivor of the lattice's residual menu.
  - Prediction: sin²θ₁₂ = 0.3182 ± 0.0002. JUNO's first result, verified, is 0.3092 ± 0.0087, about 1.0σ away (arXiv:2511.14593).
  - TM1 as a pattern is known in the literature. What is new is its lattice realisation, and that it is the only survivor.
