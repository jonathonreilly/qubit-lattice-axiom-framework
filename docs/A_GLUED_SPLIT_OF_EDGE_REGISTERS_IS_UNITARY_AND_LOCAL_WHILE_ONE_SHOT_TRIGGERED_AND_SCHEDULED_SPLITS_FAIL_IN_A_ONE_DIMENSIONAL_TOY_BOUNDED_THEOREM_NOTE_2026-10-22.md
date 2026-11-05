---
claim_id: a_glued_split_of_edge_registers_is_unitary_and_local_while_one_shot_triggered_and_scheduled_splits_fail_in_a_one_dimensional_toy_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the update law's split when edges are quantum registers (length L(1 + n/2S)), in a supplied one-dimensional toy (one chain cell = one edge register plus two fermion modes; its split = two child edges at n = 0 plus four modes, the two new ones in the children's vacuum): the passing of the cell's matter onto the children is an isometry that keeps the charge N - modes/2; a one-shot split controlled by the full edge, acting on the sum over refinement patterns, is not an isometry (two orthogonal states collide); the exchange form V + V^dag is unitary but, with slow edges, sends the odds between parent and children every other half-tick; the glued form, in which the raise that would fill the last quantum passes onto the children's split image and its lowering passes back, is hermitian, so the tick is unitary, keeps the charge, moves the children's weight smoothly, and leaves the cell's distribution over configurations and sectors independent of a remote setting; for any unitary the weight split across a generation cut equals the weight merged back. On an edge-length ladder the glued junction transmits an up-moving packet that a box would reflect, and the actuality law's transport stays Born-distributed across it. A split triggered by the actual configuration breaks the Born law for the split event and lets a remote setting change its frequency (a toy with a remote qubit); a split at a fixed tick catches only part of the odds. Supplied model, finite diagnostic: no response-law edge dynamics, collective children, supplied hops, costs and packets; the estimates against the expansion history use supplied measured inputs."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/a_glued_split_of_edge_registers_is_unitary_and_local_while_one_shot_triggered_and_scheduled_splits_fail_in_a_one_dimensional_toy_2026_10_22.py
---

# A glued split of edge registers is unitary and local, while one-shot, triggered and scheduled splits fail, in a one-dimensional toy

