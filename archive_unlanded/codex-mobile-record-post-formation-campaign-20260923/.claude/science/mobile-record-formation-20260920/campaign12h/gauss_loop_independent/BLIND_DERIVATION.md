# Blind reconstruction: constrained record loops

This derivation uses only the task's definitions. No primary Gauss-loop
note, checker or result was read before this document and its checker were
sealed. It concerns a supplied thirteen-state construction, not a deduction
of a physical field theory or an audit verdict.

Let V=N^3, N odd and N>=7. At a site there is vacancy or one of
+/-A_i,+/-B_i, i=1,2,3. The corresponding E or B vector is a signed coordinate
unit vector; the other vector is zero. All norms below use unnormalized
counting measure over sites and both divergence fields.

## Exact loop and movement identities

For a loop in plane ij centered at c, its four E records (or four B records)
are at c-e_j:+e_i, c+e_i:+e_j, c+e_j:-e_i, c-e_i:-e_j.
In D2 each record contributes at the two endpoints of a length-two link
with that record as midpoint. The eight contributions cancel pairwise at
the four corners c+/-e_i+/-e_j. Hence D2E=D2B=0 exactly.

Translate these four records by any single +/-e_k into four vacant targets.
The target set is distinct and disjoint from the source set for N>=7.
The translated loop still has zero divergence, so adding it to any unchanged
divergence-free background after removing the original loop preserves the
constraint. The labels are transported unchanged. There is no preferred
translation direction. The construction requires all four targets vacant;
it does not assert that arbitrary congested configurations admit a move.

For a nearest-neighbor swap across (x,x+e_j), write
d_E=E(x+e_j)-E(x), and similarly d_B. With D=D2/2,

    ||delta DE||_2^2+||delta DB||_2^2=|d_E|^2+|d_B|^2.

For each component the four impulses have amplitudes +/-d_i/2 at
x-e_i,x+e_i,x+e_j-e_i,x+e_j+e_i. On this torus their supports do not
overlap between different components. Thus every unequal-label swap
creates a nonzero Gauss defect from a constrained configuration. The
squared centered norm is 1 for record/vacancy, 2 for distinct axes or
distinct species, and 4 for opposite labels on the same species/axis.
A volume-averaged norm would divide the squared value by V.
D2 instead of D multiplies the squared norm by four.

Circulation reversal is the joint permutation swapping the two opposite
i-label positions and the two opposite j-label positions. The resulting
field is the negative loop and has zero divergence, with every label
preserved. Either opposite-site swap alone has centered divergence norm
squared 4. Therefore reversal must be one joint constrained event; its two
swaps cannot be regarded as separately Gauss-preserving steps.

An explicit empty-site reuse history is: form an A loop at c; translate it
by e_k; form a B loop at the vacated original four sites. Each step obeys
the constraint, every site has at most one record, the first four labels
persist, and the final state has eight records. This demonstrates departure
and reformation without a global record deletion rule.

## What is being counted

For one species, interpret a record at r with vector +e_i as the oriented
edge from r-e_i to r+e_i of the step-two graph (the reverse sign reverses
the edge). The sign convention for incidence is immaterial. D2=0 says
the integral directed flow is balanced at each vertex. Every nonempty
finite balanced flow decomposes into directed cycles. The site capacity
also forbids occupying both orientations of the same edge.

Because 2 is invertible modulo odd N, the step-two graph is isomorphic to
the nearest-neighbor cubic N-torus. With N>=7 it has no triangle or
five-cycle; its shortest cycles have length four and are exactly elementary
coordinate plaquettes. Their midpoint records are exactly the supplied loops.
There are 3V plaquettes and two orientations, hence 6V four-record states
per species. A mixed state cannot have fewer than four records of each
nonempty species. This proves the counting rather than assuming a dilute
independent-loop gas.

For the static constrained law

    mu_z(eta)=Z_N(zA,zB)^(-1) zA^nA zB^nB
                1[D2E=D2B=0],

the first terms at fixed volume are

    Z_N=1+6V(zA^4+zB^4)+O_N((|zA|+|zB|)^6),
    E_mu[nA]/V=24zA^4+O_N((|zA|+|zB|)^6),
    E_mu[nB]/V=24zB^4+O_N((|zA|+|zB|)^6).

There are admissible six-record rectangles, so degree six is a real
possible next order. All remainders here are fixed-volume analytic
statements. Their bounds have not been shown uniform in N.

## Fourier covariance, including the zero mode

Use Ehat(k)=V^(-1/2) sum_x exp(-ik.x)E(x), k=2pi m/N, and analogously
Bhat. Global sign reversal of either species is a symmetry, so both means
vanish and the entire E/B cross covariance vanishes exactly, for all
fugacities. Translation invariance gives a delta between equal wave vectors
when the second Fourier variable is conjugated.

Put s_i=sin(k_i). The Fourier amplitude of an ij loop centered at c is

    (2i/sqrt(V)) exp(-ik.c) [s_j e_i-s_i e_j].

