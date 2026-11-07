# Deep marks: stopping algebra and the missing local inequality

Own derivation, 2026-11-01, at `ae6bb189621a8f54d84347c84c59de476152eda4`.
Mapped side only. Author check, not independent review or audit. Companion:
`../parts/hard-core--dm.md`. No numerical computation is used.

**Status.** The cancellation lemma, the graph sum, the corrected column count,
and the conditional implication below are **discharged as mathematical
lemmas under their displayed hypotheses**. The lattice stopping package (S)
and the localized marked-kernel inequality (LMK) are **gap**. In particular,
this note does not prove DM for the SU(2) measure.

## 1. Quantifiers and a replacement budget

Fix the geometry first: L, the brick tiling, t_0, r_c, d_x, the locality and
clearance radii, T, eps_q, and the constants of the allowed flow. Constants
below may depend on these, but not on the finite terminal level K, torus,
region, mark set, or data. Assume, for fixed B_0, B_1, b'>0,

    |x_(k+1)-x_k| <= B_0,
    x_r <= x_k+B_1                       (k <= r <= K),
    x_k >= x_K/2 + (K-k)b',              x_K >= x_*.

The first two are the bounded-step/envelope conditions used in the pinned
draft. There must exist one x_*, chosen after geometry and these constants,
such that the following claims hold for **every** K and allowed flow, every
0<=i<K, every allowed finite free region Omega, every compatible quiet datum
d, every parent V class (flux <=T_2) on the required parent patches, and every
finite allowed mark set M at levels <=i. Compatibility includes a positive
denominator and admissible frozen bonds; marks have the draft's two-brick
clearance. Any use at a selected stop must have these universal quantifiers
available before selecting its data.

Keep the draft's gains: g_b=(3/8)x_k c_S eps_q^2 T^2 for a type-I mark
at k, and g_b=(1/8)x_k c_T T^2 for type II. Put G(M)=sum_(b in M) g_b,
M_<i={b:lev(b)<i}, and M_i={b:lev(b)=i}.
Specify the previously ambiguous cell convention: a type-I
brick contributes **all** its support cells at birth, and a type-II mark
contributes its cell. Let s_0 bound the number of support cells per mark,
uniformly in the volume. At level k, C_k(M) is the union of the ancestors of
these cells from marks born by k. Use the draft's range-r_c clusters,
K_0=4*3^4, and counts a_k (cells in clusters larger than K_0), s_k (other
clusters). These are sets of cells, not multiplicities.

For constants C_E,C_e,c_e>0 to be chosen independently of K, define

    bar x_k = max_(k<=r<=K) x_r,
    w_k = C_E log(e+bar x_k),
    epsilon_k = C_e exp(-c_e x_k eps_q^2 T^2),
    P_i(M_<i) = sum_(k<i) [w_k a_k(M)+epsilon_k s_k(M)]
                  + sum_(b in M_<i) w_(lev b).

Here the M in the first sum can equivalently be M_<i. Set P_0=0. This is a
replacement for Psi, allowing fixed geometric multiplicities and a monotone
logarithmic envelope. It does not assert the printed coefficient 3N_c.

The proposed replacement is

    Q_i(Omega,d,V;M) <= exp[-G(M)+P_(i+1)(M)]                 (DM+)
                      <= product_(b in M) z_b,

with the **same** z_b as DM: exp[-x_k c_S eps_q^2 T^2/4] for type I and
exp[-x_k c_T T^2/16] for type II, after increasing x_* by a fixed amount.
DM+ remains a gap for the lattice measure. Sections 2-5 prove an exact
conditional reduction to (S),(LMK), not those hypotheses.
For M empty, Q_i=1 by its definition and no exploration is needed.

## 2. Lemma C: cancellation at a fixed enlarged support

