## VERDICT: NOT CONFIRMED

The numerical RP negatives are confirmed, but the measure-legitimacy premise is not. Full record: [REFEREE.md](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_NT1/REFEREE.md:3>).

1. **Measure:** Weyl projectors, chirality conventions, and determinant factorization are correct. Gauge invariance is numerically convergent, not exact at finite transport resolution. The cumulative current has not been shown to satisfy the locality, symmetry, and global-integrability conditions required by the Lüscher reconstruction theorem. The anomalous L1 model is gauge-restored equally well, exposing this gap. [Finding](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_NT1/REFEREE.md:137>) See also [Lüscher](https://arxiv.org/abs/hep-lat/9811032) and [Kadoh–Kikukawa](https://arxiv.org/abs/0709.3656).

2. **Reflection lemma/sign:** Correct for a separating class of witnesses; one finite pool alone does not prove the converse. The F3 sign correction is sound. No allowed global sign or phase can make the final indefinite kernels PSD. [Finding](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_NT1/REFEREE.md:141>)

3. **Eigenvalues:** Confirmed on all four pools. Independent full-kernel polar-overlap rebuilds agree with the saved kernels within \(1.6\)–\(3.3\times10^{-14}\), including \(n=16\rightarrow32\) stability. The error estimate is empirical because higher-level transport checks sample only 24 entries, but the signs are numerically overwhelming. Witnesses are exactly W-matched and admit gauge-invariant bump realizations. [Finding](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_NT1/REFEREE.md:179>)

4. **Chiral = modulus:** The factorization
   \[
   |\rho_{11112}|=C|\det D(1)|^2|\det D(2)|^{1/2}
   \]
   is confirmed. Phase constancy also occurs for anomalous L1 and isolated L2/R2, so it is special to this restricted \(L_x=2\), open-time, W-matched sector—not a generic property of chiral measures. What is genuinely new beyond K2c is non-RP of this fractional-power modulus, not a chirality- or anomaly-specific mechanism. [Finding](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_NT1/REFEREE.md:255>)

5. **Fixed reading:** The numerical inequality required by `CHI-RP-FAIL` is met, but the legitimate-measure setup gate is not. Therefore the strict reading is OPEN / NOT CONFIRMED. Scope remains \(L_x=2\), open time, finite 2D U(1), with anomaly cancellation’s locality role untested. [Finding](</private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_NT1/REFEREE.md:297>)

**Strongest correct statement:** On the tested finite \(L_x=2\) open-time lattices, the worker’s numerically gauge-restored 11112 prescription produces a Hermitian kernel equal within transport error to the kernel of \( |\det D(1)|^2|\det D(2)|^{1/2} \), with independently reproduced negative eigenvalues from \(-5.309\times10^{-3}\) to \(-1.143\times10^{-2}\). This robustly extends K2c to that fractional-power overlap modulus, but does not yet establish RP failure for a legitimate local anomaly-free chiral measure.

No `REFEREE_VERDICT.md` was created.