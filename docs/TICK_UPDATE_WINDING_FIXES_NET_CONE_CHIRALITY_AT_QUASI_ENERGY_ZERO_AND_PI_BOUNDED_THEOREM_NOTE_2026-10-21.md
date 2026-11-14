---
claim_id: tick_update_winding_fixes_net_cone_chirality_at_quasi_energy_zero_and_pi_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For supplied two-component SU(2) walks on Z^3, the sums of local degrees of the preimages of +I (quasi-energy 0) and of -I (quasi-energy pi) both equal minus the 3D winding W3; when every such preimage is nondegenerate (det M != 0) these sums are the net chiralities of the Weyl cones, and without that hypothesis they are not (a flattened walk homotopic to the m = -2 walk has Weyl-cone sums 0 and +1). Products of coins and coin-conditioned shifts have W3 = 0. The supplied quasi-local walk (n0 - i n.sigma)/|n| is defined for m not in {-3, -1, 1, 3}; at m = -2 it has W3 = -1, all eight preimages nondegenerate, a single cone at quasi-energy 0 and an exponential tail. Whether every finite-range walk has W3 = 0 is not claimed (the cited SK1 input is unchecked); no matter content, physical chirality or adopted tick update is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/tick_update_winding_fixes_net_cone_chirality_at_quasi_energy_zero_and_pi_2026_10_21.py
---

# The winding of a tick update fixes the net local degree at quasi-energy 0 and pi, and the net cone chirality when the cones are nondegenerate

Claim type: bounded_theorem.
Primary runner: `scripts/tick_update_winding_fixes_net_cone_chirality_at_quasi_energy_zero_and_pi_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight, and no law there fixes the tick update. This note asks how far a two-component tick on Z^3 can carry an unpaired Weyl cone. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the walks used.

## The degree theorem

For U(k) in SU(2), the points with U(k0) = s I (s = +1 at quasi-energy 0, s = -1 at pi) are the preimages of +I and -I of a map from the three-torus to the three-sphere. Write U(k0 + q) = s(1 - i sum M_ij q_j sigma_i + O(q^2)).

- Degree theorem (local degrees). For an isolated preimage, its local degree is the degree of q -> a(q)/|a(q)| on a small sphere, with a the vector part of s U(k0 + q). The sum of local degrees over the preimages of +I equals the degree of the map, and so does the sum over the preimages of -I. Both equal -W3.
- Weyl cones need regularity. If det M != 0 at a preimage, it is a Weyl cone of chirality sign det M, and its local degree is that sign. So when every preimage of +I and -I is nondegenerate, the net Weyl-cone chirality at 0 equals that at pi and equals -W3. The runner checks this hypothesis for every walk used here (check 4b: smallest |det M| 0.002 to 1.000).
- Negative result (second hold R1, 2026-11-14). Without regularity the net Weyl-cone chirality need not equal -W3. Witness: compose the m = -2 walk below, written (a0, a), with F(a0, a) = (a0, (1 - a0) a)/norm. The norm never vanishes (if a0 = 0 then |a| = 1), and replacing 1 - a0 by 1 - t a0 is a homotopy to the walk, so W3 = -1 is unchanged. At the only preimage of +I (k = 0), a0 = 1 - O(|q|^2), so the vector part is O(|q|^3): det M = 0 and this preimage is not a Weyl cone, though its local degree is still +1. At the seven preimages of -I the multiplier is 2, so they stay regular with net chirality +1. The Weyl-cone sums are therefore 0 at quasi-energy 0 and +1 at pi; the local-degree sums are +1 at both (runner check 4c: W3 = -1.000000, north det M 1e-31, |a|/|q| falls by 4.000 each time q halves).

A product of coins and coin-conditioned shifts is a product of one-variable loops, so its degree is 0. The runner finds W3 = -3.7e-16, -2.2e-17 and -1.8e-15 for the split-step walk S_z S_y S_x, a random-coin walk and a diagonal-shift walk, and -2.7e-17 for the eight-mode block candidate. The split-step walk has 8 cones at 0 and 8 at pi, four of each chirality in each set, all nondegenerate, and no others: off those 16 points, 1 - |cos w| is at least 5.48e-3 on a 60^3 grid. Narrowed (second hold R9): the source also stated that every finite-range walk has W3 = 0, citing the vanishing of SK1 of the Laurent ring C[Z^3]. No exact theorem statement or check record for that input is carried, so this note does not make that claim; its winding statements are for the coin and coin-conditioned-shift class above.

## A walk with one cone at quasi-energy 0

The quasi-local walk U = (n0 - i n.sigma)/|n|, with n0 = m + sum cos k_i and n_i = sin k_i, is defined exactly when n never vanishes. At a corner of the zone sin k = 0 and n0 = m + c with c in {-3, -1, 1, 3}, so the walk is undefined at m = -3, -1, 1 and 3 (check 4d) and smooth for every other m. At the masses run, m = 2, 0.5, 4.5 and -2, all preimages are nondegenerate and the net chirality is -W3 at both 0 and pi: W3 = -1, +2, 0 and -1. At m = -2 it has exactly one cone at quasi-energy 0, at k = 0 with chirality +1, and all seven doublers at pi (four of +, three of -). It is covariant under all 24 cube rotations to 6.8e-16. Its weight beyond range R falls as exp(-1.66 R) (1.4e-2 at R = 1, 3.4e-11 at R = 12), so it is not finite range. By additivity, U_split^dag U_{m=2} has W3 = -1 and equals -I somewhere, so no W3 = 0 walk lies within operator distance 2 of it. Modes 0.05 from a pi cone have relay energy within 0.06 of pi, outside the domain of the switching law (the runner's "CL-5" and "CL-6": source labels for a relay-energy rule and a switching rule as the source notes state them, not clauses of the current register).

## Scope

Supplied: the walks, the quasi-local walk, its parameter m and its exponential tail. Not claimed: that every finite-range two-component walk has W3 = 0 (the SK1(C[Z^3]) input is not checked here and no conclusion reads it; an open obligation). Notes that count Weyl cones from a winding carry the regularity hypothesis above. No matter content, physical chirality or adopted tick update is established.
