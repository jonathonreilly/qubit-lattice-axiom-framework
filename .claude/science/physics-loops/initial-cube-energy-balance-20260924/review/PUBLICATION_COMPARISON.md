# Milestone 11: final released-source publication comparison

No material mathematical or source/evidence discrepancy was found in the released publication. No correction is requested. This is a final comparison with the preserved PRE and POST, including a check of the newly released root density addendum. It is not a new blind derivation, a recertification of transitive parents, or an audit/retention verdict.

The complete new note, adapted primary source, and matched-density addendum were read. The affected hypotheses in the published full-ensemble parent were checked against the previously imported full-ensemble PRE: the uniform low-source convergence on `[0,T]`, graded high-source orders, all-age tail estimate, and Hermitian first-high coordinate remainder agree in scope. The existing PRE and POST remain unchanged.

## Sources and inherited scope

The publication worktree is `initial-energy-balance-publication`, at base `28965d2737ee32b01bba972273fa51d399c594e4`. The four new public files were untracked at verification; this review binds their bytes, not a later commit or landing. The exact reviewed identities are:

| Source/evidence | SHA256 |
|---|---|
| `docs/INITIAL_CUBE_ENERGY_LAYER_AND_EXACT_BAND_BALANCE_BOUNDED_THEOREM_NOTE_2026-09-24.md` | `e9d858a9a4c456c42496159c0ec75ce085957641870dc98cdb8cd69aed04629c` |
| `scripts/initial_cube_energy_layer_and_exact_band_balance_2026_09_24.py` | `3acb32fac4d5de45177fab8b7ca728545e733a1eb44ce7d6ab2778c5c28da34a` |
| `outputs/initial_cube_energy_balance_20260924/INITIAL_CUBE_ENERGY_BALANCE_RESULTS.json` | `91ecd9d08bb13d30a172be2b72b5eecdb7023c1c70aecb333cd72faa31e569e8` |
| `logs/runner-cache/initial_cube_energy_layer_and_exact_band_balance_2026_09_24.txt` | `a2ff8beb93dbb4f762cda3e69af5de05f21e053bcc21a0cb4cc2dda5f6b9f6f3` |
| Root `MATCHED_DENSITY_ROOT_ADDENDUM.md` | `663c2b5f5961e5bc10d8c1e268bd4dd49f8b56be65d74ca1e41d146fcdd279cb` |
| Root `MATCHED_DENSITY_SEAL.json` | `41b9c52af4702d0d5e77d36ef6ae5a9fdeacfd60b87826b45f6344296fec0849` |

The preserved comparison anchors are PRE `785f3c87cec7db2d00f2548745b22fd68e74afa09a307081446fc80763555b3a`, PRE seal `f459870253083462c9448a0f1ca2ea50beb9b954b34bdffd783fe27a08f060f8`, POST `1b8a71eedd1d014e22b23a87e7658cd01fd0645f932b8292dce08ddc645c42c4`, and POST seal `0c13e98f9aed198fa3079179d8fe03e288c61fa7035aad4e2e824482f7d64075`. All 19 PRE members and all three POST members were rehashed and matched. The original root author/control seals and the new one-member addendum seal also matched.

The claims keep the original compensated lambda-zero model, canonical Hermitian zero-field N=4 preparation, fixed positive delta, K and kappa, fixed finite physical horizon T, and joint integer-spin scaling `epsilon^2 S(S+1)=delta/K`. The complete original resolved or coherent instrument is retained. The full-ensemble parent remains an explicit provisional mathematical dependency; the current comparison does not reopen its entire proof or its independent history.

## New matched-density extension

Section 8 and the root addendum correctly extend the previous positive-time trace-density statement to a uniform matched statement on `[0,T]`. With the raw-mark first-high Hermitian coordinate `y_i,e,1(t,s)`, set

```
f_i,e(t,tau) = epsilon^-2 exp(i delta tau/epsilon^2)
               y_i,e,1(t,t-epsilon^2 tau),
g_i,e(t,tau) = exp(tau L) R_i u4(t),
```

and set both profiles to zero outside `0<=tau<=t/epsilon^2`. This common cutoff is essential. The exact prefactor and change of variables give

```
epsilon^-4 U1,e* rho6,e(t) U1,e
  = kappa sum_i integral |f_i,e(t,tau)><f_i,e(t,tau)| d tau.
```

The inherited coordinate remainder is `O(epsilon^4)`, hence `O(epsilon^2)` in the profile; its squared age integral is `O(epsilon^2)` over the longest interval `T/epsilon^2`. The principal exact profile has uniform squared tail bound `C_T(1+R)^(-3/2)+C_T epsilon^(1/2)` over the entire physical-time triangle. The truncated rotor profile has the corresponding integrable tail. On bounded ages the strong source and bounded-generator convergence, together with uniform continuity of `u4`, are uniform on `epsilon^2 tau<=t<=T`, including zero. Splitting the age integral at R, taking epsilon to zero and then R to infinity therefore yields uniform convergence in the direct-sum age L2 norm. No convergence rate for the evolving low source is assumed.

The integrated rank-one estimate

```
|| integral (|f><f|-|g><g|) ||_1
  <= ||f-g||_L2 (||f||_L2+||g||_L2)
```

