# Koide A1 Investigation — Final Theoretical Status

**Status:** bounded - bounded or caveated result note
**Date:** 2026-04-22 (2026-05-18: claim_scope formalized as conditional
variational route to A1, not an axiom-native derivation, per audit
verdict boundary instruction; 2026-05-19: audited-conditional repair
narrows retained scope to the trace reduction + A1 zero-locus identity
the runner verifies, and marks `V(Φ) = 81(a² − 2|b|²)²` as an
assumed ansatz — see audit block below).
**Claim type:** bounded_theorem

## 2026-05-19 audit-conditional repair

**Trigger.** Audit lane flagged this note as carrying language that
could read as if the Koide-Nishiura quartic effective potential
`V(Φ) = 81(a² − 2|b|²)²` (equivalently
`V(Φ) = [2(trΦ)² − 3tr(Φ²)]²` after the trace reduction) is *derived*
from `Cl(3)` on `Z^3`. It is not. The form is imported from the
Koide-Nishiura program as a variational ansatz on the charged-lepton
mass matrix, and the runner only verifies algebraic properties of that
ansatz; it does **not** derive the ansatz from the framework axioms.

**Retained scope after narrowing.** Of the content advertised on this
note, the only pieces retained as theorem-grade by the paired runner
`frontier_koide_a1_quartic_potential_derivation.py` (5/5 PASS) are:

1. **Trace reduction identity.** Given `Φ = a·I + b·σ` (Hermitian
   charged-lepton mass-matrix block, `a ∈ ℝ`, `b ∈ ℂ³`), the
   identity `2(trΦ)² − 3tr(Φ²) = 9(a² − 2|b|²)` holds algebraically.
   No physics input; pure trace algebra in the block.

2. **A1 zero-locus identity.** With `V(Φ) := [2(trΦ)² − 3tr(Φ²)]²
   = 81(a² − 2|b|²)²` taken as the *ansatz form*, the zero-locus
   `V(Φ) = 0` is exactly the codimension-1 surface
   `a² = 2|b|²`, equivalently the Koide A1 relation
   `(Σ m_i)² = (3/2) Σ m_i²` after the standard
   `(a, b) ↔ (m_i)` reparametrization. Uniqueness of the minimum on
   this surface is an algebraic property of the squared form.

These are the only two statements this note retains. Everything else
in the body of the note is either (a) descriptive landscape map of the
13-iteration investigation, or (b) downstream consequences that
inherit the ansatz admission.

**Explicit admission — `V(Φ) = 81(a² − 2|b|²)²` is an assumed ansatz.**
The quartic effective potential is **admitted** at this note. It is
not derived from `A1 + A2 + retained` (Cl(3) on Z³ + retained source
theorems). Concretely:

