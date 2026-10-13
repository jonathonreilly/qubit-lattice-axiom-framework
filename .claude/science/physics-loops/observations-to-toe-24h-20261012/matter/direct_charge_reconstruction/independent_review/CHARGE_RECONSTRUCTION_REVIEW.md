# Focused independent charge reconstruction review

The supplied EFT derivation and frozen numerical tables are consistent
within their stated premises. One overbroad scalar-vev sentence required
a correction; the parent applied and preserved it. The corrected note has
no remaining material mathematical or numerical finding from this review.
This is a focused independent check, not a formal audit, retained claim
promotion, empirical acceptance, or new primary research route.

## Finding and exact affected-source confirmation

The executed note, SHA-256
`ad480e1a92390acd2feb7152f274bb9677a176c30b2c07024db39f5051609672`,
said that a scalar with compensating nonzero hypercharge could not acquire
a vev preserving the same photon. Nonzero hypercharge alone is insufficient:
the supplied Higgs is a direct counterexample. A vev must instead have
zero charge under the unbroken generator Q0. For the displayed singlet
operators, a singlet compensator has T3=0, so its compensating nonzero
hypercharge also gives nonzero Q0. The intended common-charge Majorana
obstruction is therefore valid with the singlet qualification.

The parent corrected only this paragraph. The complete current note is
SHA-256
`bc695597af77e0d90d60a67b2765d4a49e27806a652b7da3cd6986f47094cd17`.
I checked the exact before/after hashes and the complete diff in
SCALAR_COMPENSATOR_CORRECTION_v2.json, whose hash is
`3c8333b8f0cdeabf5955ecc1e1706dab4c5f99d5276508ae82b14e9aaf991253`.
The original executed note remains byte-identical in both the author's
execution snapshot and this review's v1 snapshot. The runner, protocol,
observation inputs, historical result, and all other original files are
unchanged. The correction changes the scope of that sentence, not the
calculation. No numerical rerun of the author code was needed or performed.

## Complete scope and actual independent work

I read the complete protocol, original note, corrected paragraph in its
full-note context, runner, observation inputs, source ledger, results/scope
note, claim-status certificate, trace gate, both freezes, execution record,
stdout, and correction record. Empty stderr was verified. All 18 original
files were copied exactly before changes. The final 19-file source set is
bound in the final source-disposition map; no source tree outside this
review directory was edited by the reviewer.

The complete RESULTS.json was parsed and independently consumed. Every
364 cubic-trace row, all 12 gravitational traces, every 45 rational case,
all 512 graph rows, every 37 fixed-lattice row, four variable-primitive
examples, and all reported empirical numerical quantities were checked.
This is full table coverage, not inspection of first/last rows alone.

The independent script used small color/weak factor traces instead of the
author's 16-dimensional matrix assembly; GF(2) elimination and union-find
instead of symbolic graph ranks; direct rational center characters; and
exact rational summary propagation before comparison with floats. It also
solved the mass constraints, independently reduced anomaly polynomials,
checked conjugate Lie brackets and generator normalization, derived the
electron-unit map from the physical singlet charges, and tested the
mass-matrix caveat. It imported no author helper and did not execute the
author runner.

The first independent execution completed in about 0.60 seconds with one
thread requested for numerical libraries. All **1,216 checks passed**;
stderr is empty. Its exact executed source is preserved. The results are
in INDEPENDENT_RESULTS_v1.json and the execution record is in execution_v1.
The adjacent INDEPENDENT_DERIVATION.md gives the proof route and limitations.

Decisive negative controls reject a fundamental u^c assignment, omission
of n^c at a nonstandard charge, a universal-flavor claim on disconnected
supports, compactness-alone finite-gap inference, unchanged neutral-neutrino
SF6 response, uncorrelated inverted summary errors, and identifying epsilon
with the measured neutron charge before fixing the electron unit. The
scalar-vev counterexample is explicitly retained as the resolved source
finding. Expected nonzero counterfactuals are not presented as successful
models or concealed failed executions.

## Mathematical disposition

The all-left-handed signs, Yukawa relations, cubic and mixed gravitational
coefficients are correct. The no-neutrino one-generation solution is
conditional on the representation and mass-coupling inventory. Adding a
Dirac singlet restores the familiar B-L direction at Nc=3. The pure color
and mixed anomalies cancel with conjugate representations; the ordinary
SU(2) parity does not fix a generation count. The source properly avoids
claiming a classification of all global anomalies.

