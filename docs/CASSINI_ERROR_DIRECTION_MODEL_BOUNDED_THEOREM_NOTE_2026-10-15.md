# Cassini error-scale elimination under a tested direction model

**Date:** 2026-10-15
**Status:** conditional-support
**Claim type:** bounded_theorem
**Actual current surface status:** conditional-support
**Primary runner:** [cassini_error_direction_check.py](../scripts/cassini_error_direction_check.py)

The exact target is a quantizer-safe, unknown-scale confidence construction
for a finite complex tone under a supplied conditional error-direction law,
together with a frequency-uniform diagnostic of that law on a fixed exposed
Cassini sample window. Orthogonal-ratio and cone-distance mathematics is proved
below. Its probability rule is a candidate import; no scalar action, physical
initial state, absolute scale or environment is thereby derived.

The earlier constant-modulus, quantization-only model motivated this attempt.
Here the same day169 2002 seconds[48900,49500) are used, 600 one-second records
in each of two already exposed 13:35 X/Ka products. No independent empirical
test is claimed. The later 16:56/16:57 raw products remain unopened. The
[pinned manifest](../scripts/cassini_error_direction_inputs.json) includes exact
public source and label identities. No result-dependent clipping occurs.

## What is assumed and what is eliminated

Let a training observation T select any measurable reference frequency g(T).
For a distinct validation vector of N complex samples, with N >= 3, suppose

    y = c u_f + epsilon,       u_f,j = exp(2 pi i f t_j).

The complex amplitude c and frequency f are unknown. Times are the specified
uniform grid with finite fs>0, centered for numerical convenience. N is an integer,
q is finite and nonnegative, and all tail probabilities lie strictly between0 and1.
Frequencies are identified
modulo the sample rate fs. Conditional on T, suppose the direction
epsilon/||epsilon|| is uniform on the complex unit sphere and the radius is
strictly positive almost surely. Its radial distribution is entirely unspecified;
even direction-radius independence is unnecessary for the ratios below.
The term c u_f specifies a tone signal component (a location), not necessarily
E[y]. Neither zero error mean nor finite moments is required for these ratios.
For example, let U be uniform on the complex unit sphere and choose
R=1+kappa Re(U_1), with0<kappa<1. Then R>0 and U remains the direction, but
E[R U]=kappa e_1/(2N), since E[U]=0 and E[Re(U_1)U_j]=delta_(1j)/(2N).
Identifying c u_f with the statistical mean would require an additional moment
condition, which is not supplied or used here.

Independent proper complex Gaussian white noise is one sufficient example.
This angular symmetry is an explicit candidate physical import, not a consequence
of an equal output bandwidth and sample rate, a large fitted tone fraction,
isotropic covariance, a choice of filter, or a central-limit slogan.

The actual code vector is z. A separate ideal, unsaturated ADC premise implies
||z-y|| <= q. In doubled midrise code units, unit half-width in each real and
imaginary component gives q = sqrt(2N). A digital truncation convention alone
does not establish that this is the entire physical error. Here q describes only
quantization; epsilon describes all other admitted discrepancy.

Conditional angular symmetry eliminates the need to supply a stochastic noise
scale or radial law for the stated tests. It supplies **no deterministic upper
bound on error energy** and does not establish its own physical applicability.
All previously exposed Cassini data remain model-development data. The words
training and validation here name an internal sample split, not an independent
empirical test after campaign-level exposure.

## Frequency test without a supplied variance

Let P_f be the orthogonal projection onto span(u_f), P_S the projection onto
S = span(u_f,u_g), p = dim(S), A = P_S-P_f, and B = I-P_S. A and B are mutually
orthogonal projections with complex ranks r=p-1 and s=N-p. At the true f,

    Ay = A epsilon,       By = B epsilon.

