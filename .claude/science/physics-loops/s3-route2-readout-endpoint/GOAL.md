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

Block14 target: test whether a positive `O_h` channel metric on `E (+) T1`
derives the missing `lambda = q_E/q_T = 9/4` factor.
