# Integer channel calibration and receiver phase representation

**Date:** 2026-10-15
**Status:** conditional-support
**Claim type:** bounded_theorem
**Actual current surface status:** conditional-support
**Primary runner:** [scalar_channel_calibration_check.py](../scripts/scalar_channel_calibration_check.py)

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: scalar_channel_calibration
target_blocker_text: "Derive or eliminate the measured-gravity assumptions rather than supplying them"
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Derive the physical carrier estimator and reference-phase map before interpreting a scalar residual"
conditional_surface_status: "Exact channel character and ADC-cell implications under declared phase, plasma and receiver premises"
hypothetical_axiom_status: null
admitted_observation_status: "Two complete Cassini day169 RSR products exposed as development under a frozen preaccess protocol; no independent empirical test"
claim_type_reason: "Conditional character classification and finite receiver representation; actual carrier calibration and scalar theory inputs remain open"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The target is to derive the integer characters that simultaneously remove
whole-cycle histories, the two supplied plasma columns and constant receiver
origins, then determine what a recorded receiver voltage can support about
those characters. The downstream consumer is a calibrated observation-space
constraint on a scalar response. No actual scalar residual is identified here.

The obligation graph is explicit: the supplied three-channel phase law gives
two nuisance columns; their real null line plus integrality gives the endpoint
lattice; receiver-origin invariance gives the temporal kernel; direct
substitution gives common-phase sensitivity. These steps are proved below.
Conditional ADC geometry then gives finite-code phase images. The strongest
missing application lemma is a physical carrier/reference-phase estimator with
a justified error set, waveform class and clock/propagation map. It is not
assumed in order to turn a voltage statistic into a gravity result.

## 1. Model and the information being discarded

At each matched endpoint i, three received phases in cycles satisfy

    Phi_i = g_i G_i + a_i U_i + d_i D_i + b + n_i + e_i (mod 1),
    g_i = (k1 fX_i, k2 fX_i, k3 fK_i),
    a_i = (k1/fX_i, k2/fX_i, k3/fK_i),
    d_i = (1/(k1 fX_i), 1/(k2 fX_i), 1/(k3 fK_i)),
    k = (880/749, 3344/749, 14/15), rho_i=fK_i/fX_i>0.

The shared uplink/downlink columns use an explicitly supplied leading cold-plasma,
common-ray model. Frequencies are the appropriate supplied matched-event
frequencies; rounded frequency labels do not fix their exact ratio. G, U and D
are scalar endpoint quantities, b is an arbitrary constant three-channel offset
within this segment, n is an arbitrary integer history, and e is fractional error
with no default bound. Shared ray mapping, coherent transfer, clock alignment,
actual reference phases and electronics remain physical premises. Allowing U_i
and D_i arbitrary independently is a deliberately large nuisance class, not an
observed claim about the solar plasma. Relaxing it can restore information.

Every continuous function of the torus phases can be analyzed by its integer
Fourier characters exp(2*pi*i*sum_i N_i dot Phi_i). Invariance under all U_i,D_i
forces N_i dot a_i=N_i dot d_i=0 separately. Invariance under b forces sum_i N_i=0.
Conversely these identities suffice. Fourier averaging/Fejer approximation shows
that these allowed characters describe all continuous invariants. For dense
nuisance orbits the Hausdorff observable quotient is by their closure; no claim
is made about arbitrary discontinuous set-theoretic invariants.

## 2. Endpoint lattice derived from the exact turnaround ratios

Direct cross product, denominator clearing and primitive reduction gives

    (a,b,c)=(-3007586755,305348069,2325375360), gcd(a,b)=1,
    a*k1+b*k2+c*k3=0,
    a/k1+b/k2+c/k3=0, c*k3=2170350336.

The real simultaneous annihilator is N_i=m_i(a,b,c*rho_i).
Since gcd(a,b)=1, integrality of its first two entries forces m_i integer.
The remaining condition is c*rho_i*m_i integer. Thus an irrational rho_i
permits only m_i=0. For reduced rational rho=p/q, its primitive generator is

    N=(a*q/g,b*q/g,c*p/g), g=gcd(q,c).

