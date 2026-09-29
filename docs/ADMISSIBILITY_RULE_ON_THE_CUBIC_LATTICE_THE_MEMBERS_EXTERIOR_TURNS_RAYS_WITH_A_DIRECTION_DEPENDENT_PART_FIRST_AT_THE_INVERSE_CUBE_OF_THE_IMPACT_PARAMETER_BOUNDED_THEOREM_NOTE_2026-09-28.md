---
claim_id: admissibility_rule_on_the_cubic_lattice_the_members_exterior_turns_rays_with_a_direction_dependent_part_first_at_the_inverse_cube_of_the_impact_parameter_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "WITHIN block 60's curvature member and block 110's exterior, index and long-wave ray model as landed, at first order in the charges, for content at one site or with the cubic point symmetry about a site: (T1) the exterior is chi - 1 = Q G and 1 - N = P G with G the unit-source potential of the nearest-neighbour Laplacian on Z^3, so the index is n = 1 + (3a + p) 4 pi G; from the lattice symbol, G = G0 + G1 + G2 + G3 + O(r^-9) with G1 = (5 sum x^4 - 3 r^4)/(32 pi r^7) (already landed, 2026-06-07) and G2, G3 explicit (each satisfies the lattice equation away from the source at its order; none has an l = 0 part; the expansion's existence and remainder are imported); the fields' relative anisotropy is (5 sum x^4/r^4 - 3)/(8 r^2); (T2) the first-order turn toward the body is (3a + p)[2/b + 2 f1/b^3 + 4 f2/b^5 + ...] with a sideways part (3a + p)[f1'/b^3 + f2'/b^5 + ...] along t x beta, where f1 = (1/4) sum t^4 + sum t^2 beta^2 + (2/3) sum beta^4 - 3/4 and f2 is G2's line integral; (T3) the table for the axis (f1 = cos 4 phi/6), the face diagonal and the body diagonal (f1 = 0 identically, first anisotropy -(4/135) cos 6 phi at b^-5); f1 averages to zero over the azimuth; (T4) at a = p = M/2 the axis lattice term against the continuum second-order term has ratio 8/(45 pi M b). Exact (sympy) for the expansion terms, their local equations and the line integrals; the ray-turn formula is first-order ray perturbation (named), checked by direct ray integration in floating point by the probe and the referee. A harvest of probe HIT #9364 (a Claude Opus 5.5 worker), refereed by Claude Sonnet 5 (same vendor family; the owner ruled on 2026-09-28 that a Sonnet referee counts). Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_around_a_body_the_walks_rays_match_the_comparators_at_every_order_exactly_when_its_two_charges_agree_and_they_agree_only_when_hop_energy_balances_the_slowed_clocks_bounded_theorem_note_2026-09-24
runner: scripts/admissibility_rule_on_the_cubic_lattice_the_members_exterior_turns_rays_with_a_direction_dependent_part_2026_09_28.py
---

