# Physical boundaries and relative collision capacity

This is current supporting proof owned by `NATIVE_DILUTE_THERMODYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-30.md`,
under exactly its supplied full-qubit Hamiltonian and fixed positive mu,tau.
It has no separate claim classification or runner. The owner directly links
and binds it as a primary input. Its complete argument and interactions are
part of that one scientific unit. Equation numbers are local to each named
part below. Unsubscripted energy forms always use actual occupation amplitudes.

The actual [law and simultaneous gradient bound](NATIVE_QUBIT_PAIR_DENSITY_ONSET_BOUNDED_THEOREM_NOTE_2026-09-30.md) and
[physical threshold completion](NATIVE_FOUR_PARTICLE_THRESHOLD_BOUNDED_THEOREM_NOTE_2026-09-30.md) are the source inputs.
Part I constructs positive physical cells with a priced boundary penalty,
an exact guarded physical compression and a complementary gap. Part II
retains the full matching core and nonmatching self-energy in an auxiliary
relative Neumann capacity. The latter is an N4 theorem; it is never used as
an unpriced all-particle row allocation. Its scalar Neumann estimate and
actual high-component analysis also support the cell residual proof.

# Part I. Physical cells, spectator pins and complementary gap

## 1. Actual lower cells and the comparison penalty

Use the unchanged supplied qubit Hamiltonian and its simultaneous identity

 H=S+W+mu D,       S+W >= a Egrad15,       a=min(tau,mu/12)>0.

For a physical vertex cube Lambda={1,...,ell}^3 retain every complete
positive S/W row whose entire physical support lies in Lambda. Denote the
forms by S_Lambda,W_Lambda. Retain complete internal bare-pair difference
rows in Egrad15,Lambda. For x in Lambda let q_x be the number of actual
18-neighbors outside Lambda, m_int the occupied-neighbor count inside, and

 d_Lambda(x)=n_x min_(0<=j<=q_x) [(m_int+j-1)(m_int+j-2)/2].       (1)

This is the safe nonnegative diagonal. The only difference
from the literal internal phi(m_int) is removal of its isolated-site penalty
when q_x>0. Define the width-two boundary set

 partial Lambda={x:q_x>0},       N_partial=sum_(x in partial Lambda)n_x.

For 0<eta<=1/2, gamma>0 set

 H_Lambda^base=(1-eta)(S_Lambda+W_Lambda)
                 +eta a Egrad15,Lambda+mu sum_x d_Lambda(x),
 H_Lambda^+=H_Lambda^base+gamma ell^-2 N_partial.                  (2)

All forms act on the actual physical cell tensor product. The added term
is a comparison penalty, not an altered model premise.

On a torus with L divisible by ell, average all translations of a disjoint
cube tiling. The simultaneous comparison and positive-row deletion give
H>=sum_cells H_Lambda^base for every tiling. A site is in the boundary of
its cell for at most the fraction

 p_ell=1-(ell-4)^3/ell^3 <=12/ell,       ell>=4.

Indeed the graph has axial displacements of length two. Hence the exact
operator comparison after translation averaging is

 H >= average_translations sum_cells H_Lambda^+
                                  -12 gamma N/ell^3.             (3)

There is no IMS localization of the state, boundary energy deletion or
assumption about the state on the boundary. Equation(3) holds for coherent
states and arbitrary particle-number distributions. Nondivisible torus
remainders are not included in this assertion; the thermodynamic sequence
can be chosen divisible by each fixed ell.

## 2. A boundary-aware physical spectator pin

Use unique forward edges d=2e_i,e_i+/-e_j and let

 Omega_d(Lambda)={x:x,x+d in Lambda}.

Each is a rectangular anchor domain. For a nine-component field f on these
domains let

 J_Lambda(f)=Egrad9,Lambda(f)+S_Lambda(f)/mu.                      (4)

All S rows are the literal centered singlet/plane rows rewritten in forward
coordinates; no omitted component is replaced by a constant. The internal
fifteen-gradient form dominates the nine-gradient form by the actual axial
translations and duplicate plane representations. Since eta a<=(1-eta)mu,

                 H_Lambda^base >= eta a J_Lambda.                (5)