Connected charged-current support enforces one charge per connected
component. All graph rows agree, with 205 connected supports. The supplied
connectivity condition is essential to the flavor conclusion; the
disconnected three-family assignment is a valid anomaly counterexample.
No arbitrary support graph is asserted to be unitary or to fit oscillation
data. The common-charge Majorana conclusion does not incorrectly exclude
opposite-charge Dirac pairings or infer Majorana masses from oscillations.

The fixed-lattice congruences and physical-charge gaps are correct for the
specified character lattice and center embedding. A primitive character
lattice should not be confused with faithfulness of the occupied matter
weights: at epsilon=1 those weights have gcd 3, which is allowed because
the source does not impose matter faithfulness. This is a clarification of
the premise, not a defect in the reported rows. The four primitive compact
examples correctly change the embedding and make a nonzero charge
arbitrarily small. They do not contradict the conditional fixed-lattice
gaps. A reported experimental standard uncertainty is not by itself a
rigorous finite bound selecting the exact lattice point zero.

The electron-unit map, composite charges, beta-decay signs, and hydrogen
neutrality statement all hold. The SF6 coefficient is 38/73 after imposing
the candidate relation x=0. The original experiment's special x=y
interpretation cannot be carried over when the neutrino is charged. The
source makes this distinction and retains the nominal composition and
calibration assumptions needed to reuse the published summary.

## Numerical disposition and empirical boundary

Independent arithmetic reproduces the neutron-only transfer prediction
(-0.20821917808219179), propagated uncertainty (0.5726027397260274),
combined uncertainty (1.240110437639226), and standardized residual
(0.087265758595022), in the declared units. The separate joint summary
fit gives delta=-0.3556769526059353, sigma=0.9757195514807966, and
chi-square=0.007615312623164653. All full covariance entries of the
unrestricted two-summary inversion agree, and that covariance has rank two.

The calibration/transfer split is implemented as frozen: the molecular
central value does not change the neutron-only prediction. The optional
joint fit explicitly uses both summaries as calibration. Both observations
were exposed before the protocol; the source does not call either a blind
holdout. Its supplied independent-Gaussian approximation and its nominal
nucleon-mass conversion are not hidden raw-data likelihoods. The central
value is not evidence for nonzero charge, and the inferred neutrino charge
is not an independent observation.

I independently checked the primary neutron abstract's reported summary
at the [journal source](https://doi.org/10.1103/PhysRevD.37.3107).
The parent's failed full-text access is preserved; this review also claims
only abstract-level access, not a complete systematic or event-level read.

I viewed the existing external SF6 PDF's rendered pages 2, 3, and 13 and
checked its v2 identifier. They support the two-parameter molecular force,
the neutral-antineutrino interpretation, the nominal molecular counts,
and the opposite-polarity subtraction. The half-sum and independent error
propagation agree with the published rounded summary. The unknown odd
systematic is visible in the primary report, and an arbitrary even offset
would remain degenerate with charge. The [primary SF6 paper](https://arxiv.org/pdf/1102.2766v2)
was not copied into this review or public source tree; its existing exact
PDF/page hashes and paths are recorded separately.

The [Foot–Lew–Volkas review](https://arxiv.org/pdf/hep-ph/9209259)
provides prior art for the Dirac B-L and flavor freedoms, with a different
epsilon normalization. [Tong's global-group discussion](https://arxiv.org/pdf/1705.01853v2)
provides context for the center quotient and line-operator distinction.
Targeted sections were read; neither complete paper nor all prior repository
theorems are certified by this focused check. The anomaly and lattice
conclusions above were derived independently, not imported as verdicts.

## Limits, failures, and final source status

The gauge algebra, chiral inventory, Higgs, allowed couplings, ordinary
anomaly framework, flavor connectivity, global form when used, and
composite-particle identifications are supplied. No native chiral phase,
generation count, gauge/Yukawa coupling, particle mass, or TOE is derived.
The optional embedding into the earlier universal physical metric supplies
that metric and does not calculate quantum trace responses or establish
arbitrary material composition independence. No hidden measured value is
used to fix those gravitational or matter parameters.

The original note's scalar sentence was a genuine scope error, now fixed
with exact recovery. The parent full-text source-access failure remains
visible. One initial reviewer display of the large result/runner output
was truncated; the omitted runner lines were reread completely and every
table row was subsequently consumed independently. No independent numeric
execution failed, no primary source was silently replaced, and no formal
audit/status outcome was applied.

The packet's pending-review wording is historical packaging metadata;
this report supplies the completed focused check without editing those
files or promoting their status. The final receipt binds all source bytes,
recovery snapshots, independent calculations, this report, the derivation,
and the affected-source confirmation. Parent remains the scientific author
and retains interpretation and next-route decisions.