**Discharged, given the stated positive disintegration.** Let N be a marked
mass, 0<D<infinity its unmarked mass with the same parent. Suppose N<=sum_h N_h and,
for each h separately,

    N_h = sum_sigma integral O_h(sigma,d) I_h^N(sigma,d) dd,
    D  >= sum_sigma integral O_h(sigma,d) I_h^D(sigma,d) dd,

where the factors are nonnegative and I_h^D>0 wherever needed. Then

    N/D <= sum_h ess sup_(sigma,d) I_h^N/I_h^D.              (C)

Proof: if R_h is that supremum, N_h<=R_h D by multiplying the pointwise
inequality by O_h and integrating. Sum in h. There is no claim that the
denominator pieces for different h are disjoint. Zero denominator pieces
must also have zero numerator, or the hypothesis fails.

For the level-i application, Sigma includes a layer **at level i** and all
required lower layers. For a fixed enlarged support B, its exterior stop
event must be measurable on and outside Sigma. The interior certificates
are retained in I_h^N, not hidden in O_h. The common exterior includes all
remote rough configurations. This is the factorization needed to invoke C;
its geometric implementation for this proposed repair is part of (S).

An adaptive *minimal* B selected by certificates inside B cannot simply be
put in O_h: its event can read the interior. Cover by fixed B and retain the
certificates in the numerator instead. Consequently the sum in (C) is real
and must be paid. Conditioning on a chosen stop is not itself a rarity proof.

**Implication, exact class branch.** For i>=1, if M_i is empty, on W class the
definition of the effective densities on the same fibre gives

    exp[-F_i^(M_<i,d)(W)+F_i^d(W)] = Q_(i-1)(Omega^-,d^-,W;M_<i),

where Omega^-,d^- are the inherited lower-level region and data.

Assuming DM+_(i-1), multiply its uniform bound by exp[-F_i^d(W)] and
integrate over W class. Dividing by the full unmarked denominator gives

    N_class/D <= exp[-G(M)+P_i(M)] * Prob(W class)
              <= exp[-G(M)+P_i(M)].

This establishes the coefficient one for this branch. It uses no reference
ball, certificate sum, or bound on the free bonds of Omega. A non-class W
does not satisfy the hypothesis and is not covered by this calculation.

## 3. Lemma A: entropy of extensions attached to a seed

**Discharged.** Let a finite graph have degree at most D_0>=2, and let A be a
set of seed vertices. Sum u^|Y| over sets Y disjoint from A such that every
connected component of Y has an edge to A. For 0<=D_0^2 u<1,

    sum_Y u^|Y| <= exp[D_0 |A| D_0^2 u/(1-D_0^2 u)].        (A)

Proof. Give each component a canonical first edge from A to that component.
Different components have different first edges. There are at most D_0|A|
possible edges. The number of connected m-vertex sets containing a specified
vertex is at most D_0^(2m): choose a canonical spanning tree, and traverse it
depth first. Construct that tree by repeatedly attaching the first
undiscovered adjacent vertex to the reached set; connectivity ensures this
reaches every vertex, and adding a new vertex creates no cycle. The traversal
uses each of its m-1 edges twice. Its walk determines the set and has at most
D_0^(2m-2) choices. Allowing independent choices at all possible first edges
overcounts the compatible, disjoint components. Therefore the sum is at most

    [1 + sum_(m>=1) (D_0^2 u)^m]^(D_0|A|),

which is bounded as claimed by 1+t<=exp(t).

Finitely many decorations per added vertex can be included by replacing u
by their number times u. Multiple histories with one support need the same
bound; a bound on supports alone does not count histories automatically.

Two exact stress tests:

- For N disjoint seed-to-optional-vertex edges the sum is (1+u)^N. Thus
  “at most 2” independent of the number of marks is false for every u>0.
- If unanchored remote vertices are retained, an edgeless collection of R
  such vertices gives (1+u)^R. One epsilon per marked cluster cannot pay it.

These are counterexamples to proposed **entropy bounds**, not to Yang-Mills
rarity. Exterior cancellation is what removes the second collection.

