# Repo search

Written by Codex, assigned gpt-6-astra, xhigh; the runtime model identifier
is not independently exposed. FINISH row 1111. Source checkout:
`2b67c749cc219d0051de7b26c2a62c77c3948266`. Research text, not an audit;
no status is granted. Marks used here: GUIDE, OPEN, FAILS. No mass gap claimed.

The lane-specific prior digest is absent at this commit. The lead's older
`prior/repo-search-2026-11-08.md` concerns earlier UV and reconstruction
targets, not the long-sheet experiments. Its snapshot hits are not independent
results. Current task-specific sources are row 1108 (direction), row 1101
(`gap-descent-mc-astra.md`, short-sheet Monte Carlo), and
`gap-bridge-vectors-max.md` (definitions). The checked PR 10114 hit is a
one-step witness; the main hit is an SU(3) simulation protocol. Neither
contains this long-sheet measurement; their exact ranges are below.
Rows 1109 and 1110 own the GH2 and P4 proof attempts;
this lane owns only their requested serial numerical guide.

## Work plan and checkpoint

1. Read the indexed source ranges and prior sampler; fix observables and controls.
2. Pre-register, implement and run GH2_2 with long sheets and two sizes.
3. After its process exits, pre-register and run P4.
4. After its process exits, pre-register and run the reduced face and O(4) control.
5. Record binning, autocorrelation, fit-window and finite-size failures honestly.
6. Save small records and a manifest; finish with one RESULT line.

Scratch/download directory: `/tmp/sa-gap-long-sheet-guide-astra.ioPBXO`.
Both requested Sussman–Alpoge source files were fetched there once, at
`31a47c543775`. Credit Ethan Sussman and Levent Alpoge, with Claude and
Codex as authors of their text. No statement is discharged by these runs.

Final checkpoint: all 60 production chains, the three controllers,
matrix verification and analysis have finished; no numeric worker remains.
Records are packaged and the numeric lock is released. The pinned checkout
and main revisions above remain the source revisions. GH2 rate comparison,
order-one P4 x_p rates and the face endpoint category remain OPEN. Failed
routes are low finite-coupling signal, non-isolated window rates and short
bins for the face endpoint. The next scientific decision, outside this
completed batch, is whether to fund longer endpoint sampling with larger
predeclared bins and a separately controlled neutral-sector extraction.

## Source checks completed

The November 8 digest and row 1101's search were reused as maps. The nearest
actual external-lane source opened was PR 10114,
`MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149`: a positive one-step plaquette
witness, not a long-distance decay estimate. Main at `8b11ae2bb95e` has
`EXACT_TIER_PATH_INTEGRAL_BOUNDED_NOTE_2026-05-07_exact.md:150–184`:
SU(2) subgroup heat bath, anisotropy and jackknife in an SU(3) protocol.
This is algorithmic prior work, not this measurement. No matching ownership
was found by the registry searches; unrelated P4 operator-calculus rows
are not the four-sheet P4 model.

Read row 1108 D5–D6 and section 6.4, row 1101 in full, and row 1076
(`gap-bridge-vectors-max.md`) 220–240 and 350–385. Row 1108 D5 is conditional:
if transverse coupling shortens the face length, a short sheet could resolve
it (its qualification at line 289). The long-sheet experiment decides that
numerical alternative; the direction note is not evidence for either answer.

The outline README, chunk-01 62–73 and obligations 18–29 were read after
searches for GH2, P4-MIX, sigma/principal-chiral, Borisenko/Skala and mass gap.
Outline 588–599 separates polynomial decay from a gap. CA-I 2697–2713
explicitly excludes a mass-gap assertion. The 4.12–4.19 README and indexed
search supply no matching GH2/P4 long-sheet measurement. These are bounded
searches, not an absence theorem. No UV gap is imported as an IR estimate.

## Measurement definitions and pilot registration

GH2 uses the density and left gauge action of Lemma CB-L. The infinity
endpoint fixes both longitudinal gauge links to 1 on a periodic sheet,
selecting trivial holonomy. P4 uses the ordered product
Phi1 Phi2 Phi3^(-1) Phi4^(-1). The face uses periodic transverse squares
with the same oriented plaquette product and identity in-plane links.
All actions are exp(+beta times half trace), in lattice units.

