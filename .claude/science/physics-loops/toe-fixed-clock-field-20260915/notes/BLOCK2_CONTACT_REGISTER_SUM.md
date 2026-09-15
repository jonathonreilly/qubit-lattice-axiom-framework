# Summing local cofactor contacts with bounded registers

Personal proof candidate, 2026-09-15. The finite sign, derivative, operator
block and source checks pass. This extends the preceding fixed-assignment
cofactor lemma to the complete resource sum for a prescribed derivative graph.
It does not sum all derivative graphs or identify the physical expansion.
Verification and review are personal; no independent audit is claimed.

Let E be a prescribed set of k distinct pair parameters and let d_i be its
vertex degrees. Choose an orientation (r_e,c_e) of every derivative pair.
The assigned-cofactor formula sums resource choices u_e shared by its two
endpoints. Resource assignments with a repeated selected row or column at
one resource vanish. Retain the full local footprint A_i and CAR Hilbert
space of the determinant note. Fix any total vertex order O.

## 1. Local registers implement the entire resource assignment sum

For each edge e, introduce H_e=C|vac> direct-sum l2(resources). The edge
register is inactive outside the interval between its endpoints in O and
holds u_e inside that interval. At its first endpoint the local matrix
block has left register vac and right register u_e; at its last endpoint
it has left register u_e and right register vac. Internal vertices preserve
the active register value. Taking the ordered product of these block matrices
and the vacuum boundary matrix element sums every u_e exactly once. This
is an auxiliary summation identity, not a new physical degree of freedom.

Every endpoint requires u_e in A_i. At a vertex, use the cofactor CAR map
with annihilators deleted for its selected row entries and creators deleted
for its selected column entries. Only incident-edge resource values are
needed for these deletions. Coincident selected rows or columns are checked
at their common endpoint; their matrix block is zero. All nonzero base
CAR blocks are contractions.

## 2. Both kinds of cofactor signs can be evaluated while registers are live

The position-parity sign in the preceding note factors by vertices. For
one edge, its two endpoints contribute an even count before its first
endpoint, an odd count strictly after its first through its last endpoint,
and zero after its last. Thus at vertex i the sign is

    (-1)^(sum_(e active just before i) 1[u_e in A_i]).

The active set includes edges ending at i, and excludes edges starting at
i. This is a local diagonal sign on currently live registers. Multiple
edges using one resource add their exponents modulo two.

The matching-permutation sign is a product over pairs e,f assigned the
same resource whose row and column orders disagree:

    (-1)^1[(pos r_e-pos r_f)(pos c_e-pos c_f)<0].

Disjoint endpoint intervals cannot give such an inversion: both row and
column of the earlier interval precede both of the later one. Therefore
every possible inversion can be evaluated at the vertex where the later
of the two intervals starts. Both register values are then available;
intervals sharing an endpoint are included in that vertex's matrix block.
The resulting equality-dependent sign has modulus one. No closed register
has to retain a distant resource value. Same-row/same-column coincidences
were already excluded locally.

Consequently, for this prescribed orientation of E, the complete resource
sum has an ordered local-block realization

    sum_(u_e) assigned cofactor term
      =2^(-k) product_i 2^|A_i|
        <vac tensor I, product_(i in O) B_i(A_i) (vac tensor I)>.

The product includes the position and matching signs just described.

## 3. A volume-independent norm bound

Let s_i and t_i count edges starting and ending at i in O, so s_i+t_i=d_i.
In each local block matrix, a fixed left register row has at most
|A_i|^s_i nonzero right columns, since each new register must select a
resource in A_i. A fixed right column has at most |A_i|^t_i nonzero left
rows. Spectator active registers stay fixed; all other registers are vac.
Each block, acting on the base CAR Hilbert space, has norm at most one.
For a block matrix T with block norm at most one, at most R blocks per row
and C per column, Cauchy-Schwarz gives

    sum_alpha ||sum_beta T_(alpha,beta) x_beta||^2
      <=R sum_(alpha,beta allowed) ||x_beta||^2
      <=R C sum_beta ||x_beta||^2.

