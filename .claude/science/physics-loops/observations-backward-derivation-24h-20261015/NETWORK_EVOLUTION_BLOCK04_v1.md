# Record formation: observed anticorrelation and a deterministic reservoir

Personal author: /root, 2026-10-16. Conditional exploratory mathematics.
This follows the actual event-process failure in block02, rather than repairing
its average fringe by assuming independent Born draws. The constructive route
below is a standard generalized baker map, not a new law or a novelty claim.

## Observational development input

Kwiat and Chiao, Phys. Rev. Lett. 66, 588-591 (1991), DOI
10.1103/PhysRevLett.66.588, was read in full, including figures and the counting
calibration. Its polarization-cycle interference experiment also measured
anticorrelation after a second beam splitter. The reported ratio is
alpha=N123*N1/(N12*N13). The paper gives mean alpha=0.08 +/- 0.04 and calibrated
triple-count efficiency eta=0.70 +/- 0.07, with the adjusted classical bound
alpha>=eta. Narrow herald filtering gave coincidence-fringe visibility
60% +/- 5%; the singles visibility was below 2%. These are published summaries,
now exposed development input, not a raw-data reanalysis, independent holdout,
fit, new significance calculation or validation of a candidate here.

The DOI and author-hosted PDF identify the input. The exact downloaded PDF SHA256
is ade2c3d55e0023e0847ab9f915e3021b63593feff54f1ac9b631a1ac18bba93c.
The PDF is stored privately, not copied into this repository. Local retrieval
initially failed because of Python trust roots, then HTTP403; system curl
retrieved the public PDF with normal certificate verification. Neither failure
had scientific meaning. The paper's quantum interpretation is not a premise of
the algebra below. Its quoted standard deviations are not combined here without
the underlying counting and calibration covariance.

## What a common-intensity detector class actually excludes

Condition on a specified herald-selection protocol. Let J>=0 be the common
incident classical intensity, with any conditional distribution. Suppose the
two detector clicks A,B are conditionally independent given J and have response
probabilities f(J),g(J), each nondecreasing, with positive mean responses. The
functions include fixed splitting fractions and fixed efficiencies. There are
no additional anticorrelated detector states or herald-conditioned detection
noise in this class. For an independent copy J',

    2 Cov(f(J),g(J))
      = E[(f(J)-f(J'))(g(J)-g(J'))] >= 0.

Therefore P(A=1,B=1)>=P(A=1)P(B=1), and the ideal per-herald ratio is >=1.
If only registered triples are independently retained with probability eta,
while both registered singles-in-herald denominators remain as defined, the
observed ratio is >=eta. That last scalar efficiency model is an additional
calibration assumption, not a theorem about arbitrary electronics or herald
selection. Saturating Poisson photodetection f=1-exp(-aJ),g=1-exp(-bJ) belongs
to the stated monotone class. Arbitrary hidden detector state distributions need
not. The proof is a standard covariance inequality, not a no-go theorem for
all deterministic or neighborhood-driven models.

The complementary counters of block02 have zero simultaneous clicks and can
therefore evade this detector class. They do so using a shared complementary
initial condition and a prescribed nonlinear update, not by reproducing the
classical common-intensity/independent-detector premises. Their half-flux
alternation remains a separate failure against an iid record benchmark. One
observed ratio alone cannot certify the full record process.

## An explicit deterministic candidate for record fluctuations

Let p in (0,1) be a supplied target output fraction, potentially obtained from
the conditional flux calculation in block02. Introduce a real internal state
u in [0,1). Define

    if u<p:  Z=0, u_next=u/p;
    else:    Z=1, u_next=(u-p)/(1-p).

Each branch maps its subinterval bijectively onto [0,1). If u is initially
Lebesgue-uniform, then Z=0 has probability p, and the conditional distribution
of u_next given either outcome is again uniform. Induction gives independent
Bernoulli records for fixed p. For any prescribed sequence p_t, the probability
of a cylinder z_1,...,z_n is the product of p_t for zero and (1-p_t) for one.
The same induction works for p_t determined by already observed past records:
the conditional next-record law is then the specified p_t, rather than iid.

This is a deterministic evolution with no stochastic reset at each trial.
It is nonetheless deliberately constructed to implement the requested
probabilities. Branch widths p and 1-p, the full-branch rescaling law, the
initial uniform measure, exact real precision, input cadence and the detector
interpretation are supplied. Calling this map a derivation of the Born process
would hide those assumptions. Quadratic incoming flux by itself does not derive
the basin widths, the expanding map or the ensemble over u.

A pair of local detector rules can maintain exactly one click without a
per-trial message between them. Give detector 0 state u0 in [0,1), detector 1
state u1=1-u0 in (0,1], and complementary incoming fractions p and q=1-p.
Detector 0 clicks when u0<p and applies the expanding map above. Detector 1
clicks when u1<=q; when it clicks it sets u1_next=u1/q, otherwise it sets
u1_next=(u1-q)/(1-q). Direct substitution gives u1_next=1-u0_next, including
the threshold equality. Exactly one clicks on every trial. Uniform u0 gives
the full Bernoulli process, whereas a particular exceptional u0 need not.
This explicitly uses a shared preparation, complementary flux normalization,
opposite endpoint conventions and a common trial cadence. Its response inputs
must reach both detectors in the current trial; it is outside block01's
one-current-input information restriction. It is not an autonomous realization
from the framework's current minimal axioms.

## A conditional relaxation of the initial density

For fixed p, the Perron operator on initial probability densities is

    (L rho)(u)=p*rho(pu)+(1-p)*rho(p+(1-p)u).