Fix R>=4 and r=R+6. Assume ell>=2r+1. For y in Lambda set
B_y=Lambda intersect (y+[-r,r]^3), a rectangular vertex box whose side
lengths lie between r+1 and 2r+1. On its valid edge-anchor domains impose
f(e)=0 for every edge incident to y. There exists a finite C_pin(R),
independent of ell,y, such that

 sum_(e subset B_y)|f(e)|^2 <= C_pin(R) J_(B_y)(f).                (6)

Here J_(B_y) retains only complete rows inside that physical vertex box.
The estimate includes face, edge and corner positions of y.

To prove(6), first determine the exact finite-dimensional zero space. If
J_(B_y)=0, every component is constant on its connected rectangular anchor
domain. Complete interior S rows then put the nine constants in range U,
the actual five-dimensional constant soft space. There is at least one
edge incident to y of each axial type: in each coordinate at least one
side has length at least r, so a displacement of either +2 or -2 is valid.
These three pinned axial rows of U kill both E components. For each plane
ij choose signs sigma_i,sigma_j for which y+sigma_i e_i+sigma_j e_j lies
in B_y. Its edge is of one of the two forward plane types. The corresponding
row of U has magnitude1/sqrt2 in that plane's T column, and pins that
component. Thus all five soft constants vanish. There are only finitely
many possible box shapes and marked positions at fixed r, up to translation
and axis permutation. Take C_pin(R) to be the largest reciprocal smallest
eigenvalue of their pinned J matrices. Every one is strictly positive by
the preceding kernel proof. This is a finite, exact definition of a constant;
no numerical eigenvalue, favorable estimate or uniform-in-R bound is claimed.

For a physical vector psi and an output occupation eta_occ define the
literal removal amplitudes

 f_eta_occ(e)=<eta_occ|b_x b_(x+d)|psi>.

They vanish whenever e meets eta_occ. Every actual J row norm is the sum
of its amplitude-row norm over eta_occ. If an occupied removed edge has a
spectator y at distance <=R, it is contained in B_y and has the pins in(6).
Summing (6) over these spectators and output configurations gives

 <E_R^near> <= C_R J_Lambda(psi),
 C_R=C_pin(R)(2r+5)^3,                                          (7)

where E_R^near counts occupied graph edges having another occupied site
within Chebyshev distance R of either endpoint. To check incidence, a fixed
row can occur only for y within r+2 of one of its fixed anchors; there are
at most(2r+5)^3 such physical sites, irrespective of the particle number.
Each removal edge with at least one close spectator is included at least
once. No removal fiber is independently minimized, and all amplitudes in
this sum come from the same physical psi. Equation(7) is an operator-form
inequality by this literal amplitude decomposition.

Let B_R count particles outside R-isolated graph dimers, with isolation
measured only against other sites of Lambda. Every bad particle with a
graph neighbor belongs to an edge counted by E_R^near: a connected graph
component with at least three vertices has a third vertex within distance
two of an endpoint of each edge; a two-vertex component which is not isolated
has the close spectator by definition. Isolated singletons are charged to
d_Lambda unless they lie in partial Lambda. Thus pointwise

 B_R <= sum_x d_Lambda(x)+N_partial+2 E_R^near.                   (8)

This separates the free boundary singleton count from the nearby-edge
energy estimate. Charging all guard errors to B_R would lose this separation
and would unnecessarily introduce a factor ell^2 from the penalty.

## 3. Guarded rows, with no boundary-singleton loss

Fix an integer R0>=14 once and for all. For valid edges use the same actual
isolated-pair selection as on the torus, but only inside Lambda. The map
I sends a physical occupation to its set of selected isolated graph edges
in auxiliary bosonic Fock space and its complete remaining site occupation
in an environment register. Recovering the original occupation by union
proves that I is an isometry. Removing a selected edge does not change any
remaining selection or the environment, so guarded annihilation intertwines
exactly with auxiliary edge annihilation. Creation is not assumed to do so.

In an output occupation eta_occ the guard is
q(e)=1_{dist(e,eta_occ)>R0}. For every complete internal J row l, choose an
edge e0 in that row. The elementary row estimate is

 |sum_e l_e q_e f_e|^2
 <=2|sum_e l_e f_e|^2+2||l||^2 sum_e |q_e-q_e0| |f_e|^2.          (9)

The row diameter is at most four in edge Hausdorff distance. Unequal guards
therefore imply that the input edge has a spectator within R0+4. The
weighted row incidence is at most fifteen: twelve from gradients, at most
three from the actual S rows. Missing boundary rows only decrease it.
Combining(7),(9) yields, uniformly in particle number and ell,

 J_guard <= D_R0 J_Lambda,
 D_R0=2+30 C_(R0+4).                                            (10)

