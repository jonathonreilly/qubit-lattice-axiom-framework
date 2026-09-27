---
claim_id: admissibility_rule_under_the_free_particle_stretch_rule_the_seas_energy_stays_bounded_and_a_closed_lattice_that_sees_it_need_not_bounce_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "WITHIN block 147's homogeneous zero-mode model as landed (a supplied scalar constraint 24 alpha l^3 lambdadot^2 = m(lambda) with the filled negative band's instantaneous energy per site as a supplied source) and block 139's staggered mass as landed, with the walk stretched by the free-particle stretch rule of blocks 184 and 185 (pushed) instead of the frame H/l: (T1) every wave's energy is nonincreasing in l, strictly where it moves, and at most sqrt(3 + mu^2) for 0 < l^2 < 2, so the sea's energy per site m_sea(l) is nondecreasing and bounded, with no -I/l divergence as l -> 0; (T2) on block 147's side-4 torus every label is a fixed point of the rule, so the walk does not change at all and m_sea = -(3 + 3 sqrt 2 + sqrt 3)/8 (massless) at every l; the frame's turn at l = I/m0 is replaced by motion at every length (m0 > I) or at none (m0 < I); (T3) on side 6 every moving wave has |v|^2 = 1/4 at l = 1, so m_sea strictly increases there, with pressure ratio 1/12; (T4) in the model a bounce needs m0 below the finite value -m_sea(0+) (between I and sqrt(3 + mu^2)); otherwise a contracting branch reaches l -> 0, and an expanding branch on which m stays positive reaches the rule's end at l = sqrt 2, both in finite time. The instantaneous-source ansatz and the model are block 147's; the stretches of the rule do not commute on larger tori, so adiabatic following is not claimed. The supervisor's own derivation, unrefereed. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_the_members_zero_mode_tests_the_zero_of_energy_if_the_member_sees_the_half_filled_sea_a_closed_lattice_bounces_or_cannot_move_bounded_theorem_note_2026-09-25
  - admissibility_rule_the_books_admit_one_rest_energy_the_staggered_mass_keeps_them_exactly_so_massive_content_meets_the_member_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25
runner: scripts/admissibility_rule_under_the_free_particle_stretch_rule_the_seas_energy_stays_bounded_2026_09_27.py
---

# Under the free-particle stretch rule the sea's energy stays bounded, and a closed lattice that sees it need not bounce

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** bounded-support (exact within blocks 139 and 147 as landed; blocks 180, 184 and 185 are pushed and placed, and the facts used from them are re-derived; the supervisor's own derivation, unrefereed; nothing adopted or registered; unaudited)

This note works within blocks 139 and 147 as landed on main (the staggered mass, and the homogeneous zero-mode model with the filled sea's energy as a supplied source) and re-derives block 147's consequence with the walk stretched by the rule of blocks 184 and 185 instead of the frame; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 147 (landed) worked out the zero-of-energy row of the third column: what happens to a closed lattice if the member sees the filled sea. It used the frame, `H/ℓ`, so each wave's energy scaled as `1/ℓ` and the sea's energy per site was `−I/ℓ`. That diverges as the lattice shrinks, so the lattice turns at `ℓ = I/m₀` for every positive source `m₀`: a bounce. Block 120 (landed) excluded the frame as a source for the member's non-uniform modes. Blocks 184 and 185 (pushed) found the stretch rule under which every wave slows as a free particle does. This note redoes block 147 under that rule.

- **T1: the sea's energy stays bounded.** Every wave's energy falls as the lattice stretches, strictly where the wave moves, and never exceeds `√(3 + μ²)`. So the sea's energy per site is nondecreasing in `ℓ` and bounded. It does not diverge as the lattice shrinks.
- **T2: on block 147's own torus nothing changes.** On the side-4 torus every label is a fixed point of the rule. The walk is the same at every stretch, and the sea's energy per site is `−I = −(3 + 3√2 + √3)/8` throughout. The frame's turn at `ℓ = I/m₀` does not occur. With `m₀ > I` the lattice moves at every length; with `m₀ < I` it cannot move.
- **T3: on larger tori the sea responds.** On side 6 at `ℓ = 1`, every moving wave has `|v|² = 1/4`. So the sea's energy per site strictly increases with `ℓ` there, and it presses with ratio `1/12` (block 180's value).
- **T4: a bounce needs a small source.** In block 147's model a bounce needs `m₀` below the finite value `−m_sea(0⁺)`, which lies between `I` and `√(3 + μ²)`. Otherwise a contracting lattice reaches `ℓ → 0` in finite time. An expanding branch on which the source stays positive reaches the rule's end at `ℓ = √2` in finite time.

In plain terms: block 147 found that a closed lattice which feels the filled sea bounces back before it can shrink away. That was because, with every hop scaled alike, the sea's negative energy grows without limit as the lattice shrinks. With the stretch rule under which each wave slows as a free particle does, the sea's energy stays within fixed limits. On the smallest torus it does not change at all. So the bounce is no longer automatic; it needs a small enough positive source. And an expanding lattice runs into the rule's own limit at a stretch of √2.

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-27) is used for three things: no possibility or site is privileged; the Lattice axiom's sites, bonds and translations; and the memo's silence on amplitude dynamics. Blocks 139 and 147 are used as landed on main. Blocks 180, 184 and 185 are pushed and placed; the facts used from them are re-derived (runner B1, B2, C1, D1).

