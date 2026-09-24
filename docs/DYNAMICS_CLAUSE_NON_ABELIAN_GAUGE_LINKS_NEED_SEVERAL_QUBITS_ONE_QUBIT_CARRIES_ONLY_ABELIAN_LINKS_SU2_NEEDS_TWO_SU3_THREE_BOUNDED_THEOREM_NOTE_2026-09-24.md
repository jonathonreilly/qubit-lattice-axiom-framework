---
claim_id: dynamics_clause_non_abelian_gauge_links_need_several_qubits_one_qubit_carries_only_abelian_links_su2_needs_two_su3_three_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "A gauge link from vertex v to vertex w carries commuting left and right actions of the gauge group, one in each end's Gauss law; a non-Abelian field at both ends needs both actions nontrivial. (i) One qubit carries Abelian links: E = s^z generates commuting left and right U(1) actions, and s^+ is a covariant link operator (the spin-1/2 quantum link, as on the link sites of open PR 9066). One qubit carries no non-Abelian link: SU(N) for N >= 3 has no nontrivial action on C^2, and the nontrivial SU(2) action on C^2 is irreducible, with commutant the scalars. (ii) A link space with commuting nontrivial left and right SU(N) actions has dimension at least 2N. The floor is reached by (N, 1) + (1, N), which carries a nonzero covariant link operator (V^dag U V = Omega_L U Omega_R^dag), checked for N = 2, 3. For SU(3) the mixed pairings (N, 1) + (1, Nbar) carry none. (iii) So a link needs at least 1 qubit for U(1), 2 for SU(2) and 3 for SU(3). Independent SU(3) x SU(2) x U(1) link fields need dimension at least 48, so at least 6 qubits. In the doubled-coordinate role pattern, where a link site holds one qubit, non-Abelian links are therefore composite. These are minimal truncated quantum links; no continuum limit, phase or selection of the gauge group is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_non_abelian_links_need_several_qubits_2026_09_24.py
---

# Non-Abelian gauge links need several qubits

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** representation-theoretic floor with finite certificates; unaudited.

## Result

The campaign's gauge fields sit on single-qubit sites:
- the Kitaev Z2 field of open PRs 9048 and 9054;
- the U(1) field on link sites of open PRs 9066, 9069 and 9072.

The Standard Model also needs SU(2) and SU(3). This note finds the floor
that the Qubit axiom sets for them:
- **One qubit carries U(1) and Z2 links, but no non-Abelian link.**
- **An SU(N) link needs at least 2N states.** The floor is reached, with a
  covariant link operator, by the space `(N, 1) ⊕ (1, N)`: one copy of the
  fundamental at each end.
- **Qubits per link.**
  - U(1): 1.
  - SU(2): 2.
  - SU(3): 3.
  - Independent SU(3) × SU(2) × U(1) fields: at least 6.

So in the doubled-coordinate role pattern, where a link site holds one
qubit, the non-Abelian parts of a Standard Model gauge field must live on
composite links of several sites.

## Setting

- **Gauss laws at both ends.** A link from `v` to `w` carries a left action
  of the gauge group, in the Gauss law at `v`, and a right action, in the
  Gauss law at `w`.
  - The two actions commute.
  - A non-Abelian field that is charged at both ends needs both actions
    nontrivial.
- **Link operators.** A link operator is a matrix `U^{ab}` of operators with
  `V† U V = Ω_L U Ω_R†`, the consistent (Heisenberg-picture) law.
- **The Qubit axiom.** One qubit per site. A link may occupy one site (the
  link site of open PR 9066) or several.

## Theorem 1 — one qubit carries only Abelian links

- **U(1).** `E = s^z` generates commuting actions `e^{iaE}` and `e^{−ibE}`,
  and `s^+` is covariant with charge 1. This is the spin-1/2 quantum link
  used on link sites in open PR 9066. Z2 is similar.
- **SU(N), N ≥ 3.** A nontrivial action on `C²` would be a nonzero Lie
  algebra map from `su(N)` to `u(2)`. `su(N)` is simple, of dimension
  `N² − 1 > 4`, so every such map is zero.
- **SU(2).** A nontrivial action on `C²` is the fundamental, which is
  irreducible. Its commutant is the scalars, so a commuting right action is
  trivial. ∎

## Theorem 2 — the floor is 2N, and it is dynamical

**Floor.** Decompose the link space into irreducibles `(ρ, σ)` of the left
and right groups. Every nontrivial SU(N) irreducible has dimension at least
`N`.
- If one component has both `ρ` and `σ` nontrivial, it has dimension at
  least `N² ≥ 2N`.
- Otherwise a component with `ρ` nontrivial and a different one with `σ`
  nontrivial have dimensions at least `N` each.

Either way the dimension is at least `2N`. ∎

**Reached, with dynamics.** On `(N, 1) ⊕ (1, N)`, dimension `2N`, the left
and right actions commute and are nontrivial. The covariant link operators
form a nonzero space: dimension 2 for SU(2) and 1 for SU(3). They are found
by linear algebra for random group elements. For SU(3) the mixed pairing
`(N, 1) ⊕ (1, N̄)` has none.

## Corollary — qubits per link

| Gauge factor | Minimal link dimension | Qubits |
|---|---|---|
| U(1) | 2 | 1 |
| SU(2) | 4 | 2 |
| SU(3) | 6 | 3 |
| SU(3) × SU(2) × U(1), independent fields | 6 · 4 · 2 = 48 | 6 |

## What this means for the lanes

- **Gauge lane.** The campaign's exact gauge fields fit on one qubit per
  link. The Kitaev Z2 bond variables and the U(1) ring's link sites are
  Abelian.
- **Standard Model gauge group.** SU(2) and SU(3) need links of at least 2
  and 3 qubits. With one qubit per site, those links span several sites,
  which means a coarser link structure: a superlattice whose links contain
  at least 6 qubits for the full group.
- **What stays open.** Which superlattice, if any, gives the group. The
  count shows only that one-qubit links cannot.

## Checks

The runner has 5 checks and all pass in under 1 s.

| Check | Result |
|---|---|
| U(1) on a qubit | Left and right actions commute; `s^+` covariant, with defect 1e-16. |
| SU(2) on a qubit | Commutant dimension 1 (scalars). |
| Floor reached | `(N, 1) ⊕ (1, N)`: dimensions 4 (SU(2)) and 6 (SU(3)), commuting nontrivial actions. |
| Dynamical | Covariant link operators: solution spaces of dimension 2 (SU(2)) and 1 (SU(3)). |
| Qubit counts | U(1) 1, SU(2) 2, SU(3) 3; product dimension 48, so 6 qubits. |

## What this does not do

- It adopts no gauge group or superlattice, and does not derive the
  Standard Model group.
- Its links are minimal truncated quantum links. No continuum limit,
  confinement or phase is claimed.
- It gives no dynamics for composite links.
