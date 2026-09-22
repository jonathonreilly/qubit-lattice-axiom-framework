# Integer-spin record motion and a compact rotor limit

Date: 2026-09-22. Independent reconstruction from the neutral specification
and previously checked dependencies, before access to new author large-spin
sources. This is a conditional mathematical statement for the supplied model,
not a native implementation, phase theorem, publication or audit decision.

**Result.** A positive electric-square term is generated already at second
order. A joint scaling can keep it and the fourth-order plaquette coupling
finite without adding a bare single-link electric-square term. A sufficient
local finite-time limit can be proved uniformly over the stated finite tori
using a local dressed preparation, polynomially decreasing birth rates and
uniform fourth electric moments. It cannot be justified by operator-norm
convergence of spin shifts, or uniformly over arbitrary spin-S ice states.

## 1. Exact conventions and a sufficient statement

Let d>=2, let all periods be even and at least six, and let S run through
positive integers. Each positive-axis edge has electric eigenvalues
`m=-S,...,S`. Put

    C=S(S+1),   U=S_+/sqrt(C),   epsilon=t/Delta>0.

Matter is the stipulated hard-core bosonic qutrit `0,+,-`. Hops carry an
unchanged charge to an empty neighbor and shift the electric field to preserve
`div E+1_A-q=0`. Initially the code has plus at A, vacancy at B, and divergence
zero. The identical-boson premise is retained; independently readable record
identity tags would require a joint field/permutation target instead.

Fix two desired positive coefficients g,J and choose exactly

    epsilon_S^2 C = J/(2g),
    Delta_S = J/(2 epsilon_S^4) = 2g^2 C^2/J,
    t_S = epsilon_S Delta_S,
    beta_S = beta_0 epsilon_S^(2d),     beta_0>=0.       (1)

Use either `Delta N_B` or `(Delta/2)sum(div E)^2` as the penalty, with the
formation convention in Section 4. If beta_0>0, births remain enabled at each
finite S. The microscopic scales grow as Delta=O(S^4), t=O(S^3), while
beta=O(S^(-2d)). This is not a bounded-energy apparatus limit.

On each rotor link use `ell^2(Z)`, electric E|m>=m|m>, and the unitary shift
R|m>=|m+1>. Define the divergence-preserving plaquette W_p from the four
appropriate R/R^dag factors. The target is

    H_rot = g sum_e E_e^2 - J sum_p(W_p+W_p^dag).       (2)

Adding the scalar `2J #plaquettes` writes the magnetic part as
`J sum_p(I-W_p)^dag(I-W_p)`, so both specified energy contributions are
positive. No assertion about its thermodynamic phase or photon spectrum is
made.

Here is a precise sufficient initial class. For each finite torus and S,
let rho_(S,V) be an ice density supported on `|E_e|<=S` at every link and
suppose

    sup_(S,V,e) Tr rho_(S,V) (1+E_e^2)^2 <= M_4 < infinity. (3)

It may be entangled, correlated, and a mixture or superposition of winding
components. Prepare the actual matter/field state by the order `n=2d+6`
number- and gauge-preserving finite circuit

    Y_(epsilon,S)^dag (P_m tensor rho_(S,V)) Y_(epsilon,S). (4)

The circuit is the checked finite-order construction, now with the bounded
spin-S hopping terms. Its depth, range and local generator norm bounds can
be chosen independent of S and V, as justified below. Embed spin fields into
rotors by the displayed electric basis. For a bounded local rotor observable
A_X, let A_(X,S) be its compression to the spin links in X.

For any fixed time interval [0,T] and fixed support X, the microscopic open
evolution from (4) and rotor evolution (2) from the same embedded rho_(S,V)
satisfy

    sup_(0<=tau<=T) |<A_(X,S)>_micro(tau)-<A_X>_rot(tau)|
       <= C_(X,T,d,g,J,beta_0,M_4) ||A_X||
             [epsilon_S + (1+log C)^d/C].             (5)

