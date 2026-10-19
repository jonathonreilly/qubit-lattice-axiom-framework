<!-- Original PR9795 source SHA256 8da1e3ef45013ad258d65f34d77ef3ff2a11a6f889df83714a2121c0ad8f625c. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# A native heavy-defect loop vertex into the neutral background

Status: bounded-support. Use the original one-qubit Hamiltonian with periodic
longitudinal height four and an even transverse torus R>=6. No new interaction,
gauge degree of freedom, or scalar coupling is introduced. A prepared heavy
spin defect is a probe of the existing dynamics; it is not a derived fermion,
physical detector, or relaxed matter ground state.

## Exact first-order wall-preserving motion

N counts broken longitudinal bonds. The N=2 cluster costs 4J above the
aligned-column sector. Its mobile states can be labelled |i,z;s>: one spin
at layer z is flipped relative to the aligned column background s, at column
i. The background is defined by the majority spins in that column. A length
three flipped interval relative to another reference is already represented
as a singleton over a complemented column background; it is not a separate
fixed-background three-flip branch. Length-two half-column intervals have no
first-order N=2-preserving motion.

Direct physical Pauli action gives nearest-column hopping amplitudes
-Jlambda along x and -Jlambda s_i s_j along y. The latter follows from
Y_iY_j|z_i,z_j>=-z_i z_j|flipped>, with initial z_i=-s_i,z_j=s_j.
All other transverse insertions leave N=2. Thus the dimensionless mobile
block is

 T=-sum_x (|j><i|+h.c.)
   -sum_y Zbar_i Zbar_j (|j><i|+h.c.).

The background labels are physical column states. Their sign factors are not
an added gauge Hilbert space. The product of link signs around a square is
exactly P_p=product of its four Zbar columns. A local rephasing of particle
basis states changes link signs but not this loop product.

## A native loop excites the neutral operator

There are 36 four-step returns on the square lattice. Twenty-eight retrace
and contribute identity; the eight oriented square paths give twice each
of the four incident plaquettes. Consequently

 <i|T^2|i>=4I,
 <i|T^4|i>=28I+2B_i, B_i=sum_(p incident i) P_p.

On the even torus odd returns vanish. For orthogonal background states
beta,beta-prime, the return amplitude is

 <i,beta-prime|exp(-i tau T)|i,beta>
 =tau^4 <beta-prime|B_i|beta>/12+O(tau^6).

This is a derived transition vertex, not a promise that every matrix element
is nonzero. The inelastic return probability from g begins as
 tau^8 Var_g(B_i)/144+O(tau^10).
A four-hop ordered path around a single plaquette instead has vertex P_p.
If intermediate positions are selected, its leading amplitude is tau^4 P_p
for four equal short intervals. Such position selection is an explicit
preparation/readout protocol, not a derived detector mechanism.

For the vacuum coefficient ground of K=-5E-4P, translation and rotation
symmetry and the variational bound give <E_edge>>=0.6. Each plaquette flip
anticommutes with a boundary edge product; for two anticommuting Hermitian
involutions, <A>^2+<B>^2<=1. Therefore Var_g(P_p)>=0.36. The plaquette operator preserves the row/column-positive block, whose
ground is unique; this variance is therefore positive-energy weight, not
elastic motion within a degenerate ground space. The ordered native loop
has a strictly nonzero neutral excitation channel in that state. The
unmonitored B_i variance is a different quantity; the numerical R5 control
finds 3.9860571 and is not substituted for a general analytic bound. R5 has
five-step winding returns, but each runs straight around one axis and its
sign telescopes to identity; the resulting 4I is elastic. This particular
inelastic control still starts with the fourth-order vertex. The theorem
uses even R to avoid odd returns altogether.

The uniform loop operator also has a fixed relation to the original readout.
For any coefficient eigenstate e orthogonal to g,
 -4<e|P|g>-5<e|E|g>=0 and <e|O|g>=-3<e|E|g>.
Hence <e|P|g>=(5/12)<e|O|g>. This links two native operator vertices; it is
not a universal coupling to mass. A sum of loop amplitudes must not be
confused with a single unmonitored particle experiment.

## Controlled microscopic time scale

At each fixed box an analytic wall-cluster reduction gives
H_eff,N2=common scalar+Jlambda T+O_R(Jlambda^2), on the mobile block at
leading order. At physical time t=hbar tau/(Jlambda), Duhamel gives an
O_R,tau(lambda) error relative to exp(-i tau T), after the common fast phase
is removed. The preparation and readout use matching channel embeddings.
Bare local spin creation X_(i,z) on the actual vacuum differs from that
embedding by O_R(lambda), which can be included explicitly. This is a
prepared excitation statement, not an assumption about a relaxed heavy state.

Combining the two expansions yields an amplitude error
O_R(tau^6)+O_R,tau(lambda). In a joint small-tau limit the lambda error must
be smaller than tau^4 to resolve the leading amplitude. No uniform growing
box/time theorem is claimed. A microscopic scalar particle interpretation
does not follow just from access to this neutral operator.

## The heavy environment is different, and that is derived

For fixed background s, T is a degree-four signed adjacency matrix, so its
lowest eigenvalue is at least -4. Equality requires mutually consistent link
phases on every loop. Here noncontractible loop products are automatically
positive (x links are one and y products telescope), so equality is equivalent
to every P_p=+1. Flat configurations have s_xy=a_x b_y and the heavy ground
wave is b_y/sqrt(N). Half-column static channels have first-order energy zero
and cannot compete with -4 for lambda>0.

Thus the fixed-box weak-coupling heavy ground selects flat plaquette flux
already at order lambda. The vacuum coefficient ground, selected at order
lambda^4, has <P_p><=0.8 and is not that state. In the flat background
subspace, P_flat E P_flat=0 on a sufficiently large torus: an edge pair flip
creates bad plaquettes. Its vacuum coefficient energy is -4N, whereas the
actual vacuum energy is at most -10N. There is a genuine background energy
cost to the heavy state's preferred environment.

This exposes the source/detector obstacle instead of hiding it in an assumed
common field. A growing-volume dressed defect may form a local domain rather
than globally reorder the slab; that joint limit and its mode dressing remain
open. The native loop vertex is established, but identifying it with relaxed
matter, a cosmological scalar, a three-dimensional fermion, or a universal
gravity coupling would require additional derivations.