For p=2, r=1 and s=N-2. A uniform sphere direction may be represented as G/||G||
for a proper complex standard Gaussian vector G; this represents the direction
only and does not assert Gaussian errors. Orthogonal groups of its coordinates
have independent Gamma(r,1) and Gamma(s,1) squared norms. The shared normalization
and actual error radius cancel. Consequently

    (s/r) ||Ay||^2 / ||By||^2  ~  F_(2r,2s), conditional on T.

The denominator is positive almost surely under the positive-radius premise.
For upper-tail probability alpha, put

    tau^2 = (r/s) F_(2r,2s)^(-1)(1-alpha).

For r=1 this simplifies to tau^2 = alpha^(-1/s)-1 by integrating the Beta(1,s)
tail. Accept f when ||Ay|| <= tau ||By||. This is inversion of a fixed-f test;
it does not require a multiplicity correction for a continuum of candidate
frequencies to cover the single true f. Simultaneous claims for many records do
require their own allocation. If p=1, use an always-accepted frequency test;
never divide by r=0. No numerical optimizer's selected g is asserted to be a
global spectral optimum, and no validation result enters its training algorithm.

The signal may be absent (c=0); coverage still holds while frequency identification
can become uninformative. A physical nonzero signal cannot be supplied by labeling
the largest numerical periodogram peak a carrier.

## Exact quantizer-safe cone geometry

For fixed orthogonal nonzero-rank A and B and tau>0 define

    K = {w: ||Aw|| <= tau ||Bw||}.

Its unused orthogonal component is unconstrained. If a=||Az|| and b=||Bz||,

    dist(z,K) = (a-tau b)_+ / sqrt(1+tau^2).

For a>tau b, the nearest radial norms are

    b'=(tau a+b)/(1+tau^2),       a'=tau b'.

Choose the projected directions aligned with Az and Bz, and leave the unused
component unchanged. If b=0, any direction in the nonempty range(B) suffices.
The norm reverse-triangle inequality shows every other point has at least this
radial distance, proving optimality. If a<=tau b the distance is zero. This does
not require convexity of K, which generally is absent.

Therefore the Euclidean ball of possible analog vectors intersects K exactly iff

    ||Az|| <= tau ||Bz|| + q sqrt(1+tau^2).

The true ADC cell box lies inside that ball, so this enlargement is conservative
for the cell premise. Under the candidate direction law, accepting by this rule
covers true f with probability at least 1-alpha. A larger q can only enlarge the
set. It is not a fitted residual bound or a claim that all analog vectors in the
outer ball are physically available ADC values.

## Fixed-frequency amplitude and joint coverage

At the true f, write c_hat = u_f^* z/N and E_z=||(I-P_f)z||^2. For analog y,

    (N-1) N |c_hat_y-c|^2 / ||(I-P_f)y||^2 ~ F_(2,2N-2).

Applying the same translated cone geometry gives the quantizer-safe disk

    |c-c_hat| <= [tau_c sqrt(E_z)+q sqrt(1+tau_c^2)]/sqrt(N),
    tau_c^2 = alpha_c^(-1/(N-1))-1.

Combining this with frequency inversion at alpha_f gives joint coverage at least
1-alpha_f-alpha_c by the union bound, conditional on the premises. This avoids
asserting independence of arbitrary reused statistics. In the nested unquantized
projection decomposition, a stronger product result can be derived from the
Dirichlet grouping law; it is not needed for the present code or empirical plan.
An inferred phase interval additionally requires a disk excluding zero. No
nonzero-amplitude or phase-unwrapping assumption is silently added.

## Observations can challenge the angular supplier

At candidate f, derotate by D_f^*=diag(exp(-2 pi i f t_j)), take a unitary DFT,
and omit the DC coordinate. The assumed constant tone then disappears exactly.
Split non-DC indices into H: |frequency|>=fs/4, and L: 0<|frequency|<fs/4.
Let a_f and b_f be the L and H coordinate norms, and let r and s be their complex
ranks, both required to be positive for this color test (N=3 or4 lacks a low
group and is outside this extension). The corresponding projections are orthogonal and annihilate u_f. Under
the candidate angular law their normalized squared-norm ratio again has the
F_(2r,2s) distribution. Both tails can be tested with the same ADC-safe cone.