No decimal approximation to a physical ratio is promoted to this exact premise.
The common signal coefficient is

    N_i dot g_i = c*k3*m_i*fX_i*(rho_i^2-1).

At rho=1 it vanishes. Existence of a nonzero nuisance-invariant character alone
is not sufficient to infer surviving G sensitivity.

## 3. Receiver offsets and time-varying ratios

The exact constant-offset conditions are

    sum_i m_i=0, sum_i m_i*rho_i=0,
    m_i integer, c*rho_i*m_i integer at each endpoint.

Irrational-ratio endpoints have m_i=0. On r rational endpoints the lattice rank
is r-rank_Q([1;rho]), with rank zero when r=0. Denominator restrictions change
the lattice spacing but not its rank. Two distinct ratios leave only zero;
three rational endpoints admit weights proportional to
(rho2-rho3,rho3-rho1,rho1-rho2), with denominators cleared. Equal ratios give
ordinary temporal differences. The surviving functional is the sum of the
G coefficients above; it can still vanish identically. For example ratios
(1,1,2) force the third weight zero, and both others have zero G coefficient.

Changing weights can be written in measured temporal count increments when
their channel-wise sum is zero: sum_i N_i Phi_i = sum_{j=1}^{J-1}
[-sum_{i<=j}N_i] dot (Phi_{j+1}-Phi_j). All coefficients remain integer.
This is an observable construction; it does not select a physical field history.

## 4. Robustness is an additional obligation

A fixed nonzero N cannot cancel both columns for every rho in a nonempty
interval: the constant and reciprocal-rho terms must vanish separately,
forcing N3=0 and then N1=N2=0. At nominal rho0 with N=m(a,b,c*rho0), the
actual leading plasma leakage at rho is exactly

    c*m/fX*(rho0/rho-1)*(k3*U+D/k3).

Without bounds on U,D, no nonzero ratio error guarantees small leakage.

For an integer character and a rectangular error set |e_il|<=epsilon_il,
its phase error ranges over [-eta,eta], eta=sum|N_il|epsilon_il. It covers
the whole output circle once eta>=1/2. This statement for a single character
alone does NOT show that all joint quotient information is lost.

For a sufficient joint statement: at each rational endpoint the primitive
plasma quotient is one circle. If the error box maps onto that entire circle
independently at each endpoint, the product covers the whole endpoint quotient
and therefore also its constant-offset quotient. Irrational endpoints already
have trivial continuous quotient. Uniform first-two-channel error bounds
epsilon>=1/[2*(|a|+|b|)]=1/6625869648 cycles suffice for all rational ratios,
because their primitive m is a positive integer. This is a worst-case allowance,
not a measured physical noise floor. An upper error bound can be conservative;
it is not evidence that actual errors attain its whole box or are independent.

## 5. A small integer contrast with a narrower physical purpose

The exact ratio k2/k1=19/5 gives v=(19,-5,0). It obeys

    v dot g=0, v dot a=0,
    v dot d=15729/(1045*fX).

Hence it removes the shared nondispersive and uplink phase while retaining
downlink plasma/electronics. More generally, if PhiX=k1*Theta+RX+bX+nX+eX
and PhiKa=k2*Theta+RK+bK+nK+eK, then 19*PhiX-5*PhiKa eliminates ANY common
Theta, including its chirp, without a linearized gravity/plasma decomposition.
Temporal differences remove constant 19*bX-5*bK. For nonzero complex samples, the corresponding complex
sample character is (zX/|zX|)^19 * conjugate(zKa/|zKa|)^5 after physically
justified reference-phase restoration. It is a nuisance diagnostic, not a
gravity-sensitive measurement. The standard real dual-frequency contrast is
already in Asmar et al. 2005; only its exact integer compatibility and the joint
calibration/phase-history question are being investigated here.

The uniform endpoint phase-error amplification is 24; a two-endpoint contrast
has 48. These factors are mathematical, not assigned instrument uncertainties.

## 6. ADC representation route and its limits

