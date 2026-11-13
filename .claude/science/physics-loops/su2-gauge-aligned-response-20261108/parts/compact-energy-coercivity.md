# All-compact two-step forest energy coercivity

Research proof, 2026-11-08; a fresh-context mathematical check is recorded in
`../gates/forest-flat-check.md`. No formal audit or retained status is claimed.
Uses the same finite path-averaged kernels and forest convention as
`compact-forest-exchange.md`, based on main
`1e0d3b58dcda7f83152b0bb51729260247454d65`. No new literature search,
numerical job, source edit, commit or push. The previous draft is unchanged.
Model identifier unavailable through host tools; inherited supervisor model,
launch reasoning effort medium. Prior preflight: go.

Prior-art reconciliation: CUT_SECTOR_COERCIVITY_ASTRA, CS7–CS12, at draft
`89faef229ff6e6bde42baad15ed8270c2f4087d8` already proves the one-step compact
path-filling and centered-mismatch coercivity method, with explicit constants
and arbitrary real terminal field. The supervisor read that argument after
Luna located it. The proof below gives its two-step composition in a single
terminal-root forest, at terminal identity, retaining all intermediate links.
Its method is credited to the prior repo work; it is not claimed as new.

## Statement and geometric assumptions

Fix odd L>=3 and kappa>0. On a four-dimensional fine periodic lattice with
N a multiple of L² and N/L²>=3, use nested levels X0,X1,X2, spacings
1,L,L². Terminal links U2=I. The level-0 and level-1 means are exactly the
coordinate-order averaged paired paths defined in the bounded two-region
note, each with 4! L^4 paths. For U0,U1 arbitrary SU(2) link fields let

    W0=sum_(fine plaquettes p) [1-w(U0,p)],
    gamma_l,c=|M_l,c| - <U_(l+1,c),M_l,c>,
    E=W0+kappa sum_c gamma_0,c+kappa sum_c gamma_1,c.

Let terminal fine blocks be the centered cubes of side L², with one root
in X2. In each choose any internal fine spanning tree and use their union
to gauge-fix U0 to a0 and U1 to a1 as in the preceding draft. Then a finite
constant C(L,kappa), independent of N and of the choice of these trees,
satisfies

    sum_(e in E0\T) [1-w(a0,e)]
      +sum_(e in E1) [1-w(a1,e)] <= C(L,kappa) E.        (1)

Consequently the requested c=1/C>0 exists. Trees need not be shortest:
a simple tree path has at most L^8-1 links in a terminal cube. Excluding
kappa=0 is necessary: then U1 is uncontrolled. This is an energy estimate
on the full compact configuration space, not a chart assertion or a
probability/clustering estimate.

## 1. Two elementary compact estimates

Write d(A,B)=||A-B|| for quaternion Euclidean distance on SU(2).
Then d(A,B)^2=2[1-w(A*B)], and d is invariant under unitary left/right
multiplication and inversion. For n unitary factors,

    d(product A_i,product B_i)^2 <= n sum_i d(A_i,B_i)^2. (2)

This follows by telescoping and Cauchy–Schwarz. Factors traversed backwards
obey the same inequality.

Let M be an average of unitary P_i, r=|M|, V,T unitary, and
D=average_i d(P_i,T)^2. For the CENTERED gap gamma=r-<V,M>,

    d(V,T)^2 <= 4 gamma + 3 D.                          (3)

Indeed |V-M|²=(1-r)²+2gamma, |M-T|²<=D by Jensen, and
1-r<=1-<M,T>=D/2. Since 0<=1-r<=1, (1-r)²<=D/2.
Apply |V-T|²<=2|V-M|²+2|M-T|². Thus the missing mean deficit is
paid by D; it is never silently replaced by an uncentered gap. This remains
valid at M=0 and at all compact configurations.

## 2. Finite cubical filling lemma (including its quantitative meaning)

Consider two oriented fine lattice paths P,Q with the same lifted endpoints
in an integer rectangular box B. There is a finite sequence of elementary
plaquette insertions/removals and immediate backtrack cancellations
transforming P into Q, entirely in B. One proof orders the coordinate steps:
swap adjacent steps in different coordinates by their unit square, cancel
adjacent inverse steps, and repeat to reach the fixed coordinate-order
path. Equivalently, the product cubical cell complex of four intervals is
contractible and its 2-skeleton has trivial fundamental group. The explicit
step-swapping construction supplies a finite combinatorial witness; no
continuum or flatness premise is used. An interval of zero length in an
unused direction causes no problem.

