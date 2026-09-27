---
claim_id: transmon_calibration_holdout_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "Exact conditional square-sector operator identity and numerical calibrated transmon comparison for one specified KIT cooldown; no statistical rejection, native parameter prediction, or general no-go."
upstream_dependencies:
  - local_pair_form_and_general_graph_magnetic_dynamics_bounded_theorem_note_2026-09-24
  - local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24
runner: scripts/transmon_calibration_holdout_2026_09_26.py
---

**Type:** bounded_theorem
**Status:** conditional-support; numerical empirical comparison, unaudited.

# Calibrated transmon predictions for three unused KIT transitions

Fixing four calibration coordinates in a supplied single-cosine transmon plus
resonator model gives nonzero residuals on three unused measured transitions.
The drive-frequency residuals are +5.18144, +14.39572 and +28.25734 MHz. The
calibration coordinates themselves are fitted inputs and are not predictions.
This is a retrospective benchmark, with the paper's general discrepancy known
before calculation. It reports a scoped numerical observation, not a statistical
rejection or a theorem excluding other models or calibration roots.

## Conditional operator identity and its obligations

The exact mathematical claim is that the minimal-record sector of the supplied
simple-square common Hamiltonian is unitarily equivalent, up to a scalar, to
the zero-offset-charge Cooper-pair-box Hamiltonian when EC=K and EJ=4 delta.

Orient the square's four links from its two occupied A vertices to its two
empty B vertices. Gauss law gives E=(n,-n,-n,n), n integer. Thus D=4n². The
two allowed assignments in S=F_c F_a have the same final matter word and
relative field shift U, where U|n>=|n+1>. Hence S* S=2I+U+U*, and

    H_square = 4K n² - 2 delta(U+U*) - 4 delta I.

Fourier transformation on the circle sends U to exp(i phi), proving
H_square+4 delta I=4K n²-4 delta cos(phi). The bounded cosine preserves the
self-adjoint domain of n². This uses the [local pair formula](LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md)
and its [supplied common-law parent](LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md),
whose assumptions remain conditional. The Gauss reduction and the two-path
coefficient are proved here; the microscopic common-law limit is inherited,
not independently re-proved. The empirical identification of these operators,
parameters, preparation and readout with a physical device remains imported.

For positive kappa the square's eight resolved birth channels give total loss
8 kappa I in this sector. Its normalized no-event evolution follows H_square;
unconditional evolution also transfers weight into fully occupied sectors.
Setting kappa=0 is a separately supplied closed-model specialization. Neither
case identifies the formation instrument with transmon dissipation. Noninteger
offset charge and resonator terms below are external device ingredients,
not consequences of the square reduction. Spectroscopy is an imported probe,
not the preceding cube protocol's first/second formation record readout.

## Source, calibration and evaluation

