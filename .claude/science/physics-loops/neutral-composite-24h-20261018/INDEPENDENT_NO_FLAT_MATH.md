# Exact no-flat-transition certificate — independent mathematical review

Reviewed `probes/exact_no_flat_transition.py` and its JSON certificate in the current neutral-composite pack. The proposed inference is valid for the **exact decimal-rational candidate**, fixed Q=(pi,pi,pi), the infinite translation-invariant lattice, and square-integrable bilinear sources with the momentum-space metric specified below. It does not require analytic choices of individual eigenvalue branches.

## Operator and analytic argument

The finite-range Hermitian Bloch matrix h(k) is a trigonometric polynomial. On a vectorized 12x12 bilinear amplitude M(k), the fixed-Q Liouvillian is

    L_Q(k) = I_12 tensor h(k+Q) − h(k)^T tensor I_12,

for column vectorization; equivalently it acts as h(k+Q)M−Mh(k). It is a 144x144 Hermitian matrix for real momenta. Its entries, and therefore

    D_omega(k)=det[L_Q(k)−omega I],

are real analytic on the connected three-torus for each fixed real omega. A nonzero real-analytic function has a zero set of Lebesgue measure zero. Consequently a positive-measure zero set forces D_omega to vanish identically.

The direct-integral Hilbert-space operator is multiplication by L_Q(k) on L2(T^3,C^144). If a square-integrable source has a spectral atom at omega, then

    integral ||P_omega(k) M(k)||² dk > 0,

so ker[L_Q(k)−omega I] is nontrivial on a positive-measure momentum set. The analytic argument forces D_omega(k)=0 for every k. In particular omega must be a common root of the characteristic polynomials at the two selected momenta.

Thus exact coprimality of those two polynomials excludes **every real omega atom** for every such source. Indeed it excludes any point eigenvalue of the full direct-integral bilinear Liouvillian. Band crossings and nonanalytic individual eigenvector/eigenvalue labels do not affect this determinant proof.

## Why the modular reduction proves exact coprimality

At each supplied point, exp(ik_j)=(a_j+i b_j)/c_j with a_j²+b_j²=c_j². Hence both h and L_Q have entries in Q(i), because the JSON decimal tokens are parsed as exact rational numbers. Negative phase powers also lie there; these are nonzero unit-circle numbers.

It is important to say **ring reduction**, not a field embedding Q(i)->GF(p). There is no unital field homomorphism from characteristic zero to characteristic p. Choose a localization

    R=Z[i,1/D],

where D contains all input and phase denominators. For p=1009 or1013, p=1 mod4, choose a root i_p²=−1 in GF(p). The map i->i_p and rational denominators->their modular inverses defines a ring homomorphism R->GF(p), because p does not divide D. A phase numerator a+i_p b cannot vanish here: its product with a−i_p b equals c²!=0 mod p.

The two characteristic polynomials are monic of degree144 over R. Their reductions have the same degree. Coprimality over GF(p) means their resultant reduces to a nonzero element. Since resultant is a polynomial in the coefficients, the exact resultant in R cannot be zero. Thus the exact polynomials have no common root over the algebraic closure of Q(i), and in particular no common real root. This avoids any concern that a hypothetical common factor's coefficients might have additional denominators.

A single valid prime certificate is sufficient. Two primes provide useful computational redundancy. Newton trace identities are legal in each field because all integers1,...,144 are invertible when p>144. The trace-of-Kronecker-difference formula used by the root is the binomial expansion of two commuting factors; it requires no spectral diagonalization over the finite field.

## Independent implementation checks performed

Independent script/result:
- `/private/tmp/neutral-no-flat-check/check.py`
- `/private/tmp/neutral-no-flat-check/result.json`

Checks completed:
1. Candidate byte hash agrees with the published certificate (`b4c2bc8c25dafa7c529a96f3109331924eb428d2b363ec765f66fd1efc1e0588`).
2. All 1008 stored block-entry relations B_(−s)=B_s^dagger hold as exact rational equalities, so the decimal-rational h(k) really is Hermitian, not merely close numerically.
3. Every phase triple satisfies a²+b²=c², and the required denominator reductions are invertible.
4. Independently assembled 144x144 matrices agree with each recorded characteristic polynomial at eight distinct field values, using direct modular Gaussian-elimination determinants: 32 determinant comparisons total.
5. Independent SymPy polynomial gcd computation gives degree zero for both primes.

The 32 sampled determinant comparisons are independent implementation controls, not a standalone proof of equality of two degree144 polynomials. The root's full trace/Newton construction supplies that polynomial calculation; the mathematical formulas and safe small-integer modular arithmetic were checked. Do not describe the sampled evaluations as complete polynomial interpolation verification.

## State metric and scope

The statement transfers to thermal structure-factor metrics or other positive transition weights that are absolutely continuous with respect to the same Lebesgue momentum measure and whose supported action is the same multiplication Liouvillian. Finite-temperature free weights f_a(1−f_b), zero-temperature Slater occupation weights, and positive-frequency thermal commutator weights have this property; null directions can be quotiented. Multiplying by such weights cannot place nonzero measure on a Lebesgue-null level set.

It does not cover singular momentum distributions, delta-normalized non-L2 probes, or an arbitrary stationary non-Gaussian metric without verifying its momentum-space representation. A finite momentum grid has point spectra and is not itself the infinite-volume direct-integral theorem. Nor does the proof by itself establish absolute continuity with a smooth density, a quantitative density bound, or a rate for overlap decay. No-atom suffices for the previously checked qualitative residual–overlap theorem at fixed source, but the sqrt(eta) filter asymptotics require additional local-density regularity.

## Limits of the conclusion

- Fixed Q only. At q=0, conserved bilinears can have exact zero-energy atoms; no all-q statement follows.
- Exact supplied rational coefficients only. If the JSON approximates a different intended analytic model, tiny rounding can lift an exact flat relation. That intended model needs its own exact certificate or a separately quantified comparison.
- No statement about a new interacting Hamiltonian, added microscopic terms, nonlinear composite sectors, or autonomous fields outside this quadratic bilinear space.
- No isolated bilinear atom at this fixed Q rules out a source-visible exact scalar-like pole there within this candidate, but not narrow resonances, long-lived approximate modes, wave packets, other momenta or other candidates.
- Finite-range and square-integrable infinite-range amplitudes are included; distributional amplitudes supported on a measure-zero energy surface are not normalizable counterexamples.

The result is a rigorous, useful fixed-candidate/fixed-momentum obstruction and avoids a blanket prohibition on free flat-band or closed-operator exceptions in other models.
