# VERDICT: NOT CONFIRMED

The core identities and toy-model numerics are correct, but Theorem R is overstated and the fixed **V1-RECEIVER** reading is not met.

- **Lemmas E and X0:** Confirmed. \(W=nF_n\), \(W_k=((4-k)/3)\rho_k\) for pure power terms, and \(E_I\nabla^\nu X^I\) has no energy projection. `R19-27_report.md:94-104`; `scripts/r1927_identities.out:1-3`.

- **Lemma D:** The identity \(\dot\rho+3HW=F_\phi\dot\phi\) is exact. The interpretation needs qualification: for \(\dot\phi\neq0\), the term exchanges energy with the scalar sector and is not separately conserved. `R19-27_report.md:106-110`; `scripts/r1927_identities.out:4`.

- **Theorem R:** Its polynomial cancellation works only after assuming the per-site counterterm basis, exact LCP, linear mass-background relation, and \(m\ell\ll1\). P-R19-27a is explicitly an added completion datum, not forced by V1 or the axioms. “Every BO state” is unsupported given the report’s exclusions of full-SM operator mixing, gauge/fermion thermal terms, and the crossover. `R19-27_report.md:13-18,119-124,226-231`; `MINIMAL_AXIOMS_2026-06-29.md:85-90`.

- **Numerics:** Both requested runners reproduce their archived outputs byte-for-byte. An independent analytic derivative gives \(W_{\rm site}/W_{\rm LI}=-5.31892\times10^{-7}\) at \(m\ell=0.05\), matching `scripts/r1927_lcp_enthalpy.out:13`. The NN residual is stable under a fourfold reduction in finite-difference step. However, neither runner implements the full logarithmic LCP counterterm; “zero under full LCP” is analytic extrapolation, not a numerical test. `scripts/r1927_lcp_enthalpy.py:46-50`; `scripts/r1927_nn_thermal_enthalpy.py:31-35,52-53`.

- **Lattice force:** Only the additional state-dependent force vanishes after cancellation. A general inhomogeneous \(F_0(n)\) still exerts the ordinary lattice-medium force. `scripts/r1927_identities.py:68-82`; `R19-27_report.md:112-117`.

- **Per-site completion and fixed reading:** It is a legitimate conditional scalar-EFT completion and need not add a new freely fitted continuous parameter once the physical renormalization data are counted. It is nevertheless new functional law data. More importantly, it makes \(\Delta W=0\); it prevents the mismatch rather than providing a receiver for a nonzero mismatch. Therefore the literal fixed reading is **OPEN**, not V1-RECEIVER. `TESTS.md:8456-8459`; `R19-27_report.md:160-165`.

- **LI scheme:** The D1 arithmetic—\(2.13\times10^{51}\) vev drift per e-fold at Planck spacing—is confirmed. Its promotion to a universal V1 exclusion is not: the collider and clock inputs are recalled, and the result is conditional on the D1 odd-power coefficient and Higgs identification. `scripts/r1927_lcp_enthalpy.out:31-34`; `R19-27_report.md:39-42`.

- **R19-21/C-box-E:** Its D1 number and (d-i) cancellation remain correct for the LI-counterterm completion. If P-R19-27a is separately adopted in C-box-E, the power-divergent state-dependent enthalpy is absent before (d-i) acts. Thus R19-21’s one-point mismatch is completion-dependent; its shear claims are unaffected. `C5_R19-21_report.md:214-244`.

**Strongest correct statement:** For an isotropic local V1 term, \(W=nF_n\), the label-field source cannot directly receive the energy leg, and \(\dot\rho+3HW=F_\phi\dot\phi\). In the specifically stipulated small-\(m\ell\) scalar/D1 completion with site-density-dependent bare counterterms following an exact LCP, the leading D1 and NN \(O(\lambda)\) state-dependent enthalpy terms cancel without an additional fitted continuous parameter. This is a new conditional law completion—not a receiver derived from V1—and it prevents the registered mismatch from arising; it is not proved for every BO or full-SM state. Hence R19-27 is **OPEN**, while the LI-scheme drift remains a large but conditional warning.

Full referee record: [R19-27_referee_verdict.md](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R19-27/R19-27_referee_verdict.md:1>)