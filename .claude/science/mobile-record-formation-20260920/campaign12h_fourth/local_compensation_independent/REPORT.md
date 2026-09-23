# Local occupation-gated compensation: independent reconstruction

2026-09-23. Blind reconstruction of the supplied candidate, before access to the
root's specific construction packet. This is a selective mathematical check,
not a publication or formal audit disposition.

The proposed interaction works on the stated fixed finite bipartite graph.
It removes the fast second-order matter Hamiltonian on the entire P space,
leaving an exactly identifiable finite-spin electric multiplication operator.
Under the stipulated joint scaling, the microscopic densities converge on
compact ordinary-time intervals to a coupled rotor/record Lindblad evolution,
state by state in trace norm. The limiting electric energy depends on vacant
B sites. It is not the same pure-field Hamiltonian after arbitrary formations.

On the cube, the initially vacant-B branch has six genuine plaquette terms,
with coefficient -2 delta, and a scalar fourth coefficient -84 delta.
An explicit ordered pair of actual formation marks has a nonzero isometric
product on every initial field vector. This proves accessible two-formation
probability, rather than merely displaying a jump on an unrelated state.
The later waiting law is not established here, and its instantaneous rate
already depends on the field state. Removing the occupation gates erases the
entire rotor fourth-order Hamiltonian; that simpler compensation does not
retain the desired field term.

## 1. Scope, prior exposure, and definitions

Only the supplied task, the already checked parent target theorem, the sealed
independent general compensation proof, and the previously sealed independent
cube path sources were used. The parent source is
`campaign12h_third/FINITE_FORMATION_WITH_RETAINED_FOURTH_ORDER_DYNAMICS.md`,
SHA256 `002119d5a3f9bec171c3678cb15afdb91f7a763311ca38e6e4458ce10865572e`.
The independent general theorem's REPORT is SHA256
`dcd02298d9a27ea9eadfb387a81f9f1336c66f681fb84933ee48cac225ed5401`;
its PRE is `0504a3fc90cca1b0f9b7bab3a1aa346b11e0889bc25abf55bd65966965375a46`.
That theorem was already compared with the root's general bounded lemma.
The sole accepted wording repair, separately acknowledged before this work,
restricts self-adjointness to the two Hamiltonian coefficients. It changes
none of the formulas used below.

Prior exposure is explicit: I previously computed the uncompensated cube
second-event Gram and point-spectrum operators. Their path conventions were
reread as allowed dependencies. The new runners import neither those builders
nor any root builder. The compensation, its limit, and the new control
implementations were reconstructed here. No other file in
`local_compensation_author`, its specific construction seal, the local
counterterm proposal, cube-unprepared packet, checkpoint, registry, future
extension, Git or publication surface was accessed. The complete source
identities are in SOURCE_BINDINGS.json and the PRE seal.

Let the graph be finite, simple and bipartite with parts A and B. Orient every
edge once. For a in A adjacent to b in B, write s_ab=+1 if the stored edge
orientation is a to b, and -1 otherwise. The outgoing hop F_a sums the two
charges and all vacant destinations b. It moves the immutable charge q_a and
shifts that edge by -s_ab q_a. T=-sum_a(F_a+F_a^dagger). Site occupation is
n_x=q_x^2, W=sum_A(1-n_a), P=1_(W=0), and the physical equation is
`div E=q-1_A`. Link spin S is integer and
`U=S_+/sqrt(c_S)`, `c_S=S(S+1)`.

All results concern these supplied site/link resources, background, interaction,
initial preparation and jump instruments. No native-axiom selection, fuel
implementation, photon phase, or volume-uniform bound is inferred.

## 2. Locality, constraints, positivity and the exact second coefficient

For an outward hop on an occupied a and vacant b, the squared link amplitude is

    1 - (E_e^2 - s_ab q_a E_e)/c_S.                    (1)

This also gives zero at the forbidden spin endpoint. Consequently

    D_(a,infinity)-D_(a,S)
      = (n_a/c_S) sum_(b~a) (1-n_b)
                       (E_e^2-s_ab q_a E_e).          (2)

