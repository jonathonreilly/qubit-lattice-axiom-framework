# Cassini carrier reconstruction and a calibrated finite-voltage feasible set

**Date:** 2026-10-15
**Status:** conditional-support
**Claim type:** bounded_theorem
**Actual current surface status:** conditional-support
**Primary runner:** [cassini_carrier_reference_check.py](../scripts/cassini_carrier_reference_check.py)

This unit reconstructs the reference used by one exposed Cassini tracking
product, compares it with a declared estimator on simultaneous raw radio
samples, and derives what an independently supplied voltage-discrepancy bound
would imply for carrier frequency and phase. The samples reject an especially
restrictive constant-amplitude, quantization-only model. They do not determine
a physical noise upper bound, scalar residual, action, initial field state,
absolute scale, or environmental solution.

## Observation and exact target

The development window is day 169 of 2002, UTC seconds `[48900,49500)`.
Both complete 1335 X and Ka RSR products were already exposed before this
block. The 600 one-second sample blocks per band and simultaneous tracking
product are development data. No reserved product was opened, no independent
empirical gravity test was performed, and no window was selected by its fit.

The exact target has two parts: derive a finite-data carrier feasible set
conditional on a specified discrepancy class; reconstruct the archived
receiver reference and assess a predeclared carrier approximation against
simultaneous counts without fitting a reference scale, bias, sign or time shift.
Estimating one frequency and one complex amplitude per block is explicitly
three fitted real parameters, not an assumption-free extraction of physical phase.

The [RSR manifest](../scripts/cassini_rsr_development_inputs.json) pins the
two products and two labels. The [tracking manifest](../scripts/cassini_doppler_development_inputs.json)
pins ODF, ATDF and labels. Analysis choices were frozen in the campaign's
`receiver_reference/DEVELOPMENT_PROTOCOL_v1.json`, its exact-integer
supplement, and `REFERENCE_COMPARISON_FREEZE_v1.json` before their respective
calculations. Original failed implementations and all output identities remain
in that pack. The later 1656/1657 raw products remain unopened.

## Receiver reference from the documented processing branch