The constant and sufficiently large S threshold are independent of volume
and the individual state in (3). In particular this is O(1/S). One simple
common initial family consists of arbitrary ice densities supported on a
fixed electric band `|E_e|<=M`, independent of S and V. No global projection
of an arbitrary large-volume rotor density is silently assumed: such a
projection can have very small probability as V grows. Equation (5) instead
compares the specified common initial density at each S,V. A separate local
limit assumption on those densities would identify an infinite-volume initial
state; it is not needed for the finite-torus uniform estimate.

## 2. Second order: generated positive electric energy

The exact link identities are

    U^dag U = I-(E^2+E)/C,
    U U^dag = I-(E^2-E)/C,
    [E,U]=U,       ||U||=1.                            (6)

The norm statement uses integer S: m(m+1)>=0 for integer m. Let eta_e=+1
when the positive-axis tail is in A and -1 otherwise. The initially possible
A-to-B plus hop shifts E_e by -eta_e. Its squared amplitude is

    a_e = 1-q_e/C,       q_e=E_e^2-eta_e E_e.          (7)

Every q_e is nonnegative and at most C on the spin spectrum. All edges must
be counted, with their weights; the spin-half count `dV/2` cannot be reused.
There are dV edges, and on ice

    sum_e eta_e E_e = sum_(x in A) div E_x = 0,
    A(E):=sum_e a_e = dV-(sum_e E_e^2)/C.              (8)

A two-hop return must reverse the same hop: after the first hop there is
only its original A vacancy available for returning a record. Hence the
normalized effective second-order term, including its physical coefficient,
is exactly

    -(t^2/Delta) A(E)
      = -(t^2/Delta)dV + [t^2/(Delta C)]sum_e E_e^2.    (9)

The electric coefficient is positive. At fixed J=`2t^4/Delta^3`, a finite
nonzero limit g therefore requires `epsilon^2 C -> J/(2g)` at this order.
Taking S to infinity first instead removes it; taking epsilon to zero at a
fixed S>=1 makes this nonconstant term large. The exact relation (1) avoids
an additional unbounded-onsite comparison between slightly different g's.

For the homogeneous penalty, the already checked identity remains exact for
every link spin on the preserved physical charge sector:

    (1/2)sum_x(div E_x)^2 = N_(A,-)+N_(B,+).           (10)

It follows solely from Gauss, the hard-core qutrit charges and
`sum q=|A|`, not from a spin-half field count. The right side is an integer
onsite matter penalty on the full tensor-product extension. Every hop changes
it by one. In the original-number all-plus sector it equals N_B exactly.
Its zero eigenspace at fixed signed charge is the same code. This proves that
both penalties have the same closed low coefficients while also supplying
the needed local extension after births.

## 3. Full fourth order and finite-S corrections

Let the inverse penalty D act as zero on the code, use dimensionless hopping
T, and define coefficients without powers of t. The normalized expression is

    H_2=-P T D T P,       K_2=P T D^2 T P,
    H_4=-P T D T D T D T P - (K_2 H_2+H_2 K_2)/2.     (11)

In units Delta=1, K_2=A and H_2=-A, so the folded contribution is +A^2.
It is essential even though A is now a nonconstant field operator.

For a four-hop return that does not pass through the code at an intermediate
step, the B counts are 1,2,1. The first two hops occupy disjoint edges e,f.
Returning along those same edges has four orderings, common denominator 2,
and squared amplitude a_e a_f. Thus its unfolded diagonal contribution is
`-2 sum_disjoint a_e a_f`. Subtracting it from the folded A^2 leaves

    L_S(E)=sum_e a_e^2 + 2 sum_(e<f, e and f meet) a_e a_f. (12)

A non-diagonal four-hop return exchanges the two identical records around
a simple four-cycle. On the stated tori these are exactly elementary
plaquettes. Each directed circulation has four orderings and amplitude the
product of its four normalized spin shifts. Operators on those four links
commute, so no ordering-dependent field factor is omitted. Consequently

    H_eff = -(t^2/Delta)A(E)
       + (t^4/Delta^3)[L_S(E)-2 sum_p(W_(p,S)+W_(p,S)^dag)]
       + higher orders.                              (13)