- The functional form `[2(trΦ)² − 3tr(Φ²)]²` is imported from the
  Koide-Nishiura EW-scalar program (Route B in §"The three closure
  routes" below). The choice of squaring the bilinear-in-trace
  combination, the absence of competing invariants (e.g.
  `(trΦ²)²`, `tr(Φ⁴)`, mixed terms), and the overall normalization
  `81 = 9²` are **postulates** of the ansatz, not consequences of
  Cl(3)/Z³ structure.
- No retained source theorem in the audit lane derives this potential
  from framework primitives. The audit verdict's repair sub-target
  ("a retained theorem plus runner deriving the quartic effective
  potential or block extremum from Cl(3)/Z^3") remains **open work**,
  not closed by this note.
- The five mechanism attempts listed in §"Open physical bridge" (W[J]
  extremum, Coleman-Weinberg, Gaussian max-entropy, CV=1 /
  exponential max-entropy, SU(2)_L Clebsch-Gordan) all **fail** to
  recover the ansatz from primitives. That negative result is part
  of why the ansatz remains an admission rather than a theorem.

**What this note does NOT claim.**

- It does **not** claim an axiom-native derivation of the
  charged-lepton Koide relation from Cl(3) on Z³.
- It does **not** claim `V(Φ) = 81(a² − 2|b|²)²` is forced by
  framework primitives or by any retained source theorem.
- It does **not** elevate the 9 "equivalent expressions for A1 = 1/2"
  listed in §"Rigorously established" to retained status; those are
  documented coincidences whose load-bearing status depends on the
  same admitted ansatz or on the separate Route A primitive proposal.
- It does **not** retain Routes A, B, or C of §"The three closure
  routes" as closed; those remain open proposals.

**Tier.** `bounded_theorem` with retained content restricted to items
(1) and (2) above. Status authority remains independent audit lane
only. No package-control-plane wiring changes are made by this
repair; this is a narrowing of claim_scope on an already-bounded
note.
**Claim scope (post-2026-05-18 narrowing):** the load-bearing content
of this note is **a conditional variational route to the Koide A1
relation**: the Koide-Nishiura quartic effective potential `V(Φ)`
has a unique minimum at A1; four Q-formulas converge at `n = 3` via
`3! = 6`; A1 ⟺ coefficient-of-variation = 1; and the assorted
support runners listed in the runner table. This note **does NOT**
claim an **axiom-native derivation** of the charged-lepton Koide
relation from `Cl(3)` on `Z^3`; the quartic potential / block-extremum
machinery is admitted as the variational framework, not derived from
the framework axioms. The audit verdict's repair sub-target ("a
retained theorem plus runner deriving the quartic effective potential
or block extremum from Cl(3)/Z^3") remains separate open work.
**Status authority:** independent audit lane only.
**Iterations:** 13 investigation iterations across multiple sessions

## Work delivered

### New runners on working branch (6 A1-focused + 1 δ verification)

| Runner | PASS | Contribution |
|---|---|---|
| `frontier_koide_a1_quartic_potential_derivation.py` | 5/5 | Koide-Nishiura V(Φ) unique minimum at A1 |
| `frontier_koide_a1_n3_structural_uniqueness.py` | 5/5 | Four Q-formulas converge at n=3 via 3! = 6 |
| `frontier_koide_a1_cv_equals_one.py` | 4/4 | A1 ⟺ coefficient of variation = 1 |
| `frontier_koide_a1_block_democracy_max_entropy.py` | 5/5 | Block-democracy max-entropy principle explicit |
| `frontier_koide_a1_weyl_vector_kostant_coincidence.py` | 6/6 | Three-way match at 1/2 via Kostant |
| `frontier_koide_a1_a2_weyl_double_match.py` | 8/8 | A_1 AND A_2 Weyl vectors both match |
| `frontier_koide_a1_lie_theoretic_triple_match.py` | 10/10 | A1 = `|ω_{SU(2)_L, fund}|²` identified |
| `frontier_koide_a1_yukawa_casimir_identity.py` | 9/9 | `T(T+1) − Y² = 1/2` unique to Yukawa participants |
| `frontier_koide_a1_clifford_dimension_ratio.py` | 6/6 | A1 = dim(spinor)/dim(Cl⁺(3)) cleanest form |
| `frontier_koide_a1_spinor_normalization_proof_attempt.py` | 4/5 | 5th bridge mechanism tested, fails |
| `frontier_koide_radian_bridge_numerical_verification.py` | 3/3 | Radian-bridge empirically forced |

### Imported review-branch theorems (verified passing)

- `frontier_koide_frobenius_isotype_split_uniqueness.py` (SUPPORT_CHAIN=TRUE)
- `frontier_koide_kappa_block_total_frobenius_measure_theorem.py` (16/16 PASS)
- `frontier_koide_kappa_spectrum_operator_bridge_theorem.py` (9/9 PASS)
- `frontier_koide_peter_weyl_am_gm.py` (22/22 PASS)

### Documentation

- `KOIDE_A1_DERIVATION_STATUS_NOTE.md` — 6 closure routes
- `KOIDE_A1_LOOP_INVESTIGATION_SUMMARY.md` — iter-by-iter summary
- `KOIDE_A1_PHYSICAL_BRIDGE_ATTEMPT_2026-04-22.md` — 4 bridge mechanisms
- `KOIDE_A1_CLOSURE_RECOMMENDATION_2026-04-22.md` — Route A/B/C analysis
- `KOIDE_A1_LOOP_FINAL_STATUS_2026-04-22.md` — this note

## Theoretical status

### Rigorously established (RETAINED + /loop work)

1. **δ = 2/9 via AS/APS** (RIGOROUS, retained + textbook)
2. **Internal AM-GM chain for A1** (RIGOROUS, review branch theorem):
   E_+, E_⊥ forced unique Frobenius-orthogonal projections; AM-GM
   extremum at E_+ = E_⊥ = κ=2 = A1
3. **Spectrum-operator bridge identity** `a₀² − 2|z|² = 3(a² − 2|b|²)`
   (RIGOROUS, review branch)
4. **9 equivalent expressions for A1 = 1/2** (documented in /loop):
   - Pure Clifford dim ratio `dim(spinor)/dim(Cl⁺(3))`
   - Casimir difference `T(T+1) − Y²` (unique to L doublet + Higgs)
   - Lie-theoretic weight squared `|ω_{A_1, fund}|²`
   - ...and 6 others
5. **Radian-bridge postulate empirically forced** (this /loop iter 13):
   Only δ = η (numerically) matches PDG; standard Berry
   convention δ = 2π·η gives negative eigenvalue

### Open physical bridge (NOT CLOSED by any /loop attempt)

**Lemma needed**: the physical charged-lepton packet extremizes
`S_block = log E_+ + log E_⊥` (equivalently, lies at A1/κ=2).

**5 mechanism attempts all fail**:
1. W[J] = log|det D| extremum: wrong answer (|b|/a ≈ 3.3)
2. Coleman-Weinberg 1-loop V_CW: extremum at uniform eigenvalues (Q=1/3)
3. Gaussian max-entropy fixed Frobenius: ⟨a²⟩ = ⟨|b|²⟩ not 2|b|²
4. CV=1 / exponential max-entropy: continuous ≠ discrete 3-point
5. SU(2)_L Clebsch-Gordan normalization: CG same for all y_{αβ}

**Additional findings**:
- 1-loop QFT gauge contributions: uniform sign, cannot give T(T+1) − Y²
  structure
- Instanton corrections: exp(-32π²) ~ 10⁻¹³⁸ suppressed
- MRU SO(2)-quotient route demoted on review branch

## The three closure routes

**Route A (RECOMMENDED)**: Adopt block-total extremum as retained
primitive. Equivalent statements all derive from retained
CL3_SM_EMBEDDING:
- `|b|²/a² = dim(spinor)/dim(Cl⁺(3))`
- `|b|²/a² = T(T+1) − Y²` for Yukawa participants
- `|b|²/a² = |ω_{A_1, fund}|²` (Kostant)

9 natural quantities all equal 1/2 — strongest structural evidence.

**Route B**: Import Koide-Nishiura V(Φ) = [2(trΦ)² − 3tr(Φ²)]² into
retained EW-scalar lane. A1 as VEV minimum via SSB. Standard QFT.

**Route C**: Novel QFT mechanism (anomaly, topological, asymmetric
measure). Open research.

## Handoff

The investigation has produced a comprehensive landscape map. Further
progress now depends on theoretical bridge work, not more iterative
numerical verification.

For review, start with:
- `docs/CHARGED_LEPTON_KOIDE_NOTE_2026-04-18.md`
- `docs/KOIDE_A1_DERIVATION_STATUS_NOTE.md`
- `docs/KOIDE_A1_CLOSURE_RECOMMENDATION_2026-04-22.md`
