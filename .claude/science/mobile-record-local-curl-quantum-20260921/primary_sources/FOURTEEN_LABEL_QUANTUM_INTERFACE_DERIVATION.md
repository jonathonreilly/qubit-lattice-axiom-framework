# The fourteen-label wave law and a physical qubit interface

2026-09-21. Primary conditional derivation, not yet independently reviewed.
This tests the one-parent birth law in LOCAL_CURL_READOUT_AND_NATIVE_FORMATION.md.
It does not identify the axiom's possibility algebra with an operational
quantum carrier without an additional bridge assumption.

## 1. The classical probability matrix has rank seven

Use the six A labels with e=+/-e_i,b=0 and the eight B labels with e=0,
b in {+/-1}^3. Set the six-component vector t_a=(e_a,b_a/2), and

    T_ab=t_a dot t_b,
    P_ab=[1+j T_ab]/14,             0<|j|<1.              (1)

Here b indexes the single occupied parent and a the newborn label; the
other five neighboring sites are vacant. Every column sums to one because
sum_a t_a=0. If F is the matrix with row t_a, then

    F^T F=2 I_6,      T=F F^T,      T^2=2T,
    T 1=0.                                                (2)

Therefore P has eigenvalue1 on the constant vector, eigenvalue j/7 on
six feature directions, and eigenvalue0 on seven remaining directions.
It has rank7 whenever j!=0. The sign of j does not alter the rank.

Suppose each of the fourteen unknown parent labels is represented by
some density matrix rho_b on a single physical qubit. The choice of those
states is otherwise unrestricted. A fixed instrument has effects E_a,
and its classical output probabilities obey

    Q_ab=Tr(E_a rho_b).

The real space of Hermitian qubit operators has dimension4, so rank(Q)<=4.
Consequently no such instrument realizes (1) exactly, even if it may
disturb the parent, uses arbitrary input-independent ancillas, and chooses
the fourteen input density matrices freely. An input-correlated record of
the preparation label is a different resource and is excluded here.
More precisely, the input and apparatus have the product state rho_b tensor
tau, with fixed tau. Shared randomness that correlates the choice of
preparation encoding with the apparatus is also excluded; a mixture of
different coordinated encodings need not retain this rank bound. Private
apparatus randomness independent of the input is already included in E_a.

The same test applies to positive observed rate effects. Giving every input
a strictly positive content-dependent occurrence rate h_b would require
the rate matrix P diag(h). Its rank remains7, whereas a qubit rate-effect
matrix still has rank at most4. Thus a positive occurrence clock does not
repair this single-parent interface. An input at which formation never
occurs does not implement the stipulated positive-rate native law.

This is a finite operational-interface test of this matrix. It does not
rule out the record process as a classical process, spatially encoded
records, quantum-only output marginals, or a different quantum formation law.

## 2. A quantitative bound without choosing the qubit encoding

Let delta=max_b TV(P_.b,Q_.b), optimized over any choice of fourteen qubit
input states and any fourteen-effect POVM. The following bound is not
claimed sharp:

    delta >= sqrt(3/7) |j| / 14.                          (3)

Indeed rank(Q)<=4 makes its kernel have dimension at least10. Its
intersection with the seven-dimensional range of P has dimension at least3.
On that range the smallest singular value of P is |j|/7. Choose three
orthonormal vectors in the intersection. Their Q images vanish, giving

    ||P-Q||_F^2 >= 3 j^2/49.

Each column difference has zero sum. If its positive and negative masses
both equal delta_b, its squared Euclidean norm is at most2 delta_b^2.
Summing fourteen columns yields ||P-Q||_F^2<=28 delta^2, proving (3).
The argument bounds any single-qubit realization, without a covariance
restriction or an asserted optimal carrier encoding.

## 3. Exact approximation for the natural fourteen Bloch rays

Now specify rho_b=(I+v_b dot sigma)/2, with v_A=e and v_B=b/sqrt(3).
This is a different optimization: the input encoding is fixed.

Proper cubic rotations act on both sets of rays by qubit unitaries.
Group averaging cannot increase the convex worst-input total variation.
An optimal averaged POVM therefore has the form

    E_A=alpha I+u e_A dot sigma,
    E_B=eta I+w b_B dot sigma,
    6alpha+8eta=1,
    alpha>=|u|,        eta>=sqrt(3)|w|.                  (4)

