# Independent finite-mode diagonal-charge diagnostic check

Reviewed `native/neutral_mode_charges.py` and its JSON. The diagonal expectations, conditional Hellmann–Feynman signs, and common-normalization test are mathematically consistent with the declared finite-model scope. No heavy replay of the saved eigenvectors was performed.

## Gap derivatives and signs

For H_lambda=H−lambda O and differentiable resolved eigenbranches, Hellmann–Feynman gives

(d/dlambda)(E_n−E_0)|_0 = −(<n|O|n>−<0|O|0>) = −delta O_n.

Thus the fractional gap derivative is −delta O_n/Delta_n, exactly the script's definition. In a degeneracy, actual first-order branch slopes are the eigenvalues of the perturbation restricted to that degenerate eigenspace; arbitrary diagonal expectations need not be branch slopes. The corresponding qualification is required for the reference level as well as excited levels. The stored quantity remains a well-defined diagonal expectation diagnostic regardless.

The `uniform_H_rescale_derivative=gap` field corresponds to H_epsilon=(1+epsilon)H. If one instead uses the same minus-source convention with O=H, H_lambda=(1−lambda)H, the derivative is −gap. Both are correct under their respective parameter definitions; the description should state the plus-rescaling convention to avoid an apparent sign inconsistency.

## What the reported unequal ratios establish

For `sum_existing_C`, the three reported fractional derivatives are approximately

0.0644764079968, 0.582717534093, 0.432206918271.

A nonzero common normalization O->k O multiplies all these ratios by k. It cannot make three unequal ratios into one shared nonzero fractional energy rescaling. A common identity shift does not change any gap derivative. This is an exact algebraic implication of the reported diagonal values; assigning numerical certification requires the independent eigenvector/residual evidence, which this script does not reproduce.

More generally, adding a uniform H component shifts all fractional slopes by the same amount. It cannot remove their differences while retaining a nonzero coefficient of this O. This does not exclude other operators, state-dependent effects, or nonlinear environmental mechanisms; it isolates the failure of this particular fixed operator as a uniform first-order spectral rescaling on these three states.

Without branch resolution, the safest conclusion is that the compressed diagonal data in the three supplied vectors are not proportional to their gaps. With the stated eigenbranch conditions, the stronger conclusion is that their physical first-order perturbative gap slopes in this finite Hamiltonian are unequal. Neither conclusion should be promoted to a statement about actual matter species.

## Operator and boundary definition

The code's summed operator includes a same-axis distance-two pair whenever both endpoints exist, so on the open 3x3x3 cube it contains 27 terms: nine for each axis. It is not 27 copies of the interior three-term C without boundary modifications. This is a definite uniform coefficient on the EXISTING pair terms, but its local coordination and finite-boundary environment vary.

Writing d_x for the number of incident native bonds at x and using J=1, the open-graph identity is

C_partial,x = 2 e_x²−(d_x/2) I,

where C_partial,x sums only opposite-neighbor pairs that exist. Therefore sum_existing_C=2 sum_x e_x²−N_bonds I. This is a useful exact definition of the probe, not a derived universal scalar coupling. No physical meaning of lambda is supplied merely by using this differentiation direction.

## Limits of the inference

The central-C slopes even have differing signs, while the summed-C slopes differ substantially in magnitude. These are finite open-system diagnostics in a selected symmetry sector. They do not constitute an equivalence-principle experiment, a measurement of gravitational charges, a proof that the same failure persists in a thermodynamic/continuum limit, or an exclusion of all scalar/matter coupling mechanisms. Central-local and summed-boundary-sensitive probes are not automatically the operator produced by a physical homogeneous cosmological background.

The test legitimately removes a specific shortcut: a single nonzero normalization of the chosen summed composite cannot be identified with uniform spectral rescaling of these three supplied modes on the basis of these diagonal data. It does not derive the source/detector or cosmological identification that would be needed to turn those modes and probe parameters into physical observables.
