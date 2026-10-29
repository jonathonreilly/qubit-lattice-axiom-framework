# Pre-stated review criteria for the separate mass-gap target

Frozen input: MASS_GAP_TARGET.md at 9761471ab46e659ce856e2b9c7c10fef2b06cf5c, SHA256 d721bd77d36e6f96a1ce408c57d333776e17058a453b8c887ec0daf9f067cedf. Complete source read before these criteria; no computations yet. This is a sufficient-criterion and scope review, not a mass-gap construction. Same-context methodology remains current-main ca2bc7ddf64790da96cd43d42017d000fbfe4808. The completed determinant and lattice-bridge reports stay frozen.

1. Derive the spectral projection lemma independently, including domain/positivity, [0,m) versus endpoints, unique vacuum and finite excited spectral infimum. Check whether observable-dependent prefactors and onset times suffice, whether a common rate is necessary, and what density means.
2. Check the lattice-to-reconstruction quantifiers separately: a common hierarchy, physical units, centered reflected observable convergence, uniform constants and a nonvacuous separation range. In particular, decide whether the stated fixed-t passage has explicitly controlled its onset time t_F as well as m and A_F; no cutoff-dependent late window can be silently replaced by a uniform onset.
3. Verify the auxiliary massive-block example exactly; verify the selected-observable counterexample spectrally, and construct controls for a family-dependent rate and a closing cutoff gap. An interacting infrared estimate is absent unless actually supplied.
4. Read the cited primary Clay statement and OpenAI announcement, recording exact inspected scope. Do not infer the content or validity of an unreleased proof from a scope announcement. Confirm the SU(N) versus every compact simple-group distinction.
5. Record precise dispositions and smallest corrections; confirm any coordinator fix in this same reviewer context before freezing the final report. Preserve failed controls and bind complete source/evidence hashes. Write only REVIEW_MASS_GAP_TARGET_ASTRA.md and checks/review_massgap_target_*.

## Preserved implementation failure and diagnostic

The first exact-control run is retained as 15/16, not relabeled as all-pass. Its `low_spectral_weight_cannot_cancel` predicate compares an expanded SymPy expression to an unexpanded one using structural `==`. Before the diagnostic: require the polynomial residual of the intended identity to be exactly zero and require the remaining polynomial to have positive coefficients for positive q,w. Keep the original script/stdout/stderr and its failure. This checks the intended algebra without changing the scientific inequality.