No boundary particle count appears in(10). The local pin proof is applied
to actual boundary-truncated boxes. In particular this estimate cannot be
obtained by extending every field by zero and silently restoring lost rows.

## 4. The actual five open-cell soft modes

Let F_ell be the five-dimensional subspace of fields
f_d(x)=U_d z on all x in Omega_d. Its Gram matrix is

 G_ell=sum_d |Omega_d| U_d^* U_d,
             (ell-2)^3 I5 <= G_ell <= ell^3 I5.                  (11)

The normalized embedding is W1:z -> (U_d G_ell^-1/2 z)_d,x.
This uses the true orientation-dependent anchor counts. It is not the
periodic normalization ell^-3/2 U.

The internal one-body form J_Lambda satisfies

 dist(f,F_ell)^2 <= C_s ell^2 J_Lambda(f),                        (12)

with a numerical constant C_s, for all sufficiently large ell. Here is an
elementary derivation. Subtract the separate mean m_d on each rectangular
Omega_d. Scalar Neumann Poincare bounds the remainder q by
||q||^2<=ell^2 Egrad9/4. On a common interior cube, all constant-component
S rows are present and their constant form is2||P_high m||^2 per center.
The number of such centers is at least(ell-4)^3. The complete infinite S
symbol is bounded by2mu, so zero-extending q for this estimate gives
S_inner(q)<=2mu||q||^2. The square triangle inequality bounds
(ell-4)^3||P_high m||^2 by S_Lambda(f)/mu+2||q||^2. Approximating f by the
constant field U U^*m then proves(12), for example with C_s=64 when ell>=8.
The zero extension here is only an upper bound on the error's retained S
rows; it adds no row to the physical lower Hamiltonian.

Let Exc be the auxiliary number outside F_ell. Literal guarded removal and
(10),(12) imply on physical states

 I^* Exc I <=64 ell^2 D_R0 J_Lambda.                             (13)

## 5. An actual physical compression gap, including all environments

Work in the physical sector N=2n. Let W_n embed Sym^n C5 into the auxiliary
Fock space with all n pairs in F_ell and empty environment. Put

 T_n=I^* W_n,       G_n=T_n^*T_n.

The image of I with empty environment consists exactly of edge occupations
whose n edges are distinct and pairwise R0-isolated. A forbidden pair of
edges has at most C_b(R0) choices of its second edge given its first. By(11),
the compression to F_ell of the indicator of any such collection has norm
at most C_b/(ell-2)^3. Condition on the first edge, then sum its exact
one-body evaluation resolution of identity. The pair union bound on an
arbitrary symmetric n-mode vector gives

 G_n >=(1-delta_n) I,
 delta_n=binom(n,2) C_b(R0)/(ell-2)^3.                            (14)

This includes repeated auxiliary edge occupation and shared-site conflicts;
it is not a classical product-state estimate. A safe explicit choice is
C_b(R0)=18(2R0+9)^3, since either endpoint of the second edge must lie in a
bounded neighborhood of an endpoint of the first. No sharp constant is used.

Assume delta_n<1. Define the physical isometry
V_n=T_n G_n^-1/2 and P_n=V_n V_n^*. Its rank is binom(n+4,4).
On the auxiliary fixed physical-number space the complement of the
all-soft/empty-environment subspace is bounded by N_environment+Exc.
Using(8),(13) and the positive terms in(2) yields

 I-T_n T_n^* <= C_gap ell^2 H_Lambda^+,
 C_gap=1/mu+[2 C_R0+64 D_R0]/(eta a)+1/gamma.                    (15)

The right side follows term by term; constants are deliberately not sharp.
Since T_n T_n^*<=P_n,

 H_Lambda^+ >= Delta_ell (1-P_n),
                    Delta_ell=(C_gap ell^2)^-1.                 (16)

This is an operator inequality on the full physical N=2n sector, with all
bad environments retained. For odd N the all-soft/empty-environment space
is absent, so the same argument gives H_Lambda^+>=Delta_ell. The constants
are independent of N, ell and the state. Equation(16) is not an assertion
that P_n is an invariant eigenspace or that H_Lambda^+ annihilates it.

