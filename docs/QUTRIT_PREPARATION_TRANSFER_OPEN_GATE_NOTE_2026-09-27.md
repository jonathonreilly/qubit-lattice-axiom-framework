---
claim_id: qutrit_preparation_transfer_open_gate_note_2026-09-27
claim_type: open_gate
claim_scope: "Conditional population transfer from a separate qutrit relaxation calibration to Ramsey and echo acquisitions, preserving both agreement and mismatch; no coherence, precision, or native TOE confirmation."
upstream_dependencies: []
runner: scripts/preparation_transfer_2026_09_27.py
---

**Type:** open_gate
**Status:** conditional-support; supplied-model comparison, unaudited.

# Frozen-rate qutrit population transfer across preparations

Three downward transition rates calibrated on a separate nominal state-|2>
relaxation experiment predict the population sum in a Ramsey acquisition with
an RMS residual of 1.6593 percentage points, without fitting that target.
The stronger echo intervention test has a much larger residual: 15.8513
percentage points under the declared instantaneous midpoint-swap model.
Both outcomes belong to this comparison. The Ramsey agreement does not validate
general transfer of these dynamics to other pulse sequences.

This is a conditional imported rate-equation benchmark, also realizable as the
population sector of a canonical Lindblad model. An incoherent equal mixture
and an equal coherent superposition give the same observable. Consequently
these results do not test coherence, establish superposition, or confirm native
TOE physics. The decay law, state preparation, readout map and cross-acquisition
rate stability are supplied assumptions. No microscopic derivation of the rates
from the framework is supplied.

## Exact conditional construction

**Target:** Given stationary nonnegative rates k10, k21, k20, specified initial
populations, and ideal operations confined to states 1 and 2, compute the
population sum Pexc=p1+p2 without supplying any target population or frequency.

Let kij denote the rate from state i to state j. Assume no upward transitions,
no drive during the waiting intervals, a diagonal free Hamiltonian, and jump
operators sqrt(kij)|j><i|. Equivalently, use the classical population generator
in state order (0,1,2):

    L = [[0, k10, k20],
         [0, -k10, k21],
         [0, 0, -k21-k20]].

Columns sum to zero and off-diagonal entries are nonnegative. Thus exp(Lt)
preserves normalized nonnegative populations for t>=0. Put lambda=k21+k20 and

    F(t) = [exp(-k10*t)-exp(-lambda*t)]/(lambda-k10),

with continuous limit t exp(-k10*t) when lambda=k10. Integrating the triangular
population equations gives

    u2(t) = u2(0) exp(-lambda*t),
    u1(t) = u1(0) exp(-k10*t) + k21 u2(0) F(t),
    u0(t) = 1-u1(t)-u2(t).

For calibration preparation |2>, the predicted vector is

    [1-exp(-lambda*t)-k21*F(t), k21*F(t), exp(-lambda*t)].

For target initial populations [0,1/2,1/2], the Ramsey sum is

    Pexc(t) = [exp(-k10*t)+exp(-lambda*t)+k21*F(t)]/2.

No coherence phase or dephasing coefficient enters this expression. For any
final unitary U that mixes only states 1 and 2, U commutes with the projector
P=|1><1|+|2><2|. Trace cyclicity proves Tr(P U rho U†)=Tr(P rho).
This invariance does not require a perfect final pi/2 angle. Loss, leakage,
relaxation during pulses, and inaccurate initial populations are outside it.

For echo, let S exchange populations 1 and 2 while leaving population 0 fixed.
The declared instantaneous midpoint operation gives

    u_echo(t) = exp(L*t/2) S exp(L*t/2) [0,1/2,1/2].

Sum its last two components after the final within-12 unitary. The no-swap
control uses exp(L*t)[0,1/2,1/2]; it is not the declared echo sequence and is not
selected as a replacement when its residual happens to be smaller.

The exact archived echo analysis sends x0 to two x0/2 waiting intervals around
an explicit permutation matrix. This fixes the analysis convention of total
delay. The executed hardware schedule has not been recovered. Cached pulse
durations do not justify adding timing corrections. The archived notebook fits T1 with rates 1/T but its echo collapse
operators imply rates 2/T. This is a source-convention discrepancy, not an
independently justified correction to the measured clock or decay rates. Its
fitted constants are not imported here. Our rates are defined by and calibrated
to the explicit L above; no factor is selected from echo agreement.

## Observation and source identity

For each applied gate voltage, let c0,c1,c2 be the final three recorded I/Q
reference centroids. Assume y=p0*c0+p1*c1+p2*c2 and sum(p)=1. If the two-column
matrix D=[c1-c0,c2-c0] is invertible, then

    [p1,p2] = D^-1 (y-c0),  p0=1-p1-p2.

This establishes an affine readout convention, not reference-state fidelity.
No noisy population estimate is clipped or removed. Values outside the
probability simplex are retained; this can occur near population boundaries
and is not itself a measured physical failure probability.

