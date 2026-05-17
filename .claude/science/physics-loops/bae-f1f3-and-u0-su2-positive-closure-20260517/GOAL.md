# Goal — BAE F1-vs-F3 + u_0(SU(2)) positive-closure campaign

**Slug:** `bae-f1f3-and-u0-su2-positive-closure-20260517`
**Mode:** campaign
**Runtime:** 12h
**Target:** best-honest-status (positive closure if reachable; honest no-go/Path-B otherwise)
**Started:** 2026-05-17

## Two primary targets

### Target 1 — F1-vs-F3 canonical weighting selection (BAE residual) [HIGHEST LEVERAGE]

The Brannen Amplitude Equipartition `|b|²/a² = 1/2` pins specific Koide Q = 2/3 from the Brannen-Rivero parameterization `λ_k = a + 2|b|cos(arg(b) + 2πk/3)`. The 30-probe BAE campaign + PR #1174 honest Path B narrowing established:

- F1-extremum (multiplicity-weighted Frobenius measure) → kappa = 2 (MATCHES BAE)
- F3-extremum (rank-weighted (1,2) Frobenius measure) → kappa = 1 (FAILS BAE)
- Plancherel measure on Z/3Z, Born-rule operationalism, Jaynes max-entropy all select F3, not F1

Goal: find a canonical principle in retained A_min that selects F1 over F3. Routes:
- SUSY-style oscillator decomposition giving multiplicity weighting naturally
- Cl(3) bivector irrep on dim-2 spinors forcing multiplicity-weighted norm
- Plancherel on SU(2)/Cl(3)* (different group) giving F1
- Literature: published canonical extremal principles on circulant Hermitian operators

Honest outcomes accepted:
1. Positive closure: F1 selected by retained A_min-derivable principle → BAE forced → Q = 2/3 forced
2. Honest no-go (after N1-N8 Discipline Gate)
3. Path B: narrow scope to "given X assumed, F1 follows"

### Target 2 — Numerical u_0(SU(2)) value (g_2(v) chain residual)

PR #1273 retained the STRUCTURAL `N_G = 2` step. NUMERICAL u_0(SU(2)) requires SU(2) Monte Carlo, framework-native non-perturbative matching, or analytic strong-coupling. Open R1 residual per `EW_COUPLING_DERIVATION_NOTE.md` Part 3.

Routes:
- Analytic Lüscher-style mean-field tadpole derivation from Cl(3) bivector irrep + retained b_2 = 19/6
- Framework-native strong-coupling expansion at SU(2) Wilson plaquette
- Match to published SU(2) lattice u_0 + prove framework-internal route gives that value
- Use retained `alpha_s_tadpole_improvement_vertex_power_narrow_theorem` as template

Honest outcomes accepted:
1. Positive closure: u_0(SU(2)) = specific numerical value derivable from retained A_min
2. Path B: framework-native series truncated to known order with error bound
3. Honest gap: prove u_0(SU(2)) cannot derive from retained authorities alone

## Campaign rules

- A_min FIXED. No new axioms.
- No new repo vocabulary.
- Verify live ledger before citing.
- Mirror wave-2 narrow-rescope template.
- Audit-companion sympy with PASS/FAIL counts.
- No-Go Scrutiny Battery before any no-go ship.
- V1-V5 Promotion Value Gate before any retained-positive PR.
- Honest fallbacks always allowed.
- All work via PRs; review-loop salvages.
- Cycle-break work in parallel when natural cycles emerge.