## 6. Compatible trial bound and a genuinely physical finite Schur operator

Every occupation contributing to T_n consists of isolated actual graph
edges, so its diagonal d_Lambda energy is zero. For a remaining selected
(n-1)-edge occupation eta_occ the removed-edge amplitude before guarding is

             U_d G_ell^-1/2 v_eta_occ,
             sum_eta_occ ||v_eta_occ||^2 <= n.

This is the literal auxiliary annihilation identity, not independent
optimization of the removal amplitudes. Every complete S/W/gradient row
annihilates these constant soft amplitudes before the guard is applied.
A nonzero guarded row lies within a fixed shell of one of the2(n-1)
remaining occupied sites. The number of such rows is at most C(R0)(n-1),
with bounded row coefficients, while(11) supplies an ell^-3 squared-amplitude
factor. Thus for a fixed finite C_t=C_t(mu,tau,R0), independent of eta<=1/2,

                T_n^* H_Lambda^base T_n
                   <= C_t n(n-1)/ell^3 I.                        (17)

The boundary penalty has a separate direct price. Its compression to the
five soft modes is bounded by C_partial/ell per pair, because at most
C ell^2 valid edges have an endpoint within the width-two boundary and
G_ell>=c ell^3 I. Restricting to the diagonal isolated-edge image decreases
this positive diagonal observable. Consequently

 T_n^* H_Lambda^+ T_n
       <=[C_t n(n-1)+C_partial gamma n]/ell^3 I,
 V_n^* H_Lambda^+ V_n <= theta_n I,
 theta_n=[C_t n(n-1)+C_partial gamma n]/[ell^3(1-delta_n)].         (18)

For theta_n<Delta_ell, min-max and(16) put exactly binom(n+4,4) physical
levels below Delta_ell. Writing Q_n=1-P_n, the actual complement compression
C_n=Q_n H_Lambda^+ Q_n satisfies C_n>=Delta_ell Q_n. The finite physical
Schur matrix is therefore well defined:

 S_n,ell=V_n^*H_Lambda^+V_n
       -V_n^*H_Lambda^+Q_n C_n^-1 Q_nH_Lambda^+V_n.               (19)

Block Gaussian elimination gives, for ordered low eigenvalues lambda_j and Schur eigenvalues s_j,

 lambda_j<=s_j<= [1+theta_n/(Delta_ell-theta_n)]lambda_j.          (20)

This is applied to the physical open-cell operator(2), not imported from a
periodic spectrum. One may verify(20) by eliminating Q at spectral parameter
lambda, comparing C_n^-1 with(C_n-lambda)^-1, and using positivity of the
zero-parameter block Schur complement and V_n^*H V_n<=theta_n.


# Part II. Full-channel relative Neumann capacity

## 1. Statement with physical normalization

Fix mu,tau>0 and a=min(tau,mu/12). Let H4 be the actual bounded positive
Hamiltonian on unordered four-site translation orbits in Z^3, with one
amplitude per orbit. This is the checked total-momentum-zero fiber, not
an assertion that an infinite-volume center-of-mass plane wave is in l2.
Use the nine unique forward graph edges and the real9 by5 isometry U from
the physical threshold construction. Its normalized pair coefficients
include the1/sqrt2 factor on the original T triplet.

There is a finite physical collision core and an exact matching-coordinate
isometry J described below. For Lambda_R={r:|r|_infinity<=R}, v_R=|Lambda_R|,
define on the physical N4 fiber

 M_R psi=(1/(sqrt2 v_R)) sum_(r in Lambda_R)
                              U^T (J P psi)(r) U.                 (1)

P is the actual perfect-matching projector. Exchange makes(1) a symmetric
complex5 by5 tensor, with its Hilbert--Schmidt norm. In particular

                   ||M_R||^2<=1/v_R.                              (2)

The relative-capacity statement is that for sufficiently large R there is an explicit
finite-core matrix T_R on this full15-dimensional space satisfying

 H4 >= M_R* T_R M_R,
 ||T_R-T0|| <= C (log R)^(-4/9),                                  (3)

where T0 is the ACTUAL full physical zero-energy threshold form. Constants
depend on mu,tau and the fixed core, not R. The construction involves the
exact infinite nonmatching inverse and so does not claim computable matrix
entries from a finite enumeration alone. It is nevertheless an explicit
operator/variational definition with a finite-dimensional reduction.

