# Refuting pass — block 16 (supervisor-run, disjoint machinery; 2026-09-15)

Routes compared (control `specs/supervisor_control_block16_flip_monotonicity.py`, refuting pass `specs/supervisor_control_block16_refuter.py`, outputs in `.out.txt`):

| item | runner's route | refuting route | result |
|---|---|---|---|
| the flip lemma (X1) | the weight formula `M^{−n_0} Π 1/K_{|A_x|}` per order (per class on the cube) | the ratio `μ_σ/Π K` from the product of conditionals directly, at the constant pattern and each flip, on every class of the plaquette, `2×3` and the cube; the control checked all `322,560` order–site pairs of the cube by the weight formula | equal; strictness on exactly the predicted pairs |
| the qualifying orders (X2) | the union of recorded sets of size `≥ 2` | a direct search for a site with two recorded neighbours at formation time, on every order of the path and the star | agree |
| the `2×3` uniform mixture (X2) | mixture by classes | the census runner's own pinned cache (decimal to twelve digits) | match |
| the environment claim (X3) | exact laws and mixtures | by hand on the domino in the all-`+x` environment: the second site's normalizer `K_6(first, five outside +x)` is `493/1492992` at `first = +x` and `251/1492992` at `first = −x` | differ, as the lemma predicts |

Findings: none in the primary. Two scope notes recorded in the fold: the cube's runner check is per class (the control covered every order); X3 is stated for constant environments because the flip's monotonicity needs every other member of a recorded set to carry the flipped site's original value.

Attempts to refute (nothing refuted): X1 was re-read for a site `z` that belongs to the recorded sets of several later sites — each factor moves the same way, so the product moves strictly; for the flipped site's own factor `K_{|A_z|}(v_{A_z})`, which does not contain `v_z`; and for `p = q`, where the orthogonal flip replaces the antipodal one with the second form of the lemma. X2's "only if" was re-read for mixtures with zero weight on some classes (the sum is over charged orders only, and each is forced individually). Verdict of this pass: PASS-NO-BLOCKER at the supervisor's own standard, pending the owner's independent review.
