# Independent charge reconstruction derivation

This is a focused check of the parent's supplied chiral EFT. It is not a
new primary construction, a formal audit, or an assertion of a microscopic
origin. The pinned source and independently executed checker are recorded
in the adjacent receipt. The author runner was neither imported nor run.

## Local algebra and representation signs

Gauge invariance of the four specified mass couplings gives the linear
system q+h+u=0, q-h+d=0, l-h+e=0, l+h+n=0. Solving for the singlet
charges gives u=-q-h, d=h-q, e=h-l, n=-h-l. These relations assert allowed
couplings; they do not determine nonzero coefficients or masses.

Sum the Weyl charges with dimensions (2Nc,Nc,Nc,2,1,1). With the neutrino,
the first moment vanishes. The third moment reduces to

    Tr Y^3 = -6 h^2 (Nc q+l).

Removing n subtracts n and n^3, leaving l+h and
(l+h)^3-6h^2(Nc q+l). The mixed color condition is identically zero after
the mass constraints. The weak condition is Nc q+l=0. With no neutrino,
the weak and linear conditions fix l=-h and q=h/Nc; the real cubic
condition yields the same result. With a Dirac neutrino they leave the
stated one-parameter family. At Nc=3 this is the familiar B-L direction.

For a Hermitian fundamental generator T, the left-handed conjugate
representation is -T^T, not T. Its commutator is

    [-T^T,-S^T] = -[T,S]^T.

Its quadratic trace has the same sign as the fundamental, whereas its
symmetrized cubic trace has the opposite sign. This distinction explains
both the color mixed-anomaly coefficient and the pure color cancellation.

The independent calculation builds color and weak generators from matrix
units, then computes each species' trace as a product of a color trace and
a weak trace. It never forms the author's 16 by 16 matrices. Summing the
two ordered traces for each unordered generator triple reproduces all 364
zero rows exactly. All 64 color quadratic traces have normalization
Tr(Ta Tb)=delta_ab/2. All 64 conjugate commutators pass independently.
Replacing u^c by a color fundamental gives the nonzero T8 control
-sqrt(3)/3. Omitting n leaves h-3q in the gravitational trace and
-(3q-h)^3 in the cubic charge trace.

The invariant explanation extends beyond a finite sample: for color A,
weak B, and an abelian parameter z, expand the cubic trace on each tensor
factor. The surviving candidates are the pure color cubic term, the weak
cubic term, 3z Tr(A^2)(2q+u+d), 3z Tr(B^2)(Nc q+l), and z^3 Tr(Y^3).
The first cancels between the two fundamentals and two conjugates; the
weak cubic trace vanishes; the remaining displayed coefficients vanish.
Single nonabelian traces eliminate the other mixed terms.

There are Nc+1 ordinary SU(2) doublets per generation. At Nc=3 the
ordinary Witten parity is even for every integer generation count. This
does not select three generations or classify all global anomalies.

## Mixing and mass-operator boundary

The electric charge of bar(e) nu W^- is -Qe+Qnu-QW. Thus a nonzero
charged-current matrix entry implies Qnu=Qe+QW. Equality propagates along
every path of its bipartite support graph. A connected component has one
free charge, so the constraint rank is 6-c including isolated vertices.
An independent union-find calculation and GF(2) incidence elimination
reproduce every one of the 512 rows, with 205 connected supports. Incidence
rank is n-c over either the real field or GF(2); this is not a test of
whether a support is realizable by a unitary matrix.

The three-family no-neutrino assignment l=(-h+t,-h-t,-h), q=h/3 cancels
the total weak, linear, and cubic anomalies. It supplies an explicit
counterexample to extending the one-family uniqueness claim without a
mixing or other flavor premise. It does not model observed oscillations.

For a common charge r, a nonzero Majorana matrix satisfies
Q^T M+M Q=2r M=0, hence r=0. With Q=diag(r,-r), an off-diagonal matrix
can instead satisfy this equation and describes a charged Dirac pairing.
This checks the note's mass-matrix caveat. The displayed singlet
operators have charges 2n=4h epsilon and 2(l+h)=-4h epsilon, so either
nonzero coefficient forces epsilon=0 under the stated common-charge and
unbroken-photon premises.

The original scalar-vev sentence had a real counterexample: H has Y=h
nonzero but its lower component has T3=-1/2 and Q0=0. Nonzero hypercharge
by itself cannot be the obstruction. For the specified singlet
compensator, T3=0 and Q0=Y/(2h), so a nonzero compensating charge forbids
a photon-preserving vev. The corrected note now says this explicitly.

## Fixed and variable global charge lattices