# On the cubic lattice the member's exterior turns rays with a direction-dependent part, first at the inverse cube of the impact parameter

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** bounded-support (exact at first order in the charges within block 110 as landed, with the lattice potential's expansion imported; a harvest of probe HIT #9364, refereed by Claude Sonnet 5; nothing adopted or registered; unaudited)

This note works within block 60's curvature member and block 110's exterior and ray model as landed; it reports how the cubic lattice changes the turn of long-wave rays around a body at first order in its charges; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 110 (landed) found that outside a spherical body the curvature member's fields are `χ = 1 + a/r` and `N = 1 − p/r`, and that the walk's long-wave rays see the index `n = χ³/N`. That is a continuum statement. Block 110 left the lattice's corrections open. Probe HIT #9364 answered them at first order in the charges; this note harvests it with the referee's scope.

- **T1: the lattice exterior.**
  - At first order the exterior is exactly `χ − 1 = Q G` and `1 − N = P G`, where `G` is the cubic lattice's unit-source potential. So the index is `n = 1 + (3a + p) 4πG`.
  - `G` expands as `G₀ + G₁ + G₂ + G₃ + O(r⁻⁹)`, with `G₀ = 1/(4πr)` and `G₁ = (5Σx⁴ − 3r⁴)/(32πr⁷)`. `G₁` is already landed (the 2026-06-07 cubic-anisotropy note). `G₂` and `G₃` are given here from the lattice symbol.
  - The fields' relative anisotropy is `(5Σx⁴/r⁴ − 3)/(8r²)`: `+1/(4r²)` on an axis, `−1/(16r²)` on a face diagonal and `−1/(6r²)` on a body diagonal.
- **T2: the turn.** For a ray of direction `t` at impact parameter `b` in direction `β`:
  - toward the body the turn is `(3a + p)[2/b + 2f₁/b³ + 4f₂/b⁵ + …]`;
  - there is also a sideways part `(3a + p)[f₁′/b³ + f₂′/b⁵ + …]` along `t × β`, out of the plane that holds the ray and the body;
  - here `f₁ = ¼Σt⁴ + Σt²β² + ⅔Σβ⁴ − ¾`, and `f₂` is `b⁴` times the line integral of `4πG₂`.
- **T3: by direction.**
  - Along an axis, `f₁ = cos 4φ/6`.
  - Along a face diagonal, `f₁ = −cos 2φ/12 + cos 4φ/8`.
  - Along a body diagonal, `f₁ = 0` identically, and the first anisotropy is `f₂ = −(4/135) cos 6φ`, at `b⁻⁵`.
  - Averaged over the azimuth `φ`, every correction vanishes, so the averaged turn is the continuum's `2(3a + p)/b`.
- **T4: the size.** With equal charges `a = p = M/2`, along an axis at `φ = 0`, the lattice's `b⁻³` term is smaller than the continuum's second-order term `(15π/4)(M/b)²` unless `Mb < 8/(45π)`.

In plain terms: on a cubic lattice, the pull of a small lump is not quite the same in every direction. So a ray passing the lump bends slightly more or less depending on its direction, and it can also be nudged sideways, out of the plane of the lump and the ray. The first such effect is weaker than the main bend by the square of the impact distance in lattice units. Rays along a cube's body diagonal do not feel it at that order. Averaged over directions around the ray, the effect cancels.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-28.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom."
  - The member, its exterior and the ray model are supplied clauses. Nothing is adopted.
- **Block 110** (landed), quoted: outside a spherical body "the curvature member's two fields are `χ = 1 + a/r` and `N = wχ = 1 − p/r`", and the rays see "`n = χ³/N = (r + a)³/(r²(r − p))`". The normalisation is `a = Q/4π`, `p = P/4π`.
- **The lattice potential.** `G` solves `−ΔG = δ₀` for the nearest-neighbour Laplacian on `Z³` and vanishes at infinity.
- **First order in the charges.** Block 110 T2(a)'s site equations with the right-hand sides at zero field. Content sits at one site, or has the cubic point symmetry about a site.
- **Imports, named at definition level.**
  - The asymptotic expansion of the lattice potential in homogeneous terms, generated from the symbol `σ(k) = 2Σ(1 − cos k_i)` (Duffin, 1953; Maradudin and others; Martinsson and Rodin). Its existence and remainder bounds are imported.
  - The transforms of `|k|^{−2m}` in three dimensions: `1/(4πr)`, `−r/(8π)`, `r³/(96π)`, `−r⁵/(2880π)`.
  - First-order ray perturbation: the change of direction is the transverse gradient of the line integral of `n − 1` along the unperturbed line (Born's approximation for rays).
  - Exact symbolic arithmetic.

## Prior art and what is new

- **`G₁` is landed.** `GRAVITY_LEADING_LATTICE_CORRECTION_CUBIC_ANISOTROPY_THEOREM_NOTE_2026-06-07` states "`G(r) = 1/(4π r) + [5/(32π)]·K₄(n̂)/r³ + O(1/r⁵)`", the same expression. The probe's claim that no landed note contains it was wrong; the referee caught it.
- **Classical.** The expansion of the simple-cubic lattice potential (Duffin; Maradudin and others; Martinsson and Rodin).
- **Block 110** (landed): the continuum exterior and the index.
- **Probe HIT #9364** (a Claude Opus 5.5 worker, `w-jonathonsmac4f50-jae40`): the answer harvested here.
- **The referee** (Claude Sonnet 5, 2026-09-28).
  - Re-derived `G₁` from the lattice equation (unique) and `G₁`, `G₂`, `G₃` by a separate spectral route (Hankel transforms).
  - Compared them with the exact lattice potential from the Bessel integral out to `r ≈ 40` along several directions, in floating point.
  - Checked the tables by exact lattice line sums along lattice directions, and the turn by integrating rays, including the sideways part for a face-diagonal and a generic ray.
- **New here.** `G₂` and `G₃` as applied to the member, the turn to `b⁻⁵` with its sideways part, the tables, and the structure (odd powers only; zero azimuthal averages). All of it is harvested with the referee's scope and re-derived by the supervisor's runner.

## Theorem T1 — the lattice exterior

*Statement.*
- (a) At first order in the charges, `χ − 1 = QG` and `1 − N = PG` at every site, and `n − 1 = (3a + p)4πG`.
- (b) From `1/σ = 1/|k|² + B/|k|⁴ + B²/|k|⁶ + B³/|k|⁸ + …`, with `B = Σk⁴/12 − Σk⁶/360 + Σk⁸/20160`, and the transforms of `|k|^{−2m}`:
  - `G₁ = (5Σx⁴ − 3r⁴)/(32πr⁷)`;
  - `G₂ = −Σ∂_i⁶ r/(2880π) + Σ∂_i⁴Σ∂_j⁴ r³/(13824π)`;
  - `G₃` likewise.
- (c) `G₁`, `G₂` and `G₃` satisfy the lattice equation `−Δ_lat G = 0` away from the source at orders `r⁻⁵`, `r⁻⁷` and `r⁻⁹`.
- (d) `G₁` is the only degree `−3` cubic-invariant correction the local equation allows: the only cubic-invariant quadratic is `r²`, and `c/r³` is harmonic only for `c = 0`.
- (e) Neither `G₁` nor `G₂` has an `l = 0` part.
- (f) The fields' relative anisotropy is `G₁/G₀ = (5Σx⁴/r⁴ − 3)/(8r²)`.

*Proof.*
- (a) Block 110 T2(a) at zero field. `χ³/N = 1 + 3(χ − 1) + (1 − N)` at first order.
- (b)–(e) are exact symbolic computations (runner B1–B4). (f) is runner C1.
- The expansion's existence and its `O(r⁻⁹)` remainder are the named import. At degree `−5` the local equation leaves an `l = 4` harmonic free, which the symbol fixes. The referee's comparison with the exact potential confirms `G₂` and `G₃` numerically. ∎

## Theorem T2 — the turn

*Statement.* At first order in the charges the change of a ray's direction is `∇_b Ψ`, with `Ψ = (3a + p)[−2 ln b + f₁/b² + f₂/b⁴ + …]`, where `f_k/b^{2k}` is the line integral of `4πG_k` along the unperturbed line `bβ + st`.
- So the component toward the body is `(3a + p)[2/b + 2f₁/b³ + 4f₂/b⁵ + …]`.
- The sideways component is `(3a + p)[f₁′/b³ + f₂′/b⁵ + …]` along `t × β`, where `′` is the derivative in the azimuth.
- `f₁ = ¼Σt⁴ + Σt²β² + ⅔Σβ⁴ − ¾`.

*Proof.* First-order ray perturbation, the named import (block 110 T1's rays of `c = 1/n`). The line integrals are exact: `∫s^{2j} ds/(b² + s²)^{m+½} = b^{2j−2m}Γ(j + ½)Γ(m − j)/Γ(m + ½)` (runner D1, D2). The probe integrated rays directly in floating point and found agreement to `3 × 10⁻⁷`, including the sideways part for an axis ray. The referee did so for a face-diagonal and a generic ray. ∎

## Theorem T3 — by direction

*Statement.* With `φ` measured from `e₁` for the axis `e₃`, from `e₃` for the face diagonal `(1,1,0)/√2`, and from `(1,−1,0)/√2` for the body diagonal:

| ray direction | `f₁` (order `b⁻³`) | `f₂` (order `b⁻⁵`) |
|---|---|---|
| axis | `cos 4φ/6` | `(3/20) cos 4φ + (5/24) cos 8φ` |
| face diagonal | `−cos 2φ/12 + cos 4φ/8` | `(19/192) cos 4φ − (1/10) cos 6φ + (15/128) cos 8φ` |
| body diagonal | `0` identically | `−(4/135) cos 6φ` |

Averaged over `φ`, `f₁` is zero: for these three directions and for the direction `(2, 3, 6)/7`, and for every direction by the circle moments `⟨β_iβ_j⟩ = P_ij/2`, `⟨β_i⁴⟩ = 3P_ii²/8`, `P = 1 − tt`. So the averaged turn is the continuum's at order `b⁻³`. Since each `G_k` has only `l ≥ 2k` parts, every order averages to zero (the probe's argument; checked here through `k = 2`).

*Proof.* Runner D1 and D2, exact. The body diagonal's `f₁` vanishes because `Σβ_i⁴ = ½` and `Σt_i²β_i² = ⅓` for every `β ⊥ (1,1,1)`. ∎

## Theorem T4 — the size

*Statement.* With `a = p = M/2` (equal charges, block 110's comparator case), along an axis at `φ = 0`, the ratio of the lattice's `b⁻³` term to the continuum's second-order term `(15π/4)(M/b)²` is `8/(45πMb)`.

*Proof.* `(3a + p)·2f₁/b³` with `f₁ = 1/6`, divided by `(15π/4)M²/b²` (runner E1). This compares a first-order lattice term with a continuum second-order term; the lattice's own second order is not computed. ∎

## What this settles and what it does not

- **Settled** (first order in the charges, within the premises).
  - The member's lattice exterior is `Q G` and `P G`.
  - The rays' first direction-dependent turn is at `b⁻³` with the angular content `f₁`, zero only on the body diagonal, plus a sideways part.
  - There are no `b⁻²` or `b⁻⁴` terms.
  - Averaged over the azimuth, the turn is the continuum's.
- **For block 110.** Its "lattice corrections to the exterior" are answered at first order in the charges, for content with the cubic point symmetry. For such content the `b⁻³` term does not depend on the body's size, and structure-dependent terms begin at `b⁻⁵`.
- **Not settled.**
  - Second order in the charges on the lattice.
  - The walker's own finite-wave-number dispersion, a separate direction dependence.
  - Content without the cubic symmetry, where a quadrupole competes at `b⁻³`.
  - The expansion's remainder bounds (imported).

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
- First order in the charges.
- Content at one site or with the cubic point symmetry.
- The turn is for the smooth continuum extension of the site fields (block 110's ray model).
- The tables are for three directions, and the `f₁` formula holds for every direction.

### N2 — Wall independence
No repository no-go wall is used.

### N3 — Supplied structure
The member and the ray model are supplied, and the expansion is imported.

### N4 — Dependencies
Block 110 (landed; quoted); the 2026-06-07 note (landed; quoted, prior art for `G₁`).

### N5 — Resolution
- per_element: executed - the lattice symbol's expansion and the transforms of |k|^-2m
- per_site: executed - G1, G2, G3 from the symbol; the lattice equation away from the source at orders r^-5, r^-7, r^-9; G1 against the landed 2026-06-07 form
- per_mode: executed - the line integrals of 4 pi G1 and 4 pi G2 along the axis, face and body diagonals, and for the direction (2,3,6)/7
- per_block: executed - uniqueness of G1; no l = 0 parts; the azimuthal averages; the size against the continuum second order
- lattice_wide: checked and not executed - the remainder bound of the expansion (imported; the referee compared with the exact lattice potential out to r about 40 in floating point); rays integrated directly (floating point in the probe and the referee); second order in the charges; finite wave number

### N6 — Primitive boundary
No new primitive, selection or physical interpretation is adopted.

### N7 — Strongest objection
"The expansion is only asymptotic." Agreed: its existence and remainder are imported, and the tables hold to the stated orders in `1/b`. The referee's comparison with the exact potential supports them.

### N8 — Earlier claims
The probe's HIT said no landed note contains `G₁`. That was wrong: the 2026-06-07 note does. It is credited here.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 110 N1: lattice corrections to the exterior"
source_of_blocker_text: probes task J:derive:the-members-exterior-on-the-lattice (after block 110)
reachability_to_target: advances
next_trace_action: "second order in the charges on the lattice; the walker's finite-wave-number dispersion"
```

## Review record

- **Author checks (not a review PASS).** The supervisor's own runner, exact, `TOTAL: PASS=17 FAIL=0`. Mutation census 7/7, each failing in its own family only.
- **Provenance.**
  - Derived by probe worker `w-jonathonsmac4f50-jae40` (Claude Opus 5.5), HIT #9364, `check.py` 37/0.
  - Refereed by Claude Sonnet 5 on 2026-09-28: confirmed with scope corrections, all applied here (the prior art for `G₁`, the imported expansion, the ray-model scope, the size comparison's limits). Same vendor family; the owner ruled on 2026-09-28 that a Sonnet referee counts for harvest.
  - Harvested by the supervisor (Claude Opus 5.5), with its own runner.
