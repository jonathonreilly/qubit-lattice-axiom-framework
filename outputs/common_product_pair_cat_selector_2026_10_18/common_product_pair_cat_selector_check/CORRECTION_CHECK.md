# Narrow branch-terminology correction check

Disposition: CONFIRMED. Inspected the complete exact diff, without rerunning the unchanged proof.

The preserved `common_product_pair_cat_selector/AUTHOR_PROPOSAL_V1.md` hashes to `ab95fdeab0146d06ba04177cae215ad577909cba9eb2fc2a826ca6177c43df2d`, exactly the source reviewed in REVIEW.md (`0f7cd6b14562fbf50985ccb0aa1f53d1c642add92aa24fc0d1c1a90723980811`). The corrected `common_product_pair_cat_selector/PROPOSAL.md` hashes to `8f0545c498bf6e6b4796e2c47fffedead122d3fdec0fb45607b853650e3b6a71`.

There are two diff hunks: the whole-horizon paragraph now explicitly bounds the record-1 branch-comparison error ||P_R1 U E-V(t)|| against the same unnormalized parent target, and explicitly excludes an amplitude bound on ||P_R1 U E||; an appended revision qualification records this change and the preserved original hash. This implements the review's terminology qualification correctly. All existing numerical bounds, assumptions, spectral and resource formulas remain unchanged. The displayed comparison formula spells out the already reviewed meaning rather than introducing a new theorem.

The original SUPPORT disposition therefore applies to this corrected source with that ambiguity resolved. The original review's exposure, ancestry and preparation/runtime limits remain in force. This was an exact-diff check only; no full proof rerun, scientific execution, source edit, Git or checkpoint change occurred. Only this correction-check file was created.
