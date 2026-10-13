# VERDICT: CONFIRMED WITH CORRECTIONS

The worker’s **OPEN** reading is correct. All five runners reproduced their stored outputs.

1. The self-energy identity holds for the \(O(e^2)\), occupation-linear UV–thermal cross term—not the complete thermal free energy. `R19-31_report.md:95-105,245`.

2. The Abelian spatial Ward result is confirmed at every tested strain: \(\Pi_{ii}(0)\sim2\times10^{-13}\), and the static magnetic term vanishes by Brillouin-zone translation. But \(\Pi_{00}=m_D^2\neq0\); gauge invariance alone does not remove nonlocal HTLs. The no-\(g^2T^2\) cross-term conclusion additionally requires the single-cut identity and is not checked for non-Abelian gauge theory. `scripts/r1931_photon_thermal.out:3-13`; `scripts/r1931_sqed_cross.out:27-38`; `R19-31_report.md:69-74`.

3. The background-field calculation is confirmed: the gap is \(-0.0823e^2m^2\), stable under smaller strain steps. It becomes \(O(g^4T^4)\) only when \(m^2=O(g^2T^2)\). This relies on the worker’s unadopted background-field sharpening of `(S_loc)`. The numerical Debye mismatch applies to the script’s particular two-transverse-mode prescription, not every conceivable electric Debye subtraction. `scripts/r1931_mcheck.out:1-3`; `R19-31_report.md:115-136,253-257`.

4. The scalar speed residue is confirmed:
   \[
   (-0.7845)\frac{\pi^2}{90}=-0.08603,
   \]
   yielding \(m_g^2/H^2=-1.745\times10^{-3}\) under the stated Higgs mapping. The quoted \(-4\times10^{-2}\) total is only a scenario: its gauge multiplicity is guessed and its dominant fermion Hessian is uncomputed. `scripts/r1931_sizes.py:12-25`; `R19-31_report.md:176-186`.

5. The Wilson results reproduce: \(\partial_h^2\delta m=-0.06216e^2\) and an independent thermal integral gives \(m_g^2/H^2=-4.838\times10^{13}\) at 100 GeV. This is correct arithmetic, but not a checked SM prediction: it assumes a vectorlike Wilson model mapped to QCD, zero-temperature quark masses, a Planck lattice, the canonical gravity bridge, and exclusion of \(\langle\bar\psi\psi\rangle\) from `(S_loc)`. `scripts/r1931_wilson_mass.out:2-17`; `scripts/r1931_sizes.out:14-19`.

6. R19-27’s per-site counterterms cannot affect these shear Hessians within their stated \(C(n,\phi)\) class: traceless strain fixes \(n\), and R19-27 explicitly excludes anisotropic response. This does not exclude new per-link or strain-dependent counterterms. `R19-27_report.md:77-83,119-124,226-232`.

The fixed readings are applied correctly: the restricted-background \(O(g^2T^4)\) residue fails `GAUGE-CANCELS`, while the Wilson \(g^2m_fT^2\) residue depends on an unspecified background-list choice and therefore does not unambiguously establish `GAUGE-RESIDUE`. `TESTS.md:8628-8631`.

**Strongest correct statement.** In the one-loop, occupation-linear noncompact-U(1) lattice model, the spatial Ward identity removes a gauge-boson mass term at every strain, while a charged-scalar mass term remains; a scalar background-field `(S_loc)` cancels its leading \(e^2T^2\) contribution, leaving the checked \(-0.0823e^2m^2\Phi\) gap and \(-0.0860e^2T^4\) speed residue. Wilson edges also possess a checked \(-0.0622e^2\) additive-mass Hessian that can generate a huge conditional \(\langle\bar\psi\psi\rangle_T\) channel. The non-Abelian extension, fermion speed rows, complete `(S_loc)` background set, and gravity identification remain open, so **OPEN** is the strongest fixed reading.

Full record: [REFEREE_VERDICT.md](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R19-31/REFEREE_VERDICT.md:1>)