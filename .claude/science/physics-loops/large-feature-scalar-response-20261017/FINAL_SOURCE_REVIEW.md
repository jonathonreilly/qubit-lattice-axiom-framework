# Focused source review

Disposition: PASS for the stated conditional-support mathematical source. This is not a landing PASS, formal audit, retained-grade certification, or validation of a physical scalar.

Reviewed source: complete new note, complete primary runner, both result JSON files, and the complete large-feature-scalar-response-20261017 pack, including independent checker and preserved failed probe. Base supplied and used: f389e89fe84e2584ee85047f08da88c1443eb163. Source was uncommitted/untracked. Primary note and runner were hashed at entry and have unchanged final hashes below. No repository edits, commits, pushes, or audit actions performed. Methodology reference is the review-loop source at this frozen base; combined integration checks and current-main preservation remain the coordinator's later gates.

## Material findings

No substantive mathematical or physical overclaim requiring a fix was found.

The determinant defines four distinct levels with the stated multiplicities. The strict ordering inequalities select exactly the indexing used by the runner. The q>0 and b+c<0 conditions fix both discrete signs; the latter also keeps the square-root inversion regular. A scalar identity addition and alternative spectral orderings are explicitly excluded. The inverse reconstructs a, then q and r, then the negative b+c branch and the linear b,c solution. I independently differentiated the three-gap map and obtained the stated nonzero Jacobian. Consequently the common positive gap scale gives a common coefficient scale by positive homogeneity; the Bloch construction is linear at all momenta, so the full-momentum identity follows without a minimum-location assumption.

Derivative scope is properly conditional on smooth bands or a smooth degenerate effective matrix. The numerical Hessian implementation uses the mean of the isolated lowest doublet; it should be read as that cluster-average curvature, not a general proof about each eigenbranch at arbitrary degeneracy. At the reference point I additionally probed a generic direction at steps 0.01, 0.001, and 0.0001: the lowest pair remains degenerate to approximately 3e-15. No global minimum or smoothness theorem is asserted. The reference Hessian evidence is numerical and explicitly described as such.

For positive physical length and tick ratios, the gap condition sets A=g/U. Combining the curvature condition g L^2/U=1/A gives L=U/g=1/A. Conversely these equalities give both required scaling relations, and the dispersion substitution p -> p/A follows. This is sufficient only for those stated scaling relations. It supplies neither relativistic dispersion nor the physical dictionary, scalar dynamics, species identities, absolute creation energy, nor source/detector coupling. The note keeps these boundaries explicit and does not misuse the fixed-scale or kinetic-form primitives to derive state-dependent conversion factors.

This is a positive conditional inversion theorem. Its discussion of missing physical bridges is not a quantified global no-go result. No invented failed routes or five-route negative-claim campaign is warranted.

## Independent checks and evidence limits

Executed the primary runner from an exact temporary copy outside the repository: 99/99 controls pass, all three intentionally wrong algebraic alternatives detected, and generated result.json is byte-identical to the submitted result. Independently calculated the Jacobian with SymPy rather than importing a precomputed expression. Manually checked inverse branch, ordering, all-momentum linearity, and finite physical-unit algebra. Reviewed the independently supplied matrix reconstruction and its 100-spectrum/30-full-momentum output; its independence is correctly limited to reconstruction using shared graph definitions, not discovery of the graph. The three primary controls are formula alternatives, not an actual source-mutation campaign, and the note accurately says so. The symbolic check named “all momentum homogeneous Hamiltonian coefficients” operates at the selected momentum, but full-momentum linearity follows directly from the constructor and is separately sampled by the independent checker; this label is not a mathematical gap.

One incidental reviewer hash-inventory command encountered an existing __pycache__ directory after the scientific checks finished. Repeating the inventory over regular files resolved it; no scientific execution failed. The primary reproduction required NumPy/SymPy and completed well within its 120-second limit.

## Source identities (SHA-256)

