# A finite neighborhood detector and its operational effects

2026-11-09 local date. Integrated research result; source comparison tracked
separately. PRIMARY.md preserves the frozen original author argument.
Parent 69c9765a6c29470f541b428c21df41ea909357b8; governing main
bf92a1d763030836ed55631d5d7a7ef3b288f284. Current axiom memo SHA256
301bb33c1a743104208067c14684b34ba71d86674509111638ea898bc6e6c0dc.
Claim type: bounded_theorem. Status: conditional-support, not audited.

Target: implement literal outcome formation and record regrouping on a finite
Z3 patch, construct its operational effects from its process, and test whether
nominal M2 labels become context-independent physical effects. No Born rule,
Hilbert-state dynamics, quantum instrument or axiom amendment is supplied.
The clock/activation rule and prepared apparatus below ARE chosen model inputs.

## 1. Fixed finite layout and data

Every integer v below is the actual matrix content v I in M2(C). Absence is
a distinct condition, never the recorded zero. Use the nine contents
A={0,1,2,3,4,100,101,102,103} times I. Readout returns v from v I; define it
as a single constant "other" on all other unused matrices. This is a finite record code
under the literal axioms, not nine orthogonal states of a quantum qubit.
No physical quantum-capacity claim follows from this content decoder.

In one prepared frame use the following 43 distinct sites:

* Header: 100 at (0,0,0), 101 at (1,0,0), 102 at (0,1,0),
  103 at (0,0,1). These permanent records identify an origin and an ordered
  proper cubic frame; all translations and proper rotations are in the domain.
* Preparation selector s in {0,1,2,3} at (2,0,0).
* Sixteen weight records n_i(t) at (2+i,2+t,0), i,t in {0,1,2,3},
  with nonnegative integer entries and sum_i n_i(t)=4 for each t.
* Four grouping records g_i in {0,1} at (2+i,6,0).
* Sixteen initially blank race sites
  z_j=(2+(j mod 4),8+(floor(j/4) mod 2),floor(j/8)), j=0,...,15.
* Initially blank fine and coarse output sites f=(0,8,0), c=(0,9,0).

There are 25 initial records. All coordinates lie in a box whose L1 diameter
is at most 15. Radius 16 therefore includes the whole apparatus from any of
its sites. This is a fixed finite neighborhood for this family, not an
adjacent-pair actuator or a propagation-speed theorem. Outside sites stay
blank in the declared prepared domain. Seed preparation/genesis is supplied.

## 2. One chosen local law, with no external event scheduler

Fix q=1 or q=2 as part of the law, uniformly for all preparations/programs.
Define m_i=n_i(s)^q and N=sum_i m_i; 4<=N<=16. Race slots 0,...,N-1
are partitioned in outcome order into blocks of lengths m_i. Let b(j) be
the outcome index of slot j. No outcome probabilities are stored as a table.

The legal record prefixes are:

* R0: precisely the 25 seed records;
* R1(j): R0 plus I at race site z_j, j<N;
* R2(j): R1(j) plus (b(j)+1)I at f;
* R3(j): R2(j) plus g_(b(j)) I at c, terminal.

At R0 each of the N race sites has rate one and deterministic content I.
The first birth disables every other race site. At R1(j) only f has rate
one, with deterministic content (b(j)+1)I. At R2(j) only c has rate one,
with deterministic content g_(b(j))I. R3(j) is absorbing. A present record
is never eligible for formation. This is a time-homogeneous record-only
continuous-time process. The equal clocks, their independence, and these
activation/termination rules are supplied, not consequences of the axioms.

Here is a total neighborhood definition rather than an external mask. For
each center x inspect only records at 0<||y-x||_1<=16. Locate the four
header contents, require a proper cubic frame, reconstruct the specified
mandatory seed slots and their values, and check exact equality to one of
R0,R1,R2 restricted to that neighborhood with x absent. Additional visible
records invalidate the match. If exactly one such legal predecessor makes
x an enabled target, assign its stated Dirac content law and rate one.
Otherwise rate is zero and use the fallback law

    F_fallback = (1/2) Uniform(A)
                 + (1/2)[p delta_I+(1-p) delta_0],
    p=(1/2+l)/(1+k),

where k is the number of visible records and l the number equal to I.
Ambiguous headers/matches also use the fallback and zero rate. Formation
additionally requires x to be absent. This formula is defined for arbitrary
matrix-valued neighborhood contents, though the invariant legal record
domain here is only the union of the listed prepared prefixes and their
spatial orbits. It does not assert that arbitrary initial matrix records
are admissible under this law. Every fallback content in A has mass >=1/18.

