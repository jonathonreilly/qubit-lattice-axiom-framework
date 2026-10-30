# MATCHA numerical criteria — preregistration

Only the following finite diagnostic is proposed. It is not a gauge-model
integration, an all-history test, or a proof of RM2. The written argument
will be the primary evidence.

1. On a two-point ancestral space with unequal positive masses, a normalized
   two-point output kernel, four distinct original source labels and an output
   insertion, compare the direct unnormalized mixed derivative with the
   derivative reconstructed from the ancestral mass times the normalized
   expectation. Use exact rational arithmetic. All sixteen subset
   coefficients must agree exactly. Deliberately freezing the source-dependent
   ancestral mass must disagree for at least one nonempty subset. Report a
   failed comparison as FAIL; do not change the model or tolerance afterward.

Execution requires a nonblocking exclusive lock, actual nice >= 10, all six
thread variables equal to one, every load average < 8, available and free
memory fractions >= 0.30, and peak RSS < 1 GB. Do not use RLIMIT_AS or pools.
If any preflight fails, run no mathematical diagnostic and report NOT RUN.
No finite diagnostic is allowed to establish the analytic inequalities,
history uniformity, regeneration, or independent mathematical review.
