# Finite-clock transfer disorder and a spectral-gap/perimeter bound

**Date:** 2026-09-14
**Status:** proposed_retained
**Claim type:** bounded_theorem

Actual current source status is conditional-support. Independent scientific
review is pending; author calculations do not grant retention.

This note proves two conditional bridges. First, a temporally twisted finite
Euclidean transfer has a weighted disorder insertion, and an explicit
perimeter cost converts it into a unitary membrane shift. Second, if linked
unitary loops have a product expectation at least exp[-s L+o(L)], their exact
Weyl algebra and a local change of Hamiltonian at the membrane boundary imply

    Delta <= e mu v s/(mu kappa-s), when mu kappa>s.

Here Delta is a putative uniform positive spectral gap, mu and v are valid
Lieb-Robinson constants, and boundary separation is at least kappa L-o(L).
The spectral-filter proof also states its ground-sector hypothesis. It rules
out a positive gap for s=0. Positive fixed perimeter coefficients give a
positive upper bound, with no massless-photon conclusion. The theorem does
not join perimeter bounds from one model to locality from another.

**Primary:** [input-free runner](../scripts/finite_clock_transfer_disorder_and_spectral_gap_perimeter_2026_09_14.py).
**Receipt:** [canonical cache](../logs/runner-cache/finite_clock_transfer_disorder_and_spectral_gap_perimeter_2026_09_14.txt).
**Author checks:** [review history](../.claude/science/physics-loops/toe-charged-phase-20260914/deliveries/block12/REVIEW_HISTORY.md).

## Target, quantifiers and supplied data

The target is the collective phase obligation left open by the
[finite-clock tame Maxwell bridge](U1_FINITE_CLOCK_GAUGE_MATTER_AND_CONTROLLED_TAME_MAXWELL_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md).
That source constructs finite Weyl carriers and controlled reduced tame
oscillators; it does not establish a many-link thermodynamic photon phase.
Its pure-gauge Hamiltonian matches the one below with clock order N,
dA=2pi/N, t=g²/(2dA²), and magnetic coupling K=1/g². The target note uses K
for clock order; this note uses N for order and K for magnetic coupling.
Holding g fixed makes t depend on N, so a bound uniform in clock dimension
at fixed t,K does not imply a uniform bound on that different trajectory.

N, the nontrivial phase omega, and all couplings are fixed while L tends to
infinity. The asymptotic theorem applies either to a single ground-state GNS
representation with arbitrarily large finite loop operators, or to growing
finite volumes with a uniform gap and all stated bounds uniform in volume.
A separate finite-volume gap Delta_L may obey the finite inequality without
being bounded below as L grows. The geometric checks are on an unwrapped
cubic lattice embedded in a sufficiently large box, away from boundaries.

| Supplied premise | Proven consequence | Open join |
|---|---|---|
| Positive finite-clock temporal weights and their Fourier coefficients | Positive physical transfer and exact disorder source map | Quasilocal logarithm and a thermodynamic phase |
| Local electric-plus-plaquette clock Hamiltonian | Membrane deformation lives at its boundary; volume-uniform LR bounds | Both ground-state loop expectation lower bounds |
| Exact linking algebra, separated boundary deformation and controlled ground projection | Conditional gap/perimeter inequality | A route making the cost subperimeter, or quantitatively strong enough |
| Scalar Wilson compression on the ground sector, or sufficiently small leakage | One-filter proof even with ground degeneracy | Verify that property in the actual chosen phase |

No axiom, approved primitive, empirical parameter or editable prompt changes.
The construction supplies a mathematical clock model and a representation of
its ground state; it does not derive these from native Records.

## 1. Exact fixed-step transfer and the unitary disorder observable

The singular continuous-time limit is a requirement of the chosen clock
Hamiltonian route, not one of the foundation's axioms. A fixed positive
Euclidean transfer provides a different conditional model. Its exact source
map can be derived without claiming that its logarithm is spatially local.

On a finite oriented spatial cell complex let a in Z_N^E be the link variables,
d the cellular coboundary, and

    M(a)=exp[S_s(a)], S_s(a)=beta_s sum_p cos[2pi(da)_p/N].

