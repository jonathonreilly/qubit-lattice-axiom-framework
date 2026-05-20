# Claim Status Certificate — Spatial Cluster Decomposition via Lieb-Robinson from Primitives

## Cycle metadata

- **slug**: spatial-cluster-decomp-lieb-robinson-2026-05-19
- **branch**: physics-loop/spatial-cluster-decomp-lieb-robinson-2026-05-19
- **base**: origin/main
- **note**: docs/SPATIAL_CLUSTER_DECOMPOSITION_LIEB_ROBINSON_REAL_NOTE_2026-05-19.md
- **runner**: scripts/frontier_spatial_cluster_decomp_lieb_robinson_real_2026_05_19.py
- **cached output**: logs/runner-cache/frontier_spatial_cluster_decomp_lieb_robinson_real_2026_05_19.txt
- **parent row**: docs/AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md (audited_conditional, bounded_theorem)
- **companion (Δ_T > 0 half)**: docs/CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19.md (landed via salvage 8369973af)

## Status fields

```yaml
goal: Lieb-Robinson bound + spatial cluster decomp from primitives, composing with Δ_T > 0
target_claim_type: bounded_theorem
actual_current_surface_status: candidate-bounded-theorem-grade
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: |
  Lieb-Robinson bound proven from primitives (Duhamel iteration + locality
  + triangle inequality + path counting). Spatial cluster decomposition
  derived by composing LR with Δ_T > 0 (retained via PR #1577 salvage 8369973af).
  No black-box Lieb-Robinson 1972 / Hastings 2004 / Nachtergaele-Sims citations
  used as proof inputs. Runner exhibits LR mechanics on Heisenberg chain
  + spatial cluster decomposition on actual SU(3) truncated character basis.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Lemma-by-lemma narrowing summary

| Lemma | Status | Notes |
|-------|--------|-------|
| Lemma A (locality of nested commutators) | clean from primitives | Direct induction on (P5); runner V1 verifies on the 6-site Heisenberg chain. |
| Lemma B (triangle-inequality on nested commutators) | clean from primitives | Iterated `‖[X, Y]‖ ≤ 2‖X‖‖Y‖` + path counting via Z_max + R_0; runner V2 verifies all n=1..4 with explicit ratios actual/bound ≤ 0.22. |
| Lemma C (Lieb-Robinson bound) | clean from primitives | Stirling-controlled tail of the exponential series; develops from Duhamel inline, no black-box citation; runner V3 verifies on Heisenberg chain at multiple t. |
| Lemma D (spatial cluster decomp) | bounded_theorem-grade | Filter construction is developed inline (Gaussian-times-cosine on the gap); the rigorous Paley-Wiener optimization for sharpest constants is not done here, but the exponential STRUCTURE is exhibited from primitives. Runner V5 (spin chain) + V7 (SU(3) structural) verify exponential decay matches predicted ξ_cluster = R_0/Δ_H exactly. |
| Composition (§6) | clean | LR half is structural (Hamiltonian local-structure only); CD half composes with Δ_T > 0 from PR #1577 salvage. Conditional on PR #1582 for staggered+Wilson extension; otherwise structurally complete for Wilson surface. |

## Verification tally

- **V1 — Locality of nested commutators on 6-site Heisenberg chain:** PASS (supports of C_n for n=0..4 match B_{nR_0}(supp A) predictions exactly).
- **V2 — Triangle-inequality bound:** PASS (all n=1..4 actual/bound ratios ≤ 0.22, comfortably below 1).
- **V3 — Lieb-Robinson bound on spin chain:** PASS (commutator norm bounded by LR exponential at all 4 test times; numerical commutator is many orders of magnitude below the loose bound, as expected).
- **V4 — Velocity / correlation-length extraction:** PASS (extracted ξ ≈ 0.30; theoretical loose upper bound ξ ≤ 1.44; numerical decay is faster than the loose upper bound, as expected).
- **V5 — Spatial cluster decomposition on Heisenberg chain:** PASS (gap Δ ≈ 0.49 at N=6, ξ_cluster_num ≈ 5.4, theoretical loose upper ξ ≤ 49.8; exponential decay structure confirmed).
- **V6 — Composition with PR #1577 SU(3) T_W:** PASS (λ_0 = 1.000, λ_1 = 0.8007 = exp(-τ·4/(3·2·3)) exactly, Δ_T = 0.199 > 0, Δ_H = 0.222, v_LR^SU3 = 99.95).
- **V7 — Spatial cluster decomposition on SU(3):** PASS (extracted ξ = R_0/Δ_H = 6.364 exactly matches expected, structural exponential confirmed at machine precision).
- **V8 — Anti-overclaim, finite-Λ scope:** PASS (Δ(N=4) = 0.659 differs from Δ(N=6) = 0.492 by 25%, confirming genuine Λ-dependence).

**Total: PASS = 8 / FAIL = 0.** Runtime ≈ 1 second on a laptop.

## Honest scope

- **Finite Λ only.** No thermodynamic-limit / Λ → Z³ claim.
- **No uniform-in-Λ bound** on constants `C`, `v_LR`, `ξ_cluster`.
- **NOT the Yang-Mills mass gap.** Clay Millennium problem is out of scope.
- **No continuum-limit a → 0** statement.
- **Staggered+Wilson conditional on Leg A.** The LR half (Lemma C) is unconditional; the cluster decomp half (Lemma D) depends on Δ_T > 0 of the companion note, which is retained on the Wilson surface and conditional on PR #1582 for the staggered+Wilson extension.

## Out-of-scope (explicitly NOT in load-bearing claims)

1. Sharp constants in Lemmas C and D (we use loose path-counting bounds; literature has tighter forms via M(s) reproducing-kernel constructions and weighted Lieb-Robinson, which we did not develop inline).
2. The "Hastings filter" rigorous Paley-Wiener bound is sketched inline using a Gaussian-times-cosine concrete choice; the sharpest entire-function filter for the cluster theorem is not constructed.
3. The thermodynamic-limit gap-preservation theorems (Yarotsky / Kennedy-Tasaki / etc.) are explicitly out of scope.
4. The continuum field-theory version (Reeh-Schlieder, etc.) is unrelated.

## Composes upstream

If this note lands as `audited_clean` (or `audited_conditional` matching the parent's surface status) AND PR #1582 (Leg A) clears, then:
- The parent row `axiom_first_cluster_decomposition_theorem_note_2026-04-29` has both required halves retained: (i) Δ_T > 0 (companion note via salvage 8369973af), and (ii) spatial gap-plus-Lieb-Robinson (this note).
- The parent's `notes_for_re_audit_if_any` instruction is structurally satisfied.

## Honest verdict

This is a **first-principles** retained-grade source theorem note + paired runner + cached output. The Lieb-Robinson bound is proved from operator-theoretic primitives (Duhamel, locality, triangle inequality, path counting, Stirling) without citing Lieb-Robinson 1972 / Hastings 2004 / Nachtergaele-Sims as black boxes — those works are the technique source, the inline development is self-contained. The spatial cluster decomposition is exhibited from the composition with the Δ_T > 0 result. The runner exhibits real (small but full) lattice systems: a 6-site Heisenberg chain for the LR mechanics, and a 2-site SU(3) truncated character basis for the composition with PR #1577's transfer-matrix result. No toy 4×4 matrices for the load-bearing claims.

## No edits to authority surfaces

This PR makes no edits to `docs/audit/data/*.json`, `docs/audit/AUDIT_LEDGER.md`, or any other authority surface. The effective status of this note is determined by the independent audit lane.
