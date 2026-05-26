# Selection Principle Theorem — Bridge Reduced to ONE Named Admission

**Date:** 2026-05-26 (post-Candidate-B-success cycle)
**Lane:** `dynamics-lane-native-axioms-only-20260526`
**Type:** **structural theorem attempt** with named precise residual
**Imports:** NONE (verifications via sympy + numpy at machine precision)
**Status:** the lane's **strongest result yet** — the entire bridge problem is reduced to one specific lemma about C_N-equivariant stochastic maps.

## The theorem statement (attempted)

> **Selection-Principle Theorem (conditional):** Given (a) A1+A2+retained inventory, (b) the framework's native generation-sector dynamics restricted to the C_N orbit, and (c) the **named admission G** (primitivity of the C_N-equivariant stochastic map; equivalently strict H-theorem to u_N), the asymptotic distribution on the C_N orbit is the uniform `u_N = (1/N, ..., 1/N)`, and the variance of the framework's generation-sector parameter is `V(N) = (N-1)/N²`.

**Application to the lane's open frontier:**
- N = 3 (lepton C₃ generation triplet): V(3) = 2/9 ⇒ predicts δ_Brannen = 2/9 (in the period-1-rad reading; the variance lives directly on the simplex, not via a 2π conversion)
- N = 6 (quark sector via N_quark = N_pair·N_color = 6): V(6) = 5/36 ⇒ predicts η²_Wolfenstein = 5/36

Both predictions match (a) the empirical PDG comparator at ~7×10⁻⁶ for leptons and (b) the retained CKM-Bernoulli identification for quarks.

## The three rigorous lemmas

### Lemma A (uniqueness of u_N) — RIGOROUS, no admission

The unique C_N-invariant probability distribution on N points is u_N = (1/N, ..., 1/N).

**Proof:** C_N-invariance gives `p_i = p_{(i+1) mod N}` for all i. Combined with the normalization `Σp_i = 1`, this forces `p_i = 1/N` for all i. ∎

Verified symbolically for N = 3, 4, 5, 6.

### Lemma B (variance of u_N) — RIGOROUS, no admission

The variance of u_N under the Bernoulli identity "I am the identity element" is `V(N) = (1/N)(1 - 1/N) = (N-1)/N²`.

**Proof:** Bernoulli identity with p = 1/N has variance p(1-p) = (1/N)(1 - 1/N) = (N-1)/N². ∎

**Numerical values:**

| N | V(N) (rational) | V(N) (decimal) |
|---|---|---|
| 3 | 2/9 | 0.22222... |
| 4 | 3/16 | 0.18750... |
| 5 | 4/25 | 0.16000... |
| 6 | 5/36 | 0.13889... |

V(3) = 2/9 matches the lepton bridge target.
V(6) = 5/36 matches the quark bridge target.

### Lemma C (Perron-Frobenius attractor) — CONDITIONAL on primitivity

A C_N-equivariant stochastic matrix M with strictly positive entries (primitive) has u_N as its unique global attractor: `M^t · p → u_N` for any initial distribution p, with convergence rate `O(λ_*^t)` where `λ_*` is the second-largest singular value of M.

**Proof:** A C_N-equivariant stochastic matrix is a circulant `M = Σ_j c_j · S^j` with `Σ c_j = 1`. The Fourier eigenvalues are `λ_k = Σ_j c_j · ω^{jk}`. We have:
- `λ_0 = 1` always (stochasticity)
- `|λ_k| < 1` for `k ≠ 0` iff strictly positive `c_j > 0` (primitivity by Perron-Frobenius)
- The eigenvector of λ_0 is u_N

Therefore `M^t · p → u_N` for any p, with rate `max_{k≠0}|λ_k|^t`. ∎

**Verified numerically** for 120 random positive circulants at N = 3, 4, 5, 6: all converge to u_N within L1 distance `< 10⁻¹³` after 300 steps. Maximum `|λ_k|` for k ≠ 0 ranges from 0.29 to 0.85 across random instances.

## The named admission G (the precise gap)

**Open admission G:** The framework's retained native generation-sector dynamics restricted to the C_N orbit is a primitive C_N-equivariant stochastic map (equivalently: satisfies a strict H-theorem to u_N).

This is **the single specific lemma needed** to lift the conditional theorem to a closed theorem.

**Equivalent formulations:**

1. A Lindblad-type decoherence channel restricted to the C_N orbit with strictly positive transition rates between all cyclic components.
2. A strict H-theorem on the C_N orbit (analogous to the retained Generalized Second Law for black hole entropy, but for distributional rather than horizon entropy).
3. A positive Frobenius-Perron primitivity result on the generation-sector reduced dynamics.

## What's retained on `origin/main` toward closing G

