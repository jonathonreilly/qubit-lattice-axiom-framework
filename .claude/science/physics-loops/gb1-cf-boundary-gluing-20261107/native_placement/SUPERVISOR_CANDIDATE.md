# Supervisor derivation before independent comparison

This is a candidate mathematical encoding, not an axiom-selected law. Inputs:
five-state R=(0,0)+(1/2,1/2), orientation inversion K=diag(1,-1,-1,-1,1),
ordinary tensor composition, pure geometric permutations of native sites.
The framework is under test. No physical state, probability law or record
process is supplied by this encoding.

## Capacity diagnostic

For a connected finite graph the link Hilbert space has dimension 5^E.
For each occupied edge assign j=1/2, otherwise j=0. Gauge invariance requires
even occupied valence at each vertex, and every even-valence tensor of spin
halves has a singlet (pair them). Regrouping endpoint factors by vertices
gives at least one invariant vector per even occupied-edge pattern; distinct
patterns are orthogonal. Over F2 the connected incidence matrix has rank
V-1: the sum of rows is zero and any spanning-tree reduced incidence minor
is nonsingular by leaf elimination. Thus dim H_phys >= 2^(E-V+1).

For the cubic n-torus, n>=3, V=n^3, E=3n^3, so dim H_phys >=2^(2n^3+1).
At n=3 this is >=2^55 versus 2^27 for 27 native qubits. This is a decisive
finite capacity mismatch for exact same-site-count isometry of the entire
physical sector, even before locality/symmetry. It says nothing against a
coarse or restricted low-energy encoding. The one-site M2 axiom itself does
not assert ordinary generated tensor composition; that remains a condition.

## Four native qubits per link

Place four qubits along an oriented coarse edge, in traversal order 1,2,3,4.
Write unit one-excitation vectors e1=1000, e2=0100, e3=0010, e4=0001.
Define a normalized isometry J:R -> (C2)^tensor4 by

J|0>=(e1+e4)/sqrt2,
J|4>=(e2+e3)/sqrt2,
J|1>=(e1-e4)/sqrt2,
J|2>=(e2-e3)/sqrt2,
J|3>=(|1100>-|0011>)/sqrt2.

All five columns are orthonormal. The native reversal permutation F reverses
four bit positions and satisfies FJ=JK. The code excludes |0000>; its
projector Q=JJ* is invariant under F. No internal gauge color is identified
with a spatial axis. Physical operators use J O J*, with code identity Q;
these are corner embeddings, not unital M5 subalgebras of the full M16.

## Geometry and all translation phases

Work first on native torus (Z/(5n))^3, n>=3. For each p in (Z/5)^3, put
coarse vertices at p+5z. The edge from v to v+5e_i uses exactly the four
native sites v+t e_i, t=1,2,3,4. Distinct edge interiors are disjoint.
All other native qubits are fixed to |0>. Let C_p be the product of the
five-dimensional edge codes with those spectators. It is isometric to the
full 5^(3n^3)-dimensional coarse link model, including boundary sectors before
any Gauss projection. The construction is sparse: 12 active qubits among
125 native sites per coarse cell, with 113 spectators. Four is sufficient,
not asserted globally optimal.

C_p and C_q are orthogonal when p!=q mod5. Let D be the nonempty set of
coordinates in which the residues differ. If |D|=1 choose a direction i
outside D; every site q+t e_i, 1<=t<=4, differs from p in that fixed D
coordinate and in coordinate i. If |D|=2 choose i outside D, leaving two
fixed differing coordinates. If |D|=3 choose any i, again leaving two fixed
differences. In each case the q-edge lies wholly in p-spectator sites:
p-active sites have exactly one nonzero residue relative to p. That whole
q-edge is |0000> on C_p but orthogonal to |0000> on C_q, proving orthogonality.

Hence C_all=direct-sum_p C_p is a genuine native subspace of dimension
125*5^(3n^3); the phases are encoded in the same native qubits, not attached
as an extra register. Unit translations send C_p to C_(p+a). A proper cubic
rotation sends C_p to C_(Rp), reorders edge registers, and reverses any edge
whose chosen positive orientation becomes negative. FJ=JK proves the exact
intertwining with the geometric coarse-edge action, with no compensating
on-site gate. Thus C_all is invariant under the full native space group.
A fixed C_p alone has only coarse translations; including the full orbit is
essential. No average over phases or selected physical origin is assumed.

The encoded all-j=0 vector in each phase is gauge invariant. The normalized
sum over its 125 orthogonal translates is an explicit fully geometric-symmetric
code vector. It is an example of a state, not a selected physical vacuum.

## Local identification of the phase and finite-range operator extension

At every native site x let D_x be the product of Q on the six length-five
edge interiors incident to x. These six supports are disjoint. Then
D_x|C_p = identity if x=p mod5, and zero otherwise: the same residue argument
above exhibits one outgoing false-phase edge entirely on p-spectators.
D_x is a local orthogonal projector on 24 qubits in l1 radius4, carried
covariantly by every native translation and cubic rotation.

For a supplied translation/cubic-invariant coarse gauge Hamiltonian H=sum_z h_z,
let h_0 use the three outgoing electric terms and the three positive elementary
plaquette terms at 0, each physical term once in the global sum. Encode each
supported link using J to obtain htilde_0, and set a_0=D_0 htilde_0 D_0.
On true-phase codes this is h_0; on every false phase it vanishes. For O the
24 proper cubic rotations, with their actual site permutations U_R, put

H_native=(1/24) sum_(x native) sum_(R in O)
 T_x U_R a_0 U_R* T_x*.

This is exactly invariant under all native translations and rotations. On
C_p, only x=p mod5 contributes; the sum is the rotation average of the
encoded coarse Hamiltonian, equal to H because H is cubic invariant.
Every term preserves every phase code and agrees there with the exact coarse
operator. Support is within l1 radius9 of x (plaquette corner offset 5+4,
star radius4), so diameter <=18; no native nearest-neighbor law is claimed.
All products of encoded observables, gauge constraints, and existing gluing
identities carry through each isometry. This result supplies placement and
finite-range operator extension, not a physical update or record mechanism.

The infinite-lattice statement is local: the same finite support prescriptions
and product-code sectors exist on Z3, with compatible finite restrictions.
Do not assert one canonical infinite tensor-product Hilbert representation;
no thermodynamic, continuum, vacuum-selection, or mass-gap theorem is used.

## Framework comparison

Same-spacing full-model identification fails the displayed finite capacity
test under ordinary qubit composition. Coarsening by five and retaining all
origins gives an exact space-group-invariant code without enlarging the local
M2 or changing the cubic adjacency. It remains a chosen code subspace and
supplied finite-range Hamiltonian; it does not prove a nearest-neighbor
Admissibility/Record realization or that nature supplies this phase/code.
Enlarged local cells/link degrees, a different finite gauge model, or emergent
low-energy gauge variables are alternative frameworks to compare, not routes
to silently exclude. No axiom edit or physical validation is inferred.
