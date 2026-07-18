# Finite-Dimensional Chiral Vector Representation Theorem

**Date:** 2026-04-15

**Revised:** 2026-07-18

**Type:** positive_theorem

**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.

**Claim scope:** exact identities for the explicit Pauli/Kronecker matrix
packets on `C^8` and `C^16` displayed below.

**Primary runner:** [`scripts/frontier_dm_neutrino_weak_vector_theorem.py`](../scripts/frontier_dm_neutrino_weak_vector_theorem.py)

**Primary runner cache:** [`logs/runner-cache/frontier_dm_neutrino_weak_vector_theorem.txt`](../logs/runner-cache/frontier_dm_neutrino_weak_vector_theorem.txt)

## Statement

Let

- `sigma_x = [[0,1],[1,0]]`,
- `sigma_y = [[0,-i],[i,0]]`,
- `sigma_z = [[1,0],[0,-1]]`.

The spatial Clifford triple on `C^8` is

- `Gamma_1^(8) = sigma_x x I x I`,
- `Gamma_2^(8) = sigma_y x sigma_x x I`,
- `Gamma_3^(8) = sigma_y x sigma_y x sigma_x`.

The four-generator packet on `C^16` is

- `Gamma_0 = sigma_z x sigma_z x sigma_z x sigma_x`,
- `Gamma_1 = sigma_x x I x I x I`,
- `Gamma_2 = sigma_z x sigma_x x I x I`,
- `Gamma_3 = sigma_z x sigma_z x sigma_x x I`.

For either spatial triple, define

`B_a = -(i/4) sum_(m,n=1)^3 eps_(amn) Gamma_m Gamma_n`.

On `C^16`, also define

`gamma_5 = Gamma_0 Gamma_1 Gamma_2 Gamma_3`,

`P_L = (I + gamma_5)/2`, `P_R = (I - gamma_5)/2`,

and

`Y_i = P_R Gamma_i P_L`.

Then the following identities hold exactly:

1. Each spatial triple satisfies
   `{Gamma_i,Gamma_j} = 2 delta_ij I`.
2. The derived matrices have the cyclic form
   `B_1 = -(i/2) Gamma_2 Gamma_3` and cyclic permutations, form an exact `su(2)`
   triple, and obey
   `[B_a,B_b] = i eps_(abc) B_c`.
3. The spatial Clifford generators obey
   `[B_a,Gamma_b] = i eps_(abc) Gamma_c`.
4. `gamma_5` anticommutes with every spatial `Gamma_i`; `P_L` and `P_R`
   are complementary orthogonal projectors; and every `B_a` commutes with
   both projectors.
5. The chiral family obeys
   `[B_a,Y_b] = i eps_(abc) Y_c`.
6. The adjoint Casimir is `2` on both displayed vector families:
   `sum_a [B_a,[B_a,X_b]] = 2 X_b` for `X_b = Gamma_b` or `Y_b`.
7. The `C^16` chiral family has Gram matrix
   `Tr(Y_i^dag Y_j) = 8 delta_ij`.
8. For every scalar `lambda` in `C`, the family `lambda Y_i` obeys the same
   vector and Casimir equations, and
   `Tr((lambda Y_i)^dag (lambda Y_j)) = |lambda|^2 8 delta_ij`.

Item 8 is a homogeneous closure property of the displayed matrix equations.

## Derivation

The Pauli relations give each Clifford identity directly under Kronecker
multiplication. For an arbitrary spatial Clifford triple,

`[Gamma_m Gamma_n,Gamma_b]`

`= 2 delta_(nb) Gamma_m - 2 delta_(mb) Gamma_n`.

Substitution in the definition of `B_a` gives

`[B_a,Gamma_b] = i sum_c eps_(abc) Gamma_c`.

The same Clifford products give the cyclic formulas for `B_a` and then

`[B_a,B_b] = i sum_c eps_(abc) B_c`.

Applying the vector commutator twice yields

`sum_a [B_a,[B_a,Gamma_b]] = 2 Gamma_b`.

On `C^16`, `gamma_5` anticommutes with each spatial generator. It therefore
commutes with every even product `Gamma_m Gamma_n`, so
`[B_a,P_L] = [B_a,P_R] = 0`. Consequently,

`[B_a,Y_b]`

`= [B_a,P_R Gamma_b P_L]`

`= P_R [B_a,Gamma_b] P_L`

`= i sum_c eps_(abc) Y_c`.

The same double-commutator calculation gives the Casimir identity for `Y_b`.
Moreover,

`Y_i^dag Y_j = P_L Gamma_i Gamma_j P_L`.

The explicit Kronecker traces are `Tr(P_L)=8` and
`Tr(P_L Gamma_i Gamma_j)=0` for `i != j`, proving
`Tr(Y_i^dag Y_j)=8 delta_ij`.

Finally, commutators are complex-linear in `Y`, while the Gram form is
conjugate-linear in its first argument and linear in its second. Thus, for a
symbolic scalar `lambda`, the vector and Casimir residuals acquire an overall
factor `lambda`, and the Gram matrix acquires the factor
`conjugate(lambda) lambda = |lambda|^2`.

## Boundary

This theorem concerns only the displayed finite matrices and their exact
algebraic identities. Identifications of these matrices with a physical
system, and coefficients attached to any such identification, are outside
the theorem and are neither asserted nor denied.

**Downstream hygiene (2026-07-18):** references to this row may cite only the
displayed finite-matrix identities; they supply no additional physical
identification or coefficient statement.

## Executable verification

Run:

`python3 scripts/frontier_dm_neutrino_weak_vector_theorem.py`

The runner uses exact SymPy matrices over Gaussian rationals for every
load-bearing identity. It separately reports numerical support and hostile
mutation checks. The mutation suite rejects wrong bivector sign and
normalization, wrong vector sign and index, reversed projector orientation,
a false Casimir coefficient, false diagonal and off-diagonal Gram claims, and
a false invariant-Gram claim under non-unit rescaling.
