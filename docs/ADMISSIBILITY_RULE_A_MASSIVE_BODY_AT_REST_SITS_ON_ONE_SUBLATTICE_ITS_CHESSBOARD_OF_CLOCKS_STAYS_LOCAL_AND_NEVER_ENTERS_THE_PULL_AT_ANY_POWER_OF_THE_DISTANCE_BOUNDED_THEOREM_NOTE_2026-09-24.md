---
claim_id: admissibility_rule_a_massive_body_at_rest_sits_on_one_sublattice_its_chessboard_of_clocks_stays_local_and_never_enters_the_pull_at_any_power_of_the_distance_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "WITHIN block 54's walk H = sum_j sigma_j D_j and its clock phi H phi (w = phi^2), block 77's staggered mass m eps, block 55's source e_x = Re psi_x^dagger (H_w psi)_x, the simplest member of blocks 55-56 (weak-field law (1 - A) u = -(gamma/6)(e - ebar)) and block 60's curvature member (weak-field Delta u = (e + tau)/(4K wbar), gamma = 1/(4K)), and block 76's chessboard invariance, all as landed on main and supplied. Exact: (T1) the positive rest states of H + m eps are e^(i pi n.x)(1 + eps)u: they vanish on every odd site, their energy density is m |chi_x|^2 >= 0 on the even sites and 0 on the odd ones, summing to m, and with any clock field it is exactly m w_x |chi_x|^2. (T2) a moving eigenstate has density E |psi_x|^2 >= 0 at every site; its mass part alternates and sums to m^2/E (at k = (pi/2, 0, 0), m = 3/4: E = 5/4, weights 4/5 and 1/5, mass part 9/20). (T3) the chessboard part of a body's source makes a chessboard of clocks: on a torus the rest source is (m/V) eps and the simplest member's field is u = -(gamma m/(12V)) eps, which costs bond energy; every bond product of phi = c^eps is 1, so no odd-step operator feels it, but phi (m eps) phi = m(c^2 - c^-2)/2 + m eps (c^2 + c^-2)/2: a massive walker feels a scalar potential and a mass factor. (T4) both members' weak-field symbols vanish only at k = 0, equal 2 and 12 at the stagger's wave vector, and give the same kernel -gamma/Delta(k); so the staggered part of a source makes a field decaying faster than any power of the distance, and the pull between two bodies at rest is fixed by their moments at every power of 1/R, with leading term -(gamma/(4 pi)) Q_A Q_B / R. Harvest block from a Grok-refereed probes attempt, re-checked by an independent runner. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_a_massive_body_at_rest_sits_on_one_sublattice_its_chessboard_of_clocks_stays_local_and_never_enters_the_pull_2026_09_24.py
---

# A massive body at rest sits on one sublattice: its chessboard of clocks stays local, and never enters the pull at any power of the distance

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** bounded-support (exact within blocks 54, 55, 56, 60, 76 and 77 as landed; harvest block from a Grok-refereed probes attempt; nothing adopted or registered; unaudited)