There are no additional diagonal two-hop paths: returning from a different B
site changes which B site is occupied. Integer E and q_a=+/-1 make each
`E_e^2-s_ab q_a E_e` nonnegative. The diagonal difference in (2) is between
zero and D_(a,infinity), and its norm is at most z_a=deg(a).

F_a^dagger F_a preserves each A-site occupation. It therefore commutes with
Q_a, the product of other A occupations at distance at most two. The proposed

    C_S=sum_a [F_a^dagger F_a-D_(a,S)+D_(a,infinity)] Q_a   (3)

is self-adjoint and positive. It preserves all Gauss constraints, W, total
record number, and the counts of each immutable charge. Its support is the
star of a plus occupation controls on distance-two A sites. In particular it
is a fixed finite-range interaction, not a projection on all A occupations.
At fixed graph,

    ||C_S|| <= sum_a (z_a^2+z_a),                       (4)

uniformly in S. For unit rotors, (3) is simply
`C_infinity=sum_a F_a^dagger F_a Q_a` and remains bounded. The construction
supplies an extra coherent interaction; it is not derived from the original
hopping alone.

Put Aop=Pi1 T P and M=Aop^dagger Aop. The orthogonality of distinct A-vacancy
patterns gives `M=sum_a P F_a^dagger F_a P`. Since Q_a P=P,

    C_0=M+Ecal_S/c_S,
    Ecal=sum_(a in A,b~a) (1-n_b)(E_e^2-s_ab q_a E_e)
          on P.                                      (5)

Ecal_S is exactly the restriction of the common rotor diagonal Ecal to the
finite electric box. Thus the canonical second coefficient is

    K_(2,S)=C_0-M=Ecal_S/c_S.                          (6)

This is an exact identity on every P number sector, not only before the first
birth. It cancels all second-order off-diagonal matter transport.

## 3. Fourth order and the role of the gates

The already independently proved positive-overlap block formula applies,
because (3) is bounded uniformly in S and commutes with W. With
`Z=Pi2 T Pi1 Aop` and `C_1=Pi1 C_S Pi1`, it gives

    K_(4,S)=M^2-Z^dagger Z/2+Aop^dagger C_1 Aop
                         -{M,C_0}/2,
    B_(j,S)=-P j Pi1 T P.                             (7)

The leading jumps are unchanged. The excited-block term and the canonical
anticommutator cannot be dropped at finite S. The general theorem gives the
full-density O(epsilon) approximation to the P generator with Hamiltonian
`delta epsilon^-2 K_(2,S)+delta K_(4,S)` and jumps `sqrt(kappa) B_(j,S)`.
Its constants are uniform in S at this fixed graph. The proof controls the
large off-block dissipative source with the full-W-cluster correction; a
projection that merely deletes that source would not suffice.

The unit-rotor fourth coefficient has a particularly local form. Set
`a~_2 c` when distinct A sites share a B neighbor. Outward F_a and F_c commute:
terms with different destinations act on disjoint matter sites and links;
terms with a common B destination vanish in both orders by hard capacity.
Thus

    Z=2 sum_(a<c) F_c F_a P,
    Z^dagger Z/2=2 sum_(a<c) P (F_c F_a)^dagger F_c F_a P.   (8)

The different unordered pairs have orthogonal two-A-vacancy ranges.
Following an outward hop from a, C_c vanishes if c=a or a~_2 c: the first
case has an empty source and the second has a zero gate. For all remaining
c, the stars are disjoint and Q_c=1 on that one-hole pattern. Therefore

    Aop^dagger C_(1,infinity) Aop
       =2 sum_(a<c, a not~_2 c) P (F_c F_a)^dagger F_c F_a P.

Since C_(0,infinity)=M, the M^2 term cancels the canonical anticommutator.
Equations (7)-(8) leave

    K_(4,infinity)
       =-2 sum_(a<c, a~_2 c) P (F_c F_a)^dagger F_c F_a P.   (9)

