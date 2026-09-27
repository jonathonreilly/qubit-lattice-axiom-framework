---
claim_id: if_the_members_leading_action_respects_the_hypercubic_tick_surface_it_is_unique_beta_equals_minus_alpha_and_alpha_equals_k_over_four_follow_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "Conditional classification of leading symbols. Real quadratic forms Q(h,k) in a symmetric 4x4 tensor h, homogeneous of degree two in the Euclidean 4-momentum k (the dimension-4 leading symbol of a local action), exact rational counts. (T1) Under signed permutations of the three space axes with time reversal, 26 forms are invariant and 2 are also invariant under linearised relabellings h -> h + k xi^T + xi k^T; every such form with a nonzero kinetic part has, in block 101's 3+1 read-off, beta/alpha = -1 and a free transverse-traceless speed (the second basis form has no kinetic part). (T2) Under all signed permutations of the four axes (the hyperoctahedral group of Z^4), 9 forms are invariant and exactly 1 is relabelling-invariant; it is proportional to the Euclidean Fierz-Pauli form (manifestly O(4)-invariant), whose read-off has beta/alpha = -1 and transverse-traceless speed 1, i.e. K = 4 alpha at wbar = 1. Counts are unchanged with proper rotations only. Conditional: the member being a symmetric 4-tensor, its leading action being invariant under the Z^4 group and under linearised relabellings, and the identification of block 101's coefficients with Q are premises, not consequences of the axioms or of the approved kinetic_isotropy_primitive (which supplies matter kinetic isotropy and a hypercubic regulator). Leading symbols only: no exact lattice kernel, higher-derivative, nonlinear or reflection-positive realisation is classified; loop protection additionally needs a gauge-invariant regulated action, Ward identities and an exactly conserved source."
upstream_dependencies:
  - minimal_axioms
  - kinetic_isotropy_primitive
  - admissibility_rule_in_the_curvature_member_the_clock_is_a_constraint_a_bodys_change_of_energy_acts_at_once_unless_formation_keeps_energy_local_bounded_theorem_note_2026-09-23
runner: scripts/member_leading_action_on_a_hypercubic_tick_surface_is_unique_2026_09_27.py
---

# If the member's leading action respects the hypercubic tick surface, it is unique: β = −α and α = K/4 follow

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** exact counts and identities in rational arithmetic; a
conditional classification; unaudited; independent checks recorded below.

## In one paragraph

At long wavelengths the campaign's gravity field (the member) has two numbers
besides its strength:
- how its clock trades against its lengths (`β/α`);
- how fast its waves travel (`K/α`).

Requiring that relabelling points in space and time changes nothing fixes the
first, `β = −α`, as block 112 found. With only the symmetries of space, the
second stays free. That is why one light cone needed the separate condition
`α = K/4`.

Suppose the member is a four-dimensional field whose rule treats a step in
time like a step in space, the tick-grained-like-an-edge surface that the
framework approved in June for matter. Then there is exactly one possible
leading action, Einstein's (linearised), and its waves move at the same speed
as everything else. Both of the campaign's central conditions would follow
from that one symmetry.

Whether the member should live on that surface is a premise the owner would
have to accept. It is not supplied by the axioms, and not yet by the approved
primitive, which speaks of matter.

## Why this question

Blocks 134–136 found one light cone for the walker and the member iff
`α = K/4`. Block 112 found that the member's constraint algebra closes on
the lattice iff `β = −α`. The fork probe (2026-09-22) listed "two
polarisations, one speed iff `K = 4α`" as unchecked.

The one-light-cone note of the same date shows that, on the continuous-time
surface, cone identities are not protected by the symmetries of space. The
June `kinetic_isotropy_primitive` puts a matter tick on the same footing as
an edge. The June B4 note shows that this protects matter kinetic terms.

A tensor field is different. Hypercubic symmetry admits 4-index invariants
that full rotations do not; the lattice energy-momentum tensor's split into
two hypercubic irreps is the familiar example. So whether a member placed on
that surface is protected is a question, not a corollary. This note answers
it for the leading (dimension-4) symbol.

## Premises and declared objects

- **Axioms** (`docs/MINIMAL_AXIOMS_2026-06-29.md`). `Z^3` with proper spatial
  cubic rotations; no time metric, dynamics or member.
- **The approved `kinetic_isotropy_primitive`.** It supplies matter kinetic
  isotropy `c_t = c_s` and a hypercubic Euclidean regulator. It does not
  supply covariance of the member under time–space permutations, and it
  supplies no dynamics.
- **Added premises, not derived:**
  - the member is a symmetric four-tensor `h_μν`, with lapse `h_00` and
    shift `h_0i`;
  - its leading action is invariant under the chosen group and under `G`
    below;
  - block 101's coefficients are read off from that action, as below.
- **The member** as in block 101 (supplied):
  `L = [α tr(ḣ²) + β(tr ḣ)²]/w̄ + K w̄(u R_1 + R_2) − e u`.
  Its transverse-traceless speed is `w̄ sqrt(K/(4α))`, and the walker's
  speed is `w̄`.
- **The forms.** `Q(h,k)`, real, quadratic in `h` and in `k` (Euclidean,
  with `k_0` the frequency): the leading symbol of a local action.
- **Symmetries.**
  - `S3`: signed permutations of the three space axes, with time reversal.
    This is the symmetry of the campaign's current surface.
  - `B4`: signed permutations of the four axes.
  - `G`: linearised relabellings `h -> h + k ξ^T + ξ k^T`.