Let K0(a,b)=product_l w_tau(a_l-b_l), with positive w_tau and strictly positive
Fourier coefficients (Wilson at positive beta_tau and periodic heat kernels
have this property). Let P_G average site gauge transformations. K=K0 P_G
is positive definite on the gauge-invariant space. The symmetric physical
transfer is T=M^(1/2) K M^(1/2), so T is self-adjoint and strictly positive
there. In finite volume H=-log(T/lambda_max(T)) exists and is nonnegative.
This does not prove a volume-uniform quasilocal interaction for H, nor a
thermodynamic phase. The full Hilbert-space transfer has a kernel on
nonphysical states; its logarithm is taken only in the physical sector.

For any link cochain v define the UNITARY shift D_v|a>=|a+v>, and, for a
closed current j, W_j|a>=omega^(j.a)|a>. Both preserve the Gauss sector and

    W_j D_v=omega^(j.v) D_v W_j, omega=exp(2pi i/N).

Consider the Euclidean disorder insertion which twists only the temporal
plaquettes on the final seam by v. In the symmetrized Hilbert representation
its operator is

    B_v=M^(-1/2) D_v M^(1/2),

not generally the unitary D_v. Indeed Tr(T^n D_v) is the sum over paths from
a to a+v with endpoint factor sqrt[M(a) M(a+v)], whereas Tr(T^n B_v) has
endpoint factor M(a), precisely the temporally twisted Euclidean sum. This
can also be checked directly by multiplying the n kernels. B_v obeys the
same Weyl linking algebra because M commutes with W, but need not be unitary.
The distinction depends on the chosen Hilbert-space weight; an unsymmetrized
transfer convention can move the factor into the scalar product. It must not
be silently dropped when invoking norm-one operator bounds.

Since every kernel/path weight is nonnegative, define

    A_v=beta_s sum_p |sin[pi(dv)_p/N]|.

The exact identity for a cosine difference gives
|log M(a+v)-log M(a)|/2 <= A_v. Consequently

    exp(-A_v) <B_v>_n <= <D_v>_n <= exp(A_v) <B_v>_n,
    <O>_n=Tr(T^n O)/Tr(T^n).

No complex cancellation is used: the two expectations are positive path sums.
If v is a membrane shift whose spatial curl is supported on its boundary
loop C*, the correction is a perimeter factor, independent of membrane area.
For a unit boundary, A_v=beta_s |sin(pi/N)| |C*|. If dv=0, B_v=D_v exactly,
including nontrivial flat twists on a torus. Thus a valid Euclidean perimeter
lower bound can be transferred to the UNITARY Hamiltonian disorder operator
at a stated cost. This is an exact finite-step observable bridge; it is not
yet the desired photon or local-Hamiltonian theorem.

For linked loops the tensor-product support of D_v is the membrane, not just
C*. Every spanning membrane for C* intersects the linked Wilson loop C.
Ordinary spin-system clustering for disjoint tensor supports therefore cannot
be applied directly by using dist(C,C*) in place of the actual support
separation. Gauge equivalence of different membrane representatives does not
supply that missing clustering estimate by itself. A theorem in a physical
observable algebra, including its localization assumptions, is needed.

## 2. Quantitative loop-algebra criterion and its unclosed premise

For any state and bounded A,B with AB=omega BA, put a=<A>, b=<B>. If both
ordered connected expectations satisfy

    |<AB>-ab|<=epsilon, |<BA>-ab|<=epsilon,

then the algebra gives the exact elementary inequality

    |1-omega| |a b| <= 2 epsilon.

This is a useful criterion only with a valid estimate on the actual loop
operators. If |a|>=exp(-sigma_A P_A), |b|>=exp(-sigma_B P_B) and a hypothetical
loop-local clustering theorem gave epsilon<=C P^r exp(-mu d), it would imply

    mu d <= sigma_A P_A+sigma_B P_B
            +log[2 C P^r/|1-omega|].

For geometrically similar linked loops d is at most a constant times their
perimeters. Sending the size to infinity therefore bounds mu by a positive
combination of perimeter coefficients; it does NOT force mu=0. To obtain
such a conclusion one needs additional control, for example thickened
operators preserving the linking algebra with arbitrarily small perimeter
cost and adequate clustering. Neither that construction nor its required
uniform bound is supplied by ordinary exponential clustering. This is the
precise issue raised by Yaffe, PRD21,1574, sectionIII pp1579-1580.
Polchinski, PRD25,3325, also stresses matching the full conserved-flux content
of order parameters; its flux argument assumes a light/heavy dichotomy from
a mass gap. That dichotomy/source join is not imported here without proof.