Since T0>=2a/g I15>0 at the physical normalization of the threshold input,
where g=integral ell(k)^-1 dk/(2pi)^3, equation(3) implies for every eta>0
and all sufficiently large R

                 H4 >= (1-eta) M_R* T0 M_R.                        (4)

This is a lower form involving a coherent mean amplitude, not a diagonal
pair-distance potential. Its mean operator has rank15 for large R and
scale v_R^-1. It is a possible two-pair input for a subsequent replacement
argument, not that many-particle replacement itself.

## 2. Exact physical P/Q Schur reduction

The underlying Hamiltonian is the full qubit law

 H=S+mu Ddiag+W,
 Ddiag=(1/2)sum_x n_x(m_x-1)(m_x-2),

with the exact collective S/W rows and all18 original graph neighbors.
The landed simultaneous comparison is H>=mu Ddiag+a Egrad15. Let P select
four-sets whose graph has a perfect matching and Q=1-P. A four-vertex graph
without a matching either has an isolated vertex or, in the absence of an
isolated vertex, is a three-leaf star. In either case Ddiag>=1. Hence

 C=QH4Q>=mu Q,
 h=P H4 P-P H4 Q C^-1 Q H4 P>=0.                                (5)

The inverse in(5) is the bounded inverse on the actual complete nonmatching
l2 space. It is not replaced by a scalar denominator or a finite box inverse.
For every compact physical vector psi=p+q, completion of the Q square gives

 <psi,H4 psi>=<p,h p>
       +||C^(1/2)(q+C^-1 Q H4 P p)||^2.                          (6)

The matching side of P H4 Q is supported in a fixed finite collision core.
Indeed every offdiagonal move annihilates a graph edge and creates another
edge in a uniformly bounded neighborhood. If the untouched residual pair
were itself a graph edge, the input would already have a perfect matching.
Otherwise an output perfect matching must pair the residual vertices across
the newly created local pair. All four vertices are then at bounded mutual
distance. The same conclusion holds for the reverse move. Thus the Schur
term in(5) is a finite matrix on matching core coordinates, despite using
the full infinite Q inverse. No all-N nonmatching gap is asserted.

## 3. Physical core constraints in the ordered exchange carrier

Represent two graph edges as {0,d} and {r,r+e}, with d,e forward types.
Use the exchange space

 F_de(r)=F_ed(-r),
 ||F||_ex^2=(1/2)sum_(r,d,e)|F_de(r)|^2.                         (7)

A matching four-set S with m(S) perfect matchings has exactly2m(S) distinct
ordered representations. There is no nontrivial translation stabilizer of
a finite nonempty subset of Z^3. Put its physical amplitude divided by
sqrt(m(S)) in each representation. Forbidden shared-site representations
receive zero. This defines the exact isometry J from P l2 into(7).

Outside a finite collision core, the matching is unique and every ordered
coordinate represents four distinct sites. All restrictions on the range
of J are therefore finite core constraints: zeros at overlaps and equality
relations among the weighted representations of multiply matched four-sets.
Let B=range J and D_B=1-JJ*; D_B is a finite-rank orthogonal projection
supported in that core. No arbitrary ordered field is identified with a
physical state in the core.

For separated dimers the exterior law is the sum of the two true N2 edge
Hamiltonians. Write K(k) for the exact nine-bond symbol. It obeys

 K(k)>=a ell(k)I9,  ell=4 sum_i sin^2(k_i/2),
 ker K(0)=U C5,  K(0)|_(U C5)^perp=2mu I4.

For reference, its axial block is2mu P_v+tau ell(I-P_v),
v_i=exp(-ik_i), P_v=v* v/3. In plane ij, with eta=+/-1,
q_eta=-eta[exp(-i eta k_j)+exp(-ik_i)]/2 and
K_ij=2mu I2+(tau ell-mu)q* q. These are the actual free S/W rows, not a
scalar surrogate. A consistent relative-anchor convention gives

 L(k)=K(-k) tensor I9+I9 tensor K(k),
 L>=2a Delta I81.                                                (8)

Reversing the relative-anchor convention swaps the two k signs. All
subsequent definitions use the actual row action in one fixed convention.
The constant soft subspace before exchange has dimension25; exchange
restricts its constant tensors to Sym^2 C5, dimension15. Its vectors are

                  t_A(r)=sqrt2 U A U^T.                          (9)

