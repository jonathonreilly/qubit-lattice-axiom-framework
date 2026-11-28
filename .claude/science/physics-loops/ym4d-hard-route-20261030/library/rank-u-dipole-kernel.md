# The dipole pairing needed by (RANK-U)

Source pin: `892504e4c63f195fbd791a1db913f67b4b749459`.
Author: openai/gpt-6-astra/max, mac-mini-codex. Research mathematics only.
This entry supplies elementary proofs, not a literature import. Its target is
the sentence beginning "But kappa" in `../parts/witness.md`, Text 3.14.
The Green-function asymptotic for an actual level-j action is a separate input.

## 1. Conventions and the leading matrix

**Discharged (algebra).** Let V=R^4 with its usual metric and orientation.
Represent a two-form d by the antisymmetric matrix d_{ab}, and use
`<u,d> = sum_{a<b} u_ab d_ab`. For z!=0 set r=|z|, n=z/r and

    S_n d = n^flat wedge i_n d,
    Qhat(n) d = d - 2 S_n d.

Then `Qhat(n)d = R_n d R_n^T`, where `R_n=I-2nn^T` is a reflection.
Indeed the right side has entries

    d_ab - 2 n_a sum_c n_c d_cb + 2 n_b sum_c n_c d_ca;

the term with four factors of n vanishes by antisymmetry. This is exactly
`d-2 n^flat wedge i_n d`. Consequently Qhat is self-adjoint, orthogonal,
and Qhat^2=I. In particular it is invertible.

**Implication (dipole interpretation).** Suppose a conserved, finitely
supported vector current J is convolved with `G(z)=1/(4 pi^2 |z|^2)`.
For lattice currents use link midpoints in the moments. Conservation, tested
against the site polynomials x_a and x_a x_b, gives

    sum_l J_a(l)=0,
    d_ab := sum_(links in direction b) midpoint(l)_a J_b(l),
    d_ab = -d_ba.

The lattice statements are exact: the difference of x_a x_b along a b-link
is its midpoint a-coordinate (with the corresponding second term when
a=b). The same identities follow by integration by parts in the continuum.
The first nonzero Taylor term in the potential is

    E_b(z) = -sum_a d_ab partial_a G(z)
           = (1/(2 pi^2)) sum_a d_ab z_a / r^4.

Taking `partial_a E_b - partial_b E_a` gives

    F_ab(z) = (1/(pi^2 r^4)) [d_ab
                 -2 n_a sum_c n_c d_cb +2 n_b sum_c n_c d_ca].       (K1)

Thus the homogeneous leading dipole matrix is
`Q(z)=(pi^2 r^4)^(-1) Qhat(n)`, up to an overall dipole sign convention.
The Taylor remainder and its level-j uniformity are not asserted here.
Equation (K1) agrees with the 34 component displayed in witness Lemma 3.4.

## 2. An exact failure of the scalar-kernel inference

**Discharged.** Invertibility of Q(z) does not imply that
`<u,Q(z)d>` is a nonzero function for nonzero u,d. For example,

    u = e0 wedge e1,        d = e2 wedge e3

give zero for every z!=0. Their inner product is zero; `i_n u` is supported
in coordinates 0,1 and `i_n d` in coordinates 2,3, so

    <u,Qhat(n)d> = <u,d> - 2 <i_n u,i_n d> = 0.                    (K2)

There is also a three-dimensional obstruction. If `*` denotes the Euclidean
Hodge star, a reflection reverses orientation, so
`*Qhat=-Qhat*`. To verify this without a transformation rule, use the defining
identity `a wedge *b=<a,b> vol`, apply the orthogonal reflection to both
sides, and use `R_n vol=-vol`; nondegeneracy of the wedge pairing gives the
displayed identity. Hence any two self-dual forms u,d pair to zero through
Qhat; the same holds for two anti-self-dual forms. For example
`u=d=e01+e23` has squared norm 2, whereas (K2) is still identically zero.

These are counterexamples to the auxiliary assertion about arbitrary u,d.
They are not counterexamples to (RANK-U): that would additionally require
constructing t whose constrained moment and dipole images have this property.

## 3. The exact annihilator and a sufficient repair

**Discharged.** For fixed nonzero u let

    Ann(u) = {d : <u,Qhat(n)d>=0 for every unit n}.