then proves the stated trace-norm comparison with `Sigma_tr,e(t)`. This is a vector argument, not an inference from norm-squared convergence alone. The constants and finite source sum are controlled by the stated parent hypotheses.

The density matching criterion is also supported. Removing the truncated tail uniformly on `[a_e,T]` is valid if `a_e/epsilon^2` tends to infinity. Conversely, if this ratio does not tend to infinity, take a bounded-ratio subsequence and a further subsequence with ratio tending to a finite tau. At `t=a_e`, continuity of the frozen source and the initial-layer formula leave the positive tail

```
Sigma(0) - Sigma_init(tau),
```

whose trace norm is its trace, `kappa [I(0)-J(tau)]>0`. The nonzero source and bounded generator prevent its orbit from vanishing at a finite age. The uniform approximation error cannot remove that gap. Thus the stated if-and-only-if criterion is justified in the absolute trace-norm sense. No relative estimate on faster clocks, unbounded-observable consequence, or other density block limit follows automatically.

This extension is explicitly post-PRE root work combining the attributed PRE scalar matching argument and the POST vector-density argument. The publication preserves that chronology.

## Moment and balance scope

The scalar matched mean, second moment and variance statements agree with PRE, including the compact initial `t=epsilon^2 tau` profile, the moving-lower-endpoint criterion, and the initial derivative `72 kappa delta epsilon^-2+O(1)`. The zero-field constant `E0=-84 delta`, source norm sum 72, and cubic onset underlying `J(tau)=72 tau-144 kappa delta^2 tau^4+O(tau^5)` agree with the primitive-word calculation and its normalization. These remain PRE-attributed additions.

The publication distinguishes the Hermitian energy and band observable from the exact no-event generator. Its exact net drift and exact band balance retain the full anticommutator, including interband coherences. The mean convergence yields the stated distributional drift against C1 test functions, with the initial boundary atom. The note does not upgrade that conclusion to pointwise drift convergence, a total-variation bound, or weak convergence against every continuous test.

The scaled first-high gain limit is uniform under its stated hypotheses. The positive diagonal carrier uses the Hermitian first-high density and the compressed positive loss. Strong convergence of its uniformly bounded loss operator can be paired with the trace-class limit using finite-rank approximation and compactness of the limiting source orbit. The frozen-age balance gives `Tr(Gamma1 Sigma)=72 exp(-48 kappa t)`, with all kappa and delta factors accounted for. The exact diagonal energy-loss correction is `O(1)`; the off-diagonal coherent terms are not discarded. Only the stated integral/distributional conclusion is asserted for the exact loss. The closing sentence now names the gain and diagonal carrier as positive and separately identifies the exact coherent-loss limit. This resolves the POST presentation finding.

The result concerns net system energy and an identified positive carrier. It does not identify a reservoir, heat, work, implementation cost, apparatus resources, or Fisher information from mixed variance. No additional energy or apparatus derivation was undertaken for this comparison.

## Adapted controls and execution bindings

The complete public primary was inspected. Each of the six PRE primitive functions (`legal`, `combine`, `hop`, `mark`, `norm2`, `primitive_words`) and each of the three root cascade functions (`phi_laplace`, `mean`, `controls`) is identical in source text and AST to its sealed origin. The four primitive global definitions also have identical ASTs. The wrapper correctly combines the two payloads, records their source hashes and its own hash, writes the declared result, and prints the summary. It does not contain or run the PRE four-level toy. The original primitive payload's description of a new calculation refers to its disclosed PRE origin; this publication rerun does not create new independence.

All 36 primitive rows and the entire primitive payload equal the preserved PRE result. All 25 cascade initial rows, 15 physical-flow rows, five distribution rows, parameters and loss counterexample equal the sealed root result exactly after removing only the original wrapper's `elapsed_seconds` and `source_sha256`. Complete structured equality reuses the previous full row inspection; no truncated output was treated as verification. These controls check their exact finite algebra or separate cascade model, not the cube joint-limit theorem numerically.

All seven declared inputs were read and hashed in their exact order. Six transitive inputs equal the committed base bytes; five also equal the PRE snapshots. The remaining published full-ensemble parent has SHA `b2fe61b2a821fea5cc99e4e87b2d28536673a10cab5c2bed5b51daffa6cc2d9d`, as cited by the addendum. The recomputed fingerprint is `e69945c2ed29c1e45d80532e6645281408194e8a25ac50253d7d6b1f1cfbd6c7` and matches the cache.

The external frozen-source receipt, completed execution receipt and root verification receipt all match the actual files. The entire canonical cache was reconstructed byte-for-byte from the actual identities and recorded execution. The complete 26,012-character stdout is exactly the result JSON followed by `TOTAL: PASS=2 FAIL=0`. The API records exit 0 and elapsed time `0.19647526741027832` seconds. Its separate stderr field is empty; because the API merges child stderr into stdout, the narrower verified statement is that the full merged stream contains no additional diagnostic text. This review did not rerun a primary or any physics control.

`PUBLICATION_SOURCE_PINS.json` records all 49 checked source/evidence identities. `PUBLICATION_VERIFICATION.json`, the bookkeeping script and its full stdout/stderr/execution record preserve the mechanical comparison. No previous sealed file, publication file, retained/audit state, or other active checker packet was changed or opened beyond the expressly released comparison scope.
