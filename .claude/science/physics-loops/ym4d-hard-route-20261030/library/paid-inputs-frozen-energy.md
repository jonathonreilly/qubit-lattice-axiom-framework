# Frozen action in the paid energy comparison

Author: openai/gpt-6-astra/max, mac-mini-codex. Pinned source:
`b58dac27c53adb17f47520c8ca2f784014a8dcbe`.
Author mathematics, not an audit or independent review. No computation
or numerical experiment was run.

## 1. The scope of the obstruction

**Discharged (necessary condition).** Let

    a_d(V) = inf { A(W) : W has a regular chain to V with data d }.

Suppose U attains this infimum and V is class. The paid convention is
P(V)=V, N_ref(V)=empty. Hence the proposed comparison

    a_d(P(V)) <= A(U) - A^{Z_{i-1}(U)}(U)/16
                              + C_W T^2 |N_ref(V)|          (E1)

would imply A^{Z_{i-1}(U)}(U)=0. Positivity of the Wilson action is all
that is used here. In particular (E1) cannot subtract positive action
that is fixed identically on the constrained fibre.

**Scope.** This note tests the untrimmed Z in
`relative-density-bound.md:235,281-285`: level-(i-1) cells whose fine
action, on their specified enlargement, exceeds kappa T^2. The paid
proposal imports that Z unchanged in `threshold-paid-reference.md`,
section 3. The displayed definition of a_d in
`quiet-boundary-rarity.md:53` is the infimum of A(U), with the data held
fixed. No exclusion of frozen plaquettes or frozen coarse cells is in
these definitions. Under that literal convention, the construction
below refutes (E1).

If a consumer instead means only active cells and the action in the
portion left free by the layers, that is a different assertion. The
construction below does not refute that assertion. Merely subtracting
a common frozen-action constant from both A and a_d does not repair
(E1) while leaving A^Z untrimmed.

## 2. An exact small field with identity parent

**Discharged.** Take odd L>=5. Inside one parent block centered at z,
put all fine links equal to 1 except the two positively oriented
direction-1 links with initial vertices

    z+(0,1,0,0),       z+(0,-1,0,0).

Give them values exp(i a sigma_3) and exp(-i a sigma_3), respectively.
Here a>0 is smaller than T/8 and pi/16. All plaquettes are in the same
abelian subgroup. Each nonidentity link belongs to six plaquettes in
d=4; the two links share no plaquette. Thus exactly twelve plaquettes
have angle a, and all others have angle zero. The action of this field
is

    e(a) = 12 (1-cos a) > 0,                                (E2)

with normalized fundamental trace; another fixed Wilson normalization
only multiplies e(a) by a positive constant.

