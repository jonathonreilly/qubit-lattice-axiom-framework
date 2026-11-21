# The response estimate missing at nested junctions

Author: openai/gpt-6-astra/max, mac-mini-codex. Source:
`b58dac27c53adb17f47520c8ca2f784014a8dcbe`.
Author mathematics, not an independent review or audit. No numerics.

This note concerns a possible repair using only active energy. The
untrimmed-energy counterexample is in `paid-inputs-frozen-energy.md`.
Nothing here proves the repaired CI estimate.

## 1. Why a local incidence count does not bound a recursion

**Discharged (logical obstruction to the stated argument).** A path
graph has at most two neighbors at each vertex and arbitrarily long
dependency paths. For a recursion e_m=eta+e_{m-1}, e_0=0, it has
e_m=m eta. A bounded local incidence count therefore cannot by itself
bound the length or norm of a dependency chain. Likewise an estimate
by C exp(-rho distance) does not ensure that the norm of the transfer
operator is below 1: adjacent *closed* bricks have distance zero.
This is a counterexample to that inference, not to a Yang-Mills
response estimate. In particular it is not a field counterexample to
the constant C_J in `quiet-boundary-rarity.md:33`.

## 2. A sufficient same-level response estimate and its proved sum

Fix a level, its parent size L, and a tiling by axis-parallel bricks
of side t_0>=8L with disjoint interiors. A finite sequence freezes
distinct bricks b_1,...,b_M, possibly through many separate stops.
Let W_m be the constrained minimizing lift after m freezes, with the
same parents throughout. Read curvature in the consistent block-tree
frames required by the quiet test. Let Q be a testing cube of
l^infinity diameter at most t_0/4, and put

    ||H||_Q = (sum_{p in Q} |H_p|^2)^(1/2).

**Gap (IR, incremental response).** A sufficient estimate is

    ||Theta(W_m)-Theta(W_{m-1})||_Q
       <= C_R eps_q T exp(-rho dist_infinity(Q,b_m)/L).      (IR)

Its quantifiers include every previous frozen set and its quiet data,
every new brick, and quietness measured relative to the *local* lift
with those previous data, with Dev at most eps_q^2 T^2. Tails between
the local and global constrained lift must be included in C_R, with a
proved uniform bound. C_R and rho>0 must be absolute, free of L, x,
the number of prior freezes and volume. Existence of the lifts and
their placement in the regular chart is also part of this input,
or must be justified by a continuation argument. It cannot be assumed
from the stability conclusion it is meant to prove.

The bound on a covariance at a fixed regular background in Theorem
F-D is not (IR): the latter is a nonlinear comparison with nonzero
boundary displacement, exact fixed links, relative quiet data and a
uniform prefactor. The unproved relative gauge estimate is explicitly
acknowledged at `quiet-boundary-rarity.md:29`.

**Implication (proved under IR).** There is S_4(rho)<infinity such that

    ||Theta(W_M)-Theta(W_0)||_Q
          <= C_R S_4(rho) eps_q T,                         (J1)

independently of the order and number of freezes, L and the volume.

Proof. Let B_m be the bricks with distance to Q in
[m t_0,(m+1)t_0), m>=0. A brick meeting this neighborhood is contained
in the l^infinity enlargement by another t_0. Comparing its volume
t_0^4 with the containing cube, using disjoint interiors, gives

    #B_m <= [2(m+3)]^4.

The same upper bound applies on a compatible torus, using periodic
distance; the volume of a periodic ball is no larger than that of
the corresponding Euclidean cube, and the whole-torus case only
decreases the bound. Thus

    sum_b exp(-rho dist_infinity(Q,b)/L)
       <= S_4(rho) := sum_{m>=0} [2(m+3)]^4 exp(-8rho m).

This series converges: the ratio of consecutive summands tends to
exp(-8rho)<1. Telescope W_M-W_0 in curvature and use the triangle
inequality and (IR). Every brick occurs at most once in the sum.
This proves (J1). In particular C_J=[C_R S_4(rho)]^2 is sufficient
for the local squared response. No assertion about a dependency
chain having at most five steps is used. QED.

**Implication (the hostile configurations).** A layer whose residual
is exactly eps_q T is permitted in (IR); the bound does not demand
a vanishing residual. Several touching frozen bricks are included
in B_0, whose cardinality is bounded by the same volume argument.
Arbitrarily many same-level stops are handled by the summation, not
by truncating the number of predecessors. These are consequences of
the missing IR input, not tests establishing it.

## 3. Different levels and the exact outstanding inequality

**Gap.** Frozen bricks at different levels do not have disjoint
physical interiors. Counting each once at its own level does not
justify summing the bound in section 2 over levels. A sufficient
joint version, with all scale conversions included, is

    ||Theta(W_m)-Theta(W_{m-1})||_Q
                <= C_R eps_q T K(Q;b_m,ell_m),
    sup_{Q, compatible histories} sum_m K(Q;b_m,ell_m)
                <= C_sum < infinity.                     (IR-nest)

Here Q and its curvature norm are at the level of the descent currently
being performed, not the untrimmed sum of all underlying frozen fine
action. That latter reading is obstructed by the companion example.
The index ell_m records the level of the added data, whose
quiet norm is in its own level's units. Consequently K must include
these rescalings. C_R,C_sum must be free of L, x, total depth and
volume. A proved transfer contraction with norm q<1, uniform in these
parameters, would be another sufficient route. Neither route follows
from a count of bricks in one ball. Clearance is useful geometry but
is not itself a bound on the scaled response operator.

**Implication (algebra only).** IR-nest gives

    ||Theta(W^d)-Theta(W^bulk)||_Q^2
                       <= (C_R C_sum)^2 eps_q^2 T^2.        (J2)

The proof is the same finite telescoping and triangle inequality.
Combining a correctly normalized energy version of J2 with the bulk
trial estimate gives the local target bound QT^d in the companion
energy note, by |u+v|^2<=2|u|^2+2|v|^2. That statement also requires
comparison of this curvature norm with the active fine action; no
such multilevel comparison is supplied by this algebra.

**Gap (honest stop).** What remains is a uniform fixed-data response
or contraction estimate sufficient for QT^d, together with the
fixed-link RF/bump estimate. The same-level summation is discharged
as an implication, but IR, IR-nest, J2 for the actual nonlinear
minimizers, and QT^d are not discharged. Their relations are not
asserted to be independent. No W1, W2 or LNC proof is built on them.
