# M11 canonical mathematics/source correspondence, v1

This is a focused post-exposure consistency check, not a formal audit, publication approval or new scientific authorship. Root remains author. Both canonical files were copied and hashed before semantic reading, and the copied bytes remain immutable. I read the complete 421-line canonical note and complete 210-line geometry/helper source, including all 26 control records as written. I did not execute the helper or aggregate, inspect raw observations, or verify the other evolving source tests and cache.

| Complete read | SHA256 | Bytes |
| --- | --- | ---: |
| CASSINI_ERROR_DIRECTION_MODEL_BOUNDED_THEOREM_NOTE_2026-10-15.md | 7e4072642e778ee1295e2219d247795641a409315ca159690cca5a9ce56ac9e8 | 24804 |
| cassini_error_direction.py | c9b1e47cbaeaa8faf31543541e983c19f23a4e4d1fdfebae88e1e0590843e7aa | 9491 |

`CANONICAL_SOURCE_FREEZE_v1.json` carries full source and snapshot paths. The independent pre-author proof/report remains de40057de817a745e52beebb6a162802ff4215b862932ef5b7bad818f8a8f811; its 51 controls were executed before author-source exposure. The separate working-source correspondence remains 5f970aec3bb5ceb5495ddea8e1bdd01f277be7ed283ec2ed63ebc142bb2a1105. Those historical results are unchanged and are not relabeled as a fresh canonical execution.

## Mathematical correspondence

The canonical angular-law/F derivation, cone distance, quantizer-safe frequency region and translated amplitude disk agree with the frozen independent proof. The note now explicitly states finite positive fs, integer N>=3, finite nonnegative q, interior tail probabilities, and positive color ranks; it excludes N=3 or4 from the color extension. Exact rank-one carrier cases accept without a ratio. Zero signal is allowed, positive error radius is required for the exact distribution, and no physical noise-energy upper bound is inferred. Conditional uniform direction remains stronger than equal covariance and is not supplied by Gaussian-looking histograms, filter labels, bandwidth or fitted tone fraction.

The fixed-true-f tests have the stated conditional coverage. Their inversion needs no continuum multiplicity correction to cover that one true parameter. The frequency/amplitude construction uses a valid conservative union bound; optional nested unquantized independence is not transferred to the carrier/color statistics. The three direction allocations sum to alpha_record, and the fixed-record family allocation is a further union bound with no asserted record independence. The internal training split does not turn data already used for model development into an independent empirical confidence experiment. That qualification is explicit in the mathematical section, observation discussion, proof obligations and final status block.

The ball-versus-cell distinction is retained: Euclidean ball intersection is exact, but it only gives a conservative enlargement of the actual ADC box. q describes a separately supplied ideal unsaturated quantizer enclosure; other error remains epsilon. The amplitude disk contains the essential q*sqrt(1+tau_c²)/sqrt(N) term. Phase interpretation still requires excluding zero and preserving the amplitude's time-origin/frequency-representative convention. This is inherent in the supplied u_f; no absolute phase or unwrap history is derived.

The global carrier/color argument also matches the earlier proof. It uses the weaker valid lower bound ||Az|| >= (R-k)_+*||z||, the Dirichlet upper bound on a genuine uniform grid, a strict far margin and a midpoint covering with Lipschitz/ADC allowances. The outer arc contains all possible carrier acceptance in exact arithmetic. Either tail may reject an entire cell; every cell must be rejected for an empty joint set. Rank-degenerate, zero-vector and uninformative outer-arc cases are not silently forced into an exclusion. The actual numerical implementation is explicitly diagnostic, and the note does not turn the .999 real-arithmetic margin into an outward-rounded certificate.

The added explanatory FIR equation is consistent: for y_n=sum_k h_k x_(nD-k) with white input, E[y_n conjugate(y_m)] is proportional to sum_k h_k conjugate(h_(k+(m-n)D)). The two-tap example has adjacent covariance1/2 and shares an input across contiguous output halves. It is a counterexample to an unsupported independence substitution, not a recovered Cassini transfer function. The direction/covariance dependency table correctly allows direction-dependent radial laws, for which uniform direction need not imply equal covariance or finite covariance at all. The no-go section does not count a universal scalar obstruction or exhaustion of calibration routes.

## Source adaptation and the four added controls

An AST comparison confirms that all ten production functions are unchanged from the fully reviewed working helper. The docstring and timeout metadata changed; `controls` adds four records. `CANONICAL_ADAPTATION_CHECK_v1.json` and `CANONICAL_GEOMETRY_DIFF_v1.patch` preserve this comparison without executing author code.

The four new fixtures are consistent with the proof:

- The global Dirichlet fixture checks a useful arc, verifies its analytic overlap upper bound lies below m, and checks a finite set of outside-arc candidates. This supplements the theorem; finite samples alone are not a continuum proof.
- The adversarial radial perturbation moves by q in the outward cone-normal direction, giving exact real-arithmetic distance q. Its B norm remains positive for the supplied fixture.
- The carrier ADC fixture uses three orthogonal DFT modes. The A norm is tau*b+q*sqrt(1+tau²), the B norm is b, and q=0 rejects while the enlarged ball reaches the boundary. The added floating tolerance is an execution tolerance, not part of the analytic theorem.
- The amplitude fixture has z=chat*sqrt(N)*u0+b*u1 and c_true=chat+radius. For a=sqrt(N)*radius, the analog perturbation uses -a'*u0+b'*u1 with the proved closest radial norms. Its distance to z is q and it attains the unquantized amplitude cone. The signs, sqrt(N) normalization and residual direction are correct.

There are 26 control records by source inspection, compared with22 in the working helper. I do not assert a new canonical pass count from this read-only comparison. The existing independent exact orientation witness remains separate evidence. The helper still trusts several caller domains rather than acting as a hardened public API; the declared fixed-domain use is the scope of this review.

## Finding, disposition and limits

One narrow wording finding was retained in `CANONICAL_FINDING_v1.json`: the copied note's lines340–342 call the finite decimal0.3518716581 an “exact false-rejection probability.” The inclusion-exclusion probability expression is analytic/exact under the stated synthetic model, but its printed finite decimal is an ordinary floating evaluation. The requested repair is “analytic false-rejection probability approximately 0.3518716581,” or an exact expression separated from its approximate value. This is not a formula discrepancy and requires no scientific rerun. Root has reported making this wording repair; a separate affected-byte confirmation will bind the replacement source without changing this original review.

No other substantive mathematical discrepancy was found within the reviewed domains. I read but did not empirically substantiate the note's decoded settings, sample identities, correlations, exclusion counts, independent-decoder/quantile replication, tolerance-failure receipts, source-document semantics, registry checks, or cache/runner claims. Those remain the responsibility of their separately scoped evidence. This review checks the mathematical meaning and appropriately bounded presentation of those statements, not their observational truth.

The canonical surface preserves the relevant boundary: radial-scale elimination is conditional on a new direction premise; its physical suitability remains unproved and is challenged on exposed development data. A failure cannot isolate noise color, choose a receiver mean, produce a scalar-force observation or retire action/initial-state/scale/environment assumptions. No canonical file, state, index, branch or publication artifact was modified by this checker.
