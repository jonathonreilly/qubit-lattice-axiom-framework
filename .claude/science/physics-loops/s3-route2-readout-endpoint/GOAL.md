# Goal

Run the physics loop on the S3/Route-2 readout endpoint triple. Attack the
theta-to-slice coupling/readout endpoint from first principles, trying to
derive or sharply constrain

```text
(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E)
= (-1, -2, 21/4).
```

Do not audit or apply verdicts. Make review PRs for coherent science blocks,
do not push to `main`, do not refresh existing PRs to `main`, and do not check
PR conflict state. The reviewer will cherry-pick science from the PRs.

Block16 target: direct consumer support for `s3_time_theta_to_slice_coupling`
by localizing exactly how unresolved `rho_E` propagates through the conditional
theta-to-slice family.
