---
claim_id: dynamics_clause_a_record_updates_the_rest_of_the_lattice_by_compression_locality_of_marginals_forces_product_projector_joint_laws_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Take locality of marginals (D-loc) and the one-site Born law P(q | rho) = Tr(P_q rho) of open PR 9083, whose orientation uses only the lock: a record q leaves its own site in P_q. Consider records at two sites whose joint law is affine (effects E_qr >= 0) and whose marginals are each site's Born law whatever the other does. (i) Then E_qr = P_q (x) P_r: the ranges of P_q (x) I and I (x) P_r meet in one line, and E_(-q,-r) >= 0 forces full weight on it. (ii) Requiring that the partner's state after record q reproduce the joint law along every axis then gives the Lueders conditional state Tr_i[(P_q (x) I) rho (P_q (x) I)] / p_q (200 random pairs, deviation 1e-15). A reset update, which leaves the partner unchanged, misses the joint law by up to 0.243 on a singlet. (iii) With three qubits, two-qubit tomography of the rest after a record reproduces the rest's Lueders compression (deviation 3e-15). So the global compression update of open PR 9041 (D-perm), the 'collapse' at distant sites, follows from D-loc and the site-local lock. No derivation of D-loc, of the lock or of joint affinity beyond the steering argument of open PR 9083 is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_collapse_from_locality_of_marginals_2026_09_24.py
---

# A record updates the rest of the lattice by compression

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** conditional derivation with finite certificates; unaudited.

## Result

The campaign has supplied the compression update (D-perm, open PR 9041):
a record `q` at site `i` replaces the global state by
`(P_q ⊗ I) ρ (P_q ⊗ I) / p_q`. That update has two parts:
- **The lock.** Site `i` ends in `P_q`. This is what the Record axiom's
  "locks exactly one admissible local possibility" says for the site itself.
- **The distant update, or collapse.** Every other site takes its
  conditional state.

This note derives the second part from the first and locality of marginals
(D-loc):
- **Joint laws are product projectors.** Take two records' joint law, with
  each marginal the site's Born law whatever the other site does. It must
  be `P_q ⊗ P_r`.
- **So the distant update is compression.** The partner's state after a
  record must reproduce that joint law along every axis. That fixes it as
  the Lüders conditional state.

Leaving the partner unchanged, a "reset", contradicts the joint law on
entangled pairs.

## Setting and decision points

- **D-loc.** A site's marginal record distribution does not depend on
  whether, or how, distant records form (open PR 9083).
- **The one-site Born law.** `P(q | ρ) = Tr(P_q ρ)` (open PR 9083). Its
  orientation uses only the lock at the recorded site.
- **Joint affinity.** A pair's joint record law is affine in the pair's
  state. This is the steering argument of open PR 9083 applied to a pair,
  with a distant partner that purifies the pair.

None is adopted.

## Theorem 1 — joint laws are product projectors

Let `E_qr ≥ 0` be the joint effects for record `q` at site `i` and `r` at
site `j`. D-loc fixes the marginals:
- `Σ_r E_qr = P_q ⊗ I`: site `i`'s law does not change when `j` records;
- `Σ_q E_qr = I ⊗ P_r`: and the same with the roles swapped.

**Proof.**
- Each `E_qr ≤ P_q ⊗ I` and `E_qr ≤ I ⊗ P_r`. So `E_qr` is supported where
  the two ranges meet, which is the line spanned by `|q⟩|r⟩`. Hence
  `E_qr = c_qr P_q ⊗ P_r`.
- The marginal conditions give `E_(−q,−r) = P_(−q) ⊗ P_(−r) + (c_qr − 1) P_q ⊗ P_r`.
  This is positive only if `c_qr = 1`. ∎

The runner checks that the ranges meet in dimension 1. It also checks that
the smallest eigenvalue of `E_(−q,−r)` is `c − 1`, which is negative for
`c < 1`.

## Theorem 2 — the distant update is compression

After record `q` at `i`, let the partner's state be `τ_q`. For every axis
`b` at `j` it must give `P(r | q) = Tr((P_q ⊗ P_r) ρ) / p_q`. Records along
three axes determine a qubit state, so

    τ_q = Tr_i[(P_q ⊗ I) ρ (P_q ⊗ I)] / p_q .

That is the Lüders conditional state.
- **Pairs.** On 200 random pairs (ranks 1 to 4) the reconstruction matches
  it to 1e-15.
- **The rest.** With a third qubit, full two-qubit tomography of the rest
  reproduces the Lüders compression of the rest to 3e-15 (100 random
  states). ∎

**Reset fails.** Leaving the partner unchanged gives `p_q p_r`. On a
singlet this differs from `Tr((P_q ⊗ P_r) ρ)` by up to 0.243 (the bound is
1/4). So the distant update cannot be skipped. That same update is what
gives the Bell values of open PR 9043.

## What this means for the lanes

- **Born lane.** With open PR 9083, the quantum-probability rules of the
  campaign rest on:
  - D-loc;
  - the lock (the recorded site holds its possibility);
  - the antipodal menu.

  The trace rule, the Born orientation and the collapse at distant sites
  all follow. Open PR 9084 adds that the evolution between records is
  linear, and unitary under D-rev.
- **Record axiom.** The lock is close to the axiom's own text. What the
  campaign supplied as compression (D-perm) is its site-local part plus
  locality.

## Checks

The runner has 4 checks and all pass in under 1 s.

| Check | Result |
|---|---|
| Product projectors | The range intersection has dimension 1. The smallest eigenvalue of `E_(−q,−r)` at c = 0, 0.5, 0.9 and 1 is −1, −0.5, −0.1 and 0. |
| Compression on the partner | 200 random pairs, largest deviation 1.1e-15. |
| Reset fails | Largest `|joint − p_q p_r|` on a singlet is 0.243. |
| The whole rest | 100 random three-qubit states, largest deviation 3.3e-15. |

## What this does not do

- It adopts no decision point, and does not derive D-loc or the lock.
- It uses projective, two-outcome records on qubits. More general menus
  are not treated.
- Joint affinity rests on the steering argument of open PR 9083, applied
  to pairs. That step is argued, not separately computed.
