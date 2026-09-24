# High-flux energy spread at an actual cube formation

Root conditional calculation, September 23, 2026. This uses the supplied
compensated hard-core/Gauss rotor target and its unchanged formation
instrument. It is an exact finite-cube family of normalizable states, not
an autonomous energy source, a native-framework derivation, or a claim about
the unchanged microscopic Hamiltonian. The new calculation has not yet had
an independent reconstruction.

## Physical family and the actual marked event

Take the cube with vertices labelled by three binary bits, edges oriented
from smaller to larger vertex, and A={0,3,5,6}. Its effective Hamiltonian is

    h=K D+delta H4,       H4=-Z*Z/2,       K,delta>0,           (1)

on the penalty-zero physical rotor space. H4 is bounded on this fixed cube.
On the first, all-A-positive and all-B-vacant sector, D=sum_e E_e^2. On
later sectors, D is the sum of E_e(E_e+k_e) only over legal outward hops
from occupied A sites to vacant B neighbors. The target and complete
post-formation density construction were checked in the local-compensation
publication unit; here (1) remains a supplied conditional model.

For any integer n>=0, let |Omega_n> have q=1_A and the divergence-free
field circulation

    E_(0,1)=n, E_(1,3)=n, E_(2,3)=-n, E_(0,2)=-n,          (2)

with every other field zero. This is a normalizable charge/field basis
vector, not a fixed Fourier fiber. Its exact electric value is

    D |Omega_n> = 4n^2 |Omega_n>.                         (3)

Use the actual resolved first mark on edge (0,1), creating + at vertex 0
and - at vertex 1. The old + at 0 must first move to either neighbor 2 or
neighbor 4; moving it to 1 would block the birth. The two resulting
physical basis vectors, |phi_(2,n)> and |phi_(4,n)>, are orthogonal, each
with amplitude one in B_(0,1,+)|Omega_n>. Their record charge words differ.
Direct Gauss shifts are: old hop 0->2 lowers E_(0,2) by one, old hop 0->4
lowers E_(0,4) by one, and birth raises E_(0,1) by one. No unlisted
preparation, field measurement or modified instrument is used. Therefore

    B_(0,1,+)|Omega_n> = |phi_(2,n)>+|phi_(4,n)>,
    ||B_(0,1,+)|Omega_n>||^2=2.                        (4)

The first output has both B vertices 1 and 2 occupied. Every high-flux
edge of the chosen face is then incident to an occupied B and drops out
of D, so D|phi_(2,n)>=0. The second output has B vertices 1 and 4
occupied. Two high-flux edges into still-vacant B2 remain; their linear
terms cancel, giving D|phi_(4,n)>=2n^2|phi_(4,n)>. Thus the normalized
conditional first output has exact diagonal-electric distribution

    Pr(D=0)=1/2,     Pr(D=2n^2)=1/2,                     (5)
    mean(D)=n^2,     Var(D)=n^4.

The probability-rate density of this resolved first mark at t=0 is
2kappa for every n. The all-mark initial loss is 48kappa independent of
the field, as in the checked cube target. Equation (5) is an event-marked
output statement; it does not assert that the post-event state stays in
either electric eigenspace under subsequent h evolution.

Summing all 24 resolved first marks gives an exact all-n balance:

    sum_j ||B_j Omega_n||^2 = 48,
    sum_j <B_j Omega_n,D B_j Omega_n> = 96n^2.           (5a)

The same two sums hold for the twelve coherent edge marks: their two charge
orientations have orthogonal output charge words, and D is diagonal, so
grouping those orientations introduces no cross term in either sum. This
does not equate later coherent and resolved quantum histories.

