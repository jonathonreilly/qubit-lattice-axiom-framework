# Root review of the independent variance extension

2026-09-24, after reading sealed PRE. This supplement does not modify the
personal derivation sealed before disclosure. The exact full-vector identity,
explicit remainder identities and uniform rotor loss bound below originated
in the independent PRE, SHA-256
57819426fec612dcb000612dcb8419cca34d3538904dcaefea13fb4820181d8e.
The root has read its complete argument, independently built control source,
all output including the 36 charge-word cover rows, and source/evidence seals.
This is a mathematical review and synthesis, not a second blind derivation.

## Exact identity and nonnegative remainder

For x'=-iHx-alpha Gamma x with self-adjoint H,Gamma and real alpha,
Hx=i(x'+alpha Gamma x). Expanding the squared norm gives

    ||Hx||^2=||x'||^2+alpha^2||Gamma x||^2
                      +alpha d<x,Gamma x>/dt.

The sign is positive; the inner-product convention does not change the real
cross term. With alpha=kappa/(2 epsilon^2), multiplication by epsilon^2
and integration produces endpoint coefficient kappa/2. On any fixed [a,b],
a>0, the parent bounds z1=O(epsilon^(9/4)), z2=O(epsilon^4) and
Gamma J0=epsilon Gamma F+O(epsilon^2) imply

    Gamma v/epsilon -> Gamma_infinity F_infinity u uniformly,
    <v,Gamma v>=O(epsilon^2).

The first follows from bounded strong convergence on the compact limiting
orbit; the second follows from Gamma being supported on the first bare grade,
whose norm in v is O(epsilon). The bounded ordinary mean can be subtracted.
Thus the PRE's exact identity proves

    epsilon^2 integral_a^b Var_H rho dt
      -epsilon^2 integral_a^b ||v'||^2 dt
      -> kappa/2 [S(a)-S(b)].

Uniform v->u in norm also gives microscopic second-birth probability
p2,epsilon(t)->1-S(t). Hence the survival difference can be replaced by
p2,epsilon(b)-p2,epsilon(a), with an o(1) remainder. The derivative norm is
nonnegative but is not shown to vanish. This establishes the lower bound
without estimating individual energy cross terms and independently checks
the personal Sylvester route's sign and coefficient.

For an alternative explicit unresolved term, the PRE estimates integrated
low/first-high interference after removing the frequency delta/epsilon^4.
The endpoint and derivative estimates multiply M1=O(epsilon^(9/4)), so the
scaled cross term is O(epsilon^(1/4)). The second-high energy norm is O(1),
and the first-high energy norm is O(epsilon^(-7/4)); the remaining scaled
second-high square and high/high cross term vanish. Consequently one can
replace the derivative remainder by

    epsilon^2 integral_a^b ||H E1 v||^2 dt

in the displayed asymptotic identity. This quantity is also nonnegative
and unresolved. The coarse O(epsilon^(-7/2)) upper bound is valid but not
a sharp asymptotic. Neither representation justifies dropping its remainder.

## Physical-star rotor coercivity

The PRE's bound 2I<=Lambda<=16I is a bound on the full physical rotor low
space, not an inference from the separate finite flat-phase matrix check.
Each N=6 low word has four occupied A vertices, two occupied B vertices,
two vacant B vertices, five positive charges and one negative charge.
The vacant B pair has two common A neighbors. Only these active centers
can hop into an input for a subsequent original mark. Different centers
produce different vacant A vertices, so their output spaces are orthogonal.

Freezing all fields and matter outside a three-edge star preserves that
star's hopping operator. At each B leaf Gauss law determines the single
remaining star field from its charge and the frozen other two fields.
At the center, Gauss is preserved by conservation of total charge on the
star. On the rotor all integer fields are allowed, so no boundary deletes
one of these entries. This justifies exact finite direct-sum blocks.

If the unique negative charge is outside the star, the two occupied local
charges are positive. The local input is its occupied B leaf and the local
output is its remaining vacant B leaf. The matrix is the unsigned J-I,
whose squared singular values are 1,1,4. The hopping convention has no
fermionic incidence signs. If the negative charge is inside, the six possible
local inputs and outputs instead have squared singular values
0,1,1,3,3,4. The latter block supplies only nonnegativity and the common
upper bound, not a local strict lower bound.

For each fixed vacancy pair, the occupied-site pairs in the two active
stars are disjoint: their centers are distinct A vertices and their third
B neighbors are the distinct occupied B vertices. The single negative
charge lies in at most one pair. Thus at least one active star is in the
first class, and the sum of its diagonal support projections is at least I.
Multiplying the local Gram sum by the original rotor loss factor two yields
2I<=Lambda<=16I. The direct-sum and diagonal-cover arguments hold on arbitrary
superpositions, not merely on the 36 zero-field charge labels.

Consequently e^(-16 kappa t)<=S(t)<=e^(-2 kappa t), and

    kappa/2 [S(a)-S(b)] >=
      kappa/2 e^(-16 kappa a)(1-e^(-2 kappa(b-a))) > 0.

This strengthens the personal candidate from a bound conditional on positive
interval loss to a strictly positive bound on every fixed nonempty later
interval, within exactly the supplied rotor sector and positive kappa.
No analogous spin-boundary lower bound or new physical rate is inferred.

## Scope and publication decision

The extension is mathematically consistent with the stated provisional parent
bounds. It may be included in the publication with its PRE origin explicit.
The proposed claim remains a conditional quantitative theorem about this
model. It does not solve pointwise variance, select a conserved total energy,
derive a physical reservoir, exclude other formations or adopt a new axiom.
The original root proof, PRE and controls remain immutable. A released-source
POST and final source comparison are still required before publication.
