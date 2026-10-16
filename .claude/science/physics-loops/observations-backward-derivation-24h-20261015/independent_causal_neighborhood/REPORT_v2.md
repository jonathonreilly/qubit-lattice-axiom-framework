# Narrow same-session confirmation of block08 v2

PASS for the declared conditional mathematical scope. V2 resolves the sole v1 finding. This is not a formal audit verdict, empirical validation or derivation of a physical network law.

Source SHA256: 8d665cdcf728a967ccbab4e60ffc6932343226d6bbf7eac0957a3df0ac1823e8. Runner SHA256: 1ff4ff6325d23c924e43f3d188242ae7f4a478d668b222ed88e20494531a2804. Controls SHA256: 9aae84c1923e224a36197d44f1f7ef7c2bdb83c7efe2851f78faae0288c03afb. frozen_sources_v2.json binds these files, and their hashes remained unchanged after reproduction. All v1 findings and evidence remain preserved.

The complete source/code diffs were inspected against fully checked v1. The source explicitly restricts tau to [0,1/2] and preserves the tau=3/4 counterexample. With that range, both factors 1/2-tau are nonnegative, so multiplication of the conditional single-input probability lower bounds is valid. At tau=1/2 the pair lower bound is zero and q=1, the correct trivial endpoint. The fixed-N tail at q=1 is likewise a valid trivial bound. No published numeric input or reconstructed tail changes.

The runner now tests endpoint biases and retains the out-of-domain diagnostic; source/output references point to v2. No other scientific assumptions or statements changed. Separate reproduction is exactly identical to the author JSON: eight passing controls, zero failures. execution_v2.json records the actual command, 120-second bound and runtime; reproduction_v2.stdout and reproduced_controls_v2.json preserve full results. Only the final output write was redirected, with no calculation or hashing changes. No failures or timeouts occurred.

The unchanged content retains the earlier independent support for the memory-allowing CHSH argument, conditional input factorization requirement, fixed-horizon binomial-tail induction, predictable-eligibility mixture, isotropic no-signaling pair counterfamily, affine ball-state response lemma and mixture witness. Their causal, preparation, state-sufficiency and calibration assumptions remain supplied. No other unit or research scope was opened.
