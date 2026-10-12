# VERDICT: CONFIRMED WITH CORRECTIONS

1. **Kato/stabilizers:** At nonzero momentum the soft space retains only the little-group representation, not the full \(O\)-representation. The proof remains valid because the C4 and C2′ characters are restrictions of the same \(O\)-representation \(G\) at \(k=0\). Reality and cubic rotations taking \(k\to-k\) complete the branch count. `R15-3_report.md:97-115`.

2. **Irrep inequality:** Confirmed; `s1` reproduced byte-for-byte. The inequality gives \(\dim G\ge8\). However, the C4+C2′ minimizer list omits \(4A_1+4A_2\); it disappears only when C3 is also imposed. `R15-3_report.md:117-126`; `scripts/s1_characters.out:15-23`.

3. **Results and models:** Result (i) and the axis-only result (iii) are confirmed. Result (ii)’s five-branch bound requires the limiting metric residue to have rank two and span the complete axial TT plane; merely giving both branches nonzero, possibly collinear TT residue is insufficient. M1 is globally PSD and is a valid two-branch axis-only alias. M2 saturates only the character bound, not the genuine metric-TT problem. `R15-3_report.md:122-181`; `scripts/s2_models.py:18-49`; `scripts/s2_models.out:2-90`.

4. **Nonlocal symbols:** Confirmed. X1 has two linear and four flat branches under the strict count. X2 has exactly two but is discontinuous at \(k=0\). Discontinuity is therefore necessary within the finite PSD \(O\)-covariant class, not universally. `R15-3_report.md:188-192`; `scripts/s4_nonlocal_exhibits.out:1-15`.

5. **Lemma N:** Not established as a theorem. The exact polynomial result is correct—there are no degree-two polynomial TT tensors—but the extension of the soft reduction through arbitrary hard auxiliaries and Schur terms is explicitly unwritten. Lemma N remains conditional and is unnecessary for the strict reading. `R15-3_report.md:201-216,256`; `scripts/s3_poly_tt.out:1-5`.

6. **Reading:** The corrected Theorem C(i) satisfies the FIXED rule, so R15-3 is **EXCLUDED** in the stated finite continuous PSD Gaussian auxiliary class. `TESTS.md:4954-4962`; `R15-3_report.md:228-265`.

**Strongest correct statement.** For any real, translation-invariant, proper-cubic-covariant PSD quadratic bosonic Hamiltonian with finitely many canonical pairs per cell and a symbol continuous at \(k=0\), two branches with genuine TT metric polarization along both a cubic axis and a face diagonal force \(\dim G\ge8\), hence at least four strict gapless branches and two partners; if the limiting axial metric residue additionally has rank two and spans the full TT plane, then \(\dim G\ge10\) and at least five branches are forced. Thus the FIXED reading is **EXCLUDED** for finite local PSD Gaussians with arbitrary finite auxiliary \(O\)-irreps, while axis-only aliases, discontinuous symbols, infinite-mode, indefinite/constrained, non-Gaussian, and flat-is-gauge constructions remain outside the result.

Full report: [REFEREE_VERDICT.md](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R15-3/REFEREE_VERDICT.md>)