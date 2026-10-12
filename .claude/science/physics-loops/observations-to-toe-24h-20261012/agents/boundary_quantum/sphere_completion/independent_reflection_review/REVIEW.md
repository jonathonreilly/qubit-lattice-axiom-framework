# Independent reflection-witness check

2026-10-12. Focused conditional mathematics and arithmetic review. No formal
audit, apparatus claim, empirical test, novelty claim, or original sphere
classification disposition is supplied.

**Core mathematics and certificate: PASS.** The reflection bound, diagonal
normalization, degree-three factor, derivative estimate, rational enclosure,
coefficient sampling and reported conservative sample counts are correct.
One sampling-premise clarification, R1 below, is required before treating the
current note's entire error claim as an unambiguous reusable statement.

## Reviewed source identity and coverage

Complete new source read:

- `DIRECT_REFLECTION_WITNESS.md` — SHA256
  `9cc364844c1782d7119d635896cd4a8efe8aaae9b398e0ea622847eb4d34fa65`.
- `direct_reflection_check.py` — SHA256
  `225caf4c2bf1d1c2a9e89614ca922cfc07e47aaf21c88f7ece9fed87c1850d4d`.

The reused arithmetic source `sphere_certificate.py` has SHA256
`03c20ec6781b25aea43bafe8fdc75497a7e9e17c40d6a74efc950c7f10911570`.
Coverage of that file is specifically its constants, guard, rational output,
alternating arctangent/Machin pi enclosure, IV arithmetic, polynomial
evaluation and sine/cosine/exponential enclosures. Its old `certify_a3`, tail
certificate, numerical scans, contour calculations and original full theorem
are not premises of this review and receive no disposition.

Runtime inputs are `quantum/direct_reflection/FREEZE.json`, SHA256
`f3bb957def74411ad2a70848807b8c06db19378f385cd3ae24ada977dcd71223`, and
`RESULTS_v1.json`, SHA256
`a911495b6d1f60b48334d03346c45393911031bead3288c2e0c1aad2e7b25ea9`.
Both were read completely. The source bindings agree. The independent run
rechecked these original source hashes before accepting its results.

## Reflection and diagonal term

Purification and realification yield bounded strongly measurable vector
functions u and v in a separable real Hilbert space; weakly measurable local
operator families also suffice under the separability premise. Their L2 norms
are at most one. The degree-three orthogonal projection extends componentwise
to the vector-valued L2 space. Its kernel under normalized sphere measure is
`7 P3(a dot b)`. Hence `S = I - 2 Pi3` is an isometry and

    -<u,Sv> = - integral C(a,a) dmu(a)
              +14 double_integral P3(a dot b) C(a,b) dmu(a)dmu(b).

Its absolute value is at most one by Cauchy-Schwarz. This uses the actual
same-setting observable term and does not equate a trace with an arbitrarily
chosen diagonal representative of a product-L2 kernel. The maps u and v
make the diagonal scalar product measurable and bounded. Fair marginals and
isotropy are unnecessary for the bound.

For an isotropic candidate, the double integral of `P3 f` is `a3/7`. Therefore
the general candidate formula is `V [f(1) - 2 a3]`; `f(1)=1` gives the stated
formula. Both signed-polynomial controls correctly distinguish normalized
and unnormalized diagonals. No absolute summability or all-order tail theorem
enters this witness.

## Analytic derivative and enclosure checks

For `g=(u+t)/(1+ut)` on the unit square, direct differentiation gives

    g_u  = (1-t²)/(1+ut)²,       g_t  = (1-u²)/(1+ut)²,
    g_uu = -2t(1-t²)/(1+ut)³,    g_tt = -2u(1-u²)/(1+ut)³,
    g_ut = -2(u+t)/(1+ut)³.

These establish the claimed bounds 1, 1, 2, 2, 4. With `u'=-a`,
`a=2/pi<2/3`, `|t'|<=k`, and `|t''|<=k+2k²`, the chain rule gives
`|g'|<=7/6` and `|g''|<=91/18` for every `0<=k<=1/2`.

For `H=P3(cos(theta)) sin(theta)`, differentiation gives

    H'' = P3''(c) sin³(theta)
          -3 P3'(c) sin(theta) cos(theta) - P3(c) sin(theta).

The bounds `|P3|<=1`, `|P3'|<=6`, `|P3''|<=15`, and
`|sin(theta) cos(theta)|<=1/2` give `|H''|<=25`; `|H'|<=7` also holds.
Consequently the slightly sharper combined bound is
`91/18 + 2*(7/6)*7 + 25 = 835/18 < 48`. Symbolic differentiation checked
all five g identities and the H identity independently. Endpoint smoothness
holds in this theta parametrization because `1+ut>=1`; the inverse-hyperbolic
form's apparent endpoint singularity is not used in this derivative estimate.

