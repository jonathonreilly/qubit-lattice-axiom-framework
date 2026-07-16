# Defined Four-Bit Periodic Difference Operator: Exact Blocking and Module Decomposition

**Date:** 2026-07-11
**Claim type:** bounded_theorem
**Status authority:** independent audit lane. This source proposal does not
set or predict an audit verdict.
**Primary runner:**
[`scripts/frontier_staggered_os0_supplied_action_ks_blocking_four_taste_module_2026_07_11.py`](../scripts/frontier_staggered_os0_supplied_action_ks_blocking_four_taste_module_2026_07_11.py)
**Cached runner output:**
[`logs/runner-cache/frontier_staggered_os0_supplied_action_ks_blocking_four_taste_module_2026_07_11.txt`](../logs/runner-cache/frontier_staggered_os0_supplied_action_ks_blocking_four_taste_module_2026_07_11.txt)
**Legacy identity:** the stable file path and claim id are preserved for graph
continuity. Their physical terms are identity-only; they do not state the
content or hypotheses of the theorem below.

## Claim

This is an exact theorem about a defined finite periodic difference operator.
The signs, shifts, block map, and rephasing are definitions, not conclusions
about a physical action.

Fix positive integers `M_0,...,M_3`, a nonzero scalar `a`, and the finite
periodic set

```text
Lambda_M = product_(mu=0)^3 Z/(2 M_mu)Z.
```

For `n in Lambda_M`, define

```text
eta_mu(n) = (-1)^(sum_(nu<mu) n_nu),

(D f)(n) = m f(n)
           + (1/(2a)) sum_mu eta_mu(n)
             [f(n+e_mu)-f(n-e_mu)].                         (1)
```

Then the exact block map `n=2y+b`, `b in {0,1}^4`, and the diagonal
fiber rephasing defined below give

```text
P(t)^(-1) B(t) P(t)
  = m I_16 + sum_mu [(t_mu-t_mu^(-1))/(2a)] alpha_mu.        (2)
```

The four defined matrices `alpha_mu` obey the complex Clifford relations.
More strongly, the note constructs an explicit unitary `U` over the Gaussian
rationals and explicit `4 x 4` matrices `gamma_mu` such that

```text
U^dagger alpha_mu U = gamma_mu tensor I_4.                  (3)
```

Thus the defined 16-dimensional module is exactly four identical copies of a
defined irreducible 4-dimensional matrix module. This is a module
multiplicity statement only. It is not a particle, carrier, taste,
generation, continuum-species, or reconstruction theorem.

## Exact blocking and rephasing

Write a site uniquely as `n=2y+b`. Because the periods are even,
`eta_mu(2y+b)=eta_mu(b)`. On a coarse Fourier character with
`q_mu^(M_mu)=1`, choose any `t_mu` satisfying `t_mu^2=q_mu`. The fiber matrix
of (1) is

```text
B(t) = m I_16 + sum_mu B_mu(t),

(B_mu(t))_(b,b xor e_mu)
  = eta_mu(b) (1-t_mu^(-2))/(2a),   b_mu=0,
  = eta_mu(b) (t_mu^2-1)/(2a),      b_mu=1,                 (4)
```

with all other entries zero. Equation (4) follows directly from the two
defined shifts in (1): a boundary crossing changes `y_mu` by `-1` in the
first case and by `+1` in the second.

Define

```text
P(t)_(b,b) = product_mu t_mu^(b_mu),
(alpha_mu)_(b,b xor e_mu) = eta_mu(b).                      (5)
```

For `b_mu=0`, conjugation multiplies the coefficient in (4) by `t_mu`; for
`b_mu=1`, it multiplies it by `t_mu^(-1)`. Both cases give
`(t_mu-t_mu^(-1))/(2a)`, proving (2) as an identity of finite
Laurent-polynomial matrices. If `t_mu=exp(i p_mu a)`, the coefficient is
`i sin(p_mu a)/a`. No continuum limit or small-`a` expansion is used.

## Clifford relations

The matrix `alpha_mu` flips bit `b_mu` and multiplies by
`eta_mu(b)`. Since `eta_mu` does not depend on `b_mu`,
`alpha_mu^2=I_16`. If `mu<nu`, flipping `b_mu` changes the exponent defining
`eta_nu` once, while flipping `b_nu` does not change `eta_mu`. Hence

```text
alpha_mu alpha_nu = -alpha_nu alpha_mu,
{alpha_mu,alpha_nu}=2 delta_(mu nu) I_16.                   (6)
```

The 16 ordered words in the `alpha_mu` are Hilbert-Schmidt orthogonal and
therefore linearly independent. Their traces are `16` for the identity and
zero for every nonidentity word. These are exact consistency certificates;
the fourfold decomposition below does not rest on dimension counting or the
character alone.

## Explicit unitary module certificate

Define a second set of signed bit-flip matrices by

```text
(beta_mu)_(b xor e_mu,b) = (-1)^(sum_(nu>mu) b_nu).         (7)
```

Every `beta_mu` commutes with every `alpha_nu`, while the `beta_mu` themselves
obey the same Clifford relations. Put

```text
Q_01 = i beta_0 beta_1,
Q_23 = i beta_2 beta_3,
E_++ = (1/4)(I_16+Q_01)(I_16+Q_23).                        (8)
```

Let `e_0000` be the coordinate vector at the zero bit string and set

