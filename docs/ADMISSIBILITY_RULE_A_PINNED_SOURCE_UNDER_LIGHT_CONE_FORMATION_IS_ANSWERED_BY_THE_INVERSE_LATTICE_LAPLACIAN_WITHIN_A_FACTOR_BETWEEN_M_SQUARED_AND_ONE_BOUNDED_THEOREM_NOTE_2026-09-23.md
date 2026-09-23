---
claim_id: admissibility_rule_a_pinned_source_under_light_cone_formation_is_answered_by_the_inverse_lattice_laplacian_within_a_factor_between_m_squared_and_one_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "WITHIN the formation reading of the Record axiom with block 90's supplied light-cone clause (a record forms from the seven records of the previous level around it, block 19's rule on the sphere), with a uniform field eps and a source h pinned at one site added to the rule's argument; the level-to-level chain on the 3D torus of even side; reversibility exact on rings with symbolic weights; the response identities exact on the doubled ring of four; the upper bound by block 90's Gaussian domination (open PR), with exact instances on the smallest ladder; the lower bound by a rotation-derivation inequality for the sphere menu, its algebra exact; the passage to infinite volume and the positivity of the spontaneous direction not proved here; the mode-by-mode response executed only"
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_pinned_source_under_light_cone_formation_inverse_lattice_laplacian_within_m_squared_and_one_2026_09_23.py
---

# A pinned source under light-cone formation is answered by the inverse lattice Laplacian within a factor between m² and one

**Date:** 2026-09-23
**Type:** bounded_theorem
**Status:** bounded-support (exact reversibility with a source, response identities, and a two-sided bound on the response at every wave vector and every coupling; infinite volume by limits; nothing adopted or registered; unaudited)

