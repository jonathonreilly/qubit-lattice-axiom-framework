# A full-channel relative Neumann collision lower form

Author proof candidate. No independent check or formal grade is attached.
This is an N=4, zero-total-momentum result for the unchanged supplied qubit
Hamiltonian. It does not partition a many-particle state into physical
cells. The exact target and source boundaries were frozen in CONTRACT.md
before this derivation was written; no numerical job has been executed.

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

The candidate theorem is that for sufficiently large R there is an explicit
finite-core matrix T_R on this full15-dimensional space satisfying

 H4 >= M_R* T_R M_R,
 ||T_R-T0|| <= C (log R)^(-4/9),                                  (3)

where T0 is the ACTUAL full physical zero-energy threshold form. Constants
depend on mu,tau and the fixed core, not R. The construction involves the
exact infinite nonmatching inverse and so does not claim computable matrix
entries from a finite enumeration alone. It is nevertheless an explicit
operator/variational definition with a finite-dimensional reduction.

Since T0>=2a/g I15>0 at the previously checked physical normalization,
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
would not suffice. The checked physical compact-source inequality states
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
Set T_R=T_(R,theta_R). This proves the proposed convergence in(3), with
all15 channel normalizations intact. Finite R need not preserve every
physical cubic rotation in the forward-anchor convention; exchange and the
full limiting physical T0 are what the argument requires.

## 8. Actual N4 lower form and the exact remaining many-body obstruction

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

For all N, removal amplitudes have nontrivial spectator compatibility and
are not independent N4 K=0 profiles. A lift of(3) would need an actual
row/energy allocation controlling overlaps, spectator/environment effects
and center-of-mass variation. The known unrestricted N4 diagonal lift fails,
and the present proof neither repairs that lift nor pays its multiplicity.
Physical open cells also have boundary singleton sectors absent from this
auxiliary exchange-coordinate Neumann problem. Thus the full many-particle
T0 lower comparison, physical boundary packing and matching dilute EOS
remain open. Their solution is not hidden in a claimed capacity theorem.

## Current status

The construction is analytic and source-bound. No new numerical matrix,
threshold value or eigenchannel ordering has been computed. The physical
compact-source inequality, exact P/Q decomposition and true two-bond free
rows are the load-bearing earlier inputs; their identities are recorded in
SOURCE_AND_PRIOR.json. This complete new proof requires a cold adversarial
read and a separate focused check before substantial reuse. In particular,
the exact-core extension, the Neumann high-component estimate, the mean
normalization and the theta-dependent Green comparison must survive that
check. There is no formal review/audit or claim of historical novelty.
