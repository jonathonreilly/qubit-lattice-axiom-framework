---
claim_id: dynamics_clause_the_compression_update_is_the_one_distant_update_consistent_with_locality_of_marginals_and_affine_joint_laws_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Inside the Hilbert-space kinematics that the dynamics clause brings (open PR 9083), take locality of marginals at equal time (D-loc) and the one-site Born law of open PR 9083, whose orientation comes from the support condition of the compression update (D-perm). Consider records at two sites whose joint law is affine (effects E_qr >= 0) and whose marginals are each site's Born law whatever the other does. (i) Then E_qr = P_q (x) P_r: each E_qr lies below P_q (x) I and below I (x) P_r, whose ranges meet in the line spanned by |q r>, so E_qr = c_qr P_q (x) P_r, and the marginal conditions have the unique solution c_qr = 1. (ii) If the partner's state after record q is to reproduce this joint law along every axis, it must be the Lueders conditional state Tr_i[(P_q (x) I) rho (P_q (x) I)] / p_q (200 random pairs, deviation 1e-15). A reset update that leaves the partner unchanged misses the joint law on a singlet by exactly |a.b|/4, reaching 1/4 for parallel axes. (iii) With three qubits, two-qubit tomography of the rest after a record reproduces the rest's Lueders compression (deviation 6e-15). (iv) The support condition puts each effect of a two-possibility menu on its possibility; completeness e1 P1 + e2 P2 = I then holds only for antipodal possibilities, with e1 = e2 = 1. Scope: open PR 9083 used this distant update as a premise for steering, and the joint affinity used here comes from that steering. So this is a self-consistency and uniqueness result: the distant update that D-perm supplies is the one update consistent with D-loc, affine joint laws and Born marginals. It does not derive the collapse from D-loc and the lock: a replacement update that keeps the lock passes D-loc with non-Born laws (open PR 9083, Theorem 6). No derivation of the kinematics, D-loc, D-perm, joint affinity, or of menus with three or more possibilities is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_compression_is_the_consistent_distant_update_2026_09_24.py
---

# The compression update is the one distant update consistent with locality of marginals and affine joint laws

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** a self-consistency and uniqueness result inside supplied quantum
kinematics, with finite certificates; unaudited.

## Result

The campaign supplied the compression update (D-perm, open PR 9041): a
record `q` at site `i` replaces the global state by
`(P_q ⊗ I) ρ (P_q ⊗ I) / p_q`. That update has three parts:
- **The lock.** Site `i` ends in `P_q`. This is close to the Record axiom's
  "locks exactly one admissible local possibility".
- **The support condition.** The compressed state must exist whenever `q`
  can form. Open PR 9083 uses it to orient the Born law.
- **The distant update, or collapse.** Every other site takes its
  conditional state. Open PR 9083 uses it for steering.

This note checks the distant part for consistency. Take locality of
marginals (D-loc), an affine joint law for two records, and each site's
Born law as its marginal:
- **Joint laws are product projectors.** The joint law must be
  `P_q ⊗ P_r`.
- **So the distant update is compression.** The partner's state after a
  record must reproduce that joint law along every axis. That fixes it as
  the Lüders conditional state.
- **Reset fails.** Leaving the partner unchanged contradicts the joint law
  on entangled pairs.

**What this is and is not.** Open PR 9083's steering assumed the distant
update, and the joint affinity used here comes from that steering. So this
does not derive the collapse from D-loc and the lock. It shows the premise
is self-consistent and unique: no other distant update fits D-loc, affine
joint laws and Born marginals. The lock alone does not give it. A
replacement update that keeps the lock passes D-loc with non-Born laws
(open PR 9083, Theorem 6).

## Setting and decision points

- **Kinematics.** The Hilbert-space kinematics the clause brings (open PR
  9083): density operators, tensor products, purifications.
- **D-loc.** At the moment distant records form, a site's marginal record
  distribution does not depend on whether, or how, they form (open PR
  9083).
- **The one-site Born law.** `P(q | ρ) = Tr(P_q ρ)` (open PR 9083). Its
  orientation comes from D-perm's support condition.
- **Joint affinity.** A pair's joint record law is affine in the pair's
  state. This is the steering argument of open PR 9083 applied to a pair,
  with a distant partner that purifies the pair. That steering uses the
  distant update.
- **A partner state.** After a record, the partner has a state that
  reproduces the joint law. This is the form of update being tested.

None is adopted.

## Theorem 1 — joint laws are product projectors

Let `E_qr ≥ 0` be the joint effects for record `q` at site `i` and `r` at
site `j`. D-loc fixes the marginals:
- `Σ_r E_qr = P_q ⊗ I`: site `i`'s law does not change when `j` records;
- `Σ_q E_qr = I ⊗ P_r`: and the same with the roles swapped.

**Proof.**
- Each `E_qr ≤ P_q ⊗ I` and `E_qr ≤ I ⊗ P_r`. So `E_qr` is supported
  where the two ranges meet, which is the line spanned by `|q⟩|r⟩`. Hence
  `E_qr = c_qr P_q ⊗ P_r`.
