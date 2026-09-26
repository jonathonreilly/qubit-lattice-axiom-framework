---
claim_id: admissibility_rule_under_one_record_per_site_a_collision_changes_the_records_two_step_momentum_only_at_third_order_in_their_offsets_from_the_cones_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: Supplied two-record walk on Z^2 or Z^3. Exact componentwise corner kinematics give Delta g_a = -(2/3)
  Delta sum_i delta_ia^3 + O(delta^5), with no first or second order term when all offsets are below pi/4. For upper-band
  incoming pairs below sqrt(2)/2, the outgoing open channels obey that bound off the equality set. The hard-core
  antisymmetric pair has an exact rank-one resolvent and common outgoing shell distribution wherever boundary values
  and positive contact density exist. Cubic order is generic in nondegenerate scaling regimes, not nonzero for every
  collision, state, component or scaling; at zero total offset g vanishes. The same-corner singlet/triplet angular
  calculation is a three-dimensional conditional channel comparison near K/E=0. Added finite-range interactions
  have the displayed single-channel leading form only with a uniformly regular finite-support T-matrix, a nonzero
  leading amplitude, and rotation covariance for the triplet. Other corner channels, threshold poles and anisotropic
  triplet amplitudes are not excluded.
upstream_dependencies:
- admissibility_rule_exact_books_need_records_that_never_scatter_or_bind_nothing_local_keeps_them_under_one_record_per_site_bounded_theorem_note_2026-09-25
- admissibility_rule_the_walk_carries_an_exact_boost_charge_its_brackets_give_the_fall_weight_and_an_exactly_kept_angular_momentum_with_the_face_spin_bounded_theorem_note_2026-09-25
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

For the supplied walk, crystal momentum cancels the linear change of the componentwise two-step momentum whenever all incoming and outgoing offsets are below `π/4`. Its first possible change is cubic. A collision or its average can have a zero cubic coefficient; no universal nonzero loss or relaxation rate follows.

The antisymmetric hard core has an exact rank-one contact resolvent, so the outgoing distribution at a regular shell is independent of the incoming state after conditioning on a scattering event. The current changes generically where the contact weight is positive and the current varies on the shell. The same-corner angular comparison and extension to added interactions below have extra hypotheses; they do not prove universality for arbitrary finite-range interactions.

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
- (a) `g_a = Σ_i sin δ_{i,a} cos δ_{i,a}`, whatever the corners;
- (b) `δ₁ + δ₂ = δ₁′ + δ₂′` exactly;
- (c) `Δg_a = −(2/3)Δ(Σ_i δ_{i,a}³) + O(|δ|⁵)`;
- (d) a pair in the band pair `(+, +)` with energy `E < √2/2` scatters only into `(+, +)` pairs, for every incoming state off a null set, and every offset before and after has every component below `π/4`. So (a)–(c) hold for every collision of such a pair.

*Proof.* (a) `sin(A + δ) cos(A + δ) = sin δ cos δ` for `A ∈ {0, π}` (runner B1). (b) Crystal momentum is conserved modulo `2π` in each component: `A + B + δ₁ + δ₂ ≡ A′ + B′ + δ₁′ + δ₂′`. The corner sums differ by a multiple of `π`, and both offset sums lie in `(−π/2, π/2)`, so they differ by less than `π`. An odd multiple of `π` is then impossible, and an even one forces equality (runner B2). (c) `sin δ cos δ = δ − (2/3)δ³ + (2/15)δ⁵ − …` (B1), and the linear terms cancel by (b). (d) The dispersion `ε(k) = (Σ_a sin²k_a)^{1/2}` is subadditive: `sin(a_i + b_i) = sin a_i cos b_i + cos a_i sin b_i` and `|cos| ≤ 1` give `ε(a + b) ≤ ε(a) + ε(b)` (runner B3). A band pair `(+, −)` with total `K` has energy `ε(k₁′) − ε(k₂′) ≤ ε(K)`, since `ε(k₁′) ≤ ε(K) + ε(k₁′ − K)` and `ε(k₁′ − K) = ε(k₂′)`. The incoming energy is `ε(k₁) + ε(k₂) ≥ ε(K)`. Equality needs `|cos k_{2,i}| = 1` wherever `sin k_{1,i} ≠ 0`, a null set. A pair `(−, −)` has negative energy. So only `(+, +)` is open, and each record before and after has `ε ≤ E`. Finally `ε(k) ≥ |sin d_a|` for each component's offset `d_a` from the nearest multiple of `π`, and `|sin d_a| ≥ √2/2` when `|d_a| ≥ π/4`. So `E < √2/2` keeps every offset below `π/4`. ∎

