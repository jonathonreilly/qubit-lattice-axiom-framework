# Selective independent production endpoint and aggregation check

2026-09-21. No production-data discrepancy or aggregation defect was found in
the checked scope. The24 preselected physical endpoints passed reconstruction;
all144 declared point estimates and144 standard errors agree with independent
aggregation of the complete saved per-history table. The source, manifest,
receipt and analysis identities authenticate as described below. This is not
a full generator replay, a phase conclusion or a formal audit disposition.

## Selection and preserved read boundaries

Before opening any production summary, observable output, certificate, table
or NPZ array, I read the unchanged protocol/analysis plan and identity-matched
source definitions. `SELECTION.json` fixes one-based replicate indices17 and41
in every cell N in {16,32,64,128}, beta in {0.1,1,10}; the declared cell sizes
are256 for N<=64 and64 for N=128. Seeds follow the protocol's exact formula.
No endpoint was replaced according to its result.

`DECLARED_RECONSTRUCTION.md` records the independent integer, Fourier and
covariance formulas before data access. The selection seal is
`0eb3bb10d144a4a6db6be22c1a05a466a1d331ae10e7ec537611e5ff34d39902`.
The full independent NPZ reconstruction was sealed before stored outputs were
opened, at
`4e8175bd91c040100607bb0ef1805772953ad6db5e2e156fe33274658726a60b`.
The independent full-table aggregation was additionally sealed before reading
the final analysis estimates or rendered table, at
`e7d0c83092e658d1cb299f2eab6e813a4c71ff0dd9eee61ed7ec0458c4298670`.
These three artifacts and all content they bind remain unchanged.

## Physical endpoints and16-mode reconstruction

The24 archives contain14,376,960 stored site entries in total. Starting only
from their partner, identity and site-birth-count arrays, the new checker
verified signed32-bit partners/IDs and unsigned16-bit birth counts, full
reciprocal nearest-neighbor matching, no self partner, a permutation of
IDs0,...,V-1, and xor1 partner IDs. It reconstructed birth histograms, total
birth budget V, total reuse, maximum site births and the multiple-birth-site
fraction. All matched the subsequently opened stored outputs.

For positive-edge matching indicators n_i and sigma=(-1)^(x+y+z), it formed
the exact integer field Q_i=6F_i=sigma(6n_i-1). The discrete divergence
sum_i[Q_i(x)-Q_i(x-e_i)] vanishes exactly at every checked site. The orientation
counts, every parallel plane flux, the winding integers Phi_i and the identity
sum_x Q_i=6N Phi_i all agree. Hence the checked winding normalization is
W=sum_i Phi_i^2/(3N). Reconstructing the original ASCII byte stream from each
archive also recovers all24 stored precompression ASCII hashes, without
writing or retaining a large reconstructed ASCII file.

The mode calculation uses direct separable contractions of Q with three
one-dimensional complex phase vectors, independently of both the C++
sitewise direct sums and the author's NumPy FFT. For the orthonormal field
z_i=V^-1/2 sum_x F_i(x)e^(-2pi i ell.x/N), the divergence row is
d_i=1-e^(-2pi i ell_i/N). The projection is |d @ z|^2/||d||^2; d is not
conjugated in the divergence. ST=(||z||^2-longitudinal)/2.

All384 mode comparisons passed the predeclared absolute1e-8 power tolerance.
The largest C++ power difference is8.1601392309949e-14; the largest difference
from the author FFT is1.3322676295501878e-15. The largest independently
reconstructed Fourier Gauss residual is1.83323423297617e-16. The mode set has
shell counts3,6,4,3 at squared lengths1,2,3,4, with one representative of each
conjugate pair. No tolerance or selection rule was changed after seeing data.

A final endpoint cannot establish every historical record move, birth-site
assignment or timestamp. In particular these checks do not replay the
Gillespie dynamics or independently certify the RNG streams. The remaining
2472 physical arrays were hashed but were not decoded or reconstructed here.

## Full production and table authentication

The manifest and summary contain exactly the2496 distinct declared cases and
seeds, with no additions or replacements. All recorded statuses are
`full_verified`; all per-run process receipts have exit code0. Their commands
match the declared beta, kappa=1, cap10^9 and source-bound executable. The
manifest's source, wrapper, protocol and binary hash pins match actual files.
This authenticates the recorded completion/status coverage; the new physical
reconstruction remains the24-endpoint subset above.

