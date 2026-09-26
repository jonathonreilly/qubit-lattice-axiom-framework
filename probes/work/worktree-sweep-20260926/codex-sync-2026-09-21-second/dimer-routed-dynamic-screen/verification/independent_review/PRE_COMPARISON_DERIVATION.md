# Independent reconstruction before implementation access

This check concerns the declared finite full-matching color process. I read
the corrected transport note and the dynamic protocol completely. The earlier
asymptotic proof review is reused at its bound identity; no new proof of that
limit is claimed here. No dynamic author code, production output, aggregate
or analyzer was opened before this reconstruction and its controls were sealed.

## Generator and exact ideal uniformization

Let K=N^3/2, with the pair positions indexed by black sites. Each routing
q_delta maps u to the pair whose white endpoint is u+delta. For each u,
exactly one of the six deltas gives a fixed point (its matched direction).
Thus the channel list has exactly M=5K entries, retaining different original
edges which induce the same unordered pair swap. A nonfixed channel uses
four distinct positions q_delta^{-1}u,u,q_delta u,q_delta^2u for N>=8.

Write T_delta=2S_delta at gamma=1. It has integer entries in {-1,0,1}.
The integer context drive h2=T(l,a)+T(a,r)-T(l,b)-T(b,r)=2h lies in [-4,4].
At k0=11/10 the ACTUAL rate, including the outer half, is

    c = k0/2+h/4 = (22+5 h2)/40 in [1/20,21/20].

The reverse swap has rate (22-5h2)/40, so the symmetric part is 11/20.
The positive floor is 1/20, not the symmetric part. Conditional on the
current state, an attempt chooses one of M channels uniformly, then accepts
with probability c/(21/20)=(22+5h2)/42. If P is this discrete attempt kernel,

    Lambda = M(21/20),   L = Lambda(P-I).

For a microscopic interval s, exp(sL) equals the Poisson mixture
exp(-Lambda s) sum_n (Lambda s)^n P^n/n!. Rejections, and any swaps which
leave the COLOR projection unchanged, remain part of P. Independent Poisson
counts for disjoint observation intervals produce the exact ideal CTMC
observation law; event times need not be stored. The macroscopic interval
7/16 must use s=N(7/16). The expected attempt counts per interval are
75,264; 1,204,224; 19,267,584; and 308,281,344 for N=16,32,64,128.

This mathematical exactness presumes ideal independent uniform and Poisson
variates. Source scrutiny can check normalization and the selected generator;
it is not a proof of all properties of a deterministic PRNG or its floating
Poisson implementation.

## Conserved record representation

Give each initial pair a unique key k and a fixed color lookup a(k), initially
iid uniform among the fourteen labels. The state is a permutation key[u]
of 0,...,K-1. An accepted event swaps key[u],key[v]. It transports both
records attached to each key: the record initially on the black sublattice
goes between black pair endpoints, and its antipodal partner between the
corresponding white endpoints. The geometric matching is unchanged. Both
physical record displacements have nearest-neighbor path length two.

Colors must be evaluated as a(key[u]); mutating their lookup would violate
permanence. A swap of different keys of the same color still changes the
record state and counts as an accepted physical event. Key permutation,
fixed lookup, all color counts and geometric matching are exact conserved
quantities. This faithfully represents the autonomous finite-color projection
with abstract conserved identities. It does not itself instantiate continuous
projector contents, prove color-code realizability by physical measurement,
or certify the full trajectory from its two endpoints.

## Fourier convention and all six components

For phi(u)=exp(-i Q.u/N), define pair fields K^{-1/2}sum_u phi(u)e(a_u)
and the corresponding b field. At the three positive fundamental modes,
the sum of phi over the black sublattice is zero; the uniform mean e,b is
also zero. No nonzero mean subtraction is required for these vector fields.
The Fourier transform of curl is +i Q cross, with this negative-exponent
convention. Uniform colors give rho_A=3/7,rho_B=4/7 and covariance
Cov(X)=I/7, Cov(Y)=4I/7, Cov(X,Y)=0. Hence E=sqrt(7)X and B=sqrt(7)Y/2
have identity six-component equal-time covariance at initial time.

The current derivative, with its before-outer-half normalization, gives

    dE/dt = +(2i/7) Q cross B,
    dB/dt = -(2i/7) Q cross E.

Put c=2/7, q=Q/|Q|, C_q z=q cross z, P_L=q q^T, P_T=I-P_L,
theta=c|Q|t and D=P_L+cos(theta)P_T. The target matrix is

             [ D                  +i sin(theta) C_q ]
    U(t)  =  [ -i sin(theta) C_q   D                ].

It is unitary, leaves both longitudinal components static, and gives phases
0,pi/4,pi/2,3pi/4,pi at the declared times. A cosine on all six components,
a missing outer rate half, omission of N acceleration, or conjugating only
one side of the convention would change these targets.

Writing R_AB(t)=E[A(t) B(0)^dagger], the target cross blocks are
R_EB=+i sin(theta) C_q and R_BE=-i sin(theta) C_q. The signed cross scalar is

    Re tr[-i C_q^T R_EB + i C_q^T R_BE]/4 = sin(theta).

The transverse autocovariance is
Re tr[P_T R_EE+P_T R_BB]/4=cos(theta); the longitudinal one is
Re tr[P_L R_EE+P_L R_BB]/2=1. The prediction-error observable is
||[E(t),B(t)]-U(t)[E(0),B(0)]||^2/6. These formulas specify the complex
conjugation and denominators independently of any forthcoming analyzer.
At finite N the continuum predictor need not be exact or monotone in N.
All modes and observation times from a single history share one sampling
unit. No dynamical conclusion about the static geometric Gauss field follows.

## Independent finite controls and prospective endpoint scope

`independent_precheck.py` exhausts all 14^4 contexts for each positive axis,
finds the sharp h2 extrema, checks reverse-rate sums, and computes the exact
product-current derivative of the ACTUAL rate: A_i/2=T_i/28. This is checked
against the six-field Fourier matrix for three axis vectors and (1,2,3),
including exact identity initial covariance and the signed cross contraction.

A separately assembled four-position routing-cycle chain on 24 permutations
of four distinct keys (two have the same color) is nonreversible with uniform
invariant law. Its rational uniformization matrix is stochastic. An 80-term
Poisson sum agrees with a separate matrix exponential to 3.89e-16, and two
independent time intervals compose to 5.00e-16. This verifies a finite exact
generator identity plus its numerical evaluation, not a Monte Carlo trajectory.

Independently constructed N=8 winding and irregular matchings have 1,280
channels each. The irregular matching has 1,104 distinct unordered pair
edges and multiplicity up to two, so deduplication would change the process.
The two fixtures have minimum nontrivial routing cycles four and five; all
checked footprints are distinct and record displacements have length two.
The irregular fixture accepted 532 of its independently seeded plaquette
proposals; this does not test the author's as-yet-unread fixture generator.

Before any production access, `ENDPOINT_SELECTION.json` selects literal
replicate identifiers 3 and 27 in each of eight size/geometry cells: 16
endpoints total. After source inspection establishes file encodings and seed
bindings, only these selected records will be decoded, and their initial and
final Fourier fields recomputed directly. Aggregate outcomes remain unopened.
Endpoint conservation is a necessary check, not a complete event or RNG replay.

The independent control completed on its first attempt with empty stderr.
There are no provisional mathematical findings from this reconstruction.