It preserves nonnegativity, normalization and the uniform density. For a
Lipschitz density with Lipschitz constant K,

    Lip(L rho) <= c_p K,   c_p=p^2+(1-p)^2 < 1.

Since a unit-integral continuous density lies within its Lipschitz constant of
1, ||L^n rho-1||_infinity <= c_p^n K. Hence its total-variation distance from
uniform is at most c_p^n K/2. The distribution of any fixed finite future
record block, produced by the same deterministic protocol from that state,
differs from its uniform-seed distribution by no more than this TV bound.
This is a distributional burn-in bound, not a guarantee for every realized u.
It does not condition on a selected rare output history from the burn-in.

Uniform is the unique invariant probability density in L1: L is an L1
contraction, Lipschitz functions are dense in L1, and the above contraction
proves L^n f converges to the constant integral of f for Lipschitz f. Approximating
an invariant L1 density by such functions forces it to equal 1 in L1. This does
not assert uniqueness among all invariant measures; point and periodic-orbit
measures also exist. Absolute continuity is a substantive restriction on the
initial-state class, not an empirical conclusion about the realized state.

For example rho_0(u)=2u gives the exact density

    rho_n(u)=1+c_p^n(2u-1),
    TV(rho_n,1)=c_p^n/4,
    P_n(Z=0)=p-p(1-p)c_p^n.

This is a concrete transient prediction of this chosen ensemble and map. It
can be compared to a preparation protocol only after that protocol supplies a
meaning for rho_0. There is no claim that a physical detector is prepared so.

## Keeping earlier information instead of deleting it

The expanding u map loses the branch label unless it is recorded elsewhere.
Introduce v in [0,1), and replace the update by the generalized baker map:

    Z=0: (u,v) -> (u/p, p*v),
    Z=1: (u,v) -> ((u-p)/(1-p), p+(1-p)*v).

The two vertical strips map to disjoint horizontal strips, their union is the
unit square, and each branch has Jacobian determinant one. The inverse reads
the last branch from whether v_next<p, then reconstructs the previous u,v.
This is an invertible information-preserving embedding of the same output
process. An operational v update is not a rewrite of a formed fundamental
record; an append-only branch list is the separate record history. The finite
2D schematic does not establish a covariant qubit-lattice implementation or
the physical readability of infinitely fine initial-state digits.

At p=1/2, the map shifts the binary expansion of u into the record stream.
Uniform u contains the entire future iid bit stream in its initial digits.
By contrast u=0 produces only zero and u=1/7 produces a period-three stream.
No amount of deterministic mixing turns those particular states into iid
outcomes. Ensemble attraction cannot be promoted to selection of an actual
initial state or a derivation of typicality.

## Exact information budget of deterministic record generation

Let S0 be a hidden initial state, X the externally specified controls, and E
all subsequently entering unobserved inputs. If the record string Y_1:n is a
deterministic function of (S0,E,X), discrete Shannon entropy satisfies

    H(Y_1:n | X) <= H(S0,E | X).

With no fresh E and at most M initial states, H(Y_1:n|X)<=log2 M. An exact
nondegenerate iid Bernoulli(p) target has n*h2(p) bits of entropy. More strongly,
all 2^n strings have positive probability, so a deterministic M-seed model
needs M>=2^n to reproduce that entire n-trial distribution exactly. Merely
appending fresh blank record cells cannot increase the seed distribution's
support. A growing physical neighborhood can bring in new unknown inputs;
it must be included in E rather than counted as randomness derived for free.

The finite-horizon limitation is sharp for a simple example. Prepare m binary
cells with the uniform distribution on all 2^m strings. Read one cell per step
and cyclically shift the register. The first m records are exactly iid fair
bits in the ensemble; every trajectory then repeats with period dividing m.
For n>=m the n-record distribution has 2^m equally likely strings, giving
TV distance 1-2^(m-n) from n iid fair bits. Thus a finite observed iid segment
alone cannot rule out deterministic evolution with a sufficiently large hidden
initial register. Local swap gates can implement a finite shift schedule, but
that schedule, preparation and registration law are additional physical choices.

This is standard deterministic data processing and support counting. It does
not establish intrinsic indeterminism from finite observations, exclude an
infinite initial reservoir, or require iid behavior of actual apparatus data.
The generalized baker map supplies an unbounded-resolution reservoir and a
measure on it. A finite-precision realization has a finite resource and needs
its own transient, recurrence and approximation-error analysis.

## What this route does and does not retire

The per-trial random reset used as an obvious repair in block02 is unnecessary
within this constructed deterministic model: one prepared reservoir plus an
explicit invertible evolution gives the same full finite record distributions.
It replaces that reset with a stronger continuous-state preparation and a
particular expanding law. Uniformity can be weakened to an absolutely
continuous initial ensemble plus sufficient burn-in, with explicit bounds;
selection of the physical state/ensemble remains open. No framework assumption
has been retired as physically derived. The model is a useful witness to where
randomness can be stored, and to which initial-state/neighbor-input resource
must be measured or explained next.

probe_record_reservoir_v1.py checks the algebra, interval cylinders, invertible
map, density transient, finite seed limitation and detector covariance examples.
All are synthetic development checks. The published observational summaries
above motivate the targets; they are not a fit or independent test of this map.

For prior-art identification, the area-preserving map is the constant-cut case
of the generalized baker construction in Bose and Murray,
https://arxiv.org/abs/1206.2406 . The introduction and defining equations (1)-(4)
were read; its polynomial mixing theorems for other cut functions are not used.
The elementary constant-cut density proof above is supplied here in full.