```text
0cde73a74f65020828cf66a8d6228e378218cd4558f2cd9bb96284ddc45c8b23  .claude/science/physics-loops/large-feature-scalar-response-20261017/ASSUMPTIONS_AND_IMPORTS.md
1aedcdc612c449ebd3b163fecc351cbfb2ea5447afe8154afaddf9f5c584fae5  .claude/science/physics-loops/large-feature-scalar-response-20261017/CLAIM_STATUS_CERTIFICATE.md
ed892222e379645dc777d12941e4308795e5187638f4296fa4f89da69fd89c6c  .claude/science/physics-loops/large-feature-scalar-response-20261017/GOAL.md
708030df1fa6a9b195171e48d8e769bb230ac7f344f86d4a36c84dea62742e27  .claude/science/physics-loops/large-feature-scalar-response-20261017/HANDOFF.md
e0697497ba3345d92037c655ec670b7707c44100e4cfc875d0d9edcfd6ba1ef1  .claude/science/physics-loops/large-feature-scalar-response-20261017/INDEPENDENT_PHYSICAL_SCOPE_REVIEW.md
877ca5aad272fbb251c2b3b621dfd71a425ab832b5fee177291802836ca6db3f  .claude/science/physics-loops/large-feature-scalar-response-20261017/INDEPENDENT_SPECTRUM_REVIEW.md
3bc3bb9185cba20d45ff284a9da837f136b691a34886d29baa6f8705133f94d1  .claude/science/physics-loops/large-feature-scalar-response-20261017/NO_GO_LEDGER.md
4b0b35dda4a9986740f3a3ceac2e33b537087dc3a9d1109e111c88b468107044  .claude/science/physics-loops/large-feature-scalar-response-20261017/OPPORTUNITY_QUEUE.md
64e5828c05e68a8a0c869b90743ed928459f5dd05b88cf26f9fa0934bbbed344  .claude/science/physics-loops/large-feature-scalar-response-20261017/REVIEW_HISTORY.md
75dbb405844d1b8949da4f54f4310bab4a6d593ea7e4ea8cf0b5ff248ec34e9f  .claude/science/physics-loops/large-feature-scalar-response-20261017/ROUTE_PORTFOLIO.md
0264125fcfc974f1ad77be876a0fd8bd1eb3f6c5323d8e1307587c73439caf83  .claude/science/physics-loops/large-feature-scalar-response-20261017/SOURCE_IDENTITIES.json
d745d7561b4f6662eccf0d88df8721be10a7aa86143ad27ab514310702345098  .claude/science/physics-loops/large-feature-scalar-response-20261017/STATE.yaml
526d85b771a13583be13888e8916677bd2d8acbfb89787d8cfb9990b805a7650  .claude/science/physics-loops/large-feature-scalar-response-20261017/TRACE_GATE.md
2eff7a623c98eec18ef3d0b90d61ea2d314b4eee95f6c3482923373c3c0c3666  .claude/science/physics-loops/large-feature-scalar-response-20261017/failed_wrong_valley_probe.py.txt
32080be9201bdb147f1173b0a3eeb6b9d57557c4d129fd6124a1b1934dcf9183  .claude/science/physics-loops/large-feature-scalar-response-20261017/independent_spectrum_check.py
f92d86f8f9a945b9ad95e951a95d3324e9cd246c16bfac65643a7417524fc211  .claude/science/physics-loops/large-feature-scalar-response-20261017/large-feature-spectrum-check.initial-symbol-mismatch.json
a8717ef750d2b27fd751cd3745b175f613e968de7bd25b26ceccbe8c6ffd8303  docs/LARGE_FEATURE_SPECTRAL_RECONSTRUCTION_NOTE_2026-10-17.md
56d142e043d3f212360fd4eee58249487f144558c44dbb3f5cfe67cab13522ce  outputs/large_feature_spectral_response/independent.json
19ed8b4875e5426425dad5bbc69975756a922b94a407e839ff1f069d2402d860  outputs/large_feature_spectral_response/result.json
2050cf84738d979e3f152ffb875583bcc31caf1243fa1600e78ab076558ec10b  scripts/large_feature_spectral_response.py
```
