# Focused independent tensor-scalar review

Reviewer: `/root/direct_field_check`. The parent remains the scientific author.
This is a source-bound mathematical and implementation check, not a formal
audit, retained-grade decision or new primary research block.

No material mathematical or implementation correction was found in the frozen
scope. The common action gives the stated weak static map and leading circular
source/readout relation

    R_circ=(1+a/6)/(1+a)=(7+5 gamma)/12,
    f_scalar=a/(1+a)=(1-gamma)/2.

This conclusion depends on the supplied Einstein action, positive constant K,
universal exponential matter metric, retarded weak point-source limit, zero
residual body sensitivities and adiabatic circular motion. It does not resolve
the origin of those premises or their empirical adequacy.

## Complete assigned source coverage

I read the complete protocol, reconstruction note, 253-line runner, source
ledger, results/scope note, claim-status certificate, trace gate, both freezes,
execution receipt and stdout/stderr. I read every result row: five exact
field-space cases, four metric-rank rows, 100 waveform rows, 20 flux rows,
15 lens rows, the angular refinement pair, orbit declaration, rational
rectangle and summary. Initially truncated tool output was reread in bounded
chunks so the missing rows were not treated as inspected.

All 13 original files were snapshotted byte for byte before substantive review.
`SOURCE_PINS_v1.json` records their complete hashes, sizes and recovery paths.
The executed source pins are:

| Source | SHA256 |
| --- | --- |
| `PROTOCOL.md` | `c53b53b2b000313cf9287cd39bfc5fc05b7f67aafd3f541bb8fb135fef4c6cf5` |
| `DIRECT_RECONSTRUCTION.md` | `fac07945fb9d7ab1341a3b93c6a2c67637764fe30345848a34a41846833deda3` |
| `check_reconstruction.py` | `1625124b0fd8df1b3432cccdc97ff9a07270d7aff8919d3617f3d97d463aad43` |
| `evidence_v1/RESULTS.json` | `b9cde6ce9ebb1b2dc6fa31ab104bcb602605baf31ec03491cd2b97b9062b2860` |

The results' three input hashes agree with the pre-execution freeze and actual
snapshots. The protocol freeze precedes execution; result creation precedes
the execution-finished record. The source ledger is later descriptive context,
not misrepresented as a frozen numerical input. The complete frozen Cartesian
row sets, reported row errors, aggregate maxima and printed summary were
independently checked in `RESULT_ROW_INTEGRITY_v1.json`.

## Mathematical findings

`INDEPENDENT_DERIVATION.md` contains the independent calculation, including
all load-bearing signs and factors. Its main checks are as follows.

1. **Variational signs and matter exchange agree.** The covariant-metric
   definition of T_* gives delta S_m/delta phi=alpha T_*/c. The scalar action
   therefore gives Box phi=-(4 pi G_*/c^4)K^{-1}alpha T_*. The divergence of
   the scalar Einstein-source stress cancels the specified matter exchange.
   A separate conformal stress/connection transformation gives the same
   identity. Nothing permits treating the bare Einstein-frame matter source
   as independently conserved.

2. **The complete metric mode count is consistent.** I derived the symbol
   from the Hessian of the Fierz-Pauli quadratic form, using non-axis null and
   generic, temporal and spatial off-null covectors. On nonzero null k the
   kernel has dimension six, with four gauge directions and two physical
   directions. Off-null it has only the four gauge directions. The TT action
   and positive scalar kinetic matrix give positive physical quadratic
   energies and the stated outward fluxes. This is not positivity of all ten
   unphysical components or a nonlinear matter stability theorem.

3. **The invariant and static/optical maps agree.** The field redefinition
   identity is exact for arbitrary invertible S. Positive K forbids negative
   a, independent of scalar count. The scalar Green-function sign gives an
   attractive contribution to weak massive-body motion; the conformal term
   cancels from the leading optical index. Thus G_N=G_*(1+a) and
   gamma=(1-a)/(1+a) use the same normalization. The fractions concern this
   restricted weak universal force only.

4. **The combined Newtonian source stress is essential and correctly signed.**
   I checked its local divergence and independently obtained its integrated
   pair interaction using derivatives of the inverse-k^4 Green kernel. The
   tensor and scalar near-zone terms combine into the given G_N stress, and
   their integral supplies I''/2. Removing that stress halves the circular
   tensor harmonic; reversing its sign cancels it. A direct orbital Fourier
   control detects both. The field terms cannot be omitted merely because
   the far-zone metric equation is evaluated to linear order.

5. **The retained scalar multipoles require the stated circular/body limit.**
   The leading mass monopole is constant and the leading universal mass
   dipole vanishes in the Newtonian COM. Corrections to the scalar monopole
   can compete with the quadrupole for generic motion. Conservative circular
   symmetry makes that integrated monopole constant here; its radiation
   reaction evolution is higher order. Corrected dipoles and other source
   moments enter beyond the retained circular order when residual body
   sensitivities are zero. The note explicitly assumes that condition rather
   than deriving it from constant masses. An eccentric or compact-body use
   would require new source terms and is not established by this block.

