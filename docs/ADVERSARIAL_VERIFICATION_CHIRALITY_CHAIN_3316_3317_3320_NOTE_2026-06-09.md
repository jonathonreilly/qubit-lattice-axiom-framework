# Adversarial verification of the chirality chain (#3316/#3317/#3320) — algebra sound, three runner-checks overstated, causality/boost live in the admitted residual

**Date:** 2026-06-09
**Claim type:** bounded verification note (independent adversarial re-derivation; no new theorem, no status change).
**Claim boundary:** confirms the chain's sound core and pins where the PR runners over-state; does not alter the chain's verdict beyond scoping. Does not touch the firewalled `r=1/2`.
**Runner:** `scripts/adversarial_verify_chirality_chain_2026_06_09.py` (`PASS=7 FAIL=0`, 5 flags; finite-dim).

## Purpose

The chirality chain — #3316 (chirality gate = emergent-time keystone), #3317 (partner chirality = 4th Clifford gamma, decoupled from the magnitude corner), #3320 (massive Dirac field positive-energy + microcausal via T1) — is load-bearing for the spin-statistics tower that the RP drain is about to make auditable. This note re-derives its claims *independently* and tries to *refute* each, separating what is genuinely verified from what the PR runners assert.

## Confirmed SOUND (independent re-derivation)

- **Cl(3,1) gamma_5 chirality is genuine.** `{γ^μ, γ^ν} = 2η^{μν}` (full Clifford), and `γ_5 = iγ⁰γ¹γ²γ³` satisfies `γ_5²=I`, `tr γ_5 = 0`, `{γ_5, γ^μ}=0`. The partner chirality #3317(A)/#3320(MODE) claims is real. ✔
- **CAR is the unique bounded-below quantization.** With the vacuum constant kept, `Ĥ = E(a†a + b†b) − E` has eigenvalues `{−E, 0, 0, E}` (min `−E`, a finite shift); the Bose reorder gives `E(a†a − b†b)` with `min → −∞`. The statistics sign of the `b`-reorder is the engine. #3320(T1) is solid. ✔

## Three OVERSTATEMENTS in the PR runners

1. **BOOST covariance (#3320) is verified by a vacuous identity.** The runner checks `S⁻¹(m·I)S = m·I`. But `m·I` is **central**, so this holds for *any* invertible matrix — confirmed on a random non-boost `M`. The check verifies nothing. The genuine test is the mass-bilinear invariance `S†γ⁰S = γ⁰` (equivalently `S⁻¹γ^μ S = Λ^μ_ν γ^ν`); the canonical Dirac boost `exp(½η γ⁰γ³)` passes it. So boost-covariance is **true but un-verified by the check the runner ran**.
2. **MICROCAUSALITY (#3320) is only the equal-time precursor.** Spinor completeness `Σ_s(uu† + vv†) = I` gives the canonical **equal-time** anticommutator `{ψ_a, ψ†_b}=δ_{ab}` — a *necessary* condition. It is **not** microcausality, which is `{ψ(x), ψ̄(y)} = 0` for spacelike `(x−y)` and requires the Pauli–Jordan mode integral over the mass shell — a field construction the finite-dim single-momentum runner does not perform.
3. **The #3317 DECOUPLING rests on a hardcoded premise.** The Clifford-gamma-`e₄`-vs-species-`k₄`-corner *distinction* is sound (a 4×4 algebra generator vs a `2^d` momentum-doubler count — genuinely different objects). But the runner sets `has_k4_corner = False` by hand. The load-bearing claim — *continuous* emergent time supplies the gamma but **no** `k₄` doubler — is the **assumed premise (emergent-time continuity)**, not a derived result. If emergent time were a discrete 4th lattice direction, the corner would reappear and the decoupling would fail.

## Plus: the Koide overreach (already bounded)

#3316's "one keystone" framing additionally claims the Koide `Q=2/3` / generation chirality collapses into the Dirac chirality. It does not: `γ_5 = I₃⊗σ₃` is **generation-blind** (`[γ_5, Γ_χ⊗I]=0`), so it cannot supply the `Γ_χ`-anticommuting generation chirality `Q=2/3` requires. This is bounded by [`CHIRALITY_GATE_IS_TWO_INDEPENDENT_GATES_DIRAC_VS_GENERATION_SCOPING_NOTE_2026-06-08.md`](CHIRALITY_GATE_IS_TWO_INDEPENDENT_GATES_DIRAC_VS_GENERATION_SCOPING_NOTE_2026-06-08.md) (PR #3333).

## Net verdict

The chain's **algebra is sound** — the Cl(3,1) chiral grading and CAR positive-energy are genuine and independently confirmed. But **microcausality, genuine boost-covariance, and the decoupling are only partially supported**, and — the key point — the spacelike-causality and true-boost checks **live inside the residual the PRs already admit**: the OS→Wightman field construction on the emergent-time Hilbert space. So the chain's "positive-energy / microcausality CLOSES" should be scoped:

> **positive energy + the chiral algebra close at the finite-dim level; microcausality and boost-covariance close only *with* the admitted field delivery, where the Pauli–Jordan spacelike anticommutator and the `S†γ⁰S=γ⁰` covariance actually live.**

The residual is correctly *located* by the PRs; the "CLOSES" language slightly outruns what the finite-dim runners verify. No new axiom or import; no PDG load-bearing; verification only — the independent audit lane owns any status.