For N=500 and fs=1000 Hz, r=248 and s=251. At the true f, a low/high imbalance
is a model test, not a measurement of noise variance. Low/high energies evaluated
only at a fitted frequency are nuisance-dependent diagnostics; the next enclosure
keeps all candidate f instead of treating that fit as exact.

Let Z=||z||, R=|<u_g/sqrt(N),z>|/Z, and
k=|<u_f,u_g>|/N. For p=2 the normalized g tone decomposes into its f component
and a perpendicular unit vector v. Thus

    ||Az|| >= max(0,R-k) Z,       ||Bz|| <= Z.

The omitted factor 1/sqrt(1-k^2) could strengthen the first bound; discarding it
is conservative. With carrier threshold tau and Z>0, no frequency can be accepted
where

    R-k > tau + q sqrt(1+tau^2)/Z.

For aliased distance d between f and g in (0,fs/2], the uniform-grid Dirichlet
kernel gives

    k = |sin(pi N d/fs)|/[N sin(pi d/fs)]
      <= 1/[N sin(pi D/fs)]            whenever d>=D>0.

If this supplies a strict far-frequency exclusion, all remaining frequencies lie
on the arc g-D to g+D modulo fs. If the bound fails, the code declares the global
enclosure uninformative instead of selecting a convenient local interval.

For any spectral projection P,

    | ||P D_f^* z|| - ||P D_h^* z|| | <= 2 pi ||t z|| |f-h|.

This follows from the derivative of the diagonal unitary and the contraction of
an orthogonal projection. Hence the color cone score a_f-tau b_f has Lipschitz
constant at most (1+tau) 2 pi ||t z||. At each midpoint of an arc partition,
subtract this bound times the half-width and the ADC enlargement. A positive
lower score excludes that entire cell. Either color tail can exclude each cell;
if every cell is excluded, the joint frequency/color acceptance set is empty.

Use alpha_record/2 for the frequency statistic and alpha_record/4 per color tail.
The false-rejection probability of this full composite procedure is at most
alpha_record under the stated model at its true f, irrespective of correlation
among its three statistics. For the 1200 fixed records, alpha_record=.01/1200
also bounds the probability of any false rejection of their joint candidate
model by .01, without assuming independence across records. These are properties
of the fixed procedure under its premises, not a newly independent observational
test after the data helped motivate this class of procedures.

The current code evaluates the analytic enclosures in ordinary floating point.
It retains margins but is **not an outward-rounded interval proof** of observed
exclusion. Numerical outcomes are explicitly reported as development diagnostics.
Raw-level frequency aliasing, training-law failure, constant-amplitude/chirp
failure, colored noise, gain changes and unmodeled receiver behavior are possible
explanations of a discrepancy. A rejection cannot isolate error color or infer
new gravitational physics.

## Failure witness: covariance isotropy is insufficient

In C^N let epsilon choose a basis vector uniformly and multiply it by an
independent uniform phase, with fixed norm. Its mean is zero and covariance is
I/N, but its direction is axis-supported rather than sphere-uniform. For a rank-one A
aligned with one basis vector, the upper-tail cone rejects that axis choice with
probability 1/N, and accepts the other axis choices (including any 0/0 case by the cone
inequality). For N=40 and nominal alpha=.01, actual rejection is .025. Merely
measuring equal variances and zero two-point correlations does not establish
this direction law. Similarly, unspecified FIR coefficients do not supply a
whitening transformation, and choosing one would add an import.

## Empirical roles and next gate

The registered first 600 seconds of the two previously exposed 13:35 products
remain the only observations in this block. Each record is split at sample500;
the frequency reference uses the first half only. All 1200 records, flags and
competing peaks are retained. Expected FGAIN Px/No settings are summarized as
instrument settings, never as measured C/N0. No new raw product is opened.

