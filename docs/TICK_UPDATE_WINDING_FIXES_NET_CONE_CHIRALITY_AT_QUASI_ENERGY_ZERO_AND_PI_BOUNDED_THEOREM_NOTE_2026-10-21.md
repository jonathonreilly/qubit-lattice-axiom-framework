---
claim_id: tick_update_winding_fixes_net_cone_chirality_at_quasi_energy_zero_and_pi_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For supplied two-component SU(2) walks on Z^3, the net chirality of the Weyl cones at quasi-energy 0 equals that at quasi-energy pi and equals minus the 3D winding W3; products of coins and coin-conditioned shifts have W3 = 0, and a supplied quasi-local walk with W3 = -1 has a single cone at quasi-energy 0 and an exponential tail; no matter content, physical chirality or adopted tick update is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/tick_update_winding_fixes_net_cone_chirality_at_quasi_energy_zero_and_pi_2026_10_21.py
---

# The winding of a tick update fixes the net cone chirality at quasi-energy 0 and pi

Claim type: bounded_theorem.
Primary runner: `scripts/tick_update_winding_fixes_net_cone_chirality_at_quasi_energy_zero_and_pi_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight, and no law there fixes the tick update. This note asks how far a two-component tick on Z^3 can carry an unpaired Weyl cone. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the walks used.

## The degree theorem

A cone at k0 with U(k0) = s I (s = +1 at quasi-energy 0, s = -1 at pi) has chirality sign det M, where U(k0 + q) = s(1 - i sum M_ij q_j sigma_i + O(q^2)). For U(k) in SU(2) the cones are the preimages of +I and -I of a map from the three-torus to the three-sphere. Each preimage count, weighted by sign, is the degree, so the net chirality at 0 equals that at pi and equals -W3.

A product of coins and coin-conditioned shifts is a product of one-variable loops, so its degree is 0. The runner finds W3 = -3.7e-16, -2.2e-17 and -1.8e-15 for the split-step walk S_z S_y S_x, a random-coin walk and a diagonal-shift walk, and -2.7e-17 for the eight-mode block candidate. The split-step walk has 8 cones at 0 and 8 at pi, four of each chirality in each set, and no others: off those 16 points, 1 - |cos w| is at least 5.48e-3 on a 60^3 grid. That every finite-range walk has W3 = 0 follows from the vanishing of SK1 of the Laurent ring C[Z^3]; this input is cited, not rederived.

## A walk with one cone at quasi-energy 0

The quasi-local walk U = (n0 - i n.sigma)/|n| has net chirality -W3 at both 0 and pi for every mass parameter m, for example W3 = -1, +2, 0 and -1 at m = 2, 0.5, 4.5 and -2. At m = -2 it has exactly one cone at quasi-energy 0, at k = 0 with chirality +1, and all seven doublers at pi (four of +, three of -). It is covariant under all 24 cube rotations to 6.8e-16. Its weight beyond range R falls as exp(-1.66 R) (1.4e-2 at R = 1, 3.4e-11 at R = 12), so it is not finite range. By additivity, U_split^dag U_{m=2} has W3 = -1 and equals -I somewhere, so no W3 = 0 walk lies within operator distance 2 of it. Modes 0.05 from a pi cone have relay energy within 0.06 of pi, outside the domain of the switching law.

## Scope

Supplied: the walks, the quasi-local walk, its parameter m and its exponential tail. The vanishing of SK1 is an external input. No matter content, physical chirality or adopted tick update is established.