A finite algebra-only countercheck makes the logical limitation explicit.
For N>=3 let U,V be a Weyl pair and choose positive a_L,b_L with
2a_L+2b_L<1. The density matrix

    rho_L=[I+a_L(U+U*)+b_L(V+V*)]/N

is positive, normalized, and has <U>=a_L, <V>=b_L (up to interchanging the
names if a different Weyl convention is used). Taking a_L,b_L exponentially
small in a label L imitates two perimeter laws while the Weyl algebra stays
exact. Purify rho_L and take H_L=I-|psi_L><psi_L|: its unique ground state has
gap1. This is NOT a geometrically local gauge-model counterexample; it proves
only that the algebra and nonzero exponential expectations, without the
geometric/dynamical hypothesis, do not force a vanishing gap. It must never
be described as disproving the finite-Z_N Coulomb phase or the literature's
complete physical argument.

## 3. A constructive spectral-filter replacement for the clustering shortcut

There is a sharper route-local result than merely identifying missing relative
clustering. It uses the actual locality of the change of Hamiltonian under a
membrane shift. It yields a quantitative upper bound on a putative gap; it does
not by itself force zero gap at fixed N.

Assume a specified bounded finite-range Hamiltonian (or its thermodynamic
GNS generator), a normalized ground vector Omega whose zero-energy eigenspace
is one-dimensional, and a spectral gap Delta>0 above it in the sector reached
by the operators below. Suppose there are unitary loop operators U_L,V_L with

    U_L V_L=omega V_L U_L, |omega|=1, omega!=1,
    |<U_L><V_L>| >= exp[-s L+o(L)].

Let U_L be tensor-supported on a loop C_L. Require that
H^V=V_L H V_L* differs from H only in a finite boundary region Y_L separated
from C_L by d_L>=kappa L-o(L), with kappa>0. Assume an ordinary Lieb-Robinson
commutator bound on U_L and the local terms of H^V-H, with constants mu,v>0
and at most polynomial prefactors in L. Duhamel then gives, for real r,

    ||tau_r^H(U_L)-tau_r^(H^V)(U_L)||
       <= Q_L exp[-mu d_L+mu v |r|],

where Q_L is polynomial in L. Explicitly, if the local commutator bound has
prefactor c0 |C_L| ||b|| and J_L is the sum of the norms of terms in H^V-H,
one may take Q_L=c0 |C_L| J_L/(mu v), using
integral_0^|r| exp(mu v u)du <= exp(mu v |r|)/(mu v).
The trivial norm bound2 may always be used when this estimate is larger.
The usual finite-range LR theorem supplies such a bound for finite-dimensional
clock links; no loop-local clustering theorem for V_L is being assumed.

Because V U V*=omega^-1 U, it follows EXACTLY that

    ||tau_x(U) tau_y(V)-omega tau_y(V) tau_x(U)||
      =||tau_(x-y)^H(U)-tau_(x-y)^(H^V)(U)||.

The membrane support of V causes no problem here: the perturbation H^V-H is
localized at its boundary and that is the object used in the LR estimate.

For c>1 let f_n be the n-fold convolution of the uniform probability density
on [-a,a], with a=c/Delta. This is a nonnegative even density supported on
[-T,T], T=na, and its Fourier transform is

    fhat_n(E)=[sin(aE)/(aE)]^n.

For every |E|>=Delta, |fhat_n(E)|<=c^-n. Define
A=integral f_n(x)tau_x(U)dx and B=integral f_n(y)tau_y(V)dy. Then
<A>=<U>, <B>=<V>, and the gap gives

    ||(A-<U>)Omega||, ||(A* -<U>*)Omega|| <= c^-n,

and likewise for B. Cauchy-Schwarz thus bounds each ordered connected
expectation by c^(-2n). Averaging the exact twisted commutator and using
|x-y|<=2T yields the finite inequality

    |1-omega| |<U><V>|
      <= 2 c^(-2n)+Q_L exp[-mu d_L+2 mu v n c/Delta].

This derivation pays the geometric locality and relative-error cost explicitly.
It does not use a claim that arbitrary averages preserve a group fusion law;
only the original U,V need satisfy the algebra.

