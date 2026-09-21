---
claim_id: admissibility_rule_amplitudes_of_negative_energy_fall_like_the_others_and_source_the_opposite_field_a_negative_body_at_rest_has_a_largest_size_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clauses of blocks 53 to 56, 60 and 70 (open PRs #8568, #8570, #8571, #8573, #8590, #8602; not adopted): block 54's walk and its reduced form H = m sigma_1 + sigma_3 D, whose spectra are symmetric about zero; the clause that the phase is timed by the local clock (H_w = phi H phi, w = phi^2); block 55's ledger, under which the rate field's source is the amplitudes' energy density e_x = Re chi_x^dagger (H_w chi)_x; the static members of block 56 (simplest bond energy) and block 60 (curvature member). Blocks 55, 56 and 60 stated their theorems for positive energies. (T1) For every state, every rate field and every odd species n, the twin A_n psi of block 70 has e_x[A_n psi] = -e_x[psi] and the same site density at every site; on the reduced walk a real envelope with the content (1, -1) has e_x = -m w_x |chi_x|^2. Under block 55's law an amplitude of negative energy sources the opposite weak field; block 55's ledger identity does not use the sign. (T2) Block 55 T3's pulls stay matched for either sign when S = cE. A ray starting from rest accelerates at -w grad w whatever the sign of its energy, so: two positive bodies attract; two negative bodies repel; of a mixed pair the positive body recedes and the negative one follows, both accelerating the same way with the pulls summing to zero. Rays of negative energy follow the paths of rays of positive energy (p -> -p). (T3) In block 60's curvature member one body at rest of either sign, mu = m/(8K): r = (1 + 4 g_0 mu)^(1/2), Q = (r - 1)/(2 g_0), P = Q/r, chi_0 = (1 + r)/2, w_0 = 1/r. A negative body has a static field with positive rates iff m > -2K/g_0; then w >= 1 everywhere, its clock rate (1 + g_0 m/(2K))^(-1/2) grows without bound as m decreases to the bound, the box's ledger stays above -4K/g_0, and bending over fall, 1 + 2r/(1 + r), falls from 2 to 1. The quadratic's second root solves both field equations with a negative rate at the body. At the bound the unit-source potential is a zero mode of the rates' operator and no static rates exist. For many bodies, positive static rates exist iff the rates' operator -Delta + Q/chi with the walls held is positive definite. Block 56's member has the same zero mode at m = -2/(gamma g_0). (T4) The symbol of the walk's positive-energy projector is discontinuous at each of the eight zeros, so no rule of finite or summable reach that commutes with translations keeps exactly the positive energies; with a rest energy the symbol is continuous but not a trigonometric polynomial. EXECUTED, NOT CLAIMED: two walkers on a ring sourcing the field that times them - positive pair: displacements +12.5, -6.0 (attraction); mixed pair: -16.7, -9.9 (the chase); negative pair: -21.3, +11.3 (repulsion); wave-vector changes cancel to 1.5e-6 and the ledger holds to 2e-10 in all three. NOT claimed: that amplitudes of negative energy are present or absent; a reading in which they are re-described (it would need more than one amplitude); anything about fields that move; any statistical statement; any gravitational statement; any adoption."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_amplitudes_of_negative_energy_fall_like_the_others_and_source_the_opposite_field_2026_09_21.py
---

# Amplitudes of negative energy fall like the others and source the opposite field; a negative body at rest has a largest size

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact statements about supplied clauses; nothing adopted or registered; unaudited)

This note works within supplied clauses for amplitudes on the lattice timed by local clocks and for a ledger that makes their energy density the source of the rate field; it reports what those clauses say about amplitudes of negative energy; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

