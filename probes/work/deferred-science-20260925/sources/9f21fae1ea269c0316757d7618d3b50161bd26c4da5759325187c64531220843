# Local record statistics with unrestricted background formation

Root candidate, 2026-09-24. Conditional on the supplied compensated rotor
model. This argument is not yet independently checked or a retained claim.
The independent checker receives the question and exact parents, not this
answer. The finite-volume microscopic comparison is a separate obligation.

## 1. Question and exact scope

The established first-two-record readout includes a global survival factor
exp(-30 kappa V s). A local observation in a large active system should not
require every distant record to remain unchanged. Here the statistic is
instead an ordered factorial count of the same two original local marks.
It permits other events before, between and after the selected events.
It is a count expectation, not the probability of the first two events.

Use finite even cubic tori, with their vertex and link tensor factors, the
all-A-occupied P space, rotor links, and the physical Gauss constraint. The
exact parents are the local compensated common-field limit and local
pair-form note at main 0e6ad8285096ed668816f18caaa6fbbfbd9c50e8. In particular,

    h=K D+delta H4,
    L_kappa rho=-i[h,rho]+kappa sum_j D[B_j]rho,
    H4=-2 sum_{overlapping A stars {a,c}} S_ac^* S_ac,
    D=sum_{e=(a,b)} 1_(q_b=0) E_e(E_e-q_a),
    B_(a,b,sigma)=P j_(a,b,sigma) F_a P.

The sign in D uses links stored from A to B. Each summand is diagonal,
nonnegative on integer E, and supported on one edge and its endpoints.
They strongly commute. The H4 summands are bounded on the union of two
overlapping stars, with norm at most 2 z^4, and their overlap number is
bounded in a cubic family. Resolved B_j has star support and norm <=z-1.
The original coherent choice is its stated sign sum and is also uniformly
bounded and local. No change of recorded channels is made.

Encode each occupied A site by its two signs and each B site by 0,+,-.
On this tensor product the outer P factors of an individual term are local
occupancy restrictions; all other occupied-A factors act as identities.
The displayed operators have the parent's local extensions and preserve
Gauss. Restriction to the physical subspace cannot increase any ambient
operator norm used below. The tensor product is an estimation space,
not an assumption that physical gauge states factorize.

Write T_kappa(t)=exp(t L_kappa) on trace class and U(t)=exp(-iht).
For every fixed bounded local observable O_X there is a constant C_X,
depending on its fixed support and the cubic interaction geometry but not
on K, delta, kappa, the electric cutoff, or total volume, such that

    ||T_kappa^*(t) O_X-U(t)^* O_X U(t)||
       <= C_X ||O_X|| kappa t (1+delta t)^3.                 (1)

The trivial bound 2||O_X|| is also available. Equation (1) is a finite-graph
operator estimate uniform across this graph family. It neither constructs
an infinite-volume physical state nor makes the microscopic-to-rotor error
uniform in volume. The constants are not optimized or numerically calibrated.

## 2. Uniform Hamiltonian locality despite unbounded electric energy

First restrict every link to |E_e|<=L, retaining all matter factors. This
cutoff commutes with Gauss and every D summand. Compress each bounded local
H4 term and B_j separately; their supports and norm bounds are unchanged.
At fixed L this is an ordinary finite tensor-product problem.

In the interaction picture of KD, a bounded local term A_X becomes

    A_X(t)=exp(i KDt) A_X exp(-i KDt).

Every D_e disjoint from X commutes with A_X and with every other D_e, so
it cancels from this expression. Thus A_X(t) is supported within one fixed
edge neighborhood X^+ and has the same norm as A_X. This support statement
does not iterate under diagonal evolution. It is uniform in K,t,L.
It also applies to the endpoint test observable O_X(t).

Consequently the interaction-picture Hamiltonian has bounded, finite-range,
time-dependent terms with uniform support and norm <=C delta. At finite L
they are norm continuous. The usual time-dependent Lieb-Robinson bound then
gives, for any fixed-size local B_Y,

    ||[U(t)^* O_X U(t),B_Y]||
      <= C_X ||O_X|| ||B_Y|| exp(v delta t-d(X,Y)/R).        (2)

Here R,v and support enlargement constants depend only on the local cubic
geometry and H4 bounds. Absorbing the finite enlargement into C_X gives the
displayed distance on the original lattice. The trivial commutator bound
2||O_X||||B_Y|| can be used whenever smaller. The same estimate applies to
B_Y^*. No electric energy norm enters v.

