# Independent winding-stiffness diagnostic check

2026-09-21. No actionable formula or implementation defect was found in the
specified adaptive diagnostic. This is a separate Gaussian-benchmark and
source/arithmetic review, not an equilibrium, mixing, phase, or physics verdict.
The prior sampler review remains separate and unchanged.

## Read boundary and evidence

The complete plan was read first. `PRE_COMPARISON.md`, `benchmark_check.py`
and its complete output were sealed before opening the new author script or
results. The pre-comparison seal SHA-256 is
`669dc31b44e3c7b00e9b97575d81241c6ac6e0981c6d785f76369adeab897ed3`.
The complete 101-line author analysis and complete eight-case JSON were then
read. No author production or analysis program was executed by this review.

`compare_compact.py` independently verifies every new compact table, its
recorded hash, all reported arithmetic, and the seeded paired bootstrap using
multiplicity-weighted sums. It also compares every spectral/density block
against the previous 128-visit reductions and checks the first and last complete
1024-visit blocks directly from each raw trajectory. All assertions passed on
the first attempt; both full stderr files are empty. There were no failed
executions to discard. The commands are simply
`python3 benchmark_check.py` and `python3 compare_compact.py` in this directory;
their full stdout, stderr and JSON outputs are retained.

The raw-window check read 5,197,789 bytes. It verified selected sample indices,
odd-L winding integrality, and nonlinear squared-flux reduction. It did not
read, hash or replay all 150,150,494 raw bytes. The full raw hashes remain
previously recorded author provenance. The manifest, metadata, compact files,
analysis sources and results were independently hashed; complete identities
and the selected raw-window hashes are in `COMPACT_RESULTS.json` and the final
seal. The earlier sampler review is reused at its unchanged final-seal identity,
not recast as a new production reproduction.

## Gaussian normalization and finite winding benchmark

Write the orthonormal Fourier variable as Etilde(k)=Ehat(k)/sqrt(V). For the
stipulated quadratic weight exp[-K sum_x |E(x)|^2/2], a nonzero centered-divergence
symbol gives covariance K^(-1) P_T, of trace 2/K. Thus the recorded quantity
S_T=|Ehat(k)|^2/(2V) has expectation 1/K. The zero mode has three components
and no Gauss constraint; F_i=sqrt(V) Etilde_i(0), so its continuum covariance
satisfies E[F_i^2]/V=1/K. The ratio of the three-component flux average to the
four-mode S_T average is consequently one in this benchmark.

All eight actual boxes have odd side L. A closed charge-graph cycle uses
steps ±2e_i. Since twice its signed step sum equals L times its coordinate
winding, odd L implies F_i=L W_i with integer W_i. This is the relevant odd-box
quantization; it must not be transferred unchanged to arbitrary even tori.
The zero-mode energy is K W_i^2/(2L). Set sigma^2=L S with S=1/K. The correct
quantized ratio is

    d(sigma^2) = [sum_w w^2 exp(-w^2/(2sigma^2))]
                 / [sigma^2 sum_w exp(-w^2/(2sigma^2))].

Poisson summation gives

    d = 1 - 4 pi^2 sigma^2 [sum_n n^2 exp(-2pi^2 sigma^2 n^2)]
                            / [sum_n exp(-2pi^2 sigma^2 n^2)].

In particular d<1 at every finite positive sigma^2. With
r=exp(-2pi^2 sigma^2), a convenient explicit bound is

    0 < 1-d <= 8 pi^2 sigma^2 r(1+r)/(1-r)^3.

The independent checker verifies the transverse projector and compares the
direct and Poisson discrete-Gaussian formulas at four variance parameters with
high precision. In the recorded cases sigma^2 ranges from approximately
6.2629 to 17.8601. The largest resulting infinite-sum bound is
1.011e-51. The author finite sums have negligible truncation at the displayed
precision; their values 1 or 1±a machine rounding unit must not be read as exact
identities. Winding quantization within this supplied Gaussian benchmark
cannot explain a percent-scale discrepancy. This conclusion does not establish
a Gaussian effective action for the record measure: non-Gaussian sector
weights, capacity effects, finite-wavevector effects and sampling bias remain
outside this calculation.

## Estimator and paired arithmetic

The author squares each raw F_i before taking a block average. It does not
square an old block-mean F_i. The local estimator is the equal average of four
already normalized spectra, and the global estimator is the equal average
of three raw second moments F_i^2/V. Paired resampling preserves the same block
selection for both estimators and takes the ratio of their resampled means.
The independent multiplicity implementation reproduces all eight percentile
endpoints within floating-point summation tolerance.

The results use uncentered second moments, as stated in the plan. The JSON key
`global_three_flux_variance_average` denotes this second-moment estimator; it
is the target variance only using exact target inversion symmetry. Empirical
flux means are correctly reported separately rather than silently set to zero.
For odd block counts the first/last half comparison omits the middle block;
the main estimate uses all complete blocks. The listed discarded tails agree.

| L | Start | Complete blocks | Global/local | Descriptive 2.5%–97.5% interval |
|---|---|---:|---:|---|
| 17 | empty | 392 | 0.983318586 | [0.967338608, 0.999710801] |
| 17 | full | 382 | 0.993882054 | [0.976879701, 1.010130260] |
| 25 | empty | 123 | 1.011447470 | [0.978103633, 1.042348693] |
| 25 | full | 123 | 1.018030118 | [0.986836906, 1.050000149] |
| 33 | empty | 52 | 0.979367087 | [0.925606055, 1.033138288] |
| 33 | full | 54 | 1.003669774 | [0.959627643, 1.046580899] |
| 49 | empty | 17 | 0.960089475 | [0.909332523, 1.014967342] |
| 49 | full | 16 | 1.005669249 | [0.933013924, 1.075579267] |

The L17-empty interval really does narrowly exclude one: the author's exact
upper endpoint is 0.9997108009381283. It would be incorrect to say all eight
intervals include one. It would also be incorrect to call this a calibrated
rejection: this is an adaptively selected analysis of eight reused trajectories,
with 2,000 bootstrap resamples and no coverage or mixing theorem. The result is
sensitive to the interpretation of serial dependence and has no supplied
multiplicity correction or Monte Carlo endpoint-error analysis.

The new aggregate lag diagnostic flags L33-empty (local 0.289, global 0.313)
and L49-full (local 0.321). L49 has only 17/16 complete blocks. An unflagged
aggregate does not establish independence or erase the earlier sampler
review's dependence warnings for other recorded observables. First/last
halves and both starts are retained; agreement is descriptive evidence only.

## Final source binding and limits

The exact plan SHA-256 is
`a7713f111bcaf62f59c3664f7714ab5846af8d88729846535a0184347ff2956d`.
The exact analysis-script SHA-256 is
`bf7f83d313d5349f8d5e5bc345d5fbe22aa4f0ed1bebb2355c0d8382266e69ff`.
The author pre-analysis seal is
`d176654bf7ea8f12ff264835cb4672a5d52027973f5afc6a340adfec47d60302`.
The exact result, manifest, metadata and compact-file hashes are supplied in
`FINAL_SEAL.json`, together with unchanged procedure identities and all review
artifacts. No external literature was needed for this bounded calculation.

The benchmark normalization, paired implementation and compact arithmetic are
confirmed at these sources. No infinite-volume phase, equilibrium convergence,
formation-selected law, quantum vacuum, or microscopic photon conclusion
follows from this diagnostic. Nothing here upgrades the prior sampler evidence
or assigns formal audit status.
