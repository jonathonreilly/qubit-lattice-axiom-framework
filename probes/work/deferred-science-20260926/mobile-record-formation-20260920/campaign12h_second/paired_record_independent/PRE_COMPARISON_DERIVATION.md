# Independent paired-record reconstruction before author comparison

2026-09-21. The complete supplied note was read; the author runner and results
have not been opened. All calculations here use the stated events directly.

## Events, labels and conditional laws

The reciprocal relation makes every occupied site part of exactly one
undirected edge of a matching. The two possible ways to write that edge give
the same two endpoint contents, so birth has one channel per undirected edge,
not two orientation channels. A translation moves both records together;
parallel overlap is handled by first removing the old pair and then inserting
both translated records. Only targets outside the old pair must be vacant.
The inverse translation is valid with the same rate. A qualifying cube has
one opposite-face axis choice, and the four facing swaps are one atomic
channel, not four separate rate-nu events. Its inverse is itself.

These operations preserve capacity, contents and identities. They also preserve
the identity pairing of previously born partners: no event exchanges partners
between dimers. Thus tagged communicating classes can be finer than content
matching classes. The finite 108-state calculation below is the contents
projection, which is Markov because rates do not inspect identities.

All 64 neighbor-vacancy patterns around a vacant origin are feasible on Z^3:
an occupied neighbor d can be matched outward to 2d, independently on each
of the six rays. For each vacant neighbor exactly one incident beta clock
can create the corresponding direction at the origin. Thus h=beta times
the number of vacant neighbors and conditional odds are uniform on those
neighbors, undefined when that number is zero. The events at the two ends
of an edge are simultaneous; these are not independent site samples.

A one-site DLR conditional on the complete exterior is entirely different.
If no neighbor points into x, x must be vacant. If exactly one neighbor
points into x, its direction forces the record at x. Two incoming neighbors
admit no matching completion. In particular, all-vacant exterior forces a
vacant one-site value, whereas a *joint future birth* from the empty state
has six possible partner directions. The note's distinction is necessary.
For periodic degree-six geometry the empty density derivative is 6 beta;
for the reflecting eight-site cube it is 3 beta. Both agree with
L V_vac=-2 beta E_00, counting each empty-empty edge once.

The independent implementation enumerates edge subsets with bit masks,
constructs births/translations/cube channels separately, and verifies their
multiplicities and inverse rates. Actual state-graph covariance is checked
under all 24 proper cube actions; the same supplied elementary rules also
pass the 24 improper graph actions. This latter finite property supplies no
new physical reflection premise. Identity-based histories check all six
translations, including the two overlapping parallel shifts, and renewal.

## Staggered field and Fourier increment

For an even torus or Z^3, sigma_(x-e_i)=-sigma_x. The six incident link
occupancies sum to o(x), giving

    div B(x)=sigma_x [sum_i(n_i(x)+n_i(x-e_i))-1]
            =-sigma_x v(x).

The factor 1/6 is required because there are six incident edges. Each dimer
covers opposite sublattices, so the total formal vacancy charge is zero on
a finite even torus. Birth removes an adjacent opposite-charge pair; the
empty state has a nonzero staggered charge background. Odd periodic size is
outside this readout convention, not an alternative boundary condition for
the reflecting cube.

A signed coordinate map sends a positively based link to a possibly
negatively oriented link, requiring a change of base point. If its affine
translation is t and its direction sign is s, the mapped field is
(-1)^(sum t) s times the old field at the corresponding link. In particular,
a unit translation changes the sign under the fixed sigma convention. The
independent integer implementation checks this covariance, including the
base-point shift, and checks wrapped dimers on an even periodic torus.

For the stated cube, use X=exp(-ik_x), Y=exp(-ik_y), Z=exp(-ik_z). Direct
edge changes give

    Delta Bhat=((Y-1)(1+Z),(1-X)(1+Z),0).

Its backward-divergence polynomial is identically zero. The linear term is
(-2i k_y,2i k_x,0), and the zero Fourier value vanishes. Every cut flux of
this cube increment also vanishes. The two faces add because of staggering.
This is an update increment, not a generator eigenfrequency. The conservative
rates are symmetric by matching each channel with its inverse, so the
finite conservative generator has a real nonpositive spectrum in its uniform
component measures. A local curl increment cannot by itself create waves.

## Reflecting cube: independent enumeration and analytic lumping

Vertices are {0,1}^3 and its twelve ordinary edges. A birth, translation or
cube event is included only if its complete support lies in those eight
sites. No wrapping or exterior vacant targets are allowed. Edge-mask
enumeration gives 108 matchings with census (1,12,42,44,9).

There is an exact ten-class Markov lumping. Its class sizes are:

    empty 1; one dimer 12;
    two parallel dimers on one face 12;
    two parallel dimers diagonally separated 6;
    two nonparallel dimers 24;
    three parallel dimers 12;
    three dimers with orientation counts (2,1,0) 24;
    three dimers with counts (1,1,1), unfilled traps 8;
    full columnar matchings 3; full mixed matchings 6.

Every one-dimer state has seven births: two create face-parallel pairs,
one a diagonal parallel pair, and four nonparallel pairs. Its two allowed
translations stay within the one-dimer class. Every nonparallel two-dimer
state has three birth channels, one of each axis. The previously unused
axis creates a trap; the two used axes create fillable (2,1,0) states.
Translations preserve the two distinct occupied axes. Parallel two-dimer
states can never produce a (1,1,1) three-dimer trap, since orientation
counts never decrease. Hence, independent of waiting times,

    P_empty(unfilled absorption)=(4/7)(1/3)=4/21.

This calculation is checked by a rational harmonic function on all states:
values 4/21 on zero/one-dimer states, 1/3 on nonparallel two-dimer states,
1 on traps, and zero elsewhere. Its generator is zero separately under
each of the three channel families. Every nonclosed state has at least
one available birth, and births increase dimer count at most four times;
with beta>0 finite rates, absorption occurs almost surely. Thus the harmonic
certificate has the required hitting-probability interpretation.

For beta=kappa=nu=1, a separate exact seven-transient-class linear solve
within the ten-class lump gives empty-start probabilities

    unfilled: 4/21; full columnar: 13/49; full mixed: 80/147.

The lumped full-mixed class hides its three distinct two-state components;
the class solve is used for these aggregate events only. Direct reachability
on the entire 108-state graph gives 91 transient states and 14 closed
components: eleven singletons and three pairs. Eight singletons have three
dimers and opposite-corner vacancies. Their remaining induced hexagon is
alternately matched, and all allowed reflecting rates vanish. Three other
singletons are full columnar states; the six mixed full states form the
three cube-exchange pairs, each with exactly one rate-nu channel.

The ten-class generator and complete 108-state birth/translation/cube graph
are archived, making the rate counts and lumpability directly inspectable.
The 4/21 event cannot be transferred to a periodic box, even though an
embedded reflecting cube has the same eight vertex coordinates. Allowing
outside targets changes its transition graph. No periodic accessibility,
Coulomb phase, quantum interface or continuum wave result is inferred.

## Execution record

The first exact Fourier assertion compared factored expression syntax and
failed because -(X-1)(Z+1) and (1-X)(Z+1) are structurally different. Its
source, stdout/stderr and diagnostic are preserved. Their expanded difference
is identically zero. The assertion was changed only to polynomial equality;
the complete second run passed. A third run added the requested fixed-origin
readout covariance and persistent-partner controls and also passed; the prior
successful source and full output are preserved as attempt2. No scientific
premise or expected coefficient was altered. No material defect has been
found before source comparison.
