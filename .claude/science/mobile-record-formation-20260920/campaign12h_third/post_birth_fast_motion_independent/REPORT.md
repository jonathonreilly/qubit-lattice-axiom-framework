# Source-informed review of post-formation fast vacancy motion

No required mathematical correction was found. The supplied six-site model has
an exact infinite-path fast-motion limit, and the stated vacancy-return law
follows. The microscopic approximation is uniform on compact **fast-time**
intervals and in spin; it is not a fixed nonzero laboratory-time assertion.
This is source-informed bounded scientific review, not a blind reconstruction,
formal audit, publication decision, or a continuation of the preceding general
dissipative theorem's scope.

## Source and verification boundary

The complete reviewed note is
`post_birth_fast_motion_author/FAST_VACANCY_MOTION_AFTER_FORMATION.md`, SHA256
`76d7f2faf3a0b4635499ddff1d8a88868d691d58c035780af737129701e30eeb`.
The nine-artifact author seal is
`945fe1a4e76d39c09f435df29409d3dd507af94aed757dfb277f773f4bc5b79f`.
All nine artifacts authenticate. Both complete scientific sources, the complete
current result, receipt and initial execution observation were read. Every old
result field other than its source hash was compared exactly with the current
result: they are unchanged; the new result additionally carries the integer
cycle certificate. The exact source delta is preserved here.

The independent code was written after reading the note but before opening the
author runner. It builds physical states `(q,E)` and performs legal gauge hops;
it does not import or execute an author builder, use the author's Fourier
matrix, or obtain the graph from author results. The independent evidence and
all command streams are retained. No PRE-stage independence is asserted.

## 1. Birth output and exact two-block structure

The physical equation is `E_e-E_(e-1)+b_e-q_e=0`, with background
`b=(1,0,1,0,1,0)`. A charge c hopping in the positive edge orientation lowers
that edge's electric integer by c; a reverse hop raises it by c. Thus the hop
0 to 5 from the initial ice vector raises E5 from 0 to 1 and empties site 0.
The resolved edge-0 plus birth then raises E0 from 0 to 1 and inserts charges
plus at 0 and minus at 1. The result is exactly

    q=(1,-1,1,0,1,1),  E=(1,0,0,0,0,1).

Every Gauss equation holds. The two normalized spin matrix elements are both
one for every integer S>=1. The minus sign in T and the prefactor minus in
`B=-P j T P` cancel, so this vector has amplitude one. No second contribution
exists for this mark: the hop 0 to 1 would occupy the other birth endpoint;
any hop from another A site leaves site 0 occupied. The independent enumerator
checks this complete action, not merely that the proposed output is legal.

There are five records and one vacancy. All pair-birth operators vanish on the
entire number-five sector. There is no subsequent no-event backaction to retain.
The only vacancy is either in B (W=0) or A (W=1), and each hop switches the two.
Consequently the exact Hamiltonian has the displayed off-diagonal T block and
identity high-sector W. Each basis state has at most two incoming/outgoing hops,
each with absolute amplitude at most one. The Schur bound gives `||T||<=2`,
independently of spin, and hence `||A||<=2`.

The vector above is a valid specified conditional post-event preparation and an
actual nonzero effective marked output. This does not assert that the exact
microscopic process, observed at an arbitrary later random birth time, always
prepares that vector. The note makes the preparation explicit and does not need
that stronger assertion. It also does not condition an event to occur at a
fixed deterministic time.

## 2. Uniform singular-block estimate

After setting laboratory time `tau=epsilon^2 u/delta`, the generator of u is

    M_epsilon = [[0,A^dagger/epsilon],
                 [A/epsilon,I/epsilon^2]].

For singular value `sqrt(lambda)` of A, the nontrivial block is two by two.
Its low eigenvalue is

    e_-=-2lambda/(1+sqrt(1+4epsilon^2 lambda)).

The eigenvalue equation also gives

    e_-+lambda=epsilon^2 e_-^2,
    |e_-|<=lambda<=4.

Therefore its phase error relative to `-lambda` is at most
`16 |u| epsilon^2`. The diagonalizing rotation angle obeys
`tan(2theta)=2epsilon sqrt(lambda)` with `0<=theta<pi/4`; hence
`||R-I||<=theta<=2epsilon`. Inserting this rotation at both endpoints gives
the explicit sufficient estimate

    ||exp(-iu M_epsilon)P-P exp(iu A^dagger A)||
        <=4epsilon+16 U epsilon^2,  |u|<=U.               (1)

This estimate includes the small initial high-energy component; it does not
assume low-spectral rather than bare-P preparation. Kernel vectors of A are
exact zero modes and cause no division by zero. The proof extends from finite
singular blocks to the direct-integral spectral representation of `A^dagger A`.
The unmatched kernel of `A^dagger` lies in Q and has no initial P component.
Thus (1) is also valid for bounded rotor A, with no finite-dimensional
multiplicity assumption. The author's O(epsilon) statement follows for bounded
U and epsilon<=1.

Embed each spin box into the integer rotor space and zero-extend its shifts.
The shifts and adjoints converge strongly, have uniformly bounded norms, and
preserve the physical Gauss constraint. Hence `A_S^dagger A_S` converges
strongly to the rotor operator, with a common norm bound four. The exponential
power series, uniformly controlled on compact u intervals, then gives strong
propagator convergence there. Combining this with (1) proves the claimed joint
limit for the fixed normalizable initial vector, along any epsilon->0,
S->infinity sequence, including `epsilon^2 S(S+1)=delta/K`.

