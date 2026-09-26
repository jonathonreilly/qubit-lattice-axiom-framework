# A metric-compatible noisy pointer still fails the exact routed rate law

2026-09-22. Exact author certificate, independent check pending. Raw research
only: no completed no-go publication packet or audit status is claimed.

## Scope

Use the finite N=12 winding-matching torus, its fourteen colors, and the
full routed swap generator defined in
`DIMER_FIXED_ENCODING_QUANTUM_CONTRACTION.md`. Take k0=11/10, gamma=1.
Instead of that note's mixed four-qubit states, use an orthonormal pointer
basis of size m=14 and the commuting states

    rho_a = (1-eta)|a><a| + (eta/14) I14,       0 < eta < 1.

They are faithful to probabilities and full rank on their common support.
The pointer basis may be embedded in the six-qubit code of the companion
positive construction; unused orthogonal states do not affect the argument.
The preparation is a tensor product over the 864 black sites. The target
is exact intertwining of every joint classical law with a differentiable
quantum channel family at t=0. Arbitrary global channels are allowed.

The uniform one-site reference is I14/14. Its transverse metric has
u=7(1-eta)^2, v=7(1-eta)^2/4 and zero cross term. Hence u=4v. The long-wave
two-component metric obstruction examined for the earlier code is absent.
This note tests positivity of the full generator, not that one tangent.

## Why linear inversion fixes a transition probability

In the pointer basis the preparation matrix is

    B = r I + q 11^T,    r=1-eta, q=eta/14,
    B^-1 = (I-q 11^T)/r.

B is invertible. Product prepared states span the full diagonal matrix
space, even though their positive convex hull does not contain every pure
pointer state. Linearity of an exact quantum extension consequently fixes
its action on every pure pointer configuration. On this diagonal subspace
the required generator is

    L_required = B^tensor K L_class (B^-1)^tensor K.

For different configurations x,y, a positive differentiable quantum evolution
from |y><y| must have initial derivative of probability <x|rho(t)|x>
nonnegative. Thus one negative off-diagonal entry of L_required suffices to
exclude this specified extension. The argument uses positivity already;
complete positivity is a stronger requirement.

## A three-position witness in the full cubic generator

Take three consecutive positions on the delta=-e1 route:

    u0=(0,0,0), u1=(10,0,0), u2=(8,0,0).

Let b=B(-1,-1,-1), c=B(+1,-1,-1), and a=A(+e2). The input colors at these
positions are (b,c,a), the output colors are (a,b,c), and every other
position has the same arbitrary fixed pointer color in input and output.
All three displayed colors are different. For S=S_-e1, S_ab=S_ac=1/2.

Conjugation by the product B leaves the support of each local operator
inside its original stencil. Only a stencil containing all three changed
positions can contribute. Exact enumeration of all 4320 nonidentity routed
stencils on this torus finds exactly two: the route edges (u0,u1) and
(u1,u2). Other spatial directions cannot cancel the witness.

The constant-rate swaps change only two positions and commute with the
product B, so their contribution to this entry is zero. For a two-position
diagonal color interaction define

    K_S=(B tensor B) diag_(i,j)(S_ij) (B^-1 tensor B^-1).

The two relevant bias terms give exactly

    (L_required)_(x,y) = -(1/4)[(K_S)_(ab,ba)+(K_S)_(ac,ca)].

Here the diagonal loss terms have support on only two positions and also
give zero. This is a statement about the complete generator, not an extra
requirement on its individual quantum jump decomposition.

For different colors i,j, define
w^(i,j)_s=B_(i,s)(B^-1)_(s,j)=q/r[delta_(s,j)-r delta_(s,i)-q]. Since S has
zero row and column sums, is symmetric, and has zero diagonal,

    (K_S)_(ij,ji) = (w^(i,j))^T S w^(j,i)
                  = q^2(1+r^2) S_ij/r^2.

Therefore the exact full-generator entry is

    -eta^2 [1+(1-eta)^2] / [784 (1-eta)^2] < 0.

At eta=1/2 it is -5/3136. The author checker also obtains this value by an
independent algebraic expression: explicitly sum the full four-position
rate over all 14^4=38416 color configurations in each of the two stencils.
The two stencil contributions are both -5/6272 and their constant-rate
contributions are exactly zero. Integer arithmetic has a conservative
absolute sum bound 86818348781640000, below the signed int64 limit.

The symbolic pair calculation covers every eta in (0,1), and the exhaustive
local calculation checks the eta=1/2 specialization. The proof of local
support reduction connects those finite sums to the whole torus; no huge
joint matrix is constructed.

## Consequence, limits and controls

The specified product depolarized pointer family cannot exactly implement
the specified routed process through a positive quantum evolution. This
remains true for arbitrarily small positive eta. It is not a theorem about
all overlapping record codes, different rate laws, correlated preparations,
limited observables, finite-accuracy implementations, or the framework.

At eta=0 the orthogonal-pointer Lindblad construction is available. At eta=1
all prepared colors coincide and faithfulness is lost; the inverse argument
does not apply. At gamma=0 the color-dependent bias vanishes and random
unitary swaps implement the remaining transport for every eta. These are
physical changes in the target, not contradiction repairs inside it.

This supplies a second design check: matching one necessary information
metric is not sufficient for exact quantum dynamics. The positive block
construction and approximate or altered dynamics remain useful alternatives.
No assertion that a new axiom is required follows.

Reproduction: `python3 noisy_pointer_generator_check.py`. Full exact output,
the author command and timestamps, script identity and stderr are preserved.
The initial JSON serialization failure is archived separately and is not
counted as a completed run. The N1-N8 publication packet remains incomplete;
this note is a scoped raw calculation pending independent scrutiny.