The existing PDS SIS says signed truncated samples k require the 2*k+1
correction. Under an additional unsaturated ideal midrise-quantizer premise,
the unknown analog I/Q at the ADC lies in the square of half-width one about
the corrected odd-integer center z. If |z|>sqrt(2), enclosing that square in a
disk gives angular error <=asin(sqrt(2)/|z|)/(2*pi) cycles. Exact rectangle
extrema can be obtained from its four corner arguments in a continuous lift
relative to the center (not naive principal-angle min/max) when the origin is
outside the rectangle. Saturated extreme codes do not establish a bounded
cell; any origin-reaching cell needs special handling. A format correction
alone does not prove the quantizer transfer function or absence of clipping.

This would bound representation of total analog complex voltage only. Thermal
noise, plasma, oscillator and receiver error, carrier extraction, reference
phase convention, and time matching remain separate. It is not a carrier
accuracy bound and cannot supply a scalar residual or energy budget.

## 7. Inner-cell information at finite receiver resolution

Suppose each real ADC component has B signed bits and the corrected complex
center is z=(2*i+1)+i_unit*(2*q+1). Suppose also that an unsaturated code's
entire analog preimage is the square z+[-1,1]^2. These are explicitly supplied
quantizer premises. The documentation supplies the stored representation and
2*k+1 correction; it does not alone establish the complete physical preimage.

The square contains the closed disk of radius1 centered at z. When |z|>1,
the analog phase image therefore contains the interval

    arg(z) +/- asin(1/|z|),

using a continuous lift. The endpoints follow from the tangent lines to that
disk. Its angular width in cycles is at least1/(pi*|z|), since asin(x)>=x.
The B-bit code centers obey |z|<=sqrt(2)*(2^B-1), even including extreme codes
for this upper bound. If a cell includes zero, voltage phase is undefined and
the simple phase observable is already outside its domain.

At any rational relative carrier ratio, the primitive simultaneous-plasma
character has first coefficient N1=L*a with L>=1 and |a|=3007586755. Keeping
the other channels at their centers and varying only the X-channel voltage
inside its admissible disk, the character phase spans an interval of at least

    |N1|/[pi*sqrt(2)*(2^B-1)] cycles.

For B=16 this exceeds1 by a large margin. A completely rational sufficient
certificate uses pi<22/7 and sqrt(2)<3/2:

    |N1|/[pi*sqrt(2)*(2^16-1)]
      > |a|*7/[33*65535] > 1.

Thus the image of that single ideal ADC preimage cell under the primitive
character already covers its entire output circle. No raw code can determine
this pointwise voltage-phase character to a proper arc if that entire cell
remains admissible. Independently admissible cells across endpoints similarly
cover the whole product endpoint quotient and its constant-offset quotient.
This conclusion uses inner admissible disks, not the invalid inference that
a loose outer error box is actually attained.

There are several scope limits. This does not prove physical carrier noise
is large, does not reject coherent carrier fitting, and does not apply after
an independently justified waveform/time correlation restricts the Cartesian
voltage-cell set. Increasing the number of samples while fitting a restricted
coherent signal changes the admissible class. The hypothetical small integer
19/-5 downlink diagnostic is outside the simultaneous-plasma-annihilation
class and has a much smaller ADC-cell image, as the development calculation
illustrates. It still is not a gravity-sensitive signal or a calibrated
carrier measurement.

The implication for this pointwise route is a supplier requirement: a physical
coherent phase estimator or restricted waveform/error model must bridge the
raw finite-resolution receiver samples to the phase quotient before the large
joint-plasma character can be used as a measurement. A preferred phase lift,
rounded frequency ratio, assigned physical noise bound, or the format's
2*k+1 correction is not that bridge.

## 8. Exact coherent-averaging witness

Let two ideal voltage channels have unit amplitudes and the shared phase law
zX(t)=exp(5*i*theta(t)), zKa(t)=exp(19*i*theta(t)). At each sample,
zX(t)^19 * conjugate(zKa(t))^5=1 exactly. This is the ideal19/-5 contrast
with its common phase rescaled; neither noise nor phase slips are needed.

