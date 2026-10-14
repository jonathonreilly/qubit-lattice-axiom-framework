# VERDICT: CONFIRMED WITH CORRECTIONS

The fixed TW-2 reading is **SPLIT-SAFE**.

1. **First-order coupling:** Confirmed for the stipulated one-loop \(U=1\), Psym law. The \(D_4\) symmetry forbids the \(B_1\) linear response but permits the tetragonal \(A_1\) response (`TW2_report.md:166-175`). My independent integral gives \(B'=-0.0454159364\) and light-twin leak \(+0.0454159402\,\sigma e^2t\); the longer symbol gives \(+0.00263580\,\sigma e^2t\) (`referee_tw2_independent.out:3`).

2. **Fixed wording:** SPLIT-SAFE is correct because the plain question and probe (b) explicitly pre-register the additive-mass **Hessian** (`TESTS.md:9633-9639`). Including the subsequently discovered first derivative would change the frozen scope. Physically, however, the minimal branch is clock-hazardous.

3. **Folding, legality and \(T_1\):** Confirmed. Independent null-space calculation finds no one-bit/nearest-neighbour ordinary taste-split mass; the first such masses occupy the face-diagonal classes (`referee_tw2_algebra.out:2-3`). The exact \(4+4\) projectors commute with the stipulated law to \(3.2\times10^{-16}\) (`referee_tw2_algebra.out:4-6`). The triplet has the \(T_1\) characters and no invariant vector (`referee_tw2_algebra.out:7-8`). The epsilon-odd nearest-neighbour triplet exists, but needs a body-diagonal singlet to split mass magnitudes. Also, body-diagonal symmetry forbids only the derivative at zero—not exact finite-strain evenness (`scripts/tw2_sigma8_N32.out:14-17`).

4. **Second order:** Confirmed independently:
   - Minimal: \(L''_{E_g}=0.1237817\), \(L''_{\rm tet}=0.0380123\).
   - Longer symbol: \(L''_{\rm tet}=0.0072309\).
   
   This gives \(8.28\times10^{-11}\) of the Earth row and \(4.63\times10^{-14}\)–\(6.18\times10^{-13}\) of the clock row (`referee_tw2_independent.out:3-5`).

5. **Clock arithmetic:** Confirmed under the packet’s assumptions. I obtain \(d\ln m_e/dt=0.467264\), \(d\ln m_p/dt=0.308207\), and net \(-0.159057\), producing ×4.693–17.814; the longer symbol gives ×0.272–1.034 (`referee_tw2_independent.out:6-9`). The net is sensitive because the electron and proton pieces separately give ×13.785 and ×9.093 and partially cancel. Couplings, partner masses, axes, and slope estimator therefore materially affect the result.

6. **Other corrections:** Pairing three generations into two-taste fields forces fourth partners, but “one vector-like family” is supplied model content, not forced by counting. The Hamming reading also does **not** force grid-scale splitting: its theorem leaves \(\lambda\) supplied and uncalibrated; \(\lambda=0.1\) is merely the worker’s sampled grid-scale case. An e–μ calibration would instead give \(\lambda=4.306\times10^{-21}\) (`referee_tw2_algebra.out:9`; prior theorem `:46-50,174-182`).

**Strongest correct statement:** On the stipulated face-diagonal one-loop law, the taste split is a direction-selecting \(T_1\) bilinear with an exact two-block reduction and independently confirmed \(B'=-0.04541594\). Its pre-registered Hessian leak is safely negligible, so TW-2 is literally SPLIT-SAFE; nevertheless, the same symmetry breaking permits an additional linear leak that conditionally exceeds the clock row by ×4.7–17.8 for the minimal symbol, while a longer legal symbol is only borderline. This is a serious branch-dependent hazard—not a family-wide theorem—and remains conditional on an axiom-noncovariant fixed direction, the off-shell one-loop/SM mapping, and estimated couplings and partner content.

Full record: [TW2_referee_verdict.md](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/ref_TW2/TW2_referee_verdict.md:1>). Independent runs peaked at 187 MB and 35 MB RSS.