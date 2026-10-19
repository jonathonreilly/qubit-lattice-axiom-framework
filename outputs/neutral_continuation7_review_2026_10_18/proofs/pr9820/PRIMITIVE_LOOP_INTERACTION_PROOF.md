<!-- Original PR9820 source SHA256 b0fd47f02dd0049ce99d858e38d6f7eae4e295a9a4086043cee384f3a09fd58c. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Native primitive-loop law and a complete directional interaction test

Status: bounded-support. Trace: upstream_support to deriving interactions of
large features from the one-qubit Hamiltonian. No added interaction, fitted
potential, observational identification or retained proposal.

## 1. Precisely which coefficient is derived

Use H=-J sum(ZZ_z+lambda XX_x+lambda YY_y), aligned column backgrounds s_r,
fixed L=10 and sufficiently large even transverse periods (R>=8 for the local
order-eight example). Give a simple nonwrapping transverse cycle's N distinct
edges independent couplings g_e. We calculate the squarefree monomial
product_e g_e in its connected ground-energy expansion. This is a primitive
single-layer coefficient, not the sum of all native words at order N.
Repeated edges, multiple cycles and proper projected returns require separate
connected/folded calculations. The order-eight example below includes them.

Within this single-layer monomial a flipped spin costs d=4J. Its exact
intermediate costs therefore coincide with independent spins in fields d/2.
This is an auxiliary coefficient calculation, not a Gaussian assumption about
the actual lattice. A proper nonempty subset of a simple cycle has a vertex
with one Pauli insertion, whose ground expectation is zero. Every proper
partition in the connected cumulant vanishes. The complete distinct-edge
moment is consequently already the connected cumulant; no folded vacuum
return occurs in this particular monomial.

## 2. Exact local correlations give a closed law

With Fourier convention integral exp(i omega tau), the reference up-spin
correlations are

 G_XX=G_YY=2d/(omega²+d²),
 G_XY=-2omega/(omega²+d²), G_YX=+2omega/(omega²+d²).

For example the time-domain mixed function is i sign(tau) exp(-d|tau|).
Reversing the reference spin reverses the mixed functions only. If the cycle
has m turns (axis changes, not signed left/right turns), there are m/2 XY
and m/2 YX vertices. Convolution around the cycle leaves one frequency
integral. Dividing out the total time interval and taking minus logZ gives

 c_(N,m)(d)=(-1)^(m/2+1) integral dω/(2pi)
             (2d)^(N-m)(2ω)^m/(ω²+d²)^N.

The background operator is product_(turn vertices) s_r. Distinct edge labels
cancel the exponential's N!; there is no additional factor two for directions
of traversal. Setting g_e=Jlambda and d=4J gives the native contribution
Jlambda^N c_(N,m) times this corner product, where

 c_(N,m)=(-1)^(m/2+1) 2^(1-N)/pi
          Gamma((m+1)/2) Gamma(N-(m+1)/2)/Gamma(N).

Both Gamma arguments are positive. Four-turn loops are negative, six-turn
loops positive, eight-turn loops negative. Concavity adds no other sign.
Thus retaining only attractive rectangles is not a justified interaction law.

For rectangles, m=4 and N=2(a+b):

 c_N=-3 Gamma(N-5/2)/(2^(N+1)sqrt(pi)Gamma(N)),
 c_(N+2)/c_N=(N-5/2)(N-3/2)/(4N(N+1)).

The aspect ratio drops out because only four mixed and N-4 equal-axis vertex
functions occur. Values at N=4,6,8,10,12,14 are respectively
-1/128,-3/8192,-9/262144,-143/33554432,-663/1073741824,-6783/68719476736.
This law is derived from the integral, not inferred from these controls.
For fixed four turns its magnitude has asymptotic
3*2^(-N-1)N^(-5/2)/sqrt(pi). This is the primitive coefficient's asymptotic,
not a convergence proof for the full interaction series.