- **Block 147's model** (landed), quoted:
  - the supplied scalar action with "constraint `24alpha ell³ lambdadot²=m(lambda)`";
  - the frame's sea: "`m_sea=-I/ell`";
  - its turn: "The permitted lengths obey ell>=I/m0.";
  - on side 4: "`I=(3+3sqrt(2)+sqrt(3))/8`".
  - Block 147's qualifiers carry over. The model is not a proven solution of the full lattice constraints. Feeding the instantaneous filled sea into `m` is a supplied source ansatz. The sea energy per site counts each reduced-zone pair once.
- **Block 139** (landed), quoted: "`mε` anticommutes with the walk, so the squared energy is `|sin k|² + m²`".
- **The stretch rule** (blocks 184 and 185, pushed). `k = k₀ + ((ℓ² − 1)/2) sin 2k₀` and `F = sin k₀ (sin² k₀ + ℓ² cos² k₀)^{1/2}` per axis, with the staggered mass unchanged, for `0 < ℓ² < 2`. Under it, every wave obeys `d log E/d log ℓ = −ℓ²|v|²` at fixed label (block 185 T1, re-derived as runner B1).
- **The model's source.** `m(ℓ) = m₀ + m_sea(ℓ)`, with `m_sea(ℓ) = −average_k E(k; ℓ)` over the torus labels, held fixed.

In the literature, a homogeneous model of this kind is the lattice analogue of a closed universe's scale-factor equation (Friedmann's). This note uses none of it as authority.

## Domain qualifications

- Block 147's homogeneous model, and its source ansatz.
- The rule's domain is `0 < ℓ² < 2`.
- On tori larger than side 4 the rule's stretches do not commute (block 180 at first order), so a filled sea need not stay filled. As in block 147's massive case, adiabatic following is not claimed.

## Theorem T1 — the sea's energy stays bounded

*Statement.* For `0 < ℓ² < 2`, every wave's energy is nonincreasing in `ℓ`, strictly where `v ≠ 0`, and `E ≤ √(3 + μ²)`. So `m_sea(ℓ)` is nondecreasing, lies in `[−√(3 + μ²), 0]`, and has a finite limit `m_sea(0⁺)` as `ℓ → 0`.

*Proof.*
- The law gives `d log E/d log ℓ = −ℓ²|v|² ≤ 0` (runner B1).
- `F² = x(x + ℓ²(1 − x))` with `x = sin² k₀`. Its `x`-derivative is `ℓ² + 2x(1 − ℓ²)`, which is positive on `[0, 1]` for `0 < ℓ² < 2`. So `F² ≤ 1` (runner B2).
- A monotone bounded function has a limit. ∎

## Theorem T2 — on block 147's own torus nothing changes

