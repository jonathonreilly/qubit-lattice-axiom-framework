# Cluster Decomposition Block 02 — CLAIM_STATUS_CERTIFICATE

## Block 02: Δ_T > 0 finite-Λ Perron-Frobenius narrow bounded support

### Status fields

```yaml
block: 02
artifact: docs/CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_PERRON_FROBENIUS_NARROW_BOUNDED_NOTE_2026-05-18.md
runner: scripts/frontier_cluster_decomposition_delta_t_finite_lambda_perron_frobenius_narrow_2026_05_18.py
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Narrow bounded support theorem on finite-Λ Δ_T > 0 for canonical Cl(3) ⊗ Z^3 staggered + Wilson, via standard Perron-Frobenius (textbook Wilson lattice gauge theory) composed with framework's already-retained Leg A fermion-determinant positivity. Bounded because thermodynamic limit, Yang-Mills mass gap, and uniformity-in-Λ are explicitly out of scope."
audit_required_before_effective_retained: true
bare_retained_allowed: false
target_for_parent_row:
  parent: axiom_first_cluster_decomposition_theorem_note_2026-04-29
  proposed_disposition: replace "Δ_T > 0 admitted" with "Δ_T > 0 retained on finite Λ via this note"; the thermodynamic limit and spatial cluster decomposition step remain open
review_loop_disposition: pending (run review-loop after PR open)
runner_result: PASS=30 FAIL=0
```

### V1-V5 Promotion Value Gate

| # | Question | Honest answer |
|---|---|---|
| V1 | What SPECIFIC verdict-identified obstruction does this PR close? | The parent row's "Open dependency for full L2 closure" §"Standard candidates" explicitly lists "Perron-Frobenius for the positive transfer matrix proving non-degeneracy of the top eigenvalue under canonical-surface boundary conditions" as candidate 2. This PR delivers candidate 2 on **finite Λ**, with explicit out-of-scope disclaimers for the thermodynamic limit. |
| V2 | What NEW derivation does this PR contain? | The composition of standard textbook Perron-Frobenius for pure Wilson (Osterwalder-Seiler 1978) with the framework's already-retained **Leg A fermion-determinant positivity** (from `STRONG_CP_THETA_ZERO_NOTE.md`) to extend the gap result to the canonical staggered + Wilson Hamiltonian on finite Λ. This composition has not been packaged separately as a retained authority. |
| V3 | Could the audit lane already complete this derivation? | Partial: the textbook Perron-Frobenius for pure Wilson is standard; the composition with Leg A is a small framework-specific bridge that the audit lane could verify in principle but has not been packaged. |
| V4 | Is the marginal content non-trivial? | **Yes** — the four-step proof (Wilson PF → irreducibility → fermion-det positivity → composite PF) is a specific framework-substrate bridge composition. The Leg A appeal in Step 4 (`det(D+m) = Π_k (m²+λ_k²) > 0` for real `m > 0`) is the load-bearing framework-specific input. |
| V5 | One-step variant of prior cycle? | **No** — different parent row (cluster_decomposition vs observable_principle), different mechanism (Perron-Frobenius vs Cauchy classifier), different scope (finite-Λ spectral gap vs scalar functional admissibility class). |

**V-gate disposition:** PR may be opened. Marginal content
non-trivial; not a one-step variant of any prior cycle.

### What this block does NOT do (anti-overclaim list)

- Does **NOT** close the thermodynamic limit Λ → Z^3.
- Does **NOT** establish a uniform-in-Λ gap bound.
- Does **NOT** claim the Yang-Mills mass gap (Clay Millennium problem).
- Does **NOT** establish a continuum limit a → 0 gap.
- Does **NOT** close spatial cluster decomposition (still needs separate spatial Lieb-Robinson / spatial transfer-matrix argument).
- Does **NOT** promote `AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE` to retained — only supplies the previously-admitted `Δ_T > 0` input on finite Λ.

### Independent audit handoff

The audit lane retains full authority to:
1. Audit this finite-Λ Perron-Frobenius bounded support theorem and ratify or modify.
2. Re-audit `AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29` against this new finite-Λ supply for the `Δ_T > 0` admission.
3. Independently decide whether the thermodynamic-limit and spatial-clustering open work require separate retained-bounded source notes.

### Honest narrowest status

**Bounded support — finite-Λ Δ_T > 0 via Perron-Frobenius + Leg A.**

This block delivers candidate 2 of the parent row's three open
mechanism candidates, on finite spatial volume only. The
thermodynamic-limit closure remains a Clay Millennium-level open
problem and is **not** undertaken or pre-judged here.