Set n=floor(gamma L). If mu kappa>s, the lower bound on the product is
incompatible with the upper bound whenever a gamma exists with

    s/(2 log c)<gamma<Delta(mu kappa-s)/(2 mu v c).

Consequently every such gapped realization obeys

    Delta <= [c/log c] mu v s/(mu kappa-s).

Choosing c=e minimizes this elementary constant:

    Delta <= e mu v s/(mu kappa-s), provided mu kappa>s.

Subexponential corrections and polynomial prefactors disappear after taking
logarithms and dividing by L. For s=0, the same finite inequality rules out
any positive Delta. For positive fixed s it only provides a positive upper
bound. This is exactly the remaining distinction needed for the current phase
campaign. One may optimize over valid LR parameters, but not over parameters
for which no commutator estimate has been established.

Application of the locality hypothesis to the ACTUAL clock Hamiltonian:

    H=t sum_l(2-X_l-X_l*)
      +K sum_p[1-(Z_boundary(p)+Z_boundary(p)*)/2].

A membrane product V=product_l X_l^(v_l) leaves every electric term unchanged.
Only magnetic plaquettes with (dv)_p !=0 mod N change. Each changed term has
norm at most 2K |sin[pi(dv)_p/N]|. Thus for a unit membrane with boundary
length P_V, J_L<=2K |sin(pi/N)| P_V. A linked Wilson loop U has its ordinary
edge support on C_L, well separated from the boundary plaquettes although it
intersects the membrane itself. Two offset square Hopf loops can have
P_U=P_V=8L and d_L>=L-O(1) in a fixed lattice metric. Their exact Weyl phase
is omega=exp(2pi i/N). The LR prefactor grows only polynomially with L.
This verifies the distinctive geometric hypothesis without making V a
fictitious tensor-local boundary operator.

Explicitly, take the positively oriented Wilson square in z=0 with x,y
between -L and L. Let v equal one on positive y-links based at (x,0,z),
where 0<=x<=2L-1 and -L+1<=z<=L, and zero elsewhere. The Wilson current
intersects this membrane once, on its x=L side; its other y-directed side
has x=-L and does not intersect. Thus j.v=1. The rectangular sheet's
interior curl cancels pairwise. Its four boundary rows each contain 2L
plaquettes, giving 8L nonzero curl entries of magnitude one. Their link
centers lie on the corresponding rectangular boundary strip. Comparing
that strip with the four sides of the Wilson square gives Manhattan
separation at least L-1; the one-link thickness is the only offset loss.
These cancellations and distances hold for every positive integer L.

What is still missing: perimeter lower bounds for BOTH these unitary loop
families in the SAME actual continuous-time clock ground state, with coefficients
strong enough for a useful bound, or a controlled widening/dressing construction
for which s tends to zero while the geometry and locality constants remain
adequate. Fixed Euclidean perimeter bounds alone do not supply these hypotheses
for this H. A finite positive transfer-defined H has the exact observable map
in section1 but its quasilocal LR estimate is still unproved here. Combining
one model's perimeter bounds with the other model's locality would be invalid.

Even success at Delta=0 would show gaplessness, not a simple photon pole or a
native record-derived phase. Ground-space degeneracy also requires a separate
argument: if the spectral filter projects onto a multidimensional ground space,
the connected-expectation estimate above need not hold. This boundary is part
of the theorem, not an ignorable finite-volume detail.

### 3.1 One-filter proof and degenerate ground sectors

An alternative proof filters U alone. It gives

    |1-omega| |<U><V>|
       <=2 c^-n+Q_L exp[-mu d_L+mu v n c/Delta],

and the same optimized asymptotic bound on Delta. Each ordered connected
expectation is bounded by c^-n using the norm-one V. This proof needs only

    P0 U Omega=<U>Omega, P0 U* Omega=<U>*Omega,

where P0 projects onto the entire zero-energy subspace. V need not act as a
scalar on that subspace. Thus a one-dimensional ground space is sufficient,
but not necessary. An exactly locally indistinguishable ground sector can
also satisfy the condition for the finite contractible Wilson loops. That
property must be checked; degeneracy alone neither establishes nor refutes it.
If the two ground-sector remainders instead have norm at most ell_L, the
right side acquires at most2 ell_L. The same conclusion holds when ell_L
is exponentially smaller than the perimeter product (decay rate greater
than s). An unsuppressed ground-sector remainder invalidates this proof.

