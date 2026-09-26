---
claim_id: admissibility_rule_under_one_record_per_site_a_collision_changes_the_records_two_step_momentum_only_at_third_order_in_their_offsets_from_the_cones_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "WITHIN block 54's walk and block 78's one record per site, two records on Z^2 or Z^3 with no added interaction, and blocks 140 and 143 as landed: (T1) exact: near the corners of the zone the two-step momentum depends only on the offset delta from the nearest corner, sin(A + delta) cos(A + delta) = sin(delta) cos(delta); with every offset below pi/4, crystal momentum forces the offsets' sum to be conserved exactly in every collision, whichever corners the records leave and reach; so a collision changes the pair's total two-step momentum g = sum sin(delta) cos(delta) only through -(2/3) Delta(sum delta^3) + O(delta^5), third order in the offsets. (T2) exact: for antisymmetric pairs the hard core scatters through the rank-one T-matrix |c><c|/G_cc(z), c the coincident singlet, so every incoming state on an energy shell scatters into the same distribution, weighted by the singlet's overlap; the rate at which a collision changes g, from an incoming state q, is proportional to |<c|q>|^2 (gbar - g(q)), with gbar the contact-weighted shell mean of g. (T3) for almost every total wave vector and energy, gbar - g(q) is nonzero for almost every incoming state (block 143 T1), and near the corners it is third order in the offsets with a leading term that varies on the massless shell. At leading order near one corner the same holds for symmetric pairs: at K = 0 the coincident triplet carries an irreducible representation of the cube's rotations, so the hard core acts on it as a multiple of the identity, the kernel is a function of the angle alone (the singlet's is uniform, the triplet's is c^2/4 with c the cosine of the angle), and the loss from direction n is proportional to (1 - <c^2>) sum_a K_a (n_a^2 - 1/3), with <c^2> = 1/3 (singlet) and 3/5 (triplet). (T4) for a pair near one corner, any bounded finite-range interaction meets the pair at leading order in the offsets only through the spatially even coin sector (the singlet for antisymmetric pairs, the triplet for symmetric ones, where the cube's symmetry makes the amplitude a multiple of the identity), since the pair's plane waves are constant across the interaction region to that order; so its on-shell T-matrix has the hard core's coin structure, the outgoing distribution is the hard core's, and the leading third-order change per collision is the same for every such interaction with a nonzero singlet amplitude at threshold: an interaction changes the collision rate, not the order or its leading coefficient. So under one record per site the pair's two-step momentum, which is its energy current once the records are apart, changes in collisions at third order in the records' offsets from the corners, and not below. The supervisor's own derivation (Claude Opus 5.5), following a panel's proposal; not refereed by another model family. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_under_one_record_per_site_a_collision_changes_the_records_two_step_momentum_only_at_third_order_in_their_offsets_from_the_cones_2026_09_26.py
---

