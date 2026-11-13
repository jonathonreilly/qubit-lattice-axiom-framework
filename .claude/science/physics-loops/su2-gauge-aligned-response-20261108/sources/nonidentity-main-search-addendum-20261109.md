# Current-main and open-PR coverage addendum: nonidentity compact backgrounds

Read-only follow-up in `/Users/jonreilly/.codex/worktrees/su2-background-centered/Physics`, worktree HEAD `97fc90828ab071b5813d1c9b6c8a952dc042509b`; `origin/main` at launch was `bf92a1d763030836ed55631d5d7a7ef3b288f284` and was not fetched or changed. The existing author file `parts/nonidentity-centered-regional-estimates.md` was present as untracked before this pass and was not read or modified. This addendum is bounded source checking, not a proof, novelty result, or exhaustive repository/PR survey.

## Current-main search and matches

Ran six streaming `git grep -I -n -i -E` patterns over `origin/main -- docs .claude/science`: `non[- ]?identity` (548 lines/245 files), `background field` (18/14), `relative coerciv` (0/0), `stationary.{0,30}(center|field|mode)|center.{0,30}stationary` (149/90), `complete normalized` (42/37), and `compact.{0,40}coerciv|coerciv.{0,40}compact` (4/4). Full line inventories are in `logs/su2-nonidentity-compact-20261109/main-grep-inventory.log`; the broad filename keyword inventory is in `main-filename-inventory.log` (577 paths, intentionally noisy). Many matches are unrelated historical packets and mathematical uses of “nonidentity”; the patterns are retrieval filters, not a completeness certificate.

Three plausible current-main hits were inspected at the relevant argument scope:

| Exact current-main source / SHA-256 | Result and scope | Match limit |
|---|---|---|
| `docs/SU2_TWO_REGION_BOUNDARY_RESPONSE_BOUNDED_THEOREM_NOTE_2026-11-08.md` / `94986863c312a5880569cdf8d663c191a3d802a51542e2b671bcfdbc615e913c`, §§1–2 and 7 | One-step finite Wilson law `q_beta(U) product_c k_c(V_c|U)`, exact source/boundary identities and a volume-uniform Dobrushin comparison when its explicit small-parameter condition (33) holds; all conditioned-kernel normalizers are retained. | Different one-hidden-layer posterior, not the two-hidden-layer deleted-`J` marginal. Criterion is a small-`beta`, small-`lambda` sufficient regime and supplies no full compact centered mode/relative coercivity for the target at arbitrary fixed `kappa>0,u>=1`. Closest live-main conditional response machinery, not a drop-in theorem. |
| `docs/COMPACT_U1_WILSON_TO_SOURCE_FREE_MAXWELL_BOUNDED_THEOREM_NOTE_2026-09-02.md` / `f267dc6289b28802cb063740854cbb5b513d49ccaddd79cdba23a0648b65411f`, §§1–6 | Compact `U(1)` supplied Wilson action, exact compact cube identity, smooth-field limit, and flat-background quadratic kernel. | Abelian action/continuum statement; no SU(2) normalized hidden posterior, regional conditioning, or deleted terminal kernels. |
| `.claude/science/physics-loops/native-wilson-second-order-20260907/PRIMARY_STRUCTURAL_REVIEW.md` / `055eea596a2616f87538c0a5936c1e98bfca34133f8fa265656dadf133e40bf1`, full 31 lines | Checks a compact positive transfer operator's dense range, indefiniteness of a multiplier insertion, and leading spectral difference. | Spectral operator perturbation argument, not a nonidentity-background energy-minimizer or compact conditional-density estimate. No transfer is indicated. |

Thus the wider current-main scan exposed no closer match than the one-step SU(2) response note. This is a bounded result about the inspected candidates and search terms only.

## Targeted current open-PR search

Used read-only GitHub search, repo `jonathonreilly/qubit-lattice-axiom-framework`, `state=open`, topn 20, with exact queries:

- `repo:jonathonreilly/qubit-lattice-axiom-framework is:pr is:open SU2 coercivity` returned no items.
- `repo:jonathonreilly/qubit-lattice-axiom-framework is:pr is:open background field` returned #10139, whose TOE assembly body mentions a Yang–Mills background in unrelated proposed-theory planning; not a compact SU(2) hidden-law theorem.
- `repo:jonathonreilly/qubit-lattice-axiom-framework is:pr is:open Yang-Mills regional` returned #10149. Its body states the identity-terminal seven-edge two-plaquette marginal and explicitly names nonidentity terminal-background compact estimates as next work. This is the target PR, not an independent supplier.

Search is title/body keyword retrieval, not exhaustive open-PR review. The external primary-literature comparison is unchanged from the parent extraction; no new exact source surfaced, so no further literature search was run.

Recovery: source revision and hashes are pinned above; full deterministic repo inventories and query text are under the adjacent log directory. No source, existing author part, Git ref, PR, or scientific status was changed. Only this addendum and the assigned logs are outputs.
