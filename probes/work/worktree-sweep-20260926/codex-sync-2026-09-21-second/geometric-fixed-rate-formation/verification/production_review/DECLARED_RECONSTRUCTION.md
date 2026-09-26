# Declared independent endpoint and aggregation check

Written before opening any production observable table, summary, per-case
output, verification certificate or NPZ array. The unchanged protocol and
analysis plan, source definitions and prior source-review/correction evidence
have been read. This is not a generator replay or a phase inference.

Selection is deterministic: one-based declared replicate indices17 and41 in
each of the12 cells N in {16,32,64,128}, beta in {0.1,1,10}. The first nine
cells declare256 histories each; the three N=128 cells declare64. No selected
index will be replaced based on outcome. The seed is
210000000+10000*N+1000*beta_index+replicate, with beta_index=0,1,2 in that order.
All24 exact paths, seeds and cell counts are recorded in SELECTION.json.

For a selected archive, read only its partner, identity and births_at_site
arrays at first. Flattening is x-major: site=(x*N+y)*N+z. Reconstruct integer
nearest-neighbor displacement, reciprocal partner matching, absence of self
partners, and a permutation of record IDs0,...,V-1 with paired IDs differing
by xor1. Birth counts are nonnegative uint16, their sum is V, and the number
of distinct recorded pairs is V/2. Compute total excess birth count
sum_x max(b_x-1,0), fraction with b_x>1, maximum b_x and the complete birth
count histogram. A final snapshot tests endpoint consistency, not every
historical move, birth location or timestamp.

Let sigma=(-1)^(x+y+z), n_i(x)=1_{partner(x)=x+e_i}, and
F_i(x)=sigma(x)[n_i(x)-1/6]. Work first with exact integers
Q_i=6F_i=sigma(6n_i-1). At full packing verify
sum_i[Q_i(x)-Q_i(x-e_i)]=0, the three positive-edge orientation counts and
their sum V/2, and equality of all N parallel plane fluxes
Phi_i=sum_{x:x_i=a}sigma(x)n_i(x). Check sum_xF_i=N*Phi_i exactly using Q.
Compute W=sum_i Phi_i^2/(3N).

The16 declared nonconjugate modes have squared lengths1,2,3,4 and their first
nonzero component positive. They are explicitly recorded before data access.
For each, independently contract three one-dimensional phase vectors against
each Q_i to obtain

    z_i(ell) = [6 sqrt(V)]^-1 sum_x Q_i(x) exp(-2pi i ell.x/N).
    d_i = 1-exp(-2pi i ell_i/N),
    power = sum_i |z_i|^2,
    longitudinal = |sum_i d_i z_i|^2 / sum_i |d_i|^2,
    ST = (power-longitudinal)/2.

The divergence row uses d @ z, without conjugating d. This direct separable
DFT differs from the author's full NumPy FFT and C++ sitewise direct sum.
Predeclared comparison tolerances are absolute1e-8 for saved powers and1e-9
for the reconstructed Gauss residual, matching the already checked wrapper
limits. Integer properties are exact. Any failure is retained; no seed or
tolerance is changed in response to results. Seal reconstructed endpoint
results before reading their stored JSON outputs/certificates for comparison.

For the full per-history table, preserve one completed history as the unit.
With ST modes averaged within each history, the11 columns are S1,S2,S3,S4,W,
mean_axis(ST_mode^2),S1^2,W^2,time/V,slides/V,and fraction of sites with b_x>1.
Independent aggregation uses compensated scalar sums for column means and
the paired sample covariance matrix, rather than importing the analyzer.
For a ratio g=m_a/m_b^q, q=1 or2, its gradient has
g_a=m_b^-q, g_b=-q*m_a*m_b^(-q-1); its delta-method SE is
sqrt(gradient^T sample_covariance gradient / number_of_histories).
For linear means this reduces to sample SD/sqrt(number_of_histories).
Ratios of means are distinct from means of per-history ratios.

Check every declared point estimate and SE in all cells, plus sample counts,
fixed lexicographic bootstrap seed indices, exclusions and metric statuses.
An empty cell, fewer than two histories, or a zero denominator must retain its
defined/undefined scope. Reuse the previously independently checked paired
10000-resample implementation; do not rerun it absent a concrete concern.
Authenticating a stored interval does not independently validate its sampling
coverage. Conditional Gaussian references remain assumptions, not conclusions.

Authenticate manifest/summary/analysis identities and every listed per-history
receipt file by streaming hashes in place. Decode only the24 selected NPZ
arrays; all large arrays remain external. Verify that the saved per-history
table is consistently derived from the per-case JSON/certificate records,
but distinguish those author certificates from independent reconstruction of
the unselected physical arrays. No production event-stream replay is claimed.
