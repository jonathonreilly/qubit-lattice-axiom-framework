# Independent reconstruction of the smooth-winding entropy proof

2026-09-21. The complete proposed proof was read at SHA-256
`dbd07eca8db76c58f672791aa0f20b8483886352d79638931702306518b829b4`.
This reconstruction and the accompanying controls precede access to any
author smooth-time checker or result. The exact rates and flux/entropy
algebra are reused from the separately sealed nonlinear packet at the
identities in `PRE_COMPARISON_SOURCES.json`.

**Assessment:** the conditional theorem follows by the stated argument.
No missing scale factor, conditional-measure assumption, block-geometry
obstruction or entropy cancellation was found. This conclusion requires the
fixed winding matching, fixed positive rate floor, fixed smooth interior
solution and relative-entropy initial preparation. It does not establish
existence of that solution, preparation by formation, or a moving-geometry
extension.

## 1. Uniform-reference stationarity and dissipation

The swap preserves all color counts, so every homogeneous product law has
the same weight before and after an event. For a directed route channel the
drive changes sign under swapping its endpoints. Summing the four-context
drive around a route gives zero: the two nearest-neighbor S sums are shifts
of one another, as are the two next-nearest-neighbor sums. Consequently the
stationary incoming and outgoing weights agree after summing channels.
Detailed balance of the driven generator is not required.

For any density f relative to invariant uniform pi, write g=sqrt(f). With
microscopic rates r, stationarity and log z<=2(sqrt(z)-1) give

    d_t H(mu_t|pi)
      = N sum_eta pi(eta) f(eta) sum_e r_e(eta)
                                      log[f(eta^e)/f(eta)]
      <= -N sum_e E_pi r_e(eta)[g(eta^e)-g(eta)]^2
      <= -2 N r_* D_N(g).

The equality between the two square terms uses stationarity, not pairwise
reversibility. With the source's D_N=(1/2)sum E_pi(diff)^2, the coefficient
is exactly -2 N r_*. Since H(mu|pi) is between zero and K log14 on the
finite color space, integration gives the displayed K/N bound on total
bare Dirichlet energy for arbitrary initial laws. Zeros of f are harmless
in the finite-state integrated inequality by adding a small stationary
uniform component and passing to a limit.

This use of pi does not require irreducibility across different global
counts. That distinction matters later: a Poincare inequality is used only
inside a fixed block count sector.

## 2. Blocks, conditional measures and the one-block step

The columns g0=-2e1, g1=e2-e1, g2=e3-e1 have determinant -2 and generate
exactly the even-parity sublattice. Every black integer vector x has
coordinates r1=x2,r2=x3,r0=-(x1+x2+x3)/2. For N>8 ell the image of
`{0,...,ell-1}^3` embeds in the periodic lattice with m=ell^3 distinct sites.
The three actual bare swap families make this block a connected rectangular
grid. On every fixed count sector, adjacent swaps along a spanning tree
generate every color arrangement. The uniform conditional measure is
therefore invariant and irreducible, so its finite-state Poincare gap is
strictly positive. There are finitely many sectors for fixed ell; sectors
with a single arrangement have identically zero variance. A positive
minimum g_ell exists, without a claimed bound uniform in ell.

The conditional distribution used here is pi given the exterior and block
counts. It is uniform on the allowed block arrangements. It is not the
conditional law of mu. To see the precise estimate, let V have zero mean
under each of these pi-conditionals, and let m_g=E_B g. Then

    E_mu V = E_pi V(g^2-m_g^2).

Conditional Cauchy-Schwarz and
`E_B(g+m_g)^2 <= 4 E_B f` give

    |E_mu V| <= 2 ||V||_infinity
                 sqrt[E_pi Var_B(g)]
             <= 2 ||V||_infinity g_ell^(-1/2)
                 sqrt[E_pi D_B(g)].

The second averaging Cauchy-Schwarz uses E_pi f=1. No conditional
uniformity of mu has been assumed, and f need not be conditionally
normalized. This resolves the potentially delicate conditional-measure
point in the proof.

Each global internal bare edge lies in at most O(m) translated blocks.
Thus summing the last display over all K origins and integrating time
gives

    C sqrt(K/g_ell) sqrt(T integral sum_u E_pi D_(u+B)(g_t) dt)
      <= C K sqrt(T m/(N g_ell)).

The dependence on ell is allowed because ell is fixed before N tends to
infinity. Context-dependent actual rates outside a block cause no problem:
only their uniform lower bound is used to control these internal bare
swaps by the global dissipation.