Each plaquette move changes path transporter by a conjugated plaquette
holonomy, in a common endpoint frame. If the chosen sequence has m moves,
(2) bounds

    d(U(P),U(Q))² <= 2m sum_(moves j) [1-w(U_pj)].       (4)

Multiplicity is retained. We will use finitely many path templates, with
bounded box sizes and path lengths depending only on L. Choose a finite
move sequence for each template, and take the maximum of twice its length
times its maximal plaquette multiplicity. This defines a finite constant
C_fill(L) for bounding (4) by the unweighted sum of plaquette actions in
the template box. It is an exact finite-domain existence definition, not
a proposed numerical constant. There are finitely many templates even when
all internal terminal-block spanning trees are allowed, because their graph
has L^8 vertices. Translates use translated witnesses.

Periodic convention: paths used below are first lifted into the universal
integer lattice in their specified local blocks, then projected to the
torus. Comparing paths always uses identical lifted endpoints. Thus every
filled loop has zero winding. Projecting (4) preserves its validity even
if a projected cell is repeated; repetitions keep their multiplicity.
No arbitrary winding loop is filled or declared trivial. The terminal
straight path is retained explicitly precisely when the lifted roots differ.

## 3. Intermediate links and plaquettes are controlled by level-zero energy

For each intermediate edge e=(x,x+L e_mu), let R0,e be its straight fine
path and define delta_e=d(U1,e,U0(R0,e))². Every paired path in M0,e
has the same lifted endpoints as R0,e, lies in the rectangular union of
the two adjacent level-zero blocks and their connecting edges, and has
length bounded by a function of L. Apply (4) to each such path, average,
then apply (3). Thus there is a finite fine-plaquette set B_e and a
constant C0(L) with

    delta_e <= 4 gamma_0,e + C0(L) sum_(p in B_e) W0,p.  (5)

The B_e are translates of finitely many bounded templates, with periodic
multiplicities retained when necessary. In particular no division by |M|
or near-identity assumption occurs.

For an intermediate plaquette P, compare its four-link transporter to the
fine perimeter obtained by replacing every edge with R0,e. By (2) its
squared discrepancy is at most 4 sum_(e in boundary P) delta_e.
The fine perimeter bounds an L-by-L fine square. Its transporter differs
from I by (4), using the standard square filling. Applying the squared
triangle inequality gives a constant C1(L) such that

    W1,P := 1-w(U1,P)
       <= 4 sum_(e in boundary P) delta_e
          + C1(L) sum_(p in the fine square) W0,p.       (6)

This establishes a local positive linear bound of W1,P in gamma_0 and
fine plaquette action. We do not posit a Wilson law at level one.

## 4. Terminal constraints control straight fine root-to-root transport

For each terminal edge c=(q,q+L² e_mu), write R1,c for its straight
intermediate path of L edges and T_c=U0(R0 of those consecutive edges).
Thus T_c is EXACTLY the straight fine path of length L², not a replacement
mean. Apply (3),(4) on the intermediate lattice to M1,c with output I:

    d(I,U1(R1,c))²
       <= 4 gamma_1,c + C2(L) sum_(P in B1,c) W1,P.     (7)

Every paired level-one path and R1,c has the same lifted endpoints in a
bounded two-terminal-block box, so the filling lemma applies. Replacing
the L edges of R1,c with their fine straight paths and using (2) gives

    d(I,T_c)² <= 8 gamma_1,c
          + 2 C2(L) sum_(P in B1,c) W1,P
          + 2L sum_(e in R1,c) delta_e.                 (8)

Combine (5),(6),(8). The result is a positive linear bound for d(I,T_c)²
in finitely many fine W0,p, level-zero gamma_0,e and this gamma_1,c, all
inside a bounded translate of a fixed finite collection of lattice boxes.
This is how terminal identity enters. Fine curvature alone would not
control nontrivial flat periodic holonomy; (8) retains the terminal gaps
and does control each elementary terminal root-to-root segment.

## 5. Every remaining forest-gauge link has a controlled reference

Let H_x be the fine tree transporter from x's terminal root r(x) to x,
so a_l(x,y)=H_x U_l(x,y) H_y*. For a fine edge e=(x,y), define the fine
path P_e: root r(x) to x along its tree, traverse e, then traverse the
reverse tree from y to r(y). Its transporter is a0,e.