This is not operator-norm convergence of spin shifts. Nor does it cover states
whose mass escapes to the spin cutoff without an initial-state convergence
hypothesis. Neither stronger assertion is made by the note. Pure-state vector
convergence implies trace-norm convergence of the corresponding densities and
convergence of the bounded vacancy projector's probability.

## 3. Physical graph, holonomy and exact probability

At number five and charge three there is one minus record, four plus records
and one vacancy. There are 30 charge words and 15 with the vacancy in B. Every
charge word has one integer free circulation coordinate, such as E0; Gauss
fixes all the other fields. In the unit-rotor limit, two hops from a P state
give two immediate returns of weight one and one continuation in each vacancy
direction, each of weight one. Thus

    H2=-A^dagger A=-2I-(forward+backward)

on the lifted P graph. No two distinct forward paths have been collapsed into
one incorrectly normalized edge: at each step there is one intermediate Q
state for each continuation.

The period fifteen can also be understood without trusting a matrix fit.
Each forward P step advances the vacancy by two sites and moves two records
past it. The vacancy returns to its original site after multiples of three
steps. Returning the single minus to its original cyclic record position
requires the total two-step record count to be divisible by five. The first
simultaneous return is fifteen steps. During these thirty microscopic hops,
each of the five records has made one complete circuit opposite the vacancy.
The net field shift on every link is therefore the total transported signed
charge, three (or minus three for reverse orientation).

Our direct integer-state walk confirms all fifteen words, the vacancy order
3,5,1 repeated, and

    E(after 15)-E(before)=(3,3,3,3,3,3).

It continues for sixty steps without identifying two physical states. Since
the charge-word cycle is connected and a complete circuit changes the free
flux by three, the full P lift has exactly three components. Each is an
infinite path; the specified vector selects one. This conclusion uses the
actual integer flux, not just an angle-fiber spectrum.

A Fourier fiber is a fifteen-cycle with holonomy `exp(3i theta)`. Gauge-moving
its edge phases gives eigenvalues

    -2-2cos((2pi k+3theta)/15),  k=0,...,14,

up to orientation reversal. The author's omission of the initial E0=1 global
phase in each fiber does not change its matter probabilities: that phase
cancels before integration. A single fiber is not a normalizable physical
state; the complete Fourier integral is required.

For the normalizable origin delta vector on the physical infinite path,
`exp(iu(S+S^dagger))` has amplitude `i^n J_n(2u)`, up to the scalar phase
from `-2I`. The vacancy returns to site 3 exactly when n is divisible by three.
The characteristic function of n is the angular integral

    E[exp(i alpha n)]
      =(1/2pi) integral exp(2iu[cos(k+alpha)-cos(k)]) dk
      =J0(4u sin(alpha/2)).

The three-root filter therefore gives

    p3(u)=[1+2 J0(2sqrt(3)u)]/3.                           (2)

It is a position probability, not a no-hop, survival, or first-return
probability. In particular `p3(1)=0.08338269583779327` and
`p3(1/2)=0.5862929500285945`. This is substantial movement during the
laboratory interval `epsilon^2/delta`, not a statement about limiting
large-scale transport or a persistent post-event field wave.

## 4. Controls, comparison and limits

The independent complete finite-spin physical sectors have dimensions 39, 99
and 219 for S=1,2,4; their P dimensions are 21,51,111. These are not the
fifteen-dimensional rotor Fourier fibers. Every state's Gauss law and the
complete hopping matrix's symmetry and off-block structure are checked. At
three epsilons and three fast times, direct microscopic propagation agrees
with the bound (1); no author model builder or propagator was used. For
example S=4,epsilon=0.05,u=1 has vector error 0.09438228447400175 against
the explicit upper bound 0.24.

A separate 121-site path exponential at six fast times through u=3 agrees with
both the truncated Bessel sum and (2) to floating precision. This finite path
is numerical corroboration; the Fourier calculation proves the infinite-path
law, and no floating result is offered as an interval certificate.

The author source faithfully builds its 30-state fibers and integer exponents.
The exact certificate agrees word-for-word with the independently generated
physical route. All four stored spectral rows and eighteen probability rows
were recomputed from the analytic formulas; the largest stored spectral
error is 4.44e-15. Every unchanged initial result field matches the expanded
result exactly. Current stdout equals the result JSON byte-for-byte, and the
timed receipt and all source bindings authenticate. The original exploratory
run expressly lacks separate saved timing/stdout; its observation receipt is
not treated as one. The source change adds the graph certificate and changes
the output location; no threshold or scientific parameter was relaxed.

One independent wrapper invocation failed its path guard before the scientific
script started. Its observed traceback and repair are preserved in
WRAPPER_INVOCATION_FAILURE.json. The unchanged wrapper was then called with
its documented basename arguments. Both scientific/evidence runs passed their
first actual executions, with full stdout, empty stderr and timed receipts.
No mathematical failure or negative result has been discarded.

The required bounded obligations are complete. No author correction is
requested. The result is conditional on this Hamiltonian, gauge sector,
resolved output and initial preparation. No later birth is possible in this
sector. It supplies neither a repeated-formation law nor macroscopic-time
averaging, a cubic post-birth field theorem, thermodynamic transport, photons,
fermion statistics, energy/fuel autonomy or native microscopic derivation.
The preceding fast-matter and pre-event field results remain separate. No
unrelated author packet, checkpoint, registry, or Git/audit state was accessed
or changed during this review.

Complete exact source and independent evidence identities are in FINAL_SEAL.json.