The walk of block 54 has as many states of negative energy as of positive energy. Block 70 (open PR #8602) showed that they are exact twins as *test bodies*: the same fields, the same movie of site densities. Blocks 53–60 stated every theorem about *sources* for positive energies. This note asks what the same clauses say when the energy is negative.

1. **Twins source oppositely** (T1). The twin's energy density is minus the original's at every site and every time. Under block 55's ledger the source *is* the energy density, so a negative amplitude raises the rates around it where a positive one lowers them.
2. **Everything falls towards slow clocks, whatever its own sign** (T2). So two positive bodies attract; two negative bodies **repel**; and of a mixed pair the positive one recedes while the negative one follows — both accelerate the same way, with the pulls exactly matched and the ledger exactly kept. Executed on a ring: displacements `+12.5, −6.0`; `−21.3, +11.3`; and `−16.7, −9.9` for the mixed pair.
3. **A negative body at rest has a largest size** (T3). In the curvature member the clock at a body of bare energy `m` runs at `w_0 = (1 + g_0 m/(2K))^{−1/2}` — one formula for both signs. For `m > 0` it is slow and never stops (block 60). For `m < 0` it is fast, and as `m` decreases to `−2K/g_0` it grows without bound; beyond, there is no static field. The quadratic's other root solves the equations with a *negative* rate at the body.
4. **No rule of finite reach keeps only the positive energies** (T4). The operator that does is discontinuous in the wave number at each of the walk's eight zeros.

In plain terms: every walker has a twin of negative energy. The twin falls exactly as the original does. As a source it does the opposite — clocks run fast around it, and since everything falls towards slow clocks, everything flees it, its own kind included. Set one beside an ordinary body and the ordinary body runs, the twin chases, and the books still balance. The clauses supplied so far do not say which amplitudes are present, and no short-range rule can sort them.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 70 (PR #8602), next_trace_action: 'what a ledger that counts energy does with sixteen branches'; block 55 T4(b) and block 60 T4 presume positive energies."
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the owner's fork: which amplitudes are present - a clause about the content, not about the field; candidates to examine: a reading with more than one amplitude; a ledger whose total is zero; next derivations: many bodies of both signs at rest (the criterion of T3(d) in examples), fields that move"
conditional_surface_status: "T1 exact for every state and rate field; T2 exact for point bodies in the weak field and for rays; T3 exact for one body at rest in a box with held walls, with the criterion for many bodies; T4 exact for the walk and its reduced form"
hypothetical_axiom_status: "block 54's walk timed by local clocks; block 55's ledger; the static members of blocks 56 and 60; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom, the Qubit axiom's one-site algebra, and the memo's silence on amplitude dynamics. Blocks 53–56, 60, 70 (open PRs) supply the objects.

- **Energy density.** `e_x = Re χ_x†(H_wχ)_x`, `H_w = φHφ`; block 55 T1: `∂⟨H_w⟩/∂u_x = e_x`, for every amplitude.
- **Block 55's law.** `∂F/∂u_x = −(e_x − μ)`; weak field of a point body `−γSG_0`; pull on a body `−E ×` (central difference of the others' fields); matched pulls iff `S = cE`.
- **Block 60's member.** Bodies at rest with `e = mw`; `χ = √ℓ`, `N = wχ`; field equations `(Δχ)_z = −μ_z/χ_z`, `(ΔN)_z = (Q_z/χ_z)N_z`, `Q_z = μ_z/χ_z`, walls at `χ = N = 1`; `g` the unit-source potential of the box, `g_0` its value at the body.
- **Twins.** `A_n = ΘV_n` of block 70, `n` odd.
- **Rates' operator.** `L = −Δ + Q/χ` on the interior sites, walls held.

Negative-energy solutions of a first-order wave equation, and the reading of their absence as a filled set of levels, are Dirac's; the motion of a pair of bodies of opposite mass is Bondi's; rays are governed by the equations of Hamilton; a symmetric matrix with non-positive off-diagonal entries and a connected graph has a positive lowest mode (Perron and Frobenius). Nothing is used as authority.

## Prior art and what is new

Every qualitative statement here is classical. New, inside the framework's vocabulary: that block 55's ledger and block 60's curvature member, stated for positive energies, extend verbatim and what they then say — the exact opposite source for the exact twin; the closed form `w_0 = (1 + g_0 m/(2K))^{−1/2}` for both signs, with a bound for negative bodies and a zero mode at it; and that the supplied clauses contain no statement about which amplitudes are present. No gravitational claim is made.

## Exact target and obligation graph

Target: what the supplied clauses say about amplitudes of negative energy. Obligations: (O1) as sources; (O2) pairs; (O3) the strong field; (O4) whether a rule of the supplied kind could exclude them. T1–T4 discharge them.

## Theorem T1 — twins source oppositely

*Statement.* (a) For every state, every positive rate field and every odd `n`: `e_x[A_nψ] = −e_x[ψ]` and `|A_nψ|²_x = |ψ|²_x` at every site. (b) On the reduced walk with any rate field, an amplitude with a real envelope and the content `(1, −1)` has `e_x = −m w_x|χ_x|²` at every site. (c) Block 55 T1 and T2 hold for amplitudes of either sign; under block 55's law the twin of an amplitude is the source of the opposite weak field.

*Proof.* (a) Block 70 T1(d): `V_n` multiplies the energy density by `s_n = −1`. `Θ` commutes with `H_w`, so `(Θψ)†_x(H_wΘψ)_x = (σ_2ψ̄)†_x(σ_2\overline{H_wψ})_x` is the complex conjugate of `ψ†_x(H_wψ)_x`, with the same real part. Both maps are unitary or antiunitary site by site. (b) `(1, −1)σ_3(1, −1)ᵀ = 0` and `(1, −1)σ_1(1, −1)ᵀ = −2`. (c) The proofs of block 55 T1, T2 use that `⟨H_w⟩` is a quadratic form in `φ`, not its sign. ∎

Block 55 T4(b) argued from `⟨H_w⟩ > 0` that the unit of rate cannot be varied; that presumption is a presumption about which amplitudes are present.

## Theorem T2 — pairs

*Statement.* (a) For two point bodies with `S = cE`, `c > 0`: the pull on `A` is `γcE_AE_B∇_cG_0(x_A − x_B)`, and the two pulls sum to zero for any signs of the energies. (b) A ray starting from rest obeys `d²x/dt² = −w∇w` whatever the sign of its energy. Hence `A` accelerates towards `B` iff `E_B > 0`: two positive bodies attract; two negative bodies repel; of a mixed pair the positive body recedes and the negative body follows. (c) If `(x(t), p(t))` is a ray of `w(x)ε(p)`, `ε` even, then `(x(t), −p(t))` is a ray of `−w(x)ε(p)`.

*Proof.* (a) Block 55 T3's formula; it is antisymmetric under exchange for every sign. (b) For `±w(m² + sin²p)^{1/2}` at small `p`: `dx/dt = ±wp/m`, `dp/dt = ∓m∇w`, so `d²x/dt² = −w∇w` at `p = 0`; the two signs cancel. (c) `∂(−ε)/∂p` at `−p` equals `∂ε/∂p` at `p`, and `d(−p)/dt = −(−ε)∇w`. ∎

The mixed pair's motion keeps the momentum and the ledger: the negative body's momentum points against its velocity.

## Theorem T3 — a negative body at rest in the curvature member

*Statement.* One body at rest at a site of a box with held walls, `μ = m/(8K)` of either sign. (a) The lengths' equation has real solutions iff `1 + 4g_0μ ≥ 0`; they are `χ = 1 + Qg`, `Q = (±r − 1)/(2g_0)`, `r = (1 + 4g_0μ)^{1/2}`. For `μ < 0` both have positive lengths; for `μ > 0` only the upper sign has (block 60's solution). (b) For `r > 0` the rates are `N = 1 − Pg`, `P = Q/(±r)`. With the upper sign: `χ_0 = (1 + r)/2`, `w_0 = 1/r`, all rates positive; for `μ < 0`, `w ≥ 1` everywhere. With the lower sign `N` at the body is `−(1 − r)/(2r)` and the rate there is `−1/r < 0`, for `0 < r < 1`. (c) At `r = 0`, `Q/χ_0 = −1/g_0`, `Lg = 0`, and the rates' equation has no solution. Hence a negative body at rest has a static field with positive rates iff `m > −2K/g_0`. (d) For bodies of any signs with positive lengths, positive static rates exist iff `L` is positive definite. (e) The ledger of the box is `M = 8KQ = (4K/g_0)(r − 1) > −4K/g_0`; far from the body the lengths carry `2Q` and the rates `P + Q`, and bending over fall is `1 + 2r/(1 + r)`: between 2 and 3 for a positive body (block 60), between 1 and 2 for a negative one. (f) In block 56's member `φ_0 = 1/(1 + γmg_0/2)`; at `m = −2/(γg_0)` the same `g` is a zero mode.