The positive atanh series has tail bounded by
`x^(2n+1)/[(2n+1)(1-x²)]` for `0<=x<1`. Integer-square-root bracketing and
outward division place both arguments in this domain, and the resulting k
interval lies strictly between zero and one half. The Machin pi enclosure
uses valid adjacent alternating-series partial sums. Its exact tangent
identity was separately checked. Fixed-point floor and ceiling directions,
negative multiplication corners, positive-denominator division, and Horner
interval propagation are correct.

The reused sine polynomial extends through degree 25, so including the next
zero coefficient gives remainder `2^27/27!`; cosine through degree 24 has
remainder `2^26/26!`. All midpoint arguments are positive and below 2. The
exponential polynomial through degree 24 has a nonnegative omitted tail at
most `3/25!` for `0<=x<1`. The new code enforces that exponential domain.
Using `e<3` is justified by the elementary exponential series. The exact
rational midpoint value of u cancels pi correctly. Every enclosure operation
therefore contains the same exact k and midpoint integrand despite repeated
interval dependencies.

The composite midpoint remainder is `7*48*L³/(24 n²)`, with `L=pi/2<11/7`.
For 2048 panels its rational upper bound is exactly `1331/102760448`.
The supplied negative a3 interval and its witness endpoints follow with
correct signs. This is a certificate using explicit analytic bounds, not
promotion of an mpmath integral to proof.

## Independent implementation and controls

The adjacent `independent_reflection_check.py` imports no author helper. It
uses Fraction endpoints at scale `10^45`, 180 atanh terms with a separate
uniform tail, 60/18-term alternating arctangent brackets, Taylor recurrences
through sine degree 33, cosine degree 32 and exponential degree 32, and a
different polynomial association. The same declared 2048-panel grid is kept.
Its independent rational a3 enclosure is

    [-0.0533073190610549226132153793826198545424085992653061224489796...,
     -0.0532814141525827446795419099940467715899746407346938775510204...].

This entire interval is inside the author's published interval. At V=19/20,
the independent lower endpoint is

    B >= 1.05123468688990721489112962898868886602095181739591836734694... .

The author's slightly weaker exact lower bound
`1.05123468688990720817613836399686861439531449...` is therefore independently
certified. Rational numerators and denominators, rather than the displayed
decimal ellipses, are the actual evidence.

A separate GL4 by nine-azimuth control grid exactly integrates products of
harmonics through degree three in the analytic quadrature rule. The numerical
degree-three projector error was `1.80e-16` and reflection-square error
`7.07e-16`. The cosine and positive-P3 quantum controls saturate B=1. At
eta=1/4, V=3/4, the normalized signed polynomial gives B=9/8, whereas the
unnormalized version gives B=15/16, as predicted independently. The largest
control error was below `1e-14`.

## Sampling coefficient, memory premise, and sample count

The primitive `5c^4/8 - 3c²/4`, evaluated at 0, 1 and `sqrt(3/5)`, gives
`integral_-1^1 |P3(c)| dc = 13/20` exactly. Thus `J=1+7*(13/20)=111/20`.
The first branch coefficient satisfies `(20/111)J=1`. The second satisfies
`(91/111)J*(20/13)=7`; uniform relative azimuth and the normalized-sphere
factor `dc/2` convert this to the required coefficient 14. Its c density
integrates to one. Rotational invariance makes both local marginals uniform.
No branch-dependent observable or branch-conditioned source is allowed.

Under fresh joint settings independent of the source conditionally on the
past, and one local setting map across branches, each quantum conditional
mean is at most one. The conditional range width is 2J, giving the stated
martingale Hoeffding exponent `-N epsilon²/(2J²)`.

**R1 — clarify the alternative's conditional mean.** The lower-tail error
guarantee under the alternative requires

    E[Z_i | past] >= 1+Delta for every included trial,

or an explicit iid/stability assumption implying this. A fixed unconditional
mean alone does not suffice under source memory: a random bias shared by an
entire run can leave a nonvanishing lower-tail probability as N grows. The
current phrase “stipulated stable alternative” should state this exact
premise. The parent has agreed to make a narrow note-only clarification;
that future source has not yet been reviewed in this receipt.

With that premise, threshold `1+Delta/2` gives each error bound at most
`exp[-N Delta²/(8J²)]`. The source proves `ln(100)<5` using an exact positive
partial sum for e^5. The reviewer exactly reproduced
`ceil(40 J²/Delta²) = 469373` for V=19/20 using the author's weaker certified
gap, and 108502 for V=1. The adjacent integer fails the stated coarse
inequality, so these are the correct ceilings for that conservative rule.
These counts do not cover apparatus uncertainty, missed detections, setting
leakage, selected coincidences, or deviations from the conditional premises.

## Evidence and limits

The independent command was `/usr/local/bin/python3` followed by the adjacent
checker path; it exited zero in about six seconds. Full rational results and
source hashes are in runtime `independent_reflection_review/CHECKS_v1.json`.
The checker writes only its assigned review directory and refuses to
overwrite its result. No author source, campaign process or observed dataset
was changed. A source-bound receipt accompanies this report. R1 needs final
note confirmation; no arithmetic rerun is indicated by that wording change.
