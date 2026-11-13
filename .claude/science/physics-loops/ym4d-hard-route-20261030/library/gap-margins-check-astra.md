## Repo search

Searched `*.md` and `*.tex` on `origin/main`, `pr/10114`, `pr/10133`,
`pr/10134`, `pr/10141` in `/Users/jonreilly/Projects/Physics`, with the
requested bounded `git grep ... | head` commands. Terms: `gap-margins`,
`Bennett acceptance`, `stack interpolation`, `cut.and.reglue`,
`dilute.gas.*glueball`, `heat.bath.*SU.?2`, `SEED-FP`, `gap-transport`.
The final search, excluding queue tables and raw prompts, returned 23
lines below its cap of 36. Earlier searches with `K_E` and generic
`dilute.gas` saturated their caps with unrelated hits; no absence claim
uses those searches.

| Relevant source hit | Exact content and closeness |
|---|---|
| `origin/main:research/mass-gap/library/gap-skeleton-final.md:475-490` | Records the existing dilute-gas estimate: seed time about twelve inverse glueball masses; n=10 near beta=2.30. This size estimate predates row 918. Reuse it; this check does not claim it as a new result. Its transport rows at 157-160 concern a flow/Hessian criterion, not this sampler or its error estimates. |
| `pr/10133:.claude/science/toe-ruleset-20261021/agents/ym4d-proof/checks/cw/README.md:1-32` | Describes an earlier SU(2) heat-bath/overrelaxation scan and jackknife spectroscopy. It explicitly says its scripts support no proved statement and raw configurations are not committed. Related method, not a check of lane918's colouring, BAR or gluing implementation. Credit that earlier Grok PR's campaign separately. |
| `origin/main:docs/HIGGS_MASS_WILSON_LOOP_SPECTROSCOPY_BOUNDED_NOTE_2026-05-10_higgsH3.md:365`, also on the four PR refs | Search hit is a bibliography description of SU(N) subgroup sweeps. It supplies no lane918 algorithm check or margin. |
| Local `library/prior/gap-seed-size.md`, sections 1-2 | Already collects spectrum inputs and computes a dilute-state seed model (row 706). Used for provenance, not recomputed. |

No row-919 check, BAR implementation check, or cut-and-reglue check was
found by these terms. `prior/repo-search-2026-11-08.md` was read; it concerns
other RG targets. No separate "Repo prior work" lines occur in row 919.
The registry search for the target and these numerical objects found no
other owner. This is the assigned check, not an attack on the seed,
transport, EXC or free-wall proof obligations owned elsewhere.

Search revisions, in the ref order above:
`4d88da5504d356762deb6b1a1c2695336af9fb81`,
`f76f6c649cff7dffbab664d8976e680e8f287fe9`,
`89faef229ff6e6bde42baad15ed8270c2f4087d8`,
`1e70c7211a2cdbc39001e619f1dd89db45e25851`,
`c73ad7b177d94f89ff37b77386936e3d52b48b05`.

Codex / gpt-6-astra / xhigh; source checkout
`b0fa8c588e746972cbb83ffd7474e2346fb20b75`; 2026-11-13.
Research check of FINISH row 918, GUIDE only, not an audit; grants no status.
Author checked: Claude Opus 5.5, high. The target-specific prior note is absent.

Scope: check the sampler, twist/BAR estimator and errors, thermal and seam
free energies, gas extrapolation, transport, EXC, and each margin verdict.
No long reruns. No numerical run can discharge a proof obligation.

Index first: read `sa-index/README.md`, searched chunk files and
`obligations.md` for the objects above and for transfer operators.
No heat-bath/BAR/thermal-sum/torelon/glueball/free-wall entries matched.
`chunk-02.md:95-106` locates the established positive trace-class transfer
and trace identity at SA 2313-2336, read directly from
`/Users/jonreilly/ym4d-lead/sa/YM4_sketch_500.tex` at the supplied
`31a47c543775` revision. It says the operator "is positive and trace class"
and gives `Z_s(0)=Tr L^s`, without an extra Haar volume factor. This is
existing Sussman--Alpoge work, with Claude and Codex as authors of their
text. It is reused, not rederived. No claim about a missing theorem in
CA-I/II/III or Balaban's papers is made or needed for this script check.