## Theorem T2 — every collision on a shell scatters alike

*Statement.* For antisymmetric pairs, in each fiber of total wave vector `K`:
- (a) the compressed generator's resolvent is `G(z) = R₀ − R₀|c⟩⟨c|R₀/G_cc(z)`, with `R₀` the free pair's resolvent and `G_cc = ⟨c|R₀|c⟩`. So the hard core scatters through the rank-one T-matrix `|c⟩⟨c|/G_cc(z)`;
- (b) from an incoming state `q` on the shell at energy `E`, the rate at which collisions change `g` is `2π|⟨c|q⟩|² ρ_c(E)(ḡ − g(q))/|G_cc(E + i0)|²`. Here `ρ_c(E) = ∫_shell |⟨q′|c⟩|² dσ/|∇E|` and `ḡ = ∫_shell |⟨q′|c⟩|² g dσ/|∇E| / ρ_c`. The factor `ḡ` is the same for every incoming state on the shell.

*Proof.* (a) `G` annihilates `c` on both sides, and `P(h₀ − z)PG = P` on the complement (runner C1, exactly in a finite model). (b) The on-shell kernel is `⟨q′|c⟩⟨c|q⟩/G_cc(E + i0)`. Summing the transition rates times `g(q′) − g(q)` over the shell gives the stated product (runner C2). ∎

## Theorem T3 — generic cubic variation and a conditional angular comparison

*Statement.*
- (a) For almost every regular `K` and `E` with positive finite contact density and finite boundary values, the rate of T2(b) is nonzero for almost every incoming state in the contact-coupled part of the shell.
- (b) Near the corners, `ḡ − g(q) = −(2/3)(⟨Σδ³⟩ − Σδ³(q)) + O(δ⁵)`, where `⟨·⟩` is the singlet-weighted shell mean. At leading order the shell is massless, `|δ₁| + |δ₂| = E`. There the cubic is not constant: with total offset `(p, 0, 0)`, `Σδ³ = p³/4 + 3px²` along the family `δ₁ = (p/2 + x, y, 0)`, `δ₂ = (p/2 − x, −y, 0)`. This gives a nonzero cubic variation in this scaling family, with `0 < |p| < E` and fixed nonzero `p/E`. It does not prove a nonzero coefficient in every state or direction. At total offset zero, `g_a = 0` identically; if `p` tends to zero faster than the relative offsets, the first nonzero change may have higher order. The order here concerns change per collision, not the rate prefactor in T2.

- (c) *Three-dimensional same-corner channel comparison.* Take offsets small and additionally `|K|/E → 0`, conditioning both incoming and outgoing states to the same corner, on the shell of the band pair `(+, +)`, which at leading order is the sphere `|q| = E/2`. At `K = 0` the coincident triplet carries an irreducible representation of the cube's rotations, so `A†R₀A` is a multiple of the identity on it (an operator commuting with an irreducible representation is scalar; named under Premises), and the hard core's kernel is `w(n·n′) = |⟨u(n′)|P|u(n)⟩|²`, with `P` the singlet or triplet projector. It is a function of the angle alone: `1/4` for the singlet and `c²/4` for the triplet, `c = n·n′`. With `g_a = sin K_a cos 2q_a = K_a − 2K_aq_a² + …`, the componentwise rate at which collisions change `g_a` from direction `n` is proportional to `(1 − ⟨c²⟩_w) K_a(n_a² − 1/3)`, where `⟨c²⟩_w` is the kernel-weighted mean of `c²`. It is `1/3` (singlet) and `3/5` (triplet), both below one. Within this three-dimensional angular comparison the first term in nonzero K is generically nonzero. At exactly K = 0 it vanishes. The plane has a circle rather than a sphere; its angular means are 1/2 and 3/4, and the three-dimensional triplet irreducibility argument is not a plane theorem. This calculation does not sum all other corner channels, which are kinematically open.