# Under one record per site a collision changes the records' two-step momentum only at third order in their offsets from the cones

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** bounded-support (exact kinematics and the exact rank-one contact collision, within the landed walk and one record per site; the supervisor's own derivation, not refereed by another model family; nothing adopted or registered; unaudited)

This note works within blocks 54, 78, 140 and 143 as landed on main (the walk, one record per site, the two-step momentum and the shell geometry); it reports at which order in the records' offsets from the corners of the zone a collision changes their two-step momentum; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Under one record per site, no finite-range interaction lets two records keep their total energy current, and no local two-step momentum is conserved either (block 151, pushed). A panel of three lenses asked the next question: at which order does the current change? This note answers it for the hard core alone.

- **T1: the change is third order in the offsets.** Near a corner `A ∈ {0, π}^d` of the zone, a record's two-step momentum depends only on its offset `δ` from that corner: `sin(A + δ) cos(A + δ) = sin δ cos δ`. When every offset is below `π/4`, crystal momentum forces the sum of the two records' offsets to be the same before and after a collision, whichever corners they leave and reach. So the pair's total two-step momentum changes only through `−(2/3)Δ(Σδ³) + O(δ⁵)`.
- **T2: every collision on a shell scatters alike.** For antisymmetric pairs the hard core removes one coincident state, the singlet `c`. Its T-matrix is `|c⟩⟨c|/G_cc(z)`, rank one. So every incoming state on an energy shell scatters into the same distribution, weighted by the singlet's overlap. The rate at which collisions change `g`, from an incoming state `q`, is proportional to `|⟨c|q⟩|²(ḡ − g(q))`, with `ḡ` the singlet-weighted mean of `g` on the shell.
- **T3: the change happens, at exactly third order.** For almost every total wave vector and energy, `ḡ − g(q)` is nonzero for almost every incoming state (block 143 T1). Near the corners it is third order in the offsets, and its leading term, the cubic `Σδ³`, is not constant on the massless shell.

- **T4: no finite-range interaction improves it near one corner.** For an antisymmetric pair near one corner, any bounded finite-range interaction acts, at leading order in the offsets, only through the spatially even coin singlet. So its T-matrix has the hard core's coin structure, and every such interaction with a nonzero singlet amplitude at threshold gives the same leading third-order change per collision. An interaction changes how often the records collide, not what a collision does to their current at leading order.

In plain terms: two records that bump into each other change their combined energy current, but only a little when they move slowly. The change is of third order in how far their momenta sit from the special points of the zone where the walk is at rest. Up to second order the books are kept; at third order they are not. That is the same order at which the walkers' clock rules part from the member's (block 150 T5(c)).

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-26.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom." The memo does not "define a time metric". The walk and one record per site are supplied clauses. Nothing is adopted.
- **Two records** (blocks 54 and 78 as landed). `h(k) = Σ_a sin k_a σ_a`, energies `±|sin k|`. One record per site removes the coincident coin states: the singlet for antisymmetric pairs, three states for symmetric pairs (block 143 T4). No other interaction is added.
- **The two-step momentum** (block 140 T1). For one free record, `i[H, D] = P` with `P_a = sin k_a cos k_a`. For a pair at total wave vector `K`, `g_a = sin K_a cos 2q_a` (block 143 T1). Once the records are apart, the pair's energy current is `g`, up to terms of finite relative range.
- **Corners and offsets.** The walk's energy vanishes at the corners `A ∈ {0, π}^d` of the zone. A record near corner `A` has offset `δ = k − A`.
- **The collision rate.** For an incoming pair state `q` on an energy shell, the rate of transitions to `q′` is `2π|t(q′, q)|²` per unit energy density on the shell, with `t` the on-shell T-matrix. It is named at definition level: the transition rate of scattering theory.
- **Standard imports, named at definition level.** Exact symbolic and rational arithmetic. The resolvent of a compression to a subspace of codimension one (the Schur complement). The identity theorem for real-analytic functions. Schur's lemma: an operator commuting with an irreducible representation is a multiple of the identity.

## Theorem T1 — the change is third order in the offsets

*Statement.* Take two records with offsets `δ₁`, `δ₂` from corners `A`, `B`, every component of every offset below `π/4` in size, before and after a collision (outgoing corners `A′`, `B′`, offsets `δ₁′`, `δ₂′`). Then:
- (a) `g = Σ_{i,a} sin δ_{i,a} cos δ_{i,a}`, whatever the corners;
- (b) `δ₁ + δ₂ = δ₁′ + δ₂′` exactly;
- (c) `Δg = −(2/3)Δ(Σ_{i,a} δ_{i,a}³) + O(|δ|⁵)`.

*Proof.* (a) `sin(A + δ) cos(A + δ) = sin δ cos δ` for `A ∈ {0, π}` (runner B1). (b) Crystal momentum is conserved modulo `2π` in each component: `A + B + δ₁ + δ₂ ≡ A′ + B′ + δ₁′ + δ₂′`. The corner sums differ by a multiple of `π`, and both offset sums lie in `(−π/2, π/2)`, so they differ by less than `π`. An odd multiple of `π` is then impossible, and an even one forces equality (runner B2). (c) `sin δ cos δ = δ − (2/3)δ³ + (2/15)δ⁵ − …` (B1), and the linear terms cancel by (b). ∎

## Theorem T2 — every collision on a shell scatters alike

*Statement.* For antisymmetric pairs, in each fiber of total wave vector `K`:
- (a) the compressed generator's resolvent is `G(z) = R₀ − R₀|c⟩⟨c|R₀/G_cc(z)`, with `R₀` the free pair's resolvent and `G_cc = ⟨c|R₀|c⟩`. So the hard core scatters through the rank-one T-matrix `|c⟩⟨c|/G_cc(z)`;
- (b) from an incoming state `q` on the shell at energy `E`, the rate at which collisions change `g` is `2π|⟨c|q⟩|² ρ_c(E)(ḡ − g(q))/|G_cc(E + i0)|²`. Here `ρ_c(E) = ∫_shell |⟨q′|c⟩|² dσ/|∇E|` and `ḡ = ∫_shell |⟨q′|c⟩|² g dσ/|∇E| / ρ_c`. The factor `ḡ` is the same for every incoming state on the shell.

*Proof.* (a) `G` annihilates `c` on both sides, and `P(h₀ − z)PG = P` on the complement (runner C1, exactly in a finite model). (b) The on-shell kernel is `⟨q′|c⟩⟨c|q⟩/G_cc(E + i0)`. Summing the transition rates times `g(q′) − g(q)` over the shell gives the stated product (runner C2). ∎

## Theorem T3 — the change happens, at exactly third order

*Statement.*
- (a) For almost every `K` and `E`, the rate of T2(b) is nonzero for almost every incoming state on the shell.
- (b) Near the corners, `ḡ − g(q) = −(2/3)(⟨Σδ³⟩ − Σδ³(q)) + O(δ⁵)`, where `⟨·⟩` is the singlet-weighted shell mean. At leading order the shell is massless, `|δ₁| + |δ₂| = E`. There the cubic is not constant: with total offset `(p, 0, 0)`, `Σδ³ = p³/4 + 3px²` along the family `δ₁ = (p/2 + x, y, 0)`, `δ₂ = (p/2 − x, −y, 0)`. So the change is exactly third order whenever the pair's total offset is nonzero.

- (c) *Both exchange signs, at leading order near one corner.* Take `K → 0` with the records near one corner, on the shell of the band pair `(+, +)`, which at leading order is the sphere `|q| = E/2`. At `K = 0` the coincident triplet carries an irreducible representation of the cube's rotations, so `A†R₀A` is a multiple of the identity on it (an operator commuting with an irreducible representation is scalar; named under Premises), and the hard core's kernel is `w(n·n′) = |⟨u(n′)|P|u(n)⟩|²`, with `P` the singlet or triplet projector. It is a function of the angle alone: `1/4` for the singlet and `c²/4` for the triplet, `c = n·n′`. With `g_a = sin K_a cos 2q_a = K_a − 2K_aq_a² + …`, the rate at which collisions change `g` from direction `n` is proportional to `(1 − ⟨c²⟩_w) Σ_a K_a(n_a² − 1/3)`, where `⟨c²⟩_w` is the kernel-weighted mean of `c²`. It is `1/3` (singlet) and `3/5` (triplet), both below one. So the change is nonzero for generic directions for both exchange signs.

*Proof.* (a) By block 143 T1, `g` is constant on no shell component for almost every `(K, E)`. It is analytic there, so `g − ḡ` vanishes only on a null subset of the shell. The singlet's overlap with the band pair `(s₁, s₂)` is `(1 − s₁s₂ n₁·n₂)/4` (runner E1), which vanishes only where `n₁·n₂ = s₁s₂`, a null set. And `Im G_cc(E + i0) = πρ_c(E) ≠ 0` wherever `ρ_c > 0`, with `R₀ = (h₀ − z)⁻¹`. (b) T1(a) and (c) on the shell, where `Σδ` is fixed by `K` in every channel (T1(b)). The family and two exact points, at `E = 5/2` and `p = 1`, where `Σδ³` takes `79/16` and `1/4`, are runner D1. (c) For a kernel that depends on the angle alone, `Σ_{n′} w n′n′ᵀ = A nnᵀ + B·1` with `A + 3B = N = Σ w` and `A = N(3⟨c²⟩ − 1)/2`. So the rate is proportional to `(A − N)Σ_a K_a(n_a² − 1/3)`, with `A − N = −(3/2)N(1 − ⟨c²⟩)`. The kernels, the means and the irreducibility (the triplet's commutant under the two quarter turns is the scalars) are runner E3. ∎

