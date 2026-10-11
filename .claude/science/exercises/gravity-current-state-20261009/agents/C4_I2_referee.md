# VERDICT: CONFIRMED WITH CORRECTIONS

1. **Generator equivalence:** Exact for a uniform reblocked fine lattice. In 3D, refinement `a/L` requires `L³` sites/bands—not `L`; an arbitrary `N`-site cell is not equivalent to spacing `a/N`. The 3D rational residual is exactly zero. `i2_poincare_exact.py:1-13`; `referee_independent_checks.out:1-7`.

2. **C1 two-band network:** Confirmed in 1D. Its matrix commutes with an exact fine translation, so the equivalence extends beyond the spectrum and the partner floor is exactly `2π`. The claimed 3D extension remains unproved. `RC_C1_report.md:186,236-247`; `referee_independent_checks.out:8-9`.

3. **S1/S2:** Both are correct with scope qualifications. S1 matches I1’s sum rule; conservation makes the current band-diagonal and scalar within degenerate energy blocks under the standard first-moment generator assumptions. S2 applies to bands assigned to a lifted tower, not arbitrary networks without that target. `I1_report_unrefereed.md:47-59,107-126`; `I2_report.md:93-110`.

4. **Scattering:** Fine translation is sufficient for the selection rule, and the tested forbidden vertex amplitude turns on linearly with symmetry breaking; a rate turns on quadratically. Necessity of an internal `Z_N` is not proved. Fine-lattice umklapp remains order one near the truncation edge. `i2_umklapp.out:1-35`.

5. **Scalings:** Reruns were byte-identical. Window powers and conditional `N*` arithmetic are correct. The exact `−1` result is the unweighted signed average; loop-weighted ratios are only asymptotically constant for the tested nearest-neighbour scalar. `N⁴` uses `N` as linear refinement. A P0-level loop/TT `N*` is not established without I3. `I2_report.md:77-89,172-191,240-250`; `referee_independent_checks.out:10-17`.

6. **Fixed reading:** I2 establishes “every finite-`N` truncation inexact” for its stated free, finite-component, periodic `C²` quadratic, standard-generator C3 class. It does not establish the full lane FAIL, which also needs I1’s infinite-DOF necessity and I3’s loop/TT result. `TESTS.md:1281-1285`.

**Strongest correct statement:** For a finite-dimensional Hermitian periodic `C²` Bloch dynamical matrix with the standard first-moment boost, conserved energy current, and a common nonzero C3/HDA coefficient `β`, periodicity forces the signed band-and-zone averaged boost anomaly to equal `−β` per mode, so no finite band count closes C3 exactly; an `N_band`-branch tower assignment also incurs aggregate C1 face residual at least `π|β|N_band`. A uniform `L³`-site cubic supercell is exactly a fine lattice of spacing `a/L`, and the specific 1D C1 two-band model is exactly the folded `a/2` chain, but these results neither identify arbitrary finite networks as fine lattices nor prove a universal `Z_N` necessity or P0-level loop response.

Full referee report: [I2_referee.md](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C4/ref_I2/I2_referee.md:1>).