## 4. The exact local obligation

**Gap (S), the stopped representation.** For every tuple in section 1 there
must be a positive cover as in Lemma C with the following properties. The
seed A is a fixed-radius enlargement of C_i(M), with

    |A| <= C_A [a_i(M)+s_i(M)].

The fixed constant absorbs K_0 and brick volumes. Histories h are encoded by
extensions Y as in Lemma A, including their rough-pattern and certificate
decorations. All multiplicity is included in their activities. Empty h has
one code. Disconnected events outside the stopped components are integrated
in O_h. The actual level-i integration dimensions obey a local bound

    n_i(h) <= C_n [|A|+v_i(h)],                            (S-dim)

with v_i(h) the number of encoded added vertices. Components not joined by
an extension factor at the same frozen layers. No filled hull, enclosed
pocket, or whole torus can be counted as an added vertex of zero cost.
Witnesses that are reused or overlap must be assigned with a uniform
multiplicity bound. The terminal case B=Omega is included in these clauses.
Every retained mark must still denote its original event after the new data
are frozen. For the local-lift definition, sufficient clearance means the
new frozen bonds miss its defining patch; otherwise an event-inclusion
estimate with the changed threshold is additionally required.

Most importantly the zero-extension, class-field contribution on a small
cluster with M_i empty passes the lower marked probability with coefficient
at most one. It is not estimated by a denominator ball. An interior rough
pattern or a failed separator is a nonempty decorated extension, even when
its spatial support fits in the initial seed. One can reserve a bounded
number of attachment slots per seed cell for such internal decorations;
their graph degree and count must remain bounded. This is part of (S), not
a claim that the existing exploration has already produced the coding.

**Gap (LMK_i), localized marked-kernel inequality.** Choose constants
C_u,c_u>0 and u_i=C_u exp(-c_u x_i eps_q^2 T^2). For every fixed history h,
and all compatible quiet data on its stopped layers, require

    I_h^N/I_h^D
      <= exp[-G(M)+P_i(M_<i)
                    +(w_i/2)(a_i(M)+|M_i|)] u_i^v_i(h).   (LMK_i)

I_h^N contains the original marks, the certificate leaves at **all** their
levels, and the specified interior rough-pattern restrictions. I_h^D is the
unmarked integral on that same fibre and region. The inequality is required
for the positive masses before summing histories; no DM_i may be used to
bound the level-i certificate marks in its proof. For i=0, P_0=0 and the
integrals use the bare action. A same-level certificate gain here is a
restricted-integral energy estimate, not an invocation of the probability
theorem under proof.

This is stronger than saying that the stopped region is small. It includes
the full cost of certificate leaves, their entropy, the changes to the lower
mark budget, and any junction data. It is much more local than the original
DM: only the seeded components and their specified extensions are compared.
It is the missing estimate, not an established alternative name for DM.

### How one could prove LMK, and where this note stops

