# Source-bound comparison of the local compensation and locality extension

2026-09-23. Bounded post-PRE mathematical comparison, not a formal audit or
publication disposition.

**Disposition:** No material mathematical discrepancy or required source
correction was found in the two authorized packets. The full density/domain
argument and cube field calculation agree with the sealed blind reconstruction.
The author additions—the all-mark second-event coefficient, exact ungated
sum-of-squares construction, restricted necessity/detuning argument, and
first-sector formula on general simple bipartite graphs—were reconstructed
and checked separately below. The PRE has not been altered.

## 1. Exact sources and read boundary

The independent PRE remains
`bc1f83597d26466a02d2a1375fea91624b3adb99dcac25f7902262935a9feeb2`,
binding 9 sources and 25 artifacts. Its REPORT remains
`bb92e2a7367db959390d29c3ee9724fdafd25a200ea7ad6a66ac3f2433ae0312`.
All 34 bindings were reauthenticated before comparison and again at final
sealing.

Authorized author seals:

- `local_compensation_author/LOCAL_CONSTRUCTION_AUTHOR_SEAL.json`,
  SHA256 `88d002cd35fb4b71859bc23efe2f41d465dd2ac5c33a0826db596934189f70b3`.
- `local_compensation_locality_author/AUTHOR_SEAL.json`,
  SHA256 `b275ae727810f32fe3c2721e2c3d294a8dfc9873f5a4a97344590217ffe76413`.

The complete new arguments read were:

- `LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT.md`,
  `42ec5430a0f49c9b6e70577be601df72e23d881b7ef152186de2cdb1ff3faba4`;
- `UNGATED_SUM_OF_SQUARES_AND_TUNING.md`,
  `d67499010fcd7659b7e245bb05c33f64069db1691f57446477506cfcad11fa16`;
- `LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS.md`,
  `5539bbe3171ba21933aa42c4cc191b787029e5f5c9220dc8c3ee255e4906f582`.

All three new author control sources were read completely:
`local_compensation_check.py` (6c8abe65...), `mechanism_check.py`
(b6ceb181...), and `general_graph_locality_check.py` (7319cca1...). Their
complete result fields, actual run receipts and log contents were inspected.
The repeated JSON log bodies were authenticated against the result files;
all distinct log prefixes were read. One combined tool response truncated the
mechanism result; a subsequent compact read explicitly covered all 36 mark
rows and every remaining field. No truncated response was treated as a
completed read.

The physical cube source binding at 20f0a6a... was inspected only for its
integer tree/chord construction, grade/offset/hop/weight functions and finite
spin-state enumeration. The bound second-event source at 4827171... was
inspected for graph, charge, hop, birth, Gauss and effective-path definitions.
The original-model cube consequence was not read as a theorem premise or
re-reviewed. Those modules were not imported or executed by this comparison.
The unchanged general compensation theorem and its separately acknowledged
self-adjointness wording correction were reused at their already checked
identities. Every source binding in both authorized seals authenticates.

The locality draft seal records 20:11:23 UTC and the exact-control receipt
20:13:52 UTC, both binding the same frozen note/runner now compared. The root
reported these preceded receipt of the independent same-formula progress
message. The local-pair identity and proof were already present in the blind
PRE; this comparison does not retrofit the author additions into that history.
The larger-graph first-sector count below is a post-source check of an author
addition, not a claim that it was established in the PRE.

No proposal, current checkpoint, Git surface, unprepared-cube consequence,
publication surface or other new frontier directory was opened. No author
source or prior independent artifact was edited. No author runner was rerun.

## 2. What was already established independently before comparison

The blind reconstruction proved, with the author's definitions and the same
canonical block convention,

    P C_S P=M_S+D/c_S,
    H2_S^C=D/c_S,
    H4_infinity^C=-2 sum_(a<c, distance(a,c)=2)
                            P(F_c F_a)^dagger F_c F_a P.          (1)

