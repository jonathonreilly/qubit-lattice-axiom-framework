# Route Portfolio

| Route | Type | Score | Hard-residual pressure | Outcome |
|---|---|---:|---:|---|
| Factor typed bridge into selector and sign switches | no-go/obstruction | 3 | 3 | selected |
| Prove connected selector `kappa=0` | constructive theorem | 2 | 3 | deferred |
| Prove endpoint orientation `sigma=-1` | constructive theorem | 2 | 3 | deferred |
| Re-run typed graph no-path | no-go/obstruction | 1 | 1 | not selected |

Selected route: classify the minimal bridge ansatz
`c_TE = sigma * R_phys(kappa)` and solve the target exactly.  This narrows the
bridge from one vague missing edge into two explicit theorem targets.

Stuck fan-out:

1. Color support: `F_adj=8/9` is exact but positive.
2. Connected-selector frame: `kappa=0` is not derived by the Rconn repair.
3. Orientation frame: `sigma=-1` is not derived by the Route-2 endpoint bank.
4. Endpoint algebra frame: both switches together force `rho_E=21/4`.
5. Physical selector interval: the target has only the `sigma=-1,kappa=0`
   solution in the physical selector line.