## Theorem T4 — no finite-range interaction changes the leading loss near one corner

*Statement.* Take a pair near one corner `A`, so that `K` and the relative wave vector `q` are small; for symmetric pairs take `K = 0` at leading order. Add any bounded hermitian translation-invariant interaction acting within relative distance `R`. Then, at leading order in the offsets:
- its on-shell T-matrix is `t(q′, q) = ⟨u(q′)|s⟩ τ(E) ⟨s|u(q)⟩` for antisymmetric pairs, with `s` the coin singlet, `u` the pair's band spinor and `τ` a scalar; for symmetric pairs it is `τ(E)⟨u(q′)|P_t|u(q)⟩`, with `P_t` the triplet projector, since the cube's symmetry at `K = 0` makes any interaction's triplet amplitude a multiple of the identity;
- the outgoing distribution of a collision is therefore the hard core's, and so is the leading third-order change per collision, `ḡ − g(q)` of T2 and T3, for every interaction with `τ(0) ≠ 0`.

*Proof.* The interaction and the exclusion act on the finite set `Ω` of relative positions within `R`. The pair's antisymmetric plane wave restricted to `Ω` is `(e^{iq·r}u(q) − e^{−iq·r}SWAP u(q))/√2` at each `r`, where `SWAP` exchanges the coins. With `q` small and `Ω` finite, `e^{±iq·r} = 1 + O(qR)`. So the restriction is `√2 (Σ_{r∈Ω}|r⟩) ⊗ P_s u(q) + O(qR)`, with `P_s = (1 − SWAP)/2` the projector onto the singlet (runner E2); for symmetric pairs the same step gives `P_t = (1 + SWAP)/2`, and the irreducibility of the triplet (runner E3) makes the triplet amplitude scalar. Any operator supported on `Ω` then has the stated on-shell form at leading order. Corrections of relative order `q` shift the singlet-weighted mean of the cubic by terms of fourth order in the offsets. ∎

