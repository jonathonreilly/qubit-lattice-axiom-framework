# Nonidentity terminal backgrounds: compact-control prior art

Read-only extraction for the continuation of PR #10149. Worktree snapshot
`97fc90828ab071b5813d1c9b6c8a952dc042509b`; current `origin/main`
`bf92a1d763030836ed55631d5d7a7ef3b288f284`. Target law is the actual
`q_u K0 product_(c in O) k1,c(V_c|U1)` with `J` the seven edges of two
plaquettes sharing one edge, `O=E2\J`, odd `L>=3`, `kappa>0`, `m>=3`,
`u>=1`, arbitrary allowed fine trees, and fixed background
`sup_c chord(V_c,I)<=epsilon` for one small epsilon independent of volume.
Keep every surviving input-dependent radial normalizer and exact Haar
normalization. This record is a bounded source map, not a proof or novelty
claim.

## Closest repository statements and exact scope

| Source (SHA-256) | Usable result | Exact mismatch / boundary |
|---|---|---|
| `parts/marginal-nonlinear-chart-estimates.md` (`b1e26baa37cf1dc47331d9a98a834afda5e7634d62f31df50600fd321fc45cb7`) | §§1–5 define the actual deleted-`J` law with surviving `V_c=exp(i v_c.sigma)` and prove uniform finite-template Hessian/chart covariance for every small `v` and all hidden readers in the fixed identity-centered cube. Identity Hessian includes actual deleted-kernel convention, positive normalizer variance, and Haar chart term. | This already covers local nonidentity terminal outputs; it does not give compact complement control or a globally centered Haar-density mode/relative-energy bound at `V`. No inference from local strict convexity to all-compact coercivity. |
| `parts/marginal-regional-relative-coercivity.md` (`2d142414fb4992c2a1e907d42d15ca9f7164ee6e90c892d8c3d529b39e297385`) | §§1–5 give the seven-edge deleted law's small-collar stationary field and full compact relative-energy estimate from the actual global `E_J` inequality, retaining surviving kernel factors. | Explicitly fixes all surviving terminal outputs to `I`; its stationary point and cancellation argument are identity-background results. Needs uniform perturbation in the fixed nonidentity terminal field, with matching regional readers and constants. |
| `parts/marginal-normalized-regional-coercivity.md` (`bd3fa8b5eb989c7718ad5d760a913e33166f3e9edcf52b9f17f82cbd809ca255`) | §§1–3 prove identity-background regional minimizer/compact Haar-energy ratio for the complete normalized kernels; §4 proves all-`u>=1` identity-centered chart convexity/covariance. | Compact regional assertion assumes terminal outputs `I`; §4's allowed small nonidentity `V` is still inside a fixed hidden identity chart. Not a compact-background theorem. |
| `parts/marginal-connected-density-expansion.md` (`79d6f2d98f058180d98f576b1840681a42e504186e1be4975bbbaf47a5121d98`), especially §§1–3, 6–8 | Identifies source-marked compact/chart correction and connected-response consumer; exact surviving normalizers and derivative readers are part of the bookkeeping. | Consumer is zero-source, identity-terminal-background. A shifted compact gas/ratio must be re-instantiated and its activity budget and exact normalizers checked; local chart covariance alone does not provide that compact remainder. |
| `PROOF_TREE.md` §§“subsequent regional/chart” and “Next theorem to attack” | Explicitly distinguishes compact regional estimates at terminal `I` from chart theorem's small nonidentity terminal neighborhood; names the next target as compact connected control on a fixed small terminal-background class. | Planning map only, not evidence for a theorem. |

The actual compact energy is `E_J,V = W0 + kappa sum gamma0 + kappa sum_(c in O) (|M1,c|-<V_c,M1,c>)`; its normalized law also has the surviving `H_u(|M|)` radial terms. The identity theorem's `E_J,I >= c_J sum_e(1-w(a_e))` is not itself the desired relative inequality at `V`: its baseline and tangent cancellation are centered at `I`. Smallness of `V-I` gives local Hessian control in the existing chart, but no uniform bound on the compact complement follows from that fact alone.

## Closest primary literature

T. Balaban, “The variational problem and background fields in renormalization group method for lattice gauge theories,” *Communications in Mathematical Physics* 102 (1985), 277–309, DOI [10.1007/BF01229381](https://doi.org/10.1007/BF01229381). The publisher page and Rutgers author-affiliation record were opened; their abstract states existence of an action minimum on regular gauge configurations with fixed averages and uniqueness up to gauge transformations. The full theorem text was not accessible in this pass (Springer served an access page), so no detailed hypotheses or proof step are imported. It is the closest conceptual comparator for a background-dependent minimizer, but its background is constrained coarse average data in a regular gauge-field space, while the target is a two-layer posterior on a fixed forest slice with seven deleted normalized terminal kernels, arbitrary allowed internal trees, compact relative control against all hidden configurations, and exact radial normalizers. Its abstract alone does not establish any target clause.

J. Dimock, “Covariant Axial Gauge,” [arXiv:1410.2798](https://arxiv.org/abs/1410.2798), is the accessible comparator already recorded in `sources/two-plaquette-coercivity-prior-art-20261109.md`: §§2.1–2.2 treat abelian real-valued fields and quadratic curl control, not nonlinear compact SU(2) energy or deleted normalized kernels. It does not close the target gap. Bauerschmidt–Bodineau's whole-Euclidean-space covariance and Kolesnikov–Milman's smooth-boundary results remain chart-method comparators as described in `sources/marginal-regional-chart-prior-art-20261109.md`; neither supplies full compact group control for this law.

Search coverage: targeted primary searches for Balaban background-field minimizers, Dimock/SU(2) compact coercivity, and compact-group low-temperature minimizers with nonidentity boundary values; exact queries and returns are preserved in `logs/su2-nonidentity-compact-20261109/literature-search.log`. Existing repo prior-art records and PR #10149 proof tree were reused; no exhaustive literature or open-PR search is claimed. No historical automation or external theorem was used as a proof premise.

## First missing mathematical bridge

For the specified fixed `epsilon`-ball, establish (or refute) a uniform
centered compact estimate for the actual normalized Haar density: construct a
background-dependent mode `a*(V)` with constants uniform in volume, `u>=1`,
tree choices, and all such `V`, then prove a relative lower bound against
`sum_e[1-w(a_e^*^{-1}a_e)]` on the entire compact hidden space. The proof must
include the actual `O`-kernel terms and their radial normalizers, including
zero-mean cases, and preserve exact Haar ratios. This is the first gate before
transporting regional ratios/connected compact activities and source readers.
The existing chart theorem can support local Hessian/covariance around its
identity-centered domain for small nonidentity `V`; it does not discharge this
global bridge. Nothing here establishes its truth or failure.

Evidence identities: source hashes above were refreshed from this worktree at
write time. `origin/main` freshness and exact worktree revision are as listed
above. Only this note and its assigned search log are deliverables; no source,
prompt, Git ref, PR, or scientific status was changed.