The fixed neutral basis comprises E_r, r=1,4,8,16: the average half trace
of a field at u joined to its field at u+r e by a longitudinal transporter
(the identity in P4/face). Here e is perpendicular to the separation axis.
These operators are invariant under every far-end rigid group. Channel 5
is the GH2 gauge plaquette, or x_p in P4/face. Slice averages and both
longitudinal axes are saved separately. E8 is the primary GH2 channel;
x_p is the primary P4 channel. The other channels can expose overlap failure,
but selecting a noisy minimum cannot refute monotonicity. Spin chi0/chi1
are calibration diagnostics only at the independent-sheet endpoint.

The new geometry reuses the exact quaternion and radial sampler from
`runs/gap-descent-mc-astra/su2_guarded.cpp`. Credit Creutz and Kennedy–Pendleton.
A cycle is one heat-bath and four over-relaxation sweeps. Initial controls
compare local conditional action changes with the full action and verify
full-sweep over-relaxation and unit norms. Maximum discrepancies were
7.82e-14, 2.20e-13 and 6.66e-16 respectively (GUIDE implementation checks).
The action comparison uses separate local and global loops but shares
quaternion multiplication; it is not an independent scientific check.

Before timing: pilot records are excluded from scientific fits. The pilot
passes only resource/implementation gates: correct record length, finite
bounded fields, no RSS violation, normal exit. No sign or rate decision
will be taken from it. Production counts and statistical gates will be
registered after timing, before production records are examined.

Resource preflight: 83% memory free, 41 GB disk free, lock free. The machine
numeric lock acquired at 2026-11-17 12:38:26Z, holder
`gap-long-sheet-guide-astra-2b67c749c`. Controls exited with code 0 before
any timing run. Each subsequent sampler is started only after wait() has
reaped the previous process; analysis runs only after an entire batch exits.

## (a) GH2 pre-registration — before production

Grid: beta_M=2.3,2.4,2.5; L=128,192; beta_L/beta_M=1,4,infinity.
This is a three-point scan, not coverage of all beta_L. At every point:
independent hot/cold starts, 1024 discarded cycles, 2048 saved cycles,
stride 1. Seeds and counts are fixed in `gh_plan.json` before launch.
No pilot records are pooled. Timing pilots both exited 0; the larger
128^2 x 6^2 face used about 40 MB RSS. Both ran at nice 20. Setting nice
10 was denied (PermissionError); all production remains at the inherited
lower priority, explicitly departing from exact nice 10.

Predeclared analysis for every phase: connected subtraction within each
jackknife replica; 64-cycle bins and a 128-cycle comparison, at least 16
pooled bins. Autocorrelation uses the initial positive-pair sequence with
window 6 tau, on the mean and connected-product probes at t=2,8,16.
A fit needs bin >= 8 tau and ESS >=100. Use a correlated periodic cosh,
C(t)=A(exp(-m t)+exp(-m(L-t))), with windows [2,6], [4,8], [6,12],
[8,16], [12,20], [16,24], [20,32], [24,40], [32,48]. Only windows below
L/2 are eligible. Every included correlation must exceed 3 errors;
p>0.05; relative mass error <50%; no boundary mass; stability within two
combined errors on removing the first point; doubled-bin errors within
[2/3,3/2] of the primary error, with the doubled-bin fit still resolved.
Covariance rank must cover every fitted point. Hot/cold mean and t=2
correlation must agree within 4 errors, and within-chain early/late means
must agree within 4 errors. Choose the latest accepted start, then the
longest fixed window. No accepted window means OPEN, not zero rate.

GUIDE reading: a resolved finite-minus-infinity candidate that is not
negative by three combined errors at both sizes leaves the monotone form
unrefuted, never proved. FAILS reading: the same predeclared E8 channel
falls below infinity by more than three errors at both sizes, with valid
calibration and axis/window agreement. Such a discovery triggers new seeds
at those points with the discovered windows frozen, before a GUIDE
refutation is reported. A minimum selected among secondary channels cannot
trigger the claim without this held-out confirmation. Unresolved tails,
failed calibration or thermal/fit gates leave the comparison OPEN.
The fitted channel rate is not identified with the lowest rate over all
neutral observables. The infinity endpoint also retains its trivial-holonomy
restriction. These qualifications limit even a confirmed numerical dip.