The rule is translation/proper-rotation covariant, since the frame is read
from records and all spatial tests use the supplied lattice structure. It
uses only scalar contents, hence even independent local algebra relabelings
fix all used values. It is nonconstant; the fallback varies with k,l and
the legal predecessor contexts give Dirac laws. No global site is privileged.

Permanence also requires support, not just never overwriting. For an initial
record x, removing x from the visible condition leaves a mandatory seed hole,
so its conditional content law is the positive fallback. Removing the latest
new record restores its exact predecessor, whose distribution supports that
content. Removing an earlier new record leaves a hole with later output
present, so it matches no predecessor and receives the fallback. Therefore
every record remains admissible at every reachable prefix. At most three
births occur. The minimum of finitely many exponentials and the two later
rate-one waits are finite almost surely, so each run terminates on literal
Z3 with 28 permanent records. The mean completion time in the chosen rate units is 1/N+2. No measured
time unit or infinite-volume ordering assertion is inferred.

## 3. Derived probabilities and an actual coarse record

For the selected independent rate-one clocks,

    Pr(j wins) = integral_0^infty exp(-t) exp(-(N-1)t) dt = 1/N.

The later writes are deterministic. Hence the fine outcome probability is

    p_q(i|s,n) = n_i(s)^q / sum_j n_j(s)^q,

and the probability of the actual coarse output record I is

    e_(n,g)(s) = sum_i g_i p_q(i|s,n).

This normalized law is derived from the chosen clock/process mechanism, not
postulated as Born probabilities. Every menu is normalized, including refined
menus. Empty outcome blocks have probability zero and produce no winner.
Every run retains the winning race record and the fine output after the
coarse record forms. Grouping does not erase either record.

Define an operational effect for this chosen output question as the response
function e:S->[0,1], S={0,1,2,3}. Equal functions are equivalent only for
this output question over these preparations. They need not have equal
entire histories, apparatus states, or future instruments. If disjoint
outcome groups G,H are implemented in this same detector, their response
functions satisfy e_(G union H)=e_G+e_H. The final writer realizes the
grouping physically; it is not just a later algebraic relabeling.

If preparation s is additionally selected by an ordinary classical mixture
pi, total probability gives p(e|pi)=sum_s pi_s e(s). This affine response is
a consequence of that classical mixture construction. It does not determine
an M2 positive cone, noncommuting tests, or a quantum composite rule. The
space of response functions is an operational summary of a chosen process,
not an added ontic state and not a prediction before the process is supplied.

## 4. Exact diagonal bridge for the linear-channel constructor

Restrict the preparation interface to s=0,1 and set q=1. A mathematical
embedding of these two classical alternatives into M2 requires a chosen
pair P0,P1 of complementary rank-one orthogonal projectors. This is an
explicit coordinate/calibration choice, not selected by the scalar records.
Define the NOMINAL program labels

    E_i = [n_i(0)P0+n_i(1)P1]/4.

Since N=4 for every preparation, the derived response pair of outcome i is
exactly (n_i(0)/4,n_i(1)/4). Thus the operational effect can be represented by
E_i. All 25 diagonal effects with both entries in {0,1/4,1/2,3/4,1} occur
in binary programs. For each summable pair of these effects, a three-outcome
program uses their two integer columns and the remainder to 4. There are
15^2=225 such ordered pairs. Its coarse output has the summed effect.

Merging program weights before running the q=1 constructor gives the same
coarse response as running the fine device and writing its grouped output.
This cross-program equality follows from the actual counts and equal clock
law; it is not assumed as an abstract noncontextuality postulate. The
linearity of channel allocation n -> n identical clocks is a supplied
physical architecture. Identifying the resulting DIAGONAL representation
with physical quantum effects is still a calibration choice.

For pi=(pi0,pi1), rho=pi0 P0+pi1 P1 gives p=tr(rho E). This is ordinary
classical probability embedded into a commuting matrix algebra. It is not
a derivation of the noncommuting Born rule. The finite effect domain is not
all positive effects in M2, and no density/state ontology is adopted.

## 5. A normalized neighboring construction that separates the two equalities

Keep all the layout, record laws, permanence proofs and equal clock rates,
but use q=2. Compare programs, for each preparation, with weights

    direct: (2,2,0,0), group first outcome;
    refined: (1,1,2,0), group first two outcomes.

The nominal grouped matrix label in the two-preparation diagonal convention
is I/2 in both devices. The direct constructor has 4 versus 4 active race
channels, giving coarse probability 1/2. The refined constructor has 1+1
versus 4 channels, giving coarse probability 1/3. Its fine weights are
(1/6,1/6,4/6,0), which sum to one. Its actual merger faithfully writes the
sum 1/3. This repairs the limitation of the previous binary-only alternative:
there is now a full normalized formation process for every allowed menu.

