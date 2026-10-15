# Integer-history elimination for radio phase observations

**Date:** 2026-10-15
**Status:** conditional-support
**Claim type:** bounded_theorem
**Actual current surface status:** conditional-support
**Primary runner:** [scalar_phase_quotient_check.py](../scripts/scalar_phase_quotient_check.py)

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: scalar_phase_quotient
target_blocker_text: "Derive or eliminate the revised scalar theory's remaining history and measured-gravity assumptions"
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Derive applicable fractional-error and reset calibration, then a physical scalar residual"
conditional_surface_status: "Integer ambiguity is eliminated for reduced observations under supplied phase and response maps"
hypothetical_axiom_status: null
admitted_observation_status: "Previously exposed Cassini day169 archive, including its day170 records; development consistency only"
claim_type_reason: "Exact quotient and conditional energy inequalities; no observed scalar signal, fitted state or physical noise budget"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The downstream consumer is scalar reconstruction from radio observations.
This note removes the need to choose a whole-cycle history for a deliberately
reduced observable. It does not reconstruct lost whole-cycle information.
The exact target is to derive the surviving phase quotient, its conditional
energy inequality, and check the reduced archive conversion on every exposed
Doppler record without selecting a forward lift.

## Observation and exact target

The registered day169 archive is already exposed development data. Its ATDF
phase is represented modulo M=2^32 cycles; the prior full-value reconstruction
chose a nonnegative increment below M and no reset. All 183329 matched endpoint
occurrences remain preserved, including 18393 nonzero item87 diagnostics. Those
diagnostics are not yet a certified signed correction or physical error bound.
The encoding is distinct from the received physical phase.

Target: remove arbitrary integer histories from a usable observable, rather
than infer them from a smoothness rule or choose their minimum-energy lift.
Success is an exact quotient observable, its response/energy inequality, and
all-row precursor agreement without calling a forward-lift function. This is
not recovery of the full unwrapped phase. Later raw products remain unopened.

Primary documentation: the registered PDS label and PDS tdf_unpack guide
(corrected high-part scale), Morabito–Asmar1995 for modulo-M count processing.
TRK-2-34 J-1 note31 describes a software slip estimate in that later format;
its mapping to this ATDF field is not silently adopted. Source-level field
semantics are being checked separately.

## 1. Quotients before fitting a history

Let q_j be native endpoint phase numbers in cycles. On a supplied continuous
segment the candidate identification is

    q_j = phi_j + b_s + n_j + e_j  (mod M),   n_j in Z.

Here phi is the relevant received/reference phase under a separately supplied
transfer map; b_s is an arbitrary real constant per segment; n_j is an
arbitrary integer history; e_j is a real error with no default bound. This
model does NOT cover arbitrary real counter resets or fractional transients
unless they are included in e with a separately justified budget.

Let D be the oriented incidence matrix of consecutive endpoints. Then Db=0
within each segment. x=Dq is represented modulo M. Since M is an integer,
adding arbitrary integer histories leaves exactly the one-cycle classes

    [x]_1 in R^n/Z^n, or z_i=exp(2pi i x_i).

There is no bound on n, no preferred lift, and no monotonicity premise. On a
chain every integer edge history is Dn for an integer endpoint history, by
successive summation. Multiple chains retain their own arbitrary offsets.
Unknown real resets between endpoints are outside this identification, not
eliminated by it. A graph with loops can carry additional shared-endpoint
constraints; independent edge integers are the conservative enlargement.

Without the integer-slip premise the exact native quotient is instead R/MZ.
More generally write the established ambiguity as P Z^n, with P=M or P=1.
For v in Z^n, exp(2pi i v^T x/P) is well-defined. Conversely a linear character
exp(2pi i a^T x) descends precisely when P a_j is an integer for every j:
translate one coordinate by P, and require the phase factor to be one.