Take two samples theta0=0 and theta1=pi/10. Their complex means are

    mean(zX)=exp(i*pi/4)*cos(pi/4),
    mean(zKa)=exp(i*19*pi/20)*cos(19*pi/20).

Both means are nonzero. The first cosine is positive and the second negative.
After normalizing each mean to unit modulus, the19/-5character is-1, since
the shared mean phase cancels but the second channel's minus sign is raised
to an odd power. Thus the pointwise contrast is identically+1 while the
contrast of the two independently averaged channels is-1: a half-cycle change.

This explicitly tested construction rules out commuting independent voltage
averaging with integer cancellation for arbitrary shared phase histories. It
does not reject a physical carrier estimator supplied with the appropriate
dechirp, waveform regularity, phase-continuity, time alignment or error bound.
Those restrictions could exclude this fixture. No physical noise level or
phase selector has been introduced to do so here.

For the raw-record route, the practical consequence is to specify and justify
the phase estimator and its interaction with channel transfer before using
averaging as a replacement for the observed instantaneous-voltage contrast.

## Receiver development comparison and failed timing discriminator

A protocol was frozen before raw access. Both entire products are now exposed
development, even though sample analysis is restricted to 2002 day169 UTC
seconds 48900 inclusive through 49500 exclusive. The later16:56/16:57 receiver
pair remains unopened. There are zero independent empirical tests or fits.

The two products each contain 8941 records of 4260 bytes, with consecutive one-second
tags 48900 through 57840. All 17882 headers are retained. The selected 600 records
per channel have 16-bit components at 1000 complex samples/second, giving 600000
paired samples. Every selected pair contributes to the code-cell summaries;
there is no quality, amplitude or result-based clipping. Hardware flags,
receiver metadata and unused header fields remain in the ledgers.

The independent decoder uses scalar struct/integer parsing; the author uses
vectorized word extraction. All 1200 per-record corrected-I/Q hashes match.
All 1251740 scalar header values match, including IEEE floats bit-for-bit, and
all 17882 sixteen-byte spare blocks match. Nineteen separately frozen synthetic
controls cover packing and725 exact rational cell points. These are independent
implementations on the same exposed data, not independent physics experiments.

Under the stated ideal-cell premise, the 19/-5character's cell-width median is
0.0005482142770177202cycles and maximum 0.13411429875218084cycles. No selected
code is extreme and no selected cell touches the origin. These facts do not
establish an unsaturated analog history or physical carrier accuracy. The
independent cell calculations differ by at most 2.78e-17cycles. Instantaneous
baseband characters and their lag statistics remain baseband diagnostics;
no sky-phase convention or phase-unwrapping rule was fitted.

The original 2001DSN0159-Science specification, section 2.4, uses phase argument
msec/1000 and frequency argument(msec+0.5)/1000. The day169 label uses the
midpoint in both descriptions. The specification provides first-sample tags,
subsequent sample-period increments and designed pipeline compensation;
there is no claim that sample timing is wholly undocumented. However, neither
reviewed source explicitly fixes the I+jQfrequency sign or all physical LO and
electronics phases.

Root compared the two documented phase arguments on all 17880 adjacent-record
pairs, using exact rational arithmetic on the recorded IEEE doubles. The
retained join residuals are unwrapped, with no fitted offset. A separate
fractional diagnostic is also reported; neither diagnostic selects a phase
convention. At zero shift the largest join discrepancies are
9.701276819193579e-12cycles(X) and2.425319205857186e-12cycles(Ka). At 0.5 ms they
are1.2085462609361324e-11 and1.1486178882641445e-11cycles. Both are tiny.
This attempted discriminator failed: a common small translation of a smooth
polynomial stream can preserve continuity. A smaller join residual does not
calibrate the absolute phase timestamp. The discrepancy remains open.

## Imports, provenance and physical limits

- Ideal880/749, 3344/749 and 14/15 turnaround ratios are instrument premises,
  documented for spacecraft-received inputs. The actual cross-uplink frequency
  relation is not derived from a shared reference or rounded carrier labels.
- Phase in cycles, coherent transfer, matched emission events, common leading
  plasma columns, arbitrary per-endpoint plasma and fixed receiver origins
  define the conditional model. An actual correlated plasma family may retain
  more information and must be analyzed on its own terms.
