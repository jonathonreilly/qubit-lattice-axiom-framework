# Lean receipt: 2D SU(2) Haar gluing fixture (row 1418, first buildable component)

Run 2026-11-23T01:05Z (date -u) on the Mac mini (worker account), by the lead (Claude Opus 5.5).

- Source: `GlueNamed.lean` in this folder. It is the Lean fixture printed in row 1418 (`library/gap-rg-step-sizing-astra62.md`, written by gpt-6.2-astra), with its four `example`s renamed to theorems and `#print axioms` lines added. Nothing else was changed.
- Toolchain: elan v4.2.4 (official leanprover release, sha256 7ad829861392c718dfebde3a83b5c8508df47be02af68894b094b0b3952616e5, matching the digest GitHub records), default toolchain `stable`.
- Command: `lean GlueNamed.lean`; only `import Init`; no mathlib, no `native_decide`.

Output, verbatim:

```text
Lean (version 4.36.0, arm64-apple-darwin24.6.0, commit 611c117bfaf7b7ae1cfcf246ce6fba31e8f509e9, Release)
26cf37221eb009f786cfaeb1ccf35ae8a86f4d636f0e9b91dde99196bc078924  GlueNamed.lean
'square_ok' does not depend on any axioms
'square_assoc_ok' does not depend on any axioms
'reject_b' does not depend on any axioms
'reject_d' does not depend on any axioms
exit=0
```

What it checks: the moment-polynomial model of the open 2D square glued from four plaquettes with weight 1 + chi_(1/2)/4 + chi_1/16, in both associations, agrees with the known character coefficients 1, 1/2048, 1/1769472 (as (a + b x + c x^2)/d with x the quaternion scalar part); two corrupted targets (a wrong fundamental coefficient, a zero denominator) are rejected. All four statements are closed by `decide` in the kernel and depend on no axioms.

Negative control (run, not committed): replacing the last statement by the false claim that the corrupted target is accepted makes Lean report an error ("Tactic decide proved that the proposition ... is false").

What it does not check: the Haar sphere-moment identities and Schur orthogonality that connect this integer model to the actual Haar integral are separate proof obligations (row 1418; check 1420). Peak memory of the first run: about 412 MB; wall time about 3 s.