For the finite-dimensional bounded theorem, use Theorem 1 and its proof in
Barthel and Kliesch, *Quasi-locality and efficient simulation of Markovian
quantum dynamics*, arXiv:1111.4210v2, PRL 108, 230504 (2012),
https://arxiv.org/pdf/1111.4210v2. Its Hamiltonian specialization applies to
the local commutator maps for the Hermitian real and imaginary parts of
B_Y, and the transformed Hamiltonian terms. Applying the theorem to both
parts and summing covers a non-Hermitian mark, with a harmless factor two.
Those maps annihilate disjoint observables, all restricted Hamiltonian
propagators are contractions, and range, overlap count and term norm are
uniform. These are the hypotheses used here. The original rotor generator
is not directly declared norm continuous by appeal to that theorem.

To remove the cutoff, keep each graph fixed. The finite-box projections
Pi_L increase strongly to I and commute with D. Use KD on the full space
and extend the compressed bounded terms by zero outside Pi_L. On the box
this agrees with the finite calculation. Each compressed term and its
adjoint converge strongly, with uniform fixed-graph norm bounds. The
interaction-picture Dyson expansion against the same KD therefore gives
strong convergence of the unitaries, uniformly on compact time intervals.
The analogous bounded perturbation series on trace class gives convergence
of the complete dissipative semigroups on every fixed trace-class input.
Finite rank approximation justifies multiplication by strongly converging
bounded terms. This is the same fixed-graph mechanism explicitly used in
the common-limit parent, with box-compressed rotor shifts here.

For a bounded local O, its box compression and its adjoint converge strongly.
Pass each matrix element of (2) to the limit; uniform operator bounds pass
with it. For (1), proved first below in the box, trace-class duality passes
the uniform norm inequality to the rotor. No energy moment is required of
the test density. The constants remain independent of L and volume even
though this convergence argument is performed separately at each volume.

## 3. Sum the local disturbances, not the global jump rate

For D_j^*(O)=B_j^* O B_j-{B_j^*B_j,O}/2,

    D_j^*(O)=[B_j^*,O] B_j/2+B_j^*[O,B_j]/2.

Combining (2) with the trivial bound gives

    ||D_j^*(U(v)^*O_X U(v))||
       <= C_X ||O_X|| min{1,C_X exp(v0 delta v-d(X,X_j)/R)}.

The constants absorb the uniformly bounded mark norms and support sizes.
The number of marks at graph distance in the nth fixed-width shell of X
is at most C_X(n+1)^2 on every cubic torus. This follows by covering X with
finitely many lattice balls; periodic identification only reduces the count.

Set A=v0 delta v+max(0,log C_X). The sum of (n+1)^2 min(1,exp(A-n)) is
bounded by C(1+A)^3: sum the polynomial for n<=ceil(A)+1, then substitute
n=ceil(A)+1+m in the exponentially decaying tail. All sums of m^k exp(-m),
k=0,1,2, are finite. Hence

    sum_j ||D_j^*(U(v)^* O_X U(v))||
                    <= C_X ||O_X|| (1+delta v)^3.            (3)

At finite cutoff the exact variation-of-constants identity is

    T_kappa^*(t)O-U(t)^*OU(t)
      =kappa int_0^t T_kappa^*(s)
          [sum_j D_j^*(U(t-s)^*OU(t-s))] ds.

The full Heisenberg semigroup is a contraction because it is unital and
completely positive. Equation (3) and integration prove (1), with the
coarser t(1+delta t)^3 in place of the exact integrated polynomial.
The cutoff removal in section 2 proves the rotor estimate.

This argument compares to the full Hamiltonian h on all matter sectors.
It does not replace any actual trajectory by a field-only postbirth law.
The appearance of the cubic polynomial reflects a conservative locality
cone, not a claim that observed light propagates with speed delta. The
packet group velocity and this norm-bound velocity are different quantities.

## 4. A local ordered factorial statistic with other events allowed

Use the resolved local marks j,l of the established cubic readout geometry.
Let M_l=B_l^* B_l and O_jl=B_j^* M_l B_j. This is a bounded local positive
operator on the entire common matter-field space, not merely its initial
matter block. The exact ordered factorial intensity of recorded j at s and
recorded l at s+u, with any other events allowed, is

    F_jl(s,u)=kappa^2 Tr[M_l T_kappa(u)
                                  (B_j rho(s) B_j^*)],
    rho(s)=T_kappa(s)rho(0), u>0.                            (4)

Summing the intervening jump histories gives the trace-preserving T_kappa,
rather than a no-event propagator. The bounded marked maps and strong
trace-class continuity imply

    F_jl(s,0+)=kappa^2 Tr[O_jl T_kappa(s)rho(0)].             (5)

