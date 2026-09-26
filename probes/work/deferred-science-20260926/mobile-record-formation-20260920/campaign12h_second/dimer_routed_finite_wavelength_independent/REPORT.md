# Independent finite-wavelength and original-analysis review

2026-09-21. Bounded scientific check, not an audit or a phase assessment.
The projection, covariance-curvature identity and four statistics reconstruct.
All original N<=128 history statistics, means and standard errors agree with
independent reconstruction. The selected bootstrap intervals and the unfitted
winding benchmark comparison also agree. **One minor display correction, F1,
remains open at this seal:** a fixed plot limit clips one error-bar cap. No
mathematical or numerical-aggregation defect was identified.

The complete derivation was reconstructed and sealed before opening author
projection controls, the original analyzer or by-axis comparisons. Earlier
generator/endpoint evidence was reused at unchanged identities. No N256
observable, unrelated quantum work or other new theory was opened.

## F1: clipped one-standard-error bar

`compare_dimer_routed_finite_wavelength.py`, SHA-256
`14fbb2aa97e2a5e8da70ca963c57a28db1e57307248b24661b9c43193b4b3bd5`,
line 72 fixes the propagation-error y-range to (-0.08,2.3). For N=64, the
winding x mode at t=21/16, the saved and independently reconstructed values are

    mean = 2.196496360849972
    SE   = 0.11232465801764097
    mean + SE = 2.308821018867613.

The figure advertises points plus/minus one SE, but this upper cap lies outside
the panel. The JSON value is correct. Raise only that upper limit above the
endpoint, for example to 2.4; retain the estimates, predictions and scope labels.
`FINDINGS.json` binds the exact source, point and requested change. The parent
acknowledged the finding and will preserve the reviewed source/plot bytes before
a separate narrow correction. No primary source was changed by this review.

## Independent projection and curvature reconstruction

The primary mathematical note, `DIMER_ROUTED_FINITE_WAVELENGTH_PROJECTION.md`,
is 6,357 bytes, SHA-256
`c125636d6e2808e0f9ea452187bd3533159d4953205faf4bb68bc148c6c14aeb`.
`PRE_COMPARISON_DERIVATION.md` contains the full independent argument; the
precomparison seal is
`a195d2e03d1ab0034263415942ef6bef8423d598c830bebdc312b3a45f790f5f`.

At uniform p, the symmetric pair tensor has zero row/column means. Conditioning
the actual current, with rate c=k0/2+h/4, on its four distinct context labels
gives A_delta/4, (k0/2)I, -(k0/2)I and A_delta/4 on the probability tangent.
The middle conditional means include the appropriate subtraction of p. This
checks the physical outer factor one half and prevents a factor-two error in
both damping and propagation.

For a winding-channel displacement a_delta=delta-e1 and z=k.a_delta, multiplying
the exchange factor exp(-iz)-1 by the four reindexed coefficients yields

    symmetric: -2k0 sin^2(z/2) I,
    context:   -(i/2)[sin(2z)-sin(z)] A_delta.

Their sum is B(k)=-d(k)I-iA_6(q_eff), with exactly the source's d and q_eff.
The normalized fields (sqrt(7)e,sqrt(7)b/2) have covariance I6, and

    A_6(q)=(2gamma/7) [[0,-C_q],[C_q,0]],  C_q v=q cross v.

The seven unused linear tangent moments do not introduce a coupling into
these six. The axis formulas and the different leading winding-direction
damping coefficients, 4k0 versus k0, follow directly from the channel sum.
The small-k expansion q_eff=k+O(|k|^3) is correct.

The symmetric constant-swap part preserves the full linear Fourier space.
The remaining generator is antisymmetric in the invariant product L2 law.
Writing LF=BF+R and L*F=B^dagger F-R gives

    C'(0)=B,
    C''(0)=B^2-E[RR^dagger].

This is an initial-derivative identity, not an exact finite-time closure.
At gamma=0 the residual is zero and the invariant linear-space exponential
is exact. At gamma!=0 a nonzero residual supplies a direct countercontrol to
claiming closure without another argument.