Each surviving term has finite support in the two overlapping stars. This
proof covers all P charge/occupation patterns, including later formations.
The restriction P describes the target Hilbert space; the term's physical
action on that space is local.

A useful countercontrol is the ungated choice
`Cplain_S=sum_a(F_a^dagger F_a-D_(a,S)+D_(a,infinity))`.
It has the same second coefficient, but in the rotor limit all pairs survive
in Aop^dagger C1 Aop. They cancel Z^dagger Z/2 exactly, giving

    K_(4,infinity)^plain=0.                            (10)

Thus boundedness and cancellation of fast motion alone do not establish
retention of plaquette dynamics. The gates materially change the answer.

## 4. Joint spin limit, operator domains, and full density convergence

Fix delta,K,kappa>0 and choose

    epsilon_S^2=delta/(K c_S),
    delta/epsilon_S^2=K c_S.                           (11)

On the physical P rotor Hilbert space, a countable charge/integer-field basis,
Ecal is a nonnegative real multiplication operator. Define it on

    D(Ecal)={psi: sum_(q,E) Ecal(q,E)^2 |psi(q,E)|^2<infinity}.

Finite-support physical vectors form a core. Nonnegativity follows term by
term from (5); no coercivity on inactive links is assumed. For example Ecal
vanishes when every B site is occupied. Let

    H_eff=K Ecal+delta K_(4,infinity),
    L_eff(rho)=-i[H_eff,rho]+kappa sum_j D[B_(j,infinity)]rho. (12)

The fourth coefficient and all jumps are bounded at fixed graph. Hence
H_eff is self-adjoint on D(Ecal), bounded below, and its unitary group plus
the bounded dissipative perturbation defines a unique CPTP semigroup on trace
class. Equation (12) is a mild semigroup definition on general trace-class
inputs; it does not require the formal commutator to exist for every density.
In particular no electric moment is needed for the qualitative density limit.

Embed each finite-spin space in the rotor space through its electric box
`R_S=1_(|E_e|<=S for every edge)`. These projections commute with Gauss, P and
Ecal and increase strongly to I on P. Normalized spin shifts, extended with
zero at their endpoints, and their adjoints converge strongly to unit shifts,
with uniform norm at most one. Every finite polynomial in those shifts,
charge projectors and gates has the corresponding strong limit. The diagonal
differences (2) tend strongly to zero and are uniformly bounded. It follows
that the embedded K_(4,S), B_(j,S), and their adjoints converge strongly,
uniformly bounded, to the operators in (12).

For precision, extend the finite target to the full rotor space using the
same unbounded K Ecal, with its bounded fourth/jump operators compressed by
R_S and zero outside. The electric box is reducing, and the restriction is
exactly the finite target because (6) and (11) give K Ecal_S with no remainder.
In the interaction picture of K Ecal, the bounded perturbations converge
strongly, uniformly on compact sets of vectors. Dyson expansions with uniform
bounds, first on rank-one operators and then by trace-class approximation,
prove uniform-on-compact-time strong convergence of their CPTP semigroups.
Contraction extends the assertion from finite electric-support densities to
all trace-class densities.

Consequently, if rho is any P density and rho_S are physical finite-spin
P densities with ||rho_S-rho||_1->0 after embedding, then

    sup_(0<=t<=T0) ||rho_(microscopic,S)(t)-exp(t L_eff)rho||_1 -> 0   (13)

for every fixed finite T0. Combine the parent/general-compensation uniform
O(epsilon_S) approximation with the just-proved target convergence and initial
trace-norm convergence. This is a complete joint limit, including recycling
and all accessible record-number sectors. It is not restricted to a no-event
branch. A normalized truncation of any fixed rho gives such rho_S for large S.
Number-sector coherences are allowed for the explicitly supplied W Hamiltonian;
no number-offset Hamiltonian reinterpretation is used.

