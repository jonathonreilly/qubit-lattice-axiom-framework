# Focused independent implementation and numerical review

I found no material implementation discrepancy in the frozen first run. The
recorded covariant forces, energy exchange, vacuum modes and complete tracking
and disturbed-history outputs agree with independent calculations. All four
deliberate omission mutations are rejected by the existing off-trajectory
controls, including a restoring-force omission that is invisible on the exact
u=0 trajectory. No author source change is requested by this review.

This confirmation is numerical and source-bound. The global homogeneous
future-attractor theorem remains the separately reviewed mathematical
argument. Neither that theorem nor these numerical fixtures establish a new
empirical fit, selection of the finite-time history, or general spacetime
stability.

## Exact source and input coverage

The independent stage first froze all twenty present parent source/context and
first-execution evidence paths. It then froze the exact upstream result used
for the imported photon calibration. The complete runner, fixtures,
calibration scope, freeze and execution records were read. The handwritten
proof review is reused only by its exact unchanged source identities.

| Principal input | SHA-256 |
| --- | --- |
| check_analytic_fluid_v1.py | d247f6dc0143d2548a46c59abaec09cb2521c03fe3de73691a5f1f85293c41ef |
| NUMERICAL_FIXTURES_v1.json | 24ea85efb6725a97b10ac1618b1ebe1a4a02aef50d9799dc91d836877200a1c9 |
| CALIBRATION_SCOPE_v1.json | c8eb905fe3cbf3e6b464a1d8dcb11f8078e47af49b6a173cd0cebbd59a74e9ae |
| evidence_v1/RESULTS.json | 82e04b99fcc878d267a7c82ec92d9aeb238015cc65f98947ecd60fb6cf274160 |
| Upstream radiation RESULTS.json | 8c0bb51294f924530c5068b61fda0ebfca8818870fea0cb68556381faed01fe7 |

All seven declared execution inputs agree across the before-run freeze, the
parent's source snapshots, the result's source-hash map and the independently
captured current sources. The parent freeze precedes the first execution;
the recorded run lasts 37.8002 seconds, exits 0 and records 1492 passing checks
with no failures. The independent reader verified all 1492 records and their
applicable numeric tolerance arithmetic. The actual source/evidence bytes,
rather than a campaign HEAD or a later version, define this review.

`SOURCE_DISPOSITIONS.json` supplies exact source/snapshot recovery paths and
coverage for every captured input. `RECEIPT.json` binds this report, the full
independent recipe, executed reviewer sources, results and all failed mutant
evidence. Only `independent_numerical_review/` was written. No parent file was
edited and no Git, PR, formal audit or empirical fitting operation was run.

## Independent results

The derivation and reproducible procedures are in
`INDEPENDENT_NUMERICAL_RECIPE.md`. No parent helper is imported for positive
evidence. The main results are:

| Result class | Complete coverage | Independent result |
| --- | --- | --- |
| Covariant forces and exchange | 72 fixtures, all components | Hamiltonian differentiation at 70 digits agrees with both stored force implementations; maximum normalized force discrepancy 6.67e-16. |
| Free vacuum modes | 25 rows | 80-digit oscillator power series agrees; maximum absolute mode difference 1.39e-16; critical nu=9/4 included. |
| Exact tracking | 12 independent evolutions compared with all 24 author runs and all 12 sites | Maximum state difference 3.30e-10, or 0.001441 tolerance units. |
| Disturbed histories | 48 independent evolutions, both author formulations, all 61 sites | Maximum state difference 1.08e-12 against N evolution and 6.35e-12 against proper-time evolution. |
| Proper-time quadrature | All 48 histories and 61 sites | Maximum difference 2.10e-12. |
| Energy | All recorded histories and sites | Recomputed identities, floor, sampled monotonicity and cross-formulation values agree. |

The high-precision force route starts with canonical energy
E=sum pi_i^2/(2K_i)+V+sigma+r and differentiates it at fixed momenta. It
reconstructs the proper-time force and pulls it into N coordinates. This
avoids an explicit copy of the parent's connection formulas. It checks all
recorded K, V, potential-gradient, metric-derivative, H, H_J, conservation and
acceleration values, as well as the exchanged-energy cancellation.

The independent nonlinear solver evolves canonical momenta in N and
eliminates dust and radiation differential variables through their exact
number/conservation laws. It uses Radau, rather than either of the parent's
integrators. Invertible reference scales condition the large tracking fields
from z=10^6 to N=6; the fields and momenta remain independently dynamical.
The disturbed system also integrates dt/dN=1/H, allowing an independent
proper-time comparison without the parent's root-finding procedure.

All solver settings were written before execution. Every comparison uses the
original frozen tolerances; none was loosened to produce agreement. The
largest tracking H^2 discrepancy is only 2.76e-6 tolerance units. Raw absolute
H^2 differences at the earliest redshift are inappropriate standalone error
measures because the dimensionless H^2 is enormous there; normalized
comparisons are retained in `COMPARISON_METRICS_v1.json`.

The independent row/identity/force/mode reader reports 15,068 passing checks.
The separate Hamiltonian evolution reports 470 passing checks. These counts
include coverage and arithmetic checks; they are not numbers of independent
experiments. All sources, exact outputs, execution receipts and empty stderr
streams are preserved. No unexpected reviewer execution failed in this stage.

## Deliberate failures and oracle sensitivity

Each mutation changes a source copy under the review directory and runs only
the parent's frozen off-trajectory controls. These executions test whether
the original controls reject an incorrect implementation; they are not used
as independent positive evidence. Every changed source, full result, exact
patch, fixture and nonzero return is preserved.

| Actual source-copy mutation | Numeric failures | Largest tolerance violation |
| --- | ---: | ---: |
| Omit metric connection in N acceleration | 60 full-KG checks | 3.96e8 units |
| Omit dust mass exchange | 48 conservation checks | 2.39e6 units |
| Omit scalar matter force | 48 full-KG checks | 5.70e8 units |
| Omit u(4x^2+nu) restoring force | 60 full-KG checks | 2.70e9 units |

All four executions exit 1 because actual assertions fail, not because the
harness crashes. In total, 216 failed assertions remain preserved. The final
omission vanishes on the exact u=0 tracking trajectory, so its rejection
directly demonstrates that the full off-trajectory checks detect this form of
exact-trajectory blindness. Zero-density or zero-velocity fixtures do not
detect terms that vanish there, as expected. This is targeted sensitivity
evidence, not an exhaustive claim about all possible defects.

## Calibration and interpretation boundaries

The calibrated Omega_gamma=5.046740289227271e-5 matches the central thermal
row of the exactly pinned upstream radiation result. The current fixture
uses that value as exposed input. The stated G_N=(1+a)G_* bridge, H0=70,
m=0.3, photon temperature, H_v normalization and initial amplitudes are
supplied assumptions or prior calibration. Their roles are explicit in
`CALIBRATION_SCOPE_v1.json`; this review confirms the import and algebra, not
a new likelihood or local measurement validation of the action. The scope
remains photons only, with no inferred neutrino sector.

The disturbed runs are finite-interval comparisons through N=12. Some have
not reached the vacuum to machine precision: the largest recorded final
energy excess above 3/2 is about 3.43e-5, reproduced independently. This is
consistent with slow decaying modes and must not be replaced by a claim that
all finite histories have already reached the vacuum. The mathematical
attractor proof concerns the infinite future under its stated homogeneous
assumptions, and it does not select the observed finite-time trajectory.

The original handwritten repeated-root and frame qualifications stay fixed
in the prior review. This stage finds no new implementation correction and
does not promote the candidate to a broader scientific status.