The blocks of x and y either coincide or are neighbors along e's direction.
If they coincide, P_e is a zero-winding loop in that block; compare it to
the empty path. If they differ, choose the adjacent lifted roots and
compare P_e to their straight terminal path, using T_c or its inverse.
Both paths have identical lifted endpoints in a rectangular box containing
the two blocks. The forest paths stay in their blocks and each has length
at most L^8-1. Consequently (4) and the squared triangle inequality give

    d(I,a0,e)² <= C3(L) sum_(p in Bforest,e) W0,p
                    + 2 d(I,T_c)²,                    (9)

where the last term is zero for a same-block edge. This applies also to
fine tree edges, whose left side is identically zero; including them when
summing is harmless. Arbitrary tree shape changes the finite template,
not the uniformity of its upper bound.

For an intermediate edge e=(x,y), first replace U1,e by U0(R0,e). The
squared discrepancy in the forest frame is exactly delta_e. The fine path
H_x R0,e H_y* again joins either the same terminal root or neighboring
terminal roots: a straight intermediate edge of length L cannot skip a
terminal block of side L². Its lifted box and length are uniformly bounded.
Apply the same filling argument and a squared triangle inequality:

    d(I,a1,e)² <= 2 delta_e
          + C4(L) sum_(p in Bforest1,e) W0,p
          + 4 d(I,T_c)².                              (10)

Again omit the last term when roots coincide. Equations (5)–(10) now
bound every requested link by a local positive linear combination of the
actual energy summands. No logarithm or local gauge chart was introduced.

## 6. Uniform summation, exact definition of the finite constant

Here is a precise way to close the counting without assuming a numerical
incidence estimate. Fix one terminal root at the origin in the infinite
lattice. List every fine or intermediate positive link whose tail is in
that terminal block. There are finitely many such links. For each link,
list every allowed tree choice in the endpoint blocks, every coordinate-
order paired path, and every plaquette or path needed in (5)–(10).
Choose one filling witness for each comparison as in §2. Expand the
right sides of (5)–(10) completely into W0,p, gamma_0,e and gamma_1,c.
Take for each link and input summand the maximum coefficient over the
finite allowed tree choices; include absent summands with coefficient
zero. Sum these majorant coefficients for all output links in the origin
terminal block, using the conversion 1-w(a)=d(I,a)²/2.

This defines a finite nonnegative stencil of weights on input energy
summands, with total coefficient mass K(L)<infinity. If necessary enlarge
K to max(1,K); this ensures a positive denominator. The stencil uses only
L, the prescribed paired-path construction and the finitely chosen filling
witnesses; it does not use N or a configuration. The maximum over trees
also covers different choices in different translated terminal blocks.

Translate this majorant over all terminal roots of a finite torus. An
individual input summand can receive contributions only from the finite
stencil offsets and orientations. Its total incoming coefficient is at
most K(L), including offsets coinciding after periodic projection. This
last claim can alternatively be seen by assigning each stencil term its
output-root translate: for a fixed input and a fixed template offset,
there is at most one root translate modulo the torus. Therefore

    sum_(remaining e) [1-w(a_e)]
      <= K(L) [sum_p W0,p + sum_e gamma_0,e + sum_c gamma_1,c]
      <= K(L) max(1,kappa^(-1)) E.                       (11)

Set C(L,kappa)=K(L) max(1,kappa^(-1)) and c=1/C. This is the promised
finite geometric existence constant. Nothing in its definition invokes
an unverified filling, an unbounded volume enumeration, or numerical data.
A more efficient tree or smaller explicit constants could improve it, but
is unnecessary for the quantified existence theorem.

## Checks, scope and remaining quantitative task

The proof covers r=0, reversed orientations, periodic boundary crossings,
and every internal spanning tree. It deliberately does not fill a winding
loop: terminal-edge comparison paths retain their lifted endpoint displacement.
As a consistency consequence E=0 forces every a0 and a1 link to I, so no
nonidentity quotient zero-energy state survives under terminal V=I.
This consequence is derived from the quantitative inequality, not assumed
from the historical zero-energy argument.

The coefficient deteriorates with L and kappa and is not optimized.
The actual posterior also contains all normalized-kernel radial weights;
(11) alone does not control their rough-sector probabilities uniformly in
volume, connected responses, or any continuum limit. A small energy
supplies compact quotient closeness in summed chord-square, but energy
coercivity is not a clustering estimate. This draft requires independent
checking of the finite-template and normalization-sensitive uses before
any downstream status promotion.