## 1. Sampler and twist estimator

Read the full 401-line row-918 note and `su2lat.py`, `twist.py`, `split.py`,
`ti.py`, `ana_ti.py`, `ana_fw.py`, `ana_split.py`, `spec.py`, `gas.py`,
and `ana_exc.py`. The following are written checks, not conclusions from runs.

**Sampler: HOLDS on the simulated extents, with a detailed-balance distinction.**
Sources: `su2lat.py:64-155`, `validate.py`, `out/validate_{A,B,C}.log`.
For a direction-mu link, another direction-mu link in its plaquette is at
x plus/minus e_nu. Every retained such neighbour changes either an odd-cycle
colour digit or the combined even/free parity bit. On an odd periodic cycle,
the last vertex gets colour 2; both closing edges therefore change colour.
Free closing plaquettes have zero coefficient. These classes are independent
conditional blocks. Extent-one periodic directions are excluded from this
argument and were not used in the campaign.

Writing the weighted staple as A=kV, the one-link density is
exp(beta k Re(UV)). The code samples W=UV with scalar density proportional
to exp(beta k w0) sqrt(1-w0^2), then returns U=WV*. Away from the explicit
small-k substitutions, the rejection sampler has that density in exact
arithmetic. At zero staple its separate normalized-Gaussian draw is Haar.
The map U -> V* U* V*
is an involution, preserves Haar measure, and preserves Re(UV).
Thus each conditional heat bath and each overrelaxation step has detailed
balance. Their fixed ordered composition preserves the Gibbs law; the full
sweep is not generally reversible. These statements describe the ideal
updates: `_h1` substitutes the Haar scalar law at beta k<1e-9, and the
outer update substitutes Haar at k<1e-12. For nonzero k these are tiny
approximations, as is floating-point arithmetic, not exact detailed balance
of executable samples.
The validation logs reproduce the quoted 3^4 differences (about 1.1 and
0.3 nominal standard errors), strong-coupling comparison and free-wall Haar
moments. The sequential comparison shares `staple` and `_h1`; it tests the
colour scheduling independently, not those common routines. The written
conditional-law calculation above checks their normalization separately.

**BAR point estimator: HOLDS; reported error: FAILS.**
Put w=beta(s1-s0)X and d=log(Z1/Z0). Then p1/p0=exp(w-d), so
E0 logistic(w-d)=E1 logistic(d-w). This is the equal-count equation solved
by the code, with the correct sign and endpoints. BAR has no s-quadrature
error. For unequal counts, the code also has the correct
M=log(nf/nr): its equation is sum0 logistic(w-d-M) =
sum1 logistic(d+M-w). For constant work w=c it returns d=c,
including unequal counts. All campaign comparisons use equal counts.

`twist.py` adds the variances of adjacent BAR links. Both links use the
same intermediate X sample. The missing covariance is positive to first
order: in the small-step limit d_i = beta ds (mean X_i+mean X_(i+1))/2.
An interior mean has total coefficient beta ds, whereas separate variance
addition counts only two coefficients beta ds/2. Its variance contribution
is therefore halved. A bootstrap/jackknife must resample each ensemble once
and recompute the whole telescoping sum. Fixed short blocks also do not
establish thermalization or an autocorrelation plateau. Simpson and BAR
use the same chains, so their agreement is not independent statistical
validation.

**Cut-and-reglue identity and sampler: HOLDS for the even a used.**
The two endpoint partition functions are Z(2a) and Z(a)^2 with the same
normalized Haar variables. The summed staples differentiate precisely the
interpolating action. The altered forward/backward time maps are mutual
inverses. Both maps flip time parity when a is even, so the update classes
remain proper. Thus Delta=2g(a)-g(2a) has the printed integral sign.
The finite reconstruction is only a lower sum:
g(2)=Delta(2)/2+Delta(4)/4+Delta(8)/8+g(16)/8.
`ana_split.py` computes a possible tail interval but prints and uses only
the lower endpoint for ratios and join excesses. Its table is not an
unbiased measurement of g; this does not rescue a resolved doubling ratio.