It checked positivity, Gauss/number preservation, radius-two support and
uniform boundedness of C_S. Its bound sum_a(z_a^2+z_a) is slightly sharper
than the author's sum_a(z_a^2+2z_a); the latter is valid and is not a defect.
It also independently established the full statewise joint-spin density
limit, the cube scalar -84 and six plaquette coefficients -2, and an explicit
accessible two-mark isometry from the original all-A-plus sector. Those
arguments and controls are reused, not rerun for additional PASS counts.

The author retains precisely the same finite-S canonical normalization and
excited-block term. On the cube C_S vanishes on every W>=1 sector, not just
W=1: an occupied center's gate sees any other vacant A, while a vacant center
has zero bracket. Thus C1=0 there is an exact identity. On larger graphs the
nonzero distant-star C1 contributions must remain and cancel only the
corresponding disjoint-star part of Z^dagger Z/2. Both sources do that.

The local-pair formula in the locality note is identical to (1). Orthogonality
of the two-hole ranges and commutation of the two outward hops give its
coefficient 2. Commutation of different positive S_ac^dagger S_ac terms is
neither true in general nor needed. The bound

    ||H4_infinity^C|| <= |A| z^5(z-1)

follows by bounding at most z(z-1) overlapping A centers per a, counting
unordered pairs once, and using ||F_a||<=z_a. It is an extensive bound,
not a volume-independent total norm.

## 3. Full density convergence and its actual domain scope

The author D is exactly the PRE's Ecal. Its diagonal values are sums of
integer E(E+/-1) over active A-to-vacant-B edges and hence are nonnegative.
The multiplication operator on the physical P rotor Hilbert space is
self-adjoint on its maximal weighted l2 domain, with finite-support core.
Inactive electric directions, including the fully occupied sector where D=0,
do not invalidate this domain statement.

All other limiting Hamiltonian and jump terms are bounded at fixed graph.
Bounded perturbation supplies a self-adjoint Hamiltonian on D(D), and the
Hamiltonian group plus bounded jump/loss perturbation gives a CPTP semigroup
on trace class. General densities need not lie in a commutator domain to have
this mild evolution. Energy expectations and differentiability would require
separate moment/domain assumptions, which the author does not claim.

The proof uses the exact finite-S equality
`delta epsilon^-2 H2_S^C=K D_S`, not merely strong convergence multiplied by a
divergent coefficient. Extending the finite-spin bounded terms by zero and
using the same unbounded K D makes each electric box reducing. Uniformly
bounded strong convergence of those terms and their adjoints then yields
strong trace-class convergence in the common interaction picture, uniformly
on compact time intervals. The fixed-graph uniform-S O(epsilon) theorem
supplies the microscopic-to-target step. This also covers complete recycling
and finite count/mark registers; it is not merely a first-event result.

This argument agrees with the PRE in both proof and qualification. The rotor
limit is for each fixed initial trace-class density and trace-norm convergent
physical approximants. It is not a supremum over every S-dependent initial
density. The author's phrase "all states" concerns the allowed fixed inputs,
not operator-norm convergence of spin shifts or a uniform high-energy family.
No rate for that additional rotor convergence or volume-uniform estimate is
supplied. The field Hamiltonian on the initial sector must not be extended
unchanged beyond a formation: the coupled operator D depends on vacancies.

## 4. Exact ungated sum of squares and the restricted tuning claims

The PRE proved ungated cancellation through fourth order. The author adds
an exact all-order explanation, which is correct for the explicitly different
interaction Cplain=sum_a F_a^dagger F_a, without the diagonal spin repair.
Let h_a=1-n_a. The hard-core tensor-product identities are

    F_a^2=0, h_a F_a=F_a, F_a h_a=0,
    [F_a,F_c]=[h_a,F_c]=0 for a!=c.

At a shared B target both products of creation operators vanish; no fermionic
sign convention is being silently used. Therefore

    W+epsilon T+epsilon^2 sum F_a^dagger F_a
        =sum_a(h_a-epsilon F_a)^dagger(h_a-epsilon F_a).            (2)