*Proof.* (a) By block 143 T1, `g` is constant on no shell component for almost every `(K, E)`. It is analytic there, so `g − ḡ` vanishes only on a null subset of the shell. The singlet's overlap with the band pair `(s₁, s₂)` is `(1 − s₁s₂ n₁·n₂)/4` (runner E1), which vanishes only where `n₁·n₂ = s₁s₂`, a null set. And `Im G_cc(E + i0) = πρ_c(E) ≠ 0` wherever `ρ_c > 0`, with `R₀ = (h₀ − z)⁻¹`. (b) T1(a) and (c) on the shell, where `Σδ` is fixed by `K` in every channel (T1(b)). The family and two exact points, at `E = 5/2` and `p = 1`, where `Σδ³` takes `79/16` and `1/4`, are runner D1. (c) For a kernel that depends on the angle alone, `Σ_{n′} w n′n′ᵀ = A nnᵀ + B·1` with `A + 3B = N = Σ w` and `A = N(3⟨c²⟩ − 1)/2`. So the rate is proportional to `(A − N)K_a(n_a² − 1/3)`, with `A − N = −(3/2)N(1 − ⟨c²⟩)`. The kernels, the means and the irreducibility (the triplet's commutant under the two quarter turns is the scalars) are runner E3. ∎

## Theorem T4 — conditional same-corner factorization

Let the incoming and outgoing channels both remain near the same corner, with `qR` small. Assume that the effective on-shell operator on the fixed finite interaction support has a uniformly bounded limit with an O(offset) remainder as the offsets and energy tend to zero, and that its leading projected amplitude is nonzero. This regular-threshold assumption is additional to a bounded microscopic interaction. For the symmetric three-dimensional case also impose cube-rotation covariance at K = 0; exchange symmetry alone is insufficient.

For an antisymmetric pair the restriction to the support is
`(exp(iq.r)u - exp(-iq.r)SWAP u)/sqrt(2) = sqrt(2) 1_Ω ⊗ P_s u + O(qR)`.
The singlet projector has rank one, so sandwiching the uniformly regular supported operator gives `⟨u′|s⟩ τ ⟨s|u⟩ + O(qR)`. For symmetric pairs the same restriction uses the triplet projector; only the additional rotation covariance makes its three-dimensional amplitude scalar. Thus, **conditioned on the same-corner channel**, the leading outgoing angular distribution agrees with the contact comparison when that leading amplitude is nonzero. The error changes a cubic observable at fourth or higher total offset order under these regularity and fixed-ratio scaling hypotheses.

A finite-range interaction can break cube rotations, have a threshold pole or zero, or scatter into other corners. Bounded microscopic matrix elements do not bound the inverse entering its T-matrix. Other outgoing corners carry different fixed phases on the support, so their amplitudes need not share one scalar τ. No universal leading loss per collision over all channels is established for arbitrary finite-range interactions. Runner E2 checks the projector factorization, not these additional analytic or channel hypotheses.

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
  - T3: on regular shells with positive contact density the loss is generically nonzero; a cubic variation is exhibited in a fixed-ratio scaling family.
  - T4: conditional same-corner factorization under a regular threshold limit, nonzero amplitude and, for triplets, rotation covariance.
- **Provenance.** The supervisor's own derivation, prompted by a same-vendor panel. No other model family has refereed it.

## Exact target and obligation graph

Target: at which order in the records' offsets from the corners a collision changes their two-step momentum, for antisymmetric pairs under the hard core alone. The obligations are:
- (O1) the kinematics (T1: proved here; runner B);
- (O2) the contact collision (T2: proved here; runner C);
- (O3) nonvanishing and the exact order (T3: proved here from block 143 T1; runner D, E);
- (O4) conditional same-corner factorization (T4; E2 tests only the algebraic projector step). Uniform threshold regularity and full multichannel universality are not proved.

The strongest missing lemma: the statements away from leading order for symmetric pairs, where the hard core has rank three and the outgoing distribution depends on the incoming state.

## No-Go Discipline Gate

The note's negative sentence: the first possible change is cubic, and a generic cubic variation is exhibited; special states and scalings can keep it or delay the change.