## 2. Gas, spectroscopy and CORE conclusions

**Gas extrapolation: HOLDS as a specified model calculation; FAILS as a
validated uncertainty bracket or as the claim that the even sector carries
all the seed.** `gas_2.3.txt` and `gas_2.5.txt` print the reported first
passing cube times 9/10 and 14/17 for the four chosen masses. But at beta=2.5,
m0=0.9, N=14 they print S=1.795e-4 and S_ev=9.407e-5: S_ev/S is about 0.524.
Almost half is flux. At the same coupling with m0=0.7, the SH-shape table
has S(17)=0.3540 > 0.3 and S(18)=0.1741 < 0.3. The reported SH range
14--17 must be 14--18 (spatial sides 336--432).

The pre-existing `prior/gap-seed-size.md` already records the roughly twelve
inverse-mass scale, with quoted Athenodorou--Teper inputs m0=1.224(16) at
beta=2.2986 and 0.6563(56) at beta=2.509. These are nearby, not identical,
couplings. They do not support calling 1.3--1.4 or 0.7--0.9 uncertainty
brackets. Recalled string tensions, higher masses, multiplicities and critical
couplings remain model inputs. The independent Poisson gas formula is
algebraically consistent; it does not bound interactions, missing states,
finite-volume mass shifts or lattice dispersion errors. Agreement with a
flux ratio and a torelon energy checks only the flux part, not the glueball
thermal trace which controls most claimed passing boxes. No resolved cold
measurement validates the glueball trace at 2e-4 precision. The two-sigma
agreement criterion in Step 4 is too weak when the errors are orders of
magnitude above the target. The printed first-passing integers are verified
as log transcriptions, not as independently rerun model outputs.

**Spectroscopy and transport: FAILS as a measured lowest-level rate; retain
only an illustrative TIGHT comparison.** `spec.py` computes log C(d)/C(d+1)
on a periodic T=16 lattice. Even a single exact level gives
C(d)=A[exp(-Ed)+exp(-E(T-d))], hence
log[C(d)/C(d+1)]=log[cosh(E(T/2-d))/cosh(E(T/2-d-1))], not E.
It falls towards zero near the midpoint for any fixed E>0. Thus the
beta=2.5 sequence ending at 0.076 and 0.025 cannot show an odd energy
below 0.1. Nor are these finite-temperature log ratios rigorously upper
bounds on the vacuum excitation energy. Excited-state and thermal-transition
contamination need control before assigning masses or comparing their drops.
For a hand-checkable example, take transfer eigenvalues 1 and 1/2 and an
operator interchanging their eigenvectors. At T=16, d=7, the log ratio is
log(5/4), strictly below the actual excitation energy log(2). Thus transfer
positivity alone supplies no claimed upper-bound interpretation.

The arithmetic log(1.3/0.9)/0.2 is about 1.84. The two quoted masses have no
resolved plateau, and their errors are chosen summaries, not fitted
uncertainties. Even treating both 0.2 errors as independent standard errors
gives a linearized error about 1.35, not a derived range 0--3.8. Taking the
endpoints of both individual one-sigma ranges instead gives 0--3.81; that
rectangle is not a one-sigma interval for the ratio. Moreover the rate is
over [2.3,2.5] on 8^3, while the budget concerns [beta0,2.3] on b>=256.
The transport hypothesis is therefore UNMEASURED, even if the chosen proxy
1.84 is called TIGHT against the budgets. There is also an arithmetic
correction: log[b/(2 ceil(log2 b))]/2.3 gives **1.2055, 1.7112, 2.2347**
at b=256,1024,4096, not 1.21,1.69,2.17. Using 2.3-beta0 instead changes
these only slightly. The displayed strong-coupling integral
log(log(102400)/log(4)) is about 2.12; extending its asymptotic integrand
to beta=1 and assigning a constant rate over [1,2.3] are untested model
choices. The box sizes 2e3--2e4 are conditional arithmetic, not measured
transport requirements. Row 708's K about 3.3 is a previously recorded
string-tension scale proxy, not a bound on all levels.