Apply this with R=|A_i|^s_i and C=|A_i|^t_i. The calculation first holds
for finitely supported register vectors and extends by the same norm bound
to the countable resource Hilbert space. The resulting bound is

    ||B_i(A_i)|| <= |A_i|^(d_i/2).

For d_i=0 this means one, including an empty footprint. For d_i>0 an empty
footprint gives the zero operator. The norm contains no total resource
count and no lattice volume. Repeated-resource restrictions and phase
signs only zero blocks or multiply them by unit scalars.

The scalar derivative coefficient has this representation in every cyclic
vertex order, although the local blocks change. The earlier cyclic-realization
source proof therefore applies without assuming these blocks commute.

## 4. Absorb degrees with one exponential footprint reserve per vertex

Choose epsilon>0. For integer d>=1 and a>=0,

    a^(d/2) exp(-epsilon a)
        <=(d/(2e epsilon))^(d/2)
        <=sqrt(d!) (2epsilon)^(-d/2).

For d=0 use exp(-epsilon a)<=1. Absorb the positive vertex weight

    q(A)=w(A) 2^|A| exp(epsilon |A|) exp(R|L(A)|)

into the scalar sine matrix J, and normalize each local block by the
corresponding degree constant. Gaussian replica phases and the remaining
source exponential are local contractions. For one orientation the source
trace bound acquires

    2^(-k) (2epsilon)^(-k) product_i sqrt(d_i!).

Summing the 2^k orientations gives, for the FULL prescribed mixed derivative
partial_E D and any distribution of four source powers,

    |F_E| <= (2epsilon)^(-k) product_i sqrt(d_i!)
                      rho^(l-2) Tr |L|^4 J^2,
    rho=||J||.

The two-source version follows by the same scalar interpolation proof.
The same q is used for every derivative graph; its resource cost remains
linear in mass because |A|<=3m. For example epsilon=log2 makes the boost
4^|A| instead of 2^|A|. In the previous small macroscopic-source regime,

    q <=(2/384) exp[-(x/128-6log2)m]
      <=(2/384) exp[-xm/256] if x/256>=6log2.

Thus x>=32768 still satisfies the previous sufficient moment and sine-norm
constants, including rho<3.862e-33. The source trace remains O(a^4) there.
For one prescribed E, Taylor's four-source remainder gains the factor
(R^4/24) l^4 in addition to the displayed degree constant. The parameter
example remains a restricted-bound example, not a phase-window claim.
At each fixed graph the earlier absolute contact and graph Holder estimates
justify the subtracted component cutoff passage; the operator bound is
uniform in that cutoff. No graph-order limit is taken here.

This bound sums the resource choices for one prescribed derivative graph.
It has not summed graphs, graph embeddings, or the physical BKAR/cut
combinatorics. In particular an arbitrary extra forest on the vertices of
an already enumerated loop must not be summed by claiming its count is only
exponential in loop length. Residual mixed phases remain another obligation.


## Author challenges and remaining count

A direct determinant-jet comparator multiplies the original determinant
permutation polynomials and extracts the prescribed derivative. Separately,
the register checker sums oriented resource assignments, applies the local
active-register signs, and evaluates the remaining cross minors. It checks
800 footprint/graph/order cases, including paths, a star, and interleaved
edges, with maximum discrepancy 4.45e-16. Omitting matching inversions gives
an error 2.764. The CAR cross-minor formula is separately challenged in the
preceding runner; this checker does not construct the entire large tensor
Hilbert space or claim an independent proof.

Finite block matrices with varying row/column branching obey the local
Schur bound. Complete determinant derivatives on a four-label loop obey
the source bound for all 35 four-source placements on each of five prescribed
graphs. These generic finite checks do not determine a physical covariance
or test infinite-volume convergence. The proof carries those finite-cutoff
norm identities; the declared graph-summation limitation remains.
