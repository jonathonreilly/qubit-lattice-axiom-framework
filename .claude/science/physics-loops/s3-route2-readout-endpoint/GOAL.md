# S3 / Route-2 Readout Endpoint Physics Loop

**Runtime request:** 12-hour physics-loop campaign.
**Active block:** block20.
**Branch:** `physics-loop/s3-route2-readout-endpoint-block20-20260621`

## Objective

Attack the `s3_time_theta_to_slice_coupling_note` readout endpoint triple from
first principles, trying to derive or sharply constrain

```text
(beta_T/alpha_T, alpha_T/alpha_E, beta_E/alpha_E) = (-1, -2, 21/4).
```

Do not audit or apply verdicts. Make PRs for coherent science blocks. Do not
push to `main` and do not refresh existing PR branches onto `main`.

## Block20 Target

Package the factor-rigidity / readout-primitive bridge split:

- preserve the exact factor-rigidity support statements for the time channel;
- isolate the local `delta_E` source of remaining `rho_E` dependence;
- prevent downstream consumers from citing factor-rigidity as a readout-map
  primitive-selection theorem.

