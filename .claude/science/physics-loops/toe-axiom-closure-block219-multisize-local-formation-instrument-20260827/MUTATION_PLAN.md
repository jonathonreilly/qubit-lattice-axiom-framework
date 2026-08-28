# Mutation Plan

The primary runner has 26 load-bearing mutations.  They alter the transient
center or shell, physical complement, radius, size/coordinate/global metadata,
branch normalization/deletion/lock labeling, translation/cubic covariance,
rank, held-volume separation, success probability, typed critical pairs,
terminal support, history marginalization, numerical rule digest, autonomous
scope, voter completeness/bias/dark states, readable-label covariance and
commit locality.  Final result:

- baseline: `38/38`;
- mutations detected: `26/26`.

The independent runner has 23 nonidentical mutations.  They alter either
frozen numerical digest, held size, displacement, event/edge ownership,
translation, rank, kernel, raw probability, complement, three-branch
completeness/typing, typed critical pairs, reversed cylinders, scope/commit,
voter branch completeness/bias/absorption/label covariance and held commit
locality.  Final result:

- baseline: `33/33`;
- mutations detected: `23/23`.

Every mutation exits nonzero, emits at least one named `FAIL`, and ends with a
nonzero-failure `TOTAL:` footer.