The O(epsilon_S) microscopic-to-target error is uniform over densities; the
additional spin-to-rotor convergence in (13) is statewise. No rate or uniform
supremum over all moving high-electric-energy inputs is proved. In particular
`||(U_S-U)|S>||=1`: operator-norm convergence of shifts is false. This distinction
is essential. Constants are not uniform in graph volume and no growing-time
claim is made.

A finite count/mark register can be adjoined throughout, with no reachable
overflow since births increase a bounded record count. The same proof then
gives the corresponding finite-register and integrated marked-event
probabilities. It does not assert total variation convergence of all continuous
quantum trajectories. The model remains a supplied open system with a growing
microscopic scale and formation channels, not an autonomous energy/fuel account.

## 5. Cube field Hamiltonian before the first event

Use binary cube vertices 0,...,7, A={0,3,5,6}, low-to-high edge orientation,
and initially q=1_A. This graph has degree three; it is not the periodic cubic
family used for the parent's quoted field coefficient. The coefficient here
was derived directly rather than importing that formula.

Every pair of A vertices shares exactly two B neighbors. Therefore C1 vanishes
on the entire cube W=1 space. On the initially vacant-B sector, a given pair
of A sources has `3*3-2=7` allowed ordered distinct B destinations. Returning
each record to its own A site gives seven diagonal paths. Exchanging the two
return destinations gives the two orientations of the unique square through
those A sites and their common B neighbors. Equation (9) hence becomes

    K_(4,infinity)|Pv=-84 I-2 sum_(six faces p)(W_p+W_p^dagger).      (14)

The exact path check lists all twelve integer circulation shifts and their
coefficient -2. Gauss gives div E=0 on Pv, so the linear electric terms sum
to zero and Ecal=sum_e E_e^2. The conditional field Hamiltonian, up to the
scalar -84 delta, is

    H_field=K sum_e E_e^2-2 delta sum_p(W_p+W_p^dagger).              (15)

It is nonconstant on normalizable states. For the electric-zero basis vector,
the variance of H_field is exactly 48 delta^2, independently of K. Fiber
calculations used in the controls are operator checks, not normalizable
plane-wave preparations.

Each resolved first channel has B_j^dagger B_j=2 I on Pv; each coherent edge
channel has 4 I. The old-record destinations are orthogonal, as are the two
created A charges. There are 24 resolved channels or 12 coherent edge channels,
so the total first rate is r=48 kappa, independent of the field density.
Before the first event the unnormalized density is

    e^(-48 kappa t) e^(-it H_field) rho e^(it H_field).               (16)

Resolved marks are uniform among 24 and coherent edge marks among 12, for the
specified instruments. These operational marks give different post-event
coherences. After a birth, (12), not (15), governs the coupled state. At full
occupation, all F_a and B_j vanish and Ecal=0, so the limiting state freezes.
The microscopic fully occupied states also have W=T=C=j=0 in this model.

## 6. An accessible second formation, and its limitations

Take the first resolved mark to be edge (0,1), with + charge at 0. The old
plus from 0 can move to 2 or 4; B1 is the coherent sum of those two paths and
`B1^dagger B1=2 I` on Pv. Next choose edge (4,5), with - charge at its low
endpoint 4 and + at 5. Only the first branch of B1 can contribute: it leaves
holes 4 and 7, allowing the old plus at 5 to move to 7 and the new pair to
fill 4 and 5. The branch with a plus at 4 is blocked by hard capacity.
Thus B2 B1 is a single unit-rotor path. It takes initial q=1_A to

    q_final=(1,-1,1,1,-1,1,1,1)

and adds the link increments

    E01:+1, E02:-1, E45:-1, E57:-1; all other increments zero.       (17)

Its Gauss identity is exact and

    (B2 B1)^dagger(B2 B1)=I on Pv.                                  (18)

This holds for any normalizable pure field input and, by linearity, any field
density, including arbitrary cycle correlations. It is not just a path starting
from an inaccessible six-record state. Conditional on the freshly normalized
first resolved output, this particular next marked hazard is kappa/2.
For coherent edge marks at both selected edges, the first norm square is four
and the ordered two-mark norm square is four; the four charge outputs are
orthogonal and the corresponding fresh next-edge hazard is kappa.