The one-half norm in(7) makes the squared norm per relative volume of t_A
exactly ||A||_HS^2. This fixes the normalization in(1)-(4).

Extend the exact Schur form to the full exchange space only by

        Hext=J h J*+mu D_B=L+Pi_K* V Pi_K.                        (10)

Here K is a sufficiently large fixed symmetric relative cube containing
the constraint core, every modified row/column and the Schur coupling
support, and Pi_K is restriction to K. V is a finite Hermitian core matrix.
Equality to L off that core follows from the separated-dimer law. The
extension mu D_B is bookkeeping on forbidden coordinates. Every physical
capacity below imposes Pi_K f in the allowed subspace, so this extension
vanishes there and does not change the law or the threshold value.

## 4. Homogeneous coercivity from actual compact-source duality

This step controls the negative core self-energy. Positivity of T0 alone
would not suffice. The [physical threshold proof](NATIVE_FOUR_PARTICLE_THRESHOLD_BOUNDED_THEOREM_NOTE_2026-09-30.md) establishes the compact-source inequality
that for every compact physical source r,

                    |<r,psi>|^2<=C(r)<psi,H4 psi>.                 (11)

It follows from the simultaneous unscaled ordered-removal gradient and
mu Q comparison; the2m matching multiplicity is included in its source
lift. Thus every fixed physical coordinate is continuous in energy norm.
It applies to l2 vectors as well, since H4 is bounded and compact vectors
are dense there.

For a compact p in P, take the exact minimizing q=-C^-1 QH4P p in(6).
Equation(11) bounds every physical matching core coordinate of p by a
constant times <p,hp>. Under J, each ordered core coordinate is a fixed
multiple of one such p coordinate. For a general compact exchange vector
f=Jp+z, z in range D_B, equation(10) gives

 E_ext(f)=<p,hp>+mu||z||^2,
 ||Pi_K f||^2<=C_K E_ext(f).                                     (12)

All norms on the exchange core use the same one-half measure. The constants
are finite sums of the explicit C(r) from(11) and a finite multiple of1/mu.
There is no sum over infinitely many relative positions in C_K.

Using(10),(12),

 E_L(f)<=E_ext(f)+||V||||Pi_K f||^2
        <=(1+||V||C_K)E_ext(f).

Conversely, free three-dimensional point-source duality from(8) gives
||Pi_K f||^2<=C'_K E_L(f). Therefore for some c0,C0>0,

                  c0 E_L <= E_ext <= C0 E_L.                      (13)

These inequalities extend to the homogeneous free energy completion.
It has a faithful l6 representative from the discrete Sobolev inequality
and(8). Equation(13) proves equivalence of the completions and excludes
an unpriced homogeneous zero-energy pole, including in the core. It is
stronger than merely asserting that the incoming threshold is positive.
The value of c0 may be very small, but it is fixed at fixed mu,tau and core.

## 5. Regularized relative Neumann form and its true kernel

Let R be large enough to contain K well inside Lambda_R. Restrict every
complete positive free L row whose support is inside Lambda_R; denote
the resulting form L_R^row. This retains the literal two-bond S/W row
structure, including high components. Define, for0<theta<=1/2,

 L_(R,theta)=(1-theta)L_R^row+2a theta Delta_R I81,                 (14)

where Delta_R is the internal-edge Neumann scalar gradient. Both row
families respect the exchange involution because the cube is symmetric.
Their infinite-volume counterpart is

                  L_theta=(1-theta)L+2a theta Delta I81.

It satisfies (1-theta)L<=L_theta<=L and L_theta>=2a Delta.
The finite form has no assumed high-component boundary gap. Instead its
explicit theta gradient forces every zero vector to be spatially constant.
The retained interior S rows then force its constant value into ker L(0).
Exchange leaves exactly the15 constant fields(9), with no other kernel.

There is a uniform Neumann Sobolev estimate

 ||f||_6 <= C theta^(-1/2) E_(R,theta)(f)^(1/2),
                  f perpendicular to the constant soft kernel.  (15)

To verify it, decompose f=m+q, where q has zero spatial mean. A reflected
extension and cutoff, followed by the infinite discrete Sobolev inequality
and the Neumann Poincare inequality, give ||q||_6<=C||gradient q||_2.
The explicit gradient in(14) bounds this by C theta^-1/2 E^1/2.
Orthogonality to the kernel gives P_soft m=0. The interior S rows applied
to the constant m have energy proportional to their volume times
<m,L(0)m>, with high gap2mu. Applying the square triangle inequality to
those rows on m=f-q gives

 |Lambda_R||m|^2<=C E_(R,theta)(f)+C||q||_2^2.