Our separately assembled four-position cycle uses all 14^4=38,416 states,
four distinct context positions, k0=5/4, axis e1 and Fourier phase pi/2. Exact
integer sums and rational arithmetic give, at gamma=1,

    E[RR^dagger] = diag(2/49,11/98,11/98,15/196,15/196,15/196),
    trace = 97/196.

The residual vanishes at gamma=0. Both derivative identities and all four
conditional projection matrices are checked exactly. This auxiliary cycle
is not an N=4 physical cubic torus. Additional independent controls compare
the unsimplified symbol against the compact formula at oblique wavevectors,
both coupling signs, zero coupling and zero wavevector. Matrix exponentials
are checked against the scalar statistic formulas at 60 chosen size/axis/time
points before any production comparison.

## Statistic normalization and original data reconstruction

Let n=Q/|Q|, P_L=diag(nn^T,nn^T), P_T=I-P_L and
`D=[[0,iC_n],[-iC_n,0]]`. Then D^dagger=-D, D^2=-P_T, and
`U=P_L+cos(omega t)P_T+sin(omega t)D`, omega=(2gamma/7)|Q|. Thus the signed
cross target is positive sin(omega t) with the recorded negative Fourier phase.

For endpoint covariance I6 and two-time covariance C, the four means are

    error             = 2-Re tr(U^dagger C)/3,
    transverse auto   = Re tr(P_T C)/4,
    signed cross      = Re tr(D^dagger C)/4,
    longitudinal auto = Re tr(P_L C)/2.

For the projected axis benchmark, r=exp(-Ntd) and
theta_eff=(2gamma/7)Nq_eff,axis t reduce them to
`2-r[2+4cos(theta_eff-omega t)]/3`, `r cos(theta_eff)`,
`r sin(theta_eff)` and r. Unit equal-time endpoint variances remain in the
error formula. The deterministic damped-trajectory substitute is wrong: at
C=I/2,U=I it gives 1/4 instead of the correct stationary error 1.

After sealing this reconstruction, the complete original protocol and analyzer
were read. Their observation times are 0,7/16,7/8,21/16,7/4. These times were
then substituted into the same independent formulas; the precomparison control
times were merely independent test choices, not a change to the original
schedule. The four statistics, normalization, mode averaging and whole-history
uncertainty conventions match the protocol.

`rebuild_histories.py` reads the raw JSON Fourier fields for every original
history, independently forms the E/B component cross products and continuum
prediction, and derives the four quantities without importing the author's
observable function. It reconstructs all eight cells, 960 histories and 57,600
history/time/mode/statistic values. Modes are averaged within each history
before the between-history standard error is computed. Means use compensated
sums; SE is

    sqrt[sum_h (x_h-mean)^2 / (R(R-1))].

The raw reconstruction was fixed in `RAW_RECONSTRUCTION_SEAL.json`, SHA-256
`ab5767777c7d9e278735ba0da851c224792f679b1b34aa1879bcfab16a9c5319`,
before comparing saved numerical statistic arrays. Source/schema metadata had
already been inspected; the raw calculation did not use the saved estimates.

The 57,600 history values agree within 1.78e-15 absolute error. All 2,784 saved
mean/SE entries were checked, including per-mode and mode-averaged statistics,
component variances, attempts, acceptances, color changes and wall time. Their
maximum discrepancy after scaling by max(1,absolute saved value) is below
1.27e-15. The largest absolute discrepancy, in the large auxiliary quantities,
is below 9.1e-13. Seed, count, attempt and other copied history metadata agree.

Every original manifest, dispatch, summary, receipt and output payload was
authenticated: 960 receipts and 3,840 payloads totaling 450,177,989 bytes.
All receipt-to-history key mappings were separately checked. The original
N<=128 size boundary is asserted before opening any history. Endpoint state
files were hashed, not decoded again. This is not a trajectory replay or a
new independent decoding of every key/count flag. The previously sealed
sixteen-endpoint/implementation review remains the independent decoding input.
Raw production arrays were not copied into this packet.

## Bootstrap and author comparison

The original analyzer resamples whole histories using multinomial count vectors
with R draws and probabilities 1/R. A count vector is used for every retained
time/mode/statistic from that resampled history; modes are not treated as
independent replicates. The 10,000-draw seed is fixed and the percentile bounds
use the ordinary linearly interpolated empirical quantile. These are pointwise
bootstrap intervals, not simultaneous coverage or exact finite-sample coverage.

