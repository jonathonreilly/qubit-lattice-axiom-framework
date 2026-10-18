<!-- Saved by supervisor from worker's final message (harness blocked REPORT.md write). -->
**Reading: OPEN, leaning TETRAGONAL.** The pre-registered reading for the strain/speed channel is OPEN, because D2h vacua appear only at the admissibility edge (step 1 below). If those edge vacua are taken at face value, it is LANDAU-D2H but tuned: 2.5% of couplings, edge only. The Yukawa/mass channel is TETRAGONAL.

**Provenance.** One Opus 5.5 worker, the same family as K, R1 and GEN-2, and unrefereed. PREREG.md was written at 22:57Z, before any run. Peak memory was 188 MB, one process at a time, and nothing is left running.

**What I read first.**
- The required background: MINIMAL_AXIOMS_2026-06-29 (all of it), PRIMITIVE_REGISTRY_CHECK, SCALE_REFERENCE_PRIMITIVE_NOTE, and derivation_obligations.json (3 entries, none on the hierarchy).
- The exercise files: WALL, TESTS, SUMMARY, K's report with k1, R1's report, T's PREREG, and GEN-2's PREREG, REPORT and gen2_symm.py.
- Prior art on main:
  - `YT_CLASS_7_SPONTANEOUS_C3_BREAKING` is a no-go for corner generations, not rods.
  - The historic intake `TETRAGONAL_STABILIZER_MU_TAU` already maps "a tetragonal residual leaves a degenerate pair" for diagonal couplings.
  - I found no Eg Landau computation for rod generations on main.

**Model added (a named premise).** GEN-2 builds no rod Hamiltonian, so I supplied the smallest one with its content:
- three rod species, one per axis;
- the Eg order coupled linearly to the rods' speeds, with the 3 couplings the cubic group allows;
- the order's own potential angle-blind, so every direction-dependent coefficient comes from integrating out the fermions.

This is mean field and one loop at once. I ran it with naive (all-doubler) rods and with Wilson rods (doublers gapped), over 600 coupling directions each. Channel B is Dirac fermions whose mass matrix is linear in the order.

## Plain-words findings

1. **The fermions always want the order to grow (proved).** The ground-state energy is concave in any linearly coupled order parameter, because it is a minimum of affine functions.
   - The fermion quadratic term is negative for every coupling (0 of 1200 positive).
   - The fermion quartic is negative for 80% of naive couplings and all Wilson couplings.
   - In pure mean field there is no interior ordered vacuum for 571/600 naive and 600/600 Wilson couplings. The order runs away until some rod's speed has fallen to 5% of its base value, or to the ρ = 1.5 cap.
   - The 29 interior vacua that do exist are all tetragonal.

2. **The cubic term dominates.**
   - b₃ is nonzero for every coupling, with either sign about equally often.
   - c₆ is about 50 times smaller (median |c₆/b₃| ≈ 1/45).
   - K's radius (|b₃|/4c₆)^{1/3} lies beyond the admissibility edge for 98% of couplings, with a median of 2.3 times the edge.
   - K's criterion matches the exact angular minimum at 99.7–100% of points.

3. **A D2h direction needs O(1) Lorentz violation (checked).**
   - Even if any strain could be held by an angle-blind potential, D2h occurs for only 3% of couplings.
   - At its onset the fermion speeds have already shifted by at least 30% (naive) or 50% (Wilson); the median is about 85%.
   - At strains where speeds shift by 10% or less, none of 8000 direction samples gives D2h. The fraction is about 1% at the edge; the sixth-order form suggests it scales as ρ³ at small strain.
   - The Lorentz-violation cost per unit order parameter is about 0.9 for the rods' own speeds, and 0.15–0.7 for the part every field feels.

4. **The mass channel is always tetragonal (proved for a definite real mass matrix).**
   - tr M and tr M² do not depend on the angle.
   - tr M³ = c₀ + κρ³cos3θ, with κ ∝ (μ₁−μ₂)²(μ₁+2μ₂).
   - The derivative of V with respect to tr M³ is a second divided difference whose sign is fixed while M stays definite. So V is monotone in cos3θ, and the minimum sits on a tetragonal line.
   - Checked numerically: 132/132 real couplings away from the flat lines and 480/480 complex samples are tetragonal.
   - On the lines μ₁ = μ₂ and μ₁ = −2μ₂ the spectrum does not depend on the angle at all, so one loop chooses no direction there.

5. **The mass levels at the D2h vacua give no evidence.**
   - The realised angles θ* spread over 2.5° to 58.8°, so the model does not fix the angle.
   - Fitting K's form M_f = a(1 + βJ + γ diag(ê)) gives ×4.65 (MZ), ×4.66 (GUT) and ×4.15 (MIX), so all three fail ×3.
   - In the 200-spectrum random control, 18.5% fit within ×3, and 26–32% fit at least as well as the real data.

6. **A correction to TESTS' tetragonal reading.** With the J structure, a tetragonal vacuum gives three levels, not two.
   - But the eigenvector (0,1,−1)/√2 is shared by every sector, so one generation does not mix: |V_ub| = 0 exactly. That held at 98% of grid points, and the best fit is off by about 1e10.
   - It is still a kill, but the mechanism is an unmixed generation, not a two-level ceiling.

## Labels
- **Proved:** the concavity result, the channel-B monotonicity lemma for a definite real mass matrix, and the two flat lines.
- **Checked:** everything else above. Brillouin-zone convergence at M = 24 matches M = 16 to within about 1–5% on b₃ and c₆ for every D2h case.
- **Suggested:** the ρ³ scaling.
- **Comparator:** the mass and CKM data, recalled rather than fetched.

## Deviations (post-hoc, none enters the reading)
- These arms were added after the prereg:
  - the angle-blind "any strain" arm;
  - the dense strain scan;
  - complex channel B;
  - the flat-line check;
  - the mean-field interior check.
- The angle refinement used parabolic interpolation instead of the pre-registered golden-section search.
- The mass search kept the top 300 mass candidates per sector before the CKM step. The control was searched the same way.

**For the wall.** The vacuum-direction route does not derive the hierarchy. In GEN-2's simplest rod model a direction-picking (D2h) vacuum is a minority, edge-of-validity outcome that needs O(1) Lorentz violation. Its angle is not fixed, and its fits do no better than random spectra. The mass channel is tetragonal.

## Files
The reports are saved only in this message, because writing REPORT.md was refused. Everything is in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/masswall/T3/`:
- PREREG.md
- scripts/t3_landau.py → t3_AN.out, t3_AW.out, t3_B.out
- scripts/t3_detail.py → t3_AN_detail.out, t3_AW_detail.out
- scripts/t3_scaling.py, t3_bflat.py, t3_bcomplex.py, t3_hs_check.py, t3_masses.py, each with a matching .out
- scripts/smoke.py → scripts/smoke.out