The [Borisenko–Skala comparator](https://arxiv.org/abs/hep-lat/9812020)
was also opened directly, not merely copied from row 1101: PDF pages
16–17, equations (48)–(50)
and Tables 1–2. The table page was rendered and inspected. At L=128 the
second-moment lengths are 18.95(13), 25.39(13), 33.14(12), at their 2 beta
= our beta_M = 2.3, 2.4, 2.5. Formula (50) is
xi_2nd = sqrt(chi0/chi1 - 1)/(2 sin(pi/L)). These are finite-volume spin
lengths, not exponential singlet lengths. Their L=256 entries differ;
we will not pretend the L=128 table is an exact L=192 benchmark.
The new PDF is only in `/tmp/sa-gap-long-skala.YIk2wV`; no paper enters
the checkout. `pdftotext` was unavailable; PyMuPDF supplied extraction and
rendering instead.

## (b) P4 pre-registration — before production or GH2 fit inspection

Use beta_M=2.4, L=128 and kappa=0.024,0.24,1.2,2.4. This midpoint scan
is the chosen scope for (b), not a scan of the whole beta_M window.
Two starts per coupling, 1024 burn cycles, 2048 records, stride 1;
`p4_plan.json` fixes seeds and counts. Use the same statistical gates and
windows as (a), with x_p as primary and E_r as secondary observables.
The pooled fit must also agree with resolved fits on the separate axes;
an axis without adequate signal is recorded as unresolved.

GUIDE reading: resolved positive x_p candidate rates and measured
correlations versus kappa describe this finite-volume scan only.
FAILS reading: a failed normalization, stationarity, bin or fit gate
invalidates that extraction; late signal with no accepted exponential
window is OPEN. A slowly decaying finite-torus sample is not by itself a
counterexample to P4-MIX. The theorem, all-box uniformity, the beta_M
endpoints and other neutral sectors stay OPEN whatever the fits show.

## (c) Reduced-face pre-registration — before production or prior fits

Use beta=2.4, L_long=128 in both longitudinal directions, transverse
periods T=4,6, and beta_T=0,0.24,1.2,2.4. Since 128>4*25.39, this meets
the four-anchor-length condition. No infinite transverse-volume limit is
claimed. Two starts at every point, 512 burn cycles, 1024 records, stride
1, fixed in `face_plan.json`. The reduced model selects trivial longitudinal
holonomy. Other beta values and a second longitudinal size are outside
this midpoint measurement, not silently extrapolated.

The beta_T=0 control must reproduce the Borisenko–Skala L=128 spin length
within three combined errors, with stable bin errors and hot/cold agreement.
Failure blocks quantitative face conclusions. Compare the same E8 singlet
candidate at beta_T=0 and beta_T=beta; report x_p and other E_r separately.
Use the same fit, bin, autocorrelation and stationarity gates as (a).

GUIDE anchor-like reading: both T values give a resolved E8 face candidate
within a factor two of its measured anchor candidate, with its three-error
upper endpoint below 0.25. GUIDE short-length reading: both give a resolved
E8 candidate in [0.35,0.65], with a three-error lower endpoint above 0.30
and a three-error separation from their anchors. The transverse-size rates
must agree within two combined errors for either reading. A disagreement,
an intermediate rate or unresolved long tail is OPEN. An x_p-only fast fit
cannot establish a fast common neutral rate while E8 is unresolved or slow.
FAILS marks a failed control or extraction, not a proof that FACE-SG fails.
All numerical conclusions remain candidate-channel and finite-volume ones.

## (a) Result — GUIDE data; neutral-rate comparison OPEN

All 36 chains and the controller exited 0. Nine saved configurations were
recomputed by a separate 2x2 complex-matrix path: maximum slice-readout
difference 2.98e-8, within float32 storage precision. The analysis process
then exited 0. No sampling overlapped verification or analysis.

The L=128 spin controls give xi_2nd=19.291(426), 24.939(604), 33.894(513)
at beta_M=2.3,2.4,2.5. Their discrepancies from Borisenko–Skala are
+0.76, -0.73, +1.43 combined errors. These controls pass the registered
sampling gates. At L=192, beta_M=2.5, the largest spin autocorrelation is
9.46 cycles, so the fixed 64-cycle bin fails the 8 tau rule; that control
is OPEN. It is not compared with the wrong-size published number.

**No pooled finite-beta_L neutral channel passes the registered fit gates.**
This is not a measured zero rate, and it is not evidence of monotonicity.
For example, beta_M=beta_L=2.3, L=128, E1 has C(2)=4.26e-6 +/-5.29e-7,
but C(3)=-0.084e-6 +/-0.403e-6. E8 has C(2)=2.25e-6 +/-2.01e-6.
The primary comparison therefore has no resolved finite-minus-infinity
rate differences. There is no eligible discovery to confirm.

The frozen endpoint itself demonstrates the danger of interpreting a
passing window as the common neutral gap:

| beta_M | L | E8 candidate | window |
|---|---:|---:|---|
| 2.3 | 128 | 0.1360 +/-0.0194 | 12–20 |
| 2.3 | 192 | 0.2526 +/-0.0144 | 8–16 |
| 2.4 | 128 | 0.2264 +/-0.0135 | 8–16 |
| 2.4 | 192 | 0.2286 +/-0.0122 | 8–16 |
| 2.5 | 128 | 0.2187 +/-0.0144 | 8–16 |
| 2.5 | 192 | 0.1590 +/-0.0161 | 12–20 |

At beta_M=2.3 the two selected E8 estimates differ by about 4.8 combined
errors. E16 generally gives smaller candidates (for example 0.1523 at
beta_M=2.4, L=128). Different selected windows and overlaps remain an
uncontrolled systematic. **FAILS:** the interpretation of these window
fits as an isolated common neutral gap. This does not refute the sampling
measure or GH2-DESC. The spin length is not a remedy for singlet isolation.
All per-axis fits, rejected windows, correlations, errors and effective
masses are retained in the hashed scratch analysis files named by
`gh_summary.json`. All neutral-probe autocorrelation diagnostics are retained; the separate
spin-control exception above is not suppressed.

## Face design revision after (a), before any face production

The first neutral basis did not reliably isolate the slow endpoint rate.
For (c) only, retain E1 and E8 and replace E4,E16 with E32,E64. Use E64 as
the primary slow-sector probe, with E8 and x_p reported separately. These
are extended, rigid-group-invariant observables with transverse-to-separation
longitudinal spans 32 and 64; they are not point plaquettes. Their purpose
is better slow-mode overlap, which is not presumed to succeed. The same
basis will measure both beta_T=0 and beta_T=beta. Counts, couplings,
statistical gates and category thresholds remain as registered above, with
E64 substituted for E8 in the category decision. Source is
`face_sheets.cpp`, a recorded readout-only change to `sheets.cpp`.
This adaptation uses the completed GH2 data and is not a blind design;
no face production data existed when it was made. P4 remains unchanged.

## (b) Result — GUIDE correlations; order-one x_p rate OPEN

All eight P4 chains, the controller, matrix verification and analysis
exited 0 before face sampling. Four matrix-readout checks have maximum
error 2.98e-8. The following are the measured slice covariances with one-standard-error
uncertainties. A pooled fit is listed even when the additional axis gate fails.

| kappa | C_xp(4) | C_xp(8) | pooled candidate / window |
|---:|---:|---:|---|
| 0.024 | 3.4716e-4 +/-4.36e-6 | 1.0585e-4 +/-4.51e-6 | 0.2613 +/-0.0239, 8–16 |
| 0.24 | 4.6767e-5 +/-2.58e-6 | 8.3898e-6 +/-2.19e-6 | 0.5298 +/-0.0761, 4–8; axis gate FAILS |
| 1.2 | 1.5570e-6 +/-1.06e-6 | 1.2166e-6 +/-1.07e-6 | OPEN |
| 2.4 | -3.9982e-7 +/-6.15e-7 | -5.9573e-8 +/-5.65e-7 | OPEN |

The x_p signal shrinks sharply at order-one kappa. At kappa=2.4 even
C_xp(2)=1.634e-6 +/-0.647e-6 is below the registered three-error threshold.
Thus no x_p tail rate is resolved at the proof row's main endpoint. This
is not evidence of a vanishing rate or of a uniform positive rate.
The primary x_p autocorrelation times are 0.55–1.24 saved cycles. Other
singlet probes can retain slower signals: at kappa=0.24, E16 has a pooled
candidate 0.0791 +/-0.0119 on 20–32, while x_p's early candidate is 0.5298.
They cannot both be called the common neutral gap. P4-MIX remains OPEN.
The separate-axis readings and every rejected window are retained in
`p4_summary.json` and its hashed detail files.

At kappa=0.024 the separate x_p axes give 0.2688(173) on 6–12 and
0.2249(256) on 8–16, compatible with the pooled candidate. At kappa=0.24,
axis 0 instead gives 0.7861(272) on 2–6, about 3.17 combined errors from
the pooled value; axis 1 has no accepted window. **FAILS:** the registered
axis-consistency gate for the kappa=0.24 pooled candidate. Its rate reading
is OPEN. This disagreement is retained, not averaged away.

## (c) Result — GUIDE controls and correlations; endpoint category OPEN

All 16 face chains exited 0 and were reaped. Eight saved configurations
passed the independent complex-matrix readout check, maximum difference
2.98e-8. The final analysis receipt was written at 2026-11-17 14:33:57Z;
the analysis process has exited. The geometry is 128^2 x T^2 throughout.

At beta_T=0 the spin controls are xi_2nd=25.0078 +/-0.1303 for T=4 and
25.2568 +/-0.1050 for T=6. Against the published 25.39 +/-0.13 these are
-2.08 and -0.80 combined errors. Both pass the registered calibration,
bin-error, hot/cold and within-chain stationarity gates. Their largest
spin autocorrelation times are 4.47 and 6.26 cycles. The doubled-bin
errors are 0.1422 and 0.1409, respectively. This calibrates the independent
O(4) spin sheets; it does not identify the lowest neutral exponential rate.

| T | beta_T | pooled E64 candidate / window | final reading after separate-axis checks |
|---:|---:|---|---|
| 4 | 0 | OPEN | chi-square/bin stability prevents a pooled anchor fit |
| 4 | 0.24 | 0.10268 +/-0.00482, 16–24 | GUIDE candidate; both axes compatible |
| 4 | 1.2 | 0.10210 +/-0.00373, 12–20 | OPEN: axis 0 fails the bin-length gate |
| 4 | 2.4 | OPEN | bin-length and effective-sample gates FAILS |
| 6 | 0 | 0.10475 +/-0.00442, 12–20 | GUIDE candidate; both axes compatible |
| 6 | 0.24 | 0.09672 +/-0.00334, 12–20 | OPEN: axis 1 fails the bin-length gate |
| 6 | 1.2 | OPEN | pooled bin-length gate FAILS |
| 6 | 2.4 | OPEN | bin-length and effective-sample gates FAILS |

For the T=4, beta_T=0.24 candidate, axis rates are 0.11337 +/-0.00826
on 16–24 and 0.09734 +/-0.01158 on 20–32. For the T=6 anchor they are
0.10475 +/-0.00731 on 16–24 and 0.10725 +/-0.00654 on 12–20. These
are compatible window fits, not demonstrations of asymptotic isolation.
At T=4, beta_T=1.2 the largest axis-0 E64 tau is 8.24 cycles; at T=6,
beta_T=0.24 axis 1 reaches 8.85. Pooling can hide this gate failure, so
the otherwise passing pooled candidates are not promoted.

At beta_T=beta=2.4 the pooled E64 autocorrelation times are 30.85,28.02
cycles for the two T=4 starts and 25.13,27.67 for T=6. The 64-cycle bin
is much shorter than 8 tau; the corresponding pooled ESS estimates are
about 33 and 37, below 100. Individual axes reach tau=41.57. **FAILS:**
the registered sampling gates for the endpoint rate extraction. Hot/cold
agreement alone does not repair autocorrelation. A post-hoc rebinning or
an early unqualified fit is not substituted for the registered analysis.

The following endpoint E64 covariances retain the observed slow-looking
signal, with their nominal 64-bin jackknife errors shown explicitly as
**under-controlled at this endpoint**. They are diagnostic records, not
valid significance levels or a refutation of a 0.5 asymptotic rate.

| T | C_E64(8) | C_E64(16) | C_E64(24) |
|---:|---:|---:|---:|
| 4 | 2.1241e-4 +/-1.3024e-5 | 1.0387e-4 +/-1.2402e-5 | 5.5664e-5 +/-1.1758e-5 |
| 6 | 8.6934e-5 +/-4.1280e-6 | 3.9331e-5 +/-3.8533e-6 | 1.8951e-5 +/-4.1331e-6 |

The endpoint x_p channel is also unresolved, for a different reason:
C_xp(2)=1.2681e-7 +/-5.7771e-8 (T=4) and
6.5704e-8 +/-2.2391e-8 (T=6), both below three errors; subsequent windows
fail the signal threshold. There is no passing 0.5 face rate here.
There is also no passing endpoint E64 rate to compare with the anchor.
Neither registered category, anchor-like nor short-length, is selected.
The T=4 anchor's own E64 pooled fit is OPEN, an additional obstacle to
the prescribed two-size category decision. Row 1101's 0.5 candidates
therefore receive no validation or numerical refutation from this batch.

The useful GUIDE outcome is methodological and specific: increasing the
sheet size and operator span exposes a slow neutral signal and slow Markov
mixing, while local x_p loses measurable tail amplitude. This is a reason
to separate those observables in any later design. It is not a conclusion
about the face's lowest singlet rate, GH2-DESC, P4-MIX or FACE-SG.
## Records, resource checks and limitations

The scripts, plans, receipts, logs, 120 small diagnostic CSVs and 30 complete
analysis-detail JSONs are in `runs/gap-long-sheet-guide-astra/`.
`manifest.json` names and hashes all raw records, downloaded sources,
sampler sources, analysis sources and excluded pilots. Every packaged file
is under 1 MB. The 1,201,153,186 bytes of production raw records, including
configurations and duplicate scratch CSVs, remain in the fresh scratch
directory named above; the durable small copies do not include the large
configurations or slice time series. Scratch is temporary storage: hashes
establish identity, not retention. The README specifies the binary layouts.

The manifest verifies 60 zero-exit, reaped production processes, no overlap,
and completion of each phase's analysis before the next phase's sampling.
All production receipts record the five thread-limit environment variables
as 1. Runtime thread-pool introspection during packaging returned no pools;
it supplied no additional measurement of worker thread counts. The minimum
recorded free-memory percentage was 83%; maximum sampler peak RSS was
39,632,896 bytes. The sampler and Python analysis include 2 GB RSS stops;
there was no resource-stop event. Analysis peak RSS is not retained as a
separate maximum, so the sampler maximum is not presented as a global peak.

Exact nice 10 could not be applied: lowering inherited nice 20 raised
PermissionError. Every recorded sampler and controller stayed at nice 20.
This is the explicit scheduling deviation. The lock release receipt says
`status: released`, `lock: null`. No further numerical job follows it.

`record_checks.json` verifies source hashes (including the frozen GH2/P4
analysis versions), small-copy hashes, Python syntax, zero exits and record
size limits. Its first bookkeeping attempt raised KeyError because older
GH2 receipts carry a source hash but no source-path field; the checker then
used their fixed `sheets.cpp` source. The receipts and scientific records
were not rewritten. `environment.json` records compiler, Python, NumPy,
SciPy and platform versions. Verification checked 21 saved configurations
through the separate matrix readout path; this does not independently
validate the Markov law, equilibration or an asymptotic theorem.

There is no common-gap estimate, no all-beta or all-volume result, and no
proof discharge. Even locally passing fits have finite-volume, operator-
overlap and selected-window systematics outside their quoted statistical
errors. The infinity endpoint fixes trivial holonomy. P4 and the face were
measured only at beta_M=2.4; the face has one longitudinal size. A matrix
readout check, a published spin calibration and agreement of two starts are
different limited controls; none is evidence for uniform exponential
clustering. No fresh held-out confirmation was triggered, because GH2 had
no eligible two-size dip. The failed face bins were not silently enlarged.

Only this report and `runs/gap-long-sheet-guide-astra/` were added. Work is
local and uncommitted on `research/gap-long-sheet-guide-astra`; nothing was
pushed or posted. No FINISH, registry, audit or scientific-status file was
changed. Sussman–Alpoge source readings remain credited to Ethan Sussman and
Levent Alpoge, with Claude and Codex as authors of their text; their outline
and complete account were each fetched once at `31a47c543775`.

RESULT: GUIDE — all three serial measurements recorded; GH2_2 monotonicity, order-one P4 x_p rates and the face anchor-versus-0.5 comparison remain OPEN; specified extraction gates FAILS; no proof step discharged and no mass gap claimed.
