## Repo search

Writer: OpenAI Codex, assigned **gpt-6-astra / xhigh**, row 1101.
The runtime model identifier is not independently exposed. Research text,
not an audit. GUIDE computations discharge no proof step and grant no status.
No mass gap is claimed. Source checkout: `16c93871f140b78f3d5b69de4b5b9de720e2f474`.

The task-specific prior record is absent. The lead's November 8 digest
concerns earlier UV/RG targets. I opened its nearest hits: a one-step
local witness in PR 10114, a momentum-chart use of ‘face’, and main's
noncompact Maxwell Wilson-loop note. None supplies this rate comparison.
Rows 1089–1090 already test boxes with one transverse plaquette; their
positive window signs are reused, not recomputed. The registry has no hit
for MON-L, gap-descent, gap-face, anisotropy, or glueball. The separate
literature row 1102 owns a literature survey, not this measurement.
Detailed source checks and the remaining search results are recorded below.

## Scope and checkpoint

This run does not cover a proof of MON-L, an infinite-volume extrapolation,
continuum scaling, all observable sectors, or the full periodic Wilson
face with fluctuating longitudinal holonomies. The requested periodic
reduced-sheet model selects trivial longitudinal holonomy; see
`gap-face-2d-astra.md`, section 2.1. A measured minimum in the stated basis
is called a measured candidate rate, not the exact common clustering rate.

Final checkpoint (2026-11-17 11:11 UTC): all sampling, fits, controls and
record verification are complete. The machine numeric lock is released.
There are 74 retained gauge chains (72 grid/anchor chains plus two 16^4
control chains) and 18 standalone O(4) chains. One affected gauge chain was
reproduced serially, with the original archived and not pooled. The pilot
is excluded. No fresh confirmation chains were triggered.

**Outcome: no sampled finite-minus-face difference is below zero by three
standard errors, even at one size. But one matched-volume scalar control
FAILS at 3.36 combined errors. These are candidate rates, not a validated
extraction of the common asymptotic clustering rate. MON-L remains OPEN.**
All six transverse-direction face rates are unresolved in this basis.
The 16^4 run is an isotropic control only; it has no matching face run.

The first implementation controls passed at GUIDE grade. Scratch:
`/tmp/sa-gap-descent-mc-astra.C6QR8N` contains the
outline and CA-I, each downloaded once at `31a47c543775`.

The test uses the requested periodic 8^4 and 12^4 volumes and couplings,
with raw slice observables, autocorrelations, binned errors and fit ranges.
A negative comparison needs both sizes, more than three standard errors,
and adequate controls. Selection over noisy observables cannot itself
establish a negative sign. No infinite-volume extrapolation was attempted.

## Source checks and reuse

Rules and the physics-loop skill were read from main `8b11ae2bb9`, through
git, without changing this pinned checkout. This is a bounded dispatched
measurement, not a new proof campaign. The task's output paths and pinned
revision take precedence over generic pack/PR instructions.

The lead digest's nearest hits were opened: PR 10114
`MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149` gives a positive one-step witness,
not a decay estimate; `BOTTOM_SECOND_CURVATURE_ASTRA.md:353–364` uses
“face” for momentum charts. Main's noncompact Wilson-loop note, lines
120–145, treats a different Dirichlet Maxwell law. None covers this target.
The refreshed main/PR search used MON-L, gap-descent, Kennedy-Pendleton and
SU(2) heat-bath terms. It found the existing SU(3) numerical protocol in
`docs/EXACT_TIER_PATH_INTEGRAL_BOUNDED_NOTE_2026-05-07_exact.md:150–184`:
SU(2) subgroup updates and time/space anisotropy. That is prior algorithmic
work, not this 2+2 SU(2) rate comparison. Search lists are preserved in runs.
PR 10114's `.claude/science/toe-ruleset-20261021/agents/ym4d-existence/REVIEW_X8.md:370–415`
and the neighbouring `REVIEW_X9.md:310–360` discuss beta=16/32 small-box ultraviolet
probes; they do not supply the finite-to-face infrared comparison either.
PR heads: 10114 `f76f6c649c`, 10133 `89faef229f`, 10134 `1e70c7211a`,
10141 `fb99b4dddc`. The initial combined fetch returned 1; these actual
local remote refs were subsequently read. No claim of exhaustive absence.