For an explicit dimension-independent LR source use Nachtergaele-Ogata-Sims,
math-ph/0603064v1, Theorem2.1, Eqs2.2/2.17, with proof pp3-4 and setup pp1-2.
Clock links can be treated as sites at their edge centers with the Manhattan
metric. This set is a finite union of translated cubic lattices, so
F(r)=(1+r)^-4 has finite uniform sum and convolution constants, as required
by Eqs1.3-1.4. Every spatial plaquette's four link centers have diameter1.
After removing identity constants, electric onsite terms have norm<=2t and
magnetic four-link terms norm<=K. The interaction norm of Eq1.7 is therefore
bounded by max(2t+4K,16K exp(mu)), independently of N and volume. The theorem
then supplies a finite velocity and a prefactor polynomial (indeed at most
linear after summing boundary terms) in L. No exponential N^(2|C|) prefactor
is hidden in the application. The earlier Nachtergaele-Sims single-site
bound could alternatively be applied by telescoping the product Wilson loop;
using its generic many-site prefactor without telescoping would be too weak.


## 4. Proof checks, primary sources and falsifiers

The five runner families separate distinct finite calculations. On a
two-plaquette, seven-link complex, direct enumeration of N^7 link increments
is compared with its independently factored Fourier kernel for N=2,3,5.
Direct paths of two and three time slices test both trace insertions and the
perimeter comparison. Fixed-start flux path sums additionally test every
diagonal sourced matrix element: a reversed seam similarity initially
escaped the charge-conjugation-symmetric summed traces and is detected by
this stronger check. The initial missed mutation and its repair are preserved.
Exact integer cochains construct offset square Hopf
loops for L=1,2,3,5,8,12; their counts are 8L Wilson edges, 4L² membrane
edges, 8L changed plaquettes, and separation L-1 in the link-center metric.
These finite fixtures support, but do not numerically prove, the all-L
geometric construction given in the text.

One-clock dense matrices at N=3,5,7 verify the exact twisted dynamical
identity independently by diagonalizing H and VHV*. Spectral multipliers
are compared with triangular time-density quadrature; both one- and
two-filter bounds are tested. A degenerate six-dimensional model satisfies
scalar Wilson compression while the membrane has a nonscalar ground
component. A separate adverse control shows that filtering cannot remove
an unsuppressed zero-energy Wilson remainder. These are finite algebra
checks, not spectra of the large Hopf-loop lattice. The asymptotic theorem
uses the written proof and its hypotheses, not finite numerical extrapolation.

Primary source attribution and inspected scopes:

