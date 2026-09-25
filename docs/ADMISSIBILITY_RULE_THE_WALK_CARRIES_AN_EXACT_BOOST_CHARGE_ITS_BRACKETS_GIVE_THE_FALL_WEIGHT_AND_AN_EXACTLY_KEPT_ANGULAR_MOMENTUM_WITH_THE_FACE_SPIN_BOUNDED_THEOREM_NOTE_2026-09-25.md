---
claim_id: admissibility_rule_the_walk_carries_an_exact_boost_charge_its_brackets_give_the_fall_weight_and_an_exactly_kept_angular_momentum_with_the_face_spin_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "WITHIN block 54's walk H = sum_a sigma_a S_a (with or without block 77's staggered rest energy m eps), block 73's two-step momentum P_j = S_j C_j, as landed on main and supplied, with block 106 (landed) and blocks 136, 138 and 139 (open) placed. Exact operator identities: (T1) the energy dipole D_i = (X_i H + H X_i)/2, the first moment of the averaged energy, obeys i[H, D_i] = P_i, so the boost charge K_i = D_i - t P_i is kept for every state. (T2) i[D_i, P_j] = - delta_ij cos(2k_j) H (C2_j H on the lattice): the boost-momentum bracket carries block 106's fall weight. (T3) i[D_i, D_j] = eps_ijl J_l with J_l = (X x P)_l + (1/2) C_i C_j sigma_l, the orbital angular momentum of the two-step momentum plus the coin's spin carried on the faces (block 138), and [H, J_l] = 0 exactly; J is the same with the staggered mass. (T4) [J_l, P_m] = i eps_lmn cos(2k_m) P_n; every factor tends to 1 at long wavelength, where the brackets are the comparator's kinematic ones with J = L + sigma/2; at each species corner the spin weight tends to that species' own sign. The J-J bracket is not claimed exact. The supervisor's own derivation (Claude Opus 5.5), checked by its runner; not refereed by another model family. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_the_walk_carries_an_exact_boost_charge_its_brackets_give_the_fall_weight_and_an_exactly_kept_angular_momentum_with_the_face_spin_2026_09_25.py
---