The respective fourfold and threefold stabilizers force the displayed
vector directions. Only proper rotations are used in this argument.
For j>=0 put a=alpha-1/14, d=eta-1/14 and z=w/sqrt(3)-j/56. The two
distinct input-row losses, computed directly from the dot-product counts,
are

    TV_A=max(|a|,|u-j/14|)+2|a|+4max(|d|,|w|),
    TV_B=3max(|a|,|u|/sqrt(3))
              +max(|d|,3|z|)+3max(|d|,|z|).             (5)

Project u into [0,j/14] and w into [0,sqrt(3)j/56]. This decreases every
absolute slope discrepancy in (5). Replacing a,d by zero then decreases
the displayed losses again. The resulting effects obey positivity at
alpha=eta=1/14 for 0<=j<=1. Thus a,d can be set to zero in the unrestricted
optimization, not merely in a convenient ansatz. It remains to minimize

    max(j/14-u+4w, sqrt(3)u+3j/28-2sqrt(3)w)             (6)

over that rectangle. A positive weighted average of the two affine
functions cancels w and is minimized at u=0. Their intersection at u=0
lies within the rectangle. Equivalently, along the intersection the loss
increases with u. Hence

    delta_natural=|j|(3-sqrt(3))/14,                     (7)
    u=0,     w=j(2-sqrt(3))/56,
    alpha=eta=1/14.

Relabeling every output by t_a->-t_a handles negative j. Formula (7) is an
exact optimum over all POVMs for these fixed inputs. It is not the optimum
over all qubit encodings in Section2. For j=1/2 it is about0.045284 of total
variation; the unrestricted-encoding lower bound (3) is about0.023381.

## 4. Positive higher-dimensional realizations

The rank bound for a d-dimensional carrier is d^2>=7, hence d>=3. This is
only a dimension lower bound. The following constructions establish more.

For |j|<=1/3, a qutrit suffices. Let G_1,...,G_6 be six traceless Hermitian
Gell-Mann matrices normalized by Tr(G_r G_s)=2delta_rs. Write G(t)=sum t_rG_r.
Its operator norm is at most its Hilbert-Schmidt norm sqrt(2)|t|<=sqrt(2).
Set

    epsilon=1/(3sqrt(2)),      d_j=3sqrt(2)j/28,
    rho_b=I_3/3+epsilon G(t_b),
    E_a=I_3/14+d_j G(t_a).                              (8)

The states have trace1 and are positive. The effects sum to I_3 and their
minimum eigenvalue is at least(1-3|j|)/14. Direct trace multiplication
gives Tr(E_a rho_b)=(1+j t_a dot t_b)/14. Thus the minimum carrier Hilbert
dimension is exactly3 for 0<|j|<=1/3 when parent disturbance is allowed.
No minimal-dimension claim is made for 1/3<|j|<1.

A four-dimensional carrier works throughout |j|<=1. Use an orthogonal
two-valued orbit register and one qubit:

    rho_A=|A><A| tensor (I+e_A dot sigma)/2,
    rho_B=|B><B| tensor (I+b_B dot sigma/sqrt(3))/2.

Define block-diagonal effects, listing their A and B register blocks,

    E_A=diag((I+j e_A dot sigma)/14, I/14),
    E_B=diag(I/14, (I+j sqrt(3)b_B dot sigma/4)/14).       (9)

They sum to identity; their nonconstant Bloch radii are |j| and3|j|/4,
so they are positive. Their probabilities are exactly (1). These are
ordinary disturbed-parent instruments, for example by square-root effects.
The register is an additional physical resource. Encoding a qutrit or
four-level carrier across fundamental qubits would require an explicit
spatial carrier, motion and capacity construction; (8)-(9) do not supply it.

There is a stronger exact statement if the carrier must also realize the
proper cubic rotations by a single projective unitary representation U_g,
with rho_(gb)=U_g rho_b U_g^dagger and E_(ga)=U_g E_a U_g^dagger.
Under that extra covariance condition the minimum carrier dimension is4
for every 0<|j|<1. The construction (9) is covariant with
U_g=I_orbit tensor u_g, where u_g is the usual spinor implementing the
proper rotation on Bloch vectors. The following argument rules out d=3
without assuming the qutrit states in (8).

The proper cubic group is S_4. Both triples e and b transform in its
three-dimensional rotation representation R. Since P acts as j/7 on
their direct sum, the equivariant preparation map from label coefficients
to Hermitian carrier operators must be injective on R+R. The conjugation
representation Ad(U) must therefore contain at least two copies of R.
If d=3, its remaining dimension is3; one dimension is the identity
operator. Write its character as 1+2chi_R+chi_W, with W of dimension2.

