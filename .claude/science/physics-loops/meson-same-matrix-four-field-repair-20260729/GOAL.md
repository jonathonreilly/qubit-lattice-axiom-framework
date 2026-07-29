# Goal

## Exact target contract

**Target statement.** On each finite carrier and gauge configuration listed in the
meson note, compute the connected four-field Berezin/Wick minor
from the same finite staggered matrix whose determinant weights the gauge average, and
show that it agrees with the independently evaluated analytic trace kernel both at
fixed background and after the determinant-weighted finite average.

**Quantifiers/domain.** The four deterministic U(1)/SU(3) carriers, samples, and
quadratures in the primary runner; `m=0.5`, `NT_BULK=14`, open finite temporal chain,
and the note's Wilson-line meson basis.

**Allowed premises.** The displayed finite staggered action, ordinary finite Gaussian
Grassmann integration/Wick determinants, the explicit reflection convention and
two-step finite kernel, and the linked staggered determinant-positivity
dependency.

**Forbidden weakenings.** Reusing an `Lt=2` determinant with an `Lt=28` kernel;
expanding the reduced trace and calling it a direct four-field calculation; comparing
only spectra while omitting temporal eigenvectors; or dropping determinant weighting.

**Required edge cases.** Both cross-reflection orientations, reflection sign,
`C_BLOCK=2` normalization, eigenvector/isometry identification, determinant phase,
degenerate minimal carrier, mixing carriers, and gauge transforms.

**Completion witness.** SHA-pinned runner stdout with all same-matrix checks passing,
plus a source note that displays the explicit `2 x 2` Wick minor and its connected
subtraction.

**Non-closures.** Propagator-only agreement, same-loop consistency, a flat gauge
average, or an unsupported operator-Hilbert-space interpretation do not close this target.
