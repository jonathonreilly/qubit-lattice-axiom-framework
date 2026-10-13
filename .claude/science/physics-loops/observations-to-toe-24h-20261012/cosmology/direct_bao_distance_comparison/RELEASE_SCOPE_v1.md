# Exact release and statistical scope

The official likelihood repository is explicitly designated by sectionX of
DESI DR2 II, arXiv2503.14738v2 andv3. The selected ALL files at commit
bb0c1c9009dc76d1391300e169e8df38fd1096db descend unchanged from the
March20,2025 DR2 addition b7b8a36e9bccb063081f811f323cada21ab5fbdd.

The release covariance is the exact numeric covariance used here. Its
diagonal errors are not identical to rounded Table4 errors in either paper
version: for example BGS has sqrt(.00578998687), about.07609, while the
table displays.075. The table says systematics are included, so attributing
this difference to extra systematic errors is not established by that text.
The discrepancy is retained. Means and covariance are sourced directly from
the designated likelihood release, not reconstructed from the displayed
errors. Separate component files permit an ordering/rounding cross-check.
No model result is used to select a covariance.

The thirteen entries include one DV/rd and six correlated DM/rd,DH/rd pairs.
Lyalpha appears DH beforeDM in the actual ALL file; preserve that order.
The quoted transfer quadratic is a linear-Gaussian GLS diagnostic with an
unbounded amplitude nuisance for its analytic covariance formula. Physical
positivity is checked on the calibrated amplitude; a positively truncated
posterior is not computed or claimed. No sampling p-value is reported.
'Without diagonalizing' in the protocol means retaining off-diagonal
covariance entries, not forbidding eigenvalue/Cholesky numerical checks.

The pre-data protocol and fixed six model histories precede this block's
primary numeric retrieval. General cosmological context was already known,
and published numbers became exposed during source inspection. This is a
frozen transfer comparison, not a globally blind or independent replication
of the underlying DESI measurement. Raw clustering templates and sound-horizon
physics are not supplied by this candidate calculation.