### N1 — Attack routes and the scope they leave
Attack routes, each tested here:
1. *Collisions between different corners give a first-order change.* The offsets' sum is conserved exactly in every channel (T1(b); runner B2). ATTEMPTED.
2. *The second-order term survives.* `sin δ cos δ` is odd in `δ`, so there is no second-order term (runner B1). ATTEMPTED.
3. *The cubic change averages to zero.* The outgoing distribution is the same for every incoming state, and the incoming value varies on the shell, so the mean change vanishes only on a null set (T2, T3(a)). ATTEMPTED.
4. *The cubic is constant on the massless shell.* It is not: `p³/4 + 3px²` along an explicit family, with exact points (runner D1). ATTEMPTED.
5. *The singlet does not couple to the band pair.* Its weight `(1 − s₁s₂n₁·n₂)/4` is positive off a null set (runner E1). ATTEMPTED.
6. *An added interaction changes the leading loss.* The same-corner projector factorization is tested (E2), but threshold singularities, zero amplitudes, anisotropic triplets and other outgoing corner channels remain open counterroutes. No unrestricted exclusion is claimed.
7. *Records scatter far from the corners, into a band pair `(+, −)`.* Below pair energy `√2/2` that channel is closed and every offset stays below `π/4` (T1(d); runner B3). ATTEMPTED.

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
- This note: the records' first possible loss at third order, with generic examples and exceptional zero-loss cases.

## Falsifiers

- Two offsets below `π/4` and a collision in which `δ₁ + δ₂` changes.
- Momenta `a`, `b` with `ε(a + b) > ε(a) + ε(b)`.
- A shell on which the singlet-weighted mean of `g` equals `g` at almost every incoming state.
- An error in the runner's identities.

## Boundaries and non-claims

- Offsets below `π/4`; componentwise kinematics and the antisymmetric rank-one hard core. T3(c) is a three-dimensional same-corner, small-K/E comparison. T4 is conditional as stated; arbitrary finite-range interaction universality is withdrawn. Cubic-order change per collision is distinct from collision rate, and can vanish in special states or scaling regimes.
- The rate is the transition rate of scattering theory for one pair; no gas average or distribution is assumed.
- Not refereed by another model family.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 54, 78, 140 and 143 (landed), restated or recomputed in part.
- Named standard imports, at definition level: exact symbolic and rational arithmetic; the resolvent of a compression (the Schur complement); the transition rate of scattering theory (Fermi's golden rule); the identity theorem for real-analytic functions.

## Review record

Landing review separates vector components, generic cubic variation from universal nonzero change, and per-event change from collision rate. The angular averages 1/3 and 3/5 use the sphere in three dimensions; the plane values differ. The original T4 is narrowed to its actual regular-threshold and same-channel hypotheses. For example, an anisotropic rank-one triplet interaction need not commute with rotations, and at zero total offset the exact pair current is zero. Original stronger statements remain at the frozen PR head as research material, not retained conclusions.

- **Who and when.** Supervisor-run block, 2026-09-26, during the owner's 12-hour campaign of that day, after a panel on the next programme.
- **Provenance.** The supervisor's own derivation (Claude Opus 5.5), with exact checks by its own runner. It is not refereed by another model family.
- **Before writing.** The own prior-art check (memory, open PRs, probes attempts, main) found block 137's single-collision witness and blocks 143 and 151, and no statement of the order.
- **The improvement question.** T4 retains only conditional single-channel factorization. The original broader universality claim lacked threshold regularity, rotation covariance and control of other open corner channels.
- **Independence.** Mutation census: eight mutations, at least one per science family (two in B, one in C, one in D, two in E) and two in family F, each failing in its own family.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_under_one_record_per_site_a_collision_changes_the_records_two_step_momentum_only_at_third_order_in_their_offsets_from_the_cones_2026_09_26.py
```

Expected: `TOTAL: PASS=16 FAIL=0`.

## Dependencies

- [Current scoped input](ADMISSIBILITY_RULE_EXACT_BOOKS_NEED_RECORDS_THAT_NEVER_SCATTER_OR_BIND_NOTHING_LOCAL_KEEPS_THEM_UNDER_ONE_RECORD_PER_SITE_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [Current scoped input](ADMISSIBILITY_RULE_THE_WALK_CARRIES_AN_EXACT_BOOST_CHARGE_ITS_BRACKETS_GIVE_THE_FALL_WEIGHT_AND_AN_EXACTLY_KEPT_ANGULAR_MOMENTUM_WITH_THE_FACE_SPIN_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [Current scoped input](MINIMAL_AXIOMS_2026-06-29.md)