If an interaction were tuned so that `τ(0) = 0`, the next order would take over with a different distribution. That case is not examined. Records near different corners are not covered either: there the plane waves carry a fixed alternating phase across `Ω`, and both coin sectors couple at leading order.

**The order, side by side.**
- The walkers' clock rules part from the member's at third order in the lapses' wave numbers (block 150 T5(c)).
- The records' two-step momentum changes in collisions at third order in their offsets from the corners (this note).

Both are third order, in different variables. Whether one effective source term carries both is not examined.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "decision-record addendum 43 (a panel after the records-side no-go): at which order do the records' books fail"
source_of_blocker_text: block 151 (pushed); the panel of 2026-09-26
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "symmetric pairs (rank three); pairs near different corners with added interactions; the member's response to a third-order source defect; an other-family referee"
conditional_surface_status: "two records; the hard core alone; offsets below pi/4; the collision rate of scattering theory"
hypothetical_axiom_status: "the walk and one record per site are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks.**
  - Block 54: the walk. Block 78: one record per site.
  - Block 140: the two-step momentum.
  - Block 143: the shell geometry (T1) and the removed states (T4), as landed.
  - Block 151 (pushed): no finite-range interaction keeps the current exactly.
  - Block 150 (pushed): the walkers' clock defect at third order.
- **Probes and panel.** A three-lens panel (Claude Fable 5.1 subagents, the same vendor family as the supervisor, so not a referee) ranked this question first. Its lattice and gravitation lenses asked whether the loss is third order, and whether collisions between different corners give a larger loss. T1 answers both.
- **In the literature.** Contact scattering and its rank-one T-matrix; the lattice's crystal momentum and umklapp processes, which change a lattice gas's current (the Peierls picture of lattice transport); the energy current of relativistic particles, which equals their conserved momentum. Reference only.
- **New here:**
  - T1: third order in every channel, including collisions between different corners.
  - T2: the rank-one structure makes every collision on a shell scatter alike.
  - T3: the loss is nonzero for almost every incoming state, exactly third order.
  - T4: near one corner, no finite-range interaction changes the leading loss per collision.
- **Provenance.** The supervisor's own derivation, prompted by a same-vendor panel. No other model family has refereed it.

## Exact target and obligation graph

Target: at which order in the records' offsets from the corners a collision changes their two-step momentum, for antisymmetric pairs under the hard core alone. The obligations are:
- (O1) the kinematics (T1: proved here; runner B);
- (O2) the contact collision (T2: proved here; runner C);
- (O3) nonvanishing and the exact order (T3: proved here from block 143 T1; runner D, E);
- (O4) no finite-range interaction changes the leading loss near one corner (T4: proved here; runner E2).

The strongest missing lemma: the statements away from leading order for symmetric pairs, where the hard core has rank three and the outgoing distribution depends on the incoming state.

## No-Go Discipline Gate

The note's negative sentence: the pair's two-step momentum is not kept in collisions beyond second order in the offsets.

