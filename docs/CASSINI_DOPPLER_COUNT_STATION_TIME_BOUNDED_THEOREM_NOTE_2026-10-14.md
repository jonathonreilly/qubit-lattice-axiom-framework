# Cassini count reconstruction and finite station-time phase response

**Date:** 2026-10-14
**Status:** proposed_retained
**Claim type:** bounded_theorem
**Actual current surface status:** conditional-support
**Primary runner:** [cassini_doppler_count_bridge_check.py](../scripts/cassini_doppler_count_bridge_check.py)

This note reconstructs one exposed Cassini Doppler product from its archived
precursor counts and derives a finite-count phase response under explicit
clock, transfer and coverage hypotheses. The precursor and processed product
are dependent data. Their agreement is an instrument-conversion check, not an
independent test of gravity. No scalar action, potential, initial state or
absolute scale is selected here.

## Observations and exact target

The development product is `c32easc2002_169_0000xmmmv0`, starting June 18, 2002.
The ODF has 91,863 orbit records, including 91,664 Doppler records: 61,459
two-way, 29,556 three-way and 649 one-way. Its ATDF precursor has 160,870
tracking records. All matched Doppler endpoints identify Block V receivers,
positive bias field 1000, sky-level reference and a synthesizer reference flag.
The ODF receiver/exciter-independent flag is one. These are decoded metadata,
not a claim that every instrument calibration is known.

**Exact target:** within the stated counter and receiver domain, reconstruct
the stored Doppler values without fitted constants; for a prescribed coherent
phase map, derive its station-clock finite-count operator and a rigorous
endpoint-displacement error bound on verified frequency coverage.

The tracked [source manifest](../scripts/cassini_doppler_development_inputs.json)
pins URLs, lengths and SHA-256 values. It binds the ODF
`39a658fd74044783b598c947f54dc97dee755c8499a58d7f371831e3f2792e5f`
and ATDF `215c2de473fd00b278267ab3ff0431ab4d00e9c3baaa17e949105b964644f4f3`.
The original campaign protocol exposed this development product before model
construction. An extension registered the matching ATDF before its download.
Separately reserved calibration and within-experiment validation products
remain unopened at this checkpoint. The published Cassini gamma summary was
already exposed; it supplies no validation result here.

## Counter decoding, history and the receiver convention

Let H,I,L be the three stored count parts. The correct count is

    N = (H*10^14 + I*10^7 + L)/10^6 cycles.

