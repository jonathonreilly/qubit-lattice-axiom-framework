# VERDICT: NOT CONFIRMED

The calculations support a conditional `M + V0 + SF` joint zero, but not the claimed setting-level **LIFTED** reading. The correct reading is **OPEN**.

1. **Theorem DT — confirmed conditionally.** Independent finite-\(q\) evaluation agrees with the formula to \(2.7\times10^{-9}\). It additionally requires an ultralocal seagull. V0 and SF are explicitly stated and usable stipulations, but are not derived from one Belinfante lattice action (`R16-13_report.md:84-97,138-160`; `R16-13_referee_checks.out:37-42`).

2. **Signs — confirmed for D1 versus G, not universally.** Independently:
   \[
   D1:(+5.4601{\times}10^{-3},+2.8291{\times}10^{-3},-2.9185{\times}10^{-2}),
   \]
   versus
   \[
   G:(-1.6892{\times}10^{-3},-8.4891{\times}10^{-4},+4.3384{\times}10^{-3}).
   \]
   The worker’s signs are correct; its \(\mu_E\) magnitude is about 1% underconverged (`R16-13_report.md:181-202`; `R16-13_referee_checks.out:22-26`).

3. **\(T_{2g}\) shear mass — confirmed.** The shared Wilson mass gives \(H_{xy}=W'_xW'_y\), defeating the separable Liouville zero. Explicit values are nonzero, including \(\mu_{T2}=-3.53\times10^{-5}\) at the joint root. This invalidates R16-9’s coupling-specific zero row, though \(H_{xy}\neq0\) alone is not a universal nonvanishing proof (`R16-13_report.md:171-174`; `C5_R16-9_report.md:218-225`).

4. **Joint zero — independently confirmed after retuning.** At \(m=0.01\),
   \[
   (b_2,b_f,r)=(1.740668966789,1.313474886012,0.572783392213),
   \]
   with higher-resolution residuals \((-1.93,-1.16,151.3)\times10^{-11}\) and Jacobian determinant \(6.75\times10^{-8}\). A separate \(m=0.001\) root also survives. All edges are subluminal. Corrections: the verification freezes the width fraction, not physical \(w_2\), and fixed-law mass drift is linear—not \(O(m^2)\)—because \(M=m+\sum W\) (`R16-13_report.md:233-250,265-266`; `R16-13_referee_checks.out:3-35`).

5. **Reading — OPEN.** The isolated wording at `TESTS.md:5610` is formally met by the three-integral exercise. But the governing setting imports the local R9-9/R13-5 lattice-stress prescription (`TESTS.md:5597-5599`). The only root violates that setting because it uses M on gapped G/Gw edges. Nonzero \(\mu_{T2}\) is not itself fatal to the literal clause; two scalar edges and non-SM counts instead leave the SM-like probe open.

6. **R17-4 Lemma M — confirmed and decisive.** Proper \(C_{2y}\) covariance and periodicity force a continuous \(T_{xy}\) amplitude to vanish at \((\pi,K_y,0)\), while M requires \(g(\pi)g(K_y)>0\). Therefore M has no absolutely summable local stress kernel on the root’s edges (`C5_R17-4_report.md:114-127`). R13-5 had already identified M-on-G as nonlocal (`C5_R13-5_report.md:168-180`).

**Strongest correct statement.** Under an ultralocal-seagull assumption and the stipulated V0 Dirac TT and SF strain responses, Theorem DT, the D1 opposite-sign example, Lemma V1, the Wilson \(T_{2g}\) shear mechanism, and a subluminal codimension-three axial \((\Xi_{T2g},\Xi_{Eg},\mu_E)=0\) are reproducible at separately tuned light masses. This does not lift R16-9 in the registered local-stress setting: the only root uses a nonlocal scalar M amplitude, \(\mu_{T2}\) remains nonzero, and neither one-Higgs-edge nor SM-count content is reached. The full result remains **OPEN**.

Full record: [R16-13_referee_verdict.md](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R16-13/R16-13_referee_verdict.md:1>) · [independent checks](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R16-13/R16-13_referee_checks.out:1>) · [root runner](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R16-13/referee_numeric.py:1>) · [DT runner](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_R16-13/referee_dt_check.py:1>).