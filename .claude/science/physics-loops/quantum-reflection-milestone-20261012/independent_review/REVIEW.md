# Independent source review: portable sphere visibility and reflection milestone

Reviewer: `/root/direct_quantum_visibility_review`. Date: 2026-10-12.

**Source readiness: PASS within the explicit mathematical and conditional sampling premises. No materially required source correction remains.** This is independent affected-source review, not formal audit, retained status, combined validation or authorization to land. The parent remains the scientific author.

## Bound source and reading scope

The original constituent is commit `0a2ce9ac6d0d1647c24b54bcb95e23136ff6c0f6`, based directly on `516cb69d8487ff04f8a48e065d3dcbe71d7dd237`, on `codex/quantum-visibility-reflection-20261012`. Its tree is `8069c8dfe91c5ce189373c22c5bbcf90e3e498de`. I independently verified that its delta is exactly the following four paths and that their committed bytes match disk and the reviewed identities.

| Source | SHA-256 |
|---|---|
| `docs/SPHERE_QUANTUM_VISIBILITY_REFLECTION_BOUNDED_THEOREM_NOTE_2026-10-12.md` | `cd2f4f552f3f95b3e91e0ab046f0bf3da2a29f52383f7e920b316afd99d1a3ef` |
| `scripts/sphere_quantum_visibility_reflection_2026_10_12.py` | `cf57773d518b09544dfdb75e0aa91bc8f1a18786d6c895ff2b51955c240482dc` |
| `logs/runner-cache/sphere_quantum_visibility_reflection_2026_10_12.txt` | `6d824ece1241b706f1d62941e7593cad8fead772b08c2c78240525a3ddfecd6a` |
| `docs/audit/data/citation_graph_manifest.json` | `675c43ed9194a86a2b2e8f1417e0d6877b1a9d020a15b4a83fcfd0c9e729d8d6` |

I read the complete portable proof and runner, their evidence, the complete five milestone metadata files, and the affected manifest diff. This review reuses my earlier full visibility and reflection reviews, including an independently implemented exact interval certificate, only for unchanged transferred arguments and arithmetic. The old whole-sphere parameter classification, resource obstruction and finite 300-setting numerical witness are outside this review and are not premises of the portable note. The receipt binds the reused reports and check results explicitly.

## Proof and imported-premise assessment

The realization criterion is correctly quantified for real continuous isotropic kernels, common visibility, measurable binary local observables, one normal state, and separable tensor Hilbert spaces across all settings. Purification and realification give bounded measurable vector maps. The associated integral maps have Hilbert-Schmidt norm at most one; their product is trace class with norm at most one. The spherical eigenvalue multiplicity cancels the Legendre normalization, giving `V sum_l |a_l| <= 1`. Necessity does not assume summability.

The reverse construction preserves the sign of every harmonic coefficient, uses the Bob transpose required by the maximally entangled identity, supplies a fair two-dimensional degree-zero sector and a fair uncorrelated residual sector, and uses one countable direct-sum normal state. Absolute convergence and continuity recover the target for every direction. Infinite local dimension is allowed; finite energy, entropy, entanglement cost or efficient implementation is not established. These limitations are explicit in the note.

The reflection bound correctly uses `I - 2 Pi_3`, with projection kernel `7 P_3`. Its coefficient is 14 and its first term is the actual common-setting correlation. It never infers a diagonal trace from an arbitrary product-L2 kernel. Thus the quantum bound is valid without isotropy or fair marginals. The isotropic expectation is `V[f(1)-2a_3]`; normalization to `V(1-2a_3)` uses the stated endpoint value. The controls distinguish normalized and unnormalized polynomials and correctly give `B(-P_3)=-1`.

The portable candidate, exact parameter and comparison model are supplied assumptions. The exact parameter calibrates a stipulated angle; this is accurately labelled calibration, not an empirical prediction or data fit. No registered framework axiom or primitive is silently imported. The Tsirelson reference is background; the needed vector argument and Clifford construction are given in the source. The bibliographic record was verified from the primary MathNet record; the unavailable PDF was not treated as proof evidence.

## Exact certificate and prospective trial premise

The transfer preserves the exact rational enclosure of k, the `835/18 < 48` second-derivative bound, 2048-panel midpoint error `1331/102760448`, outward interval operations, Taylor domains and remainders. The six inlined arithmetic helper definitions are AST-identical to the versions already reviewed; no original full-sphere theorem is imported with them. Current rational k, a_3 and quadrature-error endpoints exactly equal the previously reviewed certificate. My independently computed interval remains strictly inside the portable a_3 interval.

The certified candidate expectation satisfies `B(-0.95 f_k)>1.0512346868899072`. The value is a continuum mathematical certificate. Numerical quadrature is explicitly a separate floating control; rounded finite settings and a physical apparatus are not covered by this certificate. At V=0.9 this statistic does not decide the full realization question. The critical-visibility formula for a general normalized kernel needs the complete absolute tail, which has not been evaluated for this candidate.