Bounded jump maps and strongly continuous no-event semigroups make the ordered
trajectory integrands continuous at zero even for a density outside D(Ecal).
For these two specified resolved marks, their probability by time t is

    (kappa^2/2) t^2+o(t^2),                                         (19)

in the limiting model. For the two coherent edge marks it is
`2 kappa^2 t^2+o(t^2)`. Full occupation follows the second event, so these
positive small-time probabilities also imply a positive probability of two
formations by every fixed t>0. Finite-register convergence transfers those
fixed-time probabilities to the microscopic joint limit. The order is first
the joint S/epsilon limit and then the small-t expansion: microscopic jP=0
prevents identifying an initial microscopic derivative with the limiting one.

Neither (18) nor finite fiber spectra prove almost-sure completion from every
later state. No such assertion or exact second waiting law is made here.
Indeed the normalized pullback of total second loss through B1 is

    B1^dagger (sum_j B_j^dagger B_j) B1 / 2
        =8 I+W_square+W_square^dagger,                              (20)

where the square is 0-2-6-4-0 (orientation is immaterial in this sum). The same
formula holds after a coherent first edge mark, with denominator four.
Independent exact path assembly reproduces (20). Electric delta_0 and the
normalizable `(delta_0 +/- delta_square)/sqrt(2)` inputs give instantaneous
second rates 8 kappa, 9 kappa and 7 kappa respectively. Later dynamics includes
K Ecal, (9), and the full loss/recycling operators. A constant-hazard or
unchanged-first-clock approximation is unjustified.

## 7. Independent controls and verification limits

All scientific controls were assembled in this directory without importing
any root builder or previous independent builder.

- `rotor_check.py` constructs both outward grades and the canonical fourth
  coefficient at exact Gaussian-integer cube phases, on number sectors
  4,6,8. Their grade dimensions are (1,16,36), (36,96,36), and (28,0,0).
  It checks C0=M, C1=0, the gated formula, and the ungated zero fourth term.
  An eight-site path additionally checks the nonzero distant-center C1
  contributions and their cancellation. Integer path enumeration verifies
  (14), variance 48, and the complete two-formation witness (17)-(18).
  Reported finite-fiber loss eigenvalues are floating diagnostics only.
- `gram_check.py` reconstructs (20) using exact rational coefficients from
  complete two-mark path sums, retaining all twelve integer link shifts.
  It also checks every local spin matrix weight for S=1,...,7, including
  endpoints and positivity of (2).
- `finite_spin_check.py` assembles complete cyclic physical sectors at
  S=1,2 (dimensions 19 and 39), verifying the constraint/number/grade rules,
  positive C_S, and exact second-coefficient formula to floating roundoff.
  It then builds the complete eight-site path sector (266 states, 65 in P),
  including P populations 4,6,8 and nonzero excited-block C1. Full target
  densities with recycling at S=4,8,16,32 converge to the independently
  constructed rotor target. At delta=.7,K=.4,kappa=.2 and time .6, trace
  errors are approximately .0176173,.00494236,.00131178,.000338123.
  The rotor probabilities of populations 4,6,8 are .236928,.649567,.113506.
  These are finite floating controls, not a convergence-rate proof or a
  microscopic-generator replay. The analytic argument supplies (13).

`run_logged.py` captures actual commands, input hashes, times, return codes,
stdout and stderr. All three runs passed at their original assertions with
empty stderr. No failed execution attempt occurred. The failed simplification
(10), false operator-norm shortcut, and nonconstant second hazard are retained
as explicit countercontrols rather than omitted. Results are preserved in full,
not reduced to PASS counts.

The full-density theorem is conditional on exactly the supplied compensated
interaction and rate/resource scaling. Locality of that interaction is proved;
local-volume error bounds, long times, unique terminal states, physical record
realization, autonomous fuel, and a persistent wave/particle phase are outside
this check. The reconstruction is complete and ready for separately authorized
comparison with the frozen specific author construction.