For h=1/2, the weights in a specified character lattice z=6Y are

    (1+2epsilon, -4-2epsilon, 2-2epsilon,
     -3-6epsilon, 6+6epsilon, 6epsilon, 3).

The Q weight requires 2epsilon integer; this is sufficient for all seven
weights. The stated central generator has phase in turns

    t/3 + w/2 + z/6.

Requiring it to be an integer yields the Z6 rule, and applying its third
or second power yields Z2 or Z3. These direct character phases reproduce
all 37 reported rows. Their epsilon sets are respectively (1/2)Z, Z,
(3/2)Z, and 3Z for product, Z2, Z3, and Z6.

Here primitive means the specified U(1) character lattice. It does not
require the occupied matter weights to generate that lattice faithfully.
At epsilon=1 the displayed weights have gcd 3, yet they are valid
representations of the fixed U(1). If matter faithfulness were imposed as
another premise, some allowed rows would be removed. It was not imposed
here, and is not needed for the claimed gap or the small-charge examples.

On epsilon>-1, delta=epsilon/(1+epsilon) has positive derivative
1/(1+epsilon)^2. The product lattice's nearest positive epsilon is 1/2,
giving delta=1/3. Its only negative nonzero epsilon in this branch is
-1/2, giving delta=-1. Thus the smallest nonzero absolute charge is 1/3.
For Z6 the first positive epsilon is 3, giving 3/4, and no negative lattice
point lies in the branch. Values epsilon=-1 or below in the global-row
table are algebraic representation checks, not uses of the measured-charge
normalization on its excluded branch.

For D=10^k, D is even and D=1 mod 3. Setting epsilon=1/D makes every
hypercharge an integer multiple of 1/D; the n weight is 1 and H has
weight D/2. The gcd is therefore 1. All four listed examples satisfy
these exact conditions. Their measured neutron charge 1/(D+1) approaches
zero without reaching it. The primitive embedding changes, which is why
this does not contradict the fixed-lattice gaps.

## Physical units and empirical response

Conjugating the right-handed singlets to physical particles gives the
electric charges before selecting a unit. On epsilon>-1 the electron
magnitude is e_ref=e0(1+epsilon). Dividing by it, rather than setting it
equal to e0, gives

    (up, down, electron, neutrino, proton, neutron, W+)
    = ((2-delta)/3, (-1+2delta)/3, -1, -delta, 1, delta, 1-delta).

The inverse parameter map is epsilon=delta/(1-delta). Beta charge
conservation then reads delta=1-1-(-delta). A body with Z protons and Z
electrons has net charge N delta. In particular hydrogen neutrality
leaves delta unconstrained in this family.

Independently counting nominal S32 plus six F19 atoms gives Z=70,
N=76, A=146. The generic molecular response is Zx+Ny; the published
per-nucleon parameter therefore becomes s=(70x+76y)/146 at the stated
nominal-mass approximation. Neutral antineutrinos would imply x=y through
beta decay. The anomaly family instead imposes x=0 and y=delta, giving
c=38/73. Keeping the old x=y interpretation would change the candidate's
response incorrectly.

Using exact rational decimal summaries, the neutron calibration is
y=-2/5 with variance 121/100 in units of 10^-21. The molecular summary is
s=-1/10 with the same variance. The independent prediction and variance
are c*y and c^2*vy. The residual variance is vs+c^2*vy, conditional on
independent Gaussian summary errors. This gives the reported prediction
-0.20821917808219179 and standardized residual 0.087265758595022.

The optional weighted fit is derived directly by completing the square:

    delta_joint=(y*vs+c*s*vy)/(vs+c^2*vy),
    Var(delta_joint)=vy*vs/(vs+c^2*vy).

Its minimized chi-square equals (s-c*y)^2/(vs+c^2*vy). Both summaries
are calibration inputs for this separate fit. It does not alter the
neutron-only transfer prediction or create a blind holdout.

Without x=0, solve y=y_neutron and x=(A*s-N*y)/Z. The neutrino quantity
is x-y=A*(s-y)/Z under beta charge conservation. Differentiate this full
linear map with respect to the two original summaries; summing the two
variance-weighted derivative outer products yields the reported complete
rank-two covariance, including its negative x-y covariance. The neutrino
quantity is inferred, not a third independent measurement.

The polarity half-sum is exactly -1/10 and its independent variance is
(1.4^2+1.6^2)/4=113/100. Its standard deviation is about 1.063. The
half-difference is 46/5 and is the odd nuisance component. An unconstrained
even offset remains degenerate with a genuine signal. These calculations
cannot validate unprovided raw events, the full systematic covariance,
or the acoustic calibration model.