6. **The curvature, wave patterns and powers agree.** I constructed the
   linear Riemann components of h_TT+2 zeta eta in non-axis frames, obtaining
   the tensor plus transverse breathing tide. A conformal time-sign error
   creates a longitudinal tide and fails the control. Two charge insertions
   give a in the sourced detector amplitude, while the scalar energy norm
   gives a in the power. Independent angular moments recover 8 pi/5 for the
   TT projector norm and 8 pi/15 for the scalar contraction. They yield
   P_S/P_T=a/6. Comparing at the same G_N and trajectory supplies the
   additional factor 1/(1+a) in R_circ.

The theoretical field inventory is two tensor modes plus n scalar fields,
while the common weak source and physical metric expose one sourced scalar
breathing combination at this order. Arbitrary free scalar initial data lie
outside that sourced waveform. Numerical agreement at floating-point precision
does not bound neglected post-Newtonian, finite-body or detector corrections.

## Independent controls and their limits

The author runner was neither imported nor executed. My new checker uses
Fierz-Pauli Hessians, direct linear curvature, a differentiated Green kernel,
orbital Fourier moments, a 14-node degree-five spherical cubature, exact
rational sphere monomial averages and compactified Simpson ray integrals.
It does not call the author's operator, moment, projection, field or flux
helpers. The checker and its exact executed snapshot are preserved.

All 175 independent checks passed. Separately, all nine output/provenance
integrity checks passed. These counts include individual finite rows and hash
checks; they are not claims of 175 independent theories or proof obligations.

| Compared output | Independent method | Maximum difference |
| --- | --- | --- |
| All 100 normalized waveform rows | Fourier source moments and direct polarization contractions | 8.89e-16 absolute |
| All 20 tensor flux rows | 14-node sphere cubature of contracted TT norm | 3.56e-15 fractional |
| All 20 scalar flux rows | Same distinct cubature, scalar contraction | 2.23e-15 fractional |
| All 15 lens rows | z=b tan(theta), composite Simpson integration | 3.11e-14 fractional |

The analytic sphere identities are also verified exactly for a non-axis
trace-free matrix. The rational image of the prescribed rectangle is
a<=1/2499, f_scalar<=1/2500 and R_circ>=2999/3000.

Decisive false alternatives were checked: omitting or reversing Newtonian
field stress, changing the conformal time sign, omitting the G_* to G_N
calibration, doubling the scalar wave amplitude, and dropping the detector
charge insertion. Some are exact formula counterfactuals; the stress and
curvature changes are independently computed altered expressions. No mutated
author source was run, and no such execution is implied.

These numerical controls test the stated leading formulas. The Newtonian
stress and scalar-ordering arguments additionally rest on the explicit
derivation; the finite waveform rows alone do not establish source-body
closure. The original sphere refinement is a consistency check on a smooth
low-degree angular integrand, not a certified error bound for a full nonlinear
evolution or an actual binary waveform.

## Primary-source and observational roles

The known tensor-multiscalar action and normalization are consistent with the
[Damour–Esposito-Farese primary paper](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/DAMOUR/1988-1993/P_91_93/P_91_93_web.pdf).
The existing exact 8,134,643-byte PDF has the ledger's SHA256. I inspected
rendered PDF pages 8, 9 and 27 for the action, field equations and tensor/scalar
flux factors, and read page 23's extracted context. I do not claim to have
read the entire 97-page paper. The independent derivation above carries this
review, rather than importing the paper as an unexamined proof.

The [primary VLBA report](https://arxiv.org/html/0904.3992v1) supports the stated
published gamma and reported uncertainty. The wider rectangle is an author's
fixed development choice, not that paper's confidence interval transported
into this candidate. Its exact mathematical image is correct. No raw VLBA
data were fitted in this review.

The [GW170814 primary paper](https://dcc.ligo.org/public/0145/P170814/015/LIGO-P170814.pdf)
restricts its cited exercise to pure polarization models with a GR phase
model; it does not provide a likelihood for this mixed tensor/scalar source.
The [GW170817/GRB primary paper](https://arxiv.org/pdf/1710.05834v2) explicitly
conditions the propagation comparison on distance and intrinsic emission-lag
assumptions. Those source roles match the ledger. No published Bayes factors,
GR mass posteriors or timing interval were reused as candidate-specific
evidence. These materials were already exposed development context.

The narrow primary reads and the failed direct web opening of the IHES PDF
are recorded in `PRIMARY_READS_v1.json`. The exact existing local PDF was
used successfully. No statement of novelty, native Einstein-field emergence,
Standard Model completion, galaxy-fit inheritance or TOE is supported or
asserted here.

## Final source disposition

All original source bytes remain unchanged at review completion. The complete
13-row reviewer-owned `SOURCE_DISPOSITIONS_v1.json` records each original
path/hash, immutable snapshot recovery and final path/hash. No parent files
were edited and no Git mutation, PR action, formal audit, worker/model change
or delegated primary research occurred.

There were no failed scientific assertions in the independent run. The
initial output truncation and IHES web-access failure were resolved by bounded
reads and exact local recovery; both remain documented. The complete checker
stdout/stderr and executed checker bytes are retained. Newly authored text
ends in a single newline; immutable original snapshots and empty execution
stderr remain byte-exact.

The outcome is a checked conditional leading construction with substantial
explicit physical obligations still open. It does not authorize treating
compact-body sensitivities as solved, extending the circular radiation map
to eccentric sources, replacing detector calibration with an ideal-arm
formula, or claiming an independent empirical success.