The local model source is Claude Opus 5.5's `gap-bridge-exercise-opus.md`,
section 2.2 and section 7.3. Its covariance comparison already fails because
L-plaquettes are constant on the face. The target here is only its rate
comparison. The face source is Codex's `gap-face-2d-astra.md`, read whole;
its equation (1) and holonomy warning fix the simulated face model.
Rows 1089–1090 are not rerun: their one-transverse-plaquette tests are
smaller-volume prior work, with unresolved Wilson convergence at n=3.

The outline index was searched before source reads. Neighbouring rows
`chunk-01.md:62–73`, `obligations.md:18–29`, and outline 588–599 distinguish
polynomial clustering from a spectral gap. CA-I 2697–2713 explicitly
excludes a mass-gap claim. The 4.12–4.19 index gives no matching face or
principal-chiral supplier under those searches. Credit **Ethan Sussman and
Levent Alpoge, with Claude and Codex as authors of their text** for these
scope statements. Nothing from their ultraviolet construction is used as
an infrared estimate. No Balaban paper is imported.

## Simulation and analysis contract

The density is exp(sum beta_type ReTr(U_p)/2). Directions 0,1 are
longitudinal; 2,3 transverse. The face fixes U_0=U_1=1 and updates only
U_2,U_3. Its mixed action is beta sum_e,u,a Phi_e(u) dot Phi_e(u+a),
with the transverse Wilson plaquette potential retained.