The failure is the NOMINAL matrix identification across two device contexts,
not ordinary event additivity. Both constructors have valid operational
effects, and both can be represented by diagonal matrices of their actual
responses. Relabeling E after observing p makes a trace formula true by
construction; it does not explain the response probabilities or establish
that the original algebraic program label was the physical effect.

Within the broader count-rate model p_i=w(n_i)/sum_j w(n_j), w(0)=0 and
w(k)>0 for k>0, demanding equality under merging weights a,b in the presence
of a spectator c>0 forces

    (w(a)+w(b))/(w(a)+w(b)+w(c))
      = w(a+b)/(w(a+b)+w(c))  ==>  w(a+b)=w(a)+w(b).

For the fixed total-4 integer menus, (a,b,c)=(1,1,2) and (1,2,1) force
w(2)=2w(1) and w(3)=3w(1). w(4) is not fixed by outcome probabilities:
it appears only in a single nonzero outcome, so its scale cancels. It can
affect waiting times. Thus the finite selector constrains the observable
law without falsely claiming to determine every microscopic rate. This
is an implication under the additional cross-program equivalence requirement,
not a proof that the axioms impose it.

## 6. Test the next noncommuting identification, not just a smaller reduction

Use all four preparation selectors and q=1. A valid program sets
n_0(s)=4 for s=0,1 and 0 for s=2,3; n_1(s)=4-n_0(s), n_2=n_3=0.
Group only outcome 0. The actual response vector is e=(1,1,0,0).

Attempt the EXTRA quantum calibration identifying these four preparation
tags with Pz+,Pz-,Px+,Py+, and seek a single effect 0<=E<=I whose usual
matrix pairings reproduce those four responses. The two z responses force
both diagonal entries of E to be one. Positivity of I-E then forces E=I,
which would give x and y responses one, contradicting the actual zeros.
Equivalently, linear tomography gives E=I-sigma_x-sigma_y, with determinant
-1. It is not positive. This is a direct test of that candidate calibration,
not a use of the Born formula to generate the record probabilities.

Thus even having literal record events and positive affine operational
effects does not automatically identify their ordered space with the
positive effects of M2. Four distinguishable classical preparation tags
are not four calibrated nonorthogonal quantum preparations merely because
their sites have possibility domain M2. The detector in this construction reads s as a classical preparation-label
record. It has not been restricted to a quantum carrier without that side
information. A genuine qubit accompanied by a readable preparation label
could also be distinguished using the label. This witness does not rule out
a different native law, a restricted quantum sector or a derived calibration.


### A stronger interface test without fixing Pauli labels

The independent proof supplies a general-program corollary. Choose one fixed
program n_i(s)=4 delta_(i,s). Both q laws produce fine outcome i=s with
certainty for all four input selectors. Suppose the ENTIRE declared interface
could be represented by densities rho_s on C^d and one common POVM {E_i},
with tr(rho_s E_i)=delta_(s,i). Since 0<=rho_s<=I and E_s>=0,

    1=tr(rho_s E_s)<=tr(E_s),
    4<=sum_s tr(E_s)=d.

Thus d=2 is impossible for that full interface, even allowing arbitrary mixed
preparations and arbitrary positive effects. This is a test of the desired
quantum representation, not the Born rule used as the detector's dynamics.
It does not assign dimension two to the whole 43-site apparatus. It also
does not exclude a qubit plus a classical label: the detector explicitly has
such label access. It shows why the physical input boundary, allowed readout,
and restrictions on accessible preparation information matter. The literal
matrix-content code alone supplies none of those restrictions. The corollary
is a hand proof for a legal program; no extra numerical case is claimed.

## 7. Closure and remaining physical obligation

The finite constructor supplies actual record formation, a physical grouping
writer, and operational effect addition without Born. Its q=1 sector also
has an exact finite commuting-matrix representation and cross-program
regrouping. These depend on supplied clocks, prepared program, record code,
finite neighborhood and linear channel architecture. The q=2 process and
four-preparation witness expose the additional physical identification that
has not emerged from the axioms. No new physical principle is adopted.
This is not a necessity or minimality theorem for changing the foundation.

The construction concerns one prepared detector patch. It proves no Bell
locality, quantum composite law, vacuum or mass gap. Spatial neighborhoods
have fixed radius 16 here; no bound on a microscopic propagation speed is
inferred. The [assumption ledger](ASSUMPTIONS.md) and
[scoped route check](NO_GO_DISCIPLINE_CHECKLIST.md) state these boundaries.
The operational-effect viewpoint is standard; see Peter Janotta and Haye
Hinrichsen, sections 2.2-2.3 of https://arxiv.org/abs/1402.6562. The finite
process, response functions and comparison calculations are proved above.