```text
v   = 2 E_++ e_0000,
w_0 = v,
w_1 = alpha_0 v,
w_2 = alpha_2 v,
w_3 = alpha_0 alpha_2 v.                                  (9)
```

Direct exact multiplication gives `E_++^2=E_++`, `rank(E_++)=4`, and an
orthonormal ordered basis `(w_0,w_1,w_2,w_3)` of its range. For
`r,s in {0,1}`, define `R_rs=beta_0^r beta_2^s`. The four spaces
`R_rs range(E_++)` are mutually orthogonal, have dimension four, sum to
`C^16`, and are invariant under every `alpha_mu`.

Let `(f_rs)` be the ordered basis `(f_00,f_01,f_10,f_11)` of `C^4`. Define
`U:C^4 tensor C^4 -> C^16` by

```text
U(e_j tensor f_rs) = R_rs w_j.                             (10)
```

Equation (10) gives an explicit unitary. In the basis (9), the four matrices
on the first factor are

```text
gamma_0 = [[0, 1, 0, 0],
           [1, 0, 0, 0],
           [0, 0, 0, 1],
           [0, 0, 1, 0]],

gamma_1 = [[0,-i, 0, 0],
           [i, 0, 0, 0],
           [0, 0, 0,-i],
           [0, 0, i, 0]],

gamma_2 = [[0, 0, 1, 0],
           [0, 0, 0,-1],
           [1, 0, 0, 0],
           [0,-1, 0, 0]],

gamma_3 = [[0, 0,-i, 0],
           [0, 0, 0, i],
           [i, 0, 0, 0],
           [0,-i, 0, 0]].                                 (11)
```

The 16 words in (11) span `M_4(C)` exactly, so this 4-dimensional module is
irreducible. Since every `R_rs` commutes with every `alpha_mu`, multiplication
of (10) by `alpha_mu` proves (3) entry by entry. The claimed multiplicity is
therefore certified by an explicit unitary intertwiner, not by `16=4*4`.

An independent exact route solves the full commutant equations
`X alpha_mu=alpha_mu X`. Their solution space has dimension 16; the 16 words
in the `beta_mu` form a basis. The four joint spectral projectors of
`Q_01,Q_23` have rank four, and compressing the commutant to any one of them
gives only scalar multiples of that projector. This independently proves
four irreducible, mutually intertwined summands.

## Consequences inside the defined theorem

For scalars `s_mu`, (6) gives

```text
(sum_mu s_mu alpha_mu)^2 = (sum_mu s_mu^2) I_16.            (12)
```

Therefore, whenever `m^2+sum_mu s_mu^2` is nonzero,

```text
[m I_16+i sum_mu s_mu alpha_mu]^(-1)
  = [m I_16-i sum_mu s_mu alpha_mu]
    /(m^2+sum_mu s_mu^2).                                  (13)
```

At `m=s_0=s_1=s_2=s_3=0`, the matrix is zero and (13) is outside its stated
domain. Equation (3) also shows that the characteristic polynomial of the
defined `16 x 16` matrix is the fourth power of that of its defined `4 x 4`
factor; every eigenvalue's algebraic multiplicity is therefore multiplied by
four.

The Hamming-weight counts of the block labels are `(1,4,6,4,1)`. They record
only the grading of `{0,1}^4`; they play no role in proving module
multiplicity.

## Hypothesis and import firewall

The load-bearing inputs are exactly the definitions (1), (4), (5), and (7),
plus finite-dimensional complex linear algebra. The note consumes no
physical action, framework carrier, axiom, approved primitive, source/action
bridge, observational value, fitted selector, external numerical comparator,
or continuum assumption. In particular, none of the following follows from
this theorem:

- identification of `D` with a staggered fermion or Kogut-Susskind action;
- identification of either tensor factor with physical spin or taste;
- a Dirac field, physical matter carrier, OS0 reconstruction, or continuum
  species count;
- a taste, generation, occupancy, readout, mass, coupling, or probability
  statement.

Those phrases occur here only to deny an inference and to preserve the legacy
identity boundary. Any positive physical use needs a separate retained
carrier/action/continuum identification theorem.

The current minimal-surface kinetic/corner non-forcing note is relevant
context but is not a dependency: it concerns physical-law selection, whereas
this theorem defines its operator and makes no selection claim.

## Validation

The exact SymPy runner has four modes:

1. normal mode checks the finite periodic blocking coefficients, Laurent
   rephasing, Clifford relations, explicit `U`, equation (3), irreducibility,
   character, inverse, and hypothesis firewall;
2. `--independent` checks the full commutant, its signed-flip basis, the four
   rank-4 projectors, and scalar compressed commutants;
3. `--hostile` verifies rejection of mutated sign, shift, Clifford generator,
   intertwiner, multiplicity, and illicit physical-inference proposals; and
4. `--intentional-failure` installs those mutations as if they were valid,
   emits failures, and exits nonzero.

Normal execution exits nonzero on any failed check. The committed cache is the
normal-mode output and is keyed to the runner source SHA.

## Dependency and downstream routing

This theorem is self-contained and has no load-bearing source-note dependency.
Its one direct semantic consumer is the existing
`STAGGERED_DIRAC_SUBSTEP3_SPECIES_REDUCTION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`
row. This is a downstream routing pointer, deliberately not a markdown
dependency link. That consumer may use only the exact defined-operator
identities above. It may not inherit a physical action, carrier, taste, spin,
species, or continuum interpretation from this note.
