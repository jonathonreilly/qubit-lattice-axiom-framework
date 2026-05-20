---
goal: discharge spatial slab-bridge note's named hypotheses for canonical Cl(3)⊗Z³
target_claim_type: bounded_theorem
actual_current_surface_status: candidate-bounded-theorem-grade
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: |
  §3 lifts PR #1577 salvage 8369973af's Δ_T>0 result to Δ_x>0 by Wilson
  cubic axis-permutation symmetry. §4 composes with Leg A (PR #1582 salvage
  5f6f0b87a) for staggered+Wilson conditional Δ_x_full>0. §5 discharges
  hypotheses (i) and (ii) of the 2026-05-17 slab-bridge note. Runner
  verifies axis-permutation invariance + T_x=T_τ + Δ_x=Δ_τ on actual SU(3)
  truncated character basis.
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Claim status certificate — Slab-bridge spatial T_x positivity and Δ_x > 0

## Pack identity

- **Pack name:** slab-bridge-spatial-Tx-real-2026-05-19
- **Source theorem note:** [`docs/SPATIAL_SLAB_TRANSFER_OPERATOR_POSITIVITY_AND_DELTA_X_REAL_NOTE_2026-05-19.md`](../../../../docs/SPATIAL_SLAB_TRANSFER_OPERATOR_POSITIVITY_AND_DELTA_X_REAL_NOTE_2026-05-19.md)
- **Runner:** [`scripts/frontier_slab_bridge_spatial_Tx_real_2026_05_19.py`](../../../../scripts/frontier_slab_bridge_spatial_Tx_real_2026_05_19.py)
- **Cached output:** [`logs/runner-cache/frontier_slab_bridge_spatial_Tx_real_2026_05_19.txt`](../../../../logs/runner-cache/frontier_slab_bridge_spatial_Tx_real_2026_05_19.txt)
- **Parent slab-bridge note:** [`docs/CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17.md`](../../../../docs/CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17.md)
- **Source date:** 2026-05-19

## Claim under audit

The 2026-05-17 spatial slab-bridge note proved a CONDITIONAL exponential
spatial clustering result, conditional on two named hypotheses:

- **H1.** Existence of a positive Hermitian spatial slab transfer operator
  `T_x : H_slab(x) → H_slab(x)` on a finite-dim slab Hilbert space, with the
  standard slab construction `Z(Λ) = Tr(T_x^{L_x})`.
- **H2.** Spatial transfer-matrix gap `Δ_x > 0`.

This pack discharges both H1 and H2 on the canonical Cl(3)⊗Z³ surface via:

- **Theorem A (pure Wilson, source-side bounded_theorem-grade):** Wilson
  lattice action's cubic axis-permutation symmetry lifts PR #1577 salvage
  `8369973af`'s temporal-slab Δ_T > 0 result verbatim to the spatial-slab
  transfer operator T_x. T_x_W is self-adjoint, trace-class, strictly
  positivity-preserving, with simple top eigenvalue and Δ_x_W > 0 on finite Λ.

- **Theorem B (staggered+Wilson, source-side bounded_theorem-grade conditional on Leg A):**
  Composing the pure-Wilson T_x_W with the spatial-slab fermion determinant
  factor `det(D_x[U] + m·I)` (positive pointwise via Leg A retain from PR
  #1582 salvage `5f6f0b87a`) gives T_x_full positive Hermitian trace-class
  with Δ_x_full > 0 on finite Λ. Conditional only on Leg A retention.

## Runner verification

8 verifications, all PASS. Cached runtime: 0.29 s.

- **V1 — Wilson action axis-permutation invariance.** N=20 random SU(3)
  configurations on a 2×2×2 lattice; all 3 cubic axis-swaps yield
  `S_W[σU] = S_W[U]` to max |ΔS| = 2.13e-14.
- **V2 — T_x = T_τ kernel under axis swap.** Spectrum lengths 3136, max
  spectrum difference = 0.0 (bit-identical).
- **V3 — T_x kernel strict positivity.** min K_τ = 1.29e-3 on 16×16 SU(3)
  torus mesh at τ=4, N_max=12; margin > 1e-4.
- **V4 — Trace-class convergence.** Partial sums at τ=4: S_4=50.25, S_8=53.65,
  S_12=53.65; relative tail S_8→S_12 = 5.94e-6 < 1e-4.
- **V5 — Δ_x > 0 from diagonalization.** Top λ_0 = 1.0 (multiplicity 1),
  λ_1 = 0.411, Δ_x = log(λ_0/λ_1) = 8.89e-1 matches predicted 2τ/9 to 1e-10.
- **V6 — Δ_x = Δ_τ to machine precision.** Independent constructions give
  Δ_τ = Δ_x = 0.88888888888888884, relative difference = 0.0.
- **V7 — Spatial-slab Leg A fermion det positivity.** N=30 random SU(3)
  configurations; min det(D_x + m I) = 0.125 at m=0.5; all real-positive.
- **V8 — Slab-bridge bound (S) operational.** d ∈ {0, 1, 2}: |C(d)| ≤
  ‖A‖‖B‖ exp(-d · Δ_x) with equality (single-link transfer saturates the
  bound on the (1,0)+(0,1) subspace).

## Composition upstream (audit trace)

This pack supplies OR-branch (b) to the parent
`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29`'s spatial half.
Combined with PR #1583 (LR + composition) as OR-branch (a), PR #1577 salvage
`8369973af` (Δ_T > 0) for the temporal half, and PR #1582 salvage
`5f6f0b87a` (Leg A) for the staggered+Wilson composition, the parent has
TWO independent spatial routes plus a single temporal route to cluster
decomposition on finite Λ.

The audit lane decides whether the discharge of H1 and H2 here suffices to
lift the 2026-05-17 slab-bridge note's status.

## Honest scope

- Finite-Λ only. Thermodynamic limit and Yang-Mills mass gap are explicitly
  out of scope.
- Source `Status:` is source-side; effective status is the audit lane's call.
- Theorem B retains Leg A as a named conditional input.
- This pack does NOT promote the slab-bridge parent row or the Leg A parent
  note. The audit citation graph records edges as described in the source
  note §10.

## Anti-overclaim checks

- The Theorem A lift is structural (axis-permutation symmetry on Wilson +
  Haar + heat kernel), not numerical. The runner verifies the lifted spectrum
  matches identically at machine precision.
- Theorem B is conditional on Leg A and does not stand on its own.
- The (S) bound check in V8 uses the saturating subspace as a strict upper
  bound; the runner does not claim arbitrary correlators saturate.

## Promotion path

- Source-side `bounded_theorem`-grade for Theorem A (pure Wilson).
- Source-side `bounded_theorem`-grade for Theorem B, conditional on Leg A
  retention.
- Effective tier on the public row is the audit lane's decision once the
  PR is reviewed.
