# Independent check of the vector mechanical readout

Reviewed October 12, 2026. This is a focused mathematical/source check of the
parent-authored block. It is not a formal audit or a retained-science verdict.
The author runner was neither imported nor executed. No author file, Git
state, PR, empirical target, worker or model was changed.

The current note is mathematically consistent with its stated linear,
plane-wave, scalar-force and simultaneous mechanical-readout assumptions.
One network-rank wording error was identified and corrected by the author.
The exact original text, corrected text and difference are preserved. I find
no unresolved material mathematical correction in the current source.
Neither this check nor the author controls supplies an optical/metric
prediction or a likelihood for an observed event.

## Source coverage and identity

I read the complete protocol, note, source ledger, runner and numerical
receipt. The snapshot/manifest includes their exact bytes and absolute source
paths. I also checked the original executed four inputs against every hash
in RESULTS v1 and against the author's subsequent source_snapshot copies.

| File | Current SHA256 |
| --- | --- |
| PROTOCOL.md | e7739cca78bc8f71dd72c256fb2987aa12dba5586f98443c5da74f0cca9c56a2 |
| DIRECT_READOUT.md | 6c33aa974f21ff0934a8c825c5b77ba8354b68bc7e27a802d13531fb6b5ca290 |
| SOURCE_LEDGER.md | 14259802a4f032fb600216ab911dfd147baa76d9d2ab6937037977c433f23e30 |
| direct_readout_check.py | 408b67d69a0df25fdcad80c4c4588397f8f7fec942991deecc5ea0711fecc714 |
| evidence_v1/RESULTS.json | 38211e20ff4a0d9cac2602994dbc34955ffbd9fa9f07178639cca01db534e9f6 |

The numerical receipt pins the original note,
392e8d068c9f07c1e3584a8f5f93cc014afcf09a02f67f43eeafa646b19b7f8c.
It does not purport to have executed the corrected prose. The other three
executed inputs and the result are unchanged. The corrected note only adds
the two rank qualifications described below; the formulas and controls
remain identical. This is a transparent source-version transition, not a
relabeling of the old execution.

Prior-context coverage was deliberately narrower: I checked the supplied
matter force and illustrative speed-calibration paragraph and its receipt
in direct_vector_matter_radiation. I did not review that entire radiation
block here. Exact context snapshots/hashes are included in
source_manifest_v1.json, SHA256
64521db2ca1756ee0f0eb1baf779c3b2beafef9a287fa1a7866e4a8826b689b0.

## Independent force-to-tide derivation

Put tau=t-n.x/c, with unit n and constant c>0. From the supplied force,

    a_i = -partial_i f(tau) = n_i f'(tau)/c,
    partial_j a_i = -n_i n_j f''(tau)/c^2.

The sign in the note is correct. This is a rank-at-most-one matrix, including
rank zero when its coefficient vanishes. With P=I-n n^T, both P T P and
its transverse trace-free part vanish. For a harmonic potential, f''=-omega^2
f, so the coefficient becomes +omega^2 phi/c^2; this agrees with the direct
acceleration derivative.

A sum of modes with the same n and possibly different speeds still multiplies
n n^T. A sum with different directions need not: at t=x=y=0,
phi=cos(t-x)+cos(t-y) gives diag(1,1,0), of rank two. Likewise, retaining
spatial derivatives of a nonconstant far-zone amplitude adds terms outside
the exact plane-wave proof. The note states both the common-direction and
leading-far-zone restrictions.

The vector character of u does not alter the spatial direction of the
gradient of the scalar e.u for one plane wave. A transverse u polarization
orthogonal to e is invisible in this linear coupling. When e is parallel to
n, both transverse field polarizations are invisible; when e is perpendicular
to n, the longitudinal scalar projection is invisible. The generic network
discussion presumes the relevant scalar amplitudes are available. This is
not a metric Riemann-tensor or relativistic polarization classification.

The independent numerical route differentiates a nonlinear phase function's
acceleration directly at 80-digit precision, rather than using the author's
symbolic Hessian. Its maximum tensor error was 2.64e-82; P T P was below
5.41e-84. These finite controls support the explicit algebra above.

## Exact endpoint response and initial conditions

For phi=A exp(-i omega t+i omega n.x/c), Newton's equation gives

    delta x = i n phi/(omega c),
    delta x_ddot = -i omega n phi/c = -grad phi.

At fixed unperturbed base x, the first-order simultaneous length variation
is the arm projection of the endpoint displacement difference. With unit
arm a, mu=n.a and z=omega L mu/c,

    delta L/L = i mu phi(x) [exp(i z)-1]/(omega c L)
              = -phi(x) mu^2 exp(i z/2) sinc(z/2)/c^2.