Summing its two circulations, three planes and all centers gives

    E[Ehat(k) Ehat(k)^*]
       =8zA^4[|s|^2 I-s s^T]+O_N((|zA|+|zB|)^6),
    E[Bhat(k) Bhat(k)^*]
       =8zB^4[|s|^2 I-s s^T]+O_N((|zA|+|zB|)^6).

The exact constraint is s.Ehat(k)=s.Bhat(k)=0. For odd N only k=0 has
s=0. At every nonzero k the leading matrix has rank two. Its coefficient
vanishes quadratically as k approaches zero: it is not a constant-amplitude
transverse projector and does not itself establish a Coulomb phase.

The zero mode is not constrained to vanish in the full mu_z ensemble.
A straight winding line of N equal +A_i records has D2E=0 and total
E=N e_i, and the reversed line has opposite total E. Any balanced flow
with nonzero total vector has at least N records: each cycle's signed
step counts are multiples of N, and total population bounds their l1 norm.
At population N these are precisely straight winding cycles. There are
two orientations and N^2 transverse positions per axis. Consequently the
first nonzero zero-mode coefficients are

    E[Ehat(0)Ehat(0)^T]
        =2N zA^N I+O_N((|zA|+|zB|)^(N+2)),
    E[Bhat(0)Bhat(0)^T]
        =2N zB^N I+O_N((|zA|+|zB|)^(N+2)).

Population N+1 cannot have nonzero total vector: below 2N the only possible
nonzero flux has l1 norm N and odd parity, whereas N+1 is even. Adding the
other species costs at least four records. These facts justify the stated
next-order remainder. At N=7 the independent direct winding sum gives
coefficient 14I, with 294 winding configurations per species.

## Exact phase integral and the XY distinction

Introduce compact phases theta_x and phi_x in [0,2pi). Fourier-projecting
the integer divergences gives exactly

    Z_N = integral product_x[dtheta_x dphi_x/(2pi)^2]
          product_r {1
            +2zA sum_i cos(theta_(r-e_i)-theta_(r+e_i))
            +2zB sum_i cos(phi_(r-e_i)-phi_(r+e_i))}.

The global phase shifts represent redundant total-divergence constraints
and need no extra normalization. Crucially, hard capacity gives a SUM
of the vacancy, A and B alternatives at each site. It does not give a
product of independent species factors or independent bond factors.

For zA+zB<1/6 each local factor is positive, so the formula is a positive
coupled compact-phase weight in that restricted range. Its logarithm
contains mixed-species and multi-bond interactions; it is not the usual
factorized positive XY measure. For general positive fugacities even
pointwise positivity fails. On N=7 take theta=pi at +e1,+e2,+e3 and zero
elsewhere, and phi=0 everywhere. At zA=1/4,zB=1/100 the local factors
are -11/25 once, 14/25 three times, 39/25 nine times and 64/25 at the
remaining 330 sites. The whole integrand is negative.

A restricted four-site diamond provides another exact control. Allowing
all thirteen labels on those four sites and fixing the rest vacant yields
Z_restricted=1+2zA^4+2zB^4. Independent species factorization would falsely
include 4zA^4 zB^4, corresponding to double occupancy of the same sites.

## Dynamics, sectors and limitations

The static mu_z definition is not automatically stationary for the
one-way loop-formation dynamics. Empty has positive outgoing birth rate
and no incoming transition if no deletion is supplied. Detailed balance
with that grand-canonical law would require an explicitly chosen reverse
move/rate or another sampler. No such sampler is part of this brief.

All supplied exchanges preserve species populations, while each loop birth
adds four to one population. Thus nA and nB modulo four remain fixed.
All loop births have zero total vector; translations and reversals preserve
it. Starting empty stays in zero total E/B flux and populations divisible
by four. The full constrained measure includes straight winding states
and even zero-flux six-record rectangles that lie outside these sectors.
Therefore Gauss admissibility, dynamical reachability and a chosen static
ensemble are distinct. No irreducibility claim follows from the moves.

Odd N>=7 matters for the simple first coefficient: smaller or even tori
can introduce shorter winding cycles or additional centered-divergence
zero modes. No uniform thermodynamic convergence, phase transition,
long-distance correlation law or phase stiffness follows merely from these
finite-volume coefficients. A uniform convergent expansion or a separate
phase theorem would be needed. Establishing such a theorem is outside this
bounded check.

## Independent controls and seal

blind_check.py imports no primary source and ran once successfully.
Its ten integer/rational control groups cover 12 loops, 72 translations,
507 swaps, atomic versus sequential reversal, departure/reformation,
minimal-cycle enumeration, Laurent covariance coefficients, a six-record
sector witness, the zero-mode winding sum, 28,561 restricted assignments,
and the explicit negative phase weight. Full output is BLIND_CHECK.log;
BLIND_RESULTS.json records identities and runtime versions. No failed
execution occurred. PRE_SOURCE_SEAL.json binds these artifacts before any
primary-source comparison.