**Discharged elementary integral calculation.** On a component with n free
coordinates suppose, for a reference W^0 and an active restriction H,

    D_in >= exp[-F_i^d(W^0)] (c x_i^(-1/2))^n exp(-C_0 n),
    volume of the numerator fibre <= C_1^n,
    F_i^(M' union Y',d)(W)-F_i^d(W^0)
                         >= G(M)-P_i(M')+H_h-C_2 n
                                                    for every W in H.

Then directly integrating the third inequality and dividing by the first
gives

    N_in(H)/D_in <= exp[-G(M)+P_i(M')-H_h+C_3 n log(e+x_i)]. (B)

C_3 depends only on c,C_0,C_1,C_2. No estimate of the dimension by marks was
used in this calculation. Y' consists of lower certificate leaves; H keeps
the top marks, top certificate leaves and active-pattern restrictions.
For inactive class components, use the exact
common-fibre identity and DM_(i-1) instead; their factor has no n log x_i.

To turn (B) into LMK, the stopped geometry and **surplus** energy must give,
after allocating all original and certificate mark gains,

    H_h - C_3 n_active(h) log(e+x_i)
       >= c_u x_i eps_q^2 T^2 v_i(h) - v_i(h) log C_u
                       -(w_i/2)(a_i(M)+|M_i|).            (PAY_i)

This explicitly displays the missing inequality. In particular, certificate
non-quietness cannot be erased when applying the pointwise energy bound.
For leaves below i, their change to P_i and their witness-tree entropy have
to be subtracted before declaring H_h a surplus. Adding a leaf can merge
mark clusters at many levels, so bounding P_i(M' union Y)-P_i(M') by a sum
over Y without a separation proof is not permitted.

The pinned draft proposes using I_i, Z_i, W1, W2 and the class reference for
the third hypothesis of (B). This note does **not** derive that pointwise
hypothesis with the required uniform data, nor the certificate allocation
in PAY_i. S-dim alone fixes only the bond-count defect. These are the exact
places where the proposed level-i repair remains open.

**Implication, sufficient active-volume count.** A more useful target than
the count of all stopped coordinates is

    n_active(h) <= C_act [a_i(M)+|M_i|+v_i(h)].             (S-active)

It follows from the following explicit coding conditions: large seed
clusters contribute at most a fixed number of coordinates per support cell;
small clusters with a top mark contribute a bounded number per such mark;
every other small cluster that is integrated by (B) is attached to a
nonempty extension; at most D_0 such clusters attach to any extension
vertex; and all remaining active coordinates lie in a bounded enlargement
of those vertices. The third group then has at most D_0 v_i clusters, each
of bounded size K_0. Adding the four counts proves S-active. Whether the
lattice exploration has this coding, especially at old layers, is **gap**.

If in addition H_h>=chi x_i eps_q^2 T^2 v_i(h), chi>0, the active-volume
count implies PAY_i: choose w_i/2>=C_3 C_act log(e+x_i),
c_u=chi/2, C_u>=1, and x_* so
(chi/2)x_i eps_q^2 T^2>=C_3 C_act log(e+x_i).
Thus the missing physical task is to prove this **remaining** H_h after
the prescribed gains and lower-level losses, with bounded reuse of witness
leaves. It is not enough to show that an unconditioned brick is expensive.

**Implication, witness-tree arithmetic only.** If a leaf at level k has an
available weight tau_k=A exp(-h x_k), h>0, q>=2 children are required at a
promoted node, and at most N child choices are allowed, the sum of formal
tree weights obeys p_k<=tau_k+N p_(k-1)^q. From x_(k-1)>=x_k-B_0,

    N(2A)^q exp[-hq(x_k-B_0)] <= A exp[-h x_k]

holds once h(q-1)x_k >= log(N 2^q A^(q-1))+hqB_0. Induction then gives
p_k<=2tau_k, starting with p_0=tau_0. This sums **weights**, not probabilities;
it does not supply the joint leaf estimate in LMK. In the application h is
a fixed positive multiple of eps_q^2 T^2. Extra geometric multiplicity and
any power loss in selecting separated leaves must first be included in h,N.

## 5. The conditional theorem and its well-founded order

**Implication, proved.** Suppose S and LMK_i hold at every level, with their
constants uniform as quantified above. Then DM+ holds at every level.

Proof. Lemmas C and A yield

    Q_i <= exp[-G(M)+P_i(M_<i)+(w_i/2)(a_i+|M_i|)]
            * exp[eta_i (a_i+s_i)],
    eta_i = D_0 C_A D_0^2 u_i/(1-D_0^2 u_i).

Increase x_* so D_0^2 u_i<=1/2. Choose C_e,c_e so eta_i<=epsilon_i,
uniformly in i, and increase x_* again so epsilon_i<=w_i/2. The exponent is
at most -G(M)+P_i(M_<i)+w_i(a_i+|M_i|)+epsilon_i s_i, exactly DM+.

For deriving LMK rather than assuming it, a possible dependency order is

    classical uniform-data inputs,
    I_0 -> LMK_0 -> DM+_0,
    (all earlier I,Z,DM+) -> Z_i -> I_i -> LMK_i -> DM+_i.

Each LMK_i must be proved directly by localized integration, using DM+ only
at levels <i. No region or mark induction is then needed. The arrows into
Z_i and I_i are the **proposed** earlier closure, not proved in this note;
they must also tolerate the changed constants in P. For the probability
implication itself, S and LMK are the complete hypotheses. I,Z are a possible
route to them, not additional results certified here.

In particular, “given Z_i” does not mean “given Z_(i+1)”: applying the latter
with class top would prove DM immediately but its far components call DM_i.
That would be circular in the pinned construction.

## 6. Lemma F: the corrected, finite-depth column budget

**Discharged for the nested block geometry stated here.** Suppose parent
cells are the regular L-block quotient of the torus for all existing levels.
Choose N_c>=1 with L^(N_c-1)>=r_c and L>=8*3^4. For any nonnegative
nonincreasing weights w_k, continued constantly below 0,

    sum_(k=0)^i w_k a_k(M)
       <= 3 N_c s_0 sum_(b in M) w_(max(0,lev(b)-N_c)).     (F)

Proof. Give every support cell of every mark a separate birth token. Tokens
at the same cell can merge at birth; subsequently each occupied cell has
its unique parent. Include new tokens when their birth level arrives. This
gives a forest with at most s_0|M| leaves.

For a range-r_c cluster of k>K_0 cells at a starting level j, a spanning
tree can be traversed in length <=2kr_c in level-j's cell metric. At N_c
levels up, let n be the number of its
ancestor cells. Colour the coarse torus with at most 3^4 colours so cells
of one colour are non-adjacent: a cycle needs at most three colours, and
use the product colouring. To colour a cycle, alternate two colours for
even length; for odd length alternate on the first n-1 vertices and give
the last a third colour (lengths one and two are immediate). Two distinct
cells of one product colour have an intervening coarse cell in at least
one coordinate. Their points are thus separated by at least L^N_c in the
finer metric. Selecting one point
from each such ancestor on the tree walk therefore gives

    n <= 3^4(1+2kr_c/L^N_c) <= 3^4(1+2k/L) <= k/2.

For each starting level j with j+N_c<=i, let d_j count all forest merges in
(j,j+N_c], with p incoming branches counted as p-1 merges. The drop in the
number of distinct ancestors of the large clusters implies a_j<=2d_j.
Indeed the sum of their separate ancestor counts is at least the count of
their union, so cross-cluster mergers do not invalidate this inequality.
Births add branches and cannot reduce the number of required mergers.

A merge at level v occurs in at most N_c intervals and their weights are
at most w_(max(0,v-N_c)). Order children at every vertex. Assign one merge
to the first-child leaf in each non-first child subtree. These assigned
leaves are distinct, and their birth levels b satisfy b<=v. Hence each
assigned weight is at most w_(max(0,b-N_c)). This proves the bound with
2N_c for starting levels having N_c successors.

There are at most N_c remaining starting levels at the top. At each of
them a_j<=number of tokens born by j. Charging each cell to any descendant
token, each token is used at most once per level; monotonicity gives a total
at most N_c sum_tokens w_(birth). This proves (F), including terminal
clusters that never merge. No artificial levels beyond the finite torus
were introduced.

For small clusters choose one descendant token per cluster. A token is used
at most once at any level. Therefore, if E=sum_(k=0)^K epsilon_k,

    sum_(k=0)^i epsilon_k s_k(M) <= s_0 E |M|.

The flow gives, by the finite geometric series,

    E <= C_e exp[-c_e eps_q^2 T^2 x_K/2]
                /[1-exp(-c_e eps_q^2 T^2 b')].

Choose x_* so E<=1. Since w_(max(0,b-N_c))
<=C_E log(e+x_b+N_c B_0+B_1), (F) and the explicit birth costs give

    P_(i+1)(M) <= sum_(b in M)
        [(3N_c s_0+1) C_E log(e+x_b+N_c B_0+B_1)+s_0].     (F+)

For fixed constants, this is <=sum_b (g_b+log z_b) when x_* is large enough:
the right side allowed per mark is x_b c_S eps_q^2 T^2/8 for type I and
x_b c_T T^2/16 for type II, whereas (F+) is logarithmic. This proves the
second inequality of DM+ **conditional on its first**. Fixed support-cell
multiplicity and the finite top boundary cost no depth factor.

## 7. Tests of the proposed repair and of inner inductions

**Discharged tests of the bookkeeping; lattice realization still gap.**

1. A long thin rough set with m cells requires a tube of O(m) cells at fixed
   d_x,t_0, including one that winds around a torus. Its reference-ball cost
   is C m log x_i, not O(log x_i). If available surplus is c x_i T^2 m,
   the inequality c x_i T^2/2 >= C log(e+x_i)+log D_0^2 pays each cell and
   the graph entropy. One rare factor for the entire component does not.
   If only a thin boundary is certified while an uncontrolled volume is
   integrated, S-dim/PAY fails. Keep thick pockets in the common exterior.
2. N separated small seed clusters have N root factors. Lemma A pays their
   sum by exp(C u_i N), and the flow sums this loss over levels per birth
   token. Thus many marks are allowed. A single global 1+epsilon_i or 2 is
   not enough, and applying independent probabilities without conditional
   factorization is not an alternative proof.
3. Induction on |M| alone fails as a proposed order: a failure adds Y and
   asks about M union Y, not fewer marks. Conditioning successively on the
   other non-quiet marks supplies rough information, not an admissible quiet
   boundary datum of DM.
4. Induction on free top bonds n is a legitimate **possible** order if every
   recursive component has strictly fewer than n bonds, with all mark sets
   quantified at that n. But the terminal B=Omega has no new separator and
   need not decrease n. It needs a direct estimate such as LMK. A long thin
   certificate may have arbitrarily many bricks; it is not a bounded base
   case. Dense separated marks can already fill the initial seed region.
5. Even proper-region induction does not itself close a uniform constant.
   An estimate f(n)<=(1+u) max_(m<n)f(m), f(1)=1, allows
   f(n)=(1+u)^(n-1). Reusing an epsilon slack at every same-level spatial
   recursion can accumulate with volume. The flow only sums different
   **levels**. One needs denominator weights yielding a contraction, a
   strengthened budget with proved consumption, or the direct LMK route.

Thus the lead's circularity concern is real for the suggested use of DM_i
on its own certificates. It is not a proof of unavoidable circularity:
sections 4-5 specify an acyclic route, conditional on a new local estimate.

## 8. The reference threshold

**Gap, inherited and not solved here.** The direct route through Z_i compares
W with W^# on tube{flux(W)>T_2}, retaining all prescribed bonds, and then
uses I_i on W^#. It needs

    inf_(W^#=W on prescribed bonds) max_p theta_p(W^#) <= T_2,

the (EXT=) of `../parts/hard-core--fill.md:119-168`. The stopping algebra and
graph lemmas use no reference field. The proposed physical proof of LMK via
the pinned Z/OW uses exactly the same threshold T_2, not C_a T_2. Applying
the multiplicative fill at T is invalid when the retained field is only
known to have flux <=T_2. Expanding the filled set to {flux>T} would change
the class branch and its empty-excursion factor, so would require new proofs.

The uniform-data W1,W2,(CI-N)^d, stability at nested junctions and the
modified-energy exchange (LNC) are likewise inherited gaps for that route.
Nothing in the positive-integral algebra supplies them.
