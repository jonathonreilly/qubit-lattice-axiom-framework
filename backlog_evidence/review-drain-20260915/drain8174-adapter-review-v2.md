# PR8174 immutable adapter review v2

**Accepted for bounded capture** by `/root/review_8174`, the same original reviewer, under cold-review-v1. No blocking finding.

Primary SHA: `dc13c94c2fae5e86b4a362547a6504ef655134780c023f1ea3b2d43109f978b0`. Mutation SHA: `fb3defdf7ec1d2e37e11c2191fb952e23035817f6542a8bffdf94fa857f55629`.

I verified exact hashes and entire diffs. Changes only bind the actual cold receipt and add before/after guards for frozen base `51cac1a`, staged tree `5083bc62`, exact reviewed main `3dca18dd`, ancestry and disjointness across every source/input category. Existing identity/stat guards, limits, once-only markers and full raw preservation remain intact.

Guard-only controls passed on actual Git state and rejected changed main, source overlap, tooling-input overlap, wrong HEAD and failed ancestry for both adapters. No adapter main or scientific runner was executed.

Authorized: one 17-check baseline and each of 11 mathematical mutations once, 900 seconds and 768 MiB sampled aggregate process-tree RSS per invocation, while exact reviewed main and every guard hold. No automatic retry or simulation. Preserve all failures; source remains frozen. Final evidence review and landing validation remain pending.