If the conditional supplier fails this challenge, preserve the failure and seek
an actual filter/covariance or signal-waveform supplier, rather than interpreting
the residual as a scalar signal. If it survives, the physical premise remains
unproved; survival alone neither derives a scalar assumption nor calibrates an
independent experiment. The user-requested work-back program still requires a
distinct observation-supported action, initial-state, scale and environmental
bridge. This block is a bounded attempt to remove one measurement import.

## Observation-level results and source boundary

The fixed sample split uses samples0–499 for g and500–999 for the contrast
statistics. The training estimator uses the largest16000-point FFT bin and a
bounded local refinement; it is not asserted globally optimal. At this g, the
median real adjacent residual correlation is0.2289104633 in X and0.8343492492
in Ka. Median low/high non-DC energy per complex rank is1.634887009 and
11.52567688, respectively. These fitted-frequency diagnostics have no exact
nuisance-free p-value assigned to them.

The continuous-frequency procedure, with the conservative real-arithmetic
Dirichlet and mesh bounds above, gives the following **floating diagnostics**:

| Allocation | X numerical exclusions /600 | Ka numerical exclusions /600 | X / Ka uninformative outer arcs |
| --- | ---: | ---: | ---: |
| alpha_record=.01 |489|592|0 /8|
| alpha_record=.01/1200 |168|578|0 /21|

All uninformative or nonexcluded records remain in the output. One additional
Ka arc remains nonexcluded under the stricter allocation. There is no tuning
of a covariance matrix or signal/noise scale to these results. This is a
challenge of the joint constant-tone, conditional-direction and measurement
model. It cannot identify which of its physical premises fails. The nominal
allocation is a property of the fixed procedure under those premises; choices
were recorded before these new diagnostics but after prior raw-data exposure;
these previously exposed observations do not become an independent empirical
confidence experiment because an internal half-record split was used.