## 3. A full local interaction where nonrectangular loops matter

Define the diagonal connected two-column energy at a fixed order by
V(u,v)=E({u,v})-E({u})-E({v})+E(empty), with a common flat reference and
matched native N0 normal form. Below order ten there is no nontrivial N0
column flip, so the scalar fixed-background coefficient calculation is valid.
This is an effective interaction coefficient, not a scattering amplitude.

Take u=(0,0),v=(2,2). No order below eight has connected sign support on both.
At order eight the primitive simple cycles are one 2 by 2 boundary and two
L-triomino boundaries. Their coefficients sum to

 -9/262144+2*(5/262144)=1/262144.

This is not yet the complete answer. Two elementary squares with anchors
(0,0) and (1,1) share a column and contribute at the same order. Let z be their
layer separation. The exact connected coefficient, including folds, is

 z=0: 3/65536,
 z=+/-1: -127/10616832,
 |z|>=2 (without wraps): 0.

The local intermediate cost is 4J times the number of flipped spins minus
4J for each adjacent simultaneously flipped pair on the shared column.
The root's exact squarefree Rayleigh recursion uses this cost and the physical
XX/YY phases. A different independent Feshbach enumeration of all 40320
orders gives the following irreducible and folded parts:

| separation | irreducible | folded | connected |
|---|---|---|---|
| 0 | 1/131072 | 5/131072 | 3/65536 |
| 1 | -133/2654208 | 5/131072 | -127/10616832 |
| 2 | -5/131072 | 5/131072 | 0 |

Discarding folds gives the wrong coefficient and fails disconnected
cancellation. Each square has E4=-1/128 and self-energy derivative -5/2048;
the fold is E4(A)Sigma4'(B)+E4(B)Sigma4'(A).

Completeness follows from the operation budget. A simple cycle through u,v
needs two arcs of length at least four; at length eight these are shortest
monotone paths, giving exactly the three simple cycles above. Smaller cycles
with repeated edges cannot have both columns in their corner sign support.
The remaining possibility is two four-cycles. To share column support while
containing u and v their anchors must be (0,0),(1,1). Equal and neighboring
layers are exactly the computed cases; disjoint column support has additive
H0 energies and connected cancellation. Both cycles already consume all eight
operations, leaving no extra connecting word. The background factor of the
two-square term is P00 P11, with the shared corner cancelling.

Every listed corner product contains u,v once, so its connected pair contrast
is four times its coefficient. There are L choices for a common layer and L
for each adjacent-layer offset. Thus

 V((0,0),(2,2))=JLlambda8 *545/5308416+O(Jlambda10)>0

at sufficiently small lambda, for this fixed local coefficient convention.
The leading interaction is repulsive. The O(lambda10) is a local expansion
statement, not a volume-uniform bound on the entire many-body spectrum.

## 4. Companion attractive direction and scope

For separation (3,0), the first connected sign-supporting graph also has eight
operations. Its simple cycles are the two 1 by 3 rectangles on opposite sides
of the axis. Two elementary squares spanning this distance have disjoint
column supports and no connected contribution; shorter repeated graphs cannot
carry both corner labels. Therefore

 V((0,0),(3,0))=-9JLlambda8/32768+O(Jlambda10).

This attractive direction and the repulsive diagonal are both stronger in
power counting than the charged-column hopping Jgamma lambda10. They give
native shape-dependent interactions useful for the relative-motion problem.
They do not prove an isolated new molecular band: the complete relevant Q8
shape manifold and kinetic reductions would still need to be solved.

The primitive formula alone must not be extrapolated to the full coefficient
of a corner operator at arbitrary order. Repeated-edge renormalization,
interacting cycles and, at winding orders, degenerate-sector transformations
are separate contributions. No all-range attraction, long-range force,
Newtonian limit, universal scalar coupling or observed particle assignment
follows. The supplied native Hamiltonian, geometry and units remain explicit.
All controls are exposed model development, with no observational data used.