For reference the complete ordinary S_4 character table is below, on
classes identity, transposition, double transposition, three-cycle,
four-cycle (sizes1,6,3,8,6):

    1:       (1,  1,  1,  1,  1)
    sign:    (1, -1,  1,  1, -1)
    E:       (2,  0,  2, -1,  0)
    R:       (3, -1, -1,  0,  1)
    R sign:  (3,  1, -1,  0, -1).

These follow from the sign representation, the four-letter permutation
representation minus its constant, and the permutation of the three
pairings minus its constant. Character inner products verify irreducibility
and the squared dimensions sum to24. Thus every dimension2 W is E or a
sum of two one-dimensional characters.

At a transposition, the proposed Ad(U) character equals -1+chi_W(g).
It must equal |Tr U_g|^2>=0, including for a projective U. The only
dimension2 choice with chi_W(g)>=1 is two trivial characters. Thus
Ad(U) would have exactly three trivial components. Equivalently, the
complex commutant of U would have dimension3. Complete reducibility for
unitary representations of a fixed finite projective multiplier says this
dimension is the sum of the squared irreducible multiplicities. Dimension3
therefore forces three inequivalent multiplicity-one blocks. In total
carrier dimension3 each block must be one-dimensional. Three inequivalent
one-dimensional projective representations with the same multiplier cannot
exist: the ratio of any two is an ordinary S_4 character, and S_4 has
only two such characters. This is a contradiction. The d=1,2 cases were
already excluded by rank. No classification of all projective S_4 irreps
is needed for this argument.

## 5. Exact pure-parent permanence is a stronger interface

Suppose the parent carrier instead has a pure state |psi_b> for each
label b, and the whole fixed channel must return that same pure parent
state exactly. Its dilation factors on each input as

    V|psi_b>=|psi_b> tensor |z_b>.

For any nonorthogonal pair, preservation of the inner product gives
<z_b|z_c>=1 (up to consistent state phases), so their complementary
classical outcome laws must agree. Every two columns of P differ for
j!=0: F has column rank6, so T_.b=T_.c would imply t_b=t_c, contrary
to the fourteen distinct features. Hence all fourteen parent states must
be mutually orthogonal if the nonconstant marked birth law is implemented
with exact pure-parent preservation. The carrier dimension is then at
least14, attained by a fourteen-state classical pointer register with
the controlled stochastic law (1).

Four physical qubits can hold that many orthogonal code states, but this
dimension statement is not a mobile four-site record construction. It does
not apply unchanged to mixed-state permanence, quantum-only newborn
outputs, inaccessible hidden labels or a model outside ordinary quantum
instruments. It is the explicit operational bridge, not mobility alone,
that carries this obligation.

The higher-dimensional constructions certify probability kernels. In
particular, the qutrit construction has not supplied a unitary representation
of the spatial cubic group that acts on its encoded states; the preceding
argument shows that it cannot meet that additional covariance requirement.
The covariant four-dimensional realization remains a disturbed-parent
instrument and does not satisfy exact pure-parent permanence.

The principal consequence is that the new local-curl construction proves
compatibility of specified classical dynamics with kinematic Gauss and
propagating modes, while its particular fourteen-label native law still
needs a nontrivial physical qubit/record bridge. Neither the selected
alphabet nor the rank7 kernel is derived from the four minimal axioms.

## Literature and verification scope

Prepare-and-measure dimension tests are established quantum-information
machinery; see Gallego, Brunner, Hadley and Acin,
[Device-independent tests of classical and quantum dimensions](https://arxiv.org/abs/1010.5064).
The representation in their Eq.(1) and their distinction between uncorrelated
devices and shared preparation/measurement randomness were inspected. This
note uses the former representation and a nonlinear rank argument; it does
not import a device-independent bound valid under all shared resources.
The exact kernel and approximation constants above are this campaign's
application of that machinery, with no novelty claim for the general method.

`fourteen_label_quantum_check.py` checks all196 probabilities of both positive
carrier constructions, the rank/eigenspaces, a natural-encoding minimax
primal witness and reduced dual identity. Nine unrestricted qubit POVM
programs use all fourteen independent effects and reproduce (7); they do not
force cubic covariance or solve the variable-input-encoding optimization.
The full results, feasibility residuals and source identity are retained in
FOURTEEN_LABEL_QUANTUM_RESULTS.json. Numerical optima supplement the proof;
they do not establish the physical bridge or an independent review.
