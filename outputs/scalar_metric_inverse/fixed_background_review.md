# Final focused fixed-action metric closure report

The compared root C1-C5 algebra is consistent with the fixed-background
equations on its equal-Einstein-potential branch. The revised canonical note
also correctly distinguishes that scalar reconstruction from the broader
local uniqueness of the actual matter slip J. No further mathematical
correction is requested within this focused scope. This is a research check,
not a formal audit or an empirical validation.

This report supersedes REPORT_v1.md's outstanding integration comments.
The earlier report, source snapshot and failed computation are preserved.

## Final source binding

| Source | SHA256 |
| --- | --- |
| Canonical note, final compared version | 1e3b1dbdd0f42ebee7a66ce6fd27aeb0c5702baa594438654b564a05f05f8c63 |
| Original root closure note | 419b98cad87d7c99ff3859326796e0e48fc5101a53d5ae1875e55c80556778f7 |
| Original root closure runner | 157d34a955fb2367cd523ddf760da6d27c803f6532d8160a23500949d9ee9b00 |
| Added root kernel integration note | 3a4024db3e426bba8ad7487c67ac0128823c2a51754de7655434ad3972fae803 |
| Added root kernel integration runner | cbd2ae623bdf2960c191d8cf2467c30e47507ca793527906158b67f67066fd7c |
| Canonical local-kernel helper | 12bd022f297d965c1c58ef87d118e14a02e64fb2fd473af5a67609db1c37d021 |

Exact absolute paths, byte counts and copied sources are in
AUTHOR_SNAPSHOT_v1.json and AUTHOR_INTEGRATION_SNAPSHOT_v1.json. The original
canonical snapshot had SHA 2151e6773f5cc2eee70c01fcb0964ec43d749feb37710435b30ddcabd9e86307.
CANONICAL_DELTA_v1.json preserves the exact change losslessly.
SOURCE_STATUS_v2.json found all 12 latest compared source/dependency files
unchanged at 2026-10-16T11:54:57.502304Z and all 15 pre-author frozen files
unchanged.

## Mathematical disposition

The independent pre-exposure route uses momentum, Euler, Hamiltonian and
bare-dust continuity to obtain radial transport and a Helmholtz equation for
Z=a Vv. A local radial exponential-polynomial argument excludes a zero-data
difference on an open observer-centered spherical annulus. It needs no
boundary value, real Fourier spectrum, center regularity, decay or nonzero
time derivative of the transport coefficient.

Absence of anisotropic stress alone leaves
chi=c0+c_i X_i+c2 r^2 on a local patch. Retaining this kernel and time-only
integration functions gives polynomial forcing in the two spatial equations.
The same argument forces Z spatially constant and J=Z_r/a=0. Therefore J is
unique in this broader local class. It does not establish uniqueness of every
scalar representation mode.

The revised targets, action convention and closure section now state that
root's explicit w reconstruction requires the equal-Einstein-potential branch
and fixed integrated-potential conventions. Full-sky recovered l>=2 sectors
remove the polynomial kernel; an arbitrary local mask does not. The added
kernel proof and planar full-action witness accurately reproduce the
independently frozen result with attribution. The canonical note explicitly
restores the units of R,kappa,h,q,x; the historical root wording is preserved
rather than silently edited.

Root's isolated D=0 derivative limit is valid because D_r=C/r^2!=0. The
post-exposure expression

    w=(r^2/C)(N_r-CN-Df)

also holds throughout r>0,C!=0. It trades the D denominator for another
derivative. Neither formula supplies a finite-noise stability bound.

The plane-parallel null solves all original linear equations but has nonzero
true radial redshift on an open angular patch. It identifies a geometry
boundary; it does not refute the spherical-annulus result.

## Evidence and independence boundary

The proof was frozen at 11:37:34.301099Z and the completed independent results
at 11:41:51.679109Z, before opening the new root closure source.
DERIVATION_BEFORE_AUTHOR_v1.md has SHA
d3b0f8120f4cb95ff973b3f47069afcaa7f0fd1cddc23a5c713da6622e98947e;
INDEPENDENT_OUTPUT_FREEZE_v1.json has SHA
8d8020527879601f1aafdad5c4b17e0eaeebc7e81f9e03231c30cd1a93ddb9cc.
Earlier action/mode equations and the known power background were acknowledged
context. All calculations share Python 3.12.8/SymPy 1.14.0.

| Execution | Actual result | Wall seconds |
| --- | --- | --- |
| Independent attempt 1 | 54 pass, 1 fail | 0.582 |
| Independent attempt 2 | 55 pass, 0 fail | 0.440 |
| New post-exposure correspondence | 27 pass, 0 fail | 0.609 |
| Unchanged root closure replay | 24 pass, 0 fail; byte-identical output | 0.646 |
| Unchanged root kernel integration replay | 23 pass, 0 fail; byte-identical output | 0.529 |
| Canonical helper correspondence | 4 checks pass; replays the same 23 controls | 0.534 |

Counts are not pooled as independent experiments. Every subprocess was bounded
at 120 seconds, with bytecode disabled and complete stdout/stderr/resource
records retained. None timed out.

The actual first failure was a SymPy comparison of equivalent cone derivatives
represented by different Subs objects. Both sides were subsequently pulled
back to independent eta,r after differentiation. The exact one-line change
is preserved losslessly in ATTEMPT_RECOVERY_v1.json; no physical equation or
tolerance changed. The original failed code and output remain intact.

Independent controls include the local kernel, the radial obstruction, an
all-chart Z formula, a growing spherical full-action fixture and the planar
null. Post-exposure controls additionally reduce the root trace coefficient,
test the arbitrary angular-jet identity, verify all six original Einstein-time
equations for the author's m=1/5,Y=143/85,k^2=728/75 witness
(delta/P=-6151/255), and recover the independent growing mode with root's
formula. The canonical helper's scientific AST is exactly equal to the added
root runner's calculation, and its complete returned checks equal the frozen
root receipt.

Copied replays are reproductions, not independent derivations. The older
check_metric_readout_v1.py and its receipt were only copied/read as declared
integrity dependencies; they were not executed. The primary canonical runner
and unrelated canonical helpers were outside this focused scope.

## Surviving obligations

The result assumes one fixed compatible homogeneous action/background,
a,R>0, b,x!=0, r>0, sufficient smoothness and an open time/radial/angular
neighborhood. A single ray, cone or isolated samples do not supply the proof.
Arbitrary P,Rz still require all original residuals; existence is not inferred
from the reconstruction alone.

The next scientific obligation is to establish calibrated primitive inputs
and a compatible background jointly, with controlled derivative errors and
the same pressureless dust velocity in the redshift channel. This check does
not select an action/background or derive the required distance/clock,
angular, null-time or tracer calibration. It establishes no measured scalar,
nonlinear stability, initial-state probability, absolute normalization or
prior-art priority. The full canonical note was read only for this closure
integration; its other blocks were not re-established.