For J_epsilon=product_a(I+epsilon F_a), an independent useful exact identity is

    (h_a-epsilon F_a)J_epsilon=J_epsilon h_a.

The product is invertible, with inverse product_a(I-epsilon F_a), so its
common nullspace is exactly J_epsilon P. The positive sum in (2) has that
kernel. For small epsilon this is the separated low cluster, with identically
zero canonical Hamiltonian at every order. The author's cluster argument is
valid also for the bounded infinite-dimensional rotor setting. The zero kernel
identity itself does not require small epsilon; identifying it with a separated
perturbative low cluster does.

`comparison_check.py` verifies (2), the full similarity identity, invertibility
and kernel dimension exactly over rational matrices on the complete 19-state
physical spin-one four-cycle, using epsilon=2/5. The P rank and Hamiltonian
kernel dimension both equal nine. This checks every physical P vector in that
control, rather than only a few dressed seeds. No root builder was imported.
For the ungated spin compensation that *also* contains D_infinity-D_S, the
remaining joint-limit electric term is K D; the exact-zero Hamiltonian claim
is not incorrectly applied to that different finite-S interaction.

The necessity argument is appropriately restricted. At t_S=u/eta the uniformly
bounded fourth and effective dissipative terms contribute o(1), while the
leading bounded H2_S converges strongly to C_(0,infinity)-M_infinity. Hence
the limiting short-time density is conjugated by exp[-iu(C0-M)]. Uniform
ordinary-time convergence including zero to a strongly continuous evolution
would instead return the initial density. Equality on all rank-one densities
for every u forces a scalar on the allowed observable block. If number-sector
coherences are prohibited, the conclusion is scalar only within each allowed
number block. No local-topology, initial-layer, interaction-picture or selected
subspace obstruction is being asserted.

The cube non-scalar premise has an independent physical control: a single
normalizable charge/electric basis component of an actual first output has
mean M=6, ||M psi||^2=44 and variance 8. Thus fixed fractional detuning leaves
a non-scalar fast term even within a fixed-number physical block. Conversely,
`lambda_S=1+nu/eta+o(eta^-1)` adds a uniformly bounded perturbation converging
strongly to nu M_infinity. The same domain and interaction-picture argument
then gives h+nu M_infinity. The source correctly makes neither an optimal
sensitivity claim nor a uniqueness/naturalness claim for the compensation.

## 5. All-mark cube second-formation coefficient

The PRE verified a specified two-mark sequence and the selected first-mark
next-loss polynomial. It did not claim the total all-mark coefficient.
The new comparison code rebuilds every first and second channel with the
independent PRE path builder, retaining all twelve integer link shifts.
For all four combinations of resolved/coherent instruments it obtains

    sum_(j,k) (B_k B_j)^dagger B_k B_j
      =384 I+8 sum_(six faces p)(W_p+W_p^dagger) on Pv.              (3)

This exact aggregate operator is an additional post-source control. It
reproduces all 36 author first-mark Laurent polynomials individually and
all four direct two-mark totals. The nonzero channel counts are respectively
336,168,168,84, with first total 48 and zero-field two-mark norm squared 384.
Thus, for the normalizable zero-electric-field initial vector,

    Pr(N=8 at t)=192 kappa^2 t^2+o(t^2)                            (4)

in the limiting compensated dynamics. For a general fixed density on Pv,
(3) gives the coefficient (kappa^2/2) times its expectation; unitary-loop
bounds give the stated interval [144,240] kappa^2. Finite-support zero field
is a legitimate physical state here, not a fixed Fourier fiber.

The ordered two-jump integral has a continuous integrand at zero because
the jump maps are bounded and the no-event semigroups are strongly continuous.
No differentiation of an unbounded Hamiltonian is required. The fixed-time
microscopic transfer comes from the finite-register limit. Equation (4) is
read in the source's limiting-target context (its Eq. 11); it is not the
Taylor law of the undressed microscopic density at fixed finite S. The joint
limit precedes t down to zero. In particular microscopic jP=0 prevents
silently interchanging these limits.

