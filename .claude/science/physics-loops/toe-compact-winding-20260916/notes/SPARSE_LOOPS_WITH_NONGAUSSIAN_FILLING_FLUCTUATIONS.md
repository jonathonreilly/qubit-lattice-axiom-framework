# Sparse conserved loops can have non-Gaussian filling fluctuations

Working personal counterexample proposal, 2026-09-16. The target implication
is precise: joint bad-vertex bounds, uniformly bounded conserved-current
components, stationary ergodicity and cubic symmetry do not, by themselves,
imply Gaussian diffuse-source limits for the local integer fillings.
The construction below is not the compact Hamiltonian Gibbs law. It does
not satisfy or refute that law's conditional bridge specification, and is
not an obstruction to a photon phase or to the framework axioms.

## 1. A stationary current law with isolated unit loops

Work on the dual cubic lattice Z^4. Fix0<p<1 and q=p^4. Partition its
vertices into side6 blocks

    B_r=6r+U+{0,1,2,3,4,5}^4, r in Z^4,

where U is uniform on{0,1,2,3,4,5}^4. The random origin is independent of
all variables below. There are six increasing coordinate planes
I={i,j}, i<j. For every pair(I,nu), nu=1,...,4, let

    {xi^(I,nu)_k:k in Z}

be an independent two-sided sequence of symmetric Rademacher signs.
All24 sequences are mutually independent. Define the plane-specific sign
field on block indices by

    sigma^I_r=product_(nu=1)^4 xi^(I,nu)_(r_nu).            (1)

At each block choose independently: an activation A_r with Bernoulli(q)
law; a plane M_r uniform among the six planes; and two independent
perpendicular offsets, each uniform on{2,3}. These marks are independent
across blocks and independent of the sign sequences.

The selected unit plaquette Q_r lies strictly inside its block. Its two
varying coordinates run from2 to3, and its two perpendicular coordinates
are the chosen offsets. Orient it in the increasing order of M_r. Put

    Q=sum_r A_r sigma^(M_r)_r Q_r,   j=boundary Q.          (2)

This is an integer2-chain and a conserved integer1-current, with
boundary j=0 and |j_e|<=1. Set B equal to the four vertices of every
active plaquette. Neighboring blocks' interior vertices are separated
by at least5 in some coordinate. Thus every bad-vertex component under
Chebyshev adjacency is exactly one four-vertex square. Every nonzero
current component is its four-edge loop. The components cannot join.

The coordinate bounding box of an active square, enlarged by1, stays
inside its block's closed coordinate box[1,4]^4. Adjacent blocks' enlarged
boxes are separated by at least3; even Chebyshev adjacency is excluded. Consequently even the enlarged filling regions
have a deterministic, volume-independent diameter bound. The canonical
coordinate-path filling of a unit planar loop gives the very plaquette
Q_r in(2); no remote surface is needed.

## 2. The joint small-probability bound

For any fixed finite set S of n vertices, condition on U, the plane and
offset marks, and all sign environments. If any requested vertex is not
in its block's selected square, the event S subset B is impossible.
Otherwise the event requires activation of at least ceil(n/4) distinct
blocks. Their activations remain independent under this conditioning.
Hence

    P(S subset B | conditioned variables)
         <=q^(ceil(n/4))<=p^n.

Averaging gives exactly

    P(S subset B)<=p^|S| for every finite S.               (3)

The parameter p can be arbitrarily small while all conclusions below
remain nontrivial. The sign correlations do not change(3), and the
components are bounded even without a subcritical counting argument.
This is stronger geometry than an exponential component tail.

## 3. Stationarity, ergodicity and lattice symmetries

First consider translations by6 lattice spacings, which act on block
indices. In particular translation by the block vector(1,1,1,1) shifts
all24 independent Rademacher sequences by one and shifts the iid block
marks along that vector. This transformation is mixing: for two cylinder
functions, sufficiently separated translates depend on disjoint sequence
coordinates and disjoint block marks, so their expectations factor.
Approximation by cylinder functions extends mixing to bounded measurable
functions. Therefore this single block translation is ergodic, and any
event invariant under the full Z^4 block action has probability0 or1.

