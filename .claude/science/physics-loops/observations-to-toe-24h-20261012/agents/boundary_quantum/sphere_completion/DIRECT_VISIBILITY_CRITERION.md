# Full-sphere quantum visibility from an absolute harmonic sum

Direct parent derivation, 2026-10-12. This answers a different question from
the existing perfect-anticorrelation classification. It permits a declared
common visibility V and asks for one bipartite state and measurement family
for all directions. No visibility is fitted to the exposed public experiment.
No empirical exclusion or novelty claim is made.

## Exact mathematical statement

Let f be a real continuous isotropic pair kernel on S2 with Legendre
coefficients a_l=(2l+1)/2 integral_-1^1 f(c)P_l(c)dc. Let0<V<=1. Require
measurable projective binary local observables in separable tensor Hilbert
spaces and one normal state, with fair marginals and correlation

    C(a,b)=-V f(a dot b).

Such a realization exists if and only if

    V sum_(l>=0) |a_l| <= 1.

The sum may be infinite, in which case no V>0 qualifies. V0 is trivial.
The state and local dimension may be countably infinite. The result does not
promise finite energy, finite entanglement, economical dimension, or a
microscopic source mechanism. Those are additional physical obligations.

## Necessity: a trace-norm bound

Purify the state if necessary and put
u(a)=(A(a) tensor I)|psi>, v(b)=(I tensor B(b))|psi>. Regard the complex
space as a real Hilbert space with inner product Re<.,.>. Both vector norms
are one and their inner product is C(a,b). The same bound holds for binary
POVM contractions, whose norms are at most one.

Use normalized area measure mu on S2. The integral maps

    U h = integral u(a)h(a)dmu(a),
    W h = integral v(b)h(b)dmu(b)

from real L2(mu) into this Hilbert space are Hilbert-Schmidt, with squared
norms integral||u||^2 and integral||v||^2, each at most one. Measurability,
separability and bounded norms justify the integrals; expanding in orthonormal
bases and applying Tonelli proves these Hilbert-Schmidt identities. The
correlation integral operator is T=U* W, so

    ||T||_1 <= ||U||_2 ||W||_2 <= 1.

The normalized spherical-harmonic addition theorem gives eigenvalue
-V a_l/(2l+1) with multiplicity2l+1. Thus ||T||_1=V sum|a_l|. In particular,
trace-class summability is forced by a quantum realization, rather than
assumed in order to prove necessity. Fair marginals were not needed here.

## Sufficiency: signed harmonic sectors

Suppose S=V sum|a_l|<=1. Absolute summability makes the Legendre series
uniformly convergent, and it equals f by uniqueness/completeness in L2 and
continuity. For each nonzero coefficient choose the real unit harmonic
feature w_l(a) with dot product P_l(a dot b).

For l>=1 use2l+1 traceless Hermitian Clifford matrices in dimension2^l.
With a maximally entangled state and observables

    A_l(a)=w_l(a) dot Gamma_l,
    B_l(b)=-sign(a_l)[w_l(b) dot Gamma_l]^T,

the correlation is -sign(a_l)P_l and both marginals vanish. For l0 use
Pauli Z in a two-dimensional maximally entangled sector, with the same sign
rule; this avoids the nonexistent traceless one-dimensional involution.

Give sector l probability V|a_l|. Give the remaining probability1-S to a
separate product state |+x> tensor |+x>, measured with Pauli Z on both sides;
it supplies zero correlation and fair marginals. On countable local direct
sums, a pure superposition of these matching sector states is normalized.
Block-diagonal observables eliminate cross-sector terms. Their correlation
is the required series for all a,b at once. No setting-dependent state or
measurement retuning is introduced.

## Relation to the fixed conditioned family

For f_k(1)=1, absolute summability gives sum a_l=1. Therefore

    sum|a_l| = 1 + 2 sum_(a_l<0)|a_l|,
    V_critical = 1/[1+2 sum_(a_l<0)|a_l|].

At V1 this reduces to nonnegative Legendre coefficients, consistent with
the prior exact-anticorrelation result. At lower V a negative coefficient
alone no longer rules out the whole quantum realization. A finite scan does
not determine the exact critical visibility; an unsampled absolute tail must
be bounded or otherwise proved. The pending sphere-classification proof is
not silently promoted by this theorem.

The resource obstruction in DIRECT_RESOURCE_OBSTRUCTION.md applies directly
to the positive-coefficient unit-visibility construction. A signed/noisy
construction needs its own resource check; this criterion alone grants none.

## A finite, prospective observable without an all-order tail claim

For any fixed settings a_i,b_j and positive weights p_i,q_j summing to one,
let M_ij=sqrt(p_i) C(a_i,b_j) sqrt(q_j). Quantum vector factorization gives
||M||_*<=1, since its two factor matrices have Frobenius norms at most one.
For any fixed real matrix S with operator norm at most one,

    |sum_(ij) sqrt(p_i q_j) S_ij C(a_i,b_j)| <= 1.

This is a bounded linear correlation witness, valid for arbitrary quantum
binary correlations on those settings, without the candidate law or fair
marginals. For a predeclared candidate kernel G and matching grids, a sign
matrix of sqrt(p)G sqrt(p) makes its candidate value V times the weighted
trace norm. Finite trace-norm success is necessary, not generally sufficient
for a finite table's quantum membership. It does not prove the continuum
absolute-sum criterion from a finite sample.

The prospective numerical check uses only the already specified mathematical
k*=sqrt2[atanh(1/sqrt2)-atanh(1/2)]. Before evaluation, fix Gauss-Legendre
polar orders4,8,12 with2n+1 uniformly spaced azimuths; use their normalized
product weights. Check candidate visibilities .9,.95,1 and the cosine control.
The largest grid is the declared final grid, not whichever gives the preferred
value. Directions, weights, candidate matrix and witness coefficients are
preserved. Quantize the computed sign matrix to integers and certify its
operator-norm upper bound by exact integer row sums of S^T S before using
the witness. Candidate expectation evaluation remains numerical unless an
independent interval bound is supplied. This is a proposed future observation,
not a result from any real apparatus.

Vector-factorization and Clifford ingredients are standard; see the primary
[Tsirelson paper](https://www.mathnet.ru/eng/znsl4332) and the existing pinned
composition source packet. The normalized harmonic spectral and trace-norm
argument is written in full here for checking. Independent review is pending.