The product label instead supplies H*10^6 cycles for the high part. The
[PDS ATDF interpretation guide](https://pds-geosciences.wustl.edu/radiosciencedocs/urn-nasa-pds-radiosci_documentation/DSN_TRK-2-25/tdf_unpack.pdf),
Table 5 and Appendix B(3), explicitly corrects the underlying documentation.
Its example H=16,I=4398198,L=1475000 gives 1643981981.475 cycles. This example
is checked independently of the Cassini comparison. Raw extraction is retained;
only the decoded count scale changes.

Write M=2^32 cycles. If each counter lies in [0,M), there is no reset during
the interval, and the true increment satisfies 0<=DeltaN<M, then

    DeltaN = N_end-N_start + M*1[N_end<N_start].

Proof: the raw difference is in (-M,M); exactly one representative modulo M
lies in [0,M). This proves uniqueness within the stipulated interval, not the
physical history bound itself. For example, endpoint counts 11 and 37 occur
both for an increment 26 and for 26+M. The second history is a constructive
alias witness outside the chosen domain. The standard modulo-reset correction
is documented in [Morabito and Asmar, 1995](https://tda.jpl.nasa.gov/progress_report/42-120/120B.pdf),
section III.C. The bound/no-reset condition remains explicit rather than being
declared derived from two endpoints or from a small residual.

In the checked receiver domain, T is the positive reception count interval
in seconds and C=DeltaN/T. For the coherent two-way and three-way records,

    D_reconstructed = C - 10^6 Hz.

For the one-way records, let F_A be the stored ATDF receiver reference, using
the S-band normalization in this conversion, and F_O the ODF nominal S-band
spacecraft reference. The ATDF level flag alone is not a physical-frequency
calibration; the conversion also uses the legacy band/reference definitions. Then

    D_reconstructed = C - 10^6 - [(880/221)F_A - (11/3)F_O].

The factors are instrument band/reference conversions, not a scalar coupling
or an inferred transponder law. The old format's X/S factor 11/3 and receiver
S-band multiplier 240/221 give 880/221. The positive bias is1000 kHz. The
one-way subtraction retains the distinct spacecraft reference. These conventions
are reconstructed using [TRK-2-18, June 2000](https://pds-geosciences.wustl.edu/radiosciencedocs/urn-nasa-pds-radiosci_documentation/DSN_TRK-2-18/dsn_trk-2-18.2000-06-15.pdf),
Appendix A, and [Moyer, 2000](https://descanso.jpl.nasa.gov/monograph/series2/Descanso2_all.pdf),
sections 13.2.4 and 13.2.6. Later ODF definitions are not silently substituted.

For the pre-NSP Block V description, the synthesized count phase has the form
N(s)=F_ref*s-Phi_received(s)+C4*s+constant. Subtracting the documented bias
therefore gives reference cycles minus received cycles per reception interval.
After the one-way reference adjustment above, the same difference uses the
nominal spacecraft reference instead. This derivation explains the sign and
offset; its successful precursor reconstruction supports that convention on
this product. It does not establish calibrated physical proper-time frequency
or every hardware/electronic delay. An unknown phase slip or reset requires its
own term. The coherent turnaround ratio below is a separate quantity k.

## Full development comparison and preserved failure

The first implementation followed the label literally and kept unwrapped
differences. Of 91,664 Doppler rows, 91,663 had unique endpoint records; 999
failed the fixed storage-quantum comparison and one had duplicate endpoint
records. That failed source, output and row hash are preserved in the campaign.
The primary PDS correction then repaired 978 high-part carries; 21 remaining
events use the documented modulo correction under the stated history domain.

The duplicate occurs at ODF record 4100: ATDF records 25901 and 25902 have
identical first count and reference but different high/low-rate and quality
fields. Both variants are retained. Their identical conversion states make the
reconstructed value unique without choosing a variant by its Doppler residual;
quality provenance remains nonunique. The field labeled total slipped cycles
(item87) is also retained for every endpoint; it has nonzero values in the
development data. Its receiver-specific interpretation and phase-history effect
remain application work. Stored-value agreement does not establish slip-free
physical phase transfer.

The corrected computation accounts for all 91,664 Doppler rows. It retains all
quality groups and uses no residual clipping. Largest absolute difference from
stored ODF is 7.60550527903469e-7 Hz; the largest coherent difference is 4.73e-7 Hz.
All rows lie within the comparison scales 2e-6/T+1e-9 Hz, with the one-way scale
also including (11/3)*1e-3+(880/221)*1e-6Hz for reference storage quanta.
These scales describe stored-number comparisons. Neither they nor the much
smaller observed differences certify instrumental accuracy or legacy arithmetic.

Countermodels remain executable: the wrong label scale produces 999 failures,
omitting rollover produces 21, wrong bias units and reversed count sign each
produce 91,664, and omitting the one-way reference term produces 649. Counts
refer to this pinned development product and fixed reconstruction, not a new
statistical likelihood or independent samples of gravity.

## Station clocks and the coherent phase operator

Let t_i be coordinate time, tau_i proper time and s_i the actual station clock
coordinate at the relevant electronics event. Set w_i=d tau_i/dt_i>0 and
g_i=ds_i/d tau_i>0. Neither station time nor its archived label is equated to
proper time or UTC. Let transmitted phase be Theta_e(s_1), with f=dTheta_e/ds_1,
and adopt the explicitly conditional phase law

    Theta_r(s_3) = k Theta_e(s_1(s_3)) + constant.

The retarded map is prescribed, uniquely selected and temporally ordered on
the integration interval; k is fixed. With J=dt_1/dt_3, the chain rule gives

    f_received = k f(s_1) (g_1*w_1)/(g_3*w_3) J.

For reception endpoints c<d and mapped emission endpoints a<b, exact received
cycles are k integral_a^b f(s)ds. The clock factors are already in the endpoint
map and frequency definition. Multiplying this integral by another clock ratio
changes the model. Physical clock effects still determine that endpoint map.
For known reference phase increment R and T=d-c>0,

    D = [R - k P(a,b)]/T,   P(a,b)=integral_a^b f(s)ds.

This is a self-contained consequence of the stated phase/reference law; it
does not import an unmerged theorem as authority. It reconstructs the phase
bookkeeping used in Moyer's Eq. 13-50. Independently known R is needed for an
absolute value; comparing models at identical R,k,T cancels only their shared
reference. The finite algebraic example (P,R)->(P+h,R+k*h) preserves D and
illustrates why supplying an arbitrary per-record reference adds freedom.

## Endpoint sensitivity with an explicit error domain

Keep R,k,T and the transmitted phase function fixed. If the modeled round-trip
station-time changes at the two endpoints are delta_s and delta_e, the new
emission endpoints are a-delta_s,b-delta_e. Oriented integration gives exactly

    DeltaD = k/T [integral_(b-delta_e)^b f(s)ds
                  - integral_(a-delta_s)^a f(s)ds].

Suppose f is Lipschitz on each full endpoint-displacement interval, with
constants L_e,L_s, and all those intervals have verified frequency coverage.
Then

    DeltaD_linear = k/T [f(b)delta_e - f(a)delta_s],
    |DeltaD-DeltaD_linear| <= |k|/(2T)(L_e*delta_e^2+L_s*delta_s^2).

At either endpoint x, subtract f(x)delta from the oriented integral and write
the difference as integral_0^delta[f(x-u)-f(x)]du. Its magnitude is bounded
by L*delta^2/2 for either sign of delta. The triangle inequality gives the
two-endpoint result. For affine ramps with endpoint slopes r_e,r_s the exact
remainder is -k/(2T)(r_e*delta_e^2-r_s*delta_s^2).

With delta_c=(delta_e+delta_s)/2 and delta_d=delta_e-delta_s, the linear term is

    k/T [(f(b)-f(a))*delta_c + (f(b)+f(a))*delta_d/2].

A common endpoint shift cancels for constant frequency; a duration error
retains the carrier coefficient. A ramp generally retains a common-shift
response. A clock-origin relabeling also moves the ramp epochs and preserves
phase, unlike moving physical endpoints against a fixed frequency ledger.
No station-clock precision or probability distribution has been supplied.

## Finite ramp integration and a discontinuity witness

For integer-nanosecond endpoints A,B and ramp origin S, stored start frequency
F in nano-Hz and slope R_f in nano-Hz per second, exact phase on that segment is

    F*(B-A)/10^18 + R_f*((B-S)^2-(A-S)^2)/(2*10^27).

Sum clipped segments with rational arithmetic. The implementation rejects
gaps, overlaps, mixed stations/levels and extrapolation. Across a contiguous
frequency jump the integral still exists, but a segment-slope Lipschitz bound
does not apply. The explicit frequency 10 before zero and 30 after zero yields
4 cycles on [-.1,.1], whereas 30*.2 gives 6 cycles despite zero segment slopes.
This is a constructive counterexample to that particular shortcut.

The product has 69 ramps, two gaps and 17 nonzero contiguous frequency jumps.
All91,664 nominal receiver intervals have coverage, but that does not establish
coverage at retarded transmitter endpoints or identify a receiver tuning ramp
as the transmitted phase ledger. The physical map must make that distinction.

## Obligation graph, imports and scope

| Component | Role and provenance | Proof or remaining application work |
| --- | --- | --- |
| Binary layouts, corrected count scale, bias/reference conventions | Imported instrument definitions from pinned PDS/JPL sources | Checked against published example, independent extraction and the complete exposed precursor comparison |
| Forward count increment in [0,2^32), no reset | Explicit bounded-history condition | Uniqueness within that domain proved above; physical history remains an input |
| Coherent phase law, fixed k, electronics endpoints and retarded map | Explicit measurement premises | Chain-rule and finite-count identities proved here; real hardware, clocks and propagation need modeling |
| Known reference and frequency ledger, fixed reception interval | Imported calibrated functions for a physical application | Exact integration and conditional difference response derived; real accuracy remains to be established |
| Lipschitz endpoint coverage | Mathematical hypothesis | Integral inequality proves the bound; jumps/gaps handled explicitly |
| Exposed June 18 archive | Development data, dependent precursor/product pair | Verifies stored conversion; supplies no independent gravity test |
| Candidate scalar action, potential, initial state, scales and environment | Outside the proved conversion theorem | No selection or retirement asserted |

All intermediate mathematical obligations are supplied by the displayed
definitions and proofs. The strongest next application obligation is the
candidate-consistent retarded worldline/clock/media model with a controlled
error budget. It is not hidden as an assumed terminal lemma proving the scalar
theory. The present result removes ambiguity in a particular stored conversion;
it leaves physical measurement accuracy and the fundamental theory open.

## Execution and review record

The primary runner directly imports all five helper modules. Its declared
inputs bind this note, the source manifest, helper bytes and exposure protocols.
On a fresh checkout it downloads only the pinned development data/labels into
`outputs/cassini_doppler_inputs`; mismatched bytes or unavailable sources fail
the run. It needs Python, SymPy and working HTTPS trust; certifi is used when
installed. Its declared cache timeout is 240 seconds. Outputs and complete row
accounting are under `outputs/cassini_doppler_bridge`; no raw data are committed.
The source proof supplies the general result; finite controls corroborate it.

The author endpoint runner has 526 exact/symbolic checks; a separate independent
calculation supplies 2417 checks using nonlinear clocks and non-affine Lipschitz
functions. The ramp implementation has 16 synthetic controls and a separate
all-record/interval calculation. Independent extraction checks every ODF field;
focused ATDF reconstruction review binds final source identities in the campaign
review record. This is not a formal audit verdict or completed landing review.

The failed literal-label route remains part of the evidence. Original exploratory
notes that left the receiver convention unidentified retain their historical
scope; this note narrows that uncertainty through the precursor comparison.
No family-wide impossibility or exhausted theory-search claim is proposed.
The finite alias and jump witnesses above stand as explicit configurations.
Full integrated landing checks and independent audit remain outstanding.

## Claim-status record

```yaml
target_claim_id: cassini_doppler_count_station_time_reconstruction
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
conditional_surface_status: "Stored-count reconstruction and finite phase response under explicit receiver, history and clock hypotheses"
hypothetical_axiom_status: null
admitted_observation_status: "One exposed development precursor/product pair; no independent empirical gravity test"
claim_type_reason: "Positive count reconstruction and phase/error identities with explicit domains"
audit_required_before_effective_retained: true
bare_retained_allowed: false
trace_class: upstream_support
target_blocker_text: "Derive the measured-gravity bridge rather than supply its instrument identification"
source_of_blocker_text: user_goal
reachability_to_target: "Fixes count sign, scale and reference conversion and supplies a finite phase error operator for a later candidate-consistent gravity comparison"
artifact_role: "Conditional instrument reconstruction and analytic observation operator"
next_trace_action: "Reconstruct retarded emission coverage and station/media/trajectory errors before calibration and reserved-track testing"
```
