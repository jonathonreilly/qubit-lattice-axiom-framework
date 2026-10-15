# Affected confirmation: coherent count normalization wording

Reviewer `/root/inertial_response_check`. I read the complete delta from the
canonical note at SHA-256
`72113d39011cd2a29beb3355edae2d122549f0369769fdb59b51594f48a9e711`
to
`4a2bd6a11b68dc115a80cf716564baf195502dd3efc1b249eeea644e36b8269e`.
The earlier independent and author-comparison reports/identities remain
unchanged. This is a focused text confirmation, not a full canonical review.

The repair resolves the scoped normalization finding. Section 7 now explicitly
identifies chi as the source-frequency-normalized phase before turnaround
multiplication. It defines the bounded unit-duration count contrast as
kappa sum_j beta_j chi(t_i,j), and says the displayed weights and harmonic
response absorb alpha*kappa=1 without setting either factor separately to one.
The plane-wave substitution is now expressly into that multiplied contrast.
These statements agree with section 6 and the independently frozen null-leg
calculation.

Only these explanatory sentences changed. The displayed chi, windows, joint
amplitude, exact matrix, scope and conclusions are unchanged. No code, fixture,
threshold or mathematical normalization factor was altered. The old working
note remains historical; the canonical clarification does not retroactively
change its bytes or the report that identified the issue. No suite rerun is
needed for this text-only change, and none was performed.

The author repair record matches both note hashes and the original finding
report hash. The exact delta is retained as
`COHERENT_NORMALIZATION_AFFECTED_v1.patch`. No unresolved scoped normalization
discrepancy remains. All reviewer writes are confined to this independent
directory. No source, index, branch, lock, state or publication was changed.