The early definitions twice write an extra G in the denominator of K_eff.
With their own definition <E>_t=-partial_t G, the correct formula is
K_eff=(partial_beta G)/(t <E>_t); Step 7 uses this form. At finite T the
measured functions are G_t-(t/T)G_T and its beta derivative, not G_t and
its derivative. A t-difference also adds G_T/T to the inferred energy.
Hot-box action shifts are not measurements of individual level deficits.

**CORE verdicts: FAIL as the advertised pre-registered ROOM/NO ROOM map.**
At beta=2.3, (a,b)=(6,6), even the original underestimated BAR errors give
0.03329-2(0.10119)=-0.16909 < log(0.9). At (6,8), the corresponding lower
endpoint is -0.12810. Both are TIGHT under the original two-sigma criterion,
not ROOM. At (4,8), -0.26514+2(0.17779)=0.09044 > log(0.9), so the blanket
NO ROOM for a<=4 also fails its own rule. These statements precede any
error correction. No sampled shape has b>=24a. A trend on b<=8 proves no
verdict for that aspect ratio or for all a below a recalled transition.
At beta=2.5 the BAR estimates nominally fail the threshold on the measured
(6,4), (6,6), (6,8), (8,8) boxes. At (8,8), however, the improved Simpson
value -0.563(323) crosses the threshold at two sigma, and all error caveats
remain. Keep the finite-box evidence for failure, not the extrapolated
claim "none for a<=8". Values above the exact bound rho<=1 must not be
clipped into a new one-sigma upper bound on Q0 without a stated confidence
construction.

## 3. Beta integration and cut/free-wall free energies

**Beta-TI identity: HOLDS. Calling its finite-reference value G itself:
HOLDS AFTER CORRECTION. Errors: incomplete.** Sources: `ti.py`,
`ana_ti.py:15-55`, `ana_fw.py:11-31`, and the `ti_*` logs.
With normalized Haar measure, F(0)=0. The derivative of F is the sum of
active plaquette means, including the free-wall masks. Thus the exact
integral measures

    H_T(t) = F(t)-(t/T)F(T) = G(t)-(t/T)G(T) <= G(t).

The trapezoid weights and propagation of independent per-point variances
are correct. The grid starts at 0.5 with an artificial exact (0,0) endpoint;
there is no quadrature-refinement error estimate. Annealing in beta and
short fixed bins leave equilibration and correlation errors unchecked.
Shared T=16 data correlate every H_T(t), its finite differences, and its
endpoint derivative. The tabulated K_eff errors do not track that joint
covariance. The T=12 free-wall version has the same issues.

The logs support large positive estimates in several hot boxes, vastly
above 1/5041. That is useful GUIDE NO ROOM there. It does not establish
the table's **"NO ROOM at N<=4 (measured)"**: the seed cube at N=4 is
4 x 8^3, not the cited 4 x 4^3. There is no resolved thermal measurement
of that seed cube. At beta=2.3 its twist estimate is also TIGHT, as above.

**Spatial join: HOLDS AFTER CORRECTION of the finite-T substitution.**
The source `gap-cutth-max.md:62-77` uses the **vacuum** cut expectation,
lim_(T->infinity) <X_cut>_T/T. At finite T the expression printed as
(J-INT) in row 918 and `fw.py` measures

    E_T(a) = E(a)-(a/T)E(T),

not E(a). Unlike G(T), the join excess E(T) has no fixed sign here.
Neither a bound nor an equality to E(a) follows by dropping it.
`fw.py`'s cut masks and integration derivative are otherwise consistent.
The report's delivered join numbers come from differences of truncated
g estimates, not a resolved vacuum-subtracted spatial-cut measurement.