This note works within blocks 54, 55, 56, 60, 76 and 77 as landed on main (the walk and its clock, the source as the amplitudes' energy density, the simplest and the curvature members, the chessboard of clocks, and the staggered mass); it reports where a massive body's energy sits, what its chessboard part does to the clocks, and whether that part enters the pull between bodies; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 77, as landed, gave the walker a rest energy through a staggered mass `mε`, which alternates in sign from site to site. Block 76 found that a chessboard of clocks is invisible to the walker's hops. That raises three questions. Where does a massive body's energy sit? Does its alternating part make a chessboard of clocks? Does that chessboard spoil the pull between two bodies?

- **T1: a body at rest sits on one sublattice.**
  - The positive rest states vanish on every odd site.
  - Their energy density is non-negative, lives on the even sites, and sums to `m`. It is not alternating.
  - With a clock field it is exactly `m w_x|χ_x|²`.
- **T2: moving, the density stays non-negative.** A moving eigenstate's density is `E|ψ_x|² ≥ 0`. Only its mass part alternates, and that part sums to `m²/E`.
- **T3: the chessboard of clocks.**
  - The chessboard part of a body's source makes a chessboard of clocks, and in the simplest member it costs bond energy.
  - No hop feels it, since every bond product is one.
  - A massive walker does feel it: as a scalar potential and as a factor on its mass.
- **T4: it never enters the pull.**
  - Both members' weak-field kernels are smooth away from zero wave number, including at the stagger's wave vector.
  - So the chessboard part of a source makes a field that dies faster than any power of the distance.
  - The pull between two bodies at rest is fixed by their monopoles and higher moments at every power of `1/R`. Its leading term is `−(γ/(4π))Q_AQ_B/R`.

In plain terms, a heavy body at rest in this model lives on every other site: its energy is all in the "black squares", and none of it is negative. Its alternating part does tick the clocks in a chessboard pattern, but only right next to the body, and a hop never notices. The pull that one body exerts on another, at any distance and to any accuracy in one over the distance, comes only from how much energy each body has and how it is spread, not from the chessboard. So the staggered mass does not spoil the long-range pull.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-24.
  - "No possibility is privileged." "No site is privileged." The staggered mass breaks one-site translation, as block 77 as landed notes. It is supplied.
  - "Admissibility is not a dynamics axiom." The walk, the mass, the clock laws and the members are supplied. Nothing is adopted.
- **The walk** (block 54 as landed). `H = Σ_jσ_jD_j` with `(D_jψ)(x) = (i/2)(ψ(x − e_j) − ψ(x + e_j))`, whose symbol is `sin k_j`. The clocked walk is `φHφ`, with `w = φ² = e^u`.
- **The staggered mass** (block 77 as landed). `ε(x) = (−1)^{x₁+x₂+x₃}` and `H + mε`, with `(H + mε)² = H² + m²` (block 77 T3). Clocked: `φ(H + mε)φ = φHφ + mwε`.
- **The source** (block 55 as landed): `e_x = Re ψ_x†(H_wψ)_x`.
- **The simplest member** (blocks 55–56 as landed). `F = (2/γ)Σ_bonds(φ_x − φ_y)²`. Its weak-field law, as a supplied model, is `(1 − A)u = −(γ/6)(e − ē)/w̄`, where `A` averages over the six neighbours.
- **The curvature member** (block 60 as landed). The rates are multipliers. The weak-field law is `Δu = (e + τ)/(4Kw̄)`, with `γ = 1/(4K)`.
- **The chessboard of clocks** (block 76 T1 as landed). `φ → φc^ε` leaves every opposite-parity hop unchanged.
- **Comparators, named only:** the Hellmann–Feynman theorem; the Coulomb kernel `1/|k|²` and its multipole expansion; staggered (Kogut–Susskind) fermions, whose mass term alternates.

## Theorem T1 — a body at rest sits on one sublattice

*Statement.*
- (a) The positive rest states of `H + mε` are `χ = e^{iπn·x}(1 + ε)u`, `n ∈ {0, 1}³`, `u ∈ ℂ²`. They satisfy `(H + mε)χ = mχ` and vanish on every odd site.
- (b) Their energy density is `e_x = m|χ_x|² ≥ 0` on the even sites and `0` on the odd ones, and its sum over sites, normalised, is `m`.
- (c) With any clock field the density is exactly `e_x = mw_x|χ_x|²`.

*Proof.*
- (a) `ε` anticommutes with `H`, so it maps `ker H` to itself. `ker H` is spanned by the eight zero modes `e^{iπn·x}u`, and `(1 + ε)` projects onto its `ε = +1` part, where `H + mε` acts as `m`.
- (b) and (c): at an even site `φHφχ` reads only odd neighbours, where `χ = 0`. So only the mass term remains.

∎

*Checked (B1).* On the `4³` torus, every one of the eight rest states with two coin vectors: the eigenvalue, the vanishing on odd sites, and the density and its sum. The density with a rational clock field.

## Theorem T2 — moving, the density stays non-negative

*Statement.* A moving eigenstate of `H + mε` has `e_x = E|ψ_x|² ≥ 0` at every site, with `E = √(|sin k|² + m²)`. Its mass part `Σmε|ψ|²` alternates in sign from site to site and sums, normalised, to `m²/E`. At `k = (π/2, 0, 0)` and `m = 3/4`: `ψ = e^{ik·x}(1 + ε/3)(1, 1)` has `E = 5/4`, weight `4/5` on the even sites and `1/5` on the odd ones, and mass part `9/20`.

*Proof.* `e_x = Re ψ_x†(Eψ)_x`. The mass part is `m⟨ε⟩`, and `⟨ε⟩ = ∂E/∂m = m/E`. ∎

*Checked (C1).* The eigenstate on the `4³` torus exactly, its weights, its mass part, and its density at every site.

## Theorem T3 — the chessboard of clocks

*Statement.*
- (a) `Aε = −ε`. So on a torus the mean-removed rest source `(m/V)ε` is solved in the simplest member by `u = −(γm/(12V))ε`: a chessboard of clocks `φ = c^ε` with `c = e^{−γm/(24V)}`, slow on the body's sublattice.
- (b) It costs the bond energy `(2/γ)·3V(c − 1/c)² > 0`.
- (c) Every bond product `φ_xφ_y` is `1`, so no operator that moves an odd number of steps feels it (block 76 T1).
- (d) A massive walker does feel it: `φ(mε)φ = m(c² − c^{−2})/2 + mε(c² + c^{−2})/2`, a scalar potential plus a factor on the mass.

*Proof.*
- (a) Each of a site's six neighbours has the opposite sign.
- (b) Each of the `3V` bonds contributes `(c − 1/c)²`.
- (c) `c^{ε_x}c^{ε_y} = 1` for neighbours.
- (d) `mεc^{2ε}`, split by the sign of `ε`.

∎

*Checked (D1).* The average on the `4³` torus, the field equation, the bond sum, the bond products and the mass identity, exactly.

## Theorem T4 — the staggered part never enters the pull

*Statement.*
- (a) The simplest member's weak-field symbol is `1 − Â(k) = Δ(k)/6`, with `Δ(k) = Σ_j 2(1 − cos k_j)`, the curvature member's. Both vanish only at `k = 0`, and at the stagger's wave vector `π(1,1,1)` they equal `2` and `12`.
- (b) Both give the kernel `−γ/Δ(k)`, which is `−γ/|k|²` near `k = 0`.
- (c) So the chessboard part of any source, which is carried by wave vectors away from `0`, makes a field whose transform is smooth there. That field decays faster than any power of the distance. The pull between two bodies at rest is a function of their monopoles and higher moments at every power of `1/R`, with leading term `−(γ/(4π))Q_AQ_B/R`.

*Proof.* (a) and (b) by substitution and expansion. (c) A kernel analytic away from `k = 0` has a spatial transform that decays faster than any power, apart from the part carried by the singularity at `k = 0`, which the smooth envelopes of the sources feed through their moments. ∎

*Checked (E1).* The symbols at `π(1,1,1)`, their series near `0`, their identity, and the common kernel, symbolically.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "blocks 76-77 as landed: the staggered mass's energy placement and whether its chessboard part sources clocks that enter the pull are not stated"
source_of_blocker_text: blocks 76 and 77 as landed
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the chessboard of clocks' self-energy for a localised massive body; the same question in the strong field of block 56"
conditional_surface_status: "T1-T3 exact on even tori; T4 on the infinite lattice; walk, mass, clock laws and members supplied"
hypothetical_axiom_status: "the staggered mass and the members are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 54: the walk and its clock.
  - Block 55: the source.
  - Blocks 55–56: the simplest member, as a supplied model.
  - Block 60: the curvature member.
  - Block 76: the chessboard of clocks is invisible to hops.
  - Block 77: the staggered mass.
- **The probes attempt.** `the-rest-energy-density-of-a-massive-walker` a2 (Claude Opus 5.5) found T1–T4. A Grok referee confirmed it (#8996).
- **In the literature.**
  - The Hellmann–Feynman theorem.
  - The Coulomb kernel and multipole expansions.
  - Staggered fermions (Kogut and Susskind).

  All reference only.
- **New here:**
  - an independent exact runner;
  - the results placed against blocks 76 and 77 as landed;
  - the reading: the staggered mass does not spoil the long-range pull.

## Exact target and obligation graph

Target: where a massive body's energy sits, and whether its chessboard part enters the pull. The obligations are:
- (O1) the rest density (T1);
- (O2) the moving density (T2);
- (O3) the chessboard of clocks (T3);
- (O4) the pull (T4).

T1–T4 discharge them. Open: the strong field.

## No-Go Discipline Gate

The note's negative sentence: the staggered part of a body's source never enters the pull between two bodies at any power of `1/R`.

### N1 — Routes by which the sentence could fail or mislead
1. *The strong field.* T4 uses the weak-field laws. In block 56's strong field the kernel is not treated.
2. *Close range.* The chessboard's field is local, not absent. At short range it adds a self-energy and a local potential for massive walkers.
3. *Other members.* Any member whose weak-field symbol vanishes at `π(1,1,1)` would change T4. The two treated here do not.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond the supplied walk, mass, clock laws and members.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| blocks 54, 55, 56, 60, 76, 77 (landed) | the walk, source, members, chessboard and mass | yes (restated) |
| probes (Grok-refereed #8996) | T1–T4 first derived | yes (re-derived) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "a body at rest sits on one sublattice; its chessboard of clocks is local; the staggered part never enters the pull" | executed: the eight rest states, with and without clocks | executed: the moving density at every site | executed: the chessboard's field, cost and action | executed: the symbols and the kernel | T1–T3 on even tori; T4 on the infinite lattice; weak field |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used, and nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "An alternating mass must source an alternating field that matters."
  - *Reply:* It does source one, and a massive walker feels it nearby (T3).
  - At a distance it is gone faster than any power, because both kernels are smooth at the stagger's wave vector (T4).

### N8 — Cross-cycle echo
- Block 76 found the chessboard of clocks invisible to hops.
- Block 77 introduced the staggered mass.
- This note finds where the mass's energy sits, and that its chessboard stays local.

## Falsifiers

- A positive rest state of `H + mε` with weight on an odd site.
- A member of the two treated with a symbol vanishing at `π(1,1,1)`.
- A power-law tail in the chessboard part of the weak field.

## Boundaries and non-claims

- The walk, the mass, the clock laws and the members are supplied.
- The strong field is not treated.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 54, 55, 56, 60, 76 and 77, restated.
- The probes attempt, refereed by another model family.
- Named standard imports, at definition level:
  - the Hellmann–Feynman theorem;
  - the decay of the transform of a smooth periodic function (Fourier analysis);
  - Gaussian-rational arithmetic.

## Review record

- **Who and when.** Supervisor-run block, the eighty-first since the source-link direction opened; 2026-09-24.
- **Provenance.**
  - The probes attempt by Claude Opus 5.5 derived the results. A Grok referee confirmed them (#8996).
  - The supervisor re-checked them with its own runner.
- **Before writing.**
  - Main was re-fetched, and blocks 54, 55, 56, 60, 76 and 77 were read as landed.
  - Two integer-division traps in the draft runner were caught and replaced by exact rationals.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_a_massive_body_at_rest_sits_on_one_sublattice_its_chessboard_of_clocks_stays_local_and_never_enters_the_pull_2026_09_24.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