There are no odd returns. For degree 2d, each edge meets `4d-2` others.
Writing the finite-S diagonal term explicitly and using (8) gives

    L_S-dV(4d-1)
      = -2(4d-1)sum_e E_e^2/C
        + [sum_e q_e^2+2 sum_meeting q_e q_f]/C^2.      (14)

Thus after subtracting scalar energies the fourth-order field Hamiltonian is

    H_(S,4) = g sum E_e^2
       +(J/2)[L_S-dV(4d-1)]
       -J sum_p(W_(p,S)+W_(p,S)^dag).                 (15)

The corrected quadratic coefficient is `g-J(4d-1)/C`; the remaining quartic
diagonal expression in (14) is nonnegative for integer fields. It can retain
the supplied checkerboard orientation through q_e. It is neither a constant
nor a plaquette-flippability potential at finite S. On any fixed field band,
it vanishes with 1/C, as does the spin-shift correction to W. In particular,
if delta_e=+/-1 are the plaquette increments,

    W_(p,S) = W_p product_(e in p)
          sqrt(1-E_e(E_e+delta_e)/C)                  (16)

on the allowed spin domain, with zero boundary amplitudes understood. On a
fixed band this equals W_p times
`1-sum E_e(E_e+delta_e)/(2C)+O_band(C^-2)`.

One normal-form identification issue is new here: the second-order block
is no longer scalar, so fourth-order gauge invariance cannot simply be
borrowed from the spin-half proof. Choose the first circuit generators from
the individual edge hopping terms. For distinct edges e,f,
`P S_(1,e) S_(1,f) P=0`, since two different hops cannot return to the code.
The same holds in the reversed order. Each order-two homological generator
has zero code block. Hence the circuit's code block through order two has
the same Hermitian normalization `I-epsilon^2 A/2` and no anti-Hermitian
block rotation. Its relative block gauge against the canonical normalized
identification has no order-two term. Odd code terms vanish by parity, so a
gauge change first affects this Hamiltonian at order six. Equations
(13)-(15) therefore apply to this explicit circuit choice, without assuming
that arbitrary block gauges have identical fourth coefficients.
This is an identity of fixed formal coefficients; it does not require an
isolated global low-energy band at the parameter value used on a large torus.

## 4. Formation loss and unchanged onsite structure

Use the original rate convention `J_(e,q)=sqrt(beta)V_(e,q)` for each
charge-resolved branch, or one coherent jump
`sqrt(beta)(V_(e,+)+exp(i phi)V_(e,-))`. The two charge images are orthogonal.
Their common total loss on an edge is now

    Gamma_e = 2 beta P_(e,vac)[I-E_e^2/C].             (17)

It is not beta times the vacancy projector. At E=0 the rate is 2 beta; at
either spin boundary it is `2 beta/(S+1)`. Dividing the supplied jumps by
sqrt(2) would change the convention, not remove the electric dependence.
Using both coherent signs as independent unrescaled jumps doubles (17).
Resolved jumps have norm at most one before sqrt(beta); a coherent jump has
norm at most sqrt(2). These bounds are uniform in S. The loss is strictly
positive on a vacant edge at each finite S, but has no S-independent positive
lower bound. None of these statements implies uniform occupation completion.

The Gauss, charge, record permanence, and count identities are unchanged.
A star-penalty birth changes the integer penalty by zero or two. Its rate
weights, however, are (6). In particular the spin-half argument counting
exactly d-1 eligible energy-raising branches at an A vacancy does not extend
unchanged. No previous sharp density constant or scalar first-excursion loss
is imported into this proof.

For reference, at leading second order in t at fixed Delta,beta, a first hop
on e has squared amplitude a_e. Its new A vacancy has the other 2d-1 B
neighbors vacant, with loss

    gamma_e(E)=2 beta sum_(f meets that A, f!=e)(1-E_f^2/C).