[Moyer (2000)](https://descanso.jpl.nasa.gov/monograph/series2/Descanso2_all.pdf),
sections 13.2.4 and 13.3.1.2, distinguishes the receiving station's reference
from the actual transmitted uplink. For the pre-NSP Block-5 branch, the MDA
constructs a counter, in cycles,

    N(t) = f_REF*(t-t0) - Phi_R(t) + C4*(t-t0),
    Phi_R(t) = integral^t f_R(s) ds.

Here `t` is the receiver station-time coordinate. For the selected coherent
branch, subtracting `C4` from the count rate yields

    D = DeltaN/T - C4 = f_REF - DeltaPhi_R/T.

The receiver reference uses the receiving exciter band. In these 600 ODF
records the receiver is DSS-25, transmitting station DSS-54, exciter band S,
uplink band X, downlink band X, and compression interval one second. Matched
ATDF endpoints identify receiver type 5, frequency level 1, bias `1000 kHz`
and synthesizer flag 1. The constant reference has value

    Fstored = 2117064000 Hz,
    f_REF = (880/221)*Fstored = 1863016320000/221 Hz.

Level 1 is the sky-level exciter quantity. The S-exciter/X-downlink ratio
`880/221 = (11/3)*(240/221)` already includes the relevant band conversion.
No additional factor 96, 11/3 or spacecraft X/X ratio 880/749 is inserted.
The finite received-frequency reconstruction is consequently

    mean f_R = (880/221)*Fstored - D
             = (880/221)*Fstored + 10^6 - DeltaN/T.

The [2000 ODF specification](https://pds-geosciences.wustl.edu/radiosciencedocs/urn-nasa-pds-radiosci_documentation/DSN_TRK-2-18/dsn_trk-2-18.2000-06-15.pdf)
Table 3-3b and Appendix A distinguish the reference encoding, band fields
and general bias construction. The ODF reference is a split 46-bit mHz
integer; ATDF uses two decimal-scaled fields. The code checks both encodings
against each other and retains every matched endpoint variant and its selected
decoded quality/slip fields; this is not an extraction of every ATDF field.
This is the selected pre-NSP branch, not a universal inversion of every ODF.
Neither a nonzero flag nor agreement of processed values proves the historical
physical calibration. Source provenance for this branch remains a premise.

For an unsigned counter modulo `2^32` cycles, the smallest nonnegative
increment uses one wrap when the end counter is below the start. Its physical
interpretation assumes no reset and a true increment in `[0,2^32)`.
Adding any whole modulus gives the same endpoints. The raw values, wrap
choice and nonzero slip diagnostics remain visible; this history condition
has not been derived from a small comparison residual.

The receiving reference is evaluated at reception. A transmitting ramp at
retarded emission time belongs to the distinct propagation phase integral.
There is no transmitter-ramp substitution in the calculation above.

## RSR reference, sign and finite-interval qualifications

The [2001 RSR specification](https://pds-geosciences.wustl.edu/radiosciencedocs/urn-nasa-pds-radiosci_documentation/DSN_0159-SCIENCE/dsn_0159-science.2001-02-28.pdf),
sections 2.4–2.6, documents

    f_sky = 10^6*(LO_RFIF + LO_DDC) - F_NCO + f_residual.

LO header fields are MHz; frequency coefficients and residual frequency are Hz.
The corrected recorded voltage is `z=(2I+1)+i(2Q+1)` in scaled ADC units.
[Border and Paik (2009)](https://ipnpr.jpl.nasa.gov/progress_report/42-177/177C.pdf),
section V, p.10, describes `I+iQ` as positive rotating actual-minus-predicted
phase plus noise, and explains the opposite signs of SFDU and prediction
coefficients. That paper concerns later RSR experiments, so it supports the
instrument convention without certifying the 2002 software 2632 configuration.
Our transform is `sum z_n exp(-2*pi*i*f*t_n)`, giving a positive frequency for
a positive rotating tone. Both signs are nevertheless recorded in the
predeclared development comparison.

Write the archived continuous phase polynomial in cycles as

    P(u) = P1 + P2*u + P3*u^2 + P4*u^3.

The original specification loads phase at a millisecond's start and frequency
at its midpoint. The day-169 labels instead use the midpoint argument for
phase too. The previous adjacent-polynomial check did not distinguish them.
Both polynomial readings, `delta=0` and `delta=1/2000` seconds, are retained:

    DeltaP(delta) = P(1+delta)-P(delta)
                 = P2 + P3*(1+2*delta) + P4*(1+3*delta+3*delta^2).

All GHz-scale subtraction uses exact fractions of the archived IEEE values.
The ideal derivative relations are `F1=P2,F2=2P3,F3=3P4`, but separately
rounded archived fields need not satisfy them as exact rational identities.
The final calculation uses the declared P fields. The original working
calculation integrated F instead; that protocol mismatch is preserved and
corrected, despite its tiny numerical effect on this window.
Only the fitted residual is a floating estimate. The comparison candidate is

    mean f_R,approx = LO - DeltaP(delta) + sign*f_hat.

This is a continuous-polynomial candidate, not a complete reconstruction of
hardware register dynamics. For example, an ideal midpoint-held frequency
over a millisecond `h` has phase increment `h*F(u+h/2)`, while a quadratic
frequency polynomial has integrated increment differing by `F3*h^3/12`.
Actual phase loading, filtering and timestamp compensation need their own
validated model. They are not inferred by picking the smaller comparison RMS.

The RSR samples occupy `t=second+n/1000`, `n=0,...,999`; the ODF count
interval is `[second,second+1]`. A fitted voltage frequency is generally
different from an interval phase increment. Replacing the latter by the
fitted slope imports a local carrier-model approximation and a common time
identification. The 100 ns timing specification is not an empirical error
certificate for this track.

## Carrier geometry with a supplied discrepancy bound

Let `N>=1`, let `u_f,n=exp(2*pi*i*f*t_n)`, and write a candidate finite
voltage model `z=c*u_f+eta`, with unrestricted complex `c`. This is a class
of candidate approximations, not a derived radio-noise law. Define

    c_hat(f) = u_f^*z/N,
    E(f) = ||z||^2 - |u_f^*z|^2/N.

Orthogonality of `z-c_hat*u_f` to `u_f` gives the exact identity

    ||z-c*u_f||^2 = E(f) + N*|c-c_hat(f)|^2.                 (1)

If a separately justified total discrepancy bound `||eta||<=B`, `B>=0`, is supplied,
the feasible frequency set, allowing `c=0`, is exactly `{f:E(f)<=B^2}`.
For a feasible `f`, amplitudes form the closed disk

    |c-c_hat(f)| <= rho(f),   rho(f)=sqrt((B^2-E(f))/N).    (2)

These are necessary and sufficient: (1) proves necessity; choosing any point
in the disk and setting `eta=z-c*u_f` proves sufficiency. If a nonzero carrier
is required, remove `c=0`; a disk consisting only of zero then supplies no
carrier. If a lower amplitude `|c|>=a_min` is additionally calibrated, the
minimum possible error becomes

    E(f) + N*max(0,a_min-|c_hat(f)|)^2.

That amplitude supplier must also be stated, not silently inferred from the fit.

Here `B` bounds total discrepancy from the recorded center vector. If a bound
`B_phys` instead applies to analog model discrepancy before ideal quantization,
the triangle inequality gives the sufficient center bound
`B=B_phys+sqrt(2N)`. This outer ball generally loses the cell geometry and is
not an exact equivalence for the physical-plus-quantizer model.

For `0<=rho<|c_hat|`, the disk avoids zero and its carrier phases have the
sharp angular enclosure

    |Arg(c/c_hat)| <= asin(rho/|c_hat|).

Here `Arg(c/c_hat)` is the circular angular separation, not a difference of
two principal arguments across their branch cut. The tangent from the origin
to the disk proves sharpness. Divide by `2*pi`
for cycles. At `rho=|c_hat|>0` the disk touches zero; nonzero phases approach
but do not attain the two tangent directions, giving an open semicircle.
At `rho>|c_hat|` every phase occurs. A zero center requires its own zero/nonzero
case. These phase enclosures concern the candidate complex amplitude at the
chosen reference time; conversion to physical endpoint phase requires the
waveform/reference/time identification above and, where relevant, integer lifts.

The minimum fitted residual is a lower bound on discrepancy required by this
model class, not an upper bound on the physical discrepancy. Without any
restriction on `eta`, for every frequency and every nonzero `c` the assignment
`eta=z-c*u_f` reproduces the same finite samples. A fitted zero residual can
even coexist with a different true tone plus an exactly compensating
discrepancy. This constructive nonidentification statement is restricted to
the unrestricted additive-discrepancy class. It does not rule out identification
from known waveform dynamics, calibrated injected tones or a justified noise law.

## Exact quantization-cell rejection of constant modulus

Assume each unsaturated ideal midrise cell is enclosed by a closed square of half-width one about
the corrected integer center `z_n=x_n+i*y_n`. This is an explicit quantizer
premise; total analog voltage is not identified with carrier voltage. Write
`r_n=|z_n|`. Any constant-modulus waveform `v_n=r*exp(i*theta_n)` obeys

    ||z-v||^2 >= sum (r_n-r)^2
              >= S - (sum r_n)^2/N,    S=sum r_n^2.

The first inequality is the reverse triangle inequality; minimizing the
quadratic in `r>=0` gives the second. Set the exact integer
`C=sum ceil(sqrt(x_n^2+y_n^2))`. Since `sum r_n<=C`, every such waveform
has residual at least `S-C^2/N`. Any vector inside the ideal cells is at
distance at most `sqrt(2N)` from the centers. Therefore the integer condition

    N*S-C^2 > 2*N^2                                         (3)

rejects every constant-modulus waveform within those cells, including a
constant-amplitude tone of any frequency or phase. No FFT result enters this
certificate. This is a sufficient rejection criterion, not a necessary one.

There is also an exact necessary and sufficient closed-cell criterion for arbitrary
sample phases with one common modulus. Each cell's possible squared radii run
continuously between

    l_n = max(|x_n|-1,0)^2 + max(|y_n|-1,0)^2,
    h_n = (|x_n|+1)^2 + (|y_n|+1)^2.

A common modulus exists iff `max l_n <= min h_n`. Continuity on each connected
square fills its radius interval, and intersection supplies a point in every
cell. Arbitrary phases need not form a tone, so acceptance does not prove a
coherent carrier. Both exact tests reject all 1200 observed blocks. Extreme
code and origin-reaching flags are zero in this fixed window, and all samples
are retained. This rejects constant analog modulus plus ideal quantization
alone; it does not distinguish amplitude modulation, other signals, propagation
effects, gain variation or noise, and supplies no physical noise upper bound.
If the actual quantizer uses half-open cells, equality in the closed-cell
intersection can be feasible only on an excluded boundary. The iff statement
applies to the closed enclosures; strict exclusion still applies to any subset.

## Numerical estimator and development results

For each block the estimator minimizes unweighted single-tone squared error
over a 16000-point FFT grid covering one sampled-frequency period, followed
by bounded local refinement around the strongest bin. Its returned solution
is a numerical local refinement, not a certified global maximizer. With
centered times, `A(f)=sum z_n exp(-2*pi*i*f*t_n)` satisfies

    |A(f)-A(g)| <= L*|f-g|,   L=2*pi*sum |t_n*z_n|.

The inequality follows termwise from `|exp(ix)-exp(iy)|<=|x-y|`.
A grid with covering radius `q` bounds the true maximum magnitude by
`max_grid |A|+L*q`, with the sampled-frequency seam handled periodically
in magnitude. This is an analytic covering theorem. Its floating FFT
evaluation is recorded as a numerical diagnostic, not an interval certificate.
Changing the time origin leaves magnitudes unchanged but rephases the complex
correlation; a centered derivative bound must not be assigned to an uncentered
complex correlation without that rephasing.

All 600 X-band and 600 Ka-band numerical fits completed. Median fitted
single-tone fractions of total corrected-voltage energy are 0.5363141 and
0.5851255 respectively. They are descriptive projections, not physical SNRs.
All 1200 blocks fail both exact constant-modulus cell tests. The code does not
reject blocks or reinterpret residual energy as thermal noise.

The matched X-band comparison is:

| RSR spectral sign | Phase argument shift | RMS difference from tracking mean sky (Hz) |
|---|---:|---:|
| + | 0 | 0.06642541944 |
| + | 0.5 ms | 0.06642635395 |
| − | 0 | 0.82041769874 |
| − | 0.5 ms | 0.82052780837 |

For the source-supported plus sign and zero shift, the signed mean difference
is -0.0004016645353 Hz, median 0.00006966959 Hz, and range
[-0.2170102366,0.3113512511] Hz. No offset or time shift was fitted.
The source-supported sign is consistent with the exposed data; the comparison
does not by itself identify a physical convention or provide a confidence level.
Both timing alternatives remain unresolved. All 600 ODF flags are good, but
54 matched ATDF endpoint occurrences have nonzero unsigned slip diagnostics;
none are removed or treated as signed corrections. ODF and counter-derived
sky values agree within 4.39e-7 Hz, a dependent storage comparison only.
There is no simultaneous Ka tracking-frequency validation in this product.

A separately frozen 32768-bin/direct-Newton implementation agrees with 1199
of the 1200 fitted frequencies within its predeclared 2e-5 Hz comparison
tolerance. The remaining Ka block, second 49112, is a real numerical
discrepancy: the original route gives +0.92517469095 Hz, while the independent
route finds -0.53222627866 Hz with lower squared residual. Direct correlation
and refinement of both peaks confirms residual energies 308885791468.964
and 308532966242.017 in squared corrected-code units. The frequencies differ
by 1.45740096962 Hz. A 65536-bin diagnostic also finds the negative-frequency
neighborhood. Both candidates and original estimates are preserved; no
single-row override, tolerance relaxation or physical frequency choice is made.
The local-search limitation is therefore demonstrated on exposed data, not
merely hypothetical. All X-band fits pass the independent comparison, so this
Ka discrepancy does not alter the table above. The separately implemented
integer cell certificates agree for all 1200 blocks.

## Surviving assumptions and route boundary

The archival reference scale and a source-supported complex sign have now
been reconstructed and checked on exposed observations. They are instrument
reconstructions conditional on historical applicability, not new axioms of a
scalar theory. Remaining suppliers include physical timing and phase transfer,
calibrated discrepancy or noise model, waveform adequacy, counter resets/slips,
plasma and trajectory separation, same-environment gravity identification,
scalar action/potential, actual initial state and dimensional scales.

The useful next route is to calibrate or constrain those suppliers using
documented reference signals, redundant observations or physical dynamics.
Choosing a fitted noise radius would not retire them. The exact geometry gives
a place for a justified supplier to enter and a way to reject incompatible
candidates; it does not supply the supplier.

The negative scope is deliberately finite. N1: target is finite sampled
single-tone/constant-modulus reconstruction. N2: additive-discrepancy and ideal
cell domains are explicit. N3: countermodels and integer certificates are
constructive. N4: focused independent checks are preserved in the campaign
pack. N5: a genuinely supplied bound yields the positive feasible-set theorem.
N6: waveform restrictions or calibrated references reopen identification.
N7: input, protocol, source and result hashes identify the exact attempt.
N8: this is upstream conditional support, not a no-go for carrier estimation,
the revised scalar theory, or observation-driven theory construction.

## Reproduction and evidence status

Run `python3 scripts/cassini_carrier_reference_check.py` with the pinned public
inputs in the declared caches. `--fetch-inputs` performs acquisition separately;
the scientific execution itself makes no network call. Outputs retain all
estimates, exact cell certificates, endpoint metadata, sign/timing alternatives
and comparison rows. Synthetic controls check complex projection, phase-disk
boundaries, finite-frequency conventions and deliberately incompatible models.
The campaign evidence pack records independent scope and source correspondence.
No formal audit verdict or integrated-main result is claimed here.