- [Nachtergaele, Ogata and Sims, math-ph/0603064v1](https://arxiv.org/abs/math-ph/0603064v1),
  setup pp1-2 and Theorem2.1 with proof pp3-4. Its dimension-independent
  commutator estimate, including interaction norm and geometry hypotheses,
  supplies the LR input. The displayed spectral-filter/perimeter implication
  is derived in this note; it is not attributed to that paper.
- [Yaffe, Physical Review D21,1574](https://doi.org/10.1103/PhysRevD.21.1574),
  pp1-6 read, especially sectionIII pp1579-1580. The relative versus absolute
  error problem in a naive perimeter/clustering argument is prior work.
  Weighted transfer conventions motivate careful source matching; the exact
  finite-clock insertion and norm comparison above are checked directly.
- [Polchinski, Physical Review D25,3325](https://doi.org/10.1103/PhysRevD.25.3325),
  all six pages read. Matching conserved-flux order parameters is necessary;
  its light/heavy flux argument is not imported as a proved theorem for the
  present Hamiltonian.
- [Fröhlich and Spencer, IHES/P/81/40 preprint](https://omeka.ihes.fr/files/original/c59d65f61f9b1aba2d8eb6f4c01ceb88.pdf),
  pp1-70 and selected later passages inspected during this campaign. The
  U(1) covariance argument and fixed-step finite-Z_N perimeter argument
  have distinct inputs. No uninspected published-version correction or
  finite-N Hamiltonian photon theorem is asserted here.

Failure tests include reversing the seam similarity factors, losing the
Weyl phase or support separation, dropping the gap in the spectral
multiplier, using a many-site LR prefactor exponential in loop size,
silently discarding ground leakage, or interpreting a positive bound as
Delta=0. Source hashes and exact author mutation results are in the receipt.

## No-Go Discipline Gate

### N1 — Routes actually distinguished

| Honesty | Route | Result |
|---|---|---|
| ATTEMPTED | Direct clustering of linked tensor supports | Supports intersect; boundary distance is not tensor-support distance |
| ATTEMPTED | Hypothetical boundary clustering plus ordinary perimeter laws | Only a positive inverse-correlation-length upper bound |
| ATTEMPTED | Exact finite-transfer source map | Constructive unitary comparison at a perimeter cost |
| ATTEMPTED | Spectral filtering and local Hamiltonian deformation | Constructive conditional gap/perimeter theorem |
| ATTEMPTED | One-filter ground-sector refinement | Scalar Wilson compression suffices; explicit leakage term |
| OPEN | Thickened or dressed loop families with subperimeter cost | Requires control of algebra, locality and expectations together |
| OPEN | Collective resummation of fixed-payload Hamiltonian histories | Neither proved nor refuted here |

### N2 — Dependence and negative status

The first two limitations overlap: both concern insufficient relative-error
control. The two spectral filters are alternative proofs of the same
theorem, not independent walls. Transfer conversion is a positive bridge.
The heavy five-family negative packet is NOT PASS. This note ships a
narrowed positive theorem and explicitly partial phase attempt; it does
not claim that five independent routes fail or that the axioms force an update.

### N3 — Hidden conditions

The state, local Hamiltonian, loop embedding, nontrivial fixed Weyl phase,
ground projection and expectation bounds are supplied. The gap and LR
estimates must refer to the same model. The transfer logarithm is defined
only on the physical Gauss sector. A finite-dimensional positive transfer
does not by itself prove a spatially quasilocal logarithm.

### N4 — Residual matching

The target remains a collective fixed-payload clock phase with controlled
transverse response. A gap upper bound is weaker than gaplessness, and
gaplessness is weaker than a simple photon pole. A native physical
realization remains a separate obligation. Neither the target note's tame
oscillator nor an algebra-only gapped countercheck settles this phase.

### N5 — Resolution and rhetoric

Exact integer cochains, floating finite matrices and analytic asymptotic
statements are named separately. Five families are author evidence, not
independent reviewers. The runner explicitly states that no lattice-wide
infinite-volume phase or photon pole is executed. A complete current-source
review does not confer formal retained status.

### N6 — Partial closure and remaining routes

The exact observable map and local-deformation spectral estimate are usable
conditional components. Loop widening, uniform Hamiltonian perimeter
bounds, collective current resummation and local logarithm control remain
available. No axiom or primitive revision is proposed by these calculations.

### N7 — Steelman

A full dual-order theorem could contain more information than two simple
perimeter inequalities. A dressed operator may reduce its cost while
retaining algebra and suitable deformation locality. A topologically
degenerate phase may satisfy scalar compression for contractible Wilson
loops. Each possibility is compatible with this theorem and must be tested
on its own assumptions; none is declared impossible.

### N8 — Cross-cycle echo

Earlier campaign notes distinguish compact current sectors, finite-clock
transfer limits and raw curvature from a physical photon response. This
note adds an exact disorder source conversion and a paid spectral-filter
argument. It does not relabel those earlier phase gaps as new axiom walls.

## Source status and trace

```yaml
actual_current_surface_status: "conditional-support"
target_claim_type: "bounded_theorem"
trace_class: "upstream_support"
target_claim_id: "u1_finite_clock_gauge_matter_and_controlled_tame_maxwell_bridge_bounded_theorem_note_2026-09-03"
target_blocker_text: "Establish the collective fixed-payload many-link phase and transverse response beyond the controlled tame oscillator bridge."
source_of_blocker_text: "physics_loop"
reachability_to_target: "supports"
artifact_role: "theorem"
next_trace_action: "Independently check the disorder source map and spectral-filter bound, then prove both loop estimates and locality in one specified Hamiltonian model."
conditional_surface_status: "Supplied finite-clock model, Gauss sector, local Hamiltonian or positive transfer, ground projection and loop expectation assumptions as individually stated."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Exact conditional transfer-source comparison and spectral-gap/perimeter inequality; no thermodynamic phase or axiom wall."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