- Then `Σ_r c_qr P_q ⊗ P_r = P_q ⊗ I` forces `c_(q,r) = c_(q,−r) = 1`,
  since `P_q ⊗ P_r` and `P_q ⊗ P_(−r)` are linearly independent. ∎

The runner checks that all four range intersections have dimension 1. It
also checks that the marginal conditions, as a linear system in the four
`c`'s, have rank 4 and the unique solution `c = 1`.

## Theorem 2 — the distant update consistent with it is compression

After record `q` at `i`, let the partner's state be `τ_q`. For every axis
`b` at `j` it must give `P(r | q) = Tr((P_q ⊗ P_r) ρ) / p_q`. Records along
three axes determine a qubit state, so

    τ_q = Tr_i[(P_q ⊗ I) ρ (P_q ⊗ I)] / p_q .

That is the Lüders conditional state.
- **Pairs.** On 200 random pairs (ranks 1 to 4) the reconstruction matches
  it to 1e-15. As the independent check notes, this is close to a
  tautology: the reconstruction is a partial trace. Its content is
  uniqueness.
- **The rest.** With a third qubit, full two-qubit tomography of the rest
  reproduces the Lüders compression of the rest to 6e-15 (100 random
  states). ∎

**Reset fails.** Leaving the partner unchanged gives `p_q p_r`. On a
singlet this differs from `Tr((P_q ⊗ P_r) ρ)` by exactly `|a·b|/4`, which
reaches 1/4 for parallel axes. So the distant update cannot be skipped.
That same update is what gives the Bell values of open PR 9043.

## Theorem 3 — two-possibility menus are antipodal

Let a qubit record have two possibilities `q₁`, `q₂`, with effects `E₁`, `E₂`.
- D-perm's support condition (open PR 9083, Theorem 4) puts each effect on
  its possibility: `E_k = e_k P_{q_k}`.
- Completeness (the menu's normalization) then requires
  `e₁ P₁ + e₂ P₂ = I`. That holds only when `P₁ ⊥ P₂`, that is, antipodal
  Bloch vectors, and then `e₁ = e₂ = 1`. ∎

The runner shows the completeness residual is zero at 180°. It is 0.219,
0.816 and 0.975 at 162°, 90° and 36°. So two-possibility menus are
projective and antipodal, given the support condition and normalization.
Menus with three or more possibilities, such as trines, are not treated.

## What this means for the lanes

- **Born lane.** Inside the supplied kinematics, the campaign's
  quantum-probability rules form a self-consistent set:
  - D-perm (the lock, the support condition, the distant update);
  - D-tr (the law sees the site's conditional state);
  - D-loc at equal time;
  - two-possibility menus.

  Given these, the trace rule, the Born orientation and antipodal menus
  follow (open PR 9083 and Theorem 3). The distant update is the one
  consistent with D-loc, affine joint laws and Born marginals (Theorems 1
  and 2).
- **Record axiom.** The lock is close to the axiom's own text. The support
  condition and the distant update are not in the axiom text; they are
  supplied.
- **Prior art.** No-signalling arguments of this kind are standard (Simon,
  Bužek and Gisin 2001, who assume the projection postulate). They are
  cited as prior art, not as premises.

## Checks

The runner has 5 checks and all pass in under 1 s.

| Check | Result |
|---|---|
| Product projectors | All four range intersections have dimension 1. The marginal system in the four `c`'s has rank 4 and the unique solution `c = 1` (residual 1e-15). |
| Compression on the partner | 200 random pairs, largest deviation 1.1e-15. |
| Reset fails | The gap on a singlet equals `|a·b|/4` to 2e-16 over 100 random axis pairs. It is 0.250 at parallel axes. |
| The whole rest | 100 random three-qubit states, largest deviation 6.4e-15. |
| Antipodal menus | Completeness residual 0 at 180°; 0.219, 0.816 and 0.975 at 162°, 90° and 36°. |

## Independent checks

A separate checker wrote its own code without reading this runner. A later
adversarial review of the whole chain ran its own checks.
- **Confirmed.** The range intersections (800 of 800 cases). A dual
  certificate that the only valid joint law is `P_q ⊗ P_r`. The partner
  and three-qubit reconstructions. The antipodal residuals. The trine
  `E_k = (2/3) P_k` escapes, as this note says.
- **Flagged, now addressed.**
  - The first version claimed the distant collapse follows from D-loc and
    the lock. That is circular, since the joint affinity comes from
    steering that assumes the distant update. The note now states a
    self-consistency and uniqueness result.
  - The orientation comes from the support condition, not the lock.
  - The proof's positivity step gave only `c ≥ 1`. The proof now uses the
    marginal conditions, which fix `c = 1` directly.
  - The reset gap is `|a·b|/4`, not the sampled 0.243.

## What this does not do

- It adopts no decision point. It does not derive the kinematics, D-loc,
  D-perm, the lock or joint affinity.
- It uses two-possibility records on qubits. Menus with three or more
  possibilities are not treated.
- Joint affinity rests on the steering argument of open PR 9083, applied
  to pairs. That step is argued, not separately computed.