Use the first KIT cooldown, row `KIT`, in Willsch et al.,
[Observation of Josephson harmonics in tunnel junctions](https://doi.org/10.1038/s41567-024-02400-8).
The numerical source is [Juelich DATA](https://doi.org/10.26165/JUELICH-DATA/LGRHUH),
which points to the authors' repository. The committed CSV is byte-identical
to `results/Experiment.csv` at commit
`d97280c61c54ca8d54ccf0a8706713130778eb63`, SHA256
`0b6abf45a5b574f2ecc492b19560d44ff1638894a0579504dc850c1cb628a01b`.
No author fitted parameter table is read. Numerical values are GHz energy
frequencies throughout; no extra factor of 2 pi is applied.

The explicitly imported device Hamiltonian is

    H/h = 4 EC(n-ng)² - EJ cos(phi) + Omega a* a + G n(a+a*).

Its four positive parameters are fitted only to

| Calibration coordinate | Value, GHz |
|---|---:|
| f01 | 6.0391 |
| f02 | 11.8680 |
| resonator frequency for transmon ground state | 7.4613 |
| resonator frequency for first excited transmon state | 7.4587 |

The CSV calls the last two coordinates `fres1` and `fres2`. The fourth input
incorporates a dispersive shift transferred from cooldown 2; these are not
four contemporaneous independent cooldown-1 measurements. This is explicit
in [Supplementary Information, III.A and Table S6](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41567-024-02400-8/MediaObjects/41567_2024_2400_MOESM1_ESM.pdf).

Adopt the source model's average of the ng=0 and ng=1/2 transition frequencies.
A direct controlled parity-branch average for KIT is not established here.
Both endpoints and a charge grid are computed as sensitivity checks. Full
capacitive coupling is retained, including counter-rotating terms.

Three starting guesses converge to the same found calibration root:

    EC = 0.196567178810, EJ = 24.852181043101,
    Omega = 7.453936854591, G = 0.077763912291 GHz.

This is found-root consistency, not global uniqueness. The numerical
calibration error is below 0.001 MHz. Parameters are then fixed before
converting any evaluation value. All available higher KIT transitions are
reported; unavailable f06/f07 are not counted as tests.

| Unused transition | Measured total GHz | Calculated total GHz | Total residual MHz | Drive residual MHz |
|---|---:|---:|---:|---:|
| f03 | 17.457 | 17.472544315 | +15.544315 | +5.181438 |
| f04 | 22.778 | 22.835582891 | +57.582891 | +14.395723 |
| f05 | 27.794 | 27.935286714 | +141.286714 | +28.257343 |

The measured j-photon drive frequency is f0j/j. The paper's approximate
1 MHz accuracy refers to this drive coordinate, not to a Gaussian standard
deviation of each total transition. The CSV supplies no covariance matrix;
no p-value or uncertainty-normalized rejection is calculated. The model and
dataset were selected with prior exposure to the published general result.
The computational calibration/evaluation separation is not historical blindness.

## Numerical checks and declared sensitivity scenarios

The primary calculation uses charges -14..14, twelve bare-transmon levels
and nine photon states. Individual and joint increases through charges
-40..40, twenty-four transmon levels and twenty photon states change the
three evaluated totals by at most 0.000030 MHz. A separately written direct
charge-tensor-photon construction avoids transmon-subspace truncation and
agrees within that amount; the primary runner imports this helper and checks
its numerical eigenpair residuals and unique assignments. Both use SciPy
linear algebra, so independence concerns operator construction and basis,
not independent numerical-library certification. Floating convergence checks
are not formal infinite-basis intervals.

Dressed levels are identified by bare-state overlap with an explicit
uniqueness check. The minimum overlap along twenty-one sampled coupling
values is above 0.97. This is a sampled assignment check, not a proof of
continuous adiabatic branch tracking. A separate development review also
tracked adjacent eigenvectors. Its finding is corroborative review history;
the fresh runner's declared guarantee is the sampled check.

The twenty-one-point charge grid gives total-frequency widths approximately
0.000368, 0.008878 and 0.157861 MHz for f03,f04,f05. It is not an enclosure
of every intermediate charge offset. For calibration sensitivity, perturb
the four total-frequency coordinates by [1,2,1,1] MHz in every sign
combination and recalibrate each scenario using only those four coordinates.
The second width is doubled because f02 is a two-photon total frequency.
The cavity widths are explicitly chosen sensitivity values, not published
independent error bars.

| Unused transition | Drive residual across sixteen corners, MHz |
|---|---:|
| f03 | +1.70986 to +8.63695 |
| f04 | +7.95155 to +20.78745 |
| f05 | +18.24457 to +38.15028 |

These are finite scenarios, not proven extrema over the box or a confidence
region. Subtracting an additional 1 MHz target-drive variation still leaves
positive residuals at every tested corner. Cross-cooldown transfer, drive
shifts, additional modes and other systematics are not exhausted by this
exercise. The local calibration Jacobian has condition number about 7826
in the stated coordinate units; its linearized box halfwidths are also printed. The
statement is the existence of these calculated residuals under named inputs,
not exclusion of every model compatible with all experimental uncertainties.

## Imports and scientific meaning

The mathematical model, tensor-product quantum mechanics, Gauss law and
common-limit construction are supplied. The circuit identification, offset
charge, resonator, probe interpretation, calibration data and endpoint mean
are external physical inputs. None is retired by numerical agreement.
The exact operator map is useful, but the full physical identification and
finite-microscopic spectroscopic error budget remain open obligations.

This benchmark qualifies an earlier exploratory bare-transmon comparison
with a rounded 455 MHz anharmonicity: reproducing a calibrated low spectral
feature does not by itself test additional features. Here the additional
features have explicitly computed residuals. This does not derive Josephson
harmonics or uniquely identify the missing physical correction. A next test
could derive corrections from the microscopic law with their coefficients
fixed before data comparison, or use a fuller independently calibrated device
model. Existing conventional explanations are comparators, not conclusions
selected by this computation.

## No-Go Discipline Gate

The published claim is a bounded positive numerical observation: the stated
calibrations and finite checks produce the displayed residuals. No universal
negative or independent-wall count is proposed. The following scope checks
also document the limits of interpreting that observation negatively.

- **N1 — Alternatives:** five distinct possible error mechanisms were ATTEMPTED:
  basis truncation (larger bases), omitted readout hybridization (full cavity
  coupling), charge-offset convention (endpoints and grid), calibration input
  uncertainty (nonlinear corner refits), and incorrect spectral labels
  (unique dominant overlaps and sampled coupling values). Each has the
  computed outcome above; these checks do not rule out all possible versions
  of any mechanism. Unmodeled drive, extra modes and alternate roots remain
  unexhausted. No five-route impossibility certificate is claimed.
- **N2 — Conditions:** no assertion of mutually independent walls is made.
  Circuit identification, calibration and omitted-physics errors can interact;
  their implication relations are unresolved. No additive wall count is used.
- **N3 — Hidden inputs:** all quantum, graph, device, calibration, offset and
  readout assumptions are named. The transferred cavity calibration is exposed
  rather than counted as a separate same-cooldown measurement.
- **N4 — Residual matching:** the external spectroscopy dataset supplies this
  device's measured frequencies. The local-pair parent supplies the square
  operator, not empirical validation. Neither is cited as excluding arbitrary
  microscopic extensions. The paper's general result is context, not a
  replacement for recalculation of these three residuals.
- **N5 — Resolution:** three transition totals and their drive coordinates are
  evaluated for one device. No per-spatial-site or lattice-wide conclusion
  follows. The runner emits its actual resolution coverage.
- **N6 — Partial closure:** calibration and the imported circuit map provide
  a useful conditional benchmark without adopting a new framework primitive.
  No new-axiom requirement or primitive-absence theorem is asserted.
- **N7 — Steelman:** a fuller device model, different admissible calibration
  root, unaccounted transfer error or drive-dependent line shift could change
  the comparison. Their terminal obligation is to fix those ingredients from
  independent information and predict unused lines, rather than fit the
  residuals. This is why the claim is the displayed scoped observation and
  not a general no-go or unique diagnosis.
- **N8 — Prior context:** current-main/open-PR searches found no transmon
  benchmark already present. The earlier private rotor comparison used a
  different device and observable; it neither refutes nor validates this one.
  No prior failed route is promoted into a general prohibition here.

## Review record and reproduction

Independent source review checked units, calibration/evaluation separation,
SI interpretation and indexing. It exposed the cooldown transfer and
multiphoton-accuracy qualifications, both incorporated above. Independent
numerical work constructed the direct charge-photon Hamiltonian before seeing
primary predicted vectors, then confirmed nominal predictions, numerical
cutoffs, assignments and the sixteen corner forward predictions. The review
shares calibrated parameters and measured data; it is not an independent
experiment or formal repository audit. Final publication-source review and
mutation results are recorded in the branch handoff.

Run `python3 scripts/transmon_calibration_holdout_2026_09_26.py`.
The primary imports both numerical implementations, so no claim-scoped helper
registry change is needed. It reads the pinned external CSV, uses only its
four named calibration cells inside the optimizer, and evaluates the three
remaining measured lines after predictions are constructed. `AUDIT_INPUT_PATHS`
binds both helpers, provenance, source note and model parents; the canonical
cache is generated by `scripts/runner_cache.py`. Dependency fingerprints are
integrity reads, not additional measured input. No network is needed to run.

```yaml
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: Exact supplied-square operator identity with a scoped numerical calibrated circuit comparison; numerical residuals are not a statistical theorem.
audit_required_before_effective_retained: true
bare_retained_allowed: false
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: Test additional measured transitions after calibration without refitting them.
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: literature_bridge
next_trace_action: Independently fix additional device or microscopic corrections and test unused measurements with an explicit error budget.
```
