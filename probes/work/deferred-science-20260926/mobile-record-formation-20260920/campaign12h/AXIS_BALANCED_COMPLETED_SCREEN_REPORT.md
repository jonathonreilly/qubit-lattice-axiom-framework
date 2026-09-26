# Completed axis-balanced wave screen

2026-09-21. Fixed supplied rate parameters and predeclared simulation/analysis plan. This is finite-volume evidence, not a scaling theorem.

All eight planned cases completed, including the three L=64 stationary cases. Each stationary case used 256 independent paths. The source/seed-preserving continuation changed batch execution only; its bitwise control and scheduling receipts are retained.

The L=64 fitted speeds agree with the predeclared density-dependent speed within each of the nine conditional bootstrap intervals. Damping remains substantial: the first axial density minimum is about -0.49 to -0.61 instead of the Euler cosine value -1. Increasing volume improves the oscillation amplitude in every density case, but two sizes do not establish a limiting rate.

| Density | L | Predicted speed | Axial fitted speed [95% bootstrap] | Axial first-minimum correlation [95% bootstrap] |
|---|---:|---:|---|---|
| 0.25 | 32 | 0.250000 | 0.239634 [0.233059, 0.245909] | -0.3327 [-0.3870, -0.2789] |
| 0.25 | 64 | 0.250000 | 0.250420 [0.246593, 0.254252] | -0.5253 [-0.5757, -0.4737] |
| 0.50 | 32 | 0.408248 | 0.402778 [0.393246, 0.412542] | -0.3561 [-0.4097, -0.3053] |
| 0.50 | 64 | 0.408248 | 0.408579 [0.402286, 0.414507] | -0.6140 [-0.6789, -0.5509] |
| 0.75 | 32 | 0.433013 | 0.417300 [0.403487, 0.429558] | -0.2566 [-0.3029, -0.2117] |
| 0.75 | 64 | 0.433013 | 0.433622 [0.425844, 0.441516] | -0.4887 [-0.5423, -0.4354] |

The maximum relative speed discrepancy among the nine L=64 fits is 0.595%; 9/9 displayed intervals contain the predicted value. This is a descriptive comparison across correlated fitted observables, not a simultaneous confidence statement.

The fit uses a complex damped exponential over the first predicted half-period. Four thousand whole-trajectory bootstrap samples preserve dependence among times, fields and symmetry modes; one thousand are refitted. Directional shells are averaged within each path. Pointwise intervals describe sampling variation conditional on the fit and omit finite-size and model error. Raw correlation arrays and every bootstrap fit are available for alternate diagnostics.

All completed raw NPZ and metadata identities were authenticated. The maximum final Fourier reconstruction discrepancy is 1.28e-11. The exact conserved counts and birth bookkeeping remain in the raw audits.

The two nonstationary uniform-birth cases have a separate evolving-covariance analysis in GROWING_ANALYSIS.json; they are not folded into stationary speed fits. The native formation experiments use another generator and remain separate.

The plot is figures/axis_balanced_completed_screen.png (and PDF). Figure, analysis, fit, plan and raw input identities are recorded in figures/AXIS_BALANCED_FIGURE_PROVENANCE.json. No inferred parameter or target was changed after seeing these data.
