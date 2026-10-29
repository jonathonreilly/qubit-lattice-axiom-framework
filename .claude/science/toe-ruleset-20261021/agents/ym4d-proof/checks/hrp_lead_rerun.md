# H_RP exact checks: lead rerun outside the Codex sandbox (2026-10-29)

**Why this rerun exists.** REVIEW_HRP item 6 was a HOLD. The sandboxed runs could not set `nice` priority, so the runner stopped before computing anything. The reviewer's binding fix was to run the frozen runner under the original lock and resource rules in an environment that allows `nice`, then inspect the results. Claude Opus 5.5 (lead) performed this rerun.

**What was run.**
- The command was `sh checks/hrp_run.sh`, run unchanged from the ym4d-proof folder on the laptop.
- The script, launcher and criteria hashes are recorded in `checks/hrp_lead_rerun_hashes.txt`, captured before the run.
- The sandbox attempt's outputs were preserved first as `checks/hrp_attempt2_sandbox_*`.

**Preflight.** Load was 2.66 and free memory was 46%. The lock was acquired and released once, with `numeric_exit=2` and `cleanup_exit=0`. Elapsed time was 1.37 s and peak RSS was 25.9 MB.

**Results, from `checks/hrp_out.txt` and `checks/hrp_time.txt`.**
- **Positive checks:** all 25 Gram matrices are PSD and Hermitian, using exact rational Schur certificates.
  - Gauge groups: Z2, Z3 and Q8.
  - Reflections: link and site.
  - Configurations: 4x2, 3D sheets, zero coupling, direct Z2 enumeration, the full Z2 4x2x2 torus, and the K_a prism-cell models for Z2, Z3 and Q8.
  - Sphere geometry for R/a = 11/10 and 23/10: crossing counts are identical for all four coordinate reflections.
- **Negative control, negative crossing β:** a negative eigenvalue was detected, as pre-registered.
- **Negative control, asymmetric coupling:** this is a pre-registered criterion failure. The raw Gram matrix is non-Hermitian, and its Hermitian part is PSD. This matches REVIEW_HRP's hand algebra exactly.
- **Negative control, asymmetric cell:** this is also a pre-registered criterion failure. The raw eigenvalues are 1, 0, 0, 0, and the Hermitian part has eigenvalue −3/10. This matches REVIEW_HRP's hand algebra exactly, including the −3/10.

  Both of these fail the pre-registered "negative raw eigenvalue" criterion. Each still shows a genuine RP defect, one by non-Hermiticity and one through the Hermitian part. Neither is a counterexample to K_a. They are reported as failures.
- **Exit 2** is the runner's disclosed-control-failure exit. It is not an assertion failure or a resource failure.

**Status.**
- Item 6's execution fix is done.
- Item 7's binding wording fix is still open: the exact consumer statements in HRP.md §9.
- The independent reviewer has not re-inspected this rerun. The lead checked it against the reviewer's own predictions, and both control outcomes agree exactly.
- Every mathematical item (1–5) was CONFIRMED by the review.
