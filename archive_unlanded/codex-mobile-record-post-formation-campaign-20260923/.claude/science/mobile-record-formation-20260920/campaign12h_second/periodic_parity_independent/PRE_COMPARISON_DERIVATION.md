# Independent reconstruction before author-code access

2026-09-21. This is a bounded check of the two supplied notes, not new
production theory, a simulator review, a phase theorem, or an audit verdict.
The complete notes were read; their identities and unchanged model/procedure
dependencies are in READ_BOUNDARY.json. Neither author runner nor its output
has been opened at this boundary. The checker was written independently with
site-to-identity/content dictionaries and direct global reciprocity tests.

## 1. Periodic absorbing configuration and finite-volume reachability

Use even N >= 4, or the infinite lattice, with the supplied three dimers in
each disjoint period-two cube. Each occupied endpoint has its reciprocal
opposite label one unit away, so the configuration is a matching. There are
three dimers per eight sites and one dimer of each axis per tile.

The vacancies are the parity classes 000 and 111. A nearest-neighbor step
changes exactly one coordinate parity, including a periodic crossing for
even N. Hence no two vacancies are adjacent. A dimer of axis i in the pattern
has unequal parities in the other two coordinates. Its entire axis-i line is
occupied, so even an overlapping axial translation, which needs only its
one new endpoint vacant, is blocked. A transverse translation would require
an adjacent vacant pair. Every unit cube has exactly one of every parity
triple and hence two vacancies, so none supports the original full-cube
event. These observations exhaust the original supplied event list.

On a finite torus the prescribed matching can be built from empty by creating
its disjoint edges in any fixed order. Each requested birth remains available
and has positive rate; a finite sequence of such events has positive
probability when competing total rates are finite. This proves failure of
almost-sure full packing for the original process, not a positive lower bound
uniform in N and not a typical-density claim. No analogous positive-probability
infinite birth history has been used.

The finite orbit under translations and proper cubic rotations consists of
absorbing configurations because the original rule is covariant. Its uniform
mixture is stationary and symmetry invariant. Its vacancy indicator obeys
V(x+2z)=V(x) in every configuration of the orbit. Therefore its connected
vacancy covariance at every even displacement is Var(V(x))=3/16. This is
explicit periodic long-range order in a nonergodic mixture, not a selected
formation state.

## 2. Reflecting cube, parallel-swap family, and actual escape

If a reflecting cube has one dimer of each orientation, the coordinate-i cut
is crossed once. Each of its faces has an odd number of occupied vertices,
so each has an odd number of holes. There are only two holes; there must be
one on each face in every direction. Thus the holes are opposite corners.
This remains true for any rearrangement confined to the cube that preserves
axis counts and produces a matching. It does not depend on the available
permutation supports.

For a cube and axis, its four parallel edges are disjoint. Any nonempty
subset defines a site permutation P with P^2=identity. The acceptance
condition is P eta in the set of global reciprocal matchings. If eta and
P eta are valid, the inverse channel is accepted at P eta and has the same
rate. Summing channels preserves detailed balance, including duplicate site
permutations represented in different cubes. Consequently the finite-volume
uniform matching measure, and mixtures of its invariant count sectors, are
reversible when births are absent. Any infinite-volume formulation of a
uniform law requires its usual local conditional-uniform meaning; no unique
infinite-volume measure or mixing is established here.

There are 3(2^4-1)=45 attempted channels per cube. The multiset, including
multiplicities, maps into itself under translations and signed coordinate
permutations with the corresponding polar action on the six directions;
this includes the claimed proper cubic subgroup. A site's reciprocity can
change only if that site or its prospective partner changed. Checking the
changed sites and all their nearest neighbors is therefore sufficient.
The update support is the cube; its decision reads a bounded neighborhood.
All moved records keep their identity and direction and move one lattice
step. Unchanged contents can still conceal a swap of equal-label identities.
The extension does not require permanent *partner identities*: for example,
swapping only two adjacent +x records in a full x-columnar state keeps the
contents and matching valid while changing their identity-labeled partners.
No permanent-partner invariant from the smaller rule is imported here.

In the proposed three-edge y-swap, the +z and -z records move from 010,011
to 000,001; the +x and -x records move from 001,101 to 011,111. The y-dimer
is fixed. Exactly four old identities take one nearest-neighbor step. The
holes are now 010 and 101 inside the cube. The neighboring hole 020 was
untouched, so 010--020 is a legal birth edge. It increases the population
by two without altering any old record. Applying the three swaps twice
recovers the exact identity-labeled initial configuration.

The independent checker finds zero original exits on N=4,6,8, populations
48->50, 162->164, 384->386 after this history, and the same four displacements
in each case. It separately enumerates all 108 reflecting-cube matchings;
exactly eight have one dimer per axis, and all have opposite holes. On N=4
it checks every one of the 2880 attempted extension channels on five chosen
states for exact inverse and content-count preservation. It also checks the
entire channel multiset under all 48 signed coordinate permutations and the
three unit translations. There are 1920 distinct site permutations: 1344
with multiplicity one, 384 with multiplicity two, and 192 with multiplicity
four. These multiplicities matter if the supplied clocks are implemented.

