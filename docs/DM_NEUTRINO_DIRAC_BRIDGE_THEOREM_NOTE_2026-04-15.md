# DM Neutrino Dirac Bridge Algebra Note

**Date:** 2026-04-15
**Type:** positive_theorem
**Claim scope:** a conditional finite-matrix theorem for the displayed
Hermitian Euclidean `Cl(4)` generators on `C^16`, real coefficients
`phi_1, phi_2, phi_3`, and explicitly defined bit-basis projectors.
**Status authority:** independent audit lane only. This source does not set or
predict an audit outcome.
**Primary runner:**
[`scripts/frontier_dm_neutrino_dirac_bridge_theorem.py`](./../scripts/frontier_dm_neutrino_dirac_bridge_theorem.py)

---

## Result

Let `G_0, G_1, G_2, G_3` be the displayed Hermitian generators satisfying

`{G_mu, G_nu} = 2 delta_munu I_16`.

Define

- `gamma_5 = G_0 G_1 G_2 G_3`;
- `Xi_5 = G_1 G_2 G_3 G_0`;
- `P_L = (I_16 + gamma_5)/2` and
  `P_R = (I_16 - gamma_5)/2`; and
- for real `phi_i`,
  `M(phi) = phi_1 G_1 + phi_2 G_2 + phi_3 G_3`.

Then the following finite-matrix statements hold exactly:

1. `M(phi)` is Hermitian.
2. `M(phi)^2 = (phi_1^2 + phi_2^2 + phi_3^2) I_16`.
3. `{M(phi), gamma_5} = 0`.
4. `P_L M(phi) P_L = P_R M(phi) P_R = 0`.
5. `M(e_i) = G_i` for `i = 1,2,3`.
6. `Xi_5 = -gamma_5`, so
   `P_L Xi_5 P_R = P_R Xi_5 P_L = 0`.

These are algebraic grading statements. They do **not** identify either
matrix as a physical Dirac or Yukawa carrier.

## Exact proof certificate

The primary runner constructs the displayed `16 x 16` matrices over the
exact SymPy domain. It checks all sixteen ordered Clifford
anticommutators, generator Hermiticity and involution, and the identities
above as polynomial identities in symbols declared real.

The real-coefficient hypothesis is load-bearing. It is not inferred:
`i G_1` is an explicit wrong-object rejector because it is anti-Hermitian.
The runner also rejects a doubled norm, replacing `G_3` by `Xi_5`, and
dropping the `phi_3 G_3` term.

Moving `G_0` left across three anticommuting generators gives

`Xi_5 = G_1 G_2 G_3 G_0 = -G_0 G_1 G_2 G_3 = -gamma_5`.

The runner verifies this entry by entry and checks all 24 orderings of the
four generators: twelve equal `+gamma_5` and twelve equal `-gamma_5`.
It also replays the Clifford, grading, and reordering identities in a
separate standard `4 x 4` Euclidean realization. That replay is
representation-robustness support; it does not add physical semantics.

For the displayed `C^16` representation, the squared Frobenius weights of
the `LL/LR/RL/RR` blocks are

- `Xi_5`: `8/0/0/8`;
- `G_1`: `0/8/8/0`.

Thus the one-direction norm `||P_R G_1 P_L||_F` is
`sqrt(8) = 2 sqrt(2)`, while the norm of the full off-diagonal sum
`P_L G_1 P_R + P_R G_1 P_L` is `4`.

The direct statement about bare `Xi_5` must not be generalized to
composites. In particular,

`i G_1 Xi_5`

is Hermitian, anticommutes with `gamma_5`, and squares to `I_16`. The
runner carries this explicit counterexample so that the bare grading
identity cannot be read as a no-go for dressed or composite carriers.

## Finite bit-basis return lemma

Label the spatial bit basis by

- `O_0 = {(0,0,0)}`;
- `T_1 = {(1,0,0),(0,1,0),(0,0,1)}`;
- `T_2 = {(1,1,0),(1,0,1),(0,1,1)}`; and
- `O_3 = {(1,1,1)}`.

With the corresponding exact projectors, including both values of the
fourth bit, the displayed matrix `G_1` obeys

`P_T1 G_1 P_T1 = 0`

and

`P_T1 G_1 (P_O0 + P_T2) G_1 P_T1 = P_T1`.

Adding `P_O3` to the intermediate projector does not change the restricted
return. These are exact statements about the six-dimensional `T_1`
bit-basis block. Calling `T_1` a physical generation triplet, or promoting
this return to an effective Yukawa interaction, requires a separate bridge
and is not claimed here.

## Selector boundary

No selector theorem is claimed. For

`V_sel(phi) = 32 sum_{i<j} phi_i^2 phi_j^2`,

the global minimum over `R^3` is zero on the full union of the three
coordinate axes, including the origin and arbitrary magnitudes and signs.
On the separately supplied nonnegative normalized simplex
`phi_i >= 0`, `sum_i phi_i = 1`, the only zeros are `e_1,e_2,e_3`, because
every summand is nonnegative and two nonzero coordinates would make at least
one summand positive. Neither the selector form, that simplex domain, nor a
physical axis choice is derived here. The runner therefore does not use a
selector to infer operator selection.

## Claim and import boundary

The exact certificate is conditional on definitions and domains, not on
measured or fitted input:

- **Defined algebraic data:** the displayed `C^16` generators, `gamma_5`,
  `Xi_5`, the projectors, and the family `M(phi)`.
- **Explicit domain condition:** `phi_1, phi_2, phi_3` are real.
- **Exact internal consequences:** the Clifford, square, grading, block,
  ordering, norm, and finite bit-basis return identities.
- **Support only:** the independent `4 x 4` realization replay.
- **Not supplied by the registered primitives and still open:** a physical
  realization of the `C^16` family, identification of the constructed
  grading with emergent `3+1` chirality, an action or Hamiltonian convention
  connecting matrix blocks to a Yukawa bilinear, a forced selector and its
  domain, a physical weak-axis choice, a generation interpretation of
  `T_1`, and any normalization or suppression law.

The registered `minimal_axioms`, `scale_reference_primitive`,
`kinetic_isotropy_primitive`, and `realized_state_primitive` are not treated
as walls or bounded imports; none supplies the open physical bridges just
listed. No new axiom or primitive is proposed.

## Proof-obligation disposition

The finite-matrix theorem is closed under its displayed definitions and real
coefficient domain. The physical operator-selection graph remains open at
the carrier, chirality-realization, action/bilinear, selector, branch, and
normalization leaves. Those leaves are not renamed as conventions or
discharged by the matrix calculation.

This note does not ship a negative route-exhaustion claim. In particular, it
does not claim that `Xi_5` cannot participate in a physical carrier, that all
dressings are ruled out, or that physical operator selection is closed.
Accordingly, an `N1`-through-`N8` no-go packet is not asserted; the exact
composite counterexample above records why such a packet would be premature.