The no-event second-order probability-loss coefficient is the diagonal sum
`sum_e t^2 a_e gamma_e/[Delta^2+(gamma_e/2)^2]`. It need not be scalar and
does not assert an exact exponential clock. The local convergence argument
below uses the full dissipator and requires no such effective-clock model.

## 5. Uniform microscopic-to-spin-field comparison

The prior finite-circuit/locality machinery applies, with the following
explicit changes and checks.

1. The local link dimension grows, but hopping norms are at most one and
   birth norms at most sqrt(2). The integer onsite penalty is still a sum
   of matter projectors. Its homological inverse has norm at most pi/2,
   independently of S. The finite support counting, gate-product Cauchy
   estimates and commutator bounds use operator norms and never a matrix
   dimension factor. Thus the order-n local remainder is uniformly
   `O(Delta epsilon^(n+1))` in both S and V.
2. Gauge and count commutation are termwise. The code stays invariant under
   the normal-form diagonal part K. A bare birth annihilates P, so a dressed
   jump B obeys `||BP||=O(epsilon)` uniformly in S,V. For a code density,
   `||D[B]sigma||_1 <= ||BP||^2+||B||||BP||=O(epsilon)`.
   This includes no-event anticommutators and arbitrary code entanglement.
3. Removing Delta N by its onsite interaction picture leaves finite-range
   local Lindblad terms with velocity `O(Delta epsilon^2+beta)`.
   The already checked Barthel-Kliesch norm bound is dimension independent
   at this point. The earlier alternative locality estimate with an
   explicit local-dimension factor is not used in a growing-S argument.
4. The same clipped-cone sum as in the completed uniform-local proof gives
   the microscopic error

       C_X,T [epsilon
          + Delta epsilon^(n+1)(1+epsilon^-2 T)^d
          + beta epsilon(1+epsilon^-2 T+|log epsilon|)^d].

   With n=2d+6 and (1), this is O(epsilon), uniformly in S,V.
5. Within the code, replace the second-order block by the equal onsite
   `g sum E^2` plus its scalar, using Gauss as in (8). The remaining
   fourth-order terms have bounded local norm independent of S:
   `0<=a_e<=1` and `||W_(p,S)||<=1`. Removing the electric onsite term
   leaves a bounded locality velocity. All higher normal coefficients
   start at sixth order with local norm `O(Delta epsilon^6)=O(1/C)`.
   A second locality comparison therefore reduces K to (15) with
   an O(1/C) local error.

This controls the full open dynamics, including repeated formation. It
does not condition on no births in the whole torus. The field-star proof
uses its exact onsite matter extension on the invariant physical sector;
using the large full-space norm of the original star expression would be
an unnecessary and invalid source of S-dependent constants here.

## 6. Spin fields to rotors: moments, domains and local volume bounds

Norm convergence of U to R is false: `U|S>=0` while `R|S>=|S+1>`. Instead
embed the spin space in ell^2(Z) and define

    U_S=R sqrt([1-E(E+1)/C]_+),
    a_(e,S)=[1-(E_e^2-eta_e E_e)/C]_+.

These extend the exact spin operators, vanish across the cutoff, and have
norm at most one. They define a rotor-space extension of (15) preserving the
embedded spin space. For integer m the relevant quadratic products are
nonnegative, and `1-sqrt([1-x]_+)<=x` for x>=0. Hence for any density rho,

    ||(R-U_S)rho^(1/2)||_2
        <= C^(-1) <[E(E+1)]^2>_rho^(1/2),
    ||(1-a_(e,S))rho^(1/2)||_2
        <= C^(-1) <q_e^2>_rho^(1/2).                  (18)

The lowering analogue is identical. The moments on the right are bounded
by a constant times `<(1+E^2)^2>`. Telescoping a four-link product in (16)
uses only contractions on the other links, which commute with this link's
moment weight. Similarly `1-a_e a_f <= (1-a_e)+(1-a_f)`. Thus each local
Hamiltonian-difference source between (15) and (2), on a reference state
with fourth moments at most M, has trace norm at most `C_d J sqrt(M)/C`.
The commutator estimate used here is
`||[D,rho]||_1<=2||D rho^(1/2)||_2` for Hermitian D. The total difference
also has bounded local operator norm independent of S, even though that
norm does not tend to zero.