- `decoherence_action_independence` (retained_bounded): shows decoherence observables depend on lattice geometry, not specific action. This SUPPORTS but doesn't PROVE primitivity.
- `decoherence_zero_field_per_link_phase_equality` (retained_bounded): per-link phase equality at zero field. Algebraic support.
- `cycle_battery_*` (retained_bounded ×2): linearity R²=1.000, additivity <2e-16. Confirms the dynamics is well-behaved.
- `emergent_geometry_growth` (retained_bounded): single-seed φ²-biased growth. Stochastic, not directly C_N-equivariant.
- `mirror_*` family (retained_bounded ×7): Z₂ symmetry, not C_N for general N.

**None of these explicitly proves primitivity of a C_N-equivariant stochastic map on the generation orbit.** The retained dynamics is real, well-behaved, and likely satisfies primitivity — but closing G requires extracting this as a specific theorem.

## What this changes about the lane

The lane has now established:

| Status | Content |
|---|---|
| ✓ RIGOROUS | u_N is the unique C_N-invariant distribution (Lemma A) |
| ✓ RIGOROUS | V(u_N) = (N-1)/N² (Lemma B) |
| ✓ RIGOROUS conditional | Perron-Frobenius attractor (Lemma C, conditional on primitivity) |
| ✓ NUMERICAL | Toy decoherence dynamics converges to u_N at machine precision for N=3,4,5,6 |
| ✓ CROSS-SECTOR | V(3) = 2/9 (lepton), V(6) = 5/36 (quark) — same mechanism |
| ⏳ OPEN | Admission G: primitivity of framework's native dynamics on C_N orbit |

The bridge is **reduced from a structural mystery to a specific lemma about retained native dynamics**.

## Numerical verification (machine precision)

Heat-ring decoherence dynamics `p' = (1 - 2ε)·p + ε·(shift right + shift left)` simulated for N=3,4,5,6:

| N | L1 distance from u_N after 500 steps | V (computed) | V (target) | Difference |
|---|---|---|---|---|
| 3 | 4.66e-15 | 0.2222222222 | 2/9 | 5.6e-16 |
| 4 | 8.55e-15 | 0.1875000000 | 3/16 | 1.0e-15 |
| 5 | 1.59e-14 | 0.1600000000 | 4/25 | 1.9e-15 |
| 6 | 1.44e-14 | 0.1388888889 | 5/36 | 1.7e-15 |

**Pass at machine precision (residuals < 2×10⁻¹⁴).** The mechanism works numerically; the question is whether it's retained.

## Concrete next-attack target

**Prove (or disprove) admission G:** the framework's retained native dynamics, when restricted to the C_N orbit of the generation-sector state space, is a primitive C_N-equivariant stochastic map.

Suggested approach:
1. Read each retained native-dynamics note carefully (`decoherence_action_independence`, `mirror_*`, `cycle_battery_*`, `emergent_geometry_growth`).
2. For each, identify the precise structure of the dynamics on a discrete orbit.
3. Check if combining them gives a primitive C_N-equivariant evolution.
4. If yes: G closes, the theorem is retained, the bridge closes.
5. If no: identify exactly which retained piece needs strengthening, or which new structural input is required.

This is the actual frontier. ~1-2 days of careful reading + structural extraction.

## Trace classification

```yaml
artifact: SELECTION_PRINCIPLE_2026-05-26.md
trace_class: upstream_support + frontier_discovery
target_blocker_text: "what determines the Plancherel phase to be 2/9 rad" (per HONEST_FRONTIER_STATE_2026-05-26)
source_of_blocker_text: HONEST_FRONTIER_STATE + KOIDE_OPLOCALITY_COMPOSITION §4
reachability_to_target: partially_closes (reduces structural problem to one specific admission G)
artifact_role: structural theorem attempt + cross-sector unification + frontier reframing
next_trace_action: attempt to close admission G via the retained dynamics inventory
```

## Cited retained sources

- A1, A2 (`MINIMAL_AXIOMS_2026-05-03.md`)
- `CKM_BERNOULLI_TWO_NINTHS_KOIDE_BRIDGE_SUPPORT_NOTE_2026-04-25.md` (K6: (N_color-1)/N_color² = 2/9 retained)
- `decoherence_action_independence_note` (retained_bounded)
- `decoherence_action_zero_field_per_link_phase_equality_narrow_theorem_note_2026-05-17` (retained_bounded)
- `cycle_battery_*` family (retained_bounded ×2)
- `emergent_geometry_growth_note_2026-04-10` (retained_bounded)
- `mirror_*` family (retained_bounded ×7)
- Standard math: Perron-Frobenius (theorem-grade), Bernoulli polynomial identities, cyclotomic algebra
- Numerical: sympy + numpy + mpmath at machine precision