For the current replacement, the five route vectors in block coordinates
are (1,0,0),(0,1,0),(0,0,1),(1,-1,0),(1,0,-1). Requiring all four sites
`r-a,r,r+a,r+2a` to remain inside the block loses a boundary fraction at
most C/ell. Every remaining stencil has four distinct sites. Under the
uniform count-conditional law, its colors are draws without replacement
from m labeled positions. Couple them with four draws with replacement;
the probability of a repeated index is at most 6/m. Since the current is
bounded, this changes its expectation by at most C/m. This is valid for
all count vectors, including monochromatic sectors and zero empirical
color probabilities. The with-replacement expectation is exactly
F_delta(pbar)/2 by the already checked homogeneous-current formula.

Apply the conditional estimate to the difference between the internal
block current average and its count-conditional expectation. Averaging
translated blocks, and translating a deterministic smooth coefficient
between origins and current anchors, produces only C ell/N additional
relative error. This proves the expectation-level replacement remainder

    sup_(t<=T) |R_(N,ell)(t)|/K
      <= C_T(1/ell+1/m+ell/N)+C_(ell,T)/sqrt(N).

It is not a pathwise replacement identity, nor is one needed in the
entropy calculation. The smooth weighted indicator-to-block-average
replacement is deterministic, by reindexing the same translated sum,
and costs C K ell/N.

## 3. Relative entropy and the tangent cancellation

Let theta=log p and h=H(mu|nu), with nu the supplied product profile. The
exact decomposition is

    h'=H(mu|pi)' - N E_mu L_N sum_u theta(u/N).I_u
                   - E_mu sum_u theta_t(u/N).I_u.

Dropping the nonpositive first term is legitimate; its integrated energy
bound has already been used in the independent one-block estimate. The
exchange difference of the log product density is
`[theta(w/N)-theta(u/N)].(I_u-I_w)`. Taylor expansion of this deterministic
coefficient costs O(K/N) after the Euler factor N, since channel lengths
and rates are uniformly bounded and there are O(K) channels. This verifies
both the sign and the scale in the source's entropy production estimate.

Replacing the current and indicator in the integrated inequality, and using
`(1/2)sum a_delta tensor delta=I`, gives the sum of

    -sum_j partial_j theta . F_j(pbar) - theta_t . pbar.

Expand in z=pbar-p, which is always tangent to mass one. The constant
theta_t.p is zero. The remaining constant term is the divergence
`sum_j partial_j(theta.F_j-q_eta,j)`, since
`dq_eta,j=grad eta . dF_j` and the species-total flux is zero. Its periodic
integral is zero. The normalized black-lattice Riemann sum has error
O(1/N), so the unnormalized sum costs O(K/N). The normalization K=N^3/2
does not introduce an extra factor: the black points have density one
after normalization by their own number. For example, pairing opposite
parities in the e1 direction bounds the difference from the full-lattice
Riemann sum by C/N.

For the linear coefficient, p_t=-sum_j A_j partial_j p and
theta_t=H_eta p_t. Both z and each partial_j p are tangent. The already
checked tangent symmetry of H_eta A_j therefore gives

    z^T [theta_t+sum_j A_j^T partial_j theta]=0.

The bracket need not be zero as an ambient fourteen-vector. Its constant
all-ones component is irrelevant because z has zero sum. An exact rational
control below deliberately has a nonzero constant ambient remainder.
Requiring componentwise zero would have been an erroneous stronger step;
the source correctly uses only tangent cancellation.

The remainder is bounded by C sum |pbar-p|^2 because F is a fixed cubic
polynomial and theta and its derivatives remain bounded on the given
smooth interior profile. The Taylor segment may meet a boundary empirical
distribution: polynomial derivatives of F are still bounded on the closed
simplex. No logarithm of the empirical pbar is taken.

## 4. Exponential estimate and the order of limits

For m independent, possibly nonidentically distributed categorical
observations, each coordinate average satisfies
`P(|pbar_a-qbar_a|>r)<=2 exp(-2m r^2)`. If
`m |pbar-qbar|^2>s`, at least one of fourteen coordinates has square
greater than s/(14m). Hence

    P(m |pbar-qbar|^2>s) <= 28 exp(-s/7).

For Y=m |pbar-qbar|^2, tail integration gives

    E exp(Y/14) <= 1+(28/14)/(1/7-1/14)=29.

For completeness, the Bernoulli exponential estimate requires no theorem
import: the second derivative of
`log(1-p+p exp(t))-p t` is q(t)(1-q(t))<=1/4, and the function and its first
derivative vanish at zero. Integrating gives t^2/8. Independence adds these
log moment bounds; Chernoff optimization and the two tails give the
coordinate inequality above.

No independence between the fourteen coordinates is needed, only
independence across sites. This estimate is uniform even at degenerate
site laws; the actual deterministic reference profile is interior.

