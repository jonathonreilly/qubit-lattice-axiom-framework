# Approach registry — admissibility-induced-law-20260906

| Family | Approach | Status |
|---|---|---|
| F1 static-law existence | Brook ratio lemma + canonical potential (Möbius) + triangle-free cliques | T1 proof route (native) |
| F2 static-law non-existence certificate | exact compatibility rank; symbolic Brook cycle | T1 executed instances (sum rule) |
| F3 positivity necessity | finite occurrence-census contradiction on the eight-configuration four-cycle law | T1 witness |
| F4 formation law | the pointwise identity mu_sigma * prod Z_k = mu * Z_W; normalizer constancy lemmas; plaquette lemma | T2 proof route |
| F5 coincidence routes | five exact attempted routes (constant rule; site weight; absence extension; order mixture; non-product rule) | family G; N-gate |
| F6 infinite volume | DLR specification from the finite static laws | not this block; queued |

## Block 08 — the three-dimensional monotone formation law (2026-09-15)

| Family | Object/formulation | Mechanism/invariant | Terminal obligation | Strength vs target | Status | Concrete evidence | Reopen condition |
|---|---|---|---|---|---|---|---|
| F8.1 projective consistency in 3D | box laws under translation | the 2D 180° identity (P7(a)) | first-plane removal identity | target-equivalent for a translation-invariant limit | blocked-local (refuted at scope) | the `2×2` plane-transfer witness: 1296/1296 states differ at (3,1,2); the successor/predecessor-triple lemma | an identity other than telescoping |
| F8.2 plane-transfer chain | planes as states of a Markov chain | positivity → unique stationary law; down-set consistency across cross-sections | the infinite-cross-section limit | weaker (finite W) / comparable with F8.3 for W → ∞ | candidate-complete (finite W); provisional (W → ∞ via F8.3) | exact `π_2` by orbit reduction; boundary planes 2D | — |
| F8.3 causal coupling | discrepancy propagation along monotone paths | per-neighbor sensitivity `c`; path counting `N(z,x) c^d` | none in the region `3c < 1` | stronger than needed (gives decay and uniqueness) | candidate-complete in the region | exact `c` at eight triples; cube influence check | a bound for `c ≥ 1/3` needs a different mechanism |
| F8.4 Gibbs form | product of kernels regrouped | normalizers as `K`-sums | irreducibility of `K_3` | exact | candidate-complete | third difference `2160/2197` at (3,1,2) | — |
| F8.5 down-set consistency | marginals on down-sets | leaf removal in reverse order | none | exact, any dimension | candidate-complete | cube marginal on `x_3 = 0` equals the 2D law | — |

## Block 09 — Markov graph, eight corner laws, the sweep's imprint (2026-09-15)

| Family | Object/formulation | Mechanism/invariant | Terminal obligation | Strength vs target | Status | Concrete evidence | Reopen condition |
|---|---|---|---|---|---|---|---|
| F9.1 DLR limit | finite-box conditional identity on a window | factors not meeting the window cancel; the identity is finite and passes to the limit | none in the region | exact | candidate-complete | L1 | — |
| F9.2 specification uniqueness under full support | two continuous finite-range kernels a.s. equal | every cylinder charged ⇒ equal everywhere | full support (proved from box positivity) | exact | candidate-complete | L2 | — |
| F9.3 dependency-set combinatorics | offsets κ_i e_i − κ_j e_j and their grouping | point reflection preserves the set, not the grouping | within-pair witness | exact | candidate-complete | C1–C3 | — |
| F9.4 column reversibility | J = πP versus J^T | the reversed class is the reversed chain | none | exact at 2x2 | candidate-complete | D1–D5 | larger cross-sections not computed |

## Block 10 — the recorded-set Gibbs theorem (2026-09-15)

| Family | Object/formulation | Mechanism/invariant | Terminal obligation | Strength vs target | Status | Concrete evidence | Reopen condition |
|---|---|---|---|---|---|---|---|
| F10.1 regrouping | the product of conditionals over an order | every edge recorded once by its later endpoint | none | exact | candidate-complete | T1 (executed on 48 orders) | — |
| F10.2 vacuum-normalized potential | Möbius inversion on the subset lattice | uniqueness; clique support under a Markov hypothesis | none | exact | candidate-complete | T3(a) re-proved | — |
| F10.3 mixed differences | `Δ_k log K_k` at the vacuum | nonzero iff a genuine `k`-body term | nonzero at every nonconstant triple (open) | exact where executed | candidate-complete at two triples | `k = 2..6` ratios | a triple with a vanishing difference |
| F10.4 bipartite obstruction | co-recorded neighbors are non-adjacent | even coordinate sums | none | exact | candidate-complete | T4 | a non-bipartite window (none on `Z^3`) |
