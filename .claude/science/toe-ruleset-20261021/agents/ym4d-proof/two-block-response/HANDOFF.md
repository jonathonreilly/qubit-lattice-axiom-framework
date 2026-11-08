# SU(2) two-block response checkpoint

Author proof milestone, 2026-11-08. This is the current recovery record for
the user-requested continuation of #10133, not an audit or a mass-gap result.

## Target and source identity

Derive the exact finite-volume two-region conditional response for the actual
normalized S4-prime soft kernel, including two fine sources, exterior changes,
source-only normalizers and conditional covariance. Work out the adjacent
two-plaquette shared-link moment explicitly, then attempt the spatial estimate
needed by CW-entry-SU2. Completion of an identity alone does not establish
cutoff-uniform crossover at fixed positive physical scale.

- Scientific base: PR #10133, `89faef229ff6e6bde42baad15ed8270c2f4087d8`.
- Governance/prior-art main: `43a1fcc374711ca50626eca667441d3ca575c7d1`.
- Working branch: `physics-loop/su2-two-block-response-20261108`.
- Accepted mathematical model: finite four-dimensional Wilson SU(2), normalized
  Haar, finite real beta and lambda, the supplied S4-prime path means. These
  are explicit model premises; this task does not derive them from the ontology.
- No gauge fixing, small-field restriction, continuum limit, selected history,
  computer-assisted proof, new axiom or primitive is a proof input.
- Runtime: bounded interactive task, not an unattended campaign.

## Completed argument and claim boundary

1. Disintegrate the actual joint fine/coarse measure over two coarse regions
   and their fixed exterior. Keep the exterior source partition separately.
2. Differentiate its complete integrated weight. Two source derivatives give
   a conditional covariance; boundary derivatives give third/fourth cumulants.
3. For adjacent coarse plaquettes, integrate the shared link using its second
   SU(2) moment; test the product-of-means replacement on the same expression.
4. Express mixed boundary log ratios as posterior covariances. Reuse the
   existing comparison argument, with the soft-kernel normalizers included.
5. Prove an explicit volume-uniform spatial bound in the sufficient domain
   q+8s_L lambda^2<1, with s_L=(8L-7)L^3 and
   q=18beta+8(s_L-1)(lambda+lambda^2/4). This is a one-step endpoint estimate.

The primary `../SU2_TWO_BLOCK_BOUNDARY_RESPONSE.md` contains all five parts.
In the adjacent pair, the shared-link conditional covariance contains
lambda^6 w(A_M B_M)/4^7+O(lambda^8), before the product of conditional means.
Its exterior response has both a third cumulant of means and the covariance
of the shared-link term with the boundary insertion. These are explicit
finite-model results. The physical crossover theorem remains open.

Luna performed bounded repo reads. Two inherited-model workers requested at
medium reasoning wrote source and estimate drafts, as expressly authorized by the
user. The supervising selected model retains mathematical judgment and final
review. A fresh inherited-model context independently derived the shared-link
moment; another rechecked the full argument by a semigroup route. Workers
wrote disjoint durable drafts outside this checkout. This is same-provider research checking,
not formal independent review or audit.

## Prior work and checks already performed

Luna found the rectangular covariance identity and a small-beta slab comparison
in `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, equations (14)-(18). They are prior machinery,
not discoveries of this continuation. `MASS_GAP_CONSTRUCTION_ASTRA.md`, section
2, supplies the normalized SU(2) kernel and disjoint-loop transport. Its
repeated-link warning is directly relevant here. A fresh main search and the
bounded Luna inventory are preserved in the local research evidence folder.

The literature search located Patrick Rebeschini and Ramon van Handel,
*Comparison Theorems for Gibbs Measures* (2014), arXiv:1308.4117. This credits
comparison machinery; a finite-product proof was checked directly. No
unread published theorem is assumed to establish the crossover estimate.

Preflight passed disk, memory, load and origin connectivity. The inherited
branch has no `scripts/lab_ops.py`; the pinned current-main snapshot was used.
No target-specific model floor was checked by that script; the user's explicit
worker-effort instruction governs the scoped writing jobs.

## Checks, delivery and next decision

The primary and both worker drafts were read in full. The shared-edge
character proof and the full-proof check are included; exact revisions and
check limits are in `REVIEW_HISTORY.md`, `SOURCE_MANIFEST.json` and
`FULL_PROOF_CHECK.md`. The primary final SHA256 is
`934b10582986d3d484e158af2913050d872788d1ee3171720abe3e37daa1073c`.

The next theorem is an all-boundary, summable connected-insertion estimate for
the actual normalized hidden chain along the weak-coupling Wilson trajectory,
uniform in cutoff and volume after reaching a fixed positive physical scale.
It must retain the conditional covariance and its higher source responses.
The posterior-Dobrushin route is sufficient and may be stronger than the
coarse contraction target; obtaining its exact covariance representation is
not itself progress on those physical-scale quantifiers. Multi-step identities
are proved, while the quantitative estimate is one-step. No failed attempt is
presented as route exhaustion, and the original crossover target is unchanged.

Proposed delivery is a regular PR stacked on `ym/crossover-reduction`, whose
head remains `89faef229ff6e6bde42baad15ed8270c2f4087d8` and whose PR #10133
is still draft. It cannot be treated as an independently landed base. Current
`SCIENCE_WORKFLOW.md` section 10 requires owner approval of exact text for
public claims. The repository is public; the proof and prepared PR text are
ready locally for that approval. No external post, merge or audit action has
been performed as part of this checkpoint.

No files containing editable instructions or prompts have been changed.
