# Supplied OS0 Staggered Action: KS Blocking and Four-Taste Module Narrow Theorem

**Date:** 2026-07-11
**Claim type:** bounded_theorem
**Status authority:** independent audit lane. This source proposal does not
set or predict an audit verdict.
**Primary runner:**
[`scripts/frontier_staggered_os0_supplied_action_ks_blocking_four_taste_module_2026_07_11.py`](../scripts/frontier_staggered_os0_supplied_action_ks_blocking_four_taste_module_2026_07_11.py)
**Cached runner output:**
[`logs/runner-cache/frontier_staggered_os0_supplied_action_ks_blocking_four_taste_module_2026_07_11.txt`](../logs/runner-cache/frontier_staggered_os0_supplied_action_ks_blocking_four_taste_module_2026_07_11.txt)

## Claim

Supply the one-component free Kogut-Susskind action on the OS0
`Z^3 x Z_tau` kinetic block,

```text
S = sum_n chi_bar(n) [m chi(n)
    + (1/(2a)) sum_mu eta_mu(n)
      (chi(n+e_mu)-chi(n-e_mu))],

eta_mu(n)=(-1)^(sum_{nu<mu} n_nu),   mu=0,1,2,3.
```

For this supplied action, the block decomposition `n=2y+b`,
`b in {0,1}^4`, and a momentum-local rephasing derive the exact reduced
operator

```text
D_red(p) = m I_16 + i sum_mu alpha_mu sin(p_mu a)/a,
(alpha_mu)_(b xor e_mu,b) = eta_mu(b).
```

The four matrices `alpha_mu` furnish a 16-dimensional complex module for
`Cl_4(C) = M_4(C)`. Their character is four times the character of the
unique 4-dimensional irreducible module. Therefore the blocked carrier is
the direct sum of four Dirac-spin modules,

```text
C^16 = C^4_spin tensor C^4_taste,
alpha_mu = gamma_mu tensor I_4,
N_taste = 4,
```

after a choice of module isomorphism. The multiplicity four follows from the
action and its canonical phases; it is not inferred from the integer identity
`16=4*4` or from Hamming-weight enumeration by itself.

## Supplied-action boundary

The action displayed above is the premise of this bounded theorem. The theorem
does not derive that action from Lattice, Qubit, Admissibility, and Record, and
does not identify it as the realized charged-lepton matter carrier. It derives
the Kogut-Susskind blocking and module multiplicity once that action is
supplied. It supplies no generation identification, occupancy/readout rule,
value of `r`, phase `delta`, mass, coupling, probability rule, or outcome
dictionary.

This boundary is load-bearing. The theorem repairs an algebraic supplier gap
in the species-reduction row; it does not discharge the physical-carrier or
charged-lepton occupancy-grain questions.

## Exact derivation

### Blocked finite difference

Write `n=2y+b` with `b in {0,1}^4`, and Fourier transform the coarse cell
coordinate `y`. Set

```text
t_mu = exp(i p_mu a),   K_mu = 2 p_mu a.
```

For a fixed direction `mu`, the blocked finite-difference matrix has one
nonzero entry in row `b`, column `b xor e_mu`. Its coefficient is

```text
eta_mu(b) (1-t_mu^(-2))/(2a),  b_mu=0,
eta_mu(b) (t_mu^2-1)/(2a),     b_mu=1.
```

Let `P_b=product_mu t_mu^(b_mu)`. In both cases,

```text
(P^(-1) D_mu P)_(b,b xor e_mu)
  = eta_mu(b) (t_mu-t_mu^(-1))/(2a)
  = i eta_mu(b) sin(p_mu a)/a.
```

Summing the four directions and the mass term gives the displayed
`D_red(p)` exactly. No small-`a` expansion is used.

### Clifford relations

For every block label `b`, `alpha_mu` flips bit `b_mu` with sign
`eta_mu(b)`. Flipping the same bit twice gives `alpha_mu^2=I_16`.
For `mu<nu`, flipping `b_mu` changes the exponent in `eta_nu` once, while
flipping `b_nu` does not change the exponent in `eta_mu`. Hence

```text
alpha_mu alpha_nu = - alpha_nu alpha_mu,
{alpha_mu,alpha_nu}=2 delta_(mu nu) I_16.
```

Thus the action supplies a representation of `Cl_4(C)` on the 16 blocked
components.

### Four-module multiplicity

The 16 ordered Clifford words

```text
alpha_0^(epsilon_0) ... alpha_3^(epsilon_3),
epsilon_mu in {0,1},
```

are linearly independent, so the represented algebra has complex dimension
16. Their traces are

```text
Tr(I_16)=16,
Tr(alpha_0^(epsilon_0)...alpha_3^(epsilon_3))=0
for nonzero epsilon.
```

Complex Clifford classification gives `Cl_4(C)=M_4(C)`, with a unique
irreducible module of complex dimension four. A 16-dimensional module is
therefore four copies of that irrep. The trace character confirms the
multiplicity: it is four times the irreducible character. Equivalently, the
commutant is `M_4(C)`, the taste factor.

The same Clifford relations give

```text
(sum_mu s_mu alpha_mu)^2 = (sum_mu s_mu^2) I_16,

[m I_16+i sum_mu s_mu alpha_mu]^(-1)
  = [m I_16-i sum_mu s_mu alpha_mu]
    /(m^2+sum_mu s_mu^2),

s_mu=sin(p_mu a)/a,
m^2+sum_mu s_mu^2 != 0.
```

At the excluded point `m=0` and `s_mu=0` for every `mu`, the operator is
zero and has no inverse.

The spectrum consequently consists of four identical Dirac-spin spectra.

## Relation to Hamming-weight enumeration

The block labels have multiplicities `(1,4,6,4,1)` by Hamming weight and sum
to 16. That enumeration establishes the blocked-component count and grading.
The multiplicity `N_taste=4` is established separately by the Clifford-module
decomposition above. This distinction prevents the arithmetic factorization
`16=4*4` from being used as a surrogate for the action-level taste derivation.

## Inputs and non-import statement

The load-bearing physical input is the explicitly supplied one-component free
OS0 staggered action and its displayed canonical phases. Mathematical
infrastructure consists of finite-dimensional complex linear algebra,
Laurent-polynomial identities, and the standard complex Clifford-algebra
classification `Cl_4(C)=M_4(C)`.

No observational number, fitted selector, external numerical comparator,
physical-species identification, charged-lepton readout rule, or additional
framework axiom or primitive is used.

## Validation

The exact SymPy runner checks:

1. the 16 block labels and their Hamming-weight multiplicities;
2. each Laurent-polynomial rephasing identity in four directions;
3. the full blocked operator identity;
4. the exact Clifford anticommutators;
5. exact rank 16 for the Clifford-word span;
6. the character `(16,0,...,0)`;
7. fourfold irreducible-module multiplicity; and
8. the exact scalar-denominator numerator identity and inverse on its declared
   nonzero-denominator domain; and
9. exclusion of the singular point `m=s_0=s_1=s_2=s_3=0`.

Expected result: `TOTAL: PASS=17, FAIL=0`.

## Dependency and downstream routing

This derivation is self-contained conditional on the displayed action; it
consumes no source-note effective status. The following are plain-text routing
pointers rather than load-bearing citation edges:

- `STAGGERED_DIRAC_SUBSTEP3_SPECIES_REDUCTION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`
  should cite this theorem when separating Hamming enumeration from the
  action-derived taste multiplicity.
- `LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md`
  contains a broader numerical implementation of the same blocked-action
  algebra as part of a continuum two-point-function packet.
- `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` retains the separate
  physical-carrier identification question.