Fourth moments remain controlled for fixed times under the rotor reference.
Set `F_e=(1+E_e^2)^2`. The electric Hamiltonian commutes with F_e. A unit shift
satisfies

    1/3 <= [1+(m+1)^2]/[1+m^2] <= 3,
    ||F_e^(-1/2)[W_p,F_e]F_e^(-1/2)|| <= 3            (19)

when p meets e. The first inequality follows from
`3(1+m^2)-(1+(m+1)^2)=2(m-1/2)^2+1/2>0` and reversal.
There are `2(d-1)` incident plaquettes and two orientations. Therefore

    sup_e <F_e>_(rot,tau) <= M_4 exp[12J(d-1)tau].     (20)

For mixtures the weighted commutator is paired with the positive trace-class
operator `F_e^(1/2)rho F_e^(1/2)`; no factorization is needed.

There is no hidden infinite-dimensional locality assumption in this step.
On each finite torus, the electric Hamiltonian is self-adjoint on its natural
domain, and the finite sum of magnetic shifts is a bounded perturbation.
To justify both (20) and the local comparison, first truncate the *rotor*
links at a larger integer M>=S, replacing R by its hard truncated shift.
Both models then have finite-dimensional factors. Their common electric
term is removed exactly by an onsite interaction picture. Local interaction
norms, the weighted commutator bound (19) and the locality constants are
independent of M and S.

At fixed finite volume the truncated magnetic terms converge strongly to
the rotor magnetic terms and are uniformly bounded. In the electric
interaction picture, their Dyson series converge strongly, uniformly on
compact time intervals, by dominated convergence. Initial trace-class
states and local bounded observables pass to the limit. Fourth moments
pass by positive truncation/lower semicontinuity. This constructs the needed
domain extension from the finite-dimensional estimates, rather than
asserting operator-norm continuity of the unbounded onsite evolution.

Use variation of constants with the rotor reference and the full spin-field
propagator, just as in the prior open comparison. For a nearby source use
(18)-(20); far away use the dimension-independent locality bound with a
bounded velocity. Clipping at `O(1/C)` gives

    local field error <= C_(X,T,J,d,M_4) ||A_X||
                             (1+log C)^d/C.           (21)

All constants were uniform before removing M. The comparison is exact for
the embedded spin initial state, since its evolution under the extended
spin Hamiltonian remains within that subspace. Its expectation of A_X is
therefore exactly the finite-spin expectation of the compression A_(X,S).
There is no global cutoff probability in (21). Combining (21) with Section 5
proves (5).

## 7. Countercontrols, checks and limitations

A uniform claim over all initial ice states would fail at the field step.
Take every canonically oriented link at E=S, with even S, so divergence is
zero. Every spin plaquette circulation needs a forbidden raising operation,
so this word is an eigenvector of (15). In the rotor model both circulations
remain available. For the fixed bounded observable `(-1)^E_e`, the rotor
second derivative from this word is `-16(d-1)J^2`, while the spin-ring value
is zero. Uniform flux translation gives the same rotor evolution as the
zero-flux word, up to an overall phase in the conserved total-electric sector,
so this discrepancy is not removed by increasing S. These initial states
violate (3). The example refutes an unrestricted approximation, not the
moment-restricted limit or a general physical model.

The independent scripts do not import any new author code.

* `finite_spin_check.py` assembles all physical square states directly from
  Gauss, with both charges and births: dimensions 19,39,59 at S=1,2,3.
  Their original-number sectors have dimensions 13,25,37. It computes every
  normalized second- and fourth-order matrix entry for both penalties,
  verifies (13), both birth refinements' exact losses, and all distinct
  first-order edge products on the code. For S=1 the low matrices are
  `H2=diag(-2,-4,-2)` and
  `H4=[[2,-2,0],[-2,12,-2],[0,-2,2]]`, in Delta=1 units.