Multiply by R^-2 and use Poincare again. Since the squared l6 norm of the
constant m is comparable to R|m|^2, this proves(15). Constants are uniform
in R and theta<=1/2 apart from the displayed theta^-1/2. No diagonalization
of the matrix symbol or boundary high-mode assumption is inserted.

The scalar Sobolev ingredient can be established by the discrete BV
inequality ||g||_(3/2)<=C sum_i||D_i g||_1, telescoping along three coordinate
directions and applying Cauchy successively. Apply it to |f|^4, then Holder,
to obtain ||f||_6<=C||gradient f||_2. Reflection/Poincare supplies its
mean-zero Neumann version. The same proof works for the finite81-component
norm; its fixed dimension can also be absorbed into C.

## 6. Finite-core Green convergence with an explicit theta cost

On the finite exchange space let L_(R,theta)^+ have its15-dimensional
kernel removed, and set

 G_(R,theta)=Pi_K L_(R,theta)^+ Pi_K*,
 G_theta=Pi_K L_theta^-1 Pi_K*,
 G0=Pi_K L^-1 Pi_K*.                                             (16)

Infinite inverses in(16) mean compact-source energy inverses. Their matrix
entries are finite by(8), not by a bounded inverse on all l2. The exchange
core carries the one-half measure, so Pi_K* is zero extension in that
measure. All matrices act on that exact core space.

G0 is positive definite: a nonzero compact core source has a nonzero
Fourier polynomial, and its inverse-form integral is strictly positive.
The finite trace map from the mean-soft-zero subspace onto the core is
surjective for large R. Prescribe any exchange-compatible core values and
cancel their soft mean by a constant soft field outside K. Thus G_(R,theta)
is also positive definite. The bounds on L_theta give

                  G0<=G_theta<=(1-theta)^-1 G0.                   (17)

Choose an even radial cutoff chi equal to1 through R^(1/4), zero beyond
R^(1/2), and linear in log radius in between. For large R it equals1 on K
and is supported well inside Lambda_R. Direct shell summation gives

                  ||gradient chi||_3<=C(log R)^(-2/3).            (18)

For each bounded-range row B, choose one of its anchors and expand
B(chi f)=chi_anchor Bf+[B,chi]f. Bounded row incidence and Holder give

 sum_rows ||[B,chi]f||^2<=C||gradient chi||_3^2||f||_6^2.

All nonzero cutoff rows are genuinely interior. With(15), a finite
mean-soft-zero f therefore has

 E_(infinity,theta)(chi f)<= (1+k_R)^2 E_(R,theta)(f),
 k_R=C theta^-1/2(log R)^(-2/3).                                 (19)

Apply the compact-source variational principle to
f=L_(R,theta)^+ Pi_K* q. Its source pairing is unchanged by chi. This yields
<q,G_(R,theta)q><=(1+k_R)^2<q,G_theta q>.

For the reverse comparison start with u=L_theta^-1 Pi_K* q. Its infinite
l6 bound is uniform in theta because L_theta>=2a Delta. Cut it by chi and
subtract its constant soft mean on Lambda_R. This projection changes no
finite Neumann energy and preserves exchange. Its source pairing changes
by at most

 C||q|| R^-3 ||chi u||_1
   <= C||q|| R^-3 (R^(3/2))^(5/6)||u||_6
   <= C R^(-7/4)||q||^2.                                       (20)

The infinite cutoff energy cost is1+C(log R)^(-2/3), independently of
theta. Optimizing the finite variational principle and using the uniform
positive lower eigenvalue of G_theta>=G0 shows the reverse inequality
with error C[(log R)^(-2/3)+R^(-7/4)]||q||^2. Together with(17)-(19),

 ||G_(R,theta)-G0||
 <=C[theta+theta^-1/2(log R)^(-2/3)
                  +theta^-1(log R)^(-4/3)+R^(-7/4)].              (21)

This is a matrix estimate for every complex core source, including all
high components and collision coordinates. It is not a scalar Green
substitution. No exterior normal-mode formula is assumed.

## 7. Constrained capacity and the actual full T0