Claim type: bounded_theorem.
Primary runner: `scripts/a_glued_split_of_edge_registers_is_unitary_and_local_while_one_shot_triggered_and_scheduled_splits_fail_in_a_one_dimensional_toy_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its update law (CL-1 in the three-law numbering) splits a cube into eight children when its edges reach twice the rung length, and with edge registers the edge length is an operator, L(1 + n/2S) with n = 0..2S. The split trigger then acts on odds, not on a definite length, and the register must say how. This note compares four forms in a one-dimensional toy: (a) a glued split, in which the parent's full state is the children's split image; (b) a split triggered by the actual configuration of the actuality law (CL-2); (c) a split at a fixed tick; and the one-shot controlled and exchange forms of (a). The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. Structure (one cell: parent = edge register plus modes a, b with one fermion; children = two edge registers plus modes a, 1, 2, b with two fermions).

1. The passing of the matter onto the children (parent vacuum to the children's vacuum, the excitation to the lowest excitation) is an isometry from 2 to 6 states that keeps the charge Q = N - modes/2: the new modes are half filled.
2. A one-shot split controlled by the full edge, acting on the sum over refinement patterns (split the full component, identity elsewhere), is not an isometry: its image lands on child states the map also keeps, so two orthogonal states become one.
3. The exchange V + V^dag on (full component, split image) is unitary and an involution; it carries a merge V^dag. With slow edges it sends the odds parent to children and back on alternate ticks, so the actuality law's actual configuration would gain and lose the new sites each time.
4. The glued form: on the parent window n = 0..2S-1, the edge raise that would fill the last quantum passes onto the children's split image (V), and the lowering of the image passes back (V^dag). The generator is hermitian, so the tick is unitary on the sum over refinement patterns; it keeps Q, and with slow edges the children's weight grows smoothly.
5. With the glued split, the cell's distribution over configurations, including the sector label (the number of sites and so of records), is independent of a setting on a remote qubit entangled with it.
6. For any unitary on the sum over refinement patterns from a finite start, the trace weight split across a generation cut equals the weight merged back. Only a non-onto isometry, a history label, splits without merging.

B. The top wall (edge-length ladder only, hops proportional to length; parent levels 0..11, child levels from 0).

7. Without the split, an up-moving packet reflects at the top of the parent window, as in a box. Glued, it passes into the children; the residual is set by the junction's impedance step and falls as the packet widens.
8. Across the glued junction, the actuality law's transport (fewest changes, then greatest entropy) keeps the actual configuration Born-distributed over the sectors. It splits with the forward flux and merges back only with the reflected flux, so the net flux equals the children's weight.
9. (c) A split at a fixed tick finds only the full component. The rest of the odds would need children below the rung length, which have no state, and that rest grows with the packet's width.

C. The actual-configuration trigger (b) against the glued split (a); a small ladder with children, times a remote qubit.

10. (b) With the update chosen by the actual configuration, the odds branch by junction history, and the frequency of the actual split differs from the odds weight of the split averaged over the branches: the Born law fails for the split event.
11. (b) That frequency, the tick at which the records double, depends on a setting at a remote qubit that never interacts with the edge: it signals in this toy.
12. (a) With the glued split, the frequency of the split is its Born weight, independent of the setting.

## Derivation

Item 1. The parent's one-fermion sector on modes (a, b) has 2 states; the children's two-fermion sector on (a, 1, 2, b) has 6. V maps the parent's ground and excited states to the children's ground and first excited states of the hopping chain; its columns are orthonormal eigenvectors, so V^T V = 1. Q = N - modes/2 is 1 - 1 = 0 in the parent and 2 - 2 = 0 in the children.

Item 2. S = V P_full + (1 - P_full) keeps every child state, including the image of V, as itself, and also sends the full component onto that image; two orthogonal inputs then share an output, so S^T S != 1.

Item 3. With Q_im = V V^T, G = V + V^T + (1 - P_full - Q_im) swaps the full component with its image and acts as identity elsewhere, so G^2 = 1 and G is unitary.

Item 4. The glued generator adds J_top (V + V^dag) between the parent's top window state and the children's image to the in-sector hops. It is hermitian, so exp(-iH) is unitary; every term keeps N - modes/2.

Item 5. The glued tick acts on the cell alone; a rotation on the remote qubit commutes with it, so the cell's reduced distribution, sector label included, does not depend on the rotation.

Item 6. For a unitary U and projectors P (parent) and C (children) with P + C = 1, ||C U P||^2 = tr(P) - ||P U P||^2 and ||P U C||^2 = tr(P) - ||P U P||^2 also, since U^dag U = U U^dag = 1 on the finite space; the two fluxes are equal. A one-way isometry is not onto and escapes this.

Items 10 and 11. Under (b), whether the junction acts in a tick depends on whether the actual configuration is at the parent top. The odds then follow a different unitary on each branch, and the actual configuration's split frequency is a weighted sum over branches that need not equal the Born weight. A local rotation on the remote qubit changes the odds on each branch and so the branch weights.

## Checks

The runner ends with `TOTAL: PASS=16 FAIL=0` in about 30 s.

Exact checks and identities (checked numerically):
- Passing: |V^T V - 1| = 7e-16; Q = 0 in parent and children; vacuum energies -1.000 and -2.236.
- One-shot controlled split: |S^T S - 1| = 1.000. The collision rank 2 is stated in the runner, not computed.
- Exchange form: |G^T G - 1| = 1e-15, and G^2 = 1 (asserted below 1e-13).
- Glued form (2S = 2, edge hop 0.02): |U^dag U - 1| = 3e-15; [H, Q] = 0 (asserted below 1e-13).
- No signalling with the glued split, five remote settings between 0 and pi, seeded random entangled start: maximum difference 2e-17.
- Generation-cut flux: up 0.000390 = down 0.000390; the history-labelled isometry gives up 2, down 0.
- Glued split frequency against the remote setting (three random starts, settings 0 and pi/4): maximum difference 3e-16; glued P(split) 0.6237 for the first start.

Finite diagnostics (supplied model, finite diagnostic, no physical identification):
- Exchange form with slow edges: P(children) per tick 1.00, 0.00, 1.00, 0.00, 1.00, 0.00, 1.00, 0.00.
- Glued form with slow edges: P(children) 0.0002, 0.0007, 0.0015, 0.0023, 0.0031 over the first five ticks.
- Top wall: in the box the mean level peaks at 9.89 and then falls to 4.50; glued transmission 0.937 (width 1.2) and 0.982 (width 2.5), against 1.000 on a uniform chain with no impedance step; two independent child edges 0.948.
- Transport across the junction (entropic limit with tau = 0.1, cost = level difference): Born error 1e-13; actual flux up 0.9819, down 0.0002, children's weight 0.9818.
- Fixed schedule: the best fixed tick carries 0.751 (width 1.2) and 0.553 (width 2.5) of the odds.
- Actual-configuration trigger (12 ticks, three random starts): maximum |P(actual split) - E[odds split]| = 0.288 (for example 0.3603 against 0.0723); at most 254 branches; weight kept 1.0000. Remote setting 0 against pi/4: maximum |dP(split)| = 0.0483 (for example 0.3603 against 0.3135).

## Estimates against measurement

Estimates with supplied inputs (t_P, H0, the age 4.35e17 s, a factor 4e9 in scale factor since nucleosynthesis, and a rung L = sqrt(8 pi) l_P):
- Exchange form today: a register gains about 2S H0 t_tick quanta per tick, so a full cube would flicker parent to children about 1/(2S H0 t_P) times per split; H0 t_P = 1.2e-61, about 9e+60/2S flickers per cube per split. The glued form does not flicker.
- (c) A fixed schedule against the measured expansion history: the window needs |ln a(t) - (ln 2) t/(K t_tick)| < ln 2 at all times. A schedule matching the 32 doublings since nucleosynthesis gives about 1e-14 splits between 1 s and 180 s, against 3.7 needed (half of log2(180), for radiation-era growth of the scale factor by about 13; the growth factor is stated, not computed).
- (a) The glued split fires once per doubling of each cube's own edge, so the split cascade has period ln 2 in ln a in every era; (c) gives period H K t_tick, equal to ln 2 only in a tuned de Sitter phase. This line is a structural reading; the runner records it with no computation.

## Boundary

Supplied: the one-dimensional chain cell; the spin-S edge hop and the length-proportional ladder hops (no response-law edge dynamics); collective children; the junction hop as a geometric mean; the cross-sector unit cost and the entropic transport at tau = 0.1; packet shapes and widths; the remote-qubit toy and its settings; the measured inputs of the estimates. Forced, given those: the isometry and charge of the passing; the failure of the one-shot controlled split to be an isometry; unitarity of the exchange and glued forms; the flicker of the exchange form with slow edges; locality of the glued split; equality of split and merge flux for any unitary; Born failure and remote-setting dependence of the actual-configuration trigger in the toy. Not claimed: any three-dimensional split with eight children; edge dynamics from the response law; that the toy's transmission values or branch counts hold beyond the toy; that the glued form is the register's unique consistent split; that the estimates are predictions beyond their supplied inputs.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the split, the split window and the edge registers of the update law, and the Born-preserving transport and records of the actuality law. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/a_glued_split_of_edge_registers_is_unitary_and_local_while_one_shot_triggered_and_scheduled_splits_fail_in_a_one_dimensional_toy_2026_10_22.py
```

Needs numpy and scipy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120` (with an internal timer at 118 s), runs in about 30 s with about 70 MB resident, prints about 4.7 kB and ends with `TOTAL: PASS=16 FAIL=0`. Its random starts are seeded; two repeated runs gave identical output apart from the elapsed-time line.