The random origin makes the induced fine-lattice law stationary. Any
fine-translation invariant event is invariant under6Z^4, so it is
constant on each origin fiber; unit translations permute all1296 fibers
transitively. Its probability is0 or1. The current law, being a measurable
factor, is stationary and ergodic.

Coordinate permutations permute the six plane labels and the four
families within each plane. Reflections reverse block indices up to an
integer shift and send an interior perpendicular offset2 to3 or vice
versa. The block origin remains uniform. Reorienting the image plaquette
into increasing coordinate order introduces a fixed sign for each plane.
That sign can be absorbed by reversing one complete Rademacher sequence
in the corresponding plane family; its joint law is unchanged. Therefore
the current law is invariant under coordinate permutations and reflections,
with the ordinary oriented action on currents. This includes spatial
cubic rotations and time reversal. Ergodicity has not been replaced by a
mixture over a fixed preferred plane.

These properties concern this constructed current measure. They do not
make it a local Hamiltonian Gibbs measure or establish reflection positivity.

## 4. A local filling observable and its diffuse limit

Fix one oriented plane I. Sum the signed coefficient of Q over all
I-plaquettes in a block. This local observable is

    Y_r=A_r 1_(M_r=I) sigma^I_r=V_r sigma^I_r,
    V_r iid Bernoulli(rho), rho=q/6.                      (4)

The V_r are independent of the four sign sequences for this plane.
For a block cube{1,...,L}^4 define

    X_L=L^(-2) sum_r Y_r.                                 (5)

The test has counting l2 norm1 on block variables and l3 norm cubed
L^(-2), tending to0. The corresponding physical plaquette test, constant
on all I-faces of each included block, has a bounded l2 norm and the same
vanishing l3 scaling, up to a fixed block-size factor. The random origin
is part of the block formulation; section6 gives a deterministic physical
window formulation.

Write V_r=rho+(V_r-rho). Then

    X_L=rho product_(nu=1)^4 Z_(nu,L)+W_L,
    Z_(nu,L)=L^(-1/2) sum_(k=1)^L xi^(I,nu)_k,
    W_L=L^(-2) sum_r (V_r-rho) sigma^I_r.                  (6)

The four Z_(nu,L) converge jointly to independent standard Gaussians
Z_1,...,Z_4. Conditional on the sign environments, the summands of W_L
are independent and centered, their total variance isrho(1-rho), and
the maximum summand magnitude is at mostL^(-2). Expanding their
conditional characteristic functions shows, uniformly in all signs,

    E[exp(i t W_L) | signs]
              ->exp[-t^2 rho(1-rho)/2].                  (7)

The error in the logarithm is O_(rho,t)(L^(-2)). Uniform convergence
makes this limit independent of the sign environments. Thus

    X_L converges in law to
    X=rho Z_1 Z_2 Z_3 Z_4+sqrt(rho(1-rho)) Z_0,            (8)

where Z_0,...,Z_4 are independent standard Gaussians. The limit has
variance rho but is not Gaussian. In particular,

    fourth cumulant(X)=rho^4(3^4-3)=78rho^4>0.             (9)

For distinct blocks r,s, E[sigma^I_r sigma^I_s]=0: at least one
coordinate uses distinct independent centered signs. Therefore the
finite covariance is already diagonal,

    E Y_r=0, Cov(Y_r,Y_s)=rho 1_(r=s), Var(X_L)=rho.        (10)

This example does not fail merely because the variance grows with volume.
It has bounded covariance, ergodicity, arbitrarily rare isolated loops,
and a genuinely non-Gaussian diffuse limit.

## 5. Exact finite fourth moment and failure of a cubic MGF estimate

There is an exact finite-volume check of(9), independent of a numerical
central-limit fit. Let N=L^4. For the product sign field,

    E (sum_r sigma^I_r)^4=(3L^2-2L)^4.