The [2001 RSR specification](https://pds-geosciences.wustl.edu/radiosciencedocs/urn-nasa-pds-radiosci_documentation/DSN_0159-SCIENCE/dsn_0159-science.2001-02-28.pdf),
sections2.3 and3.5, describes the decimating FIR, truncation and expected FGAIN
settings. The headers carry FGAIN38dB-Hz in X and44dB-Hz in Ka throughout this
window, IF bandwidth setting110MHz and digitizer attenuation codes40/49.
Those expected gain-setting inputs are not measured noise power or a covariance
matrix. All selected downstream codes avoid the extreme16-bit values and have
zero data-error count; this does not prove upstream clipping absence or the
ideal analog cell premise.

The [Cassini Radio Science User's Guide](https://pds.nasa.gov/data/pds4/misc/document_cassini/Cassini_Radio_Science_Users_Guide_30Sep2018.pdf),
section2.5.2.4, identifies monitor products that may contain receiver noise
temperature and carrier SNR. Sections3.2.1.1.1 and3.3.4.6 discuss averaging,
overlap correlations and I/Q SNR estimation in later examples. No matching
track-specific monitor value or transfer response was acquired here. Those
remain concrete supplier routes; the source check is not an archive-wide
absence claim.

Even white proper Gaussian input becomes temporally correlated under a generic
FIR: for y_n=sum_k h_k x_(nD-k), covariance is proportional to
sum_k h_k conjugate(h_(k+(m-n)D)). Output whiteness needs these nonzero-shift
inner products to vanish. The explicit filter y_n=(x_n+x_(n-1))/sqrt(2)
has adjacent covariance1/2, and contiguous half-records share an input. A
nominal bandwidth equal to sample rate does not establish independence or
uniform error direction. This counterexample is explanatory mathematics,
not a fitted model of the Cassini receiver.

## Proof obligations, imports and review scope

The obligation chain consists of the conditional sphere/Gamma ratio, exact
cone distance, translated amplitude disk, Dirichlet outer exclusion and
spectral Lipschitz bound, all proved above. Ordinary finite-dimensional
probability and projection identities are reconstructed here, not claimed as
new statistical laws. Their composition supplies the stated carrier procedure.
The strongest missing physical step is a validated joint signal/error/measurement
model for the actual receiver interval. That premise is not replaced by a
fitted radius, a frequency optimizer, a covariance estimate or a selected
symmetry. The present observations actively challenge the simplest supplier.

| Input | Role and provenance | Remaining physical bridge |
| --- | --- | --- |
| Constant complex tone per half-record | Explicit candidate signal model | Actual amplitude/phase variation and reference dynamics |
| Uniform direction conditional on training | Stated mathematical probability premise | Receiver and propagation law, filter memory and conditioning |
| Positive error radius | Exact-distribution domain, no radial law supplied | Zero-radius mass would make inequalities conservative |
| Uniform time grid and ideal ADC cells | Instrument-grid/cell model and label conventions | Actual analog transfer, clipping and timing |
| FFT training reference | Declared fitted nuisance, first500 samples only | No physical optimum or true-frequency identification |
| Raw products and flags | Exposed development observations, pinned URLs/hashes | No independent test or calibrated covariance inferred |

The primitive registry and the current realized-state/kinetic-isotropy source
notes were checked. Pointwise realized-state evaluation does not supply a
probability law; kinetic-form isotropy does not supply receiver-error symmetry.
No registry or axiom is changed. The permitted Planck reference concerns units
and is not used to calibrate this receiver or derive a dimensionless scale.

## Review record

The earlier quantization-only exclusion and supplied-discrepancy construction
remain separate conditional results. This note supplies a scale-free probability
construction only under the new angular premise; it does not derive the physical
discrepancy bound left open earlier. Candidate rejection is limited to the joint
signal, direction and measurement model. No earlier result is promoted by this
reconstruction. Integrated landing and independent audit remain future gates.

Independent mathematics was frozen before author-source exposure, with51
separate controls. Independent raw decoding and a separate beta-quantile
implementation reproduce all1200 I/Q digests and all2400 enclosure/exclusion
decisions. Six original numerical-tolerance failures across five Ka records are
preserved: five relative arc-radius differences and one normalized score
difference. The largest arc-radius relative difference is3.3102e-6; the score
difference is0.00061026. A subsequent calculation with a common training
frequency reduces these differences to roundoff scale and identifies strong
conditioning near the arcsine boundary. No tolerance was relaxed and no row
was replaced. Agreement of exclusion decisions does not erase those failed
comparisons. This is computational replication, not additional observations. Author controls, independent checks and later formal
review remain separate. No formal audit verdict or integrated-main validation
is claimed.

## No-Go Discipline Gate

This is a bounded construction plus an exposed-development model diagnostic,
not a universal no-go for scalar gravity, carrier recovery or calibration.
The following are actual distinct attempted mechanisms; none is counted as
exhaustion of the larger research problem.

- N1, scale cancellation — ATTEMPTED: orthogonal projection ratios remove the
  unspecified radial law. The remaining conditional angular premise is explicit;
  physical calibration is not closed by the algebra.
- N1, covariance substitution — ATTEMPTED: the exact axis-supported witness
  has identity-proportional covariance yet rejection.025 at nominal.01, so
  covariance isotropy alone cannot replace direction symmetry.
- N1, validation-based reference selection — ATTEMPTED: maximizing over39
  validation DFT modes gives analytic false-rejection probability approximately
  0.3518716581 at
  nominal.01. The separate training condition matters; simulation checks this
  failure rather than using it as a valid analysis method.
- N1, header-based physical calibration — ATTEMPTED: source definitions and
  decoded FGAIN fields distinguish expected settings from measured noise.
  Actual monitor/calibration products remain a live route.
- N1, filter-based whiteness — ATTEMPTED: the explicit two-tap FIR covariance
  calculation disproves inference from nominal rate/bandwidth alone. It neither
  reconstructs nor rules out a suitable actual calibrated filter response.
- N1, frequency-uniform observation test — ATTEMPTED: the bounded arc and
  spectral search challenge the joint candidate class without fixing the
  validation frequency. Failures and non-enclosures are preserved. Ordinary
  floating execution is not an exact observational exclusion certificate.

N2: no independent-wall count is claimed. The single physical-model obligation
includes signal, conditional direction and measurement correspondence. A table
of logical relationships prevents double counting:

| Pair | Forward implication | Reverse implication | Treatment |
| --- | --- | --- | --- |
| Direction law / unknown radial scale | Ratios remove scale dependence | Scale knowledge does not give direction law | Collapse scale for these tests only |
| Direction law / equal covariance | Not in general when radius depends on direction | Axis-supported witness disproves converse | Neither substituted for the other |
| Correct signal / direction law | No: colored error can accompany an exact tone | No: uniform error can accompany a chirp | Both in the stated joint premise |
| Ideal ADC / angular law | No: ideal cells allow colored error | No: upstream clipping can alter measured cells | Separate measurement condition |
| Uniform grid / training conditioning | No: correlated FIR outputs can share inputs | No: independent blocks can have nonuniform times | Separate declared mathematical domains |

N3: the hidden-condition scan exposes the analog cell, grid, positive ranks,
positive radius and conditional direction assumptions; FFT maxima and
registered products are computational/provenance descriptions. No framework
state, background, covariance or probability law is silently supplied.
N4: no prior no-go is a proof dependency. Current axis-supported, selection and FIR
witnesses attack precisely their named substitutions; the primary instrument
sources establish metadata semantics only, not error-law impossibility.
N5: execution distinguishes ADC components, Fourier modes and finite records;
no spatial-site or lattice-wide conclusion is computed. Cached stdout declares
these scopes explicitly.
N6: scale cancellation is a positive partial closure. A measured transfer
response, suitable guard interval, separately calibrated covariance and justified
error law could reopen confidence inference. No new axiom is asserted necessary.
N7: the strongest counterargument is that a varying coherent signal or known
colored receiver response explains the observed imbalance. The terminal task
is to derive/measure that response and its conditioning, then test a frozen
model on genuinely unexposed data. This is live; the present claim is narrowed
to the explicitly tested supplier.
N8: the prior finite-discrepancy construction left its bound supplied. This
block replaces a radial-scale input only conditional on a new direction premise
and then challenges that premise. It does not recycle the ADC phase-cell
obstruction into a no-go for coherent estimation or claim the original physical
calibration obligation has disappeared.

## Reproduction and current status

Run `python3 scripts/cassini_error_direction_check.py`. With absent pinned
public inputs, run once with `--fetch-inputs` first; acquisition is separate
from scientific execution. The new decoder, estimator, geometry and controls
are self-contained inside this unit. Historical working-protocol manifest
names are provenance; the current manifest contains the same pinned input
bytes and is the only manifest read by the canonical computation.

The primary runner imports every load-bearing helper. No helper-registry policy
edit is required. Sources are declared in `AUDIT_INPUT_PATHS`; the standard
runner-cache envelope binds final source bytes. The independent review lane
still owns complete integrated validation, landing and later audit.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Physical carrier/noise calibration for the revised scalar observation bridge"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Derive a measurement-supported response/signal model or move to a distinct cross-domain scalar constraint."
conditional_surface_status: "Unknown radial scale cancels under conditional uniform error direction and stated analog/cadence premises."
hypothetical_axiom_status: null
admitted_observation_status: "1200 exposed development records; no independent empirical test or scalar inference."
claim_type_reason: "Finite-dimensional conditional construction with explicit physical supplier and numerical limits."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