**Free-wall verdict UNMEASURED: HOLDS.** The time-regluing identity and
even-a sampler were checked in section 1. The positive-transfer facts give
g>=0, g decreasing, and Delta=2g(a)-g(2a)>=g(a)>=0. They also give the
tail upper bound used in `ana_split.py`, but not permission to discard
that tail in a ratio. Ratios of Gaussian estimates whose denominators
straddle zero have no useful bounded confidence interval; their printed
medians are not measurements of k. Negative Delta estimates at 1.8 and
2.4 nominal sigmas warrant checking errors/equilibration/quadrature, but
alone do not prove which one failed. The observed precision is roughly
0.1--0.6, far above the seed scale (for k=3, 1/(4k^6)=1/2916).
"3000 times" is an order-of-magnitude comparison with a chosen 1e-4
resolution, not an independently measured signal/noise ratio.

The spectral proxy does not change this verdict. Differences of two
contaminated effective-energy estimates do not bound the difference of
two true gaps. The multiplicity ratio n'/n about 2 and a 1/b^2 mass shift
are additional assumptions. The prediction k about 16 is conditional on
them; neither TIGHT nor NO ROOM for the actual doubling bound follows.

## 4. EXC estimator, errors and verdict

**Sector identity: HOLDS; implemented high-spin observable and errors:
HOLDS AFTER CORRECTION. Verdict UNMEASURED: HOLDS.** Sources:
`gap-filter-ls-opus.md:101-175`, `gap-exc-check-opus.md:65-79`,
`su2lat.py:173-202`, `twist.py:44-49,97-108`, `ana_exc.py`, and
`out/exc_summary.txt`.

Writing p=(1-rho)/2 and inserting P_-=(1-C)/2 gives exactly

    <N>_- - <N>_0 = rho(<N>_0-<N>_v)/(1-rho).

The one-link integration has the right character normalization: with
Sigma the selected staple, A'=A-Sigma, k'=|A'|, k=|A| and d=2j+1,
its numerator is
`[d (2/beta) I_d(beta)] [(2/(beta k')) I_d(beta k')]
chi_j(A'^* Sigma/k')`, divided by `(2/(beta k)) I_1(beta k)`.
This is the code's Bessel ratio and character recurrence. Selected
plaquettes have c=1 because the twist time slice is excluded. Time-translation
invariance of the trace gives the one-slice count. Signed per-configuration
estimators are allowed; negative estimates do not alone refute positivity
of the exact sector expectation.

However, `nmax=11` sums only j=5/2,7/2,9/2,11/2. Calling this the full
j>=5/2 count needs an omitted-tail bound, which is not supplied. The
"all half-integer" proxy is truncated too. This matters to the exact
observable identification even if the numerical tail is plausibly small.

`ana_exc.py:12` clamps the sampled log rho at -1e-4, and first replaces
a positive fitted central value by -1e-3. This creates artificial mass
near a tiny denominator; it is not a confidence procedure. The note
correctly marks the two rho-about-one cases undefined, despite their
enormous printed script values. In the other cases the procedure still
omits correlations between rho and endpoint spin means, as well as BAR's
missing covariance. The saved NPZ files contain X/Y, not the spin time
series needed to recover that covariance.

The final claims "0 within about 1e-3 on all 9 defined runs" and uniformly
"4 times below noise" do not follow from the saved table. There are seven
non-singular rows there; (4,8,2.3) has median -0.0108 and 16--84 percent
range [-0.039,-0.003]. Two low-spin examples have positive central values
whose one-sigma intervals include zero. The strongest spin-3/2 indication,
(6,8,2.5), is +0.123 with range [0.076,0.20]; this is a proxy observation
with the above error qualifications, not a high-spin excess.

