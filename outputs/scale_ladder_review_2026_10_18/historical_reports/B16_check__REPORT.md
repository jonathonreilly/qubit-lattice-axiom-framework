# B16 check: Maxwell closure

Provenance: a fresh-context checker of the same model family. It wrote all its own code, importing nothing from B14 or B16. Saved by the supervisor from the hand-back.

**Runners:** chk1_timing, chk1b, chk1c, chk2_cone, chk2j, chk3_obstruction, chk3b, chk3c, chk4. Together: 23 PASS and 6 FAIL. None of the FAILs is a B16 claim failing:
- C2d: the checker's own hypothesis, refuted.
- C2h: the staggered half fails.
- C2j: the slope is 0.80 against a 1 ± 0.2 threshold, with local slopes rising.
- C3c-FWD: pre-asymptotic, superseded by C3d.
- C3d-STAG: inconclusive.

Buggy first-run logs are kept as `*_run1_*_BUG.log`.

## Verdicts

1. **Timing.** Confirmed within B16's class, corrected in scope.
   - The 8 one-sided classes reproduce, including mod Gauss.
   - (mean, four) leaves 384 non-bond pairs at L=4.
   - No generator Σ ξ_b O_b paired with gravity's bond ξ can rescue the symmetric timing (C2e).
   - **Exact local rule (C1e–g).** {H, H} is bond-supported iff each plaquette weights only corners whose opposite corner is not covered by its links' timing supports.
   - **Correction.** Reflection-symmetric closing timings exist if unit translations are broken. Example: staggered, with links at their even endpoints and plaquettes at the mean of their odd corners (C1d). This gives the same cone (C2f).
   - But the staggered generator carries an O(1) doubler component (C2j). Its {G′,C} ratio runs 1.000 → 1.072 at L = 16–56, which suggests an O(1) defect (one configuration).
2. **Cone.** Numbers confirmed; framing corrected.
   - c_B = −sK/(4α) for FWD and STAG. Doubling the generator gives 2κ (C2g). g-independence is exact.
   - G_A is the generator induced by the bracket (C2a), and acts as the unit L_ξ on smooth fields (C2h, error ∝ L^-0.97).
   - Sector generators λ_s L_ξ give a total G that closes on itself only if all λ_s are equal.
   - **So the normalisation is derived, given {G, G} closure and δ_ξh = L_ξg. The same holds for G_m and G_f.**
   - Open: the lattice {G, G} was not checked; the argument is nonlinear-order.
3. **Stress coupling.**
   - The one-parameter family is confirmed with Gauss imposed via E = curl W (C4a). Without Gauss, P_A has no solution and G_Lie closes (C4b).
   - M3–M6 (structure function, shared λ, c_φ = c_B) were not independently checked.
4. **Gauss multipliers: confirmed.** T5b is true by definition on the lattice.
5. **Obstruction.** The identity is exact (C3a), coupling-independent and non-absorbable by grading.
   - **Measured:** FWD Maxwell D/H(∂N) and R/H(∂N) ~ L^-1.03, so O(a). The B14 scalar gives D = 0 and R ~ L^-2.06, so O(a²).
   - **Attribution corrected.** The O(a) comes from the non-antisymmetric one-sided G_A that the timing forces. The scalar's central-difference G_m is antisymmetric.
   - B14 E5's ansatz-independence logic is valid. T6d was not rerun.
6. **Prior art.** Add:
   - Schwinger's energy-density commutator condition (1962–63);
   - Loll 1997 (gr-qc/9708025);
   - arXiv:2305.10097;
   - the cubical cell-ownership convention: forward timing is common, so "upwind" overstates it.