All2496 receipt identities and all14,976 files they list were independently
hashed in place, totaling3,182,599,753 bytes. This includes every stored NPZ,
trajectory CSV, per-case JSON, verification certificate and stdout/stderr.
All2496 per-run stderr files are empty. `RECEIPT_FILE_HASHES.jsonl` retains the
complete file inventory. No large arrays were copied into this evidence tree.
Hashing the trajectories is an identity check, not an event-stream replay.

For every history, the saved per-history sufficient statistics were separately
reconstructed from its stored per-case output and certificate: four shell
means, winding power, the two distinct axis fourth-moment numerators, winding
square, time/V, slides/V and multiple-birth-site fraction. The largest table
reconstruction difference is5.551115123125783e-17. This validates table
derivation from the stored certificates; it does not convert the unselected
author certificates into independently rebuilt physical endpoints.

## Independent means and standard errors

The full2496-row table was grouped by the12 declared cells. Each history is
one unit; modes are averaged within a history. Independent compensated scalar
sums give the column means and paired sample covariance matrix S. For
g=m_a/m_b^q, q=1 or2, the nonzero gradient components are
g_a=m_b^-q and g_b=-q*m_a*m_b^(-q-1); the reported SE was independently
recomputed as sqrt(gradient^T S gradient/n). This uses the covariance quadratic
form instead of importing the analyzer's influence-vector implementation.
Linear means use sqrt(S_aa/n).

All144 point estimates and144 standard errors agree. The maximum absolute
differences are5.551115123125783e-15 for estimates and
1.942890293094024e-16 for SEs. All cell counts, completion/exclusion flags,
declared bootstrap seed indices, metric statuses and SE-method labels match.
The rendered TABLE.md agrees exactly with the saved results after applying
the declared formatting.

The unchanged, previously independently checked whole-history bootstrap
mechanics were reused as requested. The10000 production resamples and their
quantiles were not recomputed. All144 stored interval entries and their
defined/undefined metadata were authenticated and checked for structural
consistency, and the table reproduces them. This is not an independent
quantile recalculation or a claim about percentile-interval coverage.

No inference about finite-volume bias, asymptotic scaling, Gaussianity,
equilibrium sampling, topological-sector weights, phase structure or wave
physics follows from this verification. The Gaussian comparison constants
remain conditional definitions in the source plan, not verified physical laws.

## Preserved failure, sources and reproduction boundary

The endpoint and authentication/aggregation executions passed on their first
runs. The first final table-text comparison failed because this independent
checker's Markdown separator had six cells under a five-column header.
The stored table and primary analyzer were correct. The original checker,
full traceback, expected text and exact rendering delta remain as
`RENDER_ATTEMPT_*` and `compare_analysis_before_table_separator_fix.py`.
Only that separator was corrected; no production value, estimator or tolerance
changed. The successful final comparison has empty stderr. There are no open
findings against the production sources or outputs in this bounded review.

Key identities:

- Protocol: `4dae8ad738bf49af9b01ac6dada4f8f35383f317d6716b9e4de279797b999d48`.
- Analysis plan: `13db5d01088ff610b4787b89b42c04cc048e0322fb666a0985141011352e13ab`.
- Corrected analyzer: `9da84212404a18f7a1eaf6be7ddef3bfab657d6d8f5c201bba5778ac4720597a`.
- Production MANIFEST: `5ef3455f4902be019f0863754c14b44b447914eed3f3219a17891fa29c6a00e2`.
- Production SUMMARY: `310e9bc256bbad3e03cefd5d44258d781ea431e42b5e253114eedfbc4a948ea0`.
- Analysis PER_HISTORY: `2bfcb1b31f4d4010488920652cd43163c624121f5d8826bbf10417baa398aa88`.
- Analysis RESULTS: `51b2f9b5174877030b7ebb8baa345dd030dbeb23b3ca3072f6525fb73ed79c86`.

`FINAL_SEAL.json` binds complete source, prior-review and evidence identities.
The three runnable checks are `reconstruct_endpoints.py`,
`authenticate_and_aggregate.py` and `compare_analysis.py`; their full commands
and logs are preserved. The first two refuse to overwrite their completed
result files. Reproduction should preserve the originals and the external
input paths rather than modifying this sealed evidence. All new writes are
inside this assigned directory; prior reviews, primary sources, external
arrays, Git state and audit status were left unchanged.