Let D be the allowed core subspace, the restriction of range J to K.
All its finite relations and zeros are retained; K contains every ordered
representation of each constrained physical orbit. Let B:D->core be its
isometric inclusion, and let t_K(A)=Pi_K t_A. Define the finite capacity
as the minimum of

 E_(R,theta)(f)+<Pi_K f,V Pi_K f>

over exchange fields f with soft mean t_A and Pi_K f in D. Subtracting the
constant field t_A leaves a vector perpendicular to the finite kernel.
For any prescribed core value w=Pi_K f, the minimum free energy is

              <w-t_K,G_(R,theta)^-1(w-t_K)>.

This is the usual finite-source Riesz minimization in the specified Hilbert
measure, and follows directly by solving the trace constraint with
L_(R,theta)^+ Pi_K* G_(R,theta)^-1. Thus the capacity has the exact finite
matrix expression

 T_(R,theta)[A]=<t_K,[G^-1-G^-1 B
             (B*(G^-1+V)B)^-1 B*G^-1]t_K>,
                              G=G_(R,theta).                     (22)

It remains to justify the inverses and the infinite limiting identification.
For any homogeneous free field with prescribed core trace w, minimize the
free energy first. Equation(13) then implies

                  G0^-1+V >= c0 G0^-1 >0.                        (23)

This supplies a strict finite-dimensional margin against the exact negative
self-energy. For small theta and sufficiently large R, (21) preserves that
margin, so every inverse in(22) exists uniformly. It also makes(22) locally
Lipschitz in G. This does not follow from positivity of T0 alone.

At G=G0, the same formula is the infimum of the infinite form L+V over
f=t_A+v, v in its homogeneous energy completion, with core trace in D.
The actual incoming Phi_A obeys J Phi_A=t_A+k_A, where k_A is compact:
it corrects precisely the overlaps and multiple-matching core. Consequently
the constraint on f is equivalent to physicality of the matching correction
v-k_A. By(13), this physical correction belongs to the exact matching
Schur energy completion, and conversely every such matching correction
gives an allowed v. Completing the unchanged Q square supplies its unique
minimizing Q correction in l2: QH4P has finite matching-core support, so
it acts continuously on the faithful energy-completion coordinates. The
identification follows first for compact corrections and then by energy
density and this core continuity. Therefore the infinite constrained minimum
is exactly the original physical threshold infimum, namely T0[A]. It is
neither a relaxation of the core constraints nor a projected two-dimer model.
The arbitrary positive extension on D_B vanishes on every admitted f.

Combining(21)-(23) gives the same error bound for
||T_(R,theta)-T0||. Choose theta_R=(log R)^(-4/9), once R is large enough
that it lies below1/2 and the coercivity threshold in(23). The first two
errors in(21) are both O((log R)^(-4/9)); the remaining terms are smaller.
Set T_R=T_(R,theta_R). This proves the convergence in(3), with
all15 channel normalizations intact. Finite R need not preserve every
physical cubic rotation in the forward-anchor convention; exchange and the
full limiting physical T0 are what the argument requires.

## 8. Actual N4 lower form and its domain

For a compact physical psi, apply(6) and put f=J P psi. The global free
comparison in(8) and positive-row deletion imply

 E_L(f)=(1-theta)E_L(f)+theta E_L(f)
       >=(1-theta)E_R^row(f|Lambda_R)
                         +2a theta Egrad_R(f|Lambda_R).

The core term V is unchanged. The restricted field satisfies every actual
core constraint and has mean t_(M_R psi). Its finite capacity is therefore
a lower bound, proving H4>=M_R* T_R M_R. Boundedness extends the inequality
from compact to l2 physical orbit vectors. Cauchy on the mean and J's exact
isometry prove(2). To see rank15 for large R, restrict J Phi_A=t_A+k_A to
the cube and extend by zero. It is a compact physical matching field and
its mean tensor is A+O(v_R^-1)A. This map is invertible for large R.

The comparison never removes actual neighbors from Ddiag. Q is eliminated
with its entire infinite operator before any relative boundary is imposed.
The scalar-gradient fraction uses the proved global FREE comparison(8);
it is not an assignment of that comparison to physical many-particle rows.
Nor is the relative cube a cell in the original spatial tensor product.
It bounds a coherent average of two-pair relative amplitudes in the actual
K=0 N4 fiber. No periodic seam or finite-N spectral limit was used.
