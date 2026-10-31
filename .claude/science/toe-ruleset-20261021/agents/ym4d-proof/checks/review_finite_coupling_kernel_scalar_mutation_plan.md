# Additional post-exposure scalar-term probe

The seven initial executable substitutions all exited nonzero. Contrary to
the preregistered expectation for `double_cubic`, that copy is detected:
the opposite-parity expression contains the original coefficient explicitly.
This result is preserved; no earlier result is relabelled.

The author Weyl-integral routine tests its nonzero complex lambda sample by
grid convergence only. A distinct implementation error may therefore survive:
replace its scalar odd phase `+1j*lam*sin(angles).sum/3` by zero while retaining
all grids, inputs and assertions. This substitution must be recorded as a
survivor if all 35 checks still pass. No pass is inferred in advance. It is
not a theorem falsifier: the source's analytic cubic calculation and the
independently frozen Fourier-determinant lambda-derivative check directly
test this term. A zero-lambda integral would give derivative zero, missing
the independent target `-10/3` by more than3.

Use an owned result-path copy and the unchanged gated launcher. No thresholds,
author files, original logs or earlier reviewer evidence are modified.