The deterministic, all-lines parent is exactly the identity, not just
identity to first order. To see this, write H for the real abelian
link angle. On this field every logarithm in the average is on its
principal branch, so the abelian block map is the exact linear formula
from the mapped Text 3.1,

    QH = Q_path H + Phi(y)-Phi(y').                         (E3)

Commutativity makes a product's angle the sum of the link angles;
the smallness of a prevents reduction modulo 2pi. For direction 1,
every straight line at transverse coordinate z_2+1 is paired with
the line at z_2-1 with identical longitudinal weight and opposite
angle. Thus Q_path H=0. Other directions have H_mu=0, so their straight
parts vanish as well.

For Phi(z), reflect a contour and its endpoint in x_2=z_2. The family
of shortest axial contours used by the average is invariant under this
reflection, and its direction-1 link sum changes sign. Therefore
Phi(z)=0. The same cancellation holds for each fixed axial order.
Contours inside other blocks meet no nonidentity link, so Phi=0 at
their centers too. This proves (E3) is zero on every parent bond.
The actual smooth-mixture kernel has all labels zero, since every
plaquette angle is below T. It therefore uses precisely this
deterministic average, with no excluded lines or Haar parents.

Several copies can be put in distinct, separated parent blocks. Each
parent path reads two blocks, so its angles remain within 4a<pi.
Equation (E3) is still exact and linear, and every parent is 1. At all
subsequent levels the fields are identically 1.

## 3. Quiet frozen copies are exact constrained minimizers

**Discharged.** Put one such copy well inside each of some frozen
fine-level bricks, with every incident plaquette wholly in that brick.
This is possible since a brick contains whole parent blocks and
t_0>=8L. Separate the copies so their plaquette supports are disjoint.
Freeze all links with both endpoints in the frozen site set, as the
source prescribes. Every nonzero-action plaquette then has all four
links frozen.

For a fixed brick, the curvature of the local free-edge lift with
identity parents is zero: identity is an admissible zero-action field.
The tree gauge does not change the curvature angles of our abelian
field. Its Dev is m_D a^2, where m_D is the positive, finite incidence
count in the source's cell convention. With individual plaquettes
counted once m_D=12; counting a plaquette in its incident cells changes
this only by a dimensional factor. Choose a>0 so

    m_D a^2 <= eps_q^2 T^2,    a<T/8,    a<pi/16.            (E4)

This proves the data quiet, without a stability theorem. When eps_q
is sufficiently small, equality in the first inequality is possible:
the example can be at the quiet limit. Strictly smaller a works for
every positive eps_q, so saturation is not needed for the obstruction.
At levels >=1 the data and the lifts are identity and their Dev is zero.
Adding the bricks one at a time gives the same conclusion for the
relative quiet test: already frozen copies have no response outside
their fixed plaquettes, and identity on the new brick still minimizes
the remaining nonnegative action. Gauge-related flat minimizers have
the same zero curvature, which is all the test reads.

Let U be this field, identity elsewhere, with its identity chain above
level 0. For any other field with the same frozen data, the action of
these twelve plaquettes per copy is unchanged, and every other
plaquette has nonnegative action. U makes all those other plaquettes
identity. Consequently, for M copies,

    A(U) = M e(a) = a_d(1).                                (E5)

The infimum is attained by this explicit U; no existence or uniqueness
theorem for general constrained minimizers is used. All chain levels
are below T. The field is also globally below 2T, including every
closed-face plaquette in the mesh repair of the companion note.

## 4. Admissible nested layers and arbitrary fine action under one cell

**Discharged (geometry and packing).** The copies can be put on the
layers in the source, rather than on isolated frozen bonds or a thin
strip inside a block. Use the x_4 direction of BG, where its layers
have unshifted, parallel brick faces, and work on a large compatible
periodic torus. Use a wide free slab and its exterior E_j at each
level. The two faces can be treated separately, far apart. At one face
write the exterior as x_4>=h_j, with h_j a brick-wall coordinate.
Choose, recursively downward, a wall h_j in

    [ L h_{j+1}-9t_0, L h_{j+1}-8t_0 ].                    (E6)

Such a wall exists because successive x_4 walls are t_0 apart. Shadow
under the site-centered block map multiplies the geometric wall
coordinate by L. Thus E_j includes the 3t_0 neighborhood of the shadow
of E_{j+1}, with room for the brick rounding. Every added exterior
brick is within at most 10t_0 of that shadow. For fixed sufficiently
large L, for example L>=60, this is below R_B=(2/3)t_0 L.
These are (N) and (B). The opposite face uses the opposite displacement.
Start with a slab wide enough that the faces never meet.

Use the prescribed Sigma(E_j) as the frozen layers. They contain a
full row of x_4 bricks, and all their sites are unions of whole parent
blocks. Their thickness is at most a fixed multiple of t_0; the exact
open/closed endpoint convention does not affect the margins in (E6).
The parent of Sigma_j lies in Sigma_{j+1}: its distance from h_{j+1}
is at most 12t_0/L<t_0. The free parents are on the other side of the
full next-level frozen row. Their shadow ends no later than
L h_{j+1}-L t_0+2L, allowing an endpoint/block rounding margin, whereas
Sigma_j starts no earlier than L h_{j+1}-11t_0. The clearance is thus
at least t_0(L-11)-2L >= t_0 L/2 for L>=60 and t_0>=8L. This is more
than r_S L, since the source chooses t_0>=4r_S. Extend the family
through level i and put identity data on its top frozen bonds as well.

At level h=i-1 a cell has fine side S=L^h. A flat fine frozen layer
has a row of fine bricks of thickness t_0 and arbitrarily large
transverse extent. Once S is large against t_0, a level-h cell meeting
this row contains, or its stated support enlargement contains, at
least c (S/t_0)^3 disjoint fine bricks away from transverse edges, with
c>0 dimensional. One elementary proof is to discard a t_0 boundary
strip in each of the three transverse coordinates and count disjoint
intervals of length t_0; the BG shifts translate their starting points
but not their spacing. If the row crosses a normal cell boundary,
one side has at least t_0/2 thickness and still contains an interior
parent block for a copy. Choose the copies there, so their nonzero
plaquettes lie inside the un-enlarged level-h cell c itself. There is
no reliance on whether A^Z includes the enlargement.

This c is in the frozen coarse band, by the parent containment just
proved. That fact is essential to the scope of the counterexample.
For any fixed L,T,t_0,eps_q,kappa and a chosen as in (E4), increase h
until enough copies fit to give

    M e(a) > kappa T^2.                                    (E7)

The ambient torus can be chosen to have side a sufficiently large
multiple of 8t_0 L^i. This is compatible with every level's brick
periodicity and leaves ample space between the slab's faces. All
geometric constants are fixed before h and the volume are increased.
Only put copies in this selected patch of the fine frozen layer;
all other frozen and free links remain identity.

The chosen c belongs to the untrimmed Z_{i-1}(U). Moreover its fine
action is positive, so A^{Z_{i-1}(U)}(U)>0. Equations (E5) and (E1),
with V_i=1 and N_ref=empty, would give

    M e(a) <= M e(a) - A^{Z_{i-1}(U)}(U)/16,

which is false. This works at any fixed admissible odd L by taking enough
depth and volume. No value of C_W, even one depending on L or depth,
can rescue a zero-support error term. x never enters the example.

## 5. What a repaired assertion must still prove

**Gap.** A possible repair restricts Z and its energy gain to the
active portion of the hierarchy, or uses an excess relative to the
frozen-data minimizer. The literal all-cells Z cannot be retained.
Such a repair must reprove the restricted TE allocation used in W2;
there is no claim here that changing the symbol alone suffices. Simply
discarding every frozen coarse cell can also discard free descendants
below its fixed parent, whose rough-cell gains still need allocation.

**Gap (QT^d, a precise local estimate in the source's proposed proof).**
Even with that repair, `quiet-boundary-rarity.md:203` needs a target
W^d respecting the already frozen data and parents, for which, on every
descent cube of radius r<=r_* in level-(i-1) units,

    E_Q(W^d) <= C_Q T^2 [ eps_q^2 + b_2^2 (r/L)^4 ],
    b_2=T_2/T,                                             (QT^d)

on the portion whose action the descent may change. C_Q and r_* must
be independent of x,L,depth,volume and the number/order of stops;
b_2 is the fixed absolute threshold ratio. The condition for a
positive small-cube gain is, for example,

    C_f C_Q [ eps_q^2 + b_2^2 (r_*/L)^4 ] <= kappa/4.       (E8)

A global O(T^2) bound per parent block does not give (QT^d). The first
term must stay small at the quiet limit, at multi-brick junctions, and
after arbitrarily many successive freezes. The preceding counterexample
also shows why E_Q cannot indiscriminately include all deeper frozen
plaquettes.

**Gap (preserving the data during gluing).** The current RF statement
only matches the two sides of a band, up to a gauge on its inner side.
The frozen version needed here must additionally preserve the exact
fixed links on every intersection with that band and restore parents,
with a cost bounded by C_f times shell energy plus target energy,
and with the bump cost absorbable in the gain (E8). An unrestricted
site gauge on a frozen component is not equality to its prescribed
links. These are not supplied hypotheses of RF at lines 117-137.

Neither this fixed-link RF estimate nor (QT^d) is derived here. The
companion response note states a concrete sufficient estimate for the
junction part, and proves only its summation implication. This does
not assert that the active-energy repair is false, or that no other
proof of it exists.