The 100--200-fold extrapolation assumes, without a model for it, a second
factor-ten enrichment from 3/2 to 5/2. In addition, gamma about 0.010
in row 881 is the **integrated electric-reference** boost gain per L_i.
It is not a necessary lower bound Delta(1)>=0.010 L_i in the isotropic
theory. The exact target integrates Delta(s) ds/s. A small value at s=1
cannot determine that integral. No boosted-s measurements were made.
Several rectangular runs also lack a spatial side equal to time a and
therefore are proxies outside the stated (a,a,c,d) family. UNMEASURED is
the defensible verdict; the proposed enrichment is not a measured DRESS
margin or a refutation of EXC.

## 5. Per-item disposition

These are research-check verdicts only. "Nominal" below uses the author's
printed errors, whose coverage has not been established.

| Item | Check verdict | Margin supported by this record |
|---|---|---|
| Odd-extent heat bath and overrelaxation | HOLDS on used extents; full-sweep detailed balance is not asserted | A valid invariant-law algorithm; convergence/error control still needed |
| Twist interpolation and BAR equation | HOLDS | Central estimates usable as GUIDE |
| BAR and associated ratio errors | FAILS: shared-ensemble covariance omitted | No validated two-sigma margin |
| CORE | HOLDS AFTER CORRECTION of classification and scope | Nominal TIGHT at beta=2.3, (6,6), (6,8), (4,8); nominal NO ROOM in the clearly failing measured boxes; actual b>=24a regime UNMEASURED |
| Beta-TI and seed S | HOLDS AFTER CORRECTION to H_T; numerical errors incomplete | NO ROOM in resolved hot boxes as GUIDE; cold seed UNMEASURED; no measured blanket N<=4 conclusion |
| Even sum S_ev | HOLDS AFTER CORRECTION of the gas reading | UNMEASURED; the negligible-flux claim fails at one advertised first passing box |
| Gas size forecast and recalled inputs | HOLDS as conditional code/log arithmetic; validation/bracketing FAILS | Cube forecasts 18--20 and 28--34 are parameter scenarios only; SH forecast at beta=2.5 corrected to sides 336--432 |
| Transport K_E and magnetic deficit | FAILS as a measured level/cold-trace rate | UNMEASURED for the consumer; TIGHT only for a selected effective-mass proxy; hot magnetic signs are measured plaquette differences |
| Time-regluing and spatial joining | Identity/sampler HOLDS; finite-T/tail interpretation needs correction | Free-wall k and E UNMEASURED; spectral proxy does not settle their margins |
| EXC high-spin excess | Sector identity HOLDS; truncation and error interpretation need correction | UNMEASURED; low-spin signs and enrichment guesses do not decide EXC |

## 6. Verification and limits

All fourteen files in `guide/lane918/scripts/` were read in full.
The source note, the two gas outputs, validation logs, both periodic
spectroscopy logs, EXC summary, twist result rows, split/free-wall result
rows, free-wall spectroscopy rows and thermal integration grid/endpoint
records were inspected. Additional source ranges are cited
above. Log parsing and elementary arithmetic were used only to check
transcription and comparisons. No sampler, long job, gas mesh, bootstrap
or spectroscopy fit was rerun. In particular, there is no new corrected
BAR confidence interval and no independent verification of stored random
samples or quoted external spectrum tables. Existing logs remain at
`library/guide/lane918/out/`; sources were not edited.

The independence here is the written conditional-law, likelihood-ratio,
finite-reference and finite-period spectral checks, plus direct comparison
with raw script/log artifacts. A second-provider label is not itself
evidence. No proof obligation was discharged. Only this report was written,
incrementally, in the pinned checkout; it is left uncommitted and unpushed
for the lane lead.

RESULT: GUIDE check requires corrections: the sampler, BAR equation and time-regluing construction hold on the used geometries, but BAR errors omit covariance, CORE ROOM fails the stated two-sigma criterion, finite-reference/tail terms are dropped, gas summaries contain explicit numerical contradictions, and spectroscopy does not measure the claimed transport rate; retain hot-box NO ROOM as scoped GUIDE evidence and UNMEASURED for the cold seed, transport, free-wall doubling and EXC, with no proof or status granted.