More explicitly, for J endpoints in S supplied nonempty segments, let B
be the segment incidence matrix and K take each nonanchor endpoint minus
its segment anchor. Then KB=0, ker K=im B and K Z^J=Z^(J-S). If K(q-q')
is integral, subtract that integer difference with zero anchor entries;
the remainder is constant on each segment. This proves the exact quotient
R^J/(Z^J+B R^S) is T^(J-S). Singleton segments contribute no coordinate.
Consecutive differences D are another integer basis on each chain.
Nonzero ordinary real-valued linear contrasts do not descend under arbitrary
integer histories: shifting a single endpoint changes any nonzero weight.
Periodic functions of the quotient, including its circle characters, do.

This is an algebraic consequence of the stated ambiguity group, not a claim
that all physical receiver error is integer-valued. A nonlinear response
still requires a correct phase transfer model.

## 2. Integer contrasts and a limit of real projections

For adjacent one-second counts, v=(1,-2,1) gives endpoint coefficients
gamma=(-1,3,-3,1). These annihilate every quadratic polynomial in equally
spaced endpoint time, by the finite-difference identity. Thus in a supplied
flat reference model whose initial orbit/clock contributions have that form,
their observable sensitivity vanishes, while the quotient remains defined.
This is an exact nuisance cancellation, not selection of a physical history.
Unequal durations require working in cycles and separately checking the
integer nullspace; averaging frequencies before accounting for durations is
not the same operation. A known baseline p is removed as [x-p]_P.

A real linear projection cannot generally be applied to an arbitrary lift
and then treated modulo one. For a=(1/2,1), adding (1,0) changes its phase by
pi. The projection is instead well-defined modulo 1/2; multiplying the row by 2
produces an integer character. In general commensurate coefficients generate
a discrete projected period, calculable from their common denominator and
integer gcd. This rescaling also rescales signal and real error and cannot
be treated as free precision.

For a=(1,sqrt(2)), the projected integer group Z+sqrt(2)Z is dense in R.
Pigeonhole approximation gives nonzero group elements arbitrarily close to
zero; their integer multiples approximate any real number. Therefore the
distance of any real value to that group is zero, and any continuous scalar
observable invariant under that group is constant. A noninteger projection
can destroy all continuous one-dimensional information when the full integer
history is left arbitrary. This is a statement about this projection class,
not a no-go for the original torus data, bounded histories, or all inference.

The curved contrast in the preceding block has beta_i=(1-H(t_i-2L))*gamma_i.
For rational t0,L,spacing and an irrational dimensionless H, coefficients can
generate a dense group. In the prior fixture t0=7/5,L=3/5,spacing1,
beta0=-1+H/5 and beta3=1-16H/5; beta0+beta3=-3H, while
15beta0+(beta0+beta3)=-15. Thus its projected ambiguity contains both 15Z
and 3H Z and is dense if H is irrational. The prior real-valued contrast is
valid for calibrated real counts; it is not automatically a character on
the one-cycle quotient. Finite measurement precision does not derive whether
the physical H is rational. Keep this domain boundary visible.

## 3. Conditional field-energy bound without choosing a lift

Let Hfield be a real Hilbert space with squared norm N, and let A:Hfield->R^n
be a bounded linear observation map. Only the stated finite contrasts need
be bounded; no boundedness of every absolute raw phase is inferred. For a
scalar integer contrast v define
sigma_v=||A* v||. Suppose the supplied physical observation model obeys

    r = A h + e + P k,   k in Z^n,

where r is any representative after subtracting a specified baseline. If
|v^T e|<=eta_v, put g=gcd(|v_1|,...,|v_n|)>0 and

    d = dist(v^T r, g P Z).

For every admissible h, e, k,

    d <= |v^T A h|+eta_v <= sigma_v sqrt(N)+eta_v,
    N >= max(d-eta_v,0)^2/sigma_v^2.                    (1)

If a separately justified physical-energy conversion is E>=q N, q>0,
multiply (1) by q. There is no inferred actual E, upper energy budget, or
selected minimizing initial state. If sigma_v=0 and d>eta_v the supplied
model is inconsistent; if d<=eta_v there is no positive bound from this row.
The zero contrast carries no information. A phase-error box |e_endpoint,j|
<=epsilon_j supplies eta_v=sum_j |(D^T v)_j| epsilon_j; shared endpoints
must be combined before bounding, rather than counted twice as independent.

For a single nonzero functional, absent real error and without any other
observation constraint, the bound is sharp: choose a nearest integer multiple
and a Riesz-representer field achieving that scalar response. Bezout's identity
realizes the multiple as v^T k. This is a proof of a universal lower bound's
sharpness, not a physical state-selection rule. For the whole observation
vector it can be conservative because the other rows constrain the same h.

When G=A A* is positive definite, the exact infimum over all fields and all
integer histories for error-free data is

    Ninf = min_{k in Z^n} (r+P k)^T G^{-1}(r+P k).      (2)

For each real target y, Hilbert projection gives minimum y^T G^{-1}y.
Positive definiteness makes the lattice objective coercive, so the minimum
exists. If the supplied real-error set is the ellipsoid e^T G^{-1}e<=eta^2,
the exact infimum becomes max(sqrt(Ninf)-eta,0)^2, by triangle inequality and
moving along a nearest lattice representative. The actual error set is not
derived by choosing this ellipsoid. Singular G requires an exact range
condition and separate treatment; the SPD statement is not silently extended. In the positive semidefinite
case the compatible residual must lie in range(G); a pseudoinverse alone
would conceal impossible data. For example, G=diag(1,0), r=(1/4,1/10),
P=1 and zero error admit no compatible integer lift, although the unconstrained
pseudoinverse quadratic gives 1/16. This explicit witness is not a claim
that every singular problem is infeasible.

Componentwise nearest-integer rounding need not minimize (2). In the earlier
exact two-count example G=[[3064,-1871],[-1871,3064]]/(1620pi), take
r=(49/100,49/100). Its positive off-diagonal G^{-1} term favors opposite signs;
a lift with one coordinate decreased by1 beats the componentwise choice.
This is an exact mathematical fixture, not an observed Cassini residual.

## 4. Information and empirical limits

For a primitive scalar contrast d<=P/2, so a one-cycle quotient intentionally
loses all integer-cycle information and its direct lower bound saturates.
That loss is the price of eliminating unrestricted integer histories.
The characteristic period is one native cycle, not one fractional Doppler
unit or one normalized radio frequency. Turnaround ratios, resampling and
frequency normalization must be applied with the correct lattice map.

The all-row check below compares dependent archive products in quotient space.
It can remove the bounded-lift premise from their agreement and test code and
format semantics. It cannot validate phi as sky phase, certify receiver noise,
separate plasma or clock effects, supply a trajectory, or test the scalar
theory. Native third endpoint differences are descriptive data summaries,
not scalar residuals. Zero or nonzero item87 is not used as a selection rule.

Remaining suppliers: correct physical phase transfer and baseline, actual
continuous segments/reset behavior, real error bounds, action/background and
field-energy normalization, nonlinear/source corrections, and an actual
same-environment comparison. These are not retired by quotienting.

## 5. What the instrument metadata establishes

The actual product has format 8 and 288-byte tracking records. The
[SFOC-NAV-TRK-2-25 interface](https://pds-geosciences.wustl.edu/radiosciencedocs/urn-nasa-pds-radiosci_documentation/DSN_TRK-2-25/dsn_trk-2-25.1996-07-31.pdf)
defines items 19/24 on PDF page 13, item 87 on page 17, and packing/status
conventions on page 21. Those page images were read, because the scan has no
extractable embedded text. The named field layouts agree with this product's
PDS label and every decoded tracking format identifier.

| Field | Zero-based bit offset / width | Supported interpretation |
| --- | --- | --- |
| Item 19 | 216 / 1 | Doppler good/bad flag; zero is the affirmative good assertion |
| Item 24 | 238 / 1 | Receiver-loop lock flag; zero is the affirmative lock assertion |
| Item 87 | 1466 / 10 | Unsigned total slipped-cycle metadata during the count |

Nonapplicable fields are zero, so non-Doppler zero flags are excluded from the
Doppler status interpretation. Even among DOY 169 Doppler sample IDs 1/2,
5790 records have both flags zero and nonzero item 87. This is a finite
counterexample to equating those flag values with a zero recorded diagnostic.
It does not count actual uncorrected physical slips. The source supplies no
signed correction rule, deterministic bound on unrecorded error, saturation
rule, or proof of continuity throughout a whole count.

The later [TRK-2-34 J-1 interface](https://pds-geosciences.wustl.edu/radiosciencedocs/urn-nasa-pds-radiosci_documentation/DSN_TRK-2-34/dsn_trk-2-34.2008-02-29.pdf)
defines a different signed four-byte field on PDF page 70. Page 121, notes
31/36, describes a noise-sensitive slip estimate and a total-phase origin
that changes after events breaking lock. These facts concern that format.
No conversion from that signed field to this ATDF item 87 is asserted.
Consequently, the error budget in (1) remains a supplied physical obligation.

## 6. Complete exposed archive comparison

The four original PDS input identities are fixed in
`scripts/cassini_doppler_development_inputs.json`; the detailed reuse protocol
is `calibration_error/DEVELOPMENT_PROTOCOL_v1.json` in the campaign pack.
This is an after-exposure development protocol, not a preregistered holdout.
The file named day169 also contains day170 records; all are retained.
Only these four measurement files/labels were opened. Later raw radio,
atmosphere and other-day products remain outside this computation.

The [PDS unpacking guide](https://pds-geosciences.wustl.edu/radiosciencedocs/urn-nasa-pds-radiosci_documentation/DSN_TRK-2-25/tdf_unpack.pdf)
supplies the corrected native phase encoding

    N = (item30*10^14 + item31*10^7 + item32)/10^6 cycles.

The [receiver processing description](https://tda.jpl.nasa.gov/progress_report/42-120/120B.pdf)
provides the modulo-2^32 processing and 1 MHz reference-bias context.
The already declared archive conversion is Q=T(D+10^6) cycles for coherent
ODF counts; for one-way counts it is
Q=T[D+10^6+(880/221)F_ATDF-(11/3)F_ODF]. This convention is reconstructed
as a stored-product relation, without deriving the physical receiver phase.
The program directly compares N_end-N_start with Q modulo M and modulo one.
It never calls a forward-lift routine and needs no sign or increment bound.

| Exact finite-data quantity | Result |
| --- | --- |
| Tracking records decoded | 160870 |
| ODF orbit records examined | 91863; 199 type-37 rows are outside the Doppler comparison |
| Doppler intervals accounted | 91664; none clipped by quality, slip flag or residual |
| Matched endpoint occurrences / unique raw records | 183329 / 91701 |
| Nonzero item-87 occurrences / unique raw records | 18393 / 9207 |
| Intervals with nonzero item 87 and all matched flags 19/24 zero | 13015 |
| Negative signed native counter differences | 21; no lift selected |
| Maximum format discrepancy, both quotients | 100849/132600000000 cycles |
| Static strata / adjacent chains | 8 / 36 |
| Equal-duration consecutive triples | 91593 |
| Maximum triple format discrepancy modulo one | 893/500000000 cycles |

The maximum interval discrepancy is approximately 7.60550527903469e-7 cycles;
the triple discrepancy is 1.786e-6 cycles. These describe dependent stored
products, not physical instrument accuracy. All nominal durations are one
second, but the computation performs the explicit conversion to cycles.
One chain has a single interval; that explains why subtracting twice the
chain count from the interval count misses one triple.

One matched endpoint has two raw record alternatives with equal counter and
reference states. Both metadata variants stay in the interval ledger. The
author emits one numeric comparison per interval/triple; the independent raw
implementation also expands all Cartesian alternatives, obtaining 91665
interval-pair and 91594 triple comparisons with the same values. These are
different accounting units, not missing observations. No numerical ambiguity
is silently resolved by selecting a preferred quality flag.

For triples the integer count row (1,-2,1) equals the phase endpoint row
(-1,3,-3,1). This produces a useful observable invariant under the declared
integer histories. The resulting native third differences still contain
orbit, clock, medium and electronics contributions. No physical scalar
residual, gravitational parameter, energy or noise level is fitted here.

## 7. Proof obligations, imports and review record

The proof chain is explicit: the segment/integer equivalence establishes the
torus quotient; the character test establishes admissible scalar reductions;
finite differences remove the stated polynomial columns; Riesz and the
projected error bound yield (1); surjectivity for an SPD Gram and coercivity
yield (2). Each mathematical step is proved above. The density statement is
restricted to an unrestricted integer history and continuous scalar reduction.
It excludes no constrained history, full-vector inference or alternative
measurement law. The matrix example is a supplied exact SPD fixture; its use
here does not require an empirical Cassini Gram or revalidate the earlier
physical action.

The inherited flat/curved response formulas are conditional context. The exact
curved coefficient combination used here is displayed and checked directly.
No new scalar dynamics, action, potential, scale, continuous segment map,
fractional-error distribution or absolute energy normalization is derived.
Approved units, kinetic isotropy and pointwise realized-state primitives are
not classified as missing imports; the present obligations concern actual
measurement/state content beyond their declared roles.

The strongest missing physical lemma is an applicable phase-transfer and
reset/error calibration with a quantitative real-error set, tied to the
same observing environment. It is stronger than archive-format agreement
and is not assumed to have been supplied by the quotient theorem.

The original author working run has 31 exact mathematical controls. Canonical
controls additionally reject floating/symbolic-irrational period inputs and
exercise nonzero error and zero response, for 38 mathematical controls.
The primary runner adds 11 all-row development checks. The independent
mathematical derivation froze 114 controls before author-source exposure.
It independently found false-bound witnesses for an untransformed scaled
lattice, correlated componentwise wrapping, and a pseudoinverse without a
range condition. The independent data implementation uses bit strings and
exact fractions, importing no author decoder; all finite counts and extrema
above agree. A separate source/page/metadata check reads only the declared
metadata. These independent implementations share already-exposed inputs;
they are not independent empirical experiments.

The author working helper accepted float approximations through Fraction.
Review identified that this could invent a discrete period for an irrational
weight. Canonical projected_period now rejects such values instead of
inferring exact arithmetic from finite precision. Original source and review
are preserved. The main theorem did not assume finite precision proves
rationality.

Review also identified a zero-error default in the mathematical helper.
The canonical scalar bound requires an explicit error argument; the
error-free sharpness fixture passes zero as its declared synthetic premise.
No physical application inherits a default zero-error budget.

Canonical source review, source-bound execution and mutation results are
recorded in the campaign review history and cache. No author check sets an
audit verdict. This is a stacked source milestone; complete integrated-base
validation and later independent audit are separate landing obligations.
All actual source inputs must be carried in that integrated reviewed tree.
The current physics-loop status contract permits conditional-support; the
older conformance spec's mandatory proposed_retained prose is not used to
overstate an import-bearing support result.

To reproduce from the four pinned files in the local input cache:

```sh
python3 scripts/scalar_phase_quotient_check.py --input-cache outputs/cassini_doppler_inputs
```

The input manifest includes public retrieval URLs and exact byte counts and
hashes. Absent files must be retrieved at those identities first; mismatched
bytes fail. Outputs contain the full deterministic interval/triple ledgers.
The primary cache binds the complete declared local source closure.

## No-Go Discipline Gate

This is a positive conditional quotient construction with narrow failure
witnesses. No general impossibility of scalar reconstruction is claimed.

**N1 — Actual alternative mechanisms.** All entries below are ATTEMPTED;
none invokes an earlier result as a retained negative authority.

| Approach | What it tests | Actual disposition and evidence |
| --- | --- | --- |
| Receiver metadata calibration | Use quality/lock/slip words to supply a physical error bound | The actual unsigned layout and good/locked nonzero-diagnostic records defeat that shortcut; section 5 leaves detector/correction calibration open |
| Native group reduction | Remove arbitrary history through integer-invariant phase characters | Succeeds on the declared model, sections 1–2; loses whole-cycle information |
| Real nuisance projection | Apply curved real coefficients directly to period-one data | The displayed irrational-H image is dense; the restriction concerns this scalar projection only, section 2 |
| Finite Hilbert geometry | Bound energy without a preferred history | The scalar bound and full SPD lattice minimum succeed under supplied response/error premises, section 3 |
| Coordinatewise history rounding | Replace the correlated lattice search by nearest wraps | The exact two-count SPD fixture gives a smaller compatible joint lift, section 3 and the runner's exact fractions |
| Singular response reduction | Use a pseudoinverse without compatibility | The displayed rank-one example has no compatible lift, although its unchecked quadratic is finite; section 3 |

These routes differ in documentary identification, group invariant,
real-nuisance arithmetic, energy geometry, integer optimization and response
range. Their count is not evidence that all inference routes are exhausted.

**N2 — Relations among conditions.** Measurement transfer/reset/error content
is one grouped empirical obligation; action/environment/energy conversion is
one grouped physical-model obligation. In both directions the implication
between those two groups is unresolved here, so no independent-wall count is
claimed. Boundedness/SPD and the integer ambiguity group are theorem
hypotheses, not extra empirical walls. A future supplier may constrain both
groups at once; this packet does not claim pairwise physical independence.

**N3 — Hidden premises.** Supplied segment, known baseline, bounded linear
response, SPD, positive conversion and quantitative error are explicit in
sections 1–4. “Registered” and “canonical” label source identities and
implementation versions only. The curved background is explicitly supplied
context. No smoothness choice, default zero error, minimum-energy history,
native-to-sky phase identification or physical rationality of H is imported.

**N4 — Witness matching.** Section 5's primary table/packing pages attack only
the signed-correction and flag shortcut; they do not attack scalar dynamics.
Section 2's coefficient identities attack only the one-dimensional projected
integer ambiguity. Section 3's two exact fixtures attack only the specified
rounding and unchecked-pseudoinverse shortcuts. No prior campaign no-go is a
load-bearing witness. Earlier response notes are provenance for examples,
not proofs that the physical calibration obligation cannot be closed.

**N5 — Resolution.** Per endpoint, integer translations and fractional-reset
witnesses are exact. Per segment/count block, quotient reconstruction and all
declared data comparisons are tested. Per finite response mode, the exact
Gram and scalar fixtures are tested. No lattice-site measurement or
lattice-wide emergence theorem is executed or inferred. The primary stdout
records those resolutions separately. There is no extension from a finite
metadata fact to a universal receiver or gravity statement.

**N6 — Partial closure.** Changing the observable to a quotient retires the
need for a selected integer history for that observable alone. Carrying the
correct scaled lattice repairs rational-coordinate shortcuts. These are
mathematical reframings, not new physical axioms. The primitive registry was
checked; its approved units/isotropy/state-evaluation content is left intact.
No primitive is claimed to supply a numerical error, actual state or transfer.

**N7 — Strongest counter-route.** A reviewer should insist on retaining the
full vector lattice, or a physically justified restricted slip/reset family,
before discarding information through a real projection. Actual engineering
calibration and another observing channel could bound fractional errors and
recover useful information beyond this conservative quotient. The terminal
obligation is the applicable same-instrument transfer/reset/error map, not
another chosen state. Sections 1 and 3 already preserve the mathematical
full-vector route; the engineering route remains open.

**N8 — Earlier work.** The earlier count-conversion note preserved its bounded
forward-lift premise; this note removes that premise only from reduced
agreement. The earlier count-energy and mass/curvature notes supplied real
counts and response/error hypotheses. Their real projections remain valid
in those stated domains, while section 2 prevents transplanting them
unchanged onto arbitrary one-cycle histories. Initial-phase cancellation
in the plasma/count work is a related real-nuisance removal; this note checks
the additional integer-lattice compatibility it did not establish. None is
reported as a retired physical-error calibration or global no-go.
