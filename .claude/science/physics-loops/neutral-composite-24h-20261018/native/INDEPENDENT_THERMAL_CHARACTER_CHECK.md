# Independent low-temperature character-mixture check

Disposition: PASS under the stated global equivariant normal-form bounds. The estimate removes dependence on a chosen flat character for this adopted low-temperature Gibbs preparation. It does not derive cooling, thermalization, or a cosmological initial state.

## Required normal-form structure

Work on the full finite physical Hilbert space, with a unitary U such that

    U H U^dagger = B + R,   ||R|| <= delta.

The required inputs are:

* B is exactly block diagonal in N, and in Q inside N0.
* The N0,Q0 projector P has dimension |G|=2^(2R-1), and B P=e_M P exactly.
* The N0,Q=q block obeys B >= e_M+g q, with g=c J lambda^4 uniformly positive.
* Every wall block N>=2 obeys B >= e_M+J (or any other fixed positive multiple of J).

These are global block/form statements, not just bounds in a single chosen plane sector or for compact few-defect vectors. The cited all-Q relative bound and wall extension are what justify their use. An operator norm estimate for a low-Q restriction alone would not suffice for the Gibbs entropy sum. Any small residual global correction to the wall lower bound can be absorbed into a fixed positive fraction of J for small lambda.

The flat block is exactly scalar only for the retained fixed-order B at sufficiently large R, before the norm remainder; the actual-H flat-derived band can split. This is consistent with the later Gibbs perturbation estimate and does not assume exact ground degeneracy.

## N0 dimension and partition bound

The column-to-plaquette syndrome map is linear over F2. Its kernel is the flat row/column flip group, so every admissible syndrome has exactly |G| column configurations. There are at most binom(R^2,q) syndromes of weight q, even though many are forbidden by row/column parity. Thus

    dim(N0,Q=q) <= |G| binom(R^2,q).

No restriction to positive X/Y character is being made in this count. The full |G| factor in the denominator is essential. Since Z_B >= |G| exp(-beta e_M), the nonflat probability in the Gibbs state of B is at most

    [(1+exp(-beta g))^(R^2)-1]
       + [2^(10R^2)/|G|] exp(-beta J).

This is a valid upper bound even though the first bracket overcounts forbidden syndromes and the second term overcounts all wall states. It is not necessary to determine their actual degeneracies.

For R~lambda^(-1), beta g=a log(1/lambda), and fixed a>2, the first term is O(lambda^(a-2)), because R^2 lambda^a tends to zero. The logarithm of the second term is at most

    10(log 2) R^2 - beta J - log|G|,

which tends to minus infinity faster than any logarithm: beta J is of order lambda^(-4) log(1/lambda), dominating the volume entropy O(lambda^(-2)). Thus the wall contribution is superpolynomially small.

Conditioned on the flat block, rho_B is EXACTLY P/|G|. Because B is block diagonal, its trace-norm distance to sigma=P/|G| equals twice its nonflat probability, not merely the probability. Consequently

    ||rho_B-sigma||_1 <= 2 O(lambda^(a-2)) + superpolynomial terms.

The factor two does not change the proposed asymptotic order.

## Gibbs perturbation and numerical exponents

For rho'=exp[-beta(B+R)]/Z' and rho_B=exp(-beta B)/Z_B,

    D(rho'||rho_B)
      = -beta Tr(rho' R) + log Z_B - log Z'.

The operator norm perturbation bound gives |log Z'-log Z_B|<=beta delta, so D<=2 beta delta without requiring [B,R]=0. Quantum Pinsker in natural logarithms yields

    ||rho'-rho_B||_1 <= sqrt(2D) <= 2 sqrt(beta delta).

With delta=C J R^2 lambda^M and the chosen beta,

    beta delta = O(lambda^(M-6) log(1/lambda)),
    ||rho'-rho_B||_1
       = O(lambda^((M-6)/2) sqrt(log(1/lambda))).

For M=20 this is O(lambda^7 sqrt(log(1/lambda))). Unitary invariance and the triangle inequality give

    ||rho_H - U^dagger(P/|G|)U||_1
       <= O(lambda^(a-2))
          + O(lambda^7 sqrt(log(1/lambda)))
          + superpolynomial terms.

At a=10 the first term is O(lambda^8), agreeing with the root. All of these are o(1/log(1/lambda)). The dimension in Pinsker does not create an extra volume factor.

## Preparation and observable scope

The flat mixture can equivalently be expressed as the uniform computational-flat mixture or the uniform mixture of all compatible character Fourier vacua. It does not select one character. The previously proved local character-independence permits the same matched neutral protocol in this mixture.

Any SAME CPTP preparation/readout channel applied to the two density matrices contracts trace distance. In particular the result survives a fixed matched state preparation and bounded-outcome measurement. A character-dependent family of protocols is not automatically one such common channel; if needed it must be defined explicitly on the full space. Postselection followed by renormalization is not trace-distance contractive and needs a success-probability bound. Likewise for an unbounded-with-volume observable, its expectation difference is bounded by its operator norm times the trace distance; one cannot silently use the trace distance as an absolute expectation error for an O(R) operator. Bounded measurement probabilities and normalized channel comparisons avoid that issue.

The adopted inverse-temperature scaling is beta~J^(-1)lambda^(-4)log(1/lambda), corresponding to a temperature below the defect scale by a logarithm. The proof supplies no dynamics that creates or maintains this Gibbs state. The actual microscopic Hamiltonian and the matched dressed protocol remain the ones already specified; no new physical interaction is introduced.