Before interval-value comparison, `QUANTILE_SELECTION.json` fixed eight checks:
propagation error and signed cross at t=7/8 and 7/4 in N=16 winding and N=128
irregular. The declared RNG stream was advanced through all eight cells in its
original order, but only those selected intervals were computed. Manual sorting
and interpolation at (B-1)p reproduce all sixteen endpoints within 2.23e-16.
This bootstrap-weight replay is distinct from replaying the dynamics RNG.
The other bootstrap intervals were not independently recomputed.

The complete author projection checker, original analyzer and comparison script
were inspected: respectively 140, 179 and 92 lines. The author exact cycle uses
the e3 axis and k0=11/10; its derivative and residual matrices match the rotated
independent result, including trace97/196 and the constant-rate zero residual.
All twelve N<=128 size/axis benchmark tables were independently recomputed at
the original five times; maximum discrepancy is below 4.45e-16. Every by-axis
observed mean, SE and difference and all four mode-averaged comparisons agree
with the independently checked original analysis and benchmark.

The original and copied analysis JSON files are byte-identical. The original
analysis source and sign-control bindings are correct. The frozen theoretical
projection file contains N256 predictions, but no N256 measured observable;
only N<=128 predictions were evaluated in this review. Its timestamps and
stated scope identify it as a post-outcome mechanistic follow-up after the
original mode averages, not a preregistered confirmation. The benchmark has no
fitted parameter and is consistently described as an unproved exponential
closure at gamma=1. It is not applied to the irregular matching.

The comparison figure correctly labels one-SE bars, the projected benchmark,
the Euler target and the post-outcome scope. The PNG was viewed after the
numerical clipping scan identified F1; the PDF was byte-authenticated but not
separately rendered. Apart from that cap, no displayed point or one-SE bar lies
outside the specified panel ranges. No claim of exact finite-time closure or
new damping law is inferred from agreement or disagreement with the curves.

## Source identities and reproduction limits

The principal author identities are:

| File | SHA-256 |
|---|---|
| Projection checker | `d6c825f3efcac8aa0a49a614d33add45c406d47d24872b89fc4a1122ed2a6df6` |
| Original analyzer | `752ccdd5506c5f7714bb7c97175dde7fc179ba8592a9248df4a8dc00760e283c` |
| Original RESULTS | `08aab30040e7b0c50c60486bf769f7c87247d8771f3f2315d577725fd4d60345` |
| Original PER_HISTORY | `433459f27af8320e915c9568bfa8d726d94483c8cf85cffec6b0f20d1fdfcf92` |
| Original AUTHENTICATION | `62d3fcbb7c9ce85900df21568de5014f637c828c1e36c5f07e0fc8c57a6820a1` |
| Frozen projection RESULTS | `89bd6b739074ffd695e0883394339bb975248e1e9793510bee3b84bafb9aa556` |
| Comparison RESULTS | `51fdd3128de3e2e6edc181740e49cd56c134e337bd4d05ec5c771962f228d7eb` |
| Comparison PNG | `298b9cfe4166c8592e94ae4ce298d3e537a73cbdaa067c59c14cd452d94f0102` |
| Comparison PDF | `d6feb78f8312e9533f8612a16b4b780fdab471ba8d149f6cac36a43ce9ef4a89` |

`FINAL_SEAL.json` supplies the complete source and artifact bindings. The
external payload identities are transitively bound by
`RAW_HISTORY_AUTHENTICATION.json`, not duplicated in the final seal.
Executable checks are `independent_projection.py`, `rebuild_histories.py`,
`compare_analysis_and_benchmark.py` and `final_evidence_check.py`. Run them in
a reproduction copy to preserve sealed outputs. Full stdout, stderr and
execution receipts are preserved. All four first executions succeeded;
there were no helper failures to erase or conceal in this packet. F1 is an
identified display defect, not a failed reconstruction.

The raw histories' statistical independence rests on the supplied sampling
construction and the earlier implementation review; this packet does not prove
all RNG properties. The current checks do not extend to N256 data, higher
wavevectors, thermodynamic extrapolation, a quantitative Euler remainder,
quantum identification or a propagating geometric Gauss field. No primary
source, publication, Git state or audit status was modified.