The sampling coefficients, `integral |P_3| = 13/20`, total weight `J=111/20`, and the two branch probabilities are consistent. Correlated joint settings are intentional; the source must be conditionally independent of the fresh joint setting choice, and one local observable map must be used across branches. With conditional range width 2J, the Hoeffding calculation gives the stated quantum error bound even with trial memory. The alternative lower-tail guarantee additionally requires `E[Z_i | past] >= 1+Delta` on every included trial. The final note explicitly states this premise; an unconditional average is insufficient. That is the corrected premise from the earlier reflection R1 review.

The conservative sufficient counts 469373 at V=0.95 and 108502 at V=1 follow from the certified lower gaps and `ln(100)<5`. They are prospective conditional guarantees, not measured power, an apparatus certification, or an optimized sample count. Direction calibration and resolution, source stability, branch independence of observables, detection and included-trial definitions remain physical obligations.

## Code, evidence and source closure

The runner is self-contained scientific code. Its only imports are Python standard libraries, mpmath, NumPy and SciPy's `roots_legendre`. It neither imports another repository science module nor reads scientific data, a campaign file or a runtime result. Its paired note is a literal declared integrity input, and its declared timeout is 120 seconds. The note's local links resolve to the runner and canonical cache. There are no repository proof parents, supporting proof fragments or scientific helper runners.

The transfer comparator in this review directory additionally reads pinned originating-campaign evidence to establish continuity. Those absolute provenance reads belong to this review, not to the portable scientific runner. Their identities are bound in the receipt; a checkout lacking that old local evidence can run the primary portable runner but cannot replay the complete provenance comparison from the comparator alone.

I independently executed the exact final runner in JSON mode: nine families passed, zero failed. The canonical cache was unchanged. The repository cache API reported it fresh with note fingerprint `2fdfe9fb317e3036e24e4c3aa7b10887c2c587fb4be7369a20c9fec101008ac4`; raw v2 stdout equals the cached stdout. The freeze v2 hash is `24889d899e7fb73c0a45e72212644b5000f47d2b418551b48bcc06467260f8d1`.

Independent controls include exact polynomial expectations `1, -1, 9/8, 15/16`, the harmonic integrals, derivative-bound arithmetic, candidate calibration and the prior independent interval inclusion. The checked author mutation record contains nine nonzero exits, each with its intended family failure. Its tested source differs from the current runner by only one removed terminal blank line, verified by hashing current source plus one newline. I inspected this evidence rather than rerunning identical mutations. The initially wrong expected sign for `C=-P_3` was corrected before source freeze; no observed failure was hidden or relabelled.

Focused report-only vocabulary checking found zero violations in the note and five metadata files. Working, staged and base-relative whitespace checks passed. No full pipeline, strict integration, formal audit, source edits, commits, pushes or landing were performed by this reviewer.

## Governance and applicability

The current repository review-loop instructions were used after detecting the installed skill's older copy; the pinned repository entry is recorded in the receipt. Conditional-support status, explicit imports, trace classification and absence of premise adoption are honest. The documented conformance/status wording discrepancy does not justify promoting a conditional source to retained status. The five packet files are process/claim-boundary records, not additional mathematical premises. Their pending-review statements reflect their captured pre-report state; the coordinator may add a later evidence-only update without rewriting this report.

The no-go discipline packet is **not applicable** to this artifact's actual claim. This is a proved realization criterion and a prospective bounded statistic, not a failed-search inference, assertion of framework route exhaustion, or universal physical reconstruction wall. The current actual gate returns false for artifact classification, negative-boundary rhetoric and requirement in both development and forensic modes. No N1-N8 mechanism quota was invented.

One portability wording issue was closed: the generic statement about a finite subset not determining a reciprocal was replaced by the precise positive obligation to control the full absolute tail. That removes an unrelated rhetoric-trigger ambiguity and accurately states the mathematics. The runner, certificate and sampling protocol were unchanged; old source/cache evidence remains preserved. No other source correction is required.

The manifest has exactly one added zero-dependency node, `sphere_quantum_visibility_reflection_bounded_theorem_note_2026-10-12`. Every previous node entry is unchanged and its edge count remains 15,805. I checked this diff and parsed comparison; I did not run a second graph build or combined pipeline. The four original paths are preserved at the committed identities in `REVIEW_RECEIPT_v1.json`.

## Disposition

The four-file constituent is ready to proceed to the parent's combined validation under the stated source verdict. The evidence does not establish a measured quantum violation, a realized alternative angular law, a finite-resource implementation, a framework axiom adoption, full candidate-tail classification or a TOE. Reviewable packaging and integration checks remain the coordinator's responsibility. This report grants neither retained status nor authority to land science.