Equality of (3) for the four instruments concerns this coefficient and does
not identify their entire later quantum histories or densities. The notes do
not use it to prove an exponential second waiting law or almost-sure filling
from every six-record state. At eight records every allowed hop/birth and D
vanishes, so the freeze statement is exact for this supplied target.

## 6. General-graph first-sector formula and locality boundary

The full local-pair theorem was already in the PRE. The author's explicit
initial-sector evaluation is a further correct consequence. A pair a,c of A
sites has z_a z_c-r_ac distinct two-hop destination assignments. Only two
assignments exchanging a pair of common B neighbors share the same final
matter word; their field difference is one four-cycle circulation. Each
unordered pair of common neighbors supplies one W and its adjoint, with unit
coefficient before the -2 in (1). Thus

    H4_initial^C=c_G I-2 sum_(simple unoriented four-cycles p)
                                      (W_p+W_p^dagger),
    c_G=-2 sum_(a<c,r_ac>0)(z_a z_c-r_ac).                         (5)

Pairs of disjoint stars contribute only an original-law scalar. Using
M=|E| I on this initial sector gives

    c_original=sum_a z_a^2+sum_b z_b(z_b-1),                      (6)

with exactly the same four-cycle coefficient. The linear electric term
vanishes by div E=0, so retaining the initial electric and magnetic dynamics
up to a scalar is valid on every fixed simple bipartite graph. It does not
produce a magnetic term on a square-free graph.

A new independently selected nine-vertex irregular disconnected graph tests
this additional count beyond the PRE and author fixtures. Its A set is
{0,2,5,8}; one overlapping pair has three common neighbors, another has two,
and a separate one-edge component has none. Exact canonical path assembly
gives four cycles, c_G=-40, c_original=42 and the predicted eight oriented
loop terms. A physical post-first output separately reproduces the local-pair
formula. Full edges and output identities are in the comparison result.

The effective birth jump is supported on one A star: only that center can
supply the vacancy needed by its edge's formation, and the old destination
must differ from the birth endpoint. Bounding its z_a-1 partial-isometry
terms proves the stated resolved norm bound. The electric terms commute as
multiplication operators. On each finite graph, conjugation by their group
requires only the diagonal terms touching a bounded observable's support;
mutual commutativity prevents successive support spreading from this step.
This supports the source's finite support statement but does not itself
supply an infinite-volume or uniform microscopic approximation. The note
explicitly leaves the remaining interaction-picture dynamics, locality,
state/domain and boundary issues open. Those are not gaps in its stated
finite-graph conclusion.

## 7. Code/evidence correspondence and disposition limits

The author local runner's six complete finite-spin cube cases test the P
identity and gate annihilation; it does not numerically prove the full
trace-density theorem. Its two core vectors and four all-mark instrument
combinations match their stated purpose. The exact mechanism runner checks
rational dressing identities and all first-mark rate polynomials; its
spin-one unit-amplitude convention is correct. The locality runner tests
nine named graphs and 45 particular seeds, including square-free,
disconnected, multiple-common-neighbor and hypercube cases. It does not
claim exhaustive all-charge testing, and its general theorem is proved
analytically rather than by those seed counts.

The complete result/log bindings agree with those implementations and prose.
The scientific source-bound computations were authenticated, not counted as
new independent calculations. The new independent post-source control and
its actual stdout/stderr/receipt are separate. Its additional imported module
`finite_spin_check.py` is an unchanged PRE artifact; all builders are our own.
No failed new run occurred and no threshold or fixture was revised.

The previously accepted general-note self-adjointness wording correction
remains necessary as its separately sealed companion. It is already
acknowledged and is not a new finding in these packets. No additional source
repair is required by this bounded comparison. It confirms the supplied,
fixed-graph conditional construction and the explicitly restricted additions;
it confers no native selection, autonomous resource completion, thermodynamic
phase, volume-uniform microscopic theorem, publication status or formal audit.
