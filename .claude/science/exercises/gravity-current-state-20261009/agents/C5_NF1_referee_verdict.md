# VERDICT: NOT CONFIRMED

The central symmetry result is confirmed, but the fixed reading must be **OPEN**, not **NF-TASTE-WALL**.

1. **\(U(1)_\epsilon\):** Failure confirmed. Continuous time requires \([\epsilon,h]=0\), while the staggered law has \(\{\epsilon,h\}=0\); independently, \(\|[\epsilon,h]\|/\|h\|=2\). (`NF1_report.md:124-127`; `ref_nf1_checks.out:2`)

2. **\(\Theta\), \(P_{\rm stag}\), and all 64 entries:** Confirmed. Their simultaneous constraints have rank 64 and nullity zero; independent direct \(8\times8\) integrations give every entry below \(2.7\times10^{-17}\). However, \(P_{\rm stag}\) requires an inversion-covariant link lift—not literally any c-number functional. (`NF1_report.md:129-142`; `ref_nf1_checks.out:3,6-9`)

3. **Flow compatibility:** Confirmed for every uniform symmetric strain. Independent generic off-diagonal testing gives zero inversion-oddness error and \(8.9\times10^{-16}\) π-shift error. Nonuniform strain remains outside scope. (`NF1_report.md:117-122`; `ref_nf1_checks.out:4-5`)

4. **Controls and residual:** Confirmed. Both ε-breaking controls are nonzero; the ε-respecting dressing remains zero. The reported \(z''=+1.139\times10^{-2}e^2\) and Earth ratio \(1.3\times10^{-13}\) are confirmed as the conditional, off-shell \(P=0\) estimator. The zero critical-mass knock-on and vanishing linear \(c_1\) channel hold only on the native symmetric branch. (`scripts/nf1_conv_B_240.out:2-5`; `scripts/nf1_conv_C_240.out:2-4`; `scripts/nf1_conv_M_240.out:7-10`; `NF1_report.md:194-198`)

5. **Taste count/R9-1:** The two-Dirac-taste count and \(22.5/2=11.25\) obstruction are correct. A twin electron gives the quoted 36.5-width-error discrepancy only conditional on an identical electroweak/Z coupling and Dirac sea, which NF-1 does not construct. T2 is untested, not “not excluded”; its required taste splitting breaks \(\Theta\) and leaves the exact-zero class. (`NF1_report.md:202-229`; `C5_R9-1_referee_verdict.md:8-9`)

6. **Re-solve:** The reduction to three rows is structurally correct, but the worker divided the fermion rows by four twice. Corrected \(N=48\) roots survive for \(N_s=11.25\) and \(16\), with substantially different parameters; the claimed \(N_s=22.5\) root was not reproduced. “Only at” the small-box photon edge was not established. (`scripts/nf1_rows.py:43-65`; `scripts/nf1_solve3.py:17-32`; `ref_nf1_resolve_N48.out:2-11`; `ref_nf1_resolve.out:12-16`)

7. **Fixed reading:** **OPEN.** The frozen probe explicitly asks whether \(U(1)_\epsilon\) is exact. It is not, so the `NF-ZERO` antecedent of `NF-TASTE-WALL` fails; `NF-BROKEN` also fails because the Hessian is zero. (`TESTS.md:9448-9473`; `NF1_report.md:257-269`)

**Strongest correct statement:** On the native massless staggered law, continuous \(U(1)_\epsilon\) is absent, but—in any symmetry-covariant regulator and link lift—the discrete pair \(\Theta\) and \(P_{\rm stag}\) forces all 64 entries of \(\Sigma(0,0)\) to vanish at every perturbative order, eliminating the additive strain mass, critical-mass knock-on, and Wilson-linear \(c_1\) channel while leaving a tiny multiplicative residual. The price is two identical tastes and a genuine SM count/degeneracy problem; proposed taste splitting breaks the protection and is uncomputed. Because the immutable test names \(U(1)_\epsilon\), the correct fixed result is **OPEN**.

Full record: [C5_NF1_referee_verdict.md](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_NF1/C5_NF1_referee_verdict.md:1>)