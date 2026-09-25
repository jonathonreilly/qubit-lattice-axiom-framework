---
claim_id: admissibility_rule_the_lattice_expands_with_the_static_pulls_coupling_iff_alpha_equals_k_over_four_and_top_speed_walkers_lose_energy_as_one_over_the_length_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "WITHIN block 60's homogeneous kinetic model (T5(b)), block 124's kinetic family, block 129's volume power s = 3 and block 101's static clock law, with blocks 134, 135 and 136 for the kinetic normalization, all as landed on main; uniform content on a closed lattice; unit rate. (T1) exact: the member's clock constraint has no zero mode, so a static closed lattice holds no positive content; on the uniform dilation the member's kinetic term gives c_k = 12 alpha + 36 beta, which is -24 alpha < 0 at the closing ratio, so block 60's uniform motion exists, with lamdot^2 = rho/(24 alpha) (rho the content's energy per unit volume). (T2) exact: the static clock law gives the pull's coupling G = 1/(16 pi K), and the expansion obeys lamdot^2 = (8 pi G/3) rho with that same G iff alpha = K/4; then l-ddot/l = -(4 pi G/3)(rho + 3p), with the content's pressure p defined by dm/dlam = -3 p l^3. (T3) exact: content crosses bonds at rate w/l, so the massless walk on a uniformly stretched lattice is H(k)/l: a top-speed walker keeps its wave vector, its energy falls exactly as 1/l and its pressure is rho/3; the lattice then expands as l = (1 + t/t1)^(1/2), against (1 + t/t0)^(2/3) for rest content; a mixture's pressure is that of its top-speed part. The supervisor's own derivation (Claude Opus 5.5); not refereed by another model family. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_the_lattice_expands_with_the_static_pulls_coupling_iff_alpha_equals_k_over_four_and_top_speed_walkers_lose_energy_as_one_over_the_length_2026_09_25.py
---

# The lattice expands with the static pull's coupling iff α = K/4, and top-speed walkers lose energy as one over the length

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** bounded-support (exact within block 60's homogeneous kinetic model and the landed member, for uniform content on a closed lattice; the supervisor's own derivation, not refereed by another model family; nothing adopted or registered; unaudited)

This note works within blocks 60, 101, 124 and 129 as landed on main (the homogeneous kinetic model, the static clock law, the kinetic family and the volume power), with blocks 134, 135 and 136 as landed for the kinetic normalization; it reports how a closed lattice with content moves as a whole; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

The landing review of blocks 134–139 left one question open: the member's zero modes. On a closed lattice the member's constraints have a uniform part, and at linear order about a static lattice that part forces the mean energy to vanish. Block 60 (landed) found that a closed lattice with content has no static configuration, but can move uniformly when its kinetic coefficient `c_k` is negative. This note puts the member's own numbers into that motion.