The sign, phase, factor of two and unnormalized sinc convention are all
correct. The formula is continuous at mu=0 and z=0. At nonzero phase nodes
z=2 pi m, the two endpoints receive equal accelerations and their relative
response vanishes, even though the local tide need not vanish.

For zero displacement and velocity at t=0, the correct time factor is

    Q(t)=exp(-i omega t)-1+i omega t.

It satisfies Q(0)=Q'(0)=0 and Q''=-omega^2 exp(-i omega t). Omitting the
constant subtraction violates the initial displacement; omitting the
linear subtraction violates the initial velocity. The linear term is the
homogeneous free motion selected by those initial conditions. It does not
justify extending the first-order displacement approximation to arbitrarily
long times. The later monochromatic network formula refers to the harmonic
component, with the initial-condition transients treated separately.

Units also close: phi has units L^2/T^2, T_ij has 1/T^2,
phi/(omega c) is a displacement and phi/c^2 is dimensionless. This proof
uses coordinate-simultaneous Euclidean endpoint length, not photon phase,
an optical round trip, a clock prescription or calibrated strain.

I solved a 13-state linear initial-value system by scipy.linalg.expm: two
three-component positions, two three-component velocities, and a driving
complex oscillator. The force coefficients were constructed separately at
the two endpoints. This is a different numerical route from the author's
scalar acceleration quadrature. It agrees with the formula for all 36
declared mu/c/omega/L/time invariants, using independent amplitude, base
point and geometry. The maximum relative discrepancy is 2.33e-13, below
the original 2e-10 threshold. I do not claim to replay the author's unstored
random three-vectors. An additional 17 fixtures cover independent rotations,
mu=0, positive/negative unit mu and full phase nodes; their maximum error
scaled by |A|/c^2 is 1.12e-15.

## Angular degeneracy and its finite-arm boundary

For unit arms a,b, D=a a^T-b b^T has trace zero, whether or not the arms
are orthogonal. Consequently

    D:(I-n n^T) = -D:(n n^T) = -F.

This establishes degeneracy of those angular patterns up to an amplitude
and sign convention for this restricted long-wavelength differential
mechanical readout. The underlying longitudinal and breathing tidal
matrices remain different. It does not assert equivalence of complete
metric/optical models.

Writing E(z)=[exp(i z)-1]/(i z), the exact finite-arm pattern is

    H(s)=mu_a^2 E(s mu_a)-mu_b^2 E(s mu_b), s=omega L/c,
    E(z)=1+i z/2-z^2/6+O(z^3).

The leading complex correction to F is generally linear in s. Thus the
author's successive error ratios near two have the expected analytic
origin. For n=(1,2,3)/sqrt(14), a=x and b=y, F=-3/14 exactly. My independent
phase-quotient arithmetic reproduces the four absolute error entries to
8.7e-19 and the finite pattern at s=2.2 to 4.0e-17. The table's small-phase
errors are absolute; its separately labeled finite comparison is relative.

A more decisive independent boundary fixture is
n=(1,-1,0)/sqrt(2), a=x, b=y. Here F=0, but at s=pi sqrt(2),

    H(s)=2 i/pi.

No frequency-independent multiplication of F reproduces this result.
This tests the extension of the constant angular factor, not a comparison
with an unsupplied finite-frequency breathing/optical transfer function.
The protocol's final qualification and the receipt say this explicitly.

## Two-speed network: corrected rank statement

Let X_A=n.x_A and C_As=F_A exp(i omega X_A/c_s)/c_s^2. For two sites A,B,
the squared norm of their two-column minor is

    4 F_A^2 F_B^2/(c_T^4 c_L^4)
      * sin^2[omega (X_B-X_A)(1/c_T-1/c_L)/2].

This is positive for at least one pair exactly when the two columns are
linearly independent. Thus two different speeds generically give rank two
with at least two responsive sites, but special projected-baseline phase
aliases can give rank one at a chosen frequency. Equal speeds give
proportional columns. A fully blind network gives rank zero. Aligning all
sites using c_L left-multiplies C by a diagonal unitary matrix and cannot
change its rank; it generally leaves nonconstant relative c_T phases.

The original note had two imprecise statements: it called a one-speed
response rank one without the blind-network qualification, and listed a
vanishing amplitude as a cause of the full matrix rank falling. Matrix
rank is independent of the amplitudes multiplying its columns. Setting
one amplitude to zero restricts the active signal family to one column;
it does not modify C. I reported this, and the parent corrected both
statements in current lines 88-98. The exact original/corrected snapshots
and network_wording_correction.diff preserve the finding and resolution.

