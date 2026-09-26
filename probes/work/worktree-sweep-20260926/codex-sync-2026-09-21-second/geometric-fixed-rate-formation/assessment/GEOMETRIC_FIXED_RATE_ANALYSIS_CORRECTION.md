# Analysis correction after selective source review, before production values

2026-09-21. The completed independent source review identified three
reporting/edge-case defects. Its original report, source identities and
failure controls remain sealed. The original protocol and analysis plan
are unchanged. No production observable values have been inspected to
choose these repairs.

All twelve declared cells are now reported, including cells with zero
completed histories. Bootstrap seeds use their declared lexicographic
indices. Counts distinguish capped histories, deadline nonstarts and other
failures. Any partial sample is described as conditional on full verified
completion, with its actual exclusion causes. A wrapper exception preserves
its error/traceback and is excluded without requiring the name or receipt
that the wrapper does not promise. If a partial receipt exists, its bytes
are hashed but its file list is not certified by the analyzer.

Each metric has separate estimate, standard-error and interval statuses.
A zero empirical denominator makes that ratio undefined while preserving
other defined metrics. If even one bootstrap resample has zero denominator,
the affected entire percentile interval is reported undefined, together
with the defined and undefined resample counts. No resample is dropped or
replaced. A cell with no completed histories has no estimates or intervals.

For linear means, the standard error is the sample standard deviation over
the square root of the number of completed histories. For a ratio
g=m_a/m_b^q, q=1 or2, use the paired delta-method influence

    I_j=(X_aj-m_a)/m_b^q - q m_a (X_bj-m_b)/m_b^(q+1).

Its sample standard deviation divided by sqrt(n) is the reported ratio SE.
It retains within-history numerator/denominator covariance. This SE is a
first-order uncertainty estimate; it is distinct from the declared paired
percentile bootstrap. It is undefined with fewer than two histories or a
zero point denominator. The original successful nondegenerate estimators
and all paired resamples remain unchanged.

These corrections implement the existing protocol and specify previously
unhandled cases. They do not change the simulator, case set, event cap,
primary observables, exclusions or physical interpretation.