The source is Krause et al.'s public archive
[DOI 10.5281/zenodo.10728469](https://doi.org/10.5281/zenodo.10728469), SHA-256
`a8272b6cbe92ddc083d2a22b94bdb7743b19c50debbe89f4106baf817c69c574`.
Exact source member hashes and compact raw I/Q arrays are packaged. Producer
notebooks identify the acquisition-specific reference masks; a uniform-looking
time grid alone does not establish that every sample is a waiting time.

| Role | Exact TUID | Genuine observations | Separate reference samples per gate |
|---|---|---:|---:|
| State 2 calibration | 20220920-215202-730-31ad1f | 61 gates x 197 delays x 3 populations | 3 |
| Ramsey target | 20220921-083404-829-b243a3 | 31 gates x 380 delays | 3 |
| Echo target | 20220920-210206-915-8331be | 61 gates x 246 delays | 3 |

The three calibration population coordinates sum to one and have correlated
reference noise. Equal weighting defines a descriptive least-squares objective,
not an independent-coordinate likelihood. Target reference samples provide
readout calibration but are not fitted dynamical observations.

Ramsey starts 10 h 42 min 02 s after calibration. Recorded fields/readout settings
agree, while microwave frequencies/amplitudes and initialization duration change.
Echo starts 49 min 55.815 s before calibration, with the reviewed snapshot
settings equal. This is retrospective source research, not a physical forecast
made before acquisition. Within this workflow, each complete target prediction
was frozen before opening that target's amplitudes. Hashes and code paths support
the recorded boundary; they cannot certify absence of all historical human access.
Equal applied gates and settings do not establish stable offset charge or rates.

## Calibration and all declared controls

The three-rate model fits all 36,051 calibration population coordinates, with
fixed initial |2>, no offset/rescaling, rates in [0,10] per microsecond, and three
starts. All three returns stop by ftol and remain above the requested gradient
tolerance. All starts and their statuses are preserved. No active bounds occur.
Rates are approximately [k10,k21,k20]=[0.07126916,0.11124121,0.00839770] per
microsecond, with calibration population RMS 0.03151155. A local Jacobian
condition near 4.97 is a numerical sensitivity diagnostic, not a confidence bound
or proof of global identification. Close starts do not define an error bar.

A later, explicitly post hoc control sets k20=0 and recalibrates the two remaining
rates on exactly the same calibration populations. It also retains all three
starts, all ftol terminations above gradient tolerance, and all target curves.
No target population is fitted. Rates are approximately [0.07728135,0.11762925,0]
per microsecond; calibration RMS is 0.03227173. The original target freeze is
unchanged. A fixed population-one no-decay comparator is another post hoc control.

| Target / declared dynamics | RMS residual (percentage points) | Mean prediction minus observation (percentage points) |
|---|---:|---:|
| Ramsey / three rates | 1.659315 | +0.274780 |
| Ramsey / sequential-only recalibration | 1.673540 | +0.358514 |
| Ramsey / fixed no decay | 5.164180 | +4.414061 |
| Echo / three rates and midpoint swap | 15.851257 | +14.175870 |
| Echo / three rates without swap | 13.387442 | +12.104752 |
| Echo / sequential-only and midpoint swap | 16.254789 | +14.553427 |
| Echo / sequential-only without swap | 13.308114 | +12.070934 |

Rounded values represent the calibration-cost-selected return of each model;
all six rate returns and all twelve echo curves remain in the data and runner.
The tiny Ramsey RMS difference does not establish necessity of direct 2-to-0
decay or statistical preference. The echo mismatch remains large for both rate
models and the no-swap comparator. No target-dependent timing factor, rate
rescaling, initial-state adjustment, or readout offset is introduced to repair it.

At the first/last Ramsey delay, the full prediction is 0.996810/0.920138 and the
measured gate mean is 0.992118/0.916535. At the last echo delay, the full swap
prediction is about 0.664548 versus measured mean 0.424026. These are descriptive
comparisons, not significance tests. Reference covariance, preparation, finite
pulse dynamics, clock/rate conventions, and cross-acquisition changes remain
unresolved; this finite mismatch is not a universal no-go or exclusion of the
canonical model class.

## Verification, reproducibility and limits

The portable primary `scripts/preparation_transfer_2026_09_27.py` reconstructs
raw affine populations, propagates every supplied rate return with stable closed
forms, and reproduces the reported calibration objectives and target residuals.
It imports `scripts/preparation_transfer_independent_2026_09_27.py`, which uses
SI-second matrix exponentials and augmented affine QR readout. Literal input
closure is declared. All runtime data are repo-local; the comparator does not
rerun the historical nonlinear optimizers or claim access to executed waveforms.
Its numerical/integrity checks do not assert that measured residuals are small.

Independent external reconstruction checked raw readout, source masks, the
calibration/target separation, and all supplied Ramsey/control curves. Echo
checks and final mechanical publication results are recorded in the paired
review evidence and PR body. Numerical agreement between implementations is
narrower than experimental adequacy, native derivation or formal audit status.

## Claim state and remaining obligations

    actual_current_surface_status: conditional-support
    target_claim_type: open_gate
    trace_class: frontier_discovery
    target_claim_id: null
    reachability_to_target: unknown_frontier
    artifact_role: frontier_probe
    independent_audit_required: true

This supplies an explicit preparation-dynamics-observation comparator and a
stronger failed transfer, useful for future readout modeling. It promotes no
existing framework claim and retires no native-theory import. Required next
work is independently established pulse/clock conventions, preparation/readout
errors and rate stability, followed by genuinely discriminating held-out tests.
Do not tune those quantities to the echo target and relabel the result a prediction.
