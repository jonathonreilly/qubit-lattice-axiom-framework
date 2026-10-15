# Scoped author comparison: exact coherent-link composition

Reviewer `/root/inertial_response_check`. This report follows the frozen
independent coherent calculation and its 61 controls. Neither the original
precheck nor its completed report/identity has been changed. The independent
result was supplied to the author before these new author sources were read.
This is a focused composition/source comparison, not a formal audit or a full
canonical-unit review.

## Exact sources and read scope

| Source | SHA-256 |
| --- | --- |
| Working exact derivation | `c4457b88521f426dde272db43cdee77712f5a8779764aef39823c5320e55cc99` |
| `coherent_exact_energy_v1.py` | `81dbec52ef73deb04aef25dee498a839f1e1f7664615cb8355e01a09d1aeb92f` |
| Working exact result JSON | `58885fa5ad2c05d9ad438e5461e4bc857a01a038da1eef43ff374f542803ea62` |
| Packaged exact helper | `6925adf6599f7df586810b4b6e7bae61368399953edb2a517cd492b3d422dc2f` |
| Canonical note, section 7 and normalization context | `72113d39011cd2a29beb3355edae2d122549f0369769fdb59b51594f48a9e711` |

I read the working note and both helper sources completely, the stored result,
and canonical section 7. I also read the canonical field/count conventions and
section 6 to resolve the turnaround normalization context. The full canonical
science-unit check is another reviewer's scope. Original working/canonical note
bytes are retained locally as `COHERENT_COMPARISON_ORIGINAL_*_v1.md`; saving the
full canonical bytes does not mean that its remaining sections were reviewed.

## Mathematics and implementation agreement

The author null-leg phase, compact force/clock weights, shifted common-arrival
amplitude and exact matrix agree with the independently frozen calculation:

    G = [[3064,-1871],[-1871,3064]]/(1620 pi).

The arbitrary initial positions and velocities are annihilated by exact zeroth
and first contrast moments. The shared station-clock anchor cancels, and an
independent spacecraft clock does not enter this specified instantaneous
coherent map. Both the direct-clock coefficient and the spacecraft force term
are retained. Its zero integrated direct coefficient removes a constant scalar
perturbation without selecting an absolute background or physical field state.

The positive-exponential branch used by the author is the complex conjugate of
my independent branch. Its particular displacement/clock signs and event
coefficients give the same real Gram. The `-1/2` factor in the absolute-distance
matrix is the correct radial half-line factor when that matrix is reported as
4 pi G. The zero sums justify using the finite difference of divergent cosine
integrals; the source correctly discusses regulating that finite combination.
Its exact positive determinant and eigenvalues are consistent with my matrix.

The time representation partitions all affine endpoint crossings, orders the
arrival intervals on each open angular segment, forms the total shared-field
amplitude there and integrates its polynomial products. Its endpoint values
have measure zero and cause no missing contribution. The spectral program uses
separate original harmonic events and exact absolute time differences. The
interior angular partition at -2/3 and 2/3 is complete for this fixture. The two
representations are distinct calculations; neither calls the other's Gram.

The omitted-clock and equal-coordinate variants have the intended meanings.
I independently reevaluated them with my already frozen overlap routine and
new explicit coefficient/lag inputs. Their changes in 4 pi G are exactly

    omitted clock: [[-344,166],[166,-344]]/135,
    equal coordinate: [[3848,-2557],[-2557,3848]]/405.

These checks confirm the documented differences, not a general rejection of
other physical link models. The final calibration paragraph is also correct:
exact nullspace cancellation cannot be inferred from a merely small numerical
leakage when its unknown amplitude is unbounded. Its conditional
M||(C-C_hat)^T t|| bound is the appropriate Euclidean Cauchy-Schwarz bound.

## Packaging and recorded outputs

The six calculation functions are exactly AST-identical in the working and
packaged helper. After removing only the working timestamp/output writes and
renaming main to run_checks, the complete driver AST is also identical. The
packaged helper adds AUDIT_TIMEOUT_SEC=180, returns its result, and prints only
when executed directly. No mathematical formula or assertion was changed by
that packaging. Canonical section 7 is exactly the working scientific body,
with the harmonic subsection heading moved one level deeper.

The saved working result is bound to its exact source and contains 15 checks.
All twelve algebraic residual entries are zero; the other three entries record
the positive determinant and two rejected variants. Its rational matrix,
determinant and decimals agree with the independent calculation. No complete
author suite was rerun. Eighteen narrow source/AST/recorded-result/variant
comparisons passed, as recorded in `COHERENT_AUTHOR_COMPARISON_RESULTS_v1.json`.
The new variant reevaluations use the independent overlap function, not either
author implementation. Original independent evidence remains intact.

## Narrow normalization wording finding

The matrix and code are correct for alpha*kappa=1. The note should explicitly
connect its displayed chi to that product normalization. In canonical section
6, chi_m is the phase perturbation before multiplication by kappa and the
normalized count is kappa times its endpoint difference. Section 7's chi also
omits kappa, consistent with that definition, but then calls the contrast a
count and says direct substitution in chi gives the displayed T, with no alpha
remaining. If alpha and kappa are not separately one, that final step requires
multiplying the contrast by kappa.

The precise clarification is: the unit-duration contrast being bounded is
kappa sum_j beta_j chi(t_i,j); the displayed W, c and T have already absorbed
alpha*kappa=1. Alternatively one could explicitly specialize both constants
to one, which would be a narrower premise. I sent the first clarification to
the author promptly. No matrix or code correction is needed. Any later text
repair should receive a separate affected confirmation rather than relabeling
this original source-bound report.

No other scoped discrepancy was found. No source, index, branch, campaign
state, lock, publication or raw observation was changed by this reviewer.