* `boundary_and_bulk_check.py` checks the link algebra, all weighted
  disjoint/adjacent path counts on independently constructed 6^2 and 6^3
  divergence-free words, the bulk expansion (14), and the saturated-flux
  second-derivative countercontrol. This is static exact arithmetic, not a
  production simulation.
* `circuit_gauge_check.py` independently builds and orders the local gates
  through fourth order on the complete S=1 and S=2 square sectors. Their
  second-order blocks are nonconstant, but their fourth-order code matrices
  equal (11) exactly. This checks the new identification issue separately
  from the canonical weighted-path computation.
* The first script also compares the exact fourth-order single-loop field
  Hamiltonian with a rotor cutoff at 24 for S=1,2,4,8,16 and three times.
  It corroborates the 1/C trend. Small computed cutoff occupation is not
  used as a proof of truncation error or a volume-uniform theorem; the
  domain and moment proof above supplies that argument.

All three scientific executions passed on their first runs. Complete stdout,
stderr, receipts and all result fields are preserved and were read. There
was no failed scientific assertion to hide. An initially truncated combined
read of unchanged dependencies was repaired by a targeted read of the
missing relevant section; their prior complete reviews remain identity-bound.

The sufficient schedule and fourth-moment condition are not optimized.
Fixed beta, a bare quench, growing observation times, states spread across
the full spin band, or a preparation law selecting (3)-(4) require another
argument. No unchanged spin-half density constant, all-state completion,
thermodynamic phase, native qubit compiler, or emergent photon claim follows.
The generated electric term does not eliminate the supplied background,
bosonic statistics, enlarged link Hilbert spaces, preparation circuit,
Hamiltonian time or formation apparatus. Scalar energy subtractions compare
dynamics; they do not pay for the diverging microscopic scales or make
formation energy conserving.

The next authorized action is source comparison after this reconstruction's
PRE seal. All newer author large-spin, weak-field, energy, transport and ramp
sources and the campaign checkpoint/registry remain unread at this stage.

## 8. Pinned dependencies and external-import boundary

The allowed definitions and inherited machinery were reused at these exact
identities; all seven and all 58 bindings of the preceding final packet were
authenticated before this seal. `SOURCE_READ_BOUNDARY.json` contains full
absolute paths and byte counts.

| Source | SHA-256 |
|---|---|
| `HARDCORE_RECORD_MOTION_GENERATES_GAUGE_RINGS.md` | `a527532324a5ed75e660b19c131f759fa0b38be4cdcf855f3a4f59c205cbc99e` |
| `HOMOGENEOUS_FIELD_STAR_PENALTY_FOR_MOBILE_RECORDS.md` | `860e8d364e50f8cddcbb6c534d69ca4ce822020ea80deab6c22361eeda0d361c` |
| `UNIFORM_LOCAL_RING_DYNAMICS_WITH_SLOW_RECORD_FORMATION.md` | `e03793ab0cc06bcc0d536db5b846addf3a999733c6dc25cc4d08ae457263e16e` |
| Prior independent uniform-local `REPORT.md` | `4dc693c1b9cadd94ea95ce01108a72570482ad82c10c4b3f5f611169f749621e` |
| Prior independent uniform-local `COMPARISON.md` | `00048adee9d46312bb197b590d3d2c709e209d7527cd44c2c7f9942a96feea1c` |
| Prior independent uniform-local `FINAL_SEAL.json` | `cc213db7ba3b00cce3ae52d8206878219257bda27b831bfdad93129a9dbcafcf` |
| Cached Barthel-Kliesch 1111.4210v2 HTML | `abdeedde2be6d39e29f766e860d90e54783f9a384c3dbf1e75244769a07e84a7` |

The only locality theorem import is the already checked finite-dimensional,
time-dependent local Lindblad bound of
[Barthel and Kliesch, arXiv:1111.4210v2](https://arxiv.org/html/1111.4210v2).
Its hypotheses and full relevant proof were read in the preceding comparison.
The finite-cutoff rotor passage and moment estimates are derived in this
report; no unreviewed infinite-dimensional locality theorem is imported. No
new network lookup or author large-spin source was needed.
