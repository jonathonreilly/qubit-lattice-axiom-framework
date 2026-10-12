# Monotone response basis: direct solar checks

2026-10-12. Direct author calculation in this chat, following
DIRECT_RESPONSE_INVERSION_TARGET.md. This is preparation for a combined
inverse problem, not a fit, an empirical exclusion or an independent review.

For a transition interval [L,H] in physical Newtonian acceleration, define

    b(A)=1                          when A<=L,
         log(H/A)/log(H/L)           when L<A<H,
         0                          when A>=H.

The candidate response N=1+w*b with w>=0 has a bounded low-acceleration
enhancement and returns exactly to one above H. An unbounded deep-MOND tail
is a different supplied assumption; this finite basis does not derive it
from observations on finite acceleration windows.

## Regularity extension for this particular basis

b is continuous and absolutely continuous on every compact positive interval,
with -b'(A)=1/[A log(H/L)] on (L,H) and zero elsewhere. No delta functions
occur at its derivative jumps. Approximate the log-acceleration derivative
by positive smooth compactly supported mollifications. Their integrated
responses are C1 monotone functions satisfying the earlier theorem's low-
and high-acceleration bounds. They converge uniformly to b; their derivative
measures have mass one on a common compact interval away from zero.

Since W is continuous and bounded there, its integrals against those measures
converge to the displayed log-ramp integral. This supplies the limit of the
positive response formula. For the point-Sun boundary problem, the anomalous
source vanishes near the Sun where its acceleration exceeds every transition
support. At large distance, the uniform external field has only an O(r^-3)
gradient perturbation; the Hessian Green integral therefore has an integrable
tail. The bounded derivative on the compact acceleration interval supplies
domination away from the Sun. A zero-field saddle lies below the lower support,
where the response is constant. These facts give the same weak Poisson
solution and Hessian limit for this finite-knot response. They do not extend
the theorem to arbitrary discontinuous functions or arbitrary mass measures.

Put l=L/g_Ne and h=H/g_Ne. The single-column solar coefficient is

    q(L,H;g_Ne) = g_Ne^(3/2)/sqrt(G M_sun) * F(l,h),
    F(l,h) = 9/[8 log(h/l)] integral_l^h W(s) ds/s.

Linearity then gives Q2=sum w_j q_j for a finite nonnegative combination.
This converts a trial response shape into one directly testable solar output
without introducing a redundant acceleration-coordinate parameter a0.

## Actual numerical comparisons

`direct_response_basis.py` evaluates that positive one-dimensional integral,
the independent-variable two-dimensional density/Hessian expression, and
its integration-by-parts form. They are separate calculations by this author,
not separate reviewers. Angular integrations split wherever either response
knot is crossed. Radial integrations split when a knot reaches c=+1 or -1;
these points obey w^2=|eta +/- q_knot|.

| Transition [L/g_Ne,H/g_Ne] | F |
| --- | ---: |
| [0.02,0.2] | 0.0000125789143166 |
| [0.5,2] | 0.310927661815 |
| [2,5] | 0.261953243645 |
| [10,100] | 0.0845644187090 |

For each row the dummy dimensionless convention eta=0.5, 1 and 2 gives the
same physical coefficient after its eta^(3/2) scaling. At integration order
96 the largest relative difference among forms is 5.21e-11. The order-48
low-acceleration row differs by 5.23e-9. These are finite convergence checks,
not certified interval bounds. They do not use any measured acceleration or
quadrupole estimate.

The first execution failed substantially for the two intervals above the
external acceleration. It omitted the radial transition sqrt(q_knot-eta)
by clipping a negative eta-q_knot to zero. The source was corrected to split
at the absolute difference. The original source, actual failing results,
correction record and successful rerun remain in runtime gravity/ under
`direct_response_basis_v1.*`, `direct_response_basis_failure_v1.json` and
`direct_response_basis_v2.json`. No response interval or acceptance threshold
was adjusted to repair that code error.

The solar basis is now computationally checked in isolation. The actual
galaxy basis operator, its numerical convergence, source nuisances, shared
external-field identification, fit/test allocation and independent review
remain prerequisites to a combined empirical conclusion.