In the expansion over four ordered block indices, the all-equal terms
numberN, the two-pair terms number3N(N-1), and terms with exactly three
distinct indices have zero expectation. In the remaining four-distinct
terms, each activation contributes an independent factor rho. Hence

    E X_L^4 =rho/N+3rho^2(1-1/N)
          +rho^4[(3-2/L)^4-3+2/N],
    cumulant4(X_L)=(rho-3rho^2)/N
          +rho^4[(3-2/L)^4-3+2/N].                       (11)

This tends to(9). The fourth moment of each normalized Rademacher sum
is explicit; higher even moments are uniformly bounded. Conditional
bounded-summand estimates likewise bound moments of W_L. Thus moment
convergence is consistent with the distributional limit rather than an
unsupported interchange.

More sharply, no uniform cubic log-MGF remainder controlled only by the
vanishing l3 cube can hold for this source. On the event that all4L signs
of the chosen plane in the window equal+1, which has probability2^(-4L),
the conditional filling variables are iid Bernoulli(rho). For every t>0,

    log E exp(t X_L)
      >=-4L log2+L^4 log[1-rho+rho exp(t/L^2)]
      >=-4L log2+rho t L^2 ->infinity.                    (12)

The second inequality is Jensen for a Bernoulli variable. In contrast,
Var(X_L)=rho and ||h_L||_3^3=L^(-2). A bound of the form

    |log E exp(t X_L)-t^2 Var(X_L)/2|
                       <=C |t|^3 ||h_L||_3^3

with fixed C would force a finite Gaussian limit of the log-MGF. Equation
(12) rules it out. The limiting product-Gaussian variable itself has no
finite real MGF at nonzero argument; weak convergence is not MGF convergence.
No simulation is needed for this conclusion.

## 6. Deterministic physical windows and scope

One may use a fixed fine-lattice cube of side6L rather than a window
aligned to the random origin. For any origin there is an aligned cube
of L^4 blocks differing from the physical window by O(L^3) boundary
blocks. Different blocks' signed filling observables are uncorrelated,
including after selecting a subset of their plaquette locations, because
the product signs remain centered and pairwise orthogonal. The normalized
boundary discrepancy therefore has variance O(L^(-1)) and vanishes inL2.
Translation invariance of the underlying sequences gives the same limit
(8). This yields deterministic diffuse plaquette tests; a random test
chosen after observing the field is not needed.

The effect also survives smooth tests. Take a nonzero product of compactly
supported smooth functions f_nu and weight block r by
 L^(-2) product_nu f_nu(r_nu/L). The coherent term in(6) still factors
into four independent weighted Rademacher sums. Their limiting variances
are v_nu=integral f_nu^2>0. The conditional noise variance tends to
rho(1-rho) product_nu v_nu. The limit is the variable in(8) multiplied
by sqrt(product_nu v_nu), with fourth cumulant
 78rho^4(product_nu v_nu)^2>0. Evaluating the smooth test at the actual
fine-lattice plaquette positions instead of block reference points
changes each coefficient by O(L^(-3)); pairwise orthogonality makes the
total error variance O(L^(-2)). Thus neither a discontinuous box test nor
a source adapted to the random block origin is essential.

The observable in(4) is a component of a specified local integer filling,
not the conserved current paired with a constant edge test. For the
latter, conservation would cause cancellations. Integer fillings enter
the proposed compact-to-real curl comparison, so their source behavior
is precisely a relevant missing control. This note does not identify
Y_r with the physical magnetic field of the supplied Hamiltonian.

The counterexample satisfies every premise listed in its target
implication. No representation as the actual Hamiltonian local Gibbs law
is supplied or needed, and its additional weight structure was never among
those premises. It shows why a normalized source argument must use
more than sparse geometry, even when ergodicity and cubic symmetry are
available. The actual Hamiltonian has additional local conditional
structure; testing that structure is the next positive route. No phase
or axiom no-go follows.

For the scope of negative statements, see the [N1-N8 review](../NO_GO_DISCIPLINE_CHECKLIST.md).