Independent 80-digit Gram eigenvalues, obtained without SVD, are
1.8609186392448590985 and 0.4208868525251534985. They agree with the receipt
within 2.23e-16. The Gram determinant equals the sum of the pair-minor
squares, 0.6134589275668187819. The aligned c_T constant-fit residual is
2.0895103284415327402. I also tested equal speeds, complete blindness,
one responsive site and a distinct-speed phase alias. The synthetic F_A
are realizable with orthogonal unit arms: for n=x, choose arm angle theta
with cos(2 theta)=F_A.

This matrix rank describes the response to two arbitrary incident scalar
amplitudes at fixed direction/frequency. A specified source can correlate
those amplitudes or make a component invisible/absent; therefore rank two
does not establish two freely fitted physical source functions, two
simultaneously observed arrivals, or a model evidence. The note's emission
history/time-window qualification is necessary and correctly retained.
The illustrative c_T/c_L=0.7185375538936453 follows from its earlier
conditional power-comparison polynomial; it is not an observed wave speed.
I independently reproduced that ratio from 6 x^7-21 x^2-20=0 with x=sqrt(q).

## Controls, failures and external-source scope

The author receipt's five families and 36 endpoint integrations match its
complete source. It asserts the endpoint tolerance and wrong-sign test for
each case, tests long-wavelength convergence, finite-arm deviation and
network rank, and identifies its negative controls as false-alternative
comparisons rather than mutated-source executions. No empirical arrays
enter that runner.

The final reviewer calculation has 12 passed checks and zero failed checks.
It also rejects wrong response sign, either omitted zero-initial-condition
term, conjugated endpoint phase, extending constant F to finite arms, and
reusing one-speed alignment/rank for the generic two-speed matrix. These
are independent false-formula fixtures, not executions of modified author
source. The evidence includes all 53 endpoint cases and exact methods.

Reviewer failures are preserved rather than overwritten. The first
reviewer run had 11 passes and one comparison failure: I initially divided
the small-phase angular errors by |F| before comparing them to the author's
absolute errors. Inspecting the complete author expression identified the
reviewer normalization mistake. The v2 script removes that division and
changes only its receipt version/output path; the v1 script, results and
logs remain. REVIEWER_CONTROL_CORRECTION_v1.json records the precise change.
Setup failures (Python TLS trust, a relative sibling path and the resulting
first curl output-directory failure) are also recorded. The official PDF
was subsequently saved successfully with ordinary TLS-verified curl.

I read sections V and VII of the official GW170814 paper. Its pure
polarization comparisons use specified antenna functions while retaining
GR phasing; mixed-polarization models were outside that comparison. This
supports the ledger's contextual description, but does not supply this
candidate's readout or propagation likelihood. No reported preference or
inferred mass was transferred. [Official version of record](https://dcc.ligo.org/public/0145/P170814/015/LIGO-P170814.pdf).

The exact official PDF is preserved with SHA256
6f629844c3ef3bce9357ff858995f6fb3f99b3522c669cda9951031275725a1d.
The current source appropriately leaves photons, clocks, metric coupling,
suspensions, actual waveform/source history, calibration/noise and strain
inference outside the model. The result is a conditional mechanical
readout calculation and a reason that field-component counting or matching
one radiated-power number cannot by itself supply detector polarizations.
It is neither empirical acceptance nor a whole-class gravitational exclusion.

## Preserved evidence

- source_manifest_v1.json and snapshots/: complete current inputs, original
  executed inputs and separately scoped prior context.
- network_wording_correction.diff: the resolved author wording finding.
- check_readout_independent.py and INDEPENDENT_CALCULATIONS_v1.json: original
  independent control and its preserved reviewer comparison failure.
- check_readout_independent_v2.py and INDEPENDENT_CALCULATIONS_v2.json:
  corrected independent control, 12 passed/0 failed, 53 endpoint cases.
- REVIEWER_CONTROL_CORRECTION_v1.json and both run stdout/stderr pairs.
- operational_failures_v1.json and primary_sources/: retrieval history,
  official-source scope and exact official PDF.
- FINAL_REVIEW_RECEIPT_v1.json: final source recheck and hashes of this
  report and all reviewer-owned evidence.

Final independent calculation SHA256:
d52d022e2d9916a77d9a73ed5a05884ec459c71f2f627b4063bab2ceae278700.
Final independent script SHA256:
eb51cc14303875c3b5b9ea018dea518d80def4893dc51f558ab98bcedbb9fdef.