Two translated blocks overlap only if their displacement is in B-B.
Its cardinality is at most (2ell-1)^3 on the finite torus, including any
periodic coincidences. Thus the overlap graph has a proper coloring using
at most (2ell-1)^3 colors, and exactly chi=8m slots may be used by adding
empty classes. Blocks in each class are disjoint and independent under nu.
This avoids any false assumption of an exact periodic tiling when ell
does not divide N.

Holder over the chi classes and the inequality
`|pbar-p|^2 <= 2|pbar-qbar|^2+2|qbar-p|^2` give

    log E_nu exp[alpha sum_u |pbar_u-p_u|^2]
       <= K log29/(8m)+C alpha K ell^2/N^2,

because alpha=1/224 makes `2 alpha chi=m/14`. The deterministic mean
shift is O(ell/N). The entropy inequality then bounds the expected sum
of squares by

    h/alpha+K log29/(8m alpha)+C K ell^2/N^2.

Most significantly, the coefficient 1/alpha of h is independent of ell.
Combining the inequalities yields the stated integrated Gronwall bound.
First hold ell fixed and take N through even values tending to infinity;
the dissipation replacement error C_(ell,T)/sqrt(N) vanishes regardless of
how small the fixed finite gap g_ell is. Then take ell to infinity. There
is no simultaneous unproved gap scaling in this order of limits.

This proves `sup_(t<=T) H(mu_N(t)|nu_N(t))/K ->0` from its initial version.
It gives a qualitative theorem; neither a uniform quantitative rate nor
microscopic total-variation convergence is inferred.

## 5. Uniform-time empirical conclusion

A bounded smooth-test empirical average under nu has exponentially small
fixed-deviation tails at each time by the sitewise Bernoulli exponential
bound. The entropy event inequality with h=o(K) transfers that fixed-time
concentration to mu. The deterministic mean converges by the black-lattice
Riemann sum.

The entropy event inequality itself follows by coarse-graining to the
indicator of the event: binary relative entropy is at least
`mu(A) log(1/nu(A))-log2`. Thus the exponentially small product probability
and o(K) entropy suffice, without total-variation closeness of the full laws.

For the actual process, one local exchange changes the normalized smooth
average by at most C/(N K). There are O(K) bounded-rate microscopic
channels, accelerated by N. Its martingale bracket is at most C_T/(N K)
and its drift is bounded uniformly by C. Doob's inequality removes the
martingale uniformly in time. A fixed finite mesh, the bounded drift,
and continuity of the target profile upgrade the fixed-time probability
limits to the asserted supremum over [0,T]. No pathwise version of the
one-block replacement was silently used here.

## 6. Independent finite controls and scope

The accompanying standalone checker uses no author-code imports. It
assembles the complete 14^4-state process on one actual four-anchor
N=8 route cycle with gamma=2/3,k0=5/2. Integer incoming/outgoing rates
balance exactly. It verifies the entropy dissipation normalization and
the exact inhomogeneous-reference entropy decomposition for a positive
correlated density. All count sectors are retained in the conditional
variance calculation. Exact bare four-cycle gaps are computed for every
count partition of four; relabeling covers all fourteen-color count
sectors. This finite cycle is a control of the identities, not a substitute
for the general rectangular-block argument.

A preserved countercontrol takes a density depending only on the number
of one color. Its swap Dirichlet form is zero, while the expectation of
the incorrectly grand-canonically centered observable is 13/252. This
tests why conditional count-sector centering is essential. The correctly
centered bound holds in the direct control.

Separate periodic block checks use (N,ell)=(24,2),(40,4),(48,5),(80,9),
including nondivisible sizes. They verify embedded sites, actual internal
edges, edge multiplicities, overlap degrees and all five four-context
boundary losses. Exact symbolic controls check the nonzero ambient but
zero tangent entropy coefficient, the entropy-divergence constant term,
alpha=1/224 and the integrated tail constant 29. A nonidentical categorical
law and canonical count boundary cases test the probability estimates.

The complete first execution succeeded. Its source, versions, full stdout,
empty stderr, results and command receipt are retained. No failed attempt
was discarded. The finite controls only check selected identities and
normalizations; the general assertions rest on the arguments above.

All conclusions concern the closed fourteen-color projection with its
fixed winding geometry. They require the supplied C3 interior solution
on a fixed finite time interval and the o(K) relative-entropy preparation.
They establish neither that births produce this initial law, nor a
hydrodynamic theorem for arbitrary matching geometry, moving geometry,
shocks, boundary densities, microscopic keys beyond the color projection,
or a quantum or spacetime interpretation.