- **Read-off.**
  - Put `h_0μ = 0` and `k = (k_0, 0, 0, 0)`. Then
    `Q = k_0^2 [A Σ h_ij² + B (tr h)²]`, and `β/α = B/A`.
  - The transverse-traceless mode `h_12` with `p` along axis 3 gives the
    spatial coefficient. Its speed squared (Minkowski) is spatial over
    temporal.

## T1 — with only the symmetries of space: β = −α, and the wave speed is free

*Statement.*
- 26 forms are `S3`-invariant. Exactly 2 are also `G`-invariant, spanned by
  `v_0` and `v_1`.
- `v_1` has no kinetic part. For `Q = a v_0 + b v_1` with `a != 0`:
  - `β/α = −1`;
  - the transverse-traceless speed squared is `−b/(2a)`, which is free.

*Proof.* The invariant bases are orbit sums. Gauge invariance is a linear
condition on their coefficients, and its null space is computed exactly
(sympy). ∎

So block 112's closing ratio follows from relabelling invariance, whenever
the form has a kinetic part at all. The one-cone ratio does not. With only
the symmetries of space it is a free parameter, and it can have either sign.

## T2 — on the hypercubic surface the leading form is unique

*Statement.*
- 9 forms are `B4`-invariant, and exactly 1 is also `G`-invariant.
- It is proportional to the Euclidean Fierz–Pauli (linearised
  Einstein–Hilbert) form

  `(1/2) k² h·h − |h k|² + (k·h·k) tr h − (1/2) k² (tr h)²`,

  which is manifestly `O(4)`-invariant: it is built from the Euclidean
  contractions alone. The runner also checks one exact rational rotation.
- Its read-off has `β/α = −1` and transverse-traceless speed squared `1`. In
  block 101's parametrisation that is `K = 4α` at `w̄ = 1`.

*Proof.* Exact, as in T1. The proportionality constant depends on the
normalisation of the null vector and carries no meaning. ∎

*Reflections.* The axioms name proper rotations. With only the proper
subgroups the counts are unchanged:

| group | invariant forms | relabelling-invariant |
|---|---|---|
| proper cubic, with time reversal | 26 | 2 |
| proper cubic, without time reversal | 30 | 2 |
| proper `B4` | 9 | 1 |

So the result does not depend on reflections. This does not derive
time–space mixing from the spatial axioms. That remains a premise.

## What it means, and what it needs

*If* the member is placed on the hypercubic tick surface, as a four-tensor
whose leading action respects `B4` and `G`, then:
- `β = −α` and `K = 4α` are not two conditions to impose. They are what the
  unique leading form says.
- The leading symbol can change only by its overall coefficient under any
  correction that preserves `B4` and `G`.

For loop corrections to preserve `G`, the member's source must be exactly
conserved. That is the campaign's "books balance" programme: exact for free
walkers, lost at third order under one record per site. Conservation is
necessary, not sufficient. A regulated gauge-invariant member action, Ward
identities and anomaly freedom are also needed. That the campaign's two-step
content is the conserved four-dimensional source is not shown here.

On the campaign's current surface, T1 shows that nothing in the symmetry
fixes the member's wave speed, even at tree level.

## What it does not say

- It does not say the member lives on the hypercubic surface. That is an
  owner-level premise extending the approved matter primitive.
- It classifies leading symbols only. It does not classify exact lattice
  kernels, higher-derivative or nonlocal terms, nonlinear vertices, or
  reflection-positive realisations.
- It does not treat order beyond linear in `h`. Whether lattice relabelling
  invariance can hold beyond linear order is the campaign's open nonlinear
  problem (block 150 T5(d)).
- It does not construct a lattice member action on `Z^4` with exact
  linearised lattice relabelling invariance and reflection positivity.
  - The obvious candidate is Fierz–Pauli with `k_μ` replaced by
    `2 sin(k_μ/2)` and fields at half-shifted positions. It is exactly
    `G`-invariant and `B4`-covariant by construction.
  - But the Euclidean Fierz–Pauli form is not bounded below: the conformal
    (trace) mode has the wrong sign. That is the four-dimensional face of the
    member's indefinite trace direction, already met by the campaign (panel
    of 2026-09-25, F0). Positivity must be shown on the constrained
    transverse-traceless sector before real time is reconstructed.
- It does not resolve block 105's tension. On this surface the clock would
  be `h_00` inside a four-dimensional action, not a stretched tick. The
  walker-in-a-field identities would then hold in the continuum limit rather
  than exactly on the lattice.

## Independent checks

- **Codex `gpt-5.6-sol` referee**, at xhigh. Another vendor family; it read
  only the axioms memo, this note's first version, the primitive's note and
  block 101. Verdict on the first version: "the main physical conclusion
  fails; the finite-dimensional classification stands only as a conditional
  mathematical result".
  - **Reproduced by its own enumeration of all 550 monomials:** `26 -> 2`,
    `9 -> 1`, the proper-group counts, the Fierz–Pauli identification up to
    scale, and the 3+1 ratios.
  - **Applied in this revision:**
    - the title and scope are now conditional;
    - the member's `B4` and `G` invariance is an added premise, not a
      consequence of the approved primitive;
    - the meaningless normalisation constant is dropped;
    - "every" is restricted to forms with a kinetic part;
    - the claims are limited to the leading symbol;
    - a conserved source is necessary, not sufficient, for loop
      protection;
    - O(4) invariance is by manifest construction, not one rotation;
    - the proper-rotation counts answer only the reflections question.
- **Claude Fable 5.1 subagent** (same vendor family, not a referee): see the
  PR body.

## Reproduction

```bash
python3 scripts/member_leading_action_on_a_hypercubic_tick_surface_is_unique_2026_09_27.py
```

Expected: `TOTAL: PASS=7 FAIL=0` (under a minute).