*Statement.* The labels `0`, `π/2` and `π` are fixed points of the rule at every `ℓ`, with `F = 0`, `1` and `0` there. On the side-4 torus every label is one of these. So the walk is the same at every stretch, and `m_sea = −I` with `I = (3 + 3√2 + √3)/8` (massless). In the model, `λ̇² = (m₀ − I)/(24αℓ³)`. It allows every length when `m₀ > I` and none when `m₀ < I`. The frame's turn at `ℓ = I/m₀` does not occur.

*Proof.* `sin 2k₀ = 0` at the three labels. Runner C1 and C2 check the fixed points, the side-4 energy and the model's two cases. ∎

Since the walk does not change, its sea is not excited either: on side 4 the adiabatic question does not arise.

## Theorem T3 — on larger tori the sea responds

*Statement.* On the side-6 torus at `ℓ = 1`, `sin² k ∈ {0, 3/4}`, and every wave with `E > 0` has `|v|² = 1/4`. So each moving wave has `d log E/d log ℓ = −1/4` there, the sea's energy per site strictly increases with `ℓ`, and the sea's pressure ratio is `1/12`.

*Proof.* A wave with `n` moving axes has `E² = 3n/4` and `|v|² = n(3/4)(1/4)/(3n/4)` (runner D1). ∎

## Theorem T4 — a bounce needs a small source

*Statement.* In block 147's model with `m = m₀ + m_sea(ℓ)`:
- The source is smallest as `ℓ → 0`, where it tends to `m₀ + m_sea(0⁺)`, with `I ≤ −m_sea(0⁺) ≤ √(3 + μ²)` (massless: `μ = 0`).
- If `m₀ > −m_sea(0⁺)`, the source is positive at every length. A contracting branch then reaches `ℓ → 0` in finite time: at most `(2/3)√(24α/m_min) ℓ₁^{3/2}` from `ℓ₁`.
- A turning point needs `m₀ < −m_sea(0⁺)`.
- An expanding branch on which `m ≥ m_min > 0` reaches `ℓ = √2`, the rule's end, in finite time.
- Under the frame, `m₀ − I/ℓ` vanishes at `ℓ = I/m₀` for every `m₀ > 0`, so a turn always occurs.

*Proof.* `ℓ̇ = (m/(24αℓ))^{1/2}`, so `dt = (24αℓ/m)^{1/2} dℓ`, integrable on bounded intervals when `m ≥ m_min > 0` (runner E1). The bounds on `m_sea(0⁺)` come from T1: `m_sea` is nondecreasing with `m_sea(1) = −I`. ∎

## What this settles and what it does not

- **Settled.**
  - Under the free-particle stretch rule, block 147's automatic bounce is gone. The sea's energy stays bounded, so a bounce needs a source below a finite value.
  - On block 147's own side-4 torus the walk does not change at all under the rule.
  - An expanding branch meets the rule's end at `√2`.
- **For the third column** (the zero-of-energy row). Its worked consequence, "a closed lattice bounces or cannot move", was the frame's. Under the member's own coupling, completed by the free-particle rule, it becomes: the lattice bounces only for a small enough source, and otherwise moves freely down to small lengths or up to the rule's end.
- **Not settled.**
  - `m_sea(ℓ)` on larger tori away from `ℓ = 1`, which needs the transcendental relabelling.
  - Adiabatic following of the sea on tori larger than side 4.
  - The full lattice constraints beyond block 147's homogeneous model.
  - What happens at `ℓ = √2`, where the rule has no smooth continuation.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "decision-record addendum 65's audit: block 147's zero-mode consequence rests on block 62's frame, excluded as a source by block 120"
source_of_blocker_text: admissibility_rule_the_members_zero_mode_tests_the_zero_of_energy_if_the_member_sees_the_half_filled_sea_a_closed_lattice_bounces_or_cannot_move_bounded_theorem_note_2026-09-25
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "an other-family referee; m_sea(l) on larger tori; adiabatic following"
conditional_surface_status: "exact within block 147's homogeneous model and source ansatz, under the free-particle stretch rule"
hypothetical_axiom_status: "the model, the source ansatz and the stretch rule are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks.**
  - Block 147 (landed): the model, the frame's sea, the bounce, and side 4's `I`.
  - Block 139 (landed): the staggered mass.
  - Block 180 (pushed): the first-order sea under the two-step coupling, and its side-4 and side-6 pressure ratios `0` and `1/12`.
  - Blocks 184 and 185 (pushed): the stretch rule and its law.