# The walk carries an exact boost charge: its brackets give the fall weight and an exactly kept angular momentum with the face spin

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** bounded-support (exact within the landed walk, momentum and rest energy, with blocks 106, 136, 138 and 139 placed; the supervisor's own derivation, not refereed by another model family; nothing adopted or registered; unaudited)

This note works within blocks 54, 73, 77 and 106 as landed on main (the walk, the two-step momentum, the staggered rest energy and the fall weight), with blocks 136, 138 and 139 placed; it reports the brackets of the walk's energy dipole with the energy, the momentum and itself; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Blocks 136 and 139 (open) found the books: the averaged energy of the walk, with or without its rest energy, flows exactly as the two-step momentum. Summed over the lattice, that is a statement about the energy's centroid. This note takes the centroid, the energy dipole `D`, and computes its brackets.

- **T1: the centroid moves with the momentum.** `i[H, D_i] = P_i` exactly. So the boost charge `K_i = D_i − tP_i` is kept for every state, massless or massive.
- **T2: boost against momentum carries the fall weight.** `i[D_i, P_j] = −δ_ij cos(2k_j) H`. The factor `cos 2k` is block 106's fall weight of the two-step momentum. The books are exact at first order in the member's fields, and the fall is exact only at leading order; this bracket is where the two meet.
- **T3: boost against boost is a kept angular momentum.** `i[D_i, D_j] = ε_ijl J_l`, where `J` is the orbital angular momentum of the two-step momentum plus the coin's spin carried on the faces: block 138's face spin, summed. `J` commutes with `H` exactly, and it is the same with the rest energy.
- **T4: the rest, and the long-wave limit.**
  - The angular momentum turns the momentum with the same factor: `[J_l, P_m] = iε_lmn cos(2k_m)P_n`.
  - Every factor tends to 1 at long wavelength, where the brackets become the comparator's kinematic ones, with `J = L + σ/2`.
  - At each species corner the spin weight tends to that species' own sign.

In plain terms, the lattice has no smooth rotations and no smooth changes of velocity, yet the walker carries exact counterparts of both. The centre of its energy moves exactly with its momentum. Two such "velocity charges" combine into an exactly conserved spin-and-orbit angular momentum, whose spin part is the coin's spin spread over the faces. The only departure from the smooth-space rules is a factor `cos 2k`, the same factor that makes the walker fall with slightly less than full weight at the lattice scale.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-25.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom." The memo does not "define a time metric". The walk, its rest energy and its momenta are supplied. Nothing is adopted.
- **The walk** (blocks 54 and 77 as landed). `H = Σ_aσ_aS_a`, or `H + mε`, with `S_a = (T_a − T_a⁻¹)/(2i)` and `C_a = (T_a + T_a⁻¹)/2`.
- **The two-step momentum** (block 73 as landed). `P_j = S_jC_j`, with symbol `½ sin 2k_j`, and `C2_j = (T_j² + T_j⁻²)/2`, with symbol `cos 2k_j`.
- **Position and dipole.**
  - `X_i` is the position.
  - `D_i = ½(X_iH + HX_i)`, so `⟨t|D_i|s⟩ = ½(x_t + x_s)_i⟨t|H|s⟩`. It is `Σ_x x_i e′(x)`, since the body-diagonal average keeps first moments (block 137 T3).
- **Angular momentum.** `J_l = (X × P)_l + ½C_iC_jσ_l`, where `{i, j}` are the two directions other than `l`. Its second term is the coin's spin `σ/2` carried on the faces perpendicular to `l`; summed over the lattice, that is block 138's face spin.
- **Comparators, named only:**
  - the kinematic algebra of the comparator (Poincaré), generated by energy, momenta, boosts and rotations;
  - the centre-of-energy theorem;
  - the fall weight of block 106.

## Theorem T1 — the centroid moves with the momentum

*Statement.* `i[H, D_i] = P_i`. So `K_i = D_i − tP_i` is kept, `dK_i/dt = 0`, for every state, with or without the staggered mass.

*Proof.*
- `i[H, X_i]` is the velocity `σ_iC_i`, and `D_i = ½(X_iH + HX_i)`. So `i[H, D_i] = ½{σ_iC_i, H} = C_iS_i`, using `{σ_i, σ_a} = 2δ_ia`.
- With `mε`, the mass term anticommutes with the velocity, so it drops out of the anticommutator.
- Equivalently, sum block 136 T1 and block 139 T1 against `x_i`.

∎

*Checked (B1).*
- Symbolically, on spinor functions of `k`.
- As exact vectors over `ℚ(i)` on the open lattice, for four states, massless and with `m = 3/4`.

## Theorem T2 — the boost–momentum bracket carries the fall weight

*Statement.* `i[D_i, P_j] = −δ_ij cos(2k_j)H`, which is `−δ_ijC2_jH` on the lattice, and likewise with `H + mε`. At each species corner, `cos 2(πn + κ) = cos 2κ`.

*Proof.* `i[X_i, P_j] = −∂_iP_j = −δ_ij cos 2k_j`, and `P_j` commutes with `H`. ∎

*Checked (C1).* Symbolically, and as exact vectors, massless and massive.

## Theorem T3 — the boost–boost bracket is a kept angular momentum

*Statement.* `i[D_i, D_j] = ε_ijlJ_l` and `[H, J_l] = 0`, exactly. `J` does not depend on the staggered mass.

*Proof.*
- `J_l` is kept because it is the bracket of two kept charges: `i[K_i, K_j] = i[D_i, D_j]`, since `[D_i, P_j] = 0` for `i ≠ j` and the `P`s commute.
- Its form follows from the two-by-two algebra of the coin matrices and `i[X_i, P_j] = −δ_ij cos 2k_j`.

∎

*Checked (D1).* Symbolically, and as exact vectors, massless and massive.

## Theorem T4 — the rest of the algebra, and the long-wave limit

*Statement.*
- `[J_l, P_m] = iε_lmn cos(2k_m)P_n`.
- Every factor tends to 1 at long wavelength, where `P → k`, `cos 2k → 1` and `C_iC_j → 1`, and the brackets become the comparator's kinematic ones, with `J = L + σ/2`.
- At the species corner `πn` the spin weight `cos k_i cos k_j` tends to `(−1)^{n_i+n_j}`, the spin of that species' reflected frame.
- The bracket of two components of `J` closes only up to lattice corrections, and is not claimed exact.

*Proof.* The first item: `i[X_i, P_m] = −δ_im cos 2k_m`, and the spin part commutes with `P`. The rest is series. ∎

*Checked (E1).* The bracket symbolically; the series; the eight corners.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "blocks 106 (landed), 136, 138, 139 (open): the fall weight cos 2k, the exact books and the face spin stated separately"
source_of_blocker_text: blocks 106 (landed), 136, 138 and 139 (open)
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the J-J bracket's lattice correction; the boost charge under exclusion (block 137); an other-family referee"
conditional_surface_status: "exact operator identities for one walker, massless or with the staggered mass; many free walkers by second quantisation of bilinears"
hypothetical_axiom_status: "nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 54: the walk.
  - Block 73: the two-step momentum.
  - Block 77: the staggered rest energy.
  - Block 106: the fall weight `cos 2k` of the two-step momentum.
- **Opened, not landed.**
  - Blocks 136 (PR #9196) and 139 (PR #9201): the books.
  - Block 138 (PR #9200): the face spin.
  - Block 137 (PR #9197): the first moment.
- **In the literature.**
  - The kinematic algebra of the comparator (Poincaré).
  - The centre-of-energy theorem.

  Both reference only.
- **New here:**
  - T1: the exact lattice boost charge;
  - T2: the fall weight as the boost–momentum bracket;
  - T3: the exactly kept angular momentum, with the face spin;
  - T4: the rotation of the momentum, and the long-wave limit.
- **Provenance.** This is the supervisor's own derivation, in the same model family as the probes workers. No other model family has refereed it.

## Exact target and obligation graph

Target: the brackets of the energy dipole. The obligations are:
- (O1) with the energy (T1);
- (O2) with the momentum (T2);
- (O3) with itself (T3);
- (O4) the remaining bracket and the limit (T4).

T1–T4 discharge them, except the `J–J` bracket, which is left open.

## No-Go Discipline Gate

The note's negative sentence: the boost–momentum bracket is not the comparator's; it carries `cos 2k`.

### N1 — Routes by which the sentence could fail or mislead
1. *Another momentum.* The one-step momentum gives `cos k` and fails T1 (a mutation). Block 73 makes the two-step momentum the only covariant conserved one of reach two.
2. *Another dipole.* Any placement with the same first moment gives the same `D`.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond the supplied walk, rest energy and momenta.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| blocks 54, 73, 77 (landed) | the walk; the momentum; the rest energy | yes (restated) |
| block 106 (landed) | the fall weight | no (comparison) |
| blocks 136–139 (open) | the books; the face spin; the first moment | no (placement) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the boost charge is kept; its brackets give `cos 2k` and a kept angular momentum with the face spin" | executed: exact vectors over `ℚ(i)`, massless and massive | executed: four states per mass | executed: all brackets symbolically | executed: series and species | operator identities; the `J–J` bracket not claimed |

### N6 — Partial-closure paths and primitive scan
`kinetic_isotropy_primitive` is not used. Nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "A kept `J` on a cubic lattice contradicts the absence of rotations."
  - *Reply:* `J` is not the generator of rotations of the lattice. Its orbital part uses the two-step momentum, and its bracket with itself is not exactly that of rotations (T4).
  - It is the bracket of two kept boost charges, and is therefore kept.

### N8 — Cross-cycle echo
- Block 106 found the fall weight `cos 2k`.
- Blocks 136 and 139 found the books.
- Block 138 found the face spin.
- This note shows that all three are brackets of one object, the walk's energy dipole.

## Falsifiers

- A state for which T1, T2 or T3 fails.
- A component of `J` that does not commute with `H`.

## Boundaries and non-claims

- The walk, its rest energy and its momenta are supplied.
- The `J–J` bracket is not claimed exact.
- The result is for one walker; many free walkers follow by the second quantisation of bilinears. Excluded records (block 137) are not covered.
- Not refereed by another model family.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 54, 73, 77 and 106, restated. Blocks 136–139, placed.
- Named standard imports, at definition level:
  - Fourier analysis on the lattice;
  - the algebra of the coin matrices;
  - exact arithmetic over `ℚ(i)`;
  - series expansion.

## Review record

- **Who and when.** Supervisor-run block, the eighty-eighth since the source-link direction opened; 2026-09-25.
- **Provenance.** The supervisor's own derivation (Claude Opus 5.5), checked by its own runner. It is not refereed by another model family.
- **Before writing.** The own prior-art check (memory, open PRs, probes attempts, main) found no boost charge or angular momentum of the walk.
- **Independence.** Every bracket is checked symbolically and, for T1–T3, again as exact vectors on the open lattice. Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_walk_carries_an_exact_boost_charge_its_brackets_give_the_fall_weight_and_an_exactly_kept_angular_momentum_with_the_face_spin_2026_09_25.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