## 3. Count parity and the nonfrozen two-hole obstruction

Let chi_i(x)=x_i mod 2. An i-dimer contributes 1 to the sum of chi_i over
occupied endpoints modulo 2, and a dimer of any other direction contributes
0. The sum over all N^3 sites is N^3/2, which is even for even N. Subtracting
occupied sites proves

    M_i = sum_{x vacant} chi_i(x) (mod 2).

Full packing therefore has even M_i for all i. With two holes and three odd
M_i, their coordinate parities differ in every direction; they cannot be
nearest neighbors. Any conservative permutation preserving the six content
counts preserves this obstruction, irrespective of locality or rate. A last
paired birth is impossible. This does not imply that conservative activity
ceases. Conversely, a single odd M_i is only a necessary parity pattern for
adjacent holes; it does not force adjacency and does not explain every jam.

Removing the four x-dimers of one cube in a fully x-columnar matching and
replacing them, as a *configuration specification*, by the three-dimer pattern
gives counts (N^3/2-3,1,1) and exactly two holes. The checker verifies counts
(29,1,1), (105,1,1), (253,1,1) for N=4,6,8. On N=4 this state has three
content-changing extension channels, so it is an explicit nonfrozen state
with the final-birth obstruction. Its birth-only finite construction gives
positive finite-volume probability of entering an unfillable sector; it does
not describe a legal count-changing conservative conversion of old records.

The even-period assumption is substantive. On N=5, a single x-dimer wrapping
from 400 to 000 has M_x odd but an even vacant-coordinate-parity sum. The
checker includes this excluded-hypothesis countercontrol.

## 4. Fourier identity, complex projection, and scaling

With sigma_x=(-1)^(x_1+x_2+x_3), reciprocity gives

    sum_i [B_i(x)-B_i(x-e_i)] = -sigma_x 1{x vacant},
    B_i(x)=sigma_x[n_i(x)-1/6].

Use Fourier normalization N^(-3/2) and phase exp(-ik.x). Then the row
constraint is d.Bhat=qhat with d_i=1-exp(-ik_i). Its Hermitian normal vector
is conjugate(d), since <conjugate(d),Bhat>=d.Bhat. For nonzero lattice momentum
modulo 2 pi,

    P_L Bhat = conjugate(d) qhat / ||d||^2,
    ||P_L Bhat||^2 = |qhat|^2/||d||^2
       <= m^2 / [4 N^3 sum_i sin^2(k_i/2)].

No stochastic, stationary, independence, or equilibration assumption enters.
At k=K/N, K=2 pi ell != 0 fixed, the denominator is asymptotic to N|K|^2.
For N >= 2 max_i |ell_i| it is at least 16 N|ell|^2, so a uniform finite-N
bound is available as well. Thus m_N=o(sqrt(N)) implies the longitudinal
amplitude tends to zero, and E m_N^2=o(N) suffices for its L2 convergence.
Finitely many fixed modes follow by summing their bounds. K=0 is excluded;
for any fixed nonzero integer ell, accidental small-N aliasing disappears
for sufficiently large N.

For two holes the *squared norm* is O(N^-1), while the norm is O(N^-1/2).
The source's last O(N^-1) sentence is correct when read as the bound in its
displayed equation (2); it must not be interpreted as an amplitude bound.
This distinction is sharp. For N divisible by four, keep a full x-columnar
matching except on one x-line. Leave holes at 0 and L=N/2-1 along that line
and pair consecutive remaining sites on the two intervals. For K=2 pi e_x,

    ||P_L Bhat||^2 = sin^2(pi L/N) / [N^3 sin^2(pi/N)],
    N ||P_L Bhat||^2 -> 1/pi^2.

The checker constructs these valid matchings on N=4,8,16,32. This example
also separates small residual population from a stronger, unjustified
amplitude estimate.

An exact genuinely complex N=4 control uses the all-odd sector and mode
ell=(1,2,0). It gives d=(1+i,2,0), q=(-1+i)/8,
Bhat=(-1/8,i/8,1/8), ||P_L Bhat||^2=1/192, and bound 1/96. Replacing
conjugate(d) by d leaves constraint residual -i/12 and is decisively wrong.
Integer real-space Gauss checks and six additional finite Fourier checks
are recorded. None supplies the vacancy scaling for a formation process,
transverse covariance, a nonzero continuum field, a phase, or wave motion.

## Preliminary disposition and read boundary

The mathematical claims reconstruct correctly at the supplied even-period,
matching, channel, and Fourier hypotheses. No substantive defect has been
found before author-code comparison. An optional wording clarification is
to name the squared norm explicitly in the two-vacancy O(N^-1) sentence.
The author-data assertions about named pilot/screen endpoints remain unchecked
at this seal; they will be assessed only after this independent record is
frozen. No simulation kinetics or phase inference will be reviewed.

The independently written checker passed on its first execution. Full stdout,
stderr, result JSON and execution receipt are retained; there was no failed
attempt to discard. PRE_COMPARISON_SEAL.json will bind all these bytes before
any author runner/results access.