### N1 — Attack routes and the scope they leave
Attack routes, each tested here:
1. *Collisions between different corners give a first-order change.* The offsets' sum is conserved exactly in every channel (T1(b); runner B2). ATTEMPTED.
2. *The second-order term survives.* `sin δ cos δ` is odd in `δ`, so there is no second-order term (runner B1). ATTEMPTED.
3. *The cubic change averages to zero.* The outgoing distribution is the same for every incoming state, and the incoming value varies on the shell, so the mean change vanishes only on a null set (T2, T3(a)). ATTEMPTED.
4. *The cubic is constant on the massless shell.* It is not: `p³/4 + 3px²` along an explicit family, with exact points (runner D1). ATTEMPTED.
5. *The singlet does not couple to the band pair.* Its weight `(1 − s₁s₂n₁·n₂)/4` is positive off a null set (runner E1). ATTEMPTED.
6. *An added interaction cancels the leading loss.* Near one corner it acts only through the singlet at leading order, so the leading loss is the hard core's (T4; runner E2). ATTEMPTED.

Scope left open: symmetric pairs beyond leading order near one corner; interactions tuned to a zero singlet amplitude at threshold; pairs near different corners with added interactions; more than two records in a dense gas; the member's response.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical". The collision rate is named under Premises; the offsets' bound `π/4` is stated in T1. No hidden condition was found.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| blocks 54, 78 (landed) | the walk; one record per site | yes (restated) |
| block 140 (landed) | the two-step momentum | yes (restated) |
| block 143 (landed) | T1 (g on shells), T4 (the removed states) | yes (T1 used as landed; T4's overlap recomputed: runner E1) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the pair's two-step momentum changes in collisions only at third order in the offsets" | executed: the corner identity and the series | executed: the offsets' sum in every corner channel | executed: the compression's resolvent and the rank-one loss formula | executed: the cubic on the massless shell; the singlet's weight | every total wave vector near the corners; antisymmetric pairs |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "This is lattice umklapp folklore: currents of lattice gases relax."
  - *Reply:* The folklore says currents relax; it does not say at which order in the offsets, or that the order is the same in every corner channel, or that the hard core alone does it. For relativistic particles the energy current is the conserved momentum and never changes. Here it changes, but only at third order.

### N8 — Cross-cycle echo
- Block 137: the current is lost at a single collision.
- Block 151: no finite-range interaction keeps it.
- Block 150 T5(c): the walkers' clock defect at third order.
- This note: the records' loss at third order.

## Falsifiers

- Two offsets below `π/4` and a collision in which `δ₁ + δ₂` changes.
- A shell on which the singlet-weighted mean of `g` equals `g` at almost every incoming state.
- An error in the runner's identities.

## Boundaries and non-claims

- Offsets below `π/4`; antisymmetric pairs with the hard core alone (T1–T3(b)); both exchange signs at leading order near one corner (T3(c)); near one corner any finite-range interaction with a nonzero amplitude at threshold (T4). Symmetric pairs beyond leading order, tuned interactions, added interactions between different corners and dense gases are not covered.
- The rate is the transition rate of scattering theory for one pair; no gas average or distribution is assumed.
- Not refereed by another model family.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 54, 78, 140 and 143 (landed), restated or recomputed in part.
- Named standard imports, at definition level: exact symbolic and rational arithmetic; the resolvent of a compression (the Schur complement); the transition rate of scattering theory (Fermi's golden rule); the identity theorem for real-analytic functions.

## Review record

- **Who and when.** Supervisor-run block, 2026-09-26, during the owner's 12-hour campaign of that day, after a panel on the next programme.
- **Provenance.** The supervisor's own derivation (Claude Opus 5.5), with exact checks by its own runner. It is not refereed by another model family.
- **Before writing.** The own prior-art check (memory, open PRs, probes attempts, main) found block 137's single-collision witness and blocks 143 and 151, and no statement of the order.
- **The improvement question.** T4 answers the panel's strategy lens for pairs near one corner: an interaction changes the collision rate, not the leading loss.
- **Independence.** Mutation census: one mutation per science family (B, C, D, E), each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_under_one_record_per_site_a_collision_changes_the_records_two_step_momentum_only_at_third_order_in_their_offsets_from_the_cones_2026_09_26.py
```

Expected: `TOTAL: PASS=15 FAIL=0`.