- **T1: the zero mode is an expansion.** The member's clock constraint has no uniform part, so a static closed lattice holds no positive content. On a uniform stretch the member's kinetic term gives `c_k = 12α + 36β`, which is `−24α` at the closing ratio. That is negative, so block 60's uniform motion exists: the lattice expands (or contracts) with `λ̇² = ρ/(24α)`, where `ℓ = e^λ` is the bond length and `ρ` the content's energy per unit volume.
- **T2: the same coupling as the static pull.** The member's static clock law gives the pull between bodies the coupling `G = 1/(16πK)`. The expansion obeys `λ̇² = (8πG/3)ρ` with that same `G` if and only if `α = K/4`. Then the expansion's rate of change obeys `ℓ̈/ℓ = −(4πG/3)(ρ + 3p)`, with `p` the content's pressure.
- **T3: walkers in an expanding lattice.**
  - Content crosses bonds at a rate proportional to `1/ℓ` (block 60's premise). So on a uniformly stretched lattice the massless walk is exactly `H(k)/ℓ`. A top-speed walker keeps its wave vector, and its energy falls exactly as `1/ℓ`. Its pressure is one third of its energy density.
  - A lattice filled with top-speed content expands as `ℓ = (1 + t/t₁)^{1/2}`. With content at rest it expands as `(1 + t/t₀)^{2/3}` (block 60).
  - In a mixture only the top-speed part has pressure.

In plain terms: a closed lattice with anything in it cannot sit still; it must stretch or shrink as a whole. How fast is set by the same number, `α = K/4`, that the books fixed and that makes bodies' pulls consistent with their motion. With that number, the stretching rate and the pull between two bodies are governed by one and the same constant. As the lattice stretches, a walker moving at the top speed keeps its wave pattern on the lattice, but each hop takes longer, so its energy falls in proportion to the stretch.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-25.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom." The memo does not "define a time metric". The member, its kinetic term, the content and its crossing of bonds are supplied clauses. Nothing is adopted.
- **The member's clock constraint** (block 101 as landed): `K R₁ = e`, with `R₁ = ∂_i∂_jh_ij − ∇² tr h`.
- **Block 60's homogeneous model** (landed, T5(b)): on a closed lattice with uniform content of energy `m(λ)` per site, the action `c_k ℓ^s λ̇²/w − w m`, with `ℓ = e^λ` the bond length and `w` the uniform rate. Stationarity in `w` is the constraint, and the length's equation keeps it. Time is labelled so that `w = 1`.
- **The kinetic family and the volume power** (landed). Block 124: the member's kinetic term `α tr(Ḣ²) + β(tr Ḣ)²`, whose value on a uniform stretch is `c_k = 12α + 36β`. Block 129: `s = p + 2 = 3` for the curvature member. Blocks 134–136: `α = K/4` as a necessary condition for the walker's content to meet the member's identity, and the closing ratio `β = −α`.
- **Content and its pressure.** `ρ = m/ℓ³` is the energy per unit volume, since a site has volume `ℓ³`. The pressure `p` is defined by `dm/dλ = −3pℓ³`, the energy's change as the volume changes.
- **Crossing bonds.** Block 60's premise is that bonds are crossed at `√(w_xw_y)/(χ_xχ_y)`, which on a uniform stretch is `w/ℓ`. For the walk this makes the hopping part `H(k)/ℓ`.
- **Standard imports, named at definition level.** The fundamental solution of the Laplacian (`1/p²` is `1/(4πr)`); exact symbolic arithmetic.

## Theorem T1 — the zero mode is an expansion

*Statement.*
- (a) `R₁` has no uniform part. So the uniform part of the clock constraint `K R₁ = e` reads `⟨e⟩ = 0`, and a static closed lattice holds no positive content.
- (b) The member's kinetic term on a uniform stretch `h = 2λδ` is `c_k λ̇²` with `c_k = 12α + 36β`, which is `−24α < 0` at the closing ratio.
- (c) Block 60's uniform motion therefore exists. Its constraint is `m = 24αℓ³λ̇²`, that is `λ̇² = ρ/(24α)`, and the length's equation keeps it for any content `m(λ)`.

*Proof.*
- (a) On a plane wave `R₁ = p²tr h − p·h·p`, which vanishes at `p = 0` (runner B1).
- (b) Direct (runner B2).
- (c) Block 60 T5(b) with `s = 3` and (b). The rate of change of the constraint is `−λ̇` times the length's equation (runner B1). ∎

## Theorem T2 — the same coupling as the static pull

*Statement.*
- (a) The static clock law `u = −e/(4Kp²)` gives, for a body of energy `m`, `u = −Gm/r` with `G = 1/(16πK)`.
- (b) The expansion `λ̇² = ρ/(24α)` is `(8πG/3)ρ` with this `G` if and only if `α = K/4`.
- (c) The length's equation, with the constraint, gives `ℓ̈/ℓ = λ̈ + λ̇² = −(ρ + 3p)/(48α)`. At `α = K/4` this is `−(4πG/3)(ρ + 3p)`.

*Proof.*
- (a) `1/p²` is `1/(4πr)` (runner C1).
- (b) Solve for `α` (runner C1).
- (c) The length's equation at `c_k = −24α`, `s = 3` is `−24αℓ³(2λ̈ + 3λ̇²) − 3pℓ³ = 0`. Substitute the constraint (runner C2). ∎

So `α = K/4`, which the books fixed as a necessary condition (blocks 134–136), is also the value at which the lattice's expansion and the pull between bodies share one coupling. This is a second route to that value, independent of the books (block 144's condition is the books' condition in exchange form). It uses only the landed static clock law and block 60's homogeneous model.

## Theorem T3 — walkers in an expanding lattice

*Statement.*
- (a) On a uniformly stretched lattice the massless walk is `H(k)/ℓ`, with eigenvalues `±|sin k|/ℓ`. A top-speed walker keeps its wave vector, and its energy falls exactly as `1/ℓ` for any history `ℓ(t)`. Top-speed content with `m = ε/ℓ` has pressure `p = ρ/3`.
- (b) At `c_k = −24α`, `s = 3`, the uniform motions are exactly:
  - `ℓ = (1 + t/t₁)^{1/2}` with `t₁ = √(6α/ε)` for top-speed content;
  - `ℓ = (1 + t/t₀)^{2/3}` with `t₀ = (4/3)√(6α/m₀)` for content at rest.
- (c) For a mixture `m = m₀ + ε/ℓ`, the pressure is that of the top-speed part alone, and the constraint is kept.

*Proof.*
- (a) The walk's plane-wave symbol divided by `ℓ`. `H(k)/ℓ(t)` commutes with itself at all times, so each eigenstate keeps its wave vector and its energy is `E(k)/ℓ(t)`. Then `dm/dλ = −m` (runner D1).
- (b) Substitute into the constraint and the length's equation (runner D2).
- (c) Runner E1. ∎

For massive walkers the rest energy does not scale with `ℓ`, so the walk at different lengths does not commute. Their energies follow `√(m² + k²/ℓ²)` only for slow stretching. That is not treated here.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "landing review of blocks 134-139 (unit 27): zero-mode solvability is not established; block 136 as landed requires mean e = 0 and mean P = 0 on a periodic lattice"
source_of_blocker_text: the landing review (ef918c1910; probes deferred-science-20260925 unit 27); block 136 (landed)
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "uniform shear (anisotropic zero modes); massive walkers in a slowly stretching lattice; the member's zero modes on the lattice beyond the homogeneous model; an other-family referee"
conditional_surface_status: "uniform content on a closed lattice; block 60's homogeneous kinetic model with s = 3; unit rate"
hypothetical_axiom_status: "the member, its kinetic term, the content and its crossing of bonds are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 60: rates as multipliers; a closed lattice with content has no static configuration; uniform motion iff `c_k < 0`, with `ℓ ∝ t^{2/s}` for rest content.
  - Block 101: the static clock law.
  - Block 124: the kinetic family, and `c_k = 12α + 36β`.
  - Block 129: `s = p + 2`, the kinetic sign, and the comparator's values `s = 3` and `c_k = −6K`.
  - Blocks 134–136: `α = K/4` as a necessary condition; the closing ratio; the zero-mode restriction.
- **Opened, not landed.** Blocks 144 and 145 (PRs #9230 and #9233): the same `G = 1/(16πK)` from the member's pull at first order.
- **Probes.** The owner's residual task `deferred-20260925-walker-source-closure` names zero-mode solvability among its open questions. No attempt yet.
- **In the literature.**
  - The expansion equations of Friedmann, and their pressure form.
  - The fall of a massless particle's energy with the scale of an expanding space.
  - All reference only.
- **New here:**
  - T1: the zero mode's resolution in the member's own numbers, `c_k = −24α`.
  - T2: the expansion shares the static pull's coupling iff `α = K/4`, a route to that value independent of the books; and the pressure form of the rate of change.
  - T3: the exact `1/ℓ` fall of top-speed walkers' energy, the pressure `ρ/3`, and the `t^{1/2}` expansion.
- **Provenance.** This is the supervisor's own derivation, in the same model family as the probes workers. No other model family has refereed it.

## Exact target and obligation graph

Target: the member's zero mode on a closed lattice with content, in the member's own numbers. The obligations are:
- (O1) no static solution, and the kinetic coefficient on a uniform stretch (T1);
- (O2) the expansion's coupling against the static pull's, and the rate of change (T2);
- (O3) walkers in an expanding lattice, with exact solutions (T3).

T1–T3 discharge them.

## No-Go Discipline Gate

The note's negative sentences:
- a static closed lattice holds no positive content;
- at any `α ≠ K/4` the expansion and the static pull have different couplings.

### N1 — Routes by which the sentences could fail or mislead
1. *The homogeneous model.* Uniform motion is block 60's homogeneous kinetic model with `s = 3`. Anisotropic uniform modes (shear) are not treated.
2. *Content.* Uniform content only. Its pressure comes from how its energy changes with `ℓ`.
3. *Massive walkers.* Their energies follow `√(m² + k²/ℓ²)` only for slow stretching. Not treated.
4. *The static coupling* is from block 101's clock law at unit rate. The pull's velocity terms (block 144) are not needed.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond the supplied member, kinetic term, content and crossing of bonds.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| block 60 (landed) | the homogeneous model; crossing of bonds | yes (restated) |
| block 101 (landed) | the static clock law | yes (restated) |
| blocks 124, 129 (landed) | `c_k = 12α + 36β`; `s = 3` | yes (restated) |
| blocks 134, 135, 136 (landed) | `α = K/4`, `β = −α`; the zero-mode restriction | yes (restated) |
| blocks 144, 145 (open) | the same `G` from the pull | no (comparison) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "a closed lattice with content expands, sharing the static pull's coupling iff `α = K/4`; top-speed walkers' energies fall as `1/ℓ`" | executed: the zero mode of the constraint; `c_k` on the stretch | executed: the homogeneous model's constraint for any content | executed: the couplings and the rate of change | executed: the stretched walk; exact solutions; mixtures | uniform content; the homogeneous model |

### N6 — Partial-closure paths and primitive scan
`kinetic_isotropy_primitive` grants `c_t = c_s` of a kinetic form of the repository. It is not used. `scale_reference_primitive` is not used. Nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "Block 60 already had the uniform motion. This only renames constants."
  - *Reply:* Block 60 had the motion with a free `c_k` and free `K`. Here the member's own kinetic term fixes `c_k = −24α`. The comparison with the static clock law shows that one value, `α = K/4`, makes the stretching rate and the pull between bodies one constant. That is a consistency condition, not a renaming.
  - The walker's `1/ℓ` fall and the `t^{1/2}` law are new.

### N8 — Cross-cycle echo
- Block 60: no static closed lattice; uniform motion iff `c_k < 0`.
- Blocks 124 and 129: `c_k = 12α + 36β`; `s = 3`.
- Blocks 134–136: `α = K/4` from the books.
- This note: `α = K/4` again, from the expansion.

## Falsifiers

- A static closed-lattice solution of the member's constraints with positive content.
- A uniform stretch on which the member's kinetic term gives a value other than `12α + 36β`.
- A top-speed walker whose energy on a uniformly stretched lattice is not `E/ℓ`.
- An error in the runner's algebra.

## Boundaries and non-claims

- Uniform content on a closed lattice; block 60's homogeneous kinetic model with `s = 3`; unit rate.
- Anisotropic uniform modes and massive walkers in a stretching lattice are not treated.
- The uniform motion reaches zero length at `t = −t₀` (or `−t₁`). Nothing is claimed about that endpoint.
- Not refereed by another model family.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 60, 101, 124, 129, 134, 135 and 136 (landed), restated. Blocks 144 and 145 (open), for comparison only.
- Named standard imports, at definition level: exact symbolic arithmetic; the fundamental solution of the Laplacian.

## Review record

- **Who and when.** Supervisor-run block, the ninety-fourth since the source-link direction opened; 2026-09-25.
- **Provenance.** The supervisor's own derivation (Claude Opus 5.5), with exact checks by its own runner. It is not refereed by another model family.
- **Before writing.** The own prior-art check (memory, open PRs, probes attempts, main) found block 60's uniform motion and block 129's comparator values, and no statement tying the expansion's coupling to the static pull, no `1/ℓ` fall of walkers' energy, and no probes attempt on zero modes.
- **Why now.** The landing review of blocks 111–141 (ef918c1910) listed zero-mode solvability as open for blocks 134–139. This note answers it for uniform content within block 60's homogeneous model.
- **Independence.** Mutation census: six mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_lattice_expands_with_the_static_pulls_coupling_iff_alpha_equals_k_over_four_and_top_speed_walkers_lose_energy_as_one_over_the_length_2026_09_25.py
```

Expected: `TOTAL: PASS=14 FAIL=0`.
