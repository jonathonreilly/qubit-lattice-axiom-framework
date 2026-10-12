# Separate narrow checks: Lorentz promotion, angular cusp, and knot wording

2026-10-12. Independent mathematical checking of the three assigned notes and
the resource-check script. No author files were edited. No actual galaxy fields,
empirical fits, sphere-classification certificate run, or formal audit was done.

## Disposition and source identity

No material mathematical error was found in either narrow proof under its
declared assumptions. The static-knot wording fix resolves the earlier
qualification. These checks do not establish a healthy covariant completion,
a universal resource lower bound, or the pending full-sphere classification.

| Subject | SHA-256 |
| --- | --- |
| DIRECT_STATIC_ACTION.md, narrow wording fix | `2115ad64153b021607f3d10e3aa9141c7d8655bc908826d4c69b95f3c41a7d4b` |
| DIRECT_COVARIANT_PROMOTION_FAILURE.md | `e1e3d164d6872e7000ba127482734eba1e5d9595ef3ec204c62964ffd2396dbb` |
| DIRECT_RESOURCE_OBSTRUCTION.md | `9148b9dad4108abb58f6e725f374e19358d4b203645277452685095f897bc9ec` |
| direct_resource_check.py | `76144b6684cd2c1aac48550a152b9eb0d8a35f4387e04a3c75e96ca27a79f992` |

The exact snapshots and static wording diff are preserved here. The construction
in section 7 of SPHERE_THEOREM.md was read as context at hash
`3ee37c5af31847807decf92360c04f851d3c280bd809dcf63db609ac51d8a1e5`.
That context hash is not a review disposition of its classification, contour,
threshold, or certificate arguments. The new resource theorem assumes a positive
normalized Legendre expansion and does not require that numerical threshold.

The author's resource receipt
`quantum/direct_resource/resource_check_v1.json` has SHA-256
`bfec157f52e23ac23ff5834a2672da9400d81df0380b1fc1f078a10d8200f47e`.
Its source and note hashes match the subjects above. It is supporting finite
evidence, not the proof of the all-order obstruction.

## Two independent Lorentz scalars

With signature `(-,+,+,+)` and the prescribed smooth continuation through zero
gradient, `F'(0)=N0`. Quadratic time derivatives therefore give the symmetric
matrix `K=[[0,1],[1,-N0]]` with determinant `-1`. Its eigenvalues have opposite
signs because their product is negative, independently of N0. The velocity
Hessian is `2 C K`, whose determinant is `-4 C^2<0` for real nonzero C.
It has full rank, so the declared unconstrained two-field model has no primary
velocity constraint that would remove either mode.

An independent Legendre transformation gives

    p = 2 C K dot q,
    K^(-1) = [[N0,1],[1,0]],
    H_kin = [N0 p_X^2 + 2 p_X p_Y]/(4 C).

Choosing `p_X=1` and `p_Y=(-N0+1)/2` or `(-N0-1)/2` yields opposite energy
signs `+1/(4C)` and `-1/(4C)`. An overall sign flip cannot make both positive.
Algebraic source and mass terms leave this velocity Hessian unchanged. Higher
terms in a smooth F near zero begin beyond the quadratic fluctuation action
and do not repair its local kinetic signature.

The field-redefinition statement has its usual precise scope: an invertible
real point-field transformation induces a nonsingular Jacobian congruence on
the quadratic kinetic form, and Sylvester inertia preserves its sign counts.
A transformation that adds derivatives, constraints, or gauge structure would
require a different analysis and is outside the minimal two-derivative,
unconstrained promotion being rejected. The note does not exclude those other
completions or modified gravity generally.

The static D condition controls a spatial constitutive term; it cannot alter
`det K=-1`. Rejecting this candidate as a positive-energy completion is supported.
No observational exclusion follows from that local mathematical failure.

## Conditional angular-cusp resource theorem