This note works within the formation reading of the Record axiom with the supplied light-cone clause of block 90, with a source pinned at one site; it reports how the records of a level answer the source, between two bounds; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 90 (open PR #8692) proved that light-cone formation is reversible and that its long-time law keeps a common record direction in 3+1 for `β > 0.5905`. The gravity node of this campaign (blocks 29 and 35) asks what kernel carries a source's influence through the records; blocks 29 and 35 found, for the static law and for level-ordered formation, that it is not simply the inverse lattice Laplacian. Here a source is held at one site: at every level, the record forming there feels an extra pull `h` added to its seven predecessors (weight `e^{β s'·(h_x(s) + h)}`). The question is how the other records answer.

1. **A source keeps formation reversible (T1).** With a uniform field `ε` everywhere and the source `h` at one site, the chain still satisfies detailed balance. Its long-time law is one level of block 90's doubled-graph ferromagnet with the field on every vertex and the source on **both** vertices of the pinned site, the level below and the level above. Exact on rings with symbolic weights.
2. **Response is a covariance (T2).** So the stationary response of a level's records to the source equals `β` times their covariance with the pinned site's two records. In block 90's bilayer labels those two records are the two slabs at the site. The response is `2β` times the covariance of the slabs' mean `S_+`, and in wave vectors `R̂(k) = 2β N⁻¹⟨|Ŝ_+(k)|²⟩`. Exact on the doubled ring of four at every site and wave number.
3. **The window (T3).** For every even side `L`, every `β`, every uniform field `ε ≥ 0` along `e₀`, and every `k ≠ 0`, the response transverse to `e₀` satisfies

   `⟨m⟩² / (⟨P_b⟩E(k) + ε⟨m⟩)  ≤  R̂_⊥(k)  ≤  1/E(k)`,  `E(k) = 6 − 2Σ_j cos k_j`.

   Here `⟨m⟩` is the stationary mean record direction along `e₀`, and `⟨P_b⟩ ≤ 1` is the correlation `s^x s^x' + s^z s^z'` of a record with one of its displaced predecessors. The upper bound is block 90's infrared bound. The lower bound comes from integrating the rotation symmetry by parts and applying Cauchy–Schwarz. Because the weights `1 − cos k·x` are nonnegative, the window carries over to potential differences: `R(0) − R(x) = N⁻¹Σ_{k≠0}(1 − cos k·x)R̂(k)` lies between the same sums of the two bounds; the upper one is `Γ(x) = N⁻¹Σ_{k≠0}(1 − cos k·x)/E(k)`, the drop of the inverse lattice Laplacian's kernel.
4. **So the kernel is the inverse lattice Laplacian, with its strength bracketed.** Let `L → ∞` and then `ε ↓ 0` along a sequence on which `⟨m⟩` and `⟨P_b⟩` have limits `m*` and `P_b*`. Every limit point of `R̂_⊥(k)` lies between `m*²/(P_b* E(k))` and `1/E(k)`, and every limit of `R(0) − R(x)` between `(m*²/P_b*)Γ_∞(x)` and `Γ_∞(x)`. This holds at every wave vector, not only at small ones. That `m* > 0` above block 90's `0.5905` is the standard passage from long-range order to a spontaneous direction. It is named and not re-proved here. In position space, a held source is surrounded by the inverse lattice Laplacian's kernel (the `1/r` potential of a point source on `Z³`) times a factor between `m*²/P_b*` and `1`.
5. **Executed.** My own two-copy simulator (a small uniform field `ε = 0.02`, a source small enough for linear response) measures `R̂(k)E(k)` shell by shell on `16³` planes. At every shell and every `β` tried it lies inside the window, and close to its floor: the measured response is `1.04`, `1.01` and `1.004` times the lower bound at `β = 1, 2, 3`, and at most `0.98` of the upper bound. So the answer is very nearly `⟨m⟩²/(⟨P_b⟩E(k) + ε⟨m⟩)` at every wave vector. The probes' position-space ratios at `r = 1…4` (planes 32 to 64, `β = 1…12`) all lie between `m²` and `1`. The probes' "linear prediction" `h/(βE(k))` is exactly the upper bound, since their source enters as `e^{s'·h}`. The gain-one linear model gives `A(7β)/E(k)`, below the measured values.
6. **What was already known, and what is new.** For the static sphere law this two-sided window is block 19's transverse channel (PR #8153, the G-series), and block 20 (PR #8154) runs its lower side at zero field against the long-range-order parameter itself. Block 29's measured normalization, 0.9 to 1.0 of the infrared bound, sits in it. New here: T1–T2, which make the formation law's own answer to a held source an equilibrium covariance of block 90's bilayer, so the window applies to records that form; the sharper floor with `⟨P_b⟩` in place of `1`; and the measurement that the floor is nearly attained. A zero-field form in terms of block 90's long-range-order parameter would follow by block 20's argument applied to the bilayer; it is not carried out here.

In plain terms: hold one site's forming records under a steady extra pull, and watch how the records around it lean in answer. Wave by wave, the lean has exactly the shape of the lattice's own inverse Laplacian, which is the `1/r` potential of a point source. Its strength is pinned between two numbers that the records themselves set: from below by how well they are aligned (squared) over how stiffly neighbouring records hold together, from above by one. Measured, it sits at the bottom of that window, within a few per cent.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "the gravity node's kernel under the owner's reading (blocks 29, 35; memory 'Formation in 3+1 lead': the probes' source-potential scans found the inverse lattice Laplacian's kernel around a held source under light-cone formation, executed only)"
source_of_blocker_text: 2026-09-23 harvest and block 90
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the response of light-cone formation to a held source lies between <m>^2/(<P_b>E(k) + eps<m>) and 1/E(k) at every wave vector; next: the two-source interaction at second order; whether R^(k)E(k) has a limit as k -> 0 (a sharper small-k statement); the level-ordered law, not reversible and not covered; an other-family referee"
conditional_surface_status: "T1 for every ring or torus and every menu by the symmetry of the stencil, checked on rings; T2 for every even L by the slab swap, checked on the ring of four; T3's upper bound for every even L and every menu by block 90's Gaussian domination, checked on the smallest ladder; T3's lower bound for the sphere menu by the derivation inequality, its algebra checked; the infinite-volume statement by limits, with the positivity of m* a named standard step"
hypothetical_axiom_status: "the light-cone formation clause; the sphere menu and block 19's rule; the coupling beta; the held source and the uniform field; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Record axiom ("Records form"; permanence), the Admissibility axiom (one covariant nearest-neighbour rule), and the Lattice axiom. Block 90 (open PR #8692) supplies the light-cone clause, the doubled graph, the bilayer and Gaussian domination; block 19 (open PR #8153) the rule on the sphere and the infrared-bound machinery; blocks 29 and 35 (open PRs #8173, #8180) the gravity node's question. Nothing is adopted here.

- **The clause with a held source (supplied).** The record at `(t + 1, x)` forms with density proportional to `exp(β s'·(h_x(s) + ε + h[x = x₀]))`, `h_x(s)` the sum of the seven records below `x`, `ε` a uniform field along `e₀`, `h` the held source.
- **Response.** `R(x − x₀) = ∂⟨s^α(x)⟩/∂h^α` at `h = 0` in the stationary law, `α` transverse to `e₀` (any `α` when `ε = 0`); `R̂(k) = Σ_x e^{−ik·x}R(x)`, `k ≠ 0`.
- **Bilayer labels.** Block 90's relabelling `(x, a) ↦ (x, a ⊕ parity(x))`; slab fields `S_0`, `S_1`; `S_± = (S_0 ± S_1)/2`.
- **`⟨m⟩`** the stationary mean record direction along `e₀` (the same on both levels by the level swap); **`⟨P_b⟩`** the stationary mean of `s^x s^x' + s^z s^z'` over a bond joining a record to a displaced predecessor (the same on all such bonds by the lattice's symmetries), `z` along `e₀`.

The response-equals-covariance identity for a reversible chain is the fluctuation–response relation of equilibrium statistical mechanics (Kubo; for Markov chains, the Agarwal form); the upper bound is the infrared bound of Fröhlich, Simon and Spencer; the lower bound is the classical form of the Bogoliubov inequality used in the Mermin–Wagner argument; the bracketing of the transverse response by the squared magnetization and the stiffness is the Goldstone–Josephson relation's rigorous side; the passage from long-range order to a spontaneous magnetization is Griffiths' (1966). The idea of measuring the response to a held source under formation is the probes' (`formation_response.py`, the scans `X:source-potential`, 2026-09-19 to 22), by one model family and unrefereed. None is used as authority; every step is re-derived or checked here.

## Prior art and what is new

Block 19 (PR #8153) proved the static sphere law's transverse channel two-sided, `(M²/3)²/(βE(k)) ≤ lim inf u(k) ≤ 1/(βE(k))`, with the Bogoliubov inequality run at zero field against the long-range-order parameter; block 20 (PR #8154, closed and archived) made that lower side dimension-free and used it for planes and lines. Blocks 29 and 35 measured and derived kernels for the static law and for level-ordered formation. The probes measured the response to a held source under light-cone formation and found the lattice Green function at about 0.91 to 0.99 of their linear prediction. New here, inside the framework's vocabulary: the formation law's own response as an equilibrium covariance of the bilayer (T1–T2), so that block 19's window applies to records that form; the window in the bilayer's form with the sharper `⟨P_b⟩`; the identification of the probes' linear prediction with the upper side; exact finite checks of every identity; and a mode-by-mode measurement by independent code that finds the floor nearly attained.

## Exact target and obligation graph

Target: the kernel by which light-cone formation answers a held source. Obligations: (O1) the chain with a source stays reversible; (O2) response as a covariance; (O3) an upper bound; (O4) a lower bound; (O5) the comparison with the linear model and the probes. T1–T4 discharge O1–O5.

## Theorem T1 — a held source keeps formation reversible

*Statement.* For a symmetric past, any menu, a uniform field `ε` and a source `h` at `x₀`, the chain satisfies detailed balance with `π(s) ∝ exp(βε·Σ_x s_x + βh·s_{x₀}) Π_x Z(h_x(s) + ε + h[x = x₀])`, which is the level marginal of `μ ∝ exp(β Σ_{edges} s·s' + βε·Σ_{vertices} s + βh·(s_{(x₀,0)} + s_{(x₀,1)}))` on the doubled graph.

*Proof.* `π(s)P(s'|s) = exp(βA(s', s) + βε·(Σs + Σs') + βh·(s_{x₀} + s'_{x₀}))` with `A` symmetric for a symmetric past (block 90 T1). Integrating `s'` out site by site gives `π`. Family B checks detailed balance for every pair on a ring of four (two values) and a ring of three (four six-axis contents), with `t = e^β`, `v = e^{βε}`, `u = e^{βh}` symbolic, and the marginal for every configuration. ∎

## Theorem T2 — response is a covariance, and a covariance of the slabs' mean

*Statement.* `∂⟨f⟩_π/∂h^α = β Cov_μ(f, s^α_{(x₀,0)} + s^α_{(x₀,1)})`. For `f = s^α_{(x,0)}`: `R(x − x₀) = 2β Cov(S^α_+(x), S^α_+(x₀))`, so `R̂(k) = 2β N⁻¹⟨|Ŝ^α_+(k)|²⟩` for `k ≠ 0`. A level's structure factor is `N⁻¹⟨|ŝ_0(k)|²⟩ = N⁻¹⟨|Ŝ_+(k)|²⟩ + N⁻¹⟨|Ŝ_−(k + (π,π,π))|²⟩`, with no cross term.

*Proof.* Differentiate `π_h` from T1. The pinned site's two vertices are the two slabs at `x₀` (their parities differ), so their sum is `2S_+(x₀)`; a level's record is `S_+ + (−1)^{parity} S_−`, and the slab swap, a symmetry of `μ` (the field sits on both levels), is odd on `S_−` and even on `S_+`. Family C checks the derivative against the covariance at every site of the doubled ring of four (symbolic `t`), the slab form at every site, and the branch decomposition with its vanishing cross term at every wave number. ∎

## Theorem T3 — the window

*Statement.* For every even `L`, `β > 0`, `ε ≥ 0` and `k ≠ 0`, with the sphere menu:

`⟨m⟩² / (⟨P_b⟩E(k) + ε⟨m⟩)  ≤  R̂_⊥(k)  ≤  1/E(k)`.

The upper bound holds for every menu. The weights `1 − cos k·x` are nonnegative, so `R(0) − R(x) = N⁻¹Σ_{k≠0}(1 − cos k·x)R̂(k)` lies between the same bounds summed with those weights.

*Proof.* Upper: block 90's Gaussian domination gives `⟨(s^α, φ)²⟩ ≤ 1/(βλ)` for every normalized eigenvector `φ` of the bilayer's Laplacian; with `φ = (2N)^{−1/2}e^{ik·x}(1, 1)`, `λ = E(k)`, this is `N⁻¹⟨|Ŝ^α_+(k)|²⟩ ≤ 1/(2βE(k))`, and T2 gives `R̂ ≤ 1/E`. With a uniform field the reflections still act as symmetries, so the bound persists. Lower: let `D = Σ_u c_u L_u`, with `L_u` the rotation of the record at `u` about the axis perpendicular to `e₀` and to `α`, and `c_u = e^{ik·x_u}`. Integration by parts on the sphere gives `⟨DF⟩ = β⟨F DH⟩`, and applying it twice gives `⟨|DH|²⟩ = β⁻¹⟨D̄DH⟩`. Cauchy–Schwarz then gives `|⟨DF⟩|² ≤ β⟨|F|²⟩⟨D̄DH⟩`. With `F = Σ_u c̄_u s^α_u = 2Ŝ^α_+(k)` we have `DF = Σ_u s^z_u` and `⟨DF⟩ = 2N⟨m⟩`. Also `D̄DH = Σ_{edges}|c_u − c_v|²P_{uv} + εΣ_u s^z_u`. The rungs join equal phases and carry no weight. Every slab bond carries the same `⟨P_b⟩` by the lattice's symmetries, and the slab bonds sum to `2N E(k)`. Family D checks exact instances of the upper side on the Ising ladder: Gaussian domination for 2315 fields at two couplings, and the bound at every wave number with `β` bounded by rationals. Family E checks the derivation algebra symbolically, the sphere integrals, the stiffness sum on `4³` (and `N E(k)` on a single torus), and the bounds' algebra. ∎

## Theorem T4 — the linear comparator and the probes' prediction

*Statement.* The gain-one linear model with the rule's gain at the aligned configuration, `A(7β)/7`, and predecessor average `1 − E(k)/7` answers `A(7β)/E(k)`, with `A(κ) = coth κ − 1/κ`. The probes' linear prediction, `(h/(7β))·7/E(k)` with the source entering as `e^{s'·h}`, is the upper bound `h/(βE(k))` itself.

*Proof.* Stationary mean of `θ' = (1 − E/7)θ + (A/7)h`; unit conversion `h_probes = βh`. Family E. ∎

## Executed (supervisor control; floating point; evidence, not proof)

Controls in the pack (`specs/supervisor_control_block91_pinned_source.py`, output in `.out.txt`).

*W1 — the smallest ladder.* `2β N⁻¹⟨|Ŝ_+(k)|²⟩E_1(k)` is `0.004 … 0.006` at `t = 4` and `0.12 … 0.15` at `t = 9/4`: the instance sits well below its bound.

*W2 — the response mode by mode.* Two copies with common random numbers, both with the uniform field `ε = 0.02` along `e₀`, the second with the source at the origin, `16³`, 3000 levels, the last 2000 averaged; fixed axes (`m_z`, `⟨P_b⟩` with `x` the source's direction and `z = e₀`). Each entry is measured `R̂(k)E(k)` over the lower bound's `m_z²/(⟨P_b⟩ + εm_z/E(k))`, averaged over the shell; the upper bound is `1`:

| `β` | `m_z` | `⟨P_b⟩` | `|k| < 0.5` | `0.5–1` | `1–1.5` | `1.5–2.2` | `2.2–3.2` | `> 3.2` |
|---|---|---|---|---|---|---|---|---|
| 1 | 0.767 | 0.638 | 0.828 / 0.797 | 0.923 / 0.887 | 0.945 / 0.909 | 0.954 / 0.915 | 0.958 / 0.918 | 0.960 / 0.920 |
| 2 | 0.896 | 0.827 | 0.858 / 0.850 | 0.947 / 0.937 | 0.968 / 0.958 | 0.975 / 0.964 | 0.977 / 0.967 | 0.979 / 0.969 |
| 3 | 0.932 | 0.886 | 0.866 / 0.862 | 0.952 / 0.948 | 0.973 / 0.969 | 0.979 / 0.975 | 0.982 / 0.977 | 0.982 / 0.979 |

The source is `h = 0.1` (the rule's argument gains `βh`); `h = 0.05` gives the same numbers to three decimals. With `h = 0.5` at `β = 3` the source is 8 per cent of the local field, and every shell drops by about 0.5 per cent to just below the floor (`0.860 … 0.974`): a finite-source effect, not a failure of the bound. Without the uniform field the record direction wanders across a 16³ plane in 3000 levels (up to 55 per cent of the magnetization turns into the source's direction at `β = 2`), and a fixed-axis measurement then mixes in the longitudinal response; the window is stated with `ε > 0` for that reason.

*The probes' position-space ratios* (`X:source-potential`, light-cone past, source `h = 0.5` in their units, ratio to `h/(βE)` averaged over `r = 1…4`, planes 32 and 48 unless stated, two seeds):

| `β` | `m` | `m²` | ratio |
|---|---|---|---|
| 1 | 0.762 | 0.580 | 0.914 – 0.964 |
| 2 | 0.895 | 0.801 | 0.965 – 0.979 |
| 3 | 0.932 | 0.868 | 0.955 (plane 64) – 0.986 |
| 6 | 0.967 | 0.935 | 0.965 (plane 64) – 0.993 |
| 12 | 0.984 | 0.967 | 0.990 – 0.996 |

At `β = 3` the ratio does not move with the source's size (`h = 0.1 … 2`: `0.979 … 0.986`), as a linear response should not. The level-ordered past is not reversible and is not covered. Its ratios scatter from `0.918` to `1.060`, with a forward–backward asymmetry, and one exceeds the upper bound.

## No-Go Discipline Gate

The note's negative sentences: the level-ordered law is not covered; the gain-one linear model lies below the measured response.

### N1 — Routes by which the sentences could fail or mislead
1. *Infinite volume.* The window is exact in finite volume with `ε > 0`; the corollary takes limits along subsequences, and the positivity of `m*` above `0.5905` is the standard passage from long-range order, named and not re-proved.
2. *Finite sources.* The window is for the linear response; a source comparable to the local field answers less (the control's `h = 0.5` at `β = 3`).
3. *Transverse versus longitudinal.* The lower bound is for the response transverse to the ordering direction; the longitudinal response has no such lower bound here.
4. *Position space.* The window is mode by mode and for potential differences; it does not fix the coefficient of the `1/r` tail beyond the bracket.
5. *Provenance.* The question is the probes' (one model family, unrefereed); this block is by the same family. The exact checks are independent code.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The sphere menu for the lower bound; even tori; the aligned start and finite runs in the simulators.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | "Records form"; one covariant nearest-neighbour rule | yes (premise) |
| block 90 (open PR #8692) | the light-cone clause; reversibility; the bilayer; Gaussian domination | yes (the machinery) |
| block 19 (open PR #8153) | the sphere rule; the infrared-bound machinery; the static law's two-sided window (prior) | yes |
| block 20 (PR #8154, closed and archived) | the zero-field, dimension-free form of the lower side (prior) | no (placed) |
| blocks 29, 35 (open PRs #8173, #8180) | the gravity node's question and measurements | yes (placed) |
| the probes' `X:source-potential` scans | the measured ratios | no (evidence) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "a held source's response under light-cone formation lies between <m>^2/(<P_b>E(k) + eps<m>) and 1/E(k)" | executed: detailed balance with field and source for every pair on two rings; the marginal | executed: the response at every site against the covariance, both labellings; the stiffness sum over every edge | executed: the branch decomposition at every wave number; the ladder bound; control mode by mode | executed: Gaussian domination on the ladder; the derivation algebra; the bounds' algebra | T1–T3 for every even L with the stated scope; infinite volume by limits

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "The upper bound is the infrared bound and the lower bound is the classical inequality behind the no-order theorem in two dimensions; nothing is new." Reply: the content is that the formation law's own answer to a held source is a covariance of an equilibrium bilayer (T1–T2, exact), so both classical bounds apply to records that form; and that together they fix the kernel's shape at every wave vector and its strength to a window that the measurements fill. Second objection: "The window is wide at weak order." Reply: at `β = 1` it is `[m²/⟨P_b⟩, 1] = [0.92, 1]` away from the smallest wave vectors, and the measured response sits within 4 per cent of its floor.

### N8 — Cross-cycle echo
Block 29 measured the static law's kernel at 0.9 to 1.0 of the infrared bound; block 35 found the heat kernel in level time for level-ordered formation; here the light-cone law's answer to a held source is the inverse lattice Laplacian within `[m²/⟨P_b⟩, 1]`.

## Falsifiers

- A pair of configurations on a ring for which the chain with a field and a source violates detailed balance with the stated law.
- A site of the doubled ring at which the response differs from the covariance with the pinned site's two records.
- A field on the ladder with `Z(h) > Z(0)`, or a wave number where the ladder's response exceeds `1/E_1(k)`.
- A torus, coupling and wave vector with `R̂_⊥(k)` outside the window.

## Boundaries and non-claims

The light-cone clause, the sphere menu, block 19's rule, the source and the field are supplied; the level-ordered law is not covered; the infinite-volume statement is by limits with the positivity of `m*` a named standard step; the lower bound is transverse only; no statistical statement, no gravitational statement, no adoption.

## Imports
- `minimal_axioms`: the Record, Admissibility and Lattice axioms. Blocks 19, 29, 35 and 90 (open PRs): restated or used as machinery.
- Named standard imports at definition level: the fluctuation–response relation for reversible chains; reflection positivity, Gaussian domination and the infrared bound (block 90, after Fröhlich, Simon and Spencer); the classical Bogoliubov inequality (integration by parts on the sphere and Cauchy–Schwarz); Griffiths' passage from long-range order to a spontaneous magnetization (for the corollary only); partial sums of the exponential series as rational lower bounds; floating-point simulation for the control.

## Review record
Supervisor-run block, the thirty-ninth since the source-link direction opened; the formation lane; the third run on Claude Opus 5.5. The question came from the probes' source-potential scans and block 90; the bounds are the supervisor's derivation. Lens pass, in writing, by the supervisor: a foundations lens — the source and the field are supplied and enter the rule like the neighbours' sum, and the level-ordered law is kept apart; a rigour lens — every identity is checked exactly on the smallest instance (rings, the doubled ring, the ladder), the upper bound's machinery is exercised on the ladder with rational enclosures of `β`, and the lower bound's algebra is checked symbolically; the first form of the lower bound used `⟨P⟩ ≤ 1` bond by bond, and the sharper `⟨P_b⟩` form was added when the symmetry of the slab bonds was noticed. The control first appeared to violate the sharper floor at `β = 2` and `3`; two causes were found and removed in turn: without a uniform field the record direction wandered and a fixed-axis measurement mixed in the longitudinal response, and a source of 8 per cent of the local field answered nonlinearly. With `ε = 0.02` and `h = 0.1` (checked against `h = 0.05`) every shell lies in the window. Mutation census: eight mutations, each failing in its own family only. No independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_pinned_source_under_light_cone_formation_inverse_lattice_laplacian_within_m_squared_and_one_2026_09_23.py
```

Expected: `TOTAL: PASS=17 FAIL=0`.
