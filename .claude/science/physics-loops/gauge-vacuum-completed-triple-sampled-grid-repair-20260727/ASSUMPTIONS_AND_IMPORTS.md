# Assumptions and Imports

The primitive-registry check found no registered framework primitive used by
this finite runner predicate. In particular, scale reference, kinetic
isotropy, and realized-state specialization are not premises of this claim.

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| `Z^min` from `completed_sector_data()` | Target vector | computed lattice input | rank-one transfer helper | yes | yes | Primary runner checks it against the note to `10^-12`. | checked |
| `spatial_pair`/recurrence machinery | Produces each witness vector | retained support | helper-runner chain declared in `AUDIT_INPUT_PATHS` | yes | yes | Dependency-aware cache fingerprint plus live execution. | checked |
| Float64 evaluation | Defines the numerical predicate | admitted normalization | NumPy implementation in primary runner | yes | yes | Exact/interval arithmetic would support a stronger successor claim. | explicit scope ceiling |
| `10^-6` numerical-zero threshold | Defines pass/fail for the finite numerical claim | admitted normalization | primary runner and source note | yes | yes | Replace with interval enclosure only for a stronger exact claim. | explicit scope ceiling |
| Empirical Lipschitz constants | Archived continuous-box scouting | support-only | continuous-box runner | no | no | Analytic or interval-certified derivative bounds. | excluded |

## Counterfactual pass

| Assumption | What if it is wrong? | Concrete alternative | Direction it opens | Feasibility | Score |
|---|---|---|---|---|---|
| The claim is about the explicit grid. | Demand every continuous parameter value. | Interval subdivision with certified enclosures. | Stronger continuous no-go. | live but outside this short repair | 2 |
| Float64 values define the reported predicate. | Demand exact sampled-coordinate non-equality. | Validated interval matrix functions at all 1440 tuples. | Exact finite-grid theorem. | live, new infrastructure | 1 |
| `c` is optimized analytically. | Treat `c` as another grid parameter. | Direct scalar sweep. | Weaker and less exact than projection. | falsified by projection formula | 0 |
| The target helper is current. | Allow target drift. | Hard-code an independent exact target construction. | Provenance cross-check. | already checked numerically | 1 |

Selected route: keep the finite numerical claim and make its domain,
projection, target, threshold, and cache provenance executable. The two
stronger interval routes remain explicit future work.
