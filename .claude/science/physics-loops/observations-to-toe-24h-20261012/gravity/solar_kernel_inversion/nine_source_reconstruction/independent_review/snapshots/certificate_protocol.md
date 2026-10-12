# Exact check of the frozen finite linear programs

Parent protocol written after the six nine-source fits and field checks, before
the dual calculations. All nine galaxies are exposed development data. No
candidate, response knot, target, source map, bound, or fitted weight is changed.

Reconstruct each of the six original primary matrices using the frozen source
and target arrays and unchanged components. Save every matrix and bound as
binary64 hexadecimal values, with row labels and hashes. Rerun only the original
primary objective to obtain proposed dual multipliers. This calculation checks
the finite LP, not observational independence or a continuum field theorem.

For min c.x with A.x <= b, x=(w,t)>=0, c=(0,...,0,1), and sum(w)<=100,
convert all matrix entries and proposed multipliers to exact rational numbers.
Clamp any positive multiplier to zero. Rescale the resulting y<=0 downward,
if needed, so (A^T y)_t<=1 exactly. Define

    delta = max(0, max_j<20 ((A^T y)_j-c_j)).
    L = y.b - 100 delta.

Then every feasible point obeys t>=L: y.A.x>=y.b, the remaining t coefficient
is nonnegative, and each remaining weight coefficient is at least -delta.
This uses the explicit weight cap. It remains valid when rounded dual weight
constraints miss exact feasibility. Store exact rational y, delta and L;
print only downward-rounded lower bounds as certified decimal claims.

Preserve all six certificates even when numerical field gates failed for a
selected primal vector. A finite-matrix certificate does not repair that gate.
The galaxy-only matrix does not involve E; its bound therefore also applies
when constraints on E or the solar quadrupole are added to this same matrix.
This does not extend it to another baryonic map, response basis, weight cap,
readout, or exact continuum projection. The solar-bound floating inputs are
not independently certified measurements or exact continuum kernels.

Inspect the nonzero dual rows to identify which fixed inputs force the residual.
This is a post-result diagnostic, not a preregistered observation prediction.
Create a standard-library verifier which reads the saved certificate and matrix,
uses rational arithmetic, and does not call the fit or numerical optimizer.
Request a focused independent derivation and reconstruction check. No broad
theory exclusion, statistical significance, or retained-grade verdict is claimed.