This is a limiting density, not simultaneous events with positive mass.
Let C_jl(I,b) count every ordered pair of these two labels whose first time
lies in I and whose positive lag is at most b. On a fixed finite graph the
total number of original births is bounded, so this random variable is
finite, including possible multiple contributions. Its exact mean is the
integral of (4) over I times (0,b]. For fixed parameters, dominated
convergence gives

    E C_jl(I,b)/(kappa^2 b)
             -> int_I Tr[O_jl T_kappa(s)rho(0)] ds.          (6)

The domination is local: F_jl/kappa^2 <=||B_j||^2||B_l||^2,
using trace preservation and positivity. No global survival appears in
(4)-(6). A count expectation must not be presented as a Bernoulli event
probability or assigned the previous first-pair variance formula.

Apply (1) with O_jl. For the two prepared initial densities rho_1,g and
rho_0,g on a fixed cubic graph, the Hamiltonian-only initial evolution
stays in the original all-A-plus/B-empty sector. Its O_jl compression is
the independently checked 23I+W_p+W_p^*. The prepared weak-field argument
therefore gives, uniformly for 0<=s<=T,

    Delta F_jl(s,0+)/kappa^2
      =-2g^2 exp(-g^2 v_p/2)|chi_p(s)|^2
        +O_T(g^4)+O(C_jl kappa T(1+delta T)^3).              (7)

The O(g^4) preparation constant is still fixed-volume; equation (1) does
not make that separate constant uniform in volume. The negative signal is
preserved by this sufficient error estimate whenever the last term is
small compared with the specified nonzero g^2 packet signal.

With tau_*=a/c, K=g^2/(2tau_*), delta=1/(4tau_*g^2) and fixed T/tau_*,
one sufficient *additional supplied rate family* is

                    kappa_g tau_*=o(g^8).                 (8)

Then the last term in (7), divided by g^2, tends to zero. Equation (8) is
not a selected physical rate or a necessary condition. For fixed kappa,
this conservative bound does not establish weak-field signal survival on
a fixed observation horizon. A failure of this estimate is not evidence
that the actual signal disappears.

For each fixed row g,kappa and fixed graph, (6) permits choosing a sufficiently
small positive b so that its averaging error is o(g^2) along a subsequently
selected sequence. This is an existence statement with no lag rate. It is
not the quantitative first-pair bin estimate: a different count statistic
and all intervening records are involved. An actual microscopic marked-count
comparison would need the corresponding registered theorem and error control;
it is not imported from convergence of a point density.

## 5. What this would and would not add

The new mathematical content is a finite-graph local disturbance estimate
whose constant does not grow with total volume, together with its explicit
application to original record counts that permit background formation.
It addresses one artificial global waiting condition, within a weak and
explicitly conditional signal regime. It does not select the compensated
law, state preparation, a,c,g,kappa, clock, or a physical observer.

The principal remaining gaps are a quantitative nonshrinking observation
window, signal survival at physical rates/couplings, count variance and
feasible repetition, uniform packet propagation in large systems, and
microscopic resource bounds. Infinite-volume physical states, boundary
independence and retained audit status are also not supplied by this note.
No observed photon dataset is fitted or explained here. Adjustable small
rates and spacing cannot count as empirical confirmation.

## 6. Separate root controls and evidence limits

The root control first checks a three-rotor diagonal toy
D=(E1-E2)^2+(E2-E3)^2. Conjugating a shift on link 1 changes its phase by
2E1-2E2+1, independent of E3. At four electric cutoffs the distant shift
commutator is zero while the adjacent one has norm 2|sin(0.173)|. This
corroborates the one-neighborhood argument without approximating large
electric phases as small.

A separate chain of three through six two-state sites has a commuting
nearest-neighbor number diagonal, a number-conserving exchange Hamiltonian,
and local pair-creation jumps. Twenty-four combinations of chain length,+electric coefficient and time evaluate the complete Heisenberg evolution
and compare its local observable norm error with the numerically integrated
Duhamel norm bound. All inequalities passed. The largest difference between
20- and 32-point quadrature is 1.44e-8; those approximations are disclosed
and are not interval upper bounds. The code uses a tolerance based on their
difference when checking the numerically corroborative inequality.

The full control run exited zero in 3.9454514579847455 seconds with empty
stderr. Complete code, four cutoff rows and all twenty-four chain rows were
read by the root. Neither toy contains the original cubic Gauss law,
two-mark Wilson effect or weak-field photon preparation. These controls do
not prove the general locality theorem, calibrate its constants, or provide
observational evidence. The analytic proof and independent check have
separate responsibilities.