Each cycle is one heat-bath sweep and one microcanonical over-relaxation
sweep. Credit **Michael Creutz**, [Phys. Rev. D 21 (1980) 2308](https://doi.org/10.1103/PhysRevD.21.2308), and
**A. D. Kennedy and B. J. Pendleton**, [Phys. Lett. B 156 (1985) 393–399](https://doi.org/10.1016/0370-2693(85)91632-6).
The code uses the SU(2) conditional radial density
sqrt(1-r_0^2) exp(alpha r_0), with the weighted staple norm alpha.
For alpha >= 1 it uses Kennedy–Pendleton rejection; below 1 it uses
Creutz exponential-envelope rejection. Neither update changes the action
normalization between finite beta_L and the face.

The predeclared grid has 72 chains: two independent starts for each of
30 requested points and six beta_T=0 anchors. Each has 2048 discarded
cycles and 2048 measurements, four cycles apart. Seeds, commands, source
hash and record layout are in `runs/gap-descent-mc-astra/manifest.json`.
Large link configurations stay in scratch. The checkout saves compressed
raw slice records, not configurations.

Measurements retain all six plaquette orientations, and 1x2 rectangles,
separately along axes 0 and 2. The rectangle extends one step along the
measurement axis when that axis lies in its plane. Otherwise its two
orientations are averaged. Production links undergo zero or eight spatial
APE steps with alpha=1/2, excluding the measurement axis. The initial
two-step runs are preserved as the pilot below. On the face the frozen
longitudinal links remain fixed during smearing too. The restricted
smearing therefore differs from unconstrained finite-beta_L smearing;
this changes overlaps, and is not an equality of operators. Bare L loops
are exactly constant on the face and have no mass estimate.

Correlations use the spatial slice averages and all periodic origins.
Connected subtraction is recomputed in each jackknife replica. Plane-type
and scalar spatial averages are additional fixed channels. A periodic
single-state fit uses C(t)=A[exp(-mt)+exp(-m(L-t))]. The revised window
search starts at t=1 for spatial loops and t=2 for loops extending along
the measurement axis. It considers every interval with at least three
points, ending no later than L/2. Among accepted windows it takes the
latest start, then longest interval. Removing the first point must leave
a resolved mass too. These changes precede all face comparisons.
Accepted candidate rates require a positive signal above three standard
errors throughout a window with at least three points, fit p>0.05,
relative mass error below 50%, stability on removing its first point and
doubling the bin width, and cold/hot consistency. Unresolved channels stay
OPEN. Effective masses and all rejected fits are retained; a small noisy
minimum is not promoted to a rate. Statistical errors exclude finite-size,
thermal-state, overlap and holonomy systematics.

The mass uncertainty after selecting a minimum is conditional on that
choice. If a point shows a negative difference above three standard
errors at both sizes, it triggers fresh confirmation chains with the
selected observables and windows fixed. No selected noisy minimum alone
will be called a GUIDE counterexample. The search order is beta=2.3,
2.4,2.5, then beta_L/beta=1,2,4,8.

Winding-loop correlations are also saved for an isotropic torelon control.
Before examining the first beta=2.4 control fits, the analysis added a
rotation-averaged winding control: at each measurement axis, it averages
the three diagonal winding-direction correlations. It does not multiply
or combine loops of different center charges. Individual winding results
remain available. This addition changes no local-rate or face selection.
The small 2x2 Creutz ratio is a short-distance diagnostic, not an asymptotic
string tension. A winding-loop energy can be compared with the leading
string expression E= sigma L - pi/(3L), with its finite-length limitations.

## Resource and implementation record

The first preflight failed because this sparse checkout lacks
`scripts/automation_lock.py`. The main version was read into scratch and
made available with PYTHONPATH; no repository helper was edited.
The successful preflight reported 86% free memory, 42 GB free disk, and
a free numeric lock. Acquisition returned `status: acquired` at 07:44 UTC.
The sampler driver runs one chain at a time, invoked with `nice -n 10`,
with all five thread variables set to 1. Process inspection found actual
nice **20**, because the runner
already had reduced priority. `renice 10` returned permission denied for
both owned processes. No privilege change was attempted; this departure
from exact nice 10 leaves the jobs at lower priority. The manifest records
the actual value, 20.
Every chain checks the lock and at least 50% free memory; the lease is
refreshed between chains. The C++ process and Python driver stop above
2 GB RSS. No process pool is used.

`pilot_v1/control.log` records seven independent-draw heat-bath mean checks against
I_2(alpha)/I_1(alpha), all within 1.77 standard errors; weighted-staple
action agreement (2.1e-14); full-sweep over-relaxation action agreement
(2.9e-13); gauge invariance including smeared measurements; direct face
action agreement (7.2e-15); and unit quaternion norms. These are GUIDE
implementation checks, not proofs or an independent review. The short
8^4 pilot had mean plaquette 0.629914 at beta=2.4; it is excluded from
production. A brief pilot-overlap mistake occurred: the seven heat-bath
mean comparisons were evaluated while the 12^4 timing pilot was active.
A second overlap occurred at the beta=2.5 control pause: the identified
sampler exited, its successor started, and the old-PID stop failed after
the controller was stopped. The successor (`L12_b2.5_2_c0`) overlapped the
analysis before its stopped state was verified. Exact overlap duration was
not recorded. Strict serial execution was therefore **not maintained for
the entire session**. The original chain is archived in `handoff_overlap/`.
Its serial reproduction has identical raw-record, final-configuration and
warm-up-record hashes, recorded in `serial_reproduction.json`. Final fits
use the replacement once. This is reproduction, not an independent check.
The remaining handoffs waited for the whole batch to end. Wall-clock job
durations include the deliberate SIGSTOP pauses.
After the smearing change, `control_v2.log` rechecks gauge invariance of the
eight-step measurements (zero discrepancy at stored float precision),
while the shared update/action checks reproduce their earlier results.
This rerun is not an independent implementation check.

### Pilot failure and revision — GUIDE / FAILS as a plateau procedure

Ten initial chains completed with two APE steps. Their raw records, original
source, manifest and diagnostics are retained in `runs/gap-descent-mc-astra/pilot_v1/`.
The eleventh chain was deliberately stopped; its partial record remains in
scratch and is identified in `pilot_v1/interruption.json`. It is not a
completed ensemble. The sampler and controller were both confirmed stopped
before the diagnostic analysis ran, under the same lock.

At beta=2.3, the scalar signals reached the noise floor before the midpoint.
For example, on 12^4 the two-step spatial-rectangle channel along axis 0
had C(3)=1.134e-6 with error 2.394e-7, but C(4)=7.925e-8 with error
2.418e-7. Requiring every fit to reach L/2 therefore discarded the useful
early signal. The pilot also exposed an analysis defect: a shifted fit
with an unresolved near-zero mass could pass the compatibility test because
its error was large. That provisional candidate is rejected, not retained.

The revised run increases spatial APE smearing to eight steps, uses the
shorter window search specified above, and rejects unresolved shifted or
doubled-bin fits. New independent seeds start with 11020000. The complete
requested grid restarts with that basis; no pilot record is pooled into it.
This is an openly recorded design change after inspecting beta=2.3 finite
couplings, before measuring a face rate or a descent difference.

## Published comparators and normalization

All copies are open arXiv PDFs. Each was downloaded into its own new empty
directory; `sources.json` records locations and SHA-256 hashes. Formula and
table pages were rendered and inspected. No paper is copied into this checkout.

| Source and exact locator | Published comparator in lattice units | Use |
|---|---|---|
| Biagio Lucini and Michael Teper, [hep-lat/0103027](https://arxiv.org/abs/hep-lat/0103027), Table 1, PDF p.24 | beta=2.4, 12^4: m_0++=0.953(19), sqrt(sigma)=0.2634(14), torelon E=0.745(9) | Exact-size isotropic control. |
| Michael Teper, [hep-th/9812187](https://arxiv.org/abs/hep-th/9812187), Appendix A, PDF pp.11–12, Table 10 | beta=2.5: 16^4 m_0+=0.660(22), sqrt(sigma)=0.1834(26); 20^4 0.723(23), 0.1881(28); 32^4 0.70(4), 0.187(12) | Larger-volume comparator; finite-size differences are not sampler errors by themselves. |
| Lucini, Teper and Urs Wenger, [hep-lat/0404008](https://arxiv.org/abs/hep-lat/0404008), Table 5, PDF p.27 | Neighbouring beta=2.5115 on 20^4: m_0++=0.658(10), sqrt(sigma)=0.1768(8) | Context only; not substituted for beta=2.5. |
| Oleg Borisenko and Peter Skala, [hep-lat/9812020](https://arxiv.org/abs/hep-lat/9812020), equations (48)–(50), Tables 1–2, PDF pp.16–17 | 128^2, their 2 beta=2.3,2.4,2.5: second-moment xi=18.95(13),25.39(13),33.14(12) | Matched-coupling, matched-size supplemental O(4) control. |
| Roger Horsley, Brian Pendleton and Julian Wack, [arXiv:2308.14628](https://arxiv.org/abs/2308.14628), equation (10), Table 1, PDF pp.2,5 | Their beta=1.2 means our O(4) coupling 2.4; fitted xi=25.41(3) on 224^2 | Confirms the normalization and warns that 8^2/12^2 are small. Their fitted xi is not the second-moment definition. |

The O(4) single-spin correlation length is a control of the sheet measure.
It is not identified with the gauge-invariant singlet clustering length.
The supplemental 128^2 run uses the same heat bath and four over-relaxation
sweeps per cycle, two independent starts, 4096 discarded cycles and 8192
records two cycles apart. This supplements the actual 8^4/12^4 face anchors.
It does not replace those records or assert an infinite-volume limit.
Standalone 8^2 and 12^2 O(4) controls additionally compare point correlations
at every saved separation against the embedded beta_T=0 face. Their geometry
is separate, but the heat-bath routine is shared; this is limited independence.

## Completed rate comparison — GUIDE / OPEN

Write m_hat for the smallest accepted candidate in the measured basis,
and Delta=m_hat(beta_L,beta,beta)-m_hat(face,beta,beta). Errors below are
conditional on the selected observable and window; they exclude overlap,
finite-volume, thermal-state and holonomy systematics. A numerical fit
passing the gates above is not by itself an asymptotic plateau certificate.

All 24 finite-minus-face comparisons are compatible with Delta >= 0 at
two reported standard errors. Central values are sometimes negative.
The largest downward difference is beta=2.4, beta_L=19.2 on 8^4:
Delta=-0.12852 +/- 0.06683, z=-1.923. On 12^4 at the same point,
Delta=-0.01849 +/- 0.11466, z=-0.161. No point has a three-error violation
at both sizes, so there is **no first GUIDE-grade counterexample** and no
held-out confirmation run was triggered. This does not establish MON-L.

| beta | beta_L/beta | L | measured minimum | observable / direction | fit t | difference from face | z |
|---|---|---|---|---|---|---|---|
| 2.3 | 1 | 8 | 1.2241 ± 0.074 | a2_s8_scalar_R | [1, 3] | 0.58217 ± 0.085 | 6.8398 |
| 2.3 | 1 | 12 | 1.1499 ± 0.061 | a2_s8_scalar_P | [1, 3] | 0.57115 ± 0.11 | 4.9838 |
| 2.3 | 2 | 8 | 0.702 ± 0.066 | a0_s8_13_R | [2, 4] | 0.06011 ± 0.078 | 0.76863 |
| 2.3 | 2 | 12 | 0.41771 ± 0.13 | a0_s8_Mspace_R | [4, 6] | -0.16106 ± 0.16 | -0.98869 |
| 2.3 | 4 | 8 | 0.6203 ± 0.05 | a0_s8_Mspace_R | [2, 4] | -0.02159 ± 0.066 | -0.32689 |
| 2.3 | 4 | 12 | 0.59954 ± 0.093 | a0_s8_Mspace_R | [3, 5] | 0.02077 ± 0.13 | 0.15491 |
| 2.3 | 8 | 8 | 0.61361 ± 0.048 | a0_s8_13_R | [2, 4] | -0.028277 ± 0.065 | -0.43833 |
| 2.3 | 8 | 12 | 0.46427 ± 0.094 | a0_s8_12_R | [4, 6] | -0.11451 ± 0.13 | -0.84989 |
| 2.3 | face | 8 | 0.64189 ± 0.043 | a0_s8_23_R | [2, 4] | — | — |
| 2.3 | face | 12 | 0.57877 ± 0.097 | a0_s8_23_R | [3, 5] | — | — |
| 2.4 | 1 | 8 | 0.76084 ± 0.047 | a0_s8_scalar_R | [2, 4] | 0.12591 ± 0.07 | 1.7983 |
| 2.4 | 1 | 12 | 0.77554 ± 0.086 | a2_s8_13_P | [2, 4] | 0.26975 ± 0.13 | 2.1312 |
| 2.4 | 2 | 8 | 0.69763 ± 0.057 | a0_s8_Mspace_R | [2, 4] | 0.062708 ± 0.077 | 0.81619 |
| 2.4 | 2 | 12 | 0.78522 ± 0.093 | a0_s8_23_R | [2, 4] | 0.27943 ± 0.13 | 2.1311 |
| 2.4 | 4 | 8 | 0.60995 ± 0.051 | a0_s8_Mspace_R | [2, 4] | -0.024976 ± 0.073 | -0.34293 |
| 2.4 | 4 | 12 | 0.54296 ± 0.074 | a0_s8_Mspace_R | [3, 5] | 0.03716 ± 0.12 | 0.31366 |
| 2.4 | 8 | 8 | 0.50641 ± 0.043 | a0_s8_13_R | [2, 4] | -0.12852 ± 0.067 | -1.9232 |
| 2.4 | 8 | 12 | 0.4873 ± 0.068 | a0_s8_13_R | [3, 6] | -0.018493 ± 0.11 | -0.1613 |
| 2.4 | face | 8 | 0.63493 ± 0.052 | a0_s8_23_R | [2, 4] | — | — |
| 2.4 | face | 12 | 0.50579 ± 0.092 | a0_s8_23_R | [3, 5] | — | — |
| 2.5 | 1 | 8 | 0.75881 ± 0.07 | a0_s8_Mspace_R | [2, 4] | 0.15242 ± 0.091 | 1.6679 |
| 2.5 | 1 | 12 | 0.44126 ± 0.14 | a0_s8_13_R | [4, 6] | -0.043681 ± 0.17 | -0.26168 |
| 2.5 | 2 | 8 | 0.64308 ± 0.059 | a0_s8_12_R | [2, 4] | 0.036687 ± 0.083 | 0.43965 |
| 2.5 | 2 | 12 | 0.78989 ± 0.086 | a0_s8_13_R | [2, 4] | 0.30495 ± 0.12 | 2.5375 |
| 2.5 | 4 | 8 | 0.5801 ± 0.06 | a0_s8_13_R | [2, 4] | -0.026293 ± 0.084 | -0.3123 |
| 2.5 | 4 | 12 | 0.56331 ± 0.079 | a0_s8_13_R | [3, 6] | 0.078372 ± 0.12 | 0.67925 |
| 2.5 | 8 | 8 | 0.53079 ± 0.041 | a0_s8_Mspace_R | [2, 4] | -0.0756 ± 0.071 | -1.0574 |
| 2.5 | 8 | 12 | 0.66489 ± 0.074 | a0_s8_12_P | [2, 6] | 0.17995 ± 0.11 | 1.6075 |
| 2.5 | face | 8 | 0.60639 ± 0.059 | a0_s8_23_R | [2, 4] | — | — |
| 2.5 | face | 12 | 0.48494 ± 0.084 | a0_s8_23_R | [3, 6] | — | — |

The units are inverse lattice spacings. `a0` means longitudinal separation,
`a2` transverse; `s8` means eight spatial APE steps; `P` is a plaquette and
`R` a spatially oriented 1x2 rectangle (orientation averaged when both sides
are spatial). Plane `13` is mixed; `23` is T. `Mspace` averages the mixed
planes not containing the separation axis; `scalar` averages all three
spatial planes. Thus each row identifies both the observable and direction
setting its measured minimum. L/T group aliases are not independent channels.

Every face minimum is set by `a0_s8_23_R`. No transverse face channel passes
the plateau gates; L-plaquettes on the face are constant and are excluded.
Consequently these minima cannot rule out an unseen slower sector. Both
directional minima, all rejected windows and all effective masses are saved
in [tables.md](../runs/gap-descent-mc-astra/tables.md),
[fit_inventory.csv](../runs/gap-descent-mc-astra/fit_inventory.csv) and
[effective_masses.csv](../runs/gap-descent-mc-astra/effective_masses.csv).

The largest local-loop integrated autocorrelation time over the 37 ensembles
is 2.430 saved records (four HB+OR cycles per record); the largest local
mean/t=2 hot-cold discrepancy is 3.781 combined errors. The analysis uses
64-record bins and a 128-record comparison. These diagnostics do not test
all slow modes. The maximum standalone O(4) autocorrelation time is 3.635
records, with two HB+4OR cycles per record and 512/1024-record bins.

Effective-mass figures: [beta=2.3](../runs/gap-descent-mc-astra/plateaus_beta2.3.png),
[beta=2.4](../runs/gap-descent-mc-astra/plateaus_beta2.4.png),
[beta=2.5](../runs/gap-descent-mc-astra/plateaus_beta2.5.png).
A central effective mass at a fit-window endpoint may use a neighbouring
correlator outside that window. Several accepted fits contain only three
correlator points, so their evidence for asymptotic isolation is limited.

## Published controls — GUIDE, with a failed rate-extraction control

The fixed scalar control is the eight-step spatial-rectangle average,
not a minimum over all observables. The matching-volume results are:

| beta | volume | axis | candidate rate | fit t | published scalar mass | z |
|---|---|---|---|---|---|---|
| 2.4 | 12^4 | 0 | 0.9849 +/- 0.1040 | 2–4 | 0.953 +/- 0.019 | +0.30 |
| 2.4 | 12^4 | 2 | 0.9740 +/- 0.0451 | 1–3 | 0.953 +/- 0.019 | +0.43 |
| 2.5 | 16^4 | 0 | 0.8792 +/- 0.0615 | 2–4 | 0.660 +/- 0.022 | **+3.36** |
| 2.5 | 16^4 | 2 | 0.6815 +/- 0.1358 | 3–5 | 0.660 +/- 0.022 | +0.16 |

**FAILS:** the beta=2.5, 16^4 axis-0 candidate misses the published scalar
mass by more than three combined errors. Later axis-0 windows fail the
signal gate; they are not substituted to obtain agreement. The axis-2
estimate agrees but is imprecise. This demonstrates that the candidate-fit
procedure has not reliably isolated the asymptotic mass in every case.
It prevents promoting the rate table to a calibrated common-gap comparison.
It does not by itself identify a defect in the sampling measure.

The smaller-volume scalar results also differ: at beta=2.4, 8^4 gives
0.7608(474), 0.7729(582), compared with the 12^4 benchmark 0.953(19).
At beta=2.5, 12^4 gives 0.4960(527), 0.5076(666), compared with the 16^4
benchmark 0.660(22). These mismatched-volume comparisons are retained,
not treated as exact-size calibrations. The added 16^4 pair used the same
burn/measurement counts, seeds 31010000/31010131, and the resource gates.

The winding controls are more consistent at matching volume. On 12^4,
beta=2.4, the pooled energies are 0.6289(798), 0.6782(859), t=4–6,
against 0.745(9). Their leading-string sqrt(sigma) proxies are
0.2443(136), 0.2526(142), against 0.2634(14). On 16^4, beta=2.5, the
proxies are 0.17995 +/- 0.012 and 0.17421 +/- 0.011, t=6–8, against
0.1834(26). Each matching-volume proxy is within two combined errors.
This uses the leading string correction, not a controlled infinite-string
limit. The 8^4 beta=2.5 axis-0 proxy, 0.21122 +/- 0.00096, differs strongly
from the 16^4 value; its axis-2 pooled fit is unresolved. All individual
winding fits remain in the records. No 2x2 Creutz ratio is called sigma.

The matched 128^2 O(4) checks reproduce the published second-moment lengths:

| coupling | measured xi_2nd | published xi_2nd | z |
|---|---|---|---|
| 2.3 | 18.959(290) | 18.95(13) | +0.030 |
| 2.4 | 25.306(276) | 25.39(13) | -0.275 |
| 2.5 | 33.234(322) | 33.14(12) | +0.273 |

Energy-per-bond discrepancies are -0.93, -0.55 and +1.06 combined errors.
Doubling bins changes the xi errors to 0.268, 0.339 and 0.343; the largest
hot-cold xi discrepancy is 1.26 errors. The separate small-lattice geometry
also agrees with the embedded beta_T=0 sheets at every saved separation:

| coupling | largest absolute z on 8^2 versus embedded 8^4 | on 12^2 versus embedded 12^4 |
|---|---|---|
| 2.3 | 2.252 | 0.814 |
| 2.4 | 0.509 | 0.522 |
| 2.5 | 1.062 | 1.254 |

The standalone and embedded implementations share the radial sampler;
this is limited independence. The spin correlation length is not equated
with a gauge-invariant local-loop clustering length.

## Record verification and delivered artifacts

[record_verification.json](../runs/gap-descent-mc-astra/record_verification.json)
checks 74 gauge archives and 18 O(4) archives, their hashes, shapes,
finiteness and bounded observables. A separate 2x2 complex-matrix path
recomputes all 24 bare loop means on four final configurations, including
the face and the 16^4 control. Its largest discrepancy is 2.55e-8, within
float32 storage precision; quaternion norm errors are at most 6.67e-16.
These checks do not discharge a scientific proof step.

An I/O defect was found during source inspection: an unopened optional
`ofstream` initially tests true, so a non-anchor run attempts one unused
spin write before its stream fails. This does not modify links or consume
random draws, and the retained anchor records passed their shape/value
checks. The experimental source is frozen as `su2.cpp` for exact provenance.
The supplied `su2_guarded.cpp` successor uses an explicit save flag and
checks stream opening, writing and flushing, including configuration output.
It was not used for the experiment. Two small seeded cases have identical
records/configurations under both versions, and two intentional I/O-failure
checks propagate the expected errors; see `io_guard_check.json`.

The scripts, manifests, per-chain receipts, raw compressed observations,
complete per-channel analyses, figures and logs are in
[runs/gap-descent-mc-astra](../runs/gap-descent-mc-astra/README.md).
Large configurations, binaries, downloads and the interrupted pilot remain
in the named scratch directories. `pilot_v1/` and `handoff_overlap/` preserve
excluded history. The final analysis uses each retained chain once.
The numeric lock release receipt reports `status: released`, `lock: null`.
No audit verdict, retained-grade status, physical axiom, or mass-gap claim
is supplied. These local files are uncommitted and unpushed.

RESULT: GUIDE / OPEN — no two-size three-error descent violation; one matched-volume rate-extraction control FAILS, so MON-L is neither killed nor validated.