To see the quadratic coefficient without a fit, each marked output occupies
two distinct B sites: the birth endpoint and the old record's destination.
The four high-flux edges of (2) are the two face edges incident to B1 and
the two incident to B2. Across the 48 legal signed paths, each of B1 and
B2 is occupied 12 times as a birth endpoint and 12 times as an old-record
destination. Thus 96 of the 192 potential high-edge/path contributions
are excluded, leaving coefficient 96. The shifts happen only on the two
newly occupied B edges and therefore do not alter any active D term. The
linear-in-n sum vanishes: averaging the two birth charge signs removes the
center-A contribution; the two opposite oriented face contributions at
the other A centers cancel, and for center 0 or 3 the two face-B vacancy
multiplicities are equal. At n=0 every shifted link is excluded, so there
is no constant term. The direct all-mark control enumerates all 48 paths
and verifies (5a) at positive and negative integers.

For this initial pure state, D|Omega_n>=4n^2|Omega_n> makes the expectation
of its Hamiltonian commutator vanish at time zero. Consequently the full
first derivative of the *electric* expectation is exactly

    (d/dt)<K D> at t=0 = -96 kappa K n^2.               (5b)

Here the derivative is evaluated on this finite-support input, not a claim
that every trace-class state's unbounded energy expectation is
differentiable. The Hamiltonian part also leaves its own h expectation
constant. The H4 contribution to the dissipative total-energy derivative
is bounded independently of n because H4 and the jumps are bounded on
this fixed graph. Thus

    (d/dt)<h> at t=0 = -96 kappa K n^2+O(kappa delta),    (5c)

with a constant depending on the cube, not on n. This is system energy
bookkeeping inside the stipulated non-autonomous target, not heat delivered
to a named source.

## Hamiltonian-energy consequence and its limit

Let V_r=delta H4 on the r-record block, with v_r=||V_r||<infinity for
r=4,6. The input Hamiltonian mean is

    <h>_before=4K n^2+O(v_4).                           (6)

The conditional output has

    <h>_after=K n^2+O(v_6),
    Var(h)_after=K^2 n^4+O(K v_6 n^2+v_6^2).           (7)

The variance bound follows directly from
sigma(KD)=K n^2, sigma(V_6)<=v_6 and Cauchy-Schwarz for the covariance.
The mean transition is -3K n^2+O(v_4+v_6). An additive chemical offset
mu N changes it only by the fixed 2mu and leaves the variance (7)
unchanged. These are moments of the stipulated system Hamiltonian at the
specified marked event, not measured heat or an autonomous conservation
law. No bath Hamiltonian, drive work or energy-conserving dilation is
supplied by the model, so (6)-(7) assign none of those quantities.

This high-field family sharpens the energy-accounting question. A source
account that reproduces the stipulated state-independent mark across the
whole rotor Hilbert space must explain energy changes growing as n^2 and
an output energy variance growing as n^4. Finite-field preparation,
field-dependent formation amplitudes, an external drive, or a suitable
energy-carrying environment could change that account; this note does not
exclude any such completion. The result is on one finite cube and gives no
all-time heating law, continuum particle prediction, or TOE identification.
The order of limits is fixed: each finite n is a legitimate normalizable
rotor input obtained after the checked fixed-cube spin/epsilon limit, and
only then is the family n->infinity examined. There is no uniform-in-n
microscopic approximation or finite-S unlimited-flux assertion here.

## Exact control and standing

The root's standalone standard-library control enumerates the twelve
oriented cube edges, verifies Gauss after every hop and birth, and evaluates
D on the two actual first outputs for n=0,1,2,3,7,19,100. A separate
all-mark control tests (5a)-(5b) over 24 resolved marks and both positive
and negative n. Neither imports a repository builder. A cross-check uses
the earlier independently constructed formation-path implementation at
its pinned hash to match both resolved paths and all four coherent paths.
The all-n proof is the explicit face flux, two-path evaluation and path
count above, not extrapolation from those tested integers.
The H4 bound is analytic from the existing fixed-cube target, and the code
does not simulate an autonomous source. Exact source/results and run receipt
are recorded in this unit. An independent source-bound reconstruction and
review remain open before a review PR.