- Torus characters, integer arithmetic and Fourier approximation are ordinary
  mathematical tools; they do not select a physical state or action.
- The ideal ADC preimage, independently admissible voltage variations and a
  pointwise voltage-phase identification are explicit conditional premises.
  Recorded signed-word representation and2k+1centering do not derive them.
- Actual carrier extraction, NCO implementation, complex sign, analog LO phase,
  timing, ray mapping, physical error/energy budgets, scalar action/potential,
  initial state, scales and environmental solution remain open. They are not
  counted as independent walls or silently replaced with selected values.

Primary sources: [Armstrong,2006article revised2016,section4.6](https://pds-geosciences.wustl.edu/radiosciencedocs/urn-nasa-pds-radiosci_documentation/DOCUMENT/armstrong.2016.pdf),
[Asmar et al.,2005,sections3–4](https://www.issibern.ch/teams/pioneer/public/Asmar_etal_2005.pdf),
[DSN0159-Science,2001-02-28,sections2.4–2.6](https://pds-geosciences.wustl.edu/radiosciencedocs/urn-nasa-pds-radiosci_documentation/DSN_0159-SCIENCE/dsn_0159-science.2001-02-28.pdf),
and the hash-pinned product labels in
[cassini_rsr_development_inputs.json](../scripts/cassini_rsr_development_inputs.json).
The Cassini SIS specifies signed truncation correction in section 1.5.2.1.
Its exact identity and source scope, and the supplemental ground-system sources,
are preserved in the evidence index; no inaccessible original PDF is claimed read.

## No-Go Discipline Gate

The conclusion is conditional channel/measurement mathematics. No impossibility
of radio tracking, coherent estimation, scalar theory or a TOE is proposed.

**N1 — Actual attack routes.** The following materially different formulations
were ATTEMPTED; none is labeled RULED OUT BY PRIOR. Their authorities are the
self-contained proofs and explicit fixtures in this note and the independently
checked working evidence, not an invented retained result. Successful routes
are preserved rather than forced into a blanket negative conclusion.

| Route and terminal obligation | Result and scope |
| --- | --- |
| Real algebraic plasma projection: remove two physical columns | A real null row exists; integrality is a separate condition. A unit coordinate shift gives the explicit failure of treating an arbitrary real row as a unit-period character. |
| Nonlinear continuous torus observable: recover information beyond a linear row | Fourier support lies in the same annihilator; an irrational relative ratio leaves only constant continuous endpoint invariants within the stated unrestricted nuisance class. |
| Multi-epoch count construction: remove receiver origins despite changing ratios | Three rational ratios give a constructive nonzero temporal kernel; two distinct endpoints do not. This positive escape prevents a broad changing-frequency obstruction. |
| Robust approximate calibration: replace exact ratios with close values | The displayed leakage formula and a half-cycle choice of arbitrary plasma amplitude give a counterexample to a uniform closeness guarantee without a plasma bound. |
| Quantized-voltage inverse image: obtain the character from an admissible cell | The inner-disk construction covers its output circle for the large 16-bit pointwise character. Restricted waveform information can shrink that admissible set. |
| Coherent voltage averaging: suppress fluctuations before cancellation | The exact noiseless two-sample construction changes +1 to -1. A justified dechirp/estimator can exclude that history and remains open. |

These six routes differ in primary object or terminal obligation. This is not
an exhaustive search over physical estimators; general statements quantify
only over the explicit groups/cells in their proofs.

**N2 — Condition relations.** Group the open physical suppliers as phase/channel
transfer(P), operational frequency relation(R), estimator/error admissibility(E)
and scalar/environment response(S). For pairs P/R,P/E,P/S,R/E,R/S,E/S, neither
physical implication is established here; both directions remain unresolved.
No pair is declared independent, and no numerical independent-wall count is
claimed. The ADC-cell premise implies its displayed representation interval;
those are one dependency, not two independent conditions. Carrier restriction
can shrink the ADC admissible set, so the full-cell conclusion is not carried
to that different domain.

**N3 — Hidden-condition scan.** Supplied phases, frequencies, plasma variables,
segment origins, nonzero voltages, full ideal cells and independence of their
variation are explicitly stated before use. “By construction” in the fixture
means the given finite voltage values, not physical selection. “Registered”
and “canonical” refer only to input/source bookkeeping. No background,
standard-QFT or framework premise is used to close the measurement bridge.

**N4 — Residual matching.** No earlier campaign is cited as a no-go authority.
The prior coherent-count and phase-history work motivated this question but
its relevant linear/lattice facts are derived here. Armstrong supports ideal
turnaround ratios, not operational cross-uplink commensurability. The RSR label
and 2001specification support their stated model/packing fields, not physical
carrier accuracy. ADC and averaging witnesses address only the explicitly
specified voltage/estimator maps; they are not witnesses against scalar action
or initial-state existence.

**N5 — Resolution.** Endpoint characters and ADCcells are per-element results;
Fourier characters are mathematical modes, not a measured scalar spectrum;
temporal kernels and the fixed 600-second development window are per-block.
No lattice-site or lattice-wide physical claim is tested. The primary cached
runner states each of these resolutions separately.

**N6 — Partial closure and conventions.** Carrying the correct phase period and
using temporal integer weights already retire an arbitrary normalization or
receiver-origin choice within the model. A phase-zero convention is distinct
from fractional resets and hardware timing. Calibration, synthesis records,
restricted plasma and a justified carrier estimator are concrete remaining
routes; this note does not say that a new axiom is required. Previously inspected
approved framework primitives retain their existing roles; no primitive or
relabeling is claimed to supply a receiver error budget.

**N7 — Strongest counter-route.** A real receiver estimates a coherent carrier
from many voltages with a known synthesized reference; it does not necessarily
apply a huge character to independently free sample phases. Derive the actual
joint waveform, dechirp and reference transfer, restrict the voltage preimage
accordingly, and establish a deterministic or calibrated statistical error set.
The documented NCO and simultaneous closed-loop records are concrete starting
suppliers. That route can evade the pointwise full-cell assumptions and is not
closed by the present theorem. It is the next application target, rather than
an in-domain contradiction of the stated cell/group proofs.

**N8 — Cross-cycle echo.** The earlier coherent-channel count note removed
constant initial receiver phases with supplied real rows; the phase-history
note removed arbitrary integer histories for reduced observations. Their
remaining physical phase/error identification was not retired. This block
combines those obligations explicitly and preserves the constructive temporal
route. Current-main searches for joint integer/plasma and chirp conditions are
recorded with source identity; no exhaustive literature novelty claim follows.

## Verification and review record

The primary runner imports all three helpers and reads four pinned public
inputs through an explicit local cache. Its package-integrity reads are its
own source, declared helpers, note, input manifest and the frozen protocol.
External scientific reads are the two raw products and two labels. It fits no
parameters and performs no independent empirical experiment.

From a fresh checkout, fetch the four exact public inputs first:

```bash
python3 scripts/scalar_channel_calibration_check.py --fetch-inputs
python3 scripts/scalar_channel_calibration_check.py
```

The canonical cache is generated only through scripts/runner_cache.py with
the runner's declared timeout. Author arithmetic and data counts, mutation
results, exact source identities and the focused independent reports are in
the branch-local evidence index. Original independent derivations/extractions
are distinguished from later author-source correspondence. Their raw samples
are the same exposed inputs, not a fresh empirical holdout.

The v2 working note explicitly repaired nonzero-complex-sample and coherent
angular-lift qualifications identified in the mathematical check. The decoder
adds exact input hashes, deterministic gzip output and a 1 kSPS lag-domain guard;
its scientific extraction is unchanged. Transport TLS/timeout failures and the
unsuccessful NCO timing discriminator remain preserved.

This note and its runner propose conditional support. Formal audit and combined
current-main landing checks are separate and pending. No audit verdict, merged
science, physical error floor, carrier-phase restoration or scalar discovery is
claimed. The new source is self-contained; earlier unmerged milestones are
historical context, not undeclared load-bearing runner inputs.
