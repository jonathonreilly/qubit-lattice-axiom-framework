# PR8169 original independent review

Head `7e268bd96edda8819250318a3cbdaa1b20e90f35`; actual merge base `6dda46fc1af02827e9c6b64b2f7d05c381a3ce07`; committed authority/current main `631d6b36cd1e9b860763ebcad36e40a2bbe7439c`.

**FIX REQUIRED.** Original proof framing fails at symmetry, support and joint-law steps. Several exact identities survive; the order obstruction has a short corrected conditional proof. Formal negative packet FAIL is separate from mathematical validity. No audit verdict or landing PASS.

## Material findings

### 8169-F1 — State the complete input symmetry before copy/flip classification
Original note lines [154, 166]. The bisector rotation exchanges ordered records. Internal SO(3) alone permits masses (1/2,1/4,1/8,1/8) on (q,qprime,-q,-qprime). The parent also supplies independent cubic slot permutations; an explicit slot exchange can repair the argument.

Narrow repair: State unordered pair or the two occupied slots and their cubic exchange; combine slot swap and internal bisector to stabilize the complete input. At fixed occupancy geometry, orbit t classifies the pair. Distinguish opposite versus adjacent slot strata if both are included.

### 8169-F2 — Finite menu is not always probability support
Original note lines [29, 33, 196, 206]. delta_q is a covariant normalized one-neighbor finite law. Finite SO(2)-invariant support is a nonempty subset of {q,-q}. For copy/flip weights alpha=1/2,gamma=0, the four-point menu has support size2, not4. Current axiom memo explicitly defines finite support by nonzero mass.

Narrow repair: Use menu for all four candidate points; actual support4 requires alpha,gamma>0. State singleton/pair one-neighbor possibilities. Preserve boundary cases and replace deterministic copy wording by uniform choice between the two copy atoms where appropriate.

### 8169-F3 — Linear family needs parameter domain and functional qualification
Original note lines [177, 181]. At t=3/5, lambda=1 gives flip mass -3/20. Arbitrary alpha(t) corresponds to lambda(t)=(4alpha(t)-1)/(1+t), with |lambda(t)|(1+t)<=1. Fixed lambda is not every t-dependent law. Finite beta Gibbs gives strictly positive weights, approaching endpoints only in limits.

Narrow repair: Supply the domain -1<t<1, parameter bound, pointwise/function interpretation, and Gibbs limits. Rename runner beta argument as B at t=0 or implement/restrict it honestly; current gibbs_copy_mass silently deletes t.

### 8169-F4 — Replace conditional-cardinality comparison by a joint-event proof
Original note lines [194, 206]. Chain endpoints q and qprime noncollinear are unreachable when all one-neighbor draws lie on the preceding axis. Conditional menus at that configuration do not alone establish different joint measures. However the intended negative result is repairable: E={|L dot R|<1} has probability0 in chain and1 under independent Haar ends-first roots.

Narrow repair: State supplied sequential product kernel, independent empty-neighbor draws, Haar sphere domain, and finite antipodal-supported one-neighbor law. Prove the endpoint event separation, including zero-weight cases. Retain original2-vs4 geometry only as a menu illustration; do not discard the negative theorem.

### 8169-F5 — Keep raw Born normalization identity; remove unsupported variation inference
Original note lines [184, 192, 247, 248]. Raw overlap values sum to2 for every noncollinear pair. Once divided by2, the law is normalized, depends on qprime through moving atoms and t, and is internally SO(3)-covariant though not exchange-symmetric. The runner D2 only compares two overlap values and does not test variation. Born about normalized bisector also sums to2 before a factor1/2.

Narrow repair: Separate raw two-outcome overlap from a four-effect/normalized menu law. Preserve sum2 and normalized asymmetric counterexample. Do not infer failure of the framework variation clause from absence of qprime as a literal formula parameter; label exchange failure under the explicitly supplied exchange symmetry.

### 8169-F6 — Negative packet is incomplete independently of valid mathematics
Original note lines [238, 290]. N1 lists4 routes, lacks required honesty markers; N2 asserts independence without nonimplication witnesses; N3 misses symmetry/positivity/product hypotheses; N5 has no five stdout resolution lines; N7 dismisses triviality instead of testing a concrete counterroute; N8 has no demonstrated prior-scope search.

Narrow repair: Preserve four actual routes and their exact dispositions; do not invent a fifth. Correct mathematical claim scope, record formal negative-certification FAIL/deferred explicitly, and preserve negative proofs and recovery. Honest N5 lines can be added, but do not claim packet PASS until the actual contract is satisfied.

### 8169-F7 — Remove live PR-local authority language and strengthen evidence
Original note lines [75, 83, 126, 138, 217, 218]. Open sibling PR8152 is explicitly not a premise, but live prose/runner F3 requires its PR number. Runner C1 verifies only chosen normalized pairs, not covariance classification; E3 verifies menu lengths, not joint law. Cache reports21 PASS but misses these decisive gaps and all N5 lines.

Narrow repair: Keep source at canonical note/runner paths; historical sibling mention belongs in recovery history. Add decisive symmetry, parameter-bound, support, and joint-event controls. Refresh final cache only on frozen final source/actual inputs, with bounded execution and mutation controls; regenerate topology on integration rather than copying stale manifest.

## Exact proof recovery

For noncollinear ordered pairs, the SO(3) stabilizer is trivial and t is the orbit invariant, so four normalized nonnegative functions are possible. Add exchange symmetry to obtain alpha(t),alpha(t),gamma(t),gamma(t). Equivalently combine a slot exchange with the internal bisector rotation. The parent explicitly supplies independent slot and internal actions. This is conditional mathematics, not an axiom-selected probability rule.

For every noncollinear pair, the raw overlaps sum to2 by antipodal cancellation. The symmetric linear family has lambda(t)=(4alpha(t)-1)/(1+t), with |lambda(t)|(1+t)<=1. Finite beta Gibbs has alpha/gamma=exp(2beta(1+t)), and B=2,t=0 gives1/3 and1/6. Copy/flip endpoints are two-atom distributions, not deterministic single records.

For the supplied sequential product model, every chain draw after the first lies on the same unoriented axis: endpoints are collinear with probability1. Ends-first roots are independent Haar sphere draws, so endpoint noncollinearity has probability1. That measurable event separates joint laws regardless of later two-neighbor weights; the original2-vs4 conditional-menu check does not establish this alone.

## Provenance, disposition and validation

All8 original paths, modes, Git blobs and SHA256 hashes are frozen in drain8169-inventory.json; complete original/current-main recovery and claim dispositions are in drain8169-review-original.json. Original source is in drain8169-originals. No original deletions. Both actual premise blobs are identical at base/head/main. Seven added paths are absent on frozen main; the existing topology manifest must be regenerated without losing main content. Final-candidate loss/interactions remain due.

check8169.py/json records18 independent bounded checks. Original primary not rerun; original21-PASS cache preserved as historical output, not decisive proof. No pipeline, audit worker, source mutation, commit, PR mutation or landing performed. Final primary mutation controls and combined gate remain due after repair.

Failures: python alias absent (recovered with python3); oversized reverse-side diff/governance displays truncated (correct inventory and targeted sources read thereafter); initial shard parser assumed wrapper (recovered by exact shard read).

The source report carries all import classifications, actual inputs, frozen authority hashes, N1–N8 dispositions, and complete recovery mapping. This session remains the original reviewer for cold/final affected-fix confirmation.
