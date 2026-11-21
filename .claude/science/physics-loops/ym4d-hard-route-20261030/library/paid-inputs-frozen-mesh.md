# Frozen site blocks and the vertex mesh

Author: openai/gpt-6-astra/max, mac-mini-codex. Source:
`b58dac27c53adb17f47520c8ca2f784014a8dcbe`.
Author mathematics, not an audit or independent review. No numerics.

## 1. The actual frozen bonds

**Discharged (failure of the literal hypothesis FG).** Work in units of
the level being filled. For odd L write R=(L-1)/2. The site-centered
block is

    B_z = Lz + {-R,...,R}^4.

This is the convention of the mapped block average (Text 3.1), made
explicit in `../checks/hard-core--mapped_contour_gradient.py:21-22`.
The coordinates and mixture kernel are Text 5.1-5.2. The frozen/free
rule is explicit in `fibre-propagator.md:118` and
`quiet-boundary-rarity.md:225`: a bond is free if at least one endpoint
is in a free block. Thus, if S is the set of frozen sites, the frozen
bonds are

    F(S) = {[x,x+e_mu] : x and x+e_mu are in S}.              (G1)

This includes bonds between two different frozen bricks. The source
check `hard-core--mapped_sharp_two.py:204-210` uses the same rule;
that code was read, not run.

A geometric site brick has the form

    B = product_j [a_j-1/2, a_j+t_0-1/2],   a_j integers,
    S_B = product_j {a_j,...,a_j+t_0-1}.

In Lemma BG the offsets between walls are multiples of t_0/8, with
t_0 a multiple of 8L. The common offset from the vertex lattice is
still half-integral. No common *integer* translation puts these walls
through lattice vertices, as FG requires.

Moreover, take two frozen bricks sharing a facet and choose an integer
point away from the edges of that facet. The normal link across the
facet has endpoints at a-1 and a, while the separating wall is a-1/2.
Both endpoints are frozen, so (G1) freezes the link; neither closed
brick contains the entire link. A facet contains such points since its
side lengths are at least t_0/8 >= L. These two failures are geometric,
even when the field is identically 1. They do not disprove existence of
a fill preserving the actual data.

## 2. A local sufficient repair, with its extra regularity explicit

**Discharged (geometry).** Leave the site blocks, the block map, the
tree roots and (G1) unchanged. For purposes of filling only, translate
the auxiliary brick tiling by (1/2,1/2,1/2,1/2):

    B^v = B + (1/2) 1 = product_j [a_j,a_j+t_0].             (G2)

These are lattice-vertex rectangles, with the same t_0 and recursive
offsets as BG. Every frozen bond is contained in B^v for the original
frozen brick containing its positively oriented initial endpoint x:
all coordinates of x lie in [a_j,a_j+t_0-1], and adding e_mu stays in
B^v. This also proves the assertion at a junction, without a bound on
the number of incident bricks. The half-unit displacement is the
smallest possible displacement in each coordinate that turns a
half-integral wall into a vertex wall. No claim of a globally minimal
repair among arbitrary fill algorithms is made.

**Gap (extra face data).** Translating the mesh alone does not prove the
regularity needed by the frozen-brick clause. Its precise additional
test is

    theta_p(V) <= t for every fine plaquette p contained in B^v,
    for each original frozen brick B.                       (G3)

For the paid reference t=2T. If the current meaning of quiet on a brick
already includes all these closed-face plaquettes, no extra field
hypothesis is needed. The site-centered convention and the displayed
Dev_b definition do not explicitly establish this. In particular a
plaquette in an exposed upper face of B^v can have all its vertices
outside S_B. Such links were not frozen by (G1).

A precise convention change is to certify (G3) when a brick is frozen,
in addition to the existing quiet test. Only the plaquettes not already
certified by that test need adding. They are in a one-fine-cell collar
of the original brick. Alternatively define the quiet test on this
closed vertex brick and prove its lift bound there. Neither alternative
is silently asserted to follow from Dev_b^d, particularly at nested
junctions. Deleting crossing bonds from (G1) is unnecessary and would
change the conditioned problem.

**Implication (fill under exactly G3 and the supplied Theorem S).** Fix
t, n=ceil(sqrt(16pi/t)), and t_0 in 8L Z with t_0>=8n. All coordinates
of walls of B^v lie in a common integer translate of (t_0/8)Z. Put
m=t_0/8. Divide every interval of length m into q=floor(m/n) integer
subintervals, distributing the remainder among them. Each resulting
length is at least n and at most 2n: m/q < n+n/q <=2n, and rounding
up cannot exceed the integer 2n. Repeat this fixed subdivision in each
coordinate. It gives a global rectangular vertex mesh refining every
B^v, independent of the frozen mask. Ambient periods and prescribed
outer faces must be compatible with this mesh, as in the original FG.

Select every mesh 4-cell containing a plaquette above t. By (G3), no
mesh cell inside a frozen B^v is selected. Prescribe V on all unselected
cells and their faces. Every frozen bond belongs to one such B^v by
(G2), hence belongs to the prescribed subcomplex. Apply Theorem S of
`fill-cubical-extension.md` on the entire mesh. Its extension fixes
every frozen bond, including crossing bonds between frozen bricks,
and gives the same flux bound A_f t as F2-mult. Any changed link lies
in a selected cell of l^1 diameter at most 8n containing a rough
plaquette. The support and Borel-selector conclusions are therefore
exactly the original ones. A selected cell on the other side of a
prescribed face cannot change the face's links. This proves the
implication without using BG's local half-ball assertion.

The construction of the mesh and the containment argument are proved
here; the analytic extension theorem S is an inherited, independently
unchecked input. This is a same-level fill. It does not preserve extra
blocking constraints automatically.

## 3. Constants and disposition

**Discharged.** The displacement 1/2, collar width 1, dimensional
incidences and support multiplier 8 are absolute, free of x, L, depth
and volume. The inherited A_f depends only on the fill theorem's fixed
numerical constants and dimension. The integer n depends on T, and
t_0 is chosen after T and L; these lengths are free of x, depth and
volume. Rounding t_0 upward to a multiple of 8L meeting t_0>=8n is a
one-time choice. The proof never uses the number of frozen components.

**Gap.** For the unchanged site-centered convention, literal FG is
false. The auxiliary vertex-brick repair is proved under the explicit
closed-face regularity test (G3). Its automatic availability for the
draft's current notion of nested quiet data has not been proved. No
consumer or convention has been edited.