- **In the literature.** Homogeneous scale-factor equations with a supplied source, of Friedmann's type. None is used as authority.
- **New here.**
  - Under the rule the sea's energy is bounded, and on side 4 it is constant (T1, T2).
  - Block 147's bounce becomes conditional on a small source (T4).
  - Expanding branches meet the rule's end (T4).
- **Provenance.** The supervisor's own (Claude Opus 5.5), unrefereed.

## Exact target and obligation graph

Target: block 147's zero-mode consequence under the member's own coupling. The obligations are:
- (O1) the premises (A3);
- (O2) monotonicity and the bound (B1, B2);
- (O3) the fixed labels and side 4 (C1, C2);
- (O4) side 6 (D1);
- (O5) the model's times and the frame's turn (E1).

## No-Go Discipline Gate

The note's negative sentences:
- on the side-4 torus, the rule gives no turn at any length;
- no bounce occurs in the model when `m₀ > −m_sea(0⁺)`.

### N1 — Attack routes and the scope they leave
Attack routes, each examined:
1. *A different reference length.* The rule is anchored at the free walk, `ℓ = 1`. Block 184 found that it is not self-similar. ATTEMPTED; stated.
2. *The massive sea.* Covered: the mass is unchanged under the rule (block 185 T1), and the bound holds with `μ`.
3. *Adiabatic excitation.* Not examined beyond side 4.
4. *Beyond the model.* Not examined.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- The following are declared: the model, the source ansatz, the rule, fixed labels.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; sites, bonds, translations; silence on amplitude dynamics | yes |
| block 147 (landed) | the model, the frame's sea, the turn, `I` | yes (quoted, A3) |
| block 139 (landed) | the staggered mass | yes (quoted, A3) |
| blocks 180, 184, 185 (pushed) | the rule, its law, side 6's ratio | re-derived (B1, B2, C1, D1) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "under the rule the sea's energy is bounded, constant on side 4; a bounce needs a small source" | executed: the law's sign, the bound, the fixed labels | executed: side 4 and the model's cases | executed: side 6 at `ℓ = 1` | executed: the finite times and the frame's turn | not executed: `m_sea(ℓ)` on larger tori away from `ℓ = 1` |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "Side 4 is a degenerate torus; its fixed labels make the result trivial."
  - *Reply:* It is block 147's own worked torus, which is why it is shown. T1 and T4 hold on every torus.

### N8 — Cross-cycle echo
- Block 147: under the frame a closed lattice that sees the sea bounces or cannot move.
- Block 180: the first-order sea under the two-step coupling.
- Blocks 184 and 185: the stretch rule.
- This note: under the rule the bounce needs a small source.

## Falsifiers

- A torus and a stretch below `√2` where a wave's energy increases with `ℓ` under the rule.
- A label on the side-4 torus that the rule moves.

## Boundaries and non-claims

- Block 147's homogeneous model and source ansatz; the rule's domain.
- The model, the source ansatz and the rule are supplied.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 139 and 147 (landed), quoted. Blocks 180, 184 and 185 (pushed), placed and re-derived.
- Named standard imports, at definition level:
  - monotone bounded functions have limits;
  - integration of a first-order equation for a length;
  - exact symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run block (Claude Opus 5.5), 2026-09-27, during the owner's second 12-hour campaign.
- **Provenance.** The supervisor's own derivation, unrefereed.
- **Before writing.**
  - Origin was re-fetched. Blocks 139 and 147 were read as landed, and blocks 180, 184 and 185 on their branches.
  - Decision-record addendum 65's audit lists block 147 as re-derived only at first order (block 180). This note is the all-orders re-derivation within block 147's model.
- **Mutation census.** One mutation per science family, each failing only in its own family, and two in family G.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_under_the_free_particle_stretch_rule_the_seas_energy_stays_bounded_2026_09_27.py
```

Expected: `TOTAL: PASS=14 FAIL=0`.
