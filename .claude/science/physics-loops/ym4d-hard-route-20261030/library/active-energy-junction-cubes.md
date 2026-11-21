# Cube propagation for Lemma J

Author: openai/gpt-6-astra/max mac-mini-codex. Source pinned at
`105283f2c2a5a306a2aff46a47dfadb7a3b6ef0e`.
Author derivation, not an independent check or audit. No numerical run.
Credit: the brick tiling and response formulation are those of
`fibre-propagator.md`, Lemma BG, and `quiet-boundary-rarity.md`, Lemma J.
This note repairs their geometric implication; it supplies no analytic
response theorem and invokes no lemma from a paper.

Continuation at `25a86977f`, openai/gpt-6-astra/max macbook-codex:
**Unchecked author counterexample:** literal Resp, comparing the
finite free-edge local lift to the common global reference with no
additive term, fails already with no older frozen data. See
[`active-energy-response-tail.md`](active-energy-response-tail.md),
sections 1-4. The conditional geometry below remains valid. Section
5A records the corresponding implication for the corrected Resp+;
the analytic input remains a gap.

## 1. Precise scope

**Implication (statement).** Fix one lattice level, d=4, parent length L,
brick side t=t_0>=8L, and a compatible periodic tiling or its restriction
to a region. Freeze distinct bricks in any order. Assume (Resp), in
one fixed system of curvature frames relative to the same W_ref, with
constants C_r and rho>0 uniform over the preceding frozen data:

    ||Theta(Lift_b^d)-Theta(W_ref)||_Q^2
       <= C_r sum_{Q' in older bricks}
                   exp(-2 rho dist(Q,Q')/L) a(Q'),       (Resp)
    a(Q') = ||Theta(d)-Theta(W_ref)||_{Q'}^2.

Assume also that each brick's data at its freezing time obey
||Theta(d)-Theta(Lift_b^d)||_b^2 <= e := eps_q^2 T^2.
The norm is a sum over the assigned curvature entries of that brick.
Each entry is assigned once; a convention with a fixed incidence
multiplicity changes the constants by that multiplicity.

Use the axis-parallel cube partition of side h=t/1024, aligned with the
common grid of brick walls. Curvature entries can be assigned to these
half-open geometric cubes even when h is not an integer. Every cube
interior lies in one brick. Distance below is the l-infinity distance
between closed cubes; a response bound using Euclidean or lattice
path distance implies this weaker bound. Boundary entries are assigned
consistently to one adjacent brick and cube.

There are constants C_J and c_0 depending only on C_r,rho,d and this
fixed incidence convention such that, if t/L>=c_0,

    sup_Q a(Q) <= 2 C_J eps_q^2 T^2.                       (J-cubes)

They are free of x,L,volume,number/order of freezes and depth, PROVIDED
the input (Resp) has precisely that uniformity. This is a same-level
geometric implication, not a derivation of the response to data at
different levels. Such data may enter (Resp)'s background only if its
uniformity over them has been established separately.

## 2. Small boxes in the actual brick tiling

**Discharged (geometry).** After a common translation, the brick with
integer indices (m_1,m_2,m_3,m_4) has coordinate intervals of length t
starting at

    x_4/t = m_4,
    x_3/t = m_3 + m_4/2,
    x_2/t = m_2 + m_3/2 + m_4/4,
    x_1/t = m_1 + m_2/2 + m_3/4 + m_4/8.

This follows by substituting the layer shifts in BG, one dimension
at a time. All wall coordinates therefore belong to delta Z, with
delta=t/8=128h. The common translation includes the half-unit offset
if the site-centred convention is used; no frozen set is moved.

Here is a direct point-incidence proof of the property we need. In
dimension q, the walls in coordinate j of T_q lie in
t 2^{-(q-j)} Z. At a wall between two q-dimensional layers, the lower
(q-1)-dimensional tiling and its translate have disjoint wall-coordinate
sets in each of their coordinates: the translation is half that
coordinate's wall spacing. Inductively, a point lying on walls in k
distinct coordinate directions in a layer belongs to at most k+1
bricks in that layer. At an interface, the coordinate directions that
carry walls in the upper and lower patterns are disjoint. Adding their
two incidence bounds gives at most q+1. The one-dimensional base has
at most two intervals. Thus at most five closed bricks meet a point
in dimension four. This argument uses no assertion about balls.

If an axis-parallel box has width strictly less than delta in every
coordinate, all bricks meeting it contain one common point: in each
coordinate choose the unique delta-grid plane in that interval if
there is one, otherwise any interior coordinate. Every brick interval
meeting the small interval contains that chosen coordinate, since its
endpoints are delta-grid points. Taking the four chosen coordinates
gives the point. Therefore at most five bricks meet such a box.
The same statement holds in a lifted periodic chart.

## 3. Finite near propagation on cubes

**Discharged (geometry).** Change the printed cutoff t/40 to

    r=t/64=16h.

Draw an edge Q -> Q' when Q' belongs to a strictly older brick and
dist_infinity(Q,Q')<=r. Cube centres then differ by at most r+h in
each coordinate. A chain of six cubes has coordinate span, including
the cubes themselves, at most

    5r + 6h = 86h < 128h = delta.

Its six strictly ordered brick ages belong to six distinct bricks,
contradicting section 2. Thus there is no chain of five near edges.
Define the rank of a cube as one plus the longest outgoing near path.
Ranks lie in {1,...,5}, and every near predecessor has strictly smaller
rank. This is a rank on the actual cubes in (Resp), not on points that
may move within a cube. Equivalently the near matrix N satisfies N^5=0.

On a compatible torus a hypothetical path can be lifted successively
to the cover using the close representatives. Its total span above
is less than one brick side, so the same contradiction applies.

For each Q there are at most

    N_0 = (2(r/h+1)+1)^4 = 35^4

near cubes on the full grid. Restricting to older or frozen cubes
only decreases this count. Periodic distance gives no larger count:
choose one closest representative of each periodic cube.

## 4. The far row sum and absorption

**Discharged (summation).** Set alpha_0=1/128, so h/L>=alpha_0.
The number of cubes at centre displacement mh in l-infinity norm is
n_0=1 and n_m=(2m+1)^4-(2m-1)^4 for m>=1. Their set distance is
h(m-1)_+. Define the finite number

    S(rho) = sum_{m>=0} n_m exp[-rho alpha_0 (m-1)_+].

Convergence follows since n_m is a cubic polynomial and the
exponential has strictly negative rate. On the far part dist>r,

    sum_{Q' far} exp[-2 rho dist(Q,Q')/L]
       <= exp[-rho r/L] S(rho).                           (FAR)

The same bound on a torus follows by choosing closest representatives;
it is bounded by the full infinite-grid sum. It is uniform in volume
and the frozen subset. A single far entry bound without this sum would
not have sufficed.

**Implication (proved from Resp).** The triangle inequality squared
and relative quietness give, for each cube,

    a(Q) <= 2e + 2 C_r sum_{Q' older} w(Q,Q') a(Q').

Let A be the maximum over the finite frozen set, A_k the maximum over
rank<=k, and A_0=0. With

    B=2 C_r N_0,
    D=2 C_r S(rho) exp[-rho t/(64L)],
    P=1+B+B^2+B^3+B^4,

the rank property and (FAR) imply

    A_k <= 2e + B A_{k-1} + D A,
    A=A_5 <= P(2e+D A).

Choose t/L so that PD<=1/2, for example

    t/L >= max{8, (64/rho) log(max{1,4 C_r S(rho) P})}.

Then A<=4P e, which is (J-cubes) with C_J=2P. The factor four is
retained; the printed unrolling did not retain its absorption factor.
This value is for the stated aligned partition. If the conclusion's
supremum is instead over ALL translated cubes of side h, their assigned
entries lie in at most 2^4 partition cubes. Summing their nonnegative
energies gives sup a(Q)<=64P e; take C_J=32P for that convention.
This is a finite a priori estimate, with no fixed-point existence
argument required. The empty frozen set has A=0. Infinite-volume
uniform estimates, if needed, follow first for each finite history;
no existence of an infinite-history minimizer is asserted.

## 5. What remains open

**Gap.** The corrected Resp+ of the response-tail note: exact frozen
links, the relative-gauge l^2 estimate, an explicit local/global lift
tail, a regular nonlinear chart and a prefactor C_r uniform in L and
all earlier/nested data. The literal tail-free Resp has the author
counterexample identified above. F-D's graph inverse at an already
regular background does not prove the corrected input.

**Gap.** A simultaneous different-level response estimate needs its
scale weights and a depth-uniform row sum; see the explicitly
conditional (IR-nest) in `paid-inputs-junction-response.md`. This note
does not sum the same-level a(Q) over fine energy at all levels, nor
prove the frozen-data R3/bump used in the energy descent.

**Discharged/implication boundary.** The wall grid, point incidence,
near nilpotence, row-sum bound and scalar absorption are derived here.
Lemma J for the actual lifts is conditional exactly on the response,
quietness, frame and partition hypotheses in section 1. No numerical
check or claim about all of F-D or BG's extension proof is made.

## 5A. Continuation: retaining the patch tail

**Implication (author algebra; analytic hypotheses remain gaps).**
Replace Resp by

    ||Theta(Lift_b^d)-Theta(W_ref)||_Q^2
       <= C_r sum_{older Q'} w(Q,Q')a(Q') + tau_b(Q)^2,
    sup_{b,Q, histories} tau_b(Q)^2 <= kappa_tail e,
    e=eps_q^2 T^2.

The same near ranks, far sum, B,D,P give
A_k<=2(1+kappa_tail)e+B A_{k-1}+D A. For PD<=1/2,
A<=4P(1+kappa_tail)e. Thus C_J=2P(1+kappa_tail) for the aligned
partition and C_J=32P(1+kappa_tail) for all translated testing cubes.
The constants depend only on C_r,rho,kappa_tail and the fixed
incidence convention, and are free of x,L,depth,volume only if those
input constants are uniform; t_0/L must meet section 4's bound.
No same-level or multilevel nonlinear response estimate is proved
by this replacement. The one numerical run in this continuation is
the separate scalar check recorded in the response-tail note; the
geometry and this algebra were not established by that computation.