Its dimension is at most 3. It is the same-duality three-space if u is
self-dual or anti-self-dual; otherwise `Ann(u)=span(*u)`.

Proof. Orthogonally choose coordinates with `u=a e01+b e23`, a!=0.
For completeness such coordinates can be obtained by maximizing |Uv|^2 on
the unit sphere, where U is the antisymmetric matrix of u. Differentiating
at a maximizer gives `-U^2 v=a^2 v`. The span of v and Uv/a is U-invariant,
its orthogonal complement is invariant by antisymmetry, and a skew map on
that two-dimensional complement is a multiple of the standard rotation.
The signs of the oriented basis vectors accommodate either sign of b.

Write `d=p e01+q e02+r e03+s e12+t e13+v e23`.
Since `i_n u=U^T n`, (K2) vanishes for every n precisely when

    UD+DU = -<u,d>I.

This follows by comparing the symmetric quadratic form on every unit vector;
its diagonal entries are recovered at coordinate vectors and off-diagonal
entries at their normalized pairwise sums. Matrix multiplication gives

    ap=bv,    as=br,    ar=bs,    at=-bq,    aq=-bt.               (K3)

If a^2!=b^2, q=r=s=t=0 and (p,v) is proportional to (b,a), proving the
one-dimensional assertion. If b=a, the solutions have p=v, s=r, t=-q,
the self-dual space. If b=-a, they are the anti-self-dual space. This also
proves the dimension bound in the degenerate case b=0. []

**Implication.** If a cell's moment image contains a nonzero u and its
dipole image D has dimension at least 4, some d in D and some n have
`<u,Qhat(n)d>!=0`. Dimension 3 also suffices when D is neither of the two
duality spaces. Nonzero D alone does not suffice.

**Discharged (finite directional test).** It suffices to test the ten
directions `e_a` and `(e_a+e_b)/sqrt(2)`, a<b. The pairing is the quadratic
form with matrix `<u,d>I+UD+DU`. The four coordinate tests give its diagonal;
the six other tests then give its off-diagonal entries. Thus all ten tests
vanish if and only if the pairing vanishes at every direction.

## 4. A nonzero scalar kernel really has arbitrarily large matrix rank

**Discharged.** Fix u,d for which k(z)=<u,Q(z)d> is not identically zero.
For every N and every N distinct column locations y_1,...,y_N there are
distinct row locations x_1,...,x_N, avoiding the columns, such that
`[k(x_i-y_j)]` is invertible. The rows may be selected in any prescribed
nonempty open set avoiding the columns.

Proof. k is a homogeneous rational function of degree -4: its denominator
is pi^2 |z|^6 and its numerator is a quadratic polynomial. Suppose
`sum_j c_j k(x-y_j)=0` on a nonempty open set away from the y_j. Multiply
by the product of the denominators. A polynomial vanishing on an open set
vanishes identically (apply the one-variable statement successively to an
open rectangular subset). The rational identity therefore holds everywhere
away from the y_j. Choose a unit n with k(n)!=0 and let x=y_j+epsilon n.
The j-th term equals `c_j epsilon^(-4) k(n)`; all other terms remain bounded.
Multiplying by epsilon^4 and taking epsilon to zero gives c_j=0. Thus the
N translated functions are linearly independent even on the prescribed
open set. Their evaluation vectors span R^N; otherwise a nonzero vector
orthogonal to that span would give a linear dependence. Selecting a basis
of evaluation vectors gives the desired matrix and distinct rows. []

This elementary pole argument replaces the source's appeal to the theorem
on translation-invariant finite-rank kernels. It supplies neither the
finite-color grid theorem nor a uniform lower bound on the seventh singular
value for cell-dependent images or growing gauge bounds.

## Remaining conditions

- **Discharged counterexample in the subsequent `rank-u-staggered-limit.md`:**
  the proposed quantitatively positive coupling over all bounded gauges and
  their limiting subspaces is false. Pointwise compatibility is still open.
- **Gap:** control the level-j error relative to the seventh singular value
  of the selected leading matrix as the geometry and gauge bound grow.
- **Unchecked:** no numerical runner from `checks/rank-u/` was run in this
  session. The proofs above do not depend on such a run.