*Proof.* (a) Off the body `Δχ = 0`, so `χ = 1 + Qg` with `Q(1 + Qg_0) = μ`; for `μ < 0`, `Q < 0` and `g ≤ g_0` give `χ ≥ 1 + Qg_0 = (1 ± r)/2 > 0` since `r < 1`; for `μ > 0` the lower sign has `χ_0 = (1 − r)/2 < 0`. (b) `N = 1 − Pg` with `P = (Q/χ_0)(1 − Pg_0)`, i.e. `P(1 + 2Qg_0) = Q`, and `1 + 2Qg_0 = ±r`; `N_0 = χ_0/(±r)`. For `μ < 0` and the upper sign `Q, P < 0`, so `χ ≤ 1 ≤ N`. (c) `(−Δg)_z = δ_z` and `(Q/χ_0)g_0 = −1`. Writing `N = 1 + n`, `Ln = −(Q/χ_0)δ`; pairing with the zero mode gives `0 = g_0/g_0 = 1`. (d) If `L` is positive definite and `LN' = b` with `b ≥ 0` the walls' contribution: split `N' = N⁺ − N⁻`; `⟨N⁻, LN⁺⟩ ≤ 0` because the off-diagonal entries are non-positive and the supports disjoint, so `⟨N⁻, LN⁻⟩ ≤ −⟨N⁻, b⟩ ≤ 0` and `N⁻ = 0`; a zero of `N'` at an interior site would force zeros at its neighbours and so up to the walls. Conversely let `f > 0` be the lowest mode of `L` (named under Imports), eigenvalue `λ`: `λ⟨f, N'⟩ = ⟨f, b⟩ > 0`. (e) Block 60 T4(c), (d), whose proofs do not use the sign. (f) Block 56's law is `(2/γ)(−Δφ)_z + m_zφ_z = 0`; `φ = 1 − (γ/2)mφ_0g`. ∎

## Theorem T4 — no rule of finite reach keeps only the positive energies

*Statement.* (a) The projector onto the positive energies of the walk has the symbol `½(1 + σ·s/|s|)`, `s_a = sin k_a`, which has different limits along different directions at each of the eight zeros. An operator that commutes with translations and has finite — or absolutely summable — reach has a continuous symbol. (b) For the reduced walk with `m > 0` the symbol is continuous, and it is not a trigonometric polynomial.

*Proof.* (a) Along `k = (t, 0, 0)` the unit vector is `±e_1` for `t → 0±`; block 70's maps carry this zero to the others. (b) If it were, `1/ε` would be a trigonometric polynomial `p` with `p²(m² + sin²k) = 1`; the top coefficient of the left side is `−a²/4`, `a` that of `p`. ∎

## Executed (supervisor control; floating point; evidence, not proof)

`specs/supervisor_control_block71_negative_energy.py`. **W1** (block 55's control with a walker from the negative branch; ring of 1500 sites, packets of width 30 at 600 and 900, rest energies 0.3 and 0.6, `Γ = 0.002`, `T = 300`; source = energy density). Positive pair: `u` at the bodies `−0.069, −0.124`; displacements `+12.5, −6.0`. Mixed pair (energies `+0.285, −0.696`): `u = −0.057` at `A`, `+0.155` at `B`; displacements `−16.7, −9.9`. Negative pair: `u = +0.081, +0.163`; displacements `−21.3, +11.3`. In all three the two wave-vector changes cancel to `1.5e-6` or better and the ledger moves by less than `2e-10`. **W2** (box with interior `9×9×9`, `K = 1`, `g_0 = 0.238703`, bound `−8.3786`): iteration from empty space, continued downwards in `m`: `w_0 = 1.1547, 1.4142, 2.0000, 3.1623, 10.000, 31.623` at `m = 0.25, 0.5, 0.75, 0.9, 0.99, 0.999` of the bound, equal to the closed form to the digits shown, as is `χ_0`; the lowest eigenvalue of `L` falls `0.2937 → 0.0784`; all rates lie between 1 and `w_0`. Beyond the bound (`1.05`) the lengths' equation is not solved by 200 steps (residual `0.11`).

## No-Go Discipline Gate

The note's negative sentences: a negative body below `−2K/g_0` has no static field with positive rates; no rule of finite reach keeps only the positive energies.

### N1 — Routes by which the sentences could fail or mislead
1. *More than one amplitude.* A reading in which the negative levels are filled, or re-described, is not a statement about one amplitude and is outside the supplied clauses.
2. *Another source.* A source such as `|e_x|` is not the derivative of the clocked energy; by block 55 T2(b) the ledger then moves at `Σ(e_x − s_x)du_x/dt`.
3. *Fields that move.* Beyond the bound a time-dependent field is not excluded.
4. *Rules outside T4.* A rule that depends on the state, or does not commute with translations, is outside T4; so is a rule that removes more than the negative energies.
5. *Extended bodies.* The bound is for a body on one site; for a body spread over many sites `g_0` is replaced by a smaller self-potential and the bound is lower. T3(d) is the general statement.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
A box with held walls (the bound depends on the box through `g_0`; on the infinite lattice `g_0` is the unit-source potential at the origin); bodies pinned at rest; slow bodies and rays in T2(b), (c); the weak field in T2(a).

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the lattice; the Qubit axiom's one-site algebra | yes (premise) |
| blocks 54, 55 (open PRs #8570, #8571) | the clocked walk; the ledger and its source; the pulls | yes (restated) |
| blocks 56, 60 (open PRs #8573, #8590) | the two static members | yes (restated; equations re-verified) |
| block 70 (open PR #8602) | the twins | yes (restated; re-verified in B1) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "twins source oppositely; pairs; a negative body's bound; no finite-reach rule" | executed: the energy densities of a state and its twin at all 216 sites; the reduced walk's two contents at all 12 sites | executed: both field equations at all 27 interior sites for three bodies of either sign and for the second root; the zero mode at every site; block 56's law at all 27 sites | executed: the 27 pivots of `L` at both roots; the one-sided limits of the symbol; top coefficients for degrees 0 to 3 | executed: the pulls and accelerations of three kinds of pair on a ring with the exact potential; the symmetry of the rays' equations | T1 every state and rate field; T2 point bodies in the weak field, rays; T3 one body in a box, many through the criterion; T4 the walk and its reduced form; which amplitudes are present is not decided |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; in particular the registered realized-state primitive supplies no rule for which states are present, and none is proposed.

### N7 — Steelman
Hostile reviewer: "Negative-energy states are an artefact; drop them." Reply: they are half of the supplied walk's states, block 70's maps tie them to the positive ones exactly, and T4 shows that dropping them is not something a rule of the supplied kind can do. Whether to supply something else is the owner's. Second objection: "The chase is a known pathology; it refutes the clauses." Reply: it refutes nothing by itself — the ledger and the momentum are kept — and the note claims no more than that the clauses, as supplied, contain it. Third objection: "The bound is a lattice artefact." Reply: `g_0` is the lattice's self-potential of a point; N1.5 says what replaces it for an extended body.

### N8 — Cross-cycle echo
Block 55: the source must be the energy density — with its sign. Block 60: a positive body's clock slows and never stops. Here: a negative body's clock quickens and has a last value. Block 70: the twins are exact copies as test bodies; here they are exact opposites as sources.

## Falsifiers

- A state and rate field with `e_x[A_nψ] ≠ −e_x[ψ]` at some site.
- A static field with positive rates for one body at rest with `m ≤ −2K/g_0` in the curvature member.
- An operator of finite reach, commuting with translations, equal to the walk's positive-energy projector.

## Boundaries and non-claims

Which amplitudes are present is not decided and no rule is proposed. Bodies are pinned; fields that move are outside; records and formation events are outside. No statistical statement, no gravitational statement, no adoption.

## Imports
- `minimal_axioms`: the Lattice axiom, the Qubit axiom's one-site algebra, the memo's silence on amplitude dynamics. Blocks 53–56, 60, 70 (PRs #8568, #8570, #8571, #8573, #8590, #8602, open): restated or placed.
- Named standard imports at definition level: quadratic equations; symmetric matrices with non-positive off-diagonal entries and their positive lowest mode (Perron and Frobenius); symbols of operators that commute with translations; trigonometric polynomials.
- Reference only: Dirac; Bondi; Hamilton.

## Review record
Supervisor-run block, the nineteenth of the source-link direction and the fifteenth of the owner's 12-hour campaign. Lens pass, in writing, by the supervisor (the campaign's no-subagent rule). A foundations lens: the axioms say nothing about amplitudes, so nothing in them selects a sign of energy; the registered realized-state primitive is not a selection rule and is not used as one; the note must not smuggle in a many-amplitude reading. A rigour lens: before writing, the supervisor read block 55's theorems and block 60's T4, statement and proof, for where positivity was used — block 55 T1–T3 do not use it, T4(b) does; block 60 T4 assumes `m_i > 0` in its uniqueness argument (a convex function on the positive orthant), which fails for negative bodies, where the quadratic has two real roots: the second was examined and is excluded by the sign of its rate, not ignored; the "iff" of T3(c) was checked at the bound itself (no solution, by pairing with the zero mode) and beyond it; T3(d)'s two directions are both proved. A strategy lens: block 70 made the species question one of multiplicity; this block shows the multiplicity is not innocent — half of each class sources with the opposite sign — and hands the owner a fork about the content rather than the field. Control: as reported under Executed; the negative pair's repulsion was seen in the control first and then added to the runner's exact check. Mutation census: 7 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_amplitudes_of_negative_energy_fall_like_the_others_and_source_the_opposite_field_2026_09_21.py
```

Expected: `TOTAL: PASS=12 FAIL=0`.