The cited Laplace integral is consistent with the order-zero specialization of
[NIST DLMF 14.12.7](https://dlmf.nist.gov/14.12.E7). For integer degree, the
formula is a polynomial identity, so continuation to `x=cos(theta)` has no
fractional-power branch ambiguity. Independently, summing its finite-power
integrands against a small generating parameter gives
`(1-2t cos(theta)+t^2)^(-1/2)`, the Legendre generating function.

Set `z=cos(theta)+i sin(theta)cos(phi)`. Both `|z|` and `|partial_theta z|`
are at most one. Differentiating its finite integer power inside the integral
therefore gives `|partial_theta P_l(cos(theta))|<=l` for `l>=1`; `l=0` is
constant. Together with `P_l(1)=1` and `P_l<=1`, this yields

    0 <= [1-P_l(cos(theta))]/theta <= l.

Each fixed polynomial contributes a ratio tending to zero. If `sum l*a_l`
were finite, that upper bound would be an integrable dominator on the discrete
positive measure with masses `a_l`. Dominated convergence would then force the
full ratio to tend to zero, contradicting a positive cusp slope. This proves
the first-moment divergence without differentiating an infinite series.
Normalization and `|P_l|<=1` justify the original uniformly absolutely convergent
expansion and the expression for `1-f`.

In the specified direct-sum pure state, distinct partner sectors are orthogonal.
Taking the partial trace kills their cross terms and gives
`rho_A=direct_sum_l a_l I_(2^l)/2^l`. Its entropy is therefore
`sum[-a_l log a_l + a_l*l*log(2)]`, in the extended nonnegative sense. Every
summand is nonnegative, so divergence of the first moment forces infinite
entropy without an infinity-minus-infinity ambiguity. A positive local energy
with sector expectation bounded below by `epsilon*l` similarly has infinite
expectation. That energy conclusion uses the explicit Hamiltonian premise;
the pair law does not determine such a Hamiltonian.

For the conditioned family, algebra gives the useful stable identity

    1-f = (1-u)(1-t)/(1+u*t),
    u=1-2 theta/pi,  t=tanh(k cos(theta)).

Dividing by theta and taking the one-sided limit directly gives
`(2/pi)exp(-2k)>0` for every finite k. This calculation makes no claim that all
such k have nonnegative Legendre coefficients. The theorem applies only when
the positive normalized expansion premise holds. It concerns the specified
harmonic/Clifford realization, not the entanglement cost of every possible
realization or a universal quantum no-go. The zero cusp slope of `f(c)=c`
is consistent with its stated exemption.

## Exact benchmark and finite-accuracy escape

Independent monomial integration gives, for integer m>=0,

    integral_-1^1 (2/pi) asin(x) x^(2m+1) dx
       = [1-C_(m+1)]/(m+1),
    C_n = binomial(2n,n)/4^n.

Combining this with the exact Rodrigues polynomial coefficients reproduces
`a_(2n+1)=C_n^2-C_(n+1)^2`; all even coefficients vanish. This is a separate
route from the author's Legendre-derivative integration by parts and its
numerical quadrature.

The central-binomial bound used for the tail follows by induction because

    (n+2)(2n+1)^2 <= 4(n+1)^3,

whose right-minus-left difference is `3n+2`. Hence `C_n^2<=1/(n+1)` and
the telescoping limit vanishes. The tail above `2N+1` is exactly
`r_N=C_(N+1)^2`. Moving that mass to the l=1 sector preserves positivity and
normalization. The correlation change is a sum of tail weights multiplying
`P_1-P_l`, with magnitude at most two per term, proving the uniform bound
`2r_N<=2/(N+2)`. A finite number of finite-dimensional sectors has finite
entropy and, with finite stipulated sector energies, finite energy. This
changes the required approximation tolerance, not the exact law's weights.

Summation by parts gives the stated exact partial first-moment identity. Its
finite numerical growth is a consistency check; the divergence claim relies
on the preceding dominated-convergence argument, not extrapolation of that
growth.

## Independent execution and wording fix

`check_narrow_proofs.py` imports no author computational helpers. It verifies:

- kinetic inverses, momentum/velocity Legendre transforms, and explicit
  opposite-energy directions using exact rationals for five N0 values and two
  common action signs;
- exact equality of the expanded Laplace integral and Rodrigues polynomials
  through degree 34;
- exact arcsine Legendre coefficients for degrees 0 through 24 and additional
  degrees 31, 41 and 51, using the independent monomial moments above;
- exact normalization, tail, partial-moment and conservative-bound identities
  at N=0,1,7,31,128, plus agreement with the author's ten recorded coefficients;
- cusp identities at k=0,.17,1,3 with relative finite-angle error below
  `3.18e-17`, without asserting positivity at those parameter values;
- finite-accuracy examples at N=0,1,4,16,32, all within the analytic uniform
  bound, and a 42-dimensional truncated pure-state partial trace whose entropy
  `1.4812871955552385` agrees with the sector formula to floating precision.

These light controls took 0.013 seconds with peak resident memory 36,634,624
bytes and one-thread settings. They support, and do not replace, the all-order
arguments reviewed above.

The static note's three changed passages now restrict the classical Hessian
to points away from response knots, state its one-sided interpretation and
continuous gradient at joins, and restrict strict Jacobian positivity to smooth
intervals. The equations, weights, and D condition are unchanged. This resolves
the earlier wording qualification at the fixed-note hash above.

The runtime receipt pins this report and all evidence. The pending full-sphere
classification and actual inverse-field validation remain separate obligations.
